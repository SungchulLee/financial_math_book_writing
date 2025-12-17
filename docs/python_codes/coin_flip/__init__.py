# ============================================================================
# coin_flip/__init__.py
# ============================================================================
"""
Coin Flip
=========

File structure:
coin_flip/
├── __init__.py
└── coin_flip_simulation.py         # Core coin flip simulation and binary process generation

The Coin Flip Process: X_n ∈ {-1, +1} or {0, 1}
Key Properties:
- Discrete binary outcomes
- Independent trials: P(X_n = +1) = p, P(X_n = -1) = 1-p
- Bernoulli distribution for each flip
- Binomial distribution for sum of flips
- Discrete-time random walk foundation

Relationship to Brownian Motion:
- Scaled coin flip → Brownian motion (Central Limit Theorem)
- √n · (S_n/n - p) → N(0, p(1-p)) as n → ∞
- Discrete approximation of continuous stochastic processes
"""

# Core coin flip simulation
from .coin_flip_simulation import CoinFlip


__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Coin flip process simulation and binary random walk generation"