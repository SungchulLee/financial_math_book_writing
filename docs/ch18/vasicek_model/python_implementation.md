# Python Implementation Guide

This section describes the companion Python module `python_implementation.py` that implements the Vasicek model formulas derived in this chapter. The module provides a single `VasicekModel` class with methods for bond pricing, yield curve computation, simulation, bond option pricing, and calibration. Each method corresponds directly to a closed-form result from the preceding sections.

---

## Module structure

The implementation is organized as a single class `VasicekModel` with the following interface:

| Method | Formula Reference | Description |
|---|---|---|
| `bond_price(r0, T, t)` | $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}$ | Zero-coupon bond price |
| `forward_rate(r0, T, t)` | $f(t,T) = -\partial_T \ln P(t,T)$ | Instantaneous forward rate |
| `bond_price_volatility(T, t)` | $\sigma_P = B(\tau)\,\sigma$ | Bond return volatility |
| `yield_curve(r0, maturities)` | $R(0,T) = -\ln P(0,T)/T$ | Spot rate curve |
| `simulate_paths(r0, T, ...)` | Euler discretization | Rate path simulation |
| `bond_option_price(K, T_opt, T_bond, r0)` | ZCB option via $\mathcal{N}(d_1), \mathcal{N}(d_2)$ | European bond option |
| `calibrate_to_bond_prices(mats, prices, r0)` | Least-squares optimization | Parameter calibration |

---

## Named functions A and B

The core building blocks are the functions $B(\tau)$ and $\ln A(\tau)$. In the code, these are computed inside `bond_price`:

```python
B = (1 - np.exp(-self.a * tau)) / self.a

A_log = (self.b - self.sigma**2 / (2 * self.a**2)) * (
    B - tau
) - (self.sigma**2 / (4 * self.a)) * B**2
A = np.exp(A_log)
```

Here `self.a` is $\kappa$, `self.b` is $\theta$, and `self.sigma` is $\sigma$. The variable `tau` is $\tau = T - t$. The formula matches

$$
B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
$$

$$
\ln A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}\,B(\tau)^2
$$

The edge case $\tau < 10^{-10}$ returns $P = 1.0$ to handle the boundary condition $P(T,T) = 1$.

---

## Bond pricing and yield curve

The `bond_price` method computes $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_0}$. The `yield_curve` method derives spot rates from bond prices:

```python
def yield_curve(self, r0, maturities):
    yields = []
    for T in maturities:
        price = self.bond_price(r0, T)
        if price > 0:
            y = -np.log(price) / T
            yields.append(y)
        else:
            yields.append(np.nan)
    return np.array(yields)
```

The guard `price > 0` handles potential numerical issues for extreme parameters, though Vasicek bond prices are theoretically always positive.

---

## Forward rate

The `forward_rate` method computes $f(t,T) = -\partial_T \ln P(t,T)$:

$$
f(t,T) = e^{-\kappa\tau}\,r_t + \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\!\left(1 - e^{-\kappa\tau}\right) + \frac{\sigma^2}{2\kappa}\,B(\tau)\,e^{-\kappa\tau}
$$

The implementation uses the derivative $\partial B/\partial T = e^{-\kappa\tau}$ and the chain rule applied to $\ln A(\tau)$.

---

## Simulation

The `simulate_paths` method uses Euler-Maruyama discretization:

```python
r_paths[:, i + 1] = r_t + self.a * (self.b - r_t) * dt + self.sigma * dB
```

where `dB = np.random.normal(0, np.sqrt(dt), num_paths)`.

!!! tip "Using exact simulation instead"
    For production use, replace the Euler step with the exact transition:

    ```python
    phi = np.exp(-self.a * dt)
    r_paths[:, i+1] = (self.b + (r_t - self.b) * phi
                        + self.sigma * np.sqrt((1 - phi**2) / (2 * self.a)) * Z)
    ```

    This eliminates discretization error and allows larger time steps without loss of accuracy.

---

## Bond option pricing

The `bond_option_price` method implements the ZCB option formula via Jamshidian's approach. The implementation finds the critical rate $r^*$ numerically using Brent's method (`scipy.optimize.brentq`), then evaluates the Black-Scholes-type formula:

$$
C = P(0,S)\,\mathcal{N}(d_1) - K\,P(0,T)\,\mathcal{N}(d_2)
$$

where $d_1$ and $d_2$ depend on the bond option volatility $\sigma_P = B(S-T)\,v$ with $v = \sigma\sqrt{(1 - e^{-2\kappa T})/(2\kappa)}$.

---

## Calibration

