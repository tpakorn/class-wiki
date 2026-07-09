# Cauchy's Theorem

*Source lecture(s):* [PHY622 Lec4](../lectures.md)

## Intuition

Integrating an analytic function around a closed loop gives zero—the integral depends only on endpoints.

## Formal Definition

$$\oint_C f(z)\,dz = 0$$ when $f$ is analytic on and inside $C$.

## Mathematical Formulation

Proof via deformation to a point: split into elementary rectangles; opposite sides cancel because $f_z$ is continuous.

## Derivation

Divide $C$ into $N$ small loops. By continuity, opposite contributions of adjacent small loops cancel, leaving only the outer loop integral.

## Worked Example

$\oint_{|z|=1} \frac{1}{z}\,dz = 2\pi i$, but here $1/z$ has a pole at 0, so Cauchy's theorem does NOT apply.

## Common Mistakes

- Applying to functions with singularities inside the contour.
- Forgetting that the domain must be simply connected.

## Related Concepts

- [Analytic Functions](analytic-functions.md)
- [Cauchy's Integral Formula](cauchy-integral-formula.md)

## Quiz

**Q1.** Does Cauchy's theorem apply if $f$ has a pole inside $C$?

??? success "Answer"
    No.
