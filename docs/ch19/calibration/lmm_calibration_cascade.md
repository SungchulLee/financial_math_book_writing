# LMM Calibration Cascade

Calibrating the LIBOR Market Model to both caps and swaptions requires a structured, multi-stage procedure. Because caplet prices depend on individual forward rate volatilities while swaption prices also depend on inter-rate correlations, the calibration naturally decomposes into a **cascade**: first calibrate volatilities to caplets sequentially, then adjust correlations to match swaptions, iterating if necessary. This section presents the cascade algorithm in detail, analyzes the role of volatility parameterization, and discusses the re-calibration of correlations to the full swaption matrix.

---

## The Calibration Challenge in the LMM

### Parameter Count

A full-tenor LMM with $n$ forward rates $L_0, L_1, \ldots, L_{n-1}$ has:

- **Volatility functions:** $\sigma_i(t)$ for $i = 0, \ldots, n-1$, each defined on $[0, T_i]$
- **Correlation matrix:** $\rho \in \mathbb{R}^{n \times n}$ with $n(n-1)/2$ free parameters

For a 30-year quarterly model ($n = 120$), the raw parameter count exceeds 7,000 correlations alone. Parsimonious parameterization is essential.

### Separation of Concerns

The key insight enabling the cascade is that in the LMM:

- **Caplet prices depend only on individual volatilities:** The caplet on $L_i$ has price determined by $v_i^2 = \int_0^{T_i} \sigma_i(t)^2 \, dt$ alone, independent of $\rho_{ij}$
- **Swaption prices depend on both volatilities and correlations:** Via Rebonato's formula,

$$
\sigma_S^2 T_\alpha = \sum_{i,j} \frac{w_i w_j L_i(0) L_j(0)}{S(0)^2} \rho_{ij} \int_0^{T_\alpha} \sigma_i(t) \sigma_j(t) \, dt
$$

This separation makes a two-stage approach natural and efficient.

---

## Stage 1: Sequential Caplet Calibration

### Volatility Parameterization

The instantaneous volatility $\sigma_i(t)$ is typically parameterized as a function of **time to expiry** $T_i - t$:

$$
\sigma_i(t) = \phi(T_i - t; a, b, c, d)
$$

The most common form is the **abcd parameterization** (Rebonato):

$$
\phi(\tau; a, b, c, d) = (a + b\tau) e^{-c\tau} + d
$$

where $\tau = T_i - t$ is the time remaining until the forward rate fixes. The parameters have natural interpretations:

- $d$: long-run (asymptotic) volatility level
- $a + d$: instantaneous volatility at expiry ($\tau = 0$)
- $b/c$: controls the hump size
- $c$: decay rate

### The Hump Shape

The abcd parameterization produces a **humped volatility term structure**: volatility rises initially, peaks at intermediate maturities, then declines. This matches the empirical observation that 2--5 year forward rates are typically the most volatile.

The peak occurs at:

$$
\tau^* = \frac{1}{c} - \frac{a}{b}
$$

provided $b > 0$ and $a/b < 1/c$.

### Matching Caplet Volatilities

Given stripped caplet (Black) volatilities $\sigma_1^{\text{mkt}}, \sigma_2^{\text{mkt}}, \ldots, \sigma_{n-1}^{\text{mkt}}$, the model caplet volatility for $L_i$ is:

$$
(\sigma_i^{\text{model}})^2 = \frac{1}{T_i} \int_0^{T_i} \phi(T_i - t; a, b, c, d)^2 \, dt
$$

The calibration minimizes:

$$
\min_{a,b,c,d} \sum_{i=1}^{n-1} \left(\sigma_i^{\text{model}}(a,b,c,d) - \sigma_i^{\text{mkt}}\right)^2
$$

With only 4 parameters fitting many caplet vols, the fit is approximate but smooth.

### Piecewise Calibration for Exact Fit

For an exact fit to each caplet volatility, one can use **piecewise-constant instantaneous volatilities**: define $\sigma_i(t) = \lambda_{ij}$ on the interval $[T_{j-1}, T_j)$ for $j \leq i$. Then:

$$
v_i^2 = \sum_{j=1}^{i} \lambda_{ij}^2 (T_j - T_{j-1})
$$

By choosing the $\lambda_{ij}$ structure appropriately, each $v_i$ can be matched exactly.

!!! info "Cascading Volatility Matrix"
    The piecewise volatilities form a **lower-triangular matrix** $\Lambda = (\lambda_{ij})$, where row $i$ contains the volatilities for forward rate $L_i$ across time periods. This matrix is the "cascade" in the name: calibration proceeds row by row, from the shortest to the longest forward rate.

---

## The Cascade Algorithm

### Volatility Cascade

**Input:** Stripped caplet volatilities $v_1^{\text{mkt}}, v_2^{\text{mkt}}, \ldots, v_{n-1}^{\text{mkt}}$

**Output:** Volatility matrix $\Lambda = (\lambda_{ij})$

