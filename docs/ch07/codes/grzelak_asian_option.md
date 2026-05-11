# Asian Option (Grzelak)

## Background

Price Asian options using Monte Carlo simulation with cost reduction.

This script demonstrates Monte Carlo pricing of Asian (average) options,
which depend on the average of the stock price over the option's life rather
than just the final price. A cost reduction technique (variance reduction) is
demonstrated by comparing the variance of the final stock price (European option)
with the variance of the arithmetic average (Asian option).

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
Price Asian options using Monte Carlo simulation with cost reduction.

This script demonstrates Monte Carlo pricing of Asian (average) options,
which depend on the average of the stock price over the option's life rather
than just the final price. A cost reduction technique (variance reduction) is
demonstrated by comparing the variance of the final stock price (European option)
with the variance of the arithmetic average (Asian option).

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np


# =============================================================================
# 1. Path Generation
# =============================================================================

def generate_paths_gbm_euler(num_paths, num_steps, T, r, sigma, s0):
    """
    Generate sample paths for geometric Brownian motion using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.
    s0 : float
        Initial stock price.

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid (ndarray of shape (num_steps+1,))
        - 'S': stock price paths (ndarray of shape (num_paths, num_steps+1))
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))

    # Euler Approximation
    s1 = np.zeros((num_paths, num_steps + 1))
    s1[:, 0] = s0

    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    for i in range(0, num_steps):
        # Standardize samples to ensure mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]

        s1[:, i + 1] = (s1[:, i] + r * s1[:, i] * dt +
                        sigma * s1[:, i] * (w[:, i + 1] - w[:, i]))
        time[i + 1] = time[i] + dt

    paths = {"time": time, "S": s1}
    return paths


# =============================================================================
# 2. Valuation
# =============================================================================

def payoff_valuation(S, T, r, payoff):
    """
    Compute discounted expected payoff using Monte Carlo samples.

    Parameters
    ----------
    S : ndarray
        Stock prices at maturity (1D array of final prices).
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    payoff : callable
        Payoff function taking stock price(s) as argument.

    Returns
    -------
    value : float
        Discounted expected payoff.
    """
    return np.exp(-r * T) * np.mean(payoff(S))


# =============================================================================
# 3. Main
# =============================================================================

def main():
    """Run Asian option pricing demonstration."""
    # Parameters
    num_paths = 5000       # Number of Monte Carlo paths
    num_steps = 250        # Number of time steps

    s0 = 100.0             # Initial stock price
    r = 0.05               # Risk-free rate
    T = 5.0                # Time to maturity
    sigma = 0.2            # Volatility

    # Generate paths
    paths = generate_paths_gbm_euler(num_paths, num_steps, T, r, sigma, s0)
    s_paths = paths["S"]
    s_T = s_paths[:, -1]

    # Payoff setting
    K = 100.0              # Strike price

    # Payoff specification (call option payoff)
    payoff = lambda S: np.maximum(S - K, 0.0)

    # Valuation of European call option
    val_t0 = payoff_valuation(s_T, T, r, payoff)
    print("Value of the contract at t0 ={0}".format(val_t0))

    # Valuation of Asian option
    A_T = np.mean(s_paths, 1)
    val_asian_t0 = payoff_valuation(A_T, T, r, payoff)
    print("Value of the Asian option at t0 ={0}".format(val_asian_t0))

    # Variance comparison
    print('variance of S(T) = {0}'.format(np.var(s_T)))
    print('variance of A(T) = {0}'.format(np.var(A_T)))


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Explain the cost reduction technique for Asian options: why does averaging reduce MC variance?

??? success "Solution to Exercise 1"
    The arithmetic average $\bar{S} = \frac{1}{n}\sum S_{t_i}$ has lower variance than $S_T$ because averaging diversifies across time. The covariance between $S_{t_i}$ and $S_{t_j}$ is positive but less than $\text{Var}(S_T)$, so the overall variance decreases as $O(1/n)$. This directly reduces the MC standard error.

---

**Exercise 2.**
Compare the variance of $S_T$ versus $\bar{S}$ for GBM with $\sigma = 0.20$ and $T = 1$.

??? success "Solution to Exercise 2"
    $\text{Var}(S_T)/S_0^2 = e^{2rT}(e^{\sigma^2 T} - 1) \approx e^{0.1}(e^{0.04} - 1) \approx 0.0449$. For the continuous average, $\text{Var}(\bar{S})/S_0^2 \approx 0.0150$ (roughly one-third). The Asian option payoff has about 60--70% less variance.

---

**Exercise 3.**
How would you modify the simulation to price an Asian put?

??? success "Solution to Exercise 3"
    Change the payoff from $\max(\bar{S} - K, 0)$ to $\max(K - \bar{S}, 0)$. The path simulation and averaging are identical. The cost reduction effect still applies.

---

**Exercise 4.**
The script is based on Grzelak (2019). What Euler scheme is used, and why is it exact for GBM?

??? success "Solution to Exercise 4"
    The scheme $S_{t+\Delta t} = S_t\exp((r - \frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}Z)$ is the exact GBM solution at each step. It preserves the log-normal distribution exactly, with no time-stepping bias. This is possible because GBM has a known closed-form solution.
