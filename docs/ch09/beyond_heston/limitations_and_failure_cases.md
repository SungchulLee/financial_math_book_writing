# Limitations and When the COS Method Fails

The COS method delivers exponential convergence for a broad class of models, but it is not infallible. Certain characteristic functions, density shapes, and parameter regimes expose structural weaknesses in the cosine expansion, leading to slow convergence, oscillatory errors, or outright failure. Understanding these limitations is essential for practitioners who must decide when to trust the COS price and when to reach for an alternative method. This section catalogs the principal failure modes, explains their mathematical origins, and presents practical remedies.

!!! info "Prerequisites"

    - [COS Pricing Formula](../cos_method/cos_pricing_formula.md) (cosine expansion and convergence)
    - [Error Analysis and Convergence](../cos_method/error_analysis_and_convergence.md) (truncation and series error)
    - [COS for Other Affine Models](cos_for_other_affine_models.md) (model-specific CFs)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Identify the smoothness, decay, and analyticity conditions that guarantee exponential COS convergence
    2. Explain why heavy-tailed densities degrade COS performance and how to widen the truncation interval
    3. Diagnose oscillatory characteristic functions and their impact on the cosine coefficients
    4. Recognize models with insufficient density smoothness and predict the resulting algebraic convergence rate
    5. Apply practical remedies including filtering, adaptive truncation, and alternative quadrature

---

## Conditions for Exponential Convergence

The COS method approximates the risk-neutral density $f(x)$ on a truncated interval $[a, b]$ using a cosine series:

$$
f(x) \approx \sum_{k=0}^{N-1}{}' A_k \cos\!\left(k\pi\frac{x - a}{b - a}\right)
$$

where the coefficients $A_k$ are recovered from the characteristic function $\phi(u)$. Exponential convergence --- the property that the error decreases as $e^{-cN}$ for some $c > 0$ --- requires three conditions:

1. **Smoothness**: The density $f$ must be infinitely differentiable ($C^\infty$) on $[a, b]$.
2. **Analyticity**: For exponential (rather than merely superalgebraic) convergence, $f$ must extend to an analytic function in a strip around the real axis.
3. **Rapid decay**: The density must decay fast enough that truncation from $\mathbb{R}$ to $[a, b]$ introduces negligible error.

When any of these conditions is violated, convergence degrades. The following sections examine each failure mode in detail.

---

## Failure Mode 1: Heavy Tails and Truncation Error

### The Problem

The COS method replaces the infinite integration domain $\mathbb{R}$ with a finite interval $[a, b]$. The truncation error is:

$$
\epsilon_{\text{trunc}} = \int_{-\infty}^a f(x)\,dx + \int_b^{\infty} f(x)\,dx
$$

For densities with exponential tails (e.g., Heston, VG, NIG), the cumulant-based rule $[a, b] = [c_1 - L\sqrt{c_2}, \; c_1 + L\sqrt{c_2}]$ with $L = 10$--$12$ produces truncation error below $10^{-10}$.

For densities with **polynomial tails** --- where $f(x) \sim |x|^{-(1+\alpha)}$ for some $\alpha > 0$ --- the truncation error decays only as a power of $(b - a)$:

$$
\epsilon_{\text{trunc}} = O\!\left((b - a)^{-\alpha}\right)
$$

This forces much wider intervals, which in turn require more cosine terms to maintain resolution.

### Which Models Are Affected

| Model | Tail behavior | Truncation difficulty |
|---|---|---|
| Heston | Exponential tails | Low (standard $L$ works) |
| VG | Exponential tails | Low to moderate |
| CGMY ($Y < 1$) | Exponential tails | Moderate |
| CGMY ($Y \geq 1$) | Semi-heavy tails | High |
| Stable processes ($\alpha < 2$) | Polynomial tails | Very high |
| Student-$t$ mixture models | Polynomial tails | Very high |

### Diagnosis

Slow convergence that improves when $[a, b]$ is widened (but not when $N$ is increased) indicates a truncation error problem. The characteristic function often provides a direct diagnostic: if $|\phi(u)|$ decays as a power law $|u|^{-\gamma}$ rather than exponentially, the density has heavy tails.

