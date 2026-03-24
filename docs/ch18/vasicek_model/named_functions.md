# Named Functions A(t,T) and B(t,T)

In the Vasicek model the zero-coupon bond price takes the exponential-affine form $P(t,T) = A(t,T)\,e^{-B(t,T)\,r_t}$, where $A$ and $B$ are deterministic functions of time to maturity alone. This factorization is the hallmark of affine term structure models: the entire dependence on the stochastic short rate is captured by the single exponential $e^{-B\,r_t}$, while $A$ absorbs the drift and convexity effects. Deriving closed-form expressions for $A$ and $B$ transforms the bond pricing PDE into explicit algebra, enabling instantaneous computation of prices, yields, forward rates, and sensitivities.

---

## Affine ansatz and the bond pricing PDE

The zero-coupon bond price $P(t,T) = f(t, r_t)$ satisfies the bond pricing PDE derived in the previous section:

$$
f_t + \frac{1}{2}\sigma^2 f_{rr} + \kappa(\theta - r)\,f_r - r\,f = 0
$$

with terminal condition $f(T, r) = 1$ for all $r$. Here $\kappa$, $\theta$, $\sigma$ are the risk-neutral parameters (incorporating the market price of risk).

We seek a solution of the **affine** form

$$
P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}
$$

where $\tau = T - t$ is the time to maturity, $A(\tau) > 0$, and $B(\tau)$ are deterministic functions with initial conditions $A(0) = 1$ and $B(0) = 0$ so that $P(T,T) = 1$.

The key insight is that if the drift and diffusion of the short rate are affine in $r$, then the log-bond price is affine in $r$, and the PDE reduces to ordinary differential equations for $A$ and $B$.

---

## Derivation of B(t,T)

### Substitution into the PDE

Taking $f = A\,e^{-Br}$ and computing the partial derivatives (using $\partial_t \tau = -1$):

$$
f_t = \left(-A'(\tau)\,e^{-B(\tau)r} + A(\tau)\,B'(\tau)\,r\,e^{-B(\tau)r}\right)(-1) \cdot (-1)
$$

More carefully, since $\tau = T - t$ we have $\frac{\partial}{\partial t} = -\frac{d}{d\tau}$. Writing $\dot{A} = dA/d\tau$ and $\dot{B} = dB/d\tau$:

$$
f_t = -\dot{A}\,e^{-Br} + A\,\dot{B}\,r\,e^{-Br}
$$

$$
f_r = -A\,B\,e^{-Br}
$$

$$
f_{rr} = A\,B^2\,e^{-Br}
$$

Substituting into the PDE and dividing through by $A\,e^{-Br} > 0$:

$$
-\frac{\dot{A}}{A} + \dot{B}\,r + \frac{1}{2}\sigma^2 B^2 - \kappa(\theta - r)\,B - r = 0
$$

### Separation by powers of r

Collecting terms in $r$ and terms independent of $r$:

$$
\left(\dot{B} + \kappa B - 1\right) r + \left(-\frac{\dot{A}}{A} + \frac{1}{2}\sigma^2 B^2 - \kappa\theta B\right) = 0
$$

Since this must hold for all $r$, both the coefficient of $r$ and the constant term must vanish separately. This yields two ODEs.

---

### The ODE for B

Setting the coefficient of $r$ to zero:

$$
\dot{B}(\tau) = 1 - \kappa\,B(\tau), \qquad B(0) = 0
$$

This is a first-order linear ODE. Using the integrating factor $e^{\kappa\tau}$:

$$
\frac{d}{d\tau}\!\left(e^{\kappa\tau} B\right) = e^{\kappa\tau}
$$

Integrating from $0$ to $\tau$:

$$
e^{\kappa\tau} B(\tau) = \frac{1}{\kappa}\left(e^{\kappa\tau} - 1\right)
$$

$$
\boxed{B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}}
$$

