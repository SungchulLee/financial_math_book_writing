# ============================================================================
# heat_equation_2d/plotting.py
# ============================================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Dict, Optional, Tuple
from .analytical import solve_analytical


def plot_2d_solution(X, Y, u_initial, u_final, method="Heat Equation", plot_type="contour"):
    """Plot initial and final 2D solutions."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    if plot_type == "contour":
        # Initial condition
        c1 = ax1.contourf(X, Y, u_initial, levels=20, cmap='hot')
        fig.colorbar(c1, ax=ax1)
        ax1.set_title("Initial Temperature")
        ax1.set_xlabel("x"); ax1.set_ylabel("y")
        
        # Final solution
        c2 = ax2.contourf(X, Y, u_final, levels=20, cmap='hot')
        fig.colorbar(c2, ax=ax2)
        ax2.set_title(f"Final Temperature ({method})")
        ax2.set_xlabel("x"); ax2.set_ylabel("y")
    
    elif plot_type == "surface":
        # 3D surface plots
        from mpl_toolkits.mplot3d import Axes3D
        ax1 = fig.add_subplot(121, projection='3d')
        ax2 = fig.add_subplot(122, projection='3d')
        
        ax1.plot_surface(X, Y, u_initial, cmap='hot', alpha=0.8)
        ax1.set_title("Initial Temperature")
        ax1.set_xlabel("x"); ax1.set_ylabel("y"); ax1.set_zlabel("Temperature")
        
        ax2.plot_surface(X, Y, u_final, cmap='hot', alpha=0.8)
        ax2.set_title(f"Final Temperature ({method})")
        ax2.set_xlabel("x"); ax2.set_ylabel("y"); ax2.set_zlabel("Temperature")
    
    plt.tight_layout()
    plt.show()


def plot_method_comparison_2d(X, Y, u_initial, results):
    """Plot comparison of different methods."""
    valid_results = {k: v for k, v in results.items() if v is not None}
    n_methods = len(valid_results)
    
    if n_methods == 0:
        print("No valid results to plot")
        return
    
    fig, axes = plt.subplots(1, n_methods+1, figsize=(4*(n_methods+1), 4))
    if n_methods == 0: axes = [axes]
    
    # Plot initial condition
    c0 = axes[0].contourf(X, Y, u_initial, levels=20, cmap='hot')
    fig.colorbar(c0, ax=axes[0])
    axes[0].set_title("Initial")
    axes[0].set_xlabel("x"); axes[0].set_ylabel("y")
    
    # Plot results
    for i, (method, solution) in enumerate(valid_results.items()):
        c = axes[i+1].contourf(X, Y, solution, levels=20, cmap='hot')
        fig.colorbar(c, ax=axes[i+1])
        axes[i+1].set_title(method)
        axes[i+1].set_xlabel("x"); axes[i+1].set_ylabel("y")
    
    plt.tight_layout()
    plt.show()


def plot_2d_evolution(X: np.ndarray, Y: np.ndarray, solution_history: np.ndarray,
                     time_array: np.ndarray, method: str = "Heat Equation",
                     n_snapshots: int = 6, plot_type: str = "contour",
                     figsize: Tuple[float, float] = (15, 10)) -> None:
    """
    Plot evolution of 2D solution over time.
    
    Args:
        X: 2D array of x coordinates
        Y: 2D array of y coordinates
        solution_history: Array of solutions at different times
        time_array: Array of time values
        method: Method name
        n_snapshots: Number of snapshots to show
        plot_type: "surface", "contour", or "both"
        figsize: Figure size
    """
    n_times = len(solution_history)
    snapshot_indices = np.linspace(0, n_times - 1, n_snapshots, dtype=int)
    
    if plot_type == "contour":
        n_cols = 3
        n_rows = (n_snapshots + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
        axes = axes.flatten()
        
        for i, idx in enumerate(snapshot_indices):
            t = time_array[idx]
            c = axes[i].contourf(X, Y, solution_history[idx], levels=20, cmap='hot')
            fig.colorbar(c, ax=axes[i])
            axes[i].set_title(f"t = {t:.4f}")
            axes[i].set_xlabel("x"); axes[i].set_ylabel("y")
        
        # Hide unused subplots
        for i in range(n_snapshots, len(axes)):
            axes[i].set_visible(False)
            
    elif plot_type == "surface":
        n_cols = 3
        n_rows = (n_snapshots + n_cols - 1) // n_cols
        fig = plt.figure(figsize=figsize)
        
        for i, idx in enumerate(snapshot_indices):
            t = time_array[idx]
            ax = fig.add_subplot(n_rows, n_cols, i+1, projection='3d')
            ax.plot_surface(X, Y, solution_history[idx], cmap='hot', alpha=0.8)
            ax.set_title(f"t = {t:.4f}")
            ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("T")
    
    fig.suptitle(f"Heat Equation Evolution ({method})", fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_error_analysis_2d(X: np.ndarray, Y: np.ndarray, numerical: np.ndarray,
                          analytical: np.ndarray, method: str = "Numerical",
                          figsize: Tuple[float, float] = (15, 5)) -> None:
    """
    Plot error analysis for 2D solutions.
    
    Args:
        X: 2D array of x coordinates
        Y: 2D array of y coordinates
        numerical: Numerical solution
        analytical: Analytical solution
        method: Method name
        figsize: Figure size
    """
    absolute_error = np.abs(numerical - analytical)
    relative_error = absolute_error / (np.abs(analytical) + 1e-12)
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=figsize)
    
    # Numerical solution
    c1 = ax1.contourf(X, Y, numerical, levels=20, cmap='hot')
    fig.colorbar(c1, ax=ax1)
    ax1.set_title(f"{method} Solution")
    ax1.set_xlabel("x"); ax1.set_ylabel("y")
    
    # Absolute error
    c2 = ax2.contourf(X, Y, absolute_error, levels=20, cmap='viridis')
    fig.colorbar(c2, ax=ax2)
    ax2.set_title(f"Absolute Error\nMax: {np.max(absolute_error):.2e}")
    ax2.set_xlabel("x"); ax2.set_ylabel("y")
    
    # Relative error
    c3 = ax3.contourf(X, Y, relative_error, levels=20, cmap='plasma')
    fig.colorbar(c3, ax=ax3)
    ax3.set_title(f"Relative Error\nMax: {np.max(relative_error):.2e}")
    ax3.set_xlabel("x"); ax3.set_ylabel("y")
    
    plt.tight_layout()
    plt.show()


def plot_stability_analysis_2d(stability_data: dict, figsize: Tuple[float, float] = (12, 8)) -> None:
    """
    Plot stability analysis results for 2D methods.
    
    Args:
        stability_data: Dictionary with stability analysis results
        figsize: Figure size
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)
    
    if 'dt_values' in stability_data and 'errors' in stability_data:
        # Error vs time step
        ax1.loglog(stability_data['dt_values'], stability_data['errors'], 'bo-')
        ax1.set_xlabel("Time Step (dt)")
        ax1.set_ylabel("L2 Error")
        ax1.set_title("Error vs Time Step")
        ax1.grid(True, alpha=0.3)
    
    if 'stability_params' in stability_data and 'max_errors' in stability_data:
        # Error vs stability parameter
        stable_mask = np.array(stability_data['stability_params']) <= 0.5
        unstable_mask = ~stable_mask
        
        if np.any(stable_mask):
            ax2.semilogy(np.array(stability_data['stability_params'])[stable_mask], 
                        np.array(stability_data['max_errors'])[stable_mask], 
                        'go-', label="Stable")
        if np.any(unstable_mask):
            ax2.semilogy(np.array(stability_data['stability_params'])[unstable_mask], 
                        np.array(stability_data['max_errors'])[unstable_mask], 
                        'ro-', label="Unstable")
        
        ax2.axvline(x=0.5, color='black', linestyle='--', alpha=0.7, label="Stability Limit")
        ax2.set_xlabel("Stability Parameter (rx + ry)")
        ax2.set_ylabel("Max Error")
        ax2.set_title("Stability Analysis")
        ax2.grid(True, alpha=0.3)
        ax2.legend()
    
    # Additional plots can be added based on available data
    ax3.text(0.5, 0.5, "Additional\nAnalysis\nPlaceholder", 
             ha='center', va='center', transform=ax3.transAxes, fontsize=14)
    ax3.set_title("Future Extension")
    
    ax4.text(0.5, 0.5, "Convergence\nRate Analysis\nPlaceholder", 
             ha='center', va='center', transform=ax4.transAxes, fontsize=14)
    ax4.set_title("Future Extension")
    
    plt.tight_layout()
    plt.show()


