# Extreme Scenarios

Extreme scenarios represent severe but plausible market conditions designed to test the resilience of portfolios and institutions. They form the core of stress testing frameworks and are essential for identifying hidden vulnerabilities.

---

## What Is an Extreme Scenario?

An extreme scenario involves:

- **Large, correlated market moves** across asset classes
- **Breakdown of normal relationships** (correlation regime shifts)
- **Stressed liquidity conditions** (widened bid-ask spreads, reduced depth)
- **Feedback effects** (fire sales, margin calls, contagion)

Extreme scenarios often **exceed historical extremes** in severity or combine features not previously observed together.

---

## Design Principles

### Severe but Plausible

The scenario must be:
- **Severe enough** to reveal vulnerabilities
- **Plausible enough** to be taken seriously by management
- **Economically coherent** (not arbitrary factor combinations)

**Bad example:** "All assets drop 50% while interest rates fall 500 bps"—internally inconsistent.

**Good example:** "Flight to quality with equity crash, credit spread widening, and rate rally in safe-haven bonds."

### Internally Consistent

Scenario factors should move together in economically meaningful ways:

$$
\text{Scenario Coherence:} \quad \Delta\mathbf{X} \text{ consistent with some } \mathbb{Q}^{\text{stress}}
$$

Use economic models or historical analogs to ensure consistency.

### Tailored to Portfolio

Scenarios should target the portfolio's specific vulnerabilities:
- Concentration risks
- Nonlinear exposures (options near barriers)
- Liquidity mismatches
- Funding dependencies

---

## Scenario Categories

### 1. Historical Scenarios

Replay specific historical episodes:

| Event | Period | Key Features |
|-------|--------|--------------|
| 2008 GFC | Sep-Oct 2008 | Credit freeze, equity crash, volatility spike |
| COVID Crash | Mar 2020 | Rapid equity decline, liquidity crisis, flight to quality |
| Dot-com Bust | 2000-2002 | Tech sector collapse, gradual equity decline |
| 1998 LTCM | Aug-Oct 1998 | EM crisis, credit spread widening, vol spike |
| Black Monday | Oct 1987 | Single-day equity crash (22%) |
| European Debt Crisis | 2011-2012 | Sovereign spreads, banking stress |

**Application:** Scale historical returns to current portfolio, often with adjustments for current market conditions.

### 2. Hypothetical Scenarios

Construct scenarios not directly observed historically:

**Geopolitical:**
- Major conflict escalation
- Sovereign default of G7 economy
- Trade war escalation

**Financial:**
- CCP failure
- Cyberattack on payment systems
- Simultaneous failure of multiple banks

**Economic:**
- Stagflation (high inflation + recession)
- Deflation spiral
- Currency crisis in reserve currency

### 3. Regulatory Scenarios

Scenarios prescribed by supervisors:

**Fed CCAR/DFAST Severely Adverse:**
- Typically includes recession, equity decline, credit spread widening
- Specifies paths for dozens of macro variables

**EBA Adverse Scenario:**
- EU-wide common scenario
- Multi-year horizon with specified GDP, unemployment, etc.

### 4. Sensitivity Scenarios

Single-factor shocks for granular analysis:

| Factor | Typical Shock |
|--------|---------------|
| Equity indices | −20% to −40% |
| Interest rates | ±100-300 bps |
| Credit spreads | +200-500 bps |
| FX rates | ±10-30% |
| Volatility (VIX) | +30-50 points |
| Commodity prices | ±30-50% |

---

## Quantitative Scenario Generation

### Mahalanobis Distance Approach

Define the "extremity" of a scenario $\mathbf{x}$ as:

$$
D(\mathbf{x}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})}
$$

Generate scenarios by targeting a specific Mahalanobis distance while varying the direction.

### Maximum Loss Direction

Find the scenario that maximizes portfolio loss for a given extremity:

$$
\mathbf{x}^* = \arg\max_{\mathbf{x}} L(\mathbf{x}) \quad \text{s.t.} \quad D(\mathbf{x}) \le D_{\text{target}}
$$

This identifies the **most dangerous** direction in risk factor space.

### Importance Sampling

Sample from a distribution tilted toward extreme outcomes:

$$
\mathbf{X} \sim f^{\text{tilted}}(\mathbf{x}) \propto f(\mathbf{x}) \cdot h(L(\mathbf{x}))
$$

where $h(\cdot)$ is an increasing function that overweights large losses.

---

## Correlation Under Stress

A critical feature of extreme scenarios is **correlation breakdown**:

### Empirical Evidence

