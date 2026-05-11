# Risk-Neutral vs Physical Measure

Stochastic volatility models distinguish between **physical (real-world)** dynamics and **risk-neutral** dynamics used for pricing. Understanding this distinction is essential for calibration, interpretation, and connecting option prices to market expectations. The gap between measures encodes the **volatility risk premium**.

---

## Two Probability Measures

### Physical Measure (P)

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

### Risk-Neutral Measure (Q)

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

## Discrepancies Between P and Q

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

---

## Exercises

**Exercise 1.** Under the physical measure $\mathbb{P}$, the Heston variance process has parameters $\kappa^{\mathbb{P}} = 1.5$ and $\theta^{\mathbb{P}} = 0.04$. The market price of volatility risk is $\lambda^V = \lambda\sqrt{V}$ with $\lambda = 2.0$, and $\xi = 0.3$. Compute the risk-neutral parameters $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$. Verify that $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$ and interpret this economically.

??? success "Solution to Exercise 1"
    Using the formulas $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$ and $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa^{\mathbb{Q}}$:

    $$
    \kappa^{\mathbb{Q}} = 1.5 + 2.0 \times 0.3 = 1.5 + 0.6 = 2.1
    $$

    $$
    \theta^{\mathbb{Q}} = \frac{1.5 \times 0.04}{2.1} = \frac{0.06}{2.1} \approx 0.02857
    $$

    Verification: $\kappa^{\mathbb{Q}} = 2.1 > 1.5 = \kappa^{\mathbb{P}}$ as expected.

    **Economic interpretation:** The faster mean reversion under $\mathbb{Q}$ reflects the volatility risk premium. Since investors are willing to pay a premium for protection against volatility spikes, the risk-neutral measure "prices in" a faster normalization of volatility. Under $\mathbb{Q}$, high-volatility states are expected to revert more quickly, which lowers the risk-neutral expected duration of volatility excursions.

    Note also that $\theta^{\mathbb{Q}} \approx 0.02857 < 0.04 = \theta^{\mathbb{P}}$, so the risk-neutral long-run variance is lower than the physical long-run variance. However, this does not contradict the empirical observation that implied variance often exceeds realized variance — the variance swap rate depends on the entire path distribution under $\mathbb{Q}$, not just $\theta^{\mathbb{Q}}$ alone.

---

**Exercise 2.** A variance swap with 3-month maturity has a swap rate of $(22\%)^2 = 0.0484$. Historical analysis estimates the expected realized variance under $\mathbb{P}$ to be $(18\%)^2 = 0.0324$. Compute the variance risk premium $VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]$ in both variance and volatility terms. If a trader sells the variance swap and realizes the expected variance, what is the annualized P&L?

??? success "Solution to Exercise 2"
    The variance risk premium is:

    $$
    \text{VRP} = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2] = 0.0484 - 0.0324 = 0.0160
    $$

    In variance terms, this is 1.60 percentage points (of variance).

    In volatility terms: $\sqrt{0.0484} = 22\%$ and $\sqrt{0.0324} = 18\%$, so the VRP in volatility terms is approximately $22\% - 18\% = 4\%$ (though this difference in standard deviations is not the same as the square root of the variance difference).

    If a trader sells the variance swap at the swap rate of 0.0484 and realized variance comes in at the expected 0.0324, the P&L is:

    $$
    \text{P\&L} = \text{Notional} \times (\text{Swap Rate} - \text{Realized Variance}) = \text{Notional} \times (0.0484 - 0.0324) = \text{Notional} \times 0.0160
    $$

    Per unit notional, the annualized P&L is 0.0160 (or 160 variance points). This represents the compensation the variance seller receives for bearing the risk that realized variance could exceed the swap rate. The positive VRP reflects the empirical regularity that implied variance systematically exceeds realized variance for equity indices.

---

**Exercise 3.** Explain why mixing $\mathbb{P}$-parameters with $\mathbb{Q}$-parameters leads to inconsistent dynamics. Specifically, suppose a practitioner calibrates $\kappa^{\mathbb{Q}} = 3.0$ and $\theta^{\mathbb{Q}} = 0.05$ from options, but uses $\kappa^{\mathbb{P}} = 1.5$ from time-series estimation as the mean-reversion speed in a Monte Carlo simulation for pricing. What error results, and how does it affect the term structure of implied volatility?

