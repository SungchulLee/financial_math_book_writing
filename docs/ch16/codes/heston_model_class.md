# Heston Model Class

A well-designed model class serves as the single source of truth for parameters, validation, and derived quantities. Every pricing engine---characteristic function, COS, FFT, Monte Carlo, and FDM---needs the same five Heston parameters plus market data. Centralizing these in a `HestonModel` class eliminates duplication, enforces consistency, and makes the codebase easier to extend. This guide walks through the class design, explains the mathematical constraints behind each validation check, and shows how the class integrates with downstream pricing engines.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Design a `HestonModel` class that stores, validates, and exposes the five Heston parameters plus market data
    2. Implement parameter validation checks with clear mathematical justifications
    3. Compute derived quantities (Feller ratio, mean-reversion half-life, stationary moments) from stored parameters
    4. Connect the model class to pricing engines through a consistent interface

!!! tip "Prerequisites"
    This section builds on the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md) and the [Feller condition](../model_definition/feller_condition_and_boundary.md). The companion implementation is in [`heston_model_class.py`](heston_model_class.md).

---

## The Heston SDE System

Recall the risk-neutral Heston dynamics:

$$
dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

with $d\langle W^{(1)}, W^{(2)} \rangle_t = \rho \, dt$. The five model parameters are:

| Parameter | Symbol | Domain | Interpretation |
|---|---|---|---|
| Initial variance | $v_0$ | $(0, \infty)$ | Variance at $t = 0$ |
| Mean-reversion speed | $\kappa$ | $(0, \infty)$ | Rate of pull toward $\theta$ |
| Long-run variance | $\theta$ | $(0, \infty)$ | Stationary mean of $v_t$ |
| Vol-of-vol | $\xi$ | $(0, \infty)$ | Diffusion coefficient of $v_t$ |
| Correlation | $\rho$ | $(-1, 1)$ | Correlation between $dW^{(1)}$ and $dW^{(2)}$ |

The market data consists of: spot price $S_0 > 0$, risk-free rate $r \geq 0$, and dividend yield $q \geq 0$.

---

## Class Design

The `HestonModel` class stores all parameters and market data in a single object. The design follows three principles:

1. **Immutable after construction**: Parameters are set at initialization and cannot be silently modified. To change parameters, create a new instance.
2. **Validate on construction**: All mathematical constraints are checked in `__init__`. Invalid parameters raise an exception immediately rather than producing silent errors downstream.
3. **Expose derived quantities**: Frequently needed quantities (Feller ratio, half-life, stationary moments) are computed once and cached as properties.

### Constructor

```python
class HestonModel:
    def __init__(self, S0, r, q, v0, kappa, theta, xi, rho):
        # Market data
        self.S0 = float(S0)
        self.r = float(r)
        self.q = float(q)

        # Model parameters
        self.v0 = float(v0)
        self.kappa = float(kappa)
        self.theta = float(theta)
        self.xi = float(xi)
        self.rho = float(rho)

        # Validate
        self._validate()
```

### Validation Method

The `_validate` method enforces the mathematical domain constraints:

```python
def _validate(self):
    if self.S0 <= 0:
        raise ValueError(f"S0 must be positive, got {self.S0}")
    if self.v0 <= 0:
        raise ValueError(f"v0 must be positive, got {self.v0}")
    if self.kappa <= 0:
        raise ValueError(f"kappa must be positive, got {self.kappa}")
    if self.theta <= 0:
        raise ValueError(f"theta must be positive, got {self.theta}")
    if self.xi <= 0:
        raise ValueError(f"xi must be positive, got {self.xi}")
    if not (-1 < self.rho < 1):
        raise ValueError(f"rho must be in (-1, 1), got {self.rho}")
```

!!! warning "Do Not Enforce the Feller Condition in Validation"
    The Feller condition $2\kappa\theta \geq \xi^2$ ensures strict positivity of $v_t$, but many market-calibrated parameters violate it. The class should **warn** about Feller violation (since it affects simulation accuracy) but not **reject** such parameters. Validation enforces the hard mathematical domain constraints; the Feller condition is a soft recommendation.

### Feller Condition Check

```python
@property
def feller_ratio(self):
    """2 * kappa * theta / xi^2. Values >= 1 satisfy the Feller condition."""
    return 2 * self.kappa * self.theta / self.xi**2

@property
def feller_satisfied(self):
    return self.feller_ratio >= 1.0
```