where $\tau = T - t$.

**Properties of B:**

- $B(0) = 0$, ensuring $P(T,T) = 1$
- $B(\tau) > 0$ for $\tau > 0$, so bond prices decrease in the short rate
- $B(\tau) \to 1/\kappa$ as $\tau \to \infty$ (saturation due to mean reversion)
- $B(\tau) \approx \tau$ for small $\tau$ (behaves like duration for short maturities)
- $\dot{B}(\tau) = e^{-\kappa\tau} > 0$, so $B$ is strictly increasing

---

## Derivation of A(t,T)

Setting the constant term to zero and using $\dot{A}/A = d(\ln A)/d\tau$:

$$
\frac{d}{d\tau}\ln A(\tau) = \frac{1}{2}\sigma^2 B(\tau)^2 - \kappa\theta\,B(\tau), \qquad \ln A(0) = 0
$$

### Integration

Integrating from $0$ to $\tau$:

$$
\ln A(\tau) = \frac{1}{2}\sigma^2 \int_0^\tau B(s)^2\,ds - \kappa\theta \int_0^\tau B(s)\,ds
$$

The required integrals are computed by substituting $B(s) = (1 - e^{-\kappa s})/\kappa$.

**First integral:**

$$
\int_0^\tau B(s)\,ds = \frac{1}{\kappa}\left[\tau - \frac{1}{\kappa}(1 - e^{-\kappa\tau})\right] = \frac{1}{\kappa}\left[\tau - B(\tau)\right]
$$

**Second integral:**

$$
\int_0^\tau B(s)^2\,ds = \frac{1}{\kappa^2}\int_0^\tau \left(1 - e^{-\kappa s}\right)^2 ds = \frac{1}{\kappa^2}\left[\tau - 2\,\frac{1 - e^{-\kappa\tau}}{\kappa} + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right]
$$

$$
= \frac{1}{\kappa^2}\left[\tau - 2B(\tau) + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right]
$$

### Closed-form expression

Combining and simplifying:

$$
\boxed{\ln A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\!\big(B(\tau) - \tau\big) - \frac{\sigma^2}{4\kappa}\,B(\tau)^2}
$$

**Properties of A:**

- $A(0) = 1$, ensuring $P(T,T) = 1$
- $A(\tau) < 1$ when $\theta > \sigma^2/(2\kappa^2)$ (the typical case where the convexity correction is dominated by the drift effect)
- $\ln A$ is always a concave function of $\tau$

---

## Complete bond pricing formula

Assembling the pieces, the Vasicek zero-coupon bond price is

$$
P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}
$$

with

$$
B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
$$

$$
\ln A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}\,B(\tau)^2
$$

**Verification of boundary condition.** At $\tau = 0$: $B(0) = 0$ and $\ln A(0) = 0$, so $P(T,T) = 1 \cdot e^0 = 1$. $\square$

---

## Yield and forward rate formulas

### Continuously compounded yield

The yield $R(t,T) = -\ln P(t,T) / \tau$ is

$$
R(t,T) = -\frac{\ln A(\tau)}{\tau} + \frac{B(\tau)}{\tau}\,r_t
$$

Since $B(\tau)/\tau \to 1$ as $\tau \to 0$ and $B(\tau)/\tau \to 0$ as $\tau \to \infty$, the yield interpolates between the short rate for short maturities and the long-run yield $R_\infty$ for long maturities.

### Long-run yield

As $\tau \to \infty$, $B(\tau) \to 1/\kappa$ and $B(\tau) - \tau \to -\tau + 1/\kappa$, giving

$$
R_\infty = \lim_{\tau \to \infty} R(t,T) = \theta - \frac{\sigma^2}{2\kappa^2}
$$

This is a fundamental result: the asymptotic yield depends on the long-run mean $\theta$ reduced by a **convexity correction** $\sigma^2/(2\kappa^2)$ that arises from Jensen's inequality applied to the exponential discount factor.

