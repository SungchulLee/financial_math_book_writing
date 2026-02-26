#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_sde_simulation_statistics.py
SDE Simulation and Statistical Analysis

Credits
-------
Based on notebook "1.2 SDE simulations and statistics" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 3 -- SDEs).

Topics covered
--------------
1. Brownian motion path simulation and terminal-value statistics.
2. Hypothesis testing for normality:
   - Shapiro-Wilk, Jarque-Bera, Kolmogorov-Smirnov tests.
   - Q-Q plots.
3. Geometric Brownian motion simulation and parameter estimation.
4. GBM path generation.
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot


# ============================================================================
# 1. BROWNIAN MOTION SIMULATION
# ============================================================================

def simulate_brownian_motion(mu=0.1, sigma=0.2, T=100, paths=4000, steps=1000,
                             seed=42):
    """
    Simulate Brownian motion paths with drift mu and diffusion sigma.

    Each increment: dX = mu*dt + sigma*dW, where dW ~ N(0, dt).
    Terminal distribution: X_T ~ N(mu*T, sigma^2*T).

    Returns
    -------
    T_vec : ndarray  Time grid of shape (steps,).
    X : ndarray      Paths of shape (paths, steps).
    """
    np.random.seed(seed)
    T_vec, dt = np.linspace(0, T, steps, retstep=True)

    X0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(loc=mu * dt, scale=np.sqrt(dt) * sigma,
                             size=(paths, steps - 1))
    X = np.concatenate((X0, increments), axis=1).cumsum(1)
    return T_vec, X


def terminal_statistics(X_end, mu, sigma, T):
    """
    Print and return terminal value statistics for Brownian motion.

    Expected: E[X_T] = mu*T, Std[X_T] = sigma*sqrt(T).
    """
    mean_est = X_end.mean()
    std_est = X_end.std(ddof=1)
    print(f"E[X_T] estimated:  {mean_est:.4f}  (theoretical: {mu * T:.4f})")
    print(f"Std[X_T] estimated: {std_est:.4f}  (theoretical: {sigma * np.sqrt(T):.4f})")
    return {"mean": mean_est, "std": std_est}


# ============================================================================
# 2. HYPOTHESIS TESTING FOR NORMALITY
# ============================================================================

def normality_tests(data, true_loc=None, true_scale=None, alpha=0.05):
    """
    Run normality tests on the data and print results.

    Tests
    -----
    - Shapiro-Wilk: H0 = data are normally distributed.
    - Jarque-Bera:  H0 = data are normally distributed.
    - Kolmogorov-Smirnov: H0 = data follow N(true_loc, true_scale^2).
      (requires true_loc and true_scale; skipped if not provided.)

    Parameters
    ----------
    data : array_like     Sample to test.
    true_loc : float      Population mean (for KS test).
    true_scale : float    Population std dev (for KS test).
    alpha : float         Significance level.

    Returns
    -------
    dict  Test statistics and p-values.
    """
    results = {}

    # Shapiro-Wilk
    sw_stat, sw_p = ss.shapiro(data)
    verdict_sw = "reject H0" if sw_p < alpha else "cannot reject H0"
    print(f"Shapiro-Wilk:  stat={sw_stat:.6f}, p-value={sw_p:.6f}  => {verdict_sw}")
    results["shapiro_wilk"] = {"statistic": sw_stat, "pvalue": sw_p}

    # Jarque-Bera
    jb_stat, jb_p = ss.jarque_bera(data)
    verdict_jb = "reject H0" if jb_p < alpha else "cannot reject H0"
    print(f"Jarque-Bera:   stat={jb_stat:.6f}, p-value={jb_p:.6f}  => {verdict_jb}")
    results["jarque_bera"] = {"statistic": jb_stat, "pvalue": jb_p}

    # Kolmogorov-Smirnov
    if true_loc is not None and true_scale is not None:
        ks_stat, ks_p = ss.kstest(data,
                                  lambda x: ss.norm.cdf(x, loc=true_loc,
                                                        scale=true_scale))
        verdict_ks = "reject H0" if ks_p < alpha else "cannot reject H0"
        print(f"KS test:       stat={ks_stat:.6f}, p-value={ks_p:.6f}  => {verdict_ks}")
        results["ks_test"] = {"statistic": ks_stat, "pvalue": ks_p}

    return results


def plot_qq(data, title="Q-Q Plot"):
    """Plot a Q-Q plot for the sample against a normal reference."""
    plt.figure(figsize=(6, 5))
    qqplot(data, line="s", ax=plt.gca())
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_histogram_vs_normal(data, title="Histogram vs Normal distribution"):
    """
    Overlay a histogram of the data with the fitted normal density.
    """
    mu_fit, sigma_fit = ss.norm.fit(data)
    x = np.linspace(data.min(), data.max(), 200)
    pdf_fitted = ss.norm.pdf(x, mu_fit, sigma_fit)

    plt.figure(figsize=(8, 5))
    plt.plot(x, pdf_fitted, color="r", label="Fitted Normal")
    plt.hist(data, density=True, bins=50, facecolor="LightBlue",
             label="Histogram")
    plt.legend()
    plt.title(title)
    plt.xlabel("Value")
    plt.tight_layout()
    plt.show()


# ============================================================================
# 3. GEOMETRIC BROWNIAN MOTION
# ============================================================================

