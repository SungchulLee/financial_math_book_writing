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
# heat_equation_1d/solvers.py
# ============================================================================
import numpy as np
from typing import Tuple, Callable
from .matrices import (
    construct_forward_euler_matrix,
    construct_backward_euler_matrix, 
    construct_crank_nicolson_matrices,
    construct_theta_method_matrices


if __name__ == "__main__":
    )
    from .grid import check_stability


    def solve_forward_euler(u_initial: np.ndarray, coeff: float, Nt: int,
                           check_stable: bool = True) -> np.ndarray:
        """
        Solve using Forward Euler method.
    
        Args:
            u_initial: Initial condition
            coeff: Diffusion coefficient (D*dt/dx^2)
            Nt: Number of time steps
            check_stable: Whether to check stability condition
        
        Returns:
            Final solution array
        """
        if check_stable:
            check_stability(coeff, "forward")
    
        Nx = len(u_initial)
        A = construct_forward_euler_matrix(Nx, coeff)
    
        u = u_initial.copy()
        for _ in range(Nt):
            u = A @ u
    
        return u


    def solve_backward_euler(u_initial: np.ndarray, coeff: float, Nt: int) -> np.ndarray:
        """
        Solve using Backward Euler method.
    
        Args:
            u_initial: Initial condition
            coeff: Diffusion coefficient (D*dt/dx^2)
            Nt: Number of time steps
        
        Returns:
            Final solution array
        """
        Nx = len(u_initial)
        A = construct_backward_euler_matrix(Nx, coeff)
    
        u = u_initial.copy()
        for _ in range(Nt):
            u = np.linalg.solve(A, u)
    
        return u


    def solve_crank_nicolson(u_initial: np.ndarray, coeff: float, Nt: int) -> np.ndarray:
        """
        Solve using Crank-Nicolson method.
    
        Args:
            u_initial: Initial condition
            coeff: Diffusion coefficient (D*dt/dx^2)
            Nt: Number of time steps
        
        Returns:
            Final solution array
        """
        Nx = len(u_initial)
        A, B = construct_crank_nicolson_matrices(Nx, coeff)
    
        u = u_initial.copy()
        for _ in range(Nt):
            rhs = B @ u
            u = np.linalg.solve(A, rhs)
    
        return u


    def solve_theta_method(u_initial: np.ndarray, coeff: float, Nt: int, 
                          theta: float) -> np.ndarray:
        """
        Solve using theta method (generalized scheme).
    
        Args:
            u_initial: Initial condition
            coeff: Diffusion coefficient (D*dt/dx^2)
            Nt: Number of time steps
            theta: Implicitness parameter (0=explicit, 1=implicit, 0.5=Crank-Nicolson)
        
        Returns:
            Final solution array
        """
        if theta == 0:
            check_stability(coeff, "forward")
            return solve_forward_euler(u_initial, coeff, Nt, check_stable=False)
    
        Nx = len(u_initial)
        A, B = construct_theta_method_matrices(Nx, coeff, theta)
    
        u = u_initial.copy()
        for _ in range(Nt):
            rhs = B @ u
            u = np.linalg.solve(A, rhs)
    
        return u


    def solve_with_history(u_initial: np.ndarray, coeff: float, Nt: int,
                          method: str = "forward", save_every: int = 1) -> Tuple[np.ndarray, np.ndarray]:
        """
        Solve and save solution history.
    
        Args:
            u_initial: Initial condition
            coeff: Diffusion coefficient
            Nt: Number of time steps
            method: Solution method ("forward", "backward", "cn")
            save_every: Save solution every N time steps
        
        Returns:
            Tuple of (time_indices, solution_history)
        """
        Nx = len(u_initial)
        n_saves = Nt // save_every + 1
    
        # Pre-allocate solution history
        solution_history = np.zeros((n_saves, Nx))
        time_indices = np.zeros(n_saves, dtype=int)
    
        solution_history[0] = u_initial
        time_indices[0] = 0
    
        # Choose solver
        if method == "forward":
            check_stability(coeff, "forward")
            A = construct_forward_euler_matrix(Nx, coeff)
            step_func = lambda u: A @ u
        elif method == "backward":
            A = construct_backward_euler_matrix(Nx, coeff)
            step_func = lambda u: np.linalg.solve(A, u)
        elif method == "cn":
            A, B = construct_crank_nicolson_matrices(Nx, coeff)
            step_func = lambda u: np.linalg.solve(A, B @ u)
        else:
            raise ValueError("Method must be 'forward', 'backward', or 'cn'")
    
        u = u_initial.copy()
        save_idx = 1
    
        for t_step in range(1, Nt + 1):
            u = step_func(u)
        
            if t_step % save_every == 0:
                solution_history[save_idx] = u
                time_indices[save_idx] = t_step
                save_idx += 1
    
        return time_indices[:save_idx], solution_history[:save_idx]


    def solve_adaptive_timestep(u_initial: np.ndarray, coeff_func: Callable, 
                               T: float, dt_initial: float = None,
                               method: str = "forward", tolerance: float = 1e-6) -> Tuple[np.ndarray, np.ndarray]:
        """
        Solve with adaptive time stepping (basic implementation).
    
        Args:
            u_initial: Initial condition
            coeff_func: Function that returns coeff given current dt
            T: Final time
            dt_initial: Initial time step
            method: Solution method
            tolerance: Error tolerance for adaptation
        
        Returns:
            Tuple of (time_array, final_solution)
        """
        # This is a simplified adaptive scheme - in practice, you'd want more sophisticated error estimation
        if dt_initial is None:
            dt_initial = T / 1000
    
        t = 0.0
        dt = dt_initial
        u = u_initial.copy()
        time_history = [0.0]
    
        while t < T:
            dt = min(dt, T - t)  # Don't overshoot final time
            coeff = coeff_func(dt)
        
            if method == "forward":
                check_stability(coeff, "forward")
                u_new = solve_forward_euler(u, coeff, 1, check_stable=False)
            elif method == "backward":
                u_new = solve_backward_euler(u, coeff, 1)
            else:
                u_new = solve_crank_nicolson(u, coeff, 1)
        
            # Simple error estimation (compare with half-step)
            coeff_half = coeff_func(dt / 2)
            u_half1 = solve_forward_euler(u, coeff_half, 1, check_stable=False) if method == "forward" else u_new
            u_half2 = solve_forward_euler(u_half1, coeff_half, 1, check_stable=False) if method == "forward" else u_new
        
            error = np.max(np.abs(u_new - u_half2))
        
            if error < tolerance or dt <= dt_initial / 1000:  # Accept step
                u = u_new
                t += dt
                time_history.append(t)
                if error < tolerance / 10:  # Increase time step
                    dt = min(dt * 1.2, dt_initial * 2)
            else:  # Reject step and reduce time step
                dt = dt * 0.5
    
        return np.array(time_history), u


    def compare_methods(u_initial: np.ndarray, coeff: float, Nt: int) -> dict:
        """
        Compare all three methods and return results.
    
        Args:
            u_initial: Initial condition
            coeff: Diffusion coefficient
            Nt: Number of time steps
        
        Returns:
            Dictionary with results from each method
        """
        results = {}
    
        # Forward Euler (check stability first)
        try:
            check_stability(coeff, "forward")
            results["forward"] = solve_forward_euler(u_initial, coeff, Nt)
        except ValueError as e:
            results["forward"] = f"Unstable: {e}"
    
        # Backward Euler
        results["backward"] = solve_backward_euler(u_initial, coeff, Nt)
    
        # Crank-Nicolson
        results["crank_nicolson"] = solve_crank_nicolson(u_initial, coeff, Nt)
    
        return results
