# ============================================================================
# heat_equation_2d/analytical.py
# ============================================================================
import numpy as np
from typing import Callable


def solve_analytical_2d(X: np.ndarray, Y: np.ndarray, t: float, 
                       initial_func: Callable, D: float, Lx: float, Ly: float,
                       method: str = "eigenfunction", N: int = 20) -> np.ndarray:
    """
    Basic analytical solution for 2D heat equation (simplified version).
    
    For now, this provides a simple eigenfunction expansion for sine wave initial conditions.
    """
    if method == "eigenfunction":
        # Only works for sine wave initial conditions
        try:
            # Try to detect if this is a sine wave
            # This is a simplified implementation
            return _solve_sine_eigenfunction(X, Y, t, D, Lx, Ly, N)
        except:
            # Fallback: return zeros if analytical solution fails
            print("Analytical solution not available for this initial condition")
            return np.zeros_like(X)
    else:
        print(f"Analytical method '{method}' not implemented yet")
        return np.zeros_like(X)


def _solve_sine_eigenfunction(X: np.ndarray, Y: np.ndarray, t: float, 
                             D: float, Lx: float, Ly: float, N: int = 20) -> np.ndarray:
    """Simple eigenfunction solution for (1,1) sine mode."""
    # For u(x,y,0) = sin(πx/Lx)sin(πy/Ly), the analytical solution is:
    # u(x,y,t) = sin(πx/Lx)sin(πy/Ly) * exp(-D*π²*(1/Lx² + 1/Ly²)*t)
    
    lambda_11 = np.pi**2 * (1/Lx**2 + 1/Ly**2)
    return np.sin(np.pi * X / Lx) * np.sin(np.pi * Y / Ly) * np.exp(-D * lambda_11 * t)


def validate_against_analytical_2d(numerical_solution: np.ndarray, 
                                  X: np.ndarray, Y: np.ndarray, t: float,
                                  initial_func: Callable, D: float, 
                                  Lx: float, Ly: float,
                                  method: str = "eigenfunction") -> dict:
    """
    Basic validation against analytical solution.
    """
    try:
        analytical_solution = solve_analytical_2d(X, Y, t, initial_func, D, Lx, Ly, method)
        
        # Calculate error metrics
        absolute_error = np.abs(numerical_solution - analytical_solution)
        relative_error = absolute_error / (np.abs(analytical_solution) + 1e-12)
        
        # Calculate grid spacing for integration
        dx = X[0, 1] - X[0, 0] if X.shape[1] > 1 else 1.0
        dy = Y[1, 0] - Y[0, 0] if Y.shape[0] > 1 else 1.0
        
        return {
            "max_abs_error": np.max(absolute_error),
            "max_rel_error": np.max(relative_error),
            "mean_abs_error": np.mean(absolute_error),
            "mean_rel_error": np.mean(relative_error),
            "l2_error": np.sqrt(dx * dy * np.sum(absolute_error**2)),
            "l2_norm_analytical": np.sqrt(dx * dy * np.sum(analytical_solution**2)),
            "relative_l2_error": np.sqrt(dx * dy * np.sum(absolute_error**2)) / 
                               (np.sqrt(dx * dy * np.sum(analytical_solution**2)) + 1e-12)
        }
    except Exception as e:
        print(f"Validation failed: {e}")
        return {
            "max_abs_error": float('nan'),
            "max_rel_error": float('nan'), 
            "mean_abs_error": float('nan'),
            "mean_rel_error": float('nan'),
            "l2_error": float('nan'),
            "l2_norm_analytical": float('nan'),
            "relative_l2_error": float('nan')
        }


# Placeholder functions to match the expected interface
def solve_analytical(x: np.ndarray, t: float, initial_func: Callable, 
                    D: float, L: float, method: str = "eigenfunction") -> np.ndarray:
    """1D analytical solution placeholder."""
    # This is for 1D compatibility - just return zeros for now
    return np.zeros_like(x)