# ============================================================================
# heat_equation_2d/solvers.py
# ============================================================================
import numpy as np
import scipy.sparse.linalg as spsolve
from .matrices import (
    construct_backward_matrix_2d,
    construct_crank_nicolson_matrices_2d,
)


def step_forward_euler_2d(u: np.ndarray, D: float, dt: float,
                         dx2: float, dy2: float) -> np.ndarray:
    """
    Perform one Forward Euler time step in 2D.
    
    Args:
        u: Current solution (2D array)
        D: Thermal diffusivity
        dt: Time step size
        dx2: dx^2
        dy2: dy^2
        
    Returns:
        Updated solution array
    """
    u_new = u.copy()
    
    # Compute second derivatives using finite differences
    u_xx = (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx2
    u_yy = (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dy2
    
    # Update interior points
    u_new[1:-1, 1:-1] += D * dt * (u_xx + u_yy)
    
    return u_new


def solve_forward_euler_2d(u_initial, params):
    """Solve using Forward Euler method."""
    # Check stability
    if params.rx + params.ry > 0.5:
        raise ValueError(f"Unstable: rx+ry = {params.rx+params.ry:.3f} > 0.5")
    
    u = u_initial.copy()
    dx2, dy2 = params.dx**2, params.dy**2
    
    for _ in range(params.Nt):
        u_new = u.copy()
        # Compute finite differences for interior points
        u_xx = (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx2
        u_yy = (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dy2
        u_new[1:-1, 1:-1] += params.D * params.dt * (u_xx + u_yy)
        u = u_new
    
    return u


def solve_backward_euler_2d(u_initial, params):
    """Solve using Backward Euler method."""
    A = construct_backward_matrix_2d(params)
    u = u_initial.copy()
    
    for _ in range(params.Nt):
        u_flat = u.reshape(-1)
        u_new_flat = spsolve.spsolve(A, u_flat)
        u = u_new_flat.reshape(params.Nx, params.Ny)
    
    return u


def solve_crank_nicolson_2d(u_initial, params):
    """Solve using Crank-Nicolson method."""
    A, B = construct_crank_nicolson_matrices_2d(params)
    u = u_initial.copy()
    
    for _ in range(params.Nt):
        u_flat = u.reshape(-1)
        rhs = B @ u_flat
        u_new_flat = spsolve.spsolve(A, rhs)
        u = u_new_flat.reshape(params.Nx, params.Ny)
    
    return u


def solve_crank_nicolson_adi_2d(u_initial, params):
    """
    Solve 2D heat equation using Crank-Nicolson ADI method.
    
    Args:
        u_initial: Initial condition (2D array)
        params: Grid parameters
        
    Returns:
        Final solution array (2D)
    """
    Nx, Ny = params.Nx, params.Ny
    rx, ry = params.rx / 2, params.ry / 2  # Half time steps for ADI
    
    u = u_initial.copy()
    
    for _ in range(params.Nt):
        # First half-step: solve in x-direction
        u_half = solve_adi_x_step(u, rx, ry)
        
        # Second half-step: solve in y-direction
        u = solve_adi_y_step(u_half, rx, ry)
    
    return u


def solve_adi_x_step(u, rx, ry):
    """
    Solve ADI x-direction step using tridiagonal solver.
    """
    Nx, Ny = u.shape
    u_half = np.zeros_like(u)
    
    # Apply boundary conditions (Dirichlet: u = 0 on boundaries)
    u_half[0, :] = 0
    u_half[-1, :] = 0
    u_half[:, 0] = 0
    u_half[:, -1] = 0
    
    # Solve for each row (y-constant lines)
    for j in range(1, Ny-1):
        # Set up tridiagonal system for x-direction
        a = -rx * np.ones(Nx-3)  # sub-diagonal
        b = (1 + 2*rx) * np.ones(Nx-2)  # main diagonal
        c = -rx * np.ones(Nx-3)  # super-diagonal
        
        # Right-hand side with y-direction explicit terms
        rhs = u[1:-1, j].copy()
        if j > 1:
            rhs += ry * (u[1:-1, j-1] - 2*u[1:-1, j] + u[1:-1, j+1])
        
        # Solve tridiagonal system
        u_half[1:-1, j] = solve_tridiagonal(a, b, c, rhs)
    
    return u_half


def solve_adi_y_step(u_half, rx, ry):
    """
    Solve ADI y-direction step using tridiagonal solver.
    """
    Nx, Ny = u_half.shape
    u_new = np.zeros_like(u_half)
    
    # Apply boundary conditions
    u_new[0, :] = 0
    u_new[-1, :] = 0
    u_new[:, 0] = 0
    u_new[:, -1] = 0
    
    # Solve for each column (x-constant lines)
    for i in range(1, Nx-1):
        # Set up tridiagonal system for y-direction
        a = -ry * np.ones(Ny-3)  # sub-diagonal
        b = (1 + 2*ry) * np.ones(Ny-2)  # main diagonal
        c = -ry * np.ones(Ny-3)  # super-diagonal
        
        # Right-hand side with x-direction explicit terms
        rhs = u_half[i, 1:-1].copy()
        if i > 1:
            rhs += rx * (u_half[i-1, 1:-1] - 2*u_half[i, 1:-1] + u_half[i+1, 1:-1])
        
        # Solve tridiagonal system
        u_new[i, 1:-1] = solve_tridiagonal(a, b, c, rhs)
    
    return u_new


def solve_tridiagonal(a, b, c, d):
    """
    Solve tridiagonal system using Thomas algorithm.
    
    Args:
        a: sub-diagonal (length n-1)
        b: main diagonal (length n)
        c: super-diagonal (length n-1)
        d: right-hand side (length n)
        
    Returns:
        Solution vector
    """
    n = len(d)
    
    # Forward elimination
    for i in range(1, n):
        w = a[i-1] / b[i-1]
        b[i] -= w * c[i-1]
        d[i] -= w * d[i-1]
    
    # Back substitution
    x = np.zeros(n)
    x[n-1] = d[n-1] / b[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]
    
    return x


def compare_2d_methods(u_initial, params):
    """Compare different 2D methods."""
    results = {}
    
    # Forward Euler
    try:
        results["Forward Euler"] = solve_forward_euler_2d(u_initial, params)
        print("✓ Forward Euler completed")
    except ValueError as e:
        print(f"✗ Forward Euler failed: {e}")
        results["Forward Euler"] = None
    except Exception as e:
        print(f"✗ Forward Euler failed: {e}")
        results["Forward Euler"] = None
    
    # Backward Euler
    try:
        results["Backward Euler"] = solve_backward_euler_2d(u_initial, params)
        print("✓ Backward Euler completed")
    except Exception as e:
        print(f"✗ Backward Euler failed: {e}")
        results["Backward Euler"] = None
    
    # Crank-Nicolson
    try:
        results["Crank-Nicolson"] = solve_crank_nicolson_2d(u_initial, params)
        print("✓ Crank-Nicolson completed")
    except Exception as e:
        print(f"✗ Crank-Nicolson failed: {e}")
        results["Crank-Nicolson"] = None
    
    # ADI (if you want to include it)
    try:
        results["ADI"] = solve_crank_nicolson_adi_2d(u_initial, params)
        print("✓ ADI completed")
    except Exception as e:
        print(f"✗ ADI failed: {e}")
        results["ADI"] = None
    
    return results

