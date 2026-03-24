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

---

## Exercises

**Exercise 1.** A portfolio has 500 days of historical returns. Using historical simulation, compute the 99% VaR as $L_{(\lceil 500 \times 0.99 \rceil)} = L_{(495)}$ and the 99% ES as the average of the 5 worst losses. If the 5 largest losses (in millions) are 12.3, 10.8, 9.5, 8.7, and 8.1, compute both the VaR and ES. Discuss why the ES estimate based on only 5 observations has high sampling uncertainty.

---

**Exercise 2.** Explain the concept of filtered historical simulation. A GARCH(1,1) model estimates current conditional volatility at $\hat{\sigma}_t = 2.5\%$ (daily), while the historical average volatility is $1.5\%$. A historical return of $r_s = -3.0\%$ has a standardized innovation $\epsilon_s = r_s / 1.5\% = -2.0$. Under filtered historical simulation, what is the volatility-adjusted scenario return applied to the current portfolio? Compare this to the unfiltered historical simulation return and discuss when filtered simulation gives materially different risk estimates.

---

**Exercise 3.** A risk manager must decide between using 1 year (250 days) and 4 years (1,000 days) of historical data for VaR estimation at the 99% confidence level. With 250 days, there are approximately 2-3 observations in the tail; with 1,000 days, approximately 10. Discuss the tradeoff between sample size and relevance (stationarity). Under what market conditions would the shorter window be preferred? Compute the standard error of the empirical 99% quantile for both sample sizes using the approximation $\text{SE}(\hat{q}_\alpha) \approx \sqrt{\alpha(1-\alpha)/(n \cdot f(q_\alpha)^2)}$, assuming $f(q_\alpha) = 0.02$.

---

**Exercise 4.** During the 2008 financial crisis, correlations between major equity markets increased from approximately 0.6 to 0.9. A portfolio is equally weighted across 4 equity markets, each with daily volatility $\sigma = 1.5\%$. Compute the portfolio daily volatility under normal correlations ($\rho = 0.6$) and stressed correlations ($\rho = 0.9$). What is the percentage increase in portfolio risk? Explain why historical simulation using pre-crisis data would underestimate risk during the crisis.

---

**Exercise 5.** Compare how historical simulation and stress testing handle the following scenario: a central bank unexpectedly raises rates by 300 bps (an event not observed in the 5-year historical window). Explain why historical simulation fails to capture this risk and how a stress test can address it. Describe how you would design an internally consistent stress scenario around this rate shock, specifying at least four other risk factors and their plausible movements.

---

**Exercise 6.** A bank uses historical simulation with a 250-day window for daily VaR reporting and also runs quarterly stress tests with scenarios calibrated to 2008-level severity. The historical simulation 99% VaR is \$50 million, while the stress test loss is \$350 million. Discuss the implications of this large gap. Should the bank's capital be sized to the VaR estimate or the stress test loss? Explain the regulatory formula

$$
\text{Total Risk Picture} = \text{Statistical Measures (VaR/ES)} + \text{Stress Test Results}
$$

and how each component contributes to the capital requirement.

---

**Exercise 7.** The Basel framework requires banks to compute a "Stressed VaR" using a 12-month period of significant stress. Explain the methodology: how is the stress period selected, and how is Stressed VaR different from simply applying historical simulation with all available data? If a bank selects the period September 2008 to August 2009, discuss what features of the market during that period would cause the Stressed VaR to be significantly higher than the current VaR computed over the most recent 250 days of relatively calm markets.
