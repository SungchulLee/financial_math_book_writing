# Characteristic Functions

A major reason stochastic volatility models (especially affine models like Heston) are practical is that many admit **closed-form characteristic functions** of the log-price. These characteristic functions enable efficient pricing, calibration, and risk computation via Fourier techniques.

---

## Definition and Properties

### The Characteristic Function

For a random variable $X$ with distribution $F$, the **characteristic function** is:

$$
\varphi_X(u) = \mathbb{E}[e^{iuX}] = \int_{-\infty}^{\infty} e^{iux}\,dF(x), \quad u \in \mathbb{R}
$$

**Key properties:**

1. **Uniqueness:** $\varphi_X$ uniquely determines the distribution of $X$
2. **Boundedness:** $|\varphi_X(u)| \leq 1$ for all $u$
3. **Continuity:** $\varphi_X$ is uniformly continuous
4. **Moments:** If $\mathbb{E}[|X|^n] < \infty$, then $\mathbb{E}[X^n] = \frac{1}{i^n}\varphi_X^{(n)}(0)$

### Conditional Characteristic Function

For option pricing, we use the **conditional** characteristic function:

$$
\varphi(t, x, v; T, u) = \mathbb{E}^{\mathbb{Q}}\left[e^{iuX_T} \mid X_t = x, V_t = v\right]
$$

where $X_t = \log S_t$ is the log-price.

---

## Why Characteristic Functions Are Useful

### Inversion Formulas

The density can be recovered via Fourier inversion:

$$
f_X(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-iux}\varphi_X(u)\,du
$$

The distribution function via Gil-Pelaez:

$$
F_X(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty} \text{Re}\left[\frac{e^{-iux}\varphi_X(u)}{iu}\right]du
$$

### Option Pricing

European option prices can be written as integrals involving $\varphi$:

$$
C(K) = e^{-rT}\mathbb{E}[(S_T - K)^+] = e^{-rT}\int_{\log K}^{\infty}(e^x - K)f(x)\,dx
$$

Substituting the Fourier representation of $f$ yields pricing formulas.

### Computational Advantages

| Method | Cost per price | Cost for $N$ strikes |
|--------|---------------|---------------------|
| Monte Carlo | $O(M \cdot n)$ | $O(N \cdot M \cdot n)$ |
| PDE | $O(N_x \cdot N_v \cdot N_t)$ | Same |
| Fourier/FFT | $O(N_u)$ | $O(N_u \log N_u)$ |

Fourier methods are dramatically faster for calibration across many strikes.

---

## Affine Exponential Form

### General Affine Models

For affine stochastic volatility models, the characteristic function has the form:

$$
\varphi(\tau, u) = \exp\left(A(\tau, u) + B(\tau, u)V_t + iuX_t\right)
$$

where $\tau = T - t$ and $A$, $B$ solve **Riccati ODEs**.

### Heston Characteristic Function

Recall (see [§ Affine Structure](../the_heston_model/affine_structure.md)): for the Heston model, the log-price characteristic function has the affine exponential form

$$
\varphi(\tau, u) = \exp\left(C(\tau, u) + D(\tau, u)V_0 + iu\log S_0\right),
$$

where $C$ and $D$ are obtained in closed form by solving the Riccati system associated with the variance dynamics; full coefficients $C,D,d,g$ and the rotation-count fix for the "little Heston trap" are derived there. The Fourier-pricing machinery in this folder applies directly given $\varphi$.

---

## Characteristic Functions of Other Models

### Black–Scholes

Recall (see [§ Characteristic Function to Density](../../ch09/cos_method/characteristic_function_to_density.md)): for GBM with constant volatility $\sigma$, $\varphi_{\text{BS}}(\tau, u)$ is Gaussian in $u$ and serves as the standard sanity check (Heston with $\xi\to 0$).

### Variance Gamma

$$
\varphi_{\text{VG}}(\tau, u) = \exp(iu\omega\tau)\left(\frac{1}{1 - iu\theta\nu + \frac{\sigma^2\nu u^2}{2}}\right)^{\tau/\nu}
$$

### CGMY

$$
\varphi_{\text{CGMY}}(\tau, u) = \exp\left(\tau C\Gamma(-Y)\left[(M-iu)^Y - M^Y + (G+iu)^Y - G^Y\right]\right)
$$

### 3/2 Model

Semi-closed form involving confluent hypergeometric functions.

### SABR

No closed-form CF; asymptotic implied volatility formula used instead.

---

