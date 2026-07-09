# Proposal · Energy-Cascade Sandbox

## Learning goal

Internalize the [K41 picture](../concepts/energy-cascade.md): injection scale,
inertial range with $-5/3$ slope, dissipation cutoff at the Kolmogorov scale — and how
the range *widens* as $Re^{3/4}$.

## Widget type

Interactive log–log spectrum plot with parameter sliders + eddy cartoon.

## Inputs

- $Re$ — Reynolds number (log slider, $10^2$–$10^8$)
- $\varepsilon$ — dissipation rate (slider)
- Toggle: overlay experimental spectra (tidal channel, jet, atmosphere — digitized
  reference curves)

## Outputs

- Model spectrum $E(k)$ with labeled integral scale $1/L$, inertial $-5/3$ segment,
  and dissipation roll-off at $1/\eta$; $\eta$, $u_\eta$, $\tau_\eta$ readouts
- Side panel: cartoon of eddies splitting (Richardson rhyme), sized to the current
  scale separation $L/\eta = Re^{3/4}$
- Grid-point counter $N \sim Re^{9/4}$ — why DNS of an airliner is impossible

## Educational value

Students see *why* the $-5/3$ law is dimensional necessity and how scale separation
explodes with $Re$ — the single most exam-relevant fact of the
[turbulence](../concepts/turbulence.md) chapter.

## Implementation notes

- Canvas or inline SVG; spectrum = piecewise model
  (von Kármán low-$k$ + $-5/3$ + exponential cutoff)
- ~150 lines JS; no dependencies; dark/light aware via CSS variables
