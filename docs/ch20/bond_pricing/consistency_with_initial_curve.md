# Consistency with Initial Yield Curve

A short rate model is useful in practice only if it reproduces today's observed bond prices exactly. The Hull-White model achieves this through the time-dependent mean reversion level $\theta^{\mathbb{Q}}(t)$, which is chosen so that the model-implied zero-coupon bond curve $P(0,T)$ matches the market curve $P^M(0,T)$ for every maturity $T$. This section derives the explicit formula for $\theta^{\mathbb{Q}}(t)$ and verifies the consistency condition.

## Why Consistency Matters

In the Vasicek model the parameters $a$, $b$, and $\sigma$ are constants, producing a term structure that generically does not match the observed market curve. A trader using Vasicek would price a 10-year bond at a value different from the quoted market price, creating an immediate arbitrage signal that has nothing to do with the derivative being priced.

Hull and White resolved this by promoting the mean reversion target from a constant $b$ to a deterministic function $\theta^{\mathbb{Q}}(t)$, chosen to absorb the entire initial term structure. The resulting model prices all vanilla bonds correctly at $t = 0$ and can then be used to price derivatives consistently with the market.

## The Consistency Condition

Recall the Hull-White bond price formula derived via expectation:

$$
P(t,T) = A(t,T)\,e^{-B(t,T)\,r(t)}
$$

where

$$\begin{array}{lllll}
\displaystyle
B(t,T)
&=&\displaystyle
\frac{1}{\lambda}\left[1 - e^{-\lambda(T-t)}\right]
\end{array}$$

At time $t = 0$, the model price must equal the market price for every $T > 0$:

$$
P(0,T) = A(0,T)\,e^{-B(0,T)\,r(0)} = P^M(0,T)
$$

This single equation, holding for all $T$, uniquely determines $\theta^{\mathbb{Q}}(t)$.

## Derivation of A(0,T)

!!! info "Proposition: Deterministic Factor at Time Zero"
    Setting $t = 0$ in the bond price formula, the function $A(0,T)$ satisfies

    $$
    \log A(0,T) = \log P^M(0,T) + B(0,T)\,r(0)
    $$

    This is equivalent to requiring that $A(0,T)e^{-B(0,T)r(0)} = P^M(0,T)$ holds identically.

???+ note "Proof"

    From the general formula

    $$\begin{array}{lllll}
    \displaystyle
    A(t,T)
    &=&\displaystyle
    \frac{P^M(0,T)}{P^M(0,t)}\exp\!\left\{B(t,T)f^M(0,t) - \frac{\sigma^2}{4\lambda}B(t,T)^2\left(1 - e^{-2\lambda t}\right)\right\}
    \end{array}$$

    setting $t = 0$ gives $P^M(0,0) = 1$ and $1 - e^{-2\lambda \cdot 0} = 0$, so

    $$
    A(0,T) = P^M(0,T)\,\exp\!\left\{B(0,T)\,f^M(0,0)\right\}
    $$

    Since $r(0) = f^M(0,0)$ (the short rate equals the instantaneous forward rate at time zero), we verify

    $$
    A(0,T)\,e^{-B(0,T)\,r(0)} = P^M(0,T)\,e^{B(0,T)\,r(0)}\,e^{-B(0,T)\,r(0)} = P^M(0,T)
    $$

    confirming exact calibration to the market curve. $\square$

## Determination of the Mean Reversion Level

The function $\theta^{\mathbb{Q}}(t)$ is determined by differentiating the consistency condition with respect to $T$ and matching to the model dynamics.

!!! info "Theorem: Hull-White Mean Reversion Level"
    The time-dependent mean reversion level in the Hull-White model is

    $$
    \theta^{\mathbb{Q}}(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}\left(1 - e^{-2\lambda t}\right)
    $$

    where $f^M(0,t) = -\frac{\partial}{\partial t}\log P^M(0,t)$ is the market instantaneous forward rate.

