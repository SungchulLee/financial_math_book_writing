# Key Rate Duration

Modified duration measures the sensitivity of a bond or portfolio to a **parallel shift** in the yield curve. In practice, yield curves rarely move in parallel --- they steepen, flatten, twist, and butterfly. **Key rate duration** (KRD) generalizes duration by measuring sensitivity to shifts at specific maturities along the curve, providing a richer picture of interest rate risk. This section defines key rate shifts, derives the partial DV01 framework, presents hedging applications, and connects key rate durations to principal component analysis.

---

## Motivation: Beyond Parallel Shifts

### The Limitation of Modified Duration

Recall that modified duration gives the price sensitivity to a uniform yield change:

$$
\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y
$$

This assumes the entire yield curve moves by the same amount $\Delta y$. Empirically, however:

- Short-term rates are driven by central bank policy and may move independently of long rates
- The yield curve steepens during easing cycles and flattens during tightening cycles
- The "belly" of the curve (5--7 year sector) can move differently from both ends

A 10-year zero-coupon bond and a barbell portfolio of 2-year and 30-year bonds can have the same modified duration but very different responses to a curve steepening.

### What Key Rate Duration Measures

Key rate duration decomposes the total interest rate sensitivity into contributions from **specific maturity points** on the yield curve. If the yield curve moves by different amounts at different maturities, the total price change is:

$$
\frac{\Delta P}{P} \approx -\sum_{k=1}^{K} \text{KRD}_k \cdot \Delta y_k
$$

where $\text{KRD}_k$ is the key rate duration at maturity $\tau_k$ and $\Delta y_k$ is the yield change at that maturity.

---

## Key Rate Shift Functions

### Standard Key Rates

The yield curve is sampled at $K$ **key rate maturities**:

$$
\tau_1 < \tau_2 < \cdots < \tau_K
$$

Common choices: 3M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 15Y, 20Y, 25Y, 30Y.

### Triangular Shift Functions

The standard construction uses **piecewise linear (triangular) shift functions** $s_k(T)$ for each key rate $\tau_k$:

$$
s_k(T) = \begin{cases}
0 & \text{if } T \leq \tau_{k-1} \\[6pt]
\dfrac{T - \tau_{k-1}}{\tau_k - \tau_{k-1}} & \text{if } \tau_{k-1} < T \leq \tau_k \\[6pt]
\dfrac{\tau_{k+1} - T}{\tau_{k+1} - \tau_k} & \text{if } \tau_k < T \leq \tau_{k+1} \\[6pt]
0 & \text{if } T > \tau_{k+1}
\end{cases}
$$

with boundary conventions: $s_1(T) = 1$ for $T \leq \tau_1$ and $s_K(T) = 1$ for $T \geq \tau_K$.

### Properties of Shift Functions

The triangular shift functions have two important properties:

**Partition of unity:** For any maturity $T$:

$$
\sum_{k=1}^{K} s_k(T) = 1
$$

This means a parallel shift of 1 bp applied to all key rates simultaneously produces a uniform 1 bp shift across the entire curve.

**Locality:** Each key rate shift $s_k$ is nonzero only in the interval $[\tau_{k-1}, \tau_{k+1}]$, so a shift at key rate $k$ affects only the yields in its immediate neighborhood.

---

## Key Rate Duration: Definition and Computation

### Definition

The **key rate duration** at key rate $k$ is defined as:

$$
\boxed{\text{KRD}_k = -\frac{1}{P} \frac{\partial P}{\partial y_k}}
$$

where the partial derivative represents the price change when the yield curve is shifted by the function $s_k(T)$ applied with magnitude $\Delta y_k$.

### Numerical Computation

In practice, key rate durations are computed by **finite differences**:

$$
\text{KRD}_k \approx -\frac{P(y + \Delta y \cdot s_k) - P(y - \Delta y \cdot s_k)}{2 \, P(y) \, \Delta y}
$$

where $\Delta y$ is a small shift (typically 1 bp = 0.0001).

**Algorithm:**

1. Price the instrument at the base yield curve: $P_0 = P(y)$
2. For each key rate $k = 1, \ldots, K$:
    - Shift the yield curve up: $y^+(T) = y(T) + \Delta y \cdot s_k(T)$
    - Price: $P_k^+ = P(y^+)$
    - Shift the yield curve down: $y^-(T) = y(T) - \Delta y \cdot s_k(T)$
    - Price: $P_k^- = P(y^-)$
    - Compute: $\text{KRD}_k = -(P_k^+ - P_k^-)/(2 P_0 \Delta y)$

### Key Rate DV01 (Partial DV01)

The **key rate DV01** (or **partial DV01**, or **bucket DV01**) is the dollar price change per 1 bp shift at key rate $k$:

$$
\text{KR-DV01}_k = -\frac{\partial P}{\partial y_k} \times 0.0001 = \text{KRD}_k \times P \times 0.0001
$$

### Relationship to Modified Duration

The sum of all key rate durations equals the modified duration (for a parallel shift):