The **Feller ratio** $\mathcal{F} = 2\kappa\theta / \xi^2$ is a dimensionless diagnostic:

- $\mathcal{F} \geq 1$: Feller condition satisfied, $v_t > 0$ a.s.
- $\mathcal{F} < 1$: Feller condition violated, $v_t$ touches zero with positive probability

---

## Derived Quantities

Several quantities that depend on the stored parameters are useful for diagnostics and downstream calculations.

### Mean-Reversion Half-Life

The expected variance at time $t$ given $v_0$ is:

$$
\mathbb{E}[v_t] = \theta + (v_0 - \theta) e^{-\kappa t}
$$

The **half-life** of mean-reversion is the time for the expected gap $v_0 - \theta$ to halve:

$$
t_{1/2} = \frac{\ln 2}{\kappa}
$$

```python
@property
def half_life(self):
    """Mean-reversion half-life in years."""
    return np.log(2) / self.kappa
```

### Stationary Distribution Moments

In the limit $t \to \infty$, $v_t$ converges to its stationary (gamma) distribution with moments:

$$
\mathbb{E}[v_\infty] = \theta, \qquad \text{Var}[v_\infty] = \frac{\theta \xi^2}{2\kappa}, \qquad \text{Std}[v_\infty] = \xi \sqrt{\frac{\theta}{2\kappa}}
$$

```python
@property
def stationary_mean(self):
    return self.theta

@property
def stationary_std(self):
    return self.xi * np.sqrt(self.theta / (2 * self.kappa))
```

### ATM Implied Volatility Approximation

For short maturities, the ATM implied volatility is approximately $\sigma_{\text{ATM}} \approx \sqrt{v_0}$. For longer maturities, the average expected variance provides a better approximation:

$$
\sigma_{\text{ATM}}(T) \approx \sqrt{\bar{v}(T)} = \sqrt{\theta + (v_0 - \theta) \frac{1 - e^{-\kappa T}}{\kappa T}}
$$

```python
def atm_vol_approx(self, T):
    """Approximate ATM implied volatility for maturity T."""
    if T < 1e-10:
        return np.sqrt(self.v0)
    avg_var = self.theta + (self.v0 - self.theta) * (
        1 - np.exp(-self.kappa * T)
    ) / (self.kappa * T)
    return np.sqrt(max(avg_var, 0))
```

---

## String Representation

A readable `__repr__` is valuable for debugging and logging:

```python
def __repr__(self):
    feller = "satisfied" if self.feller_satisfied else "VIOLATED"
    return (
        f"HestonModel(S0={self.S0:.2f}, r={self.r:.4f}, q={self.q:.4f},\n"
        f"  v0={self.v0:.6f}, kappa={self.kappa:.4f}, "
        f"theta={self.theta:.6f},\n"
        f"  xi={self.xi:.4f}, rho={self.rho:.4f},\n"
        f"  Feller ratio={self.feller_ratio:.3f} [{feller}],\n"
        f"  half-life={self.half_life:.2f}y)"
    )
```

---

## Integration with Pricing Engines

The `HestonModel` class serves as input to all pricing engines. Each engine extracts the parameters it needs:

```python
# Characteristic function engine
cf_engine = HestonCFEngine(model)
price = cf_engine.call_price(K=100, T=0.5)

# COS method engine
cos_engine = HestonCOSEngine(model, N=128)
prices = cos_engine.call_prices(strikes=[90, 100, 110], T=0.5)

# Monte Carlo engine
mc_engine = HestonMCEngine(model, scheme="QE")
price, std_err = mc_engine.call_price(K=100, T=0.5, n_paths=100_000)
```

The key design decision is that engines receive the **model object**, not individual parameters. This prevents parameter mismatch errors (e.g., passing different $v_0$ to the pricing engine and the Greeks engine).

---

## Worked Example

Create a Heston model with typical equity parameters and inspect its diagnostics:

```python
model = HestonModel(
    S0=100, r=0.03, q=0.01,
    v0=0.04, kappa=2.0, theta=0.04, xi=0.5, rho=-0.7
)
print(model)
```

Output:

```
HestonModel(S0=100.00, r=0.0300, q=0.0100,
  v0=0.040000, kappa=2.0000, theta=0.040000,
  xi=0.5000, rho=-0.7000,
  Feller ratio=0.640 [VIOLATED],
  half-life=0.35y)
```

Key observations:

1. The Feller ratio is 0.64 < 1, so the Feller condition is **violated**. The variance process will touch zero, requiring careful treatment in Monte Carlo simulation (e.g., the QE scheme).
2. The half-life is 0.35 years, meaning the variance reverts halfway to $\theta$ in about 4.2 months.
3. The stationary standard deviation of $v$ is $0.5 \sqrt{0.04/4} = 0.05$, so $v_\infty$ fluctuates roughly in the range $[0.04 \pm 0.10]$ (two standard deviations), implying realized volatility between 0% and 37%.

Compute the approximate ATM term structure:

```python
for T in [0.08, 0.25, 0.5, 1.0, 2.0, 5.0]:
    print(f"T={T:.2f}y: ATM vol ~ {model.atm_vol_approx(T)*100:.1f}%")
```

Since $v_0 = \theta = 0.04$, the term structure is flat at approximately 20% across all maturities.

---

## Summary

The `HestonModel` class encapsulates the five model parameters and market data in a single validated object. Construction-time validation enforces the mathematical domain constraints ($v_0 > 0$, $\kappa > 0$, $\theta > 0$, $\xi > 0$, $|\rho| < 1$) while issuing warnings for Feller condition violations. Derived properties---Feller ratio, half-life, stationary moments, and ATM volatility approximation---provide immediate diagnostic insight without recomputation. By passing the model object (not individual parameters) to pricing engines, the design eliminates parameter mismatch errors and provides a clean separation between model specification and numerical computation.

---

## Exercises

**Exercise 1.**
For the model $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, compute the Feller ratio, mean-reversion half-life, stationary mean, and stationary standard deviation. Verify that the Feller condition is violated. If you were to increase $\kappa$ to satisfy Feller while keeping all other parameters fixed, what is the minimum $\kappa$ required?

??? success "Solution to Exercise 1"
    Given $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$:

    **Feller ratio:**

    $$
    \mathcal{F} = \frac{2\kappa\theta}{\xi^2} = \frac{2 \times 2.0 \times 0.04}{0.5^2} = \frac{0.16}{0.25} = 0.64
    $$

    Since $\mathcal{F} = 0.64 < 1$, the Feller condition is **violated**.

    **Mean-reversion half-life:**

    $$
    t_{1/2} = \frac{\ln 2}{\kappa} = \frac{0.6931}{2.0} = 0.347 \text{ years} \approx 4.2 \text{ months}
    $$

    **Stationary mean:**

    $$
    \mathbb{E}[v_\infty] = \theta = 0.04
    $$

    **Stationary standard deviation:**

    $$
    \text{Std}[v_\infty] = \xi\sqrt{\frac{\theta}{2\kappa}} = 0.5\sqrt{\frac{0.04}{4.0}} = 0.5\sqrt{0.01} = 0.5 \times 0.1 = 0.05
    $$

    **Minimum $\kappa$ to satisfy Feller:**

    The Feller condition requires $2\kappa\theta \geq \xi^2$:

    $$
    \kappa \geq \frac{\xi^2}{2\theta} = \frac{0.25}{2 \times 0.04} = \frac{0.25}{0.08} = 3.125
    $$

    The minimum $\kappa$ is 3.125, which is 56% higher than the current $\kappa = 2.0$. This is a significant increase: the half-life would drop from 0.35 years to $\ln 2/3.125 = 0.22$ years ($\approx$ 2.7 months), meaning much faster mean-reversion. In practice, calibrated parameters often violate Feller because the market-implied dynamics demand a lower $\kappa$ than the Feller bound allows---this is why the QE Monte Carlo scheme (which handles $v_t = 0$ gracefully) is essential.

---

**Exercise 2.**
The ATM implied volatility approximation is:

$$
\sigma_{\text{ATM}}(T) \approx \sqrt{\theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}}
$$

For $v_0 = 0.0225$ (initial vol = 15%), $\theta = 0.0625$ (long-run vol = 25%), and $\kappa = 1.5$, compute $\sigma_{\text{ATM}}(T)$ for $T = 0.1, 0.5, 1, 2, 5$ years. Plot or describe the shape of the term structure. At what maturity $T^*$ does the approximation reach 90% of the way from $\sqrt{v_0}$ to $\sqrt{\theta}$?

