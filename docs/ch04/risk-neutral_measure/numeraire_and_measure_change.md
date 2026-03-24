# Numéraire and Change of Measure

Changing the **numéraire** (unit of account) provides a powerful and elegant framework for derivative pricing. Each choice of numéraire corresponds to a different equivalent martingale measure, and selecting the right numéraire often dramatically simplifies pricing formulas.

---

## The Numéraire Concept

### Definition

A **numéraire** is any strictly positive traded asset used as the unit of account for measuring value.

**Key property**: If $N_t > 0$ is a numéraire, then any asset price $S_t$ can be expressed in "units of $N$" as:

$$
\frac{S_t}{N_t}
$$

### Common Numéraires

| Numéraire | Asset | Associated Measure |
|-----------|-------|-------------------|
| Money market account | $B_t = e^{\int_0^t r_s\,ds}$ | Risk-neutral $\mathbb{Q}$ |
| Zero-coupon bond | $P(t,T)$ | $T$-forward measure $\mathbb{Q}^T$ |
| Stock | $S_t$ | Stock measure $\mathbb{Q}^S$ |
| Foreign money market | $B_t^f X_t$ | Foreign risk-neutral |

---

## The Fundamental Theorem for Numéraires

**Theorem**: Let $N_t$ be any positive traded asset (numéraire). There exists a probability measure $\mathbb{Q}^N$ equivalent to $\mathbb{P}$ such that for **any** traded asset $S_t$:

$$
\boxed{
\frac{S_t}{N_t} \text{ is a } \mathbb{Q}^N\text{-martingale}
}
$$

### General Pricing Formula

Under measure $\mathbb{Q}^N$, the price of a claim $\Phi_T$ at time $T$ is:

$$
\boxed{
V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\left[\frac{\Phi_T}{N_T} \;\middle|\; \mathcal{F}_t\right]
}
$$

---

## Relationship Between Measures

### Change of Numéraire Formula

If $M_t$ and $N_t$ are two numéraires with associated measures $\mathbb{Q}^M$ and $\mathbb{Q}^N$, then:

$$
\boxed{
\frac{d\mathbb{Q}^N}{d\mathbb{Q}^M}\bigg|_{\mathcal{F}_T} = \frac{N_T/N_0}{M_T/M_0}
}
$$

**Interpretation**: The likelihood ratio is the relative performance of the two numéraires.

### Special Case: Money Market to Bond

From $\mathbb{Q}$ (money market numéraire $B_t$) to $\mathbb{Q}^T$ (bond numéraire $P(t,T)$):

$$
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{P(T,T)/P(0,T)}{B_T/B_0} = \frac{1}{P(0,T)B_T} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
$$

---

## The T-Forward Measure

### Definition

The **$T$-forward measure** $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numéraire.

### Key Property

Under $\mathbb{Q}^T$, the **forward price** $F(t,T) = S_t/P(t,T)$ is a martingale:

$$
F(t,T) = \mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t]
$$

### Forward Pricing Formula

For a European claim with payoff $\Phi(S_T)$:

$$
V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi(S_T) \mid \mathcal{F}_t]
$$

**No explicit discounting needed!** The bond price $P(t,T)$ handles it.

---

## Example: Black's Formula

### Setup

Price a European call on a forward contract with strike $K$ and maturity $T$.

### Under Risk-Neutral Measure Q

$$
C_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}(F_T - K)^+ \mid \mathcal{F}_t\right]
$$

This requires modeling the joint distribution of $r$ and $F$.

### Under Forward Measure Q^T

$$
C_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[(F_T - K)^+ \mid \mathcal{F}_t]
$$

If $F_t$ is log-normal under $\mathbb{Q}^T$ with volatility $\sigma_F$:

$$
\boxed{
C_t = P(t,T)[F_t\Phi(d_1) - K\Phi(d_2)]
}
$$

where:

$$
d_1 = \frac{\ln(F_t/K) + \frac{1}{2}\sigma_F^2(T-t)}{\sigma_F\sqrt{T-t}}, \quad d_2 = d_1 - \sigma_F\sqrt{T-t}
$$

This is **Black's formula** (1976).

---

## Example: Exchange Option (Margrabe's Formula)

### Setup

Option to exchange asset $S^2$ for asset $S^1$ at time $T$:

$$
\Phi_T = (S_T^1 - S_T^2)^+
$$

### Using S² as Numéraire

Under $\mathbb{Q}^{S^2}$, the ratio $S_t^1/S_t^2$ is a martingale.

$$
V_t = S_t^2 \cdot \mathbb{E}^{\mathbb{Q}^{S^2}}\left[\left(\frac{S_T^1}{S_T^2} - 1\right)^+ \;\middle|\; \mathcal{F}_t\right]
$$

If the ratio is log-normal:

$$
\boxed{
V_t = S_t^1\Phi(d_1) - S_t^2\Phi(d_2)
}
$$

where:

$$
d_1 = \frac{\ln(S_t^1/S_t^2) + \frac{1}{2}\sigma^2(T-t)}{\sigma\sqrt{T-t}}
$$

