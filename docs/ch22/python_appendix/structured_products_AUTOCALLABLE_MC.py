"""
Autocallable Note Pricing Module
================================

Monte Carlo simulation for pricing autocallable structured notes including:
- Standard autocallables with periodic observations
- Step-down autocallables
- Memory coupon features
- Worst-of multi-asset autocallables
- Greeks computation via bump-and-revalue

Reference: Chapter 22 - Structured Products
"""

import numpy as np
from typing import Tuple, Optional, List
from dataclasses import dataclass
from enum import Enum


@dataclass
class AutocallableParams:
    """Parameters for autocallable note pricing."""
    S0: float                    # Initial stock price (or array for multi-asset)
    principal: float             # Note principal
    T: float                     # Maturity (years)
    r: float                     # Risk-free rate
    q: float                     # Dividend yield (or array for multi-asset)
    sigma: float                 # Volatility (or array for multi-asset)
    autocall_level: float        # Autocall trigger (as % of initial, e.g., 1.0 = 100%)
    coupon_barrier: float        # Coupon barrier (as % of initial)
    ki_barrier: float            # Knock-in barrier (as % of initial)
    coupon_rate: float           # Annual coupon rate (e.g., 0.10 = 10%)
    observation_freq: int        # Observations per year (e.g., 4 for quarterly)
    step_down: float = 0.0       # Step-down per observation (e.g., 0.05 = 5%)
    memory_coupon: bool = False  # Whether coupons accumulate (memory feature)


@dataclass  
class MultiAssetParams:
    """Parameters for worst-of autocallable."""
    S0: np.ndarray               # Initial prices array
    principal: float
    T: float
    r: float
    q: np.ndarray                # Dividend yields array
    sigma: np.ndarray            # Volatilities array
    rho: np.ndarray              # Correlation matrix
    autocall_level: float
    coupon_barrier: float
    ki_barrier: float
    coupon_rate: float
    observation_freq: int
    step_down: float = 0.0
    memory_coupon: bool = False


