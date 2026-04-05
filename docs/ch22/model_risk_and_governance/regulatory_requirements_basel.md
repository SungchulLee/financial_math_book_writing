# Regulatory Requirements (Basel)

Banking regulation exists because individual institutions, acting rationally in their own interest, can collectively create fragility that threatens the entire financial system. The Basel framework addresses this by requiring banks to hold capital proportional to the risks they take, thereby aligning private incentives with systemic stability. This section presents the mathematical foundations of the Basel II/III/IV capital requirements, the Fundamental Review of the Trading Book (FRTB), and the model validation standards that govern internal risk models.

---

## Basel Framework Evolution

### From Basel I to Basel IV

The Basel Committee on Banking Supervision (BCBS) has progressively refined capital regulation:

- **Basel I (1988):** Simple risk-weighted assets with flat weights (e.g., 0% for sovereigns, 100% for corporates)
- **Basel II (2004):** Internal Ratings-Based (IRB) approach; three-pillar structure
- **Basel III (2010):** Higher capital ratios, liquidity requirements, leverage ratio
- **Basel IV (2017):** Output floor, revised standardized approaches, FRTB

### Three-Pillar Structure

| Pillar | Content | Mathematical Focus |
|--------|---------|-------------------|
| **Pillar 1** | Minimum capital requirements | Risk-weighted asset formulas |
| **Pillar 2** | Supervisory review | Stress testing, ICAAP |
| **Pillar 3** | Market discipline | Disclosure requirements |

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The IRB capital formula and its derivation from the Vasicek single-factor model
    - How FRTB replaces VaR with expected shortfall for market risk capital
    - The mathematical structure of the standardized and internal models approaches
    - Model validation requirements under SR 11-7 and their quantitative implications

---

## Capital Adequacy Ratios

### Regulatory Capital

Banks must maintain capital above prescribed minimums:

$$
\text{Capital Ratio} = \frac{\text{Regulatory Capital}}{\text{Risk-Weighted Assets (RWA)}}
$$

Under Basel III, the minimum requirements are:

$$
\frac{\text{CET1}}{\text{RWA}} \geq 4.5\%, \quad \frac{\text{Tier 1}}{\text{RWA}} \geq 6\%, \quad \frac{\text{Total Capital}}{\text{RWA}} \geq 8\%
$$

where CET1 denotes Common Equity Tier 1 capital.

### Capital Buffers

Basel III introduced additional buffers above the minimums:

- **Capital conservation buffer:** 2.5% CET1
- **Countercyclical buffer:** 0--2.5% CET1 (varies by jurisdiction)
- **G-SIB surcharge:** 1--3.5% CET1 (based on systemic importance score)

The total CET1 requirement for a large G-SIB can therefore reach:

$$
4.5\% + 2.5\% + 2.5\% + 3.5\% = 13\%
$$

---

## Credit Risk: The IRB Approach

### Vasicek Single-Factor Model

The IRB capital formula is derived from the **Vasicek (1987) asymptotic single-factor model**. Consider a portfolio of $n$ obligors, where the asset return of obligor $i$ follows:

$$
A_i = \sqrt{\rho}\, Z + \sqrt{1 - \rho}\, \varepsilon_i
$$

where $Z \sim N(0,1)$ is the systematic factor, $\varepsilon_i \sim N(0,1)$ are independent idiosyncratic factors, and $\rho \in (0,1)$ is the asset correlation.

Obligor $i$ defaults when $A_i < \Phi^{-1}(\text{PD}_i)$, where $\text{PD}_i$ is the probability of default and $\Phi$ is the standard normal CDF.

### Conditional Default Probability

Conditional on the systematic factor $Z = z$, the default probability is:

$$
p(z) = \Phi\!\left(\frac{\Phi^{-1}(\text{PD}) - \sqrt{\rho}\, z}{\sqrt{1-\rho}}\right)
$$

By the law of large numbers, as $n \to \infty$, the portfolio loss fraction converges to this conditional default probability (the **Vasicek limit**).

### IRB Capital Formula

The regulatory capital for credit risk is based on the 99.9% quantile of the loss distribution. Setting $z = \Phi^{-1}(0.999)$, the capital charge per unit of exposure at default (EAD) is:

$$
K = \text{LGD} \cdot \Phi\!\left(\frac{\Phi^{-1}(\text{PD}) + \sqrt{\rho}\,\Phi^{-1}(0.999)}{\sqrt{1-\rho}}\right) - \text{LGD} \cdot \text{PD}
$$

where:

- $\text{PD}$ = probability of default (1-year horizon)
- $\text{LGD}$ = loss given default
- $\rho$ = asset correlation (prescribed by regulation)

The first term is the 99.9th percentile loss; subtracting $\text{LGD} \cdot \text{PD}$ removes the expected loss (covered by provisions).