$$
\boxed{\sum_{k=1}^{K} \text{KRD}_k = D_{\text{mod}}}
$$

This follows from the partition of unity: $\sum_k s_k(T) = 1$ implies a simultaneous 1 bp shift at all key rates is equivalent to a parallel 1 bp shift.

---

## Worked Example: Key Rate Durations of a Coupon Bond

??? example "Key Rate Duration Calculation"

    **Setup:** A 10-year, 5% annual coupon bond priced at par (yield = 5%), face value \$100.

    **Key rates:** 1Y, 2Y, 3Y, 5Y, 7Y, 10Y.

    **Cash flows:**

    | Year | Cash Flow | PV (at 5%) |
    |---|---|---|
    | 1 | 5 | 4.762 |
    | 2 | 5 | 4.535 |
    | 3 | 5 | 4.319 |
    | 4 | 5 | 4.114 |
    | 5 | 5 | 3.918 |
    | 6 | 5 | 3.731 |
    | 7 | 5 | 3.553 |
    | 8 | 5 | 3.384 |
    | 9 | 5 | 3.223 |
    | 10 | 105 | 64.461 |
    | **Total** | | **100.000** |

    **Step 1: Shift the 1Y key rate by 1 bp (up and down)**

    The 1Y shift function $s_1(T)$ is 1 at $T = 1$, linearly declining to 0 at $T = 2$, and 0 for $T > 2$.

    - At $T = 1$: yield shifts by 1 bp to 5.01%
    - At $T = 1.5$: yield shifts by 0.5 bp
    - At $T \geq 2$: no change

    Repricing gives $P^+ = 99.9995$, $P^- = 100.0005$.

    $\text{KRD}_1 = -(99.9995 - 100.0005)/(2 \times 100 \times 0.0001) = 0.050$

    **Step 2: Repeat for each key rate**

    | Key Rate | KRD | KR-DV01 (\$) |
    |---|---|---|
    | 1Y | 0.050 | 0.50 |
    | 2Y | 0.048 | 0.48 |
    | 3Y | 0.045 | 0.45 |
    | 5Y | 0.168 | 1.68 |
    | 7Y | 0.153 | 1.53 |
    | 10Y | 6.458 | 64.58 |
    | **Total** | **6.922** | **69.22** |

    **Observations:**

    - The 10Y key rate dominates because 64.5% of the bond's present value comes from the final coupon + principal payment
    - Short-tenor key rate durations are small because only the coupon cash flows at those tenors are affected
    - The total $\sum \text{KRD}_k = 6.922$ equals the modified duration (within rounding)

---

## Hedging Yield Curve Risk

### The Hedging Problem

Given a portfolio with key rate DV01 profile $\text{KR-DV01}_k^{\text{port}}$ for $k = 1, \ldots, K$, we want to find hedge positions in $m$ instruments with key rate DV01 profiles $\text{KR-DV01}_k^{(j)}$ for $j = 1, \ldots, m$ such that:

$$
\sum_{j=1}^{m} h_j \cdot \text{KR-DV01}_k^{(j)} + \text{KR-DV01}_k^{\text{port}} = 0 \quad \text{for all } k
$$

where $h_j$ is the hedge ratio (notional) for instrument $j$.

### Matrix Formulation

Defining $A_{kj} = \text{KR-DV01}_k^{(j)}$ and $b_k = -\text{KR-DV01}_k^{\text{port}}$:

$$
Ah = b
$$

- If $m = K$ (as many instruments as key rates): exact hedge, $h = A^{-1}b$
- If $m < K$: under-determined; use least-squares or accept residual risk
- If $m > K$: over-determined; use minimum-notional or other optimization criteria

### Practical Hedge Construction

!!! tip "Hedging with Swaps"
    In practice, interest rate swaps of various tenors are used as hedging instruments. A common setup:

    - **Key rates:** 2Y, 5Y, 10Y, 30Y (4 key rates)
    - **Hedging instruments:** 2Y, 5Y, 10Y, 30Y par swaps
    - Each swap has a concentrated KR-DV01 profile near its maturity
    - The system $Ah = b$ is nearly diagonal and easy to solve

---

## Worked Example: Bucket Hedge

??? example "Key Rate Hedging a Bond Portfolio"

    **Portfolio:** Long \$10M 10-year bond (from previous example).

    **Key rate DV01 profile (per \$100 face):**

    | Key Rate | Portfolio KR-DV01 |
    |---|---|
    | 2Y | \$980 |
    | 5Y | \$1,680 |
    | 10Y | \$64,580 |

    **Hedging instruments:** Par swaps (per \$1M notional):

    | Instrument | 2Y KR-DV01 | 5Y KR-DV01 | 10Y KR-DV01 |
    |---|---|---|---|
    | 2Y Swap | \$195 | \$0 | \$0 |
    | 5Y Swap | \$0 | \$475 | \$0 |
    | 10Y Swap | \$0 | \$0 | \$880 |

    **Hedge ratios:**

    $h_{\text{2Y}} = -980 / 195 = -\$5.03\text{M notional (pay fixed)}$

    $h_{\text{5Y}} = -1,680 / 475 = -\$3.54\text{M notional (pay fixed)}$

    $h_{\text{10Y}} = -64,580 / 880 = -\$73.39\text{M notional (pay fixed)}$

    **Result:** The hedged portfolio has zero KR-DV01 at each key rate, providing protection against steepening, flattening, and butterfly moves. The 10Y hedge dominates because the bond has concentrated exposure at the 10-year point.

