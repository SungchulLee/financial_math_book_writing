#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Levy Process Parameter Estimation: VG and NIG -- Educational Version
=====================================================================

Based on cells 36-62 of the notebook "1.5 SDE - Levy processes" from
"Financial Models Numerical Methods" by cantaro86.

Original repository:
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

References:
    [1] Cont, R. and Tankov, P. (2003) "Financial Modelling with Jump
        Processes", Chapman and Hall/CRC.
    [2] Madan, D. and Seneta, E. (1990) "The Variance Gamma model for
        share market returns", The Journal of Business, 63(4), 511-524.
    [3] Barndorff-Nielsen, O. E. (1998) "Processes of Normal Inverse
        Gaussian type", Finance and Stochastics, 2, 41-68.

This file implements a two-stage parameter estimation pipeline for both the
Variance Gamma (VG) and Normal Inverse Gaussian (NIG) Levy processes:

    Stage 1 -- Approximated Method of Moments (MoM):
        A first-order Taylor expansion in theta decouples the moment
        equations, yielding closed-form estimators that serve as warm
        starts for the optimizer.

    Stage 2 -- Maximum Likelihood Estimation (MLE):
        L-BFGS-B optimization of the log-likelihood, seeded with the
        MoM estimates and constrained to enforce the correct sign of
        theta (matching the observed skewness).

Also included is a simulation of the Inverse Gaussian first-passage-time
distribution, which provides physical intuition for WHY the IG distribution
arises as the NIG subordinator.

