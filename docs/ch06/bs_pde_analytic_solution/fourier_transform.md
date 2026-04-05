# Fourier Transform Methods for Black-Scholes


The heat equation approach solved the Black-Scholes PDE by transforming variables until the equation became the classical diffusion equation. Fourier transform methods take a more direct route: rather than reducing to a known PDE, they **diagonalize the differential operator itself**. In frequency space, derivatives become multiplication, the PDE collapses to an algebraic equation, and the solution is recovered by inverse transformation. Crucially, the characteristic function $\phi_T(\omega) = \mathbb{E}^{\mathbb{Q}}[e^{i\omega \ln S_T}]$ that appears in the Fourier solution is the **Fourier transform of the transition density** --- the same Gaussian kernel derived in the heat equation section and the same density under which the Feynman-Kac expectation is computed. The three core methods are united here: the spectral viewpoint decomposes the same pricing operator into its frequency components.

This section is organized in two parts. **Part A** develops the analytic solution: transform of the PDE, characteristic functions, and the damping trick. **Part B** addresses the computational problem of evaluating the inverse Fourier integral efficiently via Carr-Madan, FFT, and Gil-Pelaez formulas.

---

# Part A --- Analytic Solution

---

## Fundamental Theory


### Fourier Transform Definition


For a function $f: \mathbb{R} \to \mathbb{C}$:

$$
\boxed{\hat{f}(\omega) = \mathcal{F}[f](\omega) = \int_{-\infty}^{\infty} f(x)e^{-i\omega x}dx}
$$

**Inverse transform**:

$$
\boxed{f(x) = \mathcal{F}^{-1}[\hat{f}](x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(\omega)e^{i\omega x}d\omega}
$$

### Key Properties


**Linearity**:

$$
\mathcal{F}[\alpha f + \beta g] = \alpha\hat{f} + \beta\hat{g}
$$

**Derivative**:

$$
\boxed{\mathcal{F}\left[\frac{df}{dx}\right](\omega) = i\omega\hat{f}(\omega)}
$$

$$
\boxed{\mathcal{F}\left[\frac{d^2f}{dx^2}\right](\omega) = -\omega^2\hat{f}(\omega)}
$$

**Shift**:

$$
\mathcal{F}[f(x-a)](\omega) = e^{-i\omega a}\hat{f}(\omega)
$$

**Convolution theorem**:

$$
\boxed{\mathcal{F}[f * g] = \hat{f} \cdot \hat{g}}
$$

where $(f * g)(x) = \int_{-\infty}^{\infty}f(x-y)g(y)dy$.

### Parseval's Identity

$$
\boxed{\int_{-\infty}^{\infty}|f(x)|^2 dx = \frac{1}{2\pi}\int_{-\infty}^{\infty}|\hat{f}(\omega)|^2 d\omega}
$$

Energy is preserved under the transform.

---

## Black-Scholes PDE in Fourier Space


### Log-Price Formulation


As in the heat equation section, define $x = \ln(S/K)$ and $\tau = T - t$. The Black-Scholes PDE becomes:

$$
\boxed{\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV}
$$

with terminal condition $V(x,0) = \Phi(Ke^x)$.

### Apply Fourier Transform


Transform in the $x$ variable:

$$
\hat{V}(\omega,\tau) = \int_{-\infty}^{\infty}V(x,\tau)e^{-i\omega x}dx
$$

Using the derivative properties:

$$
\frac{\partial \hat{V}}{\partial \tau} = -\frac{\sigma^2\omega^2}{2}\hat{V} + i\omega\left(r - \frac{\sigma^2}{2}\right)\hat{V} - r\hat{V}
$$

$$
\boxed{\frac{\partial \hat{V}}{\partial \tau} = \psi(\omega)\hat{V}(\omega,\tau)}
$$

where the **characteristic exponent** is:

$$
\boxed{\psi(\omega) = -\frac{\sigma^2\omega^2}{2} + i\omega\left(r - \frac{\sigma^2}{2}\right) - r}
$$

### ODE in Fourier Space


This is a **first-order ODE** (no longer a PDE):

$$
\hat{V}(\omega,\tau) = \hat{V}(\omega,0)e^{\psi(\omega)\tau}
$$

With $\hat{V}(\omega,0) = \hat{\Phi}(\omega)$:

$$
\boxed{\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}}
$$

