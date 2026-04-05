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

---

## Exercises

**Exercise 1.** For a portfolio loss $X \sim N(\mu, \sigma^2)$ with $\mu = 0$ and $\sigma = \$10\text{M}$, compute the 97.5% VaR and 97.5% ES using the formulas $\text{VaR}_\alpha = \sigma\,\Phi^{-1}(\alpha)$ and $\text{ES}_\alpha = \sigma\,\frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha}$.

??? success "Solution to Exercise 1"

    We are given $X \sim N(0, \sigma^2)$ with $\sigma = \$10\text{M}$ and $\alpha = 0.975$.

    **97.5% VaR:**

    $$
    \text{VaR}_{0.975} = \sigma \Phi^{-1}(0.975) = 10 \times 1.960 = \$19.60\text{M}
    $$

    **97.5% ES:**

    Using the formula for normal losses with zero mean:

    $$
    \text{ES}_{0.975} = \sigma \cdot \frac{\phi(\Phi^{-1}(0.975))}{1 - 0.975}
    $$

    We need $\phi(\Phi^{-1}(0.975)) = \phi(1.960)$. The standard normal PDF is:

    $$
    \phi(1.960) = \frac{1}{\sqrt{2\pi}} e^{-1.960^2/2} = \frac{1}{\sqrt{2\pi}} e^{-1.9208} \approx 0.05844
    $$

    Therefore:

    $$
    \text{ES}_{0.975} = 10 \times \frac{0.05844}{0.025} = 10 \times 2.338 = \$23.38\text{M}
    $$

    Note that $\text{ES}_{0.975} \approx \$23.38\text{M} > \text{VaR}_{0.975} \approx \$19.60\text{M}$. ES exceeds VaR by approximately 19%, reflecting the additional information ES captures about the severity of tail losses beyond the quantile.

---

**Exercise 2.** ES can be expressed as $\text{ES}_\alpha(X) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(X)\,du$, the average of VaR levels above $\alpha$. Verify this formula for a uniform distribution $X \sim U(0,1)$ with $\alpha = 0.95$.

??? success "Solution to Exercise 2"

    We verify the integral representation for $X \sim U(0,1)$ with $\alpha = 0.95$.

    **Step 1: Compute VaR for the uniform distribution.**

    For $X \sim U(0,1)$, the CDF is $F_X(x) = x$ on $[0,1]$, so the quantile function is:

    $$
    \text{VaR}_u(X) = F_X^{-1}(u) = u
    $$

    **Step 2: Compute ES via the integral representation.**

    $$
    \text{ES}_{0.95}(X) = \frac{1}{1-0.95} \int_{0.95}^{1} \text{VaR}_u(X)\,du = \frac{1}{0.05} \int_{0.95}^{1} u\,du
    $$

    $$
    = 20 \left[\frac{u^2}{2}\right]_{0.95}^{1} = 20 \times \frac{1 - 0.9025}{2} = 20 \times \frac{0.0975}{2} = 20 \times 0.04875 = 0.975
    $$

    **Step 3: Verify via the conditional expectation definition.**

    $$
    \text{ES}_{0.95}(X) = \mathbb{E}[X \mid X \ge \text{VaR}_{0.95}] = \mathbb{E}[X \mid X \ge 0.95]
    $$

    Since $X \mid (X \ge 0.95) \sim U(0.95, 1)$, the conditional expectation is:

    $$
    \mathbb{E}[X \mid X \ge 0.95] = \frac{0.95 + 1}{2} = 0.975
    $$

    Both methods yield $\text{ES}_{0.95} = 0.975$, confirming the integral representation.

---

**Exercise 3.** Explain why ES is a coherent risk measure while VaR is not. Specifically, construct an example where two portfolios have $\text{VaR}_{0.95}(X_1 + X_2) > \text{VaR}_{0.95}(X_1) + \text{VaR}_{0.95}(X_2)$, but $\text{ES}_{0.95}(X_1 + X_2) \le \text{ES}_{0.95}(X_1) + \text{ES}_{0.95}(X_2)$.