!!! warning "Cumulant-Based Truncation Can Fail"
    The standard cumulant formula assumes that the fourth cumulant $c_4$ captures the tail behavior. For distributions where $c_4$ is infinite (e.g., stable distributions with $\alpha < 4$), the cumulant rule underestimates the required interval width. In such cases, use quantile-based truncation: choose $a$ and $b$ so that $F(a) < \epsilon$ and $1 - F(b) < \epsilon$, estimating the quantiles from the CF via numerical inversion.

### Remedy

1. **Wider truncation**: Increase $L$ from 10--12 to 20--30 (or use quantile-based bounds).
2. **Adaptive truncation**: Start with a moderate $[a, b]$, compute the COS price, widen by 20%, recompute, and check convergence.
3. **Tail correction**: Approximate the tail integral analytically using the asymptotic form of $f(x)$ and add it to the COS price.

---

## Failure Mode 2: Slow Characteristic Function Decay

### The Problem

**Recall** (see [§ Cosine Series Coefficients via CF](../cos_method/cosine_coefficients_via_cf.md)): the COS density coefficients are $A_k = \frac{2}{b-a}\operatorname{Re}[\phi(k\pi/(b-a))\,e^{-ik\pi a/(b-a)}]$.

The convergence rate of the cosine series depends on how fast $|A_k|$ decays as $k \to \infty$, which in turn depends on how fast $|\phi(u)|$ decays as $|u| \to \infty$.

**If $|\phi(u)|$ decays exponentially** (i.e., $|\phi(u)| \leq C e^{-\delta|u|}$ for some $\delta > 0$), then $|A_k|$ decays exponentially and the COS series converges exponentially.

**If $|\phi(u)|$ decays only as a power law** ($|\phi(u)| \sim |u|^{-\gamma}$), then $|A_k| \sim k^{-\gamma}$ and the COS series converges only algebraically:

$$
\left|V_{\text{exact}} - V_{\text{COS}}(N)\right| = O(N^{-\gamma+1})
$$

### Which Models Are Affected

The decay rate of $|\phi(u)|$ is directly related to the smoothness of the density. By the Paley-Wiener theorem:

- $f \in C^\infty$ and compactly supported $\Rightarrow$ $|\phi(u)|$ decays faster than any polynomial
- $f$ is analytic in a strip of width $\delta$ $\Rightarrow$ $|\phi(u)| = O(e^{-\delta|u|})$
- $f$ has $p$ derivatives but $f^{(p)}$ has a jump $\Rightarrow$ $|\phi(u)| = O(|u|^{-(p+1)})$

Most financial models produce smooth densities, but certain parameter regimes create problems:

| Scenario | CF decay | COS convergence |
|---|---|---|
| CGMY with $Y \to 2$ | Slow power law | Algebraic |
| Merton jumps with very high $\lambda$ | Oscillatory with slow envelope | Slow |
| Near-degenerate Heston ($\xi \to 0$) | Nearly Gaussian but very peaked | Needs high $N$ |
| Models with atomic components | No decay | Series does not converge |

---

## Failure Mode 3: Oscillatory Characteristic Functions

### The Problem

Some characteristic functions oscillate rapidly as $|u|$ grows, causing the cosine coefficients $A_k$ to fluctuate in sign and magnitude rather than decaying monotonically. This leads to **Gibbs-like phenomena** in the recovered density and cancellation errors in the price.

### Mathematical Mechanism

Consider a density that is a mixture of a smooth component and a translated component:

$$
f(x) = (1 - p)\,f_0(x) + p\,f_0(x - \mu)
$$

The characteristic function is $\phi(u) = (1 - p)\phi_0(u) + p\,e^{iu\mu}\phi_0(u)$, which contains the oscillatory factor $e^{iu\mu}$. If $\mu$ is large relative to $(b - a)$, the oscillation frequency $\mu/(b - a)$ interacts with the cosine frequencies $k\pi/(b - a)$, creating aliasing.

Jump models are the primary source of oscillatory CFs. The Merton jump component contributes:

$$
\phi_{\text{jump}}(u) = \exp\!\left(\lambda T\left[e^{i\mu_J u - \sigma_J^2 u^2/2} - 1\right]\right)
$$

When $\lambda T$ is large (many expected jumps) and $\sigma_J$ is small (concentrated jump sizes), the CF oscillates rapidly with a slowly decaying envelope.

### Diagnosis

Plot $|\phi(u)|$ and $\operatorname{Re}[\phi(u)]$ as functions of $u$. Rapid oscillation with a non-monotone envelope signals trouble. Alternatively, monitor the COS price as $N$ increases: non-monotone convergence (the error oscillates rather than decreasing steadily) indicates oscillatory CF interference.

### Remedy

1. **Increase $N$ substantially**: Match the Nyquist condition $N > 2\mu/(b-a) \cdot T$ to resolve the oscillation.
2. **Damping / exponential tilting**: Replace $\phi(u)$ by $\phi(u + i\eta)$ for a suitable $\eta > 0$ (equivalent to pricing under an exponentially tilted measure). This damps the oscillations at the cost of modifying the payoff coefficients.
3. **Fractional FFT**: When the COS method struggles, the fractional FFT (Chourdakis, 2005) or the Carr-Madan FFT approach may be more robust because they integrate $\phi$ against a damped kernel.

---

## Failure Mode 4: Insufficient Density Smoothness

### The Problem

The COS method achieves exponential convergence only when the density $f(x)$ is smooth (ideally analytic) on $[a, b]$. If $f$ has a kink, jump, or is only finitely differentiable, the cosine coefficients $A_k$ decay at an algebraic rate determined by the order of the singularity.

!!! info "Theorem (Algebraic Convergence for Non-Smooth Densities)"
    If the density $f$ has $p$ continuous derivatives on $[a, b]$ but $f^{(p)}$ has a discontinuity, then the cosine coefficients satisfy $|A_k| = O(k^{-(p+1)})$ and the COS pricing error is $O(N^{-p})$.

### When Does This Occur?

Most standard models (Heston, VG, NIG, CGMY with $Y < 2$) produce $C^\infty$ densities. Insufficient smoothness arises in:

1. **Barrier and digital options**: The payoff function itself has a discontinuity. Although the density may be smooth, the product $f(x) \cdot g(x)$ (where $g$ is the payoff) inherits the payoff's kink. The COS payoff coefficients $V_k$ then decay slowly.

