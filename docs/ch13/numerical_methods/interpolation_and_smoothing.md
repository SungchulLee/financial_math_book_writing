# Interpolation and Smoothing

Dupire's formula requires the partial derivatives $\partial C / \partial T$, $\partial C / \partial K$, and $\partial^2 C / \partial K^2$ of the call price surface. In practice, European option prices are observed at a discrete, irregular grid of strikes and maturities, and these observations contain noise from bid-ask spreads, staleness, and microstructure effects. Computing second derivatives of noisy discrete data amplifies the noise dramatically, producing a local volatility surface riddled with oscillations and even negative values. This section develops the interpolation and smoothing techniques needed to transform raw market data into a smooth, arbitrage-free call price surface suitable for differentiation.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Explain why smoothing is essential before applying Dupire's formula
    - Apply cubic spline interpolation to implied volatility data with arbitrage-free constraints
    - State and enforce the three no-arbitrage conditions: monotonicity, convexity, and calendar spread
    - Describe the SVI and SSVI parametrizations and their arbitrage-free properties
    - Identify the tradeoffs between overfitting (capturing noise) and underfitting (losing smile structure)

## The Smoothing Problem

### Why Raw Data Fails

Consider a discrete set of market call prices $\{C_{\text{mkt}}(K_i, T_j)\}$ observed at strikes $K_1 < K_2 < \cdots < K_m$ and maturities $T_1 < T_2 < \cdots < T_p$. Applying Dupire's formula directly via finite differences:

$$
\sigma_{\text{loc}}^2(K_i, T_j) = \frac{\frac{C(K_i, T_{j+1}) - C(K_i, T_{j-1})}{T_{j+1} - T_{j-1}} + (r - q)K_i \frac{C(K_{i+1}, T_j) - C(K_{i-1}, T_j)}{K_{i+1} - K_{i-1}} + qC(K_i, T_j)}{\frac{1}{2}K_i^2 \frac{C(K_{i+1}, T_j) - 2C(K_i, T_j) + C(K_{i-1}, T_j)}{(\Delta K)^2}}
$$

The denominator involves a second difference of noisy data. If the noise in each price is $\epsilon$, the noise in $C_{KK} \approx \partial^2 C / \partial K^2$ scales as $\epsilon / (\Delta K)^2$, which can be enormous when $\Delta K$ is small or $\epsilon$ is not negligible relative to the butterfly spread price.

**Example:** With $\Delta K = 5$ and price noise $\epsilon = \$0.05$:

$$
\text{noise in } C_{KK} \approx \frac{0.05}{25} = 0.002
$$

Since $C_{KK} = e^{-rT} q(K)$ (the discounted density), typical values are $10^{-3}$ to $10^{-2}$. The noise is comparable to the signal, rendering the raw finite difference useless.

### Interpolation vs Smoothing

- **Interpolation** passes through every data point exactly: $f(K_i) = C_i$. This preserves noise.
- **Smoothing** finds a function close to the data but not necessarily passing through each point. This filters noise at the cost of some approximation error.

For local volatility construction, **smoothing** is essential. The goal is to find a function $\hat{C}(K, T)$ that:

1. Approximates the market prices: $|\hat{C}(K_i, T_j) - C_{\text{mkt}}(K_i, T_j)| \leq \epsilon_{ij}$
2. Is sufficiently smooth for differentiation: $\hat{C} \in C^2$ in $K$ and $C^1$ in $T$
3. Satisfies no-arbitrage constraints

## No-Arbitrage Constraints

### The Three Conditions

Any arbitrage-free call price surface must satisfy:

**Condition 1: Strike monotonicity.** Call prices are decreasing in strike:

$$
\frac{\partial C}{\partial K} \leq 0
$$

Violation produces a trivial arbitrage: sell the cheaper high-strike call and buy the more expensive low-strike call.

**Condition 2: Strike convexity (butterfly constraint).** Call prices are convex in strike:

