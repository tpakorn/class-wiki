# Conformal Map Explorer

## Learning goal

*See* what [analyticity](../concepts/analytic-functions.md) does to the plane: an
analytic map bends the coordinate grid, but wherever $f'(z) \neq 0$ the red and blue
grid lines still cross at **exactly 90°** — angle preservation is
[conformality](../concepts/conformal-mapping.md), and it is the geometric face of the
[Cauchy–Riemann equations](../concepts/cauchy-riemann.md).

<iframe src="../../assets/conformal.html" width="100%" height="560"
        style="border:none;" title="Conformal map explorer"></iframe>

## Things to try

1. **$w = z^2$** — hover along the real axis toward the origin: angles *double* at
   $z = 0$, the one point where $f' = 0$.
2. **$w = e^z$** — the Cartesian grid becomes a polar grid: horizontal lines → rays,
   vertical lines → circles. This is why $e^z$ solves strip-shaped boundary-value
   problems.
3. **Joukowski $w = z + 1/z$** — the map behind
   [airfoil theory](../../fluids/concepts/conformal-mapping-and-images.md); watch the
   region near $z = \pm 1$ fold into sharp edges.
4. **Möbius $(z-1)/(z+1)$** — the right half-plane becomes the unit disk; circles map
   to circles, always.

## Related

[Conformal mapping](../concepts/conformal-mapping.md) ·
[Analytic functions](../concepts/analytic-functions.md) ·
[Potential-flow application (PC316)](../../fluids/concepts/conformal-mapping-and-images.md)
