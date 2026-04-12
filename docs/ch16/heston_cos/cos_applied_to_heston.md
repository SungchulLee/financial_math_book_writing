# COS Method Applied to Heston

The Fourier Cosine (COS) method extends the Fourier inversion principle to construct an extremely fast pricing algorithm. It combines Fourier series expansions with characteristic functions to achieve rapid convergence and exceptional computational efficiency.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand Fourier cosine series expansions of densities
    2. Derive closed-form payoff coefficients for European options
    3. Apply the COS method to Heston option pricing

---

## Fourier Cosine Series Representation

Assume the density $f(x)$ is supported on the interval $[a, b]$. The Fourier cosine series expansion is:

$$
f(x) \approx \sum_{k=0}^{n-1} \mathop{'} A_k \cos\left(k\pi \frac{x - a}{b - a}\right)
$$

where the prime notation $\sum \mathop{'}$ indicates the first term is weighted by $1/2$, and the coefficients are:

$$
A_k = \frac{2}{b-a} \mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right) e^{-i\frac{k\pi a}{b-a}}\right]
$$

Here $\varphi(u)$ is the characteristic function. The key advantage is that $A_k$ is trivial to compute if $\varphi$ is available.

---

## COS Method for Option Pricing

The option price under risk-neutral valuation is:

$$
V(t, S) = e^{-r\tau} \mathbb{E}^{\mathbb{Q}}[V(T, x) | \mathcal{F}(t)]
$$

where $x = \log S(T)$. Substituting the cosine expansion of the density:

$$
V(t, S) \approx e^{-r\tau} \frac{b-a}{2} \sum_{k=0}^{n-1} \mathop{'} A_k H_k
$$

Here:
- $A_k$ are the density Fourier coefficients (computed from the characteristic function)
- $H_k$ are the payoff coefficients, defined as:

$$
H_k = \frac{2}{b-a} \int_a^b V(T, x) \cos\left(k\pi \frac{x - a}{b - a}\right) dx
$$

---

## Closed-Form Payoff Coefficients

For European calls and puts, the payoff integrals have closed-form solutions using auxiliary functions:

**Chi function:**

$$
\chi_k(c, d) := \int_c^d e^x \cos\left(k\pi \frac{x - a}{b - a}\right) dx
$$

$$
= \frac{1}{1 + \left(\frac{k\pi}{b-a}\right)^2} \left[
\cos\left(k\pi \frac{d-a}{b-a}\right)e^d - \cos\left(k\pi \frac{c-a}{b-a}\right)e^c
\right
$$

$$
\left. + \frac{k\pi}{b-a}\sin\left(k\pi \frac{d-a}{b-a}\right)e^d - \frac{k\pi}{b-a}\sin\left(k\pi \frac{c-a}{b-a}\right)e^c
\right]
$$

**Psi function:**

$$
\psi_k(c, d) := \int_c^d \cos\left(k\pi \frac{x - a}{b - a}\right) dx
$$

$$
= \begin{cases}
\frac{b-a}{k\pi}\left[\sin\left(k\pi \frac{d-a}{b-a}\right) - \sin\left(k\pi \frac{c-a}{b-a}\right)\right] & k \neq 0\\
d - c & k = 0
\end{cases}
$$

**Call payoff coefficients:**

$$
H_k^{\text{call}} = \frac{2}{b-a} \chi_k(\log K, b) - \frac{2K}{b-a} \psi_k(\log K, b)
$$

**Put payoff coefficients:**

$$
H_k^{\text{put}} = \frac{2K}{b-a} \psi_k(a, \log K) - \frac{2}{b-a} \chi_k(a, \log K)
$$

---

## COS Method vs FFT Method

| Aspect | COS | FFT |
|--------|-----|-----|
| Density grid | Cosine series (adaptive) | Equidistant FFT grid |
| Convergence | Exponentially fast | Algebraic |
| # of terms needed | 32-128 typically | 512-4096 typically |
| Payoff formulas | Closed-form for vanilla | Numerical integration |
| Speed for single strike | Very fast | Slower |
| Speed for many strikes | Moderate | Very fast |

The COS method converges **exponentially** fast, making it one of the most efficient Fourier methods for vanilla European options.

---

## Implementation Steps for Heston

1. **Set bounds:** Choose $[a, b]$ to contain the significant mass of the log-return density (typically $\pm 3 \times \text{standard deviation}$)

2. **Compute characteristic function:** For Heston, evaluate the closed-form CF at frequency points $u_k = \frac{k\pi}{b-a}$

3. **Compute $A_k$:** Use the formula:

   $$
   A_k = \frac{2}{b-a} \mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right) e^{-i\frac{k\pi a}{b-a}}\right]
   $$

