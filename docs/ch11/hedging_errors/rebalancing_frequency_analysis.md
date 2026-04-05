# Rebalancing Frequency Analysis

Continuous delta hedging is an idealization that cannot be achieved in practice. Real hedging occurs at discrete times, introducing a random hedging error. This section analyzes how the **rebalancing frequency** affects hedging quality, derives the fundamental scaling laws, and studies the **cost-error tradeoff** that arises when transaction costs are included.

---

## Setup: Discrete Hedging Framework

### The Hedging Problem

Consider an option $V(t,S)$ hedged by holding $\Delta_k = \Delta(t_k, S_{t_k})$ shares of the underlying at discrete rebalancing times $t_0 < t_1 < \cdots < t_N = T$ with uniform spacing $\delta t = T/N$.

The hedge portfolio evolves as:

$$
\Pi_{k+1} = \Pi_k\, e^{r\,\delta t} + \Delta_k\left(S_{k+1} - S_k\, e^{r\,\delta t}\right)
$$

The hedging error at each step is the mismatch between the option value change and the hedge portfolio change:

$$
\epsilon_k = \left(V_{k+1} - V_k\right) - \left(\Pi_{k+1} - \Pi_k\right)
$$

### Taylor Expansion of the Error

Using the Ito-Taylor expansion (ignoring discounting for clarity):

$$
V_{k+1} - V_k \approx \Delta_k\,\delta S_k + \Theta_k\,\delta t + \frac{1}{2}\Gamma_k\,(\delta S_k)^2
$$

where $\delta S_k = S_{k+1} - S_k$. Since the hedge captures only $\Delta_k\,\delta S_k$:

$$
\boxed{\epsilon_k \approx \Theta_k\,\delta t + \frac{1}{2}\Gamma_k\,(\delta S_k)^2}
$$

Using the theta-gamma identity $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma \approx r(V - S\Delta)$:

$$
\epsilon_k \approx \frac{1}{2}\Gamma_k\left[(\delta S_k)^2 - \sigma^2 S_k^2\,\delta t\right]
$$

This reveals that the hedging error is driven by the **difference between realized and expected squared price moves**.

---

## Variance of the Hedging Error

### Single-Step Variance

Under Black-Scholes dynamics with $\delta S_k = \sigma S_k \sqrt{\delta t}\, Z_k + O(\delta t)$ where $Z_k \sim \mathcal{N}(0,1)$:

$$
(\delta S_k)^2 = \sigma^2 S_k^2\,\delta t\, Z_k^2 + O(\delta t^{3/2})
$$

The conditional mean and variance of $\epsilon_k$ are:

$$
\mathbb{E}[\epsilon_k \mid \mathcal{F}_{t_k}] \approx 0
$$

$$
\operatorname{Var}(\epsilon_k \mid \mathcal{F}_{t_k}) \approx \frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4\,(\delta t)^2
$$

The factor $\frac{1}{2}$ comes from $\operatorname{Var}(Z^2) = 2$ for $Z \sim \mathcal{N}(0,1)$.

### Cumulative Error Variance

Summing over $N = T/\delta t$ independent steps:

$$
\boxed{\operatorname{Var}(\mathrm{HE}) \approx \frac{1}{2}\,\overline{\Gamma^2 S^4 \sigma^4}\, T\,\delta t}
$$

where $\overline{\Gamma^2 S^4 \sigma^4}$ denotes the time-averaged quantity. The key scaling law is:

$$
\operatorname{Std}(\mathrm{HE}) \propto \sqrt{\delta t} = \frac{1}{\sqrt{N}} \cdot \sqrt{T}
$$

**Theorem (Hedging Error Scaling).** *Under Black-Scholes dynamics with $N$ equally spaced rebalancing dates, the standard deviation of the cumulative hedging error satisfies:*

$$
\operatorname{Std}(\mathrm{HE}) = c_\Gamma \cdot \sqrt{\frac{T}{N}}
$$

*where $c_\Gamma = \sqrt{\frac{1}{2}\int_0^T \mathbb{E}[\Gamma(t,S_t)^2 S_t^4 \sigma^4]\,dt}$ is a constant depending on the option characteristics.*

!!! info "Interpretation"
    - Doubling the rebalancing frequency reduces hedging error standard deviation by a factor of $\sqrt{2} \approx 1.41$.
    - To halve the hedging error, you need four times as many rebalancing dates.
    - This $\sqrt{N}$ convergence is a consequence of the central limit theorem applied to the sum of per-step errors.

