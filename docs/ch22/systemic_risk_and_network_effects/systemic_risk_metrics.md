# Systemic Risk Metrics

Standard risk measures such as VaR and ES quantify the risk of a single institution in isolation. But the 2007--2009 financial crisis revealed that the failure of interconnected institutions can cascade through the financial system, causing damage far exceeding the sum of individual losses. **Systemic risk metrics** address this gap by measuring how much a given institution contributes to or is exposed to system-wide distress. This section presents the three most widely used metrics---CoVaR, MES, and SRISK---together with the network-based clearing framework that underpins structural approaches.

---

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The formal definition and estimation of CoVaR via quantile regression
    - How Marginal Expected Shortfall captures tail co-movement
    - The SRISK framework for measuring capital shortfall under stress
    - The Eisenberg-Noe clearing model and its role in network-based systemic risk measurement
    - How different metrics complement one another in regulatory practice

---

## From Individual to Systemic Risk

### Why Individual Risk Measures Are Insufficient

Consider a system of $n$ financial institutions. Let $R_i$ denote the return of institution $i$ and $R_{\text{sys}}$ the return of a system aggregate (e.g., a financial sector index). Standard risk management focuses on the marginal distribution of $R_i$, but systemic risk depends on the **joint distribution** $(R_1, \ldots, R_n)$ and especially on its behavior in the tails.

Two institutions may each have acceptable standalone risk, yet their joint failure can be catastrophic. Systemic risk metrics capture this by conditioning on extreme events or aggregating contributions to system-wide losses.

### Taxonomy of Approaches

| Approach | Examples | Data Required |
|----------|----------|---------------|
| **Market-based** | CoVaR, MES, SRISK | Equity prices, CDS spreads |
| **Network-based** | Eisenberg-Noe, DebtRank | Balance sheet exposures |
| **Indicator-based** | G-SIB scores | Size, interconnectedness, complexity |

---

## CoVaR (Adrian-Brunnermeier)

### Definition

The **Conditional Value-at-Risk** of the system given institution $i$ is defined as:

$$
\Pr\!\big(R_{\text{sys}} \leq \text{CoVaR}_\alpha^{\,\text{sys}|i}\,\big|\, R_i = \text{VaR}_\alpha^i\big) = \alpha
$$

In words, $\text{CoVaR}_\alpha^{\,\text{sys}|i}$ is the $\alpha$-quantile of the system return conditional on institution $i$ being at its $\alpha$-VaR level.

### Delta-CoVaR

The **systemic risk contribution** of institution $i$ is measured by comparing CoVaR under stress versus normal conditions:

$$
\Delta\text{CoVaR}_\alpha^i = \text{CoVaR}_\alpha^{\,\text{sys}|R_i = \text{VaR}_\alpha^i} - \text{CoVaR}_\alpha^{\,\text{sys}|R_i = \text{Median}^i}
$$

A large $|\Delta\text{CoVaR}^i|$ indicates that institution $i$'s distress significantly worsens system-wide risk.

### Estimation via Quantile Regression

Adrian and Brunnermeier (2016) estimate CoVaR using quantile regression. Specify:

$$
R_{\text{sys},t} = \beta_0^\alpha + \beta_1^\alpha R_{i,t} + \gamma^\alpha M_t + \varepsilon_t^\alpha
$$

where $M_t$ is a vector of state variables (e.g., VIX, credit spreads, term spread, market return) and the coefficients are estimated at quantile level $\alpha$ (typically 5% or 1%).

The estimated CoVaR is:

$$
\widehat{\text{CoVaR}}_\alpha^{\,\text{sys}|i} = \hat{\beta}_0^\alpha + \hat{\beta}_1^\alpha \cdot \widehat{\text{VaR}}_\alpha^i + \hat{\gamma}^\alpha M_t
$$

!!! note "Time-Varying CoVaR"
    Because the state variables $M_t$ change over time, CoVaR is inherently **time-varying**. This allows it to capture the buildup of systemic risk during credit booms, even before a crisis materializes.

### Properties and Limitations

**Strengths:**

- Uses publicly available market data
- Captures tail dependence between institution and system
- Time-varying via conditioning on state variables

**Limitations:**

- Conditioning on a point ($R_i = \text{VaR}$) is statistically fragile; some implementations use $R_i \leq \text{VaR}$ instead
- Sensitive to choice of state variables and quantile level
- Does not directly measure capital shortfall

---

## Marginal Expected Shortfall (MES)

### Definition

The **Marginal Expected Shortfall** of institution $i$ is the expected return of institution $i$ conditional on the system being in its tail:

