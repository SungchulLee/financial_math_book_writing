#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_mvo_short_cvxpy.py
MVO Extensions: Log-to-Linear Returns, CVXPY Frontier, Short Positions & Portfolio Density

Credits
-------
Based on notebook "7.1 Classical MVO" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 3 -- Portfolio Optimization).

Topics covered
--------------
1. Log-return to linear-return conversion (exact formula).
2. Efficient frontier via CVXPY with risk-aversion parameter sweep.
3. Short positions: closed-form solution using sufficient statistics
   (Omega, A, B, C, D) from the unconstrained Lagrangian.
4. Theoretical efficient frontier equation as a conic section.
5. Portfolio return probability density: Monte Carlo simulation
   with KDE vs normal approximation and loss probability.
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from scipy.optimize import minimize, Bounds, LinearConstraint


# ============================================================================
# 1. LOG-RETURN TO LINEAR-RETURN CONVERSION
# ============================================================================

def log_to_linear_moments(mu_log, cov_log):
    """
    Convert log-return mean and covariance to linear-return moments.

    If log-returns r ~ N(mu_log, cov_log), then the linear return
    R = exp(r) - 1 has:
        E[R_i] = exp(mu_log_i + 0.5 * cov_log_ii) - 1
        Cov(R_i, R_j) = (E[R_i]+1)(E[R_j]+1)(exp(cov_log_ij) - 1)

    This is the EXACT conversion, not the first-order approximation
    E[R] ≈ mu_log + 0.5*sigma^2.

    Parameters
    ----------
    mu_log : ndarray, shape (N,)
        Mean of log-returns (scaled to desired horizon).
    cov_log : ndarray, shape (N, N)
        Covariance matrix of log-returns (scaled to desired horizon).

    Returns
    -------
    MU : ndarray, shape (N,)
        Expected linear returns.
    COV : ndarray, shape (N, N)
        Covariance matrix of linear returns.
    """
    MU = np.exp(mu_log + 0.5 * np.diag(cov_log)) - 1
    diag_MU1 = np.diag(MU + 1)
    COV = diag_MU1 @ (np.exp(cov_log) - 1) @ diag_MU1
    return MU, COV


# ============================================================================
# 2. EFFICIENT FRONTIER VIA CVXPY (RISK-AVERSION SWEEP)
# ============================================================================

def efficient_frontier_cvxpy(MU, COV, Rf=0.0, n_gamma=500,
                             gamma_min=1.0, gamma_max=1e4, long_only=True):
    """
    Compute the efficient frontier by sweeping the risk-aversion parameter
    gamma in the CVXPY convex program:

        maximize  MU'w - gamma * w'COV*w
        subject to  sum(w) = 1,  w >= 0  (if long_only)

    As gamma -> 0, the portfolio maximises return (most aggressive).
    As gamma -> inf, the portfolio minimises variance (most conservative).

    Parameters
    ----------
    MU : ndarray, shape (N,)
        Expected returns.
    COV : ndarray, shape (N, N)
        Covariance matrix.
    Rf : float
        Risk-free rate (for Sharpe ratio computation).
    n_gamma : int
        Number of risk-aversion values to sweep.
    gamma_min, gamma_max : float
        Range of risk-aversion parameter (log-spaced).
    long_only : bool
        If True, enforce w >= 0.

    Returns
    -------
    dict with keys:
        std_values : ndarray      Portfolio volatilities.
        mean_values : ndarray     Portfolio expected returns.
        sharpe_values : ndarray   Sharpe ratios.
        gamma_values : ndarray    Risk-aversion parameters.
        portfolios : list         List of weight vectors.
        best_idx : int            Index of maximum Sharpe ratio.
    """
    try:
        import cvxpy as cp
    except ImportError:
        raise ImportError("cvxpy is required: pip install cvxpy")

    N = len(MU)
    w = cp.Variable(N)
    gamma = cp.Parameter(nonneg=True)
    ret = MU @ w
    risk = cp.quad_form(w, COV)
    objective = cp.Maximize(ret - gamma * risk)
    constraints = [cp.sum(w) == 1]
    if long_only:
        constraints.append(w >= 0)
    prob = cp.Problem(objective, constraints)

    gamma_vals = np.logspace(np.log10(gamma_min), np.log10(gamma_max),
                             num=n_gamma)
    std_values = np.zeros(n_gamma)
    mean_values = np.zeros(n_gamma)
    sharpe_values = np.zeros(n_gamma)
    portfolios = []

    for i in range(n_gamma):
        gamma.value = gamma_vals[i]
        prob.solve()
        std_values[i] = np.sqrt(risk.value)
        mean_values[i] = ret.value
        if std_values[i] > 1e-12:
            sharpe_values[i] = (mean_values[i] - Rf) / std_values[i]
        portfolios.append(w.value.copy())

    best_idx = np.argmax(sharpe_values)

    return {
        "std_values": std_values,
        "mean_values": mean_values,
        "sharpe_values": sharpe_values,
        "gamma_values": gamma_vals,
        "portfolios": portfolios,
        "best_idx": best_idx,
    }


