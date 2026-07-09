# Fourier Transform

*Source lecture(s):* [PHY621 Lec3](../lectures.md)

## Intuition

When a function is not periodic, the Fourier series becomes an integral with continuous frequencies.

## Formal Definition

$$\hat{f}(k)=\int_{-\infty}^\infty f(x)\,e^{-ikx}\,dx$$
$$f(x)=\frac{1}{2\pi}\int_{-\infty}^\infty \hat{f}(k)\,e^{ikx}\,dk$$

## Mathematical Formulation

$$\hat{f}(k)=\int_{-\infty}^\infty f(x)\,e^{-ikx}\,dx$$
$$f(x)=\frac{1}{2\pi}\int_{-\infty}^\infty \hat{f}(k)\,e^{ikx}\,dk$$

## Derivation

Let discrete spacing $\Delta k=\pi/L\to dk/2\pi$ as $L\to\infty$; the sum becomes an integral.

## Worked Example

The Gaussian $f(x)=e^{-x^2/2}$ transforms to $\hat{f}(k)=\sqrt{2\pi}\,e^{-k^2/2}$.

## Common Mistakes

- Mixing up $1/2\pi$ placement in forward vs inverse transform.
- Confusing $e^{-ikx}$ vs $e^{ikx}$ sign convention.

## Related Concepts

- [Fourier Series](fourier-series.md)
- [Laplace Transform](laplace-transform.md)
- [Convolution](convolution.md)

## Quiz

**Q1.** What does the uncertainty principle say in Fourier language?

??? success "Answer"
    A function and its transform cannot both be arbitrarily localized.
