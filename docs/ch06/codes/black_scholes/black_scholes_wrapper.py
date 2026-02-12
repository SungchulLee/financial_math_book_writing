# ============================================================================
# black_scholes/black_scholes_wrapper.py  
# ============================================================================
import matplotlib.pyplot as plt
import numpy as np
import time
from .black_scholes_formula import BlackScholesFormula
from .black_scholes_greeks import BlackScholesGreeks
from .black_scholes_implied_vol import BlackScholesImpliedVol
from .black_scholes_monte_carlo import BlackScholesMonteCarlo
from .black_scholes_numerical import BlackScholesNumericalSolver
from .black_scholes_utils import simulate_gbm_paths, draw_finite_difference_grid, theta, rho, plot_gbm_paths_with_distribution

class BlackScholes:
    """
    A unified interface for all Black-Scholes option pricing functionality.
    
    FIXED VERSION - Now properly integrates enhanced Monte Carlo while maintaining 
    complete backward compatibility.
    
    This wrapper combines analytical formulas, Greeks calculation, Monte Carlo simulation,
    finite difference methods, and implied volatility computation into a single cohesive interface.
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

    def calculate_greeks(self):
        """
        Calculate all option Greeks using analytical formulas.
        UNCHANGED API.
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
        UNCHANGED API.
        """
        return self.implied_vol.compute(
            market_price=market_price,
            sigma_0=sigma_0,
            option_type=option_type,
            **kwargs
        )

    def compare_methods(self, option_type='call', mc_paths=50000, 
                       numerical_method='cn', enhanced=True, **kwargs):
        """
        Compare option prices across different pricing methods.
        
        FIXED VERSION - Now includes enhanced Monte Carlo comparison.
        
        Parameters:
        -----------
        option_type : str
            Option type: 'call' or 'put' (default: 'call')
        mc_paths : int
            Number of Monte Carlo paths (default: 50000)
        numerical_method : str
            Numerical method for finite difference (default: 'cn')
        enhanced : bool
            Whether to use enhanced Monte Carlo (default: True)
        **kwargs : dict
            Additional arguments for numerical methods
            
        Returns:
        --------
        dict: Comparison results with prices from different methods
        """
        # Analytical price
        call_analytical, put_analytical = self.price_analytical()
        analytical_price = call_analytical if option_type == 'call' else put_analytical
        
        # Monte Carlo price (enhanced or legacy)
        mc_results = self.price_monte_carlo(
            num_paths=mc_paths, 
            plot_histogram=False,
            enhanced=enhanced
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
        
        # Calculate standard error for Monte Carlo
        mc_std_error = mc_std / np.sqrt(mc_paths)
        
        return {
            'analytical': analytical_price,
            'monte_carlo': {
                'price': mc_price,
                'std_error': mc_std_error,
                'confidence_interval': (mc_price - 1.96 * mc_std_error,
                                       mc_price + 1.96 * mc_std_error),
                'enhanced': enhanced
            },
            'numerical': numerical_price,
            'differences': {
                'mc_vs_analytical': abs(mc_price - analytical_price),
                'numerical_vs_analytical': abs(numerical_price - analytical_price),
                'mc_vs_numerical': abs(mc_price - numerical_price)
            }
        }
    
    def compare_monte_carlo_modes(self, num_paths=50000, seed=42, **kwargs):
        """
        Compare enhanced vs standard Monte Carlo modes side by side.
        
        NEW METHOD - Demonstrates the variance reduction effectiveness.
        
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
        dict : Comparison results showing variance reduction effectiveness
        """
        return self.monte_carlo.compare_modes(num_paths=num_paths, seed=seed, **kwargs)
    
    def plot_convergence(self, option_type='call', methods=['explicit', 'implicit', 'cn'],
                        grid_points=None, S_max=None, **kwargs):
        """
        Enhanced convergence plot with detailed analysis showing error vs step size.
        UNCHANGED from Version 1 behavior.
        """
        # Remove 'grid_sizes' from kwargs if present (to avoid conflicts)
        clean_kwargs = {k: v for k, v in kwargs.items() if k != 'grid_sizes'}
        
        # Default comprehensive range of grid points
        if grid_points is None:
            grid_points = [25, 50, 75, 100, 150, 200, 300, 400]
        
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
                    
                    # Use original numerical methods with original defaults
                    if method.lower() == 'explicit':
                        S_grid, option_values = self.numerical.explicit(
                            option_type=option_type, 
                            Smin=0, Smax=S_max,
                            NS=num_points,
                            **clean_kwargs
                        )
                    elif method.lower() == 'implicit':
                        S_grid, option_values = self.numerical.implicit(
                            option_type=option_type,
                            Smin=1e-3, Smax=S_max,
                            NS=num_points,
                            **clean_kwargs
                        )
                    elif method.lower() == 'cn':
                        S_grid, option_values = self.numerical.cn(
                            option_type=option_type,
                            Smin=0, Smax=S_max,
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
        
        # Format plots
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
        
        # Plot 2 specific formatting
        ax2.set_xlabel('Computation Time (seconds)', fontsize=14, fontweight='bold')
        ax2.set_title('Efficiency Analysis\n(Error vs Computation Time)', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        return all_errors

    def plot_finite_difference_grid(self, M=5, N=5):
        """
        Visualize the finite difference grid structure.
        UNCHANGED.
        """
        draw_finite_difference_grid(M=M, N=N)

    def plot_gbm_comparison(self, mu, num_paths=1000, num_steps=252, 
                        max_paths_display=30, seed=42, **kwargs):
        """
        Compare risk-neutral vs real-world GBM simulations side by side.
        UNCHANGED from original.
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

        for risk_neutral, ax in zip((True, False), (ax1, ax2)):
            t, S_paths = self.simulate_paths(
                num_paths=num_paths,
                num_steps=num_steps,
                risk_neutral=risk_neutral,
                mu=mu,
                seed=seed
                )
            if risk_neutral:
                title = f'Sample GBM Paths with Final Price Distribution\nunder Risk Neutral Measure r = {self.r}'
            else:
                title = f'Sample GBM Paths with Final Price Distribution\nunder Physical Measure mu = {mu}'

            stats = plot_gbm_paths_with_distribution(
                t=t, S_paths=S_paths, S0=self.S0, T=self.T, 
                r=self.r, sigma=self.sigma, q=self.q, K=self.K,
                ax=ax, max_paths_display=max_paths_display,
                risk_neutral=risk_neutral, mu=mu, title=title, **kwargs
            )
        
        plt.tight_layout()
        plt.show()
        
        return fig, (ax1, ax2)

    def plot_paths_and_histogram(self, num_paths=1000, num_steps=252, 
                                max_paths_display=50, risk_neutral=True, 
                                mu=None, seed=None, figsize=(12, 8), **kwargs):
        """
        Plot GBM paths with final price distribution and theoretical lognormal PDF.
        UNCHANGED from original.
        """ 

        # Simulate paths
        t, S_paths = self.simulate_paths(
            num_paths=num_paths,
            num_steps=num_steps,
            risk_neutral=risk_neutral,
            mu=mu,
            seed=seed
            )
               
        fig, ax = plt.subplots(figsize=figsize)

        # Use utility function
        stats = plot_gbm_paths_with_distribution(
            t=t, S_paths=S_paths, S0=self.S0, T=self.T, 
            r=self.r, sigma=self.sigma, q=self.q, K=self.K,
            ax=ax, max_paths_display=max_paths_display,
            risk_neutral=risk_neutral, mu=mu, **kwargs
        )
        
        plt.tight_layout()
        plt.show()
        
        return fig, ax

    def price_analytical(self):
        """
        Calculate European option prices using analytical Black-Scholes formula.
        UNCHANGED API.
        """
        return self.formula.price()
    
    def price_monte_carlo(self, num_paths=10000, steps_per_year=252, seed=None, 
                         plot_histogram=True, enhanced=True, **kwargs):
        """
        Price options using Monte Carlo simulation.
        
        FIXED API - Now supports both enhanced and legacy modes.
        
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
            enhanced=enhanced,
            **kwargs
        )
    
    def price_numerical(self, method='explicit', option_type='put', **kwargs):
        """
        Price options using finite difference methods.
        UNCHANGED API.
        """
        return self.numerical.solve(method=method, option_type=option_type, **kwargs)
    
    def __repr__(self):
        """String representation of the model"""
        return (f"BlackScholes(S0={self.S0}, K={self.K}, T={self.T}, "
                f"r={self.r}, sigma={self.sigma}, q={self.q})")
    
    def simulate_paths(self, num_paths=1000, num_steps=252, risk_neutral=True, 
                      mu=None, seed=None, **kwargs):
        """
        Simulate stock price paths using geometric Brownian motion.
        UNCHANGED API.
        """
        return simulate_gbm_paths(
            S0=self.S0,
            T=self.T,
            r=self.r,
            sigma=self.sigma,
            num_paths=num_paths,
            num_steps=num_steps,
            risk_neutral=risk_neutral,
            mu=mu,
            seed=seed,
            **kwargs
        )
    
    def summary(self):
        """Print a comprehensive summary of the model and calculated prices"""
        # Calculate and display analytical prices
        call_price, put_price = self.price_analytical()
        
        # Calculate and display Greeks
        greeks = self.calculate_greeks()
        
        print(f"BLACK-SCHOLES MODEL SUMMARY")
        print(f"Parameters: S0={self.S0}, K={self.K}, T={self.T}, r={self.r}, σ={self.sigma}, q={self.q}")
        print(f"Moneyness:          {self.S0/self.K:>10.4f}")
        print(f"Option Price (C/P): {call_price:>10.4f}     {put_price:>10.4f}")
        print(f"Delta (C/P):        {greeks['delta_call']:>10.4f}     {greeks['delta_put']:>10.4f}")
        print(f"Gamma:              {greeks['gamma']:>10.4f}")
        print(f"Vega:               {greeks['vega']:>10.4f}")
        print(f"Theta (C/P):        {greeks['theta_call']:>10.4f}     {greeks['theta_put']:>10.4f}")
        print(f"Rho (C/P):          {greeks['rho_call']:>10.4f}     {greeks['rho_put']:>10.4f}")
    
    @property
    def dividend_yield(self):
        """Dividend yield"""
        return self.q
    
    @property
    def risk_free_rate(self):
        """Risk-free interest rate"""
        return self.r
    
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
    def volatility(self):
        """Volatility"""
        return self.sigma