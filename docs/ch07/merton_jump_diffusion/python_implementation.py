# python_implementation.py
"""
Merton Jump-Diffusion Model Implementation.

This module implements the Merton jump-diffusion model for asset pricing,
which extends the Black-Scholes model by adding random jumps to capture
discontinuous price movements and fat tails in return distributions.

Model: dS_t = μS_t dt + σS_t dB_t + S_t dJ_t
where J_t is a compound Poisson jump process.
"""

import numpy as np
from scipy.special import factorial
from scipy.stats import poisson, norm
from typing import Tuple, List


class MertonJumpDiffusion:
    """Merton jump-diffusion model for option pricing."""
    
    def __init__(
        self,
        S0: float,
        r: float,
        sigma: float,
        lambda_jump: float,
        mu_jump: float,
        sigma_jump: float
    ):
        """
        Initialize Merton jump-diffusion parameters.
        
        Args:
            S0: Initial spot price
            r: Risk-free rate
            sigma: Volatility of continuous component
            lambda_jump: Jump intensity (expected number of jumps per year)
            mu_jump: Mean of jump size (log-normal, 0 means no jump)
            sigma_jump: Standard deviation of log jump size
        """
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.lambda_jump = lambda_jump
        self.mu_jump = mu_jump
        self.sigma_jump = sigma_jump
        
        # Adjust drift for jump risk
        self.mu_adjusted = self._compute_adjusted_drift()
    
    def _compute_adjusted_drift(self) -> float:
        """
        Compute drift adjustment for jump component.
        
        The expected return must be r (risk-free rate) under risk-neutral measure.
        Adjustment accounts for expected jump impact: E[e^(μ_j + σ_j*Z) - 1]
        """
        jump_adjustment = self.lambda_jump * (
            np.exp(self.mu_jump + 0.5 * self.sigma_jump**2) - 1
        )
        return self.r - jump_adjustment
    
    def simulate_paths(
        self,
        T: float,
        num_paths: int = 10000,
        num_steps: int = 100,
        seed: int = None
    ) -> np.ndarray:
        """
        Simulate asset price paths under Merton jump-diffusion.
        
        Args:
            T: Time to maturity
            num_paths: Number of simulation paths
            num_steps: Number of time steps
            seed: Random seed
        
        Returns:
            Array of shape (num_paths, num_steps + 1) with simulated prices
        """
        if seed is not None:
            np.random.seed(seed)
        
        dt = T / num_steps
        S_paths = np.zeros((num_paths, num_steps + 1))
        S_paths[:, 0] = self.S0
        
        for i in range(num_steps):
            # Brownian motion increment
            dB = np.random.normal(0, np.sqrt(dt), num_paths)
            
            # Jump component: Poisson number of jumps
            num_jumps = np.random.poisson(self.lambda_jump * dt, num_paths)
            
            # Jump sizes (log-normal)
            jump_effect = np.ones(num_paths)
            for j in range(num_paths):
                if num_jumps[j] > 0:
                    # Each jump multiplies price by e^(μ_j + σ_j*Z)
                    log_jumps = np.random.normal(
                        self.mu_jump,
                        self.sigma_jump,
                        num_jumps[j]
                    )
                    jump_effect[j] = np.exp(np.sum(log_jumps))
            
            # Update price: S_{t+dt} = S_t * e^(drift*dt + sigma*dB) * jump_effect
            S_paths[:, i + 1] = (
                S_paths[:, i] *
                np.exp((self.mu_adjusted - 0.5 * self.sigma**2) * dt + self.sigma * dB) *
                jump_effect
            )
        
        return S_paths
    
    def option_price_monte_carlo(
        self,
        K: float,
        T: float,
        option_type: str = "call",
        num_paths: int = 10000,
        seed: int = None
    ) -> Tuple[float, float]:
        """
        Price European option using Monte Carlo simulation.
        
        Args:
            K: Strike price
            T: Time to maturity
            option_type: "call" or "put"
            num_paths: Number of simulation paths
            seed: Random seed
        
        Returns:
            Tuple of (option_price, standard_error)
        """
        paths = self.simulate_paths(T, num_paths, seed=seed)
        
        if option_type == "call":
            payoffs = np.maximum(paths[:, -1] - K, 0)
        elif option_type == "put":
            payoffs = np.maximum(K - paths[:, -1], 0)
        else:
            raise ValueError(f"Unknown option type: {option_type}")
        
        discounted_payoffs = payoffs * np.exp(-self.r * T)
        price = np.mean(discounted_payoffs)
        std_error = np.std(discounted_payoffs) / np.sqrt(num_paths)
        
        return price, std_error
    
    def option_price_series(
        self,
        K: float,
        T: float,
        option_type: str = "call",
        max_jumps: int = 10,
        tolerance: float = 1e-10
    ) -> float:
        """
        Price European option using Merton's series formula.
        
        The idea: condition on number of jumps n, then use Black-Scholes
        for each component weighted by Poisson probability.
        
        Args:
            K: Strike price
            T: Time to maturity
            option_type: "call" or "put"
            max_jumps: Maximum number of jumps to include in series
            tolerance: Convergence tolerance
        
        Returns:
            Option price (series approximation)
        """
        from scipy.special import factorial
        
        price = 0.0
        
        for n in range(max_jumps + 1):
            # Probability of exactly n jumps
            prob_n_jumps = poisson.pmf(n, self.lambda_jump * T)
            
            if prob_n_jumps < tolerance:
                break
            
            # Volatility conditional on n jumps
            if n == 0:
                sigma_n = self.sigma
            else:
                # Variance from Brownian + n independent jump sizes
                var_jumps = n * (self.sigma_jump**2 + self.mu_jump**2)
                sigma_n = np.sqrt(self.sigma**2 + var_jumps / T)
            
            # Forward adjusted for expected jump impact
            S_n = self.S0 * np.exp(
                self.mu_adjusted * T + n * (self.mu_jump + 0.5 * self.sigma_jump**2)
            )
            
            # Black-Scholes price with adjusted parameters
            if option_type == "call":
                d1 = (np.log(S_n / K) + (self.r + 0.5 * sigma_n**2) * T) / (sigma_n * np.sqrt(T))
                d2 = d1 - sigma_n * np.sqrt(T)
                option_n = S_n * norm.cdf(d1) - K * np.exp(-self.r * T) * norm.cdf(d2)
            else:  # put
                d1 = (np.log(S_n / K) + (self.r + 0.5 * sigma_n**2) * T) / (sigma_n * np.sqrt(T))
                d2 = d1 - sigma_n * np.sqrt(T)
                option_n = K * np.exp(-self.r * T) * norm.cdf(-d2) - S_n * norm.cdf(-d1)
            
            # Add weighted component
            price += prob_n_jumps * option_n
        
        return price


