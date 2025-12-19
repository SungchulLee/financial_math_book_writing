# Numéraire and Change of Measure

This section develops the **numéraire viewpoint** and the associated **change of measure** technique, which naturally follow from the Fundamental Theorem of Asset Pricing (FTAP). While the FTAP guarantees the existence of an equivalent martingale measure (EMM), the choice of numéraire determines *which* martingale measure is used and how prices are represented.

---

## Numéraire: Definition and Generality

A **numéraire** is any strictly positive traded asset (N_t > 0) almost surely for all (t). The only mathematical requirement is strict positivity, ensuring that all prices can be normalized relative to (N_t).

Typical examples include:

* A risk-free money market account (N_t = e^{rt})
* A zero-coupon bond
* A risky stock (e.g. an equity index or individual stock)
* A portfolio of traded assets

There is **no requirement** that the numéraire be risk-free. The frequent use of the risk-free bond is a matter of convenience, not necessity.

---

## Discounted Prices and Numéraire Measures

Given a choice of numéraire (N_t), define **normalized prices**

[
\tilde{S}^i_t := \frac{S^i_t}{N_t},
]

for all traded assets (S^i_t).

The FTAP implies:

> **Numéraire Version of FTAP.**
> A market is arbitrage-free if and only if there exists a probability measure (\mathbb{Q}^N), equivalent to the physical measure (\mathbb{P}), under which all normalized prices (\tilde{S}^i_t) are martingales.

The measure (\mathbb{Q}^N) is called the **numéraire-associated martingale measure**.

---

## Pricing with a General Numéraire

Let (\Phi_T) be a contingent claim payable at time (T). Under the numéraire (N_t), its arbitrage-free price process is

[
V_t = N_t , \mathbb{E}^{\mathbb{Q}^N}!\left[\frac{\Phi_T}{N_T} \mid \mathcal{F}_t\right].
]

This formula generalizes the familiar risk-neutral valuation formula obtained when the money market account is used as numéraire.

---

## Change of Numéraire Theorem

Let (N_t) and (M_t) be two numéraires with associated martingale measures (\mathbb{Q}^N) and (\mathbb{Q}^M). Then the two measures are related by the **Radon–Nikodym derivative**

[
\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\bigg|_{\mathcal{F}_T}
= \frac{M_T / M_0}{N_T / N_0}.
]

> **Change of Numéraire Theorem.**
> Prices are invariant under a change of numéraire: for any payoff (\Phi_T),
>
> [
> N_t , \mathbb{E}^{\mathbb{Q}^N}!\left[\frac{\Phi_T}{N_T} \mid \mathcal{F}_t\right]
> ==================================================================================
>
> M_t , \mathbb{E}^{\mathbb{Q}^M}!\left[\frac{\Phi_T}{M_T} \mid \mathcal{F}_t\right].
> ]

Thus, different numéraires yield different martingale measures but **the same arbitrage-free prices**.

---

## Examples of Useful Numéraires

### Risk-Free Money Market Account

Choosing (N_t = e^{rt}) leads to the standard **risk-neutral measure** (\mathbb{Q}), under which discounted asset prices are martingales:

[
e^{-rt} S_t = \mathbb{E}^{\mathbb{Q}}!\left[e^{-rT} S_T \mid \mathcal{F}_t\right].
]

This choice yields the familiar pricing formula

[
V_t = e^{-r(T-t)} , \mathbb{E}^{\mathbb{Q}}[\Phi_T \mid \mathcal{F}_t].
]

---

### Zero-Coupon Bond and Forward Measure

Let (N_t = P(t,T)) be the price of a zero-coupon bond maturing at (T). Under the associated **(T)-forward measure** (\mathbb{Q}^T),

[
\frac{S_t}{P(t,T)}
= \mathbb{E}^{\mathbb{Q}^T}!\left[\frac{S_T}{P(T,T)} \mid \mathcal{F}_t\right]
= \mathbb{E}^{\mathbb{Q}^T}[S_T \mid \mathcal{F}_t].
]

Forward measures are fundamental in interest-rate modeling and the pricing of caps, floors, and swaptions.

---

### Stock as Numéraire

A risky asset, such as a stock (S^j_t), may also serve as numéraire. Under the corresponding measure (\mathbb{Q}^j), relative prices satisfy

[
\frac{S^i_t}{S^j_t}
= \mathbb{E}^{\mathbb{Q}^j}!\left[\frac{S^i_T}{S^j_T} \mid \mathcal{F}_t\right].
]

This approach is particularly useful for equity derivatives and foreign exchange models.

---

## Connection to Black–Scholes

In the Black–Scholes model

[
dS_t = \mu S_t , dt + \sigma S_t , dW_t,
]

choosing the money market account as numéraire produces the risk-neutral measure under which

[
dS_t = r S_t , dt + \sigma S_t , dW_t^{\mathbb{Q}}.
]

Because there is a single source of randomness, the market is complete and the martingale measure is unique. Choosing alternative numéraires (e.g. the stock itself) leads to equivalent pricing formulas under different measures.

---

## Interpretation and Significance

* The numéraire represents a **choice of units** in which prices are measured.
* Different numéraires correspond to different martingale measures, but not different prices.
* Change of numéraire is a powerful computational tool for simplifying expectations.
* The theory highlights the deep connection between pricing, probability measures, and market structure.

---

## Summary

The numéraire framework extends the FTAP by showing that arbitrage-free pricing is invariant under the choice of reference asset. Any strictly positive traded asset may serve as numéraire, leading to a corresponding martingale measure. Change-of-numéraire techniques play a central role in modern derivative pricing, particularly in interest-rate, foreign exchange, and equity markets.
