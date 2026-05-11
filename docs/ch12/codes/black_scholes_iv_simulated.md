# Implied Volatility (Simulated Data)

## Background

Black Scholes Iv Simulated

Educational script demonstrating black scholes iv simulated concepts.

---

## Code

```python
"""
Black Scholes Iv Simulated

Educational script demonstrating black scholes iv simulated concepts.
"""

# ============================================================================
# black_scholes_IMPLIED_VOLATILITY.py 
# ============================================================================
import black_scholes as bs
    
# Create model with synthetic data


if __name__ == "__main__":
    model = bs.BlackScholesImpliedVol(S0=100, K=100, T=0.25, r=0.05, sigma=0.2, tol=0.3)
    model.create_synthetic_data()
    
    # Compute implied volatilities
    bs.compute_implied_volatilities_and_summarize(model, sigma_0=2.0)
    
    # Run advanced analysis
    bs.run_advanced_analysis_on_implied_vol(model)
```


## Exercises

**Exercise 1.**
Synthetic option data is generated using known $\sigma = 0.2$. After computing IV, all recovered values should be 0.2. What errors might cause deviations?

??? success "Solution to Exercise 1"
    Deviations arise from: (1) Newton-Raphson tolerance not tight enough; (2) numerical errors in $N(d)$ computation for extreme $d$ values; (3) deep ITM/OTM options where vega is tiny, causing division by near-zero; (4) floating-point precision limits ($\sim 10^{-15}$). For well-conditioned ATM options, the recovered IV should match to 8+ decimal places.

---

**Exercise 2.**
Explain the flat volatility smile that results from GBM-generated option prices. What model feature would create a non-flat smile?

??? success "Solution to Exercise 2"
    Under GBM, all options at the same maturity have the same $\sigma$ by construction, giving a flat smile. Non-flat smiles arise from: stochastic volatility (Heston), jumps (Merton), local volatility, or any non-lognormal feature. The smile is a "fingerprint" of the deviation from GBM assumptions.

---

**Exercise 3.**
For the synthetic data with $S_0 = 100$, $\sigma = 0.2$, $T = 0.25$, compute the ATM straddle price (call + put) and its sensitivity to $\sigma$.

??? success "Solution to Exercise 3"
    ATM straddle: $C + P = 2C - (S_0 - Ke^{-rT})$ by parity. For $K = 100$: $C \approx S_0\sigma\sqrt{T}/\sqrt{2\pi} \approx 100(0.2)(0.5)/2.507 = \$3.99$. Straddle $\approx 2(3.99) - (100 - 98.77) = 7.98 - 1.23 = \$6.75$. Sensitivity: $\partial(\text{straddle})/\partial\sigma \approx 2 \times \text{Vega} = 2 \times S\sqrt{T}n(d_1) \approx 2(100)(0.5)(0.399) = \$39.9$ per 100% vol change.

---

**Exercise 4.**
The advanced analysis includes term structure and skew metrics. For flat IV, what should the term structure slope and skew be?

??? success "Solution to Exercise 4"
    Under GBM with constant $\sigma$: the IV term structure is perfectly flat (same $\sigma$ for all maturities), so the slope is zero. The skew (IV difference between OTM puts and ATM) is also zero since the smile is flat. Any nonzero slope or skew in the synthetic data indicates numerical artifacts or insufficient convergence in the IV solver.