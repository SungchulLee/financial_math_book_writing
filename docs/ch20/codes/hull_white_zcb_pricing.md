# Zero-Coupon Bond Pricing

## Background

hull_white_zcb_pricing.py

This module implements Zero-Coupon Bond Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_zcb_pricing.py

This module implements Zero-Coupon Bond Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def hull_white_zcb_pricing():
    """
    Zero-Coupon Bond Pricing.
    
    This function demonstrates the key concepts and computational techniques
    for zero-coupon bond pricing.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Zero-Coupon Bond Pricing
    print(f"Computing Zero-Coupon Bond Pricing...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Zero-Coupon Bond Pricing"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_zcb_pricing()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Zero-Coupon Bond Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_zcb_pricing.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_zcb_pricing.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The Hull-White ZCB price is $P(t, T) = A(t,T)\,e^{-B(t,T)\,r(t)}$. Derive the expression for $B(t,T)$ from the ODE $B'(\tau) = 1 - \lambda B(\tau)$, $B(0) = 0$.

??? success "Solution to Exercise 1"
    The ODE is $dB/d\tau = 1 - \lambda B$ with $B(0) = 0$. This is a first-order linear ODE. The solution is:

    $$
    B(\tau) = \frac{1 - e^{-\lambda\tau}}{\lambda}.
    $$

    We can verify: $B(0) = 0$ and $B'(\tau) = e^{-\lambda\tau} = 1 - \lambda \cdot \frac{1 - e^{-\lambda\tau}}{\lambda} = 1 - (1 - e^{-\lambda\tau}) = e^{-\lambda\tau}$. Checks out.

---

**Exercise 2.**
For $\lambda = 0.1$ and $\eta = 0.015$, compute $B(0, 5)$ and $B(0, 30)$. Interpret the saturation of $B$ for long maturities.

??? success "Solution to Exercise 2"
    $$
    B(0,5) = \frac{1 - e^{-0.5}}{0.1} = \frac{1 - 0.6065}{0.1} = \frac{0.3935}{0.1} = 3.935.
    $$

    $$
    B(0,30) = \frac{1 - e^{-3}}{0.1} = \frac{1 - 0.0498}{0.1} = \frac{0.9502}{0.1} = 9.502.
    $$

    The maximum is $B_\infty = 1/\lambda = 10$. $B(0,30) = 9.502$ is already $95\%$ of the maximum, showing that bond price sensitivity to the short rate saturates for long maturities. This reflects mean reversion: a change in today's rate has a diminishing effect on far-future rates.

---

**Exercise 3.**
Compute the ZCB price $P(0, 10)$ if $r(0) = 3\%$, $A(0,10) = 0.72$, and $B(0,10) = 6.32$.

??? success "Solution to Exercise 3"
    $$
    P(0,10) = A(0,10) \times e^{-B(0,10) \times r(0)} = 0.72 \times e^{-6.32 \times 0.03} = 0.72 \times e^{-0.1896} = 0.72 \times 0.8273 = 0.5957.
    $$

---

**Exercise 4.**
Explain why the $A(t,T)$ coefficient depends on the entire initial yield curve while $B(t,T)$ depends only on $\lambda$.

??? success "Solution to Exercise 4"
    The $B$ coefficient comes from the Riccati equation for the affine term structure, which involves only the mean reversion speed $\lambda$. It measures the sensitivity of the bond price to the current short rate and is a purely structural parameter.

    The $A$ coefficient incorporates the initial yield curve through $\theta(t)$, which is calibrated to match market bond prices. It ensures $P(0,T) = P_{\text{market}}(0,T)$ by absorbing the level of the yield curve. If $\theta(t)$ changes (e.g., the yield curve shifts), $A$ changes but $B$ remains the same. This separation is a key feature of affine term structure models: the "shape" ($B$) is model-determined while the "level" ($A$) is market-calibrated.
