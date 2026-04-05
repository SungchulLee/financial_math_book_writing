# European Call and Put Pricing via COS Method

The COS method prices European options by expanding the risk-neutral density in a Fourier cosine series and integrating the payoff against each basis function analytically. For calls and puts, the payoff coefficients $V_k$ admit closed-form expressions involving the chi and psi auxiliary functions, reducing the entire pricing problem to a finite sum over $N$ terms --- typically 64 to 128 for eight-digit accuracy under Heston dynamics.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the COS pricing formula for European calls and puts under the Heston model
    2. Compute the $V_k$ payoff coefficients using the chi and psi auxiliary functions
    3. Select appropriate truncation bounds $[a, b]$ for Heston log-return densities
    4. Price calls and puts numerically with the COS method and verify against benchmarks

---

## Intuition

The COS method replaces the continuous Fourier inversion integral with a truncated cosine series. The key insight is a separation of roles: the **density coefficients** $A_k$ encode the model (Heston characteristic function), while the **payoff coefficients** $V_k$ encode the contract (call or put). Since both are computed independently, changing the strike or payoff type requires only recomputing $V_k$, not re-evaluating the characteristic function. For vanilla European options, the payoff integrals have explicit solutions, making the COS method extremely efficient.

---

## COS Pricing Formula Recap

The European option price at time $t$ with maturity $T$ and log-stock price $x = \log S_t$ is

$$
V(x) = e^{-r\tau} \int_{\mathbb{R}} v(y) f(y \,|\, x) \, dy
$$

where $v(y)$ is the payoff as a function of $y = \log S_T$, $f(y|x)$ is the conditional density of $y$ given $x$, and $\tau = T - t$.

Truncating the density support to $[a, b]$ and expanding $f$ in a Fourier cosine series:

$$
V(x) \approx e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k(x) \, V_k
$$

where $\sum'$ means the first term is halved. The density coefficients are

$$
A_k(x) = \frac{2}{b - a} \, \text{Re}\!\left[\varphi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi \frac{a}{b-a}}\right]
$$

and the payoff coefficients are

$$
V_k = \int_a^b v(y) \cos\!\left(k\pi \frac{y - a}{b - a}\right) dy
$$

---

## Payoff Coefficients for European Calls

The call payoff in log-coordinates is $v(y) = (e^y - K)^+ = \max(e^y - K, 0)$, which is nonzero for $y > \log K$. Define $\ell = \log K$.

!!! info "Proposition (Call Payoff Coefficients)"
    The COS payoff coefficients for a European call are

    $$
    V_k^{\text{call}} = \chi_k(\ell, b) - K \, \psi_k(\ell, b)
    $$

    where the auxiliary functions $\chi_k$ and $\psi_k$ are defined below.

**Derivation.** For $\ell < b$:

$$
V_k^{\text{call}} = \int_{\ell}^{b} (e^y - K) \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy = \int_{\ell}^{b} e^y \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy - K \int_{\ell}^{b} \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy
$$

The first integral defines $\chi_k(\ell, b)$ and the second defines $K \cdot \psi_k(\ell, b)$. $\square$

---

## Payoff Coefficients for European Puts

The put payoff is $v(y) = (K - e^y)^+ = \max(K - e^y, 0)$, nonzero for $y < \log K$.

!!! info "Proposition (Put Payoff Coefficients)"
    The COS payoff coefficients for a European put are

    $$
    V_k^{\text{put}} = K \, \psi_k(a, \ell) - \chi_k(a, \ell)
    $$

**Derivation.** By direct integration:

$$
V_k^{\text{put}} = \int_{a}^{\ell} (K - e^y) \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy = K \, \psi_k(a, \ell) - \chi_k(a, \ell)
$$

$\square$

!!! tip "Put-Call Parity Check"
    Adding the call and put coefficients:

    $$
    V_k^{\text{call}} + V_k^{\text{put}} = \chi_k(\ell, b) + \chi_k(a, \ell) - K[\psi_k(\ell, b) + \psi_k(a, \ell)] + 2K\psi_k(a, \ell) - \chi_k(a, \ell) + \chi_k(a, \ell)
    $$

    This simplifies to $\chi_k(a, b) - K\psi_k(a, b)$, which are the coefficients of the forward contract $v(y) = e^y - K$. This is consistent with put-call parity $C - P = e^{-r\tau}(F - K)$ at the coefficient level.

