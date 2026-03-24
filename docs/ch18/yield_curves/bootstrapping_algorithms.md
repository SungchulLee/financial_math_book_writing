# Bootstrapping Algorithms

**Bootstrapping** is the standard method for constructing a discount curve from market quotes. The algorithm sequentially extracts discount factors from increasingly longer-maturity instruments, using previously determined values to solve for new ones.

---

### Overview of the Bootstrapping Process

#### The Problem

Market data comes in the form of:
- Deposit rates (short maturities)
- Futures prices (medium maturities)
- Swap rates (longer maturities)

Each instrument depends on multiple discount factors. Bootstrapping solves for discount factors **sequentially** from short to long maturities.

#### General Principle

Given:
1. A market quote for an instrument with maturity $T_n$
2. All discount factors $P(0, T_1), \ldots, P(0, T_{n-1})$ for shorter maturities

Solve for $P(0, T_n)$ such that the instrument is correctly priced.

---

### Stage 1: Money Market Deposits

#### Instrument Description

A **deposit** with maturity $T$ and rate $R_d$ pays:
- Invest 1 at time 0
- Receive $1 + R_d \cdot \delta$ at time $T$

where $\delta$ is the day count fraction (typically ACT/360).

#### Bootstrapping Formula

The deposit rate directly implies the discount factor:

$$
P(0, T) = \frac{1}{1 + R_d \cdot \delta}
$$

#### Example

| Maturity | Deposit Rate | Day Count | Discount Factor |
|----------|--------------|-----------|-----------------|
| 1M | 5.00% | 31/360 | 0.995719 |
| 2M | 5.10% | 62/360 | 0.991311 |
| 3M | 5.15% | 92/360 | 0.986932 |

---

### Stage 2: Futures (Eurodollar/SOFR Futures)

#### Instrument Description

A **3-month interest rate future** with price $F$ implies a forward rate:

$$
R_{\text{fut}} = \frac{100 - F}{100}
$$

for the period from the futures expiry $T_1$ to $T_2 = T_1 + 0.25$.

#### Convexity Adjustment

Futures rates differ from forward rates due to daily margining. The **convexity adjustment** is:

$$
F(0; T_1, T_2) \approx R_{\text{fut}} - \text{CA}(T_1)
$$

A common approximation:

$$
\text{CA}(T_1) \approx \frac{1}{2} \sigma^2 T_1 (T_2 - T_1)
$$

where $\sigma$ is the rate volatility (typically 0.5-1.5%).

#### Bootstrapping Formula

Given $P(0, T_1)$ from previous stage and forward rate $F(0; T_1, T_2)$:

$$
P(0, T_2) = \frac{P(0, T_1)}{1 + F(0; T_1, T_2) \cdot (T_2 - T_1)}
$$

#### Sequential Application

Futures strip provides a chain:

$$
P(0, T_1) \to P(0, T_2) \to P(0, T_3) \to \cdots
$$

Each step uses the forward rate from the corresponding future.

---

### Stage 3: Interest Rate Swaps

#### Instrument Description

A **payer swap** with:
- Fixed leg: pays fixed rate $S$ on notional $N$
- Floating leg: receives floating rate (e.g., 3M LIBOR/SOFR)

The swap rate $S_n$ for an $n$-year swap is the rate that makes the swap have zero initial value.

#### Swap Valuation

The present value of a swap is:

$$
V_{\text{swap}} = \underbrace{\sum_{i=1}^{n} \delta_i P(0, T_i) \cdot (F_i - S)}_{\text{floating - fixed}}
$$

where $F_i$ is the forward rate for period $i$.

At inception, $V_{\text{swap}} = 0$ when $S = S_n$ (the par swap rate).

#### Par Swap Rate Formula

The par swap rate satisfies:

$$
S_n = \frac{P(0, T_0) - P(0, T_n)}{\sum_{i=1}^n \delta_i P(0, T_i)}
$$

For a spot-starting swap with $T_0 = 0$ (so $P(0, T_0) = 1$):

$$
S_n = \frac{1 - P(0, T_n)}{\sum_{i=1}^n \delta_i P(0, T_i)}
$$

#### Bootstrapping Formula

Rearranging to solve for the unknown $P(0, T_n)$:

