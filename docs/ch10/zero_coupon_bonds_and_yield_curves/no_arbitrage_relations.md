# No-Arbitrage Relations

No-arbitrage principles link discount factors, zero rates, and forward rates. These relations are the foundation of curve construction and fixed-income pricing, ensuring internal consistency of the term structure.

---

## The Fundamental No-Arbitrage Principle

An **arbitrage opportunity** is a trading strategy that:
1. Requires no initial investment
2. Has no possibility of loss
3. Has positive probability of profit

In well-functioning markets, arbitrage opportunities cannot persist. This principle imposes strong constraints on the relationships between financial instruments.

---

## Replication Argument for Forward Rates

### Setup

Consider two strategies for obtaining 1 unit of currency at time $T_2$:

**Strategy A (Direct):**
- At time 0: Buy a $T_2$ zero-coupon bond
- Cost: $P(0, T_2)$
- Payoff at $T_2$: 1

**Strategy B (Synthetic):**
- At time 0: Buy $1/P(T_1, T_2)$ units of a $T_1$ zero-coupon bond
- This costs: $P(0, T_1) / P(T_1, T_2)$
- At time $T_1$: Receive $1/P(T_1, T_2)$ and invest at the prevailing rate

### The Problem with Strategy B

Strategy B involves reinvestment at an **unknown future rate**. To eliminate this uncertainty, we use a **forward contract**:

- At time 0: Enter a forward agreement to lend at rate $F(0; T_1, T_2)$ from $T_1$ to $T_2$
- At time 0: Buy a $T_1$ zero-coupon bond for $P(0, T_1)$
- At $T_1$: Receive 1, lend at the locked-in forward rate
- At $T_2$: Receive $1 + F(0; T_1, T_2)(T_2 - T_1)$

### No-Arbitrage Condition

For no arbitrage, both strategies must cost the same:

$$
P(0, T_2) \cdot [1 + F(0; T_1, T_2)(T_2 - T_1)] = P(0, T_1)
$$

Rearranging:

$$
\frac{P(0, T_1)}{P(0, T_2)} = 1 + F(0; T_1, T_2)(T_2 - T_1)
$$

This is precisely the forward rate definition, showing it arises from no-arbitrage.

---

## Discount Factor Constraints

### Monotonicity

Under absence of arbitrage with non-negative rates:

$$
T_1 < T_2 \implies P(0, T_1) \geq P(0, T_2)
$$

**Proof:** If $P(0, T_1) < P(0, T_2)$:
- Buy the $T_1$ bond (cost $P(0, T_1)$)
- Sell the $T_2$ bond (receive $P(0, T_2)$)
- Net cash: $P(0, T_2) - P(0, T_1) > 0$
- At $T_1$: Receive 1, invest risk-free to $T_2$
- At $T_2$: Have $\geq 1$, pay 1 on short position
- This is arbitrage

### Positivity

Discount factors must be strictly positive:

$$
P(0, T) > 0 \quad \text{for all } T
$$

A non-positive discount factor would imply:
- Receiving money today for a future obligation (if $P < 0$)
- Getting a free bond (if $P = 0$)

Both are arbitrage.

### Convexity (Jensen's Inequality Effect)

For stochastic rates, discount factors exhibit convexity:

$$
P(0, T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s ds}\right] \geq e^{-\mathbb{E}^{\mathbb{Q}}\left[\int_0^T r_s ds\right]}
$$

by Jensen's inequality (since $e^{-x}$ is convex).

---

## No-Arbitrage in Continuous Time

### Instantaneous Forward Rates

The continuous-time analog of the replication argument yields:

$$
P(0, T) = P(0, t) \cdot e^{-\int_t^T f(0,u) du}
$$

for any $0 \leq t \leq T$. Differentiating:

$$
f(0, T) = -\frac{\partial}{\partial T} \log P(0, T)
$$

### Chain Rule for Discount Factors

For any partition $0 = T_0 < T_1 < \cdots < T_n = T$:

$$
P(0, T) = \prod_{i=1}^{n} \frac{P(0, T_i)}{P(0, T_{i-1})} \cdot P(0, T_0)
= \prod_{i=1}^{n} \frac{P(0, T_i)}{P(0, T_{i-1})}
$$

This **multiplicative decomposition** underlies bootstrapping algorithms.

---

## Coupon Bond Pricing

