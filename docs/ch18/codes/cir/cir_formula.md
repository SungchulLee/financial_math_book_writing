# Cir Formula

## Background

Cir Formula

Educational script demonstrating cir formula concepts.

---

## Code

```python
"""
Cir Formula

Educational script demonstrating cir formula concepts.
"""

# ============================================================================
# cir/cir_formula.py
# ============================================================================
import numpy as np
from .cir_base import CIRParameters, CIRNumericalError


class CIRAnalytical:
    """Analytical formulas for CIR model."""
    
    @staticmethod
    def mean(params: CIRParameters, t: float) -> float:
        """Analytical mean of CIR process at time t."""
        if t <= 0:
            return params.r0
        return params.theta + (params.r0 - params.theta) * np.exp(-params.kappa * t)
    
    @staticmethod
    def variance(params: CIRParameters, t: float) -> float:
        """Analytical variance of CIR process at time t."""
        if t <= 0:
            return 0.0
            
        exp_kt = np.exp(-params.kappa * t)
        exp_2kt = np.exp(-2 * params.kappa * t)
        
        term1 = (params.r0 * params.sigma**2 / params.kappa) * (exp_kt - exp_2kt)
        term2 = (params.theta * params.sigma**2 / (2 * params.kappa)) * (1 - exp_kt)**2
        
        return term1 + term2
    
    @staticmethod
    def standard_deviation(params: CIRParameters, t: float) -> float:
        """Analytical standard deviation at time t."""
        return np.sqrt(CIRAnalytical.variance(params, t))


class CIRBondPricer:
    """Bond pricing utilities for CIR model."""
    
    @staticmethod
    def zero_coupon_bond_price(
        params: CIRParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """
        Calculate analytical zero-coupon bond price using CIR formula.
        
        P(r,t,T) = A(t,T) * exp(-B(t,T) * r)
        """
        if time_to_maturity <= 0:
            return 1.0
        
        if current_rate < 0:
            raise CIRNumericalError("Current rate cannot be negative")
        
        try:
            # Calculate helper variables
            gamma = np.sqrt(params.kappa**2 + 2 * params.sigma**2)
            exp_gamma_T = np.exp(gamma * time_to_maturity)
            
            # B(t,T) coefficient
            numerator = 2 * (exp_gamma_T - 1)
            denominator = (gamma + params.kappa) * (exp_gamma_T - 1) + 2 * gamma
            B_T = numerator / denominator
            
            # A(t,T) coefficient (using log for numerical stability)
            nu = 2 * params.kappa * params.theta / (params.sigma**2)
            
            A_numerator = 2 * gamma * np.exp((params.kappa + gamma) * time_to_maturity / 2)
            A_denominator = denominator  # Same as B_T denominator
            
            log_A_T = nu * (np.log(A_numerator) - np.log(A_denominator))
            
            # Bond price calculation
            log_bond_price = log_A_T - B_T * current_rate
            bond_price = np.exp(log_bond_price)
            
            # Ensure reasonable bounds
            return float(np.clip(bond_price, 1e-10, 1.0))
            
        except (OverflowError, ZeroDivisionError, ValueError) as e:
            raise CIRNumericalError(f"Bond pricing computation failed: {e}")
    
    @staticmethod
    def yield_to_maturity(
        params: CIRParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """Calculate yield to maturity from bond price."""
        if time_to_maturity <= 0:
            return current_rate
        
        bond_price = CIRBondPricer.zero_coupon_bond_price(
            params, current_rate, time_to_maturity
        )
        return -np.log(bond_price) / time_to_maturity
    
    @staticmethod
    def yield_curve(
        params: CIRParameters,
        current_rate: float,
        maturities: np.ndarray
    ) -> np.ndarray:
        """Calculate yield curve for given maturities."""
        yields = np.zeros_like(maturities)
        
        for i, T in enumerate(maturities):
            yields[i] = CIRBondPricer.yield_to_maturity(params, current_rate, T)
        
        return yields
    
    @staticmethod
    def forward_rate(
        params: CIRParameters,
        current_rate: float,
        t1: float,
        t2: float
    ) -> float:
        """Calculate forward rate between times t1 and t2."""
        if t1 >= t2:
            raise ValueError("t1 must be less than t2")
        
        P_t1 = CIRBondPricer.zero_coupon_bond_price(params, current_rate, t1)
        P_t2 = CIRBondPricer.zero_coupon_bond_price(params, current_rate, t2)
        
        return np.log(P_t1 / P_t2) / (t2 - t1)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Using the CIR analytical mean formula, compute $\mathbb{E}[r(5)]$ given $r_0 = 0.03$, $\theta = 0.06$, and $\kappa = 0.2$.

??? success "Solution to Exercise 1"
    The analytical mean of the CIR process at time $t$ is

    $$
    \mathbb{E}[r(t)] = \theta + (r_0 - \theta)\,e^{-\kappa t}.
    $$

    Substituting the given values with $t = 5$:

    $$
    \mathbb{E}[r(5)] = 0.06 + (0.03 - 0.06)\,e^{-0.2 \times 5} = 0.06 - 0.03\,e^{-1}.
    $$

    Since $e^{-1} \approx 0.3679$:

    $$
    \mathbb{E}[r(5)] \approx 0.06 - 0.03 \times 0.3679 = 0.06 - 0.01104 = 0.04896.
    $$

---

**Exercise 2.**
Derive the formula for $B(t,T)$ in the CIR zero-coupon bond pricing formula $P(r,t,T) = A(t,T)\,e^{-B(t,T)\,r}$. Write the expression in terms of $\kappa$, $\sigma$, and $\tau = T - t$.

??? success "Solution to Exercise 2"
    Define the auxiliary quantity $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. The $B$ coefficient for the CIR bond pricing formula is

    $$
    B(\tau) = \frac{2\bigl(e^{\gamma \tau} - 1\bigr)}{(\gamma + \kappa)(e^{\gamma \tau} - 1) + 2\gamma},
    $$

    where $\tau = T - t$ is the time to maturity. As $\tau \to 0$, $B(\tau) \to 0$ and $P \to 1$, consistent with a maturing bond. As $\tau \to \infty$, $B(\tau) \to 2 / (\gamma + \kappa)$, reflecting the long-term sensitivity of bond prices to the short rate.

---

**Exercise 3.**
Consider CIR parameters $r_0 = 0.04$, $\theta = 0.05$, $\kappa = 0.15$, $\sigma = 0.04$. Compute the yield to maturity for a 10-year zero-coupon bond, given $P(r_0, 0, 10) = 0.6703$.

??? success "Solution to Exercise 3"
    The yield to maturity is defined as

    $$
    y(0, T) = -\frac{\ln P(r_0, 0, T)}{T}.
    $$

    Substituting $P = 0.6703$ and $T = 10$:

    $$
    y(0, 10) = -\frac{\ln(0.6703)}{10} = -\frac{-0.3996}{10} = 0.03996 \approx 4.00\%.
    $$

---

**Exercise 4.**
Explain how the forward rate $f(0, t_1, t_2)$ is computed from two CIR bond prices $P(r_0, 0, t_1)$ and $P(r_0, 0, t_2)$. If $P(r_0, 0, 2) = 0.9200$ and $P(r_0, 0, 5) = 0.8100$, compute $f(0, 2, 5)$.

??? success "Solution to Exercise 4"
    The forward rate between times $t_1$ and $t_2$ is

    $$
    f(0, t_1, t_2) = \frac{\ln P(r_0, 0, t_1) - \ln P(r_0, 0, t_2)}{t_2 - t_1}.
    $$

    Substituting the given values:

    $$
    f(0, 2, 5) = \frac{\ln(0.9200) - \ln(0.8100)}{5 - 2} = \frac{-0.08338 - (-0.21072)}{3} = \frac{0.12734}{3} \approx 0.04245.
    $$

    The forward rate is approximately $4.24\%$.