??? success "Solution to Exercise 3"

    **Why ES is coherent and VaR is not:**

    ES satisfies all four coherence axioms (monotonicity, translation invariance, positive homogeneity, and subadditivity). VaR satisfies the first three but fails **subadditivity**.

    **Constructing the example:**

    Let $X_1$ and $X_2$ be independent Bernoulli losses:

    - $\mathbb{P}(X_i = 100) = 0.04$, $\mathbb{P}(X_i = 0) = 0.96$ for $i = 1, 2$

    **Individual VaR at 95%:**

    Since $\mathbb{P}(X_i \le 0) = 0.96 > 0.95$:

    $$
    \text{VaR}_{0.95}(X_1) = \text{VaR}_{0.95}(X_2) = 0
    $$

    **Portfolio VaR at 95%:**

    For independent $X_1, X_2$, the portfolio $X_1 + X_2$ has:

    - $\mathbb{P}(X_1 + X_2 = 0) = 0.96^2 = 0.9216$
    - $\mathbb{P}(X_1 + X_2 = 100) = 2 \times 0.04 \times 0.96 = 0.0768$
    - $\mathbb{P}(X_1 + X_2 = 200) = 0.04^2 = 0.0016$

    Since $\mathbb{P}(X_1 + X_2 \le 0) = 0.9216 < 0.95$, the 95th percentile is 100:

    $$
    \text{VaR}_{0.95}(X_1 + X_2) = 100 > 0 = \text{VaR}_{0.95}(X_1) + \text{VaR}_{0.95}(X_2)
    $$

    VaR violates subadditivity.

    **Now check ES at 95%:**

    Individual ES:

    $$
    \text{ES}_{0.95}(X_i) = \mathbb{E}[X_i \mid X_i \ge \text{VaR}_{0.95}(X_i)] = \mathbb{E}[X_i \mid X_i \ge 0]
    $$

    Since $\text{VaR}_{0.95}(X_i) = 0$ and $\mathbb{P}(X_i \ge 0) = 1$, we need a more careful computation using the integral formula. The worst $5\%$ tail for $X_i$ includes the mass at 100 (probability 0.04) plus part of the mass at 0:

    $$
    \text{ES}_{0.95}(X_i) = \frac{1}{0.05}\left[0.04 \times 100 + 0.01 \times 0\right] = \frac{4}{0.05} = 80
    $$

    So $\text{ES}_{0.95}(X_1) + \text{ES}_{0.95}(X_2) = 160$.

    Portfolio ES: The worst $5\%$ of $X_1 + X_2$ consists of:

    - $X_1 + X_2 = 200$ with probability 0.0016
    - $X_1 + X_2 = 100$ with probability 0.0768 (but we only need up to 0.05 total)

    Total tail probability needed: 0.05. We include $\mathbb{P}(200) = 0.0016$ and $\mathbb{P}(100)$ up to the remaining $0.05 - 0.0016 = 0.0484$:

    $$
    \text{ES}_{0.95}(X_1+X_2) = \frac{1}{0.05}[0.0016 \times 200 + 0.0484 \times 100] = \frac{0.32 + 4.84}{0.05} = \frac{5.16}{0.05} = 103.2
    $$

    **Subadditivity of ES holds:**

    $$
    \text{ES}_{0.95}(X_1 + X_2) = 103.2 \le 160 = \text{ES}_{0.95}(X_1) + \text{ES}_{0.95}(X_2) \checkmark
    $$

    ES correctly rewards diversification in this example.

---

**Exercise 4.** A portfolio has daily P&L observations: $\{-15, -12, -8, -5, -3, 1, 2, 4, 7, 10\}$ (in millions). Compute the empirical 80% VaR and 80% ES from this sample.

