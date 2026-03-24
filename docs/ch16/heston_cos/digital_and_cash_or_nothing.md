# Digital and Cash-or-Nothing Options via COS Method

Digital options pay a fixed amount (cash-or-nothing) or the asset price (asset-or-nothing) contingent on whether the underlying exceeds a barrier at maturity. Their discontinuous payoffs create special challenges for Fourier-based pricing: the Gibbs phenomenon causes oscillatory errors near the strike that converge slowly. The COS method handles these payoffs through modified payoff coefficients that exploit the psi auxiliary function, and convergence can be accelerated through smoothing techniques.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define and price cash-or-nothing and asset-or-nothing options using the COS method
    2. Derive closed-form payoff coefficients $V_k$ for digital payoffs
    3. Understand the Gibbs phenomenon and its impact on COS convergence for discontinuous payoffs
    4. Apply Richardson extrapolation and other smoothing techniques to accelerate convergence

---

## Intuition

A European call option pays $(S_T - K)^+$, which is a continuous function of $S_T$. A cash-or-nothing call pays a fixed amount $B$ if $S_T > K$ and zero otherwise --- a step function with a discontinuity at $S_T = K$. Fourier series approximate smooth functions with exponential convergence but approximate discontinuous functions with only algebraic convergence (the Gibbs phenomenon). This means the COS method, which achieves $N = 64$ accuracy for vanilla calls, may need $N = 256$ or more for digitals to reach the same precision. Understanding and mitigating this slowdown is essential for accurate pricing.

---

## Digital Option Payoffs

Three types of digital options are standard.

!!! info "Definition (Digital Option Types)"
    Let $K$ be the strike and $B$ the notional amount.

    - **Cash-or-nothing call**: pays $B$ if $S_T > K$, zero otherwise. Payoff: $v(y) = B \cdot \mathbf{1}_{y > \log K}$
    - **Cash-or-nothing put**: pays $B$ if $S_T < K$, zero otherwise. Payoff: $v(y) = B \cdot \mathbf{1}_{y < \log K}$
    - **Asset-or-nothing call**: pays $S_T$ if $S_T > K$, zero otherwise. Payoff: $v(y) = e^y \cdot \mathbf{1}_{y > \log K}$
    - **Asset-or-nothing put**: pays $S_T$ if $S_T < K$, zero otherwise. Payoff: $v(y) = e^y \cdot \mathbf{1}_{y < \log K}$

    where $y = \log S_T$.

The standard European call decomposes as $C = \text{Asset-or-nothing call} - K \cdot \text{Cash-or-nothing call}$, confirming that digitals are building blocks for vanilla options.

---

## COS Payoff Coefficients for Cash-or-Nothing Options

The COS payoff coefficients for digital options follow from direct integration of the indicator payoff against cosine basis functions.

!!! info "Proposition (Cash-or-Nothing Call Coefficients)"
    The COS payoff coefficients for a cash-or-nothing call with notional $B$ and strike $K$ are

    $$
    V_k^{\text{CoN,call}} = B \, \psi_k(\ell, b)
    $$

    where $\ell = \log K$ and $\psi_k$ is the psi auxiliary function.

**Proof.** The payoff in log-coordinates is $v(y) = B \cdot \mathbf{1}_{y > \ell}$. On the truncated domain $[a, b]$:

$$
V_k = \int_a^b v(y) \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy = B \int_{\ell}^{b} \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy = B \, \psi_k(\ell, b)
$$

$\square$

!!! info "Proposition (Cash-or-Nothing Put Coefficients)"
    The COS payoff coefficients for a cash-or-nothing put are

    $$
    V_k^{\text{CoN,put}} = B \, \psi_k(a, \ell)
    $$

**Proof.** Analogous to the call case, integrating over $[a, \ell]$. $\square$

**Consistency check:** $V_k^{\text{CoN,call}} + V_k^{\text{CoN,put}} = B \, \psi_k(a, b)$, which are the coefficients of the constant payoff $B$ --- the price of a zero-coupon bond, as expected.

---

## COS Payoff Coefficients for Asset-or-Nothing Options

!!! info "Proposition (Asset-or-Nothing Call Coefficients)"
    The COS payoff coefficients for an asset-or-nothing call with strike $K$ are

    $$
    V_k^{\text{AoN,call}} = \chi_k(\ell, b)
    $$

    where $\chi_k$ is the chi auxiliary function.

**Proof.** The payoff is $v(y) = e^y \cdot \mathbf{1}_{y > \ell}$:

$$
V_k = \int_{\ell}^{b} e^y \cos\!\left(k\pi \frac{y-a}{b-a}\right) dy = \chi_k(\ell, b)
$$

$\square$

!!! info "Proposition (Asset-or-Nothing Put Coefficients)"

    $$
    V_k^{\text{AoN,put}} = \chi_k(a, \ell)
    $$

