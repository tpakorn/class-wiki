# Sweet–Parker Model

*Source lecture(s):* [pc368_lec17_sweetparker](../lectures.md)

## Intuition

In the Sweet–Parker picture, reconnection takes place in a long, thin current
sheet. Plasma from far upstream is squeezed into the sheet, diffuses across
resistively, and shoots out the other side. The sheet length $L$ is macroscopic,
but its thickness $\delta$ is microscopic ($\delta \ll L$). The result is a
very slow reconnection rate unless the Lundquist number is modest.

## Formal Definition

The **Sweet–Parker model** gives the steady-state reconnection rate in a
long, thin resistive current sheet:

$$V_{\text{rec}} = V_{\text{in}} \sim \eta \frac{L}{\delta} \sim \frac{v_A}{\sqrt{S}}$$

where $S = \mu_0 v_A L / \eta$ is the Lundquist number.

## Mathematical Formulation

From the four sheets (inflow, transition, outflow, current):

1. **Mass conservation:** $U_{\text{in}} L = U_{\text{out}} \delta$
2. **Transition balance:** $U_{\text{in}} B_{\text{in}} \sim \eta B_{\text{in}} / (\mu_0 \delta)$
3. **Induction in sheet:** $\partial \psi / \partial t + U\cdot\nabla\psi = \eta/\mu_0 \nabla^2\psi$

Combining (1) and (2):

$$\frac{U_{\text{out}}}{U_{\text{in}}} = \frac{L}{\delta}, \qquad U_{\text{in}} \sim \frac{\eta}{\mu_0 \delta}$$

With $v_A = B_{\text{in}}/\sqrt{\mu_0 \rho}$, the reconnection rate is:

$$M_A = \frac{U_{\text{in}}}{v_A} \sim \frac{1}{\sqrt{S}}, \qquad S = \frac{\mu_0 v_A L}{\eta}$$

## Derivation

1. Inflow region: ideal Ohm’s law $\mathbf{E} + \mathbf{U}_{\text{in}}\times\mathbf{B} = 0$.
   At the separatrices, $\mathbf{E}_{\text{rec}} = -U_{\text{in}} B_{\text{in}}$.
2. Inside sheet: resistive Ohm’s law $\eta \mathbf{J} = \mathbf{E} + \mathbf{U}_{\text{out}}\times\mathbf{B}$.
   With $\mathbf{U}_{\text{out}} \approx 0$ in the sheet, $E_{\parallel} = \eta J_{\parallel}$.
3. Transition layer: match $|\mathbf{U}\times\mathbf{B}| \sim |\eta\mathbf{J}|$.
4. Using Ampère’s law $J \sim B_{\text{in}}/(\mu_0\delta)$ gives sheet thickness.
5. Mass conservation ties $U_{\text{in}}$ and $U_{\text{out}}$.
6. Eliminate $\delta$ to express rate purely in terms of $S$.

## Worked Example

> **Solar corona reconnection:** For $L = 10^7$ m, $v_A = 10^6$ m/s,
> $\eta = 1$ m$^2$/s, compute $S$ and $U_{\text{in}}$.
> $S = \mu_0 v_A L / \eta \sim 10^{13}$. Then $M_A = S^{-1/2} \sim 10^{-6.5}$.
> $U_{\text{in}} \sim 10$ cm/s. This is far slower than observed reconnection
> rates, motivating Petschek fast-mode or collisionless diffusion models.

## Common Mistakes

- **Sweet–Parker is always slow.** It is only slow when $S \gg 1$; for $S \sim 10^2$
  the rate is already substantial.
- **Applying it to collisionless plasmas.** The original model assumes resistive
> MHD; kinetic effects are needed for magnetospheric reconnection.
- **Assuming steady state.** Unsteady plasmoid instability tears the sheet into
> many small islands, enhancing the rate.

## Related Concepts

- [Magnetic Reconnection](magnetic-reconnection.md)
- [MHD Instability](mhd-instability.md)
- [Alfvén Speed](../equations/alfven-velocity.md)

## Quiz Questions

1. **Conceptual:** Why does a longer current sheet reconnect more slowly in the
   Sweet–Parker regime?
2. **Computational:** Show that plasmoid instability grows when $S > S_c \sim 10^4$.
3. **MCQ:** The Lundquist number compares:
   - A) Inertia to pressure
   - B) Advection to diffusion
   - C) Hall term to resistivity
   - D) Gravity to Lorentz force

## Further Reading

- P. A. Sweet, * Nuggets of Plasma Astrophysics*.
