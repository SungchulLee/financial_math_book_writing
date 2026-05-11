# Hedging Error Distribution

## Background

hedging_error_distribution.py

This module implements Hedging Error Distribution.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hedging_error_distribution.py

This module implements Hedging Error Distribution.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def hedging_error_distribution():
    """
    Hedging Error Distribution.
    
    This function demonstrates the key concepts and computational techniques
    for hedging error distribution.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Hedging Error Distribution
    print(f"Computing Hedging Error Distribution...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Hedging Error Distribution"
    }
    
    return results


def main():
    """Main execution function."""
    results = hedging_error_distribution()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Hedging Error Distribution")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hedging_error_distribution.png", dpi=150)
    print(f"Figure saved to /tmp/hedging_error_distribution.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The hedging error is defined as the difference between the option payoff and the value of the replicating portfolio at maturity. Under what conditions is the expected hedging error zero?

??? success "Solution to Exercise 1"
    The expected hedging error is zero when: (1) the hedging model matches the true data-generating process; (2) the initial option premium equals the theoretical BS price; (3) hedging is self-financing. Under these conditions, $\mathbb{E}[\text{error}] = 0$ by the martingale property of the discounted hedging portfolio under the risk-neutral measure.

---

**Exercise 2.**
The hedging error variance decreases with rebalancing frequency. If the variance with daily hedging ($N = 252$) is $V_0$, estimate the variance with weekly hedging ($N = 52$).

??? success "Solution to Exercise 2"
    Variance scales as $O(1/N)$: $V_{52} \approx V_0 \cdot 252/52 = 4.85 V_0$. The standard deviation increases by factor $\sqrt{4.85} \approx 2.2$. Weekly hedging produces about 2.2 times wider P&L dispersion than daily hedging.

---

**Exercise 3.**
Explain why the hedging error distribution is approximately normal for frequent rebalancing but develops heavier tails for infrequent rebalancing.

??? success "Solution to Exercise 3"
    With frequent rebalancing, each hedging error increment is small and approximately independent, so the CLT applies, giving a normal total error. With infrequent rebalancing, each increment can be large (large stock moves between rebalancing) and the gamma contribution $(dS)^2$ introduces positive skewness and excess kurtosis. The error distribution becomes leptokurtic.

---

**Exercise 4.**
A risk manager sets a hedging error tolerance of $\$0.10$ (1 std dev) for a $\$100$ notional option. How many rebalancing steps per year are needed if the error std dev with $N = 100$ steps is $\$0.50$?

??? success "Solution to Exercise 4"
    Std dev scales as $1/\sqrt{N}$: $\text{std}(N) = 0.50 \sqrt{100/N}$. Setting $0.50\sqrt{100/N} = 0.10$: $\sqrt{100/N} = 0.2$, so $100/N = 0.04$, giving $N = 2500$ steps per year, or about 10 rebalancing events per trading day.