---

## Connection to Principal Component Analysis

### PCA of Yield Curve Movements

Principal Component Analysis (PCA) applied to historical yield curve changes reveals that 95--99% of yield curve variation is explained by three factors:

$$
\Delta y(T) \approx z_1 \cdot \text{PC}_1(T) + z_2 \cdot \text{PC}_2(T) + z_3 \cdot \text{PC}_3(T)
$$

where $z_1, z_2, z_3$ are the factor loadings (random) and $\text{PC}_1, \text{PC}_2, \text{PC}_3$ are the principal components (deterministic functions of maturity):

| Component | Shape | Variance Explained | Interpretation |
|---|---|---|---|
| PC1 | Approximately flat | 80--90% | Level (parallel shift) |
| PC2 | Upward-sloping | 5--10% | Slope (steepening/flattening) |
| PC3 | Humped | 2--5% | Curvature (butterfly) |

### KRD-PCA Relationship

The P&L of a portfolio under a yield curve scenario can be decomposed in two ways:

**Key rate decomposition:**

$$
\Delta P \approx -P \sum_{k=1}^{K} \text{KRD}_k \cdot \Delta y_k
$$

**PCA decomposition:**

$$
\Delta P \approx -P \sum_{j=1}^{3} z_j \underbrace{\left(\sum_{k=1}^{K} \text{KRD}_k \cdot \text{PC}_j(\tau_k)\right)}_{\text{PC duration}_j}
$$

The **PC duration** for factor $j$ is the portfolio's sensitivity to a unit move in principal component $j$:

$$
D_{\text{PC},j} = \sum_{k=1}^{K} \text{KRD}_k \cdot \text{PC}_j(\tau_k)
$$

### Interpretation

- **$D_{\text{PC},1}$:** Sensitivity to level (approximately equal to modified duration)
- **$D_{\text{PC},2}$:** Sensitivity to slope (steepening/flattening exposure)
- **$D_{\text{PC},3}$:** Sensitivity to curvature (butterfly exposure)

!!! info "Theorem (KRD-PCA Equivalence)"
    The key rate duration profile $(\text{KRD}_1, \ldots, \text{KRD}_K)$ and the PC duration profile $(D_{\text{PC},1}, D_{\text{PC},2}, D_{\text{PC},3})$ contain the same information, related by the linear transformation:

    $$
    D_{\text{PC},j} = \sum_{k=1}^{K} \text{KRD}_k \cdot \text{PC}_j(\tau_k)
    $$

    Conversely, if the first three PCs span the space of plausible yield curve moves, the KRD profile can be approximated from the PC durations:

    $$
    \text{KRD}_k \approx \sum_{j=1}^{3} D_{\text{PC},j} \cdot \text{PC}_j(\tau_k) \cdot w_k
    $$

    where $w_k$ are appropriate weights depending on the eigenvalues.

---

## Bucket Risk for Interest Rate Derivatives

### Swap DV01 Profile

An interest rate swap has a characteristic key rate DV01 profile:

- **Fixed leg:** Concentrated near the swap maturity (like a bond)
- **Floating leg:** Very small, concentrated at the next reset date
- **Net (payer swap):** Positive KR-DV01 concentrated at the swap maturity, small negative KR-DV01 at the front end

### Cap/Floor DV01 Profile

A cap or floor has key rate DV01 distributed across all caplet maturities:

$$
\text{KR-DV01}_k^{\text{cap}} = \sum_{i} \text{KR-DV01}_k^{\text{caplet}_i}
$$

Each caplet contributes primarily at its own maturity, so the cap has a distributed exposure profile unlike a swap.

### Swaption DV01 Profile

A swaption's KR-DV01 profile depends on the delta:

- **Deep ITM payer swaption:** Behaves like a payer swap (concentrated exposure)
- **Deep OTM swaption:** Very small, spread-out KR-DV01
- **ATM swaption:** Intermediate, with exposure at both the option expiry and the underlying swap tenor

---

## Risk Reporting and Limits

### Bucket Risk Report

A standard risk report presents the KR-DV01 profile:

| Key Rate | Portfolio KR-DV01 | Limit | Utilization |
|---|---|---|---|
| 3M | \$5,200 | \$50,000 | 10.4% |
| 1Y | \$12,400 | \$50,000 | 24.8% |
| 2Y | \$28,300 | \$100,000 | 28.3% |
| 5Y | \$67,500 | \$200,000 | 33.8% |
| 10Y | \$124,000 | \$200,000 | 62.0% |
| 30Y | \$45,600 | \$150,000 | 30.4% |

