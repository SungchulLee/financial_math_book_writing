# ============================================================================
# black_scholes_RUN_IMPLICIT_SCHEME_FOR_AMERICAN_PUT.py
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
    NS=M+1, 
    early_exercise=True
)

# === Run Implicit FDM in Log-Price Space ===
print(f"  Running Implicit FDM (Log-Price Space)...")
S_log, V_log = bs_model.price_numerical(
    method="implicit_log", 
    option_type=option_type, 
    Smin=S_min_log, 
    Smax=S_max, 
    NX=M+1, 
    early_exercise=True
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
ax.plot(S_all, V_exact_all, 'r--', label='European Analytical (BS)', linewidth=2)

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
ax.set_title(f'American {option_type.capitalize()} Option: Implicit FDM Analysis\n' +
            f'Original vs Log-Space vs European Benchmark', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)

# Clean appearance
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# === Error Analysis (American vs European) ===
print(f"\nAmerican vs European Analysis:")

# Get European prices at grid points
if option_type == "call":
    V_exact_orig = bs.bs_call_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
    V_exact_log = bs.bs_call_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)
else:
    V_exact_orig = bs.bs_put_price(np.maximum(S_orig, 1e-10), K, T, r, sigma, q)
    V_exact_log = bs.bs_put_price(np.maximum(S_log, 1e-10), K, T, r, sigma, q)

# Calculate early exercise premiums
premium_orig = V_orig - V_exact_orig
premium_log = V_log - V_exact_log

# Error analysis
error_orig = np.max(np.abs(V_orig - V_exact_orig))
error_log = np.max(np.abs(V_log - V_exact_log))

print(f"  Early Exercise Premium Analysis:")
print(f"    Original Space:")
print(f"      Max Premium: ${np.max(premium_orig):.6f}")
print(f"      Mean Premium: ${np.mean(premium_orig):.6f}")
print(f"      Max Error vs European: ${error_orig:.6f}")

print(f"    Log Space:")
print(f"      Max Premium: ${np.max(premium_log):.6f}")
print(f"      Mean Premium: ${np.mean(premium_log):.6f}")
print(f"      Max Error vs European: ${error_log:.6f}")

# Method comparison
method_diff = np.max(np.abs(V_orig - np.interp(S_orig, S_log, V_log)))
print(f"\n  Method Agreement:")
print(f"    Max difference between methods: ${method_diff:.6f}")

if method_diff < 0.001:
    print(f"    ✅ Excellent agreement between implicit methods")
elif method_diff < 0.01:
    print(f"    ✅ Good agreement between implicit methods") 
else:
    print(f"    ⚠️  Consider higher grid resolution")

# === Detailed Price Analysis ===
print(f"\nPrice Analysis at Key Points:")
print(f"{'Stock':<8} {'European':<10} {'Amer Orig':<11} {'Amer Log':<11} {'Premium':<10}")
print("-" * 60)

key_prices = [60, 80, 100, 120, 150] if option_type == "call" else [40, 60, 80, 100, 120]

for S_test in key_prices:
    # European benchmark
    if option_type == "call":
        euro_price = bs.bs_call_price(S_test, K, T, r, sigma, q)
    else:
        euro_price = bs.bs_put_price(S_test, K, T, r, sigma, q)
    
    # American prices
    idx_orig = np.argmin(np.abs(S_orig - S_test))
    idx_log = np.argmin(np.abs(S_log - S_test))
    
    amer_orig = V_orig[idx_orig]
    amer_log = V_log[idx_log]
    avg_premium = (amer_orig + amer_log) / 2 - euro_price
    
    print(f"${S_test:<7.0f} ${euro_price:<9.4f} ${amer_orig:<10.4f} "
          f"${amer_log:<10.4f} ${avg_premium:<9.5f}")

# === Current Stock Price Analysis ===
print(f"\nAt Current Stock Price (S = ${S0}):")

# Analytical benchmark
analytical_call, analytical_put = bs_model.price_analytical()
european_current = analytical_call if option_type == "call" else analytical_put

# American prices
idx_orig_s0 = np.argmin(np.abs(S_orig - S0))
idx_log_s0 = np.argmin(np.abs(S_log - S0))
american_orig_s0 = V_orig[idx_orig_s0]
american_log_s0 = V_log[idx_log_s0]

print(f"  European Price:    ${european_current:.6f}")
print(f"  American (Orig):   ${american_orig_s0:.6f}")
print(f"  American (Log):    ${american_log_s0:.6f}")
print(f"  Early Ex Premium:  ${american_orig_s0 - european_current:.6f}")

# === Summary ===
print(f"\n{'='*70}")
print("SUMMARY")
print("="*70)

print(f"✅ Implicit Method Results:")
print(f"   • Original Space Max Premium: ${np.max(premium_orig):.6f}")
print(f"   • Log Space Max Premium:      ${np.max(premium_log):.6f}")
print(f"   • Method Agreement:           ${method_diff:.6f}")

if option_type == "call" and q == 0:
    print(f"\n💡 Call Option Insights:")
    print(f"   • No dividends: Early exercise premium is minimal")
    print(f"   • American ≈ European for most practical purposes")
    print(f"   • Premium appears mainly for deep ITM options")
else:
    print(f"\n💡 Put Option Insights:")
    print(f"   • Significant early exercise value for ITM puts")
    print(f"   • Premium increases as stock price decreases")
    print(f"   • Log-space critical for S→0 boundary handling")
    print(f"   • Maximum put value at S=0: K*e^(-rT) = ${K * np.exp(-r * T):.4f}")

print(f"\n🎯 Computational Notes:")
print(f"   • Implicit methods: Unconditionally stable")
print(f"   • Can use larger time steps than explicit methods")
print(f"   • Linear system solved at each time step")
print(f"   • Early exercise via projection constraint")

print(f"\n⚡ Method Recommendations:")
if np.max(premium_log) > np.max(premium_orig):
    print(f"   • Log-space shows higher premiums (more accurate)")
    print(f"   • Prefer log-space for wide price ranges")
else:
    print(f"   • Both methods show similar premiums")
    print(f"   • Original space adequate for moderate ranges")

print(f"   • Grid resolution affects early exercise accuracy")
print(f"   • Consider adaptive mesh refinement")

print("="*70)