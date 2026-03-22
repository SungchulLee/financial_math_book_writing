# Log-Stock Price Moments via Characteristic Function

The characteristic function encodes the entire distribution of $\log S_T$ in a single complex-valued function. Differentiating it at the origin extracts every moment of the distribution without ever recovering the density itself. For the Heston model, these derivatives yield closed-form expressions for the mean, variance, skewness, and kurtosis of log-returns, providing essential diagnostics for understanding how stochastic volatility reshapes the return distribution relative to the Black-Scholes lognormal benchmark.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the general moment-extraction formula from the characteristic function
    2. Compute the mean, variance, skewness, and kurtosis of $\log S_T$ under the Heston model
    3. Interpret how each Heston parameter influences the shape of the return distribution
    4. Verify moment formulas numerically against Monte Carlo simulation

---

## Intuition

In the Black-Scholes world, $\log S_T$ is normally distributed, so its skewness is zero and its excess kurtosis is zero. Real equity return distributions exhibit negative skewness (large downward moves are more likely than large upward moves) and positive excess kurtosis (fat tails). The Heston model generates both features through the interplay of stochastic variance and the correlation parameter $\rho$.

Rather than integrating the density $f(x)$ against powers of $x$ to compute moments, one can differentiate the characteristic function $\varphi(u) = \mathbb{E}[e^{iu X}]$ at $u = 0$. This avoids density recovery entirely and produces exact, closed-form moment expressions when $\varphi$ is available analytically.

---

## General Moment-Extraction Formula

Let $X = \log S_T$ and let $\varphi(u) = \mathbb{E}[e^{iuX}]$ denote its characteristic function. The $n$-th raw moment is obtained by differentiation.

!!! info "Theorem (Moments from the Characteristic Function)"
    If $\mathbb{E}[|X|^n] < \infty$, then $\varphi$ is $n$-times differentiable at $u = 0$ and

    $$
    \mathbb{E}[X^n] = (-i)^n \left.\frac{d^n \varphi}{du^n}\right|_{u=0}
    $$

**Proof.** By definition, $\varphi(u) = \mathbb{E}[e^{iuX}]$. When $\mathbb{E}[|X|^n] < \infty$, differentiation under the expectation is justified by dominated convergence, since $|\partial_u^n e^{iuX}| = |X|^n$. Then

$$
\frac{d^n \varphi}{du^n}(u) = \mathbb{E}\left[(iX)^n e^{iuX}\right]
$$

Evaluating at $u = 0$ gives $\varphi^{(n)}(0) = i^n \mathbb{E}[X^n]$, so $\mathbb{E}[X^n] = (-i)^n \varphi^{(n)}(0)$. $\square$

The central moments and cumulants follow from the **cumulant-generating function** $\psi(u) = \log \varphi(u)$, whose derivatives at $u = 0$ give the cumulants directly.

!!! info "Definition (Cumulants)"
    The $n$-th cumulant $\kappa_n$ of $X$ is defined by

    $$
    \kappa_n = (-i)^n \left.\frac{d^n}{du^n} \log \varphi(u)\right|_{u=0}
    $$

    The first four cumulants relate to standard distributional measures:

    - $\kappa_1 = \mathbb{E}[X]$ (mean)
    - $\kappa_2 = \text{Var}(X)$ (variance)
    - $\kappa_3 = \mathbb{E}[(X - \kappa_1)^3]$ (third central moment)
    - $\kappa_4 = \mathbb{E}[(X - \kappa_1)^4] - 3\kappa_2^2$ (excess kurtosis contribution)

---

## Heston Characteristic Function Recap

Under the risk-neutral measure $\mathbb{Q}$, the Heston model specifies

$$
dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

with $d\langle W^{(1)}, W^{(2)} \rangle_t = \rho \, dt$. The characteristic function of $X_T = \log S_T$ conditional on $(\log S_t, v_t)$ is

$$
\varphi(u) = \exp\bigl(C(\tau, u) + D(\tau, u) \, v_t + iu \log S_t\bigr)
$$

where $\tau = T - t$, and the functions $C(\tau, u)$ and $D(\tau, u)$ satisfy the Riccati system

