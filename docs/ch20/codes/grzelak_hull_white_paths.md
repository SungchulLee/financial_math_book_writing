# Hull-White Paths

## Background

Monte Carlo paths for the Hull-White model.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak

---

## What This Code Demonstrates

- Hull-White Path Generator =============
- Plotting Functions =============

---

## Code

```python
"""
Monte Carlo paths for the Hull-White model.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt


# ============= Hull-White Path Generator =============

def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """
    Generate interest rate paths using Hull-White model with Euler discretization.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths
    num_steps : int
        Number of time steps
    t : float
        Total time horizon
    p0t : callable
        Zero-coupon bond price function P(0, T)
    lambd : float
        Mean reversion speed
    eta : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with 'time' and 'R' keys containing time grid and rates
    """
    # Time-step for numerical differentiation
    dt_diff = 0.0001

    def f0t(tau):
        """Compute forward rate at time tau."""
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)

    # Initial interest rate
    r0 = f0t(0.00001)

    def theta(tau):
        """Compute mean-reverting level theta(t)."""
        return (1.0 / lambd * (f0t(tau + dt_diff) - f0t(tau - dt_diff)) / (2.0 * dt_diff) +
                f0t(tau) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)
    for i in range(0, num_steps):
        # Ensure samples have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])

        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + lambd * (theta(time[i]) - r[:, i]) * dt + eta * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt

    return {"time": time, "R": r}


# ============= Plotting Functions =============

def plot_lambda_effect(num_paths, num_steps, t, p0t, eta):
    """
    Plot the effect of mean reversion speed lambda on interest rate paths.

    Parameters
    ----------
    num_paths : int
        Number of paths
    num_steps : int
        Number of steps
    t : float
        Time horizon
    p0t : callable
        Zero-coupon bond function
    eta : float
        Volatility
    """
    plt.figure(1)
    legend = []
    lambda_vec = [-0.01, 0.2, 5.0]

    for lambda_temp in lambda_vec:
        np.random.seed(2)
        paths = generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambda_temp, eta)
        legend.append('lambda={0}'.format(lambda_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))

    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def plot_eta_effect(num_paths, num_steps, t, p0t, lambd):
    """
    Plot the effect of volatility eta on interest rate paths.

    Parameters
    ----------
    num_paths : int
        Number of paths
    num_steps : int
        Number of steps
    t : float
        Time horizon
    p0t : callable
        Zero-coupon bond function
    lambd : float
        Mean reversion speed
    """
    plt.figure(2)
    legend = []
    eta_vec = [0.1, 0.2, 0.3]

    for eta_temp in eta_vec:
        np.random.seed(2)
        paths = generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta_temp)
        legend.append('eta={0}'.format(eta_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))

    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def main():
    """Main computation for Hull-White path generation and analysis."""
    num_paths = 1
    num_steps = 5000
    t = 50.0
    lambd = 0.5
    eta = 0.01

    # ZCB curve (from market)
    p0t = lambda tau: np.exp(-0.05 * tau)

    # Effect of mean reversion lambda
    plot_lambda_effect(num_paths, num_steps, t, p0t, eta)

    # Effect of volatility
    plot_eta_effect(num_paths, num_steps, t, p0t, lambd)


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The Hull-White Euler discretization is $r_{i+1} = r_i + \lambda(\theta(t_i) - r_i)\,\Delta t + \eta\,\Delta W_i$. For $\lambda = 0.03$, $\eta = 0.01$, and a flat curve at $5\%$, compute $\theta(0)$ and the first step with $r_0 = 0.05$, $\Delta t = 0.01$, $\Delta W = 0.005$.

??? success "Solution to Exercise 1"
    For a flat curve at $5\%$, $\theta(0) \approx f(0,0) = 0.05$ (ignoring the small convexity correction). The first Euler step is:

    $$
    r_1 = 0.05 + 0.03(0.05 - 0.05) \times 0.01 + 0.01 \times 0.005 = 0.05 + 0 + 0.00005 = 0.05005.
    $$

    The rate increases slightly due to the positive Brownian increment.

---

**Exercise 2.**
The code normalizes Brownian increments to have exact mean zero and unit variance. Explain the purpose and effect on simulation accuracy.

??? success "Solution to Exercise 2"
    Normalization adjusts each time step's increments: $z_i^{\text{norm}} = (z_i - \bar{z}_i)/s_i$. This is a variance reduction technique that:

    1. Removes sampling noise from the first two moments, ensuring $\mathbb{E}[\Delta W] = 0$ and $\text{Var}[\Delta W] = \Delta t$ exactly.
    2. Improves convergence of Monte Carlo estimates, especially for a moderate number of paths.
    3. Has no effect on the distributional shape (the normalized samples are still approximately Gaussian).

    The improvement is most noticeable for expectations that depend on the mean (like bond prices) rather than tail quantities.

---

**Exercise 3.**
If 1000 Hull-White paths are simulated over 10 years with 500 time steps, estimate the memory required to store all rate paths (using 64-bit floating point).

??? success "Solution to Exercise 3"
    The rate array has shape $(1000, 501)$ (including the initial value). Each entry uses 8 bytes (64-bit float):

    $$
    \text{Memory} = 1000 \times 501 \times 8 = 4{,}008{,}000 \text{ bytes} \approx 3.82 \text{ MB}.
    $$

    This is modest. However, if auxiliary arrays (Brownian increments, money market accounts) are also stored, the total is approximately $3 \times 3.82 \approx 11.5$ MB.

---

**Exercise 4.**
Describe how the mean reversion speed $\lambda$ affects the dispersion of simulated Hull-White paths over a long horizon.

??? success "Solution to Exercise 4"
    The variance of $r(t)$ is $\text{Var}[r(t)] = \eta^2(1 - e^{-2\lambda t})/(2\lambda)$. For large $t$:

    - Small $\lambda$ (e.g., $0.01$): The variance grows slowly toward $\eta^2/(2\lambda)$, which is large. Paths spread widely, similar to a random walk. The half-life is $\ln(2)/0.01 \approx 69$ years.
    - Large $\lambda$ (e.g., $1.0$): The variance quickly saturates at $\eta^2/2$, which is small. Paths cluster tightly around the mean. The half-life is $0.69$ years.

    Stronger mean reversion produces a tighter "funnel" of paths around $\theta(t)$, while weak mean reversion allows paths to wander far from the initial curve.
