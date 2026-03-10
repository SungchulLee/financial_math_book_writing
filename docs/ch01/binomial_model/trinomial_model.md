# Trinomial Model

The trinomial model allows three possible stock price movements per period, illustrating market incompleteness where the risk-neutral measure is no longer unique.

## Definition

At each time step, the stock price moves to one of three values:

$$
S_{\Delta t} \in \{uS_0,\; mS_0,\; dS_0\}
$$

where $u > m > d > 0$. With two traded assets (stock and bond) and three states, the replication system has three equations but only two unknowns $(\Delta, B)$. In general, no portfolio of stock and bond can replicate an arbitrary three-state payoff.

A risk-neutral measure $\mathbb{Q}$ assigns probabilities $(q_u, q_m, q_d)$ with $q_u + q_m + q_d = 1$ and the martingale condition

$$
q_u \cdot u + q_m \cdot m + q_d \cdot d = e^{r\Delta t}
$$

This is one equation in three unknowns (subject to positivity and summing to one), so the solution is not unique. The market is **incomplete**.

## Explanation

Incompleteness means that not every contingent claim can be replicated, and consequently there is no unique arbitrage-free price. Instead, no-arbitrage constrains prices to an interval: the **sub-replication price** (cheapest super-hedge from below) and the **super-replication price** (cheapest super-hedge from above) define bounds within which any consistent price must lie.

A common parameterization is $u = e^{\sigma\sqrt{2\Delta t}}$, $m = 1$, $d = e^{-\sigma\sqrt{2\Delta t}}$, which provides better convergence properties than the binomial model for certain payoffs. The trinomial tree can also be viewed as an explicit finite difference scheme for the Black-Scholes PDE.

Despite incompleteness, one can select a particular risk-neutral measure by imposing additional criteria (e.g., minimum entropy, variance optimality), leading to a unique price within the no-arbitrage bounds.

## Examples

Demonstrate non-uniqueness of the risk-neutral measure for the trinomial model and compute the pricing bounds for a call option.

```python
import numpy as np
from scipy.optimize import linprog

S0, K, r, sigma, dt = 100, 100, 0.05, 0.20, 1.0
u = np.exp(sigma * np.sqrt(2 * dt))
m = 1.0
d = np.exp(-sigma * np.sqrt(2 * dt))
disc = np.exp(-r * dt)

print(f"u={u:.4f}, m={m:.4f}, d={d:.4f}")

# Call payoffs in each state
H = np.array([max(u*S0 - K, 0), max(m*S0 - K, 0), max(d*S0 - K, 0)])
print(f"Payoffs: up={H[0]:.2f}, mid={H[1]:.2f}, down={H[2]:.2f}")

# Find min and max risk-neutral call price
# Variables: q_u, q_m, q_d >= 0
# Constraints: q_u + q_m + q_d = 1, u*q_u + m*q_m + d*q_d = exp(r*dt)
A_eq = np.array([[1, 1, 1], [u, m, d]])
b_eq = np.array([1, np.exp(r * dt)])

# Minimize discounted expected payoff
res_min = linprog(disc * H, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, 1)]*3, method='highs')
# Maximize (minimize negative)
res_max = linprog(-disc * H, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, 1)]*3, method='highs')

print(f"Price lower bound: {res_min.fun:.4f}")
print(f"Price upper bound: {-res_max.fun:.4f}")
print(f"Binomial-like midpoint: {(res_min.fun - res_max.fun)/2:.4f}")
```
