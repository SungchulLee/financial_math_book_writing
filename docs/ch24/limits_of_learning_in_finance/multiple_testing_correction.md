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

---

## Exercises

**Exercise 1.** A quant fund tests $m = 50$ trading signals and obtains $p$-values $\{p_1, \ldots, p_{50}\}$ sorted in increasing order. Apply the Bonferroni correction at level $\alpha = 0.05$: what threshold must each $p$-value meet? If $p_{(1)} = 0.0005$, $p_{(2)} = 0.002$, and $p_{(3)} = 0.015$, which signals survive the Bonferroni correction?

??? success "Solution to Exercise 1"
    **Bonferroni correction with $m = 50$ and $\alpha = 0.05$.**

    The Bonferroni threshold is:

    $$
    \frac{\alpha}{m} = \frac{0.05}{50} = 0.001
    $$

    Each p-value must satisfy $p_i \leq 0.001$ to be declared significant.

    **Applying to the given p-values:**

    | Signal | p-value | Threshold | Decision |
    |--------|---------|-----------|----------|
    | 1 | $p_{(1)} = 0.0005$ | 0.001 | **Reject** ($0.0005 \leq 0.001$) |
    | 2 | $p_{(2)} = 0.002$ | 0.001 | Fail to reject ($0.002 > 0.001$) |
    | 3 | $p_{(3)} = 0.015$ | 0.001 | Fail to reject ($0.015 > 0.001$) |

    **Only signal 1 survives the Bonferroni correction.** Signals 2 and 3, which would be significant at the individual 5% level, are no longer significant after adjusting for the 50 simultaneous tests.

    The correction is intuitive: with 50 tests, we expect $50 \times 0.05 = 2.5$ false positives at the uncorrected level. By requiring $p \leq 0.001$, we ensure that the probability of *any* false positive across all 50 tests is at most 0.05. The union bound gives:

    $$
    \text{FWER} \leq \sum_{i \in \mathcal{H}_0} \Pr(p_i \leq 0.001) = m_0 \times 0.001 \leq 50 \times 0.001 = 0.05
    $$

---

**Exercise 2.** Apply the Benjamini-Hochberg (BH) procedure to the same 50 $p$-values from Exercise 1. The BH procedure rejects $H_{(i)}$ for all $i \leq k^*$ where $k^* = \max\{i : p_{(i)} \leq i \cdot \alpha / m\}$. Show that BH rejects more hypotheses than Bonferroni while controlling the false discovery rate at $\alpha = 0.05$.

??? success "Solution to Exercise 2"
    **Benjamini-Hochberg procedure for the same 50 p-values.**

    The BH procedure rejects $H_{(1)}, \ldots, H_{(k^*)}$ where:

    $$
    k^* = \max\!\left\{i : p_{(i)} \leq \frac{i \cdot \alpha}{m}\right\} = \max\!\left\{i : p_{(i)} \leq \frac{i \cdot 0.05}{50}\right\} = \max\!\left\{i : p_{(i)} \leq i \cdot 0.001\right\}
    $$

    Evaluating the BH threshold for each of the three smallest p-values:

    | $i$ | $p_{(i)}$ | BH threshold $i \times 0.001$ | $p_{(i)} \leq$ threshold? |
    |-----|-----------|-------------------------------|---------------------------|
    | 1   | 0.0005    | 0.001                         | Yes                       |
    | 2   | 0.002     | 0.002                         | Yes ($0.002 \leq 0.002$) |
    | 3   | 0.015     | 0.003                         | No ($0.015 > 0.003$)     |

    The largest $i$ for which $p_{(i)} \leq i \cdot 0.001$ is $k^* = 2$.

    **BH rejects signals 1 and 2.** This is strictly more than Bonferroni, which only rejected signal 1.

    **Why BH is more powerful:** The key difference is that BH uses an increasing sequence of thresholds ($0.001, 0.002, 0.003, \ldots$) rather than the fixed Bonferroni threshold ($0.001$). The second signal, with $p_{(2)} = 0.002$, exactly meets the BH threshold of $2 \times 0.001 = 0.002$ but misses the Bonferroni threshold of $0.001$.

    **FDR guarantee:** Under independence (or positive regression dependence) of the p-values:

    $$
    \text{FDR} = \mathbb{E}\!\left[\frac{V}{R \vee 1}\right] \leq \frac{m_0}{m}\alpha \leq \alpha = 0.05
    $$

    The BH procedure controls the *expected proportion* of false discoveries among rejections, rather than the probability of *any* false discovery. This less stringent requirement yields substantially higher power, especially when the number of tests $m$ is large.

---

