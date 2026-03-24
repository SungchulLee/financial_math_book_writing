# KMV Distance to Default

The **KMV model**, developed by Kealhofer, McQuown, and Vasicek and commercialized by Moody's Analytics (formerly KMV Corporation), operationalizes the Merton structural framework for practical credit risk assessment. Its central output is the **distance to default** (DD), a normalized measure of how far a firm's asset value is from its default point. The DD is then mapped to an **expected default frequency** (EDF) using a proprietary empirical database, bridging structural theory with observed default rates.

---

## From Merton to KMV

### The Merton Model's Practical Gap

The Merton model provides elegant pricing formulas but faces practical challenges:

- Asset value $V_t$ is **unobservable**
- Asset volatility $\sigma_V$ is **unobservable**
- The model maps risk-neutral default probabilities, which differ from physical (real-world) ones
- Direct application yields default probabilities that are too low compared to historical data

The KMV approach addresses these issues by:

1. Extracting $V_t$ and $\sigma_V$ from equity market data
2. Computing a physical-measure distance to default
3. Mapping DD to empirical default frequencies rather than relying on $N(-DD)$

### Conceptual Flow

$$
\text{Equity Price} \xrightarrow{\text{Calibration}} (V_0, \sigma_V) \xrightarrow{\text{DD Formula}} \text{DD} \xrightarrow{\text{Empirical Map}} \text{EDF}
$$

---

## The Default Point

### Definition

The **default point** (DP) is the asset value at which default is deemed to occur. KMV defines it empirically, not as the total face value of debt:

$$
\text{DP} = \text{STD} + \frac{1}{2} \cdot \text{LTD}
$$

where:

- **STD** = Short-term debt (maturity $\le 1$ year): current liabilities, commercial paper, short-term bank loans
- **LTD** = Long-term debt (maturity $> 1$ year): bonds, long-term loans, other long-term liabilities

### Economic Rationale

The default point lies between short-term and total debt because:

- Firms **must** service short-term obligations (failure triggers default)
- Long-term debt provides some flexibility (renegotiation, covenant waivers)
- Empirical observation: firms typically default when assets fall to roughly STD + 0.5 LTD

!!! note "Empirical Calibration"
    The coefficient $1/2$ on long-term debt is not a theoretical result but an empirically calibrated parameter from Moody's KMV extensive default database. Different implementations may use slightly different weights.

---

## Distance to Default

### Definition

The **distance to default** measures how many standard deviations the expected asset value at the horizon is above the default point:

$$
DD = \frac{\ln(V_0 / \text{DP}) + (\mu_V - \sigma_V^2/2)T}{\sigma_V \sqrt{T}}
$$

where:

- $V_0$: current asset value (inferred from equity)
- DP: default point
- $\mu_V$: expected asset return under the physical measure $\mathbb{P}$
- $\sigma_V$: asset volatility
- $T$: time horizon (typically 1 year)

### Derivation

Under the physical measure $\mathbb{P}$, asset value follows:

$$
V_T = V_0 \exp\left[\left(\mu_V - \frac{\sigma_V^2}{2}\right)T + \sigma_V W_T^{\mathbb{P}}\right]
$$

so that $\ln V_T \sim \mathcal{N}\left(\ln V_0 + (\mu_V - \sigma_V^2/2)T, \, \sigma_V^2 T\right)$.

Default occurs when $V_T < \text{DP}$:

$$
\mathbb{P}(V_T < \text{DP}) = \mathbb{P}\left(\frac{\ln V_T - \mathbb{E}[\ln V_T]}{\sigma_V\sqrt{T}} < \frac{\ln \text{DP} - \mathbb{E}[\ln V_T]}{\sigma_V\sqrt{T}}\right) = N(-DD)
$$

Therefore DD is precisely the number of standard deviations between the expected log-asset value and the log-default point, normalized by the volatility of log-asset value over the horizon.

### Interpretation

$$
DD = \frac{\text{Expected} \ln V_T - \ln \text{DP}}{\text{Std Dev of } \ln V_T}
$$

- $DD \gg 0$: Firm is far from default (safe)
- $DD \approx 0$: Firm is near the default boundary
- $DD < 0$: Expected asset value is below the default point

