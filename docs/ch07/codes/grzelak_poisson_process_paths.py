# -*- coding: utf-8 -*-
"""
Generate sample paths for the Poisson process and compensated Poisson process.

This script demonstrates Monte Carlo simulation of Poisson processes, including
the standard Poisson process and its compensated (martingale) version. Sample
paths are generated and visualized to illustrate their behavior.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Path Generation
# =============================================================================

def generate_paths_poisson(num_paths, num_steps, T, xi_p):
    """
    Generate sample paths for Poisson and compensated Poisson processes.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    T : float
        Time to maturity.
    xi_p : float
        Jump intensity (Poisson parameter).

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid (ndarray of shape (num_steps+1,))
        - 'X': Poisson process (ndarray of shape (num_paths, num_steps+1))
        - 'Xcomp': compensated Poisson process (ndarray of shape
                   (num_paths, num_steps+1))
    """
    # Create empty matrices for Poisson and compensated Poisson processes
    x = np.zeros((num_paths, num_steps + 1))
    x_comp = np.zeros((num_paths, num_steps + 1))
    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)

    # Generate Poisson random variables
    z = np.random.poisson(xi_p * dt, (num_paths, num_steps))

    for i in range(0, num_steps):
        # Update Poisson process
        x[:, i + 1] = x[:, i] + z[:, i]
        # Update compensated (martingale) Poisson process
        x_comp[:, i + 1] = x_comp[:, i] - xi_p * dt + z[:, i]
        time[i + 1] = time[i] + dt

    paths = {"time": time, "X": x, "Xcomp": x_comp}
    return paths


# =============================================================================
# 2. Visualization
# =============================================================================

def plot_poisson_process(time, x):
    """
    Plot Poisson process sample paths.

    Parameters
    ----------
    time : ndarray
        Time grid.
    x : ndarray
        Poisson process paths of shape (num_paths, num_steps+1).
    """
    plt.figure(1)
    plt.plot(time, np.transpose(x), '-b')
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("X(t)")
    plt.tight_layout()


def plot_compensated_poisson(time, x_comp):
    """
    Plot compensated Poisson process sample paths.

    Parameters
    ----------
    time : ndarray
        Time grid.
    x_comp : ndarray
        Compensated Poisson process paths of shape (num_paths, num_steps+1).
    """
    plt.figure(2)
    plt.plot(time, np.transpose(x_comp), '-b')
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("X(t)")
    plt.tight_layout()


# =============================================================================
# 3. Main
# =============================================================================

def main():
    """Run Poisson process path generation demonstration."""
    # Parameters
    num_paths = 25         # Number of Monte Carlo paths
    num_steps = 500        # Number of time steps
    T = 30.0               # Time to maturity
    xi_p = 1.0             # Jump intensity

    # Generate paths
    paths = generate_paths_poisson(num_paths, num_steps, T, xi_p)
    time_grid = paths["time"]
    x = paths["X"]
    x_comp = paths["Xcomp"]

    # Visualize results
    plot_poisson_process(time_grid, x)
    plot_compensated_poisson(time_grid, x_comp)
    plt.show()


if __name__ == "__main__":
    main()
