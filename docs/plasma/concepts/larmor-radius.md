# Larmor Radius

*Source lecture(s):* [pc368_lec07_drift](../lectures.md)

## Intuition

The Larmor radius is the radius of the circular motion a charged particle makes
when it gyrates around a magnetic field line. It measures how tightly a
particle is bound to the field.

## Formal Definition

$$\\rho_s = \\frac{m_s v_{\\perp}}{|q_s| B}$$

where $v_{\\perp}$ is the velocity component perpendicular to $\\mathbf{B}$.

## Mathematical Formulation

For a thermal species with $v_{\\perp} \\sim v_{th} = \\sqrt{2 k_B T_s/m_s}$:

$$\\rho_{th} = \\frac{\\sqrt{2 m_s k_B T_s}}{|q_s| B}$$

## Derivation

Lorentz force provides centripetal acceleration:

$$|q| v_\\perp B = \\frac{m v_\\perp^2}{\\rho} \\quad \\Rightarrow \\quad \\rho = \\frac{m v_\\perp}{|q| B}$$

## Worked Example

For a 1-keV proton in $B = 3$ T:
- $v_\\perp \\approx \\sqrt{2\\times 1.6\\times 10^{-16}\\,\\text{J} / 1.67\\times 10^{-27}\\,\\text{kg}}
  \\approx 4.4\\times 10^5\\,\\text{m/s}$
- $\\rho \\approx (1.67\\times 10^{-27} \\times 4.4\\times 10^5) / (1.6\\times 10^{-19} \\times 3)
  \\approx 1.5\\times 10^{-3}\\,\\text{m}$

## Common Mistakes

- Using parallel velocity instead of perpendicular velocity.
- Forgetting the $\\sqrt{2}$ factor when converting from temperature to thermal speed.

## Related Concepts

- [Drift Motion](drift-motion.md)
- [Adiabatic Invariant](adiabatic-invariant.md)
- [Magnetic Mirror](magnetic-mirror.md)

## Quiz Questions

1. If $B$ doubles, what happens to $\\rho$?
2. Why do electrons gyrate faster than ions?

## Further Reading

- F. F. Chen, *Introduction to Plasma Physics and Controlled Fusion*.
