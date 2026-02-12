# ============================================================================
# heat_equation_1d/wrapper.py
# ============================================================================
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Callable, Optional, Union

# Import all the core modules
from .heat_equation import HeatEquation1D, solve_heat_equation
from .grid import create_grid, check_stability, GridParams
from .initial_conditions import (
    step_function, gaussian_pulse, sine_wave, triangle_wave, 
    custom_function, zero_initial_condition
)
from .solvers import (
    solve_forward_euler, solve_backward_euler, solve_crank_nicolson,
    solve_with_history, compare_methods
)
from .analytical import solve_analytical, validate_against_analytical
from .plotting import (
    plot_solution, plot_method_comparison, plot_with_analytical,
    plot_convergence_study, plot_stability_analysis
)


class HeatSolver:
    """
    Unified wrapper class for solving 1D heat equation problems.
    
    This class provides a simple interface for common use cases while
    maintaining access to all advanced features of the package.
    """
    
    def __init__(self, L: float = 1.0, T: float = 0.1, Nx: int = 100, 
                 Nt: int = 1000, D: float = 0.01):
        """
        Initialize the heat equation solver.
        
        Args:
            L: Domain length
            T: Total simulation time
            Nx: Number of spatial grid points
            Nt: Number of time steps
            D: Thermal diffusivity
        """
        self.solver = HeatEquation1D(L, T, Nx, Nt, D)
        self._results = {}
        self._validation = {}
    
    def set_initial_condition(self, condition_type: str, **kwargs) -> 'HeatSolver':
        """
        Set initial condition using predefined types or custom function.
        
        Args:
            condition_type: "step", "gaussian", "sine", "triangle", "zero", or "custom"
            **kwargs: Parameters specific to each condition type
            
        Returns:
            Self for method chaining
        """
        if condition_type == "triangle":
            # Handle triangle wave separately since it's not in the main class
            func = lambda x: triangle_wave(x, L=self.solver.params.L, **kwargs)
            self.solver.set_initial_condition("custom", func=func)
        elif condition_type == "zero":
            func = lambda x: zero_initial_condition(x)
            self.solver.set_initial_condition("custom", func=func)
        else:
            self.solver.set_initial_condition(condition_type, **kwargs)
        
        return self
    
    def solve(self, method: str = "cn") -> 'HeatSolver':
        """
        Solve the heat equation using specified method.
        
        Args:
            method: "forward", "backward", "cn" (Crank-Nicolson), or "all"
            
        Returns:
            Self for method chaining
        """
        if method == "all":
            self._results = self.solver.compare_all_methods()
        else:
            solution = self.solver.solve(method)
            self._results[method] = solution
        
        return self
    
    def validate(self, analytical_method: str = "eigenfunction") -> Dict:
        """
        Validate numerical solution against analytical solution.
        
        Args:
            analytical_method: "eigenfunction", "heat_kernel", or "fourier"
            
        Returns:
            Validation metrics dictionary
        """
        self._validation = self.solver.validate_solution(analytical_method)
        return self._validation
    
    def plot(self, show_analytical: bool = True, show_methods: List[str] = None) -> 'HeatSolver':
        """
        Plot results with various options.
        
        Args:
            show_analytical: Whether to include analytical solution
            show_methods: List of methods to plot, or None for all available
            
        Returns:
            Self for method chaining
        """
        if len(self._results) > 1:  # Multiple methods available
            if show_analytical:
                self.solver.plot_method_comparison()
                self.solver.plot(show_analytical=True)
            else:
                self.solver.plot_method_comparison()
        else:
            self.solver.plot(show_analytical=show_analytical)
        
        return self
    
    def get_results(self) -> Dict:
        """Get all computed results."""
        return {
            'grid': self.solver.params,
            'initial': self.solver.u_initial,
            'solutions': self._results,
            'validation': self._validation
        }
    
    def get_error_summary(self) -> Dict:
        """Get summary of validation errors if available."""
        if not self._validation:
            return {"error": "No validation performed yet"}
        
        return {
            "max_absolute_error": self._validation["max_absolute_error"],
            "max_relative_error": self._validation["max_relative_error"],
            "l2_error": self._validation["l2_error"],
            "relative_l2_error": self._validation["relative_l2_error"]
        }
    
    @property
    def x(self) -> np.ndarray:
        """Spatial grid points."""
        return self.solver.x
    
    @property
    def info(self) -> Dict:
        """Solver information."""
        return self.solver.info()


