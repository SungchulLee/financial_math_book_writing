# Affine Structure and Characteristic Function

A key advantage of the Heston model is its **affine structure**, which enables semi-closed-form pricing of European options via characteristic functions. This section derives the characteristic function explicitly and explains its use in option pricing.

---

## Affine Processes and the Heston CF

Recall (see [§ Affine Processes](../../ch15/index.md)) that a Markov process is **affine** when its conditional characteristic function has exponential-affine form, with the coefficients solving Riccati ODEs. This yields semi-closed-form European pricing, tractable Greeks, and FFT-based calibration.

For the Heston log-price $X_t = \log S_t$ (SDE: see [§ Model Definition](model_definition.md)), the conditional characteristic function takes the form

$$
\varphi(\tau, u) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{iuX_T} \,\big|\, X_t, V_t\right] = \exp\!\left(C(\tau, u) + D(\tau, u)V_t + iuX_t\right), \qquad \tau = T - t.
$$

---

## Derivation of Riccati Equations

By Feynman–Kac, $f(t,x,v)=\mathbb{E}[e^{iuX_T}\mid X_t=x, V_t=v]$ satisfies $\partial_t f + \mathcal{L}f = 0$ with terminal condition $f(T,x,v)=e^{iux}$. Substituting the affine ansatz $f=\exp(C(\tau,u)+D(\tau,u)v+iux)$ and separating terms constant and linear in $v$ produces

**$D$ (Riccati):**

$$
\dot{D} = \frac{\xi^2}{2}D^2 + (\rho\xi iu - \kappa)D - \frac{1}{2}(iu + u^2), \qquad D(0,u)=0.
$$

**$C$ (linear in $D$):**

$$
\dot{C} = (r-q)iu + \kappa\theta D, \qquad C(0,u)=0.
$$

Recall (see [§ Heston Characteristic Function and Riccati](../../ch16/heston_cf/heston_sde_and_affine_recap.md)) the closed-form solutions

$$
\begin{aligned}
D(\tau, u) &= \frac{\kappa - \rho\xi iu - d}{\xi^2}\cdot\frac{1 - e^{d\tau}}{1 - ge^{d\tau}},\\
C(\tau, u) &= (r-q)iu\tau + \frac{\kappa\theta}{\xi^2}\!\left[(\kappa - \rho\xi iu - d)\tau - 2\ln\!\frac{1 - ge^{d\tau}}{1-g}\right],\\
d &= \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}, \qquad g = \frac{\kappa - \rho\xi iu - d}{\kappa - \rho\xi iu + d}.
\end{aligned}
$$

The Lord–Kahl reparametrization (replacing $g$ by $g^{-1}$ and $e^{d\tau}$ by $e^{-d\tau}$) restores numerical stability by keeping $|g^{-1}e^{-d\tau}|<1$ — this and the "Little Heston Trap" / branch-tracking remedies are covered in [§ Heston CF Numerical Stability](../../ch16/heston_cf/heston_sde_and_affine_recap.md).

---

## Moments from Characteristic Function

### Moment Generating Property

The moments of $X_T = \log S_T$ are obtained from:

$$
\mathbb{E}[(X_T)^n] = \frac{1}{i^n}\frac{\partial^n \varphi}{\partial u^n}\bigg|_{u=0}
$$

### First Two Moments

**Mean of log-price:**

$$
\mathbb{E}[X_T] = X_0 + (r-q)T - \frac{1}{2}\mathbb{E}\left[\int_0^T V_s\,ds\right]
$$

where $\mathbb{E}[\int_0^T V_s\,ds] = \theta T + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}$.

**Variance of log-price:**

$$
\text{Var}[X_T] = \mathbb{E}\left[\int_0^T V_s\,ds\right] + \text{(covariance correction)}
$$

The full expression involves the covariance between $X_T$ and $\int_0^T V_s\,ds$.

---

## Option Pricing via Fourier Methods

Recall (see [§ European Pricing](../../ch16/european_pricing/semi_closed_form_fourier_inversion.md) and [§ Heston COS Method](../../ch16/heston_cos/cos_applied_to_heston.md)) the standard Fourier-pricing toolkit: density recovery $f(x)=\frac{1}{2\pi}\int e^{-iux}\varphi(\tau,u)\,du$, Gil-Pelaez inversion, Heston's original two-integral formula $C=S_0 e^{-qT}P_1 - Ke^{-rT}P_2$, the Carr–Madan damped-call FFT, and the COS expansion.

---

