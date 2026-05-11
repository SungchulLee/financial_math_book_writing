# Potential Future Exposure (PFE)

**Potential Future Exposure (PFE)** measures the worst-case exposure at a given confidence level. It complements Expected Exposure by focusing on tail risk rather than average exposure.

---

## Definition

For confidence level $\alpha \in (0,1)$, the Potential Future Exposure at time $t$ is:

$$
\text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(E_t \le x) \ge \alpha\} = F_{E_t}^{-1}(\alpha)
$$

where $E_t = V_t^+$ is the exposure and $F_{E_t}$ is its cumulative distribution function.

**Interpretation:** With probability $\alpha$, exposure at time $t$ will not exceed $\text{PFE}_\alpha(t)$.

---

## Standard Confidence Levels

| Confidence Level | Use Case |
|-----------------|----------|
| 95% | Internal risk management |
| 97.5% | Regulatory (Basel) |
| 99% | Conservative limits |

A statement like "the 95% PFE at 1 year is \$20 million" means there is only a 5% chance that exposure exceeds \$20 million at the 1-year point.

---

## PFE Profile

The **PFE profile** plots $\text{PFE}_\alpha(t)$ as a function of time:

$$
t \mapsto \text{PFE}_\alpha(t), \quad t \in [0, T]
$$

**Characteristics:**

- Always non-negative
- Typically exceeds EE profile
- Shape depends on product type and volatility

---

## Relation to Expected Exposure

**Hierarchy:**

$$
\text{EE}(t) \le \text{PFE}_\alpha(t) \quad \text{for } \alpha > 0.5
$$

The gap between PFE and EE reflects the **skewness and tail thickness** of the exposure distribution.

**Ratio:**

$$
\frac{\text{PFE}_\alpha(t)}{\text{EE}(t)}
$$

This ratio is often 2-4× for typical derivatives portfolios.

---

## PFE Under Normality

If the portfolio value $V_t$ is normally distributed:

$$
V_t \sim N(\mu_t, \sigma_t^2)
$$

Then exposure $E_t = V_t^+$ has:

$$
\text{EE}(t) = \mu_t \Phi\left(\frac{\mu_t}{\sigma_t}\right) + \sigma_t \phi\left(\frac{\mu_t}{\sigma_t}\right)
$$

$$
\text{PFE}_\alpha(t) = \max\left(\mu_t + \sigma_t \Phi^{-1}\left(\frac{\alpha - \Phi(-\mu_t/\sigma_t)}{1 - \Phi(-\mu_t/\sigma_t)}\right), 0\right)
$$

**Approximation for small $\mu_t$:**

$$
\text{PFE}_\alpha(t) \approx \sigma_t \Phi^{-1}(\alpha)
$$

---

## Peak PFE

The **Peak PFE** is the maximum PFE over the portfolio's lifetime:

$$
\text{Peak PFE}_\alpha = \max_{t \in [0,T]} \text{PFE}_\alpha(t)
$$

**Uses:**

- Credit limit approval
- Counterparty exposure limits
- Stress testing benchmarks

---

## PFE for Different Products

### Interest Rate Swap

- Hump-shaped profile (peaks mid-life)
- Peak PFE typically at 30-50% of tenor
- Declines toward maturity (pull-to-par)

**Example:** 10-year receiver swap

- Peak PFE at ~5 years
- PFE at maturity ≈ 0

### FX Forward

- Monotonically increasing profile
- Maximum at maturity
- Linear growth approximately

**Scaling:**

$$
\text{PFE}_\alpha(t) \propto \sigma_{\text{FX}} \sqrt{t}
$$

### Options

- Buyer: PFE follows option value dynamics
- Seller: Zero PFE (after premium received)

---

## Monte Carlo Estimation

### Algorithm

1. Simulate $N$ paths of risk factors
2. For each path $j$ and time $t$, compute exposure $E_t^{(j)} = V_t^{(j)+}$
3. For each time $t$, sort exposures: $E_t^{(1)} \le E_t^{(2)} \le \cdots \le E_t^{(N)}$
4. Estimate PFE as the empirical quantile:

$$
\widehat{\text{PFE}}_\alpha(t) = E_t^{(\lceil N\alpha \rceil)}
$$

### Confidence Interval

The standard error of the PFE estimate is approximately:

$$
\text{SE}(\widehat{\text{PFE}}_\alpha) \approx \frac{\sqrt{\alpha(1-\alpha)}}{f_{E_t}(\text{PFE}_\alpha) \sqrt{N}}
$$

where $f_{E_t}$ is the density of exposure.

**Implication:** PFE estimates have higher variance than EE estimates because they depend on tail observations.

---

## Non-Additivity of PFE

**Critical property:** PFE is **not additive** across portfolios:

$$
\text{PFE}_\alpha(A + B) \ne \text{PFE}_\alpha(A) + \text{PFE}_\alpha(B)
$$

In general:

$$
\text{PFE}_\alpha(A + B) \le \text{PFE}_\alpha(A) + \text{PFE}_\alpha(B)
$$

with equality only for perfectly correlated exposures.

**Implication:** 

- Cannot simply sum PFEs across counterparties
- Netting benefits apply to PFE
- Diversification reduces portfolio PFE

---

## PFE and Credit Limits

### Limit Framework

$$
\text{PFE}_\alpha(\text{Counterparty}) \le \text{Credit Limit}
$$

Credit limits are set based on:

- Counterparty creditworthiness
- Internal risk appetite
- Regulatory requirements

### Pre-Deal Check

Before executing a trade:

1. Compute incremental PFE
2. Check against available limit
3. Approve or reject

$$
\text{Available Limit} = \text{Total Limit} - \text{Current PFE}
$$

---

## Marginal PFE

The **marginal PFE** of a new trade measures its incremental impact:

$$
\Delta \text{PFE} = \text{PFE}_\alpha(\text{Portfolio} + \text{New Trade}) - \text{PFE}_\alpha(\text{Portfolio})
$$

**Properties:**

- Can be negative (diversification benefit)
- Depends on correlation with existing portfolio
- Used for trade-level limit allocation

---

## PFE with Collateral

Under a collateral agreement with threshold $H$:

$$
E_t^{\text{coll}} = \max(V_t - C_{t-\Delta}, 0)
$$

where $\Delta$ is the margin period of risk (MPOR).

**Collateralized PFE:**

$$
\text{PFE}_\alpha^{\text{coll}}(t) = \text{Quantile}_\alpha(E_t^{\text{coll}})
$$

**Effect:** Collateral significantly reduces PFE but:

- MPOR creates residual exposure
- Threshold $H$ creates a floor
- Collateral disputes can increase effective MPOR

---

## Wrong-Way Risk and PFE

When exposure and default probability are correlated:

$$
\text{PFE}^{\text{WWR}}_\alpha(t) > \text{PFE}_\alpha(t)
$$

**Treatment:**

- Stressed PFE calculations
- Explicit correlation modeling
- Conservative add-ons

See [Wrong-Way Risk](wrong_way_risk.md) for details.

---

## Regulatory Use of PFE

### Basel SA-CCR

The Standardized Approach for CCR uses PFE concepts:

$$
\text{EAD} = \alpha \times (\text{RC} + \text{PFE})
$$

where:

- EAD = Exposure at Default
- RC = Replacement Cost
- PFE = Potential Future Exposure (add-on)
- $\alpha = 1.4$ (regulatory multiplier)

### Internal Models Method (IMM)

Advanced banks can use internal PFE models:

- Subject to regulatory approval
- Backtesting requirements
- Capital multipliers

---

## Backtesting PFE

### Methodology

Compare realized exposures to predicted PFE:

1. At time $t_0$, compute $\text{PFE}_\alpha(t_0 + h)$ for horizon $h$
2. At time $t_0 + h$, observe realized exposure $E_{t_0+h}$
3. Count exceedances: $\mathbf{1}_{E_{t_0+h} > \text{PFE}_\alpha(t_0+h)}$