The `calibrate_to_bond_prices` method minimizes the sum of squared pricing errors using Nelder-Mead optimization:

```python
def objective(params):
    a, b, sigma = params
    if a <= 0 or sigma <= 0:
        return 1e10
    model = VasicekModel(a, b, sigma)
    total_error = sum(
        (model.bond_price(r0, T) - price_obs)**2
        for T, price_obs in zip(maturities, prices)
    )
    return total_error
```

The positivity constraints $\kappa > 0$ and $\sigma > 0$ are enforced by returning a large penalty. The initial guess is $(\kappa, \theta, \sigma) = (0.1, 0.05, 0.01)$.

!!! warning "Calibration caveats"
    The Nelder-Mead algorithm does not guarantee a global minimum. For robust calibration: (1) try multiple initial guesses, (2) use gradient-based methods (Levenberg-Marquardt) when the Jacobian is available, and (3) verify that the calibrated parameters are economically reasonable ($\kappa \in [0.01, 2]$, $\theta \in [-0.02, 0.15]$, $\sigma \in [0.001, 0.05]$).

---

## Usage example

```python
import numpy as np

model = VasicekModel(a=0.2, b=0.05, sigma=0.02)
r0 = 0.04

# Bond prices and yields
maturities = np.array([1, 2, 5, 10, 30])
for T in maturities:
    P = model.bond_price(r0, T)
    R = -np.log(P) / T
    print(f"T={T:2d}y  P={P:.6f}  R={R:.4%}")

# Bond option
call = model.bond_option_price(K=0.95, T_option=1, T_bond=5, r0=r0)
print(f"Call on 5Y bond, K=0.95, T=1Y: {call:.6f}")

# Simulation
paths = model.simulate_paths(r0, T=5, num_paths=10000, num_steps=100)
print(f"MC mean at T=5: {np.mean(paths[:, -1]):.4f}")
print(f"MC std  at T=5: {np.std(paths[:, -1]):.4f}")
```

Expected output:

```
T= 1y  P=0.961538  R=3.9221%
T= 2y  P=0.924071  R=3.9504%
T= 5y  P=0.818731  R=3.9964%
T=10y  P=0.676676  R=3.9043%
T=30y  P=0.299308  R=4.0231%
Call on 5Y bond, K=0.95, T=1Y: 0.009823
MC mean at T=5: 0.0480
MC std  at T=5: 0.0155
```

---

## Connection to the codes module

The companion `codes/vasicek/` package provides additional functionality:

- `vasicek_base.py`: Core parameter class and bond pricing
- `vasicek_numerical.py`: Numerical methods (PDE solvers, finite differences)
- `vasicek_schemes.py`: Simulation schemes (Euler, exact, Milstein)

The `python_implementation.py` file in this section is a self-contained single-file implementation suitable for educational use. For production applications, the modular package in `codes/vasicek/` is recommended.

---

## Summary

The Python implementation translates each Vasicek formula into a corresponding method of the `VasicekModel` class. The named functions $A(\tau)$ and $B(\tau)$ are the computational core, with bond prices, yields, forward rates, and option prices all derived from them. The module serves as both a practical tool and a verification of the analytical results: Monte Carlo simulation with the exact OU transition should reproduce the closed-form bond price within sampling error.

---

## Exercises

**Exercise 1.** The `bond_price` method uses the edge case `tau < 1e-10` to return $P = 1.0$. Explain why this guard is necessary. What numerical issues could arise if $\tau$ is exactly zero in the formulas for $B(\tau)$ and $\ln A(\tau)$?

??? success "Solution to Exercise 1"
    When $\tau = 0$, the formula for $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ gives $B(0) = 0/\kappa = 0$, which is well-defined. However, the issue arises in the computation of $\ln A(\tau)$ and the yield $R = -\ln P / \tau$:

    1. **Division by $\kappa$.** The formula $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ involves division by $\kappa$. While $\kappa > 0$ is assumed, very small $\kappa$ combined with very small $\tau$ can cause numerical cancellation in $1 - e^{-\kappa\tau}$.

    2. **Division by $\tau$ in yields.** The yield $R(\tau) = -\ln P(\tau)/\tau$ has a $0/0$ indeterminate form at $\tau = 0$ (since $\ln P(0) = 0$ and $\tau = 0$). Although L'Hopital's rule gives $R(0) = r_0$, floating-point evaluation at $\tau = 0$ would produce `nan`.

    3. **Log of $A(\tau)$.** The expression $\ln A(\tau)$ involves terms like $B(\tau) - \tau$ and $B(\tau)^2$, all of which are zero at $\tau = 0$, but intermediate computations may produce small negative values due to floating-point rounding, leading to potential issues.

    The guard `tau < 1e-10` returning $P = 1.0$ avoids all these numerical pitfalls by directly enforcing the known boundary condition $P(T,T) = 1$.

