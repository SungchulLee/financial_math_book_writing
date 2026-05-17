# Heston Model Characteristic Function

The characteristic function (CF) is the Fourier transform of the probability density function. For the Heston stochastic volatility model, the characteristic function has a closed-form expression that makes it invaluable for option pricing via Fourier methods.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Heston characteristic function
    2. Understand the role of the non-centrality parameter
    3. Use the CF for density recovery and option pricing

---

## Heston Model Specification

Recall (see [§ Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)) the Heston SDE under $\mathbb{Q}$ with vol-of-vol $\gamma$ and mean-reversion level $\bar v$.

---

## Characteristic Function Formula

The characteristic function of $X_T = \log S(T)$ conditional on the initial state $(t, S, v)$ is:

$$
\varphi(u) := \mathbb{E}^{\mathbb{Q}}\left[e^{iu X_T} \big| \mathcal{F}(t)\right] = e^{r(T-t) + A(\tau,u) + B(\tau,u)X + C(\tau,u)v}
$$

where $\tau = T - t$ is time to maturity, and the components are:

$$
\boxed{
\begin{aligned}
A(\tau,u) &= \frac{\kappa\bar{v}\tau}{\gamma^2}\left(\kappa - \gamma\rho iu - D\right) - \frac{2\kappa\bar{v}}{\gamma^2}\log\left(\frac{1 - ge^{-D\tau}}{1-g}\right)\\[0.5em]
B(\tau,u) &= iu\\[0.5em]
C(\tau,u) &= \frac{1 - e^{-D\tau}}{\gamma^2(1 - ge^{-D\tau})}(\kappa - \gamma\rho iu - D)\\[0.5em]
D &= \sqrt{(\kappa - \gamma\rho iu)^2 + (u^2 + iu)\gamma^2}\\[0.5em]
g &= \frac{\kappa - \gamma\rho iu - D}{\kappa - \gamma\rho iu + D}
\end{aligned}
}
$$

---

## Key Structural Elements

**Complex argument $D$:** The term $D$ encodes the interaction between mean reversion rate $\kappa$, volatility of volatility $\gamma$, and correlation $\rho$. The square root ensures the solution is well-defined for all complex arguments $u$.

**Ratio $g$:** The ratio $g$ is crucial for stability in numerical computation and controls the asymptotic behavior as $\tau \to \infty$.

**Logarithmic term in $A$:** The log term arises from integrating the CIR-type variance process and captures the mean reversion dynamics.

---

## Transform to Physical Measure

If we wish to transition from the risk-neutral measure $\mathbb{Q}$ to the physical measure $\mathbb{P}$, we adjust the mean reversion level and the drift:

$$
dS(t) = \mu S(t) dt + \sqrt{v(t)} S(t) dW_x^{\mathbb{P}}(t)
$$

$$
dv(t) = \kappa(\bar{v}^{\mathbb{P}} - v(t)) dt + \gamma\sqrt{v(t)} dW_v^{\mathbb{P}}(t)
$$

Under Girsanov's theorem, the risk-neutral mean reversion level becomes:

$$
\bar{v} = \bar{v}^{\mathbb{P}} - \frac{\rho\gamma(\mu - r)}{\kappa}
$$

This adjustment ensures consistency between physical and risk-neutral dynamics while preserving the Heston model structure.

---

## Properties and Computational Notes

1. **Affine structure:** The exponent is linear in $X$ and $v$, making the Heston model an affine jump-diffusion (without jumps).

2. **Numerical stability:** When computing $D$ for complex $u$, care must be taken with the square root branch. Typically, the square root is chosen such that $\text{Im}(D) > 0$.

3. **Decay at infinity:** As $|u| \to \infty$, the CF decays sufficiently fast, allowing Fourier inversion via FFT.

4. **Special case:** When $\rho = 0$, the stock and variance dynamics decouple, simplifying the derivation.

---

## Summary

