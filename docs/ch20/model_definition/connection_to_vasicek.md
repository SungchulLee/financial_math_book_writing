# Connection to Vasicek

The Hull-White model is often called the "extended Vasicek model" because it generalizes the classical Vasicek model (1977) by replacing the constant drift parameter with a time-dependent function $\theta(t)$. This extension is not merely cosmetic: the time-dependent drift enables exact calibration to the observed term structure, which the original Vasicek model cannot achieve. Understanding the precise relationship between the two models clarifies when the simpler Vasicek model suffices and why the Hull-White extension is essential for derivative pricing in practice.

!!! info "Prerequisites"
    - Hull-White SDE and mean reversion (previous section)
    - Vasicek model: SDE, solution, bond pricing formula (Chapter 18)
    - Term structure of interest rates: zero-coupon bond prices, forward rates

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Vasicek SDE and identify it as a special case of Hull-White
    2. Derive the exact parameter mapping between the two models
    3. Compare the stationary distribution of Vasicek with the asymptotic behavior of Hull-White
    4. Explain why constant $\theta$ cannot fit an arbitrary initial yield curve
    5. Quantify the term structure fitting error of the Vasicek model

---

## The Vasicek Model

The Vasicek model (1977) was the first equilibrium short-rate model to incorporate mean reversion.

!!! note "Definition: Vasicek Model"
    The **Vasicek model** specifies the risk-neutral short rate dynamics

    $$
    dr_t = a\bigl(\theta_{\infty} - r_t\bigr)\, dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    where:

    - $\theta_{\infty} > 0$ is the constant long-run mean level
    - $a > 0$ is the mean-reversion speed
    - $\sigma > 0$ is the short rate volatility

The parameters $a$, $\theta_{\infty}$, and $\sigma$ are all constants. The short rate reverts to the fixed level $\theta_{\infty}$ at speed $a$, regardless of the current time or market conditions.

---

## Hull-White as Generalized Vasicek

The connection between the two models becomes transparent when we write them side by side.

| | Vasicek | Hull-White |
|:---|:---:|:---:|
| SDE | $dr_t = a(\theta_{\infty} - r_t)\, dt + \sigma\, dW_t$ | $dr_t = [\theta(t) - a\, r_t]\, dt + \sigma\, dW_t$ |
| Drift function | $a\theta_{\infty}$ (constant) | $\theta(t)$ (time-dependent) |
| Mean-reversion target | $\theta_{\infty}$ (fixed) | $\theta(t)/a$ (time-varying) |
| Free parameters | $a, \theta_{\infty}, \sigma$ | $a, \sigma$ (plus curve $\theta(t)$) |

!!! note "Theorem: Vasicek as Special Case"
    The Vasicek model is recovered from the Hull-White model by setting

    $$
    \theta(t) = a\, \theta_{\infty} \quad \text{for all } t \geq 0
    $$

    That is, replacing the time-dependent $\theta(t)$ with the constant $a\theta_{\infty}$ reduces the Hull-White SDE to the Vasicek SDE.

???+ note "Proof"
    The Hull-White SDE is

    $$
    dr_t = \bigl[\theta(t) - a\, r_t\bigr]\, dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    Setting $\theta(t) = a\theta_{\infty}$:

    $$
    dr_t = \bigl[a\theta_{\infty} - a\, r_t\bigr]\, dt + \sigma\, dW_t^{\mathbb{Q}} = a\bigl(\theta_{\infty} - r_t\bigr)\, dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    which is precisely the Vasicek SDE. $\square$

---

## Comparison of Solutions

Both models are Ornstein-Uhlenbeck processes with explicit solutions. The structural parallel is revealing.

**Vasicek solution** (starting from $r_s$ at time $s$):

$$
r_t = \theta_{\infty} + (r_s - \theta_{\infty})\, e^{-a(t-s)} + \sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}
$$

**Hull-White solution** (starting from $r_s$ at time $s$):

$$
r_t = r_s\, e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\, \theta(u)\, du + \sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}
$$

