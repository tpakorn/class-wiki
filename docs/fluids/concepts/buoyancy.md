# Buoyancy

## Intuition

A submerged object is squeezed by pressure on all sides — but
[pressure grows with depth](hydrostatic-equilibrium.md), so the push on its bottom
beats the push on its top. The imbalance is a net upward force. Archimedes' genius was
to notice its exact size: replace the object by fluid and that fluid would float in
equilibrium — so the upward force on *anything* occupying that space equals the
**weight of the displaced fluid**.

## Formal statement (Archimedes' principle)

$$\boxed{\,F_\text{buoy} = \rho_\text{fluid}\, V_\text{displaced}\, g\,}$$

directed opposite to gravity. Consequently:

- $\rho_\text{object} < \rho_\text{fluid}$ → floats (rises until the *submerged* volume displaces exactly its weight)
- $\rho_\text{object} > \rho_\text{fluid}$ → sinks
- $\rho_\text{object} = \rho_\text{fluid}$ → neutrally buoyant

## Worked example: the iceberg

Ice ($\rho_\text{ice} = 917\ \text{kg m}^{-3}$) floats in seawater
($\rho_\text{water} = 1025\ \text{kg m}^{-3}$). What fraction is submerged?

Float condition — buoyancy carries the full weight:

$$\rho_\text{water} V_\text{sub}\, g = \rho_\text{ice} V_\text{ice}\, g
\implies \frac{V_\text{sub}}{V_\text{ice}} = \frac{\rho_\text{ice}}{\rho_\text{water}} = \frac{917}{1025} \approx 89\%$$

Only about a ninth of an iceberg shows. ("Tip of the iceberg" is quantitatively fair.)

## Worked example: the melting ice cube

An ice cube floats in a glass of water. As it melts, does the water level rise, fall,
or stay put?

While floating, the cube displaces a water volume weighing exactly its own weight.
When it melts, it *becomes* that same weight of water — which occupies exactly the
volume it was displacing. **The level does not change.** (Sea-level rise comes from
*land* ice and thermal expansion, not from melting sea ice.)

## Physical interpretation

Buoyancy is not a new force — it is the resultant of hydrostatic
[pressure](pressure.md) integrated over the body's surface:

$$\mathbf{F}_\text{buoy} = -\oint_S P\, d\mathbf{A} = -\int_V \nabla P\, dV = \rho_\text{fluid}\, g\, V\, \hat{k}$$

using $\nabla P = \rho_\text{fluid}\,\mathbf{g}$ inside the fluid. The divergence-theorem
step is why the result depends only on displaced *volume*, never on shape.

## Common mistakes

- **Using the object's density in the buoyancy formula.** $F_\text{buoy}$ depends on the
  *fluid's* density and the *displaced* volume only.
- **Using total volume for a floating body.** Only the submerged part displaces fluid.
- **Thinking buoyancy disappears for sunk objects.** A rock on the seabed still feels
  $\rho_\text{fluid} V g$ upward; it's just smaller than the rock's weight.

## Related concepts

- [Hydrostatic equilibrium](hydrostatic-equilibrium.md) — the pressure field behind the force
- [Pressure](pressure.md) — prerequisite
- [Hydrostatic force on surfaces](hydrostatic-force-on-surfaces.md) — same integral, plane geometry
- [Rayleigh–Taylor instability](rayleigh-taylor-instability.md) — buoyancy gone wrong: heavy fluid over light

## Knowledge graph position

**Prerequisites:** [Pressure](pressure.md), [Hydrostatic equilibrium](hydrostatic-equilibrium.md).
**Leads to:** [Rayleigh–Taylor instability](rayleigh-taylor-instability.md).

## Quiz

**Q1 (computational).** A 60 kg person floats in the Dead Sea
($\rho \approx 1240\ \text{kg m}^{-3}$). What volume of water do they displace?

??? success "Answer"
    $V = m/\rho_\text{fluid} = 60/1240 \approx 0.048\ \text{m}^3$ (48 L) — noticeably
    less than in fresh water (60 L), which is why floating there feels so easy.

**Q2 (conceptual).** A boat carrying a boulder floats in a small pond. The boulder is
thrown overboard and sinks. Does the pond level rise or fall?

??? success "Answer"
    Falls. In the boat, the boulder displaced its *weight* in water
    ($V = m/\rho_\text{water}$, large). On the bottom it displaces only its *volume*
    ($V = m/\rho_\text{rock}$, smaller since $\rho_\text{rock} > \rho_\text{water}$).

**Q3 (multiple choice).** Two solid cubes of identical volume, one steel and one wood,
are fully submerged and held in place. The buoyant force is:

- (a) larger on steel  (b) larger on wood  (c) equal  (d) zero on the wood

??? success "Answer"
    **(c).** Same fluid, same displaced volume ⇒ same buoyant force. What differs is the
    *net* force once weight is included.
