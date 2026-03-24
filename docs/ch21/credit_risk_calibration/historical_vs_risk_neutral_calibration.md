# Historical vs Risk-Neutral Calibration

Credit models can be calibrated to two fundamentally different data sources: **historical default data** (physical measure $\mathbb{P}$) and **market prices** (risk-neutral measure $\mathbb{Q}$). The two yield systematically different default probabilities, and the gap between them---the **credit risk premium**---reveals the compensation investors demand for bearing default risk. Understanding this distinction is essential for correct application of credit models in pricing, risk management, and capital allocation.

---

## Two Measures, Two Calibrations

### Physical Measure ($\mathbb{P}$)

Under the **physical** (or historical, or real-world, or actuarial) measure:

- Default probabilities are estimated from **historical default rates** (e.g., Moody's annual default studies)
- Parameters reflect the **true statistical likelihood** of default
- Used for: risk management, capital allocation, internal rating systems, stress testing

### Risk-Neutral Measure ($\mathbb{Q}$)

Under the **risk-neutral** (or pricing) measure:

- Default probabilities are **implied from market prices** (CDS spreads, bond yields)
- Parameters incorporate both expected losses and risk premiums
- Used for: pricing credit derivatives, marking to market, relative value

### The Fundamental Inequality

Empirically, for virtually all credit qualities:

$$
\mathbb{Q}(\tau \le T) > \mathbb{P}(\tau \le T)
$$

Risk-neutral default probabilities **exceed** physical default probabilities. The ratio is typically 2--10 for investment-grade issuers and 1.5--3 for speculative-grade issuers.

---

## Mathematical Framework

### Intensity Under Both Measures

Let $\lambda_t^{\mathbb{P}}$ and $\lambda_t^{\mathbb{Q}}$ denote the default intensity under the physical and risk-neutral measures, respectively.

The **Girsanov theorem** relates them. Under a change of measure from $\mathbb{P}$ to $\mathbb{Q}$, the intensity transforms as:

$$
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} \cdot \eta_t
$$

where $\eta_t > 0$ is the **market price of default risk** (or default risk premium factor). Equivalently:

$$
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t
$$

with $\theta_t = \lambda_t^{\mathbb{P}}(\eta_t - 1)$ being the **additive risk premium**.

### Radon-Nikodym Derivative

The measure change for the default component is characterized by:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{G}_t} = \mathcal{E}\left(\int_0^{\cdot} (\eta_s - 1)(dH_s - \lambda_s^{\mathbb{P}} ds)\right)_t \cdot L_t^{\text{diff}}
$$

where $\mathcal{E}(\cdot)$ denotes the stochastic exponential, $H_t = \mathbf{1}_{\{\tau \le t\}}$, and $L_t^{\text{diff}}$ accounts for the Girsanov change in diffusion components.

### Survival Probabilities

Under each measure:

$$
S^{\mathbb{P}}(0,T) = \mathbb{E}^{\mathbb{P}}\left[e^{-\int_0^T \lambda_s^{\mathbb{P}} ds}\right], \quad S^{\mathbb{Q}}(0,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T \lambda_s^{\mathbb{Q}} ds}\right]
$$

Since $\lambda^{\mathbb{Q}} > \lambda^{\mathbb{P}}$ (for risk-averse investors):

$$
S^{\mathbb{Q}}(0,T) < S^{\mathbb{P}}(0,T)
$$

Risk-neutral survival is lower, meaning risk-neutral default probability is higher.

---

## Historical Calibration

### Data Sources

- **Rating agency studies:** Moody's, S&P, and Fitch publish annual default studies with cohort-based transition matrices
- **CreditRisk+ databases:** Default counts by rating, industry, geography
- **Internal bank data:** Proprietary default observations

### Cohort-Based Estimation

For a rating category (e.g., BBB), the $T$-year default rate is estimated as:

$$
\hat{p}^{\mathbb{P}}(T) = \frac{\text{Number of defaults within } T \text{ years}}{\text{Number of issuers at start}}
$$