???+ note "Verification of Equivalence"
    Substituting $\theta(u) = a\theta_{\infty}$ into the Hull-White solution:

    $$
    \int_s^t e^{-a(t-u)}\, a\theta_{\infty}\, du = a\theta_{\infty} \left[-\frac{1}{a}\, e^{-a(t-u)}\right]_{u=s}^{u=t} = \theta_{\infty}\bigl(1 - e^{-a(t-s)}\bigr)
    $$

    Therefore the Hull-White solution becomes

    $$
    r_t = r_s\, e^{-a(t-s)} + \theta_{\infty}\bigl(1 - e^{-a(t-s)}\bigr) + \sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}
    $$

    $$
    = \theta_{\infty} + (r_s - \theta_{\infty})\, e^{-a(t-s)} + \sigma \int_s^t e^{-a(t-u)}\, dW_u^{\mathbb{Q}}
    $$

    which matches the Vasicek solution exactly. $\square$

The stochastic parts of both solutions are identical. The only difference lies in the deterministic drift integral, which in the Vasicek case evaluates to the closed-form expression $\theta_{\infty}(1 - e^{-a(t-s)})$ rather than requiring numerical evaluation of $\int_s^t e^{-a(t-u)}\theta(u)\, du$.

---

## Stationary Distribution Versus Asymptotic Behavior

A key qualitative difference between the two models concerns their long-time behavior.

!!! note "Theorem: Vasicek Stationary Distribution"
    The Vasicek model has a stationary distribution. As $t \to \infty$ with $s$ fixed:

    $$
    r_t \xrightarrow{d} r_{\infty} \sim \mathcal{N}\!\left(\theta_{\infty},\; \frac{\sigma^2}{2a}\right)
    $$

    The long-run mean is $\theta_{\infty}$ and the stationary variance is $\sigma^2/(2a)$.

???+ note "Proof"
    From the Vasicek solution, the conditional distribution is

    $$
    r_t \mid r_s \sim \mathcal{N}\!\left(\theta_{\infty} + (r_s - \theta_{\infty})e^{-a(t-s)},\; \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})\right)
    $$

    As $t - s \to \infty$:

    - The conditional mean converges to $\theta_{\infty}$ since $e^{-a(t-s)} \to 0$
    - The conditional variance converges to $\sigma^2/(2a)$ since $e^{-2a(t-s)} \to 0$

    The limiting distribution $\mathcal{N}(\theta_{\infty}, \sigma^2/(2a))$ is independent of the initial condition $r_s$, confirming stationarity. $\square$

The Hull-White model, by contrast, does **not** have a stationary distribution in general because $\theta(t)$ varies over time, so the mean-reversion target changes. The conditional variance still saturates at $\sigma^2/(2a)$ for large $t - s$ (the same as Vasicek), but the conditional mean $\mu(s,t)$ depends on the entire path of $\theta(u)$ over $[s,t]$ and does not converge to a fixed value.

---

## Term Structure Fitting: Why Vasicek Fails

The fundamental practical limitation of the Vasicek model is that its three parameters $(a, \theta_{\infty}, \sigma)$ are insufficient to match an arbitrary initial term structure.

!!! note "Proposition: Vasicek Bond Price"
    Under the Vasicek model, the zero-coupon bond price at time zero is

    $$
    P^{\text{Vas}}(0,T) = \exp\!\left(A^{\text{Vas}}(T) - B(T)\, r_0\right)
    $$

    where $B(T) = \frac{1 - e^{-aT}}{a}$ and

    $$
    A^{\text{Vas}}(T) = \left(\theta_{\infty} - \frac{\sigma^2}{2a^2}\right)\bigl(B(T) - T\bigr) - \frac{\sigma^2}{4a}\, B(T)^2
    $$

The function $P^{\text{Vas}}(0,T)$ is determined by three parameters, and its shape is tightly constrained. In particular, the implied forward rate curve under Vasicek is

$$
f^{\text{Vas}}(0,T) = -\frac{\partial}{\partial T}\ln P^{\text{Vas}}(0,T) = \theta_{\infty} + (r_0 - \theta_{\infty})\, e^{-aT} - \frac{\sigma^2}{2a^2}(1 - e^{-aT})^2
$$

This is a monotone function that converges to $\theta_{\infty} - \sigma^2/(2a^2)$ as $T \to \infty$. It cannot produce humped, inverted, or otherwise complex forward curve shapes that are frequently observed in the market.

