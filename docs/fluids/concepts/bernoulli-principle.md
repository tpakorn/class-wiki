# Bernoulli's Principle

## Intuition

A fluid particle sliding along a streamline is like a bead on a frictionless wire: it
trades one form of energy for another, never losing any. Speed up → pressure drops.
Climb → pressure or speed must pay for the height. Bernoulli's equation is just energy
book-keeping per unit volume of moving fluid — valid exactly when nothing (viscosity,
shocks, heat) can steal from the account.

## The equation

For **steady, inviscid, incompressible** flow along a streamline:

$$\boxed{\,p + \tfrac{1}{2}\rho v^2 + \rho g z = \text{constant}\,}$$

Three terms, three energies per unit volume: pressure work, kinetic, gravitational
potential. See the [equation page](../equations/bernoulli-equation.md) for variables,
assumptions and applications in detail.

## Derivation (Newton along a streamline)

Apply $F = ma$ to a fluid element of length $ds$ and cross-section $dA$ along a
streamline: pressure difference $-dP\,dA$ and gravity component $-\rho g\,dA\,ds\,
\frac{dz}{ds}$ drive acceleration $V\frac{dV}{ds}$:

$$-dP - \rho g\, dz = \rho V\, dV
\;\Longrightarrow\;
\frac{dP}{\rho} + \tfrac{1}{2}d(V^2) + g\,dz = 0$$

For constant $\rho$, integrate → Bernoulli. The same result follows from integrating
[Euler's equation](../equations/euler-equation.md) along a streamline.

## Compressible extensions

If $\rho$ varies, keep $\int dP/\rho$ and specify thermodynamics:

- **Isothermal** ideal gas ($P = \rho R T$):
  $\;RT\ln P + \tfrac{1}{2}V^2 + gz = \text{const.}$
- **Isentropic** ($P/\rho^\gamma$ const.):
  $\;\dfrac{\gamma}{\gamma - 1}\dfrac{P}{\rho} + \tfrac{1}{2}V^2 + gz = \text{const.}$

The isentropic form is the workhorse of compressible aerodynamics below shock
strength; across a [shock](shock-waves.md) Bernoulli **fails** (entropy jumps).

## Worked example: tank discharge, optimal hole

Water drains from a tank filled to height $H$ through a small hole at height $h$.
Where should the hole be for the jet to land farthest?

Bernoulli from the surface to the hole: $v = \sqrt{2g(H - h)}$ (Torricelli).
Projectile fall time: $t = \sqrt{2h/g}$. Range:

$$x = vt = 2\sqrt{h(H - h)}$$

Maximizing: $\frac{dx}{dh} = 0 \Rightarrow H - 2h = 0 \Rightarrow \boxed{h = H/2}$,
with maximum range $x = H$. Elegant symmetry: holes at $h$ and $H-h$ hit the same spot.

## More classics solved on linked pages

- [Venturi effect](pressure.md#worked-example-the-venturi-effect) — pressure drop in a constriction
- [Necking of a falling water stream](../examples/necking-stream.md)
- [Superman's straw](hydrostatic-equilibrium.md#worked-example-superman-with-a-straw) — the static limit

## Common mistakes

- **Applying it across streamlines** — the constant is per-streamline unless the flow
  is irrotational ([potential flow](potential-flow.md)), where it becomes global.
- **Using it in viscous regions** (boundary layers, pipes with friction) or across
  [shocks](shock-waves.md) — energy is dissipated there.
- **The "equal transit time" airfoil myth.** Lift does follow from pressure differences
  consistent with Bernoulli, but the premise that parcels split at the leading edge
  must reunite at the trailing edge is simply false.
- **Forgetting the elevation term** in anything taller than a bench-top apparatus.

## Related concepts

- [Euler's equation](../equations/euler-equation.md) — parent equation
- [Continuity equation](../equations/continuity-equation.md) — almost always used together
- [Potential flow](potential-flow.md) — where Bernoulli holds everywhere
- [Shock waves](shock-waves.md) — where it breaks

## Knowledge graph position

**Prerequisites:** [Pressure](pressure.md), [Material derivative](material-derivative.md), [Continuity](../equations/continuity-equation.md).
**Leads to:** [Potential flow](potential-flow.md), [Kelvin–Helmholtz analysis](kelvin-helmholtz-instability.md) (perturbed Bernoulli at the interface).

## Quiz

**Q1 (computational).** Wind of speed 30 m/s ($\rho = 1.2\ \text{kg m}^{-3}$) blows
over a flat roof. Estimate the lift pressure (suction) relative to still air inside.

??? success "Answer"
    $\Delta p = \tfrac12 \rho v^2 = 0.5\times1.2\times900 = 540$ Pa — about 54 kg-force
    per square metre. This is why roofs peel *upward* in storms.

**Q2 (conceptual).** Two identical tanks drain through identical holes, one at the
bottom, one halfway up. Which jet travels farther on level ground at the tank base?

??? success "Answer"
    The halfway hole ($h = H/2$ is optimal; the bottom hole has maximum speed but zero
    fall time, so range → 0).

**Q3 (multiple choice).** Which assumption is *not* required for the basic Bernoulli
equation?

- (a) steady flow  (b) incompressible  (c) irrotational everywhere  (d) inviscid

??? success "Answer"
    **(c).** Along a single streamline, rotationality doesn't matter. Irrotationality
    only upgrades the constant from per-streamline to global.
