# Credit Spreads and OAS: Supplementary Content

This addendum addresses specific enhancement suggestions from the chapter review, including spread convexity, OAS sensitivity to volatility assumptions, and a conceptual OAS calculation example.

---

## Spread Convexity for Large Spread Moves


**The problem with linear spread approximations:**

The standard formula for spread duration assumes linear price-spread relationships:

$$
\Delta P \approx -D_s \times \Delta S \times P
$$

This approximation breaks down for large spread moves due to **spread convexity**.

### Mathematical Framework


**Taylor expansion of price as function of spread:**

$$
P(S + \Delta S) \approx P(S) + \frac{\partial P}{\partial S} \Delta S + \frac{1}{2} \frac{\partial^2 P}{\partial S^2} (\Delta S)^2 + O((\Delta S)^3)
$$

**Defining spread convexity:**

$$
C_s = \frac{1}{P} \frac{\partial^2 P}{\partial S^2}
$$

**More accurate price change formula:**

$$
\frac{\Delta P}{P} \approx -D_s \times \Delta S + \frac{1}{2} C_s \times (\Delta S)^2
$$

### Why Spread Convexity Matters


**For large spread moves (>50 bp), convexity materially affects P&L:**

| Spread Move | Duration Effect | Convexity Effect | Total | Error Without Convexity |
|-------------|-----------------|------------------|-------|------------------------|
| 25 bp | -1.125% | +0.01% | -1.115% | 0.01% |
| 50 bp | -2.250% | +0.05% | -2.200% | 0.05% |
| 100 bp | -4.500% | +0.20% | -4.300% | 0.20% |
| 200 bp | -9.000% | +0.80% | -8.200% | 0.80% |
| 500 bp | -22.500% | +5.00% | -17.500% | 5.00% |

*Assuming 4.5 year spread duration and typical convexity.*

**Key insight:** Spread convexity is always positive for standard bonds—the second-order term partially offsets duration losses when spreads widen.

### Calculating Spread Convexity


**Numerical approximation:**

$$
C_s \approx \frac{P(S + \Delta) + P(S - \Delta) - 2P(S)}{P(S) \times \Delta^2}
$$

**Example:**

For a 5-year BBB corporate bond:
- Current spread: 150 bp
- Price at 150 bp: $100.00
- Price at 160 bp: $99.55
- Price at 140 bp: $100.46

$$
C_s = \frac{100.46 + 99.55 - 2 \times 100.00}{100.00 \times (0.001)^2} = \frac{0.01}{0.0001} = 100
$$

**Convexity contribution for 100 bp widening:**

$$
\frac{1}{2} \times 100 \times (0.01)^2 = 0.50\%
$$

This partially offsets the 4.5% duration loss.

### Practical Applications


**1. Crisis P&L Estimation:**

In March 2020, IG spreads widened from 100 bp to 250 bp (150 bp move).

**Without convexity:**
$$
\text{Loss} = -4.5 \times 1.50\% = -6.75\%
$$

**With convexity (C_s ≈ 80):**
$$
\text{Loss} = -6.75\% + 0.5 \times 80 \times (0.015)^2 = -6.75\% + 0.90\% = -5.85\%
$$

**Error from ignoring convexity: 0.90% (13% of total move)**

**2. Hedging Large Portfolios:**

For portfolios >$1B, the convexity error can exceed $10M in crisis scenarios.

**Recommendation:** Always include convexity in stress testing and scenario analysis for large portfolios or extreme moves (>100 bp).

---

## OAS Sensitivity to Interest Rate Volatility Assumptions


**The hidden parameter in OAS:**

OAS is calculated by simulating interest rate paths and determining the spread that equates model price to market price. A critical input is the **interest rate volatility assumption**.

### The Volatility-OAS Relationship


**For callable bonds:**

$$
\text{OAS} = \text{Z-spread} - \text{Option Value}
$$

**Option value depends on rate volatility:**

$$
\text{Option Value} = f(\sigma_r) \quad \text{(increasing in volatility)}
$$

**Therefore:**

$$
\frac{\partial \text{OAS}}{\partial \sigma_r} < 0 \quad \text{(for callable bonds)}
$$

Higher volatility assumption → Higher option value → Lower OAS

### Quantifying the Sensitivity


**Example: 10-year callable corporate (callable in 3 years)**

| Assumed Rate Vol | Z-spread | Option Value | OAS |
|------------------|----------|--------------|-----|
| 15% (low) | 180 bp | 25 bp | 155 bp |
| 20% (market) | 180 bp | 35 bp | 145 bp |
| 25% (high) | 180 bp | 48 bp | 132 bp |
| 30% (stress) | 180 bp | 62 bp | 118 bp |

**Impact:** A 10% increase in vol assumption changes OAS by ~13 bp (9%).

### Sources of Volatility Inputs


**1. Swaption Market:**
- Most common source
- Observable, market-based
- At-the-money swaption implied volatilities
- Example: 3Y × 7Y swaption vol for 10nc3 bond

**2. Cap/Floor Market:**
- Alternative source
- LIBOR/SOFR caps and floors
- May differ from swaption vol

**3. Historical Volatility:**
- Realized rate movements
- Backward-looking
- May underestimate stress scenarios

**4. Model Calibration:**
- Fit to current option prices
- Ensures no-arbitrage
- Standard practice for dealers

### Best Practices


**1. Consistency:**
- Use same vol source across portfolio
- Compare OAS on equal footing
- Document assumptions

**2. Sensitivity Analysis:**
- Report OAS at ±5% vol shifts
- Understand parameter sensitivity
- Flag high-sensitivity positions

**3. Market Calibration:**
- Use current swaption vols
- Update regularly (daily for trading desks)
- Avoid stale parameters

