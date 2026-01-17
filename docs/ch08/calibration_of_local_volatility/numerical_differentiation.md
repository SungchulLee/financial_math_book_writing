# Numerical Differentiation for Local Volatility

Local volatility calibration via Dupire's formula requires computing derivatives of option prices or implied volatilities with respect to strike and maturity. Since market data are discrete and noisy, numerical differentiation must be performed carefully to avoid catastrophic error amplification.

---

## The differentiation problem

Dupire's formula involves:

$$
\sigma_{\text{loc}}^2(T, K) = \frac{2 \left( \partial_T C + (r - q) K \partial_K C - q C \right)}{K^2 \partial_{KK} C}.
$$

All three derivatives ($\partial_T C$, $\partial_K C$, $\partial_{KK} C$) must be estimated from discrete, noisy data.

### Why differentiation amplifies noise

If $C^{\text{obs}}(K) = C^{\star}(K) + \varepsilon(K)$ where $\varepsilon$ is observation noise with standard deviation $\sigma_\varepsilon$, then a central difference approximation

$$
\partial_K C \approx \frac{C(K + h) - C(K - h)}{2h}
$$

has error

$$
\text{Error} \approx \frac{\sigma_\varepsilon}{h} + O(h^2).
$$

The first term (noise amplification) grows as $h \to 0$, while the second term (truncation error) shrinks. There is an optimal $h$ balancing these effects.

For second derivatives:

$$
\partial_{KK} C \approx \frac{C(K + h) - 2C(K) + C(K - h)}{h^2},
$$

with error scaling as $\sigma_\varepsilon / h^2$—much worse.

---

## Finite difference schemes

### First derivatives

**Forward difference:**
$$
\partial_K C \approx \frac{C(K + h) - C(K)}{h}, \quad \text{Error} = O(h).
$$

**Backward difference:**
$$
\partial_K C \approx \frac{C(K) - C(K - h)}{h}, \quad \text{Error} = O(h).
$$

**Central difference (preferred):**
$$
\partial_K C \approx \frac{C(K + h) - C(K - h)}{2h}, \quad \text{Error} = O(h^2).
$$

### Second derivatives

**Standard central difference:**
$$
\partial_{KK} C \approx \frac{C(K + h) - 2C(K) + C(K - h)}{h^2}, \quad \text{Error} = O(h^2).
$$

**Five-point stencil (higher accuracy):**
$$
\partial_{KK} C \approx \frac{-C(K + 2h) + 16C(K + h) - 30C(K) + 16C(K - h) - C(K - 2h)}{12h^2}, \quad \text{Error} = O(h^4).
$$

### Time derivatives

For $\partial_T C$, data are typically available at discrete maturities $T_1 < T_2 < \cdots$. Options include:

**Forward difference:**
$$
\partial_T C \approx \frac{C(K, T_{i+1}) - C(K, T_i)}{T_{i+1} - T_i}.
$$

**Central difference (if three maturities available):**
$$
\partial_T C \approx \frac{C(K, T_{i+1}) - C(K, T_{i-1})}{T_{i+1} - T_{i-1}}.
$$

In total variance coordinates $w(k, T) = T \sigma_{\text{impl}}^2(k, T)$:

$$
\partial_T w \approx \frac{w(k, T_{i+1}) - w(k, T_i)}{T_{i+1} - T_i}.
$$

---

## Richardson extrapolation

Richardson extrapolation improves accuracy by combining estimates at different step sizes.

### Principle

If an approximation $A(h)$ has error expansion

$$
A(h) = A^{\star} + c_1 h^p + c_2 h^{p+1} + \cdots,
$$

then

$$
A_{\text{extrap}} = \frac{2^p A(h/2) - A(h)}{2^p - 1}
$$

has error $O(h^{p+1})$.

### Application to second derivatives

With central differences ($p = 2$):

$$
\partial_{KK} C \approx \frac{4 D(h/2) - D(h)}{3}, \quad \text{where } D(h) = \frac{C(K+h) - 2C(K) + C(K-h)}{h^2}.
$$

This yields $O(h^4)$ accuracy from $O(h^2)$ building blocks.

### Practical limitations

Richardson extrapolation assumes smooth underlying functions. With noisy data, it can amplify errors rather than reduce them. It works best when applied to smoothed data or analytic interpolants.

---

## Spline-based differentiation

A more robust approach is to fit a smooth interpolant and differentiate analytically.

### Cubic spline interpolation

Given data $(K_i, C_i)$, fit a cubic spline $S(K)$ such that:

- $S(K_i) = C_i$ (interpolation).
- $S''$ is continuous (smoothness).
- Boundary conditions (natural, clamped, or not-a-knot).

Then compute:

$$
\partial_K C(K) = S'(K), \qquad \partial_{KK} C(K) = S''(K).
$$

### Advantages

- Derivatives are smooth and well-defined everywhere.
- No step-size selection required.
- Handles non-uniform strike spacing naturally.

### Disadvantages

