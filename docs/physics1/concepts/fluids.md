# Fluid Statics: Pressure, Pascal & Archimedes

*Source lecture(s):* [SC133 Lec 18](../lectures.md)

## Intuition

A fluid — liquid or gas — can't hold a shape, so it pushes only one way:
perpendicular to every surface, with a squeeze called **pressure**. From that single
fact flow three famous results: pressure grows with depth (dams), pressure applied
anywhere appears everywhere (hydraulic lifts — Pascal), and immersed bodies get
buoyed up by the weight of displaced fluid (Archimedes and his bathtub).

## Pressure and depth

$$P = \frac{F}{A}\ \text{(Pa)} \qquad\qquad
\boxed{\,P = P_0 + \rho g h\,}\ \text{(incompressible fluid, depth } h)$$

Each 10 m of water adds about one atmosphere ($P_\text{atm} \approx 101\,\text{kPa}$).
Pressure at a given depth is the same in *every direction* and independent of the
container's shape — the **hydrostatic paradox**: a thin tube and a lake at equal
depth exert equal pressure.

**Gauge vs absolute:** gauges read $P - P_\text{atm}$; your "2.2 bar" tires hold
~3.2 bar absolute.

## Pascal's principle

Pressure applied to an enclosed fluid transmits **undiminished** to every point:

$$\frac{F_1}{A_1} = \frac{F_2}{A_2}$$

A small force on a small piston yields a large force on a large piston — the
hydraulic lever behind car lifts, brakes, and excavators. No free lunch: the small
piston moves proportionally farther, and [work](kinetic-energy-and-work.md) balances.

## Archimedes' principle

A body immersed (fully or partly) feels an upward **buoyant force equal to the weight
of fluid it displaces**:

$$\boxed{\,F_B = \rho_\text{fluid}\, V_\text{displaced}\; g\,}$$

*Why:* the pressure on the body's bottom exceeds that on its top by $\rho g \Delta h$;
summed over the surface, the imbalance equals the displaced fluid's weight — the
force that would have held that fluid parcel in equilibrium.

- Floats if $\rho_\text{body} < \rho_\text{fluid}$; the floating fraction submerged is
  $\rho_\text{body}/\rho_\text{fluid}$ (an iceberg: $917/1025 \approx 89\%$ under).
- A steel ship floats because its *average* density (hull + air) is below water's.

## Worked example: crown or fake?

A "gold" crown weighs 9.8 N in air and 9.0 N submerged. Verdict?

Buoyant force $= 0.8\,\text{N} = \rho_w V g \Rightarrow V = 8.2\times10^{-5}\,\text{m}^3$.
Density $= \frac{m}{V} = \frac{1.0}{8.2\times10^{-5}} \approx 12\,200\,\text{kg/m}^3$
— far from gold's 19 300. Fake (legend says Archimedes reached the same verdict, then
ran through Syracuse).

## Common mistakes

- **Buoyancy depends on the body's density?** No — on the *fluid's* density and
  displaced volume. A sunken cannonball still feels full buoyancy; it's just
  outweighed.
- **Deeper = more buoyancy?** No (incompressible fluid): displaced volume is
  unchanged, so $F_B$ is depth-independent.
- **Using total volume for floating bodies** — only the submerged part displaces.
- **Forgetting atmospheric pressure in absolute-pressure problems** (straws, suction,
  [barometers](../../fluids/concepts/hydrostatic-equilibrium.md)).

## Related concepts

- [Flowing fluids: continuity & Bernoulli](bernoulli.md) — statics set in motion
- [Equilibrium & elasticity](equilibrium.md) — why fluids are the zero-shear limit
- [The full treatment (PC316)](../../fluids/concepts/pressure.md) — pressure, [buoyancy](../../fluids/concepts/buoyancy.md), and beyond
- [Newton's laws](newtons-laws.md) — every result here is force balance

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md), [Equilibrium](equilibrium.md).
**Leads to:** [Bernoulli](bernoulli.md), the entire [PC316 fluids course](../../fluids/index.md).

## Quiz

**Q1 (computational).** A hydraulic lift: input piston 2 cm radius, output 20 cm.
Force needed to lift a 1200 kg car?

??? success "Answer"
    Area ratio $= 100$, so $F = 1200\times9.8/100 \approx 118\,\text{N}$ — one firm
    push. (You'll pump the small piston 100× the lift height.)

**Q2 (conceptual).** An ice cube floats in a full glass. When it melts, does the glass
overflow?

??? success "Answer"
    No — the level is unchanged. Floating, the cube displaces its *weight* in water;
    melted, it becomes exactly that much water. (Sea-level rise comes from *land*
    ice and thermal expansion.)

**Q3 (multiple choice).** A dam must be built thickest:
(a) at the top (b) at the bottom (c) uniformly — pressure depends on the reservoir's
total volume

??? success "Answer"
    **(b).** $P = \rho g h$ grows with depth and doesn't care about the reservoir's
    extent — a short deep lake pushes as hard as an ocean of equal depth.
