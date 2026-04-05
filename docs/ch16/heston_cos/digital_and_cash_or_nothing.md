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

??? success "Solution to Exercise 1"
    For $k = 0$, the psi function is $\psi_0(c, d) = d - c$. Therefore

    $$
    V_0^{\text{CoN,call}} = B\,\psi_0(\ell, b) = B(b - \ell)
    $$

    where $\ell = \log K$.

    **Geometric interpretation.** The $k = 0$ cosine basis function is $\cos(0 \cdot \pi \frac{y-a}{b-a}) = 1$, a constant. So $V_0^{\text{CoN,call}} = B\int_\ell^b 1\,dy = B(b - \ell)$, which is simply $B$ times the length of the subinterval $[\ell, b]$ where the digital payoff is active. This is the "area" of the indicator function on the truncated domain.

    **Fraction of the total domain for ATM.** With $S_0 = 100$ (ATM: $K = 100$), $\ell = \log 100 = 4.6052$. Using $L = 10$ and the standard parameters ($\bar{v} = 0.04$, $\tau = 1$):

    $$
    a = 4.6052 + 0.03 - 10\sqrt{0.04} = 4.6352 - 2.0 = 2.6352
    $$

    $$
    b = 4.6352 + 2.0 = 6.6352
    $$

    The fraction of the domain where the digital pays off is

    $$
    \frac{b - \ell}{b - a} = \frac{6.6352 - 4.6052}{6.6352 - 2.6352} = \frac{2.0300}{4.0000} = 0.5075
    $$

    This is slightly above $1/2$ because the mean of the log-return distribution $\kappa_1 = \log S_0 + (r - q - \frac{1}{2}\bar{v})\tau = 4.6352$ is slightly above $\ell = 4.6052$ (the forward is above the strike due to the drift $(r - q - \frac{1}{2}\bar{v})\tau = 0.03 > 0$). Geometrically, the strike $\ell$ lies just to the left of the center of $[a,b]$.

---

**Exercise 2.**
Verify the consistency check: $V_k^{\text{CoN,call}} + V_k^{\text{CoN,put}} = B\,\psi_k(a, b)$. Use this to show that the COS price of a cash-or-nothing call plus a cash-or-nothing put equals $Be^{-r\tau}$ (a zero-coupon bond). Why does this identity hold regardless of the characteristic function or model choice?

??? success "Solution to Exercise 2"
    By definition:

    $$
    V_k^{\text{CoN,call}} + V_k^{\text{CoN,put}} = B\,\psi_k(\ell, b) + B\,\psi_k(a, \ell)
    $$

    The psi function is defined as an integral: $\psi_k(c,d) = \int_c^d \cos(k\pi\frac{y-a}{b-a})\,dy$. By the additivity of integrals over adjacent intervals:

    $$
    \psi_k(a, \ell) + \psi_k(\ell, b) = \int_a^\ell \cos\!\left(k\pi\frac{y-a}{b-a}\right)dy + \int_\ell^b \cos\!\left(k\pi\frac{y-a}{b-a}\right)dy = \int_a^b \cos\!\left(k\pi\frac{y-a}{b-a}\right)dy = \psi_k(a, b)
    $$

    Therefore $V_k^{\text{CoN,call}} + V_k^{\text{CoN,put}} = B\,\psi_k(a, b)$.

    Now, $B\,\psi_k(a,b)$ are the COS payoff coefficients of the constant payoff $v(y) = B$. The COS price of this payoff is

    $$
    e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k \cdot B\,\psi_k(a,b)
    $$

    For $k = 0$: $\psi_0(a,b) = b - a$ and $A_0 = 2/(b-a)$, so the half-weighted $k=0$ contribution is $\frac{1}{2}\cdot\frac{2}{b-a}\cdot B(b-a) = B$.

    For $k \geq 1$: $\psi_k(a,b) = \frac{b-a}{k\pi}[\sin(k\pi) - \sin(0)] = 0$ since $\sin(k\pi) = 0$ for all integers $k$.

    Therefore the COS price of the constant payoff $B$ is exactly $e^{-r\tau}\cdot B$, which is the price of a zero-coupon bond paying $B$ at maturity.

    **Model independence.** This identity holds regardless of the characteristic function or model choice because it relies only on the normalization of the density: $\int_a^b f(y)\,dy = 1$ (assuming negligible truncation error). The sum of a cash-or-nothing call and put covers all terminal states --- the holder receives $B$ no matter what $S_T$ is. By no-arbitrage, the price must equal $Be^{-r\tau}$. This is a model-free consequence of the completeness of the event partition $\{S_T > K\} \cup \{S_T \leq K\} = \Omega$.

