# Implied Volatility (Figures)

## Background

Black Scholes Iv Figures

Educational script demonstrating black scholes iv figures concepts.

---

## Code

```python
"""
Black Scholes Iv Figures

Educational script demonstrating black scholes iv figures concepts.
"""

# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_6_FIGURES.py 
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
    
    # Load real VSTOXX data (with auto-download if needed)
    model.load_data(auto_download=True)  # This will download if file doesn't exist
    
    # Compute implied volatilities on real data
    model.compute_implied_volatility_batch(sigma_0=2.0)
    
    # Get summary statistics
    stats = model.get_summary_statistics()
    print(f"📊 Results Summary:")
    print(f"   ✅ Valid computations: {stats['count']:,}")
    print(f"   📈 Mean volatility: {stats['mean']:.4f} ({stats['mean']*100:.2f}%)")
    print(f"   📏 Range: {stats['min']:.4f} - {stats['max']:.4f}")
    print(f"   📊 Std deviation: {stats['std']:.4f}")
    
    # Plot 1: Volatility Smiles (creates its own figure)
    model.plot_volatility_smiles("Real VSTOXX Implied Volatility Smiles")
    
    # Plot 2: 3D Surface (creates its own figure)
    model.plot_3d_surface(
        title="Real VSTOXX - 3D Volatility Surface",
        save_path="./data/real_3d_surface.png"
    )
    
    # Plot 3: 3D Smiles (creates its own figure)
    model.plot_3d_smiles(
        title="Real VSTOXX - 3D Volatility Smiles",
        save_path="./data/real_3d_smiles.png"
    )
```


## Exercises

**Exercise 1.**
The volatility smile plots IV versus strike for fixed maturities. Explain why different maturities show different smile shapes.

??? success "Solution to Exercise 1"
    Short maturities show steeper smiles because: (1) near-term uncertainty is more concentrated, amplifying the impact of jumps and skewness; (2) the probability of extreme moves is relatively higher for short periods; (3) supply-demand effects (hedging pressure) are stronger near expiry. Longer maturities show flatter smiles as the CLT smooths out short-term effects and diffusion dominates jumps.

---

**Exercise 2.**
The 3D volatility surface plots IV as a function of both strike and maturity. Describe the typical shape for equity indices.

??? success "Solution to Exercise 2"
    For equity indices: the surface shows a pronounced skew (higher IV for low strikes) at short maturities, flattening at longer maturities. The term structure can be upward-sloping (contango, normal markets) or downward-sloping (backwardation, during crises). The ATM term structure typically rises with maturity reflecting the mean-reverting nature of volatility.

---

**Exercise 3.**
Explain why the 3D surface may have artifacts or missing data points, and how interpolation handles these gaps.

??? success "Solution to Exercise 3"
    Missing data occurs when: (1) certain strike-maturity combinations have no traded options; (2) options are too deep OTM/ITM for reliable IV computation; (3) the Newton-Raphson iteration fails to converge. Interpolation methods (cubic spline, radial basis functions, or SVI parametric fits) fill these gaps. Care must be taken to ensure the interpolated surface is arbitrage-free (no calendar spread or butterfly arbitrage).

---

**Exercise 4.**
If you observe IV of 110% for a 1-month VSTOXX option and 90% for a 1-year option, compute the forward implied volatility from month 1 to month 12 using the variance additive rule.

??? success "Solution to Exercise 4"
    Total variance: $\sigma_1^2 T_1 = 1.21 \times 1/12 = 0.1008$, $\sigma_2^2 T_2 = 0.81 \times 1 = 0.81$. Forward variance from $T_1$ to $T_2$: $\sigma_f^2(T_2 - T_1) = 0.81 - 0.1008 = 0.7092$. Forward vol: $\sigma_f = \sqrt{0.7092/0.9167} = \sqrt{0.7737} = 0.880$ or 88%. The forward vol is lower than the spot 1-month vol, indicating the market expects volatility to decrease after the near-term event.