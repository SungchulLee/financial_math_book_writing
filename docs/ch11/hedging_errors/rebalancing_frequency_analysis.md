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
