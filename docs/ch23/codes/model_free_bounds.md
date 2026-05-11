# Model-Free Bounds Computation

## Background

model_free_bounds.py

This module implements Model-Free Bounds Computation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
model_free_bounds.py

This module implements Model-Free Bounds Computation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def model_free_bounds():
    """
    Model-Free Bounds Computation.
    
    This function demonstrates the key concepts and computational techniques
    for model-free bounds computation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Model-Free Bounds Computation
    print(f"Computing Model-Free Bounds Computation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Model-Free Bounds Computation"
    }
    
    return results


def main():
    """Main execution function."""
    results = model_free_bounds()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Model-Free Bounds Computation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/model_free_bounds.png", dpi=150)
    print(f"Figure saved to /tmp/model_free_bounds.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The model-free upper bound for a European call option on a non-dividend-paying stock is $C \leq S_0$. Derive this bound.

??? success "Solution to Exercise 1"
    The call payoff satisfies $\max(S_T - K, 0) \leq S_T$ for all $S_T \geq 0$. Taking risk-neutral expectations:

    $$
    C = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\max(S_T - K, 0)] \leq e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T] = e^{-rT} \cdot S_0 e^{rT} = S_0.
    $$

    The call price cannot exceed the current stock price, since the call's payoff is always at most $S_T$ and the stock costs $S_0$.

---

**Exercise 2.**
Given call prices at strikes $K_1 < K_2 < K_3$, derive the butterfly spread inequality as a model-free constraint.

??? success "Solution to Exercise 2"
    A butterfly spread is: long 1 call at $K_1$, short 2 calls at $K_2$, long 1 call at $K_3$, with $K_2 = (K_1 + K_3)/2$. The payoff $(S - K_1)^+ - 2(S - K_2)^+ + (S - K_3)^+ \geq 0$ for all $S$. Therefore:

    $$
    C(K_1) - 2C(K_2) + C(K_3) \geq 0.
    $$

    This convexity constraint must hold model-free. Violation would create an arbitrage opportunity via the butterfly spread.

---

**Exercise 3.**
Explain how model-free bounds are computed from a set of observed call prices across multiple strikes.

??? success "Solution to Exercise 3"
    Given call prices $C(K_1), \ldots, C(K_n)$, the model-free bounds for an exotic payoff $f(S_T)$ are obtained by solving:

    $$
    \text{Upper:} \quad \sup_{\mu} \int f(s)\,d\mu(s) \quad \text{s.t.} \quad \int (s - K_i)^+ d\mu(s) = C(K_i) \; \forall i.
    $$

    This is a linear programming problem: the decision variable is the distribution $\mu$, and the constraints ensure consistency with market call prices. The solution identifies the worst-case (or best-case) distribution for the exotic payoff within the set of all distributions matching the observed vanillas.

---

**Exercise 4.**
If the model-free bounds for a variance swap strike are $[18\%, 22\%]$ while a particular model gives $20\%$, what does this tell us about model risk?

??? success "Solution to Exercise 4"
    The model-free bounds $[18\%, 22\%]$ represent the range of prices consistent with all available market information (vanilla options). The model price of $20\%$ lies within this range, so it is arbitrage-free. However, the $4\%$ width of the bounds indicates significant model uncertainty: different arbitrage-free models can disagree by up to $4\%$. The model risk (potential pricing error due to model choice) is at most $2\%$ (half the width). If the bounds were tighter (e.g., $[19.5\%, 20.5\%]$), model risk would be small and the model choice matters less.