$$
\text{MES}_\alpha^i = -\mathbb{E}\!\big[R_i \,\big|\, R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}\big]
$$

The negative sign ensures MES is positive when the institution loses money during systemic stress.

### Connection to System ES

MES has an elegant decomposition property. The system expected shortfall can be written as:

$$
\text{ES}_\alpha^{\text{sys}} = -\mathbb{E}\!\big[R_{\text{sys}} \,\big|\, R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}\big] = \sum_{i=1}^n w_i \cdot \text{MES}_\alpha^i
$$

where $w_i$ is institution $i$'s weight in the system portfolio. This means MES provides an **exact additive decomposition** of systemic risk.

!!! tip "Euler Allocation Interpretation"
    The MES decomposition is precisely the **Euler allocation** of system ES to its components. This follows from the homogeneity property of ES:

    $$
    \text{MES}_\alpha^i = \frac{\partial}{\partial w_i}\text{ES}_\alpha^{\text{sys}}
    $$

    This makes MES the natural marginal contribution of institution $i$ to total system risk.

### Estimation

**Nonparametric estimator:** Given a sample of $T$ return pairs $(R_{i,t}, R_{\text{sys},t})$:

$$
\widehat{\text{MES}}_\alpha^i = -\frac{1}{|\mathcal{T}_\alpha|}\sum_{t \in \mathcal{T}_\alpha} R_{i,t}
$$

where $\mathcal{T}_\alpha = \{t : R_{\text{sys},t} \leq \widehat{\text{VaR}}_\alpha^{\text{sys}}\}$.

**DCC-GARCH estimator** (Brownlees and Engle, 2017): Model the joint dynamics using a bivariate DCC-GARCH:

$$
R_{i,t} = \sigma_{i,t}\,\varepsilon_{i,t}, \quad R_{\text{sys},t} = \sigma_{\text{sys},t}\,\varepsilon_{\text{sys},t}
$$

with time-varying correlation $\rho_t$. Then:

$$
\text{MES}_\alpha^i(t) = \sigma_{i,t}\,\rho_t\,\mathbb{E}\!\left[\varepsilon_{\text{sys}} \,\middle|\, \varepsilon_{\text{sys}} < \frac{\text{VaR}_\alpha}{\sigma_{\text{sys},t}}\right] + \sigma_{i,t}\sqrt{1-\rho_t^2}\,\mathbb{E}\!\left[\varepsilon_i \,\middle|\, \varepsilon_{\text{sys}} < \frac{\text{VaR}_\alpha}{\sigma_{\text{sys},t}}\right]
$$

---

## SRISK (Brownlees-Engle)

### Capital Shortfall Framework

**SRISK** measures the expected capital shortfall of institution $i$ in a systemic crisis. It answers: how much capital would institution $i$ need if the market falls by a specified amount?

$$
\text{SRISK}_i = k \cdot D_i - (1-k) \cdot W_i \cdot (1 - \text{LRMES}_i)
$$

where:

- $k$ = prudential capital ratio (e.g., 8%)
- $D_i$ = book value of debt
- $W_i$ = market value of equity
- $\text{LRMES}_i$ = long-run marginal expected shortfall (equity loss in a crisis)

### Long-Run MES

The LRMES approximates the expected equity decline over a longer horizon (typically 6 months) given a severe market decline (e.g., 40%):

$$
\text{LRMES}_i \approx 1 - \exp(-18 \cdot \text{MES}_i)
$$

This approximation, due to Acharya, Engle, and Richardson (2012), converts the daily MES into a six-month loss estimate using the scaling factor derived from a bivariate GARCH model.

### Interpretation

- **SRISK > 0:** Institution $i$ would have a capital shortfall in a crisis; it is a **net contributor** to systemic risk
- **SRISK < 0:** Institution is well-capitalized even under stress; it is a **net absorber** of risk

The **aggregate SRISK** across all institutions with positive shortfalls measures total system-wide recapitalization needs:

$$
\text{SRISK}_{\text{aggregate}} = \sum_{i:\, \text{SRISK}_i > 0} \text{SRISK}_i
$$

??? example "SRISK Calculation"
    Consider a bank with:

    - Market equity $W = \$50$ billion
    - Book debt $D = \$450$ billion
    - Daily $\text{MES}_{5\%} = 3.5\%$
    - Prudential ratio $k = 8\%$

    Step 1: $\text{LRMES} \approx 1 - \exp(-18 \times 0.035) = 1 - e^{-0.63} \approx 0.467$

    Step 2: Capital shortfall

    $$
    \text{SRISK} = 0.08 \times 450 - 0.92 \times 50 \times (1 - 0.467) = 36 - 24.5 = \$11.5 \text{ billion}
    $$

    This bank would need \$11.5 billion in recapitalization during a severe crisis.

