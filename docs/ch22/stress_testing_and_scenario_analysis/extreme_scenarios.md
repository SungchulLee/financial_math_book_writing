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

??? success "Solution to Exercise 1"

    **Given:**

    - $\Delta_{\text{equity}} = 50$M per 1%, $\Delta_{\text{credit}} = -30$M per 100 bps
    - $\Gamma_{\text{equity,equity}} = 2$M per 1%$^2$
    - Scenario: $\Delta x_{\text{equity}} = -25\%$, $\Delta x_{\text{credit}} = +400$ bps

    **Step 1: Linear (delta) contribution.**

    $$
    -\Delta_{\text{equity}} \cdot \Delta x_{\text{equity}} = -50 \times (-25) = +1250 \text{ M (loss, since positive)}
    $$

    Wait---we must be careful with signs. The loss function is:

    $$
    L^{\text{stress}} \approx -\sum_i \Delta_i \cdot \Delta x_i - \frac{1}{2}\sum_{i,j}\Gamma_{ij} \cdot \Delta x_i \cdot \Delta x_j
    $$

    The equity delta is $\Delta_{\text{equity}} = 50$M per 1%, meaning the portfolio gains \$50M for each 1% increase in equities. A decline of 25% means $\Delta x_{\text{equity}} = -25$ (in units of 1%).

    $$
    -\Delta_{\text{equity}} \cdot \Delta x_{\text{equity}} = -(50)(-25) = +1250 \text{ M}
    $$

    For credit, $\Delta_{\text{credit}} = -30$M per 100 bps means the portfolio loses \$30M for each 100 bps widening. With $\Delta x_{\text{credit}} = +4$ (in units of 100 bps):

    $$
    -\Delta_{\text{credit}} \cdot \Delta x_{\text{credit}} = -(-30)(4) = +120 \text{ M}
    $$

    **Step 2: Quadratic (gamma) contribution.**

    $$
    -\frac{1}{2}\Gamma_{\text{equity,equity}} \cdot (\Delta x_{\text{equity}})^2 = -\frac{1}{2}(2)(625) = -625 \text{ M}
    $$

    The negative sign means the gamma effect actually **reduces** the loss. This makes sense if the portfolio has positive gamma (long options): the convexity benefit partially offsets losses from the large move.

    **Step 3: Total stress loss.**

    $$
    L^{\text{stress}} \approx 1250 + 120 - 625 = 745 \text{ M} = \$745 \text{ million}
    $$

    **Discussion of when the approximation fails:**

    The delta-gamma approximation fails significantly when:

    1. **Moves are very large:** For a 25% equity decline, third-order and higher terms (speed, etc.) become material. The quadratic approximation truncates the Taylor series after the second-order term.
    2. **Barrier options are present:** If the portfolio contains barrier options, the payoff is discontinuous and no smooth Taylor expansion is valid near the barrier level.
    3. **Volatility changes are ignored:** The formula above omits vega terms ($\mathcal{V}_i \cdot \Delta \sigma_i$). During a 25% equity crash, implied volatility would spike dramatically (VIX could increase 30--50 points), and ignoring this understates losses for short-volatility positions.
    4. **Cross-gamma terms are missing:** The formula only includes $\Gamma_{\text{equity,equity}}$ but not equity-credit cross-gamma, which could be significant for structured credit products.
    5. **The Greeks themselves change:** Delta and gamma are not constant over a 25% move---they depend on the current market level. For very large moves, the initial Greeks are poor approximations.

    For these reasons, **full revaluation** (re-pricing every position under the stressed market conditions) is strongly preferred for extreme scenarios.

---

**Exercise 2.** The Mahalanobis distance of a scenario $\mathbf{x}$ from the mean $\boldsymbol{\mu}$ under covariance $\boldsymbol{\Sigma}$ is

$$
D(\mathbf{x}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})}
$$

