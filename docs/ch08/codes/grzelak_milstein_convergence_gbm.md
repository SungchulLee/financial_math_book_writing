# Milstein Convergence Geometric Brownian Motion

## Background

Milstein discretization convergence for Geometric Brownian Motion.

Demonstrates weak and strong convergence properties of the Milstein scheme
for GBM approximation.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
Milstein discretization convergence for Geometric Brownian Motion.

Demonstrates weak and strong convergence properties of the Milstein scheme
for GBM approximation.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Path Generation
# =============================================================================

def generate_paths_gbm_milstein(num_paths, num_steps, maturity, r, sigma, s0):
    """
    Generate GBM paths using Milstein discretization.

    Parameters
    ----------
    num_paths : int
        Number of sample paths.
    num_steps : int
        Number of time steps.
    maturity : float
        Time to maturity (T).
    r : float
        Risk-free rate.
    sigma : float
        Volatility.
    s0 : float
        Initial stock price.

    Returns
    -------
    paths : dict
        Dictionary with keys 'time', 'S1' (Milstein approx), 'S2' (exact).
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))

    # Approximation (Milstein scheme)
    s1 = np.zeros((num_paths, num_steps + 1))
    s1[:, 0] = s0

    # Exact solution
    s2 = np.zeros((num_paths, num_steps + 1))
    s2[:, 0] = s0

    time = np.zeros(num_steps + 1)

    dt = maturity / float(num_steps)
    for i in range(num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]

        # Milstein scheme
        s1[:, i + 1] = (s1[:, i] + r * s1[:, i] * dt + sigma * s1[:, i] * (w[:, i + 1] - w[:, i])
                        + 0.5 * sigma ** 2 * s1[:, i] * ((w[:, i + 1] - w[:, i]) ** 2 - dt))

        # Exact solution
        s2[:, i + 1] = s2[:, i] * np.exp((r - 0.5 * sigma * sigma) * dt + sigma * (w[:, i + 1] - w[:, i]))
        time[i + 1] = time[i] + dt

    paths = {"time": time, "S1": s1, "S2": s2}
    return paths


# =============================================================================
# 2. Visualization
# =============================================================================

def plot_sample_paths(time, s1, s2):
    """
    Plot sample paths from Milstein and exact schemes.

    Parameters
    ----------
    time : ndarray
        Time grid.
    s1 : ndarray
        Milstein scheme paths.
    s2 : ndarray
        Exact scheme paths.
    """
    plt.figure(1, figsize=(10, 6))
    plt.plot(time, np.transpose(s1), 'k')
    plt.plot(time, np.transpose(s2), '--r')
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("S(t)")
    plt.tight_layout()


def plot_convergence(dt_vec, error_weak, error_strong):
    """
    Plot weak and strong convergence errors.

    Parameters
    ----------
    dt_vec : ndarray
        Vector of time steps.
    error_weak : ndarray
        Weak convergence errors.
    error_strong : ndarray
        Strong convergence errors.
    """
    plt.figure(2, figsize=(10, 6))
    plt.plot(dt_vec, error_weak)
    plt.plot(dt_vec, error_strong, '--r')
    plt.grid()
    plt.legend(['weak convergence', 'strong convergence'])
    plt.xlabel("dt")
    plt.ylabel("error")
    plt.tight_layout()


# =============================================================================
# 3. Main
# =============================================================================

def main():
    """Run convergence analysis for Milstein GBM scheme."""
    # ===== Sample Path Visualization =====
    num_paths = 25
    num_steps = 25
    maturity = 1.0
    r = 0.06  # Risk-free rate
    sigma = 0.3  # Volatility
    s0 = 50.0  # Initial stock price

    paths = generate_paths_gbm_milstein(num_paths, num_steps, maturity, r, sigma, s0)
    time = paths["time"]
    s1 = paths["S1"]
    s2 = paths["S2"]

    plot_sample_paths(time, s1, s2)

    # ===== Convergence Analysis =====
    num_steps_vec = range(1, 500, 1)
    num_paths = 100
    error_weak = np.zeros((len(num_steps_vec), 1))
    error_strong = np.zeros((len(num_steps_vec), 1))
    dt_vec = np.zeros((len(num_steps_vec), 1))

    for idx, num_steps in enumerate(num_steps_vec):
        paths = generate_paths_gbm_milstein(num_paths, num_steps, maturity, r, sigma, s0)
        # Get paths at maturity
        s1_at_t = paths["S1"][:, -1]
        s2_at_t = paths["S2"][:, -1]

        error_weak[idx] = np.abs(np.mean(s1_at_t) - np.mean(s2_at_t))
        error_strong[idx] = np.mean(np.abs(s1_at_t - s2_at_t))
        dt_vec[idx] = maturity / num_steps

    print(error_strong)
    plot_convergence(dt_vec, error_weak, error_strong)
    plt.show()


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Write the Milstein scheme for GBM and show that the correction term $\frac{1}{2}\sigma^2 S[(\Delta W)^2 - \Delta t]$ recovers strong order 1.

??? success "Solution to Exercise 1"
    The Milstein scheme: $S_{i+1} = S_i + rS_i\Delta t + \sigma S_i \Delta W_i + \frac{1}{2}\sigma^2 S_i[(\Delta W_i)^2 - \Delta t]$. This equals $S_i(1 + r\Delta t + \sigma\Delta W + \frac{\sigma^2}{2}((\Delta W)^2 - \Delta t))$. Expanding the exact $\exp((r - \sigma^2/2)\Delta t + \sigma\Delta W)$ to second order matches, confirming strong order 1.

---

**Exercise 2.**
If Euler strong error at $\Delta t = 0.002$ is $0.1$ and Milstein is $0.01$, estimate both at $\Delta t = 0.0002$.

??? success "Solution to Exercise 2"
    Euler ($O(\sqrt{\Delta t})$): $0.1/\sqrt{10} \approx 0.0316$. Milstein ($O(\Delta t)$): $0.01/10 = 0.001$. At $\Delta t = 0.0002$, Milstein is about 32 times more accurate.

---

**Exercise 3.**
For what class of SDEs does the Milstein scheme reduce to the Euler scheme?

??? success "Solution to Exercise 3"
    When $b^\prime(X) = 0$, i.e., when the diffusion coefficient is constant (additive noise). Examples: Ornstein-Uhlenbeck ($dX = \kappa(\theta - X)dt + \sigma dW$) and the Bachelier model. For these, both schemes have strong order 1.

---

**Exercise 4.**
How does the number of Monte Carlo paths (e.g., 100) affect the reliability of the estimated convergence rate?

??? success "Solution to Exercise 4"
    The standard error of the strong error estimate is $\text{SE} \approx \sigma_{\text{abs}}/\sqrt{N_{\text{paths}}}$. With 100 paths, $\text{SE} \approx \hat{\epsilon}/10$, giving 10% relative uncertainty. The convergence slope on a log-log plot has uncertainty $\pm 0.1$. Using 10,000 paths would reduce SE to 1%, giving a much cleaner convergence plot.