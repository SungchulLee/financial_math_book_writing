# ============================================================================
# black_scholes_RUN_EXPLICIT_SCHEME_FOR_EUROPEAN_PUT.py
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