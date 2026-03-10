# Arbitrage and Dominance

Arbitrage and dominance principles provide the foundational constraints on asset prices, establishing that in well-functioning markets, no riskless profit opportunities can persist.

## Definition

A portfolio $\boldsymbol{\theta} = (\theta_1, \ldots, \theta_N)^\top$ is an **arbitrage** if

$$
\boldsymbol{\theta}^\top \mathbf{P} \leq 0, \quad \mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}, \quad \text{and} \quad \mathbf{X}^\top \boldsymbol{\theta} \neq \mathbf{0}
$$

That is, the portfolio has zero or negative initial cost, non-negative payoff in all states, and strictly positive payoff in at least one state. An asset $A$ **dominates** asset $B$ if $A$ costs no more than $B$ and pays at least as much in every state, with strict inequality in at least one state.

## Explanation

The **no-arbitrage principle** asserts that arbitrage opportunities cannot persist in equilibrium. This seemingly simple condition has powerful consequences: it implies the existence of positive state prices $\boldsymbol{\phi} \gg 0$ such that $\mathbf{P} = \mathbf{X}\boldsymbol{\phi}$, which is the First Fundamental Theorem of Asset Pricing in the finite-state setting.

Dominance is a weaker but practically useful notion. The **law of one price** states that two portfolios with identical payoffs must have the same price. Dominance extends this: if portfolio $A$ pays at least as much as $B$ in every state, then $A$ must cost at least as much as $B$. Violations of dominance are a special case of arbitrage.

These principles yield model-free bounds on derivative prices. For example, a call option must satisfy $\max(S_0 - Ke^{-rT}, 0) \leq C \leq S_0$, which follows purely from no-arbitrage without any distributional assumptions.

## Examples

Check no-arbitrage in a three-asset, two-state economy and derive call option bounds.

```python
import numpy as np

# Payoff matrix: 3 assets, 2 states
X = np.array([
    [1.0, 1.0],    # risk-free bond
    [120, 80],      # stock
    [20, 0],        # call option
])
P = np.array([0.95, 100, 8])  # prices

# Check for state prices: X @ phi = P
# Solve with first two assets, verify third
X_sub = X[:2, :]
phi = np.linalg.solve(X_sub, P[:2])
print(f"State prices: phi = {phi}")
print(f"Both positive: {np.all(phi > 0)} => no-arbitrage holds")

# Verify call price is consistent
call_price_implied = X[2, :] @ phi
print(f"Implied call price: {call_price_implied:.4f}")
print(f"Market call price:  {P[2]:.4f}")
print(f"Arbitrage exists: {abs(call_price_implied - P[2]) > 1e-10}")

# Model-free call bounds
S0, K, r, T = 100, 100, 1/0.95 - 1, 1.0
lower = max(S0 - K / (1 + r), 0)
upper = S0
print(f"\nCall bounds: {lower:.2f} <= C <= {upper:.2f}")
```