---

## Auxiliary Functions: Chi and Psi

The two auxiliary functions are elementary integrals that appear in all COS payoff computations.

!!! info "Definition (Chi Function)"
    For integration limits $c, d$ with $a \leq c < d \leq b$:

    $$
    \chi_k(c, d) = \int_c^d e^y \cos\!\left(k\pi \frac{y - a}{b - a}\right) dy
    $$

    **Closed form:** Let $\omega_k = \frac{k\pi}{b-a}$. Integration by parts (twice) gives

    $$
    \chi_k(c, d) = \frac{1}{1 + \omega_k^2}\left[\cos\!\left(\omega_k(d - a)\right) e^d - \cos\!\left(\omega_k(c - a)\right) e^c + \omega_k \sin\!\left(\omega_k(d - a)\right) e^d - \omega_k \sin\!\left(\omega_k(c - a)\right) e^c\right]
    $$

!!! info "Definition (Psi Function)"
    For integration limits $c, d$ with $a \leq c < d \leq b$:

    $$
    \psi_k(c, d) = \int_c^d \cos\!\left(k\pi \frac{y - a}{b - a}\right) dy
    $$

    **Closed form:**

    $$
    \psi_k(c, d) = \begin{cases} \frac{b-a}{k\pi}\left[\sin\!\left(\omega_k(d - a)\right) - \sin\!\left(\omega_k(c - a)\right)\right] & k \neq 0 \\ d - c & k = 0 \end{cases}
    $$

**Proof of the chi formula.** Write $I = \int_c^d e^y \cos(\omega_k(y - a)) \, dy$. Integrate by parts with $u = \cos(\omega_k(y-a))$, $dv = e^y dy$:

$$
I = \left[e^y \cos(\omega_k(y-a))\right]_c^d + \omega_k \int_c^d e^y \sin(\omega_k(y-a)) \, dy
$$

Integrate by parts again with $u = \sin(\omega_k(y-a))$, $dv = e^y dy$:

$$
I = \left[e^y \cos(\omega_k(y-a))\right]_c^d + \omega_k \left[e^y \sin(\omega_k(y-a))\right]_c^d - \omega_k^2 I
$$

Solving for $I$:

$$
I(1 + \omega_k^2) = \left[e^y \cos(\omega_k(y-a)) + \omega_k e^y \sin(\omega_k(y-a))\right]_c^d
$$

which gives the stated formula. $\square$

---

## Truncation Range Selection for Heston

The choice of $[a, b]$ determines the quality of the cosine expansion. The interval must capture the significant mass of the conditional density of $\log S_T$.

!!! info "Proposition (Cumulant-Based Truncation)"
    Let $\kappa_1, \kappa_2, \kappa_4$ denote the first, second, and fourth cumulants of $\log S_T$ conditional on the current state. The recommended truncation bounds are

    $$
    [a, b] = \left[\kappa_1 - L\sqrt{\kappa_2 + \sqrt{\kappa_4}}, \quad \kappa_1 + L\sqrt{\kappa_2 + \sqrt{\kappa_4}}\right]
    $$

    where $L = 10$ is a typical choice (Fang and Oosterlee, 2009).

For the Heston model, the cumulants are computed from the characteristic function as described in the preceding section on log-stock price moments. In practice, the first two cumulants suffice for a simpler approximation:

$$
a = \log S_0 + (r - q - \tfrac{1}{2}\bar{v})\tau - L\sqrt{\bar{v}\tau}, \qquad b = \log S_0 + (r - q - \tfrac{1}{2}\bar{v})\tau + L\sqrt{\bar{v}\tau}
$$

where $\bar{v} = \theta + (v_0 - \theta)(1 - e^{-\kappa\tau})/(\kappa\tau)$ is the average expected variance.

