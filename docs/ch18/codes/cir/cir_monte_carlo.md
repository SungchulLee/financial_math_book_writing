# Cir Monte Carlo

## Background

Cir Monte Carlo

Educational script demonstrating cir monte carlo concepts.

---

## Code

```python
"""
Cir Monte Carlo

Educational script demonstrating cir monte carlo concepts.
"""

# ============================================================================
# cir/cir_monte_carlo.py
# ============================================================================
import brownian_motion as bmw
import logging
import numpy as np
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .cir_base import CIRParameters, CIRScheme, CIRSimulationError
from .cir_schemes import get_scheme_simulator


@dataclass
class SimulationConfig:
    """Configuration for CIR simulation."""
    num_paths: int = 1000
    num_steps: Optional[int] = None
    scheme: CIRScheme = CIRScheme.EULER_MARUYAMA
    increment_type: bmw.IncrementType = bmw.IncrementType.NORMAL
    absorption_fix: bool = True
    normalize_columns: bool = True
    
    def __post_init__(self):
        """Validate simulation configuration."""
        if self.num_paths <= 0:
            raise CIRSimulationError("Number of paths must be positive")
        
        if self.num_steps is not None and self.num_steps <= 0:
            raise CIRSimulationError("Number of steps must be positive")


@dataclass
class CIRResult:
    """Container for CIR simulation results."""
    time_steps: np.ndarray
    short_rate_paths: np.ndarray
    parameters: CIRParameters
    config: SimulationConfig
    brownian_increments: np.ndarray
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate result arrays."""
        if self.short_rate_paths.ndim != 2:
            raise CIRSimulationError("Short rate paths must be 2D array")
        
        if len(self.time_steps) != self.short_rate_paths.shape[1]:
            raise CIRSimulationError("Time steps length must match path length")
    
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


class CIRModel(bmw.BrownianMotion):
    """
    CIR Model implementation inheriting from BrownianMotion.
    
    This class extends the BrownianMotion class to simulate CIR short rate paths
    using the generated Brownian increments.
    """
    
    def __init__(
        self,
        parameters: CIRParameters,
        seed: Optional[int] = None,
        check_feller: bool = True
    ):
        # Initialize parent BrownianMotion class
        super().__init__(maturity_time=parameters.maturity_time, seed=seed)
        
        self.parameters = parameters
        self.logger = logging.getLogger(__name__)
        
        if check_feller:
            self.parameters.check_feller_condition(strict=False)
    
    def simulate_cir(self, config: SimulationConfig) -> CIRResult:
        """
        Simulate CIR short rate paths.
        
        This method uses the inherited BrownianMotion functionality to generate
        increments and then applies CIR-specific dynamics.
        """
        self.logger.info(f"Starting CIR simulation: {config.num_paths} paths")
        
        # Generate Brownian motion using parent class
        brownian_result = super().simulate(
            num_paths=config.num_paths,
            num_steps=config.num_steps,
            increment_type=config.increment_type,
            normalize_columns=config.normalize_columns
        )
        
        # Apply CIR dynamics to the Brownian increments
        short_rate_paths = self._apply_cir_dynamics(
            brownian_result.increments,
            brownian_result.time_step_size,
            config
        )
        
        result = CIRResult(
            time_steps=brownian_result.time_steps,
            short_rate_paths=short_rate_paths,
            parameters=self.parameters,
            config=config,
            brownian_increments=brownian_result.increments,
            metadata={
                'simulation_time': brownian_result.time_steps[-1],
                'feller_satisfied': self.parameters.satisfies_feller_condition,
                'scheme_used': config.scheme.value
            }
        )
        
        self.logger.info("CIR simulation completed successfully")
        return result
    
    def _apply_cir_dynamics(
        self,
        brownian_increments: np.ndarray,
        dt: float,
        config: SimulationConfig
    ) -> np.ndarray:
        """Apply CIR dynamics to Brownian increments."""
        # Get the appropriate scheme simulator
        scheme_simulator = get_scheme_simulator(config.scheme)
        
        # Apply the CIR dynamics
        return scheme_simulator(
            self.parameters,
            brownian_increments,
            dt,
            config.absorption_fix
        )
    
    def analytical_mean(self, t: float) -> float:
        """Analytical mean at time t."""
        from .cir_formula import CIRAnalytical
        return CIRAnalytical.mean(self.parameters, t)
    
    def analytical_variance(self, t: float) -> float:
        """Analytical variance at time t."""
        from .cir_formula import CIRAnalytical
        return CIRAnalytical.variance(self.parameters, t)
    
    def analytical_std(self, t: float) -> float:
        """Analytical standard deviation at time t."""
        from .cir_formula import CIRAnalytical
        return CIRAnalytical.standard_deviation(self.parameters, t)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Describe the two-step procedure used by the `CIRModel.simulate_cir` method: (1) generating Brownian increments and (2) applying CIR dynamics. Why is this decomposition useful from a software engineering perspective?

??? success "Solution to Exercise 1"
    The first step inherits from the `BrownianMotion` parent class and generates standard Brownian increments $\Delta W_i \sim \mathcal{N}(0, \Delta t)$ for all paths and time steps. The second step takes these increments and applies the CIR-specific SDE

    $$
    r_{i+1} = r_i + \kappa(\theta - r_i)\,\Delta t + \sigma\sqrt{r_i}\,\Delta W_i.
    $$

    This decomposition follows the strategy pattern: the Brownian motion generation is reusable across different interest rate models (Vasicek, CIR, Hull-White), while only the dynamics step differs. It also facilitates testing, since one can verify the Brownian increments independently from the model-specific logic.

---

**Exercise 2.**
The `CIRResult.has_negative_rates` property checks whether any simulated rate is negative. Explain why negative rates can appear in an Euler-Maruyama simulation of the CIR process even though the theoretical CIR process is non-negative.

??? success "Solution to Exercise 2"
    The continuous-time CIR process $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$ is non-negative when the Feller condition $2\kappa\theta \geq \sigma^2$ holds. However, the Euler-Maruyama discretization

    $$
    r_{i+1} = r_i + \kappa(\theta - r_i)\,\Delta t + \sigma\sqrt{r_i}\,\Delta W_i
    $$

    can produce $r_{i+1} < 0$ for a large negative $\Delta W_i$, since the discrete step does not enforce non-negativity. This occurs more frequently when $\Delta t$ is large, $\sigma$ is large relative to $\kappa\theta$, or when $r_i$ is close to zero. The `absorption_fix` option in `SimulationConfig` addresses this by applying $r_{i+1} = \max(r_{i+1}, 0)$.

---

**Exercise 3.**
Suppose a CIR simulation produces `num_paths = 5000` and `num_time_steps = 200`. What are the dimensions of the `short_rate_paths` array, and how do you extract the distribution of rates at the midpoint of the simulation?

??? success "Solution to Exercise 3"
    The `short_rate_paths` array has shape $(5000, 200)$, where each row is a path and each column corresponds to a time step. To extract rates at the midpoint (time step index 100):

    ```python
    midpoint_rates = result.short_rate_paths[:, 100]
    ```

    This gives a one-dimensional array of 5000 values representing the distribution of $r(T/2)$ across all simulated paths. One can then compute summary statistics such as `np.mean(midpoint_rates)` and `np.std(midpoint_rates)` or plot a histogram.

---

**Exercise 4.**
The `get_statistics` method returns percentiles `q25` and `q75` of the final rate distribution. If `q25 = 0.038` and `q75 = 0.062`, compute the interquartile range (IQR). Using the IQR, propose a criterion for detecting outlier paths.

??? success "Solution to Exercise 4"
    The interquartile range is

    $$
    \text{IQR} = q_{75} - q_{25} = 0.062 - 0.038 = 0.024.
    $$

    A standard outlier detection criterion (Tukey's fences) flags any final rate $r_T$ as an outlier if

    $$
    r_T < q_{25} - 1.5 \times \text{IQR} \quad \text{or} \quad r_T > q_{75} + 1.5 \times \text{IQR}.
    $$

    Substituting:

    $$
    r_T < 0.038 - 0.036 = 0.002 \quad \text{or} \quad r_T > 0.062 + 0.036 = 0.098.
    $$

    Paths with final rates below $0.2\%$ or above $9.8\%$ would be flagged as outliers.
