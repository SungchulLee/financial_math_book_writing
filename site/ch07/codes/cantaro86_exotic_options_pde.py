#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_exotic_options_pde.py
Exotic Option Pricing: Digital, Barrier, and Asian Options

Credits
-------
Based on notebook "2.2 Exotic options" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 7 -- Extensions & Exotics).

Topics covered
--------------
1. Digital (binary) options: closed formula, Monte Carlo, PDE.
2. Barrier options (Up-and-Out Call, Down-and-In Call):
   closed formula, Monte Carlo with Broadie–Glasserman–Kou correction, PDE.
3. Asian options (fixed-strike and floating-strike):
   Monte Carlo and PDE via coordinate transformation.
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse.linalg import spsolve, splu


# ============================================================================
# 1. DIGITAL (BINARY) OPTIONS
# ============================================================================

def digital_call_closed(S0, K, T, r, sigma):
    """
    Price a digital (binary) call option by Black-Scholes closed formula.

    Payoff: 1 if S_T > K, else 0.
    Price:  e^{-rT} * N(d2)
    """
    d2 = (np.log(S0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    return np.exp(-r * T) * ss.norm.cdf(d2)


def digital_call_mc(S0, K, T, r, sigma, N_sim=20_000_000, seed=42):
    """
    Price a digital call by Monte Carlo simulation.

    Returns dict with price and standard error.
    """
    np.random.seed(seed)
    W = (r - sigma**2 / 2) * T + ss.norm.rvs(loc=0, scale=sigma,
                                               size=N_sim) * np.sqrt(T)
    S_T = S0 * np.exp(W)
    indicator = (S_T > K).astype(float)
    price = np.exp(-r * T) * np.mean(indicator)
    std_err = np.exp(-r * T) * ss.sem(indicator)
    return {"price": price, "std_error": std_err}


def digital_call_pde(S0, K, T, r, sigma, Nspace=6000, Ntime=6000):
    """
    Price a digital call by solving the BS PDE in log-variables
    with a binary terminal condition.

    Returns dict with price, S_grid, V_curve, V_surface, T_grid, payoff.
    """
    X0 = np.log(S0)
    x_max = np.log(3 * K)
    x_min = np.log(K / 3)

    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)
    T_arr, dt = np.linspace(0, T, Ntime, retstep=True)
    Payoff = np.where(np.exp(x) > K, 1.0, 0.0)

    V = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)

    V[:, -1] = Payoff
    V[-1, :] = 1  # deep ITM boundary
    V[0, :] = 0   # deep OTM boundary

    sig2 = sigma * sigma
    dxx = dx * dx
    a = (dt / 2) * ((r - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r)
    c = -(dt / 2) * ((r - 0.5 * sig2) / dx + sig2 / dxx)
    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()
    DD = splu(D)

    for i in range(Ntime - 2, -1, -1):
        offset[0] = a * V[0, i]
        offset[-1] = c * V[-1, i]
        V[1:-1, i] = DD.solve(V[1:-1, i + 1] - offset)

    price = np.interp(X0, x, V[:, 0])
    return {"price": price, "S_grid": np.exp(x), "V_curve": V[:, 0],
            "V_surface": V, "T_grid": T_arr, "payoff": Payoff}


# ============================================================================
# 2. BARRIER OPTIONS
# ============================================================================

def barrier_upout_call_closed(S0, K, B, T, r, sigma):
    """
    Closed-form price for an Up-and-Out European call.
    Requires B > K and B > S0.

    Reference: Bjork (2009) Ch. 7.3.3 and Rubinstein-Reiner (1991).
    """
    sig = sigma
    d1 = lambda t, s: (np.log(s) + (r + sig**2 / 2) * t) / (sig * np.sqrt(t))
    d2 = lambda t, s: (np.log(s) + (r - sig**2 / 2) * t) / (sig * np.sqrt(t))

    price = (
        S0 * (ss.norm.cdf(d1(T, S0 / K)) - ss.norm.cdf(d1(T, S0 / B)))
        - np.exp(-r * T) * K
        * (ss.norm.cdf(d2(T, S0 / K)) - ss.norm.cdf(d2(T, S0 / B)))
        - B * (S0 / B) ** (-2 * r / sig**2)
        * (ss.norm.cdf(d1(T, B**2 / (S0 * K))) - ss.norm.cdf(d1(T, B / S0)))
        + np.exp(-r * T) * K * (S0 / B) ** (-2 * r / sig**2 + 1)
        * (ss.norm.cdf(d2(T, B**2 / (S0 * K))) - ss.norm.cdf(d2(T, B / S0)))
    )
    return price


def barrier_downin_call_closed(S0, K, BB, T, r, sigma):
    """
    Closed-form price for a Down-and-In European call.
    Requires BB < S0 and BB < K.
    """
    sig = sigma
    d1 = lambda t, s: (np.log(s) + (r + sig**2 / 2) * t) / (sig * np.sqrt(t))
    d2 = lambda t, s: (np.log(s) + (r - sig**2 / 2) * t) / (sig * np.sqrt(t))

    price = (
        S0 * (BB / S0) ** (1 + 2 * r / sig**2)
        * ss.norm.cdf(d1(T, BB**2 / (S0 * K)))
        - np.exp(-r * T) * K * (BB / S0) ** (-1 + 2 * r / sig**2)
        * ss.norm.cdf(d2(T, BB**2 / (S0 * K)))
    )
    return price


def barrier_mc(S0, K, B_up, B_down, T, r, sigma, N=10000, paths=50000,
               seed=42, apply_correction=True):
    """
    Monte Carlo pricing for Up-and-Out call and Down-and-In call,
    with optional Broadie-Glasserman-Kou continuity correction.

    Parameters
    ----------
    B_up : float    Up barrier for knock-out.
    B_down : float  Down barrier for knock-in.
    apply_correction : bool  Apply the beta1 correction (default True).

    Returns
    -------
    dict with up_out_price, up_out_se, down_in_price, down_in_se.
    """
    np.random.seed(seed)
    dt = T / (N - 1)

    # Broadie-Glasserman-Kou correction
    B_u = B_up
    B_d = B_down
    if apply_correction:
        beta1 = 0.5826
        B_u = B_up * np.exp(-beta1 * np.sqrt(dt) * sigma)
        B_d = B_down * np.exp(beta1 * np.sqrt(dt) * sigma)

    # Path generation
    X_0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(loc=(r - sigma**2 / 2) * dt,
                              scale=np.sqrt(dt) * sigma,
                              size=(paths, N - 1))
    X = np.concatenate((X_0, increments), axis=1).cumsum(1)
    S = S0 * np.exp(X)

    M = np.amax(S, axis=1)   # maximum of each path
    MM = np.amin(S, axis=1)  # minimum of each path

    # Up and Out: payoff if max < barrier
    payoff_uo = np.maximum(S[:, -1] - K, 0) * (M < B_u)
    uo_price = np.exp(-r * T) * np.mean(payoff_uo)
    uo_se = np.exp(-r * T) * ss.sem(payoff_uo)

    # Down and In: payoff if min <= barrier
    payoff_di = np.maximum(S[:, -1] - K, 0) * (MM <= B_d)
    di_price = np.exp(-r * T) * np.mean(payoff_di)
    di_se = np.exp(-r * T) * ss.sem(payoff_di)

    return {"up_out_price": uo_price, "up_out_se": uo_se,
            "down_in_price": di_price, "down_in_se": di_se}


def barrier_upout_pde(S0, K, B, T, r, sigma, Nspace=14000, Ntime=10000):
    """
    PDE price for an Up-and-Out European call.
    The upper boundary is set at the barrier B where V=0.
    """
    X0 = np.log(S0)
    x_max = np.log(B)
    x_min = np.log(K / 3)

    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)
    T_arr, dt = np.linspace(0, T, Ntime, retstep=True)
    Payoff = np.maximum(np.exp(x) - K, 0)

    V = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)

    V[:, -1] = Payoff
    V[-1, :] = 0  # knocked out at barrier
    V[0, :] = 0   # deep OTM

    sig2 = sigma * sigma
    dxx = dx * dx
    a = (dt / 2) * ((r - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r)
    c = -(dt / 2) * ((r - 0.5 * sig2) / dx + sig2 / dxx)
    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()
    DD = splu(D)

    for i in range(Ntime - 2, -1, -1):
        offset[0] = a * V[0, i]
        offset[-1] = c * V[-1, i]
        V[1:-1, i] = DD.solve(V[1:-1, i + 1] - offset)

    price = np.interp(X0, x, V[:, 0])
    return {"price": price, "S_grid": np.exp(x), "V_curve": V[:, 0],
            "V_surface": V, "T_grid": T_arr, "payoff": Payoff}


def barrier_downin_pde(S0, K, BB, T, r, sigma, Nspace=5000, Ntime=5000):
    """
    PDE price for a Down-and-In European call.

    Uses a two-step approach:
    1. Solve the vanilla call on an extended grid starting from the barrier.
    2. Solve the barrier-modified problem on the upper sub-grid.
    """
    X0 = np.log(S0)
    x_max = np.log(K * 3)
    B_log = np.log(BB)

    # Extended grid starting from the barrier
    x_b, dx = np.linspace(B_log, x_max, Nspace, retstep=True)
    x_lower = np.arange(B_log, np.log(K / 3), -dx)[::-1][:-1]
    x = np.concatenate((x_lower, x_b))
    N_tot = len(x)

    T_arr, dt = np.linspace(0, T, Ntime, retstep=True)
    Payoff = np.maximum(np.exp(x) - K, 0)

    # Step 1: Solve vanilla call on full grid
    V = np.zeros((N_tot, Ntime))
    offset = np.zeros(N_tot - 2)

    V[:, -1] = Payoff
    V[-1, :] = np.exp(x_max) - K * np.exp(-r * T_arr[::-1])
    V[0, :] = 0

    sig2 = sigma * sigma
    dxx = dx * dx
    a = (dt / 2) * ((r - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r)
    c = -(dt / 2) * ((r - 0.5 * sig2) / dx + sig2 / dxx)
    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(N_tot - 2, N_tot - 2)).tocsc()
    DD = splu(D)

    for i in range(Ntime - 2, -1, -1):
        offset[0] = a * V[0, i]
        offset[-1] = c * V[-1, i]
        V[1:-1, i] = DD.solve(V[1:-1, i + 1] - offset)

    # Step 2: Barrier problem on the upper sub-grid
    VB = V[-Nspace:, :].copy()
    offset_b = np.zeros(Nspace - 2)

    VB[:, -1] = 0
    VB[-1, :] = 0

    D_b = sparse.diags([a, b, c], [-1, 0, 1],
                        shape=(Nspace - 2, Nspace - 2)).tocsc()
    DD_b = splu(D_b)

    for i in range(Ntime - 2, -1, -1):
        offset_b[0] = a * VB[0, i]
        offset_b[-1] = c * VB[-1, i]
        VB[1:-1, i] = DD_b.solve(VB[1:-1, i + 1] - offset_b)

    price = np.interp(X0, x_b, VB[:, 0])
    return {"price": price, "S_grid": np.exp(x_b), "V_curve": VB[:, 0]}


# ============================================================================
# 3. ASIAN OPTIONS
# ============================================================================

def asian_mc(S0, K, T, r, sigma, N=10000, paths=50000, seed=41):
    """
    Monte Carlo pricing for Asian options (arithmetic average).

    Returns
    -------
    dict with fixed_strike_price, fixed_strike_se,
              float_strike_price, float_strike_se.
    """
    np.random.seed(seed)
    dt = T / (N - 1)

    X_0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(loc=(r - sigma**2 / 2) * dt,
                              scale=np.sqrt(dt) * sigma,
                              size=(paths, N - 1))
    X = np.concatenate((X_0, increments), axis=1).cumsum(1)
    S = S0 * np.exp(X)

    A = np.mean(S, axis=1)  # arithmetic average

    # Fixed strike: max(A - K, 0)
    payoff_fixed = np.maximum(A - K, 0)
    fixed_price = np.exp(-r * T) * np.mean(payoff_fixed)
    fixed_se = np.exp(-r * T) * ss.sem(payoff_fixed)

    # Floating strike: max(S_T - A, 0)
    payoff_float = np.maximum(S[:, -1] - A, 0)
    float_price = np.exp(-r * T) * np.mean(payoff_float)
    float_se = np.exp(-r * T) * ss.sem(payoff_float)

    return {"fixed_strike_price": fixed_price, "fixed_strike_se": fixed_se,
            "float_strike_price": float_price, "float_strike_se": float_se}


def asian_fixed_strike_pde(S0, K, T, r, sigma, Nspace=6000, Ntime=6000):
    """
    PDE price for a fixed-strike arithmetic Asian call option.

    Uses the coordinate transformation from Vecer (2001) / cantaro86:
        g(t, y) where y = gamma(t)*S - e^{-r(T-t)}*K  (normalised)
    with gamma(t) = (1 - e^{-r(T-t)}) / (rT).

    The PDE becomes one-dimensional with time-dependent diffusion
    coefficient sigma^2 * (gamma(t) - y)^2.
    """
    def gamma(t):
        return 1 / (r * T) * (1 - np.exp(-r * (T - t)))

    def get_X0(S_val):
        return gamma(0) * S_val - np.exp(-r * T) * K

    y_max, y_min = 60, -60
    y, dy = np.linspace(y_min, y_max, Nspace, retstep=True)
    T_arr, dt = np.linspace(0, T, Ntime, retstep=True)
    Payoff = np.maximum(y, 0)

    G = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)

    G[:, -1] = Payoff
    G[-1, :] = y_max
    G[0, :] = 0

    sig2 = sigma * sigma
    dyy = dy * dy

    for n in range(Ntime - 2, -1, -1):
        a = -0.5 * (dt / dyy) * sig2 * (gamma(T_arr[n]) - y[1:-1])**2
        b_diag = 1 + (dt / dyy) * sig2 * (gamma(T_arr[n]) - y[1:-1])**2
        a0 = a[0]
        cM = a[-1]
        aa = a[1:]   # lower diagonal
        cc = a[:-1]  # upper diagonal
        D = sparse.diags([aa, b_diag, cc], [-1, 0, 1],
                          shape=(Nspace - 2, Nspace - 2)).tocsc()

        offset[0] = a0 * G[0, n]
        offset[-1] = cM * G[-1, n]
        G[1:-1, n] = spsolve(D, G[1:-1, n + 1] - offset)

    X0 = get_X0(S0)
    price = S0 * np.interp(X0 / S0, y, G[:, 0])
    return {"price": price, "y_grid": y, "G_curve": G[:, 0],
            "get_X0": get_X0}