---

## Network Models: Eisenberg-Noe Clearing

### Setup

Consider $n$ financial institutions forming a network. Each institution $i$ has:

- External assets $e_i \geq 0$
- Nominal interbank liabilities $\bar{p}_i$ to other institutions
- A relative liability matrix $\Pi$ where $\Pi_{ij}$ is the fraction of $i$'s liabilities owed to $j$

### Clearing Vector

A **clearing payment vector** $p = (p_1, \ldots, p_n)$ satisfies:

$$
p_i = \min\!\left(\bar{p}_i,\; e_i + \sum_{j=1}^n \Pi_{ji}\, p_j\right)
$$

In matrix form:

$$
p = \min\!\big(\bar{p},\; e + \Pi^\top p\big)
$$

Each institution pays the lesser of its obligations and its available resources (external assets plus incoming payments).

**Theorem (Eisenberg-Noe, 2001).** Under the assumption that $\Pi$ is a substochastic matrix with $\sum_j \Pi_{ij} \leq 1$, there exists a greatest clearing vector $p^*$ that can be computed by the iterative algorithm:

$$
p^{(k+1)} = \min\!\big(\bar{p},\; e + \Pi^\top p^{(k)}\big)
$$

starting from $p^{(0)} = \bar{p}$. The sequence is monotonically decreasing and converges in finitely many steps. $\square$

### Default and Contagion

Institution $i$ **defaults** in the clearing equilibrium if $p_i^* < \bar{p}_i$. The **contagion set** is:

$$
\mathcal{D} = \{i : p_i^* < \bar{p}_i\}
$$

An initial shock that reduces some $e_i$ values can cause defaults that cascade through the network via reduced payments.

### DebtRank

**DebtRank** (Battiston et al., 2012) extends the Eisenberg-Noe framework by tracking the **relative equity loss** propagating through the network. Define $h_i \in [0,1]$ as the distress level of institution $i$:

$$
h_i(t+1) = \min\!\left(1,\; h_i(t) + \sum_{j \in \mathcal{N}(i)} W_{ij}\, h_j(t)\right)
$$

where $W_{ij} = A_{ij}/E_i$ is the exposure of $i$ to $j$ relative to $i$'s equity, and the sum runs over $i$'s neighbors in the network.

---

## Comparison of Systemic Risk Metrics

| Feature | CoVaR | MES | SRISK | Eisenberg-Noe |
|---------|-------|-----|-------|---------------|
| **Data** | Market | Market | Market + balance sheet | Balance sheet |
| **Frequency** | Daily | Daily | Weekly/monthly | Quarterly |
| **Additivity** | No | Yes (Euler) | Yes | N/A |
| **Capital shortfall** | No | Indirectly | Directly | Yes |
| **Network structure** | No | No | No | Yes |
| **Forward-looking** | Partially | Partially | Yes | Scenario-based |

!!! info "Regulatory Applications"
    - **G-SIB designation:** Indicator-based approach, but market-based metrics inform supervisory judgment
    - **Macroprudential stress tests:** SRISK-type frameworks inform system-wide capital adequacy
    - **FSOC (US) / ESRB (EU):** Use combinations of metrics for monitoring financial stability
    - **Systemic risk surcharges:** Calibrated using network and market-based measures

---

## Key Takeaways

- CoVaR measures the system's risk conditional on an institution's distress, estimated via quantile regression
- MES provides an exact Euler decomposition of system ES into institutional contributions
- SRISK combines MES with balance sheet data to estimate dollar capital shortfall under stress
- The Eisenberg-Noe clearing model captures payment cascades through interbank networks
- DebtRank extends network analysis to track the propagation of equity losses
- No single metric captures all dimensions of systemic risk; regulators use multiple approaches in combination

---

## Further Reading

- Adrian, T. & Brunnermeier, M. (2016), "CoVaR," *American Economic Review*, 106(7), 1705--1741
- Acharya, V., Pedersen, L., Philippon, T. & Richardson, M. (2017), "Measuring Systemic Risk," *Review of Financial Studies*, 30(1), 2--47
- Brownlees, C. & Engle, R. (2017), "SRISK: A Conditional Capital Shortfall Measure of Systemic Risk," *Review of Financial Studies*, 30(1), 48--79
- Eisenberg, L. & Noe, T. (2001), "Systemic Risk in Financial Systems," *Management Science*, 47(2), 236--249
- Battiston, S. et al. (2012), "DebtRank: Too Central to Fail?," *Scientific Reports*, 2, 541
- Bisias, D., Flood, M., Lo, A. & Valavanis, S. (2012), "A Survey of Systemic Risk Analytics," *Annual Review of Financial Economics*, 4, 255--296

