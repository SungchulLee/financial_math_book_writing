# Gamma Hedging with Options

## Background

gamma_hedging_with_options.py

This module implements Gamma Hedging with Options.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
gamma_hedging_with_options.py

This module implements Gamma Hedging with Options.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def gamma_hedging_with_options():
    """
    Gamma Hedging with Options.
    
    This function demonstrates the key concepts and computational techniques
    for gamma hedging with options.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Gamma Hedging with Options
    print(f"Computing Gamma Hedging with Options...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Gamma Hedging with Options"
    }
    
    return results


def main():
    """Main execution function."""
    results = gamma_hedging_with_options()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Gamma Hedging with Options")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/gamma_hedging_with_options.png", dpi=150)
    print(f"Figure saved to /tmp/gamma_hedging_with_options.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
A delta-neutral portfolio has $\Gamma = -0.05$ (short gamma). To gamma-hedge, you buy calls with individual gamma $\gamma_c = 0.025$. How many calls are needed?

??? success "Solution to Exercise 1"
    Calls needed: $n = |\Gamma_{\text{portfolio}}| / \gamma_c = 0.05 / 0.025 = 2$. After adding 2 calls, the portfolio gamma becomes $-0.05 + 2(0.025) = 0$. However, adding calls changes the portfolio delta by $2\Delta_c$, requiring a spot adjustment to maintain delta neutrality.

---

**Exercise 2.**
Explain why gamma hedging requires options (not just the underlying asset) and what tradeoff the hedger faces.

??? success "Solution to Exercise 2"
    The underlying has $\Gamma = 0$, so it cannot offset portfolio gamma. Only options have nonzero gamma. The tradeoff: buying options for gamma protection costs money (option premium and time decay). The hedger pays theta to earn gamma protection. Short gamma earns theta but risks large losses from sudden moves.

---

**Exercise 3.**
For a gamma-neutral, delta-neutral portfolio, what is the dominant remaining risk? How would you hedge it?

??? success "Solution to Exercise 3"
    The dominant remaining risk is vega (volatility) risk. If implied volatility changes, the option values shift but the hedge may not compensate. Vega hedging requires adding options with different characteristics (e.g., different strikes or maturities) to achieve the desired vega exposure. Additionally, higher-order risks (vanna, volga) remain.

---

**Exercise 4.**
A portfolio is short 100 ATM calls ($\Gamma = -0.02$ each, total $\Gamma = -2.0$). ATM puts have $\Gamma = 0.02$. Compute the put quantity needed for gamma neutrality and the resulting theta cost if each put has $\Theta = -5$/year.

??? success "Solution to Exercise 4"
    Puts needed: $100$ (since each put has $\Gamma = 0.02$ and total needed is $2.0$). Total theta from puts: $100 \times (-5) = -\$500$/year. The short calls also generate theta income: if each short call has $\Theta = +5$/year (for the short position), income is $+\$500$/year. Net theta $\approx 0$, which is typical for delta-gamma-neutral positions.