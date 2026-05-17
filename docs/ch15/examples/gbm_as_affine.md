# Geometric Brownian Motion as Affine

*This section explores geometric brownian motion in the context of affine processes. Specifically, we show that the stock price itself does not satisfy the affine property, but the log stock price does.*

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand why standard GBM is not an affine process
    2. Recognize the transformation that makes GBM affine
    3. Apply the affine framework to logarithmic stock prices
    4. Work with characteristic functions for log-normal distributions
    5. Connect this to practical financial modeling

---

## Overview

Geometric Brownian Motion is ubiquitous in finance for modeling stock prices. However, it presents an interesting case study for affine processes: the price itself fails one of the linearity conditions, but a simple logarithmic transformation renders it perfectly affine. This section develops both aspects in detail.

---

## Stock Price Dynamics

Consider the standard Black-Scholes model for a stock price $S_t$:

$$
dS_t = rS_t dt + \sigma S_t dW_t
$$

where:

- $r$ is the constant risk-free rate
- $\sigma$ is the volatility
- $W_t$ is a standard Brownian motion

This is **Geometric Brownian Motion (GBM)**.

---

## Why S_t is NOT Affine

Recall (see [affine definition](../definition_and_setup/definition_of_affine_process.md)) the linearity conditions on drift, diffusion, and short rate.

### Analysis

For the GBM process:

$$
dS_t = rS_t dt + \sigma S_t dW_t
$$

We can identify:

$$
\begin{array}{lllllll}
\displaystyle \bar{\mu}(S_t) = rS_t &\quad& \text{Linear in } S_t & \quad & \color{green}{\checkmark} \text{ Good}\\
\displaystyle \bar{\sigma}(S_t) = \sigma S_t &\Rightarrow& \bar{\sigma}(S_t)\bar{\sigma}(S_t)^T = \sigma^2 S_t^2 & \quad & \color{red}{\times} \text{ NOT Linear!}\\
\displaystyle r(S_t) = r &\quad& \text{Linear in } S_t & \quad & \color{green}{\checkmark} \text{ Good}\\
\end{array}
$$

### Conclusion

The diffusion matrix $\bar{\sigma}(S_t)\bar{\sigma}(S_t)^T = \sigma^2 S_t^2$ is **quadratic**, not linear, in $S_t$. This violates the affine property.

**Therefore, the stock price process $S_t$ is NOT affine.**

---

## Transformation: X_t = log S_t

Recall (see [Itô calculus applications](../../ch03/ito_lemma/ito_calculus_applications.md)) the derivation of $d(\log S_t)$ under GBM. The result is:

$$
dX_t = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
$$

This is arithmetic Brownian motion with drift.

---

## Why X_t = log S_t IS Affine

### Checking the Affine Conditions

For $X_t$, we have:

$$
\begin{array}{lll}
\displaystyle \bar{\mu}(X_t) = r - \frac{\sigma^2}{2} & \quad & \text{Constant (linear in } X_t\text{)}\\
\displaystyle \bar{\sigma}(X_t) = \sigma &\Rightarrow& \bar{\sigma}(X_t)\bar{\sigma}(X_t)^T = \sigma^2 & \quad & \text{Constant (linear in } X_t\text{)}\\
\displaystyle r(X_t) = r & \quad & \text{Constant (linear in } X_t\text{)}\\
\end{array}
$$

### Affine Parameters

In the standard affine form $\bar{\mu}(\mathbf{X}) = a_0 + a_1 \mathbf{X}$, we identify (for the one-dimensional case):

$$
\begin{array}{lll}
a_0 = r - \frac{\sigma^2}{2} & \Rightarrow & \text{Drift constant}\\
a_1 = 0 & \Rightarrow & \text{No linear dependence on } X_t\\
c_0 = \sigma^2 & \Rightarrow & \text{Diffusion constant}\\
c_1 = 0 & \Rightarrow & \text{No state-dependent volatility}\\
r_0 = r & \Rightarrow & \text{Short rate constant}\\
r_1 = 0 & \Rightarrow & \text{No dependence on } X_t\\
\end{array}
$$

### Conclusion

