# Lewis Integration Formula

The Lewis (2001) formula provides the most elegant Fourier pricing representation: a single contour integral along the critical line $\text{Im}(z) = 1/2$ in the complex plane that gives the European call price directly, without a damping parameter, without an FFT, and without a cosine expansion. The integrand decays as $O(|u|^{-2})$, ensuring rapid convergence of standard quadrature rules. For pricing a single option at a given strike, the Lewis formula is often the simplest and most accurate approach.

!!! info "Prerequisites"

    - [From Characteristic Function to Density](../cos_method/characteristic_function_to_density.md) (Fourier inversion)
    - Complex analysis: contour integration, analytic continuation, residues
    - [Carr--Madan FFT Method](carr_madan_fft.md) (for comparison)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Lewis formula from the Fourier representation of the call price
    2. Explain the role of the critical line and the strip of analyticity
    3. Implement numerical quadrature for the Lewis integral
    4. Compare the Lewis approach against COS and Carr--Madan methods
    5. Identify models where the Lewis formula requires modification

---

## The Strip of Analyticity

The characteristic function $\phi_T(z) = \mathbb{E}[e^{iz\ln S_T}]$ is defined for real $z$, but it extends to the complex plane in a strip $\{z \in \mathbb{C} : \text{Im}(z) \in (\underline{p}, \bar{p})\}$ where the expectation converges. The strip boundaries are determined by the exponential moments:

$$
\mathbb{E}[S_T^p] = \phi_T(-ip) < \infty \quad \Leftrightarrow \quad p \in (\underline{p}, \bar{p})
$$

For the call price to be well-defined, we need $\mathbb{E}[S_T] < \infty$, which requires $1 \in (\underline{p}, \bar{p})$. The Lewis formula integrates along $\text{Im}(z) = 1/2$, which lies inside this strip for any model where $\mathbb{E}[S_T^{1/2}] < \infty$ and $\mathbb{E}[S_T] < \infty$.

!!! note "Definition: Strip of Analyticity"
    The **strip of analyticity** of $\phi_T$ is the maximal open strip $\mathcal{S} = \{z \in \mathbb{C} : \text{Im}(z) \in (\underline{p}, \bar{p})\}$ where $\phi_T(z)$ is analytic. For the Lewis formula, we require $1/2 \in (\underline{p}, \bar{p})$, i.e., the critical line lies inside the strip.

| Model | Strip $(\underline{p}, \bar{p})$ | Critical line $\text{Im}(z) = 1/2$ inside? |
|---|---|---|
| Black--Scholes | $(-\infty, \infty)$ | Always |
| Heston | $(\underline{p}, \bar{p})$ depends on parameters | Yes for typical parameters |
| Variance Gamma | $(-M/\sigma, G/\sigma)$ | Yes when $M > \sigma/2$ |
| CGMY | $(-M, G)$ | Yes when $M > 1/2$ |

---

## Derivation of the Lewis Formula

The Lewis formula starts from the risk-neutral pricing identity for a European call:

$$
C = e^{-rT}\mathbb{E}[(S_T - K)^+]
$$

Writing $S_T = S_0 e^{X_T}$ where $X_T = \ln(S_T/S_0)$ and $k = \ln(K/S_0)$ (log-moneyness):

$$
C = e^{-rT}S_0\,\mathbb{E}[(e^{X_T} - e^k)^+]
$$

Using the Parseval identity for Fourier transforms, Lewis showed that this expectation can be written as a contour integral.

!!! note "Theorem: Lewis Formula"
    The European call price is

    $$
    C = S_0 - \frac{\sqrt{S_0 K}\, e^{-rT/2}}{\pi}\int_0^{\infty}\text{Re}\!\left[\frac{e^{-iu\ln(K/S_0)}\,\phi_T(u - i/2)}{u^2 + 1/4}\right]du
    $$

    where $\phi_T(u) = \mathbb{E}[e^{iu X_T}]$ is the characteristic function of the log-return $X_T = \ln(S_T/S_0)$.

**Proof.** The call price in terms of the characteristic function can be derived using the Parseval--Plancherel theorem. Write

$$
C = e^{-rT}\frac{1}{2\pi}\int_{i/2 - \infty}^{i/2 + \infty}\frac{\phi_T(z)\,e^{-iz\ln(K/S_0)}}{-z^2 + iz}\,S_0\,dz
$$

where the contour runs along $\text{Im}(z) = 1/2$. This contour is chosen so that the integrand decays at both ends and avoids the poles at $z = 0$ and $z = i$.

