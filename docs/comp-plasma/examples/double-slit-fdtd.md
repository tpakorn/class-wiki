# Example · Double-Slit Diffraction by FDTD

## Problem statement

Solve the 2-D scalar wave equation on a $256\times256$ grid containing a barrier with
two slits; drive a sinusoidal wave from one wall and observe the interference pattern.

## Given information

- Wave equation: $\partial_t^2 U = c^2\nabla^2 U$, $c = 1$, unit box
- Update rule ([FDTD](../concepts/fdtd-method.md)):
  $U^{n+1}_{i,j} = 2U^n_{i,j} - U^{n-1}_{i,j} + \frac{c^2\Delta t^2}{\Delta x^2}\text{Lap}^n_{i,j}$
- [CFL](../equations/cfl-condition.md): $\Delta t = \frac{\sqrt2}{2}\Delta x/c$
- A boolean **mask** marks walls and the barrier ($U = 0$ there); two gaps in the
  barrier are the slits

## Solution strategy

1. Build the mask: outer walls + a barrier row, then carve two slit openings.
2. Keep two time levels ($U$, $U_\text{prev}$); compute the
   [5-point Laplacian](../concepts/finite-difference-method.md) with `np.roll`.
3. Each step: update → zero the masked cells → drive the source wall
   $U(0, :) = \sin\omega t$ → rotate time levels.

```python
lap = (np.roll(U,1,0) + np.roll(U,-1,0)
     + np.roll(U,1,1) + np.roll(U,-1,1) - 4*U)
Unew = 2*U - Uprev + fac*lap
Unew[mask] = 0
Unew[0,:] = np.sin(omega*t)
```

## Expected results

Beyond the barrier, the two slit-waves overlap into alternating bright/dark fringes —
constructive where path lengths differ by $m\lambda$, destructive at
$(m + \frac12)\lambda$. Experiments to run:

- **Wavelength vs slit width:** $\lambda \sim$ slit → strong diffraction;
  $\lambda \ll$ slit → sharp geometric shadows
- **Slit separation** sets fringe spacing ($\Delta y \approx \lambda D/d$)
- One slit closed → single-slit envelope

## Key takeaways

- No optics was programmed — interference *emerges* from the discretized wave
  equation. Huygens' principle is a theorem of the PDE, not an extra assumption.
- The same code structure (mask + stencil + march) handles waveguides, cavities, and
  scattering obstacles: change the mask, not the method.
- Hard walls reflect — visible artifacts motivate absorbing boundaries (PML) in
  serious electromagnetic work.

## Related

[FDTD method](../concepts/fdtd-method.md) ·
[CFL condition](../equations/cfl-condition.md) ·
[Finite differences](../concepts/finite-difference-method.md)
