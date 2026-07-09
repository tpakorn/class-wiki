# Sweet–Parker Reconnection Rate

$$M_A = \frac{U_{\text{in}}}{v_A} \sim \frac{1}{\sqrt{S}}$$

*Source lecture(s):* [pc368_lec17_sweetparker](../lectures.md)

## Physical Meaning

The Sweet–Parker rate gives the fraction of the Alfvén speed at which magnetic
flux is reconnected in a long, thin resistive current sheet. It quantifies how
efficiently magnetic energy is converted to plasma energy in the MHD paradigm.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $U_{\text{in}}$ | Inflow velocity | m s$^{-1}$ |
| $v_A$ | Alfvén speed | m s$^{-1}$ |
| $S$ | Lundquist number | dimless |

## Assumptions

- Steady-state 2D resistive MHD.
- Long, thin sheet ($L \gg \delta$).
- Uniform resistivity $\eta$.
- Incompressible flow.

## Derivation

Combine:

1. **Transition balance:** $U_{\text{in}} B = \eta B / (\mu_0 \delta) \Rightarrow U_{\text{in}} \sim \eta/(\mu_0 \delta)$.
2. **Mass conservation:** $U_{\text{in}} L = U_{\text{out}} \delta$.
3. **Energy / outflow continuity:** $U_{\text{out}} \sim v_A$.
4. Eliminate $\delta$: $\delta = \eta L/(\mu_0 U_{\text{in}} v_A)$.
5. From $U_{\text{in}} = U_{\text{out}} \delta/L$, substitute and solve for $U_{\text{in}}$.
6. Result: $U_{\text{in}} \sim v_A S^{-1/2}$.

## Applications

- **Solar corona:** Motivated the search for faster reconnection mechanisms.
- **Laboratory plasma:** Scaling of flux consumption in RFP and tokamak sawteeth.
- **Geospace:** Magnetospheric substorm current sheets.

## Connections to Other Equations

- [Lundquist Number](../equations/lundquist-number.md): Defines $S$.
- [Alfvén Speed](../equations/alfven-velocity.md): Normalization.
- [Magnetic Reconnection](../concepts/magnetic-reconnection.md): General concept.
- [Sweet–Parker Model](../concepts/sweet-parker-model.md): Full derivation and picture.
