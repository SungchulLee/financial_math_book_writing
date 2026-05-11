# Implied Volatility (Custom Analysis)

## Background

Black Scholes Iv Custom Filter

Educational script demonstrating black scholes iv custom filter concepts.

---

## Code

```python
"""
Black Scholes Iv Custom Filter

Educational script demonstrating black scholes iv custom filter concepts.
"""

# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_ 4_CUSTOM_ANALYSIS_AND_FILTERING.py 
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
    bs.compute_implied_volatilities_and_summarize(model, print_summary=False)
    
    print(f"🔍 Custom Filtering Examples:")
    
    # High volatility options
    high_vol = model.filter_options(min_vol=0.4, max_ttm=0.5)
    print(f"   📈 High volatility options (>40%, <6mo): {len(high_vol)}")
    
    # ATM options
    atm_options = model.filter_options(min_moneyness=0.95, max_moneyness=1.05)
    print(f"   🎯 ATM options (95-105% moneyness): {len(atm_options)}")
    
    # Short-term options
    short_term = model.filter_options(max_ttm=0.25)
    print(f"   ⏰ Short-term options (<3mo): {len(short_term)}")
    
    # Custom analysis on filtered data
    if len(atm_options) > 0:
        atm_vol_mean = atm_options['IMP_VOL'].mean()
        print(f"   📊 ATM average volatility: {atm_vol_mean:.4f}")
```


## Exercises

**Exercise 1.**
Define moneyness as $m = S_0/K$. For $S_0 = 17.66$, compute the moneyness for strikes $K = 15, 17, 18, 20, 22$. Classify each as ITM, ATM, or OTM for a call.

??? success "Solution to Exercise 1"
    $m = 17.66/K$: $K=15$: $m=1.177$ (ITM); $K=17$: $m=1.039$ (near ATM); $K=18$: $m=0.981$ (near ATM); $K=20$: $m=0.883$ (OTM); $K=22$: $m=0.803$ (deep OTM). ATM is typically $0.95 < m < 1.05$.

---

**Exercise 2.**
Filtering for $\text{min\_vol} = 0.4$ and $\text{max\_ttm} = 0.5$ selects high-volatility short-term options. Explain why this subset is particularly interesting for traders.

??? success "Solution to Exercise 2"
    High IV short-term options have the fastest time decay (theta), making them attractive for option sellers collecting premium. They also indicate market expectation of near-term turbulence. For market makers, these options have the highest gamma risk and require more frequent hedging.

---

**Exercise 3.**
If the ATM average volatility is $\bar{\sigma}_{\text{ATM}} = 1.20$ (120%), explain what this means for the expected range of the VSTOXX index over the next 3 months.

??? success "Solution to Exercise 3"
    A 120% annualized volatility means the 3-month standard deviation is $1.20\sqrt{0.25} = 0.60$, or 60% of the current level. For $S_0 = 17.66$: one-std-dev range is $17.66 \times (1 \pm 0.60) = [7.06, 28.26]$. The 95% range is approximately $[17.66 e^{-1.20}, 17.66 e^{1.20}] = [5.32, 58.59]$. This extremely wide range reflects the high uncertainty in volatility forecasting.

---

**Exercise 4.**
Explain the difference between filtering options by moneyness versus by delta. Which is more stable across different volatility environments?

??? success "Solution to Exercise 4"
    Moneyness $S/K$ is a fixed ratio independent of volatility. Delta depends on $\sigma$: $\Delta = N(d_1)$ where $d_1$ involves $\sigma$. In high-vol environments, a 90% moneyness option may have $\Delta = 0.6$, while in low vol it has $\Delta = 0.3$. Delta-based filtering (e.g., 25-delta puts) is more stable because it represents the same probability of exercise regardless of vol level, making it preferred for cross-market and cross-time comparisons.