### Risk Aggregation

The total portfolio risk under a given yield curve scenario is:

$$
\text{P\&L} = -\sum_k \text{KR-DV01}_k \cdot \Delta y_k
$$

For risk measurement, the variance of P&L is:

$$
\text{Var}(\text{P\&L}) = \sum_{k,l} \text{KR-DV01}_k \cdot \text{KR-DV01}_l \cdot \text{Cov}(\Delta y_k, \Delta y_l)
$$

The covariance matrix $\text{Cov}(\Delta y_k, \Delta y_l)$ can be estimated historically or derived from the PCA decomposition:

$$
\text{Cov}(\Delta y_k, \Delta y_l) = \sum_{j=1}^{3} \lambda_j \cdot \text{PC}_j(\tau_k) \cdot \text{PC}_j(\tau_l)
$$

where $\lambda_j$ is the variance of the $j$-th principal component.

---

## Key Takeaways

- **Key rate duration** measures price sensitivity to yield shifts at specific maturities, generalizing modified duration to non-parallel curve moves
- **Triangular shift functions** provide a partition-of-unity construction ensuring that the sum of KRDs equals the modified duration
- **Numerical computation** uses finite differences: bump the curve at each key rate and reprice
- **Key rate DV01** (partial DV01, bucket DV01) is the dollar sensitivity per basis point at each key rate
- **Hedging** with KRDs involves matching the KR-DV01 profile across all key rates, typically using swaps of various tenors
- **PCA connection:** The first three principal components (level, slope, curvature) explain 95--99% of yield curve variation; PC durations are linear combinations of KRDs
- **Bucket risk** reporting is the industry standard for managing yield curve exposure in trading books

---

## Further Reading

- Ho (1992), "Key Rate Durations: Measures of Interest Rate Risks"
- Tuckman & Serrat (2011), *Fixed Income Securities*, Chapters 5--7
- Fabozzi (2007), *Fixed Income Analysis*, Chapter on Duration
- Litterman & Scheinkman (1991), "Common Factors Affecting Bond Returns" (PCA of yield curves)

---

## Exercises

**Exercise 1.** Consider a 5-year zero-coupon bond priced at par yield 4\%, with key rates at 2Y, 5Y, and 10Y. Using the triangular shift functions defined in this section, determine which key rate shifts affect this bond's price. Compute the key rate durations at 2Y, 5Y, and 10Y. Verify that their sum equals the modified duration.

??? success "Solution to Exercise 1"

    A 5-year zero-coupon bond has a single cashflow at maturity $T = 5$. With key rates at 2Y, 5Y, and 10Y:

    **Which shifts affect the bond?**

    The bond's cashflow is at $T = 5$, which coincides with the 5Y key rate. We examine each shift function:

    - **2Y shift** $s_1(T)$: The triangular function centered at 2Y is nonzero for $T \in [0, 5]$ (since 5Y is the next key rate). At $T = 5$: $s_1(5) = 0$ (the shift has decayed to zero by the 5Y point). For $T$ between 2Y and 5Y, $s_1(T) = (5 - T)/(5 - 2) = (5 - T)/3$. At $T = 5$: $s_1 = 0$. So the 2Y shift does **not** affect the bond price (since the cashflow is exactly at $T = 5$, where $s_1 = 0$).

    - **5Y shift** $s_2(T)$: The triangular function centered at 5Y. At $T = 5$: $s_2(5) = 1$. The bond's only cashflow is at this point, so the 5Y shift fully affects the bond.

    - **10Y shift** $s_3(T)$: The triangular function centered at 10Y. At $T = 5$: since 5Y is the key rate before 10Y, $s_3(5) = (5 - 5)/(10 - 5) = 0$. So the 10Y shift does not affect the bond.

    **Key rate durations:**

    For a zero-coupon bond priced as $P = e^{-y(5) \cdot 5}$:

    When we shift key rate $k$ by $\Delta y$, the yield at maturity $T = 5$ changes by $\Delta y \cdot s_k(5)$.

    $$
    \text{KRD}_{2Y} = -\frac{1}{P}\frac{\partial P}{\partial y_{2Y}} = 5 \times s_1(5) = 5 \times 0 = 0
    $$

    $$
    \text{KRD}_{5Y} = 5 \times s_2(5) = 5 \times 1 = 5
    $$

    $$
    \text{KRD}_{10Y} = 5 \times s_3(5) = 5 \times 0 = 0
    $$

    **Verification:**

    $$
    \sum_k \text{KRD}_k = 0 + 5 + 0 = 5 = T = D_{\text{mod}} \checkmark
    $$

    The modified duration of a 5-year zero-coupon bond is 5 years, and it is entirely concentrated at the 5Y key rate. This makes intuitive sense: the bond's sensitivity is localized at its maturity point on the curve.

---

