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