!!! note "Asset Correlation Function"
    For corporate exposures, Basel prescribes:

    $$
    \rho = 0.12 \cdot \frac{1 - e^{-50 \cdot \text{PD}}}{1 - e^{-50}} + 0.24 \cdot \left(1 - \frac{1 - e^{-50 \cdot \text{PD}}}{1 - e^{-50}}\right)
    $$

    This assigns higher correlation ($\rho \to 0.24$) to low-PD obligors and lower correlation ($\rho \to 0.12$) to high-PD obligors, reflecting the empirical observation that defaults among investment-grade firms are more correlated.

### Risk-Weighted Assets

The risk-weighted assets for a single exposure are:

$$
\text{RWA} = K \cdot 12.5 \cdot \text{EAD} \cdot \text{MA}
$$

where $\text{MA}$ is the maturity adjustment:

$$
\text{MA} = \frac{1 + (M - 2.5) \cdot b(\text{PD})}{1 - 1.5 \cdot b(\text{PD})}
$$

with $b(\text{PD}) = (0.11852 - 0.05478 \cdot \ln(\text{PD}))^2$ and $M$ the effective maturity.

??? example "Numerical Example: IRB Capital Calculation"
    Consider a corporate loan with:

    - $\text{PD} = 1\%$, $\text{LGD} = 45\%$, $\text{EAD} = \$100$ million, $M = 3$ years

    Step 1: Asset correlation

    $$
    \rho = 0.12 \cdot \frac{1 - e^{-0.5}}{1 - e^{-50}} + 0.24 \cdot \left(1 - \frac{1 - e^{-0.5}}{1 - e^{-50}}\right) \approx 0.2038
    $$

    Step 2: Capital charge

    $$
    K = 0.45 \cdot \Phi\!\left(\frac{\Phi^{-1}(0.01) + \sqrt{0.2038} \cdot \Phi^{-1}(0.999)}{\sqrt{1 - 0.2038}}\right) - 0.45 \cdot 0.01 \approx 0.0856
    $$

    Step 3: RWA = $0.0856 \times 12.5 \times 100 \approx \$107$ million

---

## Market Risk: The Fundamental Review of the Trading Book

### From VaR to Expected Shortfall

A key innovation of FRTB is replacing Value-at-Risk with **Expected Shortfall** as the primary market risk measure. The motivation is that ES, unlike VaR, is a coherent risk measure satisfying subadditivity:

$$
\text{ES}_\alpha(X + Y) \leq \text{ES}_\alpha(X) + \text{ES}_\alpha(Y)
$$

Under FRTB, the confidence level shifts from 99% VaR to 97.5% ES, which for normal distributions yields approximately the same capital level:

$$
\text{ES}_{97.5\%}^{\text{Normal}} \approx \text{VaR}_{99\%}^{\text{Normal}}
$$

### Internal Models Approach (IMA)

Banks approved for IMA compute ES across multiple risk factor classes. The aggregate capital charge is:

$$
\text{IMCC} = \rho \cdot \text{ES}_{\text{FC}} + (1 - \rho) \cdot \sum_{i=1}^{5} \text{ES}_{\text{RC},i}
$$

where:

- $\text{ES}_{\text{FC}}$ = ES with full correlations across all risk classes
- $\text{ES}_{\text{RC},i}$ = ES for risk class $i$ in isolation
- $\rho = 0.5$ (regulatory correlation parameter)

The five risk classes are: interest rate, equity, foreign exchange, commodity, and credit spread.

### Liquidity Horizons

FRTB introduces **variable liquidity horizons** rather than a uniform 10-day holding period. The ES is computed as:

$$
\text{ES} = \sqrt{\sum_{j=1}^{J} \left(\text{ES}_j(P_j)\right)^2}
$$

where $\text{ES}_j(P_j)$ is the expected shortfall at liquidity horizon $P_j$ for the $j$-th set of risk factors, and the horizons $P_j \in \{10, 20, 40, 60, 120\}$ trading days.

### Standardized Approach (SA)

For banks not approved for IMA, the **Sensitivities-Based Method** computes capital from first-order risk sensitivities:

$$
K_{\text{SA}} = \sqrt{\sum_{k} \sum_{l} \gamma_{kl}\, K_k\, K_l}
$$

where $K_k$ is the capital charge for risk bucket $k$ and $\gamma_{kl}$ are prescribed inter-bucket correlations.

Within each bucket, the capital aggregates delta, vega, and curvature risks:

$$
K_k = K_k^{\text{delta}} + K_k^{\text{vega}} + K_k^{\text{curvature}}
$$

!!! warning "Trading Book Boundary"
    FRTB introduces a stricter boundary between the trading book and banking book. Instruments must meet specific criteria for trading book designation, and internal transfers between books require regulatory approval. This boundary matters because market risk capital (trading book) and credit risk capital (banking book) use fundamentally different methodologies.

---

## Operational Risk

### Basel III Standardized Measurement Approach (SMA)

