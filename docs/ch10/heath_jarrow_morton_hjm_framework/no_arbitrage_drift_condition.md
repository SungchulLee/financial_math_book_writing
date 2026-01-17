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

### Computing $dZ(t, T)$

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

### Dynamics of $P(t, T)/B_t$

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

### $n$-Factor HJM

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

---

## Further Reading

- Heath, Jarrow & Morton (1992), "Bond Pricing and the Term Structure of Interest Rates: A New Methodology"
- Björk, *Arbitrage Theory in Continuous Time*, Chapter 25
- Filipović, *Term-Structure Models*, Chapter 7
