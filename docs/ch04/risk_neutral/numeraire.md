# Numéraire and Change of Measure

Changing the **numéraire** (unit of account) provides a powerful and elegant framework for derivative pricing. Each choice of numéraire corresponds to a different equivalent martingale measure, and selecting the right numéraire often dramatically simplifies pricing formulas.

The risk-neutral measure $\mathbb{Q}$ uses the money market account $B_t$ as numéraire.
But there is nothing special about $B_t$: any strictly positive traded asset can serve as
the unit of value. Changing the numéraire is equivalent to **changing the unit in which
all prices are measured**. Just as switching from dollars to euros does not alter the
economic content of a trade, switching from $B_t$ to a bond $P(t,T)$ or a stock $S_t$
does not change which strategies are arbitrage-free --- it only changes the probability
measure under which relative prices are martingales. Choosing the right unit often
turns a difficult pricing problem into a simple one.

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

**Theorem**: Let $N_t$ be any positive traded asset (numéraire). There exists (under the absence of arbitrage in the sense of NFLVR and the Fundamental Theorem of Asset Pricing) a probability measure $\mathbb{Q}^N$ equivalent to $\mathbb{P}$ such that for **any** traded asset $S_t$:

$$
\boxed{
\frac{S_t}{N_t} \text{ is a } \mathbb{Q}^N\text{-martingale}
}
$$

The intuition is direct: if $N_t$ is the unit of value, then no-arbitrage requires every
asset price expressed in that unit to have zero expected excess return --- that is,
zero drift, which is exactly the martingale property. If this were not true, one could
construct a trading strategy that generates profit in units of the numéraire without
risk, violating no-arbitrage.

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

**Interpretation**: The likelihood ratio equals the relative performance of the two
numéraires. Paths on which $N$ outperforms $M$ receive higher weight under
$\mathbb{Q}^N$ than under $\mathbb{Q}^M$, and vice versa. A one-step intuition: if the
only traded assets are $M$ and $N$, then $N_t / M_t$ must be a $\mathbb{Q}^M$-martingale.
Multiplying by $M_0 / N_0$ produces the Radon–Nikodym derivative $Z_T$, which is
therefore itself a $\mathbb{Q}^M$-martingale with expectation 1.

### Special Case: Money Market to Bond

From $\mathbb{Q}$ (money market numéraire $B_t$) to $\mathbb{Q}^T$ (bond numéraire $P(t,T)$):

$$
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{P(T,T)/P(0,T)}{B_T/B_0} = \frac{1}{P(0,T)B_T} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
$$

---

## The T-Forward Measure

The most important special case: the **$T$-forward measure** $\mathbb{Q}^T$ uses the
zero-coupon bond $P(t,T)$ as numéraire, making the forward price
$F(t,T) = S_t/P(t,T)$ a martingale. This eliminates stochastic discounting:

$$
V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi(S_T) \mid \mathcal{F}_t]
$$

See [The Forward Measure](forward_measure.md) for the full development, including
dynamics under $\mathbb{Q}^T$, LIBOR forward rates, and caplet pricing.

---

## Example: Black's Formula

