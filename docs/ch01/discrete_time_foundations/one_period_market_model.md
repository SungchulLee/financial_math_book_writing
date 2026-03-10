# One-Period Market Model

The one-period market model is the simplest framework for studying arbitrage-free pricing, where $N$ assets are traded today and deliver state-contingent payoffs at a single future date across $S$ possible states.

## Definition

A **one-period market** consists of time $t = 0$ (today) and $t = 1$ (future), with $S$ possible states $\omega_1, \ldots, \omega_S$ occurring with physical probabilities $p_s > 0$. There are $N$ traded assets with price vector $\mathbf{P} \in \mathbb{R}^N$ and payoff matrix

$$
\mathbf{X} \in \mathbb{R}^{N \times S}, \qquad X_{js} = \text{payoff of asset } j \text{ in state } s
$$

A **portfolio** $\boldsymbol{\theta} \in \mathbb{R}^N$ has initial cost $\boldsymbol{\theta}^\top \mathbf{P}$ and state-contingent payoff $\mathbf{X}^\top \boldsymbol{\theta} \in \mathbb{R}^S$.

## Explanation

The market is **arbitrage-free** if and only if there exist strictly positive state prices $\boldsymbol{\phi} \gg 0$ satisfying $\mathbf{P} = \mathbf{X}\boldsymbol{\phi}$ (First Fundamental Theorem). The market is **complete** if and only if every payoff $\mathbf{c} \in \mathbb{R}^S$ can be replicated, which requires $\operatorname{rank}(\mathbf{X}) = S$. Completeness is equivalent to uniqueness of the state price vector (Second Fundamental Theorem).

When a risk-free asset with return $R_f = 1 + r_f$ exists, the state prices can be re-expressed as risk-neutral probabilities $q_s = \phi_s R_f$, and every asset is priced by $P_j = R_f^{-1} \mathbb{E}^{\mathbb{Q}}[X_j]$.

## Examples

Construct a two-state, two-asset economy and extract state prices, risk-neutral probabilities, and price a derivative.

```python
import numpy as np

# Two states (Boom, Recession), two assets (bond, stock)
X = np.array([
    [1.0, 1.0],     # bond pays 1 in both states
    [130, 80],       # stock payoffs
])
P = np.array([0.95, 100])  # current prices

# Solve for state prices
phi = np.linalg.solve(X, P)
print(f"State prices: phi_boom={phi[0]:.4f}, phi_rec={phi[1]:.4f}")

# Risk-free rate and risk-neutral probabilities
Rf = 1 / sum(phi)
q = phi * Rf
print(f"Risk-free rate: {Rf - 1:.4f}")
print(f"Risk-neutral probs: q_boom={q[0]:.4f}, q_rec={q[1]:.4f}")

# Price a call with strike 100
call_payoff = np.array([max(130 - 100, 0), max(80 - 100, 0)])
call_price = phi @ call_payoff
print(f"Call price (state prices): {call_price:.4f}")
print(f"Call price (risk-neutral): {(q @ call_payoff) / Rf:.4f}")
```