# ============================================================================
# 3. SHORT POSITIONS -- CLOSED-FORM SOLUTION
# ============================================================================

def short_position_weights(MU, COV, target_mu):
    """
    Closed-form optimal portfolio weights when short selling is allowed.

    Without the non-negativity constraint w >= 0, the Lagrangian for:
        minimize  w'COV*w
        s.t.      MU'w = target_mu,  1'w = 1
    has an explicit solution using the sufficient statistics:
        Omega = COV^{-1}
        A = 1'Omega*MU,  B = MU'Omega*MU,  C = 1'Omega*1
        D = B*C - A^2

    The optimal weights are:
        w* = [target_mu * Omega(C*MU - A*1) + Omega(B*1 - A*MU)] / D

    The minimum variance is: sigma^2 = (C*target_mu^2 - 2*A*target_mu + B) / D

    Parameters
    ----------
    MU : ndarray, shape (N,)
        Expected returns.
    COV : ndarray, shape (N, N)
        Covariance matrix (must be full rank).
    target_mu : float
        Target portfolio expected return.

    Returns
    -------
    dict with keys:
        weights : ndarray     Optimal weights (may be negative).
        std : float           Portfolio standard deviation.
        A, B, C, D : float   Sufficient statistics.
    """
    N = len(MU)
    ones = np.ones(N)
    Omega = np.linalg.inv(COV)

    A = ones @ Omega @ MU
    B = MU @ Omega @ MU
    C = Omega.sum()  # = ones @ Omega @ ones
    D = B * C - A**2

    weights = (target_mu * Omega @ (C * MU - A * ones)
               + Omega @ (B * ones - A * MU)) / D

    sigma2 = (C * target_mu**2 - 2 * A * target_mu + B) / D
    std = np.sqrt(max(sigma2, 0.0))

    return {"weights": weights, "std": std,
            "A": A, "B": B, "C": C, "D": D}


def theoretical_frontier_short(MU, COV, n_points=400):
    """
    Compute the theoretical efficient frontier (hyperbola) when short
    selling is allowed, using the closed-form variance formula:

        sigma^2(mu) = (C*mu^2 - 2*A*mu + B) / D

    This traces out the full frontier including the inefficient branch.

    Parameters
    ----------
    MU : ndarray, shape (N,)
        Expected returns.
    COV : ndarray, shape (N, N)
        Covariance matrix.
    n_points : int
        Number of points on the frontier.

    Returns
    -------
    frontier_std : ndarray   Standard deviations.
    frontier_mean : ndarray  Expected returns.
    A, B, C, D : float       Sufficient statistics.
    """
    N = len(MU)
    ones = np.ones(N)
    Omega = np.linalg.inv(COV)
    A = ones @ Omega @ MU
    B = MU @ Omega @ MU
    C = Omega.sum()
    D = B * C - A**2

    mu_range = np.linspace(MU.min() - 0.1, MU.max() + 0.1, n_points)
    sigma2 = (C * mu_range**2 - 2 * A * mu_range + B) / D
    sigma2 = np.maximum(sigma2, 0.0)

    return np.sqrt(sigma2), mu_range, A, B, C, D


# ============================================================================
# 4. PORTFOLIO RETURN PROBABILITY DENSITY
# ============================================================================