**Expected exceedance rate:** $1 - \alpha$

### Statistical Test

Under correct model, exceedances follow Binomial$(n, 1-\alpha)$.

Test statistic:

$$
Z = \frac{\hat{p} - (1-\alpha)}{\sqrt{(1-\alpha)\alpha/n}}
$$

where $\hat{p}$ is the observed exceedance rate.

---

## Key Takeaways

- PFE is the $\alpha$-quantile of future exposure distribution
- It measures tail exposure, complementing average exposure (EE)
- PFE is non-additive—cannot sum across portfolios
- Peak PFE is used for credit limit setting
- Collateral reduces PFE but MPOR creates residual risk
- Monte Carlo simulation is the standard estimation method
- PFE estimates have higher variance than EE estimates

---

## Further Reading

- Basel Committee, "The Standardised Approach for Measuring Counterparty Credit Risk Exposures (SA-CCR)"
- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Pykhtin, M. (2009), "Modeling Credit Exposure for Collateralized Counterparties"
- Glasserman, P. & Yang, L. (2016), "Bounding Wrong-Way Risk in CVA Calculation"

---

## Exercises

**Exercise 1.** Define Potential Future Exposure (PFE) at confidence level $\alpha$ and time $t$: $\text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(V_t^+ \le x) \ge \alpha\}$. For a portfolio whose positive exposure follows a lognormal distribution with mean \$5M and volatility 40%, compute the 97.5% PFE at $t = 1$ year.

??? success "Solution to Exercise 1"
    **Definition:** The Potential Future Exposure at confidence level $\alpha$ and time $t$ is:

    $$
    \text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(V_t^+ \le x) \ge \alpha\}
    $$

    This is the $\alpha$-quantile of the exposure distribution at time $t$.

    **Computation for lognormal exposure:**

    We are told the positive exposure follows a lognormal distribution with mean $\mu_E = \$5$M and volatility (coefficient of variation) of 40%. For a lognormal random variable $E$ with $\mathbb{E}[E] = \mu_E$ and relative volatility $\sigma_{\text{rel}} = 0.40$, we need to find the parameters of the underlying normal distribution.

    If $E = e^X$ where $X \sim N(m, s^2)$, then:

    $$
    \mathbb{E}[E] = e^{m + s^2/2} = \mu_E = 5
    $$

    The variance of the lognormal is:

    $$
    \text{Var}(E) = \mu_E^2(e^{s^2} - 1)
    $$

    The "volatility 40%" means $\sigma_E / \mu_E = 0.40$, so:

    $$
    e^{s^2} - 1 = (0.40)^2 = 0.16 \implies s^2 = \ln(1.16) \approx 0.14842
    $$

    $$
    s \approx 0.3853
    $$

    From the mean condition:

    $$
    m = \ln(\mu_E) - s^2/2 = \ln(5) - 0.07421 \approx 1.6094 - 0.0742 = 1.5352
    $$

    The 97.5% quantile of the lognormal distribution is:

    $$
    \text{PFE}_{97.5\%} = e^{m + s \cdot \Phi^{-1}(0.975)}
    $$

    where $\Phi^{-1}(0.975) = 1.960$. Therefore:

    $$
    \text{PFE}_{97.5\%} = e^{1.5352 + 0.3853 \times 1.960} = e^{1.5352 + 0.7552} = e^{2.2904}
    $$

    $$
    \text{PFE}_{97.5\%} \approx 9.88 \text{ million}
    $$

    **Interpretation:** There is only a 2.5% probability that the exposure at $t = 1$ year exceeds approximately \$9.88M. This is roughly twice the expected exposure of \$5M, which is typical for the PFE/EE ratio.

    **Note:** The exact answer depends on the interpretation of "volatility 40%." If instead this means $s = 0.40$ (the volatility parameter of the lognormal), then $m = \ln(5) - 0.08 = 1.5294$, and:

    $$
    \text{PFE}_{97.5\%} = e^{1.5294 + 0.40 \times 1.960} = e^{1.5294 + 0.784} = e^{2.3134} \approx 10.11\text{M}
    $$

