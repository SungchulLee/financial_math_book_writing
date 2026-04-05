# Backtesting and Limits

**Backtesting** compares model predictions to realized outcomes, providing empirical validation. **Risk limits** translate model outputs into actionable controls. Together, they form the operational backbone of risk management.

---

## Purpose of Backtesting

### Objectives

1. **Model validation:** Does the model predict accurately?
2. **Performance monitoring:** Is performance stable over time?
3. **Regulatory compliance:** Does the model meet regulatory standards?
4. **Early warning:** Detect model degradation before failures

### Principle

A good risk model should:
- Predict exceedances at the stated confidence level
- Not be too conservative (wasteful) or too aggressive (unsafe)

---

## VaR Backtesting

### Exceedance Counting

For a $\alpha$-level VaR (e.g., 99%), count days when losses exceed VaR:

$$
I_t = \mathbf{1}_{\{L_t > \text{VaR}_{\alpha,t}\}}
$$

**Expected exceedances:** $(1-\alpha) \times n$ days out of $n$

**Example:** 99% VaR over 250 days → expect 2.5 exceedances

### Kupiec Test (Unconditional Coverage)

**Null hypothesis:** $\mathbb{E}[I_t] = 1 - \alpha$

**Test statistic (likelihood ratio):**

$$
LR_{uc} = -2 \ln\left[\frac{(1-\alpha)^{n_0} \alpha^{n_1}}{\hat{p}^{n_1} (1-\hat{p})^{n_0}}\right]
$$

where:
- $n_1$ = number of exceedances
- $n_0 = n - n_1$ = non-exceedances
- $\hat{p} = n_1/n$ = observed exceedance rate

Under $H_0$: $LR_{uc} \sim \chi^2(1)$

**Decision:** Reject if $LR_{uc} > \chi^2_{1,1-\gamma}$ (critical value)

### Christoffersen Test (Independence)

Good VaR should have **independent** exceedances (no clustering).

**Transition probabilities:**
- $\pi_{01}$ = P(exceedance today | no exceedance yesterday)
- $\pi_{11}$ = P(exceedance today | exceedance yesterday)

**Independence requires:** $\pi_{01} = \pi_{11}$

**Test statistic:**

$$
LR_{ind} = -2 \ln\left[\frac{L(\hat{\pi})}{L(\hat{\pi}_{01}, \hat{\pi}_{11})}\right] \sim \chi^2(1)
$$

### Conditional Coverage Test

**Combined test:**

$$
LR_{cc} = LR_{uc} + LR_{ind} \sim \chi^2(2)
$$

Tests both correct level AND independence.

---

## Basel Traffic Light Approach

### Zones

Based on exceedances over 250 days at 99% VaR:

| Zone | Exceedances | VaR Multiplier | Interpretation |
|------|-------------|----------------|----------------|
| **Green** | 0-4 | 3.0 | Model acceptable |
| **Yellow** | 5-9 | 3.4-3.85 | Model questionable |
| **Red** | 10+ | 4.0 | Model rejected |

### Multiplier Adjustment

Capital = Multiplier × VaR

Yellow zone multiplier:

$$
k = 3.0 + 0.2 \times (\text{exceedances} - 4)
$$

---

## ES Backtesting

### Challenge

ES is not directly elicitable, making backtesting harder than VaR.

### Acerbi-Szekely Test

Based on the identity:

$$
\mathbb{E}\left[\frac{L \cdot \mathbf{1}_{L > \text{VaR}_\alpha}}{\text{ES}_\alpha}\right] = 1 - \alpha
$$

**Test statistic:**

$$
Z = \frac{1}{n(1-\alpha)} \sum_{t: L_t > \text{VaR}_t} \frac{L_t}{\text{ES}_t}
$$

Under correct model: $\mathbb{E}[Z] = 1$

### McNeil-Frey Test

Transform exceedances:

$$
e_t = \frac{L_t - \text{VaR}_t}{\text{ES}_t - \text{VaR}_t} \quad \text{for } L_t > \text{VaR}_t
$$

Under correct model: $e_t$ should follow standard exponential distribution.

Test using Kolmogorov-Smirnov or Anderson-Darling.

---

## Risk Limits

### Purpose

Translate risk measures into operational controls:
- Prevent excessive risk-taking
- Ensure capital adequacy
- Enable decentralized decision-making

### Types of Limits

**Position limits:** Maximum notional or delta exposure