and $\sigma^2 = \sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2$.

**Note**: Interest rate $r$ does not appear—the option is self-financing in either asset.

---

## Dynamics Under Different Measures

### Under Money Market Numéraire (Q)

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

### Under Forward Measure (Q^T)

$$
dS_t = (r + \sigma\sigma_P\rho_{SP})S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^T}
$$

where $\sigma_P$ is bond volatility and $\rho_{SP}$ is stock-bond correlation.

### Under Stock Measure (Q^S)

$$
dS_t = (r + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^S}
$$

The drift increases by $\sigma^2$ (the "convexity adjustment").

---

## When to Use Which Numéraire

| Problem | Best Numéraire | Reason |
|---------|----------------|--------|
| Equity options | Money market | Standard Black-Scholes |
| Interest rate caps/floors | Zero-coupon bond | Forward rate is martingale |
| Swaptions | Annuity | Swap rate is martingale |
| Exchange options | One of the assets | Eliminates one variable |
| Quanto options | Foreign bond | Simplifies FX dependence |

---

## The Annuity Numéraire (Swap Measure)

For interest rate swaps, the natural numéraire is the **annuity**:

$$
A(t) = \sum_{i=1}^n \tau_i P(t, T_i)
$$

Under the **swap measure** $\mathbb{Q}^A$, the **swap rate** is a martingale:

$$
S(t) = \frac{P(t, T_0) - P(t, T_n)}{A(t)}
$$

This leads to Black's model for swaptions.

---

## Summary

$$
\boxed{
V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\left[\frac{\Phi_T}{N_T} \;\middle|\; \mathcal{F}_t\right]
}
$$

| Principle | Statement |
|-----------|-----------|
| Any positive asset can be numéraire | Flexibility in measure choice |
| Relative prices are martingales | $S_t/N_t$ is $\mathbb{Q}^N$-martingale |
| Measure change formula | $d\mathbb{Q}^N/d\mathbb{Q}^M = (N_T/N_0)/(M_T/M_0)$ |
| Right numéraire simplifies pricing | Choose to make payoff simple |

**Numéraire techniques are essential for interest rate derivatives, FX options, and multi-asset problems.**

---

## Exercises

**Exercise 1.**
Verify the change-of-numeraire formula: if $M_t = B_t$ (money market) and $N_t = P(t,T)$ (zero-coupon bond), write $d\mathbb{Q}^T / d\mathbb{Q}|_{\mathcal{F}_T}$ and show that it equals $e^{-\int_0^T r_s\,ds} / P(0,T)$. Confirm that this is a valid Radon-Nikodym derivative by showing its $\mathbb{Q}$-expectation is 1.

---

**Exercise 2.**
Under the stock measure $\mathbb{Q}^S$ (numeraire $N_t = S_t$), a European put option with payoff $(K - S_T)^+$ has price $V_t = S_t \cdot \mathbb{E}^{\mathbb{Q}^S}[(K/S_T - 1)^+ | \mathcal{F}_t]$. Explain why this formulation is useful, and describe how the distribution of $1/S_T$ under $\mathbb{Q}^S$ differs from the distribution of $S_T$ under $\mathbb{Q}$.

---

**Exercise 3.**
For Black's formula, a call on a forward contract has price $C_t = P(t,T)[F_t\Phi(d_1) - K\Phi(d_2)]$. Verify that as $\sigma_F \to 0$, the formula reduces to $C_t = P(t,T)\max(F_t - K, 0)$. What is the interpretation of this limit?

---

**Exercise 4.**
In the exchange option (Margrabe's formula), the price is $V_t = S_t^1\Phi(d_1) - S_t^2\Phi(d_2)$. Explain why the risk-free rate $r$ does not appear. Compute $V_0$ for $S_0^1 = 100$, $S_0^2 = 95$, $\sigma_1 = 0.20$, $\sigma_2 = 0.25$, $\rho = 0.5$, and $T = 1$.

---

**Exercise 5.**
Under the money market numeraire, $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. Under the stock measure, $dS_t = (r + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^S}$. Derive the drift change $r \to r + \sigma^2$ using the Girsanov kernel implicit in the numeraire change from $B_t$ to $S_t$.

---

**Exercise 6.**
The annuity numeraire is $A(t) = \sum_{i=1}^n \tau_i P(t, T_i)$. Under the swap measure $\mathbb{Q}^A$, the swap rate $S(t) = (P(t,T_0) - P(t,T_n))/A(t)$ is a martingale. Explain why this makes Black's model applicable to swaptions. What assumption about the swap rate distribution is needed?

---

**Exercise 7.**
Consider a quanto option: a European call on a foreign stock $S_t^f$ with strike $K$, where the payoff $(S_T^f - K)^+$ is paid in domestic currency. The relevant numeraire is the foreign money market account converted to domestic currency: $N_t = B_t^f X_t$. Write the pricing formula under the corresponding measure and explain what "quanto adjustment" is needed for the drift of $S_t^f$.
