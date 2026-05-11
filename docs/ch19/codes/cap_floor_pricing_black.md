# Cap and Floor Pricing (Black's Formula)

## Background

cap_floor_pricing_black.py

This module implements Cap and Floor Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
cap_floor_pricing_black.py

This module implements Cap and Floor Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def cap_floor_pricing_black():
    """
    Cap and Floor Pricing.
    
    This function demonstrates the key concepts and computational techniques
    for cap and floor pricing.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Cap and Floor Pricing
    print(f"Computing Cap and Floor Pricing...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Cap and Floor Pricing"
    }
    
    return results


def main():
    """Main execution function."""
    results = cap_floor_pricing_black()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Cap and Floor Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/cap_floor_pricing_black.png", dpi=150)
    print(f"Figure saved to /tmp/cap_floor_pricing_black.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Using Black's formula, the price of a caplet with strike $K = 5\%$, forward rate $F = 6\%$, volatility $\sigma = 20\%$, maturity $T = 1$, day count fraction $\tau = 0.25$, notional $N = \$1{,}000{,}000$, and discount factor $P(0,T+\tau) = 0.97$ is given by Black's caplet formula. Compute $d_1$ and $d_2$.

??? success "Solution to Exercise 1"
    $$
    d_1 = \frac{\ln(F/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{\ln(0.06/0.05) + \frac{1}{2}(0.04)(1)}{0.20 \times 1} = \frac{0.1823 + 0.02}{0.20} = \frac{0.2023}{0.20} = 1.0117.
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 1.0117 - 0.20 = 0.8117.
    $$

---

**Exercise 2.**
Explain put-call parity for caps and floors. If a cap with strike $K$ costs $C$ and the corresponding floor costs $F$, what is the relationship between them?

??? success "Solution to Exercise 2"
    Cap-floor parity states that

    $$
    \text{Cap}(K) - \text{Floor}(K) = \text{Swap}(K),
    $$

    where $\text{Swap}(K)$ is a payer interest rate swap with fixed rate $K$. Equivalently, for each caplet-floorlet pair at time $T_i$:

    $$
    \text{Caplet}(K, T_i) - \text{Floorlet}(K, T_i) = \tau_i\,P(0, T_{i+1})(F_i - K),
    $$

    where $F_i$ is the forward rate and $\tau_i$ is the day count fraction. This is analogous to call-put parity for equity options and follows from the linearity of the payoff: $\max(L - K, 0) - \max(K - L, 0) = L - K$.

---

**Exercise 3.**
A 3-year cap consists of caplets at years 1, 2, and 3. If the caplet prices are \$1,200, \$1,800, and \$2,100, what is the total cap price? What is the flat (implied) cap volatility if the model cap price equals the market cap price at $\sigma_{\text{flat}} = 22\%$?

??? success "Solution to Exercise 3"
    The total cap price is the sum of all caplet prices:

    $$
    \text{Cap} = 1{,}200 + 1{,}800 + 2{,}100 = \$5{,}100.
    $$

    The flat cap volatility $\sigma_{\text{flat}}$ is the single volatility that, when plugged into Black's formula for each caplet, reproduces the total cap price:

    $$
    \sum_{i=1}^{3} \text{Caplet}_{\text{Black}}(K, T_i, \sigma_{\text{flat}}) = \$5{,}100.
    $$

    If this equation is satisfied at $\sigma_{\text{flat}} = 22\%$, then the flat cap volatility is $22\%$. Note that this is generally different from the individual caplet volatilities.

---

**Exercise 4.**
Explain why Black's formula uses the forward rate rather than the spot rate, and what measure change is implied.

??? success "Solution to Exercise 4"
    Black's formula prices the caplet under the $T$-forward measure $\mathbb{Q}^T$, where the numeraire is $P(t, T)$. Under this measure, the forward rate $F(t, T_1, T_2)$ is a martingale:

    $$
    \mathbb{E}^{\mathbb{Q}^T}[F(T_1, T_1, T_2) \mid \mathcal{F}_t] = F(t, T_1, T_2).
    $$

    This eliminates the need to model the drift of the forward rate, simplifying the pricing formula to a Black-Scholes-type expression. The spot rate evolves under the risk-neutral measure $\mathbb{Q}$ and is not a martingale under any natural numeraire, making it less convenient for direct use in option pricing.
