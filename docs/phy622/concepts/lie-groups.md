# Lie Groups

*Source lecture(s):* [PHY622 Lec10-11](../lectures.md)

## Intuition

Continuous groups whose elements are parameterized smoothly—like rotations forming SO(3).

## Formal Definition

A group that is also a smooth manifold, with multiplication and inversion smooth maps.

## Mathematical Formulation

Near identity: $g(\theta)\approx I + i\theta^a T_a + O(\theta^2)$. Generators $T_a$ satisfy $[T_a,T_b]=if_{abc}T_c$.

## Derivation

Take an infinitesimal parameter $\epsilon$; expand $g(\epsilon)=I+\epsilon X+O(\epsilon^2)$. The generator $X$ is the tangent vector at identity.

## Worked Example

SO(2) is the circle group $e^{i\theta}$; generator $J=i$ with $[J,J]=0$.

## Common Mistakes

- Forgetting that Lie brackets measure non-commutativity.
- Treating global and infinitesimal parameters interchangeably.

## Related Concepts

- [Symmetry Groups](symmetry-groups.md)
- [Group Representations](group-representations.md)
- [SU(2) and SO(3)](su2-so3.md)

## Quiz

**Q1.** What is the Lie algebra of a Lie group?

??? success "Answer"
    Tangent space at identity with bracket.