**Exercise 3.** Harvey, Liu, and Zhu (2016) recommend a minimum $t$-statistic of 3.0 for new factor discoveries. If a researcher claims a new factor with $t = 2.5$ based on 20 years of monthly data, compute the corresponding $p$-value and explain why this evidence is insufficient given the multiple testing problem across decades of factor research. Estimate how many factors have been tested in the finance literature (hint: HLZ estimate over 300).

??? success "Solution to Exercise 3"
    **HLZ threshold and the insufficiency of $t = 2.5$.**

    **$p$-value for $t = 2.5$:** Under a standard normal approximation (appropriate for large samples), the two-sided $p$-value is:

    $$
    p = 2(1 - \Phi(2.5)) = 2 \times (1 - 0.99379) = 2 \times 0.00621 = 0.0124
    $$

    This is significant at the 5% level for a single, pre-specified test. However, the multiple testing problem makes this insufficient.

    **HLZ's estimate of the testing burden.** Harvey, Liu, and Zhu documented over 300 published factors as of 2012, and the true number of tested factors (including unpublished ones) is certainly much larger. A conservative estimate is $m = 300$; a more realistic estimate accounting for unpublished work might be $m = 1000$ or more.

    **Adjusted threshold for $m = 300$:** Using the Bonferroni correction:

    $$
    \frac{\alpha}{m} = \frac{0.05}{300} = 0.0001667
    $$

    The corresponding $t$-statistic threshold is:

    $$
    t_{\text{threshold}} = \Phi^{-1}\!\left(1 - \frac{0.0001667}{2}\right) = \Phi^{-1}(0.9999167) \approx 3.78
    $$

    **Why $t = 2.5$ is insufficient:** The factor's $p$-value of 0.0124 far exceeds the Bonferroni-adjusted threshold of 0.000167. Equivalently, $t = 2.5$ is far below $t_{\text{threshold}} \approx 3.78$. Even under the more lenient HLZ recommendation of $t \geq 3.0$ (which accounts for correlation among tests), $t = 2.5$ falls short.

    With 20 years of monthly data ($T = 240$ observations), the researcher has reasonable statistical power for detecting genuine effects, but the issue is not sample size --- it is the accumulated multiple testing burden across the entire literature. A factor with $t = 2.5$ would be expected to arise roughly:

    $$
    300 \times 0.0124 \approx 3.7 \text{ times}
    $$

    out of 300 tested factors even if *no* factor has genuine predictive power. The evidence is simply consistent with chance.

---

**Exercise 4.** The deflated Sharpe ratio adjusts a backtested Sharpe ratio for the number of trials. If the observed Sharpe ratio is $\hat{SR} = 1.8$ from the best of $N = 100$ strategies, and the strategies are independent, compute the expected maximum Sharpe ratio under the null hypothesis of zero true Sharpe ratios: $\mathbb{E}[\max_i SR_i] \approx \sqrt{2 \log N}$. What is the deflated Sharpe ratio?

