# Duration and Convexity

**Duration** and **convexity** are fundamental measures of interest rate sensitivity for fixed-income portfolios. They quantify how bond prices respond to yield changes, serving as the interest rate analogs of delta and gamma in equity options.

---

## Motivation

### The Problem

How does a bond price change when interest rates move?

For a zero-coupon bond:

$$
P = e^{-yT}
$$

Taking differentials:

$$
dP = -T e^{-yT} dy = -T \cdot P \cdot dy
$$

So:

$$
\frac{dP}{P} = -T \cdot dy
$$

The **time to maturity** $T$ measures sensitivity. For coupon bonds, this generalizes to **duration**.

---

## Macaulay Duration

### Definition

**Macaulay duration** is the weighted average time to receive cashflows:

$$
D_{\text{Mac}} = \frac{\sum_{i=1}^{n} t_i \cdot PV(c_i)}{\sum_{i=1}^{n} PV(c_i)} = \frac{\sum_{i=1}^{n} t_i \cdot c_i \cdot e^{-y t_i}}{P}
$$

where:
- $c_i$: cashflow at time $t_i$
- $y$: continuously compounded yield
- $P$: bond price

### Interpretation

Macaulay duration answers: "What is the effective maturity of this bond, accounting for all cashflows?"

For a zero-coupon bond: $D_{\text{Mac}} = T$ (maturity)

For a coupon bond: $D_{\text{Mac}} < T$ (earlier cashflows reduce effective maturity)

### Example

A 3-year bond with 5% annual coupons, par value 100, priced at par (y = 5%):

| Year | Cashflow | PV | Weight | Contribution |
|------|----------|-----|--------|--------------|
| 1 | 5 | 4.76 | 4.76% | 0.0476 |
| 2 | 5 | 4.54 | 4.54% | 0.0907 |
| 3 | 105 | 90.70 | 90.70% | 2.7211 |
| **Total** | | **100** | | **2.86 years** |

---

## Modified Duration

### Definition

**Modified duration** directly measures price sensitivity:

$$
D_{\text{mod}} = -\frac{1}{P} \frac{dP}{dy}
$$

For continuously compounded yields:

$$
D_{\text{mod}} = D_{\text{Mac}}
$$

For annually compounded yields ($y_a$):

$$
D_{\text{mod}} = \frac{D_{\text{Mac}}}{1 + y_a}
$$

### Price Sensitivity Formula

$$
\boxed{\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y}
$$

This linear approximation works well for small yield changes.

### Example

If $D_{\text{mod}} = 5$ and yields increase by 50 bps (0.5%):

$$
\frac{\Delta P}{P} \approx -5 \times 0.005 = -2.5\%
$$

A \$1M bond portfolio loses approximately \$25,000.

---

## Dollar Duration (DV01)

### Definition

**Dollar duration** (or **DV01**, **PV01**) is the absolute price change per 1 basis point yield change:

$$
\text{DV01} = -\frac{dP}{dy} \times 0.0001 = D_{\text{mod}} \times P \times 0.0001
$$

### Interpretation

DV01 answers: "How many dollars do I gain/lose per basis point?"

### Example

A \$10M position with $D_{\text{mod}} = 7$:

$$
\text{DV01} = 7 \times 10,000,000 \times 0.0001 = \$7,000
$$

A 10 bp rate increase costs \$70,000.

---

## Convexity

### Motivation

Duration provides a linear approximation. For large yield changes, the **curvature** of the price-yield relationship matters.

### Definition

**Convexity** is the second derivative of price with respect to yield:

$$
C = \frac{1}{P} \frac{d^2 P}{dy^2}
$$

For a bond with cashflows $c_i$ at times $t_i$:

$$
C = \frac{\sum_{i=1}^{n} t_i^2 \cdot c_i \cdot e^{-y t_i}}{P}
$$

### Second-Order Approximation

Including convexity:

$$
\boxed{\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2}
$$

### Convexity Effect

Since $C > 0$ for standard bonds:
- When yields rise, price falls **less** than duration predicts
- When yields fall, price rises **more** than duration predicts

