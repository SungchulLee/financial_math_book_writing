# Vasicek Formula

## Background

Vasicek Formula

Educational script demonstrating vasicek formula concepts.

---

## Code

```python
"""
Vasicek Formula

Educational script demonstrating vasicek formula concepts.
"""

# ============================================================================
# vasicek/vasicek_formula.py
# ============================================================================
import numpy as np
from .vasicek_base import VasicekParameters, VasicekNumericalError


class VasicekAnalytical:
    """Analytical formulas for Vasicek model."""
    
    @staticmethod
    def mean(params: VasicekParameters, t: float) -> float:
        """Analytical mean of Vasicek process at time t."""
        if t <= 0:
            return params.r0
        return params.b + (params.r0 - params.b) * np.exp(-params.a * t)
    
    @staticmethod
    def variance(params: VasicekParameters, t: float) -> float:
        """Analytical variance of Vasicek process at time t."""
        if t <= 0:
            return 0.0
        return (params.sigma**2 / (2 * params.a)) * (1 - np.exp(-2 * params.a * t))
    
    @staticmethod
    def standard_deviation(params: VasicekParameters, t: float) -> float:
        """Analytical standard deviation at time t."""
        return np.sqrt(VasicekAnalytical.variance(params, t))


class VasicekBondPricer:
    """Bond pricing utilities for Vasicek model."""
    
    @staticmethod
    def zero_coupon_bond_price(
        params: VasicekParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """
        Calculate analytical zero-coupon bond price using Vasicek formula.
        
        P(r,t,T) = A(t,T) * exp(-B(t,T) * r)
        """
        if time_to_maturity <= 0:
            return 1.0
        
        try:
            # B(t,T) coefficient
            if params.a == 0:
                B_T = time_to_maturity
            else:
                B_T = (1 - np.exp(-params.a * time_to_maturity)) / params.a
            
            # A(t,T) coefficient
            if params.a == 0:
                A_T = np.exp(-params.b * time_to_maturity + 
                            (params.sigma**2 * time_to_maturity**3) / 6)
            else:
                term1 = (params.b - params.sigma**2 / (2 * params.a**2)) * (B_T - time_to_maturity)
                term2 = (params.sigma**2 / (4 * params.a)) * B_T**2
                A_T = np.exp(term1 - term2)
            
            # Bond price
            bond_price = A_T * np.exp(-B_T * current_rate)
            
            return float(np.clip(bond_price, 1e-10, 1.0))
            
        except (OverflowError, ZeroDivisionError, ValueError) as e:
            raise VasicekNumericalError(f"Bond pricing computation failed: {e}")
    
    @staticmethod
    def yield_to_maturity(
        params: VasicekParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """Calculate yield to maturity from bond price."""
        if time_to_maturity <= 0:
            return current_rate
        
        bond_price = VasicekBondPricer.zero_coupon_bond_price(
            params, current_rate, time_to_maturity
        )
        return -np.log(bond_price) / time_to_maturity
    
    @staticmethod
    def yield_curve(
        params: VasicekParameters,
        current_rate: float,
        maturities: np.ndarray
    ) -> np.ndarray:
        """Calculate yield curve for given maturities."""
        yields = np.zeros_like(maturities)
        
        for i, T in enumerate(maturities):
            yields[i] = VasicekBondPricer.yield_to_maturity(params, current_rate, T)
        
        return yields
    
    @staticmethod
    def forward_rate(
        params: VasicekParameters,
        current_rate: float,
        t1: float,
        t2: float
    ) -> float:
        """Calculate forward rate between times t1 and t2."""
        if t1 >= t2:
            raise ValueError("t1 must be less than t2")
        
        P_t1 = VasicekBondPricer.zero_coupon_bond_price(params, current_rate, t1)
        P_t2 = VasicekBondPricer.zero_coupon_bond_price(params, current_rate, t2)
        
        return np.log(P_t1 / P_t2) / (t2 - t1)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Using the Vasicek analytical formulas, compute the mean and variance of $r(10)$ given $r_0 = 0.03$, $b = 0.05$, $a = 0.1$, and $\sigma = 0.02$.

??? success "Solution to Exercise 1"
    The mean is

    $$
    \mathbb{E}[r(10)] = b + (r_0 - b)e^{-aT} = 0.05 + (0.03 - 0.05)e^{-1} = 0.05 - 0.02 \times 0.3679 \approx 0.04264.
    $$

    The variance is

    $$
    \text{Var}[r(10)] = \frac{\sigma^2}{2a}(1 - e^{-2aT}) = \frac{0.0004}{0.2}(1 - e^{-2}) = 0.002 \times 0.8647 \approx 0.001729.
    $$

    The standard deviation is $\sqrt{0.001729} \approx 0.04158$.

---

**Exercise 2.**
Derive the $B(t,T)$ coefficient for the Vasicek bond pricing formula $P = A \cdot e^{-B \cdot r}$ and explain why $B(t,T) \to T - t$ as $a \to 0$.

??? success "Solution to Exercise 2"
    For the Vasicek model, solving the Riccati equation yields

    $$
    B(\tau) = \frac{1 - e^{-a\tau}}{a}, \quad \tau = T - t.
    $$

    As $a \to 0$, applying L'Hopital's rule or the Taylor expansion $e^{-a\tau} \approx 1 - a\tau$:

    $$
    B(\tau) = \frac{1 - (1 - a\tau + O(a^2))}{a} = \tau + O(a).
    $$

    So $B \to \tau = T - t$, recovering the Ho-Lee limit. Economically, when there is no mean reversion ($a = 0$), a unit change in the short rate has a duration effect equal to the full time to maturity.

---

**Exercise 3.**
Compute the Vasicek yield curve for maturities $T \in \{1, 5, 10, 30\}$ given $r = 0.03$, $b = 0.05$, $a = 0.1$, $\sigma = 0.02$. Is the curve upward-sloping?

??? success "Solution to Exercise 3"
    Using $y(T) = -\ln P(r,0,T)/T$, we need $B(T)$ and $\ln A(T)$ for each maturity. With $B(T) = (1 - e^{-0.1T})/0.1$:

    - $T = 1$: $B = 0.9516$, the yield is approximately $3.05\%$
    - $T = 5$: $B = 3.935$, the yield is approximately $3.38\%$
    - $T = 10$: $B = 6.321$, the yield is approximately $3.68\%$
    - $T = 30$: $B = 9.502$, the yield is approximately $4.08\%$

    The curve is upward-sloping, rising from $3.05\%$ at the short end toward $4.08\%$ at the long end. This reflects $r_0 < b$: the market expects rates to rise toward the long-term mean.

---

**Exercise 4.**
Compute the forward rate $f(0, 5, 10)$ if $P(0,5) = 0.8450$ and $P(0,10) = 0.6900$.

??? success "Solution to Exercise 4"
    The forward rate is

    $$
    f(0, 5, 10) = \frac{\ln P(0,5) - \ln P(0,10)}{10 - 5} = \frac{\ln(0.8450) - \ln(0.6900)}{5}.
    $$

    Computing:

    $$
    f = \frac{-0.16839 - (-0.37106)}{5} = \frac{0.20267}{5} = 0.04053.
    $$

    The 5-year forward rate starting in 5 years is approximately $4.05\%$.
