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

??? success "Solution to Exercise 1"
    Given $P(0, 3) = 0.915$ with $T = 3$ years.

    **Continuously compounded zero rate:**

    $$
    R_c(0, 3) = -\frac{\ln P(0, 3)}{T} = -\frac{\ln 0.915}{3} = -\frac{-0.08879}{3} \approx 0.02960 = 2.960\%
    $$

    **Semi-annually compounded rate:** Using $P(0, T) = \left(1 + R_{sa}/2\right)^{-2T}$, solve for $R_{sa}$:

    $$
    R_{sa} = 2\left(P(0, 3)^{-1/(2 \times 3)} - 1\right) = 2\left(0.915^{-1/6} - 1\right)
    $$

    Computing $0.915^{-1/6} = e^{-\frac{1}{6}\ln 0.915} = e^{0.01480} \approx 1.01491$:

    $$
    R_{sa} = 2 \times 0.01491 = 0.02982 = 2.982\%
    $$

    **Simply compounded rate:** Using $P(0, T) = 1/(1 + R_s \cdot T)$:

    $$
    R_s = \frac{1 - P(0, 3)}{P(0, 3) \cdot T} = \frac{1 - 0.915}{0.915 \times 3} = \frac{0.085}{2.745} \approx 0.03096 = 3.096\%
    $$

    **Verification:**

    - Continuous: $e^{-0.02960 \times 3} = e^{-0.08879} \approx 0.915$
    - Semi-annual: $(1 + 0.02982/2)^{-6} = (1.01491)^{-6} \approx 0.915$
    - Simple: $1/(1 + 0.03096 \times 3) = 1/1.09288 \approx 0.915$

    All three conventions reproduce the original discount factor, as expected. The simple rate is highest because interest is computed on the original principal only, while continuous compounding yields the lowest stated rate due to the most frequent compounding.

---

**Exercise 2.** Prove that in a positive-rate environment, $P(t, T)$ is strictly decreasing in $T$. What does a discount factor $P(0, T) > 1$ imply about the interest rate over $[0, T]$?

??? success "Solution to Exercise 2"
    **Claim:** If $z(t, T) > 0$ for all $T > t$ (positive-rate environment), then $P(t, T)$ is strictly decreasing in $T$.

    **Proof.** Since $P(t, T) = e^{-z(t, T)(T - t)}$ and $z(t, T) > 0$ for $T > t$, the exponent $-z(t, T)(T - t)$ is strictly negative and its magnitude grows with $T$ (assuming the zero rate does not decrease fast enough to offset the increasing time horizon).

    More precisely, consider $T_1 < T_2$. The no-arbitrage forward rate over $[T_1, T_2]$ is:

    $$
    f_c(t; T_1, T_2) = \frac{z(t, T_2)(T_2 - t) - z(t, T_1)(T_1 - t)}{T_2 - T_1}
    $$

    In a positive-rate environment, we require $f_c(t; T_1, T_2) \geq 0$, meaning $z(t, T_2)(T_2 - t) \geq z(t, T_1)(T_1 - t)$, which implies:

    $$
    P(t, T_2) = e^{-z(t, T_2)(T_2 - t)} \leq e^{-z(t, T_1)(T_1 - t)} = P(t, T_1)
    $$

    with strict inequality when the forward rate is strictly positive.

    Alternatively, from a no-arbitrage perspective: if $P(t, T_1) < P(t, T_2)$ for some $T_1 < T_2$, one could buy the cheaper $T_1$-bond and sell the $T_2$-bond, pocketing $P(t, T_2) - P(t, T_1) > 0$ at inception. At $T_1$, receive 1 and invest it risk-free. At $T_2$, the invested amount is at least 1 (positive rates), which covers the obligation on the short $T_2$-bond. The initial cash is pure profit — an arbitrage.

    **Interpretation of $P(0, T) > 1$:** Since $P(0, T) = e^{-z(0, T) \cdot T}$, having $P(0, T) > 1$ requires $z(0, T) < 0$, meaning the interest rate over $[0, T]$ is negative. Economically, this means an investor pays a premium today (more than \$1) to receive exactly \$1 at time $T$. This occurs in practice when central banks set negative policy rates and investors accept a guaranteed small loss for the safety and liquidity of government bonds.

---

**Exercise 3.** The discount factor curve is given at maturities $T = 1, 2, 3, 4, 5$ as $P = (0.97, 0.93, 0.89, 0.85, 0.80)$. Compute the zero rate curve $R(0, T)$ for each maturity. Is the zero rate curve upward-sloping, flat, or inverted?

