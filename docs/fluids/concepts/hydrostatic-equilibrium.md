# Hydrostatic Equilibrium

## Intuition

A fluid at rest is a tug-of-war that ends in a draw: gravity pulls every parcel down,
and the pressure difference between a parcel's bottom and top pushes it up. Equilibrium
means these balance exactly — which forces pressure to increase with depth at precisely
the rate needed to carry the weight of everything above.

## Mathematical formulation

Consider a thin slab of fluid of area $A$ and thickness $\Delta y$ at depth $d$.
Balancing pressure forces against weight $W = \rho g A\,\Delta y$ gives, in the limit:

$$\frac{dP}{dy} = \rho g \quad (y \text{ measured downward})$$

For an **incompressible liquid** ($\rho$ constant), integrate from the surface
($P(0)=P_0$):

$$\boxed{\,P(y) = P_0 + \rho g y\,}$$

## The compressible atmosphere: three barometric formulas

For a gas, $\rho$ depends on $P$ through the ideal-gas law $P = \rho R T$, so the
balance $dP/dh = -\rho g$ (now $h$ measured upward) becomes
$\frac{dP}{P} = -\frac{g}{RT}\,dh$, and the answer depends on the temperature profile:

**Isothermal** ($T$ constant):

$$P(h) = P_0 \exp\!\left(-\frac{gh}{RT}\right)$$

**Linear lapse rate** ($T = T_0 - \lambda h$):

$$P(h) = P_0\left(1 - \frac{\lambda h}{T_0}\right)^{g/R\lambda}, \qquad \text{valid while } T_0 > \lambda h$$

**Adiabatic** ($P/\rho^\gamma$ constant):

$$P(h) = P_0\left(1 - \frac{gh}{RT_0}\,\frac{\gamma - 1}{\gamma}\right)^{\gamma/(\gamma-1)}$$

All three agree to first order in $h$ — near the ground, pressure falls off linearly
either way.

## Worked example: Superman with a straw

*How high can anyone — even Superman — drink water through a straw?*

Sucking creates low pressure at the top; the atmosphere pushes the water up. The best
possible "suck" is a perfect vacuum, $P_\text{top} = 0$:

$$P_\text{atm} = P_\text{top} + \rho g h \implies h_\text{max} = \frac{P_\text{atm}}{\rho g} = \frac{101.3\times 10^3}{1000 \times 9.8} \approx 10.3\ \text{m}$$

Lung power is irrelevant beyond this: the atmosphere, not the drinker, does the lifting.

## Physical interpretation

$dP/dh = -\rho g$ says pressure is the *integrated weight per unit area* of fluid
above. That reading explains at a glance why mountain air is thin, why dams thicken
toward the base, and why [buoyancy](buoyancy.md) exists at all: a submerged body's
bottom feels more pressure than its top.

## Common mistakes

- **Using the incompressible formula for tall gas columns.** For air over kilometres,
  density varies — use a barometric formula.
- **Forgetting that only depth matters.** The pressure at the bottom of a wide lake and
  a narrow tube of equal depth is identical (the *hydrostatic paradox*).
- **Sign errors:** decide whether your coordinate increases up or down before
  integrating.

## Related concepts

- [Pressure](pressure.md) — prerequisite
- [Buoyancy](buoyancy.md) — direct consequence
- [Fluid in rigid-body motion](fluid-in-rigid-body-motion.md) — the generalization $\nabla P + \rho g\hat{k} = -\rho\mathbf{a}$
- [Euler's equation](../equations/euler-equation.md) — hydrostatics is the $\mathbf{v}=0$ special case

## Knowledge graph position

**Prerequisites:** [Pressure](pressure.md).
**Leads to:** [Buoyancy](buoyancy.md), [Hydrostatic force on surfaces](hydrostatic-force-on-surfaces.md), [Fluid in rigid-body motion](fluid-in-rigid-body-motion.md).

## Quiz

**Q1 (computational).** At what depth in fresh water does the absolute pressure double
from its surface value?

??? success "Answer"
    Need $\rho g h = P_\text{atm}$: $h = 101.3\times10^3/(1000\times 9.8) \approx 10.3$ m —
    the same number as the straw limit, and not a coincidence.

**Q2 (conceptual).** Two barometric formulas (isothermal and adiabatic) give different
pressures at 10 km. Which physical assumption differs?

??? success "Answer"
    The temperature profile: isothermal assumes $T$ constant with height; adiabatic
    assumes parcels exchange no heat, so $T$ falls with altitude. Reality (troposphere)
    sits between, closer to a constant lapse rate.

**Q3 (multiple choice).** In hydrostatic equilibrium, the pressure gradient vector
$\nabla P$ points:

- (a) opposite to gravity — upward
- (b) along gravity — downward
- (c) horizontally
- (d) it vanishes

??? success "Answer"
    **(b).** $\nabla P = \rho \mathbf{g}$: pressure increases in the direction gravity
    points (downward).
