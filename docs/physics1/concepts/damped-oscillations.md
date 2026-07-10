# Damped & Driven Oscillations, Resonance

*Source lecture(s):* [SC133 Lec 21](../lectures.md)

## Intuition

Real oscillators run down: friction and drag bleed energy, and the sinusoid decays
inside a shrinking envelope. Push back rhythmically and you can sustain the motion —
and if you push **at the oscillator's own frequency**, tiny efforts build enormous
swings. That amplification is **resonance**: the reason a child's swing responds to
gentle, well-timed pushes, radios select stations, and soldiers break step on
bridges.

## Damped oscillations

Add a velocity-proportional drag $-b\dot x$ to the [SHM equation](simple-harmonic-motion.md):

$$m\ddot x + b\dot x + kx = 0$$

For light damping the solution is a decaying sinusoid:

$$x(t) = A\,e^{-bt/2m}\cos(\omega' t + \phi), \qquad
\omega' = \sqrt{\omega_0^2 - \left(\frac{b}{2m}\right)^2}$$

- The amplitude envelope decays with time constant $\tau = 2m/b$; energy
  ($\propto A^2$) decays twice as fast.
- Frequency shifts *down* slightly — usually negligibly.

**Three regimes:**

| Regime | Condition | Behavior |
|---|---|---|
| Underdamped | $b < 2\sqrt{km}$ | oscillates, decays |
| Critically damped | $b = 2\sqrt{km}$ | fastest return, no overshoot |
| Overdamped | $b > 2\sqrt{km}$ | slow creep back |

Car suspensions and door closers are tuned near **critical** damping — return
quickly, don't bounce.

## Driven oscillations & resonance

Drive with a periodic force $F_0\cos\omega_d t$ and, after transients die, the system
oscillates *at the driving frequency* with amplitude

$$A(\omega_d) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega_d^2)^2 + (b\omega_d/m)^2}}$$

- Peak near $\omega_d \approx \omega_0$: **resonance**.
- Peak height and sharpness are set by damping — the quality factor
  $Q = \omega_0 m/b$ counts (roughly) the oscillations before the energy decays by
  $e^{2\pi}$; high-$Q$ systems ring long and resonate sharply.

**Resonance in the wild:** pushing a swing · tuning circuits
([the same curve in SC134's RLC lab](../../sc134/simulations/rc-rlc-lab.md)) ·
microwave ovens driving water molecules · opera singers and wine glasses · the
Tacoma Narrows bridge (aeroelastic flutter — resonance's dramatic cousin) · MRI
machines resonating nuclear spins.

## Worked example: how many swings?

A pendulum with $Q = 300$ (typical clock pendulum) loses what fraction of energy per
cycle?

$$\frac{\Delta E}{E} \approx \frac{2\pi}{Q} = \frac{2\pi}{300} \approx 2\%$$

— which is exactly the energy the escapement mechanism must replace each swing to
keep the clock running at constant amplitude.

## Try it live

The **[oscillator lab](../simulations/shm-lab.md)** has damping and driving sliders:
sweep the drive frequency across $\omega_0$ and watch the amplitude peak — then
increase damping and watch the peak flatten.

## Common mistakes

- **Expecting the driven system to move at its natural frequency.** Steady state
  follows the *drive*; $\omega_0$ only decides the amplitude.
- **"More damping always means less motion."** Below resonance, damping barely
  matters; and critical damping *returns* fastest — overdamping is slower.
- **Confusing resonance with matching any frequency** — the match must be to
  $\omega_0$ (or, for swings pumped by kneeling, $2\omega_0$ — parametric resonance).
- **Forgetting transients.** Right after switch-on, the motion is a mix of natural
  and driven oscillations; the formulas above describe the long run.

## Related concepts

- [SHM](simple-harmonic-motion.md) — the undamped ideal
- [Friction & drag](friction-and-drag.md) — where $b\dot x$ comes from
- [RLC resonance (SC134)](../../sc134/simulations/rc-rlc-lab.md) — identical mathematics, electrical costume
- [Driven plasma oscillations (PC368)](../../plasma/concepts/plasma-frequency.md)

## Knowledge graph position

**Prerequisites:** [SHM](simple-harmonic-motion.md), [Friction & drag](friction-and-drag.md).
**Leads to:** [Waves](waves.md), AC circuits (SC134), every spectroscopy.

## Quiz

**Q1 (conceptual).** Why do soldiers break step crossing a footbridge?

??? success "Answer"
    Marching in step delivers a periodic force; if its frequency lands near the
    bridge's $\omega_0$, resonance pumps the amplitude cycle after cycle. Random
    steps spread the force over frequencies, starving the resonance.

**Q2 (computational).** An oscillator has $m = 0.2$ kg, $k = 80$ N/m, $b = 0.4$ kg/s.
Underdamped? Find $Q$.

??? success "Answer"
    $2\sqrt{km} = 2\sqrt{16} = 8 \gg 0.4$: strongly underdamped.
    $\omega_0 = 20\,\text{rad/s}$, $Q = \omega_0 m/b = 20(0.2)/0.4 = 10$.

**Q3 (multiple choice).** For the *fastest* return to equilibrium without overshoot,
choose damping: (a) as small as possible (b) critical (c) as large as possible

??? success "Answer"
    **(b).** The definition of critical damping — and the design point of shock
    absorbers and analog meter needles.
