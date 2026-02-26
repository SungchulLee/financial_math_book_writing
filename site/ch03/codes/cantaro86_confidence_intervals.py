#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_confidence_intervals.py

Confidence interval construction and empirical failure-rate demonstration
for normally distributed data, with application to Brownian motion terminal
values.

Based on cells 7-12 of "1.2 SDE simulations and statistics" from cantaro86's
"Financial-Models-Numerical-Methods"
(https://github.com/cantaro86/Financial-Models-Numerical-Methods).
Adapted as a self-contained educational module -- no local imports required.

Topics covered
--------------
1. Z-confidence interval for the mean (sigma known).
2. t-confidence interval for the mean (sigma unknown).
3. Chi-squared confidence interval for variance / standard deviation.
4. CI failure-rate experiment: repeat 95% CI construction 100 times on
   independent Brownian motion samples and show that the true mean falls
   outside the interval approximately 5% of the time.

Theory (brief recap)
--------------------
Let X_1, ..., X_n be i.i.d. Normal(mu, sigma^2).

* Z-CI (sigma known):
      x_bar +/- z_{alpha/2} * sigma / sqrt(n)
  where z_{alpha/2} = norm.ppf(1 - alpha/2).

* t-CI (sigma unknown):
      x_bar +/- t_{alpha/2, n-1} * s / sqrt(n)
  where s is the sample standard deviation (ddof=1) and t_{alpha/2, n-1}
  comes from the Student-t distribution with n-1 degrees of freedom.

* Chi-squared CI for sigma^2:
      [(n-1)*s^2 / chi2_{alpha/2}, (n-1)*s^2 / chi2_{1-alpha/2}]
  where chi2 quantiles use n-1 degrees of freedom.
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 1. Z-confidence interval for the mean (sigma known)
# ---------------------------------------------------------------------------

def z_confidence_interval(x, sigma, alpha=0.05):
    """
    Compute the Z-confidence interval for the population mean, assuming
    the population standard deviation sigma is known.

    Parameters
    ----------
    x : array_like
        Sample observations.
    sigma : float
        Known population standard deviation (> 0).
    alpha : float
        Significance level; the confidence level is (1 - alpha).

    Returns
    -------
    low : float
        Lower bound of the confidence interval.
    high : float
        Upper bound of the confidence interval.
    """
    x = np.asarray(x)
    n = len(x)
    x_bar = x.mean()
    z = ss.norm.ppf(1 - alpha / 2)
    margin = z * sigma / np.sqrt(n)
    return x_bar - margin, x_bar + margin


# ---------------------------------------------------------------------------
# 2. t-confidence interval for the mean (sigma unknown)
# ---------------------------------------------------------------------------

def t_confidence_interval(x, alpha=0.05):
    """
    Compute the t-confidence interval for the population mean when the
    population standard deviation is unknown.

    Uses the Student-t distribution with n-1 degrees of freedom and the
    sample standard error.

    Parameters
    ----------
    x : array_like
        Sample observations.
    alpha : float
        Significance level; the confidence level is (1 - alpha).

    Returns
    -------
    low : float
        Lower bound of the confidence interval.
    high : float
        Upper bound of the confidence interval.
    """
    x = np.asarray(x)
    n = len(x)
    low, high = ss.t.interval(1 - alpha, df=n - 1, loc=x.mean(), scale=ss.sem(x))
    return low, high


# ---------------------------------------------------------------------------
# 3. Chi-squared confidence interval for variance / standard deviation
# ---------------------------------------------------------------------------

def chi2_confidence_interval_variance(x, alpha=0.05):
    """
    Compute the chi-squared confidence interval for the population variance.

    Parameters
    ----------
    x : array_like
        Sample observations (assumed normally distributed).
    alpha : float
        Significance level; the confidence level is (1 - alpha).

    Returns
    -------
    var_low : float
        Lower bound of the variance CI.
    var_high : float
        Upper bound of the variance CI.
    """
    x = np.asarray(x)
    n = len(x)
    s2 = x.var(ddof=1)  # unbiased sample variance
    df = n - 1

    # Chi-squared quantiles (note the "flipped" order):
    #   chi2_{alpha/2}   is the UPPER quantile  (larger value)
    #   chi2_{1-alpha/2} is the LOWER quantile  (smaller value)
    chi2_upper = ss.chi2.ppf(1 - alpha / 2, df=df)
    chi2_lower = ss.chi2.ppf(alpha / 2, df=df)

    var_low = df * s2 / chi2_upper
    var_high = df * s2 / chi2_lower
    return var_low, var_high


def chi2_confidence_interval_std(x, alpha=0.05):
    """
    Compute the chi-squared confidence interval for the population
    standard deviation (simply the square root of the variance CI).

    Parameters
    ----------
    x : array_like
        Sample observations (assumed normally distributed).
    alpha : float
        Significance level.

    Returns
    -------
    std_low : float
        Lower bound of the standard deviation CI.
    std_high : float
        Upper bound of the standard deviation CI.
    """
    var_low, var_high = chi2_confidence_interval_variance(x, alpha)
    return np.sqrt(var_low), np.sqrt(var_high)


# ---------------------------------------------------------------------------
# 4. CI failure-rate experiment
# ---------------------------------------------------------------------------

def ci_failure_experiment(mu_true, sigma_true, n_samples, n_experiments=100,
                          alpha=0.05, seed_start=0):
    """
    Repeat the construction of a (1-alpha) t-confidence interval for the
    mean across many independent experiments and record which ones fail
    to contain the true population mean.

    Each experiment draws n_samples observations from N(mu_true, sigma_true^2),
    builds a t-CI, and checks whether mu_true is inside.

    Parameters
    ----------
    mu_true : float
        True population mean.
    sigma_true : float
        True population standard deviation (used only for data generation,
        NOT passed to the CI -- the t-CI estimates sigma from the sample).
    n_samples : int
        Number of observations per experiment.
    n_experiments : int
        Number of independent repetitions.
    alpha : float
        Significance level.
    seed_start : int
        The experiment with index k uses np.random.seed(seed_start + k).

    Returns
    -------
    results : list of dict
        One entry per experiment with keys:
        'seed', 'low', 'high', 'mean', 'contains_true'.
    n_failures : int
        Number of experiments where the CI did NOT contain mu_true.
    """
    results = []
    n_failures = 0

    for k in range(n_experiments):
        np.random.seed(seed=seed_start + k)
        sample = ss.norm.rvs(loc=mu_true, scale=sigma_true, size=n_samples)
        low, high = t_confidence_interval(sample, alpha=alpha)
        contains = (low <= mu_true <= high)
        if not contains:
            n_failures += 1
        results.append({
            "seed": seed_start + k,
            "low": low,
            "high": high,
            "mean": sample.mean(),
            "contains_true": contains,
        })

    return results, n_failures


def plot_ci_failure_experiment(results, mu_true, alpha=0.05, save_path=None):
    """
    Visualise the CI failure experiment: each horizontal line segment is one
    confidence interval, coloured green if it contains the true mean and
    red if it does not.

    Parameters
    ----------
    results : list of dict
        Output of ci_failure_experiment().
    mu_true : float
        True population mean (drawn as a vertical line).
    alpha : float
        Significance level (used only for the title).
    save_path : str or None
        If given, save the figure to this path.
    """
    n_exp = len(results)
    fig, ax = plt.subplots(figsize=(10, max(6, n_exp * 0.08)))

    for i, r in enumerate(results):
        colour = "green" if r["contains_true"] else "red"
        lw = 1.0 if r["contains_true"] else 1.8
        ax.plot([r["low"], r["high"]], [i, i], color=colour, linewidth=lw)
        ax.plot(r["mean"], i, marker="o", markersize=2.5, color=colour)

    ax.axvline(mu_true, color="black", linewidth=1.5, linestyle="--",
               label=f"True mean = {mu_true}")

    n_failures = sum(1 for r in results if not r["contains_true"])
    failure_pct = 100 * n_failures / n_exp

    ax.set_xlabel("Value")
    ax.set_ylabel("Experiment index")
    ax.set_title(
        f"{100*(1-alpha):.0f}% t-Confidence Intervals  "
        f"({n_exp} experiments, {n_failures} failures = {failure_pct:.1f}%)"
    )
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3, axis="x")

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"  Figure saved: {save_path}")
    plt.show()
    plt.close()


