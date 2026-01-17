# Affine Structure and Characteristic Function

A key advantage of the Heston model is its **affine structure**, which enables semi-closed-form pricing of European options via characteristic functions. This section derives the characteristic function explicitly and explains its use in option pricing.

---

## Affine Processes

### Definition

A Markov process $(X_t, V_t)$ is **affine** if its conditional characteristic function has exponential-affine form:

$$
\mathbb{E}\left[e^{iu X_T + wV_T} \mid X_t, V_t\right] = \exp\left(A(\tau, u, w) + B(\tau, u, w)V_t + iuX_t\right)
$$

where $\tau = T - t$ and the functions $A, B$ satisfy ordinary differential equations (Riccati equations).

### Why Affine Structure Matters

1. **Semi-closed form:** Characteristic function given by solving ODEs
2. **Fast evaluation:** No Monte Carlo needed for European options
3. **Gradient availability:** Derivatives for calibration are tractable
4. **Fourier pricing:** Efficient methods via FFT

The Heston model belongs to the affine class, making it computationally tractable.

---

## Characteristic Function of Log-Price

### Setup

Let $X_t = \log S_t$. Under the risk-neutral measure $\mathbb{Q}$:

$$
\begin{aligned}
dX_t &= \left(r - q - \frac{1}{2}V_t\right)dt + \sqrt{V_t}\,dW_t^S \\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
\end{aligned}
$$

with $\langle W^S, W^V \rangle_t = \rho t$.

### The Characteristic Function

The conditional characteristic function of $X_T$ is:

$$
\varphi(\tau, u) = \mathbb{E}^{\mathbb{Q}}\left[e^{iuX_T} \mid X_t, V_t\right] = \exp\left(C(\tau, u) + D(\tau, u)V_t + iuX_t\right)
$$

where $\tau = T - t$.

---

## Derivation of Riccati Equations

### Feynman–Kac Approach

Define $f(t, x, v) = \mathbb{E}[e^{iuX_T} | X_t = x, V_t = v]$.

By Feynman–Kac, $f$ satisfies the PDE:

$$
\frac{\partial f}{\partial t} + \mathcal{L}f = 0
$$

with terminal condition $f(T, x, v) = e^{iux}$, where $\mathcal{L}$ is the infinitesimal generator.

### Generator Calculation

The generator is:

$$
\mathcal{L}f = \left(r - q - \frac{v}{2}\right)\frac{\partial f}{\partial x} + \kappa(\theta - v)\frac{\partial f}{\partial v} + \frac{v}{2}\frac{\partial^2 f}{\partial x^2} + \rho\xi v\frac{\partial^2 f}{\partial x \partial v} + \frac{\xi^2 v}{2}\frac{\partial^2 f}{\partial v^2}
$$

### Affine Ansatz

Substitute the ansatz $f = \exp(C + Dv + iux)$:

$$
\frac{\partial f}{\partial t} = \left(\dot{C} + \dot{D}v\right)f
$$

$$
\frac{\partial f}{\partial x} = iu \cdot f, \quad \frac{\partial^2 f}{\partial x^2} = -u^2 f
$$

$$
\frac{\partial f}{\partial v} = D \cdot f, \quad \frac{\partial^2 f}{\partial v^2} = D^2 f
$$

$$
\frac{\partial^2 f}{\partial x \partial v} = iuD \cdot f
$$

### Collecting Terms

Substituting into the PDE and dividing by $f$:

$$
\dot{C} + \dot{D}v + (r-q-\tfrac{v}{2})iu + \kappa(\theta - v)D - \frac{u^2 v}{2} + \rho\xi v \cdot iuD + \frac{\xi^2 v}{2}D^2 = 0
$$

Separating terms constant in $v$ and linear in $v$:

**Constant terms:**
$$
\dot{C} + (r-q)iu + \kappa\theta D = 0
$$

**Linear in $v$:**
$$
\dot{D} - \frac{iu}{2} - \kappa D - \frac{u^2}{2} + \rho\xi iu D + \frac{\xi^2}{2}D^2 = 0
$$

---

## Solving the Riccati Equations

### The $D$ Equation (Riccati)

$$
\dot{D} = \frac{\xi^2}{2}D^2 + (\rho\xi iu - \kappa)D - \frac{1}{2}(iu + u^2)
$$

with terminal condition $D(0, u) = 0$.

This is a Riccati ODE with solution:

$$
D(\tau, u) = \frac{1 - e^{d\tau}}{1 - ge^{d\tau}} \cdot \frac{\kappa - \rho\xi iu - d}{\xi^2}
$$

where:

$$
d = \sqrt{(\rho\xi iu - \kappa)^2 + \xi^2(iu + u^2)}
$$

$$
g = \frac{\kappa - \rho\xi iu - d}{\kappa - \rho\xi iu + d}
$$

### The $C$ Equation (Linear)

$$
\dot{C} = -(r-q)iu - \kappa\theta D
$$

with terminal condition $C(0, u) = 0$.

Integrating:

$$
C(\tau, u) = (r-q)iu\tau + \frac{\kappa\theta}{\xi^2}\left[(\kappa - \rho\xi iu - d)\tau - 2\ln\left(\frac{1 - ge^{d\tau}}{1-g}\right)\right]
$$

---

## Complete Characteristic Function

### Final Formula

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

$$
d = \sqrt{(\kappa - \rho\xi iu)^2 + \xi^2(iu + u^2)}
$$

$$
g = \frac{\kappa - \rho\xi iu - d}{\kappa - \rho\xi iu + d}
$$

### Alternative Formulation (Lord–Kahl)

For numerical stability, use the alternative form:

$$
D(\tau, u) = \frac{\kappa - \rho\xi iu + d}{\xi^2} \cdot \frac{1 - e^{-d\tau}}{1 - g^{-1}e^{-d\tau}}
$$

$$
C(\tau, u) = (r-q)iu\tau + \frac{\kappa\theta}{\xi^2}\left[(\kappa - \rho\xi iu + d)\tau - 2\ln\left(\frac{1 - g^{-1}e^{-d\tau}}{1-g^{-1}}\right)\right]
$$

This avoids numerical issues when $|g| > 1$.

---

## Numerical Stability Issues

### The "Little Heston Trap"

The original Heston formulation can suffer from:
1. **Branch cut issues:** Complex logarithm discontinuities
2. **Cancellation errors:** Near-zero denominators
3. **Overflow:** Large exponentials

### Rotation Count Method

Track the branch of the complex logarithm by counting rotations:

$$
\ln(z) = \ln|z| + i(\arg(z) + 2\pi n)
$$

where $n$ is chosen for continuity as $u$ varies.

### Practical Recommendations

1. Use the Lord–Kahl formulation
2. Implement rotation counting for $\ln(1 - ge^{d\tau})$
3. Test against known limits (Black–Scholes when $\xi \to 0$)
4. Validate with Monte Carlo for extreme parameters

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

### Density Recovery

The risk-neutral density of $X_T$ is:

$$
f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-iux}\varphi(\tau, u)\,du
$$

### Gil-Pelaez Inversion

For the distribution function:

$$
F(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty} \text{Re}\left[\frac{e^{-iux}\varphi(\tau, u)}{iu}\right]du
$$

### Call Price Formula (Heston's Original)

$$
C = S_0 e^{-qT}P_1 - Ke^{-rT}P_2
$$

where:

$$
P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\left[\frac{e^{-iu\log K}\varphi_j(\tau, u)}{iu}\right]du
$$

and $\varphi_1$, $\varphi_2$ are modified characteristic functions.

### Carr–Madan Formula

See Section 9.4 for the complete Fourier pricing methodology.

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
