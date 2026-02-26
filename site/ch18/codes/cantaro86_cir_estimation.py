"""
cantaro86_cir_estimation.py

CIR process simulation (4 truncation schemes), Bessel-function density,
OLS parameter estimation, and log-transform simulation.

Based on the CIR material (cells 37-60) in cantaro86's notebook
"1.2 SDE simulations and statistics" from the repository
Financial-Models-Numerical-Methods
(https://github.com/cantaro86/Financial-Models-Numerical-Methods).

Adapted as a self-contained educational module -- no local imports required.

Contents
--------
1. Euler-Maruyama CIR simulation with four truncation methods:
       reflection, positive-part, full truncation, partial truncation.
2. CIR density via modified Bessel functions (CIR_pdf) and
       equivalence check with scipy.stats.ncx2.
3. OLS regression estimator for (kappa, theta, sigma):
       closed-form formulas + scipy.optimize.minimize verification.
4. Log-transform simulation: Ito-lemma change of variable Y = log(X),
       Euler-Maruyama on Y, then recover X = exp(Y).
5. Histogram vs density comparison with original and estimated parameters.
"""

import numpy as np
import scipy.stats as ss
from scipy.special import iv          # modified Bessel function, 1st kind
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# ============================================================================
# 1. CIR process simulation -- Euler-Maruyama with 4 truncation methods
# ============================================================================

def simulate_cir_euler(
    kappa, theta, sigma, X0, T, N, paths,
    method="reflection", seed=42
):
    """
    Simulate the CIR process via Euler-Maruyama with a chosen truncation
    scheme to handle the square-root of potentially negative values.

    The CIR SDE is:
        dX_t = kappa * (theta - X_t) dt + sigma * sqrt(X_t) dW_t

    Parameters
    ----------
    kappa : float
        Mean reversion speed.
    theta : float
        Long-run mean level.
    sigma : float
        Volatility coefficient.
    X0 : float
        Initial value of the process.
    T : float
        Terminal time.
    N : int
        Number of time steps (N-1 increments after the initial value).
    paths : int
        Number of independent Monte-Carlo paths.
    method : str
        Truncation method.  One of:
            'reflection'        -- method 4: take abs of the whole update
            'positive_part'     -- method 1: use max(X, 0) under sqrt only
            'full_truncation'   -- method 2: use max(X, 0) in both drift
                                   and diffusion
            'partial_truncation'-- method 3: use abs(X) under sqrt only
    seed : int or None
        Random seed for reproducibility.

    Returns
    -------
    T_vec : ndarray, shape (N,)
        Time grid.
    X : ndarray, shape (N, paths)
        Simulated paths (rows = time steps, columns = paths).
    """
    if seed is not None:
        np.random.seed(seed)

    T_vec, dt = np.linspace(0, T, N, retstep=True)
    W = ss.norm.rvs(loc=0, scale=np.sqrt(dt), size=(N - 1, paths))

    X = np.zeros((N, paths))
    X[0, :] = X0

    for t in range(N - 1):
        Xt = X[t, :]

        if method == "reflection":
            # Method 4:  X_{i+1} = | X_i + drift + diffusion |
            X[t + 1, :] = np.abs(
                Xt + kappa * (theta - Xt) * dt + sigma * np.sqrt(Xt) * W[t, :]
            )

        elif method == "positive_part":
            # Method 1:  sqrt uses X^+ only; result may still be negative
            Xt_pos = np.maximum(Xt, 0.0)
            X[t + 1, :] = (
                Xt + kappa * (theta - Xt) * dt
                + sigma * np.sqrt(Xt_pos) * W[t, :]
            )

        elif method == "full_truncation":
            # Method 2:  both drift and diffusion use X^+
            Xt_pos = np.maximum(Xt, 0.0)
            X[t + 1, :] = (
                Xt + kappa * (theta - Xt_pos) * dt
                + sigma * np.sqrt(Xt_pos) * W[t, :]
            )

        elif method == "partial_truncation":
            # Method 3:  sqrt uses |X|; drift uses original X
            X[t + 1, :] = (
                Xt + kappa * (theta - Xt) * dt
                + sigma * np.sqrt(np.abs(Xt)) * W[t, :]
            )

        else:
            raise ValueError(
                f"Unknown method '{method}'. Choose from: reflection, "
                "positive_part, full_truncation, partial_truncation."
            )

    return T_vec, X


