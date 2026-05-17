# Named Functions A(t,T) and B(t,T)

In the Vasicek model the zero-coupon bond price takes the exponential-affine form $P(t,T) = A(t,T)\,e^{-B(t,T)\,r_t}$, where $A$ and $B$ are deterministic functions of time to maturity alone. This factorization is the hallmark of affine term structure models: the entire dependence on the stochastic short rate is captured by the single exponential $e^{-B\,r_t}$, while $A$ absorbs the drift and convexity effects. Deriving closed-form expressions for $A$ and $B$ transforms the bond pricing PDE into explicit algebra, enabling instantaneous computation of prices, yields, forward rates, and sensitivities.

---

## Affine ansatz and the bond pricing PDE

Recall (see [§ Zero-coupon bond pricing](zero_coupon_bond_pricing.md), [§ General affine bond pricing](../../ch15/affine_term_structure/bond_pricing_affine_framework.md)) the bond pricing PDE $f_t + \tfrac{1}{2}\sigma^2 f_{rr} + \kappa(\theta - r)f_r - rf = 0$ with $f(T,r) = 1$, and the affine ansatz $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ with $A(0) = 1$, $B(0) = 0$.

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

Recall (see [§ General affine bond pricing](../../ch15/affine_term_structure/bond_pricing_affine_framework.md), [§ Vasicek-as-affine](../../ch15/examples/vasicek_cir_as_affine.md)) for the embedding into the affine class and the contrast with CIR's Riccati equation.

---

## Summary

The named functions $A(\tau)$ and $B(\tau)$ encode all the information needed for bond pricing in the Vasicek model. The function $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ captures the sensitivity of the bond price to the short rate and saturates at $1/\kappa$ due to mean reversion. The function $\ln A(\tau)$ captures the drift and convexity effects, producing the long-run yield reduction $R_\infty = \theta - \sigma^2/(2\kappa^2)$. Together they deliver the full yield curve, forward rate curve, and all rate sensitivities in closed form.

---

## Exercises

**Exercise 1.** Verify the ODE for $B(\tau)$. Starting from $\dot{B} = 1 - \kappa B$ with $B(0) = 0$, solve using the integrating factor $e^{\kappa\tau}$ and confirm that $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$. Check that $B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2$ for small $\tau$ by Taylor expansion.

??? success "Solution to Exercise 1"
    The ODE is $\dot{B}(\tau) = 1 - \kappa B(\tau)$ with $B(0) = 0$.

    **Solution using integrating factor.** Multiply both sides by $e^{\kappa\tau}$:

    $$
    e^{\kappa\tau}\dot{B} + \kappa e^{\kappa\tau}B = e^{\kappa\tau}
    $$

    The left side is $\frac{d}{d\tau}(e^{\kappa\tau}B)$. Integrating from $0$ to $\tau$:

    $$
    e^{\kappa\tau}B(\tau) - e^0 B(0) = \int_0^\tau e^{\kappa s}\,ds = \frac{1}{\kappa}(e^{\kappa\tau} - 1)
    $$

    Since $B(0) = 0$:

    $$
    B(\tau) = \frac{e^{\kappa\tau} - 1}{\kappa e^{\kappa\tau}} = \frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    **Taylor expansion for small $\tau$.** Using $e^{-\kappa\tau} = 1 - \kappa\tau + \frac{1}{2}\kappa^2\tau^2 - \frac{1}{6}\kappa^3\tau^3 + \cdots$:

    $$
    B(\tau) = \frac{1 - (1 - \kappa\tau + \frac{1}{2}\kappa^2\tau^2 - \frac{1}{6}\kappa^3\tau^3 + \cdots)}{\kappa}
    $$

    $$
    = \frac{\kappa\tau - \frac{1}{2}\kappa^2\tau^2 + \frac{1}{6}\kappa^3\tau^3 - \cdots}{\kappa} = \tau - \frac{1}{2}\kappa\tau^2 + \frac{1}{6}\kappa^2\tau^3 - \cdots
    $$

    For small $\tau$, $B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2$, confirming that $B$ behaves like the time to maturity $\tau$ for short maturities, with a negative correction due to mean reversion.

---

**Exercise 2.** For $\kappa = 0.5$ and $\sigma = 0.02$, compute $B(\tau)$ and $\ln A(\tau)$ at $\tau = 1, 5, 10, 30$ using $\theta = 0.04$. Verify that $B(\tau)/\tau$ decreases monotonically toward $0$ and that $B(\tau) \to 1/\kappa = 2$ as $\tau \to \infty$.

