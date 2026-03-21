# Instability of Higher-Order Greeks


Higher-order Greeks can be unstable to estimate, especially near maturity and near payoff kinks.

---

## Noise amplification in finite differences


Second derivatives amplify noise. For numerical gamma:

\[
\Gamma_{\text{num}}(S)= \frac{V(S+h)-2V(S)+V(S-h)}{h^2}
\]

**Error analysis.** If \(V\) is computed with error \(\epsilon\):

\[
\Gamma_{\text{num}} = \Gamma_{\text{true}} + \mathcal{O}\left(\frac{\epsilon}{h^2}\right) + \mathcal{O}(h^2)
\]

The first error term comes from noise amplification; the second from truncation.

**Optimal step size.** Balancing these:

\[
h_{\text{opt}} \sim \epsilon^{1/4}
\]

For machine precision \(\epsilon \sim 10^{-16}\), optimal \(h \sim 10^{-4}\). For Monte Carlo with \(\epsilon \sim N^{-1/2}\), this gives \(h \sim N^{-1/8}\).

---

## Condition number for gamma


The condition number for gamma computation is:

\[
\kappa_\Gamma = \frac{|\Gamma| \cdot h^2}{|V|}
\]

Near ATM at expiry:
- \(\Gamma \sim \tau^{-1/2}\) (large)
- \(V \sim \sigma\sqrt{\tau}\) (small)

This gives:
\[
\kappa_\Gamma \sim \frac{h^2}{\sigma\tau}
\]

For small \(\tau\), the condition number becomes very large, making gamma estimation ill-conditioned.

---

## Instability of third-order Greeks


Third-order Greeks (speed, charm, vanna, etc.) are even more unstable:

**Speed** (\(\partial\Gamma/\partial S\)):
\[
\text{Speed}_{\text{num}} = \frac{\Gamma(S+h) - \Gamma(S-h)}{2h} = \frac{V(S+2h) - 2V(S+h) + 2V(S-h) - V(S-2h)}{2h^3}
\]

Error scales as \(\mathcal{O}(\epsilon/h^3)\), making speed extremely sensitive to noise.

**Numerical example.** With \(V\) accurate to 4 decimal places (\(\epsilon = 10^{-4}\)):

| Greek | Derivative order | Optimal \(h\) | Achievable accuracy |
|:------|:-----------------|:--------------|:--------------------|
| Delta | 1 | 0.01 | \(10^{-3}\) |
| Gamma | 2 | 0.03 | \(10^{-2}\) |
| Speed | 3 | 0.05 | \(10^{-1}\) |

Higher derivatives require larger \(h\), reducing accuracy.

---

## Gamma instability near expiry


Near expiry (\(\tau \to 0\)) for ATM options:

\[
\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} \sim \tau^{-1/2}
\]

**Spatial sensitivity.** The gamma profile has width \(\sim \sigma\sqrt{\tau}\), so:

\[
\frac{\partial \Gamma}{\partial S} \sim \frac{\Gamma}{\sigma\sqrt{\tau}} \sim \frac{1}{\sigma^2 \tau}
\]

This diverges faster than gamma itself, making spatial derivatives of gamma very unstable.

**Numerical evidence.** For \(S = K = 100\), \(\sigma = 20\%\):

| \(\tau\) (days) | \(\Gamma\) | \(\partial\Gamma/\partial S\) | Numerical stability |
|:----------------|:-----------|:------------------------------|:--------------------|
| 30 | 0.055 | 0.003 | Good |
| 7 | 0.114 | 0.016 | Moderate |
| 1 | 0.301 | 0.30 | Poor |
| 0.1 | 0.95 | 9.5 | Unstable |

---

## Smoothing and regularization


Practical approaches to stabilize Greek estimation:

**1. Bucketing.** Instead of pointwise Greeks, compute averages over strike/maturity buckets:

\[
\bar{\Gamma}_{[K_1,K_2]} = \frac{1}{K_2-K_1}\int_{K_1}^{K_2} \Gamma(K) \, dK
\]

**2. Polynomial fitting.** Fit \(V(S)\) to a smooth polynomial, then differentiate analytically:

\[
V(S) \approx \sum_{n=0}^N a_n (S-S_0)^n
\]

\[
\Gamma \approx 2a_2
\]

**3. Likelihood ratio methods.** Use LR/Malliavin estimators that don't require differencing:

\[
\Gamma = \mathbb{E}\left[e^{-r\tau}\Phi(S_T) \cdot H_\Gamma\right]
\]

where \(H_\Gamma\) is the Malliavin weight.

**4. Automatic differentiation.** Compute exact derivatives through the pricing algorithm using AD:

\[
\Gamma = \frac{\partial^2 V}{\partial S^2}\bigg|_{\text{AD}}
\]

This avoids finite-difference errors entirely.

---

## Model-specific instabilities


Beyond numerical issues, some models have inherent Greek instabilities:

**Local volatility.** \(\sigma(S,t)\) surface irregularities create Greek noise.

**Stochastic volatility.** Vega becomes multi-dimensional (vanna, volga effects).

**Jump-diffusion.** Greeks have discontinuities across jump thresholds.

**Digital options.** Delta is a Dirac delta; gamma is its derivative.

---

## Risk management implications


1. **Do not trust pointwise near-expiry gamma**: Use integrated/bucketed measures
2. **Higher-order Greeks are indicative only**: Don't rely on precise values for hedging
3. **Cross-validate methods**: Compare finite differences, LR, AD when possible
4. **Monitor condition numbers**: Flag when Greek estimation becomes unreliable
5. **Stress test Greeks**: Compute at perturbed parameters to assess stability

---

## What to remember


- Gamma estimation is numerically ill-conditioned near expiry
- Error amplification scales as \(\epsilon/h^2\) for finite differences
- Third-order Greeks (speed, etc.) are even more unstable
- Optimal step size balances truncation and noise: \(h \sim \epsilon^{1/4}\)
- Robust systems smooth or bucket sensitivities
- Alternative methods (LR, AD) can avoid finite-difference instabilities
