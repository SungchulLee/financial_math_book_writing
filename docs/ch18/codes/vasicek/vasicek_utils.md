# Vasicek Utils

## Background

Vasicek Utils

Educational script demonstrating vasicek utils concepts.

---

## Code

```python
"""
Vasicek Utils

Educational script demonstrating vasicek utils concepts.
"""

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


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
A Vasicek simulation produces an empirical variance of $0.00180$ while the theoretical variance is $0.00173$. Compute the relative error and determine whether the variance validation test passes with $5\%$ tolerance.

??? success "Solution to Exercise 1"
    The relative error is

    $$
    \varepsilon = \frac{|0.00180 - 0.00173|}{0.00173} = \frac{0.00007}{0.00173} \approx 0.0405 = 4.05\%.
    $$

    Since $4.05\% < 5\%$, the variance validation test passes.

---

**Exercise 2.**
The Gaussianity validation uses the Shapiro-Wilk test. Explain why the test is applied to a subsample of at most 5000 observations, and what the null hypothesis is.

??? success "Solution to Exercise 2"
    The Shapiro-Wilk test has a null hypothesis $H_0$: the sample comes from a normal distribution. For very large samples, even tiny deviations from normality lead to rejection (the test becomes too powerful), so the code caps the sample at 5000 to avoid spurious rejections due to Monte Carlo sampling noise rather than genuine non-normality. The threshold $p > 0.01$ is deliberately loose to accommodate the finite-sample approximations inherent in Monte Carlo. Since the Vasicek process is theoretically Gaussian, this test validates that the simulation correctly reproduces the distributional property.

---

**Exercise 3.**
The OLS calibration estimates $a$ from $\hat{a} = -\ln(\hat{\beta})/\Delta t$. If the autocorrelation between consecutive daily rates is $\hat{\rho} = 0.998$ and $\Delta t = 1/252$, estimate $a$.

??? success "Solution to Exercise 3"
    Since $\hat{\beta} \approx \hat{\rho} = 0.998$:

    $$
    \hat{a} = \frac{-\ln(0.998)}{1/252} = \frac{0.002002}{0.003968} \approx 0.5045.
    $$

    The estimated mean reversion speed is approximately $0.50$, implying a half-life of $\ln(2)/0.50 \approx 1.39$ years.

---

**Exercise 4.**
The `calculate_model_metrics` function computes `convergence_to_b` as $|\bar{r}_T - b|$. If $\bar{r}_T = 0.047$ and $b = 0.05$, compute this metric. How would you expect it to behave as $T \to \infty$ and $N \to \infty$?

??? success "Solution to Exercise 4"
    The convergence metric is

    $$
    |\bar{r}_T - b| = |0.047 - 0.05| = 0.003.
    $$

    As $T \to \infty$, $\mathbb{E}[r(T)] \to b$, so the theoretical mean approaches $b$. As the number of paths $N \to \infty$, the sample mean $\bar{r}_T$ converges to $\mathbb{E}[r(T)]$ by the law of large numbers. Therefore, for large $T$ and $N$, this metric converges to zero: $|\bar{r}_T - b| \to 0$. The rate of convergence in $N$ is $O(1/\sqrt{N})$ and in $T$ is $O(e^{-aT})$.