def price_autocallable(
    params: AutocallableParams,
    n_paths: int = 100000,
    n_steps_per_obs: int = 5,
    seed: Optional[int] = None
) -> dict:
    """
    Price a single-asset autocallable note using Monte Carlo simulation.
    
    Parameters
    ----------
    params : AutocallableParams
        Note parameters
    n_paths : int
        Number of simulation paths
    n_steps_per_obs : int
        Time steps between observations (for path resolution)
    seed : int, optional
        Random seed
        
    Returns
    -------
    dict
        Contains: price, std_error, autocall_prob, ki_prob, avg_life
        
    Example
    -------
    >>> params = AutocallableParams(
    ...     S0=100, principal=1000, T=3, r=0.05, q=0.02, sigma=0.25,
    ...     autocall_level=1.0, coupon_barrier=0.7, ki_barrier=0.6,
    ...     coupon_rate=0.10, observation_freq=4
    ... )
    >>> result = price_autocallable(params, n_paths=50000)
    >>> print(f"Price: ${result['price']:.2f}")
    """
    if seed is not None:
        np.random.seed(seed)
    
    S0 = params.S0
    principal = params.principal
    T = params.T
    r = params.r
    q = params.q
    sigma = params.sigma
    
    n_obs = int(params.observation_freq * T)
    dt_obs = T / n_obs
    n_steps = n_obs * n_steps_per_obs
    dt = T / n_steps
    
    # Generate paths
    drift = (r - q - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt)
    
    Z = np.random.standard_normal((n_paths, n_steps))
    log_returns = drift + diffusion * Z
    log_prices = np.log(S0) + np.cumsum(log_returns, axis=1)
    S = np.exp(log_prices)
    
    # Extract observation dates
    obs_indices = [i * n_steps_per_obs - 1 for i in range(1, n_obs + 1)]
    S_obs = S[:, obs_indices]  # Shape: (n_paths, n_obs)
    
    # Track minimum for KI barrier
    S_min = np.minimum.accumulate(S, axis=1)[:, obs_indices]
    
    # Initialize tracking arrays
    payoffs = np.zeros(n_paths)
    redemption_times = np.full(n_paths, T)
    autocalled = np.zeros(n_paths, dtype=bool)
    knocked_in = np.zeros(n_paths, dtype=bool)
    
    # Coupon tracking for memory feature
    if params.memory_coupon:
        missed_coupons = np.zeros(n_paths)
    
    # Process each observation
    for i in range(n_obs):
        obs_time = (i + 1) * dt_obs
        
        # Step-down adjustment
        current_autocall = params.autocall_level - i * params.step_down
        
        # Performance relative to initial
        perf = S_obs[:, i] / S0
        min_perf = S_min[:, i] / S0
        
        # Check knock-in (barrier breach)
        knocked_in = knocked_in | (min_perf <= params.ki_barrier)
        
        # Paths not yet autocalled
        active = ~autocalled
        
        # Check autocall condition
        autocall_now = active & (perf >= current_autocall)
        
        if np.any(autocall_now):
            # Coupon payment
            coupon_periods = i + 1
            if params.memory_coupon:
                total_coupon = (coupon_periods * params.coupon_rate / params.observation_freq + 
                               missed_coupons[autocall_now]) * principal
            else:
                total_coupon = coupon_periods * params.coupon_rate / params.observation_freq * principal
            
            payoffs[autocall_now] = principal + total_coupon
            redemption_times[autocall_now] = obs_time
            autocalled[autocall_now] = True
        
        # Track missed coupons for memory feature
        if params.memory_coupon:
            coupon_missed = active & ~autocall_now & (perf < params.coupon_barrier)
            missed_coupons[coupon_missed] += params.coupon_rate / params.observation_freq
    
    # Final observation for non-autocalled paths
    still_active = ~autocalled
    final_perf = S_obs[:, -1] / S0
    
    # Final payoff calculation
    # If knocked in: receive min(principal, principal * final_perf)
    # If not knocked in: receive principal
    
    final_payoff = np.zeros(np.sum(still_active))
    ki_active = knocked_in[still_active]
    final_perf_active = final_perf[still_active]
    
    # Not knocked in: full principal
    final_payoff[~ki_active] = principal
    
    # Knocked in: may lose principal
    final_payoff[ki_active] = principal * np.minimum(1.0, final_perf_active[ki_active])
    
    # Add final coupon if above coupon barrier
    coupon_earned = final_perf_active >= params.coupon_barrier
    final_coupon = params.coupon_rate * T * principal
    if params.memory_coupon:
        final_payoff[coupon_earned] += (final_coupon + missed_coupons[still_active][coupon_earned] * principal)
    else:
        # Only last period coupon if not memory
        final_payoff[coupon_earned] += params.coupon_rate / params.observation_freq * principal
    
    payoffs[still_active] = final_payoff
    
    # Discount payoffs
    discount_factors = np.exp(-r * redemption_times)
    discounted_payoffs = payoffs * discount_factors
    
    # Statistics
    price = np.mean(discounted_payoffs)
    std_error = np.std(discounted_payoffs) / np.sqrt(n_paths)
    autocall_prob = np.mean(autocalled)
    ki_prob = np.mean(knocked_in)
    avg_life = np.mean(redemption_times)
    
    return {
        'price': price,
        'std_error': std_error,
        'autocall_prob': autocall_prob,
        'ki_prob': ki_prob,
        'avg_life': avg_life,
        'price_pct': price / principal * 100
    }


