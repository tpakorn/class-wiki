# Kelvin–Helmholtz Instability

## Intuition

Wind blowing over water makes waves. Two clouds layers sliding past each other roll up
into perfect billows. Wherever two fluid streams *shear* past one another, the
interface between them is a coiled spring: any tiny ripple deflects the flow, the
deflection changes the pressure ([Bernoulli](bernoulli-principle.md): faster = lower),
and the pressure difference amplifies the ripple. Shear + interface = instability.

## Setup and result

Two inviscid, irrotational streams: density $\rho_1$, speed $U_1$ above; $\rho_2$,
$U_2$ below, gravity $g$ down, interface at $y = 0$ perturbed as
$h \sim e^{ikx + st}$. Away from the interface the flow stays potential
($\nabla^2\phi_{1,2} = 0$, perturbations decaying as $e^{\mp ky}$); matching the
kinematic condition and pressure continuity (perturbed Bernoulli) yields the
**dispersion relation**:

$$s = -ik\,\frac{\rho_1 U_1 + \rho_2 U_2}{\rho_1 + \rho_2}
\;\pm\; \sqrt{\frac{k^2\rho_1\rho_2 (U_1 - U_2)^2}{(\rho_1+\rho_2)^2}
+ \frac{kg(\rho_1 - \rho_2)}{\rho_1 + \rho_2}}$$

(Full derivation on the [dispersion-relation page](../equations/interface-dispersion-relation.md).)
Instability ⇔ the square root is real and positive, i.e.

$$\boxed{\,k^2 \rho_1\rho_2 (U_1 - U_2)^2 > k g\,(\rho_2^2 - \rho_1^2)\,}$$

(with $\rho_2$ the lower/denser fluid).

## Reading the physics out of the formula

- **Any shear destabilizes short waves.** If $U_1 \neq U_2$, the $k^2$ shear term beats
  the $k$ gravity term at large $k$ — without extra physics, arbitrarily small
  wavelengths grow arbitrarily fast.
- **What tames it in reality:** viscosity (damps large $k$) and **surface tension**
  $\gamma$, which adds $-\gamma\kappa^3/(\rho_1+\rho_2)$ under the square root and
  stabilizes short waves. With both gravity and surface tension, stability holds while
  $$(U_1 - U_2)^2 < \frac{2(\rho_1+\rho_2)}{\rho_1\rho_2}\sqrt{\gamma g (\rho_2 - \rho_1)}$$
- **Wind over water:** $U_2 = 0$, $\rho_2 \gg \rho_1$ gives onset at
  $k > g\rho_2/(U_1^2\rho_1)$. With real air/water numbers the critical wind is
  $U_1 \approx 6.6\ \text{m/s}$ with first wavelength $\lambda \approx 1.7\ \text{cm}$ —
  ripples appear on a pond at a stiff breeze, as observed.
- **3-D perturbations** ($e^{ikx + ilz}$) are *less* unstable than 2-D ones with the
  same $k$ (Squire's theorem in spirit): the most dangerous billows are two-dimensional.

## Where you see it

Wind waves · billow clouds (Kelvin–Helmholtz clouds) · smoke rising into crosswind ·
the flanks of Jupiter's Great Red Spot · [magnetized versions in plasmas](../../plasma/index.md)
· mixing layers in jet engines.

## Common mistakes

- **Forgetting the vortex sheet.** The unperturbed interface carries infinite vorticity
  (velocity jump); "irrotational" applies only *away* from it.
- **Concluding "everything is always unstable".** The inviscid, tension-free result is
  a limiting idealization; real cutoffs matter and give the observed onset thresholds.
- **Confusing KH with [Rayleigh–Taylor](rayleigh-taylor-instability.md):** KH is
  *shear*-driven (can occur with stable stratification); RT is *buoyancy*-driven (no
  shear needed).

## Related concepts

- [Hydrodynamic stability](hydrodynamic-stability.md) — the method
- [Interface dispersion relation](../equations/interface-dispersion-relation.md) — the algebra
- [Rayleigh–Taylor instability](rayleigh-taylor-instability.md) — same equation, different limit
- [Potential flow](potential-flow.md) — the machinery of the derivation
- [Turbulence](turbulence.md) — KH billows are a classic route there

## Knowledge graph position

**Prerequisites:** [Hydrodynamic stability](hydrodynamic-stability.md), [Potential flow](potential-flow.md), [Bernoulli](bernoulli-principle.md).
**Leads to:** [Turbulence](turbulence.md), mixing-layer theory.

## Quiz

**Q1 (conceptual).** Explain in one sentence, using Bernoulli, why a bump on the
interface between two shearing streams grows.

??? success "Answer"
    The stream deflected over the bump speeds up, lowering pressure above it (and the
    one below slows, raising pressure beneath), so the net pressure difference pulls
    the bump further out.

**Q2 (computational).** For air over water with $U_1 = 10$ m/s, is a 1.7 cm ripple
unstable? ($\rho_1 = 1.22$, $\rho_2 = 1000\ \text{kg/m}^3$, $\gamma = 0.074$ N/m)

??? success "Answer"
    Critical speed is 6.6 m/s; at 10 m/s > 6.6 m/s the combined gravity–capillary
    restoring force is beaten and ripples near that wavelength grow. Yes — unstable.

**Q3 (multiple choice).** In the pure KH limit ($g = 0$, no surface tension), the
growth rate scales with wavenumber as:

- (a) $s \propto k^{1/2}$  (b) $s \propto k$  (c) $s \propto k^2$  (d) independent of $k$

??? success "Answer"
    **(b).** $s = k\,|U_1 - U_2|\sqrt{\rho_1\rho_2}/(\rho_1+\rho_2)$ — shortest waves
    grow fastest, which is why regularization physics is essential.
