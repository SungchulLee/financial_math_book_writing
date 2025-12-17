# ============================================================================
# cir/__init__.py
# ============================================================================
"""
CIR
===

File structure:
cir/
├── __init__.py
├── cir_base.py                  # Base classes, parameters, exceptions
├── cir_formula.py               # Analytical formulas and bond pricing
├── cir_monte_carlo.py           # Monte Carlo simulation (inherits from brownian_motion)
├── cir_numerical.py             # Numerical methods and schemes
├── cir_utils.py                 # Utility functions and helpers
├── cir_schemes.py               # Different discretization schemes (Euler, Milstein, etc.)
└── cir_wrapper.py               # High-level wrapper and convenience functions

The CIR model: dr_t = κ(θ - r_t)dt + σ√r_t dW_t
Where:
- κ: mean reversion speed (a in Vasicek notation)
- θ: long-term mean (b in Vasicek notation)
- σ: volatility coefficient (multiplied by √r_t, unlike constant σ in Vasicek)

Key Differences from Vasicek:
- CIR has √r_t volatility term (prevents negative rates)
- Vasicek has constant σ volatility (allows negative rates)
- CIR: Non-central chi-squared distribution
- Vasicek: Gaussian distribution
- CIR: No exact simulation available
- Vasicek: Exact simulation possible
"""

# Core base classes and configuration
from .cir_base import (
    CIRParameters, 
    CIRConfig, 
    CIRScheme,
    CIRError,
    CIRParameterError,
    CIRSimulationError,
    CIRValidationError,
    CIRNumericalError
)

# Monte Carlo simulation
from .cir_monte_carlo import (
    CIRModel,
    CIRResult,
    SimulationConfig
)

# Analytical formulas and bond pricing
from .cir_formula import (
    CIRAnalytical,
    CIRBondPricer
)

# Numerical methods 
from .cir_numerical import (
    CIRNumerical,
    CIRRiskMetrics
)

# Utilities and validation
from .cir_utils import (
    CIRValidator,
    CIRCalibrator,
    ValidationResult,
    calculate_model_metrics
)

# High-level wrapper and convenience functions
from .cir_wrapper import (
    create_cir_model,
    quick_simulation,
    CIRAnalyzer
)

# External dependencies
from brownian_motion import IncrementType


__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Cox-Ingersoll-Ross short rate model implementation"