## Risk-Neutral Drift and Martingale Condition

### No-Arbitrage Constraint

Under $\mathbb{Q}$, the discounted stock price must be a martingale:

$$
\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}S_T \mid \mathcal{F}_t] = e^{-q(T-t)}S_t
$$

This implies:

$$
\varphi(\tau, -i) = e^{(r-q)\tau}
$$

### Verification

For Heston, substituting $u = -i$ into the characteristic function should yield:

$$
\varphi(\tau, -i) = \exp\left((r-q)\tau + 0 \cdot V_0 + \log S_0\right) \cdot e^{-\log S_0} = e^{(r-q)\tau}
$$

This is the **martingale condition** and should be verified numerically.

---

## Complex-Valued Extensions

### Analytic Continuation

The characteristic function $\varphi(u)$ for real $u$ can often be extended to complex $u$:

$$
\varphi(u + iv) = \mathbb{E}[e^{i(u+iv)X}] = \mathbb{E}[e^{iuX - vX}]
$$

This requires $\mathbb{E}[e^{-vX}] < \infty$, i.e., moments must exist.

### Strip of Regularity

For Heston, $\varphi(u)$ is analytic in the strip:

$$
\{u \in \mathbb{C} : \text{Im}(u) \in (-u^-, u^+)\}
$$

where $u^-$ and $u^+$ depend on model parameters (related to moment explosion).

### Importance for Pricing

Recall (see [§ Carr–Madan FFT](../../ch09/alternative_fourier/carr_madan_fft.md), [§ Lewis Integration Formula](../../ch09/alternative_fourier/lewis_integration_formula.md)): Fourier pricing methods evaluate $\varphi$ at complex $u$ (Carr–Madan at $u - i(\alpha+1)$, Lewis at $u - i/2$), and the strip of regularity determines admissible damping.

---

## Moment Existence and Explosion

### Critical Moment

For Heston, the $n$-th moment $\mathbb{E}[S_T^n]$ exists if and only if $n < n^*(T)$, where $n^*$ depends on $(\kappa, \theta, \xi, \rho, T)$.

**Andersen–Piterbarg condition:** The critical moment $n^*$ solves:

$$
D(\tau, -in^*) = \infty
$$

### Implications

1. **Short maturities:** Higher moments exist
2. **Long maturities:** Fewer moments exist
3. **High vol-of-vol:** Moments explode faster
4. **Pricing formulas:** Must use damping within the valid strip

### Lee's Moment Formula

Recall (see [§ Error Analysis and Convergence](../../ch09/cos_method/error_analysis_and_convergence.md)): the moment-explosion critical $n^*(T)$ controls implied-volatility wings via Lee's formula $\sigma_{\text{impl}}^2(k, T) \sim \frac{2|k|}{T}\left(1 - \frac{1}{n^*(T)}\text{sgn}(k)\right)$ as $|k| \to \infty$.

---

## Practical Implementation Notes

### Numerical Evaluation

Recall (see [§ Affine Structure](../the_heston_model/affine_structure.md)): a reference Lord–Kahl implementation of `heston_cf(u, S0, V0, kappa, theta, xi, rho, r, q, tau)` is given there; the stability rules below apply to any affine SV CF used in the Fourier-pricing machinery of this folder.

### Stability Checklist

1. **Use Lord–Kahl formulation** to avoid the "little Heston trap"
2. **Implement rotation counting** for complex logarithms
3. **Check martingale condition:** $|\varphi(-i) - e^{(r-q)\tau}| < \epsilon$
4. **Validate against Black–Scholes** when $\xi \to 0$
5. **Test at multiple $u$ values** for smoothness

### Common Pitfalls

| Issue | Symptom | Solution |
|-------|---------|----------|
| Branch cut | Discontinuous prices | Rotation counting |
| Overflow | NaN for large $\tau$ | Use stable formulation |
| Underflow | Zero for large $|u|$ | Truncate integration |
| Wrong branch of $\sqrt{}$ | Wrong sign of $d$ | Enforce $\text{Re}(d) > 0$ |

---

## Key Takeaways

- Characteristic functions are central to practical stochastic volatility pricing
- Affine models (Heston) yield exponential-affine CFs with Riccati structure
- The CF uniquely determines the distribution and enables Fourier pricing
- Analytic continuation to complex $u$ is essential for pricing formulas
- Moment existence limits the strip of regularity
- Numerical stability requires careful implementation

---

## Further Reading

