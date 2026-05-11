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

---

## Exercises

**Exercise 1.** A risk manager has three VaR models producing daily 99% VaR estimates of \$12M, \$15M, and \$18M for the same portfolio. Describe the model averaging and envelope approaches. Compute the risk estimate under each. Discuss when each approach is more appropriate, and explain why equal-weighted averaging may be suboptimal.

??? success "Solution to Exercise 1"
    **Model averaging vs. envelope approaches.**

    **Given:** Three VaR models producing 99% daily VaR estimates of \$12M, \$15M, and \$18M.

    **Model averaging approach:**

    $$
    \hat{\rho}_{\text{avg}} = \sum_{i=1}^{3} w_i \cdot \rho_i
    $$

    With equal weights $w_i = 1/3$:

    $$
    \hat{\rho}_{\text{avg}} = \frac{1}{3}(12 + 15 + 18) = \frac{45}{3} = \$15\text{M}
    $$

    **Envelope approach:**

    $$
    \hat{\rho}_{\text{env}} = \max_i \rho_i = \max(12, 15, 18) = \$18\text{M}
    $$

    **When each approach is more appropriate:**

    *Model averaging* is appropriate when:

    - The models are believed to be approximately equally reliable, and each captures different aspects of risk.
    - The goal is a "best estimate" of risk that balances across methodologies.
    - The models' errors are believed to be diversified (some overestimate, others underestimate).

    *Envelope approach* is appropriate when:

    - The cost of underestimating risk far exceeds the cost of overestimating risk (asymmetric loss function).
    - The institution is in a period of heightened uncertainty or stress.
    - Regulatory or policy requirements demand conservatism.
    - At least one model may be capturing a genuine risk that others miss.

    **Why equal-weighted averaging may be suboptimal:**

    1. **Model quality varies.** If the \$18M model is a sophisticated Monte Carlo simulation while the \$12M model is a crude parametric approximation, equal weighting gives too much influence to the less reliable model.

    2. **Historical performance differs.** If backtesting shows one model has consistently better exceedance properties, it should receive higher weight.

    3. **Model dependence.** If two of the three models share similar assumptions (e.g., both are parametric with slightly different distribution assumptions), they are not independent, and equal weighting effectively double-counts their shared perspective.

    4. **Bayesian model averaging** provides a principled alternative: assign weights proportional to each model's posterior probability given the data:

        $$
        w_i \propto p(\text{Data} | \text{Model}_i) \cdot p(\text{Model}_i)
        $$

        This naturally up-weights models with better out-of-sample performance and down-weights models that fit the data poorly.

---

**Exercise 2.** Consider the maximin decision framework

$$
\max_a \min_s U(a, s)
$$

A portfolio manager must choose between two hedging strategies $a_1$ and $a_2$ under three scenarios $s_1, s_2, s_3$ with the following utility (P&L) matrix:

| | $s_1$ | $s_2$ | $s_3$ |
|---|---|---|---|
| $a_1$ | $-5$ | $+10$ | $+2$ |
| $a_2$ | $+1$ | $+3$ | $+4$ |

Which action does the maximin criterion select? Compare this to the expected utility criterion assuming equal scenario probabilities. Discuss the tradeoffs between the two decision rules in the context of risk management.