Typical values for investment-grade firms: $DD \in [4, 8]$. For speculative-grade firms: $DD \in [1, 3]$.

---

## Calibration: Extracting Asset Parameters

### The Two-Equation System

The key calibration challenge is to extract the unobservable $(V_0, \sigma_V)$ from observable equity data. Two equations relate equity to asset quantities:

**Equation 1 (Equity as a call option):**

$$
E_0 = V_0 N(d_1) - \text{DP} \cdot e^{-rT} N(d_2)
$$

where:

$$
d_1 = \frac{\ln(V_0/\text{DP}) + (r + \sigma_V^2/2)T}{\sigma_V\sqrt{T}}, \quad d_2 = d_1 - \sigma_V\sqrt{T}
$$

**Equation 2 (Volatility linkage via delta):**

From Ito's lemma applied to $E = E(V, t)$:

$$
\sigma_E E_0 = \frac{\partial E}{\partial V} \sigma_V V_0 = N(d_1) \sigma_V V_0
$$

which gives:

$$
\sigma_E = \frac{V_0 N(d_1)}{E_0} \cdot \sigma_V
$$

### Iterative Solution Algorithm

The system is nonlinear and solved iteratively:

1. **Initialize:** Set $V_0^{(0)} = E_0 + \text{DP} \cdot e^{-rT}$ (approximate asset value)
2. **Compute $\sigma_V^{(k)}$:** From Equation 2:

$$
\sigma_V^{(k)} = \frac{\sigma_E E_0}{V_0^{(k)} N(d_1^{(k)})}
$$

3. **Update $V_0^{(k+1)}$:** Solve Equation 1 for $V_0$ given $\sigma_V^{(k)}$ (one-dimensional root finding)
4. **Check convergence:** If $|V_0^{(k+1)} - V_0^{(k)}| < \varepsilon$, stop; otherwise return to step 2

The iteration typically converges in 5--10 steps.

??? example "Alternative: Direct Nonlinear System"
    One can also solve the two-equation system simultaneously using Newton's method in two dimensions. Define $F: \mathbb{R}^2 \to \mathbb{R}^2$ with:

    $$
    F_1(V, \sigma) = V N(d_1) - \text{DP} \cdot e^{-rT} N(d_2) - E_0
    $$

    $$
    F_2(V, \sigma) = V N(d_1) \sigma - \sigma_E E_0
    $$

    and iterate $\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - J_F^{-1} F(\mathbf{x}^{(k)})$ where $J_F$ is the Jacobian.

---

## Expected Default Frequency

### The Naive Normal Mapping

If asset returns were exactly normal, the physical default probability would be:

$$
\text{EDF}_{\text{naive}} = N(-DD)
$$

However, this consistently **underestimates** actual default rates because:

- Asset returns have heavier tails than the normal distribution
- Firms with the same DD may have different default rates due to industry, size, and other factors
- The Merton structural model is an idealization

### The Empirical EDF Mapping

KMV/Moody's Analytics replaces the theoretical mapping with an **empirical** one:

$$
\text{EDF} = g(DD)
$$

where $g(\cdot)$ is constructed from a vast historical database of firm defaults:

1. For each firm-year in the database, compute DD at the start of the year
2. Group observations by DD into bins
3. Within each bin, compute the fraction of firms that defaulted within the year
4. Fit a smooth, monotonically decreasing function through these empirical points

### Properties of the EDF Mapping

The empirical mapping $g(DD)$ typically satisfies:

- $g(DD) > N(-DD)$ for most DD values (heavier tails than normal)
- The difference $g(DD) - N(-DD)$ is largest for intermediate DD
- At very high DD ($> 6$), both the theoretical and empirical probabilities are negligible
- At very low DD ($< 1$), both approaches give high probabilities

!!! info "EDF Scale"
    EDFs are reported in basis points (bp) or percentages:

    - AAA-rated firms: EDF $\approx$ 1--5 bp (0.01%--0.05%)
    - BBB-rated firms: EDF $\approx$ 20--50 bp (0.20%--0.50%)
    - B-rated firms: EDF $\approx$ 200--800 bp (2%--8%)
    - CCC-rated firms: EDF $\approx$ 1000--3500 bp (10%--35%)