For a two-factor model with $\boldsymbol{\mu} = (0, 0)^\top$ and $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.6 \\ 0.6 & 1 \end{pmatrix}$, compute the Mahalanobis distance for the scenarios $\mathbf{x}_1 = (-3, -3)^\top$ and $\mathbf{x}_2 = (-3, 3)^\top$. Which scenario is more "extreme" in the Mahalanobis sense? Discuss which is more plausible during a flight-to-quality episode.

??? success "Solution to Exercise 2"

    **Step 1: Compute $\boldsymbol{\Sigma}^{-1}$.**

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.6 \\ 0.6 & 1 \end{pmatrix}
    $$

    The determinant is $\det(\boldsymbol{\Sigma}) = 1 - 0.36 = 0.64$.

    $$
    \boldsymbol{\Sigma}^{-1} = \frac{1}{0.64}\begin{pmatrix} 1 & -0.6 \\ -0.6 & 1 \end{pmatrix} = \begin{pmatrix} 1.5625 & -0.9375 \\ -0.9375 & 1.5625 \end{pmatrix}
    $$

    **Step 2: Compute $D(\mathbf{x}_1)$ for $\mathbf{x}_1 = (-3, -3)^\top$.**

    $$
    \mathbf{x}_1^\top \boldsymbol{\Sigma}^{-1} \mathbf{x}_1 = (-3, -3) \begin{pmatrix} 1.5625 & -0.9375 \\ -0.9375 & 1.5625 \end{pmatrix} \begin{pmatrix} -3 \\ -3 \end{pmatrix}
    $$

    First compute $\boldsymbol{\Sigma}^{-1} \mathbf{x}_1$:

    $$
    \begin{pmatrix} 1.5625(-3) + (-0.9375)(-3) \\ -0.9375(-3) + 1.5625(-3) \end{pmatrix} = \begin{pmatrix} -4.6875 + 2.8125 \\ 2.8125 - 4.6875 \end{pmatrix} = \begin{pmatrix} -1.875 \\ -1.875 \end{pmatrix}
    $$

    Then:

    $$
    \mathbf{x}_1^\top \boldsymbol{\Sigma}^{-1} \mathbf{x}_1 = (-3)(-1.875) + (-3)(-1.875) = 5.625 + 5.625 = 11.25
    $$

    $$
    D(\mathbf{x}_1) = \sqrt{11.25} \approx 3.354
    $$

    **Step 3: Compute $D(\mathbf{x}_2)$ for $\mathbf{x}_2 = (-3, 3)^\top$.**

    $$
    \boldsymbol{\Sigma}^{-1} \mathbf{x}_2 = \begin{pmatrix} 1.5625(-3) + (-0.9375)(3) \\ -0.9375(-3) + 1.5625(3) \end{pmatrix} = \begin{pmatrix} -4.6875 - 2.8125 \\ 2.8125 + 4.6875 \end{pmatrix} = \begin{pmatrix} -7.5 \\ 7.5 \end{pmatrix}
    $$

    $$
    \mathbf{x}_2^\top \boldsymbol{\Sigma}^{-1} \mathbf{x}_2 = (-3)(-7.5) + (3)(7.5) = 22.5 + 22.5 = 45
    $$

    $$
    D(\mathbf{x}_2) = \sqrt{45} \approx 6.708
    $$

    **Step 4: Comparison.**

    $D(\mathbf{x}_1) \approx 3.354$ and $D(\mathbf{x}_2) \approx 6.708$. Scenario $\mathbf{x}_2$ has a Mahalanobis distance roughly **twice** that of $\mathbf{x}_1$, making it far more extreme (less plausible) in the statistical sense.

    **Interpretation:** Since the two factors have a positive correlation of 0.6, the scenario $\mathbf{x}_1 = (-3, -3)$ where both factors decline together is **consistent** with the correlation structure and thus has a lower Mahalanobis distance. The scenario $\mathbf{x}_2 = (-3, 3)$ where one factor drops while the other rises moves **against** the correlation, requiring a much more unusual event.

    **Flight-to-quality context:** However, during a flight-to-quality episode (e.g., equities crash while government bonds rally), the scenario $\mathbf{x}_2$ is precisely what occurs in practice. If factor 1 represents equities and factor 2 represents government bond prices, then $\mathbf{x}_2 = (-3, 3)$ is the classic flight-to-quality pattern. The high Mahalanobis distance reflects that this scenario is extreme relative to the **normal-regime correlation**, but it becomes much more plausible under a **stressed correlation regime** where the equity-bond correlation flips from positive to negative. This illustrates a key limitation of using the normal-regime covariance matrix for plausibility assessment: correlation breakdown during crises renders normal-time Mahalanobis distances misleading.