The Heston characteristic function provides a closed-form expression for the joint distribution of log-returns and variance. Its affine structure enables efficient option pricing through Fourier methods (FFT and COS methods) and is the foundation for understanding smile dynamics and variance-of-variance effects in modern derivatives markets.

---

## Exercises

**Exercise 1.** Starting from the Heston PDE for the characteristic function, substitute the exponential-affine ansatz and collect terms independent of $v$ (giving the $C$-equation) and terms proportional to $v$ (giving the $D$-equation). Verify the resulting Riccati system.

??? success "Solution to Exercise 1"
    The Heston PDE for the characteristic function $\varphi(u, \tau; x, v) = \mathbb{E}[e^{iux_T} \mid x_t = x, v_t = v]$ (with $\tau = T - t$) is:

    $$
    \frac{\partial\varphi}{\partial\tau} = (r - q - \tfrac{1}{2}v)\frac{\partial\varphi}{\partial x} + \kappa(\theta - v)\frac{\partial\varphi}{\partial v} + \tfrac{1}{2}v\frac{\partial^2\varphi}{\partial x^2} + \rho\sigma_v v\frac{\partial^2\varphi}{\partial x\,\partial v} + \tfrac{1}{2}\sigma_v^2 v\frac{\partial^2\varphi}{\partial v^2}
    $$

    Substitute the exponential-affine ansatz $\varphi = \exp(C(\tau, u) + D(\tau, u)v + iux)$. The relevant partial derivatives are:

    $$
    \partial_\tau\varphi = (C' + D'v)\varphi, \quad \partial_x\varphi = iu\,\varphi, \quad \partial_{xx}\varphi = -u^2\varphi
    $$

    $$
    \partial_v\varphi = D\,\varphi, \quad \partial_{vv}\varphi = D^2\varphi, \quad \partial_{xv}\varphi = iu\,D\,\varphi
    $$

    Substituting and dividing by $\varphi \neq 0$:

    $$
    C' + D'v = (r-q-\tfrac{1}{2}v)(iu) + \kappa(\theta - v)D + \tfrac{1}{2}v(-u^2) + \rho\sigma_v v(iu\,D) + \tfrac{1}{2}\sigma_v^2 v\,D^2
    $$

    Collecting terms independent of $v$ (the $C$-equation):

    $$
    C' = (r-q)iu + \kappa\theta D
    $$

    Collecting terms proportional to $v$ (the $D$-equation, the Riccati ODE):

    $$
    D' = \tfrac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v iu - \kappa)D + \tfrac{1}{2}(iu - u^2)
    $$

    with initial conditions $C(0, u) = 0$, $D(0, u) = 0$. This is verified because the matching of $v^0$ and $v^1$ coefficients is exact, and the ansatz is consistent with the PDE structure.

---

**Exercise 2.** For the special case $\rho = 0$ and $\sigma_v = 0$, show that the Heston characteristic function reduces to the Black-Scholes characteristic function $\exp(iux + (iu(r-q) - \frac{1}{2}u^2 v_0)\tau)$.

??? success "Solution to Exercise 2"
    When $\rho = 0$ and $\sigma_v = 0$, the variance $v_t = v_0$ is constant (no stochastic volatility). The Riccati coefficients become:

    $$
    a = 0, \quad b = -\kappa, \quad c = \tfrac{1}{2}(iu - u^2)
    $$

    The $D$-equation reduces to $D' = -\kappa D + \frac{1}{2}(iu - u^2)$ with $D(0) = 0$. Since $a = 0$, this is a linear ODE with solution:

    $$
    D(\tau) = \frac{iu - u^2}{2\kappa}(1 - e^{-\kappa\tau})
    $$

    As $\kappa \to 0$ (no mean reversion), L'Hopital's rule gives $D(\tau) \to \frac{1}{2}(iu - u^2)\tau$.

    The $C$-equation gives $C(\tau) = (r-q)iu\tau + \kappa\theta\int_0^\tau D(s)\,ds$. With $\sigma_v = 0$, the variance is identically $v_0$, so $\kappa\theta = \kappa v_0$ (at stationarity). In the limit $\kappa \to 0$:

    $$
    C(\tau) = (r-q)iu\tau
    $$

    and $D(\tau)v_0 = \frac{1}{2}(iu - u^2)v_0\tau$.

    The characteristic function becomes:

    $$
    \varphi(u) = \exp\!\left(iux + (r-q)iu\tau + \tfrac{1}{2}(iu - u^2)v_0\tau\right)
    $$

    $$
    = \exp\!\left(iu\bigl[x + (r-q)\tau\bigr] - \tfrac{1}{2}u^2 v_0\tau\right)
    $$

    This is exactly the Black-Scholes characteristic function for $\log S_T$ with constant variance $v_0$ (i.e., constant volatility $\sigma = \sqrt{v_0}$), confirming the reduction.

