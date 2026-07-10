# The Distribution of Molecular Speeds

*Source lecture(s):* [SC133 Lec 29](../lectures.md)

## Intuition

At 300 K, air molecules average ~500 m/s — but that's an *average* over anarchy. Any
instant, some molecules crawl and a lucky few streak at several kilometres per
second, their speeds constantly reshuffled by ~10⁹ collisions per second each.
Maxwell's great insight (1860): despite the chaos, the *distribution* of speeds is
fixed, universal, and calculable — statistical order emerging from molecular mayhem.
It was physics' first probability distribution, and the door to statistical
mechanics.

## The Maxwell–Boltzmann distribution

The fraction of molecules with speed near $v$:

$$f(v) = 4\pi N\left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2\, e^{-mv^2/2k_BT}$$

Two competing factors sculpt the famous skewed bell:

- $v^2$ — more directions available at higher speed (phase-space volume) — kills the
  distribution at $v = 0$
- $e^{-mv^2/2k_BT}$ — the Boltzmann energy penalty — kills it at high $v$

Heat the gas and the peak shifts right and flattens; the area (total count) stays
fixed. The exponential *tail* never quite dies — and much of nature lives in that
tail.

## Three landmark speeds

$$v_p = \sqrt{\frac{2k_BT}{m}} \;<\;
\bar v = \sqrt{\frac{8k_BT}{\pi m}} \;<\;
v_\text{rms} = \sqrt{\frac{3k_BT}{m}}$$

(most probable : mean : root-mean-square = $\sqrt2 : \sqrt{8/\pi} : \sqrt3$ ≈
1 : 1.13 : 1.22). The rms speed is the one tied to
[temperature and pressure](ideal-gas.md) ($\overline{K} = \tfrac32 k_BT$); the
distribution's skew is why they differ.

## The tail runs the world

- **Evaporative cooling:** only the fastest molecules escape a liquid's surface;
  the remainder is cooler — sweating, and the trick behind Bose–Einstein-condensate
  experiments.
- **Atmospheric escape:** a tiny hydrogen/helium tail exceeds Earth's
  [escape velocity](gravitation.md) (11.2 km/s); over eons those gases leaked away —
  while the Moon (2.4 km/s) lost *everything*. N₂ and O₂, 14–16× heavier, have
  effectively no escaping tail: that's why Earth kept *this* atmosphere.
- **Chemical reactions & fusion:** reactions need collisions above an activation
  energy — rates track the tail population, hence the exponential temperature
  sensitivity (Arrhenius), and why
  [fusion plasmas](../../plasma/index.md) fixate on temperature.

## Worked example: hydrogen vs nitrogen at 300 K

$$v_\text{rms}^{H_2} = \sqrt{\frac{3k_BT}{m_{H_2}}} \approx 1930\,\text{m/s}
\qquad
v_\text{rms}^{N_2} \approx 517\,\text{m/s}$$

Same temperature, same average *energy* — but H₂ is 14× lighter, hence
$\sqrt{14} \approx 3.7×$ faster, with a far fatter high-speed tail relative to escape
velocity. Geology by statistics.

## Common mistakes

- **"All molecules move at $v_\text{rms}$."** The spread is comparable to the mean —
  the distribution *is* the physics.
- **Peak = mean.** The skew puts $\bar v$ and $v_\text{rms}$ to the right of the
  peak $v_p$.
- **Doubling $T$ doubles speeds.** Speeds scale as $\sqrt T$ — doubling 300 K → 600 K
  raises speeds by 41%.
- **Using Celsius anywhere near these formulas.** Kelvin only.

## Related concepts

- [Ideal gas](ideal-gas.md) — where $v_\text{rms}$ comes from
- [Temperature](temperature.md) — the parameter that shapes the curve
- [Escape velocity](gravitation.md) — the bar the tail must clear
- [Velocity distributions in plasmas (PC368)](../../plasma/concepts/vlasov-equation.md) — $f(v)$ promoted to the main character; its slope even [damps waves](../../plasma/concepts/landau-damping.md)

## Knowledge graph position

**Prerequisites:** [Ideal gas](ideal-gas.md).
**Leads to:** [Second law](second-law-of-thermodynamics.md) (statistics → entropy), kinetic theory, [Vlasov theory](../../plasma/concepts/vlasov-equation.md).

## Quiz

**Q1 (computational).** At what temperature does H₂'s rms speed equal N₂'s at 300 K?

??? success "Answer"
    $v_\text{rms} \propto \sqrt{T/m}$: need $T_{H_2}/m_{H_2} = 300/m_{N_2}$, so
    $T = 300\times(2/28) \approx 21\,\text{K}$ — hydrogen at liquid-helium-ish
    temperatures still moves like room-temperature nitrogen.

**Q2 (conceptual).** Why does a puddle evaporate at 25 °C when water "boils at 100 °C"?

??? success "Answer"
    The Maxwell tail: even at 25 °C some surface molecules carry enough KE to break
    free. Boiling is bulk vapor formation; evaporation is the tail deserting one
    molecule at a time — cooling what remains.

**Q3 (multiple choice).** For a gas at temperature $T$, the ordering is:
(a) $v_p < \bar v < v_\text{rms}$ (b) $v_\text{rms} < \bar v < v_p$ (c) all equal

??? success "Answer"
    **(a)** — the high-speed skew drags the averages (especially the squared one)
    above the peak.