??? success "Solution to Exercise 3"
    The inconsistency arises because the drift of $V$ under the pricing measure should be $\kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - V)$, but the practitioner uses $\kappa^{\mathbb{P}} = 1.5$ instead of $\kappa^{\mathbb{Q}} = 3.0$ while keeping $\theta^{\mathbb{Q}} = 0.05$.

    Under the correct risk-neutral dynamics, the variance process mean-reverts with speed 3.0 to level 0.05. Using $\kappa^{\mathbb{P}} = 1.5$ instead makes variance revert **too slowly** under the pricing measure. This creates several errors:

    1. **Variance term structure:** The expected integrated variance $\mathbb{E}^{\mathbb{Q}}[\int_0^T V_s\,ds]$ depends on $\kappa^{\mathbb{Q}}$. With slower mean reversion, the current variance level $V_0$ has more persistent influence, distorting the variance term structure.

    2. **Implied volatility term structure:** The ATM implied volatility term structure is driven by the expected average variance. With $\kappa^{\mathbb{P}} < \kappa^{\mathbb{Q}}$, if $V_0 > \theta^{\mathbb{Q}}$, the model overestimates long-dated implied volatilities (variance stays elevated too long). If $V_0 < \theta^{\mathbb{Q}}$, it underestimates them (variance approaches $\theta^{\mathbb{Q}}$ too slowly).

    3. **Smile dynamics:** The term structure of skew is also affected, as slower mean reversion preserves the influence of the correlation parameter $\rho$ over longer horizons.

    The fundamental lesson is that all parameters used in a pricing model must be self-consistent under a single measure.

---

**Exercise 4.** The Radon–Nikodym derivative for the measure change is

$$
Z_T = \exp\!\left(-\int_0^T \lambda_t \cdot dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T |\lambda_t|^2\,dt\right)
$$

Show that $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$ (i.e., $Z_T$ defines a valid probability measure) by computing $d(\log Z_t)$ using Ito's lemma and verifying that $Z_t$ is a martingale under $\mathbb{P}$ when $\lambda$ satisfies the Novikov condition.

??? success "Solution to Exercise 4"
    We compute $d(\log Z_t)$ using Ito's lemma. Writing $Z_t = \mathcal{E}(-\lambda \cdot W^{\mathbb{P}})_t$ (the stochastic exponential), we have:

    $$
    Z_t = \exp\!\left(-\int_0^t \lambda_s \cdot dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^t |\lambda_s|^2\,ds\right)
    $$

    Let $L_t = -\int_0^t \lambda_s \cdot dW_s^{\mathbb{P}}$, which is a local martingale with $dL_t = -\lambda_t \cdot dW_t^{\mathbb{P}}$ and quadratic variation $d\langle L \rangle_t = |\lambda_t|^2\,dt$.

    Then $\log Z_t = L_t - \frac{1}{2}\langle L \rangle_t$, and by Ito's lemma applied to $Z_t = e^{\log Z_t}$:

    $$
    dZ_t = Z_t\,d(\log Z_t) + \frac{1}{2}Z_t\,d\langle \log Z \rangle_t
    $$

    Since $d(\log Z_t) = dL_t - \frac{1}{2}|\lambda_t|^2\,dt$ and $d\langle \log Z \rangle_t = |\lambda_t|^2\,dt$:

    $$
    dZ_t = Z_t\!\left(dL_t - \frac{1}{2}|\lambda_t|^2\,dt\right) + \frac{1}{2}Z_t\,|\lambda_t|^2\,dt = Z_t\,dL_t = -Z_t\,\lambda_t \cdot dW_t^{\mathbb{P}}
    $$

    This shows $Z_t$ satisfies $dZ_t = -Z_t\,\lambda_t \cdot dW_t^{\mathbb{P}}$, which is a driftless SDE — meaning $Z_t$ is a local martingale under $\mathbb{P}$.

    The **Novikov condition** states that if $\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T |\lambda_t|^2\,dt\right)\right] < \infty$, then $Z_t$ is a true martingale (not merely a local martingale). In that case:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_T] = Z_0 = 1
    $$

    Since $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$ and $Z_T \geq 0$, the measure $d\mathbb{Q} = Z_T\,d\mathbb{P}$ is a valid probability measure.

---

**Exercise 5.** A practitioner estimates from historical S&P 500 data that $\theta^{\mathbb{P}} \approx (16\%)^2$ and $\kappa^{\mathbb{P}} \approx 2.0$. From option calibration, she obtains $\theta^{\mathbb{Q}} \approx (19\%)^2$ and $\kappa^{\mathbb{Q}} \approx 3.2$, with $\xi = 0.4$. Using the relationship $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$, recover the risk premium parameter $\lambda$. Then verify consistency via $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa^{\mathbb{Q}}$. Is the recovered $\theta^{\mathbb{Q}}$ consistent? If not, what could explain the discrepancy?

