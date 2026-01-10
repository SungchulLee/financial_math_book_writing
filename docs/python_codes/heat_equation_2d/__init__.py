# ============================================================================
# heat_equation_2d/__init__.py
# ============================================================================
"""
Heat Equation 2D
================

File structure:
heat_equation_2d/
├── __init__.py
├── analytical.py                    # Analytical solutions (2D Green's function, product solutions)
├── grid.py                         # 2D spatial mesh generation and boundary handling
├── heat_equation.py                # 2D PDE formulation: ∂u/∂t = α(∂²u/∂x² + ∂²u/∂y²)
├── initial_conditions.py           # 2D initial temperature distributions and boundary conditions
├── matrices.py                     # 2D finite difference matrices and sparse linear algebra
├── plotting.py                     # 3D surface plots, contour plots, and heat map animations
├── solvers.py                      # 2D numerical solvers (ADI, splitting methods, multigrid)
└── wrapper.py                      # High-level interface for 2D heat simulation

The 2D Heat Equation: ∂u/∂t = α(∂²u/∂x² + ∂²u/∂y²)
Where:
- u(x,y,t): Temperature at position (x,y) and time t
- α: Thermal diffusivity coefficient
- Laplacian operator in 2D space

Multi-Dimensional Financial Applications:
- Two-factor interest rate models (Hull-White 2F)
- Basket option pricing (multi-asset Black-Scholes)
- Currency pairs and correlation modeling
- Multi-dimensional risk factor evolution
"""

# ============================================
# heat_equation_2d/__init__.py
# ============================================

# Grid generation and management
from .grid import (
    Grid2DParams,
    create_2d_grid,
    check_2d_stability,
    create_time_array_2d,
    get_stability_info
)

# Initial and boundary conditions
from .initial_conditions import (
    step_function_2d,
    gaussian_pulse_2d,
    gaussian_2d,
    circular_pulse_2d,
    sine_wave_2d,
    multiple_hotspots_2d,
    ring_pattern_2d,
    custom_function_2d,
    zero_initial_condition_2d
)

# Matrix construction and linear algebra
from .matrices import (
    construct_2d_laplacian,
    construct_forward_euler_2d,
    construct_backward_euler_2d,
    construct_crank_nicolson_2d,
    construct_crank_nicolson_matrices_2d,
    construct_adi_matrices,
    apply_dirichlet_bc_2d,
    construct_neumann_bc_2d
)

# Numerical solvers
from .solvers import (
    solve_forward_euler_2d,
    solve_backward_euler_2d,
    solve_crank_nicolson_2d,
    solve_crank_nicolson_adi_2d,
    compare_2d_methods
)

# Analytical solutions
from .analytical import (
    solve_analytical_2d,
    validate_against_analytical_2d
)

# Visualization and plotting
from .plotting import (
    plot_2d_solution,
    plot_method_comparison_2d,
    plot_2d_evolution,
    plot_cross_sections
)

from .wrapper import (
    HeatEquation2D,
    solve_heat_equation_2d
)

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "2D Heat equation numerical solver with multi-dimensional PDE methods"