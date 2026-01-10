# ============================================================================
# heat_equation_2d/matrices.py
# ============================================================================
import numpy as np
import scipy.sparse as sparse
from typing import Tuple


def construct_2d_laplacian(Nx: int, Ny: int, dx: float, dy: float) -> sparse.csr_matrix:
    """
    Construct 2D discrete Laplacian operator using Kronecker products.
    
    Args:
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        dx: Grid spacing in x direction
        dy: Grid spacing in y direction
        
    Returns:
        2D Laplacian matrix in CSR format
    """
    # Identity matrices
    Ix = sparse.identity(Nx)
    Iy = sparse.identity(Ny)
    
    # 1D second derivative operators
    Dx = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / dx**2
    Dy = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)) / dy**2
    
    # 2D Laplacian using Kronecker products
    # Lx operates on x, keeps y unchanged: Lx ⊗ Iy
    # Ly operates on y, keeps x unchanged: Ix ⊗ Ly
    Lx = sparse.kron(Iy, Dx)
    Ly = sparse.kron(Dy, Ix)
    
    Laplacian = Lx + Ly
    return Laplacian.tocsr()


def construct_forward_euler_2d(Nx: int, Ny: int, rx: float, ry: float) -> sparse.csr_matrix:
    """
    Construct matrix for 2D Forward Euler method.
    
    Update rule: u^{n+1} = A @ u^n
    
    Args:
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        rx: Diffusion coefficient in x (D*dt/dx^2)
        ry: Diffusion coefficient in y (D*dt/dy^2)
        
    Returns:
        Forward Euler matrix
    """
    # Create Laplacian
    Laplacian = construct_2d_laplacian(Nx, Ny, 1.0, 1.0)  # Unit spacing, scaled by rx, ry
    
    # Scale by diffusion coefficients
    Laplacian_scaled = rx * sparse.kron(sparse.identity(Ny), 
                                       sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx))) + \
                      ry * sparse.kron(sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)), 
                                       sparse.identity(Nx))
    
    # Forward Euler: I + dt*L
    I = sparse.identity(Nx * Ny)
    A = I + Laplacian_scaled
    
    return A.tocsr()


def construct_backward_euler_2d(Nx: int, Ny: int, dx: float, dy: float, 
                                D: float, dt: float) -> sparse.csr_matrix:
    """
    Construct matrix for 2D Backward Euler method.
    
    Solve: A @ u^{n+1} = u^n
    
    Args:
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        dx: Grid spacing in x direction
        dy: Grid spacing in y direction
        D: Thermal diffusivity
        dt: Time step size
        
    Returns:
        Backward Euler matrix
    """
    # Create Laplacian
    Laplacian = construct_2d_laplacian(Nx, Ny, dx, dy)
    
    # Backward Euler: I - dt*D*L
    I = sparse.identity(Nx * Ny)
    A = I - D * dt * Laplacian
    
    return A.tocsr()


def construct_backward_matrix_2d(params):
    """Construct matrix for Backward Euler method."""
    Nx, Ny = params.Nx, params.Ny
    
    # Create 1D operators
    Ix, Iy = sparse.identity(Nx), sparse.identity(Ny)
    Dx = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / params.dx**2
    Dy = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)) / params.dy**2
    
    # 2D Laplacian using Kronecker products
    Lx = sparse.kron(Iy, Dx)
    Ly = sparse.kron(Dy, Ix)
    Laplacian = Lx + Ly
    
    # Backward Euler matrix: I - dt*D*L
    I = sparse.identity(Nx * Ny)
    A = I - params.D * params.dt * Laplacian
    
    return A.tocsr()



def construct_crank_nicolson_matrices_2d(params):
    """Construct matrices for Crank-Nicolson method."""
    Nx, Ny = params.Nx, params.Ny
    
    # Create Laplacian (same as backward Euler)
    Ix, Iy = sparse.identity(Nx), sparse.identity(Ny)
    Dx = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / params.dx**2
    Dy = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)) / params.dy**2
    Lx = sparse.kron(Iy, Dx)
    Ly = sparse.kron(Dy, Ix)
    Laplacian = Lx + Ly
    
    # Crank-Nicolson matrices
    I = sparse.identity(Nx * Ny)
    half_dt_D_L = 0.5 * params.D * params.dt * Laplacian
    A = I - half_dt_D_L  # Implicit
    B = I + half_dt_D_L  # Explicit
    
    return A.tocsr(), B.tocsr()


def construct_crank_nicolson_2d(Nx: int, Ny: int, dx: float, dy: float, 
                               D: float, dt: float) -> Tuple[sparse.csr_matrix, sparse.csr_matrix]:
    """
    Construct matrices for 2D Crank-Nicolson method.
    
    Solve: A @ u^{n+1} = B @ u^n
    
    Args:
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        dx: Grid spacing in x direction
        dy: Grid spacing in y direction
        D: Thermal diffusivity
        dt: Time step size
        
    Returns:
        Tuple of (A_matrix, B_matrix)
    """
    # Create Laplacian
    Laplacian = construct_2d_laplacian(Nx, Ny, dx, dy)
    
    # Crank-Nicolson matrices
    I = sparse.identity(Nx * Ny)
    half_dt_D_L = 0.5 * D * dt * Laplacian
    
    A = I - half_dt_D_L  # Implicit part
    B = I + half_dt_D_L  # Explicit part
    
    return A.tocsr(), B.tocsr()


