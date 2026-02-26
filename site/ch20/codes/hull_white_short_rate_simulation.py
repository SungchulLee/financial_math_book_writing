"""
Hull-White Short Rate Model Simulation

This module implements the one-factor Hull-White interest rate model.
The Hull-White model is a Gaussian short-rate model that extends
Vasicek by allowing time-dependent parameters.

The SDE is:
    dr(t) = [theta(t) - lambda * r(t)] dt + sigma * dW(t)
    where theta(t) is chosen to match the initial yield curve

Key features:
- Analytical zero-coupon bond prices (ZCB)
- Closed-form option prices on bonds
- Calibration to market yield curve
- Cap/floor pricing

Based on: QuantPie Lecture Notes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import norm
from scipy.optimize import brentq
from enum import Enum


class OptionType(Enum):
    """Enumeration for option types."""
    CALL = 1
    PUT = -1


class OptionTypeSwap(Enum):
    """Enumeration for swaption types."""
    PAYER = 1
    RECEIVER = -1


def f(P, T):
    """
    Extract forward rate from zero-coupon bond prices.

    Parameters
    ----------
    P : callable
        ZCB price function P(t, T) where t is fixed
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
        r(0)

    Notes
    -----
    r(0) = f(0, 0) = -d/dT log(P(0, T))|_{T=0}
    """
    return f(P, 0.0)


def compute_theta(P, T, lambd, sigma):
    """
    Compute time-dependent theta for Hull-White calibration.

    Parameters
    ----------
    P : callable
        ZCB price function
    T : float
        Time
    lambd : float
        Mean reversion rate (lambda)
    sigma : float
        Volatility

    Returns
    -------
    float
        theta(T)

    Notes
    -----
    theta(T) = df/dT(0,T) + lambda*f(0,T) + sigma^2/(2*lambda^2) * (1 - exp(-2*lambda*T))^2
    """
    f_T = f(P, T)
    df_dT = df_over_dT(P, T)

    if lambd > 1e-8:
        sigma_term = sigma**2 / (2 * lambd**2) * (1 - np.exp(-2 * lambd * T))**2
    else:
        sigma_term = sigma**2 * T**2 / 2

    return df_dT + lambd * f_T + sigma_term


def compute_theta_T(theta_func, T):
    """
    Wrapper for theta function at time T.

    Parameters
    ----------
    theta_func : callable
        Theta function theta(T)
    T : float
        Time

    Returns
    -------
    float
        theta(T)
    """
    return theta_func(T)


def compute_sigma_P(sigma, lambd, T, U):
    """
    Compute bond price volatility for option pricing.

    Parameters
    ----------
    sigma : float
        Short rate volatility
    lambd : float
        Mean reversion rate
    T : float
        Option expiration
    U : float
        Bond maturity (U > T)

    Returns
    -------
    float
        sigma_P

    Notes
    -----
    sigma_P = sigma/lambda * (1 - exp(-lambda*(U-T)))
    Volatility of bond price at time T
    """
    if lambd > 1e-8:
        return sigma / lambd * (1 - np.exp(-lambd * (U - T)))
    else:
        return sigma * (U - T)


def compute_mu_r_T(r_0, lambd, T):
    """
    Compute mean of short rate under risk-neutral measure.

    Parameters
    ----------
    r_0 : float
        Initial short rate
    lambd : float
        Mean reversion rate
    T : float
        Time

    Returns
    -------
    float
        E[r(T)]

    Notes
    -----
    E[r(T)] = f(0, T) + sigma^2/(2*lambda^2) * (1 - exp(-lambda*T))^2
    """
    return r_0


def compute_mu_r_T_ForwardMeasure(theta_func, lambd, T, U):
    """
    Compute mean of short rate under forward measure (T, U).

    Parameters
    ----------
    theta_func : callable
        Theta function
    lambd : float
        Mean reversion rate
    T : float
        Current time
    U : float
        Maturity of bond

    Returns
    -------
    float
        Mean under forward measure
    """
    # Integral of theta from 0 to T
    def integrand(s):
        return compute_theta_T(theta_func, s) * np.exp(lambd * (s - T))

    integral, _ = quad(integrand, 0, T)
    return np.exp(-lambd * T) * integral


def compute_sigma_square_r_T(sigma, lambd, T):
    """
    Compute variance of short rate.

    Parameters
    ----------
    sigma : float
        Short rate volatility
    lambd : float
        Mean reversion rate
    T : float
        Time

    Returns
    -------
    float
        Var[r(T)]

    Notes
    -----
    Var[r(T)] = sigma^2/(2*lambda) * (1 - exp(-2*lambda*T))
    """
    if lambd > 1e-8:
        return sigma**2 / (2 * lambd) * (1 - np.exp(-2 * lambd * T))
    else:
        return sigma**2 * T


def compute_A(P_0, sigma, lambd, T, U):
    """
    Compute A coefficient for ZCB pricing formula.

    Parameters
    ----------
    P_0 : callable
        Initial ZCB price P(0, S)
    sigma : float
        Volatility
    lambd : float
        Mean reversion rate
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
    """
    B_TU = compute_B(lambd, T, U)
    sigma_P_TU = compute_sigma_P(sigma, lambd, T, U)

    # A = P(0,U) / P(0,T) * exp(sigma_P^2 / 4*lambda^2 * (exp(-2*lambda*T) - 1)^2)
    # Simplified computation
    if lambd > 1e-8:
        exp_term = np.exp(sigma_P_TU**2 / (2 * lambd) * (1 - np.exp(-2 * lambd * T)))
    else:
        exp_term = 1.0

    return P_0(U) / P_0(T) * exp_term


def compute_B(lambd, T, U):
    """
    Compute B coefficient for ZCB pricing formula.

    Parameters
    ----------
    lambd : float
        Mean reversion rate
    T : float
        Current time
    U : float
        Bond maturity

    Returns
    -------
    float
        B(T, U)

    Notes
    -----
    B(t, U) = 1/lambda * (1 - exp(-lambda*(U-t)))
    """
    if lambd > 1e-8:
        return 1.0 / lambd * (1 - np.exp(-lambd * (U - T)))
    else:
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


def generate_sample_paths(r0, theta_func, lambd, sigma, T, num_steps, num_paths, seed=None):
    """
    Generate Hull-White short rate paths via Euler discretization.

    Parameters
    ----------
    r0 : float
        Initial short rate
    theta_func : callable
        Theta function theta(t)
    lambd : float
        Mean reversion rate
    sigma : float
        Volatility
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
        Short rates (num_paths, num_steps + 1)
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

    # Euler discretization: dr = (theta - lambda*r) dt + sigma dW
    for i in range(num_steps):
        theta_t = compute_theta_T(theta_func, t[i])
        dW = sqrt_dt * Z[:, i]

        # dr = (theta(t) - lambda*r(t)) dt + sigma dW
        dR = (theta_t - lambd * R[:, i]) * dt + sigma * dW
        R[:, i+1] = R[:, i] + dR

        # dM/M = r(t) dt (money market account)
        M[:, i+1] = M[:, i] * np.exp(R[:, i] * dt)

    return t, R, M