---

## Asymptotic Distribution

### Central Limit Theorem for Hedging Error

For large $N$, the cumulative hedging error is approximately Gaussian:

$$
\mathrm{HE}_N \xrightarrow{d} \mathcal{N}\!\left(0,\; \frac{1}{2}\int_0^T \Gamma^2 S_t^4 \sigma^4\,dt \cdot \delta t\right)
$$

More precisely, the normalized hedging error converges:

$$
\frac{\mathrm{HE}_N}{\sqrt{\delta t}} \xrightarrow{d} \mathcal{N}\!\left(0,\; \frac{1}{2}\int_0^T \Gamma^2 S_t^4 \sigma^4\,dt\right)
$$

This result, due to Bertsimas, Kogan, and Lo (2000), provides the basis for confidence intervals:

$$
\Pr\!\left(|\mathrm{HE}_N| \leq 1.96 \cdot \operatorname{Std}(\mathrm{HE})\right) \approx 0.95
$$

---

## Frequency-Error Table

Consider an ATM call with $S = K = 100$, $\sigma = 20\%$, $T = 0.25$ years, $r = 5\%$. The gamma is approximately $\Gamma \approx 0.032$, giving $c_\Gamma \approx \frac{1}{\sqrt{2}} \times 0.032 \times 10{,}000 \times 0.04 \times 0.5 \approx 4.5$.

| Frequency | $N$ | $\delta t$ (years) | $\operatorname{Std}(\mathrm{HE})$ | Relative to daily |
|:---|:---|:---|:---|:---|
| Monthly | 3 | 1/12 | $\sim \$1.30$ | 3.2x |
| Weekly | 13 | 1/52 | $\sim \$0.63$ | 1.5x |
| Daily | 63 | 1/252 | $\sim \$0.40$ | 1.0x |
| Twice daily | 126 | 1/504 | $\sim \$0.28$ | 0.71x |
| Hourly | 504 | 1/2016 | $\sim \$0.14$ | 0.35x |
| Continuous | $\infty$ | 0 | 0 | 0 |

The pattern is clear: moving from weekly to daily reduces the error by about $\sqrt{5} \approx 2.2$ times; moving from daily to hourly reduces it by about $\sqrt{8} \approx 2.8$ times.

---

## Transaction Costs and the Cost-Error Tradeoff

### Transaction Cost Model

Each rebalancing incurs a cost proportional to the number of shares traded:

$$
\text{TC}_k = \kappa\, S_k\, |\Delta_{k+1} - \Delta_k|
$$

where $\kappa$ is the proportional transaction cost (half-spread). The total transaction cost over $[0, T]$ is:

$$
\text{TC}_{\text{total}} = \kappa \sum_{k=0}^{N-1} S_k\, |\Delta_{k+1} - \Delta_k|
$$

### Expected Transaction Cost

The delta change at each step satisfies:

$$
|\Delta_{k+1} - \Delta_k| \approx |\Gamma_k|\,|\delta S_k| \approx |\Gamma_k|\, \sigma S_k\, \sqrt{\delta t}\, |Z_k|
$$

Taking expectations (using $\mathbb{E}[|Z|] = \sqrt{2/\pi}$):

$$
\mathbb{E}[\text{TC}_k] \approx \kappa\, |\Gamma_k|\, \sigma S_k^2 \sqrt{\frac{2\,\delta t}{\pi}}
$$

Summing over $N$ steps:

$$
\boxed{\mathbb{E}[\text{TC}_{\text{total}}] \approx \kappa\, \overline{|\Gamma| \sigma S^2}\, T \sqrt{\frac{2}{\pi\,\delta t}} = C_0 \sqrt{N}}
$$

where $C_0$ depends on the option parameters and spread. Transaction costs grow as $\sqrt{N}$ --- more frequent rebalancing is increasingly expensive.

### The Tradeoff

| Component | Scaling with $N$ |
|:---|:---|
| Hedging error std | $\propto 1/\sqrt{N}$ (decreasing) |
| Expected transaction cost | $\propto \sqrt{N}$ (increasing) |
| Total cost (error + TC) | $\propto 1/\sqrt{N} + c\sqrt{N}$ (U-shaped) |

