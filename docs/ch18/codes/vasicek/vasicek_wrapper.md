# Vasicek Wrapper

## Background

This page presents the Python implementation for **Vasicek Wrapper**.

---

## Code

```python
"""
Vasicek Wrapper

Educational script demonstrating vasicek wrapper concepts.
"""

# ============================================================================
# vasicek/vasicek_wrapper.py
# ============================================================================
import brownian_motion as bmw
from typing import Optional
from .vasicek_base import VasicekParameters, VasicekConfig, VasicekScheme
from .vasicek_monte_carlo import VasicekModel, SimulationConfig, VasicekResult


def create_vasicek_model(
    r0: float = VasicekConfig.DEFAULT_R0,
    b: float = VasicekConfig.DEFAULT_B,
    a: float = VasicekConfig.DEFAULT_A,
    sigma: float = VasicekConfig.DEFAULT_SIGMA,
    maturity_time: float = VasicekConfig.DEFAULT_MATURITY,
    seed: Optional[int] = None


if __name__ == "__main__":
    ) -> VasicekModel:
        """
        Factory function to create Vasicek model with validation.
    
        Args:
            r0: Initial short rate
            b: Long-term mean rate
            a: Mean reversion speed
            sigma: Constant volatility
            maturity_time: Time horizon for simulation
            seed: Random seed for reproducibility
        
        Returns:
            Configured VasicekModel instance
        """
        parameters = VasicekParameters(
            r0=r0,
            b=b,
            a=a,
            sigma=sigma,
            maturity_time=maturity_time
        )
    
        return VasicekModel(
            parameters=parameters,
            seed=seed
        )


    def quick_simulation(
        num_paths: int = VasicekConfig.DEFAULT_NUM_PATHS,
        scheme: VasicekScheme = VasicekScheme.EXACT,
        increment_type: bmw.IncrementType = bmw.IncrementType.NORMAL,
        **model_params
    ) -> VasicekResult:
        """
        Quick simulation with default parameters.
    
        Args:
            num_paths: Number of simulation paths
            scheme: Discretization scheme to use
            increment_type: Type of Brownian increments
            **model_params: Additional Vasicek model parameters
        
        Returns:
            VasicekResult containing simulation results
        """
        model = create_vasicek_model(**model_params)
        config = SimulationConfig(
            num_paths=num_paths,
            scheme=scheme,
            increment_type=increment_type
        )
        return model.simulate_vasicek(config)


    class VasicekAnalyzer:
        """High-level analyzer for Vasicek model results."""
    
        def __init__(self, model: VasicekModel):
            self.model = model
            from .vasicek_utils import VasicekValidator
            self.validator = VasicekValidator()
    
        def comprehensive_analysis(self, result: VasicekResult) -> dict:
            """Perform comprehensive analysis of Vasicek simulation results."""
            from .vasicek_utils import calculate_model_metrics
        
            analysis = {
                'model_parameters': self.model.parameters.to_dict(),
                'simulation_statistics': result.get_statistics(),
                'validation_results': self.validator.full_validation(result),
                'model_metrics': calculate_model_metrics(result),
                'theoretical_benchmarks': self._calculate_theoretical_benchmarks(result),
            }
        
            # Add overall assessment
            validation_results = analysis['validation_results']
            all_passed = all(v.passed for v in validation_results.values())
        
            analysis['overall_assessment'] = {
                'validation_passed': all_passed,
                'negative_rates_present': result.has_negative_rates,
                'quality_score': self._calculate_quality_score(analysis)
            }
        
            return analysis
    
        def _calculate_theoretical_benchmarks(self, result: VasicekResult) -> dict:
            """Calculate theoretical benchmarks for comparison."""
            final_time = result.time_steps[-1]
        
            return {
                'theoretical_final_mean': self.model.analytical_mean(final_time),
                'theoretical_final_variance': self.model.analytical_variance(final_time),
                'theoretical_final_std': self.model.analytical_std(final_time),
                'long_term_mean': self.model.parameters.b,
                'initial_rate': self.model.parameters.r0,
            }
    
        def _calculate_quality_score(self, analysis: dict) -> float:
            """Calculate a quality score for the simulation (0-100)."""
            score = 100.0
        
            # Deduct points for validation failures
            for validation in analysis['validation_results'].values():
                if not validation.passed:
                    score -= 20 * validation.relative_error
        
            # Note: Unlike CIR, negative rates are allowed in Vasicek
            # so we don't penalize for them
        
            return max(0.0, min(100.0, score))
```

