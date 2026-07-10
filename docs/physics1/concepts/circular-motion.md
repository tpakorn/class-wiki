# Circular Motion

*Source lecture(s):* [SC133 Lec 5](../lectures.md)

## Intuition

A ball on a string moves in a circle at constant speed — yet it is *accelerating* the
whole time, because its velocity's **direction** keeps changing. The acceleration
points toward the center (centripetal, "center-seeking"): the string constantly pulls
the velocity vector around without ever changing its length. No inward force, no
circle — let go of the string and the ball flies off along the *tangent*, not
outward.

## The formulas

For speed $v$ on a circle of radius $r$:

$$\boxed{\,a_c = \frac{v^2}{r} = \omega^2 r\,} \qquad \text{directed toward the center}$$

with angular speed $\omega = v/r$ (rad/s), period $T = 2\pi r/v = 2\pi/\omega$.

The inward force required, by [Newton's second law](newtons-laws.md):

$$F_c = \frac{m v^2}{r}$$

**Centripetal force is not a new force** — it is a *role* played by whatever real
force points inward: string tension, gravity (orbits), friction (cornering car),
normal force (banked turn, loop-the-loop).

## Derivation of $a_c = v^2/r$

In time $\Delta t$ the position vector rotates by $\Delta\theta = \omega\Delta t$; so
does the velocity vector. For small angles the change in velocity has magnitude
$|\Delta \vec v| \approx v\,\Delta\theta$, pointing toward the center. Hence

$$a = \frac{|\Delta\vec v|}{\Delta t} = v\frac{\Delta\theta}{\Delta t} = v\omega = \frac{v^2}{r}.$$

The geometry of the velocity triangle mirrors the position triangle — that similarity
is the entire proof.

## Non-uniform circular motion

If the speed changes too, add a **tangential** component $a_t = dv/dt$ along the
motion; total acceleration $a = \sqrt{a_c^2 + a_t^2}$. The centripetal part handles
turning, the tangential part handles speeding up.

## Worked example: how fast can a car corner?

Static friction supplies the centripetal force: $\mu_s m g \geq mv^2/r$, so

$$v_\text{max} = \sqrt{\mu_s\, g\, r}$$

For $\mu_s = 0.8$, $r = 50\,\text{m}$: $v_\text{max} = \sqrt{0.8\times9.8\times50}
\approx 19.8\,\text{m/s} \approx 71\,\text{km/h}$. Independent of the car's mass —
heavier cars need more force but also grip harder.

## Common mistakes

- **Inventing "centrifugal force".** In an inertial frame there is no outward force on
  the ball; the outward *feeling* is your body trying to go straight while the car
  turns under you.
- **Thinking constant speed means zero acceleration.** Acceleration is change of
  *velocity* — direction counts.
- **Drawing $F_c$ as an extra arrow on a free-body diagram.** Label the *actual*
  forces (tension, gravity, friction, normal); their inward resultant *is* the
  centripetal force.

## Related concepts

- [Vectors](vectors.md) — velocity direction is everything here
- [Newton's laws](newtons-laws.md) — supplies the required force
- [Rotation](rotation.md) — same angular language for spinning bodies
- [Kepler's laws & orbits](keplers-laws.md) — gravity as centripetal force
- [Gyration in magnetic fields (PC368)](../../plasma/concepts/larmor-radius.md) — the same circle with $qvB$ as the inward force

## Knowledge graph position

**Prerequisites:** [Kinematics](kinematics.md), [Vectors](vectors.md).
**Leads to:** [Rotation](rotation.md), [Gravitation & orbits](gravitation.md).

## Quiz

**Q1 (computational).** A satellite orbits at $r = 7000\,\text{km}$ with
$v = 7.5\,\text{km/s}$. Its centripetal acceleration?

??? success "Answer"
    $a_c = v^2/r = (7500)^2 / 7\times10^6 \approx 8.0\,\text{m/s}^2$ — nearly $g$!
    Orbiting *is* falling; the satellite just keeps missing the ground.

**Q2 (conceptual).** A ball on a string is swung in a vertical circle. Where is the
string tension largest?

??? success "Answer"
    At the bottom: tension must supply the centripetal force *and* fight gravity,
    $T = mv^2/r + mg$ (and $v$ is also largest there by energy conservation).

**Q3 (multiple choice).** The string breaks at the top of a horizontal circle. The
ball initially flies: (a) radially outward (b) along the tangent (c) spirally

??? success "Answer"
    **(b).** Remove the force and Newton's first law takes over: straight-line motion
    along the instantaneous velocity — the tangent.