def quick_solve(initial_condition: str = "step", method: str = "cn",
                L: float = 1.0, T: float = 0.1, Nx: int = 50, Nt: int = 500,
                D: float = 0.01, plot: bool = True, validate: bool = True,
                **ic_kwargs) -> Dict:
    """
    Solve a heat equation problem with one function call.
    
    Args:
        initial_condition: Type of initial condition
        method: Numerical method to use
        L, T, Nx, Nt, D: Problem parameters
        plot: Whether to create plots
        validate: Whether to validate against analytical solution
        **ic_kwargs: Parameters for initial condition
        
    Returns:
        Dictionary with all results
    """
    solver = HeatSolver(L, T, Nx, Nt, D)
    solver.set_initial_condition(initial_condition, **ic_kwargs)
    solver.solve(method)
    
    results = {"solver": solver}
    
    if validate and solver.solver.initial_func is not None:
        results["validation"] = solver.validate()
        results["error_summary"] = solver.get_error_summary()
    
    if plot:
        solver.plot(show_analytical=validate)
    
    results.update(solver.get_results())
    return results


def benchmark_methods(initial_condition: str = "gaussian", 
                     L: float = 1.0, T: float = 0.05, Nx: int = 50, 
                     Nt: int = 1000, D: float = 0.01, **ic_kwargs) -> Dict:
    """
    Benchmark all numerical methods against analytical solution.
    
    Args:
        initial_condition: Type of initial condition
        L, T, Nx, Nt, D: Problem parameters
        **ic_kwargs: Parameters for initial condition
        
    Returns:
        Dictionary with benchmark results
    """
    solver = HeatSolver(L, T, Nx, Nt, D)
    solver.set_initial_condition(initial_condition, **ic_kwargs)
    solver.solve("all")
    
    # Validate each method
    validation_results = {}
    if solver.solver.initial_func is not None:
        # Get analytical solution
        analytical = solve_analytical(
            solver.x, T, solver.solver.initial_func, D, L, "eigenfunction"
        )
        
        for method, solution in solver._results.items():
            if isinstance(solution, np.ndarray):
                validation = validate_against_analytical(
                    solution, solver.x, T, solver.solver.initial_func, D, L
                )
                validation_results[method] = {
                    "max_abs_error": validation["max_absolute_error"],
                    "max_rel_error": validation["max_relative_error"],
                    "l2_error": validation["l2_error"],
                    "rel_l2_error": validation["relative_l2_error"]
                }
    
    # Create comprehensive plot
    solver.plot(show_analytical=True)
    
    return {
        "solver": solver,
        "validation": validation_results,
        "summary": _create_benchmark_summary(validation_results)
    }


def convergence_study(initial_condition: str = "gaussian", method: str = "cn",
                     grid_sizes: List[int] = None, T: float = 0.05,
                     L: float = 1.0, D: float = 0.01, **ic_kwargs) -> Dict:
    """
    Perform convergence study for a given method.
    
    Args:
        initial_condition: Type of initial condition
        method: Numerical method to study
        grid_sizes: List of Nx values to test
        T, L, D: Problem parameters
        **ic_kwargs: Parameters for initial condition
        
    Returns:
        Dictionary with convergence results
    """
    if grid_sizes is None:
        grid_sizes = [25, 50, 100, 200]
    
    errors = []
    
    for Nx in grid_sizes:
        # Use proportional time steps to maintain accuracy
        Nt = max(int(T * Nx * 10), 100)
        
        try:
            result = quick_solve(
                initial_condition, method, L, T, Nx, Nt, D,
                plot=False, validate=True, **ic_kwargs
            )
            
            if "validation" in result:
                errors.append(result["validation"]["l2_error"])
            else:
                errors.append(np.nan)
                
        except Exception as e:
            print(f"Failed for Nx={Nx}: {e}")
            errors.append(np.nan)
    
    # Plot convergence
    plot_convergence_study(grid_sizes, errors, method)
    
    # Calculate convergence rate
    convergence_rate = _estimate_convergence_rate(grid_sizes, errors)
    
    return {
        "grid_sizes": grid_sizes,
        "errors": errors,
        "convergence_rate": convergence_rate,
        "method": method
    }


