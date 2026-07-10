# The Second Law & Entropy

*Source lecture(s):* [SC133 Lec 30](../lectures.md)

## Intuition

Drop dye in water: it spreads. It never un-spreads. Coffee cools; it never re-heats
by chilling the room. The [first law](first-law-of-thermodynamics.md) would happily
allow the reverse — energy balances either way. Something else forbids it: the
**second law**, the only fundamental law of physics with a built-in *arrow of time*.
Its currency is **entropy** — and the reason is ultimately just counting: disordered
arrangements outnumber ordered ones so astronomically that "toward disorder" is
simply "toward the overwhelmingly probable."

## Classical statements (all equivalent)

- **Clausius:** heat never flows spontaneously from cold to hot.
- **Kelvin–Planck:** no cyclic engine can convert heat into work with *no other
  effect* (no perfect engine).
- **Entropy:** for an isolated system,

$$\boxed{\,\Delta S \geq 0\,}$$

with equality only for idealized reversible processes.

## Entropy, macroscopically

$$\Delta S = \int \frac{dQ_\text{rev}}{T} \qquad [\text{J/K}]$$

A state function, like $E_\text{int}$. Canonical example — heat $Q$ leaks from hot
$T_h$ to cold $T_c$:

$$\Delta S = \frac{Q}{T_c} - \frac{Q}{T_h} > 0$$

The cold body gains more entropy than the hot one loses (dividing by a smaller $T$)
— which is *why* heat flows that way and not backward.

## Entropy, microscopically

Boltzmann's tombstone equation:

$$S = k_B \ln W$$

$W$ = number of microscopic arrangements consistent with the macroscopic state.
Gas spreading into a vacuum: each molecule doubles its options, so
$W \to 2^N W$ and $\Delta S = Nk_B\ln 2$. With $N \sim 10^{23}$, the probability of
spontaneous un-spreading is $2^{-10^{23}}$ — not forbidden, just *never*. The second
law is statistics with teeth.

## Heat engines and the Carnot ceiling

Any cyclic engine takes $Q_h$ from a hot reservoir, dumps $Q_c$ to a cold one, and
delivers $W = Q_h - Q_c$. The second law caps its efficiency at the **Carnot limit**:

$$e = \frac{W}{Q_h} \leq e_\text{Carnot} = 1 - \frac{T_c}{T_h}$$

Power plants at $T_h \approx 800$ K, $T_c \approx 300$ K: ceiling ~62%, real ~40%.
The waste heat isn't engineering sloppiness — it is the entropy *tax*: dumping $Q_c$
into the cold reservoir is what pays for the entropy removed from the hot one.
Refrigerators run the cycle backward, using work to pump heat cold→hot — allowed,
because *something else* (the power station) raises entropy on your behalf.

## Worked example: the melting ice cube

50 g of ice melts at 0 °C in a 25 °C room. Entropy change of the universe?

Ice: $\Delta S_\text{ice} = \frac{mL_f}{T} = \frac{0.05\times334000}{273} \approx +61.2\,\text{J/K}$.
Room: $\Delta S_\text{room} = \frac{-16\,700}{298} \approx -56.0\,\text{J/K}$.
Total: $+5.2\,\text{J/K} > 0$ ✓ — spontaneous, irreversible, and quantifiably so.

## Common mistakes

- **"Entropy always increases."** Only for *isolated* systems. Your freezer lowers
  entropy locally — the power plant more than compensates. Life itself is a local
  entropy-lowering enterprise funded by the Sun.
- **Entropy = messiness.** It counts *microstates*, with precise units — a shuffled
  desk is a metaphor, not a calculation.
- **Blaming friction for all inefficiency.** Even a perfect, frictionless engine hits
  the Carnot wall; the limit is thermodynamic, not mechanical.
- **Using °C in Carnot's formula** — ratios of temperatures require kelvin.

## Related concepts

- [First law](first-law-of-thermodynamics.md) — what's *possible*; second law: what *happens*
- [Molecular speeds](molecular-speed.md) — the statistical world underneath
- [Temperature & heat](temperature.md) — the flow the law directs
- [Entropy jump across shocks (PC316)](../../fluids/concepts/shock-waves.md) — the second law selecting physical solutions

## Knowledge graph position

**Prerequisites:** [First law](first-law-of-thermodynamics.md), [Ideal gas](ideal-gas.md), [Molecular speeds](molecular-speed.md).
**Leads to:** statistical mechanics, and the deep ends of every field — from [shock physics](../../fluids/concepts/shock-waves.md) to cosmology.

## Quiz

**Q1 (computational).** A Carnot engine runs between 500 K and 300 K, drawing 1000 J
per cycle. Maximum work?

??? success "Answer"
    $e = 1 - 300/500 = 0.4 \Rightarrow W_\text{max} = 400\,\text{J}$, with 600 J
    *necessarily* dumped to the cold reservoir.

**Q2 (conceptual).** Does a growing crystal (highly ordered!) violate the second law?

??? success "Answer"
    No — freezing releases latent heat into the surroundings, whose entropy gain
    ($Q/T_\text{surr}$) exceeds the crystal's loss. Order can grow locally whenever
    it exports more than enough disorder.

**Q3 (multiple choice).** Which single change raises a Carnot engine's efficiency
most, per kelvin? (a) raising $T_h$ (b) lowering $T_c$ (c) identical effect

??? success "Answer"
    **(b).** $\partial e/\partial T_c = -1/T_h$ vs $\partial e/\partial T_h = T_c/T_h^2$;
    since $T_c < T_h$, one kelvin off the cold side beats one kelvin onto the hot
    side — though engineering usually finds $T_h$ easier to raise.

**Q4 (conceptual).** Why is the second law the only law with a time direction?

??? success "Answer"
    Microscopic laws (Newton, Maxwell) are time-reversible; entropy's arrow is
    statistical: forward = toward the vastly more numerous microstates. Play the
    film backward and no collision breaks a law — but the sequence becomes
    astronomically improbable.
