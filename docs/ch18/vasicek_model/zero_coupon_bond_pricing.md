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

**Boundary condition**: $f(T, r_T, T) = 1$ (the bond pays \$1 at maturity)

---

## Method 2: Risk-Neutral Measure Approach

### Step 1: Change of Measure via Girsanov Theorem

We seek a risk-neutral measure $\mathbb{Q}$ under which discounted bond prices are martingales. Define the Radon–Nikodym derivative process:

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

Recall (see [§ Named functions A and B](named_functions.md), [§ General affine bond pricing](../../ch15/affine_term_structure/bond_pricing_affine_framework.md), [§ Vasicek-as-affine](../../ch15/examples/vasicek_cir_as_affine.md)) for the full derivation of $A(t,T)$ and $B(t,T)$. The PDE has the exponential-affine solution $P(t,T) = A(t,T)e^{-B(t,T)r_t}$ with $B(t,T) = (1 - e^{-\alpha(T-t)})/\alpha$ and $A$ given in closed form. The boundary $P(T,T) = 1$ follows from $B(0) = 0$, $A(0) = 1$.

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

---

## Exercises

**Exercise 1.** Starting from the Vasicek SDE $dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$, apply Ito's lemma to $f(t, r_t) = P(t,T)$ and derive the drift $\mu$ and volatility $\nu$ of the bond return $df/f$. Show that $\nu(t, r_t, T) = \sigma f_r / f$ and interpret the sign of $\nu$ given that $f_r < 0$ for zero-coupon bonds.

??? success "Solution to Exercise 1"
    Apply Ito's lemma to $f(t, r_t) = P(t, T)$ where $dr_t = \alpha(\theta - r_t)\,dt + \sigma\,dW_t$:

    $$
    df = f_t\,dt + f_r\,dr_t + \frac{1}{2}f_{rr}\,(dr_t)^2
    $$

    Using $(dr_t)^2 = \sigma^2\,dt$:

    $$
    df = \left[f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr}\right]dt + \sigma f_r\,dW_t
    $$

    Dividing by $f$:

    $$
    \frac{df}{f} = \underbrace{\frac{f_t + \alpha(\theta - r_t)f_r + \frac{1}{2}\sigma^2 f_{rr}}{f}}_{\mu}\,dt + \underbrace{\frac{\sigma f_r}{f}}_{\nu}\,dW_t
    $$

    The volatility of the bond return is $\nu(t, r_t, T) = \sigma f_r / f$.

    **Sign of $\nu$.** For a zero-coupon bond, $f_r = \partial P/\partial r < 0$ because higher interest rates reduce bond prices (the bond pays a fixed \$1 at maturity, and the discount factor decreases when rates rise). Since $\sigma > 0$ and $f > 0$, the ratio $\sigma f_r / f$ is **negative**: $\nu < 0$.

    This means the bond return is negatively correlated with the Brownian motion driving rates: when $dW_t > 0$ (rates increase), the bond return is negative, and vice versa. The magnitude $|\nu| = \sigma |f_r|/f = \sigma B(\tau)$ (using $f_r = -B(\tau)f$) increases with maturity, reflecting the greater interest rate sensitivity of longer-duration bonds.

---

**Exercise 2.** In the market price of risk approach, the no-arbitrage condition leads to $(\mu - r)/\nu = \lambda_t$ being independent of maturity $T$. Explain economically why the Sharpe ratio of every bond (regardless of maturity) must be the same. What would happen if two bonds had different Sharpe ratios?

??? success "Solution to Exercise 2"
    The Sharpe ratio of any bond is $(\mu - r_t)/\nu = \lambda_t$, independent of maturity $T$.

    **Economic interpretation.** All bonds are exposed to the same source of risk---the single Brownian motion $dW_t$ driving the short rate. Since there is only one risk factor, the compensation per unit of risk must be the same for all assets exposed to that factor. If Bond A had a higher Sharpe ratio than Bond B, an arbitrageur could go long A (earning more per unit of risk) and short B (earning less), creating a portfolio with positive expected return and zero systematic risk---a **risk-free arbitrage**.

    The no-arbitrage condition forces all bonds to lie on the same capital market line: excess return is proportional to volatility, with the proportionality constant $\lambda_t$ being the market price of risk. This is the interest rate analog of the equity market's requirement that all assets have the same Sharpe ratio in a single-factor CAPM world.

    **If Sharpe ratios differed:** One could construct a long-short portfolio of bonds with different maturities that has zero net exposure to $dW_t$ (by appropriate weighting) but a non-zero expected excess return. This violates no-arbitrage, which requires any zero-risk portfolio to earn exactly the risk-free rate.