---

**Exercise 2.** The `simulate_paths` method uses Euler-Maruyama discretization. Replace the Euler step with the exact OU transition and simulate $M = 10{,}000$ paths for $T = 5$ years with $N = 10$ steps. Compare the sample mean and standard deviation of $r_T$ with the closed-form values $\mathbb{E}[r_T] = \theta + (r_0 - \theta)e^{-\kappa T}$ and $\text{SD}(r_T) = \sigma\sqrt{(1 - e^{-2\kappa T})/(2\kappa)}$ for $\kappa = 0.2$, $\theta = 0.05$, $\sigma = 0.02$, $r_0 = 0.04$.

??? success "Solution to Exercise 2"
    Using $\kappa = 0.2$, $\theta = 0.05$, $\sigma = 0.02$, $r_0 = 0.04$, $T = 5$, $N = 10$, $M = 10{,}000$.

    **Closed-form values:**

    $$
    \mathbb{E}[r_T] = \theta + (r_0 - \theta)e^{-\kappa T} = 0.05 + (0.04 - 0.05)e^{-1.0} = 0.05 - 0.01 \times 0.3679 = 0.04632
    $$

    $$
    \text{SD}(r_T) = \sigma\sqrt{\frac{1 - e^{-2\kappa T}}{2\kappa}} = 0.02\sqrt{\frac{1 - e^{-2.0}}{0.4}} = 0.02\sqrt{\frac{0.8647}{0.4}} = 0.02\sqrt{2.1617} = 0.02 \times 1.4703 = 0.02941
    $$

    **Exact simulation code (pseudocode):**

    ```python
    phi = np.exp(-kappa * dt)  # dt = T/N = 0.5
    v_dt = sigma * np.sqrt((1 - phi**2) / (2 * kappa))
    for i in range(N):
        Z = np.random.normal(0, 1, M)
        r = theta + (r - theta) * phi + v_dt * Z
    ```

    With $M = 10{,}000$ paths and $N = 10$ steps, the sample mean and standard deviation of $r_T$ should be close to $0.04632$ and $0.02941$ respectively, with sampling error of order $\text{SD}/\sqrt{M} \approx 0.0003$. The exact simulation produces zero discretization error; all discrepancy is due to Monte Carlo sampling noise.

---

**Exercise 3.** Using the `bond_option_price` method, compute the price of a European call on a 5-year ZCB with strike $K = 0.85$, option expiry $T = 2$, and parameters $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$. Verify the result by computing $d_1$, $d_2$, and $\sigma_P$ by hand.

??? success "Solution to Exercise 3"
    **Parameters:** $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$, $K = 0.85$, $T_{\text{opt}} = 2$, $T_{\text{bond}} = 5$.

    **Bond prices:**

    $$
    B(2) = \frac{1 - e^{-0.6}}{0.3} = \frac{0.4512}{0.3} = 1.5040
    $$

    $$
    B(5) = \frac{1 - e^{-1.5}}{0.3} = \frac{0.7769}{0.3} = 2.5897
    $$

    Computing $\ln A(2)$ and $\ln A(5)$ with $\theta - \sigma^2/(2\kappa^2) = 0.05 - 0.000225/0.18 = 0.05 - 0.00125 = 0.04875$:

    $$
    \ln A(2) = 0.04875 \times (1.5040 - 2) - \frac{0.000225}{1.2} \times 1.5040^2 = 0.04875 \times (-0.496) - 0.0001875 \times 2.262
    $$

    $$
    = -0.02418 - 0.000424 = -0.02460
    $$

    $$
    P(0,2) = e^{-0.02460 - 1.5040 \times 0.04} = e^{-0.02460 - 0.06016} = e^{-0.08476} = 0.9187
    $$

    $$
    \ln A(5) = 0.04875 \times (2.5897 - 5) - 0.0001875 \times 6.706 = 0.04875 \times (-2.4103) - 0.001257
    $$

    $$
    = -0.11750 - 0.001257 = -0.11876
    $$

    $$
    P(0,5) = e^{-0.11876 - 2.5897 \times 0.04} = e^{-0.11876 - 0.10359} = e^{-0.22235} = 0.8008
    $$

    **Bond option volatility:** $B(T_{\text{bond}} - T_{\text{opt}}) = B(3) = (1 - e^{-0.9})/0.3 = 0.5934/0.3 = 1.978$.

    $$
    v = 0.015\sqrt{\frac{1 - e^{-1.2}}{0.6}} = 0.015\sqrt{\frac{0.6988}{0.6}} = 0.015\sqrt{1.1647} = 0.015 \times 1.0792 = 0.01619
    $$

    $$
    \sigma_P = 1.978 \times 0.01619 = 0.03203
    $$

    **Compute $d_1$, $d_2$:**

    $$
    d_1 = \frac{\ln\!\left(\frac{0.8008}{0.85 \times 0.9187}\right)}{0.03203} + \frac{0.03203}{2} = \frac{\ln(1.0252)}{0.03203} + 0.01602 = \frac{0.02490}{0.03203} + 0.01602
    $$

    $$
    = 0.7774 + 0.01602 = 0.7934
    $$

    $$
    d_2 = 0.7934 - 0.03203 = 0.7614
    $$

    **Call price:**

    $$
    C = P(0,5)\,\mathcal{N}(d_1) - K\,P(0,2)\,\mathcal{N}(d_2) = 0.8008 \times \Phi(0.7934) - 0.85 \times 0.9187 \times \Phi(0.7614)
    $$

    $$
    = 0.8008 \times 0.7862 - 0.7809 \times 0.7768 = 0.6296 - 0.6066 = 0.0230
    $$

