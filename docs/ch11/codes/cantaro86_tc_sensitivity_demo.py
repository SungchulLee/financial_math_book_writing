#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_tc_sensitivity_demo.py
Transaction Cost Option Pricing: Sensitivity Analyses and Key Insights

Credits
-------
Based on notebook "4.1 Option pricing with transaction costs" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 11 -- Hedging & Transaction Costs).

Topics covered
--------------
1. Payoff modification under transaction costs (buy-side cost distortion).
2. Writer vs buyer indifference prices across spot prices.
3. Computational complexity of the DPZ binomial tree algorithm.
4. Drift sensitivity: why the physical drift mu matters when hedging
   is imperfect (unlike the drift-free Black-Scholes world).

See also: cantaro86_transaction_cost_pricer.py for the full TC_pricer class
and core algorithm description.
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time as timer
from scipy.stats import norm

# ============================================================================
# We import the TC_pricer and helpers from the companion module.
# If running standalone, place this file alongside
# cantaro86_transaction_cost_pricer.py in the same directory.
# ============================================================================
try:
    from cantaro86_transaction_cost_pricer import (
        TC_pricer, bs_call_price,
        terminal_no_option, terminal_writer, terminal_buyer,
    )
except ImportError:
    # Fallback: define minimal versions inline for standalone use
    import numpy.matlib

    def terminal_no_option(x, y, cost_b, cost_s):
        cost = np.zeros((len(x), len(y)))
        for i in range(len(y)):
            if y[i] <= 0:
                cost[:, i] = (1 + cost_b) * y[i] * np.exp(x)
            else:
                cost[:, i] = (1 - cost_s) * y[i] * np.exp(x)
        return cost

    def terminal_writer(x, y, cost_b, cost_s, K):
        cost = np.zeros((len(x), len(y)))
        for i in range(len(x)):
            for j in range(len(y)):
                S_i = np.exp(x[i])
                if y[j] < 0 and (1 + cost_b) * S_i <= K:
                    cost[i][j] = (1 + cost_b) * y[j] * S_i
                elif y[j] >= 0 and (1 + cost_b) * S_i <= K:
                    cost[i][j] = (1 - cost_s) * y[j] * S_i
                elif y[j] - 1 >= 0 and (1 + cost_b) * S_i > K:
                    cost[i][j] = (1 - cost_s) * (y[j] - 1) * S_i + K
                elif y[j] - 1 < 0 and (1 + cost_b) * S_i > K:
                    cost[i][j] = (1 + cost_b) * (y[j] - 1) * S_i + K
        return cost

    def terminal_buyer(x, y, cost_b, cost_s, K):
        cost = np.zeros((len(x), len(y)))
        for i in range(len(x)):
            for j in range(len(y)):
                S_i = np.exp(x[i])
                if y[j] < 0 and (1 + cost_b) * S_i <= K:
                    cost[i][j] = (1 + cost_b) * y[j] * S_i
                elif y[j] >= 0 and (1 + cost_b) * S_i <= K:
                    cost[i][j] = (1 - cost_s) * y[j] * S_i
                elif y[j] + 1 >= 0 and (1 + cost_b) * S_i > K:
                    cost[i][j] = (1 - cost_s) * (y[j] + 1) * S_i - K
                elif y[j] + 1 < 0 and (1 + cost_b) * S_i > K:
                    cost[i][j] = (1 + cost_b) * (y[j] + 1) * S_i - K
        return cost

    class TC_pricer:
        def __init__(self, S0, K, T, r, mu, sig, cost_b=0.0, cost_s=0.0, gamma=0.001):
            self.S0 = S0
            self.K = K
            self.T = T
            self.r = r
            self.mu = mu
            self.sig = sig
            self.cost_b = cost_b
            self.cost_s = cost_s
            self.gamma = gamma

        def price(self, N=500, TYPE="writer", verbose=False):
            t_start = timer()
            np.seterr(all="ignore")
            x0 = np.log(self.S0)
            T_vec, dt = np.linspace(0, self.T, N + 1, retstep=True)
            delta = np.exp(-self.r * (self.T - T_vec))
            dx = self.sig * np.sqrt(dt)
            dy = dx
            M = int(np.floor(N / 2))
            y = np.linspace(-M * dy, M * dy, 2 * M + 1)
            N_y = len(y)
            med = np.where(y == 0)[0].item()

            def F(xx, ll, nn):
                return np.exp(self.gamma * (1 + self.cost_b) * np.exp(xx) * ll / delta[nn])

            def G(xx, mm, nn):
                return np.exp(-self.gamma * (1 - self.cost_s) * np.exp(xx) * mm / delta[nn])

            for portfolio in ["no_opt", TYPE]:
                x = np.array([
                    x0 + (self.mu - 0.5 * self.sig**2) * dt * N + (2 * i - N) * dx
                    for i in range(N + 1)
                ])
                if portfolio == "no_opt":
                    Q = np.exp(-self.gamma * terminal_no_option(x, y, self.cost_b, self.cost_s))
                elif portfolio == "writer":
                    Q = np.exp(-self.gamma * terminal_writer(x, y, self.cost_b, self.cost_s, self.K))
                elif portfolio == "buyer":
                    Q = np.exp(-self.gamma * terminal_buyer(x, y, self.cost_b, self.cost_s, self.K))

                for k in range(N - 1, -1, -1):
                    Q_new = (Q[:-1, :] + Q[1:, :]) / 2.0
                    x = np.array([
                        x0 + (self.mu - 0.5 * self.sig**2) * dt * k + (2 * i - k) * dx
                        for i in range(k + 1)
                    ])
                    Buy = np.copy(Q_new)
                    Buy[:, :-1] = np.matlib.repmat(F(x, dy, k), N_y - 1, 1).T * Q_new[:, 1:]
                    Sell = np.copy(Q_new)
                    Sell[:, 1:] = np.matlib.repmat(G(x, dy, k), N_y - 1, 1).T * Q_new[:, :-1]
                    Q = np.minimum(np.minimum(Buy, Sell), Q_new)

                if portfolio == "no_opt":
                    Q_no = Q[0, med]
                else:
                    Q_yes = Q[0, med]

            if TYPE == "writer":
                price = (delta[0] / self.gamma) * np.log(Q_yes / Q_no)
            else:
                price = (delta[0] / self.gamma) * np.log(Q_no / Q_yes)

            elapsed = timer() - t_start
            if verbose:
                return price, elapsed
            return price

    def bs_call_price(S0, K, T, r, sigma):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


