# No-Arbitrage Drift Condition

A defining feature of the Heath-Jarrow-Morton (HJM) framework is that **no-arbitrage uniquely determines the drift** of forward rates once their volatility structure is specified. This section provides the complete derivation of this fundamental result.

---

## Setup and Notation

### Forward Rate Dynamics

The HJM framework postulates that instantaneous forward rates follow:

$$
df(t, T) = \alpha(t, T) \, dt + \sigma(t, T) \, dW_t^{\mathbb{Q}}
$$

where:
- $f(t, T)$: forward rate at time $t$ for maturity $T$
- $\alpha(t, T)$: drift (to be determined)
- $\sigma(t, T)$: volatility (modeling input)
- $W_t^{\mathbb{Q}}$: Brownian motion under risk-neutral measure

### Bond Prices from Forward Rates

The zero-coupon bond price is:

$$
P(t, T) = \exp\left(-\int_t^T f(t, u) \, du\right)
$$

### Objective

Find the drift $\alpha(t, T)$ such that discounted bond prices are martingales under $\mathbb{Q}$.

---

## The Martingale Condition

### Risk-Neutral Requirement

Under the risk-neutral measure $\mathbb{Q}$, the discounted bond price must be a martingale:

$$
\frac{P(t, T)}{B_t} \text{ is a } \mathbb{Q}\text{-martingale}
$$

where $B_t = \exp\left(\int_0^t r_s \, ds\right)$ is the money-market account, and $r_t = f(t, t)$ is the short rate.

### Equivalent Condition

Taking logs, define:

$$
Z(t, T) := \log P(t, T) = -\int_t^T f(t, u) \, du
$$

The martingale condition on $P(t, T)/B_t$ translates to conditions on the dynamics of $Z(t, T)$.

---

## Dynamics of the Log Bond Price

### Computing dZ(t, T)

We need to find $dZ(t, T)$ where:

$$
Z(t, T) = -\int_t^T f(t, u) \, du
$$

**Step 1:** Differentiate with respect to $t$

Using Leibniz's rule for stochastic integrals:

$$
dZ(t, T) = f(t, t) \, dt - \int_t^T df(t, u) \, du
$$

The first term comes from the lower limit moving, and the second from the integrand changing.

**Step 2:** Substitute forward rate dynamics

$$
df(t, u) = \alpha(t, u) \, dt + \sigma(t, u) \, dW_t
$$

So:

$$
dZ(t, T) = f(t, t) \, dt - \int_t^T \alpha(t, u) \, du \, dt - \int_t^T \sigma(t, u) \, du \, dW_t
$$

**Step 3:** Write compactly

$$
dZ(t, T) = \left[r_t - \int_t^T \alpha(t, u) \, du\right] dt - \left[\int_t^T \sigma(t, u) \, du\right] dW_t
$$

Define the **bond volatility**:

$$
\Sigma(t, T) := \int_t^T \sigma(t, u) \, du
$$

Then:

$$
dZ(t, T) = \left[r_t - \int_t^T \alpha(t, u) \, du\right] dt - \Sigma(t, T) \, dW_t
$$

---

## Dynamics of the Bond Price

### Applying Itô's Lemma

Since $P(t, T) = e^{Z(t, T)}$, by Itô's lemma:

$$
dP(t, T) = P(t, T) \left[dZ + \frac{1}{2}(dZ)^2\right]
$$

The quadratic variation is:

$$
(dZ)^2 = \Sigma(t, T)^2 \, dt
$$

So:

$$
dP(t, T) = P(t, T) \left[\left(r_t - \int_t^T \alpha(t, u) \, du + \frac{1}{2}\Sigma(t, T)^2\right) dt - \Sigma(t, T) \, dW_t\right]
$$

---

## The Discounted Bond Price

### Dynamics of P(t, T)/B_t

Let $\tilde{P}(t, T) = P(t, T)/B_t$. Using the product rule:

$$
d\tilde{P} = \frac{1}{B_t} dP - \frac{P}{B_t^2} dB = \frac{1}{B_t}\left[dP - r_t P \, dt\right]
$$

Substituting:

$$
d\tilde{P} = \tilde{P} \left[\left(-\int_t^T \alpha(t, u) \, du + \frac{1}{2}\Sigma(t, T)^2\right) dt - \Sigma(t, T) \, dW_t\right]
$$