# ============================================================================
# 2. CIR density via modified Bessel functions
# ============================================================================

def CIR_pdf(x, x0, T, k, t, s):
    """
    Probability density of the CIR process X_T | X_0 = x0.

    Uses the modified Bessel function of the first kind I_q from
    scipy.special.iv.

    The density is:

        f(x | x0) = c * exp(-u - v) * (v/u)^{q/2} * I_q(2*sqrt(u*v))

    with:
        c = 2*kappa / ((1 - exp(-kappa*T)) * sigma^2)
        q = 2*kappa*theta / sigma^2 - 1
        u = c * x0 * exp(-kappa*T)
        v = c * x

    Parameters
    ----------
    x : array_like
        Points at which to evaluate the density.
    x0 : float
        Initial value.
    T : float
        Time horizon.
    k, t, s : float
        kappa, theta, sigma of the CIR process.

    Returns
    -------
    ndarray
        Density values at each x.

    Reference
    ---------
    Cox, J.C., Ingersoll, J.E., and Ross, S.A.
    "A Theory of the Term Structure of Interest Rates."
    Econometrica, Vol. 53, No. 2 (March, 1985).
    """
    c = 2 * k / ((1 - np.exp(-k * T)) * s ** 2)
    q = 2 * k * t / s ** 2 - 1
    u = c * x0 * np.exp(-k * T)
    v = c * x
    return c * np.exp(-u - v) * (v / u) ** (q / 2) * iv(q, 2 * np.sqrt(u * v))


def CIR_ncx2_pdf(x, x0, T, kappa, theta, sigma):
    """
    Same density as CIR_pdf but computed through scipy.stats.ncx2.

    The CIR transition density is a scaled non-central chi-squared:
        X_T ~ Y / (2c)    with Y ~ ncx2(df=K, nc=lambda, scale=1)

    Parameterisation (scipy convention):
        c      = 2*kappa / ((1 - exp(-kappa*T)) * sigma^2)
        K      = 4*kappa*theta / sigma^2          (degrees of freedom)
        lambda = 2*c*x0*exp(-kappa*T)             (non-centrality)
        scale  = 1 / (2*c)

    Parameters
    ----------
    x : array_like
        Points at which to evaluate the density.
    x0 : float
        Initial value.
    T : float
        Time horizon.
    kappa, theta, sigma : float
        CIR parameters.

    Returns
    -------
    ndarray
        Density values at each x.
    """
    c = 2 * kappa / ((1 - np.exp(-kappa * T)) * sigma ** 2)
    df = 4 * kappa * theta / sigma ** 2          # degrees of freedom  K
    nc = 2 * c * x0 * np.exp(-kappa * T)         # non-centrality  lambda
    return ss.ncx2.pdf(x, df, nc, scale=1 / (2 * c))


# ============================================================================
# 3. OLS parameter estimation for CIR
# ============================================================================

