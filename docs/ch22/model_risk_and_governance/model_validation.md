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

### SR 11-7 (Federal Reserve)

Key principles:
- Sound model development, implementation, use
- Effective validation
- Governance and controls
- **Definition:** "Model risk is the potential for adverse consequences from decisions based on incorrect or misused model outputs."

### Basel Framework

Model approval requirements:
- Internal validation
- Supervisory approval for internal models
- Use test (model must inform decisions)
- Backtesting and documentation

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

---

**Exercise 2.** A model's sensitivity analysis reveals that a 1% change in the correlation parameter $\rho$ causes a 15% change in portfolio VaR, while a 1% change in individual volatilities causes only a 2% change. Discuss the implications for model risk. How should this inform the validator's recommendations regarding parameter uncertainty and limits on the model's use?

---

**Exercise 3.** Consider a model scored on four dimensions: conceptual soundness (weight 0.3), implementation quality (weight 0.2), performance (weight 0.3), and documentation (weight 0.2). Suppose the scores are 4, 5, 3, and 2 respectively (on a 1-5 scale). Compute the overall weighted rating. If the thresholds for green, yellow, and red are $[4, 5]$, $[3, 4)$, and $[1, 3)$ respectively, what is the model's traffic light rating? Identify which dimension most urgently needs improvement.

---

**Exercise 4.** A validation team discovers that a credit risk model was calibrated using data from 2012-2019, a period of low defaults. The model is currently used to estimate losses for a portfolio during a period of rising defaults. Explain which validation component (conceptual review, data quality assessment, implementation testing, or outcome analysis) is most relevant to this issue. What specific biases might be present, and how would you recommend addressing them?

---

**Exercise 5.** Explain the difference between look-ahead bias and survivorship bias in the context of model validation. Provide a concrete example of each in a portfolio risk model. Describe a testing procedure a validator could use to detect each type of bias.

---

**Exercise 6.** Under the SR 11-7 framework, model risk is defined as "the potential for adverse consequences from decisions based on incorrect or misused model outputs." Consider a correctly implemented Black-Scholes model used to price long-dated equity options. Argue that this scenario can still generate significant model risk. Identify at least three specific sources of model risk in this case, distinguishing between errors in model specification and errors in model use.

---

**Exercise 7.** A bank has 150 internal models, each requiring annual validation. With a team of 10 validators, each capable of completing 20 validations per year, the bank cannot validate all models annually. Design a risk-based prioritization scheme: define at least three criteria for ranking model validation priority, explain how you would assign models to tiers with different review frequencies, and discuss how triggered reviews interact with the periodic schedule.
