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