---

**Exercise 3.** Explain the difference between first-round and second-round effects in stress testing. A bank holds \$10 billion in corporate bonds. Under a stress scenario, credit spreads widen by 300 bps, causing a mark-to-market loss of \$1.5 billion (first round). Describe a plausible chain of second-round effects and estimate qualitatively how they might amplify the total loss. Why are second-round effects particularly difficult to model?

??? success "Solution to Exercise 3"

    **First-round effects:**

    The bank holds \$10 billion in corporate bonds. Credit spreads widen by 300 bps, causing a mark-to-market loss of \$1.5 billion. This is the direct, immediate impact of the market move on the portfolio value.

    **Chain of second-round effects:**

    1. **Margin calls and collateral requirements:** The \$1.5B MTM loss triggers margin calls on derivative positions and reduces the value of bonds posted as collateral. The bank must either post additional cash or liquidate positions. If the bank must raise \$500M in additional margin, this strains liquidity.

    2. **Fire sale losses:** To meet margin calls and maintain liquidity ratios, the bank must sell assets. Selling \$2B of bonds into an already stressed market with wider bid-ask spreads (perhaps 3--5x normal) creates additional losses. If the fire sale discount is 2--3%, this adds \$40--60M in losses per billion sold, totaling an additional \$80--150M.

    3. **Funding cost increases:** The bank's own credit spread widens as the market perceives increased risk. If the bank has \$50B in wholesale funding and its spread increases by 50 bps, the annualized additional funding cost is \$250M. If some short-term funding providers refuse to roll over, the bank faces a funding gap.

    4. **Counterparty credit deterioration:** Other banks and corporates are also affected by the same credit stress. The bank's counterparty credit risk increases, requiring additional CVA reserves. Downgrades of counterparties may trigger additional margin requirements under CSAs.

    5. **Contagion and correlation spike:** The bank's actions (selling bonds, reducing credit lines) worsen the market environment for other institutions, who face similar pressures. This creates a feedback loop: fire sales depress prices further, triggering more margin calls, more fire sales, etc.

    6. **Reputational effects:** If the market perceives the bank as distressed, depositors and counterparties may withdraw, creating a run-like dynamic.

    **Qualitative total loss estimate:** Starting from the \$1.5B first-round loss, second-round effects could plausibly amplify the total loss to \$2.5--4B, representing a 70--170% amplification. In severe cases (2008 GFC), amplification factors of 2--3x or more were observed.

    **Why second-round effects are difficult to model:**

    - They involve **behavioral responses** (management decisions, counterparty actions) that are not deterministic.
    - They require modeling **market microstructure** (bid-ask spreads, market depth) under stress.
    - **Feedback loops** create nonlinear, path-dependent dynamics that simple factor models cannot capture.
    - They depend on the **network structure** of the financial system (who is connected to whom), which requires agent-based or network models.
    - **Timing** matters: the sequence of events affects outcomes, but most stress models apply instantaneous shocks.

---

**Exercise 4.** The stressed correlation blending formula is

$$
\boldsymbol{\rho}^{\text{stress}} = \alpha \boldsymbol{\rho}^{\text{normal}} + (1-\alpha) \mathbf{1}\mathbf{1}^\top
$$

Show that if $\boldsymbol{\rho}^{\text{normal}}$ is a valid correlation matrix with ones on the diagonal, then $\boldsymbol{\rho}^{\text{stress}}$ also has ones on the diagonal. For a 3-asset portfolio with pairwise normal correlations $\rho_{12} = 0.3$, $\rho_{13} = 0.4$, $\rho_{23} = 0.2$, compute $\boldsymbol{\rho}^{\text{stress}}$ with $\alpha = 0.3$. How does portfolio diversification benefit change between the normal and stressed cases?

