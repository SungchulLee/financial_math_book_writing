# Fourier Transform Methods: Complete Mathematical Treatment

Fourier transform methods are **extraordinarily powerful** for option pricing—they convert parabolic PDEs into **algebraic equations**, enable **fast computation** via FFT, and naturally handle **Lévy processes** and **stochastic volatility**.

---

## **1. Fundamental Theory**

### **Fourier Transform Definition**

For a function $f: \mathbb{R} \to \mathbb{C}$:

$$\boxed{\hat{f}(\omega) = \mathcal{F}[f](\omega) = \int_{-\infty}^{\infty} f(x)e^{-i\omega x}dx}$$

**Inverse transform**:
$$\boxed{f(x) = \mathcal{F}^{-1}[\hat{f}](x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(\omega)e^{i\omega x}d\omega}$$

### **Key Properties**

**Linearity**:
$$\mathcal{F}[\alpha f + \beta g] = \alpha\hat{f} + \beta\hat{g}$$

**Derivative**:
$$\boxed{\mathcal{F}\left[\frac{df}{dx}\right](\omega) = i\omega\hat{f}(\omega)}$$

$$\boxed{\mathcal{F}\left[\frac{d^2f}{dx^2}\right](\omega) = -\omega^2\hat{f}(\omega)}$$

**Shift**:
$$\mathcal{F}[f(x-a)](\omega) = e^{-i\omega a}\hat{f}(\omega)$$

**Convolution theorem**:
$$\boxed{\mathcal{F}[f * g] = \hat{f} \cdot \hat{g}}$$

where $(f * g)(x) = \int_{-\infty}^{\infty}f(x-y)g(y)dy$.

### **Parseval's Identity**

$$\boxed{\int_{-\infty}^{\infty}|f(x)|^2 dx = \frac{1}{2\pi}\int_{-\infty}^{\infty}|\hat{f}(\omega)|^2 d\omega}$$

Energy is preserved under the transform.

---

## **2. Black-Scholes PDE in Fourier Space**

### **Log-Price Formulation**

Define $x = \ln(S/K)$ and $\tau = T - t$. The Black-Scholes PDE becomes:

$$\boxed{\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV}$$

with terminal condition $V(x,0) = \Phi(Ke^x)$.

### **Apply Fourier Transform**

Transform in the $x$ variable:
$$\hat{V}(\omega,\tau) = \int_{-\infty}^{\infty}V(x,\tau)e^{-i\omega x}dx$$

Using the derivative properties:
$$\frac{\partial \hat{V}}{\partial \tau} = -\frac{\sigma^2\omega^2}{2}\hat{V} + i\omega\left(r - \frac{\sigma^2}{2}\right)\hat{V} - r\hat{V}$$

$$\boxed{\frac{\partial \hat{V}}{\partial \tau} = \psi(\omega)\hat{V}(\omega,\tau)}$$

where the **characteristic exponent** is:
$$\boxed{\psi(\omega) = -\frac{\sigma^2\omega^2}{2} + i\omega\left(r - \frac{\sigma^2}{2}\right) - r}$$

### **ODE in Fourier Space**

This is a **first-order ODE** (no longer PDE!):

$$\hat{V}(\omega,\tau) = \hat{V}(\omega,0)e^{\psi(\omega)\tau}$$

With $\hat{V}(\omega,0) = \hat{\Phi}(\omega)$:

$$\boxed{\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}}$$

### **Solution via Inverse Transform**

$$\boxed{V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)e^{\psi(\omega)\tau}e^{i\omega x}d\omega}$$

This is the **complete solution** in closed form!

---

## **3. Characteristic Functions**

### **Definition**

For a random variable $X$, the **characteristic function** is:
$$\boxed{\phi_X(\omega) = \mathbb{E}[e^{i\omega X}]}$$

This is the Fourier transform of the probability density.

### **Properties**

1. $\phi_X(0) = 1$
2. $|\phi_X(\omega)| \leq 1$
3. $\phi_X(-\omega) = \overline{\phi_X(\omega)}$ (conjugate)
4. If $Y = aX + b$: $\phi_Y(\omega) = e^{i\omega b}\phi_X(a\omega)$
5. **Sum of independent RVs**: $\phi_{X+Y} = \phi_X \cdot \phi_Y$

### **Inversion Formula**

