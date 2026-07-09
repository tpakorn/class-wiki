# Potential-Flow Builder

## Learning goal

Feel **superposition** in your hands: because
[Laplace's equation](../equations/laplace-equation.md) is linear, elementary flows add.
Uniform stream + doublet *is* a cylinder; add a vortex and stagnation points migrate —
the origin of lift.

<iframe src="../../assets/potential-flow.html" width="100%" height="640"
        style="border:none;" title="Potential flow builder"></iframe>

## Things to try

1. **Cylinder preset** — find the two stagnation points. Why do streamlines never
   enter the disk?
2. **Lifting cylinder** — increase $\Gamma$ and watch the stagnation points slide
   around the body and (at large $\Gamma$) merge and detach. The asymmetry of
   streamline spacing above/below *is* the lift
   ([Bernoulli](../concepts/bernoulli-principle.md): tighter lines = faster = lower
   pressure).
3. **Source + stream** — the dividing streamline is the Rankine half-body; everything
   inside it comes from the source.
4. **Source–sink pair** — a closed Rankine oval: the potential-flow ancestor of every
   streamlined body.

## The mathematics on display

$$\phi = Ux + \frac{Q}{2\pi}\ln r + \frac{K}{r}\cos\theta - \frac{\Gamma}{2\pi}\theta$$

Streamlines are traced by integrating $\mathbf{v} = \nabla\phi$ with a midpoint
(RK2) scheme — the same
[numerical-integration machinery](../../comp-plasma/concepts/runge-kutta-methods.md)
studied in PHY653. Color encodes speed.

## Related

[Potential flow](../concepts/potential-flow.md) ·
[Conformal mapping](../concepts/conformal-mapping-and-images.md) ·
[Laplace's equation](../equations/laplace-equation.md)