4. **Compute $H_k$:** For each strike $K$, use the closed-form payoff coefficients

5. **Sum the series:**

   $$
   V = e^{-r\tau} \frac{b-a}{2} \sum_{k=0}^{n-1} \mathop{'} A_k H_k
   $$

   with typically $n = 64$ to $128$

---

## Advantages of COS Method

1. **Extreme speed:** Pricing hundreds of strikes in milliseconds
2. **Exponential convergence:** Exponentially fast in the number of terms $n$
3. **Simplicity:** No FFT algorithm needed, just a direct sum
4. **Flexibility:** Easy to extend to exotic options with integrable payoffs
5. **Stability:** More stable numerically than FFT for moderate accuracy requirements

---

## Limitations and Extensions

**Limitations:**
- Payoff must be integrable (rules out barrier/digital options without modification)
- Choice of bounds $[a, b]$ affects convergence
- Difficult to apply to path-dependent options

**Extensions:**
- Digital options: piecewise polynomial approximation
- Barrier options: combination with finite-difference solver
- American options: backward induction with COS method at each step

---

## Summary

The COS method represents a significant advancement in computational finance, combining the analytical power of Fourier analysis with the practical efficiency of series summation. For European options under the Heston model, it typically achieves 5-8 significant digits of accuracy with only 32-64 terms, making it the preferred choice in many production systems. The exponentially fast convergence and closed-form payoff coefficients make it an exemplary application of Fourier methods in quantitative finance.

---

## Exercises

**Exercise 1.**
The COS method approximates the density by $f(y) \approx \frac{2}{b-a}\sum_{k=0}^{N-1}{}' A_k \cos(k\pi\frac{y-a}{b-a})$. Explain why this is a cosine expansion on $[a, b]$ rather than a full Fourier series. What symmetry assumption about the density does this expansion implicitly make?

??? success "Solution to Exercise 1"
    The COS method uses a cosine expansion rather than a full Fourier series because the density $f(y)$ is extended to $[a,b]$ via an even reflection about the endpoints. Concretely, define the periodic extension of $f$ by reflecting it about $y = a$ to obtain an even function on $[2a - b, b]$. The Fourier series of an even function on a symmetric interval contains only cosine terms (sine coefficients vanish by symmetry). Restricting back to $[a,b]$ gives the cosine-only expansion.

    This is equivalent to performing a **half-range cosine expansion** on $[a,b]$, which implicitly assumes that the function is symmetric about the left boundary $y = a$. Formally, define $g(z) = f(a + z)$ on $[0, b-a]$ and extend $g$ evenly to $[-(b-a), b-a]$. The Fourier series of the even extension is

    $$
    g(z) = \frac{a_0}{2} + \sum_{k=1}^{\infty} a_k \cos\!\left(\frac{k\pi z}{b-a}\right)
    $$

    which, substituting back $z = y - a$, gives the cosine expansion on $[a,b]$.

    The **implicit symmetry assumption** is that $f$ can be smoothly extended as an even function about $y = a$ (and $y = b$). For densities that vanish at the boundaries (which is the case when $[a,b]$ is chosen wide enough), this assumption is essentially exact --- the density is near zero at the endpoints, so the even reflection is smooth. This is why the COS method works so well: the cumulant-based truncation ensures $f(a) \approx f(b) \approx 0$, making the even extension arbitrarily smooth.

    A full Fourier series (with both sines and cosines) would also work but would require twice as many terms for the same accuracy, since half the coefficients (the sine terms) carry no additional information about a function that is effectively even at the boundaries.

---

**Exercise 2.**
The density coefficients are $A_k = \operatorname{Re}[\varphi(k\pi/(b-a))\exp(-ik\pi a/(b-a))]$. Show that $A_0 = \operatorname{Re}[\varphi(0)] = 1$ (since $\varphi(0) = 1$ for any characteristic function). What does this coefficient represent in terms of the density?

??? success "Solution to Exercise 2"
    The density coefficients are

    $$
    A_k = \frac{2}{b-a}\operatorname{Re}\!\left[\varphi\!\left(\frac{k\pi}{b-a}\right)\exp\!\left(-i\frac{k\pi a}{b-a}\right)\right]
    $$

    For $k = 0$, the frequency is $u_0 = 0$, so

    $$
    A_0 = \frac{2}{b-a}\operatorname{Re}\!\left[\varphi(0)\cdot e^{0}\right] = \frac{2}{b-a}\operatorname{Re}[\varphi(0)]
    $$

    By definition, the characteristic function at zero is

    $$
    \varphi(0) = \mathbb{E}\!\left[e^{i \cdot 0 \cdot Y}\right] = \mathbb{E}[1] = 1
    $$

    for any random variable $Y$. Therefore

    $$
    A_0 = \frac{2}{b-a} \cdot 1 = \frac{2}{b-a}
    $$

    **Interpretation.** In the COS expansion, the $k = 0$ term (with the half-weight from the prime notation) contributes $\frac{1}{2}A_0 = \frac{1}{b-a}$ to the density approximation. This is exactly the density of a uniform distribution on $[a,b]$, which integrates to 1 over $[a,b]$. The $k = 0$ coefficient captures the total probability mass of the density on $[a,b]$: when the truncation interval is wide enough, essentially all the mass lies in $[a,b]$, so $A_0 = 2/(b-a)$ ensures the approximated density integrates to 1. The remaining coefficients $A_k$ for $k \geq 1$ provide the shape corrections that sculpt the uniform baseline into the actual density.

---

**Exercise 3.**
For a European call with payoff $(e^y - 1)^+$ (in log-moneyness), the payoff coefficients $V_k$ involve the chi and psi auxiliary functions. Verify that $V_0^{\text{call}} = \chi_0(0, b) - \psi_0(0, b)$ where $\chi_0$ and $\psi_0$ have simple closed-form expressions.

??? success "Solution to Exercise 3"
    Working in log-moneyness coordinates $y = \log(S_T/K)$ so that the payoff is $(e^y - 1)^+$ and the exercise boundary is at $y = 0$. The integration domain in log-moneyness is $[\tilde{a}, \tilde{b}]$ where $\tilde{a} = a - \log K$ and $\tilde{b} = b - \log K$.

    For $k = 0$, using $\omega_0 = 0$:

    **The chi function at $k=0$:**

    $$
    \chi_0(0, b) = \int_0^b e^y \cos(0) \, dy = \int_0^b e^y \, dy = e^b - e^0 = e^b - 1
    $$

    **The psi function at $k=0$:**

    $$
    \psi_0(0, b) = \int_0^b \cos(0) \, dy = b - 0 = b
    $$

    (Here we use the convention from the section where $a$ is the left bound of the COS domain; the integration limits $[0, b]$ refer to the payoff integration range within the COS domain.)

    Therefore the $k=0$ call payoff coefficient is

    $$
    V_0^{\text{call}} = \chi_0(0, b) - 1 \cdot \psi_0(0, b) = (e^b - 1) - b
    $$

    This makes intuitive sense: $V_0^{\text{call}}$ is the average of the call payoff $(e^y - 1)^+$ over $[a,b]$ (up to the $2/(b-a)$ scaling), evaluated using the $k=0$ cosine basis function $\cos(0) = 1$. It represents the zeroth-order (constant) Fourier approximation of the payoff, weighted by the uniform part of the density.

---

**Exercise 4.**
The COS method evaluates the CF at frequencies $u_k = k\pi/(b-a)$. For a truncation range $b - a = 10$ and $N = 64$, the maximum frequency is $u_{63} = 63\pi/10 \approx 19.8$. Is this sufficient for the Heston CF to have decayed to negligible levels? Estimate $|\varphi(19.8)|$ for $v_0 = 0.04$ and $\tau = 0.5$.

??? success "Solution to Exercise 4"
    With $b - a = 10$ and $N = 64$, the maximum frequency is

    $$
    u_{63} = \frac{63\pi}{10} = \frac{63 \times 3.14159\ldots}{10} \approx 19.79
    $$

    We need to estimate $|\varphi_{\text{Heston}}(19.79)|$ for $v_0 = 0.04$ and $\tau = 0.5$.

    For large $|u|$, the Heston CF decays approximately as

    $$
    |\varphi(u)| \approx \exp\!\left(-\frac{v_0 + \theta}{2}\,\tau\,\frac{u^2}{2}\right) \cdot \text{(slower corrections)}
    $$

    More precisely, for large $u$ the Riccati function $D(\tau, u)$ behaves as $D \approx -\frac{u^2}{2\kappa_u}\,(1 - e^{-\kappa_u \tau})$ where $\kappa_u \approx i\rho\xi u - \kappa + O(1)$. A crude but useful estimate is

    $$
    |\varphi(u)| \lesssim \exp\!\left(-c \, u^2\right)
    $$

    where $c$ depends on $v_0, \theta, \kappa, \xi, \tau$. For the given parameters with moderate $\xi = 0.3$:

    The effective decay at $u = 19.8$ can be estimated from the exponential convergence rate. From the benchmarks, the COS error at $N = 64$ (maximum $u \approx 19.8$) is about $10^{-6}$, implying $|A_{63}| \cdot |V_{63}| \approx 10^{-6}$. Since $|V_k| = O(1/k^2) \approx 2.5 \times 10^{-4}$ for $k = 63$, we get $|A_{63}| \approx 4 \times 10^{-3}$, and since $A_k \propto |\varphi(u_k)|$:

    $$
    |\varphi(19.8)| \approx \frac{b-a}{2}\,|A_{63}| \approx 5 \times 0.004 = 0.02
    $$

    This is small but not negligible, which explains why $N = 64$ achieves only $10^{-6}$ accuracy and not machine precision. With $N = 128$ (maximum $u \approx 39.9$), $|\varphi(39.9)|$ is many orders of magnitude smaller, yielding $10^{-9}$ accuracy.

    The answer to whether $u_{\max} = 19.8$ is sufficient depends on the target accuracy. For 6-digit accuracy (calibration), yes --- the CF has decayed enough. For 10+ digit accuracy, $N = 128$ or 256 is needed to push $u_{\max}$ higher.

---

**Exercise 5.**
The prime notation $\sum'$ means the $k = 0$ term is halved. Show that this is equivalent to using the trapezoidal rule for the inverse cosine transform. What accuracy improvement does this provide compared to simply summing all terms with equal weight?

??? success "Solution to Exercise 5"
    The prime notation $\sum_{k=0}^{N-1}{}'$ means

    $$
    \sum_{k=0}^{N-1}{}' c_k = \frac{c_0}{2} + c_1 + c_2 + \cdots + c_{N-1}
    $$

    **Connection to the trapezoidal rule.** The inverse cosine transform recovers the function from its coefficients:

    $$
    f(y) = \int_0^{\infty} \hat{f}(u) \cos(u(y-a))\,du \approx \sum_{k=0}^{N-1} \hat{f}(u_k) \cos(u_k(y-a))\,\Delta u
    $$

    where $u_k = k\pi/(b-a)$ and $\Delta u = \pi/(b-a)$. Applying the trapezoidal rule to this integral with nodes $u_0, u_1, \ldots, u_{N-1}$, the first and last terms are halved:

    $$
    \int_0^{u_{N-1}} g(u)\,du \approx \Delta u\left[\frac{g(u_0)}{2} + g(u_1) + \cdots + g(u_{N-2}) + \frac{g(u_{N-1})}{2}\right]
    $$

    Since $\hat{f}(u_k)$ decays exponentially, the last term $g(u_{N-1})$ is negligible, and halving it makes no practical difference. But halving the first term $g(u_0) = \hat{f}(0)\cos(0) = \hat{f}(0)$ does matter: $\hat{f}(0)$ is the total mass under the density, which is the largest coefficient.

    **Accuracy improvement.** Without the half-weight on $k=0$, the sum overestimates the integral by approximately $\frac{1}{2}\hat{f}(0)\Delta u$. For a density with $\hat{f}(0) = 1$, this excess is $\frac{\pi}{2(b-a)}$, which introduces an $O(1)$ bias in the price. With the trapezoidal (prime) weighting, this leading-order error is eliminated, and the remaining error is $O(1/N^2)$ for smooth integrands (the standard trapezoidal rule error bound). For analytic integrands, the trapezoidal rule on equally-spaced nodes converges exponentially (by the Euler-Maclaurin formula), which is consistent with the observed exponential convergence of the COS method.

---

**Exercise 6.**
Implement the COS method for a European put under Heston. The put payoff coefficients use the integration range $[a, 0]$ instead of $[0, b]$. Verify put-call parity by computing both the COS call and COS put prices and checking $C - P = S_0 e^{-qT} - Ke^{-rT}$.

??? success "Solution to Exercise 6"
    For a European put with payoff $v(y) = (K - e^y)^+$, the payoff is nonzero for $y < \log K = \ell$. The COS payoff coefficients are

    $$
    V_k^{\text{put}} = K\,\psi_k(a, \ell) - \chi_k(a, \ell)
    $$

    where the integration range is $[a, \ell]$ (instead of $[\ell, b]$ for the call).

    **Verification of put-call parity.** The COS prices are

    $$
    C = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k\,V_k^{\text{call}}, \qquad P = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k\,V_k^{\text{put}}
    $$

    The difference is

    $$
    C - P = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k\,(V_k^{\text{call}} - V_k^{\text{put}})
    $$

    We compute

    $$
    V_k^{\text{call}} - V_k^{\text{put}} = \chi_k(\ell,b) - K\psi_k(\ell,b) - K\psi_k(a,\ell) + \chi_k(a,\ell)
    $$

    $$
    = [\chi_k(a,\ell) + \chi_k(\ell,b)] - K[\psi_k(a,\ell) + \psi_k(\ell,b)]
    $$

    $$
    = \chi_k(a,b) - K\psi_k(a,b)
    $$

    where we used the additivity of integrals over adjacent intervals. These are precisely the payoff coefficients of the forward contract $v(y) = e^y - K$. Therefore

    $$
    C - P = e^{-r\tau}\sum_{k=0}^{N-1}{}' A_k\,[\chi_k(a,b) - K\psi_k(a,b)]
    $$

    Now, $\sum' A_k\,\chi_k(a,b)$ is the COS approximation of $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r-q)\tau}$ (the forward price), and $\sum' A_k\,\psi_k(a,b)$ approximates $\int_a^b f(y)\,dy = 1$. With sufficient $N$ (so truncation errors are negligible):

    $$
    C - P = e^{-r\tau}[S_0 e^{(r-q)\tau} - K] = S_0 e^{-q\tau} - Ke^{-r\tau}
    $$

    which is the standard put-call parity relation. With $q = 0$, $S_0 = 100$, $K = 100$, $r = 0.05$, $\tau = 1$:

    $$
    C - P = 100 - 100e^{-0.05} = 100 - 95.1229 = 4.8771
    $$

    This identity should hold to machine precision (better than $10^{-10}$) with $N = 64$ or more, since the forward contract has smooth (in fact linear) payoff coefficients, and the COS approximation of $\mathbb{E}[S_T]$ converges extremely fast.
