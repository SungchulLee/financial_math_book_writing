# Black Scholes Base

## Background

Black Scholes Base

Educational script demonstrating black scholes base concepts.

---

## Code

```python
"""
Black Scholes Base

Educational script demonstrating black scholes base concepts.
"""

# ============================================================================
# black_scholes/black_scholes_base.py
# ============================================================================


class BlackScholesBase:
    def __init__(self, S0, K, T, r, sigma, q=0):
        self.S0 = S0        # Initial stock price
        self.K = K          # Strike price
        self.T = T          # Time to maturity (in years)
        self.r = r          # Risk-free interest rate
        self.sigma = sigma  # Volatility of the underlying asset
        self.q = q          # Continuous dividend yield


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
List the six parameters stored in `BlackScholesBase`. For each, give a typical range of values and explain its financial meaning.

??? success "Solution to Exercise 1"
    | Parameter | Symbol | Typical Range | Financial Meaning |
    |-----------|--------|--------------|-------------------|
    | `S0` | $S_0$ | \$50--\$500 | Current market price of the underlying asset |
    | `K` | $K$ | \$50--\$500 | Strike (exercise) price of the option |
    | `T` | $T$ | 0.01--5 years | Time remaining until the option expires |
    | `r` | $r$ | 0--0.10 | Annualized risk-free interest rate |
    | `sigma` | $\sigma$ | 0.05--1.0 | Annualized volatility of the asset returns |
    | `q` | $q$ | 0--0.05 | Continuous dividend yield |

---

**Exercise 2.**
Write the Black-Scholes PDE that governs the option price $V(S, t)$. What are the boundary conditions for a European call?

??? success "Solution to Exercise 2"
    The PDE is

    $$
    \frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
    $$

    Boundary conditions for a European call:

    - Terminal: $V(S, T) = \max(S - K, 0)$
    - As $S \to 0$: $V(0, t) = 0$ (worthless)
    - As $S \to \infty$: $V(S, t) \sim S e^{-q(T-t)} - K e^{-r(T-t)}$ (deep in-the-money)

---

**Exercise 3.**
Explain why the base class stores the continuous dividend yield $q$ as a parameter. How does $q > 0$ modify the Black-Scholes formula?

??? success "Solution to Exercise 3"
    A continuous dividend yield $q$ reduces the effective growth rate of the stock under the risk-neutral measure from $r$ to $r - q$. In the BS formula, $S_0$ is replaced by $S_0 e^{-qT}$ (the present value of the stock excluding dividends):

    $$
    d_1 = \frac{\ln(S_0/K) + (r - q + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    $$
    C = S_0 e^{-qT}\mathcal{N}(d_1) - K e^{-rT}\mathcal{N}(d_2)
    $$

    When $q = 0$, the standard BS formula is recovered.

---

**Exercise 4.**
The base class uses inheritance: subclasses like `BlackScholesFormula` extend `BlackScholesBase`. What is the design advantage of this pattern?

??? success "Solution to Exercise 4"
    The inheritance pattern ensures that all Black-Scholes modules share the same parameter set and initialization logic. Advantages:

    1. **DRY (Don't Repeat Yourself)**: Parameters are defined once in the base class.
    2. **Consistency**: All subclasses automatically have `S0`, `K`, `T`, `r`, `sigma`, `q`.
    3. **Polymorphism**: Code can accept any `BlackScholesBase` subclass and access parameters uniformly.
    4. **Extensibility**: New pricing methods (e.g., tree-based, PDE-based) just extend the base class.

    The alternative (composition or standalone functions with parameter dictionaries) would require passing parameters to every function call.
