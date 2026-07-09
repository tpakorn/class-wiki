# Example · Orbit in a Magnetic Mirror

## Problem statement

Integrate an electron orbit in the mirror field derived from the flux function
$\psi = B_0\pi r^2\left(1 + z^2/L^2\right)$ and demonstrate: (a) trapping and
reflection, (b) conservation of the magnetic moment $\mu$, (c) that the guiding
center rides a constant-$\psi$ contour.

## Given information

Field components (from $\mathbf{B} = \frac{1}{2\pi}\nabla\psi\times\nabla\theta$):

$$B_r = -\frac{B_0\, r z}{L^2}, \qquad B_z = B_0\left(1 + \frac{z^2}{L^2}\right)$$

with $B_0 = L = 1$ (normalized), no electric field.

## Solution strategy

1. Implement the field in Cartesian components
   ($B_x = B_r x/r$, $B_y = B_r y/r$).
2. Push with the [3-D leapfrog solver](../equations/leapfrog-update.md) —
   symplecticity is essential over many bounce periods.
3. Launch from mid-plane with chosen pitch angle
   $\tan\theta_p = v_\perp/v_\parallel$; try several.
4. Diagnostics per step: $|\mathbf{B}|$ at the particle, $v_\perp$, $v_\parallel$,
   $\mu = \frac{mv_\perp^2}{2B}$, and $\psi(r, z)$.

## Expected results

- **Large pitch angle** (mostly perpendicular): the particle bounces between mirror
  points where $B = B_\text{min} v^2/v_{\perp 0}^2$ — trapped.
- **Small pitch angle** (inside the [loss cone](../concepts/magnetic-mirror.md),
  $\sin^2\theta_p < B_\text{min}/B_\text{max}$): sails through and escapes.
- $\mu(t)$ stays constant to high accuracy while $v_\parallel^2$ and $v_\perp^2$
  trade places — textbook adiabatic invariance, computed rather than assumed.
- The guiding center traces a constant-$\psi$ surface: flux conservation made visible.

## Key takeaways

- The bounce motion is the second periodicity of magnetized particles (gyration =
  first, [drift](../concepts/guiding-center-drifts.md) precession = third) — the basis
  of the three adiabatic invariants ($\mu$, $J$, $\Phi$) in
  [PC368](../../plasma/concepts/adiabatic-invariant.md).
- Total speed never changes (magnetic force does no work); only its
  parallel/perpendicular split oscillates.
- Set the mirrors in motion and each bounce pumps $v_\parallel$ —
  [Fermi acceleration](../concepts/fermi-acceleration.md), the sequel.

## Related

[Magnetic mirror](../concepts/magnetic-mirror.md) ·
[Leapfrog update](../equations/leapfrog-update.md) ·
[Fermi acceleration](../concepts/fermi-acceleration.md)