def simulate_gbm_terminal(S0=1, mu=0.1, sigma=0.2, T=10, N=10000, seed=42):
    """
    Simulate terminal values of a GBM process.

    S_T = S0 * exp((mu - sigma^2/2)*T + sigma*sqrt(T)*Z),  Z ~ N(0,1).

    Returns
    -------
    S_T : ndarray  Terminal stock prices of length N.
    """
    np.random.seed(seed)
    W = ss.norm.rvs(loc=(mu - 0.5 * sigma**2) * T,
                    scale=np.sqrt(T) * sigma, size=N)
    return S0 * np.exp(W)


def estimate_gbm_parameters(S_T, S0, T):
    """
    Estimate the drift mu and volatility sigma of a GBM from terminal
    prices by analysing the log-returns log(S_T / S0).

    log(S_T) ~ N((mu - sigma^2/2)*T, sigma^2*T)

    Returns
    -------
    dict  Estimated mu and sigma.
    """
    log_S = np.log(S_T / S0)
    sigma_hat = np.std(log_S, ddof=0) / np.sqrt(T)
    mu_hat = np.mean(log_S) / T + 0.5 * sigma_hat**2
    return {"mu": mu_hat, "sigma": sigma_hat}


def plot_gbm_histogram(S_T, S0, mu, sigma, T, title="GBM Histogram"):
    """
    Plot the histogram of GBM terminal values overlaid with the fitted
    log-normal density.
    """
    param_LN = ss.lognorm.fit(S_T)
    x = np.linspace(S_T.min(), S_T.max(), 200)
    pdf_fitted = ss.lognorm.pdf(x, *param_LN)

    plt.figure(figsize=(8, 5))
    plt.plot(x, pdf_fitted, color="r", label="Fitted Log-Normal")
    plt.hist(S_T, density=True, bins=50, facecolor="LightBlue",
             label="Histogram")
    plt.legend()
    plt.title(title)
    plt.xlabel("$S_T$")
    plt.tight_layout()
    plt.show()

    # Print fitted vs theoretical shape/scale
    print(f"Fitted   shape={param_LN[0]:.4f}, scale={param_LN[2]:.4f}")
    print(f"Theory   shape={sigma * np.sqrt(T):.4f}, "
          f"scale={np.exp((mu - 0.5 * sigma**2) * T):.4f}")


def simulate_gbm_paths(S0=1, mu=0.1, sigma=0.2, T=10, paths=10,
                        steps=1000, seed=42):
    """
    Simulate full GBM paths.

    Returns
    -------
    T_vec : ndarray  Time grid of shape (steps,).
    S : ndarray      Paths of shape (paths, steps).
    """
    np.random.seed(seed)
    T_vec, dt = np.linspace(0, T, steps, retstep=True)

    X0 = np.zeros((paths, 1))
    W = ss.norm.rvs((mu - 0.5 * sigma**2) * dt, np.sqrt(dt) * sigma,
                    (paths, steps - 1))
    X = np.concatenate((X0, W), axis=1).cumsum(1)
    S = S0 * np.exp(X)
    return T_vec, S


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_brownian_motion():
    """Full demo of BM simulation and statistical analysis."""
    print("=" * 60)
    print("Brownian Motion Simulation & Statistical Tests")
    print("=" * 60)

    mu, sigma, T = 0.1, 0.2, 100
    T_vec, X = simulate_brownian_motion(mu=mu, sigma=sigma, T=T)
    X_end = X[:, -1]

    # Plot paths
    plt.figure(figsize=(10, 5))
    plt.plot(T_vec, X[:8].T, alpha=0.7)
    plt.title("Brownian Motion Paths (8 of 4000)")
    plt.xlabel("Time")
    plt.show()

    # Terminal statistics
    print("\n--- Terminal statistics ---")
    terminal_statistics(X_end, mu, sigma, T)

    # Normality tests
    print("\n--- Normality tests ---")
    normality_tests(X_end, true_loc=mu * T, true_scale=sigma * np.sqrt(T))

    # Plots
    plot_histogram_vs_normal(X_end, "BM Terminal Values: Histogram vs Normal")
    plot_qq(X_end, "Q-Q Plot of BM Terminal Values")


def demo_gbm():
    """Full demo of GBM simulation and parameter estimation."""
    print("\n" + "=" * 60)
    print("Geometric Brownian Motion Simulation & Estimation")
    print("=" * 60)

    S0, mu, sigma, T = 1, 0.1, 0.2, 10

    # Terminal values
    S_T = simulate_gbm_terminal(S0, mu, sigma, T, N=10000)
    params = estimate_gbm_parameters(S_T, S0, T)
    print(f"\nTrue:      mu={mu}, sigma={sigma}")
    print(f"Estimated: mu={params['mu']:.6f}, sigma={params['sigma']:.6f}")

    plot_gbm_histogram(S_T, S0, mu, sigma, T)

    # Full paths
    T_vec, S = simulate_gbm_paths(S0, mu, sigma, T, paths=10)
    plt.figure(figsize=(10, 5))
    plt.plot(T_vec, S.T)
    plt.title("Geometric Brownian Motion Paths")
    plt.xlabel("Time")
    plt.ylabel("$S_t$")
    plt.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_brownian_motion()
    demo_gbm()
