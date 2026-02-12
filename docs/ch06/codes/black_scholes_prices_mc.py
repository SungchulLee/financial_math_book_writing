# ============================================================================
# black_scholes_OPTION_PRICES_USING_MONTE_CARLO.py
# ============================================================================
import black_scholes as bs

# Parameters
S = 100        # Initial stock price
K = 100        # Strike price
T = 1/12       # Time to maturity (1 month)
mu = 0.1       # Drift (used for simulation)
r = 0.05       # Risk-free rate
q = 0.0        # Dividend yield
sigma = 0.2    # Volatility
steps_per_year = 252*2
num_paths = 100_000
seed = 42

# Create Black-Scholes model using the wrapper
bs_model = bs.BlackScholes(S, K, T, r, sigma, q)

# Compute option prices using the Black-Scholes analytical formula
call_formula, put_formula = bs_model.price_analytical()

# Compute option prices using Monte Carlo simulation with empirical confidence intervals
result = bs_model.price_monte_carlo(
    num_paths=num_paths, 
    steps_per_year=steps_per_year, 
    seed=seed,
    plot_histogram=True  # Set to True to see the distributions
)

call_mc, put_mc, call_mc_std, put_mc_std, call_ci, put_ci, call_prices, put_prices = result

# Bootstrap confidence intervals for E[option price]
call_bootstrap_ci = bs_model.monte_carlo.calculate_bootstrap_ci(call_prices)
put_bootstrap_ci = bs_model.monte_carlo.calculate_bootstrap_ci(put_prices)

# Display results
print()
print("-" * 80)
print("OPTION PRICING COMPARISON")
print("-" * 80)
print(f"{'Method':<15}{'Call Price':>12}{'Put Price':>12}")
print("-" * 80)
print(f"{'Black-Scholes':<15}{call_formula:12.4f}{put_formula:12.4f}")
print(f"{'Monte Carlo':<15}{call_mc:12.4f}{put_mc:12.4f}")
print(f"{'Difference':<15}{abs(call_mc - call_formula):12.4f}{abs(put_mc - put_formula):12.4f}")
print("-" * 80)

print(f"\n95% Bootstrap CI for E[Option Price] (Monte Carlo Estimation Accuracy):")
print(f"Call E[X]: [{call_bootstrap_ci[0]:.4f}, {call_bootstrap_ci[1]:.4f}]  (width: {call_bootstrap_ci[1] - call_bootstrap_ci[0]:.4f})")
print(f"Put  E[X]: [{put_bootstrap_ci[0]:.4f}, {put_bootstrap_ci[1]:.4f}]  (width: {put_bootstrap_ci[1] - put_bootstrap_ci[0]:.4f})")

print(f"\nMonte Carlo Estimation Quality:")
call_contains_bs = call_bootstrap_ci[0] <= call_formula <= call_bootstrap_ci[1]
put_contains_bs = put_bootstrap_ci[0] <= put_formula <= put_bootstrap_ci[1]
print(f"Call - BS within MC 95% CI for E[X]: {call_formula:.4f} {'✓' if call_contains_bs else '✗'}")
print(f"Put  - BS within MC 95% CI for E[X]: {put_formula:.4f} {'✓' if put_contains_bs else '✗'}")

if call_contains_bs and put_contains_bs:
    print("✓ Excellent! Monte Carlo estimates are statistically consistent with Black-Scholes")
else:
    print("⚠ Monte Carlo estimates may need more paths or different parameters")

print(f"\n95% Confidence Intervals for Option Prices (Empirical - shows price variability):")
print(f"Call Option: [{call_ci[0]:.4f}, {call_ci[1]:.4f}]  <- 95% of simulated call prices")
print(f"Put Option:  [{put_ci[0]:.4f}, {put_ci[1]:.4f}]  <- 95% of simulated put prices")

print(f"\nInterpretation:")
print(f"• Bootstrap CI: How precisely we estimated E[Option Price] using {num_paths:,} MC paths")
print(f"• Empirical CI: Range of individual option outcomes (for risk assessment)")
print(f"• Narrow bootstrap CI = precise estimation of expected value")
print(f"• Wide empirical CI = high variability in option outcomes")

# Additional wrapper demonstration
print(f"\n{'-'*80}")
print("ADDITIONAL WRAPPER FEATURES")
print("-" * 80)

# Show comprehensive comparison using wrapper method
comparison = bs_model.compare_methods(option_type='call', mc_paths=num_paths)
print(f"\nComprehensive Method Comparison (Call Option):")
print(f"  Analytical Price:     ${comparison['analytical']:.4f}")
print(f"  Monte Carlo Price:    ${comparison['monte_carlo']['price']:.4f}")
print(f"  MC Standard Error:    ${comparison['monte_carlo']['std_error']:.6f}")
print(f"  MC 95% CI:            [{comparison['monte_carlo']['confidence_interval'][0]:.4f}, {comparison['monte_carlo']['confidence_interval'][1]:.4f}]")
print(f"  Numerical Price:      ${comparison['numerical']:.4f}")

print(f"\nMethod Differences:")
print(f"  MC vs Analytical:        ${comparison['differences']['mc_vs_analytical']:.6f}")
print(f"  Numerical vs Analytical: ${comparison['differences']['numerical_vs_analytical']:.6f}")
print(f"  MC vs Numerical:         ${comparison['differences']['mc_vs_numerical']:.6f}")

# Display Greeks
greeks = bs_model.calculate_greeks()
print(f"\nOption Greeks:")
print(f"  Delta (Call/Put):     {greeks['delta_call']:>8.4f} / {greeks['delta_put']:>8.4f}")
print(f"  Gamma:                {greeks['gamma']:>8.4f}")
print(f"  Vega:                 {greeks['vega']:>8.4f}")
print(f"  Theta (Call/Put):     {greeks['theta_call']:>8.4f} / {greeks['theta_put']:>8.4f}")
print(f"  Rho (Call/Put):       {greeks['rho_call']:>8.4f} / {greeks['rho_put']:>8.4f}")

# Model summary
print(f"\n{'-'*80}")
print("COMPLETE MODEL SUMMARY")
print("-" * 80)
bs_model.summary()

print()