# Hamilton's Principle

*Source lecture(s):* [PHY622 Lec2](../lectures.md)

## Intuition

Physics chooses the path that makes the action stationary, not the path of greatest or least anything.

## Formal Definition

The action $S=\int_{t_0}^{t_1} L(q,\dot{q},t)\,dt$ is stationary for the true trajectory.

## Mathematical Formulation

$$\delta S = \delta\int_{t_0}^{t_1} L(q,\dot{q},t)\,dt = 0$$

## Derivation

Apply Euler-Lagrange to the Lagrangian $L=T-V$. The resulting equations are Newton's second law in generalized coordinates.

## Worked Example

For a simple harmonic oscillator, $L=\frac{1}{2}m\dot{x}^2-\frac{1}{2}kx^2$, giving $m\ddot{x}+kx=0$.

## Common Mistakes

- Thinking 'stationary' means 'minimum'—saddles exist.
- Applying to dissipative systems without modification.

## Related Concepts

- [Calculus of Variations](calculus-of-variations.md)
- [Euler-Lagrange Equation](euler-lagrange-equation.md)

## Quiz

**Q1.** Is Hamilton's principle valid for dissipative forces?

??? success "Answer"
    No, without adding Rayleigh's dissipation function.
