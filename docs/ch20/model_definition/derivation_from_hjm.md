# Derivation from HJM Framework

The Heath-Jarrow-Morton (HJM) framework provides the most fundamental approach to interest rate modeling by specifying the dynamics of the entire forward rate curve. The Hull-White model arises as a special case of HJM when the forward rate volatility takes the specific exponentially decaying form $\sigma_f(t,T) = \sigma e^{-a(T-t)}$. This derivation is important because it demonstrates that the Hull-White model is not merely an ad hoc specification but is the unique short-rate model consistent with the HJM framework under this volatility structure. Moreover, the HJM perspective automatically ensures no-arbitrage pricing and makes the role of the initial term structure explicit.

!!! info "Prerequisites"
    - HJM framework: forward rate dynamics, drift condition (Chapter 19)
    - Hull-White SDE and mean reversion (previous section)
    - Stochastic calculus: Ito's formula, stochastic Fubini theorem
    - Instantaneous forward rates and their relationship to bond prices

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the HJM forward rate dynamics and the no-arbitrage drift condition
    2. Specify the Hull-White volatility structure and derive the resulting drift
    3. Extract the short rate dynamics from the forward rate equation via $r_t = f(t,t)$
    4. Identify $\theta(t)$ in terms of the initial forward curve
    5. Verify that the derived SDE matches the Hull-White model

---

## The HJM Framework

The HJM framework models the evolution of the instantaneous forward rate curve $f(t,T)$ for all maturities $T \geq t$ simultaneously.

!!! note "Definition: HJM Forward Rate Dynamics"
    Under the risk-neutral measure $\mathbb{Q}$, the instantaneous forward rate satisfies

    $$
    df(t,T) = \alpha(t,T)\, dt + \sigma_f(t,T)\, dW_t^{\mathbb{Q}}
    $$

    where $\sigma_f(t,T)$ is the forward rate volatility (which may depend on $t$ and $T$ but is assumed deterministic for the Hull-White case) and $\alpha(t,T)$ is the drift.

The fundamental result of the HJM theory is that the no-arbitrage condition uniquely determines the drift in terms of the volatility.

!!! note "Theorem: HJM Drift Condition"
    Under the risk-neutral measure $\mathbb{Q}$, absence of arbitrage requires

    $$
    \alpha(t,T) = \sigma_f(t,T) \int_t^T \sigma_f(t,u)\, du
    $$

    That is, the drift of the forward rate at maturity $T$ is completely determined by the volatility structure.

This is a powerful constraint: choosing the volatility function $\sigma_f(t,T)$ determines the entire model, including the drift, leaving no additional freedom.

---

## Hull-White Volatility Specification

The Hull-White model corresponds to a specific choice of forward rate volatility.

!!! note "Definition: Hull-White Volatility Structure"
    The **Hull-White forward rate volatility** is

    $$
    \sigma_f(t,T) = \sigma\, e^{-a(T-t)}
    $$

    where $\sigma > 0$ is a constant and $a > 0$ is the mean-reversion speed.

This is a deterministic function of $t$ and $T$ that decays exponentially with the time to maturity $T - t$. The economic interpretation is that near-term forward rates are more volatile than distant forward rates, with the rate of decay governed by $a$. When $a = 0$, the volatility is constant across all maturities ($\sigma_f = \sigma$), recovering the Ho-Lee model.

---

## Deriving the Forward Rate Drift

Applying the HJM drift condition to the Hull-White volatility structure yields the forward rate drift.

!!! note "Proposition: Hull-White Forward Rate Drift"
    Under the Hull-White volatility $\sigma_f(t,T) = \sigma e^{-a(T-t)}$, the HJM no-arbitrage drift is

    $$
    \alpha(t,T) = \frac{\sigma^2}{a}\, e^{-a(T-t)}\bigl(1 - e^{-a(T-t)}\bigr)
    $$

???+ note "Proof"
    Apply the HJM drift condition:

    $$
    \alpha(t,T) = \sigma_f(t,T) \int_t^T \sigma_f(t,u)\, du = \sigma\, e^{-a(T-t)} \int_t^T \sigma\, e^{-a(u-t)}\, du
    $$

    Evaluate the integral with the substitution $s = u - t$:

    $$
    \int_t^T \sigma\, e^{-a(u-t)}\, du = \sigma \int_0^{T-t} e^{-as}\, ds = \sigma \left[-\frac{1}{a}\, e^{-as}\right]_0^{T-t} = \frac{\sigma}{a}\bigl(1 - e^{-a(T-t)}\bigr)
    $$

    Therefore:

    $$
    \alpha(t,T) = \sigma\, e^{-a(T-t)} \cdot \frac{\sigma}{a}\bigl(1 - e^{-a(T-t)}\bigr) = \frac{\sigma^2}{a}\, e^{-a(T-t)}\bigl(1 - e^{-a(T-t)}\bigr)
    $$

    $\square$

