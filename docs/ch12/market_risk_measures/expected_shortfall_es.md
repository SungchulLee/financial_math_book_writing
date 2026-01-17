# Expected Shortfall (ES)

**Expected Shortfall (ES)**, also known as **Conditional Value-at-Risk (CVaR)** or **Average Value-at-Risk (AVaR)**, addresses key shortcomings of VaR by measuring the average loss in the tail beyond the VaR threshold.

---

## Definition

For confidence level $\alpha \in (0,1)$, the Expected Shortfall of loss $L$ is defined as:

$$
\text{ES}_\alpha(L) = \mathbb{E}[L \mid L \ge \text{VaR}_\alpha(L)]
$$

This is the **conditional expectation of losses given that they exceed VaR**.

---

## Integral Representation

An equivalent and often more useful representation expresses ES as an average of VaRs:

$$
\text{ES}_\alpha(L) = \frac{1}{1-\alpha} \int_\alpha^1 \text{VaR}_u(L) \, du
$$

**Interpretation:** ES is the average of all VaR levels from $\alpha$ to 1. This shows that ES incorporates information about the entire tail, not just a single quantile.

**Proof sketch:** For continuous $F_L$:
$$
\text{ES}_\alpha = \frac{1}{1-\alpha} \int_\alpha^1 F_L^{-1}(u) \, du = \frac{1}{1-\alpha} \int_{\text{VaR}_\alpha}^\infty x \, dF_L(x) = \mathbb{E}[L \mid L \ge \text{VaR}_\alpha]
$$

---

## Alternative Formulations

### Tail Expectation

For continuous distributions:

$$
\text{ES}_\alpha(L) = \frac{1}{1-\alpha} \mathbb{E}[L \cdot \mathbf{1}_{L \ge \text{VaR}_\alpha}]
$$

### Optimization Formulation (Rockafellar-Uryasev)

ES admits a convex optimization representation:

$$
\text{ES}_\alpha(L) = \min_{v \in \mathbb{R}} \left\{ v + \frac{1}{1-\alpha} \mathbb{E}[(L-v)^+] \right\}
$$

The minimizer is $v^* = \text{VaR}_\alpha(L)$. This formulation is valuable for portfolio optimization.

---

## ES Under Normality

If $L \sim N(\mu, \sigma^2)$, then:

$$
\text{ES}_\alpha = \mu + \sigma \cdot \frac{\phi(\Phi^{-1}(\alpha))}{1-\alpha}
$$

where $\phi$ is the standard normal PDF and $\Phi$ is the CDF.

**Example:** For $\alpha = 0.99$ and $L \sim N(0, \sigma^2)$:

$$
\text{ES}_{0.99} = \sigma \cdot \frac{\phi(2.326)}{0.01} \approx 2.665\sigma
$$

Compare to $\text{VaR}_{0.99} \approx 2.326\sigma$. ES exceeds VaR by about 15%.

---

## Comparison with VaR

| Property | VaR | ES |
|----------|-----|-----|
| What it measures | Quantile (threshold) | Tail expectation (average) |
| Tail information | Single point | Entire tail |
| Subadditive | No (in general) | Yes |
| Coherent | No | Yes |
| Elicitable | Yes | No (directly) |
| Sensitivity to tail | Low | High |

---

## Coherence of ES

Expected Shortfall satisfies all four coherence axioms:

1. **Monotonicity:** If $L_1 \le L_2$ a.s., then $\text{ES}_\alpha(L_1) \le \text{ES}_\alpha(L_2)$

2. **Translation invariance:** $\text{ES}_\alpha(L + c) = \text{ES}_\alpha(L) + c$

3. **Positive homogeneity:** $\text{ES}_\alpha(\lambda L) = \lambda \, \text{ES}_\alpha(L)$ for $\lambda > 0$

4. **Subadditivity:** $\text{ES}_\alpha(L_1 + L_2) \le \text{ES}_\alpha(L_1) + \text{ES}_\alpha(L_2)$

**Subadditivity proof sketch:** Using the integral representation:
$$
\text{ES}_\alpha(L_1+L_2) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(L_1+L_2)\,du \le \frac{1}{1-\alpha}\int_\alpha^1 [\text{VaR}_u(L_1)+\text{VaR}_u(L_2)]\,du
$$

