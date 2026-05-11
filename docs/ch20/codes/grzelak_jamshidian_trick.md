# Jamshidian Trick

## Background

Jamshidian's trick for handling E[max(sum, K)] as sum of E[max].

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak

---

## Code

```python
"""
Jamshidian's trick for handling E[max(sum, K)] as sum of E[max].

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


# ======================================================================

def psi_sum(psi, n, x):
    """Compute sum of psi_i."""
    temp = 0
    for i in range(0, n):
        temp = temp + psi(i, x)
    return temp


def jamshidian_trick(psi, n, k):
    """Compute optimal strike using Jamshidian's trick."""
    a = lambda x: psi_sum(psi, n, x) - k
    result = optimize.newton(a, 0.1)
    return result


def main():
    """Main computation."""
    num_samples = 1000
    x = np.random.normal(0.0, 1.0, (num_samples, 1))
    psi_i = lambda i, x: np.exp(-i * np.abs(x))

    # Number of terms
    n = 15

    a = 0
    for i in range(0, n):
        a = a + psi_i(i, x)

    k = np.linspace(2, 10, 10)
    result_mc = np.zeros(len(k))
    for (i, ki) in enumerate(k):
        result_mc[i] = np.mean(np.maximum(a - ki, 0))

    # Jamshidian's trick
    result_jams = np.zeros(len(k))
    for i, ki in enumerate(k):
        # Compute optimal K*
        opt_x = jamshidian_trick(psi_i, n, ki)
        a = 0
        for j in range(0, n):
            a = a + np.mean(np.maximum(psi_i(j, x) - psi_i(j, opt_x), 0))
        result_jams[i] = a

    plt.figure()
    plt.plot(k, result_mc)
    plt.plot(k, result_jams, '--r')
    plt.grid()
    plt.xlabel('K')
    plt.ylabel('expectation')
    plt.legend(['Monte Carlo', "Jamshidian's trick"])


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Jamshidian's trick converts a swaption (option on a sum of cash flows) into a portfolio of options on individual cash flows. Explain the key insight.

??? success "Solution to Exercise 1"
    A payer swaption payoff is $\max\!\bigl(\sum_{i=1}^n c_i P(T, T_i) - 1, 0\bigr)$, where $c_i$ are coupon payments. Directly pricing this requires handling the maximum of a sum. Jamshidian's trick exploits the fact that in a one-factor model, all bond prices are monotonic in the short rate $r(T)$. There exists a unique $r^*$ such that $\sum_i c_i P(T, T_i; r^*) = 1$. For $r > r^*$, the swaption is in the money. The swaption decomposes into:

    $$
    \text{Swaption} = \sum_{i=1}^n c_i\,\text{ZBP}(T, T_i, K_i),
    $$

    where $K_i = P(T, T_i; r^*)$ and ZBP is the zero-coupon bond put price.

---

**Exercise 2.**
Find $r^*$ for a 1-year swaption on a 2-year annual swap with coupon $5\%$ if $P(1, 2; r) = e^{-0.8r}$ and $P(1, 3; r) = e^{-1.5r}$. The condition is $0.05\,e^{-0.8r^*} + 1.05\,e^{-1.5r^*} = 1$.

??? success "Solution to Exercise 2"
    This is a nonlinear equation that requires numerical solution. Testing $r^* = 0.05$:

    $$
    0.05\,e^{-0.04} + 1.05\,e^{-0.075} = 0.05 \times 0.9608 + 1.05 \times 0.9277 = 0.04804 + 0.97409 = 1.02213.
    $$

    This exceeds 1, so $r^*$ must be higher. Testing $r^* = 0.08$:

    $$
    0.05\,e^{-0.064} + 1.05\,e^{-0.12} = 0.05 \times 0.9380 + 1.05 \times 0.8869 = 0.04690 + 0.93125 = 0.97815.
    $$

    This is below 1, so $r^* \in (0.05, 0.08)$. Bisection or Newton's method gives $r^* \approx 0.065$.

---

**Exercise 3.**
Explain why Jamshidian's trick only works for one-factor models and fails for multi-factor models.

??? success "Solution to Exercise 3"
    The trick relies on all bond prices being monotonically decreasing functions of a single state variable $r(T)$. In a one-factor model, higher $r$ means lower prices for all bonds, so there is a unique $r^*$ where the exercise boundary is crossed. In a multi-factor model (e.g., 2F Hull-White), bond prices depend on multiple state variables $(r, u)$. The exercise boundary $\sum c_i P(T, T_i; r, u) = 1$ is a curve in $(r, u)$ space, not a single point. Different bonds may respond differently to the two factors, so no single threshold decomposes the problem into individual bond options.

---

**Exercise 4.**
After finding $r^*$ and the individual strikes $K_i = P(T, T_i; r^*)$, how do you aggregate the individual bond option prices to obtain the swaption price?

??? success "Solution to Exercise 4"
    The swaption price is simply the sum of the weighted bond put prices:

    $$
    V_{\text{swaption}} = \sum_{i=1}^n c_i \times \text{ZBP}(0, T, T_i, K_i),
    $$

    where $c_i$ is the cash flow at $T_i$ ($c_i = K\tau$ for intermediate coupons, $c_n = 1 + K\tau$ for the final coupon including principal), and $\text{ZBP}(0, T, T_i, K_i)$ is the Hull-White analytical put price on a $T_i$-maturity bond with strike $K_i$ and option expiry $T$. No optimization is needed at this stage -- it is a simple linear combination of known analytical prices.
