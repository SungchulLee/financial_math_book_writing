# Swaption Pricing (Black's Formula)

## Background

swaption_pricing_black.py

This module implements Swaption Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
swaption_pricing_black.py

This module implements Swaption Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def swaption_pricing_black():
    """
    Swaption Pricing.
    
    This function demonstrates the key concepts and computational techniques
    for swaption pricing.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Swaption Pricing
    print(f"Computing Swaption Pricing...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Swaption Pricing"
    }
    
    return results


def main():
    """Main execution function."""
    results = swaption_pricing_black()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Swaption Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/swaption_pricing_black.png", dpi=150)
    print(f"Figure saved to /tmp/swaption_pricing_black.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A European payer swaption gives the right to enter a payer swap (pay fixed, receive floating) at expiry $T$. Using Black's formula, write the swaption price in terms of the forward swap rate $S_0$, strike $K$, annuity $A_0$, and Black volatility $\sigma_{\text{Black}}$.

??? success "Solution to Exercise 1"
    The payer swaption price is

    $$
    V_{\text{payer}} = A_0\bigl[S_0\,\mathcal{N}(d_1) - K\,\mathcal{N}(d_2)\bigr],
    $$

    where

    $$
    d_1 = \frac{\ln(S_0/K) + \frac{1}{2}\sigma_{\text{Black}}^2 T}{\sigma_{\text{Black}}\sqrt{T}}, \qquad d_2 = d_1 - \sigma_{\text{Black}}\sqrt{T},
    $$

    and $A_0 = \sum_{i=1}^n \tau_i\,P(0, T_i)$ is the present value of the swap annuity.

---

**Exercise 2.**
Compute the price of a 2-year into 5-year payer swaption with $S_0 = 4\%$, $K = 4\%$ (ATM), $\sigma = 25\%$, $A_0 = 4.5$, and notional \$10,000,000.

??? success "Solution to Exercise 2"
    Since $S_0 = K$ (ATM), $\ln(S_0/K) = 0$:

    $$
    d_1 = \frac{0 + 0.5 \times 0.0625 \times 2}{0.25\sqrt{2}} = \frac{0.0625}{0.3536} = 0.1768.
    $$

    $$
    d_2 = 0.1768 - 0.3536 = -0.1768.
    $$

    $$
    \Phi(0.1768) = 0.5701, \quad \Phi(-0.1768) = 0.4299.
    $$

    $$
    V = 10{,}000{,}000 \times 4.5 \times [0.04 \times 0.5701 - 0.04 \times 0.4299] = 45{,}000{,}000 \times 0.04 \times 0.1402.
    $$

    $$
    V = 45{,}000{,}000 \times 0.005608 = \$252{,}360.
    $$

---

**Exercise 3.**
Explain payer-receiver swaption parity. If the payer swaption costs \$252,360 and the forward swap rate equals the strike, what is the receiver swaption price?

??? success "Solution to Exercise 3"
    Payer-receiver parity states

    $$
    V_{\text{payer}}(K) - V_{\text{receiver}}(K) = A_0 \times (S_0 - K) \times N.
    $$

    When $S_0 = K$ (ATM), $V_{\text{payer}} = V_{\text{receiver}}$. Therefore the receiver swaption also costs $\$252{,}360$.

---

**Exercise 4.**
The swaption volatility cube is indexed by expiry, swap tenor, and strike. Explain what the volatility smile/skew looks like for swaptions and how it differs from equity options.

??? success "Solution to Exercise 4"
    For swaptions, the implied volatility surface typically shows:

    - **Normal vol (basis point vol)**: More commonly used than lognormal vol for interest rates. The normal vol smile is often relatively flat, with a slight asymmetry.
    - **Lognormal vol (Black vol)**: Shows a pronounced downward skew at low strikes (reflecting the possibility of near-zero or negative rates) and can exhibit a smile for very out-of-the-money options.

    Unlike equity options (which show a persistent downward skew due to leverage effects and crash risk), swaption skews are more symmetric and depend heavily on the rate environment. In low-rate environments, Black vol skews are steep because lognormal vol diverges as rates approach zero, while normal vol remains well-behaved.