??? success "Solution to Exercise 2"
    Given $v_0 = 0.0225$, $\theta = 0.0625$, $\kappa = 1.5$:

    $$
    \sigma_{\text{ATM}}(T) = \sqrt{\theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}}
    $$

    Since $v_0 - \theta = 0.0225 - 0.0625 = -0.04$ (initial variance is below long-run level), the term structure will be **upward-sloping** from $\sqrt{v_0} = 15\%$ toward $\sqrt{\theta} = 25\%$.

    Computing for each maturity:

    **$T = 0.1$:** $e^{-1.5 \times 0.1} = e^{-0.15} = 0.8607$

    $$
    \bar{v} = 0.0625 + (-0.04)\frac{1 - 0.8607}{1.5 \times 0.1} = 0.0625 - 0.04 \times \frac{0.1393}{0.15} = 0.0625 - 0.0371 = 0.0254
    $$

    $$
    \sigma_{\text{ATM}}(0.1) = \sqrt{0.0254} = 15.9\%
    $$

    **$T = 0.5$:** $e^{-0.75} = 0.4724$

    $$
    \bar{v} = 0.0625 - 0.04 \times \frac{1 - 0.4724}{0.75} = 0.0625 - 0.04 \times 0.7035 = 0.0625 - 0.0281 = 0.0344
    $$

    $$
    \sigma_{\text{ATM}}(0.5) = \sqrt{0.0344} = 18.5\%
    $$

    **$T = 1.0$:** $e^{-1.5} = 0.2231$

    $$
    \bar{v} = 0.0625 - 0.04 \times \frac{1 - 0.2231}{1.5} = 0.0625 - 0.04 \times 0.5179 = 0.0625 - 0.0207 = 0.0418
    $$

    $$
    \sigma_{\text{ATM}}(1.0) = \sqrt{0.0418} = 20.4\%
    $$

    **$T = 2.0$:** $e^{-3.0} = 0.0498$

    $$
    \bar{v} = 0.0625 - 0.04 \times \frac{1 - 0.0498}{3.0} = 0.0625 - 0.04 \times 0.3167 = 0.0625 - 0.0127 = 0.0498
    $$

    $$
    \sigma_{\text{ATM}}(2.0) = \sqrt{0.0498} = 22.3\%
    $$

    **$T = 5.0$:** $e^{-7.5} = 0.00055$

    $$
    \bar{v} = 0.0625 - 0.04 \times \frac{1 - 0.00055}{7.5} = 0.0625 - 0.04 \times 0.1333 = 0.0625 - 0.0053 = 0.0572
    $$

    $$
    \sigma_{\text{ATM}}(5.0) = \sqrt{0.0572} = 23.9\%
    $$

    The term structure rises monotonically from 15.9% at $T = 0.1$ to 23.9% at $T = 5$, approaching $\sqrt{\theta} = 25\%$ asymptotically.

    **Finding $T^*$ where the approximation reaches 90% of the way from $\sqrt{v_0}$ to $\sqrt{\theta}$:**

    The target level is $\sqrt{v_0} + 0.9(\sqrt{\theta} - \sqrt{v_0}) = 0.15 + 0.9 \times 0.10 = 0.24$, corresponding to $\bar{v} = 0.0576$.

    Setting $\bar{v} = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T} = 0.0576$:

    $$
    0.0576 = 0.0625 - 0.04 \times \frac{1 - e^{-1.5T}}{1.5T}
    $$

    $$
    \frac{1 - e^{-1.5T}}{1.5T} = \frac{0.0625 - 0.0576}{0.04} = 0.1225
    $$

    This must be solved numerically. Trying $T = 5$: LHS $= 0.1333$ (too high). Trying $T = 7$: $e^{-10.5} \approx 0$, LHS $= 1/10.5 = 0.0952$ (too low). Trying $T = 5.5$: LHS $= (1 - e^{-8.25})/8.25 \approx 1/8.25 = 0.1212$ (close). So $T^* \approx 5.4$ years.

    The slow convergence to $\sqrt{\theta}$ reflects the fact that, even though the half-life is only 0.35 years, the **average** variance converges more slowly than the **instantaneous** variance because $\bar{v}$ integrates over the entire path from $t = 0$.

