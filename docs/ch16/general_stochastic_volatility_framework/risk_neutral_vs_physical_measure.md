# Risk-Neutral vs Physical Measure

Stochastic volatility models distinguish between **physical (real-world)** dynamics and **risk-neutral** dynamics used for pricing. Understanding this distinction is essential for calibration, interpretation, and connecting option prices to market expectations. The gap between measures encodes the **volatility risk premium**.

---

## Two Probability Measures

### Physical Measure ($\mathbb{P}$)

The **physical** or **real-world** measure governs actual asset evolution:

$$
\begin{aligned}
dS_t &= \mu^{\mathbb{P}} S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{S,\mathbb{P}} \\
dV_t &= a^{\mathbb{P}}(V_t)\,dt + b(V_t)\,dW_t^{V,\mathbb{P}}
\end{aligned}
$$

Under $\mathbb{P}$:
- $\mu^{\mathbb{P}}$ reflects the expected return on the asset
- $a^{\mathbb{P}}(V)$ reflects how volatility actually evolves
- This is the measure relevant for **forecasting** and **risk management**

### Risk-Neutral Measure ($\mathbb{Q}$)

The **risk-neutral** or **pricing** measure is constructed for derivative valuation:

$$
\begin{aligned}
dS_t &= (r - q) S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{S,\mathbb{Q}} \\
dV_t &= a^{\mathbb{Q}}(V_t)\,dt + b(V_t)\,dW_t^{V,\mathbb{Q}}
\end{aligned}
$$

Under $\mathbb{Q}$:
- The drift of $S$ is the risk-free rate minus dividends (no-arbitrage)
- Option prices are computed as discounted expectations
- This is the measure relevant for **pricing** and **calibration**

### Key Principle

**Option prices identify $\mathbb{Q}$-dynamics only.** They do not directly reveal $\mathbb{P}$-dynamics.

---

## Measure Change via Girsanov

### The Radon–Nikodym Derivative

The change from $\mathbb{P}$ to $\mathbb{Q}$ is characterized by a **Radon–Nikodym derivative**:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T = \exp\left(-\int_0^T \lambda_t \cdot dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T |\lambda_t|^2\,dt\right)
$$

where $\lambda_t = (\lambda_t^S, \lambda_t^V)^{\top}$ is the **market price of risk** vector.

### Girsanov Transformation

Under $\mathbb{Q}$, the Brownian motions transform as:

$$
\begin{aligned}
dW_t^{S,\mathbb{Q}} &= dW_t^{S,\mathbb{P}} + \lambda_t^S\,dt \\
dW_t^{V,\mathbb{Q}} &= dW_t^{V,\mathbb{P}} + \lambda_t^V\,dt
\end{aligned}
$$

**Crucially:** The diffusion coefficients are unchanged. Only drifts are modified.

### Drift Modification

For the asset price:
$$
\mu^{\mathbb{Q}} = \mu^{\mathbb{P}} - \lambda^S \sqrt{V} = r - q
$$

This determines the market price of equity risk:
$$
\lambda^S = \frac{\mu^{\mathbb{P}} - (r - q)}{\sqrt{V}}
$$

For the variance process:
$$
a^{\mathbb{Q}}(V) = a^{\mathbb{P}}(V) - \lambda^V b(V)
$$

---

## Market Price of Volatility Risk

### Definition

The **market price of volatility risk** $\lambda^V$ captures compensation for bearing volatility uncertainty:

$$
\lambda^V = \frac{a^{\mathbb{P}}(V) - a^{\mathbb{Q}}(V)}{b(V)}
$$

This quantity is:
- **Not determined by no-arbitrage** (volatility is non-traded)
- **Estimated from data** or **implied from options**
- **Model-dependent** in its functional form

### Common Specifications

**Constant:** $\lambda^V = \lambda_0$

Simple but may not match data well.

**Proportional to $\sqrt{V}$:** $\lambda^V = \lambda_0 \sqrt{V}$

Common in affine models; preserves affine structure.

**General affine:** $\lambda^V = \lambda_0 + \lambda_1 V$

More flexible; still tractable.

### Heston Model Example

Under $\mathbb{P}$:
$$
dV_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{P}}
$$

Under $\mathbb{Q}$ with $\lambda^V = \lambda \sqrt{V}$:
$$
dV_t = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{Q}}
$$

where:
$$
\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda\xi}
$$

**Observation:** Different $(\kappa, \theta)$ values across measures reflect the volatility risk premium.

---

## The Volatility Risk Premium

### Definition and Sign

The **volatility risk premium (VRP)** is typically defined as:

$$
\text{VRP} = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]
$$

or equivalently in terms of variance swap rates vs. realized variance.

**Empirical finding:** VRP is typically **positive** for equity indices:
- Implied variance exceeds realized variance on average
- Sellers of variance earn positive returns
- This compensates for volatility's tendency to spike during market stress

### Quantitative Estimates

| Market | VRP (annualized) | Sharpe ratio |
|--------|------------------|--------------|
| S&P 500 | 2%–5% | 0.5–1.0 |
| Euro Stoxx 50 | 2%–4% | 0.4–0.8 |
| Individual stocks | 1%–3% | 0.3–0.6 |

### Economic Interpretation

The positive VRP reflects:

1. **Jump risk:** Volatility spikes during crashes; protection is valuable
2. **Correlation with wealth:** High volatility coincides with portfolio losses
3. **Risk aversion:** Investors dislike uncertainty about uncertainty
4. **Hedging demand:** Institutional demand for downside protection

