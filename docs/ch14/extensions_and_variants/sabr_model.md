# SABR Model

SABR is treated as a stand-alone variant of the general stochastic-volatility framework: it abandons mean reversion in favor of a CEV backbone for the forward and a lognormal vol-of-vol, in exchange for a closed-form implied-volatility approximation. This page positions SABR alongside the other extensions in this folder; the full development is given in the dedicated SABR chapter folder.

Recall (see [§ SABR SDE and Parameters](../sabr_model/sabr_sde_and_parameters.md)): under the $T$-forward measure $dF_t = \sigma_t F_t^\beta dW_t^F$, $d\sigma_t = \nu\sigma_t dW_t^\sigma$, $d\langle W^F,W^\sigma\rangle_t = \rho\,dt$, with parameters $(\alpha,\beta,\rho,\nu)$.

---

## SABR as a Variant of the General SV Framework

Within the taxonomy of [§ Two-Factor Diffusion Models](../general_stochastic_volatility_framework/two_factor_diffusion_models.md), SABR sits at the opposite end from Heston:

| Feature | SABR | Heston |
|---------|------|--------|
| State variable | Forward $F_t$ | Spot $S_t$ |
| Volatility dynamics | Lognormal (GBM) | CIR (mean-reverting) |
| Mean reversion | No | Yes |
| Closed-form CF | No | Yes (see [§ Affine Structure](../the_heston_model/affine_structure.md)) |
| Implied-vol formula | Yes, asymptotic | No |
| Calibration speed | Very fast | Moderate |
| Long-dated accuracy | Poor | Good |
| Industry use | Rates, FX | Equity |

The absence of mean reversion is what makes the Hagan expansion tractable; it is also why SABR is unsuited to long-dated or path-dependent products.

Recall (see [§ Hagan et al. Implied Volatility Approximation](../sabr_model/hagan_implied_volatility_approximation.md)): the implied-vol formula is a singular-perturbation expansion in $\nu^2 T$ around the ATM lognormal backbone $\alpha/F^{1-\beta}$.

Recall (see [§ Normal SABR and Lognormal SABR](../sabr_model/normal_and_lognormal_sabr.md)): $\beta=0$ admits negative forwards (normal regime); $\beta=1$ is the lognormal regime; intermediate $\beta$ interpolates the backbone.

Recall (see [§ Arbitrage-Free SABR](../sabr_model/arbitrage_free_sabr.md)): the Hagan formula can produce negative implied densities in the deep wings; effective-PDE, mixture, and free-boundary corrections restore arbitrage-freeness.

Recall (see [§ SABR Calibration to Swaption Smiles](../sabr_model/calibration_to_swaption_smiles.md)): per expiry-tenor cell, $\alpha$ is pinned by ATM and $(\rho,\nu)$ are fit to the off-ATM smile, with $\beta$ chosen by convention.

---

## When to Reach for SABR Instead of Heston

The two models occupy complementary niches; the choice is driven by horizon and product type rather than by preference.

**Use SABR when:**

- Short to medium maturities (e.g., swaption smiles up to a few years)
- The instrument-of-interest is a vanilla option on a forward
- Calibration speed matters and a closed-form smile suffices
- Market quotes ATM in Black or Bachelier volatilities and the smile is shallow

**Use Heston (or a mean-reverting SV variant) when:**

- Long-dated or path-dependent products (variance swaps, cliquets, autocallables)
- Joint pricing across maturities with consistent dynamics is required
- Term-structure features of variance are economically important

For products that sit in between, [§ Multi-Factor Volatility Models](multi_factor_volatility_models.md) and [§ Rough Volatility Overview](rough_volatility_overview.md) provide further extensions that combine SABR-like local-vol exponents with mean reversion or roughness.

---

## Key Takeaways

- SABR is a CEV-plus-lognormal-vol variant of the general two-factor SV framework, not a competitor in the equity-SV space.
- The Hagan expansion gives near-instant calibration but is asymptotic and can violate arbitrage in the tails.
- For full development of SDE, parameters, Hagan formula, calibration, negative rates, and arbitrage-free variants, see the dedicated [SABR folder](../sabr_model/sabr_sde_and_parameters.md).