**Procedure:**

**Step 1.** For $L_1$ (the shortest forward rate, fixing at $T_1$):

$$
\lambda_{11}^2 \cdot T_1 = (v_1^{\text{mkt}})^2 \cdot T_1 \implies \lambda_{11} = v_1^{\text{mkt}}
$$

**Step 2.** For $L_2$ (fixing at $T_2$), choose $\lambda_{21}$ (volatility in $[0, T_1]$) using a structural assumption. A common choice is the **homogeneous** assumption: $\lambda_{21} = \lambda_{11}$. Then solve for $\lambda_{22}$:

$$
\lambda_{21}^2 T_1 + \lambda_{22}^2 (T_2 - T_1) = (v_2^{\text{mkt}})^2 T_2
$$

$$
\lambda_{22} = \sqrt{\frac{(v_2^{\text{mkt}})^2 T_2 - \lambda_{21}^2 T_1}{T_2 - T_1}}
$$

**Step $k$.** For $L_k$, volatilities $\lambda_{k1}, \ldots, \lambda_{k,k-1}$ are assigned from structural constraints (typically from the abcd function or homogeneity). Then:

$$
\lambda_{kk} = \sqrt{\frac{(v_k^{\text{mkt}})^2 T_k - \sum_{j=1}^{k-1}\lambda_{kj}^2(T_j - T_{j-1})}{T_k - T_{k-1}}}
$$

The cascade proceeds from $k = 1$ to $k = n-1$.

!!! warning "Positivity Check"
    The argument under the square root can become negative if the structural assumption forces too much variance into the early periods, leaving a negative residual. This signals an inconsistency between the market caplet volatilities and the chosen structural form. Resolution: relax the structural constraint or use a regularized objective.

---

## Stage 2: Swaption Re-Calibration via Correlation Fitting

### Setup

With the volatility matrix $\Lambda$ determined from Stage 1, the model swaption volatilities depend only on the correlation matrix $\rho$. Via Rebonato's formula:

$$
(\sigma_S^{\text{model}})^2 T_\alpha = \sum_{i,j=\alpha}^{\beta-1} \frac{w_i w_j L_i(0) L_j(0)}{S(0)^2} \rho_{ij} \sum_{k=1}^{k_\alpha} \lambda_{ik} \lambda_{jk} \Delta_k
$$

where $\Delta_k = T_k - T_{k-1}$ and $k_\alpha$ is the index corresponding to $T_\alpha$.

### Parametric Correlation

The correlation matrix is specified within a parametric family. Common choices:

**Exponential decay:**

$$
\rho_{ij} = e^{-\beta |T_i - T_j|}
$$

**Two-parameter with floor:**

$$
\rho_{ij} = \rho_\infty + (1 - \rho_\infty) e^{-\beta |T_i - T_j|}
$$

**Angle-based (Rebonato):**

$$
\rho_{ij} = \cos(\theta_i - \theta_j)
$$

with $\theta_i = a + bT_i + c e^{-dT_i}$.

### Optimization

The correlation parameters are calibrated to the swaption matrix:

$$
\min_{\text{corr params}} \sum_{m \in \text{swaption grid}} w_m \left(\sigma_m^{\text{model}}(\rho) - \sigma_m^{\text{mkt}}\right)^2
$$

Since this depends on the correlation parameters only (volatilities are fixed from Stage 1), the problem is low-dimensional and tractable.

---

## Worked Example: Two-Stage Cascade

??? example "Cascade Calibration for a 3-Forward-Rate LMM"

    **Setup:** Three forward rates $L_1, L_2, L_3$ with annual spacing ($T_1 = 1, T_2 = 2, T_3 = 3$).

    **Market data:**

    - Caplet vols: $v_1 = 22\%$, $v_2 = 24\%$, $v_3 = 23\%$
    - Forward rates: $L_1(0) = 4.0\%$, $L_2(0) = 4.3\%$, $L_3(0) = 4.5\%$
    - Target swaption vol (1Y into 3Y): $\sigma_S^{\text{mkt}} = 21.5\%$

    **Stage 1: Volatility cascade (homogeneous assumption)**

    Row 1: $\lambda_{11} = 22\%$

    Row 2: $\lambda_{21} = 22\%$ (homogeneous). Then:

    $\lambda_{22} = \sqrt{(0.24)^2 \times 2 - (0.22)^2 \times 1} = \sqrt{0.1152 - 0.0484} = \sqrt{0.0668} = 25.8\%$

    Row 3: $\lambda_{31} = 22\%$, $\lambda_{32} = 25.8\%$ (homogeneous). Then:

    $\lambda_{33} = \sqrt{\frac{(0.23)^2 \times 3 - (0.22)^2 \times 1 - (0.258)^2 \times 1}{1}} = \sqrt{0.1587 - 0.0484 - 0.0666} = \sqrt{0.0437} = 20.9\%$

    **Volatility matrix:**

    | | $[0,1]$ | $[1,2]$ | $[2,3]$ |
    |---|---|---|---|
    | $L_1$ | 22.0% | --- | --- |
    | $L_2$ | 22.0% | 25.8% | --- |
    | $L_3$ | 22.0% | 25.8% | 20.9% |

    **Stage 2: Correlation fitting**

    Using $\rho_{ij} = e^{-\beta|i-j|}$ and Rebonato's formula with $S(0) \approx 4.27\%$ and weights $w_1 \approx 0.34$, $w_2 \approx 0.33$, $w_3 \approx 0.33$:

    Varying $\beta$:

    - $\beta = 0$: $\sigma_S \approx 23.2\%$ (too high)
    - $\beta = 0.20$: $\sigma_S \approx 21.6\%$
    - $\beta = 0.22$: $\sigma_S \approx 21.5\%$ (match)

    **Result:** $\beta = 0.22$, giving adjacent correlations of $\rho_{12} = \rho_{23} = e^{-0.22} \approx 0.80$ and $\rho_{13} = e^{-0.44} \approx 0.64$.

