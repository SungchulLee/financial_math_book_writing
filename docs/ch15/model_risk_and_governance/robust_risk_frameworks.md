# Robust Risk Frameworks

**Robust risk frameworks** aim to manage risk effectively despite model uncertainty, data limitations, and unforeseen events. They acknowledge that no model is correct in all environments and design systems resilient to model failure.

---

## Motivation

### Model Risk Reality

- All models are wrong; some are useful
- Model assumptions fail during stress
- Historical data may not represent future
- Parameter estimates have uncertainty
- Regime changes invalidate calibrations

### Consequences of Model Failure

- 2007-2008: VaR models failed spectacularly
- LTCM: Correlation assumptions broke down
- Numerous "25-sigma" events that were model artifacts

### Goal

Build risk management systems that perform reasonably even when individual models fail.

---

## Principles of Robustness

### 1. Diversification of Methods

Don't rely on a single model:

$$
\text{Risk Assessment} = f(\text{Model}_1, \text{Model}_2, \ldots, \text{Model}_n)
$$

**Approaches:**
- Multiple VaR methodologies (historical, parametric, Monte Carlo)
- Alternative distributional assumptions
- Different calibration windows

### 2. Conservative Assumptions

When uncertain, err on the side of caution:
- Use confidence intervals, not point estimates
- Apply buffers for model uncertainty
- Choose conservative calibration when in doubt

### 3. Stress Testing Priority

Stress test results should inform decisions more than statistical models:
- Scenarios don't require probability estimates
- Capture tail risks models may miss
- Force consideration of "what if"

### 4. Simplicity Over Complexity

Complex models:
- Harder to understand and validate
- More parameters to estimate (overfitting risk)
- More failure modes

Simple models:
- Transparent limitations
- Robust to data issues
- Easier to monitor

**Principle:** Prefer simple models unless complexity adds clear value.

---

## Elements of Robust Frameworks

### Multiple Models

**Model averaging:**

$$
\hat{\rho} = \sum_i w_i \cdot \rho_i
$$

where $w_i$ are weights (possibly equal, or based on past performance).

**Envelope approach:**

$$
\hat{\rho} = \max_i \rho_i
$$

Use the most conservative estimate.

**Model selection with uncertainty:**

$$
\hat{\rho} = \rho_{\text{best}} + \text{Model Uncertainty Adjustment}
$$

### Stress Testing Integration

Robust framework combines:
- Statistical measures (VaR, ES)
- Stress test results
- Scenario analysis

$$
\text{Capital} = \max(\text{Statistical Capital}, \text{Stress Capital})
$$

### Buffers and Reserves

**Model risk buffer:**

$$
\text{Adjusted Risk} = \text{Model Risk} \times (1 + \text{Buffer})
$$

**Prudent valuation adjustments:**
- AVA for model uncertainty
- AVA for close-out costs
- AVA for market price uncertainty

### Conservative Limits

Set limits that:
- Are below model-implied thresholds
- Have cushion for model error
- Are tightened during uncertainty

---

## Governance and Culture

### Risk Culture

Robust frameworks require:
- Healthy skepticism of models
- Encouragement of challenge
- No punishment for questioning assumptions
- Learning from near-misses

### Three Lines of Defense

1. **First line:** Business units own and manage risk
2. **Second line:** Risk management provides oversight
3. **Third line:** Internal audit provides independent assurance

### Senior Management Role

- Set risk appetite with model uncertainty in mind
- Demand clarity on model limitations
- Challenge over-reliance on models
- Ensure adequate resources for risk function

### Board Oversight

- Understand key model risks
- Review stress test results
- Challenge management assumptions
- Approve risk appetite framework

---

## Practical Implementation

### Scenario-Based Decision Making

Rather than optimizing based on model output:

1. Identify plausible scenarios
2. Evaluate outcomes under each
3. Choose actions robust across scenarios

$$
\max_a \min_s U(a, s)
$$

(maximin: maximize the minimum outcome across scenarios)

### Model Uncertainty Quantification

**Bayesian approach:**

$$
p(\text{Risk} | \text{Data}) = \int p(\text{Risk} | \theta) \cdot p(\theta | \text{Data}) \, d\theta
$$

Integrate over parameter uncertainty.

**Bootstrap:**

Resample data to generate distribution of model outputs.

### Kill Switches

Predefined triggers for model override:
- Backtesting failures beyond threshold
- Unusual market conditions
- Extreme model outputs

**Action:** Switch to fallback (simpler, more conservative) approach.

---

## Framework Components

### 1. Model Inventory

Maintain complete list of models:
- Purpose and use
- Key assumptions
- Known limitations
- Validation status
- Owner and users

### 2. Tiering

Categorize models by importance:

| Tier | Criteria | Validation Frequency |
|------|----------|---------------------|
| **1** | Material impact, complex | Annual or more frequent |
| **2** | Moderate impact | Annual |
| **3** | Low impact, simple | Periodic (2-3 years) |

### 3. Model Risk Reporting

Regular reports including:
- Model performance metrics
- Backtesting results
- Model changes
- Issues and remediation
- Emerging risks

### 4. Escalation Framework

Clear protocols for:
- Model failures
- Validation issues
- Limit breaches
- Unusual outputs

---

## When Models Fail

### Recognition

Signs of model failure:
- Repeated backtesting breaches
- Implausible outputs
- Inconsistency across models
- Failure in related markets

### Response

1. **Immediate:** Increase conservatism; apply manual overlays
2. **Short-term:** Investigate root cause; implement fixes
3. **Medium-term:** Re-validate; consider replacement
4. **Long-term:** Learn lessons; improve framework

### Post-Mortem

After significant failures:
- Document what happened
- Identify warning signs missed
- Recommend improvements
- Share lessons across organization

---

## Key Takeaways

- Robust frameworks acknowledge model limitations
- Diversification of methods reduces single-model dependence
- Stress testing should complement, not replace, statistical measures
- Simplicity often beats complexity for robustness
- Governance and culture are as important as methodology
- Human judgment remains essential; models inform but don't dictate
- Preparedness for model failure is better than false confidence

---

## Further Reading

- Cont, R. (2006), "Model Uncertainty and Its Impact on the Pricing of Derivative Instruments"
- Taleb, N.N. (2007), *The Black Swan*
- Rebonato, R. (2010), *Coherent Stress Testing*
- Basel Committee (2009), "Principles for Sound Stress Testing Practices and Supervision"
- Glasserman, P. & Xu, X. (2014), "Robust Risk Measurement and Model Risk"
- Danielsson, J. et al. (2016), "Model Risk of Risk Models"
