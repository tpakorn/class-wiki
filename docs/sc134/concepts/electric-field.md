# Electric Field

*Source lecture(s):* [SC134 Lec2-3](../lectures.md)

## Intuition

A charge creates a field around it; other charges feel forces through that field without touching.

## Formal Definition

$$\vec{E} = \frac{\vec{F}}{q_0}$$ for a test charge $q_0\to0$.

## Mathematical Formulation

Point charge: $$\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{r}$$
Continuous distribution: $$\vec{E} = \int \frac{1}{4\pi\varepsilon_0}\frac{dq}{r^2}\hat{r}$$

## Derivation

Measure force per unit test charge; superposition allows summation/integration over distributions.

## Worked Example

Two equal charges at $x=\pm a$: on the $y$-axis, $E_x$ cancels, leaving $E_y = (1/4\pi\varepsilon_0)2qy/(a^2+y^2)^{3/2}$.

## Common Mistakes

- Using $E = kq/r$ instead of $kq/r^2$.
- Forgetting vector direction from source to field point.

## Related Concepts

- [Coulomb's Law](coulombs-law.md)
- [Electric Force on Charges](electric-force.md)
- [Electric Potential](electric-potential.md)

## Quiz

**Q1.** What is the unit of electric field?

??? success "Answer"
    N/C or V/m.
