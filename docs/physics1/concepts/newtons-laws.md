# Newton's Laws of Motion

*Source lecture(s):* [SC133 Lec 6](../lectures.md)

## Intuition

Before Newton, "natural" motion was rest: things stop unless pushed. Newton flipped
it: **motion continues unless pushed** — what needs explaining is *change* of motion,
and force is the thing that changes it. Three laws capture the whole story: what
happens with no force (1st), how force produces acceleration (2nd), and where forces
come from (3rd: always in pairs).

## The three laws

**First law (inertia).** If the net force on a body is zero, its velocity does not
change. Constant velocity — including rest — is the force-free state. (This law also
*defines* inertial reference frames: the frames where it holds.)

**Second law.** The net force equals mass times acceleration:

$$\boxed{\,\sum \vec F = m\vec a\,}$$

— a *vector* equation: one equation per axis. More generally
$\sum\vec F = d\vec p/dt$ with momentum $\vec p = m\vec v$, the form that survives
into [collisions](collision-and-impulse.md) and rocket motion. Details on the
[equation page](../equations/newtons-second-law.md).

**Third law.** If A pushes B with force $\vec F$, then B pushes A with $-\vec F$ —
equal magnitude, opposite direction, **acting on different bodies**. Forces are
interactions; nothing pushes without being pushed back.

## The everyday forces

| Force | Nature | Magnitude |
|---|---|---|
| Weight | gravity on mass | $mg$, downward |
| Normal force $N$ | surface pushes back | whatever geometry demands (⊥ surface) |
| Tension $T$ | rope pulls along itself | same throughout an ideal (massless) rope |
| [Friction](friction-and-drag.md) | resists sliding | $\leq \mu_s N$ static; $\mu_k N$ kinetic |
| Spring | restoring | $F = -kx$ ([Hooke's law](../equations/hookes-law.md)) |

## The method: free-body diagrams

Every Newton's-law problem is the same five steps:

1. **Isolate one body**; draw it alone.
2. **Draw every force acting *on it*** (not forces it exerts on others).
3. **Choose axes** — align one with the acceleration if you know its direction.
4. **Write $\sum F = ma$ per axis.**
5. **Solve**; sanity-check limits (does $\theta \to 0$ make sense?).

## Worked example: two blocks and a pulley

Mass $m_1 = 3$ kg on a frictionless table, string over an ideal pulley to hanging
$m_2 = 2$ kg. Find the acceleration and tension.

Two bodies, two diagrams:
$m_1$: $T = m_1 a$.
$m_2$: $m_2 g - T = m_2 a$.
Add: $m_2 g = (m_1 + m_2)a \Rightarrow a = \frac{2(9.8)}{5} = 3.92\,\text{m/s}^2$,
$T = 3(3.92) = 11.8\,\text{N}$ — less than $m_2g = 19.6$ N, as it must be (the
hanging block accelerates *down*).

## Common mistakes

- **Third-law pairs on one diagram.** Weight and normal force are *not* a third-law
  pair (both act on the same body); the pair of your weight is *your* pull on Earth.
- **"Force of motion".** A puck sliding at constant velocity needs *zero* net force —
  velocity is not evidence of force; *acceleration* is.
- **Assuming $N = mg$ always.** On inclines, in elevators, or with extra vertical
  forces, $N$ adjusts — solve for it, don't assume it.
- **Applying $\sum F = ma$ to the wrong body** or mixing forces from different bodies
  in one equation.

## Related concepts

- [Friction & drag](friction-and-drag.md) — the messy real-world forces
- [Kinetic energy & work](kinetic-energy-and-work.md) — the energy view of the same physics
- [Linear momentum](linear-momentum.md) — the deeper form $\vec F = d\vec p/dt$
- [Equilibrium](equilibrium.md) — the special case $\sum\vec F = 0$
- [Lorentz force (PHY653)](../../comp-plasma/equations/lorentz-force.md) — Newton II with electromagnetic forces

## Knowledge graph position

**Prerequisites:** [Kinematics](kinematics.md), [Vectors](vectors.md).
**Leads to:** essentially everything — [work & energy](kinetic-energy-and-work.md), [momentum](linear-momentum.md), [rotation](rotation.md), [gravitation](gravitation.md), [oscillations](simple-harmonic-motion.md).

## Quiz

**Q1 (conceptual).** A horse pulls a cart; by the third law the cart pulls the horse
back equally. How does anything ever move?

??? success "Answer"
    The pair acts on *different bodies*. The cart accelerates because the horse's pull
    exceeds friction *on the cart*; the horse accelerates because the ground's
    friction on its hooves exceeds the cart's backward pull *on the horse*. Sum forces
    per body, never across bodies.

**Q2 (computational).** A 70 kg person stands on a scale in an elevator accelerating
upward at $2\,\text{m/s}^2$. What does the scale read?

??? success "Answer"
    $N - mg = ma \Rightarrow N = m(g + a) = 70(11.8) = 826\,\text{N}$ — about 84 kg
    "apparent weight". Descending at the same rate it would read 546 N.

**Q3 (multiple choice).** An object moves at constant velocity. The net force on it
is: (a) constant and nonzero (b) in the direction of motion (c) zero

??? success "Answer"
    **(c)** — first law. Any nonzero net force would change the velocity.

**Q4 (conceptual).** Why does a small car and a huge truck experience the *same*
force magnitude in a collision, yet the car fares worse?

??? success "Answer"
    Third law guarantees equal forces. But $a = F/m$: the same force gives the lighter
    car a much larger acceleration (and its occupants larger accelerations too).
