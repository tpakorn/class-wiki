# Magnetic Islands

*Source lecture(s):* [pc368_lec16_reconnection](../lectures.md)

## Intuition

Magnetic islands form when reconnecting magnetic field lines create closed loops
of flux. They are the “beaded” droplets in the water-beading analogy: the plasma
minimizes magnetic energy by breaking a long thin current sheet into discrete
islands.

## Formal Definition

A **magnetic island** is a region of closed magnetic flux bounded by separatrices
$\\psi = \\text{const}$ in a reconnecting current sheet. The island width $w$
is measured by the $x$-distance between the separatrices.

## Mathematical Formulation

In the Sweet–Parker or Petschek picture, the island grows according to

$$\\frac{dw}{dt} \\sim \\Delta' v_A$$

where $\\Delta'$ is the stability parameter of the tearing mode and $v_A$ is
the Alfvén speed.

## Derivation

1. Start from a Harris sheet with $\\psi(x)$ having an inflection point.
2. Linearize the tearing-mode eigenvalue problem in resistive MHD.
3. The inner region gives the matching condition $\\Delta' \\gamma \\sim \\eta$.
4. Nonlinear evolution widens the island at the rate above.

## Worked Example

For a tokamak sawtooth crash with $B = 3$ T, $\\rho_{\\text{pol}} = 1$ m, and
$\\eta = 10^{-6}\\,\\text{m}^2$/s, the growth time is $\\tau \\sim
\\mu_0 \\sigma \\rho_{\\text{pol}}^2 \\sim 0.1$–$1$ s.

## Common Mistakes

- Equating islands with “bad” physics. They are natural, energetically favorable
  states.
- Ignoring the separatrix. The topology inside and outside the island is
  fundamentally different.

## Related Concepts

- [Magnetic Reconnection](magnetic-reconnection.md)
- [Sweet–Parker Model](sweet-parker-model.md)
- [MHD Instability](mhd-instability.md)

## Quiz Questions

1. Why does beading into islands lower the magnetic energy?
2. What determines whether a tearing mode grows or is stable?

## Further Reading

- P. A. Sweet, * Nuggets of Plasma Astrophysics*.