def estimate_cir_ols(X_path, dt):
    """
    Estimate CIR parameters (kappa, theta, sigma) from a single observed
    path using the OLS (Ordinary Least Squares) regression method.

    Derivation
    ----------
    Divide the discrete CIR equation by sqrt(X_i):

        (X_{i+1} - X_i) / sqrt(X_i) =  kappa*theta*dt / sqrt(X_i)
                                       - kappa*sqrt(X_i)*dt
                                       + sigma * DeltaW_i

    Define:
        Y   = (X_{i+1} - X_i) / sqrt(X_i)       -- response
        X1  = dt / sqrt(X_i)                      -- regressor 1
        X2  = dt * sqrt(X_i)                      -- regressor 2

    Then:
        Y = a * (1/sqrt(X_i)) + b * sqrt(X_i) + noise
    with  a = kappa*theta*dt,  b = -kappa*dt.

    Minimising the sum of squared residuals yields closed-form OLS
    formulas for kappa and theta (implemented below).

    sigma is estimated from the standard deviation of the residuals:
        sigma_hat = std(residuals, ddof=2) / sqrt(dt)

    The choice ddof=2 is conventional in linear regression because
    two parameters (a and b) have already been estimated.

    Parameters
    ----------
    X_path : ndarray, shape (N,)
        A single realised CIR path.
    dt : float
        Time step between consecutive observations.

    Returns
    -------
    kappa_hat : float
        Estimated mean-reversion speed.
    theta_hat : float
        Estimated long-run mean.
    sigma_hat : float
        Estimated volatility.
    """
    N = len(X_path)

    # Closed-form OLS formulas for kappa and theta
    # (derived by solving the 2x2 normal equations of the linear regression)
    X_curr = X_path[:-1]      # X_0, ..., X_{N-2}
    X_next = X_path[1:]       # X_1, ..., X_{N-1}

    n = N - 1                 # number of increments

    sum_Xnext           = np.sum(X_next)
    sum_Xcurr           = np.sum(X_curr)
    sum_inv_Xcurr       = np.sum(1.0 / X_curr)
    sum_ratio           = np.sum(X_next / X_curr)

    num_kappa = (
        n ** 2
        + sum_Xnext * sum_inv_Xcurr
        - sum_Xcurr * sum_inv_Xcurr
        - n * sum_ratio
    )
    den_kappa = (n ** 2 - sum_Xcurr * sum_inv_Xcurr) * dt

    kappa_hat = num_kappa / den_kappa

    theta_hat = (
        (n * sum_Xnext - sum_ratio * sum_Xcurr) / num_kappa
    )

    # Residuals and sigma estimation
    YY  = (X_next - X_curr) / np.sqrt(X_curr)       # response
    XX1 = 1.0 / np.sqrt(X_curr)                      # regressor 1
    XX2 = np.sqrt(X_curr)                             # regressor 2

    residuals = YY - theta_hat * kappa_hat * dt * XX1 + dt * kappa_hat * XX2
    sigma_hat = np.std(residuals, ddof=2) / np.sqrt(dt)

    return kappa_hat, theta_hat, sigma_hat


def estimate_cir_ols_minimize(X_path, dt):
    """
    Verify the OLS estimates by numerically minimising the sum of
    squared residuals with scipy.optimize.minimize (Nelder-Mead).

    This should reproduce the closed-form OLS result from
    estimate_cir_ols() up to optimiser tolerance.

    Parameters
    ----------
    X_path : ndarray, shape (N,)
        A single realised CIR path.
    dt : float
        Time step between consecutive observations.

    Returns
    -------
    kappa_opt : float
        Numerically estimated kappa.
    theta_opt : float
        Numerically estimated theta.
    result : scipy.optimize.OptimizeResult
        Full optimiser result object.
    """
    X_curr = X_path[:-1]
    X_next = X_path[1:]

    YY  = (X_next - X_curr) / np.sqrt(X_curr)
    XX1 = 1.0 / np.sqrt(X_curr)
    XX2 = np.sqrt(X_curr)

    def sum_of_squares(c):
        """Objective: sum of squared residuals."""
        kappa_trial, theta_trial = c
        predicted = theta_trial * kappa_trial * dt * XX1 - kappa_trial * dt * XX2
        return np.sum((YY - predicted) ** 2)

    result = minimize(
        sum_of_squares,
        x0=[1.0, 1.0],
        method="Nelder-Mead",
        tol=1e-8,
    )
    kappa_opt, theta_opt = result.x
    return kappa_opt, theta_opt, result


# ============================================================================
# 4. Log-transform simulation
# ============================================================================

