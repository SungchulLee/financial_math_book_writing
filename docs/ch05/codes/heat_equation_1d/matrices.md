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


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Write the Forward Euler matrix $A$ explicitly for $N_x = 5$ grid points with coefficient $\alpha = 0.4$. Verify that the boundary rows enforce Dirichlet conditions $u_0 = u_4 = 0$.

??? success "Solution to Exercise 1"
    The $5 \times 5$ matrix is

    $$
    A = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0.4 & 0.2 & 0.4 & 0 & 0 \\ 0 & 0.4 & 0.2 & 0.4 & 0 \\ 0 & 0 & 0.4 & 0.2 & 0.4 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix}
    $$

    The first row $[1, 0, 0, 0, 0]$ preserves $u_0^{n+1} = u_0^n = 0$, and the last row $[0, 0, 0, 0, 1]$ preserves $u_4^{n+1} = u_4^n = 0$. Interior rows implement the scheme $u_j^{n+1} = \alpha u_{j-1}^n + (1 - 2\alpha) u_j^n + \alpha u_{j+1}^n$.

---

**Exercise 2.**
Explain why the Backward Euler matrix requires solving a linear system $A\mathbf{u}^{n+1} = \mathbf{u}^n$ at each time step, whereas Forward Euler uses a simple matrix-vector product.

??? success "Solution to Exercise 2"
    Forward Euler is explicit: $\mathbf{u}^{n+1} = A_{\text{FE}}\,\mathbf{u}^n$, which is a direct matrix-vector multiplication.

    Backward Euler evaluates the spatial derivative at time level $n+1$: $\mathbf{u}^{n+1} = \mathbf{u}^n + \alpha\,L\,\mathbf{u}^{n+1}$, which rearranges to $(I - \alpha L)\,\mathbf{u}^{n+1} = \mathbf{u}^n$. The matrix $A_{\text{BE}} = I - \alpha L$ appears on the left-hand side, requiring a linear solve. This implicit coupling is what gives Backward Euler unconditional stability.

---

**Exercise 3.**
Show that the Crank-Nicolson scheme can be viewed as the $\theta$-method with $\theta = 1/2$. Write the general $\theta$-method update equation.

??? success "Solution to Exercise 3"
    The $\theta$-method is

    $$
    \mathbf{u}^{n+1} = \mathbf{u}^n + \alpha\bigl[(1-\theta)\,L\,\mathbf{u}^n + \theta\,L\,\mathbf{u}^{n+1}\bigr]
    $$

    Rearranging: $(I - \theta\alpha L)\,\mathbf{u}^{n+1} = (I + (1-\theta)\alpha L)\,\mathbf{u}^n$, i.e., $A\,\mathbf{u}^{n+1} = B\,\mathbf{u}^n$.

    Setting $\theta = 0$ recovers Forward Euler ($A = I$), $\theta = 1$ gives Backward Euler ($B = I$), and $\theta = 1/2$ gives Crank-Nicolson, which averages the explicit and implicit contributions equally.

---

**Exercise 4.**
Describe how Neumann (zero-flux) boundary conditions $\partial u/\partial x = 0$ at $x = 0$ and $x = L$ modify the boundary rows of the Forward Euler matrix compared to Dirichlet conditions.

??? success "Solution to Exercise 4"
    For Dirichlet conditions, the boundary rows are identity rows: $A_{0,:} = [1, 0, \ldots]$ and $A_{N-1,:} = [\ldots, 0, 1]$, which hold the boundary values fixed.

    For Neumann conditions $\partial u / \partial x = 0$, we use the ghost-point approximation: $(u_1 - u_{-1})/(2\Delta x) = 0$ implies $u_{-1} = u_1$. The boundary row becomes $A_{0,:} = [0, -1, 1, 0, \ldots]$, enforcing $u_0 = u_1$. Similarly, $A_{N-1,:} = [\ldots, 0, -1, 1]$ enforces $u_{N-1} = u_{N-2}$. This allows flux to reflect at the boundaries rather than being absorbed.
