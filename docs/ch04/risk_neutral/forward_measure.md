# The Forward Measure

The **$T$-forward measure** is a probability measure that uses the zero-coupon bond $P(t,T)$ as numéraire. It is particularly useful for pricing interest rate derivatives where the payoff occurs at a specific future date $T$.

The central advantage of the forward measure is that it **removes the randomness of
discounting**: pricing reduces to $P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}[\Phi_T]$ with a
deterministic prefactor, avoiding the correlation between stochastic discount factor
and payoff that complicates the
[risk-neutral valuation formula](risk_neutral_valuation_principle.md).

---

## Definition

The forward measure is the [numéraire framework](numeraire.md) applied to the
$T$-maturity zero-coupon bond $P(t,T)$ (with $P(T,T) = 1$ and $P(t,T) > 0$).

By the [change-of-numéraire formula](numeraire.md#relationship-between-measures), the
$T$-forward measure $\mathbb{Q}^T$ has Radon–Nikodym derivative:

$$
\boxed{
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T)}{P(0,T)B_t}
}
$$

where $B_t = e^{\int_0^t r_s\,ds}$ is the money market account and $\mathbb{Q}$ is the standard risk-neutral measure.

---

## Key Properties

### 1. Bond-Deflated Prices are Martingales

By the [numéraire theorem](numeraire.md#the-fundamental-theorem-for-numeraires),
$S_t / P(t,T)$ is a $\mathbb{Q}^T$-martingale for any traded asset $S_t$.

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

The [change of numéraire](numeraire.md) from $B_t$ to $P(t,T)$ shifts the Brownian
motion by the bond volatility $\sigma_P(t,T)$:

$$
W_t^{\mathbb{Q}^T} = W_t^{\mathbb{Q}} - \int_0^t \sigma_P(s,T)\,ds
$$

is Brownian motion, where $\sigma_P(t,T)$ is defined through the bond dynamics:

$$
\frac{dP(t,T)}{P(t,T)} = r_t\,dt + \sigma_P(t,T)\,dW_t^{\mathbb{Q}}
$$

### Asset Dynamics

If under $\mathbb{Q}$ the asset and bond are driven by (possibly correlated) diffusions
with volatilities $\sigma_S$ and $\sigma_P(t,T)$ and instantaneous correlation
$\rho_{S,P}$, then the asset dynamics change from

$$
\frac{dS_t}{S_t} = r_t\,dt + \sigma_S\,dW_t^{S,\mathbb{Q}}
$$

to

$$
\frac{dS_t}{S_t} = \bigl(r_t + \sigma_S\,\sigma_P(t,T)\,\rho_{S,P}\bigr)\,dt + \sigma_S\,dW_t^{S,\mathbb{Q}^T}
$$

The drift acquires the extra term $\sigma_S\,\sigma_P(t,T)\,\rho_{S,P}$, which is
precisely the **instantaneous covariance** between the asset return $dS/S$ and the bond
return $dP/P$.
This covariance correction arises because the Girsanov shift from $\mathbb{Q}$ to
$\mathbb{Q}^T$ is driven by the bond volatility $\sigma_P(t,T)$: the change of
numéraire tilts probabilities in proportion to the bond's own diffusion, and every
correlated diffusion picks up a corresponding drift adjustment.

---

## Example: LIBOR Forward Rate

### Definition

The **forward LIBOR rate** $L(t;T,T+\delta)$ for period $[T, T+\delta]$ is defined by:

$$
1 + \delta L(t;T,T+\delta) = \frac{P(t,T)}{P(t,T+\delta)}
$$

### Under the (T+δ)-Forward Measure

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
V_t = P(t,T+\delta) \cdot \delta \cdot [L_t\mathcal{N}(d_1) - K\mathcal{N}(d_2)]
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

### Interest Rate Under Q^T

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

All are equivalent measures connected by Radon–Nikodym derivatives.

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

All forward measures $\mathbb{Q}^{T_1}, \mathbb{Q}^{T_2}, \ldots$ and the risk-neutral
measure $\mathbb{Q}$ are **equivalent** --- they agree on which events are possible and
differ only in how they weight outcomes. The choice among them is a matter of
computational convenience, not of economic content.

**The forward measure transforms the problem of stochastic discounting into a problem of computing a simple expectation, making it indispensable for interest rate modeling.**

---

## Exercises

**Exercise 1.**
Write the Radon–Nikodym derivative $d\mathbb{Q}^T / d\mathbb{Q}|_{\mathcal{F}_t}$ in terms of $P(t,T)$, $P(0,T)$, and $B_t$. Verify that at $t = T$, this expression simplifies to $e^{-\int_0^T r_s\,ds} / P(0,T)$. Explain why $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^T / d\mathbb{Q}|_{\mathcal{F}_T}] = 1$.

