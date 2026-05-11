# Cox-Ingersoll-Ross Exact Simulation

## Background

CIR process paths using Euler discretization with two boundary conditions.

Demonstrates the Cox-Ingersoll-Ross (CIR) interest rate model with Euler
discretization, comparing truncated and reflecting boundary conditions
to ensure non-negativity of the variance process.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
CIR process paths using Euler discretization with two boundary conditions.

Demonstrates the Cox-Ingersoll-Ross (CIR) interest rate model with Euler
discretization, comparing truncated and reflecting boundary conditions
to ensure non-negativity of the variance process.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Core Computation
# =============================================================================

def generate_paths_cir_euler_2schemes(num_paths, num_steps, t, kappa, v0,
                                       vbar, gamma):
    """
    Generate CIR process paths using two boundary condition schemes.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    t : float
        Terminal time.
    kappa : float
        Mean reversion speed.
    v0 : float
        Initial variance level.
    vbar : float
        Long-term mean variance.
    gamma : float
        Volatility of variance (vol of vol).

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid of shape (num_steps+1,)
        - 'Vtruncated': truncated boundary CIR paths of shape
                        (num_paths, num_steps+1)
        - 'Vreflected': reflecting boundary CIR paths of shape
                        (num_paths, num_steps+1)
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    v1 = np.zeros((num_paths, num_steps + 1))
    v2 = np.zeros((num_paths, num_steps + 1))
    v1[:, 0] = v0
    v2[:, 0] = v0
    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)

    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])

        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]

        # Truncated boundary condition
        v1[:, i + 1] = (v1[:, i] + kappa * (vbar - v1[:, i]) * dt +
                        gamma * np.sqrt(v1[:, i]) * (w[:, i + 1] - w[:, i]))
        v1[:, i + 1] = np.maximum(v1[:, i + 1], 0.0)

        # Reflecting boundary condition
        v2[:, i + 1] = (v2[:, i] + kappa * (vbar - v2[:, i]) * dt +
                        gamma * np.sqrt(v2[:, i]) * (w[:, i + 1] - w[:, i]))
        v2[:, i + 1] = np.absolute(v2[:, i + 1])

        time[i + 1] = time[i] + dt

    # Outputs
    paths = {"time": time, "Vtruncated": v1, "Vreflected": v2}
    return paths


# =============================================================================
# 2. Plotting Functions
# =============================================================================

def plot_cir_paths(time_grid, v_truncated, v_reflected):
    """
    Plot CIR paths with both boundary conditions.

    Parameters
    ----------
    time_grid : ndarray
        Time grid of shape (num_steps+1,).
    v_truncated : ndarray
        CIR paths with truncated boundary of shape (num_paths, num_steps+1).
    v_reflected : ndarray
        CIR paths with reflecting boundary of shape (num_paths, num_steps+1).

    Returns
    -------
    None
    """
    plt.figure()
    plt.plot(time_grid, np.transpose(v_truncated), 'b')
    plt.plot(time_grid, np.transpose(v_reflected), '--r')
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("V(t)")
    plt.legend(['truncated scheme', 'reflecting scheme'])


# =============================================================================
# 3. Main Computation
# =============================================================================

def main():
    """Run demonstration of CIR process with boundary conditions."""
    # Parameters
    num_paths = 1
    num_steps = 20
    t = 1.0
    kappa = 0.5
    v0 = 0.1
    vbar = 0.1
    gamma = 0.8

    np.random.seed(210)
    paths = generate_paths_cir_euler_2schemes(num_paths, num_steps, t, kappa,
                                              v0, vbar, gamma)
    time_grid = paths["time"]
    v_truncated = paths["Vtruncated"]
    v_reflected = paths["Vreflected"]

    plot_cir_paths(time_grid, v_truncated, v_reflected)


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The CIR process can be simulated exactly using the non-central chi-squared distribution. Write the distribution of $r_{t+\Delta t}$ given $r_t$.

??? success "Solution to Exercise 1"
    Given $r_t$, the scaled future rate $\frac{4\kappa}{\sigma^2(1-e^{-\kappa\Delta t})}r_{t+\Delta t}$ follows a non-central chi-squared distribution with $d = \frac{4\kappa\theta}{\sigma^2}$ degrees of freedom and non-centrality parameter $\lambda = \frac{4\kappa e^{-\kappa\Delta t}}{\sigma^2(1-e^{-\kappa\Delta t})}r_t$. This exact distribution avoids discretization error entirely.

---

**Exercise 2.**
Compare the exact CIR simulation with the Euler scheme in terms of: (a) accuracy, (b) computational cost, (c) handling of the zero boundary.

??? success "Solution to Exercise 2"
    (a) Exact simulation has zero discretization error; Euler has $O(\Delta t)$ error. (b) Exact requires sampling from non-central $\chi^2$ (more expensive per step) vs simple Gaussian for Euler. (c) Exact automatically respects $r \geq 0$ when Feller holds; Euler can produce negative values requiring ad-hoc fixes. For pricing, exact simulation is preferred when feasible.

---

**Exercise 3.**
For the CIR process with $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.1$, compute the degrees of freedom $d$ of the chi-squared distribution.

??? success "Solution to Exercise 3"
    $d = 4\kappa\theta/\sigma^2 = 4(0.5)(0.05)/0.01 = 10$. Since $d > 2$ (equivalent to the Feller condition $2\kappa\theta > \sigma^2$), the distribution is well-defined and the rate stays strictly positive.

---

**Exercise 4.**
Explain why exact simulation is particularly important for the CIR process compared to, say, GBM.

??? success "Solution to Exercise 4"
    GBM has a closed-form exact simulation ($S_{t+\Delta t} = S_t \exp((r-\sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}Z)$), so Euler is unnecessary. The CIR process has no such simple update; the Euler scheme can violate the positivity constraint, causing crashes or biased results. Exact CIR simulation via non-central $\chi^2$ preserves all statistical properties, making it essential for accurate bond pricing and variance simulation in Heston.