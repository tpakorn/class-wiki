# Proposal · Two-Stream Phase-Space Viewer

## Learning goal

Make the [two-stream instability](../concepts/two-stream-instability.md)'s phase-space
story tangible: beams → ripples → exponential growth → cat's-eye vortices →
thermalization, with the growth rate measured live.

## Widget type

In-browser 1-D [PIC](../concepts/pic-method.md) mini-simulation (animation + plots).

## Inputs

- Beam velocity $v_b$ (slider) · thermal spread (slider)
- Perturbation amplitude (slider) · particle count (2k–20k)
- Play / pause / reset; speed control

## Outputs

- Animated $(x, v)$ scatter (canvas, alpha-blended points)
- Side panel: $\ln\mathcal{E}(t)$ field-energy trace with a draggable fit-window
  showing the measured growth rate $2\gamma$
- Live energy-conservation readout (field + kinetic)

## Educational value

Growth rates and saturation are abstractions until you watch the vortices form. The
live $\gamma$-fit teaches the actual research workflow: identify the linear phase,
fit, compare with theory ([PC368 streaming instability](../../plasma/concepts/streaming-instability.md)).

## Implementation notes

- Pure JS: typed arrays; CIC deposit via manual binning; tridiagonal periodic Poisson
  solve via cyclic Thomas algorithm (O(M)); leapfrog push
- 5k particles × 200 cells runs at 60 fps comfortably; ~300 lines
- Reuse the CSS variable theming from `assets/integrator-arena.html`
