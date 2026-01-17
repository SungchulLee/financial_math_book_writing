# Forward Rates and Term Structures

Forward rates describe **future borrowing/lending rates** implied by today's yield curve. They are central to term-structure modeling, pricing FRAs and swaps, and understanding no-arbitrage dynamics of interest rates.

---

## Simple Forward Rates from Discount Factors

### Definition

Given discount factors $P(0,T_1)$ and $P(0,T_2)$ with $0 < T_1 < T_2$, the **simple forward rate** over the period $[T_1, T_2]$ is defined by the no-arbitrage relation:

$$
P(0,T_1) = P(0,T_2) \cdot \left[1 + F(0; T_1, T_2) \cdot (T_2 - T_1)\right]
$$

Solving for the forward rate:

$$
F(0; T_1, T_2) = \frac{1}{T_2 - T_1} \left(\frac{P(0,T_1)}{P(0,T_2)} - 1\right)
$$

### Economic Interpretation

The forward rate $F(0; T_1, T_2)$ is:
- The rate that can be **locked in today** for borrowing/lending over $[T_1, T_2]$
- The rate that makes a **forward-starting loan** have zero initial value
- The **break-even rate** for the period, given the current term structure

### Time-$t$ Forward Rates

More generally, the forward rate observed at time $t$ for the period $[T_1, T_2]$ is:

$$
F(t; T_1, T_2) = \frac{1}{T_2 - T_1} \left(\frac{P(t,T_1)}{P(t,T_2)} - 1\right)
$$

This forward rate evolves stochastically as market conditions change.

---

## Continuously Compounded Forward Rates

Using continuous compounding, the forward rate $f_c(0; T_1, T_2)$ satisfies:

$$
e^{-z(0,T_1) T_1} = e^{-z(0,T_2) T_2} \cdot e^{f_c(0; T_1, T_2)(T_2 - T_1)}
$$

Solving:

$$
f_c(0; T_1, T_2) = \frac{z(0,T_2) T_2 - z(0,T_1) T_1}{T_2 - T_1}
$$

This can be rewritten as:

$$
f_c(0; T_1, T_2) = \frac{-\log P(0,T_2) + \log P(0,T_1)}{T_2 - T_1}
$$

---

## Instantaneous Forward Rate

### Definition

The **instantaneous forward rate** $f(t,T)$ is obtained by taking the limit as the accrual period shrinks to zero:

$$
f(t,T) := \lim_{\Delta \to 0} f_c(t; T, T+\Delta) = -\frac{\partial}{\partial T} \log P(t,T)
$$

This fundamental relationship can be inverted:

$$
P(t,T) = \exp\left(-\int_t^T f(t,u) \, du\right)
$$

### Relationship to Zero Rates

The zero rate is the average of instantaneous forward rates:

$$
z(t,T) = \frac{1}{T-t} \int_t^T f(t,u) \, du
$$

Equivalently, differentiating:

$$
f(t,T) = z(t,T) + (T-t) \frac{\partial z(t,T)}{\partial T}
$$

This shows that:
- If the yield curve is flat ($z$ constant), then $f(t,T) = z$
- If the yield curve is upward sloping ($\partial z/\partial T > 0$), then $f(t,T) > z(t,T)$
- If the yield curve is downward sloping, then $f(t,T) < z(t,T)$

### The Short Rate

The instantaneous short rate is the limit:

$$
r_t = f(t,t) = \lim_{T \to t^+} f(t,T)
$$

This is the rate for infinitesimally short borrowing at time $t$.

---

## Forward Rate Agreement (FRA)

A **Forward Rate Agreement** is a contract to exchange:
- A fixed rate $K$ payment
- A floating rate (typically LIBOR) payment

at a future settlement date, based on a notional principal.

### FRA Payoff

At settlement time $T_1$, the FRA payoff (to the receiver of floating) is:

$$
\text{Payoff} = N \cdot (L(T_1; T_1, T_2) - K) \cdot (T_2 - T_1)
$$