- Heston, S. (1993). *A closed-form solution for options with stochastic volatility*. Review of Financial Studies.
- Carr, P. & Madan, D. (1999). *Option valuation using the fast Fourier transform*. Journal of Computational Finance.
- Duffie, D., Pan, J., & Singleton, K. (2000). *Transform analysis and asset pricing for affine jump-diffusions*. Econometrica.
- Lee, R. (2004). *The moment formula for implied volatility at extreme strikes*. Mathematical Finance.
- Lord, R. & Kahl, C. (2010). *Complex logarithms in Heston-like models*. Mathematical Finance.
- Andersen, L. & Piterbarg, V. (2007). *Moment explosions in stochastic volatility models*. Finance and Stochastics.

---

## Exercises

**Exercise 1.** The characteristic function of a standard normal random variable $Z \sim \mathcal{N}(0,1)$ is $\varphi_Z(u) = e^{-u^2/2}$. Using the moment-generating property $\mathbb{E}[Z^n] = i^{-n}\varphi_Z^{(n)}(0)$, verify that $\mathbb{E}[Z] = 0$, $\mathbb{E}[Z^2] = 1$, $\mathbb{E}[Z^3] = 0$, and $\mathbb{E}[Z^4] = 3$ by computing successive derivatives of $\varphi_Z(u)$ at $u = 0$.

