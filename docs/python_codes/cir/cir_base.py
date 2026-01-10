# ============================================================================
# cir/cir_base.py
# ============================================================================
import warnings
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class CIRScheme(Enum):
    """CIR discretization schemes."""
    EULER_MARUYAMA = "euler_maruyama"
    MILSTEIN = "milstein"
    EXACT = "exact"
    TRUNCATED_EULER = "truncated_euler"


class CIRConfig:
    """Configuration class for CIR model settings."""
    
    # Default model parameters
    DEFAULT_R0 = 0.03
    DEFAULT_THETA = 0.05
    DEFAULT_KAPPA = 0.1
    DEFAULT_SIGMA = 0.03
    DEFAULT_MATURITY = 10.0
    
    # Numerical constraints
    MIN_RATE = 1e-10
    MAX_RATE = 1.0
    MIN_TIME = 1e-6
    MAX_TIME = 100.0
    
    # Simulation defaults
    DEFAULT_NUM_PATHS = 1000
    
    # Validation tolerances
    VALIDATION_TOLERANCE = 0.05
    FELLER_WARNING_THRESHOLD = 0.9


# ===============================================
# Custom Exceptions
# ===============================================

class CIRError(Exception):
    """Base exception for CIR model errors."""
    pass


class CIRParameterError(CIRError):
    """Exception for invalid CIR model parameters."""
    pass


class CIRSimulationError(CIRError):
    """Exception for simulation-related errors."""
    pass


class CIRValidationError(CIRError):
    """Exception for validation failures."""
    pass


class CIRNumericalError(CIRError):
    """Exception for numerical computation errors."""
    pass


# ===============================================
# Parameter Classes
# ===============================================

@dataclass(frozen=True)
class CIRParameters:
    """Immutable container for CIR model parameters."""
    r0: float
    theta: float
    kappa: float
    sigma: float
    maturity_time: float
    
    def __post_init__(self):
        """Validate parameters after initialization."""
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate all CIR parameters."""
        if not (CIRConfig.MIN_RATE < self.r0 < CIRConfig.MAX_RATE):
            raise CIRParameterError(
                f"Initial rate r0={self.r0} must be in "
                f"({CIRConfig.MIN_RATE}, {CIRConfig.MAX_RATE})"
            )
        
        if not (CIRConfig.MIN_RATE < self.theta < CIRConfig.MAX_RATE):
            raise CIRParameterError(
                f"Long-term mean theta={self.theta} must be in "
                f"({CIRConfig.MIN_RATE}, {CIRConfig.MAX_RATE})"
            )
        
        if self.kappa <= 0:
            raise CIRParameterError(
                f"Mean reversion speed kappa={self.kappa} must be positive"
            )
        
        if self.sigma <= 0:
            raise CIRParameterError(
                f"Volatility sigma={self.sigma} must be positive"
            )
        
        if not (CIRConfig.MIN_TIME < self.maturity_time < CIRConfig.MAX_TIME):
            raise CIRParameterError(
                f"Maturity time={self.maturity_time} must be in "
                f"({CIRConfig.MIN_TIME}, {CIRConfig.MAX_TIME})"
            )
    
    @property
    def feller_parameter(self) -> float:
        """Calculate the Feller parameter: 2κθ/σ²."""
        return (2 * self.kappa * self.theta) / (self.sigma ** 2)
    
    @property
    def satisfies_feller_condition(self) -> bool:
        """Check if parameters satisfy the Feller condition."""
        return self.feller_parameter >= 1.0
    
    def check_feller_condition(self, strict: bool = True) -> None:
        """Check Feller condition and raise warnings/errors."""
        if not self.satisfies_feller_condition:
            if strict and self.feller_parameter < CIRConfig.FELLER_WARNING_THRESHOLD:
                raise CIRParameterError(
                    f"Feller condition strongly violated: "
                    f"2κθ/σ² = {self.feller_parameter:.3f} < 1. "
                    f"Consider adjusting parameters or use strict=False."
                )
            else:
                warnings.warn(
                    f"Feller condition violated: "
                    f"2κθ/σ² = {self.feller_parameter:.3f} < 1. "
                    f"Rates may occasionally reach zero.",
                    UserWarning
                )
    
    def to_dict(self) -> Dict[str, float]:
        """Convert parameters to dictionary."""
        return {
            'r0': self.r0,
            'theta': self.theta,
            'kappa': self.kappa,
            'sigma': self.sigma,
            'maturity_time': self.maturity_time,
            'feller_parameter': self.feller_parameter
        }