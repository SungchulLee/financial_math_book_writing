# ============================================================================
# black_scholes_RUN_CONVERGENCE_ANALYSIS_ON_SPACE_GRID_SIZE_OF_CN_SCHEME_FOR_EUROPEAN_CALL.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

# === Parameters ===
S = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.2
q = 0
S_min = 0.1
S_max = 300    # S_max should be bigger than your S_max of interest if use log space
option_type = "call"

print(f"\n{'='*70}")
print("GRID CONVERGENCE ANALYSIS")
print("="*70)
print(f"Analyzing {option_type.upper()} option convergence")
print(f"Parameters:")
print(f"  Stock Price (S): ${S}")
print(f"  Strike Price (K): ${K}")
print(f"  Time to Maturity: {T} year")
print(f"  Risk-free Rate: {r:.1%}")
print(f"  Volatility: {sigma:.1%}")
print(f"  Price Range: ${S_min} - ${S_max}")

# Create Black-Scholes model
bs_model = bs.BlackScholes(S, K, T, r, sigma, q)

# Get analytical benchmark
if option_type == "call":
    analytical_price, _ = bs_model.price_analytical()
else:
    _, analytical_price = bs_model.price_analytical()

print(f"  Analytical Price: ${analytical_price:.6f}")

print(f"\nRunning convergence analysis...")

errors = []
grid_sizes = []
num_points = []

for M in range(15, 100, 5):  # Grid points
    print(f"  Testing grid size: {M+1} points...")
    
    # Run Crank-Nicolson method
    S_cn, V_cn = bs_model.price_numerical(
        method="cn", 
        option_type=option_type, 
        Smin=S_min, 
        Smax=S_max, 
        NS=M+1
    )
    
    # Get analytical prices at grid points
    if option_type == "call":
        V_exact = bs.bs_call_price(S_cn, K, T, r, sigma, q)
    else:
        V_exact = bs.bs_put_price(S_cn, K, T, r, sigma, q)
    
    # Calculate maximum error
    max_error = np.max(np.abs(V_cn - V_exact))
    errors.append(max_error)
    grid_sizes.append(1 / M)  # Grid spacing
    num_points.append(M + 1)

# Convert to numpy arrays for analysis
errors = np.array(errors)
grid_sizes = np.array(grid_sizes)
num_points = np.array(num_points)

print(f"Convergence analysis completed!")

# === Enhanced Plotting ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Log-log convergence plot
ax1.loglog(grid_sizes, errors, 'bo-', linewidth=2, markersize=6, label='CN FDM Errors')

# Fit theoretical convergence lines
log_h = np.log(grid_sizes)
log_err = np.log(errors)

# Fit linear regression to estimate convergence order
coeffs = np.polyfit(log_h, log_err, 1)
convergence_order = coeffs[0]

# Plot theoretical convergence lines
h_theory = np.logspace(np.log10(grid_sizes.min()), np.log10(grid_sizes.max()), 100)
C1 = errors[-1] / (grid_sizes[-1]**1)  # Adjust constant
C2 = errors[-1] / (grid_sizes[-1]**2)  # Adjust constant

ax1.loglog(h_theory, C1 * h_theory**1, 'r--', alpha=0.7, label='O(h) - First Order')
ax1.loglog(h_theory, C2 * h_theory**2, 'g--', alpha=0.7, label='O(h²) - Second Order')

