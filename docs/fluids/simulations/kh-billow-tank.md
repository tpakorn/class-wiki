# Proposal · Kelvin–Helmholtz Billow Tank

## Learning goal

Make the [KH dispersion relation](../equations/interface-dispersion-relation.md)
*visible*: students should discover that (1) more shear ⇒ faster growth, (2) short
waves grow fastest without surface tension, (3) stable stratification + tension create
an onset threshold — the 6.6 m/s wind-over-water number.

## Widget type

2-D animated interface simulation (slider-driven parameter sweep + animation).

## Inputs

- $\Delta U$ — velocity jump (slider, 0–15 m/s)
- $\rho_1/\rho_2$ — density ratio (slider)
- $\gamma$ — surface tension on/off (toggle)
- $k$ — seeded wavenumber (slider), or "natural" mode = fastest-growing

## Outputs

- Animated interface $h(x,t) = h_0 e^{\operatorname{Re}(s)t}\cos(kx + \operatorname{Im}(s)t)$
  with billow-like shading once amplitude passes a threshold
- Live plot of growth rate $\operatorname{Re}(s)$ vs $k$ with the current operating
  point marked; stability boundary highlighted

## Educational value

The dispersion relation is a wall of algebra; a slider that crosses the stability
boundary and *makes waves appear* converts it into intuition. Directly supports
[Kelvin–Helmholtz](../concepts/kelvin-helmholtz-instability.md) and
[Rayleigh–Taylor](../concepts/rayleigh-taylor-instability.md) (set $\Delta U = 0$,
invert densities).

## Implementation notes

- Pure HTML/JS canvas, no libraries; evaluate $s(k)$ from the closed-form relation
- Linear-phase animation only (exponential clamp + arctan saturation for visual
  roll-up flavor); label clearly where linear theory ends
- ~200 lines; embed via `<iframe src="../assets/kh-tank.html">` on the concept page