def compare_bs_merton(
    S0: float = 100,
    K: float = 100,
    T: float = 1.0,
    r: float = 0.05,
    sigma: float = 0.2,
    lambda_jump: float = 0.5,
    mu_jump: float = -0.1,
    sigma_jump: float = 0.3
) -> dict:
    """
    Compare Black-Scholes and Merton jump-diffusion prices.
    
    Args:
        S0: Initial spot price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        sigma: Volatility
        lambda_jump: Jump intensity
        mu_jump: Mean log-jump size
        sigma_jump: Standard deviation of log-jump size
    
    Returns:
        Dictionary with pricing results
    """
    from scipy.stats import norm
    
    # Black-Scholes price
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    bs_call = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    bs_put = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    
    # Merton prices
    merton = MertonJumpDiffusion(S0, r, sigma, lambda_jump, mu_jump, sigma_jump)
    merton_call_series = merton.option_price_series(K, T, "call")
    merton_put_series = merton.option_price_series(K, T, "put")
    merton_call_mc, _ = merton.option_price_monte_carlo(K, T, "call", num_paths=50000)
    merton_put_mc, _ = merton.option_price_monte_carlo(K, T, "put", num_paths=50000)
    
    return {
        "black_scholes": {"call": bs_call, "put": bs_put},
        "merton_series": {"call": merton_call_series, "put": merton_put_series},
        "merton_mc": {"call": merton_call_mc, "put": merton_put_mc},
        "difference_series": {
            "call": merton_call_series - bs_call,
            "put": merton_put_series - bs_put
        }
    }


if __name__ == "__main__":
    results = compare_bs_merton()
    print("Merton Jump-Diffusion vs Black-Scholes Pricing")
    print("=" * 60)
    print(f"\nCall Option:")
    print(f"  Black-Scholes:    {results['black_scholes']['call']:.6f}")
    print(f"  Merton (Series):  {results['merton_series']['call']:.6f}")
    print(f"  Merton (MC):      {results['merton_mc']['call']:.6f}")
    print(f"  Difference:       {results['difference_series']['call']:.6f}")
    
    print(f"\nPut Option:")
    print(f"  Black-Scholes:    {results['black_scholes']['put']:.6f}")
    print(f"  Merton (Series):  {results['merton_series']['put']:.6f}")
    print(f"  Merton (MC):      {results['merton_mc']['put']:.6f}")
    print(f"  Difference:       {results['difference_series']['put']:.6f}")
