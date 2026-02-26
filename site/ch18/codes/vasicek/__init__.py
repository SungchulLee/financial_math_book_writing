# ============================================================================
# vasicek/__init__.py
# ============================================================================
"""
Vasicek
=======

File structure:
vasicek/
├── __init__.py
├── vasicek_base.py              # Base classes, parameters, exceptions
├── vasicek_formula.py           # Analytical formulas and bond pricing
├── vasicek_monte_carlo.py       # Monte Carlo simulation (inherits from brownian_motion)
├── vasicek_numerical.py         # Numerical methods and schemes
├── vasicek_utils.py             # Utility functions and helpers
├── vasicek_schemes.py           # Different discretization schemes
└── vasicek_wrapper.py           # High-level wrapper and convenience functions

The Vasicek model: dr_t = a(b - r_t)dt + σ dW_t
Where:
- a: mean reversion speed (κ in CIR notation)
- b: long-term mean (θ in CIR notation)  
- σ: constant volatility (no sqrt(r_t) term)
"""

# Core base classes and configuration
from .vasicek_base import (
    VasicekParameters, 
    VasicekConfig, 
    VasicekScheme,
    VasicekError,
    VasicekParameterError,
    VasicekSimulationError,
    VasicekValidationError,
    VasicekNumericalError
)

# Monte Carlo simulation
from .vasicek_monte_carlo import (
    VasicekModel,
    VasicekResult,
    SimulationConfig
)

# Analytical formulas and bond pricing
from .vasicek_formula import (
    VasicekAnalytical,
    VasicekBondPricer
)

# Numerical methods 
from .vasicek_numerical import (
    VasicekNumerical,
    VasicekRiskMetrics
)

# Utilities and validation
from .vasicek_utils import (
    VasicekValidator,
    VasicekCalibrator,
    ValidationResult,
    calculate_model_metrics
)

# High-level wrapper and convenience functions
from .vasicek_wrapper import (
    create_vasicek_model,
    quick_simulation,
    VasicekAnalyzer
)

# External dependencies
from brownian_motion import IncrementType

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Vasicek short rate model implementation"