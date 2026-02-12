# ============================================================================
# vasicek/vasicek_monte_carlo.py
# ============================================================================
import brownian_motion as bmw
import logging
import numpy as np
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .vasicek_base import VasicekParameters, VasicekScheme, VasicekSimulationError
from .vasicek_schemes import get_scheme_simulator


@dataclass
class SimulationConfig:
    """Configuration for Vasicek simulation."""
    num_paths: int = 1000
    num_steps: Optional[int] = None
    scheme: VasicekScheme = VasicekScheme.EXACT  # Default to exact for Vasicek
    increment_type: bmw.IncrementType = bmw.IncrementType.NORMAL
    normalize_columns: bool = True
    
    def __post_init__(self):
        """Validate simulation configuration."""
        if self.num_paths <= 0:
            raise VasicekSimulationError("Number of paths must be positive")
        
        if self.num_steps is not None and self.num_steps <= 0:
            raise VasicekSimulationError("Number of steps must be positive")


@dataclass
class VasicekResult:
    """Container for Vasicek simulation results."""
    time_steps: np.ndarray
    short_rate_paths: np.ndarray
    parameters: VasicekParameters
    config: SimulationConfig
    brownian_increments: np.ndarray
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate result arrays."""
        if self.short_rate_paths.ndim != 2:
            raise VasicekSimulationError("Short rate paths must be 2D array")
        
        if len(self.time_steps) != self.short_rate_paths.shape[1]:
            raise VasicekSimulationError("Time steps length must match path length")
    
    @property
    def num_paths(self) -> int:
        """Number of simulated paths."""
        return self.short_rate_paths.shape[0]
    
    @property
    def num_time_steps(self) -> int:
        """Number of time steps."""
        return self.short_rate_paths.shape[1]
    
    @property
    def final_rates(self) -> np.ndarray:
        """Final short rates at maturity."""
        return self.short_rate_paths[:, -1]
    
    @property
    def initial_rate(self) -> float:
        """Initial short rate."""
        return self.parameters.r0
    
    @property
    def time_step_size(self) -> float:
        """Size of each time step."""
        return (self.time_steps[1] - self.time_steps[0] 
                if len(self.time_steps) > 1 else 0.0)
    
    @property
    def has_negative_rates(self) -> bool:
        """Check if any simulated rates are negative."""
        return np.any(self.short_rate_paths < 0)
    
    @property
    def min_rate(self) -> float:
        """Minimum rate across all paths and times."""
        return float(np.min(self.short_rate_paths))
    
    @property
    def max_rate(self) -> float:
        """Maximum rate across all paths and times."""
        return float(np.max(self.short_rate_paths))
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get comprehensive statistics of the simulation."""
        final_rates = self.final_rates
        
        return {
            'final_rates': {
                'mean': float(np.mean(final_rates)),
                'std': float(np.std(final_rates)),
                'min': float(np.min(final_rates)),
                'max': float(np.max(final_rates)),
                'median': float(np.median(final_rates)),
                'q25': float(np.percentile(final_rates, 25)),
                'q75': float(np.percentile(final_rates, 75)),
            },
            'path_statistics': {
                'global_min': self.min_rate,
                'global_max': self.max_rate,
                'has_negative': self.has_negative_rates,
                'negative_rate_percentage': float(np.mean(self.short_rate_paths < 0) * 100)
            },
            'simulation_info': {
                'num_paths': self.num_paths,
                'num_steps': self.num_time_steps,
                'time_step_size': self.time_step_size,
                'total_time': float(self.time_steps[-1])
            }
        }


class VasicekModel(bmw.BrownianMotion):
    """
    Vasicek Model implementation inheriting from BrownianMotion.
    
    This class extends the BrownianMotion class to simulate Vasicek short rate paths
    using the generated Brownian increments.
    
    The Vasicek model: dr_t = a(b - r_t)dt + σ dW_t
    """
    
    def __init__(
        self,
        parameters: VasicekParameters,
        seed: Optional[int] = None
    ):
        # Initialize parent BrownianMotion class
        super().__init__(maturity_time=parameters.maturity_time, seed=seed)
        
        self.parameters = parameters
        self.logger = logging.getLogger(__name__)
    
    def simulate_vasicek(self, config: SimulationConfig) -> VasicekResult:
        """
        Simulate Vasicek short rate paths.
        
        This method uses the inherited BrownianMotion functionality to generate
        increments and then applies Vasicek-specific dynamics.
        """
        self.logger.info(f"Starting Vasicek simulation: {config.num_paths} paths")
        
        # Generate Brownian motion using parent class
        brownian_result = super().simulate(
            num_paths=config.num_paths,
            num_steps=config.num_steps,
            increment_type=config.increment_type,
            normalize_columns=config.normalize_columns
        )
        
        # Apply Vasicek dynamics to the Brownian increments
        short_rate_paths = self._apply_vasicek_dynamics(
            brownian_result.increments,
            brownian_result.time_step_size,
            config
        )
        
        result = VasicekResult(
            time_steps=brownian_result.time_steps,
            short_rate_paths=short_rate_paths,
            parameters=self.parameters,
            config=config,
            brownian_increments=brownian_result.increments,
            metadata={
                'simulation_time': brownian_result.time_steps[-1],
                'scheme_used': config.scheme.value,
                'can_be_negative': True  # Unlike CIR
            }
        )
        
        self.logger.info("Vasicek simulation completed successfully")
        return result
    
    def _apply_vasicek_dynamics(
        self,
        brownian_increments: np.ndarray,
        dt: float,
        config: SimulationConfig
    ) -> np.ndarray:
        """Apply Vasicek dynamics to Brownian increments."""
        # Get the appropriate scheme simulator
        scheme_simulator = get_scheme_simulator(config.scheme)
        
        # Apply the Vasicek dynamics
        return scheme_simulator(
            self.parameters,
            brownian_increments,
            dt
        )
    
    def analytical_mean(self, t: float) -> float:
        """Analytical mean at time t."""
        from .vasicek_formula import VasicekAnalytical
        return VasicekAnalytical.mean(self.parameters, t)
    
    def analytical_variance(self, t: float) -> float:
        """Analytical variance at time t."""
        from .vasicek_formula import VasicekAnalytical
        return VasicekAnalytical.variance(self.parameters, t)
    
    def analytical_std(self, t: float) -> float:
        """Analytical standard deviation at time t."""
        from .vasicek_formula import VasicekAnalytical
        return VasicekAnalytical.standard_deviation(self.parameters, t)