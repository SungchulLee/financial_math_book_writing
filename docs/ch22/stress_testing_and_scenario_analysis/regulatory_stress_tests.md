# Regulatory Stress Tests

**Regulatory stress tests** are supervisory exercises that assess the capital adequacy of financial institutions under hypothetical adverse economic scenarios. Unlike statistical risk measures (VaR, ES) that extrapolate from historical data, stress tests evaluate forward-looking resilience by projecting losses, revenues, and capital ratios over multi-year horizons under prescribed macroeconomic paths.

---

## Overview of Major Frameworks

### US: CCAR and DFAST

The **Comprehensive Capital Analysis and Review (CCAR)** and **Dodd-Frank Act Stress Tests (DFAST)** are conducted annually by the Federal Reserve for large bank holding companies (assets $\ge$ \$100 billion).

**Key features:**

- **Scenarios:** Baseline, adverse, and severely adverse scenarios prescribed by the Fed
- **Horizon:** 9 quarters (2.25 years)
- **Capital planning:** Banks submit capital plans (dividends, buybacks) evaluated against stressed projections
- **Binding constraint:** Minimum capital ratios must remain above regulatory minimums throughout the stress horizon

### EU: EBA Stress Tests

The **European Banking Authority (EBA)** coordinates EU-wide stress tests biennially:

- **Scenarios:** Baseline and adverse (designed by ESRB)
- **Methodology:** Constrained bottom-up (banks use own models within EBA constraints)
- **Static balance sheet assumption:** No management actions or balance sheet growth
- **Horizon:** 3 years
- **No pass/fail:** Results inform Pillar 2 capital guidance

### UK: Bank of England

The BoE conducts the **Annual Cyclical Scenario (ACS)** and **Biennial Exploratory Scenario (BES)**:

- ACS severity calibrated to the financial cycle
- BES explores emerging risks (e.g., climate, cyber)
- Includes a **system-wide stress test** examining amplification mechanisms

---

## Scenario Design

### Macroeconomic Variables

Regulatory scenarios specify paths for key macroeconomic variables over the stress horizon:

| Variable | Typical Severely Adverse |
|----------|------------------------|
| GDP growth | $-$6% to $-$8% cumulative |
| Unemployment rate | Peak 10--12% |
| Equity prices | $-$40% to $-$55% |
| House prices | $-$20% to $-$30% |
| Credit spreads | +400--600 bps |
| Interest rates | Scenario-dependent |
| CRE prices | $-$30% to $-$40% |

### Scenario Construction

Let $\mathbf{z}_t = (z_{1,t}, \ldots, z_{d,t})^\top$ denote the vector of macroeconomic variables at time $t$. The scenario specifies a deterministic path $\{\mathbf{z}_t^{\text{stress}}\}_{t=1}^H$ over the horizon $H$.

**Severity calibration:** Scenarios are typically designed to represent a **severe but plausible** event, calibrated to historical recession severities:

$$
\text{Severity} \approx \text{Conditional mean given recession} + k \cdot \sigma_{\text{recession}}
$$

where $k \in [1, 2]$ determines severity relative to historical recession distributions.

### Internal Consistency

Scenario variables must be internally consistent:

- GDP decline should be consistent with unemployment increase (Okun's law: $\Delta U \approx -0.5 \Delta \text{GDP}$)
- Interest rate paths should be consistent with monetary policy response
- Asset price declines should be consistent with economic severity

Consistency can be enforced using:

- **VAR models:** $\mathbf{z}_t = \mathbf{A} \mathbf{z}_{t-1} + \boldsymbol{\epsilon}_t$ with scenario-conditioned innovations
- **DSGE models:** Structural models ensuring general equilibrium consistency
- **Expert judgment:** Overlay adjustments to model-generated paths

---

## Loss Projection Models

### Credit Loss Models

Credit losses under stress are projected using models linking macroeconomic variables to default and loss parameters.

**Probability of Default (PD) under stress:**

$$
PD_t^{\text{stress}} = \Phi\left(\frac{\Phi^{-1}(\overline{PD}) + \sqrt{\rho} \cdot z_t}{\sqrt{1 - \rho}}\right)
$$

where $\overline{PD}$ is the through-the-cycle PD, $\rho$ is the asset correlation, and $z_t$ is a systematic factor driven by the macroeconomic scenario.

**Alternative regression-based approach:**

$$
\log\left(\frac{PD_t}{1 - PD_t}\right) = \beta_0 + \beta_1 \Delta\text{GDP}_t + \beta_2 \Delta U_t + \beta_3 \Delta\text{HPI}_t + \epsilon_t
$$

**Loss Given Default (LGD) under stress:**

$$
\text{LGD}_t^{\text{stress}} = \alpha_0 + \alpha_1 \Delta\text{HPI}_t + \alpha_2 \Delta\text{CRE}_t + \epsilon_t
$$

LGD increases under stress as collateral values decline and recovery rates deteriorate.

**Expected Credit Loss (ECL):**

$$
\text{ECL}_t = \text{EAD}_t \times PD_t^{\text{stress}} \times \text{LGD}_t^{\text{stress}}
$$

where $\text{EAD}_t$ is the exposure at default.

### Pre-Provision Net Revenue (PPNR)

**PPNR** represents earnings before loan loss provisions:

$$
\text{PPNR}_t = \text{NII}_t + \text{Non-Interest Income}_t - \text{Non-Interest Expense}_t
$$

where **Net Interest Income (NII)** depends on the interest rate scenario:

$$
\text{NII}_t = \sum_i \text{Asset}_i \times r_i^{\text{asset}}(\mathbf{z}_t) - \sum_j \text{Liability}_j \times r_j^{\text{liability}}(\mathbf{z}_t)
$$

Under stress, PPNR typically declines due to compressed net interest margins, lower fee income, and increased litigation/operational costs.

### Trading and Counterparty Losses

For trading book losses under the severely adverse scenario:

$$
L^{\text{trading}} = -\sum_i \Delta_i \cdot \Delta x_i^{\text{stress}} - \frac{1}{2} \sum_{i,j} \Gamma_{ij} \cdot \Delta x_i^{\text{stress}} \cdot \Delta x_j^{\text{stress}} + \text{CVA losses}
$$

The **Global Market Shock (GMS)** component applies instantaneous market moves to the trading book, while **Counterparty Default (CD)** scenarios model the failure of the bank's largest counterparties.

---

## Capital Projections

### Capital Ratio Under Stress

The key output is the projected **Common Equity Tier 1 (CET1) ratio** over the stress horizon:

$$
\text{CET1}_{t} = \frac{\text{CET1 Capital}_{t}}{\text{RWA}_{t}}
$$

where:

$$
\text{CET1 Capital}_t = \text{CET1 Capital}_{t-1} + \text{PPNR}_t - \text{Provisions}_t - \text{Trading Losses}_t - \text{Capital Actions}_t
$$

### Minimum Capital Requirements

The CET1 ratio must remain above regulatory minimums throughout the stress horizon:

| Requirement | Minimum |
|-------------|---------|
| CET1 minimum | 4.5% |
| CET1 + Capital Conservation Buffer | 7.0% |
| CET1 + CCB + G-SIB surcharge | 7.0--9.5% |
| Stress Capital Buffer (SCB) | Max of 2.5% or stressed decline |

### Stress Capital Buffer (SCB)

The **SCB** (introduced in 2020) replaces the fixed capital conservation buffer with a firm-specific buffer based on stress test results:

$$
\text{SCB} = \max\left(2.5\%, \, \text{CET1}_{t=0} - \min_{t \in [1,H]} \text{CET1}_t^{\text{stressed}} + \text{planned dividends}\right)
$$

This directly links capital requirements to stress test outcomes.

---

## Mathematical Framework for Stress Projections

### Multi-Period Capital Dynamics

The capital evolution can be written as a recursive system:

$$
K_t = K_{t-1} + R_t(\mathbf{z}_t) - L_t(\mathbf{z}_t) - D_t
$$

where:

- $K_t$ = CET1 capital at quarter $t$
- $R_t(\mathbf{z}_t)$ = revenue (PPNR) as a function of macroeconomic variables
- $L_t(\mathbf{z}_t)$ = losses (credit + trading + operational)
- $D_t$ = dividends and share repurchases

The capital ratio is:

$$
\text{CET1 Ratio}_t = \frac{K_t}{W_t(\mathbf{z}_t)}
$$

where $W_t$ = risk-weighted assets, which also vary under stress (e.g., credit migration increases RWA).

### Sensitivity Analysis

The **marginal impact** of a macroeconomic variable on the capital ratio:

$$
\frac{\partial \text{CET1 Ratio}_t}{\partial z_{j,t}} = \frac{1}{W_t}\left(\frac{\partial R_t}{\partial z_{j,t}} - \frac{\partial L_t}{\partial z_{j,t}}\right) - \frac{K_t}{W_t^2} \frac{\partial W_t}{\partial z_{j,t}}
$$

This identifies which macroeconomic variables have the largest impact on capital adequacy.

---

## Internal vs Supervisory Stress Testing

| Feature | Internal | Supervisory |
|---------|----------|-------------|
| Scenarios | Bank-designed | Regulator-prescribed |
| Purpose | Risk management | Capital adequacy assessment |
| Frequency | Ongoing | Annual or biennial |
| Models | Bank's own | Subject to supervisory review |
| Balance sheet | Dynamic (management actions) | Static (EBA) or planned (CCAR) |
| Disclosure | Internal | Public (aggregate results) |

### Complementary Roles

- **Internal stress tests** explore a wider range of scenarios tailored to the bank's specific risk profile
- **Supervisory tests** ensure comparability across institutions and set minimum capital requirements
- **Reverse stress tests** identify scenarios that would cause failure (complementing forward stress tests)

---

## Challenges and Limitations

### Model Risk

Stress test models project over horizons (2--3 years) far beyond typical model calibration periods. Key challenges:

- **Regime changes:** Historical relationships may not hold under stress
- **Nonlinearities:** Linear models may understate losses in severe scenarios
- **Tail dependence:** Correlations between risk factors typically increase under stress

### Procyclicality

Stress tests can be procyclical: tighter capital requirements during downturns may constrain lending, amplifying the recession. Mitigants include:

- Countercyclical capital buffers
- Dynamic severity calibration
- Through-the-cycle model components

### Scenario Limitations

Prescribed scenarios may not capture:

- Unprecedented events (e.g., pandemic, cyberattack)
- Institution-specific vulnerabilities
- Amplification mechanisms (fire sales, funding runs)

---

## Example: Simplified Stress Capital Projection

**Setup:** A bank with initial CET1 ratio of 12.0% and RWA of \$500B.

**Severely adverse scenario projections (cumulative over 9 quarters):**

| Component | Amount (\$B) |
|-----------|-------------|
| Initial CET1 capital | 60.0 |
| PPNR (stressed) | +18.0 |
| Credit losses | $-$25.0 |
| Trading losses | $-$8.0 |
| Operational losses | $-$3.0 |
| Capital actions (dividends) | $-$6.0 |
| RWA increase | +50.0 |

**Minimum CET1 capital:**

$$
K_{\min} = 60.0 + 18.0 - 25.0 - 8.0 - 3.0 - 6.0 = \$36.0\text{B}
$$

**Minimum CET1 ratio:**

$$
\text{CET1 Ratio}_{\min} = \frac{36.0}{550.0} = 6.5\%
$$

**Stress Capital Buffer:**

$$
\text{SCB} = \max(2.5\%, \, 12.0\% - 6.5\% + 1.2\%) = \max(2.5\%, 6.7\%) = 6.7\%
$$

The bank's total CET1 requirement becomes $4.5\% + 6.7\% = 11.2\%$.

---

## Key Takeaways

- Regulatory stress tests (CCAR/DFAST, EBA) assess capital adequacy under multi-year adverse scenarios
- Scenarios specify deterministic paths for macroeconomic variables that must be internally consistent
- Loss projections link macroeconomic variables to PD, LGD, PPNR, and trading losses via econometric models
- The capital ratio $\text{CET1}_t / \text{RWA}_t$ must remain above regulatory minimums throughout the stress horizon
- The Stress Capital Buffer directly links capital requirements to stress test outcomes
- Model risk is a major challenge: stress projections extrapolate well beyond calibration ranges
- Internal and supervisory stress tests serve complementary roles in risk management and capital planning

---

## Further Reading

- Board of Governors of the Federal Reserve System, "Dodd-Frank Act Stress Test Methodology"
- European Banking Authority, "EU-Wide Stress Test Methodological Note"
- Schuermann, T. (2014), "Stress Testing Banks," *International Journal of Forecasting*
- Kapinos, P. & Mitnik, O. (2016), "A Top-Down Approach to Stress-Testing Banks"
- Duffie, D. (2019), "Prone to Fail: The Pre-Crisis Financial System," *Journal of Economic Perspectives*
- Greenlaw, D., Kashyap, A., Schoenholtz, K., & Shin, H.S. (2012), "Stressed Out: Macroprudential Principles for Stress Testing"

---

## Exercises

**Exercise 1.** A bank has initial CET1 capital of \$70 billion and RWA of \$500 billion. Under a severely adverse scenario over 9 quarters, the bank projects PPNR of \$15B, credit losses of \$30B, trading losses of \$10B, operational losses of \$2B, dividends of \$5B, and a \$60B increase in RWA. Compute the minimum CET1 capital and the minimum CET1 ratio. Determine whether the bank passes the stress test assuming a minimum CET1 requirement of 4.5%. Also compute the Stress Capital Buffer (SCB).

??? success "Solution to Exercise 1"

    **Given:**

    - Initial CET1 capital: \$70B
    - Initial RWA: \$500B
    - PPNR (stressed): +\$15B
    - Credit losses: \$30B
    - Trading losses: \$10B
    - Operational losses: \$2B
    - Dividends: \$5B
    - RWA increase: \$60B

    **Step 1: Compute the minimum CET1 capital.**

    $$
    K_{\min} = 70 + 15 - 30 - 10 - 2 - 5 = \$38\text{B}
    $$

    **Step 2: Compute the minimum CET1 ratio.**

    The stressed RWA is $500 + 60 = \$560$B.

    $$
    \text{CET1 Ratio}_{\min} = \frac{38}{560} = 6.79\%
    $$

    **Step 3: Pass/fail determination.**

    The minimum CET1 requirement is 4.5%. Since $6.79\% > 4.5\%$, the bank **passes** the stress test.

    **Step 4: Compute the Stress Capital Buffer (SCB).**

    The initial CET1 ratio is:

    $$
    \text{CET1 Ratio}_0 = \frac{70}{500} = 14.0\%
    $$

    The planned dividend ratio over the stress horizon (approximate, using initial RWA for simplicity):

    $$
    \text{Dividend ratio} = \frac{5}{500} = 1.0\%
    $$

    The SCB formula is:

    $$
    \text{SCB} = \max\left(2.5\%, \; \text{CET1}_0 - \text{CET1}_{\min}^{\text{stressed}} + \text{planned dividends ratio}\right)
    $$

    $$
    \text{SCB} = \max\left(2.5\%, \; 14.0\% - 6.79\% + 1.0\%\right) = \max(2.5\%, 8.21\%) = 8.21\%
    $$

    The bank's total CET1 requirement becomes:

    $$
    4.5\% + 8.21\% = 12.71\%
    $$

    Since the bank's current CET1 ratio is 14.0%, it exceeds this combined requirement by $14.0\% - 12.71\% = 1.29$ percentage points.

---

**Exercise 2.** Consider the credit loss model under stress:

$$
PD_t^{\text{stress}} = \Phi\left(\frac{\Phi^{-1}(\overline{PD}) + \sqrt{\rho} \cdot z_t}{\sqrt{1 - \rho}}\right)
$$

For a portfolio with $\overline{PD} = 1.5\%$ and asset correlation $\rho = 0.15$, compute $PD^{\text{stress}}$ when the systematic factor takes the value $z = -2.5$ (representing a severely adverse macroeconomic shock). Compare this to the through-the-cycle PD and discuss the sensitivity of the stressed PD to the correlation parameter.

??? success "Solution to Exercise 2"

    **Given:** $\overline{PD} = 1.5\% = 0.015$, $\rho = 0.15$, $z = -2.5$.

    **Step 1: Compute $\Phi^{-1}(\overline{PD})$.**

    $$
    \Phi^{-1}(0.015) \approx -2.170
    $$

    **Step 2: Apply the Vasicek/Gordy formula.**

    $$
    PD^{\text{stress}} = \Phi\left(\frac{\Phi^{-1}(\overline{PD}) + \sqrt{\rho} \cdot z}{\sqrt{1 - \rho}}\right) = \Phi\left(\frac{-2.170 + \sqrt{0.15} \times (-2.5)}{\sqrt{0.85}}\right)
    $$

    Compute the components:

    $$
    \sqrt{0.15} \approx 0.3873, \quad \sqrt{0.85} \approx 0.9220
    $$

    $$
    \text{Numerator} = -2.170 + 0.3873 \times (-2.5) = -2.170 - 0.9682 = -3.1382
    $$

    $$
    \text{Argument} = \frac{-3.1382}{0.9220} = -3.4037
    $$

    $$
    PD^{\text{stress}} = \Phi(-3.4037) \approx 0.000333 = 0.0333\%
    $$

    Wait---this gives a *lower* PD than the through-the-cycle PD, which is counterintuitive. Let us reconsider the model.

    In the standard Vasicek single-factor model, the systematic factor $z$ enters as a common shock to all obligors. The conditional PD given the systematic factor is:

    $$
    PD(z) = \Phi\left(\frac{\Phi^{-1}(\overline{PD}) - \sqrt{\rho} \cdot z}{\sqrt{1 - \rho}}\right)
    $$

    Note the **minus sign** before $\sqrt{\rho} \cdot z$: when $z$ is negative (adverse economy), defaults increase. With $z = -2.5$:

    $$
    PD^{\text{stress}} = \Phi\left(\frac{-2.170 - 0.3873 \times (-2.5)}{0.9220}\right) = \Phi\left(\frac{-2.170 + 0.9682}{0.9220}\right) = \Phi\left(\frac{-1.2018}{0.9220}\right) = \Phi(-1.3035)
    $$

    $$
    PD^{\text{stress}} = \Phi(-1.3035) \approx 0.0963 = 9.63\%
    $$

    However, the exercise states the formula with a plus sign: $\Phi^{-1}(\overline{PD}) + \sqrt{\rho} \cdot z$. Using this version, a negative $z$ (severely adverse) gives:

    $$
    PD^{\text{stress}} = \Phi\left(\frac{-2.170 + 0.3873 \times (-2.5)}{0.9220}\right) = \Phi(-3.4037) \approx 0.034\%
    $$

    This is lower than the TTC PD, which makes no economic sense for an adverse scenario. The correct interpretation is that the exercise's formula uses the convention where $z_t$ represents the macroeconomic scenario factor, and a **negative** value indicates severe stress. The formula as written:

    $$
    PD^{\text{stress}} = \Phi\left(\frac{\Phi^{-1}(\overline{PD}) + \sqrt{\rho} \cdot z_t}{\sqrt{1-\rho}}\right)
    $$

    produces high PDs when $z_t$ is **positive** (i.e., the systematic factor pushes defaults higher). If $z = -2.5$ represents a severely adverse macroeconomic shock, we should interpret this as $z = +2.5$ in the formula (or equivalently, use the standard convention $\Phi^{-1}(\overline{PD}) - \sqrt{\rho} \cdot z$ with $z = -2.5$).

    Using $z_t = +2.5$ in the formula as given:

    $$
    PD^{\text{stress}} = \Phi\left(\frac{-2.170 + 0.3873 \times 2.5}{0.9220}\right) = \Phi\left(\frac{-2.170 + 0.9682}{0.9220}\right) = \Phi\left(\frac{-1.2018}{0.9220}\right) = \Phi(-1.3035)
    $$

    $$
    PD^{\text{stress}} \approx 9.63\%
    $$

    **Step 3: Compare to through-the-cycle PD.**

    The ratio is:

    $$
    \frac{PD^{\text{stress}}}{\overline{PD}} = \frac{9.63\%}{1.5\%} \approx 6.4\times
    $$

    The stressed PD is approximately **6.4 times** the through-the-cycle PD.

    **Step 4: Sensitivity to the correlation parameter $\rho$.**

    The correlation $\rho$ determines how sensitive the portfolio's default rate is to the systematic factor:

    - **Higher $\rho$:** Defaults are more concentrated (higher sensitivity to the common factor). Under stress, the PD rises more dramatically, but the unconditional PD remains the same.
    - **Lower $\rho$:** Defaults are more idiosyncratic. Even a severe systematic shock produces a more modest increase in PD because each borrower's default is mostly driven by idiosyncratic factors.

    For example, with $\rho = 0.25$ instead of $0.15$:

    $$
    PD^{\text{stress}} = \Phi\left(\frac{-2.170 + 0.5 \times 2.5}{\sqrt{0.75}}\right) = \Phi\left(\frac{-0.920}{0.8660}\right) = \Phi(-1.062) \approx 14.4\%
    $$

    This is nearly 10 times the TTC PD, versus 6.4 times with $\rho = 0.15$. The correlation parameter is a critical driver of stress test severity.

---

**Exercise 3.** Explain the difference between the static balance sheet assumption (EBA) and the planned capital actions approach (CCAR). A bank with a current CET1 ratio of 12% plans to pay \$3 billion in dividends and repurchase \$2 billion in shares over the stress horizon. Under the EBA static approach, these actions are excluded. Under CCAR, they are included. If the bank's stressed capital decline before capital actions is 4 percentage points, compute the minimum CET1 ratio under each framework. Discuss which framework is more conservative from a capital adequacy perspective.

??? success "Solution to Exercise 3"

    **Part 1: Static balance sheet (EBA) vs. planned capital actions (CCAR).**

    - **EBA static approach:** The bank's balance sheet is frozen at the starting point. No management actions (dividends, buybacks, new business) are allowed. The rationale is to measure the pure impact of the stress scenario without the confounding effect of management responses, ensuring comparability across banks.

    - **CCAR planned approach:** Banks submit their actual capital plans (planned dividends and share repurchases) as part of the stress test. These capital distributions are deducted from CET1 over the stress horizon. The rationale is to test whether the bank can maintain adequate capital while executing its planned distributions.

    **Part 2: Compute minimum CET1 ratio under each framework.**

    Current CET1 ratio: 12%. Stressed capital decline before capital actions: 4 percentage points.

    **Under EBA (static):**

    No capital actions are included, so:

    $$
    \text{CET1 Ratio}_{\min}^{\text{EBA}} = 12\% - 4\% = 8.0\%
    $$

    **Under CCAR (planned actions):**

    Capital actions: \$3B dividends + \$2B buybacks = \$5B total. To convert to ratio impact, we need the RWA. Let us assume initial CET1 capital corresponds to the 12% ratio. If RWA = $R$, then CET1 capital = $0.12R$.

    The capital action impact on the ratio is $5/R$. Without knowing $R$ explicitly, we note that the question states the stressed capital decline is 4 percentage points *before* capital actions. The capital actions further reduce the ratio.

    Assuming the \$5B in capital actions translates to a ratio impact of (say) approximately 1 percentage point (i.e., RWA $\approx$ \$500B), then:

    $$
    \text{CET1 Ratio}_{\min}^{\text{CCAR}} = 12\% - 4\% - 1\% = 7.0\%
    $$

    More generally, if the capital action ratio impact is $\delta$:

    $$
    \text{CET1 Ratio}_{\min}^{\text{CCAR}} = 12\% - 4\% - \delta = 8\% - \delta
    $$

    **Part 3: Which framework is more conservative?**

    The CCAR framework is more conservative from a capital adequacy perspective because it includes the depletion of capital from dividends and buybacks. Under the EBA approach, the bank appears better capitalized at $8.0\%$, but this ignores the fact that the bank intends to distribute \$5B to shareholders during the stress period.

    However, one could argue the EBA approach is more conservative in a different sense: by assuming a static balance sheet, it prevents banks from claiming credit for optimistic management actions (e.g., reducing risky assets or raising capital) that may not be feasible during a real crisis.

    In practice, the CCAR approach provides a more realistic assessment of capital adequacy because it reflects what the bank actually plans to do. If the resulting capital ratio is too low, the Fed can object to the capital plan and require the bank to reduce distributions.

---

**Exercise 4.** The marginal impact of a macroeconomic variable on the capital ratio is

$$
\frac{\partial \text{CET1 Ratio}_t}{\partial z_{j,t}} = \frac{1}{W_t}\left(\frac{\partial R_t}{\partial z_{j,t}} - \frac{\partial L_t}{\partial z_{j,t}}\right) - \frac{K_t}{W_t^2} \frac{\partial W_t}{\partial z_{j,t}}
$$

Explain each of the three terms on the right-hand side. For a bank where GDP growth affects both credit losses ($\partial L / \partial z_{\text{GDP}} < 0$, since lower GDP increases losses) and RWA ($\partial W / \partial z_{\text{GDP}} < 0$, since lower GDP increases risk weights), discuss why the total impact on the CET1 ratio may be larger than the loss effect alone.

??? success "Solution to Exercise 4"

    **The three terms in the marginal impact formula:**

    $$
    \frac{\partial \text{CET1 Ratio}_t}{\partial z_{j,t}} = \underbrace{\frac{1}{W_t}\frac{\partial R_t}{\partial z_{j,t}}}_{\text{(i) Revenue effect}} - \underbrace{\frac{1}{W_t}\frac{\partial L_t}{\partial z_{j,t}}}_{\text{(ii) Loss effect}} - \underbrace{\frac{K_t}{W_t^2}\frac{\partial W_t}{\partial z_{j,t}}}_{\text{(iii) RWA effect}}
    $$

    **(i) Revenue effect:** $\frac{1}{W_t}\frac{\partial R_t}{\partial z_{j,t}}$

    This captures how the macroeconomic variable $z_j$ affects pre-provision net revenue. For GDP growth: higher GDP generally increases revenues (more lending, higher fee income, better trading conditions). The coefficient $\partial R / \partial z_{\text{GDP}} > 0$, so a GDP decline reduces this term, lowering the capital ratio.

    **(ii) Loss effect:** $\frac{1}{W_t}\frac{\partial L_t}{\partial z_{j,t}}$

    This captures how $z_j$ affects credit, market, and operational losses. For GDP: $\partial L / \partial z_{\text{GDP}} < 0$ (lower GDP increases losses, i.e., losses are negatively related to GDP). Therefore, $-\frac{1}{W_t}\frac{\partial L_t}{\partial z_{\text{GDP}}}$ is negative when GDP falls, reducing the capital ratio.

    **(iii) RWA effect:** $\frac{K_t}{W_t^2}\frac{\partial W_t}{\partial z_{j,t}}$

    This captures how $z_j$ affects risk-weighted assets. For GDP: $\partial W / \partial z_{\text{GDP}} < 0$ (lower GDP increases risk weights because credit quality deteriorates---ratings migrate downward, increasing the risk weight of loans). Since $K_t / W_t^2 > 0$, the term $-\frac{K_t}{W_t^2}\frac{\partial W_t}{\partial z_{\text{GDP}}}$ is positive when GDP falls.

    Wait---let us be more careful. When GDP falls ($\Delta z_{\text{GDP}} < 0$):

    - $\partial W / \partial z_{\text{GDP}} < 0$, so $\Delta W = (\partial W / \partial z_{\text{GDP}}) \cdot \Delta z_{\text{GDP}} > 0$. RWA **increases**.
    - The third term is $-\frac{K_t}{W_t^2}\frac{\partial W_t}{\partial z_{\text{GDP}}}$. Since $\partial W / \partial z_{\text{GDP}} < 0$, this term is positive. When multiplied by $\Delta z_{\text{GDP}} < 0$, the contribution is negative.

    **Why the total impact is larger than the loss effect alone:**

    When GDP declines:

    1. Losses increase (term ii reduces the ratio by depleting the numerator $K_t$).
    2. RWA increases (term iii reduces the ratio by inflating the denominator $W_t$).

    Both effects work in the same direction, amplifying the decline in the CET1 ratio:

    $$
    \text{CET1 Ratio} = \frac{K_t}{W_t}
    $$

    A GDP decline simultaneously *reduces the numerator* (through higher losses and lower revenues) and *increases the denominator* (through higher risk weights). This "double hit" makes the CET1 ratio more sensitive to GDP than the pure loss channel would suggest.

    **Numerical illustration:** Suppose $K_t = 60$, $W_t = 500$. CET1 ratio = 12%. If losses increase by 5 ($K$ falls to 55), ratio becomes $55/500 = 11.0\%$, a decline of 1.0 pp. If simultaneously RWA increases by 50 ($W$ rises to 550), ratio becomes $55/550 = 10.0\%$, a decline of 2.0 pp. The RWA effect doubles the impact versus losses alone.

---

**Exercise 5.** Discuss the procyclicality concern in regulatory stress testing. During a recession, stress test models calibrated to worsening data may project larger losses, leading to higher capital requirements at precisely the time when banks can least afford to raise capital. Describe three specific mitigants (mathematical or regulatory) that address this procyclicality. What is the role of the countercyclical capital buffer in this context?

??? success "Solution to Exercise 5"

    **The procyclicality concern:**

    Regulatory stress tests can amplify economic cycles through the following mechanism:

    1. **During a downturn:** Macro data worsens, stress test models (calibrated to recent data) project larger losses, stress test results deteriorate.
    2. **Higher capital requirements:** Worse stress test results lead to higher SCB or Pillar 2 capital requirements.
    3. **Capital-constrained banks:** Banks that cannot easily raise capital must reduce RWA by cutting lending.
    4. **Reduced lending worsens the downturn:** Less credit availability further depresses economic activity, leading to more defaults and worse data, creating a feedback loop.

    **Three specific mitigants:**

    **1. Countercyclical Capital Buffer (CCyB).**

    The CCyB is a time-varying capital requirement set by macroprudential authorities:

    - During credit booms: CCyB is increased (0--2.5% of RWA), building capital buffers.
    - During downturns: CCyB is released (set to 0%), freeing up capital for lending.

    Mathematically, the total capital requirement becomes:

    $$
    \text{CET1 requirement} = 4.5\% + \text{CCB} + \text{CCyB}(t) + \text{G-SIB surcharge}
    $$

    By releasing the CCyB during stress, regulators reduce the binding constraint precisely when banks face losses, mitigating the procyclical squeeze.

    **2. Through-the-cycle (TTC) model components.**

    Instead of using point-in-time (PIT) PD estimates that spike during downturns, models can incorporate through-the-cycle components:

    $$
    PD^{\text{model}} = \alpha \cdot PD^{\text{PIT}} + (1-\alpha) \cdot PD^{\text{TTC}}
    $$

    The TTC component remains stable across the cycle, dampening the procyclical sensitivity of loss projections. Basel II's IRB approach uses 12-month TTC PDs rather than purely PIT estimates for exactly this reason.

    **3. Dynamic severity calibration.**

    Regulators can adjust scenario severity countercyclically:

    - During economic expansions (when risks are building): Use more severe scenarios.
    - During recessions (when risks have materialized): Use relatively less severe scenarios, since the economy is already in the "stressed" state.

    The Fed's CCAR scenario design has partially adopted this approach: the severely adverse scenario's severity is calibrated relative to the current state, so if unemployment is already high, the prescribed increase may be smaller.

    **Additional mitigant: Capital conservation buffer restrictions.**

    The capital conservation buffer framework imposes **graduated restrictions** on distributions (dividends, buybacks, bonuses) as the CET1 ratio declines toward the minimum, rather than a cliff effect. This allows banks to continue operating while conserving capital organically:

    | CET1 Ratio Range | Maximum Payout Ratio |
    |---|---|
    | Above CCB threshold | No restriction |
    | 75--100% of CCB | 60% |
    | 50--75% of CCB | 40% |
    | 25--50% of CCB | 20% |
    | 0--25% of CCB | 0% |

    This graduated approach avoids the sharp procyclical contraction that would occur if banks were forced to immediately rebuild capital to a fixed threshold.

---

**Exercise 6.** A bank uses the logistic regression model

$$
\log\left(\frac{PD_t}{1 - PD_t}\right) = \beta_0 + \beta_1 \Delta\text{GDP}_t + \beta_2 \Delta U_t + \beta_3 \Delta\text{HPI}_t
$$

with estimated parameters $\beta_0 = -3.5$, $\beta_1 = -0.08$, $\beta_2 = 0.12$, $\beta_3 = -0.04$. Under the severely adverse scenario, $\Delta\text{GDP} = -6\%$, $\Delta U = +5\%$, and $\Delta\text{HPI} = -25\%$. Compute the stressed PD. If the through-the-cycle PD (setting all macro shocks to zero) is $\Phi(\text{logit}^{-1}(\beta_0))$, compute the ratio of stressed PD to baseline PD.

??? success "Solution to Exercise 6"

    **Step 1: Compute the stressed PD using the logistic regression.**

    $$
    \text{logit}(PD) = \beta_0 + \beta_1 \Delta\text{GDP} + \beta_2 \Delta U + \beta_3 \Delta\text{HPI}
    $$

    Under the severely adverse scenario: $\Delta\text{GDP} = -6$, $\Delta U = +5$, $\Delta\text{HPI} = -25$.

    $$
    \text{logit}(PD^{\text{stress}}) = -3.5 + (-0.08)(-6) + (0.12)(5) + (-0.04)(-25)
    $$

    $$
    = -3.5 + 0.48 + 0.60 + 1.00 = -1.42
    $$

    Convert from logit to probability:

    $$
    PD^{\text{stress}} = \frac{1}{1 + e^{-(-1.42)}} = \frac{1}{1 + e^{1.42}} = \frac{1}{1 + 4.1371} = \frac{1}{5.1371} \approx 0.1947 = 19.47\%
    $$

    **Step 2: Compute the baseline (through-the-cycle) PD.**

    Setting all macro shocks to zero:

    $$
    \text{logit}(PD^{\text{TTC}}) = \beta_0 = -3.5
    $$

    $$
    PD^{\text{TTC}} = \frac{1}{1 + e^{3.5}} = \frac{1}{1 + 33.115} = \frac{1}{34.115} \approx 0.02932 = 2.93\%
    $$

    **Step 3: Compute the ratio.**

    $$
    \frac{PD^{\text{stress}}}{PD^{\text{TTC}}} = \frac{19.47\%}{2.93\%} \approx 6.64
    $$

    The stressed PD is approximately **6.6 times** the baseline PD. This dramatic increase is driven by the combined effect of all three macroeconomic shocks pushing the logit upward by $0.48 + 0.60 + 1.00 = 2.08$ units, moving the probability from the low-PD region to the moderate-PD region of the logistic curve.

    **Decomposition of contributions:**

    - GDP decline: $(-0.08)(-6) = +0.48$ (23% of total logit increase)
    - Unemployment rise: $(0.12)(5) = +0.60$ (29%)
    - House price decline: $(-0.04)(-25) = +1.00$ (48%)

    The house price decline is the single largest driver, contributing nearly half of the total stress impact. This reflects the importance of collateral values for credit risk, particularly for mortgage and CRE portfolios.

---

**Exercise 7.** Explain why PPNR is an important offset to stress losses. Under a severely adverse scenario, a bank's NII declines because the yield curve flattens (compressing net interest margins). If the bank's interest-sensitive assets total \$400B with an average yield of 4.5% and liabilities total \$380B with an average cost of 2.0%, compute baseline NII. Under stress, the asset yield falls to 3.5% and the liability cost falls to 1.8%. Compute stressed NII and the resulting decline. Discuss how a bank's asset-liability structure determines its vulnerability to interest rate scenarios.

??? success "Solution to Exercise 7"

    **Part 1: Why PPNR matters.**

    PPNR (Pre-Provision Net Revenue) represents the bank's ongoing earnings capacity before accounting for loan loss provisions. It is the primary organic defense against credit losses:

    - Over a 9-quarter stress horizon, even severely stressed PPNR can offset a significant portion of credit losses.
    - Banks with strong PPNR can absorb larger losses before capital is impaired.
    - Ignoring PPNR would dramatically overstate the net capital impact of stress.

    For example, if a bank projects \$25B in credit losses but generates \$15B in stressed PPNR, the net capital depletion is only \$10B---a fundamentally different picture than the gross \$25B.

    **Part 2: Compute baseline NII.**

    $$
    \text{NII}_{\text{baseline}} = \text{Asset Income} - \text{Liability Cost}
    $$

    $$
    = 400 \times 4.5\% - 380 \times 2.0\% = 18.0 - 7.6 = \$10.4\text{B}
    $$

    **Step 3: Compute stressed NII.**

    Under stress, asset yield falls to 3.5% and liability cost falls to 1.8%:

    $$
    \text{NII}_{\text{stressed}} = 400 \times 3.5\% - 380 \times 1.8\% = 14.0 - 6.84 = \$7.16\text{B}
    $$

    **Step 4: Compute the decline.**

    $$
    \Delta\text{NII} = 10.4 - 7.16 = \$3.24\text{B}
    $$

    $$
    \text{Percentage decline} = \frac{3.24}{10.4} = 31.2\%
    $$

    The net interest margin compresses from:

    $$
    \text{NIM}_{\text{baseline}} = \frac{10.4}{400} = 2.60\%
    $$

    to:

    $$
    \text{NIM}_{\text{stressed}} = \frac{7.16}{400} = 1.79\%
    $$

    a compression of 81 basis points.

    **Step 5: How asset-liability structure drives vulnerability.**

    The bank's vulnerability to interest rate scenarios depends on several structural factors:

    1. **Duration mismatch:** If assets have longer duration than liabilities (typical for banks that borrow short and lend long), a rate increase reduces asset values more than liability values, causing mark-to-market losses. Conversely, falling rates benefit the bank initially but compress future NII as assets reprice lower.

    2. **Repricing gap:** The speed at which assets and liabilities reprice differs. In the example, asset yields fell by 100 bps (from 4.5% to 3.5%) while liability costs fell by only 20 bps (from 2.0% to 1.8%). This asymmetric repricing compresses margins. Banks with floating-rate assets and fixed-rate deposits (like many US banks) face the opposite risk: rising rates increase deposit competition faster than asset yields adjust.

    3. **Funding structure:** Banks relying on wholesale funding (which reprices quickly and may become unavailable during stress) are more vulnerable than banks funded primarily by stable retail deposits (which reprice slowly and are insensitive to market rates).

    4. **Non-maturity deposits:** The behavioral characteristics of non-maturity deposits (checking accounts, savings accounts) are critical. If depositors are rate-insensitive (as in a low-rate environment), liability costs stay low even as asset yields fall. But if competition for deposits intensifies, the floor on liability cost reduction limits NII improvement.

    5. **Hedging:** Banks that hedge interest rate risk with swaps or other derivatives can partially immunize NII against rate changes, but this comes at the cost of giving up potential upside and adds counterparty risk.
