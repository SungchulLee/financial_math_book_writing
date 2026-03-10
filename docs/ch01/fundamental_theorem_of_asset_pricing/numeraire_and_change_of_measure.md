# Numeraire and Change of Measure

A numeraire is any strictly positive traded asset used as a unit of account; changing the numeraire changes the martingale measure but leaves all arbitrage-free prices invariant.

## Definition

A **numeraire** is a traded asset $N_t > 0$ for all $t$. The **master pricing formula** under numeraire $N_t$ with associated martingale measure $\mathbb{Q}^N$ is

$$
V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right]
$$

The **change of numeraire theorem** states: if $N_t$ and $M_t$ are two numeraires with measures $\mathbb{Q}^N$ and $\mathbb{Q}^M$, then

$$
\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\bigg|_{\mathcal{F}_t} = \frac{M_t / M_0}{N_t / N_0}
$$

and for any claim $\Phi_T$,

$$
N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\bigg|\; \mathcal{F}_t\right] = M_t \cdot \mathbb{E}^{\mathbb{Q}^M}\!\left[\frac{\Phi_T}{M_T} \;\bigg|\; \mathcal{F}_t\right]
$$

## Explanation

Standard numeraire choices include the money market account $N_t = e^{rt}$ (giving the risk-neutral measure $\mathbb{Q}$), the zero-coupon bond $N_t = P(t,T)$ (giving the $T$-forward measure $\mathbb{Q}^T$ where forward prices are martingales and discounting is absorbed), and a risky stock $N_t = S_t$ (useful for exchange options).

The proof uses the abstract Bayes formula. Since $M_t/N_t$ is a positive $\mathbb{Q}^N$-martingale with initial value $M_0/N_0$, the normalized ratio $L_t = (M_t/M_0)/(N_t/N_0)$ defines a valid Radon-Nikodym process. Under $\mathbb{Q}^M$, all prices normalized by $M_t$ are martingales, verified by applying the Bayes formula.

**Margrabe's formula** for exchange options $\Phi_T = (S^1_T - S^2_T)^+$ uses $S^2_t$ as numeraire to reduce a two-dimensional problem to one dimension: under $\mathbb{Q}^2$, the ratio $S^1_t/S^2_t$ is a GBM with volatility $\sigma_R = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2}$, yielding $V_0 = S^1_0 \Phi(d_1) - S^2_0 \Phi(d_2)$.

## Examples

Demonstrate numeraire invariance: price a call using both the money market and stock numeraires.

```python
import numpy as np
from scipy.stats import norm

S0, K, r, sigma, T = 100, 100, 0.05, 0.20, 1.0

# Standard Black-Scholes (money market numeraire)
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
C_mm = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
print(f"Call (money market numeraire): {C_mm:.6f}")

# Stock numeraire: C = S0 * Q^S(S_T > K)  -  K * e^{-rT} * Q(S_T > K)
# Under Q^S, ln(S_T) ~ N(ln(S0) + (r + sigma^2/2)T, sigma^2 T)
# P^S(S_T > K) = Phi(d1), P^Q(S_T > K) = Phi(d2)
C_stock = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
print(f"Call (stock numeraire):        {C_stock:.6f}")
print(f"Prices match: {np.isclose(C_mm, C_stock)}")

# Margrabe's formula: exchange option (S1_T - S2_T)^+
S1_0, S2_0 = 100, 95
sigma1, sigma2, rho = 0.25, 0.20, 0.5
sigma_R = np.sqrt(sigma1**2 - 2*rho*sigma1*sigma2 + sigma2**2)
R0 = S1_0 / S2_0
d1_m = (np.log(R0) + 0.5 * sigma_R**2 * T) / (sigma_R * np.sqrt(T))
d2_m = d1_m - sigma_R * np.sqrt(T)
V_margrabe = S1_0 * norm.cdf(d1_m) - S2_0 * norm.cdf(d2_m)
print(f"\nMargrabe exchange option: {V_margrabe:.4f}")
```