def stability_analysis(method: str = "forward", L: float = 1.0, Nx: int = 50,
                      dt_range: Tuple[float, float] = (1e-6, 1e-3),
                      n_points: int = 20) -> Dict:
    """
    Analyze stability of explicit methods.
    
    Args:
        method: Method to analyze (typically "forward")
        L, Nx: Spatial parameters
        dt_range: Range of time steps to test
        n_points: Number of points to test
        
    Returns:
        Dictionary with stability analysis results
    """
    if method not in ["forward"]:
        print(f"Stability analysis typically done for explicit methods. "
              f"Method '{method}' is implicit and unconditionally stable.")
        return {}
    
    dt_values = np.logspace(np.log10(dt_range[0]), np.log10(dt_range[1]), n_points)
    errors = []
    coeff_values = []
    
    D = 0.01
    T = 0.05
    
    for dt in dt_values:
        Nt = int(T / dt)
        params = create_grid(L, T, Nx, Nt, D)
        coeff = params.coeff
        coeff_values.append(coeff)
        
        try:
            # Use simple Gaussian initial condition
            u_init = gaussian_pulse(params.x, L=L)
            initial_func = lambda x: gaussian_pulse(x, L=L)
            
            if coeff <= 0.5:  # Stable regime
                u_final = solve_forward_euler(u_init, coeff, Nt)
                u_analytical = solve_analytical(params.x, T, initial_func, D, L)
                error = np.max(np.abs(u_final - u_analytical))
            else:  # Unstable regime - expect large errors
                try:
                    u_final = solve_forward_euler(u_init, coeff, Nt, check_stable=False)
                    u_analytical = solve_analytical(params.x, T, initial_func, D, L)
                    error = np.max(np.abs(u_final - u_analytical))
                except:
                    error = np.inf
            
            errors.append(error)
            
        except Exception as e:
            errors.append(np.inf)
    
    # Plot results
    plot_stability_analysis(dt_values, np.array(errors), np.array(coeff_values))
    
    return {
        "dt_values": dt_values,
        "errors": errors,
        "coeff_values": coeff_values,
        "stability_limit": 0.5,
        "method": method
    }


def demo_all_features():
    """
    Demonstration of all package features.
    """
    print("=== Heat Equation 1D Package Demo ===\n")
    
    # 1. Quick solve with different initial conditions
    print("1. Quick solve examples:")
    
    print("   - Step function with Crank-Nicolson:")
    quick_solve("step", "cn", start=0.3, end=0.7, value=1.0)
    
    print("   - Gaussian pulse with backward Euler:")
    quick_solve("gaussian", "backward", center=0.5, width=0.1, amplitude=2.0)
    
    # 2. Method comparison
    print("\n2. Method comparison:")
    benchmark_methods("gaussian", center=0.4, width=0.08)
    
    # 3. Convergence study
    print("\n3. Convergence study:")
    convergence_study("sine", "cn", n_modes=2)
    
    # 4. Stability analysis
    print("\n4. Stability analysis:")
    stability_analysis("forward")
    
    # 5. Advanced usage with method chaining
    print("\n5. Advanced usage with method chaining:")
    solver = (HeatSolver(L=2.0, T=0.1, Nx=80, Nt=1000, D=0.015)
              .set_initial_condition("triangle", peak_pos=0.3, amplitude=1.5)
              .solve("all")
              #.validate("eigenfunction")
              .plot(show_analytical=True))
    
    print("Error summary:", solver.get_error_summary())
    
    print("\nDemo completed!")


# Helper functions
def _create_benchmark_summary(validation_results: Dict) -> Dict:
    """Create summary of benchmark results."""
    if not validation_results:
        return {"error": "No validation results available"}
    
    summary = {}
    for method, metrics in validation_results.items():
        summary[method] = {
            "accuracy_rank": 0,  # Will be filled later
            "l2_error": metrics["l2_error"],
            "max_error": metrics["max_abs_error"]
        }
    
    # Rank methods by L2 error
    sorted_methods = sorted(summary.items(), key=lambda x: x[1]["l2_error"])
    for i, (method, data) in enumerate(sorted_methods):
        summary[method]["accuracy_rank"] = i + 1
    
    return summary


def _estimate_convergence_rate(grid_sizes: List[int], errors: List[float]) -> float:
    """Estimate convergence rate from grid refinement study."""
    valid_indices = [i for i, e in enumerate(errors) if not np.isnan(e) and e > 0]
    
    if len(valid_indices) < 2:
        return np.nan
    
    # Use last two valid points
    i1, i2 = valid_indices[-2], valid_indices[-1]
    h1, h2 = 1.0 / grid_sizes[i1], 1.0 / grid_sizes[i2]
    e1, e2 = errors[i1], errors[i2]
    
    # Calculate convergence rate: error ~ h^p
    if e1 > 0 and e2 > 0 and h1 != h2:
        rate = np.log(e2 / e1) / np.log(h2 / h1)
        return rate
    
    return np.nan


# Export main interface
__all__ = [
    'HeatSolver', 'quick_solve', 'benchmark_methods', 
    'convergence_study', 'stability_analysis', 'demo_all_features'
]


# Example usage
if __name__ == "__main__":
    # Run the full demo
    demo_all_features()