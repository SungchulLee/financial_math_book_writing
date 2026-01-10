# ============================================================================
# heat_equation_2d/grid.py
# ============================================================================
import numpy as np
from typing import NamedTuple


class Grid2DParams(NamedTuple):
    """Grid parameters for the 2D heat equation."""
    Lx: float; Ly: float; T: float; Nx: int; Ny: int; Nt: int; D: float
    dx: float; dy: float; dt: float; x: np.ndarray; y: np.ndarray
    X: np.ndarray; Y: np.ndarray; rx: float; ry: float


def check_2d_stability(rx: float, ry: float, method: str = "forward") -> None:
    """
    Check stability condition for 2D explicit schemes.
    
    Args:
        rx: Diffusion coefficient in x direction (D*dt/dx^2)
        ry: Diffusion coefficient in y direction (D*dt/dy^2)
        method: Numerical method being used
        
    Raises:
        ValueError: If stability condition is violated
    """
    if method == "forward" and rx + ry > 0.5:
        raise ValueError(
            f"Forward Euler unstable in 2D: rx + ry = {rx + ry:.4f} > 0.5. "
            f"Reduce dt or increase dx/dy."
        )


def create_time_array_2d(T: float, Nt: int) -> np.ndarray:
    """Create time array for the 2D simulation."""
    return np.linspace(0, T, Nt + 1)


def get_stability_info(params):
    """Get stability information for the grid parameters."""
    stability_param = params.rx + params.ry
    return {
        "stability_parameter": stability_param,
        "is_stable_forward": stability_param <= 0.5,
        "rx": params.rx,
        "ry": params.ry,
        "dx": params.dx,
        "dy": params.dy,
        "dt": params.dt
    }


def create_2d_grid(Lx=1.0, Ly=1.0, T=0.1, Nx=50, Ny=50, Nt=1000, D=0.01):
    """Create 2D grid parameters."""
    dx, dy, dt = Lx/(Nx-1), Ly/(Ny-1), T/Nt
    x, y = np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y, indexing="ij")
    rx, ry = D*dt/dx**2, D*dt/dy**2
    return Grid2DParams(Lx, Ly, T, Nx, Ny, Nt, D, dx, dy, dt, x, y, X, Y, rx, ry)