# Rayleigh–Taylor Instability

## Intuition

Try to float water on top of oil: it won't stay. A heavy fluid resting on a light one
is an inverted pendulum — in perfect equilibrium, and doomed. Any ripple lets heavy
fluid slump down and light fluid rise; gravitational potential energy is released, the
ripple grows, and soon "fingers" of the dense fluid spike downward while bubbles of
light fluid rise. That is the Rayleigh–Taylor (RT) instability.

## Result

From the general [interface dispersion relation](../equations/interface-dispersion-relation.md)
with **no shear** ($U_1 = U_2 = 0$), fluid 1 (upper) density $\rho_1$, fluid 2 (lower)
$\rho_2$:

$$s = \sqrt{g k\,\frac{\rho_1 - \rho_2}{\rho_1 + \rho_2}}$$

- **Heavy over light** ($\rho_1 > \rho_2$): $s$ real and positive → exponential growth.
  The combination $\mathcal{A} = \frac{\rho_1 - \rho_2}{\rho_1 + \rho_2}$ is the
  **Atwood number**; growth rate $s = \sqrt{gk\mathcal{A}}$.
- **Light over heavy** ($\rho_2 > \rho_1$): $s$ imaginary → the interface *oscillates*:

$$\omega = \sqrt{g k\,\frac{\rho_2 - \rho_1}{\rho_1 + \rho_2}}$$

these are **interfacial gravity waves**. With $\rho_1 \to 0$ (air over water),
$\omega = \sqrt{gk}$, giving the deep-water phase speed

$$c = \frac{\omega}{k} = \sqrt{\frac{g}{k}}$$

— longer waves travel faster, which is why long swell arrives at the beach before the
storm that made it.

## Stabilization

Surface tension penalizes interface curvature and stabilizes short wavelengths: only
modes with

$$k^2 < \frac{g(\rho_1 - \rho_2)}{\gamma}$$

grow. This is why small drops hang stably from a ceiling but a large painted surface
"rains": there's a critical patch size beyond which some unstable wavelength fits.

## Where you see it

An overturned glass of water (air pushing up into water) · Crab Nebula filaments
(supernova ejecta decelerated by interstellar medium — effective gravity from
deceleration) · inertial-confinement fusion capsules (the great engineering enemy) ·
salt fingers in the ocean · mushroom clouds.

**Equivalence principle bonus:** "gravity" can be any acceleration of the interface.
Accelerating a light fluid *into* a heavy one is RT-unstable even sideways — this is
why ICF implosions and decelerating supernova shells share the same physics.

## Common mistakes

- **Thinking static equilibrium implies stability.** The stratified state satisfies
  [hydrostatics](hydrostatic-equilibrium.md) exactly; stability is a separate,
  perturbative question — see [hydrodynamic stability](hydrodynamic-stability.md).
- **Confusing RT and [Kelvin–Helmholtz](kelvin-helmholtz-instability.md):** RT needs a
  density inversion (or acceleration), no shear; KH needs shear, no inversion. (Real
  flows often have both — RT spikes develop KH curls on their flanks.)
- **Using the linear growth rate for late times.** Exponential growth is only the
  beginning; nonlinear spikes/bubbles follow different (power-law) laws.

## Related concepts

- [Interface dispersion relation](../equations/interface-dispersion-relation.md) — parent equation
- [Buoyancy](buoyancy.md) — the driving force
- [Hydrodynamic stability](hydrodynamic-stability.md) — the framework
- [Kelvin–Helmholtz instability](kelvin-helmholtz-instability.md) — the shear sibling

## Knowledge graph position

**Prerequisites:** [Hydrodynamic stability](hydrodynamic-stability.md), [Buoyancy](buoyancy.md).
**Leads to:** gravity-wave theory, [turbulent](turbulence.md) mixing.

## Quiz

**Q1 (computational).** Water ($\rho = 1000$) over air ($\rho = 1.2$), disturbance
wavelength 10 cm, ignore surface tension. Growth rate?

??? success "Answer"
    $k = 2\pi/0.1 \approx 62.8\ \text{m}^{-1}$, Atwood $\mathcal{A} \approx 0.9976$.
    $s = \sqrt{9.8 \times 62.8 \times 0.9976} \approx 24.8\ \text{s}^{-1}$ — e-folding
    in 40 ms. Overturned glasses empty fast.

**Q2 (conceptual).** Why can you nevertheless carry an overturned glass sealed by a
card (or keep water in a thin straw with a finger on top)?

??? success "Answer"
    Rigid boundaries/surface tension suppress the unstable modes: in a narrow tube, the
    longest wavelength that fits is shorter than the surface-tension cutoff
    $k_c = \sqrt{g\Delta\rho/\gamma}$, so no growing mode exists (and air pressure
    supplies the mean force).

**Q3 (multiple choice).** The deep-water gravity-wave dispersion $\omega = \sqrt{gk}$
is obtained from the RT analysis by taking:

- (a) $\rho_1 \gg \rho_2$  (b) $\rho_1 \to 0$ (light fluid above)  (c) $g \to 0$  (d) $k \to 0$

??? success "Answer"
    **(b).** Stable stratification with a negligible upper fluid = free-surface water
    waves.