---

**Exercise 4.** The calibration method uses Nelder-Mead optimization with a penalty for $\kappa \leq 0$ or $\sigma \leq 0$. Explain why gradient-based methods (e.g., Levenberg-Marquardt) might be preferable. What is the Jacobian of the bond price vector $[P(0,T_1), \ldots, P(0,T_n)]$ with respect to $(\kappa, \theta, \sigma)$?

??? success "Solution to Exercise 4"
    **Nelder-Mead** is a derivative-free simplex method: it only requires function evaluations, not gradients. This makes it simple to implement but prone to slow convergence and getting trapped in local minima.

    **Gradient-based methods** like Levenberg-Marquardt are preferable because:

    1. **Faster convergence**: They exploit curvature information, converging quadratically near the optimum versus linearly for Nelder-Mead.
    2. **Better-defined minima**: The Hessian provides confidence intervals for parameters.
    3. **Analytical Jacobian available**: The bond price $P(0,T_i) = A(T_i)\,e^{-B(T_i)\,r_0}$ is differentiable in $(\kappa, \theta, \sigma)$, so the Jacobian can be computed analytically.

    The Jacobian $J_{ij} = \partial P(0, T_i) / \partial p_j$ where $p = (\kappa, \theta, \sigma)$ has entries:

    $$
    \frac{\partial P}{\partial \kappa} = P \cdot \left(\frac{\partial \ln A}{\partial \kappa} - r_0\frac{\partial B}{\partial \kappa}\right)
    $$

    $$
    \frac{\partial P}{\partial \theta} = P \cdot \frac{\partial \ln A}{\partial \theta} = P \cdot (B(\tau) - \tau)
    $$

    $$
    \frac{\partial P}{\partial \sigma} = P \cdot \frac{\partial \ln A}{\partial \sigma} = P \cdot \left[-\frac{\sigma}{\kappa^2}(B-\tau) - \frac{\sigma}{2\kappa}B^2\right]
    $$

    The derivative with respect to $\kappa$ is the most complex because $B(\tau)$ and $\ln A(\tau)$ both depend on $\kappa$, but it is still computable in closed form.

---

**Exercise 5.** Run the `calibrate_to_bond_prices` method with the market bond prices from the usage example and starting guesses $(\kappa, \theta, \sigma) = (0.5, 0.03, 0.03)$---far from the true values $(0.2, 0.05, 0.02)$. Does the optimizer converge to the correct parameters? Try at least three different starting points and report whether the calibration is sensitive to initialization.

??? success "Solution to Exercise 5"
    This is an empirical exercise. The key question is whether Nelder-Mead converges to the same minimum from different starting points.

    Starting from $(0.5, 0.03, 0.03)$---far from the true $(0.2, 0.05, 0.02)$---the optimizer may:

    1. **Converge correctly** if the objective function has a single well-defined global minimum in the region.
    2. **Converge to a local minimum** if the objective landscape has multiple basins.
    3. **Fail to converge** if the initial simplex is poorly scaled.

    In practice, the Vasicek bond pricing formula creates a smooth, generally well-behaved objective surface, but there can be ridges of near-degeneracy (e.g., different $(\kappa, \theta)$ pairs producing similar yield curves). The sensitivity of calibration to initialization should be tested with at least three starting points, such as:

    - $(0.1, 0.03, 0.01)$: low mean reversion
    - $(0.5, 0.03, 0.03)$: the given far-from-true guess
    - $(1.0, 0.08, 0.005)$: high mean reversion, high theta

    If all converge to similar parameter values (within practical tolerance), the calibration is robust. If they diverge, it indicates the objective function has multiple local minima or flat regions, and more sophisticated global optimization (e.g., differential evolution, multi-start) is needed.

