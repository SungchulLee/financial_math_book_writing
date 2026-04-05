# Swaption Approximations in the LMM

Unlike caplets, which depend on a single forward rate and price exactly via Black's formula in the LMM, **swaptions** depend on multiple forward rates and their correlations. The swap rate is a weighted average of forward LIBOR rates, and under the annuity measure it is a martingale --- but it is **not lognormal** in general. This section derives the standard analytical approximations for swaption pricing within the LMM, centering on **Rebonato's formula** and its extensions.

---

## The Swaption Pricing Challenge

### Swap Rate in Terms of Forward Rates

The forward swap rate for a swap over $[T_\alpha, T_\beta]$ is

$$
S(t) = \frac{P(t, T_\alpha) - P(t, T_\beta)}{A(t)}
$$

where $A(t) = \sum_{j=\alpha+1}^{\beta} \delta_j P(t, T_j)$ is the annuity factor. Expressing bond prices in terms of forward rates:

$$
S(t) = \frac{1 - \prod_{i=\alpha}^{\beta-1}(1 + \delta_i L_i(t))^{-1}}{\sum_{j=\alpha+1}^{\beta} \delta_j \prod_{i=\alpha}^{j-1}(1 + \delta_i L_i(t))^{-1}}
$$

This is a **nonlinear function** of the forward rates $L_\alpha(t), \ldots, L_{\beta-1}(t)$.

### Why Exact Pricing Is Difficult

Under the annuity measure $\mathbb{Q}^A$, $S(t)$ is a martingale. However, since each $L_i$ is lognormal under $\mathbb{Q}^{T_{i+1}}$ and the measure changes between individual forward measures and the annuity measure introduce state-dependent drifts, the distribution of $S(T_\alpha)$ under $\mathbb{Q}^A$ is not lognormal. No closed-form swaption formula exists in the general LMM.

---

## Rebonato's Swaption Volatility Formula

### Linearization of the Swap Rate

The key approximation is to linearize $S(t)$ around $t = 0$:

$$
S(t) \approx \sum_{i=\alpha}^{\beta-1} w_i(0) \, L_i(t)
$$

where the **frozen weights** are

$$
w_i(t) = \frac{\delta_i \, P(t, T_{i+1})}{A(t)}
$$

evaluated at $t = 0$. These weights satisfy $\sum_i w_i(0) = 1$ (approximately) and represent each forward rate's contribution to the swap rate.

### Swap Rate Dynamics (Frozen Weight)

Under the annuity measure, using the linearized swap rate:

$$
dS(t) \approx \sum_{i=\alpha}^{\beta-1} w_i(0) \, dL_i(t)
$$

Since $dL_i = L_i \sigma_i \, dW_i^A + \text{drift}$, and ignoring the (small) drift corrections:

$$
dS(t) \approx \sum_{i=\alpha}^{\beta-1} w_i(0) \, L_i(t) \, \sigma_i(t) \, dW_i^A(t)
$$

### Effective Swap Rate Volatility

If $S(t)$ were exactly lognormal, its volatility $\sigma_S(t)$ would satisfy

$$
S(t) \, \sigma_S(t) \, dW^A = dS(t)
$$

Matching the quadratic variations:

$$
S(t)^2 \sigma_S(t)^2 = \sum_{i,j=\alpha}^{\beta-1} w_i(0) \, w_j(0) \, L_i(t) \, L_j(t) \, \rho_{ij} \, \sigma_i(t) \, \sigma_j(t)
$$

**Freezing** $L_i(t) \approx L_i(0)$ and $S(t) \approx S(0)$, and integrating over $[0, T_\alpha]$:

$$
\boxed{\sigma_S^2 \, T_\alpha = \sum_{i,j=\alpha}^{\beta-1} \frac{w_i(0) \, w_j(0) \, L_i(0) \, L_j(0)}{S(0)^2} \, \rho_{ij} \int_0^{T_\alpha} \sigma_i(t) \, \sigma_j(t) \, dt}
$$