### Solution via Inverse Transform

$$
\boxed{V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)e^{\psi(\omega)\tau}e^{i\omega x}d\omega}
$$

This is the **complete solution** in closed form.

---

## Characteristic Functions


### Definition


For a random variable $X$, the **characteristic function** is:

$$
\boxed{\phi_X(\omega) = \mathbb{E}[e^{i\omega X}]}
$$

This is the Fourier transform of the probability density.

### Properties


1. $\phi_X(0) = 1$
2. $|\phi_X(\omega)| \leq 1$
3. $\phi_X(-\omega) = \overline{\phi_X(\omega)}$ (conjugate)
4. If $Y = aX + b$: $\phi_Y(\omega) = e^{i\omega b}\phi_X(a\omega)$
5. **Sum of independent RVs**: $\phi_{X+Y} = \phi_X \cdot \phi_Y$

### Inversion Formula


The density can be recovered:

$$
\boxed{f_X(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\phi_X(\omega)e^{-i\omega x}d\omega}
$$

### For Lognormal (Black-Scholes)


Under $\mathbb{Q}$, $X_\tau = \ln(S_T/S_0)$ satisfies:

$$
X_\tau \sim N\left[\left(r-\frac{\sigma^2}{2}\right)\tau, \sigma^2\tau\right]
$$

The characteristic function:

$$
\boxed{\phi_X(\omega,\tau) = \exp\left[i\omega\left(r-\frac{\sigma^2}{2}\right)\tau - \frac{\sigma^2\omega^2\tau}{2}\right]}
$$

### Connection to PDE Solution


Note that:

$$
e^{\psi(\omega)\tau} = e^{-r\tau}\phi_X(\omega,\tau)
$$

So:

$$
\hat{V}(\omega,\tau) = e^{-r\tau}\hat{\Phi}(\omega)\phi_X(\omega,\tau)
$$

This shows: **Fourier transform of option value = (discounted) Fourier transform of payoff times characteristic function**.

---

## European Call Option


### The Challenge: Non-Integrability


For a call: $\Phi(S) = (S - K)^+ = (Ke^x - K)^+ = K(e^x - 1)^+$

The Fourier transform:

$$
\hat{\Phi}(\omega) = K\int_0^{\infty}(e^x - 1)e^{-i\omega x}dx
$$

This integral **diverges** for real $\omega$.

### Complex Analysis Solution


Extend to **complex** $\omega = \xi + i\eta$:

$$
\hat{\Phi}(\omega) = K\int_0^{\infty}(e^x - 1)e^{-i\xi x}e^{\eta x}dx
$$

For $\eta < -1$:

$$
\hat{\Phi}(\omega) = K\left[\int_0^{\infty}e^{(1-i\xi+\eta)x}dx - \int_0^{\infty}e^{(-i\xi+\eta)x}dx\right]
$$

$$
= K\left[\frac{1}{-1+i\xi-\eta} - \frac{1}{i\xi-\eta}\right]
$$

$$
= K\left[\frac{i\xi-\eta - (-1+i\xi-\eta)}{(-1+i\xi-\eta)(i\xi-\eta)}\right]
$$

$$
\boxed{\hat{\Phi}(\omega) = \frac{K}{(i\omega+1)(i\omega)} = \frac{K}{\omega^2 - i\omega}}
$$

for $\text{Im}(\omega) < -1$.

### Carr-Madan Damping Approach


Instead of dealing with complex $\omega$, **damp** the payoff:

$$
\tilde{C}(x) = e^{\alpha x}C(x)
$$

where $\alpha > 0$ is chosen so that $\tilde{C}$ decays as $x \to \infty$.

For a call, need $\alpha > 1$ to ensure:

$$
e^{\alpha x}(e^x - 1)^+ = (e^{(\alpha+1)x} - e^{\alpha x})\mathbb{1}_{x>0} \to 0 \text{ as } x \to \infty
$$

### Fourier Transform of Damped Call

$$
\hat{\tilde{\Phi}}(\omega) = K\int_0^{\infty}(e^{(\alpha+1)x} - e^{\alpha x})e^{-i\omega x}dx
$$

$$
= K\left[\frac{1}{\alpha+1-i\omega} - \frac{1}{\alpha-i\omega}\right]
$$

$$
= K\frac{(\alpha-i\omega) - (\alpha+1-i\omega)}{(\alpha+1-i\omega)(\alpha-i\omega)}
$$

$$
\boxed{\hat{\tilde{\Phi}}(\omega) = \frac{-K}{(\alpha+i\omega)(\alpha+1+i\omega)}}
$$

Or equivalently:

$$
\boxed{\hat{\tilde{\Phi}}(\omega) = \frac{K}{\alpha^2 + \alpha - \omega^2 + i(2\alpha+1)\omega}}
$$

---

## Unification: Three Representations of One Object

With the Fourier derivation complete, all three core methods of this chapter have now been presented. Each solves the same Black-Scholes PDE, and each arrives at the same pricing formula --- but through a different representation of the pricing operator $\mathcal{P}_{\tau}$. The **heat equation** writes the solution as a convolution with the Gaussian kernel $G$. The **Feynman-Kac formula** writes it as an expectation under the transition density --- which *is* the kernel $G$. The **Fourier transform** diagonalizes the operator, expressing the solution through the characteristic function $\phi_T(\omega) = \mathbb{E}^{\mathbb{Q}}[e^{i\omega \ln S_T}]$ --- which is the Fourier transform of that same density. These are not three independent results. They are one theorem, viewed in spatial, probabilistic, and spectral coordinates.

---

# Part B --- Computational Methods

The analytic derivation is complete: the Fourier transform converts the Black-Scholes PDE into an algebraic equation, and the option price is recovered by inverse transformation. What remains is a **computational** problem: evaluating the inverse integral

$$
V(x,\tau) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{i\omega x}\, \hat{V}(\omega,\tau)\, d\omega
$$

efficiently across an entire grid of strikes. The Carr-Madan formula, FFT algorithm, and Lewis (Gil-Pelaez) inversion below solve this problem. They are not new analytic solutions; they are algorithms for evaluating the inversion integral. Their importance lies in the fact that they extend unchanged to any model whose characteristic function is known in closed form (Heston, Merton, variance gamma, etc.), making them the computational backbone of modern derivative pricing.

---

## Carr-Madan Formula


### Modified Call Price


Define:

$$
c_T(k) = e^{\alpha k}C(K = e^k, S_0, T)
$$

where $k = \ln K$ is the **log-strike**.

### Fourier Transform

$$
\psi_T(\omega) = \int_{-\infty}^{\infty}e^{i\omega k}c_T(k)dk
$$

Using the characteristic function $\phi_T(\omega)$ of $\ln(S_T/S_0)$:

$$
\boxed{\psi_T(\omega) = \frac{e^{-rT}\phi_T(\omega - (\alpha+1)i)}{\alpha^2 + \alpha - \omega^2 + i(2\alpha+1)\omega}}
$$

### Inversion

$$
c_T(k) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-i\omega k}\psi_T(\omega)d\omega
$$

