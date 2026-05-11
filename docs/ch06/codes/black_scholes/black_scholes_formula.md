# Black Scholes Formula

## Background

Analytical BS formulas and option pricing.
UNCHANGED API - improved internal implementation using utility functions.

---

## Code

```python
# ============================================================================
# black_scholes/black_scholes_formula.py
# ============================================================================
"""
Analytical BS formulas and option pricing.
UNCHANGED API - improved internal implementation using utility functions.
"""

from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import bs_call_price, bs_put_price

class BlackScholesFormula(BlackScholesBase):
    """
    Analytical Black-Scholes formula implementation.
    API UNCHANGED - delegates to utility functions for consistency.
    """
    
    def price(self):
        """
        Calculate call and put option prices.
        UNCHANGED API - now delegates to utility functions.
        """
        return (
            bs_call_price(self.S0, self.K, self.T, self.r, self.sigma, self.q),
            bs_put_price(self.S0, self.K, self.T, self.r, self.sigma, self.q)
        )


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Derive the Black-Scholes call price formula starting from the risk-neutral expectation $C = e^{-rT}E^Q[\max(S_T - K, 0)]$.

??? success "Solution to Exercise 1"
    Under the risk-neutral measure, $S_T = S_0 \exp\!\bigl((r - q - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z\bigr)$ where $Z \sim \mathcal{N}(0,1)$.

    $$
    C = e^{-rT}\int_{-\infty}^{\infty} \max(S_T(z) - K, 0)\,\phi(z)\,dz
    $$

    The payoff is positive when $S_T > K$, i.e., when $z > -d_2$ where $d_2 = [\ln(S_0/K) + (r - q - \frac{1}{2}\sigma^2)T]/(\sigma\sqrt{T})$. Splitting and evaluating the integrals:

    $$
    C = S_0 e^{-qT}\mathcal{N}(d_1) - K e^{-rT}\mathcal{N}(d_2)
    $$

    where $d_1 = d_2 + \sigma\sqrt{T}$ and $\Phi$ is the standard normal CDF.

---

**Exercise 2.**
Compute the call and put prices for $S_0 = 100$, $K = 105$, $T = 0.5$, $r = 0.03$, $\sigma = 0.25$, $q = 0$.

??? success "Solution to Exercise 2"
    $$
    d_1 = \frac{\ln(100/105) + (0.03 + 0.03125) \times 0.5}{0.25\sqrt{0.5}} = \frac{-0.04879 + 0.03063}{0.17678} = \frac{-0.01816}{0.17678} = -0.1027
    $$

    $$
    d_2 = -0.1027 - 0.17678 = -0.2795
    $$

    From tables: $\Phi(-0.1027) \approx 0.4591$, $\Phi(-0.2795) \approx 0.3899$.

    $$
    C = 100 \times 0.4591 - 105 \times e^{-0.015} \times 0.3899 \approx 45.91 - 40.32 = \$5.59
    $$

    By put-call parity: $P = C - S_0 + Ke^{-rT} = 5.59 - 100 + 103.44 = \$9.03$.

---

**Exercise 3.**
Show that the `price()` method delegates to utility functions `bs_call_price` and `bs_put_price`. What is the software engineering benefit of this delegation pattern?

??? success "Solution to Exercise 3"
    The `price()` method simply returns `(bs_call_price(...), bs_put_price(...))`, passing through all parameters. This delegation pattern has several benefits:

    1. **Reusability**: The utility functions can be called independently without creating a class instance (useful for vectorized computations or quick calculations).
    2. **Testability**: Pure functions are easier to unit test than class methods.
    3. **Consistency**: All pricing code (analytical, MC, numerical) can share the same utility functions, ensuring identical $d_1, d_2$ calculations.
    4. **Maintainability**: Bug fixes in the utility function automatically propagate to all callers.

---

**Exercise 4.**
Verify put-call parity $C - P = S_0 e^{-qT} - K e^{-rT}$ algebraically using the Black-Scholes formulas.

??? success "Solution to Exercise 4"
    $$
    C - P = [S_0 e^{-qT}\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)] - [Ke^{-rT}\mathcal{N}(-d_2) - S_0 e^{-qT}\mathcal{N}(-d_1)]
    $$

    $$
    = S_0 e^{-qT}[\mathcal{N}(d_1) + \mathcal{N}(-d_1)] - Ke^{-rT}[\mathcal{N}(d_2) + \mathcal{N}(-d_2)]
    $$

    Since $\Phi(x) + \Phi(-x) = 1$ for all $x$:

    $$
    C - P = S_0 e^{-qT} - Ke^{-rT}
    $$

    This confirms put-call parity holds for the Black-Scholes formulas with dividends.
