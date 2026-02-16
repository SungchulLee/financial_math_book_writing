"""
cir_process_simulation.py
CIR (Cox-Ingersoll-Ross) Process Simulation and Density Analysis

This module implements simulation of the CIR process using the full truncation
Euler discretization scheme. The CIR process is widely used in fixed income
modeling and stochastic volatility models (e.g., Heston).

The CIR process follows:
    dV_t = κ(θ - V_t)dt + σ√V_t dW_t

where:
    κ = mean reversion speed (kappa)
    θ = long-run variance (theta)
    σ = volatility of volatility (sigma)
    V_t ≥ 0 (non-negative by construction under Feller condition)

Key features:
- Full truncation Euler discretization for numerical stability
- Feller condition verification: 2κθ ≥ σ²
- Comparison of simulated vs theoretical statistics
- Distribution analysis using non-central chi-squared approximation
- Multiple visualization plots
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ncx2, norm
from scipy.special import gamma


class CIRProcess:
    """
    Cox-Ingersoll-Ross (CIR) process simulator.
    
    The CIR process is defined by the SDE:
        dV_t = κ(θ - V_t)dt + σ√V_t dW_t
    
    Parameters are estimated from typical Heston model volatility parameters.
    """
    
    def __init__(self, kappa, theta, sigma, V0, T, N_steps, N_paths=10000):
        """
        Initialize CIR process parameters.
        
        Args:
            kappa: Mean reversion speed (κ)
            theta: Long-run mean level (θ)
            sigma: Volatility of volatility (σ)
            V0: Initial value of process
            T: Time to maturity
            N_steps: Number of time steps
            N_paths: Number of simulation paths
        """
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.V0 = V0
        self.T = T
        self.N_steps = N_steps
        self.N_paths = N_paths
        
        self.dt = T / N_steps
        
        # Check Feller condition
        self.feller_condition = 2 * kappa * theta >= sigma**2
        self.feller_ratio = (2 * kappa * theta) / (sigma**2)
    
    def check_feller_condition(self):
        """
        Check the Feller condition for non-negative rates.
        
        The Feller condition 2κθ ≥ σ² ensures that the CIR process
        does not hit zero under the discretization scheme.
        
        Returns:
            bool: True if Feller condition is satisfied
        """
        return self.feller_condition
    
    def print_parameters(self):
        """Print process parameters and Feller condition status."""
        print("=" * 70)
        print("CIR PROCESS PARAMETERS")
        print("=" * 70)
        print(f"Mean reversion speed (κ):        {self.kappa:.4f}")
        print(f"Long-run mean level (θ):        {self.theta:.6f}")
        print(f"Volatility of volatility (σ):   {self.sigma:.4f}")
        print(f"Initial value (V0):             {self.V0:.6f}")
        print(f"Time to maturity (T):           {self.T:.4f}")
        print(f"Number of time steps:           {self.N_steps}")
        print(f"Time step (dt):                 {self.dt:.6f}")
        print(f"Number of paths:                {self.N_paths}")
        print()
        print("FELLER CONDITION CHECK")
        print("-" * 70)
        print(f"Condition: 2κθ ≥ σ²")
        print(f"2κθ = {2 * self.kappa * self.theta:.6f}")
        print(f"σ² = {self.sigma**2:.6f}")
        print(f"Ratio (2κθ)/σ² = {self.feller_ratio:.4f}")
        if self.feller_condition:
            print("Status: ✓ Feller condition SATISFIED")
        else:
            print("Status: ✗ Feller condition NOT satisfied (process may hit zero)")
        print()
    
    def simulate_paths(self):
        """
        Simulate CIR process paths using full truncation Euler discretization.
        
        The full truncation scheme:
            V_{n+1} = V_n + κ(θ - max(0, V_n))Δt + σ√max(0, V_n) √Δt Z
            V_{n+1} = max(0, V_{n+1})
        
        This ensures V_t ≥ 0 for all t.
        
        Returns:
            np.ndarray: Array of shape (N_steps + 1, N_paths) containing simulated paths
        """
        # Initialize paths array
        paths = np.zeros((self.N_steps + 1, self.N_paths))
        paths[0, :] = self.V0
        
        # Generate random numbers
        z = np.random.standard_normal((self.N_steps, self.N_paths))
        
        # Simulate using full truncation Euler
        sqrt_dt = np.sqrt(self.dt)
        
        for t in range(1, self.N_steps + 1):
            V_prev = paths[t - 1, :]
            
            # Apply full truncation: use max(0, V) in drift and diffusion
            drift = self.kappa * (self.theta - np.maximum(0, V_prev)) * self.dt
            diffusion = self.sigma * np.sqrt(np.maximum(0, V_prev)) * sqrt_dt * z[t - 1, :]
            
            # Update paths
            paths[t, :] = V_prev + drift + diffusion
            
            # Apply final truncation: ensure non-negativity
            paths[t, :] = np.maximum(0, paths[t, :])
        
        return paths
    
    def theoretical_mean(self, t):
        """
        Compute theoretical mean of V_t.
        
        E[V_t] = θ + (V0 - θ)exp(-κt)
        
        Args:
            t: Time point
            
        Returns:
            float: Theoretical mean at time t
        """
        return self.theta + (self.V0 - self.theta) * np.exp(-self.kappa * t)
    
    def theoretical_variance(self, t):
        """
        Compute theoretical variance of V_t.
        
        Var[V_t] = (V0 - θ)σ² exp(-κt)(1 - exp(-κt))/(κ) 
                   + θσ²(1 - exp(-κt))²/(2κ)
        
        Args:
            t: Time point
            
        Returns:
            float: Theoretical variance at time t
        """
        exp_term = np.exp(-self.kappa * t)
        
        # First component
        term1 = (self.V0 - self.theta) * self.sigma**2 * exp_term * (1 - exp_term) / self.kappa
        
        # Second component
        term2 = self.theta * self.sigma**2 * (1 - exp_term)**2 / (2 * self.kappa)
        
        return term1 + term2
    
    def theoretical_terminal_distribution(self):
        """
        Compute non-central chi-squared parameters for terminal distribution.
        
        The CIR process at time T follows approximately:
            (2κV_T)/(σ²) ~ non-central χ²(df, λ)
        
        Returns:
            tuple: (degrees of freedom, non-centrality parameter)
        """
        # Degrees of freedom
        df = 4 * self.kappa * self.theta / self.sigma**2
        
        # Non-centrality parameter
        V_T_mean = self.theoretical_mean(self.T)
        lambda_param = 2 * self.kappa * V_T_mean / (self.sigma**2 * (1 - np.exp(-self.kappa * self.T)))
        
        return df, lambda_param
    
    def compute_statistics(self, paths):
        """
        Compute and compare simulated vs theoretical statistics.
        
        Args:
            paths: Simulated paths array
            
        Returns:
            dict: Dictionary containing statistics at various time points
        """
        stats = {
            'time_points': [],
            'simulated_mean': [],
            'theoretical_mean': [],
            'mean_error': [],
            'simulated_std': [],
            'theoretical_std': [],
            'std_error': []
        }
        
        # Evaluate at multiple time points
        time_indices = [0, self.N_steps // 4, self.N_steps // 2, 
                        3 * self.N_steps // 4, self.N_steps]
        
        for idx in time_indices:
            t = idx * self.dt
            
            # Simulated statistics
            sim_mean = np.mean(paths[idx, :])
            sim_std = np.std(paths[idx, :])
            
            # Theoretical statistics
            theo_mean = self.theoretical_mean(t)
            theo_var = self.theoretical_variance(t)
            theo_std = np.sqrt(theo_var)
            
            # Errors
            mean_error = abs(sim_mean - theo_mean)
            std_error = abs(sim_std - theo_std)
            
            stats['time_points'].append(t)
            stats['simulated_mean'].append(sim_mean)
            stats['theoretical_mean'].append(theo_mean)
            stats['mean_error'].append(mean_error)
            stats['simulated_std'].append(sim_std)
            stats['theoretical_std'].append(theo_std)
            stats['std_error'].append(std_error)
        
        return stats
    
    def print_statistics(self, stats):
        """
        Print statistics comparison table.
        
        Args:
            stats: Statistics dictionary from compute_statistics()
        """
        print("=" * 110)
        print("STATISTICS COMPARISON: SIMULATED vs THEORETICAL")
        print("=" * 110)
        print(f"{'Time':<8} {'Sim Mean':<14} {'Theo Mean':<14} {'Mean Error':<14} "
              f"{'Sim Std':<14} {'Theo Std':<14} {'Std Error':<14}")
        print("-" * 110)
        
        for i in range(len(stats['time_points'])):
            t = stats['time_points'][i]
            print(f"{t:<8.4f} {stats['simulated_mean'][i]:<14.6f} "
                  f"{stats['theoretical_mean'][i]:<14.6f} {stats['mean_error'][i]:<14.6f} "
                  f"{stats['simulated_std'][i]:<14.6f} {stats['theoretical_std'][i]:<14.6f} "
                  f"{stats['std_error'][i]:<14.6f}")
        
        print()
    
    def plot_sample_paths(self, paths):
        """
        Plot sample paths of the CIR process.
        
        Args:
            paths: Simulated paths array
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Time grid
        time_grid = np.linspace(0, self.T, self.N_steps + 1)
        
        # Plot first 100 paths with transparency
        n_plot = min(100, self.N_paths)
        for i in range(n_plot):
            ax.plot(time_grid, paths[:, i], alpha=0.3, linewidth=0.8)
        
        # Plot mean path
        mean_path = np.mean(paths, axis=1)
        ax.plot(time_grid, mean_path, 'r-', linewidth=2.5, label='Simulated Mean')
        
        # Plot theoretical mean
        theo_mean_path = np.array([self.theoretical_mean(t) for t in time_grid])
        ax.plot(time_grid, theo_mean_path, 'b--', linewidth=2.5, label='Theoretical Mean')
        
        ax.set_xlabel('Time', fontsize=11)
        ax.set_ylabel('Variance Level (V_t)', fontsize=11)
        ax.set_title('CIR Process Simulation: Sample Paths', fontsize=13, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/sessions/serene-kind-hopper/mnt/financial_math_book_writing/docs/ch15/codes/cir_paths.png', 
                    dpi=150, bbox_inches='tight')
        print("Saved: cir_paths.png")
        plt.close()
    
    def plot_terminal_distribution(self, paths):
        """
        Plot terminal distribution and compare with theoretical distribution.
        
        Args:
            paths: Simulated paths array
        """
        terminal_values = paths[-1, :]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Histogram of simulated values
        counts, bins, patches = ax.hist(terminal_values, bins=50, density=True, 
                                        alpha=0.7, color='skyblue', edgecolor='black',
                                        label='Simulated Distribution')
        
        # Theoretical non-central chi-squared distribution
        df, lambda_param = self.theoretical_terminal_distribution()
        
        # Scale factor for chi-squared: (2κV_T)/(σ²) ~ χ²(df, λ)
        # So V_T ~ (σ²/(2κ)) * χ²(df, λ)
        scale = self.sigma**2 / (2 * self.kappa)
        
        # Create x values for theoretical curve
        x = np.linspace(0, np.max(terminal_values) * 1.2, 1000)
        
        # Non-central chi-squared PDF
        theo_pdf = ncx2.pdf(2 * self.kappa * x / self.sigma**2, df, lambda_param) * (2 * self.kappa / self.sigma**2)
        ax.plot(x, theo_pdf, 'r-', linewidth=2.5, label='Theoretical (Non-central χ²)')
        
        ax.set_xlabel('Variance Level (V_T)', fontsize=11)
        ax.set_ylabel('Density', fontsize=11)
        ax.set_title(f'CIR Terminal Distribution (T={self.T})', fontsize=13, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add statistics text
        stats_text = f'Mean (sim): {np.mean(terminal_values):.6f}\n'
        stats_text += f'Mean (theo): {self.theoretical_mean(self.T):.6f}\n'
        stats_text += f'Std (sim): {np.std(terminal_values):.6f}\n'
        stats_text += f'Std (theo): {np.sqrt(self.theoretical_variance(self.T)):.6f}'
        ax.text(0.98, 0.97, stats_text, transform=ax.transAxes, 
                fontsize=10, verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig('/sessions/serene-kind-hopper/mnt/financial_math_book_writing/docs/ch15/codes/cir_terminal_dist.png',
                    dpi=150, bbox_inches='tight')
        print("Saved: cir_terminal_dist.png")
        plt.close()
    
    def plot_mean_variance_evolution(self, paths):
        """
        Plot evolution of mean and standard deviation over time.
        
        Args:
            paths: Simulated paths array
        """
        time_grid = np.linspace(0, self.T, self.N_steps + 1)
        
        # Compute simulated statistics at each time
        sim_means = np.array([np.mean(paths[t, :]) for t in range(self.N_steps + 1)])
        sim_stds = np.array([np.std(paths[t, :]) for t in range(self.N_steps + 1)])
        
        # Compute theoretical statistics
        theo_means = np.array([self.theoretical_mean(t) for t in time_grid])
        theo_vars = np.array([self.theoretical_variance(t) for t in time_grid])
        theo_stds = np.sqrt(theo_vars)
        
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Mean evolution
        ax1.plot(time_grid, sim_means, 'b-', linewidth=2, label='Simulated Mean', alpha=0.8)
        ax1.plot(time_grid, theo_means, 'r--', linewidth=2, label='Theoretical Mean', alpha=0.8)
        ax1.fill_between(time_grid, sim_means - sim_stds, sim_means + sim_stds,
                         alpha=0.2, color='blue', label='±1 Sim Std Dev')
        ax1.set_xlabel('Time', fontsize=11)
        ax1.set_ylabel('Mean Variance Level', fontsize=11)
        ax1.set_title('Mean Evolution', fontsize=12, fontweight='bold')
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)
        
        # Standard deviation evolution
        ax2.plot(time_grid, sim_stds, 'b-', linewidth=2, label='Simulated Std Dev', alpha=0.8)
        ax2.plot(time_grid, theo_stds, 'r--', linewidth=2, label='Theoretical Std Dev', alpha=0.8)
        ax2.set_xlabel('Time', fontsize=11)
        ax2.set_ylabel('Standard Deviation', fontsize=11)
        ax2.set_title('Volatility Evolution', fontsize=12, fontweight='bold')
        ax2.legend(fontsize=10)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/sessions/serene-kind-hopper/mnt/financial_math_book_writing/docs/ch15/codes/cir_mean_variance.png',
                    dpi=150, bbox_inches='tight')
        print("Saved: cir_mean_variance.png")
        plt.close()