??? success "Solution to Exercise 2"
    With $\kappa = 0.5$, $\sigma = 0.02$, $\theta = 0.04$. We need $\frac{\sigma^2}{2\kappa^2} = \frac{0.0004}{0.50} = 0.0008$ and $\frac{\sigma^2}{4\kappa} = \frac{0.0004}{2.0} = 0.0002$.

    **At $\tau = 1$:**

    $$
    B(1) = \frac{1 - e^{-0.5}}{0.5} = \frac{1 - 0.6065}{0.5} = \frac{0.3935}{0.5} = 0.7869
    $$

    $$
    \ln A(1) = (0.04 - 0.0008)(0.7869 - 1) - 0.0002 \times 0.7869^2 = 0.0392 \times (-0.2131) - 0.0002 \times 0.6192
    $$

    $$
    = -0.008353 - 0.000124 = -0.008477
    $$

    $B(1)/1 = 0.7869$.

    **At $\tau = 5$:**

    $$
    B(5) = \frac{1 - e^{-2.5}}{0.5} = \frac{1 - 0.0821}{0.5} = 1.8358
    $$

    $$
    \ln A(5) = 0.0392 \times (1.8358 - 5) - 0.0002 \times 1.8358^2 = 0.0392 \times (-3.1642) - 0.0002 \times 3.3702
    $$

    $$
    = -0.12404 - 0.000674 = -0.12471
    $$

    $B(5)/5 = 0.3672$.

    **At $\tau = 10$:**

    $$
    B(10) = \frac{1 - e^{-5}}{0.5} = \frac{1 - 0.00674}{0.5} = 1.9865
    $$

    $$
    \ln A(10) = 0.0392 \times (1.9865 - 10) - 0.0002 \times 1.9865^2 = 0.0392 \times (-8.0135) - 0.0002 \times 3.9462
    $$

    $$
    = -0.31413 - 0.000789 = -0.31492
    $$

    $B(10)/10 = 0.1987$.

    **At $\tau = 30$:**

    $$
    B(30) = \frac{1 - e^{-15}}{0.5} \approx \frac{1}{0.5} = 2.0000
    $$

    $$
    \ln A(30) = 0.0392 \times (2.0 - 30) - 0.0002 \times 4.0 = 0.0392 \times (-28.0) - 0.0008 = -1.0976 - 0.0008 = -1.0984
    $$

    $B(30)/30 = 0.0667$.

    The ratio $B(\tau)/\tau$ decreases monotonically: $0.787 \to 0.367 \to 0.199 \to 0.067$, tending to $0$ as $\tau \to \infty$. The function $B(\tau)$ converges to $1/\kappa = 2$.

---

**Exercise 3.** Derive the long-run yield $R_\infty = \theta - \sigma^2/(2\kappa^2)$ by computing $\lim_{\tau \to \infty} R(\tau)$ from the yield formula $R(\tau) = -\ln A(\tau)/\tau + B(\tau)\,r_t/\tau$. Show that the result is independent of $r_t$ and explain why the convexity correction $\sigma^2/(2\kappa^2)$ makes $R_\infty < \theta$.

??? success "Solution to Exercise 3"
    The yield is $R(\tau) = -\ln A(\tau)/\tau + B(\tau)\,r_t/\tau$. As $\tau \to \infty$:

    - $B(\tau) \to 1/\kappa$, so $B(\tau)/\tau \to 0$
    - $B(\tau) - \tau \to 1/\kappa - \tau \to -\infty$, but the ratio $(B(\tau) - \tau)/\tau \to -1$

    For $\ln A(\tau)$:

    $$
    \ln A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
    $$

    As $\tau \to \infty$, $B(\tau) \to 1/\kappa$ and $B(\tau) - \tau \to 1/\kappa - \tau$. The dominant term is:

    $$
    \ln A(\tau) \approx -\left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\tau + \text{bounded terms}
    $$

    Therefore:

    $$
    -\frac{\ln A(\tau)}{\tau} \to \theta - \frac{\sigma^2}{2\kappa^2}
    $$

    and $B(\tau)\,r_t/\tau \to 0$. Combining:

    $$
    R_\infty = \lim_{\tau \to \infty} R(\tau) = \theta - \frac{\sigma^2}{2\kappa^2}
    $$

    The result is **independent of $r_t$**: the long-run yield depends only on model parameters, not on the current rate.

    The **convexity correction** $\sigma^2/(2\kappa^2)$ arises from Jensen's inequality. The bond price is $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}]$. Since $e^{-x}$ is convex, $\mathbb{E}[e^{-X}] > e^{-\mathbb{E}[X]}$. This means bond prices are higher than what the expected rate alone would suggest, which pushes yields below the expected average rate. The correction $\sigma^2/(2\kappa^2)$ quantifies this effect, and since it is positive, $R_\infty < \theta$.

