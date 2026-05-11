# American Put

## Background

Black Scholes Explicit Amer Put

Educational script demonstrating black scholes explicit amer put concepts.

---

## What This Code Demonstrates

- Parameters ===

---

## Code

```python
"""
Black Scholes Explicit Amer Put

Educational script demonstrating black scholes explicit amer put concepts.
"""

# ============================================================================
# black_scholes_RUN_EXPLICIT_SCHEME_FOR_AMERICAN_PUT.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

# === Parameters ===


if __name__ == "__main__":
    S0 = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2
    q = 0
    S_min = 0
    S_min_log = 1e-3   # For log-space FD
    S_max = 300    # S_max should be bigger than your S_max of interest if use log space
    M = 100        # Grid points → NS = NX = M + 1
    option_type = "call"

    print(f"\n{'='*80}")
    print("🚀 ADVANCED NUMERICAL METHODS COMPARISON")
    print("="*80)
    print(f"Option Type: {option_type.upper()}")
    print(f"Stock Price (S0): ${S0}")
    print(f"Strike Price (K): ${K}")
    print(f"Time to Maturity: {T} year")
    print(f"Risk-free Rate: {r:.1%}")
    print(f"Volatility: {sigma:.1%}")
    print(f"Dividend Yield: {q:.1%}")
    print(f"Grid Points: {M+1}")
    print(f"Stock Price Range: ${S_min} - ${S_max}")
    print(f"Log-space Min: ${S_min_log}")

    # Moneyness analysis
    moneyness = S0 / K
    print(f"Moneyness (S0/K): {moneyness:.3f} ({'ATM' if 0.95 <= moneyness <= 1.05 else 'ITM' if moneyness > 1.05 else 'OTM'})")

    # === Instantiate Black-Scholes model using wrapper ===
    bs_model = bs.BlackScholes(S0, K, T, r, sigma, q)

    print(f"\n📊 Calculating option prices using different methods...")

    # === Multiple Method Comparison ===
    methods_to_test = [
        ("explicit", "Explicit FDM (Original)"),
        ("explicit_log", "Explicit FDM (Log-space)"),
        ("implicit", "Implicit FDM (Original)"),
        ("cn", "Crank-Nicolson (Original)")
    ]

    results = {}
    calculation_times = {}

    import time

    for method, description in methods_to_test:
        print(f"  🔄 Running {description}...")
        start_time = time.time()
    
        try:
            if "log" in method:
                S_grid, V_grid = bs_model.price_numerical(
                    method=method, 
                    option_type=option_type, 
                    Smin=S_min_log, 
                    Smax=S_max, 
                    NX=M+1, 
                    early_exercise=True
                )
            else:
                S_grid, V_grid = bs_model.price_numerical(
                    method=method, 
                    option_type=option_type, 
                    Smin=S_min, 
                    Smax=S_max, 
                    NS=M+1, 
                    early_exercise=True
                )
        
            calc_time = time.time() - start_time
            results[method] = (S_grid, V_grid, description)
            calculation_times[method] = calc_time
            print(f"    ✅ Completed in {calc_time:.3f} seconds")
        
        except Exception as e:
            print(f"    ❌ Failed: {str(e)}")
            continue

    # === Analytical Black-Scholes Price (Vectorized) ===
    print("  📈 Calculating analytical Black-Scholes prices...")
    if results:
        # Use the first successful result for the stock price grid
        first_method = list(results.keys())[0]
        S_reference = results[first_method][0]
    
        # Create comprehensive price grid
        S_all = S_reference
        for method in results:
            S_all = np.union1d(S_all, results[method][0])
        S_all.sort()
        S_all_safe = np.maximum(S_all, 1e-10)  # Avoid log(0)

        # Use vectorized utility function for efficiency
        if option_type == "call":
            V_exact_all = bs.bs_call_price(S_all_safe, K, T, r, sigma, q)
        else:
            V_exact_all = bs.bs_put_price(S_all_safe, K, T, r, sigma, q)

    # === Enhanced Plot Comparison ===
    print("  🎨 Generating enhanced comparison plot...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Main comparison plot
    colors = ['blue', 'green', 'purple', 'orange']
    alphas = [0.3, 0.6, 0.8, 0.9]
    linewidths = [8, 5, 3, 2]

    for i, (method, (S_grid, V_grid, description)) in enumerate(results.items()):
        ax1.plot(S_grid, V_grid, 
                label=description, 
                linewidth=linewidths[i % len(linewidths)], 
                alpha=alphas[i % len(alphas)], 
                color=colors[i % len(colors)])

    # Analytical solution
    ax1.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', linewidth=2)

    # Add reference lines
    ax1.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax1.axvline(x=S0, color='orange', linestyle=':', alpha=0.7, label=f'Current Price = ${S0}')

    # Calculate intrinsic value for reference
    if option_type == "call":
        intrinsic = np.maximum(S_all - K, 0)
    else:
        intrinsic = np.maximum(K - S_all, 0)
    ax1.plot(S_all, intrinsic, 'k:', alpha=0.5, label='Intrinsic Value')

    ax1.set_xlabel('Stock Price ($)', fontsize=12)
    ax1.set_ylabel('Option Value ($)', fontsize=12)
    ax1.set_title(f'American {option_type.capitalize()} Option: Multiple FDM Methods', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Error analysis plot
    method_names = []
    errors = []
    times = []

    for method, (S_grid, V_grid, description) in results.items():
        # Calculate analytical prices at this grid
        if option_type == "call":
            V_exact_grid = bs.bs_call_price(np.maximum(S_grid, 1e-10), K, T, r, sigma, q)
        else:
            V_exact_grid = bs.bs_put_price(np.maximum(S_grid, 1e-10), K, T, r, sigma, q)
    
        error = np.max(np.abs(V_grid - V_exact_grid))
        errors.append(error)
        times.append(calculation_times[method])
        method_names.append(description.replace(" (Original)", "").replace(" (Log-space)", " Log"))

    # Error vs computational time
    scatter = ax2.scatter(times, errors, s=100, c=range(len(times)), cmap='viridis', alpha=0.7)
    for i, name in enumerate(method_names):
        ax2.annotate(name, (times[i], errors[i]), xytext=(5, 5), 
                    textcoords='offset points', fontsize=9)

    ax2.set_xlabel('Computation Time (seconds)', fontsize=12)
    ax2.set_ylabel('Max Absolute Error ($)', fontsize=12)
    ax2.set_title('Error vs Computational Efficiency', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

    # === Comprehensive Error Analysis ===
    print(f"\n📊 COMPREHENSIVE ERROR ANALYSIS:")
    print(f"{'Method':<25} {'Max Error':<12} {'Rel Error %':<12} {'Time (s)':<10} {'Efficiency':<12}")
    print("-" * 80)

    best_error = min(errors)
    best_time = min(times)

    for i, (method, (S_grid, V_grid, description)) in enumerate(results.items()):
        if option_type == "call":
            V_exact_grid = bs.bs_call_price(np.maximum(S_grid, 1e-10), K, T, r, sigma, q)
        else:
            V_exact_grid = bs.bs_put_price(np.maximum(S_grid, 1e-10), K, T, r, sigma, q)
    
        error = errors[i]
        rel_error = error / np.mean(V_exact_grid) * 100
        comp_time = times[i]
        efficiency = (best_error / error) * (best_time / comp_time)  # Higher is better
    
        print(f"{description:<25} ${error:<11.6f} {rel_error:<11.4f} {comp_time:<9.3f} {efficiency:<11.3f}")

    # === Price at Current Stock Price ===
    print(f"\n💰 PRICES AT CURRENT STOCK PRICE (S = ${S0}):")

    # Analytical price
    analytical_call, analytical_put = bs_model.price_analytical()
    analytical_price = analytical_call if option_type == "call" else analytical_put

    print(f"  Analytical (European): ${analytical_price:.6f}")

    for method, (S_grid, V_grid, description) in results.items():
        # Find closest grid point
        idx = np.argmin(np.abs(S_grid - S0))
        price_numerical = V_grid[idx]
        error = abs(price_numerical - analytical_price)
        premium = price_numerical - analytical_price  # Early exercise premium
    
        print(f"  {description:<20}: ${price_numerical:.6f} (error: ${error:.6f}, premium: ${premium:.6f})")

    # === Advanced Analysis ===
    print(f"\n🔬 ADVANCED ANALYSIS:")

    # Early exercise premium analysis
    print(f"\nEarly Exercise Premium Analysis:")
    if option_type == "call" and q == 0:
        print(f"  • Call with no dividends: Premium should be minimal")
        print(f"  • Theoretical maximum premium: ${max(0, S0 - K):.6f}")
    elif option_type == "put":
        print(f"  • Put options: Premium can be substantial for ITM options")
        print(f"  • Theoretical maximum premium: ${max(0, K - S0):.6f}")

    # Stability analysis
    print(f"\nStability Considerations:")
    print(f"  • Explicit methods: May require smaller time steps")
    print(f"  • Implicit/CN methods: Generally more stable")
    print(f"  • Log-space: Better for extreme stock prices")

    # Greeks comparison
    greeks = bs_model.calculate_greeks()
    print(f"\nOption Greeks (European benchmark):")
    if option_type == "call":
        print(f"  Delta:  {greeks['delta_call']:.4f}")
    else:
        print(f"  Delta:  {greeks['delta_put']:.4f}")
    print(f"  Gamma:  {greeks['gamma']:.6f}")
    print(f"  Vega:   {greeks['vega']:.4f}")
    print(f"  Theta:  {greeks['theta_call' if option_type == 'call' else 'theta_put']:.4f}")

    print(f"\n{'='*80}")
    print("🎯 SUMMARY & RECOMMENDATIONS")
    print("="*80)

    # Find best method
    best_method_idx = np.argmin(errors)
    best_method = list(results.keys())[best_method_idx]
    best_description = results[best_method][2]

    print(f"🏆 Most Accurate Method: {best_description}")
    print(f"   Max Error: ${errors[best_method_idx]:.6f}")

    fastest_method_idx = np.argmin(times)
    fastest_method = list(results.keys())[fastest_method_idx]
    fastest_description = results[fastest_method][2]

    print(f"⚡ Fastest Method: {fastest_description}")
    print(f"   Computation Time: {times[fastest_method_idx]:.3f} seconds")

    print(f"\n✅ Key Insights:")
    print(f"  • American {option_type} options show early exercise premium")
    print(f"  • Log-space methods handle extreme prices better")
    print(f"  • Implicit methods generally more stable than explicit")
    print(f"  • Crank-Nicolson often provides best accuracy/stability balance")
    print(f"  • Grid resolution affects accuracy (current: {M+1} points)")

    print(f"\n🔮 Recommendations:")
    if "log" in best_method:
        print(f"  • Use log-space methods for wide price ranges")
    else:
        print(f"  • Original space adequate for moderate price ranges")

    if best_method in ["implicit", "cn"]:
        print(f"  • Implicit/CN methods recommended for stability")
    else:
        print(f"  • Explicit methods acceptable with proper time step control")

    print("="*80)
```