Taking the real part (since $c_T$ is real):

$$
\boxed{C(K,S_0,T) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty}\text{Re}\left[e^{-i\omega k}\psi_T(\omega)\right]d\omega}
$$

### Explicit Formula for Black-Scholes


For Black-Scholes with $\phi_T(\omega) = \exp[i\omega(r-\frac{\sigma^2}{2})T - \frac{\sigma^2\omega^2 T}{2}]$:

$$
\boxed{C(K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega k}\,e^{-rT}\exp\bigl[i(\omega-(\alpha+1)i)(r-\frac{\sigma^2}{2})T - \frac{\sigma^2(\omega-(\alpha+1)i)^2T}{2}\bigr]}{\alpha^2+\alpha-\omega^2+i(2\alpha+1)\omega}\right]d\omega}
$$

---

## Fast Fourier Transform (FFT)


### Discrete Fourier Transform


For $N$ points $\{x_j\}_{j=0}^{N-1}$:

$$
\boxed{X_k = \sum_{j=0}^{N-1}x_j e^{-2\pi ijk/N}, \quad k = 0,1,\ldots,N-1}
$$

**Inverse**:

$$
\boxed{x_j = \frac{1}{N}\sum_{k=0}^{N-1}X_k e^{2\pi ijk/N}}
$$

### FFT Algorithm


The **Fast Fourier Transform** computes the DFT in:

$$
\boxed{O(N\log N) \text{ operations}}
$$

