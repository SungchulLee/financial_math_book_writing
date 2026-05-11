# When Models Fail


## Introduction


Financial models fail when their assumptions diverge sufficiently from reality that their outputs become unreliable or misleading. Understanding the modes, causes, and warning signs of model failure is essential for robust risk management and for maintaining appropriate skepticism about quantitative tools.

This section examines:

1. **Historical case studies**: LTCM, the Gaussian copula crisis, flash crashes
2. **Failure taxonomies**: Classifying different types of model breakdown
3. **Early warning indicators**: Signs that a model may be failing
4. **Mitigation strategies**: Designing systems resilient to model failure

## Case Study: LTCM (1998)


### 1. Background


**Long-Term Capital Management**: Hedge fund founded in 1994 by John Meriwether with Nobel laureates Myron Scholes and Robert Merton.

**Strategy**: Convergence trades exploiting small mispricings:

- On-the-run vs. off-the-run Treasury bonds
- Interest rate swap spreads
- Equity volatility arbitrage

**Leverage**: Approximately 25:1 on-balance sheet; much higher including derivatives.

### 2. Model Assumptions


**Correlation Stability**: Historical correlations between spread trades assumed stable.

**Liquidity**: Ability to exit positions at reasonable prices assumed.

**Normal Distribution**: Extreme events modeled using Gaussian assumptions.

**Mean Reversion**: Spreads assumed to revert to historical averages.

### 3. What Went Wrong


**Russian Default** (August 1998): Sovereign default triggered global flight to quality.

**Correlation Breakdown**: Previously uncorrelated trades became highly correlated.

**Liquidity Evaporation**: Market makers withdrew; bid-ask spreads widened dramatically.

**Feedback Effects**: LTCM's forced liquidations moved markets against its positions.

### 4. Quantitative Analysis


**VaR Failure**: 10-day 99% VaR substantially underestimated actual losses.

**Correlation Assumption**: Pre-crisis correlation matrix:

$$
\rho_{ij}^{\text{normal}} \approx 0.2
$$

Crisis correlation:

$$
\rho_{ij}^{\text{crisis}} \approx 0.8
$$

**Loss Magnification**: With leverage $L$ and correlation increase $\Delta \rho$:

$$
\text{Loss Factor} \approx L \cdot \sqrt{1 + (n-1)\Delta \rho}
$$

### 5. Lessons


1. **Tail Risk**: Extreme events are more frequent and severe than Gaussian models predict
2. **Correlation Instability**: Correlations increase during stress
3. **Liquidity Risk**: Cannot separate market risk from liquidity risk
4. **Model Risk**: Sophisticated models create false confidence

## Case Study: Gaussian Copula and the Financial Crisis (2007-2009)


### 1. Background


**CDO Pricing**: Collateralized Debt Obligations required modeling joint default probabilities.

**Gaussian Copula** (Li, 2000): Elegant framework linking marginal default probabilities through correlation:

$$
\Phi_2^{-1}(P(D_1 \leq t_1, D_2 \leq t_2)) = N_2(\Phi^{-1}(P(D_1 \leq t_1)), \Phi^{-1}(P(D_2 \leq t_2)); \rho)
$$

### 2. Model Assumptions


**Constant Correlation**: Single parameter $\rho$ governs all pairwise default dependence.

**Normal Dependence**: Tail behavior follows bivariate normal copula.

**Stationarity**: Correlation structure assumed time-invariant.

**No Systemic Risk**: Model did not capture economy-wide factors.

### 3. What Went Wrong


**Underestimation of Joint Defaults**: Gaussian copula has **weak tail dependence**:

$$
\lambda_U = \lim_{u \to 1^-} P(U_2 > u | U_1 > u) = 0
$$

**Correlation Smile**: Market-implied correlations varied with tranche (base vs. senior), inconsistent with single-$\rho$ model.

**Systemic Exposure**: House prices correlated nationally; defaults clustered.

### 4. Quantitative Analysis


**Tranche Sensitivity**: For equity tranche, small $\Delta \rho$ causes large price change:

$$
\frac{\partial V_{\text{equity}}}{\partial \rho} \gg \frac{\partial V_{\text{senior}}}{\partial \rho}
$$

**Implied Correlation Skew**: Market prices implied:

$$
\rho_{\text{equity}} < \rho_{\text{mezzanine}} < \rho_{\text{senior}}
$$

Inconsistent with single-factor Gaussian copula.

### 5. Lessons


1. **Model Simplicity vs. Reality**: Single-parameter model too parsimonious
2. **Tail Dependence**: Gaussian copula inappropriate for extreme events
3. **Calibration Warnings**: Correlation smile was a warning sign
4. **Incentive Misalignment**: Model users had incentives to underestimate risk

## Flash Crashes


### 1. May 6, 2010 Flash Crash


**Event**: Dow Jones fell ~1000 points (9%) in minutes, then recovered.

**Trigger**: Large sell order in E-mini S&P 500 futures executed via algorithm.

**Amplification**: High-frequency traders withdrew liquidity; cascading stop-losses.

### 2. Model Failures


**Market Microstructure**: Standard price models assume continuous trading; flash crash showed discrete, discontinuous dynamics.