---

**Exercise 3.** The Heston characteristic function enables pricing via $C = e^{-r\tau}\frac{1}{\pi}\int_0^\infty \operatorname{Re}[\cdots]\,du$. Explain why this integral converges and how the decay rate of $|\varphi(u)|$ as $u \to \infty$ affects the number of quadrature points needed.

??? success "Solution to Exercise 3"
    The Fourier inversion integral for a European call takes the form:

    $$
    C_{\text{call}} = e^{-r\tau}\frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iu\ln K}\varphi(u)}{iu}\right] du
    $$

    (or a similar expression using the Gil-Pelaez formula). The integral converges because:

    **1. Decay of $|\varphi(u)|$:** As $u \to \infty$, the characteristic function decays to zero. The exponent $C(\tau, u) + D(\tau, u)v_0$ has a real part that becomes increasingly negative. Specifically, the dominant contribution for large $u$ is the $-u^2$ term in the Riccati coefficient $c = \frac{1}{2}(iu - u^2)$, which drives $\operatorname{Re}(D) \sim -\alpha u^2$ for some $\alpha > 0$, so:

    $$
    |\varphi(u)| = \exp\!\bigl(\operatorname{Re}(C + Dv_0)\bigr) \to 0 \quad \text{as } u \to \infty
    $$

    **2. Integrand boundedness:** The factor $1/(iu)$ contributes a $1/u$ decay, and the oscillatory factor $e^{-iu\ln K}$ has modulus 1. So the integrand decays at least as fast as $|\varphi(u)|/u$.

    **3. Effect on quadrature:** The rate of decay of $|\varphi(u)|$ determines the effective truncation point $u_{\max}$ of the integral. Faster decay means fewer quadrature points are needed:

    - **High $\sigma_v$** (large vol-of-vol): the CF decays more slowly because the distribution has fatter tails, requiring more quadrature points (e.g., $u_{\max} \sim 100$)
    - **Low $\sigma_v$**: the CF decays rapidly (closer to Gaussian), and $u_{\max} \sim 30\text{--}50$ suffices
    - A practical rule of thumb is to integrate until $|\varphi(u_{\max})| < 10^{-8}$

---

**Exercise 4.** Compute $\varphi(-i, \tau; x, v)$ and show that it equals $e^{x+(r-q)\tau} = S_t e^{(r-q)\tau}$, confirming the martingale condition $\mathbb{E}[S_T/S_t] = e^{(r-q)\tau}$.

