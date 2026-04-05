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

---

## Exercises

**Exercise 1.** Verify the HJM drift condition $\alpha(t,T) = \sigma_f(t,T)\int_t^T \sigma_f(t,u)\,du$ for the Hull-White volatility $\sigma_f(t,T) = \sigma e^{-a(T-t)}$. Compute the integral explicitly and show that $\alpha(t,T) = \frac{\sigma^2}{a}e^{-a(T-t)}(1 - e^{-a(T-t)})$.

??? success "Solution to Exercise 1"
    The HJM drift condition states $\alpha(t,T) = \sigma_f(t,T)\int_t^T \sigma_f(t,u)\,du$. With $\sigma_f(t,T) = \sigma e^{-a(T-t)}$:

    **Step 1:** Compute the integral:

    $$
    \int_t^T \sigma_f(t,u)\,du = \sigma \int_t^T e^{-a(u-t)}\,du
    $$

    Substituting $s = u - t$:

    $$
    = \sigma \int_0^{T-t} e^{-as}\,ds = \sigma\left[-\frac{1}{a}e^{-as}\right]_0^{T-t} = \frac{\sigma}{a}(1 - e^{-a(T-t)})
    $$

    **Step 2:** Multiply by $\sigma_f(t,T)$:

    $$
    \alpha(t,T) = \sigma e^{-a(T-t)} \cdot \frac{\sigma}{a}(1 - e^{-a(T-t)}) = \frac{\sigma^2}{a}e^{-a(T-t)}(1 - e^{-a(T-t)})
    $$

    This confirms the stated formula. The drift is the product of the volatility at maturity $T$ and the cumulative volatility effect integrated over $[t, T]$.

---

**Exercise 2.** Show that the integrated HJM drift $\int_0^t \alpha(s,t)\,ds = \frac{\sigma^2}{2a^2}(1 - e^{-at})^2$. Identify this as the convexity correction in the short rate formula $r_t = f(0,t) + \frac{\sigma^2}{2a^2}(1 - e^{-at})^2 + \sigma\int_0^t e^{-a(t-s)}dW_s$.

??? success "Solution to Exercise 2"
    We need to compute $\int_0^t \alpha(s,t)\,ds$ where $\alpha(s,t) = \frac{\sigma^2}{a}e^{-a(t-s)}(1 - e^{-a(t-s)})$.

    Substituting $v = t - s$ (so $ds = -dv$, and the limits change from $s \in [0,t]$ to $v \in [t,0]$):

    $$
    \int_0^t \alpha(s,t)\,ds = \frac{\sigma^2}{a}\int_0^t e^{-av}(1 - e^{-av})\,dv = \frac{\sigma^2}{a}\int_0^t (e^{-av} - e^{-2av})\,dv
    $$

    Evaluating each integral:

    $$
    \int_0^t e^{-av}\,dv = \frac{1 - e^{-at}}{a}, \qquad \int_0^t e^{-2av}\,dv = \frac{1 - e^{-2at}}{2a}
    $$

    Therefore:

    $$
    \int_0^t \alpha(s,t)\,ds = \frac{\sigma^2}{a}\left[\frac{1 - e^{-at}}{a} - \frac{1 - e^{-2at}}{2a}\right]
    $$

    Simplify using $1 - e^{-2at} = (1 - e^{-at})(1 + e^{-at})$:

    $$
    = \frac{\sigma^2}{a}\cdot\frac{1 - e^{-at}}{a}\left[1 - \frac{1 + e^{-at}}{2}\right] = \frac{\sigma^2}{a}\cdot\frac{1 - e^{-at}}{a}\cdot\frac{1 - e^{-at}}{2} = \frac{\sigma^2}{2a^2}(1 - e^{-at})^2
    $$

    This is the **convexity correction** in the short rate formula

    $$
    r_t = f(0,t) + \frac{\sigma^2}{2a^2}(1 - e^{-at})^2 + \sigma\int_0^t e^{-a(t-s)}dW_s
    $$

    It represents the drift accumulation due to the HJM no-arbitrage condition. The convexity correction grows from $0$ at $t=0$ and saturates at $\sigma^2/(2a^2)$ as $t \to \infty$, reflecting the difference between forward rates and expected future short rates caused by Jensen's inequality in the bond pricing formula.

---

