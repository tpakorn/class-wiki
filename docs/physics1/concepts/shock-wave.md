# Shock Waves & the Sonic Boom

*Source lecture(s):* [SC133 Lec 25](../lectures.md)

## Intuition

A moving sound source pushes its wavefronts ahead of it — until it moves as fast as
the sound itself. Then the fronts can't escape: they pile up into a single,
knife-edged wall of pressure. Faster still, and the wall folds back into a cone
trailing the source. Crossing that cone is the **sonic boom** — all the sound of the
passage, delivered at once.

## The Mach cone

For source speed $v_s$ greater than sound speed $v$, the piled-up wavefronts form a
cone of half-angle $\theta$:

$$\boxed{\,\sin\theta = \frac{v}{v_s} = \frac{1}{M}\,}
\qquad M \equiv \frac{v_s}{v}\ \text{(Mach number)}$$

- $M < 1$ (subsonic): fronts bunched ahead ([Doppler](sound-waves.md)), no shock.
- $M = 1$: fronts coincide — the "sound barrier," a wall of pressure at the nose.
- $M > 1$: the cone; larger $M$, narrower cone.

The boom isn't a one-time bang at Mach 1 — the cone drags along the whole supersonic
flight, sweeping a "boom carpet" tens of kilometres wide.

## Everyday supersonics

- **Bullwhip crack:** the tapering whip accelerates its tip past ~340 m/s — the crack
  is a miniature sonic boom (humanity's first supersonic machine).
- **Thunder:** lightning heats a channel so fast the expansion is a shock that decays
  into the rumble.
- **Boat wakes:** the V-wake is the same geometry with water-surface waves.
- **Cherenkov radiation:** a particle exceeding light's speed *in a medium* makes the
  optical analogue — the blue glow of reactor pools.

## Inside the shock

Across the thin front, pressure, density, and temperature **jump** almost
discontinuously — ordinary sound is a gentle (~Pa) wiggle, a shock is a finite
(~kPa–MPa) step that heats the gas irreversibly. The jump obeys conservation laws
(mass, momentum, energy) written across the front — the
[Rankine–Hugoniot conditions](../../fluids/equations/rankine-hugoniot-conditions.md),
treated fully in [PC316's shock chapter](../../fluids/concepts/shock-waves.md), and
the reason re-entry capsules need heat shields (the shock, not friction, does the
heating).

## Worked example: how high is the jet?

You see a fighter pass directly overhead; the boom arrives 6 s later. The jet flies
at Mach 1.5 ($v = 340$ m/s). Altitude?

Cone half-angle: $\sin\theta = 1/M = 1/1.5 \Rightarrow \theta \approx 41.8°$.

You hear the boom at the instant the cone surface sweeps over you. By then the jet
has moved past overhead by $d = v_s t = 1.5(340)(6) = 3060\,\text{m}$, and the cone
geometry relates your position to the jet:
$\tan\theta = h/d$, so

$$h = d\tan\theta = 3060\times\tan 41.8° \approx 2.7\,\text{km}$$

## Common mistakes

- **"The boom happens only when breaking the barrier."** The cone persists throughout
  supersonic flight; everyone under the carpet hears it, sequentially.
- **Thinking the pilot hears the boom.** The cone trails *behind*; the aircraft
  outruns its own noise.
- **Confusing shock heating with friction.** Compression across the shock does the
  heating — that's why blunt re-entry shapes (stronger, *detached* shock) protect
  better than needles.
- **Using small-signal sound formulas across a shock** — shocks are nonlinear;
  ordinary acoustics breaks down ([the full story](../../fluids/concepts/shock-waves.md)).

## Related concepts

- [Sound waves & Doppler](sound-waves.md) — the subsonic prelude
- [Shock waves in fluids (PC316)](../../fluids/concepts/shock-waves.md) — jump conditions, blast waves
- [Waves](waves.md) — what's piling up

## Knowledge graph position

**Prerequisites:** [Sound waves](sound-waves.md).
**Leads to:** [compressible flow (PC316)](../../fluids/concepts/shock-waves.md), aerodynamics, astrophysical shocks.

## Quiz

**Q1 (computational).** A jet at Mach 2: what is the Mach-cone half-angle?

??? success "Answer"
    $\sin\theta = 1/2 \Rightarrow \theta = 30°$ — double the speed of sound, a
    30° cone.

**Q2 (conceptual).** Why does a bullwhip crack while no part of your arm approaches
the speed of sound?

??? success "Answer"
    Momentum funnels into ever-less mass: as the wave runs down the tapering whip,
    conservation drives the thin tip to enormous speed — past Mach 1 — with only a
    modest hand motion at the heavy end.

**Q3 (multiple choice).** As a supersonic jet flies faster, its Mach cone becomes:
(a) wider (b) narrower (c) unchanged

??? success "Answer"
    **(b).** $\sin\theta = 1/M$ — at very high Mach the boom concentrates into a
    slender, intense cone.