The inequality follows because quantiles of sums are bounded by sums of quantiles (for comonotonic variables, equality holds).

---

## Elicitability and Backtesting Challenges

Unlike VaR, **ES is not directly elicitable**. There is no scoring function $S$ such that:

$$
\text{ES}_\alpha(L) = \arg\min_x \mathbb{E}[S(x, L)]
$$

**Implications:**
- Cannot directly compare ES forecasts using scoring rules
- Backtesting ES requires different approaches

### Joint Elicitability

Although ES alone is not elicitable, the pair $(\text{VaR}_\alpha, \text{ES}_\alpha)$ is **jointly elicitable**. This enables:

- Joint backtesting of VaR and ES
- Proper scoring rules for the pair

### ES Backtesting Methods

**Acerbi-Szekely Tests:** Based on the identity:

$$
\mathbb{E}\left[\frac{L \cdot \mathbf{1}_{L \ge \text{VaR}_\alpha}}{\text{ES}_\alpha(L)}\right] = 1 - \alpha
$$

The test statistic compares:
$$
Z = \frac{1}{n(1-\alpha)} \sum_{t=1}^n \frac{L_t \cdot \mathbf{1}_{L_t \ge \widehat{\text{VaR}}_\alpha}}{\widehat{\text{ES}}_\alpha}
$$

to the expected value of 1.

**McNeil-Frey Residual Test:** Transform exceedances to check for standard exponential distribution under correct model.

---

## Estimation Methods

### Historical Simulation

$$
\widehat{\text{ES}}_\alpha = \frac{1}{n(1-\alpha)} \sum_{i=\lceil n\alpha \rceil}^{n} L_{(i)}
$$

where $L_{(1)} \le \cdots \le L_{(n)}$ are ordered losses.

### Parametric Estimation

1. Fit a distribution to losses (e.g., Student-$t$, generalized Pareto)
2. Compute ES analytically or numerically from fitted distribution

### Monte Carlo

1. Simulate $N$ loss scenarios from the model
2. Compute sample ES from simulated losses

**Warning:** ES estimation has higher variance than VaR estimation because it depends on tail observations, which are scarce.

---

## Regulatory Relevance

### Basel III/IV Fundamental Review of the Trading Book (FRTB)

Modern regulations favor ES over VaR:

- **Market risk capital** now based on $\text{ES}_{0.975}$ (97.5% confidence)
- **Rationale:**
  - ES captures tail severity
  - Coherence ensures diversification is rewarded
  - Discourages hiding risk beyond VaR threshold

### Capital Formula

Under FRTB internal models approach:
$$
\text{Capital} = \max\left(\text{ES}_{t-1}, m_c \cdot \overline{\text{ES}}\right) + \text{SES}
$$

where $m_c$ is a multiplier (minimum 1.5) and SES is the stressed ES.

---

## ES in Portfolio Optimization

The Rockafellar-Uryasev formulation enables ES-constrained portfolio optimization:

$$
\min_{\mathbf{w}} \quad -\mathbb{E}[R_P] \quad \text{s.t.} \quad \text{ES}_\alpha(L_P) \le \text{ES}^{\max}
$$

This is a **convex optimization problem** (unlike VaR constraints), making it tractable for large portfolios.

---

## Key Takeaways

- ES measures the expected loss in the worst $(1-\alpha)$ fraction of scenarios
- The integral representation $\text{ES}_\alpha = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u \, du$ shows ES averages all tail VaRs
- ES is coherent (satisfies subadditivity); VaR is not
- ES is not directly elicitable, complicating backtesting
- ES is now the regulatory standard for market risk under Basel III/IV

---

## Further Reading

- Acerbi, C. & Tasche, D. (2002), "On the coherence of Expected Shortfall"
- Rockafellar, R.T. & Uryasev, S. (2000), "Optimization of Conditional Value-at-Risk"
- Fissler, T. & Ziegel, J. (2016), "Higher order elicitability and Osband's principle"
- Basel Committee on Banking Supervision, "Fundamental Review of the Trading Book"
- McNeil, A., Frey, R., & Embrechts, P., *Quantitative Risk Management*