def simulate_cir_log_transform(kappa, theta, sigma, X0, T, N, paths, seed=42):
    """
    Simulate the CIR process via a log-variable change of variable.

    Let Y_t = log(X_t).  Applying Ito's lemma to f(x) = log(x):

        dY_t = exp(-Y_t) * [ kappa*(theta - exp(Y_t)) - sigma^2/2 ] dt
             + sigma * exp(-Y_t/2) dW_t

    Euler-Maruyama on Y:
        Y_{i+1} = Y_i
                  + exp(-Y_i) * [ kappa*(theta - exp(Y_i)) - 0.5*sigma^2 ] * dt
                  + sigma * exp(-Y_i/2) * DeltaW_i

    The original process is recovered as X_t = exp(Y_t).

    Advantages
    ----------
    - Y can be negative, so no square-root-of-negative issue arises.
    - Under the same random seed the path matches the direct simulation
      (reflection method) when dt is small.

    Caveats
    -------
    - For coarse grids (small N) or large sigma, exp(Y) can overflow.
    - Not universally more accurate than direct truncation methods.

    Parameters
    ----------
    kappa, theta, sigma, X0 : float
        CIR parameters and initial value.
    T : float
        Terminal time.
    N : int
        Number of time-grid points.
    paths : int
        Number of Monte-Carlo paths.
    seed : int or None
        Random seed.

    Returns
    -------
    T_vec : ndarray, shape (N,)
        Time grid.
    X : ndarray, shape (N, paths)
        Simulated CIR paths (exp of the log-variable).
    Y : ndarray, shape (N, paths)
        Simulated log-paths (before exponentiation).
    """
    if seed is not None:
        np.random.seed(seed)

    T_vec, dt = np.linspace(0, T, N, retstep=True)
    W = ss.norm.rvs(loc=0, scale=np.sqrt(dt), size=(N - 1, paths))

    Y0 = np.log(X0)
    Y = np.zeros((N, paths))
    Y[0, :] = Y0

    for t in range(N - 1):
        Yt = Y[t, :]
        exp_neg_Y = np.exp(-Yt)
        Y[t + 1, :] = (
            Yt
            + exp_neg_Y * (kappa * (theta - np.exp(Yt)) - 0.5 * sigma ** 2) * dt
            + sigma * np.exp(-Yt / 2) * W[t, :]
        )

    X = np.exp(Y)
    return T_vec, X, Y


# ============================================================================
# Main demonstration
# ============================================================================