**All affine conditions are satisfied.** The log stock price $X_t$ is an affine process.

---

## Characteristic Function

Recall (see [characteristic function](../characteristic_function/characteristic_function.md)) the general exponential-affine form and the Riccati system. For the log stock price with $(a_0, a_1=0, c_0, c_1=0, r_0, r_1=0)$, the Riccati system specializes to:

$$
\begin{array}{lll}
\displaystyle \frac{dA}{d\tau} &=& -r + \left(r - \frac{\sigma^2}{2}\right)B + \frac{1}{2}\sigma^2 B^2\\
\displaystyle \frac{dB}{d\tau} &=& 0\\
\end{array}
$$

### Solution

From $\frac{dB}{d\tau} = 0$ with terminal condition $B(0) = u$:

$$B(\tau, u) = u \quad \text{(constant in } \tau\text{)}$$

Substituting into the first equation:

$$
\frac{dA}{d\tau} = -r + \left(r - \frac{\sigma^2}{2}\right)u + \frac{1}{2}\sigma^2 u^2
$$

This is a first-order linear ODE in $A$. Integrating with terminal condition $A(0) = 0$:

$$
A(\tau, u) = \left[-r + \left(r - \frac{\sigma^2}{2}\right)u + \frac{1}{2}\sigma^2 u^2\right]\tau
$$

Simplifying:

$$
A(\tau, u) = \left[\left(r - \frac{\sigma^2}{2}\right)u - r + \frac{1}{2}\sigma^2 u^2\right]\tau
$$

### Characteristic Function Result

$$
\varphi(X_t, t, T, u) = \exp\left(\left[\left(r - \frac{\sigma^2}{2}\right)u - r + \frac{1}{2}\sigma^2 u^2\right]\left(T-t\right) + iuX_t\right)
$$

### Simplification Using Standard Form

This matches the known result for log-normal distributions. Rewriting:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{iuX_T} \Big| X_t\right] = \exp\left(iu(X_t + \mu(T-t)) - \frac{1}{2}u^2\sigma^2(T-t)\right)
$$

where $\mu = r - \frac{\sigma^2}{2}$ is the drift of $X_t$. This is the characteristic function of a normal distribution with mean $X_t + \mu(T-t)$ and variance $\sigma^2(T-t)$, confirming that $X_T | X_t \sim N(X_t + \mu(T-t), \sigma^2(T-t))$.

---

## Link to Stock Price Distribution

### Recovery of Log-Normal Distribution

Since $X_T = \log S_T$ is normally distributed:

$$
X_T | X_t \sim N\left(X_t + \left(r - \frac{\sigma^2}{2}\right)(T-t), \sigma^2(T-t)\right)
$$

Taking exponentials:

$$
S_T | S_t \sim \text{Lognormal}
$$

with parameters:

$$
\log S_T = \log S_t + \left(r - \frac{\sigma^2}{2}\right)(T-t) + \sigma\sqrt{T-t} \cdot Z
$$

where $Z \sim N(0, 1)$.

This is the standard Black-Scholes result.

---

## Practical Implications

### Advantage of Affine Formulation

1. **Analytical Tractability**: The affine form enables closed-form solutions for option prices via Fourier inversion.

2. **Computational Efficiency**: No need for Monte Carlo simulation for basic pricing; use characteristic functions.

3. **Extensions**: The framework extends to multivariate models and jump-diffusions naturally.

### When Direct Pricing Suffices

For simple European options on $S_T$:

- The log-normal distribution is known analytically
- Black-Scholes formula gives closed-form prices
- No need to invoke the full affine machinery

### When Affine Framework Shines

For complex derivatives (American options, barrier options, etc.):

- The characteristic function approach becomes indispensable
- Fourier methods enable fast numerical pricing
- Multi-factor extensions become tractable

---

## Summary