??? success "Solution to Exercise 2"
    **Maximin decision criterion vs. expected utility.**

    **Given utility matrix:**

    | | $s_1$ | $s_2$ | $s_3$ |
    |---|---|---|---|
    | $a_1$ | $-5$ | $+10$ | $+2$ |
    | $a_2$ | $+1$ | $+3$ | $+4$ |

    **Maximin criterion:**

    For each action, find the minimum utility across scenarios:

    $$
    \min_s U(a_1, s) = \min(-5, 10, 2) = -5
    $$

    $$
    \min_s U(a_2, s) = \min(1, 3, 4) = 1
    $$

    The maximin criterion selects the action that maximizes the minimum:

    $$
    \max_a \min_s U(a, s) = \max(-5, 1) = 1 \implies \text{select } a_2
    $$

    **Expected utility criterion (equal probabilities):**

    With $P(s_1) = P(s_2) = P(s_3) = 1/3$:

    $$
    \mathbb{E}[U(a_1)] = \frac{1}{3}(-5 + 10 + 2) = \frac{7}{3} \approx 2.33
    $$

    $$
    \mathbb{E}[U(a_2)] = \frac{1}{3}(1 + 3 + 4) = \frac{8}{3} \approx 2.67
    $$

    Under expected utility, $a_2$ is also preferred (2.67 > 2.33). In this example, both criteria agree.

    However, note that if the payoff of $a_1$ under $s_2$ were larger (say, $+20$ instead of $+10$), the expected utility would favor $a_1$ ($\mathbb{E}[U(a_1)] = 17/3 \approx 5.67$) while the maximin would still select $a_2$ (since the worst case of $a_1$ is still $-5$).

    **Tradeoffs between the two decision rules:**

    *Maximin:*

    - **Advantage:** Provides a guarantee on the worst-case outcome. In risk management, this is valuable because the downside (large losses) is more consequential than the upside (excess returns). It requires no probability estimates for scenarios.
    - **Disadvantage:** It is extremely conservative. It ignores all information about scenario likelihoods and potential upside. It can lead to overly cautious strategies that sacrifice significant expected value to avoid a worst case that may be very unlikely.

    *Expected utility:*

    - **Advantage:** Uses all available information (payoffs across all scenarios and their probabilities) to make an informed tradeoff. It maximizes the average outcome.
    - **Disadvantage:** Requires reliable probability estimates, which may be unavailable for stress scenarios. It is sensitive to the assumed probabilities: if the probabilities are wrong, the decision may be wrong. It does not protect against catastrophic outcomes in unlikely but severe scenarios.

    **In risk management context:** A robust framework often uses maximin or minimax regret as a complement to expected utility analysis. The maximin result shows the "floor" -- the worst that can happen under each strategy. If the maximin strategy also has reasonable expected utility (as $a_2$ does here), it is strongly preferred. When the two criteria disagree, the decision-maker must weigh the value of the potential upside against the risk of the worst case.

---

**Exercise 3.** A model risk buffer is applied as $\text{Adjusted Risk} = \text{Model Risk} \times (1 + b)$. If a bank's statistical VaR is \$100M and the stress capital is \$140M, and the capital is set as $\text{Capital} = \max(\text{Statistical Capital}, \text{Stress Capital})$, determine the minimum buffer $b$ such that statistical capital with the buffer exceeds stress capital. Discuss whether this approach adequately captures the tail risk that stress testing is designed to reveal.

??? success "Solution to Exercise 3"
    **Model risk buffer to exceed stress capital.**

    **Given:** Statistical VaR = \$100M, Stress capital = \$140M.

    The capital is set as:

    $$
    \text{Capital} = \max(\text{Statistical Capital}, \text{Stress Capital})
    $$

    where Statistical Capital $= \text{VaR} \times (1 + b)$.

    **Finding the minimum buffer $b$:**

    We need Statistical Capital $\geq$ Stress Capital:

    $$
    100 \times (1 + b) \geq 140
    $$

    $$
    1 + b \geq 1.4
    $$

    $$
    b \geq 0.4
    $$

    The minimum buffer is $b = 0.4$ (i.e., 40%).

    With $b = 0.4$: Statistical Capital $= 100 \times 1.4 = \$140$M, which equals Stress Capital. For the statistical capital to *strictly exceed* stress capital, any $b > 0.4$ suffices.

    **Does this approach adequately capture tail risk?**

    No, for several reasons:

    1. **Flat buffer is not risk-sensitive.** A fixed multiplicative buffer $b$ scales linearly with VaR, but the relationship between statistical risk and stress risk is typically nonlinear. A portfolio with large tail exposure (e.g., short options) may have a stress-to-VaR ratio much higher than 1.4, while a well-diversified cash equity portfolio may have a ratio close to 1.0. A flat buffer of 40% would be insufficient for the former and wasteful for the latter.

    2. **Buffer does not capture specific scenarios.** The purpose of stress testing is to evaluate the impact of specific adverse scenarios (e.g., a 2008-style credit crisis, a sudden rate shock). The stress capital of \$140M reflects the portfolio's vulnerability to particular tail events. A VaR-based buffer cannot replicate this scenario-specific information; it simply inflates the statistical measure without knowing *which* risks drive the stress loss.

    3. **VaR may be fundamentally wrong in the tail.** If the underlying distribution is misspecified (e.g., Gaussian when returns have fat tails), the VaR itself is unreliable. Scaling an unreliable number by $(1 + b)$ does not make it reliable. Stress testing provides an independent, scenario-based assessment that does not depend on distributional assumptions.

    4. **False sense of security.** Using a buffer to match stress capital may lead to complacency: "Our statistical capital already covers the stress scenario, so the stress test is redundant." This defeats the purpose of having two complementary approaches.

    The appropriate framework is to use **both** measures independently:

    $$
    \text{Capital} = \max(\text{VaR} \times (1 + b), \text{Stress Capital})
    $$

    where the buffer $b$ covers model uncertainty in the statistical estimate, and the stress capital covers specific tail scenarios. The two serve different purposes and should not be collapsed into a single number.

