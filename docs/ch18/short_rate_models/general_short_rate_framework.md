# General Short-Rate Framework

Short-rate models describe interest rates by modeling the **instantaneous short rate** $r_t$. Once $r_t$ is specified under the risk-neutral measure, discount factors, bond prices, and derivative values follow from expectations of discounted cashflows. This section establishes the general framework before examining specific models.

---

## The Short Rate

### Definition

The **instantaneous short rate** $r_t$ (or simply "short rate") is the continuously compounded interest rate for infinitesimally short borrowing at time $t$:

$$
r_t = \lim_{\Delta t \to 0} \frac{1}{\Delta t} \log \frac{B_{t+\Delta t}}{B_t}
$$

where $B_t$ is the money-market account value.

### Interpretation

The short rate represents:
- The rate earned on an overnight deposit (in the limit)
- The instantaneous cost of borrowing
- The drift rate of the money-market account

In practice, proxies for $r_t$ include:
- Federal Funds rate (USD)
- EONIA/€STR (EUR)
- SONIA (GBP)
- Overnight repo rates

---

## The Money-Market Account

### Dynamics

The **money-market account** (or bank account) $B_t$ evolves according to:

$$
dB_t = r_t B_t \, dt, \quad B_0 = 1
$$

This is a non-stochastic ODE given a path of $r_t$. The solution is:

$$
B_t = \exp\left(\int_0^t r_s \, ds\right)
$$

### Economic Role

The money-market account:
- Represents risk-free investment by continuous rolling of overnight deposits
- Serves as the natural **numéraire** for risk-neutral pricing
- Accumulates interest at the (stochastic) short rate

### Stochastic Discount Factor

The reciprocal $B_t^{-1} = e^{-\int_0^t r_s ds}$ is the **stochastic discount factor** from 0 to $t$, used to discount future cashflows.

---

## Zero-Coupon Bond Pricing

### Fundamental Pricing Equation

Under the risk-neutral measure $\mathbb{Q}$, the price at time $t$ of a zero-coupon bond maturing at $T$ is:

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T r_s \, ds\right) \,\bigg|\, \mathcal{F}_t\right]
$$

This is the **discounted expectation** of the terminal payoff (which is 1).

### Key Properties

1. **Terminal condition:** $P(T, T) = 1$
2. **Positivity:** $P(t, T) > 0$ for all $t < T$
3. **Monotonicity:** $P(t, T_1) \geq P(t, T_2)$ for $T_1 \leq T_2$
4. **Martingale property:** $P(t, T)/B_t$ is a $\mathbb{Q}$-martingale

### From Bonds to Yield Curve

The zero rate implied by $P(t, T)$ is:

$$
z(t, T) = -\frac{\log P(t, T)}{T - t}
$$

The instantaneous forward rate is:

$$
f(t, T) = -\frac{\partial}{\partial T} \log P(t, T)
$$

---

## Markov Short-Rate Models

### General Form

A **Markov short-rate model** specifies $r_t$ as a diffusion:

$$
dr_t = \mu^{\mathbb{Q}}(t, r_t) \, dt + \sigma(t, r_t) \, dW_t^{\mathbb{Q}}
$$

where:
- $\mu^{\mathbb{Q}}(t, r)$: drift under risk-neutral measure
- $\sigma(t, r)$: volatility function
- $W_t^{\mathbb{Q}}$: Brownian motion under $\mathbb{Q}$

### Bond Price as Function of State

In a Markov model, the bond price depends only on current time and state:

$$
P(t, T) = P(t, T, r_t)
$$

This function solves a PDE (derived below) or can be computed via the Feynman-Kac expectation.

### Why Markov?

The Markov property:
- Enables PDE methods for pricing
- Allows for closed-form solutions in special cases
- Provides a finite-dimensional state space

Non-Markov models (e.g., certain path-dependent structures) require different techniques.

---

## The Bond Pricing PDE

### Derivation via Itô's Lemma

Let $V(t, r) = P(t, T, r)$ be the bond price. By Itô's lemma:

$$
dV = \left(\frac{\partial V}{\partial t} + \mu^{\mathbb{Q}} \frac{\partial V}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial r^2}\right) dt + \sigma \frac{\partial V}{\partial r} dW_t^{\mathbb{Q}}
$$

### No-Arbitrage Condition

The discounted bond price $V/B_t$ must be a martingale under $\mathbb{Q}$. This requires:

