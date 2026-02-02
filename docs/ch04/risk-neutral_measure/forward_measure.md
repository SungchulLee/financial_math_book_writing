# The Forward Measure

The **$T$-forward measure** is a probability measure that uses the zero-coupon bond $P(t,T)$ as numéraire. It is particularly useful for pricing interest rate derivatives where the payoff occurs at a specific future date $T$.

---

## Definition

### The Numéraire

The **$T$-maturity zero-coupon bond** has price process $P(t,T)$ satisfying:

- $P(T,T) = 1$ (pays 1 at maturity)
- $P(t,T) > 0$ for $t < T$

### The $T$-Forward Measure

The $T$-forward measure $\mathbb{Q}^T$ is defined by the Radon-Nikodym derivative:

$$
\boxed{
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T)}{P(0,T)B_t}
}
$$

where $B_t = e^{\int_0^t r_s\,ds}$ is the money market account and $\mathbb{Q}$ is the standard risk-neutral measure.

---

## Key Properties

### 1. Bond-Deflated Prices are Martingales

Under $\mathbb{Q}^T$, for any traded asset $S_t$:

$$
\frac{S_t}{P(t,T)} \text{ is a } \mathbb{Q}^T\text{-martingale}
$$

### 2. Forward Prices are Martingales

The **forward price** of $S$ for delivery at $T$:

$$
F(t,T) = \frac{S_t}{P(t,T)}
$$

is a $\mathbb{Q}^T$-martingale:

$$
F(t,T) = \mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t]
$$

### 3. Pricing Formula

For a claim with payoff $\Phi_T$ at time $T$:

$$
\boxed{
V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi_T \mid \mathcal{F}_t]
}
$$

**No explicit discounting required**—the bond price handles it.

---

## Comparison: Risk-Neutral vs Forward Measure

| Aspect | Risk-Neutral $\mathbb{Q}$ | Forward $\mathbb{Q}^T$ |
|--------|---------------------------|------------------------|
| Numéraire | Money market $B_t$ | Bond $P(t,T)$ |
| Martingale | $S_t/B_t$ | $S_t/P(t,T)$ |
| Pricing | $V_t = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}\Phi_T]$ | $V_t = P(t,T)\mathbb{E}^{\mathbb{Q}^T}[\Phi_T]$ |
| Discount | Stochastic | Deterministic factor $P(t,T)$ |

---

## Dynamics Under the Forward Measure

### Brownian Motion Change

Under $\mathbb{Q}$: $W_t^{\mathbb{Q}}$ is Brownian motion.

Under $\mathbb{Q}^T$:

$$
W_t^{\mathbb{Q}^T} = W_t^{\mathbb{Q}} - \int_0^t \sigma_P(s,T)\,ds
$$

is Brownian motion, where $\sigma_P(t,T)$ is the volatility of the bond:

$$
\frac{dP(t,T)}{P(t,T)} = r_t\,dt + \sigma_P(t,T)\,dW_t^{\mathbb{Q}}
$$

### Asset Dynamics

If under $\mathbb{Q}$:

$$
\frac{dS_t}{S_t} = r_t\,dt + \sigma_S\,dW_t^{\mathbb{Q}}
$$

then under $\mathbb{Q}^T$:

$$
\frac{dS_t}{S_t} = (r_t + \sigma_S\sigma_P(t,T))\,dt + \sigma_S\,dW_t^{\mathbb{Q}^T}
$$

The drift changes by the covariance between $S$ and $P$.

---

## Example: LIBOR Forward Rate

### Definition

The **forward LIBOR rate** $L(t;T,T+\delta)$ for period $[T, T+\delta]$ is defined by:

$$
1 + \delta L(t;T,T+\delta) = \frac{P(t,T)}{P(t,T+\delta)}
$$

### Under the $(T+\delta)$-Forward Measure

The forward LIBOR rate is a $\mathbb{Q}^{T+\delta}$-martingale:

$$
L(t;T,T+\delta) = \mathbb{E}^{\mathbb{Q}^{T+\delta}}[L(T;T,T+\delta) \mid \mathcal{F}_t]
$$