$$
\text{Position}_i \le \text{Limit}_i
$$

**VaR limits:** Maximum VaR at desk/portfolio level

$$
\text{VaR}_{\text{desk}} \le \text{VaR Limit}
$$

**Stress limits:** Maximum loss under stress scenarios

$$
\text{Stress Loss} \le \text{Stress Limit}
$$

**Sensitivity limits:** Maximum Greeks (delta, gamma, vega)

$$
|\Delta| \le \Delta^{\max}, \quad |\Gamma| \le \Gamma^{\max}
$$

### Limit Framework

**Hierarchy:**
1. Firm-wide risk appetite
2. Business unit limits
3. Desk limits
4. Trader limits

$$
\sum_{\text{desks}} \text{Limit}_{\text{desk}} \le \text{Business Unit Limit} \le \text{Firm Limit}
$$

**Note:** Limits are not additive due to diversification; "budget" not "constraint."

---

## Limit Breach Management

### Breach Classification

| Severity | Description | Action |
|----------|-------------|--------|
| **Technical** | Brief, small breach | Document and monitor |
| **Minor** | Within tolerance | Explain and reduce within timeframe |
| **Major** | Significant breach | Escalate; immediate action required |
| **Critical** | Threatens capital | Senior management; possible forced liquidation |

### Escalation Procedures

1. **Detection:** Automated monitoring identifies breach
2. **Notification:** Alert to risk management and trader
3. **Explanation:** Trader provides rationale
4. **Decision:** Risk committee approves or requires action
5. **Resolution:** Position reduced or limit temporarily raised
6. **Documentation:** Record for audit trail

### Limit Exceptions

Temporary limit increases require:
- Business justification
- Senior approval
- Time limit
- Enhanced monitoring

---

## Backtesting and Limits Integration

### Using Backtesting for Limit Calibration

Poor backtesting results may indicate:
- Model underestimates risk → Tighten limits
- Model overestimates risk → Limits may be too conservative

### Backtesting of Limit Utilization

Track:
- Frequency of approaching limits
- Causes of breaches
- Relationship to P&L outcomes

### Early Warning Indicators

- Increasing limit utilization
- Clustering of near-breaches
- Correlation of utilization with market stress

---

## Key Takeaways

- Backtesting validates models by comparing predictions to outcomes
- Kupiec test checks exceedance rate; Christoffersen adds independence
- Basel traffic light penalizes poor VaR performance with higher multipliers
- ES backtesting requires special techniques (Acerbi-Szekely, McNeil-Frey)
- Risk limits operationalize risk measures into controls
- Breach management requires clear escalation procedures
- Backtesting results should inform limit calibration

---

## Further Reading

- Kupiec, P. (1995), "Techniques for Verifying the Accuracy of Risk Measurement Models"
- Christoffersen, P. (1998), "Evaluating Interval Forecasts"
- Acerbi, C. & Szekely, B. (2014), "Backtesting Expected Shortfall"
- Basel Committee (1996, updated), "Supervisory Framework for the Use of Backtesting"
- McNeil, A. & Frey, R. (2000), "Estimation of Tail-Related Risk Measures for Heteroscedastic Financial Time Series"

---

## Exercises

**Exercise 1.** A bank uses a 99% VaR model and observes 8 exceedances over 250 trading days. Compute the Kupiec likelihood ratio test statistic $LR_{uc}$ and determine whether the model falls in the Basel green, yellow, or red zone. State clearly the expected number of exceedances under $H_0$.