??? success "Solution to Exercise 4"

    **Data (sorted losses):** The P&L observations are $\{-15, -12, -8, -5, -3, 1, 2, 4, 7, 10\}$. Since these are P&L values, we convert to losses: $L_i = -\text{P\&L}_i$, giving:

    $$
    L = \{15, 12, 8, 5, 3, -1, -2, -4, -7, -10\}
    $$

    Sorted in increasing order:

    $$
    L_{(1)} = -10, \; L_{(2)} = -7, \; L_{(3)} = -4, \; L_{(4)} = -2, \; L_{(5)} = -1, \; L_{(6)} = 3, \; L_{(7)} = 5, \; L_{(8)} = 8, \; L_{(9)} = 12, \; L_{(10)} = 15
    $$

    **Empirical 80% VaR:**

    With $n = 10$ and $\alpha = 0.80$:

    $$
    \widehat{\text{VaR}}_{0.80} = L_{(\lceil 10 \times 0.80 \rceil)} = L_{(8)} = 8
    $$

    So $\text{VaR}_{0.80} = \$8\text{M}$.

    **Empirical 80% ES:**

    ES is the average of the losses in the worst $(1-\alpha) = 20\%$ tail, i.e., the top 2 losses:

    $$
    \widehat{\text{ES}}_{0.80} = \frac{1}{n(1-\alpha)} \sum_{i=\lceil n\alpha \rceil}^{n} L_{(i)} = \frac{1}{10 \times 0.20} \left(L_{(8)} + L_{(9)} + L_{(10)}\right)
    $$

    More precisely, with $n(1-\alpha) = 2$ observations in the tail above the VaR:

    $$
    \widehat{\text{ES}}_{0.80} = \frac{L_{(9)} + L_{(10)}}{2} = \frac{12 + 15}{2} = \$13.5\text{M}
    $$

    (Using $\lceil n\alpha \rceil + 1 = 9$ through $n = 10$, the observations strictly exceeding the VaR threshold.)

    Alternatively, using the full formula including the boundary observation:

    $$
    \widehat{\text{ES}}_{0.80} = \frac{1}{10 \times 0.20}(L_{(9)} + L_{(10)}) = \frac{27}{2} = \$13.5\text{M}
    $$

    The ES of \$13.5M significantly exceeds the VaR of \$8M, reflecting the severity of the two worst losses (\$12M and \$15M).

---

**Exercise 5.** ES is not "elicitable" (there is no scoring function that ES uniquely minimizes), which makes backtesting more challenging than for VaR. Explain what elicitability means and why it matters for model validation. Describe the joint backtesting approach using VaR and ES together.

??? success "Solution to Exercise 5"

    **Elicitability** means that a risk measure $\rho$ can be expressed as the minimizer of an expected scoring function:

    $$
    \rho(L) = \arg\min_x \mathbb{E}[S(x, L)]
    $$

    for some function $S(x, y)$.

    **VaR is elicitable:** The scoring function for the $\alpha$-quantile is the pinball (quantile) loss:

    $$
    S(x, L) = (\mathbf{1}_{L \le x} - \alpha)(x - L)
    $$

    This means one can evaluate competing VaR forecasts by comparing their average scores on realized outcomes. The model with the lower average score is better.

    **ES is not directly elicitable:** There is no single scoring function $S$ that ES uniquely minimizes. This was proven by Gneiting (2011).

    **Why elicitability matters for model validation:**

    1. **Comparative backtesting:** With an elicitable risk measure, one can rank competing forecasts by their average scores. For VaR, this is straightforward. For ES, one cannot directly compare two ES models using scoring rules.
    2. **Regression-based estimation:** Elicitable quantities can be estimated via M-estimation (generalized regression), which provides statistical theory for inference.
    3. **Incentive compatibility:** Elicitability ensures that the forecaster is incentivized to report the true risk measure; misreporting increases the expected score.

    **Joint backtesting approach (Fissler-Ziegel):**

    Although ES alone is not elicitable, the pair $(\text{VaR}_\alpha, \text{ES}_\alpha)$ is **jointly elicitable**. This means there exists a bivariate scoring function $S(v, e; L)$ such that:

    $$
    (\text{VaR}_\alpha, \text{ES}_\alpha) = \arg\min_{(v,e)} \mathbb{E}[S(v, e; L)]
    $$

    **Practical backtesting methods for ES include:**

    - **Acerbi-Szekely test:** Uses the identity $\mathbb{E}\left[\frac{L \cdot \mathbf{1}_{L \ge \text{VaR}_\alpha}}{\text{ES}_\alpha}\right] = 1 - \alpha$ to construct a test statistic
    - **McNeil-Frey residual test:** Transforms exceedances beyond VaR and tests whether they follow the predicted conditional distribution
    - **Joint scoring approach:** Evaluates the pair (VaR, ES) simultaneously using strictly consistent joint scoring functions

    The joint approach has become the recommended practice under Basel III's FRTB framework, where both VaR and ES must be backtested together.