??? success "Solution to Exercise 4"

    **Part 1: Diagonal property.**

    The $(i,i)$ entry of $\boldsymbol{\rho}^{\text{stress}}$ is:

    $$
    \rho_{ii}^{\text{stress}} = \alpha \rho_{ii}^{\text{normal}} + (1 - \alpha)[\mathbf{1}\mathbf{1}^\top]_{ii}
    $$

    Since $\boldsymbol{\rho}^{\text{normal}}$ is a correlation matrix, $\rho_{ii}^{\text{normal}} = 1$. Also, $[\mathbf{1}\mathbf{1}^\top]_{ii} = 1 \cdot 1 = 1$. Therefore:

    $$
    \rho_{ii}^{\text{stress}} = \alpha \cdot 1 + (1 - \alpha) \cdot 1 = 1
    $$

    So $\boldsymbol{\rho}^{\text{stress}}$ has ones on the diagonal. $\blacksquare$

    **Part 2: Compute $\boldsymbol{\rho}^{\text{stress}}$ with $\alpha = 0.3$.**

    The normal correlation matrix is:

    $$
    \boldsymbol{\rho}^{\text{normal}} = \begin{pmatrix} 1 & 0.3 & 0.4 \\ 0.3 & 1 & 0.2 \\ 0.4 & 0.2 & 1 \end{pmatrix}
    $$

    The matrix $\mathbf{1}\mathbf{1}^\top$ is the $3 \times 3$ matrix of all ones.

    $$
    \boldsymbol{\rho}^{\text{stress}} = 0.3 \begin{pmatrix} 1 & 0.3 & 0.4 \\ 0.3 & 1 & 0.2 \\ 0.4 & 0.2 & 1 \end{pmatrix} + 0.7 \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}
    $$

    Computing each off-diagonal entry:

    - $\rho_{12}^{\text{stress}} = 0.3 \times 0.3 + 0.7 \times 1 = 0.09 + 0.70 = 0.79$
    - $\rho_{13}^{\text{stress}} = 0.3 \times 0.4 + 0.7 \times 1 = 0.12 + 0.70 = 0.82$
    - $\rho_{23}^{\text{stress}} = 0.3 \times 0.2 + 0.7 \times 1 = 0.06 + 0.70 = 0.76$

    $$
    \boldsymbol{\rho}^{\text{stress}} = \begin{pmatrix} 1 & 0.79 & 0.82 \\ 0.79 & 1 & 0.76 \\ 0.82 & 0.76 & 1 \end{pmatrix}
    $$

    **Part 3: Diversification benefit comparison.**

    For an equally weighted portfolio of 3 assets with common volatility $\sigma$, the portfolio variance is:

    $$
    \sigma_p^2 = \frac{\sigma^2}{9}\left(3 + 6\bar{\rho}\right) = \frac{\sigma^2}{3}(1 + 2\bar{\rho})
    $$

    where $\bar{\rho}$ is the average pairwise correlation.

    **Normal regime:** $\bar{\rho} = (0.3 + 0.4 + 0.2)/3 = 0.3$

    $$
    \sigma_p^2 = \frac{\sigma^2}{3}(1 + 0.6) = \frac{1.6\sigma^2}{3} \approx 0.533\sigma^2
    $$

    **Stressed regime:** $\bar{\rho} = (0.79 + 0.82 + 0.76)/3 = 0.79$

    $$
    \sigma_p^2 = \frac{\sigma^2}{3}(1 + 1.58) = \frac{2.58\sigma^2}{3} \approx 0.86\sigma^2
    $$

    The diversification benefit can be measured as the reduction from undiversified variance ($\sigma^2$):

    - Normal: diversification reduces variance by $1 - 0.533 = 46.7\%$
    - Stressed: diversification reduces variance by only $1 - 0.86 = 14\%$

    The diversification benefit **collapses** from 47% to 14% under stress. In terms of volatility (standard deviation), the portfolio risk increases from $\sqrt{0.533}\sigma = 0.730\sigma$ to $\sqrt{0.86}\sigma = 0.927\sigma$, a 27% increase in portfolio volatility purely from the correlation increase, even without any change in individual asset volatilities.

