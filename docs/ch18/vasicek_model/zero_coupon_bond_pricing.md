# Zero-Coupon Bond Pricing (Closed-Form)

*This section covers zero-coupon bond pricing (closed-form) in the context of Zero Coupon Bond Pricing in Chapter 18.*

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand the two fundamental approaches to deriving bond prices: market price of risk and risk-neutral measures
    2. Apply Itô's lemma to bond price dynamics
    3. Derive the PDE governing bond prices under different measures
    4. Solve the PDE to obtain the closed-form bond price formula
    5. Connect no-arbitrage arguments to partial differential equations

---

## Overview

In the Vasicek model, zero-coupon bond prices can be derived through two elegant approaches: the **market price of risk method** and the **risk-neutral measure method**. Both methods yield the same PDE, but they employ different mathematical frameworks. This section presents both derivations, showing their equivalence and complementary insights.

The key assumption in short-rate models is that the bond price depends only on the current time $t$, the current short rate $r_t$, and the maturity date $T$:

$$P(t,T) = f(t, r_t, T)$$

---

## Method 1: Market Price of Risk Approach

### Step 1: Apply Itô's Lemma to Bond Prices

The Vasicek short rate follows the SDE:

$$dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$$

For a bond price $P(t,T) = f(t, r_t, T)$, we apply Itô's lemma:

$$df = f_t dt + f_r dr + \frac{1}{2}f_{rr}(dr)^2$$

Substituting the short rate SDE and using $(dr)^2 \approx \sigma^2 dt$:

$$df = f_t dt + f_r\left[\alpha(\theta - r_t)dt + \sigma dW_t\right] + \frac{1}{2}f_{rr}\sigma^2 dt$$

$$= \left(f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr}\right)dt + \sigma f_r dW_t$$

Dividing by $f$ to express in return form:

$$\frac{df}{f} = \left[\frac{f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr}}{f}\right]dt + \frac{\sigma f_r}{f}dW_t$$

$$:= \mu(t, r_t, T)dt + \nu(t, r_t, T)dW_t$$

where:
- **Drift**: $\mu(t, r_t, T) = \frac{f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr}}{f}$
- **Volatility**: $\nu(t, r_t, T) = \frac{\sigma f_r}{f}$

### Step 2: Construct a Risk-Free Portfolio

Consider a portfolio consisting of:
- Short position (issue): one $T_1$-maturity bond with value $U_1$
- Long position (buy): one $T_2$-maturity bond with value $U_2$
- Net portfolio value: $U = U_2 - U_1$

The portfolio evolution is:

$$dU = \mu(t, r_t, T_2)U_2 dt + \nu(t, r_t, T_2)U_2 dW_t - \mu(t, r_t, T_1)U_1 dt - \nu(t, r_t, T_1)U_1 dW_t$$

$$= [\mu(t, r_t, T_2)U_2 - \mu(t, r_t, T_1)U_1]dt + [\nu(t, r_t, T_2)U_2 - \nu(t, r_t, T_1)U_1]dW_t$$

To eliminate randomness, set the Wiener process coefficient to zero:

$$\nu(t, r_t, T_2)U_2 - \nu(t, r_t, T_1)U_1 = 0$$

Combined with $U = U_2 - U_1$, solving this system yields:

$$U_1 = U\frac{\nu(t, r_t, T_2)}{\nu(t, r_t, T_1) - \nu(t, r_t, T_2)}$$

$$U_2 = U\frac{\nu(t, r_t, T_1)}{\nu(t, r_t, T_1) - \nu(t, r_t, T_2)}$$

### Step 3: Derive the Market Price of Risk

With these positions, the deterministic drift becomes:

$$dU = \frac{\mu(t, r_t, T_2)\nu(t, r_t, T_1) - \mu(t, r_t, T_1)\nu(t, r_t, T_2)}{\nu(t, r_t, T_1) - \nu(t, r_t, T_2)}U dt$$

By the **no-arbitrage principle**, a risk-free portfolio must earn the risk-free rate:

$$dU = r_t U dt$$

This implies:

$$\frac{\mu(t, r_t, T_2)\nu(t, r_t, T_1) - \mu(t, r_t, T_1)\nu(t, r_t, T_2)}{\nu(t, r_t, T_1) - \nu(t, r_t, T_2)} = r_t$$

Rearranging:

$$\frac{\mu(t, r_t, T_1) - r_t}{\nu(t, r_t, T_1)} = \frac{\mu(t, r_t, T_2) - r_t}{\nu(t, r_t, T_2)} := \lambda_t$$

**Key insight**: The ratio $\lambda_t$ is independent of maturity $T$. This quantity is the **market price of risk** (also called market price of interest rate risk), representing the excess return per unit of systematic risk.

### Step 4: Derive the PDE

Substituting the definitions of $\mu$ and $\nu$:

$$\frac{\mu(t, r_t, T) - r_t}{\nu(t, r_t, T)} = \lambda_t$$

$$\frac{\frac{f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr}}{f} - r_t}{\frac{\sigma f_r}{f}} = \lambda_t$$

$$\frac{f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr} - rf}{\sigma f_r} = \lambda_t$$

Rearranging:

$$f_t + \frac{1}{2}\sigma^2 f_{rr} + [\alpha(\theta - r_t) - \sigma\lambda_t]f_r - rf = 0$$

This is the **bond pricing PDE** under the physical measure, with the market price of risk $\lambda_t$ incorporated.

**Boundary condition**: $f(T, r_T, T) = 1$ (the bond pays $1 at maturity)

