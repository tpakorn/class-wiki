# Fourier Series

*Source lecture(s):* [PHY621 Lec3](../lectures.md)

## Intuition

Any periodic waveform decomposes into sine and cosine waves at integer multiples of a fundamental frequency.

## Formal Definition

For $f(x)$ period $2L$: $f(x)=\frac{a_0}{2}+\sum_{n=1}^\infty[a_n\cos(n\pi x/L)+b_n\sin(n\pi x/L)]$.

## Mathematical Formulation

$$a_n=\frac{1}{L}\int_{-L}^L f(x)\cos\frac{n\pi x}{L}\,dx$$
$$b_n=\frac{1}{L}\int_{-L}^L f(x)\sin\frac{n\pi x}{L}\,dx$$

## Derivation

Use orthogonality: $\int_{-L}^L \cos(m\pi x/L)\cos(n\pi x/L)\,dx=L\delta_{mn}$ for $m,n>0$.

## Worked Example

Square wave on $[-L,L]$ has only odd sine coefficients.

## Common Mistakes

- Using sine series for even functions.
- Forgetting $a_0/2$ normalization.

## Related Concepts

- [Fourier Transform](fourier-transform.md)
- [Laplace Transform](laplace-transform.md)

## Quiz

**Q1.** What is the Fourier basis for even functions on $[-L,L]$?

??? success "Answer"
    Cosine terms only.
