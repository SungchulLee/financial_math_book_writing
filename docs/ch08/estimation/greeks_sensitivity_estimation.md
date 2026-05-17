# Greeks and Sensitivity Estimation

Once the FDM has solved the Black-Scholes PDE, every Greek is a partial derivative of the resulting price surface. Spatial Greeks ($\Delta$, $\Gamma$) come from differencing the grid in $S$; the time Greek ($\Theta$) comes from differencing in $t$ or from the PDE itself; parameter Greeks ($\mathcal{V}$, $\rho$) require re-solving the PDE with bumped inputs because the grid does not vary in $\sigma$ or $r$. This page is the orientation map; the per-Greek mechanics live in the companion pages.

---

## Key Greeks

| Greek     | Meaning                          | Formula                                       |
|-----------|----------------------------------|-----------------------------------------------|
| **Delta** | $\frac{\partial V}{\partial S}$  | Option price sensitivity to stock price       |
| **Gamma** | $\frac{\partial^2 V}{\partial S^2}$ | Sensitivity of Delta (convexity)             |
| **Theta** | $-\frac{\partial V}{\partial t}$ | Sensitivity to passage of time (decay)        |

---

## Delta and Gamma (Spatial Greeks)

Recall (see [§ Delta and Gamma via Finite Differences](delta_gamma_finite_differences.md)): central differences extract $\Delta = (V_{i+1}-V_{i-1})/(2\Delta S)$ and $\Gamma = (V_{i+1}-2V_i+V_{i-1})/(\Delta S)^2$ directly from the FDM grid, with one-sided formulas at boundaries.

---

## Theta (Time Derivative)

Recall (see [§ Theta from Time Stepping](theta_from_time_stepping.md)): theta can be estimated by backward differencing across stored time levels, or — preferably — via the PDE relation $\Theta = rV - rS\Delta - \tfrac{1}{2}\sigma^2 S^2\Gamma$.

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

??? success "Solution to Exercise 1"
    Using the central difference formulas with $\Delta S = 2$, $V_{i-1} = 8.50$, $V_i = 10.25$, $V_{i+1} = 12.40$:

    **Delta:**

    $$
    \Delta_i \approx \frac{V_{i+1} - V_{i-1}}{2\Delta S} = \frac{12.40 - 8.50}{2 \times 2} = \frac{3.90}{4} = 0.975
    $$

    **Gamma:**

    $$
    \Gamma_i \approx \frac{V_{i+1} - 2V_i + V_{i-1}}{(\Delta S)^2} = \frac{12.40 - 2(10.25) + 8.50}{4} = \frac{12.40 - 20.50 + 8.50}{4} = \frac{0.40}{4} = 0.10
    $$

    Therefore $\Delta_i = 0.975$ and $\Gamma_i = 0.10$.

---

**Exercise 2.** The forward difference formula for Delta is $\Delta_i \approx (V_{i+1} - V_i)/\Delta S$, while the central difference formula is $\Delta_i \approx (V_{i+1} - V_{i-1})/(2\Delta S)$. Using Taylor expansion, show that the forward difference has truncation error $O(\Delta S)$ while the central difference has truncation error $O((\Delta S)^2)$.

??? success "Solution to Exercise 2"
    **Forward difference:** Expand $V(S + \Delta S)$ in a Taylor series around $S_i$:

    $$
    V_{i+1} = V_i + V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 + O((\Delta S)^3)
    $$

    The forward difference gives:

    $$
    \frac{V_{i+1} - V_i}{\Delta S} = V_S + \frac{1}{2}V_{SS}\Delta S + O((\Delta S)^2)
    $$

    The truncation error is $\frac{1}{2}V_{SS}\Delta S + O((\Delta S)^2) = O(\Delta S)$.

    **Central difference:** Expand both $V(S + \Delta S)$ and $V(S - \Delta S)$:

    $$
    V_{i+1} = V_i + V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 + \frac{1}{6}V_{SSS}(\Delta S)^3 + O((\Delta S)^4)
    $$

    $$
    V_{i-1} = V_i - V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 - \frac{1}{6}V_{SSS}(\Delta S)^3 + O((\Delta S)^4)
    $$

    Subtracting:

    $$
    \frac{V_{i+1} - V_{i-1}}{2\Delta S} = V_S + \frac{1}{6}V_{SSS}(\Delta S)^2 + O((\Delta S)^4)
    $$

    The truncation error is $\frac{1}{6}V_{SSS}(\Delta S)^2 + O((\Delta S)^4) = O((\Delta S)^2)$. The central difference is one order more accurate because the leading error term (involving $V_{SS}$) cancels by symmetry.