### Instantaneous forward rate

The instantaneous forward rate $f(t,T) = -\partial_T \ln P(t,T)$ is

$$
f(t,T) = \dot{B}(\tau)\,r_t - \frac{d}{d\tau}\ln A(\tau)
$$

Substituting the derivatives:

$$
f(t,T) = e^{-\kappa\tau}\,r_t + \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\!\left(1 - e^{-\kappa\tau}\right) + \frac{\sigma^2}{2\kappa}\,B(\tau)\,e^{-\kappa\tau}
$$

which simplifies to

$$
f(t,T) = e^{-\kappa\tau}\,r_t + \theta\!\left(1 - e^{-\kappa\tau}\right) - \frac{\sigma^2}{2\kappa^2}\!\left(1 - e^{-\kappa\tau}\right)^2
$$

The forward rate is the conditional expectation of the future short rate $\mathbb{E}^{\mathbb{Q}}_t[r_T] = \theta + (r_t - \theta)e^{-\kappa\tau}$ minus a convexity adjustment $\frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2$ that increases with maturity.

---

## Sensitivity to the short rate

The partial derivative of the bond price with respect to the current short rate is

$$
\frac{\partial P}{\partial r} = -B(\tau)\,P(t,T)
$$

In relative terms:

$$
\frac{1}{P}\frac{\partial P}{\partial r} = -B(\tau)
$$

Therefore $B(\tau)$ plays the role of the **bond's duration with respect to the short rate**. This is distinct from the Macaulay or modified duration (which measure sensitivity to the yield), but for short maturities where $B(\tau) \approx \tau$, the two coincide.

The second derivative gives the **convexity** with respect to $r$:

$$
\frac{\partial^2 P}{\partial r^2} = B(\tau)^2\,P(t,T)
$$

Since $B(\tau)^2 > 0$, the bond price is a convex function of the short rate, consistent with the general property that discount bond prices are convex in interest rates.

---

## Numerical example

Consider Vasicek parameters $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, and current short rate $r_0 = 0.03$.

**Computing $B(\tau)$ for various maturities:**

| $\tau$ (years) | $B(\tau)$ | $B(\tau)/\tau$ |
|:-:|:-:|:-:|
| 0.25 | 0.2353 | 0.9412 |
| 1 | 0.7869 | 0.7869 |
| 5 | 1.8358 | 0.3672 |
| 10 | 1.9865 | 0.1987 |
| 30 | 2.0000 | 0.0667 |

The ratio $B(\tau)/\tau$ starts near $1$ (short-rate sensitivity dominates) and decays toward $0$ (mean reversion attenuates long-maturity sensitivity). The saturation level is $1/\kappa = 2.0$.

**Computing bond prices:**

| $\tau$ | $B(\tau)$ | $\ln A(\tau)$ | $P(0,\tau)$ | Yield $R$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 0.7869 | $-0.0029$ | 0.9738 | 2.66% |
| 5 | 1.8358 | $-0.0456$ | 0.8996 | 2.12% |
| 10 | 1.9865 | $-0.1118$ | 0.8291 | 1.87% |
| 30 | 2.0000 | $-0.3864$ | 0.6197 | 1.60% |

The long-run yield converges to $R_\infty = \theta - \sigma^2/(2\kappa^2) = 0.04 - 0.0004 = 0.0396 \approx 3.96\%$. With $r_0 = 0.03 < \theta$, the yield curve is upward-sloping for short maturities, then flattens as the convexity correction takes over.

---

## Connection to the general affine framework

The Vasicek model is the simplest member of the affine term structure class. In the general one-factor affine model, the short rate satisfies

$$
dr_t = (\alpha_0 + \alpha_1 r_t)\,dt + \sqrt{\beta_0 + \beta_1 r_t}\,dW_t
$$