---

**Exercise 3.**
The stationary distribution of the CIR variance process is a Gamma distribution with shape $\alpha = 2\kappa\theta / \xi^2$ and scale $\beta = \xi^2 / (2\kappa)$. For $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, compute $\alpha$ and $\beta$. What is the probability that the stationary variance exceeds $0.16$ (i.e., instantaneous vol exceeds 40%)? Use the fact that for a Gamma$(\alpha, \beta)$ random variable, the CDF can be expressed via the regularized incomplete gamma function.

??? success "Solution to Exercise 3"
    For the CIR stationary distribution (Gamma distribution) with shape $\alpha = 2\kappa\theta/\xi^2$ and scale $\beta = \xi^2/(2\kappa)$:

    $$
    \alpha = \frac{2 \times 2.0 \times 0.04}{0.25} = \frac{0.16}{0.25} = 0.64
    $$

    $$
    \beta = \frac{0.25}{4.0} = 0.0625
    $$

    Note that $\alpha = 0.64$ is also the Feller ratio. Since $\alpha < 1$, the Gamma density diverges as $v \to 0^+$ (the mode is at zero), consistent with the Feller violation.

    **Verification:** $\mathbb{E}[v_\infty] = \alpha\beta = 0.64 \times 0.0625 = 0.04 = \theta$ and $\text{Var}[v_\infty] = \alpha\beta^2 = 0.64 \times 0.00390625 = 0.0025$, so $\text{Std}[v_\infty] = 0.05$, matching the earlier calculation.

    **Probability that $v_\infty > 0.16$:**

    We need $\mathbb{P}(v_\infty > 0.16) = 1 - F_{\text{Gamma}}(0.16; \alpha = 0.64, \beta = 0.0625)$ where $F_{\text{Gamma}}$ is the CDF of the Gamma distribution.

    The standardized variable is $z = v/\beta = 0.16/0.0625 = 2.56$.

    So $\mathbb{P}(v_\infty > 0.16) = 1 - \frac{\gamma(0.64, 2.56)}{\Gamma(0.64)}$ where $\gamma(\alpha, z) = \int_0^z t^{\alpha-1}e^{-t}dt$ is the lower incomplete gamma function.

    Using the regularized incomplete gamma function $P(\alpha, z) = \gamma(\alpha, z)/\Gamma(\alpha)$:

    $$
    \mathbb{P}(v_\infty > 0.16) = 1 - P(0.64, 2.56)
    $$

    For $\alpha = 0.64$ and $z = 2.56$, the regularized incomplete gamma function gives $P(0.64, 2.56) \approx 0.912$ (this can be computed numerically using `scipy.stats.gamma.cdf(0.16, a=0.64, scale=0.0625)` or equivalently `scipy.special.gammainc(0.64, 2.56)`).

    Therefore:

    $$
    \mathbb{P}(v_\infty > 0.16) \approx 1 - 0.912 = 0.088 \approx 8.8\%
    $$

    There is about an 8.8% probability that the stationary variance exceeds 0.16, corresponding to instantaneous volatility above 40%. This is not negligible and reflects the heavy right tail of the Gamma distribution with shape parameter less than 1.

---

**Exercise 4.**
The class validates that $|\rho| < 1$ but accepts $\rho = 0$ and $\rho = \pm 0.99$. Explain why $\rho = \pm 1$ is excluded from the mathematical domain. What happens to the Heston model when $\rho = -1$? Show that with $\rho = -1$, the log-price and variance processes can be written in terms of a single Brownian motion, and discuss the implications for option pricing.