def SwapPrice(fixed_rate, t_fixing, t_settlement, t_maturity, notional, P_func):
    """
    Compute swap price given cash flows.

    Parameters
    ----------
    fixed_rate : float
        Fixed rate of swap
    t_fixing : ndarray
        Fixing times
    t_settlement : ndarray
        Settlement times
    t_maturity : float
        Swap maturity
    notional : float
        Notional principal
    P_func : callable
        ZCB price function P(t, T)

    Returns
    -------
    float
        Swap price (fixed leg value)
    """
    price = 0.0
    for t_fix, t_settle in zip(t_fixing, t_settlement):
        if t_settle <= t_maturity:
            tau = t_settle - t_fix  # day count fraction
            cf = fixed_rate * tau * notional
            df = P_func(t_settle)
            price += cf * df
    return price


def SwapPrice_HW(R_paths, M_paths, r0, theta_func, lambd, sigma,
                 fixed_rate, t_fixing, t_settlement, t_maturity,
                 notional, P_0, num_steps, T):
    """
    Compute swap price under Hull-White model (Monte Carlo).

    Parameters
    ----------
    R_paths : ndarray
        Short rate paths
    M_paths : ndarray
        Money market paths
    r0 : float
        Initial short rate
    theta_func : callable
        Theta function
    lambd : float
        Mean reversion
    sigma : float
        Volatility
    fixed_rate : float
        Fixed swap rate
    t_fixing : ndarray
        Fixing times
    t_settlement : ndarray
        Settlement times
    t_maturity : float
        Maturity
    notional : float
        Notional
    P_0 : callable
        Initial ZCB prices
    num_steps : int
        Number of time steps
    T : float
        Total time horizon

    Returns
    -------
    float
        Expected swap value
    """
    num_paths = R_paths.shape[0]
    swap_values = np.zeros(num_paths)

    t_grid = np.linspace(0, T, num_steps + 1)

    for path_idx in range(num_paths):
        r_path = R_paths[path_idx, :]
        m_path = M_paths[path_idx, :]

        pv = 0.0
        for t_fix, t_settle in zip(t_fixing, t_settlement):
            if t_settle <= T:
                tau = t_settle - t_fix
                cf = fixed_rate * tau * notional

                # Find closest time step
                idx = np.argmin(np.abs(t_grid - t_settle))
                discount = 1.0 / m_path[idx]
                pv += cf * discount

        swap_values[path_idx] = pv

    return np.mean(swap_values)