**Convexity is always beneficial** for long bond positions!

---

## Duration of a Portfolio

### Linearity

Portfolio duration is the weighted average of component durations:

$$
D_{\text{portfolio}} = \sum_i w_i D_i
$$

where $w_i = \frac{P_i}{\sum_j P_j}$ is the weight of bond $i$.

### Dollar Duration Additivity

Total DV01 is the sum of component DV01s:

$$
\text{DV01}_{\text{portfolio}} = \sum_i \text{DV01}_i
$$

---

## Key Rate Duration

### Motivation

Duration assumes **parallel shifts** in the yield curve. In reality, curves steepen, flatten, or twist.

### Definition

**Key rate duration** (KRD) measures sensitivity to a shift at a specific maturity:

$$
\text{KRD}_k = -\frac{1}{P} \frac{\partial P}{\partial y_k}
$$

where $y_k$ is the yield at key rate $k$.

### Example Key Rates

Typical key rates: 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y

### Decomposition

$$
\sum_{k} \text{KRD}_k = D_{\text{mod}}
$$

The sum of key rate durations equals modified duration (for parallel shift).

---

## Duration of Interest Rate Derivatives

### Zero-Coupon Bond

$$
D = T \quad \text{(maturity)}
$$

### Floating Rate Note

$$
D \approx \text{time to next reset}
$$

A floater reprices at par at each reset, so effective duration is short.

### Interest Rate Swap

**Payer swap** (pay fixed, receive floating):

$$
D_{\text{swap}} \approx D_{\text{fixed leg}} - D_{\text{floating leg}} \approx D_{\text{fixed leg}}
$$

The floating leg has near-zero duration.

### Caps and Floors

Duration depends on delta:

$$
D_{\text{cap}} = \Delta \times D_{\text{underlying}}
$$

For deep ITM caps, duration approaches that of a floater.

---

## Duration Hedging

### Immunization

To protect against parallel yield shifts:

$$
D_{\text{portfolio}} = D_{\text{target}}
$$

Setting $D_{\text{target}} = 0$ creates a **duration-neutral** position.

### Hedge Ratio

To hedge a position with duration $D_A$ using an instrument with duration $D_B$:

$$
\text{Hedge ratio} = -\frac{D_A \cdot P_A}{D_B \cdot P_B}
$$

### Example

Hedge a \$10M bond portfolio ($D = 6$) with 10-year Treasury futures ($D = 8$, price \$100K per contract):

$$
\text{Contracts} = -\frac{6 \times 10,000,000}{8 \times 100,000} = -75 \text{ contracts (short)}
$$

---

## Convexity Hedging

### Why Hedge Convexity?

Duration hedging leaves residual risk from large rate moves. Convexity mismatch creates P&L.

### Convexity Matching

For full immunization:

$$
D_{\text{portfolio}} = D_{\text{target}}
$$

$$
C_{\text{portfolio}} = C_{\text{target}}
$$

Requires at least two hedging instruments.

### Convexity Trading

- **Long convexity:** Profits from rate volatility (long options)
- **Short convexity:** Loses from rate volatility (short options)

Selling convexity (e.g., writing swaptions) generates premium but loses on large moves.

---

## Effective Duration for Non-Linear Instruments

### Definition

For instruments without analytical duration, use **numerical effective duration**:

$$
D_{\text{eff}} = -\frac{P(y + \Delta y) - P(y - \Delta y)}{2 \cdot P(y) \cdot \Delta y}
$$

### Effective Convexity

$$
C_{\text{eff}} = \frac{P(y + \Delta y) + P(y - \Delta y) - 2P(y)}{P(y) \cdot (\Delta y)^2}
$$

### Applications

Effective duration is essential for:
- Mortgage-backed securities (prepayment optionality)
- Callable bonds
- Structured products

---

## Duration and Bond Portfolio Management

### Tracking Error

The difference between portfolio and benchmark duration creates tracking error:

$$
\text{TE} \approx |D_{\text{portfolio}} - D_{\text{benchmark}}| \times \sigma_y
$$