**The Hull-White resolution.** In the Hull-White model, $\theta(t)$ is chosen to satisfy

$$
\theta(t) = \frac{\partial f^M(0,t)}{\partial t} + a\, f^M(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

where $f^M(0,t)$ is the market forward rate. This ensures $P^{\text{HW}}(0,T) = P^M(0,T)$ for all $T$ by construction, regardless of the shape of the market curve. The time-dependent $\theta(t)$ absorbs all the complexity of the initial term structure that Vasicek's constant $\theta_{\infty}$ cannot capture.

!!! example "Numerical Comparison"
    Consider a market yield curve with a hump: $f^M(0,t) = 0.03 + 0.02\, t\, e^{-0.5t}$.

    - **Vasicek** with best-fit parameters $(a = 0.1, \theta_{\infty} = 0.04, \sigma = 0.01, r_0 = 0.03)$ produces a monotonically increasing forward curve $f^{\text{Vas}}(0,t)$ that misses the hump entirely. The maximum fitting error $|f^M(0,t) - f^{\text{Vas}}(0,t)|$ exceeds 100 basis points near $t = 2$.
    - **Hull-White** with $(a = 0.1, \sigma = 0.01)$ and $\theta(t)$ computed from the formula above reproduces the humped market curve exactly at all maturities.

---

## Parameter Correspondence

When the Vasicek model is a reasonable approximation (e.g., for a nearly flat yield curve), the parameter correspondence provides useful intuition.

| Vasicek Parameter | Hull-White Equivalent | Interpretation |
|:---|:---|:---|
| $\theta_{\infty}$ | $\theta(t)/a$ at time $t$ | Instantaneous mean-reversion target |
| $a$ | $a$ (same) | Mean-reversion speed |
| $\sigma$ | $\sigma$ (same) | Short rate volatility |
| $r_0$ | $r_0$ (same) | Initial short rate |
| $\sigma^2/(2a)$ | $\sigma^2/(2a)$ (same) | Long-run (saturation) variance |
| $\ln 2 / a$ | $\ln 2 / a$ (same) | Half-life of mean reversion |

The mean-reversion speed $a$ and volatility $\sigma$ carry the same interpretation in both models. The only structural difference is that the constant target $\theta_{\infty}$ is replaced by the time-varying function $\theta(t)/a$ in Hull-White.

---

## When to Use Which Model

The choice between Vasicek and Hull-White depends on the application:

- **Vasicek** is appropriate for equilibrium modeling, long-horizon risk analysis, and theoretical studies where term structure consistency is not required. Its simplicity (three constant parameters, closed-form everything) makes it useful for building intuition and for pedagogical purposes.

- **Hull-White** is required whenever derivative prices must be consistent with observed bond prices. This includes all practical applications: pricing caps, floors, swaptions, callable bonds, and any product whose value depends on the term structure. The additional complexity of $\theta(t)$ is a small price to pay for no-arbitrage consistency with the market.

In practice, the market standard is to use Hull-White (or its extensions) and view Vasicek as the special case that provides intuition and limiting behavior.

---

## Summary

The Hull-White model generalizes Vasicek by replacing the constant drift $a\theta_{\infty}$ with $\theta(t)$, enabling exact calibration to the initial term structure. Setting $\theta(t) = a\theta_{\infty}$ recovers the Vasicek model, with its stationary distribution $\mathcal{N}(\theta_{\infty}, \sigma^2/(2a))$ and closed-form forward curve. The Vasicek model cannot match an arbitrary yield curve because its three parameters constrain the forward curve to a monotone exponential shape, while the Hull-White drift function $\theta(t)$ absorbs all the complexity of the observed market curve. Both models share the same mean-reversion speed, volatility, and variance structure, differing only in the drift specification.

---

## Exercises

**Exercise 1.** Consider the Vasicek model with $a = 0.08$, $\theta_\infty = 0.05$, $\sigma = 0.015$. Compute the stationary mean and variance. What is the 95% confidence interval for the long-run short rate?

??? success "Solution to Exercise 1"
    The stationary distribution of the Vasicek model is $\mathcal{N}(\theta_\infty, \sigma^2/(2a))$.

    **Stationary mean:** $\theta_\infty = 0.05$ (5%)

    **Stationary variance:**

    $$
    \frac{\sigma^2}{2a} = \frac{(0.015)^2}{2 \times 0.08} = \frac{0.000225}{0.16} = 0.00140625
    $$

    **Stationary standard deviation:**

    $$
    \sqrt{0.00140625} \approx 0.03750
    $$

    **95% confidence interval:** Using the standard normal quantile $z_{0.025} = 1.96$:

    $$
    \theta_\infty \pm 1.96 \times \frac{\sigma}{\sqrt{2a}} = 0.05 \pm 1.96 \times 0.03750 = 0.05 \pm 0.0735
    $$

    The 95% confidence interval is approximately $[-0.0235, \; 0.1235]$, or $[-235 \text{ bps}, \; 1235 \text{ bps}]$.

    Note that the interval includes negative rates, illustrating the Gaussian limitation of the Vasicek (and Hull-White) model. The lower bound of $-2.35\%$ is financially unrealistic for most historical environments, though negative rates have been observed in practice (e.g., European sovereign bonds post-2014).

---

**Exercise 2.** Verify that substituting $\theta(t) = a\theta_\infty$ into the Hull-White solution $r_t = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du + \sigma\int_s^t e^{-a(t-u)}dW_u$ yields the Vasicek solution. Evaluate the deterministic integral explicitly.

??? success "Solution to Exercise 2"
    Starting from the Hull-White solution with $\theta(u) = a\theta_\infty$:

    $$
    r_t = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)} a\theta_\infty\,du + \sigma\int_s^t e^{-a(t-u)}dW_u
    $$

    Evaluate the deterministic integral by substituting $v = t - u$, so $du = -dv$:

    $$
    \int_s^t e^{-a(t-u)} a\theta_\infty\,du = a\theta_\infty \int_0^{t-s} e^{-av}\,dv = a\theta_\infty \left[-\frac{1}{a}e^{-av}\right]_0^{t-s} = \theta_\infty(1 - e^{-a(t-s)})
    $$

    Substituting back:

    $$
    r_t = r_s e^{-a(t-s)} + \theta_\infty(1 - e^{-a(t-s)}) + \sigma\int_s^t e^{-a(t-u)}dW_u
    $$

    Rearranging $r_s e^{-a(t-s)} + \theta_\infty - \theta_\infty e^{-a(t-s)}$:

    $$
    r_t = \theta_\infty + (r_s - \theta_\infty)e^{-a(t-s)} + \sigma\int_s^t e^{-a(t-u)}dW_u
    $$

    This is exactly the standard Vasicek solution.

