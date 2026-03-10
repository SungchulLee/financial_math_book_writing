# American Options on Binomial Trees

American options can be exercised at any time before expiry, making their valuation an optimal stopping problem that binomial trees solve naturally through backward induction.

## Definition

An **American option** with payoff function $\Phi(S)$ on a binomial tree with $N$ steps is valued by the backward recursion

$$
V_{n,j} = \max\!\bigl(\Phi(S_{n,j}),\; e^{-r\Delta t}[q\,V_{n+1,j+1} + (1-q)\,V_{n+1,j}]\bigr)
$$

for $n = N-1, N-2, \ldots, 0$ and $j = 0, 1, \ldots, n$, with terminal condition $V_{N,j} = \Phi(S_{N,j})$. Here $S_{n,j} = S_0 u^j d^{n-j}$, and $q = (e^{r\Delta t} - d)/(u-d)$ is the risk-neutral probability.

## Explanation

The key difference from European pricing is the $\max$ operator at each node. The holder compares the **continuation value** (the discounted risk-neutral expectation of future option value) against the **intrinsic value** (immediate exercise payoff). Exercise is optimal whenever the intrinsic value exceeds the continuation value.

For an American **call** on a non-dividend-paying stock, early exercise is never optimal. The continuation value always dominates because the time value of the option is positive. For an American **put**, early exercise can be optimal when the stock price is sufficiently low, since the payoff $K - S$ is bounded above by $K$ while the time value of money erodes the present value of deferred exercise.

The set of nodes where exercise is optimal defines the **early exercise boundary**, which separates the continuation region from the stopping region.

## Examples

Price a 1-year American put with strike \$100 on a stock at \$100, with $r = 5\%$, $\sigma = 20\%$, using a 3-step tree.

```python
import numpy as np

S0, K, r, sigma, T, N = 100, 100, 0.05, 0.20, 1.0, 3
dt = T / N
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
q = (np.exp(r * dt) - d) / (u - d)
disc = np.exp(-r * dt)

# Stock prices at each node
S = np.zeros((N + 1, N + 1))
for n in range(N + 1):
    for j in range(n + 1):
        S[n, j] = S0 * u**j * d**(n - j)

# Backward induction for American put
V = np.maximum(K - S[N, :N + 1], 0)  # terminal payoff
for n in range(N - 1, -1, -1):
    cont = disc * (q * V[1:n + 2] + (1 - q) * V[:n + 1])
    intrinsic = np.maximum(K - S[n, :n + 1], 0)
    V = np.maximum(cont, intrinsic)

print(f"American put price: {V[0]:.4f}")

# Compare with European put (no early exercise)
V_eur = np.maximum(K - S[N, :N + 1], 0)
for n in range(N - 1, -1, -1):
    V_eur = disc * (q * V_eur[1:n + 2] + (1 - q) * V_eur[:n + 1])

print(f"European put price: {V_eur[0]:.4f}")
print(f"Early exercise premium: {V[0] - V_eur[0]:.4f}")
```