??? success "Solution to Exercise 1"
    We need to compute successive derivatives of $\varphi_Z(u) = e^{-u^2/2}$ and evaluate at $u = 0$.

    **First moment ($n=1$):** We compute $\varphi_Z'(u) = -u\,e^{-u^2/2}$, so

    $$
    \mathbb{E}[Z] = \frac{1}{i}\varphi_Z'(0) = \frac{1}{i}\cdot 0 = 0
    $$

    **Second moment ($n=2$):** We compute $\varphi_Z''(u) = (u^2 - 1)e^{-u^2/2}$, so $\varphi_Z''(0) = -1$ and

    $$
    \mathbb{E}[Z^2] = \frac{1}{i^2}\varphi_Z''(0) = \frac{-1}{-1} = 1
    $$

    **Third moment ($n=3$):** We compute $\varphi_Z'''(u) = (-u^3 + 3u)e^{-u^2/2}$, so $\varphi_Z'''(0) = 0$ and

    $$
    \mathbb{E}[Z^3] = \frac{1}{i^3}\varphi_Z'''(0) = 0
    $$

    **Fourth moment ($n=4$):** We compute $\varphi_Z^{(4)}(u) = (u^4 - 6u^2 + 3)e^{-u^2/2}$, so $\varphi_Z^{(4)}(0) = 3$ and

    $$
    \mathbb{E}[Z^4] = \frac{1}{i^4}\varphi_Z^{(4)}(0) = \frac{3}{1} = 3
    $$

    These match the known moments of the standard normal: mean 0, variance 1, skewness 0, and kurtosis 3.

---

**Exercise 2.** Write the Black–Scholes characteristic function for $X_T = \log S_T$ with parameters $S_0 = 100$, $r = 3\%$, $q = 1\%$, $\sigma = 25\%$, and $T = 0.5$. Verify the martingale condition $\varphi(-i) = e^{(r-q)T}$ by substituting $u = -i$ into your formula.

??? success "Solution to Exercise 2"
    The Black-Scholes CF for $X_T = \log S_T$ is

    $$
    \varphi(u) = \exp\!\left(iu\!\left[\log S_0 + (r - q - \tfrac{\sigma^2}{2})T\right] - \frac{\sigma^2 u^2 T}{2}\right)
    $$

    Substituting the given parameters $S_0 = 100$, $r = 0.03$, $q = 0.01$, $\sigma = 0.25$, $T = 0.5$:

    $$
    \varphi(u) = \exp\!\left(iu\!\left[\log 100 + (0.03 - 0.01 - 0.03125)\cdot 0.5\right] - \frac{0.0625\,u^2\cdot 0.5}{2}\right)
    $$

    Simplifying: $0.03 - 0.01 - 0.03125 = -0.01125$ and $(-0.01125)(0.5) = -0.005625$, so

    $$
    \varphi(u) = \exp\!\left(iu[\log 100 - 0.005625] - 0.015625\,u^2\right)
    $$

    **Martingale check:** Substitute $u = -i$, so $iu = 1$ and $u^2 = -1$:

    $$
    \varphi(-i) = \exp\!\left(\log 100 - 0.005625 + 0.015625\right) = \exp(\log 100 + 0.01)
    $$

    Meanwhile $(r - q)T = (0.03 - 0.01)(0.5) = 0.01$, so

    $$
    e^{(r-q)T} \cdot S_0 = 100\,e^{0.01}
    $$

    Since $\varphi(-i) = \mathbb{E}[e^{X_T}] = \mathbb{E}[S_T]$ and we need $\mathbb{E}[S_T] = S_0\,e^{(r-q)T}$, we verify:

    $$
    \varphi(-i) = e^{\log 100 + 0.01} = 100\,e^{0.01} = S_0\,e^{(r-q)T}
    $$

    The martingale condition is satisfied.

---

**Exercise 3.** The Heston characteristic function involves the discriminant $d = \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}$. For $\kappa = 2$, $\xi = 0.4$, $\rho = -0.7$: (a) compute $d$ at $u = 0$ and verify it equals $\kappa$; (b) compute $d$ at $u = 5$ and $u = 20$, showing that $\text{Re}(d) > 0$; (c) explain why the choice of branch for the complex square root affects the result and how the Lord-Kahl formulation addresses this.

??? success "Solution to Exercise 3"
    **(a)** At $u = 0$:

    $$
    d = \sqrt{(\kappa - \rho\xi\cdot i\cdot 0)^2 + \xi^2(i\cdot 0 + 0^2)} = \sqrt{\kappa^2} = \kappa = 2
    $$

    **(b)** At $u = 5$, with $\kappa = 2$, $\xi = 0.4$, $\rho = -0.7$:

    The argument under the square root is

    $$
    (\kappa - \rho\xi\,iu)^2 + \xi^2(iu + u^2) = (2 + 0.28\cdot 5i)^2 + 0.16(5i + 25)
    $$

    $$
    = (2 + 1.4i)^2 + 0.16(25 + 5i) = (4 - 1.96 + 5.6i) + (4 + 0.8i) = 6.04 + 6.4i
    $$

    So $d = \sqrt{6.04 + 6.4i}$. Writing $6.04 + 6.4i$ in polar form: $|z| = \sqrt{6.04^2 + 6.4^2} = \sqrt{36.48 + 40.96} = \sqrt{77.44} \approx 8.80$. The angle is $\arg(z) = \arctan(6.4/6.04) \approx 0.815$ rad. Then $d \approx \sqrt{8.80}\,e^{i\cdot 0.4075} \approx 2.967\,(\cos 0.4075 + i\sin 0.4075) \approx 2.73 + 1.18i$. Since $\text{Re}(d) \approx 2.73 > 0$, the condition is satisfied.

    At $u = 20$:

    $$
    (\kappa - \rho\xi\,iu)^2 + \xi^2(iu + u^2) = (2 + 5.6i)^2 + 0.16(20i + 400)
    $$

    $$
    = (4 - 31.36 + 22.4i) + (64 + 3.2i) = 36.64 + 25.6i
    $$

    Here $|z| = \sqrt{36.64^2 + 25.6^2} \approx \sqrt{1998.4} \approx 44.7$. The principal square root gives $\text{Re}(d) \approx \sqrt{44.7}\cos(\tfrac{1}{2}\arctan(25.6/36.64)) > 0$.

    **(c)** The complex square root is a multi-valued function with two branches differing by a sign. If we choose the wrong branch (e.g., $\text{Re}(d) < 0$), the exponential $e^{d\tau}$ can grow rather than decay, causing the CF to blow up for large $\tau$. The Lord-Kahl formulation resolves this by: (i) enforcing the convention $\text{Re}(d) > 0$; and (ii) tracking the winding number of the complex logarithm $\ln(1 - ge^{-d\tau})$ along the integration path in $u$, adding $2\pi i$ corrections when discontinuities are crossed. This avoids the "little Heston trap" where the standard formulation produces discontinuous CF values.

---

**Exercise 4.** The Gil-Pelaez inversion formula for the CDF is

$$
F_X(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-iux}\varphi_X(u)}{iu}\right]du
$$

For a standard normal with $\varphi(u) = e^{-u^2/2}$, evaluate $F_X(0)$ and verify it equals $1/2$. Then set $x = 1.96$ and compute the integral numerically (using, e.g., the trapezoidal rule with $\Delta u = 0.01$ and $u_{\max} = 50$) to verify that $F_X(1.96) \approx 0.975$.

??? success "Solution to Exercise 4"
    **Evaluating $F_X(0)$:** Substitute $x = 0$ and $\varphi(u) = e^{-u^2/2}$:

    $$
    F_X(0) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty}\text{Re}\!\left[\frac{e^{-i\cdot 0\cdot u}\cdot e^{-u^2/2}}{iu}\right]du = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty}\text{Re}\!\left[\frac{e^{-u^2/2}}{iu}\right]du
    $$

    Since $\frac{1}{iu} = \frac{-i}{u}$ is purely imaginary, $\text{Re}\!\left[\frac{e^{-u^2/2}}{iu}\right] = 0$. Therefore $F_X(0) = \frac{1}{2}$, as expected for a symmetric distribution.

    **Numerical evaluation at $x = 1.96$:** We compute

    $$
    F_X(1.96) = \frac{1}{2} - \frac{1}{\pi}\int_0^{50}\text{Re}\!\left[\frac{e^{-i\cdot 1.96\cdot u}\cdot e^{-u^2/2}}{iu}\right]du
    $$

    Using the trapezoidal rule with $\Delta u = 0.01$ and $u_{\max} = 50$, we discretize:

    $$
    \int_0^{50} g(u)\,du \approx \Delta u\!\left[\frac{g(0)}{2} + \sum_{n=1}^{4999} g(n\Delta u) + \frac{g(50)}{2}\right]
    $$

    Note that $g(0) = \lim_{u\to 0}\text{Re}\!\left[\frac{e^{-1.96iu}\cdot e^{-u^2/2}}{iu}\right]$. By L'Hopital's rule (or Taylor expansion), as $u \to 0$: $e^{-1.96iu} \approx 1 - 1.96iu$, so $\frac{e^{-1.96iu}}{iu} \approx \frac{1}{iu} - 1.96$. The real part of $\frac{1}{iu}$ is zero, so $g(0) = -1.96$. Applying the trapezoidal sum numerically yields

    $$
    F_X(1.96) \approx 0.975
    $$

    confirming $\Phi(1.96) \approx 0.975$, consistent with the well-known 97.5th percentile of the standard normal.

---

**Exercise 5.** Analytic continuation of the characteristic function to complex arguments is essential for Fourier pricing. Explain why the Carr-Madan formula evaluates $\varphi(u - i(\alpha + 1))$ rather than $\varphi(u)$. If the critical moment for the Heston model is $n^*(T) = 3.5$, what is the maximum allowable damping parameter $\alpha$? What happens numerically if $\alpha$ is chosen too large?

??? success "Solution to Exercise 5"
    The Carr-Madan formula evaluates $\varphi(u - i(\alpha + 1))$ rather than $\varphi(u)$ because the call price $C(K)$ as a function of log-strike $k = \log K$ is not square-integrable: as $k \to -\infty$ (i.e., $K \to 0$), $C(K) \to S_0 e^{-qT}$, which does not decay. The damping factor $e^{\alpha k}$ is introduced to force the modified call $c(k) = e^{\alpha k}C(e^k)$ to be square-integrable (it vanishes as $k \to -\infty$ for $\alpha > 0$). Taking the Fourier transform of $c(k)$ and substituting the payoff integral produces $\varphi(u - i(\alpha+1))$ in the numerator, because multiplying by $e^{\alpha k}$ in the spatial domain shifts the argument by $-i\alpha$ in the frequency domain, and the call payoff itself introduces an additional shift of $-i$.

    **Maximum damping parameter:** The CF evaluation $\varphi(u - i(\alpha+1))$ requires the moment $\mathbb{E}[S_T^{\alpha+1}] < \infty$. If $n^*(T) = 3.5$, then we need $\alpha + 1 < n^*(T) = 3.5$, so $\alpha < 2.5$. The maximum allowable value is $\alpha_{\max} = 2.5$ (exclusive).

    **Numerical consequences of choosing $\alpha$ too large:** If $\alpha + 1 \geq n^*(T)$, the moment $\mathbb{E}[S_T^{\alpha+1}]$ does not exist. Numerically, the CF $\varphi(u - i(\alpha+1))$ will blow up for $u$ near zero (or become extremely large), producing overflow, NaN, or wildly oscillating and inaccurate prices. The integrand fails to decay, making the Fourier integral divergent.

---

**Exercise 6.** Lee's moment formula states that the implied volatility wing behaves as

$$
\sigma_{\text{impl}}^2(k, T) \sim \frac{2|k|}{T}\left(1 - \frac{1}{n^*}\text{sgn}(k)\right) \quad \text{as } |k| \to \infty
$$

For a model with critical right moment $n^* = 4$ and $T = 1$, compute the asymptotic implied volatility at log-moneyness $k = 2$ (far OTM call). Repeat for $k = -2$ (far OTM put) assuming the critical left moment is also $n^* = 4$. Compare with typical Black-Scholes implied volatilities.

??? success "Solution to Exercise 6"
    For the right wing ($k = 2$, far OTM call) with $n^* = 4$ and $T = 1$:

    $$
    \sigma_{\text{impl}}^2(2, 1) \sim \frac{2\cdot|2|}{1}\!\left(1 - \frac{1}{4}\cdot(+1)\right) = 4\cdot\frac{3}{4} = 3
    $$

    so $\sigma_{\text{impl}}(2, 1) \sim \sqrt{3} \approx 1.732$, i.e., about 173%.

    For the left wing ($k = -2$, far OTM put) with critical left moment $n^* = 4$:

    $$
    \sigma_{\text{impl}}^2(-2, 1) \sim \frac{2\cdot 2}{1}\!\left(1 - \frac{1}{4}\cdot(-1)\right) = 4\cdot\frac{5}{4} = 5
    $$

    so $\sigma_{\text{impl}}(-2, 1) \sim \sqrt{5} \approx 2.236$, i.e., about 224%.

    **Comparison:** Typical Black-Scholes implied volatilities for equity options are 15%--40%. These asymptotic values (173% and 224%) are extreme, but they describe the far wings at log-moneyness $|k| = 2$ (corresponding to strikes roughly $e^2 \approx 7.4$ times or $e^{-2} \approx 0.14$ times the spot). In practice, market quotes rarely extend to such extremes. The asymmetry between the wings (put wing steeper than call wing when left and right critical moments are equal) arises from the $\text{sgn}(k)$ term, reflecting that the left tail contributes differently than the right tail.

---

**Exercise 7.** The Variance Gamma (VG) model has characteristic function

$$
\varphi_{\text{VG}}(\tau, u) = \exp(iu\omega\tau)\left(\frac{1}{1 - iu\theta\nu + \frac{\sigma^2\nu u^2}{2}}\right)^{\tau/\nu}
$$

Show that the characteristic function is well-defined (the base of the power is positive) for all real $u$ when $\sigma > 0$ and $\nu > 0$. Compare the tail behavior of $|\varphi_{\text{VG}}(u)|$ as $|u| \to \infty$ with that of the Black-Scholes CF $|\varphi_{\text{BS}}(u)| = e^{-\sigma^2 u^2 T/2}$. Which decays faster, and what does this imply about the smoothness of the respective densities?

??? success "Solution to Exercise 7"
    **Well-definedness:** The base of the power is

    $$
    h(u) = 1 - iu\theta\nu + \frac{\sigma^2\nu u^2}{2}
    $$

    For real $u$, the real part is $\text{Re}[h(u)] = 1 + \frac{\sigma^2\nu u^2}{2}$ and the imaginary part is $\text{Im}[h(u)] = -u\theta\nu$. Since $\sigma > 0$ and $\nu > 0$, we have $\text{Re}[h(u)] \geq 1 > 0$ for all real $u$. A complex number with strictly positive real part is nonzero and lies in the right half-plane, so the principal value of the complex power $h(u)^{-\tau/\nu}$ is well-defined and continuous for all real $u$.

    **Tail behavior:** The modulus of the VG CF for large $|u|$ satisfies

    $$
    |h(u)|^{-\tau/\nu} = \left(|h(u)|^2\right)^{-\tau/(2\nu)}
    $$

    where $|h(u)|^2 = \left(1 + \frac{\sigma^2\nu u^2}{2}\right)^2 + u^2\theta^2\nu^2 \sim \frac{\sigma^4\nu^2 u^4}{4}$ as $|u| \to \infty$. Therefore

    $$
    |\varphi_{\text{VG}}(u)| \sim C|u|^{-2\tau/\nu}
    $$

    which is polynomial decay. In contrast, $|\varphi_{\text{BS}}(u)| = e^{-\sigma^2 u^2 T/2}$ decays as a Gaussian in $u$, which is much faster.

    **Implications for density smoothness:** By Fourier analysis, faster decay of the CF corresponds to greater smoothness of the density. The Gaussian decay of the BS characteristic function means the log-normal density is infinitely differentiable (in fact, analytic). The polynomial decay of the VG characteristic function means the VG density is less smooth -- it is finitely differentiable, with the number of derivatives depending on $\tau/\nu$. In particular, the VG density can have heavier tails and sharper features than the log-normal density.
