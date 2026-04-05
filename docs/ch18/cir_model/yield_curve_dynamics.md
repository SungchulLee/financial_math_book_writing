# Yield Curve Dynamics Under CIR

The yield curve --- the function mapping maturity $\tau$ to the continuously compounded yield $R(t,T)$ --- summarizes the term structure of interest rates implied by a model at a given instant. Under the CIR model, the yield curve is entirely determined by the current short rate $r_t$ and the three model parameters $\kappa$, $\theta$, $\sigma$. Unlike models with constant volatility, the CIR framework generates yield curves that can be normal (upward-sloping), inverted (downward-sloping), or humped, depending on the relationship between $r_t$ and the model parameters. This section derives the CIR yield and forward rate formulas, classifies the possible yield curve shapes, and analyzes how each parameter affects the term structure.

---

## Yield from the bond price formula

The continuously compounded zero-coupon yield for maturity $\tau = T - t$ is defined by

$$
R(t,T) = -\frac{\ln P(t,T)}{\tau}
$$

Substituting the CIR bond price $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ gives

$$
R(t,T) = -\frac{\ln A(\tau)}{\tau} + \frac{B(\tau)}{\tau}\,r_t
$$

This shows that the CIR yield is an **affine function** of the current short rate $r_t$:

$$
R(t,T) = a(\tau) + b(\tau)\,r_t
$$

where

$$
a(\tau) = -\frac{\ln A(\tau)}{\tau}, \qquad b(\tau) = \frac{B(\tau)}{\tau}
$$

The intercept $a(\tau)$ captures the contribution of mean reversion and the long-run mean $\theta$, while the slope $b(\tau)$ measures the sensitivity of the yield to the current short rate.

!!! tip "Affine yields imply linear risk"
    The affine dependence of yields on $r_t$ means that the entire yield curve shifts in a predictable way when the short rate changes. This property is the hallmark of affine term structure models and greatly simplifies risk management: the duration of any zero-coupon bond is simply $B(\tau)$, the coefficient in the exponential.

---

## Explicit yield formula

Using the closed-form expressions for $A(\tau)$ and $B(\tau)$ from the bond pricing section, the yield components are