**Verification against vanilla options.** The European call payoff $(e^y - K)^+$ decomposes as $e^y \cdot \mathbf{1}_{y > \ell} - K \cdot \mathbf{1}_{y > \ell}$, so

$$
V_k^{\text{call}} = V_k^{\text{AoN,call}} - K \cdot V_k^{\text{CoN,call}} = \chi_k(\ell, b) - K \, \psi_k(\ell, b)
$$

which matches the European call formula from the preceding section.

---

## COS Pricing Formulas

Assembling the components, the digital option prices are:

$$
\text{CoN Call} = e^{-r\tau} B \sum_{k=0}^{N-1}{}' A_k \, \psi_k(\ell, b)
$$

$$
\text{CoN Put} = e^{-r\tau} B \sum_{k=0}^{N-1}{}' A_k \, \psi_k(a, \ell)
$$

$$
\text{AoN Call} = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k \, \chi_k(\ell, b)
$$

$$
\text{AoN Put} = e^{-r\tau} \sum_{k=0}^{N-1}{}' A_k \, \chi_k(a, \ell)
$$

where the density coefficients $A_k$ are computed from the Heston characteristic function as in the standard COS framework.

---

## The Gibbs Phenomenon and Convergence

The discontinuity in the digital payoff at $y = \ell$ causes the Fourier cosine series to converge only algebraically, not exponentially.

!!! warning "Gibbs Phenomenon for Digital Payoffs"
    For a step function, the Fourier series converges as $O(1/N)$ pointwise away from the discontinuity, compared to exponential convergence for smooth payoffs. Near the discontinuity, the partial sums exhibit oscillations (Gibbs overshoot) of approximately 9% of the jump height, regardless of $N$.

    For pricing, the relevant quantity is the integral of the error against the density (not the pointwise error), so the pricing error is $O(1/N^2)$ --- better than pointwise but still much slower than the $O(e^{-cN})$ convergence of vanilla options.

**Convergence comparison:**

| $N$ | Vanilla Call Error | Cash-or-Nothing Error |
|-----|-------------------|----------------------|
| 32 | $5 \times 10^{-4}$ | $3 \times 10^{-2}$ |
| 64 | $1 \times 10^{-6}$ | $8 \times 10^{-3}$ |
| 128 | $3 \times 10^{-9}$ | $2 \times 10^{-3}$ |
| 256 | $< 10^{-12}$ | $5 \times 10^{-4}$ |
| 1024 | $< 10^{-12}$ | $3 \times 10^{-5}$ |

---

## Convergence Acceleration Techniques

Several methods restore fast convergence for digital options.

**Method 1: Call spread approximation.** Replace the digital payoff with a tight call spread:

$$
\mathbf{1}_{S_T > K} \approx \frac{(S_T - K_-)^+ - (S_T - K_+)^+}{K_+ - K_-}
$$

where $K_{\pm} = K \pm \epsilon$ and $\epsilon$ is small (e.g., $\epsilon = 0.01K$). This smooths the discontinuity and restores exponential COS convergence, at the cost of a small bias proportional to $\epsilon^2$.

**Method 2: Richardson extrapolation.** Compute the COS price at two different values of $N$, say $N$ and $2N$, and extrapolate:

$$
V_{\text{extrapolated}} = 2 V_{2N} - V_N + O(1/N^4)
$$

This improves the convergence rate from $O(1/N^2)$ to $O(1/N^4)$.

**Method 3: Direct integration approach.** Use the Gil-Pelaez formula for digitals:

$$
\text{CoN Call} = e^{-r\tau} B \left[\frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left(\frac{e^{-iu\log K}\varphi(u)}{iu}\right) du\right]
$$

This is a direct Fourier inversion that avoids the Gibbs phenomenon entirely, though it is slower than the COS method for smooth payoffs.

!!! tip "Practical Recommendation"
    For production-quality digital pricing under Heston:

    1. Use the **call spread approximation** with $\epsilon = 0.5\%$ of $K$ and $N = 128$ COS terms. This gives accuracy better than 1 basis point with the speed of the COS method.
    2. For benchmark verification, use the **Gil-Pelaez formula** with adaptive quadrature.
    3. For Greek computation, the call spread approach is particularly convenient because it automatically smooths the delta (which is a Dirac delta for a true digital).

---

## Numerical Example

Consider $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $B = 1$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1$.

**Reference prices (Gil-Pelaez):**

| Option | Price |
|--------|-------|
| Cash-or-nothing call | \$0.4884 |
| Cash-or-nothing put | \$0.4628 |
| Asset-or-nothing call | \$57.4812 |
| Asset-or-nothing put | \$42.5188 |

**COS method with $N = 128$:**

| Option | COS Direct | Error | COS + Spread ($\epsilon = 0.5$) | Error |
|--------|-----------|-------|-------------------------------|-------|
| CoN call | 0.4903 | $1.9 \times 10^{-3}$ | 0.4885 | $1.0 \times 10^{-4}$ |
| CoN put | 0.4609 | $1.9 \times 10^{-3}$ | 0.4627 | $1.0 \times 10^{-4}$ |