Basel III replaces the Advanced Measurement Approach (AMA) with the **Standardized Measurement Approach**. The capital charge combines a volume indicator with a loss history multiplier:

$$
\text{ORC} = \text{BIC} \cdot \text{ILM}
$$

where:

- $\text{BIC}$ (Business Indicator Component) is a function of the **Business Indicator** (BI), computed from financial statement items (interest income, fee income, trading income)
- $\text{ILM}$ (Internal Loss Multiplier) adjusts for the bank's historical operational losses

The Business Indicator Component uses a piecewise-linear marginal coefficient:

$$
\text{BIC} = \begin{cases}
0.12 \cdot \text{BI} & \text{if BI} \leq \text{\euro 1 billion} \\
0.12 \cdot 1 + 0.15 \cdot (\text{BI} - 1) & \text{if } 1 < \text{BI} \leq 30 \\
0.12 \cdot 1 + 0.15 \cdot 29 + 0.18 \cdot (\text{BI} - 30) & \text{if BI} > 30
\end{cases}
$$

---

## Output Floor

### Constraining Internal Models

Basel IV introduces an **output floor** to limit the benefit banks derive from internal models:

$$
\text{RWA}_{\text{floor}} = \max\!\big(\text{RWA}_{\text{internal}},\; 72.5\% \times \text{RWA}_{\text{standardized}}\big)
$$

This ensures that internally modeled RWA cannot fall below 72.5% of the standardized approach RWA, addressing the concern that internal models may systematically understate risk.

---

## Model Validation Standards (SR 11-7)

### Regulatory Definition of Model Risk

The Federal Reserve's SR 11-7 guidance defines model risk as:

> "The potential for adverse consequences from decisions based on incorrect or misused model outputs and reports."

This encompasses three sources:

1. **Fundamental errors** in the model specification
2. **Implementation errors** in coding or systems
3. **Inappropriate use** of a model beyond its intended scope

### Quantitative Validation Requirements

!!! info "Core Validation Components"
    Effective validation under SR 11-7 requires:

    - **Conceptual soundness assessment:** Evaluate whether model theory and assumptions are appropriate
    - **Outcomes analysis:** Compare model predictions to realized outcomes (backtesting)
    - **Ongoing monitoring:** Track model performance, stability, and limitations over time

#### Backtesting Framework

For VaR models, the standard backtest checks whether the observed exceedance rate $\hat{p}$ is consistent with the theoretical rate $(1 - \alpha)$. Using the Kupiec likelihood ratio test:

$$
LR_{\text{uc}} = -2\ln\!\left[\frac{(1-\alpha)^{n_0}\,\alpha^{n_1}}{\hat{p}^{\,n_1}(1-\hat{p})^{n_0}}\right] \;\sim\; \chi^2(1)
$$

where $n_1$ is the number of exceedances and $n_0 = n - n_1$.

#### Benchmarking Requirements

Models must be compared against independent benchmarks:

- Alternative model implementations
- Industry-standard models
- Vendor models
- Simple analytical approximations

The benchmark comparison should be quantified:

$$
\text{Model Difference} = \frac{|V_{\text{model}} - V_{\text{benchmark}}|}{V_{\text{benchmark}}} \times 100\%
$$

with materiality thresholds set by the institution's model risk policy.

### Model Risk Governance

SR 11-7 requires a governance framework with:

- **Model inventory:** Comprehensive register of all models
- **Model tiering:** Classification by risk (Tier 1 = highest impact)
- **Validation frequency:** Annual minimum; more frequent for high-tier models
- **Challenge function:** Independent review authority with power to restrict model use

---

## Leverage Ratio and Liquidity Requirements

### Leverage Ratio

A non-risk-based backstop:

$$
\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Exposure Measure}} \geq 3\%
$$

The exposure measure includes on-balance-sheet assets, derivatives (using SA-CCR), securities financing transactions, and off-balance-sheet items.

### Liquidity Coverage Ratio (LCR)

Banks must hold sufficient high-quality liquid assets (HQLA) to survive a 30-day stress:

$$
\text{LCR} = \frac{\text{HQLA}}{\text{Net Cash Outflows over 30 days}} \geq 100\%
$$

### Net Stable Funding Ratio (NSFR)

Longer-term structural funding requirement:

$$
\text{NSFR} = \frac{\text{Available Stable Funding}}{\text{Required Stable Funding}} \geq 100\%
$$

---

## Connections to Other Topics

The Basel framework connects deeply to other topics in this book:

- **Risk measures (Ch22):** ES and VaR provide the mathematical foundations for Pillar 1 capital
- **Model validation:** Backtesting techniques from the previous section are directly applied under SR 11-7
- **Systemic risk:** G-SIB surcharges and macroprudential buffers link to the systemic risk metrics discussed in this chapter
- **Robust risk frameworks:** The output floor and multiple approaches reflect model uncertainty considerations

---

## Key Takeaways

