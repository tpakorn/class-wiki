# Laplace Transform

*Source lecture(s):* [PHY621 Lec4](../lectures.md)

## Intuition

Turn differential equations into algebra by trading derivatives for multiplication by $s$.

## Formal Definition

$$\mathcal{L}\{f(t)\}=\hat{f}(s)=\int_0^\infty f(t)\,e^{-st}\,dt$$

## Mathematical Formulation

First derivative: $\mathcal{L}\{f'\}=s\hat{f}-f(0)$
Second derivative: $\mathcal{L}\{f''\}=s^2\hat{f}-sf(0)-f'(0)$

## Derivation

Integrate by parts: $\int_0^\infty f'(t)e^{-st}\,dt = [-f(t)e^{-st}]_0^\infty + s\int_0^\infty f(t)e^{-st}\,dt$.

## Worked Example

For $f(t)=e^{at}$, $\hat{f}(s)=\frac{1}{s-a}$.

## Common Mistakes

- Ignoring initial conditions when transforming derivatives.
- Confusing bilateral vs unilateral transforms.

## Related Concepts

- [Fourier Series](fourier-series.md)
- [Convolution](convolution.md)

## Quiz

**Q1.** What is the Laplace transform of a step function?

??? success "Answer"
    $1/s$.
