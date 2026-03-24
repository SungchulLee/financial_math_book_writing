# Python Implementation Guide

This section provides a practical guide to implementing the SABR model in Python, connecting the mathematical theory developed in earlier sections to working code. The implementation covers the Hagan implied volatility formula (with numerical stability safeguards), the calibration procedure, Monte Carlo simulation, and a complete usage workflow. The companion file `python_implementation.py` contains the full runnable code; this section explains the design decisions, highlights the numerical pitfalls, and demonstrates typical usage patterns.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement the Hagan implied volatility formula with proper edge case handling
    2. Structure a SABR calibration module with ATM-first parameter determination
    3. Implement Monte Carlo simulation with exact volatility sampling
    4. Validate implementations against known analytical results
    5. Use the module for a complete pricing and calibration workflow

---

## Module Design

### Architecture

The implementation is organized around a single class `SABRModel` that encapsulates the model parameters and provides methods for pricing, calibration, and simulation:

```python
class SABRModel:
    """SABR model for option pricing and calibration."""

    def __init__(self, F: float, beta: float = 0.5):
        self.F = F        # Forward price
        self.beta = beta   # CEV exponent (fixed by convention)

    # Core methods:
    # _hagan_implied_vol(K, T, alpha, rho, nu) -> float
    # call_price_hagan(K, T, r, alpha, rho, nu) -> float
    # simulate_paths(T, alpha, rho, nu, ...) -> arrays
    # price_monte_carlo(K, T, r, alpha, rho, nu, ...) -> (float, float)
```

A separate function `calibrate_sabr(F, T, market_data, ...)` handles calibration, since calibration is a workflow that uses the model rather than being an intrinsic property of it.

### Design Decisions

**Forward-based**: The model takes the forward $F$ as input (not the spot). This is natural for the SABR model, which is formulated in forward space.

**Beta fixed at construction**: The CEV exponent $\beta$ is set once and not changed, reflecting the convention that $\beta$ is fixed by the market.

**Parameters passed to methods**: The SABR parameters $(\alpha, \rho, \nu)$ are passed to each method rather than stored, because the same forward may be priced with different parameter sets during calibration.

---

## Hagan Formula Implementation

### The Core Function

The Hagan implied volatility formula is the most critical function to implement correctly. The key challenge is handling the edge cases that arise when $K \approx F$ (ATM), $\nu \approx 0$ (CEV limit), or $|\rho| \approx 1$.

```python
def _hagan_implied_vol(self, K, T, alpha, rho, nu):
    F, beta = self.F, self.beta

    # ATM case: use simplified formula
    if abs(F - K) < 1e-8 * F:
        fk = F * F  # F*K = F^2 at ATM
        fk_beta = fk ** ((1 - beta) / 2)
        correction = (
            (1 - beta) ** 2 * alpha ** 2 / (24 * fk ** (1 - beta))
            + rho * beta * nu * alpha / (4 * fk_beta)
            + (2 - 3 * rho ** 2) * nu ** 2 / 24
        )
        return alpha / F ** (1 - beta) * (1 + correction * T)

    # General case
    fk = F * K
    fk_beta = fk ** ((1 - beta) / 2)
    log_fk = np.log(F / K)

    # z and x(z) computation
    z = (nu / alpha) * fk_beta * log_fk
    # ...
```

### Numerical Stability: The z/x(z) Ratio

The function $x(z) = \ln((\sqrt{1 - 2\rho z + z^2} + z - \rho)/(1-\rho))$ and the ratio $z/x(z)$ require careful handling:

**When $|z| < 10^{-7}$**: Use the Taylor expansion:

```python
if abs(z) < 1e-7:
    zxz = 1.0  # z/x(z) -> 1 as z -> 0
else:
    sqrt_term = np.sqrt(1 - 2 * rho * z + z ** 2)
    x = np.log((sqrt_term + z - rho) / (1 - rho))
    zxz = z / x if abs(x) > 1e-10 else 1.0
```

**When $|\rho|$ is near 1**: The denominator $1 - \rho$ in the logarithm approaches zero. Check for this:

```python
if abs(1 - rho) < 1e-10:
    # rho ≈ 1: use limiting formula
    zxz = z / np.log(1 / (1 - z)) if z < 0.999 else 1.0
```

**When the argument of the logarithm is non-positive**: This can happen for extreme parameter combinations. Guard against it:

```python
arg = (sqrt_term + z - rho) / (1 - rho)
if arg <= 0:
    return alpha / F ** (1 - beta)  # Fall back to backbone
```

---

## Calibration Implementation

### ATM-First Procedure

The calibration follows the two-step procedure described in the calibration section:

