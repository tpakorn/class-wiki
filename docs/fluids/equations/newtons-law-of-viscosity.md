# Newton's Law of Viscosity

## Equation

$$\boxed{\,\tau = \mu\,\frac{du}{dy}\,}$$

## Physical meaning

Shear stress between fluid layers is proportional to how fast the velocity changes
across them. It is a **constitutive law** — a statement about a *material*, not a
conservation law — defining what "Newtonian fluid" means and giving
[viscosity](../concepts/viscosity.md) its operational definition: $\mu$ is the slope of
stress vs shear rate.

## Variables

| Symbol | Meaning | SI unit |
|---|---|---|
| $\tau$ | shear stress | Pa |
| $\mu$ | dynamic viscosity | Pa·s |
| $du/dy$ | velocity gradient (shear rate) | s⁻¹ |

Typical $\mu$ values: air $1.8\times10^{-5}$, water $1.0\times10^{-3}$, honey ~$10$ Pa·s.

## Assumptions

- Newtonian fluid: $\mu$ independent of shear rate (water, air, most oils — but not
  paint, blood, or cornstarch slurry)
- Simple shear geometry (the tensor generalization
  $T_{ij}^{visc} = \mu(\partial_i v_j + \partial_j v_i)$ feeds the
  [Navier–Stokes equation](navier-stokes-equation.md))

## Interpretation

Momentum diffuses down its gradient, exactly like heat down a temperature gradient
(Fourier) or species down a concentration gradient (Fick). The diffusivity is
$\nu = \mu/\rho$: kinematic viscosity, units m²/s — compare it directly with thermal
diffusivity to get the Prandtl number.

## Applications

- Measuring viscosity (rotational viscometers implement
  [Couette flow](../examples/couette-flow.md))
- Wall shear stress and skin-friction drag
- Lubrication films, blood-vessel wall stress, syrup coating

## Limitations

Non-Newtonian fluids need $\mu(\dot\gamma)$ or full viscoelastic models; rarefied gases
break the continuum premise.

## Related equations

- [Navier–Stokes equation](navier-stokes-equation.md) — where it enters as the stress model
- [TKE transport equation](tke-transport-equation.md) — its dissipative fingerprint in turbulence

## Quiz

**Q1 (computational).** A 0.1 mm oil film ($\mu = 0.1$ Pa·s) separates a 0.1 m² sliding
block from the floor. Force to slide at 0.5 m/s?

??? success "Answer"
    $F = \tau A = \mu \frac{U}{h}A = 0.1\times\frac{0.5}{10^{-4}}\times0.1 = 50$ N.

**Q2 (conceptual).** Ketchup refuses to flow, then gushes. Which viscosity class, and
what does the $\tau$–$\dot\gamma$ curve look like?

??? success "Answer"
    Shear-thinning (with a yield stress): the curve starts at a finite $\tau$ at zero
    rate and its slope (apparent $\mu$) decreases as shear rate rises. Shaking raises
    the shear rate, collapsing the viscosity.
