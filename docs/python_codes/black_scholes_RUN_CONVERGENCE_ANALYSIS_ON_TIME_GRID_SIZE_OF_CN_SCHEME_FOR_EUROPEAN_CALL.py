# ============================================================================
# black_scholes_RUN_CONVERGENCE_ANALYSIS_ON_TIME_GRID_SIZE_OF_CN_SCHEME_FOR_EUROPEAN_CALL.py
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
print("TEMPORAL CONVERGENCE ANALYSIS")
print("="*70)
print(f"Analyzing {option_type.upper()} option temporal convergence")
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

print(f"\nRunning temporal convergence analysis...")
print(f"Testing time step refinement (NT = number of time steps)")

errors = []
time_steps = []
dt_values = []

for M in range(100, 150, 10):  # Time steps
    NT = M + 1
    dt = T / M  # Time step size
    print(f"  Testing time steps: {NT} (dt = {dt:.6f})...")
    
    # Run Crank-Nicolson method with fixed spatial grid but varying time steps
    S_cn, V_cn = bs_model.price_numerical(
        method="cn", 
        option_type=option_type, 
        Smin=S_min, 
        Smax=S_max, 
        NT=NT,
        NS=101  # Fixed spatial grid
    )
    
    # Get analytical prices at grid points
    if option_type == "call":
        V_exact = bs.bs_call_price(S_cn, K, T, r, sigma, q)
    else:
        V_exact = bs.bs_put_price(S_cn, K, T, r, sigma, q)
    
    # Calculate maximum error
    max_error = np.max(np.abs(V_cn - V_exact))
    errors.append(max_error)
    time_steps.append(1 / M)  # Time step size (dt)
    dt_values.append(dt)

# Convert to numpy arrays for analysis
errors = np.array(errors)
time_steps = np.array(time_steps)
dt_values = np.array(dt_values)

print(f"Convergence analysis completed!")

# === Enhanced Plotting ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Log-log convergence plot
ax1.loglog(time_steps, errors, 'bo-', linewidth=2, markersize=6, label='CN FDM Errors')

# Fit theoretical convergence lines
log_dt = np.log(time_steps)
log_err = np.log(errors)

# Fit linear regression to estimate convergence order
coeffs = np.polyfit(log_dt, log_err, 1)
convergence_order = coeffs[0]

# Plot theoretical convergence lines
dt_theory = np.logspace(np.log10(time_steps.min()), np.log10(time_steps.max()), 100)
C1 = errors[-1] / (time_steps[-1]**1)  # Adjust constant
C2 = errors[-1] / (time_steps[-1]**2)  # Adjust constant

ax1.loglog(dt_theory, C1 * dt_theory**1, 'r--', alpha=0.7, label='O(dt) - First Order')
ax1.loglog(dt_theory, C2 * dt_theory**2, 'g--', alpha=0.7, label='O(dt²) - Second Order')

ax1.set_xlabel('Time Step Size (dt)', fontsize=12)
ax1.set_ylabel('Max Absolute Error', fontsize=12)
ax1.set_title(f'Temporal Convergence: {option_type.capitalize()} Option\n' +
             f'Estimated Convergence Order: {convergence_order:.2f}', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot 2: Semi-log plot (as in original)
ax2.plot(np.log(time_steps), errors, 'bo-', linewidth=2, markersize=6, label='CN FDM Errors')
ax2.set_xlabel('log(Time Step Size)', fontsize=12)
ax2.set_ylabel('Max Absolute Error', fontsize=12)
ax2.set_title(f'Semi-log Temporal Convergence\n{option_type.capitalize()} Option', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()

# === Detailed Analysis ===
print(f"\n{'='*70}")
print("TEMPORAL CONVERGENCE ANALYSIS RESULTS")
print("="*70)

print(f"Time Step Convergence Summary:")
print(f"{'Time Steps':<12} {'dt':<15} {'Max Error':<15} {'Error Reduction':<15}")
print("-" * 65)

for i, (nt, dt, err) in enumerate(zip(range(101, 151, 10), dt_values, errors)):
    if i == 0:
        reduction = "—"
    else:
        reduction = f"{errors[i-1]/err:.2f}x"
    
    print(f"{nt:<12} {dt:<15.6f} {err:<15.2e} {reduction:<15}")

# Convergence order analysis
print(f"\nTemporal Convergence Order Analysis:")
print(f"  Estimated Order: {convergence_order:.3f}")

if abs(convergence_order + 2) < 0.3:
    print(f"  ✅ Excellent! Close to theoretical O(dt²) for CN method")
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
print(f"  Theoretical expectation for O(dt²): ~4x")

if avg_reduction > 3.5:
    print(f"  ✅ Excellent temporal convergence behavior")
elif avg_reduction > 2.5:
    print(f"  ✅ Good temporal convergence behavior")
else:
    print(f"  ⚠️  Slower than expected temporal convergence")

# Practical recommendations
print(f"\nPractical Time Step Recommendations:")
time_step_counts = range(101, 151, 10)
best_efficiency_idx = np.argmax(1/errors / np.array(list(time_step_counts)))  # Error per computational cost
best_time_steps = list(time_step_counts)[best_efficiency_idx]

print(f"  Most efficient time steps: {best_time_steps}")
print(f"  Error at this size: {errors[best_efficiency_idx]:.2e}")
print(f"  Time step size (dt): {dt_values[best_efficiency_idx]:.6f}")

# Find time steps for specific accuracy targets
target_errors = [1e-3, 1e-4, 1e-5]
for target in target_errors:
    if errors.min() <= target:
        idx = np.where(errors <= target)[0][0]
        required_steps = list(time_step_counts)[idx]
        required_dt = dt_values[idx]
        print(f"  For {target:.0e} accuracy: {required_steps} time steps (dt = {required_dt:.6f})")

# Method characteristics
print(f"\nCrank-Nicolson Temporal Characteristics:")
print(f"  ✓ Unconditionally stable in time")
print(f"  ✓ Second-order accurate in time (theoretical)")
print(f"  ✓ Implicit method - allows larger time steps")
print(f"  ⚠ Requires solving linear systems at each time step")

# Temporal vs spatial considerations
print(f"\nTemporal vs Spatial Discretization:")
print(f"  • Time discretization: Testing dt refinement")
print(f"  • Spatial grid: Fixed at 101 points")
print(f"  • Total error = temporal error + spatial error")
print(f"  • For balanced accuracy, both dt and dx should be refined")

finest_dt = dt_values[-1]
coarsest_dt = dt_values[0]
comp_ratio = coarsest_dt / finest_dt  # Roughly proportional to computational cost

print(f"\nComputational Efficiency:")
print(f"  Time step ratio (finest/coarsest): {comp_ratio:.1f}x")
print(f"  Error improvement ratio: {errors[0]/errors[-1]:.1f}x")
print(f"  Efficiency: {(errors[0]/errors[-1])/comp_ratio:.2f}x error reduction per unit cost")

print(f"\nStability Considerations:")
print(f"  • CN method: Unconditionally stable for any dt")
print(f"  • Explicit methods would require dt ≤ O(dx²/σ²)")
print(f"  • Current dt range: {dt_values[-1]:.6f} to {dt_values[0]:.6f}")
print(f"  • All tested dt values are stable for CN method")

print("="*70)