### Duration Targeting

Active managers express views via duration:
- **Long duration:** Expect rates to fall
- **Short duration:** Expect rates to rise

### Barbell vs. Bullet

| Strategy | Structure | Duration | Convexity |
|----------|-----------|----------|-----------|
| Bullet | Concentrated at target maturity | $D$ | Lower |
| Barbell | Short and long ends | $D$ | Higher |

Same duration, different convexity profiles.

---

## Limitations of Duration

### Non-Parallel Shifts

Duration assumes parallel curve moves. Real curves:
- Steepen/flatten
- Butterfly (concave/convex)
- Twist

**Solution:** Key rate durations, principal component analysis

### Large Yield Changes

Linear approximation fails for large moves.

**Solution:** Include convexity, use full repricing

### Optionality

Callable bonds, MBS have negative convexity when rates fall.

**Solution:** Effective duration, option-adjusted duration

---

## Key Takeaways

- **Macaulay duration:** Weighted average time to cashflows
- **Modified duration:** $-\frac{1}{P}\frac{dP}{dy}$, measures price sensitivity
- **DV01:** Dollar change per basis point
- **Convexity:** Second derivative; positive for standard bonds
- **Price change:** $\frac{\Delta P}{P} \approx -D \cdot \Delta y + \frac{1}{2}C \cdot (\Delta y)^2$
- **Key rate duration:** Sensitivity to specific curve points
- **Duration hedging:** Match portfolio duration to target
- **Convexity:** Always beneficial for long positions

---

## Further Reading

- Fabozzi, *Fixed Income Analysis*, Chapters on Duration
- Tuckman & Serrat, *Fixed Income Securities*, Chapters 4-6
- Hull, *Options, Futures, and Other Derivatives*, Chapter 4

---

## Exercises

**Exercise 1.** A 5-year bond pays a 6\% annual coupon on a face value of \$100 and is priced to yield 5\% (continuously compounded). Compute the Macaulay duration, modified duration, and convexity. Using the second-order approximation, estimate the percentage price change for a 100 bp increase in yield. Compare with the exact repriced value.

??? success "Solution to Exercise 1"

    **Given:** 5-year bond, 6% annual coupon, face value \$100, continuously compounded yield $y = 5\%$.

    **Step 1: Bond price.**

    $$
    P = \sum_{i=1}^{5} c_i e^{-y t_i} = 6e^{-0.05} + 6e^{-0.10} + 6e^{-0.15} + 6e^{-0.20} + 106e^{-0.25}
    $$

    $$
    = 6(0.9512) + 6(0.9048) + 6(0.8607) + 6(0.8187) + 106(0.7788)
    $$

    $$
    = 5.7073 + 5.4290 + 5.1643 + 4.9123 + 82.5551 = 103.7680
    $$

    **Step 2: Macaulay duration.**

    $$
    D_{\text{Mac}} = \frac{\sum t_i \cdot c_i e^{-yt_i}}{P} = \frac{1(5.7073) + 2(5.4290) + 3(5.1643) + 4(4.9123) + 5(82.5551)}{103.7680}
    $$

    $$
    = \frac{5.7073 + 10.8580 + 15.4929 + 19.6491 + 412.7755}{103.7680} = \frac{464.4828}{103.7680} = 4.476 \text{ years}
    $$

    **Step 3: Modified duration.** For continuously compounded yields, $D_{\text{mod}} = D_{\text{Mac}} = 4.476$ years.

    **Step 4: Convexity.**

    $$
    C = \frac{\sum t_i^2 \cdot c_i e^{-yt_i}}{P} = \frac{1(5.7073) + 4(5.4290) + 9(5.1643) + 16(4.9123) + 25(82.5551)}{103.7680}
    $$

    $$
    = \frac{5.7073 + 21.7160 + 46.4787 + 78.5966 + 2063.8775}{103.7680} = \frac{2216.3761}{103.7680} = 21.36
    $$

    **Step 5: Price change for +100 bps ($\Delta y = 0.01$).**

    Second-order approximation:

    $$
    \frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \frac{1}{2}C \cdot (\Delta y)^2 = -4.476 \times 0.01 + \frac{1}{2}(21.36)(0.01)^2
    $$

    $$
    = -0.04476 + 0.001068 = -0.04369 = -4.369\%
    $$

    $$
    \Delta P \approx -4.369\% \times 103.768 = -\$4.533
    $$

    **Exact repriced value** at $y = 6\%$:

    $$
    P(6\%) = 6e^{-0.06} + 6e^{-0.12} + 6e^{-0.18} + 6e^{-0.24} + 106e^{-0.30}
    $$

    $$
    = 6(0.9418) + 6(0.8869) + 6(0.8353) + 6(0.7866) + 106(0.7408)
    $$

    $$
    = 5.6508 + 5.3215 + 5.0116 + 4.7198 + 78.5274 = 99.2311
    $$

    Exact change: $99.2311 - 103.768 = -4.537$, or $-4.372\%$.

    The second-order approximation ($-4.369\%$) is very close to the exact result ($-4.372\%$), with an error of only 0.003%.

