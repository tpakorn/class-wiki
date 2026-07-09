# The Particle-In-Cell (PIC) Method

## Intuition

Direct [N-body](n-body-simulation.md) costs $\mathcal{O}(N^2)$ because every particle
talks to every other. PIC's trick: particles never talk to each other directly — they
talk to a **grid**. Deposit charge onto mesh points, solve one field equation on the
mesh, interpolate the field back. Cost collapses to $\mathcal{O}(N + M)$, and the
physics gains something profound: the simulation is **self-consistent** — the fields
that push the particles are the fields the particles made.

## The PIC cycle

Every time step walks the same loop:

1. **Deposit** — assign particle charge to mesh: density $n_j$
2. **Solve** — [Poisson equation](poisson-solvers.md) on the mesh:
   $\dfrac{d^2\phi}{dx^2} = n(x) - n_0$ (electrons against a uniform ion background)
3. **Differentiate** — $E_j = -\dfrac{\phi_{j+1} - \phi_{j-1}}{2\Delta x}$
4. **Interpolate** — field from mesh to each particle position: $E(r_i)$
5. **Push** — advance particles with [leapfrog](leapfrog-method.md):
   $\dot r_i = v_i$, $\dot v_i = -E(r_i)$ (normalized electrons)

## Cloud-in-cell weighting

The deposit and interpolation both use **linear (CIC) weights**. A particle at $r_i$
between grid points $x_j$ and $x_{j+1}$:

$$n_j \mathrel{+}= \frac{x_{j+1} - r_i}{\Delta x}, \qquad
n_{j+1} \mathrel{+}= \frac{r_i - x_j}{\Delta x}$$

$$E(r_i) = \frac{x_{j+1} - r_i}{\Delta x}E_j + \frac{r_i - x_j}{\Delta x}E_{j+1}$$

Using the *same* weights both ways is not cosmetic: it guarantees momentum
conservation (no particle self-force). Implementation: `np.bincount` for deposit,
fancy indexing for interpolation.

## The field solve

The 1-D periodic [Poisson problem](poisson-solvers.md) is a tridiagonal(+corners)
sparse system solved directly each step with `scipy.sparse.linalg.spsolve` — exact,
fast, and reused thousands of times.

## What PIC actually simulates

Each computational particle is a **super-particle** standing in for millions of real
electrons; the method samples the phase-space distribution $f(x, v, t)$ with markers.
PIC is thus a Monte-Carlo-flavored solver for the
[Vlasov equation](../../plasma/concepts/vlasov-equation.md) — kinetic physics
([Landau damping](../../plasma/concepts/landau-damping.md), beam instabilities,
phase-space vortices) at a fraction of a full 6-D grid's cost. The price: statistical
noise $\propto 1/\sqrt{N_\text{per cell}}$.

## Common mistakes

- **Mismatched deposit/interpolation schemes** → self-forces, artificial heating.
- **Under-resolving the Debye length / plasma frequency.** Rules of thumb:
  $\Delta x \lesssim \lambda_D$, $\omega_{pe}\Delta t \lesssim 0.2$ — else numerical
  grid heating corrupts everything.
- **Too few particles per cell.** Noise masquerades as physics; growth-rate
  measurements need enough markers for the signal to clear the noise floor.

## Related concepts

- [Two-stream instability](two-stream-instability.md) — the demonstration
- [Poisson solvers](poisson-solvers.md) · [Leapfrog](leapfrog-method.md) — the two engines
- [N-body simulation](n-body-simulation.md) — the $\mathcal{O}(N^2)$ contrast
- [Vlasov equation (PC368)](../../plasma/concepts/vlasov-equation.md) — the equation being sampled

## Knowledge graph position

**Prerequisites:** [Leapfrog](leapfrog-method.md), [Poisson solvers](poisson-solvers.md), [N-body](n-body-simulation.md).
**Leads to:** [Two-stream instability](two-stream-instability.md), production plasma simulation.

## Quiz

**Q1 (conceptual).** Why does PIC scale so much better than direct summation?

??? success "Answer"
    Particle–particle interactions are mediated by the mesh: deposit is
    $\mathcal{O}(N)$, the 1-D field solve $\mathcal{O}(M)$, interpolation
    $\mathcal{O}(N)$ — versus $\mathcal{O}(N^2)$ pairwise forces. The grid acts as a
    common bulletin board.

**Q2 (computational).** A particle sits exactly midway between two grid points. What
CIC weights does it give each?

??? success "Answer"
    ½ and ½ — linear weighting splits it evenly.

**Q3 (MCQ).** The self-consistency of PIC means:

- (a) results are independent of $\Delta t$
- (b) the fields are recomputed from the particles every step
- (c) particles never cross cell boundaries
- (d) energy is exactly conserved

??? success "Answer"
    **(b).** Field ← particles ← field, every cycle — the defining loop of plasma
    physics, closed numerically.
