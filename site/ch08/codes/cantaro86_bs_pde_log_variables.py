#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_bs_pde_log_variables.py
Black-Scholes PDE Solver in Log-Variables with Sparse Matrices

Credits
-------
Based on notebook "2.1 Black-Scholes PDE and sparse matrices" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 8 -- FDM for BS PDE).

Topics covered
--------------
1. Transformation to log-variables: x = log(S) simplifies the PDE
   to constant coefficients, avoiding the non-uniform grid problem.
2. Implicit finite difference discretisation producing a tridiagonal
   system at each time step.
3. Sparse matrix construction using scipy.sparse.diags.
4. Solver comparison: spsolve, splu (LU factorisation), Thomas algorithm.
5. European call and put pricing with visualisation of price curves
   and 3D price surfaces.
"""

import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import sparse
from scipy.sparse.linalg import spsolve, splu
from scipy.linalg.lapack import get_lapack_funcs
from scipy.linalg.misc import LinAlgError


# ============================================================================
# 1. THOMAS ALGORITHM (TRIDIAGONAL DIRECT SOLVER)
# ============================================================================

def Thomas(A, b):
    """
    Solve the tridiagonal system A x = b using the Thomas algorithm
    (LAPACK dgtsv wrapper).  O(n) time and space.

    Parameters
    ----------
    A : ndarray or sparse, shape (n, n)
        Tridiagonal coefficient matrix.
    b : ndarray, shape (n,)
        Right-hand side vector.

    Returns
    -------
    x : ndarray, shape (n,)
    """
    if sparse.issparse(A):
        A = A.toarray()
    D = A.diagonal(0).copy()
    L = A.diagonal(-1).copy()
    U = A.diagonal(1).copy()

    (dgtsv,) = get_lapack_funcs(("gtsv",))
    du2, d, du, x, info = dgtsv(L, D, U, b)
    if info == 0:
        return x
    raise LinAlgError("Singular matrix at diagonal %d" % (info - 1))


# ============================================================================
# 2. IMPLICIT FD SCHEME IN LOG-VARIABLES
# ============================================================================

def bs_pde_implicit_log(S0, K, T, r, sigma, Nspace=3000, Ntime=2000,
                        payoff="call", solver="spsolve"):
    """
    Price a European option by solving the Black-Scholes PDE in
    log-variables using an implicit finite difference scheme.

    The transformation x = log(S) yields a PDE with constant
    coefficients:
        dV/dt + 0.5*sigma^2 * d^2V/dx^2 + (r - 0.5*sigma^2) * dV/dx - rV = 0

    The implicit discretisation at each backward time step gives:
        D * V^n = V^{n+1} + offset
    where D is a tridiagonal matrix.

    Parameters
    ----------
    S0 : float      Current stock price.
    K : float       Strike price.
    T : float       Time to maturity.
    r : float       Risk-free rate.
    sigma : float   Volatility.
    Nspace : int    Number of spatial grid points.
    Ntime : int     Number of time steps.
    payoff : str    "call" or "put".
    solver : str    "spsolve", "splu", or "Thomas".

    Returns
    -------
    dict with keys:
        price : float          Option price at S0.
        S_grid : ndarray       Stock price grid.
        V_curve : ndarray      Option value curve at t=0.
        V_surface : ndarray    Full price grid (Nspace x Ntime).
        T_grid : ndarray       Time grid.
        payoff_curve : ndarray Payoff function values.
        elapsed : float        Wall-clock time (seconds).
    """
    X0 = np.log(S0)

    # Spatial domain in log-space
    S_max = 3 * float(K)
    S_min = float(K) / 3
    x_max = np.log(S_max)
    x_min = np.log(S_min)

    # Discretisation
    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)
    T_vec, dt = np.linspace(0, T, Ntime, retstep=True)

    # Terminal condition (payoff)
    if payoff == "call":
        Payoff = np.maximum(np.exp(x) - K, 0)
    elif payoff == "put":
        Payoff = np.maximum(K - np.exp(x), 0)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    # Grid initialisation
    V = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)

    # Terminal condition
    V[:, -1] = Payoff

    # Boundary conditions (all time steps)
    if payoff == "call":
        V[-1, :] = np.exp(x_max) - K * np.exp(-r * T_vec[::-1])
        V[0, :] = 0
    else:  # put
        V[-1, :] = 0
        V[0, :] = K * np.exp(-r * T_vec[::-1]) - np.exp(x_min)

    # Tridiagonal matrix coefficients
    sig2 = sigma * sigma
    dxx = dx * dx
    a = (dt / 2) * ((r - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r)
    c = -(dt / 2) * ((r - 0.5 * sig2) / dx + sig2 / dxx)

    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()

    # Pre-factorise if using splu
    t0 = time.perf_counter()
    if solver == "splu":
        DD = splu(D)

    # Backward iteration
    for i in range(Ntime - 2, -1, -1):
        offset[0] = a * V[0, i]
        offset[-1] = c * V[-1, i]
        rhs = V[1:-1, i + 1] - offset

        if solver == "spsolve":
            V[1:-1, i] = spsolve(D, rhs)
        elif solver == "splu":
            V[1:-1, i] = DD.solve(rhs)
        elif solver == "Thomas":
            V[1:-1, i] = Thomas(D, rhs)
        else:
            raise ValueError("solver must be 'spsolve', 'splu', or 'Thomas'")

    elapsed = time.perf_counter() - t0

    # Interpolate the price at S0
    price = np.interp(X0, x, V[:, 0])

    return {
        "price": price,
        "S_grid": np.exp(x),
        "V_curve": V[:, 0],
        "V_surface": V,
        "T_grid": T_vec,
        "payoff_curve": Payoff,
        "elapsed": elapsed,
    }


# ============================================================================
# 3. ANALYTICAL BLACK-SCHOLES (FOR COMPARISON)
# ============================================================================

def bs_analytical(payoff, S0, K, T, r, sigma):
    """Analytical BS price for reference."""
    import scipy.stats as ss
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if payoff == "call":
        return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)


# ============================================================================
# 4. VISUALISATION
# ============================================================================

def plot_price_curve(result, S0, K, payoff="call"):
    """Plot the option price curve at t=0 alongside the payoff."""
    S = result["S_grid"]
    V = result["V_curve"]
    Pay = result["payoff_curve"]

    plt.figure(figsize=(10, 5))
    plt.plot(S, Pay, color="blue", label="Payoff")
    plt.plot(S, V, color="red", label=f"BS {payoff} price (PDE)")
    plt.xlim(K * 0.6, K * 1.7)
    if payoff == "call":
        plt.ylim(0, K * 0.5)
    else:
        plt.ylim(0, K * 0.5)
    plt.xlabel("S")
    plt.ylabel("Price")
    plt.legend(loc="upper left")
    plt.title(f"Black-Scholes {payoff} price at t=0 (Implicit FD, log-variables)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_price_surface(result, K, payoff="call"):
    """Plot the 3D price surface V(S, t)."""
    S = result["S_grid"]
    T_vec = result["T_grid"]
    V = result["V_surface"]

    X, Y = np.meshgrid(T_vec, S)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(Y, X, V, cmap=cm.ocean, alpha=0.8)
    ax.set_title(f"BS {payoff} price surface (Implicit FD)")
    ax.set_xlabel("S")
    ax.set_ylabel("t")
    ax.set_zlabel("V")
    ax.view_init(30, -100)
    plt.tight_layout()
    plt.show()


# ============================================================================
# 5. SOLVER TIMING COMPARISON
# ============================================================================

def compare_solvers(S0, K, T, r, sigma, Nspace=5000, Ntime=4000):
    """
    Compare spsolve, splu, and Thomas solver performance on the
    same BS PDE problem.
    """
    results = {}
    for solver in ["spsolve", "splu", "Thomas"]:
        res = bs_pde_implicit_log(S0, K, T, r, sigma,
                                   Nspace=Nspace, Ntime=Ntime,
                                   payoff="call", solver=solver)
        results[solver] = res
        print(f"  {solver:>8s}: price = {res['price']:.6f}, "
              f"time = {res['elapsed']:.4f} s")
    return results


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all BS PDE demonstrations."""
    S0, K, T, r, sigma = 100, 100, 1, 0.1, 0.2

    # 1. European call via PDE
    print("=" * 60)
    print("1. European CALL -- Implicit FD in log-variables")
    print("=" * 60)

    result_call = bs_pde_implicit_log(S0, K, T, r, sigma,
                                       Nspace=3000, Ntime=2000,
                                       payoff="call", solver="splu")
    call_analytical = bs_analytical("call", S0, K, T, r, sigma)
    print(f"  PDE price:        {result_call['price']:.6f}")
    print(f"  Analytical price: {call_analytical:.6f}")
    print(f"  Error:            {abs(result_call['price'] - call_analytical):.2e}")

    plot_price_curve(result_call, S0, K, "call")
    plot_price_surface(result_call, K, "call")

    # 2. European put via PDE
    print("\n" + "=" * 60)
    print("2. European PUT -- Implicit FD in log-variables")
    print("=" * 60)

    result_put = bs_pde_implicit_log(S0, K, T, r, sigma,
                                      Nspace=3000, Ntime=2000,
                                      payoff="put", solver="splu")
    put_analytical = bs_analytical("put", S0, K, T, r, sigma)
    print(f"  PDE price:        {result_put['price']:.6f}")
    print(f"  Analytical price: {put_analytical:.6f}")
    print(f"  Error:            {abs(result_put['price'] - put_analytical):.2e}")

    plot_price_curve(result_put, S0, K, "put")

    # 3. Solver comparison
    print("\n" + "=" * 60)
    print("3. Solver Performance Comparison (Nspace=5000, Ntime=4000)")
    print("=" * 60)
    compare_solvers(S0, K, T, r, sigma, Nspace=5000, Ntime=4000)

    # 4. Grid convergence
    print("\n" + "=" * 60)
    print("4. Grid Convergence Study")
    print("=" * 60)

    grids = [(500, 500), (1000, 1000), (2000, 2000), (3000, 2000),
             (5000, 4000)]
    for Ns, Nt in grids:
        res = bs_pde_implicit_log(S0, K, T, r, sigma,
                                   Nspace=Ns, Ntime=Nt,
                                   payoff="call", solver="splu")
        err = abs(res["price"] - call_analytical)
        print(f"  Nspace={Ns:>5d}, Ntime={Nt:>5d}: "
              f"price={res['price']:.6f}, error={err:.2e}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