---

**Exercise 2.** Prove that for a zero-coupon bond with maturity $T$ and continuously compounded yield $y$, the Macaulay duration equals $T$, the modified duration equals $T$, and the convexity equals $T^2$. Explain intuitively why a zero-coupon bond has the highest duration among all bonds with the same maturity.

??? success "Solution to Exercise 2"

    For a zero-coupon bond with maturity $T$: $P = e^{-yT}$. There is a single cashflow of 1 at time $T$.

    **Macaulay duration:**

    $$
    D_{\text{Mac}} = \frac{T \cdot 1 \cdot e^{-yT}}{e^{-yT}} = T
    $$

    **Modified duration** (continuously compounded):

    $$
    D_{\text{mod}} = -\frac{1}{P}\frac{dP}{dy} = -\frac{1}{e^{-yT}}(-T e^{-yT}) = T = D_{\text{Mac}}
    $$

    **Convexity:**

    $$
    C = \frac{1}{P}\frac{d^2P}{dy^2} = \frac{1}{e^{-yT}}(T^2 e^{-yT}) = T^2
    $$

    **Intuition for highest duration:** Consider a coupon bond and a zero-coupon bond with the same maturity $T$. The coupon bond pays intermediate cashflows at $t_1 < t_2 < \cdots < T$, so its weighted average time:

    $$
    D_{\text{Mac}}^{\text{coupon}} = \frac{\sum t_i \cdot PV(c_i)}{P} < T
    $$

    because the weights are positive and some cashflows arrive before $T$. The zero-coupon bond has all its weight at $T$, giving $D_{\text{Mac}} = T$.

    Therefore, among all bonds with maturity $T$ (and positive coupons), the zero-coupon bond has the **maximum duration** of $T$. Any coupon payment before maturity reduces the effective maturity by pulling the weighted average closer to the present. This means zero-coupon bonds are the most sensitive to yield changes among bonds of the same maturity.

---

**Exercise 3.** A portfolio consists of two bonds: Bond A with market value \$5M and modified duration 3.2, and Bond B with market value \$8M and modified duration 7.5. Compute the portfolio's modified duration and DV01. A trader wants to reduce the portfolio duration to 4.0 by selling Bond B and reinvesting in a money market fund (duration $\approx 0$). How much of Bond B must be sold?