??? success "Solution to Exercise 1"
    By definition:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T)}{P(0,T)B_t}
    $$

    At $t = T$: $P(T,T) = 1$ (the bond pays 1 at maturity) and $B_T = e^{\int_0^T r_s\,ds}$. Substituting:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{1}{P(0,T) \cdot e^{\int_0^T r_s\,ds}} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
    $$

    To verify $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^T/d\mathbb{Q}|_{\mathcal{F}_T}] = 1$: Under $\mathbb{Q}$, the discounted bond price $P(t,T)/B_t$ is a martingale. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{P(T,T)}{B_T}\right] = \frac{P(0,T)}{B_0} = P(0,T)
    $$

    since $B_0 = 1$. Hence:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}\right] = \frac{1}{P(0,T)}\mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{B_T}\right] = \frac{P(0,T)}{P(0,T)} = 1
    $$

    This confirms the Radon–Nikodym derivative is properly normalized.

---

**Exercise 2.**
A forward contract on a stock $S$ for delivery at $T$ has payoff $S_T - K$ at maturity. Using the forward measure, show that the value at time $t$ is $V_t = P(t,T)(F(t,T) - K)$ where $F(t,T) = S_t / P(t,T)$. Determine the forward price $K^*$ that makes the contract initially worth zero.

??? success "Solution to Exercise 2"
    The forward contract pays $\Phi_T = S_T - K$ at time $T$. Under the $T$-forward measure:

    $$
    V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[S_T - K \mid \mathcal{F}_t] = P(t,T)\!\left(\mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t] - K\right)
    $$

    Since the forward price $F(t,T) = S_t/P(t,T)$ is a $\mathbb{Q}^T$-martingale:

    $$
    \mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t] = \mathbb{E}^{\mathbb{Q}^T}[F(T,T) \mid \mathcal{F}_t] = F(t,T) = \frac{S_t}{P(t,T)}
    $$

    (using $F(T,T) = S_T/P(T,T) = S_T$). Therefore:

    $$
    V_t = P(t,T)\!\left(\frac{S_t}{P(t,T)} - K\right) = S_t - KP(t,T) = P(t,T)(F(t,T) - K)
    $$

    The forward price $K^*$ that makes the contract initially worth zero satisfies $V_0 = 0$:

    $$
    P(0,T)(F(0,T) - K^*) = 0 \implies K^* = F(0,T) = \frac{S_0}{P(0,T)}
    $$

---

**Exercise 3.**
In the Vasicek model with $\kappa = 0.3$, $\bar{r} = 0.05$, $\sigma_r = 0.02$, and $B(t,T) = (1 - e^{-\kappa(T-t)})/\kappa$, compute the bond volatility $\sigma_P(t,T) = -B(t,T)\sigma_r$ for $T - t = 5$. Write the drift adjustment for the short rate under $\mathbb{Q}^T$.

??? success "Solution to Exercise 3"
    With $\kappa = 0.3$, $\sigma_r = 0.02$, and $T - t = 5$:

    $$
    B(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa} = \frac{1 - e^{-0.3 \cdot 5}}{0.3} = \frac{1 - e^{-1.5}}{0.3} = \frac{1 - 0.22313}{0.3} = \frac{0.77687}{0.3} = 2.58957
    $$

    The bond volatility is:

    $$
    \sigma_P(t,T) = -B(t,T)\sigma_r = -2.58957 \cdot 0.02 = -0.05179
    $$

    Under $\mathbb{Q}^T$, the Brownian motion is $W_t^{\mathbb{Q}^T} = W_t^{\mathbb{Q}} - \int_0^t \sigma_P(s,T)\,ds$, and the short rate dynamics become:

    $$
    dr_t = [\kappa(\bar{r} - r_t) - \sigma_r^2 B(t,T)]\,dt + \sigma_r\,dW_t^{\mathbb{Q}^T}
    $$

    The drift adjustment is $-\sigma_r^2 B(t,T) = -(0.02)^2 \cdot 2.58957 = -0.001036$ (evaluated at $T - t = 5$). This term shifts the short rate drift downward, reflecting the convexity adjustment arising from the correlation between the bond price and the short rate.

