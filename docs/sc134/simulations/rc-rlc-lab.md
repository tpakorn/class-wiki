# RC / RLC Circuit Lab

## Learning goal

Two behaviors that rule all of circuit dynamics: the **exponential** (RC charging,
time constant $\tau = RC$) and the **resonance peak** (series RLC,
$f_0 = 1/2\pi\sqrt{LC}$, sharpness set by $Q = \omega_0 L/R$).

<iframe src="../../assets/rc-rlc.html" width="100%" height="620"
        style="border:none;" title="RC RLC circuit lab"></iframe>

## Things to try

1. **RC tab:** double $R$, then double $C$ — same stretch of $\tau$ either way. Why
   does only the *product* matter?
2. Find settings where the capacitor is "fully" charged within 100 ms. (Rule of
   thumb: $5\tau$.)
3. **RLC tab:** lower $R$ and watch the peak sharpen — high-$Q$ tuning. This curve is
   how a radio picks one station out of the spectrum.
4. Double $L$ *and* halve $C$: the resonance stays put but the peak narrows —
   $f_0$ depends on $LC$, $Q$ on $\sqrt{L/C}/R$.

## Related

[RC circuits](../concepts/rc-circuits.md) ·
[DC circuits](../concepts/dc-circuits.md) ·
[Faraday's law & inductance](../concepts/faraday-law.md)