At time $T$, the spot LIBOR fixes: $L(T;T,T+\delta) = L_T$.

### Caplet Pricing

A caplet with strike $K$ pays $\delta(L_T - K)^+$ at time $T+\delta$.

Under $\mathbb{Q}^{T+\delta}$:

$$
V_t = P(t,T+\delta) \cdot \delta \cdot \mathbb{E}^{\mathbb{Q}^{T+\delta}}[(L_T - K)^+ \mid \mathcal{F}_t]
$$

If $L(t;T,T+\delta)$ is log-normal under $\mathbb{Q}^{T+\delta}$ with volatility $\sigma_L$:

$$
V_t = P(t,T+\delta) \cdot \delta \cdot [L_t\Phi(d_1) - K\Phi(d_2)]
$$

This is **Black's formula for caplets**.

---

## Example: Forward Contract

### Setup

Forward contract to buy asset $S$ at time $T$ for price $K$.

Payoff at $T$: $\Phi_T = S_T - K$.

### Under Risk-Neutral Measure

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}(S_T - K) \mid \mathcal{F}_t\right]
$$

Requires knowing the joint distribution of $r$ and $S$.

### Under Forward Measure

$$
V_t = P(t,T)\mathbb{E}^{\mathbb{Q}^T}[S_T - K \mid \mathcal{F}_t] = P(t,T)(F(t,T) - K)
$$

Since $F(t,T)$ is a $\mathbb{Q}^T$-martingale: $\mathbb{E}^{\mathbb{Q}^T}[S_T] = F(t,T)$.

**Much simpler!** No need to model $r$ and $S$ jointly.

---

## The Forward Measure in Vasicek Model

### Bond Price Dynamics

In Vasicek:

$$
dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma_r\,dW_t^{\mathbb{Q}}
$$

The bond price is:

$$
P(t,T) = A(t,T)e^{-B(t,T)r_t}
$$

with $B(t,T) = \frac{1-e^{-\kappa(T-t)}}{\kappa}$.

### Bond Volatility

$$
\sigma_P(t,T) = -B(t,T)\sigma_r
$$

### Interest Rate Under $\mathbb{Q}^T$

$$
dr_t = [\kappa(\bar{r} - r_t) - \sigma_r^2 B(t,T)]\,dt + \sigma_r\,dW_t^{\mathbb{Q}^T}
$$

The drift is modified by the "volatility of the drift" adjustment.

---

## Multiple Forward Measures

For different maturities $T_1 < T_2$:

$$
\frac{d\mathbb{Q}^{T_2}}{d\mathbb{Q}^{T_1}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T_2)/P(0,T_2)}{P(t,T_1)/P(0,T_1)}
$$

Each maturity has its own forward measure.

### The Tower of Measures

$$
\mathbb{Q} \longleftrightarrow \mathbb{Q}^{T_1} \longleftrightarrow \mathbb{Q}^{T_2} \longleftrightarrow \cdots
$$

All are equivalent measures connected by Radon-Nikodym derivatives.

---

## When to Use the Forward Measure

| Problem | Use Forward Measure When |
|---------|--------------------------|
| European options | Payoff at single date $T$ |
| Caps/Floors | Separate caplet for each period |
| Bond options | Option on $P(T,S)$ at time $T$ |
| Forward starting options | Payoff depends on forward price |

**Avoid** forward measure for:
- Path-dependent options (use $\mathbb{Q}$)
- American options (early exercise)
- Options with multiple payment dates (use swap measure)

---

## Summary

$$
\boxed{
V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi_T \mid \mathcal{F}_t]
}
$$

| Property | Statement |
|----------|-----------|
| Numéraire | Zero-coupon bond $P(t,T)$ |
| Martingale | Forward price $F(t,T) = S_t/P(t,T)$ |
| Advantage | Eliminates stochastic discounting |
| Use case | Interest rate derivatives |

**The forward measure transforms the problem of stochastic discounting into a problem of computing a simple expectation, making it indispensable for interest rate modeling.**