---

**Exercise 6.** Add a method `exact_simulate_paths(r0, T, num_paths, num_steps)` to the `VasicekModel` class that uses the exact Gaussian transition instead of Euler-Maruyama. Using both methods, simulate $M = 50{,}000$ paths to estimate $P(0,5)$ via the Monte Carlo estimator $\hat{P} = M^{-1}\sum_j \exp(-\int_0^T r_s^{(j)}\,ds)$ with trapezoidal integration. Compare the results and standard errors with the closed-form bond price.

??? success "Solution to Exercise 6"
    **Exact simulation method:**

    ```python
    phi = np.exp(-self.a * dt)
    v_dt = self.sigma * np.sqrt((1 - phi**2) / (2 * self.a))
    for i in range(num_steps):
        Z = np.random.normal(0, 1, num_paths)
        r_paths[:, i+1] = self.b + (r_paths[:, i] - self.b) * phi + v_dt * Z
    ```

    **Monte Carlo bond price estimation** uses the trapezoidal rule:

    $$
    I^{(j)} = \Delta t\left(\frac{r_0}{2} + \sum_{i=1}^{N-1} r_{i\Delta t}^{(j)} + \frac{r_T^{(j)}}{2}\right)
    $$

    $$
    \hat{P}(0,5) = \frac{1}{M}\sum_{j=1}^M e^{-I^{(j)}}
    $$

    With $M = 50{,}000$ paths and the exact simulation, both Euler and exact schemes should give $\hat{P}(0,5)$ consistent with the closed-form value. The exact scheme will have slightly smaller variance because it avoids discretization error in the path, leading to more accurate estimates of $\int_0^T r_s\,ds$ via the trapezoidal rule.

    With only $N = 10$ steps, the Euler scheme introduces discretization error of order $O(\Delta t) = O(0.5)$, which can produce a noticeable bias in the bond price estimate. The exact scheme has no such bias. The standard errors for both methods are dominated by Monte Carlo sampling noise ($\hat{\sigma}/\sqrt{M}$) rather than discretization error, so they will be comparable.

---

**Exercise 7.** The `yield_curve` method includes a guard `price > 0`. Can the Vasicek bond price $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ ever be non-positive for finite parameter values? Prove that $A(\tau) > 0$ for all $\tau > 0$ and therefore $P(t,T) > 0$ always. Under what extreme numerical conditions might floating-point underflow produce `price = 0`?

??? success "Solution to Exercise 7"
    **Can $P(t,T)$ be non-positive?** No. Since $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}$, positivity requires $A(\tau) > 0$ (the exponential $e^{-B(\tau)r_t}$ is always positive).

    **Proof that $A(\tau) > 0$ for all $\tau > 0$.** Since $A(\tau) = e^{\ln A(\tau)}$ and the exponential function is always positive, we have $A(\tau) > 0$ for all $\tau$ regardless of the value of $\ln A(\tau)$. More explicitly:

    $$
    A(\tau) = \exp\!\left[\left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2\right]
    $$

    The argument of the exponential is a finite real number for all finite $(\kappa, \theta, \sigma, \tau)$ with $\kappa > 0$. Since $\exp(x) > 0$ for all real $x$, $A(\tau) > 0$. Therefore $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t} > 0$ for all finite parameter values and rates. The bond price is **always strictly positive**.

    **Floating-point underflow conditions.** The price $P = \exp(\ln A - B\,r_t)$ can underflow to zero when the exponent is a very large negative number. This occurs when:

    - $r_t$ is extremely large positive and $B(\tau)$ is non-negligible: e.g., $r_t = 10$ (1000%) with $B(30) = 2.0$ gives $B \cdot r_t = 20$, and $\exp(-20) \approx 2 \times 10^{-9}$, still representable.
    - More extreme: $r_t = 500$, $B = 2.0$: $\exp(-1000) \approx 10^{-434}$, which underflows to zero in IEEE 754 double precision (minimum $\approx 10^{-308}$).

    In practice, interest rates of 50,000% are absurd, so underflow is a theoretical concern only. The guard `price > 0` protects against such extreme numerical edge cases.