---

**Exercise 4.** In the Bayesian approach to model uncertainty, the posterior predictive distribution of risk is

$$
p(\text{Risk} | \text{Data}) = \int p(\text{Risk} | \theta) \cdot p(\theta | \text{Data}) \, d\theta
$$

Explain why a point estimate $\hat{\theta}$ (e.g., MLE) underestimates the true uncertainty in the risk measure compared to the full Bayesian integral. Suppose the model is a normal distribution with unknown mean $\mu$ and known variance $\sigma^2$. Show that the posterior predictive variance of a future observation exceeds $\sigma^2$, and interpret this extra variance as parameter uncertainty.

??? success "Solution to Exercise 4"
    **Bayesian posterior predictive variance and parameter uncertainty.**

    **Why a point estimate underestimates uncertainty:**

    A point estimate $\hat{\theta}$ (e.g., MLE) treats the parameter as known and fixed. The risk measure is then computed as $\rho(\hat{\theta}) = p(\text{Risk} | \hat{\theta})$, which captures only the **aleatoric uncertainty** (randomness inherent in the data-generating process).

    The full Bayesian approach integrates over parameter uncertainty:

    $$
    p(\text{Risk} | \text{Data}) = \int p(\text{Risk} | \theta) \cdot p(\theta | \text{Data}) \, d\theta
    $$

    This captures both aleatoric uncertainty (through $p(\text{Risk} | \theta)$) and **epistemic uncertainty** (through $p(\theta | \text{Data})$). Since the integral is over a spread of parameter values (not a single point), it produces a wider predictive distribution and higher variance.

    By Jensen's inequality, if $\text{Var}(\text{Risk} | \theta)$ is concave in $\theta$ (or more generally, by the law of total variance), the Bayesian predictive variance always exceeds the plug-in variance.

    **Demonstration with a normal model:**

    Suppose $X_1, \ldots, X_n \sim N(\mu, \sigma^2)$ with $\mu$ unknown and $\sigma^2$ known. We want the predictive distribution of a future observation $X_{n+1}$.

    **Prior:** Use a conjugate normal prior $\mu \sim N(\mu_0, \tau_0^2)$.

    **Posterior:** After observing data with sample mean $\bar{X}$:

    $$
    \mu | \text{Data} \sim N\!\left(\frac{\tau_0^{-2}\mu_0 + n\sigma^{-2}\bar{X}}{\tau_0^{-2} + n\sigma^{-2}},\; \frac{1}{\tau_0^{-2} + n\sigma^{-2}}\right)
    $$

    Denote the posterior mean as $\mu_n$ and posterior variance as $\tau_n^2 = (\tau_0^{-2} + n/\sigma^2)^{-1}$.

    **Posterior predictive distribution:**

    $$
    X_{n+1} | \text{Data} \sim N(\mu_n,\; \sigma^2 + \tau_n^2)
    $$

    The **posterior predictive variance** is:

    $$
    \text{Var}(X_{n+1} | \text{Data}) = \sigma^2 + \tau_n^2
    $$

    This exceeds $\sigma^2$ by exactly $\tau_n^2$, the **posterior variance of $\mu$**. This decomposition follows from the law of total variance:

    $$
    \text{Var}(X_{n+1} | \text{Data}) = \underbrace{\mathbb{E}[\text{Var}(X_{n+1} | \mu) | \text{Data}]}_{\sigma^2} + \underbrace{\text{Var}(\mathbb{E}[X_{n+1} | \mu] | \text{Data})}_{\tau_n^2}
    $$

    The first term is the **average within-model variance** (aleatoric), and the second term is the **variance of the model's prediction across parameter values** (epistemic/parameter uncertainty).

    **Interpretation:** The extra variance $\tau_n^2$ reflects the fact that we do not know $\mu$ exactly. As $n \to \infty$, $\tau_n^2 \to 0$ and the Bayesian predictive variance converges to $\sigma^2$, recovering the plug-in result. For finite samples, ignoring parameter uncertainty (using $\hat{\mu}$ as if it were the true $\mu$) underestimates the true predictive variance by $\tau_n^2$, leading to risk measures that are too tight.

    For risk management, this means VaR or ES computed from a point estimate $\hat{\theta}$ will be systematically too low, because it fails to account for the possibility that the true parameter is worse than estimated.