$$
b(\tau) = \frac{B(\tau)}{\tau} = \frac{2(e^{\gamma\tau} - 1)}{\tau\left[(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma\right]}
$$

$$
a(\tau) = \frac{2\kappa\theta}{\sigma^2\tau}\left[\ln\frac{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}{2\gamma} - \frac{(\gamma + \kappa)\tau}{2}\right]
$$

where $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ as before.

---

## Short-rate and long-rate limits

### Short-maturity limit

As $\tau \to 0^+$, using $B(\tau) \approx \tau$ and $A(\tau) \approx 1$:

$$
R(t,T) \to r_t
$$

The yield curve starts at the current short rate, which is consistent with the definition of the instantaneous rate.

### Long-maturity limit

As $\tau \to \infty$, both $a(\tau)$ and $b(\tau)$ converge to finite limits. Since $B(\tau) \to B_\infty = 2/(\gamma + \kappa)$ and $\ln A(\tau) \sim -\frac{\kappa\theta(\gamma - \kappa)}{\sigma^2}\tau$, the long-run yield is

$$
R_\infty = \lim_{\tau \to \infty} R(t,T) = \frac{2\kappa\theta}{\gamma + \kappa}
$$

This is a fundamental quantity: it depends only on the model parameters and is independent of the current short rate $r_t$. In particular, all CIR yield curves converge to the same long rate regardless of the starting point.

!!! note "Long rate under CIR vs Vasicek"
    In the Vasicek model, the long rate is $R_\infty^{\text{Vas}} = \theta - \frac{\sigma^2}{2\kappa^2}$, which can be negative for large $\sigma$. The CIR long rate $R_\infty^{\text{CIR}} = \frac{2\kappa\theta}{\gamma + \kappa}$ is always positive (since all parameters are positive), reflecting the non-negativity of CIR rates.

---

## Instantaneous forward rate

The instantaneous forward rate is defined by

$$
f(t,T) = -\frac{\partial}{\partial T}\ln P(t,T)
$$

For the CIR bond price $P = A(\tau)e^{-B(\tau)r_t}$ with $\tau = T - t$:

$$
f(t,T) = -\frac{A'(\tau)}{A(\tau)} + B'(\tau)\,r_t = \kappa\theta\,B(\tau) + B'(\tau)\,r_t
$$

Substituting the expressions for $B(\tau)$ and $B'(\tau) = 1 - \kappa B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2$:

$$
f(t,T) = \kappa\theta\,B(\tau) + \left(1 - \kappa\,B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2\right)r_t
$$

Like the yield, the forward rate is affine in $r_t$. As $\tau \to 0$, $B(\tau) \to 0$ and $f(t,t) = r_t$. As $\tau \to \infty$, $B(\tau) \to B_\infty$ and the forward rate converges to

$$
f_\infty = \kappa\theta\,B_\infty + \left(1 - \kappa\,B_\infty - \frac{1}{2}\sigma^2 B_\infty^2\right)r_t
$$

Since $B_\infty$ is the equilibrium of the Riccati ODE (where $B' = 0$), the coefficient of $r_t$ vanishes, giving

$$
f_\infty = \kappa\theta\,B_\infty = \frac{2\kappa\theta}{\gamma + \kappa} = R_\infty
$$

confirming that the long forward rate equals the long yield.

---

## Classification of yield curve shapes

The CIR yield curve shape depends on the relationship between the current short rate $r_t$ and the long-run yield $R_\infty$. Three cases arise.

### Normal (upward-sloping) curve

When $r_t < R_\infty$, the yield curve rises from $r_t$ at the short end toward $R_\infty$ at the long end. This is the most common shape and corresponds to the situation where the current rate is below its risk-neutral equilibrium. Mean reversion pulls rates upward over time, increasing expected future discounting.

### Inverted (downward-sloping) curve

When $r_t > R_\infty$, the yield curve slopes downward. The current rate exceeds the long-run level, and mean reversion pulls rates down. Long-maturity bonds reflect the expectation of lower future rates and therefore have lower yields.

### Humped curve

When $r_t$ is moderately above $R_\infty$ and the volatility $\sigma$ is sufficiently large, the yield curve can exhibit a hump: it initially rises for short maturities before declining toward $R_\infty$. The hump arises because the convexity effect (which lowers yields) is small at short maturities but grows with $\tau$, eventually dominating the mean-reversion effect.

The condition for a humped curve can be analyzed by studying the derivative $\partial R / \partial \tau$ at $\tau = 0$:

$$
\left.\frac{\partial R}{\partial \tau}\right|_{\tau = 0} = \frac{1}{2}\left(\kappa(\theta - r_t) - \frac{1}{2}\sigma^2 r_t\right) \cdot \frac{1}{r_t}
$$

A positive initial slope (local increase) combined with the long-rate limit below $r_t$ guarantees a hump.

---

## Parameter sensitivity

Each CIR parameter has a distinct effect on the yield curve.

### Speed of mean reversion ($\kappa$)

Increasing $\kappa$ strengthens the pull toward $\theta$, making the yield curve converge to its long-run level more quickly. For a normal curve, higher $\kappa$ steepens the short end. The long rate $R_\infty = 2\kappa\theta/(\gamma + \kappa)$ increases with $\kappa$ (holding other parameters fixed) because faster mean reversion reduces the effective variance of cumulative discounting.

### Long-run mean ($\theta$)

The parameter $\theta$ primarily affects the level of the yield curve. Increasing $\theta$ raises $R_\infty$ and shifts the entire long end upward. Since $a(\tau)$ is proportional to $\kappa\theta$, both the intercept and the long rate scale with $\theta$.

### Volatility ($\sigma$)

Increasing $\sigma$ has two effects:

1. **Convexity effect**: Higher volatility increases the convexity of bond prices, which lowers yields (the Jensen's inequality effect). This is captured by the discriminant $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ growing with $\sigma$.

2. **Long-rate depression**: Since $R_\infty = 2\kappa\theta/(\gamma + \kappa)$ and $\gamma$ increases with $\sigma$, the long rate decreases with volatility. This is the CIR analogue of the Vasicek convexity adjustment.

!!! warning "Convexity effect can invert the curve"
    For sufficiently high volatility, the convexity depression of long yields can invert a curve that would otherwise be normal. This effect is purely model-driven and should be distinguished from market-implied inversions driven by monetary policy expectations.

---

## Numerical example

Consider CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.1$. The discriminant is $\gamma = \sqrt{0.27} \approx 0.5196$.

**Long-run yield**:

$$
R_\infty = \frac{2(0.5)(0.06)}{0.5196 + 0.5} = \frac{0.06}{1.0196} \approx 0.0588
$$

**Yield curve at $r_0 = 0.04$ (normal curve)**:

| Maturity $\tau$ | $B(\tau)$ | $R(0,\tau)$ |
|:---:|:---:|:---:|
| 1 | 0.881 | 4.55% |
| 2 | 1.541 | 4.86% |
| 5 | 1.813 | 5.23% |
| 10 | 1.909 | 5.52% |
| 30 | 1.959 | 5.82% |

The yield curve is monotonically increasing, starting at $r_0 = 4\%$ and approaching $R_\infty \approx 5.88\%$.

**Yield curve at $r_0 = 0.08$ (inverted curve)**:

With the same parameters but $r_0 = 8\%$, the curve starts at 8% and decreases toward 5.88%, producing an inverted shape.

---

## Summary

The CIR yield curve is an affine function of the current short rate, with coefficients $a(\tau)$ and $b(\tau)$ derived from the closed-form bond price formula. The yield starts at $r_t$ for short maturities and converges to the long-run level $R_\infty = 2\kappa\theta/(\gamma + \kappa)$, which is always positive and independent of $r_t$. The curve can be normal, inverted, or humped depending on the position of $r_t$ relative to $R_\infty$ and the magnitude of the volatility-induced convexity effect. The mean-reversion speed $\kappa$ controls convergence rate, $\theta$ controls the level, and $\sigma$ introduces a convexity depression that lowers long yields. These properties make the CIR yield curve flexible enough to capture the main empirical features of term structures while maintaining the constraint of non-negative rates.

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, compute the long-run yield $R_\infty = 2\kappa\theta/(\gamma + \kappa)$. If $r_0 = 0.03$, is the yield curve normal or inverted? If $r_0 = 0.08$?

??? success "Solution to Exercise 1"

    Given $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$:

    $$
    \gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196
    $$

    $$
    R_\infty = \frac{2\kappa\theta}{\gamma + \kappa} = \frac{2(0.5)(0.06)}{0.5196 + 0.5} = \frac{0.06}{1.0196} \approx 5.884\%
    $$

    **If $r_0 = 0.03$:** Since $r_0 = 3\% < R_\infty = 5.88\%$, the yield curve is **normal** (upward-sloping). The curve starts at approximately 3% and rises toward 5.88%.

    **If $r_0 = 0.08$:** Since $r_0 = 8\% > R_\infty = 5.88\%$, the yield curve is **inverted** (downward-sloping). The curve starts at approximately 8% and decreases toward 5.88%.

---

**Exercise 2.** Verify the short-maturity limit by expanding $R(t,T) = a(\tau) + b(\tau)r_t$ for small $\tau$. Use $B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2$ and $\ln A(\tau) \approx -\frac{1}{2}\kappa\theta\tau^2$ (to leading order). Show that $R(t,T) \to r_t$ as $\tau \to 0$.

??? success "Solution to Exercise 2"

    For small $\tau$, use the expansions:

    $$
    B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2 + O(\tau^3)
    $$

    $$
    \ln A(\tau) = -\kappa\theta\int_0^\tau B(s)\,ds \approx -\kappa\theta\int_0^\tau \left(s - \frac{1}{2}\kappa s^2\right)ds = -\kappa\theta\left[\frac{\tau^2}{2} - \frac{\kappa\tau^3}{6}\right]
    $$

    To leading order: $\ln A(\tau) \approx -\frac{1}{2}\kappa\theta\tau^2$.

    Now compute $R(t,T) = -\ln A(\tau)/\tau + B(\tau)r_t/\tau$:

    $$
    R = \frac{\frac{1}{2}\kappa\theta\tau^2}{\tau} + \frac{(\tau - \frac{1}{2}\kappa\tau^2)r_t}{\tau} + O(\tau^2)
    $$

    $$
    = \frac{1}{2}\kappa\theta\tau + r_t\left(1 - \frac{1}{2}\kappa\tau\right) + O(\tau^2)
    $$

    $$
    = r_t + \frac{1}{2}\kappa(\theta - r_t)\tau + O(\tau^2)
    $$

    As $\tau \to 0$: $R(t,T) \to r_t$. $\checkmark$

    The first-order correction $\frac{1}{2}\kappa(\theta - r_t)\tau$ shows that for small maturities, the yield increases if $\theta > r_t$ (normal curve) and decreases if $\theta < r_t$ (inverted curve).

---

**Exercise 3.** The initial slope of the yield curve is $\left.\frac{\partial R}{\partial \tau}\right|_{\tau=0} = \frac{1}{2}\left[\kappa(\theta - r_t) - \frac{1}{2}\sigma^2 r_t\right]/r_t$. For $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, find the value of $r_t$ at which the initial slope is zero. For $r_t$ above this value, the yield curve initially decreases. Is this the same as $R_\infty$?

??? success "Solution to Exercise 3"

    The initial slope is:

    $$
    \left.\frac{\partial R}{\partial \tau}\right|_{\tau=0} = \frac{1}{2}\left[\kappa(\theta - r_t) - \frac{1}{2}\sigma^2 r_t\right] \cdot \frac{1}{r_t}
    $$

    Setting this to zero:

    $$
    \kappa(\theta - r_t) - \frac{1}{2}\sigma^2 r_t = 0
    $$

    $$
    \kappa\theta = (\kappa + \frac{1}{2}\sigma^2)r_t
    $$

    $$
    r_t^* = \frac{\kappa\theta}{\kappa + \frac{1}{2}\sigma^2}
    $$

    With $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$:

    $$
    r_t^* = \frac{0.5 \times 0.06}{0.5 + 0.005} = \frac{0.03}{0.505} \approx 0.05941 = 5.94\%
    $$

    Compare with $R_\infty = 5.88\%$. These are **not** the same: $r_t^* \approx 5.94\% > R_\infty \approx 5.88\%$.

    The critical rate $r_t^*$ for zero initial slope is slightly above $R_\infty$. For $r_t$ between $R_\infty$ and $r_t^*$, the initial slope is positive (yield curve initially rises) but the long rate is below $r_t$, creating the possibility of a humped curve. The difference $r_t^* - R_\infty$ is due to the convexity effect ($\frac{1}{2}\sigma^2 r_t$ term), which creates a gap between the zero-slope condition and the long-rate crossing.

---

**Exercise 4.** Compute the CIR yield curve $R(0, \tau)$ for $\tau \in \{0.5, 1, 2, 5, 10, 20, 30\}$ with $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, and $r_0 = 0.04$. Then recompute with $\sigma = 0.25$ (all other parameters the same). How does the higher volatility affect the long-run yield and the overall shape of the curve?

??? success "Solution to Exercise 4"

    With $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.04$:

    Using $\gamma = 0.5196$ and computing for each $\tau$ (abbreviated computations):

    **Case 1: $\sigma = 0.10$** (computed earlier):

    $R_\infty = 5.88\%$. The yield curve rises from $r_0 = 4\%$ toward 5.88%.

    **Case 2: $\sigma = 0.25$:**

    $$
    \gamma = \sqrt{0.25 + 2(0.0625)} = \sqrt{0.375} \approx 0.6124
    $$

    $$
    R_\infty = \frac{0.06}{0.6124 + 0.5} = \frac{0.06}{1.1124} \approx 5.39\%
    $$

    The long-run yield drops from 5.88% to 5.39% --- a decrease of 49 basis points. This is the **convexity effect**: higher volatility increases the Jensen's inequality correction that depresses long yields. Since $\gamma$ increases with $\sigma$ and appears in the denominator of $R_\infty$, the long rate falls.

    The overall yield curve with $\sigma = 0.25$ is still upward-sloping (since $r_0 = 4\% < R_\infty = 5.39\%$), but it converges to a lower long-run level. The yield at every maturity is lower than with $\sigma = 0.10$, and the curve is flatter at the long end.

---

**Exercise 5.** Show that the CIR long-run yield $R_\infty = 2\kappa\theta/(\gamma + \kappa)$ is always less than $\theta$. (Hint: show $\gamma > \kappa$ and therefore $\gamma + \kappa > 2\kappa$, so $2\kappa\theta/(\gamma + \kappa) < \theta$.) Interpret this inequality: why is the long-run yield always below the long-run mean of the short rate?

??? success "Solution to Exercise 5"

    We need to show $R_\infty = 2\kappa\theta/(\gamma + \kappa) < \theta$.

    Since $\gamma = \sqrt{\kappa^2 + 2\sigma^2} > \sqrt{\kappa^2} = \kappa$ (because $\sigma > 0$):

    $$
    \gamma + \kappa > 2\kappa
    $$

    Therefore:

    $$
    R_\infty = \frac{2\kappa\theta}{\gamma + \kappa} < \frac{2\kappa\theta}{2\kappa} = \theta
    $$

    **Economic interpretation:** The long-run yield $R_\infty$ is the yield on an infinitely long zero-coupon bond. It is below $\theta$ (the long-run mean of the short rate) because of the **convexity effect**: the bond price $P = e^{-\int r\,ds}$ is a convex function of the integrated rate. By Jensen's inequality:

    $$
    \mathbb{E}[e^{-\int r\,ds}] > e^{-\mathbb{E}[\int r\,ds]}
    $$

    This means the expected bond price is higher than it would be if rates were deterministic at their mean, so the yield (negative log of the bond price divided by maturity) is lower than the mean rate. The gap $\theta - R_\infty$ is the convexity adjustment, which increases with volatility $\sigma$.

---

**Exercise 6.** The yield $R(t,T) = a(\tau) + b(\tau)r_t$ is affine in $r_t$. Compute the duration $\partial P/\partial r_t$ for a CIR zero-coupon bond and express it in terms of $B(\tau)$ and $P(t,T)$. If $B(10) = 1.909$ and $P(0,10) = 0.839$, what is the rate sensitivity (DV01) per basis point?

??? success "Solution to Exercise 6"

    The CIR bond price is $P(t,T) = A(\tau)e^{-B(\tau)r_t}$. The sensitivity is:

    $$
    \frac{\partial P}{\partial r_t} = -B(\tau) \cdot A(\tau)e^{-B(\tau)r_t} = -B(\tau) \cdot P(t,T)
    $$

    **DV01** is the change in price per one basis point (0.01% = 0.0001) change in $r_t$:

    $$
    \text{DV01} = -\frac{\partial P}{\partial r_t} \times 0.0001 \times \text{Face} = B(\tau) \cdot P(t,T) \times 0.0001 \times \text{Face}
    $$

    With $B(10) = 1.909$, $P(0,10) = 0.839$, and face value \$1,000,000:

    $$
    \text{DV01} = 1.909 \times 0.839 \times 0.0001 \times 1{,}000{,}000 = 1.602 \times 0.0001 \times 10^6 = \$160.18
    $$

    Each basis point change in the short rate changes the bond value by approximately \$160.

---

**Exercise 7.** A humped yield curve can arise when $r_t$ is moderately above $R_\infty$. For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.15$, compute $R_\infty$. Then find a value of $r_0$ such that the initial slope is positive but $r_0 > R_\infty$, which would indicate a humped curve. Verify by computing the yield at several maturities and identifying the peak.

??? success "Solution to Exercise 7"

    With $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.15$:

    $$
    \gamma = \sqrt{0.09 + 0.045} = \sqrt{0.135} \approx 0.3674
    $$

    $$
    R_\infty = \frac{2(0.3)(0.05)}{0.3674 + 0.3} = \frac{0.03}{0.6674} \approx 4.495\%
    $$

    **Finding $r_0$ for a humped curve:** We need the initial slope to be positive but $r_0 > R_\infty$.

    The initial slope is zero when $r_0 = r_t^* = \kappa\theta/(\kappa + \frac{1}{2}\sigma^2)$:

    $$
    r_t^* = \frac{0.3 \times 0.05}{0.3 + 0.5 \times 0.0225} = \frac{0.015}{0.31125} \approx 4.82\%
    $$

    For a humped curve: $R_\infty < r_0 < r_t^*$, i.e., $4.50\% < r_0 < 4.82\%$.

    Choose $r_0 = 0.046$ (4.6%). Then $R_\infty = 4.50\% < r_0 = 4.60\% < r_t^* = 4.82\%$.

    The initial slope is positive (since $r_0 < r_t^*$), so the curve initially rises. But the long rate $R_\infty = 4.50\%$ is below $r_0 = 4.60\%$, so the curve must eventually decline. This creates a hump.

    **Verification:** Computing yields at several maturities:

    - $R(0, 0.5) \approx 4.62\%$ (slightly above $r_0$, rising)
    - $R(0, 1) \approx 4.63\%$ (near the peak)
    - $R(0, 2) \approx 4.62\%$ (starting to decline)
    - $R(0, 5) \approx 4.56\%$ (declining)
    - $R(0, 10) \approx 4.52\%$ (approaching $R_\infty$)
    - $R(0, 30) \approx 4.50\%$ (very close to $R_\infty$)

    The yield curve peaks at approximately $\tau \approx 1$ year and then declines toward $R_\infty = 4.50\%$, confirming the humped shape. The hump is small (only about 13 basis points above $r_0$) because the window $R_\infty < r_0 < r_t^*$ is narrow.
