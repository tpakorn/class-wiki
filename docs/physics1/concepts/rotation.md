# Rotation

*Source lecture(s):* [SC133 Lec 12](../lectures.md)

## Intuition

Everything you learned about straight-line motion has a spinning twin. Angle replaces
position, angular velocity replaces velocity, torque replaces force, moment of
inertia replaces mass — and *every equation carries over unchanged*. Learn the
dictionary once and rotation costs you nothing new; the only genuinely fresh idea is
that the "mass" of rotation depends on *where* the mass sits.

## The translation dictionary

| Linear | Rotational | Link |
|---|---|---|
| position $x$ | angle $\theta$ (rad) | $s = r\theta$ |
| velocity $v$ | angular velocity $\omega = d\theta/dt$ | $v = r\omega$ |
| acceleration $a$ | angular acceleration $\alpha = d\omega/dt$ | $a_t = r\alpha$ |
| mass $m$ | moment of inertia $I$ | [see below](moment-of-inertia.md) |
| force $F$ | torque $\tau$ | [$\tau = rF\sin\phi$](torque.md) |
| $\sum F = ma$ | $\sum\tau = I\alpha$ | Newton II, rotated |
| $K = \tfrac12 mv^2$ | $K = \tfrac12 I\omega^2$ | |
| $p = mv$ | $L = I\omega$ | [angular momentum](rolling-torque-angular-momentum.md) |

The constant-$\alpha$ kinematics come along for free:
$\omega = \omega_0 + \alpha t$, $\theta = \omega_0 t + \tfrac12\alpha t^2$,
$\omega^2 = \omega_0^2 + 2\alpha\Delta\theta$ — the
[kinematic equations](../equations/kinematic-equations.md) with letters swapped.

## Radians, or the dictionary breaks

The linking relations $s = r\theta$, $v = r\omega$ hold **only in radians**
(the definition of angle as arc/radius). One revolution $= 2\pi$ rad;
$1\,\text{rpm} = 2\pi/60\,\text{rad/s}$.

## Every point of a rigid body

All points share the same $\omega$ and $\alpha$; each point's *linear* speed grows
with radius, $v = r\omega$. A point at radius $r$ also has centripetal acceleration
$a_c = \omega^2 r$ toward the axis — [circular motion](circular-motion.md) applied
point by point.

## Worked example: spinning up a flywheel

A flywheel with $I = 2\,\text{kg·m}^2$ starts at rest under constant torque
$\tau = 10\,\text{N·m}$ for 6 s. Find $\omega$, the angle turned, and the kinetic
energy.

$\alpha = \tau/I = 5\,\text{rad/s}^2$;
$\omega = \alpha t = 30\,\text{rad/s}$;
$\theta = \tfrac12\alpha t^2 = 90\,\text{rad}$ (≈14.3 rev);
$K = \tfrac12 I\omega^2 = 900\,\text{J}$ — which equals the work $\tau\theta = 10\times90$ ✓.

## Common mistakes

- **Degrees in the linking formulas.** $v = r\omega$ with $\omega$ in deg/s is
  meaningless; convert first.
- **Confusing $a_t$ and $a_c$.** Tangential acceleration ($r\alpha$) changes speed;
  centripetal ($\omega^2 r$) changes direction; both may coexist.
- **Treating $\omega$ as the same for different bodies** connected by belts: belts
  share *linear* speed at the rim ($v = r\omega$), so different radii spin at
  different $\omega$.

## Related concepts

- [Moment of inertia](moment-of-inertia.md) — the rotational mass
- [Torque](torque.md) — the rotational force
- [Rolling, torque & angular momentum](rolling-torque-angular-momentum.md) — the synthesis
- [Circular motion](circular-motion.md) — one particle's view

## Knowledge graph position

**Prerequisites:** [Kinematics](kinematics.md), [Newton's laws](newtons-laws.md), [Circular motion](circular-motion.md).
**Leads to:** [Moment of inertia](moment-of-inertia.md), [Torque](torque.md), [Rolling & angular momentum](rolling-torque-angular-momentum.md).

## Quiz

**Q1 (computational).** A hard disk spins at 7200 rpm. Angular velocity in rad/s, and
linear speed at radius 4 cm?

??? success "Answer"
    $\omega = 7200\times2\pi/60 = 754\,\text{rad/s}$;
    $v = r\omega = 0.04\times754 \approx 30\,\text{m/s}$ — over 100 km/h at the rim.

**Q2 (conceptual).** Two children sit on a merry-go-round, one near the center, one
at the edge. Compare their angular and linear velocities.

??? success "Answer"
    Same $\omega$ (rigid body), but the edge child moves faster linearly
    ($v = r\omega$) — and needs more centripetal force to hold on.

**Q3 (multiple choice).** Doubling a flywheel's angular speed multiplies its kinetic
energy by: (a) 2 (b) 4 (c) $\sqrt2$

??? success "Answer"
    **(b).** $K = \tfrac12 I\omega^2 \propto \omega^2$ — exactly like $v^2$ for
    linear motion; the dictionary never lies.
