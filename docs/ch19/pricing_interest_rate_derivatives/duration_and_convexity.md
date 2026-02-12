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

A $1M bond portfolio loses approximately $25,000.

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

A $10M position with $D_{\text{mod}} = 7$:

$$
\text{DV01} = 7 \times 10,000,000 \times 0.0001 = \$7,000
$$

A 10 bp rate increase costs $70,000.

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

Hedge a $10M bond portfolio ($D = 6$) with 10-year Treasury futures ($D = 8$, price $100K per contract):

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
