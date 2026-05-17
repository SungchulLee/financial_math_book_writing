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

Recall (see [§ Value-at-Risk](value_at_risk_var.md)) the square-root-of-time rule $\text{VaR}_\alpha(h) \approx \sqrt{h}\,\text{VaR}_\alpha(1)$, exact under i.i.d. normal returns and prone to underestimation under volatility clustering, fat tails, or serial correlation. For regulatory 10-day VaR the factor is $\sqrt{10} \approx 3.16$.

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

---

## Exercises

**Exercise 1.** Describe the three principal methods for computing VaR: historical simulation, parametric (variance-covariance), and Monte Carlo simulation. For each method, state one key advantage and one key limitation.

??? success "Solution to Exercise 1"

    **The three principal methods for computing VaR:**

    **1. Historical Simulation:**

    - Uses the empirical distribution of past portfolio losses directly.
    - Order $n$ historical losses and take the $\lceil n\alpha \rceil$-th value as $\widehat{\text{VaR}}_\alpha$.
    - **Key advantage:** Model-free (nonparametric). Automatically captures fat tails, skewness, and complex dependence without imposing distributional assumptions.
    - **Key limitation:** Assumes stationarity -- past returns must be representative of future risk. Cannot extrapolate beyond the range of observed data, and suffers from the "ghost effect" when extreme observations enter or leave the estimation window.

    **2. Parametric (Variance-Covariance) Method:**

    - Assumes returns follow a multivariate normal (or other parametric) distribution.
    - Computes $\text{VaR}_\alpha = -\mathbf{w}^\top\boldsymbol{\mu} + \sqrt{\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}} \cdot \Phi^{-1}(\alpha)$.
    - **Key advantage:** Computationally efficient with a closed-form expression. Natural decomposition into component VaR for risk attribution.
    - **Key limitation:** The normality assumption is typically violated in practice. Fat tails, skewness, and nonlinear payoffs (options) cause systematic underestimation of tail risk.

    **3. Monte Carlo Simulation:**

    - Specifies a stochastic model for risk factors, simulates $N$ scenarios, computes portfolio losses via full revaluation, and estimates VaR as the empirical quantile.
    - **Key advantage:** Maximum flexibility -- handles any distribution, nonlinear instruments (options), path-dependent payoffs, and complex dynamics (stochastic volatility, jumps).
    - **Key limitation:** Computationally expensive (requires $N \times M$ portfolio valuations for $N$ scenarios and $M$ instruments). Results are model-dependent, and convergence is slow for extreme quantiles ($O(1/\sqrt{N})$).

---

**Exercise 2.** A portfolio of two assets has weights $w_1 = 0.6$, $w_2 = 0.4$, daily volatilities $\sigma_1 = 2\%$, $\sigma_2 = 3\%$, and correlation $\rho = 0.5$. Using the parametric method, compute the portfolio's daily standard deviation and the 99% VaR for a \$100M portfolio.

??? success "Solution to Exercise 2"

    **Given:** $w_1 = 0.6$, $w_2 = 0.4$, $\sigma_1 = 2\% = 0.02$, $\sigma_2 = 3\% = 0.03$, $\rho = 0.5$, portfolio value $= \$100\text{M}$.

    **Step 1: Compute the portfolio variance.**

    $$
    \sigma_P^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho \sigma_1 \sigma_2
    $$

    $$
    = (0.6)^2(0.02)^2 + (0.4)^2(0.03)^2 + 2(0.6)(0.4)(0.5)(0.02)(0.03)
    $$

    $$
    = 0.36 \times 0.0004 + 0.16 \times 0.0009 + 2 \times 0.6 \times 0.4 \times 0.5 \times 0.0006
    $$

    $$
    = 0.000144 + 0.000144 + 0.000144 = 0.000432
    $$

    **Step 2: Compute the portfolio standard deviation.**

    $$
    \sigma_P = \sqrt{0.000432} = 0.02078 = 2.078\%
    $$

    **Step 3: Compute the 99% VaR.**

    With $\Phi^{-1}(0.99) = 2.326$ and assuming $\mu \approx 0$:

    $$
    \text{VaR}_{0.99} = \sigma_P \times \Phi^{-1}(0.99) = 0.02078 \times 2.326 = 0.04834 = 4.834\%
    $$

    **In dollar terms:**

    $$
    \text{VaR}_{0.99} = 4.834\% \times \$100\text{M} = \$4.834\text{M}
    $$

    **Note on diversification benefit:** The undiversified VaR (sum of individual VaRs) would be:

    $$
    w_1 \sigma_1 \Phi^{-1}(0.99) + w_2 \sigma_2 \Phi^{-1}(0.99) = (0.6 \times 0.02 + 0.4 \times 0.03) \times 2.326 = 0.024 \times 2.326 = 5.582\%
    $$

    The diversification benefit is $5.582\% - 4.834\% = 0.748\%$, or approximately \$748K in capital savings.