def asian_floating_strike_pde(S0, K, T, r, sigma, Nspace=4000, Ntime=7000):
    """
    PDE price for a floating-strike arithmetic Asian call option.

    Uses the dimensionality reduction via the variable z = S/A.
    The auxiliary function W(t, z) satisfies a one-dimensional PDE
    with time-dependent coefficients.
    """
    x_max, x_min = 10, 0
    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)
    T_arr, dt = np.linspace(0.0001, T, Ntime, retstep=True)
    Payoff = np.maximum(x - 1, 0)

    V = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)
    V[:, -1] = Payoff
    V[-1, :] = x_max - 1
    V[0, :] = 0

    sig2 = sigma * sigma
    dxx = dx * dx

    for n in range(Ntime - 2, -1, -1):
        drift = x[1:-1] * (r - (x[1:-1] - 1) / T_arr[n])
        max_part = np.maximum(drift, 0)  # upwind positive
        min_part = np.minimum(drift, 0)  # upwind negative

        a = min_part * (dt / dx) - 0.5 * (dt / dxx) * sig2 * x[1:-1]**2
        b_diag = (1 + dt * (r - (x[1:-1] - 1) / T_arr[n])
                  + (dt / dxx) * sig2 * x[1:-1]**2
                  + dt / dx * (max_part - min_part))
        c = -max_part * (dt / dx) - 0.5 * (dt / dxx) * sig2 * x[1:-1]**2

        a0 = a[0]
        cM = c[-1]
        aa = a[1:]
        cc = c[:-1]
        D = sparse.diags([aa, b_diag, cc], [-1, 0, 1],
                          shape=(Nspace - 2, Nspace - 2)).tocsc()

        offset[0] = a0 * V[0, n]
        offset[-1] = cM * V[-1, n]
        V[1:-1, n] = spsolve(D, V[1:-1, n + 1] - offset)

    # ATM: x = S/A = 1
    price = S0 * np.interp(1, x, V[:, 0])
    return {"price": price, "x_grid": x, "V_curve": V[:, 0],
            "V_surface": V, "T_grid": T_arr, "payoff": Payoff}


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all exotic option demonstrations."""
    S0, K, T, r, sigma = 100.0, 100.0, 1.0, 0.1, 0.2
    B_up, B_down = 120, 90

    # ---- 1. Digital Options ----
    print("=" * 60)
    print("1. Digital (Binary) Call Option")
    print("=" * 60)

    d_closed = digital_call_closed(S0, K, T, r, sigma)
    d_mc = digital_call_mc(S0, K, T, r, sigma, N_sim=5_000_000)
    d_pde = digital_call_pde(S0, K, T, r, sigma, Nspace=6000, Ntime=6000)

    print(f"  Closed formula: {d_closed:.6f}")
    print(f"  Monte Carlo:    {d_mc['price']:.6f} "
          f"(se: {d_mc['std_error']:.6f})")
    print(f"  PDE (implicit): {d_pde['price']:.6f}")

    # Plot digital option
    plt.figure(figsize=(10, 5))
    plt.plot(d_pde["S_grid"], d_pde["payoff"], color="blue", label="Payoff")
    plt.plot(d_pde["S_grid"], d_pde["V_curve"], color="red",
             label="Digital call (PDE)")
    plt.xlim(60, 200)
    plt.ylim(0, 1.1)
    plt.xlabel("S")
    plt.ylabel("V")
    plt.legend()
    plt.title("Digital Call Option: Payoff vs Price at t=0")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 2. Barrier Options ----
    print("\n" + "=" * 60)
    print("2. Barrier Options")
    print("=" * 60)

    # Up-and-Out
    uo_closed = barrier_upout_call_closed(S0, K, B_up, T, r, sigma)
    print(f"\n  Up-and-Out Call (B={B_up}):")
    print(f"    Closed formula: {uo_closed:.6f}")

    mc_res = barrier_mc(S0, K, B_up, B_down, T, r, sigma,
                        N=10000, paths=50000)
    print(f"    Monte Carlo:    {mc_res['up_out_price']:.6f} "
          f"(se: {mc_res['up_out_se']:.6f})")

    uo_pde = barrier_upout_pde(S0, K, B_up, T, r, sigma,
                                Nspace=8000, Ntime=6000)
    print(f"    PDE (implicit): {uo_pde['price']:.6f}")

    # Down-and-In
    di_closed = barrier_downin_call_closed(S0, K, B_down, T, r, sigma)
    print(f"\n  Down-and-In Call (B={B_down}):")
    print(f"    Closed formula: {di_closed:.6f}")
    print(f"    Monte Carlo:    {mc_res['down_in_price']:.6f} "
          f"(se: {mc_res['down_in_se']:.6f})")

    di_pde = barrier_downin_pde(S0, K, B_down, T, r, sigma,
                                 Nspace=5000, Ntime=5000)
    print(f"    PDE (implicit): {di_pde['price']:.6f}")

    # Plot barrier option
    plt.figure(figsize=(10, 5))
    plt.plot(uo_pde["S_grid"], uo_pde["payoff"], color="blue",
             label="Call payoff")
    plt.plot(uo_pde["S_grid"], uo_pde["V_curve"], color="red",
             label="Up-and-Out call (PDE)")
    plt.axvline(x=B_up, color="gray", ls="--", label=f"Barrier B={B_up}")
    plt.xlim(40, 130)
    plt.ylim(0, 2)
    plt.xlabel("S")
    plt.ylabel("V")
    plt.legend()
    plt.title("Up-and-Out Call: Payoff vs Price at t=0")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 3. Asian Options ----
    print("\n" + "=" * 60)
    print("3. Asian Options")
    print("=" * 60)

    # Monte Carlo
    asian_res = asian_mc(S0, K, T, r, sigma, N=10000, paths=50000)
    print(f"\n  Monte Carlo:")
    print(f"    Fixed strike call:    {asian_res['fixed_strike_price']:.6f} "
          f"(se: {asian_res['fixed_strike_se']:.6f})")
    print(f"    Floating strike call: {asian_res['float_strike_price']:.6f} "
          f"(se: {asian_res['float_strike_se']:.6f})")

    # Fixed strike PDE
    asian_fixed = asian_fixed_strike_pde(S0, K, T, r, sigma,
                                          Nspace=6000, Ntime=6000)
    print(f"\n  PDE (fixed strike):     {asian_fixed['price']:.6f}")

    # Floating strike PDE
    asian_float = asian_floating_strike_pde(S0, K, T, r, sigma,
                                             Nspace=4000, Ntime=7000)
    print(f"  PDE (floating strike):  {asian_float['price']:.6f}")

    # Plot fixed-strike Asian
    get_X0 = asian_fixed["get_X0"]
    S_plot = np.linspace(70, 130, 100)
    asian_curve = S_plot * np.interp(get_X0(S_plot) / S_plot,
                                      asian_fixed["y_grid"],
                                      asian_fixed["G_curve"])

    plt.figure(figsize=(10, 5))
    plt.plot(S_plot, np.maximum(S_plot - K, 0), color="blue",
             label="Call payoff")
    plt.plot(S_plot, asian_curve, color="red",
             label="Fixed-strike Asian call (PDE)")
    plt.xlabel("S")
    plt.ylabel("Price")
    plt.legend()
    plt.title("Fixed-Strike Asian CALL Price at t=0")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
