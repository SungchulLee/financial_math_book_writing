# Sensitivity Analysis

## Background

Black Scholes Sensitivity

Educational script demonstrating black scholes sensitivity concepts.

---

## Code

```python
"""
Black Scholes Sensitivity

Educational script demonstrating black scholes sensitivity concepts.
"""

# ============================================================================
# black_scholes_SENSITIVITY_ANALYSIS.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Model parameters
    S0 = 100      # Current stock price
    K = 105       # Strike price
    T = 0.25      # 3 months to expiration
    r = 0.05      # 5% risk-free rate
    sigma = 0.2   # 20% volatility
    q = 0.02      # 2% dividend yield
    mu = 0.1
    
    # =============================================================================
    # SENSITIVITY ANALYSIS
    # =============================================================================
    print("Analyzing option price sensitivity to parameters...")
    
    # Volatility sensitivity
    vol_range = np.linspace(0.1, 0.4, 10)
    call_prices_vol = []
    
    for vol in vol_range:
        bs_temp = bs.BlackScholes(S0, K, T, r, vol, q)
        call_temp, _ = bs_temp.price_analytical()
        call_prices_vol.append(call_temp)
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(vol_range*100, call_prices_vol, 'b-', linewidth=2, marker='o')
    plt.axvline(sigma*100, color='red', linestyle='--', alpha=0.7, 
                label=f'Current σ = {sigma*100:.1f}%')
    plt.xlabel('Volatility (%)')
    plt.ylabel('Call Price ($)')
    plt.title('Call Price vs Volatility')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Stock price sensitivity
    S_range = np.linspace(80, 120, 20)
    call_prices_S = []
    
    for S in S_range:
        bs_temp = bs.BlackScholes(S, K, T, r, sigma, q)
        call_temp, _ = bs_temp.price_analytical()
        call_prices_S.append(call_temp)
    
    plt.subplot(1, 2, 2)
    plt.plot(S_range, call_prices_S, 'g-', linewidth=2, marker='o')
    plt.axvline(S0, color='red', linestyle='--', alpha=0.7, 
                label=f'Current S₀ = ${S0}')
    plt.axhline(K, color='orange', linestyle=':', alpha=0.7, 
                label=f'Strike K = ${K}')
    plt.xlabel('Stock Price ($)')
    plt.ylabel('Call Price ($)')
    plt.title('Call Price vs Stock Price')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Plot (conceptually) the call price as a function of volatility $\sigma \in [0.1, 0.4]$ for an ATM option. Is the relationship linear, convex, or concave?

??? success "Solution to Exercise 1"
    The call price increases with $\sigma$ (positive vega). The relationship is approximately linear for small $\sigma$ changes but slightly concave for large ranges. This is because vega itself decreases as $\sigma$ increases (the second derivative of price with respect to $\sigma$, called "volga" or "vomma", can be negative for certain parameters). For ATM options, the price-vol curve is nearly linear over typical ranges.

---

**Exercise 2.**
For $S_0 = 100$, $K = 105$, $T = 0.25$, $r = 0.05$, $\sigma = 0.2$, $q = 0.02$, compute the call price sensitivity to a 1% increase in volatility (from 20% to 21%).

??? success "Solution to Exercise 2"
    Vega $\approx S_0 e^{-qT} \sqrt{T} \cdot n(d_1) = 99.5 \times 0.5 \times n(-0.363) = 49.75 \times 0.374 = \$18.60$ per 100% vol change, or $\$0.186$ per 1% change. So the call price increases by approximately $\$0.19$ when $\sigma$ goes from 20% to 21%.

---

**Exercise 3.**
Explain why the call price is convex in the underlying price $S$ (i.e., gamma is positive) and the financial implication for delta hedging.

??? success "Solution to Exercise 3"
    Convexity ($\Gamma > 0$) means the call price curve lies above its tangent line at any point. For delta hedging: the hedge (short $\Delta$ shares) is linear, while the option payoff is convex. When $S$ moves, the option gains more (or loses less) than the linear hedge predicts. This "convexity advantage" is paid for through time decay (theta). Large moves benefit long-gamma positions; small moves benefit short-gamma positions.

---

**Exercise 4.**
Compare the sensitivity of call and put prices to the risk-free rate $r$. Which has positive rho and which has negative rho? Explain the economic intuition.

??? success "Solution to Exercise 4"
    Call rho is positive: $\rho_C = KTe^{-rT}N(d_2) > 0$. Put rho is negative: $\rho_P = -KTe^{-rT}N(-d_2) < 0$. Intuition: A call is a substitute for buying stock. Higher $r$ makes the deferred payment $Ke^{-rT}$ cheaper, increasing call value. A put substitutes for shorting stock. Higher $r$ makes the deferred receipt less valuable, decreasing put value.