and bond prices take the form $P(t,T) = e^{A(\tau) - B(\tau) r_t}$ where $A$ and $B$ solve Riccati ODEs. For Vasicek: $\alpha_0 = \kappa\theta$, $\alpha_1 = -\kappa$, $\beta_0 = \sigma^2$, $\beta_1 = 0$. The Riccati ODE for $B$ is linear (not quadratic) because $\beta_1 = 0$, which is why $B$ has a simple closed form. In contrast, the CIR model has $\beta_1 > 0$, producing a genuinely quadratic Riccati equation and a more complex expression for $B$.

---

## Summary

The named functions $A(\tau)$ and $B(\tau)$ encode all the information needed for bond pricing in the Vasicek model. The function $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ captures the sensitivity of the bond price to the short rate and saturates at $1/\kappa$ due to mean reversion. The function $\ln A(\tau)$ captures the drift and convexity effects, producing the long-run yield reduction $R_\infty = \theta - \sigma^2/(2\kappa^2)$. Together they deliver the full yield curve, forward rate curve, and all rate sensitivities in closed form.

---

## Exercises

**Exercise 1.** Verify the ODE for $B(\tau)$. Starting from $\dot{B} = 1 - \kappa B$ with $B(0) = 0$, solve using the integrating factor $e^{\kappa\tau}$ and confirm that $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$. Check that $B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2$ for small $\tau$ by Taylor expansion.

---

**Exercise 2.** For $\kappa = 0.5$ and $\sigma = 0.02$, compute $B(\tau)$ and $\ln A(\tau)$ at $\tau = 1, 5, 10, 30$ using $\theta = 0.04$. Verify that $B(\tau)/\tau$ decreases monotonically toward $0$ and that $B(\tau) \to 1/\kappa = 2$ as $\tau \to \infty$.

---

**Exercise 3.** Derive the long-run yield $R_\infty = \theta - \sigma^2/(2\kappa^2)$ by computing $\lim_{\tau \to \infty} R(\tau)$ from the yield formula $R(\tau) = -\ln A(\tau)/\tau + B(\tau)\,r_t/\tau$. Show that the result is independent of $r_t$ and explain why the convexity correction $\sigma^2/(2\kappa^2)$ makes $R_\infty < \theta$.

---

**Exercise 4.** The instantaneous forward rate is $f(t,T) = -\partial_T \ln P(t,T)$. Using $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, show that

$$
f(t,T) = e^{-\kappa\tau}\,r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
$$

and verify that $f(t,t) = r_t$ and $\lim_{\tau\to\infty} f(t,T) = R_\infty$.

---

**Exercise 5.** Show that $\partial P/\partial r = -B(\tau)\,P(t,T)$ and $\partial^2 P/\partial r^2 = B(\tau)^2\,P(t,T)$. Explain why $B(\tau)$ plays the role of "duration with respect to the short rate." For what range of $\tau$ is $B(\tau) \approx \tau$ (i.e., when does short-rate duration approximately equal time to maturity)?

---

**Exercise 6.** In the general one-factor affine framework with $dr_t = (\alpha_0 + \alpha_1 r_t)dt + \sqrt{\beta_0 + \beta_1 r_t}\,dW_t$, the Riccati ODE for $B$ is $\dot{B} = 1 + \alpha_1 B + \frac{1}{2}\beta_1 B^2$. For the Vasicek model ($\beta_1 = 0$), confirm that this reduces to the linear ODE $\dot{B} = 1 - \kappa B$. Why does $\beta_1 = 0$ make the ODE simpler than the CIR case?

---

**Exercise 7.** Verify the numerical example: for $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $r_0 = 0.03$, compute $P(0,1)$, $P(0,5)$, and $P(0,10)$ step by step. Compare the yields $R(0,\tau) = -\ln P(0,\tau)/\tau$ with the long-run yield $R_\infty$. Is the yield curve upward-sloping, and does it converge to $R_\infty$?
