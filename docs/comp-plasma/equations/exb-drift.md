# E×B Drift

## Equation

$$\boxed{\,\mathbf{v}_E = \frac{\mathbf{E}\times\mathbf{B}}{B^2}\,}$$

## Physical meaning

A charged particle in crossed fields doesn't run along $\mathbf{E}$ — it marches
sideways, perpendicular to *both* fields, at speed $E_\perp/B$. During the gyration
half where the particle moves with $\mathbf{E}$ it speeds up (fatter arc); against,
it slows (tighter arc). The lopsided circles add up to a steady sidestep.

## Variables

$\mathbf{E}$ — electric field (V/m) · $\mathbf{B}$ — magnetic field (T) ·
$\mathbf{v}_E$ — drift velocity (m/s), independent of $q$, $m$, and energy.

## Assumptions

Magnetized particle ($r_L$ small vs field scales, $\omega_c$ fast vs field changes);
$E/B \ll c$; the drift describes the *guiding center*, not the instantaneous velocity.

## The deepest way to see it

$\mathbf{v}_E$ is the velocity of the reference frame in which $\mathbf{E}_\perp$
vanishes (a Lorentz boost at $\mathbf{E}\times\mathbf{B}/B^2$ removes the
perpendicular electric field). In that frame the particle just gyrates; back in the
lab frame, the gyration center translates. That is why the drift is independent of
charge, mass, and energy — it's kinematics, not dynamics.

## Consequences

- **No current:** ions and electrons drift together — bulk plasma *flow*.
  (Currents come from the [charge-dependent drifts](grad-b-curvature-drift.md).)
- The cross-field **cycloid** benchmark's average motion — see
  [cyclotron motion](cyclotron-motion.md).
- Tokamak rotation, ionospheric convection, Hall-thruster operation, and the
  $\mathbf{E}\times\mathbf{B}$ velocimetry of lab plasmas.

## Numerical verification

Exercise 1 of [Chapter 3](../concepts/guiding-center-drifts.md): integrate uniform
crossed fields with the [3-D leapfrog](leapfrog-update.md) and recover a helical
cycloid drifting at exactly $E/B$; Exercise 2 wraps the drift around a line charge —
azimuthal orbits at $v_E = \lambda/2\pi r B$.

## Related equations

- [Lorentz force](lorentz-force.md) — parent
- [Grad-B & curvature drifts](grad-b-curvature-drift.md) — the charge-dependent siblings
- [PC368 drift theory](../../plasma/concepts/drift-motion.md) — theory-course treatment

## Quiz

**Q1 (computational).** Solar-wind conditions: $E = 1$ mV/m, $B = 5$ nT. Drift speed?

??? success "Answer"
    $v_E = 10^{-3}/5\times10^{-9} = 2\times10^5$ m/s = 200 km/s — solar-wind scale;
    E×B drifts are anything but small in space plasmas.

**Q2 (MCQ).** Doubling a particle's kinetic energy changes its E×B drift by:

- (a) ×2  (b) ×√2  (c) ×4  (d) nothing

??? success "Answer"
    **(d).** Energy-independent — only the field ratio matters.
