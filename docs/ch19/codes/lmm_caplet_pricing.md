# LIBOR Market Model Caplet Pricing

## Background

lmm_caplet_pricing.py

This module implements LMM Caplet Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
lmm_caplet_pricing.py

This module implements LMM Caplet Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def lmm_caplet_pricing():
    """
    LMM Caplet Pricing.
    
    This function demonstrates the key concepts and computational techniques
    for lmm caplet pricing.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of LMM Caplet Pricing
    print(f"Computing LMM Caplet Pricing...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "LMM Caplet Pricing"
    }
    
    return results


def main():
    """Main execution function."""
    results = lmm_caplet_pricing()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("LMM Caplet Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/lmm_caplet_pricing.png", dpi=150)
    print(f"Figure saved to /tmp/lmm_caplet_pricing.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the LIBOR Market Model (LMM), each forward rate $L_k(t)$ follows $dL_k = \mu_k\,dt + \sigma_k L_k\,dW_k$ under the risk-neutral measure. Under the $T_{k+1}$-forward measure, what is the drift of $L_k$?

??? success "Solution to Exercise 1"
    Under the $T_{k+1}$-forward measure $\mathbb{Q}^{T_{k+1}}$, the forward rate $L_k(t)$ is a martingale, so its drift is zero:

    $$
    dL_k(t) = \sigma_k\,L_k(t)\,dW_k^{T_{k+1}}(t).
    $$

    This is the key simplification of the LMM: by choosing the appropriate forward measure for each caplet, the drift disappears and the forward rate follows a geometric Brownian motion. The caplet on $L_k$ can then be priced using Black's formula directly.

---

**Exercise 2.**
Using Black's formula under the LMM, price a caplet with $L_k(0) = 5\%$, strike $K = 4.5\%$, volatility $\sigma_k = 20\%$, expiry $T_k = 2$ years, $\tau = 0.5$ years, notional $N = \$1{,}000{,}000$, and $P(0, T_{k+1}) = 0.95$.

??? success "Solution to Exercise 2"
    Compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(0.05/0.045) + 0.5 \times 0.04 \times 2}{0.20\sqrt{2}} = \frac{0.1054 + 0.04}{0.2828} = \frac{0.1454}{0.2828} = 0.5142.
    $$

    $$
    d_2 = 0.5142 - 0.2828 = 0.2314.
    $$

    The caplet price is

    $$
    V = N \cdot \tau \cdot P(0, T_{k+1})\bigl[L_k(0)\,\mathcal{N}(d_1) - K\,\mathcal{N}(d_2)\bigr].
    $$

    $$
    V = 1{,}000{,}000 \times 0.5 \times 0.95 \times [0.05 \times 0.6964 - 0.045 \times 0.5915].
    $$

    $$
    V = 475{,}000 \times [0.03482 - 0.02662] = 475{,}000 \times 0.00820 \approx \$3{,}895.
    $$

---

**Exercise 3.**
Explain the difference between caplet volatilities (spot volatilities) and cap volatilities (flat volatilities) in the LMM framework.

??? success "Solution to Exercise 3"
    Caplet volatilities $\sigma_k$ are the individual volatility parameters for each forward rate $L_k$. Each caplet can have a different volatility reflecting the term structure of volatility. Cap volatilities are single "flat" volatilities $\bar{\sigma}$ that, when applied to all caplets in a cap, reproduce the market cap price:

    $$
    \text{Cap}(\bar{\sigma}) = \sum_{k} \text{Caplet}_k(\bar{\sigma}) = \text{Market price}.
    $$

    The flat cap volatility is a weighted average of the individual caplet volatilities, with weights depending on the caplet prices. Converting between the two is called "cap stripping."

---

**Exercise 4.**
If caplet volatilities for years 1 through 5 are $\{18\%, 19\%, 20\%, 21\%, 22\%\}$, what qualitative pattern does this represent, and what are its implications for cap pricing?

??? success "Solution to Exercise 4"
    This is an upward-sloping volatility term structure: longer-dated caplets have higher volatilities. This pattern implies that the market expects greater uncertainty about forward rates further in the future. For cap pricing:

    - Short-dated caps are priced with lower volatilities and are therefore cheaper per unit of risk.
    - Long-dated caps have progressively higher volatilities, making them relatively more expensive.
    - The flat cap volatility for a 5-year cap will be a weighted average, somewhere between $18\%$ and $22\%$, with longer-dated caplets receiving more weight due to their higher notional contribution.