- The IRB formula derives from the Vasicek single-factor model, using the 99.9th percentile of the asymptotic loss distribution
- FRTB replaces VaR with expected shortfall, introduces variable liquidity horizons, and tightens the trading book boundary
- The output floor at 72.5% of standardized RWA constrains internal model benefits
- SR 11-7 establishes quantitative standards for model validation: backtesting, benchmarking, and ongoing monitoring
- Capital buffers (conservation, countercyclical, G-SIB) add layers above minimum requirements

---

## Further Reading

- Basel Committee on Banking Supervision (2006), "International Convergence of Capital Measurement and Capital Standards (Basel II)"
- Basel Committee on Banking Supervision (2019), "Minimum Capital Requirements for Market Risk (FRTB)"
- Basel Committee on Banking Supervision (2017), "Basel III: Finalising Post-Crisis Reforms (Basel IV)"
- Board of Governors of the Federal Reserve System (2011), "Supervisory Guidance on Model Risk Management (SR 11-7)"
- Vasicek, O. (2002), "The Distribution of Loan Portfolio Value"
- McNeil, A., Frey, R. & Embrechts, P. (2015), *Quantitative Risk Management: Concepts, Techniques and Tools*, 2nd ed., Princeton University Press

---

## Exercises

**Exercise 1.** A corporate loan has $\text{PD} = 2\%$, $\text{LGD} = 40\%$, $\text{EAD} = \$50$ million, and effective maturity $M = 4$ years. Using the Basel IRB asset correlation formula

$$
\rho = 0.12 \cdot \frac{1 - e^{-50 \cdot \text{PD}}}{1 - e^{-50}} + 0.24 \cdot \left(1 - \frac{1 - e^{-50 \cdot \text{PD}}}{1 - e^{-50}}\right)
$$

compute the asset correlation $\rho$, the capital charge $K$, the maturity adjustment $\text{MA}$, and the resulting risk-weighted assets.

??? success "Solution to Exercise 1"
    **IRB capital calculation for a corporate loan.**

    **Given:** $\text{PD} = 2\% = 0.02$, $\text{LGD} = 40\% = 0.40$, $\text{EAD} = \$50$ million, $M = 4$ years.

    **Step 1: Asset correlation $\rho$.**

    $$
    \rho = 0.12 \cdot \frac{1 - e^{-50 \cdot 0.02}}{1 - e^{-50}} + 0.24 \cdot \left(1 - \frac{1 - e^{-50 \cdot 0.02}}{1 - e^{-50}}\right)
    $$

    Since $e^{-50} \approx 0$ (effectively zero), we have $1 - e^{-50} \approx 1$. Therefore:

    $$
    \frac{1 - e^{-1.0}}{1 - e^{-50}} \approx 1 - e^{-1} = 1 - 0.36788 = 0.63212
    $$

    $$
    \rho = 0.12 \times 0.63212 + 0.24 \times (1 - 0.63212)
    $$

    $$
    = 0.12 \times 0.63212 + 0.24 \times 0.36788
    $$

    $$
    = 0.07585 + 0.08829 = 0.1641
    $$

    **Step 2: Capital charge $K$.**

    We need $\Phi^{-1}(\text{PD}) = \Phi^{-1}(0.02) \approx -2.0537$ and $\Phi^{-1}(0.999) \approx 3.0902$.

    $$
    K = \text{LGD} \cdot \Phi\!\left(\frac{\Phi^{-1}(\text{PD}) + \sqrt{\rho}\,\Phi^{-1}(0.999)}{\sqrt{1-\rho}}\right) - \text{LGD} \cdot \text{PD}
    $$

    Computing the argument of $\Phi$:

    $$
    \sqrt{\rho} = \sqrt{0.1641} = 0.4051
    $$

    $$
    \sqrt{1 - \rho} = \sqrt{0.8359} = 0.9143
    $$

    $$
    \frac{-2.0537 + 0.4051 \times 3.0902}{0.9143} = \frac{-2.0537 + 1.2518}{0.9143} = \frac{-0.8019}{0.9143} = -0.8771
    $$

    $$
    \Phi(-0.8771) \approx 0.1902
    $$

    $$
    K = 0.40 \times 0.1902 - 0.40 \times 0.02 = 0.07608 - 0.008 = 0.06808
    $$

    **Step 3: Maturity adjustment $\text{MA}$.**

    First compute $b(\text{PD})$:

    $$
    b(\text{PD}) = (0.11852 - 0.05478 \cdot \ln(0.02))^2
    $$

    $$
    \ln(0.02) = -3.9120
    $$

    $$
    b = (0.11852 - 0.05478 \times (-3.9120))^2 = (0.11852 + 0.21434)^2 = (0.33286)^2 = 0.11080
    $$

    The maturity adjustment with $M = 4$:

    $$
    \text{MA} = \frac{1 + (M - 2.5) \cdot b}{1 - 1.5 \cdot b} = \frac{1 + 1.5 \times 0.11080}{1 - 1.5 \times 0.11080} = \frac{1 + 0.16620}{1 - 0.16620} = \frac{1.16620}{0.83380} = 1.3987
    $$

    **Step 4: Risk-weighted assets.**

    $$
    \text{RWA} = K \times 12.5 \times \text{EAD} \times \text{MA}
    $$

    $$
    = 0.06808 \times 12.5 \times 50 \times 1.3987
    $$

    $$
    = 0.06808 \times 12.5 \times 69.935
    $$

    $$
    = 0.8510 \times 69.935 \approx \$59.5 \text{ million}
    $$

    **Summary:**

    | Parameter | Value |
    |-----------|-------|
    | Asset correlation $\rho$ | 0.1641 |
    | Capital charge $K$ | 6.81% |
    | Maturity adjustment MA | 1.399 |
    | RWA | ~\$59.5 million |

