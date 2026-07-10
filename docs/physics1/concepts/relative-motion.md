# Relative Motion

*Source lecture(s):* [SC133 Lec 5](../lectures.md)

## Intuition

Velocity is always *relative to something*. Walk forward at $1\,\text{m/s}$ inside a
train doing $30\,\text{m/s}$: the ground sees you at $31\,\text{m/s}$; a fellow
passenger sees $1\,\text{m/s}$; you see yourself at rest. None of these is "the real"
velocity — each is correct in its own **reference frame**. Physics only demands that
observers agree on the *laws*, not on the velocities.

## The velocity-addition rule

Label frames and objects with subscripts — "P relative to A" as $\vec v_{PA}$. The
chain rule of frames:

$$\boxed{\,\vec v_{PA} = \vec v_{PB} + \vec v_{BA}\,}$$

Read the subscripts like dominoes: $PA = PB + BA$ (inner letters match and cancel).
Reversing a pair flips the sign: $\vec v_{AB} = -\vec v_{BA}$.

Because the rule is a vector equation, it works in 2-D: this is where
[vector components](vectors.md) earn their keep.

## Worked example: crossing a river (two strategies)

River flows east at $3\,\text{m/s}$; boat does $5\,\text{m/s}$ relative to the water.

**Fastest crossing:** aim straight across. Ground velocity =
$5$ across + $3$ downstream = $\sqrt{34} \approx 5.8\,\text{m/s}$; you land
downstream but in minimum time.

**Straight-line crossing:** aim *upstream* at angle $\sin\theta = 3/5 \Rightarrow
\theta = 37°$. Ground speed across: $\sqrt{5^2 - 3^2} = 4\,\text{m/s}$. You land
directly opposite, but the crossing takes longer.

Same physics, different goals — the classic exam pair.

## Worked example: rain on a moving car

Rain falls vertically at $8\,\text{m/s}$; you drive at $6\,\text{m/s}$. In your frame
the rain has a horizontal component $6\,\text{m/s}$ *toward* you:
it appears to fall at $\tan^{-1}(6/8) \approx 37°$ from vertical, at
$10\,\text{m/s}$. This is why the front windscreen catches rain and the rear window
stays dry.

## Frames and the laws of physics

All frames moving at *constant velocity* (inertial frames) agree on accelerations —
$\vec a_{PA} = \vec a_{PB}$ when $\vec v_{BA}$ is constant — so they agree on
[Newton's laws](newtons-laws.md). Accelerating frames disagree, and require
fictitious forces; that thread leads to the
[rotating-bucket problem in fluids](../../fluids/concepts/fluid-in-rigid-body-motion.md)
and beyond.

## Common mistakes

- **Adding speeds instead of velocities.** Direction matters — use components.
- **Scrambling subscripts.** Write the chain out ($v_{PA} = v_{PB} + v_{BA}$) and
  check the inner letters cancel before plugging numbers.
- **Believing one frame is "really" at rest.** The ground is just a convenient frame
  — it's also on a spinning planet orbiting a star.

## Related concepts

- [Vectors](vectors.md) — the addition rule is vector addition
- [Projectile motion](projectile-motion.md) — try analyzing it from the frame moving horizontally with the projectile
- [Eulerian vs Lagrangian frames (PC316)](../../fluids/concepts/eulerian-vs-lagrangian.md) — frames of reference as a research tool

## Knowledge graph position

**Prerequisites:** [Vectors](vectors.md), [Kinematics](kinematics.md).
**Leads to:** [Newton's laws](newtons-laws.md) (inertial frames), collision analysis in the [center-of-mass frame](center-of-mass.md).

## Quiz

**Q1 (computational).** Plane airspeed $200\,\text{km/h}$ pointing north; wind
$50\,\text{km/h}$ blowing east. Ground speed and track?

??? success "Answer"
    $v = \sqrt{200^2 + 50^2} \approx 206\,\text{km/h}$, heading
    $\tan^{-1}(50/200) \approx 14°$ east of north.

**Q2 (conceptual).** Two cars approach each other, each at $60\,\text{km/h}$. What is
the velocity of car A in car B's frame?

??? success "Answer"
    $120\,\text{km/h}$ toward B: $\vec v_{AB} = \vec v_{A,\text{gnd}} - \vec v_{B,\text{gnd}}
    = 60 - (-60) = 120$ km/h.

**Q3 (multiple choice).** You drop a ball inside a train moving at constant velocity.
It lands: (a) behind your hand (b) directly below your hand (c) ahead of your hand

??? success "Answer"
    **(b).** The ball keeps the train's horizontal velocity (Newton's first law); in
    the train frame the physics is identical to standing still — the definition of an
    inertial frame.
