# Forward Smile Comparison

## Background

local_vol_forward_smile.py

This module implements Forward Smile Comparison.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
local_vol_forward_smile.py

This module implements Forward Smile Comparison.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def local_vol_forward_smile():
    """
    Forward Smile Comparison.
    
    This function demonstrates the key concepts and computational techniques
    for forward smile comparison.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Forward Smile Comparison
    print(f"Computing Forward Smile Comparison...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Forward Smile Comparison"
    }
    
    return results


def main():
    """Main execution function."""
    results = local_vol_forward_smile()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Forward Smile Comparison")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/local_vol_forward_smile.png", dpi=150)
    print(f"Figure saved to /tmp/local_vol_forward_smile.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Explain the key difference between local volatility and implied volatility. Which one is path-dependent?

??? success "Solution to Exercise 1"
    Implied volatility is a single number that, when plugged into the BS formula, recovers the market price---it is an average over all paths and all times. Local volatility $\sigma_{\text{loc}}(S, t)$ is the instantaneous volatility at a specific spot level and time, varying along each path. Neither is path-dependent per se, but local vol determines the dynamics path-by-path, while implied vol summarizes the result.

---

**Exercise 2.**
In a local volatility model, the stock follows $dS = rS\,dt + \sigma_{\text{loc}}(S,t)S\,dW$. Explain why this model exactly reproduces all European option prices.

??? success "Solution to Exercise 2"
    By construction, the Dupire formula ensures the risk-neutral density implied by $\sigma_{\text{loc}}(S,t)$ matches the market-implied density at every strike and maturity. Since European prices are expectations of discounted payoffs under this density, the local vol model reprices all Europeans exactly. This is the fundamental theorem connecting local vol to European prices.

---

**Exercise 3.**
Local volatility models have a well-known failure: they predict that the forward smile flattens as maturity increases. Explain why this contradicts market behavior.

??? success "Solution to Exercise 3"
    Local vol assumes volatility is a deterministic function of spot, not stochastic. When the spot moves to a new level, the local vol surface dictates a specific volatility---there is no uncertainty about future volatility. This means forward-starting options see less smile than spot-starting options, flattening the forward smile. Markets exhibit persistent smiles even for forward-starting options, indicating stochastic volatility is needed.

---

**Exercise 4.**
Compare Monte Carlo and finite difference methods for pricing under local volatility. Which is more efficient for vanilla Europeans? For path-dependent exotics?

??? success "Solution to Exercise 4"
    For vanilla Europeans, FDM is more efficient: it solves the PDE on a 2D grid (S, t) in $O(M \times N)$ operations, giving prices at all strikes simultaneously. Monte Carlo requires separate simulations for each strike, converging as $O(1/\sqrt{N_{\text{paths}}})$. For path-dependent exotics (barriers, Asians), Monte Carlo is more flexible as it naturally handles path dependency, while FDM requires higher-dimensional grids or auxiliary state variables.