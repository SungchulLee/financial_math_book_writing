# Vasicek Monte Carlo

## Background

Vasicek Monte Carlo

Educational script demonstrating vasicek monte carlo concepts.

---

## Code

```python
"""
Vasicek Monte Carlo

Educational script demonstrating vasicek monte carlo concepts.
"""

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


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
The Vasicek model uses the exact simulation scheme as its default. Write the exact transition formula for $r(t + \Delta t) \mid r(t)$ and explain why it eliminates discretization error.

??? success "Solution to Exercise 1"
    The exact transition is

    $$
    r(t + \Delta t) = r(t)\,e^{-a\Delta t} + b(1 - e^{-a\Delta t}) + \sigma\sqrt{\frac{1 - e^{-2a\Delta t}}{2a}}\,Z,
    $$

    where $Z \sim \mathcal{N}(0,1)$. This formula is exact because the Vasicek SDE has a linear drift and constant diffusion, making $r(t)$ an Ornstein-Uhlenbeck process with a known Gaussian transition density. No approximation is made; the conditional distribution of $r(t + \Delta t)$ given $r(t)$ is exactly Gaussian with the specified mean and variance, regardless of the step size $\Delta t$.

---

**Exercise 2.**
Explain why the `VasicekResult.has_negative_rates` property is expected to return `True` for most Vasicek simulations, unlike the CIR model.

??? success "Solution to Exercise 2"
    The Vasicek process is Gaussian, meaning $r(t)$ can take any real value. The probability of negative rates is

    $$
    \mathbb{P}(r(t) < 0) = \Phi\!\left(\frac{-\mathbb{E}[r(t)]}{\sqrt{\text{Var}[r(t)]}}\right),
    $$

    which is nonzero whenever $\mathbb{E}[r(t)] < \infty$. For typical parameters ($b = 0.05$, $\sigma = 0.02$, $a = 0.1$) and long horizons, this probability can be several percent. With thousands of paths and hundreds of time steps, it is virtually certain that at least one rate observation will be negative. This contrasts with the CIR model, where $r(t) \geq 0$ almost surely under the Feller condition.

---

**Exercise 3.**
The `get_statistics` method returns the negative rate percentage. If $r(t)$ is stationary with mean $b = 0.04$ and standard deviation $\sigma_\infty = \sigma/\sqrt{2a} = 0.03$, estimate the long-run percentage of negative rates.

??? success "Solution to Exercise 3"
    In stationarity, $r \sim \mathcal{N}(b, \sigma_\infty^2) = \mathcal{N}(0.04, 0.0009)$. The probability of a negative rate is

    $$
    \mathbb{P}(r < 0) = \Phi\!\left(\frac{0 - 0.04}{0.03}\right) = \Phi(-1.333) \approx 0.0912.
    $$

    Approximately $9.1\%$ of rate observations in the stationary regime will be negative.

---

**Exercise 4.**
The `VasicekModel` class inherits from `BrownianMotion`. Describe the inheritance hierarchy and how the `simulate_vasicek` method leverages the parent class.

??? success "Solution to Exercise 4"
    The hierarchy is `BrownianMotion` $\to$ `VasicekModel`. The parent class `BrownianMotion` provides:

    - Random seed management
    - The `simulate` method that generates Brownian increments $\Delta W_i$
    - Time grid construction

    The `simulate_vasicek` method calls `super().simulate(...)` to obtain a `BrownianResult` containing the increments and time grid. It then passes these increments to `_apply_vasicek_dynamics`, which selects the appropriate scheme (exact, Euler-Maruyama, or Milstein) and transforms the Brownian increments into Vasicek short rate paths. This design separates the stochastic driver (Brownian motion) from the model-specific dynamics, enabling code reuse across different short-rate models.