# ============================================================================
# 1. PAYOFF WITH TRANSACTION COSTS
# ============================================================================

def plot_payoff_with_tc(K=15, cost_b=0.01):
    """
    Show how proportional transaction costs distort the call payoff.

    With buy-side cost lambda, the effective payoff becomes:
        max((1 + lambda) * S - K, 0)
    The exercise threshold shifts from K to K / (1 + lambda).

    Parameters
    ----------
    K : float      Strike price.
    cost_b : float Proportional buy cost (lambda).
    """
    S = np.linspace(K - 1, K + 1, 500)
    payoff_zero = np.maximum(S - K, 0)
    payoff_tc = np.maximum(S * (1 + cost_b) - K, 0)

    plt.figure(figsize=(10, 5))
    plt.plot(S, payoff_zero, color="blue", linewidth=2, label="Zero-cost payoff")
    plt.plot(S, payoff_tc, color="red", linewidth=2, label=f"With TC (λ={cost_b})")
    plt.axvline(x=K, color="grey", ls="--", alpha=0.5, label=f"K = {K}")
    plt.axvline(x=K / (1 + cost_b), color="red", ls=":", alpha=0.5,
                label=f"K/(1+λ) = {K / (1 + cost_b):.4f}")
    plt.xlabel("S")
    plt.ylabel("Payoff")
    plt.title("Call Payoff: Zero Transaction Costs vs Proportional Costs")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ============================================================================
# 2. WRITER vs BUYER PRICE ACROSS SPOT PRICES
# ============================================================================

