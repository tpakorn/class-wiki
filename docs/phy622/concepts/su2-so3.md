# SU(2) and SO(3)

*Source lecture(s):* [PHY622 Lec11-12](../lectures.md)

## Intuition

SU(2) is the double cover of SO(3): two SU(2) matrices correspond to one SO(3) rotation. Spinors live in SU(2).

## Formal Definition

SU(2): $2\times2$ unitary matrices with det=1. SO(3): $3\times3$ orthogonal matrices with det=1.

## Mathematical Formulation

$$U=\exp\left(-i\frac{\vec{\theta}\cdot\vec{\sigma}}{2}\right)$$ where $\vec{\sigma}$ are Pauli matrices.
Mapping: double cover because $U$ and $-U$ give the same SO(3) rotation.

## Derivation

Parameterize SU(2) by Euler angles; compose two rotations. The kernel $\{I,-I\}$ shows SU(2) covers SO(3) twice.

## Worked Example

A $2\pi$ rotation in SO(3) corresponds to $-I$ in SU(2), not $I$.

## Common Mistakes

- Confusing SU(2) and SO(3) as the same group.
- Forgetting the global phase in SU(2).

## Related Concepts

- [Lie Groups](lie-groups.md)
- [Group Representations](group-representations.md)

## Quiz

**Q1.** How many preimages does one SO(3) rotation have in SU(2)?

??? success "Answer"
    Two.
