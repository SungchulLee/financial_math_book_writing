# Cir Utils

## Background

Cir Utils

Educational script demonstrating cir utils concepts.

---

## Code

```python
"""
Cir Utils

Educational script demonstrating cir utils concepts.
"""

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


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
A CIR simulation produces an empirical final rate mean of $0.0485$ while the theoretical mean is $0.0500$. With a validation tolerance of $5\%$, does this test pass? Compute the relative error.

??? success "Solution to Exercise 1"
    The relative error is

    $$
    \varepsilon_{\text{rel}} = \frac{|0.0485 - 0.0500|}{0.0500} = \frac{0.0015}{0.0500} = 0.03 = 3\%.
    $$

    Since $3\% < 5\%$ (the tolerance), the mean validation test passes.

---

**Exercise 2.**
Explain the method-of-moments approach used in `estimate_parameters_from_data` to estimate the CIR volatility $\sigma$ from historical rate data. What assumption is being made?

??? success "Solution to Exercise 2"
    The method uses the relationship between the long-run variance of the CIR process and its parameters. In the stationary distribution, the variance is

    $$
    \text{Var}(r_\infty) = \frac{\sigma^2 \theta}{2\kappa}.
    $$

    The code estimates $\theta \approx \bar{r}$ (the sample mean) and then solves

    $$
    \hat{\sigma} = \sqrt{\frac{2\,\text{Var}(r)}{\bar{r}}},
    $$

    where $\text{Var}(r)$ is the sample variance. This assumes the data is from the stationary distribution, meaning the time series is long enough that transient effects from the initial condition $r_0$ have dissipated.

---

**Exercise 3.**
The `validate_non_negativity` method returns a `ValidationResult`. If a simulation with `absorption_fix=False` and Euler-Maruyama produces a minimum rate of $-0.002$, describe the `ValidationResult` fields.

??? success "Solution to Exercise 3"
    The fields would be:

    - `test_name`: `"Non-negativity"`
    - `passed`: `False` (since $-0.002 < 0$)
    - `empirical_value`: $-0.002$ (the minimum rate observed)
    - `theoretical_value`: $0.0$ (the theoretical lower bound)
    - `relative_error`: $0.002$ (the absolute value of the minimum rate)
    - `tolerance`: $0.0$ (any negative rate constitutes a failure)
    - `message`: `"Min rate: -0.002000 (FAIL)"`

    This indicates the simulation violated the theoretical non-negativity property, likely because the Feller condition was violated or the Euler-Maruyama discretization produced overshoots.

---

**Exercise 4.**
The `calculate_model_metrics` function computes `absorption_frequency` as the percentage of zero rates. If paths have shape $(1000, 500)$ and 250 entries equal zero, compute this metric. What does a high absorption frequency indicate about the model parameters?

??? success "Solution to Exercise 4"
    The total number of entries is $1000 \times 500 = 500{,}000$. The absorption frequency is

    $$
    \text{absorption frequency} = \frac{250}{500{,}000} \times 100 = 0.05\%.
    $$

    A high absorption frequency indicates that the Feller condition is violated or nearly violated ($2\kappa\theta < \sigma^2$ or close), meaning the process frequently touches zero. This suggests that either $\sigma$ is too large relative to $\kappa\theta$, or the absorption fix is actively clamping negative values to zero. It may warrant parameter adjustment or switching to a more appropriate scheme (e.g., exact simulation).