---

**Exercise 2.** In the Vasicek single-factor model, the conditional default probability given the systematic factor $Z = z$ is

$$
p(z) = \Phi\!\left(\frac{\Phi^{-1}(\text{PD}) - \sqrt{\rho}\, z}{\sqrt{1-\rho}}\right)
$$

Show that $p(z)$ is decreasing in $z$ and increasing in $\rho$ (for fixed $z < 0$). Explain the economic intuition: why does higher asset correlation lead to a fatter tail in the portfolio loss distribution?

??? success "Solution to Exercise 2"
    **Monotonicity properties of the conditional default probability.**

    **Part 1: $p(z)$ is decreasing in $z$.**

    $$
    p(z) = \Phi\!\left(\frac{\Phi^{-1}(\text{PD}) - \sqrt{\rho}\, z}{\sqrt{1-\rho}}\right)
    $$

    Since $\Phi$ is a monotonically increasing function, $p(z)$ is decreasing in $z$ if and only if the argument of $\Phi$ is decreasing in $z$. Taking the derivative of the argument with respect to $z$:

    $$
    \frac{\partial}{\partial z}\left(\frac{\Phi^{-1}(\text{PD}) - \sqrt{\rho}\, z}{\sqrt{1-\rho}}\right) = \frac{-\sqrt{\rho}}{\sqrt{1-\rho}} < 0
    $$

    since $\rho \in (0,1)$. Therefore the argument is strictly decreasing in $z$, and since $\Phi$ is strictly increasing, $p(z)$ is strictly decreasing in $z$. $\blacksquare$

    **Interpretation:** When $z$ is large (favorable systematic environment), fewer obligors default. When $z$ is small or negative (adverse systematic shock), more obligors default.

    **Part 2: $p(z)$ is increasing in $\rho$ for fixed $z < 0$.**

    Define $g(\rho) = \frac{\Phi^{-1}(\text{PD}) - \sqrt{\rho}\, z}{\sqrt{1-\rho}}$ and compute $\frac{\partial g}{\partial \rho}$.

    Let $d = \Phi^{-1}(\text{PD}) < 0$ (since $\text{PD} < 0.5$). Then:

    $$
    g(\rho) = \frac{d - \sqrt{\rho}\, z}{\sqrt{1-\rho}}
    $$

    Using the quotient rule:

    $$
    \frac{\partial g}{\partial \rho} = \frac{\left(-\frac{z}{2\sqrt{\rho}}\right)\sqrt{1-\rho} - (d - \sqrt{\rho}\,z)\left(-\frac{1}{2\sqrt{1-\rho}}\right)}{1-\rho}
    $$

    $$
    = \frac{-\frac{z}{2\sqrt{\rho}}\sqrt{1-\rho} + \frac{d - \sqrt{\rho}\,z}{2\sqrt{1-\rho}}}{1-\rho}
    $$

    $$
    = \frac{1}{2(1-\rho)}\left[-\frac{z\sqrt{1-\rho}}{\sqrt{\rho}} + \frac{d - \sqrt{\rho}\,z}{\sqrt{1-\rho}}\right]
    $$

    $$
    = \frac{1}{2(1-\rho)}\left[\frac{-z(1-\rho) + \sqrt{\rho}(d - \sqrt{\rho}\,z)}{\sqrt{\rho}\sqrt{1-\rho}}\right]
    $$

    $$
    = \frac{1}{2(1-\rho)^{3/2}\sqrt{\rho}}\left[-z + z\rho + d\sqrt{\rho} - \rho z\right]
    $$

    $$
    = \frac{1}{2(1-\rho)^{3/2}\sqrt{\rho}}\left[-z + d\sqrt{\rho}\right]
    $$

    $$
    = \frac{d\sqrt{\rho} - z}{2(1-\rho)^{3/2}\sqrt{\rho}}
    $$

    When $z < 0$, we have $-z > 0$, and since $d = \Phi^{-1}(\text{PD}) < 0$, we get $d\sqrt{\rho} < 0$. Thus the numerator is $d\sqrt{\rho} - z$, where $-z > 0$ and $d\sqrt{\rho} < 0$... actually we need to be more careful. We have $d\sqrt{\rho} - z$. Since $z < 0$, we have $-z > 0$, so $d\sqrt{\rho} - z = d\sqrt{\rho} + |z| > 0$ when $|z|$ is sufficiently large. In the regime of interest (stressed conditions where $z < 0$ and $|z|$ is large, i.e., the tail that matters for capital), the numerator is positive, so $\frac{\partial g}{\partial \rho} > 0$, meaning $p(z)$ is increasing in $\rho$.

    More precisely, $\frac{\partial g}{\partial \rho} > 0$ whenever $z < d\sqrt{\rho}$. Since $d < 0$ and $z < 0$, this holds when $|z| > |d|\sqrt{\rho}$, which is the adverse tail relevant for capital ($z = \Phi^{-1}(0.001) \approx -3.09$, while $|d\sqrt{\rho}|$ is typically much smaller). $\blacksquare$

    **Economic intuition:** Higher asset correlation $\rho$ means obligors are more exposed to the common systematic factor $Z$. When $Z$ takes an adverse value ($z < 0$), high correlation causes defaults to be more synchronized -- many firms default together. This creates a **fatter right tail** in the portfolio loss distribution: losses are typically small (in good times, few defaults), but when losses occur, they are catastrophic (in bad times, many defaults simultaneously).

    In the Vasicek limit, the portfolio loss fraction equals $p(Z)$, which is a nonlinear function of the Gaussian systematic factor $Z$. Higher $\rho$ makes this function steeper -- small changes in $Z$ cause large changes in the default rate -- amplifying the tail of the loss distribution and increasing the 99.9th percentile capital requirement.

