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

## Exercises

**Exercise 1.** The Heston model has five parameters $(v_0, \kappa, \theta, \sigma_v, \rho)$. Describe qualitatively which parameters are primarily identified by short-dated options and which by long-dated options. Why does this separation motivate a hierarchical calibration strategy?

??? success "Solution to Exercise 1"
    The five Heston parameters separate into groups by their sensitivity to different parts of the maturity spectrum.

    **Short-dated options primarily constrain $v_0$ and $\rho$.**
    For short maturities $T \to 0$, the variance process has not had time to mean-revert, so $v_t \approx v_0$. The ATM implied volatility at short maturities is approximately $\sigma_{\text{ATM}} \approx \sqrt{v_0}$, providing a direct constraint on $v_0$. The skew (slope of the implied volatility smile) at short maturities is driven by the instantaneous correlation $\rho$ between the price and variance Brownian motions: $\partial \sigma / \partial k |_{k=0} \propto \rho \sigma_v / \sqrt{v_0}$. Since $\sigma_v$ also appears, the skew alone does not identify $\rho$ uniquely, but in combination with the smile curvature, $\rho$ is well-determined at short maturities.

    **Long-dated options primarily constrain $\kappa$, $\theta$, and $\sigma_v$.**
    For long maturities $T \to \infty$, the variance $v_t$ has mean-reverted toward $\theta$, and the ATM implied volatility converges to approximately $\sqrt{\theta}$. The rate of convergence from $\sqrt{v_0}$ (short-dated) to $\sqrt{\theta}$ (long-dated) is governed by $\kappa$: larger $\kappa$ means faster convergence, producing a steeper term structure of ATM volatility. The smile curvature at long maturities is controlled by $\sigma_v$, the vol-of-vol, which determines the excess kurtosis of the log-price distribution.

    **Hierarchical calibration motivation.**
    This separation motivates a two-stage approach:

    1. *Stage 1:* Calibrate $v_0$ and $\rho$ from short-dated options only (e.g., $T < 3$ months), holding $\kappa$, $\theta$, $\sigma_v$ at initial guesses.
    2. *Stage 2:* Calibrate $\kappa$, $\theta$, $\sigma_v$ from the full surface, holding $v_0$ and $\rho$ near their Stage 1 values (or allowing small adjustments).

    This hierarchical approach reduces the effective dimension of each optimization from 5 to 2--3, improving convergence speed and reducing the risk of landing in a spurious local minimum caused by $(\kappa, \theta)$ entanglement. It also provides better initial values for a final joint optimization over all 5 parameters.

---

**Exercise 2.** State the Feller condition $2\kappa\theta \ge \sigma_v^2$ and explain its financial significance. If a calibration yields $\kappa = 1.5$, $\theta = 0.03$, $\sigma_v = 0.6$, check whether the Feller condition is satisfied. What are the numerical consequences for Monte Carlo simulation when it is violated?

??? success "Solution to Exercise 2"
    **The Feller condition** states that

    $$
    2\kappa\theta \geq \sigma_v^2
    $$

    **Financial significance.** When the Feller condition holds, the variance process $v_t$ remains strictly positive almost surely. This ensures that the asset price process $S_t$ has well-defined, nonzero volatility at all times. The asset price never becomes deterministic (which would happen if $v_t = 0$ with zero vol-of-vol), and the model remains a genuine stochastic volatility model.

    When the Feller condition is violated ($2\kappa\theta < \sigma_v^2$), the variance process can reach zero. At $v_t = 0$, the drift term $\kappa(\theta - 0) = \kappa\theta > 0$ pushes the variance back up, so zero is an instantaneously reflecting boundary (not absorbing). However, the process spends time at or near zero, creating degeneracies.

    **Checking the condition for the given parameters.** With $\kappa = 1.5$, $\theta = 0.03$, $\sigma_v = 0.6$:

    $$
    2\kappa\theta = 2 \times 1.5 \times 0.03 = 0.09
    $$

    $$
    \sigma_v^2 = 0.6^2 = 0.36
    $$

    Since $0.09 < 0.36$, the Feller condition is **violated**. The ratio $2\kappa\theta / \sigma_v^2 = 0.25$, which is well below 1.

    **Numerical consequences for Monte Carlo simulation.**
    When the Feller condition is violated and standard Euler discretization is used:

    1. **Negative variance.** The Euler scheme $v_{t+\Delta t} = v_t + \kappa(\theta - v_t)\Delta t + \sigma_v \sqrt{v_t} \sqrt{\Delta t} \, Z$ can produce $v_{t+\Delta t} < 0$ when $v_t$ is small and $Z$ is a large negative normal draw. This is unphysical and crashes the simulation.
    2. **Common fixes.** (a) Full truncation: replace $v_t$ by $\max(v_t, 0)$ in both the drift and diffusion terms. (b) Reflection: use $|v_{t+\Delta t}|$ when the scheme produces a negative value. (c) The Milstein scheme or the QE (quadratic-exponential) scheme of Andersen (2008), which handles the CIR boundary more carefully.
    3. **Bias and convergence.** Naive truncation introduces bias that converges slowly as $\Delta t \to 0$. The QE scheme provides much better accuracy for the same step size when the Feller condition is violated.
    4. **Impact on Greeks.** Unstable Monte Carlo paths near $v_t = 0$ produce noisy Greeks, particularly vega and volga, which depend on the variance dynamics.