The total cost function is:

$$
\text{Total}(N) = \frac{a}{\sqrt{N}} + b\sqrt{N}
$$

where $a$ represents the hedging error impact and $b$ represents the transaction cost per rebalancing.

### Optimal Rebalancing Frequency

Minimizing the total cost:

$$
\frac{d}{dN}\text{Total}(N) = -\frac{a}{2N^{3/2}} + \frac{b}{2\sqrt{N}} = 0
$$

$$
\boxed{N^* = \frac{a}{b} = \frac{\text{error sensitivity}}{\text{transaction cost rate}}}
$$

The optimal frequency is:

$$
\delta t^* = T \cdot \frac{b}{a}
$$

!!! tip "Practical Interpretation"
    - **Liquid markets** (small $\kappa$, small $b$): Rebalance frequently ($N^*$ is large).
    - **Illiquid markets** (large $\kappa$, large $b$): Rebalance less often.
    - **High gamma** (large $a$): More frequent rebalancing is warranted.
    - **Low gamma** (small $a$): The hedging error is small regardless, so less frequent rebalancing suffices.

---

## Leland's Adjusted Volatility

### Modified Hedging Strategy

Leland (1985) proposed adjusting the implied volatility used for computing deltas to account for transaction costs. The **Leland volatility** is:

$$
\hat{\sigma}^2 = \sigma^2\left(1 + \sqrt{\frac{2}{\pi}} \cdot \frac{\kappa}{\sigma\sqrt{\delta t}}\right)
$$

By hedging with $\hat{\Delta} = \Delta(\hat{\sigma})$ instead of $\Delta(\sigma)$, the expected hedging cost (error plus transaction costs) is reduced. The adjustment widens the effective volatility, which systematically over-hedges to compensate for the discrete rebalancing.

### Interpretation

The Leland adjustment adds a correction term of order $O(1/\sqrt{\delta t})$ to the volatility. In the limit $\delta t \to 0$ (continuous hedging), $\hat{\sigma} \to \sigma$ and the adjustment vanishes. For finite $\delta t$, the adjustment accounts for the asymmetric impact of transaction costs on the hedging P&L.

---

## Gamma-Weighted Rebalancing

### Non-Uniform Schedules

The analysis above assumes uniform rebalancing. Since gamma varies over the option's life (peaking near expiry for ATM options), a **non-uniform** schedule can improve efficiency.

**Principle:** Rebalance more frequently when gamma is large, less frequently when gamma is small.

A simple adaptive rule: rebalance when the estimated hedging error exceeds a threshold:

$$
\frac{1}{2}|\Gamma_k| \cdot \sigma^2 S_k^2 \cdot (t - t_k) > \varepsilon_{\text{target}}
$$

This leads to shorter intervals near the strike and near expiry, and longer intervals when the option is deep in- or out-of-the-money.

---

## Numerical Example

Consider delta-hedging a short ATM European call ($S = K = 100$, $\sigma = 25\%$, $T = 0.5$, $r = 3\%$) with transaction costs $\kappa = 0.001$ (10 bps half-spread).

**Parameters:**

- Option price $\approx \$7.50$
- Average $\Gamma S^2 \sigma^2 / 2 \approx 20$ (dollar gamma)
- Transaction cost per rebalance $\approx \$0.05$

**Comparison of frequencies:**

| Frequency | $N$ | HE Std | Expected TC | Total |
|:---|:---|:---|:---|:---|
| Weekly | 26 | \$0.98 | \$0.26 | \$1.24 |
| Daily | 126 | \$0.45 | \$0.56 | \$1.01 |
| Twice daily | 252 | \$0.32 | \$0.79 | \$1.11 |
| Hourly | 1008 | \$0.16 | \$1.59 | \$1.75 |

The minimum total cost occurs near **daily** rebalancing for this set of parameters. Hourly rebalancing improves hedging accuracy but the transaction costs dominate. Weekly rebalancing saves on costs but leaves too much hedging error.

---

## Higher-Order Corrections

### Beyond the Leading Term

The $\sqrt{\delta t}$ scaling captures the leading-order behavior. Higher-order asymptotic expansions reveal:

$$
\operatorname{Var}(\mathrm{HE}) = c_1\,\delta t + c_2\,(\delta t)^2 + O((\delta t)^3)
$$

