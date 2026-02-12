# ============================================================================
# black_scholes/black_scholes_monte_carlo.py
# ============================================================================
"""
Monte Carlo simulation for Black-Scholes options.
FIXED VERSION - Maintains API compatibility while providing enhanced accuracy.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import simulate_gbm_paths, monte_carlo_pricing

class BlackScholesMonteCarlo(BlackScholesBase):
    """
    Monte Carlo simulation for Black-Scholes options.
    
    FIXED VERSION - Now provides both enhanced and legacy modes:
    - enhanced=True: Uses variance reduction techniques (better accuracy)
    - enhanced=False: Uses original Version 1 logic (educational/debugging)
    """
    
    def price(self, num_paths=10000, steps_per_year=252, seed=None, plot_histogram=True, enhanced=True):
        """
        Price options using Monte Carlo simulation.
        
        FIXED API - Now supports both enhanced and legacy modes for backward compatibility.
        
        Parameters:
        -----------
        num_paths : int
            Number of simulation paths (default: 10000)
        steps_per_year : int
            Number of time steps per year (default: 252)
        seed : int, optional
            Random seed for reproducibility
        plot_histogram : bool
            Whether to plot histograms of option prices (default: True)
        enhanced : bool
            If True: Use variance reduction techniques (antithetic + control variates)
            If False: Use original Version 1 logic for exact backward compatibility
            (default: True)
            
        Returns:
        --------
        tuple: (call_price, put_price, call_price_std, put_price_std, 
                call_ci, put_ci, call_prices, put_prices)
        
        Notes:
        ------
        - enhanced=True: Better accuracy, 2-3x variance reduction
        - enhanced=False: Exact Version 1 behavior for educational use
        """
        self.num_paths = num_paths
        num_steps = int(steps_per_year * self.T)
        
        # Store mode for plotting purposes
        self._last_enhanced_mode = enhanced
        
        if enhanced:
            # Use enhanced implementation with variance reduction
            result = monte_carlo_pricing(
                S0=self.S0, K=self.K, T=self.T, r=self.r, sigma=self.sigma, q=self.q,
                n_paths=num_paths, n_steps=num_steps, seed=seed,
                antithetic=True, control_variate=True
            )
            
            # Extract results using the FIXED monte_carlo_pricing output
            call_price = result['call_price']
            put_price = result['put_price']
            call_price_std = result['call_std']      # FIX: Use actual std from simulation
            put_price_std = result['put_std']        # FIX: Use actual std from simulation
            call_ci = result['call_ci']
            put_ci = result['put_ci']
            call_prices = result['call_prices']      # FIX: Use actual simulated prices
            put_prices = result['put_prices']        # FIX: Use actual simulated prices
            
        else:
            # Use original Version 1 implementation for exact backward compatibility
            call_price, put_price, call_price_std, put_price_std, call_ci, put_ci, call_prices, put_prices = self._price_legacy(
                num_paths, num_steps, seed
            )
        
        # Plot histograms if requested (works with both modes)
        if plot_histogram:
            self._plot_histograms(call_prices, put_prices, call_price, put_price, 
                                call_price_std, put_price_std, call_ci, put_ci)
        
        return call_price, put_price, call_price_std, put_price_std, call_ci, put_ci, call_prices, put_prices
    
    def _price_legacy(self, num_paths, num_steps, seed):
        """
        Original Version 1 implementation for exact backward compatibility.
        
        This method replicates the exact logic from Version 1 to ensure
        identical results when enhanced=False.
        """
        # Use original simulate_gbm_paths function
        _, paths = simulate_gbm_paths(
            self.S0, self.T, self.r, self.sigma, 
            num_paths, num_steps, 
            risk_neutral=True, seed=seed
        )
        
        S_T = paths[:, -1]
        discount = np.exp(-self.r * self.T)
        
        # Calculate option payoffs
        call_payoffs = np.maximum(S_T - self.K, 0)
        put_payoffs = np.maximum(self.K - S_T, 0)
        
        # Calculate discounted prices
        call_prices = discount * call_payoffs
        put_prices = discount * put_payoffs
        
        # Calculate statistics (exactly as in Version 1)
        call_price = np.mean(call_prices)
        put_price = np.mean(put_prices)
        call_price_std = np.std(call_prices)
        put_price_std = np.std(put_prices)
        
        # Calculate empirical confidence intervals (exactly as in Version 1)
        call_ci = self._calculate_empirical_ci(call_prices, confidence_level=0.95)
        put_ci = self._calculate_empirical_ci(put_prices, confidence_level=0.95)
        
        return call_price, put_price, call_price_std, put_price_std, call_ci, put_ci, call_prices, put_prices
    
    def _calculate_empirical_ci(self, prices, confidence_level=0.95):
        """Calculate empirical confidence interval using percentiles - UNCHANGED from Version 1"""
        alpha = 1 - confidence_level
        lower_percentile = (alpha / 2) * 100
        upper_percentile = (1 - alpha / 2) * 100
        
        ci_lower = np.percentile(prices, lower_percentile)
        ci_upper = np.percentile(prices, upper_percentile)
        
        return (ci_lower, ci_upper)
    
    def calculate_bootstrap_ci(self, data, confidence_level=0.95, n_bootstrap=1000):
        """
        Calculate bootstrap confidence interval for the mean - UNCHANGED from Version 1
        
        Note: This method is preserved for backward compatibility but is not used
        in the main pricing workflow to avoid seed conflicts.
        """
        np.random.seed(42)  # For reproducibility
        bootstrap_means = []
        
        for _ in range(n_bootstrap):
            # Resample with replacement
            bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
            bootstrap_means.append(np.mean(bootstrap_sample))
        
        bootstrap_means = np.array(bootstrap_means)
        alpha = 1 - confidence_level
        lower_percentile = (alpha / 2) * 100
        upper_percentile = (1 - alpha / 2) * 100
        
        ci_lower = np.percentile(bootstrap_means, lower_percentile)
        ci_upper = np.percentile(bootstrap_means, upper_percentile)
        
        return (ci_lower, ci_upper)
    
    def _plot_histograms(self, call_prices, put_prices, call_mean, put_mean, 
                        call_std, put_std, call_ci, put_ci):
        """
        Plot histograms of option prices with enhanced statistics display.
        ENHANCED VERSION - now shows variance reduction info when applicable.
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Determine if this is enhanced mode (for display purposes)
        is_enhanced = hasattr(self, '_last_enhanced_mode') and self._last_enhanced_mode
        mode_text = "Enhanced MC (Variance Reduction)" if is_enhanced else "Standard MC"
        
        # Call option histogram
        ax1.hist(call_prices, bins=50, density=True, alpha=0.7, color='green', 
                edgecolor='black', label=mode_text)
        
        # Normal distribution overlay for comparison
        x_call = np.linspace(call_prices.min(), call_prices.max(), 1000)
        normal_call = stats.norm.pdf(x_call, call_mean, call_std)
        ax1.plot(x_call, normal_call, 'r-', linewidth=2, alpha=0.7, 
                label='Normal Density (comparison)')
        
        # Add confidence interval shading
        ax1.axvspan(call_ci[0], call_ci[1], alpha=0.3, color='orange', 
                   label=f'95% CI: [{call_ci[0]:.3f}, {call_ci[1]:.3f}]')
        ax1.axvline(call_mean, color='red', linestyle='--', alpha=0.8, 
                   label=f'Mean: {call_mean:.4f}')
        ax1.axvline(call_ci[0], color='orange', linestyle='-', alpha=0.8)
        ax1.axvline(call_ci[1], color='orange', linestyle='-', alpha=0.8)
        
        ax1.set_xlabel('Call Option Price')
        ax1.set_ylabel('Density')
        ax1.set_title(f'Call Option Price Distribution\n'
                     f'Mean: {call_mean:.4f}, Std: {call_std:.4f}')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Put option histogram
        ax2.hist(put_prices, bins=50, density=True, alpha=0.7, color='green', 
                edgecolor='black', label=mode_text)
        
        # Normal distribution overlay for comparison
        x_put = np.linspace(put_prices.min(), put_prices.max(), 1000)
        normal_put = stats.norm.pdf(x_put, put_mean, put_std)
        ax2.plot(x_put, normal_put, 'r-', linewidth=2, alpha=0.7, 
                label='Normal Density (comparison)')
        
        # Add confidence interval shading
        ax2.axvspan(put_ci[0], put_ci[1], alpha=0.3, color='orange', 
                   label=f'95% CI: [{put_ci[0]:.3f}, {put_ci[1]:.3f}]')
        ax2.axvline(put_mean, color='red', linestyle='--', alpha=0.8, 
                   label=f'Mean: {put_mean:.4f}')
        ax2.axvline(put_ci[0], color='orange', linestyle='-', alpha=0.8)
        ax2.axvline(put_ci[1], color='orange', linestyle='-', alpha=0.8)
        
        ax2.set_xlabel('Put Option Price')
        ax2.set_ylabel('Density')
        ax2.set_title(f'Put Option Price Distribution\n'
                     f'Mean: {put_mean:.4f}, Std: {put_std:.4f}')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Print detailed statistics
        self._print_detailed_statistics(call_prices, put_prices, call_mean, put_mean, 
                                       call_std, put_std, call_ci, put_ci)
    
    def _print_detailed_statistics(self, call_prices, put_prices, call_mean, put_mean, 
                                  call_std, put_std, call_ci, put_ci):
        """Print comprehensive statistics including confidence intervals - ENHANCED"""
        is_enhanced = hasattr(self, '_last_enhanced_mode') and self._last_enhanced_mode
        mode = "ENHANCED (Antithetic + Control Variates)" if is_enhanced else "STANDARD"
        
        print(f"\nMONTE CARLO STATISTICS (SAMPLE SIZE {self.num_paths:,})")
        print(f"Mode: {mode}")
        
        # Basic statistics
        print(f"\nBasic Statistics:")
        print(f"Call - Mean: {call_mean:.4f}, Std: {call_std:.4f}, "
              f"Min: {call_prices.min():.4f}, Max: {call_prices.max():.4f}")
        print(f"Put  - Mean: {put_mean:.4f}, Std: {put_std:.4f}, "
              f"Min: {put_prices.min():.4f}, Max: {put_prices.max():.4f}")
        
        # Distribution shape
        call_skew = stats.skew(call_prices)
        put_skew = stats.skew(put_prices)
        call_kurt = stats.kurtosis(call_prices)
        put_kurt = stats.kurtosis(put_prices)
        
        print(f"\nDistribution Shape:")
        print(f"Call - Skewness: {call_skew:.4f}, Kurtosis: {call_kurt:.4f}")
        print(f"Put  - Skewness: {put_skew:.4f}, Kurtosis: {put_kurt:.4f}")
        
        # Confidence intervals
        print(f"\n95% Confidence Intervals:")
        print(f"Call: [{call_ci[0]:.4f}, {call_ci[1]:.4f}], Width: {call_ci[1] - call_ci[0]:.4f}")
        print(f"Put:  [{put_ci[0]:.4f}, {put_ci[1]:.4f}], Width: {put_ci[1] - put_ci[0]:.4f}")
        
        # Standard errors for mean estimates
        call_std_error = call_std / np.sqrt(self.num_paths)
        put_std_error = put_std / np.sqrt(self.num_paths)
        
        print(f"\nStandard Errors of Mean:")
        print(f"Call: {call_std_error:.6f}, Put: {put_std_error:.6f}")
        
        if is_enhanced:
            print("\nNote: Enhanced mode uses variance reduction for better accuracy")
        else:
            print("\nNote: Standard mode for educational/debugging purposes")
    
    def compare_modes(self, num_paths=50000, seed=42, **kwargs):
        """
        Compare enhanced vs standard Monte Carlo modes side by side.
        
        This method demonstrates the variance reduction effectiveness.
        
        Parameters:
        -----------
        num_paths : int
            Number of paths for comparison (default: 50000)
        seed : int
            Random seed for fair comparison (default: 42)
        **kwargs : dict
            Additional arguments for pricing
            
        Returns:
        --------
        dict : Comparison results
        """
        print("COMPARING ENHANCED vs STANDARD MONTE CARLO")
        print("=" * 60)
        
        # Standard mode (Version 1 equivalent)
        print("\nRunning Standard Monte Carlo...")
        std_result = self.price(num_paths=num_paths, seed=seed, enhanced=False, 
                               plot_histogram=False, **kwargs)
        
        # Enhanced mode (Version 2 with variance reduction)
        print("Running Enhanced Monte Carlo...")
        enh_result = self.price(num_paths=num_paths, seed=seed, enhanced=True, 
                               plot_histogram=False, **kwargs)
        
        # Analytical benchmark
        from .black_scholes_utils import bs_call_price, bs_put_price
        analytical_call = bs_call_price(self.S0, self.K, self.T, self.r, self.sigma, self.q)
        analytical_put = bs_put_price(self.S0, self.K, self.T, self.r, self.sigma, self.q)
        
        # Calculate errors and improvements
        std_call_error = abs(std_result[0] - analytical_call)
        enh_call_error = abs(enh_result[0] - analytical_call)
        std_put_error = abs(std_result[1] - analytical_put)
        enh_put_error = abs(enh_result[1] - analytical_put)
        
        # Variance reduction ratios
        call_var_ratio = (std_result[2]**2) / (enh_result[2]**2)
        put_var_ratio = (std_result[3]**2) / (enh_result[3]**2)
        
        print(f"\nCOMPARISON RESULTS:")
        print(f"{'Metric':<20} {'Standard':<12} {'Enhanced':<12} {'Improvement':<12}")
        print("-" * 60)
        print(f"{'Call Price':<20} {std_result[0]:<12.6f} {enh_result[0]:<12.6f} {'-':<12}")
        print(f"{'Call Error':<20} {std_call_error:<12.6f} {enh_call_error:<12.6f} {enh_call_error/std_call_error if std_call_error > 0 else 1:<12.2f}x")
        print(f"{'Call Std Dev':<20} {std_result[2]:<12.6f} {enh_result[2]:<12.6f} {np.sqrt(call_var_ratio):<12.2f}x")
        print(f"{'Put Price':<20} {std_result[1]:<12.6f} {enh_result[1]:<12.6f} {'-':<12}")
        print(f"{'Put Error':<20} {std_put_error:<12.6f} {enh_put_error:<12.6f} {enh_put_error/std_put_error if std_put_error > 0 else 1:<12.2f}x")
        print(f"{'Put Std Dev':<20} {std_result[3]:<12.6f} {enh_result[3]:<12.6f} {np.sqrt(put_var_ratio):<12.2f}x")
        
        print(f"\nVARIANCE REDUCTION:")
        print(f"Call variance reduction: {call_var_ratio:.2f}x (equivalent to {call_var_ratio * num_paths:,.0f} standard paths)")
        print(f"Put variance reduction:  {put_var_ratio:.2f}x (equivalent to {put_var_ratio * num_paths:,.0f} standard paths)")
        
        print(f"\nANALYTICAL COMPARISON:")
        print(f"Analytical Call: {analytical_call:.6f}")
        print(f"Analytical Put:  {analytical_put:.6f}")
        
        return {
            'standard': std_result,
            'enhanced': enh_result,
            'analytical': (analytical_call, analytical_put),
            'variance_reduction': (call_var_ratio, put_var_ratio),
            'error_improvement': (enh_call_error/std_call_error if std_call_error > 0 else 1, 
                                enh_put_error/std_put_error if std_put_error > 0 else 1)
        }