??? success "Solution to Exercise 1"
    **Kupiec test and Basel zone classification for 8 exceedances over 250 days.**

    **Expected exceedances under $H_0$:**

    For a 99% VaR model over $n = 250$ days, the expected number of exceedances is:

    $$
    \mathbb{E}[n_1] = (1 - \alpha) \times n = (1 - 0.99) \times 250 = 0.01 \times 250 = 2.5
    $$

    **Observed values:**

    - $n_1 = 8$ (exceedances)
    - $n_0 = 250 - 8 = 242$ (non-exceedances)
    - $\hat{p} = n_1 / n = 8 / 250 = 0.032$

    **Kupiec likelihood ratio test statistic:**

    $$
    LR_{uc} = -2 \ln\!\left[\frac{(1-\alpha)^{n_0} \cdot \alpha^{n_1}}{\hat{p}^{\,n_1} \cdot (1-\hat{p})^{n_0}}\right]
    $$

    Substituting values:

    $$
    LR_{uc} = -2 \ln\!\left[\frac{(0.01)^{242} \cdot (0.99)^{8}}{(0.032)^{8} \cdot (0.968)^{242}}\right]
    $$

    It is easier to compute the log directly:

    $$
    \ln\!\left[\frac{(1-\alpha)^{n_0} \cdot \alpha^{n_1}}{\hat{p}^{\,n_1} \cdot (1-\hat{p})^{n_0}}\right] = n_0 \ln\!\left(\frac{1-\alpha}{1-\hat{p}}\right) + n_1 \ln\!\left(\frac{\alpha}{\hat{p}}\right)
    $$

    Note: here $\alpha = 0.99$ is the confidence level, so the exceedance probability under $H_0$ is $1 - \alpha = 0.01$. Following the formula as stated in the text where $\alpha$ in the formula represents the *non-exceedance* probability:

    $$
    = n_0 \ln\!\left(\frac{1 - 0.01}{1 - 0.032}\right) + n_1 \ln\!\left(\frac{0.01}{0.032}\right)
    $$

    $$
    = 242 \ln\!\left(\frac{0.99}{0.968}\right) + 8 \ln\!\left(\frac{0.01}{0.032}\right)
    $$

    $$
    = 242 \ln(1.02273) + 8 \ln(0.3125)
    $$

    $$
    = 242 \times 0.02247 + 8 \times (-1.16315)
    $$

    $$
    = 5.438 - 9.305 = -3.867
    $$

    Therefore:

    $$
    LR_{uc} = -2 \times (-3.867) = 7.734
    $$

    Under $H_0$, $LR_{uc} \sim \chi^2(1)$. The critical value at the 5% significance level is $\chi^2_{1,0.95} = 3.841$. Since $7.734 > 3.841$, we **reject** $H_0$: the model significantly underestimates risk.

    **Basel traffic light zone:**

    With 8 exceedances over 250 days at 99% VaR:

    - Green zone: 0--4 exceedances
    - Yellow zone: 5--9 exceedances
    - Red zone: 10+ exceedances

    Since $8 \in [5, 9]$, the model falls in the **Yellow zone**. This means the model is questionable, and the bank faces an increased capital multiplier.

---

**Exercise 2.** Suppose a VaR backtest over $n = 250$ days at the 99% confidence level yields the following transition counts: $n_{00} = 234$, $n_{01} = 6$, $n_{10} = 6$, $n_{11} = 4$. Compute the transition probabilities $\hat{\pi}_{01}$ and $\hat{\pi}_{11}$, and explain whether the exceedances exhibit clustering. Set up the Christoffersen independence test statistic $LR_{ind}$ and state its asymptotic distribution under $H_0$.

