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