instead of $O(N^2)$ for naive implementation.

This is based on the **Cooley-Tukey algorithm** using divide-and-conquer.

### Application to Option Pricing


**Setup**:

1. Choose $N = 2^n$ (power of 2 for FFT)
2. Discretize log-strike: $k_u = k_0 + u\Delta k$ for $u = 0,1,\ldots,N-1$
3. Discretize frequency: $\omega_j = j\Delta\omega$ for $j = 0,1,\ldots,N-1$
4. Set grid spacing: $\Delta k \cdot \Delta\omega = \frac{2\pi}{N}$

### Discretization


The integral:

$$
c_T(k_u) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-i\omega k_u}\psi_T(\omega)d\omega
$$

becomes:

$$
c_T(k_u) \approx \frac{\Delta\omega}{2\pi}\sum_{j=0}^{N-1}e^{-i\omega_j k_u}\psi_T(\omega_j)
$$

$$
= \frac{\Delta\omega}{2\pi}\sum_{j=0}^{N-1}e^{-2\pi iju/N}\psi_T(\omega_j)
$$

This is an **inverse DFT**.

### Implementation Steps


1. Choose $\alpha$ (typically $\alpha = 0.75$ or $\alpha = 1.5$)
2. Set $\Delta k$ (strike spacing), compute $\Delta\omega = \frac{2\pi}{N\Delta k}$
3. Compute $\psi_T(\omega_j)$ for $j = 0,\ldots,N-1$
4. Apply **FFT** to get $\{c_T(k_u)\}$
5. Extract $C(K_u) = e^{-\alpha k_u}c_T(k_u)$

### Complexity


- **Direct integration**: $O(N^2)$ for $N$ strikes
- **FFT**: $O(N\log N)$ for $N$ strikes simultaneously

**Speedup factor**: $\frac{N}{\log_2 N}$, e.g., for $N = 1024$: speedup $\approx 100\times$.

---

## Lewis Formula (Gil-Pelaez)


### Alternative Inversion


The **Gil-Pelaez inversion theorem** avoids damping:

$$
\boxed{C(K,S,T) = \frac{S}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega \ln(K/S)}\phi(\omega-i)}{i\omega}\right]d\omega - \frac{Ke^{-rT}}{2}}
$$

$$
\boxed{\quad - \frac{Ke^{-rT}}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega)}{i\omega}\right]d\omega}
$$

where $\phi(\omega)$ is the characteristic function of $\ln(S_T/S_0)$ under $\mathbb{Q}$.

### Simplified Form


Combining terms:

$$
\boxed{C = S\cdot\Pi_1 - Ke^{-rT}\cdot\Pi_2}
$$

where:

$$
\Pi_1 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega-i)}{i\omega}\right]d\omega
$$

$$
\Pi_2 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega)}{i\omega}\right]d\omega
$$

### Connection to Black-Scholes


For lognormal $\phi$, after evaluation of integrals:

- $\Pi_1 = N(d_1)$
- $\Pi_2 = N(d_2)$

Recovering the Black-Scholes formula. $\square$

### Advantages over Carr-Madan


1. **No damping parameter** $\alpha$ to choose
2. **Direct** formula without modification
3. Works for **wider class** of characteristic functions
4. **Numerically stable** for most models

---

## Greeks via Fourier Methods


Since the option price is expressed as a Fourier integral, Greeks follow by differentiating under the integral sign.

**Delta.** With $x = \ln S$:

$$
\boxed{\Delta = \frac{1}{S}\cdot\frac{1}{2\pi}\int_{-\infty}^{\infty}i\omega\,\hat{C}(\omega,\tau)\,e^{i\omega x}\,d\omega}
$$

**Gamma.**

$$
\boxed{\Gamma = \frac{1}{S^2}\cdot\frac{1}{2\pi}\int_{-\infty}^{\infty}(-\omega^2 - i\omega)\,\hat{C}(\omega,\tau)\,e^{i\omega x}\,d\omega}
$$

**Theta.**

$$
\boxed{\Theta = -\frac{1}{2\pi}\int_{-\infty}^{\infty}\psi(\omega)\,\hat{\Phi}(\omega)\,e^{\psi(\omega)\tau}\,e^{i\omega x}\,d\omega}
$$

