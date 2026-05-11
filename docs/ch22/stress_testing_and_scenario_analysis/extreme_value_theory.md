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

### Characterization for Heavy Tails (ξ > 0)

$F \in \text{MDA}(G_\xi)$ with $\xi > 0$ if and only if:

$$
\bar{F}(x) = 1 - F(x) = x^{-1/\xi} \ell(x)
$$

where $\ell(x)$ is a **slowly varying function** ($\ell(tx)/\ell(x) \to 1$ as $x \to \infty$ for all $t > 0$).

**Examples in the Frechet domain:**

- Student-$t$ with $\nu$ degrees of freedom: $\xi = 1/\nu$
- Pareto distribution: $\xi = 1/\alpha$ where $\alpha$ is the Pareto exponent
- Stable distributions with index $\alpha < 2$: $\xi = 1/\alpha$

### Characterization for Light Tails (ξ = 0)

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

---

## Exercises

**Exercise 1.** A dataset of 2,500 daily losses has 80 exceedances above a threshold $u = 2.5\%$. The GPD fit yields $\hat{\xi} = 0.25$ and $\hat{\beta} = 0.8\%$. Compute the EVT-based estimates of $\text{VaR}_{99\%}$, $\text{VaR}_{99.9\%}$, and $\text{ES}_{99\%}$ using the formulas

$$
\widehat{\text{VaR}}_\alpha = u + \frac{\hat{\beta}}{\hat{\xi}} \left[\left(\frac{n}{N_u}(1 - \alpha)\right)^{-\hat{\xi}} - 1\right]
$$

$$
\widehat{\text{ES}}_\alpha = \frac{\widehat{\text{VaR}}_\alpha + \hat{\beta} - \hat{\xi} u}{1 - \hat{\xi}}
$$

Compare the 99.9% VaR to the normal approximation $\Phi^{-1}(0.999) \cdot \sigma$ where $\sigma = 1\%$.

??? success "Solution to Exercise 1"

    **Given data:**

    - $n = 2500$, $N_u = 80$, $u = 2.5\%$, $\hat{\xi} = 0.25$, $\hat{\beta} = 0.8\%$.

    **Step 1: Compute $\text{VaR}_{99\%}$.**

    Using the EVT VaR formula with $\alpha = 0.99$:

    $$
    \widehat{\text{VaR}}_{0.99} = u + \frac{\hat{\beta}}{\hat{\xi}} \left[\left(\frac{n}{N_u}(1 - \alpha)\right)^{-\hat{\xi}} - 1\right]
    $$

    First compute the inner ratio:

    $$
    \frac{n}{N_u}(1 - \alpha) = \frac{2500}{80}(0.01) = 31.25 \times 0.01 = 0.3125
    $$

    Then raise to the power $-\hat{\xi} = -0.25$:

    $$
    (0.3125)^{-0.25} = \frac{1}{(0.3125)^{0.25}}
    $$

    Since $0.3125 = 5/16$, we have $(0.3125)^{0.25} = (0.3125)^{1/4}$. Computing: $\sqrt{0.3125} \approx 0.5590$, then $\sqrt{0.5590} \approx 0.7477$. Thus $(0.3125)^{-0.25} \approx 1.3374$.

    Now substitute:

    $$
    \widehat{\text{VaR}}_{0.99} = 2.5\% + \frac{0.8\%}{0.25}(1.3374 - 1) = 2.5\% + 3.2\% \times 0.3374 = 2.5\% + 1.08\% = 3.58\%
    $$

    **Step 2: Compute $\text{VaR}_{99.9\%}$.**

    With $\alpha = 0.999$:

    $$
    \frac{n}{N_u}(1 - \alpha) = 31.25 \times 0.001 = 0.03125
    $$

    $$
    (0.03125)^{-0.25} = \frac{1}{(0.03125)^{0.25}}
    $$

    Computing: $\sqrt{0.03125} \approx 0.17678$, then $\sqrt{0.17678} \approx 0.4205$. Thus $(0.03125)^{-0.25} \approx 2.3784$.

    $$
    \widehat{\text{VaR}}_{0.999} = 2.5\% + 3.2\% \times (2.3784 - 1) = 2.5\% + 3.2\% \times 1.3784 = 2.5\% + 4.41\% = 6.91\%
    $$

    **Step 3: Compute $\text{ES}_{99\%}$.**

    $$
    \widehat{\text{ES}}_{0.99} = \frac{\widehat{\text{VaR}}_{0.99} + \hat{\beta} - \hat{\xi} u}{1 - \hat{\xi}} = \frac{3.58\% + 0.8\% - 0.25 \times 2.5\%}{1 - 0.25} = \frac{3.58\% + 0.8\% - 0.625\%}{0.75} = \frac{3.755\%}{0.75} = 5.01\%
    $$

    **Step 4: Comparison with normal approximation.**

    Under the normal model with $\sigma = 1\%$:

    $$
    \text{VaR}_{99.9\%}^{\text{Normal}} = \Phi^{-1}(0.999) \times 1\% = 3.09 \times 1\% = 3.09\%
    $$

    The EVT estimate of $6.91\%$ is more than **twice** the normal estimate of $3.09\%$. This dramatically illustrates how the normal distribution underestimates extreme tail risk. The heavy tail captured by $\hat{\xi} = 0.25$ (implying a power-law tail with index $1/\xi = 4$) produces far larger extreme quantiles than the exponentially decaying normal tail.

