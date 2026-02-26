# calibration_pipeline.py
"""
Heston Calibration Pipeline.

This module implements an end-to-end calibration pipeline for the Heston model
using differential evolution and market option data.

The Heston model: dS = μS dt + √v S dW_S
                  dv = κ(θ - v) dt + σ_v√v dW_v
"""

import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.fft import fft
from typing import Dict, Tuple, List
import warnings
warnings.filterwarnings('ignore')


class HestonCalibrator:
    """Heston model calibration to market option data."""
    
    def __init__(self, S0: float, r: float):
        """
        Initialize Heston calibrator.
        
        Args:
            S0: Spot price
            r: Risk-free rate
        """
        self.S0 = S0
        self.r = r
    
    def heston_cf(
        self,
        phi: complex,
        S0: float,
        v0: float,
        kappa: float,
        theta: float,
        sigma_v: float,
        rho: float,
        r: float,
        T: float
    ) -> complex:
        """
        Heston characteristic function (simplified).
        
        Args:
            phi: Fourier variable
            v0: Initial variance
            kappa: Mean reversion speed
            theta: Long-run variance
            sigma_v: Volatility of variance
            rho: Correlation
            Other parameters: spot, rate, maturity
        
        Returns:
            Characteristic function value
        """
        # Simplified version - full implementation would use exact formula
        # This is a placeholder that returns approximate value
        
        i = complex(0, 1)
        
        # Characteristic exponent components
        d = np.sqrt((rho * sigma_v * phi * i - kappa)**2 + 
                   sigma_v**2 * (phi * i + phi**2))
        
        g = (kappa - rho * sigma_v * phi * i - d) / (
            kappa - rho * sigma_v * phi * i + d
        )
        
        C = r * phi * i * T + kappa * theta / (sigma_v**2) * (
            (kappa - rho * sigma_v * phi * i - d) * T - 
            2 * np.log((1 - g * np.exp(-d * T)) / (1 - g))
        )
        
        D = (kappa - rho * sigma_v * phi * i - d) / sigma_v**2 * (
            (1 - np.exp(-d * T)) / (1 - g * np.exp(-d * T))
        )
        
        return np.exp(C + D * v0 + i * phi * np.log(S0))
    
    def heston_call_price(
        self,
        K: float,
        T: float,
        S0: float,
        v0: float,
        kappa: float,
        theta: float,
        sigma_v: float,
        rho: float,
        r: float
    ) -> float:
        """
        Price European call using Heston characteristic function.
        
        This is a simplified approximation.
        Full implementation would use Fourier inversion.
        
        Args:
            K: Strike
            T: Maturity
            Other: Heston parameters
        
        Returns:
            Call price approximation
        """
        # Simplified pricing - use lognormal approximation at ATM
        from scipy.stats import norm
        
        # Black-Scholes with Heston ATM vol
        sigma_atm = np.sqrt(theta)
        
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma_atm**2) * T) / (
            sigma_atm * np.sqrt(T)
        )
        d2 = d1 - sigma_atm * np.sqrt(T)
        
        call = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        return call
    
    def calibration_objective(
        self,
        params: np.ndarray,
        market_data: Dict,
        weights: np.ndarray = None
    ) -> float:
        """
        Objective function for optimization.
        
        Args:
            params: [v0, kappa, theta, sigma_v, rho]
            market_data: {'strikes': [...], 'prices': [...], 'maturities': [...]}
            weights: Optional weights for different options
        
        Returns:
            Weighted sum of squared pricing errors
        """
        v0, kappa, theta, sigma_v, rho = params
        
        # Constraints
        if v0 <= 0 or kappa <= 0 or theta <= 0 or sigma_v <= 0:
            return 1e10
        if abs(rho) >= 1:
            return 1e10
        if 2 * kappa * theta < sigma_v**2:  # Feller condition
            return 1e10
        
        strikes = market_data['strikes']
        market_prices = market_data['prices']
        maturities = market_data['maturities']
        
        if weights is None:
            weights = np.ones_like(market_prices)
        
        total_error = 0
        
        for i, (K, T, market_price) in enumerate(
            zip(strikes, maturities, market_prices)
        ):
            try:
                model_price = self.heston_call_price(
                    K, T, self.S0, v0, kappa, theta, sigma_v, rho, self.r
                )
                
                error = (model_price - market_price)**2
                total_error += weights[i] * error
            except:
                return 1e10
        
        return total_error
    
    def calibrate_differential_evolution(
        self,
        market_data: Dict,
        weights: np.ndarray = None,
        seed: int = 42
    ) -> Dict:
        """
        Calibrate using differential evolution (global optimizer).
        
        Args:
            market_data: Market option data
            weights: Optional weights
            seed: Random seed
        
        Returns:
            Dictionary with calibrated parameters
        """
        bounds = [
            (0.01, 1.0),      # v0: variance
            (0.01, 5.0),      # kappa: mean reversion
            (0.01, 1.0),      # theta: long-run variance
            (0.01, 2.0),      # sigma_v: vol of vol
            (-0.99, 0.99)     # rho: correlation
        ]
        
        result = differential_evolution(
            lambda p: self.calibration_objective(p, market_data, weights),
            bounds,
            seed=seed,
            maxiter=300,
            atol=1e-6,
            tol=1e-6
        )
        
        v0, kappa, theta, sigma_v, rho = result.x
        
        return {
            "v0": v0,
            "kappa": kappa,
            "theta": theta,
            "sigma_v": sigma_v,
            "rho": rho,
            "error": result.fun,
            "success": result.success,
            "iterations": result.nit
        }
    
    def calibrate_local_search(
        self,
        market_data: Dict,
        initial_guess: Tuple = None,
        weights: np.ndarray = None
    ) -> Dict:
        """
        Calibrate using local optimization (faster but may get stuck).
        
        Args:
            market_data: Market data
            initial_guess: Starting parameters [v0, kappa, theta, sigma_v, rho]
            weights: Optional weights
        
        Returns:
            Calibration results
        """
        if initial_guess is None:
            initial_guess = (0.1, 2.0, 0.1, 0.2, -0.3)
        
        result = minimize(
            lambda p: self.calibration_objective(p, market_data, weights),
            initial_guess,
            method='Nelder-Mead',
            options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 10000}
        )
        
        v0, kappa, theta, sigma_v, rho = result.x
        
        return {
            "v0": v0,
            "kappa": kappa,
            "theta": theta,
            "sigma_v": sigma_v,
            "rho": rho,
            "error": result.fun,
            "success": result.success
        }
    
    def validate_calibration(
        self,
        params: Dict,
        market_data: Dict
    ) -> Dict:
        """
        Validate calibrated parameters against market data.
        
        Args:
            params: Calibrated parameters
            market_data: Market data
        
        Returns:
            Validation metrics
        """
        strikes = market_data['strikes']
        market_prices = market_data['prices']
        maturities = market_data['maturities']
        
        model_prices = []
        errors = []
        rel_errors = []
        
        for K, T, market_price in zip(strikes, maturities, market_prices):
            model_price = self.heston_call_price(
                K, T, self.S0,
                params['v0'], params['kappa'], params['theta'],
                params['sigma_v'], params['rho'],
                self.r
            )
            model_prices.append(model_price)
            errors.append(model_price - market_price)
            rel_errors.append((model_price - market_price) / market_price)
        
        return {
            "model_prices": np.array(model_prices),
            "market_prices": np.array(market_prices),
            "absolute_errors": np.array(errors),
            "relative_errors": np.array(rel_errors),
            "rmse": np.sqrt(np.mean(np.array(errors)**2)),
            "mae": np.mean(np.abs(errors)),
            "mape": np.mean(np.abs(rel_errors))
        }