2. **Models with atoms**: If the risk-neutral distribution places a point mass at a specific value (e.g., the default-adjusted stock price in Merton's structural model), the density contains a Dirac delta, and the cosine expansion cannot converge.

3. **Numerical CFs**: When the characteristic function is obtained by numerically solving an ODE (e.g., time-changed models without closed-form CF), rounding errors can introduce effective roughness in $\phi(u)$ at large $|u|$, contaminating the high-frequency coefficients.

### Remedy

1. **Payoff smoothing**: Replace the discontinuous payoff with a smoothed version (e.g., replace the indicator $\mathbf{1}_{\{x > \ln K\}}$ with a logistic approximation).
2. **Richardson extrapolation**: Compute COS prices at $N$ and $2N$, then extrapolate to reduce the leading error term.
3. **Hybrid methods**: Use COS for the smooth density part and handle the singular part (atoms, barriers) separately via exact formulas.

---

## Failure Mode 5: Numerical Instability in the Characteristic Function

### The Problem

Even when the analytical CF is well-behaved, its numerical evaluation can introduce errors that propagate into the COS price.

### Common Sources

**Branch-cut discontinuities in the Heston CF.** Recall (see [§ Numerical Stability and Branch Cuts](../../ch16/heston_cf/numerical_stability_and_branch_cuts.md)): the Heston CF involves a complex square root whose principal-branch cut can be crossed by $u$, producing a discontinuous $\phi(u)$ that destroys COS convergence; the "little Heston trap" rotation (Albrecher et al., 2007) eliminates this.

**Overflow/underflow in exponentials.** For large $|u|$ or long maturities $T$, the exponential terms $e^{-\gamma T}$ in the Heston CF can overflow or underflow, producing NaN or zero values in the cosine coefficients.

**Cancellation in near-degenerate regimes.** When $\xi \to 0$ (deterministic volatility limit) or $\kappa \to \infty$ (instantaneous mean reversion), the CF approaches a simpler limiting form, but the general formula involves differences of nearly equal large numbers, causing catastrophic cancellation.

### Remedy

1. **Use the "little Heston trap" formulation** (Albrecher et al., 2007) to avoid branch-cut discontinuities.
2. **Log-sum-exp tricks**: Compute $\ln\phi(u)$ instead of $\phi(u)$ and exponentiate only at the final step.
3. **Asymptotic expansions**: In degenerate parameter regimes, switch to the appropriate limiting formula (e.g., Black-Scholes CF when $\xi = 0$).
4. **Extended precision**: Use 128-bit floating point for the CF evaluation when standard double precision is insufficient.

---

## Diagnostic Checklist

Before trusting a COS price, verify the following.

| Check | Method | Action if failed |
|---|---|---|
| CF evaluates without NaN | Evaluate $\phi(u)$ at $u = 0, 10, 100, 1000$ | Fix branch cuts, overflow |
| $\|\phi(u)\|$ decays for large $u$ | Plot $\|\phi(u)\|$ vs $u$ | If power-law decay, increase $N$ |
| Price converges as $N$ increases | Compute at $N = 64, 128, 256, 512$ | If oscillating, check oscillatory CF |
| Price stable under $[a,b]$ widening | Widen by 20% and recompute | If changes, increase $L$ |
| Density non-negative | Evaluate $f_{\text{COS}}(x)$ on a grid | If negative, increase $N$ or smooth |
| Put-call parity satisfied | Check $C - P = e^{-qT}S_0 - e^{-rT}K$ | If violated, review truncation |

---

## Comparison with Alternative Methods

When COS fails, several alternative Fourier pricing methods may succeed.

| Method | Strengths | Weaknesses |
|---|---|---|
| COS | Fastest for smooth CFs, exponential convergence | Sensitive to truncation, smoothness |
| Carr-Madan FFT | Robust damping kernel, handles oscillatory CFs | $O(N\log N)$ cost, grid constraints |
| Fractional FFT | Flexible strike grid | More complex implementation |
| Lewis (2001) saddle-point | Good for heavy tails | Requires analyticity strip analysis |
| Direct numerical integration | Most robust | Slowest, $O(N)$ per strike |

!!! tip "Practical Decision Rule"
    Start with COS ($N = 128$). If the convergence check passes (price stable at $N = 256$), use COS. If convergence is slow or erratic, switch to Carr-Madan FFT with damping parameter $\alpha = 1.5$. For models with atoms or extreme tails, use direct numerical integration as the baseline.

---

## Worked Example: COS Failure for CGMY with Y near 2

!!! example "CGMY with $Y = 1.8$"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.05$, $T = 0.25$, $C = 1$, $G = 5$, $M = 10$, $Y = 1.8$.

    The density has semi-heavy tails and the CF decays as $|\phi(u)| \sim \exp(-c|u|^Y)$ with $Y = 1.8 < 2$, which is slower than Gaussian decay.

    | $N$ | COS price | Error vs benchmark |
    |:---:|:---------:|:------------------:|
    | 64 | 5.8412 | $2.1 \times 10^{-1}$ |
    | 128 | 5.6501 | $1.8 \times 10^{-2}$ |
    | 256 | 5.6338 | $1.5 \times 10^{-3}$ |
    | 512 | 5.6324 | $1.2 \times 10^{-4}$ |
    | 1024 | 5.6323 | $9.8 \times 10^{-6}$ |

    The convergence is algebraic (roughly $O(N^{-2.4})$) rather than exponential. With $L = 10$, the truncation interval is too narrow; increasing to $L = 20$ and using $N = 512$ achieves $10^{-5}$ accuracy.

    For comparison, the same model with $Y = 0.5$ achieves $10^{-8}$ accuracy with $N = 128$ and $L = 10$.

---

## Summary

The COS method fails or degrades when its three foundational assumptions are violated: smooth density, rapidly decaying CF, and adequate truncation interval. Heavy-tailed distributions require wider truncation and more terms. Oscillatory characteristic functions (from concentrated jumps) create aliasing that demands either very high $N$ or exponential tilting. Densities with finite smoothness (from barriers, atoms, or numerical CFs) produce algebraic rather than exponential convergence. Numerical instabilities in CF evaluation (branch cuts, overflow, cancellation) can be addressed by careful implementation choices. A systematic diagnostic checklist --- checking CF evaluation, convergence in $N$, stability under truncation widening, and put-call parity --- identifies the failure mode and guides the choice of remedy. When COS cannot be made to work, the Carr-Madan FFT with damping or direct numerical integration provides a robust fallback.

---

## Further Reading

- Fang, F. and Oosterlee, C. W. (2008). "A novel pricing method for European options based on Fourier-cosine series expansions." *SIAM Journal on Scientific Computing*, 31(2), 826--848.
- Carr, P. and Madan, D. (1999). "Option valuation using the fast Fourier transform." *Journal of Computational Finance*, 2(4), 61--73.
- Albrecher, H., Mayer, P., Schoutens, W., and Tistaert, J. (2007). "The little Heston trap." *Wilmott Magazine*, January, 83--92.
- Lord, R. and Kahl, C. (2010). "Complex logarithms in Heston-like models." *Mathematical Finance*, 20(4), 671--694.

---

## Exercises

**Exercise 1.** The COS method requires three conditions for exponential convergence: smoothness of the density, rapid decay of the CF, and adequate truncation. For a model where the density has a kink (e.g., a barrier option density), which condition is violated? What is the resulting convergence rate, and how many COS terms would be needed for $10^{-4}$ accuracy if $|A_k| = O(k^{-2})$?

??? success "Solution to Exercise 1"
    The smoothness condition is violated. A barrier option density (or more precisely, the product of the density with the barrier payoff) has a **kink** (discontinuity in the first derivative) at the barrier level. This means the function being expanded in a cosine series is not $C^\infty$; it has only $p = 1$ continuous derivatives (continuous but with a discontinuous first derivative).

    By the algebraic convergence theorem, if $f$ has $p$ continuous derivatives but $f^{(p)}$ has a discontinuity, then $|A_k| = O(k^{-(p+1)})$ and the COS pricing error is $O(N^{-p})$.

    For a kink ($p = 1$): $|A_k| = O(k^{-2})$, so the COS series error is $O(N^{-1})$.

    To achieve $10^{-4}$ accuracy with $|A_k| = O(k^{-2})$, we need the truncation error of the series to satisfy:

    $$
    \sum_{k=N}^{\infty} |A_k| \approx \int_N^{\infty} k^{-2}\,dk = \frac{1}{N} < 10^{-4}
    $$

    This requires $N > 10^4 = 10{,}000$ terms. This is far more than the 64--256 terms typical for smooth densities, illustrating why payoff discontinuities severely degrade COS performance. In practice, payoff smoothing or Richardson extrapolation is essential.

---

**Exercise 2.** For the CGMY model with $Y = 1.8$, the worked example shows algebraic convergence: $N = 64$ gives error $\approx 0.21$, while $N = 512$ gives error $\approx 1.2 \times 10^{-4}$. Estimate the convergence order $p$ in $\varepsilon \sim N^{-p}$ by fitting $\log(\varepsilon)$ vs $\log(N)$ using two data points. Compare this to the exponential convergence for CGMY with $Y = 0.5$.

??? success "Solution to Exercise 2"
    Using the data points $(N_1, \varepsilon_1) = (64, 0.21)$ and $(N_2, \varepsilon_2) = (512, 1.2 \times 10^{-4})$:

    The model is $\varepsilon \sim C N^{-p}$, so $\log \varepsilon = \log C - p\log N$.

    $$
    p = \frac{\log \varepsilon_1 - \log \varepsilon_2}{\log N_2 - \log N_1} = \frac{\log(0.21) - \log(1.2 \times 10^{-4})}{\log 512 - \log 64}
    $$

    Computing the numerator:

    $$
    \log(0.21) - \log(1.2 \times 10^{-4}) = \log\!\left(\frac{0.21}{1.2 \times 10^{-4}}\right) = \log(1750) \approx 3.2430
    $$

    Computing the denominator:

    $$
    \log 512 - \log 64 = \log(512/64) = \log 8 \approx 0.9031
    $$

    Therefore:

    $$
    p \approx \frac{3.2430}{0.9031} \approx 3.59
    $$

    So the convergence is approximately $O(N^{-3.6})$, which is algebraic (polynomial) convergence.

    **Comparison with $Y = 0.5$:** The text states that CGMY with $Y = 0.5$ achieves $10^{-8}$ accuracy with $N = 128$ and $L = 10$. This is exponential convergence: the error decreases as $e^{-cN}$ for some $c > 0$. With exponential convergence, doubling $N$ from 64 to 128 typically reduces the error by many orders of magnitude simultaneously (e.g., from $10^{-4}$ to $10^{-8}$). In contrast, the algebraic convergence for $Y = 1.8$ requires going from $N = 64$ all the way to $N = 1024$ just to get from error $0.21$ to error $10^{-5}$---a reduction that exponential convergence would achieve with far fewer terms.

---

**Exercise 3.** The Heston characteristic function involves $\gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}$. Explain why the principal branch of the complex square root can produce a discontinuous $\phi(u)$ along the real $u$-axis. Describe the "little Heston trap" fix (Albrecher et al., 2007) and why it resolves the branch-cut problem.