---

**Exercise 5.** During the 2008 financial crisis, many banks experienced "25-sigma events" under their Gaussian VaR models. Explain why these events were model artifacts rather than genuine statistical anomalies. If a bank observed daily returns of $-8\%$ with an estimated daily volatility of $1\%$ under a Gaussian model, compute the implied number of standard deviations. Discuss at least two specific model assumptions that failed and how a robust framework could have provided better risk estimates.

??? success "Solution to Exercise 5"
    **Analysis of "25-sigma events" during the 2008 crisis.**

    **Implied number of standard deviations:**

    With a daily return of $-8\%$ and estimated daily volatility of $1\%$:

    $$
    z = \frac{-0.08}{0.01} = -8
    $$

    This is an **8-sigma event**. Under a Gaussian distribution, the probability of a return exceeding 8 standard deviations is:

    $$
    P(Z < -8) \approx 6.2 \times 10^{-16}
    $$

    This corresponds to roughly one event per $1.6 \times 10^{15}$ days, or once every $6.4 \times 10^{12}$ years -- approximately 460 times the age of the universe. For the commonly cited "25-sigma" events, the probability is $P(Z < -25) \approx 10^{-138}$, which is effectively impossible.

    **Why these were model artifacts, not genuine anomalies:**

    These extreme sigma counts reveal failures in the model, not in the market. The market did what markets do; the model was wrong.

    **Specific model assumptions that failed:**

    1. **Gaussian (thin-tailed) distribution.** The normal distribution dramatically underestimates the probability of extreme returns. Empirical return distributions exhibit **fat tails** (excess kurtosis), meaning large moves occur far more frequently than the Gaussian predicts. If returns follow a Student-$t$ distribution with, say, 4 degrees of freedom, a $-8\%$ return with $1\%$ daily volatility is approximately a 3.5-sigma event -- rare but not impossible.

    2. **Constant volatility.** The $1\%$ daily volatility was estimated from a calm pre-crisis period. During the crisis, realized volatility surged to 4--6% per day. The model used a stale volatility estimate that was 4--6 times too low, mechanically inflating the sigma count. A GARCH model or realized volatility estimator would have shown volatility increasing before the extreme moves occurred, producing a more reasonable sigma count.

    3. **Independence of returns (no clustering).** The Gaussian VaR model assumes returns are i.i.d. In reality, large losses cluster (volatility clustering), so the probability of a large loss *given that recent losses have been large* is much higher than the unconditional probability.

    **How a robust framework could have provided better estimates:**

    - **Fat-tailed distributions:** Using a Student-$t$, generalized hyperbolic, or EVT-based model would have assigned much higher probability to extreme losses.
    - **Time-varying volatility:** A GARCH or EWMA model would have increased volatility estimates as the crisis unfolded, keeping sigma counts in a reasonable range.
    - **Stress testing:** Scenario-based stress tests (e.g., replaying the 1987 crash or 1998 LTCM crisis) would have revealed the portfolio's vulnerability to large moves without relying on distributional assumptions.
    - **Ensemble of models:** Using multiple VaR methodologies (historical simulation, Monte Carlo with fat tails, parametric with GARCH) would have provided a range of estimates, with the most conservative flagging danger well before the "25-sigma" narrative emerged.
    - **Kill switches:** Trigger-based overrides (e.g., switching to a stressed model when realized volatility exceeds 2x the model estimate) would have activated well before the largest losses occurred.