This is **Rebonato's formula**. It expresses the Black swaption implied volatility $\sigma_S$ in terms of the LMM parameters: forward rate volatilities $\sigma_i(t)$, correlations $\rho_{ij}$, and initial forward rates $L_i(0)$.

### Swaption Price

With $\sigma_S$ computed from Rebonato's formula, the swaption is priced using Black's formula under the annuity measure:

$$
V_0 = A(0)\bigl[S(0) \, N(d_1) - K \, N(d_2)\bigr]
$$

$$
d_1 = \frac{\ln(S(0)/K) + \frac{1}{2}\sigma_S^2 T_\alpha}{\sigma_S\sqrt{T_\alpha}}, \qquad d_2 = d_1 - \sigma_S\sqrt{T_\alpha}
$$

---

## Analysis of Rebonato's Formula

### Sources of Approximation

Rebonato's formula involves two approximations:

1. **Frozen weights:** $w_i(t) \approx w_i(0)$ --- the annuity weights are held constant
2. **Frozen forward rates:** $L_i(t) \approx L_i(0)$ --- forward rates in the volatility formula are evaluated at time zero

Both approximations become more accurate when:

- The option expiry $T_\alpha$ is short (less time for rates to deviate from initial values)
- The volatilities are moderate
- The tenor of the underlying swap is short (fewer forward rates, so the nonlinearity is milder)

### Accuracy

Empirical studies show that Rebonato's formula is accurate to within a few basis points of volatility for typical market parameters. The approximation error increases for:

- Long-dated swaptions (large $T_\alpha$)
- High volatilities
- Deep in-the-money or out-of-the-money strikes (where the lognormal approximation is weaker)

### Decomposition of Swaption Volatility

Expanding the double sum:

$$
\sigma_S^2 T_\alpha = \underbrace{\sum_{i=\alpha}^{\beta-1} \frac{w_i^2 L_i^2}{S^2} \int_0^{T_\alpha} \sigma_i^2 \, dt}_{\text{diagonal (individual contributions)}} + \underbrace{\sum_{\substack{i,j=\alpha \\ i \neq j}}^{\beta-1} \frac{w_i w_j L_i L_j}{S^2} \rho_{ij} \int_0^{T_\alpha} \sigma_i \sigma_j \, dt}_{\text{off-diagonal (correlation contributions)}}
$$

- **Higher correlation** increases the off-diagonal terms, raising $\sigma_S$
- **Lower correlation** reduces $\sigma_S$ through diversification among forward rates

---

## Improved Approximations

### Hull--White Adjustment

Hull and White (2000) proposed keeping the weights dynamic by expanding to first order in the forward rate changes:

$$
w_i(t) \approx w_i(0) + \sum_k \frac{\partial w_i}{\partial L_k}\bigg|_0 (L_k(t) - L_k(0))
$$

This second-order correction improves accuracy for longer-dated swaptions but significantly increases computational complexity.

### Andersen--Andreasen Displaced Diffusion

Instead of a pure lognormal assumption, model the swap rate as a displaced diffusion:

$$
dS(t) = \sigma_S(S(t) + d) \, dW_t^A
$$

The displacement parameter $d$ is chosen to match the effective skew from the LMM. This provides a better approximation for out-of-the-money swaptions.

### Drift-Adjusted Approximation

Including the drift terms that were dropped in the frozen-weight approximation:

$$
\mathbb{E}^A[S(T_\alpha)] = S(0) + \text{convexity correction}
$$

The convexity correction is typically small but can matter for long-dated or deep OTM swaptions.

---

## Worked Example