$$
\frac{\partial V}{\partial t} + \mu^{\mathbb{Q}} \frac{\partial V}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial r^2} = r V
$$

### Bond Pricing PDE

$$
\boxed{\frac{\partial P}{\partial t} + \mu^{\mathbb{Q}}(t, r) \frac{\partial P}{\partial r} + \frac{1}{2}\sigma(t, r)^2 \frac{\partial^2 P}{\partial r^2} - r P = 0}
$$

with terminal condition:

$$
P(T, T, r) = 1 \quad \text{for all } r
$$

### Boundary Conditions

Appropriate boundary conditions depend on the model:

| Boundary | Condition | Rationale |
|----------|-----------|-----------|
| $r \to +\infty$ | $P(t, T, r) \to 0$ | High rates heavily discount |
| $r \to -\infty$ | Model-dependent | Gaussian models allow negative rates |
| $r = 0$ | Reflection or absorption | CIR has $r = 0$ as boundary |

---

## Physical vs. Risk-Neutral Dynamics

### Physical Measure P

Under the real-world (physical) measure, the short rate follows:

$$
dr_t = \mu^{\mathbb{P}}(t, r_t) \, dt + \sigma(t, r_t) \, dW_t^{\mathbb{P}}
$$

The drift $\mu^{\mathbb{P}}$ reflects actual rate dynamics observed historically.

### Risk-Neutral Measure Q

Under $\mathbb{Q}$, the dynamics become:

$$
dr_t = \mu^{\mathbb{Q}}(t, r_t) \, dt + \sigma(t, r_t) \, dW_t^{\mathbb{Q}}
$$

where:

$$
\mu^{\mathbb{Q}}(t, r) = \mu^{\mathbb{P}}(t, r) - \lambda(t, r) \sigma(t, r)
$$

and $\lambda(t, r)$ is the **market price of interest rate risk**.

### Girsanov Transformation

The relationship between Brownian motions is:

$$
dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \lambda(t, r_t) \, dt
$$

### Implications

| Measure | Use | Drift |
|---------|-----|-------|
| $\mathbb{P}$ | Simulation, forecasting, risk management | Historical |
| $\mathbb{Q}$ | Pricing, no-arbitrage valuation | Risk-adjusted |

The volatility $\sigma(t, r)$ is the same under both measures.

---

## Relationship to HJM

### Short Rate as Limit

The short rate is the limit of the forward rate curve:

$$
r_t = f(t, t) = \lim_{T \to t^+} f(t, T)
$$

### Induced Forward Rates

A short-rate model **implies** forward rate dynamics. From:

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} \,|\, \mathcal{F}_t\right]
$$

one can derive $f(t, T)$ and its stochastic evolution.

### Markovian HJM

Not all HJM models are driven by a finite-dimensional short rate. Short-rate models correspond to **Markovian HJM** models with specific volatility structures.

---

## Classification of Short-Rate Models

### By Volatility Structure

| Model Class | Volatility $\sigma(t, r)$ | Example |
|-------------|---------------------------|---------|
| Gaussian | $\sigma(t)$ (constant in $r$) | Vasicek, Hull-White |
| Square-root | $\sigma \sqrt{r}$ | CIR |
| Lognormal | $\sigma r$ | Black-Karasinski |
| CEV | $\sigma r^\gamma$ | General |

### By Tractability

| Level | Property | Examples |
|-------|----------|----------|
| Closed-form bonds | Analytic $P(t, T, r)$ | Vasicek, CIR |
| Affine | $\log P$ linear in $r$ | Vasicek, CIR, Gaussian multi-factor |
| Quasi-affine | Fast numerical methods | Hull-White |
| General | Requires PDE/Monte Carlo | Black-Karasinski |

### By Number of Factors

| Type | State Variable | Flexibility |
|------|----------------|-------------|
| One-factor | $r_t$ | Limited yield curve dynamics |
| Two-factor | $(r_t, x_t)$ | Richer dynamics, steepening/flattening |
| Multi-factor | $(r_t, x_t^{(1)}, x_t^{(2)}, \ldots)$ | Full curve dynamics |

---

## Calibration Perspective

### Calibration Targets

Short-rate models are typically calibrated to:

1. **Today's yield curve:** Match initial discount factors $P(0, T)$
2. **Interest rate options:** Match cap/floor/swaption prices
3. **Historical dynamics:** Match observed volatility and mean reversion (for $\mathbb{P}$-measure parameters)

