# Green's Functions

*Source lecture(s):* [PHY621 Lec7](../lectures.md)

## Intuition

A Green's function is the impulse response of a linear operator. Build any solution by superposition.

## Formal Definition

For $L u=f$, $G(x;x_0)$ satisfies $L G=\delta(x-x_0)$.

## Mathematical Formulation

$$u(x)=\int G(x;x_0)\,f(x_0)\,dx_0$$

## Derivation

Expand $f$ and $G$ in eigenfunctions $\phi_n$ of $L$: $G=\sum \phi_n(x)\phi_n^*(x_0)/\lambda_n$.

## Worked Example

For $y''=-f(x)$ with $y(0)=y(L)=0$, $G(x;x_0)=\frac{1}{L}\min(x,x_0)(L-\max(x,x_0))$.

## Common Mistakes

- Ignoring boundary conditions when constructing $G$.
- Forgetting symmetry for self-adjoint operators.

## Related Concepts

- [Partial Differential Equations](partial-differential-equations.md)
- [Ordinary Differential Equations](ordinary-differential-equations.md)

## Quiz

**Q1.** Does Green's function apply to nonlinear ODEs?

??? success "Answer"
    No—only linear operators.
