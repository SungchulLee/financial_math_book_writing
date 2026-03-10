# Binomial to Black-Scholes Limit

As the number of binomial time steps tends to infinity, the CRR model converges to the Black-Scholes framework, connecting the discrete random walk to geometric Brownian motion via the central limit theorem.

## Definition

With the **Cox-Ross-Rubinstein parameterization** $u = e^{\sigma\sqrt{\Delta t}}$, $d = e^{-\sigma\sqrt{\Delta t}}$, and $\Delta t = T/n$, the log-price after $n$ steps is

$$
\ln S_n = \ln S_0 + \sigma\sqrt{\Delta t}\sum_{i=1}^{n} X_i
$$

where $X_i = +1$ (up) with risk-neutral probability $q$ and $X_i = -1$ (down) with probability $1-q$. As $n \to \infty$, the Central Limit Theorem gives

$$
\ln S_n \xrightarrow{d} \mathcal{N}\!\left(\ln S_0 + \left(r - \tfrac{1}{2}\sigma^2\right)T,\; \sigma^2 T\right)
$$

so $S_T$ converges to the geometric Brownian motion solution $S_T = S_0 \exp\!\bigl((r - \tfrac{1}{2}\sigma^2)T + \sigma W_T\bigr)$.

## Explanation

**Risk-neutral probability limit.** Expanding $q = (e^{r\Delta t} - d)/(u - d)$ for small $\Delta t$ gives $q = \tfrac{1}{2} + \tfrac{r\sqrt{\Delta t}}{2\sigma} + O(\Delta t)$, so $q \to \tfrac{1}{2}$.

**The Ito correction.** The martingale condition constrains the arithmetic return $\mathbb{E}^{\mathbb{Q}}[S_{i+1}/S_i] = e^{r\Delta t}$, but Jensen's inequality applied to $\ln(\cdot)$ implies $\mathbb{E}[\ln R_i] < \ln\mathbb{E}[R_i] = r\Delta t$. A second-order expansion yields

$$
\mathbb{E}^{\mathbb{Q}}[\ln R_i] \approx r\Delta t - \tfrac{1}{2}\sigma^2\Delta t
$$

which sums to $(r - \tfrac{1}{2}\sigma^2)T$ over $n$ steps. This is the discrete origin of the Ito correction term.

**PDE emergence.** Taylor-expanding the backward recursion $V_i = e^{-r\Delta t}[qV_{i+1}^u + (1-q)V_{i+1}^d]$ around $(S, t)$ and taking $\Delta t \to 0$ yields the Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

**Convergence rate.** For European options, $|C_n - C_{BS}| = O(1/n)$ with oscillations between odd and even $n$. Richardson extrapolation (combining $C_n$ and $C_{2n}$) achieves $O(1/n^2)$.

**Delta convergence.** The discrete hedge ratio $\Delta_i = (V_{i+1}^u - V_{i+1}^d)/(S(u-d))$ converges to $\partial V/\partial S$, the Black-Scholes delta.

## Examples

Demonstrate convergence of the binomial call price to the Black-Scholes formula as $n$ increases.

```python
import numpy as np
from scipy.stats import norm

S0, K, r, sigma, T = 100, 100, 0.05, 0.20, 1.0

# Black-Scholes closed form
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
bs_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
print(f"Black-Scholes price: {bs_price:.6f}")

# Binomial prices for increasing n
for n in [10, 50, 100, 500, 1000]:
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    # Terminal payoffs
    j = np.arange(n + 1)
    S_T = S0 * u**j * d**(n - j)
    V = np.maximum(S_T - K, 0)

    # Backward induction
    for step in range(n):
        V = disc * (q * V[1:] + (1 - q) * V[:-1])

    error = V[0] - bs_price
    print(f"n={n:5d}  price={V[0]:.6f}  error={error:+.6f}")
```
