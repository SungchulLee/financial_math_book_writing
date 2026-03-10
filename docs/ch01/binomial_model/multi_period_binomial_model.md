# Multi-Period Binomial Model

The multi-period binomial tree extends one-period pricing to arbitrary maturities through backward induction, enabling dynamic delta hedging and American option valuation.

## Definition

Fix maturity $T$ divided into $N$ equal steps with $\Delta t = T/N$. At node $(n, j)$ the stock price is $S_{n,j} = S_0 u^j d^{n-j}$, and the recombining property $ud = 1$ ensures only $n+1$ nodes at time $n$. The **European option** backward recursion is

$$
V_{n,j} = e^{-r\Delta t}\bigl[q\,V_{n+1,j+1} + (1-q)\,V_{n+1,j}\bigr]
$$

with terminal condition $V_{N,j} = H(S_{N,j})$ and risk-neutral probability $q = (e^{r\Delta t} - d)/(u - d)$. For **American options**, the recursion becomes

$$
V_{n,j} = \max\!\bigl(\Phi(S_{n,j}),\; e^{-r\Delta t}[q\,V_{n+1,j+1} + (1-q)\,V_{n+1,j}]\bigr)
$$

where $\Phi$ is the exercise payoff.

## Explanation

At each node, the local hedge ratio is $\Delta_{n,j} = (V_{n+1,j+1} - V_{n+1,j})/(S_{n,j}(u-d))$, and the cash position is $B_{n,j} = V_{n,j} - \Delta_{n,j} S_{n,j}$. The **self-financing property** guarantees that rebalancing at each step requires no external cash injection: the old portfolio value exactly equals the cost of the new position.

For American puts, early exercise can be optimal when the stock price is sufficiently low and the intrinsic value exceeds the continuation value. The **early exercise boundary** separates the stopping region from the continuation region. For American calls on non-dividend-paying stocks, early exercise is never optimal because holding always dominates.

The algorithm has $O(N^2)$ time complexity and $O(N)$ space when only one time slice is stored.

## Examples

Price European and American puts with strike \$100 on a stock at \$100, with $\sigma = 20\%$, $r = 5\%$, $T = 1$ year, $N = 200$ steps.

```python
import numpy as np

S0, K, r, sigma, T, N = 100, 100, 0.05, 0.20, 1.0, 200
dt = T / N
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
q = (np.exp(r * dt) - d) / (u - d)
disc = np.exp(-r * dt)

# Terminal stock prices
j = np.arange(N + 1)
S_T = S0 * u**j * d**(N - j)

# European put via backward induction
V_eur = np.maximum(K - S_T, 0.0)
for n in range(N - 1, -1, -1):
    V_eur = disc * (q * V_eur[1:] + (1 - q) * V_eur[:-1])
print(f"European put: {V_eur[0]:.4f}")

# American put via backward induction
V_am = np.maximum(K - S_T, 0.0)
for n in range(N - 1, -1, -1):
    S_n = S0 * u**np.arange(n + 1) * d**(n - np.arange(n + 1))
    cont = disc * (q * V_am[1:] + (1 - q) * V_am[:-1])
    V_am = np.maximum(np.maximum(K - S_n, 0.0), cont)
print(f"American put: {V_am[0]:.4f}")
print(f"Early exercise premium: {V_am[0] - V_eur[0]:.4f}")
```
