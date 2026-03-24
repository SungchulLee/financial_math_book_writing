# Discount Factors and Zero Rates

Yield curves summarize the time value of money and are foundational for pricing fixed-income instruments and for discounting cashflows in derivatives. This section introduces **discount factors** and **zero (spot) rates**, along with key conventions and their mathematical relationships.

---

## Discount Factors

A **discount factor** $P(0,T)$ is the time-0 price of a zero-coupon bond paying 1 unit of currency at maturity $T$:

$$
P(0,T) = \text{Price at }0\text{ of a claim paying }1\text{ at }T
$$

More generally, for any valuation time $t \leq T$:

$$
P(t,T) = \text{Price at }t\text{ of a claim paying }1\text{ at }T
$$

### Fundamental Properties

In standard, positive-rate environments, discount factors satisfy:

1. **Normalization:** $P(t,t) = 1$ for all $t$
2. **Monotonicity:** $P(t,T_1) \geq P(t,T_2)$ whenever $T_1 \leq T_2$
3. **Positivity:** $0 < P(t,T) \leq 1$
4. **Continuity:** $T \mapsto P(t,T)$ is continuous (and typically smooth)

In modern markets with negative rates, discount factors remain positive but may exceed 1 for short maturities.

### Economic Interpretation

The discount factor $P(0,T)$ answers the question: "How much would a rational investor pay today for a guaranteed payment of 1 unit at time $T$?"

This value reflects:
- Time preference (preferring consumption today over future)
- Opportunity cost (alternative investment returns)
- Inflation expectations (erosion of purchasing power)

---

## Zero (Spot) Rates

### Continuously Compounded Zero Rate

The **continuously compounded zero rate** $z(t,T)$ is defined implicitly by:

$$
P(t,T) = e^{-z(t,T)(T-t)}
$$

Solving for the zero rate:

$$
z(t,T) = -\frac{\log P(t,T)}{T-t}
$$

For the initial curve at $t=0$:

$$
z(0,T) = -\frac{\log P(0,T)}{T}
$$

The zero rate $z(0,T)$ represents the constant continuously compounded rate that, if applied over $[0,T]$, produces the observed discount factor.

### Alternative Compounding Conventions

Different markets use different compounding conventions:

**Simple (Money Market) Compounding:**

$$
P(0,T) = \frac{1}{1 + R_s(0,T) \cdot T}
$$

Inverting:

$$
R_s(0,T) = \frac{1 - P(0,T)}{P(0,T) \cdot T}
$$

This convention is standard for maturities under one year.

**Annual Compounding:**

$$
P(0,T) = \frac{1}{(1 + R_a(0,T))^T}
$$

Inverting:

$$
R_a(0,T) = P(0,T)^{-1/T} - 1
$$

**Semi-Annual Compounding:**

$$
P(0,T) = \frac{1}{\left(1 + \frac{R_{sa}(0,T)}{2}\right)^{2T}}
$$

This is the standard convention for US Treasury bonds.

### Conversion Between Conventions

Given a continuously compounded rate $z$, equivalent rates under other conventions are:

| Convention | Formula |
|------------|---------|
| Simple (for period $\tau$) | $R_s = (e^{z\tau} - 1)/\tau$ |
| Annual | $R_a = e^z - 1$ |
| Semi-annual | $R_{sa} = 2(e^{z/2} - 1)$ |
| $m$-times per year | $R_m = m(e^{z/m} - 1)$ |

---

## The Term Structure of Interest Rates

The mapping $T \mapsto z(0,T)$ (or equivalently $T \mapsto P(0,T)$) is called the **term structure of interest rates** or simply the **yield curve**.

### Typical Yield Curve Shapes

Empirically observed yield curve shapes include:

1. **Normal (Upward Sloping):** $z(0,T_1) < z(0,T_2)$ for $T_1 < T_2$
   - Most common shape historically
   - Reflects term premium and expected rate increases

2. **Inverted (Downward Sloping):** $z(0,T_1) > z(0,T_2)$ for $T_1 < T_2$
   - Often precedes recessions
   - Reflects expected rate cuts

3. **Flat:** $z(0,T) \approx \text{constant}$
   - Transitional state
   - Ambiguous economic signal