where $c_1$ is the gamma-squared integral and $c_2$ involves the **speed** (derivative of gamma with respect to spot) and the **charm** (derivative of delta with respect to time). These corrections become relevant for very coarse rebalancing schedules.

### Skewness

The hedging error distribution is not perfectly Gaussian. The leading-order skewness is:

$$
\operatorname{Skew}(\mathrm{HE}) \propto (\delta t)^{1/2}
$$

which vanishes as $\delta t \to 0$, consistent with the CLT. For finite $\delta t$, the distribution is slightly right-skewed for long gamma positions (since $(Z^2 - 1)$ has positive skewness).

---

## Summary

| Result | Formula |
|:---|:---|
| Per-step error | $\epsilon_k \approx \frac{1}{2}\Gamma_k[(\delta S_k)^2 - \sigma^2 S_k^2\,\delta t]$ |
| Error std scaling | $\operatorname{Std}(\mathrm{HE}) \propto \sqrt{\delta t} = O(1/\sqrt{N})$ |
| Transaction cost scaling | $\mathbb{E}[\text{TC}] \propto \sqrt{N}$ |
| Optimal frequency | $N^* = a/b$ (error sensitivity / cost rate) |
| Asymptotic distribution | Gaussian by CLT |
| Leland adjustment | $\hat{\sigma}^2 = \sigma^2(1 + \kappa\sqrt{2/(\pi\sigma^2\delta t)})$ |
| Key insight | Hedging quality is limited by the $\sqrt{\delta t}$ barrier; transaction costs create a U-shaped total cost curve |

---

## Exercises

**Exercise 1.** For an ATM call with $S = K = 100$, $\sigma = 0.25$, $T = 0.5$, and constant $\Gamma = 0.028$, compute the cumulative hedging error standard deviation for $N = 26$ (weekly), $N = 126$ (daily), and $N = 504$ (twice daily) rebalancing dates. Verify that the ratios of these standard deviations are consistent with the $\sqrt{\delta t}$ scaling law.

??? success "Solution to Exercise 1"
    With $S = K = 100$, $\sigma = 0.25$, $T = 0.5$, $\Gamma = 0.028$:

    The cumulative hedging error variance is:

    $$
    \operatorname{Var}(\text{HE}) = \frac{1}{2}\Gamma^2 S^4 \sigma^4 T \cdot \delta t
    $$

    First compute the constant factor:

    $$
    \frac{1}{2}\Gamma^2 S^4 \sigma^4 T = \frac{1}{2}(0.028)^2(10^8)(0.25)^4(0.5)
    $$

    $$
    = \frac{1}{2}(7.84 \times 10^{-4})(10^8)(3.906 \times 10^{-3})(0.5)
    $$

    $$
    = \frac{1}{2}(7.84 \times 10^{-4})(10^8)(1.953 \times 10^{-3}) = \frac{1}{2}(7.84 \times 10^{-4})(1.953 \times 10^{5})
    $$

    $$
    = \frac{1}{2}(153.1) = 76.55
    $$

    **Weekly** ($N = 26$, $\delta t = T/N = 0.5/26 \approx 0.01923$):

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{76.55 \times 0.01923} = \sqrt{1.472} \approx 1.213
    $$

    **Daily** ($N = 126$, $\delta t = 0.5/126 \approx 0.003968$):

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{76.55 \times 0.003968} = \sqrt{0.3038} \approx 0.551
    $$

    **Twice daily** ($N = 504$, $\delta t = 0.5/504 \approx 0.000992$):

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{76.55 \times 0.000992} = \sqrt{0.07594} \approx 0.276
    $$

    **Verification of $\sqrt{\delta t}$ scaling:**

    $$
    \frac{\text{Std(weekly)}}{\text{Std(daily)}} = \frac{1.213}{0.551} \approx 2.20 \approx \sqrt{126/26} = \sqrt{4.846} \approx 2.20 \;\checkmark
    $$

    $$
    \frac{\text{Std(daily)}}{\text{Std(twice daily)}} = \frac{0.551}{0.276} \approx 2.00 \approx \sqrt{504/126} = \sqrt{4} = 2.00 \;\checkmark
    $$

    The ratios confirm the $\sqrt{\delta t}$ scaling law.

---