??? example "Rebonato's Formula Calculation"

    **Setup:** 2Y into 3Y swaption (expiry $T_\alpha = 2$, underlying swap pays annually at $T_3 = 3, T_4 = 4, T_5 = 5$).

    **Forward rates and weights:**

    | $i$ | $L_i(0)$ | $\sigma_i$ | $w_i(0)$ | $w_i L_i / S$ |
    |---|---|---|---|---|
    | 2 | 4.5% | 22% | 0.346 | 0.369 |
    | 3 | 4.2% | 20% | 0.333 | 0.332 |
    | 4 | 4.0% | 18% | 0.321 | 0.304 |

    **Swap rate:** $S(0) = \sum w_i L_i(0) = 0.346 \times 0.045 + 0.333 \times 0.042 + 0.321 \times 0.040 = 0.04217 = 4.22\%$.

    **Correlations:** $\rho_{23} = 0.95$, $\rho_{24} = 0.88$, $\rho_{34} = 0.95$.

    **Integrated products** ($\int_0^2 \sigma_i \sigma_j \, dt = \sigma_i \sigma_j \times 2$ for constant vol):

    | $i,j$ | $w_i w_j L_i L_j / S^2$ | $\rho_{ij}$ | $\sigma_i \sigma_j \times T$ | Contribution |
    |---|---|---|---|---|
    | 2,2 | 0.136 | 1.00 | 0.0968 | 0.01317 |
    | 3,3 | 0.110 | 1.00 | 0.0800 | 0.00880 |
    | 4,4 | 0.092 | 1.00 | 0.0648 | 0.00596 |
    | 2,3 | 0.245 | 0.95 | 0.0880 | 0.02052 |
    | 2,4 | 0.224 | 0.88 | 0.0792 | 0.01562 |
    | 3,4 | 0.202 | 0.95 | 0.0720 | 0.01382 |

    **Total:** $\sigma_S^2 T = 0.01317 + 0.00880 + 0.00596 + 2(0.02052 + 0.01562 + 0.01382) = 0.12785$.

    **Swaption vol:** $\sigma_S = \sqrt{0.12785/2} = \sqrt{0.06393} = 25.3\%$.

    This swaption has a Black implied volatility of approximately 25.3%, which can be plugged into Black's formula with $A(0)$, $S(0) = 4.22\%$, and the strike $K$ to obtain the swaption price.

---

## Calibration Implications

### Joint Cap-Swaption Calibration

Rebonato's formula establishes a direct link between:

- **Caplet prices** $\to$ individual forward rate volatilities $\sigma_i$
- **Swaption prices** $\to$ correlations $\rho_{ij}$

The calibration proceeds:

1. Strip caplet volatilities from cap prices to determine $\sigma_i$
2. Use Rebonato's formula to express model swaption vols as functions of $\rho_{ij}$
3. Optimize $\rho_{ij}$ (within a parametric family) to match market swaption vols

### Model Limitations

- The approximation may produce inconsistencies when the model is calibrated to the entire swaption matrix simultaneously
- Co-terminal swaptions can be calibrated exactly, but non-co-terminal swaptions may show residual errors
- The frozen-weight assumption can fail for very long-dated swaptions

---

## Key Takeaways

- In the LMM, the swap rate is a nonlinear function of forward rates and is **not** exactly lognormal under the annuity measure
- **Rebonato's formula** provides an analytical approximation: $\sigma_S^2 T_\alpha = \sum_{i,j} (w_i w_j L_i L_j / S^2) \rho_{ij} \int \sigma_i \sigma_j \, dt$
- The formula uses two frozen approximations (weights and forward rates at time zero) and is accurate for typical market parameters
- **Higher correlation increases** swaption volatility; lower correlation reduces it
- Rebonato's formula is the primary tool for **LMM calibration to swaptions**, linking correlations to swaption prices
- Improved approximations (Hull--White, displaced diffusion, drift-adjusted) extend accuracy to long-dated and OTM swaptions

---

## Further Reading

- Rebonato (2002), *Modern Pricing of Interest-Rate Derivatives*, Chapters 8--9
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 7.4
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume II, Chapter 14
- Hull & White (2000), "Forward Rate Volatilities, Swap Rate Volatilities, and the Implementation of the LIBOR Market Model"

---

## Exercises

**Exercise 1.** Consider a 1-year into 2-year swaption in an LMM with two annual forward rates $L_0$ and $L_1$. The initial rates are $L_0(0) = 3.5\%$ and $L_1(0) = 3.8\%$, with constant volatilities $\sigma_0 = 22\%$ and $\sigma_1 = 24\%$, and correlation $\rho_{01} = 0.80$. The annuity weights are $w_0 = 0.51$ and $w_1 = 0.49$, and the forward swap rate is $S(0) = 3.65\%$. Using Rebonato's formula, compute the approximate Black swaption implied volatility.

