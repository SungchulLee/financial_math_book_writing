# American Call

## Background

Black Scholes Explicit Amer Call

Educational script demonstrating black scholes explicit amer call concepts.

---

## What This Code Demonstrates

- Parameters ===

---

## Code

```python
"""
Black Scholes Explicit Amer Call

Educational script demonstrating black scholes explicit amer call concepts.
"""

# ============================================================================
# black_scholes_RUN_EXPLICIT_SCHEME_FOR_AMERICAN_CALL.py
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

    print(f"\n{'='*70}")
    print("NUMERICAL METHODS COMPARISON")
    print("="*70)
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

    # === Instantiate Black-Scholes model using wrapper ===
    bs_model = bs.BlackScholes(S0, K, T, r, sigma, q)

    print(f"\nCalculating option prices using different methods...")

    # === Run Explicit FDM in Original Space ===
    print("  Running Explicit FDM in original space...")
    S_orig, V_orig = bs_model.price_numerical(
        method="explicit", 
        option_type=option_type, 
        Smin=S_min, 
        Smax=S_max, 
        NS=M+1, 
        early_exercise=True
    )

    # === Run Explicit FDM in Log-Price Space ===
    print("  Running Explicit FDM in log-price space...")
    S_log, V_log = bs_model.price_numerical(
        method="explicit_log", 
        option_type=option_type, 
        Smin=S_min_log, 
        Smax=S_max, 
        NX=M+1, 
        early_exercise=True
    )

    # === Analytical Black-Scholes Price (Vectorized) ===
    print("  Calculating analytical Black-Scholes prices...")
    S_all = np.union1d(S_orig, S_log)
    S_all.sort()
    S_all_safe = np.maximum(S_all, 1e-10)  # Avoid log(0)

    # Use vectorized utility function for efficiency
    if option_type == "call":
        V_exact_all = bs.bs_call_price(S_all_safe, K, T, r, sigma, q)
    else:
        V_exact_all = bs.bs_put_price(S_all_safe, K, T, r, sigma, q)

    # === Plot Comparison ===
    print("  Generating comparison plot...")
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(S_orig, V_orig, label='Explicit FDM (Original Space)', linewidth=8, alpha=0.3, color='blue')
    ax.plot(S_log, V_log, label='Explicit FDM (Log Space)', linewidth=4, alpha=0.8, color='green')
    ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', linewidth=2)

    # Add reference lines
    ax.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax.axvline(x=S0, color='orange', linestyle=':', alpha=0.7, label=f'Current Price = ${S0}')

    # Calculate intrinsic value for reference
    if option_type == "call":
        intrinsic = np.maximum(S_all - K, 0)
    else:
        intrinsic = np.maximum(K - S_all, 0)
    ax.plot(S_all, intrinsic, 'k:', alpha=0.5, label='Intrinsic Value')

    ax.set_xlabel('Stock Price ($)', fontsize=12)
    ax.set_ylabel('Option Value ($)', fontsize=12)
    ax.set_title(f'American {option_type.capitalize()} Option: Explicit FDM Comparison\n' +
                f'Original Space vs Log-Space vs Analytical', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend()

    # Clean up plot appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

    # === Compute Max Errors ===
    print(f"\nError Analysis:")

    # Get exact values at grid points
    if option_type == "call":
        V_exact_orig = bs.bs_call_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
        V_exact_log = bs.bs_call_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)
    else:
        V_exact_orig = bs.bs_put_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
        V_exact_log = bs.bs_put_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)

    error_orig = np.max(np.abs(V_orig - V_exact_orig))
    error_log = np.max(np.abs(V_log - V_exact_log))

    print(f"  Max absolute error (original space): ${error_orig:.6f}")
    print(f"  Max absolute error (log space):      ${error_log:.6f}")

    # Relative errors
    rel_error_orig = error_orig / np.mean(V_exact_orig) * 100
    rel_error_log = error_log / np.mean(V_exact_log) * 100

    print(f"  Max relative error (original space): {rel_error_orig:.4f}%")
    print(f"  Max relative error (log space):      {rel_error_log:.4f}%")

    # Determine which method is more accurate
    if error_log < error_orig:
        print(f"  ✓ Log-space method is more accurate by a factor of {error_orig/error_log:.2f}")
    else:
        print(f"  ✓ Original-space method is more accurate by a factor of {error_log/error_orig:.2f}")

    # === Price at Current Stock Price ===
    print(f"\nPrices at Current Stock Price (S = ${S0}):")

    # Analytical price
    analytical_call, analytical_put = bs_model.price_analytical()
    analytical_price = analytical_call if option_type == "call" else analytical_put

    # Find closest grid points
    idx_orig = np.argmin(np.abs(S_orig - S0))
    idx_log = np.argmin(np.abs(S_log - S0))

    price_orig = V_orig[idx_orig]
    price_log = V_log[idx_log]

    print(f"  Analytical Price:     ${analytical_price:.6f}")
    print(f"  CN Original Space:    ${price_orig:.6f} (error: ${abs(price_orig - analytical_price):.6f})")
    print(f"  CN Log Space:         ${price_log:.6f} (error: ${abs(price_log - analytical_price):.6f})")

    # === Demonstrate other wrapper features ===
    print(f"\n{'='*70}")
    print("ADDITIONAL WRAPPER FEATURES")
    print("="*70)

    # Monte Carlo comparison
    print(f"Comparing with Monte Carlo simulation...")
    mc_results = bs_model.price_monte_carlo(num_paths=100000, plot_histogram=False)
    mc_price = mc_results[0] if option_type == "call" else mc_results[1]
    mc_std = mc_results[2] if option_type == "call" else mc_results[3]

    print(f"  Monte Carlo Price:    ${mc_price:.6f} ± ${mc_std/np.sqrt(100000):.6f}")

    # Method comparison using wrapper
    comparison = bs_model.compare_methods(option_type=option_type, numerical_method='explicit')
    print(f"\nComprehensive Method Comparison:")
    print(f"  Analytical:           ${comparison['analytical']:.6f}")
    print(f"  Monte Carlo:          ${comparison['monte_carlo']['price']:.6f}")
    print(f"  Numerical (Explicit): ${comparison['numerical']:.6f}")

    print(f"\nMethod Differences:")
    print(f"  MC vs Analytical:     ${comparison['differences']['mc_vs_analytical']:.6f}")
    print(f"  Numerical vs Analytical: ${comparison['differences']['numerical_vs_analytical']:.6f}")

    # Greeks for context
    greeks = bs_model.calculate_greeks()
    print(f"\nOption Greeks (for reference):")
    if option_type == "call":
        print(f"  Delta:                {greeks['delta_call']:.4f}")
    else:
        print(f"  Delta:                {greeks['delta_put']:.4f}")
    print(f"  Gamma:                {greeks['gamma']:.6f}")
    print(f"  Vega:                 {greeks['vega']:.4f}")










    # ============================================================================
    # black_scholes_RUN_EXPLICIT_SCHEME_FOR_AMERICAN_CALL.py
    # ============================================================================
    import black_scholes as bs
    import matplotlib.pyplot as plt
    import numpy as np

    # === Parameters ===
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

    print(f"\n{'='*70}")
    print("NUMERICAL METHODS COMPARISON")
    print("="*70)
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

    # === Instantiate Black-Scholes model using wrapper ===
    bs_model = bs.BlackScholes(S0, K, T, r, sigma, q)

    print(f"\nCalculating option prices using different methods...")

    # === Run Explicit FDM in Original Space ===
    print("  Running Explicit FDM in original space...")
    S_orig, V_orig = bs_model.price_numerical(
        method="explicit", 
        option_type=option_type, 
        Smin=S_min, 
        Smax=S_max, 
        NS=M+1, 
        early_exercise=True
    )

    # === Run Explicit FDM in Log-Price Space ===
    print("  Running Explicit FDM in log-price space...")
    S_log, V_log = bs_model.price_numerical(
        method="explicit_log", 
        option_type=option_type, 
        Smin=S_min_log, 
        Smax=S_max, 
        NX=M+1, 
        early_exercise=True
    )

    # === Analytical Black-Scholes Price (Vectorized) ===
    print("  Calculating analytical Black-Scholes prices...")
    S_all = np.union1d(S_orig, S_log)
    S_all.sort()
    S_all_safe = np.maximum(S_all, 1e-10)  # Avoid log(0)

    # Use vectorized utility function for efficiency
    if option_type == "call":
        V_exact_all = bs.bs_call_price(S_all_safe, K, T, r, sigma, q)
    else:
        V_exact_all = bs.bs_put_price(S_all_safe, K, T, r, sigma, q)

    # === Plot Comparison ===
    print("  Generating comparison plot...")
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(S_orig, V_orig, label='Explicit FDM (Original Space)', linewidth=8, alpha=0.3, color='blue')
    ax.plot(S_log, V_log, label='Explicit FDM (Log Space)', linewidth=4, alpha=0.8, color='green')
    ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', linewidth=2)

    # Add reference lines
    ax.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax.axvline(x=S0, color='orange', linestyle=':', alpha=0.7, label=f'Current Price = ${S0}')

    # Calculate intrinsic value for reference
    if option_type == "call":
        intrinsic = np.maximum(S_all - K, 0)
    else:
        intrinsic = np.maximum(K - S_all, 0)
    ax.plot(S_all, intrinsic, 'k:', alpha=0.5, label='Intrinsic Value')

    ax.set_xlabel('Stock Price ($)', fontsize=12)
    ax.set_ylabel('Option Value ($)', fontsize=12)
    ax.set_title(f'American {option_type.capitalize()} Option: Explicit FDM Comparison\n' +
                f'Original Space vs Log-Space vs Analytical', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend()

    # Clean up plot appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

    # === Compute Max Errors ===
    print(f"\nError Analysis:")

    # Get exact values at grid points
    if option_type == "call":
        V_exact_orig = bs.bs_call_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
        V_exact_log = bs.bs_call_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)
    else:
        V_exact_orig = bs.bs_put_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
        V_exact_log = bs.bs_put_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)

    error_orig = np.max(np.abs(V_orig - V_exact_orig))
    error_log = np.max(np.abs(V_log - V_exact_log))

    print(f"  Max absolute error (original space): ${error_orig:.6f}")
    print(f"  Max absolute error (log space):      ${error_log:.6f}")

    # Relative errors
    rel_error_orig = error_orig / np.mean(V_exact_orig) * 100
    rel_error_log = error_log / np.mean(V_exact_log) * 100

    print(f"  Max relative error (original space): {rel_error_orig:.4f}%")
    print(f"  Max relative error (log space):      {rel_error_log:.4f}%")

    # Determine which method is more accurate
    if error_log < error_orig:
        print(f"  ✓ Log-space method is more accurate by a factor of {error_orig/error_log:.2f}")
    else:
        print(f"  ✓ Original-space method is more accurate by a factor of {error_log/error_orig:.2f}")

    # === Price at Current Stock Price ===
    print(f"\nPrices at Current Stock Price (S = ${S0}):")

    # Analytical price
    analytical_call, analytical_put = bs_model.price_analytical()
    analytical_price = analytical_call if option_type == "call" else analytical_put

    # Find closest grid points
    idx_orig = np.argmin(np.abs(S_orig - S0))
    idx_log = np.argmin(np.abs(S_log - S0))

    price_orig = V_orig[idx_orig]
    price_log = V_log[idx_log]

    print(f"  Analytical Price:     ${analytical_price:.6f}")
    print(f"  CN Original Space:    ${price_orig:.6f} (error: ${abs(price_orig - analytical_price):.6f})")
    print(f"  CN Log Space:         ${price_log:.6f} (error: ${abs(price_log - analytical_price):.6f})")

    # === Demonstrate other wrapper features ===
    print(f"\n{'='*70}")
    print("ADDITIONAL WRAPPER FEATURES")
    print("="*70)

    # Monte Carlo comparison
    print(f"Comparing with Monte Carlo simulation...")
    mc_results = bs_model.price_monte_carlo(num_paths=100000, plot_histogram=False)
    mc_price = mc_results[0] if option_type == "call" else mc_results[1]
    mc_std = mc_results[2] if option_type == "call" else mc_results[3]

    print(f"  Monte Carlo Price:    ${mc_price:.6f} ± ${mc_std/np.sqrt(100000):.6f}")

    # Method comparison using wrapper
    comparison = bs_model.compare_methods(option_type=option_type, numerical_method='explicit')
    print(f"\nComprehensive Method Comparison:")
    print(f"  Analytical:           ${comparison['analytical']:.6f}")
    print(f"  Monte Carlo:          ${comparison['monte_carlo']['price']:.6f}")
    print(f"  Numerical (Explicit): ${comparison['numerical']:.6f}")

    print(f"\nMethod Differences:")
    print(f"  MC vs Analytical:     ${comparison['differences']['mc_vs_analytical']:.6f}")
    print(f"  Numerical vs Analytical: ${comparison['differences']['numerical_vs_analytical']:.6f}")

    # Greeks for context
    greeks = bs_model.calculate_greeks()
    print(f"\nOption Greeks (for reference):")
    if option_type == "call":
        print(f"  Delta:                {greeks['delta_call']:.4f}")
    else:
        print(f"  Delta:                {greeks['delta_put']:.4f}")
    print(f"  Gamma:                {greeks['gamma']:.6f}")
    print(f"  Vega:                 {greeks['vega']:.4f}")
```