---

## Calibration Implications

### What Option Calibration Recovers

Fitting a stochastic volatility model to option prices yields **risk-neutral parameters**:

| Parameter | Recovered from options |
|-----------|----------------------|
| $\kappa^{\mathbb{Q}}$ | Risk-neutral mean reversion |
| $\theta^{\mathbb{Q}}$ | Risk-neutral long-run variance |
| $\xi$ | Vol-of-vol (same under both measures) |
| $\rho$ | Correlation (same under both measures) |
| $V_0$ | Current variance (same) |

### What Time-Series Estimation Recovers

Estimating from historical data (realized variance, returns) yields **physical parameters**:

| Parameter | Recovered from data |
|-----------|-------------------|
| $\kappa^{\mathbb{P}}$ | Physical mean reversion |
| $\theta^{\mathbb{P}}$ | Physical long-run variance |
| $\xi$ | Vol-of-vol |
| $\rho$ | Correlation |

### The Mixing Problem

**Danger:** Using $\kappa^{\mathbb{P}}$ from time series with $\theta^{\mathbb{Q}}$ from options creates:
- Inconsistent dynamics
- Incorrect risk-neutral expectations
- Poor hedging performance

**Solution:** Either:
1. Use only option-implied ($\mathbb{Q}$) parameters for pricing
2. Explicitly model the risk premium to connect $\mathbb{P}$ and $\mathbb{Q}$
3. Joint estimation using both options and returns

---

## Discrepancies Between $\mathbb{P}$ and $\mathbb{Q}$

### Mean Reversion Speed

Typically: $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$

**Interpretation:** Under $\mathbb{Q}$, volatility mean-reverts faster. This occurs because:
- The risk premium $\lambda > 0$ adds to mean reversion
- Markets "price in" faster normalization of volatility spikes

### Long-Run Variance

Typically: $\theta^{\mathbb{Q}} > \theta^{\mathbb{P}}$ or ambiguous

**Interpretation:** Risk-neutral long-run variance may exceed realized long-run variance, reflecting the premium for bearing volatility risk.

### Implied vs. Realized Comparison

The **variance swap rate** (traded at zero cost) satisfies:

$$
\text{VS Rate} = \mathbb{E}^{\mathbb{Q}}\left[\frac{1}{T}\int_0^T V_s\,ds\right]
$$

The **realized variance** satisfies:

$$
\text{RV} = \frac{1}{T}\int_0^T V_s\,ds \quad \text{(realized path)}
$$

**VRP = VS Rate $-$ $\mathbb{E}^{\mathbb{P}}[\text{RV}]$** is persistently positive.

---

## Joint Modeling Approaches

### Separate Estimation

**Step 1:** Estimate $\mathbb{P}$-parameters from historical data
**Step 2:** Estimate $\mathbb{Q}$-parameters from option prices
**Step 3:** Infer risk premium parameters from the difference

**Advantage:** Uses all available data
**Disadvantage:** May find inconsistent parameters; requires care

### Joint Maximum Likelihood

Simultaneously estimate $(\theta^{\mathbb{P}}, \theta^{\mathbb{Q}}, \lambda)$ using:
- Return data (contributes to $\mathbb{P}$-likelihood)
- Option prices (contributes to $\mathbb{Q}$-likelihood)

**Eraker, Johannes, Polson (2003):** MCMC approach for joint estimation.

### Bayesian Approaches

Place priors on risk premium parameters and update with data:
- Natural framework for uncertainty quantification
- Can incorporate economic constraints
- Computationally intensive

---

## Practical Recommendations

### For Pricing and Calibration

1. **Use $\mathbb{Q}$-parameters exclusively** from option calibration
2. **Do not mix** time-series estimates with option-implied values
3. **Recognize** that calibrated parameters are risk-neutral, not forecasts

### For Risk Management

1. **Physical measure matters** for VaR, expected shortfall
2. **Model the risk premium** explicitly if using option-implied inputs
3. **Stress test** under both measures

### For Model Validation

1. **Compare** option-implied and realized variance time series
2. **Check** whether $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$ (expected ordering)
3. **Monitor** stability of estimated risk premium

---

## Key Takeaways

- Pricing uses $\mathbb{Q}$; forecasting uses $\mathbb{P}$
- Girsanov theorem changes drifts, not diffusions
- The volatility risk premium is positive for equities (sellers of vol earn returns)
- Option calibration recovers $\mathbb{Q}$-parameters only
- Mixing $\mathbb{P}$ and $\mathbb{Q}$ parameters leads to inconsistency
- The gap $\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}} = \lambda\xi$ encodes the risk premium

---

## Further Reading

- Duffie, D. (2001). *Dynamic Asset Pricing Theory*, 3rd ed. Princeton University Press.
- Bollerslev, T., Tauchen, G., & Zhou, H. (2009). *Expected stock returns and variance risk premia*. Review of Financial Studies.
- Eraker, B., Johannes, M., & Polson, N. (2003). *The impact of jumps in volatility and returns*. Journal of Finance.
- Carr, P. & Wu, L. (2009). *Variance risk premiums*. Review of Financial Studies.
- Andersen, T.G. & Piterbarg, V. (2007). *Moment explosions in stochastic volatility models*. Finance and Stochastics.
- Fouque, J.-P., Papanicolaou, G., Sircar, R., & Sølna, K. (2011). *Multiscale Stochastic Volatility for Equity, Interest Rate, and Credit Derivatives*. Cambridge University Press.