---

**Exercise 2.** Explain the difference between PFE and Expected Exposure (EE). A risk manager uses PFE for setting counterparty credit limits and EE for CVA calculations. Justify why each measure is appropriate for its respective purpose.

??? success "Solution to Exercise 2"
    **PFE** and **EE** are both forward-looking measures of counterparty credit exposure, but they capture fundamentally different aspects of the exposure distribution.

    **Expected Exposure (EE):** The mean of the exposure distribution at time $t$:

    $$
    \text{EE}(t) = \mathbb{E}[V_t^+]
    $$

    EE captures the **average** exposure — the central tendency of what the bank expects to lose if default occurs at time $t$. It reflects the typical scenario, not the worst case.

    **Potential Future Exposure (PFE):** The $\alpha$-quantile of the exposure distribution:

    $$
    \text{PFE}_\alpha(t) = F_{E_t}^{-1}(\alpha)
    $$

    PFE captures **tail risk** — the exposure level that is exceeded only with probability $1-\alpha$. At $\alpha = 97.5\%$, it reflects a scenario that is worse than 97.5% of all possible outcomes.

    **Why EE is appropriate for CVA:**

    CVA is the **expected loss** from counterparty default, computed as:

    $$
    \text{CVA} = \text{LGD}\int_0^T \text{EE}(t) \cdot dPD(t)
    $$

    As a fair-value pricing adjustment, CVA should reflect the **expected cost** of counterparty default risk. Using the mean (EE) is appropriate because:

    - CVA is a risk-neutral expectation — it prices the average outcome across all scenarios
    - It is additive across time periods and (approximately) across counterparties
    - It represents the cost of hedging the counterparty risk in the market

    Using PFE would overstate CVA because it would price the credit risk at a worst-case level rather than the expected level.

    **Why PFE is appropriate for credit limits:**

    Credit limits control the **maximum potential loss** to a counterparty. A risk manager needs to ensure that even in adverse scenarios, the bank's exposure does not exceed its risk appetite. PFE is appropriate because:

    - It captures the tail of the exposure distribution, providing a conservative bound
    - It answers: "How much could we lose in a bad scenario?" — the right question for limit-setting
    - Peak PFE ($\max_t \text{PFE}_\alpha(t)$) gives the worst-case exposure over the trade's life
    - It is analogous to VaR for market risk, providing a threshold-based risk measure

    Using EE for credit limits would be dangerously unconservative: the average exposure may be \$5M while the 99% PFE is \$15M, and the bank needs to be prepared for the latter.

---

**Exercise 3.** Sketch the PFE profile of a 10-year interest rate swap at the 97.5% confidence level. Explain why the PFE profile is "hump-shaped" and peaks at roughly 30--50% of the swap's life.

