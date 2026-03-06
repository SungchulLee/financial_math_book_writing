#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_bs_numerical_methods.py
Black-Scholes Valuation Methods -- Comprehensive Numerical Demo

Credits
-------
Based on notebook "1.1 Black-Scholes numerical methods" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 6 -- Black-Scholes).

All external FMNM dependencies have been inlined so the file runs
stand-alone with only NumPy, SciPy, and Matplotlib.

Topics covered
--------------
1. Black-Scholes closed formula (call and put).
2. Put-call parity verification.
3. Numerical integration of the log-normal density.
4. Change-of-measure pricing (stock vs money-market numeraire).
5. Monte Carlo pricing with standard error.
6. Efficient binomial tree implementation (with optimisation tricks).
7. Price as a function of volatility (limits of the BS model).
"""

import numpy as np
import scipy.stats as ss
from scipy.integrate import quad
from functools import partial
import matplotlib.pyplot as plt


# ============================================================================
# 1. BLACK-SCHOLES CLOSED FORMULA
# ============================================================================

def bs_price(payoff, S0, K, T, r, sigma):
    """
    Analytical Black-Scholes price for a European option.

    Parameters
    ----------
    payoff : str  "call" or "put"
    S0 : float    Current stock price
    K : float     Strike price
    T : float     Time to maturity (years)
    r : float     Risk-free rate (continuous compounding)
    sigma : float Annualised volatility

    Returns
    -------
    float  Option price.
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if payoff == "call":
        return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
    elif payoff == "put":
        return K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)
    else:
        raise ValueError("payoff must be 'call' or 'put'")


# ============================================================================
# 2. PUT-CALL PARITY CHECK
# ============================================================================

def check_put_call_parity(S0, K, T, r, sigma):
    """
    Verify put-call parity: C - P = S0 - K * exp(-rT).

    Returns
    -------
    dict  Call price, put price, LHS, RHS, and absolute error.
    """
    call = bs_price("call", S0, K, T, r, sigma)
    put = bs_price("put", S0, K, T, r, sigma)
    lhs = call - put
    rhs = S0 - K * np.exp(-r * T)
    return {"call": call, "put": put, "LHS": lhs, "RHS": rhs, "error": abs(lhs - rhs)}


# ============================================================================
# 3. NUMERICAL INTEGRATION OF THE LOG-NORMAL DENSITY
# ============================================================================

def log_normal_density(x, e_ret, vol):
    """
    Log-normal density f(x | e_ret, vol).

    The density of S_T where log(S_T) ~ N(e_ret, vol^2).

    Parameters
    ----------
    x : float or array  Evaluation points (S_T values).
    e_ret : float        E[log S_T] = log(S0) + (r - sigma^2/2)*T.
    vol : float          Std[log S_T] = sigma * sqrt(T).
    """
    return (1.0 / (x * vol * np.sqrt(2 * np.pi))
            * np.exp(-((np.log(x) - e_ret) ** 2) / (2 * vol**2)))


def price_by_numerical_integration(S0, K, T, r, sigma, payoff="call"):
    """
    Price a European option by direct numerical integration of the
    risk-neutral expectation against the log-normal density.

    C = e^{-rT} * integral_{K}^{inf} (s - K) * f(s|S0) ds
    P = e^{-rT} * integral_{0}^{K}  (K - s) * f(s|S0) ds
    """
    e_ret = np.log(S0) + (r - 0.5 * sigma**2) * T
    vol = sigma * np.sqrt(T)

    if payoff == "call":
        integrand = lambda s: (s - K) * ss.lognorm.pdf(s, vol, scale=np.exp(e_ret))
        price = quad(integrand, K, np.inf)[0] * np.exp(-r * T)
    elif payoff == "put":
        integrand = lambda s: (K - s) * ss.lognorm.pdf(s, vol, scale=np.exp(e_ret))
        price = quad(integrand, 0, K)[0] * np.exp(-r * T)
    else:
        raise ValueError("payoff must be 'call' or 'put'")
    return price