---

## Iterative Refinement

### When Iteration Is Needed

The two-stage cascade assumes that changing the correlation does not affect caplet prices. This is exactly true in the LMM. However, the volatility parameterization may interact with the swaption fit:

- If the piecewise volatility structure is modified to improve the swaption fit (e.g., by adjusting the time allocation of variance), caplet vols must be re-verified
- In models where caplet and swaption pricing is coupled (e.g., short-rate models), full iteration between stages is necessary

### Convergence

The iteration typically converges in 2--3 rounds:

1. **Round 1:** Calibrate $\Lambda$ to caplets; calibrate $\rho$ to swaptions
2. **Round 2:** Adjust $\Lambda$ to improve swaption fit while preserving caplet totals; re-optimize $\rho$
3. **Round 3:** Fine-tune if residuals exceed tolerance

!!! tip "Convergence Criterion"
    Stop when the maximum absolute swaption vol error is below 1--2 bps and all caplet vols are matched within 0.5 bps.

---

## Co-Terminal Swaption Calibration

### The Co-Terminal Set

A **co-terminal** swaption set consists of swaptions that share the same final maturity $T_n$:

| Expiry | Tenor | Final Date |
|---|---|---|
| 1Y | $(n-1)$Y | $T_n$ |
| 2Y | $(n-2)$Y | $T_n$ |
| $\vdots$ | $\vdots$ | $T_n$ |
| $(n-1)$Y | 1Y | $T_n$ |

### Exact Calibration to Co-Terminals

In the LMM, the co-terminal swaption set can be calibrated **exactly** (not just approximately) by choosing the volatility structure appropriately. The key is that each co-terminal swaption's volatility can be expressed as a linear combination of volatility matrix elements, and the lower-triangular structure provides enough degrees of freedom.

The procedure:

1. Start with the longest-expiry co-terminal swaption (effectively a caplet)
2. Work backward to shorter expiries, solving for the volatility parameters in each period
3. Each step introduces one new unknown (the diagonal element $\lambda_{kk}$), which is determined by matching the co-terminal swaption price

### Non-Co-Terminal Swaptions

After exact calibration to the co-terminal set, non-co-terminal swaptions are priced approximately. The residual errors reveal the limitations of the correlation parameterization and provide diagnostics for model adequacy.

---

## Diagnostics and Quality Control

### Error Attribution

After calibration, decompose the swaption pricing error into:

- **Volatility error:** Due to the functional form of $\sigma_i(t)$
- **Correlation error:** Due to the parametric constraint on $\rho_{ij}$
- **Approximation error:** Due to Rebonato's frozen-weight approximation

### Stability Tests

- **Perturbation analysis:** Shift each market quote by 1 bp and re-calibrate. The change in parameters should be proportional to the perturbation
- **Rolling calibration:** Calibrate on consecutive dates and monitor parameter evolution. Smooth evolution indicates a stable model specification

### Common Problems and Solutions

| Problem | Symptom | Solution |
|---|---|---|
| Negative $\lambda_{kk}^2$ | Cascade fails at step $k$ | Relax homogeneity; use parametric $\sigma_i(t)$ |
| Poor swaption fit | Residual > 3 bps | Use richer correlation model (2+ parameters) |
| Unstable parameters | Large day-to-day jumps | Add regularization penalty |
| Co-terminal fit inconsistency | Cannot match all co-terminals | Increase volatility degrees of freedom |

---

## Key Takeaways

- The **LMM calibration cascade** is a two-stage procedure: first calibrate forward rate volatilities to caplets, then fit correlations to swaptions
- **Stage 1** (caplet calibration) uses the abcd parameterization or a piecewise-constant volatility matrix, proceeding sequentially from short to long maturities
- **Stage 2** (swaption calibration) optimizes a parametric correlation matrix to match the swaption volatility grid via Rebonato's formula
- The **volatility cascade** builds a lower-triangular matrix $\Lambda$ row by row, with each diagonal element determined by the residual variance constraint
- **Co-terminal swaptions** can be calibrated exactly; non-co-terminal swaptions test the adequacy of the correlation model
- Iteration between stages typically converges in 2--3 rounds
- **Diagnostics** include error attribution, perturbation analysis, and rolling calibration stability