---

**Exercise 3.** Derive the bond pricing PDE $f_t + \frac{1}{2}\sigma^2 f_{rr} + [\alpha(\theta - r) - \sigma\lambda]f_r - rf = 0$ from the martingale condition on the discounted bond price $f(t,r)\,D(t)$ under $\mathbb{Q}$. Verify that the cross-variation term $d\langle f, D\rangle = 0$ because $D(t)$ has no diffusion component.

??? success "Solution to Exercise 3"
    Under $\mathbb{Q}$, the discounted bond price $Z(t) = f(t,r_t)\,D(t)$ where $D(t) = e^{-\int_0^t r_s\,ds}$ must be a martingale.

    The dynamics of $D(t)$: $dD = -r_t D\,dt$ (deterministic, no diffusion). Therefore the cross-variation $d\langle f, D \rangle = 0$ because $D$ has no $dW_t$ component (zero diffusion coefficient). The quadratic covariation between a process with diffusion coefficient $\sigma f_r$ and a process with diffusion coefficient $0$ is zero.

    By the Ito product rule:

    $$
    d(fD) = f\,dD + D\,df + d\langle f, D\rangle = f(-r_t D)\,dt + D\,df + 0
    $$

    $$
    = D\!\left[-r_t f + f_t + [\alpha(\theta - r_t) - \sigma\xi]f_r + \frac{1}{2}\sigma^2 f_{rr}\right]dt + D\,\sigma f_r\,dW_t^{\mathbb{Q}}
    $$

    For this to be a $\mathbb{Q}$-martingale, the drift must vanish:

    $$
    f_t + [\alpha(\theta - r_t) - \sigma\xi]f_r + \frac{1}{2}\sigma^2 f_{rr} - r_t f = 0
    $$

    This is the bond pricing PDE, identical to the one derived via the market price of risk approach with $\xi = \lambda_t$.

---

**Exercise 4.** The closed-form solution is $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ with $B(\tau) = (1 - e^{-\alpha\tau})/\alpha$. Verify the boundary condition $P(T,T) = 1$ by substituting $\tau = 0$. Then compute $\partial P / \partial r$ and show it is negative, confirming that bond prices decrease when rates increase.

??? success "Solution to Exercise 4"
    The solution is $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ with $B(\tau) = (1 - e^{-\alpha\tau})/\alpha$.

    **Boundary condition at $\tau = 0$:**

    $$
    B(0) = \frac{1 - e^0}{\alpha} = \frac{1 - 1}{\alpha} = 0
    $$

    $$
    \ln A(0) = \left(\theta - \frac{\sigma^2}{2\alpha^2}\right)(0 - 0) - \frac{\sigma^2}{4\alpha} \times 0 = 0 \quad \Longrightarrow \quad A(0) = 1
    $$

    $$
    P(T,T) = A(0)\,e^{-B(0)\,r_T} = 1 \times e^0 = 1
    $$

    The boundary condition is satisfied.

    **Derivative with respect to $r$:**

    $$
    \frac{\partial P}{\partial r} = A(\tau)\,e^{-B(\tau)\,r_t}\,(-B(\tau)) = -B(\tau)\,P(t,T)
    $$

    Since $B(\tau) = (1 - e^{-\alpha\tau})/\alpha > 0$ for $\tau > 0$ and $P(t,T) > 0$, we have:

    $$
    \frac{\partial P}{\partial r} = -B(\tau)\,P(t,T) < 0
    $$

    This confirms that bond prices **decrease** when rates increase, which is the fundamental property of fixed-income securities: a rise in the discount rate reduces the present value of future cash flows.

---

