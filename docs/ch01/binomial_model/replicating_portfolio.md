# Replicating Portfolio

In a complete market, every contingent claim can be replicated by a portfolio of traded assets, and the replication cost is the unique no-arbitrage price of the claim.

## Definition

Given a contingent claim with payoffs $(H_u, H_d)$ in the one-period binomial model, the **replicating portfolio** $(\Delta, B)$ satisfies

$$
\Delta \cdot uS_0 + B \cdot e^{r\Delta t} = H_u, \qquad \Delta \cdot dS_0 + B \cdot e^{r\Delta t} = H_d
$$

Solving the $2 \times 2$ system yields

$$
\Delta = \frac{H_u - H_d}{(u - d)S_0}, \qquad B = e^{-r\Delta t}\!\left(\frac{uH_d - dH_u}{u - d}\right)
$$

The no-arbitrage price is $V_0 = \Delta S_0 + B$, which equals $e^{-r\Delta t}(qH_u + (1-q)H_d)$ where $q = (e^{r\Delta t} - d)/(u - d)$.

## Explanation

The one-period binomial model has two states and two independent assets (stock and bond), so the payoff space is two-dimensional and every contingent claim can be replicated. This is **market completeness**: two linearly independent assets span all possible two-state payoffs.

An equivalent pricing framework uses **Arrow-Debreu securities** -- state-contingent claims paying \$1 in exactly one state. Their prices are the **state prices**:

$$
\psi_u = e^{-r\Delta t} q, \qquad \psi_d = e^{-r\Delta t}(1 - q)
$$

Any payoff is priced by $V_0 = \psi_u H_u + \psi_d H_d$. The sum of state prices equals the discount factor: $\psi_u + \psi_d = e^{-r\Delta t}$.

The First Fundamental Theorem of Asset Pricing states that the market is arbitrage-free if and only if positive state prices exist. The Second states that the market is complete if and only if the state prices (equivalently, the risk-neutral measure) are unique.

## Examples

Price a European call and put with strike \$105, and verify put-call parity.

```python
import numpy as np

S0, K, r, dt = 100, 105, 0.05, 1.0
u, d = 1.2, 0.9

# Call payoffs
H_u_call = max(u * S0 - K, 0)  # 15
H_d_call = max(d * S0 - K, 0)  # 0

# Put payoffs
H_u_put = max(K - u * S0, 0)   # 0
H_d_put = max(K - d * S0, 0)   # 15

def replicate(H_u, H_d):
    delta = (H_u - H_d) / ((u - d) * S0)
    B = np.exp(-r * dt) * (u * H_d - d * H_u) / (u - d)
    price = delta * S0 + B
    return delta, B, price

delta_c, B_c, C0 = replicate(H_u_call, H_d_call)
delta_p, B_p, P0 = replicate(H_u_put, H_d_put)

print(f"Call: delta={delta_c:.4f}, B={B_c:.2f}, price={C0:.4f}")
print(f"Put:  delta={delta_p:.4f}, B={B_p:.2f}, price={P0:.4f}")

# Put-call parity check
lhs = C0 - P0
rhs = S0 - K * np.exp(-r * dt)
print(f"C - P = {lhs:.4f}, S - K*exp(-rT) = {rhs:.4f}")

# State prices
q = (np.exp(r * dt) - d) / (u - d)
psi_u = np.exp(-r * dt) * q
psi_d = np.exp(-r * dt) * (1 - q)
print(f"State prices: psi_u={psi_u:.4f}, psi_d={psi_d:.4f}")
print(f"Sum = {psi_u + psi_d:.4f} vs discount = {np.exp(-r*dt):.4f}")
```