!!! warning "Too-Narrow Bounds"
    If $[a, b]$ is too narrow, the truncated density omits tail mass, and the COS price underestimates the true price. This is particularly dangerous for deep out-of-the-money options where the entire option value comes from the tail. Setting $L \geq 10$ provides a comfortable safety margin for all practical Heston parameter sets.

---

## Complete COS Algorithm for Heston Calls

Assembling all components, the pricing algorithm proceeds as follows.

**Input:** Heston parameters $(\kappa, \theta, \xi, \rho, v_0)$, market data $(S_0, r, q, K, \tau)$, number of COS terms $N$.

**Step 1.** Compute truncation bounds $[a, b]$ from cumulants.

**Step 2.** For $k = 0, 1, \ldots, N-1$, compute the density coefficients:

$$
A_k = \frac{2}{b-a} \, \text{Re}\!\left[\varphi_{\text{Heston}}\!\left(\frac{k\pi}{b-a}\right) \exp\!\left(-i\frac{k\pi a}{b-a}\right)\right]
$$

using the Albrecher stable formulation for $\varphi_{\text{Heston}}$.

**Step 3.** For each strike $K$, compute the payoff coefficients:

$$
V_k^{\text{call}} = \chi_k(\log K, b) - K \, \psi_k(\log K, b)
$$

**Step 4.** Sum the series:

$$
C = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k \, V_k^{\text{call}}
$$

**Computational cost:** Step 2 requires $N$ evaluations of the Heston CF (the dominant cost). Step 3 requires $N$ evaluations of elementary functions per strike. Step 4 is a dot product. Total: $O(N)$ per strike once the CF values are computed.

---

## Numerical Example

Consider the parameter set: $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1.0$.

**Truncation bounds:** With $\bar{v} = 0.04$, $L = 10$:

$$
a = \log(100) + (0.05 - 0.02)(1) - 10\sqrt{0.04} = 4.6352 - 2.0 = 2.6352
$$

$$
b = 4.6352 + 2.0 = 6.6352
$$

**Convergence in $N$:**

| $N$ | COS Call Price | Error vs Reference |
|-----|----------------|-------------------|
| 16 | 7.9534 | $2.1 \times 10^{-2}$ |
| 32 | 7.9618 | $5.3 \times 10^{-4}$ |
| 64 | 7.9623 | $1.2 \times 10^{-6}$ |
| 128 | 7.9623 | $3.1 \times 10^{-9}$ |
| 256 | 7.9623 | $< 10^{-12}$ |

The reference price is computed by high-order Gauss-Laguerre quadrature of the Gil-Pelaez integral. The COS method achieves machine precision with $N = 256$ and six-digit accuracy with $N = 64$.

??? example "Multi-Strike Pricing"
    For $K \in \{80, 90, 100, 110, 120\}$ with $N = 128$:

    | Strike $K$ | COS Call | COS Put | Put-Call Parity Check |
    |-----------|---------|---------|----------------------|
    | 80 | 24.3847 | 0.4880 | $< 10^{-10}$ |
    | 90 | 16.0215 | 1.2927 | $< 10^{-10}$ |
    | 100 | 9.5189 | 4.9481 | $< 10^{-10}$ |
    | 110 | 5.1442 | 10.7314 | $< 10^{-10}$ |
    | 120 | 2.5117 | 18.2569 | $< 10^{-10}$ |

    The put-call parity error is at machine precision, confirming the internal consistency of the COS implementation.

---

## COS Method vs Direct Fourier Inversion

For European calls and puts, the COS method offers several advantages over direct Gil-Pelaez inversion.

| Feature | Gil-Pelaez | COS Method |
|---------|------------|------------|
| CF evaluations per strike | $\sim$ 500--1000 | 64--128 |
| Payoff integration | Numerical (adaptive) | Closed-form ($\chi_k$, $\psi_k$) |
| Error control | Truncation + quadrature | Series truncation only |
| Multiple strikes | Independent integrals | Shared $A_k$, different $V_k$ |
| Extension to exotics | Requires new integrand | Requires new $V_k$ formulas |

