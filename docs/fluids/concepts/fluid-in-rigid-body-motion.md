# Fluid in Rigid-Body Motion

## Intuition

Slam the brakes with a coffee in your cup holder: the surface tilts. Spin a bucket of
water: the surface forms a bowl. In both cases the fluid moves *as a rigid body* — no
shearing between layers — so it is still "statics", just in an accelerating frame.
Pressure now has to balance gravity **and** supply the acceleration.

## Mathematical formulation

For a fluid element $dx\,dy\,dz$, the surface force is $-\nabla P\, dV$ and the body
force is $-\rho g\,\hat{k}\, dV$. Newton's second law gives the governing equation:

$$\boxed{\,\nabla P + \rho g\,\hat{k} = -\rho\,\mathbf{a}\,}$$

Hydrostatics is the special case $\mathbf{a} = 0$.

## Three canonical cases

**1 · Free fall** ($\mathbf{a} = -g\hat{k}$): the equation gives $\nabla P = 0$ —
pressure is *uniform*. A freely falling container feels no internal pressure gradient;
the bottom feels only atmospheric pressure. (Fluids in orbit behave the same way.)

**2 · Uniform linear acceleration** ($\mathbf{a} = a_x\hat{i} + a_z\hat{k}$):

$$\frac{\partial P}{\partial x} = -\rho a_x, \qquad \frac{\partial P}{\partial z} = -\rho(g + a_z)$$

$$P(x,z) = P_0 - \rho a_x x - \rho(g + a_z) z$$

Isobars (and the free surface) are inclined planes with slope

$$\frac{\Delta z_s}{\Delta x} = -\frac{a_x}{g + a_z}.$$

**3 · Rotating container** (angular velocity $\omega$, cylindrical coordinates): the
centripetal acceleration $-r\omega^2\hat{r}$ gives

$$\frac{\partial P}{\partial r} = \rho r \omega^2, \qquad \frac{\partial P}{\partial z} = -\rho g$$

Setting $dP = 0$ yields the isobar slope $dz/dr = r\omega^2/g$, hence a
**paraboloid of revolution**. Matching the fluid volume $V = \pi R^2 h_0$ fixes the
free surface:

$$z_s = h_0 - \frac{\omega^2}{4g}\left(R^2 - 2r^2\right)$$

## Application: the liquid-mirror telescope

The Large Zenith Telescope used a slowly rotating dish of mercury: rotation makes the
surface an exact paraboloid — precisely the shape a telescope mirror needs — for a tiny
fraction of the cost of polished glass. The focal length is set by $\omega$:
$f = g/(2\omega^2)$.

## Common mistakes

- **Forgetting the $g + a_z$ coupling** — vertical acceleration changes the *effective
  gravity*, which also rescales buoyancy.
- **Assuming the deepest point stays put when spinning up.** Fluid rises at the rim and
  dips at the axis by equal volume: $z_s(0) = h_0 - \omega^2R^2/4g$.
- **Applying these results to sheared flows.** Rigid-body motion means *no relative
  motion* between fluid particles — otherwise viscosity enters and you need
  [Navier–Stokes](../equations/navier-stokes-equation.md).

## Related concepts

- [Hydrostatic equilibrium](hydrostatic-equilibrium.md) — the $\mathbf{a}=0$ base case
- [Euler's equation](../equations/euler-equation.md) — the full inviscid momentum equation this is a corollary of
- [Buoyancy](buoyancy.md) — rescaled by effective gravity in accelerating frames

## Knowledge graph position

**Prerequisites:** [Hydrostatic equilibrium](hydrostatic-equilibrium.md).
**Leads to:** [Euler's equation](../equations/euler-equation.md).

## Quiz

**Q1 (computational).** A tank of water accelerates horizontally at
$a_x = 4.9\ \text{m s}^{-2}$. At what angle does the free surface tilt?

??? success "Answer"
    $\tan\alpha = a_x/g = 0.5 \Rightarrow \alpha \approx 26.6°$, surface tilting up
    toward the rear of the tank.

**Q2 (conceptual).** In a freely falling elevator, a cork is held at the bottom of a
water bottle and released. Does it rise?

??? success "Answer"
    No. Free fall makes $\nabla P = 0$ — no pressure gradient, no
    [buoyancy](buoyancy.md). The cork just floats where it is (effective gravity is
    zero).

**Q3 (multiple choice).** Doubling $\omega$ for a rotating bucket changes the dip of
the surface at the axis by a factor of:

- (a) 2  (b) 4  (c) $\sqrt{2}$  (d) 8

??? success "Answer"
    **(b).** The dip is $\omega^2 R^2/4g \propto \omega^2$.