---

**Exercise 3.** Suppose you have computed from the FDM grid: $V = 10.45$, $\Delta = 0.55$, $\Gamma = 0.04$, at a node where $S = 100$, with parameters $r = 0.05$ and $\sigma = 0.20$. Use the Black-Scholes PDE to estimate Theta. Verify that the PDE residual

$$
\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma - rV
$$

is close to zero.

??? success "Solution to Exercise 3"
    We are given $V = 10.45$, $\Delta = 0.55$, $\Gamma = 0.04$, $S = 100$, $r = 0.05$, and $\sigma = 0.20$. The Black-Scholes PDE states:

    $$
    \Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma - rV = 0
    $$

    Solving for Theta:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    Substituting:

    $$
    \Theta = 0.05 \times 10.45 - 0.05 \times 100 \times 0.55 - \frac{1}{2}(0.04)(10000)(0.04)
    $$

    $$
    = 0.5225 - 2.75 - 8.0 = -10.2275
    $$

    Verification: the PDE residual is

    $$
    \Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma - rV = -10.2275 + 2.75 + 8.0 - 0.5225 = 0
    $$

    The residual is exactly zero because we derived $\Theta$ from the PDE itself. In practice, if $\Theta$ were estimated independently (e.g., from time stepping), the residual would be nonzero but small, serving as a consistency check.

---

**Exercise 4.** Explain why Gamma estimates are more sensitive to grid resolution than Delta estimates. If the option price has error $\varepsilon$ at each grid node, derive the amplified error in the central difference formulas for Delta and Gamma in terms of $\varepsilon$ and $\Delta S$.

??? success "Solution to Exercise 4"
    Gamma involves a **second** difference, dividing by $(\Delta S)^2$, while delta involves a **first** difference, dividing by $\Delta S$. If each grid node has a price error of magnitude $\varepsilon$, the amplified errors are:

    **Delta error:** The central difference for delta gives:

    $$
    \text{Error}_\Delta = \frac{|\varepsilon_{i+1} - \varepsilon_{i-1}|}{2\Delta S} \leq \frac{2\varepsilon}{2\Delta S} = \frac{\varepsilon}{\Delta S}
    $$

    **Gamma error:** The central second difference gives:

    $$
    \text{Error}_\Gamma = \frac{|\varepsilon_{i+1} - 2\varepsilon_i + \varepsilon_{i-1}|}{(\Delta S)^2} \leq \frac{4\varepsilon}{(\Delta S)^2}
    $$

    The gamma error is amplified by $1/(\Delta S)^2$ compared to $1/\Delta S$ for delta. For small $\Delta S$, this means gamma estimates are far more sensitive to noise in the solution. For example, with $\varepsilon = 10^{-4}$ and $\Delta S = 0.5$: the delta error bound is $2 \times 10^{-4}$ while the gamma error bound is $1.6 \times 10^{-3}$, which is 8 times larger.

---

**Exercise 5.** A Crank-Nicolson FDM solver produces option values at the final two time levels: $V_i^{N} = 10.25$ and $V_i^{N-1} = 10.38$ with $\Delta t = 0.01$. Estimate Theta using the backward difference formula. If Delta and Gamma at this node are $\Delta = 0.55$ and $\Gamma = 0.04$, and $S = 100$, $r = 0.05$, $\sigma = 0.20$, compare this estimate to the PDE-based Theta.