---

## Exercises

**Exercise 1.** Using the quantile regression specification

$$
R_{\text{sys},t} = \beta_0^\alpha + \beta_1^\alpha R_{i,t} + \gamma^\alpha M_t + \varepsilon_t^\alpha
$$

suppose at the 5% quantile the estimated coefficients are $\hat{\beta}_0 = -0.01$, $\hat{\beta}_1 = 0.8$, and $\hat{\gamma} = -0.3$. The current state variable is $M_t = 0.05$ and institution $i$'s $\text{VaR}_{5\%} = -6\%$. Compute $\text{CoVaR}_{5\%}^{\text{sys}|i}$. If the median return of institution $i$ is $+0.5\%$, compute $\Delta\text{CoVaR}^i$. Interpret the result.

??? success "Solution to Exercise 1"
    We are given the quantile regression specification at the 5% level:

    $$
    R_{\text{sys},t} = \beta_0^\alpha + \beta_1^\alpha R_{i,t} + \gamma^\alpha M_t + \varepsilon_t^\alpha
    $$

    with $\hat{\beta}_0 = -0.01$, $\hat{\beta}_1 = 0.8$, $\hat{\gamma} = -0.3$, $M_t = 0.05$, and $\text{VaR}_{5\%}^i = -0.06$.

    **Step 1: Compute CoVaR under stress.** Substitute $R_{i,t} = \text{VaR}_{5\%}^i = -0.06$:

    $$
    \widehat{\text{CoVaR}}_{5\%}^{\,\text{sys}|i} = \hat{\beta}_0 + \hat{\beta}_1 \cdot \text{VaR}_{5\%}^i + \hat{\gamma} \cdot M_t
    $$

    $$
    = -0.01 + 0.8 \times (-0.06) + (-0.3) \times 0.05
    $$

    $$
    = -0.01 - 0.048 - 0.015 = -0.073
    $$

    So $\text{CoVaR}_{5\%}^{\,\text{sys}|i} = -7.3\%$.

    **Step 2: Compute CoVaR under normal conditions.** Substitute $R_{i,t} = \text{Median}^i = +0.005$:

    $$
    \widehat{\text{CoVaR}}_{5\%}^{\,\text{sys}|\text{median}} = -0.01 + 0.8 \times 0.005 + (-0.3) \times 0.05
    $$

    $$
    = -0.01 + 0.004 - 0.015 = -0.021
    $$

    So $\text{CoVaR}_{5\%}^{\,\text{sys}|\text{median}} = -2.1\%$.

    **Step 3: Compute Delta-CoVaR.**

    $$
    \Delta\text{CoVaR}_{5\%}^i = \text{CoVaR}_{5\%}^{\,\text{sys}|\text{stress}} - \text{CoVaR}_{5\%}^{\,\text{sys}|\text{median}}
    $$

    $$
    = -0.073 - (-0.021) = -0.052
    $$

    **Interpretation:** $\Delta\text{CoVaR}^i = -5.2\%$. When institution $i$ moves from its median state to its 5% VaR stress state, the system's 5% quantile worsens by 5.2 percentage points (from $-2.1\%$ to $-7.3\%$). This indicates that institution $i$ is a significant contributor to systemic risk. The large $|\Delta\text{CoVaR}|$ reflects both the sensitivity of the system to institution $i$ (captured by $\hat{\beta}_1 = 0.8$) and the magnitude of institution $i$'s tail risk ($\text{VaR}_{5\%}^i = -6\%$).

---

**Exercise 2.** Show that MES provides an exact additive decomposition of system ES:

$$
\text{ES}_\alpha^{\text{sys}} = \sum_{i=1}^n w_i \cdot \text{MES}_\alpha^i
$$

Start from the definition $\text{ES}_\alpha^{\text{sys}} = -\mathbb{E}[R_{\text{sys}} | R_{\text{sys}} \le \text{VaR}_\alpha^{\text{sys}}]$ and the fact that $R_{\text{sys}} = \sum_i w_i R_i$. Explain why this Euler allocation property makes MES particularly useful for attributing systemic risk across institutions.

