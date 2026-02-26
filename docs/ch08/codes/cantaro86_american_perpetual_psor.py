#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_american_perpetual_psor.py
American Options: Binomial Tree, LSM Walkthrough, and Perpetual Put via PSOR

Credits
-------
Based on notebook "2.3 American Options" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 8 -- FDM / American Options).

Topics covered
--------------
1. American put pricing via CRR binomial tree.
2. Longstaff-Schwartz (LSM) Monte Carlo -- step-by-step walkthrough
   reproducing the classic 8-path example from the original paper.
3. Perpetual American put: analytical formula and numerical solution
   via Projected SOR (PSOR) for the free-boundary ODE.
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


# ============================================================================
# 1. AMERICAN PUT -- BINOMIAL TREE
# ============================================================================

def american_put_binomial(S0, K, T, r, sigma, N=25000):
    """
    Price an American put via the CRR binomial tree.

    At each node, the option value is the maximum of the continuation
    value and the immediate exercise value (early exercise check).

    Parameters
    ----------
    S0 : float  Spot price.
    K : float   Strike price.
    T : float   Time to maturity.
    r : float   Risk-free rate.
    sigma : float  Volatility.
    N : int     Number of time steps.

    Returns
    -------
    float  American put price.
    """
    dT = T / N
    u = np.exp(sigma * np.sqrt(dT))
    d = 1.0 / u
    a = np.exp(r * dT)
    p = (a - d) / (u - d)
    q = 1.0 - p

    # Terminal stock prices
    S_T = np.array([S0 * u**j * d**(N - j) for j in range(N + 1)])
    V = np.maximum(K - S_T, 0.0)

    # Backward induction with early exercise
    for i in range(N - 1, -1, -1):
        V[:-1] = np.exp(-r * dT) * (p * V[1:] + q * V[:-1])
        S_T = S_T * u  # stock prices at step i
        V = np.maximum(V, K - S_T)

    return V[0]


# ============================================================================
# 2. LONGSTAFF-SCHWARTZ -- STEP-BY-STEP WALKTHROUGH
# ============================================================================

def lsm_walkthrough():
    """
    Reproduce the classic 8-path example from the Longstaff-Schwartz
    (2001) paper to illustrate the LSM algorithm step by step.

    This is a pedagogical demonstration with N=4 time points,
    8 paths, and the stock matrix from the original paper.

    Returns
    -------
    dict with keys:
        V0 : float      Estimated option price.
        S : ndarray      Stock price matrix (8 x 4).
        H : ndarray      Intrinsic value matrix (8 x 4).
        V : ndarray      Cash flow matrix (8 x 4).
    """
    N = 4      # time points
    r = 0.06   # interest rate
    K = 1.1    # strike
    T = 3      # maturity
    dt = T / (N - 1)
    df = np.exp(-r * dt)

    # Stock price matrix from Longstaff-Schwartz (2001)
    S = np.array([
        [1.00, 1.09, 1.08, 1.34],
        [1.00, 1.16, 1.26, 1.54],
        [1.00, 1.22, 1.07, 1.03],
        [1.00, 0.93, 0.97, 0.92],
        [1.00, 1.11, 1.56, 1.52],
        [1.00, 0.76, 0.77, 0.90],
        [1.00, 0.92, 0.84, 1.01],
        [1.00, 0.88, 1.22, 1.34],
    ])

    H = np.maximum(K - S, 0)  # intrinsic values
    V = np.zeros_like(H)      # cash flow matrix
    V[:, -1] = H[:, -1]       # terminal payoff

    print("  Stock price matrix S:")
    print(np.array2string(S, precision=2, suppress_small=True))
    print("\n  Intrinsic value matrix H = max(K - S, 0):")
    print(np.array2string(H, precision=2, suppress_small=True))

    # Backward induction with regression
    for t in range(N - 2, 0, -1):
        print(f"\n  --- Time step t={t} ---")

        good_paths = H[:, t] > 0
        n_good = np.sum(good_paths)
        print(f"  In-the-money paths: {np.where(good_paths)[0]} "
              f"({n_good} paths)")

        if n_good < 3:
            print("  Too few ITM paths for regression, skip.")
            discount_path = V[:, t] == 0
            V[discount_path, t] = V[discount_path, t + 1] * df
            continue

        # Polynomial regression (degree 2) on ITM paths
        rg = np.polyfit(S[good_paths, t],
                        V[good_paths, t + 1] * df, 2)
        C = np.polyval(rg, S[good_paths, t])

        print(f"  Regression coefficients: {rg}")
        print(f"  Continuation values C:  "
              f"{np.array2string(C, precision=4)}")
        print(f"  Intrinsic values H:     "
              f"{np.array2string(H[good_paths, t], precision=4)}")

        # Exercise decision
        exercise = np.zeros(len(good_paths), dtype=bool)
        exercise[good_paths] = H[good_paths, t] > C

        exercised_paths = np.where(exercise)[0]
        print(f"  Exercise at paths: {exercised_paths}")

        V[exercise, t] = H[exercise, t]
        V[exercise, t + 1:] = 0
        discount_path = V[:, t] == 0
        V[discount_path, t] = V[discount_path, t + 1] * df

    V0 = np.mean(V[:, 1]) * df
    print(f"\n  Cash flow matrix V:")
    print(np.array2string(V, precision=4, suppress_small=True))
    print(f"\n  LSM price = E[V(:,1)] * df = {V0:.4f}")

    return {"V0": V0, "S": S, "H": H, "V": V}


