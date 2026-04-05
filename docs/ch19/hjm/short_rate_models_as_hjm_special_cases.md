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

??? success "Solution to Exercise 1"

    **Step 1: Compute the forward rate from the bond price.**

    The Vasicek bond price is $P(t, T) = A(T-t)\,e^{-B(T-t)\,r_t}$ where $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$.

    Taking the log:

    $$
    \ln P(t, T) = \ln A(T-t) - B(T-t)\,r_t
    $$

    The forward rate is:

    $$
    f(t, T) = -\frac{\partial}{\partial T}\ln P(t, T) = -\frac{\partial \ln A}{\partial T}(\tau) + \frac{\partial B}{\partial T}(\tau)\,r_t
    $$

    where $\tau = T - t$.

    **Step 2: Compute $\partial B / \partial T$.**

    $$
    B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}, \quad \frac{\partial B}{\partial T} = \frac{dB}{d\tau} = e^{-\kappa\tau}
    $$

    **Step 3: Identify the diffusion coefficient.**

    Since $f(t, T) = -\frac{\partial \ln A}{\partial T} + e^{-\kappa(T-t)}\,r_t$ and $r_t$ satisfies $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$:

    $$
    df(t, T) = e^{-\kappa(T-t)}\,dr_t + \kappa e^{-\kappa(T-t)}\,r_t\,dt + \text{deterministic terms from } A
    $$

    The stochastic part comes entirely from $e^{-\kappa(T-t)}\,dr_t$, and the diffusion coefficient of $dr_t$ is $\sigma$. Therefore:

    $$
    \sigma_f(t, T) = \sigma\,e^{-\kappa(T-t)}
    $$

    This is the HJM volatility for the Vasicek model. The exponential decay reflects mean reversion: long-maturity forward rates are less sensitive to the current short-rate shock than short-maturity rates. $\square$

---

**Exercise 2.** For the Ho--Lee model with constant HJM volatility $\sigma(t, T) = \sigma$, verify the drift condition $\alpha(t, T) = \sigma^2(T - t)$ and show that the short rate $r_t = f(t, t)$ follows $dr_t = \theta(t)\,dt + \sigma\,dW_t$ with no mean reversion. What is the limitation of this model for long-dated derivatives?

??? success "Solution to Exercise 2"

    **Step 1: Verify the drift condition.**

    With $\sigma(t, T) = \sigma$:

    $$
    \alpha(t, T) = \sigma \int_t^T \sigma\,du = \sigma^2(T - t)
    $$

    $\checkmark$

    **Step 2: Derive the short-rate dynamics.**

    The forward rate SDE is $df(t, T) = \sigma^2(T-t)\,dt + \sigma\,dW_t$. Setting $T = t$:

    $$
    r_t = f(t, t) = f(0, t) + \int_0^t \sigma^2(t-s)\,ds + \sigma W_t = f(0, t) + \frac{\sigma^2 t^2}{2} + \sigma W_t
    $$

    Differentiating:

    $$
    dr_t = \left[\frac{\partial f(0, t)}{\partial t} + \sigma^2 t\right]dt + \sigma\,dW_t = \theta(t)\,dt + \sigma\,dW_t
    $$

    where $\theta(t) = f'(0, t) + \sigma^2 t$. There is **no mean reversion** ($\kappa = 0$): the drift $\theta(t)$ is purely deterministic and does not depend on $r_t$.

    **Step 3: Limitation for long-dated derivatives.**

    Since the Ho--Lee model has no mean reversion, the short rate is a Gaussian process with variance $\sigma^2 t$ that grows linearly in time. For long-dated derivatives:

    1. The probability of negative rates grows over time: $\mathbb{P}(r_t < 0) \to 1/2$ as $t \to \infty$ (for suitable drift).
    2. The forward rate variance $\text{Var}(f(t, T)) = \sigma^2 t$ grows without bound, making long-dated forward rates excessively volatile.
    3. All forward rates are perfectly correlated (correlation = 1), so the model cannot capture steepening, flattening, or butterfly movements.

    These limitations make the Ho--Lee model unsuitable for pricing long-dated or curve-shape-sensitive derivatives.

---

**Exercise 3.** In the CIR model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$, the forward rate volatility is state-dependent: $\sigma_f(t, T) = B'(T-t)\,\sigma\sqrt{r_t}$. Explain why this means the CIR model does not fit into the standard (deterministic volatility) HJM framework but does fit into the extended HJM framework with state-dependent volatilities. What are the consequences for analytical tractability?

