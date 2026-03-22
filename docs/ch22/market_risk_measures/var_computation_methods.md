# VaR Computation Methods

Computing Value-at-Risk requires estimating a quantile of the portfolio loss distribution. The three principal methods -- **historical simulation**, **parametric (variance-covariance)**, and **Monte Carlo simulation** -- represent fundamentally different approaches to this estimation problem, each with distinct statistical properties, computational costs, and model risk profiles.

---

## Setup and Notation

Let $\mathbf{R}_t = (R_{1,t}, \ldots, R_{d,t})^\top$ denote the vector of $d$ risk factor returns on day $t$, and let $L_t = -\mathbf{w}^\top \mathbf{R}_t$ be the portfolio loss for weight vector $\mathbf{w}$. We seek $\text{VaR}_\alpha(L)$ at confidence level $\alpha$ (typically 0.95 or 0.99) over a holding period $h$.

For a general (possibly nonlinear) portfolio value function $P(\mathbf{x})$ depending on risk factors $\mathbf{x}$, the loss from an initial state $\mathbf{x}_0$ is:

$$
L = P(\mathbf{x}_0) - P(\mathbf{x}_0 + \Delta\mathbf{x})
$$

where $\Delta\mathbf{x}$ is the change in risk factors over the holding period.

---

## Historical Simulation

### Method

Historical simulation estimates VaR directly from past realized losses, without imposing any distributional assumptions.

Given $n$ historical return vectors $\{\mathbf{R}_1, \ldots, \mathbf{R}_n\}$, compute the corresponding losses:

$$
L_i = -\mathbf{w}^\top \mathbf{R}_i, \quad i = 1, \ldots, n
$$

Order the losses $L_{(1)} \le L_{(2)} \le \cdots \le L_{(n)}$ and estimate:

$$
\widehat{\text{VaR}}_\alpha = L_{(\lceil n\alpha \rceil)}
$$

where $\lceil \cdot \rceil$ denotes the ceiling function.

### Full Revaluation

For portfolios with nonlinear payoffs (options, structured products), historical simulation uses **full revaluation**: apply each historical scenario to the current portfolio and reprice:

$$
L_i = P(\mathbf{x}_0) - P(\mathbf{x}_0 + \Delta\mathbf{x}_i), \quad i = 1, \ldots, n
$$

This captures gamma and vega effects that linear approximations miss.

### Statistical Properties

The estimator $\widehat{\text{VaR}}_\alpha$ is the sample quantile, which is asymptotically normal:

$$
\sqrt{n}\left(\widehat{\text{VaR}}_\alpha - \text{VaR}_\alpha\right) \xrightarrow{d} N\left(0, \frac{\alpha(1-\alpha)}{f_L(\text{VaR}_\alpha)^2}\right)
$$

where $f_L$ is the density of $L$ at the true quantile. The variance is inversely proportional to $f_L(\text{VaR}_\alpha)^2$: estimation is less precise when the density is low at the quantile, which is precisely the case for extreme quantiles in the tail.

**Advantages:**

- No distributional assumptions (nonparametric)
- Automatically captures fat tails, skewness, and cross-asset dependence present in historical data
- Simple to implement and explain

**Limitations:**

- Requires sufficient historical data (typically 250--500+ observations)
- Assumes stationarity: past returns are representative of future risk
- Ghost effects: a single extreme event enters and exits the window, causing VaR jumps
- Cannot extrapolate beyond observed historical scenarios

---

## Filtered Historical Simulation

### Motivation

Standard historical simulation ignores time-varying volatility. During calm periods it overestimates risk; during turbulent periods it underestimates risk.

### Method

**Filtered historical simulation** (Barone-Adesi, Giannopoulos, and Vosper, 1999) standardizes returns by conditional volatility:

1. Fit a GARCH(1,1) model to each risk factor:

$$
\sigma_{j,t}^2 = \omega_j + \alpha_j R_{j,t-1}^2 + \beta_j \sigma_{j,t-1}^2
$$

2. Compute standardized residuals:

$$
\epsilon_{j,t} = \frac{R_{j,t}}{\sigma_{j,t}}, \quad j = 1, \ldots, d
$$