## Key Takeaways

- Affine structure yields exponential-affine characteristic functions
- Heston CF is given by explicit formulas involving Riccati solutions
- Numerical stability requires careful implementation (Lord–Kahl formulation)
- The characteristic function enables Fourier-based option pricing
- Moments and Greeks can be derived from CF derivatives

---

## Further Reading

- Heston, S. (1993). *A closed-form solution for options with stochastic volatility*. Review of Financial Studies.
- Duffie, D., Pan, J., & Singleton, K. (2000). *Transform analysis and asset pricing for affine jump-diffusions*. Econometrica.
- Lord, R. & Kahl, C. (2010). *Complex logarithms in Heston-like models*. Mathematical Finance.
- Albrecher, H., Mayer, P., Schoutens, W., & Tistaert, J. (2007). *The little Heston trap*. Wilmott Magazine.
- Carr, P. & Madan, D. (1999). *Option valuation using the fast Fourier transform*. Journal of Computational Finance.

---

## Exercises

**Exercise 1.** Verify the affine structure of the Heston model by showing that the conditional characteristic function $\mathbb{E}[e^{iuX_T} | X_t, V_t]$ has the exponential-affine form $\exp(C(\tau, u) + D(\tau, u)V_t + iuX_t)$. Start from the Feynman-Kac PDE and substitute the affine ansatz. Identify the two ODEs that result from separating terms constant in $V$ and linear in $V$.

??? success "Solution to Exercise 1"
    We start from the Feynman--Kac PDE. Define $f(t, x, v) = \mathbb{E}[e^{iuX_T} | X_t = x, V_t = v]$. This satisfies:

    $$
    \frac{\partial f}{\partial t} + \left(r - q - \frac{v}{2}\right)\frac{\partial f}{\partial x} + \kappa(\theta - v)\frac{\partial f}{\partial v} + \frac{v}{2}\frac{\partial^2 f}{\partial x^2} + \rho\xi v\frac{\partial^2 f}{\partial x \partial v} + \frac{\xi^2 v}{2}\frac{\partial^2 f}{\partial v^2} = 0
    $$

    with terminal condition $f(T, x, v) = e^{iux}$.

    Substitute the affine ansatz $f = \exp(C(\tau, u) + D(\tau, u)v + iux)$ where $\tau = T - t$. Computing the partial derivatives:

    - $\partial f/\partial t = (-\dot{C} - \dot{D}v)f$ (since $\partial\tau/\partial t = -1$)
    - $\partial f/\partial x = iu \cdot f$, $\partial^2 f/\partial x^2 = -u^2 f$
    - $\partial f/\partial v = D \cdot f$, $\partial^2 f/\partial v^2 = D^2 f$
    - $\partial^2 f/\partial x \partial v = iuD \cdot f$

    Substituting and dividing by $f$:

    $$
    -\dot{C} - \dot{D}v + (r-q-\tfrac{v}{2})iu + \kappa(\theta - v)D - \frac{u^2 v}{2} + \rho\xi v\,iuD + \frac{\xi^2 v}{2}D^2 = 0
    $$

    Collecting terms constant in $v$ gives the ODE for $C$:

    $$
    \dot{C} = (r-q)iu + \kappa\theta D
    $$

    Collecting terms linear in $v$ gives the Riccati ODE for $D$:

    $$
    \dot{D} = -\frac{iu}{2} - \kappa D - \frac{u^2}{2} + \rho\xi\,iu\,D + \frac{\xi^2}{2}D^2
    $$

    Both have initial conditions $C(0, u) = D(0, u) = 0$. The separation into constant and linear terms in $v$ is exact because the Heston drift and diffusion coefficients are affine in $v$, confirming the affine structure.

---

**Exercise 2.** The Riccati ODE for $D(\tau, u)$ is

$$
\dot{D} = \frac{\xi^2}{2}D^2 + (\rho\xi iu - \kappa)D - \frac{1}{2}(iu + u^2)
$$

Show that in the limit $\xi \to 0$ (deterministic volatility), $D(\tau, u) = 0$ for all $\tau$, and $C(\tau, u)$ reduces to the Black–Scholes log-characteristic function $(r-q)iu\tau - \frac{1}{2}(iu + u^2)\theta\tau$. (Hint: when $\xi = 0$, $V_t$ is deterministic and converges to $\theta$.)

