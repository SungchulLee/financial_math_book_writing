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