# ============================================================================
# 3. PERPETUAL AMERICAN PUT -- ANALYTICAL FORMULA
# ============================================================================

def perpetual_put_analytical(S, K, sigma, r):
    """
    Analytical formula for the perpetual American put option.

    The perpetual put has no expiration (T -> infinity).  The price
    satisfies the ODE:
        0.5*sigma^2*S^2*V'' + r*S*V' - r*V = 0
    with boundary conditions V(inf) = 0 and smooth pasting at S_f.

    The optimal exercise boundary is:
        S_f = K / (sigma^2/(2r) + 1)

    Parameters
    ----------
    S : float or ndarray  Stock price(s).
    K : float             Strike.
    sigma : float         Volatility.
    r : float             Risk-free rate.

    Returns
    -------
    float or ndarray  Perpetual put price(s).
    """
    s0 = K / (sigma**2 / (2 * r) + 1)
    B = sigma**2 / (2 * r) * s0 ** (2 * r / sigma**2 + 1)
    return np.where(S < s0, K - S, B * S ** (-2 * r / sigma**2))


# ============================================================================
# 4. PROJECTED SOR (PSOR) -- NUMERICAL SOLVER FOR FREE BOUNDARY
# ============================================================================

def PSOR(a, b, c, B_vec, C, w=1.999, eps=1e-12, N_max=1000000):
    """
    Projected SOR (Successive Over-Relaxation) solver for the Linear
    Complementarity Problem (LCP) arising in American option pricing.

    Solves:  A*V >= B_vec,  V >= C,  (A*V - B_vec)^T (V - C) = 0
    where A is tridiagonal with diagonals (a, b, c) and C is the
    payoff (constraint).

    The PSOR iteration updates each component and then projects
    onto the feasible set V >= C (early exercise constraint).

    Parameters
    ----------
    a : float      Sub-diagonal coefficient.
    b : float      Main diagonal coefficient.
    c : float      Super-diagonal coefficient.
    B_vec : ndarray  Right-hand side vector (boundary terms).
    C : ndarray     Payoff / constraint vector.
    w : float       Relaxation parameter (1 < w < 2 for over-relaxation).
    eps : float     Convergence tolerance.
    N_max : int     Maximum iterations.

    Returns
    -------
    V : ndarray     Solution satisfying the LCP.
    """
    N = len(C)
    V = C.copy().astype(np.float64)
    V_old = V.copy()

    for k in range(N_max):
        for i in range(N):
            # Standard SOR update
            if i == 0:
                sigma_sum = c * V[i + 1]
            elif i == N - 1:
                sigma_sum = a * V[i - 1]
            else:
                sigma_sum = a * V[i - 1] + c * V[i + 1]

            V_sor = (1 - w) * V[i] + (w / b) * (B_vec[i] - sigma_sum)

            # Projection: enforce V >= C (early exercise constraint)
            V[i] = max(V_sor, C[i])

        # Convergence check
        if np.max(np.abs(V - V_old)) < eps:
            return V

        V_old = V.copy()

    print(f"  PSOR: did not converge in {N_max} iterations")
    return V


