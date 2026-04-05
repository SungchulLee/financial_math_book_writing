# Numerical Differentiation for Local Volatility

Local volatility calibration via Dupire's formula requires computing derivatives of option prices or implied volatilities with respect to strike and maturity. Since market data are discrete and noisy, numerical differentiation must be performed carefully to avoid catastrophic error amplification.

---

## The differentiation problem

Dupire's formula involves:

$$
\sigma_{\text{loc}}^2(T, K) = \frac{2 \left( \partial_T C + (r - q) K \partial_K C - q C \right)}{K^2 \partial_{KK} C}
$$

All three derivatives ($\partial_T C$, $\partial_K C$, $\partial_{KK} C$) must be estimated from discrete, noisy data.

### Why differentiation amplifies noise

If $C^{\text{obs}}(K) = C^{\star}(K) + \varepsilon(K)$ where $\varepsilon$ is observation noise with standard deviation $\sigma_\varepsilon$, then a central difference approximation

$$
\partial_K C \approx \frac{C(K + h) - C(K - h)}{2h}
$$

has error

$$
\text{Error} \approx \frac{\sigma_\varepsilon}{h} + O(h^2)
$$

The first term (noise amplification) grows as $h \to 0$, while the second term (truncation error) shrinks. There is an optimal $h$ balancing these effects.

For second derivatives:

$$
\partial_{KK} C \approx \frac{C(K + h) - 2C(K) + C(K - h)}{h^2}
$$

with error scaling as $\sigma_\varepsilon / h^2$—much worse.

---

## Finite difference schemes

### First derivatives

**Forward difference:**

$$
\partial_K C \approx \frac{C(K + h) - C(K)}{h}, \quad \text{Error} = O(h)
$$

**Backward difference:**

$$
\partial_K C \approx \frac{C(K) - C(K - h)}{h}, \quad \text{Error} = O(h)
$$

**Central difference (preferred):**

$$
\partial_K C \approx \frac{C(K + h) - C(K - h)}{2h}, \quad \text{Error} = O(h^2)
$$

### Second derivatives

**Standard central difference:**

$$
\partial_{KK} C \approx \frac{C(K + h) - 2C(K) + C(K - h)}{h^2}, \quad \text{Error} = O(h^2)
$$

**Five-point stencil (higher accuracy):**

$$
\partial_{KK} C \approx \frac{-C(K + 2h) + 16C(K + h) - 30C(K) + 16C(K - h) - C(K - 2h)}{12h^2}, \quad \text{Error} = O(h^4)
$$

### Time derivatives

For $\partial_T C$, data are typically available at discrete maturities $T_1 < T_2 < \cdots$. Options include:

**Forward difference:**

$$
\partial_T C \approx \frac{C(K, T_{i+1}) - C(K, T_i)}{T_{i+1} - T_i}
$$

**Central difference (if three maturities available):**

$$
\partial_T C \approx \frac{C(K, T_{i+1}) - C(K, T_{i-1})}{T_{i+1} - T_{i-1}}
$$

In total variance coordinates $w(k, T) = T \sigma_{\text{impl}}^2(k, T)$:

$$
\partial_T w \approx \frac{w(k, T_{i+1}) - w(k, T_i)}{T_{i+1} - T_i}
$$

---

## Richardson extrapolation

Richardson extrapolation improves accuracy by combining estimates at different step sizes.

### Principle

If an approximation $A(h)$ has error expansion

$$
A(h) = A^{\star} + c_1 h^p + c_2 h^{p+1} + \cdots
$$

then

$$
A_{\text{extrap}} = \frac{2^p A(h/2) - A(h)}{2^p - 1}
$$

has error $O(h^{p+1})$.

### Application to second derivatives

With central differences ($p = 2$):

