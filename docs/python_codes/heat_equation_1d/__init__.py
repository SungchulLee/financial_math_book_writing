# ============================================================================
# heat_equation_1d/__init__.py
# ============================================================================
"""
Heat Equation 1D
================

File structure:
heat_equation_1d/
├── __init__.py
├── analytical.py                    # Analytical solutions (Green's function, separation of variables)
├── grid.py                         # Spatial and temporal grid generation and management
├── heat_equation.py                # Core PDE formulation and equation setup
├── initial_conditions.py           # Initial condition functions and boundary conditions
├── matrices.py                     # Finite difference matrices and linear algebra setup
├── plotting.py                     # Visualization of heat diffusion and solution evolution
├── solvers.py                      # Numerical solvers (explicit, implicit, Crank-Nicolson)
└── wrapper.py                      # High-level interface and convenience functions

The Heat Equation: ∂u/∂t = α ∂²u/∂x²
Where:
- u(x,t): Temperature at position x and time t
- α: Thermal diffusivity coefficient
- Parabolic PDE with diffusion behavior

Connection to Finance:
- Heat equation ↔ Black-Scholes PDE (via variable transformation)
- Diffusion processes ↔ Stochastic processes
- Numerical methods applicable to option pricing PDEs
"""

# Core PDE formulation
from .heat_equation import (
    HeatEquation1D,
    solve_heat_equation
)

# Grid generation and management
from .grid import create_grid

# Initial and boundary conditions
from .initial_conditions import (
    step_function,
    gaussian_pulse
)

# Numerical solvers
from .solvers import (
    solve_forward_euler,
    solve_backward_euler,
    solve_crank_nicolson
)

# Analytical solutions
from .analytical import (
    solve_analytical,
    validate_against_analytical
)

# Visualization and plotting
from .plotting import (
    plot_method_comparison,
    plot_convergence_study,
    plot_with_analytical
)

from .wrapper import (
    HeatSolver,
    quick_solve
)

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "1D Heat equation numerical and analytical solver with visualization"