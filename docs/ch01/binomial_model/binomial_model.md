# Binomial Asset Pricing Model

The Cox-Ross-Rubinstein (1979) binomial model provides the simplest discrete-time framework for derivative pricing, capturing the essential logic of arbitrage-free valuation through a two-state stock price evolution.

## Definition

Consider a one-period market on the time grid $t \in \{0, \Delta t\}$ with two traded assets. A **risk-free asset** grows deterministically as $B_{\Delta t} = e^{r \Delta t}$. A **risky asset** (stock) evolves from $S_0 > 0$ to

$$
S_{\Delta t} =
\begin{cases}
u S_0 & \text{with probability } p \quad \text{(up state)} \\[6pt]
d S_0 & \text{with probability } 1-p \quad \text{(down state)}
\end{cases}
$$

where $u > 1$ is the up factor and $0 < d < 1$ is the down factor. The market is **arbitrage-free** if and only if

$$
d < e^{r \Delta t} < u
$$

Under this condition, there exists a unique **risk-neutral probability**

$$
q = \frac{e^{r \Delta t} - d}{u - d}
$$

such that the discounted stock price $\tilde{S}_t = e^{-rt} S_t$ is a martingale under the measure $\mathbb{Q}(\text{up}) = q$.

## Explanation

The no-arbitrage condition has a geometric interpretation: the risk-free return $e^{r\Delta t}$ must lie strictly inside the interval $[d, u]$. If the bank always beats the stock (even in the best case), or the stock always beats the bank (even in the worst case), a riskless profit can be constructed.

The risk-neutral probability $q$ is derived by requiring $S_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}]$, so that discounted prices are martingales. This probability is independent of the physical probability $p$ and depends only on the market parameters $(u, d, r, \Delta t)$.

A **contingent claim** with payoff $H(S_{\Delta t})$ is priced by the risk-neutral expectation

$$
V_0 = e^{-r \Delta t} \mathbb{E}^{\mathbb{Q}}[H] = e^{-r \Delta t}\bigl[q\,H_u + (1-q)\,H_d\bigr]
$$

This formula is equivalent to replication via a stock-bond portfolio and to delta hedging. All three approaches yield the same arbitrage-free price.

A **portfolio** $(\Delta, \beta)$ holds $\Delta$ shares of stock and $\beta$ units of the bank account. It is self-financing if rebalancing uses only the current portfolio value with no external cash flows.

## Examples

Price a European call with strike \$105 on a stock at \$100, with $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$ year.

```python
import numpy as np

S0, K, r, dt = 100, 105, 0.05, 1.0
u, d = 1.2, 0.9

# Risk-neutral probability
q = (np.exp(r * dt) - d) / (u - d)
print(f"Risk-neutral probability q = {q:.4f}")

# Payoffs
H_u = max(u * S0 - K, 0)
H_d = max(d * S0 - K, 0)
print(f"Payoff up: {H_u:.2f}, Payoff down: {H_d:.2f}")

# Risk-neutral price
V0 = np.exp(-r * dt) * (q * H_u + (1 - q) * H_d)
print(f"European call price: {V0:.4f}")

# Verify no-arbitrage condition
assert d < np.exp(r * dt) < u, "No-arbitrage condition violated"
print(f"No-arbitrage check: {d} < {np.exp(r*dt):.4f} < {u}")
```
