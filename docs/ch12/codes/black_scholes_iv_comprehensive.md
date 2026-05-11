# Implied Volatility (Comprehensive Workflow)

## Background

Black Scholes Iv Comprehensive

Educational script demonstrating black scholes iv comprehensive concepts.

---

## Code

```python
"""
Black Scholes Iv Comprehensive

Educational script demonstrating black scholes iv comprehensive concepts.
"""

# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_ 3_COMPREHENSIVE_WORKFLOW.py 
# ============================================================================
import black_scholes as bs
    
# Initialize model


if __name__ == "__main__":
    model = bs.BlackScholesImpliedVol(
            S0=17.6639,  # VSTOXX spot value
            K=18.0,      # Placeholder
            T=0.25,      # Placeholder
            r=0.01,      # Risk-free rate
            sigma=0.2,   # Initial volatility
            tol=0.5      # Moneyness tolerance
        )
    
    # Load data
    model.load_data()
    
    # Compute implied volatilities
    bs.compute_implied_volatilities_and_summarize(model, sigma_0=2.0, print_summary=False)
    
    # Use the built-in comprehensive analysis
    results = model.run_full_analysis(
        create_plots=True,
        save_results=True,
        results_dir="./data/comprehensive_unified"
    )
        
    print(f"✅ Comprehensive analysis completed!")
    print(f"📁 Results saved to: ./data/comprehensive_unified/")
        
    # Show summary of what was generated
    print(f"\n📋 Generated Results:")
    for key, value in results.items():
        if hasattr(value, 'shape'):  # DataFrame
            print(f"   📊 {key}: {value.shape} data")
        elif isinstance(value, dict):
            print(f"   📋 {key}: {len(value)} metrics")
        elif value is not None:
            print(f"   ✅ {key}: Generated")
```


## Exercises

**Exercise 1.**
The Newton-Raphson method for implied volatility solves $f(\sigma) = C_{\text{BS}}(\sigma) - C_{\text{market}} = 0$. Write the iteration formula using vega as the derivative.

??? success "Solution to Exercise 1"
    $\sigma_{n+1} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{\text{Vega}(\sigma_n)}$ where $\text{Vega} = S\sqrt{T}n(d_1)$. Convergence is quadratic when $\sigma_0$ is close to the solution. The method fails if vega is near zero (deep ITM/OTM options).

---

**Exercise 2.**
A VSTOXX call option has market price $\$2.50$, $S_0 = 17.66$, $K = 18$, $T = 0.25$, $r = 0.01$. Starting from $\sigma_0 = 2.0$, explain why such a high initial guess is needed for volatility indices.

??? success "Solution to Exercise 2"
    VSTOXX measures volatility of the EURO STOXX 50, with typical values 15--30. Since VSTOXX itself is a volatility index, the "volatility of volatility" is often 50--200%. Starting at $\sigma_0 = 2.0$ (200%) ensures the Newton iteration begins in the right range. A typical equity starting point of $\sigma_0 = 0.2$ would be far too low.

---

**Exercise 3.**
The moneyness filter $|S/K - 1| < \text{tol}$ with $\text{tol} = 0.5$ retains options within 50% of ATM. Explain why very deep ITM/OTM options are excluded from IV computation.

??? success "Solution to Exercise 3"
    Deep ITM/OTM options have near-zero vega, making the Newton iteration ill-conditioned (division by near-zero). Additionally, their prices are dominated by intrinsic value (ITM) or are extremely small (OTM), so small price errors lead to large IV errors. The moneyness filter excludes these unreliable points.

---

**Exercise 4.**
The volatility smile for VSTOXX shows higher IV for OTM puts. Explain this pattern in terms of market fear and demand for downside protection.

??? success "Solution to Exercise 4"
    OTM puts on VSTOXX protect against sudden drops in volatility (which correspond to market rallies). However, the more common pattern is: OTM puts on equity indices have higher IV (skew) due to demand for crash protection. For VSTOXX, since it rises during crises, OTM calls on VSTOXX (corresponding to market fear) may have elevated IV. The smile shape reflects supply-demand imbalances and the non-lognormal distribution of the underlying.