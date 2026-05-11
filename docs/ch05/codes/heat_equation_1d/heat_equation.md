# Heat Equation

## Background

Heat Equation

Educational script demonstrating heat equation concepts.

---

## Code

```python
"""
Heat Equation

Educational script demonstrating heat equation concepts.
"""

# ============================================================================
# heat_equation_1d/heat_equation.py
# ============================================================================
import numpy as np
from typing import Optional, Callable, Dict
from .grid import create_grid
from .initial_conditions import step_function, gaussian_pulse, sine_wave
from .solvers import solve_forward_euler, solve_backward_euler, solve_crank_nicolson, compare_methods
from .analytical import solve_analytical, validate_against_analytical
from .plotting import plot_solution, plot_method_comparison, plot_with_analytical


class HeatEquation1D:
    """
    Lightweight wrapper class for 1D heat equation solver.
    
    All heavy lifting is done by pure functions. This class just provides
    a convenient interface and stores state for easy plotting/analysis.
    """
    
    def __init__(self, L: float = 1.0, T: float = 0.1, Nx: int = 100, 
                 Nt: int = 1000, D: float = 0.01):
        """
        Initialize heat equation parameters.
        
        Args:
            L: Length of domain
            T: Total simulation time
            Nx: Number of spatial grid points
            Nt: Number of time steps
            D: Thermal diffusivity
        """
        # Create grid using pure function
        self.params = create_grid(L, T, Nx, Nt, D)
        
        # State variables
        self.u_initial: Optional[np.ndarray] = None
        self.u_current: Optional[np.ndarray] = None
        self.last_method: Optional[str] = None
        self.initial_func: Optional[Callable] = None
    
    @property
    def x(self) -> np.ndarray:
        """Spatial grid points."""
        return self.params.x
    
    @property
    def coeff(self) -> float:
        """Diffusion coefficient."""
        return self.params.coeff
    
    def set_initial_condition(self, condition_type: str = "step", **kwargs) -> None:
        """
        Set initial condition using predefined functions.
        
        Args:
            condition_type: "step", "gaussian", "sine", or "custom"
            **kwargs: Parameters for the chosen condition type
        """
        if condition_type == "step":
            self.u_initial = step_function(self.x, L=self.params.L, **kwargs)
            self.initial_func = lambda x: step_function(x, L=self.params.L, **kwargs)
            
        elif condition_type == "gaussian":
            self.u_initial = gaussian_pulse(self.x, L=self.params.L, **kwargs)
            self.initial_func = lambda x: gaussian_pulse(x, L=self.params.L, **kwargs)
            
        elif condition_type == "sine":
            self.u_initial = sine_wave(self.x, L=self.params.L, **kwargs)
            self.initial_func = lambda x: sine_wave(x, L=self.params.L, **kwargs)
            
        elif condition_type == "custom":
            func = kwargs.get("func")
            if func is None:
                raise ValueError("Custom condition requires 'func' parameter")
            self.u_initial = func(self.x)
            self.initial_func = func
            
        else:
            raise ValueError("condition_type must be 'step', 'gaussian', 'sine', or 'custom'")
        
        self.u_current = self.u_initial.copy()
    
    def solve(self, method: str = "forward") -> np.ndarray:
        """
        Solve the heat equation using specified method.
        
        Args:
            method: "forward", "backward", or "cn" (Crank-Nicolson)
            
        Returns:
            Final solution array
        """
        if self.u_initial is None:
            raise ValueError("Set initial condition first using set_initial_condition()")
        
        # Call appropriate pure function
        if method == "forward":
            self.u_current = solve_forward_euler(self.u_initial, self.coeff, self.params.Nt)
        elif method == "backward":
            self.u_current = solve_backward_euler(self.u_initial, self.coeff, self.params.Nt)
        elif method == "cn":
            self.u_current = solve_crank_nicolson(self.u_initial, self.coeff, self.params.Nt)
        else:
            raise ValueError("Method must be 'forward', 'backward', or 'cn'")
        
        self.last_method = method
        return self.u_current
    
    def compare_all_methods(self) -> Dict[str, np.ndarray]:
        """
        Compare all numerical methods.
        
        Returns:
            Dictionary with results from each method
        """
        if self.u_initial is None:
            raise ValueError("Set initial condition first")
        
        return compare_methods(self.u_initial, self.coeff, self.params.Nt)
    
    def get_analytical_solution(self, method: str = "eigenfunction") -> np.ndarray:
        """
        Get analytical solution at final time.
        
        Args:
            method: "eigenfunction", "heat_kernel", or "fourier"
            
        Returns:
            Analytical solution array
        """
        if self.initial_func is None:
            raise ValueError("Initial function not available for analytical solution")
        
        return solve_analytical(self.x, self.params.T, self.initial_func, 
                              self.params.D, self.params.L, method)
    
    def validate_solution(self, analytical_method: str = "eigenfunction") -> Dict:
        """
        Validate current solution against analytical solution.
        
        Args:
            analytical_method: Analytical method to use for comparison
            
        Returns:
            Dictionary with validation metrics
        """
        if self.u_current is None or self.initial_func is None:
            raise ValueError("Solve the equation first and ensure initial_func is available")
        
        return validate_against_analytical(
            self.u_current, self.x, self.params.T, self.initial_func,
            self.params.D, self.params.L, analytical_method
        )
    
    def plot(self, show_analytical: bool = False, analytical_method: str = "eigenfunction") -> None:
        """
        Plot the solution.
        
        Args:
            show_analytical: Whether to include analytical solution
            analytical_method: Analytical method to use if show_analytical=True
        """
        if self.u_current is None or self.u_initial is None:
            raise ValueError("Solve the equation first")
        
        if show_analytical and self.initial_func is not None:
            plot_with_analytical(
                self.x, self.u_current, self.params.T, self.initial_func,
                self.params.D, self.params.L, self.last_method, analytical_method
            )
        else:
            plot_solution(self.x, self.u_initial, self.u_current, self.last_method)
    
    def plot_method_comparison(self) -> None:
        """Plot comparison of all methods."""
        if self.u_initial is None:
            raise ValueError("Set initial condition first")
        
        results = self.compare_all_methods()
        plot_method_comparison(self.x, self.u_initial, results)
    
    def reset(self) -> None:
        """Reset to initial condition."""
        if self.u_initial is not None:
            self.u_current = self.u_initial.copy()
    
    def info(self) -> Dict:
        """Get information about current setup."""
        return {
            "domain_length": self.params.L,
            "total_time": self.params.T,
            "spatial_points": self.params.Nx,
            "time_steps": self.params.Nt,
            "diffusivity": self.params.D,
            "spatial_step": self.params.dx,
            "time_step": self.params.dt,
            "diffusion_coefficient": self.params.coeff,
            "has_initial_condition": self.u_initial is not None,
            "last_method": self.last_method,
            "stability_parameter": self.params.coeff
        }


# Convenience function for quick solving
def solve_heat_equation(initial_condition: str = "step", method: str = "forward",
                       L: float = 1.0, T: float = 0.1, Nx: int = 100, 
                       Nt: int = 1000, D: float = 0.01, **ic_kwargs) -> Dict:
    """
    Convenience function to solve heat equation with one function call.
    
    Args:
        initial_condition: Type of initial condition
        method: Numerical method
        L, T, Nx, Nt, D: Problem parameters
        **ic_kwargs: Parameters for initial condition
        
    Returns:
        Dictionary with solution and metadata
    """
    # Create solver
    solver = HeatEquation1D(L, T, Nx, Nt, D)
    
    # Set initial condition
    solver.set_initial_condition(initial_condition, **ic_kwargs)
    
    # Solve
    solution = solver.solve(method)
    
    # Return everything
    return {
        "x": solver.x,
        "u_initial": solver.u_initial,
        "u_final": solution,
        "method": method,
        "params": solver.params,
        "solver": solver  # Return solver for further analysis
    }


# Example usage
if __name__ == "__main__":
    # Method 1: Using the class
    heat = HeatEquation1D(L=1.0, T=0.1, Nx=50, Nt=500, D=0.01)
    heat.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    solution = heat.solve("cn")
    heat.plot(show_analytical=True)
    
    # Method 2: Using convenience function
    result = solve_heat_equation("gaussian", "backward", center=0.5, width=0.1)
    result["solver"].plot()
    
    # Method 3: Direct function calls (most flexible)
    from .grid import create_grid
    from .initial_conditions import step_function
    from .solvers import solve_crank_nicolson
    from .plotting import plot_solution
    
    params = create_grid(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    u_init = step_function(params.x, L=params.L)
    u_final = solve_crank_nicolson(u_init, params.coeff, params.Nt)
    plot_solution(params.x, u_init, u_final, "crank_nicolson")
```