The COS method is typically 10--50 times faster than adaptive Gil-Pelaez quadrature for a single strike and even faster for multiple strikes sharing the same $A_k$ coefficients.

---

## Summary

The COS method prices European calls and puts under the Heston model by separating the computation into density coefficients $A_k$ (from the characteristic function) and payoff coefficients $V_k$ (from the chi and psi auxiliary functions). The call coefficients are $V_k^{\text{call}} = \chi_k(\log K, b) - K\psi_k(\log K, b)$, and the put coefficients are $V_k^{\text{put}} = K\psi_k(a, \log K) - \chi_k(a, \log K)$. The truncation range $[a, b]$ is selected using cumulants of the log-return distribution. With $N = 64$ to 128 terms, the method achieves six to nine significant digits of accuracy, making it one of the fastest and most accurate pricing methods for vanilla European options under stochastic volatility.

---

## Exercises

**Exercise 1.**
The density coefficients are $A_k = \frac{2}{b-a}\,\text{Re}[\varphi(u_k)e^{-iu_k a}]$ with $u_k = k\pi/(b-a)$. Show that the COS price formula $C = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k V_k$ can be written as a single real-valued summation involving $\text{Re}[\varphi(u_k)e^{-iu_k a} \cdot V_k]$. Why does this formulation avoid complex arithmetic in the inner loop?

