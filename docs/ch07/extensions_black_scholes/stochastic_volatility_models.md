# Stochastic Volatility Models

Stochastic volatility models introduce a **second random factor** to capture the empirical observation that volatility itself fluctuates randomly over time. This creates volatility smile/skew, term structure effects, and volatility clustering.

---

### Motivation

#### Empirical Evidence

1. **Volatility clustering**: High volatility tends to follow high volatility
2. **Mean reversion**: Volatility reverts to a long-term average
3. **Leverage effect**: Negative correlation between returns and volatility
4. **Fat tails**: Return distributions have heavier tails than normal
5. **Smile persistence**: The volatility smile persists over time

#### Limitations of Local Volatility

Local volatility models fit the smile but predict it will flatten—contrary to market behavior. Stochastic volatility produces more realistic dynamics.

---

### General Framework

#### Two-Factor Model

Under the risk-neutral measure $\mathbb{Q}$:

$$
\boxed{
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \alpha(t, v_t)\,dt + \beta(t, v_t)\,dW_t^{(2)} \\
d\langle W^{(1)}, W^{(2)}\rangle_t &= \rho\,dt
\end{aligned}
}
$$

where:
- $v_t$ is the **instantaneous variance** (or volatility squared)
- $\alpha(t, v)$ is the variance drift
- $\beta(t, v)$ is the **vol-of-vol** (volatility of volatility)
- $\rho$ is the correlation (typically negative for equities)

#### The Leverage Effect

When $\rho < 0$:
- Stock falls → volatility rises
- Creates negative skew in the smile
- Observed empirically: $\rho \approx -0.7$ for equity indices

---

### The Heston Model

#### Model Specification

$$
\boxed{
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
}
$$

**Parameters**:
- $\kappa > 0$: Speed of mean reversion
- $\theta > 0$: Long-term variance level
- $\xi > 0$: Vol-of-vol
- $\rho \in [-1, 1]$: Correlation
- $v_0$: Initial variance

#### Feller Condition

To ensure $v_t > 0$ (variance stays positive):

$$
\boxed{
2\kappa\theta \geq \xi^2
}
$$

If violated, variance can hit zero (but is reflected).

#### Affine Structure

Heston is an **affine** model: the characteristic function has exponential-affine form, enabling semi-analytical pricing via Fourier methods.

---

### Pricing in Stochastic Volatility

#### The 2D PDE

For option price $V(t, S, v)$:

$$
\boxed{
\frac{\partial V}{\partial t} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi vS\frac{\partial^2 V}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + rS\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} - rV = 0
}
$$

**Note**: The mixed derivative $\partial_{Sv}$ term arises from correlation.

#### Characteristic Function Method

For Heston, the log-price characteristic function is:

$$
\phi(u) = \mathbb{E}^{\mathbb{Q}}[e^{iu\log S_T} | S_t, v_t] = e^{C(T-t, u) + D(T-t, u)v_t + iu\log S_t}
$$

where $C$ and $D$ satisfy Riccati ODEs with known solutions.

#### Fourier Pricing

European call prices via inverse Fourier transform:

$$
C(K) = S_0 - \frac{Ke^{-rT}}{\pi}\int_0^\infty \text{Re}\left[\frac{e^{-iu\log K}\phi(u-i)}{iu}\right]du
$$

**Advantages**: Fast and accurate for vanilla options.

---

### Calibration

#### Parameters to Calibrate

| Parameter | Effect |
|-----------|--------|
| $v_0$ | Current ATM volatility level |
| $\theta$ | Long-term volatility level |
| $\kappa$ | Term structure shape |
| $\xi$ | Smile convexity (vol-of-vol) |
| $\rho$ | Smile skew |

#### Typical Procedure

1. Fix $v_0$ from ATM short-term options
2. Calibrate $\rho$ and $\xi$ from smile shape
3. Calibrate $\kappa$ and $\theta$ from term structure
4. Refine jointly via optimization

#### Identifiability Issues

- $\kappa$ and $\theta$ are often difficult to separate
- Multiple parameter sets can produce similar fits
- Regularization may be needed

---

### Incomplete Markets

#### The Problem

Two sources of randomness ($W^{(1)}$, $W^{(2)}$) but only one traded asset ($S$).

#### Implications

1. **Non-unique risk-neutral measure**: Volatility risk premium is not determined by no-arbitrage
2. **Imperfect hedging**: Cannot replicate arbitrary payoffs
3. **Model calibration determines $\mathbb{Q}$**: Not derived from $\mathbb{P}$

#### The Volatility Risk Premium

Under $\mathbb{P}$, variance drift may differ:

$$
dv_t = [\kappa(\theta - v_t) - \lambda(t, v_t)]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{P}}
$$

where $\lambda$ is the volatility risk premium (typically negative—investors pay for volatility protection).

---

### Other Stochastic Volatility Models

#### SABR Model

Popular for interest rate and FX options:

$$
\begin{aligned}
dF_t &= \sigma_t F_t^\beta\,dW_t^{(1)} \\
d\sigma_t &= \alpha\sigma_t\,dW_t^{(2)}
\end{aligned}
$$

**Asymptotic formula** for implied volatility (Hagan et al.):

$$
\sigma_{\text{imp}}(K) \approx \frac{\alpha}{(FK)^{(1-\beta)/2}}\left[1 + \frac{(1-\beta)^2}{24}\log^2\frac{F}{K} + \cdots\right] \times \frac{z}{x(z)}
$$

#### Hull-White Model

$$
dv_t = \mu v_t\,dt + \xi v_t\,dW_t^{(2)}
$$

Log-normal variance process.

#### 3/2 Model

$$
dv_t = \kappa v_t(\theta - v_t)\,dt + \xi v_t^{3/2}\,dW_t^{(2)}
$$

Higher vol-of-vol at high variance levels.

---

### Comparison: Local vs Stochastic Volatility

| Aspect | Local Volatility | Stochastic Volatility |
|--------|-----------------|----------------------|
| Factors | 1 | 2 |
| Market | Complete | Incomplete |
| Smile fit | Exact | Approximate |
| Forward smile | Flattens | Persists |
| Calibration | Unstable | More stable |
| Hedging | Poor | Better |
| Exotic pricing | Problematic | More reliable |

---

### Numerical Methods

#### Monte Carlo

```python
# Euler discretization for Heston
for i in range(N):
    dW1 = sqrt(dt) * randn()
    dW2 = rho * dW1 + sqrt(1 - rho**2) * sqrt(dt) * randn()
    
    v[i+1] = max(v[i] + kappa*(theta - v[i])*dt + xi*sqrt(v[i])*dW2, 0)
    S[i+1] = S[i] * exp((r - 0.5*v[i])*dt + sqrt(v[i])*dW1)
```

**Note**: Need to handle $v_t < 0$ (truncation, reflection, or better schemes).

#### PDE Methods

- ADI (Alternating Direction Implicit) for 2D PDE
- Finite differences on $(S, v)$ grid
- Careful boundary conditions at $v = 0$ and $v \to \infty$

---

### Summary

$$
\boxed{
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
}
$$

| Feature | Description |
|---------|-------------|
| **Key innovation** | Variance is a random process |
| **Smile generation** | Correlation $\rho$ creates skew |
| **Term structure** | Mean reversion $\kappa$ shapes it |
| **Market completeness** | Incomplete (2 factors, 1 asset) |
| **Pricing** | Fourier methods or 2D PDE |

**Stochastic volatility models capture realistic smile dynamics at the cost of market incompleteness, leading to more reliable exotic pricing and hedging than local volatility.**

---

## Exercises

**Exercise 1.** In the Heston model, the variance process $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$ is a CIR process. (a) Verify the Feller condition $2\kappa\theta \geq \xi^2$ for the parameter set $\kappa = 2$, $\theta = 0.04$, $\xi = 0.3$. (b) When the Feller condition is violated, what happens to the variance process at $v = 0$? (c) Compute the long-run mean and variance of $v_t$ in terms of $\kappa$, $\theta$, and $\xi$.

---

**Exercise 2.** The Heston PDE for option price $V(t, S, v)$ contains a mixed derivative term $\rho\xi v S \frac{\partial^2 V}{\partial S \partial v}$. (a) Explain the financial origin of this term in terms of the correlation between stock and volatility shocks. (b) Why does this term vanish when $\rho = 0$? (c) Describe the computational challenge this mixed derivative introduces for finite difference methods and how ADI (Alternating Direction Implicit) schemes address it.

---

**Exercise 3.** The Heston model has five parameters: $v_0, \kappa, \theta, \xi, \rho$. Describe the effect of each parameter on the implied volatility surface. Specifically: (a) Which parameter controls the ATM volatility level? (b) Which parameter controls the skew? (c) Which parameter controls the smile convexity (curvature)? (d) Which parameters determine the term structure?

---

**Exercise 4.** Explain why stochastic volatility models lead to incomplete markets. Specifically, identify the two sources of randomness and the single traded asset. What is the volatility risk premium $\lambda(t, v_t)$, and why is it not determined by no-arbitrage alone? Describe how calibration to option prices implicitly selects a specific risk-neutral measure.

---

**Exercise 5.** Compare local volatility and stochastic volatility models by filling in a comparison table covering: (a) number of risk factors, (b) market completeness, (c) quality of smile fit, (d) forward smile behavior, (e) calibration stability, and (f) hedging performance. Explain why the forward smile behavior is a critical distinguishing factor for pricing exotic options.

---

**Exercise 6.** Write pseudocode for an Euler discretization of the Heston model. Generate correlated Brownian increments $dW_1$ and $dW_2$ from independent standard normals. Discuss the issue of negative variance and compare the truncation scheme $v_{i+1} = \max(v_{i+1}, 0)$ with the reflection scheme $v_{i+1} = |v_{i+1}|$. Which scheme introduces less bias?