---

**Exercise 5.** A risk manager must design a hypothetical stagflation scenario. Specify at least six risk factors (equities, rates, credit spreads, FX, commodities, volatility) and their stressed values. Ensure the scenario is internally consistent: explain the economic logic linking each factor move to the stagflation narrative. Why is stagflation particularly challenging for portfolios that use equities and bonds as diversifiers?

??? success "Solution to Exercise 5"

    **Stagflation scenario specification:**

    Stagflation combines high inflation with economic stagnation (low/negative growth and rising unemployment). This is challenging because the typical policy response to inflation (rate hikes) worsens the recession, and the typical response to recession (rate cuts, stimulus) worsens inflation.

    | Risk Factor | Stressed Value | Rationale |
    |-------------|---------------|-----------|
    | Equities (S&P 500) | $-30\%$ | Corporate earnings decline from rising input costs and falling demand; margin compression |
    | Interest rates (10Y Treasury) | $+200$ bps | Central bank tightens to combat inflation; inflation expectations push term premium higher |
    | Credit spreads (IG) | $+250$ bps | Rising defaults from higher borrowing costs and falling revenues; risk aversion |
    | FX (USD) | $-10\%$ (vs. major currencies) | Loss of confidence in monetary policy; capital outflows seeking real assets abroad |
    | Commodities (Oil) | $+60\%$ | Supply shock or sustained demand/supply imbalance driving the inflation; energy costs spike |
    | Volatility (VIX) | $+25$ points | Uncertainty about policy response and economic outlook; elevated risk premia |

    **Economic logic linking the factor moves:**

    1. **Oil and commodity surge** is the proximate cause of inflation, raising input costs across the economy.
    2. **Rising interest rates** follow from the central bank's attempt to anchor inflation expectations and from higher inflation compensation demanded by bond investors.
    3. **Equity decline** results from the dual pressure of rising discount rates (higher rates) and falling earnings (cost pressure plus weakening demand).
    4. **Credit spread widening** reflects higher default risk as firms face the double squeeze of rising costs and falling revenues, compounded by higher refinancing costs.
    5. **USD depreciation** reflects concern about the economy's inability to grow out of the inflationary episode, and capital seeking real assets (commodities, foreign equities in less-affected regions).
    6. **VIX increase** captures the elevated uncertainty inherent in a stagflationary environment where the policy toolkit is constrained.

    **Why stagflation is particularly challenging for equity-bond diversified portfolios:**

    The standard 60/40 equity-bond portfolio relies on **negative equity-bond correlation** during stress: when equities fall, bonds typically rally (flight to quality). This worked during the 2008 GFC, the 2020 COVID crash, and most recessions since the 1990s.

    In stagflation, this diversification **breaks down completely**:

    - **Equities fall** due to earnings pressure and higher discount rates.
    - **Bonds also fall** because rising inflation and rate hikes drive bond prices down.

    Both legs of the portfolio lose simultaneously. The equity-bond correlation flips from negative (typical in demand-driven recessions) to **positive** (characteristic of supply-driven inflation). This was observed in the 1970s stagflation episodes and partially in 2022.

    The result is that the "natural hedge" provided by bonds in a traditional portfolio vanishes, and total portfolio losses are much larger than either a pure equity crash or a pure rate shock would produce. Risk models calibrated to the post-1990 era, where negative equity-bond correlation was the norm, would dramatically underestimate portfolio losses in a stagflationary scenario.

---

**Exercise 6.** Consider the maximum loss direction problem

$$
\mathbf{x}^* = \arg\max_{\mathbf{x}} L(\mathbf{x}) \quad \text{s.t.} \quad D(\mathbf{x}) \le D_{\text{target}}
$$

