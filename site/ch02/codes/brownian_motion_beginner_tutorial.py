"""
Beginner Examples: Brownian Motion Construction
=================================================

This module provides basic introduction to simulating and visualizing Brownian motion.
Heavily commented for educational purposes.

Topics covered:
1. Simple Brownian motion simulation
2. Visualization of sample paths
3. Verification of basic properties
4. Multiple paths visualization

Author: Sungchul, Yonsei University
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# Set random seed for reproducibility in educational setting
np.random.seed(42)


def simulate_brownian_motion_basic(T: float = 1.0, N: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate a standard Brownian motion path using independent increments.
    
    This is the most straightforward construction method:
    - Divide time [0, T] into N equal intervals of length dt
    - Generate independent N(0, dt) increments  
    - Cumulative sum gives Brownian motion path
    
    Mathematical basis:
    -------------------
    If W(t) is Brownian motion, then:
    - W(0) = 0
    - W(t) - W(s) ~ N(0, t-s) for t > s (stationary increments)
    - Increments over disjoint intervals are independent
    
    Parameters:
    -----------
    T : float
        Final time (default: 1.0)
    N : int
        Number of time steps (default: 1000)
        
    Returns:
    --------
    t : ndarray
        Time grid of shape (N+1,)
    W : ndarray
        Brownian motion values of shape (N+1,)
        
    Example:
    --------
    >>> t, W = simulate_brownian_motion_basic(T=1.0, N=1000)
    >>> plt.plot(t, W)
    >>> plt.show()
    """
    # Step 1: Create time grid
    # ------------------------
    # We divide [0, T] into N equal intervals
    # This gives us N+1 time points: 0, dt, 2*dt, ..., N*dt = T
    dt = T / N  # Time step size
    t = np.linspace(0, T, N + 1)  # Time grid: [0, dt, 2dt, ..., T]
    
    # Step 2: Generate independent normal increments
    # -----------------------------------------------
    # For Brownian motion, W(t+dt) - W(t) ~ N(0, dt)
    # So we need N increments (from t_0 to t_1, t_1 to t_2, ..., t_{N-1} to t_N)
    # Each increment: dW ~ N(0, dt), which means dW = sqrt(dt) * Z where Z ~ N(0,1)
    dW = np.random.normal(loc=0.0,           # mean = 0
                          scale=np.sqrt(dt),  # std = sqrt(dt)
                          size=N)             # N increments
    
    # Step 3: Construct Brownian motion path
    # ---------------------------------------
    # W(t_k) = W(0) + sum_{i=0}^{k-1} dW_i
    # We use cumsum for efficient computation
    # We prepend 0 because W(0) = 0
    W = np.concatenate([[0], np.cumsum(dW)])
    
    return t, W


