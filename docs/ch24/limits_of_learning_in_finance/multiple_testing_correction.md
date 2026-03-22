# Multiple Testing Correction

Quantitative researchers routinely test hundreds of trading strategies, risk factors, or model specifications against the same historical data. When many hypotheses are tested simultaneously, some will appear statistically significant purely by chance. If 200 strategies are backtested at the 5% significance level, we expect roughly 10 "significant" results even if none has genuine predictive power. **Multiple testing correction** provides the mathematical tools to control the rate of false discoveries when many hypotheses are evaluated in parallel. This section develops the theory from classical error rate control through modern false discovery rate methods, and then applies these tools to the specific challenges of financial research: backtesting bias, factor selection, and Sharpe ratio adjustment.

---

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The distinction between family-wise error rate and false discovery rate
    - The Bonferroni and Holm-Bonferroni procedures for FWER control
    - The Benjamini-Hochberg procedure for FDR control
    - How backtesting bias inflates the apparent performance of strategies
    - The Harvey-Liu-Zhu framework for adjusting t-statistics in factor research
    - Haircut Sharpe ratios as a practical correction for multiple testing

---

## The Multiple Testing Problem

### Setup

Consider $m$ null hypotheses $H_{0,1}, \ldots, H_{0,m}$ tested simultaneously. Let:

- $m_0$ = number of true nulls (genuinely worthless strategies)
- $m_1 = m - m_0$ = number of false nulls (genuinely profitable strategies)
- $R$ = total number of rejections (declared "significant")
- $V$ = number of false rejections (type I errors among rejections)

The outcomes are summarized in:

| | Not rejected | Rejected | Total |
|---|---|---|---|
| **True null** | $U$ | $V$ | $m_0$ |
| **False null** | $T$ | $S$ | $m_1$ |
| **Total** | $m - R$ | $R$ | $m$ |

### Why Individual p-values Fail

If each test is conducted at level $\alpha = 0.05$ independently, the probability of *at least one* false rejection among $m_0$ true nulls is:

$$
\Pr(V \geq 1) = 1 - (1 - \alpha)^{m_0} \approx 1 - e^{-m_0 \alpha}
$$

For $m_0 = 100$ and $\alpha = 0.05$: $\Pr(V \geq 1) \approx 99.4\%$. Near certainty of at least one false discovery.

---

## Family-Wise Error Rate (FWER)

### Definition

The **family-wise error rate** is the probability of making one or more false rejections:

$$
\text{FWER} = \Pr(V \geq 1)
$$

Controlling FWER at level $\alpha$ ensures that the probability of any false positive is at most $\alpha$.

### Bonferroni Correction

The simplest FWER control: reject $H_{0,i}$ if and only if $p_i \leq \alpha / m$.

**Theorem (Bonferroni).** The Bonferroni procedure controls FWER at level $\alpha$ for any dependence structure among the tests.

*Proof.* By the union bound:

$$
\text{FWER} = \Pr\!\left(\bigcup_{i \in \mathcal{H}_0} \{p_i \leq \alpha/m\}\right) \leq \sum_{i \in \mathcal{H}_0} \Pr(p_i \leq \alpha/m) = m_0 \cdot \frac{\alpha}{m} \leq \alpha
$$

$\square$

!!! note "Conservatism of Bonferroni"
    Bonferroni is **conservative** because it uses the union bound. When tests are positively correlated (common in finance, where strategies share the same market data), the actual FWER is substantially below $\alpha$. This means Bonferroni may reject too few hypotheses, missing genuinely profitable strategies.

### Holm-Bonferroni (Step-Down) Procedure

A uniformly more powerful alternative:

1. Order the p-values: $p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$
2. Find the smallest $k$ such that $p_{(k)} > \alpha / (m - k + 1)$
3. Reject $H_{0,(1)}, \ldots, H_{0,(k-1)}$

**Theorem (Holm, 1979).** The Holm procedure controls FWER at level $\alpha$ under arbitrary dependence, and is uniformly more powerful than Bonferroni. $\square$

??? example "Bonferroni vs Holm"
    Suppose we test $m = 5$ strategies with p-values: $0.001, 0.013, 0.029, 0.04, 0.15$ at $\alpha = 0.05$.

    **Bonferroni threshold:** $\alpha/m = 0.01$. Only strategy 1 ($p = 0.001$) is rejected.

    **Holm procedure:**

    | $k$ | $p_{(k)}$ | Threshold $\alpha/(m - k + 1)$ | Decision |
    |-----|----------|-------------------------------|----------|
    | 1 | 0.001 | 0.010 | Reject |
    | 2 | 0.013 | 0.0125 | Stop (0.013 > 0.0125) |

    Holm rejects strategy 1 only. In this case the results coincide, but Holm is generally at least as powerful.

---

## False Discovery Rate (FDR)

### Motivation

FWER control becomes increasingly conservative as $m$ grows. In financial research with hundreds of factors, FWER control may reject nothing, even when many factors are genuinely predictive. The **false discovery rate** offers a less conservative alternative.

