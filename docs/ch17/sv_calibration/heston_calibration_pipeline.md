# Heston Calibration Pipeline

Calibrating the Heston stochastic volatility model to market data requires a structured pipeline that connects observed option prices to model parameters. Unlike simpler models with closed-form inversions, the Heston model demands characteristic-function-based pricing, careful objective function design, and robust numerical optimization. This section develops each stage of the pipeline in detail, from raw market data to validated parameter estimates.

---

## The Heston model and its parameters

Recall that under the risk-neutral measure $\mathbb{Q}$, the Heston (1993) model specifies the asset price $S_t$ and its instantaneous variance $v_t$ as

$$
dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^S
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \sigma_v \sqrt{v_t} \, dW_t^v
$$

where $dW_t^S \, dW_t^v = \rho \, dt$. The five parameters to calibrate are:

| Parameter | Symbol | Role | Typical range |
|-----------|--------|------|---------------|
| Initial variance | $v_0$ | Current volatility level | $(0.001, 1.0)$ |
| Mean-reversion speed | $\kappa$ | Rate of reversion to $\theta$ | $(0.1, 10)$ |
| Long-run variance | $\theta$ | Stationary variance level | $(0.001, 1.0)$ |
| Vol-of-vol | $\sigma_v$ | Variance of the variance | $(0.01, 2.0)$ |
| Correlation | $\rho$ | Skew parameter | $(-1, 0)$ typically |

The Feller condition $2\kappa\theta \geq \sigma_v^2$ ensures that $v_t > 0$ almost surely. When the Feller condition is violated, $v_t$ can reach zero but is immediately reflected.

!!! tip "Parameter interpretation"
    The parameters separate into **level** ($v_0$, $\theta$), **dynamics** ($\kappa$, $\sigma_v$), and **skew** ($\rho$). Short-dated options primarily constrain $v_0$ and $\rho$, while long-dated options identify $\kappa$, $\theta$, and $\sigma_v$. This separation motivates the hierarchical calibration strategies discussed below.

---

## Data preparation

Before optimization begins, raw market data must be cleaned and organized into a form suitable for calibration.

### Market data inputs

The calibration input consists of European option prices $C^{\mathrm{mkt}}(K_j, T_j)$ or implied volatilities $\sigma_j^{\mathrm{impl}}$ for a grid of strikes $K_1, \ldots, K_m$ and maturities $T_1, \ldots, T_n$. Additional inputs are:

- The risk-free rate curve $r(T)$, typically bootstrapped from OIS or Treasury data
- The dividend yield curve $q(T)$, extracted from put-call parity on each expiry
- The spot price $S_0$

### Data cleaning

Several filters ensure data quality before calibration:

1. **Liquidity filter.** Discard options with wide bid-ask spreads (e.g., spread exceeding 20% of mid-price) or zero open interest.
2. **Arbitrage filter.** Verify that call prices decrease in strike and increase in maturity (in terms of total implied variance $w = T \sigma^2$). Remove any quote violating butterfly or calendar spread arbitrage.
3. **Strike range.** Restrict to strikes where the pricing model is reliable, typically $|k| \leq 3$ in log-moneyness $k = \ln(K / F_T)$, where $F_T = S_0 e^{(r-q)T}$ is the forward price.
4. **Mid-price convention.** Use mid-prices $C^{\mathrm{mid}} = (C^{\mathrm{bid}} + C^{\mathrm{ask}})/2$ as calibration targets.

### Forward prices and moneyness

For each maturity $T_j$, compute the forward price

$$
F_j = S_0 \, e^{(r_j - q_j) T_j}
$$

and express strikes in log-moneyness $k_{ij} = \ln(K_i / F_j)$. Working in log-moneyness coordinates normalizes the strike dimension across maturities and simplifies the characteristic function evaluation.

---

## Characteristic function pricing

The Heston model admits a semi-analytic pricing formula through the characteristic function of the log-price. This is the computational engine of the calibration pipeline.

### Log-price characteristic function

Let $x_T = \ln(S_T / K)$. The characteristic function of $x_T$ conditional on $(S_0, v_0)$ takes the form

$$
\phi(u) = \mathbb{E}^{\mathbb{Q}}\!\left[ e^{i u x_T} \right] = \exp\!\left( C(u, T) + D(u, T) v_0 + i u \ln(F_T / K) \right)
$$

where the functions $C$ and $D$ solve a system of Riccati ODEs. In the Heston model, the closed-form solutions are

$$
C(u, T) = \frac{\kappa \theta}{\sigma_v^2} \left[ (\kappa - i \rho \sigma_v u - d(u)) T - 2 \ln\!\left( \frac{1 - g(u) e^{-d(u) T}}{1 - g(u)} \right) \right]
$$