### Fitting the Initial Curve

A key requirement is **exact fit** to the initial term structure. Approaches include:

- **Time-dependent drift:** Hull-White extension with $\theta(t)$
- **Parameter functions:** Time-varying $\kappa(t)$, $\sigma(t)$
- **HJM framework:** Automatic fit by construction

### Trade-offs

| Feature | Simple Models | Extended Models |
|---------|---------------|-----------------|
| Analytical tractability | High | Lower |
| Curve fit | Approximate | Exact |
| Option calibration | Limited | Better |
| Stability | High | Can be sensitive |

---

## Key Takeaways

- Short-rate models specify $r_t$ under $\mathbb{Q}$; all bond prices follow
- The bond pricing equation $P(t, T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s ds}]$ is fundamental
- Markov models yield PDEs: $\partial_t P + \mu^{\mathbb{Q}} \partial_r P + \frac{1}{2}\sigma^2 \partial_{rr} P = rP$
- Physical and risk-neutral drifts differ by the market price of risk
- Model choice involves trade-offs between tractability and flexibility

---

## Further Reading

- Brigo & Mercurio, *Interest Rate Models—Theory and Practice*, Chapter 3
- Björk, *Arbitrage Theory in Continuous Time*, Chapters 22-23
- Filipović, *Term-Structure Models*, Chapters 5-6

---

## Exercises

**Exercise 1.** Starting from the bond pricing formula $P(t,T) = \mathbb{E}_t^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}]$, show that the instantaneous forward rate satisfies $f(t,T) = -\frac{\partial}{\partial T}\ln P(t,T)$ and that $P(t,T) = \exp(-\int_t^T f(t,u)\,du)$.

??? success "Solution to Exercise 1"
    Starting from the fundamental pricing formula under the risk-neutral measure $\mathbb{Q}$:

    $$
    P(t,T) = \mathbb{E}_t^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\right]
    $$

    **Forward rate.** By definition, $f(t,T) = -\frac{\partial}{\partial T}\ln P(t,T)$. We compute:

    $$
    \ln P(t,T) = \ln \mathbb{E}_t^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\right]
    $$

    Differentiating with respect to $T$ (under regularity conditions allowing interchange of differentiation and expectation):

    $$
    \frac{\partial}{\partial T}\ln P(t,T) = \frac{1}{P(t,T)}\frac{\partial}{\partial T}\mathbb{E}_t^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\right] = \frac{\mathbb{E}_t^{\mathbb{Q}}\!\left[-r_T\,e^{-\int_t^T r_s\,ds}\right]}{P(t,T)}
    $$

    Hence $f(t,T) = -\frac{\partial}{\partial T}\ln P(t,T)$.

    **Reconstruction formula.** Integrating $f(t,u)$ from $t$ to $T$:

    $$
    \int_t^T f(t,u)\,du = -\int_t^T \frac{\partial}{\partial u}\ln P(t,u)\,du = -\bigl[\ln P(t,u)\bigr]_{u=t}^{u=T} = -\ln P(t,T) + \ln P(t,t)
    $$

    Since $P(t,t) = 1$, we have $\ln P(t,t) = 0$, so

    $$
    \int_t^T f(t,u)\,du = -\ln P(t,T)
    $$

    Exponentiating:

    $$
    P(t,T) = \exp\!\left(-\int_t^T f(t,u)\,du\right)
    $$

    This shows that the entire discount curve can be recovered from the forward rate curve, and vice versa.

---

---

**Exercise 2.** Derive the PDE satisfied by the zero-coupon bond price $P(t,T) = F(t, r_t, T)$ in a general short-rate model $dr_t = \mu(t,r)\,dt + \sigma(t,r)\,dW_t$. Apply Ito's lemma and use the no-arbitrage condition to obtain the term-structure PDE.

