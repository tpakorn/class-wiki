# Adiabatic Invariant

*Source lecture:* pc368_lec08_adiabatic_invariant

## Intuition

If you slowly squeeze a magnet, particles trapped in its field lines find
themselves in tighter orbits. The magnetic moment $\mu$—the ratio of the
perpendicular kinetic energy to the field strength—stays nearly constant. This
invarianc governs the mirror trapping of particles in the Earth’s radiation
belts and the heating of fusion plasmas.

## Formal Definition

An **adiabatic invariant** is a quantity that remains constant when external
parameters vary slowly compared to the particle’s internal dynamical timescale.
For magnetized particles, the first adiabatic invariant is the magnetic moment:

$$\mu = \frac{m v_\perp^2}{2 B}$$

## Mathematical Formulation

For a particle in a slowly varying **B**-field with $\Omega_c \gg \omega_{\text{drift}}$:

$$\mu = \frac{p_\perp^2}{2 m B} = \text{const along orbit}$$

The moment arises from averaging the perpendicular energy over one cyclotron
period. The condition for validity is:

$$\frac{1}{B} \frac{dB}{dt} \ll \Omega_c$$

## Derivation

1. Write the equation of motion perpendicular to **B**:

   $$m \dot{\mathbf{v}}_\perp = q \mathbf{v}_\perp \times \mathbf{B}$$

2. The perpendicular kinetic energy is $W_\perp = \frac{1}{2}m v_\perp^2$.
3. Differentiate $W_\perp/B$ using the slow-field condition:

   $$\frac{d}{dt}\Bigl(\frac{W_\perp}{B}\Bigr) \approx \frac{1}{B}\frac{dW_\perp}{dt} - \frac{W_\perp}{B^2}\frac{dB}{dt}$$

4. Because the gyration is periodic and the field changes adiabatically,
   $\langle dW_\perp/dt \rangle = 0$ over one gyroperiod.
5. Therefore $d\mu/dt = 0$ to leading order.

## Worked Example

> **Magnetic mirror trap:** A particle has $v_\parallel = 0$ at the mirror
> midplane where $B = B_0$. Its equatorial magnetic moment is $\mu_0 = m v_{\perp 0}^2/(2B_0)$.
> At the mirror throat $B_m$, the parallel velocity is:

$$v_\parallel^2 = \frac{2}{m}\Bigl(\mu_0 B_m - \frac{1}{2}m v_\perp^2\Bigr)$$

Reflection occurs when $v_\parallel \to 0$, i.e. when $\sin^2\theta_0 = B_0/B_m$.
Particles with small enough pitch angle escape.

## Common Mistakes

- **$\mu$ is always constant.** It fails if $B$ changes on the timescale of the
  gyroperiod ($\omega_B/\Omega_c \not\ll 1$).
- **Confusing invariants.** The first invariant is $\mu$; the second involves
> the bounce action; the third is magnetic flux enclosed.
- **Mirror trapping is perfect.** In real scenarios, collisions and non-adiabatic
  scattering destroy trapping.

## Related Concepts

- [Drift Motion](drift-motion.md)
- [Magnetic Mirror](magnetic-mirror.md)
- [Larmor Radius](larmor-radius.md)

## Quiz Questions

1. **Conceptual:** Why does $\mu$ conservation imply that particles move to
   regions of weaker $B$ when they gain perpendicular energy?
2. **Computational:** A proton with $W_\perp = 5$ keV enters a region where
   $B$ doubles adiabatically. What is its new $W_\perp$?
3. **MCQ:** The adiabatic invariant applies when:
   - A) $|dB/dt| \gg \Omega_c B$
   - B) $|dB/dt| \ll \Omega_c B$
   - C) $B$ is zero
   - D) The particle is unmagnetized

## Further Reading

- M. Walt, *Introduction to Geomagnetically Trapped Radiation*.
