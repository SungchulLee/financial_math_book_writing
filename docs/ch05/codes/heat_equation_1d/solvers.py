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