**Exercise 2.** Show that the triangular shift functions satisfy the partition of unity property $\sum_{k=1}^{K} s_k(T) = 1$ for any maturity $T$. Using this result, prove that $\sum_{k=1}^{K} \text{KRD}_k = D_{\text{mod}}$ for any bond or portfolio.

??? success "Solution to Exercise 2"

    **Partition of unity:** Consider any maturity $T$ with $\tau_{k-1} \leq T \leq \tau_k$ for some $k$ (i.e., $T$ lies between consecutive key rates). By the definition of the triangular shift functions:

    - $s_{k-1}(T) = (\tau_k - T)/(\tau_k - \tau_{k-1})$ (the declining part of the triangle centered at $\tau_{k-1}$)
    - $s_k(T) = (T - \tau_{k-1})/(\tau_k - \tau_{k-1})$ (the rising part of the triangle centered at $\tau_k$)
    - $s_j(T) = 0$ for all $j \neq k-1, k$

    Therefore:

    $$
    \sum_{j=1}^K s_j(T) = s_{k-1}(T) + s_k(T) = \frac{\tau_k - T}{\tau_k - \tau_{k-1}} + \frac{T - \tau_{k-1}}{\tau_k - \tau_{k-1}} = \frac{\tau_k - \tau_{k-1}}{\tau_k - \tau_{k-1}} = 1
    $$

    At the boundary cases: for $T \leq \tau_1$, $s_1(T) = 1$ and all others are 0. For $T \geq \tau_K$, $s_K(T) = 1$ and all others are 0. In both cases the sum is 1.

    **Proof that $\sum_k \text{KRD}_k = D_{\text{mod}}$:**

    A parallel shift of magnitude $\Delta y$ at all key rates simultaneously produces a yield curve change:

    $$
    \Delta y(T) = \Delta y \cdot \sum_{k=1}^K s_k(T) = \Delta y \cdot 1 = \Delta y
    $$

    for all $T$ (by partition of unity). This is a uniform parallel shift.

    The total price change under this shift is:

    $$
    \Delta P = \sum_{k=1}^K \frac{\partial P}{\partial y_k} \Delta y = -P \sum_{k=1}^K \text{KRD}_k \cdot \Delta y
    $$

    But under a parallel shift $\Delta y$, the price change is also:

    $$
    \Delta P = -P \cdot D_{\text{mod}} \cdot \Delta y
    $$

    Equating:

    $$
    -P \sum_k \text{KRD}_k \cdot \Delta y = -P \cdot D_{\text{mod}} \cdot \Delta y
    $$

    Dividing by $-P \cdot \Delta y$:

    $$
    \sum_{k=1}^K \text{KRD}_k = D_{\text{mod}} \qquad \blacksquare
    $$

---

**Exercise 3.** A portfolio has the following key rate DV01 profile (per \$100M notional):

| Key Rate | 2Y | 5Y | 10Y | 30Y |
|---|---|---|---|---|
| KR-DV01 | \$3,200 | \$8,500 | \$15,000 | \$2,300 |

Suppose the yield curve steepens: the 2Y rate falls by 25 bps, the 5Y rate is unchanged, the 10Y rate rises by 15 bps, and the 30Y rate rises by 30 bps. Compute the portfolio P\&L. What would the P\&L be under a parallel shift of $+10$ bps?

??? success "Solution to Exercise 3"

    **Given KR-DV01 profile (per \$100M notional):**

    | Key Rate | 2Y | 5Y | 10Y | 30Y |
    |---|---|---|---|---|
    | KR-DV01 | \$3,200 | \$8,500 | \$15,000 | \$2,300 |

    **Scenario 1: Curve steepening.**

    $\Delta y_{2Y} = -25$ bps $= -0.0025$, $\Delta y_{5Y} = 0$, $\Delta y_{10Y} = +15$ bps $= +0.0015$, $\Delta y_{30Y} = +30$ bps $= +0.0030$.

    $$
    \text{P\&L} = -\sum_k \text{KR-DV01}_k \cdot \frac{\Delta y_k}{0.0001}
    $$

    (Since KR-DV01 is the dollar change per 1 bp, we multiply by the number of bps.)

    $$
    \text{P\&L} = -[3{,}200 \times (-25) + 8{,}500 \times 0 + 15{,}000 \times 15 + 2{,}300 \times 30]
    $$

    $$
    = -[-80{,}000 + 0 + 225{,}000 + 69{,}000]
    $$

    $$
    = -[214{,}000] = -\$214{,}000
    $$

    The portfolio **loses \$214,000** under this steepening scenario. The 2Y rally contributes a gain (\$80K), but the 10Y and 30Y sell-off causes larger losses (\$225K + \$69K).

    **Scenario 2: Parallel shift of +10 bps.**

    $$
    \text{P\&L} = -[3{,}200 \times 10 + 8{,}500 \times 10 + 15{,}000 \times 10 + 2{,}300 \times 10]
    $$

    $$
    = -[32{,}000 + 85{,}000 + 150{,}000 + 23{,}000] = -290{,}000
    $$

    The portfolio **loses \$290,000** under a 10 bp parallel shift. This is consistent with the total DV01 being \$29,000 per bp.

