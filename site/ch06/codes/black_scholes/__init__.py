# ============================================================================
# black_scholes/__init__.py
# ============================================================================
"""
Black-Scholes Option Pricing Library
====================================

File structure (UNCHANGED from original):
black_scholes/
├── __init__.py
├── black_scholes_base.py            # Base classes, parameters, exceptions
├── black_scholes_formula.py         # Analytical BS formulas and option pricing
├── black_scholes_greeks.py          # Greeks calculation (Delta, Gamma, Theta, etc.)
├── black_scholes_implied_vol.py     # Implied volatility calculations
├── black_scholes_monte_carlo.py     # Monte Carlo simulation
├── black_scholes_numerical.py       # Numerical methods and finite difference schemes
├── black_scholes_schemes.py         # Different discretization schemes
├── black_scholes_utils.py           # Utility functions and helpers
└── black_scholes_wrapper.py         # High-level wrapper and convenience functions

BACKWARD COMPATIBILITY GUARANTEED:
- All original files preserved
- All original classes work unchanged
- All original methods work unchanged
- Only internal implementations improved
- New features added without breaking existing API
"""

# Core base classes and configuration (UNCHANGED IMPORTS)
from .black_scholes_base import BlackScholesBase

# Analytical formulas and option pricing (UNCHANGED IMPORTS)
from .black_scholes_formula import BlackScholesFormula

# Greeks calculations (UNCHANGED IMPORTS)
from .black_scholes_greeks import BlackScholesGreeks

# Implied volatility calculations (UNCHANGED IMPORTS)
from .black_scholes_implied_vol import BlackScholesImpliedVol

# Monte Carlo simulation (UNCHANGED IMPORTS)
from .black_scholes_monte_carlo import BlackScholesMonteCarlo

# Numerical methods (UNCHANGED IMPORTS)
from .black_scholes_numerical import BlackScholesNumericalSolver

# High-level wrapper (UNCHANGED IMPORTS)
from .black_scholes_wrapper import BlackScholes

# Utility functions (UNCHANGED IMPORTS)
from .black_scholes_utils import (
    d1_d2, 
    bs_call_price, 
    bs_put_price, 
    delta, 
    gamma, 
    vega,
    theta, 
    rho,
    implied_volatility,
    simulate_gbm_paths,
    draw_finite_difference_grid,
    compute_implied_volatilities_and_summarize,
    run_advanced_analysis_on_implied_vol
)

__version__ = "1.1.0"  # Minor version bump to indicate improvements
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Black-Scholes option pricing model implementation"