**Exercise 3.** For a flat forward curve $f(0,t) = 0.04$ with $a = 0.1$ and $\sigma = 0.01$, compute $\theta(t)$ at $t = 0, 5, 10, 50$. Verify that $\theta(0) = a \times 0.04 = 0.004$ and identify the long-run limit of $\theta(t)$.

??? success "Solution to Exercise 3"
    With $f(0,t) = 0.04$ (flat), $a = 0.1$, $\sigma = 0.01$:

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + a\,f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    Since $f(0,t) = 0.04$ is constant, $\frac{\partial f(0,t)}{\partial t} = 0$.

    $$
    \theta(t) = 0 + 0.1 \times 0.04 + \frac{0.0001}{0.2}(1 - e^{-0.2t}) = 0.004 + 0.0005(1 - e^{-0.2t})
    $$

    **At $t = 0$:** $\theta(0) = 0.004 + 0.0005 \times 0 = 0.004 = a \times 0.04$. Verified.

    **At $t = 5$:** $\theta(5) = 0.004 + 0.0005(1 - e^{-1.0}) = 0.004 + 0.0005 \times 0.6321 = 0.004316$

    **At $t = 10$:** $\theta(10) = 0.004 + 0.0005(1 - e^{-2.0}) = 0.004 + 0.0005 \times 0.8647 = 0.004432$

    **At $t = 50$:** $\theta(50) = 0.004 + 0.0005(1 - e^{-10.0}) = 0.004 + 0.0005 \times 0.99995 \approx 0.004500$

    **Long-run limit:** As $t \to \infty$, $e^{-2at} \to 0$, so

    $$
    \theta(\infty) = a\,f(0,\infty) + \frac{\sigma^2}{2a} = 0.004 + 0.0005 = 0.0045
    $$

    | $t$ | $\theta(t)$ |
    |:---:|:---:|
    | $0$ | $0.00400$ |
    | $5$ | $0.00432$ |
    | $10$ | $0.00443$ |
    | $50$ | $0.00450$ |
    | $\infty$ | $0.00450$ |

    The slight increase from $0.004$ to $0.0045$ is the convexity correction: even with a flat forward curve, $\theta(t)$ must increase slightly to compensate for the Jensen's inequality effect in bond pricing.

---

**Exercise 4.** Explain why the exponential volatility structure $\sigma_f(t,T) = \sigma e^{-a(T-t)}$ produces a Markov short rate, while a general deterministic volatility $\sigma_f(t,T) = g(t,T)$ does not. What algebraic property of the exponential function is essential?

??? success "Solution to Exercise 4"
    The exponential volatility $\sigma_f(t,T) = \sigma e^{-a(T-t)}$ produces a Markov short rate because of the **separability** of the exponential function: $e^{-a(T-t)} = e^{-aT} \cdot e^{at}$.

    The stochastic integral in the short rate is

    $$
    \sigma\int_0^t e^{-a(t-s)}dW_s = \sigma e^{-at}\int_0^t e^{as}dW_s
    $$

    The key point is that $\int_0^t e^{as}dW_s$ is a single real-valued process. Given $r_t$, the entire history of $W_s$ for $s \leq t$ is not needed to determine the future of $r$; only the current value $r_t$ matters, because the SDE $dr_t = [\theta(t) - ar_t]\,dt + \sigma\,dW_t$ involves only $r_t$ and $t$ in the coefficients.

    **Why a general $\sigma_f(t,T) = g(t,T)$ fails:** For a general deterministic volatility, the short rate is

    $$
    r_t = f(0,t) + \text{(drift terms)} + \int_0^t g(s,t)\,dW_s
    $$

    and the forward rate at maturity $T > t$ is

    $$
    f(t,T) = f(0,T) + \text{(drift terms)} + \int_0^t g(s,T)\,dW_s
    $$

    The forward rate depends on $\int_0^t g(s,T)\,dW_s$, which in general cannot be expressed as a function of $r_t = f(0,t) + \cdots + \int_0^t g(s,t)\,dW_s$ alone, because the "weighting function" $g(s,T)$ differs from $g(s,t)$.

    For the exponential case, $g(s,T) = \sigma e^{-a(T-s)} = e^{-a(T-t)} \cdot \sigma e^{-a(t-s)}$, so $\int_0^t g(s,T)\,dW_s = e^{-a(T-t)}\int_0^t \sigma e^{-a(t-s)}dW_s$, which is a deterministic multiple of the stochastic part of $r_t$. This factorization is the essential algebraic property that produces the Markov property.

