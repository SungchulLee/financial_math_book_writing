"""
Jump Diffusion Calibration

Educational script demonstrating jump diffusion calibration concepts.
"""

# ---
# title: "Jump-Diffusion Model Calibration to Option Prices"
# description: >
#   Calibrates a Merton (1976) jump-diffusion model to observed
#   European call option prices.  The workflow:
#     1. Load (or synthesise) market option quotes with strikes
#        and implied volatilities.
#     2. Build a jump-diffusion Monte Carlo pricer.
#     3. Define a mean-squared-error (MSE) objective function.
#     4. Run a two-stage optimisation:
#        (a) Global grid search via ``scipy.optimize.brute``.
#        (b) Local refinement via ``scipy.optimize.fmin`` (Nelder-Mead).
#     5. Compare calibrated model values against market quotes and
#        visualise the fit.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import math
import numpy as np
import pandas as pd
import scipy.optimize as spo
import matplotlib.pyplot as plt
from functools import lru_cache


# ══════════════════════════════════════════════════════════════════
#  Jump-Diffusion Monte Carlo Pricer
# ══════════════════════════════════════════════════════════════════

# ======================================================================

def jd_mcs_european_call(S0, K, T, r, sigma, lamb, mu_j, delta,
                         I=50_000, M=50, fixed_seed=True):
    """Price a European call under the Merton jump-diffusion model.

    Parameters
    ----------
    S0    : float – initial underlying price
    K     : float – strike price
    T     : float – time to maturity (years)
    r     : float – risk-free rate
    sigma : float – diffusion volatility
    lamb  : float – jump intensity (expected jumps per year)
    mu_j  : float – mean of log-jump size
    delta : float – std dev of log-jump size
    I     : int   – number of Monte Carlo paths
    M     : int   – number of time steps
    fixed_seed : bool – reproducible results

    Returns
    -------
    price : float – discounted expected payoff
    """
    if fixed_seed:
        np.random.seed(1000)

    dt = T / M
    # Risk-neutral jump compensator
    rj = lamb * (math.exp(mu_j + 0.5 * delta ** 2) - 1)

    S = np.zeros((M + 1, I))
    S[0] = S0
    sn1 = np.random.standard_normal((M + 1, I))
    sn2 = np.random.standard_normal((M + 1, I))
    poi = np.random.poisson(lamb * dt, (M + 1, I))

    for t in range(1, M + 1):
        S[t] = S[t - 1] * (
            np.exp((r - rj - 0.5 * sigma ** 2) * dt
                   + sigma * math.sqrt(dt) * sn1[t])
            + (np.exp(mu_j + delta * sn2[t]) - 1) * poi[t])
        S[t] = np.maximum(S[t], 0)

    payoff = np.maximum(S[-1] - K, 0)
    return math.exp(-r * T) * np.mean(payoff)


# ══════════════════════════════════════════════════════════════════
#  Synthetic Market Data (replace with real quotes in production)
# ══════════════════════════════════════════════════════════════════

def generate_synthetic_option_data(S0=100.0, r=0.02, T=0.25):
    """Create a set of synthetic European call quotes exhibiting
    a mild volatility smile, suitable for calibration demos."""
    strikes = np.arange(S0 - 15, S0 + 15.1, 1.5)
    # Implied vols with a skew/smile pattern
    moneyness = strikes / S0
    ivs = 0.20 - 0.08 * (moneyness - 1.0) + 0.15 * (moneyness - 1.0) ** 2

    from scipy.stats import norm
    prices = []
    for K, iv in zip(strikes, ivs):
        d1 = (math.log(S0 / K) + (r + 0.5 * iv ** 2) * T) / (iv * math.sqrt(T))
        d2 = d1 - iv * math.sqrt(T)
        prices.append(
            S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2))

    return pd.DataFrame({
        'STRIKE': strikes,
        'MARKET_PRICE': prices,
        'IMP_VOL': ivs * 100,  # in percent
    })


# ══════════════════════════════════════════════════════════════════
#  Calibration Machinery
# ══════════════════════════════════════════════════════════════════