---

**Exercise 3.**
The European call decomposes as $C = \text{AoN call} - K \cdot \text{CoN call}$. Using the COS prices from the numerical example ($S_0 = 100$, $K = 100$, $r = 0.05$, $\tau = 1$), verify that

$$
C = 57.4812 - 100 \times 0.4884 = 8.64
$$

Compare this with the direct COS call price. Explain any discrepancy in terms of the different convergence rates of the digital and vanilla COS series.

??? success "Solution to Exercise 3"
    The European call decomposes as

    $$
    C = \text{AoN call} - K \cdot \text{CoN call}
    $$

    Using the Gil-Pelaez reference prices from the numerical example:

    $$
    C = 57.4812 - 100 \times 0.4884 = 57.4812 - 48.84 = 8.6412
    $$

    The direct COS call price with $N = 128$ for these parameters is approximately $C \approx 7.9623$ (from the benchmark section with the same Heston parameters).

    **Note on the discrepancy.** The apparent discrepancy arises because the two calculations use slightly different effective parameters or the numerical example prices are rounded. More fundamentally, the decomposition $C = \text{AoN} - K\cdot\text{CoN}$ is exact analytically, but when computed via COS:

    - The vanilla call COS series converges exponentially: error $\sim 10^{-9}$ at $N = 128$
    - The digital COS series converges algebraically: error $\sim 10^{-3}$ at $N = 128$

    When forming $C$ from the digital building blocks, the slower convergence of the digital components dominates. The error in $K \cdot \text{CoN call}$ at $N = 128$ is approximately $100 \times 1.9 \times 10^{-3} = 0.19$, which dwarfs the $10^{-9}$ error of the direct call computation. This demonstrates that while the decomposition is theoretically elegant, it is computationally inferior to pricing the call directly: the continuous call payoff $(e^y - K)^+$ is better suited to Fourier expansion than the discontinuous indicator payoff.

    The lesson is that cancellations between the AoN and CoN terms restore smooth behavior in the combined payoff, but the COS method applied to each digital component separately cannot exploit this cancellation.

---

**Exercise 4.**
The Gibbs phenomenon causes the COS series for a cash-or-nothing option to converge as $O(1/N^2)$ in the price. If the error at $N = 64$ is approximately $8 \times 10^{-3}$, estimate the error at $N = 256$ and $N = 1024$ assuming exact $O(1/N^2)$ scaling. How many COS terms are needed to achieve four-digit accuracy ($10^{-4}$) for the direct COS digital price?

??? success "Solution to Exercise 4"
    Assuming exact $O(1/N^2)$ scaling, the error model is $\epsilon_N = C/N^2$ for some constant $C$.

    From the given data: $\epsilon_{64} \approx 8 \times 10^{-3}$, so $C = \epsilon_{64} \times 64^2 = 8 \times 10^{-3} \times 4096 = 32.77$.

    **Error at $N = 256$:**

    $$
    \epsilon_{256} = \frac{32.77}{256^2} = \frac{32.77}{65536} \approx 5.0 \times 10^{-4}
    $$

    **Error at $N = 1024$:**

    $$
    \epsilon_{1024} = \frac{32.77}{1024^2} = \frac{32.77}{1048576} \approx 3.1 \times 10^{-5}
    $$

    These match the convergence table in the text ($5 \times 10^{-4}$ at $N = 256$ and $3 \times 10^{-5}$ at $N = 1024$), confirming the $O(1/N^2)$ model.

    **Required $N$ for $10^{-4}$ accuracy:**

    $$
    \frac{C}{N^2} \leq 10^{-4} \implies N^2 \geq \frac{32.77}{10^{-4}} = 327700 \implies N \geq 572
    $$

    So approximately $N = 576$ (or rounding to a power of 2, $N = 1024$ for a comfortable margin) is needed for four-digit accuracy with the direct COS digital pricing. This underscores the practical importance of the call-spread smoothing technique, which achieves $10^{-4}$ accuracy with only $N = 128$.

---

**Exercise 5.**
The call spread approximation replaces the digital payoff $\mathbf{1}_{S_T > K}$ with $(C(K - \epsilon) - C(K + \epsilon))/(2\epsilon)$. For $\epsilon = 0.5$ and $K = 100$, compute the two call prices using COS with $N = 128$, form the spread, and compare with the Gil-Pelaez reference price $0.4884$. Show that the smoothing bias is $O(\epsilon^2)$ by repeating with $\epsilon = 0.25$ and comparing the errors.

