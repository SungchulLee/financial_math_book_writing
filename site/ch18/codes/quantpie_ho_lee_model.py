"""
Ho-Lee Interest Rate Model

This module implements the Ho-Lee interest rate model, a simple but pedagogically
important Gaussian short-rate model that captures the basics of term structure modeling.

The Ho-Lee model is a special case of Hull-White with lambda=0. The SDE is:
    dr(t) = theta(t) dt + sigma dW(t)

where theta(t) is calibrated to match the initial yield curve:
    theta(t) = df/dT(0,t) + sigma^2 * t

Key features:
- No mean reversion (random walk behavior)
- Time-dependent drift calibrated to initial curve
- Analytical zero-coupon bond prices
- Closed-form option prices
- Simple enough for intuition, realistic enough for applications

The model captures parallel shifts in the yield curve and is useful for:
- Cap/floor pricing
- Swaption pricing
- Bond option valuation

Based on: QuantPie Lecture Notes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import brentq


def f(P, T):
    """
    Extract forward rate from zero-coupon bond prices.

    Parameters
    ----------
    P : callable
        ZCB price function P(0, T)
    T : float
        Maturity time

    Returns
    -------
    float
        Forward rate f(0, T)

    Notes
    -----
    f(0, T) = -d/dT log(P(0, T))
    Computed via finite difference
    """
    dT = 1e-6
    log_P_minus = np.log(P(T - dT))
    log_P_plus = np.log(P(T + dT))
    return -(log_P_plus - log_P_minus) / (2 * dT)


def df_over_dT(P, T):
    """
    Compute derivative of forward rate with respect to maturity.

    Parameters
    ----------
    P : callable
        ZCB price function
    T : float
        Maturity time

    Returns
    -------
    float
        df/dT(0, T)
    """
    dT = 1e-6
    f_minus = f(P, T - dT)
    f_plus = f(P, T + dT)
    return (f_plus - f_minus) / (2 * dT)


def compute_r0(P):
    """
    Extract initial short rate from yield curve.

    Parameters
    ----------
    P : callable
        ZCB price function P(0, T)

    Returns
    -------
    float
        r(0) = f(0, 0)
    """
    return f(P, 0.0)


def compute_theta(P, T, sigma):
    """
    Compute time-dependent theta for Ho-Lee calibration.

    Parameters
    ----------
    P : callable
        ZCB price function
    T : float
        Time
    sigma : float
        Volatility

    Returns
    -------
    float
        theta(T)

    Notes
    -----
    For Ho-Lee: theta(T) = df/dT(0, T) + sigma^2 * T

    This choice ensures the model fits the initial yield curve exactly
    and maintains consistency with the given volatility.
    """
    df_dT = df_over_dT(P, T)
    return df_dT + sigma**2 * T


def generate_sample_path(r0, theta_func, sigma, T, num_steps, num_paths, seed=None):
    """
    Generate Ho-Lee short rate paths via Euler discretization.

    Parameters
    ----------
    r0 : float
        Initial short rate
    theta_func : callable
        Theta function theta(t)
    sigma : float
        Volatility (constant)
    T : float
        Final time
    num_steps : int
        Number of time steps
    num_paths : int
        Number of Monte Carlo paths
    seed : int, optional
        Random seed

    Returns
    -------
    t : ndarray
        Time grid (num_steps + 1,)
    R : ndarray
        Short rate paths (num_paths, num_steps + 1)
    M : ndarray
        Money market account (num_paths, num_steps + 1)
    """
    if seed is not None:
        np.random.seed(seed)

    # Time grid
    t = np.linspace(0, T, num_steps + 1)
    dt = t[1] - t[0]
    sqrt_dt = np.sqrt(dt)

    # Initialize
    R = np.zeros((num_paths, num_steps + 1))
    M = np.ones((num_paths, num_steps + 1))
    R[:, 0] = r0

    # Brownian increments
    Z = np.random.normal(0, 1, (num_paths, num_steps))

    # Euler discretization: dr = theta(t) dt + sigma dW
    for i in range(num_steps):
        theta_t = theta_func(t[i])
        dW = sqrt_dt * Z[:, i]

        # dr = theta(t) dt + sigma dW
        dR = theta_t * dt + sigma * dW
        R[:, i+1] = R[:, i] + dR

        # dM/M = r(t) dt (money market account)
        M[:, i+1] = M[:, i] * np.exp(R[:, i] * dt)

    return t, R, M


def compute_A(P_0, sigma, T, U):
    """
    Compute A coefficient for ZCB pricing formula.

    Parameters
    ----------
    P_0 : callable
        Initial ZCB price P(0, S)
    sigma : float
        Volatility
    T : float
        Current time
    U : float
        Bond maturity

    Returns
    -------
    float
        A(T, U)

    Notes
    -----
    Bond price: P(t, U) = A(t, U) * exp(-B(t, U) * r(t))
    For Ho-Lee: B(T, U) = U - T (no mean reversion)
    A(T, U) is adjusted for volatility
    """
    B_TU = U - T

    # Variance adjustment
    var_adjustment = sigma**2 / 2 * (U - T)**2 * T

    return P_0(U) / P_0(T) * np.exp(var_adjustment)


def compute_B(T, U):
    """
    Compute B coefficient for ZCB pricing formula.

    Parameters
    ----------
    T : float
        Current time
    U : float
        Bond maturity

    Returns
    -------
    float
        B(T, U) = U - T

    Notes
    -----
    For Ho-Lee (no mean reversion), this is simply the time difference.
    """
    return U - T


def compute_ZCB(A_T_U, B_T_U, r_T):
    """
    Compute zero-coupon bond price.

    Parameters
    ----------
    A_T_U : float
        A coefficient
    B_T_U : float
        B coefficient
    r_T : float
        Short rate at time T

    Returns
    -------
    float
        P(T, U)
    """
    return A_T_U * np.exp(-B_T_U * r_T)


def zcb_call_price(K, T, U, P_0, r0, sigma):
    """
    Compute call option on zero-coupon bond under Ho-Lee.

    Parameters
    ----------
    K : float
        Strike price
    T : float
        Option expiration
    U : float
        Bond maturity (U > T)
    P_0 : callable
        Initial ZCB prices
    r0 : float
        Initial short rate
    sigma : float
        Volatility

    Returns
    -------
    float
        Call option price
    """
    # Bond price volatility
    B_TU = U - T
    sigma_P = sigma * B_TU * np.sqrt(T)

    # Expected bond price at T
    P_T = compute_A(P_0, sigma, 0, T) * np.exp(-B_TU * r0) / P_0(T)
    F = P_T / P_0(T)  # Forward bond price

    # Black76 formula
    d1 = (np.log(F / K) + 0.5 * sigma_P**2) / sigma_P
    d2 = d1 - sigma_P

    call = P_0(U) * norm.cdf(d1) - K * P_0(T) * norm.cdf(d2)
    return call


def zcb_put_price(K, T, U, P_0, r0, sigma):
    """
    Compute put option on zero-coupon bond under Ho-Lee.

    Parameters
    ----------
    K : float
        Strike price
    T : float
        Option expiration
    U : float
        Bond maturity (U > T)
    P_0 : callable
        Initial ZCB prices
    r0 : float
        Initial short rate
    sigma : float
        Volatility

    Returns
    -------
    float
        Put option price
    """
    # Bond price volatility
    B_TU = U - T
    sigma_P = sigma * B_TU * np.sqrt(T)

    # Expected bond price at T
    A_TU = compute_A(P_0, sigma, 0, T)
    P_T = A_TU * np.exp(-B_TU * r0) / P_0(T)
    F = P_T / P_0(T)  # Forward bond price

    # Black76 formula
    d1 = (np.log(F / K) + 0.5 * sigma_P**2) / sigma_P
    d2 = d1 - sigma_P

    put = K * P_0(T) * norm.cdf(-d2) - P_0(U) * norm.cdf(-d1)
    return put


def caplet_price(K, t_fixing, t_settlement, notional, day_count, P_0, sigma):
    """
    Compute caplet price under Ho-Lee.

    Parameters
    ----------
    K : float
        Strike rate (cap rate)
    t_fixing : float
        Fixing time
    t_settlement : float
        Settlement time
    notional : float
        Notional principal
    day_count : float
        Day count fraction (tau)
    P_0 : callable
        Initial ZCB prices
    sigma : float
        Volatility

    Returns
    -------
    float
        Caplet price
    """
    tau = day_count

    # Forward LIBOR at time 0
    L_0 = (P_0(t_fixing) - P_0(t_settlement)) / (tau * P_0(t_settlement))

    # LIBOR volatility
    sigma_L = sigma * tau * np.sqrt(t_fixing)

    # Black76 formula
    d1 = (np.log(L_0 / K) + 0.5 * sigma_L**2) / sigma_L
    d2 = d1 - sigma_L

    caplet = notional * tau * P_0(t_settlement) * (L_0 * norm.cdf(d1) - K * norm.cdf(d2))
    return caplet


def main():
    """
    Demonstrate Ho-Lee model with path simulation and option pricing.
    """
    print("=" * 70)
    print("Ho-Lee Interest Rate Model Demonstration")
    print("=" * 70)

    # Parameters
    T_total = 5.0
    num_steps = 50
    num_paths = 1000

    # Model parameters
    sigma = 0.015  # Volatility (1.5%)
    r0 = 0.05      # Initial rate (5%)

    print(f"\nModel Parameters:")
    print(f"  Sigma (volatility):  {sigma:.4f}")
    print(f"  r(0) (initial rate): {r0:.4f}")
    print()

    # Simple yield curve: flat at r0
    def P_0(T):
        return np.exp(-r0 * T)

    # Theta function
    def theta_func(t):
        return compute_theta(P_0, t, sigma)

    # Generate paths
    print("Generating Ho-Lee paths...")
    t_grid, R_paths, M_paths = generate_sample_path(
        r0, theta_func, sigma, T_total, num_steps, num_paths, seed=42
    )

    print(f"  Generated {num_paths} paths with {num_steps} steps")
    print(f"  Time horizon: {T_total} years")
    print()

    # Statistics
    mean_r = np.mean(R_paths, axis=0)
    std_r = np.std(R_paths, axis=0)

    print(f"Short rate statistics at final time T={T_total}:")
    print(f"  Mean r(T):      {mean_r[-1]:.6f}")
    print(f"  Std r(T):       {std_r[-1]:.6f}")
    print(f"  Min r(T):       {R_paths[:, -1].min():.6f}")
    print(f"  Max r(T):       {R_paths[:, -1].max():.6f}")
    print()

    # Negative rates possible (characteristic of Ho-Lee without floor)
    neg_rates = np.sum(R_paths < 0) / (num_paths * (num_steps + 1))
    print(f"Proportion of negative rates: {neg_rates*100:.2f}%")
    print("(Note: Ho-Lee allows negative rates; add a floor for more realism)")
    print()

    # Option pricing examples
    T_opt = 2.0  # Option expiration
    U_opt = 5.0  # Bond maturity
    K_opt = 0.92 # Strike

    call_price = zcb_call_price(K_opt, T_opt, U_opt, P_0, r0, sigma)
    put_price = zcb_put_price(K_opt, T_opt, U_opt, P_0, r0, sigma)

    print(f"Bond Option Prices (T={T_opt}, U={U_opt}, K={K_opt}):")
    print(f"  Call price: {call_price:.6f}")
    print(f"  Put price:  {put_price:.6f}")
    print()

    # Caplet pricing
    caplet_price_val = caplet_price(K=0.05, t_fixing=1.0, t_settlement=1.25,
                                    notional=1e6, day_count=0.25, P_0=P_0, sigma=sigma)
    print(f"Caplet Price (notional 1M, K=5%, fixing at 1y):")
    print(f"  Caplet: {caplet_price_val:.2f}")
    print()

    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Sample paths
    ax = axes[0, 0]
    sample_indices = np.arange(0, num_paths, max(1, num_paths // 50))
    for idx in sample_indices:
        ax.plot(t_grid, R_paths[idx, :], alpha=0.3, linewidth=0.8)
    ax.plot(t_grid, mean_r, 'r-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, mean_r - std_r, mean_r + std_r,
                     alpha=0.2, color='red', label='Mean +/- 1 Std')
    ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Short rate r(t)')
    ax.set_title('Ho-Lee Short Rate Paths')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Terminal distribution
    ax = axes[0, 1]
    ax.hist(R_paths[:, -1], bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.axvline(mean_r[-1], color='r', linestyle='--', linewidth=2, label='Mean')
    ax.axvline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    ax.set_xlabel('Short rate r(T)')
    ax.set_ylabel('Density')
    ax.set_title(f'Terminal Distribution of r(T) at T={T_total}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 3: Mean and confidence bands
    ax = axes[1, 0]
    percentile_95 = np.percentile(R_paths, 95, axis=0)
    percentile_5 = np.percentile(R_paths, 5, axis=0)
    ax.plot(t_grid, mean_r, 'b-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, percentile_5, percentile_95, alpha=0.3, label='5%-95%')
    ax.fill_between(t_grid, 0, mean_r, where=(mean_r >= 0), alpha=0.1, color='green', label='Positive rates')
    ax.fill_between(t_grid, 0, mean_r, where=(mean_r < 0), alpha=0.1, color='red', label='Negative rates')
    ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Short rate r(t)')
    ax.set_title('Short Rate Evolution: Mean and Confidence Interval')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 4: Theta function evolution
    ax = axes[1, 1]
    theta_vals = np.array([theta_func(t) for t in t_grid])
    ax.plot(t_grid, theta_vals, 'g-', linewidth=2, label='theta(t)')
    ax.axhline(r0, color='r', linestyle='--', linewidth=2, label=f'Initial rate r(0)={r0:.4f}')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Theta(t)')
    ax.set_title('Time-Dependent Drift: theta(t) = df/dT(0,t) + sigma^2*t')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('quantpie_ho_lee_model.png', dpi=150, bbox_inches='tight')
    print("Figure saved as 'quantpie_ho_lee_model.png'")
    plt.show()


if __name__ == '__main__':
    main()