### Linearity of Pricing

A coupon bond with cashflows $c_i$ at times $T_i$ (for $i = 1, \ldots, n$) has price:

$$
B_0 = \sum_{i=1}^n c_i \cdot P(0, T_i)
$$

This is a direct consequence of:
1. **Value additivity:** Portfolio value = sum of component values
2. **No arbitrage:** Each cashflow is discounted at its appropriate rate

### Par Yield

The **par yield** $y_n$ for maturity $T_n$ is the coupon rate that makes a bond trade at par:

$$
1 = \sum_{i=1}^n y_n \cdot \delta_i \cdot P(0, T_i) + P(0, T_n)
$$

where $\delta_i = T_i - T_{i-1}$ is the accrual fraction.

Solving:

$$
y_n = \frac{1 - P(0, T_n)}{\sum_{i=1}^n \delta_i \cdot P(0, T_i)}
$$

Par yields are observable in swap markets.

---

## Static Arbitrage Conditions

### Calendar Spread Arbitrage

A curve violates no-arbitrage if:

$$
\frac{P(0, T_1)}{P(0, T_2)} < 1 \quad \text{for some } T_1 < T_2
$$

This would imply a negative forward rate:

$$
F(0; T_1, T_2) = \frac{1}{T_2 - T_1}\left(\frac{P(0, T_1)}{P(0, T_2)} - 1\right) < 0
$$

While negative forwards can occur (with negative rates), **implied negative rates must be consistent with market reality**.

### Butterfly Arbitrage

For three maturities $T_1 < T_2 < T_3$, convexity requires:

$$
P(0, T_2) \leq \lambda P(0, T_1) + (1-\lambda) P(0, T_3)
$$

where $\lambda = (T_3 - T_2)/(T_3 - T_1)$.

Violation implies arbitrage via a butterfly trade:
- Long $\lambda$ units of $T_1$ bond
- Long $(1-\lambda)$ units of $T_3$ bond  
- Short 1 unit of $T_2$ bond

---

## Forward-Starting Instruments

### Forward Bond

A **forward contract** to buy a $T_2$-bond at time $T_1$ has forward price:

$$
F_B(0; T_1, T_2) = \frac{P(0, T_2)}{P(0, T_1)}
$$

This is the ratio of discount factors, reflecting no-arbitrage.

### Forward Swap

A **forward-starting swap** beginning at $T_0$ with payments at $T_1, \ldots, T_n$ has forward swap rate:

$$
S(0; T_0, T_n) = \frac{P(0, T_0) - P(0, T_n)}{\sum_{i=1}^n \delta_i P(0, T_i)}
$$

This rate makes the swap have zero initial value.

---

## Arbitrage Checks for Curve Construction

When constructing a yield curve, verify:

| Check | Condition | Failure Interpretation |
|-------|-----------|------------------------|
| Positivity | $P(0,T) > 0$ | Impossible prices |
| Monotonicity | $P(0,T_1) \geq P(0,T_2)$ for $T_1 < T_2$ | Calendar arbitrage |
| Smoothness | No extreme oscillations in $f(0,T)$ | Numerical instability |
| Instrument fit | Reprices input instruments | Calibration error |

---

## Practical Implications

### For Traders
- Arbitrage conditions define **fair value bounds**
- Violations signal **relative value opportunities** or **data errors**
- Forward rates should be **economically sensible**

### For Quants
- Curve construction must **respect no-arbitrage**
- Interpolation schemes should **preserve monotonicity**
- Model calibration should **exactly match liquid instruments**

### For Risk Managers
- Arbitrage-free curves ensure **consistent risk measures**
- Violations in stress scenarios may indicate **model breakdown**
- Forward rates provide **sensitivity benchmarks**

---

## Key Takeaways

- No-arbitrage links forwards and discount factors via replication
- Discount factors must be positive and (typically) decreasing
- Coupon bond pricing follows from linearity and no-arbitrage
- Calendar and butterfly arbitrage conditions constrain curve shapes
- Curve construction must respect these constraints for consistency

---

## Further Reading

- Björk, *Arbitrage Theory in Continuous Time*, Chapter 22
- Brigo & Mercurio, *Interest Rate Models—Theory and Practice*, Chapters 1-2
- Rebonato, *Modern Pricing of Interest-Rate Derivatives*, Chapter 2
