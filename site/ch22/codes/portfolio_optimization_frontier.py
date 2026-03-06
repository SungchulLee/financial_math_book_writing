"""
Portfolio Optimization Frontier

Educational script demonstrating portfolio optimization frontier concepts.
"""

# ---
# title: "Mean-Variance Portfolio Optimisation & Efficient Frontier"
# description: >
#   Implements Markowitz mean-variance optimisation:
#     1. Random portfolio scatter (Monte Carlo sampling of weights).
#     2. Maximum-Sharpe-ratio portfolio (tangency portfolio).
#     3. Minimum-variance portfolio.
#     4. Efficient frontier via constrained optimisation.
#     5. Capital market line via spline interpolation and tangent
#        from the risk-free rate.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import math
import numpy as np
import pandas as pd
import scipy.optimize as sco
import scipy.interpolate as sci
import matplotlib.pyplot as plt


# ══════════════════════════════════════════════════════════════════
#  Synthetic Return Data (replace with real data in production)
# ══════════════════════════════════════════════════════════════════

# ======================================================================

def generate_correlated_returns(symbols=None, n_days=2000, seed=42):
    """Create synthetic daily log-returns with realistic
    correlations, means, and volatilities.

    Returns
    -------
    rets : DataFrame  —  daily log-returns
    """
    if symbols is None:
        symbols = ['AAPL', 'MSFT', 'SPY', 'GLD']
    np.random.seed(seed)
    noa = len(symbols)
    # Target annual means and vols
    ann_means = np.array([0.21, 0.14, 0.10, 0.01])[:noa]
    ann_vols = np.array([0.25, 0.22, 0.15, 0.16])[:noa]
    # Correlation matrix
    corr = np.array([
        [1.00, 0.60, 0.55, 0.05],
        [0.60, 1.00, 0.65, -0.02],
        [0.55, 0.65, 1.00, 0.01],
        [0.05, -0.02, 0.01, 1.00],
    ])[:noa, :noa]
    L = np.linalg.cholesky(corr)
    daily_vols = ann_vols / np.sqrt(252)
    daily_means = ann_means / 252

    z = np.random.standard_normal((n_days, noa))
    corr_z = z @ L.T
    daily_rets = daily_means + daily_vols * corr_z

    dates = pd.bdate_range('2010-01-04', periods=n_days)
    return pd.DataFrame(daily_rets, index=dates, columns=symbols)


# ══════════════════════════════════════════════════════════════════
#  Portfolio Return & Volatility
# ══════════════════════════════════════════════════════════════════

def portfolio_return(weights, mean_returns):
    """Annualised portfolio return."""
    return np.sum(mean_returns * weights) * 252


def portfolio_volatility(weights, cov_matrix):
    """Annualised portfolio volatility."""
    return np.sqrt(weights.T @ (cov_matrix * 252) @ weights)


# ══════════════════════════════════════════════════════════════════
#  Optimisation
# ══════════════════════════════════════════════════════════════════

def max_sharpe_portfolio(mean_returns, cov_matrix, rf=0.0):
    """Find the tangency (max Sharpe) portfolio."""
    noa = len(mean_returns)
    def neg_sharpe(w):
        ret = portfolio_return(w, mean_returns)
        vol = portfolio_volatility(w, cov_matrix)
        return -(ret - rf) / vol

    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = tuple((0, 1) for _ in range(noa))
    w0 = np.ones(noa) / noa
    res = sco.minimize(neg_sharpe, w0, method='SLSQP',
                       bounds=bounds, constraints=constraints)
    return res


def min_variance_portfolio(mean_returns, cov_matrix):
    """Find the global minimum-variance portfolio."""
    noa = len(mean_returns)
    def vol(w):
        return portfolio_volatility(w, cov_matrix)

    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = tuple((0, 1) for _ in range(noa))
    w0 = np.ones(noa) / noa
    res = sco.minimize(vol, w0, method='SLSQP',
                       bounds=bounds, constraints=constraints)
    return res


def efficient_frontier(mean_returns, cov_matrix, n_points=50):
    """Trace the efficient frontier by minimising variance at each
    target return level.

    Returns
    -------
    trets : ndarray – target return levels
    tvols : ndarray – corresponding minimum volatilities
    """
    noa = len(mean_returns)
    bounds = tuple((0, 1) for _ in range(noa))
    w0 = np.ones(noa) / noa

    # Range of target returns
    ret_min = portfolio_return(
        min_variance_portfolio(mean_returns, cov_matrix)['x'],
        mean_returns)
    ret_max = max(mean_returns) * 252
    trets = np.linspace(ret_min, ret_max * 0.95, n_points)
    tvols = []

    for tret in trets:
        constraints = (
            {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq',
             'fun': lambda w, t=tret: portfolio_return(w, mean_returns) - t},
        )
        res = sco.minimize(
            lambda w: portfolio_volatility(w, cov_matrix),
            w0, method='SLSQP', bounds=bounds,
            constraints=constraints)
        tvols.append(res['fun'])

    return trets, np.array(tvols)