??? success "Solution to Exercise 2"
    Consider a general short-rate model $dr_t = \mu(t,r)\,dt + \sigma(t,r)\,dW_t$ under $\mathbb{Q}$. The bond price $P(t,T) = F(t,r_t,T)$ is a function of $(t,r)$ for fixed $T$. Applying Ito's lemma:

    $$
    dF = \left(\frac{\partial F}{\partial t} + \mu(t,r)\frac{\partial F}{\partial r} + \frac{1}{2}\sigma(t,r)^2\frac{\partial^2 F}{\partial r^2}\right)dt + \sigma(t,r)\frac{\partial F}{\partial r}\,dW_t
    $$

    Under $\mathbb{Q}$, the discounted bond price $F/B_t$ must be a martingale, where $B_t = e^{\int_0^t r_s\,ds}$. By the product rule:

    $$
    d\!\left(\frac{F}{B_t}\right) = \frac{1}{B_t}\bigl(dF - r_t F\,dt\bigr)
    $$

    For this to be a martingale, the $dt$-coefficient must vanish:

    $$
    \frac{\partial F}{\partial t} + \mu(t,r)\frac{\partial F}{\partial r} + \frac{1}{2}\sigma(t,r)^2\frac{\partial^2 F}{\partial r^2} - r\,F = 0
    $$

    This is the **term-structure PDE**, valid for any Markov short-rate model. The terminal condition is $F(T,r,T) = 1$ for all $r$.

    By the Feynman-Kac theorem, the solution of this PDE is precisely

    $$
    F(t,r,T) = \mathbb{E}_t^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\bigg|\,r_t = r\right]
    $$

    confirming the equivalence of the PDE and expectation approaches.

---

---

**Exercise 3.** The money-market account satisfies $dB_t = r_t B_t\,dt$ with $B_0 = 1$. Show that $B_t = \exp(\int_0^t r_s\,ds)$. Why is this account risk-free in the instantaneous sense but not over finite horizons?

??? success "Solution to Exercise 3"
    The money-market account satisfies $dB_t = r_t B_t\,dt$ with $B_0 = 1$. This is a first-order linear ODE (given a path of $r_t$):

    $$
    \frac{dB_t}{B_t} = r_t\,dt
    $$

    Integrating both sides from $0$ to $t$:

    $$
    \int_0^t \frac{dB_s}{B_s} = \int_0^t r_s\,ds \implies \ln B_t - \ln B_0 = \int_0^t r_s\,ds
    $$

    Since $B_0 = 1$:

    $$
    B_t = \exp\!\left(\int_0^t r_s\,ds\right)
    $$

    **Instantaneously risk-free.** Over an infinitesimal interval $[t, t+dt]$, the return is $dB_t/B_t = r_t\,dt$, which is deterministic (no $dW_t$ term). There is no randomness in the instantaneous return.

    **Not risk-free over finite horizons.** Over a finite interval $[t, t+\Delta t]$, the accumulated return is $\int_t^{t+\Delta t} r_s\,ds$. Since $r_s$ is a stochastic process, this integral is random. At time $t$, one does not know the future path of $r_s$, so the total return $B_{t+\Delta t}/B_t = \exp(\int_t^{t+\Delta t} r_s\,ds)$ is uncertain. The money-market account is analogous to a floating-rate deposit: the rate adjusts continuously, but the cumulative interest over any finite period is not known in advance.

---

---

**Exercise 4.** Explain why the short-rate model approach is considered a "bottom-up" approach to term-structure modeling, while the HJM framework is "top-down." What are the main advantages and disadvantages of each?

??? success "Solution to Exercise 4"
    **Short-rate models (bottom-up).** One specifies the dynamics of a single state variable $r_t$ (or a small vector) under the risk-neutral measure. Bond prices for all maturities are then derived as expectations $P(t,T) = \mathbb{E}_t^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}]$. The entire yield curve is an output of the model, generated from the bottom (the short end) up to all maturities.

    **HJM framework (top-down).** One directly models the dynamics of the entire forward rate curve $\{f(t,T) : T \geq t\}$. The no-arbitrage drift restriction then constrains the relationship between forward rate drifts and volatilities. The short rate is recovered as $r_t = f(t,t)$.

    **Advantages of short-rate models:**

    - Finite-dimensional state: PDE and lattice methods apply efficiently.
    - Closed-form solutions exist for Vasicek, CIR, Hull-White.
    - Intuitive economic interpretation of the state variable.

    **Disadvantages of short-rate models:**

    - The implied forward rate dynamics may be unrealistic or difficult to control.
    - One-factor models produce perfectly correlated yield changes across maturities.
    - Fitting the initial term structure requires extensions (e.g., time-dependent parameters).

    **Advantages of HJM:**

    - Automatically fits the initial yield curve by construction.
    - Models the entire curve directly, allowing flexible correlation structures.
    - General framework nesting many specific models.

    **Disadvantages of HJM:**

    - Infinite-dimensional in general (the state is the entire curve).
    - Non-Markovian except for special volatility structures.
    - Implementation typically requires Monte Carlo or discretization of the full curve.