---

## Further Reading

- Rebonato (2002), *Modern Pricing of Interest-Rate Derivatives*, Chapters 8--10
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 7
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume II, Chapter 15
- Rebonato (2004), *Volatility and Correlation*, Chapters 18--20

---

## Exercises

**Exercise 1.** Consider an LMM with four forward rates $L_1, L_2, L_3, L_4$ on an annual grid ($T_i = i$ for $i=1,\ldots,4$). The stripped caplet Black volatilities are $v_1 = 20\%$, $v_2 = 22\%$, $v_3 = 21\%$, $v_4 = 19\%$. Using the homogeneous assumption (each off-diagonal volatility in a new row equals the corresponding diagonal element of the previous row), execute the volatility cascade to compute the full lower-triangular volatility matrix $\Lambda = (\lambda_{ij})$. Check that no negative variance arises.

??? success "Solution to Exercise 1"
    **Setup:** Four forward rates on an annual grid with $T_i = i$, so $\Delta_k = T_k - T_{k-1} = 1$ for all $k$. Stripped caplet vols: $v_1 = 20\%$, $v_2 = 22\%$, $v_3 = 21\%$, $v_4 = 19\%$.

    The volatility cascade builds the lower-triangular matrix $\Lambda = (\lambda_{ij})$ row by row. The constraint for row $i$ is:

    $$
    (v_i^{\text{mkt}})^2 \cdot T_i = \sum_{j=1}^{i} \lambda_{ij}^2 \cdot \Delta_j
    $$

    With the **homogeneous assumption**, each off-diagonal entry in a new row equals the corresponding diagonal element from the previous row: $\lambda_{i,j} = \lambda_{j,j}$ for $j < i$.

    **Row 1 ($L_1$):**

    $$
    \lambda_{11}^2 \cdot 1 = (0.20)^2 \cdot 1 = 0.04 \implies \lambda_{11} = 20.0\%
    $$

    **Row 2 ($L_2$):**

    Homogeneous: $\lambda_{21} = \lambda_{11} = 20.0\%$. Solve for $\lambda_{22}$:

    $$
    \lambda_{21}^2 \cdot 1 + \lambda_{22}^2 \cdot 1 = (0.22)^2 \cdot 2 = 0.0968
    $$

    $$
    \lambda_{22}^2 = 0.0968 - (0.20)^2 = 0.0968 - 0.04 = 0.0568
    $$

    $$
    \lambda_{22} = \sqrt{0.0568} = 23.83\%
    $$

    **Row 3 ($L_3$):**

    Homogeneous: $\lambda_{31} = \lambda_{11} = 20.0\%$, $\lambda_{32} = \lambda_{22} = 23.83\%$. Solve for $\lambda_{33}$:

    $$
    (0.20)^2 + (0.2383)^2 + \lambda_{33}^2 = (0.21)^2 \cdot 3 = 0.1323
    $$

    $$
    \lambda_{33}^2 = 0.1323 - 0.04 - 0.05678 = 0.03552
    $$

    $$
    \lambda_{33} = \sqrt{0.03552} = 18.85\%
    $$

    **Row 4 ($L_4$):**

    Homogeneous: $\lambda_{41} = 20.0\%$, $\lambda_{42} = 23.83\%$, $\lambda_{43} = 18.85\%$. Solve for $\lambda_{44}$:

    $$
    (0.20)^2 + (0.2383)^2 + (0.1885)^2 + \lambda_{44}^2 = (0.19)^2 \cdot 4 = 0.1444
    $$

    $$
    \lambda_{44}^2 = 0.1444 - 0.04 - 0.05678 - 0.03553 = 0.01209
    $$

    $$
    \lambda_{44} = \sqrt{0.01209} = 10.99\%
    $$

    **Check for negative variance:** All $\lambda_{kk}^2$ values are positive: $0.04$, $0.0568$, $0.03552$, $0.01209$. No negative variance arises.

    **Full volatility matrix $\Lambda$:**

    | | $[0,1]$ | $[1,2]$ | $[2,3]$ | $[3,4]$ |
    |---|---|---|---|---|
    | $L_1$ | 20.00% | --- | --- | --- |
    | $L_2$ | 20.00% | 23.83% | --- | --- |
    | $L_3$ | 20.00% | 23.83% | 18.85% | --- |
    | $L_4$ | 20.00% | 23.83% | 18.85% | 10.99% |

    Note the diagonal volatilities: 20.00%, 23.83%, 18.85%, 10.99%. The decline in $\lambda_{44}$ reflects the fact that $v_4 = 19\%$ is the lowest caplet vol, and the homogeneous assumption forces significant variance into the early periods, leaving little residual for the final period.