```

## Exercises

**Exercise 1.**
Describe the computational cost per time step for Forward Euler, Backward Euler, and Crank-Nicolson on a grid with $N_x$ points. Which method is cheapest per step, and which is most expensive?

??? success "Solution to Exercise 1"

    - **Forward Euler**: matrix-vector product $A\mathbf{u}$, costing $O(N_x)$ operations since $A$ is tridiagonal. This is the cheapest.
    - **Backward Euler**: solve $A\mathbf{u}^{n+1} = \mathbf{u}^n$. For a tridiagonal system, the Thomas algorithm costs $O(N_x)$, though with a larger constant than the explicit multiplication.
    - **Crank-Nicolson**: compute $\mathbf{b} = B\mathbf{u}^n$ (one tridiagonal multiply) then solve $A\mathbf{u}^{n+1} = \mathbf{b}$ (one tridiagonal solve). Total cost is $O(N_x)$ but with the largest constant of the three.

    All are $O(N_x)$ per step, but Forward Euler has the smallest constant. However, Forward Euler may require many more time steps due to its stability restriction.

---

**Exercise 2.**
The `solve_with_history` function stores the solution every `save_every` time steps. If $N_t = 10{,}000$ and `save_every = 100`, how many snapshots are stored? What is the memory requirement in terms of $N_x$?

??? success "Solution to Exercise 2"
    The number of snapshots is $N_t / \text{save\_every} + 1 = 10{,}000/100 + 1 = 101$ (including the initial condition).

    Each snapshot is a vector of length $N_x$, so the total memory is $101 \times N_x$ floating-point numbers. For $N_x = 1000$ and 8-byte doubles, this is $101 \times 1000 \times 8 = 808{,}000$ bytes $\approx 0.8$ MB.

---

**Exercise 3.**
Explain why the $\theta$-method with $\theta = 0$ reduces to Forward Euler and $\theta = 1$ reduces to Backward Euler. For what value of $\theta$ is the method second-order in time?

??? success "Solution to Exercise 3"
    The $\theta$-method is $\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta t[\theta F(\mathbf{u}^{n+1}) + (1-\theta)F(\mathbf{u}^n)]$ where $F(\mathbf{u}) = D L\mathbf{u}$.

    - $\theta = 0$: only the explicit term remains, giving $\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta t\,F(\mathbf{u}^n)$ (Forward Euler).
    - $\theta = 1$: only the implicit term remains, giving $\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta t\,F(\mathbf{u}^{n+1})$ (Backward Euler).
    - $\theta = 1/2$: the trapezoidal rule, i.e., Crank-Nicolson, which is second-order in time because the local truncation error of the trapezoidal rule is $O(\Delta t^3)$.

---

**Exercise 4.**
The `compare_methods` function catches a `ValueError` when Forward Euler is unstable. Explain how one could modify the comparison to still include Forward Euler results by automatically adjusting $N_t$ to satisfy the stability condition.

??? success "Solution to Exercise 4"
    Given $\alpha = D\Delta t / \Delta x^2 \le 0.5$, the maximum stable time step is $\Delta t_{\max} = 0.5\,\Delta x^2 / D$. The minimum number of time steps is $N_t^{\min} = \lceil T / \Delta t_{\max} \rceil$.

    The modification would:

    1. Check if the given $\alpha > 0.5$.
    2. If so, compute $N_t^{\text{stable}} = \lceil T \cdot D / (0.5 \Delta x^2) \rceil$.
    3. Re-solve Forward Euler with the larger $N_t^{\text{stable}}$.
    4. Report that the time step was adjusted for stability.

    This ensures a fair comparison: all methods solve to the same final time $T$, but Forward Euler uses more (smaller) steps when necessary.