---

**Exercise 3.** Historical simulation uses 500 days of return data. Explain the "ghost effect": when a large loss drops out of the estimation window, the VaR can change abruptly even if recent market conditions are stable. Propose a remedy using exponentially weighted returns.

??? success "Solution to Exercise 3"

    **The ghost effect:**

    When using a rolling window of $n = 500$ days for historical simulation:

    - Each day, the oldest observation drops out and a new one enters the window.
    - If the observation dropping out is an extreme loss (say, from a market crash 500 days ago), the VaR can suddenly decrease significantly, even if recent market conditions are unchanged.
    - Conversely, when a new extreme loss enters the window, VaR jumps up abruptly.

    **Example:** Suppose the 5th largest loss in the window is \$15M and the 6th largest is \$8M (for 99% VaR with 500 observations, VaR is the 5th largest loss). If the current 5th largest loss drops out of the window, VaR suddenly falls from \$15M to \$8M -- a large discontinuous change unrelated to current market dynamics.

    This creates **artificial volatility** in the VaR estimate and undermines its reliability as a risk management tool.

    **Remedy: Exponentially Weighted Historical Simulation**

    Instead of equal weights on all observations, assign exponentially decaying weights:

    $$
    w_i = \frac{\lambda^{n-i}(1-\lambda)}{1-\lambda^n}, \quad i = 1, \ldots, n
    $$

    where $\lambda \in (0,1)$ is the decay factor (typically $\lambda = 0.94$ to $0.99$).

    **Implementation:**

    1. Assign weights $w_i$ to each historical loss $L_i$, with more recent observations receiving higher weight.
    2. Sort losses and accumulate the weights until the cumulative weight reaches $\alpha$.
    3. The VaR is the loss at which the cumulative weight crosses $\alpha$.

    **Benefits:**

    - Old observations gradually fade out rather than abruptly disappearing, eliminating the ghost effect.
    - Recent data (which better reflects current market conditions) receives more influence.
    - The method adapts to changing volatility regimes, somewhat like filtered historical simulation but without explicitly fitting a GARCH model.
    - The parameter $\lambda$ controls the effective window length: smaller $\lambda$ means faster decay and a shorter effective window.

    **Trade-off:** Very small $\lambda$ leads to high sensitivity to recent events and an effectively small sample size, increasing estimation noise. The choice of $\lambda$ balances responsiveness against estimation stability.

---

**Exercise 4.** Monte Carlo VaR requires specifying a model for the joint distribution of risk factors. Describe the steps: (a) calibrate the model, (b) simulate $N$ scenarios, (c) revalue the portfolio under each scenario, (d) compute the $\alpha$-quantile of losses. How many simulations are typically needed for stable 99% VaR estimates?