The density can be recovered:
$$\boxed{f_X(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\phi_X(\omega)e^{-i\omega x}d\omega}$$

### **For Lognormal (Black-Scholes)**

Under $\mathbb{Q}$, $X_\tau = \ln(S_T/S_0)$ satisfies:
$$X_\tau \sim N\left[\left(r-\frac{\sigma^2}{2}\right)\tau, \sigma^2\tau\right]$$

The characteristic function:
$$\boxed{\phi_X(\omega,\tau) = \exp\left[i\omega\left(r-\frac{\sigma^2}{2}\right)\tau - \frac{\sigma^2\omega^2\tau}{2}\right]}$$

### **Connection to PDE Solution**

Note that:
$$e^{\psi(\omega)\tau} = e^{-r\tau}\phi_X(\omega,\tau)$$

So:
$$\hat{V}(\omega,\tau) = e^{-r\tau}\hat{\Phi}(\omega)\phi_X(\omega,\tau)$$

This shows: **Fourier transform of option value = (discounted) Fourier transform of payoff × characteristic function**.

---

## **4. European Call Option**

### **The Challenge: Non-Integrability**

For a call: $\Phi(S) = (S - K)^+ = (Ke^x - K)^+ = K(e^x - 1)^+$

The Fourier transform:
$$\hat{\Phi}(\omega) = K\int_0^{\infty}(e^x - 1)e^{-i\omega x}dx$$

This integral **diverges** for real $\omega$!

### **Complex Analysis Solution**

Extend to **complex** $\omega = \xi + i\eta$:
$$\hat{\Phi}(\omega) = K\int_0^{\infty}(e^x - 1)e^{-i\xi x}e^{\eta x}dx$$

For $\eta < -1$:
$$\hat{\Phi}(\omega) = K\left[\int_0^{\infty}e^{(1-i\xi+\eta)x}dx - \int_0^{\infty}e^{(-i\xi+\eta)x}dx\right]$$

$$= K\left[\frac{1}{-1+i\xi-\eta} - \frac{1}{i\xi-\eta}\right]$$

$$= K\left[\frac{i\xi-\eta - (-1+i\xi-\eta)}{(-1+i\xi-\eta)(i\xi-\eta)}\right]$$

$$\boxed{\hat{\Phi}(\omega) = \frac{K}{(i\omega+1)(i\omega)} = \frac{K}{\omega^2 - i\omega}}$$

for $\text{Im}(\omega) < -1$.

### **Carr-Madan Damping Approach**

Instead of dealing with complex $\omega$, **damp** the payoff:

$$\tilde{C}(x) = e^{\alpha x}C(x)$$

where $\alpha > 0$ is chosen so that $\tilde{C}$ decays as $x \to \infty$.

For a call, need $\alpha > 1$ to ensure:
$$e^{\alpha x}(e^x - 1)^+ = (e^{(\alpha+1)x} - e^{\alpha x})\mathbb{1}_{x>0} \to 0 \text{ as } x \to \infty$$

### **Fourier Transform of Damped Call**

$$\hat{\tilde{\Phi}}(\omega) = K\int_0^{\infty}(e^{(\alpha+1)x} - e^{\alpha x})e^{-i\omega x}dx$$

$$= K\left[\frac{1}{\alpha+1-i\omega} - \frac{1}{\alpha-i\omega}\right]$$

$$= K\frac{(\alpha-i\omega) - (\alpha+1-i\omega)}{(\alpha+1-i\omega)(\alpha-i\omega)}$$

$$\boxed{\hat{\tilde{\Phi}}(\omega) = \frac{-K}{(\alpha+i\omega)(\alpha+1+i\omega)}}$$

Or equivalently:
$$\boxed{\hat{\tilde{\Phi}}(\omega) = \frac{K}{\alpha^2 + \alpha - \omega^2 + i(2\alpha+1)\omega}}$$

---

## **5. Carr-Madan Formula**

### **Modified Call Price**

Define:
$$c_T(k) = e^{\alpha k}C(K = e^k, S_0, T)$$

where $k = \ln K$ is the **log-strike**.

### **Fourier Transform**

$$\psi_T(\omega) = \int_{-\infty}^{\infty}e^{i\omega k}c_T(k)dk$$

Using the characteristic function $\phi_T(\omega)$ of $\ln(S_T/S_0)$:

$$\boxed{\psi_T(\omega) = \frac{e^{-rT}\phi_T(\omega - (\alpha+1)i)}{\alpha^2 + \alpha - \omega^2 + i(2\alpha+1)\omega}}$$

### **Inversion**

$$c_T(k) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-i\omega k}\psi_T(\omega)d\omega$$

Taking the real part (since $c_T$ is real):

$$\boxed{C(K,S_0,T) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty}\text{Re}\left[e^{-i\omega k}\psi_T(\omega)\right]d\omega}$$

### **Explicit Formula**

For Black-Scholes with $\phi_T(\omega) = \exp[i\omega(r-\frac{\sigma^2}{2})T - \frac{\sigma^2\omega^2 T}{2}]$:

$$\boxed{C(K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty}\frac{e^{-rT}\exp[i\omega k + (r-\frac{\sigma^2}{2})T(\omega-(\alpha+1)i) - \frac{\sigma^2(\omega-(\alpha+1)i)^2T}{2}]}{\alpha^2+\alpha-\omega^2+i(2\alpha+1)\omega}d\omega}$$

where only the real part is taken.

---

