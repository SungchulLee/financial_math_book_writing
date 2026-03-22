# Heston Model Class

A well-designed model class serves as the single source of truth for parameters, validation, and derived quantities. Every pricing engine---characteristic function, COS, FFT, Monte Carlo, and FDM---needs the same five Heston parameters plus market data. Centralizing these in a `HestonModel` class eliminates duplication, enforces consistency, and makes the codebase easier to extend. This guide walks through the class design, explains the mathematical constraints behind each validation check, and shows how the class integrates with downstream pricing engines.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Design a `HestonModel` class that stores, validates, and exposes the five Heston parameters plus market data
    2. Implement parameter validation checks with clear mathematical justifications
    3. Compute derived quantities (Feller ratio, mean-reversion half-life, stationary moments) from stored parameters
    4. Connect the model class to pricing engines through a consistent interface

!!! tip "Prerequisites"
    This section builds on the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md) and the [Feller condition](../model_definition/feller_condition_and_boundary.md). The companion implementation is in [`heston_model_class.py`](heston_model_class.py).

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
