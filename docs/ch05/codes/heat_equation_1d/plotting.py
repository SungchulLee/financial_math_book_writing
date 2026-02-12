# ============================================================================
# heat_equation_1d/plotting.py
# ============================================================================
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Callable, Tuple
from .analytical import solve_analytical


def plot_solution(x: np.ndarray, u_initial: np.ndarray, u_final: np.ndarray,
                  method: str = "forward", figsize: Tuple[float, float] = (10, 6)) -> None:
    """
    Plot initial and final temperature distributions.
    
    Args:
        x: Spatial grid points
        u_initial: Initial condition
        u_final: Final solution
        method: Method name for title
        figsize: Figure size tuple
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(x, u_initial, "--r", linewidth=2, label="Initial Temperature")
    ax.plot(x, u_final, "-b", linewidth=2, label="Final Temperature")
    
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    
    method_name = method.replace("_", " ").title()
    if method == "cn":
        method_name = "Crank-Nicolson"
    
    ax.set_title(f"Temperature Distribution ({method_name})")
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.show()


def plot_method_comparison(x: np.ndarray, u_initial: np.ndarray, 
                          results: Dict[str, np.ndarray],
                          figsize: Tuple[float, float] = (12, 8)) -> None:
    """
    Plot comparison of different numerical methods.
    
    Args:
        x: Spatial grid points
        u_initial: Initial condition
        results: Dictionary with method names as keys and solutions as values
        figsize: Figure size tuple
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot initial condition
    ax.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    
    # Color map for different methods with different line styles for visibility
    plot_styles = {
        "forward": {"color": "red", "linestyle": "-", "alpha": 0.8},
        "backward": {"color": "blue", "linestyle": "--", "alpha": 0.9}, 
        "crank_nicolson": {"color": "green", "linestyle": "-.", "alpha": 0.7}
    }
    method_names = {"forward": "Forward Euler", "backward": "Backward Euler", 
                   "crank_nicolson": "Crank-Nicolson"}
    
    for method, solution in results.items():
        if isinstance(solution, np.ndarray):  # Skip error messages
            style = plot_styles.get(method, {"color": "black", "linestyle": "-", "alpha": 1.0})
            name = method_names.get(method, method.replace("_", " ").title())
            ax.plot(x, solution, 
                   color=style["color"], 
                   linestyle=style["linestyle"],
                   linewidth=3, 
                   alpha=style["alpha"], 
                   label=name)
    
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Comparison of Numerical Methods")
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.show()