```python
def calibrate_sabr(F, T, market_vols, beta=0.5):
    """
    Calibrate SABR to market implied volatilities.

    Args:
        F: Forward price
        T: Time to expiry
        market_vols: dict {strike: implied_vol}
        beta: CEV exponent (fixed)

    Returns:
        dict with calibrated (alpha, rho, nu)
    """
    model = SABRModel(F, beta)
    atm_vol = market_vols.get(F, None)

    def alpha_from_atm(rho, nu):
        """Solve for alpha given ATM vol, rho, nu."""
        # Newton's method on the ATM Hagan formula
        alpha = atm_vol * F ** (1 - beta)  # Initial guess
        for _ in range(10):
            vol = model._hagan_implied_vol(F, T, alpha, rho, nu)
            dvol = ...  # derivative w.r.t. alpha
            alpha -= (vol - atm_vol) / dvol
        return alpha

    def objective(params):
        rho, nu = params
        alpha = alpha_from_atm(rho, nu)
        error = 0
        for K, vol_mkt in market_vols.items():
            vol_model = model._hagan_implied_vol(K, T, alpha, rho, nu)
            error += (vol_model - vol_mkt) ** 2
        return error

    # Optimize over (rho, nu)
    from scipy.optimize import minimize
    result = minimize(objective, [-0.3, 0.4],
                      bounds=[(-0.999, 0.999), (0.01, 2.0)])
    rho_opt, nu_opt = result.x
    alpha_opt = alpha_from_atm(rho_opt, nu_opt)

    return {"alpha": alpha_opt, "rho": rho_opt, "nu": nu_opt}
```

### Bounds and Constraints

The optimization enforces $\rho \in (-0.999, 0.999)$ and $\nu \in (0.01, 2.0)$ using bounds. These prevent the optimizer from exploring unphysical parameter regions where the Hagan formula is unreliable.

---

## Monte Carlo Implementation

### Exact Volatility, Euler Forward

The recommended simulation scheme uses exact sampling for the lognormal volatility and Euler discretization for the forward:

```python
def simulate_paths(self, T, alpha, rho, nu,
                   num_paths=10000, num_steps=100, seed=None):
    if seed is not None:
        rng = np.random.default_rng(seed)
    else:
        rng = np.random.default_rng()

    dt = T / num_steps
    F = np.full(num_paths, self.F)
    sigma = np.full(num_paths, alpha)

    for _ in range(num_steps):
        # Independent normals
        Z1 = rng.standard_normal(num_paths)
        Z2 = rng.standard_normal(num_paths)

        # Correlated increments
        W1 = Z1
        W2 = rho * Z1 + np.sqrt(1 - rho ** 2) * Z2

        # Exact volatility step (lognormal)
        sigma *= np.exp(-0.5 * nu ** 2 * dt + nu * np.sqrt(dt) * W2)

        # Euler forward step with absorbing boundary
        dF = sigma * np.maximum(F, 0) ** self.beta * np.sqrt(dt) * W1
        F = np.maximum(F + dF, 0)

    return F, sigma
```

### Key Implementation Details

**Vectorization**: The entire simulation is vectorized over paths using NumPy arrays. No Python loops over paths.

**Absorbing boundary**: `np.maximum(F, 0)` in the diffusion coefficient and `np.maximum(F + dF, 0)` after the step ensure the forward stays non-negative.

**Exact volatility**: `sigma *= np.exp(...)` is the exact lognormal evolution, avoiding the negative-volatility issue.

**Random number generation**: Uses `np.random.default_rng()` (the modern NumPy generator) instead of the deprecated `np.random.seed()`.

---

## Validation

### Against Known Results

The implementation should be validated against:

1. **CEV limit** ($\nu = 0$): The Hagan formula should reduce to $\sigma_B = \alpha / F^{1-\beta}$ at the money.

2. **Black--Scholes limit** ($\beta = 1$, $\nu = 0$): The Hagan formula should return $\sigma_B = \alpha$ for all strikes.

3. **Symmetry** ($\rho = 0$, $\beta = 1$): The smile should be symmetric around ATM.

4. **Monte Carlo vs Hagan**: For European options, the MC price should converge to the Hagan price as the number of paths and time steps increase.

```python
def validate():
    model = SABRModel(F=0.03, beta=0.5)
    alpha, rho, nu = 0.035, -0.3, 0.4

    # Test 1: ATM Hagan vs MC
    vol_hagan = model._hagan_implied_vol(0.03, 1.0, alpha, rho, nu)
    price_hagan = model.call_price_hagan(0.03, 1.0, 0.0, alpha, rho, nu)

    F_terminal, _ = model.simulate_paths(1.0, alpha, rho, nu,
                                          num_paths=500000, num_steps=200)
    payoffs = np.maximum(F_terminal - 0.03, 0)
    price_mc = np.mean(payoffs)

    print(f"Hagan price: {price_hagan:.6f}")
    print(f"MC price:    {price_mc:.6f} +/- {np.std(payoffs)/np.sqrt(len(payoffs)):.6f}")
```

### Typical Validation Results

| Test | Expected | Actual | Pass |
|------|----------|--------|------|
| ATM vol ($\nu=0$) = $\alpha/F^{0.5}$ | 20.21% | 20.21% | Yes |
| MC vs Hagan (ATM, 500K paths) | Agreement within 1 bps | 0.3 bps difference | Yes |
| Symmetric smile ($\rho=0$, $\beta=1$) | $\sigma(K) = \sigma(F^2/K)$ | Verified | Yes |