??? success "Solution to Exercise 3"
    **PFE profile shape for a 10-year IRS at 97.5%:**

    The PFE profile has a **hump shape** similar to the EE profile but amplified. It starts near zero, rises to a peak at roughly 30--50% of the swap's life (3--5 years for a 10-year swap), then declines back toward zero at maturity.

    The qualitative sketch would show:

    - At $t = 0$: PFE $\approx 0$ (swap is at par, no rate movement yet)
    - Rising phase ($0 < t < 4$ years): PFE increases as rate uncertainty grows
    - Peak at $t \approx 3$--$5$ years: maximum PFE
    - Declining phase ($4 < t < 10$ years): PFE decreases as remaining cash flows shrink
    - At $t = 10$ years: PFE $= 0$ (swap has expired)

    **Why the hump shape and peak location:**

    The PFE at confidence level $\alpha$ is approximately:

    $$
    \text{PFE}_\alpha(t) \approx \Phi^{-1}(\alpha) \cdot \sigma_{\text{swap}} \cdot \sqrt{t} \cdot \frac{T - t}{T}
    $$

    This is proportional to the EE profile (with a scaling factor $\Phi^{-1}(\alpha)/\phi(0)$), so it has the same hump shape driven by the same two competing effects:

    1. **Diffusion effect** ($\sqrt{t}$): Interest rate uncertainty grows with the square root of time. Under typical rate models, the standard deviation of the swap rate change is $\sigma\sqrt{t}$. This increases PFE because the $\alpha$-quantile of the swap value distribution widens.

    2. **Amortization effect** ($(T-t)/T$): As coupons are paid, the remaining notional (in DV01 terms) decreases. A rate movement of the same magnitude produces a smaller NPV impact when fewer cash flows remain. At maturity, only the final coupon remains, and the PFE is essentially zero.

    **Why the peak is at 30--50% of the swap's life:**

    The peak of $\sqrt{t}(T-t)$ occurs at $t^* = T/3 \approx 3.3$ years. In practice, discrete coupon effects, mean reversion in the rate model, and the exact confidence level shift the peak to $t \approx 3$--$5$ years. The PFE peak tends to occur slightly later than the EE peak because the quantile scaling factor $\Phi^{-1}(\alpha)$ amplifies the right tail more when the distribution is wider (larger $t$), and the skewness of the rate distribution can shift the quantile relative to the mean.

    **PFE vs EE ratio:** At the peak, $\text{PFE}_{97.5\%}/\text{EE} \approx \Phi^{-1}(0.975)/\phi(0) \approx 1.96/0.399 \approx 4.9$ under normality assumptions. In practice, this ratio is typically 2--4$\times$ due to the positive mass at zero in the exposure distribution.

---

**Exercise 4.** A bank sets a counterparty credit limit of \$50M based on peak PFE. The current portfolio's peak PFE is \$45M. A new trade would add \$8M to the peak PFE. Should the bank enter the trade? What options are available (e.g., netting, collateral, restructuring)?

??? success "Solution to Exercise 4"
    **Current situation:**

    - Counterparty credit limit: \$50M (based on peak PFE)
    - Current portfolio peak PFE: \$45M
    - New trade incremental peak PFE: \$8M
    - Post-trade peak PFE: \$45M + \$8M = \$53M (assuming worst case of additive PFE)

    **Should the bank enter the trade?**

    Under a strict limit framework, the answer is **no**. The post-trade peak PFE of \$53M exceeds the \$50M credit limit. The available limit is:

    $$
    \text{Available Limit} = \$50\text{M} - \$45\text{M} = \$5\text{M}
    $$

    The incremental PFE of \$8M exceeds the available limit of \$5M.

    However, this analysis is conservative because it assumes PFE is additive ($\text{PFE}(A+B) = \text{PFE}(A) + \text{PFE}(B)$). In reality, PFE is sub-additive due to diversification:

    $$
    \text{PFE}_\alpha(\text{Portfolio} + \text{New Trade}) \le \text{PFE}_\alpha(\text{Portfolio}) + \text{PFE}_\alpha(\text{New Trade})
    $$

    If the new trade partially offsets existing positions (e.g., opposite direction), the **marginal PFE** could be less than \$8M or even negative. The bank should compute:

    $$
    \Delta\text{PFE} = \text{PFE}_\alpha(\text{Portfolio} + \text{New}) - \text{PFE}_\alpha(\text{Portfolio})
    $$

    If $\Delta\text{PFE} \le \$5$M, the trade can be approved.

    **Options available if the limit is breached:**

    1. **Netting:** Ensure the new trade is under the same ISDA Master Agreement / netting set. If the new trade offsets existing positions, the marginal PFE may be within limits.

    2. **Collateral (CSA):** Negotiate or amend the Credit Support Annex to include collateral with a low threshold. Collateralization can reduce PFE dramatically (e.g., by 70--90%). With daily margining and zero threshold, the PFE is limited to the margin-period-of-risk exposure.

    3. **Restructuring the trade:** Modify trade terms to reduce exposure:
        - Add break clauses (mandatory early termination)
        - Reduce notional
        - Shorten maturity
        - Add reset features that periodically settle the mark-to-market

    4. **Limit increase:** If the counterparty is creditworthy and the bank's risk appetite allows, request a limit increase from credit risk management, supported by analysis of the netting benefit and collateral.

    5. **Trade compression:** Terminate or novate existing offsetting trades to free up PFE limit before entering the new trade.

    6. **Central clearing:** Move eligible trades to a CCP, which typically reduces bilateral PFE and may free up limit.