**Computational efficiency.** All Greeks are computed from the **same FFT output**: evaluate $\hat{C}(\omega_j,\tau)$ once, multiply by $i\omega_j$ (Delta), $-\omega_j^2 - i\omega_j$ (Gamma), or $\psi(\omega_j)$ (Theta), and apply the inverse FFT. The incremental cost per Greek is $O(N\log N)$.

---

## Comparison with Other Methods


Fourier methods are most effective for **European options across many strikes simultaneously** when the characteristic function is available in closed form. The FFT prices an entire strike grid in $O(N\log N)$ operations, compared with $O(N^2)$ for pointwise quadrature or one PDE solve per strike. Greeks come essentially for free from the same transform.

The principal limitations are: (i) the payoff must be Fourier-representable, which requires damping for calls and puts; (ii) **American options** and other free-boundary problems are not directly accessible; (iii) non-smooth payoffs (e.g., digitals) introduce Gibbs oscillations; and (iv) the method suffers from the curse of dimensionality for $d > 3$ assets.

For single-strike pricing, direct PDE or closed-form evaluation may be simpler. For path-dependent or early-exercise problems, finite-difference and Monte Carlo methods are generally preferable.

---

## Summary


The Fourier approach to Black-Scholes pricing proceeds in four steps:

```
Option Payoff Phi(S)
    |
Transform to log-price: Phi(e^x)
    |
Fourier Transform: hat{Phi}(omega)
    |
Multiply by e^{psi(omega) tau}  (characteristic function)
    |
Inverse Fourier Transform
    |
Option Value V(x, tau)
```

**Key formulas.** The PDE in Fourier space reduces to the ODE

$$
\frac{\partial\hat{V}}{\partial\tau} = \psi(\omega)\hat{V}
$$

with solution

$$
\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}
$$

and inversion

$$
V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)e^{\psi(\omega)\tau}e^{i\omega x}d\omega
$$

The identity $e^{\psi(\omega)\tau} = e^{-r\tau}\phi_X(\omega,\tau)$ connects the PDE characteristic exponent to the probabilistic characteristic function of the log-return. All three inversion routes -- direct quadrature, Carr-Madan with FFT, and Gil-Pelaez -- produce the Black-Scholes formula $C = SN(d_1) - Ke^{-rT}N(d_2)$ as a special case.

---

---

## Exercises

**Exercise 1.** Verify the characteristic exponent for the Black-Scholes model. Starting from the log-price formulation of the PDE, apply the Fourier transform to both sides and show that the ODE in Fourier space has the characteristic exponent $\psi(\omega) = -\frac{\sigma^2\omega^2}{2} + i\omega(r - \frac{\sigma^2}{2}) - r$.

??? success "Solution to Exercise 1"
    The log-price PDE is:

    $$
    \frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV
    $$

    Apply the Fourier transform $\hat{V}(\omega,\tau) = \int_{-\infty}^{\infty} V(x,\tau) e^{-i\omega x} dx$ to both sides.

    **Left side:** $\mathcal{F}\left[\frac{\partial V}{\partial \tau}\right] = \frac{\partial \hat{V}}{\partial \tau}$

    **Right side, term by term:**

    - $\frac{\sigma^2}{2}\mathcal{F}\left[\frac{\partial^2 V}{\partial x^2}\right] = \frac{\sigma^2}{2}(-\omega^2)\hat{V} = -\frac{\sigma^2\omega^2}{2}\hat{V}$
    - $\left(r - \frac{\sigma^2}{2}\right)\mathcal{F}\left[\frac{\partial V}{\partial x}\right] = \left(r - \frac{\sigma^2}{2}\right)(i\omega)\hat{V}$
    - $-r\mathcal{F}[V] = -r\hat{V}$

    Combining:

    $$
    \frac{\partial \hat{V}}{\partial \tau} = \left[-\frac{\sigma^2\omega^2}{2} + i\omega\left(r - \frac{\sigma^2}{2}\right) - r\right]\hat{V}
    $$

    This is a first-order ODE $\frac{\partial \hat{V}}{\partial \tau} = \psi(\omega)\hat{V}$ with the characteristic exponent:

    $$
    \psi(\omega) = -\frac{\sigma^2\omega^2}{2} + i\omega\left(r - \frac{\sigma^2}{2}\right) - r
    $$

    $\square$