---

**Exercise 3.** Under Basel III, a G-SIB has a CET1 ratio of 11.5%, with a countercyclical buffer set at 1.5% and a G-SIB surcharge of 2.0%. Determine whether this bank meets all capital requirements including the capital conservation buffer. If the bank's RWA is \$800 billion, compute the CET1 shortfall (if any) in dollar terms.

??? success "Solution to Exercise 3"
    **Capital adequacy assessment for a G-SIB.**

    **Total CET1 requirement:**

    | Component | Requirement |
    |-----------|------------|
    | Minimum CET1 | 4.5% |
    | Capital conservation buffer | 2.5% |
    | Countercyclical buffer | 1.5% |
    | G-SIB surcharge | 2.0% |
    | **Total** | **10.5%** |

    **Assessment:**

    The bank has a CET1 ratio of 11.5%, which exceeds the total requirement of 10.5%. Therefore, the bank **meets all capital requirements** including all buffers.

    The surplus is $11.5\% - 10.5\% = 1.0\%$.

    **Dollar terms:**

    With RWA of \$800 billion:

    - Required CET1 capital: $10.5\% \times \$800\text{B} = \$84$ billion
    - Actual CET1 capital: $11.5\% \times \$800\text{B} = \$92$ billion
    - Surplus: $\$92\text{B} - \$84\text{B} = \$8$ billion

    There is **no shortfall**; the bank has an \$8 billion CET1 surplus above all requirements.

    Note that if the bank's CET1 ratio were to fall into the buffer zone (between 4.5% and 10.5%), the bank would face **restrictions on distributions** (dividends, share buybacks, bonus payments) but would not technically violate minimum capital requirements. The hard minimum is 4.5%, while the buffers impose graduated distribution constraints.

---

**Exercise 4.** Explain why FRTB replaces the uniform 10-day VaR horizon with variable liquidity horizons $P_j \in \{10, 20, 40, 60, 120\}$ days. Consider a portfolio of liquid equity index futures (10-day horizon) and illiquid credit derivatives (120-day horizon). Discuss qualitatively how the FRTB aggregation formula

$$
\text{ES} = \sqrt{\sum_{j=1}^{J} \left(\text{ES}_j(P_j)\right)^2}
$$

treats these two positions differently, and why this is economically appropriate.