??? success "Solution to Exercise 4"
    The Heston model requires $|\rho| < 1$ because $\rho$ is the correlation coefficient between two Brownian motions $W^{(1)}$ and $W^{(2)}$. The correlation matrix:

    $$
    \Sigma = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
    $$

    must be **positive definite**, which requires $\det(\Sigma) = 1 - \rho^2 > 0$, i.e., $|\rho| < 1$. At $\rho = \pm 1$, the matrix is singular (rank 1), and the two-dimensional Brownian motion collapses to a one-dimensional one.

    **With $\rho = -1$:**

    The Cholesky decomposition gives $W^{(2)} = -W^{(1)}$ (perfectly anticorrelated). The Heston system becomes:

    $$
    dS_t = (r - q)S_t dt + \sqrt{v_t} S_t dW_t
    $$

    $$
    dv_t = \kappa(\theta - v_t)dt - \xi\sqrt{v_t} dW_t
    $$

    where $W_t = W_t^{(1)}$ is a **single** Brownian motion. The system is now driven by one source of randomness, making the market **complete** (in the standard sense of having one risk factor and one traded asset).

    Applying Ito's lemma to $x_t = \ln S_t$:

    $$
    dx_t = \left(r - q - \frac{v_t}{2}\right)dt + \sqrt{v_t}\,dW_t
    $$

    Adding and subtracting the variance equation (scaled appropriately):

    $$
    d(x_t + v_t/\xi) = \left(r - q - \frac{v_t}{2} + \frac{\kappa(\theta - v_t)}{\xi}\right)dt + \left(\sqrt{v_t} - \sqrt{v_t}\right)dW_t
    $$

    Wait---this does not simplify to zero diffusion unless $\xi$ is specifically tuned. Let us be more careful. With $\rho = -1$:

    $$
    dx_t = \left(r - q - \frac{v_t}{2}\right)dt + \sqrt{v_t}\,dW_t
    $$

    $$
    dv_t = \kappa(\theta - v_t)dt - \xi\sqrt{v_t}\,dW_t
    $$

    The linear combination $Z_t = x_t + v_t/\xi$ satisfies:

    $$
    dZ_t = \left(r - q - \frac{v_t}{2} + \frac{\kappa(\theta - v_t)}{\xi}\right)dt + \left(\sqrt{v_t} - \sqrt{v_t}\right)dW_t = \text{(drift only)}
    $$

    The diffusion cancels! So $Z_t = x_t + v_t/\xi$ follows a purely deterministic path (conditional on $v_t$). This means $x_T$ is deterministically determined by $v_T$ and the integrated drift, reducing the pricing problem from two stochastic dimensions to one.

    **Implications for option pricing:** With $\rho = -1$, the model has one effective risk factor (the variance process alone). The option price depends only on the distribution of $v_T$ and the deterministic relationship $x_T = Z_T - v_T/\xi$. This simplification is academically interesting but practically unrealistic: equity markets have $\rho \approx -0.5$ to $-0.8$, never $-1$. The singularity at $\rho = -1$ also causes numerical issues in all Heston pricing engines (the CF, FDM, and MC all have terms involving $\sqrt{1 - \rho^2}$ in denominators or square roots).

---

**Exercise 5.**
A colleague creates two model instances:

```python
model_a = HestonModel(S0=100, r=0.03, q=0.01, v0=0.04, kappa=2.0,
                      theta=0.04, xi=0.5, rho=-0.7)
model_b = HestonModel(S0=100, r=0.03, q=0.01, v0=0.04, kappa=8.0,
                      theta=0.01, xi=0.5, rho=-0.7)
```

Both have $\kappa\theta = 0.08$. Compute and compare: the Feller ratio, mean-reversion half-life, stationary standard deviation, and $\sigma_{\text{ATM}}(T)$ for $T = 0.25$ and $T = 2.0$. Which model would produce a flatter ATM term structure?