??? success "Solution to Exercise 3"

    **Standard HJM framework** assumes the volatility $\sigma(t, T)$ is a **deterministic** function of $(t, T)$ (or possibly adapted but dependent on the current forward curve in a prescribed way). In the CIR model, $\sigma_f(t, T) = B'(T-t)\,\sigma\sqrt{r_t}$, which depends on the **stochastic** short rate $r_t$. This state dependence means:

    1. The CIR volatility is **not** a deterministic function of $(t, T)$ alone. It is adapted (depends on $\mathcal{F}_t$) and random.

    2. The standard (Gaussian) HJM framework assumes deterministic volatilities, which guarantees that forward rates are Gaussian and that bond prices have lognormal dynamics. The CIR model does not fit this framework because:
        - Forward rates are **not** normally distributed (they inherit the non-central chi-squared distribution of $r_t$).
        - The short rate is **non-negative** (bounded below by zero), unlike Gaussian models.

    3. The **extended HJM framework** allows the volatility to be a functional of the current state:

        $$
        \sigma_f(t, T) = \sigma_f(t, T, r_t) \quad \text{or more generally} \quad \sigma_f(t, T, f(t, \cdot))
        $$

        The CIR model fits naturally into this extension with $\sigma_f(t, T) = B'(T-t)\,\sigma\sqrt{r_t}$.

    **Consequences for analytical tractability:**

    - Loss of Gaussian structure: bond option prices no longer follow simple Black-type formulas.
    - The CIR model retains tractability through its **affine structure**: bond prices are exponential-affine in $r_t$, and the characteristic function of $r_t$ is known in closed form, enabling Fourier-based option pricing.
    - In the general state-dependent HJM framework, closed-form solutions are rare. Monte Carlo simulation or PDE methods are typically required.
    - The state-dependent volatility also complicates the existence and uniqueness theory for the HJM SDE (additional regularity conditions on the volatility functional are needed).

---

**Exercise 4.** The Hull--White model $dr_t = (\theta(t) - \kappa r_t)\,dt + \sigma\,dW_t$ generalizes Vasicek by allowing a time-dependent drift. Show that the HJM volatility is still $\sigma_f(t, T) = \sigma e^{-\kappa(T-t)}$, independent of $\theta(t)$. Explain why the function $\theta(t)$ affects only the drift in the HJM representation and is determined by fitting the initial yield curve.