---

## Method 2: Risk-Neutral Measure Approach

### Step 1: Change of Measure via Girsanov Theorem

We seek a risk-neutral measure $\mathbb{Q}$ under which discounted bond prices are martingales. Define the Radon-Nikodym derivative process:

$$dW_t^\mathbb{Q} = \xi dt + dW_t$$

where $\xi$ is the market price of risk (Girsanov kernel). Under the risk-neutral measure $\mathbb{Q}$, the bond price follows:

$$df = f_t dt + f_r[(\alpha(\theta - r_t) - \sigma\xi)dt + \sigma dW_t^\mathbb{Q}] + \frac{1}{2}\sigma^2 f_{rr}dt$$

$$= [f_t + (\alpha(\theta - r_t) - \sigma\xi)f_r + \frac{1}{2}\sigma^2 f_{rr}]dt + \sigma f_r dW_t^\mathbb{Q}$$

### Step 2: Martingale Property of Discounted Bonds

The discount factor is $D(t) = e^{-\int_0^t r_s ds}$, with dynamics:

$$dD(t) = -r_t D(t)dt$$

Consider the product $Z(t) = P(t,T) \cdot D(t) = f(t, r_t, T) \cdot D(t)$. Applying Itô's product rule:

$$d(fD) = (df)D + f(dD) + d\langle f, D\rangle$$

where $d\langle f, D\rangle = 0$ (no cross-variation since $D$ has no diffusion term).

$$d(fD) = [f_t + (\alpha(\theta - r_t) - \sigma\xi)f_r + \frac{1}{2}\sigma^2 f_{rr} - rf]dt + \sigma f_r dW_t^\mathbb{Q}$$

### Step 3: Zero-Drift Condition for Martingales

For $fD$ to be a martingale under $\mathbb{Q}$, the drift must vanish:

$$f_t + (\alpha(\theta - r_t) - \sigma\xi)f_r + \frac{1}{2}\sigma^2 f_{rr} - rf = 0$$

$$f_t + \frac{1}{2}\sigma^2 f_{rr} + [\alpha(\theta - r_t) - \sigma\xi]f_r - rf = 0$$

This is exactly the same PDE as the market price of risk method! The parameter $\xi = \lambda_t$ identifies the two approaches.

**Under the risk-neutral measure**: Short rates follow

$$dr_t = \alpha(\theta - r_t)dt - \sigma\lambda_t dt + \sigma dW_t^\mathbb{Q} = \alpha^*(\theta^* - r_t)dt + \sigma dW_t^\mathbb{Q}$$

where $\alpha^* = \alpha$ and the risk-adjusted drift incorporates the market price of risk.

### Step 4: Bond Price as Expectation

Under the risk-neutral measure, the bond price is:

$$P(t,T) = \mathbb{E}^\mathbb{Q}\left[\exp\left(-\int_t^T r_s ds\right) \Big| \mathcal{F}_t\right]$$

This expectation formula is fundamental in interest rate modeling, providing an alternative characterization of bond prices.

---

## Solution: Closed-Form Bond Price Formula

The PDE:

$$f_t + \frac{1}{2}\sigma^2 f_{rr} + [\alpha(\theta - r_t) - \sigma\lambda_t]f_r - rf = 0$$

with boundary condition $f(T, r_T, T) = 1$ has the solution:

$$P(t,T) = A(t,T)e^{-B(t,T)r_t}$$

where:

$$B(t,T) = \frac{1 - e^{-\alpha(T-t)}}{\alpha}$$

$$A(t,T) = \exp\left[\frac{(B(t,T) - (T-t))(a^2b - \sigma^2/2)}{\alpha^2} - \frac{\sigma^2 B^2(t,T)}{4\alpha}\right]$$

Here $a = \alpha$ and $b = \theta - \lambda_t/\alpha$ (incorporating the market price of risk adjustment).

**Key properties**:
- When rates are low, $B(t,T)$ is large, making the exponential more sensitive to rate changes
- As $T \to t$, both $B(t,T) \to 0$ and $A(t,T) \to 1$, giving $P(t,t) = 1$ (correctness at maturity)
- The $A(t,T)$ factor accounts for the convexity and term structure curvature

---

## Comparison of Approaches

| Aspect | Market Price of Risk | Risk-Neutral Measure |
|--------|---------------------|----------------------|
| **Starting Point** | No-arbitrage with hedging portfolio | Change of measure (Girsanov) |
| **Physical vs Risk-Neutral** | Physical measure explicitly | Risk-neutral by construction |
| **PDE Interpretation** | Hedging eliminates drift relationship | Martingale property implies zero drift |
| **Market Price of Risk** | Derived from no-arbitrage | Specified as Girsanov kernel |
| **Final PDE** | Identical | Identical |
| **Computational Approach** | Backward induction intuitive | Expectation-based, Monte Carlo friendly |

---

## Summary

Both the **market price of risk approach** and the **risk-neutral measure approach** lead to the same fundamental PDE for Vasicek bond prices. The equivalence reflects the deep connection between:

1. **No-arbitrage principle** (no risk-free arbitrage)
2. **Risk-neutral valuation** (expectations under the right measure)
3. **Partial differential equations** (dynamics of value functions)

The closed-form solution $P(t,T) = A(t,T)e^{-B(t,T)r_t}$ provides a practical tool for bond pricing, option pricing, and portfolio management in the Vasicek framework.

**Based on**: QuantPie Lecture Notes - Interest Rate Modeling
