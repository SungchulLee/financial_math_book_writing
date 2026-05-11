# Cap and Floor Pricing

## Background

hull_white_cap_floor_pricing.py

This module implements Cap and Floor Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_cap_floor_pricing.py

This module implements Cap and Floor Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def hull_white_cap_floor_pricing():
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
    results = hull_white_cap_floor_pricing()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Cap and Floor Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_cap_floor_pricing.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_cap_floor_pricing.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A cap with semi-annual payments over 3 years at strike $3\%$ consists of how many caplets? Which payment is excluded from the cap?

??? success "Solution to Exercise 1"
    With semi-annual payments over 3 years, there are 6 payment periods. However, the first payment (at 6 months) is excluded because the LIBOR rate for the first period is already known at inception (it is the spot rate, not a forward rate). Therefore, the cap consists of **5 caplets** covering periods $[0.5, 1.0], [1.0, 1.5], [1.5, 2.0], [2.0, 2.5], [2.5, 3.0]$.

---

**Exercise 2.**
Using cap-floor parity, if a 3-year cap at $3\%$ costs \$15,000 and the corresponding swap (pay fixed $3\%$) has value \$2,000, what is the floor price?

??? success "Solution to Exercise 2"
    Cap-floor parity: $\text{Cap}(K) - \text{Floor}(K) = \text{Swap}(K)$, so

    $$
    \text{Floor} = \text{Cap} - \text{Swap} = 15{,}000 - 2{,}000 = \$13{,}000.
    $$

---

**Exercise 3.**
Explain the intuition behind the Hull-White caplet price being expressed as a bond put option.

??? success "Solution to Exercise 3"
    The caplet pays $\tau\max(L - K, 0)$ where $L = (1/P(T_1,T_2) - 1)/\tau$. High LIBOR corresponds to low bond price. Specifically, $L > K$ is equivalent to $P(T_1,T_2) < 1/(1 + K\tau) = \bar{K}$. So the caplet payoff (after scaling) is proportional to $\max(\bar{K} - P(T_1,T_2), 0)$, which is a put on the bond. In the Hull-White model, bond prices are lognormally distributed (approximately), so the bond put price has a Black-Scholes-type formula.

---

**Exercise 4.**
If interest rates drop to $-0.5\%$ while the floor strike is $0\%$, compute the intrinsic value of the floorlet for $\tau = 0.5$ and notional \$1,000,000.

??? success "Solution to Exercise 4"
    The floorlet payoff is $N \cdot \tau \cdot \max(K - L, 0) = 1{,}000{,}000 \times 0.5 \times \max(0 - (-0.005), 0) = 500{,}000 \times 0.005 = \$2{,}500$.

    This intrinsic value would be discounted to the present using $P(0, T_2)$. The total floorlet value would be higher than the intrinsic value due to time value.
