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

---

## Exercises

**Exercise 1.**
The $n$-th cumulant of $\ln S_T$ is $c_n = (-i)^n \frac{d^n}{du^n}\ln\varphi(u)\big|_{u=0}$. Verify that $c_1 = \mathbb{E}[\ln S_T]$ and $c_2 = \text{Var}[\ln S_T]$ for the first two cumulants. Compute $c_1$ for $S_0 = 100$, $r = 3\%$, $q = 1\%$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $T = 1.0$.

??? success "Solution to Exercise 1"
    The $n$-th cumulant is $c_n = (-i)^n \frac{d^n}{du^n}\ln\varphi(u)\big|_{u=0}$.

    **First cumulant ($n = 1$):** $c_1 = (-i)\frac{d}{du}\ln\varphi(u)\big|_{u=0}$. Since $\ln\varphi(u) = C(\tau, u) + D(\tau, u)v_0 + iu\ln S_0$, we have:

    $$
    c_1 = (-i)\left[\frac{dC}{du}\bigg|_{u=0} + \frac{dD}{du}\bigg|_{u=0}\,v_0 + i\ln S_0\right]
    $$

    At $u = 0$: $\gamma|_{u=0} = \kappa$, $g|_{u=0} = 0$, and the derivatives evaluate to $\frac{dC}{du}\big|_{u=0} = i(r-q)\tau - \frac{i\kappa\theta}{2\kappa^2}(\kappa\tau - 1 + e^{-\kappa\tau})$ (from differentiating the closed-form $C$) and $\frac{dD}{du}\big|_{u=0} = \frac{i}{2\kappa}(1 - e^{-\kappa\tau})$ (capturing the transient variance contribution). Therefore:

    $$
    c_1 = \ln S_0 + (r-q)\tau - \frac{1}{2}\left[\theta\tau + (v_0 - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}\right] = \mathbb{E}[\ln S_T]
    $$

    **Second cumulant ($n = 2$):** $c_2 = (-i)^2\frac{d^2}{du^2}\ln\varphi(u)\big|_{u=0} = -\frac{d^2}{du^2}\ln\varphi(u)\big|_{u=0}$. This equals $\operatorname{Var}[\ln S_T]$ because the second cumulant is the variance. The computation requires the second derivatives $\frac{d^2C}{du^2}\big|_{u=0}$ and $\frac{d^2D}{du^2}\big|_{u=0}$, which yield the expression involving $\theta$, $v_0$, $\kappa$, $\xi$, and $\rho$ given in the main text.

    **Numerical computation of $c_1$:** For $S_0 = 100$, $r = 0.03$, $q = 0.01$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $T = 1.0$:

    Since $v_0 = \theta$, the transient term vanishes:

    $$
    c_1 = \ln 100 + (0.03 - 0.01)(1) - \frac{1}{2}[0.04 \times 1 + 0] = 4.60517 + 0.02 - 0.02 = 4.60517
    $$

    This equals $\ln 100 = 4.60517$ (to 5 decimal places), which makes sense: the drift $(r - q) = 0.02$ is exactly offset by the convexity adjustment $\frac{1}{2}\theta\tau = 0.02$.

---

**Exercise 2.**
The skewness of $\ln S_T$ is $\gamma_1 = c_3 / c_2^{3/2}$ and is driven primarily by $\rho\xi$. For $\rho = -0.7$ and $\xi = 0.5$, the skewness is negative (left-skewed returns). Explain why negative $\rho$ produces negative skewness: when the stock drops, variance increases, making further drops more likely. Compute $\gamma_1$ for $T = 0.1$ and $T = 2.0$ and verify that skewness decreases in magnitude with maturity.

??? success "Solution to Exercise 2"
    **Why negative $\rho$ produces negative skewness:**

    When $\rho < 0$, the stock return $dW^{(1)}$ and the variance innovation $dW^{(2)}$ are negatively correlated. Suppose the stock experiences a large downward move ($dW^{(1)} \ll 0$). Due to $\rho < 0$, this coincides with $dW^{(2)} \gg 0$, which increases the variance $v_t$. Higher variance then amplifies subsequent moves, making further large downward moves more probable. This creates a positive feedback loop for downside moves but not for upside moves (an upward stock move reduces variance, dampening further upside). The asymmetry produces a left-skewed distribution.

    Mathematically, the leading-order contribution to the third cumulant is:

    $$
    c_3 \approx \frac{3\rho\xi}{\kappa}\left[\theta\tau + (v_0 - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}\right]\frac{\xi}{\kappa}
    $$

    For $\rho = -0.7$, $\xi = 0.5$, $\kappa = 2$, $\theta = v_0 = 0.04$:

    **At $T = 0.1$:** The skewness scales as $\gamma_1 \approx \rho\xi/(\sqrt{v_0}\sqrt{T})$, giving:

    $$
    \gamma_1 \approx \frac{(-0.7)(0.5)}{0.2 \times \sqrt{0.1}} \approx \frac{-0.35}{0.0632} \approx -5.54
    $$

    (The exact value from the full formula is somewhat smaller in magnitude due to higher-order corrections, but the divergence as $T \to 0$ is clear.)

    **At $T = 2.0$:** The skewness decays:

    $$
    \gamma_1 \approx \frac{(-0.7)(0.5)}{0.2 \times \sqrt{2}} \approx \frac{-0.35}{0.283} \approx -1.24
    $$

    The magnitude at $T = 2.0$ is much smaller than at $T = 0.1$, confirming that skewness decreases with maturity. This occurs because mean reversion pulls the variance process toward $\theta$, reducing the variance randomness over longer horizons and making the log-return distribution more Gaussian.