4. **Humped:** Non-monotonic with interior maximum
   - Reflects complex rate expectations
   - Common in certain market conditions

---

## Interpretation and Uses

Zero rates and discount factors serve as building blocks for:

1. **Discounting deterministic cashflows:** A cashflow $c$ at time $T$ has present value $c \cdot P(0,T)$

2. **Pricing coupon bonds:** A bond paying coupons $c_i$ at times $T_i$ and principal $F$ at $T_n$:

$$
B_0 = \sum_{i=1}^n c_i P(0,T_i) + F \cdot P(0,T_n)
$$

3. **Building forward rates:** Forward rates are derived from ratios of discount factors (next section)

4. **Model calibration:** Initial yield curves are inputs to term structure models

---

## Short Rate Connection

Under the risk-neutral measure $\mathbb{Q}$, if $r_t$ denotes the instantaneous short rate, then:

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s \, ds} \,\bigg|\, \mathcal{F}_t\right]
$$

This fundamental relationship:
- Links observable bond prices to the stochastic short rate
- Forms the basis of short-rate modeling (Section 10.2)
- Reduces to $P(0,T) = e^{-\int_0^T r(s)ds}$ when rates are deterministic

---

## Day Count Conventions

Practical rate calculations require specifying how time intervals are measured:

| Convention | Description | Typical Use |
|------------|-------------|-------------|
| ACT/360 | Actual days / 360 | Money markets, LIBOR |
| ACT/365 | Actual days / 365 | UK markets |
| ACT/ACT | Actual / actual days in period | Government bonds |
| 30/360 | Assume 30-day months | Corporate bonds, swaps |

For a period from date $d_1$ to $d_2$:

$$
\tau = \frac{\text{Day count}(d_1, d_2)}{\text{Year basis}}
$$

Consistency in day count conventions is essential when comparing rates or building curves.

---

## Key Takeaways

- Discount factors $P(0,T)$ are the fundamental primitives of the yield curve
- Zero rates are logarithmic transforms: $z(0,T) = -\frac{1}{T}\log P(0,T)$
- Multiple compounding conventions exist; conversion formulas are routine but must be applied carefully
- The term structure shape carries economic information about rate expectations
- Day count conventions matter for practical calculations

---

## Further Reading

- Brigo & Mercurio, *Interest Rate Models—Theory and Practice*
- Hull, *Options, Futures, and Other Derivatives* (yield curve basics)
- Filipović, *Term-Structure Models: A Graduate Course*

---

## Exercises

**Exercise 1.** Given a discount factor $P(0, 3) = 0.915$, compute the continuously compounded zero rate $R(0,3)$, the semi-annually compounded rate, and the simply compounded rate over 3 years. Verify all three produce the same discount factor.

---

**Exercise 2.** Prove that in a positive-rate environment, $P(t, T)$ is strictly decreasing in $T$. What does a discount factor $P(0, T) > 1$ imply about the interest rate over $[0, T]$?

---

**Exercise 3.** The discount factor curve is given at maturities $T = 1, 2, 3, 4, 5$ as $P = (0.97, 0.93, 0.89, 0.85, 0.80)$. Compute the zero rate curve $R(0, T)$ for each maturity. Is the zero rate curve upward-sloping, flat, or inverted?

---

**Exercise 4.** Show that the relationship between continuous and discrete compounding rates is $R_c = m\ln(1 + R_m/m)$. For $R_m = 5\%$ with quarterly compounding ($m = 4$), compute $R_c$.

---

**Exercise 5.** A central bank sets a negative policy rate of $-0.5\%$. Compute the discount factor $P(0, 1)$ under continuous compounding with $R = -0.005$. Verify that $P > 1$ and explain the economic meaning: you pay more today to receive \$1 in one year.

---

**Exercise 6.** Given discount factors at semi-annual intervals $P(0, 0.5) = 0.988$, $P(0, 1.0) = 0.975$, $P(0, 1.5) = 0.960$, $P(0, 2.0) = 0.944$, compute the present value of a cash flow stream paying \$50 at $T = 0.5, 1.0, 1.5$ and \$1050 at $T = 2.0$.