---

**Exercise 4.** Using the matrix formulation $Ah = b$, set up and solve the hedging problem for the portfolio in Exercise 3 using three hedging instruments: 2Y, 10Y, and 30Y par swaps. The KR-DV01 profiles (per \$1M notional) of the swaps are:

| Instrument | 2Y KR-DV01 | 5Y KR-DV01 | 10Y KR-DV01 | 30Y KR-DV01 |
|---|---|---|---|---|
| 2Y Swap | \$190 | \$0 | \$0 | \$0 |
| 10Y Swap | \$0 | \$10 | \$870 | \$0 |
| 30Y Swap | \$0 | \$0 | \$20 | \$2,500 |

Explain why the 5Y bucket cannot be fully hedged with these three instruments.

??? success "Solution to Exercise 4"

    **Matrix formulation:** We need to solve $Ah = b$ where:

    $$
    A = \begin{pmatrix} 190 & 0 & 0 \\ 0 & 10 & 0 \\ 0 & 870 & 20 \\ 0 & 0 & 2{,}500 \end{pmatrix}, \qquad b = \begin{pmatrix} 3{,}200 \\ 8{,}500 \\ 15{,}000 \\ 2{,}300 \end{pmatrix}, \qquad h = \begin{pmatrix} h_{\text{2Y}} \\ h_{\text{10Y}} \\ h_{\text{30Y}} \end{pmatrix}
    $$

    (Note: $A$ is $4 \times 3$ and $b$ is $4 \times 1$, so the system is overdetermined.)

    **Solve row by row where possible:**

    **Row 1 (2Y bucket):** $190 h_{\text{2Y}} = 3{,}200 \implies h_{\text{2Y}} = 3{,}200/190 = 16.84$ (\$M notional)

    **Row 4 (30Y bucket):** $2{,}500 h_{\text{30Y}} = 2{,}300 \implies h_{\text{30Y}} = 2{,}300/2{,}500 = 0.92$ (\$M notional)

    **Row 3 (10Y bucket):** $870 h_{\text{10Y}} + 20 h_{\text{30Y}} = 15{,}000$

    $870 h_{\text{10Y}} + 20(0.92) = 15{,}000$

    $870 h_{\text{10Y}} = 15{,}000 - 18.4 = 14{,}981.6$

    $h_{\text{10Y}} = 17.22$ (\$M notional)

    **Row 2 (5Y bucket):** $10 h_{\text{10Y}} = 8{,}500$?

    $10 \times 17.22 = 172.2 \neq 8{,}500$

    **The 5Y bucket cannot be hedged.** With the three instruments chosen, the 5Y KR-DV01 of the hedge is only $10 \times 17.22 = \$172$ (from the small 5Y exposure of the 10Y swap), far short of the required \$8,500.

    **Why:** None of the three hedging instruments has significant KR-DV01 at the 5Y point. The 2Y swap has zero exposure at 5Y. The 10Y swap has only \$10 per \$1M notional at 5Y (a tiny spillover). The 30Y swap also has zero at 5Y. To hedge the 5Y bucket, one needs a **5Y swap** (or an instrument with concentrated 5Y exposure) as an additional hedging instrument. This illustrates that $K$ key rate buckets generally require $K$ hedging instruments with distinct KR-DV01 profiles.

---

**Exercise 5.** Suppose the first three principal components of yield curve changes are PC$_1 = (1, 1, 1, 1)$, PC$_2 = (-1, -0.3, 0.3, 1)$, PC$_3 = (1, -1, -1, 1)$ at key rates 2Y, 5Y, 10Y, 30Y. For the portfolio in Exercise 3, compute the PC durations $D_{\text{PC},1}$, $D_{\text{PC},2}$, $D_{\text{PC},3}$. Interpret each: which yield curve movements pose the greatest risk?