discounted back to $T_1$, where $L(T_1; T_1, T_2)$ is the realized LIBOR rate.

### FRA Pricing

The fair fixed rate $K$ that makes the FRA have zero initial value is precisely the forward rate:

$$
K^* = F(0; T_1, T_2)
$$

The value of an existing FRA with rate $K$ is:

$$
V_{\text{FRA}}(0) = N \cdot (F(0; T_1, T_2) - K) \cdot (T_2 - T_1) \cdot P(0, T_2)
$$

---

## Term Structure Representations

A **term structure** can be equivalently represented by any of these curves:

| Representation | Notation | Contains |
|----------------|----------|----------|
| Discount curve | $T \mapsto P(0,T)$ | Prices of zero-coupon bonds |
| Zero curve | $T \mapsto z(0,T)$ | Spot rates for each maturity |
| Forward curve | $T \mapsto f(0,T)$ | Instantaneous forward rates |

All three contain equivalent information (given sufficient smoothness) but serve different purposes:

- **Discount curve:** Direct use in present value calculations
- **Zero curve:** Comparison across maturities, yield analysis
- **Forward curve:** Rate expectations, model inputs (HJM)

### Conversion Formulas Summary

| From | To | Formula |
|------|-----|---------|
| $P(0,T)$ | $z(0,T)$ | $z = -\frac{1}{T}\log P$ |
| $P(0,T)$ | $f(0,T)$ | $f = -\frac{\partial}{\partial T}\log P$ |
| $z(0,T)$ | $P(0,T)$ | $P = e^{-zT}$ |
| $z(0,T)$ | $f(0,T)$ | $f = z + T\frac{\partial z}{\partial T}$ |
| $f(0,T)$ | $P(0,T)$ | $P = e^{-\int_0^T f(u)du}$ |
| $f(0,T)$ | $z(0,T)$ | $z = \frac{1}{T}\int_0^T f(u)du$ |

---

## Forward Rates and Expectations

### The Expectations Hypothesis

Under the **pure expectations hypothesis**, forward rates equal expected future spot rates:

$$
F(0; T_1, T_2) = \mathbb{E}[z(T_1, T_2)]
$$

However, this hypothesis is empirically rejected. The observed relationship is:

$$
F(0; T_1, T_2) = \mathbb{E}^{\mathbb{P}}[z(T_1, T_2)] + \text{term premium}
$$

### Risk-Neutral Expectations

Under the risk-neutral measure $\mathbb{Q}$, forward rates **do** equal expected future rates:

$$
F(0; T_1, T_2) = \mathbb{E}^{\mathbb{Q}}[L(T_1; T_1, T_2)]
$$

This is the foundation of forward measure pricing (Section 10.5).

---

## Practical Notes on Forward Rate Curves

### Sensitivity to Interpolation

Forward rates are derivatives of the discount curve, making them sensitive to interpolation choices:

- Linear interpolation on zero rates produces discontinuous forwards
- Cubic spline interpolation can produce oscillating forwards
- Monotone convex methods balance smoothness and stability

### Forward Rate Volatility

Instantaneous forward rates inherit volatility from the term structure:
- Short-end forwards are more volatile
- Long-end forwards are more stable
- This affects HJM model specification

### Negative Forward Rates

Forward rates can be negative when:
- The yield curve is sufficiently inverted
- Market rates are near or below zero

This does not indicate arbitrage but requires care in lognormal models.

---

## Key Takeaways

- Forward rates are implied by ratios of discount factors via no-arbitrage
- The instantaneous forward rate satisfies $f(t,T) = -\partial_T \log P(t,T)$
- Zero rates are averages of forward rates; forwards are marginal rates
- FRA pricing directly uses forward rates
- Term structure representations (discount, zero, forward) are mathematically equivalent
- Forward rates are sensitive to curve construction choices

---

## Further Reading

- Brigo & Mercurio, *Interest Rate Models—Theory and Practice*, Chapter 1
- Filipović, *Term-Structure Models: A Graduate Course*
- Hull, *Options, Futures, and Other Derivatives*, Chapters 4 and 6