This file is self-contained and requires only standard scientific Python
libraries: numpy, scipy, matplotlib.
"""

import numpy as np
import scipy.stats as ss
import scipy.special as scps
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# ============================================================================
# VG and NIG Density Functions
# ============================================================================

def VG_density(x, T, c, theta, sigma, kappa):
    """
    Variance Gamma probability density function.

    The VG density is expressed in terms of the modified Bessel function of
    the second kind K_v.  With location parameter c (deterministic drift),
    the VG random variable at time T is:

        Y_T = c * T + X_T^{VG}

    Parameters
    ----------
    x : array_like
        Points at which to evaluate the density.
    T : float
        Time horizon.
    c : float
        Deterministic drift (location parameter).
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance rate of the Gamma subordinator.

    Returns
    -------
    array_like
        VG density values.

    Notes
    -----
    The density formula is (see [1], Section 4.3):

        f(x) = 2 * exp(theta*(x-c) / sigma^2)
               / (kappa^(T/kappa) * sqrt(2*pi) * sigma * Gamma(T/kappa))
               * ((x-c)^2 / (2*sigma^2/kappa + theta^2))^(T/(2*kappa) - 1/4)
               * K_{T/kappa - 1/2}(
                     sigma^{-2} * sqrt((x-c)^2 * (2*sigma^2/kappa + theta^2))
                 )

    where K_v is the modified Bessel function of the second kind (order v).
    """
    return (
        2
        * np.exp(theta * (x - c) / sigma**2)
        / (kappa ** (T / kappa) * np.sqrt(2 * np.pi) * sigma
           * scps.gamma(T / kappa))
        * ((x - c) ** 2
           / (2 * sigma**2 / kappa + theta**2)) ** (T / (2 * kappa) - 0.25)
        * scps.kv(
            T / kappa - 0.5,
            sigma ** (-2)
            * np.sqrt((x - c) ** 2 * (2 * sigma**2 / kappa + theta**2)),
        )
    )


def NIG_density(x, T, c, theta, sigma, kappa):
    """
    Normal Inverse Gaussian probability density function.

    With location parameter c (deterministic drift), the NIG random
    variable at time T is:

        Y_T = c * T + X_T^{NIG}

    Parameters
    ----------
    x : array_like
        Points at which to evaluate the density.
    T : float
        Time horizon.
    c : float
        Deterministic drift (location parameter).
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance of the Inverse Gaussian subordinator.

    Returns
    -------
    array_like
        NIG density values.

    Notes
    -----
    Defining:
        A = theta / sigma^2
        B = sqrt(theta^2 + sigma^2/kappa) / sigma^2
        C = (T/pi) * exp(T/kappa) * sqrt(theta^2/(kappa*sigma^2) + 1/kappa^2)

    the NIG density is:

        f(x) = C * exp(A*(x - c*T))
               * K_1(B * sqrt((x - c*T)^2 + T^2 * sigma^2/kappa))
               / sqrt((x - c*T)^2 + T^2 * sigma^2/kappa)

    Note: unlike the VG density (which uses K_v with variable order
    T/kappa - 1/2), the NIG density always uses K_1, the Bessel function
    of order 1.  This simplification comes from the Inverse Gaussian
    subordinator being a special case of the generalized inverse Gaussian.
    """
    A = theta / (sigma**2)
    B = np.sqrt(theta**2 + sigma**2 / kappa) / sigma**2
    C = (T / np.pi * np.exp(T / kappa)
         * np.sqrt(theta**2 / (kappa * sigma**2) + 1.0 / kappa**2))

    arg = np.sqrt((x - c * T) ** 2 + T**2 * sigma**2 / kappa)

    return C * np.exp(A * (x - c * T)) * scps.kv(1, B * arg) / arg


# ============================================================================
# Approximated Method of Moments (shared by VG and NIG)
# ============================================================================

def approximate_method_of_moments(data, T):
    """
    First-order (in theta) approximated method of moments.

    This method exploits the fact that theta is typically small in financial
    applications.  By dropping terms of order theta^2 and higher from the
    VG/NIG moment formulas, the system of four equations (mean, variance,
    skewness, kurtosis) decouples into four closed-form estimators.

    KEY INSIGHT: at first order in theta, the VG and NIG moment formulas
    are IDENTICAL:

        E[X_T]    = T * (c + theta)
        Var[X_T]  = T * sigma^2              (no theta^2 * kappa term)
        Skew[X_T] = (1/sqrt(T)) * 3*theta*kappa / sigma
        Kurt[X_T] = (1/T) * 3*kappa          (excess kurtosis)

    This means the SAME MoM formulas serve as initial guesses for BOTH
    the VG and NIG maximum likelihood estimations.

    Inverting gives:
        sigma = std(X) / sqrt(T)
        kappa = T * excess_kurtosis(X) / 3
        theta = sqrt(T) * skew(X) * sigma / (3 * kappa)
        c     = mean(X) / T - theta

    Interpretation:
        - kappa controls the KURTOSIS (fat-tailedness).
        - theta controls the SKEWNESS (asymmetry).
          Sign of theta = sign of observed skewness.
        - sigma sets the overall VOLATILITY scale.
        - c absorbs whatever mean is not explained by theta.

    Parameters
    ----------
    data : array_like
        Observed sample of the process at time T (i.e., X_T values).
    T : float
        Time horizon at which data was observed.

    Returns
    -------
    c_mm : float
        Estimated deterministic drift.
    theta_mm : float
        Estimated Brownian drift.
    sigma_mm : float
        Estimated Brownian volatility.
    kappa_mm : float
        Estimated subordinator variance.
    """
    sigma_mm = np.std(data) / np.sqrt(T)
    kappa_mm = T * ss.kurtosis(data) / 3        # excess kurtosis
    theta_mm = np.sqrt(T) * ss.skew(data) * sigma_mm / (3 * kappa_mm)
    c_mm = np.mean(data) / T - theta_mm

    return c_mm, theta_mm, sigma_mm, kappa_mm


# ============================================================================
# Maximum Likelihood Estimation -- VG
# ============================================================================

def vg_mle(data, T, verbose=True):
    """
    Two-stage VG parameter estimation: MoM warm start + MLE.

    Stage 1: Compute approximate method-of-moments estimates.
    Stage 2: Maximize log-likelihood using L-BFGS-B with:
        - MoM estimates as initial guess (warm start)
        - Bounds that enforce the correct sign of theta
          (matching observed skewness)
        - Positivity constraints on sigma and kappa

    The log-likelihood is:
        LL = sum_{i=1}^{N} log( VG_density(x_i; T, c, theta, sigma, kappa) )

    We minimize -LL via scipy.optimize.minimize.

    Parameters
    ----------
    data : array_like
        Observed sample X_T.
    T : float
        Time horizon.
    verbose : bool
        If True, print intermediate results.

    Returns
    -------
    c_mle : float
        MLE estimate of c.
    theta_mle : float
        MLE estimate of theta.
    sigma_mle : float
        MLE estimate of sigma.
    kappa_mle : float
        MLE estimate of kappa.
    result : scipy.optimize.OptimizeResult
        Full optimization result object.
    """
    # --- Stage 1: Method of Moments ---
    c_mm, theta_mm, sigma_mm, kappa_mm = approximate_method_of_moments(data, T)

    if verbose:
        print("  VG Method-of-Moments estimates:")
        print(f"    c     = {c_mm:.6f}")
        print(f"    theta = {theta_mm:.6f}")
        print(f"    sigma = {sigma_mm:.6f}")
        print(f"    kappa = {kappa_mm:.6f}")
        print(f"    c + theta = {c_mm + theta_mm:.6f}")
        print()

    # --- Stage 2: MLE ---
    def neg_log_likelihood(params, data, T):
        c, theta, sigma, kappa = params
        pdf_vals = VG_density(data, T, c, theta, sigma, kappa)
        # Guard against log(0) or log(negative)
        pdf_vals = np.maximum(pdf_vals, 1e-300)
        return -np.sum(np.log(pdf_vals))

    # Determine bounds based on observed skewness:
    # theta must have the same sign as the observed skewness
    observed_skew = ss.skew(data)
    if observed_skew < 0:
        theta_bounds = (-1.0, -1e-15)
    else:
        theta_bounds = (1e-15, 1.0)

    bounds = [
        (-1.0, 1.0),           # c: location drift
        theta_bounds,          # theta: sign matches skewness
        (1e-15, 2.0),         # sigma: positive
        (1e-15, None),        # kappa: positive
    ]

    result = minimize(
        neg_log_likelihood,
        x0=[c_mm, theta_mm, sigma_mm, kappa_mm],
        method="L-BFGS-B",
        args=(data, T),
        tol=1e-8,
        bounds=bounds,
    )

    c_mle, theta_mle, sigma_mle, kappa_mle = result.x

    if verbose:
        print(f"  VG MLE optimization: {result.message}")
        print(f"    Iterations: {result.nit}")
        print(f"  VG MLE estimates:")
        print(f"    c     = {c_mle:.6f}")
        print(f"    theta = {theta_mle:.6f}")
        print(f"    sigma = {sigma_mle:.6f}")
        print(f"    kappa = {kappa_mle:.6f}")

    return c_mle, theta_mle, sigma_mle, kappa_mle, result


# ============================================================================
# Maximum Likelihood Estimation -- NIG
# ============================================================================

def nig_mle(data, T, verbose=True):
    """
    Two-stage NIG parameter estimation: MoM warm start + MLE.

    This is the ONLY NIG parameter estimation implementation in the
    repository.  The key insight that makes the two-stage approach work
    is that at first order in theta, the VG and NIG moment formulas are
    IDENTICAL.  Therefore, the SAME approximate MoM formulas provide
    good initial guesses for the NIG MLE.

    The NIG log-likelihood is:
        LL = sum_{i=1}^{N} log( NIG_density(x_i; T, c, theta, sigma, kappa) )

    Parameters
    ----------
    data : array_like
        Observed sample X_T.
    T : float
        Time horizon.
    verbose : bool
        If True, print intermediate results.

    Returns
    -------
    c_mle : float
        MLE estimate of c.
    theta_mle : float
        MLE estimate of theta.
    sigma_mle : float
        MLE estimate of sigma.
    kappa_mle : float
        MLE estimate of kappa.
    result : scipy.optimize.OptimizeResult
        Full optimization result object.
    """
    # --- Stage 1: Method of Moments ---
    # Same formulas as VG, because first-order moments in theta are identical
    c_mm, theta_mm, sigma_mm, kappa_mm = approximate_method_of_moments(data, T)

    if verbose:
        print("  NIG Method-of-Moments estimates (same formulas as VG):")
        print(f"    c     = {c_mm:.6f}")
        print(f"    theta = {theta_mm:.6f}")
        print(f"    sigma = {sigma_mm:.6f}")
        print(f"    kappa = {kappa_mm:.6f}")
        print(f"    c + theta = {c_mm + theta_mm:.6f}")
        print()

    # --- Stage 2: MLE ---
    def neg_log_likelihood(params, data, T):
        c, theta, sigma, kappa = params
        pdf_vals = NIG_density(data, T, c, theta, sigma, kappa)
        pdf_vals = np.maximum(pdf_vals, 1e-300)
        return -np.sum(np.log(pdf_vals))

    observed_skew = ss.skew(data)
    if observed_skew < 0:
        theta_bounds = (-1.0, -1e-15)
    else:
        theta_bounds = (1e-15, 1.0)

    bounds = [
        (-1.0, 1.0),
        theta_bounds,
        (1e-15, 2.0),
        (1e-15, None),
    ]

    result = minimize(
        neg_log_likelihood,
        x0=[c_mm, theta_mm, sigma_mm, kappa_mm],
        method="L-BFGS-B",
        args=(data, T),
        tol=1e-8,
        bounds=bounds,
    )

    c_mle, theta_mle, sigma_mle, kappa_mle = result.x

    if verbose:
        print(f"  NIG MLE optimization: {result.message}")
        print(f"    Iterations: {result.nit}")
        print(f"  NIG MLE estimates:")
        print(f"    c     = {c_mle:.6f}")
        print(f"    theta = {theta_mle:.6f}")
        print(f"    sigma = {sigma_mle:.6f}")
        print(f"    kappa = {kappa_mle:.6f}")

    return c_mle, theta_mle, sigma_mle, kappa_mle, result


# ============================================================================
# Inverse Gaussian First-Passage-Time Simulation
# ============================================================================

def simulate_ig_first_passage(delta, gamma, T_max=20, paths=40000,
                              steps=10000, seed=42):
    """
    Simulate the Inverse Gaussian distribution as a first-passage-time.

    This provides PHYSICAL INTUITION for why the IG distribution appears as
    the NIG subordinator.  The IG(mu, lambda) distribution is the distribution
    of the first time a drifted Brownian motion:

        dZ_s = gamma * ds + dW_s

    crosses a linearly-growing barrier delta * t.  The IG process T_t at
    time t equals:

        T_t = inf{ s > 0 : Z_s = delta * t }

    which is distributed as IG(delta*t / gamma, delta^2 * t^2).

    This connects the abstract IG subordinator to a concrete physical picture:
    the random "operational time" in the NIG model is the first time a noisy
    signal (Brownian motion with drift) reaches a linearly-growing threshold.

    Parameters
    ----------
    delta : float
        Barrier slope (the barrier at time t is delta * t).
    gamma : float
        Drift of the Brownian motion.
    T_max : float
        Maximum simulation time.
    paths : int
        Number of Monte Carlo paths.
    steps : int
        Number of time steps.
    seed : int
        Random seed.

    Returns
    -------
    first_passage_times : ndarray
        Array of first passage times (one per path).
    theoretical_mean : float
        Theoretical mean = delta / gamma.
    theoretical_var : float
        Theoretical variance = delta / gamma^3.
    lam : float
        IG shape parameter = delta^2.
    mu_scaled : float
        Scaled mean for scipy.stats.invgauss = (delta/gamma) / delta^2.
    """
    np.random.seed(seed)

    T_vec, dt = np.linspace(0, T_max, steps, retstep=True)
    X0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(
        loc=gamma * dt, scale=np.sqrt(dt), size=(paths, steps - 1)
    )

    Z = np.concatenate((X0, increments), axis=1).cumsum(axis=1)

    # First passage time: first index where Z > delta (the barrier)
    first_passage_times = np.argmax(Z > delta, axis=1) * dt

    theoretical_mean = delta / gamma
    theoretical_var = delta / gamma**3
    lam = delta**2
    mu_scaled = (delta / gamma) / lam  # scipy's mu parameter

    return first_passage_times, theoretical_mean, theoretical_var, lam, mu_scaled


# ============================================================================
# Simulation helpers
# ============================================================================

def simulate_vg(T, N, theta, sigma, kappa, c=0.0, seed=42):
    """
    Simulate VG process via Gamma subordination.

        Y_T = c * T + theta * G + sigma * sqrt(G) * Z

    where G ~ Gamma(T/kappa, kappa), Z ~ N(0,1).

    Parameters
    ----------
    T : float
        Time horizon.
    N : int
        Number of samples.
    theta, sigma, kappa : float
        VG model parameters.
    c : float
        Deterministic drift.
    seed : int
        Random seed.

    Returns
    -------
    ndarray
        Array of N samples from the VG distribution at time T.
    """
    np.random.seed(seed)
    G = ss.gamma(T / kappa, scale=kappa).rvs(N)
    Z = ss.norm.rvs(0, 1, N)
    return c * T + theta * G + sigma * np.sqrt(G) * Z


def simulate_nig(T, N, theta, sigma, kappa, c=0.0, seed=42):
    """
    Simulate NIG process via Inverse Gaussian subordination.

        Y_T = c * T + theta * IG + sigma * sqrt(IG) * Z

    where IG ~ InverseGaussian(mu=T, lambda=T^2/kappa), Z ~ N(0,1).

    Parameters
    ----------
    T : float
        Time horizon.
    N : int
        Number of samples.
    theta, sigma, kappa : float
        NIG model parameters.
    c : float
        Deterministic drift.
    seed : int
        Random seed.

    Returns
    -------
    ndarray
        Array of N samples from the NIG distribution at time T.
    """
    np.random.seed(seed)
    lam = T**2 / kappa
    mu_s = T / lam  # scipy's mu parameter
    IG = ss.invgauss.rvs(mu=mu_s, scale=lam, size=N)
    Z = ss.norm.rvs(0, 1, N)
    return c * T + theta * IG + sigma * np.sqrt(IG) * Z


# ============================================================================
# Main demonstration
# ============================================================================

if __name__ == "__main__":

    # ================================================================
    # True parameters for both VG and NIG
    # ================================================================
    T_true = 2.0              # time horizon
    N_samples = 1_000_000     # number of simulated samples
    theta_true = -0.1         # BM drift (negative -> left skew)
    sigma_true = 0.2          # BM volatility
    kappa_true = 0.5          # subordinator variance
    c_true = 0.0              # deterministic drift

    print("=" * 70)
    print("  Levy Process Parameter Estimation")
    print("  cantaro86: '1.5 SDE - Levy processes', cells 36-62")
    print("=" * 70)
    print()
    print(f"  True parameters: c={c_true}, theta={theta_true}, "
          f"sigma={sigma_true}, kappa={kappa_true}")
    print(f"  Time horizon T={T_true}, samples N={N_samples:,}")
    print()

    # ================================================================
    # PART 1: VG Estimation
    # ================================================================
    print("-" * 70)
    print("  PART 1: Variance Gamma (VG) Parameter Estimation")
    print("-" * 70)
    print()

    X_vg = simulate_vg(T_true, N_samples, theta_true, sigma_true,
                        kappa_true, c=c_true, seed=42)

    print(f"  Sample statistics of VG data:")
    print(f"    Mean:              {np.mean(X_vg):.6f}  "
          f"(theoretical: {(c_true + theta_true) * T_true:.6f})")
    print(f"    Std deviation:     {np.std(X_vg):.6f}")
    print(f"    Skewness:          {ss.skew(X_vg):.6f}")
    print(f"    Excess kurtosis:   {ss.kurtosis(X_vg):.6f}")
    print()

    c_vg, theta_vg, sigma_vg, kappa_vg, res_vg = vg_mle(X_vg, T_true)
    print()

    print("  VG estimation summary:")
    print(f"    {'Param':<8} {'True':>10} {'MoM':>10} {'MLE':>10}")
    print(f"    {'-----':<8} {'----':>10} {'---':>10} {'---':>10}")
    c_mm, theta_mm, sigma_mm, kappa_mm = approximate_method_of_moments(
        X_vg, T_true
    )
    print(f"    {'c':<8} {c_true:>10.4f} {c_mm:>10.4f} {c_vg:>10.4f}")
    print(f"    {'theta':<8} {theta_true:>10.4f} {theta_mm:>10.4f} "
          f"{theta_vg:>10.4f}")
    print(f"    {'sigma':<8} {sigma_true:>10.4f} {sigma_mm:>10.4f} "
          f"{sigma_vg:>10.4f}")
    print(f"    {'kappa':<8} {kappa_true:>10.4f} {kappa_mm:>10.4f} "
          f"{kappa_vg:>10.4f}")
    print()

    # ================================================================
    # PART 2: NIG Estimation
    # ================================================================
    print("-" * 70)
    print("  PART 2: Normal Inverse Gaussian (NIG) Parameter Estimation")
    print("-" * 70)
    print()

    X_nig = simulate_nig(T_true, N_samples, theta_true, sigma_true,
                          kappa_true, c=c_true, seed=42)

    print(f"  Sample statistics of NIG data:")
    print(f"    Mean:              {np.mean(X_nig):.6f}  "
          f"(theoretical: {(c_true + theta_true) * T_true:.6f})")
    print(f"    Std deviation:     {np.std(X_nig):.6f}")
    print(f"    Skewness:          {ss.skew(X_nig):.6f}")
    print(f"    Excess kurtosis:   {ss.kurtosis(X_nig):.6f}")
    print()

    c_nig, theta_nig, sigma_nig, kappa_nig, res_nig = nig_mle(X_nig, T_true)
    print()

    print("  NIG estimation summary:")
    print(f"    {'Param':<8} {'True':>10} {'MoM':>10} {'MLE':>10}")
    print(f"    {'-----':<8} {'----':>10} {'---':>10} {'---':>10}")
    c_mm2, theta_mm2, sigma_mm2, kappa_mm2 = approximate_method_of_moments(
        X_nig, T_true
    )
    print(f"    {'c':<8} {c_true:>10.4f} {c_mm2:>10.4f} {c_nig:>10.4f}")
    print(f"    {'theta':<8} {theta_true:>10.4f} {theta_mm2:>10.4f} "
          f"{theta_nig:>10.4f}")
    print(f"    {'sigma':<8} {sigma_true:>10.4f} {sigma_mm2:>10.4f} "
          f"{sigma_nig:>10.4f}")
    print(f"    {'kappa':<8} {kappa_true:>10.4f} {kappa_mm2:>10.4f} "
          f"{kappa_nig:>10.4f}")
    print()

    # ================================================================
    # PART 3: Inverse Gaussian First-Passage-Time Simulation
    # ================================================================
    print("-" * 70)
    print("  PART 3: Inverse Gaussian as First-Passage-Time Distribution")
    print("-" * 70)
    print()
    print("  Physical picture: the IG subordinator in the NIG model")
    print("  represents the first time a drifted Brownian motion")
    print("  crosses a linearly-growing barrier.")
    print()

    t_fpt = 2          # time parameter for the barrier
    delta_fpt = 3 * t_fpt   # barrier = delta * t
    gamma_fpt = 2       # drift of the Brownian motion

    fpt, th_mean, th_var, lam_ig, mu_ig = simulate_ig_first_passage(
        delta=delta_fpt, gamma=gamma_fpt, T_max=20,
        paths=40000, steps=10000, seed=42
    )

    print(f"  Barrier: delta = {delta_fpt}, BM drift: gamma = {gamma_fpt}")
    print(f"  Theoretical mean: {th_mean:.4f}")
    print(f"  Theoretical variance: {th_var:.4f}")
    print(f"  Simulated mean: {fpt.mean():.4f}")
    print(f"  Simulated variance: {fpt.var():.4f}")
    print()

    # ================================================================
    # PART 4: Plots
    # ================================================================
    print("-" * 70)
    print("  PART 4: Generating plots...")
    print("-" * 70)
    print()

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # --- Plot (a): VG histogram vs estimated density ---
    ax = axes[0, 0]
    x_grid = np.linspace(X_vg.min(), X_vg.max(), 500)
    ax.hist(X_vg, density=True, bins=200, facecolor="LightBlue", alpha=0.7,
            label="Simulated VG data")
    ax.plot(x_grid,
            VG_density(x_grid, T_true, c_true, theta_true, sigma_true,
                       kappa_true),
            "r-", linewidth=2, label="True VG density")
    ax.plot(x_grid,
            VG_density(x_grid, T_true, c_vg, theta_vg, sigma_vg, kappa_vg),
            "g--", linewidth=2, label="MLE-estimated VG density")
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("Density", fontsize=11)
    ax.set_title("VG: Histogram vs True and Estimated Densities", fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # --- Plot (b): NIG histogram vs estimated density ---
    ax = axes[0, 1]
    x_grid2 = np.linspace(X_nig.min(), X_nig.max(), 500)
    ax.hist(X_nig, density=True, bins=200, facecolor="LightBlue", alpha=0.7,
            label="Simulated NIG data")
    ax.plot(x_grid2,
            NIG_density(x_grid2, T_true, c_true, theta_true, sigma_true,
                        kappa_true),
            "r-", linewidth=2, label="True NIG density")
    ax.plot(x_grid2,
            NIG_density(x_grid2, T_true, c_nig, theta_nig, sigma_nig,
                        kappa_nig),
            "g--", linewidth=2, label="MLE-estimated NIG density")
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("Density", fontsize=11)
    ax.set_title("NIG: Histogram vs True and Estimated Densities", fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # --- Plot (c): VG vs NIG comparison (log scale) ---
    ax = axes[1, 0]
    # Use a common grid for comparison
    x_common = np.linspace(
        max(X_vg.min(), X_nig.min()),
        min(X_vg.max(), X_nig.max()),
        500,
    )
    vg_dens = VG_density(x_common, T_true, c_true, theta_true, sigma_true,
                         kappa_true)
    nig_dens = NIG_density(x_common, T_true, c_true, theta_true, sigma_true,
                           kappa_true)
    # Normal density for comparison
    normal_dens = ss.norm.pdf(
        x_common,
        loc=(c_true + theta_true) * T_true,
        scale=np.sqrt((sigma_true**2 + theta_true**2 * kappa_true) * T_true),
    )

    ax.semilogy(x_common, vg_dens, "b-", linewidth=2, label="VG (true)")
    ax.semilogy(x_common, nig_dens, "r-", linewidth=2, label="NIG (true)")
    ax.semilogy(x_common, normal_dens, "k--", linewidth=1.5,
                label="Normal (matched moments)")
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("Density (log scale)", fontsize=11)
    ax.set_title(
        "VG vs NIG vs Normal (log scale)\n"
        r"Same $\theta, \sigma, \kappa$ -- different tail behavior",
        fontsize=12,
    )
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=1e-6)

    # --- Plot (d): Inverse Gaussian first-passage-time ---
    ax = axes[1, 1]
    x_ig = np.linspace(0.01, 10, 10000)
    ax.hist(fpt[fpt > 0], density=True, bins=100, facecolor="LightBlue",
            alpha=0.7, label="Simulated first-passage times")
    ax.plot(x_ig,
            ss.invgauss.pdf(x_ig, mu=mu_ig, scale=lam_ig),
            "r-", linewidth=2, label="Theoretical IG density")
    ax.set_xlabel("First passage time", fontsize=11)
    ax.set_ylabel("Density", fontsize=11)
    ax.set_title(
        "Inverse Gaussian as First-Passage-Time\n"
        rf"$\delta$={delta_fpt}, $\gamma$={gamma_fpt}: "
        rf"IG($\mu$={th_mean:.1f}, $\lambda$={lam_ig:.0f})",
        fontsize=12,
    )
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)

    plt.tight_layout()
    plt.savefig("levy_estimation_results.png", dpi=150)
    plt.show()
    print("  Plot saved to levy_estimation_results.png")
    print()
    print("=" * 70)
    print("  Done.")
    print("=" * 70)