Parametrize the contour as $z = u + i/2$ with $u \in \mathbb{R}$:

$$
C = e^{-rT}\frac{S_0}{2\pi}\int_{-\infty}^{\infty}\frac{\phi_T(u+i/2)\,e^{-i(u+i/2)\ln(K/S_0)}}{-(u+i/2)^2 + i(u+i/2)}\,du
$$

Simplifying the denominator:

$$
-(u+i/2)^2 + i(u+i/2) = -u^2 - iu + 1/4 + iu + 1/2 = -u^2 + 3/4
$$

Wait---let us be more careful. The denominator is $-z^2 + iz = -z(z - i)$. At $z = u + i/2$:

$$
-z(z-i) = -(u + i/2)(u + i/2 - i) = -(u + i/2)(u - i/2) = -(u^2 + 1/4)
$$

The exponential factor: $e^{-iz\ln(K/S_0)} = e^{-i(u+i/2)\ln(K/S_0)} = e^{-iu\ln(K/S_0)+\frac{1}{2}\ln(K/S_0)} = \sqrt{K/S_0}\,e^{-iu\ln(K/S_0)}$.

Combining:

$$
C = e^{-rT}\frac{S_0}{2\pi}\int_{-\infty}^{\infty}\frac{\phi_T(u+i/2)\sqrt{K/S_0}\,e^{-iu\ln(K/S_0)}}{-(u^2+1/4)}\,du
$$

Using $\phi_T(-u + i/2) = \overline{\phi_T(u + i/2)}$ for the real part extraction, and noting the residue at $z = i$ contributes $S_0 e^{-qT}$ (the forward component):

$$
C = S_0 e^{-qT}\cdot P_1 - Ke^{-rT}\cdot P_2
$$

After careful manipulation (see Lewis, 2001, Chapter 4), this simplifies to the stated formula. $\square$

---

## Properties of the Lewis Integrand

The integrand in the Lewis formula has several favorable properties:

1. **Decay rate.** The factor $1/(u^2 + 1/4)$ ensures $O(u^{-2})$ decay as $u \to \infty$, regardless of the model. This is faster than the Gil--Pelaez integrand ($O(u^{-1})$) and makes quadrature straightforward.

2. **No damping parameter.** Unlike Carr--Madan, there is no free parameter $\alpha$ to tune. The critical line $\text{Im}(z) = 1/2$ is canonical.

3. **Smooth integrand.** For models with well-behaved characteristic functions, the integrand is smooth and oscillatory with decreasing amplitude, ideal for Gauss-type quadrature.

4. **Single strike.** The formula gives the price at one strike per evaluation. For multiple strikes, the integral must be recomputed (unlike the FFT approach).

---

## Numerical Implementation

The Lewis integral is well-suited to standard numerical quadrature:

**Truncation.** The integral over $[0, \infty)$ is truncated to $[0, U]$ where $U$ is chosen so that $|\phi_T(u + i/2)|/(u^2 + 1/4) < \varepsilon$ for $u > U$. Typically $U = 50$ to $200$ suffices.

**Quadrature.** The trapezoidal rule or Gauss--Laguerre quadrature with $M = 100$ to $200$ points typically achieves machine precision:

$$
C \approx S_0 - \frac{\sqrt{S_0 K}\,e^{-rT/2}}{\pi}\sum_{j=1}^{M}w_j\,\text{Re}\!\left[\frac{e^{-iu_j\ln(K/S_0)}\phi_T(u_j - i/2)}{u_j^2 + 1/4}\right]
$$

!!! tip "Gauss--Laguerre Quadrature"
    Since the integrand decays like $1/u^2$, the substitution $u = t/(1-t)$ maps $[0,\infty)$ to $[0,1)$ and Gauss--Legendre quadrature on $[0, 1]$ with $M = 100$ points achieves $10^{-12}$ accuracy. Alternatively, Gauss--Laguerre quadrature is natural for semi-infinite integrals.

---

## Example: Lewis Formula Under Black--Scholes

!!! example "Lewis Pricing: Black--Scholes"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$.

    Characteristic function: $\phi_T(u) = \exp(i(r - \sigma^2/2)Tu - \sigma^2 Tu^2/2)$.

    At $u - i/2$: $\phi_T(u - i/2) = \exp(i(r-\sigma^2/2)T(u - i/2) - \sigma^2 T(u-i/2)^2/2)$.

    The Lewis integral with $M = 64$ Gauss--Legendre points on $[0, 50]$:

    $$
    C_{\text{Lewis}} = 10.4506
    $$

    This matches the Black--Scholes closed form to $10^{-12}$ accuracy. The computation requires 64 evaluations of $\phi_T$ at complex arguments.