During crises:
- Equity correlations increase (diversification fails)
- Equity-bond correlations may flip sign
- Credit spreads correlate with equity declines
- Liquidity correlations spike

### Stressed Correlation Modeling

**Approach 1: Scaling**

$$
\boldsymbol{\Sigma}^{\text{stress}} = \mathbf{D} \boldsymbol{\Sigma} \mathbf{D}
$$

where $\mathbf{D}$ is a diagonal scaling matrix.

**Approach 2: Correlation Adjustment**

$$
\boldsymbol{\rho}^{\text{stress}} = \alpha \boldsymbol{\rho}^{\text{normal}} + (1-\alpha) \mathbf{1}\mathbf{1}^\top
$$

This blends normal correlations toward perfect correlation.

**Approach 3: Regime-Switching Copulas**
Use different copulas for normal vs. stressed regimes (e.g., Gaussian normal, $t$ or Clayton stressed).

---

## Portfolio Impact Analysis

### Full Revaluation

For complex portfolios (options, structured products):

$$
L^{\text{stress}} = P_0 - P(\mathbf{x}^{\text{stress}})
$$

where $P(\mathbf{x})$ is the full pricing function.

### Sensitivity-Based Approximation

For large portfolios, approximate using Greeks:

$$
L^{\text{stress}} \approx -\sum_i \Delta_i \cdot \Delta x_i - \frac{1}{2} \sum_{i,j} \Gamma_{ij} \cdot \Delta x_i \cdot \Delta x_j - \sum_i \mathcal{V}_i \cdot \Delta \sigma_i
$$

**Warning:** Approximations can fail for large moves; use full revaluation when feasible.

---

## Nonlinear Effects

Extreme scenarios reveal nonlinearities masked in normal conditions:

### Option Payoffs
- Barrier breaches
- Deep ITM/OTM transitions
- Volatility smile effects

### Margin and Collateral
- Margin calls under stress
- Collateral haircuts increase
- Forced liquidation losses

### Funding
- Funding costs spike
- Rollover risk materializes
- Counterparty credit concerns

---

## Second-Round Effects

First-round effects: Direct P&L impact of factor moves.

Second-round effects (often more severe):
- **Fire sales:** Forced selling depresses prices further
- **Margin spirals:** Losses trigger margin calls, requiring more selling
- **Funding withdrawal:** Counterparties reduce credit lines
- **Contagion:** Default of one entity affects others

**Modeling challenge:** Second-round effects require dynamic, agent-based, or network models.

---

## Example: 2008-Style Crisis Scenario

### Scenario Specification

| Factor | Move | Rationale |
|--------|------|-----------|
| S&P 500 | −40% | Equity bear market |
| VIX | +50 points | Fear spike |
| 10Y Treasury | −150 bps | Flight to quality |
| IG Spreads | +200 bps | Credit stress |
| HY Spreads | +800 bps | Default fears |
| USD/EUR | +15% | Dollar strength |
| Oil | −50% | Demand collapse |

### Correlation Assumptions

- Equity correlations: 0.7 → 0.9
- Equity-credit correlation: 0.5 → 0.8
- Liquidity: Bid-ask spreads 3× normal

### Timeline

| Phase | Duration | Characteristics |
|-------|----------|-----------------|
| Acute | Weeks 1-2 | Sharp declines, extreme vol |
| Sustained | Months 1-3 | Continued stress, bankruptcies |
| Recovery | Months 3-12 | Gradual normalization |

---

## Governance and Usage

### Scenario Approval

- Scenarios should be approved by senior risk committee
- Clear documentation of assumptions and rationale
- Regular review and update (at least annually)

### Integration with Risk Limits

- Stress losses inform position limits
- Capital buffers sized to absorb stress scenarios
- Trigger points for risk reduction

### Board Reporting

- Key stress results reported to board
- Comparison to capital and liquidity buffers
- Action plans for severe scenarios

### Documentation

Each scenario should document:
- Economic narrative
- Factor specifications
- Historical analogies
- Key assumptions
- Known limitations

---

## Limitations

### Scenario Selection Bias
Chosen scenarios may miss the actual future crisis.

### Model Dependence
Revaluation models may fail under extreme conditions.

### Behavioral Responses
Scenarios often ignore management actions and market adaptations.

### Probability Assignment
Extreme scenarios typically lack probability assignments, complicating aggregation.

---

## Key Takeaways

- Extreme scenarios probe vulnerabilities beyond historical data
- Scenarios must be severe, plausible, and internally consistent
- Correlation increases under stress—diversification fails
- Second-round effects (fire sales, margin spirals) amplify first-round losses
- Nonlinear positions require full revaluation
- Scenarios need governance, documentation, and regular updates

