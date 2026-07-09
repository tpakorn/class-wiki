# Electric Potential

*Source lecture(s):* [SC134 Lec5](../lectures.md)

## Intuition

Potential is the potential-energy cost per unit charge—a scalar that is often easier to compute than the vector field.

## Formal Definition

$$V = \frac{U}{q}$$
From field: $$\Delta V = -\int \vec{E}\cdot d\vec{s}$$

## Mathematical Formulation

Point charge: $V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$
Group: $V = \sum \frac{1}{4\pi\varepsilon_0}\frac{q_i}{r_i}$
Continuous: $V = \int \frac{1}{4\pi\varepsilon_0}\frac{dq}{r}$

## Derivation

Work to bring $q_0$ from infinity to $P$ against conservative force; divide by $q_0$.

## Worked Example

Dipole on axis at distance $r\gg d$: $V\approx(1/4\pi\varepsilon_0)p/r^2$.

## Common Mistakes

- Sign errors when going from $E$ to $V$ (remember $-$).
- Forgetting reference at infinity.

## Related Concepts

- [Electric Field](electric-field.md)
- [Electric Dipole](electric-dipole.md)
- [Equipotential Surfaces](equipotential.md)

## Quiz

**Q1.** What are the units of potential?

??? success "Answer"
    Volts (J/C).

**Q2.** Is potential a scalar or vector?

??? success "Answer"
    Scalar.
