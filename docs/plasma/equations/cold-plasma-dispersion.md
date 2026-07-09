# Cold Plasma Dispersion Tensor

$$\mathbf{n}\times(\mathbf{n}\times\mathbf{E}) + \mathbf{K}\cdot\mathbf{E} = 0$$

*Source lecture:* pc368_lec13_magnetized_wave

## Physical Meaning

The cold-plasma wave equation describes electromagnetic wave propagation in a
magnetized, collisionless plasma. The refractive index tensor $\mathbf{K}$
determines cutoff, resonance, and mode polarization.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\mathbf{n} = c\mathbf{k}/\omega$ | Refractive-index vector | dimless |
| $\mathbf{K}$ | Dielectric (Stix) tensor | dimless |
| $S, D, P$ | Stix parameters | dimless |
| $\omega_{ps}, \Omega_{cs}$ | Species plasma/cyclotron frequencies | rad s$^{-1}$ |

## Assumptions

- Uniform $\mathbf{B}_0$.
- Cold fluid species (finite temperature adds kinetic corrections).
- Linear waves.

## Derivation

Linearize the cold-fluid momentum equation for each species, include Lorentz
force, and couple to Maxwell’s equations. The susceptibility tensor is:

$$\chi_{ij} = -\sum_s \frac{\omega_{ps}^2}{\omega^2} \Bigl[ \mathbf{I} + \frac{\omega}{\Omega_{cs}}\mathbf{M} + \Bigl(\frac{\omega}{\Omega_{cs}}\Bigr)^2 \mathbf{b}\mathbf{b} \Bigr]$$

where $\mathbf{M}$ encodes the magnetization. In their standard form this yields
the $S, D, P$ tensor.

## Applications

- **RF heating:** Ion cyclotron range of frequencies (ICRF).
- **Ionospheric propagation:** HF radio windows and cuts.
- **ECRH:** Electron cyclotron resonance heating.

## Connections to Other Equations

- [Magnetized Waves](../concepts/magnetized-waves.md): The physical modes.
- [Plasma Frequency](../equations/plasma-frequency.md): Enters $P$ and $S$.
- [Alfvén Speed](../equations/alfven-velocity.md): Related to $\Omega_{ci}$.
