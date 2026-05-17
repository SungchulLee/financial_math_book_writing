# Model Validation

**Model validation** ensures that risk models are conceptually sound, correctly implemented, and appropriate for their intended purpose. It is a cornerstone of model risk management.

---

## Objectives of Model Validation

### Core Goals

1. **Conceptual soundness:** Is the model theoretically appropriate?
2. **Implementation correctness:** Is the code bug-free?
3. **Fitness for purpose:** Does it work for intended use cases?
4. **Ongoing performance:** Does it continue to perform adequately?

### Independence Principle

Validation should be performed by parties **independent** of model development:

- Separate team
- Different reporting line
- No conflicts of interest

---

## Components of Validation

### 1. Conceptual Review

Assess model theory and assumptions:

- Mathematical foundations
- Economic rationale
- Key assumptions and limitations
- Comparison to alternative approaches

**Questions:**

- Does the model capture relevant risk drivers?
- Are assumptions realistic?
- What is the model's domain of validity?

### 2. Data Quality Assessment

Evaluate inputs:

- Data sources and reliability
- Time series length and stationarity
- Missing data treatment
- Outlier handling
- Representativeness of historical period

### 3. Implementation Testing

Verify correct implementation:

- Unit tests for components
- Benchmark against analytical solutions
- Cross-validation with alternative implementations
- Sensitivity analysis

### 4. Outcome Analysis

Compare predictions to realized outcomes:

- Backtesting
- Out-of-sample performance
- Stress scenario validation

---

## Regulatory Guidance

