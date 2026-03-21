#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_kalman_filter.py
==========================
Kalman Filter for Linear Regression Beta Estimation.

Based on Kalman_filter.py from:
    cantaro86 - Financial-Models-Numerical-Methods
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

The Kalman filter provides an online (recursive) estimate of the regression
coefficient beta in the time-varying linear model:
    Y_t = alpha + beta_t * X_t + epsilon_t      (measurement equation)
    beta_t = beta_{t-1} + eta_t                  (state transition)

where:
    epsilon_t ~ N(0, var_eps)    measurement noise
    eta_t     ~ N(0, var_eta)    process noise (drives beta evolution)

When var_eta = 0, beta is constant and we recover OLS regression.
When var_eta > 0, beta is allowed to drift, and the Kalman filter
tracks this time-varying relationship.

Applications in Quantitative Finance:
    - Pairs trading: track the hedge ratio between cointegrated assets
    - Factor models: estimate time-varying factor loadings
    - Volatility tracking: estimate time-varying volatility parameters
    - Signal processing: separate signal from noise in alpha signals

Key Features:
    1. Kalman Filter (forward pass) -- online beta estimation
    2. MLE Calibration -- estimate var_eta and var_eps from data
    3. R2 Calibration  -- tune var_eta to maximise R-squared
    4. RTS Smoother    -- backward pass for smoothed beta estimates

