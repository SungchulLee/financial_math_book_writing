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

---

**Exercise 2.** Suppose a VaR backtest over $n = 250$ days at the 99% confidence level yields the following transition counts: $n_{00} = 234$, $n_{01} = 6$, $n_{10} = 6$, $n_{11} = 4$. Compute the transition probabilities $\hat{\pi}_{01}$ and $\hat{\pi}_{11}$, and explain whether the exceedances exhibit clustering. Set up the Christoffersen independence test statistic $LR_{ind}$ and state its asymptotic distribution under $H_0$.

---

**Exercise 3.** A desk operates under a VaR limit of \$50 million and a stress loss limit of \$200 million. On a given day, the desk's VaR is \$48 million and its worst-case stress loss is \$210 million. Classify the breach severity for each limit, and describe the appropriate escalation actions according to a standard limit breach management framework.

---

**Exercise 4.** Consider the Acerbi-Szekely ES backtest. Given a sample of $n = 250$ days at confidence level $\alpha = 0.975$, suppose there are 7 exceedances with losses $L_t$ and corresponding ES forecasts $\text{ES}_t$ as follows:

$$
\sum_{t: L_t > \text{VaR}_t} \frac{L_t}{\text{ES}_t} = 8.12
$$

Compute the test statistic $Z$ and interpret whether the ES model appears to be well-calibrated (i.e., whether $Z$ is close to 1).

---

**Exercise 5.** In the Basel traffic light framework, a bank has 6 exceedances over 250 days at 99% VaR. The base capital multiplier is 3.0. Compute the adjusted multiplier $k$ using the yellow zone formula

$$
k = 3.0 + 0.2 \times (\text{exceedances} - 4)
$$

If the bank's current VaR is \$80 million, what is the required regulatory capital under the adjusted multiplier versus the base multiplier?

---

**Exercise 6.** Explain why Expected Shortfall is not directly elicitable, and discuss how this complicates backtesting compared to VaR. Describe how the McNeil-Frey test transforms exceedances

$$
e_t = \frac{L_t - \text{VaR}_t}{\text{ES}_t - \text{VaR}_t}
$$

and state what distribution the transformed residuals should follow under a correctly specified model. What statistical tests can be used to verify this?

---

**Exercise 7.** A firm has a hierarchical limit structure: the firm-wide VaR limit is \$500 million, and it has three business units with individual VaR limits of \$250 million, \$200 million, and \$180 million. Explain why the sum of business unit limits (\$630 million) can exceed the firm-wide limit without inconsistency. Under what correlation assumptions would the firm-wide limit be binding? Derive a condition on the pairwise correlation $\rho$ among business unit P&L assuming equal volatilities such that the aggregate VaR equals the firm-wide limit.