??? success "Solution to Exercise 2"
    **Step 1: Start from the definition of system ES.**

    $$
    \text{ES}_\alpha^{\text{sys}} = -\mathbb{E}\!\big[R_{\text{sys}} \,\big|\, R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}\big]
    $$

    **Step 2: Express the system return as a weighted sum.**

    Since $R_{\text{sys}} = \sum_{i=1}^n w_i R_i$, substitute into the ES definition:

    $$
    \text{ES}_\alpha^{\text{sys}} = -\mathbb{E}\!\left[\sum_{i=1}^n w_i R_i \,\bigg|\, R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}\right]
    $$

    **Step 3: Use linearity of conditional expectation.**

    Conditional expectation is linear, so we can interchange the sum and expectation:

    $$
    \text{ES}_\alpha^{\text{sys}} = -\sum_{i=1}^n w_i \,\mathbb{E}\!\big[R_i \,\big|\, R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}\big]
    $$

    **Step 4: Identify each term as MES.**

    By definition, $\text{MES}_\alpha^i = -\mathbb{E}[R_i \mid R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}]$, so:

    $$
    \text{ES}_\alpha^{\text{sys}} = \sum_{i=1}^n w_i \cdot \text{MES}_\alpha^i
    $$

    This completes the proof. $\square$

    **Why this Euler allocation property makes MES useful:** The decomposition is exact and additive---the individual MES contributions sum precisely to the total system ES, with no residual term. This means MES provides a consistent attribution of systemic risk: each institution's MES measures its marginal contribution to total system risk. This is the same as the Euler allocation principle from risk capital theory:

    $$
    \text{MES}_\alpha^i = \frac{\partial}{\partial w_i}\text{ES}_\alpha^{\text{sys}}
    $$

    Practically, this means:

    - MES allows fair risk allocation: each institution is charged for exactly its contribution
    - Reducing any institution's MES by one unit reduces total system risk by exactly $w_i$ units
    - Unlike CoVaR, which measures conditional quantiles and is not additive, MES enables direct comparison across institutions using a single consistent decomposition
    - Regulators can use MES to design proportional systemic risk surcharges

---

**Exercise 3.** Compute SRISK for two banks:

- Bank A: $W_A = \$30$B, $D_A = \$270$B, daily $\text{MES}_{5\%} = 2.5\%$
- Bank B: $W_B = \$100$B, $D_B = \$400$B, daily $\text{MES}_{5\%} = 1.8\%$

Use $k = 8\%$ and $\text{LRMES} \approx 1 - \exp(-18 \cdot \text{MES})$. Which bank has a higher SRISK? Decompose the result into the debt contribution ($k \cdot D$) and the equity absorption capacity ($(1-k) \cdot W \cdot (1 - \text{LRMES})$). Discuss why a highly leveraged bank with moderate MES can have higher SRISK than a less leveraged bank with higher MES.

??? success "Solution to Exercise 3"
    **Step 1: Compute LRMES for each bank.**

    Using $\text{LRMES} \approx 1 - \exp(-18 \cdot \text{MES})$:

    - Bank A: $\text{LRMES}_A = 1 - \exp(-18 \times 0.025) = 1 - e^{-0.45} = 1 - 0.6376 = 0.3624$
    - Bank B: $\text{LRMES}_B = 1 - \exp(-18 \times 0.018) = 1 - e^{-0.324} = 1 - 0.7234 = 0.2766$

    **Step 2: Compute SRISK for each bank.**

    Using $\text{SRISK}_i = k \cdot D_i - (1-k) \cdot W_i \cdot (1 - \text{LRMES}_i)$:

    - Bank A:

    $$
    \text{SRISK}_A = 0.08 \times 270 - 0.92 \times 30 \times (1 - 0.3624)
    $$

    $$
    = 21.6 - 0.92 \times 30 \times 0.6376 = 21.6 - 17.60 = \$4.00\text{B}
    $$

    - Bank B:

    $$
    \text{SRISK}_B = 0.08 \times 400 - 0.92 \times 100 \times (1 - 0.2766)
    $$

    $$
    = 32.0 - 0.92 \times 100 \times 0.7234 = 32.0 - 66.55 = -\$34.55\text{B}
    $$

    **Step 3: Decomposition.**

    | Component | Bank A | Bank B |
    |-----------|--------|--------|
    | Debt contribution $k \cdot D$ | \$21.6B | \$32.0B |
    | Equity absorption $(1-k) \cdot W \cdot (1-\text{LRMES})$ | \$17.60B | \$66.55B |
    | **SRISK** | **\$4.00B** | **$-$\$34.55B** |

    **Bank A has higher SRISK** (\$4.00B > $-$\$34.55B). Although Bank B has a larger debt contribution (\$32.0B vs. \$21.6B), its much larger equity base (\$100B vs. \$30B) provides ample absorption capacity even after accounting for crisis losses.

    **Discussion:** Bank A is highly leveraged: $D_A/W_A = 270/30 = 9.0$, while Bank B has $D_B/W_B = 400/100 = 4.0$. Despite Bank A having higher MES (2.5% vs. 1.8%), the key driver is leverage. The debt contribution grows linearly with $D$, but the equity absorption capacity grows with $W$. A highly leveraged institution with moderate tail exposure can have higher SRISK than a less leveraged institution with higher tail exposure, because the leveraged institution has less equity to absorb losses relative to its debt obligations. This is why SRISK is often described as primarily a measure of leverage-adjusted systemic risk.

