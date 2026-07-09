# Sound Speed

*Source lecture(s):* [pc368_lec09_wave1, pc368_lec10_wave2, pc368_lec11_streaming_ins](../lectures.md)

## Intuition

Sound speed in a plasma is the characteristic speed at which pressure
perturbations propagate through the ion fluid. It sets the scale for ion
acoustic waves and appears in Mach-number criteria like the Bohm criterion.

## Formal Definition

$$c_s = \\sqrt{\\frac{\\gamma_e k_B T_e + \\gamma_i k_B T_i}{m_i}}$$

For cold ions and isothermal electrons ($T_i \\ll T_e$, $\\gamma_e = 1$):

$$c_s \\approx \\sqrt{\\frac{k_B T_e}{m_i}}$$

## Mathematical Formulation

From the two-fluid ion momentum equation with electron pressure gradient:

$$m_i \\frac{\\partial \\mathbf{u}_i}{\\partial t} = -\\frac{\\nabla p_e}{n_i}$$

Linearizing $p_e = n_e k_B T_e$ and using Boltzmann response yields the
acoustic wave equation with speed $c_s$.

## Derivation

1. Start with ion continuity and momentum.
2. Use Boltzmann electrons: $n_e = n_0 \\exp(e\\phi/k_B T_e)$.
3. For small $\\phi$: $n_{e1} = (e\\phi/k_B T_e) n_0$.
4. Insert into Poisson and eliminate $\\phi$ to get wave equation.
5. The natural frequency is $\\omega = k c_s$.

## Worked Example

For $T_e = 10$ eV in hydrogen:
- $c_s \\approx \\sqrt{1.6\\times 10^{-18}\\,\\text{J} / 1.67\\times 10^{-27}\\,\\text{kg}}
  \\approx 3.1\\times 10^4\\,\\text{m/s}$.

## Common Mistakes

- Using $T_i$ instead of $T_e$. Electron pressure dominates the restoring force.
- Forgetting the $\\gamma$ factors in the general definition.

## Related Concepts

- [Ion Acoustic Wave](ion-acoustic-wave.md)
- [Plasma Sheath](plasma-sheath.md)
- [Plasma Waves](plasma-waves.md)

## Quiz Questions

1. How does $c_s$ change if $T_e$ doubles?
2. Why is $c_s$ called “sound speed” in plasma?

## Further Reading

- F. F. Chen, *Introduction to Plasma Physics and Controlled Fusion*.
