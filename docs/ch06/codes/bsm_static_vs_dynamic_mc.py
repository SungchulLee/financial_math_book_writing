"""
Bsm Static Vs Dynamic Mc

Educational script demonstrating bsm static vs dynamic mc concepts.
"""

# ---
# title: "BSM Static vs Dynamic Monte Carlo Comparison"
# description: >
#   Compares two Monte Carlo approaches for European option pricing:
#     1. Static MC — simulate only the terminal value S(T) in one step.
#     2. Dynamic MC — simulate full paths with M time steps.
#   Both methods use antithetic variates and moment matching for
#   variance reduction.  Results are benchmarked against the
#   closed-form Black-Scholes-Merton value.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import math
import numpy as np
import numpy.random as npr
import scipy.stats as scs
import matplotlib.pyplot as plt

# ======================================================================
# ── Variance-reduction random-number generator ───────────────────
def gen_sn(M, I, anti_paths=True, mo_match=True):
    """Generate standard-normal random numbers with optional
    antithetic variates and moment matching.

    Parameters
    ----------
    M : int
        Number of time intervals for discretisation.
    I : int
        Number of paths to simulate.
    anti_paths : bool
        Use antithetic variates (default True).
    mo_match : bool
        Apply moment matching so mean=0, std=1 (default True).

    Returns
    -------
    sn : ndarray, shape (M+1, I)
    """
    if anti_paths:
        sn = npr.standard_normal((M + 1, int(I / 2)))
        sn = np.concatenate((sn, -sn), axis=1)
    else:
        sn = npr.standard_normal((M + 1, I))
    if mo_match:
        sn = (sn - sn.mean()) / sn.std()
    return sn


# ── Closed-form BSM call value (for benchmarking) ────────────────
def bsm_call_value(S0, K, T, r, sigma):
    """Analytical Black-Scholes-Merton European call price."""
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (
        sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S0 * scs.norm.cdf(d1) - K * math.exp(-r * T) * scs.norm.cdf(d2)


# ── Static MC: simulate only S(T) ────────────────────────────────
def gbm_mcs_static(S0, K, T, r, sigma, I):
    """European call value via static (one-step) Monte Carlo.

    Draws S(T) directly from the log-normal distribution of GBM.
    """
    sn = gen_sn(1, I)
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T
                     + sigma * math.sqrt(T) * sn[1])
    payoff = np.maximum(ST - K, 0)
    return math.exp(-r * T) * np.mean(payoff)


# ── Dynamic MC: simulate full path with M steps ──────────────────
def gbm_mcs_dynamic(S0, K, T, r, sigma, I, M=50, option='call'):
    """European option value via dynamic (multi-step) Monte Carlo.

    Simulates full GBM paths with *M* Euler steps, then computes
    the discounted expected payoff at maturity.

    Parameters
    ----------
    option : str
        ``'call'`` or ``'put'``.
    """
    dt = T / M
    S = np.zeros((M + 1, I))
    S[0] = S0
    sn = gen_sn(M, I)
    for t in range(1, M + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt
                                 + sigma * math.sqrt(dt) * sn[t])
    if option == 'call':
        payoff = np.maximum(S[-1] - K, 0)
    else:
        payoff = np.maximum(K - S[-1], 0)
    return math.exp(-r * T) * np.mean(payoff)


# ── Longstaff-Schwartz LSM for American options ──────────────────
def gbm_mcs_american(S0, K, T, r, sigma, I, M=50, option='call'):
    """American option value via Least-Squares Monte Carlo (LSM).

    Uses polynomial regression (degree 7) to estimate the
    continuation value at each exercise date.
    """
    dt = T / M
    df = math.exp(-r * dt)
    S = np.zeros((M + 1, I))
    S[0] = S0
    sn = gen_sn(M, I)
    for t in range(1, M + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt
                                 + sigma * math.sqrt(dt) * sn[t])
    if option == 'call':
        h = np.maximum(S - K, 0)
    else:
        h = np.maximum(K - S, 0)

    # Backward induction
    V = np.copy(h)
    for t in range(M - 1, 0, -1):
        reg = np.polyfit(S[t], V[t + 1] * df, 7)
        C = np.polyval(reg, S[t])
        V[t] = np.where(C > h[t], V[t + 1] * df, h[t])

    return df * np.mean(V[1])