def portfolio_density(mu_log, cov_log, weights, n_sim=50000, seed=42):
    """
    Estimate the probability density of the portfolio return by Monte Carlo
    simulation of multivariate log-normal returns.

    Simulates log-returns from N(mu_log, cov_log), converts to linear
    returns via R = exp(r) - 1, then computes portfolio return R_p = w'R.

    Returns both the KDE estimate and the normal approximation.

    Parameters
    ----------
    mu_log : ndarray, shape (N,)
        Log-return mean vector.
    cov_log : ndarray, shape (N, N)
        Log-return covariance matrix.
    weights : ndarray, shape (N,)
        Portfolio weights.
    n_sim : int
        Number of simulated scenarios.
    seed : int
        Random seed.

    Returns
    -------
    dict with keys:
        portfolio_returns : ndarray  Simulated portfolio returns.
        kde : scipy.stats.gaussian_kde  KDE estimator.
        normal : scipy.stats.norm  Normal approximation.
        mu_port : float              Portfolio mean.
        sigma_port : float           Portfolio std.
    """
    rng = np.random.RandomState(seed)
    log_returns = rng.multivariate_normal(mu_log, cov_log, size=n_sim)
    linear_returns = np.exp(log_returns) - 1
    portfolio_returns = linear_returns @ weights

    mu_port = portfolio_returns.mean()
    sigma_port = portfolio_returns.std()

    kde = ss.gaussian_kde(portfolio_returns)
    normal = ss.norm(loc=mu_port, scale=sigma_port)

    return {
        "portfolio_returns": portfolio_returns,
        "kde": kde,
        "normal": normal,
        "mu_port": mu_port,
        "sigma_port": sigma_port,
    }


def loss_probability(density_result, threshold):
    """
    Compute the probability of portfolio loss exceeding a threshold.

    Parameters
    ----------
    density_result : dict
        Output from portfolio_density().
    threshold : float
        Maximum loss threshold (e.g., -0.09 for 9% loss).

    Returns
    -------
    dict with keys:
        kde_prob : float    P(R_p < threshold) from KDE.
        normal_prob : float P(R_p < threshold) from normal approximation.
    """
    kde_prob = density_result["kde"].integrate_box_1d(-np.inf, threshold)
    normal_prob = density_result["normal"].cdf(threshold)
    return {"kde_prob": kde_prob, "normal_prob": normal_prob}


# ============================================================================
# 5. MIN-VARIANCE OPTIMIZER (SCIPY, WITH/WITHOUT SHORT SELLING)
# ============================================================================

