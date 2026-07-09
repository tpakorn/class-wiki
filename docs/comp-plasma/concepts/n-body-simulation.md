# N-Body Simulation

## Intuition

Until now the fields were prescribed; now the particles *are* the field sources.
Gravity is the cleanest playground: $N$ masses, every pair attracting. The algorithm
is almost embarrassingly direct — sum the forces, [kick–drift–kick](leapfrog-method.md),
repeat — and yet it produces star clusters, galaxy collisions, and the irreducible
chaos of the three-body problem.

## The force

$$\boxed{\,\mathbf{a}_i = G\sum_{j\neq i}\frac{m_j(\mathbf{x}_j - \mathbf{x}_i)}{\left(|\mathbf{x}_j - \mathbf{x}_i|^2 + \epsilon^2\right)^{3/2}}\,}$$

Two practicalities hiding in that formula:

- **Softening $\epsilon$:** the raw $1/r^2$ force diverges at close encounters,
  destroying the integrator's accuracy. Adding $\epsilon^2$ caps the force — you give
  up resolving scales below $\epsilon$ in exchange for sane time steps.
- **Cost:** $N(N-1)/2$ pairs — $\mathcal{O}(N^2)$ per step. Vectorize with NumPy
  broadcasting (`x[None,:,:] - x[:,None,:]`); production codes go further
  (tree codes $\mathcal{O}(N\log N)$, or the grid trick that becomes
  [PIC](pic-method.md)).

## Time stepping: kick–drift–kick

$$\mathbf{v}_{n+1/2} = \mathbf{v}_n + \tfrac{\Delta t}{2}\mathbf{a}_n
\qquad
\mathbf{x}_{n+1} = \mathbf{x}_n + \Delta t\,\mathbf{v}_{n+1/2}
\qquad
\mathbf{v}_{n+1} = \mathbf{v}_{n+1/2} + \tfrac{\Delta t}{2}\mathbf{a}_{n+1}$$

Symplectic [leapfrog](leapfrog-method.md) is non-negotiable here: over the millions of
steps of a cluster simulation, [RK4](runge-kutta-methods.md)'s secular energy drift
would slowly evaporate or collapse the system by pure numerics.

## Diagnostics: energy and the virial theorem

$$K = \frac12\sum_i m_i v_i^2, \qquad
U = -G\sum_{i<j}\frac{m_i m_j}{|\mathbf{x}_i - \mathbf{x}_j|}$$

Two health checks for any run:

1. **Total energy** $K + U$ conserved (up to leapfrog's bounded oscillation)
2. **Virial theorem** for a relaxed bound system:
   $$\boxed{\,2\langle K\rangle = -\langle U\rangle\,}$$
   Start a cloud cold, let it collapse and relax, and watch the time averages settle
   onto the virial ratio — statistical mechanics emerging from Newton.

## The three-body problem

$N = 3$ is already chaotic: no general closed-form solution, exquisite sensitivity to
initial conditions, generic outcomes of ejection or near-collision. Special periodic
solutions exist (Euler's collinear, Lagrange's triangle, the figure-eight) — finding
and *stress-testing* them numerically is the classic exercise. Chaos also raises the
stakes for the integrator: only symplectic schemes keep the energy surface honest
while trajectories scramble.

## Common mistakes

- **Skipping softening** and wondering why energy explodes at the first close pass.
- **Using adaptive-step RK for long-term orbits** — adaptivity breaks time symmetry
  and reintroduces drift.
- **Testing chaos with one run.** Sensitivity means single trajectories are
  meaningless at late times; compare ensembles or conserved quantities.

## Related concepts

- [Leapfrog / KDK](leapfrog-method.md) — the integrator
- [PIC method](pic-method.md) — the grid-based alternative for plasmas
- [Convergence and error](convergence-and-error.md) — validation discipline

## Knowledge graph position

**Prerequisites:** [Leapfrog](leapfrog-method.md), Newtonian gravity.
**Leads to:** [PIC method](pic-method.md), astrophysical simulation.

## Quiz

**Q1 (computational).** A direct N-body code takes 1 s per step at $N = 10^3$.
Estimate the time per step at $N = 10^5$.

??? success "Answer"
    $\mathcal{O}(N^2)$: $(100)^2 = 10^4$ × slower ⇒ ~3 hours per step. Hence tree
    codes and PIC.

**Q2 (conceptual).** A cold, collapsing star cluster ends up with
$2\langle K\rangle = -\langle U\rangle$. If the initial state had $K = 0$ and
potential energy $U_0$, what fraction of $|U_0|$ was "lost" to reach virial
equilibrium at the same $U$? (It isn't really lost.)

??? success "Answer"
    Virial: $K = -U/2$, so $E = K + U = U/2$. Starting from $E = U_0$… energy is
    conserved: the system contracts until $U = 2U_0$ (deeper), giving $K = -U_0$.
    Nothing is lost — potential energy converts to kinetic, carried largely by a few
    ejected particles and the deeper-bound core.

**Q3 (MCQ).** Gravitational softening $\epsilon$ primarily trades:

- (a) speed for memory  (b) small-scale accuracy for numerical stability
- (c) energy conservation for momentum conservation  (d) nothing; it's free

??? success "Answer"
    **(b).** Below $\epsilon$ the force law is wrong on purpose, so close encounters
    can't demand impossibly small time steps.
