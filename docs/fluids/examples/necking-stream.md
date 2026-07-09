# Example · Necking of a Falling Water Stream

## Problem statement

The smooth stream from a tap visibly narrows ("necks down") as it falls. Measuring the
cross-sectional area $A_0$ at the tap and $A$ at a distance $h$ below, determine the
volume flow rate $R_v$ — with a ruler, no flowmeter.

## Given information

- Areas $A_0$ (top) and $A$ (bottom), fall height $h$
- Laminar, steady stream; atmospheric pressure all around the jet

## Solution strategy

Two conservation laws on the free jet:
[continuity](../equations/continuity-equation.md) (what goes in comes out) and
[Bernoulli](../equations/bernoulli-equation.md) (free fall: pressure is atmospheric
everywhere on the jet surface, so speed grows like a dropped stone).

## Step-by-step solution

1. **Continuity:** $A_0 v_0 = A v \Rightarrow v = \dfrac{A_0 v_0}{A}$
2. **Bernoulli** between the two stations (equal pressure, height drop $h$):
   $$v^2 = v_0^2 + 2gh$$
3. Substitute and solve for $v_0$:
   $$\frac{A_0^2 v_0^2}{A^2} = v_0^2 + 2gh
   \;\Longrightarrow\;
   v_0 = \sqrt{\frac{2gh}{\dfrac{A_0^2}{A^2} - 1}}$$

## Final answer

$$\boxed{\;R_v = A_0 v_0 = A_0\sqrt{\frac{2gh}{\left(A_0/A\right)^2 - 1}}\;}$$

*(Equivalently $R_v = A_0 A\sqrt{\dfrac{2gh}{A_0^2 - A^2}}$.)*

## Key takeaways

- The stream narrows precisely because it speeds up: constant $Q = Av$ forces
  $A \propto 1/v$. The visible shape of a water stream *is* the continuity equation.
- Kitchen metrology: two diameters and a ruler give the flow rate to a few percent.
- The jet eventually breaks into drops — surface tension (Plateau–Rayleigh), a cousin
  of the [interface instabilities](../concepts/rayleigh-taylor-instability.md).

## Related

[Continuity equation](../equations/continuity-equation.md) ·
[Bernoulli's principle](../concepts/bernoulli-principle.md) ·
[Tank discharge](../concepts/bernoulli-principle.md#worked-example-tank-discharge-optimal-hole)