---

**Exercise 2.** In the abcd volatility parameterization $\phi(\tau) = (a + b\tau)e^{-c\tau} + d$, suppose $a = 0.05$, $b = 0.12$, $c = 0.80$, and $d = 0.14$. Compute the peak maturity

$$
\tau^* = \frac{1}{c} - \frac{a}{b}
$$

and the corresponding peak volatility $\phi(\tau^*)$. Sketch the volatility as a function of $\tau$ and interpret the hump economically.

??? success "Solution to Exercise 2"
    **Peak maturity:**

    $$
    \tau^* = \frac{1}{c} - \frac{a}{b} = \frac{1}{0.80} - \frac{0.05}{0.12} = 1.25 - 0.4167 = 0.8333 \text{ years}
    $$

    **Peak volatility:**

    $$
    \phi(\tau^*) = (a + b\tau^*)e^{-c\tau^*} + d
    $$

    $$
    = (0.05 + 0.12 \times 0.8333)\,e^{-0.80 \times 0.8333} + 0.14
    $$

    $$
    = (0.05 + 0.10)\,e^{-0.6667} + 0.14
    $$

    $$
    = 0.15 \times 0.5134 + 0.14
    $$

    $$
    = 0.0770 + 0.14 = 0.2170 = 21.70\%
    $$

    **Behavior at key points:**

    - At $\tau = 0$ (at expiry): $\phi(0) = (0.05 + 0)\,e^{0} + 0.14 = 0.05 + 0.14 = 19.0\%$
    - At $\tau = \tau^* = 0.833$: $\phi(\tau^*) = 21.70\%$ (peak)
    - As $\tau \to \infty$: $\phi(\tau) \to 0 + d = 14.0\%$ (the exponential term decays to zero)

    **Sketch description:** The volatility curve starts at 19.0% for $\tau = 0$, rises to a peak of 21.70% at $\tau \approx 0.83$ years, then decays gradually toward the asymptotic level of 14.0%.

    **Economic interpretation of the hump:**

    The hump shape reflects the empirical observation that forward rates at **intermediate maturities** (roughly 1--3 years ahead) tend to be the most volatile. This occurs because:

    - **Very short-term rates** are anchored by central bank policy and change only at discrete meeting dates, limiting their variability.
    - **Intermediate rates** are driven by expectations about the future path of monetary policy, which are inherently uncertain and subject to frequent revision.
    - **Very long-term rates** are dominated by slow-moving factors like long-run inflation expectations and term premia, which change gradually.

    The parameters capture this: $d = 14\%$ is the baseline (long-run) vol level, the exponential term adds extra volatility that peaks near $\tau^* \approx 0.83$ years, and $c = 0.80$ controls how quickly the extra volatility decays with maturity.

---

**Exercise 3.** Suppose Stage 1 of the cascade has been completed and yields a $3 \times 3$ volatility matrix $\Lambda$. Three forward rates have initial values $L_1(0) = 3.5\%$, $L_2(0) = 3.8\%$, $L_3(0) = 4.0\%$ and the initial swap rate is $S(0) = 3.77\%$ with equal weights $w_i = 1/3$. Using Rebonato's swaption volatility formula with exponential correlation $\rho_{ij} = e^{-\beta|i-j|}$, derive an expression for the model swaption volatility $\sigma_S^{\text{model}}$ as an explicit function of $\beta$. Explain qualitatively why increasing $\beta$ (decreasing correlation) reduces $\sigma_S^{\text{model}}$.