def perpetual_put_psor(K, r, sigma, Nspace=10000):
    """
    Numerically solve for the perpetual American put price using PSOR.

    The log-variable ODE:
        0.5*sigma^2*V'' + (r - 0.5*sigma^2)*V' - r*V = 0
    with V(x) >= max(K - e^x, 0) and smooth pasting.

    Parameters
    ----------
    K : float      Strike.
    r : float      Risk-free rate.
    sigma : float  Volatility.
    Nspace : int   Number of grid points.

    Returns
    -------
    dict with keys:
        V : ndarray      Numerical solution.
        x : ndarray      Log-price grid.
        S : ndarray      Stock price grid (exp(x)).
    """
    S_max = 10 * K
    S_min = K / 3
    x_max = np.log(S_max)
    x_min = np.log(S_min)
    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)

    sig2 = sigma * sigma
    dxx = dx * dx

    # Tridiagonal coefficients
    a_coeff = (r - 0.5 * sig2) / (2 * dx) - sig2 / (2 * dxx)
    b_coeff = sig2 / dxx + r
    c_coeff = -(r - 0.5 * sig2) / (2 * dx) - sig2 / (2 * dxx)

    # Payoff (constraint)
    C = np.maximum(K - np.exp(x), 0)

    # Boundary terms
    B_vec = np.zeros(Nspace)
    B_vec[0] = -a_coeff * (K - S_min)
    B_vec[-1] = 0

    V = PSOR(a_coeff, b_coeff, c_coeff, B_vec, C,
             w=1.999, eps=1e-12, N_max=500000)

    return {"V": V, "x": x, "S": np.exp(x)}


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all American option demonstrations."""
    S0, K, T, r, sigma = 100.0, 100.0, 1.0, 0.1, 0.2

    # 1. Binomial tree
    print("=" * 60)
    print("1. American Put -- CRR Binomial Tree")
    print("=" * 60)

    price_bin = american_put_binomial(S0, K, T, r, sigma, N=25000)
    print(f"  American put (N=25000): {price_bin:.6f}")

    # Compare with European
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    eu_put = K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)
    print(f"  European put (BS):      {eu_put:.6f}")
    print(f"  Early exercise premium: {price_bin - eu_put:.6f}")

    # 2. LSM walkthrough
    print("\n" + "=" * 60)
    print("2. Longstaff-Schwartz -- Classic 8-Path Example")
    print("=" * 60)
    lsm_result = lsm_walkthrough()

    # 3. Perpetual put
    print("\n" + "=" * 60)
    print("3. Perpetual American Put")
    print("=" * 60)

    s0_star = K / (sigma**2 / (2 * r) + 1)
    print(f"  Optimal exercise boundary: S_f = {s0_star:.4f}")

    # Analytical
    S_plot = np.linspace(60, 160, 1000)
    V_anal = perpetual_put_analytical(S_plot, K, sigma, r)

    # Numerical (PSOR)
    print("  Running PSOR solver...")
    psor_result = perpetual_put_psor(K, r, sigma, Nspace=10000)
    V_num = psor_result["V"]
    S_num = psor_result["S"]

    # Compare at S0 = 100
    price_anal = perpetual_put_analytical(S0, K, sigma, r)
    price_num = np.interp(np.log(S0), psor_result["x"], V_num)
    print(f"  Analytical price at S0={S0}: {price_anal:.6f}")
    print(f"  Numerical (PSOR) at S0={S0}: {price_num:.6f}")
    print(f"  Difference:                  {abs(price_anal - price_num):.2e}")

    # Plot perpetual put
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(S_plot[::10], perpetual_put_analytical(S_plot[::10], K, sigma, r),
             "*", label="Analytical", markersize=4)
    ax1.plot(S_num, V_num, label="PSOR numerical", alpha=0.7)
    ax1.plot(S_num, np.maximum(K - S_num, 0), "--",
             label="Payoff", alpha=0.5)
    ax1.axvline(x=s0_star, color="k", ls="--", alpha=0.5,
                label=f"S_f = {s0_star:.2f}")
    ax1.set_xlim(30, 200)
    ax1.set_ylim(-1, 70)
    ax1.set_xlabel("S")
    ax1.set_ylabel("V(S)")
    ax1.set_title("Perpetual Put: Analytical vs PSOR")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Error plot
    V_anal_on_grid = perpetual_put_analytical(S_num, K, sigma, r)
    ax2.plot(S_num, V_anal_on_grid - V_num, label="Error")
    ax2.set_xlabel("S")
    ax2.set_ylabel("Analytical - Numerical")
    ax2.set_title("Difference: Analytical - PSOR")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
