# Risk-Neutral Pricing

In an arbitrage-free market, the price of any contingent claim equals the discounted expectation of its payoff under a unique risk-neutral measure that makes discounted prices martingales.

## Definition

The **risk-neutral measure** $\mathbb{Q}$ on the binomial state space is defined by $\mathbb{Q}(\text{up}) = q$ where

$$
q = \frac{e^{r\Delta t} - d}{u - d}
$$

Under $\mathbb{Q}$, the discounted stock price is a **martingale**: $\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}/e^{r\Delta t}] = S_0$. The **risk-neutral pricing formula** for a claim with payoff $H$ is

$$
V_0 = e^{-r\Delta t}\,\mathbb{E}^{\mathbb{Q}}[H] = e^{-r\Delta t}\bigl[q\,H_u + (1-q)\,H_d\bigr]
$$

In the multi-period tree, this generalizes to

$$
V_0 = e^{-rT} \sum_{j=0}^{N} \binom{N}{j} q^j (1-q)^{N-j}\, H(S_0 u^j d^{N-j})
$$

## Explanation

The risk-neutral probability $q$ is not a forecast of which state will occur. It is a mathematical construct determined entirely by the market parameters $(u, d, r, \Delta t)$, independent of the physical probability $p$. Under $\mathbb{Q}$, the stock's expected return equals the risk-free rate, as if investors were indifferent to risk.

Risk-neutral pricing is **equivalent to replication**: both yield the same unique no-arbitrage price. The advantage of the expectation approach is computational convenience and the ability to decompose complex payoffs via linearity:

$$
V_0(\alpha H^{(1)} + \beta H^{(2)}) = \alpha\, V_0(H^{(1)}) + \beta\, V_0(H^{(2)})
$$

This linearity immediately yields **put-call parity**: using $(S - K)^+ - (K - S)^+ = S - K$,

$$
C_0 - P_0 = e^{-r\Delta t}\,\mathbb{E}^{\mathbb{Q}}[S_{\Delta t} - K] = S_0 - K e^{-r\Delta t}
$$

The price of a digital call (paying \$1 if up) is $e^{-r\Delta t} q$, revealing that risk-neutral probabilities are discounted Arrow-Debreu prices.

## Examples

Price a call, put, digital, and forward, then verify put-call parity.

```python
import numpy as np

S0, K, r, dt = 100, 105, 0.05, 1.0
u, d = 1.2, 0.9
q = (np.exp(r * dt) - d) / (u - d)
disc = np.exp(-r * dt)

# Risk-neutral pricing for various claims
payoffs = {
    "Call":    (max(u*S0 - K, 0), max(d*S0 - K, 0)),
    "Put":     (max(K - u*S0, 0), max(K - d*S0, 0)),
    "Digital": (1, 0),
    "Forward": (u*S0 - S0*np.exp(r*dt), d*S0 - S0*np.exp(r*dt)),
}

for name, (Hu, Hd) in payoffs.items():
    price = disc * (q * Hu + (1 - q) * Hd)
    print(f"{name:8s}: price = {price:.4f}")

# Put-call parity verification
C = disc * (q * max(u*S0-K, 0) + (1-q) * max(d*S0-K, 0))
P = disc * (q * max(K-u*S0, 0) + (1-q) * max(K-d*S0, 0))
print(f"\nC - P = {C - P:.4f}")
print(f"S - K*exp(-rT) = {S0 - K * disc:.4f}")

# Martingale property check
E_S = q * u * S0 + (1 - q) * d * S0
print(f"\nE^Q[S] = {E_S:.4f}, S0*exp(rT) = {S0*np.exp(r*dt):.4f}")
```