??? success "Solution to Exercise 3"
    **Setup:** Three forward rates with $L_1(0) = 3.5\%$, $L_2(0) = 3.8\%$, $L_3(0) = 4.0\%$, $S(0) = 3.77\%$, equal weights $w_i = 1/3$, exponential correlation $\rho_{ij} = e^{-\beta|i-j|}$.

    Assume Stage 1 produced a $3 \times 3$ volatility matrix $\Lambda$. For a swaption with expiry $T_\alpha = T_1 = 1$ (the first period), Rebonato's formula gives:

    $$
    (\sigma_S^{\text{model}})^2 \cdot T_1 = \sum_{i,j=1}^{3}\frac{w_i w_j L_i(0) L_j(0)}{S(0)^2}\rho_{ij}\sum_{k=1}^{1}\lambda_{ik}\lambda_{jk}\Delta_k
    $$

    Since we integrate only over $[0, T_1]$ (the first period, $k=1$, $\Delta_1 = 1$):

    $$
    (\sigma_S^{\text{model}})^2 = \frac{1}{9 \cdot S(0)^2}\sum_{i,j=1}^{3}L_i(0)\,L_j(0)\,\rho_{ij}\,\lambda_{i1}\,\lambda_{j1}
    $$

    Define $A_i = L_i(0)\,\lambda_{i1}$. Then:

    $$
    (\sigma_S^{\text{model}})^2 = \frac{1}{9\,S(0)^2}\sum_{i,j=1}^{3}A_i\,A_j\,\rho_{ij}
    $$

    Expanding the double sum with $\rho_{ij} = e^{-\beta|i-j|}$:

    $$
    \sum_{i,j}A_i A_j \rho_{ij} = A_1^2 + A_2^2 + A_3^2 + 2A_1 A_2 e^{-\beta} + 2A_2 A_3 e^{-\beta} + 2A_1 A_3 e^{-2\beta}
    $$

    Therefore:

    $$
    (\sigma_S^{\text{model}})^2 = \frac{1}{9\,S(0)^2}\bigl[A_1^2 + A_2^2 + A_3^2 + 2(A_1 A_2 + A_2 A_3)e^{-\beta} + 2A_1 A_3 e^{-2\beta}\bigr]
    $$

    This is the explicit expression for the model swaption volatility as a function of $\beta$.

    **Qualitative explanation of why increasing $\beta$ reduces $\sigma_S^{\text{model}}$:**

    Increasing $\beta$ decreases the correlation $\rho_{ij} = e^{-\beta|i-j|}$ between distinct forward rates ($i \neq j$). In the formula, the cross terms $A_i A_j \rho_{ij}$ are positive (since all $A_i > 0$), and reducing $\rho_{ij}$ decreases these terms while leaving the diagonal terms $A_i^2$ unchanged. Therefore the total sum $\sum_{i,j} A_i A_j \rho_{ij}$ decreases, reducing $\sigma_S^{\text{model}}$.

    Economically, lower correlation means forward rates move more independently. When rates are imperfectly correlated, individual rate movements partially cancel in the swap rate (which is a weighted average of forward rates). This **diversification effect** reduces the variance, and hence the volatility, of the swap rate.

---

**Exercise 4.** Explain why a negative value of $\lambda_{kk}^2$ in the cascade indicates an inconsistency between the market caplet volatilities and the structural assumption used for the off-diagonal entries. Propose two concrete remedies and discuss the trade-off between exact caplet fit and parameter smoothness.

??? success "Solution to Exercise 4"
    **Why negative $\lambda_{kk}^2$ indicates inconsistency:**

    In the cascade, the diagonal volatility is determined by:

    $$
    \lambda_{kk}^2 = \frac{(v_k^{\text{mkt}})^2 T_k - \sum_{j=1}^{k-1}\lambda_{kj}^2\Delta_j}{\Delta_k}
    $$

    This is negative when:

    $$
    \sum_{j=1}^{k-1}\lambda_{kj}^2\Delta_j > (v_k^{\text{mkt}})^2 T_k
    $$

    meaning the variance assigned to the off-diagonal entries (periods before $T_{k-1}$) already **exceeds** the total variance required by the market caplet volatility $v_k^{\text{mkt}}$. The structural assumption (e.g., homogeneity: $\lambda_{kj} = \lambda_{jj}$) forces the earlier-period volatilities to be too high for forward rate $L_k$, and there is no positive residual variance left for the final period.

    This typically happens when:

    - The market caplet volatility $v_k$ is lower than previous caplet vols, but the homogeneous assumption assigns the high earlier volatilities to the new row.
    - The volatility term structure is steeply declining at maturity $T_k$.

    **Remedy 1: Relax the homogeneity assumption.**

    Instead of setting $\lambda_{kj} = \lambda_{jj}$, use a scaled version: $\lambda_{kj} = \alpha_k \cdot \lambda_{jj}$ with $\alpha_k \leq 1$. The scaling factor $\alpha_k$ is chosen so that the off-diagonal entries do not consume too much variance. Alternatively, use the abcd function: set $\lambda_{kj} = \phi(T_k - T_{j-1})$ where $\phi$ is the abcd function. Since the abcd function typically declines for large $\tau$, this naturally assigns lower volatility to the earliest periods.

    **Remedy 2: Regularized (non-exact) fit.**

    Instead of requiring an exact match to each caplet volatility, minimize:

    $$
    \sum_k (v_k^{\text{model}} - v_k^{\text{mkt}})^2 + \alpha\sum_k(\lambda_{kk} - \lambda_{k-1,k-1})^2
    $$

    The smoothness penalty prevents any single $\lambda_{kk}$ from deviating too far from its neighbor, even if this means a small caplet pricing error. This avoids the negative variance problem at the cost of an approximate (rather than exact) caplet fit.

    **Trade-off:** Exact caplet fit requires the cascade to absorb all residual variance into the diagonal element, which can produce extreme or negative values when the structural assumption is incompatible with the data. Parameter smoothness, achieved by relaxing exactness, produces more economically sensible and numerically stable volatility matrices, but introduces caplet pricing errors (typically small, 0.5--1 bp in vol terms). In practice, the slight loss of exactness is overwhelmingly preferred over the instability of exact fitting.

---

