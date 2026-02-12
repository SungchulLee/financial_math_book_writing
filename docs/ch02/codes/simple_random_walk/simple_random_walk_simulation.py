# ============================================================================
# simple_random_walk/simple_random_walk_simulation.py
# ============================================================================
import numpy as np
from typing import Tuple, Optional
from enum import Enum


class StepType(Enum):
    FAIR_COIN = "fair_coin"
    NORMAL = "normal"


class SimpleRandomWalk:
    
    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        self.rng = np.random.RandomState(seed)

    def simulate(self, 
                num_paths: int = 1, 
                num_steps: int = 100, 
                step_type: StepType = StepType.FAIR_COIN) -> Tuple[np.ndarray, np.ndarray]:

        self._validate_parameters(num_paths, num_steps)
        
        # Generate random steps
        steps = self._generate_steps(num_paths, num_steps, step_type)
        
        # Add initial position (0) to the beginning
        initial_positions = np.zeros((num_paths, 1))
        all_steps = np.hstack((initial_positions, steps))
        
        # Calculate cumulative positions
        positions = np.cumsum(all_steps, axis=1)
        
        # Generate time steps
        time_steps = np.arange(num_steps + 1)
        
        return time_steps, positions
    
    def _validate_parameters(self, num_paths: int, num_steps: int):
        if num_paths <= 0:
            raise ValueError("num_paths must be positive")
        if num_steps <= 0:
            raise ValueError("num_steps must be positive")
    
    def _generate_steps(self, num_paths: int, num_steps: int, step_type: StepType) -> np.ndarray:
        if step_type == StepType.FAIR_COIN:
            return self.rng.binomial(n=1, p=0.5, size=(num_paths, num_steps)) * 2 - 1
        elif step_type == StepType.NORMAL:
            return self.rng.standard_normal((num_paths, num_steps))
        else:
            raise ValueError(f"Unsupported step type: {step_type}")
        
        # Standardize across paths if multiple paths exist
        if num_paths > 1:
            # Avoid division by zero
            std_dev = steps.std(axis=0)
            std_dev = np.where(std_dev == 0, 1, std_dev)
            steps = (steps - steps.mean(axis=0)) / std_dev
            
        return steps
    
    def reset_seed(self, new_seed: Optional[int] = None):
        self.seed = new_seed
        self.rng = np.random.RandomState(new_seed)
    
    def get_seed(self) -> Optional[int]:
        return self.seed