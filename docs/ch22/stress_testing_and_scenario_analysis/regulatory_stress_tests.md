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

---

**Exercise 2.** Consider the credit loss model under stress:

$$
PD_t^{\text{stress}} = \Phi\left(\frac{\Phi^{-1}(\overline{PD}) + \sqrt{\rho} \cdot z_t}{\sqrt{1 - \rho}}\right)
$$

For a portfolio with $\overline{PD} = 1.5\%$ and asset correlation $\rho = 0.15$, compute $PD^{\text{stress}}$ when the systematic factor takes the value $z = -2.5$ (representing a severely adverse macroeconomic shock). Compare this to the through-the-cycle PD and discuss the sensitivity of the stressed PD to the correlation parameter.

---

**Exercise 3.** Explain the difference between the static balance sheet assumption (EBA) and the planned capital actions approach (CCAR). A bank with a current CET1 ratio of 12% plans to pay \$3 billion in dividends and repurchase \$2 billion in shares over the stress horizon. Under the EBA static approach, these actions are excluded. Under CCAR, they are included. If the bank's stressed capital decline before capital actions is 4 percentage points, compute the minimum CET1 ratio under each framework. Discuss which framework is more conservative from a capital adequacy perspective.

---

**Exercise 4.** The marginal impact of a macroeconomic variable on the capital ratio is

$$
\frac{\partial \text{CET1 Ratio}_t}{\partial z_{j,t}} = \frac{1}{W_t}\left(\frac{\partial R_t}{\partial z_{j,t}} - \frac{\partial L_t}{\partial z_{j,t}}\right) - \frac{K_t}{W_t^2} \frac{\partial W_t}{\partial z_{j,t}}
$$

Explain each of the three terms on the right-hand side. For a bank where GDP growth affects both credit losses ($\partial L / \partial z_{\text{GDP}} < 0$, since lower GDP increases losses) and RWA ($\partial W / \partial z_{\text{GDP}} < 0$, since lower GDP increases risk weights), discuss why the total impact on the CET1 ratio may be larger than the loss effect alone.

---

**Exercise 5.** Discuss the procyclicality concern in regulatory stress testing. During a recession, stress test models calibrated to worsening data may project larger losses, leading to higher capital requirements at precisely the time when banks can least afford to raise capital. Describe three specific mitigants (mathematical or regulatory) that address this procyclicality. What is the role of the countercyclical capital buffer in this context?

---

**Exercise 6.** A bank uses the logistic regression model

$$
\log\left(\frac{PD_t}{1 - PD_t}\right) = \beta_0 + \beta_1 \Delta\text{GDP}_t + \beta_2 \Delta U_t + \beta_3 \Delta\text{HPI}_t
$$

with estimated parameters $\beta_0 = -3.5$, $\beta_1 = -0.08$, $\beta_2 = 0.12$, $\beta_3 = -0.04$. Under the severely adverse scenario, $\Delta\text{GDP} = -6\%$, $\Delta U = +5\%$, and $\Delta\text{HPI} = -25\%$. Compute the stressed PD. If the through-the-cycle PD (setting all macro shocks to zero) is $\Phi(\text{logit}^{-1}(\beta_0))$, compute the ratio of stressed PD to baseline PD.

---

**Exercise 7.** Explain why PPNR is an important offset to stress losses. Under a severely adverse scenario, a bank's NII declines because the yield curve flattens (compressing net interest margins). If the bank's interest-sensitive assets total \$400B with an average yield of 4.5% and liabilities total \$380B with an average cost of 2.0%, compute baseline NII. Under stress, the asset yield falls to 3.5% and the liability cost falls to 1.8%. Compute stressed NII and the resulting decline. Discuss how a bank's asset-liability structure determines its vulnerability to interest rate scenarios.
