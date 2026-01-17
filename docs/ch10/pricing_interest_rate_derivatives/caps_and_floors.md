# Caps and Floors

**Caps** and **floors** are the most liquid interest rate options. A cap protects against rising rates; a floor protects against falling rates. They are portfolios of individual options called **caplets** and **floorlets**.

---

## Definitions

### Interest Rate Cap

A **cap** is a contract that pays the holder when a floating rate exceeds a strike rate $K$.

**Structure:**
- Notional: $N$
- Strike: $K$
- Reset dates: $T_0, T_1, \ldots, T_{n-1}$
- Payment dates: $T_1, T_2, \ldots, T_n$
- Underlying rate: $L(T_i, T_{i+1})$ (e.g., LIBOR or SOFR)

**Caplet payoff** at $T_{i+1}$:

$$
N \cdot \delta_i \cdot \max(L(T_i, T_{i+1}) - K, 0)
$$

where $\delta_i = T_{i+1} - T_i$ is the accrual fraction (day count adjusted).

### Interest Rate Floor

A **floor** pays when the floating rate falls below $K$:

$$
N \cdot \delta_i \cdot \max(K - L(T_i, T_{i+1}), 0)
$$

### Cap = Sum of Caplets

$$
\text{Cap} = \sum_{i=0}^{n-1} \text{Caplet}_i
$$

Each caplet is valued independently and summed.

---

## Cap-Floor Parity

### Relationship

A long cap and short floor with the same strike and dates equals a payer swap:

$$
\text{Cap} - \text{Floor} = \text{Payer Swap}
$$

**Proof:** For each period:

$$
\max(L - K, 0) - \max(K - L, 0) = L - K
$$

This is the floating-minus-fixed payment of a payer swap.

### Implications

- ATM cap and floor have the same value (since ATM swap has zero value)
- Out-of-the-money cap = In-the-money floor (by parity)
- Provides arbitrage relationship for pricing consistency

---

## Black's Model for Caps

### Model Assumption

Under the $T_{i+1}$-forward measure, the forward rate $F_i(t) = F(t; T_i, T_{i+1})$ is a **martingale** with lognormal dynamics:

$$
\frac{dF_i(t)}{F_i(t)} = \sigma_i \, dW_t^{T_{i+1}}
$$

where $\sigma_i$ is the **caplet volatility** for period $i$.

### Black's Caplet Formula

$$
\boxed{\text{Caplet}_i = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot [F_i N(d_1) - K N(d_2)]}
$$

where:

$$
d_1 = \frac{\ln(F_i/K) + \frac{1}{2}\sigma_i^2 T_i}{\sigma_i \sqrt{T_i}}
$$

$$
d_2 = d_1 - \sigma_i \sqrt{T_i}
$$

and:
- $F_i = F(0; T_i, T_{i+1})$ is the current forward rate
- $P(0, T_{i+1})$ is the discount factor
- $\sigma_i$ is the Black (lognormal) volatility

### Floorlet Formula

$$
\text{Floorlet}_i = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot [K N(-d_2) - F_i N(-d_1)]
$$

---

## Caplet Pricing in Short-Rate Models

### Caplet as Bond Put

The caplet paying $\delta \max(L(T_1, T_2) - K, 0)$ at $T_2$ can be rewritten.

At time $T_1$, the floating rate is:

$$
L(T_1, T_2) = \frac{1}{\delta} \left(\frac{1}{P(T_1, T_2)} - 1\right)
$$

So:

$$
\delta \max(L - K, 0) = \max\left(1 - (1 + K\delta)P(T_1, T_2), 0\right)
$$

This is $(1 + K\delta)$ times a **put option** on a zero-coupon bond with strike $K_P = 1/(1 + K\delta)$.

### Caplet Formula (Hull-White)

$$
\text{Caplet} = (1 + K\delta) \cdot \left[K_P P(0, T_1) N(-d_2) - P(0, T_2) N(-d_1)\right]
$$

where:

$$
d_1 = \frac{1}{\sigma_P} \ln \frac{P(0, T_2)}{K_P P(0, T_1)} + \frac{\sigma_P}{2}
$$

$$
\sigma_P = \sigma \cdot B(T_2 - T_1) \cdot \sqrt{\frac{1 - e^{-2\kappa T_1}}{2\kappa}}
$$

---

## Flat Volatility vs. Spot Volatility

### Flat (Cap) Volatility

Market quotes a single volatility $\sigma_{\text{flat}}$ for an entire cap. This is the volatility that, when used for all caplets, reproduces the cap price.

### Spot (Caplet) Volatilities

The **spot volatility** $\sigma_i$ is the individual volatility for caplet $i$. The relationship:

$$
\text{Cap Price} = \sum_i \text{Caplet}_i(\sigma_i)
$$

can also be written:

$$
\text{Cap Price} = \sum_i \text{Caplet}_i(\sigma_{\text{flat}})
$$

### Stripping Spot Volatilities

Given flat volatilities for caps of increasing maturity, **bootstrap** spot volatilities:

1. Start with the shortest cap (1 caplet): $\sigma_1 = \sigma_{\text{flat},1}$
2. For cap with $n$ caplets: solve for $\sigma_n$ given $\sigma_1, \ldots, \sigma_{n-1}$

