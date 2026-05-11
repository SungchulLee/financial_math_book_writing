# Fitting theta(t) to the Initial Yield Curve

The defining practical advantage of the Hull-White model over the Vasicek model is the ability to exactly reproduce the market-observed term structure of interest rates. This is achieved by choosing the drift function $\theta(t)$ so that the model bond prices at time zero match the market bond prices for all maturities. The resulting formula for $\theta(t)$ is explicit and involves only the initial forward rate curve and its derivative. This section derives the formula, proves the exact fit property, discusses numerical implementation, and illustrates with examples.

!!! info "Prerequisites"

    - Hull-White SDE and explicit solution (this chapter)
    - Short rate distribution: conditional mean and variance
    - Affine bond price formula: $P(t,T) = e^{A(t,T) + B(t,T) r_t}$
    - Market conventions: forward rates $f(0,t) = -\partial_t \ln P^M(0,t)$

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the formula for $\theta(t)$ from the no-arbitrage condition
    2. Verify that the formula guarantees $P^{\text{model}}(0,T) = P^M(0,T)$ for all $T$
    3. Interpret each term in the $\theta(t)$ formula
    4. Implement $\theta(t)$ numerically from a discrete yield curve
    5. Recognize potential numerical pitfalls and their solutions

---

## The Exact Fit Requirement

The fundamental requirement for any no-arbitrage interest rate model used in derivative pricing is:

$$
P^{\text{model}}(0,T) = P^M(0,T) \quad \text{for all } T \geq 0
$$

where $P^M(0,T)$ is the market discount factor (zero-coupon bond price) observed at time zero. If this condition fails, the model introduces arbitrage between the model-implied and market-observed bond prices, making derivative prices inconsistent with the underlying yield curve.

In the Hull-White model, the parameters $a$ and $\sigma$ are chosen to fit volatility data (caps, swaptions), while $\theta(t)$ is the degree of freedom that absorbs the initial term structure.

---

## Derivation of the theta Formula

!!! note "Theorem: Exact Calibration Formula for $\theta(t)$"
    The unique function $\theta(t)$ that makes the Hull-White model consistent with the initial term structure $P^M(0,T)$ is

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + a\, f(0,t) + \frac{\sigma^2}{2a}\bigl(1 - e^{-2at}\bigr)
    $$

    where $f(0,t) = -\frac{\partial}{\partial t}\ln P^M(0,t)$ is the market instantaneous forward rate.