**Exercise 2.** The total cost function is $\text{Total}(N) = a/\sqrt{N} + b\sqrt{N}$. Derive the optimal $N^*$ that minimizes this function. For $a = 4.0$ and $b = 0.05$, compute $N^*$ and the corresponding optimal rebalancing interval $\delta t^*$ when $T = 0.25$. What is the minimum total cost?

??? success "Solution to Exercise 2"
    The total cost function is:

    $$
    \text{Total}(N) = \frac{a}{\sqrt{N}} + b\sqrt{N}
    $$

    Taking the derivative and setting it to zero:

    $$
    \frac{d}{dN}\text{Total}(N) = -\frac{a}{2N^{3/2}} + \frac{b}{2\sqrt{N}} = 0
    $$

    Multiplying through by $2N^{3/2}$:

    $$
    -a + bN = 0 \implies N^* = \frac{a}{b}
    $$

    For $a = 4.0$ and $b = 0.05$:

    $$
    N^* = \frac{4.0}{0.05} = 80
    $$

    The optimal rebalancing interval with $T = 0.25$:

    $$
    \delta t^* = \frac{T}{N^*} = \frac{0.25}{80} = 0.003125 \text{ years} \approx 0.79 \text{ trading days}
    $$

    This suggests rebalancing slightly more frequently than once per day.

    The minimum total cost is:

    $$
    \text{Total}(N^*) = \frac{a}{\sqrt{a/b}} + b\sqrt{a/b} = \sqrt{ab} + \sqrt{ab} = 2\sqrt{ab}
    $$

    $$
    = 2\sqrt{4.0 \times 0.05} = 2\sqrt{0.20} = 2 \times 0.4472 \approx 0.894
    $$

    The minimum total cost is approximately $\$0.89$.

---

**Exercise 3.** Leland's adjusted volatility is $\hat{\sigma}^2 = \sigma^2(1 + \sqrt{2/\pi} \cdot \kappa/(\sigma\sqrt{\delta t}))$. For $\sigma = 0.20$, $\kappa = 0.002$ (20 bps half-spread), and daily rebalancing ($\delta t = 1/252$), compute $\hat{\sigma}$. By what percentage does the Leland volatility exceed the true volatility? How does this percentage change if the trader switches to weekly rebalancing?

??? success "Solution to Exercise 3"
    With $\sigma = 0.20$, $\kappa = 0.002$, $\delta t = 1/252$:

    $$
    \hat{\sigma}^2 = \sigma^2\left(1 + \sqrt{\frac{2}{\pi}} \cdot \frac{\kappa}{\sigma\sqrt{\delta t}}\right)
    $$

    Compute the correction factor:

    $$
    \frac{\kappa}{\sigma\sqrt{\delta t}} = \frac{0.002}{0.20 \times \sqrt{1/252}} = \frac{0.002}{0.20 \times 0.06299} = \frac{0.002}{0.01260} \approx 0.15873
    $$

    $$
    \sqrt{\frac{2}{\pi}} \approx 0.7979
    $$

    $$
    \hat{\sigma}^2 = 0.04\left(1 + 0.7979 \times 0.15873\right) = 0.04(1 + 0.12665) = 0.04 \times 1.12665 = 0.04507
    $$

    $$
    \hat{\sigma} = \sqrt{0.04507} \approx 0.2123
    $$

    The Leland volatility exceeds the true volatility by:

    $$
    \frac{\hat{\sigma} - \sigma}{\sigma} = \frac{0.2123 - 0.20}{0.20} = \frac{0.0123}{0.20} \approx 6.15\%
    $$

    **For weekly rebalancing** ($\delta t = 1/52$):

    $$
    \frac{\kappa}{\sigma\sqrt{\delta t}} = \frac{0.002}{0.20 \times \sqrt{1/52}} = \frac{0.002}{0.20 \times 0.13868} = \frac{0.002}{0.02774} \approx 0.07211
    $$

    $$
    \hat{\sigma}^2 = 0.04(1 + 0.7979 \times 0.07211) = 0.04(1 + 0.05753) = 0.04 \times 1.05753 = 0.04230
    $$

    $$
    \hat{\sigma} \approx \sqrt{0.04230} \approx 0.2057
    $$

    The percentage excess is:

    $$
    \frac{0.2057 - 0.20}{0.20} \approx 2.85\%
    $$

    The Leland adjustment is smaller for weekly rebalancing ($2.85\%$ vs $6.15\%$) because less frequent rebalancing incurs fewer transaction costs per unit time, requiring a smaller volatility correction.

