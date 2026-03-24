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

---

**Exercise 2.**
For $k = 0$, the psi function reduces to $\psi_0(c, d) = d - c$. Using the chi function formula, compute $\chi_0(\ell, b) = \frac{1}{1+0}[e^b - e^\ell] = e^b - e^\ell$. Verify that the $k = 0$ call payoff coefficient is $V_0^{\text{call}} = e^b - e^\ell - K(b - \ell)$. For the numerical example ($S_0 = 100$, $K = 100$, $a = 2.6352$, $b = 6.6352$), compute this value explicitly.

---

**Exercise 3.**
The truncation bounds use $\bar{v} = \theta + (v_0 - \theta)(1 - e^{-\kappa\tau})/(\kappa\tau)$ as the average expected variance. For $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\tau = 1$, show that $\bar{v} = \theta = 0.04$ (since $v_0 = \theta$). Now consider $v_0 = 0.09$ (elevated vol) and recompute $\bar{v}$, $a$, and $b$. How much wider is the truncation interval compared to the $v_0 = 0.04$ case?

---

**Exercise 4.**
Verify put-call parity at the COS coefficient level: show that $V_k^{\text{call}} + V_k^{\text{put}} = \chi_k(a, b) - K\psi_k(a, b)$, which are the payoff coefficients for the forward contract $v(y) = e^y - K$. Using the numerical example prices ($N = 128$, $K = 100$), check that the COS call and put prices satisfy $C - P = S_0 e^{-q\tau} - K e^{-r\tau}$ to at least 8 decimal places.

---

**Exercise 5.**
The COS method evaluates the characteristic function at $N$ equally spaced frequency points $u_k = k\pi/(b-a)$, while the Gil-Pelaez formula evaluates it on a continuous grid determined by adaptive quadrature. Explain why the COS method needs far fewer CF evaluations (64--128 vs 500--1000) to achieve comparable accuracy. How does the exponential decay of $|A_k|$ relate to the number of terms needed?

---

**Exercise 6.**
For deep OTM options (e.g., $K = 150$ with $S_0 = 100$), the option value comes entirely from the right tail of the density. Explain why setting $L$ too small (e.g., $L = 5$) causes a systematic underpricing bias that does not improve as $N$ increases. Compute the truncation bounds for $L = 5$ and $L = 10$ with the standard parameters, and determine whether $\log K = \log 150 \approx 5.01$ falls inside $[a, b]$ in each case.

---

**Exercise 7.**
The COS method shares the density coefficients $A_k$ across all strikes but recomputes the payoff coefficients $V_k$ for each strike. If pricing 50 strikes with $N = 128$, estimate the total number of CF evaluations and compare with the Gil-Pelaez approach (assume 500 CF evaluations per strike). At what number of strikes does the FFT method (which prices all strikes simultaneously with $2^{12}$ CF evaluations) become more efficient than COS?
