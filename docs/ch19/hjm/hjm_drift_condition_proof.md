# HJM Drift Condition Proof

This section explores the principles and methods underlying the HJM drift condition proof, which forms a critical component of modern financial mathematics.

## Key Concepts

The fundamental concepts in this area include:

- Theoretical foundations and mathematical framework
- Key definitions and notation
- Important theorems and results
- Connections to other areas of financial mathematics

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The core mathematical principles and their financial interpretations
    - How these concepts connect to practical applications
    - The relationship between theory and numerical implementation

---

## Primary Proof: Martingale Approach

The main proof of the HJM drift condition uses the martingale property of discounted bond prices. This is fully developed in the **No-Arbitrage Drift Condition** section, where we show:

1. Bond prices must satisfy $P(t,T) = \exp(-\int_t^T f(t,u)du)$
2. Discounted bonds $P(t,T)/B_t$ must be martingales under $\mathbb{Q}$
3. This martingale requirement forces:

$$\boxed{\alpha(t,T) = \sigma(t,T) \int_t^T \sigma(t,u)du}$$

---

## Alternative Proof: ZCB Dynamics Approach

An alternative derivation derives the same condition from zero-coupon bond dynamics.

### Starting Point

Since the instantaneous forward rate is the log-derivative of bond prices:

$$f(t,T) = -\frac{\partial}{\partial T}\log P(t,T)$$

The forward rate dynamics can be obtained by differentiating the bond price dynamics:

$$df(t,T) = -\frac{\partial}{\partial T}d\log P(t,T)$$

### Bond Price Dynamics

Under risk-neutral pricing, the bond price follows:

$$\frac{dP(t,T)}{P(t,T)} = r(t)dt + \sigma_P(t,T)dW^{\mathbb{Q}}(t)$$