---

**Exercise 3.** Describe the data cleaning steps needed before Heston calibration: liquidity filtering, arbitrage detection, and forward extraction via put-call parity. For a specific example with $S_0 = 100$, $r = 2\%$, $q = 1\%$, $T = 0.5$, and observed call and put prices $C = 8.50$, $P = 5.20$ at $K = 100$, verify put-call parity and extract the implied forward.

??? success "Solution to Exercise 3"
    **Data cleaning steps.**

    *Liquidity filtering:* Discard options with bid-ask spreads exceeding a threshold (e.g., 20% of mid-price) or with zero open interest/volume. Illiquid options carry wide effective bid-ask bounds and introduce noise into the calibration.

    *Arbitrage detection:* Check three conditions:

    1. **Monotonicity in strike (call spread arbitrage):** Call prices must be decreasing in strike: $C(K_1) \geq C(K_2)$ for $K_1 < K_2$. Similarly, put prices must be increasing in strike.
    2. **Convexity in strike (butterfly arbitrage):** The call price must be convex in strike: $C(K_2) \leq \frac{K_3 - K_2}{K_3 - K_1} C(K_1) + \frac{K_2 - K_1}{K_3 - K_1} C(K_3)$ for $K_1 < K_2 < K_3$. Violation implies negative risk-neutral density.
    3. **Calendar spread arbitrage:** Total implied variance $w(T) = T \sigma^2(T)$ must be non-decreasing in $T$ for each fixed strike.

    *Forward extraction via put-call parity:* Put-call parity states

    $$
    C - P = S_0 e^{-qT} - K e^{-rT}
    $$

    which can be rearranged to extract the forward price $F = S_0 e^{(r-q)T}$.

    **Numerical verification.** Given $S_0 = 100$, $r = 0.02$, $q = 0.01$, $T = 0.5$, $C = 8.50$, $P = 5.20$, $K = 100$:

    The implied forward from put-call parity:

    $$
    C - P = 8.50 - 5.20 = 3.30
    $$

    $$
    F_{\text{implied}} \cdot e^{-rT} - K e^{-rT} = C - P
    $$

    $$
    e^{-rT}(F - K) = 3.30
    $$

    $$
    F - K = 3.30 \cdot e^{rT} = 3.30 \times e^{0.01} \approx 3.30 \times 1.01005 = 3.3332
    $$

    So $F_{\text{implied}} = 100 + 3.3332 = 103.3332$.

    The theoretical forward is

    $$
    F_{\text{theo}} = S_0 e^{(r-q)T} = 100 \times e^{(0.02 - 0.01) \times 0.5} = 100 \times e^{0.005} \approx 100 \times 1.005013 = 100.5013
    $$

    The discrepancy between $F_{\text{implied}} = 103.33$ and $F_{\text{theo}} = 100.50$ is large (2.8%), suggesting either the quoted prices are inconsistent, the dividend yield assumption is incorrect, or there is a data error. In practice, one would either adjust $q$ to reconcile the discrepancy or flag this option pair for investigation.

---

**Exercise 4.** Compare price-space versus implied-vol-space objective functions for Heston calibration. A deep OTM put with $K = 70$, $T = 0.25$ has a market price of \$0.05 and implied vol of 35%. A bump of 1 vol point changes the price by approximately \$0.001. Compute the residual contribution in each space for a model implying 36% vol. Which space gives more weight to this option?