**Exercise 5.** A co-terminal swaption set with final maturity $T_5 = 5$ years contains swaptions with expiries $1\text{Y}, 2\text{Y}, 3\text{Y}, 4\text{Y}$. Explain how the cascade algorithm can be run "backward" from the longest-expiry co-terminal swaption to achieve an exact fit to all four co-terminal swaption volatilities. Why does this backward calibration produce different diagonal volatilities $\lambda_{kk}$ compared to the standard (caplet-based) forward cascade?

??? success "Solution to Exercise 5"
    **Backward calibration to co-terminal swaptions:**

    A co-terminal swaption set with final maturity $T_5 = 5$ years has swaptions with expiries 1Y, 2Y, 3Y, 4Y and tenors 4Y, 3Y, 2Y, 1Y respectively (all ending at year 5).

    The backward cascade proceeds as follows:

    **Step 1: Longest expiry (4Y into 1Y).** This swaption has expiry $T_4 = 4$ and tenor 1Y. It references a single forward rate $L_4$, so it is essentially a caplet:

    $$
    \sigma_{S}^{4Y \times 1Y} = v_4
    $$

    This determines $v_4$ (the Black caplet vol for $L_4$), from which the cascade row for $L_4$ is built.

    **Step 2: Next expiry (3Y into 2Y).** This swaption references $L_3$ and $L_4$ over the period $[0, 3]$. Since $v_4$ is known from Step 1, the swaption volatility depends on $v_3$ (or more precisely, on $\lambda_{33}$) and the correlation $\rho_{34}$. Using Rebonato's formula, solve for $\lambda_{33}$ to match the co-terminal swaption vol.

    **Step 3: Continue backward.** The 2Y into 3Y swaption involves $L_2, L_3, L_4$. With $v_3, v_4$ known, solve for the volatility parameters of $L_2$ (specifically $\lambda_{22}$). Similarly, the 1Y into 4Y swaption determines $\lambda_{11}$.

    **Why backward calibration produces different diagonal volatilities:**

    In the **standard (forward) cascade**, $\lambda_{kk}$ is determined by the caplet volatility $v_k^{\text{mkt}}$ and the structural assumption for off-diagonal entries. The caplet is the calibration target, and correlations play no role.

    In the **backward (co-terminal) cascade**, $\lambda_{kk}$ is determined by the co-terminal swaption volatility, which depends on **both** volatilities and **correlations**. The same caplet vol $v_k$ may not be matched exactly because the diagonal element is chosen to match a different instrument (the co-terminal swaption). The correlation matrix influences the swaption price, so the backward cascade implicitly incorporates correlation information into the volatility matrix.

    Concretely, if correlations are low (high decorrelation), the backward cascade needs higher individual volatilities to match a given swaption vol (since diversification reduces the aggregate vol). Conversely, if correlations are high, lower individual volatilities suffice. This means the diagonal volatilities from the backward cascade depend on the assumed correlation, whereas the forward cascade's diagonal volatilities are correlation-independent.

---

**Exercise 6.** After completing both stages of the calibration cascade, the maximum residual swaption volatility error across the full $10 \times 10$ swaption matrix is 4.5 bps, concentrated at the $7\text{Y} \times 3\text{Y}$ and $8\text{Y} \times 2\text{Y}$ swaptions. Perform an error attribution analysis: describe how you would determine whether the residual is primarily due to (a) the volatility parameterization, (b) the correlation parameterization, or (c) the frozen-weight approximation in Rebonato's formula.

??? success "Solution to Exercise 6"
    **Error attribution analysis:**

    The total swaption pricing error for each (expiry, tenor) pair is:

    $$
    \epsilon_m = \sigma_m^{\text{model}} - \sigma_m^{\text{mkt}}
    $$

    To determine the source of the residual (4.5 bps at $7\text{Y}\times 3\text{Y}$ and $8\text{Y}\times 2\text{Y}$), perform the following decomposition:

    **Test (a): Volatility parameterization.**

    Replace the parametric volatility $\sigma_i(t)$ with the "free" piecewise-constant volatility matrix that matches all caplet vols exactly, and re-evaluate the swaption prices using Rebonato's formula with the same correlation parameters. If the residual drops significantly, the volatility parameterization is the bottleneck. If the residual persists, volatility is not the issue (caplet vols are matched exactly in both cases in the standard LMM, so this mainly tests whether the time-allocation of variance within each caplet period matters).

    **Test (b): Correlation parameterization.**

    Fix the volatility matrix and replace the parametric correlation $\rho_{ij} = e^{-\beta|i-j|}$ with an **unconstrained** (but positive semi-definite) correlation matrix. Optimize each $\rho_{ij}$ freely to minimize the swaption pricing errors. If the residual drops substantially (e.g., from 4.5 bps to below 1 bp), the parametric correlation model is too restrictive and is the primary error source. The problematic swaptions ($7\text{Y}\times 3\text{Y}$ and $8\text{Y}\times 2\text{Y}$) likely require correlation levels that the exponential parameterization cannot accommodate.

    **Test (c): Frozen-weight approximation.**

    Rebonato's formula uses "frozen" (time-0) weights $w_i = \delta P(0, T_{i+1})/A(0)$, which approximates the stochastic weights in the exact swaption pricing. To test this:

    - Price the problematic swaptions using **Monte Carlo simulation** of the full LMM (with the same volatilities and correlations), which does not rely on the frozen-weight approximation.
    - Compare the Monte Carlo swaption vol with Rebonato's formula swaption vol.

    If the Monte Carlo price matches the market better (residual drops), the approximation error is significant. This is more likely for long-expiry swaptions where the drift and weight dynamics have more time to deviate from their frozen values.

    **Expected diagnosis for the $7\text{Y}\times 3\text{Y}$ and $8\text{Y}\times 2\text{Y}$ swaptions:** These are long-expiry, short-tenor swaptions. They depend primarily on the volatility of a few forward rates near maturity 7--10 years and the correlation among them. The concentration of errors at these specific cells most likely indicates that the correlation model is too rigid (test b), because short-tenor swaptions are sensitive to local correlation structure that a global exponential parameterization cannot capture.