---

**Exercise 3.** Under the Vasicek model, the implied forward rate is $f^{\text{Vas}}(0,T) = \theta_\infty + (r_0 - \theta_\infty)e^{-aT} - \frac{\sigma^2}{2a^2}(1 - e^{-aT})^2$. Plot this curve for $a = 0.1$, $\theta_\infty = 0.04$, $\sigma = 0.01$, and $r_0 = 0.03$. Is it monotone? What is the asymptotic forward rate as $T \to \infty$?

??? success "Solution to Exercise 3"
    The Vasicek forward rate is

    $$
    f^{\text{Vas}}(0,T) = \theta_\infty + (r_0 - \theta_\infty)e^{-aT} - \frac{\sigma^2}{2a^2}(1 - e^{-aT})^2
    $$

    With $a = 0.1$, $\theta_\infty = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$:

    $$
    f^{\text{Vas}}(0,T) = 0.04 + (0.03 - 0.04)e^{-0.1T} - \frac{0.0001}{0.02}(1 - e^{-0.1T})^2
    $$

    $$
    = 0.04 - 0.01\,e^{-0.1T} - 0.005(1 - e^{-0.1T})^2
    $$

    Computing at several maturities:

    | $T$ | $e^{-0.1T}$ | $f^{\text{Vas}}(0,T)$ |
    |:---:|:---:|:---:|
    | 0 | 1.000 | $0.04 - 0.01 - 0 = 0.030$ |
    | 5 | 0.6065 | $0.04 - 0.006065 - 0.000774 = 0.03316$ |
    | 10 | 0.3679 | $0.04 - 0.003679 - 0.001998 = 0.03432$ |
    | 20 | 0.1353 | $0.04 - 0.001353 - 0.003739 = 0.03491$ |
    | 50 | 0.00674 | $0.04 - 0.000067 - 0.004934 = 0.03500$ |
    | $\infty$ | 0 | $0.04 - 0 - 0.005 = 0.035$ |

    **Monotonicity:** The curve is monotonically increasing from $f(0,0) = r_0 = 0.03$ toward the asymptotic level. To verify, the derivative with respect to $T$ can be checked to be positive throughout (since $r_0 < \theta_\infty - \sigma^2/(2a^2)$, the dominant term $(r_0 - \theta_\infty)(-a)e^{-aT} > 0$ drives the curve upward).

    **Asymptotic forward rate:**

    $$
    \lim_{T \to \infty} f^{\text{Vas}}(0,T) = \theta_\infty - \frac{\sigma^2}{2a^2} = 0.04 - 0.005 = 0.035
    $$

    The asymptotic forward rate is 3.5%, which is below $\theta_\infty = 4\%$ due to the convexity adjustment $\sigma^2/(2a^2) = 50$ bps.