---

## Practical Implementation

### Input Data Requirements

| Input | Source | Frequency |
|-------|--------|-----------|
| Equity price $E_0$ | Stock exchange | Daily |
| Equity volatility $\sigma_E$ | Historical returns or option-implied | Daily/Weekly |
| Short-term debt (STD) | Balance sheet filings | Quarterly |
| Long-term debt (LTD) | Balance sheet filings | Quarterly |
| Risk-free rate $r$ | Treasury curve | Daily |
| Expected asset return $\mu_V$ | CAPM or historical | Model-dependent |

### Asset Drift Estimation

The physical drift $\mu_V$ is needed for DD but is difficult to estimate precisely. Common approaches:

1. **CAPM:** $\mu_V = r + \beta_V (\mu_M - r)$ where $\beta_V$ is the asset beta
2. **Equity-based:** $\mu_V \approx \mu_E \cdot (E_0/V_0)$ (de-leveraging equity return)
3. **Industry average:** Use sector-specific expected returns
4. **Simplification:** Some implementations set $\mu_V = r$ (risk-neutral drift), accepting the resulting bias

!!! warning "Sensitivity to Drift"
    The DD is sensitive to $\mu_V$ for long horizons. A 2% change in expected return can shift DD by 0.3--0.5 standard deviations for a 1-year horizon, significantly affecting the EDF.

### Time Horizon

The standard KMV horizon is $T = 1$ year, but EDF can be computed for other horizons:

- **Term structure of EDF:** Compute DD for $T = 1, 2, 3, 5$ years
- **Cumulative EDF:** Probability of default within $T$ years
- **Forward EDF:** Marginal default probability in year $(T, T+1)$ given survival to $T$

---

## Numerical Example

**Observable data:**

- Equity value: $E_0 = \$45$ per share, 10 million shares outstanding, so $E_0 = \$450$ million
- Equity volatility: $\sigma_E = 35\%$ (annualized)
- Short-term debt: STD = \$200 million
- Long-term debt: LTD = \$300 million
- Risk-free rate: $r = 4\%$
- Expected asset return: $\mu_V = 8\%$
- Horizon: $T = 1$ year

**Step 1: Default point**

$$
\text{DP} = 200 + 0.5 \times 300 = \$350 \text{ million}
$$

**Step 2: Calibration (after convergence)**

Starting from $V_0^{(0)} = 450 + 350 e^{-0.04} = \$786$ million and iterating:

After convergence: $V_0 = \$780$ million, $\sigma_V = 20.2\%$

**Step 3: Distance to default**

$$
DD = \frac{\ln(780/350) + (0.08 - 0.0202^2/2)(1)}{0.202 \times 1} = \frac{0.8002 + 0.0596}{0.202} = \frac{0.8598}{0.202} = 4.26
$$

**Step 4: Default probability**

Naive normal: $N(-4.26) = 0.001\% \approx 1$ bp

Empirical EDF: $g(4.26) \approx 0.10\% = 10$ bp (from KMV database)

The empirical EDF is roughly 10 times the naive normal prediction, reflecting the fat tails of real-world default distributions.

---

## Strengths and Limitations

### Strengths

1. **Market-based:** Uses equity prices that update continuously and reflect forward-looking information
2. **Empirically validated:** The EDF mapping is calibrated to actual defaults, not a theoretical distribution
3. **Wide applicability:** Can be applied to any publicly traded firm
4. **Timely:** Daily updating as equity prices change
5. **Transparent metric:** DD has an intuitive interpretation

### Limitations

1. **Equity market dependence:** Requires liquid, efficiently priced equity
2. **Capital structure simplification:** Real firms have complex liability structures beyond STD + LTD
3. **Static debt:** Assumes debt is constant over the horizon
4. **Drift estimation:** Physical drift $\mu_V$ is poorly estimated and affects DD
5. **Model dependence:** The Merton-based calibration may be misspecified
6. **Private firms:** Cannot be applied directly without equity data (modified approaches exist)

### Comparison with Rating Agencies

