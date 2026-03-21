"""
Bayesian Regression Finance

Educational script demonstrating bayesian regression finance concepts.
"""

# ---
# title: "Bayesian Linear Regression for Financial Data"
# description: >
#   Demonstrates Bayesian regression applied to finance:
#     1. Introductory example: recover slope and intercept of a
#        synthetic linear relationship using PyMC3 (or a simple
#        Metropolis-Hastings sampler as fallback).
#     2. Pairs regression between two correlated assets (e.g.
#        GDX vs GLD) with static and time-varying (random-walk)
#        coefficients.
#   The code is designed to run even without PyMC3 by providing
#   a lightweight MCMC fallback.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ══════════════════════════════════════════════════════════════════
#  Lightweight Bayesian Linear Regression (no PyMC3 required)
# ══════════════════════════════════════════════════════════════════

# ======================================================================

class BayesianLinearRegression:
    """Bayesian linear regression  y = alpha + beta * x + eps
    using Gibbs sampling with conjugate priors.

    Priors
    ------
    alpha ~ N(mu_a, tau_a^{-1})
    beta  ~ N(mu_b, tau_b^{-1})
    sigma ~ InverseGamma(a0, b0)

    Parameters
    ----------
    mu_a, mu_b : float – prior means (default 0)
    tau_a, tau_b : float – prior precisions (default 0.001)
    a0, b0 : float – InverseGamma hyperparameters (default 0.01)
    """

    def __init__(self, mu_a=0, mu_b=0, tau_a=0.001, tau_b=0.001,
                 a0=0.01, b0=0.01):
        self.mu_a = mu_a
        self.mu_b = mu_b
        self.tau_a = tau_a
        self.tau_b = tau_b
        self.a0 = a0
        self.b0 = b0

    def sample(self, x, y, n_samples=2000, burn_in=500, seed=42):
        """Run Gibbs sampler.

        Returns
        -------
        trace : dict with keys 'alpha', 'beta', 'sigma'
        """
        np.random.seed(seed)
        n = len(x)
        # Initialise
        alpha = 0.0
        beta = 0.0
        sigma2 = 1.0

        trace = {'alpha': [], 'beta': [], 'sigma': []}

        for i in range(n_samples + burn_in):
            # Sample alpha | beta, sigma2
            prec_a = self.tau_a + n / sigma2
            mean_a = (self.tau_a * self.mu_a
                       + np.sum(y - beta * x) / sigma2) / prec_a
            alpha = np.random.normal(mean_a, 1.0 / np.sqrt(prec_a))

            # Sample beta | alpha, sigma2
            prec_b = self.tau_b + np.sum(x ** 2) / sigma2
            mean_b = (self.tau_b * self.mu_b
                       + np.sum(x * (y - alpha)) / sigma2) / prec_b
            beta = np.random.normal(mean_b, 1.0 / np.sqrt(prec_b))

            # Sample sigma2 | alpha, beta
            residuals = y - alpha - beta * x
            an = self.a0 + n / 2.0
            bn = self.b0 + np.sum(residuals ** 2) / 2.0
            sigma2 = 1.0 / np.random.gamma(an, 1.0 / bn)

            if i >= burn_in:
                trace['alpha'].append(alpha)
                trace['beta'].append(beta)
                trace['sigma'].append(np.sqrt(sigma2))

        for k in trace:
            trace[k] = np.array(trace[k])
        return trace


# ══════════════════════════════════════════════════════════════════
#  Rolling-Window Bayesian Regression (time-varying coefficients)
# ══════════════════════════════════════════════════════════════════

