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

### Radon–Nikodym Derivative

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

??? success "Solution to Exercise 1"
    **Given:** 5-year historical default probability $p^{\mathbb{P}} = 2.0\%$, 5-year CDS spread $s = 140$ bp, $R = 40\%$.

    **Physical intensity:**

    $$
    \lambda^{\mathbb{P}} = -\frac{1}{T}\ln(1 - p^{\mathbb{P}}) = -\frac{1}{5}\ln(1 - 0.02) = -\frac{1}{5}\ln(0.98)
    $$

    Since $\ln(0.98) = -0.02020$:

    $$
    \lambda^{\mathbb{P}} = \frac{0.02020}{5} = 0.404\% \text{ per year}
    $$

    **Risk-neutral intensity:**

    $$
    \lambda^{\mathbb{Q}} = \frac{s}{1-R} = \frac{0.0140}{0.60} = 2.333\% \text{ per year}
    $$

    **Credit risk premium ratio:**

    $$
    \eta = \frac{\lambda^{\mathbb{Q}}}{\lambda^{\mathbb{P}}} = \frac{2.333\%}{0.404\%} = 5.78
    $$

    The risk-neutral intensity is nearly 6 times the physical intensity, meaning the market demands substantial compensation beyond expected losses.

    **Spread decomposition:**

    The 140 bp CDS spread decomposes as:

    - **Expected loss component:**

    $$
    s_{\text{EL}} = (1-R)\lambda^{\mathbb{P}} = 0.60 \times 0.404\% = 0.242\% = 24.2 \text{ bp}
    $$

    - **Credit risk premium component:**

    $$
    s_{\text{CRP}} = s - s_{\text{EL}} = 140 - 24.2 = 115.8 \text{ bp}
    $$

    Equivalently:

    $$
    s_{\text{CRP}} = (1-R)(\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}) = 0.60 \times (2.333\% - 0.404\%) = 0.60 \times 1.929\% = 115.8 \text{ bp}
    $$

    **As fractions of the total spread:**

    - Expected loss: $24.2/140 = 17.3\%$
    - Risk premium: $115.8/140 = 82.7\%$

    The credit risk premium accounts for over 80% of the CDS spread, with expected loss contributing less than 20%. This is typical for investment-grade issuers.

---

**Exercise 2.** In the Merton model, the physical and risk-neutral distances to default differ by

$$
DD^{\mathbb{P}} - DD^{\mathbb{Q}} = \frac{(\mu - r)\sqrt{T}}{\sigma_V}
$$

For a firm with asset drift $\mu = 10\%$, risk-free rate $r = 3\%$, asset volatility $\sigma_V = 25\%$, and horizon $T = 5$ years, compute this gap. Explain why higher equity risk premia widen the gap between physical and risk-neutral default probabilities.

??? success "Solution to Exercise 2"
    **Given:** $\mu = 10\%$, $r = 3\%$, $\sigma_V = 25\%$, $T = 5$ years.

    **Computing the gap:**

    $$
    DD^{\mathbb{P}} - DD^{\mathbb{Q}} = \frac{(\mu - r)\sqrt{T}}{\sigma_V} = \frac{(0.10 - 0.03)\sqrt{5}}{0.25}
    $$

    $$
    = \frac{0.07 \times 2.2361}{0.25} = \frac{0.1565}{0.25} = 0.6261
    $$

    **Interpretation:** The physical distance to default exceeds the risk-neutral distance to default by 0.63 standard deviations. Since default probabilities are $\mathbb{P}(\tau \le T) = N(-DD^{\mathbb{P}})$ and $\mathbb{Q}(\tau \le T) = N(-DD^{\mathbb{Q}})$, and $DD^{\mathbb{P}} > DD^{\mathbb{Q}}$, we have $-DD^{\mathbb{P}} < -DD^{\mathbb{Q}}$, so:

    $$
    N(-DD^{\mathbb{P}}) < N(-DD^{\mathbb{Q}})
    $$

    confirming that the physical default probability is lower than the risk-neutral default probability.

    **Why higher equity risk premia widen the gap:**

    The gap $DD^{\mathbb{P}} - DD^{\mathbb{Q}} = (\mu - r)\sqrt{T}/\sigma_V$ is directly proportional to the **equity risk premium** $\mu - r$. The mechanism is:

    1. Under $\mathbb{P}$, the firm's asset value drifts at rate $\mu$, reflecting the actual expected return. A higher $\mu$ means the firm's assets grow faster, pushing the firm further from the default boundary and increasing $DD^{\mathbb{P}}$.

    2. Under $\mathbb{Q}$, the asset drift is replaced by $r$ (the risk-free rate), regardless of the firm's actual expected return. $DD^{\mathbb{Q}}$ is unaffected by changes in $\mu$.

    3. Therefore, a larger equity risk premium $\mu - r$ increases $DD^{\mathbb{P}}$ while leaving $DD^{\mathbb{Q}}$ unchanged, widening the gap.

    Economically, the equity risk premium reflects the compensation investors demand for bearing systematic asset risk. Under the pricing measure, this compensation is "removed," making default appear more likely. The larger the risk premium, the greater the divergence between the real-world and pricing-measure assessments of default risk.

    Note also that the gap grows as $\sqrt{T}$, so the $\mathbb{P}$--$\mathbb{Q}$ divergence is more pronounced at longer horizons.

