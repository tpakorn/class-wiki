# Rolling & Angular Momentum

*Source lecture(s):* [SC133 Lec 13](../lectures.md)

## Intuition

Two grand finales of rotational mechanics. **Rolling** marries translation to
rotation: a wheel that rolls without slipping is doing both at once, locked together
by its rim. **Angular momentum** is rotation's conserved currency — the reason
spinning tops stand up, skaters spin faster with arms pulled in, and planets sweep
equal areas. When no external torque acts, $L$ simply cannot change.

## Rolling without slipping

The contact point is momentarily **at rest** on the ground; the geometry locks

$$v_\text{cm} = \omega R, \qquad a_\text{cm} = \alpha R$$

Kinetic energy splits into two clean pieces:

$$K = \underbrace{\tfrac12 M v_\text{cm}^2}_{\text{translation}}
 + \underbrace{\tfrac12 I_\text{cm}\omega^2}_{\text{rotation}}
 = \tfrac12 M v_\text{cm}^2\left(1 + \frac{I_\text{cm}}{MR^2}\right)$$

**The great downhill race.** From energy conservation on a slope of height $h$:

$$v = \sqrt{\frac{2gh}{1 + I_\text{cm}/MR^2}} \qquad
a = \frac{g\sin\theta}{1 + I_\text{cm}/MR^2}$$

Mass and radius cancel; only the shape factor $I/MR^2$ matters. Sphere
($\tfrac25$) beats disk ($\tfrac12$) beats hoop ($1$) — every time, and a
frictionless *sliding* block beats them all (no energy diverted into spin). Static
friction enables rolling but does no work: the contact point never moves.

## Angular momentum

For a particle: $\vec L = \vec r\times\vec p$. For a rigid body about its axis:

$$L = I\omega \qquad\qquad \boxed{\,\sum\vec\tau = \frac{d\vec L}{dt}\,}$$

**Conservation:** zero net external torque ⇒ $\vec L$ constant, even while the body
rearranges itself:

$$I_1\omega_1 = I_2\omega_2$$

- **Skater / diver / neutron star:** pull mass inward, $I$ drops, $\omega$ soars.
  A collapsing stellar core shrinks $r$ by $\sim10^3$, spinning up from once per
  ~month to hundreds of times per second — pulsars are conservation of $L$ made
  audible.
- **Kepler's second law** is the same statement for orbits: gravity is central (zero
  torque about the Sun), so $L = mvr_\perp$ is constant — [equal areas in equal times](keplers-laws.md).
- **Helicopter tail rotors** exist because spinning up the main rotor would
  counter-spin the fuselage.

## Worked example: skater's spin

A skater at $\omega_1 = 2\,\text{rev/s}$ with arms out ($I_1 = 4\,\text{kg·m}^2$)
pulls in to $I_2 = 1.6\,\text{kg·m}^2$:

$$\omega_2 = \frac{I_1}{I_2}\omega_1 = 5\,\text{rev/s}$$

Kinetic energy rises from $\tfrac12 I_1\omega_1^2$ to $\tfrac{I_1}{I_2}$ times that
(here ×2.5) — pulling your arms in against the centrifugal tendency is real work,
and that work is where the extra energy comes from.

## Common mistakes

- **"Friction does negative work on a rolling wheel."** In pure rolling the contact
  point is instantaneously at rest — static friction does zero work; it merely
  converts between translation and rotation.
- **Using $v = \omega R$ when slipping.** The lock holds *only* for rolling without
  slipping (a skidding, braking wheel violates it).
- **Conserving $\omega$ instead of $L$.** When $I$ changes, it is $I\omega$ that
  survives.
- **Conserving $L$ despite external torque** — check the pivot: a rod struck at its
  pivot feels hinge forces but *zero torque about the hinge*, which is why we
  conserve $L$ about that specific point.

## Related concepts

- [Rotation](rotation.md), [Moment of inertia](moment-of-inertia.md), [Torque](torque.md) — the toolkit
- [Kepler's laws](keplers-laws.md) — conservation of $L$ in the sky
- [Linear momentum](linear-momentum.md) — the translational twin
- [Angular momentum in plasmas (PC368 drift theory)](../../plasma/concepts/adiabatic-invariant.md) — adiabatic invariants as "almost-conserved" $L$

## Knowledge graph position

**Prerequisites:** [Rotation](rotation.md), [Moment of inertia](moment-of-inertia.md), [Torque](torque.md), [Conservation of energy](conservation-of-energy.md).
**Leads to:** [Equilibrium](equilibrium.md), [Kepler's laws](keplers-laws.md).

## Quiz

**Q1 (computational).** A solid sphere rolls from rest down a 1.4 m-high slope. Speed
at the bottom?

??? success "Answer"
    $v = \sqrt{2gh/(1 + 2/5)} = \sqrt{2(9.8)(1.4)/1.4} = \sqrt{19.6} \approx 4.4\,\text{m/s}$
    — versus $5.2\,\text{m/s}$ for a frictionless slider; 2/7 of the energy is tied
    up in spin.

**Q2 (conceptual).** Why is it easy to balance on a moving bicycle and hard on a
stationary one?

??? success "Answer"
    The spinning wheels carry angular momentum along the axle; tipping the bike
    demands a torque to *reorient* $\vec L$, and the response (precession) steers the
    front wheel to counteract the fall. Gyroscopic stiffness + steering geometry do
    the balancing for you.

**Q3 (multiple choice).** A spinning cloud of gas collapses under gravity by a factor
10 in radius. Its rotation rate grows by roughly:
(a) 10 (b) 100 (c) 1000

??? success "Answer"
    **(b).** $I \propto r^2$, so $\omega \propto 1/r^2$ — a factor 100. This is why
    everything in astronomy (stars, disks, galaxies) ends up spinning fast.