Recall (see [§ Forward Measure, Caplet Pricing](forward_measure.md#caplet-pricing) and [§ Forward Contract](forward_measure.md#example-forward-contract)): switching to the $T$-forward measure turns $C_t = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}(F_T-K)^+ \mid \mathcal{F}_t]$ into $C_t = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}[(F_T-K)^+ \mid \mathcal{F}_t]$, which evaluates to the Black (1976) formula $C_t = P(t,T)[F_t\mathcal{N}(d_1)-K\mathcal{N}(d_2)]$ when $F$ is log-normal under $\mathbb{Q}^T$.

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
V_t = S_t^1\mathcal{N}(d_1) - S_t^2\mathcal{N}(d_2)
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

Recall (see [§ Construction of $\mathbb{Q}$](construction.md#risk-neutral-dynamics)) under $\mathbb{Q}$: $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$.

Recall (see [§ Forward Measure, Asset Dynamics](forward_measure.md#asset-dynamics)) under $\mathbb{Q}^T$: $dS_t = (r + \sigma\sigma_P\rho_{S,P})S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^T}$.

Under the **stock measure** $\mathbb{Q}^S$ (numéraire $S_t$), the drift acquires the convexity adjustment $\sigma^2$:

$$
dS_t = (r + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^S}
$$

(derived from $d\mathbb{Q}^S/d\mathbb{Q} = S_T/(S_0 B_T)$; see Exercise 5).

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

!!! abstract "The master pricing principle"

    All derivative pricing reduces to three steps:

    1. **Choose** a numéraire $N_t$.
    2. **Find** the associated measure $\mathbb{Q}^N$ under which $S_t / N_t$ is a martingale.
    3. **Price**: $V_t = N_t\,\mathbb{E}^{\mathbb{Q}^N}[\Phi_T / N_T \mid \mathcal{F}_t]$.

    Everything else --- Black-Scholes, Black's formula, Margrabe, caplet pricing --- is a
    particular choice of convenience.

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

All numéraire-induced measures are **equivalent** to one another and to $\mathbb{P}$:
they agree on which events are possible and differ only in how they weight outcomes.
The choice of numéraire is a choice of perspective, not of economic content.

**Numéraire techniques are essential for interest rate derivatives, FX options, and multi-asset problems.**

---

## Exercises

**Exercise 1.**
Verify the change-of-numeraire formula: if $M_t = B_t$ (money market) and $N_t = P(t,T)$ (zero-coupon bond), write $d\mathbb{Q}^T / d\mathbb{Q}|_{\mathcal{F}_T}$ and show that it equals $e^{-\int_0^T r_s\,ds} / P(0,T)$. Confirm that this is a valid Radon–Nikodym derivative by showing its $\mathbb{Q}$-expectation is 1.

??? success "Solution to Exercise 1"
    With $M_t = B_t$ and $N_t = P(t,T)$, the change-of-numéraire formula gives:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{N_T/N_0}{M_T/M_0} = \frac{P(T,T)/P(0,T)}{B_T/B_0}
    $$

    Since $P(T,T) = 1$, $B_0 = 1$, and $B_T = e^{\int_0^T r_s\,ds}$:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{1/P(0,T)}{e^{\int_0^T r_s\,ds}} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
    $$

    To confirm this is a valid Radon–Nikodym derivative, we verify $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^T/d\mathbb{Q}|_{\mathcal{F}_T}] = 1$. Under $\mathbb{Q}$, the discounted bond price $P(t,T)/B_t$ is a martingale, so:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{P(T,T)}{B_T}\right] = \frac{P(0,T)}{B_0} = P(0,T)
    $$

    Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}\right] = \frac{1}{P(0,T)} \cdot P(0,T) = 1
    $$

---

**Exercise 2.**
Under the stock measure $\mathbb{Q}^S$ (numeraire $N_t = S_t$), a European put option with payoff $(K - S_T)^+$ has price $V_t = S_t \cdot \mathbb{E}^{\mathbb{Q}^S}[(K/S_T - 1)^+ | \mathcal{F}_t]$. Explain why this formulation is useful, and describe how the distribution of $1/S_T$ under $\mathbb{Q}^S$ differs from the distribution of $S_T$ under $\mathbb{Q}$.

??? success "Solution to Exercise 2"
    Under the stock measure $\mathbb{Q}^S$ with numéraire $N_t = S_t$, the price of any claim $\Phi_T$ is $V_t = S_t \cdot \mathbb{E}^{\mathbb{Q}^S}[\Phi_T/S_T \mid \mathcal{F}_t]$. For a put with payoff $(K - S_T)^+$:

    $$
    V_t = S_t \cdot \mathbb{E}^{\mathbb{Q}^S}\!\left[\frac{(K - S_T)^+}{S_T}\;\middle|\;\mathcal{F}_t\right] = S_t \cdot \mathbb{E}^{\mathbb{Q}^S}\!\left[\left(\frac{K}{S_T} - 1\right)^+\;\middle|\;\mathcal{F}_t\right]
    $$

    This formulation is useful because it reframes the put as a call on $K/S_T$ (with strike 1), reducing the problem to pricing a call-like payoff under a different measure.

    Under $\mathbb{Q}$, if $S_T$ is log-normal: $\ln S_T \sim N(\ln S_0 + (r - \sigma^2/2)T, \sigma^2 T)$. Under $\mathbb{Q}^S$, the Radon–Nikodym derivative shifts the distribution. Specifically, $d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_T} = S_T/(S_0 B_T)$, which multiplies the density by $S_T$, effectively shifting the mean of $\ln S_T$ by $+\sigma^2 T$. Under $\mathbb{Q}^S$:

    $$
    \ln S_T \sim N(\ln S_0 + (r + \sigma^2/2)T,\; \sigma^2 T)
    $$

    Therefore $1/S_T$ under $\mathbb{Q}^S$ has a log-normal distribution with parameters $(-\ln S_0 - (r + \sigma^2/2)T, \sigma^2 T)$, which differs from the distribution of $S_T$ under $\mathbb{Q}$ by both the sign and the drift adjustment.

---

**Exercise 3.**
For Black's formula, a call on a forward contract has price $C_t = P(t,T)[F_t\mathcal{N}(d_1) - K\mathcal{N}(d_2)]$. Verify that as $\sigma_F \to 0$, the formula reduces to $C_t = P(t,T)\max(F_t - K, 0)$. What is the interpretation of this limit?

??? success "Solution to Exercise 3"
    As $\sigma_F \to 0$: $d_1 = [\ln(F_t/K) + \frac{1}{2}\sigma_F^2(T-t)]/(\sigma_F\sqrt{T-t})$.

    **Case 1: $F_t > K$.** Then $\ln(F_t/K) > 0$. As $\sigma_F \to 0$, $d_1 \to +\infty$ and $d_2 \to +\infty$, so $\mathcal{N}(d_1) \to 1$ and $\mathcal{N}(d_2) \to 1$:

    $$
    C_t \to P(t,T)(F_t - K) = P(t,T)\max(F_t - K, 0)
    $$

    **Case 2: $F_t < K$.** Then $\ln(F_t/K) < 0$. As $\sigma_F \to 0$, $d_1 \to -\infty$ and $d_2 \to -\infty$, so $\mathcal{N}(d_1) \to 0$ and $\mathcal{N}(d_2) \to 0$:

    $$
    C_t \to 0 = P(t,T)\max(F_t - K, 0)
    $$

    **Case 3: $F_t = K$.** Then $d_1 = \frac{1}{2}\sigma_F\sqrt{T-t} \to 0$ and $\mathcal{N}(d_1) \to 1/2$, $\mathcal{N}(d_2) \to 1/2$, giving $C_t \to 0$.

    In all cases, $C_t \to P(t,T)\max(F_t - K, 0)$. The interpretation is that with zero volatility, the forward price is deterministic, so the option value is simply the discounted intrinsic value. There is no time value when there is no uncertainty.

---

**Exercise 4.**
In the exchange option (Margrabe's formula), the price is $V_t = S_t^1\mathcal{N}(d_1) - S_t^2\mathcal{N}(d_2)$. Explain why the risk-free rate $r$ does not appear. Compute $V_0$ for $S_0^1 = 100$, $S_0^2 = 95$, $\sigma_1 = 0.20$, $\sigma_2 = 0.25$, $\rho = 0.5$, and $T = 1$.

??? success "Solution to Exercise 4"
    The interest rate $r$ does not appear because the exchange option payoff $(S_T^1 - S_T^2)^+$ can be replicated by a portfolio that is long asset 1 and short asset 2. Both assets grow at the same risk-free rate $r$ under $\mathbb{Q}$, and this common growth cancels in the ratio $S_t^1/S_t^2$. Using $S^2$ as numéraire eliminates $r$ entirely.

    Computing $V_0$ with $S_0^1 = 100$, $S_0^2 = 95$, $\sigma_1 = 0.20$, $\sigma_2 = 0.25$, $\rho = 0.5$, $T = 1$:

    $$
    \sigma = \sqrt{0.04 + 0.0625 - 2(0.5)(0.20)(0.25)} = \sqrt{0.04 + 0.0625 - 0.05} = \sqrt{0.0525} = 0.22913
    $$

    $$
    d_1 = \frac{\ln(100/95) + \frac{1}{2}(0.0525)(1)}{0.22913} = \frac{0.05129 + 0.02625}{0.22913} = \frac{0.07754}{0.22913} = 0.33841
    $$

    $$
    d_2 = 0.33841 - 0.22913 = 0.10928
    $$

    From normal tables: $\Phi(0.33841) \approx 0.6325$ and $\Phi(0.10928) \approx 0.5435$.

    $$
    V_0 = 100 \cdot 0.6325 - 95 \cdot 0.5435 = 63.25 - 51.63 = 11.62
    $$

---

**Exercise 5.**
Under the money market numeraire, $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. Under the stock measure, $dS_t = (r + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^S}$. Derive the drift change $r \to r + \sigma^2$ using the Girsanov kernel implicit in the numeraire change from $B_t$ to $S_t$.

??? success "Solution to Exercise 5"
    Under $\mathbb{Q}$ (numéraire $B_t$), $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. Changing to the stock measure $\mathbb{Q}^S$ (numéraire $S_t$), the Radon–Nikodym derivative is:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{S_T/S_0}{B_T/B_0} = \frac{S_T}{S_0 e^{rT}}
    $$

    Since $S_T = S_0\exp((r - \sigma^2/2)T + \sigma W_T^{\mathbb{Q}})$:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \exp\!\left(-\frac{\sigma^2}{2}T + \sigma W_T^{\mathbb{Q}}\right)
    $$

    This is the stochastic exponential with Girsanov kernel $\gamma = -\sigma$ (note: the standard form is $\exp(-\gamma W_T - \frac{1}{2}\gamma^2 T)$, so $\gamma = -\sigma$). By Girsanov's theorem:

    $$
    W_t^{\mathbb{Q}^S} = W_t^{\mathbb{Q}} - \sigma t
    $$

    is a Brownian motion under $\mathbb{Q}^S$. Substituting $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{Q}^S} + \sigma\,dt$:

    $$
    dS_t = rS_t\,dt + \sigma S_t(dW_t^{\mathbb{Q}^S} + \sigma\,dt) = (r + \sigma^2)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}^S}
    $$

    The drift shifts from $r$ to $r + \sigma^2$, which is the convexity adjustment arising from the nonlinearity of the numéraire change.