def plot_all_methods_with_analytical(x: np.ndarray, t: float, initial_func: Callable, 
                                   D: float, L: float, analytical_method: str = "eigenfunction",
                                   Nt: int = 1000, figsize: Tuple[float, float] = (15, 12)) -> None:
    """
    Plot all three numerical methods with analytical comparison in a 3x2 layout.
    
    Args:
        x: Spatial grid points
        t: Time of comparison
        initial_func: Initial condition function
        D: Thermal diffusivity
        L: Domain length
        analytical_method: Analytical method to use
        Nt: Number of time steps to use
        figsize: Figure size tuple
    """
    # Get analytical solution
    u_analytical = solve_analytical(x, t, initial_func, D, L, analytical_method)
    u_initial = initial_func(x)
    
    # Get solutions for all three methods
    from .solvers import solve_forward_euler, solve_backward_euler, solve_crank_nicolson
    from .grid import create_grid
    
    # Create grid parameters with explicit values
    Nx = len(x)
    params = create_grid(L=L, T=t, Nx=Nx, Nt=Nt, D=D)
    
    print(f"Debug: Nx={Nx}, Nt={Nt}, coeff={params.coeff:.4f}")
    
    # Forward Euler (with stability check)
    try:
        if params.coeff <= 0.5:
            u_forward = solve_forward_euler(u_initial, params.coeff, params.Nt, check_stable=False)
            forward_stable = True
        else:
            u_forward = None
            forward_stable = False
            print(f"Forward Euler unstable: coeff={params.coeff:.4f} > 0.5")
    except Exception as e:
        print(f"Forward Euler failed: {e}")
        u_forward = None
        forward_stable = False
        
    # Backward Euler
    try:
        u_backward = solve_backward_euler(u_initial, params.coeff, params.Nt)
        print("Backward Euler completed")
    except Exception as e:
        print(f"Backward Euler failed: {e}")
        return
    
    # Crank-Nicolson
    try:
        u_crank_nicolson = solve_crank_nicolson(u_initial, params.coeff, params.Nt)
        print("Crank-Nicolson completed")
    except Exception as e:
        print(f"Crank-Nicolson failed: {e}")
        return
    
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=figsize)
    
    # Row 1: Forward Euler
    ax1.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax1.plot(x, u_analytical, "-r", linewidth=2, label="Analytical")
    if forward_stable:
        ax1.plot(x, u_forward, "ob", markersize=4, label="Forward Euler")
        ax1.set_title(f"Forward Euler vs Analytical at t={t:.3f}")
    else:
        ax1.set_title(f"Forward Euler: Unstable (coeff={params.coeff:.3f})")
    ax1.set_xlabel("Position (x)")
    ax1.set_ylabel("Temperature (u)")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    if forward_stable and u_forward is not None:
        error_forward = np.abs(u_forward - u_analytical)
        ax2.plot(x, error_forward, "-g", linewidth=2)
        ax2.set_title(f"Forward Euler Error (Max: {np.max(error_forward):.2e})")
    else:
        ax2.text(0.5, 0.5, "Forward Euler\nUnstable", ha='center', va='center', 
                transform=ax2.transAxes, fontsize=14)
        ax2.set_title("Forward Euler Error: N/A")
    ax2.set_xlabel("Position (x)")
    ax2.set_ylabel("Absolute Error")
    ax2.grid(True, alpha=0.3)
    
    # Row 2: Backward Euler
    ax3.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax3.plot(x, u_analytical, "-r", linewidth=2, label="Analytical")
    ax3.plot(x, u_backward, "^b", markersize=4, label="Backward Euler")
    ax3.set_title(f"Backward Euler vs Analytical at t={t:.3f}")
    ax3.set_xlabel("Position (x)")
    ax3.set_ylabel("Temperature (u)")
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    error_backward = np.abs(u_backward - u_analytical)
    ax4.plot(x, error_backward, "-g", linewidth=2)
    ax4.set_title(f"Backward Euler Error (Max: {np.max(error_backward):.2e})")
    ax4.set_xlabel("Position (x)")
    ax4.set_ylabel("Absolute Error")
    ax4.grid(True, alpha=0.3)
    
    # Row 3: Crank-Nicolson
    ax5.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax5.plot(x, u_analytical, "-r", linewidth=2, label="Analytical")
    ax5.plot(x, u_crank_nicolson, "sg", markersize=4, label="Crank-Nicolson")
    ax5.set_title(f"Crank-Nicolson vs Analytical at t={t:.3f}")
    ax5.set_xlabel("Position (x)")
    ax5.set_ylabel("Temperature (u)")
    ax5.grid(True, alpha=0.3)
    ax5.legend()
    
    error_cn = np.abs(u_crank_nicolson - u_analytical)
    ax6.plot(x, error_cn, "-g", linewidth=2)
    ax6.set_title(f"Crank-Nicolson Error (Max: {np.max(error_cn):.2e})")
    ax6.set_xlabel("Position (x)")
    ax6.set_ylabel("Absolute Error")
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def plot_evolution_animation(x: np.ndarray, time_indices: np.ndarray, 
                           solution_history: np.ndarray, dt: float,
                           method: str = "forward", figsize: Tuple[float, float] = (10, 6)) -> None:
    """
    Create an animated plot of solution evolution (requires matplotlib animation).
    
    Args:
        x: Spatial grid points
        time_indices: Time step indices
        solution_history: Array of solutions at different times
        dt: Time step size
        method: Method name for title
        figsize: Figure size tuple
    """
    try:
        from matplotlib.animation import FuncAnimation
        
        fig, ax = plt.subplots(figsize=figsize)
        
        # Set up the plot
        line, = ax.plot([], [], 'b-', linewidth=2)
        ax.set_xlim(x[0], x[-1])
        ax.set_ylim(np.min(solution_history) * 1.1, np.max(solution_history) * 1.1)
        ax.set_xlabel("Position (x)")
        ax.set_ylabel("Temperature (u)")
        ax.grid(True, alpha=0.3)
        
        title_template = f"Heat Equation Evolution ({method}) - t = {{:.3f}}"
        title = ax.set_title(title_template.format(0))
        
        def animate(frame):
            t = time_indices[frame] * dt
            line.set_data(x, solution_history[frame])
            title.set_text(title_template.format(t))
            return line, title
        
        anim = FuncAnimation(fig, animate, frames=len(time_indices), 
                           interval=200, blit=True, repeat=True)
        
        plt.tight_layout()
        plt.show()
        
        return anim
        
    except ImportError:
        print("Animation requires matplotlib.animation. Creating static plots instead.")
        plot_evolution_snapshots(x, time_indices, solution_history, dt, method, figsize)