## **6. Fast Fourier Transform (FFT)**

### **Discrete Fourier Transform**

For $N$ points $\{x_j\}_{j=0}^{N-1}$:

$$\boxed{X_k = \sum_{j=0}^{N-1}x_j e^{-2\pi ijk/N}, \quad k = 0,1,\ldots,N-1}$$

**Inverse**:
$$\boxed{x_j = \frac{1}{N}\sum_{k=0}^{N-1}X_k e^{2\pi ijk/N}}$$

### **FFT Algorithm**

The **Fast Fourier Transform** computes the DFT in:
$$\boxed{O(N\log N) \text{ operations}}$$

instead of $O(N^2)$ for naive implementation.

This is based on the **Cooley-Tukey algorithm** using divide-and-conquer.

### **Application to Option Pricing**

**Setup**:
1. Choose $N = 2^n$ (power of 2 for FFT)
2. Discretize log-strike: $k_u = k_0 + u\Delta k$ for $u = 0,1,\ldots,N-1$
3. Discretize frequency: $\omega_j = j\Delta\omega$ for $j = 0,1,\ldots,N-1$
4. Set grid spacing: $\Delta k \cdot \Delta\omega = \frac{2\pi}{N}$

### **Discretization**

The integral:
$$c_T(k_u) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-i\omega k_u}\psi_T(\omega)d\omega$$

becomes:
$$c_T(k_u) \approx \frac{\Delta\omega}{2\pi}\sum_{j=0}^{N-1}e^{-i\omega_j k_u}\psi_T(\omega_j)$$

$$= \frac{\Delta\omega}{2\pi}\sum_{j=0}^{N-1}e^{-2\pi iju/N}\psi_T(\omega_j)$$

This is an **inverse DFT**!

### **Implementation Steps**

1. Choose $\alpha$ (typically $\alpha = 0.75$ or $\alpha = 1.5$)
2. Set $\Delta k$ (strike spacing), compute $\Delta\omega = \frac{2\pi}{N\Delta k}$
3. Compute $\psi_T(\omega_j)$ for $j = 0,\ldots,N-1$
4. Apply **FFT** to get $\{c_T(k_u)\}$
5. Extract $C(K_u) = e^{-\alpha k_u}c_T(k_u)$

### **Complexity**

- **Direct integration**: $O(N^2)$ for $N$ strikes
- **FFT**: $O(N\log N)$ for $N$ strikes simultaneously

**Speedup factor**: $\frac{N}{\log_2 N}$, e.g., for $N = 1024$: speedup $\approx 100\times$.

---

## **7. Lewis Formula (Gil-Pelaez)**

### **Alternative Inversion**

The **Gil-Pelaez inversion theorem** avoids damping:

$$\boxed{C(K,S,T) = \frac{S}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega \ln(K/S)}\phi(\omega-i)}{i\omega}\right]d\omega - \frac{Ke^{-rT}}{2}}$$

$$\boxed{\quad - \frac{Ke^{-rT}}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega)}{i\omega}\right]d\omega}$$

where $\phi(\omega)$ is the characteristic function of $\ln(S_T/S_0)$ under $\mathbb{Q}$.

### **Simplified Form**

Combining terms:
$$\boxed{C = S\cdot\Pi_1 - Ke^{-rT}\cdot\Pi_2}$$

where:
$$\Pi_1 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega-i)}{i\omega}\right]d\omega$$

$$\Pi_2 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega)}{i\omega}\right]d\omega$$

### **Connection to Black-Scholes**

For lognormal $\phi$, after evaluation of integrals:
- $\Pi_1 = N(d_1)$
- $\Pi_2 = N(d_2)$

Recovering the Black-Scholes formula!

### **Advantages over Carr-Madan**

1. **No damping parameter** $\alpha$ to choose
2. **Direct** formula without modification
3. Works for **wider class** of characteristic functions
4. **Numerically stable** for most models

---

## **8. COS Method (Fang-Oosterlee)**

### **Fourier-Cosine Expansion**

Expand the density on $[a,b]$:
$$f(x) = \sum_{k=0}^{\infty}A_k\cos\left(k\pi\frac{x-a}{b-a}\right)$$