def main():
    """
    Main function demonstrating CIR process simulation.
    """
    print("\n")
    print("=" * 70)
    print("CIR PROCESS SIMULATION AND DENSITY ANALYSIS")
    print("=" * 70)
    print()
    
    # Set parameters (typical Heston volatility parameters)
    kappa = 2.0           # Mean reversion speed
    theta = 0.04          # Long-run variance (4% per annum)
    sigma = 0.3           # Volatility of variance
    V0 = 0.04             # Initial variance
    T = 1.0               # 1 year maturity
    N_steps = 252         # Daily time steps
    N_paths = 10000       # Number of simulation paths
    
    # Create CIR process
    cir = CIRProcess(kappa, theta, sigma, V0, T, N_steps, N_paths)
    
    # Print parameters and check Feller condition
    cir.print_parameters()
    
    # Simulate paths
    print("Simulating CIR process paths...")
    paths = cir.simulate_paths()
    print(f"Completed: {N_paths} paths with {N_steps} steps")
    print()
    
    # Compute and print statistics
    stats = cir.compute_statistics(paths)
    cir.print_statistics(stats)
    
    # Generate plots
    print("Generating plots...")
    cir.plot_sample_paths(paths)
    cir.plot_terminal_distribution(paths)
    cir.plot_mean_variance_evolution(paths)
    
    print()
    print("=" * 70)
    print("SIMULATION COMPLETE")
    print("=" * 70)
    print()


if __name__ == '__main__':
    np.random.seed(42)  # For reproducibility
    main()
