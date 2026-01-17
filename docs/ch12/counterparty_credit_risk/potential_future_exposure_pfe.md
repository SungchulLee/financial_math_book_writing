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
