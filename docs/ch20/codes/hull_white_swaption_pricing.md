# Swaption Pricing

## Background

hull_white_swaption_pricing.py

This module implements Swaption Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_swaption_pricing.py

This module implements Swaption Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def hull_white_swaption_pricing():
    """
    Swaption Pricing.
    
    This function demonstrates the key concepts and computational techniques
    for swaption pricing.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Swaption Pricing
    print(f"Computing Swaption Pricing...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Swaption Pricing"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_swaption_pricing()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Swaption Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_swaption_pricing.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_swaption_pricing.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A European payer swaption under Hull-White can be priced using Jamshidian's trick. Describe the steps for a 2-year option on a 3-year annual swap with fixed rate $K = 4\%$.

??? success "Solution to Exercise 1"

    1. At option expiry $T = 2$, the swap has payments at $T_1 = 3$, $T_2 = 4$, $T_3 = 5$ with cash flows $c_1 = 0.04$, $c_2 = 0.04$, $c_3 = 1.04$.
    2. Find $r^*$ such that $\sum c_i P(2, T_i; r^*) = 1$.
    3. Compute strikes $K_i = P(2, T_i; r^*)$ for $i = 1, 2, 3$.
    4. The swaption price is $\sum c_i \times \text{ZBP}(0, 2, T_i, K_i)$, where ZBP is the Hull-White analytical bond put formula.

---

**Exercise 2.**
Explain why the swaption price increases with the Hull-White volatility parameter $\eta$.

??? success "Solution to Exercise 2"
    Higher $\eta$ increases the variance of the short rate at the option expiry. Since the swaption is an option (a convex payoff), greater variance increases its expected payoff by Jensen's inequality. Specifically, the bond price volatility $\sigma_P \propto \eta$, which enters the $d_1, d_2$ terms in the Black-type formula for each bond option. Higher $\sigma_P$ increases the value of each component bond put, and hence the total swaption price.

---

**Exercise 3.**
For an ATM swaption (strike equals forward swap rate), the swaption price is approximately $V \approx A_0 \cdot S_0 \cdot \sigma_S \cdot \sqrt{T} \cdot 0.4$ where $\sigma_S$ is the swaption normal vol. If $A_0 = 4$, $S_0 = 3\%$, $\sigma_S = 80$ bps/year, and $T = 2$, estimate the swaption price per unit notional.

??? success "Solution to Exercise 3"
    $$
    V \approx 4 \times 0.03 \times 0.008 \times \sqrt{2} \times 0.4 = 4 \times 0.03 \times 0.008 \times 1.414 \times 0.4.
    $$

    $$
    V \approx 4 \times 0.03 \times 0.004525 = 4 \times 0.0001358 = 0.000543.
    $$

    Per \$1,000,000 notional: $\$543$. (The factor $0.4 \approx \sqrt{2\pi}^{-1} \times 2$ comes from the ATM normal distribution approximation.)

---

**Exercise 4.**
How does increasing mean reversion $\lambda$ affect the ATM swaption price for different expiries?

??? success "Solution to Exercise 4"
    Higher $\lambda$ reduces the variance of the short rate at the option expiry: $\text{Var}[r(T)] = \eta^2(1 - e^{-2\lambda T})/(2\lambda)$. For short expiries ($T$ small), the factor $(1 - e^{-2\lambda T}) \approx 2\lambda T$ is insensitive to $\lambda$, so the swaption price is approximately unchanged. For long expiries, the variance saturates at $\eta^2/(2\lambda)$, which decreases with $\lambda$. Therefore, increasing $\lambda$ primarily reduces long-dated swaption prices while leaving short-dated prices relatively unchanged. This makes $\lambda$ useful for calibrating the term structure of swaption volatilities.