$$
\frac{\partial^2 C}{\partial K^2} \geq 0
$$

By Breeden-Litzenberger, this is equivalent to non-negativity of the risk-neutral density. Violation means negative probabilities — a butterfly spread with negative cost.

**Condition 3: Calendar monotonicity.** Total implied variance is non-decreasing in maturity:

$$
\frac{\partial C}{\partial T} \geq 0 \quad \text{(at each strike)}
$$

Equivalently, $\sigma_{\text{IV}}^2(K, T) \cdot T$ is non-decreasing in $T$. Violation produces a calendar spread arbitrage.

!!! warning "Consequence for Local Volatility"
    If any of these conditions is violated, Dupire's formula produces:

    - **Negative $C_{KK}$:** Division by a negative number gives $\sigma_{\text{loc}}^2 < 0$, which is physically meaningless
    - **Negative $C_T$:** Negative numerator gives $\sigma_{\text{loc}}^2 < 0$
    - **$C_{KK} \approx 0$:** Division by near-zero produces $\sigma_{\text{loc}} \to \infty$, destabilizing any PDE or Monte Carlo solver

    Enforcing no-arbitrage constraints is therefore a prerequisite for constructing a usable local volatility surface.

### Implications in Total Variance Space

Working in total variance $w(y, T) = \sigma_{\text{IV}}^2(y, T) \cdot T$ with log-moneyness $y = \ln(K / F)$, the conditions become:

1. **Butterfly:** $g(y, T) = \left(1 - \frac{yw_y}{2w}\right)^2 - \frac{w_y^2}{4}\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{w_{yy}}{2} \geq 0$
2. **Calendar:** $\frac{\partial w}{\partial T} \geq 0$

These conditions, due to Durrleman, are jointly necessary and sufficient for an arbitrage-free surface.

## Interpolation in Strike

### Cubic Spline in Implied Volatility

The most common approach interpolates in **implied volatility** rather than in prices, because the IV surface is smoother and better conditioned.

For each fixed maturity $T_j$, fit a cubic spline $\hat{\sigma}(K; T_j)$ to the observed implied volatilities $\{\sigma_{\text{IV}}(K_i, T_j)\}_{i=1}^m$.

A natural cubic spline minimizes the curvature integral:

$$
\min_{\hat{\sigma}} \int_{K_1}^{K_m} \left(\hat{\sigma}''(K)\right)^2 dK \quad \text{subject to} \quad \hat{\sigma}(K_i) = \sigma_i
$$

The spline is $C^2$ continuous, enabling computation of $C_{KK}$ via the chain rule:

$$
\frac{\partial^2 C}{\partial K^2} = \frac{\partial}{\partial K}\left(\frac{\partial C}{\partial \sigma}\frac{\partial \sigma}{\partial K} + \frac{\partial C}{\partial K}\bigg|_\sigma\right)
$$

where $\partial C / \partial \sigma$ is the Black-Scholes vega and $\partial C / \partial K|_\sigma$ is the Black-Scholes strike derivative at fixed $\sigma$.

### Constrained Splines

To enforce arbitrage-free conditions, the spline must satisfy additional constraints:

**Monotonicity in price:** Since $\partial C / \partial K = -e^{-rT}\mathcal{N}(d_2)$, we need $-1 \leq e^{rT}\partial C/\partial K \leq 0$. This does not directly constrain the IV spline but can be checked after converting to prices.

**Convexity in price:** $\partial^2 C / \partial K^2 \geq 0$ translates to a nonlinear constraint on the IV spline. A sufficient condition is that the IV smile not be too concave:

$$
\frac{\partial^2 \sigma}{\partial K^2} \geq -\frac{d_1 \sqrt{T}}{K^2 \sigma T}\left(\frac{\partial \sigma}{\partial K}\right)^2 - \frac{1}{K\sigma\sqrt{T}}\phi(d_2)
$$

In practice, this is enforced iteratively or via constrained optimization.

### Smoothing Splines