- Splines can oscillate (Runge phenomenon) if data are noisy.
- No built-in arbitrage constraints.

### Smoothing splines

To handle noise, use smoothing splines that minimize

$$
\sum_i (S(K_i) - C_i)^2 + \lambda \int (S''(K))^2 \, dK,
$$

where $\lambda > 0$ controls the smoothness-fit trade-off.

---

## Differentiation in implied volatility coordinates

Market data are often given as implied volatilities. Dupire's formula can be rewritten in terms of $\sigma_{\text{impl}}(K, T)$ or total variance $w(k, T)$.

### Dupire in total variance coordinates

Let $k = \log(K/F_T)$ and $w(k, T) = T \sigma_{\text{impl}}^2(k, T)$. Then:

$$
\sigma_{\text{loc}}^2 = \frac{\partial_T w}{1 - \frac{k}{w} \partial_k w + \frac{1}{4} \left( -\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2} \right) (\partial_k w)^2 + \frac{1}{2} \partial_{kk} w}.
$$

### Advantages of total variance

- $w$ is more linear in $T$ than prices, reducing interpolation error.
- Calendar arbitrage is equivalent to $\partial_T w \ge 0$.
- Butterfly arbitrage translates to constraints on the denominator.

### Differentiation procedure

1. Convert market vols to $w(k_i, T_j)$.
2. Interpolate/smooth to a regular grid in $(k, T)$.
3. Compute $\partial_k w$, $\partial_{kk} w$, $\partial_T w$ using splines or finite differences.
4. Apply the Dupire formula.

---

## Optimal step size selection

### Theoretical optimum

For central differences with noise level $\sigma_\varepsilon$ and smooth function $C$:

**First derivative:**
$$
h^{\star} \sim \left( \frac{\sigma_\varepsilon}{|C'''|} \right)^{1/3}.
$$

**Second derivative:**
$$
h^{\star} \sim \left( \frac{\sigma_\varepsilon}{|C^{(4)}|} \right)^{1/4}.
$$

### Practical estimation

Since $C'''$ and $C^{(4)}$ are unknown:

1. **Trial and error:** Compute derivatives at multiple $h$ values; look for stability.
2. **Cross-validation:** Hold out data points; choose $h$ minimizing prediction error.
3. **Use smoothing:** Replace step-size tuning with regularization parameter tuning.

---

## Ensuring positivity of local variance

The denominator in Dupire's formula must be positive for local variance to be real and positive:

$$
K^2 \partial_{KK} C > 0 \quad \Leftrightarrow \quad \partial_{KK} C > 0.
$$

This is the butterfly arbitrage condition.

### What to do if $\partial_{KK} C \le 0$

1. **Pre-filter data:** Remove arbitrage violations before differentiation.
2. **Constrained smoothing:** Fit a convex spline.
3. **Post-adjustment:** Clip or smooth local vol where denominator is small.

A small positive floor is often applied:

$$
\partial_{KK} C \leftarrow \max(\partial_{KK} C, \epsilon),
$$

but this is a band-aid, not a solution. Proper arbitrage-free surface construction (e.g., SVI/SSVI) is preferred.

---

## Differentiation near boundaries

### Short maturities

As $T \to 0$:

- Option prices become discontinuous (digital-like).
- Implied vols can spike.
- $\partial_T C$ is poorly defined.

**Mitigation:** Exclude ultra-short maturities; use forward differences from the first available maturity.

### Extreme strikes

In the wings:

- Data are sparse; extrapolation dominates.
- $\partial_{KK} C \to 0$ (linear wings in implied vol).

**Mitigation:** Use parametric wing extrapolation (e.g., SVI); freeze local vol beyond liquid strikes.

---

## Summary: best practices

1. **Prefer analytic derivatives:** Fit a smooth functional form (spline, SVI) and differentiate analytically.

2. **Use central differences:** When numerical differentiation is unavoidable, central differences have better accuracy.

3. **Apply Richardson extrapolation cautiously:** Only on smooth, low-noise data.

4. **Work in total variance coordinates:** More stable for calendar spread handling.

5. **Check for arbitrage violations:** Ensure $\partial_{KK} C > 0$ before applying Dupire.

6. **Smooth before differentiating:** Regularization is essential; raw differentiation of noisy data fails.

7. **Validate:** Reprice vanillas from the extracted local vol surface; residuals should be small.

---

## Key takeaways

- Numerical differentiation amplifies noise, especially for second derivatives.
- Spline-based or parametric (SVI) differentiation is more stable than raw finite differences.
- Richardson extrapolation can improve accuracy but is sensitive to noise.
- Total variance coordinates simplify arbitrage checking and improve stability.
- Boundary regions (short maturity, extreme strikes) require special treatment.

---

## Further reading

- Press et al., *Numerical Recipes* (differentiation and interpolation).
- de Boor, *A Practical Guide to Splines*.
- Gatheral, *The Volatility Surface* (total variance and Dupire).
- Fengler, *Semiparametric Modeling of Implied Volatility*.