??? success "Solution to Exercise 1"
    **Given:** $L_0(0) = 0.035$, $L_1(0) = 0.038$, $\sigma_0 = 0.22$, $\sigma_1 = 0.24$, $\rho_{01} = 0.80$, $w_0 = 0.51$, $w_1 = 0.49$, $S(0) = 0.0365$, $T_\alpha = 1$.

    Using Rebonato's formula:

    $$
    \sigma_S^2\,T_\alpha = \sum_{i,j=0}^{1}\frac{w_i\,w_j\,L_i(0)\,L_j(0)}{S(0)^2}\,\rho_{ij}\int_0^{T_\alpha}\sigma_i(t)\,\sigma_j(t)\,dt
    $$

    For constant volatilities and $T_\alpha = 1$: $\int_0^1 \sigma_i\sigma_j\,dt = \sigma_i\sigma_j$.

    Compute the normalized weights: $\tilde{w}_i = w_i L_i(0)/S(0)$:

    $$
    \tilde{w}_0 = \frac{0.51 \times 0.035}{0.0365} = \frac{0.01785}{0.0365} = 0.4890
    $$

    $$
    \tilde{w}_1 = \frac{0.49 \times 0.038}{0.0365} = \frac{0.01862}{0.0365} = 0.5101
    $$

    Now compute each term $\tilde{w}_i\,\tilde{w}_j\,\rho_{ij}\,\sigma_i\,\sigma_j$:

    **$(i,j) = (0,0)$:** $0.4890^2 \times 1.0 \times 0.22^2 = 0.2391 \times 0.0484 = 0.01157$

    **$(i,j) = (1,1)$:** $0.5101^2 \times 1.0 \times 0.24^2 = 0.2602 \times 0.0576 = 0.01499$

    **$(i,j) = (0,1)$ and $(1,0)$:** $2 \times 0.4890 \times 0.5101 \times 0.80 \times 0.22 \times 0.24 = 2 \times 0.4890 \times 0.5101 \times 0.80 \times 0.0528$

    $$
    = 2 \times 0.04989 \times 0.04224 = 2 \times 0.02107 = 0.02107
    $$

    Wait, let me recompute more carefully:

    $$
    2 \times 0.4890 \times 0.5101 \times 0.80 \times 0.0528 = 2 \times 0.4890 \times 0.5101 \times 0.04224
    $$

    $$
    = 2 \times 0.01054 = 0.02107
    $$

    **Total:** $\sigma_S^2 \times 1 = 0.01157 + 0.01499 + 0.02107 = 0.04763$

    $$
    \sigma_S = \sqrt{0.04763} = 0.2183 = 21.83\%
    $$

    The approximate Black swaption implied volatility is approximately **21.8%**.

    This is between the individual forward rate volatilities (22% and 24%) but reduced by the imperfect correlation ($\rho = 0.80 < 1$), reflecting the diversification effect.

---

**Exercise 2.** Rebonato's formula uses "frozen weights" evaluated at time 0. Explain what this approximation means and why it is necessary. For a 10-year into 10-year swaption, discuss qualitatively whether the frozen-weight approximation is more or less accurate than for a 1-year into 2-year swaption.