---

**Exercise 4.** A market has a humped forward curve $f^M(0,t) = 0.03 + 0.02t\,e^{-0.5t}$. Show that no choice of Vasicek parameters $(a, \theta_\infty, \sigma, r_0)$ can reproduce this curve exactly. Estimate the maximum fitting error in basis points for a best-fit Vasicek model.

??? success "Solution to Exercise 4"
    The market forward curve $f^M(0,t) = 0.03 + 0.02t\,e^{-0.5t}$ has a hump. To see this, compute $\frac{d}{dt}f^M(0,t) = 0.02 e^{-0.5t}(1 - 0.5t)$, which equals zero at $t^* = 2$, with $f^M(0,2) = 0.03 + 0.04 e^{-1} \approx 0.04472$. This is a genuine hump (the forward rate rises, peaks, then declines).

    The Vasicek forward rate has the form

    $$
    f^{\text{Vas}}(0,T) = \theta_\infty + (r_0 - \theta_\infty)e^{-aT} - \frac{\sigma^2}{2a^2}(1 - e^{-aT})^2
    $$

    **Why exact reproduction is impossible:** The derivative $\frac{d}{dT}f^{\text{Vas}}(0,T)$ is

    $$
    \frac{d}{dT}f^{\text{Vas}}(0,T) = -a(r_0 - \theta_\infty)e^{-aT} - \frac{\sigma^2}{a}e^{-aT}(1 - e^{-aT})
    $$

    For this derivative to change sign (necessary for a hump), we need $(r_0 - \theta_\infty)$ and the convexity term to have opposite signs, but the convexity term $-\frac{\sigma^2}{a}e^{-aT}(1-e^{-aT})$ is always non-positive. If $r_0 < \theta_\infty$, the first term is positive and the second is negative, so a sign change is possible. However, the resulting hump is constrained to a specific parametric shape (a combination of $e^{-aT}$ and $e^{-2aT}$ terms), which cannot match the $t\,e^{-0.5t}$ shape of the market curve.

    **Estimating the maximum fitting error:** The market curve has $f^M(0,0) = 0.03$ and $f^M(0,\infty) = 0.03$. The best-fit Vasicek must satisfy $f^{\text{Vas}}(0,0) = r_0$ and $f^{\text{Vas}}(0,\infty) = \theta_\infty - \sigma^2/(2a^2)$. Setting $r_0 = 0.03$ and the asymptotic rate to $0.03$ constrains $\theta_\infty = 0.03 + \sigma^2/(2a^2)$.

    Near the hump at $t \approx 2$, $f^M(0,2) \approx 0.0447$. A Vasicek curve with $r_0 = 0.03$ and reasonable parameters will produce a forward rate near $0.03$--$0.035$ at $T=2$ (depending on parameters), giving a fitting error of at least 100--150 basis points near the hump peak.

---

**Exercise 5.** Explain why the Hull-White model does not have a stationary distribution when $\theta(t)$ is time-dependent. Under what conditions on $\theta(t)$ would the Hull-White model have an approximate stationary distribution?