$$
D(\tau, u) = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma \tau}}{1 - g \, e^{-\gamma \tau}}
$$

$$
C(\tau, u) = (r - q) i u \tau + \frac{\kappa \theta}{\xi^2} \left[(\kappa - i\rho\xi u - \gamma)\tau - 2 \log\!\left(\frac{1 - g \, e^{-\gamma \tau}}{1 - g}\right)\right]
$$

with

$$
\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}, \qquad g = \frac{\kappa - i\rho\xi u - \gamma}{\kappa - i\rho\xi u + \gamma}
$$

---

## First Moment: Mean of Log-Returns

To compute $\mathbb{E}[\log S_T]$, differentiate $\log \varphi(u)$ with respect to $u$ and evaluate at $u = 0$. Since $\log \varphi(u) = C(\tau, u) + D(\tau, u) v_t + iu \log S_t$, we need

$$
\kappa_1 = -i \left.\frac{d}{du}\left[C(\tau, u) + D(\tau, u) v_t + iu \log S_t\right]\right|_{u=0}
$$

At $u = 0$: $\gamma|_{u=0} = \kappa$, $g|_{u=0} = 0$, $D(\tau, 0) = 0$, and $C(\tau, 0) = 0$. Computing the derivatives carefully:

$$
\left.\frac{dC}{du}\right|_{u=0} = i(r-q)\tau, \qquad \left.\frac{dD}{du}\right|_{u=0} = 0
$$

!!! info "Proposition (Mean of Log-Stock Price)"
    Under the Heston model, the conditional mean of $\log S_T$ given $\mathcal{F}_t$ is

    $$
    \mathbb{E}[\log S_T \,|\, \mathcal{F}_t] = \log S_t + (r - q)\tau - \frac{1}{2}\left[\theta \tau + (v_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}\right]
    $$

The term in brackets is $\mathbb{E}\!\left[\int_t^T v_s \, ds \,\big|\, v_t\right]$, the expected integrated variance. This confirms the standard drift-adjustment: the log-stock price drifts at rate $r - q$ minus half the expected integrated variance, exactly analogous to the Black-Scholes formula with $\sigma^2$ replaced by the path-averaged variance.

---

## Second Moment: Variance of Log-Returns

The variance of $\log S_T$ captures how uncertainty in future returns depends on both the current variance level $v_t$ and the parameters governing variance dynamics.

!!! info "Proposition (Variance of Log-Stock Price)"
    Under the Heston model, the conditional variance of $\log S_T$ given $\mathcal{F}_t$ is

    $$
    \text{Var}(\log S_T \,|\, \mathcal{F}_t) = \theta \tau + (v_t - \theta) \frac{1 - e^{-\kappa\tau}}{\kappa} + \frac{\xi^2}{2\kappa^2}\left[\theta\tau - 2\theta\frac{1-e^{-\kappa\tau}}{\kappa} + \theta\frac{1-e^{-2\kappa\tau}}{2\kappa}\right]
    $$

    $$
    {} + \frac{\xi^2}{2\kappa^2}(v_t - \theta)\left[\frac{1-e^{-\kappa\tau}}{\kappa} - \frac{1-e^{-2\kappa\tau}}{2\kappa}\right] + \frac{2\rho\xi}{\kappa}\left[\theta\tau - \theta\frac{1-e^{-\kappa\tau}}{\kappa} + (v_t - \theta)\frac{1-e^{-\kappa\tau}}{\kappa}\right]
    $$

    $$
    {} - \frac{2\rho\xi}{\kappa}\left[\theta\frac{1-e^{-\kappa\tau}}{\kappa} + (v_t-\theta)\frac{1-e^{-2\kappa\tau}}{2\kappa}\right]
    $$