---

**Exercise 6.** A bank's model inventory contains 200 models. Design a tiering scheme using three criteria: (i) P&L impact measured as the notional value of positions dependent on the model, (ii) model complexity measured as the number of parameters, and (iii) replacement difficulty. Define specific thresholds that assign each model to Tier 1, 2, or 3. For a limited validation budget of 50 full validations per year, propose a review schedule across tiers and justify your allocation.

??? success "Solution to Exercise 6"
    **Model tiering scheme and validation budget allocation.**

    **Three criteria for tiering:**

    **Criterion (i): P&L impact (notional value of dependent positions).**

    | Tier | Threshold |
    |------|-----------|
    | Tier 1 | Notional $> \$10$ billion or P&L impact $> \$100$ million |
    | Tier 2 | Notional \$1--\$10 billion or P&L impact \$10--\$100 million |
    | Tier 3 | Notional $< \$1$ billion and P&L impact $< \$10$ million |

    **Criterion (ii): Model complexity (number of parameters).**

    | Tier | Threshold |
    |------|-----------|
    | Tier 1 | $> 10$ calibrated parameters, or requires Monte Carlo / PDE solving |
    | Tier 2 | 3--10 parameters, semi-analytical solutions |
    | Tier 3 | $\leq 2$ parameters, closed-form solutions |

    **Criterion (iii): Replacement difficulty.**

    | Tier | Threshold |
    |------|-----------|
    | Tier 1 | No viable alternative; model is bespoke or deeply embedded in systems |
    | Tier 2 | Alternative exists but migration would take 3--12 months |
    | Tier 3 | Standard model with readily available replacements |

    **Composite tiering rule:** A model is assigned to the **highest tier** triggered by any criterion. For example, a simple (Tier 3 by complexity) but irreplaceable (Tier 1 by replacement difficulty) model pricing a large book (Tier 1 by P&L impact) is Tier 1.

    **Proposed allocation for 200 models with 50 full validations per year:**

    | Tier | Est. Models | Review Frequency | Annual Validations |
    |------|-------------|------------------|--------------------|
    | Tier 1 | 25 | Annual | 25 |
    | Tier 2 | 75 | Biennial | 37--38 (half each year) |
    | Tier 3 | 100 | Triennial | 33--34 (one-third each year) |

    **Annual budget:**

    - Tier 1: 25 validations
    - Tier 2: $75 / 2 \approx 38$ validations
    - Tier 3: $100 / 3 \approx 33$ validations
    - **Total scheduled:** $\approx 96$ validations per year

    This exceeds the budget of 50. To fit within 50 validations per year, we adjust:

    - **Tier 1:** 25 models, annual review = 25 validations per year (non-negotiable).
    - **Tier 2:** 75 models, biennial review = 38 per year. Reduce to targeted reviews of highest-risk Tier 2 models: 15 per year.
    - **Tier 3:** 100 models, triennial review = 33 per year. Reduce to 10 per year, using a lighter-touch "desk review" for the remainder.
    - **Total:** $25 + 15 + 10 = 50$ full validations.

    The remaining Tier 2 and Tier 3 models receive lighter monitoring (automated backtesting review, documentation check) rather than full validation.

    **Justification:** Tier 1 models carry the highest risk and must be validated annually without exception. Tier 2 models are reviewed on a rolling basis, with priority given to those with recent performance concerns or significant changes. Tier 3 models receive the lightest scrutiny, relying more on automated monitoring between periodic full reviews.

---

**Exercise 7.** Consider two kill-switch triggers: (a) more than 5 VaR backtesting exceedances in 60 days, and (b) the model's 1-day VaR exceeding 3 times its 60-day rolling average. For trigger (a), compute the probability of a false alarm under the null hypothesis that the 99% VaR model is correctly specified, using the binomial distribution with $n = 60$ and $p = 0.01$. Discuss the tradeoff between false alarms and delayed detection in setting kill-switch thresholds.