---

**Exercise 4.** In the Eisenberg-Noe framework, a 3-bank system has external assets $e = (100, 50, 30)$, nominal liabilities $\bar{p} = (80, 60, 40)$, and relative liability matrix

$$
\Pi = \begin{pmatrix} 0 & 0.5 & 0.5 \\ 0.6 & 0 & 0.4 \\ 0.4 & 0.6 & 0 \end{pmatrix}
$$

Now suppose an external shock reduces Bank 3's assets from 30 to 10. Compute the new clearing vector by iteration. Does the shock cause any additional defaults beyond Bank 3? What is the total system loss (sum of unpaid liabilities)?

??? success "Solution to Exercise 4"
    We have $n = 3$ banks with $e = (100, 50, 30)$, $\bar{p} = (80, 60, 40)$, and:

    $$
    \Pi = \begin{pmatrix} 0 & 0.5 & 0.5 \\ 0.6 & 0 & 0.4 \\ 0.4 & 0.6 & 0 \end{pmatrix}
    $$

    After the shock, Bank 3's external assets drop from 30 to 10, so $e = (100, 50, 10)$.

    **Iteration 0:** $p^{(0)} = \bar{p} = (80, 60, 40)$.

    Compute $\Pi^\top p^{(0)}$. Note that $(\Pi^\top)_{ji} = \Pi_{ij}$, so column $j$ of $\Pi^\top$ is row $j$ of $\Pi$:

    $$
    \Pi^\top = \begin{pmatrix} 0 & 0.6 & 0.4 \\ 0.5 & 0 & 0.6 \\ 0.5 & 0.4 & 0 \end{pmatrix}
    $$

    $$
    (\Pi^\top p^{(0)})_1 = 0 \times 80 + 0.6 \times 60 + 0.4 \times 40 = 0 + 36 + 16 = 52
    $$

    $$
    (\Pi^\top p^{(0)})_2 = 0.5 \times 80 + 0 \times 60 + 0.6 \times 40 = 40 + 0 + 24 = 64
    $$

    $$
    (\Pi^\top p^{(0)})_3 = 0.5 \times 80 + 0.4 \times 60 + 0 \times 40 = 40 + 24 + 0 = 64
    $$

    Now $e + \Pi^\top p^{(0)} = (100 + 52,\; 50 + 64,\; 10 + 64) = (152, 114, 74)$.

    $$
    p^{(1)} = \min(\bar{p},\; e + \Pi^\top p^{(0)}) = \min\!\big((80, 60, 40),\; (152, 114, 74)\big) = (80, 60, 40)
    $$

    Since $p^{(1)} = p^{(0)} = \bar{p}$, the algorithm has converged in one step.

    **Result:** The clearing vector is $p^* = (80, 60, 40) = \bar{p}$. **No bank defaults.** Even though Bank 3's external assets dropped from 30 to 10, it receives enough interbank payments ($64$) that its total resources ($10 + 64 = 74$) exceed its obligations ($40$). The shock to Bank 3 is absorbed by the network---incoming payments from Banks 1 and 2 are sufficient to cover Bank 3's liabilities.

    **Total system loss:** Since all banks pay their full obligations, the total unpaid liabilities are zero. The loss is confined to Bank 3's reduced equity: Bank 3's equity goes from $30 + 64 - 40 = 54$ to $10 + 64 - 40 = 34$, a loss of 20. But there is no contagion and no default cascade.

    This illustrates how diversified interbank connections can absorb moderate shocks. A larger shock to Bank 3 (e.g., $e_3 = 0$) or simultaneous shocks to multiple banks would be needed to trigger defaults.

---

**Exercise 5.** The DCC-GARCH MES estimator expresses time-varying MES as a function of conditional volatilities and correlation. Explain intuitively why MES increases when (a) the institution's own volatility $\sigma_{i,t}$ increases, (b) the correlation $\rho_t$ between the institution and the system increases, and (c) the system is in a high-volatility regime. During the 2008 crisis, all three factors moved adversely simultaneously. Discuss why this made MES estimates spike and what implications this has for real-time systemic risk monitoring.

