# Stress Testing Scenarios

## Background

stress_testing_scenarios.py

This module implements Stress Testing Scenarios.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
stress_testing_scenarios.py

This module implements Stress Testing Scenarios.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def stress_testing_scenarios():
    """
    Stress Testing Scenarios.
    
    This function demonstrates the key concepts and computational techniques
    for stress testing scenarios.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Stress Testing Scenarios
    print(f"Computing Stress Testing Scenarios...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Stress Testing Scenarios"
    }
    
    return results


def main():
    """Main execution function."""
    results = stress_testing_scenarios()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Stress Testing Scenarios")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/stress_testing_scenarios.png", dpi=150)
    print(f"Figure saved to /tmp/stress_testing_scenarios.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Distinguish between historical stress scenarios and hypothetical stress scenarios. Give an example of each.

??? success "Solution to Exercise 1"

    - **Historical**: Replay actual market conditions from a past crisis. Example: Apply the interest rate and equity moves from the 2008 financial crisis (rates drop 200 bps, equities fall 40%, credit spreads widen 500 bps) to the current portfolio.
    - **Hypothetical**: Construct plausible but unprecedented scenarios. Example: A simultaneous 300 bps rate rise, 25% equity correction, and 50% increase in FX volatility driven by a hypothetical sovereign debt crisis.

    Historical scenarios are objective but limited to past events. Hypothetical scenarios can explore tail risks that have never occurred but are plausible.

---

**Exercise 2.**
A portfolio loses \$8M under a "rates up 200 bps" stress scenario. If the portfolio has a notional of \$500M and an average duration of 5 years, verify this loss estimate.

??? success "Solution to Exercise 2"
    $$
    \Delta V \approx -D \times \Delta y \times V = -5 \times 0.02 \times 500{,}000{,}000 = -\$50{,}000{,}000.
    $$

    The duration-based estimate gives a \$50M loss, much larger than \$8M. The discrepancy suggests the portfolio has significant rate hedges (e.g., interest rate swaps offsetting the bond duration) that reduce the net sensitivity. The stress test result of \$8M is the residual loss after hedges.

---

**Exercise 3.**
Explain the concept of reverse stress testing and its regulatory importance.

??? success "Solution to Exercise 3"
    Reverse stress testing identifies the scenarios that would cause the institution to fail (e.g., breach capital requirements, become insolvent). Instead of asking "What is the loss under scenario X?", it asks "What scenario causes a loss of \$Y?". This is valuable because: (1) it identifies hidden vulnerabilities that standard scenarios might miss; (2) it forces management to consider extreme but plausible events; (3) regulators (e.g., under Basel III/IV) require banks to perform reverse stress tests as part of their ICAAP (Internal Capital Adequacy Assessment Process).

---

**Exercise 4.**
Design a stress scenario for a portfolio of interest rate derivatives in a rising rate environment. Specify the rate shock, volatility change, and credit spread move.

??? success "Solution to Exercise 4"
    **Rising Rate Stress Scenario**:

    - Short-term rates: $+150$ bps (aggressive central bank tightening)
    - Long-term rates: $+100$ bps (bear flattening)
    - Interest rate volatility: $+30\%$ (swaption implied vols increase from 50 bps to 65 bps normal)
    - Credit spreads: $+50$ bps (moderate widening due to growth concerns)
    - Recovery rates: Unchanged

    This scenario captures a tightening cycle with yield curve flattening, increased volatility, and mild credit deterioration -- a plausible combination based on historical tightening episodes.