???+ note "Proof"

    The Hull-White short rate solution gives

    $$\begin{array}{lllll}
    \displaystyle
    \mathbb{E}^{\mathbb{Q}}\!\left[r(t)\right]
    &=&\displaystyle
    r(0)e^{-\lambda t} + \lambda\int_0^t \theta^{\mathbb{Q}}(s)\,e^{-\lambda(t-s)}\,ds
    \end{array}$$

    Meanwhile, the expected short rate must be consistent with the forward rate curve. From the bond price formula, the instantaneous forward rate implied by the model is

    $$\begin{array}{lllll}
    \displaystyle
    f(0,t)
    &=&\displaystyle
    -\frac{\partial}{\partial t}\log P(0,t)
    \end{array}$$

    For the model to match the market, we need $f(0,t) = f^M(0,t)$. Starting from the short rate SDE and using the relation

    $$
    f(0,t) = \mathbb{E}^{\mathbb{Q}}\!\left[r(t)\right] - \frac{1}{2}\frac{\partial V(0,t)}{\partial t}
    $$

    where $V(0,t) = \frac{\sigma^2}{\lambda^2}\!\left[t + \frac{2}{\lambda}e^{-\lambda t} - \frac{1}{2\lambda}e^{-2\lambda t} - \frac{3}{2\lambda}\right]$ is the variance of $\int_0^t r(s)\,ds$, and matching $f(0,t) = f^M(0,t)$, one can solve for $\theta^{\mathbb{Q}}(t)$.

    Alternatively, differentiating the identity $\mathbb{E}^{\mathbb{Q}}[r(t)] = r(0)e^{-\lambda t} + \lambda\int_0^t \theta^{\mathbb{Q}}(s)e^{-\lambda(t-s)}ds$ with respect to $t$:

    $$\begin{array}{lllll}
    \displaystyle
    \frac{d}{dt}\mathbb{E}^{\mathbb{Q}}[r(t)]
    &=&\displaystyle
    -\lambda r(0)e^{-\lambda t} + \lambda\theta^{\mathbb{Q}}(t) - \lambda^2\int_0^t \theta^{\mathbb{Q}}(s)e^{-\lambda(t-s)}ds
    \\[6pt]
    &=&\displaystyle
    \lambda\theta^{\mathbb{Q}}(t) - \lambda\,\mathbb{E}^{\mathbb{Q}}[r(t)]
    \end{array}$$

    Setting the model forward rate equal to $f^M(0,t)$ and using $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$ with the identity $\mathbb{E}^{\mathbb{Q}}[r(t)] = \alpha(t)$, we solve for

    $$
    \theta^{\mathbb{Q}}(t) = \frac{1}{\lambda}\frac{d\alpha}{dt} + \alpha(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}\left(1 - e^{-2\lambda t}\right)
    $$

    $\square$

## Role of Each Term in the Formula for theta(t)

The three terms in $\theta^{\mathbb{Q}}(t)$ each serve a distinct purpose:

1. **$f^M(0,t)$** -- the market instantaneous forward rate. This is the leading-order term that anchors the mean reversion target to the observed term structure.

2. **$\frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t}$** -- a slope correction. When the forward curve is upward-sloping ($\partial f^M/\partial t > 0$), the mean reversion target must overshoot $f^M(0,t)$ to account for the pull-back effect of mean reversion.

3. **$\frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$** -- a convexity correction. Volatility causes the expected discount factor to differ from the discount factor of the expected rate (Jensen's inequality). This term compensates for that effect and grows from zero at $t = 0$ to the asymptotic value $\frac{\sigma^2}{2\lambda^2}$.

## Numerical Example

Consider a market with a flat forward rate $f^M(0,t) = 0.04$ and Hull-White parameters $\lambda = 0.1$, $\sigma = 0.015$. The mean reversion level evaluates to

$$\begin{array}{lllll}
\displaystyle
\theta^{\mathbb{Q}}(t)
&=&\displaystyle
0.04 + \frac{1}{0.1}\times 0 + \frac{0.015^2}{2 \times 0.01}\left(1 - e^{-0.2t}\right)
\;=\;
0.04 + 0.01125\left(1 - e^{-0.2t}\right)
\end{array}$$

At $t = 0$, $\theta^{\mathbb{Q}}(0) = 0.04 = f^M(0,0)$, confirming that the initial short rate equals the forward rate. As $t \to \infty$, $\theta^{\mathbb{Q}}(t) \to 0.04 + 0.01125 = 0.05125$. The convexity correction pushes the long-run mean reversion target above the flat forward rate by approximately 113 basis points.

To verify consistency, the model bond price at $t = 0$ for any maturity $T$ satisfies

$$
P(0,T) = A(0,T)\,e^{-B(0,T)\,r(0)} = e^{-0.04\,T} = P^M(0,T)
$$

exactly matching the market discount factors.

## Connection to the Alpha Function

The consistency condition is closely related to the function $\alpha(t)$ introduced in the short rate solution:

$$
\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}\left(1 - e^{-\lambda t}\right)^2
$$

