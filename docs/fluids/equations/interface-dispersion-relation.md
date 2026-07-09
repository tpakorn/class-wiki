# Interface Dispersion Relation (KH / RT / Surface Waves)

## Equation

For a perturbation $h \sim e^{ikx + st}$ of the interface between stream 1
($\rho_1, U_1$, above) and stream 2 ($\rho_2, U_2$, below), with gravity $g$ and
surface tension $\gamma$:

$$\boxed{\;s = -ik\,\frac{\rho_1 U_1 + \rho_2 U_2}{\rho_1 + \rho_2}
\pm \sqrt{\frac{k^2\rho_1\rho_2(U_1 - U_2)^2}{(\rho_1+\rho_2)^2}
+ \frac{kg(\rho_1 - \rho_2)}{\rho_1+\rho_2}
- \frac{\gamma k^3}{\rho_1+\rho_2}}\;}$$

Instability ⇔ the radicand is positive ⇔ $\operatorname{Re}(s) > 0$.

## Physical meaning

One formula, four phenomena, depending on which term wins under the square root:

| Dominant term | Phenomenon |
|---|---|
| shear $k^2\rho_1\rho_2(U_1-U_2)^2$ | [Kelvin–Helmholtz instability](../concepts/kelvin-helmholtz-instability.md) |
| gravity with $\rho_1 > \rho_2$ | [Rayleigh–Taylor instability](../concepts/rayleigh-taylor-instability.md) |
| gravity with $\rho_2 > \rho_1$ | stable **interfacial gravity waves** ($s = \pm i\omega$) |
| surface tension $\gamma k^3$ | capillary waves; stabilizes short wavelengths |

The real part of the first term is a Doppler shift: ripples ride the
density-weighted mean stream.

## Variables

$s$ — complex growth rate (s⁻¹): $\operatorname{Re}(s)$ = growth, $\operatorname{Im}(s)$ = oscillation ·
$k$ — wavenumber (m⁻¹) · $\rho_{1,2}$ — densities · $U_{1,2}$ — stream speeds ·
$g$ — gravity · $\gamma$ — surface tension (N/m).

## Assumptions

Inviscid · incompressible · irrotational away from the interface (vortex sheet at
$y=0$) · **linearized**: infinitesimal amplitude, $O(\epsilon^2)$ dropped · deep layers
(perturbations decay as $e^{\mp ky}$).

## Derivation outline

1. Base state: uniform potentials $\bar\phi_{1,2} = U_{1,2}\,x$; interface $y = 0$.
2. Perturb: $\phi_i = U_i x + \epsilon\phi_i'$, interface $y = \epsilon h(x,t)$;
   each $\phi_i'$ solves [Laplace](laplace-equation.md), decaying away from the
   interface: $\tilde\Phi_1 \propto e^{-ky}$, $\tilde\Phi_2 \propto e^{+ky}$.
3. **Kinematic condition** (interface moves with the fluid):
   $\partial_y\phi_i' = \partial_t h + U_i\,\partial_x h$ at $y = 0$, giving
   $\tilde\Phi_1(0) = -\frac{h_0}{k}(s + ikU_1)$, $\tilde\Phi_2(0) = \frac{h_0}{k}(s + ikU_2)$.
4. **Dynamic condition** (pressure continuity, with surface tension
   $P_1 = P_2 + \gamma\kappa$) via unsteady [Bernoulli](bernoulli-equation.md):
   $\rho_1[(s+ikU_1)\tilde\Phi_1(0) + gh_0] = \rho_2[(s+ikU_2)\tilde\Phi_2(0) + gh_0] - \gamma k^2 h_0$.
5. Nontrivial $h_0$ ⇒ the quadratic in $s$ above.

## Key special cases

- **Pure KH** ($g = \gamma = 0$): $s_+ = \frac{k|U_1-U_2|\sqrt{\rho_1\rho_2}}{\rho_1+\rho_2}$ — all wavelengths unstable, fastest at large $k$.
- **Pure RT** ($U_1 = U_2 = 0$, $\rho_1 > \rho_2$): $s = \sqrt{gk\,\mathcal{A}}$ with Atwood number $\mathcal{A} = \frac{\rho_1-\rho_2}{\rho_1+\rho_2}$.
- **Deep-water waves** ($\rho_1 \to 0$): $\omega^2 = gk + \gamma k^3/\rho_2$ — gravity–capillary dispersion; minimum phase speed ≈ 23 cm/s for water at $\lambda \approx 1.7$ cm.
- **Wind over water:** onset at $(U_1 - U_2)^2 = \frac{2(\rho_1+\rho_2)}{\rho_1\rho_2}\sqrt{\gamma g(\rho_2-\rho_1)}$ → critical wind ≈ 6.6 m/s.
- **3-D perturbations** ($e^{ikx+ilz}$, $\kappa = \sqrt{k^2+l^2}$): shear drive keeps
  $k^2$ but restoring terms use $\kappa$ — 2-D modes are the most dangerous.

## Limitations

Linear (onset only, no saturation or billow roll-up) · inviscid (no damping of short
waves except by tension) · sharp interface (finite shear layers cap the growth rate at
$k \sim 1/\text{thickness}$).

## Related equations

- [Laplace's equation](laplace-equation.md) — governs the perturbation potentials
- [Bernoulli's equation](bernoulli-equation.md) — the dynamic boundary condition

## Quiz

**Q1 (computational).** Deep-water gravity wave, $\lambda = 100$ m. Phase speed?

??? success "Answer"
    $c = \sqrt{g/k} = \sqrt{9.8\times100/2\pi} \approx 12.5$ m/s — ocean swell moves
    at highway speed.

**Q2 (conceptual).** Why does surface tension stabilize short waves but not long ones?

??? success "Answer"
    Its restoring term scales as $\gamma k^3$ — curvature energy grows fast as
    wavelength shrinks — while destabilizing gravity (RT) scales only as $kg\Delta\rho$.
    Below the capillary length the $k^3$ term always wins.
