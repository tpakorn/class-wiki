# Finite Difference Method

## Intuition

Calculus defines a derivative as a limit; a computer never takes limits. The finite
difference method (FDM) simply *stops before the limit*: replace $df/dx$ with a
difference quotient on a grid, and a differential equation becomes ordinary algebra —
one equation per grid point. It is the plainest of all PDE discretizations, and the
foundation of both the course's [Poisson solvers](poisson-solvers.md) and the
[FDTD wave method](fdtd-method.md).

## The stencils

From Taylor expansion around $x_i$ (grid spacing $\Delta x$, $f_i = f(x_i)$):

**First derivative:**

$$\text{forward: } f_i' \approx \frac{f_{i+1} - f_i}{\Delta x} + \mathcal{O}(\Delta x)
\qquad
\text{backward: } f_i' \approx \frac{f_i - f_{i-1}}{\Delta x} + \mathcal{O}(\Delta x)$$

$$\text{central: } f_i' \approx \frac{f_{i+1} - f_{i-1}}{2\Delta x} + \mathcal{O}(\Delta x^2)$$

**Second derivative (central):**

$$\boxed{\,f_i'' \approx \frac{f_{i+1} - 2f_i + f_{i-1}}{\Delta x^2} + \mathcal{O}(\Delta x^2)\,}$$

Centering is the free lunch: symmetric stencils cancel the odd error terms, one order
of accuracy for nothing — the same insight that makes
[leapfrog](leapfrog-method.md) second-order in time.

## The 5-point Laplacian

Apply the second-derivative stencil in both $x$ and $y$ (with $\Delta x = \Delta y = h$):

$$\nabla^2\phi\big|_{i,j} \approx
\frac{\phi_{i+1,j} + \phi_{i-1,j} + \phi_{i,j+1} + \phi_{i,j-1} - 4\phi_{i,j}}{h^2}$$

Each point talks to its four nearest neighbors — the **5-point stencil**, the
workhorse of [Poisson solvers](poisson-solvers.md), the
[2-D wave equation](fdtd-method.md), and (transposed to matrices) the
[PIC field solve](pic-method.md).

## Taylor bookkeeping (why the orders are what they are)

$$f_{i\pm1} = f_i \pm \Delta x f_i' + \frac{\Delta x^2}{2}f_i'' \pm \frac{\Delta x^3}{6}f_i''' + \cdots$$

- Forward difference keeps the $+$ line only: leading error
  $\frac{\Delta x}{2}f''$ — first order.
- Central difference subtracts the two lines: $f''$ terms cancel, leaving
  $\frac{\Delta x^2}{6}f'''$ — second order.
- Adding the two lines isolates $f''$ with error $\frac{\Delta x^2}{12}f''''$ —
  the second-derivative stencil.

## Common mistakes

- **Using one-sided stencils in the interior.** They cost an order of accuracy;
  reserve them for boundaries.
- **Shrinking $h$ without limit.** The difference of nearly equal numbers loses
  precision; error has a round-off floor just like
  [time integration](convergence-and-error.md).
- **Forgetting stencils assume smoothness.** Across a discontinuity (a
  [shock](../../fluids/concepts/shock-waves.md), a material interface) Taylor's
  theorem — and your convergence order — evaporates.

## Related concepts

- [Poisson solvers](poisson-solvers.md) — FDM for elliptic problems
- [FDTD method](fdtd-method.md) — FDM marching in time
- [Discrete Poisson equation](../equations/discrete-poisson-equation.md)
- [Convergence and error](convergence-and-error.md) — same verification logic

## Knowledge graph position

**Prerequisites:** Taylor series; [ODE integration](ode-integration.md) mindset.
**Leads to:** [Poisson solvers](poisson-solvers.md), [FDTD](fdtd-method.md), [PIC](pic-method.md).

## Quiz

**Q1 (computational).** For $f(x) = \sin x$ at $x = 0$ with $\Delta x = 0.1$, compute
the forward and central difference estimates of $f'(0) = 1$.

??? success "Answer"
    Forward: $\sin(0.1)/0.1 = 0.9983$ (error $1.7\times10^{-3}$).
    Central: $[\sin(0.1) - \sin(-0.1)]/0.2 = 0.9983...$ — same here because
    $\sin$ is odd about 0; try $x_0 = 1$: forward error $\sim 4\times10^{-2}$,
    central $\sim 1.7\times10^{-3}$ — the order gap in action.

**Q2 (MCQ).** The 5-point stencil approximates the Laplacian with error:

- (a) $\mathcal{O}(h)$  (b) $\mathcal{O}(h^2)$  (c) $\mathcal{O}(h^4)$  (d) exact

??? success "Answer"
    **(b).** Central second differences in each direction are $\mathcal{O}(h^2)$.

**Q3 (conceptual).** Why does the central first-derivative stencil skip the point
$x_i$ itself?

??? success "Answer"
    Symmetry: $f_{i+1} - f_{i-1}$ automatically cancels all even-derivative terms,
    including $f_i$. The value at the center carries no slope information in a
    symmetric difference.
