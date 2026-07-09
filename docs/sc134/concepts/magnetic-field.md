# Magnetic Field and Forces

*Source lecture(s):* [SC134 Lec9-10](../lectures.md)

## Intuition

Moving charges feel magnetic forces; currents create magnetic fields that curl around them.

## Formal Definition

Lorentz force: $\vec{F} = q\vec{v}\times\vec{B}$
Force on current element: $d\vec{F} = i\,d\vec{l}\times\vec{B}$

## Mathematical Formulation

Biot-Savart: $$d\vec{B} = \frac{\mu_0}{4\pi}\frac{i\,d\vec{l}\times\hat{r}}{r^2}$$
Ampere: $$\oint \vec{B}\cdot d\vec{l} = \mu_0 i_{\text{enc}}$$

## Derivation

Biot-Savart integrates current-element contributions; Ampere's law follows from symmetry of $\vec{B}$ around steady currents.

## Worked Example

Straight infinite wire: $B = \mu_0 i/(2\pi r)$.

## Common Mistakes

- Using Coulomb-like $1/r^2$ without cross product for Biot-Savart.
- Forgetting $\mu_0$ vs $1/(4\pi\varepsilon_0)$.

## Related Concepts

- [Biot-Savart Law](biot-savart-law.md)
- [Ampere's Law](amperes-law.md)
- [Magnetic Force](magnetic-force.md)

## Quiz

**Q1.** What direction is force on a positive charge moving right in a field into the page?

??? success "Answer"
    Upward ($+\hat{j}$).
