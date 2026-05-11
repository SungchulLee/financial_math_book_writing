# COS Pricing Formula for European Options

The COS method (Fang and Oosterlee, 2008) combines the cosine expansion of the risk-neutral density with analytic integration against the payoff to produce a remarkably efficient pricing formula. The key idea is that European option prices are expectations of the form $e^{-rT}\mathbb{E}[\Phi(X_T)]$, where $\Phi$ is the payoff function and $X_T$ is the log-price. Expanding the density in a cosine series and integrating term-by-term against $\Phi$ converts the expectation into a finite sum involving two sets of coefficients: density coefficients $F_k$ (computed from the characteristic function) and payoff coefficients $V_k$ (computed analytically). This section derives the COS pricing formula, computes $V_k$ for standard payoffs, and demonstrates the method with numerical examples.

!!! info "Prerequisites"

    - [Cosine Coefficients via CF](cosine_coefficients_via_cf.md) (the density coefficients $F_k$)
    - [Truncation to Finite Domain](truncation_to_finite_domain.md) (choice of $[a, b]$)
    - [Cosine Expansion on $[0, \pi]$](../fourier_series/cosine_expansion.md) (cosine series properties)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the COS pricing formula from the cosine expansion of the density
    2. Compute payoff coefficients $V_k$ analytically for calls, puts, and digital options
    3. Implement the COS method for European option pricing
    4. Verify COS prices against Black--Scholes closed-form values
    5. Understand the role of each component ($F_k$, $V_k$, $N$, $[a, b]$) in the formula

---

## Derivation of the COS Pricing Formula

Consider a European option with payoff $\Phi(x)$ at maturity $T$, where $x = \ln(S_T/K)$ is the log-moneyness. Under the risk-neutral measure, the option value at time $0$ is

$$
V = e^{-rT}\int_{-\infty}^{\infty} \Phi(x)\, f(x)\, dx
$$

where $f$ is the risk-neutral density of $X_T = \ln(S_T/K)$.

**Step 1: Truncate to $[a, b]$.** Replace $\mathbb{R}$ by the truncation interval:

$$
V \approx e^{-rT}\int_a^b \Phi(x)\, f(x)\, dx
$$

**Step 2: Expand $f$ in a cosine series.** Substitute the truncated cosine expansion:

$$
f(x) \approx \sum_{k=0}^{N-1}{}' F_k \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)
$$

where $F_k = \frac{2}{b-a}\,\text{Re}[\phi(k\pi/(b-a))\,e^{-ik\pi a/(b-a)}]$.

**Step 3: Exchange sum and integral.** Since the cosine series converges uniformly for smooth $f$:

$$
V \approx e^{-rT}\sum_{k=0}^{N-1}{}' F_k \int_a^b \Phi(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

**Step 4: Define the payoff coefficients.** Set