??? success "Solution to Exercise 3"
    The Heston CF involves $\gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}$, where the argument of the square root is a complex-valued function of the real variable $u$.

    **Why a discontinuity arises:** As $u$ varies continuously along the real axis, the complex argument $z(u) = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)$ traces a curve in the complex plane. The principal branch of $\sqrt{z}$ has a branch cut along the negative real axis ($\arg z = \pm\pi$). If $z(u)$ crosses the negative real axis as $u$ varies, $\arg(z)$ jumps from $+\pi$ to $-\pi$ (or vice versa), causing $\sqrt{z}$ to jump discontinuously. This discontinuity in $\gamma(u)$ propagates to $\phi(u)$, producing a discontinuous characteristic function. Since the COS coefficients $F_k = \frac{2}{b-a}\operatorname{Re}[\phi(k\pi/(b-a))\cdots]$ sample $\phi$ at discrete points, a discontinuity in $\phi$ destroys the exponential decay of $|F_k|$ and hence the exponential convergence of the COS method.

    **The "little Heston trap" fix:** Albrecher et al. (2007) observe that the Heston CF can be written in two mathematically equivalent forms. The standard form uses:

    $$
    g = \frac{\kappa - i\rho\sigma_v u - \gamma}{\kappa - i\rho\sigma_v u + \gamma}
    $$

    The "little Heston trap" formulation uses $g^* = 1/g$:

    $$
    g^* = \frac{\kappa - i\rho\sigma_v u + \gamma}{\kappa - i\rho\sigma_v u - \gamma}
    $$

    and rearranges the CF formula so that the exponential terms involve $(1 - g^* e^{-\gamma T})$ instead of $(1 - ge^{-\gamma T})$. The key insight is that $|g^*| > 1$ (while $|g| < 1$), so $g^* e^{-\gamma T}$ is better behaved numerically, and the overall expression avoids the branch-cut crossing. Specifically, the reformulation ensures that the complex argument of the logarithm/exponential in the CF never crosses the branch cut, making $\phi(u)$ continuous along the real $u$-axis.

    **Resolution:** By using the little Heston trap formulation, $\phi(u)$ is continuous and smooth in $u$, restoring exponential convergence of the COS method.