??? success "Solution to Exercise 4"
    **Price-space residual.** The model implies 36% vol versus the market's 35%. The corresponding price bump from a 1 vol point change is approximately \$0.001, so a 1-point vol error produces a price difference of approximately

    $$
    \Delta C \approx \nu \cdot \Delta\sigma = 0.001 \times 1 = \$0.001
    $$

    where $\nu$ is the Black-Scholes vega. The price-space residual for this deep OTM put is

    $$
    r_{\text{price}} = C^{\text{mod}} - C^{\text{mkt}} \approx \$0.001
    $$

    and its contribution to the price-space objective is

    $$
    r_{\text{price}}^2 = (0.001)^2 = 10^{-6}
    $$

    **Implied-vol-space residual.** In implied vol space, the residual is simply the vol difference:

    $$
    r_{\text{vol}} = 0.36 - 0.35 = 0.01 \quad (1 \text{ vol point})
    $$

    and its contribution to the vol-space objective is

    $$
    r_{\text{vol}}^2 = (0.01)^2 = 10^{-4}
    $$

    **Comparison.** The vol-space residual contribution ($10^{-4}$) is 100 times larger than the price-space contribution ($10^{-6}$). This means implied vol space gives **much more weight** to this deep OTM option.

    **Why this matters.** In price space, deep OTM options with tiny absolute prices contribute negligibly to the objective, even when their implied vols are badly fitted. ATM options, which have the largest absolute prices and vegas, dominate the calibration. This is problematic because:

    1. The smile and skew information resides primarily in OTM options.
    2. Risk management requires accurate smile fitting for OTM strikes (e.g., for delta hedging of risk reversals).

    In implied vol space, all options contribute comparably regardless of moneyness, because the residual is measured in the same units (vol points) across all strikes. This produces a more balanced fit across the entire smile.

    The vega-weighted objective $\sum (C_j^{\text{mod}} - C_j^{\text{mkt}})^2 / \nu_j^2$ achieves a similar effect: dividing by $\nu_j^2$ transforms the price residual $\Delta C \approx \nu \Delta\sigma$ into $(\Delta C / \nu)^2 \approx (\Delta\sigma)^2$, effectively converting to vol space without the root-finding step.

---

**Exercise 5.** A simple initialization heuristic sets $v_0 \approx \sigma_{\text{ATM}}^2$, $\rho$ from the 25-delta skew, and $\sigma_v$ from the smile curvature. For an ATM implied vol of 20%, 25-delta put vol of 25%, and 25-delta call vol of 18%, propose initial values for $v_0$, $\rho$, and $\sigma_v$. Discuss the limitations of this heuristic.

??? success "Solution to Exercise 5"
    **Proposed initial values.**

    *Initial variance $v_0$:* With ATM implied vol of 20%:

    $$
    v_0 \approx \sigma_{\text{ATM}}^2 = (0.20)^2 = 0.04
    $$

    *Correlation $\rho$:* The 25-delta skew is measured by the difference between the 25-delta put vol and 25-delta call vol:

    $$
    \text{skew} = \sigma_{25\Delta P} - \sigma_{25\Delta C} = 25\% - 18\% = 7\%
    $$

    The risk reversal (RR) is 7 vol points. In the Heston model, the leading-order ATM skew is approximately

    $$
    \frac{\partial \sigma}{\partial k}\bigg|_{k=0} \approx \frac{\rho \sigma_v}{2\sqrt{v_0}}
    $$

    A negative skew (puts more expensive than calls) corresponds to $\rho < 0$. As a rough rule-of-thumb, using the risk reversal to estimate $\rho$:

    $$
    \rho \approx -0.7 \quad \text{(initial guess)}
    $$

    This is based on the observation that for typical equity parameters, a 7-point risk reversal with 20% ATM vol corresponds to $\rho$ in the range $[-0.8, -0.6]$.

    *Vol-of-vol $\sigma_v$:* The smile curvature (butterfly) is measured by

    $$
    \text{BF} = \frac{\sigma_{25\Delta P} + \sigma_{25\Delta C}}{2} - \sigma_{\text{ATM}} = \frac{25\% + 18\%}{2} - 20\% = 21.5\% - 20\% = 1.5\%
    $$

    The butterfly spread of 1.5 vol points indicates moderate curvature. In the Heston model, the curvature scales approximately as $\sigma_v^2$. For a butterfly of 1.5% with 20% ATM vol:

    $$
    \sigma_v \approx 0.5 \quad \text{(initial guess)}
    $$

    **Limitations of this heuristic.**

    1. **$\kappa$ and $\theta$ are not determined.** The heuristic provides no guidance for mean-reversion speed or long-run variance. These require the term structure of ATM volatilities (multiple maturities), which the single-maturity quotes above do not provide.
    2. **Interdependence.** The formulas above treat $v_0$, $\rho$, $\sigma_v$ as independent, but in reality, all 5 parameters jointly affect the smile. The leading-order approximations break down when parameters are large (e.g., $\sigma_v > 1$) or when $T$ is not small.
    3. **Sensitivity to $\beta$ (if mapping to SABR).** The 25-delta points are not exactly at fixed log-moneyness, so the skew and curvature estimates depend on the forward level and time to expiry.
    4. **Non-uniqueness.** Different $(\rho, \sigma_v)$ combinations can produce similar skew and curvature at one maturity. The heuristic picks one combination, which may not be globally optimal.

    Despite these limitations, the heuristic provides a reasonable starting point that places the optimizer in the correct region of parameter space, significantly reducing the number of LM iterations needed for convergence.

