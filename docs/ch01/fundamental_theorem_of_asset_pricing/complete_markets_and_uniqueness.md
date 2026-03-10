# Complete Markets and Uniqueness

Market completeness determines whether every contingent claim has a unique no-arbitrage price, and it is equivalent to uniqueness of the equivalent martingale measure.

## Definition

A market is **complete** if every $\mathcal{F}_T$-measurable contingent claim can be replicated by an admissible self-financing trading strategy. In the finite-state model with $n$ states and payoff matrix $X \in \mathbb{R}^{n \times d}$, completeness requires $\operatorname{rank}(X) = n - 1$ (when a risk-free asset is included).

The **Second Fundamental Theorem of Asset Pricing** states: assuming no arbitrage, the market is complete if and only if the equivalent martingale measure $\mathbb{Q}$ is **unique**.

## Explanation

When the EMM is unique, every contingent claim has exactly one arbitrage-free price given by $V_0 = \mathbb{E}^{\mathbb{Q}}[\Phi_T / S^0_T]$. The replicating portfolio provides a perfect hedge.

When multiple EMMs exist (incomplete market), a contingent claim $\Phi$ that is not replicable has a range of no-arbitrage prices:

$$
\inf_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi_T / S^0_T] \leq V_0 \leq \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi_T / S^0_T]
$$

The bounds correspond to the sub-replication and super-replication prices. Additional criteria (utility maximization, minimum entropy) are needed to select a specific price within this interval.

In the finite model with $n$ states, completeness requires at least $n - 1$ independent risky assets. The binomial model ($n = 2$ states, $d = 1$ risky asset) is exactly complete. The trinomial model ($n = 3$ states, $d = 1$ risky asset) is incomplete.

## Examples

Demonstrate completeness in a two-state model and incompleteness in a three-state model.

```python
import numpy as np
from scipy.optimize import linprog

# Complete market: 2 states, 2 assets (bond + stock)
X_complete = np.array([
    [1.0, 1.0],   # bond
    [120, 80],     # stock
])
P_complete = np.array([0.95, 100])
phi = np.linalg.solve(X_complete, P_complete)
print(f"Complete market: unique state prices = {phi}")

# Price any claim uniquely
claim = np.array([25, 5])  # arbitrary payoff
print(f"Unique claim price: {phi @ claim:.4f}")

# Incomplete market: 3 states, 2 assets
X_incomplete = np.array([
    [1.0, 1.0, 1.0],   # bond
    [130, 100, 70],     # stock
])
P_incomplete = np.array([0.95, 100])
claim_3 = np.array([30, 0, 0])  # digital on state 1

# Find price range via linear programming
A_eq = X_incomplete
b_eq = P_incomplete
for direction, label in [(claim_3, "min"), (-claim_3, "max")]:
    res = linprog(direction, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(1e-10, None)]*3, method='highs')
    price = res.fun if label == "min" else -res.fun
    print(f"Incomplete market claim price ({label}): {price:.4f}")
```