---

**Exercise 5.** The Ho-Lee model corresponds to $a = 0$ in the HJM volatility. Derive $\alpha(t,T)$ for the Ho-Lee case by taking the limit $a \to 0$ in the Hull-White drift formula. Show that $\theta(t)$ becomes $f'(0,t) + \sigma^2 t$.

??? success "Solution to Exercise 5"
    For the Ho-Lee model, $\sigma_f(t,T) = \sigma$ (constant), which corresponds to $a = 0$ in the Hull-White volatility. We take the limit $a \to 0$.

    **Drift:** Starting from $\alpha(t,T) = \frac{\sigma^2}{a}e^{-a(T-t)}(1 - e^{-a(T-t)})$, expand for small $a$:

    $$
    e^{-a(T-t)} \approx 1 - a(T-t), \qquad 1 - e^{-a(T-t)} \approx a(T-t)
    $$

    $$
    \alpha(t,T) \approx \frac{\sigma^2}{a}\cdot 1 \cdot a(T-t) = \sigma^2(T-t)
    $$

    This is the Ho-Lee drift: $\alpha^{\text{HL}}(t,T) = \sigma^2(T-t)$.

    **$\theta(t)$ for Ho-Lee:** Taking $a \to 0$ in $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})$:

    The last term: $\frac{\sigma^2}{2a}(1 - e^{-2at}) \approx \frac{\sigma^2}{2a}\cdot 2at = \sigma^2 t$ as $a \to 0$.

    The middle term: $af(0,t) \to 0$ as $a \to 0$.

    Therefore:

    $$
    \theta^{\text{HL}}(t) = f'(0,t) + \sigma^2 t
    $$

    The Ho-Lee SDE is $dr_t = \theta^{\text{HL}}(t)\,dt + \sigma\,dW_t$ (no mean reversion term $-ar_t$, since $a = 0$). The drift function $\theta^{\text{HL}}(t) = f'(0,t) + \sigma^2 t$ grows linearly in $t$ due to the $\sigma^2 t$ convexity correction, which is unbounded -- a well-known drawback of the Ho-Lee model.

---

**Exercise 6.** Starting from the stochastic part $\tilde{r}_t = \sigma\int_0^t e^{-a(t-s)}dW_s$, apply the Leibniz-Ito rule to derive $d\tilde{r}_t = -a\tilde{r}_t\,dt + \sigma\,dW_t$. This verifies that the stochastic component is an Ornstein-Uhlenbeck process.

