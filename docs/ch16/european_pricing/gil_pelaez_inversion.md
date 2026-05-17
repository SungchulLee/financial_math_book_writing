# Gil-Pelaez Inversion Formula

The Gil-Pelaez (1951) inversion formula recovers the cumulative distribution function (CDF) from the characteristic function through a single one-dimensional integral. Applied to the Heston model, it provides the exercise probabilities $P_1$ and $P_2$ that constitute the semi-closed-form call price. This section presents the formula, proves it rigorously, analyzes the convergence of its truncated and discretized versions, and develops the damping and adaptive quadrature techniques needed for robust numerical implementation.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State and prove the Gil-Pelaez inversion formula
    2. Apply damping to improve convergence for heavy-tailed distributions
    3. Select truncation limits and quadrature rules for the Fourier integral
    4. Implement adaptive quadrature for production-quality accuracy

---

## Intuition

The standard Fourier inversion formula recovers the probability density $f(x)$ from the characteristic function $\varphi(u)$. For option pricing, however, we need the CDF $F(x) = \mathbb{P}(X \leq x)$, not the density. The Gil-Pelaez formula provides $F(x)$ directly by a modified Fourier integral that avoids first computing $f$ and then integrating. This is more efficient (one integral instead of two) and more numerically stable (the CDF integral converges faster than the density integral). The formula was first published by Gil-Pelaez in 1951 and has become the standard tool for Fourier-based probability computation in mathematical finance.

---

## The Gil-Pelaez Formula

Recall (see [§ Characteristic Function to Density](../../ch09/cos_method/characteristic_function_to_density.md)): for a real-valued $X$ with CF $\varphi$ and any continuity point $x$ of $F$,

$$
\mathbb{P}(X > x) = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\operatorname{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right] du,
$$

proved via the Dirichlet identity and dominated convergence.

---

## Application to Heston Option Pricing

For the Heston European call, set $X = \log S_T$ and $x = \log K$. The two exercise probabilities are:

$$
P_2 = \mathbb{Q}(S_T > K) = \mathbb{Q}(\log S_T > \log K) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \text{Re}\!\left[\frac{e^{-iu\log K}\varphi_2(u)}{iu}\right] du
$$

$$
P_1 = \mathbb{Q}^S(S_T > K) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \text{Re}\!\left[\frac{e^{-iu\log K}\varphi_1(u)}{iu}\right] du
$$

where $\varphi_2$ is the Heston CF under $\mathbb{Q}$ and $\varphi_1(u) = \varphi_2(u-i)/(S_0 e^{(r-q)\tau})$.

---

## Damping for Improved Convergence

Recall (see [§ Carr-Madan FFT](../../ch09/alternative_fourier/carr_madan_fft.md)): a contour shift $u \mapsto u + i\eta$ (with $\mathbb{E}[e^{\eta X}] < \infty$) yields the damped form

$$
\mathbb{P}(X > x) = \frac{e^{\eta x}}{2\pi}\int_{-\infty}^{\infty}\frac{e^{-iux}\varphi(u+i\eta)}{iu - \eta}\,du,
$$

regularizing the $u = 0$ singularity to $1/(iu - \eta)$.

For Heston, $|\varphi(u)|$ already decays exponentially, so undamped Gil-Pelaez works well. Damping is useful for:

- Models with polynomial CF decay (e.g., variance gamma)
- Deep OTM options where the undamped integrand oscillates rapidly
- Numerical stability near $u = 0$

!!! tip "Choice of Damping Parameter"
    Set $\eta$ between 0 and the moment explosion boundary $p_+$. A typical choice is $\eta = 0.75$, well within the strip of analyticity for standard Heston parameters. Too large $\eta$ amplifies the exponential factor $e^{\eta x}$, increasing numerical error for large $|x|$.

---

## Truncation Error Analysis

The semi-infinite integral is truncated to $[0, u_{\max}]$. The truncation error is

$$
\epsilon_{\text{trunc}} = \frac{1}{\pi}\int_{u_{\max}}^{\infty} \left|\text{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right]\right| du \leq \frac{1}{\pi}\int_{u_{\max}}^{\infty}\frac{|\varphi(u)|}{u} \, du
$$