---

**Exercise 6.** After calibration, the residuals (model vol minus market vol) at 10 strikes for a single maturity are: $+0.15, +0.10, +0.05, +0.02, -0.01, -0.02, +0.03, +0.08, +0.12, +0.18$ (in vol points). The residuals show a systematic U-shaped pattern. What does this suggest about the model's ability to fit the smile? Propose a model extension that could address this deficiency.

??? success "Solution to Exercise 6"
    **Analysis of the U-shaped residual pattern.**
    The residuals $+0.15, +0.10, +0.05, +0.02, -0.01, -0.02, +0.03, +0.08, +0.12, +0.18$ (assuming strikes are ordered from low to high) show:

    - Large positive residuals at low strikes (model overestimates OTM put vols)
    - Near-zero residuals near ATM
    - Large positive residuals at high strikes (model overestimates OTM call vols)

    The systematic U-shape indicates that the Heston model generates a smile that is **too wide** (too much curvature) relative to the market smile. The model's implied vol wings are higher than market observations.

    Alternatively, if we interpret the residuals as going from deep OTM puts through ATM to deep OTM calls, the pattern suggests the model's smile is shifted upward at the wings relative to the market. The RMSE is

    $$
    \text{RMSE} = \sqrt{\frac{1}{10}(0.15^2 + 0.10^2 + 0.05^2 + 0.02^2 + 0.01^2 + 0.02^2 + 0.03^2 + 0.08^2 + 0.12^2 + 0.18^2)}
    $$

    $$
    = \sqrt{\frac{0.0225 + 0.01 + 0.0025 + 0.0004 + 0.0001 + 0.0004 + 0.0009 + 0.0064 + 0.0144 + 0.0324}{10}} \approx 0.10 \text{ vol points}
    $$

    **Diagnosis.** The Heston model generates smile curvature primarily through the vol-of-vol parameter $\sigma_v$. However, the model constrains the relationship between the curvature (controlled by $\sigma_v$) and the skew (controlled jointly by $\rho$ and $\sigma_v$). When the market smile has a different skew-curvature relationship than Heston can produce, the optimizer compromises: it fits the skew reasonably well but overshoots on the wings, producing the U-shaped residual.

    **Proposed model extensions.**

    1. **Heston with jumps (Bates model).** Adding jumps in the asset price $dS_t = \ldots + S_{t^-}(e^J - 1) dN_t$ provides an additional source of smile curvature (especially at short maturities) that is independent of the $(\rho, \sigma_v)$ mechanism. The jump parameters ($\lambda$, $\mu_J$, $\sigma_J$) decouple the short-maturity wings from the diffusion skew, allowing independent control of curvature and skew.
    2. **Double Heston.** Using two independent variance processes with different $(\kappa_i, \theta_i, \sigma_{v,i}, \rho_i)$ provides a richer set of smile shapes. One process can capture the overall level and skew while the other adds curvature.
    3. **Stochastic local volatility (SLV).** Combining local volatility with stochastic volatility provides exact vanilla fit by construction (like local vol) while maintaining realistic dynamics (like stochastic vol). The mixing parameter controls the balance.

---