The complete forward rate dynamics under the Hull-White model are therefore

$$
df(t,T) = \frac{\sigma^2}{a}\, e^{-a(T-t)}\bigl(1 - e^{-a(T-t)}\bigr)\, dt + \sigma\, e^{-a(T-t)}\, dW_t^{\mathbb{Q}}
$$

---

## Extracting the Short Rate

The short rate is the forward rate at the current time: $r_t = f(t,t)$. To extract its dynamics, we integrate the forward rate equation and then evaluate at $T = t$.

!!! note "Theorem: Forward Rate Solution"
    The forward rate at time $t$ for maturity $T$ is

    $$
    f(t,T) = f(0,T) + \int_0^t \alpha(s,T)\, ds + \int_0^t \sigma_f(s,T)\, dW_s^{\mathbb{Q}}
    $$

    where $f(0,T)$ is the initial (market-observed) forward curve.

Setting $T = t$ gives the short rate:

$$
r_t = f(t,t) = f(0,t) + \int_0^t \alpha(s,t)\, ds + \int_0^t \sigma_f(s,t)\, dW_s^{\mathbb{Q}}
$$

We need to compute each integral for the Hull-White volatility.

!!! note "Theorem: Derivation of Hull-White SDE from HJM"
    Starting from the HJM forward rate dynamics with $\sigma_f(t,T) = \sigma e^{-a(T-t)}$, the short rate $r_t = f(t,t)$ satisfies

    $$
    dr_t = \bigl[\theta(t) - a\, r_t\bigr]\, dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    where

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + a\, f(0,t) + \frac{\sigma^2}{2a}\bigl(1 - e^{-2at}\bigr)
    $$

???+ note "Proof"
    **Step 1: Compute the integrated drift.**

    $$
    \int_0^t \alpha(s,t)\, ds = \int_0^t \frac{\sigma^2}{a}\, e^{-a(t-s)}\bigl(1 - e^{-a(t-s)}\bigr)\, ds
    $$

    Substituting $v = t - s$:

    $$
    = \frac{\sigma^2}{a} \int_0^t e^{-av}(1 - e^{-av})\, dv = \frac{\sigma^2}{a} \int_0^t \bigl(e^{-av} - e^{-2av}\bigr)\, dv
    $$

    $$
    = \frac{\sigma^2}{a}\left[\frac{1 - e^{-at}}{a} - \frac{1 - e^{-2at}}{2a}\right] = \frac{\sigma^2}{2a^2}\bigl(1 - e^{-at}\bigr)^2
    $$

    **Step 2: Write the short rate in closed form.**

    $$
    r_t = f(0,t) + \frac{\sigma^2}{2a^2}(1 - e^{-at})^2 + \sigma \int_0^t e^{-a(t-s)}\, dW_s^{\mathbb{Q}}
    $$

    **Step 3: Differentiate to obtain the SDE.**

    Apply Ito's formula to the expression for $r_t$. Define $\psi(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1 - e^{-at})^2$ (the deterministic part) and $\tilde{r}_t = \sigma \int_0^t e^{-a(t-s)}\, dW_s^{\mathbb{Q}}$ (the stochastic part).

    For the deterministic part:

    $$
    \psi'(t) = f'(0,t) + \frac{\sigma^2}{a}\, e^{-at}(1 - e^{-at})
    $$

    For the stochastic integral, apply Ito's formula. Writing $\tilde{r}_t = \sigma \int_0^t e^{-a(t-s)}\, dW_s$, differentiation via the Leibniz-Ito rule gives

    $$
    d\tilde{r}_t = -a\, \tilde{r}_t\, dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    Combining:

    $$
    dr_t = \psi'(t)\, dt + d\tilde{r}_t = \left[f'(0,t) + \frac{\sigma^2}{a}\, e^{-at}(1 - e^{-at}) - a\, \tilde{r}_t\right] dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    Since $r_t = \psi(t) + \tilde{r}_t$, we have $\tilde{r}_t = r_t - \psi(t)$, so $-a\tilde{r}_t = -ar_t + a\psi(t)$. Substituting:

    $$
    dr_t = \left[f'(0,t) + \frac{\sigma^2}{a}\, e^{-at}(1 - e^{-at}) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-at})^2 - a\, r_t\right] dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    Collecting the $\sigma^2$ terms:

    $$
    \frac{\sigma^2}{a}\, e^{-at}(1-e^{-at}) + \frac{\sigma^2}{2a}(1-e^{-at})^2 = \frac{\sigma^2}{2a}(1-e^{-at})\bigl[2e^{-at} + (1-e^{-at})\bigr] = \frac{\sigma^2}{2a}(1-e^{-2at})
    $$

    Therefore:

    $$
    dr_t = \left[\underbrace{f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})}_{\theta(t)} - a\, r_t\right] dt + \sigma\, dW_t^{\mathbb{Q}}
    $$

    $\square$