---

**Exercise 6.** Under Basel III's FRTB, regulatory capital is based on ES at the 97.5% confidence level over a 10-day holding period. If the 1-day ES at 97.5% is \$50M, estimate the 10-day ES using the square-root-of-time scaling $\text{ES}_{10} \approx \sqrt{10} \times \text{ES}_1$. Discuss when this scaling is appropriate and when it fails.

??? success "Solution to Exercise 6"

    **Given:** 1-day ES at 97.5% confidence is $\text{ES}_{0.975}^{1\text{-day}} = \$50\text{M}$.

    **10-day ES using square-root-of-time scaling:**

    $$
    \text{ES}_{0.975}^{10\text{-day}} \approx \sqrt{10} \times \text{ES}_{0.975}^{1\text{-day}} = \sqrt{10} \times 50 \approx 3.162 \times 50 = \$158.1\text{M}
    $$

    **When the scaling is appropriate:**

    The square-root-of-time rule is exact when:

    1. **Daily returns are i.i.d.** (independent and identically distributed)
    2. **Returns are normally distributed** (so the $h$-day return is $N(h\mu, h\sigma^2)$)
    3. **The portfolio is linear** in the risk factors (no options or nonlinear instruments)

    Under these conditions, the $h$-day loss has standard deviation $\sigma\sqrt{h}$, and since ES under normality is proportional to $\sigma$, it also scales by $\sqrt{h}$.

    **When the scaling fails:**

    1. **Volatility clustering (GARCH effects):** Returns are not identically distributed; conditional variance changes over time. During high-volatility periods, the i.i.d. assumption underestimates multi-day risk because volatility persistence amplifies losses over multiple days. The true 10-day ES exceeds $\sqrt{10} \times \text{ES}_1$.

    2. **Fat tails:** If daily returns follow a heavy-tailed distribution (e.g., Student-$t$), the $h$-day aggregated distribution may not scale by $\sqrt{h}$. For stable distributions with tail index $\alpha_s < 2$, the scaling factor is $h^{1/\alpha_s}$ instead of $h^{1/2}$, which is larger.

    3. **Serial correlation:** If returns are positively autocorrelated, 10-day variance exceeds $10 \times$ daily variance, and the square-root rule underestimates risk. Conversely, negative autocorrelation would cause overestimation.

    4. **Nonlinear portfolios:** For options, the loss distribution changes shape over longer horizons due to gamma and theta effects, so scaling the 1-day measure is unreliable.

    5. **Liquidity risk:** Over longer horizons, position liquidation costs may increase nonlinearly, adding a component that does not scale by $\sqrt{h}$.

    In practice, regulators under FRTB require direct computation of the 10-day ES from a 10-day return model or use a "liquidity-adjusted" ES with staggered horizons, rather than relying on the square-root-of-time approximation.