??? success "Solution to Exercise 2"
    **Christoffersen independence test with transition counts.**

    **Given transition counts:**

    - $n_{00} = 234$ (no exceedance followed by no exceedance)
    - $n_{01} = 6$ (no exceedance followed by exceedance)
    - $n_{10} = 6$ (exceedance followed by no exceedance)
    - $n_{11} = 4$ (exceedance followed by exceedance)

    **Transition probabilities:**

    $$
    \hat{\pi}_{01} = \frac{n_{01}}{n_{00} + n_{01}} = \frac{6}{234 + 6} = \frac{6}{240} = 0.025
    $$

    $$
    \hat{\pi}_{11} = \frac{n_{11}}{n_{10} + n_{11}} = \frac{4}{6 + 4} = \frac{4}{10} = 0.40
    $$

    **Clustering analysis:**

    Under independence, we should have $\hat{\pi}_{01} = \hat{\pi}_{11}$. However, $\hat{\pi}_{11} = 0.40$ is dramatically larger than $\hat{\pi}_{01} = 0.025$. This means the probability of an exceedance given that yesterday was also an exceedance is 16 times higher than the unconditional probability of an exceedance. This is strong evidence of **clustering**: exceedances tend to occur in clusters rather than independently.

    **Christoffersen independence test statistic:**

    Under the null of independence, the common exceedance probability is:

    $$
    \hat{\pi} = \frac{n_{01} + n_{11}}{n_{00} + n_{01} + n_{10} + n_{11}} = \frac{6 + 4}{234 + 6 + 6 + 4} = \frac{10}{250} = 0.04
    $$

    The restricted (independent) log-likelihood is:

    $$
    L(\hat{\pi}) = (1 - \hat{\pi})^{n_{00} + n_{10}} \cdot \hat{\pi}^{n_{01} + n_{11}} = (0.96)^{240} \cdot (0.04)^{10}
    $$

    The unrestricted log-likelihood is:

    $$
    L(\hat{\pi}_{01}, \hat{\pi}_{11}) = (1 - \hat{\pi}_{01})^{n_{00}} \cdot \hat{\pi}_{01}^{n_{01}} \cdot (1 - \hat{\pi}_{11})^{n_{10}} \cdot \hat{\pi}_{11}^{n_{11}}
    $$

    $$
    = (0.975)^{234} \cdot (0.025)^{6} \cdot (0.60)^{6} \cdot (0.40)^{4}
    $$

    The test statistic is:

    $$
    LR_{ind} = -2 \ln\!\left[\frac{L(\hat{\pi})}{L(\hat{\pi}_{01}, \hat{\pi}_{11})}\right]
    $$

    Computing the log ratio:

    $$
    \ln L(\hat{\pi}) = 240 \ln(0.96) + 10 \ln(0.04) = 240(-0.04082) + 10(-3.21888) = -9.797 - 32.189 = -41.986
    $$

    $$
    \ln L(\hat{\pi}_{01}, \hat{\pi}_{11}) = 234\ln(0.975) + 6\ln(0.025) + 6\ln(0.60) + 4\ln(0.40)
    $$

    $$
    = 234(-0.02532) + 6(-3.68888) + 6(-0.51083) + 4(-0.91629)
    $$

    $$
    = -5.925 - 22.133 - 3.065 - 3.665 = -34.788
    $$

    Therefore:

    $$
    LR_{ind} = -2(-41.986 - (-34.788)) = -2(-7.198) = 14.396
    $$

    Under $H_0$ (independence), $LR_{ind} \sim \chi^2(1)$. Since $14.396 \gg 3.841$ (the 5% critical value), we **strongly reject** independence. The exceedances exhibit statistically significant clustering, indicating the VaR model fails to capture time-varying volatility or other dynamics that cause losses to cluster.

---

**Exercise 3.** A desk operates under a VaR limit of \$50 million and a stress loss limit of \$200 million. On a given day, the desk's VaR is \$48 million and its worst-case stress loss is \$210 million. Classify the breach severity for each limit, and describe the appropriate escalation actions according to a standard limit breach management framework.

??? success "Solution to Exercise 3"
    **Breach classification and escalation for VaR and stress limits.**

    **VaR limit assessment:**

    - VaR limit: \$50 million
    - Current VaR: \$48 million
    - Utilization: $48/50 = 96\%$

    The desk has **not** breached the VaR limit (\$48M $<$ \$50M). However, the 96% utilization is very high. Under a standard framework, this would be classified as a **near-breach** or **warning level**. Appropriate actions:

    - Monitor closely; the desk is near capacity.
    - Alert risk management to elevated utilization.
    - No formal escalation required, but the desk should be prepared to reduce if VaR increases.

    **Stress limit assessment:**

    - Stress loss limit: \$200 million
    - Current worst-case stress loss: \$210 million
    - Breach amount: $\$210\text{M} - \$200\text{M} = \$10\text{M}$ (5% over limit)

    The stress limit has been **breached**. Classification depends on severity:

    - Breach magnitude: $10/200 = 5\%$ over limit.
    - This is a **Minor to Major** breach depending on the institution's tolerance thresholds. A 5% overshoot is typically classified as a **Minor breach** (within tolerance but requiring explanation and remediation) if the tolerance band is, say, 10%, or a **Major breach** if the institution has zero tolerance for stress limit breaches.

    **Escalation actions for the stress limit breach:**

    1. **Detection:** Automated risk systems flag the \$210M stress loss against the \$200M limit.
    2. **Notification:** Immediate alert to the desk head, business unit risk manager, and central risk management.
    3. **Explanation:** The trader/desk head must provide a rationale for the breach (e.g., new position, market move, scenario update) within the same business day.
    4. **Decision:** The risk committee (or delegated authority) must decide whether to:
        - Require the desk to reduce positions to bring stress loss below \$200M within a specified timeframe (e.g., 1--3 business days).
        - Grant a temporary exception with enhanced monitoring (requires documented business justification and senior approval).
    5. **Resolution:** The desk reduces exposure or the limit is temporarily raised with appropriate approvals.
    6. **Documentation:** All actions, decisions, and rationale are recorded for the audit trail.

    **Key point:** Even though the VaR limit is not breached, the stress limit breach may indicate concentrated or tail-heavy risk that the VaR model does not fully capture. The combination of near-maximum VaR utilization and a stress limit breach should heighten concern.

