# Biot-Savart Law

*Source lecture(s):* [SC134 Lec9-10](../lectures.md)

## Intuition

Every tiny current element paints a little contribution to the magnetic field, just like Coulomb's law for charge.

## Formal Definition

$$d\vec{B} = \frac{\mu_0}{4\pi}\frac{i\,d\vec{l}\times\hat{r}}{r^2}$$

## Mathematical Formulation

Integration over wire replaces $i\,d\vec{l}$ with $J\,d\vec{A}$ for volume currents.

## Derivation

Empirical law from Oersted and Biot-Savart experiments; superposition yields integral form.

## Worked Example

Center of circular loop radius $R$: $B = \mu_0 i/(2R)$.

## Common Mistakes

- Omitting $\times\hat{r}$ cross product.
- Integrating without projecting angle correctly.

## Related Concepts

- [Magnetic Field and Forces](magnetic-field.md)
- [Ampere's Law](amperes-law.md)

## Quiz

**Q1.** What symmetry makes Biot-Savart easiest?

??? success "Answer"
    Circular or straight segments.
