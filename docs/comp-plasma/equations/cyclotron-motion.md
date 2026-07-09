# Cyclotron Motion & the Cross-Field Cycloid

## Equations

Uniform $\mathbf{B} = B\hat{k}$: circular gyration at the **cyclotron frequency**
with **Larmor radius**

$$\boxed{\,\omega_c = \frac{qB}{m}\,} \qquad \boxed{\,r_L = \frac{m v_\perp}{qB}\,}$$

Add $\mathbf{E} = E\hat{\jmath}$ (crossed fields) and a particle starting at rest
traces a **cycloid**:

$$x(t) = R(\omega t - \sin\omega t), \qquad y(t) = R(1 - \cos\omega t),
\qquad R = \frac{mE}{qB^2}$$

— gyration superposed on the [E×B drift](exb-drift.md) $v_E = E/B$ (the rolling-wheel
curve: the wheel's center moves at $v_E$).

## Physical meaning

The two fundamental scales of magnetized-particle motion: *how fast* it circles
($\omega_c$) and *how big* the circle is ($r_L$). Their smallness compared to field
scales is what licenses the entire
[guiding-center approximation](../concepts/guiding-center-drifts.md).

## Variables

$q, m$ — charge, mass · $B$ — field strength · $v_\perp$ — speed ⊥ $\mathbf{B}$ ·
$E$ — crossed electric field · $R$ — cycloid radius.

## Why it's the course benchmark

The cycloid is an *exact, nontrivial* solution of the
[Lorentz force](lorentz-force.md): oscillatory (stresses stability), analytic
(permits exact error measurement), and physically meaningful (it *is* the E×B drift).
Every integrator in [Chapter 2](../concepts/ode-integration.md) is graded against it —
see [convergence and error](../concepts/convergence-and-error.md) and the
[worked example](../examples/cross-field-benchmark.md).

## Numbers worth knowing

Electron in a 1 T field: $\omega_c/2\pi \approx 28$ GHz (microwaves — the basis of
electron-cyclotron heating). Proton in Earth's field ($\sim 50\ \mu$T):
$\omega_c/2\pi \approx 0.76$ Hz.

## Related equations

- [Lorentz force](lorentz-force.md) — parent
- [E×B drift](exb-drift.md) — the cycloid's average velocity
- [Leapfrog update](leapfrog-update.md) — reproduces gyration exactly in radius

## Quiz

**Q1 (computational).** For $q = m = E = B = 1$ (normalized), what are $\omega$, $R$,
and the drift speed?

??? success "Answer"
    $\omega = 1$, $R = 1$, $v_E = E/B = 1$ — the course's standard test configuration.

**Q2 (conceptual).** Ions and electrons gyrate in opposite senses. Why does the
cycloid's *drift* direction nonetheless come out the same for both?

??? success "Answer"
    Both the gyration sense and the E-field acceleration direction flip with charge;
    the two sign flips cancel in $\mathbf{E}\times\mathbf{B}/B^2$ — the drift is
    charge-blind.
