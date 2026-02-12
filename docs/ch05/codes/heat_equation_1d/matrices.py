# ============================================================================
# heat_equation_1d/matrices.py
# ============================================================================
import numpy as np
from typing import Tuple


def construct_forward_euler_matrix(Nx: int, coeff: float) -> np.ndarray:
    """
    Construct matrix for Forward Euler method with Dirichlet BCs.
    
    Update rule: u^{n+1} = A @ u^n
    
    Args:
        Nx: Number of spatial grid points
        coeff: Diffusion coefficient (D*dt/dx^2)
        
    Returns:
        Forward Euler matrix A
    """
    A = np.zeros((Nx, Nx))
    
    # Dirichlet boundary conditions (identity rows)
    A[0, 0] = 1.0
    A[-1, -1] = 1.0
    
    # Interior points
    for i in range(1, Nx - 1):
        A[i, i - 1] = coeff
        A[i, i]     = 1 - 2 * coeff
        A[i, i + 1] = coeff
    
    return A


def construct_backward_euler_matrix(Nx: int, coeff: float) -> np.ndarray:
    """
    Construct matrix for Backward Euler method with Dirichlet BCs.
    
    Solve: A @ u^{n+1} = u^n
    
    Args:
        Nx: Number of spatial grid points
        coeff: Diffusion coefficient (D*dt/dx^2)
        
    Returns:
        Backward Euler matrix A
    """
    A = np.zeros((Nx, Nx))
    
    # Dirichlet boundary conditions
    A[0, 0] = 1.0
    A[-1, -1] = 1.0
    
    # Interior points
    for i in range(1, Nx - 1):
        A[i, i - 1] = -coeff
        A[i, i]     = 1 + 2 * coeff
        A[i, i + 1] = -coeff
    
    return A


def construct_crank_nicolson_matrices(Nx: int, coeff: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Construct matrices for Crank-Nicolson method with Dirichlet BCs.
    
    Solve: A @ u^{n+1} = B @ u^n
    
    Args:
        Nx: Number of spatial grid points
        coeff: Diffusion coefficient (D*dt/dx^2)
        
    Returns:
        Tuple of (A_matrix, B_matrix)
    """
    A = np.zeros((Nx, Nx))
    B = np.zeros((Nx, Nx))
    
    # Dirichlet boundary conditions
    A[0, 0] = B[0, 0] = 1.0
    A[-1, -1] = B[-1, -1] = 1.0
    
    # Interior points
    for i in range(1, Nx - 1):
        # A matrix (implicit part)
        A[i, i - 1] = -coeff / 2
        A[i, i]     = 1 + coeff
        A[i, i + 1] = -coeff / 2
        
        # B matrix (explicit part)
        B[i, i - 1] = coeff / 2
        B[i, i]     = 1 - coeff
        B[i, i + 1] = coeff / 2
    
    return A, B


def construct_theta_method_matrices(Nx: int, coeff: float, theta: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Construct matrices for theta method (generalized scheme).
    
    Solve: A @ u^{n+1} = B @ u^n
    
    theta = 0: Forward Euler
    theta = 1: Backward Euler  
    theta = 0.5: Crank-Nicolson
    
    Args:
        Nx: Number of spatial grid points
        coeff: Diffusion coefficient (D*dt/dx^2)
        theta: Implicitness parameter (0 to 1)
        
    Returns:
        Tuple of (A_matrix, B_matrix)
    """
    if not 0 <= theta <= 1:
        raise ValueError("theta must be between 0 and 1")
    
    A = np.zeros((Nx, Nx))
    B = np.zeros((Nx, Nx))
    
    # Dirichlet boundary conditions
    A[0, 0] = B[0, 0] = 1.0
    A[-1, -1] = B[-1, -1] = 1.0
    
    # Interior points
    for i in range(1, Nx - 1):
        # A matrix (implicit part)
        A[i, i - 1] = -theta * coeff
        A[i, i]     = 1 + 2 * theta * coeff
        A[i, i + 1] = -theta * coeff
        
        # B matrix (explicit part)
        B[i, i - 1] = (1 - theta) * coeff
        B[i, i]     = 1 - 2 * (1 - theta) * coeff
        B[i, i + 1] = (1 - theta) * coeff
    
    return A, B


def apply_dirichlet_bc(matrix: np.ndarray, left_val: float = 0.0, 
                       right_val: float = 0.0) -> np.ndarray:
    """
    Apply Dirichlet boundary conditions to a matrix.
    
    Args:
        matrix: Input matrix
        left_val: Left boundary value
        right_val: Right boundary value
        
    Returns:
        Modified matrix with boundary conditions
    """
    matrix = matrix.copy()
    
    # Left boundary
    matrix[0, :] = 0.0
    matrix[0, 0] = 1.0
    
    # Right boundary
    matrix[-1, :] = 0.0
    matrix[-1, -1] = 1.0
    
    return matrix


def construct_neumann_matrix(Nx: int, coeff: float, method: str = "forward") -> np.ndarray:
    """
    Construct matrix with Neumann (zero-flux) boundary conditions.
    
    Args:
        Nx: Number of spatial grid points
        coeff: Diffusion coefficient
        method: "forward", "backward", or "cn"
        
    Returns:
        Matrix with Neumann boundary conditions
    """
    if method == "forward":
        A = construct_forward_euler_matrix(Nx, coeff)
    elif method == "backward":
        A = construct_backward_euler_matrix(Nx, coeff)
    else:
        raise ValueError("Neumann BC only implemented for forward/backward Euler")
    
    # Modify boundary rows for Neumann BC (du/dx = 0)
    # Left boundary: u[0] = u[1]
    A[0, :] = 0.0
    A[0, 0] = -1.0
    A[0, 1] = 1.0
    
    # Right boundary: u[-1] = u[-2]
    A[-1, :] = 0.0
    A[-1, -1] = 1.0
    A[-1, -2] = -1.0
    
    return A