??? success "Solution to Exercise 4"
    **FRTB variable liquidity horizons: qualitative analysis.**

    **Why FRTB replaces the uniform 10-day horizon:**

    Under Basel II.5, all trading book positions were subject to a uniform 10-day VaR horizon. This was inappropriate because:

    1. **Illiquid positions cannot be hedged or exited in 10 days.** Credit derivatives, structured products, and bespoke OTC instruments may take weeks or months to unwind. A 10-day horizon underestimates the risk of holding such positions during adverse markets.

    2. **Liquid positions are overcapitalized.** Equity index futures trade with enormous liquidity and can be exited intraday. Applying a 10-day horizon to these positions overstates the actual risk.

    3. **Uniform horizons create perverse incentives.** Banks are incentivized to hold illiquid, high-yielding positions because the capital charge does not reflect the true liquidation horizon.

    **How the FRTB formula treats the two positions differently:**

    Consider the portfolio with:

    - Liquid equity index futures: assigned $P_1 = 10$ days
    - Illiquid credit derivatives: assigned $P_2 = 120$ days

    The FRTB aggregation formula is:

    $$
    \text{ES} = \sqrt{\left(\text{ES}_1(10)\right)^2 + \left(\text{ES}_2(120)\right)^2}
    $$

    Under a square-root-of-time scaling approximation, $\text{ES}_j(P_j) \propto \sqrt{P_j}$. So even if the two positions have the same 1-day ES, the credit derivative contributes $\sqrt{120/10} = \sqrt{12} \approx 3.46$ times more to the aggregate ES than the equity futures.

    **Why this is economically appropriate:**

    The key insight is that the **risk horizon should match the liquidation horizon**. During a stress event:

    - The equity index futures can be closed out quickly (within days), limiting losses to approximately the 10-day ES.
    - The credit derivatives may be stuck on the books for months, accumulating losses over the full 120-day period before they can be hedged or sold.

    The FRTB formula captures this by assigning each risk factor its appropriate horizon, then aggregating under an independence assumption (the square-root-of-sum-of-squares structure). This ensures that illiquid positions receive capital charges commensurate with the actual risk of holding them through a stress period, while liquid positions are not overcapitalized.

---

**Exercise 5.** The Basel IV output floor requires

$$
\text{RWA}_{\text{floor}} = \max\!\big(\text{RWA}_{\text{internal}},\; 72.5\% \times \text{RWA}_{\text{standardized}}\big)
$$

A bank computes $\text{RWA}_{\text{internal}} = \$400$ billion and $\text{RWA}_{\text{standardized}} = \$620$ billion. Determine the binding RWA. By what percentage would the bank need to reduce its standardized RWA (holding internal RWA fixed) for the output floor to become non-binding?

??? success "Solution to Exercise 5"
    **Output floor analysis.**

    **Given:** $\text{RWA}_{\text{internal}} = \$400$ billion, $\text{RWA}_{\text{standardized}} = \$620$ billion.

    **Binding RWA:**

    $$
    \text{RWA}_{\text{floor}} = \max(\$400\text{B},\; 72.5\% \times \$620\text{B}) = \max(\$400\text{B},\; \$449.5\text{B}) = \$449.5 \text{ billion}
    $$

    The **output floor is binding** at \$449.5 billion, which exceeds the internal models RWA by \$49.5 billion ($12.4\%$ increase over internal RWA).

    **Reduction needed for the floor to become non-binding:**

    The floor becomes non-binding when:

    $$
    \text{RWA}_{\text{internal}} \geq 72.5\% \times \text{RWA}_{\text{standardized}}
    $$

    $$
    \$400\text{B} \geq 0.725 \times \text{RWA}_{\text{standardized}}
    $$

    $$
    \text{RWA}_{\text{standardized}} \leq \frac{\$400\text{B}}{0.725} = \$551.72 \text{ billion}
    $$

    The required reduction in standardized RWA:

    $$
    \Delta = \$620\text{B} - \$551.72\text{B} = \$68.28 \text{ billion}
    $$

    As a percentage:

    $$
    \frac{\$68.28\text{B}}{\$620\text{B}} \times 100\% = 11.01\%
    $$

    The bank would need to reduce its standardized RWA by approximately **11.0%** (from \$620B to \$551.7B) for the output floor to become non-binding, holding internal RWA fixed at \$400B.

---

**Exercise 6.** A bank has total exposure of \$1.2 trillion, Tier 1 capital of \$40 billion, HQLA of \$250 billion, and projected 30-day net cash outflows of \$230 billion. Compute the leverage ratio, the LCR, and determine which of these two constraints is binding. Discuss why regulators impose a non-risk-based leverage ratio alongside risk-weighted capital requirements.