where $\sigma_P(t,T) = -\int_t^T\sigma(t,T')dT'$ is the bond volatility.

### Log Bond Price

By Itô's lemma:

$$d\log P(t,T) = \left(r(t) - \frac{1}{2}\sigma_P^2(t,T)\right)dt + \sigma_P(t,T)dW^{\mathbb{Q}}(t)$$

### Forward Rate From Derivative

Taking the $T$-derivative:

$$df(t,T) = \frac{1}{2}\frac{d\sigma_P^2(t,T)}{dT}dt - \frac{d\sigma_P(t,T)}{dT}dW^{\mathbb{Q}}(t)$$

Since $\sigma_P(t,T) = -\int_t^T\sigma(t,T')dT'$:

$$\frac{d\sigma_P(t,T)}{dT} = -\sigma(t,T)$$

$$\frac{d\sigma_P^2(t,T)}{dT} = 2\sigma_P(t,T) \cdot (-\sigma(t,T)) = -2\sigma_P(t,T)\sigma(t,T) = 2\sigma(t,T)\int_t^T\sigma(t,T')dT'$$

### Result

$$df(t,T) = \sigma(t,T)\left(\int_t^T\sigma(t,T')dT'\right)dt + \sigma(t,T)dW^{\mathbb{Q}}(t)$$

This gives the same drift condition:

$$\mu^{\mathbb{Q}}(t,T) = \sigma(t,T)\int_t^T\sigma(t,T')dT'$$

---

## Proof Comparison

| Aspect | Martingale Approach | ZCB Dynamics Approach |
|--------|-------------------|----------------------|
| **Starting Point** | Discounted bond must be martingale | Bond log-derivative gives forwards |
| **Key Tool** | Itô's lemma on discounted bonds | Itô's lemma on log bonds + differentiation |
| **Conceptual Focus** | No-arbitrage via martingale condition | Direct relationship between rates and prices |
| **Computational Path** | Integrate, then differentiate | Differentiate log, then differentiate again |
| **Result** | Same drift condition | Same drift condition |

Both approaches are valid and complementary—they illuminate different aspects of the HJM framework.

---

## Multi-Factor Generalization

For multiple volatility factors:

$$df(t, T) = \alpha(t, T) \, dt + \sum_{i=1}^n \sigma_i(t, T) \, dW_t^i$$

Both proofs generalize naturally to:

$$\alpha(t, T) = \sum_{i=1}^n \sigma_i(t, T) \int_t^T \sigma_i(t, u) \, du$$

Each factor contributes additively to the drift.

---

## Key Insights

1. **Uniqueness**: The drift is uniquely determined once volatility is specified—there is no freedom to choose drift independently.

2. **No-Arbitrage is Automatic**: By construction, any HJM model with this drift condition is automatically free of arbitrage.

3. **Both Proofs Agree**: The martingale and ZCB dynamics approaches confirm each other, providing confidence in the result.

4. **Practical Implication**: Modelers need only specify volatility; drift is computed, not calibrated.

---

## Further Reading

- **Primary source**: Heath, Jarrow & Morton (1992), "Bond Pricing and the Term Structure of Interest Rates: A New Methodology"
- **Textbooks**:
  - Björk, *Arbitrage Theory in Continuous Time*, Chapter 25
  - Filipović, *Term-Structure Models*, Chapter 7
  - Brigo & Mercurio, *Interest Rate Models - Theory and Practice*, Part III

---

## Exercises

**Exercise 1.** Reproduce the martingale-based derivation of the HJM drift condition by carrying out the following steps explicitly. Start from $Z(t, T) = -\int_t^T f(t, u)\,du$, compute $dZ(t, T)$ using Leibniz's rule, apply Ito's lemma to $P(t, T) = e^{Z(t,T)}$, form the discounted bond price $P(t,T)/B_t$, set the drift to zero, and differentiate in $T$ to obtain $\alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du$.

??? success "Solution to Exercise 1"

    We carry out each step of the martingale-based derivation explicitly.

    **Step 1: Define the log bond price.**

    $$
    Z(t, T) = -\int_t^T f(t, u)\,du
    $$

    **Step 2: Compute $dZ(t, T)$ using Leibniz's rule.**

    The integral $Z(t, T) = -\int_t^T f(t, u)\,du$ has a stochastic integrand and a moving lower limit. Applying the stochastic Leibniz rule:

    $$
    dZ(t, T) = f(t, t)\,dt - \int_t^T df(t, u)\,du
    $$

    The $f(t, t)\,dt = r_t\,dt$ term arises because the lower limit $t$ advances by $dt$, contributing $+f(t, t)\,dt$ (since the integrand is preceded by a minus sign, the lower limit advancing "removes" a slice $f(t, t)\,dt$ from the integral). Substituting $df(t, u) = \alpha(t, u)\,dt + \sigma(t, u)\,dW_t$:

    $$
    dZ(t, T) = r_t\,dt - \int_t^T \alpha(t, u)\,du\,dt - \int_t^T \sigma(t, u)\,du\,dW_t
    $$

    Defining $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$:

    $$
    dZ(t, T) = \left[r_t - \int_t^T \alpha(t, u)\,du\right]dt - \Sigma(t, T)\,dW_t
    $$

    **Step 3: Apply Ito's lemma to $P(t, T) = e^{Z(t, T)}$.**

    $$
    dP = P\left[dZ + \frac{1}{2}(dZ)^2\right] = P\left[\left(r_t - \int_t^T \alpha(t, u)\,du + \frac{1}{2}\Sigma(t, T)^2\right)dt - \Sigma(t, T)\,dW_t\right]
    $$

    **Step 4: Form the discounted bond price $\tilde{P}(t, T) = P(t, T)/B_t$ where $dB_t = r_t B_t\,dt$.**

    $$
    d\tilde{P} = \frac{1}{B_t}\bigl(dP - r_t P\,dt\bigr) = \tilde{P}\left[\left(-\int_t^T \alpha(t, u)\,du + \frac{1}{2}\Sigma(t, T)^2\right)dt - \Sigma(t, T)\,dW_t\right]
    $$

    **Step 5: Set the drift to zero (martingale condition).**

    $$
    -\int_t^T \alpha(t, u)\,du + \frac{1}{2}\Sigma(t, T)^2 = 0
    $$

    Therefore:

    $$
    \int_t^T \alpha(t, u)\,du = \frac{1}{2}\Sigma(t, T)^2 = \frac{1}{2}\left(\int_t^T \sigma(t, u)\,du\right)^2
    $$

    **Step 6: Differentiate in $T$.**

    $$
    \alpha(t, T) = \frac{\partial}{\partial T}\left[\frac{1}{2}\Sigma(t, T)^2\right] = \Sigma(t, T)\,\frac{\partial \Sigma}{\partial T}(t, T) = \Sigma(t, T)\,\sigma(t, T)
    $$

    since $\frac{\partial}{\partial T}\int_t^T \sigma(t, u)\,du = \sigma(t, T)$. This gives:

    $$
    \boxed{\alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du}
    $$

---

**Exercise 2.** Verify the HJM drift condition for the Ho--Lee model, where $\sigma(t, T) = \sigma$ is constant. Compute the drift $\alpha(t, T)$, the bond volatility $\Sigma(t, T) = \int_t^T \sigma\,du$, and show that the resulting forward rate dynamics integrate to

$$
f(t, T) = f(0, T) + \sigma^2 t(T - t/2) + \sigma W_t
$$

??? success "Solution to Exercise 2"

    **Step 1: Apply the drift condition for $\sigma(t, T) = \sigma$ (constant).**

    $$
    \alpha(t, T) = \sigma \int_t^T \sigma\,du = \sigma^2(T - t)
    $$

    **Step 2: Compute the bond volatility.**

    $$
    \Sigma(t, T) = \int_t^T \sigma\,du = \sigma(T - t)
    $$

    **Step 3: Write the forward rate SDE and integrate.**

    $$
    df(t, T) = \sigma^2(T - t)\,dt + \sigma\,dW_t
    $$

    Integrating from $0$ to $t$:

    $$
    f(t, T) = f(0, T) + \sigma^2 \int_0^t (T - s)\,ds + \sigma W_t
    $$

    The deterministic integral evaluates to:

    $$
    \int_0^t (T - s)\,ds = Tt - \frac{t^2}{2} = t\left(T - \frac{t}{2}\right)
    $$

    Therefore:

    $$
    f(t, T) = f(0, T) + \sigma^2 t\!\left(T - \frac{t}{2}\right) + \sigma W_t
    $$

    This confirms the stated result. The forward rate is Gaussian (normally distributed), and the model is Ho--Lee.

---

**Exercise 3.** For the Hull--White (extended Vasicek) volatility $\sigma(t, T) = \sigma e^{-\kappa(T-t)}$, compute the drift

$$
\alpha(t, T) = \frac{\sigma^2}{\kappa}\,e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
$$

and verify that setting $T = t$ gives $\alpha(t, t) = 0$. Explain why the drift at the short end of the curve vanishes.

??? success "Solution to Exercise 3"

    **Step 1: Compute the drift.**

    With $\sigma(t, T) = \sigma e^{-\kappa(T-t)}$:

    $$
    \alpha(t, T) = \sigma e^{-\kappa(T-t)} \int_t^T \sigma e^{-\kappa(u-t)}\,du
    $$

    Evaluate the integral:

    $$
    \int_t^T \sigma e^{-\kappa(u-t)}\,du = \sigma\left[-\frac{1}{\kappa}e^{-\kappa(u-t)}\right]_t^T = \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    Therefore:

    $$
    \alpha(t, T) = \sigma e^{-\kappa(T-t)} \cdot \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr) = \frac{\sigma^2}{\kappa}e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    **Step 2: Verify $\alpha(t, t) = 0$.**

    Setting $T = t$:

    $$
    \alpha(t, t) = \frac{\sigma^2}{\kappa}e^{0}\bigl(1 - e^{0}\bigr) = \frac{\sigma^2}{\kappa}(1 - 1) = 0
    $$

    **Step 3: Explain why the drift vanishes at the short end.**

    The HJM drift at maturity $T$ is $\alpha(t, T) = \sigma(t, T)\,\Sigma(t, T)$ where $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$. At $T = t$, the bond volatility $\Sigma(t, t) = \int_t^t \sigma(t, u)\,du = 0$, because the "bond" with zero time-to-maturity is the money-market account, which has zero volatility. Since the drift is the product of the forward rate volatility and the bond volatility, and the bond volatility is zero at $T = t$, the drift must vanish at the short end regardless of the volatility specification. This is a universal feature of the HJM drift condition.

---

**Exercise 4.** Consider a two-factor HJM model with $\sigma_1(t, T) = \sigma_1$ and $\sigma_2(t, T) = \sigma_2\,e^{-\kappa(T-t)}$. Write down the multi-factor drift condition

$$
\alpha(t, T) = \sum_{i=1}^{2}\sigma_i(t, T)\int_t^T \sigma_i(t, u)\,du
$$

and compute $\alpha(t, T)$ explicitly. Show that it reduces to the single-factor cases when either $\sigma_1 = 0$ or $\sigma_2 = 0$.

??? success "Solution to Exercise 4"

    **Step 1: Apply the multi-factor drift condition.**

    $$
    \alpha(t, T) = \sigma_1(t, T)\int_t^T \sigma_1(t, u)\,du + \sigma_2(t, T)\int_t^T \sigma_2(t, u)\,du
    $$

    **Step 2: Compute each factor's contribution.**

    Factor 1 ($\sigma_1(t, T) = \sigma_1$, constant):

    $$
    \sigma_1 \int_t^T \sigma_1\,du = \sigma_1^2(T - t)
    $$

    Factor 2 ($\sigma_2(t, T) = \sigma_2\,e^{-\kappa(T-t)}$):

    $$
    \sigma_2 e^{-\kappa(T-t)} \int_t^T \sigma_2 e^{-\kappa(u-t)}\,du = \sigma_2^2 e^{-\kappa(T-t)} \cdot \frac{1 - e^{-\kappa(T-t)}}{\kappa} = \frac{\sigma_2^2}{\kappa}e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    **Step 3: Combine.**

    $$
    \alpha(t, T) = \sigma_1^2(T - t) + \frac{\sigma_2^2}{\kappa}e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    **Step 4: Verify limiting cases.**

    If $\sigma_1 = 0$: $\alpha(t, T) = \frac{\sigma_2^2}{\kappa}e^{-\kappa(T-t)}(1 - e^{-\kappa(T-t)})$, which is the Hull--White single-factor drift.

    If $\sigma_2 = 0$: $\alpha(t, T) = \sigma_1^2(T - t)$, which is the Ho--Lee single-factor drift.

    Both limiting cases are correctly recovered. $\square$

---

**Exercise 5.** In the alternative ZCB dynamics proof, the key step is computing $d\sigma_P^2(t, T)/dT$ where $\sigma_P(t, T) = -\int_t^T \sigma(t, u)\,du$. Carry out this computation for a general volatility $\sigma(t, T)$ and verify that

$$
\frac{d\sigma_P^2(t, T)}{dT} = 2\sigma(t, T)\int_t^T \sigma(t, u)\,du
$$

Explain why the factor of 2 appears and how it leads to the drift condition after dividing by 2.

??? success "Solution to Exercise 5"

    **Step 1: Compute $d\sigma_P^2(t, T)/dT$.**

    We have $\sigma_P(t, T) = -\int_t^T \sigma(t, u)\,du$. By the fundamental theorem of calculus:

    $$
    \frac{d\sigma_P(t, T)}{dT} = -\sigma(t, T)
    $$

    Now apply the chain rule to $\sigma_P^2(t, T) = [\sigma_P(t, T)]^2$:

    $$
    \frac{d\sigma_P^2(t, T)}{dT} = 2\,\sigma_P(t, T) \cdot \frac{d\sigma_P(t, T)}{dT} = 2\,\sigma_P(t, T) \cdot (-\sigma(t, T))
    $$

    Substituting $\sigma_P(t, T) = -\int_t^T \sigma(t, u)\,du$:

    $$
    \frac{d\sigma_P^2(t, T)}{dT} = 2\left(-\int_t^T \sigma(t, u)\,du\right)(-\sigma(t, T)) = 2\,\sigma(t, T)\int_t^T \sigma(t, u)\,du
    $$

    **Step 2: Explain the factor of 2.**

    The factor of 2 arises from the chain rule: $\frac{d}{dT}[g(T)]^2 = 2\,g(T)\,g'(T)$. This is the standard derivative of a squared function.

    **Step 3: Connection to the drift condition.**

    In the ZCB dynamics approach, the forward rate drift is

    $$
    \text{drift of } df(t, T) = \frac{1}{2}\frac{d\sigma_P^2(t, T)}{dT} = \frac{1}{2} \cdot 2\,\sigma(t, T)\int_t^T \sigma(t, u)\,du = \sigma(t, T)\int_t^T \sigma(t, u)\,du
    $$

    The factor of $\frac{1}{2}$ in the Ito correction (from $d\log P$) cancels with the factor of 2 from the chain rule, yielding the clean drift condition $\alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du$ without any numerical prefactor.

---

**Exercise 6.** The HJM drift condition states that drift is uniquely determined by volatility. Does this mean that two different volatility specifications can never produce the same bond price dynamics? Construct a counterexample or prove that the mapping from $\sigma(t, T)$ to bond price dynamics is injective.

??? success "Solution to Exercise 6"

    **Claim:** The mapping from $\sigma(t, T)$ to bond price dynamics is **injective** (i.e., different volatility specifications cannot produce the same bond price dynamics).

    **Proof:**

    Under the risk-neutral measure, bond price dynamics are:

    $$
    \frac{dP(t, T)}{P(t, T)} = r_t\,dt - \Sigma(t, T)\,dW_t
    $$

    where $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$.

    The drift is always $r_t$ (risk-neutral pricing), so the dynamics are completely characterized by the bond volatility $\Sigma(t, T)$.

    Suppose two volatility functions $\sigma$ and $\tilde{\sigma}$ produce the same bond price dynamics. Then they must produce the same bond volatility:

    $$
    \int_t^T \sigma(t, u)\,du = \int_t^T \tilde{\sigma}(t, u)\,du \quad \text{for all } T \geq t
    $$

    Differentiating both sides with respect to $T$:

    $$
    \sigma(t, T) = \tilde{\sigma}(t, T) \quad \text{for all } T \geq t
    $$

    (assuming $\sigma$ and $\tilde{\sigma}$ are continuous in $T$). Therefore the volatility functions must be identical.

    The mapping is injective: different volatility specifications always produce different bond price dynamics. $\square$

    **Remark:** This injectivity holds for the diffusion coefficient. If one allows different numbers of factors (e.g., a one-factor model versus a two-factor model), the *distributional* properties of the bond price could potentially agree if the total instantaneous variance $\sum_i \Sigma_i(t, T)^2$ is the same, but the driving noise structure would differ (one vs. two Brownian motions), so the dynamics in the strong (pathwise) sense would still be different.

---

**Exercise 7.** Under the physical measure $\mathbb{P}$, forward rates have drift $\alpha^{\mathbb{P}}(t, T)$ and the market price of risk is $\lambda(t)$, so that $\alpha(t, T) = \alpha^{\mathbb{P}}(t, T) - \lambda(t)\,\sigma(t, T)$. If $\lambda(t) = \lambda_0 + \lambda_1 r_t$ (affine in the short rate), discuss what constraints the HJM no-arbitrage condition imposes on the relationship between $\alpha^{\mathbb{P}}(t, T)$ and $\sigma(t, T)$. Is $\alpha^{\mathbb{P}}(t, T)$ still uniquely determined by $\sigma(t, T)$ alone?

??? success "Solution to Exercise 7"

    **Step 1: Relate physical and risk-neutral drifts.**

    Under $\mathbb{P}$, the forward rate dynamics are:

    $$
    df(t, T) = \alpha^{\mathbb{P}}(t, T)\,dt + \sigma(t, T)\,dW_t^{\mathbb{P}}
    $$

    The Girsanov theorem relates the two measures via $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} - \lambda(t)\,dt$, so under $\mathbb{Q}$:

    $$
    df(t, T) = \bigl[\alpha^{\mathbb{P}}(t, T) + \lambda(t)\,\sigma(t, T)\bigr]\,dt + \sigma(t, T)\,dW_t^{\mathbb{Q}}
    $$

    Wait -- let us be careful with signs. Under $\mathbb{P}$: $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} + \lambda(t)\,dt$. Substituting:

    $$
    df(t, T) = \bigl[\alpha^{\mathbb{P}}(t, T) + \lambda(t)\,\sigma(t, T)\bigr]\,dt + \sigma(t, T)\,dW_t^{\mathbb{Q}}
    $$

    The risk-neutral drift is $\alpha(t, T) = \alpha^{\mathbb{P}}(t, T) + \lambda(t)\,\sigma(t, T)$, which rearranges to:

    $$
    \alpha^{\mathbb{P}}(t, T) = \alpha(t, T) - \lambda(t)\,\sigma(t, T) = \sigma(t, T)\,\Sigma(t, T) - \lambda(t)\,\sigma(t, T)
    $$

    (using the sign convention in the problem, $\alpha(t, T) = \alpha^{\mathbb{P}}(t, T) - \lambda(t)\,\sigma(t, T)$ gives the same result upon rearrangement).

    **Step 2: Apply the HJM no-arbitrage condition.**

    The HJM condition determines the $\mathbb{Q}$-drift:

    $$
    \alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du
    $$

    Therefore the physical drift must satisfy:

    $$
    \alpha^{\mathbb{P}}(t, T) = \sigma(t, T)\left[\int_t^T \sigma(t, u)\,du + \lambda(t)\right]
    $$

    **Step 3: Substitute the affine market price of risk $\lambda(t) = \lambda_0 + \lambda_1 r_t$.**

    $$
    \alpha^{\mathbb{P}}(t, T) = \sigma(t, T)\left[\int_t^T \sigma(t, u)\,du + \lambda_0 + \lambda_1 r_t\right]
    $$

    **Step 4: Is $\alpha^{\mathbb{P}}$ determined by $\sigma$ alone?**

    No. The physical drift $\alpha^{\mathbb{P}}(t, T)$ depends on:

    1. The volatility function $\sigma(t, T)$ (which determines $\Sigma(t, T)$ and the $\mathbb{Q}$-drift),
    2. The market price of risk parameters $\lambda_0$ and $\lambda_1$, and
    3. The current short rate $r_t$ (through the $\lambda_1 r_t$ term).

    The no-arbitrage condition constrains $\alpha^{\mathbb{P}}$ to have the form above, but the parameters $\lambda_0$ and $\lambda_1$ are **not** determined by $\sigma(t, T)$. They must be estimated from historical data or specified as part of the model. Therefore, $\alpha^{\mathbb{P}}(t, T)$ is **not** uniquely determined by $\sigma(t, T)$ alone --- it requires additional information about the market price of risk.

    This is the fundamental distinction: under $\mathbb{Q}$, the drift is fully pinned down by no-arbitrage; under $\mathbb{P}$, there is additional freedom parameterized by $\lambda(t)$.