---

**Exercise 2.** Show that the mean excess function of the GPD is linear in the threshold. Starting from

$$
e(u) = \mathbb{E}[L - u \mid L > u] = \frac{\beta + \xi u}{1 - \xi}
$$

explain how you would use the mean excess plot to select a threshold $u$ for a POT analysis. Sketch what a mean excess plot looks like for (a) exponentially-tailed data and (b) heavy-tailed data.

??? success "Solution to Exercise 2"

    **Part 1: Proving linearity of the GPD mean excess function.**

    The GPD with parameters $\xi < 1$ and $\beta > 0$ has density (for $\xi \neq 0$):

    $$
    g(y) = \frac{1}{\beta}\left(1 + \xi \frac{y}{\beta}\right)^{-(1/\xi + 1)}
    $$

    and survival function $\bar{G}(y) = \left(1 + \xi y / \beta\right)^{-1/\xi}$.

    For a loss $L$ with survival function $\bar{F}(x)$, the mean excess function at threshold $u$ is:

    $$
    e(u) = \mathbb{E}[L - u \mid L > u]
    $$

    If exceedances above some base threshold follow a GPD with parameters $(\xi, \beta)$, then exceedances above a higher threshold $u$ also follow a GPD (the GPD is threshold-stable). Specifically, if $Y = L - u_0 \sim \text{GPD}(\xi, \beta)$ for exceedances above $u_0$, then for $u > u_0$, the excess $L - u \mid L > u$ follows $\text{GPD}(\xi, \beta + \xi(u - u_0))$. The mean of a GPD with parameters $(\xi, \beta')$ is $\beta'/(1 - \xi)$ for $\xi < 1$. Setting $\beta' = \beta + \xi(u - u_0)$:

    $$
    e(u) = \frac{\beta + \xi(u - u_0)}{1 - \xi} = \frac{\beta - \xi u_0}{1 - \xi} + \frac{\xi}{1 - \xi} u
    $$

    Taking $u_0 = 0$ for simplicity, this gives:

    $$
    e(u) = \frac{\beta + \xi u}{1 - \xi}
    $$

    which is indeed **linear in $u$** with slope $\xi / (1 - \xi)$ and intercept $\beta / (1 - \xi)$.

    **Part 2: Using the mean excess plot for threshold selection.**

    The procedure is:

    1. Compute the empirical mean excess function $\hat{e}(u)$ for a range of thresholds $u$.
    2. Plot $\hat{e}(u)$ against $u$.
    3. Select the lowest threshold $u^*$ above which the plot is approximately linear.

    Below $u^*$, the bulk of the distribution dominates and the GPD approximation is poor. Above $u^*$, the Pickands-Balkema-de Haan theorem ensures the GPD is a good approximation, and linearity should hold.

    **Part 3: Sketching for different tail types.**

    **(a) Exponentially-tailed data** ($\xi = 0$): The mean excess function is constant, $e(u) = \beta / (1 - 0) = \beta$. The mean excess plot is a **horizontal line** for large $u$, reflecting the memoryless property of the exponential distribution.

    **(b) Heavy-tailed data** ($\xi > 0$): The mean excess function is **increasing linearly** with positive slope $\xi/(1 - \xi) > 0$. This means the expected overshoot grows as the threshold increases---a hallmark of heavy tails. The higher you set the threshold, the larger the expected excess beyond it.

    For $\xi < 0$ (bounded tail), the mean excess function would be **decreasing** and eventually reach zero at the upper endpoint of the distribution.

---

**Exercise 3.** The Hill estimator for the tail index is

$$
\hat{\xi}_{\text{Hill}} = \frac{1}{k} \sum_{i=1}^{k} \log L_{(n-i+1)} - \log L_{(n-k)}
$$

Given the 10 largest order statistics: 8.2, 7.1, 6.5, 5.8, 5.3, 4.9, 4.5, 4.2, 3.9, 3.7, compute $\hat{\xi}_{\text{Hill}}$ for $k = 5$ and $k = 9$. Discuss the sensitivity of the estimate to the choice of $k$ and the bias-variance tradeoff involved.

??? success "Solution to Exercise 3"

    **Given:** The 10 largest order statistics (in decreasing order):

    $$
    L_{(n)} = 8.2, \; L_{(n-1)} = 7.1, \; L_{(n-2)} = 6.5, \; L_{(n-3)} = 5.8, \; L_{(n-4)} = 5.3, \; L_{(n-5)} = 4.9, \; L_{(n-6)} = 4.5, \; L_{(n-7)} = 4.2, \; L_{(n-8)} = 3.9, \; L_{(n-9)} = 3.7
    $$

    The Hill estimator is:

    $$
    \hat{\xi}_{\text{Hill}} = \frac{1}{k} \sum_{i=1}^{k} \log L_{(n-i+1)} - \log L_{(n-k)}
    $$

    **Case $k = 5$:**

    The threshold is $L_{(n-5)} = 4.9$, and we use the top 5 observations: 8.2, 7.1, 6.5, 5.8, 5.3.

    $$
    \hat{\xi}_{\text{Hill}} = \frac{1}{5}\left(\log 8.2 + \log 7.1 + \log 6.5 + \log 5.8 + \log 5.3\right) - \log 4.9
    $$

    Computing the logarithms:

    - $\log 8.2 = 2.1041$
    - $\log 7.1 = 1.9601$
    - $\log 6.5 = 1.8718$
    - $\log 5.8 = 1.7579$
    - $\log 5.3 = 1.6677$
    - $\log 4.9 = 1.5892$

    Sum of logs: $2.1041 + 1.9601 + 1.8718 + 1.7579 + 1.6677 = 9.3616$.

    $$
    \hat{\xi}_{\text{Hill}} = \frac{9.3616}{5} - 1.5892 = 1.8723 - 1.5892 = 0.2831
    $$

    **Case $k = 9$:**

    The threshold is $L_{(n-9)} = 3.7$, and we use the top 9 observations: 8.2, 7.1, 6.5, 5.8, 5.3, 4.9, 4.5, 4.2, 3.9.

    Additional logarithms:

    - $\log 4.5 = 1.5041$
    - $\log 4.2 = 1.4351$
    - $\log 3.9 = 1.3610$
    - $\log 3.7 = 1.3083$

    Sum of all 9 logs: $9.3616 + 1.5892 + 1.5041 + 1.4351 + 1.3610 = 15.2510$.

    $$
    \hat{\xi}_{\text{Hill}} = \frac{15.2510}{9} - 1.3083 = 1.6946 - 1.3083 = 0.3863
    $$

    **Discussion of sensitivity and bias-variance tradeoff:**

    The estimate changes substantially from $\hat{\xi} \approx 0.283$ (for $k = 5$) to $\hat{\xi} \approx 0.386$ (for $k = 9$). This illustrates the well-known sensitivity of the Hill estimator to $k$:

    - **Small $k$** (few order statistics): The estimator uses only the most extreme observations, which are most relevant for the tail. However, with few data points, the **variance is high**. The estimate may be noisy.
    - **Large $k$** (many order statistics): More data reduces variance, but observations farther from the extreme tail are included. If the distribution is not exactly Pareto (i.e., the slowly varying function $\ell(x)$ is not constant), this introduces **bias**. The Hill estimator assumes a pure power-law tail, and including sub-tail observations contaminates the estimate.

    In practice, one constructs a **Hill plot** ($\hat{\xi}$ vs. $k$) and looks for a region of stability where the estimate is approximately constant. This stable region represents the best compromise between bias and variance.

---

**Exercise 4.** A Student-$t$ distribution with $\nu$ degrees of freedom belongs to the Frechet maximum domain of attraction with $\xi = 1/\nu$. For $\nu = 4$, compute $\xi$ and the implied tail probability $\mathbb{P}(L > x)$ for large $x$ using the power-law approximation $\bar{F}(x) \sim c \cdot x^{-1/\xi}$. Why does this imply that the fourth moment is infinite? What consequences does this have for risk estimation based on sample kurtosis?

??? success "Solution to Exercise 4"

    **Part 1: Compute $\xi$ for Student-$t$ with $\nu = 4$.**

    For a Student-$t$ distribution with $\nu$ degrees of freedom, the tail index is:

    $$
    \xi = \frac{1}{\nu} = \frac{1}{4} = 0.25
    $$

    **Part 2: Power-law tail approximation.**

    The survival function of the Student-$t$ distribution satisfies:

    $$
    \bar{F}(x) = \mathbb{P}(L > x) \sim c \cdot x^{-\nu} = c \cdot x^{-1/\xi} = c \cdot x^{-4} \quad \text{as } x \to \infty
    $$

    where $c$ is a positive constant. Specifically, for the Student-$t(\nu)$ distribution:

    $$
    c = \frac{\nu^{\nu/2}}{B(\nu/2, 1/2)} \cdot \frac{1}{\nu} = \frac{4^2}{B(2, 1/2) \cdot 4}
    $$

    though the exact constant is less important than the power-law decay rate $x^{-4}$.

    **Part 3: Why the fourth moment is infinite.**

    The $k$-th moment exists if and only if $k < \nu$. For $\nu = 4$:

    $$
    \mathbb{E}[L^k] = \int_0^\infty k x^{k-1} \bar{F}(x) \, dx \sim \int^\infty k x^{k-1} \cdot c x^{-4} \, dx = c k \int^\infty x^{k-5} \, dx
    $$

    This integral converges if and only if $k - 5 < -1$, i.e., $k < 4$. Therefore:

    - $\mathbb{E}[L]$ exists ($k = 1 < 4$)
    - $\mathbb{E}[L^2]$ exists ($k = 2 < 4$), so the variance is finite
    - $\mathbb{E}[L^3]$ exists ($k = 3 < 4$), so skewness is finite
    - $\mathbb{E}[L^4]$ diverges ($k = 4$ is not strictly less than $4$), so the **kurtosis is infinite**

    **Part 4: Consequences for risk estimation based on sample kurtosis.**

    Since the population kurtosis is infinite, the sample kurtosis:

    $$
    \hat{\kappa} = \frac{\frac{1}{n}\sum_{i=1}^n (L_i - \bar{L})^4}{\left(\frac{1}{n}\sum_{i=1}^n (L_i - \bar{L})^2\right)^2}
    $$

    does **not** converge to a finite limit. Instead, $\hat{\kappa}$ grows without bound as $n \to \infty$ (it is an inconsistent estimator of a quantity that does not exist). In practice:

    - Sample kurtosis will fluctuate wildly across samples and time windows
    - Risk measures calibrated using moment-matching (e.g., Cornish-Fisher VaR approximations that use sample kurtosis) will be unreliable
    - Any distributional fit based on matching the fourth moment is fundamentally flawed
    - This motivates the use of EVT, which directly models the tail behavior without requiring finite higher moments

---

**Exercise 5.** Explain the role of the extremal index $\theta$ when applying EVT to GARCH-type financial returns. If a series has $\theta = 0.6$, what is the average cluster size? A POT analysis identifies 100 exceedances, but after declustering (extracting cluster maxima), only 60 remain. Explain how the tail probability estimate changes when accounting for dependence, using the adjusted formula

$$
\bar{F}(x) \approx \theta \cdot \frac{N_u}{n} \cdot \left(1 + \hat{\xi}\frac{x-u}{\hat{\beta}}\right)^{-1/\hat{\xi}}
$$

??? success "Solution to Exercise 5"

    **Part 1: Average cluster size.**

    The extremal index $\theta$ satisfies the relationship:

    $$
    \text{Average cluster size} = \frac{1}{\theta}
    $$

    For $\theta = 0.6$:

    $$
    \text{Average cluster size} = \frac{1}{0.6} \approx 1.67
    $$

    This means that, on average, extreme exceedances occur in clusters of about 1.67 observations. In practical terms, when a large loss occurs, there is roughly a 67% chance that the next observation is also an exceedance (reflecting volatility clustering in GARCH-type returns).

    **Part 2: Declustering.**

    The 100 original exceedances, after declustering (extracting one maximum per cluster), yield 60 independent cluster maxima. This is consistent with $\theta \approx 60/100 = 0.6$, confirming the extremal index estimate. The 60 cluster maxima can be treated as approximately independent for the purpose of GPD fitting.

    **Part 3: Impact on tail probability estimation.**

    **Without accounting for dependence** (naive approach):

    $$
    \bar{F}^{\text{naive}}(x) = \frac{N_u}{n} \left(1 + \hat{\xi}\frac{x-u}{\hat{\beta}}\right)^{-1/\hat{\xi}}
    $$

    This uses $N_u = 100$ exceedances and treats them as independent, overcounting the effective number of independent extreme events.

    **With dependence adjustment:**

    $$
    \bar{F}^{\text{adjusted}}(x) = \theta \cdot \frac{N_u}{n} \cdot \left(1 + \hat{\xi}\frac{x-u}{\hat{\beta}}\right)^{-1/\hat{\xi}}
    $$

    The factor $\theta = 0.6$ reduces the tail probability estimate by 40%. Equivalently, one can use the declustered count $N_u^{\text{declustered}} = 60$ in place of $N_u = 100$:

    $$
    \bar{F}^{\text{adjusted}}(x) = \frac{N_u^{\text{declustered}}}{n} \cdot \left(1 + \hat{\xi}\frac{x-u}{\hat{\beta}}\right)^{-1/\hat{\xi}}
    $$

    since $\theta \cdot N_u / n = 0.6 \times 100 / n = 60 / n = N_u^{\text{declustered}} / n$.

    **Interpretation:** The naive approach overestimates the probability of exceeding any given level because it treats clustered exceedances as independent events. The adjusted formula correctly accounts for the fact that many of the 100 exceedances are part of the same volatility cluster and do not represent independent extreme events. For VaR estimation, using the naive (higher) exceedance rate would **underestimate** VaR (since a higher tail probability for the same threshold means the quantile at a given confidence level is lower), while the adjusted approach gives a more accurate (and typically higher) VaR estimate.

    **Role of $\theta$ in GARCH-type models:** GARCH processes exhibit volatility clustering, so large losses tend to occur in bursts. The extremal index captures this clustering: $\theta < 1$ indicates that extremes are not independent. Ignoring this dependence leads to biased tail risk estimates. The declustering procedure (runs declustering or blocks declustering) extracts approximately independent extreme events, enabling valid application of the GPD.

---

**Exercise 6.** Prove that the GEV distribution $G_\xi(x) = \exp(-(1 + \xi x)^{-1/\xi})$ reduces to the Gumbel distribution $G_0(x) = \exp(-e^{-x})$ as $\xi \to 0$. (Hint: Use the fact that $\lim_{\xi \to 0}(1 + \xi x)^{1/\xi} = e^x$.)

??? success "Solution to Exercise 6"

    **Goal:** Show that $\lim_{\xi \to 0} G_\xi(x) = G_0(x) = \exp(-e^{-x})$.

    Starting from the GEV distribution:

    $$
    G_\xi(x) = \exp\left(-(1 + \xi x)^{-1/\xi}\right)
    $$

    We need to evaluate $\lim_{\xi \to 0}(1 + \xi x)^{-1/\xi}$.

    **Step 1:** Consider the expression $(1 + \xi x)^{1/\xi}$. Take the logarithm:

    $$
    \frac{1}{\xi} \log(1 + \xi x)
    $$

    **Step 2:** Apply the Taylor expansion $\log(1 + u) = u - u^2/2 + O(u^3)$ with $u = \xi x$:

    $$
    \frac{1}{\xi} \log(1 + \xi x) = \frac{1}{\xi}\left(\xi x - \frac{(\xi x)^2}{2} + O(\xi^3)\right) = x - \frac{\xi x^2}{2} + O(\xi^2)
    $$

    **Step 3:** As $\xi \to 0$:

    $$
    \frac{1}{\xi} \log(1 + \xi x) \to x
    $$

    Therefore:

    $$
    (1 + \xi x)^{1/\xi} \to e^x \quad \text{as } \xi \to 0
    $$

    **Step 4:** The exponent in the GEV is $-(1 + \xi x)^{-1/\xi} = -\frac{1}{(1+\xi x)^{1/\xi}}$, so:

    $$
    -(1 + \xi x)^{-1/\xi} \to -\frac{1}{e^x} = -e^{-x}
    $$

    **Step 5:** Substituting back:

    $$
    \lim_{\xi \to 0} G_\xi(x) = \exp(-e^{-x}) = G_0(x)
    $$

    This confirms that the Gumbel distribution is the limiting case of the GEV family as $\xi \to 0$, providing a continuous bridge between the Frechet ($\xi > 0$) and Weibull ($\xi < 0$) types. $\square$

---

**Exercise 7.** A risk manager must choose between a parametric Student-$t$ VaR model and an EVT-based POT model. For a 99% VaR with 1,000 observations, both methods perform similarly. Discuss why the two approaches may diverge significantly at the 99.97% level (Basel's 3-year return period). Under what conditions would you recommend the EVT approach over the parametric approach, and what are the key practical challenges (threshold selection, data requirements, stationarity assumptions)?

??? success "Solution to Exercise 7"

    **Part 1: Why the two approaches diverge at extreme confidence levels.**

    At the 99% level with 1,000 observations, there are approximately 10 observations in the tail beyond the VaR threshold. Both methods have reasonable data support:

    - The Student-$t$ model fits the entire distribution, including the tail, parametrically.
    - The EVT/POT model focuses specifically on exceedances above a high threshold.

    At the 99.97% level (corresponding to Basel's 3-year return period, since $1 - 0.9997 = 0.0003$ and $1/0.0003 \approx 3333$ days $\approx 13$ years), with 1,000 daily observations there are essentially **zero** observations beyond this quantile. Both methods must extrapolate, but they extrapolate differently:

    - **Student-$t$:** Assumes the *entire* distribution is Student-$t$ with a fixed degrees-of-freedom parameter $\nu$ estimated from the full sample. The tail behavior is determined by the global fit. If the true tail is heavier or lighter than Student-$t$ in the extreme, the parametric model is misspecified.
    - **EVT/POT:** Models only the tail region above threshold $u$, fitting $\xi$ and $\beta$ to exceedances. It makes no assumptions about the bulk of the distribution. The GPD extrapolation is justified by the Pickands-Balkema-de Haan theorem and is asymptotically correct regardless of the underlying distribution (as long as it belongs to some MDA).

    The divergence arises because the Student-$t$ tail decay rate $x^{-\nu}$ is determined by $\nu$, which is influenced by the bulk of the data, while the EVT tail index $\xi$ is estimated from tail data alone. If the true tail is heavier than implied by the global Student-$t$ fit, EVT will give a higher (more conservative) VaR. Conversely, if the Student-$t$ overfits a few extreme observations, it may overestimate tail risk relative to EVT.

    **Part 2: When to recommend EVT over the parametric approach.**

    EVT is preferred when:

    - **Extreme confidence levels** are required (99.9%+), where the parametric model's global fit may not accurately represent the tail.
    - **The distribution is not well approximated by any single parametric family** over its entire range (e.g., the body may be approximately normal but the tail is power-law).
    - **Sufficient data** exists to reliably estimate the GPD parameters (typically at least 50--100 exceedances above the threshold).
    - **Regulatory requirements** demand extreme quantile estimation (Basel 99.97% for specific risk).

    The parametric approach may be preferred when:

    - Data is very limited (fewer than 500--1000 observations), making threshold selection and GPD estimation unreliable.
    - The confidence level is moderate (95--99%), where the parametric model has adequate data support.
    - The distribution is known to follow a specific parametric form from theoretical considerations.

    **Part 3: Key practical challenges of EVT.**

    1. **Threshold selection:** The bias-variance tradeoff is fundamental. Too low a threshold violates the GPD approximation (bias); too high a threshold leaves too few exceedances (variance). Tools like the mean excess plot and stability plots help, but the choice remains partly subjective.

    2. **Data requirements:** Reliable GPD estimation typically requires at least 50--100 exceedances. For daily data, this means at least 2--5 years of observations even with a moderate threshold (top 5--10% of losses).

    3. **Stationarity:** EVT assumes the underlying distribution is stationary (or at least that the tail behavior is stable). Financial data exhibits volatility clustering, seasonal effects, and regime changes. Violations can be partially addressed by declustering (using the extremal index) or by applying EVT to GARCH-standardized residuals.

    4. **Dependence:** The i.i.d. assumption underlying the Pickands-Balkema-de Haan theorem is violated by serially dependent financial returns. Declustering and the extremal index are necessary adjustments.

    5. **Estimation uncertainty:** Confidence intervals for extreme quantiles (99.9%+) are wide even with EVT, reflecting the fundamental difficulty of extrapolating into regions with little or no data. Profile likelihood methods can provide confidence intervals for EVT-based VaR.