**Liquidity Models**: Assumed market depth stable; in reality, liquidity evaporated.

**Feedback Loops**: Algorithms interacted in unforeseen ways.

### 3. Implications


**Model Limitation**: Intraday risk models failed to anticipate extreme moves.

**Systemic Risk**: Interconnected algorithms create emergent risks.

**Circuit Breakers**: Regulatory response acknowledges model limitations.

## Taxonomy of Model Failures


### 1. Specification Error


**Definition**: Model structure does not match data generating process.

**Examples**:

- Assuming constant volatility when volatility is stochastic
- Using normal distribution when returns are fat-tailed
- Linear model for nonlinear relationship

**Detection**: Residual analysis, specification tests.

### 2. Estimation Error


**Definition**: Parameter estimates differ from true values due to finite data.

**Manifestation**:

- Confidence intervals too narrow
- Overfitting to noise
- Unstable parameters across samples

**Mitigation**: Regularization, Bayesian methods, ensemble approaches.

### 3. Regime Change


**Definition**: Parameters or structure change over time.

**Examples**:

- Volatility regimes (low vol vs. crisis)
- Correlation breakdown during stress
- Policy regime changes (central bank intervention)

**Detection**: Structural break tests, regime-switching models.

### 4. Tail Events


**Definition**: Events in the extreme tails of distributions.

**Challenge**: By definition, limited historical data on tail events.

**Approaches**: Extreme value theory, stress testing, scenario analysis.

### 5. Implementation Error


**Definition**: Correct model implemented incorrectly.

**Sources**:

- Coding errors
- Data errors
- Numerical instability
- Approximation errors

**Prevention**: Code review, unit testing, backtesting.

## Early Warning Indicators


### 1. Statistical Signals


**Residual Analysis**:

$$
\hat{\epsilon}_t = Y_t - \hat{Y}_t
$$

Warning signs:

- Autocorrelation in residuals
- Heteroskedasticity
- Non-normality

**Forecast Error Tracking**:

$$
\text{MAE}_t = \frac{1}{n} \sum_{s=t-n+1}^{t} |Y_s - \hat{Y}_{s|s-1}|
$$

Warning: Increasing MAE trend.

### 2. Market Signals


**Implied vs. Realized**: Large divergence between implied and realized volatility.

**Correlation Breakdown**: Rolling correlation deviates from model assumption.

**Liquidity Indicators**: Bid-ask spread widening, volume declining.

### 3. Calibration Signals


**Parameter Instability**: Large daily parameter swings.

**Calibration Error Increase**: Growing gap between model and market prices.

**Correlation Smile/Skew**: Inconsistent implied correlations across instruments.

### 4. Structural Indicators


**Leverage Buildup**: System-wide leverage increases.

**Crowded Trades**: Many participants in similar positions.

**Concentration**: Single entities dominating markets.

## Model Risk Management


### 1. Model Validation


**Independent Review**: Separate team validates model assumptions and implementation.

**Backtesting**: Compare model predictions to realized outcomes.

**Benchmarking**: Compare to alternative models.

### 2. Stress Testing


**Historical Scenarios**: Apply historical crisis periods to current portfolio.

**Hypothetical Scenarios**: Construct extreme but plausible scenarios.

**Reverse Stress Testing**: Find scenarios that would cause unacceptable losses.

### 3. Model Reserves


**Definition**: Additional capital held for model uncertainty.

**Calculation**:

$$
\text{Reserve} = V^{\text{worst-case}} - V^{\text{point estimate}}
$$

### 4. Model Governance


**Inventory**: Maintain catalog of all models in use.

**Tiering**: Classify models by materiality and complexity.

**Review Cycle**: Regular review and recalibration schedule.

**Change Control**: Formal process for model changes.

## Designing Robust Systems


### 1. Defense in Depth


**Multiple Models**: Use ensemble of models; no single point of failure.

**Diverse Approaches**: Combine statistical, economic, and judgment-based views.

**Conservative Assumptions**: Err on side of caution for critical applications.

### 2. Graceful Degradation


**Fallback Procedures**: Define actions when primary model fails.

**Human Override**: Enable human intervention when models malfunction.

**Circuit Breakers**: Automatic limits triggered by unusual model outputs.

### 3. Continuous Monitoring


**Real-Time Tracking**: Monitor model performance continuously.

**Alert Systems**: Automatic alerts for anomalies.

**Escalation Procedures**: Clear chain for addressing model issues.

### 4. Learning from Failures


**Post-Mortems**: Analyze model failures after the fact.

**Knowledge Sharing**: Disseminate lessons across organization.

**Model Improvement**: Use failures to improve future models.

## Summary


### Key Failure Modes


1. **Correlation breakdown**: Diversification fails during crises
2. **Tail events**: Extreme losses beyond model predictions
3. **Liquidity evaporation**: Inability to exit positions
4. **Regime changes**: Parameters shift, invalidating calibration
5. **Feedback effects**: Model usage affects market dynamics

### Best Practices


1. **Humility**: All models are wrong; some are useful
2. **Monitoring**: Continuous vigilance for warning signs
3. **Diversification**: Multiple models and approaches
4. **Stress Testing**: Regular exploration of extreme scenarios
5. **Governance**: Formal processes for model management

