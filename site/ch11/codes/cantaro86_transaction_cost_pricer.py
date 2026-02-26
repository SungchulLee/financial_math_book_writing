#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_transaction_cost_pricer.py
====================================
Option Pricing with Transaction Costs using the
Davis-Panas-Zariphopoulou (DPZ) Model.

Based on TC_pricer.py and cost_utils.py from:
    cantaro86 - Financial-Models-Numerical-Methods
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

The DPZ Model:
    In the classical Black-Scholes world, continuous delta-hedging is
    cost-free.  In reality, each rebalancing trade incurs a transaction
    cost (bid-ask spread, commissions, market impact).

    Davis, Panas and Zariphopoulou (1993) introduced a utility-based
    framework where the agent maximises expected exponential utility:
        U(W) = -exp(-gamma * W)
    subject to proportional transaction costs:
        - cost_b (lambda): proportional BUY cost
        - cost_s (mu):     proportional SELL cost

    The option price is defined as the indifference price: the amount p
    such that the agent is indifferent between:
        (a) optimal investment without the option
        (b) writing (or buying) the option for price p and hedging optimally

    The algorithm uses a binomial tree in (log-price, stock-holding) space
    and backward induction with three possible actions at each node:
        - Buy shares   (increase holdings by dy)
        - Sell shares   (decrease holdings by dy)
        - Do nothing   (hold current position)

Key References:
    - Davis, M.H.A., Panas, V.G., Zariphopoulou, T. (1993).
      "European option pricing with transaction costs."
      SIAM J. Control Optim., 31(2), 470-493.
    - Hodges, S.D., Neuberger, A. (1989).
      "Optimal replication of contingent claims under transaction costs."
      Rev. Futures Markets, 8, 222-239.