---

**Exercise 4.** The expected total transaction cost scales as $\mathbb{E}[\text{TC}_{\text{total}}] \approx C_0 \sqrt{N}$. For an ATM call with $\Gamma = 0.032$, $\sigma = 0.20$, $S = 100$, $T = 0.25$, and $\kappa = 0.001$, compute $C_0$ and the expected transaction costs for daily and hourly rebalancing. At what rebalancing frequency do expected transaction costs equal $1\%$ of the option price (approximately $\$4.50$)?

??? success "Solution to Exercise 4"
    From the formula $\mathbb{E}[\text{TC}_{\text{total}}] \approx C_0\sqrt{N}$ where:

    $$
    C_0 = \kappa\,\overline{|\Gamma|\sigma S^2}\,T\,\sqrt{\frac{2}{\pi}}
    $$

    Wait -- more precisely, each step costs $\mathbb{E}[\text{TC}_k] \approx \kappa\,|\Gamma_k|\,\sigma S_k^2\sqrt{2\delta t/\pi}$, and summing $N$ steps:

    $$
    \mathbb{E}[\text{TC}_{\text{total}}] = N \times \kappa\,|\Gamma|\,\sigma S^2\sqrt{\frac{2\delta t}{\pi}} = \kappa\,|\Gamma|\,\sigma S^2\,\sqrt{\frac{2N}{\pi}} \cdot \sqrt{T}
    $$

    Let us define $C_0$ so that $\mathbb{E}[\text{TC}_{\text{total}}] = C_0\sqrt{N}$:

    $$
    C_0 = \kappa\,|\Gamma|\,\sigma S^2\,\sqrt{\frac{2T}{\pi}}
    $$

    With $\kappa = 0.001$, $\Gamma = 0.032$, $\sigma = 0.20$, $S = 100$, $T = 0.25$:

    $$
    C_0 = 0.001 \times 0.032 \times 0.20 \times 10000 \times \sqrt{\frac{0.5}{\pi}}
    $$

    $$
    = 0.001 \times 0.032 \times 0.20 \times 10000 \times \sqrt{0.15915}
    $$

    $$
    = 0.064 \times 0.3989 \approx 0.02553
    $$

    **Daily rebalancing** ($N = 63$ for $T = 0.25$):

    $$
    \mathbb{E}[\text{TC}] = 0.02553 \times \sqrt{63} = 0.02553 \times 7.937 \approx 0.2026
    $$

    **Hourly rebalancing** ($N = 63 \times 8 = 504$):

    $$
    \mathbb{E}[\text{TC}] = 0.02553 \times \sqrt{504} = 0.02553 \times 22.45 \approx 0.573
    $$

    **Frequency where TC equals 1% of option price.** With option price $\approx \$4.50$, we need $\text{TC} = 0.045$:

    $$
    0.02553\sqrt{N} = 0.045 \implies \sqrt{N} = 1.763 \implies N \approx 3.1
    $$

    Transaction costs reach $1\%$ of the option price at approximately $N = 3$ rebalancing events over the life of the option, which corresponds to monthly rebalancing ($\delta t \approx 0.25/3 \approx 0.083$ years). For any higher frequency, TC exceeds $1\%$ of the option price.

---

**Exercise 5.** Using the CLT for hedging error, construct a 95% confidence interval for the cumulative hedging error of a daily-rebalanced short ATM call with $S = K = 100$, $\sigma = 0.20$, $T = 0.5$, $\Gamma = 0.025$. Express the interval in dollars and as a percentage of the option price (approximately $\$6.30$). How does the interval change if gamma-weighted adaptive rebalancing reduces the effective number of high-gamma steps by half?