# ══════════════════════════════════════════════════════════════════
#  Capital Market Line
# ══════════════════════════════════════════════════════════════════

def capital_market_line(trets, tvols, rf=0.01):
    """Find the CML tangent from the risk-free rate to the
    efficient frontier via spline interpolation.

    Returns
    -------
    intercept, slope, tangent_vol : floats
    """
    # Use only the upper (efficient) part of the frontier
    idx = np.argmin(tvols)
    evols = tvols[idx:]
    erets = trets[idx:]

    tck = sci.splrep(evols, erets)

    def f(x):
        return sci.splev(x, tck, der=0)
    def df(x):
        return sci.splev(x, tck, der=1)

    def equations(p):
        eq1 = rf - p[0]
        eq2 = rf + p[1] * p[2] - f(p[2])
        eq3 = p[1] - df(p[2])
        return eq1, eq2, eq3

    opt = sco.fsolve(equations, [rf, 0.5, 0.15])
    return opt  # [intercept, slope, tangent_vol]


# ══════════════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════════════

if __name__ == '__main__':

    symbols = ['AAPL', 'MSFT', 'SPY', 'GLD']
    rets = generate_correlated_returns(symbols)
    mean_rets = rets.mean()
    cov_mat = rets.cov()
    noa = len(symbols)

    print("Annualised returns:")
    print((mean_rets * 252).round(4))
    print("\nAnnualised covariance matrix:")
    print((cov_mat * 252).round(4))

    # ── 1. Random portfolio scatter ───────────────────────────────
    n_portfolios = 3000
    p_rets, p_vols = [], []
    for _ in range(n_portfolios):
        w = np.random.random(noa)
        w /= w.sum()
        p_rets.append(portfolio_return(w, mean_rets))
        p_vols.append(portfolio_volatility(w, cov_mat))
    p_rets = np.array(p_rets)
    p_vols = np.array(p_vols)

    # ── 2. Optimal portfolios ────────────────────────────────────
    opt_s = max_sharpe_portfolio(mean_rets, cov_mat)
    opt_v = min_variance_portfolio(mean_rets, cov_mat)

    sr_ret = portfolio_return(opt_s['x'], mean_rets)
    sr_vol = portfolio_volatility(opt_s['x'], cov_mat)
    mv_ret = portfolio_return(opt_v['x'], mean_rets)
    mv_vol = portfolio_volatility(opt_v['x'], cov_mat)

    print(f"\nMax-Sharpe weights: {np.round(opt_s['x'], 3)}")
    print(f"  Return={sr_ret:.3f}, Vol={sr_vol:.3f}, "
          f"Sharpe={sr_ret/sr_vol:.3f}")
    print(f"Min-Variance weights: {np.round(opt_v['x'], 3)}")
    print(f"  Return={mv_ret:.3f}, Vol={mv_vol:.3f}")

    # ── 3. Efficient frontier ────────────────────────────────────
    trets, tvols = efficient_frontier(mean_rets, cov_mat)

    # ── 4. Plot ──────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    sc = ax.scatter(p_vols, p_rets, c=p_rets / p_vols,
                    marker='.', alpha=0.6, cmap='coolwarm')
    ax.plot(tvols, trets, 'b', lw=3, label='Efficient Frontier')
    ax.plot(sr_vol, sr_ret, 'y*', ms=15, label='Max Sharpe')
    ax.plot(mv_vol, mv_ret, 'r*', ms=15, label='Min Variance')
    ax.set_xlabel('Expected Volatility')
    ax.set_ylabel('Expected Return')
    ax.legend(loc='best')
    ax.grid(alpha=0.3)
    plt.colorbar(sc, label='Sharpe Ratio')
    fig.suptitle('Mean-Variance Optimisation', fontsize=13)
    plt.tight_layout()
    plt.show()

    # ── 5. Capital market line ───────────────────────────────────
    try:
        cml = capital_market_line(trets, tvols, rf=0.01)
        fig, ax = plt.subplots(figsize=(10, 6))
        sc = ax.scatter(p_vols, p_rets,
                        c=(p_rets - 0.01) / p_vols,
                        marker='.', alpha=0.6, cmap='coolwarm')
        # Efficient part
        idx = np.argmin(tvols)
        ax.plot(tvols[idx:], trets[idx:], 'b', lw=3)
        # CML
        cx = np.linspace(0, 0.3, 100)
        ax.plot(cx, cml[0] + cml[1] * cx, 'r', lw=1.5,
                label='Capital Market Line')
        ax.plot(cml[2], cml[0] + cml[1] * cml[2],
                'y*', ms=15, label='Tangency Portfolio')
        ax.axhline(0, color='k', ls='--', lw=0.5)
        ax.set_xlabel('Expected Volatility')
        ax.set_ylabel('Expected Return')
        ax.legend(loc='best')
        ax.grid(alpha=0.3)
        plt.colorbar(sc, label='Sharpe Ratio')
        fig.suptitle('Capital Market Line', fontsize=13)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"CML computation skipped: {e}")
