# Plasma Sheath

*Source lecture:* pc368_lec06_shealth

## Intuition

A plasma cannot touch a solid wall directly. Because electrons are lighter and faster,
they would otherwise rush to the wall and charge it negatively, repelling further
electron flow while pulling in ions. The result is a **sheath**—a non-neutral boundary
layer that sustains a potential drop and enforces charge neutrality across the
plasma–wall interface.

## Formal Definition

A **sheath** is a space-charge region adjacent to a material surface where quasi-neutrality
is violated to satisfy the **Bohm sheath criterion**:

$$c_s = \sqrt{\frac{\gamma_e T_e + \gamma_i T_i}{m_i}}$$

Ions must enter the sheath with at least the sound speed $c_s$.

## Mathematical Formulation

In a stationary, collisionless sheath with isothermal electrons:

1. **Ion continuity:** $n_i v_i = \text{const}$
2. **Ion momentum:** $m_i v_i \frac{dv_i}{dx} = -e \frac{d\phi}{dx}$
3. **Electron Boltzmann:** $n_e(x) = n_{e0} \exp\Bigl(\frac{e\phi(x)}{k_B T_e}\Bigr)$
4. **Poisson:** $\frac{d^2\phi}{dx^2} = -\frac{e}{\varepsilon_0}\bigl[n_i(x) - n_e(x)\bigr]$

## Derivation

1. Assume ions enter the sheath at $x=0$ with $v_i(0) \ge c_s$.
2. Integration of ion momentum gives the **Bohm–Chen** relation:

   $$\frac{1}{2}m_i v_i^2 + e\phi(x) = \frac{1}{2}m_i c_s^2$$

3. Combine continuity ($n_i = J_i / v_i$) with Boltzmann electrons.
4. Substitute into Poisson. The resulting integral describes the sheath potential.
5. The only self-consistent solution requires $v_i(0) = c_s$ exactly at the sheath
   edge ($\phi=0$).

## Worked Example

> **Langmuir probe:** A cylindrical probe biased negative relative to the plasma
> draws ion current $I_i = en_i A c_s$. The electron current is exponentially
> suppressed by the sheath drop.
> If $T_e = 2$ eV and $m_i = 40$ amu (argon), compute $c_s$.
> $c_s = \sqrt{(\gamma_e T_e)/m_i} \approx \sqrt{1\times 2\,\text{eV} / (40\times 1836 m_e)} \approx 1.6\times 10^3\,\text{m/s}$.

## Common Mistakes

- **Sheath is a material boundary condition.** It is not a collisionless plasma wave.
- **Ignoring electron inertia.** Electrons are Boltzmann-distributed; ions are the
  dynamical carriers.
- **Ion supersonic entry.** Sub-sonic ions are reflected; the sheath requires
  $v_i \ge c_s$ at its edge.

## Related Concepts
- [Ion Acoustic Speed](sound-speed.md)
- [Debye Shielding](debye-shielding.md)
- [MHD](mhd.md)

## Quiz Questions

1. **Conceptual:** Why does a plasma “see” a solid surface as a prospectively
   negative plane?
2. **Computational:** Derive the Bohm criterion from Poisson’s equation for a
   planar, collisionless, isothermal sheath.
3. **MCQ:** The entrance velocity into a sheath must be:
   - A) $v_i < c_s$
   - B) $v_i = c_s$
   - C) $v_i > c_s$
   - D) $v_i = 0$

## Further Reading

- I. H. Hutchinson, *Principles of Plasma Diagnostics*, Chapter on probes.