The mean reversion level $\theta^{\mathbb{Q}}(t)$ can be recovered from $\alpha(t)$ via

$$
\lambda\,\theta^{\mathbb{Q}}(t) = \alpha'(t) + \lambda\,\alpha(t)
$$

This relationship shows that $\alpha(t)$ plays the role of the expected short rate $\mathbb{E}^{\mathbb{Q}}[r(t)]$ starting from $r(0) = f^M(0,0)$, and the entire initial curve is encoded in this single deterministic function.

---

## Summary

The Hull-White model achieves exact consistency with the market zero-coupon bond curve through the time-dependent function $\theta^{\mathbb{Q}}(t)$. This function is uniquely determined by the market instantaneous forward rate $f^M(0,t)$, its derivative, and a convexity correction proportional to $\sigma^2$. At $t = 0$, the bond price formula reduces to $P(0,T) = P^M(0,T)$ for all maturities, ensuring that the model can be used for derivative pricing without introducing spurious arbitrage against observed bond prices.

---

## Exercises

**Exercise 1.** Consider a market with forward rate $f^M(0,t) = 0.03 + 0.002t$ and Hull-White parameters $\lambda = 0.08$, $\sigma = 0.012$. Compute $\theta^{\mathbb{Q}}(t)$ at $t = 0$, $t = 5$, and $t = 20$. Verify that $\theta^{\mathbb{Q}}(0) = f^M(0,0) = 0.03$.

