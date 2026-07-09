# The Lorentz Force

## Equation

$$\boxed{\,m\frac{d\mathbf{v}}{dt} = q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right)\,}$$

## Physical meaning

The complete law of motion for a charged particle in electromagnetic fields — one half
of all plasma physics (Maxwell's equations are the other). The electric term
accelerates along $\mathbf{E}$; the magnetic term bends the velocity without ever
changing the speed.

## Variables

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | particle mass | kg |
| $q$ | charge (sign matters!) | C |
| $\mathbf{v}$ | velocity | m/s |
| $\mathbf{E}$ | electric field | V/m |
| $\mathbf{B}$ | magnetic flux density | T |

## Key structural facts

- **Magnetic force does no work:**
  $\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B}) = 0$ — kinetic energy responds only to
  $\mathbf{E}$. (Any energy change in a magnetic-only simulation is numerical error —
  the standard [integrator diagnostic](../concepts/forward-euler.md).)
- **The cross product couples the velocity components** — the source of gyration
  ([cyclotron motion](cyclotron-motion.md)) and, in inhomogeneous fields, of every
  [drift](../concepts/guiding-center-drifts.md).
- As a state-space system $\mathbf{z} = (\mathbf{x}, \mathbf{v})$, it's the standard
  ODE benchmark of [Chapter 2](../concepts/ode-integration.md), with a closed-form
  [leapfrog update](leapfrog-update.md).

## Applications

Single-particle orbits, drift theory, [PIC pushers](../concepts/pic-method.md),
mass spectrometers, cyclotrons, aurora physics.

## Limitations

Non-relativistic as written (use $d(\gamma m\mathbf{v})/dt$ for fast particles);
point-particle (no radiation reaction); fields are external inputs — self-consistency
requires coupling to Maxwell ([PIC](../concepts/pic-method.md)).

## Related equations

- [Cyclotron motion](cyclotron-motion.md) — its uniform-field solution
- [E×B drift](exb-drift.md), [grad-B/curvature drifts](grad-b-curvature-drift.md) — averaged consequences
- [Leapfrog update](leapfrog-update.md) — its discrete twin

## Quiz

**Q1 (computational).** An electron moves at $10^6$ m/s perpendicular to $B = 0.01$ T.
Force magnitude?

??? success "Answer"
    $F = qvB = 1.6\times10^{-19}\times10^6\times0.01 = 1.6\times10^{-15}$ N —
    yielding an enormous acceleration $\sim 1.8\times10^{15}\ \text{m/s}^2$ for so
    light a particle.

**Q2 (conceptual).** Why can a magnetic field confine a plasma but not heat it?

??? success "Answer"
    $\mathbf{F}_B \perp \mathbf{v}$ always: it redirects momentum (confinement) but
    transfers no energy (no heating). Heating needs $\mathbf{E}$ — waves, induction,
    or collisions.