---

**Exercise 4.** Heavy-tailed distributions (e.g., stable processes with polynomial tails) cause the cumulant-based truncation rule to fail because $c_4$ may be infinite. Propose a quantile-based truncation rule as an alternative: given a target truncation error $\epsilon$, describe how to find $a$ and $b$ such that $F(a) < \epsilon$ and $1 - F(b) < \epsilon$ using the Gil-Pelaez formula for the CDF.

??? success "Solution to Exercise 4"
    For heavy-tailed distributions where $c_4$ may be infinite (e.g., stable processes with index $\alpha < 4$), the cumulant-based truncation formula breaks down. We propose using the Gil-Pelaez inversion formula to find quantile-based bounds.

    **Gil-Pelaez formula for the CDF:**

    $$
    F(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty}\operatorname{Im}\!\left[\frac{e^{-iux}\phi(u)}{u}\right]du
    $$

    **Quantile-based truncation algorithm:**

    1. Choose a target truncation error $\epsilon$ (e.g., $\epsilon = 10^{-10}$).
    2. Find $a$ such that $F(a) < \epsilon$: use bisection on $x$ with $F(x)$ evaluated via the Gil-Pelaez integral. Start with $a_0 = c_1 - 10\sqrt{c_2}$ (if $c_2$ exists) or a rough initial guess, and halve/double until $F(a) < \epsilon$.
    3. Find $b$ such that $1 - F(b) < \epsilon$: similarly, use bisection to find $b$ with $F(b) > 1 - \epsilon$.

    **Practical considerations:**

    - The Gil-Pelaez integral itself requires numerical quadrature, but it only needs to be evaluated at a few candidate values of $x$ during the bisection, so the cost is modest.
    - For the integrand $\operatorname{Im}[e^{-iux}\phi(u)/u]$, the decay rate as $u \to \infty$ is governed by $|\phi(u)|$. For heavy-tailed densities, $|\phi(u)|$ decays slowly, so the integral may need a large upper limit or adaptive quadrature.
    - An alternative is to use the tail asymptotics: if $f(x) \sim C|x|^{-(1+\alpha)}$ for large $|x|$, then $F(a) \approx C|a|^{-\alpha}/\alpha$ and $1 - F(b) \approx C b^{-\alpha}/\alpha$, giving $a \approx -(C/(\alpha\epsilon))^{1/\alpha}$ and $b \approx (C/(\alpha\epsilon))^{1/\alpha}$. This provides a direct formula when the tail index $\alpha$ is known.

    This approach guarantees that the truncation error is below $\epsilon$ regardless of whether the cumulants exist, making it universally applicable.