??? success "Solution to Exercise 5"
    The DCC-GARCH MES estimator is:

    $$
    \text{MES}_\alpha^i(t) = \sigma_{i,t}\,\rho_t\,\mathbb{E}\!\left[\varepsilon_{\text{sys}} \,\middle|\, \varepsilon_{\text{sys}} < c_t\right] + \sigma_{i,t}\sqrt{1-\rho_t^2}\,\mathbb{E}\!\left[\varepsilon_i \,\middle|\, \varepsilon_{\text{sys}} < c_t\right]
    $$

    where $c_t = \text{VaR}_\alpha / \sigma_{\text{sys},t}$.

    **(a) Increasing institution volatility $\sigma_{i,t}$:**

    Both terms in the MES formula are multiplied by $\sigma_{i,t}$. When an institution becomes more volatile, its returns are more sensitive to both systematic and idiosyncratic shocks. In the conditional tail (when the system is in distress), higher $\sigma_{i,t}$ means institution $i$'s losses are amplified proportionally. Intuitively, a more volatile institution experiences larger swings, and during a systemic downturn those larger swings are predominantly negative, increasing MES.

    **(b) Increasing correlation $\rho_t$:**

    The first term (systematic component) is directly proportional to $\rho_t$, while the second term (idiosyncratic component) is proportional to $\sqrt{1 - \rho_t^2}$. As $\rho_t$ increases, the systematic component dominates: the institution moves more in lockstep with the system. When the system is in its tail, a highly correlated institution is very likely to also be in distress. Higher correlation means less diversification benefit---the institution cannot escape a system-wide crash.

    **(c) High system volatility regime:**

    When $\sigma_{\text{sys},t}$ is high, the threshold $c_t = \text{VaR}_\alpha / \sigma_{\text{sys},t}$ changes. More importantly, in a high-volatility regime, the conditional tail expectations $\mathbb{E}[\varepsilon_{\text{sys}} | \varepsilon_{\text{sys}} < c_t]$ tend to be more negative (the tail of the standardized distribution is deeper when the system is stressed). Furthermore, high system volatility typically coincides with higher $\sigma_{i,t}$ and $\rho_t$ (volatility clustering and correlation breakdown), compounding the effect.

    **2008 crisis dynamics:** During the crisis, all three factors moved adversely simultaneously:

    - Individual bank volatilities spiked as uncertainty about exposures to mortgage-backed securities grew
    - Correlations surged toward 1 as the "flight from risk" made all financial stocks decline together
    - System-wide volatility reached historic highs (VIX exceeded 80)

    This created a **perfect storm** for MES estimates: the multiplicative interaction of $\sigma_{i,t}$, $\rho_t$, and stressed tail expectations caused MES to spike dramatically. The implication for real-time monitoring is that MES is inherently procyclical---it rises sharply during crises precisely when it is most needed but also when sudden jumps make it difficult to use for timely intervention. This suggests that (i) regulators should monitor MES trends during calm periods to identify buildup of vulnerability, and (ii) MES-based capital requirements should incorporate through-the-cycle smoothing to avoid procyclical capital calls during acute stress.

---

**Exercise 6.** A regulator observes the following daily data over 250 trading days for institution $i$ and the financial sector index. On the 12 days when the sector return was below its 5% VaR, institution $i$'s returns were: $-5.2\%$, $-4.8\%$, $-6.1\%$, $-3.9\%$, $-7.2\%$, $-4.5\%$, $-5.8\%$, $-3.2\%$, $-6.5\%$, $-4.1\%$, $-5.5\%$, $-4.0\%$. Compute the nonparametric MES estimate. Compare this to a hypothetical bank $j$ with tail-day returns averaging $-2.5\%$. Which institution poses a greater systemic risk according to MES?

