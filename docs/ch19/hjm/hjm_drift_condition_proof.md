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

---

**Exercise 2.** Verify the HJM drift condition for the Ho--Lee model, where $\sigma(t, T) = \sigma$ is constant. Compute the drift $\alpha(t, T)$, the bond volatility $\Sigma(t, T) = \int_t^T \sigma\,du$, and show that the resulting forward rate dynamics integrate to

$$
f(t, T) = f(0, T) + \sigma^2 t(T - t/2) + \sigma W_t
$$

---

**Exercise 3.** For the Hull--White (extended Vasicek) volatility $\sigma(t, T) = \sigma e^{-\kappa(T-t)}$, compute the drift

$$
\alpha(t, T) = \frac{\sigma^2}{\kappa}\,e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
$$

and verify that setting $T = t$ gives $\alpha(t, t) = 0$. Explain why the drift at the short end of the curve vanishes.

---

**Exercise 4.** Consider a two-factor HJM model with $\sigma_1(t, T) = \sigma_1$ and $\sigma_2(t, T) = \sigma_2\,e^{-\kappa(T-t)}$. Write down the multi-factor drift condition

$$
\alpha(t, T) = \sum_{i=1}^{2}\sigma_i(t, T)\int_t^T \sigma_i(t, u)\,du
$$

and compute $\alpha(t, T)$ explicitly. Show that it reduces to the single-factor cases when either $\sigma_1 = 0$ or $\sigma_2 = 0$.

---

**Exercise 5.** In the alternative ZCB dynamics proof, the key step is computing $d\sigma_P^2(t, T)/dT$ where $\sigma_P(t, T) = -\int_t^T \sigma(t, u)\,du$. Carry out this computation for a general volatility $\sigma(t, T)$ and verify that

$$
\frac{d\sigma_P^2(t, T)}{dT} = 2\sigma(t, T)\int_t^T \sigma(t, u)\,du
$$

Explain why the factor of 2 appears and how it leads to the drift condition after dividing by 2.

---

**Exercise 6.** The HJM drift condition states that drift is uniquely determined by volatility. Does this mean that two different volatility specifications can never produce the same bond price dynamics? Construct a counterexample or prove that the mapping from $\sigma(t, T)$ to bond price dynamics is injective.

---

**Exercise 7.** Under the physical measure $\mathbb{P}$, forward rates have drift $\alpha^{\mathbb{P}}(t, T)$ and the market price of risk is $\lambda(t)$, so that $\alpha(t, T) = \alpha^{\mathbb{P}}(t, T) - \lambda(t)\,\sigma(t, T)$. If $\lambda(t) = \lambda_0 + \lambda_1 r_t$ (affine in the short rate), discuss what constraints the HJM no-arbitrage condition imposes on the relationship between $\alpha^{\mathbb{P}}(t, T)$ and $\sigma(t, T)$. Is $\alpha^{\mathbb{P}}(t, T)$ still uniquely determined by $\sigma(t, T)$ alone?