where:
$$A_0 = \frac{1}{b-a}\int_a^b f(x)dx, \quad A_k = \frac{2}{b-a}\int_a^b f(x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx$$

### **Coefficients via Characteristic Function**

$$\boxed{A_k = \frac{2}{b-a}\text{Re}\left[\phi\left(\frac{k\pi}{b-a}\right)e^{-ik\pi\frac{a}{b-a}}\right]}$$

for $k \geq 1$, and $A_0 = \frac{2}{b-a}\text{Re}[\phi(0)e^{0}] = \frac{2}{b-a}$ (normalized).

### **Option Pricing**

For a European option with payoff $\Phi(x)$:
$$V(x_0,0) = e^{-rT}\int_a^b\Phi(x)f(x|x_0)dx$$

$$\approx e^{-rT}\sum_{k=0}^{N-1}A_k V_k(x_0)$$

where:
$$V_k(x_0) = \int_a^b\Phi(x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx$$

### **For European Call**

With $\Phi(x) = K(e^x - 1)^+$:

$$V_k = K\int_0^b(e^x-1)\cos\left(k\pi\frac{x-a}{b-a}\right)dx$$

This can be evaluated analytically:
$$\boxed{V_k = \frac{K}{1+\left(\frac{k\pi}{b-a}\right)^2}\left[\cos\left(k\pi\frac{-a}{b-a}\right) + \frac{k\pi}{b-a}\sin\left(k\pi\frac{-a}{b-a}\right) - e^b\cos\left(k\pi\frac{b-a}{b-a}\right)\right] + \cdots}$$

### **Advantages**

1. **Exponential convergence**: Error $\sim O(e^{-cN})$ for smooth densities
2. **No FFT required**: Direct summation
3. **Flexible payoffs**: Any payoff with computable $V_k$
4. **Barrier options**: Easy to incorporate by restricting $[a,b]$

### **Choosing $[a,b]$**

Typically choose:
$$a = \mathbb{E}[X] - L\sqrt{\text{Var}(X)}, \quad b = \mathbb{E}[X] + L\sqrt{\text{Var}(X)}$$

where $L \approx 10$ captures $\approx 99.99\%$ of the distribution.

---

## **9. Multi-Dimensional Extensions**

### **Two-Asset Option**

For $V(S_1, S_2, t)$, define:
$$\mathbf{x} = (\ln S_1, \ln S_2), \quad \mathbf{\omega} = (\omega_1, \omega_2)$$

**2D Fourier transform**:
$$\boxed{\hat{V}(\mathbf{\omega},\tau) = \int_{\mathbb{R}^2}V(\mathbf{x},\tau)e^{-i\mathbf{\omega}\cdot\mathbf{x}}d\mathbf{x}}$$

### **Joint Characteristic Function**

For $\mathbf{X} = (\ln S_1, \ln S_2)$ under $\mathbb{Q}$:
$$\phi_{\mathbf{X}}(\mathbf{\omega}) = \mathbb{E}[e^{i\mathbf{\omega}\cdot\mathbf{X}}]$$

For **bivariate lognormal** with correlation $\rho$:
$$\phi(\omega_1,\omega_2) = \exp\left[i\sum_j\omega_j\mu_j - \frac{1}{2}\sum_{j,k}\omega_j\omega_k\Sigma_{jk}\right]$$

where:
$$\Sigma = \begin{pmatrix}\sigma_1^2\tau & \rho\sigma_1\sigma_2\tau \\ \rho\sigma_1\sigma_2\tau & \sigma_2^2\tau\end{pmatrix}$$

### **Solution**

$$\hat{V}(\mathbf{\omega},\tau) = \hat{\Phi}(\mathbf{\omega})e^{-r\tau}\phi_{\mathbf{X}}(\mathbf{\omega},\tau)$$

**Inverse**:
$$V(\mathbf{x},\tau) = \frac{1}{(2\pi)^2}\int_{\mathbb{R}^2}\hat{\Phi}(\mathbf{\omega})e^{-r\tau}\phi(\mathbf{\omega})e^{i\mathbf{\omega}\cdot\mathbf{x}}d\mathbf{\omega}$$

### **2D FFT**

For numerical evaluation, use **2D FFT**:
- Discretize on grid: $(x_1^j, x_2^k)$ for $j,k = 0,\ldots,N-1$
- Compute 2D DFT: $O(N^2\log N)$ operations
- Extract option values on grid

### **Curse of Dimensionality**

For $d$ assets:
- Grid points: $N^d$
- FFT complexity: $O(N^d \log N)$
- Becomes prohibitive for $d > 3$ or $4$

**Alternatives** for high dimensions:
- **Monte Carlo** (no curse of dimensionality)
- **Sparse grids** (reduce $N^d \to O(N\log^{d-1}N)$)
- **Quasi-Monte Carlo** with Fourier methods

---

## **10. Lévy Processes**

### **General Lévy Process**

A Lévy process $L_t$ has **stationary independent increments** with characteristic function:

$$\mathbb{E}[e^{i\omega L_t}] = e^{t\psi(\omega)}$$

where $\psi(\omega)$ is the **Lévy-Khintchine exponent**:

$$\boxed{\psi(\omega) = i\omega\mu - \frac{\sigma^2\omega^2}{2} + \int_{\mathbb{R}}\left(e^{i\omega x} - 1 - i\omega x\mathbb{1}_{|x|<1}\right)\nu(dx)}$$

- $\mu$: drift
- $\sigma^2$: diffusion coefficient
- $\nu(dx)$: **Lévy measure** (jump density)

### **Option Pricing**

For $S_t = S_0 e^{rt + L_t}$ (under $\mathbb{Q}$):

$$V(S,t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi(S_0e^{L_\tau})]$$

$$= e^{-r\tau}\int_{-\infty}^{\infty}\Phi(S_0e^x)f_{L_\tau}(x)dx$$

**Fourier approach**:
$$f_{L_\tau}(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{t\psi(\omega)}e^{-i\omega x}d\omega$$

### **Variance Gamma Model**

**Lévy measure**:
$$\nu(dx) = \frac{1}{|x|}e^{-\lambda|x|}dx, \quad \lambda > 0$$

**Characteristic exponent**:
$$\psi(\omega) = -\frac{1}{\nu}\ln\left(1 - i\theta\nu\omega + \frac{\sigma^2\nu\omega^2}{2}\right)$$

where $\theta, \sigma, \nu$ are parameters.

### **NIG (Normal Inverse Gaussian)**

**Lévy measure**:
$$\nu(dx) = \frac{\alpha\delta}{\pi|x|}e^{\beta x}K_1(\alpha|x|)dx$$

where $K_1$ is the modified Bessel function.

**Characteristic function**:
$$\phi(\omega) = e^{\delta(\sqrt{\alpha^2-\beta^2} - \sqrt{\alpha^2-(\beta+i\omega)^2})}$$

### **CGMY Model**

**Lévy measure**:
$$\nu(dx) = \begin{cases}
\frac{Ce^{-G|x|}}{|x|^{1+Y}}dx & x < 0 \\
\frac{Ce^{-M|x|}}{|x|^{1+Y}}dx & x > 0
\end{cases}$$

where $C,G,M,Y$ are parameters ($Y < 2$).

**No closed-form CF**, but can be computed numerically.

### **Unified Fourier Framework**

**All Lévy models** fit into:
$$C(K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty}\text{Re}\left[e^{-i\omega k}\frac{e^{-rT}\phi_T(\omega-(\alpha+1)i)}{\alpha^2+\alpha-\omega^2+i(2\alpha+1)\omega}\right]d\omega$$

Only the **characteristic function** $\phi_T$ changes!

---

## **11. Stochastic Volatility Models**

### **Heston Model**

$$dS_t = rS_t dt + \sqrt{v_t}S_t dW_t^{(1)}$$
$$dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW_t^{(2)}$$

with $d\langle W^{(1)}, W^{(2)}\rangle = \rho dt$.

### **Joint Characteristic Function**

For $\mathbf{X}_t = (\ln S_t, v_t)$, the CF satisfies a **Riccati system**:

$$\phi(\omega,t) = \mathbb{E}[e^{i\omega\ln S_t}] = e^{A(t,\omega) + B(t,\omega)v_0 + i\omega\ln S_0}$$

where $A(t,\omega), B(t,\omega)$ solve:
$$\boxed{\frac{\partial B}{\partial t} = -\frac{\xi^2}{2}B^2 + (\kappa - i\rho\xi\omega - \frac{\xi^2}{2})B + \frac{\omega^2 + i\omega}{2}}$$

$$\boxed{\frac{\partial A}{\partial t} = \kappa\theta B + ir\omega}$$

with $A(0) = B(0) = 0$.

### **Explicit Solution**

Define:
$$d = \sqrt{(\kappa - i\rho\xi\omega)^2 + \xi^2(\omega^2 + i\omega)}$$

Then:
$$B(t,\omega) = \frac{(\omega^2+i\omega)(1-e^{-dt})}{2\kappa\theta/\xi^2 - d - (\kappa-i\rho\xi\omega)(1-e^{-dt})}$$

$$A(t,\omega) = ir\omega t + \frac{\kappa\theta}{\xi^2}\left[(\kappa-i\rho\xi\omega-d)t - 2\ln\left(\frac{1-ge^{-dt}}{1-g}\right)\right]$$

where $g = \frac{\kappa-i\rho\xi\omega-d}{\kappa-i\rho\xi\omega+d}$.

### **Option Pricing**

Use **Lewis formula** or **Carr-Madan** with Heston's $\phi(\omega,t)$:

$$C = \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega-i,T)}{i\omega}\right]d\omega - Ke^{-rT}\cdot\Pi_2$$