---

**Exercise 6.**
The annuity numeraire is $A(t) = \sum_{i=1}^n \tau_i P(t, T_i)$. Under the swap measure $\mathbb{Q}^A$, the swap rate $S(t) = (P(t,T_0) - P(t,T_n))/A(t)$ is a martingale. Explain why this makes Black's model applicable to swaptions. What assumption about the swap rate distribution is needed?

??? success "Solution to Exercise 6"
    Under the swap measure $\mathbb{Q}^A$ with numéraire $A(t) = \sum_{i=1}^n \tau_i P(t,T_i)$, the price of a swaption (option to enter a swap) with payoff $A(T_0)(S(T_0) - K)^+$ at time $T_0$ is:

    $$
    V_t = A(t) \cdot \mathbb{E}^{\mathbb{Q}^A}[(S(T_0) - K)^+ \mid \mathcal{F}_t]
    $$

    Since $S(t)$ is a $\mathbb{Q}^A$-martingale, this has the same structure as a call option on a martingale. If we assume $S(t)$ is **log-normal** under $\mathbb{Q}^A$ with volatility $\sigma_S$, then Black's formula applies directly:

    $$
    V_t = A(t)[S(t)\mathcal{N}(d_1) - K\mathcal{N}(d_2)]
    $$

    The key assumption is that the swap rate $S(t)$ follows a geometric Brownian motion (log-normal distribution) under $\mathbb{Q}^A$. This is the standard market model assumption for swaptions, analogous to assuming log-normality of the forward rate for caplets. In practice, implied volatility smiles indicate deviations from this assumption.

