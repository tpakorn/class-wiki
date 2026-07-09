# The Energy Cascade & Kolmogorov Scaling

## Intuition

Stir a cup of coffee once. You created one big swirl — and stopped adding energy. Yet
moments later the coffee is full of small eddies, and moments after that it is still,
slightly warmer. The energy *cascaded*: big whirls broke into little whirls
(Richardson's rhyme), passing energy down scale after scale until eddies became so
small that [viscosity](viscosity.md) could finally grind them into heat.

## The three ranges

1. **Energy injection** at the integral scale $L$ — the size of the biggest eddies,
   set by geometry/forcing (obstacle size, stirring). Most kinetic energy lives here.
2. **Inertial range** ($L \gg \ell \gg \eta$) — energy flows down-scale at a constant
   rate $\varepsilon$ (per unit mass), with negligible dissipation: pure nonlinear
   hand-me-down.
3. **Dissipation** at the **Kolmogorov microscale** $\eta$, where the local Reynolds
   number reaches order 1 and viscosity converts the flux to heat.

## Kolmogorov microscales (1941)

Assume the smallest scales know only $\nu$ [m²/s] and $\varepsilon$ [m²/s³].
[Dimensional analysis](dimensional-analysis.md) then fixes everything:

$$\eta = \left(\frac{\nu^3}{\varepsilon}\right)^{1/4}, \qquad
u_\eta = (\nu\varepsilon)^{1/4}, \qquad
\tau_\eta = \left(\frac{\nu}{\varepsilon}\right)^{1/2}$$

Sanity check: $Re_\eta = u_\eta\,\eta/\nu = 1$ — the definition of "where viscosity
takes over" is built in.

## The −5/3 spectrum

In the inertial range, the energy spectrum $E(k)$ (energy per unit wavenumber,
$[E] = \text{m}^3/\text{s}^2$) can depend only on $\varepsilon$ and $k$:

$$E(k) \propto \varepsilon^{a} k^{b}:\quad
\frac{m^3}{s^2} = \left(\frac{m^2}{s^3}\right)^a (m^{-1})^b
\;\Rightarrow\; a = \tfrac{2}{3},\; b = -\tfrac{5}{3}$$

$$\boxed{\,E(k) \sim \varepsilon^{2/3} k^{-5/3}\,}$$

This "K41" law is among the most-verified results in fluid mechanics — tidal channels,
wind tunnels, jets and atmospheric data collapse onto the same $-5/3$ slope.

**K41's assumptions:** at high $Re$, small scales are (1) statistically isotropic,
(2) universal — dependent only on $\varepsilon$ and $\nu$, and (3) in the inertial
range, independent even of $\nu$ (self-similar energy transfer).

## Scale separation in practice

$$\frac{L}{\eta} \sim Re^{3/4}$$

An atmospheric flow with $L \sim 1$ km and $Re \sim 10^8$ has $\eta$ under a
millimetre — five decades of active scales. That $Re^{3/4}$ (per direction; $Re^{9/4}$
in 3-D) is exactly why direct simulation of high-$Re$ [turbulence](turbulence.md) is
infeasible and [modeling](reynolds-averaging.md) is unavoidable.

## Common mistakes

- **Thinking dissipation happens at large scales.** Big eddies are essentially
  inviscid; only at $\eta$ does friction act. (Corollary: the dissipation *rate* is set
  by the large scales — $\varepsilon \sim U^3/L$ — since they control the supply.)
- **Applying $-5/3$ outside the inertial range** or in 2-D flows (which cascade
  *backwards* in energy — a beautiful, separate story).
- **Treating $\varepsilon$ as adjustable.** In steady state it is fixed by injection:
  what goes in must come out.

## Related concepts

- [Turbulence](turbulence.md) — the phenomenon
- [Dimensional analysis](dimensional-analysis.md) — the method that yields everything here
- [Viscosity](viscosity.md) — the terminal sink
- [Reynolds averaging](reynolds-averaging.md) — statistical machinery

## Knowledge graph position

**Prerequisites:** [Turbulence](turbulence.md), [Dimensional analysis](dimensional-analysis.md).
**Leads to:** turbulence modeling, spectral analysis of flows.

## Quiz

**Q1 (computational).** In a wind tunnel, $\varepsilon \approx 1\ \text{m}^2/\text{s}^3$
and $\nu = 1.5\times10^{-5}\ \text{m}^2/\text{s}$. Find $\eta$ and $\tau_\eta$.

??? success "Answer"
    $\eta = (\nu^3/\varepsilon)^{1/4} = (3.4\times10^{-15})^{1/4} \approx 0.24$ mm;
    $\tau_\eta = \sqrt{\nu/\varepsilon} \approx 3.9$ ms.

**Q2 (conceptual).** Why does the inertial-range spectrum *not* depend on viscosity?

??? success "Answer"
    In that range eddies pass energy on much faster than viscosity can act
    ($\ell \gg \eta$), so $\nu$ is dynamically irrelevant; only the throughput
    $\varepsilon$ and the scale $k$ remain — and dimensions then force $-5/3$.

**Q3 (multiple choice).** If you double the stirring power in a steady turbulent tank
(doubling $\varepsilon$), the Kolmogorov length:

- (a) doubles  (b) halves  (c) shrinks by $2^{1/4}$  (d) is unchanged

??? success "Answer"
    **(c).** $\eta \propto \varepsilon^{-1/4}$: more power pushes dissipation to
    slightly smaller scales.