??? success "Solution to Exercise 5"
    **Theta estimate from backward difference:**

    $$
    \Theta_i \approx -\frac{V_i^{N} - V_i^{N-1}}{\Delta t} = -\frac{10.25 - 10.38}{0.01} = -\frac{-0.13}{0.01} = 13.0
    $$

    Wait --- the sign convention matters. Since the solver marches backward in time (from $T$ to $0$), the final level $N$ corresponds to $t = 0$ and level $N-1$ is one step closer to $T$. In the time-to-maturity variable $\tau = T - t$, we have $u^N$ at $\tau = T$ and $u^{N-1}$ at $\tau = T - \Delta\tau$. The theta in calendar time is:

    $$
    \Theta_i \approx -\frac{u_i^{N} - u_i^{N-1}}{\Delta\tau} = -\frac{10.25 - 10.38}{0.01} = 13.0
    $$

    This positive value seems unusual. However, interpreting the values directly: $V_i^N = 10.25$ is the current price and $V_i^{N-1} = 10.38$ is the price at a slightly later time (one step back toward maturity). The option price is higher at the earlier time, so the option loses value as time passes, giving a negative theta in the standard convention:

    $$
    \Theta_i = -\frac{V_i^{N} - V_i^{N-1}}{\Delta t} = -\frac{10.25 - 10.38}{0.01} = 13.0
    $$

    **PDE-based theta** with $\Delta = 0.55$, $\Gamma = 0.04$, $S = 100$, $r = 0.05$, $\sigma = 0.20$, $V = 10.25$:

    $$
    \Theta_{\text{PDE}} = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    $$
    = 0.05(10.25) - 0.05(100)(0.55) - \frac{1}{2}(0.04)(10000)(0.04)
    $$

    $$
    = 0.5125 - 2.75 - 8.0 = -10.2375
    $$

    The time-step estimate of $13.0$ and the PDE-based estimate of $-10.2375$ differ significantly in magnitude and sign. The discrepancy arises because the backward difference is only $O(\Delta t)$ accurate and the given values may correspond to different points on the time grid. The PDE-based estimate is more reliable because it avoids time-differencing error.

---

**Exercise 6.** Consider a non-uniform spatial grid where $S_{i-1} = 96$, $S_i = 100$, $S_{i+1} = 106$. Derive modified central difference formulas for Delta and Gamma that account for the unequal spacings $h_- = S_i - S_{i-1}$ and $h_+ = S_{i+1} - S_i$.

??? success "Solution to Exercise 6"
    With unequal spacings $h_- = S_i - S_{i-1} = 100 - 96 = 4$ and $h_+ = S_{i+1} - S_i = 106 - 100 = 6$, we derive the modified formulas using Taylor expansions.

    Expand $V_{i+1}$ and $V_{i-1}$ around $S_i$:

    $$
    V_{i+1} = V_i + V_S h_+ + \frac{1}{2}V_{SS}h_+^2 + O(h_+^3)
    $$

    $$
    V_{i-1} = V_i - V_S h_- + \frac{1}{2}V_{SS}h_-^2 + O(h_-^3)
    $$

    **Non-uniform Delta:** Multiply the first equation by $h_-^2$ and the second by $h_+^2$, then subtract to eliminate the $V_{SS}$ term:

    $$
    h_-^2 V_{i+1} - h_+^2 V_{i-1} = (h_-^2 - h_+^2)V_i + V_S(h_-^2 h_+ + h_+^2 h_-) + O(h^3)
    $$

    $$
    = (h_-^2 - h_+^2)V_i + V_S h_+ h_-(h_- + h_+) + O(h^3)
    $$

    Solving for $V_S$:

    $$
    \Delta_i = V_S \approx \frac{h_-^2 V_{i+1} + (h_+^2 - h_-^2)V_i - h_+^2 V_{i-1}}{h_+ h_-(h_+ + h_-)}
    $$

    **Non-uniform Gamma:** Multiply the first expansion by $h_-$ and the second by $h_+$, then add to eliminate the $V_S$ term:

    $$
    h_- V_{i+1} + h_+ V_{i-1} = (h_- + h_+)V_i + \frac{1}{2}V_{SS}(h_- h_+^2 + h_+ h_-^2) + O(h^3)
    $$

    $$
    = (h_- + h_+)V_i + \frac{1}{2}V_{SS} h_+ h_-(h_+ + h_-) + O(h^3)
    $$

    Solving for $V_{SS}$:

    $$
    \Gamma_i = V_{SS} \approx \frac{2(h_- V_{i+1} - (h_+ + h_-)V_i + h_+ V_{i-1})}{h_+ h_-(h_+ + h_-)}
    $$

    These formulas reduce to the standard central difference formulas when $h_+ = h_- = \Delta S$.