### Martingale Condition

For $\tilde{P}(t, T)$ to be a martingale, the drift must vanish:

$$
-\int_t^T \alpha(t, u) \, du + \frac{1}{2}\Sigma(t, T)^2 = 0
$$

---

## Deriving the Drift Condition

### From Integral Condition to Pointwise Condition

From:

$$
\int_t^T \alpha(t, u) \, du = \frac{1}{2}\Sigma(t, T)^2
$$

Differentiate with respect to $T$:

$$
\alpha(t, T) = \frac{\partial}{\partial T}\left[\frac{1}{2}\Sigma(t, T)^2\right]
$$

Since $\Sigma(t, T) = \int_t^T \sigma(t, u) \, du$:

$$
\frac{\partial \Sigma(t, T)}{\partial T} = \sigma(t, T)
$$

Using the chain rule:

$$
\frac{\partial}{\partial T}\left[\frac{1}{2}\Sigma(t, T)^2\right] = \Sigma(t, T) \cdot \frac{\partial \Sigma(t, T)}{\partial T} = \Sigma(t, T) \cdot \sigma(t, T)
$$

### The HJM Drift Condition

$$
\boxed{\alpha(t, T) = \sigma(t, T) \int_t^T \sigma(t, u) \, du}
$$

Or equivalently:

$$
\boxed{\alpha(t, T) = \sigma(t, T) \cdot \Sigma(t, T)}
$$

where $\Sigma(t, T) = \int_t^T \sigma(t, u) \, du$.

---

## QuantPie Alternative Proof: Zero-Coupon Bond Dynamics

### ZCB Dynamics

An alternative derivation uses the dynamics of zero-coupon bonds directly. Since $f(t,T) = -\frac{d}{dT}\log P(t,T)$:

$$
df(t,T) = -\frac{d}{dT}d\log P(t,T)
$$

The log bond price satisfies:

$$
d\log P(t,T) = \frac{1}{P(t,T)}dP(t,T) - \frac{1}{2}\frac{1}{P(t,T)^2}(dP(t,T))^2
$$

### Bond Volatility Structure

Under risk-neutral pricing, the bond price dynamics are:

$$
\frac{dP(t,T)}{P(t,T)} = r(t)dt + \sigma_P(t,T)dW^{\mathbb{Q}}(t)
$$

where the bond volatility is:

$$
\sigma_P(t,T) = -\int_t^T\sigma(t,T')dT'
$$

### Deriving Forward Rate Dynamics

Applying Itô's lemma:

$$
d\log P(t,T) = \left(r(t) - \frac{1}{2}\sigma_P^2(t,T)\right)dt + \sigma_P(t,T)dW^{\mathbb{Q}}(t)
$$

Taking the derivative with respect to $T$:

$$
df(t,T) = -\frac{d}{dT}d\log P(t,T) = \frac{1}{2}\frac{d\sigma_P^2(t,T)}{dT}dt - \frac{d\sigma_P(t,T)}{dT}dW^{\mathbb{Q}}(t)
$$

### Computing Derivatives

Since $\sigma_P(t,T) = -\int_t^T\sigma(t,T')dT'$:

$$
\frac{d\sigma_P(t,T)}{dT} = -\sigma(t,T)
$$

$$
\frac{d\sigma_P^2(t,T)}{dT} = 2\sigma_P(t,T)\frac{d\sigma_P(t,T)}{dT} = -2\sigma_P(t,T)\sigma(t,T)
$$

### Final Result

$$
df(t,T) = \sigma(t,T)\left(\int_t^T\sigma(t,T')dT'\right)dt + \sigma(t,T)dW^{\mathbb{Q}}(t)
$$

This gives:

$$
\mu^{\mathbb{Q}}(t,T) = \sigma(t,T)\int_t^T\sigma(t,T')dT'
$$

This confirms the HJM no-arbitrage drift condition through an alternative approach based on ZCB dynamics.

---

## Interpretation

### Drift is Determined by Volatility

The key insight is:

> **In the HJM framework, once you specify the volatility structure $\sigma(t, T)$, the drift $\alpha(t, T)$ is uniquely determined by no-arbitrage.**

This is analogous to:
- Black-Scholes: drift of stock under $\mathbb{Q}$ is $r$ (determined)
- Girsanov: drift adjustment absorbs market price of risk

### Volatility is the Modeling Choice

The modeler chooses $\sigma(t, T)$, which controls:
- How different maturities move together
- The shape of yield curve dynamics
- Complexity vs. tractability

The drift follows automatically.

---

## Multi-Factor Extension

### n-Factor HJM

With $n$ driving Brownian motions:

$$
df(t, T) = \alpha(t, T) \, dt + \sum_{i=1}^n \sigma_i(t, T) \, dW_t^i
$$

The drift condition becomes:

$$
\boxed{\alpha(t, T) = \sum_{i=1}^n \sigma_i(t, T) \int_t^T \sigma_i(t, u) \, du}
$$

Each factor contributes independently to the drift.

---

## Verification: Recovering Known Models

### Ho-Lee Model

**Volatility:** $\sigma(t, T) = \sigma$ (constant)

**Drift:**

$$
\alpha(t, T) = \sigma \int_t^T \sigma \, du = \sigma^2 (T - t)
$$

This matches the Ho-Lee forward rate dynamics.

### Hull-White (Extended Vasicek)

**Volatility:** $\sigma(t, T) = \sigma e^{-\kappa(T-t)}$

**Drift:**

$$
\alpha(t, T) = \sigma e^{-\kappa(T-t)} \int_t^T \sigma e^{-\kappa(u-t)} \, du
$$

$$
= \sigma e^{-\kappa(T-t)} \cdot \sigma \cdot \frac{1 - e^{-\kappa(T-t)}}{\kappa}
$$

$$
= \frac{\sigma^2}{\kappa} e^{-\kappa(T-t)}(1 - e^{-\kappa(T-t)})
$$

This recovers the Hull-White forward rate drift.

---

## Consequences of the Drift Condition

### Initial Curve is Matched

By construction, the HJM model:
- Starts with $f(0, T)$ given by market data
- Evolves $f(t, T)$ according to the SDE
- Satisfies no-arbitrage at all times

**Exact fit to the initial yield curve is automatic.**

### Market Price of Risk Absorbed

Under the physical measure $\mathbb{P}$:

$$
df(t, T) = \alpha^{\mathbb{P}}(t, T) \, dt + \sigma(t, T) \, dW_t^{\mathbb{P}}
$$

The risk-neutral drift differs by the market price of risk:

$$
\alpha(t, T) = \alpha^{\mathbb{P}}(t, T) - \lambda(t) \sigma(t, T)
$$

The HJM condition pins down the $\mathbb{Q}$-drift; $\mathbb{P}$-drift requires additional specification.

### Bond Price Volatility

The bond price dynamics are:

$$
\frac{dP(t, T)}{P(t, T)} = r_t \, dt - \Sigma(t, T) \, dW_t
$$

where $\Sigma(t, T) = \int_t^T \sigma(t, u) \, du$ is the bond volatility.

---

## Practical Implications

### Model Specification

1. **Choose volatility structure** $\sigma(t, T)$ based on:
   - Analytical tractability
   - Calibration to market data
   - Economic intuition

2. **Drift follows automatically** from:

   $$\alpha(t, T) = \sigma(t, T) \int_t^T \sigma(t, u) \, du$$

3. **Implement** via:
   - Closed-form solutions (if available)
   - Monte Carlo simulation
   - Finite differences

### Calibration Focus

Since drift is determined, calibration focuses on:
- Volatility parameters
- Factor structure
- Correlation patterns

### Stability Considerations

The drift condition involves **integration**, which smooths out volatility irregularities. However:
- Numerical integration must be accurate
- Discontinuous volatilities can cause issues
- Maturity-dependent regularization may be needed

---

## Summary of Derivation

| Step | Result |
|------|--------|
| 1. Forward rate SDE | $df(t,T) = \alpha(t,T)dt + \sigma(t,T)dW_t$ |
| 2. Bond price from forwards | $P(t,T) = \exp(-\int_t^T f(t,u)du)$ |
| 3. Log bond price dynamics | $dZ = (r_t - \int_t^T \alpha du)dt - \Sigma dW_t$ |
| 4. Discounted bond dynamics | $d\tilde{P}/\tilde{P} = (-\int_t^T \alpha du + \frac{1}{2}\Sigma^2)dt - \Sigma dW_t$ |
| 5. Martingale condition | $-\int_t^T \alpha du + \frac{1}{2}\Sigma^2 = 0$ |
| 6. Differentiate in $T$ | $\alpha(t,T) = \sigma(t,T)\Sigma(t,T)$ |

---

## Key Takeaways

- HJM drift condition: $\alpha(t, T) = \sigma(t, T) \int_t^T \sigma(t, u) \, du$
- Derived from the requirement that discounted bonds are martingales
- Volatility is the modeling input; drift is the consequence
- Initial yield curve fit is automatic
- Multi-factor extension: sum over factors
- Known models (Ho-Lee, Hull-White) are recovered as special cases
- Alternative ZCB-based proof confirms the result

---

## Further Reading

- Heath, Jarrow & Morton (1992), "Bond Pricing and the Term Structure of Interest Rates: A New Methodology"
- Björk, *Arbitrage Theory in Continuous Time*, Chapter 25
- Filipović, *Term-Structure Models*, Chapter 7

---

## Exercises

**Exercise 1.** Starting from the log bond price $Z(t, T) = -\int_t^T f(t, u)\,du$, apply Leibniz's rule to verify that

$$
dZ(t, T) = r_t\,dt - \int_t^T \alpha(t, u)\,du\,dt - \Sigma(t, T)\,dW_t
$$

where $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$. Carefully explain the origin of the $r_t\,dt$ term from the moving lower limit of integration.

??? success "Solution to Exercise 1"

    We start from $Z(t, T) = -\int_t^T f(t, u)\,du$ and apply the stochastic Leibniz rule to compute $dZ(t, T)$.

    **The stochastic Leibniz rule.** For $Z(t, T) = -\int_t^T f(t, u)\,du$ where the integrand evolves stochastically and the lower limit depends on $t$:

    $$
    dZ(t, T) = -\left[\int_t^T df(t, u)\,du - f(t, t)\,dt\right]
    $$

    **Origin of the $r_t\,dt$ term:** The lower limit of integration is $t$, which advances by $dt$. When the lower limit increases from $t$ to $t + dt$, the integral $\int_t^T (\cdot)\,du$ loses the "slice" from $t$ to $t + dt$, which has value approximately $f(t, t)\,dt = r_t\,dt$. Since the integral carries a minus sign, this contributes $+r_t\,dt$ to $dZ$.

    **Substituting the forward rate dynamics** $df(t, u) = \alpha(t, u)\,dt + \sigma(t, u)\,dW_t$:

    $$
    dZ(t, T) = r_t\,dt - \int_t^T \bigl[\alpha(t, u)\,dt + \sigma(t, u)\,dW_t\bigr]\,du
    $$

    Exchanging the order of integration and the stochastic differential (justified by Fubini's theorem for stochastic integrals under appropriate integrability conditions):

    $$
    dZ(t, T) = r_t\,dt - \left(\int_t^T \alpha(t, u)\,du\right)dt - \left(\int_t^T \sigma(t, u)\,du\right)dW_t
    $$

    Defining $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$:

    $$
    dZ(t, T) = \left[r_t - \int_t^T \alpha(t, u)\,du\right]dt - \Sigma(t, T)\,dW_t
    $$

    This confirms the stated formula. The $r_t\,dt$ term arises purely from the moving lower limit of integration --- it is the "boundary contribution" in the stochastic Leibniz rule. $\square$

---

**Exercise 2.** Consider a two-factor HJM model with volatilities $\sigma_1(t, T) = 0.012$ and $\sigma_2(t, T) = 0.008\,e^{-0.2(T-t)}$. Compute the drift $\alpha(t, T)$ using the multi-factor drift condition. Evaluate $\alpha(t, T)$ numerically at $T - t = 5$ and $T - t = 10$. Which factor contributes more to the drift at long maturities?

??? success "Solution to Exercise 2"

    **Step 1: Apply the multi-factor drift condition.**

    With $\sigma_1(t, T) = 0.012$ and $\sigma_2(t, T) = 0.008\,e^{-0.2(T-t)}$:

    $$
    \alpha(t, T) = \sigma_1 \int_t^T \sigma_1\,du + \sigma_2\,e^{-0.2(T-t)}\int_t^T \sigma_2\,e^{-0.2(u-t)}\,du
    $$

    **Factor 1 contribution:**

    $$
    \alpha_1(t, T) = (0.012)^2(T - t) = 1.44 \times 10^{-4}(T - t)
    $$

    **Factor 2 contribution:**

    $$
    \int_t^T 0.008\,e^{-0.2(u-t)}\,du = \frac{0.008}{0.2}\bigl(1 - e^{-0.2(T-t)}\bigr) = 0.04\bigl(1 - e^{-0.2(T-t)}\bigr)
    $$

    $$
    \alpha_2(t, T) = 0.008\,e^{-0.2(T-t)} \cdot 0.04\bigl(1 - e^{-0.2(T-t)}\bigr) = 3.2 \times 10^{-4}\,e^{-0.2(T-t)}\bigl(1 - e^{-0.2(T-t)}\bigr)
    $$

    **Total drift:**

    $$
    \alpha(t, T) = 1.44 \times 10^{-4}(T-t) + 3.2 \times 10^{-4}\,e^{-0.2(T-t)}\bigl(1 - e^{-0.2(T-t)}\bigr)
    $$

    **Step 2: Evaluate at $T - t = 5$.**

    $$
    \alpha_1 = 1.44 \times 10^{-4} \times 5 = 7.20 \times 10^{-4}
    $$

    $$
    e^{-1.0} \approx 0.3679, \quad \alpha_2 = 3.2 \times 10^{-4} \times 0.3679 \times (1 - 0.3679) = 3.2 \times 10^{-4} \times 0.3679 \times 0.6321 \approx 7.44 \times 10^{-5}
    $$

    $$
    \alpha(t, t+5) \approx 7.20 \times 10^{-4} + 7.44 \times 10^{-5} \approx 7.94 \times 10^{-4}
    $$

    **Step 3: Evaluate at $T - t = 10$.**

    $$
    \alpha_1 = 1.44 \times 10^{-4} \times 10 = 1.44 \times 10^{-3}
    $$

    $$
    e^{-2.0} \approx 0.1353, \quad \alpha_2 = 3.2 \times 10^{-4} \times 0.1353 \times (1 - 0.1353) = 3.2 \times 10^{-4} \times 0.1353 \times 0.8647 \approx 3.74 \times 10^{-5}
    $$

    $$
    \alpha(t, t+10) \approx 1.44 \times 10^{-3} + 3.74 \times 10^{-5} \approx 1.48 \times 10^{-3}
    $$

    **Step 4: Which factor dominates at long maturities?**

    Factor 1 (constant volatility) contributes linearly in $T - t$, growing without bound. Factor 2 (exponentially decaying) contributes a term that peaks near $T - t \approx 3.5$ and then decays to zero. At long maturities, **Factor 1 dominates**. At $T - t = 10$, Factor 1 contributes about 97% of the total drift.

---

**Exercise 3.** Prove that the integral form of the martingale condition, $\int_t^T \alpha(t, u)\,du = \frac{1}{2}\Sigma(t, T)^2$, implies the pointwise condition $\alpha(t, T) = \sigma(t, T)\,\Sigma(t, T)$ by differentiating both sides with respect to $T$. What regularity conditions on $\alpha$ and $\sigma$ are needed for this differentiation to be valid?

??? success "Solution to Exercise 3"

    **Step 1: Start from the integral condition.**

    The martingale condition on discounted bonds gives:

    $$
    \int_t^T \alpha(t, u)\,du = \frac{1}{2}\Sigma(t, T)^2
    $$

    **Step 2: Differentiate both sides with respect to $T$.**

    Left side:

    $$
    \frac{\partial}{\partial T}\int_t^T \alpha(t, u)\,du = \alpha(t, T)
    $$

    by the fundamental theorem of calculus (valid when $\alpha(t, \cdot)$ is continuous in its second argument).

    Right side:

    $$
    \frac{\partial}{\partial T}\left[\frac{1}{2}\Sigma(t, T)^2\right] = \Sigma(t, T)\,\frac{\partial \Sigma(t, T)}{\partial T}
    $$

    Since $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$:

    $$
    \frac{\partial \Sigma(t, T)}{\partial T} = \sigma(t, T)
    $$

    again by the fundamental theorem of calculus (valid when $\sigma(t, \cdot)$ is continuous).

    **Step 3: Combine.**

    $$
    \alpha(t, T) = \Sigma(t, T)\,\sigma(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du
    $$

    **Step 4: Regularity conditions.**

    The differentiation under the integral sign requires:

    1. $\alpha(t, u)$ is continuous in $u$ for each fixed $t$ (so that the fundamental theorem of calculus applies on the left side).
    2. $\sigma(t, u)$ is continuous in $u$ for each fixed $t$ (so that $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$ is differentiable in $T$ with derivative $\sigma(t, T)$).
    3. If $\alpha$ or $\sigma$ have isolated discontinuities, the pointwise condition holds at all points of continuity, and the integral condition still holds everywhere.

    In practice, both $\alpha$ and $\sigma$ are typically assumed to be jointly measurable and sufficiently regular (e.g., continuous or piecewise continuous in $T$) for these operations to be valid. $\square$

---

**Exercise 4.** For the Hull--White volatility $\sigma(t, T) = \sigma e^{-\kappa(T-t)}$, compute the bond volatility

$$
\Sigma(t, T) = \int_t^T \sigma e^{-\kappa(u-t)}\,du = \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr)
$$

and verify that the drift condition gives $\alpha(t, T) = \frac{\sigma^2}{\kappa}e^{-\kappa(T-t)}(1 - e^{-\kappa(T-t)})$. Show that this drift is always non-negative and identify its maximum as a function of $T - t$.

??? success "Solution to Exercise 4"

    **Step 1: Compute the bond volatility.**

    $$
    \Sigma(t, T) = \int_t^T \sigma e^{-\kappa(u-t)}\,du = \sigma\left[-\frac{1}{\kappa}e^{-\kappa(u-t)}\right]_t^T = \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    **Step 2: Verify the drift condition.**

    $$
    \alpha(t, T) = \sigma e^{-\kappa(T-t)} \cdot \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr) = \frac{\sigma^2}{\kappa}e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    This matches the stated expression. $\checkmark$

    **Step 3: Show non-negativity.**

    Let $\tau = T - t \geq 0$. Then $\alpha = \frac{\sigma^2}{\kappa}e^{-\kappa\tau}(1 - e^{-\kappa\tau})$.

    - $e^{-\kappa\tau} > 0$ for all $\tau \geq 0$.
    - $1 - e^{-\kappa\tau} \geq 0$ for $\tau \geq 0$ (with equality only at $\tau = 0$).
    - $\sigma^2/\kappa > 0$.

    Therefore $\alpha(t, T) \geq 0$ for all $T \geq t$, with $\alpha(t, t) = 0$. $\square$

    **Step 4: Find the maximum.**

    Define $g(\tau) = e^{-\kappa\tau}(1 - e^{-\kappa\tau}) = e^{-\kappa\tau} - e^{-2\kappa\tau}$.

    $$
    g'(\tau) = -\kappa e^{-\kappa\tau} + 2\kappa e^{-2\kappa\tau} = \kappa e^{-\kappa\tau}(2e^{-\kappa\tau} - 1)
    $$

    Setting $g'(\tau) = 0$: $2e^{-\kappa\tau} = 1 \implies e^{-\kappa\tau} = 1/2 \implies \tau^* = \frac{\ln 2}{\kappa}$.

    The maximum drift occurs at time-to-maturity $\tau^* = \frac{\ln 2}{\kappa}$. The maximum value is:

    $$
    \alpha_{\max} = \frac{\sigma^2}{\kappa} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{\sigma^2}{4\kappa}
    $$

    For example, with $\sigma = 0.01$ and $\kappa = 0.1$: $\tau^* = 6.93$ years and $\alpha_{\max} = 2.5 \times 10^{-4}$.

---

**Exercise 5.** The HJM framework automatically fits the initial yield curve. Explain precisely how: if you specify $f(0, T)$ from market data and evolve the forward rate according to $df(t, T) = \sigma(t, T)\,\Sigma(t, T)\,dt + \sigma(t, T)\,dW_t$, why is $P(0, T) = \exp(-\int_0^T f(0, u)\,du)$ guaranteed to match market bond prices at time 0? Contrast this with the Vasicek model, where additional parameter fitting is needed.

??? success "Solution to Exercise 5"

    **Step 1: How the initial curve is automatically matched.**

    In the HJM framework, the initial forward curve $f(0, T)$ is taken as a **given input** from market data. The SDE specifies how $f(t, T)$ evolves from this initial condition:

    $$
    f(t, T) = f(0, T) + \int_0^t \alpha(s, T)\,ds + \int_0^t \sigma(s, T)\,dW_s
    $$

    At $t = 0$, both integrals vanish, giving $f(0, T) = f(0, T)$ trivially. Therefore:

    $$
    P(0, T) = \exp\!\left(-\int_0^T f(0, u)\,du\right)
    $$

    This is exactly the market bond price at time 0, computed from the market forward curve. **No calibration is needed** to match the initial yield curve --- it is satisfied by construction for any choice of volatility $\sigma(t, T)$.

    **Step 2: The no-arbitrage drift ensures consistency for $t > 0$.**

    For $t > 0$, the drift condition $\alpha(t, T) = \sigma(t, T)\,\Sigma(t, T)$ ensures that discounted bond prices $P(t, T)/B_t$ are martingales. This means:

    $$
    \frac{P(0, T)}{B_0} = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{P(t, T)}{B_t}\right]
    $$

    The initial prices are not only matched but remain consistent with no-arbitrage dynamics going forward.

    **Step 3: Contrast with Vasicek.**

    In the Vasicek model, the bond price is $P(t, T) = e^{A(\tau) - B(\tau)r_t}$ where $\tau = T - t$ and $A, B$ depend on the parameters $\kappa, \theta, \sigma$. The initial yield curve is:

    $$
    P(0, T) = e^{A(T) - B(T)r_0}
    $$

    This is a specific functional form determined by three parameters $(\kappa, \theta, \sigma)$ and the initial short rate $r_0$. The model-implied curve generally does **not** match the observed market curve exactly. To achieve a reasonable fit, one must:

    1. Estimate $\kappa, \theta, \sigma$ by minimizing the discrepancy between model and market curves.
    2. Accept that the fit is imperfect (the Vasicek curve has too few degrees of freedom to match an arbitrary market curve).
    3. Alternatively, use the Hull--White extension with time-dependent $\theta(t)$ to achieve exact fit, but this adds complexity.

    The HJM framework avoids all of these issues by taking the market curve as input rather than output.

---

**Exercise 6.** Under the physical measure $\mathbb{P}$, suppose $df(t, T) = \alpha^{\mathbb{P}}(t, T)\,dt + \sigma(t, T)\,dW_t^{\mathbb{P}}$ with a constant market price of risk $\lambda$. Show that the risk-neutral drift satisfies

$$
\alpha(t, T) = \alpha^{\mathbb{P}}(t, T) - \lambda\,\sigma(t, T)
$$

and that the HJM condition then constrains the physical drift as $\alpha^{\mathbb{P}}(t, T) = \sigma(t, T)[\Sigma(t, T) + \lambda]$. Interpret the term $\lambda\,\sigma(t, T)$ as a risk premium.

??? success "Solution to Exercise 6"

    **Step 1: Relate the two measures via Girsanov's theorem.**

    Under $\mathbb{P}$, $dW_t^{\mathbb{P}}$ is a Brownian motion. Define the risk-neutral Brownian motion by $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \lambda\,dt$ (equivalently, $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \lambda\,dt$).

    Under $\mathbb{P}$:

    $$
    df(t, T) = \alpha^{\mathbb{P}}(t, T)\,dt + \sigma(t, T)\,dW_t^{\mathbb{P}}
    $$

    Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \lambda\,dt$:

    $$
    df(t, T) = \bigl[\alpha^{\mathbb{P}}(t, T) - \lambda\,\sigma(t, T)\bigr]\,dt + \sigma(t, T)\,dW_t^{\mathbb{Q}}
    $$

    The risk-neutral drift is therefore:

    $$
    \alpha(t, T) = \alpha^{\mathbb{P}}(t, T) - \lambda\,\sigma(t, T)
    $$

    This confirms the stated relation. $\checkmark$

    **Step 2: Apply the HJM no-arbitrage condition.**

    Under $\mathbb{Q}$, the drift must satisfy:

    $$
    \alpha(t, T) = \sigma(t, T)\,\Sigma(t, T)
    $$

    Substituting:

    $$
    \alpha^{\mathbb{P}}(t, T) - \lambda\,\sigma(t, T) = \sigma(t, T)\,\Sigma(t, T)
    $$

    Solving for the physical drift:

    $$
    \alpha^{\mathbb{P}}(t, T) = \sigma(t, T)\bigl[\Sigma(t, T) + \lambda\bigr]
    $$

    **Step 3: Interpret the risk premium term.**

    The physical drift decomposes as:

    $$
    \alpha^{\mathbb{P}}(t, T) = \underbrace{\sigma(t, T)\,\Sigma(t, T)}_{\text{risk-neutral drift}} + \underbrace{\lambda\,\sigma(t, T)}_{\text{risk premium}}
    $$

    The term $\lambda\,\sigma(t, T)$ is the **risk premium** for bearing forward rate risk at maturity $T$. It is proportional to the forward rate volatility $\sigma(t, T)$: more volatile maturities carry a larger risk premium. The constant $\lambda$ represents the market price of interest rate risk --- it is positive if investors require compensation for bearing rate risk (i.e., expected returns on bonds exceed the risk-free rate).

    Under $\mathbb{P}$, forward rates drift upward (on average) faster than under $\mathbb{Q}$ by the amount $\lambda\,\sigma(t, T)$. This reflects the fact that bond prices under $\mathbb{P}$ earn an excess return (risk premium) over the money-market rate. $\square$

---

**Exercise 7.** Verify the consistency of the discounted bond price dynamics. Starting from

$$
d\tilde{P} = \tilde{P}\left[\left(-\int_t^T \alpha(t, u)\,du + \frac{1}{2}\Sigma(t, T)^2\right)dt - \Sigma(t, T)\,dW_t\right],
$$

substitute the drift condition $\int_t^T \alpha(t, u)\,du = \frac{1}{2}\Sigma(t, T)^2$ and confirm that the drift of $\tilde{P}$ vanishes, leaving $d\tilde{P} = -\tilde{P}\,\Sigma(t, T)\,dW_t$, which is indeed a martingale (assuming appropriate integrability conditions).

??? success "Solution to Exercise 7"

    **Step 1: Start from the given dynamics.**

    $$
    d\tilde{P} = \tilde{P}\left[\left(-\int_t^T \alpha(t, u)\,du + \frac{1}{2}\Sigma(t, T)^2\right)dt - \Sigma(t, T)\,dW_t\right]
    $$

    **Step 2: Substitute the drift condition.**

    The integral form of the martingale condition states:

    $$
    \int_t^T \alpha(t, u)\,du = \frac{1}{2}\Sigma(t, T)^2
    $$

    Substituting into the drift coefficient:

    $$
    -\int_t^T \alpha(t, u)\,du + \frac{1}{2}\Sigma(t, T)^2 = -\frac{1}{2}\Sigma(t, T)^2 + \frac{1}{2}\Sigma(t, T)^2 = 0
    $$

    **Step 3: Confirm the drift vanishes.**

    The dynamics reduce to:

    $$
    d\tilde{P}(t, T) = -\tilde{P}(t, T)\,\Sigma(t, T)\,dW_t
    $$

    This is a driftless SDE: the only term is the stochastic (martingale) part.

    **Step 4: Verify the martingale property.**

    The solution of $d\tilde{P} = -\tilde{P}\,\Sigma(t, T)\,dW_t$ is the stochastic exponential:

    $$
    \tilde{P}(t, T) = \tilde{P}(0, T)\,\exp\!\left(-\int_0^t \Sigma(s, T)\,dW_s - \frac{1}{2}\int_0^t \Sigma(s, T)^2\,ds\right)
    $$

    This is an exponential martingale provided the **Novikov condition** is satisfied:

    $$
    \mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^t \Sigma(s, T)^2\,ds\right)\right] < \infty
    $$

    This holds whenever $\Sigma(s, T)$ is bounded or has sufficiently light tails (which is the case for all standard HJM volatility specifications such as constant, exponential, or humped volatilities).

    Under this integrability condition, $\tilde{P}(t, T)$ is a true $\mathbb{Q}$-martingale, confirming that the HJM drift condition ensures no-arbitrage. $\square$