??? success "Solution to Exercise 5"
    **Model A:** $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $v_0 = 0.04$

    **Model B:** $\kappa = 8.0$, $\theta = 0.01$, $\xi = 0.5$, $\rho = -0.7$, $v_0 = 0.04$

    Both have $\kappa\theta = 0.08$.

    | Quantity | Model A | Model B |
    |---|---|---|
    | Feller ratio | $2(2)(0.04)/0.25 = 0.64$ | $2(8)(0.01)/0.25 = 0.64$ |
    | Half-life | $\ln 2/2.0 = 0.347$ y | $\ln 2/8.0 = 0.087$ y |
    | Stationary mean | $\theta = 0.04$ | $\theta = 0.01$ |
    | Stationary std | $0.5\sqrt{0.04/4} = 0.05$ | $0.5\sqrt{0.01/16} = 0.0125$ |

    Note that the Feller ratios are identical because $\mathcal{F} = 2\kappa\theta/\xi^2$ and $\kappa\theta$ is the same.

    **ATM volatility at $T = 0.25$:**

    $$
    \sigma_A(0.25) = \sqrt{0.04 + (0.04 - 0.04)\frac{1 - e^{-0.5}}{0.5}} = \sqrt{0.04} = 20.0\%
    $$

    $$
    \sigma_B(0.25) = \sqrt{0.01 + (0.04 - 0.01)\frac{1 - e^{-2.0}}{2.0}} = \sqrt{0.01 + 0.03 \times \frac{0.8647}{2.0}} = \sqrt{0.01 + 0.01297} = \sqrt{0.02297} = 15.2\%
    $$

    **ATM volatility at $T = 2.0$:**

    $$
    \sigma_A(2.0) = \sqrt{0.04 + 0 \times (\cdots)} = \sqrt{0.04} = 20.0\%
    $$

    $$
    \sigma_B(2.0) = \sqrt{0.01 + 0.03 \times \frac{1 - e^{-16}}{16}} \approx \sqrt{0.01 + 0.03 \times \frac{1}{16}} = \sqrt{0.01 + 0.001875} = \sqrt{0.011875} = 10.9\%
    $$

    **Which model has a flatter ATM term structure?**

    Model A has $v_0 = \theta = 0.04$, so the ATM vol is **flat** at 20.0% across all maturities. Model B has $v_0 = 0.04 \gg \theta = 0.01$, so the ATM vol starts at $\sqrt{0.04} = 20\%$ for very short maturities and declines rapidly toward $\sqrt{0.01} = 10\%$ as $T$ increases. Model A produces the flatter term structure.

    This example illustrates the $\kappa$-$\theta$ degeneracy concretely: despite having the same $\kappa\theta$, the two models produce dramatically different term structures. The product $\kappa\theta$ controls the short-run dynamics (it appears in the Feller condition and the variance drift at $v = 0$), but the individual values of $\kappa$ and $\theta$ control the mean-reversion speed and long-run level independently.

---

**Exercise 6.**
The immutability principle states that parameters should not be modified after construction. Discuss why this is important in a production system where the same model object is shared between a pricing engine and a Greeks engine. Give a concrete example of a bug that could arise if a downstream engine modified `model.v0` while another engine was still using the original value.

??? success "Solution to Exercise 6"
    **Why immutability matters:**

    In a production system, the same `HestonModel` object is typically shared across multiple consumers: a pricing engine computes option prices, a Greeks engine computes sensitivities, a risk engine computes scenario P&L, and a reporting engine logs the parameters. All these consumers assume they are working with the **same** model parameters.

    If the model were mutable, the following bug could occur:

    **Concrete example:** Suppose a Greeks engine computes delta by bumping the spot price:

    ```python
    # Greeks engine (running in parallel or sequentially)
    model.S0 = model.S0 + h  # bump up
    price_up = pricing_engine.price(model, K, T)
    model.S0 = model.S0 - 2 * h  # bump down
    price_down = pricing_engine.price(model, K, T)
    model.S0 = model.S0 + h  # restore
    delta = (price_up - price_down) / (2 * h)
    ```

    If, between the "bump up" and "bump down" steps, another engine reads `model.S0`, it would see the bumped value instead of the original. For example:

    1. Greeks engine bumps $S_0$ to 100.01
    2. Risk engine reads $S_0 = 100.01$ (wrong! should be 100.00)
    3. Risk engine computes VaR using $S_0 = 100.01$
    4. Greeks engine bumps $S_0$ down to 99.99
    5. A pricing report logs $S_0 = 99.99$ (also wrong!)

    The result: the risk report uses incorrect parameters, and the pricing report shows a different spot than the actual market. These bugs are subtle and hard to detect because the parameter is "almost right" (off by 0.01), and the error may be within normal tolerance---until it is not.

    Even in single-threaded code, mutation is dangerous: if any function modifies `model.v0` as part of its computation (e.g., a Monte Carlo engine that updates variance along a path), subsequent calls to the pricing engine will use the corrupted value.

    **The immutable design** prevents all these bugs: to compute bumped prices, the Greeks engine creates **new** model instances `HestonModel(S0=S0+h, ...)` and `HestonModel(S0=S0-h, ...)`, leaving the original untouched. This is slightly more expensive (object creation) but eliminates an entire class of concurrency and state-management bugs.

---