??? success "Solution to Exercise 2"
    **Frozen weights approximation:**

    In Rebonato's formula, the annuity weights $w_i(t) = \delta_i P(t, T_{i+1})/A(t)$ are functions of the bond prices (and hence of the forward rates) at time $t$. As the forward rates evolve stochastically, the weights change. The "frozen weights" approximation evaluates these weights at $t = 0$:

    $$
    w_i(t) \approx w_i(0)
    $$

    **Why it is necessary:** Without freezing, the swap rate dynamics $dS = \sum_i w_i\,dL_i$ involve stochastic weights, making the quadratic variation of $S$ depend on the joint evolution of weights and forward rates. This prevents a closed-form expression for the swap rate volatility. Freezing produces a linear combination with constant coefficients, yielding an analytical formula.

    **10Y into 10Y swaption vs. 1Y into 2Y swaption:**

    For the **10Y into 10Y swaption** ($T_\alpha = 10$, underlying swap with 10 annual forward rates):

    - Over 10 years, forward rates can deviate substantially from their initial values
    - The bond prices (and hence annuity weights) change significantly
    - With 10 forward rates, the nonlinearity of $S(t)$ in the $L_i(t)$ is more pronounced
    - The frozen-weight approximation is **less accurate**

    For the **1Y into 2Y swaption** ($T_\alpha = 1$, underlying swap with 2 forward rates):

    - Over 1 year, forward rates remain closer to their initial values
    - Only 2 forward rates contribute, so the nonlinearity is mild
    - The frozen-weight approximation is **more accurate**

    In general, the approximation degrades with:

    - Longer option expiry (more time for rates to move)
    - Longer underlying swap tenor (more forward rates, more nonlinearity)
    - Higher volatilities (larger deviations from initial values)

---

**Exercise 3.** Show that in the special case of a single forward rate ($n = 1$), Rebonato's formula reduces exactly to the Black caplet volatility: $\sigma_S = \sigma_0$. Verify this by substituting $w_0 = 1$ and $L_0(0) = S(0)$ into the formula.

??? success "Solution to Exercise 3"
    For a single forward rate ($\alpha = 0$, $\beta = 1$, one rate $L_0$), the swap rate is simply $S(t) = L_0(t)$ and the annuity is $A(t) = \delta_0 P(t, T_1)$.

    The weight is $w_0(t) = \delta_0 P(t, T_1)/A(t) = 1$.

    Substituting into Rebonato's formula:

    $$
    \sigma_S^2\,T_\alpha = \frac{w_0(0)^2\,L_0(0)^2}{S(0)^2}\,\rho_{00}\int_0^{T_\alpha}\sigma_0(t)^2\,dt
    $$

    With $w_0 = 1$, $L_0(0) = S(0)$, and $\rho_{00} = 1$:

    $$
    \sigma_S^2\,T_\alpha = \frac{1 \times L_0(0)^2}{L_0(0)^2} \times 1 \times \int_0^{T_0}\sigma_0(t)^2\,dt = \int_0^{T_0}\sigma_0(t)^2\,dt = v_0^2
    $$

    Therefore:

    $$
    \sigma_S = \sqrt{\frac{v_0^2}{T_0}} = \sigma_0^{\text{Black}}
    $$

    This is exactly the Black caplet volatility. In the single-rate case, the swaption is a caplet, and Rebonato's formula reduces to the exact result with no approximation error.

---

**Exercise 4.** Using the parameters from Exercise 1, compute the swaption implied volatility for two extreme correlations: $\rho_{01} = 1.0$ (perfect correlation) and $\rho_{01} = 0.0$ (zero correlation). Show that $\sigma_S$ is higher for $\rho_{01} = 1$ and lower for $\rho_{01} = 0$, and interpret this diversification effect.

??? success "Solution to Exercise 4"
    Using the same parameters as Exercise 1 except with different correlations.

    **Case 1: $\rho_{01} = 1.0$ (perfect correlation):**

    The cross term becomes:

    $$
    2 \times \tilde{w}_0\,\tilde{w}_1 \times 1.0 \times \sigma_0\sigma_1 = 2 \times 0.4890 \times 0.5101 \times 1.0 \times 0.0528 = 0.02634
    $$

    $$
    \sigma_S^2 = 0.01157 + 0.01499 + 0.02634 = 0.05290
    $$

    $$
    \sigma_S = \sqrt{0.05290} = 0.2300 = 23.00\%
    $$

    **Case 2: $\rho_{01} = 0.0$ (zero correlation):**

    The cross term vanishes:

    $$
    \sigma_S^2 = 0.01157 + 0.01499 + 0 = 0.02656
    $$

    $$
    \sigma_S = \sqrt{0.02656} = 0.1630 = 16.30\%
    $$

    **Comparison:**

    | Correlation | $\sigma_S$ |
    |---|---|
    | $\rho = 1.0$ | 23.00% |
    | $\rho = 0.8$ | 21.83% |
    | $\rho = 0.0$ | 16.30% |

    **Interpretation --- diversification effect:**

    The swap rate $S \approx w_0 L_0 + w_1 L_1$ is a weighted sum of two forward rates. When the rates are perfectly correlated ($\rho = 1$), they always move in the same direction, producing maximum swing in $S$. The swaption volatility is at its highest:

    $$
    \sigma_S \approx \tilde{w}_0\sigma_0 + \tilde{w}_1\sigma_1 = 0.4890 \times 0.22 + 0.5101 \times 0.24 = 0.1076 + 0.1224 = 0.2300
    $$

    When correlation is zero, the forward rate movements partially cancel, reducing the swap rate volatility through **diversification** --- the same effect as in portfolio theory. The swaption volatility drops by about 30% (from 23.0% to 16.3%).