def plot_evolution_snapshots(x: np.ndarray, time_indices: np.ndarray,
                            solution_history: np.ndarray, dt: float, 
                            method: str = "forward", n_snapshots: int = 6,
                            figsize: Tuple[float, float] = (15, 10)) -> None:
    """
    Plot snapshots of solution evolution.
    
    Args:
        x: Spatial grid points
        time_indices: Time step indices
        solution_history: Array of solutions at different times
        dt: Time step size
        method: Method name for title
        n_snapshots: Number of snapshots to show
        figsize: Figure size tuple
    """
    n_times = len(time_indices)
    snapshot_indices = np.linspace(0, n_times - 1, n_snapshots, dtype=int)
    
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    axes = axes.flatten()
    
    for i, idx in enumerate(snapshot_indices):
        t = time_indices[idx] * dt
        axes[i].plot(x, solution_history[idx], 'b-', linewidth=2)
        axes[i].set_title(f"t = {t:.3f}")
        axes[i].set_xlabel("Position (x)")
        axes[i].set_ylabel("Temperature (u)")
        axes[i].grid(True, alpha=0.3)
        
        # Set consistent y-limits
        axes[i].set_ylim(np.min(solution_history) * 1.1, 
                        np.max(solution_history) * 1.1)
    
    fig.suptitle(f"Heat Equation Evolution ({method})", fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_convergence_study(grid_sizes: List[int], errors: List[float], 
                          method: str = "forward", figsize: Tuple[float, float] = (10, 6)) -> None:
    """
    Plot convergence study results.
    
    Args:
        grid_sizes: List of grid sizes (Nx values)
        errors: List of corresponding errors
        method: Method name for title
        figsize: Figure size tuple
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot errors
    ax.loglog(grid_sizes, errors, 'bo-', linewidth=2, markersize=8, label="Computed Error")
    
    # Add reference lines for convergence rates
    if len(grid_sizes) >= 2:
        # Second order reference line
        x_ref = np.array([grid_sizes[0], grid_sizes[-1]])
        y_ref = errors[0] * (x_ref[0] / x_ref) ** 2
        ax.loglog(x_ref, y_ref, 'r--', alpha=0.7, label="2nd Order")
        
        # First order reference line
        y_ref = errors[0] * (x_ref[0] / x_ref) ** 1
        ax.loglog(x_ref, y_ref, 'g--', alpha=0.7, label="1st Order")
    
    ax.set_xlabel("Grid Size (Nx)")
    ax.set_ylabel("L2 Error")
    ax.set_title(f"Convergence Study ({method})")
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.show()


def plot_stability_analysis(dt_values: np.ndarray, errors: np.ndarray,
                           coeff_values: np.ndarray, figsize: Tuple[float, float] = (12, 8)) -> None:
    """
    Plot stability analysis for Forward Euler method.
    
    Args:
        dt_values: Array of time step values
        errors: Array of corresponding errors
        coeff_values: Array of corresponding diffusion coefficients
        figsize: Figure size tuple
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Plot 1: Error vs time step
    ax1.semilogy(dt_values, errors, 'bo-', linewidth=2, markersize=6)
    ax1.set_xlabel("Time Step (dt)")
    ax1.set_ylabel("Final Error")
    ax1.set_title("Error vs Time Step")
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Error vs diffusion coefficient (stability parameter)
    stable_mask = coeff_values <= 0.5
    unstable_mask = coeff_values > 0.5
    
    ax2.semilogy(coeff_values[stable_mask], errors[stable_mask], 
                'go-', linewidth=2, markersize=6, label="Stable (≤0.5)")
    ax2.semilogy(coeff_values[unstable_mask], errors[unstable_mask], 
                'ro-', linewidth=2, markersize=6, label="Unstable (>0.5)")
    
    ax2.axvline(x=0.5, color='black', linestyle='--', alpha=0.7, label="Stability Limit")
    ax2.set_xlabel("Diffusion Coefficient (D·dt/dx²)")
    ax2.set_ylabel("Final Error")
    ax2.set_title("Stability Analysis")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    
def plot_with_analytical(x: np.ndarray, u_numerical: np.ndarray, 
                        t: float, initial_func: Callable, D: float, L: float,
                        method: str = "forward", analytical_method: str = "eigenfunction",
                        figsize: Tuple[float, float] = (18, 8)) -> None:
    """
    Plot numerical solution with analytical comparison in 2x3 layout.
    Shows all three methods (Forward Euler, Backward Euler, Crank-Nicolson) 
    compared against analytical solution.
    
    Args:
        x: Spatial grid points
        u_numerical: Numerical solution (not used, computed internally)
        t: Time of comparison
        initial_func: Initial condition function
        D: Thermal diffusivity
        L: Domain length
        method: Numerical method name (not used, shows all methods)
        analytical_method: Analytical method to use
        figsize: Figure size tuple
    """
    # Get analytical solution
    u_analytical = solve_analytical(x, t, initial_func, D, L, analytical_method)
    u_initial = initial_func(x)
    
    # Get solutions for all three methods
    from .solvers import solve_forward_euler, solve_backward_euler, solve_crank_nicolson
    from .grid import create_grid
    
    # Recreate grid parameters
    Nx = len(x)
    # Use reasonable defaults for time steps
    Nt = max(int(t * 1000), 100)  # At least 100 time steps
    params = create_grid(L=L, T=t, Nx=Nx, Nt=Nt, D=D)
    
    # Forward Euler (check stability)
    try:
        if params.coeff <= 0.5:
            u_forward = solve_forward_euler(u_initial, params.coeff, params.Nt)
            forward_stable = True
        else:
            u_forward = None
            forward_stable = False
    except:
        u_forward = None
        forward_stable = False
        
    # Backward Euler and Crank-Nicolson
    u_backward = solve_backward_euler(u_initial, params.coeff, params.Nt)
    u_crank_nicolson = solve_crank_nicolson(u_initial, params.coeff, params.Nt)
    
    # Create 2x3 subplot layout
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=figsize)
    
    # Top left: Forward Euler vs Analytical
    ax1.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax1.plot(x, u_analytical, "-r", linewidth=2, label="Analytical")
    if forward_stable:
        ax1.plot(x, u_forward, "ob", markersize=4, label="Forward Euler")
        ax1.set_title(f"Forward Euler vs Analytical at t={t:.3f}")
    else:
        ax1.set_title(f"Forward Euler: Unstable (coeff={params.coeff:.3f})")
    ax1.set_xlabel("Position (x)")
    ax1.set_ylabel("Temperature (u)")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Top middle: Backward Euler vs Analytical
    ax2.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax2.plot(x, u_analytical, "-r", linewidth=2, label="Analytical")
    ax2.plot(x, u_backward, "^b", markersize=4, label="Backward Euler")
    ax2.set_title(f"Backward Euler vs Analytical at t={t:.3f}")
    ax2.set_xlabel("Position (x)")
    ax2.set_ylabel("Temperature (u)")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Top right: Crank-Nicolson vs Analytical
    ax3.plot(x, u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax3.plot(x, u_analytical, "-r", linewidth=2, label="Analytical")
    ax3.plot(x, u_crank_nicolson, "sg", markersize=4, label="Crank-Nicolson")
    ax3.set_title(f"Crank-Nicolson vs Analytical at t={t:.3f}")
    ax3.set_xlabel("Position (x)")
    ax3.set_ylabel("Temperature (u)")
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    # Bottom left: Forward Euler Error
    if forward_stable and u_forward is not None:
        error_forward = np.abs(u_forward - u_analytical)
        ax4.plot(x, error_forward, "-g", linewidth=2)
        ax4.set_title(f"Forward Euler Error (Max: {np.max(error_forward):.2e})")
    else:
        ax4.text(0.5, 0.5, "Forward Euler\nUnstable", ha='center', va='center', 
                transform=ax4.transAxes, fontsize=14)
        ax4.set_title("Forward Euler Error: N/A")
    ax4.set_xlabel("Position (x)")
    ax4.set_ylabel("Absolute Error")
    ax4.grid(True, alpha=0.3)
    
    # Bottom middle: Backward Euler Error
    error_backward = np.abs(u_backward - u_analytical)
    ax5.plot(x, error_backward, "-g", linewidth=2)
    ax5.set_title(f"Backward Euler Error (Max: {np.max(error_backward):.2e})")
    ax5.set_xlabel("Position (x)")
    ax5.set_ylabel("Absolute Error")
    ax5.grid(True, alpha=0.3)
    
    # Bottom right: Crank-Nicolson Error
    error_cn = np.abs(u_crank_nicolson - u_analytical)
    ax6.plot(x, error_cn, "-g", linewidth=2)
    ax6.set_title(f"Crank-Nicolson Error (Max: {np.max(error_cn):.2e})")
    ax6.set_xlabel("Position (x)")
    ax6.set_ylabel("Absolute Error")
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()