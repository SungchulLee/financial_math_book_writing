# Separating Hyperplane Theorem

The separating hyperplane theorem states that two disjoint convex sets can be separated by a hyperplane, providing the mathematical engine behind the proof of the Fundamental Theorem of Asset Pricing.

## Definition

**Weak separation.** Let $C, D \subset \mathbb{R}^n$ be non-empty disjoint convex sets. There exists a non-zero $p \in \mathbb{R}^n$ and $\alpha \in \mathbb{R}$ such that

$$
p^\top x \leq \alpha \leq p^\top y \quad \text{for all } x \in C,\; y \in D
$$

**Strict separation.** If $C$ is closed and $D$ is compact with $C \cap D = \emptyset$, then there exist $\alpha < \beta$ with

$$
p^\top x \leq \alpha < \beta \leq p^\top y \quad \text{for all } x \in C,\; y \in D
$$

## Explanation

The proof of strict separation proceeds by reducing to the separation of a point from a closed convex set. Form the Minkowski difference $E = C - D$, which is closed and convex with $0 \notin E$. The nearest point $x_0 \in E$ to the origin defines the separating direction $p = -x_0$, and the optimality condition $(x_0)^\top(e - x_0) \geq 0$ for all $e \in E$ yields the separation inequality.

**Connection to the FTAP.** In the finite-state model, no-arbitrage means the attainable payoff subspace $\mathcal{V} = \operatorname{Im}(X)$ is disjoint from the positive orthant $\mathbb{R}^n_{++}$. The separating hyperplane normal $q$ satisfies $X^\top q = 0$ (orthogonal to $\mathcal{V}$) with $q_i > 0$ (positive on $\mathbb{R}^n_{++}$). After normalization, $q$ becomes the EMM.

Related results include **Farkas' lemma** (the linear programming dual), **Minkowski's theorem** (separation via relative interiors), and in infinite dimensions, the **Hahn-Banach theorem** and the **Kreps-Yan theorem** used in the continuous-time FTAP.

## Examples

Illustrate separation in two dimensions and construct an EMM from the separating vector.

```python
import numpy as np

# FTAP application: 2 risky assets, 3 states
# Excess return matrix
X = np.array([
    [15, 20],     # state 1
    [-5, 0],      # state 2
    [-10, -15],   # state 3
])

# Find q in ker(X^T) with q > 0
from scipy.linalg import null_space
ns = null_space(X.T)
q_raw = ns[:, 0]
if np.min(q_raw) < 0:
    q_raw = -q_raw
q = q_raw / q_raw.sum()

print(f"Separating vector (EMM): q = {q}")
print(f"All positive: {np.all(q > 0)}")
print(f"X^T q = {X.T @ q}")

# Verify: no portfolio has non-negative payoff in all states
# Random test
np.random.seed(42)
for _ in range(10000):
    theta = np.random.randn(2)
    payoff = X @ theta
    if np.all(payoff >= 0) and np.any(payoff > 0):
        print("Arbitrage found!")
        break
else:
    print("No arbitrage found (consistent with FTAP)")
```