### **Computational Notes**

- The **branch cut** of $\sqrt{\cdot}$ in $d$ requires careful handling
- Use **rotation count algorithm** or choose branch consistently
- Numerical integration: adaptive quadrature (Gauss-Kronrod)

---

## **12. Fractional FFT (FRFT)**

### **Motivation**

Standard FFT requires:
$$\Delta k \cdot \Delta\omega = \frac{2\pi}{N}$$

This **couples** strike spacing $\Delta k$ to frequency spacing $\Delta\omega$.

**Problem**: May want dense strikes but sparse frequencies (or vice versa).

### **Fractional FFT Solution**

**Idea**: Use **chirp-z transform** to decouple grids.

The transform:
$$F(k) = \sum_{j=0}^{N-1}f(x_j)e^{-i\omega_k x_j}$$

can be rewritten as:
$$e^{-i\omega_k x_j} = e^{-i[(k-j)^2 - k^2 - j^2]/2 \cdot \Delta\omega\Delta x}$$

This converts to **convolution**:
$$F(k) = e^{-ik^2\Delta\omega\Delta x/2}\sum_{j=0}^{N-1}\left[f(x_j)e^{-ij^2\Delta\omega\Delta x/2}\right] \cdot e^{-i(k-j)^2\Delta\omega\Delta x/2}$$

