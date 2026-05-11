# Solvers

## Background

This page presents the Python implementation for **Solvers**.

---

## Code

```python
"""
Solvers

Educational script demonstrating solvers concepts.
"""

# ============================================================================
# heat_equation_2d/solvers.py
# ============================================================================
import numpy as np
import scipy.sparse.linalg as spsolve
from .matrices import (
    construct_backward_matrix_2d,
    construct_crank_nicolson_matrices_2d,


if __name__ == "__main__":
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
```

## Exercises

**Exercise 1.**
Explain the Thomas algorithm for solving tridiagonal systems. What is its computational complexity compared to general Gaussian elimination?

??? success "Solution to Exercise 1"
    The Thomas algorithm solves $A\mathbf{x} = \mathbf{d}$ where $A$ is tridiagonal with sub-diagonal $a$, main diagonal $b$, and super-diagonal $c$.

    **Forward elimination**: For $i = 2, \ldots, n$: $w = a_{i-1}/b_{i-1}$, $b_i \leftarrow b_i - w c_{i-1}$, $d_i \leftarrow d_i - w d_{i-1}$.

    **Back substitution**: $x_n = d_n/b_n$; for $i = n-1, \ldots, 1$: $x_i = (d_i - c_i x_{i+1})/b_i$.

    Total cost: $O(n)$ operations (specifically $5n - 4$ multiplications/divisions and $3n - 3$ additions). General Gaussian elimination costs $O(n^3)$, so the Thomas algorithm is dramatically faster for tridiagonal systems.

---

**Exercise 2.**
Compare the Forward Euler, Backward Euler, and Crank-Nicolson methods for the 2D heat equation in terms of stability and per-step cost.

??? success "Solution to Exercise 2"
    | Method | Stability | Per-step cost |
    |--------|-----------|---------------|
    | Forward Euler | Conditional: $r_x + r_y \le 1/2$ | $O(N_x N_y)$ explicit update |
    | Backward Euler | Unconditional | $O(N_x N_y)$ sparse solve |
    | Crank-Nicolson | Unconditional | $O(N_x N_y)$ sparse multiply + solve |

    The sparse solve for 2D problems costs more than the explicit update, but Backward Euler and Crank-Nicolson allow much larger time steps. Crank-Nicolson has the best accuracy ($O(\Delta t^2)$) among the three.

---

**Exercise 3.**
The ADI method splits the 2D problem into a sequence of 1D problems. Explain why this is advantageous over directly solving the full 2D implicit system.

??? success "Solution to Exercise 3"
    Direct 2D implicit methods require solving a linear system of size $N_x N_y$. Even with sparse solvers, the cost is $O((N_x N_y)^{3/2})$ for direct methods or requires iterative solvers.

    ADI reduces this to solving $N_y$ tridiagonal systems of size $N_x$ (x-sweep) plus $N_x$ tridiagonal systems of size $N_y$ (y-sweep). Each tridiagonal solve costs $O(N)$, so the total is $O(N_x N_y)$ -- the same as the explicit method but with unconditional stability. ADI also has better cache locality since it operates on rows/columns sequentially.

---

**Exercise 4.**
The `compare_2d_methods` function tries each method and catches exceptions. Why might Forward Euler fail while the other methods succeed?

??? success "Solution to Exercise 4"
    Forward Euler fails when the stability condition $r_x + r_y \le 1/2$ is violated. This happens when the time step $\Delta t$ is too large relative to the spatial discretization. The other methods (Backward Euler, Crank-Nicolson, ADI) are unconditionally stable, meaning they produce bounded solutions for any $\Delta t$.

    The `compare_2d_methods` function explicitly checks the stability condition before attempting Forward Euler and raises a `ValueError` if violated. The try-except block catches this and reports the failure while allowing the comparison to continue with the stable methods.