---

**Exercise 4.**
A caplet with strike $K = 0.05$ on the LIBOR rate $L(T; T, T+\delta)$ with $\delta = 0.25$ pays $\delta(L_T - K)^+$ at $T + \delta$. If $L(0; T, T+\delta) = 0.048$ and the forward LIBOR volatility is $\sigma_L = 0.20$, use Black's formula to price the caplet under $\mathbb{Q}^{T+\delta}$. Assume $P(0, T+\delta) = 0.92$.

??? success "Solution to Exercise 4"
    Given: $K = 0.05$, $\delta = 0.25$, $L_0 = L(0;T,T+\delta) = 0.048$, $\sigma_L = 0.20$, $P(0,T+\delta) = 0.92$, and maturity $T$ (we need $T$ to compute $d_1, d_2$; we take $T = 1$ as a typical assumption).

    Under Black's formula for the caplet:

    $$
    V_0 = P(0,T+\delta) \cdot \delta \cdot [L_0\mathcal{N}(d_1) - K\mathcal{N}(d_2)]
    $$

    where

    $$
    d_1 = \frac{\ln(L_0/K) + \frac{1}{2}\sigma_L^2 T}{\sigma_L\sqrt{T}} = \frac{\ln(0.048/0.05) + \frac{1}{2}(0.04)(1)}{0.20 \cdot 1}
    $$

    $$
    = \frac{\ln(0.96) + 0.02}{0.20} = \frac{-0.04082 + 0.02}{0.20} = \frac{-0.02082}{0.20} = -0.1041
    $$

    $$
    d_2 = d_1 - \sigma_L\sqrt{T} = -0.1041 - 0.20 = -0.3041
    $$

    From normal distribution tables: $\Phi(-0.1041) \approx 0.4585$ and $\Phi(-0.3041) \approx 0.3806$.

    $$
    V_0 = 0.92 \cdot 0.25 \cdot [0.048 \cdot 0.4585 - 0.05 \cdot 0.3806]
    $$

    $$
    = 0.23 \cdot [0.02201 - 0.01903] = 0.23 \cdot 0.00298 \approx 0.000686
    $$

    The caplet price is approximately $0.0686\%$ of notional, or about $6.86$ basis points.

---

**Exercise 5.**
Explain why the forward price $F(t,T) = S_t / P(t,T)$ is a $\mathbb{Q}^T$-martingale but not a $\mathbb{Q}$-martingale in general. What is the drift of $F(t,T)$ under the standard risk-neutral measure $\mathbb{Q}$?

??? success "Solution to Exercise 5"
    Under $\mathbb{Q}$, the discounted price $S_t/B_t$ is a martingale, where $B_t = e^{\int_0^t r_s\,ds}$. The forward price is $F(t,T) = S_t/P(t,T)$. Writing $F(t,T) = (S_t/B_t) \cdot (B_t/P(t,T))$, note that $S_t/B_t$ is a $\mathbb{Q}$-martingale but $B_t/P(t,T)$ is a stochastic process (not constant), so their product $F(t,T)$ is generally **not** a $\mathbb{Q}$-martingale.

    To find the drift of $F$ under $\mathbb{Q}$, apply Itô's formula to $F = S/P$. Under $\mathbb{Q}$:

    $$
    \frac{dS_t}{S_t} = r_t\,dt + \sigma_S\,dW_t^{\mathbb{Q}}, \qquad \frac{dP(t,T)}{P(t,T)} = r_t\,dt + \sigma_P(t,T)\,dW_t^{\mathbb{Q}}
    $$

    By the quotient rule (Itô):

    $$
    \frac{dF}{F} = \frac{dS}{S} - \frac{dP}{P} + \left(\frac{dP}{P}\right)^2 - \frac{dS}{S}\frac{dP}{P}
    $$

    $$
    = (r_t - r_t + \sigma_P^2 - \sigma_S\sigma_P)\,dt + (\sigma_S - \sigma_P)\,dW_t^{\mathbb{Q}}
    $$

    $$
    = \sigma_P(\sigma_P - \sigma_S)\,dt + (\sigma_S - \sigma_P)\,dW_t^{\mathbb{Q}}
    $$

    The drift $\sigma_P(\sigma_P - \sigma_S)$ is generally nonzero, confirming $F$ is not a $\mathbb{Q}$-martingale. Under $\mathbb{Q}^T$, this drift vanishes by construction (the Girsanov shift absorbs it), making $F$ a $\mathbb{Q}^T$-martingale.

