# ============================================================================
# black_scholes/__init__.py
# ============================================================================
"""
Black-Scholes
=============

File structure:
black_scholes/
├── __init__.py
├── black_scholes_base.py            # Base classes, parameters, exceptions
├── black_scholes_formula.py         # Analytical BS formulas and option pricing
├── black_scholes_greeks.py          # Greeks calculation (Delta, Gamma, Theta, etc.)
├── black_scholes_implied_vol.py     # Implied volatility calculations
├── black_scholes_monte_carlo.py     # Monte Carlo simulation (inherits from brownian_motion)
├── black_scholes_numerical.py       # Numerical methods and finite difference schemes
├── black_scholes_schemes.py         # Different discretization schemes (Euler, Milstein)
├── black_scholes_utils.py           # Utility functions and helpers
└── black_scholes_wrapper.py         # High-level wrapper and convenience functions

The Black-Scholes Model: dS_t = μS_t dt + σS_t dW_t
Where:
- S_t: Stock price at time t
- μ: Expected return (drift)
- σ: Constant volatility
- W_t: Brownian motion

Key Features:
- Geometric Brownian Motion for stock prices
- Lognormal distribution of prices
- Analytical option pricing formulas
- Greeks for risk management
- Implied volatility calibration
"""

# Core base classes and configuration
from .black_scholes_base import BlackScholesBase

# Analytical formulas and option pricing
from .black_scholes_formula import BlackScholesFormula

# Greeks calculations
from .black_scholes_greeks import BlackScholesGreeks

# Implied volatility calculations
from .black_scholes_implied_vol import BlackScholesImpliedVol

# Monte Carlo simulation
from .black_scholes_monte_carlo import BlackScholesMonteCarlo

# Numerical methods
from .black_scholes_numerical import BlackScholesNumericalSolver

# High-level wrapper
from .black_scholes_wrapper import BlackScholes

# Utility functions
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
    draw_finite_difference_grid
)

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Black-Scholes option pricing model implementation"