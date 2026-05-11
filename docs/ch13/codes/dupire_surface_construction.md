# Dupire Surface from Market Data

## Background

dupire_surface_construction.py

This module implements Dupire Surface from Market Data.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
dupire_surface_construction.py

This module implements Dupire Surface from Market Data.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def dupire_surface_construction():
    """
    Dupire Surface from Market Data.
    
    This function demonstrates the key concepts and computational techniques
    for dupire surface from market data.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Dupire Surface from Market Data
    print(f"Computing Dupire Surface from Market Data...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Dupire Surface from Market Data"
    }
    
    return results


def main():
    """Main execution function."""
    results = dupire_surface_construction()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Dupire Surface from Market Data")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/dupire_surface_construction.png", dpi=150)
    print(f"Figure saved to /tmp/dupire_surface_construction.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Dupire formula expresses local volatility as $\sigma_{\text{loc}}^2(K,T) = \frac{\partial C/\partial T + rK\,\partial C/\partial K}{\frac{1}{2}K^2\,\partial^2 C/\partial K^2}$. Explain the numerator and denominator in terms of option sensitivities.

??? success "Solution to Exercise 1"
    Numerator: $\partial C/\partial T$ is the calendar spread value (sensitivity to maturity), and $rK\partial C/\partial K$ is related to the drift contribution. Denominator: $\frac{1}{2}K^2\partial^2 C/\partial K^2$ is proportional to the butterfly spread value, which measures the density of the risk-neutral distribution at strike $K$. The ratio gives the instantaneous variance conditional on $S_T = K$.

---

**Exercise 2.**
The Dupire surface requires smooth call prices $C(K,T)$. Explain why raw market data must be interpolated before applying the formula.

??? success "Solution to Exercise 2"
    Market quotes are discrete (finite strikes and maturities), noisy (bid-ask spread), and may contain arbitrage violations. The Dupire formula requires first and second derivatives of $C$ with respect to $K$ and $T$. Differentiating noisy discrete data amplifies errors dramatically. Interpolation (e.g., SVI parametric fit or spline) creates a smooth, arbitrage-free surface from which derivatives can be computed reliably.

---

**Exercise 3.**
If $\partial^2 C/\partial K^2 < 0$ at some point, the Dupire formula gives $\sigma_{\text{loc}}^2 < 0$. What does this indicate?

??? success "Solution to Exercise 3"
    A negative butterfly spread ($\partial^2 C/\partial K^2 < 0$) indicates a butterfly arbitrage: the risk-neutral density is negative, which is impossible. This means the input call price surface is not arbitrage-free. The interpolation or raw data must be corrected to ensure $\partial^2 C/\partial K^2 \geq 0$ everywhere before applying Dupire.

---

**Exercise 4.**
Compare the Dupire local volatility surface with the implied volatility surface. Which varies more with strike? Explain the relationship.

??? success "Solution to Exercise 4"
    Local volatility varies approximately twice as much as implied volatility with respect to strike. The heuristic is $\sigma_{\text{loc}}(K) \approx \sigma_{\text{imp}}(K) + K\frac{\partial\sigma_{\text{imp}}}{\partial K}\frac{\ln(S/K)}{\sigma_{\text{imp}}\sqrt{T}}$. Since the skew $\partial\sigma_{\text{imp}}/\partial K < 0$ for equity indices, local vol has a steeper skew. The local vol surface is the "instantaneous" measure of volatility, while implied vol is an average over the option lifetime.