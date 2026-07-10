# Temperature, Heat & Thermal Expansion

*Source lecture(s):* [SC133 Lec 26](../lectures.md)

## Intuition

Touch a metal bench and a wooden one on a cold morning: the metal *feels* colder,
yet both sit at the same temperature. Your hand measures heat *flow*, not
temperature. Untangling the two is the start of thermodynamics: **temperature** is a
state — microscopically, the average kinetic energy of molecular jiggling — while
**heat** is energy *in transit* from hot to cold. Nothing "contains heat"; things
contain internal energy and exchange heat.

## Temperature and its scales

Two bodies in contact stop exchanging net energy when they reach the same
temperature — thermal equilibrium. (The *zeroth law*: if A ≡ C and B ≡ C, then
A ≡ B — which is what makes thermometers meaningful.)

$$T_K = T_C + 273.15 \qquad T_F = \tfrac95 T_C + 32$$

Physics happens in **kelvin**: only there is temperature proportional to molecular
kinetic energy, with a true zero (no jiggling left to remove). Room temperature
≈ 293 K.

## Heat, heat capacity, and phase changes

Heat $Q$ (joules) raises temperature according to the **specific heat** $c$:

$$Q = mc\,\Delta T$$

Water's $c = 4186\,\text{J/(kg·K)}$ is enormous — why coastal climates are mild,
why water cools engines, and why a pie's filling burns when its crust doesn't.

During a **phase change**, heat flows with *no* temperature change — it pays for
molecular rearrangement instead (latent heat $Q = mL$): for water,
$L_f = 334\,\text{kJ/kg}$ (melting), $L_v = 2256\,\text{kJ/kg}$ (boiling — huge,
which is why steam burns worse than boiling water and why sweating works).

**Heat travels three ways:** conduction (molecular hand-offs — metals excel: that
cold bench), convection (bulk fluid motion — see
[fluid instabilities](../../fluids/concepts/rayleigh-taylor-instability.md)), and
radiation (light — the only way through vacuum, $P \propto T^4$).

## Thermal expansion

Almost everything grows when heated — the anharmonic jiggle pushes neighbors apart:

$$\Delta L = \alpha L\,\Delta T \qquad\qquad \Delta V = \beta V\,\Delta T,\ \ \beta \approx 3\alpha$$

Steel: $\alpha \approx 12\times10^{-6}\,\text{K}^{-1}$ — a 1 km bridge breathes
~0.4 m across seasons, hence expansion joints. Famous exception: water below 4 °C
*expands* on cooling, so lakes freeze from the top and fish survive winter.

## Worked example: icing a drink

How much 0 °C ice melts to cool 300 g of water from 25 °C to 0 °C?

Heat available: $Q = mc\Delta T = 0.3\times4186\times25 \approx 31.4\,\text{kJ}$.
Ice melted: $m = Q/L_f = 31\,400/334\,000 \approx 94\,\text{g}$ — about four cubes,
and the *melting* (not the ice's coldness) does almost all the work.

## Common mistakes

- **"This object has a lot of heat."** Objects have internal energy; heat is the
  transfer. (Like "rain" vs "water in the lake".)
- **Feeling = temperature.** Touch senses heat flux — conductivity × temperature
  difference — hence cold metal, "hot" metal in the same sun-baked car.
- **Forgetting latent heat plateaus** when tracking $Q$ through a phase change: the
  temperature graph flatlines while $Q$ keeps flowing.
- **Expansion holes shrink?** No — a heated plate expands *photographically*: holes
  grow too (why heating a stuck jar lid works).

## Related concepts

- [Ideal gas](ideal-gas.md) — temperature as molecular kinetic energy, made exact
- [First law of thermodynamics](first-law-of-thermodynamics.md) — heat enters the energy books
- [Molecular speeds](molecular-speed.md) — the microscopic picture
- [Conservation of energy](conservation-of-energy.md) — the macroscopic prelude

## Knowledge graph position

**Prerequisites:** [Conservation of energy](conservation-of-energy.md).
**Leads to:** [First law](first-law-of-thermodynamics.md), [Ideal gas](ideal-gas.md), [Second law](second-law-of-thermodynamics.md).

## Quiz

**Q1 (computational).** A 2 kW kettle heats 1 L of water from 20 °C to 100 °C. Minimum
time?

??? success "Answer"
    $Q = mc\Delta T = 1\times4186\times80 \approx 335\,\text{kJ}$;
    $t = Q/P = 335\,000/2000 \approx 167\,\text{s}$ — nearly 3 minutes, all thanks
    to water's mighty $c$.

**Q2 (conceptual).** Why do bridges have toothed expansion joints while railway tracks
once buckled in heat waves?

??? success "Answer"
    Constrained expansion becomes stress:
    $\sigma = E\alpha\Delta T$ ([elasticity](equilibrium.md)) — tens of MPa for steel
    across a hot day. Joints give the length somewhere to go; continuously welded
    rail instead relies on strong anchoring and pre-tensioning.

**Q3 (multiple choice).** Equal masses of water (c = 4186) and iron (c = 450) receive
equal heat. Which ends hotter? (a) water (b) iron (c) equal

??? success "Answer"
    **(b).** $\Delta T = Q/mc$ — iron's small specific heat means a ~9× larger
    temperature rise.