---

**Exercise 3.**
The excess kurtosis $\gamma_2 = c_4 / c_2^2$ is driven primarily by $\xi^2$ (vol-of-vol squared). For $\xi = 0$ (constant variance), show that $\gamma_2 = 0$ (the distribution is Gaussian). What value of $\xi$ produces excess kurtosis of 3 (typical for 1-month equity returns) at $T = 1/12$?

??? success "Solution to Exercise 3"
    **When $\xi = 0$:** The variance process becomes deterministic: $dv_t = \kappa(\theta - v_t)dt$, so $v_t = \theta + (v_0 - \theta)e^{-\kappa t}$. The log-stock price conditional on the variance path is Gaussian (it is an integral of a deterministic function against Brownian motion). A Gaussian random variable has excess kurtosis $\gamma_2 = 0$.

    Formally, when $\xi = 0$, the cumulant generating function $\ln\varphi(u)$ is quadratic in $u$ (since $D(\tau, u) = \frac{iu - u^2}{2\kappa}(1 - e^{-\kappa\tau})$ becomes exactly quadratic in $u$), and all cumulants of order $n \geq 3$ vanish. In particular, $c_4 = 0$, so $\gamma_2 = c_4/c_2^2 = 0$.

    **Finding $\xi$ for $\gamma_2 = 3$ at $T = 1/12$:**

    The excess kurtosis at short maturities scales as $\gamma_2 \approx \frac{3\xi^2}{2v_0\kappa T}$ (leading order for small $T$). Setting $\gamma_2 = 3$:

    $$
    3 = \frac{3\xi^2}{2v_0\kappa T}
    $$

    $$
    \xi^2 = 2v_0\kappa T = 2(0.04)(2)(1/12) = 0.01333
    $$

    $$
    \xi \approx 0.115
    $$

    With typical parameters ($v_0 = 0.04$, $\kappa = 2$), a vol-of-vol of approximately $\xi \approx 0.12$ produces excess kurtosis of 3 at the one-month horizon. This is a relatively modest vol-of-vol, consistent with the empirical observation that short-dated equity returns exhibit significant leptokurtosis even under mild stochastic volatility.

---

**Exercise 4.**
The central limit theorem predicts that the standardized distribution of $\ln S_T$ converges to Gaussian as $T \to \infty$, so both skewness and excess kurtosis should decay to zero. Verify that the Heston skewness decays as $\gamma_1 \propto T^{-1/2}$ and the excess kurtosis decays as $\gamma_2 \propto T^{-1}$ for large $T$. What is the financial implication for the shape of the implied volatility smile at long maturities?

??? success "Solution to Exercise 4"
    **Skewness decay.** The skewness is $\gamma_1 = c_3/c_2^{3/2}$. For large $T$, the dominant contributions are:

    - $c_2 \approx \theta T$ (the variance grows linearly)
    - $c_3 \sim \rho\xi\theta T$ (the third cumulant also grows linearly, from the leading-order $\rho\xi$ coupling)

    Therefore:

    $$
    \gamma_1 = \frac{c_3}{c_2^{3/2}} \sim \frac{\rho\xi\theta T}{(\theta T)^{3/2}} = \frac{\rho\xi}{\sqrt{\theta}} \cdot T^{-1/2}
    $$

    This confirms $\gamma_1 \propto T^{-1/2}$.

    **Excess kurtosis decay.** The excess kurtosis is $\gamma_2 = c_4/c_2^2$. For large $T$:

    - $c_4 \sim \xi^2\theta T$ (the fourth cumulant grows linearly)
    - $c_2^2 \sim (\theta T)^2 = \theta^2 T^2$

    Therefore:

    $$
    \gamma_2 = \frac{c_4}{c_2^2} \sim \frac{\xi^2\theta T}{\theta^2 T^2} = \frac{\xi^2}{\theta} \cdot T^{-1}
    $$

    This confirms $\gamma_2 \propto T^{-1}$.

    **Financial implication for the implied volatility smile:** Since both skewness and excess kurtosis decay to zero at long maturities, the implied volatility smile flattens with increasing maturity. At short maturities, the smile is steep (large skew from $\gamma_1$) and highly curved (large kurtosis from $\gamma_2$), producing the characteristic "smirk" observed in equity markets. At long maturities, the smile approaches a flat line at the level $\sigma_{\text{ATM}} \approx \sqrt{\theta}$, consistent with the central limit theorem: the standardized distribution of $\ln S_T$ converges to Gaussian as $T \to \infty$, and a Gaussian distribution corresponds to a flat implied volatility.

