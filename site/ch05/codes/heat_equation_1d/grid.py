# ============================================================================
# heat_equation_1d/grid.py
# ============================================================================
import numpy as np
from typing import NamedTuple


class GridParams(NamedTuple):
    """Grid parameters for the 1D heat equation."""
    L: float          # Length of domain
    T: float          # Total time
    Nx: int           # Number of spatial points
    Nt: int           # Number of time steps
    D: float          # Thermal diffusivity
    dx: float         # Spatial step size
    dt: float         # Time step size
    x: np.ndarray     # Spatial grid
    coeff: float      # Diffusion coefficient (D*dt/dx^2)


def create_grid(L: float = 1.0, T: float = 0.1, Nx: int = 100, Nt: int = 1000, 
                D: float = 0.01) -> GridParams:
    """
    Create spatial and temporal grids for the heat equation.
    
    Args:
        L: Length of the rod
        T: Total simulation time
        Nx: Number of spatial grid points
        Nt: Number of time steps
        D: Thermal diffusivity constant
        
    Returns:
        GridParams containing all grid information
    """
    if L <= 0 or T <= 0 or D <= 0:
        raise ValueError("L, T, and D must be positive")
    if Nx < 3 or Nt < 1:
        raise ValueError("Nx must be >= 3, Nt must be >= 1")
    
    dx = L / (Nx - 1)
    dt = T / Nt
    x = np.linspace(0, L, Nx)
    coeff = D * dt / dx**2
    
    return GridParams(L, T, Nx, Nt, D, dx, dt, x, coeff)


def check_stability(coeff: float, method: str = "forward") -> None:
    """
    Check stability condition for explicit schemes.
    
    Args:
        coeff: Diffusion coefficient (D*dt/dx^2)
        method: Numerical method being used
        
    Raises:
        ValueError: If stability condition is violated
    """
    if method == "forward" and coeff > 0.5:
        raise ValueError(
            f"Forward Euler unstable: coeff = {coeff:.4f} > 0.5. "
            f"Reduce dt or increase dx."
        )


def create_time_array(T: float, Nt: int) -> np.ndarray:
    """Create time array for the simulation."""
    return np.linspace(0, T, Nt + 1)