??? success "Solution to Exercise 3"

    **Portfolio modified duration:**

    $$
    D_{\text{port}} = w_A D_A + w_B D_B = \frac{5}{13} \times 3.2 + \frac{8}{13} \times 7.5
    $$

    $$
    = 0.3846 \times 3.2 + 0.6154 \times 7.5 = 1.231 + 4.615 = 5.846
    $$

    **Portfolio DV01:**

    $$
    \text{DV01} = D_{\text{port}} \times P_{\text{total}} \times 0.0001 = 5.846 \times 13{,}000{,}000 \times 0.0001 = \$7{,}600
    $$

    (Equivalently: DV01$_A$ + DV01$_B$ = $3.2 \times 5M \times 0.0001 + 7.5 \times 8M \times 0.0001 = 1600 + 6000 = \$7{,}600$.)

    **To reduce portfolio duration to 4.0:**

    Let $x$ be the amount of Bond B sold (and reinvested in money market at duration 0). After selling $x$ of Bond B:

    - Bond A: \$5M, duration 3.2
    - Bond B: \$(8M $-$ $x$), duration 7.5
    - Money market: \$$x$, duration 0
    - Total: \$13M (unchanged)

    New portfolio duration:

    $$
    D_{\text{new}} = \frac{5M \times 3.2 + (8M - x) \times 7.5 + x \times 0}{13M} = 4.0
    $$

    $$
    16M + 60M - 7.5x = 52M
    $$

    $$
    76M - 7.5x = 52M
    $$

    $$
    7.5x = 24M \implies x = \$3.2M
    $$

    The trader must sell **\$3.2M** of Bond B and reinvest in the money market fund.

---

**Exercise 4.** Consider two portfolios with the same modified duration of 6 years: a "bullet" portfolio consisting of a single 6-year zero-coupon bond, and a "barbell" portfolio consisting of equal market-value positions in 2-year and 10-year zero-coupon bonds. Compute the convexity of each portfolio. Which portfolio benefits more from a large rate move, and why?

??? success "Solution to Exercise 4"

    **Bullet portfolio:** A single 6-year zero-coupon bond.

    $$
    D_{\text{bullet}} = 6, \qquad C_{\text{bullet}} = 6^2 = 36
    $$

    **Barbell portfolio:** Equal market-value positions (\$0.50 each per \$1 total) in 2-year and 10-year zero-coupon bonds.

    Duration:

    $$
    D_{\text{barbell}} = 0.5 \times 2 + 0.5 \times 10 = 6 \checkmark
    $$

    Convexity (since convexity is $T^2$ for zero-coupon bonds):

    $$
    C_{\text{barbell}} = 0.5 \times 2^2 + 0.5 \times 10^2 = 0.5 \times 4 + 0.5 \times 100 = 2 + 50 = 52
    $$

    **Comparison:** $C_{\text{barbell}} = 52 > 36 = C_{\text{bullet}}$.

    **Which benefits more from a large rate move?** The barbell portfolio benefits more. Using the second-order approximation:

    $$
    \frac{\Delta P}{P} \approx -D \cdot \Delta y + \frac{1}{2}C \cdot (\Delta y)^2
    $$

    Both portfolios have the same duration (first-order effect), so the difference in percentage price change is:

    $$
    \frac{\Delta P_{\text{barbell}}}{P_{\text{barbell}}} - \frac{\Delta P_{\text{bullet}}}{P_{\text{bullet}}} \approx \frac{1}{2}(C_{\text{barbell}} - C_{\text{bullet}})(\Delta y)^2 = \frac{1}{2}(52 - 36)(\Delta y)^2 = 8(\Delta y)^2
    $$

    This is always **positive** regardless of the direction of the rate move. For a 100 bp move: $8 \times (0.01)^2 = 0.0008 = 0.08\%$ advantage for the barbell.

    **Why:** The barbell has higher convexity because it spreads its cashflows across a wider range of maturities. The $T^2$ weighting in convexity means extreme maturities contribute disproportionately. The barbell gains more from rate decreases (the 10Y bond rallies sharply) and loses less from rate increases (the 2Y bond is less affected), compared to the bullet. Higher convexity is always beneficial for a long position, assuming no cost difference.

---

**Exercise 5.** A \$50M bond portfolio has modified duration 5.5 and convexity 42. Treasury bond futures have a modified duration of 6.8, priced at \$98,000 per contract. (a) How many futures contracts are needed to duration-hedge the portfolio? (b) If yields subsequently move by $-75$ bps, compute the portfolio P\&L using both the linear (duration-only) and quadratic (duration + convexity) approximations.