$$
D(u, T) = \frac{\kappa - i \rho \sigma_v u - d(u)}{\sigma_v^2} \cdot \frac{1 - e^{-d(u) T}}{1 - g(u) e^{-d(u) T}}
$$

with auxiliary quantities

$$
d(u) = \sqrt{(i \rho \sigma_v u - \kappa)^2 + \sigma_v^2 (i u + u^2)}
$$

$$
g(u) = \frac{\kappa - i \rho \sigma_v u - d(u)}{\kappa - i \rho \sigma_v u + d(u)}
$$

!!! warning "Branch cut and numerical stability"
    The complex square root in $d(u)$ introduces branch cuts. The formulation above (sometimes called "Formulation 1" following Albrecher et al.) can suffer from discontinuities in $d(u)$ for large $u$ or long maturities. The alternative "Formulation 2," which replaces $g(u)$ with $1/g(u)$ and adjusts the logarithm accordingly, avoids this issue and should be preferred in production implementations.

### Option pricing via Fourier inversion

Given the characteristic function, the European call price is recovered through Fourier inversion. The Carr-Madan (1999) formula expresses the call price in terms of the log-strike $k = \ln K$:

$$
C(K, T) = \frac{e^{-\alpha k}}{\pi} \int_0^\infty \mathrm{Re}\!\left[ e^{-i v k} \, \psi(v) \right] dv
$$

where $\alpha > 0$ is a dampening parameter ensuring integrability, and

$$
\psi(v) = \frac{e^{-r T} \phi(v - (\alpha + 1)i)}{{\alpha^2 + \alpha - v^2 + i(2\alpha + 1)v}}
$$

The integral is evaluated numerically using the Fast Fourier Transform (FFT), which computes prices for an entire grid of $N$ strikes simultaneously in $\mathcal{O}(N \log N)$ operations.

### FFT implementation

The FFT discretization uses a uniform grid in the Fourier variable $v_j = j \Delta v$ for $j = 0, 1, \ldots, N-1$ and produces log-strikes $k_n = -b + n \Delta k$ where $\Delta v \cdot \Delta k = 2\pi / N$ and $b = N \Delta k / 2$. The trapezoidal rule with Simpson's weights improves accuracy:

$$
C(k_n) \approx \frac{e^{-\alpha k_n}}{\pi} \sum_{j=0}^{N-1} e^{-i v_j k_n} \, \psi(v_j) \, \Delta v \, w_j
$$

where $w_j$ are Simpson's rule weights. Typical settings are $N = 4096$, $\Delta v = 0.01$, and $\alpha = 1.5$.

An alternative to the FFT is the **COS method** (Fang and Oosterlee, 2008), which expands the density in a cosine series and converges exponentially fast for smooth densities. For Heston calibration, the COS method often requires fewer terms than the FFT for comparable accuracy.

---

## Objective function design

The objective function quantifies the misfit between model and market. Its design profoundly affects the calibration outcome.

### Price-space objective

The most direct formulation minimizes the weighted sum of squared price errors:

$$
\mathcal{L}_{\mathrm{price}}(\Theta) = \frac{1}{2} \sum_{j=1}^{m} w_j \left( C_j^{\mathrm{mod}}(\Theta) - C_j^{\mathrm{mkt}} \right)^2
$$

where $\Theta = (v_0, \kappa, \theta, \sigma_v, \rho)$ and $w_j$ are weights. Price-space fitting has the advantage of directly measuring replication cost, but deep in-the-money options dominate due to their larger absolute prices.

### Implied volatility objective

The implied volatility formulation provides more uniform scaling:

$$
\mathcal{L}_{\mathrm{vol}}(\Theta) = \frac{1}{2} \sum_{j=1}^{m} w_j \left( \sigma_j^{\mathrm{impl}}(\Theta) - \sigma_j^{\mathrm{mkt}} \right)^2
$$