The call spread approximation improves accuracy by a factor of 20 at no additional computational cost.

??? example "Relationship to Exercise Probability"
    The cash-or-nothing call price divided by the discount factor gives the risk-neutral exercise probability:

    $$
    P_2 = \mathbb{Q}(S_T > K) = e^{r\tau} \times 0.4884 = 0.5134
    $$

    This matches the $P_2$ probability from the Gil-Pelaez decomposition of the European call price. The asset-or-nothing call relates to $P_1$:

    $$
    P_1 = \frac{e^{q\tau}}{S_0} \times 57.4812 = 0.5748
    $$

    The European call price is $C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2 = 100(0.5748) - 100(0.9512)(0.5134) = 57.48 - 48.85 = 8.63$, which can be verified against the direct COS call price.

---

## Summary

Digital options (cash-or-nothing and asset-or-nothing) are priced via the COS method using payoff coefficients that reduce to the psi and chi auxiliary functions. Cash-or-nothing coefficients involve only $\psi_k$, while asset-or-nothing coefficients involve only $\chi_k$. The discontinuous payoff causes the Gibbs phenomenon, reducing COS convergence from exponential to algebraic ($O(1/N^2)$ in the price). Practical mitigation strategies include the call spread approximation (which smooths the payoff and restores exponential convergence), Richardson extrapolation, and direct Gil-Pelaez inversion for benchmarking. The decomposition of vanilla options into digital building blocks provides a useful consistency check and connects COS pricing to the probability measures $P_1$ and $P_2$ from the Heston pricing framework.

---

## Exercises

**Exercise 1.**
The COS payoff coefficients for a cash-or-nothing call are $V_k^{\text{CoN,call}} = B\,\psi_k(\ell, b)$ with $\ell = \log K$. Show that for $k = 0$ this reduces to $V_0^{\text{CoN,call}} = B(b - \ell)$, and interpret this geometrically as the width of the integration domain in log-space. What fraction of the total domain $[a, b]$ does this represent for an ATM option with $S_0 = 100$ and $L = 10$?

---

**Exercise 2.**
Verify the consistency check: $V_k^{\text{CoN,call}} + V_k^{\text{CoN,put}} = B\,\psi_k(a, b)$. Use this to show that the COS price of a cash-or-nothing call plus a cash-or-nothing put equals $Be^{-r\tau}$ (a zero-coupon bond). Why does this identity hold regardless of the characteristic function or model choice?

---

**Exercise 3.**
The European call decomposes as $C = \text{AoN call} - K \cdot \text{CoN call}$. Using the COS prices from the numerical example ($S_0 = 100$, $K = 100$, $r = 0.05$, $\tau = 1$), verify that

$$
C = 57.4812 - 100 \times 0.4884 = 8.64
$$

Compare this with the direct COS call price. Explain any discrepancy in terms of the different convergence rates of the digital and vanilla COS series.

---

**Exercise 4.**
The Gibbs phenomenon causes the COS series for a cash-or-nothing option to converge as $O(1/N^2)$ in the price. If the error at $N = 64$ is approximately $8 \times 10^{-3}$, estimate the error at $N = 256$ and $N = 1024$ assuming exact $O(1/N^2)$ scaling. How many COS terms are needed to achieve four-digit accuracy ($10^{-4}$) for the direct COS digital price?

---

**Exercise 5.**
The call spread approximation replaces the digital payoff $\mathbf{1}_{S_T > K}$ with $(C(K - \epsilon) - C(K + \epsilon))/(2\epsilon)$. For $\epsilon = 0.5$ and $K = 100$, compute the two call prices using COS with $N = 128$, form the spread, and compare with the Gil-Pelaez reference price $0.4884$. Show that the smoothing bias is $O(\epsilon^2)$ by repeating with $\epsilon = 0.25$ and comparing the errors.

---

**Exercise 6.**
Richardson extrapolation uses $V_{\text{extrap}} = 2V_{2N} - V_N$ to improve convergence from $O(1/N^2)$ to $O(1/N^4)$. Compute the COS cash-or-nothing call price at $N = 64$ and $N = 128$, apply Richardson extrapolation, and compare the result with the Gil-Pelaez reference. By what factor does the error improve compared to the un-extrapolated $N = 128$ result?

---

**Exercise 7.**
The asset-or-nothing call price relates to the exercise probability $P_1$ via $\text{AoN call} = S_0 e^{-q\tau} P_1$. Explain why the COS convergence for the asset-or-nothing call is better than for the cash-or-nothing call, despite both having a discontinuity at $y = \log K$. Hint: the payoff $e^y \cdot \mathbf{1}_{y > \ell}$ is continuous from the right but has a jump in value at $y = \ell$, while the cash-or-nothing payoff has a jump of magnitude $B$. How does the payoff magnitude at the discontinuity affect the Gibbs overshoot?