??? success "Solution to Exercise 5"
    The Vasicek model has a stationary distribution because its mean-reversion target $\theta_\infty$ is constant. Starting from any initial condition, the conditional mean $\mathbb{E}[r_t | r_s] = \theta_\infty + (r_s - \theta_\infty)e^{-a(t-s)}$ converges to $\theta_\infty$ as $t-s \to \infty$, regardless of $r_s$.

    **Why Hull-White lacks stationarity:** In the Hull-White model, the conditional mean is

    $$
    \mathbb{E}[r_t | r_s] = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du
    $$

    As $t \to \infty$, the first term vanishes, but the integral $\int_s^t e^{-a(t-u)}\theta(u)\,du$ depends on the future path of $\theta(u)$, which changes over time. Since $\theta(t)$ is calibrated to the initial forward curve and varies with $t$, the "target level" $\theta(t)/a$ is itself time-dependent. There is no fixed value to which $r_t$ converges in distribution, so no stationary distribution exists.

    **Conditions for approximate stationarity:** The Hull-White model would have an approximate stationary distribution if $\theta(t)$ converges to a constant $\theta_\infty$ as $t \to \infty$. Specifically:

    - If $\theta(t) \to a\theta_\infty$ sufficiently fast (e.g., the initial forward curve $f(0,t)$ converges to a constant $f_\infty$ and the convexity correction saturates), then for large $t$, the model behaves like a Vasicek model with long-run mean $\theta_\infty$.
    - In practice, $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})$. If $f(0,t) \to f_\infty$ and $f'(0,t) \to 0$, then $\theta(t) \to af_\infty + \frac{\sigma^2}{2a}$, and the approximate stationary distribution is $\mathcal{N}(f_\infty + \frac{\sigma^2}{2a^2}, \; \frac{\sigma^2}{2a})$.

---

**Exercise 6.** The Vasicek bond price formula involves $A^{\text{Vas}}(T) = (\theta_\infty - \frac{\sigma^2}{2a^2})(B(T) - T) - \frac{\sigma^2}{4a}B(T)^2$. Derive this from the Hull-White formula for $A(t,T)$ by setting $\theta(t) = a\theta_\infty$ and $t = 0$.

??? success "Solution to Exercise 6"
    Under the Vasicek model ($\theta(t) = a\theta_\infty$ constant), the Hull-White formula $A(t,T) = \ln\frac{P(0,T)}{P(0,t)} + B(t,T)f(0,t) + \frac{\sigma^2}{4a}B(t,T)^2(1 - e^{-2at})$ must reduce to the Vasicek formula when $t = 0$.

    **Setting $t = 0$:** We have $B(0,T) = -(1 - e^{-aT})/a$, so $|B(0,T)| = B(T)$ in the standard notation. Also $P(0,0) = 1$, $f(0,0) = r_0$, and $e^{-2a \cdot 0} = 1$:

    $$
    A(0,T) = \ln P(0,T) + B(0,T) \cdot r_0 + \frac{\sigma^2}{4a}B(0,T)^2 \cdot 0
    $$

    Since $P(0,T) = e^{A^{\text{Vas}}(T) - B(T)r_0}$ (using the Vasicek formula with the sign convention $\hat{B} = -B(0,T) = B(T)$):

    $$
    A(0,T) = A^{\text{Vas}}(T) - B(T)r_0 - B(T)r_0 + 0
    $$

    Wait -- let us be more careful. Under the Hull-White convention, $P(0,T) = e^{A(0,T) + B(0,T)r_0}$, so $A(0,T) = \ln P(0,T) - B(0,T)r_0$.

    Under Vasicek, $P^{\text{Vas}}(0,T) = e^{A^{\text{Vas}}(T) - B(T)r_0}$ where $B(T) = (1 - e^{-aT})/a$ and $B(0,T) = -B(T)$.

    Setting $\theta(u) = a\theta_\infty$, start from the integral representation:

    $$
    A(0,T) = \int_0^T \theta(u) B(u,T)\,du + \frac{\sigma^2}{2}\int_0^T B(u,T)^2\,du
    $$

    With $B(u,T) = -(1 - e^{-a(T-u)})/a$ and $\theta(u) = a\theta_\infty$:

    $$
    \int_0^T a\theta_\infty \left(-\frac{1 - e^{-a(T-u)}}{a}\right) du = -\theta_\infty \int_0^T (1 - e^{-a(T-u)})\,du
    $$

    $$
    = -\theta_\infty\left[T - \frac{1 - e^{-aT}}{a}\right] = -\theta_\infty(T - B(T)) = \theta_\infty(B(T) - T)
    $$

    For the second integral:

    $$
    \frac{\sigma^2}{2}\int_0^T \frac{(1 - e^{-a(T-u)})^2}{a^2}\,du
    $$

    Substituting $v = T - u$:

    $$
    = \frac{\sigma^2}{2a^2}\int_0^T (1 - e^{-av})^2\,dv = \frac{\sigma^2}{2a^2}\left[T - \frac{2(1 - e^{-aT})}{a} + \frac{1 - e^{-2aT}}{2a}\right]
    $$

    $$
    = \frac{\sigma^2}{2a^2}\left[T - 2B(T) + \frac{1 - e^{-2aT}}{2a}\right]
    $$

    Using $B(T)^2 = (1-e^{-aT})^2/a^2$ and $\frac{1-e^{-2aT}}{2a} = \frac{(1-e^{-aT})(1+e^{-aT})}{2a}$, after simplification:

    $$
    A(0,T) = \theta_\infty(B(T) - T) + \frac{\sigma^2}{2a^2}(T - 2B(T)) + \frac{\sigma^2}{4a}B(T)^2
    $$

    Rearranging:

    $$
    A(0,T) = \left(\theta_\infty - \frac{\sigma^2}{2a^2}\right)(B(T) - T) - \frac{\sigma^2}{4a}B(T)^2
    $$

    This is precisely $A^{\text{Vas}}(T)$.

