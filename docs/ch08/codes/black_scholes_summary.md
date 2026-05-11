# Comprehensive Summary

## Background

Black Scholes Summary

Educational script demonstrating black scholes summary concepts.

---

## Code

```python
"""
Black Scholes Summary

Educational script demonstrating black scholes summary concepts.
"""

# ============================================================================
# black_scholes_COMPREHENSIVE_SUMMARY.py
# ============================================================================
import black_scholes as bs
   
# Model parameters


if __name__ == "__main__":
    S0 = 100      # Current stock price
    K = 105       # Strike price
    T = 0.25      # 3 months to expiration
    r = 0.05      # 5% risk-free rate
    sigma = 0.2   # 20% volatility
    q = 0.02      # 2% dividend yield
    mu = 0.1
  
    bs.BlackScholes(S0=S0, K=K, T=T, r=r, sigma=sigma, q=q).summary()
```


## Exercises

**Exercise 1.**
Compute the European call price for $S_0 = 100$, $K = 105$, $T = 0.25$, $r = 0.05$, $\sigma = 0.2$, and $q = 0.02$ using the Black-Scholes formula with continuous dividends.

??? success "Solution to Exercise 1"
    With dividends: $d_1 = \frac{\ln(100/105) + (0.05 - 0.02 + 0.02)(0.25)}{0.2\sqrt{0.25}} = \frac{-0.0488 + 0.0125}{0.1} = -0.363$. Then $d_2 = -0.463$. The call is $C = 100 e^{-0.005} N(-0.363) - 105 e^{-0.0125} N(-0.463) = 99.50(0.358) - 103.69(0.322) = \$2.29$.

---

**Exercise 2.**
List all five Greeks for the option in Exercise 1 and state their signs.

??? success "Solution to Exercise 2"
    Delta $= e^{-qT} N(d_1) = 0.357$ (positive); Gamma $= e^{-qT} n(d_1) / (S\sigma\sqrt{T}) > 0$ (positive); Vega $= Se^{-qT}\sqrt{T} n(d_1) > 0$ (positive); Theta $< 0$ (negative, time decay); Rho $= KTe^{-rT}N(d_2) > 0$ (positive). Delta is most important for short-term hedging.

---

**Exercise 3.**
Compute the put price via put-call parity with continuous dividends: $P = C - S_0 e^{-qT} + K e^{-rT}$.

??? success "Solution to Exercise 3"
    $$
    P = 2.29 - 100 e^{-0.005} + 105 e^{-0.0125} = 2.29 - 99.50 + 103.69 = \$6.48
    $$

---

**Exercise 4.**
Explain how the dividend yield $q = 0.02$ affects call and put prices compared to $q = 0$, and compute the call price difference.

??? success "Solution to Exercise 4"
    With $q = 0$: $d_1 = (-0.0488 + 0.0175)/0.1 = -0.313$, giving $C = 100(0.377) - 103.69(0.340) = \$2.48$. The dividend reduces the call by $2.48 - 2.29 = \$0.19$ because dividends lower the expected terminal stock price, reducing call values and increasing put values.