# Drift Motions

*Source lecture(s):* [pc368_lec07_drift](../lectures.md)

## Intuition

A charged particle gyrates rapidly around a magnetic field line. If the field has a
gradient, or if there is an electric field perpendicular to **B**, the center of
the gyration orbit moves slowly across **B**. These **drift motions** govern
particle transport in non-uniform magnetized plasmas.

## Formal Definition

A **drift** is the guiding-center motion perpendicular to the local magnetic field.
For slowly varying fields ($\omega/\Omega_c \ll 1$) and $v_\perp, v_\parallel$
constant over a gyroperiod, the average velocity is:

$$\mathbf{v}_d = \frac{\mathbf{F} \times \mathbf{B}}{q B^2}$$

where $\mathbf{F}$ is any external force.

## Mathematical Formulation

1. **$\mathbf{E}\times\mathbf{B}$ drift:**

   $$\mathbf{v}_{E\times B} = \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

   Independent of charge and mass.

2. **Gradient drift:**

   $$\mathbf{v}_{\nabla B} = \frac{m v_\perp^2}{2 q B^3} (\mathbf{B} \times \nabla B)$$

3. **Curvature drift:**

   $$\mathbf{v}_c = \frac{m v_\parallel^2}{q B^3} \bigl[\mathbf{b} \times (\mathbf{b}\cdot\nabla)\mathbf{b}\bigr]$$

4. **Gravity drift:**

   $$\mathbf{v}_g = \frac{m \mathbf{g} \times \mathbf{B}}{q B^2}$$

## Derivation

Use the guiding-center expansion:

1. Decompose $\mathbf{r} = \mathbf{R} + \boldsymbol{\rho}$, where $\mathbf{R}$ is the
   guiding center and $\boldsymbol{\rho}$ is the gyration vector.
2. Slow fields: $\mathbf{E}(\mathbf{R}), \mathbf{B}(\mathbf{R})$.
3. Average the Lorentz force over one cyclotron period.
4. The drift velocity emerges from the $\mathbf{E}\times\mathbf{B}$ advection
   and the polarization drift from time-varying **E**.

For the gradient drift, note that the orbital radius $\rho_L = m v_\perp/|q|B$
changes as $B$ varies, giving an net orbital excursion proportional to $\nabla B$.

## Worked Example

> **Tokamak ion gradient drift:** In a tokamak with circular cross-section, the
> toroidal field $B_\phi \sim 1/R$ has a gradient toward the center. Compute the
> drift direction for a co-going ion ($v_\parallel$ along $\hat{z}$).
> Using $\mathbf{v}_c \propto m v_\parallel^2 B^{-3}(\mathbf{b}\times\kappa)$,
> the curvature vector points outward ($+\hat{r}$), so the drift is vertically
> upward for ions ($q>0$).

## Common Mistakes

- **Drift speed is set by $v_\perp$ or $v_\parallel$.** Confusing them gives wrong
  scaling.
- **Drifts are NOT caused by $\mathbf{E}$ alone.** The gradient and curvature
  drifts persist even in vacuum **B**-fields.
- **Polarization drift is order $\omega/\Omega_c$.** It is often small but
  becomes important in time-dependent problems.

## Related Concepts

- [Adiabatic Invariant](adiabatic-invariant.md)
- [Larmor Radius](larmor-radius.md)
- [Magnetic Mirror](magnetic-mirror.md)

## Quiz Questions

1. **Conceptual:** Why do electrons and ions drift in the *same* direction under
   $\mathbf{E}\times\mathbf{B}$ but in *opposite* directions under $\nabla B$?
2. **Computational:** For a $\nabla B$ drift in $B = 1$ T with gradient
   $\nabla B/B = 0.1/m$, find $v_{\nabla B}$ for 1 keV protons with
   $v_\perp = v_\parallel$.
3. **MCQ:** Which drift is independent of the particle’s charge?
   - A) $\mathbf{E}\times\mathbf{B}$
   - B) Gradient
   - C) Curvature
   - D) Gravity

## Further Reading

- W. Baumjohann & R. A. Treumann, *Basic Space Plasma Physics*.
