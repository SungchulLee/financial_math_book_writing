#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_linear_solvers_extended.py
Extended Linear System Solvers: LU, Jacobi, Gauss-Seidel, TDMA, Tridiagonal SOR

Credits
-------
Based on notebooks "A.1 Solution of linear equations" and
"A.2 Optimize and speed up the code (SOR algorithm, Cython and C)" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 8 -- FDM for BS PDE).

Topics covered
--------------
1. LU decomposition (scipy): factorisation, permutation, forward/backward
   substitution.
2. Jacobi iterative method: A = D + R splitting.
3. Gauss-Seidel iterative method: A = L + U splitting with triangular solve.
4. TDMA (Thomas Algorithm): pure Python implementation for tridiagonal systems.
5. Tridiagonal SOR: optimised SOR that exploits the tridiagonal structure,
   using scalar diagonal coefficients instead of full matrix access.
6. Convergence comparison across all methods.

Companion file
--------------
The existing cantaro86_solvers.py covers:
    - Thomas algorithm (LAPACK dgtsv wrapper)
    - SOR (matrix form)
    - SOR2 (element-wise, general matrix)
This file adds the algorithms NOT covered there.
"""

import numpy as np
import time
from scipy.linalg import norm, solve_triangular
import scipy.linalg


# ============================================================================
# 1. LU DECOMPOSITION
# ============================================================================

def lu_solve_demo(A, b):
    """
    Solve A x = b via LU decomposition using scipy.

    Performs PA = LU factorisation, then solves:
        1. L y = P^T b  (forward substitution)
        2. U x = y       (backward substitution)

    Parameters
    ----------
    A : ndarray, shape (n, n)
        Square coefficient matrix.
    b : ndarray, shape (n,) or (n, 1)
        Right-hand side vector.

    Returns
    -------
    dict with keys:
        x : ndarray        Solution vector.
        P, L, U : ndarray  Factorisation matrices (PA = LU).
        residual : float   ||Ax - b||.
    """
    P, L, U = scipy.linalg.lu(A)

    # Forward substitution: L y = P^T b
    b_flat = b.ravel()
    y = solve_triangular(L, P.T @ b_flat, lower=True)
    # Backward substitution: U x = y
    x = solve_triangular(U, y, lower=False)

    residual = norm(A @ x - b_flat)

    return {"x": x, "P": P, "L": L, "U": U, "residual": residual}


def lu_factor_solve(A, b):
    """
    Solve A x = b using scipy's compact LU factorisation (lu_factor/lu_solve).

    This uses LAPACK's dgetrf for the factorisation and dgetrs for the solve,
    which is more memory-efficient than the full P, L, U form.

    Parameters
    ----------
    A : ndarray, shape (n, n)
    b : ndarray, shape (n,) or (n, 1)

    Returns
    -------
    x : ndarray  Solution vector.
    """
    LU, piv = scipy.linalg.lu_factor(A)
    x = scipy.linalg.lu_solve((LU, piv), b.ravel())
    return x


# ============================================================================
# 2. JACOBI ITERATIVE METHOD
# ============================================================================

def jacobi(A, b, eps=1e-10, N_max=1000):
    """
    Solve A x = b using the Jacobi iterative method.

    Splits A = D + R where D is the diagonal and R is the remainder.
    The iteration is:
        x^{k+1} = D^{-1} (b - R x^{k})

    Convergence is guaranteed when A is strictly diagonally dominant:
        |A_{ii}| > sum_{j!=i} |A_{ij}| for all i.

    Parameters
    ----------
    A : ndarray, shape (n, n)
        Coefficient matrix (should be diagonally dominant for convergence).
    b : ndarray, shape (n,) or (n, 1)
        Right-hand side.
    eps : float
        Convergence tolerance.
    N_max : int
        Maximum iterations.

    Returns
    -------
    dict with keys:
        x : ndarray          Solution vector.
        iterations : int     Number of iterations to converge.
        converged : bool     Whether convergence was achieved.
    """
    b = b.ravel()
    n = len(b)
    D_inv = np.diag(1.0 / np.diag(A))
    R = A - np.diag(np.diag(A))

    x0 = np.ones(n)

    for k in range(1, N_max + 1):
        x_new = D_inv @ (b - R @ x0)
        if norm(x_new - x0) < eps:
            return {"x": x_new, "iterations": k, "converged": True}
        x0 = x_new

    return {"x": x_new, "iterations": N_max, "converged": False}


# ============================================================================
# 3. GAUSS-SEIDEL ITERATIVE METHOD
# ============================================================================

def gauss_seidel(A, b, eps=1e-10, N_max=1000):
    """
    Solve A x = b using the Gauss-Seidel iterative method.

    Splits A = L + U where L is the lower triangular part (including
    diagonal) and U is the strict upper triangular part.
    The iteration is:
        L x^{k+1} = b - U x^{k}
    which is solved by forward substitution (triangular solve).

    Gauss-Seidel converges faster than Jacobi because it uses the
    most recently updated components within each iteration.

    Parameters
    ----------
    A : ndarray, shape (n, n)
    b : ndarray, shape (n,) or (n, 1)
    eps : float
        Convergence tolerance.
    N_max : int
        Maximum iterations.

    Returns
    -------
    dict with keys:
        x : ndarray          Solution vector.
        iterations : int     Number of iterations to converge.
        converged : bool     Whether convergence was achieved.
    """
    b = b.ravel()
    U = np.triu(A, k=1)
    L = np.tril(A)

    x0 = np.ones(len(b))

    for k in range(1, N_max + 1):
        x_new = solve_triangular(L, b - U @ x0, lower=True)
        if norm(x_new - x0) < eps:
            return {"x": x_new, "iterations": k, "converged": True}
        x0 = x_new

    return {"x": x_new, "iterations": N_max, "converged": False}


# ============================================================================
# 4. TDMA -- PURE PYTHON THOMAS ALGORITHM
# ============================================================================

def TDMA(A, b):
    """
    Solve a tridiagonal system A x = b using the Thomas algorithm
    (pure Python implementation without LAPACK).

    This is the Tri-Diagonal-Matrix-Algorithm: a simplified Gaussian
    elimination that exploits the tridiagonal structure for O(n) complexity.

    The algorithm has two phases:
        1. Forward sweep: eliminate sub-diagonal entries.
        2. Backward substitution: solve from the last equation upward.

    Parameters
    ----------
    A : ndarray, shape (n, n)
        Tridiagonal coefficient matrix.
    b : ndarray, shape (n,) or (n, 1)
        Right-hand side vector.

    Returns
    -------
    x : ndarray, shape (n,)
        Solution vector.
    """
    b = b.ravel().copy()
    N = len(b)
    a = A.diagonal(offset=-1).copy()   # sub-diagonal
    d = A.diagonal(offset=0).copy()    # main diagonal
    c = A.diagonal(offset=1).copy()    # super-diagonal

    x = np.zeros(N)

    # Forward sweep: eliminate sub-diagonal
    for i in range(1, N):
        w = a[i - 1] / d[i - 1]
        d[i] = d[i] - w * c[i - 1]
        b[i] = b[i] - w * b[i - 1]

    # Backward substitution
    x[-1] = b[-1] / d[-1]
    for i in range(N - 2, -1, -1):
        x[i] = (b[i] - c[i] * x[i + 1]) / d[i]

    return x


# ============================================================================
# 5. TRIDIAGONAL SOR (OPTIMISED)
# ============================================================================

def SOR_tridiag(A, b, w=1.0, eps=1e-10, N_max=100):
    """
    SOR iteration exploiting tridiagonal structure.

    Instead of computing the full inner product sum_{j!=i} A_{ij}*x_j,
    only accesses the three non-zero neighbours A[i,i-1], A[i,i], A[i,i+1].
    This reduces the per-iteration cost from O(n^2) to O(n).

    Parameters
    ----------
    A : ndarray, shape (n, n)
        Tridiagonal coefficient matrix.
    b : ndarray, shape (n,)
        Right-hand side.
    w : float
        Relaxation parameter (w=1 gives Gauss-Seidel).
    eps : float
        Convergence tolerance.
    N_max : int
        Maximum iterations.

    Returns
    -------
    dict with keys:
        x : ndarray          Solution vector.
        iterations : int     Number of iterations.
        converged : bool     Whether convergence was achieved.
    """
    b = b.ravel()
    N = len(b)
    x0 = np.ones(N, dtype=np.float64)
    x_new = np.ones(N, dtype=np.float64)

    for k in range(1, N_max + 1):
        for i in range(N):
            if i == 0:
                S = A[0, 1] * x_new[1]
            elif i == N - 1:
                S = A[N - 1, N - 2] * x_new[N - 2]
            else:
                S = A[i, i - 1] * x_new[i - 1] + A[i, i + 1] * x_new[i + 1]
            x_new[i] = (1 - w) * x_new[i] + (w / A[i, i]) * (b[i] - S)

        if norm(x_new - x0) < eps:
            return {"x": x_new, "iterations": k, "converged": True}
        x0 = x_new.copy()

    return {"x": x_new, "iterations": N_max, "converged": False}


def SOR_scalar(aa, bb, cc, b, w=1.0, eps=1e-10, N_max=100):
    """
    SOR iteration for a tridiagonal system with CONSTANT diagonals.

    When the tridiagonal matrix has the same value on each diagonal:
        A = tridiag(aa, bb, cc)
    we can avoid storing/accessing the matrix entirely and use just the
    three scalar coefficients. This is the fastest pure Python variant.

    Parameters
    ----------
    aa : float  Sub-diagonal value.
    bb : float  Main diagonal value.
    cc : float  Super-diagonal value.
    b : ndarray, shape (n,)
        Right-hand side.
    w : float   Relaxation parameter.
    eps : float Convergence tolerance.
    N_max : int Maximum iterations.

    Returns
    -------
    dict with keys:
        x : ndarray          Solution vector.
        iterations : int     Number of iterations.
        converged : bool     Whether convergence was achieved.
    """
    b = np.asarray(b, dtype=np.float64).ravel()
    N = len(b)
    x0 = np.ones(N, dtype=np.float64)
    x_new = np.ones(N, dtype=np.float64)

    for k in range(1, N_max + 1):
        for i in range(N):
            if i == 0:
                S = cc * x_new[1]
            elif i == N - 1:
                S = aa * x_new[N - 2]
            else:
                S = aa * x_new[i - 1] + cc * x_new[i + 1]
            x_new[i] = (1 - w) * x_new[i] + (w / bb) * (b[i] - S)

        if norm(x_new - x0) < eps:
            return {"x": x_new, "iterations": k, "converged": True}
        x0 = x_new.copy()

    return {"x": x_new, "iterations": N_max, "converged": False}


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all linear solver demonstrations."""

    # ---- Test system: diagonally dominant 4x4 ----
    print("=" * 60)
    print("1. LU Decomposition")
    print("=" * 60)

    A = np.array([[2, 5, 8, 7],
                  [5, 2, 2, 8],
                  [7, 5, 6, 6],
                  [5, 4, 4, 8]], dtype=float)
    x_true = np.array([1, 2, 3, 4], dtype=float)
    b = A @ x_true

    print(f"  Matrix A (rank={np.linalg.matrix_rank(A)}, "
          f"det={np.linalg.det(A):.2f}):")
    print(f"  {A}")
    print(f"  True x: {x_true}")

    # LU decomposition
    result = lu_solve_demo(A, b)
    print(f"\n  LU solution: {result['x'].round(6)}")
    print(f"  Residual: {result['residual']:.2e}")

    # lu_factor/lu_solve
    x_compact = lu_factor_solve(A, b)
    print(f"  lu_factor solution: {x_compact.round(6)}")

    # ---- Iterative methods: diagonally dominant system ----
    print("\n" + "=" * 60)
    print("2. Iterative Methods: Jacobi vs Gauss-Seidel vs SOR")
    print("=" * 60)

    A_dd = np.array([[10, 5, 2, 1],
                     [2, 15, 2, 3],
                     [1, 8, 13, 1],
                     [2, 3, 1, 8]], dtype=float)
    x_true2 = np.array([1, 2, 3, 4], dtype=float)
    b2 = A_dd @ x_true2

    print(f"  Diagonally dominant matrix (rank={np.linalg.matrix_rank(A_dd)}):")
    print(f"  {A_dd}")

    jac = jacobi(A_dd, b2)
    gs = gauss_seidel(A_dd, b2)
    print(f"\n  Jacobi:       {jac['iterations']:>3d} iterations, "
          f"error={norm(jac['x'] - x_true2):.2e}")
    print(f"  Gauss-Seidel: {gs['iterations']:>3d} iterations, "
          f"error={norm(gs['x'] - x_true2):.2e}")
    print(f"  (Gauss-Seidel converges ~{jac['iterations']/max(gs['iterations'],1):.1f}x "
          f"faster than Jacobi)")

    # ---- Thomas/TDMA for tridiagonal ----
    print("\n" + "=" * 60)
    print("3. TDMA (Pure Python Thomas Algorithm)")
    print("=" * 60)

    A_tri = np.array([[10, 5, 0, 0],
                      [2, 15, 2, 0],
                      [0, 8, 13, 1],
                      [0, 0, 1, 8]], dtype=float)
    x_true3 = np.array([1, 2, 3, 4], dtype=float)
    b3 = A_tri @ x_true3

    x_tdma = TDMA(A_tri, b3)
    print(f"  Tridiagonal matrix:")
    print(f"  {A_tri}")
    print(f"  TDMA solution: {x_tdma.round(6)}")
    print(f"  Error: {norm(x_tdma - x_true3):.2e}")

    # ---- Tridiagonal SOR comparison ----
    print("\n" + "=" * 60)
    print("4. Tridiagonal SOR: Matrix vs Scalar Diagonal")
    print("=" * 60)

    N = 500
    aa, bb, cc = 2.0, 10.0, 5.0
    A_big = (np.diag(aa * np.ones(N - 1), -1) +
             np.diag(bb * np.ones(N), 0) +
             np.diag(cc * np.ones(N - 1), 1))
    x_true_big = 2.0 * np.ones(N)
    b_big = A_big @ x_true_big

    # TDMA (direct)
    t0 = time.perf_counter()
    x_direct = TDMA(A_big, b_big)
    t_tdma = time.perf_counter() - t0

    # Tridiagonal SOR (matrix access)
    t0 = time.perf_counter()
    sor_tri = SOR_tridiag(A_big, b_big, w=1.0)
    t_sor_tri = time.perf_counter() - t0

    # Scalar diagonal SOR
    t0 = time.perf_counter()
    sor_sc = SOR_scalar(aa, bb, cc, b_big, w=1.0)
    t_sor_sc = time.perf_counter() - t0

    print(f"  System size: {N}x{N}, constant diagonals: "
          f"a={aa}, b={bb}, c={cc}")
    print(f"\n  {'Method':<25s} {'Time (ms)':>10s} {'Iters':>7s} {'Error':>12s}")
    print(f"  {'-'*25} {'-'*10} {'-'*7} {'-'*12}")
    print(f"  {'TDMA (direct)':<25s} {t_tdma*1000:10.3f} {'N/A':>7s} "
          f"{norm(x_direct - x_true_big):12.2e}")
    print(f"  {'SOR tridiag (w=1.0)':<25s} {t_sor_tri*1000:10.3f} "
          f"{sor_tri['iterations']:>7d} {norm(sor_tri['x'] - x_true_big):12.2e}")
    print(f"  {'SOR scalar (w=1.0)':<25s} {t_sor_sc*1000:10.3f} "
          f"{sor_sc['iterations']:>7d} {norm(sor_sc['x'] - x_true_big):12.2e}")

    # ---- Relaxation parameter study ----
    print("\n" + "=" * 60)
    print("5. SOR Convergence: Effect of Relaxation Parameter w")
    print("=" * 60)

    w_values = [0.5, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
    print(f"  {'w':>6s} {'Iterations':>12s} {'Error':>12s}")
    print(f"  {'-'*6} {'-'*12} {'-'*12}")
    for w_test in w_values:
        res = SOR_scalar(aa, bb, cc, b_big, w=w_test, N_max=500)
        err = norm(res["x"] - x_true_big)
        status = f"{res['iterations']}" if res["converged"] else "FAIL"
        print(f"  {w_test:6.2f} {status:>12s} {err:12.2e}")

    # ---- All methods comparison on larger system ----
    print("\n" + "=" * 60)
    print("6. Full Comparison: All Solvers on Diag-Dominant System")
    print("=" * 60)

    n = 200
    np.random.seed(42)
    lower = -0.3 * np.random.rand(n - 1)
    upper = -0.3 * np.random.rand(n - 1)
    main = 3.0 + np.random.rand(n)
    A_test = np.diag(main) + np.diag(lower, -1) + np.diag(upper, 1)
    b_test = np.random.randn(n)
    x_ref = lu_factor_solve(A_test, b_test)

    methods = [
        ("LU (lu_factor)", lambda: lu_factor_solve(A_test, b_test)),
        ("TDMA", lambda: TDMA(A_test, b_test)),
        ("Jacobi", lambda: jacobi(A_test, b_test)["x"]),
        ("Gauss-Seidel", lambda: gauss_seidel(A_test, b_test)["x"]),
        ("SOR tridiag (w=1.2)", lambda: SOR_tridiag(A_test, b_test, w=1.2)["x"]),
    ]

    print(f"  {'Method':<25s} {'Time (ms)':>10s} {'Error vs LU':>15s}")
    print(f"  {'-'*25} {'-'*10} {'-'*15}")
    for name, fn in methods:
        t0 = time.perf_counter()
        x_sol = fn()
        elapsed = (time.perf_counter() - t0) * 1000
        err = norm(x_sol - x_ref)
        print(f"  {name:<25s} {elapsed:10.3f} {err:15.2e}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