---

**Exercise 4.** Consider the Acerbi-Szekely ES backtest. Given a sample of $n = 250$ days at confidence level $\alpha = 0.975$, suppose there are 7 exceedances with losses $L_t$ and corresponding ES forecasts $\text{ES}_t$ as follows:

$$
\sum_{t: L_t > \text{VaR}_t} \frac{L_t}{\text{ES}_t} = 8.12
$$

Compute the test statistic $Z$ and interpret whether the ES model appears to be well-calibrated (i.e., whether $Z$ is close to 1).

??? success "Solution to Exercise 4"
    **Acerbi-Szekely ES backtest computation.**

    **Given:**

    - $n = 250$ days, $\alpha = 0.975$ (so the exceedance probability is $1 - \alpha = 0.025$)
    - Number of exceedances: 7
    - Sum of loss-to-ES ratios: $\displaystyle\sum_{t: L_t > \text{VaR}_t} \frac{L_t}{\text{ES}_t} = 8.12$

    **Test statistic computation:**

    $$
    Z = \frac{1}{n(1-\alpha)} \sum_{t: L_t > \text{VaR}_t} \frac{L_t}{\text{ES}_t}
    $$

    $$
    Z = \frac{1}{250 \times 0.025} \times 8.12 = \frac{8.12}{6.25} = 1.2992
    $$

    **Interpretation:**

    Under a correctly specified ES model, $\mathbb{E}[Z] = 1$. The observed value $Z = 1.30$ exceeds 1, indicating that the realized losses in the tail are **larger** than the ES model predicted.

    Specifically, $Z > 1$ means:

    $$
    \frac{1}{n(1-\alpha)} \sum_{t: L_t > \text{VaR}_t} \frac{L_t}{\text{ES}_t} > 1 \implies \text{average}\left(\frac{L_t}{\text{ES}_t}\right) > \frac{n(1-\alpha)}{n_1}
    $$

    The ES model appears to **underestimate** the severity of tail losses. Whether this is statistically significant depends on the standard error of $Z$, which requires either bootstrapping or asymptotic theory.

    As a rough assessment: $Z = 1.30$ represents a 30% exceedance above the theoretical value of 1, which is a meaningful deviation. Combined with the fact that 7 exceedances versus an expected $250 \times 0.025 = 6.25$ also suggests a slight excess, the ES model does not appear well-calibrated. Further investigation into the tail distribution is warranted.

---

**Exercise 5.** In the Basel traffic light framework, a bank has 6 exceedances over 250 days at 99% VaR. The base capital multiplier is 3.0. Compute the adjusted multiplier $k$ using the yellow zone formula

$$
k = 3.0 + 0.2 \times (\text{exceedances} - 4)
$$

If the bank's current VaR is \$80 million, what is the required regulatory capital under the adjusted multiplier versus the base multiplier?

??? success "Solution to Exercise 5"
    **Basel yellow zone multiplier and capital impact.**

    **Multiplier computation:**

    With 6 exceedances, the bank is in the **Yellow zone** (5--9 exceedances). The adjusted multiplier is:

    $$
    k = 3.0 + 0.2 \times (\text{exceedances} - 4) = 3.0 + 0.2 \times (6 - 4) = 3.0 + 0.4 = 3.4
    $$

    **Capital computation:**

    With a current VaR of \$80 million:

    - **Under base multiplier:** Capital $= 3.0 \times \$80\text{M} = \$240$ million
    - **Under adjusted multiplier:** Capital $= 3.4 \times \$80\text{M} = \$272$ million

    **Difference:**

    $$
    \Delta\text{Capital} = \$272\text{M} - \$240\text{M} = \$32 \text{ million}
    $$

    This represents a $32/240 = 13.3\%$ increase in required capital due to the backtesting penalty.

    The yellow zone penalty creates a direct financial incentive for banks to maintain well-calibrated VaR models. Each additional exceedance beyond 4 costs $0.2 \times \$80\text{M} = \$16$ million in additional capital, up to the red zone threshold at 10 exceedances where the multiplier jumps to 4.0 (requiring $\$320$ million in capital).