The convolution is computed via FFT: $O(N\log N)$.

### **Advantages**

1. **Arbitrary strike spacing**: Choose $\Delta k$ independently
2. **Arbitrary frequency spacing**: Choose $\Delta\omega$ independently
3. **Focused grids**: Concentrate points where needed

### **Applications**

- **Out-of-the-money options**: Dense strikes near spot
- **Long maturities**: Dense frequencies near $\omega = 0$
- **Calibration**: Match market strike grid exactly

---

## **13. Convolution Methods**

### **Convolution Theorem**

For densities $f_X, f_Y$ of independent RVs:
$$f_{X+Y} = f_X * f_Y$$

In Fourier space:
$$\phi_{X+Y} = \phi_X \cdot \phi_Y$$

### **Multi-Period Options**

For a **cliquet option** with resets at $t_1, \ldots, t_n$:

The payoff depends on $\sum_{i=1}^n R_i$ where $R_i = \ln(S_{t_i}/S_{t_{i-1}})$.

**Characteristic function**:
$$\phi_{\sum R_i}(\omega) = \prod_{i=1}^n \phi_{R_i}(\omega)$$

Compute each $\phi_{R_i}$ separately, multiply, and invert.

### **Compound Options**

A **call on a call** requires nested expectations.

**Outer expectation**: Use Fourier inversion
**Inner expectation**: Closed-form if European

Combine via characteristic function manipulations.

---

## **14. Time-Dependent Parameters**

### **Piecewise Constant Volatility**

If $\sigma(t) = \sigma_i$ for $t \in [t_{i-1}, t_i)$:

$$\text{Var}(\ln S_T) = \sum_{i=1}^n \sigma_i^2(t_i - t_{i-1})$$

**Characteristic function**:
$$\phi(\omega) = \exp\left[i\omega\sum_i(r-\frac{\sigma_i^2}{2})(t_i-t_{i-1}) - \frac{\omega^2}{2}\sum_i\sigma_i^2(t_i-t_{i-1})\right]$$

### **Local Volatility**

For $\sigma = \sigma(S,t)$, the characteristic function is **not explicit**.

**Numerical approach**:
1. Solve Kolmogorov forward equation for density
2. Compute CF via Fourier transform of density
3. Use in pricing formulas

Alternatively: **PDE methods** more efficient than Fourier.

### **Stochastic Interest Rates**

With $r_t$ stochastic and independent of $S_t$:

$$C = \mathbb{E}[e^{-\int_0^T r_s ds}\Phi(S_T)]$$

$$= \mathbb{E}_{r}\left[\mathbb{E}_S[\Phi(S_T)|r] \cdot e^{-\int_0^T r_s ds}\right]$$

Compute:
1. **Inner expectation**: Conditional on interest rate path
2. **Outer expectation**: Over interest rate distribution

Fourier methods apply to inner expectation with path-dependent discounting.

---

## **15. American Options**

### **Challenge**

American options involve **optimal stopping**:
$$V(S,t) = \sup_{\tau \in [t,T]}\mathbb{E}[e^{-r(\tau-t)}\Phi(S_\tau)|S_t = S]$$

Fourier methods are **not directly applicable** to free boundary problems.

### **Lower Bound via European**

$$V_{\text{American}} \geq V_{\text{European}}$$

Can compute European value via Fourier, giving a lower bound.

### **Richardson Extrapolation**

Approximate American by sequence of **Bermudan options** with $n$ exercise dates:
$$V_{\text{Bermudan}}^{(n)} \to V_{\text{American}} \text{ as } n \to \infty$$

Use **Richardson extrapolation**:
$$V_{\text{American}} \approx V_{\text{Bermudan}}^{(n)} + \frac{V_{\text{Bermudan}}^{(n)} - V_{\text{Bermudan}}^{(n/2)}}{2^p - 1}$$

where $p$ is the order of convergence.

### **CONV Method**

**Lord et al.** developed a Fourier-based method:
1. Discretize time: $t_0, t_1, \ldots, t_N$
2. At each $t_i$, compute continuation value via Fourier
3. Compare with intrinsic value
4. Use **dynamic programming** backward

**Complexity**: $O(N \cdot M\log M)$ where $M$ is spatial grid size.

