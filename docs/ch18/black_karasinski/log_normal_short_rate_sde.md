# Log-Normal Short Rate SDE

The Black-Karasinski (BK) model, introduced by Fischer Black and Piotr Karasinski in 1991, specifies the dynamics of the logarithm of the short rate rather than the short rate itself. This seemingly small modeling choice has profound consequences: rates are guaranteed to be positive (since the exponential of any real number is positive), the model can fit the initial term structure exactly through a time-dependent drift, and the resulting rate distribution is log-normal rather than normal. However, these advantages come at the cost of analytical tractability --- the BK model is not affine, and no closed-form bond price formula exists. This section defines the BK SDE, derives the short rate dynamics via Ito's lemma, characterizes the conditional distribution, and compares the structure with Vasicek and Hull-White.

---

## The Black-Karasinski SDE

The BK model specifies the risk-neutral dynamics of $x_t = \ln r_t$ as a mean-reverting Ornstein-Uhlenbeck process with time-dependent coefficients:

$$
dx_t = \left[\theta(t) - a(t)\,x_t\right]dt + \sigma(t)\,dW_t^{\mathbb{Q}}
$$

where:

- $x_t = \ln r_t$ is the log short rate
- $\theta(t)$ is the time-dependent drift function, calibrated to fit the initial term structure
- $a(t) > 0$ is the speed of mean reversion (may be time-dependent or constant)
- $\sigma(t) > 0$ is the volatility of the log rate
- $W_t^{\mathbb{Q}}$ is a standard Brownian motion under the risk-neutral measure

In the constant-parameter version (most common in practice), $a(t) = a$ and $\sigma(t) = \sigma$ are constants, while $\theta(t)$ remains time-dependent for term structure fitting:

$$
dx_t = \left[\theta(t) - a\,x_t\right]dt + \sigma\,dW_t^{\mathbb{Q}}
$$

The short rate is recovered by $r_t = e^{x_t}$.

!!! note "Notation comparison"
    Some references write the BK SDE as $d(\ln r_t) = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$, which is identical. The log-rate formulation emphasizes that $\ln r_t$ is the fundamental state variable, while $r_t$ is derived from it.

---

## Derivation of the short rate dynamics

To understand the dynamics of $r_t = e^{x_t}$, apply Ito's lemma to the function $r = e^x$:

$$
dr_t = e^{x_t}\,dx_t + \frac{1}{2}e^{x_t}(dx_t)^2
$$

Since $(dx_t)^2 = \sigma^2\,dt$:

$$
dr_t = r_t\left[\theta(t) - a\,\ln r_t + \frac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t^{\mathbb{Q}}
$$

This reveals several important features:

1. **Multiplicative noise**: The diffusion coefficient is $\sigma r_t$, making the volatility proportional to the level. This is the same multiplicative structure as geometric Brownian motion.

2. **State-dependent drift**: The drift contains $\ln r_t$, which is nonlinear in $r_t$. This nonlinearity is the source of the non-affine structure.

3. **Guaranteed positivity**: Since $r_t = e^{x_t}$ and $x_t$ can take any real value, $r_t > 0$ always. No boundary conditions or Feller-type conditions are needed.

---

## Conditional distribution of the log rate

Since $x_t = \ln r_t$ follows a linear (Ornstein-Uhlenbeck) SDE, its conditional distribution is Gaussian. Given $x_s$ at time $s < t$, with constant parameters $a$ and $\sigma$:

$$
x_t \mid x_s \sim \mathcal{N}\!\left(\mu(s,t),\;\nu^2(s,t)\right)
$$

where the conditional mean and variance are

$$
\mu(s,t) = x_s\,e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du
$$

$$
\nu^2(s,t) = \frac{\sigma^2}{2a}\left(1 - e^{-2a(t-s)}\right)
$$

The short rate $r_t = e^{x_t}$ is therefore **log-normally distributed** conditional on $\mathcal{F}_s$:

$$
r_t \mid r_s \sim \text{LogNormal}\!\left(\mu(s,t),\;\nu^2(s,t)\right)
$$

with conditional moments

$$
\mathbb{E}[r_t\,|\,r_s] = \exp\!\left(\mu(s,t) + \frac{\nu^2(s,t)}{2}\right)
$$

$$
\text{Var}(r_t\,|\,r_s) = \exp\!\left(2\mu(s,t) + \nu^2(s,t)\right)\left(e^{\nu^2(s,t)} - 1\right)
$$

!!! tip "Log-normal vs normal rates"
    The log-normal distribution assigns zero probability to negative rates (desirable) but has a heavier right tail than the normal distribution. Empirically, interest rate distributions often exhibit right skewness, making the log-normal assumption a reasonable first approximation, especially for emerging market rates or during periods of high rates.

---

## Long-run behavior

With constant parameters, the long-run distribution of $x_t$ as $t \to \infty$ is

$$
x_\infty \sim \mathcal{N}\!\left(\frac{\theta}{a},\;\frac{\sigma^2}{2a}\right)
$$

where we have assumed $\theta(t) = \theta$ is constant for this analysis. The long-run short rate distribution is therefore

$$
r_\infty \sim \text{LogNormal}\!\left(\frac{\theta}{a},\;\frac{\sigma^2}{2a}\right)
$$

with long-run mean

$$
\mathbb{E}[r_\infty] = \exp\!\left(\frac{\theta}{a} + \frac{\sigma^2}{4a}\right)
$$

The long-run mean rate increases with volatility (through the $\sigma^2/4a$ correction), reflecting the Jensen's inequality effect inherent in the exponential transformation.

---

## Comparison with other short-rate models

| Feature | Vasicek | Hull-White | CIR | Black-Karasinski |
|---------|---------|------------|-----|------------------|
| **SDE variable** | $r_t$ | $r_t$ | $r_t$ | $\ln r_t$ |
| **Drift** | $\kappa(\theta - r)$ | $\theta(t) - ar$ | $\kappa(\theta - r)$ | $\theta(t) - a\ln r$ |
| **Diffusion** | $\sigma$ | $\sigma$ | $\sigma\sqrt{r}$ | $\sigma r$ (for $r_t$) |
| **Rate distribution** | Normal | Normal | Non-central $\chi^2$ | Log-normal |
| **Negative rates** | Possible | Possible | No (Feller) | Impossible |
| **Affine** | Yes | Yes | Yes | No |
| **Closed-form ZCB** | Yes | Yes | Yes | No |
| **Exact term structure fit** | No | Yes | No | Yes |

The BK model occupies a unique position: it guarantees positive rates (like CIR) and fits the initial term structure exactly (like Hull-White), but sacrifices analytical tractability (unlike all three competitors).

---

## The role of the time-dependent drift

The function $\theta(t)$ is chosen so that the model reproduces the observed initial term structure of interest rates. Given market discount factors $P^{\text{mkt}}(0,T)$, the condition

$$
P^{\text{mkt}}(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_0^T r_s\,ds\right)\right]
$$

implicitly determines $\theta(t)$. Unlike the Hull-White model where $\theta(t)$ can be solved in closed form, the BK model requires a numerical procedure --- typically a trinomial tree or forward-induction algorithm --- to extract $\theta(t)$ from market data.

---

## Summary

The Black-Karasinski model specifies the log short rate $x_t = \ln r_t$ as a mean-reverting process $dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t$, making $r_t = e^{x_t}$ strictly positive and log-normally distributed. Ito's lemma reveals that the short rate dynamics $dr_t = r_t[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2]\,dt + \sigma r_t\,dW_t$ have a nonlinear drift ($\ln r$ term), which destroys the affine structure and prevents closed-form bond pricing. The time-dependent drift $\theta(t)$ enables exact calibration to the initial term structure, compensating for the loss of analytical tractability. The conditional log-normal distribution of $r_t$ guarantees non-negative rates, making the BK model particularly suitable for environments where negative rates are economically unreasonable.