???+ note "Proof"
    **Strategy:** Require that the model bond price $P^{\text{model}}(0,T)$ equals $P^M(0,T)$ and solve for $\theta(t)$.

    **Step 1: Model bond price at time zero.** From the affine formula:

    $$
    P(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\, ds}\right]
    $$

    Since $\int_0^T r_s\, ds$ is Gaussian with mean $M(0,T)$ and variance $V(0,T)$:

    $$
    P(0,T) = \exp\!\left(-M(0,T) + \frac{1}{2}V(0,T)\right)
    $$

    **Step 2: Compute the model forward rate.** The model forward rate is

    $$
    f^{\text{model}}(0,t) = -\frac{\partial}{\partial t}\ln P(0,t) = \frac{\partial M(0,t)}{\partial t} - \frac{1}{2}\frac{\partial V(0,t)}{\partial t}
    $$

    From the explicit solution with $s = 0$:

    $$
    \mathbb{E}[r_t] = r_0\, e^{-at} + \int_0^t e^{-a(t-u)}\, \theta(u)\, du
    $$

    The mean of the integrated rate is $M(0,t) = \int_0^t \mathbb{E}[r_s]\, ds$, and $\frac{\partial M(0,t)}{\partial t} = \mathbb{E}[r_t]$.

    For the variance term: $\frac{\partial V(0,t)}{\partial t} = \frac{\sigma^2}{a^2}[1 - 2e^{-at} + e^{-2at}] \cdot \frac{\partial}{\partial t}(\cdots)$. After careful differentiation:

    $$
    \frac{1}{2}\frac{\partial V(0,t)}{\partial t} = \frac{\sigma^2}{2a^2}(1 - e^{-at})^2
    $$

    **Step 3: Impose the fit condition.** Setting $f^{\text{model}}(0,t) = f^M(0,t)$:

    $$
    r_0\, e^{-at} + \int_0^t e^{-a(t-u)}\, \theta(u)\, du - \frac{\sigma^2}{2a^2}(1 - e^{-at})^2 = f^M(0,t)
    $$

    Differentiating both sides with respect to $t$:

    $$
    -a r_0\, e^{-at} + \theta(t) - a\int_0^t e^{-a(t-u)}\, \theta(u)\, du - \frac{\sigma^2}{a}e^{-at}(1 - e^{-at}) = f'(0,t)
    $$

    From the fit condition, $\int_0^t e^{-a(t-u)} \theta(u)\, du = f^M(0,t) - r_0 e^{-at} + \frac{\sigma^2}{2a^2}(1-e^{-at})^2$. Substituting:

    $$
    \theta(t) = f'(0,t) + a\left[f^M(0,t) - r_0 e^{-at} + \frac{\sigma^2}{2a^2}(1-e^{-at})^2\right] + ar_0 e^{-at} + \frac{\sigma^2}{a}e^{-at}(1-e^{-at})
    $$

    Simplifying (the $r_0 e^{-at}$ terms cancel):

    $$
    \theta(t) = f'(0,t) + af^M(0,t) + \frac{\sigma^2}{2a}(1 - e^{-at})^2 + \frac{\sigma^2}{a}e^{-at}(1 - e^{-at})
    $$

    Combining the $\sigma^2$ terms:

    $$
    \frac{\sigma^2}{2a}(1-e^{-at})^2 + \frac{\sigma^2}{a}e^{-at}(1-e^{-at}) = \frac{\sigma^2}{2a}(1-e^{-at})\bigl[(1-e^{-at}) + 2e^{-at}\bigr] = \frac{\sigma^2}{2a}(1-e^{-2at})
    $$

    Therefore:

    $$
    \theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    $\square$

---

## Interpretation of Each Term

The formula $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$ has three distinct contributions:

**Term 1: $f'(0,t)$ (forward curve slope).** This captures the "natural drift" of the forward curve. If forward rates are increasing ($f'(0,t) > 0$), the short rate needs additional upward drift to track the rising curve. If the curve is inverted ($f'(0,t) < 0$), the drift is reduced.

**Term 2: $af(0,t)$ (mean-reversion pull).** The mean-reversion mechanism pulls the short rate toward a target. To ensure the model expected rate matches the forward rate, the drift must compensate for this pull, contributing $af(0,t)$.

**Term 3: $\frac{\sigma^2}{2a}(1 - e^{-2at})$ (convexity correction).** This term arises from Jensen's inequality. The bond price $P(0,T) = \mathbb{E}[e^{-\int_0^T r_s\, ds}]$ involves the expectation of an exponential of a Gaussian, which introduces a variance correction. The forward rate equals $\mathbb{E}[r_t]$ minus a convexity adjustment, so $\theta(t)$ must include this correction to produce the correct expected rate.

---

## Verification of Exact Fit

!!! note "Corollary: Exact Fit at Time Zero"
    With $\theta(t)$ defined by the formula above, the Hull-White model satisfies

    $$
    P^{\text{HW}}(0,T) = P^M(0,T) \quad \text{for all } T \geq 0
    $$

???+ note "Proof"
    The affine bond price at $t = 0$ is $P(0,T) = \exp(A(0,T) + B(0,T) r_0)$ where

    $$
    A(0,T) = \ln\frac{P^M(0,T)}{P^M(0,0)} + B(0,T) f(0,0) + \frac{\sigma^2}{4a} B(0,T)^2(1 - e^0)
    $$

    Since $P^M(0,0) = 1$, $f(0,0) = r_0$, and $1 - e^0 = 0$:

    $$
    A(0,T) = \ln P^M(0,T) + B(0,T) r_0
    $$

    Therefore:

    $$
    P(0,T) = \exp(\ln P^M(0,T) + B(0,T) r_0 + B(0,T) r_0) = P^M(0,T) \cdot e^{2B(0,T) r_0}
    $$

    Wait -- this requires careful accounting. Using the standard convention $P(t,T) = \exp(A(t,T) - \hat{B}(t,T) r_t)$ with $\hat{B} = (1-e^{-a\tau})/a > 0$:

    $$
    A(0,T) = \ln P^M(0,T) + \hat{B}(0,T) r_0
    $$

    $$
    P(0,T) = \exp(A(0,T) - \hat{B}(0,T) r_0) = \exp(\ln P^M(0,T) + \hat{B}(0,T) r_0 - \hat{B}(0,T) r_0) = P^M(0,T)
    $$

    $\square$

---

## Numerical Implementation

In practice, the market provides discrete bond prices $P^M(0, T_i)$ for a grid of maturities $T_0 = 0 < T_1 < \cdots < T_n$. The implementation of $\theta(t)$ requires:

**Step 1: Construct the forward curve.** From discrete bond prices, compute the forward rate using finite differences:

$$
f(0, t_i) \approx -\frac{\ln P^M(0, t_{i+1}) - \ln P^M(0, t_i)}{t_{i+1} - t_i}
$$

Alternatively, fit a smooth parametric model (e.g., Nelson-Siegel, Svensson) to the discount curve and differentiate analytically.

**Step 2: Compute the forward curve derivative.** Using the smoothed curve:

$$
f'(0, t_i) \approx \frac{f(0, t_{i+1}) - f(0, t_{i-1})}{t_{i+1} - t_{i-1}}
$$

or use the analytic derivative of the parametric fit.

**Step 3: Evaluate $\theta(t)$.**

$$
\theta(t_i) = f'(0, t_i) + a\, f(0, t_i) + \frac{\sigma^2}{2a}(1 - e^{-2at_i})
$$

!!! warning "Numerical Pitfalls"

    - **Noisy forward curves:** Raw bootstrap of $f(0,t)$ from bond/swap data can be jagged, making $f'(0,t)$ unstable. Smoothing (splines, parametric models) is essential.
    - **Small $a$ limit:** As $a \to 0$, the convexity term $\frac{\sigma^2}{2a}(1-e^{-2at}) \to \sigma^2 t$, which is well-defined. However, the $af(0,t)$ term vanishes, reducing $\theta$ to $f'(0,t) + \sigma^2 t$ (the Ho-Lee drift).
    - **Negative $\theta(t)$:** If the forward curve is steeply inverted ($f'(0,t) \ll 0$), $\theta(t)$ can become negative, which is mathematically valid but means the instantaneous target $\theta(t)/a$ is negative.

---

## Special Case: Flat Forward Curve

!!! example "Flat Forward Curve"
    If $f(0,t) = r_0$ for all $t$ (flat term structure), then $f'(0,t) = 0$ and:

    $$
    \theta(t) = ar_0 + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    As $t \to 0$: $\theta(0) = ar_0$ (pure Vasicek drift).

    As $t \to \infty$: $\theta(\infty) = ar_0 + \frac{\sigma^2}{2a}$ (enhanced by the full convexity correction).

    The convexity correction $\frac{\sigma^2}{2a}(1-e^{-2at})$ starts at zero and monotonically increases to $\frac{\sigma^2}{2a}$, accounting for the growing cumulative effect of volatility on bond prices.

!!! example "Nelson-Siegel Forward Curve"
    For the Nelson-Siegel parameterization $f(0,t) = \beta_0 + \beta_1 e^{-\lambda t} + \beta_2 \lambda t e^{-\lambda t}$, the derivative is

    $$
    f'(0,t) = -\beta_1 \lambda e^{-\lambda t} + \beta_2 \lambda e^{-\lambda t}(1 - \lambda t)
    $$

    and $\theta(t)$ is available in closed form:

    $$
    \theta(t) = (-\beta_1 \lambda + \beta_2 \lambda)e^{-\lambda t} - \beta_2 \lambda^2 t e^{-\lambda t} + a(\beta_0 + \beta_1 e^{-\lambda t} + \beta_2 \lambda t e^{-\lambda t}) + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    This shows that $\theta(t)$ inherits the functional form of the initial curve, with each term weighted by $a$ and augmented by the convexity correction.

---

## The Deterministic Mean Function alpha(t)

The $\theta(t)$ formula also determines the deterministic mean function $\alpha(t)$ that appears in the conditional mean of $r_t$.

!!! note "Corollary: Deterministic Mean"
    The function $\alpha(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1 - e^{-at})^2$ satisfies

    $$
    \alpha'(t) = \theta(t) - a\, \alpha(t)
    $$

    and the conditional mean of $r_t$ given $r_0$ is $\mathbb{E}[r_t \mid r_0] = r_0 e^{-at} + \alpha(t) - \alpha(0) e^{-at}$.

Since $\alpha(0) = f(0,0) = r_0$, this simplifies to $\mathbb{E}[r_t \mid r_0] = \alpha(t)$, confirming that $\alpha(t)$ is the unconditional mean of the short rate at time $t$.

---

## Summary

The Hull-White drift function $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$ is determined analytically by requiring that model bond prices match the market at time zero. The formula involves the forward rate $f(0,t)$, its time derivative $f'(0,t)$, and a convexity correction that grows from zero to $\sigma^2/(2a)$. Numerical implementation requires a smooth forward curve (parametric fitting is recommended) and careful treatment of the derivative $f'(0,t)$. The exact fit property $P^{\text{HW}}(0,T) = P^M(0,T)$ is the key practical advantage over the Vasicek model and is essential for consistent derivative pricing.

---

## Exercises

**Exercise 1.** For a flat forward curve $f(0,t) = 0.04$ with $a = 0.10$ and $\sigma = 0.015$, compute $\theta(t)$ at $t = 0, 1, 5, 20$. Verify that $\theta(0) = a \times 0.04 = 0.004$ and identify the asymptotic value $\theta(\infty)$.

??? success "Solution to Exercise 1"
    With $f(0,t) = 0.04$, $a = 0.10$, $\sigma = 0.015$:

    $$
    \theta(t) = f'(0,t) + a\,f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    Since $f(0,t) = 0.04$ is constant, $f'(0,t) = 0$.

    $$
    \theta(t) = 0.10 \times 0.04 + \frac{(0.015)^2}{2 \times 0.10}(1 - e^{-0.20t}) = 0.004 + 0.001125(1 - e^{-0.20t})
    $$

    **At $t = 0$:** $\theta(0) = 0.004 + 0.001125 \times 0 = 0.004 = a \times 0.04$. Verified.

    **At $t = 1$:** $e^{-0.20} = 0.8187$, so $\theta(1) = 0.004 + 0.001125 \times 0.1813 = 0.004 + 0.000204 = 0.004204$.

    **At $t = 5$:** $e^{-1.0} = 0.3679$, so $\theta(5) = 0.004 + 0.001125 \times 0.6321 = 0.004 + 0.000711 = 0.004711$.

    **At $t = 20$:** $e^{-4.0} = 0.01832$, so $\theta(20) = 0.004 + 0.001125 \times 0.98168 = 0.004 + 0.001104 = 0.005104$.

    **Asymptotic value:** As $t \to \infty$, $e^{-2at} \to 0$:

    $$
    \theta(\infty) = 0.004 + 0.001125 = 0.005125 = ar_0 + \frac{\sigma^2}{2a}
    $$

    | $t$ | $\theta(t)$ |
    |:---:|:---:|
    | 0 | 0.00400 |
    | 1 | 0.00420 |
    | 5 | 0.00471 |
    | 20 | 0.00510 |
    | $\infty$ | 0.00513 |

---

**Exercise 2.** Explain why the convexity correction $\frac{\sigma^2}{2a}(1 - e^{-2at})$ is needed in the formula for $\theta(t)$. Relate it to Jensen's inequality and the difference between $\mathbb{E}[e^{-X}]$ and $e^{-\mathbb{E}[X]}$ for a Gaussian $X$.

??? success "Solution to Exercise 2"
    The convexity correction arises from the nonlinearity of the exponential function in bond pricing.

    The bond price is:

    $$
    P(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\right]
    $$

    The integrated short rate $X = \int_0^T r_s\,ds$ is Gaussian. By Jensen's inequality, since $g(x) = e^{-x}$ is convex:

    $$
    \mathbb{E}[e^{-X}] > e^{-\mathbb{E}[X]}
    $$

    For a Gaussian $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$, the exact relationship is:

    $$
    \mathbb{E}[e^{-X}] = e^{-\mu_X + \frac{1}{2}\sigma_X^2}
    $$

    The gap between $\mathbb{E}[e^{-X}]$ and $e^{-\mathbb{E}[X]}$ is the factor $e^{\frac{1}{2}\sigma_X^2}$, which is always greater than 1.

    This means the model forward rate $f^{\text{model}}(0,t) = -\frac{d}{dt}\ln P(0,t)$ equals $\mathbb{E}[r_t]$ minus a variance correction. To ensure $f^{\text{model}}(0,t) = f^M(0,t)$, the drift $\theta(t)$ must push $\mathbb{E}[r_t]$ above $f^M(0,t)$ by exactly the convexity correction. This is the term $\frac{\sigma^2}{2a}(1 - e^{-2at})$, which grows from 0 to $\frac{\sigma^2}{2a}$ as $t$ increases, reflecting the growing cumulative variance of the integrated short rate.

---

**Exercise 3.** Consider a Nelson-Siegel forward curve with $\beta_0 = 0.05$, $\beta_1 = -0.02$, $\beta_2 = 0.03$, and $\lambda_{\text{NS}} = 0.5$. Compute $\theta(t)$ for the Hull-White model with $a = 0.05$ and $\sigma = 0.01$ at $t = 2$ and $t = 10$.

??? success "Solution to Exercise 3"
    The Nelson-Siegel forward curve is $f(0,t) = \beta_0 + \beta_1 e^{-\lambda_{\text{NS}} t} + \beta_2 \lambda_{\text{NS}} t\,e^{-\lambda_{\text{NS}} t}$ with $\beta_0 = 0.05$, $\beta_1 = -0.02$, $\beta_2 = 0.03$, $\lambda_{\text{NS}} = 0.5$.

    Its derivative is:

    $$
    f'(0,t) = -\beta_1 \lambda_{\text{NS}} e^{-\lambda_{\text{NS}} t} + \beta_2 \lambda_{\text{NS}} e^{-\lambda_{\text{NS}} t}(1 - \lambda_{\text{NS}} t)
    $$

    $$
    = e^{-0.5t}\!\left[(-(-0.02))(0.5) + (0.03)(0.5)(1 - 0.5t)\right] = e^{-0.5t}\!\left[0.01 + 0.015(1 - 0.5t)\right]
    $$

    $$
    = e^{-0.5t}(0.025 - 0.0075t)
    $$

    Hull-White parameters: $a = 0.05$, $\sigma = 0.01$.

    **At $t = 2$:**

    $f(0,2) = 0.05 + (-0.02)e^{-1} + 0.03 \times 0.5 \times 2 \times e^{-1} = 0.05 - 0.007358 + 0.011036 = 0.05368$

    $f'(0,2) = e^{-1}(0.025 - 0.015) = 0.3679 \times 0.01 = 0.003679$

    Convexity: $\frac{(0.01)^2}{0.10}(1 - e^{-0.20}) = 0.001 \times 0.1813 = 0.000181$

    $$
    \theta(2) = 0.003679 + 0.05 \times 0.05368 + 0.000181 = 0.003679 + 0.002684 + 0.000181 = 0.006544
    $$

    **At $t = 10$:**

    $f(0,10) = 0.05 + (-0.02)e^{-5} + 0.03 \times 0.5 \times 10 \times e^{-5} = 0.05 - 0.000135 + 0.001012 = 0.05088$

    $f'(0,10) = e^{-5}(0.025 - 0.075) = 0.006738 \times (-0.05) = -0.000337$

    Convexity: $\frac{(0.01)^2}{0.10}(1 - e^{-1.0}) = 0.001 \times 0.6321 = 0.000632$

    $$
    \theta(10) = -0.000337 + 0.05 \times 0.05088 + 0.000632 = -0.000337 + 0.002544 + 0.000632 = 0.002839
    $$

---

**Exercise 4.** Suppose the forward curve is given at discrete points $f(0, t_i)$ for $i = 0, 1, \ldots, 30$ (annual spacing). Describe two methods for computing $f'(0, t_i)$: (i) central finite differences, (ii) fitting a smooth curve first. Discuss the advantages of each approach.

??? success "Solution to Exercise 4"
    **Method (i): Central finite differences.** Given discrete forward rates $f(0, t_i)$ at annual spacing $\Delta t = 1$:

    $$
    f'(0, t_i) \approx \frac{f(0, t_{i+1}) - f(0, t_{i-1})}{2\Delta t} = \frac{f(0, t_{i+1}) - f(0, t_{i-1})}{2}
    $$

    At the boundaries, use forward/backward differences: $f'(0, t_0) \approx \frac{f(0,t_1) - f(0,t_0)}{\Delta t}$.

    *Advantages:* Simple to implement, no parametric assumptions. *Disadvantages:* Amplifies noise in the data (differentiation is an ill-posed operation). If the bootstrapped $f(0,t_i)$ has noise of magnitude $\epsilon$, the finite difference has error $O(\epsilon/\Delta t)$, which can be large. The resulting $\theta(t)$ may be oscillatory or even negative.

    **Method (ii): Smooth curve fitting.** Fit a parametric model (e.g., Nelson-Siegel or Svensson) or a smoothing spline to the forward rates, then differentiate analytically:

    $$
    f'(0,t) = \frac{d}{dt}f_{\text{fitted}}(0,t)
    $$

    *Advantages:* Produces a smooth $\theta(t)$ that avoids spurious oscillations. The derivative is as smooth as the fitted curve. For Nelson-Siegel, the derivative is available in closed form.

    *Disadvantages:* Introduces model risk from the parametric choice. The fit may not exactly reproduce all market prices, introducing small calibration errors. Overfitting (too many parameters) can reintroduce noise, while underfitting (too few parameters) misses genuine curve features.

    In practice, method (ii) is strongly preferred because the derivative $f'(0,t)$ directly enters $\theta(t)$ and thus the short rate simulation. An oscillatory $\theta(t)$ creates artificial mean-reversion targets, leading to unrealistic short rate paths.

---

**Exercise 5.** Show that in the Ho-Lee limit ($a \to 0$), the formula reduces to $\theta(t) = f'(0,t) + \sigma^2 t$. Verify that this is consistent with the Ho-Lee model $dr_t = \theta(t)\,dt + \sigma\,dW_t$.

??? success "Solution to Exercise 5"
    In the Ho-Lee limit $a \to 0$, we take limits of each term.

    **Term 1:** $f'(0,t)$ is independent of $a$, so it remains $f'(0,t)$.

    **Term 2:** $a \cdot f(0,t) \to 0$ as $a \to 0$.

    **Term 3:** Using the Taylor expansion $e^{-2at} \approx 1 - 2at + 2a^2t^2 - \cdots$ for small $a$:

    $$
    \frac{\sigma^2}{2a}(1 - e^{-2at}) = \frac{\sigma^2}{2a}\!\left[2at - 2a^2t^2 + \cdots\right] = \sigma^2 t - \sigma^2 a t^2 + \cdots \to \sigma^2 t
    $$

    Therefore:

    $$
    \theta(t) \to f'(0,t) + 0 + \sigma^2 t = f'(0,t) + \sigma^2 t
    $$

    **Consistency with Ho-Lee:** The Ho-Lee model is $dr_t = \theta(t)\,dt + \sigma\,dW_t$ (no mean reversion). Its forward rate is $f^{\text{HL}}(0,t) = r_0 + \int_0^t \theta(s)\,ds - \frac{1}{2}\sigma^2 t^2$. Setting $f^{\text{HL}}(0,t) = f^M(0,t)$ and differentiating:

    $$
    \theta(t) = f'(0,t) + \sigma^2 t
    $$

    which matches the $a \to 0$ limit of the Hull-White formula. The $\sigma^2 t$ term is the Ho-Lee convexity correction, which grows linearly without bound (since there is no mean reversion to limit the variance growth).

---

**Exercise 6.** Verify the exact fit by substituting $\theta(t)$ into $P(0,T) = \exp(A(0,T) - \hat{B}(0,T)r_0)$ and showing that $P(0,T) = P^M(0,T)$. Which terms cancel and why?

??? success "Solution to Exercise 6"
    The Hull-White bond price at $t = 0$ is $P(0,T) = e^{A(0,T) - \hat{B}(0,T)r_0}$ where $\hat{B}(0,T) = \frac{1-e^{-aT}}{a}$.

    The function $A(0,T)$ is determined by $\theta(t)$. From the derivation, $A(0,T)$ is constructed so that when $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$:

    $$
    A(0,T) = \ln P^M(0,T) + \hat{B}(0,T) r_0
    $$

    Substituting into the bond price formula:

    $$
    P(0,T) = \exp\!\left(\ln P^M(0,T) + \hat{B}(0,T) r_0 - \hat{B}(0,T) r_0\right) = P^M(0,T)
    $$

    The $\hat{B}(0,T) r_0$ terms cancel exactly, leaving $P(0,T) = P^M(0,T)$.

    **Why the cancellation occurs:** The bond price formula has the form $e^{A - \hat{B}r_0}$. The function $A$ is derived by integrating $\theta(t)$ (which depends on $f(0,t) = -\partial_t \ln P^M(0,t)$) through the Riccati equations. The $\theta$ formula is chosen precisely so that $A$ absorbs the market term structure $\ln P^M(0,T)$ and leaves a residual $\hat{B}r_0$ that cancels with the $-\hat{B}r_0$ from the short rate dependence. This is the defining property that makes $\theta(t)$ unique.

---

**Exercise 7.** Discuss the practical challenges of computing $\theta(t)$ from real market data. What happens when the bootstrapped forward curve has kinks or discontinuities? How do these affect the stability of the short rate simulation?

??? success "Solution to Exercise 7"
    **Kinks in the forward curve:** If the bootstrapped forward curve $f(0,t)$ has kinks (discontinuities in $f'(0,t)$), then $f'(0,t)$ has jumps. Since $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$, $\theta(t)$ inherits these jumps. This causes:

    - Abrupt changes in the mean-reversion target $\theta(t)/a$, creating artificial regime changes in the simulated short rate
    - Discontinuities in the conditional mean $\mathbb{E}[r_t | r_0]$, which may produce unrealistic yield curve dynamics

    **Discontinuities in $f(0,t)$:** If $f(0,t)$ itself is discontinuous (e.g., from a piecewise-constant bootstrap), then $f'(0,t)$ contains Dirac delta functions, making $\theta(t)$ undefined at jump points. In discrete implementations, this manifests as extremely large values of $\theta$ near the discontinuity, causing numerical instability.

    **Practical mitigations:**

    - Smooth the forward curve before computing $\theta(t)$: fit Nelson-Siegel, Svensson, or cubic splines
    - Use monotone or tension splines that avoid spurious oscillations
    - Verify that the smoothed curve reproduces market prices within bid-ask tolerances
    - Monitor $\theta(t)$ for sign changes or extreme values as a diagnostic
    - For Monte Carlo, test that simulated bond prices $\hat{P}(0,T) = \mathbb{E}[e^{-\int_0^T r_s\,ds}]$ match $P^M(0,T)$ to within acceptable error

    The fundamental tension is that differentiation amplifies noise while calibration requires exact derivatives. A smooth parametric curve resolves this but introduces parametric model risk.