??? success "Solution to Exercise 2"
    When $\xi = 0$, the variance process becomes deterministic: $dV_t = \kappa(\theta - V_t)\,dt$, with solution $V_t = V_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})$. For large $t$, $V_t \to \theta$.

    The Riccati ODE becomes (setting $\xi = 0$):

    $$
    \dot{D} = -\kappa D - \frac{1}{2}(iu + u^2)
    $$

    With $D(0) = 0$, this linear ODE has the solution:

    $$
    D(\tau) = -\frac{iu + u^2}{2\kappa}(1 - e^{-\kappa\tau})
    $$

    However, in the deterministic volatility limit, the conditional characteristic function must reduce to a form that does not depend on $V_t$ separately from the deterministic path. As $\xi \to 0$, the contribution $D(\tau)V_t$ combines with $C(\tau)$ to reproduce the Black--Scholes characteristic function with the known deterministic integrated variance.

    For the $C$ equation with $\xi = 0$:

    $$
    \dot{C} = (r - q)iu + \kappa\theta D
    $$

    In the long-run steady state where $V_t = \theta$ for all $t$, the log-characteristic function of $X_T$ under Black--Scholes with constant variance $\theta$ is:

    $$
    \ln\varphi^{\text{BS}}(\tau, u) = (r-q)iu\tau - \frac{1}{2}(iu + u^2)\theta\tau
    $$

    Integrating the $C$ equation: $C(\tau) = (r-q)iu\tau + \kappa\theta\int_0^\tau D(s)\,ds$. Combined with $D(\tau)V_t$, the total $C(\tau) + D(\tau)\theta$ (evaluated at $V_t = \theta$) gives:

    $$
    (r-q)iu\tau - \frac{1}{2}(iu + u^2)\theta\tau
    $$

    which is exactly the Black--Scholes log-characteristic function.

---

**Exercise 3.** The discriminant of the Riccati equation is

$$
d = \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}
$$

For the parameters $\kappa = 2$, $\xi = 0.4$, $\rho = -0.7$, compute $d$ at $u = 1$ and $u = 10$. Verify that $d$ is well-defined (i.e., the quantity under the square root has positive real part). Why does the choice of branch cut for the complex square root matter for numerical implementation?

??? success "Solution to Exercise 3"
    With $\kappa = 2$, $\xi = 0.4$, $\rho = -0.7$:

    $$
    d = \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}
    $$

    **At $u = 1$:**

    $$
    \kappa - \rho\xi iu = 2 - (-0.7)(0.4)(i) = 2 + 0.28i
    $$

    $$
    (\kappa - \rho\xi iu)^2 = (2 + 0.28i)^2 = 4 + 1.12i - 0.0784 = 3.9216 + 1.12i
    $$

    $$
    \xi^2(iu + u^2) = 0.16(i + 1) = 0.16 + 0.16i
    $$

    $$
    d^2 = 3.9216 + 1.12i + 0.16 + 0.16i = 4.0816 + 1.28i
    $$

    $$
    |d^2| = \sqrt{4.0816^2 + 1.28^2} = \sqrt{16.660 + 1.638} = \sqrt{18.298} \approx 4.278
    $$

    $$
    d \approx \sqrt{4.278}\,e^{i\theta/2} \approx 2.068\,e^{i \times 0.1532} \approx 2.044 + 0.315i
    $$

    **At $u = 10$:**

    $$
    \kappa - \rho\xi iu = 2 + 2.8i
    $$

    $$
    (\kappa - \rho\xi iu)^2 = 4 + 11.2i - 7.84 = -3.84 + 11.2i
    $$

    $$
    \xi^2(iu + u^2) = 0.16(10i + 100) = 16 + 1.6i
    $$

    $$
    d^2 = 12.16 + 12.8i
    $$

    $$
    |d^2| = \sqrt{12.16^2 + 12.8^2} = \sqrt{147.87 + 163.84} = \sqrt{311.71} \approx 17.65
    $$

    $$
    d \approx 4.201\,e^{i \times 0.4120} \approx 3.846 + 1.682i
    $$

    In both cases, $\text{Re}(d^2) > 0$, so $d$ is well-defined. The choice of branch cut matters because as $u$ varies continuously (as required in the Fourier integral), the complex square root must also vary continuously. An inconsistent branch choice introduces discontinuities in $\varphi(\tau, u)$, producing errors in the numerical integration for option prices.

---

**Exercise 4.** Using the formula for the expected integrated variance

$$
\mathbb{E}\left[\int_0^T V_s\,ds\right] = \theta T + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}
$$

