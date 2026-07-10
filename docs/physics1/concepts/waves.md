# Traveling Waves

*Source lecture(s):* [SC133 Lec 22](../lectures.md)

## Intuition

Flick a rope: a bump races along it, yet no piece of rope travels with the bump —
each piece only bobs in place, briefly, handing the motion to its neighbor. **A wave
transports energy and information without transporting matter.** Stadium waves, sound,
light, earthquakes: the pattern moves; the medium (if any) stays home.

## Describing a wave

A sinusoidal wave moving in $+x$:

$$y(x, t) = A\sin(kx - \omega t + \phi)$$

| Symbol | Name | Meaning |
|---|---|---|
| $A$ | amplitude | maximum displacement |
| $k = 2\pi/\lambda$ | wave number | radians per metre |
| $\omega = 2\pi f$ | angular frequency | radians per second |
| $\lambda$ | wavelength | spatial period |
| $T = 1/f$ | period | temporal period |

The pattern repeats in space every $\lambda$ and in time every $T$; a crest advances
at the **phase speed**

$$\boxed{\,v = \lambda f = \frac{\omega}{k}\,}$$

Sign flip ($kx + \omega t$) reverses the direction. **Transverse** waves displace ⊥
to travel (rope, light); **longitudinal** waves displace along it
([sound](sound-waves.md)).

## What sets the speed: the medium

For a stretched string with tension $F_T$ and linear density $\mu$ (kg/m):

$$v = \sqrt{\frac{F_T}{\mu}}$$

The pattern is universal: $v = \sqrt{\text{restoring property}/\text{inertia
property}}$ — tension/density here, stiffness/density for sound,
[gravity/depth for water waves](../../fluids/equations/interface-dispersion-relation.md).
Speed belongs to the *medium*; frequency belongs to the *source*; wavelength adjusts:
$\lambda = v/f$.

## The wave equation

Newton's second law applied to a string element yields

$$\frac{\partial^2 y}{\partial t^2} = v^2\,\frac{\partial^2 y}{\partial x^2}$$

— the archetypal wave equation. *Any* function of $(x \mp vt)$ solves it: shape in,
shape out, moving at $v$. This same PDE returns for sound, light
([SC134](../../sc134/concepts/electromagnetic-waves.md)), and gets solved numerically
in [PHY653's FDTD](../../comp-plasma/concepts/fdtd-method.md).

## Energy transport

Each element does SHM with the wave's frequency; the average power carried by a
sinusoidal string wave is

$$P = \tfrac12 \mu \omega^2 A^2 v$$

Energy flow $\propto A^2$ and $\propto \omega^2$ — amplitude-squared scaling is a
theme from [SHM](simple-harmonic-motion.md) through optics.

## Worked example: guitar string

A 65 cm guitar string ($\mu = 6\times10^{-3}$ kg/m) is tuned to 110 Hz (A2)
fundamental. Required tension? (Fundamental: $\lambda = 2L$; see
[standing waves](superposition.md).)

$v = \lambda f = 1.3\times110 = 143\,\text{m/s}$;
$F_T = \mu v^2 = 6\times10^{-3}\times(143)^2 \approx 123\,\text{N}$ — about 12.5 kg
of pull. Six strings ⇒ nearly 70 kg on the neck, which is why guitars have truss
rods.

## Try it live

The **[wave studio](../simulations/wave-studio.md)** animates traveling waves and
their superposition — drag frequency and speed, then switch to standing-wave and
beats modes.

## Common mistakes

- **The medium travels with the wave.** No — watch a floating leaf as ripples pass:
  it circles in place.
- **"Higher frequency means faster wave."** In a non-dispersive medium, $v$ is fixed;
  raising $f$ just shortens $\lambda$.
- **Confusing wave speed with particle speed.** The string element's speed
  ($\partial y/\partial t$, max $A\omega$) is unrelated to the pattern speed $v$.
- **Mixing $k$ and $\omega$ roles** — $k$ counts radians per metre, $\omega$ per
  second; their ratio, not either alone, is the speed.

## Related concepts

- [SHM](simple-harmonic-motion.md) — each medium element's motion
- [Superposition & standing waves](superposition.md) — waves meeting waves
- [Sound waves](sound-waves.md) — longitudinal cousin
- [Wave studio (live demo)](../simulations/wave-studio.md)

## Knowledge graph position

**Prerequisites:** [SHM](simple-harmonic-motion.md).
**Leads to:** [Superposition](superposition.md), [Sound](sound-waves.md), [EM waves (SC134)](../../sc134/concepts/electromagnetic-waves.md), [plasma waves (PC368)](../../plasma/concepts/plasma-waves.md).

## Quiz

**Q1 (computational).** A wave $y = 0.02\sin(4\pi x - 200\pi t)$ (SI). Find $\lambda$,
$f$, and $v$.

??? success "Answer"
    $k = 4\pi \Rightarrow \lambda = 0.5\,\text{m}$;
    $\omega = 200\pi \Rightarrow f = 100\,\text{Hz}$;
    $v = \omega/k = 50\,\text{m/s}$ (moving in $+x$).

**Q2 (conceptual).** You double the tension in a string while the attached oscillator
keeps the same frequency. What happens to $v$ and $\lambda$?

??? success "Answer"
    $v = \sqrt{F_T/\mu}$ grows by $\sqrt2$; frequency is fixed by the source, so
    $\lambda = v/f$ also grows by $\sqrt2$.

**Q3 (multiple choice).** A wave pulse travels down a rope. The rope's material moves:
(a) along with the pulse (b) perpendicular to the rope, briefly (c) not at all

??? success "Answer"
    **(b).** Transverse motion only — each element bobs and settles as the pulse
    passes through it.