??? success "Solution to Exercise 5"

    **Given:** Portfolio: \$50M, $D = 5.5$, $C = 42$. Futures: $D_f = 6.8$, price \$98,000/contract.

    **(a) Number of futures contracts for duration hedge:**

    $$
    h = -\frac{D_{\text{port}} \times P_{\text{port}}}{D_f \times P_f} = -\frac{5.5 \times 50{,}000{,}000}{6.8 \times 98{,}000} = -\frac{275{,}000{,}000}{666{,}400} = -412.6
    $$

    Round to **$-413$ contracts** (short 413 futures).

    **(b) P&L for $\Delta y = -0.0075$ ($-75$ bps):**

    **Linear approximation (duration only):**

    $$
    \Delta P_{\text{port}} \approx -D \cdot P \cdot \Delta y = -5.5 \times 50{,}000{,}000 \times (-0.0075) = +\$2{,}062{,}500
    $$

    But the portfolio is hedged with short futures, whose P&L (from the portfolio holder's perspective) is:

    $$
    \Delta P_{\text{futures}} \approx -h \times D_f \times P_f \times \Delta y = -(-413) \times 6.8 \times 98{,}000 \times (-0.0075)
    $$

    $$
    = 413 \times 6.8 \times 98{,}000 \times (-0.0075) = -\$2{,}063{,}142
    $$

    Net P&L (linear): $\approx 2{,}062{,}500 - 2{,}063{,}142 \approx -\$642$ (approximately zero, as expected from a duration hedge).

    **Quadratic approximation (duration + convexity) for the portfolio alone (unhedged):**

    $$
    \Delta P_{\text{port}} \approx -D \cdot P \cdot \Delta y + \frac{1}{2}C \cdot P \cdot (\Delta y)^2
    $$

    $$
    = 2{,}062{,}500 + \frac{1}{2}(42)(50{,}000{,}000)(0.0075)^2
    $$

    $$
    = 2{,}062{,}500 + \frac{1}{2}(42)(50{,}000{,}000)(0.00005625)
    $$

    $$
    = 2{,}062{,}500 + 59{,}063 = \$2{,}121{,}563
    $$

    The convexity term adds \$59,063 of additional gain. Since rates fell, the convexity effect (always positive for long positions) increases the bond portfolio's gain beyond what duration alone predicts. If the futures have lower convexity, this creates a positive convexity P&L for the hedged portfolio.

---

**Exercise 6.** A callable bond has an effective duration of 3.2 at a yield of 5\%, computed via the numerical formula with $\Delta y = 25$ bps. If the bond price is \$102.50 at 5\%, \$103.80 at 4.75\%, and \$101.35 at 5.25\%, verify the effective duration calculation. Compute the effective convexity. Is the convexity positive or negative, and what does this imply about the callable bond's price behavior?

??? success "Solution to Exercise 6"

    **Given:** Callable bond price at $y = 5\%$: $P = 102.50$, at $y = 4.75\%$: $P^- = 103.80$, at $y = 5.25\%$: $P^+ = 101.35$, $\Delta y = 0.0025$.

    **Effective duration:**

    $$
    D_{\text{eff}} = -\frac{P^- - P^+}{2 P \cdot \Delta y} = -\frac{103.80 - 101.35}{2 \times 102.50 \times 0.0025}
    $$

    $$
    = -\frac{2.45}{0.5125} = -4.780
    $$

    Wait --- effective duration should be positive. The formula has a negative sign to convert the negative $dP/dy$ relationship into a positive number:

    $$
    D_{\text{eff}} = \frac{P^- - P^+}{2 P \cdot \Delta y} = \frac{103.80 - 101.35}{2 \times 102.50 \times 0.0025} = \frac{2.45}{0.5125} = 4.78
    $$

    This matches the stated effective duration of 3.2 only if we use the signed formula. Let me recheck: the problem says $D_{\text{eff}} = 3.2$. With the given prices, we get 4.78. The problem asks us to "verify" with $\Delta y = 25$ bps, and the answer is:

    $$
    D_{\text{eff}} = \frac{103.80 - 101.35}{2 \times 102.50 \times 0.0025} = \frac{2.45}{0.5125} = 4.78
    $$

    (The stated value of 3.2 may refer to a different $\Delta y$ or different prices; the numerical formula with the given data yields **4.78**.)

    **Effective convexity:**

    $$
    C_{\text{eff}} = \frac{P^+ + P^- - 2P}{P \cdot (\Delta y)^2} = \frac{101.35 + 103.80 - 2(102.50)}{102.50 \times (0.0025)^2}
    $$

    $$
    = \frac{205.15 - 205.00}{102.50 \times 0.00000625} = \frac{0.15}{0.000640625} = 234.1
    $$

    Wait, let me recheck: $P^+ + P^- = 101.35 + 103.80 = 205.15$ and $2P = 205.00$, so the numerator is $0.15 > 0$.

    $$
    C_{\text{eff}} = \frac{0.15}{102.50 \times 6.25 \times 10^{-6}} = \frac{0.15}{6.406 \times 10^{-4}} = 234.1
    $$

    The effective convexity is **positive** ($C_{\text{eff}} \approx 234$).

    However, for a callable bond near or below the call price, we would typically expect **negative convexity**. If the prices were instead such that the upward price move ($P^-$ for yield decrease) were limited by the call feature, we might see $P^- + P^+ < 2P$, giving negative convexity. With the given data, the convexity is positive, meaning the bond is not yet significantly affected by the call feature at this yield level (i.e., the call is out of the money).

    **Implications:** Positive convexity means the callable bond behaves similarly to a non-callable bond in this yield range --- it gains more from rate decreases than it loses from rate increases. If rates were to fall further toward the call level, the convexity would turn negative, and the price would be capped near the call price.

---

**Exercise 7.** The tracking error of a portfolio relative to a benchmark is approximately $|D_{\text{port}} - D_{\text{bench}}| \times \sigma_y$. If the benchmark has a duration of 6.0 years and annual yield volatility is 80 bps, what portfolio duration range keeps the annualized tracking error below 50 bps? Discuss why duration matching alone is insufficient for managing risk against a benchmark with a different convexity profile.

??? success "Solution to Exercise 7"

    **Given:** $D_{\text{bench}} = 6.0$, $\sigma_y = 80$ bps $= 0.0080$.

    **Tracking error constraint:**

    $$
    \text{TE} \approx |D_{\text{port}} - D_{\text{bench}}| \times \sigma_y < 0.0050
    $$

    $$
    |D_{\text{port}} - 6.0| \times 0.0080 < 0.0050
    $$

    $$
    |D_{\text{port}} - 6.0| < \frac{0.0050}{0.0080} = 0.625
    $$

    Therefore:

    $$
    5.375 < D_{\text{port}} < 6.625
    $$

    The portfolio duration must be within **[5.375, 6.625]** years to keep annualized tracking error below 50 bps.

    **Why duration matching alone is insufficient:**

    Duration matching neutralizes the portfolio's exposure to **parallel** yield shifts (the first principal component). However, if the portfolio and benchmark have different **convexity** profiles, residual risk arises from:

    1. **Large yield moves:** The second-order term $\frac{1}{2}(C_{\text{port}} - C_{\text{bench}})(\Delta y)^2$ creates tracking error even when durations match. If the portfolio is a barbell and the benchmark is a bullet (both with duration 6), the portfolio has higher convexity and outperforms in volatile markets but underperforms when rates are stable (due to the cost of carrying the convexity, e.g., lower yield).

    2. **Non-parallel curve moves:** Duration matching protects only against level shifts. If the portfolio and benchmark have different **key rate duration** profiles (e.g., the portfolio concentrates exposure at the 2Y and 30Y points while the benchmark concentrates at the 10Y point), a curve steepening or butterfly move creates tracking error that duration matching cannot prevent.

    3. **Convexity mismatch and options:** If the benchmark contains callable bonds (negative convexity) and the portfolio contains non-callable bonds (positive convexity), the two will respond very differently to rate moves even with matched durations.

    To properly manage tracking error, one should match both duration **and** convexity (or, better, match the full key rate duration profile), and consider higher-order risk measures when the portfolio contains optionality.
