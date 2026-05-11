# European Put

## Background

Black Scholes Explicit Euro Put

Educational script demonstrating black scholes explicit euro put concepts.

---

## What This Code Demonstrates

- Parameters ===

---

## Code

```python
"""
Black Scholes Explicit Euro Put

Educational script demonstrating black scholes explicit euro put concepts.
"""

# ============================================================================
# black_scholes_RUN_EXPLICIT_SCHEME_FOR_EUROPEAN_PUT.py
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
    option_type = "put"

    print(f"\n{'='*70}")
    print("EXPLICIT FINITE DIFFERENCE METHODS COMPARISON")
    print("="*70)
    print(f"Parameters:")
    print(f"  Option Type: {option_type.upper()}")
    print(f"  Stock Price (S0): ${S0}")
    print(f"  Strike Price (K): ${K}")
    print(f"  Time to Maturity: {T} year")
    print(f"  Risk-free Rate: {r:.1%}")
    print(f"  Volatility: {sigma:.1%}")
    print(f"  Grid Points: {M+1}")
    print(f"  Price Range: ${S_min} - ${S_max}")

    # === Instantiate Black-Scholes model using wrapper ===
    bs_model = bs.BlackScholes(S0, K, T, r, sigma, q)

    print(f"\nRunning calculations...")

    # === Run Explicit FDM in Original Space ===
    print(f"  Computing Explicit FDM (Original Space)...")
    S_orig, V_orig = bs_model.price_numerical(
        method="explicit", 
        option_type=option_type, 
        Smin=S_min, 
        Smax=S_max, 
        NS=M+1
    )

    # === Run Explicit FDM in Log-Price Space ===
    print(f"  Computing Explicit FDM (Log-Price Space)...")
    S_log, V_log = bs_model.price_numerical(
        method="explicit_log", 
        option_type=option_type, 
        Smin=S_min_log, 
        Smax=S_max, 
        NX=M+1
    )

    # === Analytical Black-Scholes Price (Vectorized) ===
    print(f"  Computing Analytical Black-Scholes prices...")
    S_all = np.union1d(S_orig, S_log)
    S_all.sort()
    S_all_safe = np.maximum(S_all, 1e-10)  # Avoid log(0)

    # Use vectorized utility functions
    if option_type == "call":
        V_exact_all = bs.bs_call_price(S_all_safe, K, T, r, sigma, q)
    else:
        V_exact_all = bs.bs_put_price(S_all_safe, K, T, r, sigma, q)

    # === Enhanced Plot Comparison ===
    print(f"  Generating comparison plot...")
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot numerical solutions
    ax.plot(S_orig, V_orig, label='Explicit FDM (Original Space)', 
            linewidth=8, alpha=0.3, color='blue')
    ax.plot(S_log, V_log, label='Explicit FDM (Log Space)', 
            linewidth=4, alpha=0.8, color='green')

    # Plot analytical solution
    ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', linewidth=2)

    # Add reference lines
    ax.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax.axvline(x=S0, color='orange', linestyle=':', alpha=0.7, label=f'Current = ${S0}')

    # Plot intrinsic value
    if option_type == "call":
        intrinsic = np.maximum(S_all - K, 0)
        ax.plot(S_all, intrinsic, 'k:', alpha=0.5, label='Intrinsic Value')
    else:
        intrinsic = np.maximum(K - S_all, 0)
        ax.plot(S_all, intrinsic, 'k:', alpha=0.5, label='Intrinsic Value')

    # Formatting
    ax.set_xlabel('Stock Price ($)', fontsize=12)
    ax.set_ylabel('Option Value ($)', fontsize=12)
    ax.set_title(f'European {option_type.capitalize()} Option: Explicit FDM Methods Comparison', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    # Clean appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

    # === Detailed Error Analysis ===
    print(f"\nDetailed Error Analysis:")

    # Compute exact values at each grid
    if option_type == "call":
        V_exact_orig = bs.bs_call_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
        V_exact_log = bs.bs_call_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)
    else:
        V_exact_orig = bs.bs_put_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
        V_exact_log = bs.bs_put_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)

    # Calculate errors
    error_orig = np.max(np.abs(V_orig - V_exact_orig))
    error_log = np.max(np.abs(V_log - V_exact_log))

    # Mean absolute errors
    mae_orig = np.mean(np.abs(V_orig - V_exact_orig))
    mae_log = np.mean(np.abs(V_log - V_exact_log))

    # Relative errors
    rel_error_orig = error_orig / np.mean(V_exact_orig) * 100
    rel_error_log = error_log / np.mean(V_exact_log) * 100

    print(f"  Original Space Method:")
    print(f"    Max Absolute Error:  ${error_orig:.6f}")
    print(f"    Mean Absolute Error: ${mae_orig:.6f}")
    print(f"    Max Relative Error:  {rel_error_orig:.4f}%")

    print(f"  Log-Space Method:")
    print(f"    Max Absolute Error:  ${error_log:.6f}")
    print(f"    Mean Absolute Error: ${mae_log:.6f}")
    print(f"    Max Relative Error:  {rel_error_log:.4f}%")

    # Determine better method
    if error_log < error_orig:
        better_method = "Log-Space"
        improvement = error_orig / error_log
        print(f"  🏆 Winner: {better_method} method (factor of {improvement:.2f} more accurate)")
    else:
        better_method = "Original Space"
        improvement = error_log / error_orig
        print(f"  🏆 Winner: {better_method} method (factor of {improvement:.2f} more accurate)")

    # === Price Comparison at Key Points ===
    print(f"\nPrice Comparison at Key Stock Prices:")
    print(f"{'Stock Price':<12} {'Analytical':<12} {'Original':<12} {'Log-Space':<12} {'Orig Error':<12} {'Log Error':<12}")
    print("-" * 84)

    # Key price points to examine
    key_prices = [50, 80, 100, 120, 150]

    for S_test in key_prices:
        # Analytical price
        if option_type == "call":
            exact_price = bs.bs_call_price(S_test, K, T, r, sigma, q)
        else:
            exact_price = bs.bs_put_price(S_test, K, T, r, sigma, q)
    
        # Find closest points in grids
        idx_orig = np.argmin(np.abs(S_orig - S_test))
        idx_log = np.argmin(np.abs(S_log - S_test))
    
        price_orig = V_orig[idx_orig]
        price_log = V_log[idx_log]
    
        error_orig_pt = abs(price_orig - exact_price)
        error_log_pt = abs(price_log - exact_price)
    
        print(f"${S_test:<11.0f} ${exact_price:<11.4f} ${price_orig:<11.4f} ${price_log:<11.4f} "
              f"${error_orig_pt:<11.5f} ${error_log_pt:<11.5f}")

    # === Grid Analysis ===
    print(f"\nGrid Analysis:")
    print(f"  Original Space Grid:")
    print(f"    Stock price range: ${S_orig[0]:.2f} - ${S_orig[-1]:.2f}")
    print(f"    Grid spacing (dS): ${(S_orig[1] - S_orig[0]):.3f}")
    print(f"    Number of points: {len(S_orig)}")

    print(f"  Log-Space Grid:")
    print(f"    Stock price range: ${S_log[0]:.3f} - ${S_log[-1]:.2f}")
    print(f"    Grid spacing varies (finer near S=0)")
    print(f"    Number of points: {len(S_log)}")

    # === Method Characteristics ===
    print(f"\nMethod Characteristics:")
    print(f"  Explicit Original Space:")
    print(f"    ✓ Intuitive setup with uniform grid")
    print(f"    ✓ Easy boundary condition implementation")
    print(f"    ⚠ May struggle with extreme stock prices")
    print(f"    ⚠ Uniform grid may be inefficient")

    print(f"  Explicit Log-Space:")
    print(f"    ✓ Better handling of S→0 behavior")
    print(f"    ✓ Natural grid refinement near important regions")
    print(f"    ✓ More stable for wide price ranges")
    print(f"    ⚠ Less intuitive coordinate transformation")

    # === Computational Summary ===
    print(f"\n{'='*70}")
    print("COMPUTATIONAL SUMMARY")
    print("="*70)
    print(f"📊 Error Comparison:")
    print(f"   Original Space: ${error_orig:.6f} max error")
    print(f"   Log-Space:      ${error_log:.6f} max error")

    print(f"\n🎯 Recommendations:")
    if error_log < error_orig:
        print(f"   • Use log-space method for better accuracy")
        print(f"   • Particularly beneficial for wide price ranges")
        print(f"   • Better handling of boundary conditions")
    else:
        print(f"   • Original space method performs adequately")
        print(f"   • May be preferred for intuitive interpretation")

    print(f"\n⚡ Performance Notes:")
    print(f"   • Both methods use explicit time stepping")
    print(f"   • Stability depends on CFL condition")
    print(f"   • Consider implicit methods for larger time steps")

    # === Analytical Benchmark ===
    analytical_call, analytical_put = bs_model.price_analytical()
    analytical_price = analytical_call if option_type == "call" else analytical_put

    print(f"\n📈 At Current Stock Price (S = ${S0}):")
    print(f"   Analytical Price: ${analytical_price:.6f}")

    # Find prices at S0
    idx_orig_s0 = np.argmin(np.abs(S_orig - S0))
    idx_log_s0 = np.argmin(np.abs(S_log - S0))
    price_orig_s0 = V_orig[idx_orig_s0]
    price_log_s0 = V_log[idx_log_s0]

    print(f"   Original Space:   ${price_orig_s0:.6f} (error: ${abs(price_orig_s0 - analytical_price):.6f})")
    print(f"   Log-Space:        ${price_log_s0:.6f} (error: ${abs(price_log_s0 - analytical_price):.6f})")

    print("="*70)
```


