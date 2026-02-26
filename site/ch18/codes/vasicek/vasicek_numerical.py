# ============================================================================
# vasicek/vasicek_numerical.py
# ============================================================================
import numpy as np
from typing import Optional, Tuple, Dict, Any
from .vasicek_base import VasicekParameters, VasicekNumericalError


class VasicekNumerical:
    """Advanced numerical methods for Vasicek model."""
    
    @staticmethod
    def transition_density(
        params: VasicekParameters,
        r_current: float,
        r_future: float,
        dt: float
    ) -> float:
        """
        Calculate the transition probability density function for Vasicek.
        
        The Vasicek process has a Gaussian transition density.
        """
        try:
            # Analytical mean and variance for transition
            mean = params.b + (r_current - params.b) * np.exp(-params.a * dt)
            variance = (params.sigma**2 / (2 * params.a)) * (1 - np.exp(-2 * params.a * dt))
            
            if variance <= 0:
                raise ValueError("Variance must be positive")
            
            # Gaussian density
            density = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-0.5 * (r_future - mean)**2 / variance)
            
            return density
            
        except Exception as e:
            raise VasicekNumericalError(f"Transition density calculation failed: {e}")
    
    @staticmethod
    def calibrate_to_yield_curve(
        yield_curve_maturities: np.ndarray,
        yield_curve_rates: np.ndarray,
        initial_guess: Optional[Dict[str, float]] = None
    ) -> Tuple[VasicekParameters, Dict[str, Any]]:
        """
        Calibrate Vasicek parameters to match an observed yield curve.
        
        Uses optimization to find parameters that best fit the yield curve.
        """
        try:
            from scipy import optimize
        except ImportError:
            raise VasicekNumericalError("scipy required for yield curve calibration")
        
        if len(yield_curve_maturities) != len(yield_curve_rates):
            raise ValueError("Maturities and rates must have same length")
        
        # Set up initial guess
        if initial_guess is None:
            initial_guess = {
                'r0': yield_curve_rates[0],
                'b': np.mean(yield_curve_rates),
                'a': 0.1,
                'sigma': 0.02
            }
        
        def objective_function(params_array):
            """Objective function for optimization."""
            try:
                r0, b, a, sigma = params_array
                
                # Ensure positive parameters where needed
                if a <= 0 or sigma <= 0:
                    return 1e6
                
                # Create temporary parameters
                temp_params = VasicekParameters(
                    r0=r0, b=b, a=a, sigma=sigma, 
                    maturity_time=max(yield_curve_maturities)
                )
                
                # Calculate model yield curve
                from .vasicek_formula import VasicekBondPricer
                model_yields = VasicekBondPricer.yield_curve(temp_params, r0, yield_curve_maturities)
                
                # Calculate sum of squared errors
                return np.sum((model_yields - yield_curve_rates)**2)
                
            except Exception:
                return 1e6
        
        # Set up optimization
        initial_params = [
            initial_guess['r0'],
            initial_guess['b'], 
            initial_guess['a'],
            initial_guess['sigma']
        ]
        
        # Bounds: r0 and b can be negative, a and sigma must be positive
        bounds = [(-0.1, 1.0), (-0.1, 1.0), (1e-6, 5.0), (1e-6, 1.0)]
        
        try:
            # Run optimization
            result = optimize.minimize(
                objective_function,
                initial_params,
                method='L-BFGS-B',
                bounds=bounds
            )
            
            if result.success:
                r0_opt, b_opt, a_opt, sigma_opt = result.x
                
                optimized_params = VasicekParameters(
                    r0=r0_opt,
                    b=b_opt,
                    a=a_opt,
                    sigma=sigma_opt,
                    maturity_time=max(yield_curve_maturities)
                )
                
                optimization_info = {
                    'success': True,
                    'final_error': result.fun,
                    'iterations': result.nit,
                    'message': result.message
                }
                
                return optimized_params, optimization_info
                
            else:
                raise VasicekNumericalError(f"Optimization failed: {result.message}")
                
        except Exception as e:
            raise VasicekNumericalError(f"Calibration failed: {e}")


class VasicekRiskMetrics:
    """Risk metrics and sensitivity analysis for Vasicek model."""
    
    @staticmethod
    def duration(params: VasicekParameters, current_rate: float, maturity: float) -> float:
        """Calculate modified duration of a zero-coupon bond."""
        # For Vasicek, we can calculate this analytically
        if params.a == 0:
            return maturity
        
        B_T = (1 - np.exp(-params.a * maturity)) / params.a
        return B_T
    
    @staticmethod
    def convexity(params: VasicekParameters, current_rate: float, maturity: float) -> float:
        """Calculate convexity of a zero-coupon bond."""
        # Analytical convexity for Vasicek
        if params.a == 0:
            return maturity**2
        
        B_T = (1 - np.exp(-params.a * maturity)) / params.a
        return B_T**2
    
    @staticmethod
    def parameter_sensitivities(
        params: VasicekParameters,
        current_rate: float,
        maturity: float
    ) -> Dict[str, float]:
        """Calculate sensitivities to Vasicek parameters."""
        from .vasicek_formula import VasicekBondPricer
        
        base_price = VasicekBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        sensitivities = {}
        delta = 1e-6
        
        # Sensitivity to a (mean reversion)
        params_a_up = VasicekParameters(
            params.r0, params.b, params.a + delta, params.sigma, params.maturity_time
        )
        price_a_up = VasicekBondPricer.zero_coupon_bond_price(params_a_up, current_rate, maturity)
        sensitivities['a'] = (price_a_up - base_price) / delta
        
        # Sensitivity to b (long-term mean)
        params_b_up = VasicekParameters(
            params.r0, params.b + delta, params.a, params.sigma, params.maturity_time
        )
        price_b_up = VasicekBondPricer.zero_coupon_bond_price(params_b_up, current_rate, maturity)
        sensitivities['b'] = (price_b_up - base_price) / delta
        
        # Sensitivity to sigma
        params_sigma_up = VasicekParameters(
            params.r0, params.b, params.a, params.sigma + delta, params.maturity_time
        )
        price_sigma_up = VasicekBondPricer.zero_coupon_bond_price(params_sigma_up, current_rate, maturity)
        sensitivities['sigma'] = (price_sigma_up - base_price) / delta
        
        return sensitivities