| Property | Stock Price $S_t$ | Log Stock Price $X_t = \log S_t$ |
|----------|------------------|----------------------------------|
| **Dynamics** | $dS = rSdt + \sigma SdW$ | $dX = (r - \sigma^2/2)dt + \sigma dW$ |
| **Drift** | $rS$ (linear) | Constant (affine) |
| **Diffusion** | $\sigma^2 S^2$ (quadratic) | $\sigma^2$ (constant, affine) |
| **Short Rate** | $r$ (linear) | $r$ (affine) |
| **Is Affine?** | **NO** | **YES** |
| **Char. Function** | Complex | Closed-form (Gaussian) |
| **Tractability** | Needs Black-Scholes | Affine framework applies |

---

## Key Takeaways

1. **Stock price is not affine** due to quadratic diffusion matrix.

2. **Log stock price is affine** because the transformation eliminates the quadratic term.

3. **Transformation is universal**: Any process with diffusion proportional to $S^k$ (for $k \neq 0$) can be affine-ified by appropriate log or power transformation.

4. **Practical insight**: In finance, many models that aren't directly affine become affine after simple transformations—recognizing this is key to applying modern computational tools.

---

## Further Reading

- Black, F., & Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy*, 81(3), 637-654.
- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.

---

## Exercises

**Exercise 1.** Starting from $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, apply Ito's lemma to $X_t = \log S_t$ and derive the dynamics $dX_t = (r - \frac{1}{2}\sigma^2)\,dt + \sigma\,dW_t$. Identify the affine parameters $\kappa_0$, $\kappa_1$, $\sigma_0$, $\sigma_1$ for $X_t$.

??? success "Solution to Exercise 1"
    Starting from $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, let $X_t = \log S_t$. By Ito's lemma with $f(S) = \log S$:

    $$
    dX_t = f'(S_t)\,dS_t + \frac{1}{2}f''(S_t)\,(dS_t)^2
    $$

    Computing derivatives: $f'(S) = 1/S$ and $f''(S) = -1/S^2$. Substituting:

    $$
    dX_t = \frac{1}{S_t}(rS_t\,dt + \sigma S_t\,dW_t) + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)\sigma^2 S_t^2\,dt
    $$

    $$
    = r\,dt + \sigma\,dW_t - \frac{\sigma^2}{2}\,dt = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
    $$

    This is an arithmetic Brownian motion with constant drift and constant diffusion. In the affine form $dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t$, the parameters are:

    - $\kappa_0 = r - \frac{\sigma^2}{2}$ (constant drift)
    - $\kappa_1 = 0$ (no mean reversion)
    - $\sigma_0 = \sigma^2$ (constant diffusion coefficient)
    - $\sigma_1 = 0$ (no state-dependent volatility)

---

**Exercise 2.** For the log-price process $X_t = \log S_t$ under GBM, write down the Riccati system and solve for $\psi(\tau)$ and $\phi(\tau)$. Use the solution to write the characteristic function $\mathbb{E}[e^{ivX_T} \mid X_t = x]$ in closed form and verify it corresponds to a Gaussian distribution.

??? success "Solution to Exercise 2"
    The log-price $X_t$ has affine parameters $a_0 = r - \frac{\sigma^2}{2}$, $a_1 = 0$, $c_0 = \sigma^2$, $c_1 = 0$, $r_0 = r$, $r_1 = 0$. The Riccati system for the characteristic exponent $\varphi(X_t, t, T, u) = e^{\phi(\tau) + \psi(\tau) X_t}$ is:

    $$
    \psi'(\tau) = -r_1 + a_1 \psi + \frac{1}{2}c_1 \psi^2 = 0, \qquad \psi(0) = iu
    $$

    $$
    \phi'(\tau) = -r_0 + a_0 \psi + \frac{1}{2}c_0 \psi^2, \qquad \phi(0) = 0
    $$

    Since $\psi'(\tau) = 0$, we have $\psi(\tau) = iu$ for all $\tau$. Substituting into the $\phi$-equation:

    $$
    \phi'(\tau) = -r + \left(r - \frac{\sigma^2}{2}\right)(iu) + \frac{\sigma^2}{2}(iu)^2 = -r + \left(r - \frac{\sigma^2}{2}\right)iu - \frac{\sigma^2 u^2}{2}
    $$

    Integrating with $\phi(0) = 0$:

    $$
    \phi(\tau) = \left[-r + \left(r - \frac{\sigma^2}{2}\right)iu - \frac{\sigma^2 u^2}{2}\right]\tau
    $$

    The characteristic function is:

    $$
    \mathbb{E}[e^{iuX_T} \mid X_t = x] = \exp\!\left(iux + \left(r - \frac{\sigma^2}{2}\right)iu\tau - \frac{\sigma^2 u^2}{2}\tau\right)
    $$

    This is $\exp(iu\,m - \frac{1}{2}u^2 s^2)$ with $m = x + (r - \frac{\sigma^2}{2})\tau$ and $s^2 = \sigma^2 \tau$, which is the characteristic function of $N(m, s^2)$. Therefore $X_T \mid X_t = x$ follows a Gaussian distribution with mean $x + (r - \frac{\sigma^2}{2})(T-t)$ and variance $\sigma^2(T-t)$.