def construct_adi_matrices(Nx: int, Ny: int, rx: float, ry: float) -> Tuple[sparse.csc_matrix, sparse.csc_matrix]:
    """
    Construct matrices for Alternating Direction Implicit (ADI) method.
    
    Args:
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        rx: Diffusion coefficient in x (D*dt/(2*dx^2))
        ry: Diffusion coefficient in y (D*dt/(2*dy^2))
        
    Returns:
        Tuple of (Ax_matrix, Ay_matrix) for ADI steps
    """
    # Matrices for x-direction solve (interior points only)
    main_x = (1 + 2 * rx) * np.ones(Nx - 2)
    off_x = -rx * np.ones(Nx - 3)
    Ax = sparse.diags([off_x, main_x, off_x], [-1, 0, 1], shape=(Nx-2, Nx-2))
    
    # Matrices for y-direction solve (interior points only)
    main_y = (1 + 2 * ry) * np.ones(Ny - 2)
    off_y = -ry * np.ones(Ny - 3)
    Ay = sparse.diags([off_y, main_y, off_y], [-1, 0, 1], shape=(Ny-2, Ny-2))
    
    return Ax.tocsc(), Ay.tocsc()


def apply_dirichlet_bc_2d(matrix: sparse.csr_matrix, Nx: int, Ny: int) -> sparse.csr_matrix:
    """
    Apply Dirichlet boundary conditions to a 2D matrix.
    
    Sets boundary nodes to identity (preserves boundary values).
    
    Args:
        matrix: Input matrix
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        
    Returns:
        Modified matrix with boundary conditions
    """
    matrix = matrix.copy()
    
    # Convert to LIL format for efficient modification
    matrix = matrix.tolil()
    
    # Apply boundary conditions
    for i in range(Nx):
        for j in range(Ny):
            idx = i * Ny + j
            
            # If on boundary, set row to identity
            if i == 0 or i == Nx-1 or j == 0 or j == Ny-1:
                matrix[idx, :] = 0
                matrix[idx, idx] = 1
    
    return matrix.tocsr()


def construct_neumann_bc_2d(Nx: int, Ny: int, dx: float, dy: float, 
                           D: float, dt: float, method: str = "backward") -> sparse.csr_matrix:
    """
    Construct matrix with Neumann (zero-flux) boundary conditions.
    
    Args:
        Nx: Number of grid points in x direction
        Ny: Number of grid points in y direction
        dx: Grid spacing in x direction
        dy: Grid spacing in y direction
        D: Thermal diffusivity
        dt: Time step size
        method: "forward", "backward", or "cn"
        
    Returns:
        Matrix with Neumann boundary conditions
    """
    if method == "forward":
        raise NotImplementedError("Neumann BC for Forward Euler 2D not implemented")
    elif method == "backward":
        A = construct_backward_euler_2d(Nx, Ny, dx, dy, D, dt)
    elif method == "cn":
        A, _ = construct_crank_nicolson_2d(Nx, Ny, dx, dy, D, dt)
    else:
        raise ValueError("Method must be 'forward', 'backward', or 'cn'")
    
    # Convert to LIL for modification
    A = A.tolil()
    
    # Apply Neumann BC: du/dn = 0 at boundaries
    # This is more complex in 2D and requires careful treatment
    # For now, we'll use a simplified approach
    
    for i in range(Nx):
        for j in range(Ny):
            idx = i * Ny + j
            
            # Boundary conditions (simplified - sets ghost points equal to interior)
            if i == 0 or i == Nx-1 or j == 0 or j == Ny-1:
                A[idx, :] = 0
                A[idx, idx] = 1
                
                # Add contributions from neighboring interior points
                # This is a simplified implementation
                if i == 0 and 1 < Nx-1:  # Left boundary
                    neighbor_idx = 1 * Ny + j
                    A[idx, neighbor_idx] = -1
                elif i == Nx-1 and Nx-2 > 0:  # Right boundary
                    neighbor_idx = (Nx-2) * Ny + j
                    A[idx, neighbor_idx] = -1
                
                if j == 0 and 1 < Ny-1:  # Bottom boundary
                    neighbor_idx = i * Ny + 1
                    A[idx, neighbor_idx] = -1
                elif j == Ny-1 and Ny-2 > 0:  # Top boundary
                    neighbor_idx = i * Ny + (Ny-2)
                    A[idx, neighbor_idx] = -1
    
    return A.tocsr()
    """Construct matrices for Crank-Nicolson method."""
    Nx, Ny = params.Nx, params.Ny
    
    # Create Laplacian (same as backward Euler)
    Ix, Iy = sparse.identity(Nx), sparse.identity(Ny)
    Dx = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / params.dx**2
    Dy = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)) / params.dy**2
    Lx = sparse.kron(Iy, Dx)
    Ly = sparse.kron(Dy, Ix)
    Laplacian = Lx + Ly
    
    # Crank-Nicolson matrices
    I = sparse.identity(Nx * Ny)
    half_dt_D_L = 0.5 * params.D * params.dt * Laplacian
    A = I - half_dt_D_L  # Implicit
    B = I + half_dt_D_L  # Explicit
    
    return A.tocsr(), B.tocsr()