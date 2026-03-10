# Delta Hedging

Delta hedging prices derivatives by combining an option with stock to eliminate risk, then applying the no-arbitrage principle that any risk-free portfolio must earn the risk-free rate.

## Definition

In the one-period binomial model, the **hedge ratio** (delta) for a contingent claim with payoffs $H_u$ (up) and $H_d$ (down) is

$$
\Delta = \frac{H_u - H_d}{(u - d)S_0}
$$

The portfolio $\Pi = \Delta S - V$ (long $\Delta$ shares, short 1 option) has the same terminal value in both states:

$$
\Pi_{\Delta t} = \frac{dH_u - uH_d}{u - d}
$$

Applying the no-arbitrage condition $\Pi_{\Delta t} = \Pi_0 \cdot e^{r\Delta t}$ and solving for the option price yields

$$
V_0 = e^{-r\Delta t}\bigl[q\,H_u + (1-q)\,H_d\bigr]
$$

where $q = (e^{r\Delta t} - d)/(u - d)$ is the risk-neutral probability that **emerges** from the hedging argument.

## Explanation

The key insight is that the hedge eliminates risk in **both** states, so the actual probability $p$ of an up move never enters the calculation. Prices are determined by what can be hedged, not by beliefs about probabilities.

Delta measures the option's sensitivity to stock price changes. In the discrete model, $\Delta = (H_u - H_d)/((u-d)S_0)$; in continuous time, this becomes $\partial V/\partial S$. For a call, $0 < \Delta < 1$ (the option gains when the stock rises). For a put, $-1 < \Delta < 0$ (the option gains when the stock falls).

The hedging approach is equivalent to the replication approach: both use the same $\Delta$, both apply no-arbitrage, and both yield the same pricing formula. Hedging asks "what portfolio eliminates risk?" while replication asks "what portfolio matches the payoff?"

## Examples

Price a European call with strike \$105 on a stock at \$100, with $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$ year.

```python
import numpy as np

S0, K, r, dt = 100, 105, 0.05, 1.0
u, d = 1.2, 0.9

# Payoffs
H_u = max(u * S0 - K, 0)  # 15
H_d = max(d * S0 - K, 0)  # 0

# Hedge ratio
delta = (H_u - H_d) / ((u - d) * S0)
print(f"Delta = {delta:.4f}")

# Risk-free portfolio terminal value (same in both states)
Pi_T = (d * H_u - u * H_d) / (u - d)
print(f"Hedged portfolio terminal value = {Pi_T:.2f}")

# No-arbitrage: risk-free portfolio earns r
Pi_0 = np.exp(-r * dt) * Pi_T
V0 = delta * S0 - Pi_0
print(f"Option price (via hedging) = {V0:.4f}")

# Verify: risk-neutral pricing gives same answer
q = (np.exp(r * dt) - d) / (u - d)
V0_rn = np.exp(-r * dt) * (q * H_u + (1 - q) * H_d)
print(f"Option price (risk-neutral) = {V0_rn:.4f}")

# Verify hedged portfolio earns risk-free rate
Pi_up = delta * u * S0 - H_u
Pi_dn = delta * d * S0 - H_d
print(f"Terminal value (up):   {Pi_up:.2f}")
print(f"Terminal value (down): {Pi_dn:.2f}")
print(f"Return: {Pi_up / Pi_0:.6f} vs e^r = {np.exp(r * dt):.6f}")
```