---

**Exercise 5.** Explain how collateral agreements affect the PFE profile. If a CSA with daily margining and a \$0 threshold is in place, describe qualitatively how the PFE profile changes compared to an uncollateralized portfolio. Why does the Margin Period of Risk determine the residual PFE?

??? success "Solution to Exercise 5"
    **How collateral agreements affect the PFE profile:**

    Without collateral, the PFE profile of a derivative portfolio follows the natural exposure dynamics — for an IRS, this is the familiar hump shape peaking at 30--50% of the tenor. The PFE grows with market factor diffusion and can reach significant levels.

    With a CSA specifying daily margining and a \$0 threshold:

    - **Variation margin (VM)** is exchanged daily based on the mark-to-market value
    - The collateral $C_t$ closely tracks the portfolio value $V_t$
    - At any point, the exposure is approximately $E_t \approx (V_t - C_t)^+$

    Under **perfect** (instantaneous, continuous) margining with zero threshold, $C_t = V_t^+$ and $E_t = 0$ always. The PFE profile would be identically zero.

    **In reality, the PFE profile changes dramatically but is not zero:**

    The collateralized PFE profile is:

    - **Much lower** than the uncollateralized profile (typically reduced by 80--95%)
    - **Approximately flat** over time (rather than hump-shaped), because the residual exposure depends primarily on short-horizon volatility, not on the long-term diffusion
    - Determined by the **Margin Period of Risk (MPOR)** rather than by the full tenor of the trade

    **Why the MPOR determines residual PFE:**

    The MPOR (typically 10 business days for bilateral, 5 for CCP-cleared) is the time between:

    1. The last successful collateral exchange before default
    2. The closeout of the defaulted counterparty's positions

    During this window, the portfolio value can move adversely while collateral remains at its previous level. The residual exposure is:

    $$
    E_t^{\text{coll}} = (V_t - C_{t-\delta})^+ \approx (\Delta V_\delta)^+
    $$

    where $\delta$ is the MPOR and $\Delta V_\delta = V_t - V_{t-\delta}$ is the change in portfolio value over the MPOR. The PFE of this residual exposure is:

    $$
    \text{PFE}_\alpha^{\text{coll}} \approx \sigma_{\text{portfolio}} \cdot \sqrt{\delta} \cdot \Phi^{-1}(\alpha)
    $$

    This depends on:

    - The **short-horizon volatility** $\sigma_{\text{portfolio}}$ of the portfolio value (not long-term diffusion)
    - The **length of the MPOR** $\delta$ (via $\sqrt{\delta}$)
    - The **confidence level** $\alpha$

    It does **not** depend significantly on the remaining maturity of the trades (unlike uncollateralized PFE), which is why the collateralized PFE profile is approximately flat.

    **Example:** For $\sigma_{\text{daily}} = \$2$M, MPOR $= 10$ days, and $\alpha = 97.5\%$:

    $$
    \text{PFE}_{97.5\%}^{\text{coll}} \approx 2 \times \sqrt{10} \times 1.96 \approx 2 \times 3.16 \times 1.96 \approx \$12.4\text{M}
    $$

    compared to an uncollateralized peak PFE that might be \$80M or more for a large swap portfolio.

---

**Exercise 6.** PFE is estimated via Monte Carlo simulation. Describe why the estimation of PFE at high confidence levels (e.g., 99%) requires many more simulation paths than EE estimation. What techniques (importance sampling, stratification) can improve efficiency?

