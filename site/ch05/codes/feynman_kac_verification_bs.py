# feynman_kac_verification_bs.py
"""
Feynman-Kac Verification for Black-Scholes PDE.

This module verifies the Feynman-Kac formula by comparing the Monte Carlo 
expectation from the risk-neutral diffusion with the analytical Black-Scholes 
solution for European option pricing.

The Feynman-Kac theorem states that the solution to a parabolic PDE:
    ∂u/∂t + Lₓu + c(x,t)u = 0
can be represented as:
    u(x,t) = E^Q[e^{-∫ᵗᵀ c(s) ds} g(X_T) | X_t = x]

where L is the infinitesimal generator and g is the terminal payoff.
"""

import numpy as np
from scipy.stats import norm
from typing import Tuple, Callable


def black_scholes_call(
    S: float, K: float, T: float, r: float, sigma: float
) -> float:
    """
    Compute Black-Scholes call option price using analytical formula.
    
    Args:
        S: Current spot price
        K: Strike price
        T: Time to maturity (years)
        r: Risk-free rate
        sigma: Volatility (annualized)
    
    Returns:
        Call option price
    """
    if T <= 0:
        return max(S - K, 0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


def black_scholes_put(
    S: float, K: float, T: float, r: float, sigma: float
) -> float:
    """
    Compute Black-Scholes put option price using analytical formula.
    
    Args:
        S: Current spot price
        K: Strike price
        T: Time to maturity (years)
        r: Risk-free rate
        sigma: Volatility (annualized)
    
    Returns:
        Put option price
    """
    if T <= 0:
        return max(K - S, 0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price


def monte_carlo_option_price(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    payoff_fn: Callable,
    num_paths: int = 10000,
    num_steps: int = 100,
    seed: int = None
) -> Tuple[float, float]:
    """
    Price a European option using Monte Carlo simulation under risk-neutral measure.
    
    Args:
        S0: Initial spot price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        sigma: Volatility
        payoff_fn: Function computing payoff at maturity (e.g., lambda S: max(S - K, 0))
        num_paths: Number of Monte Carlo paths
        num_steps: Number of time steps per path
        seed: Random seed for reproducibility
    
    Returns:
        Tuple of (option_price, standard_error)
    """
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / num_steps
    # Generate random increments for geometric Brownian motion
    dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_steps))
    
    # Simulate paths under risk-neutral measure
    S_paths = np.zeros((num_paths, num_steps + 1))
    S_paths[:, 0] = S0
    
    for i in range(num_steps):
        # Euler-Maruyama: dS = r*S*dt + sigma*S*dW
        S_paths[:, i + 1] = S_paths[:, i] * np.exp(
            (r - 0.5 * sigma**2) * dt + sigma * dW[:, i]
        )
    
    # Compute payoffs at maturity
    terminal_payoffs = np.array([payoff_fn(S) for S in S_paths[:, -1]])
    
    # Discount back to present value
    discounted_payoffs = terminal_payoffs * np.exp(-r * T)
    
    # Compute price and standard error
    price = np.mean(discounted_payoffs)
    std_error = np.std(discounted_payoffs) / np.sqrt(num_paths)
    
    return price, std_error


def verify_feynman_kac(
    S0: float = 100.0,
    K: float = 100.0,
    T: float = 1.0,
    r: float = 0.05,
    sigma: float = 0.20,
    num_paths: int = 100000,
    seed: int = 42
) -> dict:
    """
    Verify Feynman-Kac formula by comparing MC and analytical BS prices.
    
    Args:
        S0: Initial spot price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        sigma: Volatility
        num_paths: Number of Monte Carlo paths
        seed: Random seed
    
    Returns:
        Dictionary with analytical and MC prices, errors, and statistics
    """
    # Analytical Black-Scholes prices
    bs_call = black_scholes_call(S0, K, T, r, sigma)
    bs_put = black_scholes_put(S0, K, T, r, sigma)
    
    # Monte Carlo prices
    mc_call, mc_call_se = monte_carlo_option_price(
        S0, K, T, r, sigma,
        payoff_fn=lambda S: max(S - K, 0),
        num_paths=num_paths,
        seed=seed
    )
    
    mc_put, mc_put_se = monte_carlo_option_price(
        S0, K, T, r, sigma,
        payoff_fn=lambda S: max(K - S, 0),
        num_paths=num_paths,
        seed=seed + 1
    )
    
    return {
        "call": {
            "analytical": bs_call,
            "mc_estimate": mc_call,
            "mc_std_error": mc_call_se,
            "absolute_error": abs(bs_call - mc_call),
            "relative_error": abs(bs_call - mc_call) / bs_call if bs_call != 0 else 0
        },
        "put": {
            "analytical": bs_put,
            "mc_estimate": mc_put,
            "mc_std_error": mc_put_se,
            "absolute_error": abs(bs_put - mc_put),
            "relative_error": abs(bs_put - mc_put) / bs_put if bs_put != 0 else 0
        },
        "parameters": {
            "S0": S0,
            "K": K,
            "T": T,
            "r": r,
            "sigma": sigma,
            "num_paths": num_paths
        }
    }


if __name__ == "__main__":
    # Run verification
    results = verify_feynman_kac()
    print("Feynman-Kac Formula Verification for Black-Scholes PDE")
    print("=" * 60)
    print(f"\nCall Option:")
    print(f"  Analytical BS:  {results['call']['analytical']:.6f}")
    print(f"  MC Estimate:    {results['call']['mc_estimate']:.6f} (SE: {results['call']['mc_std_error']:.6f})")
    print(f"  Absolute Error: {results['call']['absolute_error']:.6f}")
    print(f"  Relative Error: {results['call']['relative_error']:.2%}")
    
    print(f"\nPut Option:")
    print(f"  Analytical BS:  {results['put']['analytical']:.6f}")
    print(f"  MC Estimate:    {results['put']['mc_estimate']:.6f} (SE: {results['put']['mc_std_error']:.6f})")
    print(f"  Absolute Error: {results['put']['absolute_error']:.6f}")
    print(f"  Relative Error: {results['put']['relative_error']:.2%}")