---

**Exercise 7.**
Consider a quanto option: a European call on a foreign stock $S_t^f$ with strike $K$, where the payoff $(S_T^f - K)^+$ is paid in domestic currency. The relevant numeraire is the foreign money market account converted to domestic currency: $N_t = B_t^f X_t$. Write the pricing formula under the corresponding measure and explain what "quanto adjustment" is needed for the drift of $S_t^f$.

??? success "Solution to Exercise 7"
    The quanto option pays $(S_T^f - K)^+$ in domestic currency. Under the domestic risk-neutral measure $\mathbb{Q}^d$ with numéraire $B_t^d$:

    $$
    V_t = \mathbb{E}^{\mathbb{Q}^d}\!\left[e^{-\int_t^T r_d\,ds}(S_T^f - K)^+\;\middle|\;\mathcal{F}_t\right]
    $$

    The challenge is that $S_T^f$ is a foreign asset. Under $\mathbb{Q}^d$, the drift of $S_t^f$ is not simply $r_f$. To find it, note that $S_t^f X_t$ (the domestic-currency value of the foreign stock) must grow at rate $r_d$ under $\mathbb{Q}^d$. If $dS_t^f/S_t^f = \mu_S\,dt + \sigma_S\,dW_t^1$ and $dX_t/X_t = \mu_X\,dt + \sigma_X\,dW_t^2$ with $\text{Corr}(dW^1, dW^2) = \rho_{SX}$, then by Itô's formula applied to $S_t^f X_t$:

    $$
    \frac{d(S_t^f X_t)}{S_t^f X_t} = (\mu_S + \mu_X + \rho_{SX}\sigma_S\sigma_X)\,dt + \cdots
    $$

    Under $\mathbb{Q}^d$, $\mu_X = r_d - r_f$ and the drift of $S_t^f X_t$ must be $r_d$. This gives $\mu_S = r_f - \rho_{SX}\sigma_S\sigma_X$.

    The **quanto adjustment** is the term $-\rho_{SX}\sigma_S\sigma_X$: under $\mathbb{Q}^d$, the foreign stock drifts at rate $r_f - \rho_{SX}\sigma_S\sigma_X$ instead of $r_f$. The pricing formula is then a modified Black-Scholes formula:

    $$
    V_t = e^{-r_d(T-t)}[S_t^f e^{(r_f - \rho_{SX}\sigma_S\sigma_X)(T-t)}\mathcal{N}(d_1) - K\mathcal{N}(d_2)]
    $$

    where $d_1$ and $d_2$ use the adjusted drift. The quanto adjustment captures the correlation between the foreign asset and the exchange rate: if $\rho_{SX} > 0$, when the foreign stock rises, the domestic currency weakens, reducing the domestic-currency payoff, leading to a lower effective drift.
