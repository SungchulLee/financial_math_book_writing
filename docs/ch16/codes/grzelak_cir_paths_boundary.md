# Cox-Ingersoll-Ross Paths Boundary

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
Two boundary treatments for the Euler-discretized CIR process are reflection ($|v|$) and absorption ($\max(v, 0)$). Compare their biases.

??? success "Solution to Exercise 1"
    Reflection: $v_{t+1} = |v_t + \kappa(\theta - v_t)\Delta t + \sigma\sqrt{v_t}\Delta W|$. This overestimates the mean by reflecting negative values to positive, creating an upward bias. Absorption: $v_{t+1} = \max(v_{t+1}, 0)$. This underestimates the mean by clamping to zero, creating a downward bias. Both converge to the correct distribution as $\Delta t \to 0$.

---

**Exercise 2.**
For a CIR process that violates the Feller condition ($2\kappa\theta < \sigma^2$), how frequently does the Euler scheme produce negative values? Estimate for $\Delta t = 0.01$, $v_0 = 0.04$, $\sigma = 0.5$, $\kappa = 1$, $\theta = 0.04$.

??? success "Solution to Exercise 2"
    Check Feller: $2(1)(0.04) = 0.08 < 0.25 = \sigma^2$, violated. Near $v \approx 0$, the variance of the increment is $\sigma^2 v \Delta t \approx \sigma^2 \times 0.001 \times 0.01 = 2.5 \times 10^{-6}$, std $\approx 0.0016$. The drift at $v = 0.001$ is $\kappa\theta \Delta t = 0.0004$. The probability of going negative is $\Phi(-(0.001 + 0.0004)/0.0016) \approx \Phi(-0.875) \approx 19\%$ when the process is near zero. This happens frequently.

---

**Exercise 3.**
The full truncation scheme uses $v^+ = \max(v, 0)$ inside the drift and diffusion: $v_{t+1} = v_t + \kappa(\theta - v_t^+)\Delta t + \sigma\sqrt{v_t^+}\Delta W$. Explain why this preserves the mean-reversion property.

??? success "Solution to Exercise 3"
    When $v_t < 0$ (a discretization artifact), $v_t^+ = 0$, so the drift becomes $\kappa\theta\Delta t > 0$ (strongly positive), pushing $v$ back toward $\theta$. The diffusion is zero (no noise at $v = 0$), preventing further negative excursions. This ensures the process recovers quickly from negative values while preserving the correct long-run mean $\theta$.

---

**Exercise 4.**
Plot (conceptually) the CIR path density at $T = 1$ for both Euler with reflection and exact simulation. Where do they differ most?

??? success "Solution to Exercise 4"
    The densities differ most near $v = 0$: reflection creates a spurious peak at small positive $v$ (reflected mass from would-be negative values), while the exact distribution has a smooth density approaching zero at $v = 0$ (when Feller holds) or a mass at $v = 0$ (when violated). For moderate $v$ values, both agree well. The right tail also differs slightly due to accumulated bias from multiple boundary corrections.