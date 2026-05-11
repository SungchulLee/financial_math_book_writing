# Implied Volatility (Single Option Analysis)

## Background

Black Scholes Iv Single Option

Educational script demonstrating black scholes iv single option concepts.

---

## Code

```python
"""
Black Scholes Iv Single Option

Educational script demonstrating black scholes iv single option concepts.
"""

# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_1_SINGLE_OPTION_ANALYSIS.py 
# ============================================================================
import black_scholes as bs

# Initialize for single option


if __name__ == "__main__":
    model = bs.BlackScholesImpliedVol(
        S0=100,      # Stock price
        K=105,       # Strike price
        T=0.25,      # 3 months
        r=0.05,      # 5% risk-free rate
        sigma=0.2,   # Initial volatility
        q=0.02       # 2% dividend yield
    )
    
    # Market price of the option
    market_price = 7.5
    
    print(f"Option Parameters:")
    print(f"  S₀: ${model.S0}, K: ${model.K}, T: {model.T}yr, r: {model.r:.1%}, q: {model.q:.1%}")
    print(f"  Market Price: ${market_price}")
    
    # Compute implied volatility
    implied_vol = model.compute(
        market_price=market_price,
        sigma_0=0.2,
        option_type="call"
    )
    
    print(f"\n✅ Implied Volatility: {implied_vol:.4f} ({implied_vol*100:.2f}%)")
```


## Exercises

**Exercise 1.**
For $S_0 = 100$, $K = 105$, $T = 0.25$, $r = 0.05$, $q = 0.02$, and market price $\$7.50$ for a call, compute the BS price at $\sigma = 0.3$ and determine whether the implied volatility is above or below 30%.

??? success "Solution to Exercise 1"
    At $\sigma = 0.3$: $d_1 = \frac{\ln(100/105) + (0.03 + 0.045)(0.25)}{0.3(0.5)} = \frac{-0.0488 + 0.01875}{0.15} = -0.200$. $d_2 = -0.350$. $C = 99.5 N(-0.200) - 103.69 N(-0.350) = 99.5(0.4207) - 103.69(0.3632) = 41.86 - 37.66 = \$4.20$. Since $4.20 < 7.50$, the market price is higher, so IV $> 30\%$.

---

**Exercise 2.**
Starting the Newton-Raphson from $\sigma_0 = 0.2$, describe the first iteration step to find the IV for the $\$7.50$ call.

??? success "Solution to Exercise 2"
    At $\sigma_0 = 0.2$: compute $C(0.2)$ and $\text{Vega}(0.2)$, then $\sigma_1 = 0.2 - (C(0.2) - 7.50)/\text{Vega}(0.2)$. If $C(0.2) = 2.29$ and $\text{Vega}(0.2) = 18.6$: $\sigma_1 = 0.2 - (2.29 - 7.50)/18.6 = 0.2 + 5.21/18.6 = 0.2 + 0.280 = 0.480$. The large step indicates $\sigma_0$ was far from the solution.

---

**Exercise 3.**
Explain why the IV for a call equals the IV for a put at the same strike and maturity (assuming European options and the same underlying).

??? success "Solution to Exercise 3"
    Put-call parity: $C - P = S_0 e^{-qT} - Ke^{-rT}$. This relationship holds for any $\sigma$, so $C(\sigma) - P(\sigma) = S_0 e^{-qT} - Ke^{-rT}$ is independent of $\sigma$. If $C_{\text{market}} - P_{\text{market}} = S_0 e^{-qT} - Ke^{-rT}$ (no arbitrage), then $C_{\text{BS}}(\sigma_{\text{IV}}) = C_{\text{market}}$ implies $P_{\text{BS}}(\sigma_{\text{IV}}) = P_{\text{market}}$. The IV is the same.

---

**Exercise 4.**
The dividend yield $q = 0.02$ affects the IV computation. If $q$ is misspecified as 0, how does this bias the computed IV?

??? success "Solution to Exercise 4"
    With $q = 0$, the BS call price $C(S_0, \sigma)$ is higher than with $q = 0.02$ (dividends reduce call value). To match the market price, the solver finds a lower $\sigma$ to compensate. Therefore, misspecifying $q = 0$ when the true $q = 0.02$ biases IV downward. The bias is approximately $\Delta\sigma \approx q\sqrt{T}/\sigma \approx 0.02(0.5)/0.3 \approx 0.033$ or 3.3 percentage points.