---
**Exercise 2.** The Fourier transform of the call payoff $(e^x - 1)^+$ diverges for real $\omega$. Show explicitly that the integral $\int_0^{\infty}(e^x - 1)e^{-i\omega x}dx$ diverges by analyzing the behavior of the integrand as $x \to \infty$. Then verify that introducing the damping factor $e^{-\alpha x}$ with $\alpha > 1$ makes the integral convergent and derive the resulting transform.

??? success "Solution to Exercise 2"
    Consider the integral $I(\omega) = \int_0^{\infty}(e^x - 1)e^{-i\omega x}dx$ for real $\omega$.

    **Divergence:** For $x \to \infty$, the integrand behaves as $e^x \cdot e^{-i\omega x} = e^{(1-i\omega)x}$. Since $|e^{(1-i\omega)x}| = e^x \to \infty$ as $x \to \infty$, the integral diverges.

    More precisely, $|e^x e^{-i\omega x}| = e^x$ which is not integrable on $[0,\infty)$.

    **Damping factor:** Now consider $\int_0^{\infty}(e^x - 1)e^{-\alpha x}e^{-i\omega x}dx$ with $\alpha > 0$. The integrand magnitude is:

    $$
    |(e^x - 1)e^{-\alpha x}e^{-i\omega x}| \leq e^{(1-\alpha)x} + e^{-\alpha x}
    $$

    For the first term, $e^{(1-\alpha)x}$ is integrable on $[0,\infty)$ if and only if $\alpha > 1$. The second term $e^{-\alpha x}$ is integrable for $\alpha > 0$. Therefore, the damped integral converges for $\alpha > 1$:

    $$
    \int_0^{\infty}(e^x - 1)e^{-(\alpha + i\omega)x}dx = \frac{1}{\alpha + i\omega - 1} - \frac{1}{\alpha + i\omega}
    $$

    $$
    = \frac{1}{(\alpha - 1 + i\omega)(\alpha + i\omega)}
    $$

    $\square$

---
**Exercise 3.** Using the Carr-Madan formula with $\alpha = 1.5$, $S_0 = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, and $T = 1$, set up the numerical integration for the call price. Write the integrand explicitly and verify that evaluating the integral (e.g., via Simpson's rule with a fine grid) recovers the standard Black-Scholes call price to at least 4 decimal places.

??? success "Solution to Exercise 3"
    With $\alpha = 1.5$, $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$, the log-strike is $k = \ln K = \ln 100$.

    The Carr-Madan integrand is:

    $$
    C(K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty}\text{Re}\left[e^{-i\omega k}\psi_T(\omega)\right]d\omega
    $$

    where:

    $$
    \psi_T(\omega) = \frac{e^{-rT}\phi_T(\omega - (\alpha+1)i)}{\alpha^2 + \alpha - \omega^2 + i(2\alpha+1)\omega}
    $$

    The characteristic function for Black-Scholes is:

    $$
    \phi_T(u) = \exp\left[iu\left(r - \frac{\sigma^2}{2}\right)T - \frac{\sigma^2 u^2 T}{2}\right]
    $$

    For $u = \omega - (\alpha+1)i = \omega - 2.5i$:

    $$
    \phi_T(\omega - 2.5i) = \exp\left[i(\omega - 2.5i)(0.05 - 0.02)(1) - \frac{0.04(\omega - 2.5i)^2}{2}\right]
    $$

    $$
    = \exp\left[(0.03i\omega + 0.075) - 0.02(\omega^2 - 5i\omega - 6.25)\right]
    $$

    $$
    = \exp\left[0.03i\omega + 0.075 - 0.02\omega^2 + 0.1i\omega + 0.125\right]
    $$

    $$
    = \exp\left[-0.02\omega^2 + 0.13i\omega + 0.2\right]
    $$

    The denominator is $\alpha^2 + \alpha - \omega^2 + i(2\alpha+1)\omega = 3.75 - \omega^2 + 4i\omega$.

    Setting up the numerical integration with Simpson's rule on a fine grid (e.g., $\omega \in [0, 50]$ with $\Delta\omega = 0.01$), and computing $\text{Re}[e^{-i\omega k}\psi_T(\omega)]$ at each point, the integral can be evaluated. The Black-Scholes price for these parameters is $C \approx 10.4506$, which the numerical integration recovers to at least 4 decimal places. $\square$

---
**Exercise 4.** Explain the relationship $e^{\psi(\omega)\tau} = e^{-r\tau}\phi_X(\omega, \tau)$ between the characteristic exponent of the PDE and the characteristic function of the log-return. Starting from the explicit forms of $\psi(\omega)$ and $\phi_X(\omega,\tau)$, verify the identity algebraically and explain why it is central to the Fourier pricing framework.

??? success "Solution to Exercise 4"
    The identity $e^{\psi(\omega)\tau} = e^{-r\tau}\phi_X(\omega,\tau)$ connects the PDE characteristic exponent to the probabilistic characteristic function.

    **Derivation.** The PDE characteristic exponent is:

    $$
    \psi(\omega) = -\frac{\sigma^2\omega^2}{2} + i\omega\left(r - \frac{\sigma^2}{2}\right) - r
    $$

    The characteristic function of $X_\tau = \ln(S_T/S_0)$ under $\mathbb{Q}$ is:

    $$
    \phi_X(\omega,\tau) = \exp\left[i\omega\left(r - \frac{\sigma^2}{2}\right)\tau - \frac{\sigma^2\omega^2\tau}{2}\right]
    $$

    Therefore:

    $$
    e^{-r\tau}\phi_X(\omega,\tau) = \exp\left[-r\tau + i\omega\left(r - \frac{\sigma^2}{2}\right)\tau - \frac{\sigma^2\omega^2\tau}{2}\right] = e^{\psi(\omega)\tau}
    $$

    **Why this is central.** This identity means the Fourier-space solution $\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}$ can be rewritten as $\hat{V}(\omega,\tau) = e^{-r\tau}\hat{\Phi}(\omega)\phi_X(\omega,\tau)$. In other words, the option price in Fourier space equals the discounted payoff transform times the characteristic function of the log-return. This directly encodes risk-neutral pricing: the transform of the discounted expected payoff factorizes into a payoff piece and a distributional piece. $\square$