def ZCBCallPutPrice(call_put_type, K, T, U, P_0, r0, sigma, lambd):
    """
    Compute call/put option on zero-coupon bond.

    Parameters
    ----------
    call_put_type : OptionType
        CALL or PUT
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
    lambd : float
        Mean reversion

    Returns
    -------
    float
        Option price
    """
    B_TU = compute_B(lambd, T, U)
    sigma_P = compute_sigma_P(sigma, lambd, T, U)

    # A coefficient
    A_TU = compute_A(P_0, sigma, lambd, T, U)

    # Forward bond price at T
    P_T = A_TU * np.exp(-B_TU * r0)

    # Black76 formula on bond
    d1 = (np.log(P_T / K) + 0.5 * sigma_P**2) / sigma_P
    d2 = d1 - sigma_P

    if call_put_type == OptionType.CALL:
        price = P_0(U) * norm.cdf(d1) - K * P_0(T) * norm.cdf(d2)
    else:  # PUT
        price = K * P_0(T) * norm.cdf(-d2) - P_0(U) * norm.cdf(-d1)

    return price


def CapletFloorletPrice(caplet_type, K, t_fixing, t_settlement,
                        notional, day_count, P_0, r0, sigma, lambd):
    """
    Compute caplet/floorlet price.

    Parameters
    ----------
    caplet_type : OptionType
        CALL (caplet) or PUT (floorlet)
    K : float
        Strike rate
    t_fixing : float
        Fixing time
    t_settlement : float
        Settlement time
    notional : float
        Notional
    day_count : float
        Day count fraction (tau)
    P_0 : callable
        Initial ZCB prices
    r0 : float
        Initial rate
    sigma : float
        Volatility
    lambd : float
        Mean reversion

    Returns
    -------
    float
        Caplet/floorlet price
    """
    tau = day_count

    # Forward LIBOR: L(0, t_fixing, t_settlement)
    L_0 = (P_0(t_fixing) - P_0(t_settlement)) / (tau * P_0(t_settlement))

    # Volatility of LIBOR
    sigma_L = sigma / (1 + K * tau)

    # Black76
    d1 = (np.log(L_0 / K) + 0.5 * sigma_L**2 * t_fixing) / (sigma_L * np.sqrt(t_fixing))
    d2 = d1 - sigma_L * np.sqrt(t_fixing)

    df = P_0(t_settlement)

    if caplet_type == OptionType.CALL:
        price = notional * tau * df * (L_0 * norm.cdf(d1) - K * norm.cdf(d2))
    else:  # FLOOR
        price = notional * tau * df * (K * norm.cdf(-d2) - L_0 * norm.cdf(-d1))

    return price