---

**Exercise 7.** Discuss the trade-offs between using the Vasicek model and the Hull-White model for (a) long-horizon risk simulation, (b) pricing a 5-year cap, and (c) hedging a callable bond. In which cases is term structure consistency essential?

??? success "Solution to Exercise 7"
    **(a) Long-horizon risk simulation (e.g., 30-year projection):**

    - **Vasicek is adequate.** For long-horizon simulation, the goal is to capture the statistical behavior of rates (mean reversion, volatility, distribution of paths) rather than to match today's market curve exactly. The Vasicek model's three constant parameters $(a, \theta_\infty, \sigma)$ provide a parsimonious description of rate dynamics. The stationary distribution $\mathcal{N}(\theta_\infty, \sigma^2/(2a))$ gives a meaningful long-run equilibrium.
    - **Hull-White trade-off:** Over 30 years, the initial term structure becomes irrelevant (the memory of $\theta(t)$ fades), and the Hull-White model effectively behaves like Vasicek. The added complexity of $\theta(t)$ provides no benefit for long-horizon statistics.

    **(b) Pricing a 5-year cap:**

    - **Hull-White is essential.** A cap is a portfolio of caplets, and its price depends on the term structure of rates at each reset date. If the model does not match the initial term structure, cap prices will be inconsistent with observed bond prices, creating arbitrage opportunities. Hull-White's $\theta(t)$ ensures that the model reproduces market discount factors exactly, so caplet prices are consistent with the yield curve.
    - **Vasicek trade-off:** Vasicek's three parameters cannot match the market yield curve, leading to systematic mispricing of caplets across different tenors. The fitting error translates directly into pricing error for the cap.

    **(c) Hedging a callable bond:**

    - **Hull-White is essential.** Hedging a callable bond requires computing sensitivities (delta, gamma) with respect to the yield curve. The hedge ratios depend on the model's bond prices matching the market at time zero. If the model misprices the underlying bonds, the hedges will be systematically biased.
    - **Vasicek trade-off:** The callable bond's exercise boundary depends on the entire yield curve at each exercise date. Vasicek's inability to match the initial curve means the exercise boundary is incorrect, leading to wrong hedge ratios and P&L leakage.

    **Summary:** Term structure consistency is essential for (b) and (c) -- any application involving relative pricing or hedging of derivatives against the observed yield curve. For (a), where the focus is on long-run statistical properties, the simpler Vasicek model suffices.