??? success "Solution to Exercise 3"
    The continuously compounded zero rate is $R(0, T) = -\frac{\ln P(0, T)}{T}$.

    | $T$ | $P(0, T)$ | $\ln P(0, T)$ | $R(0, T)$ |
    |-----|-----------|---------------|-----------|
    | 1 | 0.97 | $-0.03046$ | $3.046\%$ |
    | 2 | 0.93 | $-0.07257$ | $3.629\%$ |
    | 3 | 0.89 | $-0.11653$ | $3.884\%$ |
    | 4 | 0.85 | $-0.16252$ | $4.063\%$ |
    | 5 | 0.80 | $-0.22314$ | $4.463\%$ |

    The zero rate increases monotonically from 3.046% to 4.463%, so the curve is **upward-sloping** (normal). This is the most commonly observed shape historically and is consistent with positive term premia — investors demand higher compensation for locking in funds over longer horizons.

---

**Exercise 4.** Show that the relationship between continuous and discrete compounding rates is $R_c = m\ln(1 + R_m/m)$. For $R_m = 5\%$ with quarterly compounding ($m = 4$), compute $R_c$.

??? success "Solution to Exercise 4"
    Let $R_m$ denote the rate compounded $m$ times per year, and $R_c$ the continuously compounded rate. Both must produce the same growth over one year:

    $$
    e^{R_c} = \left(1 + \frac{R_m}{m}\right)^m
    $$

    Taking the natural logarithm of both sides:

    $$
    R_c = m \ln\left(1 + \frac{R_m}{m}\right)
    $$

    This is the desired identity.

    For $R_m = 5\% = 0.05$ with quarterly compounding ($m = 4$):

    $$
    R_c = 4 \ln\left(1 + \frac{0.05}{4}\right) = 4 \ln(1.0125) = 4 \times 0.012422 = 0.049690
    $$

    So $R_c \approx 4.969\%$.

    The continuously compounded rate is slightly lower than the quarterly rate because continuous compounding compounds more frequently — achieving the same effective growth requires a lower stated rate. This is consistent with the general ordering: for the same effective annual rate, $R_c < R_m$ for any finite $m$.

---

**Exercise 5.** A central bank sets a negative policy rate of $-0.5\%$. Compute the discount factor $P(0, 1)$ under continuous compounding with $R = -0.005$. Verify that $P > 1$ and explain the economic meaning: you pay more today to receive \$1 in one year.

??? success "Solution to Exercise 5"
    With $R = -0.005$ (continuously compounded), the discount factor is:

    $$
    P(0, 1) = e^{-R \cdot T} = e^{-(-0.005) \times 1} = e^{0.005} \approx 1.00501
    $$

    Since $P(0, 1) > 1$, this means that the price today of a zero-coupon bond paying \$1 in one year is \$1.005 — strictly greater than its face value.

    **Economic meaning:** In a negative rate environment, the holder of cash faces a cost of carry (e.g., charges on bank reserves or storage costs for safe assets). An investor willingly pays \$1.005 today to receive \$1.00 in one year because:

    - Holding cash in a bank account with a $-0.5\%$ rate would also erode the principal.
    - The bond provides a guaranteed return of the notional, which may be preferable to alternatives with greater uncertainty.
    - Institutional mandates (e.g., regulatory requirements to hold sovereign bonds) create demand even at negative yields.

    This phenomenon was observed extensively in European and Japanese government bond markets from 2014 onward, where trillions of dollars of debt traded at negative yields.

---

**Exercise 6.** Given discount factors at semi-annual intervals $P(0, 0.5) = 0.988$, $P(0, 1.0) = 0.975$, $P(0, 1.5) = 0.960$, $P(0, 2.0) = 0.944$, compute the present value of a cash flow stream paying \$50 at $T = 0.5, 1.0, 1.5$ and \$1050 at $T = 2.0$.

??? success "Solution to Exercise 6"
    The present value of a stream of cashflows $c_i$ at times $T_i$ is:

    $$
    PV = \sum_{i} c_i \cdot P(0, T_i)
    $$

    Substituting the given values:

    $$
    PV = 50 \times P(0, 0.5) + 50 \times P(0, 1.0) + 50 \times P(0, 1.5) + 1050 \times P(0, 2.0)
    $$

    $$
    PV = 50 \times 0.988 + 50 \times 0.975 + 50 \times 0.960 + 1050 \times 0.944
    $$

    Computing each term:

    $$
    PV = 49.40 + 48.75 + 48.00 + 991.20 = 1{,}137.35
    $$

    This represents a bond with face value \$1,000, paying a semi-annual coupon of \$50 (i.e., 10% annual coupon rate, paid semi-annually as 5% of face). The bond trades at a **premium** (\$1,137.35 > \$1,000) because the coupon rate (10%) significantly exceeds the prevailing zero rates (approximately 2.4-2.9% annualized from the discount factors), making the bond's cashflows more valuable than par.
