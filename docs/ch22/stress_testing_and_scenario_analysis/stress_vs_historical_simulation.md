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

Recall (see [§ Scenario Categories](extreme_scenarios.md#scenario-categories)) for the full taxonomy: historical (2008 GFC, COVID, LTCM, 1987), hypothetical (geopolitical, sovereign default, cyber), regulatory (CCAR, EBA), and single-factor sensitivity shocks. A fourth complementary mode is **reverse stress testing**: work backward from a failure threshold (see [Reverse Stress Testing](reverse_stress_testing.md)).

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

Recall (see [§ Correlation Under Stress](extreme_scenarios.md#correlation-under-stress)): diversification benefits erode as correlations spike, with stressed-correlation modeling via scaling $\boldsymbol{\Sigma}^{\text{stress}} = \mathbf{D}\boldsymbol{\Sigma}\mathbf{D}$, blending $\boldsymbol{\rho}^{\text{stress}} = \alpha\boldsymbol{\rho} + (1-\alpha)\mathbf{1}\mathbf{1}^\top$, or regime-switching copulas. The key point for historical simulation is that calm-period data embeds **normal-regime correlations**, so VaR estimates miss the correlation breakdown that defines a crisis.

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

??? success "Solution to Exercise 1"

    **Step 1: Compute the 99% VaR.**

    With $n = 500$ days, the 99% VaR is the $\lceil 500 \times 0.99 \rceil = 495$-th largest loss when ordered from smallest to largest. Equivalently, it is the 5th largest loss (since $500 - 495 = 5$ observations exceed it, but VaR is the threshold at the 99th percentile). The 5th largest loss is:

    $$
    \widehat{\text{VaR}}_{99\%} = L_{(495)} = \$8.1 \text{ million}
    $$

    (The 5 largest losses are 12.3, 10.8, 9.5, 8.7, 8.1, so the 5th largest, which is the VaR threshold, is 8.1.)

    Actually, let us be more precise. In the ordering $L_{(1)} \le L_{(2)} \le \cdots \le L_{(500)}$, the 5 largest values are:

    - $L_{(500)} = 12.3$
    - $L_{(499)} = 10.8$
    - $L_{(498)} = 9.5$
    - $L_{(497)} = 8.7$
    - $L_{(496)} = 8.1$

    So $L_{(495)}$ is the next value below 8.1 (the 6th largest loss), which is not given. The index $\lceil 500 \times 0.99 \rceil = \lceil 495 \rceil = 495$.

    By convention, the 99% VaR from 500 observations can also be defined as the 5th worst loss:

    $$
    \widehat{\text{VaR}}_{99\%} = L_{(496)} = \$8.1 \text{ million}
    $$

    using the convention $\widehat{\text{VaR}}_\alpha = L_{(\lceil n\alpha \rceil)}$ where $\lceil 500 \times 0.99 \rceil = 495$, or equivalently as the $n(1-\alpha) = 5$th worst observation.

    Under the standard convention:

    $$
    \widehat{\text{VaR}}_{99\%} = \$8.1 \text{ million}
    $$

    **Step 2: Compute the 99% ES.**

    The ES is the average of the losses exceeding the VaR:

    $$
    \widehat{\text{ES}}_{99\%} = \frac{1}{n(1-\alpha)}\sum_{i: L_i > \text{VaR}} L_i = \frac{1}{5}(12.3 + 10.8 + 9.5 + 8.7 + 8.1)
    $$

    $$
    = \frac{49.4}{5} = \$9.88 \text{ million}
    $$

    **Step 3: Discuss sampling uncertainty.**

    The ES estimate of \$9.88M is based on only **5 observations**. This tiny sample size creates several problems:

    1. **High variance:** The standard error of the mean of 5 observations is approximately $s / \sqrt{5}$, where $s$ is the standard deviation of the 5 tail observations. Here $s \approx 1.72$M, giving $\text{SE} \approx 1.72/\sqrt{5} \approx 0.77$M. A 95% confidence interval for ES would be roughly $9.88 \pm 1.5$M, spanning from about \$8.4M to \$11.4M---a range of more than 30% of the point estimate.

    2. **Sensitivity to outliers:** If the largest observation (12.3) were instead 15.0, the ES would jump to $(15.0 + 10.8 + 9.5 + 8.7 + 8.1)/5 = 10.42$M, a 5.5% increase driven by a single observation.

    3. **Bootstrapping instability:** Bootstrap resamples of the 500 observations will frequently produce different sets of 5 tail observations, leading to highly variable ES estimates across resamples.

    4. **Tail risk is understated:** With only 500 days of data, the sample may not include truly extreme events. The worst day in the sample (12.3M) may be far from the true tail---events of 20M+ may occur with non-negligible probability but simply have not been observed in this short window.

    This is precisely why EVT-based approaches (which model the tail parametrically) or longer data windows are preferred for estimating tail risk measures at high confidence levels.

---

**Exercise 2.** Explain the concept of filtered historical simulation. A GARCH(1,1) model estimates current conditional volatility at $\hat{\sigma}_t = 2.5\%$ (daily), while the historical average volatility is $1.5\%$. A historical return of $r_s = -3.0\%$ has a standardized innovation $\epsilon_s = r_s / 1.5\% = -2.0$. Under filtered historical simulation, what is the volatility-adjusted scenario return applied to the current portfolio? Compare this to the unfiltered historical simulation return and discuss when filtered simulation gives materially different risk estimates.

??? success "Solution to Exercise 2"

    **Concept of filtered historical simulation (FHS):**

    Standard historical simulation applies historical returns directly to the current portfolio, implicitly assuming that the volatility environment of the past is representative of the present. FHS corrects for this by:

    1. Fitting a GARCH(1,1) model to estimate conditional volatility $\sigma_t$ for each historical day.
    2. Extracting standardized innovations: $\epsilon_t = r_t / \sigma_t$.
    3. Scaling these innovations by the current volatility forecast: $r_t^{\text{adjusted}} = \epsilon_t \times \hat{\sigma}_{\text{current}}$.

    **Given:**

    - Current conditional volatility: $\hat{\sigma}_t = 2.5\%$
    - Historical average volatility: $1.5\%$
    - Historical return: $r_s = -3.0\%$
    - Standardized innovation: $\epsilon_s = -3.0\% / 1.5\% = -2.0$

    **Filtered (volatility-adjusted) scenario return:**

    $$
    r_s^{\text{adjusted}} = \epsilon_s \times \hat{\sigma}_t = (-2.0) \times 2.5\% = -5.0\%
    $$

    **Comparison:**

    - Unfiltered: $r_s = -3.0\%$
    - Filtered: $r_s^{\text{adjusted}} = -5.0\%$

    The filtered return is **67% larger in magnitude** than the unfiltered return. This is because the current market is in a high-volatility regime ($\hat{\sigma}_t = 2.5\%$ vs. the historical average of $1.5\%$), and a $-2\sigma$ event today is much larger than a $-2\sigma$ event during the historical average-volatility period.

    **When FHS gives materially different results:**

    FHS produces materially different risk estimates when current volatility diverges significantly from the historical average:

    - **High current volatility** (e.g., during market turmoil): FHS scales up historical returns, producing larger VaR and ES estimates than unfiltered HS. This is appropriate because risk is genuinely higher.
    - **Low current volatility** (e.g., during calm periods): FHS scales down historical returns, producing *smaller* VaR estimates. This can be dangerous if the calm period precedes a volatility spike.
    - **Stable volatility:** When current and historical volatility are similar, FHS and unfiltered HS give nearly identical results.

    The key advantage of FHS is that it makes VaR estimates **responsive to the current volatility regime** while preserving the non-parametric, model-free character of historical simulation (the shape of the standardized innovation distribution is empirical, not assumed normal).

---

**Exercise 3.** A risk manager must decide between using 1 year (250 days) and 4 years (1,000 days) of historical data for VaR estimation at the 99% confidence level. With 250 days, there are approximately 2-3 observations in the tail; with 1,000 days, approximately 10. Discuss the tradeoff between sample size and relevance (stationarity). Under what market conditions would the shorter window be preferred? Compute the standard error of the empirical 99% quantile for both sample sizes using the approximation $\text{SE}(\hat{q}_\alpha) \approx \sqrt{\alpha(1-\alpha)/(n \cdot f(q_\alpha)^2)}$, assuming $f(q_\alpha) = 0.02$.

??? success "Solution to Exercise 3"

    **Part 1: Tradeoff between sample size and relevance.**

    **250-day window (1 year):**

    - Approximately $250 \times 0.01 = 2.5$ observations in the tail (i.e., 2--3 losses beyond the 99% VaR).
    - **Advantage (relevance):** The short window captures the current market regime. If volatility, correlations, or market structure have changed recently, the 1-year window reflects current conditions.
    - **Disadvantage (sample size):** With only 2--3 tail observations, the VaR and ES estimates are extremely noisy. A single outlier day can dominate.

    **1000-day window (4 years):**

    - Approximately $1000 \times 0.01 = 10$ observations in the tail.
    - **Advantage (sample size):** More tail observations yield more stable estimates with lower sampling error.
    - **Disadvantage (relevance):** The 4-year window includes data from potentially different regimes. If market conditions have changed (e.g., a shift from low-volatility to high-volatility regime), the older data may dilute the signal from current conditions.

    **Part 2: When the shorter window is preferred.**

    The shorter 250-day window is preferred when:

    - There has been a **recent regime change** (e.g., onset of a crisis, major policy shift) and the older data is no longer representative.
    - The portfolio has changed significantly and older data applies to a different portfolio composition.
    - Market microstructure has changed (e.g., introduction of new instruments, changes in market participants).

    **Part 3: Standard error computation.**

    The standard error of the empirical $\alpha$-quantile is approximately:

    $$
    \text{SE}(\hat{q}_\alpha) \approx \frac{\sqrt{\alpha(1-\alpha)}}{\sqrt{n} \cdot f(q_\alpha)}
    $$

    where $f(q_\alpha)$ is the density at the quantile. With $\alpha = 0.99$ and $f(q_\alpha) = 0.02$:

    $$
    \sqrt{\alpha(1-\alpha)} = \sqrt{0.99 \times 0.01} = \sqrt{0.0099} = 0.09950
    $$

    **For $n = 250$:**

    $$
    \text{SE} = \frac{0.09950}{\sqrt{250} \times 0.02} = \frac{0.09950}{15.811 \times 0.02} = \frac{0.09950}{0.3162} = 0.3147
    $$

    **For $n = 1000$:**

    $$
    \text{SE} = \frac{0.09950}{\sqrt{1000} \times 0.02} = \frac{0.09950}{31.623 \times 0.02} = \frac{0.09950}{0.6325} = 0.1573
    $$

    The standard error with 1000 observations is exactly **half** that with 250 observations (since $\sqrt{1000/250} = 2$). In practical terms, if the true 99% VaR is \$10M and $f(q_{0.99}) = 0.02$:

    - With 250 days: 95% CI $\approx \$10\text{M} \pm 2 \times 0.3147 / 0.02 \approx \$10\text{M} \pm \$31.5\text{M}$

    These are units of the quantile itself. In relative terms, the SE is approximately $0.3147$ for 250 days and $0.1573$ for 1000 days, measured in units of the loss distribution. The 4x increase in sample size halves the standard error, illustrating the $\sqrt{n}$ convergence rate.

---

**Exercise 4.** During the 2008 financial crisis, correlations between major equity markets increased from approximately 0.6 to 0.9. A portfolio is equally weighted across 4 equity markets, each with daily volatility $\sigma = 1.5\%$. Compute the portfolio daily volatility under normal correlations ($\rho = 0.6$) and stressed correlations ($\rho = 0.9$). What is the percentage increase in portfolio risk? Explain why historical simulation using pre-crisis data would underestimate risk during the crisis.

??? success "Solution to Exercise 4"

    **Step 1: Portfolio variance formula.**

    For an equally weighted portfolio of 4 assets, each with weight $w_i = 1/4$ and common daily volatility $\sigma = 1.5\%$, with common pairwise correlation $\rho$:

    $$
    \sigma_p^2 = \sum_{i=1}^4 w_i^2 \sigma^2 + 2\sum_{i<j} w_i w_j \rho \sigma^2 = 4 \cdot \frac{1}{16}\sigma^2 + 2 \cdot \binom{4}{2} \cdot \frac{1}{16} \rho \sigma^2
    $$

    $$
    = \frac{\sigma^2}{4} + 2 \cdot 6 \cdot \frac{\rho \sigma^2}{16} = \frac{\sigma^2}{4}(1 + 3\rho)
    $$

    More generally, for $n$ equally weighted assets with common $\sigma$ and $\rho$:

    $$
    \sigma_p^2 = \frac{\sigma^2}{n}\left(1 + (n-1)\rho\right)
    $$

    For $n = 4$: $\sigma_p^2 = \frac{\sigma^2}{4}(1 + 3\rho)$.

    **Step 2: Normal correlations ($\rho = 0.6$).**

    $$
    \sigma_p^2 = \frac{(1.5\%)^2}{4}(1 + 1.8) = \frac{0.000225}{4} \times 2.8 = 0.00015750
    $$

    $$
    \sigma_p = \sqrt{0.00015750} = 1.255\%
    $$

    **Step 3: Stressed correlations ($\rho = 0.9$).**

    $$
    \sigma_p^2 = \frac{(1.5\%)^2}{4}(1 + 2.7) = \frac{0.000225}{4} \times 3.7 = 0.00020813
    $$

    $$
    \sigma_p = \sqrt{0.00020813} = 1.443\%
    $$

    **Step 4: Percentage increase in portfolio risk.**

    $$
    \text{Increase} = \frac{1.443 - 1.255}{1.255} = \frac{0.188}{1.255} = 14.9\%
    $$

    The portfolio daily volatility increases by approximately **15%** purely from the correlation increase, with no change in individual asset volatilities.

    For comparison, if correlations were $\rho = 1$ (perfect correlation):

    $$
    \sigma_p = \sigma = 1.5\%
    $$

    So the portfolio volatility ranges from $1.255\%$ (normal) to $1.443\%$ (stressed) to $1.500\%$ (perfect correlation). Under stress, the portfolio moves 75% of the way from the normal-regime volatility toward the undiversified level.

    **Step 5: Why historical simulation using pre-crisis data would underestimate risk.**

    Historical simulation with pre-crisis data (using historical returns from the calm period) captures the correlation structure that prevailed during that period ($\rho \approx 0.6$). The resulting VaR reflects the **normal-regime** portfolio volatility of 1.255%.

    During the crisis, the realized correlation jumps to $\rho \approx 0.9$, and the actual portfolio risk is 1.443% or higher. The VaR computed from pre-crisis data systematically understates the risk because:

    1. The historical returns reflect lower volatility (volatility was lower pre-crisis).
    2. The historical co-movements reflect lower correlations (diversification that existed pre-crisis evaporates during the crisis).
    3. The interaction of higher volatilities *and* higher correlations amplifies the underestimation: both the individual return magnitudes and their tendency to move together are understated.

    This is one of the fundamental limitations of backward-looking historical simulation: it cannot anticipate regime changes in the volatility and correlation structure.

---

**Exercise 5.** Compare how historical simulation and stress testing handle the following scenario: a central bank unexpectedly raises rates by 300 bps (an event not observed in the 5-year historical window). Explain why historical simulation fails to capture this risk and how a stress test can address it. Describe how you would design an internally consistent stress scenario around this rate shock, specifying at least four other risk factors and their plausible movements.

??? success "Solution to Exercise 5"

    **Part 1: Why historical simulation fails.**

    Historical simulation generates risk estimates by replaying the $n$ most recent historical market moves on the current portfolio. If the 5-year window contains no instance of a 300 bps rate hike (or anything close), then:

    - No historical scenario produces the loss corresponding to a 300 bps shock.
    - The VaR estimate reflects only the range of rate moves actually observed (perhaps $\pm 50$ bps in a low-rate environment).
    - The tail of the empirical distribution is determined by the largest historical move, which may be far smaller than 300 bps.
    - The risk is **invisible** to historical simulation.

    This is the fundamental limitation: historical simulation cannot capture risks that have no precedent in the historical window.

    **Part 2: How a stress test addresses this.**

    A stress test directly specifies the 300 bps rate hike as a scenario and evaluates its impact, regardless of whether it has occurred in the data. The scenario is motivated by economic reasoning (e.g., a sudden inflation shock leading to emergency rate hikes) rather than historical frequency.

    **Part 3: Internally consistent stress scenario.**

    **Central narrative:** The central bank unexpectedly raises rates by 300 bps to combat a sudden inflation surge, triggered by a commodity supply shock.

    | Risk Factor | Stressed Move | Rationale |
    |---|---|---|
    | Short-term rates | +300 bps | Central bank emergency hike |
    | Long-term rates (10Y) | +150 bps | Term premium rises but less than short end (inverted curve) |
    | Equity indices | $-15\%$ | Higher discount rates and recession fears |
    | Credit spreads (IG) | +150 bps | Increased default risk from higher borrowing costs |
    | FX (domestic currency) | +5% appreciation | Higher rates attract capital inflows |
    | Volatility (VIX) | +20 points | Uncertainty about economic outlook and policy path |

    **Internal consistency logic:**

    - The **yield curve inverts** (short rates rise more than long rates) because the market expects the aggressive tightening to cause a recession, eventually requiring rate cuts. This is the classic pattern during surprise tightening cycles.
    - **Equities decline** because higher discount rates reduce present values and the recession risk depresses earnings expectations.
    - **Credit spreads widen** because higher rates increase debt service costs for corporates, raising default probability, and risk aversion increases.
    - **Domestic currency appreciates** because the rate differential attracts foreign capital (carry trade inflows). This is the textbook monetary policy transmission mechanism.
    - **Volatility spikes** because the unexpected nature of the shock creates uncertainty about the policy path and economic consequences.

    This scenario is internally consistent because all factor moves follow logically from the same triggering event (surprise rate hike), and the magnitudes are calibrated to be mutually compatible based on historical episodes (e.g., the Volcker tightening of 1980--1981, or the 2022 Fed tightening cycle).

---

**Exercise 6.** A bank uses historical simulation with a 250-day window for daily VaR reporting and also runs quarterly stress tests with scenarios calibrated to 2008-level severity. The historical simulation 99% VaR is \$50 million, while the stress test loss is \$350 million. Discuss the implications of this large gap. Should the bank's capital be sized to the VaR estimate or the stress test loss? Explain the regulatory formula

$$
\text{Total Risk Picture} = \text{Statistical Measures (VaR/ES)} + \text{Stress Test Results}
$$

and how each component contributes to the capital requirement.

??? success "Solution to Exercise 6"

    **Part 1: Implications of the large gap.**

    The historical simulation 99% VaR of \$50M reflects the risk under "normal" market conditions captured by the 250-day window. The stress test loss of \$350M reflects the potential impact of a 2008-level crisis---7 times larger than the daily VaR.

    This gap has several implications:

    1. **VaR is not a worst-case measure.** The 99% VaR says "on 99% of days, the loss will not exceed \$50M." It says nothing about how bad the remaining 1% of days can be. The stress test reveals that on the worst days, losses can be an order of magnitude larger.

    2. **Capital based on VaR alone is insufficient.** If the bank held capital equal to (say) 3x VaR = \$150M, it would still be far short of covering the \$350M stress loss.

    3. **Tail risk is real.** The distribution of losses has a very heavy tail, and the stress scenario is probing a region far beyond the VaR threshold.

    **Part 2: How capital should be sized.**

    Capital should NOT be sized to either measure alone. The regulatory and economic rationale is to use both:

    - **VaR/ES-based capital** covers day-to-day trading risk and typical adverse conditions. Under Basel III/FRTB, market risk capital is based on Expected Shortfall at 97.5% using a stressed calibration window.

    - **Stress test-based capital** covers severe but plausible tail events. The Stress Capital Buffer (SCB) directly links capital requirements to stress test outcomes.

    **Part 3: The "Total Risk Picture" formula.**

    $$
    \text{Total Risk Picture} = \text{Statistical Measures (VaR/ES)} + \text{Stress Test Results}
    $$

    Each component contributes to capital requirements:

    - **Statistical measures** provide the **floor** for capital, ensuring adequate capital under normal market conditions. They are quantitative, backtestable, and updated frequently (daily VaR reports).

    - **Stress test results** provide **additional capital** (buffers) to absorb severe losses. They capture risks that statistical measures miss: unprecedented events, correlation breakdowns, liquidity crises, and nonlinear effects.

    In the regulatory framework:

    $$
    \text{Total Capital} = \underbrace{\text{Pillar 1 capital}}_{\text{VaR/ES-based}} + \underbrace{\text{SCB} + \text{G-SIB surcharge} + \text{CCyB}}_{\text{Stress test and macroprudential}} + \underbrace{\text{Pillar 2 add-on}}_{\text{Supervisory judgment}}
    $$

    The bank should hold capital sufficient to survive the stress scenario (\$350M loss in this example) while maintaining minimum regulatory ratios. If the current capital is below this level, the bank must either raise capital, reduce risk, or adjust its business model.

---

**Exercise 7.** The Basel framework requires banks to compute a "Stressed VaR" using a 12-month period of significant stress. Explain the methodology: how is the stress period selected, and how is Stressed VaR different from simply applying historical simulation with all available data? If a bank selects the period September 2008 to August 2009, discuss what features of the market during that period would cause the Stressed VaR to be significantly higher than the current VaR computed over the most recent 250 days of relatively calm markets.

??? success "Solution to Exercise 7"

    **Part 1: Methodology of Stressed VaR.**

    Under Basel 2.5 (introduced in 2009), banks must compute a **Stressed VaR** in addition to the regular VaR. The methodology is:

    1. **Select a 12-month stress period:** The bank identifies a continuous 12-month period of significant financial stress that is relevant to the bank's current portfolio. The period should produce the highest VaR for the current portfolio.

    2. **Apply historical simulation using the stress period data:** Using the 250 trading days from the stress period, the bank applies the standard historical simulation methodology (revalue the current portfolio under each of the 250 daily return vectors from the stress period).

    3. **Compute VaR from the stressed returns:** The 99% VaR is estimated from the empirical distribution of P&L generated by the stress period returns.

    4. **Period selection criterion:** The stress period must be chosen such that the Stressed VaR is maximized for the bank's current portfolio. This means different banks may select different stress periods depending on their risk exposures.

    **How Stressed VaR differs from using all available data:**

    - **All available data** (e.g., 5--10 years) includes both calm and volatile periods. The VaR estimate blends these, potentially diluting the contribution of extreme periods.
    - **Stressed VaR** uses only data from a period of maximum stress, ensuring that the risk estimate reflects a severe environment. It is intentionally conservative.
    - **Regular VaR** (most recent 250 days) may use data from a currently calm market, producing a low risk estimate.

    The capital charge combines both:

    $$
    \text{Market Risk Capital} = \max(\text{VaR}_{t-1}, m_c \times \overline{\text{VaR}}_{60}) + \max(\text{SVaR}_{t-1}, m_s \times \overline{\text{SVaR}}_{60})
    $$

    where $m_c$ and $m_s$ are multipliers (minimum 3) and the bars denote 60-day averages.

    **Part 2: Features of Sep 2008 -- Aug 2009 that produce high Stressed VaR.**

    This period encompasses the peak of the Global Financial Crisis and would produce exceptionally high Stressed VaR for several reasons:

    1. **Extreme daily return magnitudes:** The S&P 500 experienced multiple daily moves exceeding $\pm 5\%$, including a single-day decline of 9% on October 15, 2008. Normal-period daily moves are typically under 1%. The larger historical returns translate directly into larger simulated P&L and thus higher VaR.

    2. **Elevated volatility:** The VIX peaked above 80 in October 2008, compared to typical levels of 15--20. Average daily volatility during this period was approximately 3--4x normal levels. Every historical return vector from this period is "scaled up" by the elevated volatility.

    3. **Correlation spikes:** During the crisis, asset correlations increased dramatically. Equity markets worldwide moved together, credit and equity became highly correlated, and the normal diversification benefits collapsed. A portfolio diversified across asset classes would show much larger simulated losses using crisis-period data because the returns are highly correlated.

    4. **Fat tails and extreme events:** The distribution of returns during this period was far more leptokurtic (fat-tailed) than during calm markets. The 1st and 99th percentiles of daily returns were much more extreme.

    5. **Liquidity premium:** Bid-ask spreads widened dramatically, and some markets experienced near-zero liquidity. Returns during this period embed a liquidity risk premium that is absent from calm-market data.

    6. **Credit spread explosions:** Investment-grade and high-yield spreads widened by hundreds of basis points, producing extreme losses for any portfolio with credit exposure. A bank using Sep 2008--Aug 2009 data would capture these extreme spread moves.

    All these features---higher volatility, higher correlations, fatter tails, liquidity dislocations---combine to produce a Stressed VaR that is typically **2--4 times larger** than the current VaR computed from recent calm data.
