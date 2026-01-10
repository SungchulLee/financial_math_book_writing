# ============================================================================
# vasicek/vasicek_base.py
# ============================================================================
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class VasicekScheme(Enum):
    """Vasicek discretization schemes."""
    EULER_MARUYAMA = "euler_maruyama"
    EXACT = "exact"  # Vasicek has exact simulation
    MILSTEIN = "milstein"  # Same as Euler for linear drift


class VasicekConfig:
    """Configuration class for Vasicek model settings."""
    
    # Default model parameters
    DEFAULT_R0 = 0.03
    DEFAULT_B = 0.05  # long-term mean (b)
    DEFAULT_A = 0.1   # mean reversion speed (a)
    DEFAULT_SIGMA = 0.03
    DEFAULT_MATURITY = 10.0
    
    # Numerical constraints
    MIN_RATE = -0.1  # Vasicek can go negative
    MAX_RATE = 1.0
    MIN_TIME = 1e-6
    MAX_TIME = 100.0
    
    # Simulation defaults
    DEFAULT_NUM_PATHS = 1000
    
    # Validation tolerances
    VALIDATION_TOLERANCE = 0.05


# ===============================================
# Custom Exceptions
# ===============================================

class VasicekError(Exception):
    """Base exception for Vasicek model errors."""
    pass


class VasicekParameterError(VasicekError):
    """Exception for invalid Vasicek model parameters."""
    pass


class VasicekSimulationError(VasicekError):
    """Exception for simulation-related errors."""
    pass


class VasicekValidationError(VasicekError):
    """Exception for validation failures."""
    pass


class VasicekNumericalError(VasicekError):
    """Exception for numerical computation errors."""
    pass


# ===============================================
# Parameter Classes
# ===============================================

@dataclass(frozen=True)
class VasicekParameters:
    """Immutable container for Vasicek model parameters."""
    r0: float      # Initial rate
    b: float       # Long-term mean (θ in some notation)
    a: float       # Mean reversion speed (κ in some notation)
    sigma: float   # Constant volatility
    maturity_time: float
    
    def __post_init__(self):
        """Validate parameters after initialization."""
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate all Vasicek parameters."""
        if not (VasicekConfig.MIN_RATE < self.r0 < VasicekConfig.MAX_RATE):
            raise VasicekParameterError(
                f"Initial rate r0={self.r0} must be in "
                f"({VasicekConfig.MIN_RATE}, {VasicekConfig.MAX_RATE})"
            )
        
        if not (VasicekConfig.MIN_RATE < self.b < VasicekConfig.MAX_RATE):
            raise VasicekParameterError(
                f"Long-term mean b={self.b} must be in "
                f"({VasicekConfig.MIN_RATE}, {VasicekConfig.MAX_RATE})"
            )
        
        if self.a <= 0:
            raise VasicekParameterError(
                f"Mean reversion speed a={self.a} must be positive"
            )
        
        if self.sigma <= 0:
            raise VasicekParameterError(
                f"Volatility sigma={self.sigma} must be positive"
            )
        
        if not (VasicekConfig.MIN_TIME < self.maturity_time < VasicekConfig.MAX_TIME):
            raise VasicekParameterError(
                f"Maturity time={self.maturity_time} must be in "
                f"({VasicekConfig.MIN_TIME}, {VasicekConfig.MAX_TIME})"
            )
    
    def to_dict(self) -> Dict[str, float]:
        """Convert parameters to dictionary."""
        return {
            'r0': self.r0,
            'b': self.b,
            'a': self.a,
            'sigma': self.sigma,
            'maturity_time': self.maturity_time
        }