**Derivation sketch.** The variance arises from the second cumulant $\kappa_2 = -\varphi''(0)/\varphi(0) + (\varphi'(0)/\varphi(0))^2$, which requires computing $d^2C/du^2|_{u=0}$ and $d^2D/du^2|_{u=0}$. The correlation $\rho$ enters through the cross-term between the stock Brownian motion and the variance Brownian motion, producing the $\rho\xi$ terms that are absent in the Black-Scholes case. $\square$

In the limit $\xi \to 0$ (deterministic volatility), the variance reduces to $v_t \tau$ (constant variance), recovering the Black-Scholes result.

---

## Third and Fourth Cumulants: Skewness and Kurtosis

The skewness and excess kurtosis of $\log S_T$ quantify how the Heston distribution departs from normality. These are computed from the third and fourth cumulants.

!!! info "Definition (Skewness and Excess Kurtosis)"
    The skewness and excess kurtosis of $\log S_T$ are

    $$
    \text{Skew}(\log S_T) = \frac{\kappa_3}{\kappa_2^{3/2}}, \qquad \text{ExKurt}(\log S_T) = \frac{\kappa_4}{\kappa_2^2}
    $$

    where $\kappa_n$ denotes the $n$-th cumulant.

**Role of correlation $\rho$.** The dominant contribution to skewness comes from the correlation between stock returns and variance innovations. When $\rho < 0$ (the empirically relevant case), large downward stock moves coincide with variance increases, generating negative skewness. Specifically, the leading-order contribution to the third cumulant is proportional to $\rho \xi$:

$$
\kappa_3 \approx \frac{3\rho\xi}{\kappa} \left[\theta\tau + (v_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}\right] \cdot \frac{\xi}{\kappa} + O(\xi^3)
$$

**Role of vol-of-vol $\xi$.** The excess kurtosis is primarily driven by $\xi^2$. Even when $\rho = 0$, the randomness of variance itself generates fat tails. The leading-order contribution to the fourth cumulant scales as

$$
\kappa_4 \approx \frac{3\xi^2}{\kappa^2} \cdot (\text{integrated variance terms}) + O(\xi^3)
$$

!!! tip "Parameter Interpretation via Moments"
    - **$\rho < 0$**: Negative skewness (left-skewed returns). The more negative $\rho$, the stronger the skew.
    - **$\xi$ large**: Higher excess kurtosis (fatter tails). The vol-of-vol amplifies tail events.
    - **$\kappa$ large**: Faster mean reversion dampens both skewness and kurtosis for longer maturities.
    - **$\theta$ large**: Higher long-run variance increases the magnitude of all higher moments.

---

## Term Structure of Moments

The dependence of moments on time to maturity $\tau$ reveals important structural features of the Heston model.

**Short maturities ($\tau \to 0$).** As $\tau \to 0$:

- Variance: $\text{Var} \approx v_t \tau$, matching Black-Scholes with spot volatility $\sqrt{v_t}$
- Skewness: $\text{Skew} \approx \rho\xi / \sqrt{v_t} \cdot 1/\sqrt{\tau}$, which diverges. Short-dated options exhibit the steepest skew
- Excess kurtosis: $\text{ExKurt} \approx 3\xi^2 / (2v_t \tau)$, also diverging. Short-dated smiles have the highest curvature

**Long maturities ($\tau \to \infty$).** As $\tau \to \infty$:

- Variance: $\text{Var} \approx \theta\tau + O(1)$, growing linearly with $\tau$ as the integrated variance is dominated by the long-run level
- Skewness: $\text{Skew} \to 0$ as $1/\sqrt{\tau}$, since mean reversion pulls the distribution toward Gaussianity
- Excess kurtosis: $\text{ExKurt} \to 0$ as $1/\tau$, consistent with the central limit theorem for dependent increments

!!! warning "Moment Explosion Caveat"
    Moments $\mathbb{E}[S_T^p]$ exist only for $p$ in a bounded interval $(-p_-, p_+)$ where the critical exponents $p_\pm$ depend on $\kappa, \theta, \xi, \rho, \tau$. If $p$ exceeds $p_+$, the exponential moment explodes. This does not affect the log-return moments discussed here (which correspond to $p$ near 0), but is critical when computing the characteristic function for large imaginary arguments, as required by some Fourier pricing formulas.

---

## Numerical Example

Consider the following Heston parameter set:

| Parameter | Value | Description |
|-----------|-------|-------------|
| $S_0$ | 100 | Initial stock price |
| $v_0$ | 0.04 | Initial variance (20% vol) |
| $\kappa$ | 2.0 | Mean-reversion speed |
| $\theta$ | 0.04 | Long-run variance |
| $\xi$ | 0.3 | Vol-of-vol |
| $\rho$ | $-0.7$ | Correlation |
| $r$ | 0.05 | Risk-free rate |
| $q$ | 0.0 | Dividend yield |
| $\tau$ | 1.0 | Time to maturity |

**Step 1: Expected integrated variance.**

$$
\mathbb{E}\!\left[\int_0^T v_s \, ds\right] = \theta\tau + (v_0 - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa} = 0.04 \times 1 + 0 = 0.04
$$

Since $v_0 = \theta$, the mean-reversion term vanishes.

**Step 2: Mean of log-returns.**

$$
\mathbb{E}[\log S_T] = \log(100) + (0.05)(1) - \frac{1}{2}(0.04) = 4.6052 + 0.05 - 0.02 = 4.6352
$$

**Step 3: Variance of log-returns.** Using the full formula (simplified since $v_0 = \theta$):

$$
\text{Var}(\log S_T) \approx 0.04 + \frac{0.09}{8}(0.04)(1) + \frac{2(-0.7)(0.3)}{2}(0.04)(1 - 0.5) \approx 0.0395
$$

The standard deviation is approximately $\sqrt{0.0395} \approx 0.1988$, close to but slightly below the Black-Scholes value of $\sqrt{0.04} = 0.2$.

**Step 4: Skewness.** The negative correlation $\rho = -0.7$ produces negative skewness:

$$
\text{Skew}(\log S_T) \approx -0.31
$$

This is consistent with the empirical observation that equity returns are left-skewed.

**Step 5: Excess kurtosis.**

$$
\text{ExKurt}(\log S_T) \approx 0.22
$$

The positive excess kurtosis confirms fat tails relative to the normal distribution.

??? example "Comparison with Black-Scholes"
    Under Black-Scholes with $\sigma = 0.2$ and the same $r, q, \tau$:

    - Mean: $\log(100) + (0.05 - 0.02)(1) = 4.6352$ (identical)
    - Variance: $0.04$ (identical to leading order)
    - Skewness: $0$ (Black-Scholes returns are symmetric)
    - Excess kurtosis: $0$ (Black-Scholes returns are Gaussian)

    The Heston model's non-zero skewness and kurtosis explain the implied volatility smile observed in markets.

---

## Connection to Implied Volatility

The moments of $\log S_T$ are directly related to the shape of the implied volatility surface. A second-order expansion of the Black-Scholes implied volatility $\sigma_{\text{imp}}(K, T)$ around the at-the-money strike yields

$$
\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{ATM}} + \frac{\text{Skew}}{6\sqrt{\tau}} \cdot d + \frac{\text{ExKurt}}{24\tau} \cdot (d^2 - 1)
$$

where $d = (\log(K/F))/(\sigma_{\text{ATM}}\sqrt{\tau})$ is the standardized moneyness and $F = S_0 e^{(r-q)\tau}$ is the forward price. This formula shows that:

- **Skewness** controls the **slope** of the implied volatility smile (the skew)
- **Excess kurtosis** controls the **curvature** of the smile (the smile or smirk)

These relationships make moment computation from the characteristic function a fast diagnostic for assessing whether a given Heston parameter set produces a realistic smile.

---

## Summary

The characteristic function serves as a moment-generating device for the Heston model. Differentiating $\log \varphi(u)$ at $u = 0$ extracts cumulants that characterize the return distribution: the mean (drift minus half integrated variance), the variance (sensitive to $v_0, \theta, \xi$, and $\rho$), the skewness (driven primarily by $\rho\xi$), and the excess kurtosis (driven primarily by $\xi^2$). The term structure of these moments --- diverging skewness and kurtosis at short maturities, convergence to Gaussianity at long maturities --- explains the maturity-dependent shape of the implied volatility surface. These moment formulas provide fast, closed-form diagnostics for parameter calibration and model validation.
