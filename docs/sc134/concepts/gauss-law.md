# Gauss's Law

*Source lecture(s):* [SC134 Lec4](../lectures.md)

## Intuition

The net electric flux through any closed surface equals enclosed charge divided by $\varepsilon_0$—the differential form of Coulomb.

## Formal Definition

$$\oint \vec{E}\cdot d\vec{A} = \frac{q_{\text{enc}}}{\varepsilon_0}$$

## Mathematical Formulation

Differential form: $\nabla\cdot\vec{E} = \rho/\varepsilon_0$
Infinite sheet: $E = \sigma/(2\varepsilon_0)$ each side.

## Derivation

Apply divergence theorem to Coulomb's law; integrate over a closed surface; spherical symmetry gives $E\cdot4\pi r^2 = q/\varepsilon_0$.

## Worked Example

Uniformly charged sphere: $E = (1/4\pi\varepsilon_0)Q/r^2$ outside, $E\propto r$ inside.

## Common Mistakes

- Using Gaussian surface with wrong symmetry.
- Forgetting $q_{\text{enc}}$ only counts enclosed charge.

## Related Concepts

- [Electric Field](electric-field.md)
- [Coulomb's Law](coulombs-law.md)
- [Electric Flux](electric-flux.md)

## Quiz

**Q1.** Does Gauss's law work for non-uniform fields?

??? success "Answer"
    Yes, it is always valid.
