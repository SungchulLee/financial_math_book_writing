# ============================================================================
# simple_random_walk/__init__.py
# ============================================================================
"""
Simple Random Walk
==================

File structure:
simple_random_walk/
├── __init__.py
└── simple_random_walk_simulation.py    # Core random walk simulation and path generation

The Simple Random Walk: S_n = S_0 + ∑(i=1 to n) X_i
Where:
- S_n: Position after n steps
- X_i ∈ {-1, +1}: Independent random steps (symmetric)
- S_0: Starting position (usually 0)
- E[S_n] = S_0, Var(S_n) = n

Mathematical Properties:
- Discrete-time, discrete-space process
- Markov property: Future depends only on current state
- Scaling limit: S_n/√n → Brownian motion as n → ∞
- Recurrent in 1D, 2D; transient in 3D+

Foundation for Financial Models:
- Simplest model of price movements
- Building block for more complex processes
- Educational tool for understanding randomness
- Discrete approximation of continuous models
"""

# Core random walk simulation
from .simple_random_walk_simulation import (
    SimpleRandomWalk,
    StepType
)

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Simple random walk simulation and discrete stochastic process generation"