### Definition

The **false discovery rate** is the expected proportion of false rejections among all rejections:

$$
\text{FDR} = \mathbb{E}\!\left[\frac{V}{R \vee 1}\right]
$$

where $R \vee 1 = \max(R, 1)$ avoids division by zero.

### Benjamini-Hochberg (BH) Procedure

1. Order the p-values: $p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$
2. Find the largest $k$ such that $p_{(k)} \leq \frac{k}{m}\alpha$
3. Reject $H_{0,(1)}, \ldots, H_{0,(k)}$

**Theorem (Benjamini-Hochberg, 1995).** Under independence (or positive regression dependence) of the p-values:

$$
\text{FDR} \leq \frac{m_0}{m}\alpha \leq \alpha
$$

$\square$

!!! tip "Geometric Interpretation"
    The BH procedure has a clean geometric interpretation: plot the ordered p-values $p_{(k)}$ against the BH line $k\alpha/m$. Reject all hypotheses whose p-values fall below this line, up to the rightmost crossing point.

### Comparison: FWER vs FDR

| Property | FWER (Bonferroni) | FDR (BH) |
|----------|-------------------|----------|
| **Controls** | $\Pr(V \geq 1)$ | $\mathbb{E}[V/R]$ |
| **Conservatism** | High for large $m$ | Moderate |
| **Power** | Low when $m$ large | Higher |
| **Interpretation** | No false positive guarantee | Proportion of false positives |
| **Dependence** | Any | Independence or PRDS |

---

## Backtesting Bias in Finance

### The Data Snooping Problem

Financial backtesting introduces a severe multiple testing problem that is often implicit rather than explicit:

1. A researcher tests strategy $A$; it fails
2. Modifies to strategy $B$; it fails
3. After many iterations, strategy $Z$ "works"
4. Only strategy $Z$ is reported

The reported p-value for strategy $Z$ is meaningless because it ignores the 25 failed attempts. This is **data snooping** or **selection bias**.

### White's Reality Check

White (2000) proposed the **Bootstrap Reality Check** to test whether the best strategy is genuinely superior to a benchmark, accounting for the full universe of strategies tested.

**Null hypothesis:** No strategy outperforms the benchmark.

**Test statistic:**

$$
T^* = \max_{k=1,\ldots,m} \bar{d}_k
$$

where $\bar{d}_k = \frac{1}{n}\sum_{t=1}^n d_{k,t}$ is the average excess return of strategy $k$ over the benchmark.

The p-value is computed by bootstrapping the joint distribution of $(\bar{d}_1, \ldots, \bar{d}_m)$ under the null.

### Hansen's Superior Predictive Ability (SPA) Test

Hansen (2005) refined White's test by studentizing:

$$
T^*_{\text{SPA}} = \max_{k=1,\ldots,m} \frac{\bar{d}_k}{\hat{\sigma}_k / \sqrt{n}}
$$

This gives greater power against alternatives with high Sharpe ratio strategies.

---

## Harvey-Liu-Zhu Framework

### The Problem of Factor Proliferation

Harvey, Liu, and Zhu (2016) documented that over 300 factors had been published as "significant" predictors of stock returns. They argued that the conventional t-statistic threshold of 2.0 (corresponding to $\alpha = 0.05$) is far too low given the multiplicity of tests.

### Adjusted Significance Thresholds

Using a Bonferroni-type correction with an estimate of the total number of factors tested (including unpublished ones), they proposed:

$$
t_{\text{threshold}} = \Phi^{-1}\!\left(1 - \frac{\alpha}{2m}\right)
$$

For $m = 300$ factors and $\alpha = 0.05$:

$$
t_{\text{threshold}} = \Phi^{-1}(1 - 0.0000833) \approx 3.78
$$

They recommended that new factors should have $|t| > 3.0$ as a minimum threshold, reflecting the multiple testing burden accumulated over decades of financial research.

### Bayesian Extension

Harvey and Liu (2020) extended the framework using a Bayesian approach. If the prior probability that a factor is genuine is $\pi_0$, the posterior probability given an observed t-statistic $t_{\text{obs}}$ is:

$$
\Pr(\text{factor is genuine} \mid t_{\text{obs}}) = \frac{(1-\pi_0)\,f_1(t_{\text{obs}})}{\pi_0\,f_0(t_{\text{obs}}) + (1-\pi_0)\,f_1(t_{\text{obs}})}
$$

where $f_0$ is the density under the null and $f_1$ under the alternative. With a skeptical prior ($\pi_0$ close to 1), much stronger evidence is needed for conviction.

---

## Haircut Sharpe Ratios

### Motivation

Harvey and Liu (2015) proposed **haircut Sharpe ratios** to adjust reported backtested performance for multiple testing.

### The Adjustment

Given a reported Sharpe ratio $\widehat{\text{SR}}$ from a strategy selected from $m$ candidates, the haircut Sharpe ratio is:

$$
\text{SR}_{\text{haircut}} = \widehat{\text{SR}} - \Delta\text{SR}
$$

where $\Delta\text{SR}$ depends on:

- The number of strategies tested $m$
- The correlation structure among strategy returns
- The distribution of Sharpe ratios under the null

### Under Independence

If the $m$ strategy returns are independent under the null, the expected maximum Sharpe ratio is approximately:

$$
\mathbb{E}\!\big[\max_{k=1,\ldots,m} \widehat{\text{SR}}_k\big] \approx \sqrt{2 \ln m} \cdot \frac{1}{\sqrt{T}}
$$

where $T$ is the sample size. For $m = 100$ strategies and $T = 120$ months:

$$
\mathbb{E}[\text{max SR under null}] \approx \sqrt{2 \ln 100} / \sqrt{120} \approx 0.28
$$

Any reported Sharpe ratio should be reduced by at least this amount.

??? example "Applying the Haircut"
    A quantitative fund reports a backtested Sharpe ratio of 1.5 after testing 200 variants. Under independence:

    $$
    \Delta\text{SR} \approx \sqrt{2 \ln 200}\,/\,\sqrt{T}
    $$

    With $T = 240$ months: $\Delta\text{SR} \approx \sqrt{10.6}/\sqrt{240} \approx 0.21$.

    The haircut Sharpe ratio is $1.5 - 0.21 = 1.29$. If the strategies are correlated, the adjustment is smaller; if more strategies were tested but unreported, the adjustment is larger.

---

## Practical Guidelines for Financial Research

### Defense Against False Discoveries

1. **Pre-registration:** Specify hypotheses before looking at data
2. **Out-of-sample testing:** Reserve a holdout period for validation
3. **Economic rationale:** Require a plausible economic mechanism, not just statistical significance
4. **Multiple testing correction:** Apply BH or Bonferroni to the full set of tested strategies
5. **Replication:** Verify results across different markets, time periods, and data sources

### The Bailey-Lopez de Prado-Marcos Protocol

Bailey et al. (2014) proposed the **deflated Sharpe ratio**, which adjusts for:

- Number of trials
- Sample length
- Skewness and kurtosis of returns
- Correlation among strategies

$$
\text{DSR} = \Pr\!\left(\widehat{\text{SR}} > 0 \,\middle|\, \text{SR}_0 = \sqrt{\frac{2\ln m}{T}} \cdot \sqrt{1 - \hat{\gamma}_3 \cdot \widehat{\text{SR}} + \frac{\hat{\gamma}_4 - 1}{4}\cdot \widehat{\text{SR}}^2}\right)
$$

where $\hat{\gamma}_3$ and $\hat{\gamma}_4$ are sample skewness and kurtosis. A strategy is deemed significant only if $\text{DSR} > 0.95$.

!!! info "Connection to Overfitting"
    Multiple testing correction complements the treatment of overfitting in the previous section. Overfitting concerns a single model's complexity; multiple testing concerns the number of models considered. Both inflate apparent performance. The deflated Sharpe ratio addresses both by incorporating the number of trials *and* the distributional properties of returns.

---

## Key Takeaways

- Testing many hypotheses on the same data inflates false positive rates far beyond individual significance levels
- FWER control (Bonferroni, Holm) guarantees no false positives but is conservative for large test families
- FDR control (Benjamini-Hochberg) offers a practical balance between power and false positive control
- In finance, data snooping and strategy selection introduce implicit multiple testing that standard p-values ignore
- Harvey-Liu-Zhu recommend a t-statistic threshold of at least 3.0 for new factor discoveries
- Haircut Sharpe ratios adjust backtested performance for the number of strategies evaluated
- Combining statistical correction with economic reasoning and out-of-sample validation provides the strongest defense against false discoveries

---

## Further Reading

- Benjamini, Y. & Hochberg, Y. (1995), "Controlling the False Discovery Rate," *Journal of the Royal Statistical Society B*, 57(1), 289--300
- Harvey, C., Liu, Y. & Zhu, H. (2016), "... and the Cross-Section of Expected Returns," *Review of Financial Studies*, 29(1), 5--68
- Harvey, C. & Liu, Y. (2015), "Backtesting," *Journal of Portfolio Management*, 42(1), 13--28
- White, H. (2000), "A Reality Check for Data Snooping," *Econometrica*, 68(5), 1097--1126
- Hansen, P.R. (2005), "A Test for Superior Predictive Ability," *Journal of Business & Economic Statistics*, 23(4), 365--380
- Bailey, D., Borwein, J., Lopez de Prado, M. & Zhu, Q. (2014), "Pseudomathematics and Financial Charlatanism," *Notices of the AMS*, 61(5), 458--471
- Holm, S. (1979), "A Simple Sequentially Rejective Multiple Test Procedure," *Scandinavian Journal of Statistics*, 6(2), 65--70