---

**Exercise 5.** The Hull--White improvement to Rebonato's formula accounts for the drift of forward rates under the annuity measure. Qualitatively, explain why the frozen approximation underestimates the swaption volatility when the drift corrections are systematically positive. In what market conditions would the drift correction be most significant?

??? success "Solution to Exercise 5"
    **Qualitative explanation of the Hull--White correction:**

    In Rebonato's formula, the forward rates in the volatility expression are frozen at $L_i(0)$. Under the annuity measure, the forward rates generally have nonzero drifts. If these drifts are systematically positive (which can happen when the yield curve is steeply upward-sloping), the forward rates tend to increase over time.

    Since the swap rate volatility depends on the product $L_i(t)L_j(t)$ (through the quadratic variation), and the frozen approximation uses $L_i(0)L_j(0)$, the frozen formula **underestimates** the swaption volatility when forward rates drift upward, because:

    $$
    \mathbb{E}[L_i(t)L_j(t)] > L_i(0)L_j(0) \quad \text{(when drifts are positive)}
    $$

    **When the drift correction is most significant:**

    1. **Steep yield curve:** The forward rates at the long end are much higher than at the short end, and the annuity-measure drifts tend to be positive
    2. **High volatilities:** Larger volatilities amplify the difference between $\mathbb{E}[L_i L_j]$ and $L_i(0)L_j(0)$ through Jensen's inequality and convexity effects
    3. **Long expiry swaptions:** More time for the drift to accumulate, making the correction larger
    4. **Large number of forward rates:** More terms in the sum, each with a non-trivial drift correction

    The Hull--White improvement accounts for the first-order drift correction by expanding the weights to first order in $(L_k(t) - L_k(0))$, capturing the leading-order effect of the drift on the swaption volatility.

---

**Exercise 6.** A co-terminal swaption set consists of swaptions sharing the same final maturity $T_n$. Explain why the LMM can be calibrated exactly to a co-terminal set (one swaption at a time, working backward from the longest expiry). After exact co-terminal calibration, non-co-terminal swaptions are priced approximately. What information about the model do the residual errors on non-co-terminal swaptions reveal?