??? success "Solution to Exercise 4"

    **Steps for Monte Carlo VaR:**

    **(a) Calibrate the model:**

    - Choose a model for the joint dynamics of $d$ risk factors (e.g., correlated geometric Brownian motions, Heston stochastic volatility, jump-diffusion).
    - Estimate parameters from historical data (volatilities, correlations, mean reversion speeds, jump intensities) or calibrate to market prices (implied volatilities, option prices).
    - Example: For a multivariate normal model, estimate $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ from historical returns. For Heston, calibrate $\kappa$, $\theta$, $\xi$, $\rho$, $v_0$ to the implied volatility surface.

    **(b) Simulate $N$ scenarios:**

    - Generate $N$ independent draws of the risk factor changes $\{\Delta\mathbf{x}^{(1)}, \ldots, \Delta\mathbf{x}^{(N)}\}$ from the calibrated model over the holding period $h$.
    - For correlated normal factors: generate $\mathbf{Z}^{(j)} \sim N(\mathbf{0}, \mathbf{I}_d)$, then set $\Delta\mathbf{x}^{(j)} = \boldsymbol{\mu} h + \mathbf{C}\mathbf{Z}^{(j)}\sqrt{h}$ where $\boldsymbol{\Sigma} = \mathbf{C}\mathbf{C}^\top$ (Cholesky decomposition).
    - For more complex models: use Euler-Maruyama, Milstein, or exact simulation schemes.

    **(c) Revalue the portfolio under each scenario:**

    - For each scenario $j$, compute the new risk factor state $\mathbf{x}_0 + \Delta\mathbf{x}^{(j)}$.
    - Reprice every instrument in the portfolio under this scenario: $P^{(j)} = P(\mathbf{x}_0 + \Delta\mathbf{x}^{(j)})$.
    - Compute the loss: $L^{(j)} = P(\mathbf{x}_0) - P^{(j)}$.
    - For portfolios with options, this requires running a pricing model (Black-Scholes, binomial tree, etc.) for each scenario -- the most computationally expensive step.

    **(d) Compute the $\alpha$-quantile of losses:**

    - Sort the $N$ simulated losses: $L_{(1)} \le L_{(2)} \le \cdots \le L_{(N)}$.
    - The Monte Carlo VaR estimate is:

    $$
    \widehat{\text{VaR}}_\alpha = L_{(\lceil N\alpha \rceil)}
    $$

    **Number of simulations needed for stable 99% VaR:**

    The standard error of the Monte Carlo quantile estimator is:

    $$
    \text{SE}(\widehat{\text{VaR}}_{0.99}) \approx \frac{\sqrt{0.99 \times 0.01}}{\sqrt{N} \cdot f_L(\text{VaR}_{0.99})}
    $$

    For a relative precision of, say, 1% of VaR, typical requirements are:

    - **Without variance reduction:** $N = 50{,}000$ to $100{,}000$ simulations. At 99% confidence, only about $N \times 0.01$ observations fall in the tail. With $N = 100{,}000$, this is 1,000 tail observations, providing reasonable precision.
    - **With variance reduction** (importance sampling, stratified sampling): $N = 10{,}000$ to $50{,}000$ may suffice.
    - **Rule of thumb:** For 99% VaR, use at least $N \ge 10{,}000/(1-\alpha) = 1{,}000{,}000$ for high precision without variance reduction, though in practice $N = 10{,}000$ to $100{,}000$ is common with some tolerance for estimation error.

---

**Exercise 5.** A portfolio contains options with nonlinear payoffs. Explain why the parametric (delta-normal) method underestimates VaR for such portfolios. How does including gamma (second-order) effects improve the estimate? When is Monte Carlo simulation necessary?

??? success "Solution to Exercise 5"

    **Why the parametric (delta-normal) method underestimates VaR for options:**

    The delta-normal method approximates the portfolio loss as:

    $$
    L \approx -\boldsymbol{\delta}^\top \Delta\mathbf{x}
    $$

    This is a **linear approximation** that uses only the first-order sensitivities (deltas). For options, the payoff is a **nonlinear function** of the underlying risk factors:

    - **Gamma effect:** Options have significant curvature (gamma). A linear approximation misses the convexity of the option payoff. For a long option position, the linear approximation overstates losses on the downside and understates gains on the upside (net effect depends on position).
    - **For short option positions** (the most dangerous case): the actual loss distribution has a heavier right tail than the linear approximation suggests, because gamma amplifies losses. The delta-normal VaR thus **underestimates** the true VaR.
    - **Skewness:** The true loss distribution for an options portfolio is typically skewed, but the delta-normal method produces a symmetric (normal) distribution.

    **How including gamma (second-order) effects improves the estimate:**

    The delta-gamma approximation is:

    $$
    L \approx -\boldsymbol{\delta}^\top \Delta\mathbf{x} - \frac{1}{2}\Delta\mathbf{x}^\top \boldsymbol{\Gamma} \Delta\mathbf{x}
    $$

    where $\boldsymbol{\Gamma} = \nabla^2 P$ is the gamma matrix.

    This captures:

    - The curvature of the option payoff, which is critical for at-the-money options with large gamma
    - The asymmetry (skewness) of the loss distribution
    - Better tail behavior compared to the pure delta approximation

    The distribution of $L$ under the delta-gamma approximation is a quadratic form in normal variables, which can be computed via:

    - **Cornish-Fisher expansion:** Adjust the quantile for skewness and kurtosis
    - **Moment matching:** Fit a distribution (e.g., shifted lognormal) to the first four moments of $L$
    - **Fourier inversion:** Use the characteristic function of the quadratic form

    **When is Monte Carlo simulation necessary?**

    Monte Carlo with full revaluation is necessary when:

    1. **Higher-order effects matter:** Instruments with significant third-order and higher sensitivities (e.g., barrier options near the barrier, digital options, exotic path-dependent products).
    2. **Large risk factor moves:** For extreme scenarios, the Taylor expansion breaks down because $\Delta\mathbf{x}$ is large.
    3. **Path-dependent products:** Options whose payoff depends on the entire path (Asian, lookback, barrier options) cannot be captured by delta-gamma alone.
    4. **Complex multi-factor interactions:** Products sensitive to correlation changes, volatility smile dynamics, or cross-gamma effects between many risk factors.
    5. **Stochastic volatility/jumps:** When the risk factor dynamics themselves are nonlinear, requiring simulation of the full model.

