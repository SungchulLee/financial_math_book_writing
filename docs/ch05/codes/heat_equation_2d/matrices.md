# Matrices

## Background

Matrices

Educational script demonstrating matrices concepts.

---

## Code

```python
"""
Matrices

Educational script demonstrating matrices concepts.
"""

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


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Explain how the 2D Laplacian is constructed using Kronecker products. If $D_x$ and $D_y$ are 1D second-derivative operators, write the formula for the 2D Laplacian $L$.

??? success "Solution to Exercise 1"
    The 2D Laplacian is $L = D_x \otimes I_y + I_x \otimes D_y$, where $\otimes$ denotes the Kronecker product.

    - $D_x \otimes I_y$: applies the $x$-derivative to each row (keeping $y$ fixed).
    - $I_x \otimes D_y$: applies the $y$-derivative to each column (keeping $x$ fixed).

    For $N_x = N_y = 3$ (interior only), the resulting $9 \times 9$ matrix has the 5-point stencil structure with $-4$ on the diagonal and $+1$ on the four off-diagonals corresponding to neighbors.

---

**Exercise 2.**
The ADI (Alternating Direction Implicit) method splits each time step into two half-steps. Describe the two half-steps and explain why each involves only a tridiagonal solve.

??? success "Solution to Exercise 2"
    **Half-step 1** (x-direction implicit, y-direction explicit): For each fixed $j$, solve $(I - \frac{r_x}{2}D_x^2)u^{n+1/2}_{:,j} = (I + \frac{r_y}{2}D_y^2)u^n_{:,j}$. This is a tridiagonal system of size $N_x - 2$ for each $j$.

    **Half-step 2** (y-direction implicit, x-direction explicit): For each fixed $i$, solve $(I - \frac{r_y}{2}D_y^2)u^{n+1}_{i,:} = (I + \frac{r_x}{2}D_x^2)u^{n+1/2}_{i,:}$. This is a tridiagonal system of size $N_y - 2$ for each $i$.

    Each half-step is implicit in only one direction, producing a tridiagonal (not block-tridiagonal) system that can be solved in $O(N)$ with the Thomas algorithm.

---

**Exercise 3.**
Why does `apply_dirichlet_bc_2d` set boundary rows to identity? What would happen if boundary conditions were not applied after constructing the Laplacian?

??? success "Solution to Exercise 3"
    Setting boundary rows to identity ($A_{k,:} = e_k^T$) ensures that boundary values remain unchanged during time stepping: $u_k^{n+1} = u_k^n$ for boundary node $k$.

    Without applying boundary conditions, the Laplacian stencil at boundary nodes would reference ghost points outside the domain (undefined values). The resulting linear system would either be inconsistent or produce physically meaningless solutions that violate the boundary conditions. The identity rows effectively decouple boundary nodes from the interior solve.

---

**Exercise 4.**
Compare the sparsity patterns of the 1D and 2D Backward Euler matrices. If $N_x = N_y = 50$, how many nonzero entries does the 2D matrix have approximately?

??? success "Solution to Exercise 4"
    The 1D Backward Euler matrix is tridiagonal with $N_x$ rows and at most $3N_x - 2$ nonzeros.

    The 2D Backward Euler matrix has $N = N_x \times N_y = 2500$ rows. Each interior row has 5 nonzeros (from the 5-point stencil), and boundary rows have 1 nonzero (identity). With approximately $(N_x - 2)(N_y - 2) = 2304$ interior nodes and 196 boundary nodes:

    $$
    \text{nnz} \approx 5 \times 2304 + 1 \times 196 = 11{,}716
    $$

    A dense matrix would have $2500^2 = 6{,}250{,}000$ entries, so the sparse matrix uses only about 0.19% of the storage. This dramatic sparsity is why sparse solvers are essential for 2D problems.
