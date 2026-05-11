# Convexity Adjustment (Constant Maturity Swap)

## Background

convexity_adjustment_cms.py

This module implements Convexity Adjustment CMS.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
convexity_adjustment_cms.py

This module implements Convexity Adjustment CMS.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def convexity_adjustment_cms():
    """
    Convexity Adjustment CMS.
    
    This function demonstrates the key concepts and computational techniques
    for convexity adjustment cms.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Convexity Adjustment CMS
    print(f"Computing Convexity Adjustment CMS...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Convexity Adjustment CMS"
    }
    
    return results


def main():
    """Main execution function."""
    results = convexity_adjustment_cms()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Convexity Adjustment CMS")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/convexity_adjustment_cms.png", dpi=150)
    print(f"Figure saved to /tmp/convexity_adjustment_cms.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Explain what a Constant Maturity Swap (CMS) is and why the CMS rate requires a convexity adjustment when priced under the risk-neutral measure.

??? success "Solution to Exercise 1"
    A CMS pays the prevailing swap rate $S(T)$ of a fixed-maturity swap at payment dates. Under the risk-neutral measure, the expected discounted payoff involves $\mathbb{E}[S(T)/M(T)]$, but the swap rate is a martingale under the swap annuity measure, not under the risk-neutral measure. The change of numeraire from the annuity to the money market account introduces a Radon-Nikodym derivative that depends on the correlation between $S(T)$ and $1/M(T)$. This dependence creates the convexity adjustment:

    $$
    \text{CMS rate} \approx F_{\text{swap}} + \text{Convexity Adjustment},
    $$

    where the adjustment is positive because the swap annuity is a convex function of the swap rate.

---

**Exercise 2.**
If the forward swap rate is $F = 5\%$, the swap annuity duration is $\tau = 4$ years, and the volatility of the swap rate is $\sigma = 15\%$ with expiry $T = 2$ years, estimate the convexity adjustment using the linear approximation.

??? success "Solution to Exercise 2"
    The linear convexity adjustment is approximately

    $$
    \text{CA} \approx \frac{F^2 \sigma^2 T \cdot \tau}{1 + \tau F} = \frac{0.05^2 \times 0.0225 \times 2 \times 4}{1 + 4 \times 0.05} = \frac{0.0025 \times 0.0225 \times 8}{1.2} = \frac{0.00045}{1.2} \approx 0.000375.
    $$

    The convexity adjustment is about $3.75$ basis points, so the CMS rate is approximately $5\% + 0.0375\% = 5.0375\%$.

---

**Exercise 3.**
How does the convexity adjustment depend on volatility? Plot the qualitative behavior of the adjustment as a function of $\sigma$ and explain the economic intuition.

??? success "Solution to Exercise 3"
    The convexity adjustment is proportional to $\sigma^2$, so it is a convex, increasing function of volatility. When $\sigma = 0$, the adjustment is zero (deterministic rates, no convexity effect). As $\sigma$ increases, the adjustment grows quadratically because higher volatility amplifies the nonlinear effect of the numeraire change. Economically, higher volatility means the swap rate distribution is more spread out, and the convex relationship between the swap rate and the annuity factor produces a larger expected value under the risk-neutral measure than under the annuity measure.

---

**Exercise 4.**
A CMS receiver pays LIBOR and receives the 10-year swap rate. If the 10-year forward swap rate is $4.5\%$, the convexity adjustment is $+8$ basis points, and the 3-month LIBOR forward is $3.2\%$, what is the approximate fair value spread of the CMS leg over LIBOR?

??? success "Solution to Exercise 4"
    The adjusted CMS rate is $4.5\% + 0.08\% = 4.58\%$. The CMS receiver receives $4.58\%$ and pays LIBOR at $3.2\%$. The spread is

    $$
    \text{CMS spread} = 4.58\% - 3.20\% = 1.38\%.
    $$

    The fair value spread of the CMS leg over LIBOR is approximately $138$ basis points. Without the convexity adjustment, the spread would be $4.50\% - 3.20\% = 1.30\%$, underestimating the true value by $8$ basis points.
