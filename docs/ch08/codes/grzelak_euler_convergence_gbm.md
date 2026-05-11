# Euler Convergence Geometric Brownian Motion

## Background

Euler discretization convergence for Geometric Brownian Motion.

Demonstrates weak and strong convergence properties of the Euler scheme
for GBM approximation.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
Euler discretization convergence for Geometric Brownian Motion.

Demonstrates weak and strong convergence properties of the Euler scheme
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

def generate_paths_gbm_euler(num_paths, num_steps, maturity, r, sigma, s0):
    """
    Generate GBM paths using Euler discretization.

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
        Dictionary with keys 'time', 'S1' (Euler approx), 'S2' (exact).
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))

    # Approximation (Euler scheme)
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

        # Euler scheme
        s1[:, i + 1] = s1[:, i] + r * s1[:, i] * dt + sigma * s1[:, i] * (w[:, i + 1] - w[:, i])

        # Exact solution
        s2[:, i + 1] = s2[:, i] * np.exp((r - 0.5 * sigma ** 2.0) * dt + sigma * (w[:, i + 1] - w[:, i]))
        time[i + 1] = time[i] + dt

    paths = {"time": time, "S1": s1, "S2": s2}
    return paths


# =============================================================================
# 2. Visualization
# =============================================================================

def plot_sample_paths(time, s1, s2):
    """
    Plot sample paths from Euler and exact schemes.

    Parameters
    ----------
    time : ndarray
        Time grid.
    s1 : ndarray
        Euler scheme paths.
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
    """Run convergence analysis for Euler GBM scheme."""
    # ===== Sample Path Visualization =====
    num_paths = 25
    num_steps = 25
    maturity = 1.0
    r = 0.06  # Risk-free rate
    sigma = 0.3  # Volatility
    s0 = 50.0  # Initial stock price

    paths = generate_paths_gbm_euler(num_paths, num_steps, maturity, r, sigma, s0)
    time = paths["time"]
    s1 = paths["S1"]
    s2 = paths["S2"]

    plot_sample_paths(time, s1, s2)

    # ===== Convergence Analysis =====
    num_steps_vec = range(1, 500, 1)
    num_paths = 250
    error_weak = np.zeros((len(num_steps_vec), 1))
    error_strong = np.zeros((len(num_steps_vec), 1))
    dt_vec = np.zeros((len(num_steps_vec), 1))

    for idx, num_steps in enumerate(num_steps_vec):
        paths = generate_paths_gbm_euler(num_paths, num_steps, maturity, r, sigma, s0)
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
Show that the Euler scheme for GBM has weak convergence order 1 and strong convergence order 0.5.

??? success "Solution to Exercise 1"
    Weak convergence: expanding the exact solution to first order in $\Delta t$ matches the Euler step, giving accumulated error $O(\Delta t)$ over $N = T/\Delta t$ steps (order 1). Strong convergence: the Euler scheme misses the Ito correction term $-\frac{\sigma^2}{2}S\Delta t$. Each step has $O(\Delta t)$ error, but pathwise accumulation as a random walk gives $O(\sqrt{\Delta t})$ (order 0.5).

---

**Exercise 2.**
For GBM with $r = 0.06$, $\sigma = 0.3$, $S_0 = 50$, $T = 1$, compute $\mathbb{E}[S_T]$ exactly and explain why Euler can estimate the mean accurately despite low strong order.

??? success "Solution to Exercise 2"
    $\mathbb{E}[S_T] = 50 e^{0.06} = \$53.09$. Euler preserves $\mathbb{E}[S_{i+1}|S_i] = S_i(1 + r\Delta t)$, so the mean is accurately estimated. Weak convergence (order 1) governs expectations; strong convergence (order 0.5) governs individual paths. For pricing via expectations, Euler is effective even with moderate steps.

---

**Exercise 3.**
Explain why normalizing random samples ($z \leftarrow (z - \bar{z})/s_z$) at each step improves convergence.

??? success "Solution to Exercise 3"
    Normalization forces exact zero mean and unit variance at each step, eliminating finite-sample bias in the drift and realized volatility. This moment matching reduces Monte Carlo variance, producing smoother convergence plots, especially with few paths.

---

**Exercise 4.**
On a log-log plot, the weak error has slope 1 and the strong error has slope 0.5. If the strong error at $\Delta t = 0.01$ is $0.5$, estimate it at $\Delta t = 0.001$.

??? success "Solution to Exercise 4"
    $\epsilon_s \propto \sqrt{\Delta t}$. At $\Delta t = 0.01$: $C_s = 0.5/\sqrt{0.01} = 5$. At $\Delta t = 0.001$: $\epsilon_s = 5\sqrt{0.001} = 0.158$. Reducing $\Delta t$ tenfold reduces strong error by factor $\sqrt{10} \approx 3.16$.