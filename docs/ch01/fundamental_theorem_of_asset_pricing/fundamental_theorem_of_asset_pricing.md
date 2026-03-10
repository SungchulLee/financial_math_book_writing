# The Fundamental Theorem of Asset Pricing

The FTAP is the cornerstone of mathematical finance, establishing that a market is arbitrage-free if and only if an equivalent martingale measure exists, and complete if and only if that measure is unique.

## Definition

Consider $d+1$ assets with price processes $S^0_t, \ldots, S^d_t$ on a filtered probability space $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$. Let $\tilde{S}^i_t = S^i_t / S^0_t$ denote discounted prices. An **equivalent martingale measure (EMM)** is $\mathbb{Q} \sim \mathbb{P}$ under which all $\tilde{S}^i_t$ are martingales.

**First FTAP.** The market is arbitrage-free if and only if there exists an EMM $\mathbb{Q}$.

**Second FTAP.** Assuming no arbitrage, the market is complete if and only if $\mathbb{Q}$ is unique.

In continuous time, the condition strengthens to **No Free Lunch with Vanishing Risk (NFLVR)**, and $\mathbb{Q}$ becomes an equivalent local martingale measure (Delbaen-Schachermayer, 1994).

## Explanation

**Proof of First FTAP (finite case).** In a one-period model with states $\omega_1, \ldots, \omega_n$ and excess return matrix $X \in \mathbb{R}^{n \times d}$, no-arbitrage means $\{X\theta : \theta \in \mathbb{R}^d\} \cap \mathbb{R}^n_{++} = \emptyset$. By the separating hyperplane theorem, there exists $q \in \mathbb{R}^n$ with $q_i > 0$ and $X^\top q = 0$. After normalization, $q$ defines the EMM.

Conversely, if an EMM exists with weights $q_i > 0$ and $X^\top q = 0$, then for any $\theta$ with $X\theta \geq 0$: $0 = q^\top(X\theta) = \sum_i q_i (X\theta)_i \geq 0$, forcing $X\theta = 0$. No arbitrage.

**Proof of Second FTAP.** Completeness means $\operatorname{rank}(X) = n-1$, so $\ker(X^\top)$ is one-dimensional and intersects the probability simplex in exactly one point: the unique EMM. Conversely, uniqueness of $\mathbb{Q}$ forces $\dim(\ker(X^\top)) = 1$, giving full rank and completeness.

**Economic interpretation.** The EMM $\mathbb{Q}$ absorbs all risk preferences into the measure change from $\mathbb{P}$, so pricing reduces to computing expectations. In the Black-Scholes model, the Girsanov measure change $d\mathbb{Q}/d\mathbb{P} = \mathcal{E}(-\int_0^T \lambda_s\, dW_s)$ with market price of risk $\lambda_t = (\mu_t - r)/\sigma_t$ provides the explicit construction.

## Examples

Verify the FTAP in a one-period model: extract the EMM, confirm the martingale property, and price a derivative.

```python
import numpy as np

# 3 states, 2 risky assets + 1 risk-free
# Excess return matrix (discounted gains)
S0 = np.array([100, 50])  # initial prices of risky assets
R = np.array([
    [120, 70],    # state 1 payoffs
    [100, 50],    # state 2 payoffs
    [80,  40],    # state 3 payoffs
])
rf = 0.05
X = R - S0 * (1 + rf)  # excess returns

# Find EMM: X^T q = 0, q >= 0, sum(q) = 1
# Null space of X^T
from scipy.linalg import null_space
ns = null_space(X.T)
print(f"Null space dimension: {ns.shape[1]}")

# Find q in null space that is a valid probability
q_raw = ns[:, 0]
if np.any(q_raw < 0):
    q_raw = -q_raw  # flip sign if needed
q = q_raw / q_raw.sum()
print(f"EMM: q = {q}")
print(f"All positive: {np.all(q > 0)}")

# Verify martingale property
for j in range(2):
    E_S = q @ R[:, j]
    print(f"Asset {j+1}: E^Q[S] = {E_S:.4f}, S0*(1+r) = {S0[j]*(1+rf):.4f}")

# Price a call on asset 1 with strike 105
call_payoff = np.maximum(R[:, 0] - 105, 0)
call_price = q @ call_payoff / (1 + rf)
print(f"\nCall(K=105) price: {call_price:.4f}")
```