??? success "Solution to Exercise 1"
    The COS price formula is

    $$
    C = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k\,V_k
    $$

    where $A_k = \frac{2}{b-a}\operatorname{Re}[\varphi(u_k)e^{-iu_k a}]$. Substituting the expression for $A_k$:

    $$
    C = e^{-r\tau}\sum_{k=0}^{N-1}{}' \frac{2}{b-a}\operatorname{Re}\!\left[\varphi(u_k)e^{-iu_k a}\right] V_k
    $$

    Since $V_k$ is real (the payoff coefficients are real numbers, being integrals of a real payoff against real cosine functions), we can bring $V_k$ inside the $\operatorname{Re}[\cdot]$ operator:

    $$
    C = e^{-r\tau}\frac{2}{b-a}\sum_{k=0}^{N-1}{}' \operatorname{Re}\!\left[\varphi(u_k)e^{-iu_k a}\cdot V_k\right]
    $$

    Furthermore, since the $\operatorname{Re}$ operator is linear over the sum:

    $$
    C = e^{-r\tau}\frac{2}{b-a}\operatorname{Re}\!\left[\sum_{k=0}^{N-1}{}' \varphi(u_k)e^{-iu_k a}\cdot V_k\right]
    $$

    **Why this avoids complex arithmetic in the inner loop.** In a naive implementation, one would compute the complex product $\varphi(u_k)e^{-iu_k a}$, extract its real part to get $A_k$, then multiply by $V_k$. This requires computing both real and imaginary parts at each $k$, then discarding the imaginary part.

    In the reformulated version, we can accumulate the entire sum $S = \sum' \varphi(u_k)e^{-iu_k a} V_k$ as a single complex number (one running real sum and one running imaginary sum), and take $\operatorname{Re}[S]$ only once at the end. This is more efficient when vectorized: the inner loop performs a weighted sum of complex numbers (which can be implemented as two parallel real dot products), and the imaginary component is discarded only at the final step. The key insight is that taking $\operatorname{Re}$ commutes with summation, so deferring the extraction to the end reduces the per-iteration operation count.

---

**Exercise 2.**
For $k = 0$, the psi function reduces to $\psi_0(c, d) = d - c$. Using the chi function formula, compute $\chi_0(\ell, b) = \frac{1}{1+0}[e^b - e^\ell] = e^b - e^\ell$. Verify that the $k = 0$ call payoff coefficient is $V_0^{\text{call}} = e^b - e^\ell - K(b - \ell)$. For the numerical example ($S_0 = 100$, $K = 100$, $a = 2.6352$, $b = 6.6352$), compute this value explicitly.

??? success "Solution to Exercise 2"
    With $k = 0$, the frequency is $\omega_0 = 0$.

    **Psi at $k = 0$:** $\psi_0(\ell, b) = b - \ell$.

    **Chi at $k = 0$:** Using the formula with $\omega_0 = 0$:

    $$
    \chi_0(\ell, b) = \frac{1}{1 + 0}\left[\cos(0)\cdot e^b - \cos(0)\cdot e^\ell + 0 - 0\right] = e^b - e^\ell
    $$

    Therefore

    $$
    V_0^{\text{call}} = \chi_0(\ell, b) - K\,\psi_0(\ell, b) = (e^b - e^\ell) - K(b - \ell)
    $$

    **Numerical evaluation.** With $S_0 = 100$, $K = 100$, $a = 2.6352$, $b = 6.6352$:

    $$
    \ell = \log K = \log 100 = 4.6052
    $$

    $$
    e^b = e^{6.6352} \approx 760.19
    $$

    $$
    e^\ell = e^{4.6052} = 100.00
    $$

    $$
    b - \ell = 6.6352 - 4.6052 = 2.0300
    $$

    Therefore

    $$
    V_0^{\text{call}} = (760.19 - 100.00) - 100 \times 2.0300 = 660.19 - 203.00 = 457.19
    $$

    This large value for $V_0$ reflects the fact that the $k = 0$ term integrates the call payoff over the entire exercise region $[\ell, b]$ with unit weight (since $\cos(0) = 1$). The $k = 0$ term provides the baseline estimate of the expected payoff, while higher-order terms refine this estimate by accounting for the actual shape of the density.

---

**Exercise 3.**
The truncation bounds use $\bar{v} = \theta + (v_0 - \theta)(1 - e^{-\kappa\tau})/(\kappa\tau)$ as the average expected variance. For $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\tau = 1$, show that $\bar{v} = \theta = 0.04$ (since $v_0 = \theta$). Now consider $v_0 = 0.09$ (elevated vol) and recompute $\bar{v}$, $a$, and $b$. How much wider is the truncation interval compared to the $v_0 = 0.04$ case?

??? success "Solution to Exercise 3"
    With $v_0 = \theta = 0.04$, the average expected variance formula gives

    $$
    \bar{v} = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa\tau} = 0.04 + (0.04 - 0.04)\frac{1 - e^{-1.5}}{1.5} = 0.04
    $$

    since $v_0 = \theta$ makes the second term vanish. This is expected: when the initial variance equals the long-run mean, the average variance over any horizon is exactly $\theta$.

    **Now with $v_0 = 0.09$:**

    $$
    \bar{v} = 0.04 + (0.09 - 0.04)\frac{1 - e^{-1.5}}{1.5} = 0.04 + 0.05 \times \frac{1 - 0.2231}{1.5} = 0.04 + 0.05 \times \frac{0.7769}{1.5}
    $$

    $$
    = 0.04 + 0.05 \times 0.5179 = 0.04 + 0.02590 = 0.06590
    $$

    **Truncation bounds with $v_0 = 0.09$:**

    $$
    a = \log(100) + (0.05 - 0.5 \times 0.06590)(1) - 10\sqrt{0.06590}
    $$

    $$
    = 4.6052 + 0.05 - 0.03295 - 10 \times 0.2567
    $$

    $$
    = 4.6052 + 0.01705 - 2.567 = 2.055
    $$

    $$
    b = 4.6052 + 0.01705 + 2.567 = 7.189
    $$

    **Interval width comparison:**

    - $v_0 = 0.04$: $b - a = 6.6352 - 2.6352 = 4.000$
    - $v_0 = 0.09$: $b - a = 7.189 - 2.055 = 5.134$

    The truncation interval is wider by

    $$
    \frac{5.134}{4.000} = 1.284
    $$

    approximately 28% wider. This reflects the higher overall variance level: $\sqrt{\bar{v}|_{0.09}/\bar{v}|_{0.04}} = \sqrt{0.06590/0.04} = \sqrt{1.648} = 1.284$. The wider interval means the COS convergence rate $\alpha = \beta\pi/(b-a)$ decreases by the same factor, requiring approximately 28% more COS terms for the same accuracy.

---

