# ============================================================================
# cir/cir_utils.py
# ============================================================================
import numpy as np
from dataclasses import dataclass
from typing import Dict
from .cir_base import CIRConfig
from .cir_formula import CIRAnalytical
from .cir_monte_carlo import CIRResult


@dataclass
class ValidationResult:
    """Container for validation results."""
    test_name: str
    passed: bool
    empirical_value: float
    theoretical_value: float
    relative_error: float
    tolerance: float
    message: str = ""
    
    @property
    def error_percentage(self) -> float:
        """Get relative error as percentage."""
        return self.relative_error * 100


class CIRValidator:
    """Validator for CIR simulation results."""
    
    def __init__(self, tolerance: float = CIRConfig.VALIDATION_TOLERANCE):
        self.tolerance = tolerance
    
    def validate_mean(self, result: CIRResult) -> ValidationResult:
        """Validate empirical mean against theoretical mean."""
        final_time = result.time_steps[-1]
        empirical_mean = float(np.mean(result.final_rates))
        theoretical_mean = CIRAnalytical.mean(result.parameters, final_time)
        
        relative_error = abs(empirical_mean - theoretical_mean) / theoretical_mean
        passed = relative_error < self.tolerance
        
        return ValidationResult(
            test_name="Mean Validation",
            passed=passed,
            empirical_value=empirical_mean,
            theoretical_value=theoretical_mean,
            relative_error=relative_error,
            tolerance=self.tolerance,
            message=f"Mean error: {relative_error:.4f} {'(PASS)' if passed else '(FAIL)'}"
        )
    
    def validate_variance(self, result: CIRResult) -> ValidationResult:
        """Validate empirical variance against theoretical variance."""
        final_time = result.time_steps[-1]
        empirical_var = float(np.var(result.final_rates))
        theoretical_var = CIRAnalytical.variance(result.parameters, final_time)
        
        relative_error = abs(empirical_var - theoretical_var) / theoretical_var
        passed = relative_error < self.tolerance
        
        return ValidationResult(
            test_name="Variance Validation",
            passed=passed,
            empirical_value=empirical_var,
            theoretical_value=theoretical_var,
            relative_error=relative_error,
            tolerance=self.tolerance,
            message=f"Variance error: {relative_error:.4f} {'(PASS)' if passed else '(FAIL)'}"
        )
    
    def validate_non_negativity(self, result: CIRResult) -> ValidationResult:
        """Validate that rates remain non-negative."""
        has_negative = result.has_negative_rates
        min_rate = result.min_rate
        
        return ValidationResult(
            test_name="Non-negativity",
            passed=not has_negative,
            empirical_value=min_rate,
            theoretical_value=0.0,
            relative_error=0.0 if not has_negative else abs(min_rate),
            tolerance=0.0,
            message=f"Min rate: {min_rate:.6f} {'(PASS)' if not has_negative else '(FAIL)'}"
        )
    
    def full_validation(self, result: CIRResult) -> Dict[str, ValidationResult]:
        """Perform comprehensive validation."""
        return {
            'mean': self.validate_mean(result),
            'variance': self.validate_variance(result),
            'non_negativity': self.validate_non_negativity(result)
        }


class CIRCalibrator:
    """Calibration utilities for CIR model."""
    
    @staticmethod
    def estimate_parameters_from_data(
        rates: np.ndarray,
        time_step: float
    ) -> Dict[str, float]:
        """
        Estimate CIR parameters from historical rate data using method of moments.
        
        Args:
            rates: Array of historical interest rates
            time_step: Time step between observations
            
        Returns:
            Dictionary with estimated parameters
        """
        if len(rates) < 2:
            raise ValueError("Need at least 2 rate observations")
        
        # Calculate basic statistics
        mean_rate = np.mean(rates)
        var_rate = np.var(rates)
        
        # Simple method of moments estimation
        # More sophisticated methods would use maximum likelihood
        theta_est = mean_rate
        
        # Estimate sigma from variance relationship
        if mean_rate > 0:
            sigma_est = np.sqrt(2 * var_rate / mean_rate)
        else:
            sigma_est = 0.1  # Default fallback
        
        # Estimate kappa from autocorrelation
        if len(rates) > 1:
            autocorr = np.corrcoef(rates[:-1], rates[1:])[0, 1]
            kappa_est = -np.log(max(autocorr, 0.01)) / time_step
        else:
            kappa_est = 0.1  # Default fallback
        
        return {
            'r0': rates[0] if len(rates) > 0 else mean_rate,
            'theta': theta_est,
            'kappa': max(kappa_est, 0.01),  # Ensure positive
            'sigma': max(sigma_est, 0.01),  # Ensure positive
        }


def calculate_model_metrics(result: CIRResult) -> Dict[str, float]:
    """Calculate various model performance metrics."""
    final_rates = result.final_rates
    paths = result.short_rate_paths
    
    return {
        'final_rate_sharpe': (np.mean(final_rates) / np.std(final_rates) 
                             if np.std(final_rates) > 0 else 0),
        'path_volatility': np.mean(np.std(paths, axis=1)),
        'mean_reversion_strength': result.parameters.kappa,
        'feller_ratio': result.parameters.feller_parameter,
        'absorption_frequency': np.mean(paths == 0) * 100,
        'convergence_to_theta': abs(np.mean(final_rates) - result.parameters.theta),
    }