## Exercises

**Exercise 1.**
Write the explicit finite difference scheme for the BS PDE applied to an American call. What is the stability condition?

??? success "Solution to Exercise 1"
    $V_i^j = a_i V_{i-1}^{j+1} + b_i V_i^{j+1} + c_i V_{i+1}^{j+1}$ followed by $V_i^j = \max(V_i^j, S_i - K)$ (early exercise). The stability condition requires $b_i \ge 0$: $\Delta t \le 1/(\sigma^2 i_{\max}^2 + r)$. For large $S_{\max}$, this becomes very restrictive.

---

**Exercise 2.**
Why is the explicit scheme rarely used for production option pricing?

??? success "Solution to Exercise 2"
    The stability condition $\Delta t = O(\Delta S^2)$ requires an enormous number of time steps for fine spatial grids. With $N_S = 200$, you might need $N_t = 100{,}000+$. Implicit or CN schemes allow $\Delta t = O(\Delta S)$ or larger, requiring far fewer steps.

---

**Exercise 3.**
For a non-dividend-paying American call, what does the explicit scheme produce compared to the European call?

??? success "Solution to Exercise 3"
    The same result: since early exercise is never optimal for a non-dividend American call, the early exercise constraint $V \ge S - K$ is never binding. The explicit scheme produces the European call price. This serves as a verification test.

---

**Exercise 4.**
How would you add discrete dividends to the explicit scheme for an American call?

??? success "Solution to Exercise 4"
    At each ex-dividend date $t_d$ with dividend amount $D$: adjust the stock price grid by replacing $S_i$ with $S_i - D$ (or $S_i(1 - q)$ for proportional dividends). This creates a discontinuity in the option value that must be handled by interpolation onto the new grid. With dividends, early exercise of the American call may become optimal just before the ex-date.