def price_worst_of_autocallable(
    params: MultiAssetParams,
    n_paths: int = 100000,
    n_steps_per_obs: int = 5,
    seed: Optional[int] = None
) -> dict:
    """
    Price a worst-of autocallable note on multiple assets.
    
    The autocall and coupon barriers are based on the worst performing asset.
    
    Parameters
    ----------
    params : MultiAssetParams
        Multi-asset note parameters
    n_paths : int
        Number of simulation paths
    n_steps_per_obs : int
        Time steps between observations
    seed : int, optional
        Random seed
        
    Returns
    -------
    dict
        Pricing results
    """
    if seed is not None:
        np.random.seed(seed)
    
    n_assets = len(params.S0)
    S0 = params.S0
    principal = params.principal
    T = params.T
    r = params.r
    
    n_obs = int(params.observation_freq * T)
    dt_obs = T / n_obs
    n_steps = n_obs * n_steps_per_obs
    dt = T / n_steps
    
    # Cholesky decomposition for correlated assets
    L = np.linalg.cholesky(params.rho)
    
    # Generate correlated paths for all assets
    S_all = np.zeros((n_assets, n_paths, n_steps))
    
    for step in range(n_steps):
        Z_indep = np.random.standard_normal((n_assets, n_paths))
        Z_corr = L @ Z_indep
        
        for i in range(n_assets):
            drift = (r - params.q[i] - 0.5 * params.sigma[i]**2) * dt
            diffusion = params.sigma[i] * np.sqrt(dt)
            
            if step == 0:
                S_all[i, :, step] = S0[i] * np.exp(drift + diffusion * Z_corr[i])
            else:
                S_all[i, :, step] = S_all[i, :, step-1] * np.exp(drift + diffusion * Z_corr[i])
    
    # Extract observation dates
    obs_indices = [i * n_steps_per_obs - 1 for i in range(1, n_obs + 1)]
    
    # Compute performance relative to initial for each asset
    perf_all = np.zeros((n_assets, n_paths, n_obs))
    for i in range(n_assets):
        perf_all[i] = S_all[i, :, obs_indices] / S0[i]
    
    # Worst performer at each observation
    worst_perf = np.min(perf_all, axis=0)  # Shape: (n_paths, n_obs)
    
    # Minimum of worst performer (for KI)
    min_worst_perf = np.minimum.accumulate(worst_perf, axis=1)
    
    # Initialize tracking
    payoffs = np.zeros(n_paths)
    redemption_times = np.full(n_paths, T)
    autocalled = np.zeros(n_paths, dtype=bool)
    knocked_in = np.zeros(n_paths, dtype=bool)
    
    # Process observations
    for i in range(n_obs):
        obs_time = (i + 1) * dt_obs
        current_autocall = params.autocall_level - i * params.step_down
        
        # Check knock-in
        knocked_in = knocked_in | (min_worst_perf[:, i] <= params.ki_barrier)
        
        active = ~autocalled
        
        # Autocall if worst performer >= autocall level
        autocall_now = active & (worst_perf[:, i] >= current_autocall)
        
        if np.any(autocall_now):
            coupon_periods = i + 1
            total_coupon = coupon_periods * params.coupon_rate / params.observation_freq * principal
            payoffs[autocall_now] = principal + total_coupon
            redemption_times[autocall_now] = obs_time
            autocalled[autocall_now] = True
    
    # Final payoff
    still_active = ~autocalled
    final_worst = worst_perf[:, -1]
    
    final_payoff = np.zeros(np.sum(still_active))
    ki_active = knocked_in[still_active]
    final_worst_active = final_worst[still_active]
    
    final_payoff[~ki_active] = principal
    final_payoff[ki_active] = principal * np.minimum(1.0, final_worst_active[ki_active])
    
    # Final coupon
    coupon_earned = final_worst_active >= params.coupon_barrier
    final_payoff[coupon_earned] += params.coupon_rate / params.observation_freq * principal
    
    payoffs[still_active] = final_payoff
    
    # Discount
    discount_factors = np.exp(-r * redemption_times)
    discounted_payoffs = payoffs * discount_factors
    
    price = np.mean(discounted_payoffs)
    std_error = np.std(discounted_payoffs) / np.sqrt(n_paths)
    
    return {
        'price': price,
        'std_error': std_error,
        'autocall_prob': np.mean(autocalled),
        'ki_prob': np.mean(knocked_in),
        'avg_life': np.mean(redemption_times),
        'price_pct': price / principal * 100
    }


def compute_autocallable_greeks(
    params: AutocallableParams,
    n_paths: int = 50000,
    seed: int = 42
) -> dict:
    """
    Compute Greeks for autocallable using bump-and-revalue.
    
    Returns
    -------
    dict
        delta, gamma, vega, rho (interest rate), correlation sensitivity
    """
    base_result = price_autocallable(params, n_paths=n_paths, seed=seed)
    base_price = base_result['price']
    
    # Delta
    bump_pct = 0.01
    dS = params.S0 * bump_pct
    
    params_up = AutocallableParams(
        S0=params.S0 + dS, principal=params.principal, T=params.T,
        r=params.r, q=params.q, sigma=params.sigma,
        autocall_level=params.autocall_level, coupon_barrier=params.coupon_barrier,
        ki_barrier=params.ki_barrier, coupon_rate=params.coupon_rate,
        observation_freq=params.observation_freq, step_down=params.step_down,
        memory_coupon=params.memory_coupon
    )
    params_down = AutocallableParams(
        S0=params.S0 - dS, principal=params.principal, T=params.T,
        r=params.r, q=params.q, sigma=params.sigma,
        autocall_level=params.autocall_level, coupon_barrier=params.coupon_barrier,
        ki_barrier=params.ki_barrier, coupon_rate=params.coupon_rate,
        observation_freq=params.observation_freq, step_down=params.step_down,
        memory_coupon=params.memory_coupon
    )
    
    price_up = price_autocallable(params_up, n_paths=n_paths, seed=seed)['price']
    price_down = price_autocallable(params_down, n_paths=n_paths, seed=seed)['price']
    
    delta = (price_up - price_down) / (2 * dS)
    gamma = (price_up - 2 * base_price + price_down) / (dS ** 2)
    
    # Vega (per 1% vol)
    dsigma = 0.01
    params_vol_up = AutocallableParams(
        S0=params.S0, principal=params.principal, T=params.T,
        r=params.r, q=params.q, sigma=params.sigma + dsigma,
        autocall_level=params.autocall_level, coupon_barrier=params.coupon_barrier,
        ki_barrier=params.ki_barrier, coupon_rate=params.coupon_rate,
        observation_freq=params.observation_freq, step_down=params.step_down,
        memory_coupon=params.memory_coupon
    )
    price_vol_up = price_autocallable(params_vol_up, n_paths=n_paths, seed=seed)['price']
    vega = price_vol_up - base_price
    
    # Rho (per 1% rate)
    dr = 0.01
    params_rate_up = AutocallableParams(
        S0=params.S0, principal=params.principal, T=params.T,
        r=params.r + dr, q=params.q, sigma=params.sigma,
        autocall_level=params.autocall_level, coupon_barrier=params.coupon_barrier,
        ki_barrier=params.ki_barrier, coupon_rate=params.coupon_rate,
        observation_freq=params.observation_freq, step_down=params.step_down,
        memory_coupon=params.memory_coupon
    )
    price_rate_up = price_autocallable(params_rate_up, n_paths=n_paths, seed=seed)['price']
    rho = price_rate_up - base_price
    
    return {
        'price': base_price,
        'delta': delta,
        'delta_pct': delta * params.S0 / params.principal * 100,
        'gamma': gamma,
        'vega': vega,
        'rho': rho
    }