$$
P(0, T_n) = \frac{1 - S_n \sum_{i=1}^{n-1} \delta_i P(0, T_i)}{1 + S_n \delta_n}
$$

This requires all previous discount factors $P(0, T_1), \ldots, P(0, T_{n-1})$.

#### Sequential Application

Given swap rates for maturities 1Y, 2Y, 3Y, ..., 30Y:

1. Use deposits/futures to get $P(0, T)$ for $T \leq 1Y$
2. Use 1Y swap rate to get $P(0, 1Y)$ (or verify consistency)
3. Use 2Y swap rate + $P(0, 1Y)$ to get $P(0, 2Y)$
4. Continue inductively...

---

### Complete Bootstrapping Algorithm

```
Input: deposits {(T_d, R_d)}, futures {(T_1, T_2, F)}, swaps {(T_n, S_n)}

# Stage 1: Deposits (short end)
For each deposit (T_d, R_d):
    δ = DayCount(0, T_d)
    P(0, T_d) = 1 / (1 + R_d × δ)

# Stage 2: Futures (middle)  
For each future (T_1, T_2, F) in chronological order:
    R_fut = (100 - F) / 100
    F_fwd = R_fut - ConvexityAdjustment(T_1, T_2)
    P(0, T_2) = P(0, T_1) / (1 + F_fwd × (T_2 - T_1))

# Stage 3: Swaps (long end)
For each swap (T_n, S_n) in chronological order:
    annuity = Σ_{i=1}^{n-1} δ_i × P(0, T_i)
    P(0, T_n) = (1 - S_n × annuity) / (1 + S_n × δ_n)

Output: Discount curve {P(0, T)}
```

---

### Interpolation Between Nodes

#### The Need for Interpolation

Bootstrapping produces discount factors at **discrete** maturities. Pricing arbitrary instruments requires values at **any** maturity.

#### Common Interpolation Methods

**Linear on Log-Discounts:**

$$
\log P(0, T) = \frac{T_2 - T}{T_2 - T_1} \log P(0, T_1) + \frac{T - T_1}{T_2 - T_1} \log P(0, T_2)
$$

- Equivalent to linear interpolation on continuously compounded zero rates
- Simple, but produces discontinuous forward rates

**Cubic Spline on Zero Rates:**

Fit a cubic spline $z(T)$ through the bootstrapped zero rates.

- Produces smooth zero curve
- May produce oscillating forward rates

**Monotone Convex:**

