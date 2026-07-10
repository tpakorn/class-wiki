# Superposition, Interference & Standing Waves

*Source lecture(s):* [SC133 Lec 23](../lectures.md)

## Intuition

Two waves in the same medium don't collide — they **add**, point by point, instant by
instant, then pass through each other unchanged. That politeness (linearity) has loud
consequences: waves can reinforce into double heights (**constructive interference**),
cancel into silence (**destructive**), or — when a wave meets its own reflection —
freeze into a **standing wave** that oscillates in place. Every musical instrument is
a standing-wave machine.

## The superposition principle

$$y_\text{total}(x,t) = y_1(x,t) + y_2(x,t)$$

Two equal sinusoids offset by phase $\phi$:

$$y = \left[2A\cos\frac{\phi}{2}\right]\sin\left(kx - \omega t + \frac{\phi}{2}\right)$$

- $\phi = 0$: amplitude $2A$ — fully constructive
- $\phi = \pi$ (half a wavelength of path difference): amplitude $0$ — fully
  destructive

**Path-difference rule** for two sources in step: constructive where
$\Delta L = m\lambda$, destructive where $\Delta L = (m + \tfrac12)\lambda$ — the
fringe logic that reappears with light (SC134) and in the
[FDTD double-slit simulation](../../comp-plasma/examples/double-slit-fdtd.md).

## Standing waves

Add identical waves traveling in *opposite* directions (e.g., incident + reflected):

$$y = A\sin(kx - \omega t) + A\sin(kx + \omega t) = \boxed{\,2A\sin kx\,\cos\omega t\,}$$

Space and time have **separated**: every point oscillates in step, with a
position-dependent amplitude. **Nodes** (never move) sit every $\lambda/2$;
**antinodes** (maximum swing) between them. No net energy travels — it's trapped,
sloshing between the nodes.

## Normal modes of a string

A string fixed at both ends demands nodes at $x = 0, L$, so only certain wavelengths
fit:

$$\lambda_n = \frac{2L}{n}, \qquad
f_n = \frac{nv}{2L} = n f_1, \qquad n = 1, 2, 3, \dots$$

The **fundamental** $f_1 = v/2L$ sets the pitch; the **harmonics** $2f_1, 3f_1,\dots$
color the timbre — why a guitar and violin playing the same note sound different.
Tuning = changing $v = \sqrt{F_T/\mu}$ (tension pegs) or $L$ (frets).

These discrete allowed patterns are physics' first **eigenmode problem** — the same
mathematics that later quantizes [PDE solutions (PHY621)](../../phy621/concepts/partial-differential-equations.md)
and electron orbitals.

## Worked example: which harmonics?

A 0.9 m string has wave speed 360 m/s. A tuner drives it at 800 Hz. Does it resonate?

$f_1 = v/2L = 200\,\text{Hz}$; harmonics at 200, 400, 600, **800** ✓ — yes, the
$n = 4$ mode, with 3 interior nodes.

## Try it live

The **[wave studio](../simulations/wave-studio.md)** superposes two waves live —
flip the second wave's direction to build standing waves and watch nodes appear;
detune the frequencies slightly to preview [beats](beats.md).

## Common mistakes

- **Expecting waves to bounce off each other.** They overlap and continue — only the
  *displacement* adds while they share space.
- **"Destructive interference destroys energy."** Energy is redistributed to the
  constructive regions; the books always balance.
- **Confusing nodes with antinodes**, and node spacing ($\lambda/2$) with $\lambda$.
- **Forgetting boundary conditions choose the modes.** One fixed + one free end
  (organ pipes closed at one end) gives odd harmonics only — different physics,
  same recipe.

## Related concepts

- [Traveling waves](waves.md) — the ingredients
- [Beats](beats.md) — interference in *time* instead of space
- [Sound waves](sound-waves.md) — pipes, voices, and room acoustics
- [Fourier series (PHY621)](../../phy621/concepts/fourier-series.md) — any string shape = sum of modes

## Knowledge graph position

**Prerequisites:** [Traveling waves](waves.md).
**Leads to:** [Beats](beats.md), [Sound](sound-waves.md), musical acoustics, [eigenmode thinking everywhere](../../phy621/concepts/eigenvalues-eigenvectors.md).

## Quiz

**Q1 (computational).** Two speakers, in phase, face you: one 3.0 m away, the other
3.85 m. For sound at 400 Hz ($v = 340$ m/s), loud or quiet?

??? success "Answer"
    $\lambda = 0.85\,\text{m}$; $\Delta L = 0.85\,\text{m} = 1\lambda$ —
    **constructive**: loud.

**Q2 (conceptual).** Noise-cancelling headphones exploit which phenomenon, and what
must they generate?

??? success "Answer"
    Destructive interference: an "anti-noise" wave with equal amplitude and opposite
    phase ($\phi = \pi$) to the incoming sound at the ear — superposition sums to
    near-silence.

**Q3 (multiple choice).** On a string fixed at both ends vibrating in its third
harmonic, the number of nodes (including the ends) is:
(a) 2 (b) 3 (c) 4

??? success "Answer"
    **(c).** $n = 3$ means three half-wavelength loops: nodes at both ends + two
    interior — four total, three antinodes.