---

**Exercise 5.** Oscillatory characteristic functions arise in jump-diffusion models with concentrated jumps ($\sigma_J$ small). For the Merton model with $\lambda = 10$, $\mu_J = 0.01$, and $\sigma_J = 0.001$, the jump CF oscillates with frequency approximately $\lambda T \mu_J / \sigma_J$. Estimate this frequency for $T = 1$ and compute the Nyquist condition $N > 2\mu_J/(b-a) \cdot \lambda T / \sigma_J^2$ to determine the minimum $N$ needed to resolve the oscillations on an interval with $b - a = 4$.

??? success "Solution to Exercise 5"
    For the Merton model with $\lambda = 10$, $\mu_J = 0.01$, $\sigma_J = 0.001$, and $T = 1$:

    The jump CF is $\phi_{\text{jump}}(u) = \exp(\lambda T[e^{i\mu_J u - \sigma_J^2 u^2/2} - 1])$. The inner exponential $e^{i\mu_J u}$ oscillates with angular frequency $\mu_J$ in $u$-space. With $\lambda T = 10$ expected jumps and very concentrated jump sizes ($\sigma_J = 0.001$), the CF oscillates rapidly.

    **Oscillation frequency estimate:** The dominant oscillation in $\phi(u)$ comes from the term $e^{i\lambda T \mu_J u}$ (the leading-order contribution from the jump component for small $\sigma_J$). The angular frequency in $u$-space is approximately:

    $$
    \omega_{\text{osc}} = \lambda T \mu_J = 10 \times 1 \times 0.01 = 0.1 \text{ (radians per unit } u\text{)}
    $$

    The spatial frequency (cycles per unit $u$) is $\omega_{\text{osc}}/(2\pi) \approx 0.0159$.

    **Nyquist condition:** The COS method samples $\phi(u)$ at $u_k = k\pi/(b-a)$. The spacing in $u$ is $\Delta u = \pi/(b-a)$. To resolve oscillations with angular frequency $\omega_{\text{osc}}$, the Nyquist criterion requires:

    $$
    \Delta u < \frac{\pi}{\omega_{\text{osc}} \cdot (b-a)/(2\pi)} \implies N > \frac{2\omega_{\text{osc}}(b-a)}{\pi}
    $$

    More directly, using the given formula $N > 2\mu_J/(b-a) \cdot \lambda T / \sigma_J^2$:

    $$
    N > \frac{2 \times 0.01}{4} \times \frac{10}{0.000001} = 0.005 \times 10^7 = 50{,}000
    $$

    This is an enormous number of terms, making the COS method impractical for this parameter regime. The extremely small $\sigma_J$ creates near-Dirac jump sizes, producing extremely rapid oscillations in the CF.

    In practice, this regime requires either exponential tilting (damping the CF by evaluating $\phi(u + i\eta)$ for suitable $\eta > 0$) or switching to the Carr-Madan FFT with damping, which handles oscillatory CFs more gracefully.

