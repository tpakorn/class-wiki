# Fourier Series Builder

## Learning goal

See [Fourier series](../concepts/fourier-series.md) *converge*: each added harmonic
sharpens the partial sum toward the target waveform, the spectrum bars show which
coefficients do the work, and the stubborn overshoot at every jump — the **Gibbs
phenomenon** — shows what convergence "almost everywhere" really means.

<iframe src="../../assets/fourier-builder.html" width="100%" height="640"
        style="border:none;" title="Fourier series builder"></iframe>

## Things to try

1. **Square wave, N = 1 → 60.** The wiggles crowd toward the jumps but the ~9%
   overshoot *never shrinks*. Pointwise vs uniform convergence, live.
2. **Triangle wave.** Continuous function ⇒ coefficients fall as $1/n^2$ ⇒
   near-perfect fit by $N = 10$. Compare the spectrum decay with the square wave's
   $1/n$.
3. **Sawtooth** — all harmonics present (odd *and* even). Which symmetry of the
   square/triangle waves kills their even terms?
4. **Rectangular pulse.** The spectrum is a sampled sinc: narrow pulse ⇒ broad
   spectrum — the [uncertainty principle](../concepts/fourier-transform.md) in one
   picture.

## Related

[Fourier series](../concepts/fourier-series.md) ·
[Fourier transform](../concepts/fourier-transform.md) ·
[Fourier integral (eq.)](../equations/fourier-integral.md)