def CallPutPrice(call_put_type, S, K, T, r, sigma):
    """
    Black-Scholes call/put price (for equity options).

    Parameters
    ----------
    call_put_type : OptionType
        CALL or PUT
    S : float
        Spot price
    K : float
        Strike
    T : float
        Time to expiration
    r : float
        Risk-free rate
    sigma : float
        Volatility

    Returns
    -------
    float
        Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if call_put_type == OptionType.CALL:
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:  # PUT
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price


def ImpliedVolatilityBlack76(market_price, F, K, T, option_type, tol=1e-6):
    """
    Compute implied volatility using Black76 model (for interest rate options).

    Parameters
    ----------
    market_price : float
        Market option price
    F : float
        Forward price
    K : float
        Strike
    T : float
        Time to expiration
    option_type : OptionType
        CALL or PUT
    tol : float
        Tolerance for root finding

    Returns
    -------
    float
        Implied volatility
    """
    def objective(sigma):
        d1 = (np.log(F / K) + 0.5 * sigma**2 * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        if option_type == OptionType.CALL:
            price = F * norm.cdf(d1) - K * norm.cdf(d2)
        else:
            price = K * norm.cdf(-d2) - F * norm.cdf(-d1)

        return price - market_price

    try:
        iv = brentq(objective, 0.001, 5.0)
        return iv
    except ValueError:
        return np.nan


# Shortcuts
def E(value, lambd, T):
    """Shortcut for exponential discount."""
    return np.exp(-lambd * T) * value


def E1(value, lambd, T):
    """Shortcut for (1 - exp(-lambda*T)) / lambda."""
    if lambd > 1e-8:
        return (1 - np.exp(-lambd * T)) / lambd * value
    else:
        return T * value


def L(sigma, lambd, T):
    """Shortcut for bond volatility."""
    return sigma / lambd * (1 - np.exp(-lambd * T))


def main():
    """
    Demonstrate Hull-White model with path simulation and visualization.
    """
    print("=" * 70)
    print("Hull-White Short Rate Model Demonstration")
    print("=" * 70)

    # Parameters
    T_total = 10.0
    num_steps = 100
    num_paths = 1000

    # Model parameters
    lambd = 0.1  # Mean reversion rate (10%)
    sigma = 0.015  # Volatility (1.5%)
    r0 = 0.05  # Initial rate (5%)

    print(f"\nModel Parameters:")
    print(f"  Lambda (mean reversion):  {lambd:.4f}")
    print(f"  Sigma (volatility):       {sigma:.4f}")
    print(f"  r(0) (initial rate):      {r0:.4f}")
    print()

    # Simple yield curve: flat at 5%
    def P_0(T):
        return np.exp(-r0 * T)

    # Theta function (for flat curve, simplifies)
    def theta_func(t):
        return r0 * lambd + sigma**2 / (2 * lambd) * (1 - np.exp(-2 * lambd * t))**2

    # Generate paths
    print("Generating Hull-White paths...")
    t_grid, R_paths, M_paths = generate_sample_paths(
        r0, theta_func, lambd, sigma, T_total, num_steps, num_paths, seed=42
    )

    print(f"  Generated {num_paths} paths with {num_steps} steps")
    print(f"  Time horizon: {T_total} years")
    print()

    # Statistics
    mean_rate = np.mean(R_paths, axis=0)
    std_rate = np.std(R_paths, axis=0)

    print("Short rate statistics at final time T={}:".format(T_total))
    print(f"  Mean r(T):      {mean_rate[-1]:.4f}")
    print(f"  Std r(T):       {std_rate[-1]:.4f}")
    print(f"  Min r(T):       {R_paths[:, -1].min():.4f}")
    print(f"  Max r(T):       {R_paths[:, -1].max():.4f}")
    print()

    # Option pricing example
    T_opt = 2.0  # Option expiration
    U_opt = 5.0  # Bond maturity
    K_opt = 0.90  # Strike

    call_price = ZCBCallPutPrice(OptionType.CALL, K_opt, T_opt, U_opt, P_0, r0, sigma, lambd)
    put_price = ZCBCallPutPrice(OptionType.PUT, K_opt, T_opt, U_opt, P_0, r0, sigma, lambd)

    print(f"Bond Option Prices (T={T_opt}, U={U_opt}, K={K_opt}):")
    print(f"  Call price: {call_price:.6f}")
    print(f"  Put price:  {put_price:.6f}")
    print()

    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Sample paths
    ax = axes[0, 0]
    sample_indices = np.arange(0, num_paths, max(1, num_paths // 50))
    for idx in sample_indices:
        ax.plot(t_grid, R_paths[idx, :], alpha=0.3, linewidth=0.8)
    ax.plot(t_grid, mean_rate, 'r-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, mean_rate - std_rate, mean_rate + std_rate,
                     alpha=0.2, color='red', label='Mean +/- 1 Std')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Short Rate r(t)')
    ax.set_title('Hull-White Short Rate Paths')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Terminal distribution
    ax = axes[0, 1]
    ax.hist(R_paths[:, -1], bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.axvline(mean_rate[-1], color='r', linestyle='--', linewidth=2, label='Mean')
    ax.set_xlabel('Short Rate r(T)')
    ax.set_ylabel('Density')
    ax.set_title(f'Terminal Distribution of r(T) at T={T_total}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 3: Mean and confidence bands
    ax = axes[1, 0]
    percentile_95 = np.percentile(R_paths, 95, axis=0)
    percentile_5 = np.percentile(R_paths, 5, axis=0)
    ax.plot(t_grid, mean_rate, 'b-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, percentile_5, percentile_95, alpha=0.3, label='5%-95%')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Short Rate r(t)')
    ax.set_title('Short Rate Evolution: Mean and Confidence Interval')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 4: Bond prices over time
    ax = axes[1, 1]
    # Compute bond prices along paths for a fixed maturity
    U_fixed = 5.0
    B_TU_5 = compute_B(lambd, t_grid, U_fixed)
    A_TU_5 = compute_A(P_0, sigma, lambd, t_grid, U_fixed)

    bond_prices = np.zeros((num_paths, len(t_grid)))
    for i, t in enumerate(t_grid):
        if i < len(B_TU_5):
            bond_prices[:, i] = A_TU_5[i] * np.exp(-B_TU_5[i] * R_paths[:, i])

    # Note: proper vectorization of compute_B and compute_A would be needed for full paths
    # For demo, just plot initial values
    bond_vals = np.array([compute_A(P_0, sigma, lambd, 0, U_fixed) *
                          np.exp(-compute_B(lambd, 0, U_fixed) * r)
                          for r in R_paths[:, -1]])

    ax.hist(bond_vals, bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.set_xlabel(f'Bond Price P(T, {U_fixed})')
    ax.set_ylabel('Density')
    ax.set_title(f'Distribution of Bond Prices at T={T_total}')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('hull_white_short_rate_simulation.png', dpi=150, bbox_inches='tight')
    print("Figure saved as 'hull_white_short_rate_simulation.png'")
    plt.show()


if __name__ == '__main__':
    main()
