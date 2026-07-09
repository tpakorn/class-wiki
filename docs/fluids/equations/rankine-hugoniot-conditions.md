# Rankine–Hugoniot Conditions

## Equations

Across a stationary normal shock (upstream 1 → downstream 2):

$$\text{mass:}\quad \rho_1 u_1 = \rho_2 u_2$$

$$\text{momentum:}\quad p_1 + \rho_1 u_1^2 = p_2 + \rho_2 u_2^2$$

$$\text{energy:}\quad h_1 + \tfrac12 u_1^2 = h_2 + \tfrac12 u_2^2,
\qquad h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$$

$$\text{tangential velocity:}\quad v_{t1} = v_{t2}$$

Solved in terms of the upstream Mach number $M_1 = u_1/c_1$, $c_1 = \sqrt{\gamma p_1/\rho_1}$:

$$\frac{\rho_2}{\rho_1} = \frac{(\gamma+1)M_1^2}{(\gamma-1)M_1^2 + 2}
\qquad
\frac{p_2}{p_1} = \frac{2\gamma M_1^2 - (\gamma-1)}{\gamma+1}$$

$$\frac{T_2}{T_1} = \frac{\left[2\gamma M_1^2 - (\gamma-1)\right]\left[(\gamma-1)M_1^2 + 2\right]}{(\gamma+1)^2 M_1^2}
\qquad
M_2^2 = \frac{M_1^2 + \frac{2}{\gamma-1}}{\frac{2\gamma}{\gamma-1}M_1^2 - 1}$$

## Physical meaning

A [shock](../concepts/shock-waves.md) is thin (∼ mean free path) but must still conserve
mass, momentum and energy. These jump conditions are the conservation laws applied to a
control volume straddling the front — the integral
[Reynolds transport theorem](../concepts/reynolds-transport-theorem.md) with the volume
squeezed to zero thickness. Given the upstream state, the downstream state is fully
determined.

## Variables

$\rho$ — density · $u$ — normal velocity (shock frame) · $p$ — pressure ·
$h$ — specific enthalpy · $T$ — temperature · $M$ — Mach number ·
$\gamma$ — specific-heat ratio.

## Assumptions

Steady in the shock frame · ideal gas with constant $\gamma$ · adiabatic (no external
heat) · normal shock (oblique shocks: apply to the normal component, tangential
velocity passes through unchanged).

## Limits

**Weak shock** ($M_1 \to 1$): expanding to first order gives
$\Delta p = c_s^2\,\Delta\rho$ — an adiabatic **sound wave**.

**Strong shock** ($M_1 \gg 1$):

$$\frac{\rho_2}{\rho_1} \to \frac{\gamma+1}{\gamma-1}\ \ (\text{finite!}), \qquad
\frac{p_2}{p_1} \approx \frac{2\gamma}{\gamma+1}M_1^2, \qquad
\frac{T_2}{T_1} \approx \frac{2\gamma(\gamma-1)}{(\gamma+1)^2}M_1^2$$

Density saturates (4× for monatomic, 6× for diatomic); pressure and temperature grow
without bound; downstream flow is subsonic.

## Entropy selects the direction

$$\Delta S = C_v \ln\left[\frac{p_2}{p_1}\left(\frac{\rho_1}{\rho_2}\right)^\gamma\right] \geq 0$$

Only compressive solutions ($\rho_2 > \rho_1$, $p_2 > p_1$, $T_2 > T_1$, $u_2 < u_1$)
satisfy the second law — "expansion shocks" are forbidden. Dissipation inside the front
converts bulk kinetic energy irreversibly into heat.

## Applications

Supersonic intakes and nozzles · re-entry heating ·
[blast waves](../examples/trinity-blast-wave.md) (strong-shock limit) · astrophysical
shocks · shock tubes.

## Related equations

- [Continuity](continuity-equation.md), [Euler](euler-equation.md) — the smooth-flow versions
- [Bernoulli](bernoulli-equation.md) — *fails* across the shock (entropy jump)

## Worked example

Air ($\gamma = 1.4$), $M_1 = 2$:
$\rho_2/\rho_1 = \frac{2.4\times4}{0.4\times4+2} = 2.67$,
$p_2/p_1 = \frac{11.2-0.4}{2.4} = 4.5$,
$T_2/T_1 = 4.5/2.67 = 1.69$, and $M_2 = 0.577$ — supersonic in, subsonic out.

## Quiz

**Q1 (computational).** For a very strong shock in monatomic gas ($\gamma = 5/3$), what
is the maximum density compression?

??? success "Answer"
    $(\gamma+1)/(\gamma-1) = \frac{8/3}{2/3} = 4$.

**Q2 (conceptual).** Why does the tangential velocity component pass through a shock
unchanged?

??? success "Answer"
    The shock is thin and inviscid on either side: no shear stress acts along the
    front, so there is no force to change tangential momentum, while the tangential
    mass flux is continuous.

**Q3 (multiple choice).** Downstream of a normal shock, the flow is always:

- (a) supersonic  (b) sonic  (c) subsonic  (d) reversed

??? success "Answer"
    **(c).** $M_2 < 1$ whenever $M_1 > 1$ — shocks are nature's way of decelerating
    supersonic flow.