# ---------------------------------------------------------------------------
# Main demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    np.random.seed(seed=42)

    # ==================================================================
    # Step 1: Simulate Brownian motion terminal values
    # ==================================================================
    print("=" * 65)
    print("Brownian Motion Simulation")
    print("=" * 65)

    paths = 4000   # number of paths
    steps = 1000   # number of time steps
    mu = 0.1       # drift
    sig = 0.2      # diffusion coefficient (volatility)
    T = 100

    T_vec, dt = np.linspace(0, T, steps, retstep=True)

    X0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(loc=mu * dt, scale=np.sqrt(dt) * sig,
                             size=(paths, steps - 1))
    X = np.concatenate((X0, increments), axis=1).cumsum(axis=1)
    X_end = X[:, -1]

    # Theoretical values: E[X_T] = mu*T = 10,  Std[X_T] = sig*sqrt(T) = 2
    print(f"  Parameters: mu={mu}, sigma={sig}, T={T}")
    print(f"  Theoretical mean  : {mu * T:.4f}")
    print(f"  Theoretical stdev : {sig * np.sqrt(T):.4f}")
    print(f"  Sample mean       : {X_end.mean():.4f}")
    print(f"  Sample stdev      : {X_end.std(ddof=1):.4f}")
    print()

    # ==================================================================
    # Step 2: Z-confidence interval (sigma known)
    # ==================================================================
    print("=" * 65)
    print("1. Z-Confidence Interval for the Mean (sigma known)")
    print("=" * 65)

    # We pretend to know the true sigma = sig * sqrt(T) = 2
    sigma_known = sig * np.sqrt(T)
    z_low, z_high = z_confidence_interval(X_end, sigma=sigma_known, alpha=0.05)
    print(f"  Known sigma       : {sigma_known:.4f}")
    print(f"  Sample mean       : {X_end.mean():.6f}")
    print(f"  95% Z-CI          : ({z_low:.6f}, {z_high:.6f})")
    print(f"  True mean {mu*T:.1f} in CI? {z_low <= mu*T <= z_high}")
    print()

    # ==================================================================
    # Step 3: t-confidence interval (sigma unknown)
    # ==================================================================
    print("=" * 65)
    print("2. t-Confidence Interval for the Mean (sigma unknown)")
    print("=" * 65)

    t_low, t_high = t_confidence_interval(X_end, alpha=0.05)
    print(f"  Sample mean       : {X_end.mean():.6f}")
    print(f"  95% t-CI          : ({t_low:.6f}, {t_high:.6f})")
    print(f"  True mean {mu*T:.1f} in CI? {t_low <= mu*T <= t_high}")
    print()

    # ==================================================================
    # Step 4: Chi-squared CI for variance / standard deviation
    # ==================================================================
    print("=" * 65)
    print("3. Chi-squared Confidence Interval for Variance / Std Dev")
    print("=" * 65)

    var_low, var_high = chi2_confidence_interval_variance(X_end, alpha=0.05)
    std_low, std_high = chi2_confidence_interval_std(X_end, alpha=0.05)

    true_variance = (sig * np.sqrt(T)) ** 2  # sig^2 * T = 4
    true_std = sig * np.sqrt(T)              # 2.0

    print(f"  Sample variance   : {X_end.var(ddof=1):.6f}")
    print(f"  95% CI (variance) : ({var_low:.6f}, {var_high:.6f})")
    print(f"  True variance {true_variance:.1f} in CI? "
          f"{var_low <= true_variance <= var_high}")
    print()
    print(f"  Sample std dev    : {X_end.std(ddof=1):.6f}")
    print(f"  95% CI (std dev)  : ({std_low:.6f}, {std_high:.6f})")
    print(f"  True std dev {true_std:.1f} in CI? "
          f"{std_low <= true_std <= std_high}")
    print()

    # ==================================================================
    # Step 5: CI failure-rate experiment (the key pedagogical demo)
    # ==================================================================
    print("=" * 65)
    print("4. CI Failure-Rate Experiment")
    print("=" * 65)
    print()
    print("  We draw 4000 terminal Brownian motion values 100 times")
    print("  (each with a different random seed) and build a 95% t-CI")
    print("  for the mean each time.  We expect ~5% of these CIs to")
    print("  fail to contain the true mean mu*T = 10.")
    print()

    # Each experiment generates X_T ~ N(mu*T, sig^2*T) directly
    # (equivalent to Brownian motion terminal value).
    mu_true = mu * T      # = 10
    sigma_true = sig * np.sqrt(T)  # = 2

    results, n_failures = ci_failure_experiment(
        mu_true=mu_true,
        sigma_true=sigma_true,
        n_samples=paths,
        n_experiments=100,
        alpha=0.05,
        seed_start=0,
    )

    # Print failures
    print(f"  Results: {n_failures} failures out of 100 experiments")
    print(f"  Failure rate: {n_failures}%  (expected ~5%)")
    print()
    for r in results:
        if not r["contains_true"]:
            print(f"    seed {r['seed']:>3d}:  {mu_true} is NOT in "
                  f"({r['low']:.4f}, {r['high']:.4f})")

    print()
    print("  Plotting all 100 confidence intervals...")

    plot_ci_failure_experiment(
        results,
        mu_true=mu_true,
        alpha=0.05,
        save_path="/tmp/cantaro86_confidence_intervals.png",
    )

    # ==================================================================
    # Step 6: Brownian paths + terminal histogram (context figure)
    # ==================================================================
    print()
    print("  Plotting Brownian paths and terminal distribution...")

    np.random.seed(seed=42)
    X0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(loc=mu * dt, scale=np.sqrt(dt) * sig,
                             size=(paths, steps - 1))
    X = np.concatenate((X0, increments), axis=1).cumsum(axis=1)
    X_end = X[:, -1]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Brownian paths (plot a subset to keep the figure readable)
    n_plot = min(50, paths)
    for p in range(n_plot):
        axes[0].plot(T_vec, X[p, :], linewidth=0.4, alpha=0.6)
    axes[0].set_title(f"Brownian Motion Paths ({n_plot} of {paths})")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("X(t)")
    axes[0].grid(True, alpha=0.3)

    # Right: Histogram of terminal values vs theoretical normal
    axes[1].hist(X_end, bins=60, density=True, facecolor="LightBlue",
                 edgecolor="gray", alpha=0.8, label="Simulated X_T")
    x_grid = np.linspace(X_end.min(), X_end.max(), 200)
    axes[1].plot(x_grid, ss.norm.pdf(x_grid, loc=mu * T, scale=sig * np.sqrt(T)),
                 "r-", linewidth=2, label=f"N({mu*T}, {sig**2*T})")

    # Mark the 95% t-CI on the histogram
    t_lo, t_hi = t_confidence_interval(X_end, alpha=0.05)
    axes[1].axvline(t_lo, color="green", linestyle="--", linewidth=1.2,
                    label=f"95% t-CI: ({t_lo:.2f}, {t_hi:.2f})")
    axes[1].axvline(t_hi, color="green", linestyle="--", linewidth=1.2)
    axes[1].axvline(mu * T, color="black", linestyle="-", linewidth=1.5,
                    label=f"True mean = {mu*T}")

    axes[1].set_title("Terminal Distribution X_T with 95% CI for Mean")
    axes[1].set_xlabel("X_T")
    axes[1].set_ylabel("Density")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_confidence_intervals_paths.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_confidence_intervals_paths.png")
    plt.close()

    # ==================================================================
    # Summary
    # ==================================================================
    print()
    print("=" * 65)
    print("Summary")
    print("=" * 65)
    print(f"  Brownian motion: mu={mu}, sigma={sig}, T={T}, paths={paths}")
    print(f"  True mean  = mu*T   = {mu*T}")
    print(f"  True stdev = sig*sqrt(T) = {sig*np.sqrt(T):.4f}")
    print()
    print(f"  95% Z-CI (sigma known)    : ({z_low:.4f}, {z_high:.4f})")
    print(f"  95% t-CI (sigma unknown)  : ({t_lo:.4f}, {t_hi:.4f})")
    print(f"  95% chi2-CI (std dev)     : ({std_low:.4f}, {std_high:.4f})")
    print()
    print(f"  CI failure experiment: {n_failures}/100 failures "
          f"({n_failures}%, expected ~5%)")
    print()
    print("Done.")