??? success "Solution to Exercise 6"
    Define $\tilde{r}_t = \sigma\int_0^t e^{-a(t-s)}dW_s$. We can write this as

    $$
    \tilde{r}_t = \sigma e^{-at}\int_0^t e^{as}dW_s
    $$

    Define $Z_t = \int_0^t e^{as}dW_s$, so $\tilde{r}_t = \sigma e^{-at}Z_t$.

    By the product rule (Ito's formula):

    $$
    d\tilde{r}_t = \sigma\,d(e^{-at}Z_t) = \sigma\bigl[-a e^{-at}Z_t\,dt + e^{-at}\,dZ_t\bigr]
    $$

    Since $dZ_t = e^{at}dW_t$:

    $$
    d\tilde{r}_t = \sigma\bigl[-a e^{-at}Z_t\,dt + e^{-at}\cdot e^{at}\,dW_t\bigr] = -a\,\sigma e^{-at}Z_t\,dt + \sigma\,dW_t
    $$

    Recognizing $\sigma e^{-at}Z_t = \tilde{r}_t$:

    $$
    d\tilde{r}_t = -a\,\tilde{r}_t\,dt + \sigma\,dW_t
    $$

    This is the standard Ornstein-Uhlenbeck SDE with mean-reversion speed $a$, long-run mean $0$, volatility $\sigma$, and initial condition $\tilde{r}_0 = 0$. The stochastic component of the Hull-White short rate is therefore a zero-mean OU process, confirming the decomposition $r_t = \psi(t) + \tilde{r}_t$ where $\psi(t)$ is deterministic and $\tilde{r}_t$ is a mean-zero Gaussian process.

---

**Exercise 7.** Consider a two-factor HJM volatility $\sigma_f(t,T) = \sigma_1 e^{-a_1(T-t)} + \sigma_2 e^{-a_2(T-t)}$. Is the resulting short rate process Markov in $r_t$ alone? If not, what is the minimal state vector needed? Discuss how this relates to the two-factor Hull-White model.

??? success "Solution to Exercise 7"
    With the two-factor volatility $\sigma_f(t,T) = \sigma_1 e^{-a_1(T-t)} + \sigma_2 e^{-a_2(T-t)}$, the short rate involves two independent stochastic integrals (assuming two independent Brownian motions $W_1$ and $W_2$):

    $$
    r_t = f(0,t) + \text{(drift terms)} + \sigma_1\int_0^t e^{-a_1(t-s)}dW_{1,s} + \sigma_2\int_0^t e^{-a_2(t-s)}dW_{2,s}
    $$

    **Markov property:** The short rate $r_t$ alone is **not** Markov because knowing $r_t$ does not determine the individual stochastic integrals $X_{1,t} = \sigma_1\int_0^t e^{-a_1(t-s)}dW_{1,s}$ and $X_{2,t} = \sigma_2\int_0^t e^{-a_2(t-s)}dW_{2,s}$ separately. Since $X_{1}$ and $X_{2}$ have different mean-reversion speeds, their future evolution differs, and knowing only their sum $r_t - \psi(t) = X_{1,t} + X_{2,t}$ is insufficient to predict the future.

    **Minimal state vector:** The process $(X_{1,t}, X_{2,t})$ is Markov in $\mathbb{R}^2$, since each component satisfies an independent OU equation:

    $$
    dX_{1,t} = -a_1 X_{1,t}\,dt + \sigma_1\,dW_{1,t}, \qquad dX_{2,t} = -a_2 X_{2,t}\,dt + \sigma_2\,dW_{2,t}
    $$

    The minimal state vector is $(X_{1,t}, X_{2,t})$, which is two-dimensional. Equivalently, the state can be taken as $(r_t, X_{1,t})$ or $(r_t, X_{2,t})$ since $X_{2,t}$ can be recovered from $r_t$ and $X_{1,t}$.

    **Connection to two-factor Hull-White:** This is precisely the two-factor Hull-White model (also known as the G2++ model). The bond price becomes $P(t,T) = \exp(A(t,T) + B_1(t,T)X_{1,t} + B_2(t,T)X_{2,t})$, an affine function of the two-dimensional state. The model can generate imperfect correlations between forward rates at different maturities, resolving the perfect correlation limitation of the one-factor model.

    **Correlation computation:** For the one-factor case with two components summed, using a single Brownian motion, the correlation between forward rate changes at $T_1$ and $T_2$ involves:

    $$
    \text{Var}[\Delta f(t,T_i)] = \int_0^t (\sigma_1 e^{-a_1(T_i-s)} + \sigma_2 e^{-a_2(T_i-s)})^2\,ds
    $$

    With the given parameters $\sigma_1 = 0.008$, $a_1 = 0.02$, $\sigma_2 = 0.005$, $a_2 = 0.30$, $T_1 = 1$, $T_2 = 10$, and assuming two independent factors, the correlation is

    $$
    \rho(T_1,T_2) = \frac{\text{Cov}[\Delta f(t,T_1), \Delta f(t,T_2)]}{\sqrt{\text{Var}[\Delta f(t,T_1)]\cdot\text{Var}[\Delta f(t,T_2)]}}
    $$

    where

    $$
    \text{Cov} = \int_0^t \bigl[\sigma_1^2 e^{-a_1(T_1+T_2-2s)} + \sigma_2^2 e^{-a_2(T_1+T_2-2s)}\bigr]\,ds
    $$

    For large $t$ (stationary regime), this evaluates to

    $$
    \text{Cov} = \frac{\sigma_1^2}{2a_1}e^{-a_1(T_1+T_2-2t)} + \frac{\sigma_2^2}{2a_2}e^{-a_2(T_1+T_2-2t)}
    $$

    The first factor ($a_1 = 0.02$, slow) contributes significantly to both maturities, while the second factor ($a_2 = 0.30$, fast) decays rapidly and contributes mainly to short maturities. This imbalance produces a correlation strictly less than 1, with the exact value depending on the observation horizon $t$. For typical $t$, the correlation between the 1-year and 10-year forward rates is approximately 0.85--0.95, well below the perfect correlation of the one-factor model.