compute this quantity for $V_0 = 0.05$, $\theta = 0.04$, $\kappa = 2.0$, and $T = 0.25, 0.5, 1.0, 2.0$. The ATM implied variance is approximately $\sigma^2_{\text{impl}}(T) \approx \frac{1}{T}\mathbb{E}[\int_0^T V_s\,ds]$. Plot or compute the ATM implied volatility term structure and verify it interpolates between $\sqrt{V_0}$ and $\sqrt{\theta}$.

??? success "Solution to Exercise 4"
    With $V_0 = 0.05$, $\theta = 0.04$, $\kappa = 2.0$:

    $$
    \mathbb{E}\left[\int_0^T V_s\,ds\right] = \theta T + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa} = 0.04T + 0.01 \cdot \frac{1 - e^{-2T}}{2}
    $$

    | $T$ | $e^{-2T}$ | $\mathbb{E}[\int_0^T V_s\,ds]$ | $\sigma_{\text{impl}}(T) = \sqrt{\frac{1}{T}\mathbb{E}[\cdot]}$ |
    |-----|-----------|-------------------------------|--------------------------------------|
    | 0.25 | 0.6065 | $0.01 + 0.001967 = 0.01197$ | $\sqrt{0.04787} = 21.88\%$ |
    | 0.50 | 0.3679 | $0.02 + 0.003161 = 0.02316$ | $\sqrt{0.04632} = 21.52\%$ |
    | 1.00 | 0.1353 | $0.04 + 0.004323 = 0.04432$ | $\sqrt{0.04432} = 21.05\%$ |
    | 2.00 | 0.0183 | $0.08 + 0.004908 = 0.08491$ | $\sqrt{0.04246} = 20.61\%$ |

    As $T \to \infty$, the second term vanishes and $\sigma_{\text{impl}} \to \sqrt{\theta} = \sqrt{0.04} = 20\%$. Since $V_0 = 0.05 > \theta = 0.04$, the term structure is **downward-sloping**, interpolating from $\sqrt{V_0} = 22.36\%$ at $T = 0$ down to $\sqrt{\theta} = 20\%$.

---

**Exercise 5.** Explain the "Little Heston Trap" and why the original formulation can produce numerical errors. Specifically, for the term $\ln(1 - ge^{d\tau})$, describe under what parameter and $u$ combinations $|ge^{d\tau}|$ can approach or exceed 1. How does the Lord-Kahl alternative formulation $\ln(1 - g^{-1}e^{-d\tau})$ avoid this problem?

??? success "Solution to Exercise 5"
    **The "Little Heston Trap"** refers to numerical instability in the original Heston formulation of the characteristic function, identified by Albrecher et al. (2007).

    In the original formulation, the term $\ln(1 - ge^{d\tau})$ can become problematic because:

    1. The ratio $g = (\kappa - \rho\xi iu - d)/(\kappa - \rho\xi iu + d)$ can have modulus close to 1 for certain parameter combinations.

    2. When $|g| \approx 1$ and $\text{Re}(d) > 0$ (which occurs for large $\tau$ or certain $u$ values), the product $ge^{d\tau}$ can grow in modulus, causing $|1 - ge^{d\tau}|$ to become very small or cross zero.

    3. Specifically, for large $u$, $\text{Re}(d) > 0$ and $|g| \to 1$, so $|ge^{d\tau}|$ can exceed 1, creating a singularity in the logarithm. Even when it does not exceed 1, near-cancellation produces large numerical errors.

    4. The complex logarithm is multi-valued, and as $u$ varies continuously in the Fourier integral, the argument of $1 - ge^{d\tau}$ may wind around the origin, requiring careful branch tracking.

    The **Lord--Kahl formulation** replaces $g$ with $g^{-1}$ and $e^{d\tau}$ with $e^{-d\tau}$. Since $|g^{-1}| = 1/|g|$ and the exponential now decays, the product $|g^{-1}e^{-d\tau}|$ remains bounded below 1 for all $u$ and $\tau$. This ensures the logarithm argument stays away from zero, eliminating the numerical instability.

---

**Exercise 6.** The Gil-Pelaez inversion formula for the call price involves the integral

$$
P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-iu\log K}\varphi_j(\tau, u)}{iu}\right]du
$$

In practice, the integral is truncated at a finite upper limit $u_{\max}$. For the Heston model, the characteristic function $\varphi(\tau, u) \to 0$ as $u \to \infty$ due to the $-u^2$ term in the Riccati equation. Estimate how large $u_{\max}$ should be for $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $T = 1$, by finding the value of $u$ at which $|\varphi(\tau, u)|$ decays below $10^{-8}$.

