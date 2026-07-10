# Simple Harmonic Motion

*Source lecture(s):* [SC133 Lec 20](../lectures.md)

## Intuition

Displace almost anything slightly from stable equilibrium — a mass on a spring, a
swing, a molecule in a crystal, a ship on water — and it oscillates the same way:
sinusoidally. The reason is universal: near any
[energy-valley bottom](potential-energy.md), the restoring force is proportional to
displacement ($F = -kx$), and that one law has exactly one kind of solution. SHM is
not one system among many; it is the *local behavior of every stable system in
physics*.

## The equation and its solution

Newton's second law with a linear restoring force:

$$m\ddot x = -kx
\qquad\Longrightarrow\qquad
\ddot x = -\omega^2 x, \quad \omega = \sqrt{\frac{k}{m}}$$

Solution (see the [equation page](../equations/shm-differential-equation.md)):

$$x(t) = A\cos(\omega t + \phi)$$

- **Amplitude** $A$: set by initial conditions
- **Phase** $\phi$: where in the cycle you start
- **Angular frequency** $\omega$: set by the *system* ($k$, $m$) — **not by the
  amplitude**. Period $T = 2\pi\sqrt{m/k}$, frequency $f = 1/T = \omega/2\pi$.

That amplitude-independence (*isochronism*) is SHM's signature — it's why springs
and pendulums could run clocks.

Velocity and acceleration follow by differentiation:
$v = -A\omega\sin(\omega t + \phi)$ (max $A\omega$ at center),
$a = -A\omega^2\cos(\omega t + \phi)$ (max $A\omega^2$ at extremes).

## Energy in SHM

$$E = \tfrac12 kA^2 = \underbrace{\tfrac12 mv^2}_{\text{max at center}}
+ \underbrace{\tfrac12 kx^2}_{\text{max at turning points}}$$

Energy sloshes between kinetic and potential twice per cycle; the total is constant
and proportional to *amplitude squared* — a scaling that echoes through
[waves](waves.md) and light.

## SHM and circular motion

SHM is the shadow of [uniform circular motion](circular-motion.md): project a point
moving on a circle of radius $A$ at angular speed $\omega$ onto a diameter and you
get $A\cos\omega t$ exactly. This is why the "angular" frequency of a linear
oscillator is measured in rad/s, and why phasors work.

## Worked example: car suspension

A 1200 kg car settles 3 cm when its 80 kg driver enters. Estimate the bounce
frequency.

Spring constant: $k = mg/x = 80(9.8)/0.03 \approx 2.6\times10^4\,\text{N/m}$… per
settling, for the whole suspension. Then

$$f = \frac{1}{2\pi}\sqrt{\frac{k}{M}} = \frac{1}{2\pi}\sqrt{\frac{2.6\times10^4}{1280}} \approx 0.7\,\text{Hz}$$

— about right for a comfortable car (1 Hz-ish; sports cars run stiffer/faster).

## Try it live

The **[oscillator lab](../simulations/shm-lab.md)** lets you drag mass, spring
constant, damping and driving frequency, and watch $x(t)$ and the resonance curve
respond.

## Common mistakes

- **Thinking bigger swings take longer.** For ideal SHM, period is
  amplitude-independent — larger $A$ means proportionally larger speeds.
- **Maximum acceleration at the center?** No: $a \propto -x$ — acceleration is
  *zero* at the center (where speed peaks) and maximal at the turning points.
- **Using $\omega = \sqrt{k/m}$ for a pendulum** — the pendulum's "$k$" is
  $mg/L$; see [pendulum](pendulum.md).
- **Confusing $\omega$ (rad/s) with $f$ (Hz)** — a factor $2\pi$ that ruins exam
  answers.

## Related concepts

- [Potential energy](potential-energy.md) — why valleys ⇒ SHM
- [Pendulum](pendulum.md) — SHM's most famous example
- [Damped & driven oscillations](damped-oscillations.md) — reality's corrections
- [Waves](waves.md) — SHM handed from particle to particle
- [SHM differential equation (reference)](../equations/shm-differential-equation.md)

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md), [Potential energy](potential-energy.md), [Circular motion](circular-motion.md).
**Leads to:** [Pendulum](pendulum.md), [Damped oscillations](damped-oscillations.md), [Waves](waves.md) — and, eventually, every "normal mode" in physics, from [plasma oscillations](../../plasma/concepts/plasma-frequency.md) to quantum fields.

## Quiz

**Q1 (computational).** A 0.5 kg mass on a 200 N/m spring is pulled 10 cm and
released. Find $\omega$, the period, and the maximum speed.

??? success "Answer"
    $\omega = \sqrt{200/0.5} = 20\,\text{rad/s}$; $T = 2\pi/\omega \approx 0.31\,\text{s}$;
    $v_\text{max} = A\omega = 0.1\times20 = 2\,\text{m/s}$.

**Q2 (conceptual).** Where in the cycle are speed, acceleration, and elastic PE each
maximal?

??? success "Answer"
    Speed: at the center ($x=0$). Acceleration and PE: at the turning points
    ($x = \pm A$). KE and PE trade places twice per period.

**Q3 (multiple choice).** Doubling the amplitude of SHM multiplies the total energy
by: (a) 2 (b) 4 (c) leaves the period unchanged and the energy ×4 — both

??? success "Answer"
    **(c).** $E = \frac12 kA^2 \to 4E$, while $T = 2\pi\sqrt{m/k}$ never noticed the
    amplitude.

**Q4 (conceptual).** Why does *every* small oscillation look simple harmonic,
whatever the system?

??? success "Answer"
    Taylor-expand any potential about a minimum:
    $U \approx U_0 + \frac12 U''(x_0)(x-x_0)^2$ — the linear term vanishes at
    equilibrium, and the quadratic term *is* a spring with $k = U''(x_0)$. Nature
    reuses one solution everywhere.