$$
\text{Cap}_n(\sigma_{\text{flat},n}) = \sum_{i=1}^{n-1} \text{Caplet}_i(\sigma_i) + \text{Caplet}_n(\sigma_n)
$$

Solve for $\sigma_n$.

---

## Normal (Bachelier) Model

### Motivation

With negative rates, lognormal models break down. The **Bachelier model** assumes normal (Gaussian) dynamics:

$$
dF_i(t) = \sigma_i^{(n)} \, dW_t
$$

### Bachelier Caplet Formula

$$
\text{Caplet}_i = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot \left[(F_i - K) N(d) + \sigma_i^{(n)} \sqrt{T_i} \phi(d)\right]
$$

where:

$$
d = \frac{F_i - K}{\sigma_i^{(n)} \sqrt{T_i}}
$$

### Conversion

For ATM options:

$$
\sigma^{(n)} \approx F \cdot \sigma^{(\text{Black})}
$$

This approximate relationship helps convert between conventions.

---

## Calibration to Caps

### Market Data

The market provides:
- Cap prices (or flat implied volatilities) for various strikes and maturities
- Sometimes explicit caplet volatilities

### Calibration Procedure

**For Black's model:**
- Input: flat vol → strip to spot vols → use for pricing

**For short-rate models (e.g., Hull-White):**
1. Fix $\kappa$ (often from other considerations)
2. Fit $\sigma$ (or $\sigma(t)$) to match market cap prices

**Objective:**

$$
\min_{\sigma} \sum_{i} w_i \left(C_i^{\text{model}}(\sigma) - C_i^{\text{market}}\right)^2
$$

### Term Structure of Volatility

The spot volatility term structure $T \mapsto \sigma(T)$ reveals:
- Humped shape: volatility peaks at intermediate maturities
- Downward sloping: short-term rates more volatile
- Upward sloping: long-term uncertainty dominates

---

## Greeks for Caps

### Cap Delta

Sensitivity to forward rate movements:

$$
\Delta_{\text{cap}} = \sum_i \Delta_{\text{caplet},i}
$$

Each caplet delta:

$$
\Delta_{\text{caplet},i} = N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot N(d_1)
$$

### Cap Vega

Sensitivity to volatility:

$$
\mathcal{V}_{\text{cap}} = \sum_i N \cdot \delta_i \cdot P(0, T_{i+1}) \cdot F_i \sqrt{T_i} \phi(d_1)
$$

### Bucket Deltas

Sensitivity to individual forward rates:

$$
\frac{\partial \text{Cap}}{\partial F_j} = \frac{\partial \text{Caplet}_j}{\partial F_j}
$$

Each caplet depends only on its own forward rate.

---

## ATM Caps and the Normal Approximation

### ATM Strike

The **at-the-money** (ATM) strike is typically defined as the forward swap rate:

$$
K_{\text{ATM}} = \frac{P(0, T_0) - P(0, T_n)}{\sum_{i=1}^{n} \delta_i P(0, T_{i})}
$$

### ATM Cap Value (Approximate)

For ATM caps, a useful approximation:

$$
\text{ATM Cap} \approx \sigma \sqrt{T} \cdot \text{Annuity} \cdot \sqrt{\frac{2}{\pi}}
$$

This "rule of 40" helps with quick sanity checks.

---

## Collar = Cap - Floor

### Definition

A **collar** combines:
- Long cap at strike $K_H$ (high)
- Short floor at strike $K_L$ (low)

where $K_L < K_H$.

### Payoff

The floating rate is effectively bounded:

$$
\text{Effective Rate} = \min(\max(L, K_L), K_H)
$$

### Pricing

$$
\text{Collar} = \text{Cap}(K_H) - \text{Floor}(K_L)
$$

Often structured as **zero-cost collars** where premium paid for cap equals premium received for floor.

---

## Practical Considerations

### Market Conventions

| Item | Convention |
|------|------------|
| Day count | ACT/360 (USD), ACT/365 (GBP) |
| Quote | Flat volatility or price |
| Settlement | Spot or forward-starting |
| Premium | Upfront or amortized |

### Liquidity

- ATM caps are most liquid
- Short-dated caps (1-5 year) more liquid than long-dated
- Cap-floor parity should hold tightly

### Hedging

- Delta-hedge with forwards or futures
- Vega-hedge with other caps or swaptions
- Gamma exposure requires dynamic hedging

---

## Key Takeaways

- Cap = portfolio of caplets; Floor = portfolio of floorlets
- Cap - Floor = Payer Swap (cap-floor parity)
- Black's formula: $\text{Caplet} = N\delta P(0,T_{i+1})[F N(d_1) - K N(d_2)]$
- Caplet = Put on bond (in short-rate models)
- Flat vs. spot volatilities: stripping procedure
- Bachelier model handles negative rates
- Calibration: strip vol or fit model to cap prices

---

## Further Reading

- Hull, *Options, Futures, and Other Derivatives*, Chapters 29-30
- Brigo & Mercurio, *Interest Rate Models*, Chapter 1 and 6
- Rebonato, *Interest Rate Option Models*
