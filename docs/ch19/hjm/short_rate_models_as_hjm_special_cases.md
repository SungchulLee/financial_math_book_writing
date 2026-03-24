# Short-Rate Models as HJM Special Cases

Short-rate models such as Vasicek, Hull--White, and CIR predate the HJM framework historically, but they are mathematically embedded within it. Each short-rate model corresponds to a specific choice of the HJM volatility function $\sigma(t,T)$. This section derives these embeddings explicitly, verifies the HJM drift condition in each case, and clarifies what structural constraints the short-rate assumption imposes on forward rate dynamics.

---

## The General Connection

### From Short-Rate to Forward-Rate Volatility

In a one-factor short-rate model, the short rate evolves as

$$
dr_t = \mu(t, r_t)\,dt + \gamma(t, r_t)\,dW_t^{\mathbb{Q}}
$$

under the risk-neutral measure. The forward rate is defined by

$$
f(t,T) = -\frac{\partial}{\partial T} \ln P(t,T)
$$

In the HJM framework, the forward rate dynamics are

$$
df(t,T) = \alpha(t,T)\,dt + \sigma_f(t,T)\,dW_t^{\mathbb{Q}}
$$

The key task is to determine $\sigma_f(t,T)$ from the short-rate specification. Since $r_t = f(t,t)$, the volatility of $f(t,T)$ at $T = t$ must match the short-rate volatility:

$$
\sigma_f(t,t) = \gamma(t, r_t)
$$

For maturities $T > t$, the forward rate volatility $\sigma_f(t,T)$ depends on how the bond price $P(t,T)$ responds to changes in $r_t$.

### Bond Price Sensitivity

In affine short-rate models, the bond price takes the form

$$
P(t,T) = e^{A(t,T) - B(t,T) r_t}
$$

where $A(t,T)$ and $B(t,T)$ are deterministic functions. The forward rate is

$$
f(t,T) = -\frac{\partial A}{\partial T} + \frac{\partial B}{\partial T} \, r_t
$$

The forward rate volatility is therefore

$$
\sigma_f(t,T) = \frac{\partial B(t,T)}{\partial T} \, \gamma(t, r_t)
$$

The bond volatility (negative of the bond's diffusion coefficient per unit price) is

$$
\Sigma(t,T) = B(t,T) \, \gamma(t, r_t)
$$

---

## Vasicek Model

### Short-Rate Dynamics

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

where $\kappa > 0$ (mean reversion), $\theta$ (long-run mean), and $\sigma > 0$ (volatility) are constants.

### Bond Price

The Vasicek bond price is $P(t,T) = e^{A(t,T) - B(t,T)r_t}$ with

$$
B(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}
$$

### HJM Volatility Function

Since $\gamma(t,r_t) = \sigma$ (constant) and $\partial B / \partial T = e^{-\kappa(T-t)}$:

$$
\boxed{\sigma_f(t,T) = \sigma \, e^{-\kappa(T-t)}}
$$

This is the exponentially decaying volatility structure. The forward rate volatility decreases with time-to-maturity $T - t$, reflecting mean reversion.

### Verification of the HJM Drift Condition

The bond volatility is

$$
\Sigma(t,T) = \int_t^T \sigma_f(t,u)\,du = \int_t^T \sigma \, e^{-\kappa(u-t)}\,du = \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr)
$$

The HJM drift condition requires

$$
\alpha(t,T) = \sigma_f(t,T) \cdot \Sigma(t,T) = \sigma \, e^{-\kappa(T-t)} \cdot \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr)
$$

$$
= \frac{\sigma^2}{\kappa} e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
$$

We can verify this independently. From $f(t,T) = -\partial_T A + (\partial_T B) \, r_t$, applying Itô's formula to $f(t,T)$ using the Vasicek dynamics for $r_t$ yields the same drift. $\square$

---

## Hull--White (Extended Vasicek) Model

### Short-Rate Dynamics

$$
dr_t = \bigl(\theta(t) - \kappa \, r_t\bigr)\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

where $\theta(t)$ is a time-dependent function chosen to fit the initial yield curve exactly.

### HJM Volatility Function

The diffusion coefficient is the same as Vasicek ($\gamma = \sigma$), and the bond function $B(t,T)$ is identical:

$$
\boxed{\sigma_f(t,T) = \sigma \, e^{-\kappa(T-t)}}
$$

The HJM volatility is the same as Vasicek. The difference is that $\theta(t)$ provides an exact fit to the initial forward curve $f(0,T)$, which the HJM framework achieves automatically by construction.

### Fitting the Initial Curve

In the HJM formulation, the initial forward curve $f(0,T)$ is taken as input. Hull--White determines $\theta(t)$ from the requirement that the model-implied curve matches market data:

$$
\theta(t) = \frac{\partial f(0,t)}{\partial t} + \kappa \, f(0,t) + \frac{\sigma^2}{2\kappa}\bigl(1 - e^{-2\kappa t}\bigr)
$$

The HJM framework subsumes this: specifying $\sigma_f(t,T) = \sigma e^{-\kappa(T-t)}$ and the initial curve $f(0,T)$ determines everything, including the equivalent of $\theta(t)$.

---

## Cox--Ingersoll--Ross (CIR) Model

### Short-Rate Dynamics

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

The key difference is the **state-dependent volatility** $\gamma(t,r_t) = \sigma\sqrt{r_t}$.

### Bond Price

The CIR bond price is $P(t,T) = e^{A(t,T) - B(t,T)r_t}$ with

$$
B(t,T) = \frac{2(e^{\gamma(T-t)} - 1)}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}
$$

where $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$.

### HJM Volatility Function

Since $\gamma(t,r_t) = \sigma\sqrt{r_t}$ depends on $r_t$:

$$
\boxed{\sigma_f(t,T) = \frac{\partial B(t,T)}{\partial T} \cdot \sigma \sqrt{r_t}}
$$

Computing the derivative:

$$
\frac{\partial B(t,T)}{\partial T} = \frac{4\gamma^2 e^{\gamma(T-t)}}{\bigl[(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma\bigr]^2}
$$

### State-Dependent HJM Volatility

The CIR volatility function is **state-dependent** --- it depends on $r_t$, which in turn depends on the entire path of the Brownian motion up to time $t$. This means:

- The HJM volatility $\sigma_f(t,T)$ is not a deterministic function of $(t,T)$ alone
- The model is **non-Gaussian**: forward rates are not normally distributed
- The short rate remains non-negative (provided $2\kappa\theta \geq \sigma^2$)

### Verification of the Drift Condition

The bond volatility is

$$
\Sigma(t,T) = B(t,T) \cdot \sigma\sqrt{r_t}
$$

The HJM drift condition gives

$$
\alpha(t,T) = \sigma_f(t,T) \cdot \Sigma(t,T) = \frac{\partial B}{\partial T} \cdot B(t,T) \cdot \sigma^2 r_t
$$

This can be verified to be consistent with the CIR bond pricing equation. The state-dependence introduces no inconsistency because the HJM drift condition holds pathwise.

!!! note "State-Dependent Volatility in HJM"
    The HJM framework allows the volatility $\sigma(t,T)$ to depend on the state (e.g., $r_t$ or the entire curve $f(t,\cdot)$). State-dependent specifications are needed to match models like CIR that generate non-Gaussian dynamics. However, they sacrifice the analytical tractability of Gaussian HJM models.

---

## Ho--Lee Model

### Short-Rate Dynamics

$$
dr_t = \theta(t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

There is no mean reversion ($\kappa = 0$).

### HJM Volatility Function

With $B(t,T) = T - t$ and $\gamma = \sigma$:

$$
\boxed{\sigma_f(t,T) = \sigma}
$$

This is the constant volatility HJM model. The drift condition gives $\alpha(t,T) = \sigma^2(T - t)$.

### Comparison with Vasicek

Ho--Lee is the $\kappa \to 0$ limit of Vasicek/Hull--White:

$$
\lim_{\kappa \to 0} \sigma \, e^{-\kappa(T-t)} = \sigma
$$

$$
\lim_{\kappa \to 0} \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr) = \sigma(T-t)
$$

---

## Summary Table

| Short-Rate Model | $\gamma(t,r_t)$ | $\sigma_f(t,T)$ | $\Sigma(t,T)$ | Gaussian? |
|---|---|---|---|---|
| Ho--Lee | $\sigma$ | $\sigma$ | $\sigma(T-t)$ | Yes |
| Vasicek | $\sigma$ | $\sigma e^{-\kappa(T-t)}$ | $\frac{\sigma}{\kappa}(1-e^{-\kappa(T-t)})$ | Yes |
| Hull--White | $\sigma$ | $\sigma e^{-\kappa(T-t)}$ | $\frac{\sigma}{\kappa}(1-e^{-\kappa(T-t)})$ | Yes |
| CIR | $\sigma\sqrt{r_t}$ | $B'(t,T)\sigma\sqrt{r_t}$ | $B(t,T)\sigma\sqrt{r_t}$ | No |

---

## Structural Implications

### Markov Property

One-factor short-rate models produce a **Markovian** short rate: given $r_t$, the future evolution of $r_s$ for $s > t$ is independent of the past. In HJM terms, this means the entire forward curve $f(t,\cdot)$ is determined by a single state variable $r_t$.

This is a severe restriction. The general HJM model is infinite-dimensional (the state is the entire curve), while one-factor short-rate models collapse it to a single dimension.

### When Does HJM Reduce to a Short-Rate Model?

The forward curve is determined by $r_t$ alone if and only if the HJM volatility function has the form

$$
\sigma_f(t,T) = h(t, r_t) \cdot g(T-t)
$$

for some functions $h$ and $g$ with $g(0) = 1$. This is the **Ritchken--Sankarasubramanian condition** for the existence of a finite-dimensional Markov representation.

### Two-Factor Short-Rate Models

Two-factor models (e.g., Longstaff--Schwartz, Fong--Vasicek) embed in two-factor HJM with specific volatility structures. Each factor introduces an additional state variable, allowing richer yield curve dynamics while maintaining a finite-dimensional Markov structure.

---

## Key Takeaways

- Every short-rate model defines a specific HJM volatility function via $\sigma_f(t,T) = (\partial B/\partial T) \cdot \gamma(t,r_t)$
- **Vasicek/Hull--White** correspond to exponentially decaying HJM volatility $\sigma e^{-\kappa(T-t)}$ (Gaussian forward rates)
- **Ho--Lee** corresponds to constant HJM volatility $\sigma$ (no mean reversion)
- **CIR** produces state-dependent HJM volatility proportional to $\sqrt{r_t}$ (non-Gaussian)
- The HJM drift condition is automatically satisfied for any short-rate model derived from no-arbitrage pricing
- Short-rate models impose strong Markov restrictions on the infinite-dimensional HJM framework

---

## Further Reading

- Heath, Jarrow & Morton (1992), "Bond Pricing and the Term Structure of Interest Rates"
- Björk (2009), *Arbitrage Theory in Continuous Time*, Chapters 23--25
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 5
- Ritchken & Sankarasubramanian (1995), "Volatility Structures of Forward Rates and the Dynamics of the Term Structure"

---

## Exercises

**Exercise 1.** For the Vasicek model with $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, the bond price takes the form $P(t, T) = A(T-t)\,e^{-B(T-t)\,r_t}$ where $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$. Derive the HJM forward rate volatility $\sigma_f(t, T) = \sigma\,e^{-\kappa(T-t)}$ by computing $f(t, T) = -\partial_T \ln P(t, T)$ and identifying the diffusion coefficient.

---

**Exercise 2.** For the Ho--Lee model with constant HJM volatility $\sigma(t, T) = \sigma$, verify the drift condition $\alpha(t, T) = \sigma^2(T - t)$ and show that the short rate $r_t = f(t, t)$ follows $dr_t = \theta(t)\,dt + \sigma\,dW_t$ with no mean reversion. What is the limitation of this model for long-dated derivatives?

---

**Exercise 3.** In the CIR model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$, the forward rate volatility is state-dependent: $\sigma_f(t, T) = B'(T-t)\,\sigma\sqrt{r_t}$. Explain why this means the CIR model does not fit into the standard (deterministic volatility) HJM framework but does fit into the extended HJM framework with state-dependent volatilities. What are the consequences for analytical tractability?

---

**Exercise 4.** The Hull--White model $dr_t = (\theta(t) - \kappa r_t)\,dt + \sigma\,dW_t$ generalizes Vasicek by allowing a time-dependent drift. Show that the HJM volatility is still $\sigma_f(t, T) = \sigma e^{-\kappa(T-t)}$, independent of $\theta(t)$. Explain why the function $\theta(t)$ affects only the drift in the HJM representation and is determined by fitting the initial yield curve.

---

**Exercise 5.** A short-rate model generates bond prices of the affine form $P(t, T) = e^{A(T-t) - B(T-t)\,r_t}$. Show that this implies the forward rate $f(t, T) = -A'(T-t) + B'(T-t)\,r_t$ is affine in the short rate. Verify that the Markov property of $r_t$ is preserved and that the forward rate curve at any time $t$ is fully determined by the single state variable $r_t$.

---

**Exercise 6.** The Ritchken--Sankarasubramanian condition for a finite-dimensional Markov representation of an HJM model requires $\sigma(t, T) = h(t)\,g(T-t)$ for some functions $h$ and $g$ with $g(0) = 1$. Verify that the Hull--White volatility $\sigma e^{-\kappa(T-t)}$ satisfies this condition (with $h(t) = \sigma$ and $g(\tau) = e^{-\kappa\tau}$). Construct a volatility function that violates this condition and explain why the resulting HJM model would require an infinite number of state variables.

---

**Exercise 7.** Compare the Hull--White and Ho--Lee models as HJM special cases by computing: (a) the bond volatility $\Sigma(t, T) = \int_t^T \sigma_f(t, u)\,du$, (b) the HJM drift $\alpha(t, T) = \sigma_f(t, T)\,\Sigma(t, T)$, and (c) the variance of the $T$-maturity forward rate at time $t$, for both models. Which model produces more realistic dynamics for long-maturity forward rates and why?