**Average annual default rates (Moody's, 1970--2020):**

| Rating | 1-Year | 5-Year | 10-Year |
|--------|--------|--------|---------|
| Aaa | 0.00% | 0.08% | 0.50% |
| Aa | 0.02% | 0.20% | 0.60% |
| A | 0.06% | 0.50% | 1.50% |
| Baa | 0.17% | 1.80% | 4.50% |
| Ba | 1.10% | 8.50% | 17.0% |
| B | 4.00% | 21.0% | 33.0% |
| Caa-C | 15.0% | 42.0% | 55.0% |

### Implied Physical Intensity

From the $T$-year cumulative default probability:

$$
\hat{\lambda}^{\mathbb{P}} = -\frac{1}{T}\ln(1 - \hat{p}^{\mathbb{P}}(T))
$$

For BBB at 5 years: $\hat{\lambda}^{\mathbb{P}} = -\frac{1}{5}\ln(0.982) = 0.36\%$ per year.

---

## Risk-Neutral Calibration

### Data Sources

- **CDS spreads:** Most direct (isolate default risk)
- **Corporate bond spreads:** Over-Treasury or over-swap yields
- **Equity option-implied volatilities:** Via structural models

### CDS-Implied Intensity

From the approximate relationship $s \approx (1-R)\lambda^{\mathbb{Q}}$:

$$
\hat{\lambda}^{\mathbb{Q}} = \frac{s}{1-R}
$$

For a BBB issuer with 5Y CDS spread of 120 bp and $R = 40\%$:

$$
\hat{\lambda}^{\mathbb{Q}} = \frac{0.0120}{0.60} = 2.0\% \text{ per year}
$$

### Bond-Implied Intensity

From the bond spread $s_{\text{bond}}$:

$$
\hat{\lambda}^{\mathbb{Q}} \approx \frac{s_{\text{bond}}}{1-R}
$$

Bond spreads include liquidity and tax effects, so this estimate may be upward-biased relative to pure credit risk.

---

## The Credit Risk Premium

### Definition

The **credit risk premium** (CRP) is the difference between risk-neutral and physical default probabilities or intensities:

$$
\text{CRP}(T) = \lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}
$$

or multiplicatively:

$$
\eta = \frac{\lambda^{\mathbb{Q}}}{\lambda^{\mathbb{P}}}
$$

where $\eta > 1$ indicates a positive risk premium (investors demand compensation beyond expected loss).

### Empirical Estimates

For the BBB example:

$$
\eta = \frac{2.0\%}{0.36\%} = 5.6
$$

The risk-neutral intensity is **5.6 times** the physical intensity. Investors demand substantial compensation for bearing credit risk.

Typical ranges of $\eta$ across rating categories:

| Rating | $\lambda^{\mathbb{P}}$ (%) | $\lambda^{\mathbb{Q}}$ (%) | $\eta$ |
|--------|--------------------------|--------------------------|--------|
| AAA | 0.01 | 0.15 | 15.0 |
| AA | 0.03 | 0.25 | 8.3 |
| A | 0.08 | 0.50 | 6.3 |
| BBB | 0.36 | 2.00 | 5.6 |
| BB | 1.70 | 3.50 | 2.1 |
| B | 4.50 | 7.00 | 1.6 |

**Key pattern:** The risk premium ratio $\eta$ is **larger for higher-rated issuers**. This reflects the fact that investment-grade spreads contain a proportionally larger non-default component (liquidity, systematic risk) relative to expected loss.

---

## Decomposition of Credit Spreads

### Spread Components

The credit spread can be decomposed as:

$$
s = \underbrace{(1-R)\lambda^{\mathbb{P}}}_{\text{Expected loss}} + \underbrace{(1-R)(\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}})}_{\text{Credit risk premium}} + \underbrace{s_{\text{liq}} + s_{\text{tax}}}_{\text{Non-default components}}
$$

Or in relative terms:

$$
s = s_{\text{EL}} + s_{\text{CRP}} + s_{\text{other}}
$$

### Quantitative Breakdown

For a typical BBB bond with 150 bp spread:

- **Expected loss:** $(1-R)\lambda^{\mathbb{P}} = 0.6 \times 0.36\% = 22$ bp ($\approx 15\%$)
- **Credit risk premium:** $(1-R)(\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}) = 0.6 \times 1.64\% = 98$ bp ($\approx 65\%$)
- **Liquidity + tax:** $\approx 30$ bp ($\approx 20\%$)

The credit risk premium dominates, reflecting systematic default risk compensation.

### Why the Risk Premium?

Investors require a premium because:

1. **Systematic risk:** Default rates are correlated with the business cycle. Defaults cluster in recessions when marginal utility is high.
2. **Jump risk:** Default is a sudden, discontinuous event. Investors are averse to jump risk even beyond its expected impact.
3. **Incomplete markets:** Credit risk cannot be perfectly hedged, so the risk premium compensates for unhedgeable exposure.
4. **Loss aversion:** Behavioral factors amplify the perceived cost of credit losses.

---

## Structural Model Perspective

### Merton Model Under Both Measures

In the Merton model, the default probability depends on the asset drift:

**Physical measure:**

