# python_implementation.py
"""
SABR Model Python Implementation.

This module implements the SABR model (Stochastic Alpha Beta Rho) for
equity and rate options, including Hagan's closed-form volatility
approximation, calibration, and Monte Carlo simulation.

SABR Model: dF = α(F)^β dW_F
           dα = να dW_α, ⟨dW_F, dW_α⟩ = ρ dt
"""

import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm
from typing import Tuple, Dict


class SABRModel:
    """SABR option pricing model."""
    
    def __init__(self, F: float, beta: float = 0.5):
        """
        Initialize SABR model.
        
        Args:
            F: Forward price
            beta: CEV exponent (0.5 = lognormal, 1.0 = normal)
        """
        self.F = F
        self.beta = beta
    
    def _hagan_implied_vol(
        self,
        K: float,
        T: float,
        alpha: float,
        rho: float,
        nu: float
    ) -> float:
        """
        Compute implied volatility using Hagan's approximation formula.
        
        This is a closed-form approximation for SABR implied volatility.
        
        Args:
            K: Strike
            T: Time to maturity
            alpha: Volatility of forward (α parameter)
            rho: Correlation between F and α (ρ parameter)
            nu: Volatility of volatility (ν parameter)
        
        Returns:
            Implied volatility (annualized)
        """
        F = self.F
        beta = self.beta
        
        if abs(F - K) < 1e-8:  # ATM case
            numerator = alpha * (1 + ((2 - 3 * rho**2) / 24) * nu**2 * T)
            denominator = F**(1 - beta)
            
            atm_vol = numerator / denominator
            
            # Second-order correction
            correction = 1 + (beta**2 / 24) * np.log(F / K)**2
            correction += (rho * beta * nu / 4) * np.log(F / K)
            correction += ((2 - 3 * rho**2) * nu**2 / 24)
            
            return atm_vol * correction
        
        else:  # OTM case
            # Log-moneyness
            z = (nu / alpha) * (F**(1 - beta) - K**(1 - beta)) / (1 - beta)
            
            x = np.log((np.sqrt(1 - 2 * rho * z + z**2) + z - rho) / (1 - rho))
            
            # Numerator
            numerator = alpha / (F**(1 - beta) - K**(1 - beta))
            
            # Main term
            main_term = z / x
            
            # Correction factors
            f1 = (beta**2 / 24) * np.log(F / K)**2
            f2 = (rho * beta * nu / 4) * np.log(F / K)
            f3 = ((2 - 3 * rho**2) * nu**2 / 24) * T
            
            denominator = 1 + f1 + f2 + f3
            
            return numerator * main_term * denominator
    
    def call_price_hagan(
        self,
        K: float,
        T: float,
        r: float,
        alpha: float,
        rho: float,
        nu: float
    ) -> float:
        """
        Price call option using Hagan formula and Black formula.
        
        Args:
            K: Strike
            T: Maturity
            r: Discount rate
            alpha, rho, nu: SABR parameters
        
        Returns:
            Call option price
        """
        # Get implied volatility from Hagan formula
        sigma_impl = self._hagan_implied_vol(K, T, alpha, rho, nu)
        
        # Use Black's formula for pricing (for forward contracts)
        F = self.F
        df = np.exp(-r * T)  # Discount factor
        
        d1 = (np.log(F / K) + (sigma_impl**2 / 2) * T) / (sigma_impl * np.sqrt(T))
        d2 = d1 - sigma_impl * np.sqrt(T)
        
        call = df * (F * norm.cdf(d1) - K * norm.cdf(d2))
        return call
    
    def put_price_hagan(
        self,
        K: float,
        T: float,
        r: float,
        alpha: float,
        rho: float,
        nu: float
    ) -> float:
        """Price put option using Hagan formula."""
        F = self.F
        df = np.exp(-r * T)
        
        sigma_impl = self._hagan_implied_vol(K, T, alpha, rho, nu)
        
        d1 = (np.log(F / K) + (sigma_impl**2 / 2) * T) / (sigma_impl * np.sqrt(T))
        d2 = d1 - sigma_impl * np.sqrt(T)
        
        put = df * (K * norm.cdf(-d2) - F * norm.cdf(-d1))
        return put
    
    def simulate_paths(
        self,
        T: float,
        alpha: float,
        rho: float,
        nu: float,
        num_paths: int = 1000,
        num_steps: int = 100,
        seed: int = None
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Simulate SABR model paths using Euler discretization.
        
        Args:
            T: Maturity
            alpha, rho, nu: SABR parameters
            num_paths: Number of simulation paths
            num_steps: Time steps per path
            seed: Random seed
        
        Returns:
            Tuple of (F_paths, alpha_paths)
        """
        if seed is not None:
            np.random.seed(seed)
        
        dt = T / num_steps
        F_paths = np.zeros((num_paths, num_steps + 1))
        alpha_paths = np.zeros((num_paths, num_steps + 1))
        
        F_paths[:, 0] = self.F
        alpha_paths[:, 0] = alpha
        
        for i in range(num_steps):
            # Correlated normal increments
            Z1 = np.random.standard_normal(num_paths)
            Z2 = np.random.standard_normal(num_paths)
            
            # Maintain correlation ρ
            W_alpha = Z2
            W_F = rho * Z2 + np.sqrt(1 - rho**2) * Z1
            
            # Euler step for F and α
            F_t = F_paths[:, i]
            alpha_t = alpha_paths[:, i]
            
            dF = alpha_t * (F_t**self.beta) * W_F * np.sqrt(dt)
            dalpha = nu * alpha_t * W_alpha * np.sqrt(dt)
            
            F_paths[:, i + 1] = np.maximum(F_t + dF, 1e-6)
            alpha_paths[:, i + 1] = np.maximum(alpha_t + dalpha, 1e-6)
        
        return F_paths, alpha_paths
    
    def price_monte_carlo(
        self,
        K: float,
        T: float,
        r: float,
        alpha: float,
        rho: float,
        nu: float,
        option_type: str = "call",
        num_paths: int = 10000,
        seed: int = None
    ) -> Tuple[float, float]:
        """
        Price option using Monte Carlo simulation.
        
        Args:
            K: Strike
            T: Maturity
            r: Discount rate
            alpha, rho, nu: SABR parameters
            option_type: "call" or "put"
            num_paths: Number of paths
            seed: Random seed
        
        Returns:
            Tuple of (price, standard_error)
        """
        F_paths, _ = self.simulate_paths(
            T, alpha, rho, nu, num_paths, seed=seed
        )
        
        if option_type == "call":
            payoffs = np.maximum(F_paths[:, -1] - K, 0)
        else:
            payoffs = np.maximum(K - F_paths[:, -1], 0)
        
        df = np.exp(-r * T)
        discounted_payoffs = payoffs * df
        
        price = np.mean(discounted_payoffs)
        std_error = np.std(discounted_payoffs) / np.sqrt(num_paths)
        
        return price, std_error


def calibrate_sabr(
    F: float,
    T: float,
    market_prices: Dict[float, Tuple[float, float]],  # {K: (bid, ask)}
    r: float = 0.05,
    beta: float = 0.5,
    initial_guess: Tuple = None
) -> Dict:
    """
    Calibrate SABR model to market option prices.
    
    Args:
        F: Forward price
        T: Maturity
        market_prices: Dictionary mapping strike to (bid, ask) prices
        r: Discount rate
        beta: CEV exponent (fixed)
        initial_guess: Initial (alpha, rho, nu) for optimization
    
    Returns:
        Dictionary with calibrated parameters and error metrics
    """
    if initial_guess is None:
        initial_guess = (0.2, 0.0, 0.5)
    
    model = SABRModel(F, beta)
    
    def objective(params):
        alpha, rho, nu = params
        
        # Constraints
        if alpha <= 0 or nu <= 0:
            return 1e10
        if abs(rho) >= 1:
            return 1e10
        
        total_error = 0
        
        for K, (bid, ask) in market_prices.items():
            # Use mid-price
            mid = (bid + ask) / 2
            
            # Get model price
            model_price = model.call_price_hagan(K, T, r, alpha, rho, nu)
            
            # Squared error
            error = (model_price - mid)**2
            total_error += error
        
        return total_error
    
    # Optimize
    result = minimize(
        objective,
        initial_guess,
        method='Nelder-Mead',
        options={'xatol': 1e-6, 'fatol': 1e-6}
    )
    
    alpha_opt, rho_opt, nu_opt = result.x
    
    return {
        "alpha": alpha_opt,
        "rho": rho_opt,
        "nu": nu_opt,
        "beta": beta,
        "error": result.fun,
        "success": result.success
    }


def example_sabr():
    """Example SABR pricing and calibration."""
    model = SABRModel(F=100, beta=0.5)
    
    print("SABR Model Example")
    print("=" * 60)
    
    # Parameters
    alpha, rho, nu = 0.2, -0.3, 0.4
    T, r = 1.0, 0.05
    
    # Price calls at different strikes
    strikes = [90, 95, 100, 105, 110]
    print(f"\nCall prices (α={alpha}, ρ={rho}, ν={nu}):")
    print(f"{'Strike':<10} {'Hagan':<15} {'MC Price':<15}")
    print("-" * 40)
    
    for K in strikes:
        price_hagan = model.call_price_hagan(K, T, r, alpha, rho, nu)
        price_mc, _ = model.price_monte_carlo(K, T, r, alpha, rho, nu, "call")
        print(f"{K:<10.1f} {price_hagan:<15.6f} {price_mc:<15.6f}")


if __name__ == "__main__":
    example_sabr()
