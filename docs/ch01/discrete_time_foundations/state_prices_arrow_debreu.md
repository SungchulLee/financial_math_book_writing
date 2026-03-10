# Arrow-Debreu Securities and State Prices

Arrow-Debreu securities isolate individual states of the world, providing elementary building blocks from which any financial claim can be constructed and priced.

## Definition

An **Arrow-Debreu security** for state $s$ pays \$1 if state $\omega_s$ occurs and \$0 otherwise. Its payoff is the standard basis vector $\mathbf{e}_s \in \mathbb{R}^S$. The **state price** $\phi_s > 0$ is the time-0 cost of the Arrow-Debreu security for state $s$.

Any payoff $(X_1, \ldots, X_S)$ is priced by the **fundamental pricing equation**

$$
V_0 = \sum_{s=1}^{S} \phi_s\, X_s = \boldsymbol{\phi}^\top \mathbf{X}
$$

State prices relate to **risk-neutral probabilities** and the **stochastic discount factor** via

$$
\phi_s = \frac{q_s}{1 + r_f} = p_s \cdot m_s
$$

where $q_s = \phi_s(1 + r_f)$ are the risk-neutral probabilities and $m_s = \phi_s / p_s$ is the pricing kernel.

## Explanation

The First Fundamental Theorem of Asset Pricing states that the market is arbitrage-free if and only if strictly positive state prices exist. The Second Fundamental Theorem states that the market is complete if and only if the state prices are unique.

The sum of all state prices equals the discount factor: $\sum_s \phi_s = 1/(1+r_f)$. Risk-neutral probabilities overweight bad states (where marginal utility is high) relative to physical probabilities, reflecting aggregate risk aversion.

In continuous-state settings, the **Breeden-Litzenberger formula** extracts the state price density from European call prices:

$$
\phi(K) = e^{r_f T}\,\frac{\partial^2 C}{\partial K^2}\bigg|_{K}
$$

This connects the curvature of the call price function to the risk-neutral density, providing a bridge between theory and market observables.

## Examples

Extract state prices from a two-asset economy and price a derivative.

```python
import numpy as np

# Two states: Boom, Recession
# Two assets: bond (pays 1 in both), stock
X = np.array([
    [1.0, 1.0],
    [70, 40],
])
P = np.array([0.95, 50])

# State prices
phi = np.linalg.solve(X, P)
print(f"State prices: phi_boom={phi[0]:.4f}, phi_rec={phi[1]:.4f}")
print(f"Sum of state prices: {sum(phi):.4f} (= discount factor)")

# Risk-free rate
rf = 1 / sum(phi) - 1
print(f"Risk-free rate: {rf:.4f}")

# Risk-neutral probabilities
q = phi * (1 + rf)
print(f"Risk-neutral probs: q_boom={q[0]:.4f}, q_rec={q[1]:.4f}")

# Stochastic discount factor (assume physical probs)
p = np.array([0.6, 0.4])  # physical probabilities
m = phi / p
print(f"SDF: m_boom={m[0]:.4f}, m_rec={m[1]:.4f}")

# Price a put with strike 55
put_payoff = np.array([max(55 - 70, 0), max(55 - 40, 0)])
put_price = phi @ put_payoff
print(f"\nPut(K=55) payoffs: {put_payoff}")
print(f"Put price (state prices): {put_price:.4f}")
print(f"Put price (risk-neutral): {(q @ put_payoff) / (1+rf):.4f}")
print(f"Put price (SDF):          {p @ (m * put_payoff):.4f}")
```
