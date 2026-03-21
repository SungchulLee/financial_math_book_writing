# -*- coding: utf-8 -*-
"""
Martingale Property Verification via Nested Monte Carlo

Demonstrates that E[W(t) | F(s)] = W(s) for Brownian motion using nested
Monte Carlo simulation. Two experiments are performed:
  (A) Verify E[W(t) | F(0)] = W(0) = 0  (unconditional expectation).
  (B) Verify E[W(t) | F(s)] = W(s)  via nested sub-simulations.

For experiment (B), outer paths are simulated from 0 to s, then for each
realized W(s) a batch of inner paths continues from s to t. The conditional
expectation is estimated as the mean of the inner terminal values.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
    Course: Financial Engineering, L.A. Grzelak.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Unconditional Martingale Check
# =============================================================================

def verify_unconditional_expectation(t, num_paths):
    """
    Verify E[W(t) | F(0)] = 0 by sampling W(t) ~ N(0, t).

    Parameters
    ----------
    t : float
        Terminal time.
    num_paths : int
        Number of Monte Carlo samples.

    Returns
    -------
    mean_wt : float
        Sample mean of W(t).
    """
    w_t = np.random.normal(0.0, np.sqrt(t), (num_paths, 1))
    mean_wt = np.mean(w_t)
    return mean_wt


# =============================================================================
# 2. Nested Monte Carlo for Conditional Expectation
# =============================================================================

def normalize_samples(z):
    """
    Normalize a vector to have mean 0 and standard deviation 1.

    Parameters
    ----------
    z : ndarray
        Raw normal samples.

    Returns
    -------
    ndarray
        Normalized samples.
    """
    return (z - np.mean(z)) / np.std(z)


def simulate_brownian_paths(num_paths, num_steps, dt):
    """
    Simulate Brownian motion paths on a uniform time grid.

    Parameters
    ----------
    num_paths : int
        Number of paths to simulate.
    num_steps : int
        Number of time steps.
    dt : float
        Time increment per step.

    Returns
    -------
    W : ndarray, shape (num_paths, num_steps + 1)
        Brownian motion paths starting at 0.
    """
    Z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    W = np.zeros((num_paths, num_steps + 1))

    for i in range(num_steps):
        Z[:, i] = normalize_samples(Z[:, i])
        W[:, i + 1] = W[:, i] + np.sqrt(dt) * Z[:, i]

    return W


def verify_conditional_expectation(t, s, num_paths, num_steps):
    """
    Verify E[W(t) | F(s)] = W(s) via nested Monte Carlo.

    For each outer path, W(s) is realized. Then an inner batch of paths
    is simulated from s to t, all starting at the realized W(s). The
    conditional expectation is estimated as the inner-sample mean of W(t).

    Parameters
    ----------
    t : float
        Terminal time (t > s).
    s : float
        Conditioning time.
    num_paths : int
        Number of outer and inner paths.
    num_steps : int
        Number of time steps per segment.

    Returns
    -------
    w_s : ndarray, shape (num_paths,)
        Realized values of W(s) for each outer path.
    e_wt : ndarray, shape (num_paths,)
        Estimated E[W(t) | F(s)] for each outer path.
    errors : ndarray, shape (num_paths,)
        Difference e_wt - w_s (should be near zero).
    outer_paths : ndarray, shape (num_paths, num_steps + 1)
        Outer Brownian paths from 0 to s.
    first_inner_paths : ndarray, shape (num_paths, num_steps + 1)
        Inner sub-paths for the first outer realization (for plotting).
    """
    # Outer simulation: 0 → s
    dt_outer = s / num_steps
    outer_paths = simulate_brownian_paths(num_paths, num_steps, dt_outer)
    w_s = outer_paths[:, -1]

    # Inner simulation: s → t for each outer path
    dt_inner = (t - s) / num_steps
    e_wt = np.zeros(num_paths)
    first_inner_paths = None

    for i in range(num_paths):
        Z_inner = np.random.normal(0.0, 1.0, (num_paths, num_steps))
        W_inner = np.zeros((num_paths, num_steps + 1))
        W_inner[:, 0] = w_s[i]

        for j in range(num_steps):
            Z_inner[:, j] = normalize_samples(Z_inner[:, j])
            W_inner[:, j + 1] = W_inner[:, j] + np.sqrt(dt_inner) * Z_inner[:, j]

        e_wt[i] = np.mean(W_inner[:, -1])

        if i == 0:
            first_inner_paths = W_inner.copy()

    errors = e_wt - w_s
    return w_s, e_wt, errors, outer_paths, first_inner_paths


# =============================================================================
# 3. Visualization
# =============================================================================

def plot_nested_simulation(t, s, num_steps, outer_path, inner_paths):
    """
    Plot one outer path (0 → s) and its inner sub-simulations (s → t).

    Parameters
    ----------
    t : float
        Terminal time.
    s : float
        Conditioning time.
    num_steps : int
        Number of time steps per segment.
    outer_path : ndarray, shape (num_steps + 1,)
        Single outer Brownian path.
    inner_paths : ndarray, shape (num_inner, num_steps + 1)
        Inner sub-simulation paths from the outer path's W(s).
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    time_outer = np.linspace(0, s, num_steps + 1)
    time_inner = np.linspace(s, t, num_steps + 1)

    ax.plot(time_outer, outer_path, "b-", linewidth=2, label="Outer path (0 → s)")
    for j in range(inner_paths.shape[0]):
        ax.plot(time_inner, inner_paths[j, :], alpha=0.15, color="orange", linewidth=0.5)

    ax.axvline(x=s, color="red", linestyle="--", alpha=0.6, label=f"Conditioning time s={s}")
    ax.set_xlabel("Time")
    ax.set_ylabel("W(t)")
    ax.set_title("Nested Monte Carlo: E[W(t) | F(s)] = W(s)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# =============================================================================
# 4. Main
# =============================================================================

def main():
    """Run martingale verification experiments."""
    # Parameters
    t = 10            # Terminal time
    s = 5             # Conditioning time
    num_paths = 1000  # Number of Monte Carlo paths
    num_steps = 10    # Time steps per segment

    # --- Experiment A: E[W(t) | F(0)] = 0 ---
    mean_wt = verify_unconditional_expectation(t, num_paths)
    print(f"Experiment A: E[W(t)|F(0)]")
    print(f"  Sample mean = {mean_wt:.4f},  expected = 0.00")

    # --- Experiment B: E[W(t) | F(s)] = W(s) via nested MC ---
    w_s, e_wt, errors, outer_paths, first_inner = verify_conditional_expectation(
        t, s, num_paths, num_steps
    )
    max_error = np.max(np.abs(errors))
    print(f"\nExperiment B: E[W(t)|F(s)] = W(s)  (nested MC)")
    print(f"  Max |E[W(t)|F(s)] - W(s)| = {max_error:.6f}")

    # --- Plot first outer path with its inner sub-simulations ---
    plot_nested_simulation(t, s, num_steps, outer_paths[0, :], first_inner)


if __name__ == "__main__":
    main()