??? success "Solution to Exercise 4"
    **Expected maximum Sharpe ratio and the deflated Sharpe ratio.**

    **Setup.** Under the null hypothesis, all $N = 100$ strategies have a true Sharpe ratio of zero. The estimated Sharpe ratios are:

    $$
    \widehat{\text{SR}}_i = \frac{\bar{r}_i}{\hat{\sigma}_i}
    $$

    where $\bar{r}_i$ and $\hat{\sigma}_i$ are the sample mean and standard deviation of strategy $i$'s returns. Under the null, for large $T$, $\sqrt{T}\,\widehat{\text{SR}}_i \sim N(0, 1)$ approximately.

    **Expected maximum.** For $N$ independent standard normal random variables $Z_1, \ldots, Z_N$, the expected maximum satisfies (from extreme value theory):

    $$
    \mathbb{E}\!\left[\max_{i=1,\ldots,N} Z_i\right] \approx \sqrt{2 \log N} - \frac{\log \log N + \log(4\pi)}{2\sqrt{2\log N}}
    $$

    For large $N$, the leading term dominates:

    $$
    \mathbb{E}\!\left[\max_i Z_i\right] \approx \sqrt{2 \log N}
    $$

    With $N = 100$:

    $$
    \mathbb{E}\!\left[\max_i Z_i\right] \approx \sqrt{2 \log 100} = \sqrt{2 \times 4.605} = \sqrt{9.210} \approx 3.035
    $$

    Since $\sqrt{T}\,\widehat{\text{SR}}_i \sim N(0,1)$, the expected maximum Sharpe ratio (annualized) is:

    $$
    \mathbb{E}\!\left[\max_i \widehat{\text{SR}}_i\right] \approx \frac{\sqrt{2 \log N}}{\sqrt{T}}
    $$

    The observed maximum Sharpe is $\hat{\text{SR}} = 1.8$. If we express this in units of $1/\sqrt{T}$, we need to know the sample size $T$. If the strategies are evaluated on $T$ periods (e.g., $T = 120$ months for 10 years of monthly data):

    $$
    \mathbb{E}[\text{max SR under null}] \approx \frac{3.035}{\sqrt{120}} \approx \frac{3.035}{10.95} \approx 0.277
    $$

    **Deflated Sharpe ratio.** The deflation adjusts the observed Sharpe by the expected maximum under the null. One approach is:

    $$
    \text{SR}_{\text{deflated}} = \widehat{\text{SR}} - \mathbb{E}[\text{max SR under null}] = 1.8 - 0.277 = 1.523
    $$

    More formally, the deflated Sharpe ratio tests whether $\hat{\text{SR}}$ significantly exceeds $\text{SR}_0 = \sqrt{2\log N}/\sqrt{T}$:

    $$
    \text{DSR} = \Phi\!\left(\frac{(\widehat{\text{SR}} - \text{SR}_0)\sqrt{T-1}}{\sqrt{1 - \hat{\gamma}_3\,\widehat{\text{SR}} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{\text{SR}}^2}}\right)
    $$

    Assuming normally distributed returns ($\hat{\gamma}_3 = 0$, $\hat{\gamma}_4 = 3$) and $T = 120$:

    $$
    \text{DSR} = \Phi\!\left(\frac{(1.8 - 0.277)\sqrt{119}}{\sqrt{1 + \frac{2}{4}(1.8)^2}}\right) = \Phi\!\left(\frac{1.523 \times 10.91}{\sqrt{1 + 1.62}}\right) = \Phi\!\left(\frac{16.61}{\sqrt{2.62}}\right) = \Phi\!\left(\frac{16.61}{1.618}\right) = \Phi(10.27)
    $$

    This is essentially 1, so with these parameters the strategy would pass the deflated Sharpe test, suggesting it is genuinely profitable even after accounting for 100 trials. However, with more extreme multiple testing ($N$ in the thousands) or shorter samples, the outcome may differ.

---

**Exercise 5.** White's Reality Check tests whether the best strategy in a set significantly outperforms a benchmark. Describe the bootstrap implementation: (a) generate $B = 1000$ bootstrap samples of the strategy returns, (b) compute the test statistic under the null, and (c) compute the $p$-value. How does Hansen's SPA (Superior Predictive Ability) test improve upon White's Reality Check?

??? success "Solution to Exercise 5"
    **White's Reality Check: bootstrap implementation.**

    **Setup.** We have $m$ strategies and $n$ time periods. Strategy $k$ has excess return $d_{k,t}$ over the benchmark at time $t$. The null hypothesis is: no strategy has a positive expected excess return.

    **Test statistic:**

    $$
    T^* = \max_{k=1,\ldots,m} \bar{d}_k, \quad \text{where} \quad \bar{d}_k = \frac{1}{n}\sum_{t=1}^n d_{k,t}
    $$

    **(a) Bootstrap sample generation.** To preserve the contemporaneous cross-sectional correlation among strategies:

    1. Draw $B = 1000$ bootstrap samples. For each bootstrap $b$, sample time indices $\{t_1^{(b)}, \ldots, t_n^{(b)}\}$ with replacement from $\{1, \ldots, n\}$.
    2. For each bootstrap $b$, compute the re-centered excess returns: $\tilde{d}_{k,t}^{(b)} = d_{k,t_s^{(b)}} - \bar{d}_k$ for each strategy $k$ and each sampled time $s$. The re-centering imposes the null hypothesis (zero mean excess return).

    For serially correlated returns, use the **stationary bootstrap** (Politis and Romano, 1994) or **circular block bootstrap** instead of i.i.d. resampling.

    **(b) Null distribution of the test statistic.** For each bootstrap sample $b$:

    $$
    \bar{d}_k^{(b)} = \frac{1}{n}\sum_{s=1}^n \tilde{d}_{k,t_s^{(b)}}^{(b)}, \qquad T^{*(b)} = \max_{k=1,\ldots,m} \bar{d}_k^{(b)}
    $$

    The collection $\{T^{*(1)}, \ldots, T^{*(B)}\}$ approximates the distribution of the maximum average excess return under the null.

    **(c) $p$-value computation:**

    $$
    \hat{p} = \frac{1}{B}\sum_{b=1}^B \mathbf{1}\!\left\{T^{*(b)} \geq T^*\right\}
    $$

    Reject the null if $\hat{p} \leq \alpha$.

    **Hansen's SPA improvement.** Hansen's Superior Predictive Ability test improves upon White's Reality Check in two key ways:

    1. **Studentization:** The SPA test uses the studentized statistic:

        $$
        T^*_{\text{SPA}} = \max_{k=1,\ldots,m} \frac{\bar{d}_k}{\hat{\sigma}_k/\sqrt{n}}
        $$

        where $\hat{\sigma}_k$ is a consistent estimator of the standard deviation of $\bar{d}_k$. This accounts for different volatilities across strategies, giving more weight to strategies with higher $t$-statistics rather than just higher average returns.

    2. **Handling of poor strategies.** White's test includes all $m$ strategies in the maximum, even those that are clearly inferior (strongly negative $\bar{d}_k$). These strategies contribute to the null distribution, making it easier to reject. Hansen's test mitigates this "least favorable configuration" issue by re-centering only strategies close to zero under the null, yielding a test that is both more powerful and more accurate in finite samples.