??? success "Solution to Exercise 6"
    **Co-terminal swaption calibration:**

    A co-terminal set shares the same final maturity $T_n$. For example, with $T_n = 10Y$: the 1Y$\times$9Y, 2Y$\times$8Y, 3Y$\times$7Y, ..., 9Y$\times$1Y swaptions.

    **Why exact calibration is possible:** Work backward from the longest expiry:

    1. The 9Y$\times$1Y swaption depends only on $L_{n-1}$ (a single forward rate). Its volatility determines $\sigma_{n-1}$ exactly (this is just a caplet).

    2. The 8Y$\times$2Y swaption depends on $L_{n-2}$ and $L_{n-1}$. Since $\sigma_{n-1}$ is already fixed, and the swaption formula involves $\sigma_{n-2}$ as the only unknown (with correlation $\rho_{n-2,n-1}$), we can solve for $\sigma_{n-2}$.

    3. Continue backward: the $(n-k)$Y$\times k$Y swaption, given all $\sigma_{n-1}, \ldots, \sigma_{n-k+1}$, determines $\sigma_{n-k}$.

    At each step, there is one equation (swaption vol) and one unknown (forward rate volatility), so the calibration is exact.

    **Non-co-terminal swaptions and residual errors:**

    After co-terminal calibration, the forward rate volatilities $\sigma_i$ and the correlation structure $\rho_{ij}$ are fixed. Non-co-terminal swaptions (e.g., 2Y$\times$5Y when the co-terminal set uses $T_n = 10Y$) are priced using these parameters via Rebonato's formula, but their prices are generally **not** exactly matched.

    **Residual errors reveal:**

    1. **Correlation misspecification:** If the parametric correlation model is too restrictive, the co-terminal fit is absorbed into the volatilities, but the implied correlations for non-co-terminal swaptions may be wrong
    2. **Model limitations:** The lognormal assumption and the frozen-weight approximation contribute to systematic errors
    3. **Information content:** The residual errors quantify how well a given correlation parameterization captures the full swaption surface, beyond the co-terminal slice
    4. **Market inconsistency:** In practice, some residual errors may reflect bid-ask spreads or market imperfections rather than model limitations

---

**Exercise 7.** Compare the following two approaches to pricing a 5-year into 5-year swaption in the LMM: (a) Rebonato's analytical approximation and (b) Monte Carlo simulation with 100,000 paths. For each approach, discuss the sources of error (approximation error vs. sampling error), the computational cost, and the applicability to OTM swaptions. When would you prefer one approach over the other?

??? success "Solution to Exercise 7"
    **Approach (a): Rebonato's analytical approximation**

    - **Sources of error:**
        - Frozen weights: $w_i(t) \approx w_i(0)$
        - Frozen forward rates: $L_i(t) \approx L_i(0)$ in the volatility formula
        - Lognormal assumption for the swap rate (the true distribution is not exactly lognormal)
        - Typical error: 1--5 bps of volatility for ATM swaptions, potentially more for OTM

    - **Computational cost:**
        - Computing the weights: $O(n)$
        - Computing the double sum: $O(n^2)$ where $n = 5$ forward rates
        - Total: essentially instantaneous (microseconds)

    - **OTM swaptions:** The lognormal approximation is weakest for deep OTM swaptions because:
        - The distribution tails are most sensitive to the lognormal assumption
        - The true (non-lognormal) distribution may have fatter or thinner tails
        - Skew effects from the drift corrections are ignored

    **Approach (b): Monte Carlo simulation (100,000 paths)**

    - **Sources of error:**
        - Sampling error: $\text{SE} \approx \text{std}(V)/\sqrt{N}$, where $N = 100{,}000$
        - Discretization error: from the Euler/log-Euler scheme (depends on step size)
        - Drift approximation: frozen vs. predictor--corrector
        - Typical standard error: $\sim 0.1$--$1\%$ of the option value

    - **Computational cost:**
        - Per path: $O(n^2 \times \text{steps})$ for drift computation, $O(n \times d)$ for correlated normals
        - Total: $100{,}000 \times O(n^2 \times \text{steps})$ --- several seconds to minutes
        - Variance reduction can help, but adds implementation complexity

    - **OTM swaptions:** Monte Carlo gives unbiased estimates but with very high variance for deep OTM options (since few paths end up in the money). Importance sampling is needed to get reasonable accuracy.

    **When to prefer each approach:**

    | Criterion | Rebonato | Monte Carlo |
    |---|---|---|
    | ATM European swaptions | Preferred (fast, accurate) | Overkill |
    | OTM European swaptions | Acceptable with caution | Better (with importance sampling) |
    | Calibration (many evaluations) | Preferred (speed critical) | Too slow |
    | Exotic/path-dependent | Not applicable | Required |
    | Greeks/sensitivities | Analytical differentiation | Finite differences (noisy) |
    | Model validation | Baseline comparison | Ground truth |

    In practice, Rebonato's formula is used for calibration and rapid screening, while Monte Carlo is used for final pricing of complex products and for validating the analytical approximation.
