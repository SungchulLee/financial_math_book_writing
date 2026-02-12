# variance_swaps_and_model_free_volatility.py
"""
Variance Swaps and Model-Free Volatility (placeholder implementation).

This module provides foundational variance swap valuation and model-free
implied volatility computation from option surfaces.

Note: Full implementation would include numerical integration and
       optimization for model-free calibration.
"""

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
from typing import Dict, Tuple


class VarianceSwapCalculator:
    """Compute variance swap fair strike and implied vol from option prices."""
    
    def __init__(self, S0: float, r: float, T: float):
        """
        Initialize variance swap calculator.
        
        Args:
            S0: Spot price
            r: Risk-free rate
            T: Maturity
        """
        self.S0 = S0
        self.r = r
        self.T = T
        self.forward = S0 * np.exp(r * T)
    
    def variance_swap_fair_strike(
        self,
        strikes: np.ndarray,
        call_prices: np.ndarray,
        put_prices: np.ndarray
    ) -> float:
        """
        Compute variance swap fair strike using Demeterfi et al. formula.
        
        Fair variance = (2/T) * ∫[0,∞] (C(K) + P(K))/K² dK - (1/T)*ln²(F/S0)
        
        Args:
            strikes: Array of strike prices
            call_prices: Array of call prices at each strike
            put_prices: Array of put prices at each strike
        
        Returns:
            Fair variance strike (annualized)
        """
        # Combine call and put into single option price function
        # Use put for ITM, call for OTM
        option_prices = np.where(strikes < self.forward, put_prices, call_prices)
        
        # Numerical integration: ∫ (C+P)/K² dK
        integrand = option_prices / (strikes**2)
        
        # Trapezoid rule integration
        integral = np.trapz(integrand, strikes)
        
        # Add contribution from K=0 (usually small)
        var_integral = (2.0 / self.T) * integral
        
        # Subtract (1/T)*ln²(F/S0)
        log_term = (1.0 / self.T) * np.log(self.forward / self.S0)**2
        
        fair_variance = var_integral - log_term
        return fair_variance
    
    def vix_formula(
        self,
        strikes: np.ndarray,
        call_prices: np.ndarray,
        put_prices: np.ndarray,
        K0: float = None
    ) -> float:
        """
        Compute VIX index (model-free implied volatility).
        
        VIX² = (2/T) * ∫ (C(K) + P(K))/K² dK - (1/T)*[ln(F/K0)]²
        
        Args:
            strikes: Array of strikes
            call_prices: Call prices
            put_prices: Put prices
            K0: Reference strike (default: nearest to forward)
        
        Returns:
            VIX index (in percent, typically 30 means 30% annualized vol)
        """
        if K0 is None:
            # Use strike closest to forward
            K0 = strikes[np.argmin(np.abs(strikes - self.forward))]
        
        # Use put-call spread for robustness
        option_prices = np.where(strikes < self.forward, put_prices, call_prices)
        integrand = option_prices / (strikes**2)
        integral = np.trapz(integrand, strikes)
        
        var_integral = (2.0 / self.T) * integral
        log_term = (1.0 / self.T) * np.log(self.forward / K0)**2
        
        variance = var_integral - log_term
        vix = 100 * np.sqrt(np.maximum(variance, 0))  # Percentage
        return vix
    
    def variance_term_structure(
        self,
        maturities: np.ndarray,
        strikes_dict: Dict,
        calls_dict: Dict,
        puts_dict: Dict
    ) -> np.ndarray:
        """
        Compute variance (and thus volatility) across different maturities.
        
        Args:
            maturities: Array of maturities (in years)
            strikes_dict: Dictionary mapping maturity to strikes
            calls_dict: Dictionary mapping maturity to call prices
            puts_dict: Dictionary mapping maturity to put prices
        
        Returns:
            Array of fair variances at each maturity
        """
        variances = []
        
        for T in maturities:
            # Create temporary calculator for this maturity
            calc_T = VarianceSwapCalculator(self.S0, self.r, T)
            
            strikes = strikes_dict[T]
            calls = calls_dict[T]
            puts = puts_dict[T]
            
            var = calc_T.variance_swap_fair_strike(strikes, calls, puts)
            variances.append(var)
        
        return np.array(variances)
    
    def implied_vol_from_variance(self, variance: float) -> float:
        """Convert variance to annualized volatility."""
        return np.sqrt(variance)
    
    def variance_skew_sensitivity(
        self,
        strikes: np.ndarray,
        call_prices: np.ndarray,
        put_prices: np.ndarray
    ) -> Dict[str, float]:
        """
        Analyze sensitivity of variance to skew (OTM vs ATM prices).
        
        Returns:
            Dictionary with skew metrics
        """
        # Find ATM strike
        atm_idx = np.argmin(np.abs(strikes - self.forward))
        
        # OTM put integral (below forward)
        put_idx = strikes < self.forward
        put_integral = np.trapz(
            put_prices[put_idx] / (strikes[put_idx]**2),
            strikes[put_idx]
        )
        
        # OTM call integral (above forward)
        call_idx = strikes >= self.forward
        call_integral = np.trapz(
            call_prices[call_idx] / (strikes[call_idx]**2),
            strikes[call_idx]
        )
        
        return {
            "put_contribution": (2.0 / self.T) * put_integral,
            "call_contribution": (2.0 / self.T) * call_integral,
            "total_variance": (2.0 / self.T) * (put_integral + call_integral),
            "put_call_ratio": put_integral / call_integral if call_integral > 0 else np.inf
        }


def example_variance_swap():
    """Example computation of variance swap strike."""
    # Simple example: uniform option prices (constant surface)
    S0 = 100
    r = 0.05
    T = 1.0
    
    strikes = np.linspace(70, 130, 31)
    
    # Simple model: ATM volatility 20%, flat surface
    sigma_atm = 0.20
    from scipy.stats import norm
    
    # Approximate option prices (simplified BS)
    call_prices = np.array([
        max(S0 - K, 0) if K < S0 else 5 * (S0 - K) ** (-0.5)
        for K in strikes
    ])
    put_prices = np.array([
        max(K - S0, 0) if K > S0 else 5 * (K - S0) ** (-0.5)
        for K in strikes
    ])
    
    calc = VarianceSwapCalculator(S0, r, T)
    
    fair_var = calc.variance_swap_fair_strike(strikes, call_prices, put_prices)
    vix = calc.vix_formula(strikes, call_prices, put_prices)
    
    print("Variance Swap and Model-Free Volatility Example")
    print("=" * 60)
    print(f"Fair Variance Strike: {fair_var:.6f}")
    print(f"Fair Volatility Strike: {np.sqrt(fair_var):.4f} ({100*np.sqrt(fair_var):.2f}%)")
    print(f"VIX (Model-Free Implied Vol): {vix:.2f}")


if __name__ == "__main__":
    example_variance_swap()