if __name__ == "__main__":
    # ------------------------------------------------------------------
    # True CIR parameters (cantaro86 defaults for the interest-rate case)
    # ------------------------------------------------------------------
    kappa = 3.0
    theta = 0.04
    sigma = 0.25
    X0    = 0.05
    T     = 3.0
    N     = 200_001      # fine grid for accurate simulation
    n_paths = 2000

    feller_satisfied = 2 * kappa * theta > sigma ** 2
    std_asy = np.sqrt(theta * sigma ** 2 / (2 * kappa))

    print("=" * 70)
    print("CIR ESTIMATION AND LOG-TRANSFORM SIMULATION")
    print("  Based on cantaro86, 'SDE simulations and statistics'")
    print("=" * 70)
    print()

    print("True parameters")
    print(f"  kappa = {kappa}")
    print(f"  theta = {theta}")
    print(f"  sigma = {sigma}")
    print(f"  X0    = {X0}")
    print(f"  T     = {T}")
    print(f"  Feller condition (2*kappa*theta > sigma^2): {feller_satisfied}")
    print(f"  Asymptotic std dev = {std_asy:.6f}")
    print()

    # ==================================================================
    # Part 1 -- Direct simulation (reflection method)
    # ==================================================================
    print("-" * 70)
    print("PART 1: Direct Euler-Maruyama simulation (reflection method)")
    print("-" * 70)

    T_vec, X = simulate_cir_euler(
        kappa, theta, sigma, X0, T, N, n_paths,
        method="reflection", seed=42,
    )
    dt = T_vec[1] - T_vec[0]

    X_T = X[-1, :]       # terminal values across all paths
    X_1 = X[:, 0]        # single representative path

    print(f"  Simulated {n_paths} paths with {N} time steps (dt = {dt:.2e})")
    print(f"  E[X_T]  = {X_T.mean():.6f}   (asymptotic: {theta})")
    print(f"  Std[X_T]= {X_T.std():.6f}   (asymptotic: {std_asy:.6f})")
    print()

    # ==================================================================
    # Part 2 -- CIR density via Bessel vs ncx2
    # ==================================================================
    print("-" * 70)
    print("PART 2: CIR density -- Bessel function vs scipy.stats.ncx2")
    print("-" * 70)

    x_grid = np.linspace(0.001, 0.12, 200)
    pdf_bessel = CIR_pdf(x_grid, X0, T, kappa, theta, sigma)
    pdf_ncx2   = CIR_ncx2_pdf(x_grid, X0, T, kappa, theta, sigma)

    max_diff = np.max(np.abs(pdf_bessel - pdf_ncx2))
    print(f"  Max |CIR_pdf - ncx2_pdf| = {max_diff:.2e}  (should be ~0)")
    print()

    # ==================================================================
    # Part 3 -- OLS parameter estimation
    # ==================================================================
    print("-" * 70)
    print("PART 3: OLS parameter estimation from a single path")
    print("-" * 70)

    kappa_ols, theta_ols, sigma_ols = estimate_cir_ols(X_1, dt)

    print("  Closed-form OLS estimates:")
    print(f"    kappa_hat = {kappa_ols:.6f}   (true: {kappa})")
    print(f"    theta_hat = {theta_ols:.6f}   (true: {theta})")
    print(f"    sigma_hat = {sigma_ols:.6f}   (true: {sigma})")
    print()

    # Verify with scipy.optimize.minimize
    kappa_opt, theta_opt, opt_result = estimate_cir_ols_minimize(X_1, dt)
    print("  Numerical verification (Nelder-Mead minimiser):")
    print(f"    kappa_opt = {kappa_opt:.6f}")
    print(f"    theta_opt = {theta_opt:.6f}")
    print(f"    Optimiser success: {opt_result.success}")
    print()

    print("  Parameter comparison:")
    print(f"    {'Param':<8} {'True':>10} {'OLS':>10} {'Minimise':>10}")
    print(f"    {'-'*8} {'-'*10} {'-'*10} {'-'*10}")
    print(f"    {'kappa':<8} {kappa:>10.4f} {kappa_ols:>10.4f} {kappa_opt:>10.4f}")
    print(f"    {'theta':<8} {theta:>10.4f} {theta_ols:>10.4f} {theta_opt:>10.4f}")
    print(f"    {'sigma':<8} {sigma:>10.4f} {sigma_ols:>10.4f} {'--':>10}")
    print()

    print("  NOTE: kappa is the most volatile parameter to estimate.")
    print("  Changing the random seed will show that theta and sigma are")
    print("  quite stable, whereas kappa can vary considerably.")
    print()

    # ==================================================================
    # Part 4 -- Log-transform simulation
    # ==================================================================
    print("-" * 70)
    print("PART 4: Log-transform simulation (Y = log X, Euler on Y)")
    print("-" * 70)

    T_vec_log, X_log, Y_log = simulate_cir_log_transform(
        kappa, theta, sigma, X0, T, N, n_paths, seed=42,
    )

    # Compare first path of direct vs log-transform simulation
    X_1_log = X_log[:, 0]
    max_path_diff = np.max(np.abs(X_1 - X_1_log))
    print(f"  Max |X_direct - exp(Y)| on path 0 = {max_path_diff:.6e}")
    print("  (Same seed -> paths should match closely for fine grids)")
    print()

    print("  Caveat: for coarse grids or large sigma, exp(Y) can")
    print("  overflow to Inf / NaN.  The log-transform is the best")
    print("  theoretical approach, but the exponential creates practical")
    print("  difficulties.  (See cantaro86, cell 60.)")
    print()

    # ==================================================================
    # Part 5 -- Histogram vs density with original & estimated params
    # ==================================================================
    print("-" * 70)
    print("PART 5: Histogram vs CIR density (original & estimated params)")
    print("-" * 70)
    print("  Generating comparison plot ...")

    x_hist = np.linspace(max(X_T.min(), 1e-4), X_T.max(), 200)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.hist(
        X_T, bins=70, density=True,
        facecolor="LightBlue", edgecolor="gray", alpha=0.7,
        label="Simulated $X_T$ histogram",
    )
    ax.plot(
        x_hist, CIR_pdf(x_hist, X0, T, kappa, theta, sigma),
        "r-", linewidth=2.5, label="CIR density (true params)",
    )
    ax.plot(
        x_hist, CIR_pdf(x_hist, X0, T, kappa_ols, theta_ols, sigma_ols),
        "g--", linewidth=2.5, label="CIR density (OLS params)",
    )
    ax.set_xlabel("$X_T$", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.set_title(
        "CIR Terminal Distribution: Histogram vs Analytical Density",
        fontsize=13, fontweight="bold",
    )
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    # Parameter annotation
    param_text = (
        f"True:  $\\kappa$={kappa}, $\\theta$={theta}, $\\sigma$={sigma}\n"
        f"OLS:   $\\hat{{\\kappa}}$={kappa_ols:.3f}, "
        f"$\\hat{{\\theta}}$={theta_ols:.4f}, "
        f"$\\hat{{\\sigma}}$={sigma_ols:.4f}"
    )
    ax.text(
        0.98, 0.95, param_text,
        transform=ax.transAxes, fontsize=10,
        verticalalignment="top", horizontalalignment="right",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="wheat", alpha=0.8),
    )

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_cir_estimation.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_cir_estimation.png")
    plt.close()

    # ------------------------------------------------------------------
    # Single path comparison: direct vs log-transform
    # ------------------------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    ax2.plot(T_vec, X_1, linewidth=1.0, alpha=0.9, label="Direct (reflection)")
    ax2.plot(
        T_vec_log, X_1_log,
        linewidth=1.0, alpha=0.9, linestyle="--",
        label="Log-transform exp(Y)",
    )
    ax2.axhline(theta, color="k", linestyle=":", linewidth=1, label=f"Long-run mean $\\theta$={theta}")
    ax2.axhline(
        theta + std_asy, color="gray", linestyle=":", linewidth=0.8,
        label=f"$\\theta \\pm$ asymptotic std",
    )
    ax2.axhline(theta - std_asy, color="gray", linestyle=":", linewidth=0.8)
    ax2.set_xlabel("Time", fontsize=11)
    ax2.set_ylabel("$X_t$", fontsize=12)
    ax2.set_title(
        "CIR Path: Direct Euler vs Log-Transform (same seed)",
        fontsize=13, fontweight="bold",
    )
    ax2.legend(fontsize=10, loc="upper right")
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_cir_log_transform.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_cir_log_transform.png")
    plt.close()

    # ------------------------------------------------------------------
    # Truncation method comparison
    # ------------------------------------------------------------------
    methods = ["reflection", "positive_part", "full_truncation", "partial_truncation"]
    fig3, axes = plt.subplots(2, 2, figsize=(14, 10))

    for ax_i, method in zip(axes.ravel(), methods):
        _, X_m = simulate_cir_euler(
            kappa, theta, sigma, X0, T, N, 1,
            method=method, seed=42,
        )
        ax_i.plot(T_vec, X_m[:, 0], linewidth=0.8)
        ax_i.axhline(theta, color="r", linestyle="--", linewidth=1, alpha=0.6)
        ax_i.set_title(f"Method: {method}", fontsize=11, fontweight="bold")
        ax_i.set_xlabel("Time")
        ax_i.set_ylabel("$X_t$")
        ax_i.grid(True, alpha=0.3)

    plt.suptitle(
        "CIR Euler-Maruyama: 4 Truncation Methods (single path, same seed)",
        fontsize=14, fontweight="bold",
    )
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig("/tmp/cantaro86_cir_truncation_methods.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_cir_truncation_methods.png")
    plt.close()

    print()
    print("=" * 70)
    print("Done.")
    print("=" * 70)