**Exercise 5.** Using the risk-neutral representation $P(t,T) = \mathbb{E}^{\mathbb{Q}}_t[e^{-\int_t^T r_s\,ds}]$, explain why Jensen's inequality implies $P(t,T) \geq e^{-\mathbb{E}^{\mathbb{Q}}_t[\int_t^T r_s\,ds]}$. How does this relate to the convexity term in $\ln A(\tau)$?

??? success "Solution to Exercise 5"
    Jensen's inequality states that for a convex function $g$ and random variable $X$: $\mathbb{E}[g(X)] \geq g(\mathbb{E}[X])$.

    The function $g(x) = e^{-x}$ is convex (since $g''(x) = e^{-x} > 0$). Applying Jensen's inequality with $X = \int_t^T r_s\,ds$:

    $$
    P(t,T) = \mathbb{E}^{\mathbb{Q}}_t\!\left[e^{-\int_t^T r_s\,ds}\right] \geq e^{-\mathbb{E}^{\mathbb{Q}}_t\!\left[\int_t^T r_s\,ds\right]}
    $$

    Taking logarithms and dividing by $-\tau$:

    $$
    -\frac{\ln P(t,T)}{\tau} \leq \frac{\mathbb{E}^{\mathbb{Q}}_t[\int_t^T r_s\,ds]}{\tau}
    $$

    $$
    R(t,T) \leq \bar{r}(t,T)
    $$

    where $\bar{r}(t,T)$ is the average expected rate over $[t,T]$. The yield is **below** the average expected rate.

    The gap $\bar{r} - R = -\frac{1}{\tau}\ln\!\left(\frac{P}{e^{-\tau\bar{r}}}\right)$ is the **convexity correction**. In the Vasicek bond price, this appears in $\ln A(\tau)$ through the term $-\sigma^2 B(\tau)^2/(4\kappa)$, which is always negative (reducing $\ln A$, increasing $P$, decreasing $R$). The greater the variability of rates (larger $\sigma$), the larger the Jensen gap and the more the yield is pushed below the expected average rate.

---

**Exercise 6.** The market price of risk $\lambda$ shifts the drift of the short rate from the physical measure to the risk-neutral measure: $dr_t = [\alpha(\theta - r_t) - \sigma\lambda]dt + \sigma dW_t^{\mathbb{Q}}$. If $\lambda > 0$, does this increase or decrease the risk-neutral drift? How does the sign of $\lambda$ affect the yield curve level?

??? success "Solution to Exercise 6"
    Under the risk-neutral measure, the short rate follows:

    $$
    dr_t = [\alpha(\theta - r_t) - \sigma\lambda]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    This can be rewritten as $dr_t = \alpha^{\mathbb{Q}}(\theta^{\mathbb{Q}} - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$ where the risk-neutral drift includes $-\sigma\lambda$.

    If $\lambda > 0$ (positive market price of risk):

    - The drift decreases: $\alpha(\theta - r_t) - \sigma\lambda < \alpha(\theta - r_t)$
    - The effective long-run mean under $\mathbb{Q}$ decreases: $\theta^{\mathbb{Q}} = \theta - \sigma\lambda/\alpha < \theta$

    Under the risk-neutral measure, rates are expected to be **lower** than under the physical measure. This means:

    - $\mathbb{E}^{\mathbb{Q}}[\int_t^T r_s\,ds]$ is smaller (lower expected integrated rates)
    - $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int r_s\,ds}]$ is **larger** (less discounting)
    - Bond prices **increase** and yields **decrease**

    The positive market price of risk reflects investors' demand for compensation for bearing interest rate risk. This risk premium lowers the risk-neutral expected rate below the physical expected rate, leading to lower risk-neutral yields (higher bond prices) than a naive expectation based on physical probabilities would suggest.

---

**Exercise 7.** For Vasicek parameters $\alpha = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$, and $\lambda = 0$ (zero market price of risk), compute $P(0,1)$, $P(0,5)$, and $P(0,10)$ using the closed-form formula. Then repeat with $\lambda = 0.1$ (positive risk premium) and compare. Which set of parameters produces higher bond prices, and why?