def price_vs_spot(K=15, T=1, r=0.1, mu=0.1, sigma=0.25, gamma=0.0001,
                  cost=0.05, N=400, S_range=None):
    """
    Compare writer and buyer indifference prices across spot levels.

    Key insight: the writer charges MORE than BS (compensation for
    hedging costs), and the buyer pays LESS than BS (accounts for
    imperfect replication). The BS price lies between them.

    Parameters
    ----------
    K : float      Strike.
    T : float      Maturity.
    r : float      Risk-free rate.
    mu : float     Physical drift.
    sigma : float  Volatility.
    gamma : float  Risk aversion.
    cost : float   Proportional transaction cost (both sides).
    N : int        Binomial tree steps.
    S_range : list Spot prices to scan.

    Returns
    -------
    dict with spot prices, writer/buyer/zero-cost/BS prices.
    """
    if S_range is None:
        S_range = list(range(int(K - 10), int(K + 6)))

    price_zero = []
    price_writer = []
    price_buyer = []

    for S0 in S_range:
        # Zero-cost prices
        pricer = TC_pricer(S0, K, T, r, mu, sigma,
                           cost_b=0, cost_s=0, gamma=gamma)
        price_zero.append(pricer.price(N=N, TYPE="writer"))

        # Prices with transaction costs
        pricer = TC_pricer(S0, K, T, r, mu, sigma,
                           cost_b=cost, cost_s=cost, gamma=gamma)
        price_writer.append(pricer.price(N=N, TYPE="writer"))
        price_buyer.append(pricer.price(N=N, TYPE="buyer"))

    # BS reference
    bs_prices = [bs_call_price(s, K, T, r, sigma) for s in S_range]

    plt.figure(figsize=(10, 5))
    plt.plot(S_range, price_zero, "bs-", label="Zero TC", markersize=5)
    plt.plot(S_range, price_writer, "go-", label=f"Writer (cost={cost})", markersize=5)
    plt.plot(S_range, price_buyer, "m*-", label=f"Buyer (cost={cost})", markersize=5)
    plt.plot(S_range, bs_prices, "r--", linewidth=1.5, label="Black-Scholes")
    plt.xlabel("Spot price S")
    plt.ylabel("Option price")
    plt.title(f"Indifference Prices vs Spot (K={K}, γ={gamma}, cost={cost})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return {
        "S_range": S_range,
        "zero": price_zero,
        "writer": price_writer,
        "buyer": price_buyer,
        "bs": bs_prices,
    }


# ============================================================================
# 3. TIME COMPLEXITY ANALYSIS
# ============================================================================

def time_complexity(S0=15, K=15, T=1, r=0.1, mu=0.1, sigma=0.25,
                    gamma=0.0001, N_values=None):
    """
    Measure wall-clock time vs binomial tree size N.

    The DPZ algorithm uses a tree in (log-price, stock-holding) space:
      - At step k: (k+1) log-price nodes x (2*M+1) holding nodes
      - M = floor(N/2), so total work ~ O(N^2 * N) per step
      - With N backward steps: overall O(N^3)... but the holding grid
        grows linearly with N, so effectively O(N^2) per pricing call.

    Parameters
    ----------
    S0, K, T, r, mu, sigma, gamma : float  Model parameters.
    N_values : list  Tree sizes to test.

    Returns
    -------
    dict with N_values, prices, times, and estimated exponent.
    """
    if N_values is None:
        N_values = [50 * 2**i for i in range(7)]  # 50, 100, ..., 3200

    pricer = TC_pricer(S0, K, T, r, mu, sigma, cost_b=0, cost_s=0, gamma=gamma)
    prices = []
    times = []

    print(f"  {'N':>6s}  {'Price':>12s}  {'Time (s)':>10s}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*10}")

    for N in N_values:
        p, t = pricer.price(N=N, TYPE="writer", verbose=True)
        prices.append(p)
        times.append(t)
        print(f"  {N:>6d}  {p:>12.6f}  {t:>10.4f}")

    # Estimate scaling exponent: time ~ N^alpha
    if len(times) >= 2 and times[-1] > 0 and times[-2] > 0:
        alpha = np.log2(times[-1] / times[-2])
        print(f"\n  Estimated exponent (last two points): alpha ≈ {alpha:.2f}")
        print(f"  (Expected: ~2 for O(N^2) complexity)")

    return {"N_values": N_values, "prices": prices, "times": times}