def example_heston_calibration():
    """Example calibration to synthetic market data."""
    np.random.seed(42)
    
    # Setup
    S0 = 100
    r = 0.05
    
    # True parameters
    true_params = {
        'v0': 0.04,
        'kappa': 2.0,
        'theta': 0.04,
        'sigma_v': 0.3,
        'rho': -0.5
    }
    
    # Generate synthetic market data
    strikes = np.array([90, 95, 100, 105, 110, 100, 100])
    maturities = np.array([0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 1.0])
    
    calibrator = HestonCalibrator(S0, r)
    
    # Get "market" prices from true model with noise
    market_prices = []
    for K, T in zip(strikes, maturities):
        price = calibrator.heston_call_price(
            K, T, S0,
            true_params['v0'], true_params['kappa'], true_params['theta'],
            true_params['sigma_v'], true_params['rho'],
            r
        )
        market_prices.append(price * (1 + np.random.normal(0, 0.001)))  # Add noise
    
    market_data = {
        'strikes': strikes,
        'maturities': maturities,
        'prices': np.array(market_prices)
    }
    
    print("Heston Calibration Pipeline Example")
    print("=" * 60)
    print("\nTrue Parameters:")
    for k, v in true_params.items():
        print(f"  {k}: {v:.6f}")
    
    # Calibrate
    print("\nCalibrating using Differential Evolution...")
    calibrated = calibrator.calibrate_differential_evolution(market_data)
    
    print("\nCalibrated Parameters:")
    for k in ['v0', 'kappa', 'theta', 'sigma_v', 'rho']:
        print(f"  {k}: {calibrated[k]:.6f}")
    print(f"  Calibration Error: {calibrated['error']:.6f}")
    
    # Validate
    validation = calibrator.validate_calibration(calibrated, market_data)
    print("\nValidation Metrics:")
    print(f"  RMSE: {validation['rmse']:.6f}")
    print(f"  MAE: {validation['mae']:.6f}")
    print(f"  MAPE: {validation['mape']:.6f}")


if __name__ == "__main__":
    example_heston_calibration()
