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

---

**Exercise 2.** Show that MES provides an exact additive decomposition of system ES:

$$
\text{ES}_\alpha^{\text{sys}} = \sum_{i=1}^n w_i \cdot \text{MES}_\alpha^i
$$

Start from the definition $\text{ES}_\alpha^{\text{sys}} = -\mathbb{E}[R_{\text{sys}} | R_{\text{sys}} \le \text{VaR}_\alpha^{\text{sys}}]$ and the fact that $R_{\text{sys}} = \sum_i w_i R_i$. Explain why this Euler allocation property makes MES particularly useful for attributing systemic risk across institutions.

---

**Exercise 3.** Compute SRISK for two banks:

- Bank A: $W_A = \$30$B, $D_A = \$270$B, daily $\text{MES}_{5\%} = 2.5\%$
- Bank B: $W_B = \$100$B, $D_B = \$400$B, daily $\text{MES}_{5\%} = 1.8\%$

Use $k = 8\%$ and $\text{LRMES} \approx 1 - \exp(-18 \cdot \text{MES})$. Which bank has a higher SRISK? Decompose the result into the debt contribution ($k \cdot D$) and the equity absorption capacity ($(1-k) \cdot W \cdot (1 - \text{LRMES})$). Discuss why a highly leveraged bank with moderate MES can have higher SRISK than a less leveraged bank with higher MES.

---

**Exercise 4.** In the Eisenberg-Noe framework, a 3-bank system has external assets $e = (100, 50, 30)$, nominal liabilities $\bar{p} = (80, 60, 40)$, and relative liability matrix

$$
\Pi = \begin{pmatrix} 0 & 0.5 & 0.5 \\ 0.6 & 0 & 0.4 \\ 0.4 & 0.6 & 0 \end{pmatrix}
$$

Now suppose an external shock reduces Bank 3's assets from 30 to 10. Compute the new clearing vector by iteration. Does the shock cause any additional defaults beyond Bank 3? What is the total system loss (sum of unpaid liabilities)?

---

**Exercise 5.** The DCC-GARCH MES estimator expresses time-varying MES as a function of conditional volatilities and correlation. Explain intuitively why MES increases when (a) the institution's own volatility $\sigma_{i,t}$ increases, (b) the correlation $\rho_t$ between the institution and the system increases, and (c) the system is in a high-volatility regime. During the 2008 crisis, all three factors moved adversely simultaneously. Discuss why this made MES estimates spike and what implications this has for real-time systemic risk monitoring.

---

**Exercise 6.** A regulator observes the following daily data over 250 trading days for institution $i$ and the financial sector index. On the 12 days when the sector return was below its 5% VaR, institution $i$'s returns were: $-5.2\%$, $-4.8\%$, $-6.1\%$, $-3.9\%$, $-7.2\%$, $-4.5\%$, $-5.8\%$, $-3.2\%$, $-6.5\%$, $-4.1\%$, $-5.5\%$, $-4.0\%$. Compute the nonparametric MES estimate. Compare this to a hypothetical bank $j$ with tail-day returns averaging $-2.5\%$. Which institution poses a greater systemic risk according to MES?

---

**Exercise 7.** Compare the information content of CoVaR, MES, and SRISK for a non-bank financial institution (e.g., a large insurance company) versus a major commercial bank. Discuss which metric might be most informative for each institution type, considering differences in: (a) leverage structure, (b) liquidity of equity, (c) tail risk profile, and (d) interconnectedness with the banking system. Why might network-based models (Eisenberg-Noe) be less applicable to non-bank financials?