??? success "Solution to Exercise 5"

    **Given PCs** at key rates (2Y, 5Y, 10Y, 30Y):

    - PC$_1 = (1, 1, 1, 1)$ (level)
    - PC$_2 = (-1, -0.3, 0.3, 1)$ (slope)
    - PC$_3 = (1, -1, -1, 1)$ (curvature)

    **KR-DV01 profile:** $(3{,}200, \; 8{,}500, \; 15{,}000, \; 2{,}300)$.

    **PC durations:**

    $$
    D_{\text{PC},j} = \sum_{k=1}^{4} \text{KR-DV01}_k \cdot \text{PC}_j(\tau_k)
    $$

    **PC$_1$ (Level):**

    $$
    D_{\text{PC},1} = 3{,}200(1) + 8{,}500(1) + 15{,}000(1) + 2{,}300(1) = 29{,}000
    $$

    **PC$_2$ (Slope):**

    $$
    D_{\text{PC},2} = 3{,}200(-1) + 8{,}500(-0.3) + 15{,}000(0.3) + 2{,}300(1)
    $$

    $$
    = -3{,}200 - 2{,}550 + 4{,}500 + 2{,}300 = 1{,}050
    $$

    **PC$_3$ (Curvature):**

    $$
    D_{\text{PC},3} = 3{,}200(1) + 8{,}500(-1) + 15{,}000(-1) + 2{,}300(1)
    $$

    $$
    = 3{,}200 - 8{,}500 - 15{,}000 + 2{,}300 = -18{,}000
    $$

    **Interpretation:**

    - **$D_{\text{PC},1} = 29{,}000$:** The portfolio has significant exposure to level moves. A 1 bp parallel shift causes a \$29,000 P&L (this equals the total DV01).

    - **$D_{\text{PC},2} = 1{,}050$:** The portfolio has moderate exposure to slope (steepening/flattening). A 1-unit steepening move (short rates fall, long rates rise) causes a \$1,050 loss. This is relatively small, meaning the portfolio is roughly balanced between short-end and long-end exposure.

    - **$D_{\text{PC},3} = -18{,}000$:** The portfolio has very large exposure to curvature. A positive curvature move (wings up, belly down) causes a \$18,000 gain. The negative sign means the portfolio benefits from a "butterfly" move where the 5Y and 10Y rates fall relative to the wings. This large curvature exposure arises because the portfolio has concentrated exposure at the 5Y and 10Y points (\$8,500 + \$15,000 = \$23,500) relative to the wings (2Y + 30Y = \$5,500).

    **Greatest risk:** The level factor (PC$_1$) poses the greatest absolute risk due to the \$29,000 DV01, and it also has the highest variance (80--90% of yield curve variation). The curvature factor (PC$_3$) has a large duration (\$18,000) but lower variance, so its risk contribution depends on the eigenvalue $\lambda_3$.

---

**Exercise 6.** A 10-year interest rate cap has key rate DV01 distributed across maturities 1Y through 10Y, unlike a 10-year swap which concentrates its exposure near the 10Y point. Explain qualitatively why this difference arises. How would you construct a bucket hedge for the cap using swaps of tenors 2Y, 5Y, and 10Y?

??? success "Solution to Exercise 6"

    **Why the cap has distributed KR-DV01:**

    A 10-year interest rate cap consists of individual caplets, each referencing a different forward rate and paying at a different future date. Caplet $i$ depends on the forward rate $F(T_i, T_{i+1})$ and the discount factor $P(0, T_{i+1})$, both of which are sensitive to yields near maturity $T_{i+1}$.

    - The caplet paying at year 2 is sensitive to yields near the 2Y point
    - The caplet paying at year 5 is sensitive to yields near the 5Y point
    - The caplet paying at year 10 is sensitive to yields near the 10Y point

    Each caplet contributes KR-DV01 at its own maturity, so the total cap KR-DV01 is spread across all maturities from year 1 to year 10.

    In contrast, a 10-year par swap has a fixed leg behaving like a 10-year bond (concentrated KR-DV01 at the 10Y point) and a floating leg with near-zero duration. The net KR-DV01 is heavily concentrated at the 10Y key rate.

    **Constructing a bucket hedge:**

    The cap's KR-DV01 profile might look like:

    | Key Rate | Cap KR-DV01 |
    |---|---|
    | 2Y | \$1,500 |
    | 5Y | \$3,000 |
    | 10Y | \$2,500 |

    To hedge with 2Y, 5Y, and 10Y swaps, set up the system $Ah = b$:

    Each swap has concentrated KR-DV01 near its maturity. Assuming:

    - 2Y swap: KR-DV01$_{2Y}$ = \$195/\$1M notional
    - 5Y swap: KR-DV01$_{5Y}$ = \$475/\$1M notional
    - 10Y swap: KR-DV01$_{10Y}$ = \$880/\$1M notional

    The hedge ratios are approximately:

    - $h_{2Y} = 1{,}500/195 = \$7.7$M (pay fixed in 2Y swap)
    - $h_{5Y} = 3{,}000/475 = \$6.3$M (pay fixed in 5Y swap)
    - $h_{10Y} = 2{,}500/880 = \$2.8$M (pay fixed in 10Y swap)

    This distributes the hedging notional across multiple tenors, reflecting the cap's distributed risk profile. Compare with a naive duration hedge using only a 10Y swap, which would leave the 2Y and 5Y buckets unhedged.

---

**Exercise 7.** The variance of portfolio P\&L is given by

$$
\text{Var}(\text{P\&L}) = \sum_{k,l} \text{KR-DV01}_k \cdot \text{KR-DV01}_l \cdot \text{Cov}(\Delta y_k, \Delta y_l)
$$

For a two-key-rate system (2Y, 10Y) with KR-DV01$_{\text{2Y}} = \$5{,}000$ and KR-DV01$_{\text{10Y}} = \$20{,}000$, yield volatilities $\sigma_{\text{2Y}} = 90$ bps/year and $\sigma_{\text{10Y}} = 70$ bps/year, and correlation $\rho = 0.85$, compute the annualized P\&L standard deviation. Compare with the result assuming perfect correlation ($\rho = 1$).

