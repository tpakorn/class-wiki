# Conformal Mapping

*Source lecture(s):* [PHY622 Lec4](../lectures.md)

## Intuition

An analytic function with non-zero derivative warps the plane while preserving angles—turning hard domains into easy ones.

## Formal Definition

A mapping $w=f(z)$ is conformal if it preserves angles between intersecting curves.

## Mathematical Formulation

Conformal iff $f'(z)\neq0$ everywhere. Example: $w=z^2$ maps the upper half-plane to the plane with a branch cut.

## Derivation

Near $z_0$, $f(z)\approx f(z_0)+f'(z_0)(z-z_0)$. Multiplying by $f'(z_0)$ rotates and scales but preserves angles.

## Worked Example

The Joukowski map $w=z+1/z$ transforms a circle to an airfoil shape.

## Common Mistakes

- Forgetting that conformality fails where $f'(z)=0$.
- Applying to non-analytic transformations.

## Related Concepts

- [Analytic Functions](analytic-functions.md)
- [Complex Numbers and Functions](complex-numbers.md)

## Quiz

**Q1.** What breaks conformality?

??? success "Answer"
    Points where $f'(z)=0$.