---

**Exercise 3.** Explain why using risk-neutral default probabilities for economic capital calculations leads to overstatement of losses. Conversely, explain why using physical default probabilities for CDS pricing leads to systematic underpricing of protection. Provide a numerical example for each case.

??? success "Solution to Exercise 3"
    **Part 1: Risk-neutral PDs overstate losses for capital calculations**

    Economic capital is designed to cover unexpected losses at a given confidence level under the **real-world** measure. Using risk-neutral default probabilities inflates the loss estimate because $\lambda^{\mathbb{Q}} > \lambda^{\mathbb{P}}$.

    **Numerical example:** Consider a BBB-rated portfolio with \$1 billion notional and $R = 40\%$.

    - Physical intensity: $\lambda^{\mathbb{P}} = 0.36\%$
    - Risk-neutral intensity: $\lambda^{\mathbb{Q}} = 2.00\%$
    - 1-year physical default probability: $p^{\mathbb{P}} = 1 - e^{-0.0036} = 0.360\%$
    - 1-year risk-neutral default probability: $p^{\mathbb{Q}} = 1 - e^{-0.020} = 1.980\%$

    Expected loss calculations:

    $$
    \text{EL}^{\mathbb{P}} = (1-R) \times p^{\mathbb{P}} \times \text{Notional} = 0.60 \times 0.00360 \times 10^9 = \$2.16\text{M}
    $$

    $$
    \text{EL}^{\mathbb{Q}} = (1-R) \times p^{\mathbb{Q}} \times \text{Notional} = 0.60 \times 0.01980 \times 10^9 = \$11.88\text{M}
    $$

    Using $\mathbb{Q}$-probabilities overstates the expected loss by a factor of $11.88/2.16 = 5.5$. Capital requirements based on this would be excessively conservative, leading to inefficient capital allocation.

    **Part 2: Physical PDs underprice CDS protection**

    CDS spreads must reflect risk-neutral default probabilities to prevent arbitrage. Using physical probabilities undervalues the credit protection.

    **Numerical example:** A protection seller prices a 5-year CDS on the same BBB issuer:

    - Fair CDS spread using $\mathbb{Q}$: $s^{\mathbb{Q}} = (1-R)\lambda^{\mathbb{Q}} = 0.60 \times 2.00\% = 120$ bp
    - Incorrectly priced using $\mathbb{P}$: $s^{\mathbb{P}} = (1-R)\lambda^{\mathbb{P}} = 0.60 \times 0.36\% = 21.6$ bp

    If the seller charges only 21.6 bp (the physical expected loss), they collect $21.6$ bp per year but the market-consistent cost of hedging (or replacing) this position is $120$ bp per year. The seller is systematically undercompensated by $120 - 21.6 = 98.4$ bp annually. On \$100 million notional over 5 years, this underpricing amounts to approximately $\$100\text{M} \times 0.00984 \times 5 = \$4.92\text{M}$ in foregone risk premium---a certain path to trading losses.

---

**Exercise 4.** The credit risk premium ratio $\eta$ is empirically observed to be larger for investment-grade issuers (e.g., $\eta \approx 6$ for BBB) than for speculative-grade issuers (e.g., $\eta \approx 1.5$ for B). Provide an economic explanation for this pattern, referencing the relative importance of expected loss versus systematic risk compensation at different credit qualities.