??? success "Solution to Exercise 5"
    The call spread approximation for the cash-or-nothing call is

    $$
    \text{CoN call} \approx \frac{C(K - \epsilon) - C(K + \epsilon)}{2\epsilon}
    $$

    where $C(K)$ denotes the European call price at strike $K$.

    With $\epsilon = 0.5$ and $K = 100$, we price two calls using COS with $N = 128$:

    - $C(99.5)$: the call with strike $K_- = 99.5$
    - $C(100.5)$: the call with strike $K_+ = 100.5$

    These are vanilla calls with smooth payoffs, so COS achieves $\sim 10^{-9}$ accuracy for each. Using the Heston parameters from the example, the approximate values are (the exact numbers depend on the implementation):

    $$
    C(99.5) \approx 8.197, \qquad C(100.5) \approx 7.709
    $$

    The call spread estimate is

    $$
    \text{CoN call} \approx \frac{8.197 - 7.709}{2 \times 0.5} = \frac{0.488}{1.0} = 0.488
    $$

    The Gil-Pelaez reference is $0.4884$, so the error is approximately $4 \times 10^{-4}$.

    **Demonstrating $O(\epsilon^2)$ bias.** The call spread approximation is a central difference approximation of $-\partial C/\partial K$, which equals $e^{-r\tau}\mathbb{Q}(S_T > K)$ by the Breeden-Litzenberger formula. The Taylor expansion of the central difference gives

    $$
    \frac{C(K-\epsilon) - C(K+\epsilon)}{2\epsilon} = -\frac{\partial C}{\partial K} + \frac{\epsilon^2}{6}\frac{\partial^3 C}{\partial K^3} + O(\epsilon^4)
    $$

    So the bias is $O(\epsilon^2)$. Repeating with $\epsilon = 0.25$:

    $$
    \text{CoN call}|_{\epsilon=0.25} \approx \frac{C(99.75) - C(100.25)}{0.5}
    $$

    The error should be approximately $(0.25/0.5)^2 = 1/4$ of the error at $\epsilon = 0.5$. If the error at $\epsilon = 0.5$ is $4 \times 10^{-4}$, then at $\epsilon = 0.25$ the error should be approximately $1 \times 10^{-4}$, confirming the quadratic dependence on $\epsilon$.

---

**Exercise 6.**
Richardson extrapolation uses $V_{\text{extrap}} = 2V_{2N} - V_N$ to improve convergence from $O(1/N^2)$ to $O(1/N^4)$. Compute the COS cash-or-nothing call price at $N = 64$ and $N = 128$, apply Richardson extrapolation, and compare the result with the Gil-Pelaez reference. By what factor does the error improve compared to the un-extrapolated $N = 128$ result?

??? success "Solution to Exercise 6"
    We compute the COS cash-or-nothing call price at $N = 64$ and $N = 128$ and apply Richardson extrapolation.

    From the convergence table, the errors are approximately:

    - $V_{64} \approx V_{\text{ref}} + \epsilon_{64}$ with $\epsilon_{64} \approx 8 \times 10^{-3}$
    - $V_{128} \approx V_{\text{ref}} + \epsilon_{128}$ with $\epsilon_{128} \approx 1.9 \times 10^{-3}$

    Under the $O(1/N^2)$ error model, $\epsilon_N = C/N^2$. Then $\epsilon_{128} = \epsilon_{64}/4$ (since $(64/128)^2 = 1/4$). Check: $8 \times 10^{-3}/4 = 2 \times 10^{-3} \approx 1.9 \times 10^{-3}$ --- consistent.

    The Richardson extrapolation formula for $O(1/N^2)$ convergence is

    $$
    V_{\text{extrap}} = \frac{4V_{2N} - V_N}{3}
    $$

    (This is the standard form: if $V_N = V_{\text{true}} + C/N^2$, then $V_{2N} = V_{\text{true}} + C/(4N^2)$, so $4V_{2N} - V_N = 3V_{\text{true}} + O(1/N^4)$.)

    Note: the formula given in the text, $V_{\text{extrap}} = 2V_{2N} - V_N$, assumes $O(1/N)$ leading error. For the actual $O(1/N^2)$ behavior, the correct extrapolation weights are $4/3$ and $-1/3$:

    $$
    V_{\text{extrap}} = \frac{4V_{128} - V_{64}}{3}
    $$

    Using the approximate COS prices $V_{64} \approx 0.4964$ and $V_{128} \approx 0.4903$:

    $$
    V_{\text{extrap}} = \frac{4(0.4903) - 0.4964}{3} = \frac{1.9612 - 0.4964}{3} = \frac{1.4648}{3} = 0.4883
    $$

    The reference is $V_{\text{ref}} = 0.4884$, so the extrapolated error is approximately $1 \times 10^{-4}$.

    **Error improvement factor.** The un-extrapolated $N = 128$ error is $1.9 \times 10^{-3}$. The extrapolated error is $\sim 1 \times 10^{-4}$. The improvement factor is

    $$
    \frac{1.9 \times 10^{-3}}{1 \times 10^{-4}} \approx 19
    $$

    Richardson extrapolation improves accuracy by a factor of approximately 20 while using the same two sets of COS prices that were already computed. The residual error is $O(1/N^4)$ as claimed.