License: MIT (see original repository)
"""

import numpy as np
from scipy.optimize import minimize
import scipy.stats as ss


# ============================================================================
# Kalman Regression Class
# ============================================================================

class Kalman_regression:
    """
    Kalman Filter for linear regression beta estimation.

    The model is:
        Y_t = alpha0 + beta_t * X_t + eps_t,   eps_t ~ N(0, var_eps)
        beta_t = beta_{t-1} + eta_t,            eta_t ~ N(0, var_eta)

    Alpha is assumed CONSTANT (estimated once by OLS on training data).
    Beta is time-varying and tracked by the Kalman filter.

    Parameters
    ----------
    X : array-like
        Predictor variable (1-D).
    Y : array-like
        Response variable (1-D, same length as X).
    alpha0 : float or None
        Regression intercept. If None, estimated by OLS.
    beta0 : float or None
        Initial beta. If None, estimated by OLS.
    var_eta : float or None
        Process noise variance (controls beta drift speed).
    var_eps : float or None
        Measurement noise variance. If None, estimated by OLS.
    P0 : float, default 10.0
        Initial covariance (uncertainty) of beta.
        Large P0 means high initial uncertainty.

    Attributes (after calling run())
    ----------
    betas : ndarray
        Filtered beta estimates at each time step.
    Ps : ndarray
        Filtered covariance (uncertainty) at each time step.
    loglikelihood : float
        Log-likelihood of the observations given the model.
    R2_pre_fit : float
        R-squared computed from pre-fit residuals.
    R2_post_fit : float
        R-squared computed from post-fit residuals.

    Reference: cantaro86/Financial-Models-Numerical-Methods, Kalman_filter.py
    """

    def __init__(self, X, Y, alpha0=None, beta0=None, var_eta=None, var_eps=None, P0=10.0):
        self.alpha0 = alpha0
        self.beta0 = beta0
        self.var_eta = var_eta
        self.var_eps = var_eps
        self.P0 = P0
        self.X = np.asarray(X, dtype=np.float64)
        self.Y = np.asarray(Y, dtype=np.float64)
        self.loglikelihood = None
        self.R2_pre_fit = None
        self.R2_post_fit = None
        self.betas = None
        self.Ps = None

        # If key parameters are missing, initialise from OLS
        if (self.alpha0 is None) or (self.beta0 is None) or (self.var_eps is None):
            self.alpha0, self.beta0, self.var_eps = self._get_OLS_params()

    def _get_OLS_params(self):
        """
        Estimate alpha, beta, and residual variance by OLS.
            Y = alpha + beta * X + epsilon
        Returns (alpha, beta, var_eps).
        """
        slope, intercept, _, _, _ = ss.linregress(self.X, self.Y)
        residuals = self.Y - slope * self.X - intercept
        var_eps = residuals.var(ddof=2)
        return intercept, slope, var_eps

    def run(self, X=None, Y=None, var_eta=None, var_eps=None):
        """
        Run the Kalman filter (forward pass).

        Optionally accepts new X, Y data (e.g., test set after training).

        The algorithm at each step k:
            PREDICT:
                beta_predicted = beta_{k-1}         (random walk)
                P_predicted    = P_{k-1} + var_eta
            UPDATE:
                innovation r_k = Y_k - alpha0 - beta_predicted * X_k
                S_k = X_k^2 * P_predicted + var_eps    (innovation variance)
                KG_k = X_k * P_predicted / S_k         (Kalman gain)
                beta_k = beta_predicted + KG_k * r_k
                P_k = P_predicted * (1 - KG_k * X_k)

        Parameters
        ----------
        X, Y : array-like or None
            If provided, use these instead of self.X, self.Y.
        var_eta, var_eps : float or None
            If provided, override stored values.
        """
        if (X is None) and (Y is None):
            X = self.X
            Y = self.Y
        X = np.asarray(X, dtype=np.float64)
        Y = np.asarray(Y, dtype=np.float64)

        N = len(X)
        if len(Y) != N:
            raise ValueError("X and Y must have the same length")

        if var_eta is not None:
            self.var_eta = var_eta
        if var_eps is not None:
            self.var_eps = var_eps
        if self.var_eta is None:
            raise ValueError("var_eta is None -- must be set before running the filter")

        betas = np.zeros(N)
        Ps = np.zeros(N)
        res_pre = np.zeros(N)      # pre-fit residuals (innovations)

        Y_adj = Y - self.alpha0    # subtract constant intercept
        P = self.P0
        beta = self.beta0

        log_2pi = np.log(2 * np.pi)
        loglikelihood = 0.0

        for k in range(N):
            # --- Prediction step ---
            beta_p = beta                        # predicted beta (random walk)
            P_p = P + self.var_eta               # predicted covariance

            # --- Innovation ---
            r = Y_adj[k] - beta_p * X[k]        # pre-fit residual
            S = P_p * X[k]**2 + self.var_eps     # innovation variance
            KG = X[k] * P_p / S                  # Kalman gain

            # --- Update step ---
            beta = beta_p + KG * r               # updated beta
            P = P_p * (1 - KG * X[k])           # updated covariance

            # --- Log-likelihood ---
            loglikelihood += 0.5 * (-log_2pi - np.log(S) - (r**2 / S))

            betas[k] = beta
            Ps[k] = P
            res_pre[k] = r

        # Post-fit residuals and R-squared
        res_post = Y_adj - X * betas
        sqr_err = Y_adj - np.mean(Y_adj)
        R2_pre = 1 - (res_pre @ res_pre) / (sqr_err @ sqr_err)
        R2_post = 1 - (res_post @ res_post) / (sqr_err @ sqr_err)

        self.loglikelihood = loglikelihood
        self.R2_pre_fit = R2_pre
        self.R2_post_fit = R2_post
        self.betas = betas
        self.Ps = Ps

    def calibrate_MLE(self):
        """
        Calibrate var_eta and var_eps by Maximum Likelihood Estimation.

        Uses the L-BFGS-B optimiser to maximise the log-likelihood
        computed by the Kalman filter.  Both parameters are constrained
        to be positive.
        """
        def minus_likelihood(c):
            self.var_eps = c[0]
            self.var_eta = c[1]
            self.run()
            return -1.0 * self.loglikelihood

        result = minimize(
            minus_likelihood,
            x0=[self.var_eps, self.var_eps],
            method="L-BFGS-B",
            bounds=[[1e-15, None], [1e-15, None]],
            tol=1e-6,
        )

        if result.success:
            self.beta0 = self.betas[-1]
            self.P0 = self.Ps[-1]
            self.var_eps = result.x[0]
            self.var_eta = result.x[1]
            return {"var_eps": result.x[0], "var_eta": result.x[1]}
        else:
            print("WARNING: MLE calibration did not converge.")
            return None

    def calibrate_R2(self, mode="pre-fit"):
        """
        Calibrate var_eta by maximising R-squared.

        Only var_eta is calibrated (var_eps is held fixed).

        Parameters
        ----------
        mode : str, "pre-fit" or "post-fit"
            Which R-squared to maximise.
        """
        def minus_R2(c):
            self.var_eta = c[0]
            self.run()
            if mode == "pre-fit":
                return -1.0 * self.R2_pre_fit
            elif mode == "post-fit":
                return -1.0 * self.R2_post_fit

        result = minimize(
            minus_R2,
            x0=[self.var_eps],
            method="L-BFGS-B",
            bounds=[[1e-15, 1]],
            tol=1e-6,
        )

        if result.success:
            self.beta0 = self.betas[-1]
            self.P0 = self.Ps[-1]
            self.var_eta = result.x[0]
            return {"var_eta": result.x[0]}
        else:
            print("WARNING: R2 calibration did not converge.")
            return None

    def RTS_smoother(self, X=None, Y=None):
        """
        Rauch-Tung-Striebel (RTS) smoother for the beta estimation.

        The RTS smoother is a backward pass that uses future observations
        to refine past beta estimates.  It produces smoother beta trajectories
        than the forward-only Kalman filter.

        Algorithm:
            1. Run the forward Kalman filter to get betas[k], Ps[k]
            2. Backward pass:
                C_k = P_k / (P_k + var_eta)
                beta_smooth[k] = beta[k] + C_k * (beta_smooth[k+1] - beta[k])
                P_smooth[k] = P[k] + C_k^2 * (P_smooth[k+1] - (P[k] + var_eta))

        Parameters
        ----------
        X, Y : array-like or None
            If provided, run the forward filter first on this data.

        Returns
        -------
        betas_smooth : ndarray
            Smoothed beta estimates.
        Ps_smooth : ndarray
            Smoothed covariance estimates.
        """
        if X is not None and Y is not None:
            self.run(X, Y)
        elif self.betas is None:
            raise ValueError("Must run() the filter first or provide X, Y.")

        betas = self.betas
        Ps = self.Ps

        betas_smooth = np.zeros_like(betas)
        Ps_smooth = np.zeros_like(Ps)
        betas_smooth[-1] = betas[-1]
        Ps_smooth[-1] = Ps[-1]

        for k in range(len(betas) - 2, -1, -1):
            C = Ps[k] / (Ps[k] + self.var_eta)
            betas_smooth[k] = betas[k] + C * (betas_smooth[k + 1] - betas[k])
            Ps_smooth[k] = Ps[k] + C**2 * (Ps_smooth[k + 1] - (Ps[k] + self.var_eta))

        return betas_smooth, Ps_smooth


# ============================================================================
# Rolling Regression (for comparison)
# ============================================================================

def rolling_regression(X, Y, window):
    """
    Compute rolling OLS beta estimates.

    Parameters
    ----------
    X, Y : ndarray
        Full predictor and response arrays.
    window : int
        Rolling window size.

    Returns
    -------
    betas : ndarray
        Rolling beta estimates (length = len(X) - window + 1).
        Padded with NaN for the initial window.
    """
    N = len(X)
    betas = np.full(N, np.nan)
    for i in range(window - 1, N):
        x_win = X[i - window + 1: i + 1]
        y_win = Y[i - window + 1: i + 1]
        slope, _, _, _, _ = ss.linregress(x_win, y_win)
        betas[i] = slope
    return betas


# ============================================================================
# Demo / Main
# ============================================================================

if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("=" * 72)
    print("  KALMAN FILTER FOR LINEAR REGRESSION BETA ESTIMATION")
    print("=" * 72)

    # ---- 1. Generate synthetic AR(1) data with time-varying beta ----
    print("\n--- 1. Generating Synthetic Data ---")
    np.random.seed(42)

    N_total = 1000
    training_size = 250
    rolling_window = 50

    # True time-varying beta: starts at 0.8, drifts to 1.2, then back
    t = np.arange(N_total)
    true_beta = 0.8 + 0.4 * np.sin(2 * np.pi * t / N_total)
    alpha_true = 0.5

    # Generate X as an AR(1) process
    X = np.zeros(N_total)
    X[0] = np.random.randn()
    for i in range(1, N_total):
        X[i] = 0.95 * X[i - 1] + np.random.randn() * 0.5

    # Generate Y with time-varying beta and noise
    noise_eps = np.random.randn(N_total) * 0.3
    Y = alpha_true + true_beta * X + noise_eps

    print(f"  Total observations:  {N_total}")
    print(f"  Training set size:   {training_size}")
    print(f"  Test set size:       {N_total - training_size}")
    print(f"  True alpha:          {alpha_true}")
    print(f"  True beta range:     [{true_beta.min():.3f}, {true_beta.max():.3f}]")

    # ---- 2. Train the Kalman filter on training data ----
    print("\n--- 2. Training Phase (OLS initialisation + MLE calibration) ---")
    X_train = X[:training_size]
    Y_train = Y[:training_size]
    X_test = X[training_size:]
    Y_test = Y[training_size:]

    # Create Kalman filter (alpha0, beta0, var_eps initialised by OLS)
    KR = Kalman_regression(X_train, Y_train)
    print(f"  OLS alpha0:  {KR.alpha0:.4f}")
    print(f"  OLS beta0:   {KR.beta0:.4f}")
    print(f"  OLS var_eps: {KR.var_eps:.6f}")

    # Calibrate var_eta and var_eps by MLE
    mle_result = KR.calibrate_MLE()
    if mle_result is not None:
        print(f"  MLE var_eps: {mle_result['var_eps']:.6f}")
        print(f"  MLE var_eta: {mle_result['var_eta']:.6f}")

    # Run on training data with MLE parameters
    KR.run(X_train, Y_train)
    print(f"  Training R2 (pre-fit):  {KR.R2_pre_fit:.4f}")
    print(f"  Training R2 (post-fit): {KR.R2_post_fit:.4f}")

    # ---- 3. Test phase ----
    print("\n--- 3. Test Phase (Kalman Filter vs Rolling Regression) ---")
    # Update initial conditions from training
    KR.beta0 = KR.betas[-1]
    KR.P0 = KR.Ps[-1]

    # Run on test data
    KR.run(X_test, Y_test)
    betas_kalman = KR.betas
    Ps_kalman = KR.Ps

    print(f"  Test R2 (pre-fit):  {KR.R2_pre_fit:.4f}")
    print(f"  Test R2 (post-fit): {KR.R2_post_fit:.4f}")
    print(f"  Test log-likelihood: {KR.loglikelihood:.2f}")

    # Rolling regression on test data
    betas_rolling = rolling_regression(X_test, Y_test, rolling_window)

    # RTS Smoother
    betas_smooth, Ps_smooth = KR.RTS_smoother(X_test, Y_test)

    # ---- 4. Compute MSE ----
    true_beta_test = true_beta[training_size:]

    mse_kalman = np.mean((betas_kalman - true_beta_test)**2)
    valid_idx = ~np.isnan(betas_rolling)
    mse_rolling = np.mean((betas_rolling[valid_idx] - true_beta_test[valid_idx])**2)
    mse_smooth = np.mean((betas_smooth - true_beta_test)**2)

    print(f"\n  MSE Comparison:")
    print(f"    Kalman Filter:       {mse_kalman:.6f}")
    print(f"    Rolling Regression:  {mse_rolling:.6f}  (window={rolling_window})")
    print(f"    RTS Smoother:        {mse_smooth:.6f}")

    # ---- 5. R2 Calibration ----
    print("\n--- 4. Alternative: R2 Calibration ---")
    KR2 = Kalman_regression(X_train, Y_train)
    r2_result = KR2.calibrate_R2(mode="pre-fit")
    if r2_result is not None:
        print(f"  R2-calibrated var_eta: {r2_result['var_eta']:.6f}")
        KR2.run(X_train, Y_train)
        print(f"  Training R2 (pre-fit):  {KR2.R2_pre_fit:.4f}")
        print(f"  Training R2 (post-fit): {KR2.R2_post_fit:.4f}")

    # ---- 6. Plot results ----
    print("\n--- 5. Generating Plots ---")
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))

    # Top panel: beta estimates on test set
    ax1 = axes[0]
    test_idx = np.arange(len(X_test))
    ax1.plot(test_idx, true_beta_test, "k-", linewidth=2, label="True beta", alpha=0.8)
    ax1.plot(test_idx, betas_kalman, "b-", linewidth=1.2, label="Kalman filter")
    ax1.plot(test_idx, betas_rolling, color="orange", linewidth=1.2,
             label=f"Rolling OLS (w={rolling_window})")
    ax1.plot(test_idx, betas_smooth, "r--", linewidth=1.5, label="RTS smoother")
    ax1.fill_between(
        test_idx,
        betas_kalman + np.sqrt(Ps_kalman),
        betas_kalman - np.sqrt(Ps_kalman),
        alpha=0.3, color="steelblue", label=r"Kalman $\pm 1\sigma$"
    )
    ax1.set_xlabel("Time Step (test set)")
    ax1.set_ylabel("Beta")
    ax1.set_title("Kalman Filter vs Rolling Regression vs RTS Smoother")
    ax1.legend(loc="upper right")
    ax1.grid(True, alpha=0.3)

    # Bottom panel: Kalman gain and covariance evolution
    ax2 = axes[1]
    ax2.plot(test_idx, Ps_kalman, "b-", label="Kalman P (covariance)")
    ax2.plot(test_idx, Ps_smooth, "r--", label="Smoothed P")
    ax2.set_xlabel("Time Step (test set)")
    ax2.set_ylabel("Covariance P")
    ax2.set_title("Covariance (Uncertainty) Evolution")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("kalman_filter_demo.png", dpi=150, bbox_inches="tight")
    print("  Saved: kalman_filter_demo.png")

    # ---- Summary ----
    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    print("  The Kalman filter provides online (recursive) beta estimation that")
    print("  adapts to changing market conditions:")
    print(f"    - Kalman MSE:  {mse_kalman:.6f}  (best for real-time tracking)")
    print(f"    - Rolling MSE: {mse_rolling:.6f}  (lagging, window-dependent)")
    print(f"    - RTS MSE:     {mse_smooth:.6f}  (best overall, but uses future data)")
    print()
    print("  MLE calibration automatically finds the optimal noise parameters.")
    print("  The RTS smoother gives the best estimates but requires all data")
    print("  (not suitable for real-time applications).")
    print("=" * 72)