??? success "Solution to Exercise 1"
    The formula for $\theta^{\mathbb{Q}}(t)$ is:

    $$
    \theta^{\mathbb{Q}}(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    With $f^M(0,t) = 0.03 + 0.002t$, we have $\frac{\partial f^M}{\partial t} = 0.002$. Parameters: $\lambda = 0.08$, $\sigma = 0.012$.

    Substituting:

    $$
    \theta^{\mathbb{Q}}(t) = (0.03 + 0.002t) + \frac{0.002}{0.08} + \frac{0.012^2}{2 \times 0.08^2}(1 - e^{-0.16t})
    $$

    $$
    = (0.03 + 0.002t) + 0.025 + \frac{0.000144}{0.0128}(1 - e^{-0.16t})
    $$

    $$
    = 0.055 + 0.002t + 0.01125(1 - e^{-0.16t})
    $$

    **At $t = 0$:**

    $$
    \theta^{\mathbb{Q}}(0) = 0.055 + 0 + 0.01125(1 - 1) = 0.055
    $$

    But wait -- we should verify that $\theta^{\mathbb{Q}}(0) = f^M(0,0) + \frac{1}{\lambda}\frac{\partial f^M}{\partial t} + 0 = 0.03 + 0.025 = 0.055$.

    Note that $\theta^{\mathbb{Q}}(0) \neq f^M(0,0) = 0.03$ in general. The equality $\theta^{\mathbb{Q}}(0) = f^M(0,0)$ holds only when the slope correction vanishes (i.e., $\frac{\partial f^M}{\partial t} = 0$). Here the forward curve is upward-sloping, so $\theta^{\mathbb{Q}}(0) = 0.055 > 0.03$.

    **At $t = 5$:**

    $$
    \theta^{\mathbb{Q}}(5) = 0.055 + 0.01 + 0.01125(1 - e^{-0.8}) = 0.065 + 0.01125(1 - 0.4493)
    $$

    $$
    = 0.065 + 0.01125 \times 0.5507 = 0.065 + 0.006195 \approx 0.07120
    $$

    **At $t = 20$:**

    $$
    \theta^{\mathbb{Q}}(20) = 0.055 + 0.04 + 0.01125(1 - e^{-3.2}) = 0.095 + 0.01125(1 - 0.04076)
    $$

    $$
    = 0.095 + 0.01125 \times 0.9592 = 0.095 + 0.01079 \approx 0.10579
    $$

    The verification that $\theta^{\mathbb{Q}}(0) = f^M(0,0)$ does not hold here because of the nonzero slope term. What is always true is that $\alpha(0) = f^M(0,0) = r(0)$, which ensures $P(0,T) = P^M(0,T)$.

---

**Exercise 2.** Explain why the Vasicek model (constant $b$ instead of $\theta^{\mathbb{Q}}(t)$) generically fails to match the observed term structure. Give a specific numerical example where the Vasicek bond price at $t = 0$ differs from the market price.

??? success "Solution to Exercise 2"
    In the Vasicek model, the short rate follows $dr = a(b - r)dt + \sigma\,dW^{\mathbb{Q}}$ with constant $b$. The bond price is $P(0,T) = e^{A_V(T) - B(T)r(0)}$ where $B(T) = \frac{1-e^{-aT}}{a}$ and:

    $$
    A_V(T) = \left(b - \frac{\sigma^2}{2a^2}\right)(B(T) - T) - \frac{\sigma^2}{4a}B(T)^2
    $$

    This is determined entirely by the three constants $a$, $b$, $\sigma$ and the initial rate $r(0)$. For a generic market curve $P^M(0,T)$, the model-implied curve $P(0,T)$ will not match $P^M(0,T)$ at all maturities because the Vasicek formula has only three free parameters to fit an entire curve.

    **Numerical example:** Let $a = 0.1$, $b = 0.05$, $\sigma = 0.01$, $r(0) = 0.04$. The Vasicek 10-year bond price:

    $$
    B(10) = \frac{1 - e^{-1}}{0.1} = \frac{0.6321}{0.1} = 6.321
    $$

    $$
    A_V(10) = \left(0.05 - \frac{0.0001}{0.02}\right)(6.321 - 10) - \frac{0.0001}{0.4}(6.321)^2
    $$

    $$
    = (0.05 - 0.005)(-3.679) - 0.00025 \times 39.95 = 0.045 \times (-3.679) - 0.009988
    $$

    $$
    = -0.16556 - 0.00999 = -0.17555
    $$

    $$
    P_V(0,10) = e^{-0.17555 - 6.321 \times 0.04} = e^{-0.17555 - 0.25284} = e^{-0.42839} \approx 0.6516
    $$

    If the market curve is flat at $f^M = 0.04$, then $P^M(0,10) = e^{-0.4} \approx 0.6703$. The Vasicek price $0.6516 \neq 0.6703$, a discrepancy of approximately 187 basis points in yield. This mismatch means that the model misprices even vanilla bonds before any derivatives are considered.

---

**Exercise 3.** Show that the convexity correction term $\frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$ is monotonically increasing in $t$ and converges to $\frac{\sigma^2}{2\lambda^2}$ as $t \to \infty$. For $\lambda = 0.1$ and $\sigma = 0.015$, compute this asymptotic value and express it in basis points.

??? success "Solution to Exercise 3"
    Define $g(t) = \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$. Its derivative is:

    $$
    g'(t) = \frac{\sigma^2}{2\lambda^2} \cdot 2\lambda\,e^{-2\lambda t} = \frac{\sigma^2}{\lambda}e^{-2\lambda t}
    $$

    Since $\sigma > 0$, $\lambda > 0$, and $e^{-2\lambda t} > 0$ for all $t$, we have $g'(t) > 0$ for all $t \geq 0$. Therefore $g(t)$ is monotonically increasing.

    **Convergence as $t \to \infty$:** Since $e^{-2\lambda t} \to 0$:

    $$
    \lim_{t \to \infty} g(t) = \frac{\sigma^2}{2\lambda^2}(1 - 0) = \frac{\sigma^2}{2\lambda^2}
    $$

    **Numerical value:** With $\lambda = 0.1$ and $\sigma = 0.015$:

    $$
    \frac{\sigma^2}{2\lambda^2} = \frac{0.000225}{0.02} = 0.01125
    $$

    Converting to basis points: $0.01125 \times 10{,}000 = 112.5$ basis points. This means the long-run convexity correction pushes the mean reversion target approximately 113 basis points above the asymptotic forward rate.

---

**Exercise 4.** Starting from $\lambda\theta^{\mathbb{Q}}(t) = \alpha'(t) + \lambda\alpha(t)$ and the definition $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$, derive the formula for $\theta^{\mathbb{Q}}(t)$ by computing $\alpha'(t)$ explicitly.

??? success "Solution to Exercise 4"
    Starting from:

    $$
    \alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2
    $$

    Compute $\alpha'(t)$:

    $$
    \alpha'(t) = \frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2} \cdot 2(1 - e^{-\lambda t}) \cdot \lambda e^{-\lambda t}
    $$

    $$
    = \frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{\lambda}(1 - e^{-\lambda t})e^{-\lambda t}
    $$

    Now substitute into $\lambda\theta^{\mathbb{Q}}(t) = \alpha'(t) + \lambda\alpha(t)$:

    $$
    \lambda\theta^{\mathbb{Q}}(t) = \frac{\partial f^M}{\partial t} + \frac{\sigma^2}{\lambda}(1 - e^{-\lambda t})e^{-\lambda t} + \lambda f^M(0,t) + \frac{\sigma^2}{2\lambda}(1 - e^{-\lambda t})^2
    $$

    Divide by $\lambda$:

    $$
    \theta^{\mathbb{Q}}(t) = \frac{1}{\lambda}\frac{\partial f^M}{\partial t} + f^M(0,t) + \frac{\sigma^2}{\lambda^2}(1 - e^{-\lambda t})e^{-\lambda t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2
    $$

    Combine the last two terms by factoring out $\frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})$:

    $$
    \frac{\sigma^2}{\lambda^2}(1 - e^{-\lambda t})e^{-\lambda t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2 = \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})\left[2e^{-\lambda t} + 1 - e^{-\lambda t}\right]
    $$

    $$
    = \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})(1 + e^{-\lambda t}) = \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    Therefore:

    $$
    \theta^{\mathbb{Q}}(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    which matches the stated formula.

---

**Exercise 5.** Consider a flat forward rate $f^M(0,t) = r_0$. Show that the slope correction term $\frac{1}{\lambda}\frac{\partial f^M(0,t)}{\partial t}$ vanishes, so that $\theta^{\mathbb{Q}}(t) = r_0 + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$. Interpret why the mean reversion target exceeds the flat forward rate.

??? success "Solution to Exercise 5"
    With $f^M(0,t) = r_0$ (constant), the slope is $\frac{\partial f^M(0,t)}{\partial t} = 0$. Substituting:

    $$
    \theta^{\mathbb{Q}}(t) = r_0 + \frac{1}{\lambda} \cdot 0 + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t}) = r_0 + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    **Interpretation:** Even with a flat forward curve, the mean reversion target $\theta^{\mathbb{Q}}(t)$ exceeds $r_0$. This is a convexity effect arising from Jensen's inequality. The bond price involves $\mathbb{E}[e^{-\int r\,ds}]$, and since the exponential is convex:

    $$
    \mathbb{E}[e^{-\int r\,ds}] \leq e^{-\mathbb{E}[\int r\,ds]}
    $$

    (actually for concave $-e^{-x}$ the inequality reverses, giving $\mathbb{E}[e^{-X}] > e^{-\mathbb{E}[X]}$). To match the market price $P^M(0,T) = e^{-r_0 T}$ despite this convexity, the model must push the expected short rate above $r_0$ so that the combined effect of higher expected rates and the convexity correction produces the correct bond price. The term $\frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$ is precisely the correction needed to offset the Jensen effect.