---

**Exercise 3.** The stock price $S_t$ has drift $\mu(S) = rS$ and diffusion coefficient $a(S) = \sigma^2 S^2$. Show that $a(S)$ is quadratic (not linear) in $S$, which is the precise reason $S_t$ fails the affine diffusion condition $a(S) = c_0 + c_1 S$.

??? success "Solution to Exercise 3"
    The drift coefficient is $\mu(S) = rS$, which is linear in $S$ (affine with $a_0 = 0$, $a_1 = r$). The diffusion coefficient is $a(S) = \sigma^2 S^2$. For the affine condition, we need $a(S) = c_0 + c_1 S$ for constants $c_0$ and $c_1$. However:

    $$
    a(S) = \sigma^2 S^2
    $$

    This is a polynomial of degree 2 in $S$. A linear (affine) function $c_0 + c_1 S$ is a polynomial of degree at most 1. Since $\sigma^2 \neq 0$, the coefficient of $S^2$ is nonzero, so no choice of $c_0, c_1$ satisfies $\sigma^2 S^2 = c_0 + c_1 S$ for all $S \geq 0$.

    Concretely, if we try to match at three points:

    - At $S = 0$: $0 = c_0$, so $c_0 = 0$
    - At $S = 1$: $\sigma^2 = c_1$
    - At $S = 2$: $4\sigma^2 = 2c_1 = 2\sigma^2$, which fails

    This confirms that the quadratic dependence $a(S) = \sigma^2 S^2$ cannot be expressed as an affine function of $S$, and therefore $S_t$ fails the affine diffusion condition.

---

**Exercise 4.** Using the characteristic function of $X_T = \log S_T$ under GBM, compute the discounted characteristic function $\mathbb{E}[e^{-r\tau + ivX_T} \mid X_t = x]$ and verify that setting $v = -i$ recovers the forward price $S_t$ (i.e., the discounted stock price is a martingale).

??? success "Solution to Exercise 4"
    The discounted characteristic function is:

    $$
    \Phi(\tau, v) = \mathbb{E}[e^{-r\tau + ivX_T} \mid X_t = x]
    $$

    From the characteristic function derived in the text:

    $$
    \Phi(\tau, v) = \exp\!\left(-r\tau + ivx + \left(r - \frac{\sigma^2}{2}\right)iv\tau - \frac{\sigma^2 v^2}{2}\tau\right)
    $$

    Setting $v = -i$ (so $iv = -i \cdot i = 1$):

    $$
    \Phi(\tau, -i) = \exp\!\left(-r\tau + x + \left(r - \frac{\sigma^2}{2}\right)\tau - \frac{\sigma^2(-i)^2}{2}\tau\right)
    $$

    Since $(-i)^2 = -1$:

    $$
    = \exp\!\left(-r\tau + x + r\tau - \frac{\sigma^2}{2}\tau + \frac{\sigma^2}{2}\tau\right) = e^x
    $$

    But $e^x = e^{\log S_t} = S_t$, so:

    $$
    \mathbb{E}[e^{-r\tau + X_T} \mid X_t = x] = \mathbb{E}[e^{-r\tau} S_T \mid S_t] = S_t
    $$

    This confirms that $e^{-rt}S_t$ is a martingale under $\mathbb{Q}$, i.e., $\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}S_T \mid \mathcal{F}_t] = S_t$, which is exactly the forward price relationship for the discounted stock price.

