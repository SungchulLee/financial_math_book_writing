#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_solvers.py
====================
Thomas Algorithm (Tridiagonal Solver) and SOR (Successive Over-Relaxation)
for solving sparse linear systems arising in Finite Difference Methods (FDM)
for the Black-Scholes PDE.

Based on Solvers.py from:
    cantaro86 - Financial-Models-Numerical-Methods
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Key Algorithms:
    1. Thomas Algorithm  -- O(n) direct solver for tridiagonal systems
       Wraps LAPACK dgtsv for numerical stability and speed.
    2. SOR (matrix form) -- iterative solver with relaxation parameter w
       w = 1 gives Gauss-Seidel; w in (1,2) gives over-relaxation.
    3. SOR2 (element-wise) -- pedagogical version using explicit loops.

These solvers are fundamental building blocks for implicit / Crank-Nicolson
finite difference schemes applied to the Black-Scholes PDE:
    dV/dt + 0.5*sigma^2*S^2*d2V/dS2 + r*S*dV/dS - r*V = 0

At each time step the FDM discretisation produces a tridiagonal system
    A * V^{n} = b(V^{n+1})
which must be solved efficiently.

License: MIT (see original repository)
"""

import numpy as np
from scipy import sparse
from scipy.linalg import norm, solve_triangular
from scipy.linalg.lapack import get_lapack_funcs
from scipy.linalg.misc import LinAlgError


# ============================================================================
# Thomas Algorithm (wrapper around LAPACK dgtsv)
# ============================================================================

def Thomas(A, b):
    """
    Solve the tridiagonal linear system  A x = b  using the Thomas algorithm.

    This is a thin wrapper around LAPACK's dgtsv routine, which performs
    LU factorisation of a tridiagonal matrix in O(n) time and O(n) space.

    Parameters
    ----------
    A : ndarray or sparse matrix, shape (n, n)
        Tridiagonal coefficient matrix.  Only the three diagonals are used:
            L = A.diagonal(-1)  -- lower diagonal  (length n-1)
            D = A.diagonal(0)   -- main diagonal   (length n)
            U = A.diagonal(1)   -- upper diagonal  (length n-1)
    b : ndarray, shape (n,)
        Right-hand side vector.

    Returns
    -------
    x : ndarray, shape (n,)
        Solution vector.

    Raises
    ------
    ValueError
        If A is not square or dimensions are incompatible.
    LinAlgError
        If the matrix is singular.

    Notes
    -----
    The Thomas algorithm is the standard choice for tridiagonal systems
    because it is both exact (no iteration) and fast -- O(n) operations.
    In FDM for the Black-Scholes PDE the coefficient matrix is always
    tridiagonal, making this the ideal solver.

    Reference: cantaro86/Financial-Models-Numerical-Methods, Solvers.py
    """
    # Extract the three diagonals
    D = A.diagonal(0)
    L = A.diagonal(-1)
    U = A.diagonal(1)

    # Input validation
    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Expected square matrix")
    if A.shape[0] != b.shape[0]:
        raise ValueError("Incompatible dimensions: A is {}x{}, b has length {}".format(
            A.shape[0], A.shape[1], b.shape[0]))

    # Call LAPACK dgtsv -- general tridiagonal solver
    (dgtsv,) = get_lapack_funcs(("gtsv",))
    du2, d, du, x, info = dgtsv(L, D, U, b)

    if info == 0:
        return x
    if info > 0:
        raise LinAlgError(
            "Singular matrix: resolution failed at diagonal %d" % (info - 1))


# ============================================================================
# SOR -- Successive Over-Relaxation (matrix form)
# ============================================================================

def SOR(A, b, w=1.0, eps=1e-10, N_max=100):
    """
    Solve the linear system  A x = b  using Successive Over-Relaxation (SOR).

    The matrix A is decomposed as  A = L + D + U  where
        L = strict lower triangular part
        D = diagonal part
        U = strict upper triangular part

    The SOR iteration is:
        (D + w*L) x^{k+1} = w*b - [w*U + (w-1)*D] x^{k}

    Parameters
    ----------
    A : ndarray or sparse matrix, shape (n, n)
        Coefficient matrix (must be nonsingular with nonzero diagonal).
    b : ndarray, shape (n,)
        Right-hand side vector.
    w : float, default 1.0
        Relaxation parameter.
            w = 1   -->  Gauss-Seidel iteration
            1 < w < 2  -->  over-relaxation (faster convergence for many PDE systems)
            0 < w < 1  -->  under-relaxation (can stabilise divergent cases)
    eps : float, default 1e-10
        Convergence tolerance on the norm of successive iterates.
    N_max : int, default 100
        Maximum number of iterations.

    Returns
    -------
    x : ndarray, shape (n,)
        Approximate solution vector.

    Raises
    ------
    ValueError
        If the method fails to converge within N_max iterations.

    Notes
    -----
    SOR is useful for American option pricing where the free-boundary
    problem produces an LCP (Linear Complementarity Problem).  The
    Projected SOR (PSOR) variant enforces the early exercise constraint
    at each iteration.

    For European options the Thomas algorithm (direct solver) is preferred
    because the system is tridiagonal and can be solved in O(n).

    Reference: cantaro86/Financial-Models-Numerical-Methods, Solvers.py
    """
    x0 = b.copy()  # initial guess

    # Decompose A = L + D + U
    if sparse.issparse(A):
        D = sparse.diags(A.diagonal())         # diagonal
        U = sparse.triu(A, k=1)                # strict upper triangular
        L = sparse.tril(A, k=-1)               # strict lower triangular
        DD = (w * L + D).toarray()             # (D + wL) for the triangular solve
    else:
        D = np.eye(A.shape[0]) * np.diag(A)   # diagonal
        U = np.triu(A, k=1)                   # strict upper triangular
        L = np.tril(A, k=-1)                  # strict lower triangular
        DD = w * L + D

    for i in range(1, N_max + 1):
        # SOR update: solve (D + wL) x_new = w*b - w*U*x0 - (w-1)*D*x0
        rhs = w * b - w * U @ x0 - (w - 1) * D @ x0
        x_new = solve_triangular(DD, rhs, lower=True)

        if norm(x_new - x0) < eps:
            return x_new
        x0 = x_new

        if i == N_max:
            raise ValueError("SOR failed to converge in {} iterations".format(i))


# ============================================================================
# SOR2 -- element-wise version (pedagogical)
# ============================================================================

def SOR2(A, b, w=1.0, eps=1e-10, N_max=100):
    """
    Solve A x = b using element-wise SOR iteration (pedagogical version).

    This implementation uses explicit Python loops over matrix elements,
    making the algorithm transparent but slow for large systems.  For
    production use, prefer the matrix-form SOR() above.

    The update formula for each component i is:
        x_i^{k+1} = (1-w)*x_i^{k} + (w / A_{ii}) * (b_i - sum_{j!=i} A_{ij}*x_j)

    where x_j on the right-hand side uses the most recent value (Gauss-Seidel
    style within-iteration update).

    Parameters
    ----------
    A : ndarray, shape (n, n)
    b : ndarray, shape (n,)
    w : float, relaxation parameter
    eps : float, convergence tolerance
    N_max : int, maximum iterations

    Returns
    -------
    x : ndarray, shape (n,)

    Reference: cantaro86/Financial-Models-Numerical-Methods, Solvers.py
    """
    N = len(b)
    x0 = np.ones_like(b, dtype=np.float64)
    x_new = np.ones_like(x0)

    for k in range(1, N_max + 1):
        for i in range(N):
            S = 0.0
            for j in range(N):
                if j != i:
                    S += A[i, j] * x_new[j]
            x_new[i] = (1 - w) * x_new[i] + (w / A[i, i]) * (b[i] - S)

        if norm(x_new - x0) < eps:
            return x_new
        x0 = x_new.copy()

        if k == N_max:
            print("SOR2 failed to converge in {} iterations".format(k))
            return x_new


# ============================================================================
# Demo / Main
# ============================================================================

if __name__ == "__main__":
    from scipy.sparse.linalg import spsolve

    print("=" * 72)
    print("  TRIDIAGONAL SOLVERS DEMO")
    print("  Thomas Algorithm vs scipy.sparse.linalg.spsolve vs SOR")
    print("=" * 72)

    # ---- Build a diagonally dominant tridiagonal system ----
    # This is the type of system that arises in implicit FDM for BS PDE
    n = 200
    np.random.seed(42)

    # Diagonals: lower, main, upper
    lower_diag = -0.5 * np.random.rand(n - 1)        # sub-diagonal
    upper_diag = -0.3 * np.random.rand(n - 1)        # super-diagonal
    main_diag = 2.0 + np.random.rand(n)              # dominant main diagonal

    # Build dense tridiagonal matrix
    A_dense = np.diag(main_diag) + np.diag(lower_diag, -1) + np.diag(upper_diag, 1)

    # Build sparse version
    A_sparse = sparse.diags(
        [lower_diag, main_diag, upper_diag],
        offsets=[-1, 0, 1],
        format="csc"
    )

    # Right-hand side
    b = np.random.randn(n)

    # ---- Solve with Thomas algorithm ----
    print("\n--- 1. Thomas Algorithm (LAPACK dgtsv) ---")
    x_thomas = Thomas(A_dense, b)
    residual_thomas = norm(A_dense @ x_thomas - b)
    print(f"  System size:     {n} x {n}")
    print(f"  Residual ||Ax-b||: {residual_thomas:.2e}")

    # ---- Solve with scipy sparse solver ----
    print("\n--- 2. scipy.sparse.linalg.spsolve ---")
    x_scipy = spsolve(A_sparse, b)
    residual_scipy = norm(A_dense @ x_scipy - b)
    print(f"  Residual ||Ax-b||: {residual_scipy:.2e}")

    # ---- Compare Thomas vs scipy ----
    diff_thomas_scipy = norm(x_thomas - x_scipy)
    print(f"\n  ||x_thomas - x_scipy|| = {diff_thomas_scipy:.2e}")

    # ---- Solve with SOR (matrix form) ----
    print("\n--- 3. SOR (matrix form, w=1.0 = Gauss-Seidel) ---")
    x_sor = SOR(A_dense, b, w=1.0, eps=1e-12, N_max=500)
    residual_sor = norm(A_dense @ x_sor - b)
    print(f"  Residual ||Ax-b||: {residual_sor:.2e}")
    print(f"  ||x_thomas - x_sor|| = {norm(x_thomas - x_sor):.2e}")

    # ---- SOR convergence study: effect of relaxation parameter w ----
    print("\n--- 4. SOR Convergence Study ---")
    print("  Testing different relaxation parameters w on a smaller system...")

    n_small = 50
    lower_s = -0.3 * np.ones(n_small - 1)
    upper_s = -0.3 * np.ones(n_small - 1)
    main_s = 2.0 * np.ones(n_small)
    A_small = np.diag(main_s) + np.diag(lower_s, -1) + np.diag(upper_s, 1)
    b_small = np.ones(n_small)

    x_exact = Thomas(A_small, b_small)

    w_values = [0.5, 0.8, 1.0, 1.2, 1.5, 1.8]
    print(f"  {'w':>6s}  {'Iterations':>12s}  {'Error':>12s}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*12}")

    for w_test in w_values:
        # Run SOR with a generous iteration limit, tracking convergence
        x0_test = b_small.copy()
        converged_iter = "N/A"

        if sparse.issparse(A_small):
            D_t = sparse.diags(np.diag(A_small))
            U_t = sparse.triu(A_small, k=1)
            L_t = sparse.tril(A_small, k=-1)
            DD_t = (w_test * L_t + D_t).toarray()
        else:
            D_t = np.eye(n_small) * np.diag(A_small)
            U_t = np.triu(A_small, k=1)
            L_t = np.tril(A_small, k=-1)
            DD_t = w_test * L_t + D_t

        for it in range(1, 1001):
            rhs_t = w_test * b_small - w_test * U_t @ x0_test - (w_test - 1) * D_t @ x0_test
            x_new_test = solve_triangular(DD_t, rhs_t, lower=True)
            if norm(x_new_test - x0_test) < 1e-10:
                converged_iter = str(it)
                break
            x0_test = x_new_test

        error = norm(x_new_test - x_exact)
        print(f"  {w_test:6.2f}  {converged_iter:>12s}  {error:12.2e}")

    # ---- Timing comparison ----
    import time

    print("\n--- 5. Timing Comparison (n=1000) ---")
    n_big = 1000
    lower_b = -0.5 * np.random.rand(n_big - 1)
    upper_b = -0.3 * np.random.rand(n_big - 1)
    main_b = 3.0 + np.random.rand(n_big)
    A_big = np.diag(main_b) + np.diag(lower_b, -1) + np.diag(upper_b, 1)
    A_big_sp = sparse.csc_matrix(A_big)
    b_big = np.random.randn(n_big)

    n_trials = 50

    t0 = time.perf_counter()
    for _ in range(n_trials):
        x_t = Thomas(A_big, b_big)
    t_thomas = (time.perf_counter() - t0) / n_trials * 1000

    t0 = time.perf_counter()
    for _ in range(n_trials):
        x_s = spsolve(A_big_sp, b_big)
    t_scipy = (time.perf_counter() - t0) / n_trials * 1000

    t0 = time.perf_counter()
    for _ in range(n_trials):
        x_sor2 = SOR(A_big, b_big, w=1.0, eps=1e-10, N_max=500)
    t_sor = (time.perf_counter() - t0) / n_trials * 1000

    print(f"  Thomas (LAPACK dgtsv):  {t_thomas:.3f} ms/solve")
    print(f"  scipy spsolve:          {t_scipy:.3f} ms/solve")
    print(f"  SOR (w=1.0):            {t_sor:.3f} ms/solve")
    print(f"\n  All methods agree: ||x_thomas - x_scipy|| = {norm(x_t - x_s):.2e}")
    print(f"                     ||x_thomas - x_sor||   = {norm(x_t - x_sor2):.2e}")

    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    print("  - Thomas algorithm is the fastest for tridiagonal systems (O(n)).")
    print("  - SOR is iterative but can handle more general sparse systems.")
    print("  - For FDM in Black-Scholes PDE, the Thomas algorithm is the")
    print("    standard choice for implicit and Crank-Nicolson schemes.")
    print("  - SOR / PSOR is used for American options (free-boundary problems).")
    print("=" * 72)