if __name__ == "__main__":
    print("=" * 60)
    print("Autocallable Note Pricing Examples")
    print("=" * 60)
    
    # Single asset autocallable
    params = AutocallableParams(
        S0=100,
        principal=10000,
        T=3,
        r=0.05,
        q=0.02,
        sigma=0.25,
        autocall_level=1.0,      # 100% of initial
        coupon_barrier=0.70,     # 70% of initial
        ki_barrier=0.60,         # 60% knock-in
        coupon_rate=0.10,        # 10% annual
        observation_freq=4,      # Quarterly
        step_down=0.025,         # 2.5% step-down per observation
        memory_coupon=True
    )
    
    print("\nSingle Asset Autocallable:")
    print(f"  S0=${params.S0}, Principal=${params.principal}")
    print(f"  T={params.T}yr, Coupon={params.coupon_rate*100}%, KI={params.ki_barrier*100}%")
    print(f"  Step-down: {params.step_down*100}% per observation")
    
    result = price_autocallable(params, n_paths=100000, seed=42)
    
    print(f"\nResults:")
    print(f"  Price: ${result['price']:.2f} ({result['price_pct']:.2f}%)")
    print(f"  Std Error: ${result['std_error']:.2f}")
    print(f"  Autocall Probability: {result['autocall_prob']*100:.1f}%")
    print(f"  Knock-In Probability: {result['ki_prob']*100:.1f}%")
    print(f"  Average Life: {result['avg_life']:.2f} years")
    
    # Worst-of autocallable
    print("\n" + "-" * 50)
    print("Worst-Of Autocallable (3 assets):")
    
    wo_params = MultiAssetParams(
        S0=np.array([100.0, 100.0, 100.0]),
        principal=10000,
        T=3,
        r=0.05,
        q=np.array([0.02, 0.01, 0.015]),
        sigma=np.array([0.25, 0.30, 0.28]),
        rho=np.array([
            [1.0, 0.6, 0.5],
            [0.6, 1.0, 0.55],
            [0.5, 0.55, 1.0]
        ]),
        autocall_level=1.0,
        coupon_barrier=0.70,
        ki_barrier=0.60,
        coupon_rate=0.12,        # Higher coupon for worst-of
        observation_freq=4,
        step_down=0.025
    )
    
    wo_result = price_worst_of_autocallable(wo_params, n_paths=50000, seed=42)
    
    print(f"\nResults:")
    print(f"  Price: ${wo_result['price']:.2f} ({wo_result['price_pct']:.2f}%)")
    print(f"  Autocall Probability: {wo_result['autocall_prob']*100:.1f}%")
    print(f"  Knock-In Probability: {wo_result['ki_prob']*100:.1f}%")
    print(f"  Average Life: {wo_result['avg_life']:.2f} years")
    
    # Greeks
    print("\n" + "-" * 50)
    print("Greeks (Single Asset):")
    
    greeks = compute_autocallable_greeks(params, n_paths=30000, seed=42)
    print(f"  Delta: {greeks['delta']:.4f} ({greeks['delta_pct']:.2f}% of principal)")
    print(f"  Gamma: {greeks['gamma']:.6f}")
    print(f"  Vega: ${greeks['vega']:.2f} (per 1% vol)")
    print(f"  Rho: ${greeks['rho']:.2f} (per 1% rate)")