Understanding when and how models fail is as important as understanding how they work; robust risk management requires constant awareness of model limitations.

---

## Exercises

**Exercise 1.** The Gaussian VaR model assumes normally distributed returns. For a portfolio with daily returns that are actually $t$-distributed with 4 degrees of freedom, compute the 99% VaR under both the Gaussian and $t$-distribution assumptions. By what factor does the Gaussian model underestimate tail risk? Relate this to the concept of model misspecification.

??? success "Solution to Exercise 1"

    **Gaussian vs. Student-$t$ VaR and Model Misspecification**

    **Setup**

    Let daily returns $r_t$ have mean $\mu = 0$ and scale parameter $\sigma$. We compare the 99% VaR under two distributional assumptions:

    1. **Gaussian**: $r_t \sim N(0, \sigma^2)$
    2. **Student-$t$ with $\nu = 4$ degrees of freedom**: $r_t \sim t_4$, scaled to have the same variance.

    **Gaussian 99% VaR**

    The 99% VaR under normality is:

    $$
    \text{VaR}_{0.99}^{\text{Gauss}} = -\mu + z_{0.99} \cdot \sigma = z_{0.99} \cdot \sigma
    $$

    where $z_{0.99} = \Phi^{-1}(0.99) = 2.326$. So:

    $$
    \text{VaR}_{0.99}^{\text{Gauss}} = 2.326\,\sigma
    $$

    **Student-$t$ 99% VaR**

    For a Student-$t$ distribution with $\nu$ degrees of freedom, the variance is $\text{Var} = \nu/(\nu - 2)$ for $\nu > 2$. To match the Gaussian variance $\sigma^2$, we use a scaled $t$-distribution:

    $$
    r_t = \sigma \sqrt{\frac{\nu - 2}{\nu}} \cdot t_\nu
    $$

    For $\nu = 4$: the scaling factor is $\sigma\sqrt{2/4} = \sigma/\sqrt{2}$.

    The 99th percentile of the standard $t_4$ distribution is $t_{4, 0.99} = 3.747$. Therefore:

    $$
    \text{VaR}_{0.99}^{t_4} = \frac{\sigma}{\sqrt{2}} \cdot 3.747 = 2.650\,\sigma
    $$

    Wait --- let us be more careful. If we want $\text{Var}(r_t) = \sigma^2$ and $r_t = c \cdot t_\nu$, then $\text{Var}(r_t) = c^2 \cdot \nu/(\nu - 2) = \sigma^2$, so $c = \sigma\sqrt{(\nu-2)/\nu}$.

    For $\nu = 4$: $c = \sigma\sqrt{2/4} = \sigma/\sqrt{2}$.

    The 1st percentile (left tail) of the standard $t_4$ is $-t_{4,0.99} = -3.747$.

    $$
    \text{VaR}_{0.99}^{t_4} = -c \cdot (-3.747) = \frac{\sigma}{\sqrt{2}} \cdot 3.747 = 2.650\,\sigma
    $$

    **Underestimation Factor**

    $$
    \text{Ratio} = \frac{\text{VaR}_{0.99}^{t_4}}{\text{VaR}_{0.99}^{\text{Gauss}}} = \frac{2.650}{2.326} \approx 1.14
    $$

    At the 99% level, the Gaussian model underestimates VaR by approximately 14%.

    However, the underestimation becomes much more severe in the extreme tails. At the 99.9% level:

    - Gaussian: $z_{0.999} = 3.090$, so $\text{VaR}_{0.999}^{\text{Gauss}} = 3.090\,\sigma$.
    - $t_4$: $t_{4, 0.999} = 7.173$, so $\text{VaR}_{0.999}^{t_4} = \frac{\sigma}{\sqrt{2}} \cdot 7.173 = 5.072\,\sigma$.
    - Ratio: $5.072/3.090 \approx 1.64$. The Gaussian underestimates by 64%.

    At the 99.97% level (approximately a 3-year event):

    - Gaussian: $z_{0.9997} = 3.432$, so $\text{VaR} = 3.432\,\sigma$.
    - $t_4$: $t_{4, 0.9997} \approx 12.92$, so $\text{VaR} = \frac{\sigma}{\sqrt{2}} \cdot 12.92 = 9.14\,\sigma$.
    - Ratio: $9.14/3.43 \approx 2.67$. The Gaussian underestimates by a factor of nearly 3.

    **Connection to Model Misspecification**

    This example illustrates **specification error**: the model structure (Gaussian distribution) does not match the data-generating process ($t_4$ distribution). The key features of the misspecification are:

    1. **Tail underestimation grows with confidence level**: The Gaussian model becomes progressively worse in the tails. At the 99% level, the error is moderate; at the 99.97% level, it is catastrophic. This means the Gaussian VaR provides a misleading sense of safety precisely when extreme events occur.

    2. **Variance matching is insufficient**: Both distributions have the same mean and variance, so they are indistinguishable by first two moments. The difference lies in the fourth moment (kurtosis): the $t_4$ distribution has infinite kurtosis, while the Gaussian has kurtosis 3. VaR depends on tail behavior, not just variance.

    3. **Practical relevance**: Empirical stock return distributions typically have excess kurtosis between 5 and 50, consistent with $t$-distributions with 3--6 degrees of freedom. The Gaussian VaR systematically underestimates tail risk for real portfolios.