Computing model implied volatilities requires a root-finding step (e.g., Brent's method or the rational approximation of Jaeckel) to invert the Black-Scholes formula at each evaluation. This adds computational cost but matches market quoting conventions.

### Vega-weighted objective

A natural compromise uses vega weighting in price space:

$$
\mathcal{L}_{\mathrm{vega}}(\Theta) = \frac{1}{2} \sum_{j=1}^{m} \frac{1}{\nu_j^2} \left( C_j^{\mathrm{mod}}(\Theta) - C_j^{\mathrm{mkt}} \right)^2
$$

where $\nu_j = \partial C_j^{\mathrm{BS}} / \partial \sigma$ is the Black-Scholes vega. Since $\Delta C \approx \nu \cdot \Delta \sigma$, this is approximately equivalent to the implied volatility objective but avoids the root-finding step.

!!! note "Statistical interpretation"
    Under the assumption that market price errors are Gaussian with variance proportional to the bid-ask spread, $\varepsilon_j \sim \mathcal{N}(0, s_j^2)$, the maximum likelihood estimator corresponds to weights $w_j = 1/s_j^2$. The bid-ask spread provides a natural proxy for $s_j$.

### Maturity weighting

To prevent short-dated options from dominating (they are typically more numerous), a maturity-balancing scheme assigns equal total weight to each expiry slice:

$$
w_j = \frac{1}{n_k \cdot \sigma_j^{\mathrm{ba}}}
$$

where $n_k$ is the number of options in the $k$-th maturity slice and $\sigma_j^{\mathrm{ba}}$ is the bid-ask spread.

---

## Optimization workflow

With the objective function and characteristic-function pricer in place, the optimization proceeds through initialization, iteration, and validation.

### Parameter bounds and constraints

The parameter vector $\Theta = (v_0, \kappa, \theta, \sigma_v, \rho)$ is subject to box constraints:

$$
v_0 \in (0, 1], \quad \kappa \in (0, 10], \quad \theta \in (0, 1], \quad \sigma_v \in (0, 2], \quad \rho \in (-1, 0)
$$

The Feller condition $2\kappa\theta \geq \sigma_v^2$ may be imposed as a soft penalty rather than a hard constraint, since market-calibrated parameters frequently violate it.

Constraints are handled through **sigmoid transformation**, mapping unconstrained variables $\phi \in \mathbb{R}$ to bounded parameters:

$$
\theta_i = \theta_i^{\min} + (\theta_i^{\max} - \theta_i^{\min}) \cdot \frac{1}{1 + e^{-\phi_i}}
$$

This eliminates constrained optimization and allows standard unconstrained algorithms.

### Initialization

Good starting values are critical for convergence. A standard initialization procedure:

1. **ATM implied volatility.** Set $v_0 = (\sigma_{\mathrm{ATM}}^{\mathrm{short}})^2$ and $\theta = (\sigma_{\mathrm{ATM}}^{\mathrm{long}})^2$ from the shortest and longest maturity ATM implied volatilities.
2. **Skew.** Estimate $\rho$ from the ATM skew: $\rho \approx \text{skew} \cdot \sigma_v^{-1} \cdot (v_0 T)^{-1/2}$ as a rough rule-of-thumb.
3. **Mean-reversion.** Initialize $\kappa$ from the term structure slope: if implied volatility is increasing in maturity, $\kappa$ should be small; if decreasing, $\kappa$ should be larger.
4. **Vol-of-vol.** Initialize $\sigma_v$ from the curvature of the smile: larger curvature suggests larger $\sigma_v$.

### Levenberg-Marquardt algorithm

The Levenberg-Marquardt (LM) algorithm is the standard workhorse for Heston calibration. It solves the damped normal equations at each iteration:

$$
(J^\top W J + \lambda I) \, \Delta\Theta = -J^\top W r(\Theta)
$$

where $J = \nabla_\Theta r(\Theta) \in \mathbb{R}^{m \times 5}$ is the Jacobian of the residual vector, $W$ is the weight matrix, and $\lambda > 0$ is the damping parameter.

The adaptive damping strategy proceeds as follows:

1. Evaluate the actual reduction $\Delta_{\mathrm{act}} = \mathcal{L}(\Theta^{(k)}) - \mathcal{L}(\Theta^{(k)} + \Delta\Theta)$.
2. Evaluate the predicted reduction $\Delta_{\mathrm{pred}} = -\Delta\Theta^\top (J^\top W r + \frac{1}{2} (J^\top W J + \lambda I) \Delta\Theta)$.
3. Compute the gain ratio $\varrho = \Delta_{\mathrm{act}} / \Delta_{\mathrm{pred}}$.
4. If $\varrho > 0.75$: accept step, reduce $\lambda \to \lambda / 3$ (more Gauss-Newton-like).
5. If $0.25 < \varrho \leq 0.75$: accept step, keep $\lambda$.
6. If $\varrho \leq 0.25$: reject step, increase $\lambda \to 2\lambda$ (more gradient-descent-like).

### Jacobian computation

The Jacobian $J_{jk} = \partial r_j / \partial \Theta_k$ can be computed by:

- **Finite differences.** $\partial r_j / \partial \Theta_k \approx (r_j(\Theta + h_k e_k) - r_j(\Theta)) / h_k$ with step size $h_k \sim 10^{-6} |\Theta_k|$. Requires $d+1 = 6$ pricing evaluations per iteration.
- **Adjoint (algorithmic) differentiation.** Propagates sensitivities through the characteristic function evaluation in a single backward pass, with cost independent of the number of parameters. This is the preferred approach for production systems.

### Convergence diagnostics

The algorithm terminates when any of the following criteria are met:

$$
\|\nabla \mathcal{L}\|_\infty < \varepsilon_g, \qquad \frac{\|\Delta\Theta\|}{\|\Theta\|} < \varepsilon_\theta, \qquad \frac{|\Delta \mathcal{L}|}{|\mathcal{L}|} < \varepsilon_f, \qquad k > k_{\max}
$$

Typical values are $\varepsilon_g = 10^{-8}$, $\varepsilon_\theta = 10^{-8}$, $\varepsilon_f = 10^{-12}$, and $k_{\max} = 200$.

---

## Multi-start and global search

The Heston objective landscape contains multiple local minima, particularly due to the entanglement between $\kappa$ and $\theta$ (large $\kappa$ with large $\theta$ can produce similar stationary behavior to small $\kappa$ with small $\theta$). A single Levenberg-Marquardt run from one starting point may converge to a suboptimal minimum.

**Multi-start strategy.** Run $N_{\mathrm{start}}$ independent LM optimizations from different initial points sampled from the parameter bounds, then select the solution with the smallest objective value. Typical choices are $N_{\mathrm{start}} = 10$--$50$.

**Hybrid global-local.** Use a global method (differential evolution or particle swarm) for a limited number of iterations to identify the basin of the global minimum, then switch to LM for rapid local convergence. This two-phase approach combines the exploration of global methods with the fast convergence of LM.

---

## Parameter validation

After optimization converges, the calibrated parameters must be validated before use.

### Goodness-of-fit diagnostics

1. **Residual analysis.** Plot residuals $r_j = \sigma_j^{\mathrm{mod}} - \sigma_j^{\mathrm{mkt}}$ versus strike and maturity. Systematic patterns (e.g., residuals increasing at far OTM strikes) indicate model limitations.
2. **Root mean squared error.** Compute $\mathrm{RMSE} = \sqrt{m^{-1} \sum_j r_j^2}$. For implied volatilities, RMSE below 0.5 vol points is typical for liquid equity index options.
3. **Maximum absolute error.** Verify $\max_j |r_j|$ is within the bid-ask spread for most instruments.

### Parameter stability

1. **Bootstrap sensitivity.** Perturb market prices within the bid-ask spread and recalibrate. Stable parameters should change by less than 10--20%.
2. **Profile likelihood.** Fix one parameter and recalibrate the others, sweeping the fixed parameter over its range. A well-identified parameter produces a sharply peaked profile; a flat profile indicates poor identifiability.
3. **Temporal stability.** Compare today's parameters with yesterday's. Large day-over-day jumps (especially in $\kappa$) may indicate overfitting to noise.

### Feller condition check

Verify whether $2\kappa\theta / \sigma_v^2 \geq 1$. If violated, the variance process can reach zero, which affects Monte Carlo simulation (requiring careful discretization) and may produce unreliable Greeks for path-dependent products.

!!! example "Typical calibrated parameters"
    For S&P 500 index options in a moderate-volatility regime, typical calibrated Heston parameters are:

    | Parameter | Typical value |
    |-----------|---------------|
    | $v_0$ | $0.02$--$0.06$ |
    | $\kappa$ | $1.0$--$5.0$ |
    | $\theta$ | $0.02$--$0.08$ |
    | $\sigma_v$ | $0.3$--$0.8$ |
    | $\rho$ | $-0.8$--$-0.5$ |

    The negative correlation $\rho$ captures the leverage effect: equity prices and volatility are negatively correlated.

---

## Summary of the calibration pipeline

The complete Heston calibration pipeline consists of the following stages:

1. **Data preparation.** Collect option prices, extract forwards, filter for liquidity and arbitrage, compute log-moneyness coordinates.
2. **Pricer setup.** Implement the Heston characteristic function (Formulation 2 for numerical stability) and Fourier inversion via FFT or COS method.
3. **Objective function.** Choose between price-space, implied-vol, or vega-weighted objectives with maturity-balanced weights.
4. **Initialization.** Set starting parameters from ATM volatilities, skew, and smile curvature.
5. **Optimization.** Run Levenberg-Marquardt with adaptive damping, optionally preceded by a global search phase.
6. **Validation.** Check residuals, parameter stability, and the Feller condition.
7. **Deployment.** Use calibrated parameters for pricing and hedging, with regular recalibration as market conditions evolve.

---