## Exercises

**Exercise 1.**
State the boundary conditions for the European put at $S = 0$ and $S = S_{\max}$ in the explicit FDM. Explain why the $S = 0$ boundary is critical for put pricing.

??? success "Solution to Exercise 1"
    At $S = 0$: $V(0, t) = K e^{-r(T-t)}$, since the put is certain to pay $K$ at maturity. At $S = S_{\max}$: $V(S_{\max}, t) = 0$, since the put is deeply out of the money. The $S = 0$ boundary is critical because the put value reaches its maximum there ($K e^{-rT} \approx \$95.12$), and the option dynamics change rapidly in this region. Discretization errors at this boundary propagate throughout the solution.

---

**Exercise 2.**
Verify put-call parity numerically: for $C = 10.4506$, $P = 5.5735$, $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, check that $C - P = S_0 - K e^{-rT}$.

??? success "Solution to Exercise 2"
    $$
    C - P = 10.4506 - 5.5735 = 4.8771
    $$

    $$
    S_0 - K e^{-rT} = 100 - 100 e^{-0.05} = 100 - 95.1229 = 4.8771
    $$

    Put-call parity holds exactly. This serves as a consistency check: if the same FDM is applied to both call and put with identical parameters, the parity relation should be satisfied to numerical precision.

---

**Exercise 3.**
Explain why the kink in the put payoff $\max(K - S, 0)$ at $S = K$ causes difficulties for finite difference methods.

??? success "Solution to Exercise 3"
    The payoff has a discontinuous first derivative at $S = K$ (slope jumps from $-1$ to $0$). Finite difference approximations assume smoothness; the kink introduces $O(1)$ errors in first-derivative approximations at $S = K$. These errors generate spurious oscillations propagating backward in time. Remedies include placing a grid point exactly at $K$, using non-uniform grids near $K$, or applying payoff smoothing.

---

**Exercise 4.**
If the explicit FDM in original space has max error $\$0.4821$ and the log-space method has max error $\$0.0932$ (both with $M = 100$), compute the improvement factor and explain where the log-space advantage is most pronounced.

??? success "Solution to Exercise 4"
    The improvement factor is $0.4821 / 0.0932 \approx 5.17$. The advantage is most pronounced near $S = 0$, where the put value approaches $K e^{-rT}$ and changes rapidly. In original space, the uniform grid provides only a few points in the critical $S \in [0, 20]$ region. The log-space grid concentrates many more points near small $S$ values, dramatically reducing boundary-related errors for puts.