Specialized method ensuring:
- Positive forward rates
- Monotone forwards in each segment
- Local control (changes don't propagate)

#### Forward Rate Implications

The choice of interpolation strongly affects forward rates:

| Method | Zero Curve | Forward Curve |
|--------|------------|---------------|
| Linear on log-discounts | Piecewise linear | Piecewise constant (jumps at nodes) |
| Cubic spline | Smooth | Can oscillate, may go negative |
| Monotone convex | Smooth | Monotone within segments |

---

### Multi-Curve Bootstrapping

#### Post-2008 Reality

After the 2008 financial crisis, the single-curve framework broke down:
- **Discounting curve:** Based on OIS (overnight indexed swap) rates
- **Forwarding curves:** Tenor-specific (1M, 3M, 6M LIBOR/SOFR)

#### Dual-Curve Bootstrap

**Step 1:** Bootstrap the OIS curve for discounting

$$
P^{\text{OIS}}(0, T_n) = \frac{1 - S_n^{\text{OIS}} \sum_{i=1}^{n-1} \delta_i P^{\text{OIS}}(0, T_i)}{1 + S_n^{\text{OIS}} \delta_n}
$$

**Step 2:** Bootstrap each tenor curve using OIS for discounting

For a 3M tenor curve, use basis swaps or directly bootstrap from instruments referencing 3M rates, discounting cashflows with $P^{\text{OIS}}$.

#### Tenor Basis Spreads

The spread between curves of different tenors reflects credit and liquidity risk:

$$
\text{Basis}_{3M/6M} = S_{3M} - S_{6M}
$$

This spread was negligible pre-crisis but became significant afterward.

---

### Numerical Considerations

#### Solver Techniques

For complex instruments (e.g., in-arrears swaps), analytic inversion may not be possible. Use:

- **Newton-Raphson:** For single discount factor per instrument
- **Multidimensional optimization:** For simultaneous fitting

#### Error Handling

Common issues and remedies:

| Issue | Symptom | Remedy |
|-------|---------|--------|
| Negative discount factor | $P(0,T) \leq 0$ | Check input data, adjust interpolation |
| Non-monotone | $P(0,T_1) < P(0,T_2)$ | Verify instrument ordering |
| Discontinuous forwards | Jumps at bootstrap nodes | Use smoother interpolation |
| Poor convergence | Solver fails | Check for data inconsistency |

#### Verification

After bootstrapping, verify by **repricing** all input instruments:

$$
\max_i |V_i^{\text{model}} - V_i^{\text{market}}| < \epsilon
$$

A well-constructed curve should reprice inputs to within bid-ask tolerance.

---

### Example: USD Curve Bootstrap

#### Market Data (Illustrative)

| Instrument | Maturity | Quote |
|------------|----------|-------|
| Deposit | 1M | 5.25% |
| Deposit | 3M | 5.35% |
| Future (Jun) | 6M | 94.50 |
| Future (Sep) | 9M | 94.30 |
| Swap | 1Y | 5.00% |
| Swap | 2Y | 4.80% |
| Swap | 5Y | 4.50% |
| Swap | 10Y | 4.40% |

#### Bootstrap Results

| Maturity | Discount Factor | Zero Rate |
|----------|-----------------|-----------|
| 1M | 0.9957 | 5.25% |
| 3M | 0.9867 | 5.35% |
| 6M | 0.9738 | 5.43% |
| 9M | 0.9604 | 5.53% |
| 1Y | 0.9524 | 4.88% |
| 2Y | 0.9074 | 4.85% |
| 5Y | 0.8007 | 4.45% |
| 10Y | 0.6440 | 4.40% |

---

### Key Takeaways

- Bootstrapping sequentially extracts discount factors from short to long maturities
- Three stages: deposits → futures → swaps
- Interpolation method critically affects forward rates
- Post-2008: Multi-curve framework with OIS discounting is essential
- Verification by repricing inputs ensures curve consistency

---

### Further Reading

- Ametrano & Bianchetti, "Bootstrapping the Illiquidity"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 1
- Hagan & West, "Interpolation Methods for Curve Construction"
- Henrard, *Interest Rate Modelling in the Multi-Curve Framework*

---

## Exercises

**Exercise 1.** A 6-month deposit quotes a simply compounded rate of $L = 3.0\%$ with ACT/360 day count and 182 days to maturity. Compute the discount factor $P(0, 0.5)$ using $P = 1/(1 + L \cdot \delta)$ where $\delta = 182/360$. Then compute the continuously compounded zero rate $R$ such that $P = e^{-R \cdot 0.5}$.

---

**Exercise 2.** Given deposit-derived discount factors $P(0, 0.25) = 0.9925$ and $P(0, 0.5) = 0.9845$, and a 1-year par swap rate of $S_1 = 3.2\%$ with semi-annual payments, bootstrap the 1-year discount factor $P(0, 1.0)$ by solving $S_1 = \frac{1 - P(0,1)}{0.5 \cdot P(0, 0.5) + 0.5 \cdot P(0, 1)}$.

---

**Exercise 3.** Explain why bootstrapping must proceed sequentially from short to long maturities. What would happen if you tried to extract $P(0, 5)$ from a 5-year swap rate without first determining all intermediate discount factors?

---

**Exercise 4.** Eurodollar futures quote a rate that differs from the forward rate by a convexity adjustment. If the futures rate is $F_{\text{fut}} = 3.5\%$ and the convexity adjustment is estimated at 5 basis points, what forward rate should be used for bootstrapping? Explain the economic reason for the convexity adjustment.

---

**Exercise 5.** A bootstrapping algorithm uses deposit rates for maturities up to 6 months, futures for 6 months to 2 years, and swap rates from 2 to 30 years. Describe the potential discontinuity in the forward rate curve at the transition points between instrument types. How can this be mitigated?

---

**Exercise 6.** Implement the bootstrapping step for a 3-year annual swap rate $S_3 = 3.8\%$, given previously bootstrapped discount factors $P(0,1) = 0.968$ and $P(0,2) = 0.935$. Solve for $P(0,3)$ and compute the implied 1-year forward rate $f(0; 2, 3)$.