License: MIT (see original repository)
"""

import numpy as np
import numpy.matlib
from time import time as timer


# ============================================================================
# Terminal Condition Utilities
# ============================================================================
# These functions compute the terminal wealth at expiry for different
# portfolio scenarios.  x = log(S), y = number of shares held.
#
# At expiry the agent must liquidate the stock position:
#   - Selling y shares (y>0) incurs cost:  (1 - cost_s) * y * S
#   - Buying to close y shares (y<0):      (1 + cost_b) * y * S  (negative cost = payment)

def terminal_no_option(x, y, cost_b, cost_s):
    """
    Terminal wealth when the agent holds NO option.

    Parameters
    ----------
    x : ndarray, shape (n_x,)
        Log-prices at terminal nodes.
    y : ndarray, shape (n_y,)
        Stock holdings grid.
    cost_b : float
        Proportional buy cost (lambda).
    cost_s : float
        Proportional sell cost (mu).

    Returns
    -------
    cost : ndarray, shape (n_x, n_y)
        Terminal wealth matrix.
    """
    cost = np.zeros((len(x), len(y)))
    for i in range(len(y)):
        if y[i] <= 0:
            # Short position: must buy to close --> pay (1+cost_b)*|y|*S
            cost[:, i] = (1 + cost_b) * y[i] * np.exp(x)
        else:
            # Long position: sell shares --> receive (1-cost_s)*y*S
            cost[:, i] = (1 - cost_s) * y[i] * np.exp(x)
    return cost


def terminal_writer(x, y, cost_b, cost_s, K):
    """
    Terminal wealth for an agent who has WRITTEN (sold) a call option
    with strike K.

    At expiry:
        - If S <= K: option expires worthless, liquidate stock holdings
        - If S > K:  option is exercised, must deliver 1 share at price K,
                     so effective holdings become (y-1)
    """
    cost = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            S_i = np.exp(x[i])
            if y[j] < 0 and (1 + cost_b) * S_i <= K:
                # OTM, short stock
                cost[i][j] = (1 + cost_b) * y[j] * S_i
            elif y[j] >= 0 and (1 + cost_b) * S_i <= K:
                # OTM, long stock
                cost[i][j] = (1 - cost_s) * y[j] * S_i
            elif y[j] - 1 >= 0 and (1 + cost_b) * S_i > K:
                # ITM, long enough stock (y-1 >= 0)
                cost[i][j] = (1 - cost_s) * (y[j] - 1) * S_i + K
            elif y[j] - 1 < 0 and (1 + cost_b) * S_i > K:
                # ITM, not enough stock (y-1 < 0)
                cost[i][j] = (1 + cost_b) * (y[j] - 1) * S_i + K
    return cost


def terminal_buyer(x, y, cost_b, cost_s, K):
    """
    Terminal wealth for an agent who has BOUGHT a call option with strike K.

    At expiry:
        - If S <= K: option expires worthless, liquidate stock holdings
        - If S > K:  option is exercised, receive 1 share at price K,
                     so effective holdings become (y+1)
    """
    cost = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            S_i = np.exp(x[i])
            if y[j] < 0 and (1 + cost_b) * S_i <= K:
                cost[i][j] = (1 + cost_b) * y[j] * S_i
            elif y[j] >= 0 and (1 + cost_b) * S_i <= K:
                cost[i][j] = (1 - cost_s) * y[j] * S_i
            elif y[j] + 1 >= 0 and (1 + cost_b) * S_i > K:
                # ITM, long position after exercise (y+1 >= 0)
                cost[i][j] = (1 - cost_s) * (y[j] + 1) * S_i - K
            elif y[j] + 1 < 0 and (1 + cost_b) * S_i > K:
                # ITM, still short after exercise (y+1 < 0)
                cost[i][j] = (1 + cost_b) * (y[j] + 1) * S_i - K
    return cost


# ============================================================================
# TC_pricer Class -- Davis-Panas-Zariphopoulou Model
# ============================================================================

class TC_pricer:
    """
    Option pricer under the Davis-Panas-Zariphopoulou transaction cost model.

    The algorithm works by backward induction on a binomial tree in
    (log-price x stock-holdings) space.  At each node, the optimal action
    (buy / sell / hold) is chosen to maximise exponential utility.

    The indifference price is computed as:
        p = (delta_0 / gamma) * log(Q_option / Q_no_option)   [writer]
        p = (delta_0 / gamma) * log(Q_no_option / Q_option)   [buyer]

    Parameters
    ----------
    S0 : float
        Current stock price.
    K : float
        Strike price.
    T : float
        Time to maturity (years).
    r : float
        Risk-free interest rate.
    mu : float
        Drift coefficient of the stock (physical measure).
    sig : float
        Volatility (diffusion coefficient).
    cost_b : float, default 0.0
        Proportional BUY transaction cost (lambda in the paper).
    cost_s : float, default 0.0
        Proportional SELL transaction cost (mu in the paper).
    gamma : float, default 0.001
        Risk aversion coefficient in U(W) = -exp(-gamma * W).
    """

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
        """
        Compute the indifference price of a European call option.

        Parameters
        ----------
        N : int, default 500
            Number of time steps in the binomial tree.
            Larger N gives higher accuracy but O(N^2) memory and time.
        TYPE : str, "writer" or "buyer"
            Whether to compute the writer's or buyer's indifference price.
        verbose : bool, default False
            If True, print elapsed time.

        Returns
        -------
        price : float
            Indifference price of the call option.
        elapsed : float (only if verbose=True)
            Computation time in seconds.
        """
        t_start = timer()
        np.seterr(all="ignore")  # suppress overflow warnings in exp()

        x0 = np.log(self.S0)
        T_vec, dt = np.linspace(0, self.T, N + 1, retstep=True)
        delta = np.exp(-self.r * (self.T - T_vec))    # discount factors
        dx = self.sig * np.sqrt(dt)                    # log-price step
        dy = dx                                        # stock-holding step
        M = int(np.floor(N / 2))
        y = np.linspace(-M * dy, M * dy, 2 * M + 1)  # stock-holding grid
        N_y = len(y)
        med = np.where(y == 0)[0].item()               # index where y=0

        # Local helper functions for buy/sell utility multipliers
        def F(xx, ll, nn):
            """Utility cost of buying ll shares at log-price xx, time step nn."""
            return np.exp(self.gamma * (1 + self.cost_b) * np.exp(xx) * ll / delta[nn])

        def G(xx, mm, nn):
            """Utility cost of selling mm shares at log-price xx, time step nn."""
            return np.exp(-self.gamma * (1 - self.cost_s) * np.exp(xx) * mm / delta[nn])

        # Iterate over two portfolios: (1) no option, (2) with option
        for portfolio in ["no_opt", TYPE]:
            # Terminal log-prices at step N
            x = np.array([
                x0 + (self.mu - 0.5 * self.sig**2) * dt * N + (2 * i - N) * dx
                for i in range(N + 1)
            ])

            # Terminal conditions
            if portfolio == "no_opt":
                Q = np.exp(-self.gamma * terminal_no_option(
                    x, y, self.cost_b, self.cost_s))
            elif portfolio == "writer":
                Q = np.exp(-self.gamma * terminal_writer(
                    x, y, self.cost_b, self.cost_s, self.K))
            elif portfolio == "buyer":
                Q = np.exp(-self.gamma * terminal_buyer(
                    x, y, self.cost_b, self.cost_s, self.K))
            else:
                raise ValueError("TYPE must be 'writer' or 'buyer'")

            # Backward induction
            for k in range(N - 1, -1, -1):
                # Expectation (average of up and down nodes)
                Q_new = (Q[:-1, :] + Q[1:, :]) / 2.0

                # Log-prices at step k
                x = np.array([
                    x0 + (self.mu - 0.5 * self.sig**2) * dt * k + (2 * i - k) * dx
                    for i in range(k + 1)
                ])

                # Buy action: increase holdings by dy
                Buy = np.copy(Q_new)
                Buy[:, :-1] = np.matlib.repmat(F(x, dy, k), N_y - 1, 1).T * Q_new[:, 1:]

                # Sell action: decrease holdings by dy
                Sell = np.copy(Q_new)
                Sell[:, 1:] = np.matlib.repmat(G(x, dy, k), N_y - 1, 1).T * Q_new[:, :-1]

                # Optimal action: choose the minimum (maximum utility = minimum of -exp)
                Q = np.minimum(np.minimum(Buy, Sell), Q_new)

            # Extract value at (x0, y=0) -- agent starts with zero stock holdings
            if portfolio == "no_opt":
                Q_no = Q[0, med]
            else:
                Q_yes = Q[0, med]

        # Compute indifference price
        if TYPE == "writer":
            price = (delta[0] / self.gamma) * np.log(Q_yes / Q_no)
        else:
            price = (delta[0] / self.gamma) * np.log(Q_no / Q_yes)

        elapsed = timer() - t_start
        if verbose:
            return price, elapsed
        return price


# ============================================================================
# Black-Scholes Reference Price
# ============================================================================

def bs_call_price(S0, K, T, r, sigma):
    """
    Closed-form Black-Scholes European call price (for comparison).
    """
    from scipy.stats import norm
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


# ============================================================================
# Demo / Main
# ============================================================================

if __name__ == "__main__":

    print("=" * 72)
    print("  OPTION PRICING WITH TRANSACTION COSTS")
    print("  Davis-Panas-Zariphopoulou (DPZ) Model")
    print("=" * 72)

    # ---- Market and option parameters ----
    S0 = 100.0      # Current stock price
    K = 100.0       # Strike price (ATM)
    T = 0.5         # 6 months to maturity
    r = 0.05        # Risk-free rate
    mu = 0.10       # Physical drift (irrelevant in BS but matters with costs)
    sigma = 0.20    # Volatility
    gamma = 0.001   # Risk aversion

    print(f"\n  Parameters:")
    print(f"    S0 = {S0}, K = {K}, T = {T}")
    print(f"    r = {r}, mu = {mu}, sigma = {sigma}")
    print(f"    gamma (risk aversion) = {gamma}")

    # ---- Black-Scholes reference price ----
    bs_price = bs_call_price(S0, K, T, r, sigma)
    print(f"\n  Black-Scholes call price (no costs): {bs_price:.4f}")

    # ---- Price with ZERO transaction costs ----
    # (should approximately recover Black-Scholes)
    print("\n" + "-" * 72)
    print("  1. Zero Transaction Costs (sanity check)")
    print("-" * 72)
    N_steps = 200  # smaller N for speed in demo
    pricer_zero = TC_pricer(S0, K, T, r, mu, sigma, cost_b=0.0, cost_s=0.0, gamma=gamma)

    price_w, time_w = pricer_zero.price(N=N_steps, TYPE="writer", verbose=True)
    price_b, time_b = pricer_zero.price(N=N_steps, TYPE="buyer", verbose=True)
    print(f"    Writer's price: {price_w:.4f}  (time: {time_w:.2f}s)")
    print(f"    Buyer's price:  {price_b:.4f}  (time: {time_b:.2f}s)")
    print(f"    Spread (writer - buyer):  {price_w - price_b:.4f}")
    print(f"    BS reference:   {bs_price:.4f}")

    # ---- Price with different transaction cost levels ----
    print("\n" + "-" * 72)
    print("  2. Impact of Transaction Costs on Option Price")
    print("-" * 72)
    cost_levels = [0.0, 0.001, 0.005, 0.01, 0.02, 0.05]

    print(f"\n  {'Cost (%)':>10s}  {'Writer':>10s}  {'Buyer':>10s}  {'Spread':>10s}  {'BS':>10s}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

    writer_prices = []
    buyer_prices = []

    for c in cost_levels:
        pricer = TC_pricer(S0, K, T, r, mu, sigma, cost_b=c, cost_s=c, gamma=gamma)
        pw = pricer.price(N=N_steps, TYPE="writer")
        pb = pricer.price(N=N_steps, TYPE="buyer")
        writer_prices.append(pw)
        buyer_prices.append(pb)
        print(f"  {c*100:10.2f}  {pw:10.4f}  {pb:10.4f}  {pw - pb:10.4f}  {bs_price:10.4f}")

    # ---- Impact of risk aversion ----
    print("\n" + "-" * 72)
    print("  3. Impact of Risk Aversion (gamma)")
    print("-" * 72)
    cost_fixed = 0.01  # 1% transaction cost
    gamma_levels = [0.0005, 0.001, 0.005, 0.01, 0.05]

    print(f"\n  Transaction cost = {cost_fixed*100:.1f}%")
    print(f"  {'gamma':>10s}  {'Writer':>10s}  {'Buyer':>10s}  {'Spread':>10s}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

    for g in gamma_levels:
        pricer = TC_pricer(S0, K, T, r, mu, sigma,
                           cost_b=cost_fixed, cost_s=cost_fixed, gamma=g)
        pw = pricer.price(N=N_steps, TYPE="writer")
        pb = pricer.price(N=N_steps, TYPE="buyer")
        print(f"  {g:10.4f}  {pw:10.4f}  {pb:10.4f}  {pw - pb:10.4f}")

    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    print("  Key observations from the DPZ model:")
    print("  - With zero costs, writer and buyer prices converge to BS price.")
    print("  - Transaction costs create a bid-ask spread around the BS price.")
    print("  - The writer charges MORE than BS (compensation for hedging costs).")
    print("  - The buyer pays LESS than BS (accounts for imperfect replication).")
    print("  - Higher risk aversion (gamma) widens the bid-ask spread.")
    print("  - The spread grows with the level of transaction costs.")
    print("=" * 72)