---

**Exercise 5.** Consider a process $Y_t = S_t^2$. Apply Ito's lemma to derive $dY_t$ and check whether $Y_t$ is an affine process. If not, identify which affine condition fails.

??? success "Solution to Exercise 5"
    Let $Y_t = S_t^2$ where $dS_t = rS_t\,dt + \sigma S_t\,dW_t$. By Ito's lemma with $f(S) = S^2$:

    $$
    dY_t = 2S_t\,dS_t + \frac{1}{2}\cdot 2\,(dS_t)^2
    $$

    $$
    = 2S_t(rS_t\,dt + \sigma S_t\,dW_t) + \sigma^2 S_t^2\,dt
    $$

    $$
    = (2r + \sigma^2)S_t^2\,dt + 2\sigma S_t^2\,dW_t
    $$

    Since $S_t^2 = Y_t$:

    $$
    dY_t = (2r + \sigma^2)Y_t\,dt + 2\sigma Y_t\,dW_t
    $$

    Checking the affine conditions:

    - **Drift**: $\mu(Y) = (2r + \sigma^2)Y$ is linear in $Y$. This is affine.
    - **Diffusion**: $a(Y) = (2\sigma Y)^2 = 4\sigma^2 Y^2$ is quadratic in $Y$. This is **not** affine.

    The diffusion coefficient $a(Y) = 4\sigma^2 Y^2$ fails the affine condition $a(Y) = c_0 + c_1 Y$. This is the same quadratic problem as for $S_t$ itself. $Y_t = S_t^2$ is **not** an affine process.

    Note that this is expected: $Y_t$ is also a geometric Brownian motion (with drift $2r + \sigma^2$ and volatility $2\sigma$), and GBM is never affine in the level, only in the log.

---

**Exercise 6.** The Black-Scholes call price can be recovered from the characteristic function via Fourier inversion. Starting from the discounted characteristic function of the log-price under GBM, outline the steps of the Gil-Pelaez inversion formula to compute $\mathbb{P}(S_T > K)$ and verify that the result involves the standard normal CDF $N(d_2)$.

??? success "Solution to Exercise 6"
    The Gil-Pelaez inversion formula for a CDF from a characteristic function states:

    $$
    \mathbb{P}(X_T > k) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left(\frac{e^{-ivk}\varphi_{X_T}(v)}{iv}\right)dv
    $$

    where $k = \log K$ and $\varphi_{X_T}(v) = \mathbb{E}[e^{ivX_T}]$ is the characteristic function of the log-price.

    **Step 1.** Under GBM, $X_T = \log S_T \sim N(m, s^2)$ with $m = \log S_t + (r - \frac{\sigma^2}{2})\tau$ and $s^2 = \sigma^2 \tau$.

    **Step 2.** The characteristic function is $\varphi_{X_T}(v) = \exp(ivm - \frac{1}{2}v^2 s^2)$.

    **Step 3.** Substituting into the Gil-Pelaez formula:

    $$
    \mathbb{P}(X_T > k) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left(\frac{e^{iv(m - k) - \frac{1}{2}v^2 s^2}}{iv}\right)dv
    $$

    **Step 4.** For a Gaussian random variable $Z \sim N(m, s^2)$, the integral evaluates to:

    $$
    \mathbb{P}(Z > k) = N\!\left(\frac{m - k}{s}\right)
    $$

    **Step 5.** Substituting $k = \log K$, $m = \log S_t + (r - \frac{\sigma^2}{2})\tau$, and $s = \sigma\sqrt{\tau}$:

    $$
    \mathbb{P}(S_T > K) = \mathbb{P}(X_T > \log K) = N\!\left(\frac{\log(S_t/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}\right) = N(d_2)
    $$

    where $d_2 = \frac{\log(S_t/K) + (r - \frac{\sigma^2}{2})(T-t)}{\sigma\sqrt{T-t}}$ is the standard Black-Scholes quantity. This confirms that the Fourier inversion of the GBM characteristic function recovers the Black-Scholes $N(d_2)$ for the exercise probability under the risk-neutral measure.
