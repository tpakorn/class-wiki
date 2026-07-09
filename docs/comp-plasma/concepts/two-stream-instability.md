# Two-Stream Instability

## Intuition

Fire two electron beams through each other and the arrangement looks steady — equal
and opposite currents, uniform density. But it is a plasma pencil balanced on its
point: any tiny density ripple creates an electric field that bunches the beams
further, which strengthens the field... Exponential growth, spectacular phase-space
vortices, and finally a thermalized mess. It is *the* classic demonstration that
plasmas are never boring, and the standard first test of every
[PIC code](pic-method.md).

## The setup

- 1-D periodic domain, length $L$; uniform neutralizing ion background $n_0$
- Electrons split into two counter-propagating beams at $\pm v_b$ with thermal spread
- Equations of motion (normalized): $\dot r_i = v_i$, $\dot v_i = -E(r_i)$
- Seed perturbation: $v \to v\left[1 + A\sin(2\pi x/L)\right]$

Course parameters: 40 000 particles, 400 cells, $L = 50$, $v_b = 3$, $A = 0.1$.

## What unfolds (watch phase space!)

| Phase | Phase-space picture |
|---|---|
| **Early** | two flat horizontal bands at $v = \pm v_b$ |
| **Linear growth** | bands ripple; ripples grow exponentially |
| **Saturation** | bands roll up into "cat's-eye" **phase-space vortices** — particles trapped in their own wave |
| **Late** | vortices merge, phase space mixes toward a broad hot distribution |

The phase-space plot $(x_i, v_i)$ is the diagnostic; density or field snapshots miss
the drama.

## Measuring the growth rate

Linear theory predicts the field energy grows as
$\mathcal{E}(t) = \sum_j E_j^2\,\Delta x \propto e^{2\gamma t}$:

1. record $\mathcal{E}(t)$ every step,
2. plot $\ln \mathcal{E}$ vs $t$,
3. fit the straight (linear-phase) segment — slope $= 2\gamma$.

Compare with the kinetic-theory growth rate from the
[PC368 streaming-instability analysis](../../plasma/concepts/streaming-instability.md);
agreement of a $10^4$-particle simulation with a pencil-and-paper dispersion relation
is the course's capstone moment. Then explore: how does $\gamma$ vary with $v_b$, with
particle count, with perturbation amplitude?

## Why it matters

Beam–plasma systems are everywhere: electron beams in the solar wind, accelerator
beams, fast ignition fusion, even (in its Buneman variant) current-driven turbulence.
And the *methodology* — seed, grow, measure $\gamma$, compare with linear theory —
is the template for every instability study in computational physics, including the
[fluid ones](../../fluids/concepts/hydrodynamic-stability.md).

## Common mistakes

- **Fitting the growth rate too late** — after saturation the slope is gone; fit only
  the clean exponential segment.
- **Blaming noise for early "growth".** With few particles the noise floor is high;
  the true signal must emerge well above $\mathcal{E}_\text{noise}$ before fitting.
- **Expecting energy conservation to fail.** Field energy grows at the expense of
  beam kinetic energy; *total* energy stays constant (check it!).

## Related concepts

- [PIC method](pic-method.md) — the machinery
- [Streaming instability (PC368)](../../plasma/concepts/streaming-instability.md) — the theory
- [Landau damping (PC368)](../../plasma/concepts/landau-damping.md) — the same wave–particle physics, reversed
- [Hydrodynamic stability (PC316)](../../fluids/concepts/hydrodynamic-stability.md) — the same seed-grow-measure logic in fluids

## Knowledge graph position

**Prerequisites:** [PIC method](pic-method.md).
**Leads to:** kinetic plasma simulation, instability analysis at large.

## Quiz

**Q1 (conceptual).** Why do the phase-space vortices stop the exponential growth?

??? success "Answer"
    Particles become *trapped* in the wave's potential wells and oscillate within
    them instead of feeding the wave coherently — the linear "resonant pump" saturates
    once the trapping (bounce) frequency rivals the growth rate.

**Q2 (computational).** $\ln\mathcal{E}$ rises from −8 to −2 between $t = 10$ and
$t = 25$. Growth rate $\gamma$?

??? success "Answer"
    Slope $= 6/15 = 0.4 = 2\gamma \Rightarrow \gamma = 0.2$ (normalized units).

**Q3 (MCQ).** The instability's free-energy source is:

- (a) the ion background  (b) the beams' relative drift kinetic energy
- (c) the seed perturbation  (d) numerical error

??? success "Answer"
    **(b).** The counter-streaming drift is the reservoir; the instability is
    nature's mechanism for dissipating it into field energy and heat.
