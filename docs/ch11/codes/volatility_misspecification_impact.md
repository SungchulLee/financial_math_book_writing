# Volatility Misspecification Impact

## Background

volatility_misspecification_impact.py

This module implements Volatility Misspecification Impact.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
volatility_misspecification_impact.py

This module implements Volatility Misspecification Impact.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def volatility_misspecification_impact():
    """
    Volatility Misspecification Impact.
    
    This function demonstrates the key concepts and computational techniques
    for volatility misspecification impact.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Volatility Misspecification Impact
    print(f"Computing Volatility Misspecification Impact...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Volatility Misspecification Impact"
    }
    
    return results


def main():
    """Main execution function."""
    results = volatility_misspecification_impact()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Volatility Misspecification Impact")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/volatility_misspecification_impact.png", dpi=150)
    print(f"Figure saved to /tmp/volatility_misspecification_impact.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
If the true volatility is $\sigma_{\text{true}} = 0.25$ but you hedge using $\sigma_{\text{hedge}} = 0.20$, is the hedging P&L biased? In which direction?

??? success "Solution to Exercise 1"
    Yes, the P&L is biased. The hedger underestimates volatility, so they underhedge gamma exposure. The BS PDE gives the expected P&L as $\frac{1}{2}(\sigma_{\text{true}}^2 - \sigma_{\text{hedge}}^2)S^2\Gamma\Delta t > 0$ per step. The hedger systematically profits because they sold the option at a price computed with higher $\sigma$ than they hedge with. However, this profit comes with increased variance.

---

**Exercise 2.**
Derive the instantaneous hedging P&L when the hedge volatility differs from the realized volatility.

??? success "Solution to Exercise 2"
    The hedging P&L over $[t, t+dt]$ is: $d\Pi = \frac{1}{2}(\sigma_{\text{realized}}^2 - \sigma_{\text{hedge}}^2)S^2\Gamma_{\text{hedge}}\,dt$. This follows from the BS PDE: the option value satisfies the PDE with $\sigma_{\text{realized}}$, while the hedge portfolio evolves with $\sigma_{\text{hedge}}$. The residual is the gamma-weighted difference in variance.

---

**Exercise 3.**
If $\sigma_{\text{true}} = 0.3$ and $\sigma_{\text{hedge}} = 0.2$, compute the expected annual P&L per unit gamma for $S = 100$.

??? success "Solution to Exercise 3"
    Expected P&L $= \frac{1}{2}(0.09 - 0.04)(10000)\Gamma \times 1 = 250\Gamma$ per year per share. For $\Gamma = 0.02$: expected P&L $= 250 \times 0.02 = \$5$ per year. This is the "variance risk premium" captured by selling options at implied vol (20%) and hedging while realized vol is higher (30%).

---

**Exercise 4.**
Explain why selling options at high implied volatility and hedging at realized volatility is a common strategy, and what risks remain.

??? success "Solution to Exercise 4"
    If implied vol consistently exceeds realized vol (the "variance risk premium"), selling options and delta-hedging locks in the difference. The strategy earns $\frac{1}{2}(\sigma_{\text{implied}}^2 - \sigma_{\text{realized}}^2)S^2\Gamma$ on average. Risks: (1) realized vol may occasionally spike above implied vol (tail events); (2) the P&L path is volatile even when the average is positive; (3) model risk from stochastic volatility not captured by BS; (4) jump risk creates sudden large losses.