---

**Exercise 4.** The instantaneous forward rate is $f(t,T) = -\partial_T \ln P(t,T)$. Using $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, show that

$$
f(t,T) = e^{-\kappa\tau}\,r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
$$

and verify that $f(t,t) = r_t$ and $\lim_{\tau\to\infty} f(t,T) = R_\infty$.

??? success "Solution to Exercise 4"
    Using $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, we have $\ln P = \ln A(\tau) - B(\tau)r_t$. Since $\tau = T - t$, $\partial_T = \partial_\tau$:

    $$
    f(t,T) = -\frac{\partial}{\partial T}\ln P = -\frac{d(\ln A)}{d\tau} + \frac{dB}{d\tau}\,r_t
    $$

    From the ODE: $\dot{B}(\tau) = e^{-\kappa\tau}$. And:

    $$
    \frac{d(\ln A)}{d\tau} = \frac{1}{2}\sigma^2 B(\tau)^2 - \kappa\theta B(\tau)
    $$

    Therefore:

    $$
    f(t,T) = e^{-\kappa\tau}\,r_t - \frac{1}{2}\sigma^2 B(\tau)^2 + \kappa\theta B(\tau)
    $$

    Now substitute $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$:

    $$
    \kappa\theta B(\tau) = \theta(1 - e^{-\kappa\tau})
    $$

    $$
    \frac{1}{2}\sigma^2 B(\tau)^2 = \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
    $$

    So:

    $$
    f(t,T) = e^{-\kappa\tau}\,r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
    $$

    **Verification at $\tau = 0$:** $f(t,t) = 1 \cdot r_t + 0 - 0 = r_t$. Correct.

    **Verification as $\tau \to \infty$:** $f \to 0 + \theta - \sigma^2/(2\kappa^2) = R_\infty$. Correct.

---

**Exercise 5.** Show that $\partial P/\partial r = -B(\tau)\,P(t,T)$ and $\partial^2 P/\partial r^2 = B(\tau)^2\,P(t,T)$. Explain why $B(\tau)$ plays the role of "duration with respect to the short rate." For what range of $\tau$ is $B(\tau) \approx \tau$ (i.e., when does short-rate duration approximately equal time to maturity)?

??? success "Solution to Exercise 5"
    From $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}$:

    $$
    \frac{\partial P}{\partial r} = A(\tau)\,e^{-B(\tau)\,r_t} \cdot (-B(\tau)) = -B(\tau)\,P(t,T)
    $$

    $$
    \frac{\partial^2 P}{\partial r^2} = -B(\tau) \cdot \frac{\partial P}{\partial r} = -B(\tau) \cdot (-B(\tau)\,P) = B(\tau)^2\,P(t,T)
    $$

    **Duration interpretation.** The "duration with respect to the short rate" is defined as $-\frac{1}{P}\frac{\partial P}{\partial r} = B(\tau)$. This measures the percentage change in bond price per unit change in the short rate.

    For **small $\tau$**, $B(\tau) = (1 - e^{-\kappa\tau})/\kappa \approx \tau - \frac{1}{2}\kappa\tau^2$. When $\kappa\tau \ll 1$ (e.g., $\kappa = 0.5$, $\tau < 0.5$), the quadratic correction is small and $B(\tau) \approx \tau$. In this regime, the short-rate duration approximately equals the time to maturity, just as for the simple duration measure $-\frac{1}{P}\frac{\partial P}{\partial y} \approx \tau$ for a zero-coupon bond.

    The approximation $B(\tau) \approx \tau$ holds well for $\kappa\tau \lesssim 0.3$, i.e., $\tau \lesssim 0.3/\kappa$. For $\kappa = 0.5$, this is $\tau \lesssim 0.6$ years. Beyond this, mean reversion causes $B(\tau)$ to grow more slowly than $\tau$, saturating at $1/\kappa$.

