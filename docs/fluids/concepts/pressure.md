# Pressure

## Intuition

Dive to the bottom of a pool and your ears hurt — equally, whichever way you tilt your
head. That's the two essential facts about pressure in one experience: it grows with
the weight of fluid above you, and at any single point it pushes the *same in every
direction*. Pressure is not a vector pointing somewhere; it is a scalar intensity of
squeezing.

## Formal definition

Pressure is normal force per unit area, in the limit of a vanishing area element:

$$P = \lim_{\Delta A \to 0} \frac{\Delta F}{\Delta A}$$

with SI unit the **pascal** ($\text{Pa} \equiv \text{N m}^{-2}$). The force due to
pressure is always *normal* to a surface, and pressure is *isotropic* — the same in all
directions at a point.

Two conventions:

| Quantity | Reference | Sign |
|---|---|---|
| **Absolute pressure** $P_\text{abs}$ | perfect vacuum | always $\geq 0$ |
| **Gauge pressure** $P_\text{gauge}$ | local atmosphere | either sign |

$$P_\text{abs} = P_\text{gauge} + P_\text{atm}, \qquad P_\text{atm} \approx 101.3\ \text{kPa at sea level}.$$

## Derivation: why pressure is isotropic

Take a small triangular wedge of fluid at rest (base $\Delta x$, height $\Delta z$,
hypotenuse at angle $\theta$), with pressures $P_1, P_2, P_3$ on its three faces.
Force balance:

$$\sum F_x = 0:\quad P_1 \Delta y\,\Delta z - P_3 \Delta y\, l \sin\theta = 0$$

$$\sum F_z = 0:\quad P_2 \Delta x\,\Delta y - P_3 \Delta y\, l\cos\theta - \tfrac{1}{2}\rho g\,\Delta x\,\Delta y\,\Delta z = 0$$

With $\Delta x = l\cos\theta$ and $\Delta z = l\sin\theta$, the first gives
$P_1 = P_3$; the second gives $P_2 - P_3 = \tfrac{1}{2}\rho g \Delta z \to 0$ as the
wedge shrinks. Hence

$$P_1 = P_2 = P_3$$

— pressure at a point is independent of the orientation of the surface you measure it
on. This is why it is a scalar.

## Worked example: the Venturi effect

A fluid of density $\rho$ flows through a pipe that narrows from area $A_1$ to $A_2$.
Manometer columns show a height difference $h$. Find $h$ in terms of $v_1, A_1, A_2, g$.

From the [continuity equation](../equations/continuity-equation.md), $A_1 v_1 = A_2 v_2$.
From [Bernoulli](../equations/bernoulli-equation.md) at equal elevation:

$$p_1 - p_2 = \tfrac{1}{2}\rho\left(v_2^2 - v_1^2\right) = \rho g h$$

$$\boxed{\,h = \frac{v_1^2}{2g}\left(\frac{A_1^2}{A_2^2} - 1\right)}$$

Faster flow ⇒ lower pressure: the fluid level *drops* over the constriction.

## Common mistakes

- **Treating pressure as a vector.** The *force* $P\,d\mathbf{A}$ has direction; $P$
  itself does not.
- **Mixing gauge and absolute pressure** in the ideal-gas law or in
  [barometric formulas](hydrostatic-equilibrium.md) — those need absolute pressure.
- **Assuming pressure pushes only downward.** Water pushes *up* on the bottom of a
  boat, sideways on a dam. Direction comes from the surface, not from $P$.

## Related concepts

- [Hydrostatic equilibrium](hydrostatic-equilibrium.md) — how $P$ varies with depth/height
- [Buoyancy](buoyancy.md) — the net upward force born from that variation
- [Hydrostatic force on surfaces](hydrostatic-force-on-surfaces.md) — integrating $P\,dA$
- [Bernoulli's principle](bernoulli-principle.md) — pressure–velocity trade-off in motion

## Knowledge graph position

**Prerequisites:** [What is a fluid?](what-is-a-fluid.md)
**Leads to:** [Hydrostatic equilibrium](hydrostatic-equilibrium.md), [Buoyancy](buoyancy.md), [Bernoulli's principle](bernoulli-principle.md).

## Quiz

**Q1 (computational).** A scuba diver is at 20 m depth in seawater
($\rho = 1025\ \text{kg m}^{-3}$). What is the gauge pressure and the absolute pressure?

??? success "Answer"
    $P_\text{gauge} = \rho g h = 1025 \times 9.8 \times 20 \approx 201\ \text{kPa}$.
    $P_\text{abs} = 201 + 101.3 \approx 302\ \text{kPa}$ — about 3 atm.

**Q2 (conceptual).** The wedge derivation assumed the fluid was at rest. Where exactly
did that assumption enter?

??? success "Answer"
    We set the net force to zero (equilibrium) and included *no shear stresses* on the
    faces — only a fluid at rest exerts purely normal stresses. In a moving viscous
    fluid the stress tensor gains off-diagonal (shear) terms.

**Q3 (multiple choice).** A vertical dam wall holds back water. The pressure force on
the wall is:

- (a) vertical, equal to the weight of the water
- (b) horizontal, increasing linearly with depth
- (c) uniform over the wall
- (d) zero, since the water is static

??? success "Answer"
    **(b).** Pressure acts normal to the wall (horizontally) and grows as
    $\rho g h$ with depth — see [forces on submerged surfaces](hydrostatic-force-on-surfaces.md).