## Exercises

**Exercise 1.**
Using the `create_vasicek_model` factory function with all defaults, what are the model parameters? Compute the long-run mean and standard deviation of the short rate.

??? success "Solution to Exercise 1"
    The defaults are $r_0 = 0.03$, $b = 0.05$, $a = 0.1$, $\sigma = 0.03$, and `maturity_time = 10.0`. The long-run (stationary) distribution is $r_\infty \sim \mathcal{N}(b, \sigma^2/(2a))$:

    - Mean: $b = 0.05$
    - Variance: $\sigma^2/(2a) = 0.0009/0.2 = 0.0045$
    - Standard deviation: $\sqrt{0.0045} \approx 0.0671$

    In the long run, rates fluctuate around $5\%$ with a standard deviation of about $6.7\%$ (in absolute terms), meaning rates between $-1.7\%$ and $11.7\%$ cover roughly one standard deviation on each side.

---

**Exercise 2.**
Write a `quick_simulation` call to compare Vasicek and CIR under identical parameters $r_0 = 0.04$, long-term mean $= 0.06$, mean reversion $= 0.2$, $\sigma = 0.03$, with 5000 paths. What key difference would you observe?

??? success "Solution to Exercise 2"
    ```python
    vasicek_result = quick_simulation(num_paths=5000, r0=0.04, b=0.06, a=0.2, sigma=0.03)
    ```

    For CIR, the analogous call uses `theta=0.06`, `kappa=0.2`. The key difference: the Vasicek simulation will have `has_negative_rates = True` (since rates are Gaussian), while the CIR simulation will have `has_negative_rates = False` (the Feller parameter is $2 \times 0.2 \times 0.06 / 0.03^2 \approx 26.7$, strongly satisfying the condition). The final rate distributions will also differ: Gaussian for Vasicek, chi-squared-based for CIR.

---

**Exercise 3.**
The `VasicekAnalyzer._calculate_quality_score` method does not penalize negative rates, unlike the CIR analyzer. Explain this design choice.

??? success "Solution to Exercise 3"
    Negative rates are a fundamental mathematical property of the Vasicek model (Gaussian short rate), not a simulation artifact. Penalizing them would give misleadingly low quality scores for correctly implemented simulations. In contrast, the CIR model's theoretical process is non-negative, so negative rates in a CIR simulation indicate discretization error or parameter misconfiguration, justifying a quality penalty. The Vasicek analyzer only deducts points for validation failures (mean, variance, Gaussianity mismatches), which represent genuine simulation errors.

---

**Exercise 4.**
Describe the full workflow of `comprehensive_analysis`: what data does it collect, what tests does it run, and how does it aggregate the results into an overall assessment?

??? success "Solution to Exercise 4"
    The workflow is:

    1. **Data collection**: Extracts `model_parameters` (from `to_dict()`), `simulation_statistics` (from `get_statistics()`), and `theoretical_benchmarks` (analytical mean, variance, std at final time, plus $b$ and $r_0$).
    2. **Validation**: Runs `full_validation` which tests (a) mean accuracy, (b) variance accuracy, and (c) Gaussianity (Shapiro-Wilk). Each produces a `ValidationResult` with pass/fail and relative error.
    3. **Metrics**: Computes `model_metrics` including Sharpe ratio, path volatility, convergence to $b$, negative rate percentage, and autocorrelation.
    4. **Aggregation**: The `overall_assessment` combines (a) whether all validation tests passed, (b) whether negative rates are present (informational, not penalized), and (c) a quality score starting at 100, reduced by $20 \times \varepsilon$ for each failed validation test with relative error $\varepsilon$.