class JDCalibrator:
    """Two-stage calibrator for the Merton jump-diffusion model.

    Parameters
    ----------
    S0 : float – spot price
    r  : float – risk-free rate
    T  : float – time to maturity
    market_strikes : array – observed strike prices
    market_prices  : array – observed call prices
    I  : int   – MC paths per evaluation
    M  : int   – MC time steps
    """

    def __init__(self, S0, r, T, market_strikes, market_prices,
                 I=25_000, M=30):
        self.S0 = S0
        self.r = r
        self.T = T
        self.strikes = np.asarray(market_strikes)
        self.market = np.asarray(market_prices)
        self.I = I
        self.M = M
        self._eval_count = 0

    def _model_prices(self, params):
        """Compute model prices for all strikes given *params*."""
        sigma, lamb, mu_j, delta = params
        return np.array([
            jd_mcs_european_call(self.S0, K, self.T, self.r,
                                 sigma, lamb, mu_j, delta,
                                 I=self.I, M=self.M)
            for K in self.strikes
        ])

    def mse(self, params):
        """Mean squared error between model and market prices."""
        model = self._model_prices(params)
        err = np.sum((model - self.market) ** 2) / len(self.market)
        self._eval_count += 1
        if self._eval_count % 50 == 0 or self._eval_count == 1:
            print(f"  eval {self._eval_count:4d}  "
                  f"σ={params[0]:.3f}  λ={params[1]:.3f}  "
                  f"μ_J={params[2]:.3f}  δ={params[3]:.3f}  "
                  f"→ MSE={err:.4f}")
        return err

    def calibrate(self, verbose=True):
        """Run global + local optimisation.

        Returns
        -------
        opt_params : ndarray – [sigma, lambda, mu_j, delta]
        mse_value  : float
        """
        if verbose:
            print("Stage 1: Global grid search (brute) …")
        self._eval_count = 0
        opt_global = spo.brute(
            self.mse,
            ranges=(
                (0.05, 0.30, 0.05),   # sigma
                (0.10, 0.80, 0.10),   # lambda
                (-0.40, 0.01, 0.10),  # mu_j
                (0.00, 0.15, 0.03),   # delta
            ),
            finish=None)

        if verbose:
            mse_g = self.mse(opt_global)
            print(f"  → global optimum MSE = {mse_g:.4f}")
            print(f"    params: σ={opt_global[0]:.3f}, "
                  f"λ={opt_global[1]:.3f}, "
                  f"μ_J={opt_global[2]:.3f}, "
                  f"δ={opt_global[3]:.3f}")
            print("\nStage 2: Local refinement (Nelder-Mead) …")

        self._eval_count = 0
        opt_local = spo.fmin(
            self.mse, opt_global,
            xtol=1e-5, ftol=1e-5,
            maxiter=200, maxfun=500,
            disp=verbose)

        mse_val = self.mse(opt_local)
        return opt_local, mse_val


# ══════════════════════════════════════════════════════════════════
#  Visualisation
# ══════════════════════════════════════════════════════════════════

def plot_calibration_result(strikes, market_prices, model_prices):
    """Three-panel chart: prices, EUR errors, % errors."""
    errors_eur = model_prices - market_prices
    errors_pct = errors_eur / market_prices * 100

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True,
                                         figsize=(10, 9))
    ax1.plot(strikes, market_prices, 'b-o', ms=4, label='Market')
    ax1.plot(strikes, model_prices, 'r-s', ms=4, label='Model (JD)')
    ax1.set_ylabel('Call price')
    ax1.legend()
    ax1.grid(alpha=0.3)

    wi = (strikes[1] - strikes[0]) * 0.6
    ax2.bar(strikes, errors_eur, width=wi, alpha=0.7)
    ax2.set_ylabel('Error [price units]')
    ax2.axhline(0, color='k', lw=0.5)
    ax2.grid(alpha=0.3)

    ax3.bar(strikes, errors_pct, width=wi, alpha=0.7, color='C1')
    ax3.set_ylabel('Error [%]')
    ax3.set_xlabel('Strike')
    ax3.axhline(0, color='k', lw=0.5)
    ax3.grid(alpha=0.3)

    fig.suptitle('Jump-Diffusion Calibration Result', fontsize=13)
    plt.tight_layout()
    plt.show()

    print(f"Mean absolute error (EUR): {np.mean(np.abs(errors_eur)):.3f}")
    print(f"Mean absolute error (%):   {np.mean(np.abs(errors_pct)):.3f}")


# ══════════════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════════════

if __name__ == '__main__':

    S0, r, T = 100.0, 0.02, 0.25
    options = generate_synthetic_option_data(S0, r, T)
    print("Synthetic market data:")
    print(options.to_string(index=False))

    cal = JDCalibrator(
        S0, r, T,
        market_strikes=options['STRIKE'].values,
        market_prices=options['MARKET_PRICE'].values,
        I=20_000, M=25)

    opt_params, mse_val = cal.calibrate(verbose=True)
    print(f"\nCalibrated parameters:")
    print(f"  sigma  = {opt_params[0]:.4f}")
    print(f"  lambda = {opt_params[1]:.4f}")
    print(f"  mu_J   = {opt_params[2]:.4f}")
    print(f"  delta  = {opt_params[3]:.4f}")
    print(f"  MSE    = {mse_val:.6f}")

    # Compute final model prices at calibrated params
    model_prices = np.array([
        jd_mcs_european_call(S0, K, T, r,
                             opt_params[0], opt_params[1],
                             opt_params[2], opt_params[3],
                             I=50_000, M=50)
        for K in options['STRIKE'].values])

    plot_calibration_result(
        options['STRIKE'].values,
        options['MARKET_PRICE'].values,
        model_prices)
