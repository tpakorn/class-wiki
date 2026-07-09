# Example · Couette Flow

## Problem statement

A viscous fluid fills the gap $h$ between two parallel plates. The lower plate is
stationary; the upper plate slides at speed $U$. There is no pressure gradient. Find
the steady velocity profile $u(y)$.

## Given information

- Gap $h$, plate speed $U$, dynamic viscosity $\mu$
- Steady, incompressible, fully developed ($\partial/\partial x = 0$), no $dp/dx$

## Solution strategy

Symmetry slaughters the [Navier–Stokes equation](../equations/navier-stokes-equation.md):
one velocity component, one coordinate, no time. Integrate twice, apply
no-slip at both walls.

## Step-by-step solution

1. With $\mathbf{v} = (u(y), 0, 0)$, steady, and no pressure gradient, Navier–Stokes
   reduces to
   $$\frac{d^2 u}{dy^2} = 0$$
2. Integrate twice: $u(y) = C_1 y + C_2$.
3. Boundary conditions ([no-slip](../concepts/viscosity.md)):
   $u(0) = 0 \Rightarrow C_2 = 0$; $u(h) = U \Rightarrow C_1 = U/h$.

## Final answer

$$\boxed{\,u(y) = \frac{U}{h}\,y\,}$$

A perfectly **linear profile**. The shear stress
$\tau = \mu\,du/dy = \mu U/h$ is *uniform* across the gap — every layer drags its
neighbor equally.

## Key takeaways

- Couette flow is the physical realization of
  [Newton's law of viscosity](../equations/newtons-law-of-viscosity.md); rotational
  viscometers measure $\mu$ by building exactly this flow in an annulus.
- Momentum enters at the moving wall, diffuses across, and exits at the fixed wall —
  viscosity as momentum diffusion, in its purest form.
- Adding a pressure gradient superimposes a parabola on the line (Couette–Poiseuille
  flow) — linearity of the *reduced* equation makes superposition legal here.

## Related

[Viscosity](../concepts/viscosity.md) ·
[Hagen–Poiseuille flow](hagen-poiseuille-flow.md) ·
[Two-layer incline](two-layer-incline.md)