---

**Exercise 6.**
For two different maturities $T_1 < T_2$, write the Radon–Nikodym derivative $d\mathbb{Q}^{T_2}/d\mathbb{Q}^{T_1}|_{\mathcal{F}_t}$ and explain why the measures $\mathbb{Q}^{T_1}$ and $\mathbb{Q}^{T_2}$ differ. In which financial applications does the choice between these measures matter?

??? success "Solution to Exercise 6"
    The Radon–Nikodym derivative between the two forward measures is:

    $$
    \frac{d\mathbb{Q}^{T_2}}{d\mathbb{Q}^{T_1}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T_2)/P(0,T_2)}{P(t,T_1)/P(0,T_1)}
    $$

    The measures differ because they use different bonds as numéraires, leading to different probability tilts. Under $\mathbb{Q}^{T_1}$, the forward price $S_t/P(t,T_1)$ is a martingale, while under $\mathbb{Q}^{T_2}$, $S_t/P(t,T_2)$ is a martingale. The Girsanov kernel connecting them involves the volatility difference $\sigma_P(t,T_2) - \sigma_P(t,T_1)$.

    The choice between these measures matters in applications such as:

    - **Interest rate caps**: Each caplet with reset at $T_i$ is priced under $\mathbb{Q}^{T_{i+1}}$, so different caplets in the same cap use different forward measures.
    - **LIBOR Market Models (BGM)**: Forward LIBOR rates for different tenors are martingales under different forward measures, requiring careful measure changes when computing joint distributions.
    - **Convexity adjustments**: When a rate observed under one measure must be priced under another (e.g., CMS rates), the measure change introduces a convexity correction.

---

**Exercise 7.**
Consider the exchange option with payoff $(S_T^1 - S_T^2)^+$. Using $S_t^2$ as numeraire, derive Margrabe's formula. Explain why the interest rate $r$ does not appear in the final formula, and identify the relevant volatility parameter $\sigma$ in terms of $\sigma_1$, $\sigma_2$, and $\rho$.

??? success "Solution to Exercise 7"
    The exchange option has payoff $(S_T^1 - S_T^2)^+$. Using $N_t = S_t^2$ as numéraire, define the measure $\mathbb{Q}^{S^2}$ under which $S_t^1/S_t^2$ is a martingale.

    The price is:

    $$
    V_t = S_t^2 \cdot \mathbb{E}^{\mathbb{Q}^{S^2}}\!\left[\left(\frac{S_T^1}{S_T^2} - 1\right)^+\;\middle|\;\mathcal{F}_t\right]
    $$

    Let $R_t = S_t^1/S_t^2$. Under $\mathbb{Q}^{S^2}$, $R_t$ is a martingale. If both assets follow geometric Brownian motions under $\mathbb{Q}$ with volatilities $\sigma_1, \sigma_2$ and correlation $\rho$, then $R_t$ is log-normal under $\mathbb{Q}^{S^2}$ with volatility

    $$
    \sigma = \sqrt{\sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2}
    $$

    Since $R_t$ is a martingale, its log-normal dynamics have zero drift (in the risk-neutral sense for this numéraire), and the problem reduces to a Black-Scholes call with underlying $R_t$, strike 1, and volatility $\sigma$. Multiplying by $S_t^2$:

    $$
    V_t = S_t^1\mathcal{N}(d_1) - S_t^2\mathcal{N}(d_2)
    $$

    where

    $$
    d_1 = \frac{\ln(S_t^1/S_t^2) + \frac{1}{2}\sigma^2(T-t)}{\sigma\sqrt{T-t}}, \qquad d_2 = d_1 - \sigma\sqrt{T-t}
    $$

    The interest rate $r$ does not appear because both $S^1$ and $S^2$ grow at rate $r$ under $\mathbb{Q}$, and the ratio $S_t^1/S_t^2$ cancels this common growth. Equivalently, the option is self-financing when denominated in either asset, so no external financing (at rate $r$) is needed. The only relevant parameter is the volatility $\sigma$ of the ratio process, which depends on $\sigma_1$, $\sigma_2$, and $\rho$.