---

## **16. Barrier Options**

### **Reflection Principle**

For a **down-and-out call** with barrier $B < S < K$:

The **method of images** gives:
$$V_{DO}(S) = C_{BS}(S) - \left(\frac{B}{S}\right)^{2r/\sigma^2}C_{BS}\left(\frac{B^2}{S}\right)$$

Each term is computed via Fourier methods separately.

### **Fourier-Based Approach**

Alternatively, compute the **distribution of $\inf_{0 \leq s \leq T}S_s$** and integrate:

$$V(S,t) = e^{-rT}\int_B^{\infty}\int_0^{\infty}\Phi(S_T)\mathbb{1}_{\inf S_s > B}f(S_T, \inf S_s)dS_T d(\inf S_s)$$

The joint density can be computed via **Fourier methods** using the **Wiener-Hopf technique**.

### **First Passage Time**

The **Laplace transform** of the first passage time density:
$$\mathbb{E}[e^{-\lambda\tau_B}] = \exp\left[-\frac{2}{\sigma^2}(r - \frac{\sigma^2}{2})\ln\frac{S}{B} - \frac{1}{\sigma}\sqrt{2\lambda + (r-\frac{\sigma^2}{2})^2/\sigma^2}\ln\frac{S}{B}\right]$$

This can be inverted numerically.

---

## **17. Greeks via Fourier Methods**

### **Delta**

$$\Delta = \frac{\partial C}{\partial S} = \frac{1}{S}\frac{\partial C}{\partial x}$$

where $x = \ln S$.