def optimizer_scipy(MU, COV, target_mu, long_only=True):
    """
    Find minimum-variance portfolio weights for a fixed target return
    using scipy.optimize.

    Parameters
    ----------
    MU : ndarray, shape (N,)
        Expected returns.
    COV : ndarray, shape (N, N)
        Covariance matrix.
    target_mu : float
        Target portfolio expected return.
    long_only : bool
        If True, enforce w >= 0.

    Returns
    -------
    weights : ndarray  Optimal weights.
    """
    N = len(MU)
    A_mat = np.vstack((np.ones(N), MU))
    b_vec = np.array([1.0, target_mu])
    linear_constraint = LinearConstraint(A_mat, b_vec, b_vec)

    x0 = np.ones(N) / N

    def portfolio_variance(w):
        return w.T @ COV @ w

    if long_only:
        bounds = Bounds(0, 1)
        res = minimize(portfolio_variance, x0=x0, method="trust-constr",
                       constraints=linear_constraint, bounds=bounds)
    else:
        res = minimize(portfolio_variance, x0=x0, method="trust-constr",
                       constraints=linear_constraint)
    return res.x


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all MVO extension demonstrations."""

    # ---- Synthetic asset universe ----
    np.random.seed(42)
    asset_names = ["Tech", "Finance", "Energy", "Healthcare", "Utilities"]
    N = len(asset_names)

    # Simulate plausible monthly statistics
    # (In the original notebook, these come from CSV market data)
    mu_log = np.array([0.015, 0.010, 0.008, 0.012, 0.005])
    std_log = np.array([0.06, 0.05, 0.07, 0.04, 0.03])
    corr = np.array([
        [1.00, 0.55, 0.30, 0.40, 0.10],
        [0.55, 1.00, 0.35, 0.45, 0.20],
        [0.30, 0.35, 1.00, 0.25, 0.15],
        [0.40, 0.45, 0.25, 1.00, 0.10],
        [0.10, 0.20, 0.15, 0.10, 1.00],
    ])
    cov_log = np.outer(std_log, std_log) * corr

    Rf = 0.01 / 12  # monthly risk-free rate

    # ---- 1. Log-to-linear conversion ----
    print("=" * 60)
    print("1. Log-Return to Linear-Return Conversion")
    print("=" * 60)

    MU, COV = log_to_linear_moments(mu_log, cov_log)
    print(f"\n  Log-return means:    {mu_log}")
    print(f"  Linear-return means: {MU.round(6)}")
    print(f"\n  Difference (exact vs first-order approx):")
    approx = mu_log + 0.5 * np.diag(cov_log)
    for i in range(N):
        print(f"    {asset_names[i]:>12s}: exact={MU[i]:.6f}, "
              f"approx={np.exp(approx[i])-1:.6f}, "
              f"diff={abs(MU[i] - (np.exp(approx[i])-1)):.2e}")

    # ---- 2. CVXPY efficient frontier ----
    print("\n" + "=" * 60)
    print("2. Efficient Frontier via CVXPY (Risk-Aversion Sweep)")
    print("=" * 60)

    try:
        cvxpy_result = efficient_frontier_cvxpy(
            MU, COV, Rf=Rf, n_gamma=500, long_only=True)
        best = cvxpy_result["best_idx"]
        print(f"  Computed {len(cvxpy_result['gamma_values'])} frontier points")
        print(f"  Max Sharpe ratio: {cvxpy_result['sharpe_values'][best]:.4f} "
              f"(gamma={cvxpy_result['gamma_values'][best]:.1f})")
        print(f"  Tangent portfolio: "
              f"mean={cvxpy_result['mean_values'][best]:.4f}, "
              f"std={cvxpy_result['std_values'][best]:.4f}")
        print(f"  Weights: {cvxpy_result['portfolios'][best].round(4)}")
        has_cvxpy = True
    except ImportError:
        print("  cvxpy not installed, skipping this section.")
        has_cvxpy = False

    # ---- 3. Short positions: closed-form ----
    print("\n" + "=" * 60)
    print("3. Short Positions -- Closed-Form Solution")
    print("=" * 60)

    target = 0.02
    sp = short_position_weights(MU, COV, target_mu=target)
    print(f"\n  Target return: {target:.4f}")
    print(f"  Sufficient statistics: A={sp['A']:.4f}, B={sp['B']:.6f}, "
          f"C={sp['C']:.4f}, D={sp['D']:.6f}")
    print(f"  Theoretical weights:")
    for i in range(N):
        print(f"    {asset_names[i]:>12s}: {sp['weights'][i]:.4f}")
    print(f"  Portfolio std: {sp['std']:.6f}")

    # Compare with numerical solution
    w_num = optimizer_scipy(MU, COV, target, long_only=False)
    print(f"\n  Numerical weights (scipy):")
    for i in range(N):
        print(f"    {asset_names[i]:>12s}: {w_num[i]:.4f}")
    print(f"  Max |w_th - w_num|: {np.max(np.abs(sp['weights'] - w_num)):.2e}")

    # ---- 4. Theoretical vs numerical frontier ----
    print("\n" + "=" * 60)
    print("4. Theoretical vs Numerical Efficient Frontier (Short Allowed)")
    print("=" * 60)

    th_std, th_mean, A, B, C, D = theoretical_frontier_short(MU, COV)

    # Numerical frontier (with short selling)
    n_pts = 50
    num_means = np.linspace(MU.min() - 0.05, MU.max() + 0.05, n_pts)
    num_stds = np.zeros(n_pts)
    for i, mn in enumerate(num_means):
        w_opt = optimizer_scipy(MU, COV, mn, long_only=False)
        num_stds[i] = np.sqrt(w_opt @ COV @ w_opt)

    print(f"  Sufficient statistics: A={A:.4f}, B={B:.6f}, "
          f"C={C:.4f}, D={D:.6f}")
    print(f"  Theoretical frontier: {len(th_std)} points")
    print(f"  Numerical frontier: {n_pts} points")
    print(f"  Max std difference: "
          f"{np.max(np.abs(np.interp(num_means, th_mean, th_std) - num_stds)):.2e}")

    # ---- 5. Portfolio probability density ----
    print("\n" + "=" * 60)
    print("5. Portfolio Return Probability Density")
    print("=" * 60)

    # Use tangent portfolio weights (from scipy since cvxpy may not be installed)
    def neg_sharpe(w):
        return -(MU @ w - Rf) / np.sqrt(w.T @ COV @ w)

    bounds = Bounds(0, 1)
    lc = LinearConstraint(np.ones(N, dtype=int), 1, 1)
    res = minimize(neg_sharpe, x0=np.ones(N)/N, method="trust-constr",
                   constraints=lc, bounds=bounds)
    w_tangent = res.x

    density = portfolio_density(mu_log, cov_log, w_tangent, n_sim=50000)
    threshold = -0.05
    lp = loss_probability(density, threshold)

    print(f"  Tangent portfolio weights: {w_tangent.round(4)}")
    print(f"  Portfolio mean:  {density['mu_port']:.6f}")
    print(f"  Portfolio std:   {density['sigma_port']:.6f}")
    print(f"\n  Loss probability P(R < {threshold:.0%}):")
    print(f"    KDE estimate:    {lp['kde_prob']:.4f}")
    print(f"    Normal approx:   {lp['normal_prob']:.4f}")

    # ---- Plots ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: CVXPY frontier (or scipy long-only frontier)
    ax = axes[0, 0]
    if has_cvxpy:
        ax.plot(cvxpy_result["std_values"], cvxpy_result["mean_values"],
                "g-", lw=2, label="CVXPY frontier (long-only)")
        CML_x = np.linspace(0, cvxpy_result["std_values"].max() * 1.1, 100)
        CML_y = Rf + cvxpy_result["sharpe_values"][best] * CML_x
        ax.plot(CML_x, CML_y, "r--", lw=1.5,
                label=f"CML (SR={cvxpy_result['sharpe_values'][best]:.3f})")
        ax.plot(cvxpy_result["std_values"][best],
                cvxpy_result["mean_values"][best],
                "r*", ms=15, label="Tangent portfolio")
    for i in range(N):
        ax.plot(np.sqrt(COV[i, i]), MU[i], "o", ms=8)
        ax.annotate(asset_names[i], (np.sqrt(COV[i, i]), MU[i]),
                    textcoords="offset points", xytext=(5, 5), fontsize=8)
    ax.set_xlabel("Std")
    ax.set_ylabel("Return")
    ax.set_title("Efficient Frontier (Long-Only, CVXPY)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 2: Short positions -- theoretical vs numerical
    ax = axes[0, 1]
    ax.plot(th_std, th_mean, "k-", lw=2, alpha=0.7,
            label="Theoretical frontier")
    ax.scatter(num_stds, num_means, s=20, color="green",
               label="Numerical frontier", zorder=3)
    for i in range(N):
        ax.plot(np.sqrt(COV[i, i]), MU[i], "o", color="goldenrod", ms=8)
        ax.annotate(asset_names[i], (np.sqrt(COV[i, i]), MU[i]),
                    textcoords="offset points", xytext=(5, 5), fontsize=8)
    ax.set_xlabel("Std")
    ax.set_ylabel("Return")
    ax.set_title("Short Positions: Theoretical vs Numerical")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 3: Portfolio probability density
    ax = axes[1, 0]
    pr = density["portfolio_returns"]
    x = np.linspace(pr.min(), pr.max(), 500)
    ax.plot(x, density["kde"].evaluate(x), color="salmon", lw=2,
            label=f"KDE (P(R<{threshold:.0%})={lp['kde_prob']:.4f})")
    ax.plot(x, density["normal"].pdf(x), color="blue", lw=1.5,
            label=f"Normal (P(R<{threshold:.0%})={lp['normal_prob']:.4f})")
    ax.axvline(x=threshold, color="grey", ls="--", lw=1.5,
               label="Max loss threshold")
    ax.axvline(x=density["mu_port"], color="green", ls="--", lw=1,
               label="Portfolio mean")
    mu_p = density["mu_port"]
    sig_p = density["sigma_port"]
    ax.axvline(x=mu_p - sig_p, color="orange", ls="--", lw=1,
               label=r"$\pm$ std dev")
    ax.axvline(x=mu_p + sig_p, color="orange", ls="--", lw=1)
    ax.set_xlabel("Return")
    ax.set_ylabel("Density")
    ax.set_title("Portfolio Return Distribution")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Plot 4: Closed-form weights comparison
    ax = axes[1, 1]
    targets = np.linspace(-0.01, 0.03, 6)
    width = 0.12
    x_pos = np.arange(N)
    for j, tgt in enumerate(targets):
        sp_j = short_position_weights(MU, COV, target_mu=tgt)
        offset = (j - len(targets)/2) * width
        bars = ax.bar(x_pos + offset, sp_j["weights"], width=width,
                      label=f"mu={tgt:.2f}", alpha=0.7)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(asset_names, fontsize=8)
    ax.set_ylabel("Weight")
    ax.set_title("Closed-Form Weights (Short Allowed)")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3, axis="y")
    ax.axhline(y=0, color="k", lw=0.5)

    plt.tight_layout()
    plt.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