---

## Further Reading

- Basel Committee, "Principles for Sound Stress Testing Practices and Supervision"
- Glasserman, P., Kang, C., & Kang, W. (2015), "Stress Scenario Selection by Empirical Likelihood"
- Breuer, T. & Csiszár, I. (2013), "Systematic Stress Tests with Entropic Plausibility Constraints"
- IMF, "Stress Testing: Principles, Concepts, and Frameworks"
- Flood, M. & Korenko, G. (2015), "Systematic Scenario Selection"

---

## Exercises

**Exercise 1.** A portfolio has exposure to equities, credit, and interest rates. Using the sensitivity-based approximation

$$
L^{\text{stress}} \approx -\sum_i \Delta_i \cdot \Delta x_i - \frac{1}{2} \sum_{i,j} \Gamma_{ij} \cdot \Delta x_i \cdot \Delta x_j
$$

compute the stress loss given $\Delta_{\text{equity}} = 50$M per 1%, $\Delta_{\text{credit}} = -30$M per 100 bps, $\Gamma_{\text{equity,equity}} = 2$M per 1%$^2$, and the scenario $\Delta x_{\text{equity}} = -25\%$, $\Delta x_{\text{credit}} = +400$ bps. Discuss when this approximation would fail significantly.

---

**Exercise 2.** The Mahalanobis distance of a scenario $\mathbf{x}$ from the mean $\boldsymbol{\mu}$ under covariance $\boldsymbol{\Sigma}$ is

$$
D(\mathbf{x}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})}
$$

For a two-factor model with $\boldsymbol{\mu} = (0, 0)^\top$ and $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.6 \\ 0.6 & 1 \end{pmatrix}$, compute the Mahalanobis distance for the scenarios $\mathbf{x}_1 = (-3, -3)^\top$ and $\mathbf{x}_2 = (-3, 3)^\top$. Which scenario is more "extreme" in the Mahalanobis sense? Discuss which is more plausible during a flight-to-quality episode.

---

**Exercise 3.** Explain the difference between first-round and second-round effects in stress testing. A bank holds \$10 billion in corporate bonds. Under a stress scenario, credit spreads widen by 300 bps, causing a mark-to-market loss of \$1.5 billion (first round). Describe a plausible chain of second-round effects and estimate qualitatively how they might amplify the total loss. Why are second-round effects particularly difficult to model?

---

**Exercise 4.** The stressed correlation blending formula is

$$
\boldsymbol{\rho}^{\text{stress}} = \alpha \boldsymbol{\rho}^{\text{normal}} + (1-\alpha) \mathbf{1}\mathbf{1}^\top
$$

Show that if $\boldsymbol{\rho}^{\text{normal}}$ is a valid correlation matrix with ones on the diagonal, then $\boldsymbol{\rho}^{\text{stress}}$ also has ones on the diagonal. For a 3-asset portfolio with pairwise normal correlations $\rho_{12} = 0.3$, $\rho_{13} = 0.4$, $\rho_{23} = 0.2$, compute $\boldsymbol{\rho}^{\text{stress}}$ with $\alpha = 0.3$. How does portfolio diversification benefit change between the normal and stressed cases?

---

**Exercise 5.** A risk manager must design a hypothetical stagflation scenario. Specify at least six risk factors (equities, rates, credit spreads, FX, commodities, volatility) and their stressed values. Ensure the scenario is internally consistent: explain the economic logic linking each factor move to the stagflation narrative. Why is stagflation particularly challenging for portfolios that use equities and bonds as diversifiers?

---

**Exercise 6.** Consider the maximum loss direction problem

$$
\mathbf{x}^* = \arg\max_{\mathbf{x}} L(\mathbf{x}) \quad \text{s.t.} \quad D(\mathbf{x}) \le D_{\text{target}}
$$

For a portfolio with linear loss function $L(\mathbf{x}) = \mathbf{w}^\top \mathbf{x}$ and Mahalanobis distance constraint, show that the maximum loss scenario is $\mathbf{x}^* = -D_{\text{target}} \cdot \boldsymbol{\Sigma} \mathbf{w} / \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}$ (up to sign). Interpret this result: in which direction does the worst-case scenario point?

---

**Exercise 7.** Under the Fed CCAR severely adverse scenario, a bank projects losses of \$15 billion over 9 quarters against a starting CET1 capital of \$80 billion and RWA of \$600 billion. Compute the projected minimum CET1 ratio (ignoring any revenue offsets). If the regulatory minimum CET1 ratio including buffers is 7%, does the bank pass the stress test? Discuss why regulators prefer multi-quarter scenarios over instantaneous shocks.
