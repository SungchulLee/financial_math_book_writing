# Greeks (Basic)

## Background

Black Scholes Greeks

Educational script demonstrating black scholes greeks concepts.

---

## Code

```python
"""
Black Scholes Greeks

Educational script demonstrating black scholes greeks concepts.
"""

# ============================================================================
# black_scholes_GREEKS.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

# Parameters


if __name__ == "__main__":
    S = np.array(range(50,151),dtype=np.int64) # underlying prices
    K = 100                                    # strike price
    T = 1.0                                    # time to maturity (in years)
    r = 0.05                                   # risk-free interest rate
    sigma = 0.2                                # volatility

    # Plotting
    fig, axes = plt.subplots(5,1, figsize=(6, 10), constrained_layout=True)

    # Delta: price sensitivity to underlying price change
    delta_call, delta_put = bs.delta(S, K, T, r, sigma)
    axes[0].plot(S, delta_call, label="Call", color="blue", lw=5, alpha=0.3)
    axes[0].plot(S, delta_put, label="Put", color="red")
    axes[0].set_title("Delta")

    # Gamma: delta sensitivity to underlying price change (same for calls and puts)
    gamma_call_and_put = bs.gamma(S, K, T, r, sigma)
    axes[1].plot(S, gamma_call_and_put, color="blue", lw=5, alpha=0.3)
    axes[1].set_title("Gamma")

    # Vega: price sensitivity to volatility change (same for calls and puts)
    vega_call_and_put = bs.vega(S, K, T, r, sigma)
    axes[2].plot(S, vega_call_and_put, color="blue", lw=5, alpha=0.3)
    axes[2].set_title("Vega")

    # Theta: price sensitivity to time decay
    theta_call, theta_put = bs.theta(S, K, T, r, sigma)
    axes[3].plot(S, theta_call, label="Call", color="blue", lw=5, alpha=0.3)
    axes[3].plot(S, theta_put, label="Put", color="red")
    axes[3].set_title("Theta")

    # Rho: price sensitivity to interest rate change
    rho_call, rho_put = bs.rho(S, K, T, r, sigma)
    axes[4].plot(S, rho_call, label="Call", color="blue", lw=5, alpha=0.3)
    axes[4].plot(S, rho_put, label="Put", color="red")
    axes[4].set_title("Rho")

    for i, ax in enumerate(axes):
        for spine in ["top","right"]:
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_position(("data", 100))
        ax.set_xlabel("Underlying Price $S$")
        ax.set_ylabel("Value")
        ax.grid(False)
        if i not in {1,2}:
            ax.legend()

    plt.show()
```


## Exercises

**Exercise 1.**
For an ATM call ($S = K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.2$), compute delta. Explain why ATM delta is approximately 0.5 but not exactly 0.5.

??? success "Solution to Exercise 1"
    $d_1 = (0 + 0.07)/0.2 = 0.35$. Delta $= N(0.35) = 0.6368$. It exceeds 0.5 because the drift term $(r + \sigma^2/2)T > 0$ shifts $d_1$ above zero, making it more likely the call finishes ITM. For $r = 0$ and $\sigma \to 0$, delta approaches exactly 0.5 for ATM options.

---

**Exercise 2.**
Gamma is the same for calls and puts. Prove this using put-call parity: $C - P = S - Ke^{-rT}$.

??? success "Solution to Exercise 2"
    Differentiating twice with respect to $S$: $\frac{\partial^2 C}{\partial S^2} - \frac{\partial^2 P}{\partial S^2} = \frac{\partial^2}{\partial S^2}(S - Ke^{-rT}) = 0$. Therefore $\Gamma_{\text{call}} = \Gamma_{\text{put}}$. Similarly, vega is the same since $\frac{\partial}{\partial \sigma}(S - Ke^{-rT}) = 0$.

---

**Exercise 3.**
Theta for an ATM call is always negative. Compute theta for $S = K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.2$ and express it per calendar day.

??? success "Solution to Exercise 3"
    $\Theta_{\text{call}} = -\frac{S \cdot n(d_1) \cdot \sigma}{2\sqrt{T}} - rKe^{-rT}N(d_2) = -\frac{100 \cdot 0.3752 \cdot 0.2}{2} - 0.05 \cdot 95.12 \cdot 0.5596 = -3.752 - 2.663 = -6.415$ per year. Per day: $-6.415/365 = -\$0.0176$. The option loses about 1.8 cents per day.

---

**Exercise 4.**
Explain the relationship between gamma and theta: long gamma positions have negative theta, and vice versa. Why is this a fundamental tradeoff?

??? success "Solution to Exercise 4"
    From the BS PDE: $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma + rS\Delta - rV = 0$. For a delta-neutral portfolio ($\Delta = 0$): $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma + rV$. When gamma is large and positive, theta must be large and negative to satisfy the PDE. This is the gamma-theta tradeoff: buying options (long gamma) costs time decay (negative theta). Selling options earns theta but bears gamma risk from large moves.