---

**Exercise 6.** Prove that the consistency condition $P(0,T) = P^M(0,T)$ holds for all $T$ by directly substituting $t = 0$ into $P(t,T) = A(t,T)e^{-B(t,T)r(t)}$ and using $r(0) = f^M(0,0)$.

??? success "Solution to Exercise 6"
    From the general formula with $t = 0$:

    $$
    P(0,T) = A(0,T)e^{-B(0,T)r(0)}
    $$

    **Step 1:** At $t = 0$, $P^M(0,t) = P^M(0,0) = 1$.

    **Step 2:** The factor $1 - e^{-2\lambda t}\big|_{t=0} = 1 - 1 = 0$, so the convexity correction vanishes.

    **Step 3:** Substituting into $A(0,T)$:

    $$
    A(0,T) = \frac{P^M(0,T)}{1}\exp\left\{B(0,T)f^M(0,0) - \frac{\sigma^2}{4\lambda}B(0,T)^2 \cdot 0\right\} = P^M(0,T)\,e^{B(0,T)f^M(0,0)}
    $$

    **Step 4:** Since $r(0) = f^M(0,0)$ (the short rate at time zero equals the instantaneous forward rate):

    $$
    P(0,T) = P^M(0,T)\,e^{B(0,T)f^M(0,0)}\,e^{-B(0,T)r(0)} = P^M(0,T)\,e^{B(0,T)r(0) - B(0,T)r(0)} = P^M(0,T)
    $$

    This holds for every maturity $T > 0$, confirming exact consistency with the initial market curve.

