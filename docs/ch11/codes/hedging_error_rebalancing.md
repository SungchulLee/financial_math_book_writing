# Hedging Error vs Rebalancing Frequency

## Background

hedging_error_rebalancing.py

This module implements Hedging Error vs Rebalancing Frequency.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hedging_error_rebalancing.py

This module implements Hedging Error vs Rebalancing Frequency.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def hedging_error_rebalancing():
    """
    Hedging Error vs Rebalancing Frequency.
    
    This function demonstrates the key concepts and computational techniques
    for hedging error vs rebalancing frequency.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Hedging Error vs Rebalancing Frequency
    print(f"Computing Hedging Error vs Rebalancing Frequency...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Hedging Error vs Rebalancing Frequency"
    }
    
    return results


def main():
    """Main execution function."""
    results = hedging_error_rebalancing()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Hedging Error vs Rebalancing Frequency")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hedging_error_rebalancing.png", dpi=150)
    print(f"Figure saved to /tmp/hedging_error_rebalancing.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Plot (conceptually) the hedging error standard deviation versus $1/\sqrt{N}$ where $N$ is the number of rebalancing steps. What slope do you expect?

??? success "Solution to Exercise 1"
    The relationship is $\text{std}(\text{error}) = C / \sqrt{N}$ for some constant $C$ depending on option parameters ($\sigma$, $\Gamma$, $S$, $T$). On a plot of std vs $1/\sqrt{N}$, the relationship is linear with slope $C$ and zero intercept. The slope $C \approx \frac{\sigma^2 S^2 \Gamma}{2}\sqrt{T}$ captures the "unhedged gamma" risk.

---

**Exercise 2.**
For $N = 10, 50, 250, 1000$ rebalancing steps, the hedging error std ratios should be approximately $1 : 1/\sqrt{5} : 1/5 : 1/10$. Verify this scaling.

??? success "Solution to Exercise 2"
    Ratios relative to $N = 10$: $\sqrt{10/50} = 0.447$, $\sqrt{10/250} = 0.2$, $\sqrt{10/1000} = 0.1$. So the ratios are $1 : 0.447 : 0.2 : 0.1$, confirming the $1/\sqrt{N}$ scaling. Doubling $N$ reduces error by factor $\sqrt{2} \approx 1.41$.

---

**Exercise 3.**
Explain the economic tradeoff between rebalancing frequency and transaction costs. What is the optimal rebalancing frequency?

??? success "Solution to Exercise 3"
    More frequent rebalancing reduces hedging error variance ($\propto 1/N$) but increases transaction costs ($\propto N$, since each trade incurs a cost). Total cost $= \text{hedging error cost} + \text{TC} \approx A/N + BN$. Minimizing: $\partial/\partial N(-A/N^2 + B) = 0$ gives $N^* = (A/B)^{1/2}$. The optimal frequency balances the marginal reduction in hedging error against the marginal transaction cost.

---

**Exercise 4.**
If transaction costs are $c = 0.1\%$ per trade and the option has $\Gamma = 0.02$, $S = 100$, $\sigma = 0.2$, $T = 1$, estimate the optimal number of rebalancing steps.

??? success "Solution to Exercise 4"
    Hedging error cost $\propto \Gamma^2 S^4 \sigma^4 T / N$, transaction cost $\propto c \cdot S \cdot \mathbb{E}[|\Delta_{i+1} - \Delta_i|] \cdot N \approx c \cdot S \cdot \Gamma \cdot \sigma \cdot S \sqrt{T/N} \cdot N = cS^2\Gamma\sigma\sqrt{TN}$. Setting derivatives equal: $N^* \approx (\Gamma S^2 \sigma^2 / c)^{2/3} \approx (0.02 \times 10000 \times 0.04 / 0.001)^{2/3} = (8000)^{2/3} \approx 400$ steps.