# Merton Process Paths (Grzelak)

## Background

Generate sample paths for the Merton jump diffusion process.

This script demonstrates Monte Carlo simulation of the Merton jump diffusion
model, where stock prices follow a geometric Brownian motion with superimposed
random jumps. It generates and visualizes sample paths for both the log-price
process and the stock price process.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
Generate sample paths for the Merton jump diffusion process.

This script demonstrates Monte Carlo simulation of the Merton jump diffusion
model, where stock prices follow a geometric Brownian motion with superimposed
random jumps. It generates and visualizes sample paths for both the log-price
process and the stock price process.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Path Generation
# =============================================================================

def generate_paths_merton(num_paths, num_steps, s0, T, xi_p, mu_j, sigma_j,
                          r, sigma):
    """
    Generate sample paths for the Merton jump diffusion process.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    s0 : float
        Initial stock price.
    T : float
        Time to maturity.
    xi_p : float
        Jump intensity (Poisson parameter).
    mu_j : float
        Mean of jump size.
    sigma_j : float
        Standard deviation of jump size.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the continuous part.

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid (ndarray of shape (num_steps+1,))
        - 'X': log-price process (ndarray of shape (num_paths, num_steps+1))
        - 'S': stock price process (ndarray of shape (num_paths, num_steps+1))
    """
    # Create empty matrices for log-price and stock price
    x = np.zeros((num_paths, num_steps + 1))
    s = np.zeros((num_paths, num_steps + 1))
    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    x[:, 0] = np.log(s0)
    s[:, 0] = s0

    # Expectation E(e^J) for J~N(mu_j, sigma_j^2)
    exp_ej = np.exp(mu_j + 0.5 * sigma_j * sigma_j)

    # Generate random variables
    z_pois = np.random.poisson(xi_p * dt, (num_paths, num_steps))
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    j = np.random.normal(mu_j, sigma_j, (num_paths, num_steps))

    for i in range(0, num_steps):
        # Standardize samples to ensure mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        # Update log-price with continuous and jump components
        x[:, i + 1] = (x[:, i] + (r - xi_p * (exp_ej - 1) - 0.5 * sigma * sigma)
                       * dt + sigma * np.sqrt(dt) * z[:, i]
                       + j[:, i] * z_pois[:, i])
        time[i + 1] = time[i] + dt

    s = np.exp(x)
    paths = {"time": time, "X": x, "S": s}
    return paths


# =============================================================================
# 2. Visualization
# =============================================================================

def plot_log_prices(time, x):
    """
    Plot log-price sample paths.

    Parameters
    ----------
    time : ndarray
        Time grid.
    x : ndarray
        Log-price paths of shape (num_paths, num_steps+1).
    """
    plt.figure(1)
    plt.plot(time, np.transpose(x))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("X(t)")
    plt.tight_layout()


def plot_stock_prices(time, s):
    """
    Plot stock price sample paths.

    Parameters
    ----------
    time : ndarray
        Time grid.
    s : ndarray
        Stock price paths of shape (num_paths, num_steps+1).
    """
    plt.figure(2)
    plt.plot(time, np.transpose(s))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("S(t)")
    plt.tight_layout()


# =============================================================================
# 3. Main
# =============================================================================

def main():
    """Run Merton process path generation demonstration."""
    # Parameters
    num_paths = 25         # Number of Monte Carlo paths
    num_steps = 500        # Number of time steps
    s0 = 100.0             # Initial stock price
    T = 5.0                # Time to maturity
    xi_p = 1.0             # Jump intensity
    mu_j = 0.0             # Mean of jump size
    sigma_j = 0.7          # Standard deviation of jump size
    sigma = 0.2            # Volatility
    r = 0.05               # Risk-free rate

    # Generate paths
    paths = generate_paths_merton(num_paths, num_steps, s0, T, xi_p, mu_j,
                                  sigma_j, r, sigma)
    time_grid = paths["time"]
    x = paths["X"]
    s = paths["S"]

    # Visualize results
    plot_log_prices(time_grid, x)
    plot_stock_prices(time_grid, s)
    plt.show()


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Write the log-price increment for one Merton time step. Identify drift, diffusion, and jump components.

??? success "Solution to Exercise 1"
    $\ln S_{t+\Delta t} = \ln S_t + (r - \frac{1}{2}\sigma^2 - \lambda\bar{k})\Delta t + \sigma\sqrt{\Delta t}Z + \sum_{i=1}^n J_i$ where $n \sim \text{Poisson}(\lambda\Delta t)$ and $J_i \sim \mathcal{N}(\mu_J, \sigma_J^2)$.

---

**Exercise 2.**
Why is exact simulation possible for the Merton model?

??? success "Solution to Exercise 2"
    The diffusion and jump components are independent, the diffusion is exactly GBM (log-normal), and jumps form a compound Poisson process with known distribution. Each can be sampled exactly without discretization.

---

**Exercise 3.**
How do Merton paths visually differ from pure GBM paths?

??? success "Solution to Exercise 3"
    Merton paths show sudden vertical gaps (jumps) superimposed on smooth GBM fluctuations. The distribution has fatter tails and possibly skewness (if $\mu_J \ne 0$). GBM paths are continuous with no gaps.

---

**Exercise 4.**
What is the compensator $\lambda\bar{k}$ and why is it needed?

??? success "Solution to Exercise 4"
    $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$ is the expected relative jump size. Including $-\lambda\bar{k}$ in the drift ensures $e^{-rt}S_t$ is a martingale under the risk-neutral measure, preventing arbitrage from the expected jump return.
