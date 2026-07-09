# Shock Waves

## Intuition

Sound waves are polite: small disturbances that pass through a gas without changing it.
But crank up the amplitude — a supersonic jet, an explosion — and the wave steepens
until fluid properties *jump* almost discontinuously across a layer only a few
molecular mean-free-paths thick. That jump is a **shock**. Behind the steepening is a
simple fact: compression waves travel faster through already-compressed (hotter) gas,
so the wave's crest overtakes its foot.

## Characteristics and Riemann invariants

Start from 1-D isentropic gas dynamics (Euler equations + $P\rho^{-\gamma}$ = const,
sound speed $c_s^2 = \gamma P/\rho$). The system reorganizes into two advection
equations:

$$\left[\frac{\partial}{\partial t} + (u \pm c_s)\frac{\partial}{\partial x}\right] C_\pm = 0,
\qquad C_\pm = u \pm \frac{2}{\gamma - 1}c_s$$

The quantities $C_\pm$ — the **Riemann invariants** — are constant along
**characteristics** $dx/dt = u \pm c_s$: the trajectories of sound-speed messengers
carried by the flow. Two consequences:

- Information at a point propagates only inside the wedge between its two
  characteristics (a causality cone, like light cones in relativity).
- When faster characteristics of the same family *catch up* with slower ones, they
  cross — a multivalued "solution" — and the physical resolution is a shock.

## A mechanical model: marbles in a tube

Marbles of diameter $D$, spaced $L > D$, roll at speed $V$ toward a closed end and pile
up. The stack (density $1/D$) grows into the incoming stream (density $1/L$) — a
"shock front" moving at

$$V_\text{sh} = -V\frac{D}{L - D}$$

In the shock frame, incoming flux equals outgoing flux:
$F_1 = n_1V_1 = F_2 = n_2V_2 = \frac{V}{L-D}$. Every feature of gas-dynamic shocks is
here: density jump, frame-dependent speeds, and conservation of flux across the front —
exactly the logic of the
[Rankine–Hugoniot conditions](../equations/rankine-hugoniot-conditions.md).

## Jump conditions (summary)

Across a normal shock with upstream Mach number $M_1 = u_1/c_1$:

$$\frac{\rho_2}{\rho_1} = \frac{(\gamma+1)M_1^2}{(\gamma-1)M_1^2 + 2}, \qquad
\frac{p_2}{p_1} = \frac{2\gamma M_1^2 - (\gamma-1)}{\gamma+1}$$

- **Weak shock** ($M_1 \to 1$): $\Delta p = c_s^2\,\Delta\rho$ — it degenerates into a
  sound wave.
- **Strong shock** ($M_1 \gg 1$): density saturates at
  $\frac{\rho_2}{\rho_1} \to \frac{\gamma+1}{\gamma-1}$ (= 4 for $\gamma = 5/3$; 6 for
  $\gamma = 7/5$), while pressure and temperature grow like $M_1^2$ without bound.

Full derivations on the [Rankine–Hugoniot page](../equations/rankine-hugoniot-conditions.md).

## Entropy: the arrow across the shock

The entropy jump

$$\Delta S = C_v \ln\!\left[\frac{P_2}{P_1}\left(\frac{\rho_1}{\rho_2}\right)^{\gamma}\right] \geq 0$$

is positive for compression shocks and would be negative for "expansion shocks" — which
is why the latter don't exist. The second law selects the physical solution:
$\rho_2 > \rho_1$, $P_2 > P_1$, $T_2 > T_1$, $u_2 < u_1$. Dissipation happens inside
the front, whose thickness is of order the mean free path $\ell_s \sim \lambda_\text{mfp}$
— the one place the [continuum hypothesis](what-is-a-fluid.md) is stretched to its
limit.

## Where shocks appear

Supersonic flight and re-entry · detonations · shock tubes ·
[blast waves](../examples/trinity-blast-wave.md) (Sedov–Taylor) · astrophysical shocks
(supernova remnants, accretion) · even hydraulic jumps in your kitchen sink (the
shallow-water analogue).

## Common mistakes

- **Applying [Bernoulli](bernoulli-principle.md) across a shock** — energy is conserved
  but entropy jumps; the isentropic relation fails.
- **Expecting unlimited density compression.** Density saturates at
  $(\gamma+1)/(\gamma-1)$; it's pressure and temperature that explode.
- **Thinking shocks are truly discontinuous.** They have finite (tiny) thickness where
  viscosity and heat conduction do the dissipating.

## Related concepts

- [Rankine–Hugoniot conditions](../equations/rankine-hugoniot-conditions.md) — the jump algebra
- [Trinity blast wave](../examples/trinity-blast-wave.md) — self-similar strong-shock solution
- [Reynolds transport theorem](reynolds-transport-theorem.md) — conservation bookkeeping used at the front
- [Dimensional analysis](dimensional-analysis.md) — Taylor's yield estimate

## Knowledge graph position

**Prerequisites:** [Bernoulli](bernoulli-principle.md), [Continuity](../equations/continuity-equation.md), [Euler's equation](../equations/euler-equation.md), thermodynamics of ideal gases.
**Leads to:** [Rankine–Hugoniot](../equations/rankine-hugoniot-conditions.md), [blast waves](../examples/trinity-blast-wave.md).

## Quiz

**Q1 (conceptual).** Why do compression waves steepen into shocks while expansion waves
spread out?

??? success "Answer"
    Local wave speed is $u + c_s$, and compression raises both $u$ and $c_s$ (hotter
    gas). Crests outrun troughs ⇒ steepening. In expansion the ordering reverses, so
    characteristics fan out — a smooth rarefaction.

**Q2 (computational).** Air ($\gamma = 1.4$) shock with $M_1 = 3$. Find the density and
pressure ratios.

??? success "Answer"
    $\rho_2/\rho_1 = \frac{2.4\times9}{0.4\times9+2} = \frac{21.6}{5.6} \approx 3.86$;
    $p_2/p_1 = \frac{2\times1.4\times9 - 0.4}{2.4} \approx 10.3$.

**Q3 (multiple choice).** Along a $C_+$ characteristic, which quantity is constant?

- (a) $u$  (b) $c_s$  (c) $u + \frac{2}{\gamma-1}c_s$  (d) entropy only

??? success "Answer"
    **(c).** The Riemann invariant. ($u$ and $c_s$ individually vary; entropy is
    constant along *particle paths* in smooth isentropic flow.)
