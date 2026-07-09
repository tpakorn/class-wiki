# Capacitance

*Source lecture(s):* [SC134 Lec6](../lectures.md)

## Intuition

A capacitor stores charge by separating opposite charges onto two isolated conductors.

## Formal Definition

$$C = \frac{Q}{\Delta V}$$

## Mathematical Formulation

Parallel plate: $C = \varepsilon_0 A/d$
Series: $1/C_{\text{eq}} = \sum 1/C_i$
Parallel: $C_{\text{eq}} = \sum C_i$
Energy: $U = \frac{1}{2}CV^2 = \frac{Q^2}{2C}$

## Derivation

Integrate $dW = V\,dq$ to assemble charge from $0$ to $Q$.

## Worked Example

$10\,\mu\text{F}$ capacitor at 12 V stores $U = 0.5\times10\mu\text{F}\times144 = 720\,\mu\text{J}$.

## Common Mistakes

- Assuming $C$ depends on $Q$ or $V$ (it is geometry/material only).
- Forgetting factor $1/2$ in energy.

## Related Concepts

- [Electric Potential](electric-potential.md)
- [Dielectrics](dielectrics.md)
- [RC Circuits](rc-circuits.md)

## Quiz

**Q1.** Does capacitance depend on charge?

??? success "Answer"
    No—depends only on geometry and dielectric.