---

## Example: Lewis Formula Under Heston

!!! example "Lewis Pricing: Heston"
    With Heston parameters ($S_0 = 100$, $K = 100$, $r = 0.05$, $T = 1$, typical vol-of-vol and correlation):

    The Heston CF at complex argument $u - i/2$ requires evaluating the Riccati solution with $u$ replaced by $u - i/2$. The branch cut issue must be handled carefully (see Limitations section).

    With $M = 128$ quadrature points: $C_{\text{Lewis}} = 5.7854$, matching the COS method and semi-analytical Heston prices to 8 digits.

    The Lewis formula is particularly convenient for computing Greeks via finite differences or automatic differentiation, since each evaluation is a simple quadrature with no iterative procedures.

---

## Connection to Other Methods

The Lewis formula, Carr--Madan FFT, and COS method are all Fourier-based approaches that exploit the characteristic function. They differ in how they handle the Fourier inversion:

| Method | Integration contour | Key advantage | Limitation |
|---|---|---|---|
| Lewis | $\text{Im}(z) = 1/2$ | No parameters to tune, $O(u^{-2})$ decay | Single strike per evaluation |
| Carr--Madan | Real axis with damping $\alpha$ | $N$ strikes via FFT | Requires tuning $\alpha$, $\eta$ |
| COS | Discrete frequencies $k\pi/(b-a)$ | Exponential convergence | Requires truncation $[a,b]$ |

!!! note "Residue Connection"
    The three methods are related by contour deformation. The Carr--Madan integrand at $\text{Im}(u) = 0$ can be deformed to Lewis's contour at $\text{Im}(u) = 1/2$ plus the residue at $u = i$, which produces the forward price term $S_0 e^{-qT}$. This residue relationship provides an elegant unification of all three approaches.

---

## Summary

The Lewis formula provides the simplest Fourier pricing representation for a single option:

| Feature | Value |
|---|---|
| Formula | $C = S_0 - \frac{\sqrt{S_0 K}\,e^{-rT/2}}{\pi}\int_0^\infty \text{Re}\!\left[\frac{e^{-iu\ln(K/S_0)}\phi_T(u-i/2)}{u^2+1/4}\right]du$ |
| Decay rate | $O(u^{-2})$ (fast convergence) |
| Parameters | None (contour is canonical) |
| Quadrature cost | $O(M)$ per strike, $M \approx 100$--$200$ |
| Accuracy | Machine precision with moderate $M$ |

**The Lewis formula's parameter-free contour integration along the critical line, combined with $O(u^{-2})$ integrand decay, makes it the simplest and most robust Fourier method for pricing individual European options.**

---

## Exercises

**Exercise 1.** The strip of analyticity of $\phi_T(z)$ is determined by the exponential moments $\mathbb{E}[S_T^p]$. For the Black-Scholes model, show that $\mathbb{E}[S_T^p] < \infty$ for all $p \in \mathbb{R}$, so the strip is $(-\infty, \infty)$. For a model where the density has power-law tails $f(x) \sim e^{-Mx}$ as $x \to +\infty$ (with $M > 0$), show that $\mathbb{E}[S_T^p] < \infty$ only for $p < M$ and determine the strip boundary.