---

## Uniqueness of the Hull-White Model Under HJM

The derivation establishes a one-to-one correspondence between the volatility specification and the short-rate model.

!!! note "Proposition: Markov Property from HJM"
    The forward rate volatility $\sigma_f(t,T) = \sigma e^{-a(T-t)}$ is the unique deterministic volatility of the separable form $\sigma_f(t,T) = g(t) \cdot h(T-t)$ that produces a Markov short rate process with time-homogeneous diffusion coefficient.

The key structural reason is that the exponential function satisfies $e^{-a(T-t)} = e^{-aT} \cdot e^{at}$, which allows the stochastic integral $\int_0^t \sigma e^{-a(t-s)} dW_s$ to be expressed as a function of a single state variable. This is the Markov property: the future evolution of $r_t$ depends on the past only through the current value $r_t$, not through the entire forward curve history. General HJM models are infinite-dimensional (the state is the entire forward curve), but the Hull-White volatility reduces the state space to one dimension.

---

## The Role of the Initial Forward Curve

The HJM derivation makes the role of the initial term structure particularly transparent. The initial forward curve $f(0,T)$ enters the Hull-White model through $\theta(t)$:

$$
\theta(t) = \frac{\partial f(0,t)}{\partial t} + a\, f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

This formula has three contributions:

1. **$\frac{\partial f(0,t)}{\partial t}$**: the slope of the initial forward curve, capturing the direction in which forward rates are moving at each maturity
2. **$a\, f(0,t)$**: the mean-reversion pull toward the current forward rate level, scaled by the reversion speed
3. **$\frac{\sigma^2}{2a}(1 - e^{-2at})$**: a convexity correction arising from Jensen's inequality, which accounts for the difference between the expected short rate and the forward rate

!!! example "Computing $\theta(t)$ from a Flat Curve"
    For a flat forward curve $f(0,t) = r_0$ for all $t$:

    - $\partial_t f(0,t) = 0$
    - $af(0,t) = ar_0$
    - Convexity correction: $\frac{\sigma^2}{2a}(1 - e^{-2at})$

    Therefore $\theta(t) = ar_0 + \frac{\sigma^2}{2a}(1 - e^{-2at})$. In the long run ($t \to \infty$), $\theta(t) \to ar_0 + \frac{\sigma^2}{2a}$, which slightly exceeds $ar_0$ due to the convexity correction. Setting $\sigma = 0$ gives $\theta(t) = ar_0$ constantly, recovering the Vasicek model with $\theta_{\infty} = r_0$.

---

## Connection to the Forward Rate Dynamics Section

The forward rate dynamics derived here,

$$
df(t,T) = \frac{\sigma^2}{a}\, e^{-a(T-t)}(1 - e^{-a(T-t)})\, dt + \sigma\, e^{-a(T-t)}\, dW_t^{\mathbb{Q}}
$$

are developed in full detail in the section on HJM volatility and drift condition. The instantaneous forward rate section derives the explicit formula for $f(t,T)$ in terms of $r_t$ and the initial curve.

---

## Summary

The Hull-White model emerges from the HJM framework by choosing the forward rate volatility $\sigma_f(t,T) = \sigma e^{-a(T-t)}$. The HJM no-arbitrage drift condition determines $\alpha(t,T) = \frac{\sigma^2}{a} e^{-a(T-t)}(1 - e^{-a(T-t)})$ uniquely, and extracting the short rate via $r_t = f(t,t)$ yields the Hull-White SDE $dr_t = [\theta(t) - ar_t]\, dt + \sigma\, dW_t^{\mathbb{Q}}$ with $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})$. This derivation guarantees no-arbitrage consistency, makes the initial term structure's role explicit through $\theta(t)$, and reveals that the Hull-White model is the unique Markov short-rate model within the HJM class for this volatility structure.