3. Resample from the empirical distribution of $\{\boldsymbol{\epsilon}_1, \ldots, \boldsymbol{\epsilon}_n\}$ and rescale by current volatility:

$$
\widetilde{R}_{j,t} = \sigma_{j,T+1} \cdot \epsilon_{j,t}
$$

where $\sigma_{j,T+1}$ is the current conditional volatility forecast.

4. Compute portfolio losses from the rescaled scenarios and take the $\alpha$-quantile.

This adapts historical simulation to the current volatility regime while preserving the empirical distribution of standardized innovations, including fat tails and cross-asset dependence.

---

## Parametric (Variance-Covariance) Method

### Setup

Assume portfolio returns are multivariate normal:

$$
\mathbf{R} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})
$$

The portfolio loss $L = -\mathbf{w}^\top \mathbf{R}$ is then normally distributed:

$$
L \sim N(-\mathbf{w}^\top \boldsymbol{\mu}, \, \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w})
$$

### VaR Formula

$$
\text{VaR}_\alpha = -\mathbf{w}^\top \boldsymbol{\mu} + \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}} \cdot \Phi^{-1}(\alpha)
$$

where $\Phi^{-1}$ is the standard normal quantile function.

For short horizons where the mean is negligible ($\boldsymbol{\mu} \approx \mathbf{0}$):

$$
\text{VaR}_\alpha \approx \sigma_P \cdot \Phi^{-1}(\alpha), \quad \sigma_P = \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}
$$

### Component VaR

The **marginal contribution** of asset $i$ to portfolio VaR is:

$$
\text{CVaR}_i = w_i \cdot \frac{(\boldsymbol{\Sigma} \mathbf{w})_i}{\sigma_P} \cdot \Phi^{-1}(\alpha)
$$

By Euler's theorem for homogeneous functions:

$$
\sum_{i=1}^d \text{CVaR}_i = \text{VaR}_\alpha
$$

This decomposition enables risk attribution across portfolio components.

### Extensions Beyond Normality

The variance-covariance framework extends to non-normal distributions:

- **Student-$t$ returns:** Replace $\Phi^{-1}(\alpha)$ with $t_\nu^{-1}(\alpha) \cdot \sqrt{(\nu - 2)/\nu}$
- **Cornish-Fisher expansion:** Adjust for skewness $\mu_3$ and excess kurtosis $\mu_4$:

$$
z_\alpha^{\text{CF}} = z_\alpha + \frac{1}{6}(z_\alpha^2 - 1)\mu_3 + \frac{1}{24}(z_\alpha^3 - 3z_\alpha)\mu_4 - \frac{1}{36}(2z_\alpha^3 - 5z_\alpha)\mu_3^2
$$

where $z_\alpha = \Phi^{-1}(\alpha)$.

**Advantages:**

- Computationally efficient: closed-form for linear portfolios
- Easy to implement for large portfolios
- Natural decomposition into component contributions

**Limitations:**

- Normality assumption typically violated (fat tails, skewness)
- Underestimates tail risk for non-normal distributions
- Fails for portfolios with significant nonlinearities (options)

---

## Monte Carlo Simulation

### Algorithm

Monte Carlo VaR generates simulated scenarios from a specified stochastic model:

1. **Specify the model:** Choose dynamics for risk factors (e.g., GBM, stochastic volatility, jump-diffusion)
2. **Calibrate parameters:** Estimate from historical data or market prices
3. **Simulate $N$ scenarios:** Generate $\{\Delta\mathbf{x}^{(1)}, \ldots, \Delta\mathbf{x}^{(N)}\}$ from the model
4. **Compute portfolio losses:** $L^{(j)} = P(\mathbf{x}_0) - P(\mathbf{x}_0 + \Delta\mathbf{x}^{(j)})$ for $j = 1, \ldots, N$
5. **Estimate VaR:** $\widehat{\text{VaR}}_\alpha = L_{(\lceil N\alpha \rceil)}$

### Convergence

The Monte Carlo VaR estimator converges at rate $O(1/\sqrt{N})$. The standard error of the estimated quantile is approximately:

$$
\text{SE}(\widehat{\text{VaR}}_\alpha) \approx \frac{\sqrt{\alpha(1-\alpha)}}{\sqrt{N} \cdot f_L(\text{VaR}_\alpha)}
$$

For $\alpha = 0.99$ and $N = 10{,}000$, the relative standard error can be substantial, motivating variance reduction.

### Variance Reduction Techniques

- **Antithetic variates:** For each simulated $\Delta\mathbf{x}^{(j)}$, also use $-\Delta\mathbf{x}^{(j)}$
- **Importance sampling:** Shift the sampling distribution toward the tail region

$$
\widehat{\text{VaR}}_\alpha^{\text{IS}} = L_{(\lceil N\alpha' \rceil)}^{\text{IS}}, \quad \text{with likelihood ratio weights } \frac{f(\Delta\mathbf{x})}{g(\Delta\mathbf{x})}
$$

- **Stratified sampling:** Partition the probability space and sample proportionally from each stratum
- **Control variates:** Use a correlated random variable with known expectation to reduce variance

### Delta-Gamma Approximation

For computational efficiency, approximate portfolio losses using a Taylor expansion:

$$
L \approx -\boldsymbol{\delta}^\top \Delta\mathbf{x} - \frac{1}{2} \Delta\mathbf{x}^\top \boldsymbol{\Gamma} \Delta\mathbf{x}
$$

where $\boldsymbol{\delta} = \nabla P$ is the delta vector and $\boldsymbol{\Gamma} = \nabla^2 P$ is the gamma matrix. This avoids full revaluation at each scenario while capturing second-order effects.

**Advantages:**

- Handles any distribution, any payoff nonlinearity
- Can incorporate complex dynamics (stochastic volatility, jumps, correlation)
- Flexible: easily extended to new models or products

**Limitations:**

- Computationally intensive: $N \times M$ pricing evaluations (scenarios times instruments)
- Model-dependent: results only as good as the assumed model
- Slow convergence for extreme quantiles

---

## Comparison of Methods

| Feature | Historical Simulation | Parametric | Monte Carlo |
|---------|----------------------|------------|-------------|
| Distributional assumption | None | Explicit (e.g., normal) | Model-specified |
| Nonlinear instruments | Full revaluation | Poor (unless delta-gamma) | Full revaluation |
| Tail accuracy | Limited by data | Depends on distribution | Flexible |
| Computational cost | Low | Very low | High |
| Volatility clustering | Ignored (unless filtered) | Captured if GARCH used | Model-dependent |
| Model risk | Low (data-driven) | High (distribution choice) | Medium (model choice) |
| Extrapolation beyond data | No | Yes | Yes |

---

## Backtesting VaR Models

### Framework

VaR backtesting compares predicted exceedances against realized outcomes. Define the **hit sequence**:

$$
I_t = \mathbf{1}_{L_t > \widehat{\text{VaR}}_{\alpha,t}}
$$

Under a correctly specified model, $\{I_t\}$ should be i.i.d. Bernoulli with $\mathbb{E}[I_t] = 1 - \alpha$.

### Kupiec Unconditional Coverage Test

The **Kupiec test** checks whether the observed exceedance rate $\hat{p} = n_1/n$ matches the expected rate $p = 1 - \alpha$:

$$
LR_{\text{uc}} = -2 \ln \frac{(1-p)^{n_0} p^{n_1}}{\hat{p}^{n_1}(1-\hat{p})^{n_0}} \sim \chi^2(1)
$$

where $n_1$ is the number of exceedances and $n_0 = n - n_1$.

### Christoffersen Independence Test

The **Christoffersen test** checks whether exceedances are serially independent by testing $\pi_{01} = \pi_{11}$, where $\pi_{ij} = \mathbb{P}(I_t = j \mid I_{t-1} = i)$:

$$
LR_{\text{ind}} = -2 \ln \frac{\hat{p}^{n_1}(1-\hat{p})^{n_0}}{\hat{\pi}_{01}^{n_{01}}(1-\hat{\pi}_{01})^{n_{00}} \hat{\pi}_{11}^{n_{11}}(1-\hat{\pi}_{11})^{n_{10}}} \sim \chi^2(1)
$$

### Conditional Coverage Test

The **combined test** checks both unconditional coverage and independence:

$$
LR_{\text{cc}} = LR_{\text{uc}} + LR_{\text{ind}} \sim \chi^2(2)
$$

### Basel Traffic Light System

The Basel Committee classifies internal VaR models by the number of exceedances over 250 trading days at 99% confidence:

| Zone | Exceedances | Multiplier $k$ | Interpretation |
|------|-------------|----------------|----------------|
| Green | 0--4 | 3.0 | Model acceptable |
| Yellow | 5--9 | $3.0 + 0.2 \times (\text{exc} - 4)$ | Model questionable |
| Red | $\ge 10$ | 4.0 | Model inadequate |

The expected number of exceedances is $250 \times 0.01 = 2.5$, so up to 4 is within normal sampling variation.

---

## Example: Three-Asset Portfolio

Consider a portfolio with three assets and daily returns over $n = 500$ days. Suppose we estimate $\boldsymbol{\mu} = \mathbf{0}$ and:

$$
\boldsymbol{\Sigma} = \begin{pmatrix} 0.0004 & 0.0001 & 0.00005 \\ 0.0001 & 0.0009 & 0.0002 \\ 0.00005 & 0.0002 & 0.0016 \end{pmatrix}
$$

with equal weights $\mathbf{w} = (1/3, 1/3, 1/3)^\top$.

**Parametric VaR (99%):**

$$
\sigma_P = \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}} = \sqrt{\frac{1}{9}(0.0004 + 0.0009 + 0.0016 + 2(0.0001 + 0.00005 + 0.0002)}}
$$