# ============================================================================
# 4. CHANGE-OF-MEASURE PRICING (Q1 = stock numeraire, Q2 = money-market)
# ============================================================================

def price_by_change_of_measure(S0, K, T, r, sigma):
    """
    Price a European call using the decomposition:

        C = S0 * Q_tilde(S_T > K) - K * e^{-rT} * Q(S_T > K)

    where:
      Q_tilde uses the stock numeraire  (drift = r + sigma^2/2)
      Q       uses the money-market      (drift = r - sigma^2/2)

    Returns
    -------
    dict  Q1 probability, Q2 probability, and call price.
    """
    vol = sigma * np.sqrt(T)

    # Under stock numeraire: log S_T has drift (r + 0.5*sigma^2)*T
    e_ret_stock = np.log(S0) + (r + 0.5 * sigma**2) * T
    Q1 = quad(lambda s: ss.lognorm.pdf(s, vol, scale=np.exp(e_ret_stock)), K, np.inf)[0]

    # Under money-market numeraire: log S_T has drift (r - 0.5*sigma^2)*T
    e_ret_mm = np.log(S0) + (r - 0.5 * sigma**2) * T
    Q2 = quad(lambda s: ss.lognorm.pdf(s, vol, scale=np.exp(e_ret_mm)), K, np.inf)[0]

    call_price = S0 * Q1 - K * np.exp(-r * T) * Q2
    return {"Q1_stock": Q1, "Q2_mm": Q2, "call": call_price}


# ============================================================================
# 5. MONTE CARLO PRICING
# ============================================================================

def price_by_monte_carlo(S0, K, T, r, sigma, N=10_000_000, payoff="call", seed=44):
    """
    Monte Carlo price for a European option.

    Simulates terminal values:
        S_T = S0 * exp((r - sigma^2/2)*T + sigma*sqrt(T)*Z)
    for Z ~ N(0,1), then averages the discounted payoff.

    Returns
    -------
    dict  price, standard_error.
    """
    np.random.seed(seed)
    W = ss.norm.rvs((r - 0.5 * sigma**2) * T, np.sqrt(T) * sigma, N)
    S_T = S0 * np.exp(W)

    if payoff == "call":
        payoffs = np.exp(-r * T) * np.maximum(S_T - K, 0)
    elif payoff == "put":
        payoffs = np.exp(-r * T) * np.maximum(K - S_T, 0)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    return {"price": np.mean(payoffs), "std_error": ss.sem(payoffs)}


# ============================================================================
# 6. BINOMIAL TREE (EFFICIENT IMPLEMENTATION)
# ============================================================================

def price_by_binomial_tree(S0, K, T, r, sigma, N=15000, payoff="call"):
    """
    Price a European option using a CRR binomial tree.

    Uses the optimised final-layer enumeration trick:
        S_T[j] = S0/u^N * u^(2j)  for j = 0, ..., N

    Parameters
    ----------
    N : int  Number of time steps (higher = more accurate).

    Returns
    -------
    float  Option price.
    """
    dT = T / N
    u = np.exp(sigma * np.sqrt(dT))
    d = 1.0 / u
    a = np.exp(r * dT)
    p = (a - d) / (u - d)
    q = 1.0 - p

    # Optimised terminal stock prices (fastest approach from the notebook)
    S_0N = S0 / u**N
    S_T = np.array([S_0N * u**j for j in range(0, 2 * N + 1, 2)])

    if payoff == "call":
        V = np.maximum(S_T - K, 0.0)
    elif payoff == "put":
        V = np.maximum(K - S_T, 0.0)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    # Backward induction
    for i in range(N - 1, -1, -1):
        V[:-1] = np.exp(-r * dT) * (p * V[1:] + q * V[:-1])

    return V[0]


# ============================================================================
# 7. PRICE vs VOLATILITY (LIMITS OF THE MODEL)
# ============================================================================

