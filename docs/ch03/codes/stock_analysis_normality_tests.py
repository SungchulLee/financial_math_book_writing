# ---
# title: "Normality Tests on Log-Returns"
# description: >
#   Investigates whether log-returns of simulated GBM paths and
#   real equity data follow a normal distribution.
#     1. Simulates GBM paths and verifies that single-step
#        log-returns are indeed normal (benchmark case).
#     2. Downloads historical prices for SPY, GLD, AAPL, MSFT
#        and applies the skewness test, kurtosis test, and
#        D'Agostino-Pearson omnibus test.
#     3. Produces Q-Q plots and histograms with fitted PDFs.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import math
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt

# ── GBM path generator with moment matching ──────────────────────
def gen_paths(S0, r, sigma, T, M, I):
    """Generate Monte Carlo paths for geometric Brownian motion.

    Parameters
    ----------
    S0 : float   — initial stock/index value
    r  : float   — constant short rate
    sigma : float — constant volatility
    T  : float   — time horizon (years)
    M  : int     — number of time steps
    I  : int     — number of paths

    Returns
    -------
    paths : ndarray, shape (M+1, I)
    """
    dt = T / M
    paths = np.zeros((M + 1, I))
    paths[0] = S0
    for t in range(1, M + 1):
        rand = np.random.standard_normal(I)
        rand = (rand - rand.mean()) / rand.std()          # moment matching
        paths[t] = paths[t - 1] * np.exp(
            (r - 0.5 * sigma ** 2) * dt
            + sigma * math.sqrt(dt) * rand)
    return paths


# ── Descriptive statistics printer ────────────────────────────────
def print_statistics(array):
    """Print selected descriptive statistics."""
    sta = scs.describe(array)
    print(f"{'statistic':>14s} {'value':>15s}")
    print('-' * 30)
    print(f"{'size':>14s} {sta.nobs:15.5f}")
    print(f"{'min':>14s} {sta.minmax[0]:15.5f}")
    print(f"{'max':>14s} {sta.minmax[1]:15.5f}")
    print(f"{'mean':>14s} {sta.mean:15.5f}")
    print(f"{'std':>14s} {np.sqrt(sta.variance):15.5f}")
    print(f"{'skew':>14s} {sta.skewness:15.5f}")
    print(f"{'kurtosis':>14s} {sta.kurtosis:15.5f}")


# ── Normality test battery ────────────────────────────────────────
def normality_tests(arr):
    """Run skewness, kurtosis, and D'Agostino-Pearson tests.

    Parameters
    ----------
    arr : array-like
        Sample of observations.

    Returns
    -------
    results : dict
        Keys: 'skew', 'skew_p', 'kurt', 'kurt_p', 'normaltest_p'.
    """
    skew = scs.skew(arr)
    skew_p = scs.skewtest(arr)[1]
    kurt = scs.kurtosis(arr)
    kurt_p = scs.kurtosistest(arr)[1]
    norm_p = scs.normaltest(arr)[1]

    print(f"Skewness           {skew:14.3f}")
    print(f"Skew test p-value  {skew_p:14.3f}")
    print(f"Kurtosis (excess)  {kurt:14.3f}")
    print(f"Kurt test p-value  {kurt_p:14.3f}")
    print(f"Normal test p-val  {norm_p:14.3f}")

    return dict(skew=skew, skew_p=skew_p, kurt=kurt,
                kurt_p=kurt_p, normaltest_p=norm_p)


# ── Main ──────────────────────────────────────────────────────────
if __name__ == '__main__':

    np.random.seed(1000)

    # ========== Part 1: Benchmark — simulated GBM =================
    S0, r, sigma, T, M, I = 100.0, 0.05, 0.2, 1.0, 50, 250_000
    paths = gen_paths(S0, r, sigma, T, M, I)
    log_returns = np.log(paths[1:] / paths[:-1])

    print("=" * 50)
    print("Part 1 — Simulated GBM log-returns (benchmark)")
    print("=" * 50)
    print_statistics(log_returns.flatten())
    print()
    print("Annualised mean  :",
          round(log_returns.mean() * M + 0.5 * sigma ** 2, 6))
    print("Annualised vol   :",
          round(log_returns.std() * math.sqrt(M), 6))
    print()
    normality_tests(log_returns.flatten())

    # Histogram of log-returns with fitted normal PDF
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(log_returns.flatten(), bins=70, density=True,
            alpha=0.7, label='Simulated log-returns')
    x = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 200)
    ax.plot(x, scs.norm.pdf(x, loc=r / M, scale=sigma / np.sqrt(M)),
            'r', lw=2.0, label='Theoretical N(μ, σ)')
    ax.set_xlabel('Log-return')
    ax.set_ylabel('Density')
    ax.set_title('GBM Log-Returns vs Normal PDF (Benchmark)')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Q-Q plot
    fig, ax = plt.subplots(figsize=(8, 6))
    scs.probplot(log_returns.flatten()[::500], dist='norm', plot=ax)
    ax.set_title('Q-Q Plot — Simulated GBM Log-Returns')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Terminal distribution: raw vs log
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.hist(paths[-1], bins=30, alpha=0.7)
    ax1.set_xlabel('S(T)')
    ax1.set_title('Terminal Price (log-normal)')
    ax1.grid(alpha=0.3)
    ax2.hist(np.log(paths[-1]), bins=30, alpha=0.7)
    ax2.set_xlabel('log S(T)')
    ax2.set_title('Log Terminal Price (normal)')
    ax2.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    print("\nNormality tests on log(S_T):")
    normality_tests(np.log(paths[-1]))

    # ========== Part 2: Real market data (synthetic demo) =========
    #
    # The original notebook uses a CSV from Refinitiv Eikon.
    # Here we generate synthetic correlated returns as a
    # stand-alone demonstration of the same analysis pipeline.
    # Replace the block below with real data for production use.
    #
    print("\n" + "=" * 50)
    print("Part 2 — Synthetic 'market' returns")
    print("=" * 50)

    n_days = 2000
    symbols = ['Asset_A', 'Asset_B', 'Asset_C', 'Asset_D']

    # Simulate returns with realistic kurtosis via t-distribution
    np.random.seed(42)
    dfs = [5, 6, 4, 7]               # degrees of freedom (fat tails)
    vols = [0.01, 0.012, 0.016, 0.014]
    synth_returns = {}
    for sym, df, vol in zip(symbols, dfs, vols):
        raw = np.random.standard_t(df, size=n_days) * vol
        synth_returns[sym] = raw

    for sym in symbols:
        arr = synth_returns[sym]
        print(f"\nResults for {sym}")
        print('-' * 32)
        print_statistics(arr)
        print()
        normality_tests(arr)

    # Q-Q plots for each asset
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    for ax, sym in zip(axes.flatten(), symbols):
        scs.probplot(synth_returns[sym], dist='norm', plot=ax)
        ax.set_title(f'Q-Q Plot — {sym}')
        ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Histograms
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    for ax, sym in zip(axes.flatten(), symbols):
        ax.hist(synth_returns[sym], bins=50, density=True, alpha=0.7)
        ax.set_title(sym)
        ax.set_xlabel('log-return')
        ax.grid(alpha=0.3)
    fig.suptitle('Return Distributions (fat tails expected)', fontsize=13)
    plt.tight_layout()
    plt.show()
