# Example · The Trinity Blast Wave (Sedov–Taylor)

## Problem statement

A point explosion releases energy $E$ into a uniform atmosphere of density $\rho_0$.
Find how the blast-wave radius $R$ grows with time — and use a declassified photograph
to estimate the yield of the 1945 Trinity test, as G. I. Taylor famously did.

## Given information

- Instantaneous point release of energy $E$; ambient density $\rho_0$
- Strong-shock regime: ambient pressure negligible compared to post-shock pressure

## Solution strategy

Route 1 — pure [dimensional analysis](../concepts/dimensional-analysis.md).
Route 2 — physical energy accounting with
[strong-shock jump conditions](../equations/rankine-hugoniot-conditions.md), yielding
the same scaling with its structure exposed.

## Route 1 · Dimensional analysis

Only $E\,[ML^2T^{-2}]$, $t\,[T]$, $\rho_0\,[ML^{-3}]$ can matter. The unique
combination with dimensions of length:

$$R \sim \left(\frac{E t^2}{\rho_0}\right)^{1/5}$$

## Route 2 · Energy accounting

1. Swept-up mass: $M(t) = \frac{4\pi}{3}\rho_0 R^3$.
2. Post-shock pressure (strong shock): $p_2 = \frac{2}{\gamma+1}\rho_0 \dot R^2$.
3. Total (kinetic + thermal) energy of the shell:
   $$E = C_s\, M(t)\,\dot R^2, \qquad C_s = \frac{\gamma^2 + 3}{2(\gamma^2 - 1)}$$
4. $E$ constant ⇒ $M\dot R^2 = \text{const}$ ⇒ $R^{3/2}\dot R = \text{const}$
5. Power law $R \sim t^\alpha$: $R^{3/2}\cdot R/t = \text{const} \Rightarrow R^{5/2} \propto t$:

$$\boxed{\,R \sim E^{1/5}\rho_0^{-1/5}\, t^{2/5}\,}$$

## Final answer — Taylor's estimate

From the published Trinity photo at $t = 25$ ms, $R \approx 140$ m,
$\rho_0 = 1.2\ \text{kg/m}^3$:

$$E \sim \frac{\rho_0 R^5}{t^2} = \frac{1.2 \times (140)^5}{(0.025)^2}
\approx 10^{14}\ \text{J} \approx 25\ \text{kt TNT}$$

The classified official yield was ~21 kt. One photograph, one exponent, embarrassingly
close — the security establishment was not amused.

## Key takeaways

- Self-similarity: with no intrinsic length scale, the blast has the *same shape at
  every moment*, just rescaled — the hallmark of scale-free dynamics.
- The same $t^{2/5}$ law governs supernova remnants in their adiabatic
  (Sedov) phase — 20 orders of magnitude away in energy.
- $R \propto E^{1/5}$: yield estimates from blast radius are extremely robust
  (a factor 10 in energy moves $R$ by only 1.6×) — and conversely, blast damage radius
  scales weakly with warhead size.

## Related

[Dimensional analysis](../concepts/dimensional-analysis.md) ·
[Shock waves](../concepts/shock-waves.md) ·
[Rankine–Hugoniot conditions](../equations/rankine-hugoniot-conditions.md)
