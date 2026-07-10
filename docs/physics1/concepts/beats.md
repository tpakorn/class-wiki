# Beats

*Source lecture(s):* [SC133 Lec 25](../lectures.md)

## Intuition

Play two tones *almost* in tune — 440 Hz and 442 Hz — and you hear a single note that
throbs: *wah–wah–wah*, twice per second. The waves drift in and out of step, adding
when aligned and cancelling when opposed. Beats are
[interference](superposition.md) unfolding **in time** rather than in space — and the
most sensitive tuner nature ever gave a musician's ear.

## The mathematics

Add equal-amplitude tones at $f_1$ and $f_2$ (product-to-sum identity):

$$y = A\cos(2\pi f_1 t) + A\cos(2\pi f_2 t)
= \underbrace{2A\cos\!\big(2\pi \tfrac{f_1 - f_2}{2} t\big)}_{\text{slow envelope}}
\;\underbrace{\cos\!\big(2\pi \tfrac{f_1 + f_2}{2} t\big)}_{\text{fast carrier}}$$

You hear the **average** frequency, modulated by a slow envelope. The loudness peaks
**twice** per envelope cycle, so

$$\boxed{\,f_\text{beat} = |f_1 - f_2|\,}$$

440 & 442 Hz ⇒ a 441 Hz tone beating 2 times per second.

## Tuning by beats

Slow beats = nearly in tune. A tuner adjusts until the beats *slow to zero* — the ear
detects sub-hertz mismatches this way, far beyond its ability to compare pitches
directly. Piano technicians, guitarists using harmonics, and orchestras tuning to the
oboe all listen for the wobble, not the pitch.

## Beyond music

- **Superheterodyne radio & radar guns:** mix a received signal with a local
  oscillator; the beat ("intermediate") frequency is easy to measure — police radar
  literally hears the beat between sent and Doppler-shifted returns.
- **Optical beats** between lasers measure tiny frequency differences.
- **Binaural beats** (one tone per ear) are constructed by your brain — a perception
  experiment hiding in headphones.

## Worked example: tuning a guitar string

Your A-string against a 110 Hz reference produces beats every 0.5 s. How far off are
you?

$f_\text{beat} = 1/0.5 = 2\,\text{Hz}$ ⇒ the string is at 108 or 112 Hz. Tighten
slightly: beats *speed up* ⇒ you were sharp (112 Hz) — reverse. When the wobble
dies, you're tuned.

## Try it live

In the **[wave studio](../simulations/wave-studio.md)**, set the two frequencies a
few hertz apart and watch the envelope form — then close the gap and watch the beats
slow to nothing.

## Common mistakes

- **Halving the beat frequency.** The envelope $\cos(2\pi\frac{\Delta f}{2}t)$ peaks
  twice per cycle — the audible beat rate is the *full* $|f_1 - f_2|$.
- **Expecting beats from far-apart frequencies.** Beyond ~15 Hz difference the throb
  blurs into roughness, then into two separate tones.
- **Confusing beats with [standing waves](superposition.md)** — beats are temporal
  interference of *different* frequencies; standing waves are spatial interference of
  *equal* frequencies.

## Related concepts

- [Superposition](superposition.md) — the parent principle
- [Sound waves](sound-waves.md) — where you hear them
- [Wave studio (live demo)](../simulations/wave-studio.md)
- [Wave–wave interactions in plasmas (PC368)](../../plasma/concepts/plasma-waves.md)

## Knowledge graph position

**Prerequisites:** [Superposition](superposition.md), [Sound waves](sound-waves.md).
**Leads to:** signal processing, radio engineering (SC134 and beyond).

## Quiz

**Q1 (computational).** A 256 Hz tuning fork with a slightly loaded 260 Hz fork:
beat frequency?

??? success "Answer"
    $|260 - 256| = 4$ Hz — four throbs per second, at an apparent pitch of 258 Hz.

**Q2 (conceptual).** While tuning, you hear beats at 3 Hz. You tighten the string and
beats rise to 5 Hz. Sharp or flat — and what should you do?

??? success "Answer"
    You moved the *wrong* way: the difference grew, so the string was already sharp.
    Loosen through 3, 2, 1 Hz until the beating vanishes.

**Q3 (multiple choice).** Two flutes play "the same note" but listeners hear a slow
wobble. The flutes differ in frequency by about:
(a) 100 Hz (b) 1 Hz (c) 0 Hz

??? success "Answer"
    **(b).** A slow, audible throb means a small difference — beats live in the
    few-hertz regime.
