# ============================================================================
# black_scholes_RUN_IMPLICIT_SCHEME_FOR_EUROPEAN_PUT.py
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
print("IMPLICIT FINITE DIFFERENCE ANALYSIS")
print("="*70)
print(f"American {option_type.upper()} Option Analysis")
print(f"Stock Price (S0): ${S0}")
print(f"Strike Price (K): ${K}")
print(f"Time to Maturity: {T} year")
print(f"Risk-free Rate: {r:.1%}")
print(f"Volatility: {sigma:.1%}")
print(f"Grid Points: {M+1}")
print(f"Price Range: ${S_min} - ${S_max}")

# === Instantiate Black-Scholes model using wrapper ===
bs_model = bs.BlackScholes(S0, K, T, r, sigma, q)

print(f"\nCalculating option prices...")

# === Run Implicit FDM in Original Space ===
print(f"  Running Implicit FDM (Original Space)...")
S_orig, V_orig = bs_model.price_numerical(
    method="implicit", 
    option_type=option_type, 
    Smin=S_min, 
    Smax=S_max, 
    NS=M+1
)

# === Run Implicit FDM in Log-Price Space ===
print(f"  Running Implicit FDM (Log-Price Space)...")
S_log, V_log = bs_model.price_numerical(
    method="implicit_log", 
    option_type=option_type, 
    Smin=S_min_log, 
    Smax=S_max, 
    NX=M+1
)

# === Analytical Black-Scholes Price (Vectorized) ===
print(f"  Computing analytical benchmark...")
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

# Plot the numerical solutions
ax.plot(S_orig, V_orig, label='Implicit FDM (Original Space)', 
        linewidth=8, alpha=0.3, color='blue')
ax.plot(S_log, V_log, label='Implicit FDM (Log Space)', 
        linewidth=4, alpha=0.8, color='green')

# Plot analytical European solution for reference
ax.plot(S_all, V_exact_all, 'r--', label='Analytical (Black-Scholes)', linewidth=2)

# Add reference lines
ax.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
ax.axvline(x=S0, color='orange', linestyle=':', alpha=0.7, label=f'Current = ${S0}')

# Plot intrinsic value
if option_type == "call":
    intrinsic = np.maximum(S_all - K, 0)
else:
    intrinsic = np.maximum(K - S_all, 0)
ax.plot(S_all, intrinsic, 'k:', alpha=0.5, linewidth=2, label='Intrinsic Value')

# Formatting
ax.set_xlabel('Stock Price ($)', fontsize=12)
ax.set_ylabel('Option Value ($)', fontsize=12)
ax.set_title(f'European {option_type.capitalize()} Option: Implicit FDM Analysis\n' +
            f'Original vs Log-Space vs Analytical Benchmark', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)

# Clean appearance
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# === Error Analysis (Numerical vs Analytical) ===
print(f"\nNumerical vs Analytical Comparison:")

# Get analytical prices at grid points
if option_type == "call":
    V_exact_orig = bs.bs_call_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
    V_exact_log = bs.bs_call_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)
else:
    V_exact_orig = bs.bs_put_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
    V_exact_log = bs.bs_put_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)

# Calculate numerical errors
error_orig = np.abs(V_orig - V_exact_orig)
error_log = np.abs(V_log - V_exact_log)

# Error analysis
max_error_orig = np.max(error_orig)
max_error_log = np.max(error_log)
mean_error_orig = np.mean(error_orig)
mean_error_log = np.mean(error_log)

print(f"  Original Space Method:")
print(f"    Max Absolute Error:  ${max_error_orig:.6f}")
print(f"    Mean Absolute Error: ${mean_error_orig:.6f}")
print(f"    Max Relative Error:  {max_error_orig / np.mean(V_exact_orig) * 100:.4f}%")

print(f"  Log Space Method:")
print(f"    Max Absolute Error:  ${max_error_log:.6f}")
print(f"    Mean Absolute Error: ${mean_error_log:.6f}")
print(f"    Max Relative Error:  {max_error_log / np.mean(V_exact_log) * 100:.4f}%")

# Method comparison
method_diff = np.max(np.abs(V_orig - np.interp(S_orig, S_log, V_log)))
print(f"\n  Method Agreement:")
print(f"    Max difference between methods: ${method_diff:.6f}")

if method_diff < 0.0001:
    print(f"    ✅ Excellent agreement between implicit methods")
elif method_diff < 0.001:
    print(f"    ✅ Very good agreement between implicit methods")