---

**Exercise 7.** Suppose you are given a discrete set of market zero-coupon bond prices $P^M(0, T_i)$ for $T_i = 1, 2, \ldots, 30$. Describe how you would construct $\theta^{\mathbb{Q}}(t)$ in practice. What interpolation or smoothing challenges arise when computing $\frac{\partial f^M(0,t)}{\partial t}$ from discrete data?

??? success "Solution to Exercise 7"
    **Practical construction of $\theta^{\mathbb{Q}}(t)$:**

    1. **Interpolate the discount curve:** From the discrete bond prices $P^M(0,T_i)$, construct a smooth interpolation of $P^M(0,T)$ for all $T \in [0, 30]$. Common methods include cubic spline interpolation of zero rates or the Nelson-Siegel-Svensson parametric form.

    2. **Extract forward rates:** Compute $f^M(0,t) = -\frac{\partial}{\partial t}\log P^M(0,t)$ by differentiating the interpolated curve.

    3. **Compute the derivative:** Obtain $\frac{\partial f^M(0,t)}{\partial t}$ by differentiating $f^M$ a second time (which requires differentiating $\log P^M$ twice).

    4. **Evaluate $\theta^{\mathbb{Q}}(t)$:** Substitute into the formula $\theta^{\mathbb{Q}}(t) = f^M(0,t) + \frac{1}{\lambda}\frac{\partial f^M}{\partial t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$.

    **Interpolation and smoothing challenges:**

    - *Amplification of noise:* Each differentiation amplifies noise in the data. Computing $f^M$ requires one derivative of $\log P^M$, and $\frac{\partial f^M}{\partial t}$ requires a second. Small errors in bond prices are magnified into large oscillations in $\theta^{\mathbb{Q}}(t)$.

    - *Choice of interpolation method:* Linear interpolation of zero rates produces discontinuous forward rates and undefined $\frac{\partial f^M}{\partial t}$. Cubic splines ensure $C^2$ smoothness but can introduce spurious oscillations (Runge phenomenon). Monotone or tension splines can help.

    - *Smoothing vs. fit trade-off:* Aggressive smoothing (e.g., Nelson-Siegel with few parameters) produces stable $\theta^{\mathbb{Q}}(t)$ but may not fit all market prices exactly. Fine-grained interpolation fits perfectly but yields noisy derivatives.

    - *Boundary effects:* At the edges of the data ($T = 1$ and $T = 30$), extrapolation is needed, and derivatives are less reliable.

    In practice, practitioners often use a smoothing spline with a regularization penalty on the second derivative, or the Svensson parametric form, to balance fidelity to market data with stability of $\theta^{\mathbb{Q}}(t)$.
