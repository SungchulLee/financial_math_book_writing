# Portfolios and Payoffs

Portfolios are linear combinations of traded assets, and their payoffs span a subspace of the full state space whose dimension determines market completeness.

## Definition

Given $N$ assets with payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$, a **portfolio** $\boldsymbol{\theta} \in \mathbb{R}^N$ specifies the number of units held in each asset. The portfolio has initial cost $\boldsymbol{\theta}^\top \mathbf{P}$ and generates the payoff vector

$$
\mathbf{c} = \mathbf{X}^\top \boldsymbol{\theta} \in \mathbb{R}^S
$$

The set of all attainable payoffs is the **marketed subspace** $\mathcal{M} = \{\mathbf{X}^\top \boldsymbol{\theta} : \boldsymbol{\theta} \in \mathbb{R}^N\} = \operatorname{Im}(\mathbf{X}^\top)$.

## Explanation

The marketed subspace $\mathcal{M}$ is a linear subspace of $\mathbb{R}^S$ with dimension $\operatorname{rank}(\mathbf{X})$. When $\operatorname{rank}(\mathbf{X}) = S$, every payoff in $\mathbb{R}^S$ is attainable and the market is **complete**. When $\operatorname{rank}(\mathbf{X}) < S$, some payoffs cannot be replicated and the market is **incomplete**.

A portfolio is **self-financing** if all rebalancing is funded entirely from the portfolio's current value, with no external cash injections or withdrawals. In the one-period model, self-financing is automatic since no rebalancing occurs.

Short selling ($\theta_j < 0$) is permitted, meaning investors can take negative positions. The **law of one price** requires that two portfolios with the same payoff must have the same cost: if $\mathbf{X}^\top \boldsymbol{\theta}_1 = \mathbf{X}^\top \boldsymbol{\theta}_2$, then $\boldsymbol{\theta}_1^\top \mathbf{P} = \boldsymbol{\theta}_2^\top \mathbf{P}$.

## Examples

Analyze the marketed subspace for a three-asset, three-state economy.

```python
import numpy as np

# 3 assets, 3 states
X = np.array([
    [1.0, 1.0, 1.0],    # risk-free bond
    [150, 100, 60],      # stock
    [50,   0,  0],       # call option
])
P = np.array([0.95, 100, 15])

rank = np.linalg.matrix_rank(X)
print(f"Payoff matrix rank: {rank}, States: {X.shape[1]}")
print(f"Market is {'complete' if rank == X.shape[1] else 'incomplete'}")

# Replicate a put with strike 100: payoff = (0, 0, 40)
target = np.array([0, 0, 40])
theta = np.linalg.solve(X.T, target)  # X^T theta = target
print(f"\nReplicating portfolio for put: {theta}")
print(f"Replication cost: {theta @ P:.4f}")
print(f"Payoff check: {X.T @ theta}")

# Verify law of one price
theta2 = theta + np.array([1, -1/50, 0])  # perturb
# This changes payoff, so not same claim -- demonstrate marketed subspace
payoff2 = X.T @ theta2
print(f"\nPerturbed portfolio payoff: {payoff2}")
```
