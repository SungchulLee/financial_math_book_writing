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

The COS density coefficients are:

$$
A_k = \frac{2}{b-a}\operatorname{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi a/(b-a)}\right]
$$

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

**Branch-cut discontinuities in the Heston CF.** The Heston characteristic function involves the complex square root $\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}$. The standard principal branch of the square root has a cut along the negative real axis. For certain $u$ values, the argument of the square root crosses this cut, producing a discontinuous $\phi(u)$ that destroys convergence.

The Albrecher et al. (2007) rotation $\gamma \to -\gamma$ with corresponding adjustment of $g$ eliminates this problem for the "little Heston trap" formulation.

**Overflow/underflow in exponentials.** For large $|u|$ or long maturities $T$, the exponential terms $e^{-\gamma T}$ in the Heston CF can overflow or underflow. This produces NaN or zero values in the cosine coefficients.

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