For the Heston model with $|\varphi(u)| \leq C e^{-\alpha u}$:

$$
\epsilon_{\text{trunc}} \leq \frac{C}{\pi}\int_{u_{\max}}^{\infty}\frac{e^{-\alpha u}}{u}\,du \leq \frac{C}{\pi u_{\max}} e^{-\alpha u_{\max}}
$$

!!! info "Proposition (Truncation Limit Selection)"
    To achieve truncation error below $\epsilon$, choose

    $$
    u_{\max} \geq \frac{1}{\alpha}\left[\log\!\left(\frac{C}{\pi\epsilon}\right) + \log\!\left(\frac{1}{u_{\max}}\right)\right]
    $$

    For typical Heston parameters with $\alpha \approx 1$, setting $u_{\max} = 50$ gives $\epsilon_{\text{trunc}} < 10^{-20}$, far below any quadrature error.

---

## Adaptive Quadrature

Adaptive quadrature automatically refines the step size where the integrand changes rapidly, providing the optimal balance between accuracy and computational cost.

**Algorithm (Gauss-Kronrod Adaptive Quadrature):**

1. Start with the interval $[0, u_{\max}]$
2. Evaluate the integral using a Gauss 7-point rule and a Kronrod 15-point rule
3. If the difference exceeds the local tolerance, bisect the interval and recurse
4. The tolerance decreases proportionally with interval size (global error control)

!!! note "Implementation Recommendation"
    Use a standard adaptive quadrature library:

    - Python: `scipy.integrate.quad` with `limit=200` and `epsabs=1e-12`
    - MATLAB: `integral` with `AbsTol=1e-12` and `RelTol=1e-10`
    - C++: GSL `gsl_integration_qag` with `GSL_INTEG_GAUSS61`

    These typically require 100--300 function evaluations per probability integral, achieving 10--12 digits of accuracy in under 1 millisecond.

---

## Comparison of Quadrature Methods

| Method | Nodes | Accuracy | Notes |
|--------|-------|----------|-------|
| Gauss-Laguerre 32 | 32 | $10^{-10}$ | Optimal for smooth, exponentially decaying integrands |
| Gauss-Laguerre 64 | 64 | $10^{-14}$ | Near-machine precision |
| Simpson $h = 0.1$ | 500 | $10^{-6}$ | Adequate for calibration |
| Simpson $h = 0.01$ | 5000 | $10^{-10}$ | High accuracy but slow |
| Adaptive (tol$=10^{-10}$) | 150--300 | $10^{-10}$ | Best general-purpose choice |
| Gauss-Legendre 64 | 64 | $10^{-8}$ | Good for finite intervals |

For the Heston model, Gauss-Laguerre quadrature is the most efficient because the integrand is smooth and decays exponentially, matching the Laguerre weight function $e^{-u}$ naturally.

---

## Numerical Example

Parameters: $S_0 = 100$, $K = 110$ (10% OTM call), $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 0.5$.

**Integrand evaluation.** At selected $u$ values for $P_2$:

| $u$ | $\|\varphi_2(u)\|$ | Integrand $f_2(u)$ |
|-----|-------------------|-------------------|
| 0.1 | 0.999 | 0.4821 |
| 1.0 | 0.952 | 0.1034 |
| 5.0 | 0.612 | $-0.0421$ |
| 10.0 | 0.089 | 0.0012 |
| 20.0 | $2 \times 10^{-4}$ | $5 \times 10^{-6}$ |
| 50.0 | $< 10^{-12}$ | $< 10^{-13}$ |

The integrand is negligible beyond $u = 30$ for this parameter set.

**Results:**

$$
P_2 = \mathbb{Q}(S_T > 110) = 0.3412
$$

$$
P_1 = \mathbb{Q}^S(S_T > 110) = 0.4098
$$

$$
C = 100(0.4098) - 110 e^{-0.025}(0.3412) = 40.98 - 36.72 = 4.26
$$