---

**Exercise 6.** In the general one-factor affine framework with $dr_t = (\alpha_0 + \alpha_1 r_t)dt + \sqrt{\beta_0 + \beta_1 r_t}\,dW_t$, the Riccati ODE for $B$ is $\dot{B} = 1 + \alpha_1 B + \frac{1}{2}\beta_1 B^2$. For the Vasicek model ($\beta_1 = 0$), confirm that this reduces to the linear ODE $\dot{B} = 1 - \kappa B$. Why does $\beta_1 = 0$ make the ODE simpler than the CIR case?

??? success "Solution to Exercise 6"
    In the general affine framework, the bond pricing PDE with ansatz $P = e^{A(\tau) - B(\tau)r}$ leads to the Riccati ODE:

    $$
    \dot{B} = 1 + \alpha_1 B + \frac{1}{2}\beta_1 B^2
    $$

    For the **Vasicek model**: $\alpha_1 = -\kappa$ and $\beta_1 = 0$ (constant diffusion). The ODE becomes:

    $$
    \dot{B} = 1 - \kappa B
    $$

    This is a **linear** first-order ODE, solvable by the integrating factor method, yielding $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$.

    Setting $\beta_1 = 0$ eliminates the quadratic term $\frac{1}{2}\beta_1 B^2$, reducing the Riccati equation to a linear equation. This is why the Vasicek model has a simpler $B(\tau)$ than the CIR model.

    For the **CIR model**: $\beta_1 = \sigma^2 > 0$, so the ODE is:

    $$
    \dot{B} = 1 - \kappa B + \frac{1}{2}\sigma^2 B^2
    $$

    This is a genuine **Riccati equation** (quadratic in $B$). Its solution involves $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ and hyperbolic functions:

    $$
    B^{\text{CIR}}(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    The quadratic nonlinearity in the Riccati equation produces this more complex expression, which is a direct consequence of the state-dependent diffusion $\sigma\sqrt{r}$ in the CIR model.

---

**Exercise 7.** Verify the numerical example: for $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $r_0 = 0.03$, compute $P(0,1)$, $P(0,5)$, and $P(0,10)$ step by step. Compare the yields $R(0,\tau) = -\ln P(0,\tau)/\tau$ with the long-run yield $R_\infty$. Is the yield curve upward-sloping, and does it converge to $R_\infty$?

??? success "Solution to Exercise 7"
    With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $r_0 = 0.03$.

    The long-run yield is $R_\infty = 0.04 - 0.0004/(2 \times 0.25) = 0.04 - 0.0008 = 0.0392 = 3.92\%$.

    **$P(0,1)$:** $B(1) = 0.7869$, $\ln A(1) = -0.008477$ (from Exercise 2).

    $$
    P(0,1) = e^{-0.008477 - 0.7869 \times 0.03} = e^{-0.008477 - 0.02361} = e^{-0.03209} = 0.9684
    $$

    $$
    R(0,1) = -\ln(0.9684)/1 = 0.03209 = 3.21\%
    $$

    **$P(0,5)$:** $B(5) = 1.8358$, $\ln A(5) = -0.12471$.

    $$
    P(0,5) = e^{-0.12471 - 1.8358 \times 0.03} = e^{-0.12471 - 0.05507} = e^{-0.17978} = 0.8355
    $$

    $$
    R(0,5) = -\ln(0.8355)/5 = 0.17978/5 = 0.03596 = 3.60\%
    $$

    **$P(0,10)$:** $B(10) = 1.9865$, $\ln A(10) = -0.31492$.

    $$
    P(0,10) = e^{-0.31492 - 1.9865 \times 0.03} = e^{-0.31492 - 0.05960} = e^{-0.37452} = 0.6873
    $$

    $$
    R(0,10) = -\ln(0.6873)/10 = 0.37452/10 = 0.03745 = 3.75\%
    $$

    **Comparison with $R_\infty = 3.92\%$:** The yields are $3.21\% < 3.60\% < 3.75\% < R_\infty = 3.92\%$. The yield curve is **upward-sloping** (since $r_0 = 3\% < R_\infty = 3.92\%$) and converges toward $R_\infty$ from below. The convergence is gradual: even at $\tau = 10$, the yield has not yet reached the asymptotic value, reflecting the slow saturation of $B(\tau)$ toward $1/\kappa = 2$.