??? success "Solution to Exercise 4"
    **Observation:** $\eta \approx 6$ for BBB but $\eta \approx 1.5$ for B-rated issuers.

    **Economic explanation:**

    The credit risk premium ratio $\eta = \lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ reflects the compensation investors demand *relative to* expected losses. The pattern $\eta_{\text{IG}} \gg \eta_{\text{HY}}$ has several interconnected explanations:

    **1. Relative importance of systematic vs. idiosyncratic risk**

    For investment-grade issuers, defaults are rare events that tend to cluster during severe economic downturns. The default risk is predominantly **systematic**---correlated with the business cycle and aggregate economic conditions. Investors demand a large premium for bearing this systematic risk because defaults occur precisely when marginal utility is high (recessions). The ratio $\eta$ captures this: expected losses are tiny ($\lambda^{\mathbb{P}}$ is very small), but the systematic risk premium is substantial.

    For speculative-grade issuers, a much larger fraction of default risk is **idiosyncratic**---driven by firm-specific factors (poor management, competitive pressures, operational failures). Idiosyncratic risk can be diversified and therefore commands a smaller premium. Since $\lambda^{\mathbb{P}}$ is already large (reflecting high baseline default rates), the additional systematic premium is proportionally smaller.

    **2. The "credit spread puzzle" perspective**

    Investment-grade spreads are far wider than what expected losses alone would justify. For AAA bonds, the physical expected loss is near zero, yet spreads are 10--30 bp. Almost the entire spread is risk premium plus liquidity---hence $\eta$ is very large (10--15). For B-rated issuers, expected losses account for a much larger share of the spread (perhaps 50--70%), leaving less room for the risk premium to inflate $\eta$.

    **3. Jump risk aversion**

    Default is a discontinuous event that cannot be hedged perfectly. For investment-grade issuers, a default is a "surprise" event with severe consequences for portfolio value. The surprise component (low probability, high impact) commands a disproportionate premium. For speculative-grade issuers, default is already "priced in" as a high-probability event, so the surprise premium is proportionally smaller.

    **4. Mathematical structure**

    If the additive risk premium $\theta = \lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}$ is roughly similar across ratings (say, 1--3%), then:

    $$
    \eta = 1 + \frac{\theta}{\lambda^{\mathbb{P}}}
    $$

    For IG issuers with $\lambda^{\mathbb{P}} = 0.05\%$, even $\theta = 0.25\%$ gives $\eta = 6$. For HY issuers with $\lambda^{\mathbb{P}} = 4\%$, $\theta = 2\%$ gives $\eta = 1.5$. A relatively flat additive premium naturally produces a declining multiplicative ratio.

---

**Exercise 5.** A risk manager estimates physical default probabilities from Moody's historical data and risk-neutral probabilities from CDS spreads. During a recession, the risk premium ratio $\eta$ increases from 5 to 8. Describe how this procyclicality affects (a) CDS pricing, (b) regulatory capital calculations, and (c) relative value strategies that exploit the $\mathbb{P}$--$\mathbb{Q}$ gap.

??? success "Solution to Exercise 5"
    **Given:** $\eta$ increases from 5 to 8 during a recession, with $\lambda^{\mathbb{P}}$ approximately unchanged.

    **(a) Impact on CDS pricing:**

    Since $\lambda^{\mathbb{Q}} = \eta \cdot \lambda^{\mathbb{P}}$, an increase from $\eta = 5$ to $\eta = 8$ (with $\lambda^{\mathbb{P}}$ fixed) implies:

    $$
    \lambda_{\text{new}}^{\mathbb{Q}} = 8 \lambda^{\mathbb{P}} = \frac{8}{5}\lambda_{\text{old}}^{\mathbb{Q}} = 1.6 \times \lambda_{\text{old}}^{\mathbb{Q}}
    $$

    CDS spreads widen by approximately 60%:

    $$
    s_{\text{new}} \approx (1-R)\lambda_{\text{new}}^{\mathbb{Q}} = 1.6 \times s_{\text{old}}
    $$

    For a BBB issuer with $\lambda^{\mathbb{P}} = 0.36\%$, the CDS spread moves from $(1-0.4) \times 5 \times 0.36\% = 108$ bp to $(1-0.4) \times 8 \times 0.36\% = 173$ bp. Existing CDS positions marked to market experience significant P&L swings. Protection sellers face mark-to-market losses; protection buyers profit.

    **(b) Impact on regulatory capital:**

    Regulatory capital under the Internal Ratings-Based (IRB) approach uses **physical** default probabilities, typically through-the-cycle (TTC) estimates. If $\lambda^{\mathbb{P}}$ is roughly constant (TTC ratings are designed to be stable), then regulatory capital requirements do not change even as $\eta$ spikes.

    This creates a procyclical gap: market-implied losses (CVA, fair-value provisions) surge with $\eta$, but regulatory capital stays flat. The bank's economic capital---which may be sensitive to point-in-time (PIT) estimates---would increase if PIT estimates of $\lambda^{\mathbb{P}}$ also rise in recession, but typically less than the CDS-implied increase.

    The implication is that regulatory capital may be **insufficient** relative to market-implied risks during crises, contributing to procyclicality concerns that motivated Basel III reforms.

    **(c) Impact on relative value strategies:**

    A relative value strategy exploiting the $\mathbb{P}$-$\mathbb{Q}$ gap involves selling CDS protection (earning the spread $s$) and holding reserves for expected physical losses. The profit is:

    $$
    \text{Carry} = s - (1-R)\lambda^{\mathbb{P}} = (1-R)(\eta - 1)\lambda^{\mathbb{P}}
    $$

    When $\eta$ increases from 5 to 8, the carry increases:

    $$
    \text{Carry}_{\text{new}} = (1-R) \times 7 \times \lambda^{\mathbb{P}} \quad \text{vs.} \quad \text{Carry}_{\text{old}} = (1-R) \times 4 \times \lambda^{\mathbb{P}}
    $$

    The risk premium widens, making the strategy more attractive *in expectation*. However, the strategy faces three major risks during a recession:

    1. **Mark-to-market risk:** The increase in $\eta$ causes immediate mark-to-market losses on existing short-protection positions, even before any defaults occur.
    2. **Margin calls:** Wider spreads trigger margin calls that may force position liquidation at the worst time.
    3. **$\lambda^{\mathbb{P}}$ may also increase:** The assumption that physical default rates are constant is questionable in a recession. If $\lambda^{\mathbb{P}}$ rises simultaneously, actual defaults erode the carry.

    Thus, while the elevated $\eta$ signals a larger risk premium, entering the trade during a recession requires substantial risk capital and tolerance for interim losses.