# ============================================================================
# 4. DRIFT SENSITIVITY: WHY mu MATTERS WITH TRANSACTION COSTS
# ============================================================================

def drift_sensitivity(S0=15, K=15, T=1, r=0.1, sigma=0.25,
                      gamma=1.0, cost=0.01, N=400, mu_values=None):
    """
    Show that the physical drift mu affects option prices under
    transaction costs (unlike the drift-free Black-Scholes world).

    In Black-Scholes, the drift cancels out via risk-neutral pricing.
    With transaction costs and utility-based pricing, the drift matters
    because:
      1. Hedging is imperfect (not continuous).
      2. The agent uses exponential utility, and the drift affects
         the expected terminal wealth.
      3. Higher drift makes the stock more attractive, affecting
         the hedging strategy and thus the option's indifference price.

    This effect is most visible with HIGH risk aversion (large gamma),
    where the agent's utility is strongly sensitive to the drift.

    Parameters
    ----------
    S0, K, T, r, sigma : float  Market parameters.
    gamma : float  Risk aversion (use high value, e.g. 1.0).
    cost : float   Proportional transaction cost.
    N : int        Tree steps.
    mu_values : list  Physical drift values to scan.

    Returns
    -------
    dict with mu_values, writer prices, buyer prices.
    """
    if mu_values is None:
        mu_values = [0.01, 0.05, 0.1, 0.2, 0.3]

    writer_prices = []
    buyer_prices = []

    print(f"  Parameters: S0={S0}, K={K}, gamma={gamma}, cost={cost}")
    print(f"\n  {'mu':>8s}  {'Writer':>10s}  {'Buyer':>10s}  {'Spread':>10s}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*10}")

    for mu in mu_values:
        pricer = TC_pricer(S0, K, T, r, mu, sigma,
                           cost_b=cost, cost_s=cost, gamma=gamma)
        pw = pricer.price(N=N, TYPE="writer")
        pb = pricer.price(N=N, TYPE="buyer")
        writer_prices.append(pw)
        buyer_prices.append(pb)
        print(f"  {mu:>8.3f}  {pw:>10.4f}  {pb:>10.4f}  {pw - pb:>10.4f}")

    bs_ref = bs_call_price(S0, K, T, r, sigma)

    plt.figure(figsize=(10, 5))
    plt.plot(mu_values, writer_prices, "go-", label="Writer", markersize=8)
    plt.plot(mu_values, buyer_prices, "m*-", label="Buyer", markersize=8)
    plt.axhline(y=bs_ref, color="r", ls="--", label=f"BS price = {bs_ref:.4f}")
    plt.xlabel("Physical drift μ")
    plt.ylabel("Indifference price")
    plt.title(f"Drift Sensitivity (γ={gamma}, cost={cost})\n"
              "Unlike BS, drift matters with transaction costs!")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return {"mu_values": mu_values, "writer": writer_prices, "buyer": buyer_prices}


# ============================================================================
# 5. GAMMA (RISK AVERSION) SENSITIVITY WITH VISUALISATION
# ============================================================================

