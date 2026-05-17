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

Recall (see [§ Calibration: Inferring Asset Parameters](firm_value_models_merton.md#calibration-inferring-asset-parameters)). With DP in place of $D$:

$$
E_0 = V_0 N(d_1) - \text{DP}\,e^{-rT} N(d_2), \qquad \sigma_E = \frac{V_0 N(d_1)}{E_0}\,\sigma_V,
$$

where $d_1 = [\ln(V_0/\text{DP}) + (r+\sigma_V^2/2)T]/(\sigma_V\sqrt{T})$ and $d_2 = d_1 - \sigma_V\sqrt{T}$.

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

??? success "Solution to Exercise 1"
    **Given:** $E_0 = 50$, total liabilities $D = 80$ (STD = 30, LTD = 50), default point DP $= 30 + 0.5 \times 50 = 55$, $\sigma_E = 0.45$, $\mu = 0.08$, $r = 0.04$, $T = 1$.

    **Step 1: Set up the Merton system.**

    **Equation 1 (Equity pricing):**

    $$
    E_0 = V_0 N(d_1) - \text{DP} \cdot e^{-rT} N(d_2) \implies 50 = V_0 N(d_1) - 55 e^{-0.04} N(d_2)
    $$

    where $d_1 = \frac{\ln(V_0/55) + (0.04 + \sigma_V^2/2)}{sigma_V}$, $d_2 = d_1 - \sigma_V$.

    **Equation 2 (Volatility linkage):**

    $$
    \sigma_E E_0 = N(d_1) \sigma_V V_0 \implies 0.45 \times 50 = N(d_1) \sigma_V V_0 \implies 22.5 = N(d_1) \sigma_V V_0
    $$

    **Step 2: Iterative solution.**

    **Iteration 0:** Initialize $V_0^{(0)} = E_0 + \text{DP} \cdot e^{-rT} = 50 + 55 \times 0.9608 = 50 + 52.84 = 102.84$.

    **Iteration 1:** From Equation 2:

    $$
    \sigma_V^{(0)} = \frac{22.5}{V_0^{(0)} N(d_1^{(0)})}
    $$

    Compute $d_1^{(0)}$ using an initial guess $\sigma_V \approx 0.22$:

    $$
    d_1 = \frac{\ln(102.84/55) + (0.04 + 0.0242)}{0.22} = \frac{0.6263 + 0.0642}{0.22} = \frac{0.6905}{0.22} = 3.139
    $$

    $N(3.139) \approx 0.9992$.

    $$
    \sigma_V^{(1)} = \frac{22.5}{102.84 \times 0.9992} = \frac{22.5}{102.76} = 0.2189
    $$

    Update $V_0^{(1)}$ from Equation 1 with $\sigma_V = 0.2189$:

    $$
    d_1 = \frac{\ln(V_0/55) + (0.04 + 0.02395)}{0.2189}, \quad d_2 = d_1 - 0.2189
    $$

    Solving $50 = V_0 N(d_1) - 52.84 N(d_2)$ numerically yields $V_0^{(1)} \approx 103$.

    After several iterations (typically 5--10), convergence gives approximately:

    $$
    V_0 \approx 103, \quad \sigma_V \approx 0.219
    $$

    **Step 3: Distance to default.**

    $$
    DD = \frac{\ln(V_0/\text{DP}) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}} = \frac{\ln(103/55) + (0.08 - 0.024)}{0.219}
    $$

    $$
    = \frac{0.6282 + 0.056}{0.219} = \frac{0.6842}{0.219} = 3.12
    $$

    **Interpretation:** The firm's expected asset value is approximately 3.12 standard deviations above the default point. Using the naive normal mapping, $\mathbb{P}(\text{default}) = N(-3.12) \approx 0.09\%$. The empirical KMV mapping would give a somewhat higher EDF (typically 2--5 times the normal prediction).

---

**Exercise 2.** The KMV model maps distance to default (DD) to expected default frequency (EDF) using an empirical database rather than the normal distribution. Explain why $N(-DD)$ (the Merton model's theoretical default probability) typically underestimates the actual default rate. What empirical features (fat tails, model error) account for the discrepancy?

??? success "Solution to Exercise 2"
    **Why $N(-DD)$ underestimates actual default rates:**

    The theoretical Merton default probability $N(-DD)$ relies on the assumption that $\ln(V_T/V_0)$ is normally distributed. In reality, several factors cause actual default rates to exceed this theoretical prediction:

    **1. Fat tails in asset return distributions.**

    Real asset returns exhibit **leptokurtosis** (fat tails): extreme moves are more frequent than predicted by the normal distribution. This means:

    - Large negative asset returns (which cause default) occur more often than the normal model predicts.
    - The probability mass in the left tail of the asset return distribution is higher than $N(-DD)$.
    - Empirically, asset return distributions have excess kurtosis of 3--10, substantially inflating tail probabilities.

    For example, a firm with $DD = 4$ has $N(-4) = 0.003\%$ under normality, but observed default rates for such firms are typically 5--10 times higher.

    **2. Jump risk.**

    Firm value can experience sudden, discontinuous drops due to:

    - Fraud revelations (e.g., Enron, Worldcom)
    - Regulatory actions
    - Sudden loss of a major customer or contract
    - Natural disasters or catastrophic events

    These jumps are not captured by the continuous diffusion model. A firm with $DD = 5$ under the diffusion assumption could default instantly if asset value jumps down by 50%.

    **3. Model misspecification.**

    The Merton model assumes:

    - Constant asset volatility (in reality, $\sigma_V$ is stochastic and increases during distress)
    - Simple capital structure (real firms have complex, state-dependent liabilities)
    - Constant interest rates (rates and credit risk are correlated)
    - Log-normal asset returns (the true distribution is unknown)

    Each of these simplifications introduces systematic bias. The combined effect is that the model underestimates the probability of extreme events.

    **4. Contagion and systemic risk.**

    Defaults are correlated across firms through:

    - Common macroeconomic factors (recessions increase many firms' default probability simultaneously)
    - Financial network effects (one firm's default can trigger others)
    - Industry-specific shocks

    The single-firm Merton model does not capture these dependence effects, which inflate the actual frequency of defaults observed in the historical database.

    **5. Default boundary uncertainty.**

    The theoretical default point (face value of debt) may not match the actual trigger. Firms may default above or below the theoretical boundary due to liquidity constraints, strategic default decisions, or creditor coordination failures.

    The KMV empirical mapping $g(DD)$ addresses all of these issues by bypassing the normality assumption entirely and using observed historical default frequencies, which automatically incorporate fat tails, jumps, model error, and other factors.

---

**Exercise 3.** Two firms have the same equity value ($E_0 = 40$) and asset volatility ($\sigma_V = 20\%$), but Firm A has debt $D = 60$ and Firm B has debt $D = 90$. Compute the asset values $V_0^A$ and $V_0^B$ (approximately, using $V_0 \approx E_0 + D$). Then compute the distance to default for each firm and explain which firm has higher default risk.

??? success "Solution to Exercise 3"
    **Given:** Both firms have $E_0 = 40$ and $\sigma_V = 0.20$. Firm A has $D_A = 60$; Firm B has $D_B = 90$. Use $\mu = r = 0.05$ and $T = 1$ for simplicity.

    **Step 1: Approximate asset values.**

    Using the approximation $V_0 \approx E_0 + D$ (sum of equity and debt):

    $$
    V_0^A \approx 40 + 60 = 100, \quad V_0^B \approx 40 + 90 = 130
    $$

    Note: This is an approximation. The exact values would require solving the nonlinear Merton system. In practice, $V_0 > E_0 + De^{-rT}$ due to the option value of equity.

    **Step 2: Default points.**

    Using DP $= D$ for simplicity (assuming all debt is short-term):

    $$
    \text{DP}^A = 60, \quad \text{DP}^B = 90
    $$

    **Step 3: Distance to default.**

    For Firm A:

    $$
    DD^A = \frac{\ln(100/60) + (0.05 - 0.02) \times 1}{0.20 \times 1} = \frac{0.5108 + 0.03}{0.20} = \frac{0.5408}{0.20} = 2.70
    $$

    For Firm B:

    $$
    DD^B = \frac{\ln(130/90) + (0.05 - 0.02) \times 1}{0.20 \times 1} = \frac{0.3677 + 0.03}{0.20} = \frac{0.3977}{0.20} = 1.99
    $$

    **Step 4: Comparison.**

    | Metric | Firm A | Firm B |
    |--------|--------|--------|
    | Asset value $V_0$ | 100 | 130 |
    | Debt $D$ | 60 | 90 |
    | Leverage $D/V_0$ | 60% | 69% |
    | DD | 2.70 | 1.99 |
    | $N(-DD)$ | 0.35% | 2.33% |

    **Firm B has higher default risk** despite having a larger total asset value. The reason is **leverage**: Firm B's debt ($D_B = 90$) is much larger relative to its assets ($V_0^B = 130$), giving a leverage ratio of 69% versus 60% for Firm A. The distance to default is determined by the ratio $V_0/\text{DP}$, not by the absolute level of assets or equity.

    In the KMV framework, both firms have the same equity value and asset volatility, but Firm B's higher debt burden places it closer to the default boundary. The naive default probability for Firm B ($2.33\%$) is roughly 7 times that of Firm A ($0.35\%$).

---

**Exercise 4.** Explain the KMV "default point" convention: DPT = Short-term Debt + 0.5 $\times$ Long-term Debt. Why is only half of long-term debt included? What economic assumption about debt rollovers motivates this choice?

??? success "Solution to Exercise 4"
    **The KMV default point convention: DP = STD + 0.5 $\times$ LTD.**

    **Why only half of long-term debt is included:**

    The default point is calibrated to reflect the empirical observation that firms typically default when their asset value falls to a level **between short-term debt and total debt**, not at total debt. The reasons are:

    **1. Short-term debt must be repaid or rolled over.**

    Short-term liabilities (maturing within one year) represent **hard obligations** that must be met on schedule. These include:

    - Commercial paper maturities
    - Bank credit line drawdowns
    - Trade payables
    - Current portion of long-term debt

    Failure to meet these obligations triggers immediate default. Therefore, STD enters the default point at full face value.

    **2. Long-term debt provides flexibility.**

    Long-term obligations (maturing beyond one year) do not require immediate repayment. The firm has several options:

    - **Renegotiation:** Creditors may agree to modify terms (maturity extension, coupon reduction) to avoid the costs of bankruptcy.
    - **Covenant waivers:** Even if covenants are technically violated, creditors may waive the violation if forced liquidation would destroy value.
    - **Partial repayment:** The firm may be able to service interest on long-term debt even when unable to repay principal.
    - **Refinancing:** If markets allow, long-term debt can be refinanced, pushing maturities further out.

    Because of this flexibility, the full face value of LTD overstates the effective default trigger.

    **3. Empirical calibration.**

    The coefficient 0.5 on LTD was empirically determined by Moody's KMV from their extensive database of corporate defaults. By examining thousands of default events, they found that the asset value at the time of default was, on average, approximately equal to STD + 0.5 LTD. Key findings:

    - Firms with asset value above STD + LTD virtually never default.
    - Firms with asset value below STD almost always default.
    - The actual default trigger lies between these extremes, approximately at STD + 0.5 LTD.

    **Economic assumption about debt rollovers:**

    The 0.5 coefficient implicitly assumes that approximately half of long-term debt can be effectively "rolled over" or renegotiated during a one-year horizon. This reflects:

    - **Partial maturity:** Some LTD matures during the year and becomes effectively short-term.
    - **Creditor forbearance:** Long-term creditors have incentives to avoid triggering bankruptcy (which imposes deadweight costs) if there is a reasonable chance of recovery.
    - **Seniority structures:** Senior LTD holders may be protected even when the firm is distressed, reducing their incentive to trigger default.

    The coefficient 0.5 is a pragmatic approximation. In practice, it may vary by industry (capital-intensive industries may have different effective ratios), firm size, and credit quality.

---

**Exercise 5.** A firm's distance to default drops from DD = 4.5 to DD = 2.0 over one year. Describe the changes in the firm's financial condition that could cause this decline. What actions might the firm's management, creditors, and rating agencies take in response?

??? success "Solution to Exercise 5"
    **A firm's DD drops from 4.5 to 2.0 over one year.**

    This represents a severe deterioration in credit quality. A DD of 4.5 corresponds roughly to an A/BBB-rated firm (EDF $\approx$ 5--20 bp), while DD = 2.0 corresponds to a BB/B-rated firm (EDF $\approx$ 200--500 bp). The EDF has increased by roughly 10--100 times.

    **Changes in financial condition that could cause this decline:**

    From the DD formula $DD = \frac{\ln(V_0/\text{DP}) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}$, a decline in DD can result from:

    1. **Decrease in asset value $V_0$:** The most direct cause. This could reflect:
        - Operating losses eroding asset value
        - Write-downs of impaired assets (goodwill, bad loans, inventory)
        - A sharp decline in equity price (since $V_0$ is inferred from equity)
        - Loss of a major revenue source (customer, patent, contract)

    2. **Increase in the default point (DP):** Rising debt levels:
        - New borrowing (e.g., leveraged acquisition, emergency credit line drawdown)
        - Maturity of long-term debt converting to short-term obligations
        - Accumulation of trade payables

    3. **Increase in asset volatility $\sigma_V$:** Higher uncertainty increases the denominator and the $\sigma_V^2/2$ drag in the numerator:
        - Industry disruption increasing business risk
        - Loss of diversification (divesting stable businesses)
        - Equity volatility spike reflected in implied $\sigma_V$

    4. **Decrease in expected return $\mu$:** Lower growth prospects:
        - Deteriorating industry outlook
        - Loss of competitive advantage
        - Negative earnings revisions

    **Likely responses:**

    **Management actions:**

    - Cost-cutting and operational restructuring to preserve cash flow
    - Asset sales to raise liquidity and reduce leverage
    - Equity issuance (though difficult at depressed prices) to recapitalize
    - Dividend suspension to conserve cash
    - Renegotiation of debt terms (maturity extensions, covenant relief)
    - Engagement with financial advisors for turnaround planning

    **Creditor actions:**

    - Increased monitoring and enforcement of covenants
    - Tightening of credit lines or refusal to roll over short-term debt
    - Demand for additional collateral or guarantees
    - In severe cases, acceleration of debt and filing of involuntary bankruptcy petition
    - Formation of creditor committees to coordinate response

    **Rating agency actions:**

    - Placement on **negative watch** or **negative outlook** (warning of possible downgrade)
    - **Downgrade** from investment-grade (A/BBB) to speculative-grade (BB/B), with significant consequences:
        - Forced selling by institutional investors with investment-grade mandates
        - Increased borrowing costs
        - Potential covenant triggers tied to rating levels
    - Note: Rating agencies typically lag market-based measures like DD by 6--18 months, so the downgrade may come well after the DD decline.

---

**Exercise 6.** Compare the KMV distance-to-default approach with rating-based credit assessment (e.g., Moody's or S&P ratings). Discuss the advantages of DD as a continuous, market-based measure versus discrete ratings. What are the limitations of relying solely on market-implied measures?

??? success "Solution to Exercise 6"
    **KMV Distance-to-Default vs. Rating Agency Assessments:**

    **Advantages of DD as a continuous, market-based measure:**

    1. **Continuous scale:** DD is a real number (typically 0--8 for corporates), providing a fine-grained assessment of credit quality. Ratings are discrete categories (AAA, AA, A, BBB, etc.) with only about 20 notches, creating coarse bucketing. Two firms rated BBB may have very different default probabilities that DD would distinguish.

    2. **Timeliness:** DD updates daily (or even intraday) as equity prices change. It immediately reflects new information: earnings announcements, M&A activity, lawsuits, macroeconomic shocks. Rating agencies update ratings infrequently (every 6--18 months for stable firms), creating information staleness. Empirical studies show DD leads rating changes by 6--18 months.

    3. **Forward-looking:** Equity prices embed market expectations about future cash flows, profitability, and risk. DD inherits this forward-looking property. Rating agencies rely partly on historical financial statements, which are backward-looking. The "through-the-cycle" philosophy of rating agencies intentionally smooths over temporary fluctuations, potentially missing deterioration.

    4. **Objectivity:** DD is computed mechanically from market data, avoiding the subjective judgment inherent in rating committee decisions. This makes DD reproducible and free from analyst bias or conflicts of interest.

    5. **Universal applicability:** DD can be computed for any publicly traded firm with liquid equity, regardless of whether it has been rated by an agency. Many mid-cap and international firms lack agency ratings.

    **Limitations of relying solely on market-implied measures:**

    1. **Market noise and overreaction:** Equity prices can be driven by short-term sentiment, technical trading, and liquidity effects unrelated to credit fundamentals. DD may fluctuate excessively due to market microstructure noise, leading to false signals. Rating agencies' through-the-cycle approach filters out some of this noise.

    2. **Equity market efficiency assumption:** DD assumes equity prices efficiently reflect all information about firm value. In practice:
        - Information asymmetries may cause mispricing.
        - Thinly traded or illiquid equities may not reflect fundamentals.
        - During market crises, panic selling may depress equity prices below fundamental value, inflating DD-implied default probabilities.

    3. **Model dependence:** DD relies on the Merton structural model, which assumes GBM asset dynamics, constant volatility, and simple capital structure. Model misspecification introduces systematic bias. The calibration of $(V_0, \sigma_V)$ is sensitive to input assumptions.

    4. **Private firms excluded:** DD requires publicly traded equity. For private firms, banks, and sovereign borrowers, DD cannot be computed directly (though modified approaches exist using accounting data as proxies).

    5. **Short track record for tail events:** Market-implied measures are calibrated to recent history and may not reflect rare but severe scenarios (e.g., systemic crises, regime changes) that rating agencies may capture through qualitative assessment.

    6. **Procyclicality:** DD is inherently procyclical -- it improves during booms (as equity prices rise) and deteriorates during recessions. This can lead to under-estimation of risk during credit bubbles and over-estimation during distress, potentially amplifying financial cycles.

    **Practical recommendation:** The best credit assessment combines both approaches -- using DD/EDF for timely, quantitative monitoring and rating agency analysis for qualitative factors, industry expertise, and through-the-cycle stability. The two perspectives are complementary rather than substitutes.