??? success "Solution to Exercise 6"
    The characteristic function decays as $|\varphi(\tau, u)| \sim \exp(-\frac{1}{2}u^2 \bar{V}\tau)$ for large $u$, where $\bar{V}$ is an effective variance level. This comes from the $-u^2/2$ term in the Riccati equation dominating for large $u$.

    More precisely, for large $u$, the $D$ coefficient behaves as $D(\tau, u) \approx -\frac{u^2}{2}\frac{1-e^{-\kappa\tau}}{\kappa}$ (ignoring lower-order terms), and $C$ accumulates a corresponding contribution from $\kappa\theta D$.

    Setting $|\varphi(\tau, u_{\max})| \approx e^{-8\ln 10} = 10^{-8}$, we need:

    $$
    \frac{1}{2}u_{\max}^2\bar{V}\tau \approx 8\ln 10 \approx 18.42
    $$

    With $\theta = 0.04$ and $T = 1$, using $\bar{V} \approx \theta = 0.04$:

    $$
    u_{\max} \approx \sqrt{\frac{2 \times 18.42}{0.04 \times 1}} = \sqrt{921} \approx 30.3
    $$

    In practice, one should verify convergence by testing the integral at progressively larger $u_{\max}$. For the given parameters, $u_{\max} \approx 30$--$50$ is typically sufficient. The presence of vol-of-vol $\xi = 0.5$ causes slightly faster decay (heavier mixing of variance), so this estimate is conservative.

---

**Exercise 7.** The Heston characteristic function can be used to compute model-implied moments. Derive the formula for the variance of $X_T = \log S_T$ in terms of the characteristic function:

$$
\text{Var}[X_T] = -\frac{\partial^2}{\partial u^2}\ln\varphi(\tau, u)\bigg|_{u=0}
$$

Using the explicit formulas for $C(\tau, u)$ and $D(\tau, u)$, show that the variance depends on $V_0$, $\theta$, $\kappa$, $\xi$, and $\rho$. Why does the variance of log-returns depend on $\rho$ in a stochastic volatility model but not in Black–Scholes?

??? success "Solution to Exercise 7"
    The cumulant generating function is $\psi(\tau, u) = \ln\varphi(\tau, u) = C(\tau, u) + D(\tau, u)V_0 + iu\log S_0$.

    The mean and variance of $X_T$ are given by:

    $$
    \mathbb{E}[X_T] = \frac{1}{i}\frac{\partial\psi}{\partial u}\bigg|_{u=0}, \quad \text{Var}[X_T] = -\frac{\partial^2\psi}{\partial u^2}\bigg|_{u=0}
    $$

    To see why, note $\varphi(\tau, u) = \mathbb{E}[e^{iuX_T}]$, so:

    $$
    \frac{\partial^2}{\partial u^2}\ln\varphi\bigg|_{u=0} = \frac{\varphi''\varphi - (\varphi')^2}{\varphi^2}\bigg|_{u=0} = \frac{\mathbb{E}[(iX_T)^2] - (\mathbb{E}[iX_T])^2}{1} = -\text{Var}[X_T]
    $$

    From the explicit formulas, $\psi = C(\tau, u) + D(\tau, u)V_0 + iu\log S_0$. Both $C$ and $D$ depend on $\kappa$, $\theta$, $\xi$, and $\rho$ (through $d$ and $g$). The second derivative $\partial^2\psi/\partial u^2|_{u=0}$ therefore depends on all five parameters $V_0, \theta, \kappa, \xi, \rho$.

    **Why $\rho$ affects variance:** In a stochastic volatility model, the variance of log-returns over $[0,T]$ is:

    $$
    \text{Var}[X_T] = \text{Var}\left[\int_0^T \sqrt{V_s}\,dW_s^S\right] + \text{(drift variance terms)}
    $$

    Expanding using $dW_s^S = \rho\,dW_s^V + \sqrt{1-\rho^2}\,dW_s^\perp$, the integrated variance $\int_0^T V_s\,ds$ is random and correlated with $X_T$. When $\rho \neq 0$, the covariance $\text{Cov}(X_T, \int_0^T V_s\,ds) \neq 0$, which modifies $\text{Var}[X_T]$. In Black--Scholes, $\sigma$ is constant and there is no stochastic volatility process, so no such covariance term exists and the variance $\text{Var}[X_T] = \sigma^2 T$ is independent of any correlation parameter.