??? success "Solution to Exercise 5"
    With $S = K = 100$, $\sigma = 0.20$, $T = 0.5$, $\Gamma = 0.025$, daily rebalancing ($\delta t = 1/252$):

    $$
    \operatorname{Var}(\text{HE}) = \frac{1}{2}\Gamma^2 S^4 \sigma^4 T \cdot \delta t
    $$

    $$
    = \frac{1}{2}(0.025)^2(10^8)(0.20)^4(0.5)(1/252)
    $$

    $$
    = \frac{1}{2}(6.25 \times 10^{-4})(10^8)(1.6 \times 10^{-3})(0.5)(3.968 \times 10^{-3})
    $$

    $$
    = \frac{1}{2}(6.25 \times 10^{-4})(10^8)(3.175 \times 10^{-6})
    $$

    $$
    = \frac{1}{2}(6.25 \times 10^{-4})(317.5) = \frac{1}{2}(0.1984) = 0.09922
    $$

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{0.09922} \approx 0.3150
    $$

    The 95% confidence interval is:

    $$
    [-1.96 \times 0.315,\; +1.96 \times 0.315] = [-0.617,\; +0.617]
    $$

    **In dollars:** the interval is approximately $[-\$0.62, +\$0.62]$.

    **As a percentage of option price** ($\approx \$6.30$):

    $$
    \frac{0.617}{6.30} \approx 9.8\%
    $$

    The 95% confidence interval is approximately $\pm 9.8\%$ of the option price.

    **With adaptive rebalancing** reducing effective high-gamma steps by half: the dominant contribution to $\operatorname{Var}(\text{HE})$ comes from high-gamma steps. If adaptive scheduling halves the effective number of these steps (by rebalancing more frequently during high-gamma periods and less frequently otherwise), the variance decreases by roughly a factor of 2:

    $$
    \operatorname{Std}(\text{HE})_{\text{adaptive}} \approx \frac{0.315}{\sqrt{2}} \approx 0.223
    $$

    The 95% CI shrinks to approximately $[-\$0.44, +\$0.44]$, or about $\pm 6.9\%$ of the option price.

---

**Exercise 6.** A trader considers a non-uniform rebalancing schedule where the interval shrinks near expiry. The adaptive rule triggers rebalancing when $\frac{1}{2}|\Gamma_k| \sigma^2 S_k^2 (t - t_k) > \varepsilon_{\text{target}}$. For $\varepsilon_{\text{target}} = 0.05$, $\sigma = 0.20$, $S = 100$, and $\Gamma$ ranging from $0.03$ (at $\tau = 3$ months) to $0.30$ (at $\tau = 1$ day), compute the maximum allowable interval $\delta t_{\max}$ at each gamma level. How does this compare to a uniform daily schedule?

??? success "Solution to Exercise 6"
    The adaptive rule triggers rebalancing when:

    $$
    \frac{1}{2}|\Gamma_k|\,\sigma^2 S_k^2\,(t - t_k) > \varepsilon_{\text{target}}
    $$

    Solving for the maximum allowable interval:

    $$
    \delta t_{\max} = \frac{2\varepsilon_{\text{target}}}{|\Gamma_k|\,\sigma^2 S_k^2}
    $$

    With $\varepsilon_{\text{target}} = 0.05$, $\sigma = 0.20$, $S = 100$:

    $$
    \delta t_{\max} = \frac{2 \times 0.05}{|\Gamma_k| \times 0.04 \times 10000} = \frac{0.10}{400\,|\Gamma_k|}
    $$

    **At $\tau = 3$ months** ($\Gamma = 0.03$):

    $$
    \delta t_{\max} = \frac{0.10}{400 \times 0.03} = \frac{0.10}{12} \approx 0.00833 \text{ years} \approx 2.1 \text{ trading days}
    $$

    **At $\tau = 1$ day** ($\Gamma = 0.30$):

    $$
    \delta t_{\max} = \frac{0.10}{400 \times 0.30} = \frac{0.10}{120} \approx 0.000833 \text{ years} \approx 0.21 \text{ trading days} \approx 1.7 \text{ hours}
    $$

    **Comparison with uniform daily schedule** ($\delta t = 1/252 \approx 0.00397$ years):

    | Time to expiry | $\Gamma$ | $\delta t_{\max}$ | Uniform daily | Comparison |
    |:---|:---|:---|:---|:---|
    | 3 months | 0.03 | 2.1 days | 1 day | Adaptive allows longer intervals |
    | 1 day | 0.30 | 1.7 hours | 1 day | Adaptive requires much shorter intervals |

    When gamma is low (far from expiry), the adaptive rule permits less frequent rebalancing than daily, saving transaction costs. Near expiry, when gamma spikes, the adaptive rule demands sub-daily rebalancing to control the hedging error. A uniform daily schedule over-hedges early (wasting on transaction costs) and under-hedges near expiry (accepting too much error). The adaptive approach allocates rebalancing effort where it matters most.
