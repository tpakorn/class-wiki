# Glossary · Computational EM & Plasma

Alphabetical reference for the [PHY653 wiki](index.md).

---

**Adiabatic invariant** — Quantity (e.g. $\mu = mv_\perp^2/2B$) conserved when fields
vary slowly compared to the particle's periodic motion.
→ [Magnetic mirror](concepts/magnetic-mirror.md)

**A-stability** — Unconditional stability for decaying problems; property of implicit
schemes like backward Euler. → [Backward Euler](concepts/backward-euler.md)

**Boris pusher** — The standard PIC particle mover; a rotate-and-kick form of the
implicit leapfrog. → [Leapfrog update](equations/leapfrog-update.md)

**CFL (Courant) condition** — $\Delta t \leq \Delta x/(c\sqrt d)$: the time step must
not outrun signal propagation on the grid. → [CFL](equations/cfl-condition.md)

**Cloud-in-cell (CIC)** — Linear weighting between particles and grid in PIC deposit
and interpolation. → [PIC method](concepts/pic-method.md)

**Curvature drift** — Guiding-center drift from bent field lines, ∝ $v_\parallel^2$,
charge-dependent. → [Grad-B & curvature](equations/grad-b-curvature-drift.md)

**Cyclotron frequency** — $\omega_c = qB/m$; the gyration rate.
→ [Cyclotron motion](equations/cyclotron-motion.md)

**Explicit method** — Update computed directly from known values; cheap but
conditionally stable. → [ODE integration](concepts/ode-integration.md)

**E×B drift** — $\mathbf{v}_E = \mathbf{E}\times\mathbf{B}/B^2$; charge- and
mass-independent. → [E×B drift](equations/exb-drift.md)

**FDTD** — Finite-Difference Time-Domain: leapfrogged, staggered-grid solution of
Maxwell's curl equations. → [FDTD](concepts/fdtd-method.md)

**Fermi acceleration** — Energy gain of particles bouncing between converging magnetic
mirrors. → [Fermi acceleration](concepts/fermi-acceleration.md)

**Finite difference** — Approximating derivatives with difference quotients on a grid.
→ [FDM](concepts/finite-difference-method.md)

**Five-point stencil** — The 2-D discrete Laplacian coupling a point to its four
neighbors. → [FDM](concepts/finite-difference-method.md)

**Forward Euler** — Simplest explicit scheme, first order; gains energy on orbits.
→ [Forward Euler](concepts/forward-euler.md)

**Gauss–Seidel** — Iterative relaxation solver for Poisson/Laplace using freshly
updated neighbors. → [Poisson solvers](concepts/poisson-solvers.md)

**Grad-B drift** — Drift from spatial variation of $|\mathbf{B}|$, ∝ $v_\perp^2$,
charge-dependent. → [Grad-B & curvature](equations/grad-b-curvature-drift.md)

**Growth rate ($\gamma$)** — Exponential rate of an instability's linear phase;
measured from the slope of $\ln\mathcal{E}(t)$.
→ [Two-stream instability](concepts/two-stream-instability.md)

**Guiding center** — The slowly drifting center of a particle's fast gyration.
→ [Guiding center & drifts](concepts/guiding-center-drifts.md)

**Implicit method** — The unknown future state appears on both sides of the update;
stable but requires a solve. → [Backward Euler](concepts/backward-euler.md)

**Kick–drift–kick (KDK)** — Split-step form of leapfrog used in N-body codes.
→ [Leapfrog](concepts/leapfrog-method.md)

**Larmor radius** — $r_L = mv_\perp/qB$; the gyration radius.
→ [Cyclotron motion](equations/cyclotron-motion.md)

**Leapfrog** — Second-order symplectic integrator with staggered position/velocity.
→ [Leapfrog](concepts/leapfrog-method.md)

**Lorentz force** — $m\dot{\mathbf{v}} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$.
→ [Lorentz force](equations/lorentz-force.md)

**Loss cone** — The pitch-angle region of particles that escape a magnetic mirror.
→ [Magnetic mirror](concepts/magnetic-mirror.md)

**Magnetic mirror** — Field configuration that reflects particles via converging field
lines. → [Magnetic mirror](concepts/magnetic-mirror.md)

**Magnetic moment ($\mu$)** — $mv_\perp^2/2B$; first adiabatic invariant.
→ [Magnetic mirror](concepts/magnetic-mirror.md)

**N-body problem** — Direct integration of all pairwise interactions;
$\mathcal{O}(N^2)$. → [N-body](concepts/n-body-simulation.md)

**Order (of a method)** — Power $p$ in the global error $\mathcal{O}(\Delta t^p)$.
→ [Convergence & error](concepts/convergence-and-error.md)

**Particle-in-cell (PIC)** — Particles coupled through grid-based field solves;
self-consistent kinetic simulation. → [PIC method](concepts/pic-method.md)

**Phase space** — The $(x, v)$ plane; where kinetic plasma dynamics is legible.
→ [Two-stream instability](concepts/two-stream-instability.md)

**Poisson equation** — $\nabla^2\phi = -\rho/\varepsilon_0$; electrostatic potential
from charge. → [Poisson solvers](concepts/poisson-solvers.md)

**Polarization drift** — Drift from time-varying $\mathbf{E}$; mass-dependent, carries
current. → [Guiding center & drifts](concepts/guiding-center-drifts.md)

**Predictor–corrector** — Estimate with an explicit step, refine with an implicit-style
evaluation. → [Backward Euler](concepts/backward-euler.md)

**Runge–Kutta (RK4)** — Multi-stage explicit schemes; RK4 is 4th order with 4
evaluations. → [Runge–Kutta](concepts/runge-kutta-methods.md)

**Softening** — Regularizing the $1/r^2$ force at small separations in N-body codes.
→ [N-body](concepts/n-body-simulation.md)

**Staggered (Yee) grid** — Interleaved E and H storage in space and time for FDTD.
→ [FDTD](concepts/fdtd-method.md)

**Stiff system** — Dynamics with fast decaying modes forcing tiny explicit steps;
calls for implicit methods. → [ODE integration](concepts/ode-integration.md)

**Symplectic integrator** — Scheme preserving phase-space structure; bounded energy
error forever. → [Leapfrog](concepts/leapfrog-method.md)

**Two-stream instability** — Exponentially growing electrostatic instability of
counter-streaming beams. → [Two-stream](concepts/two-stream-instability.md)

**Virial theorem** — $2\langle K\rangle = -\langle U\rangle$ for bound gravitational
systems. → [N-body](concepts/n-body-simulation.md)
