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

## Why $S_t$ is NOT Affine

### Checking the Affine Conditions

For $S_t$ to be affine, we need:

$$
\begin{array}{lll}
\displaystyle \bar{\mu}(S_t) = a_0 + a_1 S_t & \quad & \text{(Drift linear in } S_t\text{)}\\
\displaystyle \bar{\sigma}(S_t)\bar{\sigma}(S_t)^T = c_0 + c_1^T S_t & \quad & \text{(Diffusion linear in } S_t\text{)}\\
\displaystyle r(S_t) = r_0 + r_1^T S_t & \quad & \text{(Short rate linear in } S_t\text{)}\\
\end{array}
$$

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

## Transformation: $X_t = \log S_t$

### Applying Itô's Lemma

Let $X_t = \log S_t$. By Itô's lemma:

$$
dX_t = \frac{\partial X_t}{\partial S_t} dS_t + \frac{1}{2}\frac{\partial^2 X_t}{\partial S_t^2} (dS_t)^2
$$

Computing derivatives:

$$
\frac{\partial X_t}{\partial S_t} = \frac{1}{S_t}, \quad \frac{\partial^2 X_t}{\partial S_t^2} = -\frac{1}{S_t^2}
$$

The quadratic variation is:

$$(dS_t)^2 = (\sigma S_t dW_t)^2 = \sigma^2 S_t^2 dt$$

Substituting:

$$
dX_t = \frac{1}{S_t}(rS_t dt + \sigma S_t dW_t) - \frac{1}{2}\frac{1}{S_t^2}(\sigma^2 S_t^2 dt)
$$

$$
= \left(r - \frac{\sigma^2}{2}\right)dt + \sigma dW_t
$$

### Result

The log stock price follows:

$$
dX_t = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma dW_t
$$

This is a simple arithmetic Brownian motion with drift.

---

## Why $X_t = \log S_t$ IS Affine

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

### General Affine Characteristic Function

For an affine process:

$$
\varphi(\mathbf{X}_t, t, T, \mathbf{u}) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r(\mathbf{X}_s)ds} e^{i\mathbf{u}^T \mathbf{X}_T} \Big| \mathcal{F}_t\right] = e^{A(\tau, \mathbf{u}) + \mathbf{B}^T(\tau, \mathbf{u})\mathbf{X}_t}
$$

### Riccati Equations for Our Case

For the log stock price with parameters $(a_0, a_1=0, c_0, c_1=0, r_0, r_1=0)$:

$$
\begin{array}{lll}
\displaystyle \frac{dA}{d\tau} &=& -r_0 + \mathbf{B}^T a_0 + \frac{1}{2}\mathbf{B}^T c_0 \mathbf{B}\\
\displaystyle \frac{dB}{d\tau} &=& -r_1 + a_1^T \mathbf{B} + \frac{1}{2}c_1^T \mathbf{B} \mathbf{B}\\
\end{array}
$$

Substituting our parameters:

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
\varphi(X_t, t, T, u) = \exp\left(\left[\left(r - \frac{\sigma^2}{2}\right)u - r + \frac{1}{2}\sigma^2 u^2\right](T-t) + iuX_t\right)
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
- Filipović, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.
