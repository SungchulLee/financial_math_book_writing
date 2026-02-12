# ============================================================================
# heat_equation_2d/wrapper.py
# ============================================================================
import numpy as np
from typing import Optional, Callable, Dict, Tuple, List
from .grid import create_2d_grid, Grid2DParams, get_stability_info
from .initial_conditions import (
    step_function_2d, gaussian_pulse_2d, circular_pulse_2d, sine_wave_2d,
    multiple_hotspots_2d, ring_pattern_2d, custom_function_2d, zero_initial_condition_2d
)
from .solvers import (
    solve_forward_euler_2d, solve_backward_euler_2d, solve_crank_nicolson_2d,
    solve_crank_nicolson_adi_2d
)
from .analytical import solve_analytical_2d, validate_against_analytical_2d
from .plotting import plot_2d_solution, plot_method_comparison_2d, plot_2d_evolution


class HeatEquation2D:
    """
    Lightweight wrapper class for 2D heat equation solver.
    
    All heavy lifting is done by pure functions. This class just provides
    a convenient interface and stores state for easy plotting/analysis.
    """
    
    def __init__(self, Lx: float = 1.0, Ly: float = 1.0, T: float = 0.1, 
                 Nx: int = 50, Ny: int = 50, Nt: int = 1000, D: float = 0.01):
        """
        Initialize 2D heat equation parameters.
        
        Args:
            Lx: Length of domain in x direction
            Ly: Length of domain in y direction
            T: Total simulation time
            Nx: Number of spatial grid points in x
            Ny: Number of spatial grid points in y
            Nt: Number of time steps
            D: Thermal diffusivity
        """
        # Create grid using pure function
        self.params = create_2d_grid(Lx, Ly, T, Nx, Ny, Nt, D)
        
        # State variables
        self.u_initial: Optional[np.ndarray] = None
        self.u_current: Optional[np.ndarray] = None
        self.last_method: Optional[str] = None
        self.initial_func: Optional[Callable] = None
    
    @property
    def x(self) -> np.ndarray:
        """Spatial grid points in x direction."""
        return self.params.x
    
    @property
    def y(self) -> np.ndarray:
        """Spatial grid points in y direction."""
        return self.params.y
    
    @property
    def X(self) -> np.ndarray:
        """2D meshgrid X coordinates."""
        return self.params.X
    
    @property
    def Y(self) -> np.ndarray:
        """2D meshgrid Y coordinates."""
        return self.params.Y
    
    @property
    def rx(self) -> float:
        """Diffusion coefficient in x direction."""
        return self.params.rx
    
    @property
    def ry(self) -> float:
        """Diffusion coefficient in y direction."""
        return self.params.ry
    
    def set_initial_condition(self, condition_type: str = "step", **kwargs) -> None:
        """
        Set initial condition using predefined functions.
        
        Args:
            condition_type: "step", "gaussian", "circular", "sine", "hotspots", 
                           "ring", "zero", or "custom"
            **kwargs: Parameters for the chosen condition type
        """
        if condition_type == "step":
            self.u_initial = step_function_2d(
                self.X, self.Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            self.initial_func = lambda X, Y: step_function_2d(
                X, Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            
        elif condition_type == "gaussian":
            self.u_initial = gaussian_pulse_2d(
                self.X, self.Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            self.initial_func = lambda X, Y: gaussian_pulse_2d(
                X, Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            
        elif condition_type == "circular":
            self.u_initial = circular_pulse_2d(
                self.X, self.Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            self.initial_func = lambda X, Y: circular_pulse_2d(
                X, Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            
        elif condition_type == "sine":
            self.u_initial = sine_wave_2d(
                self.X, self.Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            self.initial_func = lambda X, Y: sine_wave_2d(
                X, Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            
        elif condition_type == "hotspots":
            self.u_initial = multiple_hotspots_2d(
                self.X, self.Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            self.initial_func = lambda X, Y: multiple_hotspots_2d(
                X, Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            
        elif condition_type == "ring":
            self.u_initial = ring_pattern_2d(
                self.X, self.Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            self.initial_func = lambda X, Y: ring_pattern_2d(
                X, Y, Lx=self.params.Lx, Ly=self.params.Ly, **kwargs
            )
            
        elif condition_type == "zero":
            self.u_initial = zero_initial_condition_2d(self.X, self.Y)
            self.initial_func = lambda X, Y: zero_initial_condition_2d(X, Y)
            
        elif condition_type == "custom":
            func = kwargs.get("func")
            if func is None:
                raise ValueError("Custom condition requires 'func' parameter")
            self.u_initial = custom_function_2d(self.X, self.Y, func)
            self.initial_func = func
            
        else:
            raise ValueError(
                "condition_type must be 'step', 'gaussian', 'circular', 'sine', "
                "'hotspots', 'ring', 'zero', or 'custom'"
            )
        
        self.u_current = self.u_initial.copy()
    
    def solve(self, method: str = "backward") -> np.ndarray:
        """
        Solve the 2D heat equation using specified method.
        
        Args:
            method: "forward", "backward", "cn" (Crank-Nicolson), or "adi"
            
        Returns:
            Final solution array (2D)
        """
        if self.u_initial is None:
            raise ValueError("Set initial condition first using set_initial_condition()")
        
        # Call appropriate pure function
        if method == "forward":
            self.u_current = solve_forward_euler_2d(
                self.u_initial, self.params, self.params.Nt
            )
        elif method == "backward":
            self.u_current = solve_backward_euler_2d(
                self.u_initial, self.params, self.params.Nt
            )
        elif method == "cn":
            self.u_current = solve_crank_nicolson_2d(
                self.u_initial, self.params, self.params.Nt
            )
        elif method == "adi":
            self.u_current = solve_crank_nicolson_adi_2d(
                self.u_initial, self.params, self.params.Nt
            )
        else:
            raise ValueError("Method must be 'forward', 'backward', 'cn', or 'adi'")
        
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
        
        results = {}
        
        # Try Forward Euler (check stability first)
        stability_info = get_stability_info(self.params)
        if stability_info["is_stable_forward"]:
            try:
                results["forward"] = solve_forward_euler_2d(
                    self.u_initial, self.params, self.params.Nt
                )
            except Exception as e:
                results["forward"] = f"Error: {str(e)}"
        else:
            results["forward"] = "Unstable: rx + ry > 0.5"
        
        # Backward Euler
        try:
            results["backward"] = solve_backward_euler_2d(
                self.u_initial, self.params, self.params.Nt
            )
        except Exception as e:
            results["backward"] = f"Error: {str(e)}"
        
        # Crank-Nicolson
        try:
            results["cn"] = solve_crank_nicolson_2d(
                self.u_initial, self.params, self.params.Nt
            )
        except Exception as e:
            results["cn"] = f"Error: {str(e)}"
        
        # ADI (if implemented)
        try:
            results["adi"] = solve_crank_nicolson_adi_2d(
                self.u_initial, self.params, self.params.Nt
            )
        except Exception as e:
            results["adi"] = f"Error: {str(e)}"
        
        return results
    
    def get_analytical_solution(self, method: str = "eigenfunction") -> np.ndarray:
        """
        Get analytical solution at final time.
        
        Args:
            method: "eigenfunction", "heat_kernel", or "fourier"
            
        Returns:
            Analytical solution array (2D)
        """
        if self.initial_func is None:
            raise ValueError("Initial function not available for analytical solution")
        
        return solve_analytical_2d(
            self.X, self.Y, self.params.T, self.initial_func, 
            self.params.D, self.params.Lx, self.params.Ly, method
        )
    
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
        
        return validate_against_analytical_2d(
            self.u_current, self.X, self.Y, self.params.T, self.initial_func,
            self.params.D, self.params.Lx, self.params.Ly, analytical_method
        )
    
    def plot(self, show_analytical: bool = False, 
             analytical_method: str = "eigenfunction", 
             plot_type: str = "surface") -> None:
        """
        Plot the 2D solution.
        
        Args:
            show_analytical: Whether to include analytical solution
            analytical_method: Analytical method to use if show_analytical=True
            plot_type: "surface", "contour", or "both"
        """
        if self.u_current is None or self.u_initial is None:
            raise ValueError("Solve the equation first")
        
        if show_analytical and self.initial_func is not None:
            analytical_solution = self.get_analytical_solution(analytical_method)
            plot_2d_solution(
                self.X, self.Y, self.u_current, self.u_initial,
                self.last_method, plot_type, analytical_solution
            )
        else:
            plot_2d_solution(
                self.X, self.Y, self.u_current, self.u_initial,
                self.last_method, plot_type
            )
    
    def plot_method_comparison(self, plot_type: str = "contour") -> None:
        """
        Plot comparison of all methods.
        
        Args:
            plot_type: "surface", "contour", or "both"
        """
        if self.u_initial is None:
            raise ValueError("Set initial condition first")
        
        results = self.compare_all_methods()
        plot_method_comparison_2d(
            self.X, self.Y, self.u_initial, results, plot_type
        )
    
    def plot_evolution(self, n_snapshots: int = 6, 
                      plot_type: str = "contour") -> None:
        """
        Plot evolution of the solution over time.
        
        Args:
            n_snapshots: Number of time snapshots to show
            plot_type: "surface", "contour", or "both"
        """
        if self.u_initial is None:
            raise ValueError("Set initial condition first")
        
        # This would require modifying solvers to return history
        # For now, just plot initial and final
        self.plot(plot_type=plot_type)
    
    def reset(self) -> None:
        """Reset to initial condition."""
        if self.u_initial is not None:
            self.u_current = self.u_initial.copy()
    
    def get_stability_info(self) -> Dict:
        """Get stability information for current parameters."""
        return get_stability_info(self.params)
    
    def info(self) -> Dict:
        """Get information about current setup."""
        stability_info = self.get_stability_info()
        
        return {
            "domain_size": (self.params.Lx, self.params.Ly),
            "total_time": self.params.T,
            "spatial_points": (self.params.Nx, self.params.Ny),
            "time_steps": self.params.Nt,
            "diffusivity": self.params.D,
            "spatial_steps": (self.params.dx, self.params.dy),
            "time_step": self.params.dt,
            "diffusion_coefficients": (self.params.rx, self.params.ry),
            "stability_parameter": stability_info["stability_parameter"],
            "is_stable_forward": stability_info["is_stable_forward"],
            "has_initial_condition": self.u_initial is not None,
            "last_method": self.last_method,
            "grid_shape": (self.params.Nx, self.params.Ny)
        }


# Convenience function for quick solving
def solve_heat_equation_2d(initial_condition: str = "step", method: str = "backward",
                          Lx: float = 1.0, Ly: float = 1.0, T: float = 0.1, 
                          Nx: int = 50, Ny: int = 50, Nt: int = 1000, 
                          D: float = 0.01, **ic_kwargs) -> Dict:
    """
    Convenience function to solve 2D heat equation with one function call.
    
    Args:
        initial_condition: Type of initial condition
        method: Numerical method
        Lx, Ly, T, Nx, Ny, Nt, D: Problem parameters
        **ic_kwargs: Parameters for initial condition
        
    Returns:
        Dictionary with solution and metadata
    """
    # Create solver
    solver = HeatEquation2D(Lx, Ly, T, Nx, Ny, Nt, D)
    
    # Set initial condition
    solver.set_initial_condition(initial_condition, **ic_kwargs)
    
    # Solve
    solution = solver.solve(method)
    
    # Return everything
    return {
        "X": solver.X,
        "Y": solver.Y,
        "u_initial": solver.u_initial,
        "u_final": solution,
        "method": method,
        "params": solver.params,
        "solver": solver  # Return solver for further analysis
    }


# Example usage
if __name__ == "__main__":
    # Method 1: Using the class
    heat2d = HeatEquation2D(Lx=1.0, Ly=1.0, T=0.05, Nx=50, Ny=50, Nt=500, D=0.01)
    
    # Set a 2D step function initial condition
    heat2d.set_initial_condition("step", 
                                x_range=(0.3, 0.7), 
                                y_range=(0.3, 0.7), 
                                value=1.0)
    
    # Check stability
    print("Stability info:", heat2d.get_stability_info())
    
    # Solve using Crank-Nicolson
    solution = heat2d.solve("cn")
    
    # Plot the result
    heat2d.plot(show_analytical=True, plot_type="contour")
    
    # Compare all methods
    heat2d.plot_method_comparison()
    
    # Method 2: Using convenience function
    result = solve_heat_equation_2d(
        "gaussian", "backward", 
        center=(0.5, 0.5), 
        width=(0.1, 0.1),
        Nx=30, Ny=30, Nt=200
    )
    result["solver"].plot()
    
    # Method 3: Direct function calls (most flexible)
    from .grid import create_2d_grid
    from .initial_conditions import step_function_2d
    from .solvers import solve_crank_nicolson_2d
    from .plotting import plot_2d_solution
    
    params = create_2d_grid(Lx=1.0, Ly=1.0, T=0.1, Nx=40, Ny=40, Nt=1000, D=0.01)
    u_init = step_function_2d(params.X, params.Y, Lx=params.Lx, Ly=params.Ly)
    u_final = solve_crank_nicolson_2d(u_init, params, params.Nt)
    plot_2d_solution(params.X, params.Y, u_final, u_init, "crank_nicolson")