??? success "Solution to Exercise 6"
    **Nonparametric MES computation for institution $i$.**

    The nonparametric estimator is:

    $$
    \widehat{\text{MES}}_\alpha^i = -\frac{1}{|\mathcal{T}_\alpha|}\sum_{t \in \mathcal{T}_\alpha} R_{i,t}
    $$

    The tail days (when $R_{\text{sys}} \leq \text{VaR}_{5\%}^{\text{sys}}$) have $|\mathcal{T}_\alpha| = 12$ observations for institution $i$:

    $$
    R_{i,t} \in \{-5.2\%, -4.8\%, -6.1\%, -3.9\%, -7.2\%, -4.5\%, -5.8\%, -3.2\%, -6.5\%, -4.1\%, -5.5\%, -4.0\%\}
    $$

    Sum of returns:

    $$
    \sum R_{i,t} = -(5.2 + 4.8 + 6.1 + 3.9 + 7.2 + 4.5 + 5.8 + 3.2 + 6.5 + 4.1 + 5.5 + 4.0) = -60.8\%
    $$

    $$
    \widehat{\text{MES}}_{5\%}^i = -\frac{-60.8\%}{12} = \frac{60.8\%}{12} = 5.067\%
    $$

    **Comparison with institution $j$:**

    Institution $j$'s tail-day returns average $-2.5\%$, so:

    $$
    \widehat{\text{MES}}_{5\%}^j = -(-2.5\%) = 2.5\%
    $$

    **Conclusion:** Institution $i$ has $\widehat{\text{MES}}_{5\%}^i = 5.07\%$, which is roughly double institution $j$'s MES of $2.5\%$. According to MES, institution $i$ poses a significantly greater systemic risk because it loses much more on average during systemic stress events. When the financial sector is in its 5% tail, institution $i$'s equity declines by about 5.1% on average, compared to only 2.5% for institution $j$. This means institution $i$ is more exposed to system-wide downturns, likely due to higher leverage, greater correlation with the financial sector, or concentrated exposures to the same risk factors driving systemic stress.

    Note that with only 12 tail observations, the estimate has substantial sampling uncertainty. A 95% confidence interval using $\hat{\sigma}/\sqrt{n}$ would be fairly wide, underscoring the importance of complementing nonparametric MES with model-based (e.g., DCC-GARCH) estimates for more stable inference.

---

**Exercise 7.** Compare the information content of CoVaR, MES, and SRISK for a non-bank financial institution (e.g., a large insurance company) versus a major commercial bank. Discuss which metric might be most informative for each institution type, considering differences in: (a) leverage structure, (b) liquidity of equity, (c) tail risk profile, and (d) interconnectedness with the banking system. Why might network-based models (Eisenberg-Noe) be less applicable to non-bank financials?

??? success "Solution to Exercise 7"
    **CoVaR for insurance companies vs. commercial banks:**

    **(a) Leverage structure:** Commercial banks typically operate at 10--25x leverage, while insurance companies have lower financial leverage but may have significant embedded leverage through derivatives and guarantees. CoVaR captures tail co-movement regardless of leverage structure, making it reasonably informative for both. However, for insurance companies, distress may manifest slowly (claims development) rather than as sudden market movements, potentially making CoVaR less responsive.

    **(b) Liquidity of equity:** CoVaR and MES require liquid equity prices. Large commercial banks have very liquid equity, making these market-based metrics reliable. Some insurance companies (especially mutual or subsidiary structures) may have less liquid equity, reducing the informativeness of market-based metrics. For non-bank financials with illiquid equity, CoVaR estimates may be noisy and unreliable.

    **(c) Tail risk profile:** Insurance companies face catastrophic tail risks (natural disasters, pandemics) that are largely idiosyncratic to the insurance sector. CoVaR may understate the systemic impact of insurance-specific tail events that are poorly correlated with financial sector returns in normal times but become highly correlated during extreme stress (e.g., AIG in 2008). MES may similarly miss these risks if conditioning on the financial sector index doesn't capture insurance-specific systemic events.

    **(d) Interconnectedness with banking:** Commercial banks are directly interconnected through interbank lending, derivatives, and payment systems. Insurance companies are connected primarily through investment portfolios (holding bank bonds) and derivatives (selling CDS protection). This indirect interconnection is better captured by SRISK (which incorporates balance sheet size) than by CoVaR (which only measures statistical co-movement).

    **Most informative metric by institution type:**

    - **Commercial banks:** SRISK is most informative because it directly measures capital shortfall, incorporates leverage (which is the primary amplification mechanism for banks), and combines market data with balance sheet information. The interbank network structure makes Eisenberg-Noe models also highly applicable.
    - **Insurance companies:** MES may be most informative because it captures tail co-movement without requiring detailed balance sheet decomposition. SRISK can be adapted but requires careful treatment of insurance-specific liabilities (technical provisions vs. financial debt). CoVaR is useful but may miss slow-developing insurance risks.

    **Why Eisenberg-Noe is less applicable to non-bank financials:**

    The Eisenberg-Noe framework is designed for networks of bilateral payment obligations (interbank lending). Non-bank financials participate in different network structures:

    - Their obligations are primarily to policyholders (insurance) or fund investors (asset managers), not to other financial institutions
    - Their interconnections with banks are through investment portfolios and derivative contracts, not through the direct lending network that Eisenberg-Noe models
    - The "clearing payment" concept does not naturally apply---insurance claims are contingent, not fixed nominal payments
    - Data on non-bank interconnections is even more opaque than interbank data

    For non-bank financials, fire-sale models (Greenwood-Landier-Thesmar) capturing common asset holdings may be more relevant than credit-contagion network models.