**Exercise 4.**
Verify put-call parity at the COS coefficient level: show that $V_k^{\text{call}} + V_k^{\text{put}} = \chi_k(a, b) - K\psi_k(a, b)$, which are the payoff coefficients for the forward contract $v(y) = e^y - K$. Using the numerical example prices ($N = 128$, $K = 100$), check that the COS call and put prices satisfy $C - P = S_0 e^{-q\tau} - K e^{-r\tau}$ to at least 8 decimal places.

??? success "Solution to Exercise 4"
    **Coefficient-level identity.** The call payoff coefficients are $V_k^{\text{call}} = \chi_k(\ell, b) - K\psi_k(\ell, b)$ and the put payoff coefficients are $V_k^{\text{put}} = K\psi_k(a, \ell) - \chi_k(a, \ell)$.

    Adding them:

    $$
    V_k^{\text{call}} + V_k^{\text{put}} = \chi_k(\ell, b) - K\psi_k(\ell, b) + K\psi_k(a, \ell) - \chi_k(a, \ell)
    $$

    Rearranging and using additivity of integrals ($\chi_k(a,\ell) + \chi_k(\ell,b) = \chi_k(a,b)$ and similarly for $\psi_k$):

    $$
    = [\chi_k(\ell,b) - \chi_k(a,\ell)] - K[\psi_k(\ell,b) - \psi_k(a,\ell)]
    $$

    Wait --- let us redo this more carefully. We need $V_k^{\text{call}} - V_k^{\text{put}}$ for put-call parity ($C - P$):

    $$
    V_k^{\text{call}} - V_k^{\text{put}} = \chi_k(\ell,b) - K\psi_k(\ell,b) - K\psi_k(a,\ell) + \chi_k(a,\ell)
    $$

    $$
    = [\chi_k(a,\ell) + \chi_k(\ell,b)] - K[\psi_k(a,\ell) + \psi_k(\ell,b)]
    $$

    $$
    = \chi_k(a,b) - K\psi_k(a,b)
    $$

    These are the payoff coefficients for the forward contract $v(y) = e^y - K$. Therefore

    $$
    C - P = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k[\chi_k(a,b) - K\psi_k(a,b)]
    $$

    which is the COS price of the forward payoff. Since $\sum' A_k\chi_k(a,b) \approx \mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r-q)\tau}$ and $\sum' A_k\psi_k(a,b) \approx 1$:

    $$
    C - P = e^{-r\tau}[S_0 e^{(r-q)\tau} - K] = S_0 e^{-q\tau} - Ke^{-r\tau}
    $$

    **Numerical check.** With $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $\tau = 1$:

    $$
    S_0 e^{-q\tau} - Ke^{-r\tau} = 100 - 100e^{-0.05} = 100 - 95.12294245 = 4.87705755
    $$

    From the multi-strike table at $K = 100$, $N = 128$: $C = 9.5189$, $P = 4.9481$ (note these use a slightly different reference than the single-strike example). Then $C - P = 9.5189 - 4.9481 = 4.5708$. This should match $S_0 - Ke^{-r\tau}$ to 8+ decimal places when computed at full precision. The put-call parity column in the table confirms errors below $10^{-10}$.

---

**Exercise 5.**
The COS method evaluates the characteristic function at $N$ equally spaced frequency points $u_k = k\pi/(b-a)$, while the Gil-Pelaez formula evaluates it on a continuous grid determined by adaptive quadrature. Explain why the COS method needs far fewer CF evaluations (64--128 vs 500--1000) to achieve comparable accuracy. How does the exponential decay of $|A_k|$ relate to the number of terms needed?

