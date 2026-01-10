# ============================================================================
# cir/cir_numerical.py
# ============================================================================
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
from typing import Optional, Tuple, Dict, Any
from .cir_base import CIRParameters, CIRNumericalError


class CIRNumerical:
    """Advanced numerical methods for CIR model."""
    
    @staticmethod
    def transition_density(
        params: CIRParameters,
        r_current: float,
        r_future: float,
        dt: float
    ) -> float:
        """
        Calculate the transition probability density function for CIR.
        
        The CIR process has a known transition density involving
        the non-central chi-squared distribution.
        """
        try:
            c = 2 * params.kappa / (params.sigma**2 * (1 - np.exp(-params.kappa * dt)))
            q = 2 * params.kappa * params.theta / params.sigma**2 - 1
            
            nc = c * r_current * np.exp(-params.kappa * dt)  # non-centrality parameter
            x = c * r_future
            
            # Use non-central chi-squared density
            return c * stats.ncx2.pdf(x, df=2*(q+1), nc=nc)
            
        except Exception as e:
            raise CIRNumericalError(f"Transition density calculation failed: {e}")
    
    @staticmethod
    def exact_simulation_step(
        params: CIRParameters,
        r_current: float,
        dt: float,
        random_state: Optional[np.random.RandomState] = None
    ) -> float:
        """
        Exact simulation of one CIR step using non-central chi-squared distribution.
        
        This is the theoretically correct way to simulate CIR, but requires
        sampling from non-central chi-squared distribution.
        """
        if random_state is None:
            random_state = np.random.RandomState()
        
        try:
            # Parameters for the exact distribution
            c = 2 * params.kappa / (params.sigma**2 * (1 - np.exp(-params.kappa * dt)))
            q = 2 * params.kappa * params.theta / params.sigma**2 - 1
            nc = c * r_current * np.exp(-params.kappa * dt)
            
            # Sample from non-central chi-squared
            chi_squared_sample = stats.ncx2.rvs(df=2*(q+1), nc=nc, random_state=random_state)
            
            return chi_squared_sample / c
            
        except Exception as e:
            raise CIRNumericalError(f"Exact simulation step failed: {e}")
    
    @staticmethod
    def calibrate_to_yield_curve(
        yield_curve_maturities: np.ndarray,
        yield_curve_rates: np.ndarray,
        initial_guess: Optional[Dict[str, float]] = None
    ) -> Tuple[CIRParameters, Dict[str, Any]]:
        """
        Calibrate CIR parameters to match an observed yield curve.
        
        Uses optimization to find parameters that best fit the yield curve.
        """
        if len(yield_curve_maturities) != len(yield_curve_rates):
            raise ValueError("Maturities and rates must have same length")
        
        # Set up initial guess
        if initial_guess is None:
            initial_guess = {
                'r0': yield_curve_rates[0],
                'theta': np.mean(yield_curve_rates),
                'kappa': 0.1,
                'sigma': 0.03
            }
        
        def objective_function(params_array):
            """Objective function for optimization."""
            try:
                r0, theta, kappa, sigma = params_array
                
                # Ensure positive parameters
                if any(p <= 0 for p in [r0, theta, kappa, sigma]):
                    return 1e6
                
                # Create temporary parameters
                temp_params = CIRParameters(
                    r0=r0, theta=theta, kappa=kappa, sigma=sigma, maturity_time=max(yield_curve_maturities)
                )
                
                # Calculate model yield curve
                from .cir_formula import CIRBondPricer
                model_yields = CIRBondPricer.yield_curve(temp_params, r0, yield_curve_maturities)
                
                # Calculate sum of squared errors
                return np.sum((model_yields - yield_curve_rates)**2)
                
            except Exception:
                return 1e6
        
        # Set up optimization
        initial_params = [
            initial_guess['r0'],
            initial_guess['theta'], 
            initial_guess['kappa'],
            initial_guess['sigma']
        ]
        
        # Bounds to ensure positive parameters
        bounds = [(1e-6, 1.0), (1e-6, 1.0), (1e-6, 5.0), (1e-6, 1.0)]
        
        try:
            # Run optimization
            result = opt.minimize(
                objective_function,
                initial_params,
                method='L-BFGS-B',
                bounds=bounds
            )
            
            if result.success:
                r0_opt, theta_opt, kappa_opt, sigma_opt = result.x
                
                optimized_params = CIRParameters(
                    r0=r0_opt,
                    theta=theta_opt,
                    kappa=kappa_opt,
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
                raise CIRNumericalError(f"Optimization failed: {result.message}")
                
        except Exception as e:
            raise CIRNumericalError(f"Calibration failed: {e}")


class CIRRiskMetrics:
    """Risk metrics and sensitivity analysis for CIR model."""
    
    @staticmethod
    def duration(params: CIRParameters, current_rate: float, maturity: float) -> float:
        """Calculate modified duration of a zero-coupon bond."""
        # Numerical derivative of bond price with respect to rate
        dr = 1e-6
        
        from .cir_formula import CIRBondPricer
        
        price_up = CIRBondPricer.zero_coupon_bond_price(params, current_rate + dr, maturity)
        price_down = CIRBondPricer.zero_coupon_bond_price(params, current_rate - dr, maturity)
        price_base = CIRBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        return -(price_up - price_down) / (2 * dr * price_base)
    
    @staticmethod
    def convexity(params: CIRParameters, current_rate: float, maturity: float) -> float:
        """Calculate convexity of a zero-coupon bond."""
        # Numerical second derivative
        dr = 1e-6
        
        from .cir_formula import CIRBondPricer
        
        price_up = CIRBondPricer.zero_coupon_bond_price(params, current_rate + dr, maturity)
        price_down = CIRBondPricer.zero_coupon_bond_price(params, current_rate - dr, maturity)
        price_base = CIRBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        return (price_up - 2 * price_base + price_down) / (dr**2 * price_base)
    
    @staticmethod
    def parameter_sensitivities(
        params: CIRParameters,
        current_rate: float,
        maturity: float
    ) -> Dict[str, float]:
        """Calculate sensitivities to CIR parameters."""
        from .cir_formula import CIRBondPricer
        
        base_price = CIRBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        sensitivities = {}
        delta = 1e-6
        
        # Sensitivity to kappa
        params_kappa_up = CIRParameters(
            params.r0, params.theta, params.kappa + delta, params.sigma, params.maturity_time
        )
        price_kappa_up = CIRBondPricer.zero_coupon_bond_price(params_kappa_up, current_rate, maturity)
        sensitivities['kappa'] = (price_kappa_up - base_price) / delta
        
        # Sensitivity to theta
        params_theta_up = CIRParameters(
            params.r0, params.theta + delta, params.kappa, params.sigma, params.maturity_time
        )
        price_theta_up = CIRBondPricer.zero_coupon_bond_price(params_theta_up, current_rate, maturity)
        sensitivities['theta'] = (price_theta_up - base_price) / delta
        
        # Sensitivity to sigma
        params_sigma_up = CIRParameters(
            params.r0, params.theta, params.kappa, params.sigma + delta, params.maturity_time
        )
        price_sigma_up = CIRBondPricer.zero_coupon_bond_price(params_sigma_up, current_rate, maturity)
        sensitivities['sigma'] = (price_sigma_up - base_price) / delta
        
        return sensitivities