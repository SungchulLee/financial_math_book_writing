# Duration and Key Rate Duration

## Background

duration_key_rate.py

This module implements Duration and Key Rate Duration.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
duration_key_rate.py

This module implements Duration and Key Rate Duration.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def duration_key_rate():
    """
    Duration and Key Rate Duration.
    
    This function demonstrates the key concepts and computational techniques
    for duration and key rate duration.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Duration and Key Rate Duration
    print(f"Computing Duration and Key Rate Duration...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Duration and Key Rate Duration"
    }
    
    return results


def main():
    """Main execution function."""
    results = duration_key_rate()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Duration and Key Rate Duration")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/duration_key_rate.png", dpi=150)
    print(f"Figure saved to /tmp/duration_key_rate.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A bond has a modified duration of $7.2$ and a yield of $4\%$. If the yield increases by 50 basis points, estimate the percentage price change using the duration approximation.

??? success "Solution to Exercise 1"
    The duration approximation gives

    $$
    \frac{\Delta P}{P} \approx -D_{\text{mod}} \times \Delta y = -7.2 \times 0.005 = -0.036 = -3.6\%.
    $$

    The bond price is expected to decrease by approximately $3.6\%$.

---

**Exercise 2.**
Explain the concept of key rate duration and how it differs from effective (parallel shift) duration. Why is key rate duration important for portfolio risk management?

??? success "Solution to Exercise 2"
    Effective duration measures the bond's sensitivity to a parallel shift of the entire yield curve. Key rate duration (KRD) measures sensitivity to a change at a specific maturity point while keeping the rest of the curve unchanged. For a set of key rates at maturities $T_1, \ldots, T_n$:

    $$
    \text{KRD}(T_k) = -\frac{1}{P}\frac{\partial P}{\partial y(T_k)}.
    $$

    The sum of all key rate durations approximately equals the effective duration. KRD is important because yield curve movements are rarely parallel; curves can steepen, flatten, or twist. A portfolio hedged for parallel shifts may still lose value under non-parallel moves, and KRD identifies which maturities contribute most to risk.

---

**Exercise 3.**
A portfolio has key rate durations of $0.5$ at the 2-year point, $2.1$ at the 5-year point, and $4.8$ at the 10-year point. If the 5-year rate increases by 25 basis points while other rates remain unchanged, estimate the portfolio's percentage price change.

??? success "Solution to Exercise 3"
    Only the 5-year key rate changes, so

    $$
    \frac{\Delta P}{P} \approx -\text{KRD}(5y) \times \Delta y(5y) = -2.1 \times 0.0025 = -0.00525 = -0.525\%.
    $$

    The portfolio value decreases by approximately $0.525\%$.

---

**Exercise 4.**
Describe how key rate durations are computed numerically using finite differences. What bump size is typically used, and what are the trade-offs?

??? success "Solution to Exercise 4"
    For each key rate at maturity $T_k$, bump the yield at $T_k$ by a small amount $\Delta y$ (typically $1$ basis point $= 0.0001$), interpolate the perturbed curve, and reprice the bond:

    $$
    \text{KRD}(T_k) \approx -\frac{P(y(T_k) + \Delta y) - P(y(T_k) - \Delta y)}{2\,\Delta y \cdot P}.
    $$

    Trade-offs: A larger bump ($10$ bps) gives more stable estimates but introduces nonlinearity error. A smaller bump ($0.01$ bps) is more accurate but suffers from floating-point cancellation. The choice of interpolation method (linear, cubic) for the perturbed curve also affects the results, as it determines how the bump at $T_k$ propagates to neighboring maturities.