def plot_temperature_evolution(X, Y, solutions, time_points, method="Method"):
    """Plot temperature evolution at different time points."""
    n_times = len(solutions)
    n_cols = min(4, n_times)
    n_rows = (n_times + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(4*n_cols, 4*n_rows))
    if n_times == 1: axes = [axes]
    axes = np.array(axes).flatten()
    
    for i, (solution, t) in enumerate(zip(solutions, time_points)):
        c = axes[i].contourf(X, Y, solution, levels=20, cmap='hot')
        fig.colorbar(c, ax=axes[i])
        axes[i].set_title(f"t = {t:.4f}")
        axes[i].set_xlabel("x"); axes[i].set_ylabel("y")
    
    # Hide unused subplots
    for i in range(n_times, len(axes)):
        axes[i].set_visible(False)
    
    plt.suptitle(f"Temperature Evolution ({method})")
    plt.tight_layout()
    plt.show()


def plot_cross_sections(X, Y, u_initial, u_final, method="Method"):
    """Plot cross-sections through the center of the domain."""
    Nx, Ny = X.shape
    mid_x, mid_y = Nx // 2, Ny // 2
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # X cross-section (through middle Y)
    ax1.plot(X[:, mid_y], u_initial[:, mid_y], 'b-', label='Initial', linewidth=2)
    ax1.plot(X[:, mid_y], u_final[:, mid_y], 'r-', label='Final', linewidth=2)
    ax1.set_xlabel("x")
    ax1.set_ylabel("Temperature")
    ax1.set_title(f"Cross-section at y = {Y[mid_x, mid_y]:.2f}")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Y cross-section (through middle X)
    ax2.plot(Y[mid_x, :], u_initial[mid_x, :], 'b-', label='Initial', linewidth=2)
    ax2.plot(Y[mid_x, :], u_final[mid_x, :], 'r-', label='Final', linewidth=2)
    ax2.set_xlabel("y")
    ax2.set_ylabel("Temperature")
    ax2.set_title(f"Cross-section at x = {X[mid_x, mid_y]:.2f}")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle(f"Temperature Cross-sections ({method})")
    plt.tight_layout()
    plt.show()