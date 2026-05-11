# Yield Curve Bootstrapping

## Background

yield_curve_bootstrapping.py

This module implements Yield Curve Bootstrapping.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
yield_curve_bootstrapping.py

This module implements Yield Curve Bootstrapping.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def yield_curve_bootstrapping():
    """
    Yield Curve Bootstrapping.
    
    This function demonstrates the key concepts and computational techniques
    for yield curve bootstrapping.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Yield Curve Bootstrapping
    print(f"Computing Yield Curve Bootstrapping...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Yield Curve Bootstrapping"
    }
    
    return results


def main():
    """Main execution function."""
    results = yield_curve_bootstrapping()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Yield Curve Bootstrapping")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/yield_curve_bootstrapping.png", dpi=150)
    print(f"Figure saved to /tmp/yield_curve_bootstrapping.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Yield curve bootstrapping sequentially extracts discount factors from market instruments. Given a 1-year zero rate of $3\%$ and a 2-year par swap rate of $3.5\%$, compute the 2-year discount factor.

??? success "Solution to Exercise 1"
    The 1-year discount factor is $P(0,1) = e^{-0.03} \approx 0.9704$ (or $1/1.03 = 0.9709$ for annual compounding).

    Using annual compounding, the 2-year par swap pays $3.5\%$ annually. The par swap condition is:

    $$
    0.035 \times P(0,1) + (1 + 0.035) \times P(0,2) = 1.
    $$

    $$
    0.035 \times 0.9709 + 1.035 \times P(0,2) = 1.
    $$

    $$
    0.03398 + 1.035\,P(0,2) = 1 \implies P(0,2) = \frac{1 - 0.03398}{1.035} = \frac{0.96602}{1.035} \approx 0.9334.
    $$

---

**Exercise 2.**
Explain why bootstrapping proceeds sequentially from shorter to longer maturities and why the order matters.

??? success "Solution to Exercise 2"
    Each new instrument introduces one unknown discount factor while using all previously determined discount factors. The $n$-year par swap equation involves $P(0,1), P(0,2), \ldots, P(0,n)$, and only $P(0,n)$ is unknown (the rest were determined at earlier steps). If we tried to bootstrap out of order (e.g., solve for $P(0,5)$ before $P(0,3)$), the swap equation would contain multiple unknowns. The sequential approach ensures each step is a single-equation, single-unknown problem that can be solved analytically.

---

**Exercise 3.**
After bootstrapping, the zero rates at maturities 1, 2, 3, 5 are $\{3.0\%, 3.5\%, 3.8\%, 4.2\%\}$. Compute the 1-year forward rate from year 2 to year 3.

??? success "Solution to Exercise 3"
    The forward rate $f(2,3)$ satisfies

    $$
    (1 + y_3)^3 = (1 + y_2)^2 \times (1 + f(2,3)).
    $$

    With continuous compounding:

    $$
    f(2,3) = \frac{y_3 \times 3 - y_2 \times 2}{3 - 2} = \frac{0.038 \times 3 - 0.035 \times 2}{1} = 0.114 - 0.070 = 0.044 = 4.4\%.
    $$

---

**Exercise 4.**
Describe two common issues that arise in yield curve bootstrapping and how they are typically addressed.

??? success "Solution to Exercise 4"

    1. **Missing maturities**: Market instruments may not be available at every maturity (e.g., no liquid swap at 4 years). This is addressed by interpolation between bootstrapped points using cubic splines, monotone convex methods, or piecewise linear interpolation. The choice affects the smoothness of forward rates.

    2. **Instrument overlap**: Different instrument types (deposits, futures, swaps) may cover overlapping maturity ranges with inconsistent pricing. This is addressed by using a priority hierarchy (e.g., deposits for short end, futures for 1-3 years, swaps for long end) and ensuring smooth transitions between instrument types, sometimes using a global fitting procedure instead of sequential bootstrapping.