## Exercises

**Exercise 1.**
Using the `HeatEquation1D` class with a step function initial condition ($u = 1$ on $[0.4, 0.6]$, zero elsewhere) on $[0, 1]$, explain qualitatively what the solution looks like at $t = 0.1$ with $D = 0.01$. Why does the step smooth out?

??? success "Solution to Exercise 1"
    At $t = 0.1$, the sharp step function has diffused into a smooth bell-shaped curve centered around $x = 0.5$. The peak value is less than 1, and the tails extend beyond $[0.4, 0.6]$.

    The smoothing occurs because the heat equation describes diffusion: heat flows from hot regions (the step) to cold regions (the zero background). Mathematically, $\partial u / \partial t = D\,\partial^2 u / \partial x^2$ means the rate of change is proportional to the curvature. At the edges of the step, the large curvature drives rapid change, smoothing the discontinuity.

---

**Exercise 2.**
Compare the three numerical methods (Forward Euler, Backward Euler, Crank-Nicolson) in terms of their truncation error order and stability properties.

??? success "Solution to Exercise 2"
    | Method | Time accuracy | Space accuracy | Stability |
    |--------|:---:|:---:|---|
    | Forward Euler | $O(\Delta t)$ | $O(\Delta x^2)$ | Conditionally stable: $\alpha \le 1/2$ |
    | Backward Euler | $O(\Delta t)$ | $O(\Delta x^2)$ | Unconditionally stable |
    | Crank-Nicolson | $O(\Delta t^2)$ | $O(\Delta x^2)$ | Unconditionally stable |

    Crank-Nicolson is the most accurate due to its second-order time accuracy, achieved by averaging the explicit and implicit discretizations. Backward Euler is unconditionally stable but introduces more numerical diffusion. Forward Euler is cheapest per step but requires a small time step.