## Exercises

**Exercise 1.**
Consider an American put option with $S_0 = 100$, $K = 110$, $T = 1$, $r = 0.05$, $\sigma = 0.3$, and $q = 0$. Using the explicit finite difference method, explain why the early exercise boundary for this in-the-money put is higher than for an at-the-money put.

??? success "Solution to Exercise 1"
    For a deep in-the-money put ($S_0 < K$), the intrinsic value $K - S$ is already large. The early exercise boundary $S^*(t)$ is the stock price below which immediate exercise is optimal. For an ITM put, the boundary is higher because the time value of money on the strike payment $K e^{-r(T-t)}$ provides incentive to exercise early and invest the proceeds at the risk-free rate $r$. At the boundary, the discounted expected continuation value equals the intrinsic value. With higher $K$, the interest earned on the exercise proceeds $K - S^*$ is larger, pushing $S^*$ upward.

---

**Exercise 2.**
The CFL stability condition for the explicit scheme requires $\Delta t \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$. For $\sigma = 0.2$, $S_{\max} = 300$, and $M = 100$ spatial points, compute the maximum allowable time step and the minimum number of time steps for $T = 1$.

??? success "Solution to Exercise 2"
    The spatial step is $\Delta S = 300 / 100 = 3$. The CFL condition gives:

    $$
    \Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2} = \frac{9}{0.04 \times 90000} = \frac{9}{3600} = 0.0025
    $$

    The minimum number of time steps is $N \geq T / \Delta t = 1 / 0.0025 = 400$. In practice, one uses even more steps for safety since the condition is most restrictive at $S = S_{\max}$.