---

---

**Exercise 5.** In the general framework, the market price of risk $\lambda(t, r)$ links the physical and risk-neutral drifts: $\mu^{\mathbb{Q}} = \mu^{\mathbb{P}} - \lambda\sigma$. Explain the economic interpretation of $\lambda$ and discuss why it cannot be determined from bond prices alone.

??? success "Solution to Exercise 5"
    The market price of interest rate risk $\lambda(t,r)$ links the physical and risk-neutral drifts via

    $$
    \mu^{\mathbb{Q}}(t,r) = \mu^{\mathbb{P}}(t,r) - \lambda(t,r)\,\sigma(t,r)
    $$

    **Economic interpretation.** The quantity $\lambda(t,r)$ represents the excess return per unit of volatility that investors demand for bearing interest rate risk. Specifically, consider a bond with dynamics $dP/P = \mu_P\,dt + \sigma_P\,dW^{\mathbb{P}}$ under $\mathbb{P}$. No-arbitrage implies

    $$
    \frac{\mu_P - r}{\sigma_P} = \lambda(t,r)
    $$

    This is the Sharpe ratio of the bond: the risk premium per unit of interest rate exposure. A positive $\lambda$ means bond holders earn an excess return above the short rate (which is typical when the yield curve slopes upward on average).

    **Why $\lambda$ cannot be determined from bond prices alone.** Bond prices are determined entirely by the risk-neutral dynamics, i.e., by $\mu^{\mathbb{Q}}$ and $\sigma$. The risk-neutral drift $\mu^{\mathbb{Q}}$ absorbs both the physical drift $\mu^{\mathbb{P}}$ and the risk premium $\lambda\sigma$ into a single function. From observed bond prices (or equivalently the yield curve), one can extract $\mu^{\mathbb{Q}}$ and $\sigma$, but cannot disentangle $\mu^{\mathbb{P}}$ from $\lambda$ without additional information.

    To identify $\lambda$, one needs either:

    - Historical time-series data on rate movements (to estimate $\mu^{\mathbb{P}}$), or
    - A structural equilibrium model that specifies $\lambda$ in terms of economic fundamentals.

    This is a fundamental identification problem: cross-sectional bond data determine the pricing measure $\mathbb{Q}$ but not the physical measure $\mathbb{P}$.

---

---

**Exercise 6.** Show that if the short rate is deterministic ($\sigma = 0$), then $P(t,T) = e^{-\int_t^T r_s\,ds}$ exactly (no expectation needed). Use this to explain why stochastic models are necessary for pricing interest rate options.

??? success "Solution to Exercise 6"
    If $\sigma = 0$, then $r_t$ is deterministic: $dr_t = \mu(t,r_t)\,dt$, an ordinary differential equation. The path $\{r_s : s \in [t,T]\}$ is a known function of time (no randomness). Therefore the integral $\int_t^T r_s\,ds$ is a deterministic number, and the expectation in the bond pricing formula becomes trivial:

    $$
    P(t,T) = \mathbb{E}_t^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\right] = e^{-\int_t^T r_s\,ds}
    $$

    No expectation is needed because the quantity inside is non-random.

    **Implications for option pricing.** Consider a European call on a $T_2$-maturity bond struck at $K$, expiring at $T_1$. Its payoff is $\max(P(T_1, T_2) - K, 0)$. If rates are deterministic, then $P(T_1, T_2) = e^{-\int_{T_1}^{T_2} r_s\,ds}$ is a known constant. The option payoff is therefore either $(P(T_1,T_2) - K)^+$ with certainty or zero with certainty. The option has no time value; it is worth exactly its discounted intrinsic value:

    $$
    C = e^{-\int_0^{T_1} r_s\,ds}\max\!\left(e^{-\int_{T_1}^{T_2} r_s\,ds} - K,\, 0\right)
    $$

    This means all interest rate options (caps, floors, swaptions) would have zero implied volatility, and no non-trivial option pricing theory would be needed. Since market-quoted implied volatilities are strictly positive, stochastic short-rate models (with $\sigma > 0$) are essential for realistic option pricing. The randomness in future rates is precisely what gives interest rate options their value.