---

**Exercise 6.** A machine learning pipeline evaluates 1000 feature combinations, 5 model architectures, and 10 hyperparameter settings, yielding $m = 50{,}000$ configurations. The best configuration has a validation Sharpe ratio of 2.0. Is this likely to be a genuine discovery? Compute the expected maximum Sharpe under the null and propose a practical workflow that combines multiple testing correction with out-of-sample validation to guard against false discovery.

??? success "Solution to Exercise 6"
    **Assessing $m = 50{,}000$ configurations with best SR = 2.0.**

    **Expected maximum Sharpe under the null.** With $m = 50{,}000$ independent configurations, each having true Sharpe ratio zero:

    $$
    \mathbb{E}\!\left[\max_{i=1,\ldots,m} \widehat{\text{SR}}_i\right] \approx \frac{\sqrt{2\log m}}{\sqrt{T}}
    $$

    Computing $\sqrt{2\log m}$:

    $$
    \log(50{,}000) = \log(5 \times 10^4) = \log 5 + 4\log 10 \approx 1.609 + 9.210 = 10.819
    $$

    $$
    \sqrt{2 \times 10.819} = \sqrt{21.638} \approx 4.652
    $$

    For $T = 120$ months (10 years):

    $$
    \mathbb{E}[\text{max SR under null}] \approx \frac{4.652}{\sqrt{120}} \approx \frac{4.652}{10.95} \approx 0.425
    $$

    For $T = 60$ months (5 years):

    $$
    \mathbb{E}[\text{max SR under null}] \approx \frac{4.652}{\sqrt{60}} \approx \frac{4.652}{7.746} \approx 0.601
    $$

    **Is SR = 2.0 genuine?** The observed SR of 2.0 substantially exceeds the expected maximum under the null ($\approx 0.4$--$0.6$), suggesting it might be genuine. However, several caveats apply:

    - The 50,000 configurations are **not independent** --- they share features, data, and model components, introducing complex correlation. The effective number of independent tests may be lower than 50,000, but the correlation also means that many configurations are essentially variations of the same idea.
    - The formula above assumes normally distributed returns; fat tails increase the expected maximum.
    - The SR is computed on **validation data**, which itself may have been implicitly used for configuration selection (e.g., through iterative experimentation).

    **Practical workflow to guard against false discovery:**

    1. **Split data into three periods:**
        - **Training** (e.g., years 1--5): Fit models and select features.
        - **Validation** (e.g., years 6--8): Select among configurations. The 50,000-configuration search uses this period.
        - **Test** (e.g., years 9--10): Final evaluation. This period is touched exactly *once*.

    2. **Apply multiple testing correction on the validation set:**
        - Compute the haircut Sharpe ratio: $\text{SR}_{\text{haircut}} = \hat{\text{SR}} - \sqrt{2\log m}/\sqrt{T_{\text{val}}}$.
        - Apply the deflated Sharpe ratio test to check significance.
        - If the haircut SR is not economically meaningful (e.g., below 0.5), discard the strategy.

    3. **Require economic rationale:** Before touching the test set, verify that the selected configuration has a plausible economic mechanism (e.g., momentum, mean-reversion, carry). Pure statistical patterns without economic grounding are more likely to be noise.

    4. **Final out-of-sample evaluation:** Evaluate the single selected configuration on the held-out test period. Report the test-period SR as the unbiased performance estimate. Do *not* go back and change the configuration based on test results.

    5. **Robustness checks:** Test across different markets, asset classes, and subperiods. A genuine strategy should show consistent (if attenuated) performance across environments.

    With $m = 50{,}000$, an observed validation SR of 2.0 is promising but not conclusive. Only the out-of-sample test, combined with economic reasoning, can distinguish genuine predictive power from an artifact of massive search.
