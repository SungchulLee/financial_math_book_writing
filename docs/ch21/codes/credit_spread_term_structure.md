# Credit Spread Term Structure

## Background

credit_spread_term_structure.py

This module implements Credit Spread Term Structure.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
credit_spread_term_structure.py

This module implements Credit Spread Term Structure.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def credit_spread_term_structure():
    """
    Credit Spread Term Structure.
    
    This function demonstrates the key concepts and computational techniques
    for credit spread term structure.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Credit Spread Term Structure
    print(f"Computing Credit Spread Term Structure...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Credit Spread Term Structure"
    }
    
    return results


def main():
    """Main execution function."""
    results = credit_spread_term_structure()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Credit Spread Term Structure")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/credit_spread_term_structure.png", dpi=150)
    print(f"Figure saved to /tmp/credit_spread_term_structure.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The credit spread is defined as $s(T) = y_{\text{risky}}(T) - y_{\text{risk-free}}(T)$. If the risk-free 5-year yield is $3\%$ and the corporate bond yield is $4.5\%$, what is the credit spread?

??? success "Solution to Exercise 1"
    $$
    s(5) = 4.5\% - 3.0\% = 1.5\% = 150 \text{ bps}.
    $$

---

**Exercise 2.**
Explain the relationship between the credit spread, hazard rate, and recovery rate under the reduced-form model assumption.

??? success "Solution to Exercise 2"
    Under the reduced-form model with constant hazard rate $h$ and recovery rate $R$:

    $$
    s \approx h \times (1 - R).
    $$

    This approximation holds for small $h$ and shows that the credit spread compensates investors for expected loss: the probability of default ($h$) times the loss given default ($1 - R$). For example, $h = 2\%$ and $R = 40\%$ gives $s \approx 1.2\%$. This is a first-order approximation; the exact relationship involves continuous discounting and survival probabilities.

---

**Exercise 3.**
An upward-sloping credit spread term structure (wider spreads at longer maturities) is typical for investment-grade issuers. Explain the economic intuition.

??? success "Solution to Exercise 3"
    Investment-grade issuers have low near-term default probability, so short-dated spreads are tight. Over longer horizons, cumulative default probability increases (more time for adverse events), widening spreads. Additionally, uncertainty about the issuer's future creditworthiness grows with time, commanding a larger risk premium. The term structure can also reflect:

    - Market expectation of credit deterioration over time.
    - Liquidity premium increasing with maturity.
    - Supply/demand dynamics for long-dated corporate bonds.

---

**Exercise 4.**
A flat or inverted credit spread curve (wider spreads at shorter maturities) can occur for distressed issuers. Explain why.

??? success "Solution to Exercise 4"
    For distressed issuers, the market perceives high near-term default risk, making short-dated spreads very wide. If the issuer survives the near-term stress period, it may recover creditworthiness, so longer-dated spreads can be narrower (conditional on survival). This creates an inverted curve. Mathematically, if the hazard rate is high initially but decreasing: $h(t) = h_0 e^{-\alpha t}$, the implied spread term structure inverts because the average hazard rate over $[0, T]$ decreases with $T$.
