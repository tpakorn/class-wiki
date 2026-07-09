# Magnetized Waves

*Source lecture(s):* [pc368_lec13_magnetized_wave](../lectures.md)

## Intuition

A magnetic field acts like a plasma prism: it splits electromagnetic waves into
different modes depending on their polarization relative to **B**. Some can pass
(whistlers, O-mode), others are reflected at sharp cutoff densities (X-mode, R-mode).
This is central to radio communications, ionospheric propagation, and
electromagnetic wave heating in fusion devices.

## Formal Definition

**Magnetized waves** are electromagnetic or electrostatic modes in a plasma
subject to a background magnetic field $\mathbf{B}_0$. Their polarization and
dispersion are described by the cold-plasma dielectric tensor $\mathbf{K}$.

## Mathematical Formulation

The wave equation in a cold, uniform magnetized plasma is:

$$\mathbf{n}\times(\mathbf{n}\times\mathbf{E}) + \mathbf{K}\cdot\mathbf{E} = 0$$

where $\mathbf{n} = c\mathbf{k}/\omega$ is the refractive index and

$$\mathbf{K} = \begin{pmatrix}
S & -iD & 0 \\
iD & S & 0 \\
0 & 0 & P
\end{pmatrix}$$

with Stix parameters $S = 1 - \sum_s \frac{\omega_{ps}^2}{\omega^2 - \Omega_{cs}^2}$, $D = \sum_s \frac{\Omega_{cs}/|\Omega_{cs}|\,\omega_{ps}^2}{\omega^2 - \Omega_{cs}^2}$, $P = 1 - \sum_s \frac{\omega_{ps}^2}{\omega^2}$.

## Derivation

1. Linearize Vlasov–Maxwell for a uniform magnetized plasma.
2. Assume exp$(ik_{\parallel}z - i\omega t)$ with $\mathbf{B}_0 = B_0 \hat{z}$.
3. Solve the linearized Lorentz force and Ampère’s law to obtain the dielectric
   tensor $K_{ij}(\omega, \mathbf{k})$.
4. Insert into the wave equation. Because of anisotropy, **E**, **B**, and **k**
   are not necessarily parallel.
5. Separate into ordinary (O) and extraordinary (X) polarizations.

## Worked Example

> **R-mode cutoff:** The right-hand cutoff occurs where $S + D = 0$, i.e.
> $\omega = \omega_{R}$ such that the index $n^2 \to \infty$.
> For $\mathbf{B}_0$ along $+\hat{z}$, the R-mode sees a resonance at
> $\omega = \Omega_{ce}/2 + \sqrt{\Omega_{ce}^2/4 + \omega_{pe}^2}$.

## Common Mistakes

- **B-field parity doesn’t matter.** The R and L modes depend strongly on the
  sign of $\mathbf{B}_0$.
- **All modes propagate everywhere.** Cutoffs and resonances block propagation
  in specific frequency-density windows.
- **Cold plasma is all you need.** Finite temperature introduces Bernstein modes
  and kinetic Alfvén waves.

## Related Concepts

- [Plasma Waves](plasma-waves.md)
- [Alfvén Speed](../equations/alfven-velocity.md)
- [MHD Equilibrium](mhd-equilibrium.md)

## Quiz Questions

1. **Conceptual:** Which mode can reach the Earth’s surface after a solar flare?
   O-mode, X-mode, R-mode, or L-mode?
2. **Computational:** Show that the lower hybrid frequency is
   $\omega_{lh} = \sqrt{\Omega_{ci}^2 + \omega_{pi}^2}$.
3. **MCQ:** The O-mode (ordinary wave) has its electric field polarized:
   - A) Parallel to $\mathbf{k}$
   - B) Perpendicular to $\mathbf{k}$ and $\mathbf{B}_0$
   - C) Perpendicular to $\mathbf{k}$ but with a component along $\mathbf{B}_0$
   - D) Along $\mathbf{B}_0$ only

## Further Reading

- T. H. Stix, *Waves in Plasmas*, Chapter on cold plasma.