---

## Usage Workflow

### Complete Example

A typical workflow using the SABR module:

```python
# 1. Set up model
model = SABRModel(F=0.035, beta=0.5)

# 2. Market data
market_vols = {
    0.015: 0.248,  # -200 bps
    0.025: 0.221,  # -100 bps
    0.035: 0.202,  # ATM
    0.045: 0.192,  # +100 bps
    0.055: 0.187,  # +200 bps
}

# 3. Calibrate
params = calibrate_sabr(F=0.035, T=5.0, market_vols=market_vols, beta=0.5)
alpha, rho, nu = params["alpha"], params["rho"], params["nu"]
print(f"Calibrated: alpha={alpha:.4f}, rho={rho:.3f}, nu={nu:.3f}")

# 4. Compute smile at fine strikes
strikes = np.linspace(0.01, 0.06, 50)
vols = [model._hagan_implied_vol(K, 5.0, alpha, rho, nu) for K in strikes]

# 5. Price an exotic via MC
F_paths, sigma_paths = model.simulate_paths(5.0, alpha, rho, nu,
                                             num_paths=100000, num_steps=500)
# ... compute path-dependent payoff
```

---

## Summary

The Python implementation of the SABR model centers on three components: the Hagan implied volatility formula (with edge case handling for ATM, small $z$, and extreme $\rho$), the calibration procedure (ATM-first with Levenberg--Marquardt or Nelder--Mead for the smile), and Monte Carlo simulation (exact lognormal volatility with Euler forward stepping). The implementation is validated against CEV limits, Black--Scholes limits, symmetry checks, and Monte Carlo convergence. The companion file `python_implementation.py` provides the complete runnable code.

---

## Further Reading

- Le Floc'h, F. (2014). *Fast and accurate analytic basis point SABR*. SSRN preprint.
- Hagan, P. et al. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly, Chapters 2--4 (NumPy and SciPy).

---

## Exercises

**Exercise 1.** The Hagan formula involves the ratio $z/x(z)$ where $x(z) = \ln((\sqrt{1 - 2\rho z + z^2} + z - \rho)/(1 - \rho))$. Compute $z/x(z)$ numerically for $\rho = -0.3$ and $z = 0.5$. Then compute it for $z = 10^{-8}$ and verify that the Taylor expansion $z/x(z) \approx 1$ is appropriate for small $|z|$.

---

**Exercise 2.** The ATM-first calibration determines $\alpha$ by solving $\sigma_B^{\text{Hagan}}(\alpha, \rho, \nu) = \sigma_B^{\text{ATM}}$ using Newton's method. Write the Newton iteration formula explicitly:

$$
\alpha_{k+1} = \alpha_k - \frac{\sigma_B^{\text{Hagan}}(\alpha_k) - \sigma_B^{\text{ATM}}}{\partial\sigma_B^{\text{Hagan}}/\partial\alpha|_{\alpha_k}}
$$

For $F = 0.03$, $\beta = 0.5$, $\sigma_B^{\text{ATM}} = 0.22$, $\rho = -0.25$, and $\nu = 0.35$, compute the initial guess $\alpha_0 = \sigma_B^{\text{ATM}} \cdot F^{1-\beta}$.

---

**Exercise 3.** In the Monte Carlo implementation, the volatility is simulated exactly: $\sigma_{n+1} = \sigma_n \exp(-\frac{1}{2}\nu^2\Delta t + \nu\sqrt{\Delta t}\,W_2)$. Show that this is the exact solution to $d\sigma_t = \nu\sigma_t\,dW_t^{(2)}$ over the interval $[t_n, t_{n+1}]$. Why does this eliminate the need for a positivity floor on $\sigma$?

---

**Exercise 4.** The implementation uses `np.maximum(F + dF, 0)` to enforce the absorbing boundary. Discuss the bias this introduces: does it overestimate or underestimate the absorption probability? How would you implement the more accurate chi-squared-based absorption test described in the Monte Carlo section?

---

**Exercise 5.** Design a validation test for the SABR implementation that checks the Black-Scholes limit ($\beta = 1$, $\nu = 0$). In this limit, the SABR model reduces to geometric Brownian motion with constant volatility $\alpha$. Write a test that compares the Hagan formula output, the Monte Carlo price, and the exact Black-Scholes price for an ATM call with $F = 0.05$, $T = 1$, and $\alpha = 0.20$. What tolerances should you use for each comparison?

---

**Exercise 6.** The calibration function uses bounds $\rho \in (-0.999, 0.999)$ and $\nu \in (0.01, 2.0)$. Explain why each bound is necessary. What numerical problems arise if $\rho$ is allowed to reach exactly $\pm 1$? What happens to the Hagan formula if $\nu = 0$, and why is a small positive lower bound used instead?