ax1.set_xlabel('Grid Spacing (h)', fontsize=12)
ax1.set_ylabel('Max Absolute Error', fontsize=12)
ax1.set_title(f'Grid Convergence: {option_type.capitalize()} Option\n' +
             f'Estimated Convergence Order: {convergence_order:.2f}', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot 2: Semi-log plot (as in original)
ax2.plot(np.log(grid_sizes), errors, 'bo-', linewidth=2, markersize=6, label='CN FDM Errors')
ax2.set_xlabel('log(Grid Spacing)', fontsize=12)
ax2.set_ylabel('Max Absolute Error', fontsize=12)
ax2.set_title(f'Semi-log Convergence Plot\n{option_type.capitalize()} Option', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()

# === Detailed Analysis ===
print(f"\n{'='*70}")
print("CONVERGENCE ANALYSIS RESULTS")
print("="*70)

print(f"Grid Convergence Summary:")
print(f"{'Grid Points':<12} {'Grid Spacing':<15} {'Max Error':<15} {'Error Reduction':<15}")
print("-" * 65)

for i, (n_pts, h, err) in enumerate(zip(num_points, grid_sizes, errors)):
    if i == 0:
        reduction = "—"
    else:
        reduction = f"{errors[i-1]/err:.2f}x"
    
    print(f"{n_pts:<12} {h:<15.6f} {err:<15.2e} {reduction:<15}")

# Convergence order analysis
print(f"\nConvergence Order Analysis:")
print(f"  Estimated Order: {convergence_order:.3f}")

if abs(convergence_order + 2) < 0.3:
    print(f"  ✅ Excellent! Close to theoretical O(h²) for CN method")
elif abs(convergence_order + 1.5) < 0.5:
    print(f"  ✅ Good! Between first and second order convergence")
elif abs(convergence_order + 1) < 0.3:
    print(f"  ⚠️  First order convergence - check implementation")
else:
    print(f"  ⚠️  Unusual convergence pattern - investigate further")

# Error reduction analysis
error_reductions = [errors[i]/errors[i+1] for i in range(len(errors)-1)]
avg_reduction = np.mean(error_reductions)

print(f"\nError Reduction Analysis:")
print(f"  Average error reduction per refinement: {avg_reduction:.2f}x")
print(f"  Theoretical expectation for O(h²): ~4x")

if avg_reduction > 3.5:
    print(f"  ✅ Excellent convergence behavior")
elif avg_reduction > 2.5:
    print(f"  ✅ Good convergence behavior")
else:
    print(f"  ⚠️  Slower than expected convergence")

# Practical recommendations
print(f"\nPractical Recommendations:")
best_efficiency_idx = np.argmax(1/errors / num_points)  # Error per computational cost
best_grid = num_points[best_efficiency_idx]

print(f"  Most efficient grid size: {best_grid} points")
print(f"  Error at this size: {errors[best_efficiency_idx]:.2e}")

# Find grid size for specific accuracy targets
target_errors = [1e-3, 1e-4, 1e-5]
for target in target_errors:
    if errors.min() <= target:
        idx = np.where(errors <= target)[0][0]
        required_points = num_points[idx]
        print(f"  For {target:.0e} accuracy: {required_points} points minimum")

# Method characteristics
print(f"\nCrank-Nicolson Method Characteristics:")
print(f"  ✓ Unconditionally stable")
print(f"  ✓ Second-order accurate in time and space (theoretical)")
print(f"  ✓ Good for smooth solutions like European options")
print(f"  ⚠ Requires solving linear systems")

# Comparison insight
if option_type == "call":
    print(f"\nCall Option Specific Notes:")
    print(f"  • Smooth payoff function aids convergence")
    print(f"  • No boundary singularities")
    print(f"  • Uniform grid typically adequate")
else:
    print(f"\nPut Option Specific Notes:")
    print(f"  • Steeper gradients near S=0 may affect convergence")
    print(f"  • Consider log-space methods for better accuracy")
    print(f"  • Boundary condition at S=0 more challenging")

print(f"\nComputational Efficiency:")
finest_grid = num_points[-1]
coarsest_grid = num_points[0]
comp_ratio = (finest_grid)**2 / (coarsest_grid)**2  # Roughly proportional to computational cost

print(f"  Computational cost ratio (finest/coarsest): ~{comp_ratio:.1f}x")
print(f"  Error improvement ratio: {errors[0]/errors[-1]:.1f}x")
print(f"  Efficiency gain: {(errors[0]/errors[-1])/comp_ratio:.2f}x error reduction per unit cost")

print("="*70)