$$
\mathbb{P}(\tau \le T) = N\left(-\frac{\ln(V_0/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}\right) = N(-DD)
$$

**Risk-neutral measure:**

$$
\mathbb{Q}(\tau \le T) = N\left(-\frac{\ln(V_0/D) + (r - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}\right) = N(-d_2)
$$

The difference arises because $\mu > r$ (the equity risk premium):

$$
DD - d_2 = \frac{(\mu - r)T}{\sigma_V\sqrt{T}} = \frac{\mu - r}{\sigma_V}\sqrt{T}
$$

Since the market price of asset risk $(\mu - r)/\sigma_V > 0$, we have $DD > d_2$ and thus $N(-DD) < N(-d_2)$, confirming $\mathbb{P}(\text{default}) < \mathbb{Q}(\text{default})$.

### Distance to Default vs Risk-Neutral Distance

$$
DD^{\mathbb{P}} = \frac{\ln(V_0/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}, \quad DD^{\mathbb{Q}} = d_2 = \frac{\ln(V_0/D) + (r - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
$$

The gap $DD^{\mathbb{P}} - DD^{\mathbb{Q}} = (\mu - r)\sqrt{T}/\sigma_V$ grows with $\sqrt{T}$ and with the Sharpe ratio of firm assets.

---

## Practical Implications

### Pricing vs Risk Management

| Application | Measure | Data Source | Key Metric |
|-------------|---------|-------------|------------|
| Derivative pricing | $\mathbb{Q}$ | CDS/bond spreads | $\lambda^{\mathbb{Q}}$, risk-neutral PD |
| CVA/DVA | $\mathbb{Q}$ | CDS spreads | Risk-neutral expected loss |
| Economic capital | $\mathbb{P}$ | Default history | Physical PD |
| Regulatory capital (IRB) | $\mathbb{P}$ | Internal estimates | Through-the-cycle PD |
| Stress testing | $\mathbb{P}$ | Stressed scenarios | Stressed PD |
| Relative value | $\mathbb{Q}$ vs $\mathbb{P}$ | Both | Implied CRP |

### Common Mistakes

!!! warning "Measure Confusion"
    Using risk-neutral default probabilities for capital calculations (or physical probabilities for pricing) is a common and costly error:

    - **Overstatement:** Using $\lambda^{\mathbb{Q}}$ for capital overstates losses by the risk premium factor $\eta$
    - **Understatement:** Using $\lambda^{\mathbb{P}}$ for pricing undervalues protection, leading to systematic trading losses

### Time Variation of the Risk Premium

The credit risk premium is not constant:

- **Recessions:** $\eta$ increases (investors demand more compensation)
- **Expansions:** $\eta$ decreases (risk appetite increases)
- **Crisis events:** $\eta$ spikes dramatically

This procyclicality creates challenges for models that assume constant $\eta$.

---

## Estimation Methods

### Method 1: Direct Comparison

1. Estimate $\lambda^{\mathbb{P}}$ from historical default data
2. Estimate $\lambda^{\mathbb{Q}}$ from CDS or bond spreads
3. Compute $\eta = \lambda^{\mathbb{Q}} / \lambda^{\mathbb{P}}$

**Advantage:** Simple and transparent.

**Disadvantage:** Different time horizons, smoothing effects in historical data, and the averaging inherent in ratings.

### Method 2: Structural Model Calibration

1. Calibrate a structural model (Merton, Black-Cox) to equity data $\to$ obtain $(V_0, \sigma_V)$
2. Compute both physical and risk-neutral default probabilities from the model
3. The asset risk premium $\mu - r$ determines $\eta$

**Advantage:** Provides a structural explanation for the risk premium.

**Disadvantage:** Model-dependent; unobservable firm value.

### Method 3: Reduced-Form with Market Price of Risk

Specify $\lambda^{\mathbb{Q}} = \eta \lambda^{\mathbb{P}}$ and estimate $\eta$ from:

$$
s_{\text{market}} = (1-R)\lambda^{\mathbb{Q}} = (1-R)\eta\lambda^{\mathbb{P}}
$$

Given $\lambda^{\mathbb{P}}$ from historical data and $s$ from market:

$$
\hat{\eta} = \frac{s_{\text{market}}}{(1-R)\hat{\lambda}^{\mathbb{P}}}
$$

---

## Numerical Example

**Setup:** 5-year CDS on a BBB-rated corporate.

**Market data:**

- 5Y CDS spread: $s = 130$ bp
- Recovery rate: $R = 40\%$
- 5-year historical default rate: 1.8% (Moody's Baa)

**Step 1: Risk-neutral intensity**

$$
\lambda^{\mathbb{Q}} = \frac{0.0130}{0.60} = 2.17\%
$$

**Step 2: Physical intensity**

$$
\lambda^{\mathbb{P}} = -\frac{1}{5}\ln(1 - 0.018) = \frac{0.01816}{5} = 0.363\%
$$

**Step 3: Risk premium ratio**

$$
\eta = \frac{2.17\%}{0.363\%} = 5.98
$$

**Step 4: Spread decomposition**

- Expected loss: $(1-R)\lambda^{\mathbb{P}} = 0.6 \times 0.363\% = 21.8$ bp
- Risk premium: $130 - 21.8 = 108.2$ bp
- Risk premium as fraction: $108.2/130 = 83\%$

The vast majority of the CDS spread is risk premium, not expected loss.

---

## Key Takeaways

- Physical ($\mathbb{P}$) and risk-neutral ($\mathbb{Q}$) default probabilities differ systematically, with $\mathbb{Q}$-probabilities always larger
- The ratio $\eta = \lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ measures the credit risk premium and is typically 2--10 for investment grade
- Credit spreads decompose into expected loss, credit risk premium, and liquidity/tax components
- Expected loss is often a small fraction (15--30%) of the total spread for investment-grade bonds
- Pricing requires $\mathbb{Q}$-measure parameters; risk management requires $\mathbb{P}$-measure parameters
- Confusing the two measures leads to systematic errors in pricing or capital calculations
- The credit risk premium varies procyclically, rising in recessions and crises

---

## Further Reading

- Berndt, A., Douglas, R., Duffie, D., Ferguson, M., & Schranz, D. (2005). Measuring default risk premia from default swap rates and EDFs. *BIS Working Paper No. 173*.
- Huang, J.-Z., & Huang, M. (2012). How much of the corporate-treasury yield spread is due to credit risk? *Review of Asset Pricing Studies*, 2(2), 153--202.
- Driessen, J. (2005). Is default event risk priced in corporate bonds? *Review of Financial Studies*, 18(1), 165--195.
- Duffie, D., & Singleton, K. J. (2003). *Credit Risk: Pricing, Measurement, and Management*. Princeton University Press, Chapter 4.

---

## Exercises

**Exercise 1.** A BBB-rated issuer has a 5-year historical default probability of 2.0% and a 5-year CDS spread of 140 bp with $R = 40\%$. Compute the physical intensity $\lambda^{\mathbb{P}}$, the risk-neutral intensity $\lambda^{\mathbb{Q}}$, and the credit risk premium ratio $\eta = \lambda^{\mathbb{Q}} / \lambda^{\mathbb{P}}$. Decompose the 140 bp spread into expected loss and risk premium components.

---

**Exercise 2.** In the Merton model, the physical and risk-neutral distances to default differ by

$$
DD^{\mathbb{P}} - DD^{\mathbb{Q}} = \frac{(\mu - r)\sqrt{T}}{\sigma_V}
$$

For a firm with asset drift $\mu = 10\%$, risk-free rate $r = 3\%$, asset volatility $\sigma_V = 25\%$, and horizon $T = 5$ years, compute this gap. Explain why higher equity risk premia widen the gap between physical and risk-neutral default probabilities.

---

**Exercise 3.** Explain why using risk-neutral default probabilities for economic capital calculations leads to overstatement of losses. Conversely, explain why using physical default probabilities for CDS pricing leads to systematic underpricing of protection. Provide a numerical example for each case.

---

**Exercise 4.** The credit risk premium ratio $\eta$ is empirically observed to be larger for investment-grade issuers (e.g., $\eta \approx 6$ for BBB) than for speculative-grade issuers (e.g., $\eta \approx 1.5$ for B). Provide an economic explanation for this pattern, referencing the relative importance of expected loss versus systematic risk compensation at different credit qualities.

---

**Exercise 5.** A risk manager estimates physical default probabilities from Moody's historical data and risk-neutral probabilities from CDS spreads. During a recession, the risk premium ratio $\eta$ increases from 5 to 8. Describe how this procyclicality affects (a) CDS pricing, (b) regulatory capital calculations, and (c) relative value strategies that exploit the $\mathbb{P}$--$\mathbb{Q}$ gap.

---

**Exercise 6.** Using the data in the table of typical $\lambda^{\mathbb{P}}$ and $\lambda^{\mathbb{Q}}$ values provided in the text, compute the 5-year risk-neutral and physical survival probabilities for an A-rated and a BB-rated issuer. For each rating, compute the expected loss component and risk premium component of the credit spread (assuming $R = 40\%$). Which rating has a larger fraction of its spread attributable to expected loss?
