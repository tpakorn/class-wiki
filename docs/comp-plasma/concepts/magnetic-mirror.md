# Magnetic Mirror

## Intuition

Squeeze magnetic field lines together at two ends of a tube and you've built a bottle
for charged particles. A particle spiraling toward the pinch feels the field
strengthen; its gyration steals energy from its forward motion until — if the pinch is
strong enough — it stops, turns, and bounces back. Two mirrors face-to-face trap
particles indefinitely. Nature builds them too: Earth's Van Allen belts are mirror
machines.

## The field

The course models a mirror through its flux function in cylindrical coordinates
$(r, \theta, z)$:

$$\psi = B_0\,\pi r^2\left(1 + \frac{z^2}{L^2}\right), \qquad
\mathbf{B} = \frac{1}{2\pi}\nabla\psi\times\nabla\theta$$

which evaluates to

$$B_r = -\frac{B_0\, r z}{L^2}, \qquad B_z = B_0\left(1 + \frac{z^2}{L^2}\right)$$

$|\mathbf{B}|$ is weakest at the midplane ($z = 0$) and grows toward the mirror
points. Field lines are contours of $\psi$ — and a well-magnetized particle's guiding
center *stays on its contour*.

## Why particles reflect: the adiabatic invariant

The magnetic moment

$$\boxed{\,\mu = \frac{m v_\perp^2}{2B}\,}$$

is an **adiabatic invariant**: nearly constant when the field changes slowly over a
gyration. Since $B$ does no work, $v^2 = v_\parallel^2 + v_\perp^2$ is also constant.
As the particle rides into stronger $B$, constant $\mu$ forces $v_\perp^2$ to grow —
so $v_\parallel^2$ must shrink. If $B$ reaches
$B_\text{reflect} = B_\text{min}\, v^2/v_{\perp,0}^2$ before the throat, the particle
reflects.

## The loss cone

Particles with too much parallel velocity escape. With mirror ratio
$R_m = B_\text{max}/B_\text{min}$, the trapping condition on the midplane pitch angle
$\theta$ is

$$\sin^2\theta > \frac{B_\text{min}}{B_\text{max}} = \frac{1}{R_m}$$

Velocities inside the **loss cone** ($\theta < \theta_\text{trap}$,
$\sin\theta_\text{trap} = R_m^{-1/2}$) stream straight through. This leak is why
mirror fusion machines struggled — collisions constantly scatter particles into the
cone.

## Numerical experiment

Integrate orbits with the [3-D leapfrog solver](leapfrog-method.md) in the field
above ([worked example](../examples/magnetic-mirror-orbit.md)):

- Launch with various $v_\parallel/v_\perp$: watch trapped orbits bounce and passing
  orbits escape
- Verify $\mu$ stays constant while $v_\parallel$ oscillates
- Verify the guiding center hugs a $\psi$-contour

## Common mistakes

- **Thinking the magnetic force decelerates the particle.** $\mathbf{B}$ does no work;
  it *redirects* kinetic energy from parallel to perpendicular. Total speed never
  changes.
- **Treating $\mu$ as exactly conserved.** It's *adiabatic* — conserved to
  exponential accuracy while fields vary slowly; fast field changes (or sharp field
  gradients) break it.
- **Forgetting the loss cone.** A mirror is a leaky bottle by construction; only
  pitch angles outside the cone are held.

## Related concepts

- [Guiding center & drifts](guiding-center-drifts.md) — framework
- [Fermi acceleration](fermi-acceleration.md) — what moving mirrors do
- [Adiabatic invariants in PC368](../../plasma/concepts/adiabatic-invariant.md) — the theory treatment
- [Magnetic mirror orbit example](../examples/magnetic-mirror-orbit.md)

## Knowledge graph position

**Prerequisites:** [Guiding center](guiding-center-drifts.md), [Leapfrog](leapfrog-method.md).
**Leads to:** [Fermi acceleration](fermi-acceleration.md).

## Quiz

**Q1 (computational).** A mirror has $R_m = 4$. What fraction of an isotropic particle
population is trapped?

??? success "Answer"
    Loss cone half-angle: $\sin\theta_c = 1/2 \Rightarrow \theta_c = 30°$. Solid-angle
    fraction lost (both cones): $1 - \cos\theta_c = 1 - \frac{\sqrt3}{2} \approx 0.134$
    each side ⇒ trapped fraction $= \cos\theta_c \approx 87\%$.

**Q2 (conceptual).** A trapped particle's $v_\perp$ is largest at which point of its
bounce?

??? success "Answer"
    At the mirror (turning) points, where $B$ is largest: $\mu = mv_\perp^2/2B$ const
    forces $v_\perp^2 \propto B$. There $v_\parallel = 0$ — all energy is
    perpendicular.

**Q3 (MCQ).** Earth's radiation belts trap particles because the geomagnetic field:

- (a) is uniform  (b) strengthens toward the poles  (c) vanishes at the equator  (d) is purely radial

??? success "Answer"
    **(b).** Field lines converge near the magnetic poles — natural mirror points;
    particles bounce pole-to-pole.