elif method_diff < 0.01:
    print(f"    ✅ Good agreement between implicit methods") 
else:
    print(f"    ⚠️  Consider higher grid resolution")

# Accuracy comparison
if max_error_log < max_error_orig:
    improvement = max_error_orig / max_error_log
    print(f"    🏆 Log-space is more accurate by factor of {improvement:.2f}")
else:
    improvement = max_error_log / max_error_orig
    print(f"    🏆 Original-space is more accurate by factor of {improvement:.2f}")

# === Detailed Price Analysis ===
print(f"\nPrice Analysis at Key Points:")
print(f"{'Stock':<8} {'Analytical':<11} {'Orig FDM':<11} {'Log FDM':<11} {'Orig Error':<12} {'Log Error':<12}")
print("-" * 78)

key_prices = [60, 80, 100, 120, 150] if option_type == "call" else [40, 60, 80, 100, 120]

for S_test in key_prices:
    # Analytical benchmark
    if option_type == "call":
        exact_price = bs.bs_call_price(S_test, K, T, r, sigma, q)
    else:
        exact_price = bs.bs_put_price(S_test, K, T, r, sigma, q)
    
    # Numerical prices
    idx_orig = np.argmin(np.abs(S_orig - S_test))
    idx_log = np.argmin(np.abs(S_log - S_test))
    
    num_orig = V_orig[idx_orig]
    num_log = V_log[idx_log]
    
    err_orig = abs(num_orig - exact_price)
    err_log = abs(num_log - exact_price)
    
    print(f"${S_test:<7.0f} ${exact_price:<10.4f} ${num_orig:<10.4f} "
          f"${num_log:<10.4f} ${err_orig:<11.6f} ${err_log:<11.6f}")

# === Current Stock Price Analysis ===
print(f"\nAt Current Stock Price (S = ${S0}):")

# Analytical benchmark
analytical_call, analytical_put = bs_model.price_analytical()
analytical_current = analytical_call if option_type == "call" else analytical_put

# Numerical prices
idx_orig_s0 = np.argmin(np.abs(S_orig - S0))
idx_log_s0 = np.argmin(np.abs(S_log - S0))
numerical_orig_s0 = V_orig[idx_orig_s0]
numerical_log_s0 = V_log[idx_log_s0]

print(f"  Analytical Price:      ${analytical_current:.6f}")
print(f"  Numerical (Orig):      ${numerical_orig_s0:.6f}")
print(f"  Numerical (Log):       ${numerical_log_s0:.6f}")
print(f"  Original Error:        ${abs(numerical_orig_s0 - analytical_current):.6f}")
print(f"  Log-Space Error:       ${abs(numerical_log_s0 - analytical_current):.6f}")

# === Summary ===
print(f"\n{'='*70}")
print("SUMMARY")
print("="*70)

print(f"✅ Implicit Method Results:")
print(f"   • Original Space Max Error: ${max_error_orig:.6f}")
print(f"   • Log Space Max Error:      ${max_error_log:.6f}")
print(f"   • Method Agreement:         ${method_diff:.6f}")

if option_type == "call":
    print(f"\n💡 European Call Option Insights:")
    print(f"   • No early exercise: Pure numerical accuracy test")
    print(f"   • Should match analytical Black-Scholes closely")
    print(f"   • Errors indicate grid resolution effects")
    print(f"   • Both methods should perform similarly")
else:
    print(f"\n💡 European Put Option Insights:")
    print(f"   • No early exercise: Pure numerical accuracy test") 
    print(f"   • Log-space advantage near S→0 boundary")
    print(f"   • Higher gradients than calls require finer grids")
    print(f"   • Put value approaches K*e^(-rT) as S→0")

print(f"\n🎯 Computational Notes:")
print(f"   • Implicit methods: Unconditionally stable")
print(f"   • Can use larger time steps than explicit methods")
print(f"   • Linear system solved at each time step")
print(f"   • Early exercise via projection constraint")

print(f"\n⚡ Method Recommendations:")
if max_error_log < max_error_orig:
    print(f"   • Log-space method more accurate")
    print(f"   • Particularly beneficial for wide price ranges")
    print(f"   • Better boundary condition handling")
    if option_type == "put":
        print(f"   • Essential for puts due to S→0 behavior")
else:
    print(f"   • Original space method performs well")
    print(f"   • Both methods give similar accuracy")

print(f"   • European options: Pure numerical accuracy test")
print(f"   • Grid resolution directly affects accuracy")
print(f"   • Implicit methods: Unconditionally stable")

print("="*70)