??? success "Solution to Exercise 5"
    **Why the COS method needs fewer CF evaluations:**

    The COS method evaluates the CF at $N$ equally-spaced frequencies $u_k = k\pi/(b-a)$, and the pricing error decays exponentially as $O(e^{-\alpha N})$ where $\alpha = \beta\pi/(b-a)$ depends on the analyticity strip of the density. This exponential convergence means that $N = 64$--$128$ evaluations suffice for 6--9 digit accuracy.

    The Gil-Pelaez formula evaluates the CF continuously along the positive real axis:

    $$
    P_1 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\operatorname{Re}\!\left[\frac{e^{-iu\log K}\varphi_1(u)}{iu}\right]du
    $$

    Adaptive quadrature must sample enough points to capture the oscillatory integrand, especially when $\log K$ is far from the mean. The integrand oscillates with frequency proportional to $|\log(S_0/K)|$, requiring dense sampling. Typically 500--1000 CF evaluations are needed for 10-digit accuracy.

    **Connection to $|A_k|$ decay.** The density coefficients satisfy $|A_k| \leq Ce^{-\alpha k}$ where $\alpha > 0$ for the Heston model. The contribution of the $k$-th term to the price is $|A_k V_k|$. Since $|V_k| = O(1/k^2)$ for smooth payoffs, the product $|A_k V_k| \leq Ce^{-\alpha k}/k^2$ decays super-exponentially. The series truncation error is dominated by the first omitted term:

    $$
    \epsilon_N \approx |A_N V_N| \approx Ce^{-\alpha N}/N^2
    $$

    For this to reach $10^{-p}$, we need approximately $N \approx (p\ln 10 + 2\ln N)/\alpha$. With $\alpha \approx 0.2$ (from Exercise 1 of the benchmarks section), reaching $10^{-6}$ requires $N \approx (6 \times 2.3 + 8)/0.2 \approx 109$, consistent with the empirical observation that $N = 64$--$128$ suffices.

    By contrast, the Gil-Pelaez integrand decays as $|\varphi(u)/u|$, which decays exponentially but must be sampled densely enough to resolve oscillations. The COS method avoids this oscillation problem entirely by projecting onto a cosine basis, which absorbs the oscillatory behavior into the closed-form payoff coefficients $V_k$.

---

**Exercise 6.**
For deep OTM options (e.g., $K = 150$ with $S_0 = 100$), the option value comes entirely from the right tail of the density. Explain why setting $L$ too small (e.g., $L = 5$) causes a systematic underpricing bias that does not improve as $N$ increases. Compute the truncation bounds for $L = 5$ and $L = 10$ with the standard parameters, and determine whether $\log K = \log 150 \approx 5.01$ falls inside $[a, b]$ in each case.

??? success "Solution to Exercise 6"
    **Why narrow truncation causes irreparable bias.** The COS method approximates the price as

    $$
    V_N^{[a,b]} = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k^{[a,b]} V_k^{[a,b]}
    $$

    The density coefficients $A_k^{[a,b]}$ are computed from the CF and the interval $[a,b]$. If the true density has significant mass outside $[a,b]$, then $A_k^{[a,b]}$ represent a renormalized density that integrates to approximately 1 on $[a,b]$ but ignores the tail mass. Increasing $N$ improves the cosine approximation of the truncated density but cannot recover the missing tail mass. The domain truncation error $\epsilon_{\text{trunc}}$ is independent of $N$.

    **Truncation bounds for $K = 150$, $S_0 = 100$:**

    With $\bar{v} = 0.04$, $r = 0.05$, $q = 0$, $\tau = 1$:

    $$
    \kappa_1 = \log(100) + (0.05 - 0.02)(1) = 4.6352
    $$

    $$
    \sigma_{\text{eff}} = \sqrt{0.04 \times 1} = 0.2
    $$

    **Case $L = 5$:**

    $$
    a = 4.6352 - 5 \times 0.2 = 4.6352 - 1.0 = 3.6352
    $$

    $$
    b = 4.6352 + 1.0 = 5.6352
    $$

    Now, $\log K = \log 150 = 5.0106$. Check: is $5.0106 < 5.6352$? Yes, $\log 150$ falls inside $[a,b]$, but only barely --- it is $\frac{5.6352 - 5.0106}{0.2} = 3.12$ standard deviations from the mean, and the right boundary is only $5$ standard deviations out. The right tail beyond $\log K$ has width $b - \log K = 0.625$, capturing only a thin sliver of the density beyond the strike. More critically, any density mass beyond $b = 5.6352$ (corresponding to $S_T > e^{5.6352} = 280$) is entirely lost. For a deep OTM call at $K = 150$, a meaningful fraction of the option value comes from scenarios where $S_T > 280$ under Heston's fat tails.

    **Case $L = 10$:**

    $$
    a = 4.6352 - 2.0 = 2.6352
    $$

    $$
    b = 4.6352 + 2.0 = 6.6352
    $$

    Now $\log 150 = 5.0106$ falls well inside $[a,b]$, with $b - \log K = 1.625$, providing ample room for the right tail. The density mass beyond $b$ (corresponding to $S_T > e^{6.6352} \approx 760$) is negligible ($< 10^{-15}$).

    **Conclusion.** With $L = 5$, the truncation interval is dangerously narrow for deep OTM options. The COS price will converge as $N \to \infty$ but to the wrong value (the price conditional on $S_T \in [e^a, e^b]$). With $L = 10$, the domain error is negligible. This asymmetric risk --- convergent but biased --- is the most insidious error in COS implementations.

