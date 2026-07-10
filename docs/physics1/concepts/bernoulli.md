# Fluids in Motion: Continuity & Bernoulli

*Source lecture(s):* [SC133 Lec 19](../lectures.md)

## Intuition

Put your thumb over a garden hose: the water speeds up. Why? The same volume must
squeeze through a smaller opening each second — **continuity**. And where a fluid
speeds up, its pressure *drops* — **Bernoulli**, which is just
[energy conservation](conservation-of-energy.md) written per unit volume of flowing
fluid. Two principles, one breath: they explain airplane wings, chimney draft,
perfume atomizers, and why shower curtains attack you.

## Continuity: mass conservation

For steady incompressible flow through a tube of varying cross-section:

$$\boxed{\,A_1 v_1 = A_2 v_2\,}$$

Volume flow rate $Q = Av$ ($\text{m}^3/\text{s}$) is the same everywhere along the
tube — narrow means fast. This is why rivers race through gorges and dawdle across
plains.

## Bernoulli's equation

Along a streamline of steady, incompressible, **frictionless** flow:

$$\boxed{\,P + \tfrac12\rho v^2 + \rho g y = \text{constant}\,}$$

Three terms, three energies per unit volume: pressure (work done by squeezing),
kinetic, gravitational. Full derivation and applications:
[equation page](../equations/bernoullis-equation.md) and the graduate treatment in
[PC316](../../fluids/concepts/bernoulli-principle.md).

**The core trade-off:** at constant height, fast ⇒ low pressure. Blow across a strip
of paper and it *rises* into the fast, low-pressure stream.

## Worked example: Torricelli's tank

Water drains through a small hole a depth $h$ below the surface of an open tank.
Exit speed?

Apply Bernoulli from surface (large area ⇒ $v \approx 0$, $P = P_\text{atm}$) to hole
($P = P_\text{atm}$):

$$\rho g h = \tfrac12 \rho v^2 \Rightarrow \boxed{v = \sqrt{2gh}}$$

— identical to free fall from height $h$: the water "falls" through the pressure
field. (Where should the hole be to spray farthest? Halfway down —
[worked out in PC316](../../fluids/concepts/bernoulli-principle.md).)

## Worked example: Venturi meter

Pipe narrows from $A_1$ to $A_2$; a manometer reads the pressure drop $\Delta P$.
Continuity + Bernoulli give

$$v_1 = A_2\sqrt{\frac{2\Delta P}{\rho\,(A_1^2 - A_2^2)}}$$

— flow measured with no moving parts. The same throat-suction runs carburetors and
perfume atomizers.

## Where Bernoulli earns its reputation

- **Wings:** air over the curved top travels faster ⇒ lower pressure above ⇒ lift.
  (The full story needs circulation — [PC316 potential flow](../../fluids/concepts/potential-flow.md) —
  but the pressure-speed link is genuine.)
- **Chimneys & burrows:** wind across the top lowers pressure and draws air up —
  prairie dogs engineer their mounds for exactly this.
- **Roofs in storms:** fast wind above, still air inside ⇒ net *upward* push; roofs
  peel, not crush.

## Common mistakes

- **Applying Bernoulli across a pump, fan, or heater** — it's frictionless
  *streamline* energy bookkeeping; devices that add energy break the constant.
- **Using it in strongly viscous or turbulent regions** (long thin pipes obey
  [Poiseuille](../../fluids/examples/hagen-poiseuille-flow.md) instead).
- **Forgetting continuity first.** Almost every Bernoulli problem is a two-equation
  system: continuity fixes the speeds, Bernoulli converts to pressures.
- **"Fast air sucks."** Low pressure doesn't pull; the *surrounding higher pressure
  pushes*. Same physics, honest language.

## Related concepts

- [Fluid statics](fluids.md) — the $v = 0$ limit
- [Conservation of energy](conservation-of-energy.md) — the principle in disguise
- [Bernoulli's equation (reference)](../equations/bernoullis-equation.md)
- [PC316: the real derivation](../../fluids/concepts/bernoulli-principle.md), [continuity](../../fluids/equations/continuity-equation.md), and [when Bernoulli fails](../../fluids/concepts/shock-waves.md)

## Knowledge graph position

**Prerequisites:** [Fluid statics](fluids.md), [Conservation of energy](conservation-of-energy.md).
**Leads to:** the whole of [PC316 Fluid Mechanics](../../fluids/index.md).

## Quiz

**Q1 (computational).** Water flows at 2 m/s in a 4 cm-diameter pipe that narrows to
2 cm. Speed in the narrow section?

??? success "Answer"
    $v_2 = v_1 (d_1/d_2)^2 = 2\times4 = 8\,\text{m/s}$ — area goes as diameter
    *squared*.

**Q2 (conceptual).** Two boats moving parallel and close are pushed together. Why?

??? success "Answer"
    Water funneled between the hulls speeds up (continuity), dropping the pressure
    between them below the outside pressure — the outer water pushes the hulls
    together. The same effect once sank ships during refueling alongside.

**Q3 (multiple choice).** In the narrow throat of a horizontal Venturi tube, the
pressure is: (a) highest (b) lowest (c) unchanged

??? success "Answer"
    **(b).** Fastest flow ⇒ lowest pressure (at fixed height) — the defining
    Bernoulli trade.