Recall (see [§ Model Validation Standards (SR 11-7)](regulatory_requirements_basel.md#model-validation-standards-sr-11-7)) the SR 11-7 definition of model risk and the Basel internal-model approval requirements (use test, backtesting, supervisory approval).

---

## Validation Techniques

### Benchmarking

Compare model to:

- Industry standard models
- Vendor models
- Simpler alternative approaches

**Purpose:** Identify model-specific risks and validate reasonableness.

### Sensitivity Analysis

Test model response to input changes:

$$
\frac{\partial \text{Output}}{\partial \text{Input}_i} \quad \text{for all key inputs}
$$

**Identify:**

- Key drivers
- Unstable regions
- Nonlinearities

### Scenario Analysis

Apply hypothetical scenarios:

- Historical stress periods
- Hypothetical extremes
- Edge cases

**Assess:** Model behavior under conditions outside calibration range.

### Statistical Testing

Formal hypothesis tests:

- Parameter significance
- Residual diagnostics
- Stability tests (structural breaks)

---

## Documentation Requirements

### Model Documentation

Every model should have:

- **Theory:** Mathematical formulation and assumptions
- **Implementation:** Technical specification
- **Calibration:** Data and methodology
- **Limitations:** Known weaknesses and use restrictions
- **Version history:** Changes and rationale

### Validation Documentation

Validation reports should include:

- Scope and objectives
- Methodology
- Findings and issues
- Recommendations
- Ratings/conclusions

---

## Model Risk Rating

### Traffic Light System

| Rating | Meaning | Action |
|--------|---------|--------|
| **Green** | Model performs well | Continue use |
| **Yellow** | Issues identified | Use with restrictions; remediation needed |
| **Red** | Serious problems | Restrict/suspend use |

### Quantitative Scoring

Score models on:

- Conceptual soundness (1-5)
- Implementation quality (1-5)
- Performance (1-5)
- Documentation (1-5)

Overall rating = weighted average.

---

## Ongoing Validation

### Periodic Review

Models require regular revalidation:

- Annual review (minimum)
- More frequent for high-risk models
- Triggered reviews after significant changes

### Change Management

When models change:

1. Document change rationale
2. Assess impact
3. Re-validate affected components
4. Approve before production

### Performance Monitoring

Continuous tracking:

- Backtesting results
- Exception reports
- User feedback
- Market condition changes

---

## Common Validation Issues

### Conceptual

- Inappropriate assumptions for asset class
- Missing risk factors
- Inadequate tail modeling
- Ignoring regime changes

### Implementation

- Coding errors
- Numerical instability
- Incorrect parameter mapping
- Version control issues

### Data

- Survivorship bias
- Look-ahead bias
- Insufficient history
- Data quality issues

### Use

- Extrapolation beyond valid range
- Misinterpretation of outputs
- Inadequate use of model limitations

---

## Key Takeaways

- Validation ensures models are sound, correctly implemented, and fit for purpose
- Independence from development is essential
- Components: conceptual review, data assessment, implementation testing, outcome analysis
- Documentation is critical for governance and audit
- Ongoing monitoring catches performance degradation
- Model risk rating guides usage decisions

---

## Further Reading

- Board of Governors of the Federal Reserve System (2011), "Supervisory Guidance on Model Risk Management (SR 11-7)"
- OCC (2011), "Supervisory Guidance on Model Risk Management (OCC 2011-12)"
- Basel Committee (2009), "Principles for Sound Stress Testing"
- Rebonato, R. (2002), "Model Risk: New Challenges, New Solutions"

---

## Exercises

**Exercise 1.** A pricing model for exotic interest rate derivatives uses a one-factor short-rate model. Describe a conceptual validation process: what theoretical limitations should the validator flag, and what alternative models could serve as benchmarks?

??? success "Solution to Exercise 1"
    **Conceptual validation of a one-factor short-rate model for exotic interest rate derivatives.**

    **Theoretical limitations the validator should flag:**

    1. **Single-factor limitation.** A one-factor short-rate model (e.g., Hull-White, Vasicek, CIR) implies that the entire yield curve is driven by a single source of randomness. This means all points on the yield curve are perfectly correlated, which is empirically false. Exotic derivatives whose payoffs depend on the *shape* of the yield curve (e.g., CMS spread options, steepeners, butterfly spreads) cannot be properly priced because the model cannot generate realistic curve reshaping (flattening, steepening, or inversion independent of level shifts).

    2. **Inability to capture decorrelation across tenors.** In reality, short-term rates and long-term rates can move in opposite directions. A one-factor model forces $\text{Corr}(r(t_1), r(t_2)) = 1$ for all tenors, which misrepresents the risk of spread products.

    3. **Volatility structure.** One-factor models typically impose a specific volatility term structure (e.g., exponentially decaying in Hull-White). This may not match the market-observed swaption volatility surface, leading to mis-calibration for products sensitive to volatility at multiple tenors.

    4. **Distribution of rates.** Gaussian short-rate models (Vasicek, Hull-White) allow negative rates, which, while less problematic post-2010, may produce unrealistic dynamics for certain products. CIR avoids negative rates but has other restrictions (e.g., the Feller condition constraining volatility).

    5. **Calibration fragility for exotics.** Even if the model calibrates well to vanilla swaptions, the extrapolation to exotic payoffs (Bermudan swaptions, callable range accruals, TARNs) is unreliable because the model's dynamics are too restrictive.

    **Benchmark models:**

    - **Two-factor short-rate models** (e.g., two-factor Hull-White, G2++ model) to assess the impact of a second factor on pricing.
    - **LIBOR Market Model (LMM)** or **SABR-LMM**, which directly models forward rates and can capture decorrelation and smile effects.
    - **Quasi-Gaussian models** with stochastic volatility, which extend the short-rate framework while adding richer dynamics.
    - **Market quotes** for liquid exotic products (if available) as an empirical benchmark.

    The validator should quantify the pricing differences between the one-factor model and multi-factor benchmarks for the specific exotic products in question, flagging materiality thresholds and recommending model reserves or usage restrictions where differences are significant.

---

**Exercise 2.** A model's sensitivity analysis reveals that a 1% change in the correlation parameter $\rho$ causes a 15% change in portfolio VaR, while a 1% change in individual volatilities causes only a 2% change. Discuss the implications for model risk. How should this inform the validator's recommendations regarding parameter uncertainty and limits on the model's use?

??? success "Solution to Exercise 2"
    **Analysis of sensitivity results and implications for model risk.**

    The sensitivity analysis reveals a **disproportionate dependence** on the correlation parameter $\rho$: a 1% perturbation in $\rho$ causes a 15% change in VaR, while the same perturbation in individual volatilities causes only a 2% change. This has several important implications:

    **1. Parameter uncertainty is concentrated in $\rho$.**

    The elasticity of VaR with respect to $\rho$ is approximately:

    $$
    \eta_\rho = \frac{\Delta \text{VaR} / \text{VaR}}{\Delta \rho / \rho} \approx \frac{15\%}{1\%} = 15
    $$

    compared to an elasticity of approximately 2 for individual volatilities. The correlation parameter is the dominant risk driver for the portfolio's aggregate risk measure.

    **2. Correlation is notoriously difficult to estimate.**

    Unlike volatilities, which can be inferred from option markets or estimated from univariate return series with reasonable precision, correlations:

    - Have larger estimation error (require bivariate data)
    - Are unstable and regime-dependent (correlations tend to spike during crises)
    - May not have liquid market instruments for direct calibration
    - Are subject to the "correlation curse" where small samples produce noisy estimates

    **3. Model risk is high.**

    The combination of (a) high sensitivity to $\rho$ and (b) large uncertainty in $\rho$ means the model's output is unreliable. A mis-estimated correlation can produce dramatically wrong VaR figures.

    **Validator's recommendations:**

    - **Parameter uncertainty buffer:** Add a model risk reserve proportional to the VaR sensitivity to $\rho$. For example, if $\rho$ is estimated at $\hat{\rho}$ with standard error $\text{SE}(\hat{\rho})$, the buffer should cover:

    $$
    \text{Buffer} \approx \frac{\partial \text{VaR}}{\partial \rho} \times k \cdot \text{SE}(\hat{\rho})
    $$

    where $k$ is a coverage multiplier (e.g., $k = 2$ for approximate 95% coverage).

    - **Stress testing of correlations:** Run the model under stressed correlation scenarios (e.g., all correlations at 1, or at historically observed crisis levels) and report results alongside the base case.
    - **Usage restrictions:** The model should not be used for decisions highly sensitive to portfolio-level diversification benefits without supplementary analysis.
    - **Enhanced monitoring:** Track realized correlation against model assumptions and trigger re-validation if deviations exceed a threshold.
    - **Model improvement:** Investigate whether a more granular correlation structure (e.g., regime-switching correlations, DCC-GARCH) reduces sensitivity and improves robustness.

---

**Exercise 3.** Consider a model scored on four dimensions: conceptual soundness (weight 0.3), implementation quality (weight 0.2), performance (weight 0.3), and documentation (weight 0.2). Suppose the scores are 4, 5, 3, and 2 respectively (on a 1-5 scale). Compute the overall weighted rating. If the thresholds for green, yellow, and red are $[4, 5]$, $[3, 4)$, and $[1, 3)$ respectively, what is the model's traffic light rating? Identify which dimension most urgently needs improvement.

??? success "Solution to Exercise 3"
    **Computation of the weighted rating and traffic light classification.**

    The four dimensions, their weights, and scores are:

    | Dimension | Weight $w_i$ | Score $s_i$ |
    |-----------|-------------|-------------|
    | Conceptual soundness | 0.3 | 4 |
    | Implementation quality | 0.2 | 5 |
    | Performance | 0.3 | 3 |
    | Documentation | 0.2 | 2 |

    The overall weighted rating is:

    $$
    R = \sum_{i=1}^{4} w_i \cdot s_i = 0.3 \times 4 + 0.2 \times 5 + 0.3 \times 3 + 0.2 \times 2
    $$

    $$
    R = 1.2 + 1.0 + 0.9 + 0.4 = 3.5
    $$

    **Traffic light classification:**

    The thresholds are: Green $[4, 5]$, Yellow $[3, 4)$, Red $[1, 3)$.

    Since $R = 3.5 \in [3, 4)$, the model receives a **Yellow** rating, meaning issues have been identified and the model should be used with restrictions while remediation is pursued.

    **Most urgent dimension for improvement:**

    Documentation scores lowest at 2 out of 5. This is the most urgent area for improvement because:

    - It drags the overall score down significantly (contributing only $0.2 \times 2 = 0.4$ instead of a potential $0.2 \times 5 = 1.0$).
    - If documentation were improved from 2 to 5, the overall score would increase to $3.5 + 0.2 \times (5 - 2) = 3.5 + 0.6 = 4.1$, moving the model into the Green zone.
    - If performance (score 3) were improved to 5, the overall score would become $3.5 + 0.3 \times (5 - 3) = 3.5 + 0.6 = 4.1$, also reaching Green.
    - However, documentation improvements are typically faster and less risky than performance improvements, which may require fundamental model changes.

    Both documentation and performance need attention, but documentation is the most actionable short-term improvement.

---

**Exercise 4.** A validation team discovers that a credit risk model was calibrated using data from 2012-2019, a period of low defaults. The model is currently used to estimate losses for a portfolio during a period of rising defaults. Explain which validation component (conceptual review, data quality assessment, implementation testing, or outcome analysis) is most relevant to this issue. What specific biases might be present, and how would you recommend addressing them?

??? success "Solution to Exercise 4"
    **Identification of the relevant validation component and biases.**

    **Most relevant validation component: Data Quality Assessment.**

    The core issue is that the model was calibrated on data from a benign credit environment (2012--2019, a period of low defaults and economic expansion) and is now being applied during a period of rising defaults. This is fundamentally a data quality and representativeness problem.

    **Specific biases present:**

    1. **Regime bias (non-representativeness).** The calibration period does not contain a credit downturn, so the model has never "seen" the type of environment it is now being asked to predict. Parameters estimated from this period (e.g., default probabilities, loss given default, correlations) systematically understate the severity of losses during stress.

    2. **Procyclicality bias.** Models calibrated in benign periods produce low risk estimates, which can lead to under-provisioning and inadequate capital. When the environment deteriorates, the model fails precisely when it is needed most.

    3. **Survivorship bias.** During 2012--2019, firms that would have defaulted in a downturn may not appear in the data because defaults were rare. The calibration sample over-represents "survivors," leading to understated PDs.

    4. **Correlation underestimation.** Default correlations are higher during downturns (due to common factor exposure). A model calibrated on a low-default period will underestimate the correlation parameter $\rho$ in the Vasicek framework, leading to underestimation of tail losses.

    5. **Through-the-cycle vs. point-in-time confusion.** If the model was intended to produce through-the-cycle (TTC) estimates but was calibrated only on expansion data, it is effectively a point-in-time model for good times, not a TTC model.

    **Recommendations:**

    - **Extend the calibration window** to include at least one full credit cycle (e.g., include 2007--2011 data if available).
    - **Apply conservative overlays:** Supplement model estimates with expert judgment for stressed PDs and LGDs.
    - **Stress test the model** using historical downturn scenarios (e.g., apply 2008--2009 default rates to the current portfolio).
    - **Use downturn LGD estimates** as required by Basel IRB, rather than average-cycle LGDs.
    - **Monitor model performance intensively** during the current period and trigger re-calibration if deviations from observed defaults exceed materiality thresholds.
    - **Outcome analysis** should also be invoked as a complementary component: compare model predictions to emerging realized defaults on an ongoing basis.

---

**Exercise 5.** Explain the difference between look-ahead bias and survivorship bias in the context of model validation. Provide a concrete example of each in a portfolio risk model. Describe a testing procedure a validator could use to detect each type of bias.

??? success "Solution to Exercise 5"
    **Look-ahead bias vs. survivorship bias in model validation.**

    **Look-ahead bias** occurs when information that was not available at the time of the decision is used in the model's construction, calibration, or backtesting. The model "looks ahead" in time, using future information to make past predictions appear better than they truly were.

    **Survivorship bias** occurs when the dataset systematically excludes entities (firms, securities, funds) that have exited the sample (due to default, delisting, merger, or fund closure), leading to an overly optimistic representation of performance or risk.

    **Concrete examples in a portfolio risk model:**

    *Look-ahead bias example:* A VaR model is backtested using a dataset where corporate bond spreads have been retroactively corrected. For example, the modeler uses the "final" time series from a data vendor that includes spread corrections applied weeks after the original quotes. When the backtest simulates the VaR on date $t$, it uses spread data that was not actually available on date $t$, making the model appear more accurate than it would have been in real time.

    *Survivorship bias example:* A credit portfolio model estimates default probabilities using a database of corporate bonds. If bonds that defaulted were removed from the database (a common issue with some commercial datasets), the model is calibrated only on survivors. The estimated PD will be biased downward:

    $$
    \hat{\text{PD}}_{\text{biased}} = \frac{\text{Defaults in remaining sample}}{\text{Total in remaining sample}} < \frac{\text{True defaults}}{\text{True total}} = \text{PD}_{\text{true}}
    $$

    **Testing procedures to detect each bias:**

    *Detecting look-ahead bias:*

    - **Point-in-time reconstruction:** Rebuild the dataset using only information available at each historical date (use "as-of" or "point-in-time" snapshots from the data vendor). Compare model outputs using the reconstructed dataset versus the current dataset. Systematic differences indicate look-ahead contamination.
    - **Information lag test:** Introduce an artificial lag (e.g., 1--5 business days) in all data inputs and re-run the backtest. If model performance degrades significantly, it suggests the original backtest relied on data that was not contemporaneously available.

    *Detecting survivorship bias:*

    - **Dead firm inclusion test:** Obtain a complete list of firms (including those that defaulted, merged, or delisted) and verify they are present in the calibration dataset. Compare PD estimates with and without the excluded entities.
    - **Vintage analysis:** Track model performance by cohort vintage (e.g., all firms rated BB in 2015). If later vintages show systematically lower default rates than earlier vintages, survivorship bias may be present in the dataset construction.
    - **Cross-reference with default databases:** Compare the firm universe in the model's calibration set against a comprehensive default database (e.g., Moody's Default Study). Missing defaults are direct evidence of survivorship bias.

---

**Exercise 6.** Under the SR 11-7 framework, model risk is defined as "the potential for adverse consequences from decisions based on incorrect or misused model outputs." Consider a correctly implemented Black-Scholes model used to price long-dated equity options. Argue that this scenario can still generate significant model risk. Identify at least three specific sources of model risk in this case, distinguishing between errors in model specification and errors in model use.

??? success "Solution to Exercise 6"
    **Model risk from a correctly implemented Black-Scholes model for long-dated equity options.**

    Under SR 11-7, model risk arises from incorrect or misused model outputs. A correctly implemented Black-Scholes model used for long-dated equity options generates significant model risk despite having no implementation errors. The sources fall into two categories:

    **Errors in model specification (the model itself is wrong for this application):**

    1. **Constant volatility assumption.** Black-Scholes assumes the underlying's volatility $\sigma$ is constant over the option's life. For long-dated options (e.g., 5--10 years), this is egregiously wrong. Empirically, volatility is stochastic, mean-reverting, and exhibits clustering. The model cannot capture the term structure of volatility or the volatility smile/skew observed in the market. For long-dated options, the cumulative effect of stochastic volatility is substantial:

        $$
        \text{BS price} = \text{BS}(S, K, T, \sigma_{\text{const}}) \neq \mathbb{E}^Q\!\left[\text{Payoff under stochastic vol}\right]
        $$

    2. **Geometric Brownian motion dynamics.** The model assumes log-returns are normally distributed with constant drift and volatility. Over long horizons, equity returns exhibit fat tails, jumps, and regime changes that compound over time. The probability of extreme moves is severely underestimated:

        $$
        P_{\text{BS}}(S_T < K) = \Phi\!\left(\frac{\ln(K/S_0) - (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right)
        $$

        This normal-distribution tail probability can be orders of magnitude smaller than the empirical probability for deep out-of-the-money puts.

    3. **Constant interest rates.** For long-dated options, the assumption of a flat, constant risk-free rate ignores the stochastic nature of interest rates. Over 5--10 year horizons, rate movements can significantly affect option values, especially for deep out-of-the-money options where the discount factor dominates.

    **Errors in model use (the model is applied beyond its valid scope):**

    4. **Extrapolation beyond calibration domain.** Black-Scholes is typically calibrated to short-dated liquid options (1--3 months). Using the implied volatility from short-dated options to price long-dated exotics extrapolates far beyond the model's reliable range.

    5. **Hedging implications.** Even if the price is "close enough," the model's Greeks (delta, vega) may be materially wrong for long-dated options. Delta hedging under Black-Scholes assumes continuous rebalancing with constant volatility, neither of which holds. The resulting hedge P&L can deviate substantially from zero, creating hidden risk.

    6. **Misinterpretation of outputs.** Users may treat the Black-Scholes price as a reliable fair value without understanding that the model's assumptions are violated for long maturities. Risk reports based on Black-Scholes Greeks may understate the true risk exposure, leading to inadequate hedging and capital allocation.

    The SR 11-7 framework would require the validator to flag these issues, recommend model reserves or adjustments, and potentially restrict the model's use for maturities beyond a specified threshold.

---

**Exercise 7.** A bank has 150 internal models, each requiring annual validation. With a team of 10 validators, each capable of completing 20 validations per year, the bank cannot validate all models annually. Design a risk-based prioritization scheme: define at least three criteria for ranking model validation priority, explain how you would assign models to tiers with different review frequencies, and discuss how triggered reviews interact with the periodic schedule.

??? success "Solution to Exercise 7"
    **Risk-based prioritization scheme for model validation.**

    **Capacity analysis:** The bank has 10 validators $\times$ 20 validations/year = 200 validation slots per year. With 150 models, if all required annual review, this would require 150 slots, which is within capacity. However, in practice, validators also handle triggered reviews, ad hoc requests, and new model approvals. A risk-based scheme ensures the most critical models receive priority.

    **Three criteria for ranking model validation priority:**

    1. **Financial materiality.** The notional value, P&L contribution, or capital impact of the positions dependent on the model. Models that drive large capital charges or support significant trading activity carry higher risk if they fail. Metric: total P&L or RWA attributable to the model's outputs.

    2. **Model complexity and known limitations.** Models with more parameters, more complex mathematics, or known theoretical limitations are more likely to contain errors or produce unreliable outputs. Metric: number of calibrated parameters, number of outstanding validation findings, and subjective assessment of theoretical robustness (simple closed-form vs. Monte Carlo with many assumptions).

    3. **Recent performance and stability.** Models that have recently shown backtesting failures, large deviations from benchmarks, or parameter instability require more frequent review. Metric: number of backtesting exceptions in the past year, magnitude of parameter changes at last recalibration, and age since last full validation.

    **Tiering scheme with review frequencies:**

    | Tier | Criteria | Number of Models | Review Frequency | Annual Slots |
    |------|----------|-----------------|-----------------|-------------|
    | **Tier 1** | High materiality ($> \$1$B RWA), high complexity, or recent performance issues | ~30 models | Annual | 30 |
    | **Tier 2** | Moderate materiality ($\$100$M--$\$1$B RWA), moderate complexity | ~60 models | Biennial (every 2 years) | 30 |
    | **Tier 3** | Low materiality ($< \$100$M RWA), simple, stable performance | ~60 models | Triennial (every 3 years) | 20 |

    This allocates 30 + 30 + 20 = 80 scheduled validation slots per year, leaving 120 slots for triggered reviews, new model approvals, and other ad hoc work.

    **Interaction between triggered and periodic reviews:**

    - **Triggered reviews** are initiated by specific events: significant backtesting failures (e.g., entering the Basel yellow/red zone), major model changes, new product launches, market regime changes, or regulatory requests.
    - **Priority override:** A triggered review takes precedence over periodic reviews. If a Tier 3 model experiences a triggered event, it jumps the queue and is validated immediately, regardless of its periodic schedule.
    - **Credit toward periodic schedule:** A triggered review that includes a full validation scope counts as the periodic review, resetting the clock for the next scheduled review.
    - **Capacity management:** If triggered reviews consume a large share of capacity, Tier 2 and Tier 3 periodic reviews can be deferred (with documented justification), but Tier 1 annual reviews should never be deferred.
    - **Escalation:** If the number of triggered reviews exceeds available capacity, this itself is a risk signal that should be escalated to senior management, potentially indicating systemic model quality issues requiring additional resources.