**Exercise 7.**
Extend the `HestonModel` class conceptually to support time-dependent parameters $\kappa(t)$ and $\theta(t)$. What changes to the interface are needed? The characteristic function is no longer available in closed form for general time-dependent parameters. Describe two pricing approaches that would still work: (a) a piecewise-constant approximation that chains multiple constant-parameter Heston CFs, and (b) Monte Carlo with the QE scheme using local $\kappa(t_n)$ and $\theta(t_n)$ at each time step.

??? success "Solution to Exercise 7"
    **Interface changes for time-dependent parameters:**

    Replace scalar `kappa` and `theta` with callable functions `kappa(t)` and `theta(t)`:

    ```python
    class HestonModelTD:
        def __init__(self, S0, r, q, v0, kappa_func, theta_func,
                     xi, rho):
            self.kappa = kappa_func  # callable: t -> float
            self.theta = theta_func  # callable: t -> float
            # ... other parameters as before
    ```

    The validation method must now check positivity of $\kappa(t)$ and $\theta(t)$ at sample points, and the Feller condition becomes time-dependent: $2\kappa(t)\theta(t) \geq \xi^2$ for all $t$. Derived properties (half-life, stationary moments) become time-dependent functions rather than scalar properties.

    **(a) Piecewise-constant CF chaining:**

    Divide $[0, T]$ into subintervals $[t_0, t_1], [t_1, t_2], \ldots, [t_{n-1}, t_n]$ on which $\kappa$ and $\theta$ are constant. On each subinterval $[t_{k-1}, t_k]$ with constants $\kappa_k$ and $\theta_k$, the Heston CF has a closed-form solution.

    The characteristic function over the full interval is obtained by **chaining**: the CF from $t_0$ to $t_n$ satisfies the tower property:

    $$
    \varphi(u, 0, T) = \prod_{k=1}^{n} \exp\!\left(C_k(u, \Delta t_k) + D_k(u, \Delta t_k) \cdot v_{t_{k-1}}\right)
    $$

    where $\Delta t_k = t_k - t_{k-1}$ and $C_k, D_k$ are the Riccati solutions for constants $\kappa_k, \theta_k$. More precisely, the variance at the start of each subinterval is **random** (it depends on the path), so the chaining works through the affine structure: $D$ at the end of one interval becomes the effective "initial condition" for the next.

    The recursive formula: starting from $D_n = 0$ and $C_n = 0$ at $T$, march backward:

    $$
    D_{k-1} = D_k^{(\text{const})}(u, \Delta t_k) + D_k \cdot e^{-\kappa_k \Delta t_k} \cdot (\text{correction})
    $$

    The exact chaining formulas are derived by applying the affine property at each boundary. This approach preserves the efficiency of Fourier pricing while allowing piecewise-constant time dependence.

    **(b) Monte Carlo with time-dependent QE:**

    The QE scheme adapts naturally to time-dependent parameters. At each time step $n$, use the local values $\kappa_n = \kappa(t_n)$ and $\theta_n = \theta(t_n)$:

    $$
    m_n = \theta_n + (v_n - \theta_n)e^{-\kappa_n \Delta t}
    $$

    $$
    s_n^2 = \frac{v_n \xi^2 e^{-\kappa_n\Delta t}}{\kappa_n}(1 - e^{-\kappa_n\Delta t}) + \frac{\theta_n\xi^2}{2\kappa_n}(1 - e^{-\kappa_n\Delta t})^2
    $$

    The log-price coefficients $K_0, \ldots, K_4$ also use local $\kappa_n$ and $\theta_n$. The key advantage is that these are simply recalculated at each time step using the current parameter values---no structural change to the algorithm is needed.

    The precomputation of $e^{-\kappa\Delta t}$, $K_0$, etc., can no longer be done once outside the time loop; instead, they must be recomputed at each step (or precomputed as arrays indexed by $n$). This adds modest overhead but preserves the QE scheme's near-exact accuracy.

    **Trade-offs:** Method (a) is fast (Fourier pricing) but limited to European options and piecewise-constant parameters. Method (b) handles any payoff and any parameter schedule, but is slower due to Monte Carlo sampling. For calibration (where European pricing speed matters), method (a) is preferred. For exotic pricing with calibrated time-dependent parameters, method (b) is the natural choice.