A **smoothing spline** relaxes exact interpolation in favor of smoothness:

$$
\min_{\hat{\sigma}} \left\{\sum_{i=1}^m w_i \left(\hat{\sigma}(K_i) - \sigma_i\right)^2 + \lambda \int_{K_1}^{K_m} \left(\hat{\sigma}''(K)\right)^2 dK\right\}
$$

The parameter $\lambda > 0$ controls the smoothness-fit tradeoff:

- $\lambda \to 0$: Interpolation (passes through all points)
- $\lambda \to \infty$: Linear regression (maximum smoothness)

The weights $w_i$ can encode bid-ask spread information: wider spreads imply less confidence, so smaller weights.

!!! tip "Choosing the Smoothing Parameter"
    Cross-validation provides a data-driven choice of $\lambda$. Leave-one-out cross-validation minimizes:

    $$
    \text{CV}(\lambda) = \frac{1}{m}\sum_{i=1}^m \left(\frac{\hat{\sigma}(K_i) - \sigma_i}{1 - h_{ii}(\lambda)}\right)^2
    $$

    where $h_{ii}$ is the $i$-th diagonal element of the hat matrix. This balances fidelity to data against overfitting without requiring external information about noise levels.

## Interpolation in Maturity

### Total Variance Interpolation

For each fixed strike $K$, interpolate total variance $w(T) = \sigma_{\text{IV}}^2(K, T) \cdot T$ across maturities. Using total variance (rather than IV itself) is preferred because:

1. Total variance must be non-decreasing in $T$ (calendar constraint)
2. Linear interpolation in $w$ preserves this monotonicity
3. The variance swap decomposes additively over time intervals

**Linear interpolation in total variance:**

$$
w(T) = w(T_j) + \frac{T - T_j}{T_{j+1} - T_j}\left(w(T_{j+1}) - w(T_j)\right) \quad \text{for } T \in [T_j, T_{j+1}]
$$

Since $w(T_{j+1}) \geq w(T_j)$ (no-arbitrage), the interpolant is automatically non-decreasing.

The implied volatility is then:

$$
\sigma_{\text{IV}}(K, T) = \sqrt{\frac{w(T)}{T}}
$$

!!! note "Forward Variance"
    The **forward variance** between maturities $T_j$ and $T_{j+1}$ is:

    $$
    \sigma_{\text{fwd}}^2(T_j, T_{j+1}) = \frac{w(T_{j+1}) - w(T_j)}{T_{j+1} - T_j}
    $$

    Linear interpolation in total variance produces piecewise-constant forward variance, which is consistent with a piecewise-constant local volatility term structure.

### Higher-Order Interpolation

