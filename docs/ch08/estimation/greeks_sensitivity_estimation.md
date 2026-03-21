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
