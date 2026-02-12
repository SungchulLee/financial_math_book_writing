# ============================================================================
# brownian_motion/__init__.py
# ============================================================================
"""
Brownian Motion
===============

File structure:
brownian_motion/
├── __init__.py
└── brownian_motion_simulation.py    # Core Brownian motion simulation and increment generation

The Brownian Motion Process: W_t ~ N(0, t)
Key Properties:
- W_0 = 0 (starts at zero)
- Independent increments: W_t - W_s ~ N(0, t-s) for t > s
- Continuous paths but nowhere differentiable
- Gaussian distribution
- Quadratic variation [W]_t = t

Foundation Role:
- Base building block for all stochastic models
- Provides random increment generation
- Supports different increment types (Normal, Fair Coin, etc.)
- Used by Vasicek, CIR, Black-Scholes, and other SDE models
"""

# Core Brownian motion simulation
from .brownian_motion_simulation import (
    BrownianMotion,
    IncrementType
)

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Brownian motion process simulation and increment generation"