For a portfolio with linear loss function $L(\mathbf{x}) = \mathbf{w}^\top \mathbf{x}$ and Mahalanobis distance constraint, show that the maximum loss scenario is $\mathbf{x}^* = -D_{\text{target}} \cdot \boldsymbol{\Sigma} \mathbf{w} / \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}$ (up to sign). Interpret this result: in which direction does the worst-case scenario point?

??? success "Solution to Exercise 6"

    **Goal:** Show that for a linear loss function $L(\mathbf{x}) = \mathbf{w}^\top \mathbf{x}$, the maximum loss scenario under the Mahalanobis distance constraint is:

    $$
    \mathbf{x}^* = -D_{\text{target}} \cdot \frac{\boldsymbol{\Sigma} \mathbf{w}}{\sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}}
    $$

    (assuming $\boldsymbol{\mu} = \mathbf{0}$ for simplicity, since we are looking for the scenario direction).

    **Step 1: Formulate the optimization problem.**

    $$
    \max_{\mathbf{x}} \; \mathbf{w}^\top \mathbf{x} \quad \text{s.t.} \quad \mathbf{x}^\top \boldsymbol{\Sigma}^{-1} \mathbf{x} \le D_{\text{target}}^2
    $$

    Note: $L(\mathbf{x}) = \mathbf{w}^\top \mathbf{x}$ represents the loss, so we maximize it. The constraint is that the Mahalanobis distance is at most $D_{\text{target}}$.

    **Step 2: Apply the Cauchy-Schwarz inequality.**

    Define $\mathbf{y} = \boldsymbol{\Sigma}^{-1/2} \mathbf{x}$, so $\mathbf{x} = \boldsymbol{\Sigma}^{1/2} \mathbf{y}$ and the constraint becomes $\|\mathbf{y}\|^2 \le D_{\text{target}}^2$. The objective becomes:

    $$
    \mathbf{w}^\top \boldsymbol{\Sigma}^{1/2} \mathbf{y}
    $$

    By Cauchy-Schwarz:

    $$
    \mathbf{w}^\top \boldsymbol{\Sigma}^{1/2} \mathbf{y} \le \|\boldsymbol{\Sigma}^{1/2} \mathbf{w}\| \cdot \|\mathbf{y}\| \le \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}} \cdot D_{\text{target}}
    $$

    Equality holds when $\mathbf{y} = D_{\text{target}} \cdot \boldsymbol{\Sigma}^{1/2}\mathbf{w} / \|\boldsymbol{\Sigma}^{1/2}\mathbf{w}\|$.

    **Step 3: Convert back to $\mathbf{x}$.**

    $$
    \mathbf{x}^* = \boldsymbol{\Sigma}^{1/2} \mathbf{y}^* = D_{\text{target}} \cdot \frac{\boldsymbol{\Sigma}^{1/2} \cdot \boldsymbol{\Sigma}^{1/2} \mathbf{w}}{\sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}} = D_{\text{target}} \cdot \frac{\boldsymbol{\Sigma} \mathbf{w}}{\sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}}
    $$

    This gives the maximum loss direction. If $\mathbf{w}$ represents the direction of portfolio loss (so larger $\mathbf{w}^\top\mathbf{x}$ is worse), then the worst-case scenario is in the direction of $\boldsymbol{\Sigma}\mathbf{w}$. If instead we want the scenario that causes the **largest negative P&L** (i.e., loss as a negative return), the sign flips to $-\boldsymbol{\Sigma}\mathbf{w}$.

    **Step 4: Alternatively, via Lagrangian.**

    The Lagrangian is:

    $$
    \mathcal{L} = \mathbf{w}^\top \mathbf{x} - \frac{\lambda}{2}(\mathbf{x}^\top \boldsymbol{\Sigma}^{-1}\mathbf{x} - D_{\text{target}}^2)
    $$

    First-order condition: $\mathbf{w} = \lambda \boldsymbol{\Sigma}^{-1}\mathbf{x}$, giving $\mathbf{x} = \frac{1}{\lambda}\boldsymbol{\Sigma}\mathbf{w}$.

    Substituting into the binding constraint $\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x} = D_{\text{target}}^2$:

    $$
    \frac{1}{\lambda^2}\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w} = D_{\text{target}}^2 \implies \lambda = \frac{\sqrt{\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}}}{D_{\text{target}}}
    $$

    Therefore $\mathbf{x}^* = D_{\text{target}} \cdot \boldsymbol{\Sigma}\mathbf{w} / \sqrt{\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}}$, confirming the result.

    **Interpretation:** The worst-case scenario points in the direction $\boldsymbol{\Sigma}\mathbf{w}$, not simply $\mathbf{w}$. The covariance matrix $\boldsymbol{\Sigma}$ rotates the sensitivity direction: factors that are both (a) highly sensitive in the portfolio and (b) highly volatile and correlated with other sensitive factors receive the largest shocks. A factor with low sensitivity but high correlation with a sensitive factor still receives a significant shock, because moving it "comes cheap" in Mahalanobis distance and helps push the correlated sensitive factor.