---

**Exercise 6.** Explain why Expected Shortfall is not directly elicitable, and discuss how this complicates backtesting compared to VaR. Describe how the McNeil-Frey test transforms exceedances

$$
e_t = \frac{L_t - \text{VaR}_t}{\text{ES}_t - \text{VaR}_t}
$$

and state what distribution the transformed residuals should follow under a correctly specified model. What statistical tests can be used to verify this?

??? success "Solution to Exercise 6"
    **Elicitability of ES and the McNeil-Frey test.**

    **Why ES is not directly elicitable:**

    A risk measure $\rho$ is *elicitable* if there exists a scoring function $S(\rho, L)$ such that the true value $\rho^*$ is the unique minimizer of $\mathbb{E}[S(\rho, L)]$. VaR is elicitable because the quantile minimizes the asymmetric "tick" loss function:

    $$
    S_{\text{VaR}}(q, L) = (\alpha - \mathbf{1}_{L \leq q})(L - q)
    $$

    ES, however, is **not elicitable** (Gneiting, 2011). There exists no scoring function whose expected value is uniquely minimized at the true ES. This is a fundamental mathematical property, not a practical limitation.

    **Implications for backtesting:**

    Elicitability is the theoretical foundation for comparative backtesting: if a risk measure is elicitable, we can use the scoring function to rank competing forecasts. Since ES is not elicitable, we cannot directly compare two ES models using a scoring function without auxiliary information (such as the VaR forecast).

    In practice, this means:

    - We cannot construct a direct likelihood ratio test for ES analogous to the Kupiec test for VaR.
    - ES backtesting requires indirect methods that either condition on VaR exceedances or use the joint elicitability of (VaR, ES).

    **The McNeil-Frey test:**

    The McNeil-Frey approach transforms the exceedance losses as follows. For days where $L_t > \text{VaR}_t$:

    $$
    e_t = \frac{L_t - \text{VaR}_t}{\text{ES}_t - \text{VaR}_t}
    $$

    **Distribution under correct specification:**

    If the model is correctly specified, the excess losses beyond VaR follow a generalized Pareto distribution. Under the simplifying assumption that the conditional tail distribution is exponential (which holds, e.g., for Gaussian models or as a first-order approximation), the transformed residuals $e_t$ should follow a **standard exponential distribution** with CDF $F(x) = 1 - e^{-x}$ for $x \geq 0$.

    The intuition is: $\text{ES}_t - \text{VaR}_t$ is the expected excess loss beyond VaR. Normalizing by this quantity should yield a unit-mean exponential if the tail shape is correctly modeled.

    **Statistical tests to verify this:**

    1. **Kolmogorov-Smirnov (KS) test:** Compare the empirical CDF of $\{e_t\}$ against the standard exponential CDF. The KS statistic is:

        $$
        D_n = \sup_x |F_n(x) - (1 - e^{-x})|
        $$

    2. **Anderson-Darling test:** A more powerful variant of KS that places greater weight on the tails:

        $$
        A^2 = -n - \frac{1}{n}\sum_{i=1}^{n}(2i-1)\left[\ln F(e_{(i)}) + \ln(1 - F(e_{(n+1-i)}))\right]
        $$

    3. **QQ-plot:** Plot the quantiles of $\{e_t\}$ against the theoretical exponential quantiles. Deviations from the 45-degree line indicate model misspecification.

    4. **Mean test:** Under the null, $\mathbb{E}[e_t] = 1$. A simple $t$-test on the mean of $\{e_t\}$ tests whether the average excess is consistent with the model.

---

**Exercise 7.** A firm has a hierarchical limit structure: the firm-wide VaR limit is \$500 million, and it has three business units with individual VaR limits of \$250 million, \$200 million, and \$180 million. Explain why the sum of business unit limits (\$630 million) can exceed the firm-wide limit without inconsistency. Under what correlation assumptions would the firm-wide limit be binding? Derive a condition on the pairwise correlation $\rho$ among business unit P&L assuming equal volatilities such that the aggregate VaR equals the firm-wide limit.

