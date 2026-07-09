# The CFL (Courant) Condition

## Equation

For explicit wave-propagation schemes on a grid ([FDTD](../concepts/fdtd-method.md)):

$$\boxed{\,\Delta t \leq \frac{\Delta x}{c\sqrt{d}}\,}$$

$d$ = number of spatial dimensions (1, 2, 3); $c$ = the fastest signal speed in the
system.

## Physical meaning

**Causality on the grid.** In one time step, the numerical scheme moves information at
most one cell ($\Delta x$); physics moves it $c\,\Delta t$. If physics outruns the
stencil ($c\Delta t > \Delta x/\sqrt d$), the numerical domain of dependence cannot
contain the true one — the scheme is being asked to predict without the needed
information, and errors amplify explosively. Named for Courant, Friedrichs & Lewy
(1928) — a stability law older than the computer.

## Variables

$\Delta t$ — time step · $\Delta x$ — grid spacing · $c$ — wave/signal speed ·
$\sqrt d$ — the diagonal factor (waves can travel diagonally across cells).

## Consequences

- **Cost scaling:** refining space by 2 forces refining time by 2 → cost
  $\times 2^{d+1}$ in $d$ dimensions.
- **Fast, irrelevant waves still bind you.** If light waves live in your model but you
  care about slow plasma waves, explicit stepping still requires resolving $c$ — a
  key motivation for implicit and reduced models.
- Practical safety margin: the course uses $\Delta t = \Delta x/2c$ (1-D) and
  $\Delta t = \frac{\sqrt2}{2}\Delta x/c$ (2-D).

## Assumptions / scope

Applies to *explicit hyperbolic* (wave-type) schemes. Diffusion equations have their
own, harsher constraint ($\Delta t \lesssim \Delta x^2/2\kappa$);
[implicit methods](../concepts/backward-euler.md) trade the constraint for a linear
solve; the ODE analogue is the stability limit of
[forward Euler](../concepts/forward-euler.md).

## Related equations

- [FDTD updates](../concepts/fdtd-method.md) — the scheme it protects
- [Discrete Poisson equation](discrete-poisson-equation.md) — elliptic problems have no CFL (no time)

## Quiz

**Q1 (computational).** 1-D FDTD with $\Delta x = 1$ mm: what is the largest stable
$\Delta t$ for light?

??? success "Answer"
    $\Delta t \leq \Delta x/c = 10^{-3}/3\times10^8 \approx 3.3$ ps.

**Q2 (conceptual).** Violating CFL doesn't add a little error — the run *explodes*
within tens of steps. Why so violent?

??? success "Answer"
    Instability is multiplicative: the offending Fourier modes are amplified by a
    factor $|g| > 1$ *every step*, so errors grow like $|g|^n$ — exponential blow-up,
    usually fastest at the grid's shortest wavelength (checkerboard noise).

**Q3 (MCQ).** In 3-D, the CFL limit relative to 1-D (same $\Delta x$, $c$) is:

- (a) the same  (b) $\sqrt3$ smaller  (c) 3× smaller  (d) 3× larger

??? success "Answer"
    **(b).** $\Delta t \leq \Delta x/(c\sqrt3)$ — diagonal propagation across the cell
    sets the pace.