$$
\partial_{KK} C \approx \frac{4 D(h/2) - D(h)}{3}, \quad \text{where } D(h) = \frac{C(K+h) - 2C(K) + C(K-h)}{h^2}
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
\partial_K C(K) = S'(K), \qquad \partial_{KK} C(K) = S''(K)
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
\sum_i (S(K_i) - C_i)^2 + \lambda \int (S''(K))^2 \, dK
$$

where $\lambda > 0$ controls the smoothness-fit trade-off.

---

## Differentiation in implied volatility coordinates

Market data are often given as implied volatilities. Dupire's formula can be rewritten in terms of $\sigma_{\text{impl}}(K, T)$ or total variance $w(k, T)$.

### Dupire in total variance coordinates

Let $k = \log(K/F_T)$ and $w(k, T) = T \sigma_{\text{impl}}^2(k, T)$. Then:

$$
\sigma_{\text{loc}}^2 = \frac{\partial_T w}{1 - \frac{k}{w} \partial_k w + \frac{1}{4} \left( -\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2} \right) (\partial_k w)^2 + \frac{1}{2} \partial_{kk} w}
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
h^{\star} \sim \left( \frac{\sigma_\varepsilon}{|C'''|} \right)^{1/3}
$$

**Second derivative:**

$$
h^{\star} \sim \left( \frac{\sigma_\varepsilon}{|C^{(4)}|} \right)^{1/4}
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
K^2 \partial_{KK} C > 0 \quad \Leftrightarrow \quad \partial_{KK} C > 0
$$

This is the butterfly arbitrage condition.

### What to do if ∂_KK C ≤ 0

1. **Pre-filter data:** Remove arbitrage violations before differentiation.
2. **Constrained smoothing:** Fit a convex spline.
3. **Post-adjustment:** Clip or smooth local vol where denominator is small.

A small positive floor is often applied:

$$
\partial_{KK} C \leftarrow \max(\partial_{KK} C, \epsilon)
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

---

## Exercises

**Exercise 1.** For the central difference approximation to the first derivative, $\partial_K C \approx (C(K+h) - C(K-h))/(2h)$, the total error is the sum of truncation error $O(h^2)$ and noise amplification $\sigma_\varepsilon / h$. Derive the optimal step size $h^\star$ that minimizes total error, and show it satisfies

$$
h^\star = \left(\frac{3\sigma_\varepsilon}{|C'''|}\right)^{1/3}
$$

