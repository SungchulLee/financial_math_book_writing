# Option Prices (Using Monte Carlo)

## Background

Black Scholes Prices Mc

Educational script demonstrating black scholes prices mc concepts.

---

## Code

```python
"""
Black Scholes Prices Mc

Educational script demonstrating black scholes prices mc concepts.
"""

# ============================================================================
# black_scholes_OPTION_PRICES_USING_MONTE_CARLO.py
# ============================================================================
import black_scholes as bs

# Parameters


if __name__ == "__main__":
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
```

## Exercises

**Exercise 1.**
Describe the Monte Carlo procedure for pricing a European call option. List the steps from parameter input to price output.

??? success "Solution to Exercise 1"

    1. **Set parameters**: $S_0, K, T, r, \sigma, q$, number of paths $N$.
    2. **Generate random numbers**: Draw $Z_1, \ldots, Z_N \sim \mathcal{N}(0,1)$.
    3. **Simulate terminal prices**: $S_T^{(i)} = S_0\exp((r-q-\frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z_i)$.
    4. **Compute payoffs**: $\phi_i = \max(S_T^{(i)} - K, 0)$.
    5. **Discount and average**: $\hat{C} = e^{-rT}\frac{1}{N}\sum_{i=1}^N \phi_i$.
    6. **Compute standard error**: $\mathrm{SE} = e^{-rT}\cdot s_\phi / \sqrt{N}$ where $s_\phi$ is the sample std of payoffs.
    7. **Report**: $\hat{C} \pm 1.96\,\mathrm{SE}$ (95% CI).

---

**Exercise 2.**
The MC estimate has a standard error. Explain the difference between bias and variance in MC estimators. Is the BS MC estimator unbiased?

??? success "Solution to Exercise 2"
    **Bias** is the systematic error: $E[\hat{C}] - C_{\text{true}}$. **Variance** is the random error: $\mathrm{Var}(\hat{C})$.

    The BS MC estimator using the exact GBM solution (not Euler discretization) is **unbiased**: $E[\hat{C}] = e^{-rT}E^Q[\max(S_T - K, 0)] = C_{\text{BS}}$ exactly. The variance is $\mathrm{Var}(\hat{C}) = \mathrm{Var}(e^{-rT}\phi) / N$, which decreases as $1/N$.

    If Euler discretization is used instead of the exact solution, a small bias of $O(\Delta t)$ is introduced. This time-stepping bias does not decrease with $N$, so it eventually dominates for large $N$.

---

**Exercise 3.**
With $N = 10{,}000$ paths, the MC call price is $\$10.42 \pm 0.15$ (95% CI). The BS formula gives $\$10.45$. Is the MC result consistent with the analytical value?

??? success "Solution to Exercise 3"
    The 95% CI is $[10.42 - 0.15, 10.42 + 0.15] = [10.27, 10.57]$. Since the analytical value $10.45$ falls within this interval, the MC result is consistent.

    The deviation $|10.42 - 10.45| = 0.03$ is well within one standard error ($0.15/1.96 \approx 0.077$), corresponding to about $0.39$ standard deviations. There is no evidence of bias.

---

**Exercise 4.**
How would you modify the MC simulation to price a put option instead of a call? Does the variance of the put payoff differ from the call payoff?

??? success "Solution to Exercise 4"
    Simply change the payoff function from $\max(S_T - K, 0)$ to $\max(K - S_T, 0)$. Everything else remains the same.

    The put payoff variance is generally **different** from the call payoff variance. For ATM options, put payoff variance is usually lower because the put payoff is bounded by $K$ while the call payoff is unbounded. For deep OTM puts ($K \ll S_0$), the variance is very small (most paths give zero payoff). This means MC pricing is more efficient for puts than for calls in terms of standard error per path.