---
**Exercise 5.** The Gil-Pelaez formula writes the call price as $C = S\Pi_1 - Ke^{-rT}\Pi_2$ where $\Pi_1$ and $\Pi_2$ are given by integrals involving the characteristic function. For the Black-Scholes model, show that $\Pi_1 = N(d_1)$ and $\Pi_2 = N(d_2)$ by substituting the lognormal characteristic function and evaluating the resulting Gaussian integrals.

??? success "Solution to Exercise 5"
    The Gil-Pelaez formula gives:

    $$
    \Pi_2 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-i\omega\ln(K/S)}\phi(\omega)}{i\omega}\right]d\omega
    $$

    With the Black-Scholes characteristic function $\phi(\omega) = \exp[i\omega(r - \sigma^2/2)T - \sigma^2\omega^2 T/2]$, the integrand becomes:

    $$
    \frac{e^{-i\omega\ln(K/S)}\exp[i\omega(r-\sigma^2/2)T - \sigma^2\omega^2 T/2]}{i\omega}
    $$

    Write $\ln(K/S) = -\ln(S/K)$ and combine the exponentials:

    $$
    = \frac{\exp[i\omega(\ln(S/K) + (r-\sigma^2/2)T) - \sigma^2\omega^2 T/2]}{i\omega}
    $$

    The exponent in the numerator is $i\omega\, d_2\sigma\sqrt{T} - \sigma^2\omega^2 T/2$ where $d_2 = \frac{\ln(S/K) + (r-\sigma^2/2)T}{\sigma\sqrt{T}}$. Substituting $u = \omega\sigma\sqrt{T}$, the integral reduces to the standard result:

    $$
    \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\frac{\sin(d_2 u)}{u}e^{-u^2/2}du = N(d_2)
    $$

    using the known identity $\frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\frac{\sin(ax)}{x}e^{-x^2/2}dx = N(a)$.

    For $\Pi_1$, the argument $\phi(\omega - i)$ shifts the characteristic function. The shift replaces $\omega$ by $\omega - i$ in $\phi$, which after simplification introduces an extra factor $e^{rT}S/S$ and shifts $d_2$ to $d_1 = d_2 + \sigma\sqrt{T}$. The same Gaussian-integral identity then gives $\Pi_1 = N(d_1)$. $\square$