Compute $h^\star$ when $\sigma_\varepsilon = 0.01$ and $|C'''| = 0.0005$.

??? success "Solution to Exercise 1"
    The central difference approximation for the first derivative is

    $$
    \frac{C(K+h) - C(K-h)}{2h} = C'(K) + \frac{C'''(K)}{6}h^2 + O(h^4)
    $$

    by Taylor expansion. The total error has two components:

    - **Truncation error:** $E_{\text{trunc}} = \frac{|C'''|}{6}h^2$
    - **Noise amplification:** Each $C$ evaluation carries noise $\varepsilon \sim N(0, \sigma_\varepsilon^2)$, so the noise in the difference quotient has standard deviation $\frac{\sqrt{2}\,\sigma_\varepsilon}{2h} = \frac{\sigma_\varepsilon}{\sqrt{2}\,h}$. For a mean-squared-error analysis, the noise contribution is $E_{\text{noise}} \sim \frac{\sigma_\varepsilon}{h}$.

    The total error (in root-mean-square sense) is approximately

    $$
    E(h) = \frac{\sigma_\varepsilon}{h} + \frac{|C'''|}{6}h^2
    $$

    To find the optimal $h$, differentiate with respect to $h$ and set to zero:

    $$
    \frac{dE}{dh} = -\frac{\sigma_\varepsilon}{h^2} + \frac{|C'''|}{3}h = 0
    $$

    Solving:

    $$
    \frac{|C'''|}{3}h = \frac{\sigma_\varepsilon}{h^2} \implies h^3 = \frac{3\sigma_\varepsilon}{|C'''|}
    $$

    $$
    h^\star = \left(\frac{3\sigma_\varepsilon}{|C'''|}\right)^{1/3}
    $$

    **Numerical computation:** With $\sigma_\varepsilon = 0.01$ and $|C'''| = 0.0005$:

    $$
    h^\star = \left(\frac{3 \times 0.01}{0.0005}\right)^{1/3} = \left(\frac{0.03}{0.0005}\right)^{1/3} = (60)^{1/3} \approx 3.91
    $$

    So the optimal step size is approximately $h^\star \approx 3.9$. If strikes are spaced in units of currency (e.g., dollars), this suggests a spacing of about \$4 is optimal for this noise level and curvature.

---

**Exercise 2.** Show that the five-point stencil for $\partial_{KK}C$,

$$
\frac{-C(K+2h) + 16C(K+h) - 30C(K) + 16C(K-h) - C(K-2h)}{12h^2}
$$

has truncation error $O(h^4)$ by expanding each term in a Taylor series around $K$ through order $h^6$.

??? success "Solution to Exercise 2"
    We expand each term in a Taylor series around $K$. Let $f = C$ and write $f_{\pm j} = f(K \pm jh)$:

    $$
    f(K + h) = f + hf' + \frac{h^2}{2}f'' + \frac{h^3}{6}f''' + \frac{h^4}{24}f^{(4)} + \frac{h^5}{120}f^{(5)} + \frac{h^6}{720}f^{(6)} + \cdots
    $$

    $$
    f(K - h) = f - hf' + \frac{h^2}{2}f'' - \frac{h^3}{6}f''' + \frac{h^4}{24}f^{(4)} - \frac{h^5}{120}f^{(5)} + \frac{h^6}{720}f^{(6)} + \cdots
    $$

    $$
    f(K + 2h) = f + 2hf' + 2h^2 f'' + \frac{4h^3}{3}f''' + \frac{2h^4}{3}f^{(4)} + \frac{4h^5}{15}f^{(5)} + \frac{4h^6}{45}f^{(6)} + \cdots
    $$

    $$
    f(K - 2h) = f - 2hf' + 2h^2 f'' - \frac{4h^3}{3}f''' + \frac{2h^4}{3}f^{(4)} - \frac{4h^5}{15}f^{(5)} + \frac{4h^6}{45}f^{(6)} + \cdots
    $$

    Now compute the five-point stencil numerator:

    $$
    N = -f_{+2} + 16f_{+1} - 30f_0 + 16f_{-1} - f_{-2}
    $$

    **Coefficient of $f$:** $-1 + 16 - 30 + 16 - 1 = 0$. Correct (the stencil should annihilate constants).

    **Coefficient of $f'$:** $(-2 + 16 - 0 - 16 + 2)h = 0$. Correct.

    **Coefficient of $f''$:** $(-2 + 8 - 0 + 8 - 2)\frac{h^2}{1} = (-4 + 16 + 16 - 4)\frac{h^2}{2}$. Let us be more careful:

    $$
    -2h^2 + 16 \cdot \frac{h^2}{2} - 0 + 16 \cdot \frac{h^2}{2} - 2h^2 = -2h^2 + 8h^2 + 8h^2 - 2h^2 = 12h^2
    $$

    So $N = 12h^2 f'' + \text{higher order}$.

    **Coefficient of $f'''$:** $(-\frac{4}{3} + \frac{16}{6} + 0 - \frac{16}{6} + \frac{4}{3})h^3 = 0$. Correct (odd derivatives cancel by symmetry).

    **Coefficient of $f^{(4)}$:** $(-\frac{2}{3} + \frac{16}{24} + 0 + \frac{16}{24} - \frac{2}{3})h^4 = (-\frac{2}{3} + \frac{2}{3} + \frac{2}{3} - \frac{2}{3})h^4 = 0$.

    **Coefficient of $f^{(5)}$:** Zero by symmetry (odd derivative).

    **Coefficient of $f^{(6)}$:** $(-\frac{4}{45} + \frac{16}{720} + 0 + \frac{16}{720} - \frac{4}{45})\frac{h^6}{}$. Computing: $-\frac{8}{45} + \frac{32}{720} = -\frac{8}{45} + \frac{1}{22.5} = -\frac{128}{720} + \frac{32}{720} = -\frac{96}{720} = -\frac{2}{15}$. So the leading error term is $-\frac{2}{15}h^6 f^{(6)}$.

    Therefore:

    $$
    \frac{N}{12h^2} = f'' - \frac{h^4}{90}f^{(6)} + O(h^6)
    $$

    The truncation error is $O(h^4)$, confirming the claimed order of accuracy.

---

**Exercise 3.** Apply Richardson extrapolation to the central difference second derivative. Let $D(h) = (C(K+h) - 2C(K) + C(K-h))/h^2$. Show that the extrapolated estimate $(4D(h/2) - D(h))/3$ cancels the leading $O(h^2)$ error term and yields $O(h^4)$ accuracy. Verify numerically using $C(K) = K^4$ at $K = 1$ with $h = 0.1$.

??? success "Solution to Exercise 3"
    Let $D(h) = (C(K+h) - 2C(K) + C(K-h))/h^2$. By Taylor expansion:

    $$
    D(h) = C''(K) + \frac{h^2}{12}C^{(4)}(K) + \frac{h^4}{360}C^{(6)}(K) + O(h^6)
    $$

    Similarly, with step size $h/2$:

    $$
    D(h/2) = C''(K) + \frac{h^2}{48}C^{(4)}(K) + \frac{h^4}{23040}C^{(6)}(K) + O(h^6)
    $$

    The Richardson extrapolation formula with $p = 2$ is

    $$
    A_{\text{extrap}} = \frac{4D(h/2) - D(h)}{3}
    $$

    Substituting:

    $$
    4D(h/2) = 4C'' + \frac{h^2}{12}C^{(4)} + \frac{h^4}{5760}C^{(6)} + \cdots
    $$

    $$
    D(h) = C'' + \frac{h^2}{12}C^{(4)} + \frac{h^4}{360}C^{(6)} + \cdots
    $$

    $$
    4D(h/2) - D(h) = 3C'' + 0 \cdot h^2 C^{(4)} + h^4\left(\frac{1}{5760} - \frac{1}{360}\right)C^{(6)} + \cdots
    $$

    Dividing by 3:

    $$
    \frac{4D(h/2) - D(h)}{3} = C'' + O(h^4)
    $$

    The $O(h^2)$ error term has been cancelled, yielding $O(h^4)$ accuracy.

    **Numerical verification with $C(K) = K^4$ at $K = 1$, $h = 0.1$:**

    The exact second derivative is $C''(K) = 12K^2$, so $C''(1) = 12$.

    **Computing $D(0.1)$:**

    $$
    D(0.1) = \frac{(1.1)^4 - 2(1)^4 + (0.9)^4}{0.01} = \frac{1.4641 - 2 + 0.6561}{0.01} = \frac{0.1202}{0.01} = 12.02
    $$

    **Computing $D(0.05)$:**

    $$
    D(0.05) = \frac{(1.05)^4 - 2(1)^4 + (0.95)^4}{0.0025} = \frac{1.21550625 - 2 + 0.81450625}{0.0025} = \frac{0.0300125}{0.0025} = 12.005
    $$

    **Richardson extrapolation:**

    $$
    \frac{4 \times 12.005 - 12.02}{3} = \frac{48.02 - 12.02}{3} = \frac{36.0}{3} = 12.0
    $$

    The extrapolated result is exactly 12.0 (up to rounding), matching $C''(1) = 12$. This is expected because $C(K) = K^4$ has $C^{(6)} = 0$, so the $O(h^4)$ error also vanishes, and the extrapolation is exact.

---

**Exercise 4.** A smoothing spline is fit by minimizing $\sum_i (S(K_i) - C_i)^2 + \lambda \int (S''(K))^2\,dK$. Explain why the solution is a natural cubic spline for any $\lambda > 0$. Discuss the behavior of the derivatives $S'(K)$ and $S''(K)$ as $\lambda$ varies from $0$ (interpolation) to $\infty$ (linear regression). Which regime is more appropriate for Dupire calibration and why?

??? success "Solution to Exercise 4"
    **Why the solution is a natural cubic spline:** This is a classical result in approximation theory (Reinsch, 1967). Among all twice-continuously-differentiable functions $f$ satisfying the interpolation or smoothing criterion, the one that minimizes $\int (f'')^2\,dK$ is a natural cubic spline with knots at the data points.

    The proof proceeds via a variational argument. Let $S$ be the smoothing spline solution and $f$ any competing function with the same smoothness. Then

    $$
    \int (f'')^2 = \int (S'')^2 + 2\int S''(f'' - S'') + \int (f'' - S'')^2
    $$

    The cross term vanishes by integration by parts and the Euler--Lagrange conditions, leaving $\int (f'')^2 \ge \int (S'')^2$. The cubic polynomial structure on each interval arises because $S''$ is piecewise linear (the minimizer of the roughness functional subject to the smoothness constraints).

    **Behavior as $\lambda$ varies:**

    - **$\lambda = 0$ (interpolation):** $S(K_i) = C_i$ exactly. The spline passes through every data point. Derivatives $S'$ and $S''$ can oscillate wildly between data points, especially if the data are noisy. This is the Runge-phenomenon regime, and $S''$ may even change sign spuriously, violating the butterfly condition.

    - **$\lambda \to \infty$ (linear regression):** The roughness penalty dominates, forcing $S'' \to 0$ everywhere. The solution converges to the least-squares linear fit $S(K) = \alpha + \beta K$. Both $S'(K) = \beta$ (constant) and $S''(K) = 0$ everywhere. This is useless for Dupire calibration since $\partial_{KK}C = 0$ makes local variance undefined.

    - **Intermediate $\lambda$ (appropriate for Dupire):** The spline captures the genuine convexity of the call price surface while smoothing out noise. $S''(K) > 0$ is maintained (or can be enforced via constrained optimization), providing a stable, positive denominator for the Dupire formula. This regime is appropriate because:

        - The call surface is genuinely convex (by no-arbitrage), so a moderate $\lambda$ preserves this feature.
        - The local volatility surface extracted from $S''$ will be smooth and positive.
        - The trade-off between fit quality and smoothness can be optimized via cross-validation.

---

**Exercise 5.** Consider call prices at three strikes: $C(90) = 15.20$, $C(100) = 8.50$, $C(110) = 4.10$. Compute $\partial_{KK}C(100)$ using the central difference with $h = 10$. Verify that the butterfly arbitrage condition $\partial_{KK}C > 0$ holds. Now suppose a data error changes $C(100)$ to $8.80$. Recompute and check whether the arbitrage condition still holds. What does this imply for the robustness of the Dupire local volatility?

??? success "Solution to Exercise 5"
    **Original data:** $C(90) = 15.20$, $C(100) = 8.50$, $C(110) = 4.10$, $h = 10$.

    $$
    \partial_{KK}C(100) \approx \frac{C(110) - 2C(100) + C(90)}{h^2} = \frac{4.10 - 17.00 + 15.20}{100} = \frac{2.30}{100} = 0.023
    $$

    Since $0.023 > 0$, the butterfly arbitrage condition holds.

    **Perturbed data:** Now $C(100) = 8.80$:

    $$
    \partial_{KK}C(100) \approx \frac{4.10 - 2(8.80) + 15.20}{100} = \frac{4.10 - 17.60 + 15.20}{100} = \frac{1.70}{100} = 0.017
    $$

    The condition still holds ($0.017 > 0$), but the value has decreased by 26%.

    Now suppose a larger error: $C(100) = 9.70$:

    $$
    \partial_{KK}C(100) \approx \frac{4.10 - 19.40 + 15.20}{100} = \frac{-0.10}{100} = -0.001
    $$

    Now $\partial_{KK}C < 0$---the butterfly condition is violated.

    **Implications for Dupire robustness:** The local variance is proportional to $1/\partial_{KK}C$. In the original case, $\partial_{KK}C = 0.023$; with a \$0.30 perturbation in one price, it drops to $0.017$---a 26% change. With a \$1.20 perturbation, it becomes negative, making local variance undefined.

    This extreme sensitivity arises because $\partial_{KK}C$ is a *second derivative* estimated from three nearby points, where the signal (curvature) is small relative to the noise. The butterfly spread $C(K-h) - 2C(K) + C(K+h)$ is typically a small number (order of cents for reasonable strike spacing), so even modest price perturbations can flip its sign.

    This demonstrates that raw finite-difference Dupire calibration is fragile and requires smoothing or parametric fitting to be practically useful.

---

**Exercise 6.** In total variance coordinates with $w(k, T) = T\sigma_{\text{impl}}^2(k, T)$ and $k = \ln(K/F_T)$, the Dupire local variance involves $\partial_k w$, $\partial_{kk}w$, and $\partial_T w$. Suppose the implied volatility smile at one maturity is fit by the SVI parameterization $w(k) = a + b(\rho(k - m) + \sqrt{(k-m)^2 + \sigma^2})$. Compute $\partial_k w$ and $\partial_{kk}w$ analytically, and discuss why this approach avoids the noise amplification issues of finite differences.

??? success "Solution to Exercise 6"
    The SVI parameterization gives $w(k) = a + b(\rho(k - m) + \sqrt{(k-m)^2 + \sigma^2})$.

    **First derivative:** Let $u = k - m$. Then

    $$
    \partial_k w = b\left(\rho + \frac{u}{\sqrt{u^2 + \sigma^2}}\right)
    $$

    This is obtained by differentiating: $\partial_k[\rho u] = \rho$ and $\partial_k[\sqrt{u^2 + \sigma^2}] = u/\sqrt{u^2 + \sigma^2}$.

    **Second derivative:**

    $$
    \partial_{kk} w = b \cdot \frac{d}{du}\left(\frac{u}{\sqrt{u^2 + \sigma^2}}\right) = b \cdot \frac{\sqrt{u^2 + \sigma^2} - u \cdot \frac{u}{\sqrt{u^2+\sigma^2}}}{u^2 + \sigma^2}
    $$

    $$
    = b \cdot \frac{u^2 + \sigma^2 - u^2}{(u^2 + \sigma^2)^{3/2}} = \frac{b\sigma^2}{((k-m)^2 + \sigma^2)^{3/2}}
    $$

    **Why this avoids noise amplification:**

    1. **Analytic closed form:** The derivatives are computed exactly from the SVI parameters---no finite differences are needed. The only source of error is in the parameter estimation itself, not in differentiation.

    2. **Smooth by construction:** Both $\partial_k w$ and $\partial_{kk} w$ are infinitely differentiable functions of $k$, with no oscillations or sign changes (for $b > 0$, $\sigma > 0$).

    3. **Guaranteed positivity:** $\partial_{kk}w = b\sigma^2/((k-m)^2 + \sigma^2)^{3/2} > 0$ for all $k$, ensuring the Dupire denominator contributions from this term are always well-behaved. This eliminates the risk of negative local variance from butterfly violations.

    4. **Parameter stability:** SVI has only 5 parameters, which are estimated from many data points via least-squares. This built-in averaging reduces the effect of individual noisy quotes. By contrast, finite differences use only 2--3 points per derivative estimate, offering no noise averaging.

    5. **Controlled wing behavior:** As $|k - m| \to \infty$, $\partial_k w \to b(\rho \pm 1)$ (constant) and $\partial_{kk}w \to 0$. This means the local volatility wings are controlled by the parametric form rather than by extrapolation of noisy data.

---

**Exercise 7.** A practitioner applies the Dupire formula near the boundary: at the shortest maturity $T_1 = 0.02$ (about one week) and at a deep out-of-the-money strike $K = 140$ with $S_0 = 100$. Describe at least three distinct numerical difficulties that arise in each case. For each difficulty, propose a specific mitigation strategy (e.g., extrapolation method, exclusion rule, or alternative formula).

??? success "Solution to Exercise 7"
    **Difficulties at short maturity $T_1 = 0.02$ (about one week):**

    1. **Poor $\partial_T C$ estimation:** With $T_1 = 0.02$ as the shortest maturity, there is no earlier maturity available for a central difference. A forward difference $\partial_T C \approx (C(K, T_2) - C(K, T_1))/(T_2 - T_1)$ uses a large step, introducing significant truncation error. Moreover, option prices change rapidly near expiry, so the forward difference is a poor approximation to the instantaneous derivative.
        - *Mitigation:* Exclude the shortest maturity from Dupire calibration and extrapolate local vol from the second maturity using a parametric decay model. Alternatively, use the Black--Scholes theta at the shortest maturity as a proxy for $\partial_T C$.

    2. **Microstructure effects:** At one-week maturity, option prices are sensitive to discrete dividends, settlement conventions, and intraday volatility. Bid-ask spreads are often wider relative to the option price, increasing the noise-to-signal ratio.
        - *Mitigation:* Use mid-market prices averaged over a time window, apply a minimum time-to-expiry filter (e.g., exclude $T < 0.05$), and model discrete dividends explicitly.

    3. **Near-digital payoff behavior:** As $T \to 0$, the call price surface develops a kink at $K = S_0 e^{(r-q)T} \approx S_0$. The second derivative $\partial_{KK}C$ develops a spike (approaching a Dirac delta), making numerical differentiation extremely sensitive.
        - *Mitigation:* Work in implied volatility coordinates where the surface is smoother, or use SVI/SSVI parameterization which regularizes the near-expiry behavior through its parametric structure.

    **Difficulties at deep OTM strike $K = 140$ with $S_0 = 100$:**

    1. **Sparse data and wide spreads:** Deep OTM calls ($K/S_0 = 1.4$) are illiquid with wide bid-ask spreads. The option price itself is very small (close to zero), so relative noise is enormous.
        - *Mitigation:* Use put-call parity to work with the corresponding in-the-money put if it is more liquid. Apply parametric wing extrapolation (e.g., SVI wings) rather than relying on sparse OTM call quotes.

    2. **Small denominator $\partial_{KK}C$:** In the wings, the risk-neutral density is small, so $\partial_{KK}C \approx e^{-rT}q(K) \to 0$. The Dupire formula divides by this small quantity, amplifying any error in the numerator.
        - *Mitigation:* Apply a floor to $\partial_{KK}C$ (e.g., $\max(\partial_{KK}C, \epsilon)$), or freeze local volatility beyond the last liquid strike at its boundary value.

    3. **Extrapolation dominance:** If $K = 140$ is beyond the range of liquid strikes, all derivative estimates depend entirely on the extrapolation method. Different extrapolation choices (flat vol, linear vol, SVI wings) can produce dramatically different local vol values.
        - *Mitigation:* Use SVI-inspired asymptotic wing formulas that enforce Roger Lee's moment conditions: $\limsup_{k \to \infty} w(k)/k \le 2$. This constrains the wing slope and produces a finite, well-behaved local volatility in the extrapolation region.
