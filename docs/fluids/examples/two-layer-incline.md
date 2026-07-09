# Example · Two-Layer Flow Down an Inclined Plane

## Problem statement

Two immiscible fluid films flow steadily down a plane inclined at angle $\theta$:
layer 1 of viscosity $\mu_1$ and thickness $h_1$ lies on the plane, layer 2 of
viscosity $\mu_2$ and thickness $h_2$ lies on top, with a free surface above. Gravity
drives the flow. Find the velocity profile in each layer.

## Given information

- Depths $h_1$ (bottom layer), $h_2$ (top layer); viscosities $\mu_1$, $\mu_2$
- Steady, fully developed, incompressible; no imposed pressure gradient along the plane

## Solution strategy

In each layer the [Navier–Stokes equation](../equations/navier-stokes-equation.md)
reduces to a gravity–viscosity balance:

$$0 = \mu_i \frac{d^2 u_i}{dy^2} + \rho g\sin\theta$$

Integrate twice per layer (4 constants) and spend the 4 boundary/matching conditions:

1. **No-slip at the plane:** $u_1(0) = 0$
2. **Velocity continuity at the interface:** $u_1(h_1) = u_2(h_1)$
3. **Shear-stress continuity at the interface:**
   $\mu_1\,u_1'(h_1) = \mu_2\,u_2'(h_1)$
4. **Free surface:** $u_2'(h_1 + h_2) = 0$ (no shear from the air)

## Step-by-step solution

Each layer integrates to $u_i(y) = -\frac{\rho g\sin\theta}{2\mu_i}y^2 + C_i y + D_i$.

Working through the conditions (start from the free surface: condition 4 fixes the
total stress profile — the shear at height $y$ must carry the weight of all fluid above
it, $\tau(y) = \rho g\sin\theta\,(h_1 + h_2 - y)$, which automatically satisfies
condition 3 for equal densities):

$$u_1(y) = \frac{\rho g\sin\theta}{\mu_1}\left[(h_1 + h_2)\,y - \frac{y^2}{2}\right]$$

$$u_2(y) = \frac{\rho g\sin\theta}{\mu_2}\left[(h_1+h_2)\,y - \frac{y^2}{2}\right]
+ \rho g \sin\theta\left[\frac{h_1^2}{2} - (h_1+h_2)h_1\right]\left(\frac{1}{\mu_2} - \frac{1}{\mu_1}\right)$$

## Final answer

Two parabolic arcs, glued with equal velocity and equal shear stress at $y = h_1$; the
kink in slope at the interface is the viscosity ratio made visible:
$u_2'/u_1'|_{h_1} = \mu_1/\mu_2$.

## Key takeaways

- **The interface conditions are the entire problem.** Velocity continuous (no
  slip between liquids), *stress* continuous (Newton's third law) — and stress
  continuity means the velocity *gradient* jumps when viscosities differ.
- The shear-stress profile is set by statics alone (weight of fluid above); viscosity
  only decides how much shearing that stress produces.
- Limits check: $\mu_1 = \mu_2$ recovers the single-film Nusselt profile; a very
  viscous bottom layer ($\mu_1 \to \infty$) becomes an effective solid floor for the
  top layer.

## Related

[Couette flow](couette-flow.md) ·
[Viscosity](../concepts/viscosity.md) ·
[Navier–Stokes equation](../equations/navier-stokes-equation.md)
