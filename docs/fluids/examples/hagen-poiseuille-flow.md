# Example · Hagen–Poiseuille Flow

## Problem statement

A fluid of viscosity $\mu$ flows steadily through a circular pipe of radius $R$ under a
constant pressure gradient $dp/dx < 0$. Find the velocity profile and the volumetric
flow rate.

## Given information

- Pipe radius $R$, gradient $dp/dx$, viscosity $\mu$
- Steady, incompressible, fully developed, axisymmetric

## Solution strategy

Cylindrical [Navier–Stokes](../equations/navier-stokes-equation.md), axial component
only; integrate twice; regularity on the axis + no-slip at the wall.

## Step-by-step solution

1. The reduced equation:
   $$\frac{1}{r}\frac{d}{dr}\left(r\frac{du}{dr}\right) = \frac{1}{\mu}\frac{dp}{dx}$$
2. First integration:
   $r\frac{du}{dr} = \frac{1}{2\mu}\frac{dp}{dx}r^2 + C_1$
3. Second integration:
   $u(r) = \frac{1}{4\mu}\frac{dp}{dx}r^2 + C_1\ln r + C_2$
4. Velocity must stay finite at $r = 0$ ⇒ $C_1 = 0$.
   No-slip $u(R) = 0$ ⇒ $C_2 = -\frac{1}{4\mu}\frac{dp}{dx}R^2$.

## Final answer

$$\boxed{\,u(r) = \frac{1}{4\mu}\left(-\frac{dp}{dx}\right)\left(R^2 - r^2\right)\,}
\qquad
Q = \int_0^R u\,2\pi r\,dr = \boxed{\,\frac{\pi R^4}{8\mu}\left(-\frac{dp}{dx}\right)\,}$$

A **parabolic profile**, and the celebrated $R^4$ law.

## Key takeaways

- **$Q \propto R^4$** is brutal: narrow an artery by 20% and flow drops by ~59% at
  fixed gradient. This single exponent is why arterial stenosis and clogged pipes
  matter so much.
- [Dimensional analysis](../concepts/buckingham-pi-theorem.md#worked-example-pipe-flow-rate)
  gets $Q \sim \Delta P D^4/\mu L$ without solving anything — the exact solution
  supplies the $\pi/128$ (in diameter form).
- Valid while laminar: $Re \lesssim 2300$
  ([Reynolds number](../concepts/reynolds-number.md)); beyond that,
  [turbulence](../concepts/turbulence.md) steepens wall gradients and increases the
  effective resistance.

## Related

[Couette flow](couette-flow.md) ·
[Navier–Stokes equation](../equations/navier-stokes-equation.md) ·
[Buckingham Pi theorem](../concepts/buckingham-pi-theorem.md)
