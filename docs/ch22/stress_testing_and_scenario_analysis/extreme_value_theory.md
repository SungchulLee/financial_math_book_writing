# Extreme Value Theory

**Extreme Value Theory (EVT)** provides the mathematical foundation for modeling the tails of loss distributions beyond the range of historical observation. While standard statistical methods fit the bulk of a distribution, EVT focuses on the **asymptotic behavior of maxima and exceedances**, offering principled tools for estimating extreme quantiles (VaR) and tail expectations (ES) at confidence levels far into the tail.

---

## The Block Maxima Approach

### Setting

Let $L_1, L_2, \ldots, L_n$ be i.i.d. losses with common distribution $F$. Define the **block maximum** over $n$ observations:

$$
M_n = \max(L_1, \ldots, L_n)
$$

The distribution of $M_n$ is $F^n(x) = \mathbb{P}(M_n \le x) = F(x)^n$.

### The Fisher-Tippett-Gnedenko Theorem

!!! info "Theorem (Fisher-Tippett-Gnedenko)"
    If there exist normalizing sequences $a_n > 0$ and $b_n \in \mathbb{R}$ such that:

    $$
    \mathbb{P}\left(\frac{M_n - b_n}{a_n} \le x\right) \to G(x) \quad \text{as } n \to \infty
    $$

    for some non-degenerate distribution $G$, then $G$ belongs to the **Generalized Extreme Value (GEV)** family:

    $$
    G_\xi(x) = \exp\left(-(1 + \xi x)^{-1/\xi}\right), \quad 1 + \xi x > 0
    $$

    where $\xi \in \mathbb{R}$ is the **shape parameter** (or tail index).

This is the extreme value analogue of the Central Limit Theorem: just as sums converge to the normal distribution regardless of the underlying distribution, normalized maxima converge to the GEV.

### The Three Types

The shape parameter $\xi$ determines the tail behavior:

| Type | Name | $\xi$ | Tail | Financial Examples |
|------|------|-------|------|-------------------|
| I | Gumbel | $\xi = 0$ | Exponential decay | Normal, lognormal returns |
| II | Frechet | $\xi > 0$ | Heavy (power) tail | Student-$t$, Pareto, financial losses |
| III | Weibull | $\xi < 0$ | Bounded upper tail | Bounded distributions (rare in finance) |

For the **Gumbel case** ($\xi = 0$), the GEV reduces to:

$$
G_0(x) = \exp(-e^{-x})
$$

**Financial relevance:** Most financial return distributions have $\xi > 0$ (Frechet domain), reflecting the empirical observation that loss tails are heavier than normal. Typical estimates for equity returns give $\xi \in [0.1, 0.4]$.

---

## Maximum Domain of Attraction

A distribution $F$ belongs to the **maximum domain of attraction** of $G_\xi$ (written $F \in \text{MDA}(G_\xi)$) if the normalized maxima converge to $G_\xi$.

### Characterization for Heavy Tails ($\xi > 0$)

$F \in \text{MDA}(G_\xi)$ with $\xi > 0$ if and only if:

$$
\bar{F}(x) = 1 - F(x) = x^{-1/\xi} \ell(x)
$$

where $\ell(x)$ is a **slowly varying function** ($\ell(tx)/\ell(x) \to 1$ as $x \to \infty$ for all $t > 0$).

**Examples in the Frechet domain:**

- Student-$t$ with $\nu$ degrees of freedom: $\xi = 1/\nu$
- Pareto distribution: $\xi = 1/\alpha$ where $\alpha$ is the Pareto exponent
- Stable distributions with index $\alpha < 2$: $\xi = 1/\alpha$

### Characterization for Light Tails ($\xi = 0$)

$F \in \text{MDA}(G_0)$ if and only if:

$$
\lim_{t \to x_F} \frac{\bar{F}(t + x \cdot a(t))}{\bar{F}(t)} = e^{-x}
$$

for some positive function $a(t)$, where $x_F = \sup\{x : F(x) < 1\}$.

**Examples:** Normal, exponential, gamma, lognormal.

---

## Peaks-Over-Threshold Method

### Motivation

The block maxima approach wastes data by using only one observation per block. The **Peaks-over-Threshold (POT)** method uses all observations exceeding a high threshold $u$, extracting more information from the tail.

### The Excess Distribution

For a threshold $u$, the **excess distribution** is:

$$
F_u(y) = \mathbb{P}(L - u \le y \mid L > u) = \frac{F(u + y) - F(u)}{1 - F(u)}, \quad y \ge 0
$$

### The Pickands-Balkema-de Haan Theorem

!!! info "Theorem (Pickands-Balkema-de Haan)"
    If $F \in \text{MDA}(G_\xi)$, then there exists a positive function $\beta(u)$ such that:

    $$
    \lim_{u \to x_F} \sup_{0 \le y < x_F - u} \left|F_u(y) - G_{\xi, \beta(u)}(y)\right| = 0
    $$

    where $G_{\xi, \beta}$ is the **Generalized Pareto Distribution (GPD)**:

    $$
    G_{\xi, \beta}(y) = 1 - \left(1 + \xi \frac{y}{\beta}\right)^{-1/\xi}, \quad y \ge 0
    $$

    with $\beta > 0$ (scale) and $1 + \xi y / \beta > 0$.

**Interpretation:** For sufficiently high thresholds, exceedances over $u$ follow the GPD, regardless of the underlying distribution. This is the threshold analogue of the GEV result for block maxima.

### GPD Special Cases

- $\xi > 0$: Heavy tail (Pareto-like), $\mathbb{E}[Y] = \beta/(1 - \xi)$ for $\xi < 1$
- $\xi = 0$: Exponential distribution with mean $\beta$
- $\xi < 0$: Bounded support $[0, -\beta/\xi]$

---

## Tail Risk Estimation with EVT

### VaR Estimation

Combining the GPD tail model with the empirical survival probability above $u$:

$$
\bar{F}(x) \approx \frac{N_u}{n} \left(1 + \hat{\xi} \frac{x - u}{\hat{\beta}}\right)^{-1/\hat{\xi}}
$$

where $N_u$ is the number of exceedances above $u$ and $n$ is the total sample size.

Inverting for the $\alpha$-quantile:

$$
\widehat{\text{VaR}}_\alpha = u + \frac{\hat{\beta}}{\hat{\xi}} \left[\left(\frac{n}{N_u}(1 - \alpha)\right)^{-\hat{\xi}} - 1\right]
$$

This enables estimation of VaR at extreme confidence levels (e.g., 99.9%) where the empirical quantile is unreliable.

### ES Estimation

The Expected Shortfall under the GPD tail model is:

$$
\widehat{\text{ES}}_\alpha = \frac{\widehat{\text{VaR}}_\alpha}{1 - \hat{\xi}} + \frac{\hat{\beta} - \hat{\xi} u}{1 - \hat{\xi}}
$$

valid for $\hat{\xi} < 1$ (finite mean condition).

**Alternative form:**

$$
\widehat{\text{ES}}_\alpha = \frac{\widehat{\text{VaR}}_\alpha + \hat{\beta} - \hat{\xi} u}{1 - \hat{\xi}}
$$

---

## Parameter Estimation

### Maximum Likelihood Estimation

For exceedances $y_1, \ldots, y_{N_u}$ above threshold $u$, the GPD log-likelihood is:

$$
\ell(\xi, \beta) = -N_u \log \beta - \left(\frac{1}{\xi} + 1\right) \sum_{i=1}^{N_u} \log\left(1 + \xi \frac{y_i}{\beta}\right)
$$

MLE provides consistent and asymptotically efficient estimates under regularity conditions ($\xi > -1/2$).

### Hill Estimator

For heavy-tailed distributions ($\xi > 0$), the **Hill estimator** uses the $k$ largest order statistics $L_{(n)} \ge L_{(n-1)} \ge \cdots \ge L_{(n-k+1)}$:

$$
\hat{\xi}_{\text{Hill}} = \frac{1}{k} \sum_{i=1}^{k} \log L_{(n-i+1)} - \log L_{(n-k)}
$$

**Properties:**

- Consistent for $\xi > 0$ as $k \to \infty$ and $k/n \to 0$
- Simple to compute but sensitive to the choice of $k$
- Not applicable for $\xi \le 0$

### Probability-Weighted Moments

The **PWM estimator** provides a robust alternative:

$$
\hat{\xi} = 2 - \frac{\hat{a}_0}{\hat{a}_0 - 2\hat{a}_1}
$$

where $\hat{a}_j = \frac{1}{N_u} \sum_{i=1}^{N_u} \binom{i-1}{j} / \binom{N_u - 1}{j} \cdot y_{(i)}$ are sample probability-weighted moments.

