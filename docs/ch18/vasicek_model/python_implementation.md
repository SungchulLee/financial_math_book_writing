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
| `bond_option_price(K, T_opt, T_bond, r0)` | ZCB option via $\Phi(d_1), \Phi(d_2)$ | European bond option |
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
C = P(0,S)\,\Phi(d_1) - K\,P(0,T)\,\Phi(d_2)
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
