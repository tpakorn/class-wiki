# Group Representations

*Source lecture(s):* [PHY622 Lec8-9](../lectures.md)

## Intuition

A representation realizes an abstract group as concrete matrices acting on a vector space.

## Formal Definition

A representation $D(g)$ is a homomorphism $G\to GL(V)$ preserving multiplication: $D(g_1g_2)=D(g_1)D(g_2)$.

## Mathematical Formulation

Character: $\chi(g)=\text{Tr}[D(g)]$. Orthogonality: $\sum_g \chi^{(r)}(g)\chi^{(s)}(g)^* = |G|\delta_{rs}$.

## Derivation

Choose a basis for $V$; each group element becomes a matrix. Irreducible representations cannot be block-diagonalized further.

## Worked Example

The Pauli matrices realize an SU(2) spin-1/2 representation.

## Common Mistakes

- Confusing reducible and irreducible representations.
- Using characters of different dimensions in orthogonality.

## Related Concepts

- [Symmetry Groups](symmetry-groups.md)
- [Lie Groups](lie-groups.md)
- [SU(2) and SO(3)](su2-so3.md)

## Quiz

**Q1.** What does irreducible mean?

??? success "Answer"
    No nontrivial invariant subspace.