---

**Exercise 2.** Correlation breakdown during crises is one of the most common model failures. Using the DCC-GARCH framework, explain how conditional correlations between asset returns can spike from 0.3 to 0.9 during a market crash. Why does a constant-correlation model fail during such episodes, and what are the implications for portfolio diversification?

??? success "Solution to Exercise 2"

    **Correlation Breakdown via DCC-GARCH**

    **The DCC-GARCH Framework**

    The Dynamic Conditional Correlation (DCC) model of Engle (2002) separates the conditional covariance matrix $H_t$ into conditional volatilities and conditional correlations:

    $$
    H_t = D_t R_t D_t
    $$

    where $D_t = \text{diag}(\sigma_{1,t}, \ldots, \sigma_{n,t})$ contains conditional standard deviations (each following a GARCH process) and $R_t$ is the conditional correlation matrix.

    The DCC correlation dynamics are:

    $$
    Q_t = (1 - a - b)\bar{Q} + a \epsilon_{t-1}\epsilon_{t-1}^\top + b Q_{t-1}
    $$

    where $\epsilon_t = D_t^{-1} r_t$ are standardized residuals, $\bar{Q}$ is the unconditional correlation matrix of $\epsilon_t$, and $a, b > 0$ with $a + b < 1$. The conditional correlation is then:

    $$
    R_t = (\text{diag}(Q_t))^{-1/2} \, Q_t \, (\text{diag}(Q_t))^{-1/2}
    $$

    **How Correlations Spike During a Crash**

    During a market crash, returns are large and negative across assets. The standardized residuals $\epsilon_{i,t}$ are large and have the same sign (negative). The outer product $\epsilon_{t}\epsilon_{t}^\top$ has large positive off-diagonal entries:

    $$
    (\epsilon_t \epsilon_t^\top)_{ij} = \epsilon_{i,t} \cdot \epsilon_{j,t} > 0 \quad \text{(both negative, so product positive)}
    $$

    The DCC update incorporates this through the parameter $a$:

    $$
    Q_{t+1} = (1-a-b)\bar{Q} + a \cdot \underbrace{\epsilon_t \epsilon_t^\top}_{\text{large positive off-diag}} + b Q_t
    $$

    If the crash is severe (say $\epsilon_{i,t} = -4$ for all $i$), then $(\epsilon_t\epsilon_t^\top)_{ij} = 16$ for $i \neq j$, which is much larger than the typical value of $\bar{Q}_{ij}$ (close to the unconditional correlation). This drives $Q_{t+1}$ toward a matrix with very high off-diagonal entries, and hence $R_{t+1}$ has correlations close to 1.

    **Numerical Example**

    Suppose $\bar{Q}_{12} = 0.3$ (unconditional correlation), $a = 0.05$, $b = 0.93$. In normal times, $Q_{12,t} \approx 0.3$, and $R_{12,t} \approx 0.3$.

    After a crash day with $\epsilon_{1,t} = \epsilon_{2,t} = -4$:

    $$
    Q_{12,t+1} = (1 - 0.05 - 0.93)(0.3) + 0.05(16) + 0.93(0.3) = 0.006 + 0.8 + 0.279 = 1.085
    $$

    The diagonal entries also increase: $Q_{11,t+1} = 0.02 + 0.05(16) + 0.93(1.0) = 0.02 + 0.8 + 0.93 = 1.75$. Similarly $Q_{22,t+1} = 1.75$.

    Therefore:

    $$
    R_{12,t+1} = \frac{Q_{12,t+1}}{\sqrt{Q_{11,t+1} Q_{22,t+1}}} = \frac{1.085}{\sqrt{1.75 \times 1.75}} = \frac{1.085}{1.75} \approx 0.62
    $$

    After a second crash day of similar magnitude, the correlation would increase further toward 0.8--0.9. The persistence parameter $b = 0.93$ means elevated correlations decay slowly.

    **Why Constant-Correlation Models Fail**

    A constant-correlation model assumes $R_t = \bar{R}$ for all $t$. This means:

    1. **Portfolio risk is underestimated during crises**: If the true correlation is 0.9 during a crash but the model uses 0.3, the portfolio variance is:

        $$
        \sigma_P^2(\rho = 0.3) = \sigma^2(1 + (n-1) \times 0.3) \quad \text{vs.} \quad \sigma_P^2(\rho = 0.9) = \sigma^2(1 + (n-1) \times 0.9)
        $$

        For $n = 10$ assets: ratio is $(1 + 8.1)/(1 + 2.7) = 9.1/3.7 \approx 2.46$, so portfolio standard deviation is underestimated by a factor of $\sqrt{2.46} \approx 1.57$.

    2. **Diversification benefit is overstated**: Portfolios constructed for diversification (low correlation) lose their hedging benefit precisely when it matters most. The constant-correlation model fails to warn that diversification evaporates during crises.

    3. **VaR underestimation**: Combining volatility spikes with correlation spikes, the actual portfolio VaR during a crisis can be 3--5 times the model VaR.

    **Implications**: Risk models should use either DCC-GARCH (dynamic correlations) or, at minimum, stress-tested correlation matrices that reflect crisis-period correlations. Any risk assessment should include a scenario with correlations at crisis levels.

