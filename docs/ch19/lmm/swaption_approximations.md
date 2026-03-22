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