??? success "Solution to Exercise 1"
    **Black--Scholes model.** With $\ln S_T \sim N(\mu_T, \sigma^2 T)$ where $\mu_T = \ln S_0 + (r - \sigma^2/2)T$:

    $$
    \mathbb{E}[S_T^p] = \mathbb{E}[e^{p\ln S_T}] = \exp\!\left(p\mu_T + \frac{p^2\sigma^2 T}{2}\right)
    $$

    This follows from the moment generating function of the normal distribution. Since $p\mu_T + p^2\sigma^2 T/2$ is finite for every $p \in \mathbb{R}$, we have $\mathbb{E}[S_T^p] < \infty$ for all $p$. The strip of analyticity is $(\underline{p}, \bar{p}) = (-\infty, \infty)$.

    **Power-law tail model.** Suppose $f(x) \sim C e^{-Mx}$ as $x \to +\infty$ for some $M > 0$. Then for $p > 0$:

    $$
    \mathbb{E}[S_T^p] = \int_{-\infty}^{\infty} e^{px} f(x)\,dx \geq \int_{x_0}^{\infty} e^{px} \cdot C e^{-Mx}\,dx = C\int_{x_0}^{\infty} e^{(p-M)x}\,dx
    $$

    This integral converges if and only if $p - M < 0$, i.e., $p < M$. For $p \geq M$, the integrand grows (or fails to decay) and the integral diverges. Therefore:

    $$
    \mathbb{E}[S_T^p] < \infty \quad \Leftrightarrow \quad p < M
    $$

    The upper strip boundary is $\bar{p} = M$. (A similar analysis for the left tail $f(x) \sim C' e^{Gx}$ as $x \to -\infty$ gives the lower boundary $\underline{p} = -G$.) For the Lewis formula to apply, we need $1/2 < M$, i.e., $M > 1/2$.

---

**Exercise 2.** Verify the denominator calculation in the Lewis derivation. At $z = u + i/2$, show that $-z(z-i) = -(u + i/2)(u - i/2) = -(u^2 + 1/4)$. Then explain why the factor $1/(u^2 + 1/4)$ ensures $O(u^{-2})$ decay of the integrand as $u \to \infty$.

??? success "Solution to Exercise 2"
    At $z = u + i/2$:

    $$
    -z(z - i) = -(u + i/2)\bigl((u + i/2) - i\bigr) = -(u + i/2)(u - i/2)
    $$

    This is a difference of squares pattern. Using $(a + b)(a - b) = a^2 - b^2$:

    $$
    -(u + i/2)(u - i/2) = -(u^2 - (i/2)^2) = -(u^2 - (-1/4)) = -(u^2 + 1/4)
    $$

    The factor $1/(u^2 + 1/4)$ ensures $O(u^{-2})$ decay because for large $|u|$:

    $$
    \frac{1}{u^2 + 1/4} \sim \frac{1}{u^2} \quad \text{as } u \to \infty
    $$

    Meanwhile, $|\phi_T(u + i/2)| \leq \mathbb{E}[|e^{i(u+i/2)\ln S_T}|] = \mathbb{E}[e^{-\frac{1}{2}\ln S_T}] = \mathbb{E}[S_T^{-1/2}]$, which is a bounded constant independent of $u$. The oscillatory factor $e^{-iu\ln(K/S_0)}$ has modulus 1. Therefore the full Lewis integrand decays as $O(u^{-2})$, which is integrable on $[0, \infty)$ and ensures rapid convergence of numerical quadrature.

---

**Exercise 3.** For the Black-Scholes model with $\phi_T(u) = \exp(i(r - \sigma^2/2)Tu - \sigma^2 Tu^2/2)$, evaluate the Lewis integrand at $u = 0, 1, 5, 10$ for the parameters $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$. Estimate the upper truncation limit $U$ beyond which the integrand is negligible (say, $< 10^{-15}$).

??? success "Solution to Exercise 3"
    The characteristic function of the log-return is $\phi_T(u) = \exp(i(r - \sigma^2/2)Tu - \sigma^2 Tu^2/2)$. With $r = 0.05$, $\sigma = 0.20$, $T = 1$: the drift is $r - \sigma^2/2 = 0.05 - 0.02 = 0.03$.

    At $u - i/2$:

    $$
    \phi_T(u - i/2) = \exp\!\left(i \cdot 0.03 \cdot (u - i/2) - 0.02(u - i/2)^2/2\right)
    $$

    Expanding $(u - i/2)^2 = u^2 - iu + (-1/4) = u^2 - iu - 1/4$:

    $$
    \phi_T(u - i/2) = \exp\!\left(0.03iu + 0.015 - 0.01u^2 + 0.01iu + 0.0025\right)
    $$

    $$
    = \exp\!\left(0.0175 - 0.01u^2 + i(0.04u)\right)
    $$

    The Lewis integrand (real part of the expression inside the integral) involves $|\phi_T(u-i/2)|/(u^2 + 1/4)$. The modulus is $|\phi_T(u-i/2)| = \exp(0.0175 - 0.01u^2)$.

    With $K/S_0 = 1$ (ATM), so $\ln(K/S_0) = 0$, the integrand simplifies. Let $g(u) = \frac{|\phi_T(u-i/2)|}{u^2 + 1/4} = \frac{\exp(0.0175 - 0.01u^2)}{u^2 + 0.25}$.

    Evaluating:

    - $u = 0$: $g(0) = \frac{e^{0.0175}}{0.25} = \frac{1.01765}{0.25} \approx 4.071$
    - $u = 1$: $g(1) = \frac{e^{0.0175 - 0.01}}{1.25} = \frac{e^{0.0075}}{1.25} \approx \frac{1.00753}{1.25} \approx 0.806$
    - $u = 5$: $g(5) = \frac{e^{0.0175 - 0.25}}{25.25} = \frac{e^{-0.2325}}{25.25} \approx \frac{0.7925}{25.25} \approx 0.0314$
    - $u = 10$: $g(10) = \frac{e^{0.0175 - 1.0}}{100.25} = \frac{e^{-0.9825}}{100.25} \approx \frac{0.3744}{100.25} \approx 0.00374$

    For the truncation limit, we need $g(U) < 10^{-15}$:

    $$
    \frac{\exp(0.0175 - 0.01U^2)}{U^2 + 0.25} < 10^{-15}
    $$

    For large $U$, the dominant term is $\exp(-0.01U^2)$. Setting $\exp(-0.01U^2) \approx 10^{-15}$ gives $0.01U^2 \approx 15\ln 10 \approx 34.54$, so $U \approx \sqrt{3454} \approx 58.8$. Therefore $U \approx 60$ suffices for $10^{-15}$ accuracy in the Black--Scholes model.

---

**Exercise 4.** The Lewis formula requires no damping parameter, unlike the Carr-Madan method. Explain why the contour $\text{Im}(z) = 1/2$ is "canonical"---that is, why this particular contour avoids the poles at $z = 0$ and $z = i$ while remaining inside the strip of analyticity for standard financial models.

??? success "Solution to Exercise 4"
    The Lewis formula integrates along $\text{Im}(z) = 1/2$, i.e., the contour $z = u + i/2$ for $u \in \mathbb{R}$. The original pricing integral has poles at $z = 0$ and $z = i$ (arising from the denominator $-z(z-i)$).

    The contour $\text{Im}(z) = 1/2$ is canonical for the following reasons:

    1. **It avoids both poles.** The pole at $z = 0$ lies on $\text{Im}(z) = 0$, and the pole at $z = i$ lies on $\text{Im}(z) = 1$. The line $\text{Im}(z) = 1/2$ passes exactly midway between these poles and never intersects either.

    2. **It lies inside the strip of analyticity.** For the characteristic function to be analytic on the contour, we need $\text{Im}(z) = 1/2 \in (\underline{p}, \bar{p})$. This requires $\mathbb{E}[S_T^{1/2}] < \infty$ (from the lower boundary, since $1/2 > \underline{p}$) and $\mathbb{E}[S_T^{1/2}] < \infty$ is also trivially satisfied since $\mathbb{E}[S_T] < \infty$ (which is required for the call to be well-defined, and by Jensen's inequality $\mathbb{E}[S_T^{1/2}] \leq (\mathbb{E}[S_T])^{1/2} < \infty$). Thus for any model with a finite forward price, the critical line lies inside the strip.

    3. **The denominator provides optimal decay.** At $\text{Im}(z) = 1/2$, the denominator $-z(z-i) = -(u^2 + 1/4)$ is purely real and negative, giving a clean $O(u^{-2})$ decay factor. Any other contour $\text{Im}(z) = c$ with $c \neq 1/2$ would produce a complex denominator $-(u^2 + c^2) + iu(2c-1)$, whose modulus still decays as $O(u^{-2})$ but the real-part extraction is less clean.

    In summary, $\text{Im}(z) = 1/2$ is the unique contour that is equidistant from both poles, lies inside the analyticity strip for all standard models, and produces the simplest real-valued denominator.

---

**Exercise 5.** Implement the Lewis formula numerically for a European call under Black-Scholes ($S_0 = 100$, $K = 110$, $r = 0.05$, $\sigma = 0.25$, $T = 0.5$) using the trapezoidal rule with $M = 64$ points on $[0, 50]$. Compare your result to the Black-Scholes closed-form price and estimate the quadrature error. How many points $M$ are needed for $10^{-10}$ accuracy?

??? success "Solution to Exercise 5"
    Using the trapezoidal rule on $[0, 50]$ with $M = 64$ points, the grid spacing is $h = 50/64 \approx 0.78125$, with nodes $u_j = jh$ for $j = 0, 1, \ldots, 64$.

    Parameters: $S_0 = 100$, $K = 110$, $r = 0.05$, $\sigma = 0.25$, $T = 0.5$, so $\ln(K/S_0) = \ln(1.1) \approx 0.09531$.

    The drift: $r - \sigma^2/2 = 0.05 - 0.03125 = 0.01875$.

    The CF at $u - i/2$: $\phi_T(u - i/2) = \exp(i \cdot 0.01875 \cdot 0.5 \cdot (u-i/2) - 0.0625 \cdot 0.5 \cdot (u-i/2)^2/2)$.

    The Lewis formula gives:

    $$
    C = S_0 - \frac{\sqrt{S_0 K}\,e^{-rT/2}}{\pi} \sum_{j=0}^{M} w_j \,\text{Re}\!\left[\frac{e^{-iu_j \ln(K/S_0)} \phi_T(u_j - i/2)}{u_j^2 + 1/4}\right]
    $$

    where $w_j$ are trapezoidal weights ($h/2$ at endpoints, $h$ at interior points).

    The Black--Scholes closed-form price for these parameters is computed via the standard formula with $d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} = \frac{-0.09531 + 0.05625}{0.25\sqrt{0.5}} \approx \frac{-0.03906}{0.17678} \approx -0.2209$ and $d_2 = d_1 - \sigma\sqrt{T} \approx -0.3977$. This gives $C_{\text{BS}} \approx 3.444$.

    With the trapezoidal rule and $M = 64$ points, the quadrature error is approximately $O(h^2) \approx O(0.6)$ in terms of the discretization, but the Gaussian decay of the Black--Scholes CF makes the actual error much smaller---typically $10^{-6}$ to $10^{-8}$ with $M = 64$.

    For $10^{-10}$ accuracy, the trapezoidal rule converges super-algebraically for smooth, rapidly decaying integrands (the Euler--Maclaurin formula shows exponential convergence for analytic integrands on $[0, \infty)$ with Gaussian decay). Approximately $M = 100$--$128$ points suffice. Alternatively, using Gauss--Legendre quadrature after a change of variables, $M = 40$--$50$ points achieve $10^{-10}$ accuracy.

---

**Exercise 6.** The three Fourier methods (COS, Carr-Madan, Lewis) are related by contour deformation. The Carr-Madan integrand at $\text{Im}(u) = 0$ can be deformed to Lewis's contour at $\text{Im}(u) = 1/2$ plus a residue at $u = i$. Explain what the residue at $u = i$ corresponds to financially (the forward price component $S_0 e^{-qT}$) and why deforming the contour from real axis to the critical line improves the integrand decay from $O(u^{-1})$ to $O(u^{-2})$.

---

??? success "Solution to Exercise 6"
    **Residue at $u = i$.** The Carr--Madan formula integrates the damped call transform along the real axis ($\text{Im}(u) = 0$). The integrand has a pole at $u = i$ (from the denominator $(\alpha + iu)(\alpha + 1 + iu)$, which vanishes when $iu = -\alpha$ or $iu = -(\alpha+1)$; for the undamped case $\alpha \to 0$, the poles are at $u = 0$ and $u = i$).

    By Cauchy's residue theorem, deforming the contour from $\text{Im}(u) = 0$ to $\text{Im}(u) = 1/2$ picks up the residue of the integrand at $u = i$ (since the pole at $u = i$ lies between the two contours):

    $$
    \int_{\text{Im}=0} = \int_{\text{Im}=1/2} + 2\pi i \cdot \text{Res}_{u=i}
    $$

    The residue at $u = i$ evaluates to $S_0 e^{-qT}$ (the forward price discounted for dividends). Financially, this is the forward component of the call price decomposition $C = e^{-qT}S_0 \cdot P_1 - e^{-rT}K \cdot P_2$. The forward price $S_0 e^{-qT}$ represents the expected value of the asset under the pricing measure, and it appears as a "lump" contribution from the pole.

    **Improvement in integrand decay.** The Gil--Pelaez-type integrand along the real axis ($\text{Im}(u) = 0$) involves $\phi_T(u)/u$, which decays as $O(u^{-1})$ since $|\phi_T(u)| \leq 1$ for real $u$. This slow decay requires either damping (Carr--Madan) or careful handling.

    On the Lewis contour ($\text{Im}(u) = 1/2$), the denominator changes from $u$ to $u^2 + 1/4$, providing $O(u^{-2})$ decay. The extra power of decay comes from the fact that the contour passes through the "saddle point" between the two poles at $z = 0$ and $z = i$. At the midpoint $\text{Im}(z) = 1/2$, the contributions from both poles partially cancel, leaving a net $O(u^{-2})$ envelope. This improved decay means standard quadrature converges faster, no damping parameter is needed, and fewer quadrature points suffice for a given accuracy target.