**Exercise 7.** Describe the complete Heston calibration pipeline from start to finish for a trading desk that needs to calibrate daily to 200 SPX options across 8 maturities. Specify: data source and cleaning, objective function choice, optimization algorithm, convergence criteria, validation checks, and runtime target. Justify each choice.

??? success "Solution to Exercise 7"
    **Complete calibration pipeline for daily SPX calibration.**

    **1. Data source and cleaning.**

    - *Source:* End-of-day (or intraday snapshot) SPX option prices from a market data vendor (e.g., OPRA feed, Bloomberg, or exchange direct). Use settlement prices for end-of-day calibration.
    - *Forward extraction:* For each of the 8 maturities, extract the forward price $F_j$ from put-call parity on the nearest ATM pair. Cross-check against the OIS discount curve and estimated dividend yields.
    - *Liquidity filter:* Retain only options with bid-ask spread $< 20\%$ of mid-price and open interest $> 100$ contracts. This typically retains 15--25 strikes per maturity out of the original $\sim 200/8 = 25$ per maturity.
    - *Arbitrage filter:* Check call spread, butterfly, and calendar spread constraints. Remove violating quotes (typically 1--3 per maturity).
    - *Strike range:* Restrict to log-moneyness $|k| \leq 2.5$ to avoid extreme OTM options where the model is unreliable and market quotes are wide.

    **2. Objective function choice.**
    Use the vega-weighted price objective:

    $$
    \mathcal{L}(\Theta) = \frac{1}{2} \sum_{j=1}^{m} \frac{1}{\nu_j^2} (C_j^{\text{mod}} - C_j^{\text{mkt}})^2
    $$

    with maturity balancing (equal total weight per expiry slice). This is approximately equivalent to implied vol fitting but avoids the costly root-finding step at each evaluation. For 200 options across 8 maturities, the maturity weights are $w_k = 1/n_k$ where $n_k$ is the number of options in slice $k$.

    **3. Optimization algorithm.**
    Use a hybrid global-then-local strategy:

    - *Phase 1 (warm start):* If yesterday's calibrated parameters are available, use them as the primary starting point. If this is the first calibration or yesterday's parameters are stale, use the initialization heuristic from the ATM vol and skew.
    - *Phase 2 (multi-start LM):* Run $N = 5$ Levenberg-Marquardt optimizations: one from the warm start, four from perturbed starting points (perturbations of $\pm 20\%$ in each parameter). Use Marquardt's scaling ($\lambda \cdot \text{diag}(J^\top W J)$) for parameter-scale adaptation. Compute the Jacobian via finite differences with optimal step sizes.
    - *Phase 3 (selection):* Select the result with the smallest objective value.

    **4. Convergence criteria.**

    $$
    \|\nabla \mathcal{L}\|_\infty < 10^{-8}, \quad \frac{\|\Delta\Theta\|}{\|\Theta\|} < 10^{-8}, \quad \frac{|\Delta\mathcal{L}|}{|\mathcal{L}|} < 10^{-12}, \quad k_{\max} = 100
    $$

    Each LM run typically converges in 15--30 iterations.

    **5. Validation checks.**

    - *RMSE:* Verify $\text{RMSE} < 0.5$ vol points. Alert if $> 1.0$ vol points.
    - *Max error:* Verify $\max_j |r_j| < 1.5$ vol points (should be within bid-ask for most options).
    - *Residual pattern:* Check for systematic U-shape or asymmetry. Log any pattern for model risk monitoring.
    - *Feller condition:* Compute $2\kappa\theta / \sigma_v^2$ and log. Flag if $< 0.5$ (severe violation).
    - *Parameter stability:* Compare with yesterday's parameters. Alert if any parameter changes by more than 25% without a corresponding market move.
    - *Boundary check:* Flag if any parameter is within 5% of its bound (suggests the bound is binding).

    **6. Runtime target.**

    - FFT pricing: $\sim 1$ ms per evaluation (200 options, 8 maturities, $N_{\text{FFT}} = 4096$).
    - Jacobian: 6 evaluations $\times$ 1 ms = 6 ms per LM iteration.
    - Per LM run: 25 iterations $\times$ 6 ms = 150 ms.
    - Total (5 starts): $5 \times 150$ ms = 750 ms $< 1$ s.

    Target total runtime including data loading and validation: **under 5 seconds**. This is well within the requirements for daily calibration and feasible even for intraday recalibration at 5-minute intervals.
