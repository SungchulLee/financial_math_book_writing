# ============================================================================
# cir/cir_wrapper.py
# ============================================================================
import brownian_motion as bmw
import logging
from typing import Optional, Dict, Any
from .cir_base import CIRParameters, CIRConfig, CIRScheme
from .cir_monte_carlo import CIRModel, SimulationConfig, CIRResult
from .cir_utils import CIRValidator, calculate_model_metrics


def create_cir_model(
    r0: float = CIRConfig.DEFAULT_R0,
    theta: float = CIRConfig.DEFAULT_THETA,
    kappa: float = CIRConfig.DEFAULT_KAPPA,
    sigma: float = CIRConfig.DEFAULT_SIGMA,
    maturity_time: float = CIRConfig.DEFAULT_MATURITY,
    seed: Optional[int] = None,
    check_feller: bool = True
) -> CIRModel:
    """
    Factory function to create CIR model with validation.
    
    Args:
        r0: Initial short rate
        theta: Long-term mean rate
        kappa: Mean reversion speed
        sigma: Volatility parameter
        maturity_time: Time horizon for simulation
        seed: Random seed for reproducibility
        check_feller: Whether to check Feller condition
        
    Returns:
        Configured CIRModel instance
    """
    parameters = CIRParameters(
        r0=r0,
        theta=theta,
        kappa=kappa,
        sigma=sigma,
        maturity_time=maturity_time
    )
    
    return CIRModel(
        parameters=parameters,
        seed=seed,
        check_feller=check_feller
    )


def quick_simulation(
    num_paths: int = CIRConfig.DEFAULT_NUM_PATHS,
    scheme: CIRScheme = CIRScheme.EULER_MARUYAMA,
    increment_type: bmw.IncrementType = bmw.IncrementType.NORMAL,
    **model_params
) -> CIRResult:
    """
    Quick simulation with default parameters.
    
    Args:
        num_paths: Number of simulation paths
        scheme: Discretization scheme to use
        increment_type: Type of Brownian increments
        **model_params: Additional CIR model parameters
        
    Returns:
        CIRResult containing simulation results
    """
    model = create_cir_model(**model_params)
    config = SimulationConfig(
        num_paths=num_paths,
        scheme=scheme,
        increment_type=increment_type
    )
    return model.simulate_cir(config)


class CIRAnalyzer:
    """High-level analyzer for CIR model results."""
    
    def __init__(self, model: CIRModel, validator: Optional[CIRValidator] = None):
        self.model = model
        self.validator = validator or CIRValidator()
        self.logger = logging.getLogger(__name__)
    
    def comprehensive_analysis(self, result: CIRResult) -> Dict[str, Any]:
        """
        Perform comprehensive analysis of CIR simulation results.
        
        Args:
            result: CIRResult from simulation
            
        Returns:
            Dictionary with comprehensive analysis
        """
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
        feller_satisfied = self.model.parameters.satisfies_feller_condition
        has_negative = result.has_negative_rates
        
        analysis['overall_assessment'] = {
            'validation_passed': all_passed,
            'feller_condition_satisfied': feller_satisfied,
            'negative_rates_present': has_negative,
            'quality_score': self._calculate_quality_score(analysis, has_negative, feller_satisfied)
        }
        
        return analysis
    
    def _calculate_theoretical_benchmarks(self, result: CIRResult) -> Dict[str, float]:
        """Calculate theoretical benchmarks for comparison."""
        final_time = result.time_steps[-1]
        
        return {
            'theoretical_final_mean': self.model.analytical_mean(final_time),
            'theoretical_final_variance': self.model.analytical_variance(final_time),
            'theoretical_final_std': self.model.analytical_std(final_time),
            'long_term_mean': self.model.parameters.theta,
            'initial_rate': self.model.parameters.r0,
        }
    
    def _calculate_quality_score(self, analysis: Dict[str, Any], has_negative_rates: bool, feller_satisfied: bool) -> float:
        """Calculate a quality score for the simulation (0-100)."""
        score = 100.0
        
        # Deduct points for validation failures
        validation_results = analysis['validation_results']
        for validation in validation_results.values():
            if not validation.passed:
                score -= 20 * validation.relative_error
        
        # Deduct points for negative rates
        if has_negative_rates:
            try:
                negative_pct = analysis['simulation_statistics']['path_statistics']['negative_rate_percentage']
                score -= negative_pct * 2
            except KeyError:
                # Fallback: assume 5% negative rates
                score -= 10
        
        # Deduct points for Feller condition violation
        if not feller_satisfied:
            score -= 15
        
        return max(0.0, min(100.0, score))