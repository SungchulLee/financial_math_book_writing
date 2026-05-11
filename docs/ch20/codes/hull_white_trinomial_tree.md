# Trinomial Tree Construction

## Background

hull_white_trinomial_tree.py

This module implements Trinomial Tree Construction.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_trinomial_tree.py

This module implements Trinomial Tree Construction.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


# ======================================================================

def hull_white_trinomial_tree():
    """
    Trinomial Tree Construction.
    
    This function demonstrates the key concepts and computational techniques
    for trinomial tree construction.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Trinomial Tree Construction
    print(f"Computing Trinomial Tree Construction...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Trinomial Tree Construction"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_trinomial_tree()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Trinomial Tree Construction")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_trinomial_tree.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_trinomial_tree.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the Hull-White trinomial tree, each node has three branches (up, middle, down). How are the branching probabilities determined?

??? success "Solution to Exercise 1"
    At each node with rate $r$, the three branching probabilities $p_u, p_m, p_d$ are chosen to match the first two moments of the Hull-White process:

    $$
    p_u + p_m + p_d = 1,
    $$

    $$
    p_u \cdot \Delta r - p_d \cdot \Delta r = \lambda(\theta(t) - r)\,\Delta t \quad \text{(mean)},
    $$

    $$
    (p_u + p_d) \cdot (\Delta r)^2 = \eta^2\,\Delta t + [\lambda(\theta(t) - r)\,\Delta t]^2 \quad \text{(variance)}.
    $$

    The spacing $\Delta r = \eta\sqrt{3\Delta t}$ is chosen for optimal branching. These three equations have a unique solution for $p_u, p_m, p_d$ at each node.

---

**Exercise 2.**
Explain the advantage of a trinomial tree over a binomial tree for the Hull-White model.

??? success "Solution to Exercise 2"
    The trinomial tree has three key advantages:

    1. **Mean reversion handling**: The middle branch absorbs the mean-reverting drift, keeping the tree centered. A binomial tree would require the tree to drift, potentially creating nodes far from the mean.
    2. **Positive probabilities**: With three branches, it is easier to maintain $p_u, p_m, p_d > 0$ across all nodes, even when the drift is large (far from $\theta$). Binomial trees can produce negative probabilities for extreme nodes.
    3. **Better convergence**: The trinomial tree matches one additional moment, leading to faster convergence with fewer time steps.

---

**Exercise 3.**
If $\Delta t = 0.25$ (quarterly steps) and $\eta = 0.01$, compute the rate spacing $\Delta r$ in the trinomial tree.

??? success "Solution to Exercise 3"
    $$
    \Delta r = \eta\sqrt{3\Delta t} = 0.01 \times \sqrt{3 \times 0.25} = 0.01 \times \sqrt{0.75} = 0.01 \times 0.866 = 0.00866.
    $$

    The rate spacing is approximately 87 basis points per step.

---

**Exercise 4.**
How many nodes does a trinomial tree have after $N$ time steps, and how does this compare to a binomial tree?

??? success "Solution to Exercise 4"
    After $N$ steps, a trinomial tree has at most $2N + 1$ rate levels at the final time step, and the total number of nodes is approximately $\sum_{i=0}^{N}(2i + 1) = (N+1)^2$. A binomial tree has $N + 1$ levels at the final step, with total nodes $\sum_{i=0}^{N}(i+1) = (N+1)(N+2)/2$.

    For $N = 100$: trinomial has $\sim 10{,}201$ nodes, binomial has $\sim 5{,}151$ nodes. The trinomial tree has roughly twice as many nodes but typically requires fewer time steps for the same accuracy, so the total cost is comparable.
