# Projectile Motion

*Source lecture(s):* [SC133 Lec 4](../lectures.md)

## Intuition

Throw a ball: gravity pulls straight down and *nothing* pulls sideways. So the
horizontal motion coasts at constant velocity while the vertical motion is ordinary
free fall — **two independent 1-D problems sharing a clock**. The graceful parabola is
just a straight line (horizontal) plus a dropped ball (vertical), superimposed.
Galileo's famous demonstration: a bullet fired horizontally and one dropped at the
same instant hit the ground together.

## The equations

Launch speed $v_0$ at angle $\theta$ above the horizontal (no air resistance):

$$x(t) = v_0\cos\theta\; t \qquad\qquad y(t) = v_0\sin\theta\; t - \tfrac12 g t^2$$

$$v_x = v_0\cos\theta \;(\text{constant}) \qquad v_y = v_0\sin\theta - g t$$

Eliminating $t$ gives the trajectory — a parabola:

$$y = x\tan\theta - \frac{g\,x^2}{2 v_0^2 \cos^2\theta}$$

## The classic results (level ground)

| Quantity | Formula | Maximized when |
|---|---|---|
| Time of flight | $T = \dfrac{2v_0\sin\theta}{g}$ | $\theta = 90°$ |
| Maximum height | $H = \dfrac{v_0^2\sin^2\theta}{2g}$ | $\theta = 90°$ |
| Range | $R = \dfrac{v_0^2\sin 2\theta}{g}$ | $\theta = 45°$ |

Complementary angles ($30°$ and $60°$) give the *same range* — one flies high and
slow, the other low and fast.

## The parabola of safety

Fire projectiles at fixed speed $v_0$ in every direction. No shot can ever cross the
envelope

$$y = \frac{v_0^2}{2g} - \frac{g\,x^2}{2 v_0^2}$$

— the **parabola of safety**. Anything outside it is unreachable. (This envelope is
the star of the [PHY653 warm-up simulation](../../comp-plasma/concepts/simulation-driven-plasma-physics.md).)

## Worked example: clearing a wall

A ball is kicked at $20\,\text{m/s}$, $45°$, toward a $5\,\text{m}$ wall
$30\,\text{m}$ away. Does it clear?

At $x = 30$: $t = 30/(20\cos45°) = 2.12\,\text{s}$.
Height: $y = 20\sin45°(2.12) - 4.9(2.12)^2 = 30.0 - 22.0 = 8.0\,\text{m}$ — clears by
3 m. ✓

## Try it live

The **[projectile playground](../simulations/projectile-playground.md)** lets you
drag the launch angle and speed, watch range and height respond, and see the parabola
of safety emerge from many trajectories.

## Common mistakes

- **Letting gravity touch the horizontal motion.** $v_x$ never changes (without drag);
  only $v_y$ does.
- **Using $45°$ as optimal when launch and landing heights differ** — from a cliff the
  optimum is *less* than 45°.
- **Forgetting the two motions share time $t$.** The link between $x$ and $y$
  equations is the common clock — solve for $t$ in one, substitute into the other.
- Real balls feel [air drag](friction-and-drag.md): trajectories are shorter and
  asymmetric, and the optimum angle drops to ~35° for a golf ball.

## Related concepts

- [Kinematics](kinematics.md) & [Vectors](vectors.md) — the ingredients
- [Circular motion](circular-motion.md) — the other classic 2-D motion
- [Friction & drag](friction-and-drag.md) — why real trajectories aren't parabolas
- [Projectile playground (live demo)](../simulations/projectile-playground.md)

## Knowledge graph position

**Prerequisites:** [Kinematics](kinematics.md), [Vectors](vectors.md).
**Leads to:** [Circular motion](circular-motion.md), [orbital motion](keplers-laws.md) — a cannonball fired fast enough *is* a satellite.

## Quiz

**Q1 (computational).** A projectile launched at $\theta = 30°$, $v_0 = 40\,\text{m/s}$
on level ground: find the range.

??? success "Answer"
    $R = v_0^2\sin(2\theta)/g = 1600\times\sin 60°/9.8 = 1600(0.866)/9.8 \approx 141\,\text{m}$.

**Q2 (conceptual).** At the top of its arc, is the projectile's speed zero?

??? success "Answer"
    No — only $v_y = 0$. It still moves horizontally at $v_0\cos\theta$; speed is at
    its *minimum*, not zero. (Contrast a ball thrown straight up.)

**Q3 (conceptual).** Two identical balls: one dropped, one launched horizontally from
the same height. Which lands first?

??? success "Answer"
    They tie. Vertical motion is identical (same initial $v_y = 0$, same $g$);
    horizontal velocity is irrelevant to the fall — the independence of components.

**Q4 (multiple choice).** Doubling the launch speed multiplies the level-ground range
by: (a) 2 (b) $\sqrt2$ (c) 4

??? success "Answer"
    **(c)** — $R \propto v_0^2$. This quadratic sensitivity is why muzzle velocity
    dominates artillery design.