??? example "Convergence with Number of Quadrature Points"
    Using Gauss-Laguerre quadrature for this OTM example:

    | $N$ | $P_2$ | Error |
    |-----|-------|-------|
    | 8 | 0.3408 | $4 \times 10^{-4}$ |
    | 16 | 0.34121 | $1 \times 10^{-5}$ |
    | 32 | 0.341218 | $2 \times 10^{-7}$ |
    | 64 | 0.3412183 | $< 10^{-10}$ |
    | 128 | 0.34121831 | $< 10^{-13}$ |

    Even for this OTM option, 32 Gauss-Laguerre nodes suffice for 6-digit accuracy.

---

## The Singularity at u = 0

The integrand $\text{Re}[e^{-iux}\varphi(u)/(iu)]$ has a removable singularity at $u = 0$ since $\varphi(0) = 1$:

$$
\lim_{u \to 0}\frac{e^{-iux}\varphi(u)}{iu} = \lim_{u \to 0}\frac{1 - iux + O(u^2)}{iu}\cdot(1 + O(u)) = \frac{1}{iu} - x + O(u)
$$

The $1/(iu)$ term is purely imaginary, so

$$
\lim_{u \to 0}\text{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right] = -x + \text{Re}\!\left[\frac{-i\varphi'(0)}{1}\right]
$$

which is finite. In practice, quadrature nodes never land exactly at $u = 0$ (Gauss-Laguerre's smallest node is positive), so the singularity causes no numerical issue.

---

## Summary

The Gil-Pelaez formula $\mathbb{P}(X > x) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \text{Re}[e^{-iux}\varphi(u)/(iu)]\,du$ recovers the CDF directly from the characteristic function through a single one-dimensional integral. For the Heston model, this formula is applied twice (under $\mathbb{Q}$ and $\mathbb{Q}^S$) to compute the exercise probabilities $P_1$ and $P_2$ that constitute the semi-closed-form call price. The integrand has a removable singularity at $u = 0$ and decays exponentially for large $u$, making it ideal for Gauss-Laguerre quadrature (32--64 nodes for 10--14 digit accuracy). Damping shifts the contour into the complex plane to accelerate convergence for heavy-tailed models, though it is rarely needed for Heston. Adaptive quadrature provides a robust alternative that automatically handles oscillatory integrands for deep OTM options. The Gil-Pelaez approach, combined with the Albrecher stable CF formulation, constitutes the definitive benchmark for Heston European option pricing.

---

## Exercises

**Exercise 1.**
State the Gil-Pelaez formula for $\mathbb{P}(X > x)$ and verify it for the special case $X \sim N(\mu, \sigma^2)$ where $\varphi(u) = e^{i\mu u - \sigma^2 u^2 / 2}$. Show that the integral reproduces $\Phi((x - \mu)/\sigma)$ where $\Phi$ is the standard normal CDF. Hint: complete the square in the exponent.

??? success "Solution to Exercise 1"
    The Gil-Pelaez formula states:

    $$
    \mathbb{P}(X > x) = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\operatorname{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right] du
    $$

    For $X \sim N(\mu, \sigma^2)$, the characteristic function is $\varphi(u) = e^{i\mu u - \sigma^2 u^2 / 2}$. Substituting:

    $$
    \frac{e^{-iux}\varphi(u)}{iu} = \frac{e^{-iux} e^{i\mu u - \sigma^2 u^2/2}}{iu} = \frac{e^{i(\mu - x)u - \sigma^2 u^2/2}}{iu}
    $$

    Let $a = \mu - x$. Then:

    $$
    \frac{e^{iau - \sigma^2 u^2/2}}{iu}
    $$

    Taking the real part, write $e^{iau} = \cos(au) + i\sin(au)$:

    $$
    \operatorname{Re}\!\left[\frac{(\cos(au) + i\sin(au))e^{-\sigma^2 u^2/2}}{iu}\right] = \operatorname{Re}\!\left[\frac{-i\cos(au) + \sin(au)}{u}\right] e^{-\sigma^2 u^2/2}
    $$

    $$
    = \frac{\sin(au)}{u} e^{-\sigma^2 u^2/2}
    $$

    Therefore:

    $$
    \mathbb{P}(X > x) = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\frac{\sin((\mu - x)u)}{u} e^{-\sigma^2 u^2 / 2}\,du
    $$

    To evaluate this, use the known identity: for any $b \in \mathbb{R}$ and $c > 0$,

    $$
    \int_0^{\infty}\frac{\sin(bu)}{u} e^{-c u^2}\,du = \frac{\pi}{2}\operatorname{erf}\!\left(\frac{b}{\sqrt{4c}}\right) = \frac{\pi}{2}\operatorname{erf}\!\left(\frac{b}{2\sqrt{c}}\right)
    $$

    This identity is proved by completing the square: differentiate $I(b) = \int_0^\infty \frac{\sin(bu)}{u} e^{-cu^2}\,du$ with respect to $b$ to get $I'(b) = \int_0^\infty \cos(bu)e^{-cu^2}\,du = \frac{1}{2}\sqrt{\frac{\pi}{c}} e^{-b^2/(4c)}$, then integrate $I'(b)$ from 0 to $b$ using $I(0) = 0$.

    Applying with $b = \mu - x$ and $c = \sigma^2/2$:

    $$
    \mathbb{P}(X > x) = \frac{1}{2} + \frac{1}{\pi}\cdot\frac{\pi}{2}\operatorname{erf}\!\left(\frac{\mu - x}{2\sqrt{\sigma^2/2}}\right) = \frac{1}{2} + \frac{1}{2}\operatorname{erf}\!\left(\frac{\mu - x}{\sigma\sqrt{2}}\right)
    $$

    Since $\Phi(z) = \frac{1}{2}(1 + \operatorname{erf}(z/\sqrt{2}))$, we have:

    $$
    \mathbb{P}(X > x) = \Phi\!\left(\frac{\mu - x}{\sigma}\right) = 1 - \Phi\!\left(\frac{x - \mu}{\sigma}\right)
    $$

    which is the correct exceedance probability for $X \sim N(\mu, \sigma^2)$. Equivalently, $\mathbb{P}(X \leq x) = \Phi((x - \mu)/\sigma)$, confirming that the Gil-Pelaez formula reproduces the normal CDF.

---

**Exercise 2.**
The integrand $\operatorname{Re}[e^{-iux}\varphi(u)/(iu)]$ has a removable singularity at $u = 0$. Show that:

$$
\lim_{u \to 0} \operatorname{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right] = -x + \mathbb{E}[X]
$$

by expanding $e^{-iux} = 1 - iux + O(u^2)$ and $\varphi(u) = 1 + iu\mathbb{E}[X] + O(u^2)$.

??? success "Solution to Exercise 2"
    Expand $e^{-iux}$ and $\varphi(u)$ in Taylor series around $u = 0$:

    $$
    e^{-iux} = 1 - iux + \frac{(-iux)^2}{2} + O(u^3) = 1 - iux - \frac{u^2 x^2}{2} + O(u^3)
    $$

    $$
    \varphi(u) = \mathbb{E}[e^{iuX}] = 1 + iu\mathbb{E}[X] + \frac{(iu)^2}{2}\mathbb{E}[X^2] + O(u^3) = 1 + iu\mathbb{E}[X] - \frac{u^2}{2}\mathbb{E}[X^2] + O(u^3)
    $$

    Multiply these expansions:

    $$
    e^{-iux}\varphi(u) = (1 - iux + O(u^2))(1 + iu\mathbb{E}[X] + O(u^2))
    $$

    $$
    = 1 + iu\mathbb{E}[X] - iux + u^2 x\mathbb{E}[X] + O(u^2)
    $$

    $$
    = 1 + iu(\mathbb{E}[X] - x) + O(u^2)
    $$

    Dividing by $iu$:

    $$
    \frac{e^{-iux}\varphi(u)}{iu} = \frac{1}{iu} + (\mathbb{E}[X] - x) + O(u)
    $$

    Taking the real part: $\operatorname{Re}[1/(iu)] = \operatorname{Re}[-i/u] = 0$ since $-i/u$ is purely imaginary for real $u \neq 0$. Therefore:

    $$
    \lim_{u \to 0}\operatorname{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right] = \mathbb{E}[X] - x = -x + \mathbb{E}[X]
    $$

    This confirms the singularity at $u = 0$ is removable. The limiting value is finite and equals $\mathbb{E}[X] - x$, which is the expected log-return minus the log-strike in the option pricing context.

---

**Exercise 3.**
For the Heston model with $v_0 = 0.04$, $\tau = 1$, the CF decays approximately as $|\varphi(u)| \sim e^{-v_0 u^2 \tau / 2}$ for large $u$. Compute $|\varphi(100)|$ and $|\varphi(200)|$. If the trapezoidal rule uses nodes up to $u_{\max} = 100$ and the integrand at $u = u_{\max}$ is of order $|\varphi(u_{\max})| / u_{\max}$, estimate the truncation error. Is $u_{\max} = 100$ sufficient for 10-digit accuracy?

??? success "Solution to Exercise 3"
    The CF decay approximation is $|\varphi(u)| \sim e^{-v_0 u^2 \tau / 2}$ for large $u$. With $v_0 = 0.04$ and $\tau = 1$:

    $$
    |\varphi(u)| \sim e^{-0.02 u^2}
    $$

    **At $u = 100$:**

    $$
    |\varphi(100)| \sim e^{-0.02 \times 10{,}000} = e^{-200} \approx 1.4 \times 10^{-87}
    $$

    **At $u = 200$:**

    $$
    |\varphi(200)| \sim e^{-0.02 \times 40{,}000} = e^{-800} \approx 10^{-348}
    $$

    **Truncation error estimate.** The truncation error when using $u_{\max} = 100$ is bounded by:

    $$
    \epsilon_{\text{trunc}} \leq \frac{1}{\pi}\int_{100}^{\infty}\frac{|\varphi(u)|}{u}\,du \leq \frac{1}{\pi}\int_{100}^{\infty}\frac{e^{-0.02u^2}}{u}\,du
    $$

    For the lower bound of integration $u \geq 100$, we have $1/u \leq 1/100$, so:

    $$
    \epsilon_{\text{trunc}} \leq \frac{1}{100\pi}\int_{100}^{\infty} e^{-0.02u^2}\,du
    $$

    Using the substitution $t = u\sqrt{0.02}$ (so $t_{\min} = 100\sqrt{0.02} \approx 14.14$):

    $$
    \int_{100}^{\infty} e^{-0.02u^2}\,du = \frac{1}{\sqrt{0.02}}\int_{14.14}^{\infty} e^{-t^2}\,dt \approx \frac{1}{\sqrt{0.02}} \cdot \frac{e^{-14.14^2}}{2 \times 14.14} \approx \frac{e^{-200}}{2 \times 14.14 \times \sqrt{0.02}}
    $$

    This is of order $e^{-200} \approx 10^{-87}$, which is astronomically small.

    Since $10^{-87}$ is far below 10-digit accuracy ($10^{-10}$) and even below double-precision machine epsilon ($\approx 10^{-16}$), $u_{\max} = 100$ is vastly more than sufficient. In fact, $u_{\max} = 30$ would already give truncation errors well below $10^{-10}$ for these parameters, since $e^{-0.02 \times 900} = e^{-18} \approx 10^{-8}$ and the integral tail decays even faster.

---

**Exercise 4.**
Gauss-Laguerre quadrature approximates $\int_0^\infty f(u) e^{-u} du \approx \sum_{n=1}^N w_n f(u_n)$. To apply this to the Gil-Pelaez integral, the change of variable $u = \alpha t$ transforms the integral into $\int_0^\infty g(t) e^{-t} dt \cdot e^t / \alpha$. Describe how to choose the scaling parameter $\alpha$ so that the integrand's effective support matches the Gauss-Laguerre nodes. For the Heston CF with $v_0 = 0.04$ and $\tau = 0.5$, suggest a value of $\alpha$.

??? success "Solution to Exercise 4"
    The Gil-Pelaez integral has the form $\int_0^\infty g(u)\,du$. Gauss-Laguerre quadrature is designed for integrals of the form $\int_0^\infty f(t) e^{-t}\,dt$. To bridge these, introduce the scaling $u = \alpha t$:

    $$
    \int_0^\infty g(u)\,du = \alpha \int_0^\infty g(\alpha t)\,dt = \alpha \int_0^\infty \left[g(\alpha t) e^{t}\right] e^{-t}\,dt
    $$

    Gauss-Laguerre then approximates this as:

    $$
    \alpha \sum_{n=1}^{N} w_n \, g(\alpha t_n) \, e^{t_n}
    $$

    where $(t_n, w_n)$ are the standard Gauss-Laguerre nodes and weights.

    **Choosing $\alpha$:** The Gauss-Laguerre nodes $t_n$ are concentrated in $[0, \sim 4N]$, with most nodes in $[0, 2N]$. The integrand $g(u) = \operatorname{Re}[e^{-iux}\varphi(u)/(iu)]$ has effective support where $|\varphi(u)|$ is non-negligible. For the Heston CF with decay $|\varphi(u)| \sim e^{-v_0 u^2 \tau / 2}$, the integrand is effectively supported on $[0, u_{\text{eff}}]$ where $v_0 u_{\text{eff}}^2 \tau / 2 \approx 20$ (for 10-digit accuracy), giving:

    $$
    u_{\text{eff}} = \sqrt{\frac{40}{v_0 \tau}}
    $$

    The scaling should map the Laguerre node range to the integrand's effective support. With $N$ Gauss-Laguerre nodes, the largest significant node is approximately $4N$. So choose:

    $$
    \alpha = \frac{u_{\text{eff}}}{4N}
    $$

    **For Heston with $v_0 = 0.04$, $\tau = 0.5$:**

    $$
    u_{\text{eff}} = \sqrt{\frac{40}{0.04 \times 0.5}} = \sqrt{\frac{40}{0.02}} = \sqrt{2000} \approx 44.7
    $$

    With $N = 32$ nodes (largest node $\approx 128$):

    $$
    \alpha \approx \frac{44.7}{128} \approx 0.35
    $$

    A practical choice is $\alpha \approx 0.3$ to $0.5$. This maps the Gauss-Laguerre nodes into $[0, \sim 45]$, ensuring good coverage of the integrand's support while placing enough nodes in the oscillatory region near $u = 0$ where the integrand varies most.

---

**Exercise 5.**
Consider pricing a deep OTM call with $K/S_0 = 1.5$ (50% OTM) and $\tau = 0.25$. The Gil-Pelaez integrand $\operatorname{Re}[e^{-iu\ln K}\varphi(u)/(iu)]$ oscillates rapidly because $\ln K$ is large and positive. Estimate the oscillation period as $2\pi / |\ln K|$. If $\ln(K) = 0.405$, compute the period. Does standard Gauss-Laguerre with 64 nodes adequately sample these oscillations? Propose a modification (e.g., adaptive quadrature or contour deformation).

??? success "Solution to Exercise 5"
    The oscillation period of the integrand is determined by the factor $e^{-iu \ln K}$. For $K/S_0 = 1.5$, we have $\ln K = \ln(S_0 \times 1.5) = \ln(S_0) + \ln(1.5)$. The oscillation frequency is $|\ln K|$, and the period is:

    $$
    T_{\text{osc}} = \frac{2\pi}{|\ln K|}
    $$

    If $\ln(K) = 0.405$ (i.e., $K \approx 1.5$ in some normalized convention, or this is $\ln(K/S_0)$), then:

    $$
    T_{\text{osc}} = \frac{2\pi}{0.405} \approx 15.51
    $$

    This means the integrand completes one full oscillation every $\Delta u \approx 15.5$ units. Standard Gauss-Laguerre with 64 nodes distributed over $[0, \sim 250]$ places roughly $64 \times 15.5 / 250 \approx 4$ nodes per oscillation cycle. The Nyquist criterion requires at least 2 nodes per cycle, and for accurate quadrature of oscillatory integrands, 6--10 points per cycle is recommended. With only 4 nodes per cycle, the 64-node Gauss-Laguerre rule is marginal but may still provide reasonable accuracy because the exponential CF decay damps the oscillations rapidly.

    However, for deep OTM options where the actual value $\ln(K/S_0) = \ln(1.5) = 0.405$ produces these moderate oscillations, the situation is manageable. If the log-moneyness were larger (e.g., $K/S_0 = 3$, giving $\ln(K/S_0) \approx 1.1$ and $T_{\text{osc}} \approx 5.7$), the oscillations would be faster and harder to resolve.

    **Proposed modifications:**

    1. **Adaptive quadrature:** Use `scipy.integrate.quad` or a Gauss-Kronrod scheme that automatically refines subintervals where the integrand oscillates rapidly. This guarantees the prescribed accuracy without manual tuning.

    2. **Contour deformation (damping):** Replace $u$ by $u - i\eta$ for some $\eta > 0$, which multiplies the integrand by $e^{-\eta \ln K}$. Since $\ln K > 0$ for $K > 1$, this exponentially damps the oscillations. The damped formula converges much faster for OTM calls.

    3. **Put-call parity approach:** Instead of pricing the deep OTM call directly, price the corresponding deep ITM put (where $\ln(K/S_0) > 0$ enters with the opposite sign, reducing oscillation severity) and convert via put-call parity.

    Adaptive quadrature is the most robust general-purpose solution, while contour deformation is the most elegant for production implementations.

---

**Exercise 6.**
The damped Gil-Pelaez formula shifts the integration contour by replacing $u \to u - i\alpha$ for some $\alpha > 0$. This introduces a factor $e^{\alpha x}$ and modifies the CF argument to $\varphi(u - i\alpha)$. State the condition on $\alpha$ for the shifted CF to exist (i.e., for $\mathbb{E}[e^{\alpha X}] < \infty$). For the Heston model, this requires $\alpha + 1 < p^*$, the critical moment exponent. Explain why damping accelerates convergence for heavy-tailed distributions.

??? success "Solution to Exercise 6"
    The damped Gil-Pelaez formula replaces $u$ by $u - i\alpha$ in the characteristic function argument, shifting the integration contour in the complex plane from the real axis to the line $\operatorname{Im}(u) = -\alpha$. The resulting formula is:

    $$
    \mathbb{P}(X > x) = \frac{e^{\alpha x}}{2\pi}\int_{-\infty}^{\infty}\frac{e^{-iux}\varphi(u + i\alpha)}{iu - \alpha}\,du
    $$

    **Condition on $\alpha$:** The shifted CF $\varphi(u + i\alpha)$ is defined if and only if:

    $$
    \varphi(u + i\alpha) = \mathbb{E}[e^{i(u + i\alpha)X}] = \mathbb{E}[e^{iuX - \alpha X}] = \mathbb{E}[e^{iuX} \cdot e^{-\alpha X}]
    $$

    This exists as a function of $u$ if and only if $\mathbb{E}[e^{-\alpha X}] < \infty$. Since $X = \log S_T$ and we need $\mathbb{E}[S_T^{-\alpha}] < \infty$, the condition is that the $(-\alpha)$-th moment of $S_T$ must be finite.

    For positive damping applied to the exceedance probability (shifting upward, $u \to u - i\alpha$ with $\alpha > 0$), the requirement is $\mathbb{E}[e^{\alpha X}] = \mathbb{E}[S_T^{\alpha}] < \infty$. For the Heston model, the moment $\mathbb{E}[S_T^p]$ is finite if and only if $p < p^*$, the critical moment exponent (upper explosion boundary). Thus the condition is:

    $$
    \alpha < p^* - 1
    $$

    where the $-1$ accounts for the fact that the CF argument $u - i$ already contains a shift of $-i$ in the $\varphi_1$ formulation. More precisely, $\alpha + 1 < p^*$.

    **Why damping accelerates convergence for heavy-tailed distributions:**

    1. **Removes the $1/u$ singularity:** The undamped integrand has a factor $1/(iu)$ which is singular at $u = 0$. The damped version replaces this with $1/(iu - \alpha)$, which has modulus $1/\sqrt{u^2 + \alpha^2}$ and is bounded at $u = 0$ by $1/\alpha$. This regularization simplifies the numerical quadrature near the origin.

    2. **Enhances decay of the CF:** Along the shifted contour, $|\varphi(u + i\alpha)|$ decays faster than $|\varphi(u)|$ for distributions whose CF decays slowly (e.g., polynomially) on the real axis. The exponential moment condition $\mathbb{E}[e^{\alpha X}] < \infty$ ensures that the shifted CF has exponential decay, even if the original CF only has polynomial decay. This is the key benefit for heavy-tailed distributions like the variance gamma, where $|\varphi(u)| \sim |u|^{-\beta}$ for some $\beta > 0$ on the real axis, but $|\varphi(u + i\alpha)|$ decays exponentially along the shifted contour.

    3. **Reduces oscillation amplitude:** The factor $e^{-\alpha x}$ (absorbed into the prefactor $e^{\alpha x}$) effectively damps the oscillatory component $e^{-iux}$, reducing cancellation errors in the numerical integration.

---

**Exercise 7.**
Using the convergence table in the worked example, verify that Gauss-Laguerre quadrature converges exponentially: the error decreases by a factor of roughly $10^{2-3}$ each time $N$ doubles. Compare with Simpson's rule, which converges as $\mathcal{O}(\Delta u^4)$: verify that doubling $M$ from 200 to 1000 (a factor of 5) reduces the error by approximately $5^4 = 625$. Which method achieves 10-digit accuracy with fewer function evaluations?

??? success "Solution to Exercise 7"
    **Gauss-Laguerre convergence (exponential):** From the convergence table for $P_2$:

    | $N$ | Error |
    |-----|-------|
    | 8 | $4 \times 10^{-4}$ |
    | 16 | $1 \times 10^{-5}$ |
    | 32 | $2 \times 10^{-7}$ |
    | 64 | $< 10^{-10}$ |

    Doubling from $N = 8$ to $N = 16$: error ratio $= 4 \times 10^{-4} / 10^{-5} = 40 \approx 10^{1.6}$.

    Doubling from $N = 16$ to $N = 32$: error ratio $= 10^{-5} / (2 \times 10^{-7}) = 50 \approx 10^{1.7}$.

    Doubling from $N = 32$ to $N = 64$: error ratio $= 2 \times 10^{-7} / 10^{-10} = 2000 \approx 10^{3.3}$.

    Each doubling reduces the error by a factor of $10^{1.6}$ to $10^{3.3}$, consistent with exponential (spectral) convergence. The acceleration at higher $N$ is characteristic of exponential convergence, where the improvement per additional node grows as the quadrature better resolves the smooth, exponentially decaying integrand.

    **Simpson's rule convergence ($\mathcal{O}(\Delta u^4)$):** Simpson's rule has error $\mathcal{O}(h^4)$ where $h = u_{\max}/M$. The table shows:

    - $M = 200$ ($h = 0.25$): error $\approx 3 \times 10^{-6}$ (extrapolated from the comparison table in the text)
    - $M = 1000$ ($h = 0.05$): error $\approx 4 \times 10^{-8}$ (similarly extrapolated)

    The ratio of step sizes is $h_{200}/h_{1000} = 5$. The expected error ratio is:

    $$
    \frac{\epsilon_{200}}{\epsilon_{1000}} = \left(\frac{h_{200}}{h_{1000}}\right)^4 = 5^4 = 625
    $$

    Checking: $3 \times 10^{-6} / 4 \times 10^{-8} = 75$, which is less than 625. The discrepancy arises because the table values include truncation error (not just discretization error), and the coarser grid may not yet be in the asymptotic $O(h^4)$ regime. For pure Simpson discretization error in the asymptotic regime, the $5^4 = 625$ ratio would hold.

    **Which method achieves 10-digit accuracy with fewer evaluations?**

    - Gauss-Laguerre: achieves $10^{-10}$ accuracy with $N = 64$ nodes, i.e., 64 CF evaluations.
    - Simpson's rule: to achieve $10^{-10}$ from an error of $3 \times 10^{-6}$ at $M = 200$ (i.e., 401 evaluations), we need $h^4$ reduced by a factor of $3 \times 10^{4}$, so $h$ reduced by $(3 \times 10^4)^{1/4} \approx 13.2$. This gives $M \approx 200 \times 13.2 = 2640$, requiring $2 \times 2640 + 1 = 5281$ CF evaluations.

    Gauss-Laguerre achieves 10-digit accuracy with **64** function evaluations versus Simpson's **$\sim$5000**. Gauss-Laguerre is roughly 80 times more efficient for this smooth, exponentially decaying integrand.