From Fourier representation:
$$C(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{C}(\omega,\tau)e^{i\omega x}d\omega$$

we get:
$$\frac{\partial C}{\partial x} = \frac{1}{2\pi}\int_{-\infty}^{\infty}i\omega\hat{C}(\omega,\tau)e^{i\omega x}d\omega$$

So:
$$\boxed{\Delta = \frac{1}{S}\cdot\frac{1}{2\pi}\int_{-\infty}^{\infty}i\omega\hat{C}(\omega,\tau)e^{i\omega x}d\omega}$$

### **Gamma**

$$\Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{1}{S^2}\left[\frac{\partial^2 C}{\partial x^2} - \frac{\partial C}{\partial x}\right]$$

$$\boxed{\Gamma = \frac{1}{S^2}\cdot\frac{1}{2\pi}\int_{-\infty}^{\infty}(-\omega^2 - i\omega)\hat{C}(\omega,\tau)e^{i\omega x}d\omega}$$

### **Vega**

For models with stochastic volatility (e.g., Heston):

$$\nu = \frac{\partial C}{\partial v_0}$$

From $C = \frac{1}{2\pi}\int \phi(\omega)e^{i\omega x}d\omega$ with $\phi$ depending on $v_0$:

$$\nu = \frac{1}{2\pi}\int\frac{\partial\phi(\omega)}{\partial v_0}e^{i\omega x}d\omega$$

The derivative $\frac{\partial\phi}{\partial v_0}$ can be computed from the Riccati equations.

### **Theta**

$$\Theta = \frac{\partial C}{\partial t} = -\frac{\partial C}{\partial \tau}$$

$$= -\frac{1}{2\pi}\int\frac{\partial}{\partial\tau}[\hat{\Phi}(\omega)e^{\psi(\omega)\tau}]e^{i\omega x}d\omega$$

$$\boxed{\Theta = -\frac{1}{2\pi}\int\psi(\omega)\hat{\Phi}(\omega)e^{\psi(\omega)\tau}e^{i\omega x}d\omega}$$

### **Computational Efficiency**

All Greeks computed from **same FFT**:
1. Compute $\hat{C}(\omega_j,\tau)$ once
2. Multiply by $i\omega_j$, $-\omega_j^2$, $\psi(\omega_j)$, etc.
3. Apply inverse FFT for each Greek

**Cost**: $O(N\log N)$ per Greek (minimal overhead).

---

## **18. Numerical Integration Techniques**

### **Adaptive Quadrature**

For integrals:
$$I = \int_0^{\infty}f(\omega)d\omega$$

where $f$ decays but has oscillations.

**Gauss-Kronrod rules**:
- Adaptive subdivision
- Error estimation
- Stop when tolerance reached

### **Fourier-Bessel Transform**

For radially symmetric problems:
$$\hat{f}(\rho) = \int_0^{\infty}f(r)J_0(\rho r)r\,dr$$

where $J_0$ is the Bessel function of the first kind.

Used in **multi-dimensional** problems with spherical symmetry.

### **Filon Method**

For highly oscillatory integrands:
$$I = \int_a^b f(\omega)e^{i\lambda\omega}d\omega, \quad \lambda \gg 1$$

**Filon's method**: Uses moments of $f$ to achieve accuracy independent of $\lambda$.

### **Complex Integration**

Move integration contour to:
$$\omega \to \omega + i\eta$$

This **damps oscillations** and improves convergence:
$$e^{i(\omega+i\eta)x} = e^{-\eta x}e^{i\omega x}$$

Must ensure analyticity in the strip.

---

## **19. Comparison with Other Methods**

### **Fourier vs. Monte Carlo**

| **Aspect** | **Fourier** | **Monte Carlo** |
|------------|-------------|-----------------|
| Complexity | $O(N\log N)$ | $O(M)$ paths |
| Accuracy | Spectral (smooth) | $O(1/\sqrt{M})$ |
| Dimension | Curse ($N^d$) | No curse |
| Model flexibility | Needs CF | Any model |
| Greeks | Cheap | Expensive |

### **Fourier vs. PDE**

| **Aspect** | **Fourier** | **Finite Difference** |
|------------|-------------|----------------------|
| Early exercise | Difficult | Natural |
| Smooth payoffs | Excellent | Good |
| Non-smooth payoffs | Oscillations | Stable |
| Multiple strikes | Simultaneous | One at a time |
| Exotic models | Easy if CF exists | Need to discretize |

### **When to Use Fourier**

**Best for**:
1. **European options** with many strikes
2. **Exotic models** (Lévy, stochastic vol) with known CF
3. **Smooth payoffs** (vanilla calls/puts)
4. **Low dimensions** ($d \leq 3$)
5. **Greeks** needed efficiently

**Avoid for**:
1. **American options** (use PDE or trees)
2. **Very non-smooth payoffs** (digitals → oscillations)
3. **High dimensions** ($d > 4$)
4. **Path-dependent** without CF structure

---

## **20. Advanced Applications**

### **Variance Swaps**

Fair strike:
$$K_{\text{var}}^2 = \mathbb{E}^{\mathbb{Q}}[\text{RV}^2] = \frac{2}{T}\mathbb{E}^{\mathbb{Q}}\left[\int_0^T\sigma_t^2 dt\right]$$

Using **log-contract replication**:
$$K_{\text{var}}^2 = \frac{2e^{rT}}{T}\left[\int_0^{S_0}\frac{P(K)}{K^2}dK + \int_{S_0}^{\infty}\frac{C(K)}{K^2}dK\right]$$

Compute $C(K), P(K)$ via FFT for continuum of strikes.

### **Volatility Derivatives**

For options on realized variance:
$$\text{Payoff} = \left(\frac{1}{N}\sum_{i=1}^N\left[\ln\frac{S_{t_i}}{S_{t_{i-1}}}\right]^2 - K_{\text{var}}^2\right)^+$$

The **characteristic function** of realized variance in Heston:
$$\phi_{\text{RV}}(\omega) = \mathbb{E}\left[\exp\left(i\omega\int_0^T v_s ds\right)\right]$$

can be computed via **extended Heston formulas**.

Use Fourier methods to price.

### **Credit Derivatives**

For **CDS** pricing with jumps:
$$\lambda_t = \text{default intensity}$$

The **survival probability**:
$$\mathbb{Q}(\tau > t) = \mathbb{E}[e^{-\int_0^t\lambda_s ds}]$$

With **affine intensities**, the CF is known → Fourier pricing.

---

## **21. Summary: The Fourier Paradigm**

### **The Master Flowchart**

```
Option Payoff Φ(S)
    ↓
Transform to log-price: Φ(e^x)
    ↓
Fourier Transform: Φ̂(ω)
    ↓
Multiply by e^{ψ(ω)τ} (characteristic function)
    ↓
Inverse Fourier Transform
    ↓
Option Value V(x,τ)
```

### **Key Formulas**

**PDE in Fourier space**:
$$\boxed{\frac{\partial\hat{V}}{\partial\tau} = \psi(\omega)\hat{V}}$$

**Solution**:
$$\boxed{\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}}$$

**Inversion**:
$$\boxed{V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)e^{\psi(\omega)\tau}e^{i\omega x}d\omega}$$

### **The Power**

Fourier methods reveal that option pricing is fundamentally about:
1. **Transform** payoff to frequency domain
2. **Propagate** via characteristic function (evolution)
3. **Invert** back to price space

This works for **any model** where the characteristic function is known—which includes most models of practical interest!

### **The Beauty**

The **unification**:
- **Black-Scholes**: Gaussian CF
- **Lévy processes**: Exponential of Lévy-Khintchine
- **Stochastic volatility**: Riccati system
- **All** fit the same computational framework

Just **change the CF**, everything else stays the same!

---

Would you like me to explore:
- Detailed implementation of FFT algorithm for options
- Wiener-Hopf technique for barriers in detail
- Advanced characteristic function derivations (e.g., CGMY)
- Fourier methods for Asian and lookback options
- Numerical stability and accuracy analysis
- Extensions to rough volatility models (fractional Brownian motion)
- Connection between Fourier methods and PIDE (partial integro-differential equations)?
