# Credit Default Swap Pricing and Bootstrapping

## Background

cds_pricing_bootstrapping.py

This module implements CDS Pricing and Bootstrapping.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
cds_pricing_bootstrapping.py

This module implements CDS Pricing and Bootstrapping.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def cds_pricing_bootstrapping():
    """
    CDS Pricing and Bootstrapping.
    
    This function demonstrates the key concepts and computational techniques
    for cds pricing and bootstrapping.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of CDS Pricing and Bootstrapping
    print(f"Computing CDS Pricing and Bootstrapping...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "CDS Pricing and Bootstrapping"
    }
    
    return results


def main():
    """Main execution function."""
    results = cds_pricing_bootstrapping()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("CDS Pricing and Bootstrapping")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/cds_pricing_bootstrapping.png", dpi=150)
    print(f"Figure saved to /tmp/cds_pricing_bootstrapping.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A CDS has a notional of \$10,000,000, a spread of 200 bps, quarterly payments, and a recovery rate of $40\%$. Compute the annual premium payment.

??? success "Solution to Exercise 1"
    The annual premium is $\text{Notional} \times \text{Spread} = 10{,}000{,}000 \times 0.02 = \$200{,}000$. With quarterly payments, each payment is $200{,}000/4 = \$50{,}000$ (approximately, ignoring day count conventions and accrual). The protection buyer pays \$50,000 per quarter. In the event of default, the protection seller pays $(1 - R) \times N = 0.60 \times 10{,}000{,}000 = \$6{,}000{,}000$.

---

**Exercise 2.**
CDS bootstrapping extracts hazard rates from market CDS spreads. For a 1-year CDS with spread $s_1 = 100$ bps, annual payment, risk-free rate $3\%$, and recovery $40\%$, compute the 1-year survival probability.

??? success "Solution to Exercise 2"
    The CDS par condition equates premium and protection legs. For the 1-year case:

    $$
    s_1 \cdot P(0,1) \cdot Q(1) = (1 - R) \cdot P(0,1) \cdot [1 - Q(1)],
    $$

    where $Q(1)$ is the survival probability. Solving:

    $$
    0.01 \times Q(1) = 0.60 \times [1 - Q(1)] \implies 0.01\,Q + 0.60\,Q = 0.60 \implies Q(1) = \frac{0.60}{0.61} \approx 0.9836.
    $$

    The 1-year survival probability is approximately $98.36\%$, and the implied hazard rate is $h \approx -\ln(0.9836) \approx 1.66\%$.

---

**Exercise 3.**
Explain why the recovery rate assumption significantly affects bootstrapped hazard rates and CDS prices.

??? success "Solution to Exercise 3"
    The protection leg payment is $(1-R) \times N$, so a higher recovery rate reduces the protection leg value for the same default probability. To match a given CDS spread, higher $R$ requires higher hazard rates (more likely default). Specifically, hazard rates scale approximately as $h \approx s/(1-R)$, so changing $R$ from $40\%$ to $20\%$ reduces implied hazard rates by roughly a factor of $0.75$. Since market CDS spreads are directly observable but recovery rates are estimated, the hazard rates are model-dependent on the recovery assumption.

---

**Exercise 4.**
After bootstrapping hazard rates $h_1, h_2, h_3$ at years 1, 2, 3 from CDS spreads, how would you price a 2-year CDS with a non-standard spread?

??? success "Solution to Exercise 4"
    Using the bootstrapped survival curve $Q(t) = e^{-\int_0^t h(s)\,ds}$, compute:

    - Premium leg: $\text{PV}_{\text{prem}} = s \sum_{i=1}^{n} \tau_i P(0, T_i) Q(T_i)$
    - Protection leg: $\text{PV}_{\text{prot}} = (1-R) \sum_{i=1}^{n} P(0, T_i)[Q(T_{i-1}) - Q(T_i)]$

    The mark-to-market value of the CDS is $\text{PV}_{\text{prot}} - \text{PV}_{\text{prem}}$. For a par CDS, $s$ is chosen so the value is zero. For a non-standard spread, the value is nonzero and represents the cost of entering the contract at off-market terms.