---

## Threshold Selection

### The Bias-Variance Trade-Off

Choosing the threshold $u$ involves a fundamental trade-off:

- **$u$ too low:** GPD approximation is poor (bias), but many exceedances give low variance
- **$u$ too high:** GPD approximation is accurate (low bias), but few exceedances give high variance

### Mean Excess Plot

The **mean excess function** $e(u) = \mathbb{E}[L - u \mid L > u]$ is linear in $u$ for the GPD:

$$
e(u) = \frac{\beta + \xi u}{1 - \xi}, \quad \xi < 1
$$

Plot the empirical mean excess $\hat{e}(u) = \frac{1}{N_u} \sum_{i: L_i > u} (L_i - u)$ against $u$. The threshold should be chosen where the plot becomes approximately linear.

### Stability Plots

Plot $\hat{\xi}(u)$ and $\hat{\beta}(u)$ as functions of the threshold. The appropriate threshold region is where these estimates are stable (approximately constant).

---

## Dependence and Extremes

### Extremal Index

For stationary dependent sequences, the **extremal index** $\theta \in (0, 1]$ measures the clustering of extremes:

$$
\mathbb{P}(M_n \le u_n) \approx F(u_n)^{n\theta}
$$

- $\theta = 1$: no clustering (i.i.d.-like extremes)
- $\theta < 1$: extremes cluster in groups of average size $1/\theta$

For GARCH-type financial returns, $\theta < 1$ is typical, reflecting volatility clustering.

### Declustering

To apply EVT to dependent data:

1. Identify clusters of exceedances (e.g., runs above $u$)
2. Extract cluster maxima
3. Apply GPD to the declustered exceedances
4. Adjust the tail probability by the extremal index: $\bar{F}(x) \approx \theta \cdot (N_u / n) \cdot (1 + \hat{\xi}(x-u)/\hat{\beta})^{-1/\hat{\xi}}$

---

## Application to Financial Risk

### Equity Return Tails

For daily equity returns, typical EVT estimates:

| Parameter | Left Tail (Losses) | Right Tail (Gains) |
|-----------|-------------------|-------------------|
| $\xi$ | 0.2--0.4 | 0.15--0.35 |
| Tail equivalent d.f. $1/\xi$ | 2.5--5.0 | 2.9--6.7 |

The left tail is typically heavier than the right, reflecting the asymmetry of financial losses.

### EVT vs Parametric VaR

At the 99.9% confidence level for a portfolio with daily $\sigma = 1\%$:

| Method | VaR$_{99.9\%}$ |
|--------|----------------|
| Normal | 3.09% |
| Student-$t$ ($\nu = 5$) | 4.03% |
| EVT ($\xi = 0.3$) | 4.8--5.5% |

EVT typically produces higher VaR estimates at extreme confidence levels, reflecting the heavy-tailed nature of financial losses that parametric models may understate.

---

## Key Takeaways

- The Fisher-Tippett-Gnedenko theorem shows that normalized maxima converge to the GEV distribution, with the shape parameter $\xi$ governing tail heaviness
- Financial losses typically belong to the Frechet domain ($\xi > 0$), with heavier tails than the normal distribution
- The Peaks-over-Threshold method with the GPD is more data-efficient than block maxima for tail estimation
- EVT enables extrapolation to extreme quantiles (99.9%+) beyond the range of historical data
- Threshold selection balances bias (too low) against variance (too high), guided by mean excess and stability plots
- Dependence in financial data (volatility clustering) requires declustering with the extremal index
- EVT-based VaR and ES estimates are typically larger than normal or Student-$t$ estimates, providing more conservative tail risk assessment

---

## Further Reading

- McNeil, A., Frey, R., & Embrechts, P. (2015), *Quantitative Risk Management*, 2nd ed.
- Embrechts, P., Kluppelberg, C., & Mikosch, T. (1997), *Modelling Extremal Events for Insurance and Finance*
- Coles, S. (2001), *An Introduction to Statistical Modeling of Extreme Values*
- Pickands, J. (1975), "Statistical Inference Using Extreme Order Statistics"
- Hill, B.M. (1975), "A Simple General Approach to Inference About the Tail of a Distribution"
- Balkema, A.A. & de Haan, L. (1974), "Residual Life Time at Great Age"
