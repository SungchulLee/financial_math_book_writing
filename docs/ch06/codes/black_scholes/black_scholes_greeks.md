# Black Scholes Greeks

## Background

Greeks calculation (Delta, Gamma, Theta, etc.)
UNCHANGED API - improved internal implementation using utility functions.

---

## Code

```python
# ============================================================================
# black_scholes/black_scholes_greeks.py
# ============================================================================
"""
Greeks calculation (Delta, Gamma, Theta, etc.)
UNCHANGED API - improved internal implementation using utility functions.
"""

from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import delta, gamma, vega, theta, rho

class BlackScholesGreeks(BlackScholesBase):
    """
    Greeks calculation for Black-Scholes options.
    API UNCHANGED - now delegates to utility functions.
    """
    
    def delta(self):
        """
        Calculate delta for call and put options.
        UNCHANGED API - now delegates to utility function.
        """
        return delta(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def gamma(self):
        """
        Calculate gamma (same for calls and puts).
        UNCHANGED API - now delegates to utility function.
        """
        return gamma(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def vega(self):
        """
        Calculate vega (same for calls and puts).
        UNCHANGED API - now delegates to utility function.
        """
        return vega(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def theta(self):
        """
        Calculate theta for call and put options.
        UNCHANGED API - now delegates to utility function.
        """
        return theta(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def rho(self):
        """
        Calculate rho for call and put options.
        UNCHANGED API - now delegates to utility function.
        """
        return rho(self.S0, self.K, self.T, self.r, self.sigma, self.q)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Define delta ($\Delta$) for a European call and put. Compute $\Delta_{\text{call}}$ for $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$, $q = 0$.

??? success "Solution to Exercise 1"
    Delta is $\Delta_{\text{call}} = e^{-qT}\mathcal{N}(d_1)$ and $\Delta_{\text{put}} = -e^{-qT}\mathcal{N}(-d_1)$.

    With $q = 0$: $d_1 = (0 + 0.07)/0.20 = 0.35$, so $\Phi(0.35) \approx 0.6368$.

    $$
    \Delta_{\text{call}} = 0.6368, \quad \Delta_{\text{put}} = -(1 - 0.6368) = -0.3632
    $$

    The call delta of 0.64 means the option price increases by approximately $\$0.64$ for each $\$1$ increase in the stock price.

---

**Exercise 2.**
Show that gamma ($\Gamma$) is the same for calls and puts. Derive the formula $\Gamma = \frac{e^{-qT}\phi(d_1)}{S_0\sigma\sqrt{T}}$ where $\phi$ is the standard normal PDF.

??? success "Solution to Exercise 2"
    Since $\Delta_{\text{call}} - \Delta_{\text{put}} = e^{-qT}$ (a constant), their derivatives with respect to $S$ are equal:

    $$
    \Gamma = \frac{\partial \Delta_{\text{call}}}{\partial S} = \frac{\partial \Delta_{\text{put}}}{\partial S}
    $$

    Computing: $\Gamma = e^{-qT}\phi(d_1)\frac{\partial d_1}{\partial S}$. Since $\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{T}}$:

    $$
    \Gamma = \frac{e^{-qT}\phi(d_1)}{S_0\sigma\sqrt{T}}
    $$

    Gamma is always positive, peaking when the option is at-the-money.

---

**Exercise 3.**
Explain the financial interpretation of vega ($\nu$). Why is vega not a Greek letter, and why is it important for traders?

??? success "Solution to Exercise 3"
    Vega measures the sensitivity of the option price to changes in implied volatility: $\nu = \partial V / \partial \sigma$. The formula is $\nu = S_0 e^{-qT}\phi(d_1)\sqrt{T}$.

    Vega is not a Greek letter (it comes from the star Vega), but it is included among the "Greeks" by convention. It is crucial for traders because:

    1. Volatility is the only BS parameter not directly observable -- it must be estimated or implied.
    2. Changes in implied volatility can move option prices substantially.
    3. Volatility trading strategies (straddles, strangles) are designed to profit from vega exposure.
    4. Vega hedging is essential for market makers to manage their volatility risk.

---

**Exercise 4.**
Theta ($\Theta$) measures time decay. Explain why theta is typically negative for long option positions and derive the relationship $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma + (r-q)S\Delta = rV$.

??? success "Solution to Exercise 4"
    This relationship comes directly from the Black-Scholes PDE: $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r-q)S\frac{\partial V}{\partial S} = rV$. Identifying the partial derivatives as Greeks: $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma + (r-q)S\Delta = rV$.

    Theta is typically negative because options lose value as expiration approaches (time value erodes). This is because the probability of a large favorable move decreases with less time remaining. The equation shows that theta is the "cost" of carrying the gamma and delta exposure -- it balances the portfolio's risk-neutral return.