---

**Exercise 6.** The diagnostic checklist includes six checks. Apply all six to the following scenario: a COS price under the Heston model that changes by $0.05$ when $N$ is doubled from 128 to 256, and changes by $0.02$ when $[a, b]$ is widened by 20%. Identify the likely failure mode, propose the appropriate remedy, and describe how you would verify the fix.

---

??? success "Solution to Exercise 6"
    **Applying the six diagnostic checks:**

    **Check 1: CF evaluates without NaN.** Evaluate $\phi_{\text{Heston}}(u)$ at $u = 0, 10, 100, 1000$. If all values are finite, this check passes. If NaN appears at large $u$, the branch-cut or overflow issue is the cause. Assume this check passes (the problem statement does not mention NaN).

    **Check 2: $|\phi(u)|$ decays for large $u$.** Plot $|\phi(u)|$ vs $u$. For the Heston model, $|\phi(u)|$ should decay exponentially. If it decays only as a power law or shows oscillation, this indicates a problem. Given the Heston model, this check likely passes unless there is a branch-cut issue.

    **Check 3: Price converges as $N$ increases.** The price changes by $0.05$ when $N$ doubles from 128 to 256. For a well-converged COS calculation, the change should be negligible (e.g., $< 10^{-6}$). **This check FAILS.** The COS series has not converged at $N = 128$.

    **Check 4: Price stable under $[a,b]$ widening.** The price changes by $0.02$ when $[a, b]$ is widened by 20%. **This check FAILS.** The truncation interval is too narrow, and significant probability mass lies outside $[a, b]$.

    **Check 5: Density non-negative.** Evaluate $f_{\text{COS}}(x)$ on a grid in $[a, b]$. If negative values appear, the cosine expansion has not converged. Given the convergence problems above, negative densities near the boundaries are likely. **This check may fail.**

    **Check 6: Put-call parity satisfied.** Compute $C - P$ and compare to $e^{-qT}S_0 - e^{-rT}K$. If the COS prices for call and put are both inaccurate, put-call parity may still hold (since both prices have similar truncation errors), but it may be violated if the truncation asymmetrically affects the two payoffs.

    **Likely failure mode:** The combination of failed checks 3 and 4 points to **truncation error** as the primary issue (Failure Mode 1), possibly compounded by a **branch-cut discontinuity** in the Heston CF (Failure Mode 5). The $0.02$ change under widening confirms that the interval $[a, b]$ is capturing too little of the density. The $0.05$ change under $N$ doubling could be a secondary effect (insufficient terms for the wider effective support) or could indicate a CF evaluation problem.

    **Proposed remedy:**

    1. First, check for the Heston branch-cut issue by switching to the "little Heston trap" formulation.
    2. Increase $L$ from 10 to 20 (or higher) in the truncation formula.
    3. Recompute with $N = 256$ and $N = 512$ using the wider interval.
    4. If the price stabilizes (change $< 10^{-6}$ between consecutive $N$ values), the fix is confirmed.

    **Verification:** After applying the fix, rerun all six checks. The price should change by less than $10^{-6}$ when $N$ doubles and less than $10^{-8}$ when $[a, b]$ is widened. Put-call parity should hold to machine precision, and the recovered density should be non-negative everywhere.