??? success "Solution to Exercise 7"
    **Case 1: $\lambda = 0$.** The risk-neutral parameters equal the physical: $\alpha = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$.

    Compute $B(\tau)$ and $\ln A(\tau)$ with $\theta - \sigma^2/(2\alpha^2) = 0.05 - 0.000225/0.18 = 0.05 - 0.00125 = 0.04875$.

    **$P(0,1)$:** $B(1) = (1-e^{-0.3})/0.3 = 0.2592/0.3 = 0.8640$.

    $$
    \ln A(1) = 0.04875 \times (0.864 - 1) - \frac{0.000225}{1.2} \times 0.864^2 = 0.04875(-0.136) - 0.0001875(0.7465)
    $$

    $$
    = -0.00663 - 0.000140 = -0.00677
    $$

    $$
    P(0,1) = e^{-0.00677 - 0.864 \times 0.04} = e^{-0.04133} = 0.9595
    $$

    **$P(0,5)$:** $B(5) = (1 - e^{-1.5})/0.3 = 0.7769/0.3 = 2.590$.

    $$
    \ln A(5) = 0.04875(2.590 - 5) - 0.0001875 \times 6.708 = 0.04875(-2.410) - 0.001258
    $$

    $$
    = -0.11749 - 0.001258 = -0.11874
    $$

    $$
    P(0,5) = e^{-0.11874 - 2.590 \times 0.04} = e^{-0.11874 - 0.10360} = e^{-0.22234} = 0.8008
    $$

    **$P(0,10)$:** $B(10) = (1 - e^{-3})/0.3 = 0.9502/0.3 = 3.1674$.

    $$
    \ln A(10) = 0.04875(3.1674 - 10) - 0.0001875 \times 10.033 = 0.04875(-6.833) - 0.001881
    $$

    $$
    = -0.33308 - 0.001881 = -0.33496
    $$

    $$
    P(0,10) = e^{-0.33496 - 3.1674 \times 0.04} = e^{-0.33496 - 0.12670} = e^{-0.46166} = 0.6301
    $$

    **Case 2: $\lambda = 0.1$.** The risk-neutral parameters become $\alpha^{\mathbb{Q}} = \alpha = 0.3$ (unchanged if $\lambda$ modifies only the drift level) and the risk-neutral drift is $\alpha(\theta - r) - \sigma\lambda = 0.3(0.05 - r) - 0.015 \times 0.1 = 0.3(0.05 - r) - 0.0015$. Effectively, $\theta^{\mathbb{Q}} = \theta - \sigma\lambda/\alpha = 0.05 - 0.015 \times 0.1/0.3 = 0.05 - 0.005 = 0.045$.

    Recomputing with $\theta^{\mathbb{Q}} = 0.045$, $\theta^{\mathbb{Q}} - \sigma^2/(2\alpha^2) = 0.045 - 0.00125 = 0.04375$:

    **$P(0,1)$:** $\ln A(1) = 0.04375(-0.136) - 0.000140 = -0.005950 - 0.000140 = -0.006090$.

    $$
    P(0,1) = e^{-0.006090 - 0.03456} = e^{-0.04065} = 0.9602
    $$

    **$P(0,5)$:** $\ln A(5) = 0.04375(-2.410) - 0.001258 = -0.10544 - 0.001258 = -0.10670$.

    $$
    P(0,5) = e^{-0.10670 - 0.10360} = e^{-0.21030} = 0.8104
    $$

    **$P(0,10)$:** $\ln A(10) = 0.04375(-6.833) - 0.001881 = -0.29894 - 0.001881 = -0.30082$.

    $$
    P(0,10) = e^{-0.30082 - 0.12670} = e^{-0.42752} = 0.6523
    $$

    **Comparison:**

    | Maturity | $P$ ($\lambda=0$) | $P$ ($\lambda=0.1$) |
    |:-:|:-:|:-:|
    | 1Y | 0.9595 | 0.9602 |
    | 5Y | 0.8008 | 0.8104 |
    | 10Y | 0.6301 | 0.6523 |

    Bond prices are **higher** with $\lambda = 0.1$. This is because the positive market price of risk lowers the risk-neutral long-run mean from $\theta = 5\%$ to $\theta^{\mathbb{Q}} = 4.5\%$, so under $\mathbb{Q}$ rates are expected to be lower, producing less discounting and higher bond prices. The effect grows with maturity because longer bonds accumulate more benefit from the lower risk-neutral drift.
