"""
Asian Option Pricing Module
===========================

Comprehensive implementation of Asian option pricing including:
- Geometric Asian (closed-form Kemna-Vorst)
- Arithmetic Asian (Monte Carlo with control variate)
- Turnbull-Wakeman approximation
- Greeks computation

Reference: Chapter 22 - Structured Products
"""

import numpy as np
from scipy.stats import norm
from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class AsianOptionParams:
    """Parameters for Asian option pricing."""
    S0: float           # Current stock price
    K: float            # Strike price
    T: float            # Time to maturity (years)
    r: float            # Risk-free rate
    q: float            # Dividend yield
    sigma: float        # Volatility
    n_obs: int          # Number of averaging observations
    is_call: bool = True


def geometric_asian_continuous(params: AsianOptionParams) -> float:
    """
    Price a geometric Asian option with continuous averaging.
    
    Uses Kemna-Vorst (1990) closed-form formula.
    The geometric average is lognormally distributed.
    
    Parameters
    ----------
    params : AsianOptionParams
        Option parameters
        
    Returns
    -------
    float
        Option price
    """
    S0, K, T, r, q, sigma = params.S0, params.K, params.T, params.r, params.q, params.sigma
    
    # Adjusted drift and volatility for geometric average
    # For continuous averaging: Var(1/T ∫ln(S_t)dt) = σ²T/3
    sigma_adj = sigma / np.sqrt(3)
    
    # Adjusted cost of carry
    # b = r - q for asset, b_adj accounts for averaging effect
    b = r - q
    b_adj = 0.5 * (b - sigma**2 / 6)
    
    d1 = (np.log(S0 / K) + (b_adj + 0.5 * sigma_adj**2) * T) / (sigma_adj * np.sqrt(T))
    d2 = d1 - sigma_adj * np.sqrt(T)
    
    if params.is_call:
        price = S0 * np.exp((b_adj - r) * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * np.exp((b_adj - r) * T) * norm.cdf(-d1)
    
    return price


def geometric_asian_discrete(params: AsianOptionParams) -> float:
    """
    Price a geometric Asian option with discrete averaging.
    
    For n equally-spaced observations, the formula uses adjusted
    volatility and drift terms.
    
    Parameters
    ----------
    params : AsianOptionParams
        Option parameters
        
    Returns
    -------
    float
        Option price
    """
    S0, K, T, r, q, sigma, n = params.S0, params.K, params.T, params.r, params.q, params.sigma, params.n_obs
    
    # Time between observations
    dt = T / n
    
    # Adjusted volatility for discrete geometric average
    # σ_adj² = σ² * (n+1)(2n+1) / (6n²)
    sigma_adj_sq = sigma**2 * (n + 1) * (2 * n + 1) / (6 * n**2)
    sigma_adj = np.sqrt(sigma_adj_sq)
    
    # Adjusted drift
    # Mean of log(G) under risk-neutral measure
    b = r - q
    mu_adj = (b - 0.5 * sigma**2) * (n + 1) / (2 * n) + 0.5 * sigma_adj_sq
    
    # Forward price of geometric average
    F_G = S0 * np.exp(mu_adj * T)
    
    d1 = (np.log(F_G / K) + 0.5 * sigma_adj_sq * T) / (sigma_adj * np.sqrt(T))
    d2 = d1 - sigma_adj * np.sqrt(T)
    
    if params.is_call:
        price = np.exp(-r * T) * (F_G * norm.cdf(d1) - K * norm.cdf(d2))
    else:
        price = np.exp(-r * T) * (K * norm.cdf(-d2) - F_G * norm.cdf(-d1))
    
    return price


def turnbull_wakeman_approximation(params: AsianOptionParams) -> float:
    """
    Price an arithmetic Asian option using Turnbull-Wakeman approximation.
    
    Matches first two moments of arithmetic average with lognormal distribution.
    
    Parameters
    ----------
    params : AsianOptionParams
        Option parameters
        
    Returns
    -------
    float
        Approximate option price
    """
    S0, K, T, r, q, sigma, n = params.S0, params.K, params.T, params.r, params.q, params.sigma, params.n_obs
    
    b = r - q  # Cost of carry
    dt = T / n
    
    # First moment of arithmetic average
    if abs(b) < 1e-10:
        M1 = S0
    else:
        M1 = S0 * (np.exp(b * T) - 1) / (b * T)
    
    # Second moment of arithmetic average
    if abs(b) < 1e-10 and abs(b + sigma**2) < 1e-10:
        M2 = S0**2 * np.exp(sigma**2 * T)
    else:
        term1 = 2 * np.exp((2 * b + sigma**2) * T) / ((b + sigma**2) * (2 * b + sigma**2) * T**2)
        term2 = 2 / (b * T**2) * (1 / (2 * b + sigma**2) - np.exp(b * T) / (b + sigma**2))
        M2 = S0**2 * (term1 + term2)
    
    # Match to lognormal: A ~ LN(μ_A, σ_A)
    # M1 = exp(μ_A + σ_A²/2), M2 = exp(2μ_A + 2σ_A²)
    sigma_A_sq = np.log(M2 / M1**2)
    sigma_A = np.sqrt(max(sigma_A_sq, 1e-10))
    
    # Forward price of arithmetic average
    F_A = M1
    
    d1 = (np.log(F_A / K) + 0.5 * sigma_A_sq * T) / (sigma_A * np.sqrt(T))
    d2 = d1 - sigma_A * np.sqrt(T)
    
    if params.is_call:
        price = np.exp(-r * T) * (F_A * norm.cdf(d1) - K * norm.cdf(d2))
    else:
        price = np.exp(-r * T) * (K * norm.cdf(-d2) - F_A * norm.cdf(-d1))
    
    return price


def monte_carlo_asian(
    params: AsianOptionParams,
    n_paths: int = 100000,
    use_control_variate: bool = True,
    seed: Optional[int] = None
) -> Tuple[float, float]:
    """
    Price an arithmetic Asian option using Monte Carlo simulation.
    
    Optionally uses geometric Asian as control variate for variance reduction.
    
    Parameters
    ----------
    params : AsianOptionParams
        Option parameters
    n_paths : int
        Number of simulation paths
    use_control_variate : bool
        Whether to use geometric Asian as control variate
    seed : int, optional
        Random seed
        
    Returns
    -------
    tuple
        (price, standard_error)
    """
    if seed is not None:
        np.random.seed(seed)
    
    S0, K, T, r, q, sigma, n = params.S0, params.K, params.T, params.r, params.q, params.sigma, params.n_obs
    
    dt = T / n
    drift = (r - q - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt)
    
    # Simulate paths
    Z = np.random.standard_normal((n_paths, n))
    log_returns = drift + diffusion * Z
    log_prices = np.log(S0) + np.cumsum(log_returns, axis=1)
    S = np.exp(log_prices)
    
    # Arithmetic average
    A = np.mean(S, axis=1)
    
    # Geometric average (for control variate)
    G = np.exp(np.mean(log_prices, axis=1))
    
    # Payoffs
    if params.is_call:
        payoff_A = np.maximum(A - K, 0)
        payoff_G = np.maximum(G - K, 0)
    else:
        payoff_A = np.maximum(K - A, 0)
        payoff_G = np.maximum(K - G, 0)
    
    # Discounting
    df = np.exp(-r * T)
    
    if use_control_variate:
        # Closed-form geometric Asian price
        geo_price = geometric_asian_discrete(params)
        
        # Control variate adjustment
        # E[Y_adj] = E[Y] - β(E[X] - E[X]_exact)
        # where Y = arithmetic payoff, X = geometric payoff
        
        mc_geo = df * np.mean(payoff_G)
        
        # Optimal β
        cov_AG = np.cov(payoff_A, payoff_G)[0, 1]
        var_G = np.var(payoff_G)
        beta = cov_AG / var_G if var_G > 0 else 1.0
        
        # Adjusted payoffs
        adjusted_payoffs = df * payoff_A - beta * (df * payoff_G - geo_price)
        
        price = np.mean(adjusted_payoffs)
        std_error = np.std(adjusted_payoffs) / np.sqrt(n_paths)
    else:
        discounted = df * payoff_A
        price = np.mean(discounted)
        std_error = np.std(discounted) / np.sqrt(n_paths)
    
    return price, std_error


def asian_greeks(
    params: AsianOptionParams,
    method: str = 'monte_carlo',
    n_paths: int = 50000,
    seed: int = 42
) -> dict:
    """
    Compute Greeks for Asian options.
    
    Parameters
    ----------
    params : AsianOptionParams
        Option parameters
    method : str
        'monte_carlo', 'geometric', or 'turnbull_wakeman'
    n_paths : int
        Number of paths for Monte Carlo
    seed : int
        Random seed
        
    Returns
    -------
    dict
        Dictionary of Greeks
    """
    def price_func(p):
        if method == 'monte_carlo':
            return monte_carlo_asian(p, n_paths=n_paths, seed=seed)[0]
        elif method == 'geometric':
            return geometric_asian_discrete(p)
        else:
            return turnbull_wakeman_approximation(p)
    
    base_price = price_func(params)
    
    # Delta
    dS = params.S0 * 0.01
    params_up = AsianOptionParams(
        S0=params.S0 + dS, K=params.K, T=params.T, r=params.r,
        q=params.q, sigma=params.sigma, n_obs=params.n_obs, is_call=params.is_call
    )
    params_down = AsianOptionParams(
        S0=params.S0 - dS, K=params.K, T=params.T, r=params.r,
        q=params.q, sigma=params.sigma, n_obs=params.n_obs, is_call=params.is_call
    )
    delta = (price_func(params_up) - price_func(params_down)) / (2 * dS)
    gamma = (price_func(params_up) - 2 * base_price + price_func(params_down)) / (dS**2)
    
    # Vega
    dsigma = 0.01
    params_vol = AsianOptionParams(
        S0=params.S0, K=params.K, T=params.T, r=params.r,
        q=params.q, sigma=params.sigma + dsigma, n_obs=params.n_obs, is_call=params.is_call
    )
    vega = price_func(params_vol) - base_price
    
    # Theta
    dt = 1/365
    if params.T > dt:
        params_short = AsianOptionParams(
            S0=params.S0, K=params.K, T=params.T - dt, r=params.r,
            q=params.q, sigma=params.sigma, n_obs=params.n_obs, is_call=params.is_call
        )
        theta = price_func(params_short) - base_price
    else:
        theta = 0
    
    return {
        'price': base_price,
        'delta': delta,
        'gamma': gamma,
        'vega': vega,
        'theta': theta
    }


def compare_asian_methods(params: AsianOptionParams, n_paths: int = 100000, seed: int = 42) -> dict:
    """
    Compare different Asian option pricing methods.
    
    Returns
    -------
    dict
        Prices from different methods
    """
    geo_cont = geometric_asian_continuous(params)
    geo_disc = geometric_asian_discrete(params)
    tw_approx = turnbull_wakeman_approximation(params)
    mc_no_cv, se_no_cv = monte_carlo_asian(params, n_paths, use_control_variate=False, seed=seed)
    mc_cv, se_cv = monte_carlo_asian(params, n_paths, use_control_variate=True, seed=seed)
    
    return {
        'geometric_continuous': geo_cont,
        'geometric_discrete': geo_disc,
        'turnbull_wakeman': tw_approx,
        'monte_carlo_no_cv': mc_no_cv,
        'mc_no_cv_se': se_no_cv,
        'monte_carlo_cv': mc_cv,
        'mc_cv_se': se_cv,
        'variance_reduction': (se_no_cv / se_cv)**2 if se_cv > 0 else np.inf
    }


if __name__ == "__main__":
    print("=" * 60)
    print("Asian Option Pricing Examples")
    print("=" * 60)
    
    params = AsianOptionParams(
        S0=100, K=100, T=1, r=0.05, q=0.02, sigma=0.20,
        n_obs=12, is_call=True
    )
    
    print(f"\nParameters:")
    print(f"  S0=${params.S0}, K=${params.K}, T={params.T}yr")
    print(f"  r={params.r*100}%, q={params.q*100}%, σ={params.sigma*100}%")
    print(f"  Observations: {params.n_obs} (monthly)")
    
    # Compare methods
    print("\n" + "-" * 50)
    print("Asian Call Pricing Comparison:")
    print("-" * 50)
    
    results = compare_asian_methods(params, n_paths=100000, seed=42)
    
    print(f"Geometric (continuous):   ${results['geometric_continuous']:.4f}")
    print(f"Geometric (discrete):     ${results['geometric_discrete']:.4f}")
    print(f"Turnbull-Wakeman:         ${results['turnbull_wakeman']:.4f}")
    print(f"Monte Carlo (no CV):      ${results['monte_carlo_no_cv']:.4f} ± ${1.96*results['mc_no_cv_se']:.4f}")
    print(f"Monte Carlo (with CV):    ${results['monte_carlo_cv']:.4f} ± ${1.96*results['mc_cv_se']:.4f}")
    print(f"Variance Reduction:       {results['variance_reduction']:.1f}x")
    
    # Greeks
    print("\n" + "-" * 50)
    print("Greeks (Turnbull-Wakeman):")
    print("-" * 50)
    
    greeks = asian_greeks(params, method='turnbull_wakeman')
    print(f"Price:  ${greeks['price']:.4f}")
    print(f"Delta:  {greeks['delta']:.4f}")
    print(f"Gamma:  {greeks['gamma']:.4f}")
    print(f"Vega:   ${greeks['vega']:.4f} (per 1% vol)")
    print(f"Theta:  ${greeks['theta']:.4f} (per day)")
    
    # Asian vs Vanilla comparison
    print("\n" + "-" * 50)
    print("Asian vs Vanilla Comparison:")
    print("-" * 50)
    
    from scipy.stats import norm as norm_dist
    
    def bs_call(S, K, T, r, q, sigma):
        d1 = (np.log(S/K) + (r - q + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        return S*np.exp(-q*T)*norm_dist.cdf(d1) - K*np.exp(-r*T)*norm_dist.cdf(d2)
    
    vanilla = bs_call(params.S0, params.K, params.T, params.r, params.q, params.sigma)
    asian = results['monte_carlo_cv']
    
    print(f"Vanilla Call:  ${vanilla:.4f}")
    print(f"Asian Call:    ${asian:.4f}")
    print(f"Discount:      {(1 - asian/vanilla)*100:.1f}%")
    print(f"\nNote: Asian cheaper due to averaging effect (lower effective volatility)")
