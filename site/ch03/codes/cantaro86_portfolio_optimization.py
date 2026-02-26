#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_portfolio_optimization.py
====================================
Mean-Variance Portfolio Optimization with Sharpe Ratio Maximization.

Based on portfolio_optimization.py from:
    cantaro86 - Financial-Models-Numerical-Methods
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

This module implements the classical Markowitz mean-variance optimization
framework with the following extensions:
    - Sharpe ratio maximization (tangency portfolio)
    - No short-selling constraints (long-only)
    - Maximum weight bounds
    - Efficient frontier computation
    - Capital Allocation Line (CAL) with risk-free asset

Theory:
    Given N risky assets with:
        MU  = vector of expected returns  (N x 1)
        COV = covariance matrix           (N x N)
        Rf  = risk-free rate

    The tangency portfolio maximises:
        Sharpe Ratio = (MU' w - Rf) / sqrt(w' COV w)

    subject to:
        sum(w) = 1       (fully invested)
        0 <= w_i <= w_max (no shorting, max weight constraint)

    The Capital Allocation Line (CAL) connects the risk-free asset
    to the tangency portfolio:
        E[R_p] = Rf + SR * sigma_p

    where SR is the Sharpe ratio of the tangency portfolio.

License: MIT (see original repository)
"""

import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint


# ============================================================================
# Optimal Weights -- Sharpe Ratio Maximization
# ============================================================================

def optimal_weights(MU, COV, Rf=0.0, w_max=1.0, desired_mean=None, desired_std=None):
    """
    Compute the optimal portfolio weights by maximising the Sharpe ratio.

    Parameters
    ----------
    MU : ndarray, shape (N,)
        Vector of expected (mean) returns for each asset.
    COV : ndarray, shape (N, N)
        Covariance matrix of asset returns.
    Rf : float, default 0.0
        Risk-free rate.  If 0, only the tangency portfolio is computed
        (no CAL / desired_mean / desired_std).
    w_max : float, default 1.0
        Maximum weight for any single asset (1.0 = no constraint beyond full investment).
    desired_mean : float or None
        If provided, find the portfolio on the CAL with this expected return.
        (Requires Rf > 0.)
    desired_std : float or None
        If provided, find the portfolio on the CAL with this standard deviation.
        (Requires Rf > 0.)

    Returns
    -------
    result : dict
        Dictionary containing:
            "Sharpe Ratio" : float
            "stock weights" : ndarray
            "stock portfolio" : {"std": float, "mean": float}
        If desired_mean or desired_std is specified:
            "Bond + Stock weights" : {"Bond": float, "Stock": float}
            "Total portfolio" : {"std": float, "mean": float}

    Notes
    -----
    The optimization uses scipy's trust-constr method with:
        - Bound constraints: 0 <= w_i <= w_max (no short selling)
        - Linear constraint: sum(w_i) = 1 (fully invested in stocks)

    When a risk-free asset is available, the total portfolio is a
    combination of the risk-free asset and the tangency portfolio:
        w_stock = fraction in the tangency portfolio
        w_bond  = 1 - w_stock  (in the risk-free asset)

    If w_stock > 1, the investor borrows at the risk-free rate (leveraged).

    Reference: cantaro86/Financial-Models-Numerical-Methods, portfolio_optimization.py
    """
    # Input validation
    if (desired_mean is not None) and (desired_std is not None):
        raise ValueError("Only one of desired_mean or desired_std can be specified, not both")
    if ((desired_mean is not None) or (desired_std is not None)) and Rf == 0:
        raise ValueError("Rf must be nonzero to compute points on the efficient frontier")

    N = len(MU)

    # Constraints: weights sum to 1, each weight in [0, w_max]
    bounds = Bounds(0, w_max)
    linear_constraint = LinearConstraint(np.ones(N, dtype=int), 1, 1)

    # Initial guess: equal weights
    x0 = np.ones(N) / N

    # Objective: negative Sharpe ratio (minimise to maximise SR)
    def neg_sharpe(w):
        port_return = MU @ w - Rf
        port_vol = np.sqrt(w.T @ COV @ w)
        return -port_return / port_vol

    # Optimise
    res = minimize(
        neg_sharpe,
        x0=x0,
        method="trust-constr",
        constraints=linear_constraint,
        bounds=bounds,
    )

    if not res.success:
        print("WARNING: Optimization may not have converged -- " + res.message)

    w_tangency = res.x
    std_tangency = np.sqrt(w_tangency @ COV @ w_tangency)
    mean_tangency = MU @ w_tangency
    sharpe_ratio = -neg_sharpe(w_tangency)

    result = {
        "Sharpe Ratio": sharpe_ratio,
        "stock weights": w_tangency.round(4),
        "stock portfolio": {
            "std": round(float(std_tangency), 6),
            "mean": round(float(mean_tangency), 6),
        },
    }

    # If only tangency portfolio is requested
    if (desired_mean is None) and (desired_std is None):
        return result

    # Compute allocation along the Capital Allocation Line
    if (desired_mean is None) and (desired_std is not None):
        w_stock = desired_std / std_tangency
        if desired_std > std_tangency:
            print("  NOTE: desired_std > tangency std ==> leveraged position (short bond)")
        tot_mean = Rf + w_stock * (mean_tangency - Rf)
        return {
            **result,
            "Bond + Stock weights": {
                "Bond": round(float(1 - w_stock), 4),
                "Stock": round(float(w_stock), 4),
            },
            "Total portfolio": {"std": desired_std, "mean": round(float(tot_mean), 6)},
        }

    if (desired_mean is not None) and (desired_std is None):
        w_stock = (desired_mean - Rf) / (mean_tangency - Rf)
        if desired_mean > mean_tangency:
            print("  NOTE: desired_mean > tangency mean ==> leveraged position (short bond)")
        tot_std = w_stock * std_tangency
        return {
            **result,
            "Bond + Stock weights": {
                "Bond": round(float(1 - w_stock), 4),
                "Stock": round(float(w_stock), 4),
            },
            "Total portfolio": {"std": round(float(tot_std), 6), "mean": desired_mean},
        }


# ============================================================================
# Efficient Frontier Computation
# ============================================================================

def compute_efficient_frontier(MU, COV, Rf=0.0, w_max=1.0, n_points=100):
    """
    Compute the efficient frontier by solving minimum-variance portfolios
    for a range of target returns.

    Parameters
    ----------
    MU : ndarray, shape (N,)
        Vector of expected returns.
    COV : ndarray, shape (N, N)
        Covariance matrix.
    Rf : float
        Risk-free rate (for the CAL).
    w_max : float
        Maximum weight per asset.
    n_points : int
        Number of points on the frontier.

    Returns
    -------
    frontier_std : ndarray
        Standard deviations along the frontier.
    frontier_mean : ndarray
        Expected returns along the frontier.
    """
    N = len(MU)
    bounds = Bounds(0, w_max)
    linear_constraint = LinearConstraint(np.ones(N, dtype=int), 1, 1)

    # Range of target returns
    min_ret = MU.min()
    max_ret = MU.max()
    target_returns = np.linspace(min_ret, max_ret, n_points)

    frontier_std = []
    frontier_mean = []

    for target in target_returns:
        # Minimise variance subject to target return
        return_constraint = LinearConstraint(MU, target, target)

        def portfolio_variance(w):
            return w.T @ COV @ w

        res = minimize(
            portfolio_variance,
            x0=np.ones(N) / N,
            method="trust-constr",
            constraints=[linear_constraint, return_constraint],
            bounds=bounds,
        )

        if res.success:
            frontier_std.append(np.sqrt(res.fun))
            frontier_mean.append(target)

    return np.array(frontier_std), np.array(frontier_mean)


# ============================================================================
# Demo / Main
# ============================================================================

if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("=" * 72)
    print("  MEAN-VARIANCE PORTFOLIO OPTIMIZATION")
    print("  Sharpe Ratio Maximization & Efficient Frontier")
    print("=" * 72)

    # ---- 1. Define sample assets ----
    # Using realistic annual return statistics for a diversified portfolio
    asset_names = ["US Equity", "Intl Equity", "Bonds", "Real Estate", "Commodities"]
    N_assets = len(asset_names)

    # Expected annual returns
    MU = np.array([0.10, 0.08, 0.03, 0.07, 0.05])

    # Standard deviations
    STD = np.array([0.18, 0.22, 0.05, 0.15, 0.20])

    # Correlation matrix
    CORR = np.array([
        [1.00, 0.70, 0.10, 0.40, 0.15],
        [0.70, 1.00, 0.05, 0.35, 0.20],
        [0.10, 0.05, 1.00, 0.15, 0.00],
        [0.40, 0.35, 0.15, 1.00, 0.10],
        [0.15, 0.20, 0.00, 0.10, 1.00],
    ])

    # Build covariance matrix from correlations and standard deviations
    COV = np.outer(STD, STD) * CORR

    # Risk-free rate
    Rf = 0.02

    print("\n  Asset Universe:")
    print(f"  {'Asset':>15s}  {'E[R]':>8s}  {'Std':>8s}")
    print(f"  {'-'*15}  {'-'*8}  {'-'*8}")
    for i in range(N_assets):
        print(f"  {asset_names[i]:>15s}  {MU[i]:8.2%}  {STD[i]:8.2%}")
    print(f"\n  Risk-free rate: {Rf:.2%}")

    # ---- 2. Find the tangency portfolio ----
    print("\n" + "-" * 72)
    print("  1. Tangency Portfolio (Maximum Sharpe Ratio)")
    print("-" * 72)

    result = optimal_weights(MU, COV, Rf=Rf, w_max=1.0)

    print(f"\n  Sharpe Ratio: {result['Sharpe Ratio']:.4f}")
    print(f"  Expected Return: {result['stock portfolio']['mean']:.4%}")
    print(f"  Volatility:      {result['stock portfolio']['std']:.4%}")
    print(f"\n  Optimal Weights:")
    for i in range(N_assets):
        w = result['stock weights'][i]
        bar = "#" * int(w * 50)
        print(f"    {asset_names[i]:>15s}: {w:7.2%}  {bar}")

    # ---- 3. Efficient frontier ----
    print("\n" + "-" * 72)
    print("  2. Efficient Frontier")
    print("-" * 72)

    frontier_std, frontier_mean = compute_efficient_frontier(
        MU, COV, Rf=Rf, w_max=1.0, n_points=200)

    print(f"  Computed {len(frontier_std)} frontier points")
    print(f"  Return range: [{frontier_mean.min():.2%}, {frontier_mean.max():.2%}]")
    print(f"  Vol range:    [{frontier_std.min():.2%}, {frontier_std.max():.2%}]")

    # ---- 4. Capital Allocation Line examples ----
    print("\n" + "-" * 72)
    print("  3. Capital Allocation Line (CAL) Examples")
    print("-" * 72)

    # Portfolio with desired return of 6%
    result_06 = optimal_weights(MU, COV, Rf=Rf, w_max=1.0, desired_mean=0.06)
    print(f"\n  Target return = 6.00%:")
    print(f"    Bond allocation:  {result_06['Bond + Stock weights']['Bond']:.2%}")
    print(f"    Stock allocation: {result_06['Bond + Stock weights']['Stock']:.2%}")
    print(f"    Portfolio std:    {result_06['Total portfolio']['std']:.4%}")

    # Portfolio with desired volatility of 10%
    result_10v = optimal_weights(MU, COV, Rf=Rf, w_max=1.0, desired_std=0.10)
    print(f"\n  Target volatility = 10.00%:")
    print(f"    Bond allocation:  {result_10v['Bond + Stock weights']['Bond']:.2%}")
    print(f"    Stock allocation: {result_10v['Bond + Stock weights']['Stock']:.2%}")
    print(f"    Portfolio return: {result_10v['Total portfolio']['mean']:.4%}")

    # ---- 5. Random portfolios for comparison ----
    print("\n" + "-" * 72)
    print("  4. Monte Carlo: Random Portfolio Comparison")
    print("-" * 72)

    np.random.seed(42)
    n_random = 5000
    random_returns = np.zeros(n_random)
    random_stds = np.zeros(n_random)
    random_sharpes = np.zeros(n_random)

    for i in range(n_random):
        w = np.random.dirichlet(np.ones(N_assets))  # random weights summing to 1
        random_returns[i] = MU @ w
        random_stds[i] = np.sqrt(w @ COV @ w)
        random_sharpes[i] = (random_returns[i] - Rf) / random_stds[i]

    print(f"  Generated {n_random} random portfolios")
    print(f"  Best random Sharpe: {random_sharpes.max():.4f}")
    print(f"  Optimal Sharpe:     {result['Sharpe Ratio']:.4f}")
    print(f"  Improvement:        {(result['Sharpe Ratio']/random_sharpes.max() - 1)*100:.1f}%")

    # ---- 6. Plot ----
    print("\n--- Generating Plot ---")

    fig, ax = plt.subplots(figsize=(12, 8))

    # Random portfolios (coloured by Sharpe ratio)
    scatter = ax.scatter(
        random_stds * 100, random_returns * 100,
        c=random_sharpes, cmap="viridis", alpha=0.3, s=8,
        label="Random portfolios"
    )
    plt.colorbar(scatter, ax=ax, label="Sharpe Ratio", shrink=0.8)

    # Efficient frontier
    ax.plot(frontier_std * 100, frontier_mean * 100, "b-", linewidth=2.5,
            label="Efficient Frontier")

    # Capital Allocation Line
    cal_std = np.linspace(0, frontier_std.max() * 1.2, 100)
    cal_mean = Rf + result["Sharpe Ratio"] * cal_std
    ax.plot(cal_std * 100, cal_mean * 100, "r--", linewidth=1.5,
            label=f"CAL (SR={result['Sharpe Ratio']:.3f})")

    # Tangency portfolio
    tang_std = result["stock portfolio"]["std"]
    tang_mean = result["stock portfolio"]["mean"]
    ax.plot(tang_std * 100, tang_mean * 100, "r*", markersize=20,
            label="Tangency Portfolio", zorder=5)

    # Risk-free asset
    ax.plot(0, Rf * 100, "gs", markersize=12, label=f"Risk-free ({Rf:.0%})", zorder=5)

    # Individual assets
    for i in range(N_assets):
        ax.plot(STD[i] * 100, MU[i] * 100, "D", markersize=10, zorder=5)
        ax.annotate(asset_names[i],
                    (STD[i] * 100, MU[i] * 100),
                    textcoords="offset points", xytext=(8, 5),
                    fontsize=9, fontweight="bold")

    ax.set_xlabel("Portfolio Volatility (%)", fontsize=12)
    ax.set_ylabel("Expected Return (%)", fontsize=12)
    ax.set_title("Mean-Variance Optimization: Efficient Frontier & Tangency Portfolio",
                 fontsize=14)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, STD.max() * 130)
    ax.set_ylim(Rf * 100 - 1, MU.max() * 100 + 2)

    plt.tight_layout()
    plt.savefig("portfolio_optimization_demo.png", dpi=150, bbox_inches="tight")
    print("  Saved: portfolio_optimization_demo.png")

    # ---- Summary ----
    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    print("  Tangency Portfolio (Maximum Sharpe Ratio):")
    print(f"    Sharpe Ratio:    {result['Sharpe Ratio']:.4f}")
    print(f"    Expected Return: {result['stock portfolio']['mean']:.2%}")
    print(f"    Volatility:      {result['stock portfolio']['std']:.2%}")
    print(f"    Weights:")
    for i in range(N_assets):
        print(f"      {asset_names[i]:>15s}: {result['stock weights'][i]:.2%}")
    print()
    print("  The Capital Allocation Line (CAL) allows investors to choose")
    print("  any risk-return combination by mixing the tangency portfolio")
    print("  with the risk-free asset.")
    print("=" * 72)