??? success "Solution to Exercise 5"
    From $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$, we solve for $\lambda$:

    $$
    \lambda = \frac{\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}}}{\xi} = \frac{3.2 - 2.0}{0.4} = 3.0
    $$

    Now verify via $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa^{\mathbb{Q}}$:

    $$
    \theta^{\mathbb{Q}}_{\text{predicted}} = \frac{2.0 \times (0.16)^2}{3.2} = \frac{2.0 \times 0.0256}{3.2} = \frac{0.0512}{3.2} = 0.0160
    $$

    However, the option-calibrated value is $\theta^{\mathbb{Q}} = (0.19)^2 = 0.0361$.

    The predicted value (0.0160) is much smaller than the calibrated value (0.0361), so there is an **inconsistency**.

    Possible explanations for the discrepancy include:

    1. **The proportional specification $\lambda^V = \lambda\sqrt{V}$ may be too restrictive.** A more general risk premium, such as $\lambda^V = \lambda_0 + \lambda_1 V$, would allow independent adjustment of $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$.

    2. **Estimation error:** The physical parameters are estimated from noisy historical data, and the risk-neutral parameters are calibrated to a specific option cross-section. Sampling uncertainty in either set can produce apparent inconsistency.

    3. **Model misspecification:** The Heston model may not perfectly describe the data, so parameters estimated under different data sources may not satisfy the theoretical constraints.

---

**Exercise 6.** Consider joint estimation of $\mathbb{P}$ and $\mathbb{Q}$ parameters. You have two data sources: (a) a time series of 2000 daily returns, and (b) a cross-section of 50 option prices observed on a single day. Which data source primarily identifies each of the following: $\kappa^{\mathbb{P}}$, $\theta^{\mathbb{P}}$, $\kappa^{\mathbb{Q}}$, $\theta^{\mathbb{Q}}$, $\xi$, $\rho$, $V_0$? Explain which parameters are identifiable from options alone and which require historical data.

??? success "Solution to Exercise 6"
    The parameters are identified as follows:

    **From options alone (cross-section of 50 option prices):**

    - $\kappa^{\mathbb{Q}}$: Identified from the term structure of implied volatility (how quickly the smile flattens with maturity)
    - $\theta^{\mathbb{Q}}$: Identified from long-dated option levels (the asymptotic implied variance for large $T$)
    - $\xi$: Identified from the curvature (convexity) of the smile, since vol-of-vol is the same under both measures
    - $\rho$: Identified from the skew of the smile, since correlation is unchanged by measure change
    - $V_0$: Identified from the ATM implied volatility level at the shortest maturity

    **Requiring historical data (time series of 2000 daily returns):**

    - $\kappa^{\mathbb{P}}$: Identified from the autocorrelation decay of realized variance
    - $\theta^{\mathbb{P}}$: Identified from the long-run average of realized variance

    The parameters $\xi$, $\rho$, and $V_0$ are identifiable from either data source since they are invariant under measure change. In practice, options provide more precise estimates of $\xi$ and $\rho$ because the smile is highly sensitive to these parameters.

    The risk premium parameter $\lambda$ requires **both** data sources: it is defined by $\lambda = (\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}})/\xi$, combining option-implied and time-series information.

---

**Exercise 7.** The market price of equity risk is $\lambda^S = (\mu^{\mathbb{P}} - (r-q))/\sqrt{V}$. For a stock with $\mu^{\mathbb{P}} = 8\%$, $r = 4\%$, $q = 2\%$, and current instantaneous variance $V_0 = (20\%)^2 = 0.04$, compute $\lambda^S$. Explain why $\lambda^S$ is uniquely determined by no-arbitrage (the asset is traded), whereas $\lambda^V$ is not. What would happen to $\lambda^S$ during a high-volatility regime with $V = (40\%)^2$?

??? success "Solution to Exercise 7"
    Computing the market price of equity risk:

    $$
    \lambda^S = \frac{\mu^{\mathbb{P}} - (r - q)}{\sqrt{V}} = \frac{0.08 - (0.04 - 0.02)}{\sqrt{0.04}} = \frac{0.08 - 0.02}{0.20} = \frac{0.06}{0.20} = 0.30
    $$

    **Why $\lambda^S$ is uniquely determined:** The stock $S$ is a traded asset, so the no-arbitrage condition uniquely pins down its risk-neutral drift as $r - q$. The formula $\mu^{\mathbb{Q}} = \mu^{\mathbb{P}} - \lambda^S\sqrt{V} = r - q$ has a unique solution for $\lambda^S$. In contrast, volatility $V$ is not directly traded, so there is no analogous no-arbitrage constraint on $\lambda^V$. Different choices of $\lambda^V$ correspond to different equivalent martingale measures, all consistent with no-arbitrage — this is the manifestation of market incompleteness.

    **High-volatility regime with $V = (40\%)^2 = 0.16$:**

    $$
    \lambda^S = \frac{0.06}{\sqrt{0.16}} = \frac{0.06}{0.40} = 0.15
    $$

    The market price of equity risk **halves** from 0.30 to 0.15. This is because $\lambda^S = (\text{excess return})/\sqrt{V}$, and if the excess return $\mu^{\mathbb{P}} - (r-q)$ remains constant while volatility doubles, the Sharpe-like ratio decreases. In reality, $\mu^{\mathbb{P}}$ may also increase during high-volatility regimes (higher expected returns as compensation for risk), partially offsetting this decline.