---

## Further Reading

- Hagan, P., Kumar, D., Lesniewski, A., & Woodward, D. (2002). *Managing smile risk*. Wilmott Magazine.
- Obloj, J. (2008). *Fine-tune your smile: Correction to Hagan et al*. Working paper.
- Antonov, A., Konikov, M., & Spector, M. (2015). *SABR spreads its wings*. Risk Magazine.
- Rebonato, R. (2004). *Volatility and Correlation*, 2nd ed. Wiley.

---

## Exercises

**Exercise 1.** Using the ATM Hagan formula for $\beta = 1$:

$$
\sigma_{\text{ATM}} = \alpha\left[1 + \frac{2-3\rho^2}{24}\nu^2 T\right]
$$

compute $\sigma_{\text{ATM}}$ for $\alpha = 0.20$, $\rho = -0.6$, $\nu = 0.4$, $T = 0.5$. Then solve inversely: given a market ATM implied vol of $22\%$ with the same $\rho$, $\nu$, and $T$, recover $\alpha$.

??? success "Solution to Exercise 1"
    We use the ATM formula for $\beta = 1$:

    $$
    \sigma_{\text{ATM}} = \alpha\left[1 + \frac{2 - 3\rho^2}{24}\nu^2 T\right]
    $$

    **Forward computation.** Substituting $\alpha = 0.20$, $\rho = -0.6$, $\nu = 0.4$, and $T = 0.5$:

    $$
    \frac{2 - 3\rho^2}{24} = \frac{2 - 3(0.36)}{24} = \frac{2 - 1.08}{24} = \frac{0.92}{24} \approx 0.03833
    $$

    $$
    \sigma_{\text{ATM}} = 0.20\left[1 + 0.03833 \times 0.16 \times 0.5\right] = 0.20\left[1 + 0.003067\right] \approx 0.20061
    $$

    So $\sigma_{\text{ATM}} \approx 20.06\%$.

    **Inverse computation.** Given $\sigma_{\text{ATM}} = 0.22$, solve for $\alpha$:

    $$
    0.22 = \alpha\left[1 + 0.03833 \times 0.16 \times 0.5\right] = \alpha \times 1.003067
    $$

    $$
    \alpha = \frac{0.22}{1.003067} \approx 0.21933
    $$

    The correction factor is close to 1, so $\alpha$ is close to $\sigma_{\text{ATM}}$, but not identical.

---

**Exercise 2.** The SABR skew formula at ATM is approximately