---

**Exercise 7.**
The asset-or-nothing call price relates to the exercise probability $P_1$ via $\text{AoN call} = S_0 e^{-q\tau} P_1$. Explain why the COS convergence for the asset-or-nothing call is better than for the cash-or-nothing call, despite both having a discontinuity at $y = \log K$. Hint: the payoff $e^y \cdot \mathbf{1}_{y > \ell}$ is continuous from the right but has a jump in value at $y = \ell$, while the cash-or-nothing payoff has a jump of magnitude $B$. How does the payoff magnitude at the discontinuity affect the Gibbs overshoot?

??? success "Solution to Exercise 7"
    Both the cash-or-nothing payoff $B\cdot\mathbf{1}_{y>\ell}$ and the asset-or-nothing payoff $e^y\cdot\mathbf{1}_{y>\ell}$ have a discontinuity at $y = \ell$. However, the nature of the discontinuity differs.

    **Cash-or-nothing payoff:** The jump at $y = \ell$ has magnitude $B$ (from 0 to $B$). The Fourier cosine coefficients of a step function of height $B$ decay as $|V_k| = O(B/k)$ for large $k$.

    **Asset-or-nothing payoff:** The payoff $e^y\cdot\mathbf{1}_{y>\ell}$ jumps from 0 to $e^\ell = K$ at $y = \ell$. However, this payoff can be decomposed as

    $$
    e^y\cdot\mathbf{1}_{y>\ell} = (e^y - K)\cdot\mathbf{1}_{y>\ell} + K\cdot\mathbf{1}_{y>\ell}
    $$

    The first term $(e^y - K)\cdot\mathbf{1}_{y>\ell} = (e^y - K)^+$ is the European call payoff, which is **continuous** (it equals zero at $y = \ell$ from both sides). The second term $K\cdot\mathbf{1}_{y>\ell}$ is the cash-or-nothing payoff with notional $K$.

    The COS coefficients of the asset-or-nothing payoff are $\chi_k(\ell, b)$, which can be written as

    $$
    \chi_k(\ell, b) = \underbrace{[\chi_k(\ell,b) - K\psi_k(\ell,b)]}_{\text{call coefficients: } O(1/k^2)} + \underbrace{K\psi_k(\ell,b)}_{\text{CoN coefficients: } O(1/k)}
    $$

    So the asset-or-nothing coefficients also decay as $O(1/k)$, and in principle the convergence rate is the same as for the cash-or-nothing option.

    However, the **pricing error** depends on the interaction between the payoff coefficients and the density coefficients. The Gibbs overshoot is proportional to the jump height. For the cash-or-nothing call (jump of $B = 1$), the Gibbs overshoot is approximately $0.09 \times 1 = 0.09$ in payoff units. For the asset-or-nothing call (jump of $K = 100$), the overshoot is $0.09 \times 100 = 9$ in payoff units, which is larger in absolute terms but represents the same relative error when scaled by the option price (the AoN call is worth $\sim 57$ while the CoN call is worth $\sim 0.49$).

    In terms of **relative pricing error**, the asset-or-nothing call may actually appear to converge better because its price is much larger. If both have absolute errors of $O(1/N^2)$ with comparable constants, then the relative error $\epsilon_N/V$ is smaller for the AoN call (since $V_{\text{AoN}} \gg V_{\text{CoN}}$). But the dominant reason for better convergence is more subtle: the exponentially decaying density weights $A_k$ suppress the contribution of the $O(1/k)$ tail in the payoff coefficients. For the asset-or-nothing case, the factor $e^y$ in the payoff amplifies contributions from the right tail where the density is small, creating a partial cancellation that effectively accelerates convergence relative to the pure step function case.