---

**Exercise 6.** Backtest the following VaR model: over 250 trading days, a 99% VaR model produces 6 exceptions. Using the Kupiec test, compute the test statistic $\text{LR}_{\text{POF}} = -2\ln\left[\frac{(1-p)^{n-x} p^x}{(1-\hat{p})^{n-x}\hat{p}^x}\right]$ where $p = 0.01$, $\hat{p} = 6/250$, $n = 250$, $x = 6$. Is the model rejected at the 5% significance level?

??? success "Solution to Exercise 6"

    **Given:** $n = 250$ days, $p = 0.01$ (expected exceedance rate), $x = 6$ exceptions, $\hat{p} = 6/250 = 0.024$.

    **Step 1: Compute the Kupiec likelihood ratio test statistic.**

    $$
    LR_{\text{POF}} = -2\ln\left[\frac{(1-p)^{n-x}\,p^x}{(1-\hat{p})^{n-x}\,\hat{p}^x}\right]
    $$

    **Numerator of the likelihood ratio (null hypothesis):**

    $$
    \ln\left[(1-p)^{n-x}\,p^x\right] = (n-x)\ln(1-p) + x\ln(p) = 244\ln(0.99) + 6\ln(0.01)
    $$

    $$
    = 244 \times (-0.01005) + 6 \times (-4.6052) = -2.4522 - 27.6312 = -30.0834
    $$

    **Denominator (MLE):**

    $$
    \ln\left[(1-\hat{p})^{n-x}\,\hat{p}^x\right] = 244\ln(0.976) + 6\ln(0.024)
    $$

    $$
    = 244 \times (-0.02429) + 6 \times (-3.7297) = -5.9268 - 22.3782 = -28.3050
    $$

    **Test statistic:**

    $$
    LR_{\text{POF}} = -2 \times [(-30.0834) - (-28.3050)] = -2 \times (-1.7784) = 3.557
    $$

    **Step 2: Compare with the critical value.**

    Under the null hypothesis, $LR_{\text{POF}} \sim \chi^2(1)$. The critical value at the 5% significance level is:

    $$
    \chi^2_{0.95}(1) = 3.841
    $$

    **Step 3: Decision.**

    Since $LR_{\text{POF}} = 3.557 < 3.841$, we **fail to reject** the null hypothesis at the 5% significance level. The model is not formally rejected.

    **Interpretation:**

    - The expected number of exceptions is $250 \times 0.01 = 2.5$, and we observed 6 -- more than double the expected number.
    - Although the formal test does not reject at 5%, the result is close to the boundary ($p$-value $\approx 0.059$).
    - Under the **Basel traffic light system**, 6 exceptions places the model in the **yellow zone** (5--9 exceptions), which triggers an increased capital multiplier: $k = 3.0 + 0.2 \times (6 - 4) = 3.4$.
    - The model warrants investigation even though the formal test does not reject: possible causes include underestimation of tail risk, volatility clustering not captured by the model, or a regime change during the backtesting period.
    - A complementary test (Christoffersen independence test) should be conducted to check whether the 6 exceptions are clustered in time, which would indicate a model that fails to capture time-varying risk.
