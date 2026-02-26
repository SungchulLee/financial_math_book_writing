# ============================================================================
# binomial_model/__init__.py
# ============================================================================
"""
Binomial Model
==============

File structure:
binomial_model/
├── __init__.py
├── binomial_model_parameter.py      # Model parameters and configuration
├── binomial_model_plotter.py        # Visualization and plotting functions
├── binomial_model_pricer.py         # Option pricing and financial calculations
└── binomial_model_wrapper.py        # High-level wrapper and convenience functions

The Binomial Model: Tree-based discrete-time option pricing
Key Features:
- Discrete time steps with up/down movements
- Risk-neutral valuation
- American and European option pricing
- Dividend handling capabilities
- Convergence to Black-Scholes as steps → ∞
"""

# Core components
from .binomial_model_parameter import BinomialParameter
from .binomial_model_pricer import BinomialPricer
from .binomial_model_plotter import BinomialPlotter
from .binomial_model_wrapper import BinomialModel

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Binomial tree option pricing model implementation"