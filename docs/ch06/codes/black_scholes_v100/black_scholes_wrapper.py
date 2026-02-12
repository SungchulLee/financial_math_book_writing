# ============================================================================
# black_scholes/black_scholes_wrapper.py
# ============================================================================
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import time
from .black_scholes_formula import BlackScholesFormula
from .black_scholes_greeks import BlackScholesGreeks
from .black_scholes_implied_vol import BlackScholesImpliedVol
from .black_scholes_monte_carlo import BlackScholesMonteCarlo
from .black_scholes_numerical import BlackScholesNumericalSolver
from .black_scholes_utils import simulate_gbm_paths, draw_finite_difference_grid, theta, rho


class BlackScholes:
    """
    A unified interface for all Black-Scholes option pricing functionality.
    
    This wrapper combines analytical formulas, Greeks calculation, Monte Carlo simulation,
    finite difference methods, and implied volatility computation into a single cohesive interface.
    
    Attributes:
    -----------
    S0 : float
        Initial stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility of the underlying asset
    q : float
        Continuous dividend yield (default: 0)
    formula : BlackScholesFormula
        Analytical pricing component
    greeks : BlackScholesGreeks
        Greeks calculation component
    monte_carlo : BlackScholesMonteCarlo
        Monte Carlo simulation component
    numerical : BlackScholesNumericalSolver
        Finite difference solver component
    implied_vol : BlackScholesImpliedVol
        Implied volatility component
    
    Methods:
    --------
    price_analytical()
        Calculate option prices using analytical Black-Scholes formula
    price_monte_carlo(num_paths=10000, **kwargs)
        Price options using Monte Carlo simulation
    price_numerical(method='explicit', **kwargs)
        Price options using finite difference methods
    calculate_greeks()
        Calculate all Greeks (delta, gamma, vega, theta, rho)
    calculate_implied_volatility(market_price, option_type='call', **kwargs)
        Calculate implied volatility from market price
    simulate_paths(num_paths=1000, num_steps=252, **kwargs)
        Simulate stock price paths using geometric Brownian motion
    compare_methods(option_type='call', **kwargs)
        Compare prices across different methods
    plot_convergence(**kwargs)
        Plot convergence analysis for numerical methods
    """
    
    def __init__(self, S0, K, T, r, sigma, q=0):
        # Store parameters
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q
        
        # Initialize all components
        self.formula = BlackScholesFormula(S0, K, T, r, sigma, q)
        self.greeks = BlackScholesGreeks(S0, K, T, r, sigma, q)
        self.monte_carlo = BlackScholesMonteCarlo(S0, K, T, r, sigma, q)
        self.numerical = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)
        self.implied_vol = BlackScholesImpliedVol(S0, K, T, r, sigma, q)
    
    def price_analytical(self):
        """
        Calculate European option prices using analytical Black-Scholes formula.
        
        Returns:
        --------
        tuple: (call_price, put_price)
        """
        return self.formula.price()
    
    def price_monte_carlo(self, num_paths=10000, steps_per_year=252, seed=None, 
                         plot_histogram=True, **kwargs):
        """
        Price options using Monte Carlo simulation.
        
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
        **kwargs : dict
            Additional arguments passed to Monte Carlo pricer
            
        Returns:
        --------
        tuple: (call_price, put_price, call_price_std, put_price_std, 
                call_ci, put_ci, call_prices, put_prices)
        """
        return self.monte_carlo.price(
            num_paths=num_paths,
            steps_per_year=steps_per_year,
            seed=seed,
            plot_histogram=plot_histogram,
            **kwargs
        )
    
    def price_numerical(self, method='explicit', option_type='put', **kwargs):
        """
        Price options using finite difference methods.
        
        Parameters:
        -----------
        method : str
            Numerical method: 'explicit', 'implicit', 'cn', 'explicit_log', 
            'implicit_log', 'cn_log' (default: 'explicit')
        option_type : str
            Option type: 'call' or 'put' (default: 'put')
        **kwargs : dict
            Additional arguments for the numerical solver
            
        Returns:
        --------
        tuple: (S_grid, option_values)
        """
        return self.numerical.solve(method=method, option_type=option_type, **kwargs)
    
    def calculate_greeks(self):
        """
        Calculate all option Greeks using analytical formulas.
        
        Returns:
        --------
        dict: Dictionary containing all Greeks
            - delta_call, delta_put : Delta values
            - gamma : Gamma (same for calls and puts)
            - vega : Vega (same for calls and puts)
            - theta_call, theta_put : Theta values
            - rho_call, rho_put : Rho values
        """
        delta_call, delta_put = self.greeks.delta()
        gamma_val = self.greeks.gamma()
        vega_val = self.greeks.vega()
        theta_call, theta_put = theta(self.S0, self.K, self.T, self.r, self.sigma, self.q)
        rho_call, rho_put = rho(self.S0, self.K, self.T, self.r, self.sigma, self.q)
        
        return {
            'delta_call': delta_call,
            'delta_put': delta_put,
            'gamma': gamma_val,
            'vega': vega_val,
            'theta_call': theta_call,
            'theta_put': theta_put,
            'rho_call': rho_call,
            'rho_put': rho_put
        }
    
    def calculate_implied_volatility(self, market_price, option_type='call', 
                                   sigma_0=0.2, **kwargs):
        """
        Calculate implied volatility from market price.
        
        Parameters:
        -----------
        market_price : float
            Observed market price of the option
        option_type : str
            Option type: 'call' or 'put' (default: 'call')
        sigma_0 : float
            Initial guess for volatility (default: 0.2)
        **kwargs : dict
            Additional arguments for the implied volatility solver
            
        Returns:
        --------
        float: Implied volatility
        """
        return self.implied_vol.compute(
            market_price=market_price,
            sigma_0=sigma_0,
            option_type=option_type,
            **kwargs
        )
    
    def simulate_paths(self, num_paths=1000, num_steps=252, risk_neutral=True, 
                      mu=None, seed=None, **kwargs):
        """
        Simulate stock price paths using geometric Brownian motion.
        
        Parameters:
        -----------
        num_paths : int
            Number of paths to simulate (default: 1000)
        num_steps : int
            Number of time steps (default: 252)
        risk_neutral : bool
            Whether to use risk-neutral drift (default: True)
        mu : float, optional
            Physical drift rate (used if risk_neutral=False)
        seed : int, optional
            Random seed for reproducibility
        **kwargs : dict
            Additional arguments for path simulation
            
        Returns:
        --------
        tuple: (time_grid, stock_paths)
        """
        return simulate_gbm_paths(
            S0=self.S0,
            T=self.T,
            r=self.r,
            sigma=self.sigma,
            num_paths=num_paths,
            num_steps=num_steps,
            mu=mu,
            risk_neutral=risk_neutral,
            seed=seed,
            **kwargs
        )
    
    def compare_methods(self, option_type='call', mc_paths=50000, 
                       numerical_method='cn', **kwargs):
        """
        Compare option prices across different pricing methods.
        
        Parameters:
        -----------
        option_type : str
            Option type: 'call' or 'put' (default: 'call')
        mc_paths : int
            Number of Monte Carlo paths (default: 50000)
        numerical_method : str
            Numerical method for finite difference (default: 'cn')
        **kwargs : dict
            Additional arguments for numerical methods
            
        Returns:
        --------
        dict: Comparison results with prices from different methods
        """
        # Analytical price
        call_analytical, put_analytical = self.price_analytical()
        analytical_price = call_analytical if option_type == 'call' else put_analytical
        
        # Monte Carlo price
        mc_results = self.price_monte_carlo(
            num_paths=mc_paths, 
            plot_histogram=False
        )
        mc_price = mc_results[0] if option_type == 'call' else mc_results[1]
        mc_std = mc_results[2] if option_type == 'call' else mc_results[3]
        
        # Numerical price
        S_grid, option_values = self.price_numerical(
            method=numerical_method,
            option_type=option_type,
            **kwargs
        )
        # Find price at current stock price
        idx = np.argmin(np.abs(S_grid - self.S0))
        numerical_price = option_values[idx]
        
        return {
            'analytical': analytical_price,
            'monte_carlo': {
                'price': mc_price,
                'std_error': mc_std / np.sqrt(mc_paths),
                'confidence_interval': (mc_price - 1.96 * mc_std / np.sqrt(mc_paths),
                                       mc_price + 1.96 * mc_std / np.sqrt(mc_paths))
            },
            'numerical': numerical_price,
            'differences': {
                'mc_vs_analytical': abs(mc_price - analytical_price),
                'numerical_vs_analytical': abs(numerical_price - analytical_price),
                'mc_vs_numerical': abs(mc_price - numerical_price)
            }
        }
    
    def plot_convergence(self, option_type='call', methods=['explicit', 'implicit', 'cn'],
                                grid_points=None, S_max=None, **kwargs):
        """
        Enhanced convergence plot with detailed analysis showing error vs step size.
        
        Parameters:
        -----------
        option_type : str
            Option type: 'call' or 'put' (default: 'call')
        methods : list
            List of numerical methods to compare
        grid_points : list, optional
            List of spatial grid points to test (default: comprehensive range)
        S_max : float, optional
            Maximum stock price for domain (default: 2*S0)
        **kwargs : dict
            Additional arguments for plotting (excluding 'grid_sizes')
        """
        # Remove 'grid_sizes' from kwargs if present (to avoid conflicts)
        clean_kwargs = {k: v for k, v in kwargs.items() if k != 'grid_sizes'}
        
        # Default comprehensive range of grid points
        if grid_points is None:
            grid_points = [25, 50, 75, 100, 150, 200, 300, 400, 600, 800, 1000]
        
        # Set default S_max if not provided
        if S_max is None:
            S_max = 2 * self.S0
        
        # Get analytical benchmark
        call_analytical, put_analytical = self.price_analytical()
        benchmark = call_analytical if option_type == 'call' else put_analytical
        
        # Create subplot for detailed analysis
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
        
        # Add supertitle
        fig.suptitle(f'Black-Scholes PDE Numerical Methods Convergence Analysis\n'
                    f'S₀={self.S0}, K={self.K}, T={self.T}, r={self.r:.1%}, σ={self.sigma:.1%}, q={self.q:.1%}\n'
                    f'Analytical {option_type}: {benchmark:.6f}, Domain: S ∈ [0, {S_max}]',
                    fontsize=14, fontweight='bold', y=0.95)
        
        # Colors and styles
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        linestyles = ['-', '--', '-.', ':', '-', '--']
        markers = ['o', 's', '^', 'D', 'v', 'P']
        
        all_errors = {}
        
        for i, method in enumerate(methods):
            errors = []
            step_sizes = []
            valid_grid_points = []
            computation_times = []
            
            for num_points in grid_points:
                try:
                    start_time = time.time()
                    
                    # Use ORIGINAL numerical methods with ORIGINAL defaults
                    if method.lower() == 'explicit':
                        S_grid, option_values = self.numerical.explicit(
                            option_type=option_type, 
                            Smin=0, Smax=S_max,  # ORIGINAL defaults
                            NS=num_points,
                            **clean_kwargs
                        )
                    elif method.lower() == 'implicit':
                        S_grid, option_values = self.numerical.implicit(
                            option_type=option_type,
                            Smin=1e-3, Smax=S_max,  # ORIGINAL defaults 
                            NS=num_points,
                            **clean_kwargs
                        )
                    elif method.lower() == 'cn':
                        S_grid, option_values = self.numerical.cn(
                            option_type=option_type,
                            Smin=0, Smax=S_max,  # ORIGINAL defaults
                            NS=num_points,
                            **clean_kwargs
                        )
                    
                    computation_time = time.time() - start_time
                    
                    # Find price at current stock price
                    idx = np.argmin(np.abs(S_grid - self.S0))
                    numerical_price = option_values[idx]
                    error = abs(numerical_price - benchmark)
                    
                    # Calculate spatial step size
                    ds = S_max / (num_points - 1)
                    
                    errors.append(error)
                    step_sizes.append(ds)
                    valid_grid_points.append(num_points)
                    computation_times.append(computation_time)
                    
                except Exception as e:
                    print(f"Error with {method} at {num_points} grid points: {e}")
                    continue
            
            if errors:
                all_errors[method] = (valid_grid_points, errors, computation_times, step_sizes)
                
                # Plot 1: Error vs Spatial Step Size (loglog)
                ax1.loglog(step_sizes, errors, 
                            marker=markers[i % len(markers)], 
                            color=colors[i % len(colors)],
                            linestyle=linestyles[i % len(linestyles)],
                            label=f'{method.upper()}', 
                            linewidth=2.5, 
                            markersize=8,
                            markerfacecolor='white',
                            markeredgewidth=2,
                            alpha=0.85)
                
                # Plot 2: Error vs Computation Time (loglog)
                ax2.loglog(computation_times, errors,
                        marker=markers[i % len(markers)], 
                        color=colors[i % len(colors)],
                        linestyle=linestyles[i % len(linestyles)],
                        label=f'{method.upper()}', 
                        linewidth=2.5, 
                        markersize=8,
                        markerfacecolor='white',
                        markeredgewidth=2,
                        alpha=0.85)
        
        # Get shared y-axis limits
        if all_errors:
            all_error_values = [error for _, errors, _, _ in all_errors.values() for error in errors]
            y_min = min(all_error_values) * 0.5
            y_max = max(all_error_values) * 2.0
            
            # Apply same y-axis limits to both plots
            ax1.set_ylim(y_min, y_max)
            ax2.set_ylim(y_min, y_max)
        
        # Calculate all step sizes for formatting
        all_step_sizes = [S_max / (n - 1) for n in grid_points]
        
        # Format Plot 1 (Error vs Spatial Step Size) - loglog
        ax1.set_xlim(min(all_step_sizes) * 0.8, max(all_step_sizes) * 1.2)
        
        # Format Plot 2 (Error vs Computation Time) - loglog
        ax2.set_xlabel('Computation Time (seconds)', fontsize=14, fontweight='bold')
        # Remove y-axis label for ax2 since it shares scale with ax1
        ax2.set_title('Efficiency Analysis\n(Error vs Computation Time)', fontsize=14, fontweight='bold')
        
        # Formatting for both plots
        for ax in [ax1, ax2]:
            ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
            ax.grid(True, which='minor', alpha=0.15, linestyle='-', linewidth=0.3)
            ax.tick_params(axis='both', which='major', labelsize=11, width=1.5, length=6)
            ax.tick_params(axis='both', which='minor', labelsize=9, width=1, length=3)
            ax.minorticks_on()
            
            legend = ax.legend(loc='best', frameon=True, fancybox=True, 
                            shadow=True, fontsize=10)
            legend.get_frame().set_facecolor('white')
            legend.get_frame().set_alpha(0.9)
        
        # Plot 1 specific formatting
        ax1.set_xlabel('Spatial Step Size (Δs)', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Absolute Error vs Analytical Solution', fontsize=14, fontweight='bold')
        ax1.set_title('Convergence Analysis\n(Error vs Spatial Step Size)', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        # Print numerical results with step size focus
        print("\n" + "="*80)
        print("CONVERGENCE ANALYSIS RESULTS (Error vs Step Size)")
        print("="*80)
        
        for method, (points, errors, times, step_sizes) in all_errors.items():
            print(f"\n{method.upper()} Method:")
            print(f"{'Grid Points':<12} {'Δs':<10} {'Error':<12} {'Time (s)':<10} {'Error Ratio':<12}")
            print("-" * 70)
            
            for i, (num_points, ds, error, exec_time) in enumerate(zip(points, step_sizes, errors, times)):
                if i > 0:
                    error_ratio = errors[i-1] / error
                else:
                    error_ratio = float('inf')
                
                print(f"{num_points:<12} {ds:<10.4f} {error:<12.2e} {exec_time:<10.4f} {error_ratio:<12.2f}")

        print(f"\nNote: Δs = Spatial step size = S_max/(N-1)")
        print(f"      Error should scale as O(Δs) for first-order methods or O(Δs²) for second-order methods")
        print(f"      Smaller Δs → better accuracy (until round-off errors dominate)")

    def plot_finite_difference_grid(self, M=5, N=5):
        """
        Visualize the finite difference grid structure.
        
        Parameters:
        -----------
        M : int
            Number of spatial steps (default: 5)
        N : int
            Number of time steps (default: 5)
        """
        draw_finite_difference_grid(M=M, N=N)

    def _plot_single_gbm(self, ax, num_paths=1000, num_steps=252, 
                     max_paths_display=50, risk_neutral=True, 
                     mu=None, seed=None, title=None, show_stats=True,
                     show_histogram=True, show_theoretical_pdf=True):
        """
        Core plotting logic for a single GBM simulation.
        
        Parameters:
        -----------
        ax : matplotlib.axes.Axes
            Axis to plot on
        num_paths : int
            Number of paths to simulate
        num_steps : int
            Number of time steps
        max_paths_display : int
            Maximum number of paths to display
        risk_neutral : bool
            Whether to use risk-neutral drift
        mu : float, optional
            Physical drift rate (used if risk_neutral=False)
        seed : int, optional
            Random seed for reproducibility
        title : str, optional
            Plot title
        show_stats : bool
            Whether to show statistics text box
        show_histogram : bool
            Whether to show histogram
        show_theoretical_pdf : bool
            Whether to show theoretical PDF
            
        Returns:
        --------
        dict: Contains final_prices, mean_final, std_final, theoretical_mean
        """
        # Simulate paths
        t, S_paths = self.simulate_paths(
            num_paths=num_paths,
            num_steps=num_steps,
            risk_neutral=risk_neutral,
            mu=mu,
            seed=seed
        )
        
        # Plot a subset of paths
        num_paths_to_plot = min(max_paths_display, S_paths.shape[0])
        indices = np.random.choice(S_paths.shape[0], num_paths_to_plot, replace=False)
        
        for i in indices:
            ax.plot(t, S_paths[i], alpha=0.6, linewidth=0.8)
        
        # Add grid lines for better readability
        ax.grid(True, alpha=0.3)
        
        # Get final prices for statistics and histogram
        final_prices = S_paths[:, -1]
        mean_final = np.mean(final_prices)
        std_final = np.std(final_prices)
        
        # Calculate theoretical mean
        drift_rate = self.r if risk_neutral else (mu if mu is not None else self.r)
        theoretical_mean = self.S0 * np.exp(drift_rate * self.T)
        
        # Add expected value line
        ax.axhline(y=self.S0, color='red', linestyle='--', alpha=0.8, 
                label=f'S₀ = {self.S0}')
        ax.axhline(y=theoretical_mean, color='orange', linestyle='--', 
                alpha=0.8, label=f'E[S(T)] = {theoretical_mean:.1f}')
        
        # Show histogram and theoretical PDF if requested
        if show_histogram or show_theoretical_pdf:
            # Create histogram bins
            hist_counts, bin_edges = np.histogram(final_prices, bins=50, density=True)
            bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
            
            # Define histogram width and position
            hist_width = self.T * 0.05
            hist_position = self.T + 0.005
            
            if show_histogram:
                # Normalize histogram counts
                max_hist_count = np.max(hist_counts)
                normalized_hist_counts = hist_counts / max_hist_count
                
                # Create bar histogram
                bin_width = bin_centers[1] - bin_centers[0]
                ax.barh(bin_centers, normalized_hist_counts * hist_width, 
                    left=hist_position, height=bin_width * 0.9, alpha=0.7, 
                    color='lightblue', edgecolor='darkblue', linewidth=0.3, 
                    label='Simulated Distribution')
            
            if show_theoretical_pdf:
                # Calculate theoretical lognormal distribution
                mu_ln = np.log(self.S0) + (drift_rate - 0.5 * self.sigma**2) * self.T
                sigma_ln = self.sigma * np.sqrt(self.T)
                
                S_range = np.linspace(np.min(final_prices), np.max(final_prices), 200)
                theoretical_pdf = stats.lognorm.pdf(S_range, s=sigma_ln, scale=np.exp(mu_ln))
                
                # Normalize theoretical PDF
                max_theoretical_pdf = np.max(theoretical_pdf)
                normalized_theoretical_pdf = theoretical_pdf / max_theoretical_pdf
                
                # Plot theoretical PDF
                theoretical_x = hist_position + normalized_theoretical_pdf * hist_width
                ax.plot(theoretical_x, S_range, 'r-', linewidth=3, label='Lognormal PDF')
        
        # Formatting
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Stock Price', fontsize=12)
        
        # Set title
        if title:
            ax.set_title(title, fontsize=12)
        else:
            ax.set_title('Sample GBM Paths with Final Price Distribution', fontsize=14, pad=20)
        
        # Legend
        ax.legend(loc='upper right', bbox_to_anchor=(0.98, 0.98))
        
        # Extend x-axis to accommodate histogram
        if show_histogram or show_theoretical_pdf:
            ax.set_xlim(0, self.T * 1.15)
        else:
            ax.set_xlim(0, self.T)
        
        # Add statistics text if requested
        if show_stats:
            stats_text = f"""Simulation Statistics:
    Initial Stock Price: {self.S0:.2f}
    Strike:  {self.K:.2f}
    Maturity: {self.T:.2f}
    Interest Rate: {self.r:.2f}
    Volatility: {self.sigma:.2f}
    Dividend Yield: {self.q:.2f}
    Number of Paths: {S_paths.shape[0]:,}
    Final Price Mean: {mean_final:.2f}
    Final Price Std: {std_final:.2f}
    Theoretical Mean: {theoretical_mean:.2f}"""
            
            ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                    verticalalignment='top', 
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        return {
            'final_prices': final_prices,
            'mean_final': mean_final,
            'std_final': std_final,
            'theoretical_mean': theoretical_mean
        }

    def plot_paths_and_histogram(self, num_paths=1000, num_steps=252, 
                                max_paths_display=50, risk_neutral=True, 
                                mu=None, seed=None, figsize=(12, 8), **kwargs):
        """
        Plot GBM paths with final price distribution and theoretical lognormal PDF.
        
        Parameters:
        -----------
        num_paths : int
            Number of paths to simulate (default: 1000)
        num_steps : int
            Number of time steps (default: 252)
        max_paths_display : int
            Maximum number of paths to display (default: 50)
        risk_neutral : bool
            Whether to use risk-neutral drift (default: True)
        mu : float, optional
            Physical drift rate (used if risk_neutral=False)
        seed : int, optional
            Random seed for reproducibility
        figsize : tuple
            Figure size (default: (12, 8))
        **kwargs : dict
            Additional arguments passed to _plot_single_gbm
        
        Returns:
        --------
        fig, ax : matplotlib objects
            Figure and axis objects
        """        
        fig, ax = plt.subplots(figsize=figsize)
        
        # Call core plotting method
        self._plot_single_gbm(
            ax=ax,
            num_paths=num_paths,
            num_steps=num_steps,
            max_paths_display=max_paths_display,
            risk_neutral=risk_neutral,
            mu=mu,
            seed=seed,
            **kwargs
        )
        
        plt.tight_layout()
        plt.show()
        
        return fig, ax

    def plot_gbm_comparison(self, mu, num_paths=1000, num_steps=252, 
                        max_paths_display=30, seed=42, **kwargs):
        """
        Compare risk-neutral vs real-world GBM simulations side by side.
        
        Parameters:
        -----------
        mu : float
            Real-world drift rate
        num_paths : int
            Number of paths to simulate (default: 1000)
        num_steps : int
            Number of time steps (default: 252)
        max_paths_display : int
            Max paths to display (default: 30)
        seed : int
            Random seed (default: 42)
        **kwargs : dict
            Additional arguments passed to _plot_single_gbm
        
        Returns:
        --------
        fig, (ax1, ax2) : matplotlib objects
            Figure and axis objects
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
        
        # Common parameters for both plots
        common_params = {
            'num_paths': num_paths,
            'num_steps': num_steps,
            'max_paths_display': max_paths_display,
            'show_stats': False,  # Don't show stats box in comparison view
            **kwargs
        }
        
        # Risk-neutral simulation
        self._plot_single_gbm(
            ax=ax1,
            risk_neutral=True,
            seed=seed,
            title=f'Risk-Neutral GBM (drift = {self.r:.1%})',
            **common_params
        )
        
        # Real-world simulation
        self._plot_single_gbm(
            ax=ax2,
            risk_neutral=False,
            mu=mu,
            seed=seed+1,  # Different seed for different paths
            title=f'Real-World GBM (drift = {mu:.1%})',
            **common_params
        )
        
        plt.tight_layout()
        plt.show()
        
        return fig, (ax1, ax2)

    # Properties for easy access to parameters (backward compatibility)
    @property
    def spot_price(self):
        """Current stock price"""
        return self.S0
    
    @property
    def strike_price(self):
        """Strike price"""
        return self.K
    
    @property
    def time_to_maturity(self):
        """Time to maturity"""
        return self.T
    
    @property
    def risk_free_rate(self):
        """Risk-free interest rate"""
        return self.r
    
    @property
    def volatility(self):
        """Volatility"""
        return self.sigma
    
    @property
    def dividend_yield(self):
        """Dividend yield"""
        return self.q
    
    def __repr__(self):
        """String representation of the model"""
        return (f"BlackScholes(S0={self.S0}, K={self.K}, T={self.T}, "
                f"r={self.r}, sigma={self.sigma}, q={self.q})")
    
    def summary(self):
        """Print a comprehensive summary of the model and calculated prices"""
        print(f"{'='*80}")
        print("BLACK-SCHOLES MODEL SUMMARY")
        print(f"{'='*80}")
        print(f"Parameters:")
        print(f"  Spot Price (S0):      {self.S0:>8.2f}")
        print(f"  Strike Price (K):     {self.K:>8.2f}")
        print(f"  Time to Maturity (T): {self.T:>8.2f}")
        print(f"  Risk-free Rate (r):   {self.r:>8.2f}")
        print(f"  Volatility (σ):       {self.sigma:>8.2f}")
        print(f"  Dividend Yield (q):   {self.q:>8.2f}")
        print()
        print(f"Moneyness:              {self.S0/self.K:8.2f}")
        
        # Calculate and display analytical prices
        call_price, put_price = self.price_analytical()
        print(f"\nAnalytical Prices:")
        print(f"  Call Option:          {call_price:>8.2f}")
        print(f"  Put Option:           {put_price:>8.2f}")
        
        # Calculate and display Greeks
        greeks = self.calculate_greeks()
        print(f"\nGreeks:")
        print(f"  Delta (Call/Put):     {greeks['delta_call']:>10.4f} / {greeks['delta_put']:>10.4f}")
        print(f"  Gamma:                {greeks['gamma']:>10.4f}")
        print(f"  Vega:                 {greeks['vega']:>10.4f}")
        print(f"  Theta (Call/Put):     {greeks['theta_call']:>10.4f} / {greeks['theta_put']:>10.4f}")
        print(f"  Rho (Call/Put):       {greeks['rho_call']:>10.4f} / {greeks['rho_put']:>10.4f}")
        print(f"{'='*80}")