# The Ideal Gas

*Source lecture(s):* [SC133 Lec 28](../lectures.md)

## Intuition

Model a gas as a swarm of tiny billiard balls: pointlike, non-interacting except for
elastic bounces. Absurdly simple — yet it predicts real gas behavior superbly at
ordinary conditions, and it does something profound: it connects the world of
thermometers and pressure gauges to the invisible world of molecular collisions.
**Pressure is drumfire** — trillions of wall impacts per second — and **temperature
is the average violence of the drumming.**

## The equation of state

$$\boxed{\,PV = nRT = Nk_BT\,}$$

$n$ moles ($R = 8.314\,\text{J/(mol·K)}$) or $N$ molecules
($k_B = 1.38\times10^{-23}\,\text{J/K}$); $T$ in **kelvin**, always.
Reference: [equation page](../equations/ideal-gas-law.md). One mole at 0 °C, 1 atm:
22.4 L — the same for *any* ideal gas, which is the miracle: the law doesn't care
what the molecules are.

The old empirical laws are corollaries: Boyle ($PV$ const at fixed $T$), Charles
($V \propto T$ at fixed $P$), Gay-Lussac ($P \propto T$ at fixed $V$).

## Kinetic theory: pressure from collisions

One molecule of mass $m$, speed component $v_x$, bouncing between walls of a box of
side $L$: each wall hit transfers momentum $2mv_x$
([impulse](collision-and-impulse.md)) every $2L/v_x$ seconds. Summing over $N$
molecules and averaging:

$$PV = \tfrac13 N m \overline{v^2}$$

Comparing with $PV = Nk_BT$ yields the golden dictionary entry:

$$\boxed{\,\overline{K}_\text{trans} = \tfrac12 m\overline{v^2} = \tfrac32 k_B T\,}$$

**Temperature *is* average translational kinetic energy.** Absolute zero = zero
jiggle (classically). Every gas at the same $T$ has the same average molecular KE —
lighter molecules simply move faster ([molecular speeds](molecular-speed.md)).

## Internal energy and heat capacities

Equipartition: each quadratic degree of freedom carries $\tfrac12 k_BT$ per molecule.

| Gas | $f$ | $E_\text{int}$ | $C_V$ | $\gamma = C_P/C_V$ |
|---|---|---|---|---|
| Monatomic (He, Ar) | 3 | $\tfrac32 nRT$ | $\tfrac32 R$ | 5/3 |
| Diatomic (N₂, O₂), ~300 K | 5 | $\tfrac52 nRT$ | $\tfrac52 R$ | 7/5 |

with $C_P = C_V + R$ (constant pressure also pays for expansion work — the
[first law](first-law-of-thermodynamics.md) in action). The ratio $\gamma$ governs
[adiabatic processes](first-law-of-thermodynamics.md) and the
[speed of sound](sound-waves.md).

## Worked example: air in a dive tank

A 12 L tank holds air at 200 bar, 20 °C. How many moles — and what volume at the
surface (1 bar)?

$n = PV/RT = \frac{2\times10^7\times0.012}{8.314\times293} \approx 98.5\,\text{mol}$
(≈2.9 kg of air). At 1 bar, same $T$: $V = nRT/P \approx 2.4\,\text{m}^3$ — the tank
"contains" 2400 surface-litres, which is how dive durations are computed.

## When ideality fails

Near condensation (molecules attract) and at high density (molecules have size), use
van der Waals corrections. And in a [plasma](../../plasma/concepts/ideal-plasma.md),
"ideal" gets redefined — long-range Coulomb forces change the game entirely.

## Common mistakes

- **Celsius in the gas law.** $PV = nRT$ demands kelvin; 20 °C is 293 K, not 20.
- **"Heavier gases are hotter/faster."** Same $T$ ⇒ same average KE; heavier means
  *slower*, not more energetic.
- **Confusing $C_V$ and $C_P$** — constant-pressure heating costs more because the
  gas also does work.
- **Applying ideal-gas results to liquids** — no free flight between collisions, no
  ideal-gas law.

## Related concepts

- [Temperature & heat](temperature.md) — now with a microscopic meaning
- [Molecular speeds](molecular-speed.md) — the full distribution behind $\overline{v^2}$
- [First law](first-law-of-thermodynamics.md) — processes on the $P$–$V$ diagram
- [Ideal gas law (reference)](../equations/ideal-gas-law.md)

## Knowledge graph position

**Prerequisites:** [Collisions & impulse](collision-and-impulse.md), [Temperature](temperature.md).
**Leads to:** [Molecular speeds](molecular-speed.md), [Second law](second-law-of-thermodynamics.md), [plasma physics](../../plasma/concepts/ideal-plasma.md).

## Quiz

**Q1 (computational).** What is the average translational KE of any gas molecule at
300 K, and the rms speed of N₂ ($m = 4.65\times10^{-26}$ kg)?

??? success "Answer"
    $\overline K = \tfrac32 k_BT = 6.2\times10^{-21}\,\text{J}$;
    $v_\text{rms} = \sqrt{3k_BT/m} = \sqrt{3(1.38\times10^{-23})(300)/4.65\times10^{-26}} \approx 517\,\text{m/s}$
    — faster than sound, as it must be (sound is carried *by* these molecules).

**Q2 (conceptual).** A sealed rigid flask is heated from 300 K to 600 K. What happens
to pressure, and to the average molecular speed?

??? success "Answer"
    $P$ doubles ($P \propto T$ at fixed $V, N$); $v_\text{rms} \propto \sqrt T$ grows
    by $\sqrt2 \approx 1.41$ — pressure rises both because impacts are harder *and*
    more frequent.

**Q3 (multiple choice).** Two flasks, same $T$, $V$, $P$: one holds helium, one holds
nitrogen. Which contains more molecules? (a) He (b) N₂ (c) equal

??? success "Answer"
    **(c).** Avogadro's insight, embedded in $PV = Nk_BT$: the count is fixed by
    $P, V, T$ regardless of species.
