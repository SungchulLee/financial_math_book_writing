# Greeks and Sensitivity Estimation

The **Greeks** represent sensitivities of an option's value with respect to various parameters. When using finite difference methods to solve the Black-Scholes equation, we can estimate these sensitivities directly from the numerical solution grid.

---

## Key Greeks

| Greek     | Meaning                          | Formula                                       |
|-----------|----------------------------------|-----------------------------------------------|
| **Delta** | $\frac{\partial V}{\partial S}$  | Option price sensitivity to stock price       |
| **Gamma** | $\frac{\partial^2 V}{\partial S^2}$ | Sensitivity of Delta (convexity)             |
| **Theta** | $-\frac{\partial V}{\partial t}$ | Sensitivity to passage of time (decay)        |

---

## Delta (First Derivative in Space)

Approximate Delta at node $i$ using central differences:

$$
\Delta_i \approx \frac{V_{i+1} - V_{i-1}}{2\Delta S}
$$

At the edges ($i = 0$ or $i = M$), use forward or backward difference instead.

---

## Gamma (Second Derivative in Space)

$$
\Gamma_i \approx \frac{V_{i+1} - 2V_i + V_{i-1}}{(\Delta S)^2}
$$

High Gamma near the strike means small moves in $S$ cause big changes in Delta.

---

## Theta (Time Derivative)

Given two time levels ($V^{n+1}$ and $V^n$):

$$
\Theta_i \approx -\frac{V_i^{n+1} - V_i^n}{\Delta t}
$$

In practice, we often use the final two time steps for this estimate.

---

## Python Example: Delta and Gamma Estimation

```python
import numpy as np

def estimate_delta_gamma(S, V):
    dS = S[1] - S[0]
    delta = np.zeros_like(V)
    gamma = np.zeros_like(V)

    # Central differences for interior points
    for i in range(1, len(S) - 1):
        delta[i] = (V[i + 1] - V[i - 1]) / (2 * dS)
        gamma[i] = (V[i + 1] - 2 * V[i] + V[i - 1]) / (dS ** 2)

    # One-sided differences for boundaries
    delta[0] = (V[1] - V[0]) / dS
    delta[-1] = (V[-1] - V[-2]) / dS
    gamma[0] = gamma[1]
    gamma[-1] = gamma[-2]

    return delta, gamma
```

---

## Python Example: Plotting Greeks

```python
import matplotlib.pyplot as plt

delta, gamma = estimate_delta_gamma(S, V_cn)

fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax[0].plot(S, delta, label="Delta", color='blue')
ax[0].set_ylabel("Delta")
ax[0].legend()
ax[0].grid(True)

ax[1].plot(S, gamma, label="Gamma", color='green')
ax[1].set_xlabel("Stock Price")
ax[1].set_ylabel("Gamma")
ax[1].legend()
ax[1].grid(True)

plt.suptitle("Greeks Estimated from Crank-Nicolson FDM Solution")
plt.tight_layout()
plt.show()
```

---

## Practical Considerations

- **Grid resolution:** Delta and Gamma are sensitive to the grid — refine $\Delta S$ for more accurate Greek estimates.
- **Smoothing:** For visual plots or real-time computation, smoothing filters or interpolation may be applied.
- **Theta estimation:** Requires access to values at multiple time levels; Crank-Nicolson is backward in time, so stored values can be reused.

---

## Summary

- The Greeks are essential tools derived from the option price grid.
- Finite difference methods naturally yield accurate estimates for Delta, Gamma, and Theta.
- Proper numerical differentiation and grid resolution ensure reliable sensitivity analysis.

---

## Exercises

**Exercise 1.** Given a uniform spatial grid with $\Delta S = 2$ and the following option values at time $t = 0$: $V_{i-1} = 8.50$, $V_i = 10.25$, $V_{i+1} = 12.40$, compute the central difference estimates for Delta and Gamma at node $i$.

---

**Exercise 2.** The forward difference formula for Delta is $\Delta_i \approx (V_{i+1} - V_i)/\Delta S$, while the central difference formula is $\Delta_i \approx (V_{i+1} - V_{i-1})/(2\Delta S)$. Using Taylor expansion, show that the forward difference has truncation error $O(\Delta S)$ while the central difference has truncation error $O((\Delta S)^2)$.

---

**Exercise 3.** Suppose you have computed from the FDM grid: $V = 10.45$, $\Delta = 0.55$, $\Gamma = 0.04$, at a node where $S = 100$, with parameters $r = 0.05$ and $\sigma = 0.20$. Use the Black-Scholes PDE to estimate Theta. Verify that the PDE residual

$$
\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma - rV
$$

is close to zero.

---

**Exercise 4.** Explain why Gamma estimates are more sensitive to grid resolution than Delta estimates. If the option price has error $\varepsilon$ at each grid node, derive the amplified error in the central difference formulas for Delta and Gamma in terms of $\varepsilon$ and $\Delta S$.

---

**Exercise 5.** A Crank-Nicolson FDM solver produces option values at the final two time levels: $V_i^{N} = 10.25$ and $V_i^{N-1} = 10.38$ with $\Delta t = 0.01$. Estimate Theta using the backward difference formula. If Delta and Gamma at this node are $\Delta = 0.55$ and $\Gamma = 0.04$, and $S = 100$, $r = 0.05$, $\sigma = 0.20$, compare this estimate to the PDE-based Theta.

---

**Exercise 6.** Consider a non-uniform spatial grid where $S_{i-1} = 96$, $S_i = 100$, $S_{i+1} = 106$. Derive modified central difference formulas for Delta and Gamma that account for the unequal spacings $h_- = S_i - S_{i-1}$ and $h_+ = S_{i+1} - S_i$.