??? success "Solution to Exercise 4"

    **Step 1: Show the HJM volatility is independent of $\theta(t)$.**

    The Hull--White diffusion coefficient is $\gamma(t, r_t) = \sigma$ (constant, independent of $\theta(t)$). The bond price function $B(\tau)$ satisfies the Riccati ODE $B'(\tau) = 1 - \kappa B(\tau)$ with $B(0) = 0$, giving $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$.

    The HJM volatility is:

    $$
    \sigma_f(t, T) = \frac{\partial B(T-t)}{\partial T}\,\gamma = e^{-\kappa(T-t)} \cdot \sigma = \sigma e^{-\kappa(T-t)}
    $$

    This depends only on $\sigma$ and $\kappa$, **not** on $\theta(t)$. $\checkmark$

    **Step 2: Explain why $\theta(t)$ affects only the drift.**

    In the HJM representation:

    $$
    df(t, T) = \alpha(t, T)\,dt + \sigma e^{-\kappa(T-t)}\,dW_t
    $$

    The volatility $\sigma e^{-\kappa(T-t)}$ determines the no-arbitrage drift via $\alpha(t, T) = \sigma e^{-\kappa(T-t)}\,\Sigma(t, T)$. The function $\theta(t)$ enters through the **initial forward curve** $f(0, T)$. Specifically, when the Hull--White model is used:

    $$
    \theta(t) = \frac{\partial f(0, t)}{\partial t} + \kappa\,f(0, t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    In the HJM framework, $\theta(t)$ is not a separate parameter --- it is implicitly determined by $f(0, T)$. The HJM model takes $f(0, T)$ as input (from market data), which automatically encodes the $\theta(t)$ needed for exact calibration. This is why HJM matches the initial curve by construction: the function $\theta(t)$ is absorbed into the initial condition $f(0, T)$.

---

**Exercise 5.** A short-rate model generates bond prices of the affine form $P(t, T) = e^{A(T-t) - B(T-t)\,r_t}$. Show that this implies the forward rate $f(t, T) = -A'(T-t) + B'(T-t)\,r_t$ is affine in the short rate. Verify that the Markov property of $r_t$ is preserved and that the forward rate curve at any time $t$ is fully determined by the single state variable $r_t$.

??? success "Solution to Exercise 5"

    **Step 1: Compute the forward rate.**

    Given $P(t, T) = e^{A(T-t) - B(T-t)\,r_t}$, let $\tau = T - t$:

    $$
    \ln P(t, T) = A(\tau) - B(\tau)\,r_t
    $$

    $$
    f(t, T) = -\frac{\partial}{\partial T}\ln P(t, T) = -A'(\tau) + B'(\tau)\,r_t
    $$

    This is **affine in $r_t$**: $f(t, T) = a(\tau) + b(\tau)\,r_t$ where $a(\tau) = -A'(\tau)$ and $b(\tau) = B'(\tau)$.

    **Step 2: Verify the Markov property is preserved.**

    Since $f(t, T)$ depends on $T$ only through $\tau = T - t$ and on the state only through $r_t$, the entire forward curve at time $t$ is:

    $$
    T \mapsto f(t, T) = a(T-t) + b(T-t)\,r_t
    $$

    Given $r_t$, every forward rate $f(t, T)$ for all $T \geq t$ is **deterministically determined**. No additional information about the past trajectory of $r_s$ for $s < t$ is needed. This confirms the Markov property.

    **Step 3: Forward curve determined by a single state variable.**

    The forward curve is a one-parameter family $\{f(t, T) : T \geq t\}$, but it is fully described by the single number $r_t$. The "shape functions" $a(\tau)$ and $b(\tau)$ are known deterministic functions (solutions of ODEs arising from the affine term structure). Therefore, the infinite-dimensional HJM state collapses to a single dimension.

    Bond prices are also determined by $r_t$ alone:

    $$
    P(t, T) = \exp\!\left(-\int_t^T f(t, u)\,du\right) = \exp\!\left(-\int_0^{T-t} [a(s) + b(s)\,r_t]\,ds\right)
    $$

    which recovers the affine form $e^{A(\tau) - B(\tau)\,r_t}$ with $A(\tau) = -\int_0^\tau a(s)\,ds$ and $B(\tau) = \int_0^\tau b(s)\,ds$. $\square$

---

**Exercise 6.** The Ritchken--Sankarasubramanian condition for a finite-dimensional Markov representation of an HJM model requires $\sigma(t, T) = h(t)\,g(T-t)$ for some functions $h$ and $g$ with $g(0) = 1$. Verify that the Hull--White volatility $\sigma e^{-\kappa(T-t)}$ satisfies this condition (with $h(t) = \sigma$ and $g(\tau) = e^{-\kappa\tau}$). Construct a volatility function that violates this condition and explain why the resulting HJM model would require an infinite number of state variables.

??? success "Solution to Exercise 6"

    **Step 1: Verify the Hull--White volatility satisfies the RS condition.**

    The Hull--White HJM volatility is $\sigma_f(t, T) = \sigma e^{-\kappa(T-t)}$. This has the separable form $h(t)\,g(T-t)$ with:

    $$
    h(t) = \sigma \quad (\text{constant}), \qquad g(\tau) = e^{-\kappa\tau}
    $$

    We verify $g(0) = e^0 = 1$. $\checkmark$

    The Ritchken--Sankarasubramanian condition is satisfied, so the model admits a finite-dimensional Markov representation (specifically, a one-factor Markov model in $r_t$).

    **Step 2: Construct a volatility that violates the condition.**

    Consider:

    $$
    \sigma_f(t, T) = \sigma(T)\,e^{-\kappa(T-t)}
    $$

    where $\sigma(T)$ depends on the **calendar maturity** $T$ rather than just time-to-maturity $T - t$. For example, $\sigma(T) = \sigma_0(1 + 0.1\sin T)$.

    This cannot be written as $h(t)\,g(T-t)$ for any functions $h$ and $g$, because the dependence on $T$ and $t$ does not separate: the factor $\sigma(T) = \sigma_0(1 + 0.1\sin(t + \tau))$ mixes $t$ and $\tau = T - t$ in a non-separable way.

    **Step 3: Why violation implies infinite-dimensionality.**

    When the RS condition is violated, the forward rate $f(t, T)$ at different maturities $T$ cannot be expressed as deterministic functions of a finite number of state variables. Informally, the stochastic integral $\int_0^t \sigma_f(s, T)\,dW_s$ has different $T$-dependence at each $s$, and no finite collection of processes can capture this variation across all $T$.

    Formally, the forward curve $T \mapsto f(t, T)$ cannot be reconstructed from any finite-dimensional statistic of the path $\{W_s : 0 \leq s \leq t\}$. One would need to track, in principle, infinitely many state variables to describe the curve evolution --- making the model truly infinite-dimensional and requiring full curve simulation for numerical implementation.

---

**Exercise 7.** Compare the Hull--White and Ho--Lee models as HJM special cases by computing: (a) the bond volatility $\Sigma(t, T) = \int_t^T \sigma_f(t, u)\,du$, (b) the HJM drift $\alpha(t, T) = \sigma_f(t, T)\,\Sigma(t, T)$, and (c) the variance of the $T$-maturity forward rate at time $t$, for both models. Which model produces more realistic dynamics for long-maturity forward rates and why?

??? success "Solution to Exercise 7"

    We compute three quantities for both models. Let $\tau = T - t$.

    **(a) Bond volatility $\Sigma(t, T)$.**

    **Ho--Lee** ($\sigma_f(t, T) = \sigma$):

    $$
    \Sigma_{\text{HL}}(t, T) = \int_t^T \sigma\,du = \sigma\,\tau
    $$

    **Hull--White** ($\sigma_f(t, T) = \sigma e^{-\kappa\tau}$, using $\tau = T - t$):

    $$
    \Sigma_{\text{HW}}(t, T) = \int_t^T \sigma e^{-\kappa(u-t)}\,du = \frac{\sigma}{\kappa}(1 - e^{-\kappa\tau})
    $$

    Note: $\Sigma_{\text{HL}}$ grows linearly in $\tau$, while $\Sigma_{\text{HW}}$ saturates at $\sigma/\kappa$.

    **(b) HJM drift $\alpha(t, T)$.**

    **Ho--Lee:**

    $$
    \alpha_{\text{HL}}(t, T) = \sigma \cdot \sigma\tau = \sigma^2\tau
    $$

    **Hull--White:**

    $$
    \alpha_{\text{HW}}(t, T) = \sigma e^{-\kappa\tau} \cdot \frac{\sigma}{\kappa}(1 - e^{-\kappa\tau}) = \frac{\sigma^2}{\kappa}e^{-\kappa\tau}(1 - e^{-\kappa\tau})
    $$

    The Ho--Lee drift grows linearly, while the Hull--White drift is bounded and decays for large $\tau$.

    **(c) Variance of $f(t, T)$.**

    Since $f(t, T) = f(0, T) + \int_0^t \alpha(s, T)\,ds + \int_0^t \sigma_f(s, T)\,dW_s$, the variance is:

    $$
    \text{Var}(f(t, T)) = \int_0^t \sigma_f(s, T)^2\,ds
    $$

    **Ho--Lee:**

    $$
    \text{Var}_{\text{HL}}(f(t, T)) = \int_0^t \sigma^2\,ds = \sigma^2 t
    $$

    This is **independent of $T$**: all maturities have the same variance, growing linearly in $t$.

    **Hull--White:**

    $$
    \text{Var}_{\text{HW}}(f(t, T)) = \int_0^t \sigma^2 e^{-2\kappa(T-s)}\,ds = \sigma^2 e^{-2\kappa T}\int_0^t e^{2\kappa s}\,ds = \frac{\sigma^2}{2\kappa}e^{-2\kappa(T-t)}(e^{2\kappa t} - 1)
    $$

    For fixed $t$, this **decreases with $T$**: long-maturity forward rates have smaller variance than short-maturity rates.

    **Which model is more realistic?**

    The Hull--White model produces more realistic dynamics for long-maturity forward rates because:

    1. The **declining volatility** with maturity matches empirical observations: long-term rates are less volatile than short-term rates.
    2. The **bounded bond volatility** prevents unrealistic explosive behavior in bond price dynamics.
    3. The **mean reversion** stabilizes the short rate around a long-run level, avoiding the unbounded variance growth of Ho--Lee.

    The Ho--Lee model's constant volatility across maturities is counterfactual: in practice, the 30-year forward rate is substantially less volatile than the 1-year forward rate. For long-dated derivatives, the Ho--Lee model overestimates the uncertainty in long-maturity rates, leading to mispricing.