def gamma_sensitivity(S0=15, K=15, T=1, r=0.1, mu=0.1, sigma=0.25,
                      cost=0.01, N=400, gamma_values=None):
    """
    Show how risk aversion gamma affects the bid-ask spread.

    Higher gamma means the agent is more risk-averse, leading to:
      - Higher writer price (demands more compensation).
      - Lower buyer price (willing to pay less).
      - Wider bid-ask spread.

    Parameters
    ----------
    S0, K, T, r, mu, sigma : float  Market parameters.
    cost : float   Proportional transaction cost.
    N : int        Tree steps.
    gamma_values : list  Risk aversion levels to scan.

    Returns
    -------
    dict with gamma_values, writer prices, buyer prices.
    """
    if gamma_values is None:
        gamma_values = [0.0001, 0.001, 0.01, 0.05, 0.1, 0.3, 0.5]

    writer_prices = []
    buyer_prices = []

    print(f"  Parameters: S0={S0}, K={K}, cost={cost}")
    print(f"\n  {'gamma':>10s}  {'Writer':>10s}  {'Buyer':>10s}  {'Spread':>10s}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

    for gamma in gamma_values:
        pricer = TC_pricer(S0, K, T, r, mu, sigma,
                           cost_b=cost, cost_s=cost, gamma=gamma)
        pw = pricer.price(N=N, TYPE="writer")
        pb = pricer.price(N=N, TYPE="buyer")
        writer_prices.append(pw)
        buyer_prices.append(pb)
        print(f"  {gamma:>10.4f}  {pw:>10.4f}  {pb:>10.4f}  {pw - pb:>10.4f}")

    bs_ref = bs_call_price(S0, K, T, r, sigma)

    plt.figure(figsize=(10, 5))
    plt.plot(gamma_values, writer_prices, "go-", label="Writer", markersize=8)
    plt.plot(gamma_values, buyer_prices, "m*-", label="Buyer", markersize=8)
    plt.axhline(y=bs_ref, color="r", ls="--", label=f"BS price = {bs_ref:.4f}")
    plt.xlabel("Risk aversion γ")
    plt.ylabel("Indifference price")
    plt.title(f"Gamma Sensitivity (cost={cost})\n"
              "Higher risk aversion widens the bid-ask spread")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return {"gamma_values": gamma_values, "writer": writer_prices, "buyer": buyer_prices}


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all TC sensitivity demonstrations."""
    S0, K, T, r, mu, sigma = 15.0, 15.0, 1.0, 0.1, 0.1, 0.25

    # 1. Payoff distortion
    print("=" * 60)
    print("1. Payoff Distortion Under Transaction Costs")
    print("=" * 60)
    plot_payoff_with_tc(K=K, cost_b=0.01)

    # 2. Price vs spot
    print("\n" + "=" * 60)
    print("2. Writer vs Buyer Indifference Prices Across Spot")
    print("=" * 60)
    price_vs_spot(K=K, T=T, r=r, mu=mu, sigma=sigma,
                  gamma=0.0001, cost=0.05, N=400)

    # 3. Time complexity
    print("\n" + "=" * 60)
    print("3. Computational Complexity of the DPZ Algorithm")
    print("=" * 60)
    time_complexity(S0=S0, K=K, T=T, r=r, mu=mu, sigma=sigma,
                    gamma=0.0001, N_values=[50, 100, 200, 400, 800])

    # 4. Gamma sensitivity with plot
    print("\n" + "=" * 60)
    print("4. Risk Aversion (γ) Sensitivity")
    print("=" * 60)
    gamma_sensitivity(S0=S0, K=K, T=T, r=r, mu=mu, sigma=sigma,
                      cost=0.01, N=400)

    # 5. Drift sensitivity (key insight!)
    print("\n" + "=" * 60)
    print("5. Drift Sensitivity: Why μ Matters with Transaction Costs")
    print("=" * 60)
    print("  (Using high gamma = 1.0 to make the effect visible)")
    drift_sensitivity(S0=S0, K=K, T=T, r=r, sigma=sigma,
                      gamma=1.0, cost=0.01, N=400)

    print("\n" + "=" * 60)
    print("SUMMARY OF KEY INSIGHTS")
    print("=" * 60)
    print("  1. Transaction costs distort the payoff -- the effective exercise")
    print("     threshold shifts from K to K/(1+λ).")
    print("  2. Writer charges more than BS; buyer pays less. The BS price")
    print("     lies between the two indifference prices.")
    print("  3. The DPZ algorithm has O(N^2) complexity in the tree size N.")
    print("  4. Higher risk aversion (γ) widens the bid-ask spread, because")
    print("     the more risk-averse agent demands more/pays less.")
    print("  5. Unlike Black-Scholes, the physical drift μ MATTERS under")
    print("     transaction costs (especially with high γ), because hedging")
    print("     is no longer continuous and the drift affects expected utility.")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
