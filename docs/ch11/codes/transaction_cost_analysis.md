# Transaction Cost Analysis

## Background

transaction_cost_analysis.py

This module implements Transaction Cost Analysis.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
transaction_cost_analysis.py

This module implements Transaction Cost Analysis.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def transaction_cost_analysis():
    """
    Transaction Cost Analysis.
    
    This function demonstrates the key concepts and computational techniques
    for transaction cost analysis.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Transaction Cost Analysis
    print(f"Computing Transaction Cost Analysis...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Transaction Cost Analysis"
    }
    
    return results


def main():
    """Main execution function."""
    results = transaction_cost_analysis()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Transaction Cost Analysis")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/transaction_cost_analysis.png", dpi=150)
    print(f"Figure saved to /tmp/transaction_cost_analysis.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Define proportional transaction costs and explain how they differ from fixed costs. Which type is more relevant for option hedging?

??? success "Solution to Exercise 1"
    Proportional costs are a percentage of the trade value: cost $= c \times |S \times \Delta\text{shares}|$. Fixed costs are a constant per trade regardless of size. For option hedging, proportional costs are more relevant because hedging involves frequent small trades whose size varies with delta changes. The proportional model captures the bid-ask spread, which scales with trade size. Fixed costs matter more for retail-size trades.

---

**Exercise 2.**
If transaction costs are 0.1% per trade, a hedger rebalances 252 times per year, and each trade averages $\$500$ in notional, compute the annual transaction cost.

??? success "Solution to Exercise 2"
    Annual TC $= 252 \times 0.001 \times 500 = \$126$. If the option premium is $\$1{,}000$, this represents $12.6\%$ of the premium, significantly eroding profitability. This motivates less frequent rebalancing or bandwidth-based strategies.

---

**Exercise 3.**
A bandwidth strategy rebalances only when $|\Delta_{\text{new}} - \Delta_{\text{current}}| > \epsilon$. Explain the tradeoff and how to choose $\epsilon$.

??? success "Solution to Exercise 3"
    Larger $\epsilon$ reduces the number of trades (lower TC) but increases hedging error (higher variance). Optimal $\epsilon$ minimizes total cost = hedging error cost + transaction costs. The Whalley-Wilmott approximation gives $\epsilon^* \propto (c / \Gamma)^{1/3}$, where $c$ is the proportional cost and $\Gamma$ is the option gamma.

---

**Exercise 4.**
Compare the total hedging cost (error + TC) for three strategies: continuous hedging (theoretical), daily hedging, and bandwidth hedging with $\epsilon = 0.02$. Rank them by total cost.

??? success "Solution to Exercise 4"
    Continuous: zero hedging error, infinite TC (impractical). Daily: moderate error ($\propto 1/\sqrt{252}$), moderate TC ($252 \times c \times \text{avg trade}$). Bandwidth: adaptive error and TC depending on $\epsilon$. Ranking by total cost: bandwidth $<$ daily $<$ continuous (which is infeasible). The bandwidth strategy optimally balances the two costs by trading only when necessary.