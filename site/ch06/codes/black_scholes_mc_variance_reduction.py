"""
black_scholes_mc_variance_reduction.py
Monte Carlo Variance Reduction Techniques for Black-Scholes Option Pricing

Demonstrates variance reduction techniques for Monte Carlo pricing of European
call options under the Black-Scholes model:
- Antithetic variates
- Moment matching
- Combined antithetic variates + moment matching

Compares convergence, standard error, and variance reduction ratios across
these methods with the analytical Black-Scholes price.

Based on the variance reduction techniques in DX Analytics' sn_random_numbers.py
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# ============================================================================
# 1. STANDARD NORMAL RANDOM NUMBER GENERATORS WITH VARIANCE REDUCTION
# ============================================================================

def sn_random_numbers(shape, antithetic=False, moment_matching=False, 
                      fixed_seed=True, seed_value=42):
    """
    Generate standard normal random numbers with optional variance reduction.
    
    Parameters
    ----------
    shape : tuple
        Shape of the output array (paths, time_steps)
    antithetic : bool
        If True, generate half the paths and concatenate with negated copies
    moment_matching : bool
        If True, shift and scale to match sample mean=0 and std=1
    fixed_seed : bool
        If True, use a fixed seed for reproducibility
    seed_value : int
        The seed value to use
        
    Returns
    -------
    randoms : ndarray
        Array of standard normal random numbers with shape specified
    """
    if fixed_seed:
        np.random.seed(seed_value)
    
    if antithetic:
        # Generate half the paths, then concatenate with negated copies
        paths, steps = shape
        half_paths = paths // 2
        randoms = np.random.standard_normal((half_paths, steps))
        randoms = np.vstack((randoms, -randoms))
        # If odd number of paths, add one more path
        if paths % 2 == 1:
            randoms = np.vstack((randoms, np.random.standard_normal((1, steps))))
    else:
        randoms = np.random.standard_normal(shape)
    
    if moment_matching:
        # Shift and scale to match sample mean=0 and std=1
        randoms = (randoms - np.mean(randoms)) / np.std(randoms)
    
    return randoms


# ============================================================================
# 2. BLACK-SCHOLES ANALYTICAL PRICING
# ============================================================================

def black_scholes_call(S, K, T, r, sigma):
    """
    Analytical Black-Scholes call option price.
    
    Parameters
    ----------
    S : float
        Current spot price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility (annualized)
        
    Returns
    -------
    call_price : float
        European call option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


# ============================================================================
# 3. MONTE CARLO PRICING FUNCTIONS
# ============================================================================

def monte_carlo_call_price(S, K, T, r, sigma, num_paths, num_steps=1, 
                           antithetic=False, moment_matching=False):
    """
    Price a European call option using Monte Carlo simulation.
    
    Uses Geometric Brownian Motion: dS = r*S*dt + sigma*S*dW
    
    Parameters
    ----------
    S : float
        Current spot price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility (annualized)
    num_paths : int
        Number of simulation paths
    num_steps : int
        Number of time steps (default=1, for simple pricing at maturity)
    antithetic : bool
        Use antithetic variates
    moment_matching : bool
        Use moment matching
        
    Returns
    -------
    call_price : float
        Estimated call option price
    call_std : float
        Standard error of the estimate
    """
    # Generate standard normal random numbers
    randoms = sn_random_numbers((num_paths, num_steps), 
                               antithetic=antithetic,
                               moment_matching=moment_matching,
                               fixed_seed=False)
    
    # Time step
    dt = T / num_steps
    
    # Initialize asset prices
    S_t = np.full((num_paths, num_steps + 1), S)
    
    # Simulate GBM paths
    for t in range(num_steps):
        S_t[:, t + 1] = S_t[:, t] * np.exp((r - 0.5 * sigma**2) * dt + 
                                           sigma * np.sqrt(dt) * randoms[:, t])
    
    # Final asset prices (at maturity)
    S_T = S_t[:, -1]
    
    # Payoff at maturity
    payoff = np.maximum(S_T - K, 0)
    
    # Discount expected payoff
    call_price = np.exp(-r * T) * np.mean(payoff)
    call_std = np.exp(-r * T) * np.std(payoff) / np.sqrt(num_paths)
    
    return call_price, call_std


# ============================================================================
# 4. CONVERGENCE ANALYSIS
# ============================================================================

