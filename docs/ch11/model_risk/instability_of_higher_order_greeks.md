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

---

## Exercises

**Exercise 1.** The finite-difference gamma formula is $\Gamma_{\text{num}} = (V(S+h) - 2V(S) + V(S-h))/h^2$ with error $\mathcal{O}(\epsilon/h^2) + \mathcal{O}(h^2)$. For a Monte Carlo price with $N = 10{,}000$ paths ($\epsilon \sim N^{-1/2} = 0.01$), compute the optimal step size $h_{\text{opt}} \sim \epsilon^{1/4}$ and the achievable accuracy. Repeat for $N = 1{,}000{,}000$ paths. How does the number of paths affect the quality of gamma estimation?

??? success "Solution to Exercise 1"
    For $N = 10{,}000$ paths, $\epsilon \sim N^{-1/2} = 0.01$. The optimal step size is

    $$
    h_{\text{opt}} \sim \epsilon^{1/4} = (0.01)^{1/4} = (10^{-2})^{1/4} = 10^{-0.5} \approx 0.316
    $$

    The achievable accuracy is obtained by substituting $h_{\text{opt}}$ back into either error term. Using the truncation term $\mathcal{O}(h^2)$:

    $$
    \text{Accuracy} \sim h_{\text{opt}}^2 = (0.316)^2 \approx 0.10
    $$

    Equivalently, from the noise term $\epsilon / h^2 = 0.01 / 0.1 = 0.10$. So with 10,000 paths, gamma is accurate to roughly one decimal place only.

    For $N = 1{,}000{,}000$ paths, $\epsilon \sim N^{-1/2} = 0.001$. Then

    $$
    h_{\text{opt}} \sim (0.001)^{1/4} = (10^{-3})^{1/4} = 10^{-0.75} \approx 0.178
    $$

    $$
    \text{Accuracy} \sim h_{\text{opt}}^2 = (0.178)^2 \approx 0.032
    $$

    Increasing paths by a factor of 100 reduces $\epsilon$ by a factor of 10, but the achievable gamma accuracy only improves by a factor of $10^{1/2} \approx 3.2$. This slow improvement ($\text{accuracy} \sim N^{-1/4}$) illustrates why Monte Carlo gamma estimation is fundamentally difficult: because the second derivative amplifies noise, one needs a very large number of paths for reasonable precision.

---

**Exercise 2.** Consider the speed formula $\text{Speed}_{\text{num}} = (V(S+2h) - 2V(S+h) + 2V(S-h) - V(S-2h))/(2h^3)$. If the option price is computed to accuracy $\epsilon = 10^{-4}$, derive the optimal step size by balancing $\mathcal{O}(\epsilon/h^3)$ noise against $\mathcal{O}(h^2)$ truncation error. What achievable accuracy does this give, and how does it compare to gamma's achievable accuracy?

??? success "Solution to Exercise 2"
    The speed formula has noise error $\mathcal{O}(\epsilon / h^3)$ and truncation error $\mathcal{O}(h^2)$. To find the optimal $h$, balance these:

    $$
    \frac{\epsilon}{h^3} \sim h^2 \implies h^5 \sim \epsilon \implies h_{\text{opt}} \sim \epsilon^{1/5}
    $$

    With $\epsilon = 10^{-4}$:

    $$
    h_{\text{opt}} \sim (10^{-4})^{1/5} = 10^{-0.8} \approx 0.158
    $$

    The achievable accuracy is

    $$
    \text{Accuracy} \sim h_{\text{opt}}^2 = (0.158)^2 \approx 0.025
    $$

    Alternatively, from the noise term: $\epsilon / h^3 = 10^{-4} / (0.158)^3 = 10^{-4} / 0.00395 \approx 0.025$.

    For gamma with the same $\epsilon = 10^{-4}$, the optimal step is $h \sim \epsilon^{1/4} = (10^{-4})^{1/4} = 10^{-1} = 0.1$ and the achievable accuracy is $h^2 = 0.01$.

    Comparing: speed requires a larger step size ($0.158$ vs $0.1$) and achieves worse accuracy ($0.025$ vs $0.01$). More generally, for a $k$-th order derivative, $h_{\text{opt}} \sim \epsilon^{1/(k+2)}$ and achievable accuracy is $\sim \epsilon^{2/(k+2)}$. As the derivative order increases, estimation becomes progressively harder.

