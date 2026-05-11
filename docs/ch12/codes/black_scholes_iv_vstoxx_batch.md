# VSTOXX Demo

## Background

Black Scholes Iv Vstoxx Batch

Educational script demonstrating black scholes iv vstoxx batch concepts.

---

## Code

```python
"""
Black Scholes Iv Vstoxx Batch

Educational script demonstrating black scholes iv vstoxx batch concepts.
"""

# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_ 2_VSTOXX BATCH_ANALYSIS.py 
# ============================================================================
import black_scholes as bs
    
# Initialize for VSTOXX


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
    
    # Show data summary
    data_summary = model.get_data_summary()
    print(f"  📊 Total options: {data_summary['total_options']:,}")
    print(f"  📅 Unique maturities: {data_summary['unique_maturities']}")
    print(f"  💲 Strike range: {data_summary['strike_range']['min']:.1f} - {data_summary['strike_range']['max']:.1f}", end="\n"*2)
    
    # Compute implied volatilities
    bs.compute_implied_volatilities_and_summarize(model, sigma_0=2.0)
    
    # Run advanced analysis
    bs.run_advanced_analysis_on_implied_vol(model)
```


## Exercises

**Exercise 1.**
The VSTOXX data has multiple maturities and strikes. Explain why batch processing (computing IV for all options at once) is more efficient than individual computation.

??? success "Solution to Exercise 1"
    Batch processing allows: (1) vectorized computation of $d_1$, $d_2$, and BS prices across all options simultaneously; (2) shared forward price and discount factor calculations per maturity; (3) efficient memory layout for Newton iterations. Individual computation has overhead from function call setup for each option. Vectorization can speed up IV computation by 10--100x for thousands of options.

---

**Exercise 2.**
The data shows that short-maturity options have higher IV than long-maturity options (backwardation). What market condition causes this term structure shape?

??? success "Solution to Exercise 2"
    Backwardation (inverted term structure) occurs during market stress: current implied volatility is elevated due to immediate uncertainty, but the market expects volatility to mean-revert to lower levels over time. This is common after sharp market drops or during crisis periods. The opposite (contango) occurs in calm markets where vol is low but expected to rise.

---

**Exercise 3.**
Explain why the initial guess $\sigma_0 = 2.0$ is appropriate for VSTOXX options but would be problematic for equity options.

??? success "Solution to Exercise 3"
    VSTOXX options have IVs typically in the range 50--200% because the underlying (VSTOXX index, typically 15--30) has high percentage volatility. Starting at $\sigma_0 = 2.0$ (200%) is within the feasible range. For equity options with IVs of 10--50%, $\sigma_0 = 2.0$ is far too high, causing the Newton iteration to overshoot or converge slowly. Starting at $\sigma_0 = 0.2$--$0.5$ is more appropriate for equities.

---

**Exercise 4.**
The advanced analysis includes plotting IV smiles grouped by maturity. Describe what a "volatility term structure" plot shows and how to construct it from the batch IV results.

??? success "Solution to Exercise 4"
    The volatility term structure plots ATM IV versus time to maturity. Construction: (1) for each maturity, identify the strike closest to $S_0$ (or interpolate to find exact ATM IV); (2) plot these ATM IVs against the corresponding maturities. The resulting curve shows how the market prices near-term versus long-term uncertainty. Additional information comes from plotting 25-delta put IV and 25-delta call IV term structures, which show how skew evolves with maturity.