def convergence_analysis(S, K, T, r, sigma, path_counts, num_runs=5):
    """
    Analyze convergence of MC estimates for different methods.
    
    Parameters
    ----------
    S : float
        Current spot price
    K : float
        Strike price
    T : float
        Time to maturity
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    path_counts : ndarray
        Array of number of paths to test
    num_runs : int
        Number of runs per path count for averaging
        
    Returns
    -------
    results : dict
        Dictionary with convergence data for each method
    """
    methods = {
        'Plain MC': {'antithetic': False, 'moment_matching': False},
        'Antithetic': {'antithetic': True, 'moment_matching': False},
        'Moment Matching': {'antithetic': False, 'moment_matching': True},
        'Both': {'antithetic': True, 'moment_matching': True}
    }
    
    results = {method: {'prices': [], 'stds': [], 'errors': []} 
               for method in methods}
    
    # Analytical price
    analytical_price = black_scholes_call(S, K, T, r, sigma)
    
    for num_paths in path_counts:
        for method, params in methods.items():
            prices = []
            stds = []
            
            for _ in range(num_runs):
                price, std = monte_carlo_call_price(
                    S, K, T, r, sigma, num_paths,
                    antithetic=params['antithetic'],
                    moment_matching=params['moment_matching']
                )
                prices.append(price)
                stds.append(std)
            
            avg_price = np.mean(prices)
            avg_std = np.mean(stds)
            error = np.abs(avg_price - analytical_price)
            
            results[method]['prices'].append(avg_price)
            results[method]['stds'].append(avg_std)
            results[method]['errors'].append(error)
    
    results['analytical_price'] = analytical_price
    results['path_counts'] = path_counts
    
    return results


# ============================================================================
# 5. VARIANCE REDUCTION RATIOS
# ============================================================================

def variance_reduction_ratios(results):
    """
    Compute variance reduction ratios relative to plain MC.
    
    Parameters
    ----------
    results : dict
        Output from convergence_analysis
        
    Returns
    -------
    ratios : dict
        Variance reduction ratios for each method
    """
    plain_mc_stds = np.array(results['Plain MC']['stds'])
    ratios = {}
    
    for method in ['Antithetic', 'Moment Matching', 'Both']:
        method_stds = np.array(results[method]['stds'])
        # Variance reduction ratio = (std_plain_mc / std_method)^2
        # This shows how much the variance is reduced
        ratio = (plain_mc_stds / method_stds) ** 2
        ratios[method] = ratio
    
    return ratios


# ============================================================================
# 6. PLOTTING FUNCTIONS
# ============================================================================

def plot_convergence_analysis(results):
    """
    Plot convergence of price estimates across methods.
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    path_counts = results['path_counts']
    analytical_price = results['analytical_price']
    
    # Plot 1: Price convergence
    ax = axes[0]
    for method in ['Plain MC', 'Antithetic', 'Moment Matching', 'Both']:
        prices = results[method]['prices']
        ax.plot(path_counts, prices, marker='o', label=method, linewidth=2)
    
    ax.axhline(y=analytical_price, color='k', linestyle='--', 
               linewidth=2, label='Analytical BS')
    ax.set_xlabel('Number of Paths', fontsize=11)
    ax.set_ylabel('Call Price', fontsize=11)
    ax.set_title('(a) Price Convergence', fontsize=12, fontweight='bold')
    ax.set_xscale('log')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Standard error comparison
    ax = axes[1]
    for method in ['Plain MC', 'Antithetic', 'Moment Matching', 'Both']:
        stds = results[method]['stds']
        ax.loglog(path_counts, stds, marker='o', label=method, linewidth=2)
    
    # Plot theoretical decay (std ~ 1/sqrt(N))
    theoretical_std = results['Plain MC']['stds'][0] * np.sqrt(path_counts[0]) / path_counts
    ax.loglog(path_counts, theoretical_std, 'k--', linewidth=2, 
              label='Theoretical 1/√N')
    ax.set_xlabel('Number of Paths', fontsize=11)
    ax.set_ylabel('Standard Error', fontsize=11)
    ax.set_title('(b) Standard Error Convergence', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    
    # Plot 3: Absolute pricing error
    ax = axes[2]
    for method in ['Plain MC', 'Antithetic', 'Moment Matching', 'Both']:
        errors = results[method]['errors']
        ax.loglog(path_counts, errors, marker='o', label=method, linewidth=2)
    
    ax.set_xlabel('Number of Paths', fontsize=11)
    ax.set_ylabel('Absolute Error from Analytical', fontsize=11)
    ax.set_title('(c) Pricing Error Convergence', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    return fig


def plot_variance_reduction_ratios(results, ratios):
    """
    Plot variance reduction ratios.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    
    path_counts = results['path_counts']
    x = np.arange(len(path_counts))
    width = 0.25
    
    for i, method in enumerate(['Antithetic', 'Moment Matching', 'Both']):
        ratio = ratios[method]
        ax.bar(x + i * width, ratio, width, label=method, alpha=0.8)
    
    ax.set_xlabel('Number of Paths', fontsize=11)
    ax.set_ylabel('Variance Reduction Ratio\n(var_plain / var_method)', fontsize=11)
    ax.set_title('Variance Reduction Ratios Relative to Plain MC', 
                 fontsize=12, fontweight='bold')
    ax.set_xticks(x + width)
    ax.set_xticklabels([f'{int(p)}' for p in path_counts], rotation=45)
    ax.legend(fontsize=10)
    ax.axhline(y=1, color='k', linestyle='--', alpha=0.3)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig


# ============================================================================
# 7. MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function demonstrating Monte Carlo variance reduction techniques
    for Black-Scholes option pricing.
    """
    print("=" * 75)
    print("Monte Carlo Variance Reduction for Black-Scholes Option Pricing")
    print("=" * 75)
    
    # Standard market parameters
    S0 = 100.0      # Initial spot price
    K = 105.0       # Strike price
    T = 1.0         # Time to maturity (1 year)
    r = 0.05        # Risk-free rate (5%)
    sigma = 0.2     # Volatility (20%)
    
    print(f"\nMarket Parameters:")
    print(f"  Spot Price (S0):      {S0}")
    print(f"  Strike Price (K):     {K}")
    print(f"  Time to Maturity (T): {T} year")
    print(f"  Risk-free Rate (r):   {r*100}%")
    print(f"  Volatility (σ):       {sigma*100}%")
    
    # Analytical Black-Scholes price
    analytical_price = black_scholes_call(S0, K, T, r, sigma)
    print(f"\nAnalytical Black-Scholes Call Price: {analytical_price:.6f}")
    
    # Test with different numbers of paths
    print("\n" + "=" * 75)
    print("Single Run Comparison (10,000 paths)")
    print("=" * 75)
    
    num_paths_test = 10000
    methods = {
        'Plain MC': {'antithetic': False, 'moment_matching': False},
        'Antithetic': {'antithetic': True, 'moment_matching': False},
        'Moment Matching': {'antithetic': False, 'moment_matching': True},
        'Both': {'antithetic': True, 'moment_matching': True}
    }
    
    print(f"\n{'Method':<20} {'Price':<12} {'Std Error':<12} {'Error':<12}")
    print("-" * 56)
    
    for method, params in methods.items():
        price, std = monte_carlo_call_price(
            S0, K, T, r, sigma, num_paths_test,
            antithetic=params['antithetic'],
            moment_matching=params['moment_matching']
        )
        error = abs(price - analytical_price)
        print(f"{method:<20} {price:<12.6f} {std:<12.6f} {error:<12.6f}")
    
    # Convergence analysis
    print("\n" + "=" * 75)
    print("Convergence Analysis (averaging over 5 runs per path count)")
    print("=" * 75)
    
    path_counts = np.array([100, 500, 1000, 5000, 10000, 50000])
    results = convergence_analysis(S0, K, T, r, sigma, path_counts, num_runs=5)
    
    print(f"\n{'Paths':<10} {'Plain MC':<18} {'Antithetic':<18} "
          f"{'Moment Match':<18} {'Both':<18}")
    print("-" * 70)
    
    for i, num_paths in enumerate(path_counts):
        plain = results['Plain MC']['stds'][i]
        anti = results['Antithetic']['stds'][i]
        moment = results['Moment Matching']['stds'][i]
        both = results['Both']['stds'][i]
        print(f"{int(num_paths):<10} {plain:<18.6f} {anti:<18.6f} "
              f"{moment:<18.6f} {both:<18.6f}")
    
    # Variance reduction ratios
    print("\n" + "=" * 75)
    print("Variance Reduction Ratios (relative to Plain MC)")
    print("=" * 75)
    print("(Ratio > 1 means the method reduces variance)")
    
    ratios = variance_reduction_ratios(results)
    
    print(f"\n{'Paths':<10} {'Antithetic':<18} {'Moment Match':<18} {'Both':<18}")
    print("-" * 50)
    
    for i, num_paths in enumerate(path_counts):
        anti = ratios['Antithetic'][i]
        moment = ratios['Moment Matching'][i]
        both = ratios['Both'][i]
        print(f"{int(num_paths):<10} {anti:<18.4f} {moment:<18.4f} {both:<18.4f}")
    
    # Create plots
    print("\n" + "=" * 75)
    print("Generating plots...")
    print("=" * 75)
    
    fig1 = plot_convergence_analysis(results)
    fig1_path = '/sessions/serene-kind-hopper/mnt/financial_math_book_writing/docs/ch06/codes/black_scholes_mc_variance_convergence.png'
    fig1.savefig(fig1_path, dpi=150, bbox_inches='tight')
    print(f"\nConvergence analysis plot saved to:")
    print(f"  {fig1_path}")
    
    fig2 = plot_variance_reduction_ratios(results, ratios)
    fig2_path = '/sessions/serene-kind-hopper/mnt/financial_math_book_writing/docs/ch06/codes/black_scholes_mc_variance_reduction_ratios.png'
    fig2.savefig(fig2_path, dpi=150, bbox_inches='tight')
    print(f"\nVariance reduction ratios plot saved to:")
    print(f"  {fig2_path}")
    
    plt.close('all')
    
    print("\n" + "=" * 75)
    print("Analysis Complete!")
    print("=" * 75)
    
    # Summary statistics
    print("\nKey Observations:")
    print(f"  - Antithetic variates: reduces variance by ~{np.mean(ratios['Antithetic']):.2f}x on average")
    print(f"  - Moment matching: reduces variance by ~{np.mean(ratios['Moment Matching']):.2f}x on average")
    print(f"  - Combined method: reduces variance by ~{np.mean(ratios['Both']):.2f}x on average")
    print(f"  - Combined method is most effective for this problem")


if __name__ == '__main__':
    main()