---

**Exercise 3.** Design a set of five early warning indicators that signal potential model failure. For each indicator, specify: (a) what data is needed, (b) what threshold triggers a warning, and (c) what remedial action should be taken. Consider indicators based on backtesting violations, parameter instability, residual analysis, liquidity measures, and market regime detection.

??? success "Solution to Exercise 3"

    **Five Early Warning Indicators for Model Failure**

    **Indicator 1: Backtesting Violation Rate**

    *(a) Data needed*: Daily P&L realizations and corresponding model VaR predictions at the chosen confidence level (e.g., 99%).

    *(b) Threshold*: At 99% VaR, expect approximately 2.5 violations per year (1% of 250 trading days). Use the Kupiec test: if the number of violations in any rolling 250-day window exceeds 7 (traffic light red zone under Basel), or if a cluster of 3+ violations occurs within 10 days, trigger the warning.

    Formally, under the null hypothesis that the model is correct, the number of violations $x$ in $n$ days follows $\text{Binomial}(n, 0.01)$. Reject if:

    $$
    \text{LR}_{\text{Kupiec}} = -2\ln\left(\frac{(1-p_0)^{n-x} p_0^x}{(1-\hat{p})^{n-x} \hat{p}^x}\right) > \chi^2_{1, 0.05} = 3.84
    $$

    where $p_0 = 0.01$ and $\hat{p} = x/n$.

    *(c) Remedial action*: Investigate whether violations are due to (i) extreme market moves (tail event), (ii) model miscalibration, or (iii) data errors. If (i), stress-test the model under current conditions. If (ii), recalibrate with recent data. If (iii), fix data pipeline.

    **Indicator 2: Parameter Instability**

    *(a) Data needed*: Daily recalibrated model parameters (e.g., volatility, correlation, mean reversion speed) over a rolling window.

    *(b) Threshold*: Compute the coefficient of variation of each parameter over a 20-day rolling window. Trigger warning if any key parameter's CV exceeds 0.25 (25% relative variation), or if a parameter moves by more than 3 standard deviations of its own historical variation in a single day.

    *(c) Remedial action*: Investigate whether the instability reflects genuine market regime change or numerical calibration issues. If the former, consider switching to a regime-switching model or widening the calibration window. If the latter, investigate the calibration algorithm's convergence.

    **Indicator 3: Residual Analysis (Autocorrelation and Heteroskedasticity)**

    *(a) Data needed*: Model residuals $\hat{\epsilon}_t = r_t - \hat{r}_t$ (realized returns minus model-predicted returns).

    *(b) Threshold*: Apply the Ljung-Box test for autocorrelation in residuals and squared residuals. Trigger warning if:

    - Ljung-Box $Q$-statistic for residuals at lag 10 exceeds the 5% critical value ($\chi^2_{10, 0.05} = 18.31$), indicating predictable pattern in errors.
    - Ljung-Box for squared residuals is significant, indicating the model misses volatility clustering (ARCH effects).
    - Jarque-Bera test rejects normality of residuals at 1% level, indicating distributional misspecification.

    *(c) Remedial action*: Autocorrelated residuals suggest the model is missing a systematic factor. Add lagged returns or regime variables. ARCH in squared residuals suggests the volatility model is inadequate; consider switching to GARCH or stochastic volatility. Non-normality suggests fat-tailed distribution or jumps are needed.

    **Indicator 4: Liquidity Deterioration**

    *(a) Data needed*: Bid-ask spreads, market depth (volume at best bid/offer), daily trading volume, and Amihud illiquidity ratio $\text{ILLIQ}_t = |r_t| / \text{Volume}_t$.

    *(b) Threshold*: Trigger warning if:

    - Bid-ask spread exceeds twice its 60-day moving average for 3 consecutive days.
    - Market depth falls below 50% of its 60-day average.
    - Amihud illiquidity ratio exceeds its 95th historical percentile.

    *(c) Remedial action*: Re-evaluate all model assumptions about exit costs. Adjust position limits to reflect reduced ability to unwind. Apply liquidity-adjusted VaR (LVaR) that adds the cost of liquidation at stressed bid-ask spreads. Consider reducing positions in the most illiquid instruments.

    **Indicator 5: Regime Detection via Hidden Markov Model**

    *(a) Data needed*: Daily returns, realized volatility (e.g., from high-frequency data), and cross-asset correlation estimates.

    *(b) Threshold*: Fit a two-state hidden Markov model to recent data. Trigger warning if the filtered probability of being in the "crisis" regime exceeds 0.5:

    $$
    \mathbb{P}(S_t = \text{crisis} | r_1, \ldots, r_t) > 0.5
    $$

    Also trigger if the volatility ratio $\hat{\sigma}_t / \bar{\sigma} > 2$ (current volatility more than double the long-run average).

    *(c) Remedial action*: Switch from normal-regime model parameters to crisis-regime parameters. Increase capital buffers and reduce leverage. Activate stress-testing protocols and increase reporting frequency to senior management.

---

