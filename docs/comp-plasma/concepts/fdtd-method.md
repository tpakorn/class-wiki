# The FDTD Method

## Intuition

Maxwell's two curl equations are a perfect duet: a changing $\mathbf{E}$ makes
$\mathbf{B}$, a changing $\mathbf{B}$ makes $\mathbf{E}$. Kane Yee's 1966 insight:
*let the computer play the duet literally* — store E and H at **interleaved** points
in space and time, and update them alternately. The result, Finite-Difference
Time-Domain, is the [leapfrog method](leapfrog-method.md) reborn as a field solver,
and still a dominant tool in computational electromagnetics.

## The update scheme

From Faraday's and Ampère's laws, leapfrogged:

$$\mathbf{H}^{n+1/2} = \mathbf{H}^{n-1/2} - \frac{\Delta t}{\mu}\,\nabla\times\mathbf{E}^{n}$$

$$\mathbf{E}^{n+1} = \mathbf{E}^{n} + \frac{\Delta t}{\varepsilon}\,\nabla\times\mathbf{H}^{n+1/2}$$

In 1-D (fields $E_z$, $H_y$, propagation along $x$), with central differences on a
**staggered grid** ($E_z$ at integer points, $H_y$ at half-integer points):

$$H_y^{n+1/2}(i) = H_y^{n-1/2}(i) + \frac{c\Delta t}{\Delta x}\left(E_z^n(i{+}1) - E_z^n(i)\right)$$

$$E_z^{n+1}(i) = E_z^n(i) + \frac{c\Delta t}{\Delta x}\left(H_y^{n+1/2}(i) - H_y^{n+1/2}(i{-}1)\right)$$

Every derivative is *centered* — in space by staggering, in time by leapfrogging —
so the scheme is second-order in both, with the conservation-friendly character of
all [symplectic-style updates](leapfrog-method.md).

```python
for n in range(1, num_steps+1):
    hy[:-1] += (c*dt/dx)*(ez[1:] - ez[:-1])
    ez[source] += np.exp(-((n-30)*dt/tau)**2) * np.sin(2*np.pi*f*n*dt)
    ez[1:]  += (c*dt/dx)*(hy[1:] - hy[:-1])
```

## Stability: the CFL condition

Information moves at most one cell per step on the grid, but light moves $c\Delta t$.
Stability demands the numerical domain of dependence contain the physical one:

$$\boxed{\,\Delta t \leq \frac{\Delta x}{c\sqrt{d}}\,}$$

($d$ = spatial dimension). Violate it and the solution explodes within a few steps —
see the [CFL equation page](../equations/cfl-condition.md).

## The 2-D wave equation & double slit

The same machinery drives the scalar wave equation
$\partial_t^2 U = c^2\nabla^2 U$:

$$U^{n+1}_{i,j} = 2U^n_{i,j} - U^{n-1}_{i,j}
+ \frac{c^2\Delta t^2}{\Delta x^2}\,\text{Lap}^n_{i,j}$$

with the [5-point Laplacian](finite-difference-method.md) and a boolean **mask** for
walls and obstacles. Poke two slits in a barrier, drive one wall sinusoidally, and the
grid produces a textbook interference pattern — the
[double-slit worked example](../examples/double-slit-fdtd.md), diffraction physics from
four lines of NumPy.

## What to explore

- Phase relation of $E_z$ and $H_y$ → Poynting flux direction
- Boundary reflections → motivation for absorbing boundary conditions (PML)
- Frequency ≫ grid resolution → numerical dispersion artifacts
- Two sources → interference; material interfaces ($\varepsilon$ change) → refraction

## Common mistakes

- **Collocating E and H.** The staggering *is* the second-order accuracy; putting both
  on the same points quietly degrades the scheme.
- **Choosing $\Delta t$ and $\Delta x$ independently.** They're chained by CFL; halve
  $\Delta x$ and you must (at least) halve $\Delta t$ — cost scales like
  $N^{d+1}$.
- **Under-resolving the wavelength.** Rule of thumb: ≥ 10–20 cells per wavelength, or
  numerical dispersion distorts propagation.

## Related concepts

- [Leapfrog method](leapfrog-method.md) — the temporal ancestor
- [Finite difference method](finite-difference-method.md) — the spatial toolkit
- [CFL condition](../equations/cfl-condition.md)
- [Double-slit example](../examples/double-slit-fdtd.md)

## Knowledge graph position

**Prerequisites:** [Finite differences](finite-difference-method.md), [Leapfrog](leapfrog-method.md), Maxwell's equations.
**Leads to:** computational electromagnetics, antenna/waveguide simulation, [PIC](pic-method.md) (electromagnetic variants).

## Quiz

**Q1 (computational).** A 2-D FDTD grid has $\Delta x = 1$ cm and $c = 3\times10^8$
m/s. Maximum stable $\Delta t$?

??? success "Answer"
    $\Delta t \leq \Delta x/(c\sqrt2) = 0.01/(4.24\times10^8) \approx 23.6$ ps.

**Q2 (conceptual).** Why are $E$ and $H$ stored at different *times* ($n$ vs
$n+1/2$)?

??? success "Answer"
    Each update needs the *time-centered* derivative of the other field: updating $E$
    from $n$ to $n{+}1$ uses $H$ at $n{+}1/2$ — exactly midway — making the time
    difference central and the scheme second-order, precisely the
    [leapfrog](leapfrog-method.md) trick.

**Q3 (MCQ).** Doubling spatial resolution in a 3-D FDTD simulation multiplies total
cost by about:

- (a) 2  (b) 4  (c) 8  (d) 16

??? success "Answer"
    **(d).** $2^3$ more cells × 2 more time steps (CFL) = 16.
