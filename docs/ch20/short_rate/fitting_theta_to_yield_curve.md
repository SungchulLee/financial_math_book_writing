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