??? success "Solution to Exercise 6"
    **Why PFE estimation at high confidence levels requires many more paths:**

    EE is estimated as a sample mean:

    $$
    \widehat{\text{EE}}(t) = \frac{1}{N}\sum_{j=1}^N E_t^{(j)}
    $$

    The standard error of a sample mean is $\sigma/\sqrt{N}$, where $\sigma$ is the standard deviation of the exposure. All $N$ observations contribute equally to the estimate, giving efficient convergence.

    PFE at confidence level $\alpha$ is estimated as the empirical quantile:

    $$
    \widehat{\text{PFE}}_\alpha(t) = E_t^{(\lceil N\alpha \rceil)}
    $$

    The standard error of the quantile estimator is:

    $$
    \text{SE}(\widehat{\text{PFE}}_\alpha) \approx \frac{\sqrt{\alpha(1-\alpha)}}{f_{E_t}(\text{PFE}_\alpha)\sqrt{N}}
    $$

    where $f_{E_t}$ is the density of the exposure at the quantile. This has several implications:

    1. **Only tail observations matter:** For 99% PFE, only the top 1% of simulations contribute to the estimate. With $N = 1{,}000$ paths, only about 10 observations determine the 99th percentile — far too few for precision.

    2. **Density dependence:** The standard error is inversely proportional to $f_{E_t}(\text{PFE}_\alpha)$. In the tails of the distribution, the density is typically low, making the denominator small and the standard error large.

    3. **Order statistics variability:** The quantile estimate relies on the ordering of extreme observations, which are inherently more variable than central observations.

    **Quantitative comparison:** For EE with $N = 1{,}000$ paths, the relative standard error might be $\sigma/(E[E_t]\sqrt{1000}) \approx 3\%$. For 99% PFE with the same $N$, the relative standard error might be 15--30%, requiring $N \approx 25{,}000$--$100{,}000$ paths for comparable precision.

    **Techniques to improve efficiency:**

    1. **Importance Sampling:** Tilt the simulation measure to generate more scenarios in the tail region. Define a new measure $\widetilde{\mathbb{P}}$ that increases the probability of large exposures:

        $$
        \widehat{\text{PFE}}_\alpha = \text{Quantile}_\alpha\left\{E_t^{(j)} \cdot \frac{d\mathbb{P}}{d\widetilde{\mathbb{P}}}(\omega^{(j)})\right\}
        $$

        For example, simulate interest rates with an upward drift bias (for a receiver swap), then correct with likelihood ratios. This produces more observations in the tail, improving the quantile estimate.

    2. **Stratified Sampling:** Divide the probability space into strata (e.g., by the value of the driving Brownian motion) and sample a fixed number of paths from each stratum. This ensures adequate representation of the tails:

        - Partition $[0,1]$ into $K$ equal intervals
        - Sample $N/K$ uniform draws from each interval
        - Transform to risk factor values via the inverse CDF

        This reduces variance by eliminating the randomness in how many samples fall in each region.

    3. **Latin Hypercube Sampling (LHS):** A multidimensional extension of stratification that ensures each marginal distribution is uniformly sampled. Particularly effective for portfolios with multiple risk factors.

    4. **Quasi-Monte Carlo:** Use low-discrepancy sequences (Sobol, Halton) instead of pseudo-random numbers. These fill the probability space more uniformly, improving convergence from $O(1/\sqrt{N})$ to nearly $O(1/N)$ for smooth integrands.

    5. **Kernel Density Estimation:** Instead of using the raw empirical quantile, fit a smooth density to the simulated exposures and extract the quantile from the fitted distribution. This interpolates between observations and reduces the discreteness of the quantile estimate.

    6. **Antithetic Variates:** Pair each simulated path with its mirror image (negate the random draws). This reduces variance for symmetric components of the exposure distribution, though the benefit for tail estimation is more limited than for mean estimation.