---

**Exercise 3.** For an ATM call with $S = K = 100$, $\sigma = 0.20$, compute $\Gamma$ and $\partial\Gamma/\partial S$ (speed) at $\tau = 30$ days, $\tau = 7$ days, and $\tau = 1$ day using the Black-Scholes formula. Verify the scaling $\Gamma \sim \tau^{-1/2}$ and $\partial\Gamma/\partial S \sim \tau^{-1}$. At what maturity does the condition number $\kappa_\Gamma = |\Gamma| h^2 / |V|$ exceed 1 for $h = 0.01$?

??? success "Solution to Exercise 3"
    In the Black-Scholes model with $S = K$ (ATM), $d_1 = \frac{\sigma\sqrt{\tau}}{2}$ and for small $\tau$, $d_1 \approx 0$, so $N'(d_1) \approx N'(0) = \frac{1}{\sqrt{2\pi}} \approx 0.3989$.

    The gamma formula is

    $$
    \Gamma = \frac{N'(d_1)}{S \sigma \sqrt{\tau}}
    $$

    Converting days to years ($\tau_{\text{years}} = \tau_{\text{days}} / 365$):

    **At $\tau = 30$ days** ($\tau = 30/365 = 0.0822$):
    $\Gamma = \frac{0.3989}{100 \times 0.20 \times \sqrt{0.0822}} = \frac{0.3989}{100 \times 0.20 \times 0.2867} = \frac{0.3989}{5.734} \approx 0.0696$.

    **At $\tau = 7$ days** ($\tau = 7/365 = 0.01918$):
    $\Gamma = \frac{0.3989}{100 \times 0.20 \times \sqrt{0.01918}} = \frac{0.3989}{100 \times 0.20 \times 0.1385} = \frac{0.3989}{2.770} \approx 0.1440$.

    **At $\tau = 1$ day** ($\tau = 1/365 = 0.002740$):
    $\Gamma = \frac{0.3989}{100 \times 0.20 \times \sqrt{0.002740}} = \frac{0.3989}{100 \times 0.20 \times 0.05234} = \frac{0.3989}{1.047} \approx 0.3810$.

    **Verifying $\Gamma \sim \tau^{-1/2}$:** The ratio $\Gamma \cdot \sqrt{\tau}$ should be approximately constant: $0.0696 \times 0.2867 = 0.0200$; $0.1440 \times 0.1385 = 0.0199$; $0.3810 \times 0.05234 = 0.0199$. Confirmed.

    For speed, $\frac{\partial \Gamma}{\partial S} = -\frac{N'(d_1)}{S^2 \sigma \sqrt{\tau}}\left(1 + \frac{d_1}{\sigma\sqrt{\tau}}\right)$. At ATM with small $\tau$ where $d_1 \approx 0$, this simplifies to approximately $-\Gamma / S$, giving $|\partial\Gamma/\partial S| \approx \Gamma / S$. The values are approximately $0.000696$, $0.00144$, and $0.00381$ at the three maturities. Speed scales as $\tau^{-1/2}/S \sim \tau^{-1/2}$, but more precisely the full speed expression scales closer to $\tau^{-1}$ when higher-order terms in $d_1$ are included.

    **Condition number:** $\kappa_\Gamma = |\Gamma| h^2 / |V|$ with $h = 0.01$. The ATM call value is approximately $V \approx S \sigma \sqrt{\tau / (2\pi)}$. At $\tau = 30$ days: $V \approx 100 \times 0.20 \times \sqrt{0.0822 / 6.283} \approx 2.29$, so $\kappa_\Gamma = 0.0696 \times 0.0001 / 2.29 \approx 3.0 \times 10^{-6}$. At $\tau = 1$ day: $V \approx 100 \times 0.20 \times \sqrt{0.00274 / 6.283} \approx 0.418$, so $\kappa_\Gamma = 0.381 \times 0.0001 / 0.418 \approx 9.1 \times 10^{-5}$. For $h = 0.01$, $\kappa_\Gamma$ remains well below 1 even at 1 day. Reaching $\kappa_\Gamma = 1$ requires extremely short maturities (sub-minute timescales) or much larger $h$.

---

**Exercise 4.** Polynomial fitting is used to stabilize gamma estimation: fit $V(S)$ to a degree-4 polynomial $V(S) \approx a_0 + a_1(S - S_0) + a_2(S - S_0)^2 + a_3(S - S_0)^3 + a_4(S - S_0)^4$ using option prices at $S = 98, 99, 100, 101, 102$. If $\Gamma \approx 2a_2$, explain why this is more stable than the three-point finite difference. What is the effective smoothing being applied?

??? success "Solution to Exercise 4"
    The three-point finite difference uses prices at $S - h$, $S$, $S + h$ to form

    $$
    \Gamma_{\text{3pt}} = \frac{V(S+h) - 2V(S) + V(S-h)}{h^2}
    $$

    This uses only 3 data points and amplifies noise as $\epsilon / h^2$.

    The polynomial fit uses 5 prices at $S = 98, 99, 100, 101, 102$ (with $h = 1$ between points). The least-squares fit of a degree-4 polynomial $V(S) = a_0 + a_1(S - 100) + a_2(S - 100)^2 + a_3(S - 100)^3 + a_4(S - 100)^4$ uses all 5 data points to determine 5 coefficients, then $\Gamma \approx 2a_2$.

    **Why this is more stable:** The polynomial fit is equivalent to a weighted average of finite differences. By using 5 points instead of 3, the noise in each individual price has less influence on the final estimate. In a least-squares sense, if each price has error $\epsilon$, the error in $a_2$ scales as $\epsilon / \sqrt{5}$ (roughly), whereas the three-point formula concentrates all noise into one difference. More importantly, the effective step size is larger ($h = 2$ for the full range), which reduces noise amplification from $\epsilon / h^2$.

    **The effective smoothing:** The polynomial fit acts as a low-pass filter. By constraining the price function to lie on a smooth degree-4 polynomial, high-frequency noise is projected out. The fitting procedure implicitly averages over the 5 points, distributing the noise across the polynomial coefficients. This is mathematically equivalent to applying a smoothing kernel to the discrete price data before differentiating, with the kernel width determined by the spacing and number of data points.

---

**Exercise 5.** The gamma profile for an ATM option has spatial width $\sim \sigma\sqrt{\tau}$. For a finite-difference step $h$ used in delta computation, explain why $h$ must satisfy $h \ll \sigma\sqrt{\tau}$ for the delta estimate to be meaningful. For $\sigma = 0.20$ and $\tau = 1$ day, compute $\sigma\sqrt{\tau}$ and identify the range of acceptable $h$ values. What happens when $h$ exceeds this scale?

??? success "Solution to Exercise 5"
    The gamma profile for an ATM option has spatial width $w \sim \sigma\sqrt{\tau}$. The finite-difference delta formula is

    $$
    \Delta_{\text{num}} = \frac{V(S + h) - V(S - h)}{2h}
    $$

    For this to approximate the true delta, the step size $h$ must be small compared to the scale over which the delta changes. Since delta changes on the scale set by the gamma profile width $w = \sigma\sqrt{\tau}$, we need $h \ll \sigma\sqrt{\tau}$.

    If $h$ exceeds $\sigma\sqrt{\tau}$, the finite difference straddles the kink region of the payoff. The computed delta becomes a blend of the in-the-money and out-of-the-money deltas, effectively smoothing out the gamma peak. The numerical delta approaches the static hedge ratio rather than the local sensitivity.

    For $\sigma = 0.20$ and $\tau = 1$ day ($\tau = 1/365 \approx 0.00274$):

    $$
    \sigma\sqrt{\tau} = 0.20 \times \sqrt{0.00274} = 0.20 \times 0.0523 = 0.01047
    $$

    In dollar terms, $S \times \sigma\sqrt{\tau} = 100 \times 0.01047 \approx \$1.05$.

    Acceptable values of $h$ must satisfy $h \ll 0.01047$. In practice, $h \leq 0.002$ (i.e., $\$0.20$ for $S = 100$) would keep $h$ at roughly $20\%$ of the gamma width. Values like $h = 0.001$ (i.e., $\$0.10$) are safer.

    When $h > \sigma\sqrt{\tau} \approx 0.01$, the finite-difference delta begins averaging across the gamma peak rather than resolving it, and the estimate degrades. This is why near-expiry delta estimation requires very small step sizes, which in turn demands very accurate prices.

---

**Exercise 6.** Compare three approaches to computing gamma for a near-expiry digital call ($\tau = 1$ day, $S = K = 100$, $\sigma = 0.20$): (a) central finite differences with optimal $h$; (b) the likelihood ratio method $\Gamma = \mathbb{E}[e^{-r\tau}\Phi(S_T) H_\Gamma]$ with 100,000 Monte Carlo paths; (c) bucketing over the interval $[99, 101]$. Discuss the relative advantages and limitations of each approach for this extreme case.

??? success "Solution to Exercise 6"
    For a near-expiry digital call ($\tau = 1/365$, $S = K = 100$, $\sigma = 0.20$), the digital call has payoff $\mathbf{1}_{S_T > K}$. Its gamma is the derivative of a near-delta function, which becomes extremely peaked near expiry.

    **(a) Central finite differences with optimal $h$:** The digital call price is $V = e^{-r\tau}N(d_2)$, which has a very sharp transition near $S = K$. Using finite differences, the gamma is $\Gamma_{\text{num}} = (V(S+h) - 2V(S) + V(S-h))/h^2$. With Monte Carlo pricing ($\epsilon \sim N^{-1/2}$), the optimal $h \sim \epsilon^{1/4}$. However, the digital payoff has a discontinuity, so the "true" gamma involves a Dirac delta derivative. Finite differences with any $h$ produce values that are highly sensitive to $h$: too small and noise dominates; too large and the sharp peak is smoothed away. This method is essentially unusable for digital gamma near expiry.

    **(b) Likelihood ratio method with 100,000 paths:** The LR method computes $\Gamma = \mathbb{E}[e^{-r\tau}\Phi(S_T) H_\Gamma]$ where $H_\Gamma$ is a Malliavin weight that does not involve differencing the payoff. Since it avoids finite differences of the discontinuous payoff, it does not suffer from $\epsilon/h^2$ amplification. However, the Malliavin weight $H_\Gamma$ itself can have high variance for short maturities, since it involves terms that scale as $\tau^{-1}$. With $N = 100{,}000$ paths, the standard error may still be substantial. The advantage is that increasing $N$ reliably reduces the error as $N^{-1/2}$, unlike finite differences where the step size creates an additional tradeoff.

    **(c) Bucketing over $[99, 101]$:** The bucketed gamma is $\bar{\Gamma} = \frac{1}{K_2 - K_1}\int_{99}^{101}\Gamma(K)\,dK$, which equals $\frac{\Delta(101) - \Delta(99)}{2}$. This is computable and stable because it integrates the Dirac-like gamma peak over a finite interval. The result is a smooth, well-defined quantity. However, it does not give pointwise gamma at $S = 100$; it gives an average over a $\$2$ window. For risk management this may be sufficient, but for precise hedging of a single digital option it loses resolution.

    **Summary:** For digital options near expiry, (a) is unreliable due to the discontinuous payoff, (b) provides unbiased estimates but with high variance, and (c) is the most practical for risk management. The best choice depends on whether pointwise or averaged sensitivity is needed.