---

**Exercise 6.** Using the data in the table of typical $\lambda^{\mathbb{P}}$ and $\lambda^{\mathbb{Q}}$ values provided in the text, compute the 5-year risk-neutral and physical survival probabilities for an A-rated and a BB-rated issuer. For each rating, compute the expected loss component and risk premium component of the credit spread (assuming $R = 40\%$). Which rating has a larger fraction of its spread attributable to expected loss?

??? success "Solution to Exercise 6"
    **Data from the text:**

    | Rating | $\lambda^{\mathbb{P}}$ (%) | $\lambda^{\mathbb{Q}}$ (%) | $\eta$ |
    |--------|--------------------------|--------------------------|--------|
    | A | 0.08 | 0.50 | 6.3 |
    | BB | 1.70 | 3.50 | 2.1 |

    **5-year survival probabilities:**

    *A-rated:*

    $$
    S^{\mathbb{P}}_A(0,5) = e^{-\lambda^{\mathbb{P}} \times 5} = e^{-0.0008 \times 5} = e^{-0.004} = 0.9960
    $$

    $$
    S^{\mathbb{Q}}_A(0,5) = e^{-\lambda^{\mathbb{Q}} \times 5} = e^{-0.005 \times 5} = e^{-0.025} = 0.9753
    $$

    *BB-rated:*

    $$
    S^{\mathbb{P}}_{BB}(0,5) = e^{-0.017 \times 5} = e^{-0.085} = 0.9185
    $$

    $$
    S^{\mathbb{Q}}_{BB}(0,5) = e^{-0.035 \times 5} = e^{-0.175} = 0.8395
    $$

    **Spread decomposition (assuming $R = 40\%$):**

    *A-rated:*

    - Total credit spread: $s_A = (1-R)\lambda^{\mathbb{Q}}_A = 0.60 \times 0.50\% = 0.30\% = 30$ bp
    - Expected loss component: $s_{\text{EL}} = (1-R)\lambda^{\mathbb{P}}_A = 0.60 \times 0.08\% = 0.048\% = 4.8$ bp
    - Risk premium component: $s_{\text{CRP}} = 30 - 4.8 = 25.2$ bp
    - Expected loss fraction: $4.8/30 = 16\%$
    - Risk premium fraction: $25.2/30 = 84\%$

    *BB-rated:*

    - Total credit spread: $s_{BB} = (1-R)\lambda^{\mathbb{Q}}_{BB} = 0.60 \times 3.50\% = 2.10\% = 210$ bp
    - Expected loss component: $s_{\text{EL}} = (1-R)\lambda^{\mathbb{P}}_{BB} = 0.60 \times 1.70\% = 1.02\% = 102$ bp
    - Risk premium component: $s_{\text{CRP}} = 210 - 102 = 108$ bp
    - Expected loss fraction: $102/210 = 48.6\%$
    - Risk premium fraction: $108/210 = 51.4\%$

    **Comparison:**

    | Component | A-rated | BB-rated |
    |-----------|---------|----------|
    | Total spread (bp) | 30 | 210 |
    | Expected loss (bp) | 4.8 | 102 |
    | Risk premium (bp) | 25.2 | 108 |
    | EL fraction | 16% | 49% |
    | RP fraction | 84% | 51% |

    **BB-rated issuers have a larger fraction of their spread attributable to expected loss** (49% vs. 16%). This is because speculative-grade issuers have high physical default probabilities, so expected losses are a substantial part of the spread. For investment-grade issuers, physical default probabilities are very small, and the spread is dominated by the credit risk premium---the compensation investors demand for bearing systematic default risk rather than the expected cost of default itself.