$$
\frac{\partial\sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
$$

For $F = 100$, $\beta = 1$, $\rho = -0.65$, $\nu = 0.45$, and $\sigma_{\text{ATM}} = 0.20$, compute the ATM skew. Then repeat with $\beta = 0.5$ and explain how the CEV exponent contributes additional skew even when $\rho = 0$.

??? success "Solution to Exercise 2"
    **ATM skew formula:**

    $$
    \frac{\partial\sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
    $$

    **Case $\beta = 1$.** With $F = 100$, $\rho = -0.65$, $\nu = 0.45$, $\sigma_{\text{ATM}} = 0.20$:

    $$
    \text{Skew} = \frac{(-0.65)(0.45)}{2(0.20)} - \frac{1-1}{2(100)} = \frac{-0.2925}{0.40} = -0.73125
    $$

    The skew is approximately $-0.731$ per unit log-strike.

    **Case $\beta = 0.5$.** Now the second term contributes:

    $$
    \text{Skew} = \frac{(-0.65)(0.45)}{2(0.20)} - \frac{1 - 0.5}{2(100)} = -0.73125 - 0.0025 = -0.73375
    $$

    **CEV contribution when $\rho = 0$.** Setting $\rho = 0$ with $\beta = 0.5$:

    $$
    \text{Skew} = 0 - \frac{0.5}{200} = -0.0025
    $$

    Even with zero correlation, the CEV exponent $\beta < 1$ generates negative skew. This is because when $F$ decreases, the local volatility $F^\beta$ decreases more slowly than $F$ itself, so the effective lognormal volatility increases. This leverage-like effect is purely geometric and does not require any correlation between the forward and its volatility.

---

**Exercise 3.** Compare the SABR and Heston models by filling in the following table with qualitative assessments:

| Feature | SABR advantage | Heston advantage |
|---------|---------------|-----------------|
| Short-maturity smile | ? | ? |
| Long-maturity term structure | ? | ? |
| Calibration speed | ? | ? |
| Dynamic consistency | ? | ? |
| Negative rates handling | ? | ? |

Justify each entry with a brief explanation.

??? success "Solution to Exercise 3"
    | Feature | SABR advantage | Heston advantage |
    |---------|---------------|-----------------|
    | Short-maturity smile | SABR excels | — |
    | Long-maturity term structure | — | Heston excels |
    | Calibration speed | SABR excels | — |
    | Dynamic consistency | — | Heston excels |
    | Negative rates handling | SABR excels | — |

    **Short-maturity smile.** SABR has a closed-form implied volatility approximation specifically designed for short maturities. The Hagan formula is most accurate for small $T$, while Heston relies on characteristic function inversion that can be less intuitive to tune for very short maturities.

    **Long-maturity term structure.** Heston's mean-reverting CIR volatility process ensures the variance stays bounded and converges to its long-run mean. SABR's GBM volatility can drift without bound, making the Hagan approximation unreliable for $T > 5$ years and producing unrealistic long-dated behavior.

    **Calibration speed.** The Hagan formula evaluates in microseconds, making SABR calibration essentially instantaneous. Heston requires numerical characteristic function inversion (Fourier integrals) for each option price, which is slower by orders of magnitude.

    **Dynamic consistency.** Heston is a fully specified diffusion model, so calibrated parameters today produce consistent dynamics for hedging over time. SABR is typically recalibrated daily, and the model does not guarantee that the forward smile dynamics match market realities, leading to potential hedging errors.

    **Negative rates handling.** SABR with $\beta = 0$ (normal backbone) or the shifted SABR extension handles negative rates naturally. Heston's CIR process ensures variance stays positive, but the lognormal asset dynamics exclude negative forward prices by construction.

---

**Exercise 4.** In the shifted SABR model, the forward dynamics are $dF_t = \sigma_t(F_t + s)^\beta\,dW_t^F$. For a market where the forward rate is $F = -0.3\%$ and the shift is $s = 3\%$, compute the shifted forward $\tilde{F} = F + s$. Using $\beta = 0.5$, $\alpha = 0.005$, $\nu = 0.4$, $\rho = 0.1$, compute the ATM implied volatility using the Hagan formula applied to $\tilde{F}$. Convert from lognormal to normal (Bachelier) volatility using $\sigma_N \approx \sigma_{\text{LN}} \cdot \tilde{F}$.

??? success "Solution to Exercise 4"
    **Shifted forward.** With $F = -0.3\% = -0.003$ and $s = 3\% = 0.03$:

    $$
    \tilde{F} = F + s = -0.003 + 0.03 = 0.027
    $$

    **ATM implied volatility.** Using the Hagan ATM formula applied to $\tilde{F}$ with $\beta = 0.5$, $\alpha = 0.005$, $\nu = 0.4$, $\rho = 0.1$, and $T = 1$:

    $$
    \sigma_{\text{ATM}} = \frac{\alpha}{\tilde{F}^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2}{24}\frac{\alpha^2}{\tilde{F}^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4\tilde{F}^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
    $$

    Computing the leading term with $\tilde{F}^{1-\beta} = 0.027^{0.5} = 0.16432$:

    $$
    \frac{\alpha}{\tilde{F}^{0.5}} = \frac{0.005}{0.16432} \approx 0.03043
    $$

    The correction terms:

    $$
    \frac{(0.5)^2}{24}\frac{(0.005)^2}{0.027} = \frac{0.25}{24}\times\frac{0.000025}{0.027} \approx 0.00000965
    $$

    $$
    \frac{(0.1)(0.5)(0.4)(0.005)}{4 \times 0.16432} \approx \frac{0.0001}{0.65728} \approx 0.0001522
    $$

    $$
    \frac{2 - 3(0.01)}{24}(0.16) = \frac{1.97}{24}\times 0.16 \approx 0.01313
    $$

    So the bracket is approximately $1 + 0.01330 \approx 1.01330$:

    $$
    \sigma_{\text{ATM}} \approx 0.03043 \times 1.01330 \approx 0.03083 = 3.08\%
    $$

    **Conversion to normal volatility:**

    $$
    \sigma_N \approx \sigma_{\text{LN}} \cdot \tilde{F} = 0.03083 \times 0.027 \approx 0.000832 = 8.32 \text{ bps}
    $$

---

**Exercise 5.** Explain why the Hagan formula can produce negative probability densities for extreme parameters. Specifically, the implied density is $f(K) = e^{rT}\partial^2 C/\partial K^2$. If $\sigma_{\text{impl}}(K)$ is not a valid smile (e.g., it becomes negative at extreme strikes), $f(K) < 0$. For $\alpha = 0.30$, $\beta = 1$, $\rho = -0.9$, $\nu = 1.0$, $F = 100$, $T = 5$, explain which combination of parameter extremes is most likely to trigger this issue.

??? success "Solution to Exercise 5"
    The implied density is obtained via the Breeden-Litzenberger formula:

    $$
    f(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}
    $$

    If we express call prices through the Black-Scholes formula with the SABR implied volatility $\sigma_{\text{impl}}(K)$, the density involves second derivatives of both the smile and the Black-Scholes vega/gamma terms.

    **Why negative densities arise.** The Hagan formula is an asymptotic expansion that is accurate near ATM and for small $T$. At extreme strikes, the approximation can produce:

    - Implied volatilities that decrease too steeply in the wings, or
    - Implied volatilities that become negative (unphysical).

    Either scenario leads to $\partial^2 C / \partial K^2 < 0$, violating the no-arbitrage requirement that the density be non-negative.

    **For the given parameters** ($\alpha = 0.30$, $\beta = 1$, $\rho = -0.9$, $\nu = 1.0$, $F = 100$, $T = 5$), the combination is extreme in multiple ways:

    - $|\rho| = 0.9$ near the boundary creates very steep skew,
    - $\nu = 1.0$ is a very high vol-of-vol, amplifying smile curvature,
    - $T = 5$ is long-dated, where the $O(T^2)$ remainder in the Hagan expansion becomes large.

    The most dangerous combination is **high $\nu$ with $|\rho|$ near 1 and large $T$**. The high $\nu$ makes the smile very curved, the extreme $\rho$ makes it very skewed, and the large $T$ pushes the asymptotic expansion well outside its range of validity. Together, these cause the Hagan approximation to overshoot in the put wing (low strikes), producing implied volatilities that are too low or even negative, and hence negative densities. The correction terms proportional to $\nu^2 T$ and $\rho\nu T$ dominate the base term, invalidating the perturbation expansion.

---

**Exercise 6.** A rates trader fixes $\beta = 0$ (normal SABR) and calibrates $(\alpha, \rho, \nu)$ to a 1-year swaption smile. She obtains $\alpha = 80$ bps, $\rho = 0.15$, $\nu = 0.50$. The next day, the forward rate moves from 3.5% to 3.0% but the smile shape remains similar. Will she need to recalibrate $\alpha$, or does the normal SABR model automatically adjust? Compare with $\beta = 1$ (lognormal SABR) where $\sigma_{\text{ATM}} \propto 1/F$.

??? success "Solution to Exercise 6"
    **Normal SABR ($\beta = 0$).** The ATM normal implied volatility is approximately:

    $$
    \sigma_{\text{ATM}}^N \approx \alpha\left[1 + \frac{2 - 3\rho^2}{24}\nu^2 T\right]
    $$

    This does not depend on $F$. When the forward rate moves from 3.5% to 3.0%, the normal ATM volatility remains approximately 80 bps (since $\alpha = 80$ bps and the correction is $F$-independent). The trader does not need to recalibrate $\alpha$ for a parallel shift in the forward rate; the model automatically accommodates level changes.

    **Lognormal SABR ($\beta = 1$).** The ATM lognormal implied volatility is:

    $$
    \sigma_{\text{ATM}}^{\text{LN}} \approx \frac{\alpha}{F^{1-\beta}} = \alpha
    $$

    for $\beta = 1$, but the corresponding normal volatility is $\sigma_N \approx \sigma_{\text{LN}} \cdot F$. So when $F$ drops from 3.5% to 3.0%, the normal volatility drops proportionally:

    $$
    \sigma_N^{\text{new}} \approx \alpha \times 0.030 = 0.030\alpha
    $$

    versus $\sigma_N^{\text{old}} \approx 0.035\alpha$. This is a $14.3\%$ decline in normal volatility, which may not match the market observation that the smile shape remains similar.

    **Conclusion.** For interest rate markets where normal volatility is approximately stable across rate levels, $\beta = 0$ is the more appropriate choice. It provides a natural "sticky normal vol" behavior, whereas $\beta = 1$ implies "sticky lognormal vol" which translates to changing normal vol as rates move.

---

**Exercise 7.** The SABR model has no mean reversion in the volatility process ($d\sigma_t = \nu\sigma_t\,dW_t^\sigma$). Explain why this causes problems for long-dated options. Specifically, compute the expected value and variance of $\sigma_T$ under this GBM dynamics for $\sigma_0 = 0.2$, $\nu = 0.4$, $T = 10$. What is the probability that $\sigma_T > 1$ (100% vol)? Is this economically realistic?

??? success "Solution to Exercise 7"
    The volatility follows GBM: $d\sigma_t = \nu\sigma_t\,dW_t^\sigma$. By Ito's lemma:

    $$
    \sigma_T = \sigma_0\exp\!\left(-\frac{\nu^2}{2}T + \nu W_T\right)
    $$

    **Expected value.** Since $\sigma_T$ is a geometric Brownian motion (driftless, as the $dt$ coefficient is zero):

    $$
    \mathbb{E}[\sigma_T] = \sigma_0 = 0.2
    $$

    **Variance.** Using $\mathbb{E}[\sigma_T^2] = \sigma_0^2 e^{\nu^2 T}$:

    $$
    \text{Var}(\sigma_T) = \sigma_0^2\!\left(e^{\nu^2 T} - 1\right) = 0.04\!\left(e^{0.16 \times 10} - 1\right) = 0.04\!\left(e^{1.6} - 1\right)
    $$

    $$
    e^{1.6} \approx 4.953
    $$

    $$
    \text{Var}(\sigma_T) \approx 0.04 \times 3.953 = 0.15812
    $$

    The standard deviation is $\sqrt{0.15812} \approx 0.3976$, which is about twice the mean.

    **Probability that $\sigma_T > 1$.** We need:

    $$
    \mathbb{P}(\sigma_T > 1) = \mathbb{P}\!\left(\sigma_0 e^{-\nu^2 T/2 + \nu W_T} > 1\right)
    $$

    $$
    = \mathbb{P}\!\left(W_T > \frac{\ln(1/\sigma_0) + \nu^2 T/2}{\nu}\right)
    $$

    $$
    = \mathbb{P}\!\left(W_T > \frac{\ln 5 + 0.8}{0.4}\right) = \mathbb{P}\!\left(W_T > \frac{1.6094 + 0.8}{0.4}\right)
    $$

    $$
    = \mathbb{P}(W_T > 6.0236)
    $$

    Since $W_T \sim N(0, T) = N(0, 10)$, we standardize:

    $$
    \mathbb{P}\!\left(Z > \frac{6.0236}{\sqrt{10}}\right) = \mathbb{P}(Z > 1.904) \approx 2.85\%
    $$

    **Economic realism.** A $2.85\%$ probability of volatility exceeding 100% over 10 years is unrealistically high. In real markets, volatility exhibits strong mean reversion and rarely stays above 50% for extended periods, let alone reaching 100%. This illustrates the fundamental limitation of the SABR model for long-dated options: the GBM volatility dynamics produce excessively heavy tails in the volatility distribution, leading to option prices that overweight extreme volatility scenarios. Models with mean-reverting volatility (such as Heston) are far more appropriate for long-dated products.