---

**Exercise 3.**
Explain why the log-space transformation $x = \ln S$ is advantageous for the explicit FDM applied to American puts. Write the transformed Black-Scholes PDE in terms of $V(x, t)$.

??? success "Solution to Exercise 3"
    Under $x = \ln S$, the Black-Scholes PDE becomes:

    $$
    \frac{\partial V}{\partial t} + \left(r - q - \frac{\sigma^2}{2}\right) \frac{\partial V}{\partial x} + \frac{\sigma^2}{2} \frac{\partial^2 V}{\partial x^2} - rV = 0
    $$

    The advantages are: (1) constant coefficients eliminate the non-uniform truncation error; (2) the grid in $x$-space provides natural refinement near $S = 0$ where put values change rapidly; (3) the boundary at $S = 0$ maps to $x \to -\infty$, handled more cleanly. For American puts, the early exercise region near $S = 0$ is resolved more accurately with this transformation.

---

**Exercise 4.**
Compare the early exercise premium from the original-space versus log-space explicit FDM. If the European put price is $\$5.5735$ and the American prices are $\$6.0831$ (original) and $\$6.0847$ (log-space), compute both premiums and explain which is likely more accurate.

??? success "Solution to Exercise 4"
    The early exercise premiums are:

    - Original space: $6.0831 - 5.5735 = \$0.5096$
    - Log-space: $6.0847 - 5.5735 = \$0.5112$

    The log-space method is likely more accurate because it places more grid points near small stock prices where the early exercise boundary is located. The difference of $\$0.0016$ reflects the better resolution of the sharp transition from continuation to exercise in the deep ITM region. The log-space advantage is most significant for puts because their maximum value occurs at $S = 0$.