??? success "Solution to Exercise 6"
    **Leverage ratio, LCR, and binding constraint analysis.**

    **Given:** Total exposure = \$1.2 trillion, Tier 1 capital = \$40 billion, HQLA = \$250 billion, 30-day net cash outflows = \$230 billion.

    **Leverage ratio:**

    $$
    \text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Exposure}} = \frac{\$40\text{B}}{\$1{,}200\text{B}} = 3.33\%
    $$

    The minimum requirement is 3%. The bank meets this requirement with a surplus of $3.33\% - 3.0\% = 0.33\%$.

    **Liquidity Coverage Ratio:**

    $$
    \text{LCR} = \frac{\text{HQLA}}{\text{Net Cash Outflows}} = \frac{\$250\text{B}}{\$230\text{B}} = 108.7\%
    $$

    The minimum requirement is 100%. The bank meets this requirement with a surplus of $108.7\% - 100\% = 8.7\%$.

    **Which constraint is binding?**

    Both constraints are met, but we assess which is closer to its limit:

    - Leverage ratio surplus: $0.33/3.0 = 11\%$ above minimum
    - LCR surplus: $8.7/100 = 8.7\%$ above minimum

    The **LCR is the more binding constraint** (8.7% surplus vs. 11% surplus in relative terms). A moderate outflow shock could push the LCR below 100%.

    However, both are relatively tight. In absolute terms, the leverage ratio has very thin headroom: the bank could sustain only a $\$40\text{B} \times (0.33\%/3.33\%) \approx \$4\text{B}$ reduction in Tier 1 capital before breaching the leverage ratio.

    **Why regulators impose a non-risk-based leverage ratio alongside risk-weighted requirements:**

    1. **Backstop against model risk.** Risk-weighted capital requirements depend on risk models that may underestimate risk. The leverage ratio is model-free -- it does not depend on risk weights, internal ratings, or any quantitative model. If models systematically understate risk (as happened pre-2008), the leverage ratio provides a hard floor on capital.

    2. **Addressing low-risk-weight arbitrage.** Under risk-weighted frameworks, banks can accumulate large exposures in "low-risk" asset classes (e.g., sovereign bonds, AAA-rated securities) with little capital. The leverage ratio penalizes all exposures equally, preventing excessive balance sheet expansion even in ostensibly safe assets.

    3. **Simplicity and transparency.** The leverage ratio is easy to compute, understand, and compare across institutions. It serves as a simple diagnostic tool for supervisors and market participants.

    4. **Complementarity.** The risk-weighted ratio and the leverage ratio constrain banks from different angles. The risk-weighted ratio is more granular and risk-sensitive, while the leverage ratio is robust but blunt. Together, they provide a more resilient capital framework than either alone.

---

**Exercise 7.** In the FRTB internal models approach, the aggregate capital charge is

$$
\text{IMCC} = \rho \cdot \text{ES}_{\text{FC}} + (1 - \rho) \cdot \sum_{i=1}^{5} \text{ES}_{\text{RC},i}
$$

with $\rho = 0.5$. Suppose $\text{ES}_{\text{FC}} = \$800$ million and the five risk class ES values are \$300M, \$250M, \$200M, \$150M, and \$100M. Compute the IMCC. Explain the economic rationale for the weighted average: what happens in the limits $\rho = 0$ and $\rho = 1$, and why did the BCBS choose an intermediate value?

??? success "Solution to Exercise 7"
    **FRTB IMCC computation and economic rationale.**

    **Computation:**

    $$
    \text{IMCC} = \rho \cdot \text{ES}_{\text{FC}} + (1 - \rho) \cdot \sum_{i=1}^{5} \text{ES}_{\text{RC},i}
    $$

    The sum of individual risk class ES values:

    $$
    \sum_{i=1}^{5} \text{ES}_{\text{RC},i} = 300 + 250 + 200 + 150 + 100 = \$1{,}000 \text{ million}
    $$

    With $\rho = 0.5$:

    $$
    \text{IMCC} = 0.5 \times 800 + 0.5 \times 1000 = 400 + 500 = \$900 \text{ million}
    $$

    **Economic rationale and limiting cases:**

    The IMCC formula is a weighted average between two extreme approaches to aggregating risk across risk classes:

    **Case $\rho = 1$: Full correlation recognition.**

    $$
    \text{IMCC} = \text{ES}_{\text{FC}} = \$800\text{M}
    $$

    This uses only the fully correlated ES, which accounts for diversification benefits across risk classes exactly as estimated by the bank's internal model. The capital charge is lowest because the model's estimated inter-class correlations (which typically imply diversification) are fully recognized.

    The problem: banks' correlation estimates may be unreliable, especially during stress when correlations tend to increase toward 1. Trusting the fully correlated ES entirely may understate tail risk.

    **Case $\rho = 0$: No correlation recognition (full add-up).**

    $$
    \text{IMCC} = \sum_{i=1}^{5} \text{ES}_{\text{RC},i} = \$1{,}000\text{M}
    $$

    This assumes no diversification across risk classes, treating each class independently and summing the ES values. The capital charge is highest, representing the most conservative assumption (perfect dependence in the tail).

    The problem: this ignores genuine diversification and may lead to excessive capital charges, reducing banks' ability to intermediate risk efficiently.

    **Why $\rho = 0.5$:**

    The BCBS chose $\rho = 0.5$ as a compromise:

    - It partially recognizes diversification benefits (through $\text{ES}_{\text{FC}}$), rewarding banks whose risk is genuinely diversified.
    - It partially penalizes potential correlation underestimation (through the sum of individual ES values), providing a buffer against the well-documented tendency for correlations to spike during crises.
    - The midpoint $\rho = 0.5$ reflects regulatory skepticism about the stability of cross-asset correlations while acknowledging that perfect dependence ($\rho = 0$) is also unrealistic.

    In this example, the IMCC of \$900M sits between the optimistic \$800M (full diversification) and the conservative \$1,000M (no diversification), adding a \$100M buffer above the fully correlated estimate to account for correlation uncertainty.