$$
V_k = \int_a^b \Phi(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

!!! note "Theorem: COS Pricing Formula"
    The COS approximation to the European option value is

    $$
    V_{\text{COS}} = e^{-rT}\sum_{k=0}^{N-1}{}' F_k\, V_k
    $$

    where:

    - $F_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]$ (density coefficients from CF)
    - $V_k = \int_a^b \Phi(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx$ (payoff coefficients)
    - The prime on $\sum'$ means the $k = 0$ term is halved

---

## Payoff Coefficients for a European Call

For a European call with strike $K$, the payoff in terms of the log-moneyness $x = \ln(S_T/K)$ is

$$
\Phi(x) = K(e^x - 1)^+ = \begin{cases} K(e^x - 1) & \text{if } x > 0 \\ 0 & \text{if } x \leq 0 \end{cases}
$$

The payoff coefficients split into two integrals:

$$
V_k = K\int_0^b (e^x - 1)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

(assuming $a < 0 < b$, so the exercise region is $[0, b]$).

Define the auxiliary integrals:

$$
\chi_k(c, d) = \int_c^d e^x \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

$$
\psi_k(c, d) = \int_c^d \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

!!! note "Proposition: Closed-Form Auxiliary Integrals"
    For $\omega_k = k\pi/(b-a)$:

    $$
    \chi_k(c, d) = \frac{1}{1 + \omega_k^2}\left[e^d\left(\cos(\omega_k(d-a)) + \omega_k\sin(\omega_k(d-a))\right) - e^c\left(\cos(\omega_k(c-a)) + \omega_k\sin(\omega_k(c-a))\right)\right]
    $$

    $$
    \psi_k(c, d) = \begin{cases} \frac{b-a}{k\pi}\left[\sin(\omega_k(d-a)) - \sin(\omega_k(c-a))\right] & \text{if } k \neq 0 \\ d - c & \text{if } k = 0 \end{cases}
    $$

**Proof of $\chi_k$.** Integrate by parts twice. Let $I = \int e^x \cos(\omega_k(x-a))\,dx$. The first integration by parts gives

$$
I = e^x\cos(\omega_k(x-a)) + \omega_k\int e^x\sin(\omega_k(x-a))\,dx
$$

The second integration by parts yields

$$
I = e^x\cos(\omega_k(x-a)) + \omega_k e^x\sin(\omega_k(x-a)) - \omega_k^2 I
$$

Solving for $I$: $(1 + \omega_k^2)I = e^x[\cos(\omega_k(x-a)) + \omega_k\sin(\omega_k(x-a))]$. Evaluating between $c$ and $d$ gives the result. $\square$

The call payoff coefficients are therefore:

$$
V_k^{\text{call}} = K\left[\chi_k(0, b) - \psi_k(0, b)\right]
$$

---

## Payoff Coefficients for a European Put

By put-call parity at the coefficient level, or by direct computation with $\Phi(x) = K(1 - e^x)^+$ on $[a, 0]$:

$$
V_k^{\text{put}} = K\left[\psi_k(a, 0) - \chi_k(a, 0)\right]
$$

---

## Payoff Coefficients for Digital Options

A cash-or-nothing digital call pays $\$1$ if $S_T > K$ (i.e., $x > 0$):

$$
\Phi(x) = \mathbf{1}_{x > 0}
$$

The payoff coefficients are simply:

$$
V_k^{\text{digital}} = \psi_k(0, b)
$$

which has the closed form from the proposition above.

---

## Complete COS Algorithm

Combining all components, the COS pricing algorithm is:

**Input:** $\phi$ (characteristic function), $K$ (strike), $r$ (rate), $T$ (maturity), $N$ (number of terms), $[a, b]$ (truncation interval).

**Algorithm:**

1. Compute $\omega_k = k\pi/(b-a)$ for $k = 0, \ldots, N-1$
2. Compute density coefficients: $F_k = \frac{2}{b-a}\,\text{Re}[\phi(\omega_k)\,e^{-i\omega_k a}]$
3. Compute payoff coefficients: $V_k = K[\chi_k(0, b) - \psi_k(0, b)]$ for a call
4. Sum: $V_{\text{COS}} = e^{-rT}[\frac{1}{2}F_0 V_0 + \sum_{k=1}^{N-1} F_k V_k]$

**Complexity:** $N$ evaluations of $\phi$ (step 2) + $O(N)$ arithmetic (steps 1, 3, 4).

!!! tip "Multiple Strikes"
    For a fixed model (fixed $\phi$), the density coefficients $F_k$ are independent of the strike. To price options at multiple strikes, compute $F_k$ once and recompute only the payoff coefficients $V_k$ for each strike. The cost per additional strike is $O(N)$ arithmetic, with no additional CF evaluations.

---

## Example: Black--Scholes Verification

The COS method must reproduce the Black--Scholes formula exactly (up to truncation and series errors) when $\phi$ is the Black--Scholes characteristic function.

!!! example "COS vs Black--Scholes"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.10$, $\sigma = 0.25$, $T = 0.1$.

    The Black--Scholes call price is $C_{\text{BS}} = 3.6593$ (to four decimal places).

    The log-moneyness $x = \ln(S_T/K)$ has CF $\phi(u) = \exp(i(r - \sigma^2/2)Tu - \sigma^2 Tu^2/2)$.

    COS prices with truncation $[a,b] = [-1, 1]$:

    | $N$ | $V_{\text{COS}}$ | Error |
    |---|---|---|
    | 16 | 3.6593 | $< 10^{-4}$ |
    | 32 | 3.6593 | $< 10^{-8}$ |
    | 64 | 3.6593 | $< 10^{-12}$ |
    | 128 | 3.6593 | $< 10^{-15}$ |

    The exponential convergence is evident: each doubling of $N$ adds approximately 4 digits of accuracy. With $N = 64$, the COS price agrees with Black--Scholes to 12 decimal places.

---

## Example: Heston Model Pricing

For the Heston model, no closed-form option price exists, making the COS method a primary pricing tool.

!!! example "COS Pricing Under Heston"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0$, $T = 1$, $\kappa = 1.5768$, $\theta = 0.0398$, $\sigma_v = 0.5751$, $\rho = -0.5711$, $v_0 = 0.0175$.

    Using cumulant-based truncation with $L = 10$ and $N = 128$:

    $$
    V_{\text{COS}} = 5.7854
    $$

    This matches the semi-analytical Heston price (computed by numerical integration of the Heston formula) to 4 decimal places. Increasing to $N = 256$ gives agreement to 8 decimal places.

    The computation requires 128 evaluations of the Heston characteristic function (each involving the Riccati solution), plus $O(128)$ arithmetic for the payoff coefficients and summation. Total wall-clock time is typically under 1 millisecond.

---

## Put-Call Parity Check

A useful validation is to verify that COS call and put prices satisfy put-call parity:

$$
C_{\text{COS}} - P_{\text{COS}} = S_0 e^{-qT} - K e^{-rT}
$$

where $q$ is the dividend yield. Since the COS method approximates both $C$ and $P$ independently, checking this identity verifies that the truncation and series errors are consistent.

---

## Summary

The COS pricing formula combines density coefficients from the characteristic function with analytically computed payoff coefficients:

| Component | Formula | Source |
|---|---|---|
| Density coefficients $F_k$ | $\frac{2}{b-a}\,\text{Re}[\phi(k\pi/(b-a))\,e^{-ik\pi a/(b-a)}]$ | Characteristic function |
| Call payoff coefficients $V_k$ | $K[\chi_k(0,b) - \psi_k(0,b)]$ | Analytic integration |
| Put payoff coefficients $V_k$ | $K[\psi_k(a,0) - \chi_k(a,0)]$ | Analytic integration |
| Option price | $e^{-rT}\sum_{k=0}^{N-1}{}' F_k V_k$ | Summation |

**The COS pricing formula achieves exponential convergence for smooth densities, requires only $N$ characteristic function evaluations, and produces option prices accurate to machine precision with $N = 64$ to $128$ for typical affine models.**

---

## Exercises

**Exercise 1.** Derive the COS pricing formula $V_{\text{COS}} = e^{-rT}\sum_{k=0}^{N-1}{}' F_k V_k$ starting from the risk-neutral pricing identity $V = e^{-rT}\int_{-\infty}^{\infty}\Phi(x)f(x)\,dx$. Identify the three approximation steps (truncation to $[a, b]$, cosine expansion of $f$, exchange of sum and integral) and the error introduced by each step.

??? success "Solution to Exercise 1"
    **Step 1: Truncation to $[a, b]$.** Replace the infinite integration domain with a finite interval:

    $$
    V = e^{-rT}\int_{-\infty}^{\infty}\Phi(x)f(x)\,dx \approx e^{-rT}\int_a^b \Phi(x)f(x)\,dx
    $$

    Error: $\varepsilon_1 = e^{-rT}|\int_{\mathbb{R}\setminus[a,b]}\Phi(x)f(x)\,dx|$. This is the expected payoff from the density mass outside $[a, b]$, bounded by $e^{-rT}\mathbb{E}[|\Phi(X)|\mathbf{1}_{X \notin [a,b]}]$. With cumulant-based truncation ($L = 10$), $\varepsilon_1 < 10^{-15}$.

    **Step 2: Cosine expansion of $f$.** Replace $f(x)$ by its truncated cosine series:

    $$
    f(x) \approx \sum_{k=0}^{N-1}{}' F_k\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)
    $$

    Error: the series truncation error from dropping the terms $k \geq N$. This is $O(e^{-\beta N\pi/(b-a)})$ for analytic densities, giving $\varepsilon_2 \sim e^{-cN}$.

    **Step 3: Exchange of sum and integral.** Substituting the cosine expansion into the integral:

    $$
    \int_a^b \Phi(x)\sum_{k=0}^{N-1}{}' F_k\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx = \sum_{k=0}^{N-1}{}' F_k\int_a^b \Phi(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
    $$

    The exchange is justified because the finite sum of continuous functions converges uniformly on $[a, b]$. There is no additional error from this step (it is exact for the finite sum).

    Defining $V_k = \int_a^b \Phi(x)\cos(k\pi(x-a)/(b-a))\,dx$, we obtain:

    $$
    V_{\text{COS}} = e^{-rT}\sum_{k=0}^{N-1}{}' F_k\,V_k
    $$

    The total error is $|V - V_{\text{COS}}| \leq \varepsilon_1 + \varepsilon_2$, dominated by the series truncation error $\varepsilon_2$ in practice.

---

**Exercise 2.** Prove the closed-form expression for $\chi_k(c, d) = \int_c^d e^x\cos(\omega_k(x-a))\,dx$ using integration by parts twice. Show that $(1 + \omega_k^2)\chi_k(c,d) = [e^x(\cos(\omega_k(x-a)) + \omega_k\sin(\omega_k(x-a)))]_c^d$ and verify the formula for $k = 0$ (where $\omega_0 = 0$) reduces to $\chi_0(c,d) = e^d - e^c$.

??? success "Solution to Exercise 2"
    We need to compute $\chi_k(c,d) = \int_c^d e^x\cos(\omega_k(x-a))\,dx$ where $\omega_k = k\pi/(b-a)$.

    **First integration by parts.** Let $u = e^x$, $dv = \cos(\omega_k(x-a))\,dx$:

    - $du = e^x\,dx$
    - $v = \frac{1}{\omega_k}\sin(\omega_k(x-a))$

    $$
    \chi_k = \left[\frac{e^x\sin(\omega_k(x-a))}{\omega_k}\right]_c^d - \frac{1}{\omega_k}\int_c^d e^x\sin(\omega_k(x-a))\,dx
    $$

    **Second integration by parts.** For the remaining integral, let $u = e^x$, $dv = \sin(\omega_k(x-a))\,dx$:

    - $du = e^x\,dx$
    - $v = -\frac{1}{\omega_k}\cos(\omega_k(x-a))$

    $$
    \int_c^d e^x\sin(\omega_k(x-a))\,dx = \left[-\frac{e^x\cos(\omega_k(x-a))}{\omega_k}\right]_c^d + \frac{1}{\omega_k}\int_c^d e^x\cos(\omega_k(x-a))\,dx
    $$

    The last integral is $\chi_k$ itself. Substituting back:

    $$
    \chi_k = \left[\frac{e^x\sin(\omega_k(x-a))}{\omega_k}\right]_c^d - \frac{1}{\omega_k}\left(\left[-\frac{e^x\cos(\omega_k(x-a))}{\omega_k}\right]_c^d + \frac{1}{\omega_k}\chi_k\right)
    $$

    $$
    \chi_k = \left[\frac{e^x\sin(\omega_k(x-a))}{\omega_k}\right]_c^d + \left[\frac{e^x\cos(\omega_k(x-a))}{\omega_k^2}\right]_c^d - \frac{\chi_k}{\omega_k^2}
    $$

    Moving $\chi_k/\omega_k^2$ to the left:

    $$
    \chi_k\left(1 + \frac{1}{\omega_k^2}\right) = \left[\frac{e^x(\omega_k\sin(\omega_k(x-a)) + \cos(\omega_k(x-a)))}{\omega_k^2}\right]_c^d
    $$

    Multiplying both sides by $\omega_k^2/(1 + \omega_k^2)$:

    $$
    \chi_k = \frac{1}{1+\omega_k^2}\left[e^x\left(\cos(\omega_k(x-a)) + \omega_k\sin(\omega_k(x-a))\right)\right]_c^d
    $$

    **Verification for $k = 0$:** When $k = 0$, $\omega_0 = 0$, and $\cos(0) = 1$, $\sin(0) = 0$. The formula gives:

    $$
    \chi_0(c,d) = \frac{1}{1+0}\left[e^x(1 + 0)\right]_c^d = e^d - e^c
    $$

    which is simply $\int_c^d e^x\,dx = e^d - e^c$. Correct.

---

**Exercise 3.** For a European put with payoff $\Phi(x) = K(1 - e^x)^+$ on $[a, 0]$, derive the payoff coefficients $V_k^{\text{put}} = K[\psi_k(a, 0) - \chi_k(a, 0)]$. Verify that the put-call parity relation $V_k^{\text{call}} - V_k^{\text{put}} = K[\chi_k(a, b) - \psi_k(a, b)]$ holds at the coefficient level.

??? success "Solution to Exercise 3"
    The European put payoff is $\Phi(x) = K(1 - e^x)^+ = K(1 - e^x)$ for $x \leq 0$ and $0$ for $x > 0$.

    The payoff coefficients are:

    $$
    V_k^{\text{put}} = \int_a^b K(1 - e^x)^+\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx = K\int_a^0 (1 - e^x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
    $$

    (assuming $a < 0 < b$). Splitting:

    $$
    V_k^{\text{put}} = K\left[\int_a^0\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx - \int_a^0 e^x\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx\right]
    $$

    $$
    = K\left[\psi_k(a, 0) - \chi_k(a, 0)\right]
    $$

    **Put-call parity at the coefficient level.** We have:

    $$
    V_k^{\text{call}} - V_k^{\text{put}} = K[\chi_k(0,b) - \psi_k(0,b)] - K[\psi_k(a,0) - \chi_k(a,0)]
    $$

    $$
    = K[\chi_k(0,b) + \chi_k(a,0) - \psi_k(0,b) - \psi_k(a,0)]
    $$

    Since $\chi_k$ and $\psi_k$ are integrals over disjoint subintervals that partition $[a, b]$ (for $a < 0 < b$):

    $$
    \chi_k(a,0) + \chi_k(0,b) = \chi_k(a,b), \quad \psi_k(a,0) + \psi_k(0,b) = \psi_k(a,b)
    $$

    Therefore:

    $$
    V_k^{\text{call}} - V_k^{\text{put}} = K[\chi_k(a,b) - \psi_k(a,b)]
    $$

    This is the coefficient-level put-call parity: the difference of call and put payoff coefficients equals the coefficients of $K(e^x - 1)$ integrated over the full interval $[a, b]$.

---

**Exercise 4.** For a cash-or-nothing digital call with payoff $\Phi(x) = \mathbf{1}_{x > 0}$, the payoff coefficients are $V_k^{\text{digital}} = \psi_k(0, b)$. Compute $V_0^{\text{digital}}$, $V_1^{\text{digital}}$, and $V_2^{\text{digital}}$ for $[a, b] = [-1, 1]$. How do the coefficient magnitudes compare to those of a vanilla call?

??? success "Solution to Exercise 4"
    For $[a, b] = [-1, 1]$, we have $b - a = 2$ and $\omega_k = k\pi/2$.

    **$V_0^{\text{digital}}$:** Using $\psi_0(0, b) = d - c = b - 0 = 1$.

    $$
    V_0^{\text{digital}} = 1
    $$

    **$V_1^{\text{digital}}$:** With $\omega_1 = \pi/2$:

    $$
    V_1^{\text{digital}} = \psi_1(0, 1) = \frac{b-a}{1\cdot\pi}[\sin(\omega_1(1-a)) - \sin(\omega_1(0-a))]
    $$

    $$
    = \frac{2}{\pi}[\sin(\pi/2\cdot 2) - \sin(\pi/2\cdot 1)] = \frac{2}{\pi}[\sin(\pi) - \sin(\pi/2)] = \frac{2}{\pi}[0 - 1] = -\frac{2}{\pi} \approx -0.6366
    $$

    **$V_2^{\text{digital}}$:** With $\omega_2 = \pi$:

    $$
    V_2^{\text{digital}} = \frac{2}{2\pi}[\sin(\pi(1-(-1))) - \sin(\pi(0-(-1)))] = \frac{1}{\pi}[\sin(2\pi) - \sin(\pi)] = \frac{1}{\pi}[0 - 0] = 0
    $$

    **Comparison to vanilla call:** For a vanilla call, $V_k^{\text{call}} = K[\chi_k(0,b) - \psi_k(0,b)]$. The $\chi_k$ term involves $e^x$, which grows with $x$, making $|V_k^{\text{call}}|$ generally larger than $|V_k^{\text{digital}}|$. Moreover, the call payoff $(e^x - 1)^+$ is unbounded while the digital payoff is bounded by 1, so the call coefficients have larger magnitudes. However, both sequences decay as $O(1/k^2)$ for large $k$ because both payoff functions have a kink (discontinuity in derivative) at $x = 0$. The digital payoff actually has a jump discontinuity at $x = 0$, leading to even slower coefficient decay of $O(1/k)$, meaning more COS terms are needed for the same accuracy.

---

**Exercise 5.** In the Black-Scholes verification example ($S_0 = 100$, $K = 100$, $r = 0.10$, $\sigma = 0.25$, $T = 0.1$), the COS method achieves $10^{-12}$ accuracy with $N = 64$. Each doubling of $N$ adds approximately 4 digits of accuracy. Explain this super-exponential convergence in terms of the Gaussian decay of the cosine coefficients $|A_k| \sim e^{-ck^2}$.

??? success "Solution to Exercise 5"
    Under Black--Scholes, the log-price density is Gaussian: $f(x) \propto e^{-x^2/(2\sigma^2 T)}$. The Gaussian is an entire function (analytic everywhere in the complex plane), so the analyticity strip width $\beta = \infty$. However, the convergence rate is not simply $e^{-\beta N\pi/(b-a)}$ with $\beta = \infty$ (which would be trivially zero). Instead, the appropriate decay analysis uses the specific Gaussian form.

    The cosine coefficients of a Gaussian on $[-L\sigma\sqrt{T}, L\sigma\sqrt{T}]$ decay as:

    $$
    |A_k| \sim e^{-\sigma^2 T k^2\pi^2/(2(b-a)^2)} = e^{-ck^2}
    $$

    where $c = \sigma^2 T\pi^2/(2(b-a)^2)$. This is **super-exponential** (Gaussian decay in $k$), meaning the error decreases as $\varepsilon_2 \sim e^{-cN^2}$, not merely $e^{-cN}$.

    **Estimating $c$ from the data:** With $\varepsilon_2 \sim e^{-cN^2}$:

    - $N = 8$: $\varepsilon_2 \approx 10^{-3}$, so $-64c \approx -3\ln 10$, giving $c \approx 0.108$
    - $N = 16$: $\varepsilon_2 \approx 10^{-6}$, so $-256c \approx -6\ln 10$, giving $c \approx 0.054$
    - $N = 32$: $\varepsilon_2 \approx 10^{-11}$, so $-1024c \approx -11\ln 10$, giving $c \approx 0.0247$

    The estimates are not constant because the actual error includes sub-leading terms and the payoff coefficients also contribute. However, the key signature of super-exponential convergence is that each doubling of $N$ (quadrupling $N^2$) more than doubles the number of correct digits: from $N = 8$ to $16$, we gain 3 digits; from $16$ to $32$, we gain 5 digits; from $32$ to $64$, we gain more than 4 digits. This accelerating gain is the hallmark of $e^{-cN^2}$ decay, in contrast to exponential decay $e^{-cN}$ which adds a fixed number of digits per doubling.

---

**Exercise 6.** The COS method allows pricing at multiple strikes with a single set of density coefficients $F_k$. If pricing at 100 strikes with $N = 128$ using COS requires 128 CF evaluations plus $100 \times 128$ arithmetic operations, compare the total cost to Carr-Madan FFT pricing with $N_{\text{FFT}} = 4096$. Under what conditions does COS become more expensive than FFT for a strike grid?

---

??? success "Solution to Exercise 6"
    **COS method cost for 100 strikes:**

    - CF evaluations: 128 (computed once, shared across all strikes)
    - Payoff coefficient computation: $100 \times 128 = 12{,}800$ operations (each strike requires recomputing $V_k$ for $k = 0, \ldots, 127$)
    - Summation: $100 \times 128 = 12{,}800$ multiply-accumulate operations
    - Total: 128 CF evaluations + 25,600 arithmetic operations

    **Carr--Madan FFT cost:**

    - CF evaluations: $N_{\text{FFT}} = 4{,}096$ (one per FFT grid point)
    - FFT computation: $O(N_{\text{FFT}}\log N_{\text{FFT}}) = O(4096 \times 12) \approx 49{,}152$ operations
    - Output: prices at all $N_{\text{FFT}}$ log-strike points simultaneously (interpolation needed for specific strikes)
    - Total: 4,096 CF evaluations + $\sim$49,152 operations

    **Comparison:** The COS method requires 128 CF evaluations vs. 4,096 for FFT---a factor of 32 fewer. Since CF evaluations (especially for the Heston model) are the expensive step, COS is much cheaper for 100 strikes.

    **When COS becomes more expensive:** The COS method's CF cost is fixed at $N = 128$, but its arithmetic cost grows linearly with the number of strikes $M$: total $= 128\text{ CF evals} + O(128M)$ arithmetic. The FFT provides prices at all $N_{\text{FFT}}$ strikes simultaneously with cost $N_{\text{FFT}}\text{ CF evals} + O(N_{\text{FFT}}\log N_{\text{FFT}})$ arithmetic.

    The COS method becomes more expensive than FFT when $128 + 128M \times \alpha > 4096 + 4096\times 12\times\alpha$, where $\alpha$ is the ratio of arithmetic cost to CF evaluation cost. If CF evaluations dominate ($\alpha \ll 1$), COS is always cheaper for any reasonable $M$. If arithmetic is comparably expensive, COS becomes costlier when $M > N_{\text{FFT}}/N_{\text{COS}} = 4096/128 = 32$ strikes approximately. In practice, COS is preferred for up to several hundred strikes, while FFT is preferred when prices at thousands of strikes are needed simultaneously (e.g., for implied volatility surface calibration).
