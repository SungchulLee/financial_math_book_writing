# -*- coding: utf-8 -*-
"""
girsanov_drift_change.py

Girsanov Drift Change — Visualization and Utilities

This module implements the Girsanov theorem for changing probability measures.
It provides functions to compute the Radon–Nikodym derivative dQ/dP, transform
PDFs from the physical measure P to the risk-neutral measure Q, and generate
Brownian motion paths under both measures.

Key concepts:
    - Under the physical measure P, B_t is a standard Brownian motion.
    - Under the risk-neutral measure Q (via Girsanov), B̃_t = B_t + θt is a
      standard Brownian motion, where θ is the market price of risk.
    - The Radon–Nikodym derivative is:
        dQ/dP = exp( -½ θ² T - θ (B_T - θT) )

Based on: QuantPie Lecture Notes on Change of Numeraire / Girsanov Theorem
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# ---------------------------------------------------------------------------
# Radon–Nikodym derivative and PDF transformations
# ---------------------------------------------------------------------------

def compute_dQ_over_dP(x, T, theta):
    """
    Compute the Radon–Nikodym derivative dQ/dP evaluated at terminal
    Brownian motion value x.

    Parameters
    ----------
    x : float or ndarray
        Terminal value of B_T under the physical measure P.
    T : float
        Time horizon.
    theta : float
        Girsanov drift parameter (market price of risk).

    Returns
    -------
    float or ndarray
        dQ/dP = exp( -θ²T/2 - θ(x - θT) )
    """
    return np.exp(-theta**2 * T / 2 - theta * (x - theta * T))


def compute_pdf_under_Q(T, theta, pdf_under_P):
    """
    Transform a continuous PDF from the P-measure to the Q-measure.

    Parameters
    ----------
    T : float
        Time horizon.
    theta : float
        Girsanov drift parameter.
    pdf_under_P : callable
        PDF of B_T under P, e.g. stats.norm(0, sqrt(T)).pdf

    Returns
    -------
    callable
        PDF of B_T under Q: p_Q(x) = p_P(x) * dQ/dP(x).
    """
    return lambda x: pdf_under_P(x) * compute_dQ_over_dP(x, T, theta)


def compute_pdf_under_Q_using_histogram(T, theta, pdf_under_P_using_histogram, bins_loc):
    """
    Transform a histogram-based empirical PDF from P to Q.

    Parameters
    ----------
    T : float
        Time horizon.
    theta : float
        Girsanov drift parameter.
    pdf_under_P_using_histogram : ndarray
        Histogram bin heights under P.
    bins_loc : ndarray
        Bin center locations.

    Returns
    -------
    ndarray
        Histogram bin heights under Q.
    """
    return pdf_under_P_using_histogram * compute_dQ_over_dP(bins_loc, T, theta)


# ---------------------------------------------------------------------------
# Discrete relative probabilities (importance weights)
# ---------------------------------------------------------------------------

def compute_dQ_over_dP_relative_probabilities(num_steps, theta, T, db):
    """
    Compute relative importance weights (unnormalized) for each path
    using the discrete-time Radon–Nikodym derivative.

    Parameters
    ----------
    num_steps : int
        Total number of discrete steps.
    theta : float
        Girsanov drift parameter.
    T : float
        Time horizon.
    db : ndarray of shape (num_paths, num_steps)
        Brownian increments under P.

    Returns
    -------
    ndarray of shape (num_paths,)
        Relative probabilities (exponent shifted for numerical stability).
    """
    n = int(num_steps / T)  # number of steps per unit time
    dt = 1 / n
    exponent = np.sum(-(1 / 2) * theta**2 * dt - theta * db, axis=1)
    exponent_max = max(exponent)
    exponent_rel = exponent - exponent_max
    return np.exp(exponent_rel)


# ---------------------------------------------------------------------------
# Path generation under P and Q
# ---------------------------------------------------------------------------

def generate_BT_and_BT_prime(n_sim, T, theta, seed=None):
    """
    Generate terminal Brownian motion values under P and their
    Girsanov-shifted counterparts under Q.

    Parameters
    ----------
    n_sim : int
        Number of simulations.
    T : float
        Time horizon.
    theta : float
        Girsanov drift parameter.
    seed : int, optional
        Random seed.

    Returns
    -------
    BT : ndarray of shape (n_sim,)
        Terminal B_T under P ~ N(0, T).
    BT_prime : ndarray of shape (n_sim,)
        Shifted B̃_T = B_T + θT (standard BM under Q).
    """
    if seed is not None:
        np.random.seed(seed)
    BT = np.random.normal(loc=0, scale=np.sqrt(T), size=(n_sim,))
    BT_prime = BT + theta * T
    return BT, BT_prime


def generate_db_tilde(num_paths, num_steps, theta, T, seed=None):
    """
    Generate discrete Brownian increments and their risk-neutral (Q)
    adjusted counterparts using a symmetric random walk.

    Parameters
    ----------
    num_paths : int
        Number of sample paths.
    num_steps : int
        Number of time steps.
    theta : float
        Girsanov drift parameter.
    T : float
        Time horizon.
    seed : int, optional
        Random seed.

    Returns
    -------
    db_tilde : ndarray of shape (num_paths, num_steps)
        Risk-neutral increments: db + θ·dt
    db : ndarray of shape (num_paths, num_steps)
        Physical measure increments.
    theta_dt : float
        Drift adjustment per step.
    """
    if seed is not None:
        np.random.seed(seed)
    plus_minus_one = 2 * np.random.binomial(1, 0.5, size=(num_paths, num_steps)) - 1
    n = int(num_steps / T)  # number of steps per unit time
    db = plus_minus_one / np.sqrt(n)
    theta_dt = theta / n
    db_tilde = db + theta_dt
    return db_tilde, db, theta_dt


def generate_sample_path(num_paths, num_steps, theta, T, seed=None):
    """
    Generate full sample paths of Brownian motion with drift (under Q)
    together with importance weights for measure change.

    Parameters
    ----------
    num_paths : int
        Number of sample paths.
    num_steps : int
        Number of time steps.
    theta : float
        Girsanov drift parameter.
    T : float
        Time horizon.
    seed : int, optional
        Random seed.

    Returns
    -------
    b_plus_drift : ndarray of shape (num_paths, num_steps + 1)
        Cumulative paths B_t + θt (Brownian motion under Q).
    relative_probabilities : ndarray of shape (num_paths,)
        Importance weights for each path.
    """
    db_tilde, db, theta_dt = generate_db_tilde(num_paths, num_steps, theta, T, seed=seed)

    b_plus_drift = np.cumsum(db_tilde, axis=1)
    b_plus_drift = np.concatenate((np.zeros((num_paths, 1)), b_plus_drift), axis=1)

    relative_probabilities = compute_dQ_over_dP_relative_probabilities(num_steps, theta, T, db)
    return b_plus_drift, relative_probabilities


# ---------------------------------------------------------------------------
# Main — demonstration / visualization
# ---------------------------------------------------------------------------

def main():
    """Demonstrate Girsanov drift change with visualization."""
    print("Girsanov Drift Change Visualization")
    print("=" * 50)

    # Parameters
    T = 1.0
    theta = 1.5       # market price of risk
    num_paths = 5000
    num_steps = 200
    seed = 42

    # --- 1. Terminal distribution comparison ---
    BT, BT_prime = generate_BT_and_BT_prime(num_paths, T, theta, seed=seed)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Histogram under P
    axes[0].hist(BT, bins=60, density=True, alpha=0.6, color="steelblue", label="Simulated (P)")
    x = np.linspace(-4, 4, 300)
    axes[0].plot(x, stats.norm(0, np.sqrt(T)).pdf(x), "k-", lw=2, label=r"$N(0, T)$")
    axes[0].set_title(r"$B_T$ under $\mathbb{P}$")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Histogram under Q (reweighted)
    pdf_P = stats.norm(0, np.sqrt(T)).pdf
    pdf_Q = compute_pdf_under_Q(T, theta, pdf_P)
    axes[1].hist(BT_prime, bins=60, density=True, alpha=0.6, color="coral", label=r"Simulated ($\tilde{B}_T$ under Q)")
    axes[1].plot(x, pdf_Q(x), "k--", lw=2, label=r"Reweighted PDF")
    axes[1].plot(x, stats.norm(theta * T, np.sqrt(T)).pdf(x), "g-", lw=1.5, label=r"$N(\theta T, T)$")
    axes[1].set_title(r"$\tilde{B}_T = B_T + \theta T$ under $\mathbb{Q}$")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.suptitle(f"Girsanov Theorem: Drift Change (θ = {theta})", fontsize=14)
    plt.tight_layout()
    plt.savefig("/tmp/girsanov_drift_change.png", dpi=150)
    print("Figure saved to /tmp/girsanov_drift_change.png")
    plt.close()

    # --- 2. Sample paths with importance weights ---
    paths, weights = generate_sample_path(20, num_steps, theta, T, seed=seed)
    t_grid = np.linspace(0, T, num_steps + 1)

    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(20):
        alpha = 0.3 + 0.7 * weights[i] / weights.max()
        ax.plot(t_grid, paths[i], alpha=alpha, lw=0.8)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$B_t + \theta t$")
    ax.set_title(f"Girsanov Sample Paths (opacity ∝ dQ/dP weight, θ = {theta})")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/girsanov_sample_paths.png", dpi=150)
    print("Figure saved to /tmp/girsanov_sample_paths.png")
    plt.close()


if __name__ == "__main__":
    main()
