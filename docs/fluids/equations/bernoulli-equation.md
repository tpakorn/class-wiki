# Bernoulli's Equation

## Equation

$$\boxed{\,p + \tfrac{1}{2}\rho v^2 + \rho g z = \text{constant along a streamline}\,}$$

Compressible variants (replace $p/\rho$ by $\int dp/\rho$):

- Isothermal ideal gas: $RT\ln p + \tfrac12 v^2 + gz = \text{const}$
- Isentropic: $\dfrac{\gamma}{\gamma-1}\dfrac{p}{\rho} + \tfrac12 v^2 + gz = \text{const}$

## Physical meaning

Energy conservation per unit volume for a frictionless fluid parcel: pressure work +
kinetic energy + gravitational potential energy is a fixed budget. Speed up ⇒ pressure
down; climb ⇒ pay from pressure or speed.

## Variables

| Symbol | Meaning | SI unit |
|---|---|---|
| $p$ | static pressure | Pa |
| $\rho$ | density | kg m⁻³ |
| $v$ | speed along the streamline | m s⁻¹ |
| $z$ | elevation | m |
| $\gamma$ | ratio of specific heats | – |

## Assumptions

1. **Steady** flow · 2. **Inviscid** · 3. **Incompressible** (basic form) ·
4. **Along a streamline** (global constant only if also irrotational —
[potential flow](../concepts/potential-flow.md)) · 5. No shaft work or heat addition.

## Derivation

Newton along a streamline (see the
[concept page](../concepts/bernoulli-principle.md) for the full walk-through):

$$-dp - \rho g\,dz = \rho V\,dV \;\Rightarrow\; \frac{dp}{\rho} + \tfrac12 d(V^2) + g\,dz = 0$$

then integrate with the appropriate $\rho(p)$ relation. Equivalently, integrate
[Euler's equation](euler-equation.md) along $d\mathbf{s} \parallel \mathbf{v}$.

## Worked examples

- [Venturi meter](../concepts/pressure.md#worked-example-the-venturi-effect):
  $h = \frac{v_1^2}{2g}\left(\frac{A_1^2}{A_2^2}-1\right)$
- [Torricelli draining & optimal hole](../concepts/bernoulli-principle.md#worked-example-tank-discharge-optimal-hole): $v = \sqrt{2g(H-h)}$
- [Necking stream](../examples/necking-stream.md): flow-rate measurement with a ruler
- Pitot tube: stagnation minus static pressure = $\tfrac12\rho v^2$ → airspeed

## Limitations

Fails in boundary layers and separated/viscous regions, across
[shocks](rankine-hugoniot-conditions.md) and hydraulic jumps, through pumps/turbines
(add work terms), and in strongly unsteady flow (an unsteady term
$\rho\,\partial\phi/\partial t$ can be retained — used in the
[interface instability derivation](interface-dispersion-relation.md)).

## Related equations

- [Euler's equation](euler-equation.md) — parent
- [Continuity equation](continuity-equation.md) — constant companion
- [Interface dispersion relation](interface-dispersion-relation.md) — built on perturbed Bernoulli

## Quiz

**Q1 (computational).** A pitot-static probe on an aircraft reads
$\Delta p = 4.5$ kPa in air of density 0.9 kg/m³. Airspeed?

??? success "Answer"
    $v = \sqrt{2\Delta p/\rho} = \sqrt{2\times4500/0.9} = 100$ m/s.

**Q2 (conceptual).** Why can't Bernoulli's equation be used through a household fan,
even though the flow before and after is fast and smooth?

??? success "Answer"
    The fan does shaft work on the fluid — the energy budget jumps between inlet and
    outlet streamlines. Bernoulli holds separately upstream and downstream, not across
    the energy source.