**Exercise 4.** The "Lucas critique" states that economic relationships change when policy changes. Apply this critique to financial models: explain how the widespread adoption of delta-hedging strategies can alter the volatility dynamics that the hedging model assumes. This is an example of a feedback effect where model usage affects market dynamics.

??? success "Solution to Exercise 4"

    **The Lucas Critique Applied to Delta Hedging and Market Dynamics**

    **The Lucas Critique in Economics**

    The Lucas critique (1976) states that the parameters of econometric models are not invariant to changes in economic policy. When policy changes, agents' behavior changes, altering the statistical relationships the model was estimated from. Applying this to finance: when a financial model becomes widely adopted and used for trading, the trading activity itself changes the market dynamics that the model assumes.

    **Delta Hedging as a Feedback Mechanism**

    Consider a market where many participants delta-hedge option portfolios using the Black-Scholes model. The Black-Scholes delta for a call option is:

    $$
    \Delta = \mathcal{N}(d_1), \quad d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)\tau}{\sigma\sqrt{\tau}}
    $$

    When $S$ increases, $\Delta$ increases (for calls), so hedgers buy more stock. When $S$ decreases, $\Delta$ decreases, so hedgers sell stock. This creates a **positive feedback loop**:

    1. Stock price rises $\to$ delta hedgers buy stock $\to$ price rises further.
    2. Stock price falls $\to$ delta hedgers sell stock $\to$ price falls further.

    **Impact on Volatility Dynamics**

    The Black-Scholes model assumes constant volatility $\sigma$. But the hedging-induced feedback changes the effective volatility. The aggregate hedging demand from options is:

    $$
    \text{Hedge demand} = \sum_{\text{options}} n_i \cdot \Gamma_i \cdot \Delta S
    $$

    where $n_i$ is the position size and $\Gamma_i = \partial \Delta_i / \partial S$ is the option's gamma. This hedging demand adds to natural supply/demand, amplifying price moves.

    The effective volatility becomes:

    $$
    \sigma_{\text{effective}}^2 \approx \sigma_{\text{fundamental}}^2 \cdot \left(\frac{1}{1 - \lambda \cdot \text{Net Gamma}}\right)^2
    $$

    where $\lambda$ captures the market's price sensitivity to order flow, and Net Gamma is the aggregate gamma of all hedged option positions (positive if market makers are long gamma, negative if short gamma).

    **When Market Makers Are Short Gamma**

    If options market makers have sold options to clients (common scenario: clients buy puts for protection), the market makers are **short gamma**. Their hedging activity amplifies price moves:

    - Price falls $\to$ market makers must sell (delta decreases) $\to$ more selling pressure $\to$ price falls further.
    - This creates a volatility amplification effect, making realized volatility higher than the fundamental volatility.

    **When Market Makers Are Long Gamma**

    If market makers are long gamma (e.g., around large option expiration dates with concentrated strikes), their hedging dampens price moves:

    - Price rises $\to$ market makers sell (delta increases past their position) $\to$ selling pressure offsets the rise.
    - This creates a volatility suppression effect ("gamma pinning" near option strikes at expiration).

    **The Lucas Critique Implication**

    The Black-Scholes model was estimated and calibrated under conditions where delta hedging was not widespread. As delta hedging became universal (post-1980s), the volatility dynamics changed:

    1. **Volatility is no longer exogenous**: It depends on the distribution of option positions and hedging activity, which depends on the model itself. The model's assumption of constant, exogenous volatility is invalidated by its own use.

    2. **Smile and skew emergence**: The asymmetric impact of hedging (short gamma from put selling) contributes to the volatility skew. After 1987, the widespread purchase of protective puts and the resulting short gamma exposure of market makers became a structural feature that the original Black-Scholes model cannot explain.

    3. **Flash crash amplification**: In May 2010, automated delta-hedging and related strategies amplified the crash, precisely because the models assumed stable liquidity and continuous price paths. The models' own usage created the discontinuity they assumed away.

    4. **Endogenous regime changes**: Concentrated option expiration dates create predictable changes in market dynamics (gamma exposure shifts), which a model calibrated to historical data would not capture if it treats volatility as exogenous.

    **Practical Consequence**: Any model used for trading must account for the possibility that its widespread adoption changes the dynamics it models. This motivates scenario analysis that includes "what if everyone hedges the same way?" and stress tests for crowded-trade unwinding.

---

**Exercise 5.** Liquidity risk is notoriously difficult to model. Describe a scenario where a position appears low-risk under mark-to-market valuation but becomes extremely costly to unwind during a liquidity crisis. How should models incorporate the distinction between mark-to-market risk and liquidation risk?

