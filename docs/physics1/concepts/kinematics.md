# Motion in One Dimension (Kinematics)

*Source lecture(s):* [SC133 Lec 2](../lectures.md)

## Intuition

Kinematics is the *description* of motion — where something is, how fast it moves, how
that speed changes — without yet asking *why* (that's [Newton's laws](newtons-laws.md)).
Three quantities do all the work: **position**, its rate of change **velocity**, and
*its* rate of change **acceleration**. Each is the slope of the graph of the one
before.

## The three quantities

**Displacement** $\Delta x = x_f - x_i$ — the *change* in position (a vector; can be
negative). Distinct from *distance travelled*, the path length, which never decreases.

**Velocity** — rate of change of position:

$$v_\text{avg} = \frac{\Delta x}{\Delta t}, \qquad v = \frac{dx}{dt}$$

Average velocity is the slope of the secant on an $x$–$t$ graph; instantaneous
velocity is the slope of the tangent.

**Acceleration** — rate of change of velocity:

$$a_\text{avg} = \frac{\Delta v}{\Delta t}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

## The kinematic equations (constant acceleration)

When $a$ is constant, integrating $a = dv/dt$ and $v = dx/dt$ gives the four workhorse
equations (full derivation on the [equation page](../equations/kinematic-equations.md)):

$$v = v_0 + at \qquad x = x_0 + v_0 t + \tfrac12 a t^2$$

$$v^2 = v_0^2 + 2a(x - x_0) \qquad x = x_0 + \tfrac12(v_0 + v)t$$

The most useful trick: pick the equation that omits the variable you neither know nor
want.

## Reading motion graphs

| Graph | Slope gives | Area under gives |
|---|---|---|
| $x$ vs $t$ | velocity | — |
| $v$ vs $t$ | acceleration | displacement |
| $a$ vs $t$ | jerk | change in velocity |

Fluency at moving between these three graphs is worth more on the exam than memorizing
the four equations.

## Worked example: free fall

A ball is thrown straight up at $v_0 = 20\,\text{m/s}$ ($g = 9.8\,\text{m/s}^2$
downward). How high does it go, and when does it return?

At the top $v = 0$: from $v^2 = v_0^2 - 2gh$,
$h = v_0^2/2g = 400/19.6 \approx 20.4\,\text{m}$.
Time up: $t = v_0/g \approx 2.04\,\text{s}$; total flight $\approx 4.08\,\text{s}$
(symmetry: up-time equals down-time in free fall).

## Common mistakes

- **Confusing displacement with distance** (and velocity with speed). Displacement and
  velocity are vectors; a round trip has zero displacement but nonzero distance.
- **Using the constant-$a$ equations when $a$ isn't constant** (e.g. with
  [drag](friction-and-drag.md)). Then you must integrate the actual $a(t)$.
- **Sign errors.** Choose a positive direction *once* and stick to it — $g$ is $-9.8$
  if up is positive.

## Related concepts

- [Vectors](vectors.md) — kinematics in 2-D and 3-D needs them
- [Projectile motion](projectile-motion.md) — constant-$a$ kinematics in two dimensions
- [Newton's laws](newtons-laws.md) — the *cause* of acceleration
- [Kinematic equations (reference)](../equations/kinematic-equations.md)

## Knowledge graph position

**Prerequisites:** [Measurement & units](measurement.md).
**Leads to:** [Vectors](vectors.md), [projectile motion](projectile-motion.md), [circular motion](circular-motion.md), [Newton's laws](newtons-laws.md).

## Quiz

**Q1 (computational).** A car brakes from $30\,\text{m/s}$ to rest over $75\,\text{m}$.
What is its (constant) acceleration?

??? success "Answer"
    $v^2 = v_0^2 + 2a\Delta x \Rightarrow 0 = 900 + 2a(75) \Rightarrow a = -6\,\text{m/s}^2$.

**Q2 (conceptual).** On a $v$–$t$ graph, what does the area between the curve and the
time axis represent?

??? success "Answer"
    Displacement: $\Delta x = \int v\,dt$. Area above the axis is positive
    displacement, area below is negative.

**Q3 (conceptual).** Two balls are dropped one second apart. Does the gap between them
stay constant, grow, or shrink?

??? success "Answer"
    Grows. Both accelerate identically, but the first always leads in *velocity* by
    $g\tau$, so the separation increases linearly: $\Delta = g\tau t$ with $\tau=1$ s.

**Q4 (multiple choice).** At the very top of its flight, an object thrown upward has:
(a) zero velocity and zero acceleration (b) zero velocity, acceleration $g$ downward
(c) maximum velocity

??? success "Answer"
    **(b).** Velocity passes through zero, but gravity never switches off — $a=g$
    downward the entire time.
