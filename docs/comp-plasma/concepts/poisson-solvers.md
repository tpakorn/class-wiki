# Poisson Solvers

## Intuition

Electrostatics keeps asking one question: *given the charges, what is the potential?*

$$\nabla^2\phi = -\frac{\rho}{\varepsilon_0}$$

Discretized with the [5-point stencil](finite-difference-method.md), this becomes a
huge but beautifully structured linear system. The course solves it two ways —
**relaxation** (iterate until the grid "settles", like a stretched membrane finding
its shape) and **direct sparse solve** (one exact linear-algebra shot) — and knowing
when to use which is half the craft.

## Method 1 · Gauss–Seidel relaxation

Rearranging the stencil for $\phi_{i,j}$ turns the equation into an update rule —
each point relaxes to the average of its neighbors (plus source):

$$\phi_{i,j}^{(k+1)} = \frac{1}{4}\left(\phi_{i+1,j} + \phi_{i-1,j} + \phi_{i,j+1} + \phi_{i,j-1}
+ \frac{\rho_{i,j}}{\varepsilon_0}h^2\right)$$

Gauss–Seidel uses freshly updated neighbors immediately (unlike Jacobi), converging
roughly twice as fast; iterate until
$\max|\phi^{(k+1)} - \phi^{(k)}| <$ tolerance. Boundary (Dirichlet) values are set
once and never updated.

```python
def GS_poisson_step(phi, rho):
    for i in range(1, N-1):
        for j in range(1, N-1):
            phi[i,j] = 0.25*(phi[i+1,j] + phi[i-1,j]
                           + phi[i,j+1] + phi[i,j-1]
                           + rho[i,j]*dx**2)
    return phi
```

With $\rho = 0$ this solves the **Laplace equation** — the same PDE as
[potential flow](../../fluids/equations/laplace-equation.md) and steady heat
conduction; one solver, many physics.

## Method 2 · Direct sparse solve (1-D, periodic)

In one dimension (the [PIC](pic-method.md) setting), the stencil
$\phi_{j-1} - 2\phi_j + \phi_{j+1} = (n_j - n_0)\Delta x^2$ stacks into a tridiagonal
matrix system $A\boldsymbol\phi = \mathbf{b}$:

$$A = \frac{1}{\Delta x^2}\begin{pmatrix}
-2 & 1 & & & 1\\ 1 & -2 & 1 & & \\ & 1 & -2 & \ddots & \\ & & \ddots & \ddots & 1 \\ 1 & & & 1 & -2
\end{pmatrix}$$

The corner 1's enforce **periodic boundary conditions**. Sparse direct solution
(`scipy.sparse.linalg.spsolve`, Thomas algorithm under the hood) is exact,
non-iterative, and $\mathcal{O}(M)$ for tridiagonal systems — the right tool when you
must solve the *same* system every PIC time step.

The field then follows by a central difference:
$E_j = -(\phi_{j+1} - \phi_{j-1})/2\Delta x$, or in NumPy:
`E = -(np.roll(phi,-1) - np.roll(phi,1))/(2*dx)`.

## Choosing between them

| | Gauss–Seidel | Sparse direct |
|---|---|---|
| Nature | iterative relaxation | exact solve |
| Cost | many cheap sweeps ($\mathcal{O}(N^2)$ iterations for $N\times N$ grids) | one solve; $\mathcal{O}(M)$ tridiagonal, more in 2-D/3-D |
| Geometry flexibility | excellent (arbitrary masks/boundaries) | needs matrix assembly |
| Best for | 2-D/3-D electrostatics teaching problems, odd geometries | repeated 1-D solves in production loops (PIC) |

(Production 2-D/3-D codes graduate to multigrid or FFT solvers — same equation,
faster machinery.)

## Common mistakes

- **Updating boundary points.** Dirichlet boundaries are constraints, not unknowns.
- **Under-iterating relaxation.** Convergence is slow (error decays like
  $\sim 1 - \mathcal{O}(1/N^2)$ per sweep); check the residual, not the iteration
  count.
- **Singular periodic systems.** With periodic BCs, $\phi$ is defined only up to a
  constant and solvability requires zero net source ($\sum_j (n_j - n_0) = 0$) —
  physics (quasineutrality) and linear algebra agreeing with each other.

## Related concepts

- [Finite difference method](finite-difference-method.md) — the stencil source
- [Discrete Poisson equation](../equations/discrete-poisson-equation.md) — reference card
- [PIC method](pic-method.md) — the consumer of the 1-D solver
- [FDTD](fdtd-method.md) — the time-dependent sibling

## Knowledge graph position

**Prerequisites:** [Finite differences](finite-difference-method.md), linear algebra.
**Leads to:** [PIC method](pic-method.md).

## Quiz

**Q1 (conceptual).** Why does Gauss–Seidel converge faster than Jacobi?

??? success "Answer"
    It uses updated neighbor values *within* the same sweep, so information propagates
    across the grid faster — asymptotically it converges at twice Jacobi's rate.

**Q2 (computational).** For a 1-D periodic grid with $M = 4$ points, what is the rank
of the Laplacian matrix $A$?

??? success "Answer"
    3. The constant vector is a null mode ($A\mathbf{1} = 0$) — the potential offset
    is undetermined, so rank $= M - 1$.

**Q3 (MCQ).** In the relaxation picture, the Laplace equation drives every interior
point toward:

- (a) zero  (b) the boundary average  (c) the average of its four neighbors  (d) the global maximum

??? success "Answer"
    **(c).** That's the discrete mean-value property of harmonic functions — and the
    reason no interior extrema exist.