??? success "Solution to Exercise 7"
    **Hierarchical VaR limits and diversification.**

    **Why the sum of business unit limits can exceed the firm-wide limit:**

    VaR is not additive across portfolios due to **diversification**. When P&L across business units are not perfectly correlated, the aggregate VaR is less than the sum of individual VaRs:

    $$
    \text{VaR}_{\text{firm}} \leq \text{VaR}_1 + \text{VaR}_2 + \text{VaR}_3
    $$

    with equality only when all P&L are perfectly positively correlated. In practice, different business units (e.g., equities, fixed income, FX) have imperfect correlations, so the firm benefits from diversification. The limit structure reflects this: individual units are each allowed up to their limit, knowing that not all will be at maximum simultaneously, and even if they are, the aggregate risk is reduced by diversification.

    The sum \$250M + \$200M + \$180M = \$630M exceeds the firm-wide limit of \$500M, which is consistent as long as the correlation structure provides sufficient diversification benefit.

    **Deriving the binding condition:**

    For a normal distribution, VaR is proportional to the standard deviation of P&L:

    $$
    \text{VaR}_i = z_\alpha \cdot \sigma_i
    $$

    where $z_\alpha = \Phi^{-1}(\alpha)$ is the VaR quantile multiplier.

    The aggregate VaR for the firm is:

    $$
    \text{VaR}_{\text{firm}} = z_\alpha \cdot \sigma_{\text{firm}} = z_\alpha \cdot \sqrt{\sum_{i}\sum_{j} \rho_{ij}\,\sigma_i\,\sigma_j}
    $$

    **Condition assuming equal pairwise correlation $\rho$ and equal volatilities:**

    Suppose, as the exercise requests, equal volatilities $\sigma_1 = \sigma_2 = \sigma_3 = \sigma$. Then:

    $$
    \text{VaR}_i = z_\alpha \cdot \sigma \quad \text{for each } i
    $$

    and:

    $$
    \text{VaR}_{\text{firm}} = z_\alpha \cdot \sqrt{3\sigma^2 + 6\rho\sigma^2} = z_\alpha \cdot \sigma\sqrt{3(1 + 2\rho)} = \text{VaR}_i \cdot \sqrt{3(1 + 2\rho)}
    $$

    However, the exercise states that the individual VaR *limits* are different (\$250M, \$200M, \$180M), but asks us to derive the condition assuming equal volatilities. Under equal volatilities, each unit has the same VaR, so let us interpret this as: each unit is at its maximum VaR limit, and we ask what $\rho$ makes the aggregate equal to the firm-wide limit.

    More precisely, we use the actual VaR limits as the VaR values. The aggregate VaR is:

    $$
    \text{VaR}_{\text{firm}} = \sqrt{\sum_i \sum_j \rho_{ij} \cdot \text{VaR}_i \cdot \text{VaR}_j}
    $$

    With equal pairwise correlation $\rho$ (and $\rho_{ii} = 1$):

    $$
    \text{VaR}_{\text{firm}} = \sqrt{\text{VaR}_1^2 + \text{VaR}_2^2 + \text{VaR}_3^2 + 2\rho(\text{VaR}_1 \cdot \text{VaR}_2 + \text{VaR}_1 \cdot \text{VaR}_3 + \text{VaR}_2 \cdot \text{VaR}_3)}
    $$

    Substituting the values:

    $$
    \text{VaR}_1^2 + \text{VaR}_2^2 + \text{VaR}_3^2 = 250^2 + 200^2 + 180^2 = 62500 + 40000 + 32400 = 134900
    $$

    $$
    \text{VaR}_1 \cdot \text{VaR}_2 + \text{VaR}_1 \cdot \text{VaR}_3 + \text{VaR}_2 \cdot \text{VaR}_3 = 50000 + 45000 + 36000 = 131000
    $$

    Setting the firm-wide VaR equal to the firm-wide limit of \$500M:

    $$
    500^2 = 134900 + 2\rho \cdot 131000
    $$

    $$
    250000 = 134900 + 262000\rho
    $$

    $$
    262000\rho = 115100
    $$

    $$
    \rho = \frac{115100}{262000} \approx 0.4393
    $$

    Therefore, if the pairwise correlation among business unit P&L is $\rho \approx 0.44$, and all units are at their maximum VaR limits, the aggregate VaR exactly equals the firm-wide limit of \$500 million.

    For $\rho > 0.44$, the firm-wide limit would be **binding** (aggregate VaR exceeds \$500M even with diversification), requiring at least one business unit to operate below its individual limit. For $\rho < 0.44$, there is slack in the firm-wide limit, and all units can simultaneously be at their individual limits.
