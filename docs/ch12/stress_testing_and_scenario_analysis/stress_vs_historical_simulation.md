# Stress Testing vs Historical Simulation

Stress testing and historical simulation are two complementary approaches to assessing portfolio risk. Understanding their differences, strengths, and appropriate use cases is essential for robust risk management.

---

## Overview

| Aspect | Historical Simulation | Stress Testing |
|--------|----------------------|----------------|
| **Perspective** | Backward-looking | Forward-looking |
| **Data source** | Past observations | Hypothetical/extreme scenarios |
| **Distributional assumptions** | Minimal | Scenario-specific |
| **Tail coverage** | Limited to historical sample | Explicitly designed |
| **Primary use** | VaR/ES estimation | Capital adequacy, resilience |

---

## Historical Simulation

### Methodology

Historical simulation estimates risk by revaluing the portfolio under historical market movements.

**Algorithm:**
1. Collect $n$ historical return observations: $\mathbf{r}_1, \mathbf{r}_2, \ldots, \mathbf{r}_n$
2. Apply each historical return to current portfolio: $L_i = -P_0 \cdot (e^{\mathbf{w}^\top \mathbf{r}_i} - 1)$
3. Order losses: $L_{(1)} \le L_{(2)} \le \cdots \le L_{(n)}$
4. Estimate VaR and ES from empirical distribution

**VaR estimator:**
$$
\widehat{\text{VaR}}_\alpha = L_{(\lceil n\alpha \rceil)}
$$

**ES estimator:**
$$
\widehat{\text{ES}}_\alpha = \frac{1}{n(1-\alpha)} \sum_{i=\lceil n\alpha \rceil}^n L_{(i)}
$$

### Advantages

- **Model-free:** No parametric distributional assumptions
- **Captures fat tails:** If fat tails exist in data, they appear in estimates
- **Intuitive:** Based on actual market behavior
- **Captures nonlinearities:** Full revaluation incorporates option payoffs, etc.
- **Regulatory acceptance:** Widely used for internal models

### Limitations

- **Sample dependence:** Limited by historical data availability
- **Stationarity assumption:** Assumes past is representative of future
- **Clustering effects:** May under/overweight recent volatility
- **Tail sparsity:** Few observations in extreme tails
- **Structural breaks:** May miss regime changes

---

## Filtered Historical Simulation

An enhancement that addresses volatility clustering:

1. Fit a GARCH model to historical returns
2. Standardize returns: $\epsilon_t = r_t / \sigma_t$
3. Apply standardized innovations to current volatility forecast
4. Generate "volatility-adjusted" scenarios

**Advantages:**
- Adapts to current volatility regime
- Better tail coverage during high-volatility periods

---

## Stress Testing

### Concept

Stress testing evaluates portfolio losses under **hypothetical or extreme scenarios** designed to probe vulnerabilities beyond historical experience.

**Key distinction:** Stress tests ask "what if?" rather than "what happened?"

### Types of Stress Tests

**1. Historical Scenarios**
Replay specific historical events:
- 2008 Global Financial Crisis
- 2020 COVID-19 market crash
- 1998 LTCM crisis
- 1987 Black Monday

**2. Hypothetical Scenarios**
Economically motivated but not historically observed:
- Sovereign default of major economy
- Simultaneous equity crash and interest rate spike
- Cyberattack on financial infrastructure

**3. Sensitivity Analysis**
Single-factor shocks:
- Equity indices down 20%
- Interest rates up 200 bps
- Credit spreads widen 500 bps
- FX depreciation 30%

**4. Reverse Stress Testing**
Work backward from failure threshold (see [Reverse Stress Testing](reverse_stress_testing.md)).

---

## Scenario Design Principles

Effective stress scenarios should be:

### Severe but Plausible
- Extreme enough to be informative
- Not so extreme as to be dismissed as impossible
- Economically coherent (not arbitrary combinations)

### Relevant
- Target the portfolio's specific vulnerabilities
- Reflect plausible risk factor movements
- Consider concentration risks

### Comprehensive
- Cover multiple risk types (market, credit, liquidity)
- Include second-round effects
- Account for correlations under stress

### Dynamic
- Updated as portfolio and markets evolve
- Include emerging risks
- Not purely backward-looking

---

## Mathematical Framework for Stress Testing

### Scenario Definition

A stress scenario $\mathcal{S}$ specifies values or distributions for risk factors:

$$
\mathcal{S}: \mathbf{X} \mapsto \mathbf{x}^{\text{stress}} \quad \text{or} \quad \mathbf{X} \sim F^{\text{stress}}
$$

### Portfolio Loss Under Stress

For scenario $\mathcal{S}$:
$$
L^{\mathcal{S}} = P_0 - P(\mathbf{x}^{\text{stress}})
$$

where $P(\mathbf{x})$ is the portfolio value function.

### Stressed Risk Measures

Regulatory frameworks often require "stressed" versions of risk measures:

$$
\text{Stressed VaR} = \text{VaR}_\alpha \text{ using a stressed historical period}
$$

$$
\text{Stressed ES} = \text{ES}_\alpha \text{ calibrated to stress conditions}
$$

---

## Correlation Under Stress

A critical consideration is that **correlations change under stress**:

- Diversification benefits erode
- "Correlation breakdown": assets that seem uncorrelated become highly correlated
- Liquidity correlations spike

**Approaches:**
1. **Stressed correlation matrices:** Increase correlations uniformly or selectively
2. **Copula-based stress:** Use different copulas for normal vs. stressed conditions
3. **Factor models:** Increase factor loadings under stress

---

## Comparison Table

| Feature | Historical Simulation | Stress Testing |
|---------|----------------------|----------------|
| **Time horizon** | Fixed (e.g., 10 days) | Variable |
| **Probability assignment** | Implicit (empirical) | Often not assigned |
| **Model dependence** | Low | Moderate to high |
| **Tail coverage** | Data-limited | By design |
| **Forward-looking** | No | Yes |
| **Captures "unknown unknowns"** | No | Potentially |
| **Regulatory use** | VaR/ES capital | ICAAP, CCAR, DFAST |

---

## Integration: Complementary Roles

Robust risk management uses **both** approaches:

### Historical Simulation
- Day-to-day risk monitoring
- VaR and ES estimation
- Backtesting
- Trading limit calibration

### Stress Testing
- Capital planning
- Identification of concentrations
- Board-level risk reporting
- Recovery and resolution planning

### Best Practice
$$
\text{Total Risk Picture} = \text{Statistical Measures (VaR/ES)} + \text{Stress Test Results}
$$

Neither alone is sufficient.

---

## Regulatory Requirements

### Basel Framework
- Internal models: VaR/ES from historical simulation or Monte Carlo
- Stressed VaR: Using 12-month period of significant stress
- Stress testing: Supervisory and internal scenarios

### US Federal Reserve (CCAR/DFAST)
- Annual stress tests for large banks
- Severely adverse scenario specified by Fed
- Capital adequacy under stress

### European Banking Authority
- EU-wide stress tests
- Common methodology across banks
- Publication of results

---

## Practical Implementation

### Historical Simulation Implementation

```
1. Data collection
   - Minimum 250 days (regulatory)
   - Ideally 3-5 years
   - Clean and align data

2. Portfolio mapping
   - Map positions to risk factors
   - Handle missing data

3. Revaluation
   - Full revaluation preferred
   - Delta-gamma approximation acceptable

4. Aggregation
   - Apply netting rules
   - Consider collateral

5. Risk measure calculation
   - VaR: empirical quantile
   - ES: tail average
```

### Stress Testing Implementation

```
1. Scenario design
   - Historical analysis
   - Economic judgment
   - Regulatory guidance

2. Scenario specification
   - Specify all relevant risk factors
   - Ensure internal consistency

3. Impact assessment
   - Full revaluation under scenario
   - Include second-round effects

4. Result analysis
   - Compare to capital buffers
   - Identify vulnerabilities

5. Management action
   - Report to senior management
   - Inform risk limits
```

---

## Key Takeaways

- Historical simulation is backward-looking; stress testing is forward-looking
- Historical simulation captures typical behavior; stress testing probes extremes
- Both have limitations: sample constraints vs. scenario subjectivity
- Correlations change under stress—diversification benefits erode
- Regulatory frameworks require both approaches
- Neither is sufficient alone; they are complementary tools

---

## Further Reading

- McNeil, A., Frey, R., & Embrechts, P., *Quantitative Risk Management* (historical simulation)
- Basel Committee on Banking Supervision, "Stress Testing Principles"
- Berkowitz, J. (2001), "Testing Density Forecasts, with Applications to Risk Management"
- Pritsker, M. (2006), "The Hidden Dangers of Historical Simulation"
- Glasserman, P. (2004), *Monte Carlo Methods in Financial Engineering*
