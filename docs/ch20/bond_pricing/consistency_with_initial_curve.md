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