??? success "Solution to Exercise 5"

    **Liquidity Risk: Mark-to-Market vs. Liquidation Risk**

    **Scenario Construction**

    Consider a fixed-income portfolio holding \$500 million in corporate bonds with the following characteristics:

    - Credit quality: BBB-rated, 5-year maturity.
    - Normal bid-ask spread: 10 basis points (0.10%).
    - Mark-to-market (mid-price) value: \$500 million.
    - Duration: 4.5 years.
    - The position represents 15% of the average daily trading volume in these specific bonds.

    Under normal conditions, the mark-to-market risk is moderate: a 50 bps parallel shift in credit spreads would cause a loss of approximately $500M \times 4.5 \times 0.005 = \$11.25M$.

    **The Liquidity Crisis Scenario**

    A credit market stress event occurs (e.g., similar to March 2020 COVID dislocation or March 2008 Bear Stearns crisis):

    1. **Bid-ask spreads widen**: From 10 bps to 200--500 bps. The cost of executing a trade increases by 20--50x.

    2. **Market depth evaporates**: Average daily volume drops by 70%. The position now represents 50% of daily volume, making it impossible to exit in a single day without severe price impact.

    3. **Price impact**: Attempting to sell a large fraction of the position would move the market further. A reasonable estimate of price impact for selling 10% of daily volume is 25--50 bps; for 50% of daily volume, the impact could be 200+ bps.

    4. **Mark-to-market value may appear stable**: If bid-ask spreads widen symmetrically, the mid-price may not move much. The mark-to-market P&L would show modest losses, but the actual cost of unwinding the position is enormous.

    **Quantifying the Divergence**

    *Mark-to-market loss* (if credit spreads widen by 100 bps):

    $$
    \text{MtM Loss} = 500M \times 4.5 \times 0.01 = \$22.5M
    $$

    *Liquidation cost* (selling the entire position over 5 days):

    - Bid-ask cost: $500M \times 0.03$ (300 bps mid-to-bid in stress) $= \$15M$
    - Price impact: Selling \$100M/day when daily volume is \$200M. Estimated impact of 100 bps per day, cumulative (each day's selling depresses prices further): total impact $\approx 500M \times 4.5 \times (0.01 + 0.02 + 0.03 + 0.04 + 0.05)/5 = 500M \times 4.5 \times 0.03 = \$67.5M$ (rough estimate).
    - Total liquidation cost: $\$15M + \$67.5M = \$82.5M$

    The total loss upon liquidation is $\$22.5M + \$82.5M = \$105M$, approximately 4.7 times the mark-to-market loss alone.

    **How Models Should Incorporate Liquidation Risk**

    1. **Liquidity-adjusted VaR (LVaR)**:

        $$
        \text{LVaR} = \text{VaR} + \text{Liquidation Cost Adjustment}
        $$

        where the adjustment accounts for bid-ask spread at stressed levels and the price impact of unwinding:

        $$
        \text{LCA} = \frac{1}{2} \cdot \text{Position Size} \cdot s_{\text{stressed}} + f(\text{Position Size}, \text{ADV})
        $$

        Here $s_{\text{stressed}}$ is the stressed bid-ask spread and $f$ is a price impact function that depends on the ratio of position size to average daily volume (ADV).

    2. **Holding period adjustment**: Instead of the standard 10-day VaR horizon, use a liquidity-adjusted horizon:

        $$
        T_{\text{liq}} = \frac{\text{Position Size}}{\text{ADV}_{\text{stressed}} \times \text{participation rate}}
        $$

        For our example: $T_{\text{liq}} = 500M / (200M \times 0.20) = 12.5$ days (assuming 20% participation rate), and scale VaR accordingly.

    3. **Concentration limits**: Independent of VaR, impose limits based on the ratio of position size to ADV. A common rule is that no single position should exceed 1--3 days of average volume, so that it can be unwound within a reasonable period even under stressed conditions.

    4. **Stress testing**: Include scenarios where liquidity dries up simultaneously with adverse price moves (as typically happens in practice). The correlation between market risk and liquidity risk is positive during crises, and models must capture this joint behavior.

---

**Exercise 6.** Regime-switching models attempt to capture structural breaks in financial time series. For a two-regime model with $\mu_1 = 0.10$, $\sigma_1 = 0.15$ (normal regime) and $\mu_2 = -0.20$, $\sigma_2 = 0.40$ (crisis regime), with transition probabilities $p_{12} = 0.02$ and $p_{21} = 0.10$, compute the stationary distribution over regimes and the unconditional mean and variance of returns. How does this model improve upon a single-regime model for risk management?

??? success "Solution to Exercise 6"

    **Regime-Switching Model: Stationary Distribution and Unconditional Moments**

    **Model Specification**

    Two regimes with parameters:

    - Regime 1 (Normal): $\mu_1 = 0.10$, $\sigma_1 = 0.15$
    - Regime 2 (Crisis): $\mu_2 = -0.20$, $\sigma_2 = 0.40$

    Transition probabilities (per period):

    - $p_{12} = P(\text{Crisis}_{t+1} | \text{Normal}_t) = 0.02$
    - $p_{21} = P(\text{Normal}_{t+1} | \text{Crisis}_t) = 0.10$

    So $p_{11} = 1 - p_{12} = 0.98$ and $p_{22} = 1 - p_{21} = 0.90$.

    **Stationary Distribution**

    The stationary distribution $(\pi_1, \pi_2)$ satisfies $\pi P = \pi$ with $\pi_1 + \pi_2 = 1$:

    $$
    \pi_1 = \pi_1 p_{11} + \pi_2 p_{21}
    $$

    $$
    \pi_1 = \pi_1(1 - p_{12}) + \pi_2 p_{21}
    $$

    $$
    \pi_1 p_{12} = \pi_2 p_{21}
    $$

    $$
    \frac{\pi_1}{\pi_2} = \frac{p_{21}}{p_{12}} = \frac{0.10}{0.02} = 5
    $$

    Therefore:

    $$
    \pi_1 = \frac{p_{21}}{p_{12} + p_{21}} = \frac{0.10}{0.02 + 0.10} = \frac{0.10}{0.12} = \frac{5}{6} \approx 0.8333
    $$

    $$
    \pi_2 = \frac{p_{12}}{p_{12} + p_{21}} = \frac{0.02}{0.12} = \frac{1}{6} \approx 0.1667
    $$

    The economy spends approximately 83.3% of the time in the normal regime and 16.7% in the crisis regime. The expected duration of each regime is: normal regime $= 1/p_{12} = 50$ periods, crisis regime $= 1/p_{21} = 10$ periods.

    **Unconditional Mean**

    $$
    \bar{\mu} = \pi_1 \mu_1 + \pi_2 \mu_2 = \frac{5}{6}(0.10) + \frac{1}{6}(-0.20)
    $$

    $$
    \bar{\mu} = \frac{0.50 - 0.20}{6} = \frac{0.30}{6} = 0.05
    $$

    The unconditional expected return is 5%.

    **Unconditional Variance**

    Using the law of total variance:

    $$
    \text{Var}(r) = \mathbb{E}[\text{Var}(r | S)] + \text{Var}(\mathbb{E}[r | S])
    $$

    where $S$ denotes the regime.

    First term (average within-regime variance):

    $$
    \mathbb{E}[\text{Var}(r | S)] = \pi_1 \sigma_1^2 + \pi_2 \sigma_2^2 = \frac{5}{6}(0.0225) + \frac{1}{6}(0.16)
    $$

    $$
    = \frac{5}{6}(0.0225) + \frac{1}{6}(0.16) = 0.01875 + 0.02667 = 0.04542
    $$

    Second term (variance of regime means):

    $$
    \text{Var}(\mathbb{E}[r|S]) = \pi_1(\mu_1 - \bar{\mu})^2 + \pi_2(\mu_2 - \bar{\mu})^2
    $$

    $$
    = \frac{5}{6}(0.10 - 0.05)^2 + \frac{1}{6}(-0.20 - 0.05)^2
    $$

    $$
    = \frac{5}{6}(0.0025) + \frac{1}{6}(0.0625)
    $$

    $$
    = 0.002083 + 0.010417 = 0.012500
    $$

    Total unconditional variance:

    $$
    \text{Var}(r) = 0.04542 + 0.01250 = 0.05792
    $$

    Unconditional standard deviation:

    $$
    \sigma_{\text{unconditional}} = \sqrt{0.05792} \approx 0.2407 = 24.07\%
    $$

    **Comparison to a Single-Regime Model**

    A single-regime model calibrated to the same data would estimate $\hat{\mu} = 0.05$ and $\hat{\sigma} = 0.2407$. However, the risk profile is very different:

    | Metric | Single-Regime | Regime-Switching |
    |--------|--------------|-----------------|
    | $\mathbb{E}[r]$ | 0.05 | 0.05 (same) |
    | $\sigma$ | 0.2407 | 0.2407 (same unconditionally) |
    | 99% VaR (Gaussian) | $2.326 \times 0.2407 = 0.560$ | Depends on current regime |
    | Kurtosis | 3.0 (Gaussian) | $> 3$ (fat tails from mixture) |
    | Conditional on Normal | $\mu = 0.05$, $\sigma = 0.24$ | $\mu = 0.10$, $\sigma = 0.15$ |
    | Conditional on Crisis | $\mu = 0.05$, $\sigma = 0.24$ | $\mu = -0.20$, $\sigma = 0.40$ |

    **Improvements for Risk Management**

    1. **Conditional risk assessment**: In the normal regime, the regime-switching model reports lower risk ($\sigma_1 = 0.15$) than the single-regime model ($\sigma = 0.24$). In the crisis regime, it reports much higher risk ($\sigma_2 = 0.40$). This allows risk managers to adjust position sizes and hedging strategies based on the current regime.

    2. **Fat tails**: The mixture of two normals produces fat tails (excess kurtosis). The unconditional kurtosis is:

        $$
        \text{Kurt}(r) = \frac{\pi_1(\sigma_1^4 + 6\sigma_1^2(\mu_1 - \bar{\mu})^2 + 3(\mu_1 - \bar{\mu})^4) + \pi_2(\cdots)}{(\text{Var}(r))^2} \cdot 3
        $$

        This exceeds 3, meaning the model generates heavier tails than the Gaussian, better capturing the frequency of extreme returns.

    3. **VaR conditional on regime**: In the crisis regime, 99% VaR is $0.20 + 2.326 \times 0.40 = 1.13$ (113% loss), compared to the single-regime VaR of 56%. This is a much more realistic assessment of risk during a crisis.

    4. **Early warning**: The filtered regime probability $\pi_2(t | \text{data})$ serves as an early warning indicator. As $\pi_2(t)$ rises above 0.5, risk managers can proactively reduce exposure before the full crisis materializes.

    5. **Transition risk**: The model explicitly quantifies the probability of transitioning from normal to crisis ($p_{12} = 0.02$ per period), which a single-regime model cannot. This allows computation of the probability of entering a crisis within any given horizon.