For smoother $\partial C / \partial T$ (needed in Dupire's numerator), quadratic or cubic interpolation in total variance can be used:

$$
w(T) = \alpha_0 + \alpha_1 T + \alpha_2 T^2 + \cdots
$$

subject to the constraint $w'(T) \geq 0$ for all $T$ in the domain. This is a constrained polynomial fitting problem, solvable by quadratic programming.

## Parametric Smile Models

### SVI Parametrization

The **Stochastic Volatility Inspired (SVI)** parametrization of Gatheral models total variance as:

$$
w(y) = a + b\left(\rho(y - m) + \sqrt{(y - m)^2 + \sigma^2}\right)
$$

where $y = \ln(K/F)$ is log-moneyness and the five parameters are:

- $a$: overall variance level
- $b > 0$: slope of the wings
- $\rho \in [-1, 1]$: rotation (controls skew)
- $m$: translation (shifts center)
- $\sigma > 0$: curvature (controls ATM smoothness)

**Properties:**

- **Wing behavior:** For $|y| \to \infty$, $w(y) \approx b(1 \pm \rho)|y|$, giving linear wings with slope $b(1 + \rho)$ on the right and $b(1 - \rho)$ on the left
- **Lee's moment formula:** Constrains $b(1 + |\rho|) \leq 2$
- **Minimum variance:** The minimum of $w(y)$ occurs near $y = m$ with value $a + b(\sigma\sqrt{1 - \rho^2})$

### SSVI Parametrization

The **Surface SVI (SSVI)** of Gatheral and Jacquier extends SVI to the full $(y, T)$ surface:

$$
w(y, T) = \frac{\theta_T}{2}\left(1 + \rho \varphi(\theta_T) y + \sqrt{(\varphi(\theta_T) y + \rho)^2 + (1 - \rho^2)}\right)
$$

where $\theta_T = \sigma_{\text{ATM}}^2(T) \cdot T$ is the ATM total variance at maturity $T$, and $\varphi(\theta)$ is a function controlling the wing behavior.

**Theorem 13.5.2** (SSVI Arbitrage-Free Conditions)
The SSVI parametrization is free of butterfly arbitrage if and only if:

$$
\varphi(\theta)\theta(1 + |\rho|) \leq 4
$$

and free of calendar spread arbitrage if $\partial_T \theta_T \geq 0$ and $\varphi$ satisfies certain monotonicity conditions.

The SSVI surface requires only three global parameters ($\rho$, and two parameters defining $\varphi$) plus the ATM variance term structure $\theta_T$, making it parsimonious and easy to calibrate.

### Calibration

SVI and SSVI parameters are fitted by minimizing the sum of squared differences between model and market implied volatilities:

$$
\min_{\text{params}} \sum_{i} w_i \left(\sigma_{\text{model}}(K_i, T_j) - \sigma_{\text{mkt}}(K_i, T_j)\right)^2
$$

subject to arbitrage-free constraints. The optimization is typically non-convex, so multiple starting points or global optimization algorithms (e.g., differential evolution) are used.

## Extrapolation

### Wing Extrapolation

Market data covers a finite range of strikes. Beyond the last observed strike, extrapolation is needed. Common approaches:

**Flat extrapolation:** Set $\sigma_{\text{IV}}(K, T) = \sigma_{\text{IV}}(K_{\text{last}}, T)$ for $K$ beyond the grid. This is simple but produces a kink in the second derivative, causing a discontinuity in the local volatility.

**Linear extrapolation in total variance:** Continue the linear wing behavior $w(y) \approx c_0 + c_1 |y|$ for large $|y|$. This is consistent with Lee's moment formula and SVI wing behavior.

**Power-law tail:** Set $\sigma_{\text{IV}}(K) \propto K^{-\beta}$ for small $K$ and $\sigma_{\text{IV}}(K) \propto K^{\alpha}$ for large $K$, with $\alpha, \beta$ chosen to match Lee's bounds.

!!! warning "Extrapolation Risk"
    The local volatility surface is particularly sensitive to extrapolation in the wings because Dupire's formula divides by $C_{KK}$, which becomes very small far from ATM. Small changes in wing extrapolation can cause large changes in the local volatility at extreme strikes. For robust results, ensure that extrapolation preserves convexity and produces bounded local volatility.

## Practical Workflow

### Step-by-Step Procedure

The complete smoothing pipeline from market data to a differentiable call price surface is:

**Step 1: Data cleaning.** Remove stale quotes, filter by bid-ask spread (exclude options with spreads exceeding a threshold), and use mid-prices.

**Step 2: Convert to implied volatility.** Invert the Black-Scholes formula for each market price to obtain $\sigma_{\text{IV}}(K_i, T_j)$.

**Step 3: Interpolate in strike.** For each maturity $T_j$, fit an SVI curve or smoothing spline to the IV data across strikes, enforcing butterfly constraints.

**Step 4: Interpolate in maturity.** For each strike $K_i$, interpolate total variance $w(T) = \sigma_{\text{IV}}^2 T$ across maturities, enforcing calendar constraints.

**Step 5: Extrapolate wings.** Extend the surface to cover the full domain needed for Dupire's formula, using linear-in-total-variance or parametric tail models.

**Step 6: Convert to call prices.** Apply the Black-Scholes formula with the smoothed $\sigma_{\text{IV}}(K, T)$ to obtain $\hat{C}(K, T)$.

**Step 7: Validate.** Check that $\hat{C}_{KK} > 0$, $\hat{C}_T > 0$, and $-1 < e^{rT}\hat{C}_K < 0$ at all grid points. If violations occur, tighten the smoothing constraints and refit.

### Quality Metrics

Assess the quality of the smoothed surface by:

1. **Pricing error:** $\text{RMSE} = \sqrt{\frac{1}{n}\sum_i (\hat{C}(K_i, T_j) - C_{\text{mkt}}(K_i, T_j))^2}$
2. **Arbitrage violations:** Count of grid points where $C_{KK} < 0$ or $C_T < 0$
3. **Local volatility bounds:** Range of $\sigma_{\text{loc}}$ — values outside $[1\%, 200\%]$ suggest surface problems
4. **Smoothness:** $\int |\sigma_{\text{loc}}''(K)|^2 \, dK$ — large values indicate remaining noise

## Summary

Interpolation and smoothing form the critical preprocessing step for local volatility construction:

1. **Raw market data** is too noisy for direct differentiation — smoothing is not optional but essential
2. **No-arbitrage constraints** (monotonicity, convexity, calendar) must be enforced to ensure $\sigma_{\text{loc}}^2 > 0$
3. **Cubic splines** in implied volatility with smoothing parameters provide flexible, differentiable fits
4. **SVI/SSVI parametrizations** offer parsimonious, arbitrage-free representations of the smile surface
5. **Total variance interpolation** in maturity naturally preserves calendar monotonicity
6. **Wing extrapolation** requires care, as Dupire's formula amplifies errors at extreme strikes

---

## Exercises

**Exercise 1.** Suppose call prices are observed at strikes $K = 90, 95, 100, 105, 110$ with values $C = 12.50, 8.80, 5.90, 3.70, 2.10$. Compute the centered second difference $C_{KK}$ at $K = 100$ using the standard formula. If the prices have noise of $\epsilon = \$0.03$, estimate the noise-to-signal ratio in $C_{KK}$.

??? success "Solution to Exercise 1"
    The centered second difference at $K = 100$ with $\Delta K = 5$ is:

    $$
    C_{KK}(100) \approx \frac{C(105) - 2C(100) + C(95)}{(\Delta K)^2} = \frac{3.70 - 2(5.90) + 8.80}{25} = \frac{0.70}{25} = 0.028
    $$

    The noise in the second difference is amplified by the division by $(\Delta K)^2$. Each price has noise $\epsilon = 0.03$. The second difference involves three prices, so the worst-case noise in the numerator is $4\epsilon$ (since $\text{Var}(C_{i+1} - 2C_i + C_{i-1}) = (1 + 4 + 1)\epsilon^2 = 6\epsilon^2$, giving standard deviation $\sqrt{6}\epsilon$). A simpler upper-bound estimate uses $4\epsilon$ for the numerator noise:

    $$
    \text{noise in } C_{KK} \approx \frac{4 \times 0.03}{25} = 0.0048
    $$

    The noise-to-signal ratio is:

    $$
    \frac{0.0048}{0.028} \approx 0.17
    $$

    So the noise is approximately 17% of the signal, which is already problematic. With a tighter strike grid ($\Delta K = 2$, say), the noise would scale as $4\epsilon / (\Delta K)^2 = 0.12/4 = 0.03$, and for a similar signal magnitude, the ratio would be even worse. This demonstrates why smoothing is essential before applying Dupire's formula.

---

**Exercise 2.** State and interpret the three no-arbitrage conditions (strike monotonicity, strike convexity, calendar monotonicity) for European call prices. For each condition, describe the specific arbitrage strategy that would be available if the condition were violated.

??? success "Solution to Exercise 2"
    **Condition 1: Strike monotonicity ($\partial C / \partial K \leq 0$).**
    Call prices must decrease as the strike increases, since a higher strike makes it harder for the option to finish in the money. If this were violated and $C(K_1) < C(K_2)$ with $K_1 < K_2$, then buy the cheap low-strike call and sell the expensive high-strike call. At expiry the payoff is $(S - K_1)^+ - (S - K_2)^+$, which is always non-negative (a bull call spread), and the initial cost is negative — a riskless profit.

    **Condition 2: Strike convexity ($\partial^2 C / \partial K^2 \geq 0$).**
    Call prices must be convex in strike. By the Breeden-Litzenberger result, $C_{KK} = e^{-rT}q(K)$ where $q(K)$ is the risk-neutral density, so convexity is equivalent to non-negative probabilities. If convexity is violated at some strike $K$, the butterfly spread with strikes $K - \Delta K$, $K$, $K + \Delta K$ has negative cost: buy one call at each wing and sell two at the center. The payoff at expiry is non-negative (a tent function), but the net premium received is positive — a riskless profit.

    **Condition 3: Calendar monotonicity ($\partial C / \partial T \geq 0$).**
    Call prices (equivalently, total implied variance $\sigma^2 T$) must be non-decreasing in maturity at each strike. A longer-dated option has all the exercise opportunities of a shorter-dated one plus more. If $C(K, T_1) > C(K, T_2)$ with $T_1 < T_2$, then buy the cheap long-dated call and sell the expensive short-dated call. At $T_1$, if the short call is exercised, the long call can be sold for at least its intrinsic value, covering the obligation. The initial cash inflow is positive — a calendar spread arbitrage.

---

**Exercise 3.** Given the SVI parametrization $w(y) = a + b(\rho(y - m) + \sqrt{(y - m)^2 + \sigma^2})$ with parameters $a = 0.04$, $b = 0.15$, $\rho = -0.3$, $m = 0$, $\sigma = 0.1$, compute:

(a) The total implied variance $w(y)$ at log-moneyness $y = -0.2$, $y = 0$, and $y = 0.2$.

(b) The wing slopes $b(1 + \rho)$ and $b(1 - \rho)$, and verify that Lee's moment formula constraint $b(1 + |\rho|) \leq 2$ is satisfied.

??? success "Solution to Exercise 3"
    **(a)** The SVI formula is $w(y) = a + b(\rho(y - m) + \sqrt{(y-m)^2 + \sigma^2})$.

    With $a = 0.04$, $b = 0.15$, $\rho = -0.3$, $m = 0$, $\sigma = 0.1$:

    At $y = -0.2$:

    $$
    w(-0.2) = 0.04 + 0.15\left(-0.3(-0.2) + \sqrt{(-0.2)^2 + 0.01}\right) = 0.04 + 0.15\left(0.06 + \sqrt{0.05}\right)
    $$

    $$
    = 0.04 + 0.15(0.06 + 0.2236) = 0.04 + 0.15(0.2836) = 0.04 + 0.04254 = 0.08254
    $$

    At $y = 0$:

    $$
    w(0) = 0.04 + 0.15\left(0 + \sqrt{0 + 0.01}\right) = 0.04 + 0.15(0.1) = 0.04 + 0.015 = 0.055
    $$

    At $y = 0.2$:

    $$
    w(0.2) = 0.04 + 0.15\left(-0.3(0.2) + \sqrt{0.04 + 0.01}\right) = 0.04 + 0.15(-0.06 + 0.2236)
    $$

    $$
    = 0.04 + 0.15(0.1636) = 0.04 + 0.02454 = 0.06454
    $$

    The skew is visible: $w(-0.2) > w(0.2)$, consistent with a negative $\rho$ producing higher implied variance on the downside.

    **(b)** The wing slopes are:

    - Right wing: $b(1 + \rho) = 0.15(1 + (-0.3)) = 0.15 \times 0.7 = 0.105$
    - Left wing: $b(1 - \rho) = 0.15(1 - (-0.3)) = 0.15 \times 1.3 = 0.195$

    Lee's moment formula requires $b(1 + |\rho|) \leq 2$:

    $$
    b(1 + |\rho|) = 0.15(1 + 0.3) = 0.195 \leq 2 \quad \checkmark
    $$

    The constraint is satisfied with a wide margin.

---

**Exercise 4.** Explain the tradeoff controlled by the smoothing parameter $\lambda$ in the smoothing spline objective:

$$
\min_{\hat{\sigma}} \left\{\sum_{i=1}^m w_i (\hat{\sigma}(K_i) - \sigma_i)^2 + \lambda \int (\hat{\sigma}''(K))^2 \, dK \right\}
$$

What happens in the limits $\lambda \to 0$ and $\lambda \to \infty$? How does leave-one-out cross-validation select $\lambda$ in a data-driven manner?

??? success "Solution to Exercise 4"
    The smoothing spline objective is:

    $$
    \min_{\hat{\sigma}} \left\{\sum_{i=1}^m w_i (\hat{\sigma}(K_i) - \sigma_i)^2 + \lambda \int (\hat{\sigma}''(K))^2 \, dK \right\}
    $$

    The first term measures fidelity to the data and the second penalizes curvature (roughness). The parameter $\lambda$ controls the tradeoff:

    **When $\lambda \to 0$:** The penalty vanishes and the objective reduces to minimizing the weighted sum of squared residuals with no smoothness constraint. The solution is the interpolating spline that passes exactly through every data point ($\hat{\sigma}(K_i) = \sigma_i$). This captures all noise in the data (overfitting).

    **When $\lambda \to \infty$:** The curvature penalty dominates, forcing $\hat{\sigma}''(K) \to 0$ everywhere. The solution approaches the weighted least-squares linear fit to the data — maximum smoothness but potentially poor fit to genuine smile curvature (underfitting).

    **Leave-one-out cross-validation (LOOCV)** selects $\lambda$ by measuring out-of-sample prediction error. For each candidate $\lambda$, the LOOCV score is:

    $$
    \text{CV}(\lambda) = \frac{1}{m}\sum_{i=1}^m \left(\frac{\hat{\sigma}(K_i) - \sigma_i}{1 - h_{ii}(\lambda)}\right)^2
    $$

    where $h_{ii}$ is the $i$-th diagonal of the hat matrix (the smoother matrix). This formula efficiently computes the average squared leave-one-out residual without actually refitting $m$ times. The $\lambda$ that minimizes $\text{CV}(\lambda)$ balances underfitting (large bias from too much smoothing) against overfitting (large variance from fitting noise), without requiring external knowledge of the noise level.

---

**Exercise 5.** Consider implied volatilities at two maturities: $\sigma_{\text{IV}}(K, T_1) = 20\%$ with $T_1 = 0.25$ and $\sigma_{\text{IV}}(K, T_2) = 22\%$ with $T_2 = 1.0$. Compute the total variances $w(T_1)$ and $w(T_2)$, verify the calendar monotonicity condition, and compute the forward variance $\sigma_{\text{fwd}}^2(T_1, T_2)$. What implied volatility does linear interpolation in total variance assign to $T = 0.5$?

??? success "Solution to Exercise 5"
    **Total variances:**

    $$
    w(T_1) = \sigma_{\text{IV}}^2(K, T_1) \cdot T_1 = (0.20)^2 \times 0.25 = 0.04 \times 0.25 = 0.01
    $$

    $$
    w(T_2) = \sigma_{\text{IV}}^2(K, T_2) \cdot T_2 = (0.22)^2 \times 1.0 = 0.0484 \times 1.0 = 0.0484
    $$

    **Calendar monotonicity check:** $w(T_2) = 0.0484 > w(T_1) = 0.01$, so total variance is increasing in maturity. The calendar constraint is satisfied.

    **Forward variance:**

    $$
    \sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1} = \frac{0.0484 - 0.01}{1.0 - 0.25} = \frac{0.0384}{0.75} = 0.0512
    $$

    So $\sigma_{\text{fwd}}(T_1, T_2) = \sqrt{0.0512} \approx 22.63\%$.

    **Linear interpolation at $T = 0.5$:**

    $$
    w(0.5) = w(0.25) + \frac{0.5 - 0.25}{1.0 - 0.25}(w(1.0) - w(0.25)) = 0.01 + \frac{0.25}{0.75}(0.0484 - 0.01)
    $$

    $$
    = 0.01 + \frac{1}{3}(0.0384) = 0.01 + 0.0128 = 0.0228
    $$

    The implied volatility at $T = 0.5$:

    $$
    \sigma_{\text{IV}}(K, 0.5) = \sqrt{\frac{w(0.5)}{0.5}} = \sqrt{\frac{0.0228}{0.5}} = \sqrt{0.0456} \approx 21.35\%
    $$