---

**Exercise 3.**
The `solve` method accepts method strings `"forward"`, `"backward"`, and `"cn"`. Write pseudocode for the Crank-Nicolson update step: given $\mathbf{u}^n$, show how to compute $\mathbf{u}^{n+1}$.

??? success "Solution to Exercise 3"
    Crank-Nicolson averages the explicit and implicit discretizations:

    $$
    \mathbf{u}^{n+1} - \frac{\alpha}{2}\,L\,\mathbf{u}^{n+1} = \mathbf{u}^n + \frac{\alpha}{2}\,L\,\mathbf{u}^n
    $$

    where $L$ is the tridiagonal second-difference matrix. In matrix form: $A\,\mathbf{u}^{n+1} = B\,\mathbf{u}^n$, where $A = I - (\alpha/2)\,L$ and $B = I + (\alpha/2)\,L$. Pseudocode:

    1. Compute right-hand side: `rhs = B @ u_n`
    2. Solve the linear system: `u_{n+1} = solve(A, rhs)`
    3. Apply Dirichlet boundary conditions: `u_{n+1}[0] = u_{n+1}[-1] = 0`

---

**Exercise 4.**
Explain what `validate_solution("eigenfunction")` computes internally. Why might the eigenfunction method give a poor reference solution for a discontinuous initial condition with a small number of Fourier modes $N$?

??? success "Solution to Exercise 4"
    The method computes the eigenfunction expansion $u(x,t) = \sum_{n=1}^{N} A_n \sin(n\pi x/L)\,e^{-D(n\pi/L)^2 t}$ and compares it to the numerical solution via error metrics (max error, $L^2$ error, etc.).

    For a discontinuous initial condition (like a step function), the Fourier sine coefficients $A_n$ decay as $O(1/n)$, which is slow. With a finite number of modes $N$, the Gibbs phenomenon produces oscillations of about 9% overshoot near the discontinuity. This makes the truncated eigenfunction expansion a poor approximation of the true solution near discontinuities, so a large $N$ (e.g., $N = 100$ or more) is necessary for accurate validation.
