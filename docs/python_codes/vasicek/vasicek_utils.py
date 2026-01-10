# ============================================================================
# vasicek/vasicek_utils.py
# ============================================================================
import numpy as np
from dataclasses import dataclass
from typing import Dict
from .vasicek_base import VasicekConfig
from .vasicek_formula import VasicekAnalytical
from .vasicek_monte_carlo import VasicekResult


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


class VasicekValidator:
    """Validator for Vasicek simulation results."""
    
    def __init__(self, tolerance: float = VasicekConfig.VALIDATION_TOLERANCE):
        self.tolerance = tolerance
    
    def validate_mean(self, result: VasicekResult) -> ValidationResult:
        """Validate empirical mean against theoretical mean."""
        final_time = result.time_steps[-1]
        empirical_mean = float(np.mean(result.final_rates))
        theoretical_mean = VasicekAnalytical.mean(result.parameters, final_time)
        
        relative_error = abs(empirical_mean - theoretical_mean) / abs(theoretical_mean) if theoretical_mean != 0 else abs(empirical_mean)
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
    
    def validate_variance(self, result: VasicekResult) -> ValidationResult:
        """Validate empirical variance against theoretical variance."""
        final_time = result.time_steps[-1]
        empirical_var = float(np.var(result.final_rates))
        theoretical_var = VasicekAnalytical.variance(result.parameters, final_time)
        
        relative_error = abs(empirical_var - theoretical_var) / theoretical_var if theoretical_var != 0 else empirical_var
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
    
    def validate_gaussianity(self, result: VasicekResult) -> ValidationResult:
        """
        Validate that rates are approximately Gaussian (unique to Vasicek).
        Uses Shapiro-Wilk test if scipy is available, otherwise checks skewness/kurtosis.
        """
        final_rates = result.final_rates
        
        try:
            from scipy.stats import shapiro
            # Use Shapiro-Wilk test for normality
            stat, p_value = shapiro(final_rates[:min(5000, len(final_rates))])  # Limit sample size
            passed = p_value > 0.01  # Loose threshold for Monte Carlo
            
            return ValidationResult(
                test_name="Gaussianity (Shapiro-Wilk)",
                passed=passed,
                empirical_value=p_value,
                theoretical_value=0.05,  # Significance level
                relative_error=1 - p_value if p_value < 0.05 else 0,
                tolerance=0.01,
                message=f"p-value: {p_value:.4f} {'(PASS)' if passed else '(FAIL)'}"
            )
        except ImportError:
            # Fallback: check skewness and kurtosis
            from scipy.stats import skew, kurtosis
            empirical_skew = abs(skew(final_rates))
            empirical_kurt = abs(kurtosis(final_rates))  # Excess kurtosis
            
            # For normal distribution: skewness ≈ 0, excess kurtosis ≈ 0
            skew_ok = empirical_skew < 0.5
            kurt_ok = empirical_kurt < 1.0
            passed = skew_ok and kurt_ok
            
            return ValidationResult(
                test_name="Gaussianity (Moments)",
                passed=passed,
                empirical_value=max(empirical_skew, empirical_kurt),
                theoretical_value=0.0,
                relative_error=max(empirical_skew, empirical_kurt),
                tolerance=0.5,
                message=f"Skew: {empirical_skew:.3f}, Kurt: {empirical_kurt:.3f} {'(PASS)' if passed else '(FAIL)'}"
            )
    
    def full_validation(self, result: VasicekResult) -> Dict[str, ValidationResult]:
        """Perform comprehensive validation."""
        validations = {
            'mean': self.validate_mean(result),
            'variance': self.validate_variance(result),
            'gaussianity': self.validate_gaussianity(result)
        }
        
        return validations


class VasicekCalibrator:
    """Calibration utilities for Vasicek model."""
    
    @staticmethod
    def estimate_parameters_from_data(
        rates: np.ndarray,
        time_step: float
    ) -> Dict[str, float]:
        """
        Estimate Vasicek parameters from historical rate data using OLS.
        
        Uses the discrete-time version: r(t+1) = α + β*r(t) + ε
        Then converts to continuous-time parameters.
        """
        if len(rates) < 3:
            raise ValueError("Need at least 3 rate observations")
        
        # Set up regression: r(t+1) = α + β*r(t) + ε
        y = rates[1:]  # r(t+1)
        x = rates[:-1]  # r(t)
        
        # OLS estimation
        X = np.column_stack([np.ones(len(x)), x])
        coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
        alpha, beta = coeffs
        
        # Residuals for volatility estimation
        y_pred = alpha + beta * x
        residuals = y - y_pred
        sigma_discrete = np.std(residuals)
        
        # Convert to continuous-time parameters
        if beta <= 0 or beta >= 1:
            # Fallback for problematic beta
            a_est = 0.1
            b_est = np.mean(rates)
        else:
            a_est = -np.log(beta) / time_step
            b_est = alpha / (1 - beta)
        
        # Convert volatility (more complex for exact transformation)
        if a_est > 0:
            sigma_est = sigma_discrete * np.sqrt(2 * a_est / (1 - beta**2))
        else:
            sigma_est = sigma_discrete / np.sqrt(time_step)
        
        return {
            'r0': rates[0],
            'b': b_est,
            'a': max(a_est, 0.01),  # Ensure positive
            'sigma': max(sigma_est, 0.001),  # Ensure positive
        }


def calculate_model_metrics(result: VasicekResult) -> Dict[str, float]:
    """Calculate various model performance metrics."""
    final_rates = result.final_rates
    paths = result.short_rate_paths
    
    return {
        'final_rate_sharpe': (np.mean(final_rates) / np.std(final_rates) 
                             if np.std(final_rates) > 0 else 0),
        'path_volatility': np.mean(np.std(paths, axis=1)),
        'mean_reversion_strength': result.parameters.a,
        'negative_rate_percentage': np.mean(paths < 0) * 100,
        'convergence_to_b': abs(np.mean(final_rates) - result.parameters.b),
        'autocorrelation': np.corrcoef(final_rates[:-1], final_rates[1:])[0, 1] if len(final_rates) > 1 else 0,
    }