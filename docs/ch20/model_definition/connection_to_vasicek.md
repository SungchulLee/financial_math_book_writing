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
