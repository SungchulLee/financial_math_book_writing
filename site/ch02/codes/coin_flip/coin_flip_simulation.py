# ============================================================================
# coin_flip/coin_flip_simulation.py
# ============================================================================
import numpy as np
from typing import Optional


class CoinFlip:
    
    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        self.rng = np.random.RandomState(seed)
    
    def flip_coins(self, num_flips: int, p_heads: float = 0.5, num_paths: int = 1) -> np.ndarray:
        self._validate_parameters(num_flips, p_heads, num_paths)
        
        # Generate coin flips: 1 for Heads, -1 for Tails
        flips = self.rng.binomial(1, p_heads, size=(num_paths, num_flips)) * 2 - 1
        
        # Return 1D array if only one path for convenience
        if num_paths == 1:
            return flips[0]  
        
        return flips
    
    def _validate_parameters(self, num_flips: int, p_heads: float, num_paths: int):
        if num_flips <= 0:
            raise ValueError("num_flips must be positive")
        if not 0 <= p_heads <= 1:
            raise ValueError("p_heads must be between 0 and 1")
        if num_paths <= 0:
            raise ValueError("num_paths must be positive")
    
    def reset_seed(self, new_seed: Optional[int] = None):
        self.seed = new_seed
        self.rng = np.random.RandomState(new_seed)
    
    def get_seed(self) -> Optional[int]:
        return self.seed