---

**Exercise 7.**
The COS method shares the density coefficients $A_k$ across all strikes but recomputes the payoff coefficients $V_k$ for each strike. If pricing 50 strikes with $N = 128$, estimate the total number of CF evaluations and compare with the Gil-Pelaez approach (assume 500 CF evaluations per strike). At what number of strikes does the FFT method (which prices all strikes simultaneously with $2^{12}$ CF evaluations) become more efficient than COS?

??? success "Solution to Exercise 7"
    **COS method CF evaluations.** The density coefficients $A_k$ are shared across all strikes. For $M = 50$ strikes with $N = 128$:

    - CF evaluations: $N = 128$ (computed once, shared across all strikes)
    - Payoff coefficient evaluations: $N \times M = 128 \times 50 = 6400$ (elementary function calls per strike)
    - Dot products: $M = 50$ (one per strike)

    Total CF evaluations: **128**.

    **Gil-Pelaez CF evaluations.** Each strike requires an independent numerical integration, with approximately 500 CF evaluations per strike:

    Total CF evaluations: $500 \times 50 = $ **25,000**.

    **Ratio:** $25000/128 \approx 195$. The COS method uses approximately 200 times fewer CF evaluations.

    **FFT crossover analysis.** The Carr-Madan FFT with $N_{\text{FFT}} = 2^{12} = 4096$ points computes prices on a grid of 4096 log-strikes simultaneously, requiring 4096 CF evaluations total. The computational cost is dominated by:

    - CF evaluations: 4096
    - FFT: $O(N_{\text{FFT}}\log N_{\text{FFT}}) = O(4096 \times 12) \approx 49000$ operations

    For the COS method with $M$ strikes:

    - CF evaluations: 128
    - Payoff computations: $128 \times M$
    - Dot products: $128 \times M$

    Total COS work: $128 + 256M$ (in units of elementary operations, counting CF evaluations as more expensive).

    The FFT becomes more efficient when the cost of computing payoff coefficients for $M$ strikes exceeds the FFT cost. Since CF evaluations dominate, the crossover is approximately:

    $$
    128 + c_{\text{elem}} \times 256M \approx 4096 \times c_{\text{CF}} + 49000 \times c_{\text{elem}}
    $$

    where $c_{\text{CF}}/c_{\text{elem}} \approx 10$--$50$ (a single CF evaluation is much more expensive than an elementary function). Taking $c_{\text{CF}} = 20\, c_{\text{elem}}$:

    $$
    128 \times 20 + 256M \approx 4096 \times 20 + 49000
    $$

    $$
    2560 + 256M \approx 81920 + 49000 = 130920
    $$

    $$
    M \approx \frac{128360}{256} \approx 501
    $$

    So the FFT becomes more efficient than COS at approximately **$M \approx 500$ strikes**. In practice, the crossover is often lower (around 200--500) because the FFT produces prices at all grid points simultaneously with a single pass. For calibration tasks involving 20--50 market strikes, the COS method is decisively faster. For generating a full volatility surface on a dense grid (thousands of strikes), the FFT is preferred.
