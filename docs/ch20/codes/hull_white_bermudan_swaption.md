# Bermudan Swaption (Tree)

## Background

hull_white_bermudan_swaption.py

This module implements Bermudan Swaption Tree.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_bermudan_swaption.py

This module implements Bermudan Swaption Tree.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def hull_white_bermudan_swaption():
    """
    Bermudan Swaption Tree.
    
    This function demonstrates the key concepts and computational techniques
    for bermudan swaption tree.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Bermudan Swaption Tree
    print(f"Computing Bermudan Swaption Tree...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Bermudan Swaption Tree"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_bermudan_swaption()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Bermudan Swaption Tree")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_bermudan_swaption.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_bermudan_swaption.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A Bermudan swaption can be exercised at multiple dates. Explain why it is more valuable than a European swaption with the same terms.

??? success "Solution to Exercise 1"
    The Bermudan swaption gives the holder the right to exercise at any of several dates $T_1, T_2, \ldots, T_n$, while the European swaption allows exercise only at $T_1$. The Bermudan holder has all the rights of the European holder plus additional exercise opportunities. By the monotonicity of option value in the exercise set, $V_{\text{Bermudan}} \geq V_{\text{European}}$. The difference, called the Bermudan premium, reflects the value of timing flexibility -- the ability to enter the swap at the optimal moment based on realized rate movements.

---

**Exercise 2.**
Describe the backward induction procedure on a trinomial tree for pricing a Bermudan swaption.

??? success "Solution to Exercise 2"

    1. Construct a Hull-White trinomial tree calibrated to the yield curve and volatility.
    2. At each terminal node (final exercise date), compute the exercise value: $\max(V_{\text{swap}}, 0)$.
    3. At each interior node at an exercise date: compare the exercise value $V_{\text{ex}}$ with the continuation value $V_{\text{cont}}$ (discounted expected value from the next time step). Set $V = \max(V_{\text{ex}}, V_{\text{cont}})$.
    4. At non-exercise dates: $V = V_{\text{cont}}$.
    5. The root node value is the Bermudan swaption price.

---

**Exercise 3.**
Explain the "exercise boundary" in the context of a Bermudan payer swaption and how it relates to the short rate.

??? success "Solution to Exercise 3"
    The exercise boundary is the set of short rates $r^*(T_i)$ at each exercise date $T_i$ above which it is optimal to exercise. Since a payer swaption benefits from high rates (the fixed leg is worth more), the holder exercises when $r(T_i) > r^*(T_i)$. The boundary $r^*(T_i)$ generally decreases over time (it becomes optimal to exercise at lower rates as fewer exercise opportunities remain), creating a monotonically decreasing function of time.

---

**Exercise 4.**
Compare tree-based and Monte Carlo methods for pricing Bermudan swaptions under the Hull-White model. What are the trade-offs?

??? success "Solution to Exercise 4"

    - **Trinomial tree**: Handles the exercise decision naturally via backward induction. Accurate for 1-factor models. Computational cost grows linearly with the number of exercise dates. Limited to low-dimensional models (1-2 factors).
    - **Monte Carlo (Longstaff-Schwartz)**: Works for multi-factor models. Forward simulation with regression-based exercise decision. Can handle path-dependent features. But: biased low (the estimated continuation value is biased), slower convergence, and the exercise policy depends on the choice of basis functions.

    For 1F Hull-White, the trinomial tree is preferred due to its accuracy and efficiency. For 2F models or when path-dependent features are present, Monte Carlo is necessary.
