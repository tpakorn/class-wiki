# The Pendulum

*Source lecture(s):* [SC133 Lec 21](../lectures.md)

## Intuition

A mass on a string, pulled aside and released, swings with a rhythm so steady it
timed civilization's clocks for 300 years. For small swings it is
[simple harmonic motion](simple-harmonic-motion.md) with gravity playing the spring —
and its most famous property is what it *doesn't* depend on: the mass and (for small
angles) the amplitude.

## The simple pendulum

Tangential Newton's law for a bob on a string of length $L$ at angle $\theta$:

$$mL\ddot\theta = -mg\sin\theta$$

**Small-angle approximation** $\sin\theta \approx \theta$ (good to 1% below ~14°):

$$\ddot\theta = -\frac{g}{L}\,\theta
\quad\Rightarrow\quad
\boxed{\,\omega = \sqrt{\frac{g}{L}}, \qquad T = 2\pi\sqrt{\frac{L}{g}}\,}$$

- **Mass cancels** — the same equivalence of inertial and gravitational mass behind
  [Galileo's falling bodies](gravitation.md).
- Longer pendulum, slower swing: a 1 m pendulum ticks $T \approx 2.0$ s (the
  historical "seconds pendulum" — one second per half-swing).
- Measure $T$ and $L$, and you've measured $g$: the classic first-year lab.

Beyond small angles, the period *grows* with amplitude
($T \approx T_0[1 + \theta_0^2/16 + \dots]$) — pendulum clocks needed small,
constant swings.

## The physical pendulum

Any rigid body swinging about a pivot: replace force balance with
[torque](torque.md) about the pivot,

$$I\ddot\theta = -mgd\sin\theta
\quad\Rightarrow\quad
T = 2\pi\sqrt{\frac{I}{mgd}}$$

where $d$ is pivot-to-[CM](center-of-mass.md) distance and $I$ the
[moment of inertia](moment-of-inertia.md) about the pivot. Check: a rod pivoted at
its end ($I = \tfrac13 mL^2$, $d = L/2$) gives
$T = 2\pi\sqrt{2L/3g}$ — swings like a simple pendulum of length $\tfrac23 L$.

## Worked example: pendulum on the Moon

Your grandfather clock keeps perfect time on Earth. On the Moon
($g_M = g/6$), each period stretches by $\sqrt6 \approx 2.45$: the clock runs
**slow by a factor 2.45**. Pendulum clocks are gravimeters in disguise — expedition
scientists once mapped $g$ (and thus Earth's shape) by timing pendulums.

## Energy view

$U = mgL(1 - \cos\theta)$ from the lowest point; release from $\theta_0$ gives bottom
speed $v = \sqrt{2gL(1 - \cos\theta_0)}$ — pure
[energy conservation](conservation-of-energy.md), valid at *any* amplitude (unlike
the small-angle period).

## Common mistakes

- **Including the mass in the period.** It cancels — a lead bob and a wooden bob of
  equal length keep identical time.
- **Using the small-angle formula for large swings** — at $\theta_0 = 90°$ the true
  period is ~18% longer.
- **Confusing $L$ with the string length for a physical pendulum** — you need $I$ and
  $d$, not just geometry's longest line.
- **Assuming tension does work** — it's always ⊥ motion; only gravity trades energy.

## Related concepts

- [Simple harmonic motion](simple-harmonic-motion.md) — the framework
- [Torque](torque.md) & [Moment of inertia](moment-of-inertia.md) — the physical pendulum
- [Damped & driven oscillations](damped-oscillations.md) — real pendulums run down
- [Measurement](measurement.md) — dimensional analysis *predicts* $T \propto \sqrt{L/g}$

## Knowledge graph position

**Prerequisites:** [SHM](simple-harmonic-motion.md), [Torque](torque.md).
**Leads to:** [Damped oscillations](damped-oscillations.md); historically, to precision timekeeping and gravimetry.

## Quiz

**Q1 (computational).** What length pendulum has a period of exactly 1 s on Earth?

??? success "Answer"
    $L = g(T/2\pi)^2 = 9.8/(4\pi^2)\times1 \approx 0.248\,\text{m}$ — about 25 cm.

**Q2 (conceptual).** A pendulum clock is moved from sea level to a high mountain.
Fast or slow?

??? success "Answer"
    Slow: $g$ decreases with altitude, so $T = 2\pi\sqrt{L/g}$ lengthens. (Correcting
    clocks like this is literally how $g$-variations were first surveyed.)

**Q3 (multiple choice).** A child stands up on a moving swing. The period:
(a) increases (b) decreases (c) unchanged

??? success "Answer"
    **(b).** Standing raises the CM toward the pivot — shorter effective $L$, shorter
    period. (Kneeling/standing rhythmically is also how you *pump* a swing.)
