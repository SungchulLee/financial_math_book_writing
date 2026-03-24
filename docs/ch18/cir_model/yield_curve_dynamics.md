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

---

**Exercise 2.** Verify the short-maturity limit by expanding $R(t,T) = a(\tau) + b(\tau)r_t$ for small $\tau$. Use $B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2$ and $\ln A(\tau) \approx -\frac{1}{2}\kappa\theta\tau^2$ (to leading order). Show that $R(t,T) \to r_t$ as $\tau \to 0$.

---

**Exercise 3.** The initial slope of the yield curve is $\left.\frac{\partial R}{\partial \tau}\right|_{\tau=0} = \frac{1}{2}\left[\kappa(\theta - r_t) - \frac{1}{2}\sigma^2 r_t\right]/r_t$. For $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, find the value of $r_t$ at which the initial slope is zero. For $r_t$ above this value, the yield curve initially decreases. Is this the same as $R_\infty$?

---

**Exercise 4.** Compute the CIR yield curve $R(0, \tau)$ for $\tau \in \{0.5, 1, 2, 5, 10, 20, 30\}$ with $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, and $r_0 = 0.04$. Then recompute with $\sigma = 0.25$ (all other parameters the same). How does the higher volatility affect the long-run yield and the overall shape of the curve?

---

**Exercise 5.** Show that the CIR long-run yield $R_\infty = 2\kappa\theta/(\gamma + \kappa)$ is always less than $\theta$. (Hint: show $\gamma > \kappa$ and therefore $\gamma + \kappa > 2\kappa$, so $2\kappa\theta/(\gamma + \kappa) < \theta$.) Interpret this inequality: why is the long-run yield always below the long-run mean of the short rate?

---

**Exercise 6.** The yield $R(t,T) = a(\tau) + b(\tau)r_t$ is affine in $r_t$. Compute the duration $\partial P/\partial r_t$ for a CIR zero-coupon bond and express it in terms of $B(\tau)$ and $P(t,T)$. If $B(10) = 1.909$ and $P(0,10) = 0.839$, what is the rate sensitivity (DV01) per basis point?

---

**Exercise 7.** A humped yield curve can arise when $r_t$ is moderately above $R_\infty$. For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.15$, compute $R_\infty$. Then find a value of $r_0$ such that the initial slope is positive but $r_0 > R_\infty$, which would indicate a humped curve. Verify by computing the yield at several maturities and identifying the peak.