---

**Exercise 7.** Under the Fed CCAR severely adverse scenario, a bank projects losses of \$15 billion over 9 quarters against a starting CET1 capital of \$80 billion and RWA of \$600 billion. Compute the projected minimum CET1 ratio (ignoring any revenue offsets). If the regulatory minimum CET1 ratio including buffers is 7%, does the bank pass the stress test? Discuss why regulators prefer multi-quarter scenarios over instantaneous shocks.

??? success "Solution to Exercise 7"

    **Step 1: Compute the projected minimum CET1 capital.**

    Starting CET1 capital = \$80 billion. Total projected losses (ignoring revenue) = \$15 billion.

    $$
    K_{\min} = 80 - 15 = \$65 \text{ billion}
    $$

    **Step 2: Compute the minimum CET1 ratio.**

    Assuming RWA remains at \$600 billion (or using the starting RWA for simplicity since no RWA change is specified):

    $$
    \text{CET1 Ratio}_{\min} = \frac{65}{600} = 10.83\%
    $$

    **Step 3: Pass/fail determination.**

    The regulatory minimum CET1 ratio including buffers is 7.0%. Since:

    $$
    10.83\% > 7.0\%
    $$

    the bank **passes** the stress test with a comfortable margin of 3.83 percentage points above the minimum.

    **Step 4: Why regulators prefer multi-quarter scenarios over instantaneous shocks.**

    1. **Captures cumulative losses:** Credit losses (loan defaults, impairments) materialize over time as borrowers gradually deteriorate. An instantaneous shock misses the dynamic where an initial economic downturn leads to rising unemployment, which leads to consumer defaults, which leads to further economic weakness. The 9-quarter horizon allows this cascade to unfold.

    2. **Includes revenue offsets:** Over a multi-quarter horizon, banks earn PPNR (pre-provision net revenue) that partially offsets losses. This is economically realistic---banks do not simply absorb losses passively but continue to generate income. The net impact is more meaningful than gross instantaneous loss.

    3. **Models path-dependent effects:** Some risks are inherently time-dependent:
        - Credit migrations (investment grade to high yield to default) follow rating transition matrices over multiple quarters.
        - Trading book losses may compound as positions are marked down quarter by quarter.
        - Capital actions (dividends, buybacks) deplete capital over time.

    4. **Tests management response under sustained stress:** A 9-quarter scenario tests whether the bank can maintain capital adequacy through a prolonged downturn, not just survive a one-day shock. This is closer to how actual crises unfold (the 2008 GFC played out over 12--18 months).

    5. **Identifies the trough:** The minimum capital ratio may not occur at the end of the horizon. Losses may front-load (trading losses, immediate market moves) while PPNR gradually accumulates. The multi-quarter framework identifies the worst point in the trajectory, which is what matters for regulatory purposes.

    6. **Captures feedback effects:** Macroeconomic variables evolve over the scenario (GDP, unemployment, house prices follow specified paths), and these affect different loss components at different times, creating realistic lag structures that an instantaneous shock cannot capture.