---

**Exercise 7.** Consider a regularized cascade where the objective function adds a penalty for deviations from a smooth volatility surface:

$$
\min_{\Lambda,\, \rho\text{-params}} \sum_i \bigl(\sigma_i^{\text{model}} - \sigma_i^{\text{mkt}}\bigr)^2 + \alpha \sum_i \bigl(\lambda_{ii} - \lambda_{i-1,i-1}\bigr)^2 + \gamma \sum_m \bigl(\sigma_m^{\text{swap, model}} - \sigma_m^{\text{swap, mkt}}\bigr)^2
$$

Discuss how the regularization parameter $\alpha$ controls the trade-off between exact caplet fit and volatility smoothness. What happens in the limits $\alpha \to 0$ and $\alpha \to \infty$?

??? success "Solution to Exercise 7"
    The regularized objective function is:

    $$
    \min_{\Lambda,\,\rho} \underbrace{\sum_i (\sigma_i^{\text{model}} - \sigma_i^{\text{mkt}})^2}_{\text{caplet fit}} + \underbrace{\alpha \sum_i (\lambda_{ii} - \lambda_{i-1,i-1})^2}_{\text{volatility smoothness}} + \underbrace{\gamma \sum_m (\sigma_m^{\text{swap,model}} - \sigma_m^{\text{swap,mkt}})^2}_{\text{swaption fit}}
    $$

    **Role of $\alpha$:**

    The parameter $\alpha \geq 0$ penalizes differences between consecutive diagonal volatilities $\lambda_{ii}$ and $\lambda_{i-1,i-1}$. This enforces **smoothness** in the diagonal of the volatility matrix, preventing large oscillations between adjacent periods.

    - **Small $\alpha$:** The caplet fit term dominates. The optimizer freely adjusts each $\lambda_{ii}$ to match the corresponding caplet volatility exactly, even if this creates a jagged diagonal pattern (e.g., 20%, 28%, 15%, 25%). The result is a potentially unstable and oscillatory volatility matrix.

    - **Large $\alpha$:** The smoothness penalty dominates. The optimizer forces $\lambda_{ii} \approx \lambda_{i-1,i-1}$ for all $i$, making the diagonal nearly constant. This prevents exact caplet fitting (since different caplet vols require different diagonal elements) but produces a very smooth volatility surface.

    **Limit $\alpha \to 0$:**

    The smoothness penalty vanishes. The objective reduces to:

    $$
    \min_{\Lambda,\,\rho}\sum_i (\sigma_i^{\text{model}} - \sigma_i^{\text{mkt}})^2 + \gamma \sum_m (\sigma_m^{\text{swap,model}} - \sigma_m^{\text{swap,mkt}})^2
    $$

    This is the standard (unregularized) joint calibration. Each caplet volatility is matched as closely as possible (exact, if degrees of freedom permit), and the diagonal volatilities $\lambda_{ii}$ can take any values. The volatility matrix may be jagged and sensitive to small changes in market data.

    **Limit $\alpha \to \infty$:**

    The penalty forces $\lambda_{ii} = \lambda_{i-1,i-1}$ for all $i$, i.e., a **constant diagonal**: $\lambda_{11} = \lambda_{22} = \cdots = \lambda_{nn} = \bar{\lambda}$. The single parameter $\bar{\lambda}$ is chosen to best fit the caplet volatilities in a least-squares sense, resulting in $\bar{\lambda} \approx \bar{v}$ (a weighted average of market caplet vols). Individual caplet vols cannot be matched unless they are all equal. The model collapses to a highly constrained version that is very smooth but fits the data poorly --- this is **underfitting**.

    **Practical choice of $\alpha$:** Increase $\alpha$ from 0 until the caplet pricing errors are at the level of market bid-ask noise (typically 0.5--1 bp in vol). This gives the smoothest volatility matrix consistent with the data quality, avoiding both overfitting (oscillatory $\Lambda$) and underfitting (constant diagonal).