??? success "Solution to Exercise 7"

    **Given:** KR-DV01$_{2Y} = \$5{,}000$, KR-DV01$_{10Y} = \$20{,}000$, $\sigma_{2Y} = 90$ bps $= 0.0090$, $\sigma_{10Y} = 70$ bps $= 0.0070$, $\rho = 0.85$.

    **Covariance matrix:**

    $$
    \text{Cov}(\Delta y_{2Y}, \Delta y_{2Y}) = \sigma_{2Y}^2 = (0.0090)^2 = 8.1 \times 10^{-5}
    $$

    $$
    \text{Cov}(\Delta y_{10Y}, \Delta y_{10Y}) = \sigma_{10Y}^2 = (0.0070)^2 = 4.9 \times 10^{-5}
    $$

    $$
    \text{Cov}(\Delta y_{2Y}, \Delta y_{10Y}) = \rho \sigma_{2Y}\sigma_{10Y} = 0.85 \times 0.0090 \times 0.0070 = 5.355 \times 10^{-5}
    $$

    **Variance of P&L:**

    Note: since the P&L is $-\sum_k \text{KR-DV01}_k \cdot \Delta y_k / 0.0001$ (converting bps to yield), but KR-DV01 is already in dollars per bp, we can work directly with bp changes. Let $d_k = \text{KR-DV01}_k$ in \$/bp:

    $$
    \text{P\&L} = -d_{2Y} \cdot \Delta y_{2Y}^{(\text{bp})} - d_{10Y} \cdot \Delta y_{10Y}^{(\text{bp})}
    $$

    where $\Delta y^{(\text{bp})}$ is in basis points. Then:

    $$
    \text{Var}(\text{P\&L}) = d_{2Y}^2 \sigma_{2Y}^2 + d_{10Y}^2 \sigma_{10Y}^2 + 2 d_{2Y} d_{10Y} \rho \sigma_{2Y}\sigma_{10Y}
    $$

    with $\sigma$ in bp: $\sigma_{2Y} = 90$ bp, $\sigma_{10Y} = 70$ bp.

    $$
    \text{Var} = (5{,}000)^2(90)^2 + (20{,}000)^2(70)^2 + 2(5{,}000)(20{,}000)(0.85)(90)(70)
    $$

    $$
    = 25 \times 10^6 \times 8{,}100 + 400 \times 10^6 \times 4{,}900 + 200 \times 10^6 \times 0.85 \times 6{,}300
    $$

    $$
    = 202.5 \times 10^9 + 1{,}960 \times 10^9 + 1{,}071 \times 10^9
    $$

    $$
    = 3{,}233.5 \times 10^9
    $$

    $$
    \text{Std}(\text{P\&L}) = \sqrt{3{,}233.5 \times 10^9} = \$56{,}864/\text{year}
    $$

    Wait, let me be more careful with units. KR-DV01 is \$/bp. The yields have annual volatility in bps. So:

    $$
    \text{P\&L} = d_{2Y} \times \Delta y_{2Y} + d_{10Y} \times \Delta y_{10Y}
    $$

    where $d_k$ is in \$/bp and $\Delta y_k$ is in bp. The variance:

    $$
    \text{Var} = 5000^2 \times 90^2 + 20000^2 \times 70^2 + 2 \times 5000 \times 20000 \times 0.85 \times 90 \times 70
    $$

    $$
    = 2.025 \times 10^{11} + 1.96 \times 10^{12} + 1.071 \times 10^{12}
    $$

    $$
    = 0.2025 \times 10^{12} + 1.96 \times 10^{12} + 1.071 \times 10^{12} = 3.2335 \times 10^{12}
    $$

    $$
    \sigma_{\text{P\&L}} = \sqrt{3.2335 \times 10^{12}} = 1{,}798{,}194
    $$

    So the annualized P&L standard deviation is approximately **\$1,798,000** (or \$1.80M).

    **With perfect correlation ($\rho = 1$):**

    $$
    \text{Var}_{\rho=1} = (d_{2Y}\sigma_{2Y} + d_{10Y}\sigma_{10Y})^2 = (5000 \times 90 + 20000 \times 70)^2
    $$

    $$
    = (450{,}000 + 1{,}400{,}000)^2 = (1{,}850{,}000)^2 = 3.4225 \times 10^{12}
    $$

    $$
    \sigma_{\text{P\&L}}^{\rho=1} = 1{,}850{,}000 = \$1{,}850{,}000
    $$

    **Comparison:** With $\rho = 0.85$, the P&L standard deviation is \$1.80M; with $\rho = 1$, it is \$1.85M. Perfect correlation gives a **higher** P&L volatility because the two risk factors move in lockstep, amplifying the total exposure. The diversification benefit from imperfect correlation reduces the portfolio risk by approximately \$50K (about 3%). The small difference arises because both positions are long-duration (same sign), so correlation between the key rates increases rather than decreases total risk.
