# Theta Income from Short Call

## Background

Black Scholes Theta Income

Educational script demonstrating black scholes theta income concepts.

---

## Code

```python
"""
Black Scholes Theta Income

Educational script demonstrating black scholes theta income concepts.
"""

# ============================================================================
# black_scholes_THETA_INCOME_FROM_SHORT_CALL.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    S = 100
    K = 100
    Ts = np.linspace(0.01, 0.5, 100)  # 0.5 years to expiry
    r = 0.01
    sigma = 0.2

    theta_call, _ = bs.theta(S, K, Ts, r, sigma)

    plt.plot(Ts, - theta_call, label="Short Call Theta Income", color='orange')
    plt.xlabel("Time to Maturity (Years)")
    plt.ylabel("Theta (per year)")
    plt.title("Theta Income from Short Call Option")
    plt.grid(True)
    plt.legend()
    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.show()
```


## Exercises

**Exercise 1.**
Explain why theta income from a short call is highest when the option is at-the-money and close to expiry.

??? success "Solution to Exercise 1"
    Theta $= -\frac{Sn(d_1)\sigma}{2\sqrt{T}} - rKe^{-rT}N(d_2)$. The dominant term involves $n(d_1)/\sqrt{T}$, which is maximized when $d_1 \approx 0$ (ATM) and $T$ is small (the $1/\sqrt{T}$ factor). Near expiry, the option time value decays most rapidly because the uncertainty about the final outcome is being resolved quickly. Short sellers earn this accelerating time decay as income.

---

**Exercise 2.**
For $S = K = 100$, $r = 0.01$, $\sigma = 0.2$, compute the short call theta income at $T = 0.5$ years and $T = 0.01$ years. How much does theta increase as expiry approaches?

??? success "Solution to Exercise 2"
    At $T = 0.5$: $d_1 = (0.01 + 0.02)(0.5)/(0.2\sqrt{0.5}) = 0.106$. $\Theta = -\frac{100 \cdot 0.396 \cdot 0.2}{2\sqrt{0.5}} - 0.01 \cdot 99.5 \cdot 0.477 = -5.60 - 0.47 = -6.07$/yr. At $T = 0.01$: $\Theta \approx -\frac{100 \cdot 0.399 \cdot 0.2}{2\sqrt{0.01}} = -39.9$/yr. Theta increases roughly 6.5-fold as $T$ decreases from 0.5 to 0.01, reflecting the $1/\sqrt{T}$ acceleration.

---

**Exercise 3.**
The x-axis in the theta plot is inverted (time to maturity decreasing from left to right). Explain why this convention is natural for traders monitoring their positions.

??? success "Solution to Exercise 3"
    Traders observe time flowing forward while maturity approaches. The inverted axis shows the natural time progression: the option starts far from expiry (right side of inverted axis) and moves toward expiry (left side). This makes the accelerating theta decay visually apparent as the curve steepens near the left edge, matching the trader experience of watching time value erode faster as expiry nears.

---

**Exercise 4.**
A trader sells a 6-month ATM call for $\$7.97$ (with $S = K = 100$, $r = 0.01$, $\sigma = 0.2$). Estimate the total theta income over the first month, assuming the stock stays at $\$100$.

??? success "Solution to Exercise 4"
    If the stock stays ATM, the option value after 1 month ($T = 5/12$) is approximately $\$7.24$ (using BS with $T = 0.4167$). Theta income $\approx 7.97 - 7.24 = \$0.73$ in the first month. This is roughly $0.73/7.97 = 9.2\%$ of the premium. The remaining $\$7.24$ decays over the next 5 months, with an increasing fraction of the total decay occurring in the final weeks.