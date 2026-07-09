# The Discrete Poisson Equation

## Equations

**2-D, 5-point stencil** (grid spacing $h$):

$$\boxed{\,\phi_{i+1,j} + \phi_{i-1,j} + \phi_{i,j+1} + \phi_{i,j-1} - 4\phi_{i,j} = -\frac{\rho_{i,j}}{\varepsilon_0}h^2\,}$$

**1-D, matrix form with periodic BCs** (the [PIC](../concepts/pic-method.md) field
solve, normalized $\phi'' = n - n_0$):

$$\frac{1}{\Delta x^2}\begin{pmatrix}
-2 & 1 & & & 1\\
1 & -2 & 1 & & \\
& 1 & -2 & \ddots & \\
& & \ddots & \ddots & 1\\
1 & & & 1 & -2
\end{pmatrix}
\begin{pmatrix}\phi_1\\\phi_2\\\vdots\\\phi_{m-1}\\\phi_m\end{pmatrix}
= \begin{pmatrix}n_1\\n_2\\\vdots\\n_{m-1}\\n_m\end{pmatrix} - n_0$$

**Field recovery:** $E_j = -\dfrac{\phi_{j+1} - \phi_{j-1}}{2\Delta x}$
(periodic: `E = -(np.roll(phi,-1) - np.roll(phi,1))/(2*dx)`).

## Physical meaning

Gauss's law, pixelated: each grid point's potential is tied to its neighbors and the
local charge. The matrix is the [5-point/3-point stencil](../concepts/finite-difference-method.md)
written for all points at once; the corner 1's wrap the domain into a ring (periodic
boundary conditions).

## Variables

$\phi$ — electrostatic potential · $\rho$ (or $n - n_0$) — charge (density
imbalance) · $h, \Delta x$ — grid spacing · $m$ — number of grid points.

## Structure worth knowing

- **Sparse:** 3 diagonals + 2 corners — solvable in $\mathcal{O}(m)$
  (`scipy.sparse.linalg.spsolve` / Thomas algorithm)
- **Symmetric negative semi-definite;** the constant vector is a null mode →
  potential defined up to a constant, and solvability requires
  $\sum_j (n_j - n_0) = 0$ (net neutrality — physics and linear algebra in agreement)
- Accuracy: $\mathcal{O}(h^2)$, inherited from the central stencils

## Applications

The "solve" step of every [PIC cycle](../concepts/pic-method.md) ·
[electrostatics exercises](../concepts/poisson-solvers.md) (point charge, dipole,
capacitor) · steady heat conduction · [potential flow](../../fluids/equations/laplace-equation.md)
($\rho = 0$).

## Related equations

- [Poisson solvers](../concepts/poisson-solvers.md) — Gauss–Seidel vs direct
- [CFL condition](cfl-condition.md) — why elliptic problems have no time-step limit
  (there's no time)

## Quiz

**Q1 (conceptual).** Why do the corner entries make the boundary "disappear"?

??? success "Answer"
    They connect point 1 to point $m$ exactly as interior neighbors are connected —
    topologically the grid becomes a circle with no boundary at all, matching the
    periodic domain of the two-stream simulation.

**Q2 (computational).** On a 3-point periodic grid with $\Delta x = 1$ and source
$(n - n_0) = (1, -2, 1)$, solve $A\boldsymbol\phi = \mathbf{b}$ for one valid
$\boldsymbol\phi$.

??? success "Answer"
    First check solvability: $\sum_j b_j = 1 - 2 + 1 = 0$ ✓. The three equations are
    $-2\phi_1 + \phi_2 + \phi_3 = 1$, $\phi_1 - 2\phi_2 + \phi_3 = -2$,
    $\phi_1 + \phi_2 - 2\phi_3 = 1$. Fix the free constant by choosing $\phi_1 = 0$:
    then eq. 1 gives $\phi_2 + \phi_3 = 1$ and eq. 2 gives $-2\phi_2 + \phi_3 = -2$;
    subtracting, $3\phi_2 = 3 \Rightarrow \phi_2 = 1$, $\phi_3 = 0$. So
    $\boldsymbol\phi = (0, 1, 0)$ (plus any constant) — check eq. 3:
    $0 + 1 - 0 = 1$ ✓. The potential peaks where the charge deficit ($b_2 = -2$,
    i.e. net positive charge) sits, as electrostatics demands.
