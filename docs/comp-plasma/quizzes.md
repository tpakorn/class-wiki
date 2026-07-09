# Quizzes · Computational EM & Plasma

Integrative questions across the course; each concept page carries its own quiz too.

## Easy

**E1 (MCQ).** Which term of the Lorentz force can change a particle's kinetic energy?

- (a) $q\mathbf{E}$  (b) $q\mathbf{v}\times\mathbf{B}$  (c) both  (d) neither

??? success "Answer"
    **(a).** The magnetic force is always ⊥ velocity — zero work, ever.

**E2 (computational).** Forward Euler on $\dot y = 2t$, $y(0) = 0$, $\Delta t = 0.5$:
compute $y(1)$ and the exact value.

??? success "Answer"
    $y_1 = 0 + 0.5\times0 = 0$; $y_2 = 0 + 0.5\times1 = 0.5$. Exact: $t^2 = 1$.
    Error 0.5 — first-order pain at coarse steps.

**E3 (conceptual).** Why does the course benchmark every integrator on a problem with
a known exact solution?

??? success "Answer"
    Only an exact reference converts output into *measured error*, letting you verify
    the convergence order and catch implementation bugs — see
    [convergence & error](concepts/convergence-and-error.md).

**E4 (MCQ).** In the PIC cycle, the step "deposit" moves information from:

- (a) grid → particles  (b) particles → grid  (c) grid → grid  (d) particles → particles

??? success "Answer"
    **(b).** Charge assignment onto mesh points; "interpolate" is the reverse trip.

## Medium

**M1 (computational).** An electron ($q/m = 1.76\times10^{11}$ C/kg) in $B = 0.01$ T:
find the cyclotron frequency and period.

??? success "Answer"
    $\omega_c = (q/m)B = 1.76\times10^9$ rad/s → $f = 280$ MHz, $T = 3.6$ ns. Your
    simulation time step must resolve *this*, whatever slow physics you care about —
    the tyranny of the fastest scale.

**M2 (conceptual).** Two simulations of the same magnetized orbit: one shows the
radius slowly growing, the other shows it perfectly constant but the gyration phase
drifting. Identify the likely integrators.

??? success "Answer"
    Growing radius = energy gain = [forward Euler](concepts/forward-euler.md) (or any
    non-symplectic explicit method). Constant radius with phase error =
    [leapfrog](concepts/leapfrog-method.md) — symplectic schemes preserve the orbit
    geometry but not the clock.

**M3 (computational).** A 2-D FDTD run uses $N = 256$, $\Delta x = 1/256$, $c = 1$,
$\Delta t = \frac{\sqrt2}{2}\Delta x$. How many steps to cross the box once?

??? success "Answer"
    Crossing time $= 1/c = 1$; steps $= 1/\Delta t = 256\sqrt2 \approx 362$.

**M4 (conceptual).** Why does a purely toroidal magnetic field fail to confine a
plasma?

??? success "Answer"
    $B \propto 1/r$ ⇒ [grad-B + curvature drifts](equations/grad-b-curvature-drift.md)
    are vertical and charge-dependent → charge separation → vertical E →
    [E×B](equations/exb-drift.md) drives the whole plasma outward. Tokamaks add
    poloidal field so field lines wind around and short-circuit the separation.

**M5 (MCQ).** The Gauss–Seidel method solves the discrete Poisson equation by:

- (a) matrix inversion  (b) repeated local averaging until convergence
- (c) Fourier transform  (d) time marching with CFL limit

??? success "Answer"
    **(b).** Each point relaxes toward the mean of its neighbors (+ source);
    convergence is guaranteed but slow. → [Poisson solvers](concepts/poisson-solvers.md)

## Hard

**H1 (computational).** A trapped particle in a mirror with $B_\text{min} = 1$ T has
pitch angle 60° at the midplane. At what field strength does it reflect?

??? success "Answer"
    $\mu$ const: reflection where $v_\perp = v$, i.e.
    $B_\text{ref} = B_\text{min}/\sin^2 60° = 1/0.75 = 1.33$ T.

**H2 (conceptual).** In the two-stream simulation, doubling the particle count at
fixed cells lowers the *apparent* early-time field energy. Why, and does the physical
growth rate change?

??? success "Answer"
    The noise floor is shot noise: $\mathcal{E}_\text{noise} \propto 1/N$. More
    particles = quieter start (the seed the instability grows from is smaller), so
    saturation arrives later — but the *slope* $2\gamma$ of the linear phase is set by
    the physics ($v_b$, densities), not by $N$.

**H3 (computational).** Estimate the cost ratio of direct N-body vs PIC for
$N = 10^6$ particles on $M = 10^3$ cells (per step, order-of-magnitude).

??? success "Answer"
    Direct: $\sim N^2 = 10^{12}$ pair operations. PIC: deposit + push $\sim N = 10^6$,
    field solve $\sim M = 10^3$ → $\sim 10^6$ total. Ratio $\sim 10^6$ — the grid is
    six orders of magnitude cheaper.

**H4 (conceptual).** The leapfrog scheme applied to the Lorentz force is implicit,
yet needs no iterative solver. What structural feature makes this possible, and where
else in the course does the same trick appear?

??? success "Answer"
    The implicit unknown enters *linearly* (magnetic force ∝ $\mathbf{v}$), so
    $\mathbf{v}_\text{new} + \mathbf{A}\times\mathbf{v}_\text{new} = \mathbf{C}$ has a
    closed-form vector solution. The same "implicitness made cheap by linearity"
    appears in FDTD's staggered updates and in the direct (tridiagonal) Poisson solve —
    linear structure is the algorithmicist's best friend.
