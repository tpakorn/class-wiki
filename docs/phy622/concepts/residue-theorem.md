# Residue Theorem

*Source lecture(s):* [PHY622 Lec4](../lectures.md)

## Intuition

A contour integral around isolated singularities picks up $2\pi i$ times the sum of residues—like Gauss's law for complex functions.

## Formal Definition

$$\oint_C f(z)\,dz = 2\pi i \sum_k \text{Res}(f, z_k)$$

## Mathematical Formulation

Simple pole: $\text{Res}(f,z_0)=\lim_{z\to z_0}(z-z_0)f(z)$.
Order-$m$ pole: $\text{Res}(f,z_0)=\frac{1}{(m-1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}[(z-z_0)^m f(z)]$.

## Derivation

Deform $C$ into small circles around each singularity. Each small circle contributes $2\pi i$ times the residue.

## Worked Example

$\oint \frac{1}{(z-1)(z-2)}\,dz$ around both poles gives $2\pi i(1+(-1))=0$.

## Common Mistakes

- Counting residues outside the contour.
- Forgetting $2\pi i$ factor.

## Related Concepts

- [Cauchy's Integral Formula](cauchy-integral-formula.md)
- [Contour Integration](contour-integration.md)

## Quiz

**Q1.** How many residues contribute if the contour encloses three poles?

??? success "Answer"
    Three.
