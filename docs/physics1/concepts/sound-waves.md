# Sound Waves

*Source lecture(s):* [SC133 Lec 24](../lectures.md)

## Intuition

Sound is a **longitudinal** pressure wave: air molecules shuffle back and forth along
the travel direction, piling into compressions and thinning into rarefactions that
race outward at ~343 m/s. Your eardrum doesn't receive matter from the source — it
receives the *pattern*, a few pascals of pressure wiggle riding on the full
atmosphere.

## Speed of sound

The universal medium formula, $v = \sqrt{\text{stiffness}/\text{inertia}}$:

$$v = \sqrt{\frac{B}{\rho}}
\qquad\text{(air, ideal-gas form): } v = \sqrt{\frac{\gamma R T}{M}} \approx 343\,\text{m/s at }20°\text{C}$$

- Rises with temperature (~0.6 m/s per °C) — instruments sharpen as halls warm.
- Faster in water (~1480 m/s) and steel (~5900 m/s): stiffness wins over density.
- Depends on the *gas*, not the pressure: helium's tiny $M$ nearly triples $v$,
  raising your vocal-tract resonances — the duck voice.

## Intensity and the decibel

Sound intensity (power per area) from a point source spreads over spheres:

$$I = \frac{P}{4\pi r^2} \qquad\text{— the inverse-square law}$$

Ears operate across 12 orders of magnitude, so we use a log scale:

$$\beta = 10\log_{10}\frac{I}{I_0}\ \text{dB}, \qquad I_0 = 10^{-12}\,\text{W/m}^2$$

+10 dB = ×10 intensity (≈ "twice as loud" perceptually); +3 dB = ×2 intensity.
Whisper 30 dB, conversation 60 dB, rock concert 110 dB, pain ~130 dB.

## The Doppler effect

Relative motion between source and listener shifts the received frequency:

$$f' = f\,\frac{v \pm v_\text{listener}}{v \mp v_\text{source}}
\qquad\text{(upper signs: approaching)}$$

Approach ⇒ higher pitch (wavefronts bunched); recede ⇒ lower. The ambulance-siren
drop, radar speed guns, ultrasound blood-flow imaging, and — with light — the
redshift that revealed the expanding universe. A source *at* the sound speed piles
its wavefronts into a [shock cone](shock-wave.md).

## Worked example: concert loudness

You measure 80 dB at 10 m from a speaker. What at 40 m?

Inverse square: $I$ drops ×16 ⇒ $\Delta\beta = 10\log 16 \approx 12$ dB:
**68 dB**. (Real rooms add reverberation; outdoors this rule is good.)

## Worked example: passing train

A train horn at 400 Hz passes you at 30 m/s. Pitch heard on approach and recession?

$$f_\text{approach} = 400\,\frac{343}{343 - 30} \approx 438\,\text{Hz}
\qquad
f_\text{recede} = 400\,\frac{343}{343 + 30} \approx 368\,\text{Hz}$$

— a drop of nearly two semitones as it passes: the classic *neee-ooow*.

## Common mistakes

- **Doppler depends only on relative speed?** For sound, no — the medium matters;
  moving source and moving listener give (slightly) different formulas. (For light,
  only relative motion counts.)
- **Confusing loudness (dB, logarithmic, perceptual) with intensity (W/m², physical)**
  — "twice the watts" is +3 dB, barely noticeable.
- **Thinking molecules travel to your ear.** Displacement amplitudes are micrometres;
  it's the pattern that propagates.
- **Applying the approach formula while the source passes abeam** — at closest
  approach the shift is momentarily zero; only the radial velocity component counts.

## Related concepts

- [Traveling waves](waves.md) — the framework
- [Superposition](superposition.md) — pipes, rooms, and choirs
- [Beats](beats.md) — two close pitches interfering in time
- [Shock waves](shock-wave.md) — Doppler at Mach 1 and beyond
- [Ion-acoustic waves (PC368)](../../plasma/concepts/ion-acoustic-wave.md) — sound's plasma cousin

## Knowledge graph position

**Prerequisites:** [Traveling waves](waves.md).
**Leads to:** [Beats](beats.md), [Shock waves](shock-wave.md), acoustics and audiology.

## Quiz

**Q1 (computational).** Thunder arrives 4 s after the lightning flash. How far away
was the strike?

??? success "Answer"
    $d = vt \approx 343\times4 \approx 1.4\,\text{km}$ — the "3 seconds per
    kilometre" rule.

**Q2 (conceptual).** Why does inhaling helium raise the pitch of your voice but *not*
the frequency of a tuning fork struck in the same room?

??? success "Answer"
    Your vocal tract is a resonant cavity: its formant frequencies scale with the gas
    sound speed ($f \sim v/L$). The tuning fork's frequency is set by its own metal
    elasticity, not the surrounding gas — the gas only carries the sound.

**Q3 (multiple choice).** Moving toward a stationary siren at high speed, you hear:
(a) higher pitch and it drops as you pass (b) the true pitch (c) lower pitch rising

??? success "Answer"
    **(a).** Approach raises $f'$; after passing, recession lowers it below the true
    value — the shift flips sign at closest approach.