| Feature | KMV/EDF | Rating Agencies |
|---------|---------|-----------------|
| Update frequency | Daily | Months/Years |
| Information source | Market prices | Fundamental analysis |
| Forward-looking | Yes (via equity) | Partially (through-the-cycle) |
| Lead time before default | 1--2 years | Typically shorter |
| Point-in-time vs through-cycle | Point-in-time | Through-the-cycle |

Empirical studies show that EDF tends to **lead** rating changes by 6--18 months, reflecting the timeliness of market information.

---

## Extensions

### Multi-Period and Term-Structure EDF

The 1-year EDF can be extended to a **term structure** by computing DD at multiple horizons:

$$
DD(T) = \frac{\ln(V_0/\text{DP}) + (\mu_V - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
$$

The cumulative default probability increases with $T$, and forward default rates can be extracted.

### Portfolio Applications

In portfolio credit risk, individual firm EDFs are combined with default correlations to compute:

- Portfolio loss distributions
- Economic capital requirements
- Concentration risk measures

The **asset correlation** between firms $i$ and $j$ is estimated from equity return correlations:

$$
\rho_{ij}^V = \text{Corr}(\ln V_T^i, \ln V_T^j) \approx \text{Corr}(R_E^i, R_E^j)
$$

after de-leveraging.

---

## Key Takeaways

- The KMV model operationalizes the Merton framework by extracting asset parameters from equity data
- The default point is empirically set as STD + 0.5 LTD, capturing typical default behavior
- Distance to default measures the number of standard deviations from the default boundary
- The empirical EDF mapping replaces the theoretical normal CDF with historically calibrated default frequencies
- DD/EDF is a point-in-time, market-based credit risk measure that typically leads rating agency actions
- Calibration requires iterative solution of a nonlinear system linking equity and asset parameters

---

## Further Reading

- Crosbie, P., & Bohn, J. (2003). Modeling default risk. *Moody's KMV Technical Document*.
- Vassalou, M., & Xing, Y. (2004). Default risk in equity returns. *Journal of Finance*, 59(2), 831--868.
- Duffie, D., Saita, L., & Wang, K. (2007). Multi-period corporate default prediction with stochastic covariates. *Journal of Financial Economics*, 83(3), 635--665.
- Bharath, S. T., & Shumway, T. (2008). Forecasting default with the Merton distance to default model. *Review of Financial Studies*, 21(3), 1339--1369.

---

## Exercises

**Exercise 1.** A firm has equity value $E_0 = 50$, total liabilities $D = 80$ (with short-term debt 30, long-term debt 50, default point $= 30 + 0.5 \times 50 = 55$), equity volatility $\sigma_E = 45\%$, and expected asset return $\mu = 8\%$. Solve the Merton system to find $V_0$ and $\sigma_V$, then compute the distance to default:

$$
DD = \frac{\ln(V_0 / \text{DPT}) + (\mu - \sigma_V^2/2) \times 1}{\sigma_V \times 1}
$$

---

**Exercise 2.** The KMV model maps distance to default (DD) to expected default frequency (EDF) using an empirical database rather than the normal distribution. Explain why $N(-DD)$ (the Merton model's theoretical default probability) typically underestimates the actual default rate. What empirical features (fat tails, model error) account for the discrepancy?

---

**Exercise 3.** Two firms have the same equity value ($E_0 = 40$) and asset volatility ($\sigma_V = 20\%$), but Firm A has debt $D = 60$ and Firm B has debt $D = 90$. Compute the asset values $V_0^A$ and $V_0^B$ (approximately, using $V_0 \approx E_0 + D$). Then compute the distance to default for each firm and explain which firm has higher default risk.

---

**Exercise 4.** Explain the KMV "default point" convention: DPT = Short-term Debt + 0.5 $\times$ Long-term Debt. Why is only half of long-term debt included? What economic assumption about debt rollovers motivates this choice?

---

**Exercise 5.** A firm's distance to default drops from DD = 4.5 to DD = 2.0 over one year. Describe the changes in the firm's financial condition that could cause this decline. What actions might the firm's management, creditors, and rating agencies take in response?

---

**Exercise 6.** Compare the KMV distance-to-default approach with rating-based credit assessment (e.g., Moody's or S&P ratings). Discuss the advantages of DD as a continuous, market-based measure versus discrete ratings. What are the limitations of relying solely on market-implied measures?