# ── Main comparison ──────────────────────────────────────────────
if __name__ == '__main__':

    # Parameters
    S0 = 100.0
    r = 0.05
    sigma = 0.25
    T = 1.0
    I = 50_000
    M = 50

    np.random.seed(100)

    k_list = np.arange(80.0, 120.1, 5.0)
    stat_res, dyna_res, anal_res = [], [], []

    for K in k_list:
        stat_res.append(gbm_mcs_static(S0, K, T, r, sigma, I))
        dyna_res.append(gbm_mcs_dynamic(S0, K, T, r, sigma, I, M))
        anal_res.append(bsm_call_value(S0, K, T, r, sigma))

    stat_res = np.array(stat_res)
    dyna_res = np.array(dyna_res)
    anal_res = np.array(anal_res)

    # ── Figure 1: Static MC vs analytical ─────────────────────────
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    ax1.plot(k_list, anal_res, 'b', label='Analytical BSM')
    ax1.plot(k_list, stat_res, 'ro', label='Static MC')
    ax1.set_ylabel('European call value')
    ax1.legend(loc='best')
    ax1.set_ylim(bottom=0)
    ax1.grid(alpha=0.3)

    wi = 1.0
    ax2.bar(k_list - wi / 2,
            (anal_res - stat_res) / anal_res * 100, wi)
    ax2.set_xlabel('Strike')
    ax2.set_ylabel('Relative error [%]')
    ax2.set_xlim(left=75, right=125)
    ax2.grid(alpha=0.3)
    fig.suptitle('Static Monte Carlo vs BSM Analytical', fontsize=13)
    plt.tight_layout()
    plt.show()

    # ── Figure 2: Dynamic MC vs analytical ────────────────────────
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    ax1.plot(k_list, anal_res, 'b', label='Analytical BSM')
    ax1.plot(k_list, dyna_res, 'ro', label='Dynamic MC')
    ax1.set_ylabel('European call value')
    ax1.legend(loc='best')
    ax1.set_ylim(bottom=0)
    ax1.grid(alpha=0.3)

    ax2.bar(k_list - wi / 2,
            (anal_res - dyna_res) / anal_res * 100, wi)
    ax2.set_xlabel('Strike')
    ax2.set_ylabel('Relative error [%]')
    ax2.set_xlim(left=75, right=125)
    ax2.grid(alpha=0.3)
    fig.suptitle('Dynamic Monte Carlo vs BSM Analytical', fontsize=13)
    plt.tight_layout()
    plt.show()

    # ── Figure 3: European vs American puts ───────────────────────
    euro_puts, amer_puts = [], []
    for K in k_list:
        euro_puts.append(
            gbm_mcs_dynamic(S0, K, T, r, sigma, I, M, option='put'))
        amer_puts.append(
            gbm_mcs_american(S0, K, T, r, sigma, I, M, option='put'))

    euro_puts = np.array(euro_puts)
    amer_puts = np.array(amer_puts)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    ax1.plot(k_list, euro_puts, 'b', label='European put')
    ax1.plot(k_list, amer_puts, 'ro', label='American put (LSM)')
    ax1.set_ylabel('Put option value')
    ax1.legend(loc='best')
    ax1.grid(alpha=0.3)

    ax2.bar(k_list - wi / 2,
            (amer_puts - euro_puts) / euro_puts * 100, wi)
    ax2.set_xlabel('Strike')
    ax2.set_ylabel('Early exercise premium [%]')
    ax2.set_xlim(left=75, right=125)
    ax2.grid(alpha=0.3)
    fig.suptitle('European vs American Put (LSM)', fontsize=13)
    plt.tight_layout()
    plt.show()