$$
= \sqrt{\frac{1}{9} \times 0.0040} \approx 0.0211
$$

$$
\text{VaR}_{0.99} = 0.0211 \times 2.326 \approx 4.91\%
$$

For a \$10M portfolio, this is approximately \$491,000.

**Historical simulation** would sort the 500 observed portfolio losses and report $L_{(495)}$.

**Monte Carlo** would simulate, say, 10,000 scenarios from $N(\mathbf{0}, \boldsymbol{\Sigma})$, compute 10,000 portfolio losses, and report the 9,900th ordered loss.

---

## Multi-Day VaR and the Square-Root-of-Time Rule

For a holding period of $h$ days, under i.i.d. returns:

$$
\text{VaR}_\alpha(h) = \sqrt{h} \cdot \text{VaR}_\alpha(1)
$$

This **square-root-of-time rule** is exact under normality but approximate otherwise. It systematically underestimates multi-day VaR when:

- Returns exhibit **volatility clustering** (GARCH effects)
- Returns have **fat tails** (heavier than normal)
- Returns are **autocorrelated**

For regulatory 10-day VaR: $\text{VaR}_{0.99}^{10\text{-day}} \approx \sqrt{10} \cdot \text{VaR}_{0.99}^{1\text{-day}} \approx 3.16 \cdot \text{VaR}_{0.99}^{1\text{-day}}$.

---

## Key Takeaways

- Historical simulation is nonparametric but assumes stationarity; filtered historical simulation adapts to current volatility
- Parametric VaR is fast and analytically tractable but relies on distributional assumptions that typically understate tail risk
- Monte Carlo VaR is the most flexible method but computationally expensive with slow convergence for extreme quantiles
- Backtesting via Kupiec (coverage), Christoffersen (independence), and combined tests validates model adequacy
- The Basel traffic light system penalizes models with excessive exceedances through increased capital multipliers
- No single method dominates: the choice involves trade-offs among model risk, computational cost, and tail accuracy

---

## Further Reading

- Jorion, P., *Value at Risk: The New Benchmark for Managing Financial Risk*
- McNeil, A., Frey, R., & Embrechts, P., *Quantitative Risk Management*
- Barone-Adesi, G., Giannopoulos, K., & Vosper, L. (1999), "VaR Without Correlations for Portfolios of Derivative Securities"
- Christoffersen, P. (1998), "Evaluating Interval Forecasts," *International Economic Review*
- Kupiec, P. (1995), "Techniques for Verifying the Accuracy of Risk Measurement Models"
- Glasserman, P., *Monte Carlo Methods in Financial Engineering*
