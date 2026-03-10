# Finite Market Examples

Concrete finite-state economies illustrate how state prices, risk-neutral measures, and the FTAP work in practice, making the abstract theory tangible.

## Definition

A **finite market** consists of $N$ assets and $S$ states with payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$ and price vector $\mathbf{P} \in \mathbb{R}^N$. State prices $\boldsymbol{\phi} \in \mathbb{R}^S$ solve

$$
\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}
$$

The market is arbitrage-free if and only if $\boldsymbol{\phi} \gg 0$ exists. It is complete if and only if $\operatorname{rank}(\mathbf{X}) = S$, making $\boldsymbol{\phi}$ unique.

## Explanation

In a two-state economy with a bond and stock, the system $\mathbf{X}\boldsymbol{\phi} = \mathbf{P}$ is $2 \times 2$ and yields unique state prices directly. Adding a third asset creates an overdetermined system; consistency requires the third asset's price to match $\boldsymbol{\phi}^\top \mathbf{X}_3$. Any discrepancy signals arbitrage.

In a three-state economy with only two assets, the system is underdetermined and state prices are not unique. The set of valid state price vectors forms a line segment (or higher-dimensional region), producing a range of no-arbitrage prices for non-redundant claims.

These examples connect the algebraic theory to practical questions: given observed prices, one can extract state prices, detect arbitrage, and price derivatives.

## Examples

```python
import numpy as np

# Example 1: Two states, three assets (check for arbitrage)
X = np.array([
    [1.0, 1.0],    # bond
    [120, 80],      # stock
    [20,  0],       # call (K=100)
])
P = np.array([0.95, 100, 8.0])

# Solve with first two assets
phi = np.linalg.solve(X[:2], P[:2])
print("Example 1: Two-state economy")
print(f"  State prices: {phi}")
call_fair = X[2] @ phi
print(f"  Fair call price: {call_fair:.4f}, market: {P[2]:.4f}")
print(f"  Arbitrage: {'YES' if abs(call_fair - P[2]) > 1e-8 else 'NO'}")

# Example 2: Three states, two assets (incomplete market)
print("\nExample 2: Three-state economy (incomplete)")
X2 = np.array([
    [1.0, 1.0, 1.0],
    [140, 100, 70],
])
P2 = np.array([0.95, 100])

# Parameterize state prices: phi = phi_particular + t * phi_null
# Particular solution via pseudoinverse
phi_part = X2.T @ np.linalg.solve(X2 @ X2.T, P2)
# Null space
U, s, Vt = np.linalg.svd(X2)
phi_null = Vt[-1]  # last row of V^T

# Find range of t for phi > 0
print(f"  Particular solution: {phi_part}")
print(f"  Null space direction: {phi_null}")

# Price a digital on state 1
digital = np.array([1, 0, 0])
price_part = digital @ phi_part
price_null = digital @ phi_null
print(f"  Digital price = {price_part:.4f} + t * {price_null:.4f}")
```