??? success "Solution to Exercise 4"
    The characteristic function at $u = -i$ gives $\varphi(-i) = \mathbb{E}[e^{i(-i)X_T}] = \mathbb{E}[e^{X_T}] = \mathbb{E}[S_T]$.

    Using the Heston CF formula, we evaluate at $u = -i$. The key intermediate quantities are:

    **Discriminant:**

    $$
    \gamma(-i) = \sqrt{(\kappa - i\rho\gamma(-i))^2 + \gamma^2(i(-i) + (-i)^2)} = \sqrt{(\kappa - \rho\gamma)^2 + \gamma^2(1 - 1)} = |\kappa - \rho\gamma|
    $$

    (Here $\gamma$ on the left is the discriminant, while $\gamma$ on the right is the vol-of-vol parameter; using the notation from the file where vol-of-vol is $\gamma$.) With $\operatorname{Re}(\kappa - \rho\gamma) > 0$, we get $\gamma(-i) = \kappa - \rho\gamma$.

    **Ratio:** $g(-i) = \frac{(\kappa - \rho\gamma) - (\kappa - \rho\gamma)}{(\kappa - \rho\gamma) + (\kappa - \rho\gamma)} = 0$.

    **$D$ function:** $D(\tau, -i) = 0$ (the numerator $\kappa - \rho\gamma - \gamma(-i) = 0$).

    **$C$ function:** With $g = 0$, the log term vanishes, and:

    $$
    C(\tau, -i) = (r-q)\cdot i(-i)\cdot\tau + 0 = (r-q)\tau
    $$

    Therefore:

    $$
    \varphi(-i) = e^{C + Dv + i(-i)x} = e^{(r-q)\tau + 0 + x} = S_t\,e^{(r-q)\tau}
    $$

    This confirms $\mathbb{E}^{\mathbb{Q}}[S_T \mid \mathcal{F}_t] = S_t\,e^{(r-q)\tau}$, the risk-neutral martingale condition for the discounted stock price (after adjusting for dividends).

---

**Exercise 5.** Explain qualitatively how each Heston parameter ($\kappa$, $\theta$, $\sigma_v$, $\rho$) affects the shape of $|\varphi(u)|$ as a function of $u$. Which parameter causes the fastest decay?

??? success "Solution to Exercise 5"
    Each Heston parameter affects $|\varphi(u)|$ as follows:

    **Mean-reversion speed $\kappa$:** Higher $\kappa$ pulls the variance toward $\theta$ more quickly, reducing the effective randomness of the integrated variance. This makes the log-return distribution closer to Gaussian, so $|\varphi(u)|$ decays more slowly (Gaussian CFs decay as $e^{-cu^2}$, which is the slowest among common distributions relative to fat-tailed distributions). However, $\kappa$ also affects the characteristic time scale $\gamma \approx \kappa$ for small $u$, and large $\kappa$ compresses the transient dynamics.

    **Long-run variance $\theta$:** Higher $\theta$ increases the total variance of log-returns, which broadens the distribution. A broader distribution means faster decay of $|\varphi(u)|$ because $\operatorname{Re}(D)v + \operatorname{Re}(C)$ becomes more negative for large $u$. The effect enters through the $C$ function, which scales with $\kappa\theta$.

    **Vol-of-vol $\sigma_v$:** This is the most important parameter for CF decay. Higher $\sigma_v$ produces heavier tails (higher excess kurtosis), which means $|\varphi(u)|$ decays more slowly. The decay rate transitions from approximately Gaussian ($e^{-cu^2}$) when $\sigma_v$ is small to a slower rate when $\sigma_v$ is large. Numerically, doubling $\sigma_v$ can increase the truncation point $u_{\max}$ by a factor of 2--4.

    **Correlation $\rho$:** Negative $\rho$ introduces asymmetry (skewness) in the distribution. While $\rho$ affects the phase of $\varphi(u)$ (causing the real and imaginary parts to oscillate differently), its effect on $|\varphi(u)|$ is secondary compared to $\sigma_v$. Extreme $|\rho|$ values slightly slow the decay because they amplify the coupling between the stock and variance processes.

    **Which parameter causes the fastest decay?** The vol-of-vol $\sigma_v$ is the dominant parameter. When $\sigma_v$ is small, the model is close to Black-Scholes and $|\varphi(u)|$ decays approximately as $\exp(-\frac{1}{2}u^2 v_0 \tau)$, which is very fast. As $\sigma_v$ increases, tail heaviness grows and the CF decay slows considerably. Therefore, **low $\sigma_v$** produces the fastest decay, and **high $\sigma_v$** produces the slowest.
