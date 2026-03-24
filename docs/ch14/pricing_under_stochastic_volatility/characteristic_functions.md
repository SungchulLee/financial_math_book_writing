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

For the Heston model (derived in Section 9.3):

$$
\varphi(\tau, u) = \exp\left(C(\tau, u) + D(\tau, u)V_0 + iu\log S_0\right)
$$

with:

$$
C(\tau, u) = (r-q)iu\tau + \frac{\kappa\theta}{\xi^2}\left[(\kappa - \rho\xi iu - d)\tau - 2\ln\left(\frac{1 - ge^{d\tau}}{1-g}\right)\right]
$$

$$
D(\tau, u) = \frac{\kappa - \rho\xi iu - d}{\xi^2} \cdot \frac{1 - e^{d\tau}}{1 - ge^{d\tau}}
$$

where:

$$
d = \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}
$$

$$
g = \frac{\kappa - \rho\xi iu - d}{\kappa - \rho\xi iu + d}
$$

---

## Characteristic Functions of Other Models

### Black–Scholes

For GBM with constant volatility $\sigma$:

$$
\varphi_{\text{BS}}(\tau, u) = \exp\left(iu\left[\log S_0 + (r-q-\tfrac{\sigma^2}{2})\tau\right] - \frac{\sigma^2 u^2 \tau}{2}\right)
$$

This is Gaussian in $u$.

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

Fourier pricing methods often evaluate $\varphi$ at complex $u$:
- Carr–Madan uses $u - i(\alpha + 1)$
- Lewis formula uses $u - i/2$

The strip of regularity determines which damping parameters $\alpha$ are valid.

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

For implied volatility wings, the moment explosion determines asymptotic behavior:

$$
\sigma_{\text{impl}}^2(k, T) \sim \frac{2|k|}{T}\left(1 - \frac{1}{n^*(T)}\text{sgn}(k)\right) \quad \text{as } |k| \to \infty
$$

---

## Practical Implementation Notes

### Numerical Evaluation

```python
def heston_cf(u, S0, V0, kappa, theta, xi, rho, r, q, tau):
    """
    Heston characteristic function (Lord-Kahl formulation)
    """
    i = complex(0, 1)
    
    # Intermediate quantities
    a = kappa - rho * xi * i * u
    b = xi**2 * (i * u + u**2)
    d = np.sqrt(a**2 + b)
    
    # Guard against numerical issues
    g = (a - d) / (a + d)
    
    # C and D functions
    D = (a - d) / xi**2 * (1 - np.exp(-d * tau)) / (1 - g * np.exp(-d * tau))
    C = (r - q) * i * u * tau + kappa * theta / xi**2 * (
        (a - d) * tau - 2 * np.log((1 - g * np.exp(-d * tau)) / (1 - g))
    )
    
    return np.exp(C + D * V0 + i * u * np.log(S0))
```

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

---

**Exercise 2.** Write the Black–Scholes characteristic function for $X_T = \log S_T$ with parameters $S_0 = 100$, $r = 3\%$, $q = 1\%$, $\sigma = 25\%$, and $T = 0.5$. Verify the martingale condition $\varphi(-i) = e^{(r-q)T}$ by substituting $u = -i$ into your formula.

---

**Exercise 3.** The Heston characteristic function involves the discriminant $d = \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}$. For $\kappa = 2$, $\xi = 0.4$, $\rho = -0.7$: (a) compute $d$ at $u = 0$ and verify it equals $\kappa$; (b) compute $d$ at $u = 5$ and $u = 20$, showing that $\text{Re}(d) > 0$; (c) explain why the choice of branch for the complex square root affects the result and how the Lord-Kahl formulation addresses this.

---

**Exercise 4.** The Gil-Pelaez inversion formula for the CDF is

$$
F_X(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-iux}\varphi_X(u)}{iu}\right]du
$$

For a standard normal with $\varphi(u) = e^{-u^2/2}$, evaluate $F_X(0)$ and verify it equals $1/2$. Then set $x = 1.96$ and compute the integral numerically (using, e.g., the trapezoidal rule with $\Delta u = 0.01$ and $u_{\max} = 50$) to verify that $F_X(1.96) \approx 0.975$.

---

**Exercise 5.** Analytic continuation of the characteristic function to complex arguments is essential for Fourier pricing. Explain why the Carr-Madan formula evaluates $\varphi(u - i(\alpha + 1))$ rather than $\varphi(u)$. If the critical moment for the Heston model is $n^*(T) = 3.5$, what is the maximum allowable damping parameter $\alpha$? What happens numerically if $\alpha$ is chosen too large?

---

**Exercise 6.** Lee's moment formula states that the implied volatility wing behaves as

$$
\sigma_{\text{impl}}^2(k, T) \sim \frac{2|k|}{T}\left(1 - \frac{1}{n^*}\text{sgn}(k)\right) \quad \text{as } |k| \to \infty
$$

For a model with critical right moment $n^* = 4$ and $T = 1$, compute the asymptotic implied volatility at log-moneyness $k = 2$ (far OTM call). Repeat for $k = -2$ (far OTM put) assuming the critical left moment is also $n^* = 4$. Compare with typical Black-Scholes implied volatilities.

---

**Exercise 7.** The Variance Gamma (VG) model has characteristic function

$$
\varphi_{\text{VG}}(\tau, u) = \exp(iu\omega\tau)\left(\frac{1}{1 - iu\theta\nu + \frac{\sigma^2\nu u^2}{2}}\right)^{\tau/\nu}
$$

Show that the characteristic function is well-defined (the base of the power is positive) for all real $u$ when $\sigma > 0$ and $\nu > 0$. Compare the tail behavior of $|\varphi_{\text{VG}}(u)|$ as $|u| \to \infty$ with that of the Black-Scholes CF $|\varphi_{\text{BS}}(u)| = e^{-\sigma^2 u^2 T/2}$. Which decays faster, and what does this imply about the smoothness of the respective densities?