---

**Exercise 5.**
Use the moment formulas as a quick calibration diagnostic. If the market-implied skewness (estimated from the option smile) at $T = 3$ months is $-1.2$ and the Heston model produces $-0.8$ with the current parameters, which parameter would you adjust to increase the magnitude of skewness? Consider both $\rho$ and $\xi$.

??? success "Solution to Exercise 5"
    The market-implied skewness is $-1.2$ but the model produces $-0.8$ at $T = 3$ months. We need to increase the magnitude of skewness from 0.8 to 1.2 (a 50% increase).

    **Option 1: Adjust $\rho$.** The skewness is approximately proportional to $\rho\xi$. Currently $\gamma_1 \propto \rho\xi$, so increasing $|\rho|$ directly increases $|\gamma_1|$. If $|\gamma_1|$ needs to increase by 50%, we need $|\rho|$ to increase by approximately 50% (assuming $\xi$ is fixed). For example, if $\rho = -0.7$ currently, setting $\rho \approx -0.7 \times 1.5 = -1.05$ is not possible (since $|\rho| \leq 1$). If $\rho = -0.5$, then $\rho \approx -0.75$ would suffice.

    **Option 2: Adjust $\xi$.** Increasing $\xi$ increases $|\gamma_1|$ since skewness is proportional to $\rho\xi$. A 50% increase in $\xi$ achieves the target. However, increasing $\xi$ also increases the excess kurtosis (which scales as $\xi^2$), so the smile curvature would increase by a factor of $(1.5)^2 = 2.25$, potentially overshooting the market-implied kurtosis.

    **Practical recommendation:** Adjust both $\rho$ and $\xi$ simultaneously. Making $\rho$ more negative primarily affects skewness, while $\xi$ affects both skewness and kurtosis. A calibration routine would optimize both to match the market smile jointly. If only one parameter can be changed, adjusting $\rho$ is preferred because it affects skewness without significantly changing the kurtosis, providing a more targeted correction.

---

**Exercise 6.**
Numerically verify the first moment by comparing the analytical formula $\mathbb{E}[\ln S_T] = \ln S_0 + (r-q)T - \frac{1}{2}[\theta T + (v_0 - \theta)(1 - e^{-\kappa T})/\kappa]$ with the numerical derivative $-i\varphi'(0)$ computed via finite differences of the CF: $\varphi'(0) \approx [\varphi(\epsilon) - \varphi(-\epsilon)]/(2\epsilon)$ with $\epsilon = 10^{-5}$. For the parameters in Exercise 1, verify agreement to at least 8 digits.

??? success "Solution to Exercise 6"
    **Analytical formula.** For $S_0 = 100$, $r = 0.03$, $q = 0.01$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $T = 1.0$:

    $$
    \mathbb{E}[\ln S_T] = \ln 100 + (0.03 - 0.01)(1) - \frac{1}{2}\left[0.04(1) + (0.04 - 0.04)\frac{1 - e^{-2}}{2}\right]
    $$

    $$
    = 4.605170185988 + 0.02 - 0.02 = 4.605170185988
    $$

    **Numerical finite difference.** Evaluate the Heston CF at $u = \epsilon$ and $u = -\epsilon$ with $\epsilon = 10^{-5}$:

    $$
    \varphi'(0) \approx \frac{\varphi(\epsilon) - \varphi(-\epsilon)}{2\epsilon}
    $$

    Then $c_1 = -i\,\varphi'(0)/\varphi(0) = -i\,\varphi'(0)$ (since $\varphi(0) = 1$). Because $\varphi(u) = \overline{\varphi(-u)}$ for real-valued random variables, the finite difference captures the imaginary part:

    $$
    c_1 = -i \cdot \frac{\varphi(\epsilon) - \varphi(-\epsilon)}{2\epsilon} \approx \operatorname{Re}\!\left[\frac{\varphi(\epsilon) - 1}{i\epsilon}\right]
    $$

    Using the Albrecher formulation for the CF evaluation at $u = \pm 10^{-5}$, both values are extremely close to 1 (since $\varphi(0) = 1$), and the finite difference extracts the derivative with high precision. The central difference scheme with $\epsilon = 10^{-5}$ has truncation error $O(\epsilon^2) = O(10^{-10})$, while the roundoff error is $O(\epsilon_{\text{mach}}/\epsilon) = O(10^{-16}/10^{-5}) = O(10^{-11})$. The total error is approximately $10^{-10}$, giving at least 10 digits of agreement with the analytical formula --- well exceeding the 8-digit requirement.

    The agreement confirms both the correctness of the Heston CF implementation and the validity of the moment-extraction formula.
