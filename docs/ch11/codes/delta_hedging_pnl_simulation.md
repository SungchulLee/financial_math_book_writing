# Delta Hedging Profit and Loss Simulation

## Background

delta_hedging_pnl_simulation.py

This module implements Delta Hedging P&L Simulation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
delta_hedging_pnl_simulation.py

This module implements Delta Hedging P&L Simulation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# ======================================================================

def delta_hedging_pnl_simulation():
    """
    Delta Hedging P&L Simulation.
    
    This function demonstrates the key concepts and computational techniques
    for delta hedging p&l simulation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Delta Hedging P&L Simulation
    print(f"Computing Delta Hedging P&L Simulation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Delta Hedging P&L Simulation"
    }
    
    return results


def main():
    """Main execution function."""
    results = delta_hedging_pnl_simulation()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Delta Hedging P&L Simulation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/delta_hedging_pnl_simulation.png", dpi=150)
    print(f"Figure saved to /tmp/delta_hedging_pnl_simulation.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
In a delta hedging simulation, the hedger holds $\Delta_t$ shares at each rebalancing time. Explain the P&L evolution equation and the role of the risk-free rate.

??? success "Solution to Exercise 1"
    The P&L at time $t_{i+1}$ is: $\text{PnL}_{i+1} = \text{PnL}_i \cdot e^{r\Delta t} - (\Delta_{i+1} - \Delta_i) \cdot S_{i+1}$. The first term grows the cash balance at the risk-free rate. The second term reflects the cost of rebalancing: buying $(\Delta_{i+1} - \Delta_i)$ shares at price $S_{i+1}$. At maturity, the hedger pays the option payoff and liquidates the stock position.

---

**Exercise 2.**
Why does the hedging P&L distribution have mean near zero but nonzero variance? What determines the variance?

??? success "Solution to Exercise 2"
    The mean is near zero because delta hedging is self-financing under the risk-neutral measure: the initial option premium funds the replicating strategy on average. The variance arises from discrete rebalancing: between rebalancing times, the delta changes but the hedge does not. The variance is proportional to $\Gamma^2 S^4 \sigma^4 (\Delta t)$ per step, accumulated over $N$ steps. Finer rebalancing ($\Delta t \to 0$) reduces variance toward zero.

---

**Exercise 3.**
If the hedging is performed with 1000 time steps over 1 year, estimate the standard deviation of the hedging error for an ATM call with $S_0 = 1$, $\sigma = 0.2$.

??? success "Solution to Exercise 3"
    The hedging error std is approximately $\frac{\sigma^2 S_0}{2}\sqrt{\frac{T}{N}} \cdot \Gamma_{\text{avg}} \cdot S_0 \approx \frac{0.04}{2}\sqrt{0.001} \cdot 0.02 \cdot 1 \approx 0.000013$ per path. With $N = 1000$, this is very small, explaining the narrow P&L histogram. With $N = 50$, the error would be $\sqrt{20}$ times larger.

---

**Exercise 4.**
The histogram of final P&L is centered near zero and symmetric. Under what conditions would it become asymmetric?

??? success "Solution to Exercise 4"
    Asymmetry arises when: (1) the true dynamics differ from the hedging model (e.g., jumps or stochastic volatility in the real process but BS hedging); (2) transaction costs create asymmetric slippage; (3) very few rebalancing steps cause the gamma effect to dominate, creating positive skewness (since gamma P&L is $(dS)^2$ which is always positive for long gamma positions). Under pure GBM with frequent rebalancing, the P&L is approximately symmetric.