def rolling_bayesian_regression(x, y, window=100, n_samples=500):
    """Estimate alpha(t), beta(t) via rolling-window Bayesian
    regression, providing a simple proxy for time-varying
    coefficients.

    Returns
    -------
    alphas, betas : ndarray – posterior means at each window step
    indices : ndarray – centre indices of each window
    """
    model = BayesianLinearRegression()
    n = len(x)
    alphas, betas, indices = [], [], []
    for start in range(0, n - window + 1, window // 2):
        end = start + window
        trace = model.sample(x[start:end], y[start:end],
                             n_samples=n_samples, burn_in=200)
        alphas.append(trace['alpha'].mean())
        betas.append(trace['beta'].mean())
        indices.append((start + end) // 2)
    return np.array(alphas), np.array(betas), np.array(indices)


# ══════════════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════════════

if __name__ == '__main__':

    # ── Part 1: Introductory example ─────────────────────────────
    print("=" * 50)
    print("Part 1 — Synthetic linear data")
    print("=" * 50)

    np.random.seed(1000)
    x = np.linspace(0, 10, 500)
    y_true = 4 + 2 * x
    y = y_true + np.random.standard_normal(len(x)) * 2

    # OLS reference
    ols = np.polyfit(x, y, 1)
    print(f"OLS: slope={ols[0]:.4f}, intercept={ols[1]:.4f}")

    # Bayesian
    blr = BayesianLinearRegression()
    trace = blr.sample(x, y, n_samples=2000, burn_in=1000)

    print(f"Bayesian posterior means:")
    print(f"  alpha = {trace['alpha'].mean():.4f} "
          f"± {trace['alpha'].std():.4f}")
    print(f"  beta  = {trace['beta'].mean():.4f} "
          f"± {trace['beta'].std():.4f}")
    print(f"  sigma = {trace['sigma'].mean():.4f} "
          f"± {trace['sigma'].std():.4f}")

    # Scatter + posterior samples
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, c=y, marker='v', cmap='coolwarm', alpha=0.5, s=15)
    for i in range(0, len(trace['alpha']), 20):
        ax.plot(x, trace['alpha'][i] + trace['beta'][i] * x,
                'b', alpha=0.05)
    ax.plot(x, trace['alpha'].mean() + trace['beta'].mean() * x,
            'r', lw=2, label='Posterior mean')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Bayesian Linear Regression — Posterior Samples')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Trace plots
    fig, axes = plt.subplots(3, 2, figsize=(12, 7))
    for i, (key, true_val) in enumerate(
            [('alpha', 4), ('beta', 2), ('sigma', 2)]):
        axes[i, 0].plot(trace[key], alpha=0.7)
        axes[i, 0].axhline(true_val, color='r', ls='--', lw=1.5)
        axes[i, 0].set_ylabel(key)
        axes[i, 0].set_title(f'{key} — trace')
        axes[i, 1].hist(trace[key], bins=30, density=True, alpha=0.7)
        axes[i, 1].axvline(true_val, color='r', ls='--', lw=1.5)
        axes[i, 1].set_title(f'{key} — posterior')
    plt.tight_layout()
    plt.show()

    # ── Part 2: Pairs regression (synthetic GDX vs GLD) ──────────
    print("\n" + "=" * 50)
    print("Part 2 — Pairs regression (synthetic assets)")
    print("=" * 50)

    n_days = 2000
    np.random.seed(2024)
    # Simulate two correlated asset prices
    rho = 0.72
    L = np.linalg.cholesky([[1, rho], [rho, 1]])
    z = np.random.standard_normal((n_days, 2)) @ L.T
    gdx = 100 * np.exp(np.cumsum(0.0001 + 0.015 * z[:, 0]))
    gld = 100 * np.exp(np.cumsum(0.0002 + 0.010 * z[:, 1]))
    # Normalise to start at 1
    gdx /= gdx[0]
    gld /= gld[0]

    print(f"Correlation: {np.corrcoef(gdx, gld)[0,1]:.4f}")

    # Static Bayesian regression
    trace2 = blr.sample(gdx, gld, n_samples=2000, burn_in=1000)
    print(f"Static alpha = {trace2['alpha'].mean():.4f}")
    print(f"Static beta  = {trace2['beta'].mean():.4f}")

    fig, ax = plt.subplots(figsize=(10, 6))
    sc = ax.scatter(gdx, gld, c=np.arange(n_days), marker='o',
                    cmap='coolwarm', alpha=0.5, s=10)
    for i in range(0, len(trace2['alpha']), 40):
        ax.plot(gdx, trace2['alpha'][i] + trace2['beta'][i] * gdx,
                'b', alpha=0.03)
    ax.set_xlabel('Asset X (GDX proxy)')
    ax.set_ylabel('Asset Y (GLD proxy)')
    ax.set_title('Static Bayesian Regression')
    plt.colorbar(sc, label='Trading day')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Rolling (time-varying) Bayesian regression
    alphas, betas, idx = rolling_bayesian_regression(
        gdx, gld, window=200, n_samples=500)
    dates = pd.bdate_range('2010-01-04', periods=n_days)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates[idx], alphas, 'b-.', lw=1, label='α(t)')
    ax.plot(dates[idx], betas, 'r-.', lw=1, label='β(t)')
    ax.set_ylabel('Coefficient value')
    ax.set_title('Time-Varying Bayesian Coefficients (Rolling Window)')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