def plot_single_path(t: np.ndarray, W: np.ndarray, save_path: str = None):
    """
    Visualize a single Brownian motion path.
    
    Parameters:
    -----------
    t : ndarray
        Time points
    W : ndarray
        Brownian motion values
    save_path : str, optional
        If provided, save figure to this path
    """
    plt.figure(figsize=(10, 6))
    plt.plot(t, W, 'b-', linewidth=1.5, label='Brownian Motion Path')
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3, label='Starting Point')
    plt.xlabel('Time t', fontsize=12)
    plt.ylabel('W(t)', fontsize=12)
    plt.title('Standard Brownian Motion Sample Path', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figure saved to: {save_path}")
    
    plt.show()


def simulate_multiple_paths(T: float = 1.0, N: int = 1000, n_paths: int = 10) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate multiple independent Brownian motion paths.
    
    This function demonstrates that:
    - Different sample paths can look very different
    - But they all satisfy the same statistical properties
    
    Parameters:
    -----------
    T : float
        Final time
    N : int  
        Number of time steps per path
    n_paths : int
        Number of paths to simulate
        
    Returns:
    --------
    t : ndarray
        Time grid of shape (N+1,)
    W_all : ndarray
        All paths, shape (n_paths, N+1)
    """
    dt = T / N
    t = np.linspace(0, T, N + 1)
    
    # Preallocate array for efficiency
    W_all = np.zeros((n_paths, N + 1))
    
    # Generate each path independently
    for i in range(n_paths):
        # Generate N increments for this path
        dW = np.random.normal(0, np.sqrt(dt), N)
        # Construct path with cumulative sum
        W_all[i, :] = np.concatenate([[0], np.cumsum(dW)])
    
    return t, W_all


def plot_multiple_paths(t: np.ndarray, W_all: np.ndarray, save_path: str = None):
    """
    Visualize multiple Brownian motion paths to show variability.
    
    Parameters:
    -----------
    t : ndarray
        Time points
    W_all : ndarray
        Multiple paths, shape (n_paths, N+1)
    save_path : str, optional
        Path to save figure
    """
    n_paths = W_all.shape[0]
    
    plt.figure(figsize=(12, 6))
    
    for i in range(n_paths):
        plt.plot(t, W_all[i, :], linewidth=1.0, alpha=0.7)
    
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    plt.xlabel('Time t', fontsize=12)
    plt.ylabel('W(t)', fontsize=12)
    plt.title(f'{n_paths} Sample Paths of Standard Brownian Motion', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figure saved to: {save_path}")
    
    plt.show()


def verify_increment_distribution(T: float = 1.0, N: int = 1000, n_simulations: int = 10000):
    """
    Verify that increments W(t) - W(s) ~ N(0, t-s).
    
    This is a key property of Brownian motion. We will:
    1. Simulate many Brownian motion paths
    2. Extract the increment W(T) - W(0) = W(T) from each path
    3. Check that these increments are approximately N(0, T) distributed
    
    Parameters:
    -----------
    T : float
        Time at which we check the distribution
    N : int
        Number of time steps
    n_simulations : int
        Number of independent paths to simulate
    """
    dt = T / N
    
    # Collect final values W(T) from many independent paths
    final_values = np.zeros(n_simulations)
    
    for i in range(n_simulations):
        # Generate one path
        dW = np.random.normal(0, np.sqrt(dt), N)
        W_T = np.sum(dW)  # W(T) = sum of all increments
        final_values[i] = W_T
    
    # Theoretical distribution: W(T) ~ N(0, T)
    theoretical_mean = 0
    theoretical_std = np.sqrt(T)
    
    # Empirical statistics
    empirical_mean = np.mean(final_values)
    empirical_std = np.std(final_values, ddof=1)
    
    print("\n" + "="*60)
    print("VERIFICATION: Distribution of W(T)")
    print("="*60)
    print(f"Theoretical: N(0, {T}) => mean=0, std={theoretical_std:.4f}")
    print(f"Empirical ({n_simulations} simulations):")
    print(f"  Mean: {empirical_mean:.4f} (should be ≈ 0)")
    print(f"  Std:  {empirical_std:.4f} (should be ≈ {theoretical_std:.4f})")
    print("="*60)
    
    # Visualize histogram vs theoretical density
    plt.figure(figsize=(10, 6))
    
    # Histogram of simulated values
    plt.hist(final_values, bins=50, density=True, alpha=0.7, 
             color='blue', edgecolor='black', label='Simulated W(T)')
    
    # Theoretical N(0, T) density
    x = np.linspace(final_values.min(), final_values.max(), 200)
    theoretical_density = (1 / (np.sqrt(2 * np.pi * T))) * np.exp(-x**2 / (2 * T))
    plt.plot(x, theoretical_density, 'r-', linewidth=2, label=f'N(0, {T}) Density')
    
    plt.xlabel('W(T)', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.title(f'Distribution of W(T) from {n_simulations} Simulations', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


# =============================================================================
# MAIN: Demonstration of all beginner-level functionality
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print(" BROWNIAN MOTION: BEGINNER EXAMPLES")
    print("="*70)
    
    # Example 1: Single path simulation
    print("\n[Example 1] Simulating single Brownian motion path...")
    t, W = simulate_brownian_motion_basic(T=1.0, N=1000)
    print(f"  - Time interval: [0, {t[-1]:.2f}]")
    print(f"  - Number of steps: {len(t)}")
    print(f"  - Final value W(T): {W[-1]:.4f}")
    plot_single_path(t, W)
    
    # Example 2: Multiple paths to show variability
    print("\n[Example 2] Simulating multiple independent paths...")
    t, W_all = simulate_multiple_paths(T=1.0, N=1000, n_paths=10)
    print(f"  - Number of paths: {W_all.shape[0]}")
    print(f"  - Final values range: [{W_all[:, -1].min():.4f}, {W_all[:, -1].max():.4f}]")
    plot_multiple_paths(t, W_all)
    
    # Example 3: Verify increment distribution
    print("\n[Example 3] Verifying W(T) ~ N(0, T)...")
    verify_increment_distribution(T=1.0, N=1000, n_simulations=10000)
    
    print("\n" + "="*70)
    print(" END OF BEGINNER EXAMPLES")
    print("="*70)