def plot_price_vs_volatility(S0, K, T, r, payoff="call",
                             sig_min=0.01, sig_max=10.0, n_points=1000):
    """
    Plot the Black-Scholes price as a function of volatility.

    Demonstrates that the BS formula is an increasing function of
    volatility, but for very high volatilities the curve flattens,
    showing the model's practical limit (reliable for sigma in 0-400%).
    """
    sigmas = np.linspace(sig_min, sig_max, n_points)
    prices = np.array([bs_price(payoff, S0, K, T, r, s) for s in sigmas])

    plt.figure(figsize=(8, 5))
    plt.plot(sigmas, prices)
    plt.xlabel("Volatility (sigma)")
    plt.ylabel("Option Price")
    plt.title(f"BS {payoff} price as function of volatility")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def plot_lognormal_density(S0, K, T, r, sigma):
    """Plot the risk-neutral log-normal density of S_T conditioned on S0."""
    e_ret = np.log(S0) + (r - 0.5 * sigma**2) * T
    vol = sigma * np.sqrt(T)
    x = np.linspace(max(1, S0 * 0.3), S0 * 1.9, 200)

    plt.figure(figsize=(8, 5))
    plt.plot(x, log_normal_density(x, e_ret, vol))
    plt.title(f"Log-normal distribution, conditioned on $S_0={S0}$")
    plt.xlabel("$S_T$")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def run_all_methods(S0=100, K=100, T=1.0, r=0.1, sigma=0.2, N_mc=1_000_000):
    """
    Run all pricing methods and compare results.

    Parameters
    ----------
    S0, K, T, r, sigma : float  Standard BS parameters.
    N_mc : int                  Number of Monte Carlo samples.
    """
    print("=" * 60)
    print("Black-Scholes Numerical Methods Comparison")
    print("=" * 60)
    print(f"  S0={S0}, K={K}, T={T}, r={r}, sigma={sigma}")
    print("-" * 60)

    # 1. Closed formula
    call_cf = bs_price("call", S0, K, T, r, sigma)
    put_cf = bs_price("put", S0, K, T, r, sigma)
    print(f"1. Closed formula:     Call = {call_cf:.6f},  Put = {put_cf:.6f}")

    # 2. Put-call parity
    parity = check_put_call_parity(S0, K, T, r, sigma)
    print(f"2. Put-Call parity error: {parity['error']:.2e}")

    # 3. Numerical integration
    call_ni = price_by_numerical_integration(S0, K, T, r, sigma, "call")
    put_ni = price_by_numerical_integration(S0, K, T, r, sigma, "put")
    print(f"3. Numerical integration:  Call = {call_ni:.6f},  Put = {put_ni:.6f}")

    # 4. Change of measure
    com = price_by_change_of_measure(S0, K, T, r, sigma)
    print(f"4. Change of measure:  Call = {com['call']:.6f}")
    print(f"   Q_tilde(S_T>K) = {com['Q1_stock']:.6f},  Q(S_T>K) = {com['Q2_mm']:.6f}")

    # 5. Monte Carlo
    mc = price_by_monte_carlo(S0, K, T, r, sigma, N=N_mc, payoff="call")
    print(f"5. Monte Carlo ({N_mc:,} paths): Call = {mc['price']:.6f} "
          f"(std err = {mc['std_error']:.6f})")

    # 6. Binomial tree
    for N_tree in [1000, 5000, 15000]:
        bt = price_by_binomial_tree(S0, K, T, r, sigma, N=N_tree, payoff="call")
        print(f"6. Binomial tree (N={N_tree:>5d}):  Call = {bt:.6f}")

    print("-" * 60)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # --- Parameters ---
    S0, K, T, r, sigma = 100.0, 100.0, 1.0, 0.1, 0.2

    # --- Run all methods ---
    run_all_methods(S0, K, T, r, sigma)

    # --- Plots ---
    plot_lognormal_density(S0, K, T, r, sigma)
    plot_price_vs_volatility(S0, K, T, r, "call")