**4. Stress Testing:**
- Calculate OAS at crisis vol levels (2008, 2020)
- Understand OAS in stress
- Vol can spike 50-100%

---

## OAS Calculation via Monte Carlo: Conceptual Example


**Step-by-step OAS calculation for a callable bond:**

### Problem Setup


**Bond characteristics:**
- Face value: $100
- Coupon: 5.0% (semi-annual)
- Maturity: 10 years
- Call feature: Callable at par after year 3
- Current market price: $102.50

**Risk-free curve (spot rates):**

| Maturity | Spot Rate |
|----------|-----------|
| 1Y | 4.00% |
| 2Y | 4.20% |
| 3Y | 4.35% |
| 5Y | 4.50% |
| 7Y | 4.60% |
| 10Y | 4.70% |

**Interest rate model:** One-factor Hull-White with mean reversion

$$
dr_t = \kappa(\theta(t) - r_t)dt + \sigma dW_t
$$

Parameters: $\kappa = 0.10$, $\sigma = 1.0\%$

### Monte Carlo Simulation Process


**Step 1: Generate interest rate paths**

Generate $N = 10,000$ paths of the short rate over 10 years with monthly timesteps.

Each path $i$ gives rates $\{r_t^{(i)}\}$ for $t = 0, 1/12, 2/12, ..., 10$.

**Step 2: Determine call decision on each path**

At each call date $t_c$ (starting year 3), calculate the bond value assuming no call:

$$
V_{\text{hold}}(t_c) = \sum_{s>t_c} \frac{CF_s}{\prod_{u=t_c}^{s}(1 + r_u)}
$$

**Call rule:** Issuer calls if $V_{\text{hold}}(t_c) > 100$ (call price).

**Step 3: Calculate cash flows on each path**

- If called at $t_c$: Cash flows are coupons until $t_c$, then $100 at $t_c$
- If not called: Full coupon stream plus $100 at maturity

**Step 4: Discount at spot rates + OAS**

For path $i$:

$$
PV^{(i)}(\text{OAS}) = \sum_t \frac{CF_t^{(i)}}{(1 + r_t + \text{OAS})^t}
$$

**Step 5: Average across paths**

$$
\text{Model Price}(\text{OAS}) = \frac{1}{N} \sum_{i=1}^{N} PV^{(i)}(\text{OAS})
$$

**Step 6: Solve for OAS**

Find OAS such that:

$$
\text{Model Price}(\text{OAS}) = \text{Market Price} = 102.50
$$

### Illustrative Results


**Intermediate calculations:**

| Statistic | Value |
|-----------|-------|
| Paths simulated | 10,000 |
| Average call probability | 65% |
| Average call date (if called) | Year 4.2 |
| Average duration | 5.8 years |

**Price sensitivity to OAS:**

| OAS | Model Price |
|-----|-------------|
| 0 bp | $106.20 |
| 25 bp | $104.70 |
| 50 bp | $103.25 |
| 60 bp | $102.80 |
| 70 bp | $102.35 |
| **72 bp** | **$102.50** |
| 75 bp | $102.15 |
| 100 bp | $101.05 |

**Solution: OAS ≈ 72 bp**

### Interpreting the Result


**Z-spread comparison:**

For this bond, Z-spread (ignoring call) = 95 bp

$$
\text{Option Value} = \text{Z-spread} - \text{OAS} = 95 - 72 = 23 \text{ bp}
$$

**Interpretation:**
- The call option is worth 23 bp annually to the issuer
- Investors receive 72 bp OAS as pure credit compensation
- The 95 bp Z-spread includes 23 bp of "call penalty"

**Relative value implication:**

If similar non-callable bonds trade at 80 bp Z-spread:
- OAS of 72 bp < comparable non-callable spread of 80 bp
- This callable bond is **expensive** (low OAS vs. peer)
- Consider selling or avoiding

---

## Summary: Enhanced OAS Analysis Framework


### Comprehensive OAS Evaluation Checklist


**1. Calculate multiple spread measures:**
- [ ] G-spread (quick reference)
- [ ] Z-spread (full curve accounting)
- [ ] OAS (option-adjusted, for callables)
- [ ] ASW spread (for relative value)

**2. OAS sensitivity analysis:**
- [ ] Base case OAS at market vol
- [ ] OAS at +5% vol (conservative)
- [ ] OAS at -5% vol (optimistic)
- [ ] OAS at crisis vol (stress test)

**3. Convexity adjustment:**
- [ ] Calculate spread convexity
- [ ] Include in scenario analysis for >50 bp moves
- [ ] Document convexity contribution to stress P&L

**4. Relative value:**
- [ ] Compare OAS to non-callable peer group
- [ ] Calculate OAS percentile (historical)
- [ ] Assess if option is fairly priced

**5. Documentation:**
- [ ] Record vol assumption used
- [ ] Note model (Hull-White, BDT, etc.)
- [ ] Update parameters regularly

### Key Formulas Summary


**Spread convexity contribution:**

$$
\text{Convexity P\&L} = \frac{1}{2} C_s (\Delta S)^2
$$

**OAS-volatility sensitivity:**

$$
\frac{\Delta \text{OAS}}{\Delta \sigma} \approx -\frac{\partial \text{Option Value}}{\partial \sigma}
$$

**Monte Carlo OAS condition:**

$$
\mathbb{E}\left[\sum_t \frac{CF_t(\text{path})}{(1 + r_t(\text{path}) + \text{OAS})^t}\right] = P_{\text{market}}
$$

These enhanced frameworks ensure more accurate OAS analysis, particularly for large portfolios, crisis scenarios, and complex callable structures.
