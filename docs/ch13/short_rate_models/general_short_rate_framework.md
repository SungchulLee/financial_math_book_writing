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

### Physical Measure $\mathbb{P}$

Under the real-world (physical) measure, the short rate follows:

$$
dr_t = \mu^{\mathbb{P}}(t, r_t) \, dt + \sigma(t, r_t) \, dW_t^{\mathbb{P}}
$$

The drift $\mu^{\mathbb{P}}$ reflects actual rate dynamics observed historically.

### Risk-Neutral Measure $\mathbb{Q}$

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
