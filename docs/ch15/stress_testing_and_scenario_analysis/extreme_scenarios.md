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
