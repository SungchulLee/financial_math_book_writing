# ============================================================================
# brownian_motion/brownian_motion_simulation.py
# ============================================================================
import numpy as np
from typing import Optional
from dataclasses import dataclass
from enum import Enum


class IncrementType(Enum):
    """Enumeration for different types of Brownian motion increments."""
    NORMAL = "normal"
    FAIR_COIN = "fair_coin"
    ONES = "ones"


@dataclass
class BrownianMotionResult:
    """Container for Brownian motion simulation results."""
    time_steps: np.ndarray
    time_step_size: float
    sqrt_time_step_size: float
    brownian_paths: np.ndarray
    increments: np.ndarray
    
    @property
    def num_paths(self) -> int:
        return self.brownian_paths.shape[0]
    
    @property
    def num_time_steps(self) -> int:
        return self.brownian_paths.shape[1]


class BrownianMotion:
    
    DEFAULT_STEPS_PER_YEAR = 252  # Approximate trading days per year
    
    def __init__(self, maturity_time: float = 1.0, seed: Optional[int] = None):
        if maturity_time <= 0:
            raise ValueError("Maturity time must be positive")
        self.maturity_time = maturity_time
        self.seed = seed
        self.rng = np.random.RandomState(seed)

    def reset_seed(self, new_seed: Optional[int] = None):
        self.seed = new_seed
        self.rng = np.random.RandomState(new_seed)
    
    def get_seed(self) -> Optional[int]:
        return self.seed

    def simulate(
        self, 
        num_paths: int = 1, 
        num_steps: Optional[int] = None,
        increment_type: IncrementType = IncrementType.NORMAL,
        normalize_columns: bool = True
    ) -> BrownianMotionResult:
        
        if num_paths <= 0:
            raise ValueError("Number of paths must be positive")
        
        # Calculate time grid
        num_steps = self._get_num_steps(num_steps)
        time_steps = np.linspace(0, self.maturity_time, num_steps + 1)
        time_step_size = time_steps[1] - time_steps[0]
        sqrt_time_step_size = np.sqrt(time_step_size)
        
        # Generate increments
        raw_increments = self._generate_raw_increments(
            num_paths, num_steps, increment_type, self.rng
        )
        
        # Normalize if requested and applicable
        if self._should_normalize(num_paths, increment_type, normalize_columns):
            raw_increments = self._normalize_increments(raw_increments)
        
        # Scale by sqrt(dt) to get Brownian increments
        increments = raw_increments * sqrt_time_step_size
        
        # Compute cumulative paths starting from zero
        brownian_paths = self._compute_brownian_paths(increments)
        
        return BrownianMotionResult(
            time_steps=time_steps,
            time_step_size=time_step_size,
            sqrt_time_step_size=sqrt_time_step_size,
            brownian_paths=brownian_paths,
            increments=increments
        )
    
    def _get_num_steps(self, num_steps: Optional[int]) -> int:
        """Calculate number of time steps."""
        if num_steps is None:
            return int(self.maturity_time * self.DEFAULT_STEPS_PER_YEAR)
        if num_steps <= 0:
            raise ValueError("Number of steps must be positive")
        return num_steps
    
    def _generate_raw_increments(
        self, 
        num_paths: int, 
        num_steps: int, 
        increment_type: IncrementType,
        rng: np.random.RandomState
    ) -> np.ndarray:
        """Generate raw increments based on the specified type."""
        shape = (num_paths, num_steps)
        
        if increment_type == IncrementType.NORMAL:
            return rng.standard_normal(shape)
        elif increment_type == IncrementType.FAIR_COIN:
            return rng.binomial(1, 0.5, shape) * 2 - 1
        elif increment_type == IncrementType.ONES:
            return np.ones(shape)
        else:
            raise ValueError(f"Unknown increment type: {increment_type}")
    
    def _should_normalize(
        self, 
        num_paths: int, 
        increment_type: IncrementType, 
        normalize_columns: bool
    ) -> bool:
        """Determine if increments should be normalized."""
        return (
            normalize_columns 
            and num_paths > 1 
            and increment_type != IncrementType.ONES
        )
    
    def _normalize_increments(self, increments: np.ndarray) -> np.ndarray:
        """Normalize increments to zero mean and unit variance columnwise."""
        mean = increments.mean(axis=0)
        std = increments.std(axis=0)
        # Avoid division by zero
        std = np.where(std == 0, 1, std)
        return (increments - mean) / std
    
    def _compute_brownian_paths(self, increments: np.ndarray) -> np.ndarray:
        """Compute Brownian paths from increments via cumulative sum."""
        initial_values = np.zeros((increments.shape[0], 1))
        cumulative_increments = increments.cumsum(axis=1)
        return np.concatenate([initial_values, cumulative_increments], axis=1)