??? success "Solution to Exercise 7"
    **False alarm probability for kill-switch trigger (a).**

    **Setup:** Under $H_0$, the 99% VaR model is correctly specified, so each day's exceedance is an independent Bernoulli trial with $p = 1 - 0.99 = 0.01$. Over $n = 60$ days, the number of exceedances $X \sim \text{Binomial}(60, 0.01)$.

    The kill switch triggers when $X > 5$, i.e., more than 5 exceedances.

    **False alarm probability:**

    $$
    P(\text{false alarm}) = P(X > 5) = 1 - P(X \leq 5) = 1 - \sum_{k=0}^{5} \binom{60}{k} (0.01)^k (0.99)^{60-k}
    $$

    Computing each term:

    $$
    P(X = 0) = (0.99)^{60} = 0.54716
    $$

    $$
    P(X = 1) = \binom{60}{1}(0.01)^1(0.99)^{59} = 60 \times 0.01 \times 0.55268 = 0.33161
    $$

    $$
    P(X = 2) = \binom{60}{2}(0.01)^2(0.99)^{58} = 1770 \times 0.0001 \times 0.55827 = 0.09881
    $$

    $$
    P(X = 3) = \binom{60}{3}(0.01)^3(0.99)^{57} = 34220 \times 10^{-6} \times 0.56391 = 0.01930
    $$

    $$
    P(X = 4) = \binom{60}{4}(0.01)^4(0.99)^{56} = 487635 \times 10^{-8} \times 0.56961 = 0.00278
    $$

    $$
    P(X = 5) = \binom{60}{5}(0.01)^5(0.99)^{55} = 5461512 \times 10^{-10} \times 0.57536 = 0.000314
    $$

    Summing:

    $$
    P(X \leq 5) \approx 0.54716 + 0.33161 + 0.09881 + 0.01930 + 0.00278 + 0.000314 = 0.99997
    $$

    Therefore:

    $$
    P(\text{false alarm}) = 1 - 0.99997 \approx 0.00003 = 0.003\%
    $$

    The false alarm probability is extremely small -- approximately 3 in 100,000.

    **Tradeoff between false alarms and delayed detection:**

    The kill-switch threshold of "more than 5 exceedances in 60 days" is very conservative in terms of avoiding false alarms: the probability of triggering when the model is correct is essentially zero. However, this conservatism comes at a cost:

    1. **Delayed detection.** If the model is genuinely broken (say, the true exceedance rate is 5% instead of 1%), it may still take many days before 6 exceedances accumulate. With $p_{\text{true}} = 0.05$ and $n = 60$, the expected number of exceedances is 3, and $P(X > 5) \approx 0.068$. Even with a significantly broken model, there is only a 7% chance of triggering the kill switch in any given 60-day window, meaning detection could be delayed by months.

    2. **Lower thresholds increase sensitivity but also false alarms.** If the trigger were set at "more than 2 exceedances in 60 days," the false alarm rate would be approximately $P(X > 2) \approx 1 - 0.978 = 2.2\%$, which is higher but still manageable. The detection probability for a broken model ($p = 0.05$) would increase to approximately $P(X > 2) \approx 0.64$, dramatically improving sensitivity.

    3. **Optimal threshold depends on costs.** The appropriate threshold balances:
        - **Cost of false alarm:** Unnecessary model override, operational disruption, fallback to a possibly inferior model.
        - **Cost of delayed detection:** Continued use of a broken model, accumulation of unrecognized risk, potential for large losses.

        If the cost of a model failure is high (e.g., a pricing model for a large derivatives book), a lower threshold with more false alarms is preferable. If the cost of switching models is high (e.g., a complex system requiring days to reconfigure), a higher threshold is more appropriate.

    4. **Complementary triggers help.** Trigger (b) (VaR exceeding 3x its rolling average) detects a different type of failure: sudden regime changes or market stress. Combining both triggers provides better coverage: trigger (a) catches gradual model degradation, while trigger (b) catches sudden environmental changes. Using multiple triggers reduces the need to set any single trigger at an extremely sensitive level.
