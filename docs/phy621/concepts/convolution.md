# Convolution

*Source lecture(s):* [PHY621 Lec3-4](../lectures.md)

## Intuition

Convolution in one domain is simple multiplication in the other—why Fourier/Laplace methods simplify linear systems.

## Formal Definition

$$(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau$$

## Mathematical Formulation

$$\mathcal{F}\{f*g\}=\hat{f}\cdot\hat{g}$$
$$\mathcal{F}\{f\cdot g\}=\hat{f}*\hat{g}$$

## Derivation

Insert the Fourier representation of $g$ into the convolution integral and exchange order of integration.

## Worked Example

Convolving two Gaussians yields another Gaussian with variance equal to the sum of variances.

## Common Mistakes

- Dropping integration limits when switching domains.
- Confusing correlation with convolution.

## Related Concepts

- [Fourier Transform](fourier-transform.md)
- [Laplace Transform](laplace-transform.md)

## Quiz

**Q1.** What operation in frequency space corresponds to time-domain convolution?

??? success "Answer"
    Multiplication.