---

**Exercise 6.** Describe the complete seven-step practical workflow for transforming raw market option data into a smooth call price surface suitable for Dupire's formula. For each step, identify the primary source of error and the quality metric used to assess it.

??? success "Solution to Exercise 6"
    **Step 1: Data cleaning.**
    Remove stale quotes, filter by bid-ask spread width, and use mid-prices.
    *Primary error:* Stale or erroneous quotes contaminating the dataset.
    *Quality metric:* Percentage of quotes removed; comparison of mid-price consistency across nearby strikes.

    **Step 2: Convert to implied volatility.**
    Invert the Black-Scholes formula for each market price.
    *Primary error:* Root-finding inaccuracy for deep OTM options where vega is very small, and put-call parity violations if puts and calls imply different volatilities.
    *Quality metric:* Put-call parity residuals; verify that re-pricing from IV recovers the original price within tolerance.

    **Step 3: Interpolate in strike.**
    For each maturity, fit an SVI curve or smoothing spline to the IV data across strikes, enforcing the butterfly (convexity) constraint.
    *Primary error:* Overfitting (capturing noise, producing wiggly smile) or underfitting (missing genuine skew/kurtosis structure).
    *Quality metric:* RMSE of fit to market IVs; cross-validation score; number of butterfly constraint violations.

    **Step 4: Interpolate in maturity.**
    For each strike, interpolate total variance $w(T) = \sigma_{\text{IV}}^2 T$ across maturities, enforcing calendar monotonicity.
    *Primary error:* Large maturity gaps causing inaccurate interpolation; violation of calendar monotonicity.
    *Quality metric:* $\partial w / \partial T \geq 0$ at all grid points; smoothness of the forward variance curve.

    **Step 5: Extrapolate wings.**
    Extend the surface beyond observed strikes using linear-in-total-variance tails or parametric models consistent with Lee's moment formula.
    *Primary error:* Arbitrary wing behavior that produces unbounded or negative local volatility at extreme strikes.
    *Quality metric:* Boundedness of local volatility in the wings; consistency with Lee's moment bounds $\limsup_{|y|\to\infty} w(y)/|y| \leq 2$.

    **Step 6: Convert to call prices.**
    Apply the Black-Scholes formula with the smoothed $\sigma_{\text{IV}}(K,T)$ to produce $\hat{C}(K,T)$.
    *Primary error:* Propagation of IV interpolation errors into price space.
    *Quality metric:* $|\hat{C}(K_i, T_j) - C_{\text{mkt}}(K_i, T_j)|$ at observed points; bid-ask containment.

    **Step 7: Validate.**
    Check that $\hat{C}_{KK} > 0$, $\hat{C}_T > 0$, and $-1 < e^{rT}\hat{C}_K < 0$ at all grid points.
    *Primary error:* Residual arbitrage violations that would produce negative or infinite local volatility.
    *Quality metric:* Count of grid points with any arbitrage violation; range of $\sigma_{\text{loc}}^2$ values computed via Dupire's formula.
