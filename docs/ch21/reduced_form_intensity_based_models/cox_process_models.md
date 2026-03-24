# Cox Process Models

The **Cox process** (doubly stochastic Poisson process) provides the canonical construction of default times in reduced-form credit models. It generates surprise defaults governed by a stochastic intensity, ensuring analytical tractability and a clean separation of market and default information. This section develops the construction rigorously, derives survival probability formulas, and examines the principal intensity specifications used in practice.

---

## The Doubly Stochastic Construction

### Motivation

In deterministic-intensity models, the hazard rate $\lambda(t)$ is a known function. Real credit risk, however, evolves randomly with economic conditions. The Cox process makes the intensity itself a stochastic process while preserving the tractable exponential-survival structure.

### Ingredients

The construction requires:

1. A filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{Q})$ carrying market information
2. A non-negative, $\mathcal{F}_t$-adapted intensity process $(\lambda_t)_{t \ge 0}$ with $\int_0^t \lambda_s \, ds < \infty$ a.s. for all $t$
3. A unit-rate exponential random variable $E \sim \text{Exp}(1)$, **independent** of $\mathcal{F}_\infty$

### Default Time Construction

Define the **cumulative intensity** (or **integrated hazard**):

$$
\Lambda_t = \int_0^t \lambda_s \, ds
$$

The default time is:

$$
\tau = \inf\left\{t \ge 0 : \Lambda_t \ge E\right\}
$$

If $\Lambda_\infty := \lim_{t \to \infty} \Lambda_t < \infty$ with positive probability, then $\mathbb{Q}(\tau = \infty) = \mathbb{Q}(E > \Lambda_\infty) > 0$, meaning the firm may never default.

!!! tip "Intuition"
    Think of $\Lambda_t$ as a "credit clock" that ticks at a random speed $\lambda_t$. Default occurs when this clock reaches a random alarm time $E$. The alarm is set independently of how fast the clock runs, which is the key to the tractability of the construction.

### Equivalent Formulation via Uniform

An alternative construction uses $U \sim \text{Uniform}[0,1]$ independent of $\mathcal{F}_\infty$:

$$
\tau = \inf\{t \ge 0 : e^{-\Lambda_t} \le U\}
$$

Since $e^{-E} \sim \text{Uniform}[0,1]$, the two constructions are equivalent.

---

## Fundamental Properties

### Conditional Survival Probability

The central result of the Cox construction is the **conditional survival probability**. Given market information $\mathcal{F}_t$:

$$
\mathbb{Q}(\tau > T \mid \mathcal{F}_t) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T \lambda_s \, ds} \mid \mathcal{F}_t\right]
$$

On the pre-default event $\{\tau > t\}$, conditioning also on survival:

$$
\mathbb{Q}(\tau > T \mid \mathcal{G}_t) = \mathbf{1}_{\{\tau > t\}} \cdot \frac{\mathbb{E}^{\mathbb{Q}}\left[e^{-\Lambda_T} \mid \mathcal{F}_t\right]}{e^{-\Lambda_t}} = \mathbf{1}_{\{\tau > t\}} \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T \lambda_s \, ds} \mid \mathcal{F}_t\right]
$$

where $\mathcal{G}_t = \mathcal{F}_t \vee \sigma(\tau \wedge t)$ is the enlarged filtration.

??? info "Proof"
    On $\{\tau > t\}$, we know $E > \Lambda_t$. Then:

    $$
    \mathbb{Q}(\tau > T \mid \mathcal{F}_t, \tau > t) = \mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_t, E > \Lambda_t)
    $$

    Since $E$ is independent of $\mathcal{F}_\infty$ and $\Lambda_t$ is $\mathcal{F}_t$-measurable:

    $$
    = \frac{\mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_t)}{\mathbb{Q}(E > \Lambda_t \mid \mathcal{F}_t)} = \frac{\mathbb{E}[e^{-\Lambda_T} \mid \mathcal{F}_t]}{e^{-\Lambda_t}} = \mathbb{E}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t\right]
    $$

    $\square$

### Totally Inaccessible Default

Under the Cox construction, $\tau$ is a **totally inaccessible** $\mathcal{G}_t$-stopping time: there exists no sequence of $\mathcal{G}_t$-stopping times announcing $\tau$. This means default is always a genuine surprise, even given all available information.

### Immersion (H-Hypothesis)

The independence of $E$ from $\mathcal{F}_\infty$ ensures that the **immersion property** holds automatically: every $(\mathcal{F}_t, \mathbb{Q})$-martingale is also a $(\mathcal{G}_t, \mathbb{Q})$-martingale. This is the foundation of clean credit-market separation in reduced-form models.

---

## Compensator and Martingale

### Default Indicator Process

The default indicator $H_t = \mathbf{1}_{\{\tau \le t\}}$ is a submartingale. Its **Doob-Meyer decomposition** under $(\mathcal{G}_t, \mathbb{Q})$ is:

$$
H_t = M_t + A_t
$$

where the **compensator** is:

$$
A_t = \int_0^{t \wedge \tau} \lambda_s \, ds
$$

and the **compensated default process**:

$$
M_t = H_t - \int_0^{t \wedge \tau} \lambda_s \, ds = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} \lambda_s \, ds
$$

is a $(\mathcal{G}_t, \mathbb{Q})$-martingale.

### Interpretation

- Before default ($t < \tau$): $M_t = -\int_0^t \lambda_s ds$ decreases continuously
- At default ($t = \tau$): $M_t$ jumps by $+1$, partially offsetting the accumulated compensator
- After default ($t > \tau$): $M_t = 1 - \int_0^\tau \lambda_s ds$ remains constant

The martingale property of $M_t$ formalizes the idea that under the risk-neutral measure, the "surprise" component of default has zero expected value.

---

## CIR Intensity Model

### Dynamics

The **Cox-Ingersoll-Ross** (CIR) model is the most widely used specification for stochastic intensity:

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma\sqrt{\lambda_t} \, dW_t^{\mathbb{Q}}
$$

where:

- $\kappa > 0$: mean-reversion speed
- $\theta > 0$: long-run mean intensity
- $\sigma > 0$: volatility of intensity
- $W_t^{\mathbb{Q}}$: Brownian motion under the risk-neutral measure

### Non-Negativity (Feller Condition)

The intensity remains non-negative if and only if the **Feller condition** is satisfied:

$$
2\kappa\theta \ge \sigma^2
$$

When this holds, $\lambda_t > 0$ almost surely for all $t > 0$ (assuming $\lambda_0 > 0$). If the condition is violated, $\lambda_t$ can touch zero but is immediately reflected.

### Survival Probability (Closed Form)

The survival probability under CIR intensity has the **affine** form:

$$
S(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t\right] = A(\tau_h) \exp\left(-B(\tau_h) \lambda_t\right)
$$

where $\tau_h = T - t$ and the functions are:

$$
B(\tau_h) = \frac{2(e^{\gamma \tau_h} - 1)}{(\gamma + \kappa)(e^{\gamma \tau_h} - 1) + 2\gamma}
$$

$$
A(\tau_h) = \left[\frac{2\gamma \exp\left((\kappa + \gamma)\tau_h / 2\right)}{(\gamma + \kappa)(e^{\gamma \tau_h} - 1) + 2\gamma}\right]^{2\kappa\theta/\sigma^2}
$$

with:

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

??? info "Derivation via Riccati Equations"
    The affine structure arises because we seek $S(t,T) = e^{-\alpha(\tau_h) - \beta(\tau_h)\lambda_t}$ satisfying the Kolmogorov backward equation:

    $$
    \frac{\partial S}{\partial t} + \kappa(\theta - \lambda)\frac{\partial S}{\partial \lambda} + \frac{1}{2}\sigma^2 \lambda \frac{\partial^2 S}{\partial \lambda^2} - \lambda S = 0
    $$

    Substituting the exponential-affine ansatz and matching powers of $\lambda$ yields two ODEs:

    $$
    \beta'(\tau_h) = 1 - \kappa \beta(\tau_h) - \frac{1}{2}\sigma^2 \beta(\tau_h)^2, \quad \beta(0) = 0
    $$

    $$
    \alpha'(\tau_h) = \kappa\theta \beta(\tau_h), \quad \alpha(0) = 0
    $$

    The first is a Riccati equation with the solution given above for $B(\tau_h)$. The second integrates to give $\ln A(\tau_h) = \alpha(\tau_h)$.

    $\square$

---

## Other Intensity Specifications

### Vasicek (Ornstein-Uhlenbeck) Intensity

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma \, dW_t
$$

**Properties:**

- Gaussian process: $\lambda_t$ can become **negative** (economically problematic)
- Closed-form survival probability (affine structure)
- Simple calibration

**Survival probability:**

$$
S(t,T) = \exp\left(-B(\tau_h)\lambda_t - A(\tau_h)\right)
$$

with $B(\tau_h) = (1 - e^{-\kappa \tau_h})/\kappa$ and a corresponding $A(\tau_h)$.

### Log-Normal Intensity

$$
d\ln\lambda_t = \kappa(\theta - \ln\lambda_t) \, dt + \sigma \, dW_t
$$

**Properties:**

- Strictly positive intensity
- Heavier tails than CIR
- No closed-form survival probability (requires numerical methods)

### Jump-Diffusion Intensity

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma\sqrt{\lambda_t} \, dW_t + J \, dN_t
$$

where $N_t$ is a Poisson process and $J > 0$ is a random jump size.

**Properties:**

- Captures sudden credit deterioration (e.g., accounting fraud, rating downgrade)
- If $J \sim \text{Exp}(\mu_J)$, survival probability remains in closed form (extended affine)
- More realistic for crisis scenarios

---

## Pricing Under Cox Process Models

### General Pricing Formula

For a defaultable claim paying $X$ at maturity $T$ if no default and recovery $Z_\tau$ at default:

$$
V_t = \mathbf{1}_{\{\tau > t\}} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} X + \int_t^T e^{-\int_t^u (r_s + \lambda_s)ds} \lambda_u Z_u \, du \mid \mathcal{F}_t\right]
$$

The factor $e^{-\int_t^T \lambda_s ds}$ captures survival weighting, while $\lambda_u e^{-\int_t^u \lambda_s ds} du$ is the probability of defaulting in $(u, u+du)$ given survival to $u$.

### Defaultable Zero-Coupon Bond

Under recovery of market value (Duffie-Singleton):

$$
P^d(t,T) = \mathbf{1}_{\{\tau > t\}} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + (1-R)\lambda_s)ds} \mid \mathcal{F}_t\right]
$$

The intensity-adjusted discount rate is $r + (1-R)\lambda$, making the defaultable bond equivalent to a default-free bond with modified short rate.

### CDS Pricing

Under constant recovery $R$ and the Cox process framework, the par CDS spread is:

$$
s_{\text{par}} = \frac{(1-R)\int_0^T D(0,u) S(0,u) \lambda_u \, du}{\sum_{i=1}^n \Delta_i D(0,t_i) S(0,t_i)}
$$

where $D(0,u)$ is the risk-free discount factor and $S(0,u)$ is the survival probability.

---

## Simulation of Cox Process Default

### Algorithm

To simulate default times from a Cox process:

1. Simulate the intensity path $(\lambda_t)_{0 \le t \le T}$ on a time grid $\{t_0, t_1, \ldots, t_n\}$
2. Compute the cumulative intensity: $\Lambda_{t_k} = \sum_{j=0}^{k-1} \lambda_{t_j} \Delta t_j$
3. Draw $E \sim \text{Exp}(1)$
4. Find the first $t_k$ such that $\Lambda_{t_k} \ge E$
5. Interpolate to refine the default time: $\hat{\tau} \approx t_{k-1} + (E - \Lambda_{t_{k-1}})/\lambda_{t_{k-1}}$

### CIR Path Simulation

For the CIR intensity, common simulation schemes include:

**Exact simulation (via non-central chi-squared):**

$$
\lambda_T \mid \lambda_t \sim \frac{\sigma^2(1 - e^{-\kappa(T-t)})}{4\kappa} \chi^2\left(\frac{4\kappa\theta}{\sigma^2}, \frac{4\kappa e^{-\kappa(T-t)}}{\sigma^2(1 - e^{-\kappa(T-t)})}\lambda_t\right)
$$

**Euler-Maruyama (with reflection):**

$$
\lambda_{t+\Delta t} = \left|\lambda_t + \kappa(\theta - \lambda_t)\Delta t + \sigma\sqrt{\lambda_t^+} \sqrt{\Delta t} \, Z\right|
$$

where $Z \sim \mathcal{N}(0,1)$ and the absolute value enforces non-negativity.

---

## Numerical Example

**Parameters (CIR intensity):**

- Current intensity: $\lambda_0 = 1.5\%$
- Mean-reversion speed: $\kappa = 0.8$
- Long-run mean: $\theta = 2.5\%$
- Volatility of intensity: $\sigma = 8\%$
- Risk-free rate: $r = 3\%$ (constant)
- Horizon: $T = 5$ years

**Step 1: Compute $\gamma$**

$$
\gamma = \sqrt{0.64 + 2(0.0064)} = \sqrt{0.6528} = 0.8080
$$

**Step 2: Compute $B(5)$**

$$
B(5) = \frac{2(e^{4.04} - 1)}{(0.8080 + 0.8)(e^{4.04} - 1) + 2(0.8080)} = \frac{2(55.70)}{1.608 \times 55.70 + 1.616} = \frac{111.40}{91.13} = 1.222
$$

**Step 3: Compute $A(5)$**

$$
A(5) = \left[\frac{2(0.8080) e^{(0.8 + 0.8080)(2.5)}}{1.608(55.70) + 1.616}\right]^{2(0.8)(0.025)/(0.0064)}
$$

$$
= \left[\frac{1.616 \times e^{4.02}}{91.13}\right]^{6.25} = \left[\frac{1.616 \times 55.70}{91.13}\right]^{6.25} = (0.987)^{6.25} = 0.922
$$

**Step 4: Survival probability**

$$
S(0,5) = 0.922 \times e^{-1.222 \times 0.015} = 0.922 \times e^{-0.01833} = 0.922 \times 0.9818 = 0.905
$$

**5-year default probability:** $1 - 0.905 = 9.5\%$

**Feller condition check:** $2\kappa\theta = 2(0.8)(0.025) = 0.04 > \sigma^2 = 0.0064$ $\checkmark$

---

## Key Takeaways

- The Cox process constructs default times via $\tau = \inf\{t : \Lambda_t \ge E\}$ with $E$ independent of market information
- Conditional survival probability has the form $S(t,T) = \mathbb{E}[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t]$
- Immersion holds automatically, enabling clean separation of market and credit risk
- The compensated default process $M_t = H_t - \int_0^{t \wedge \tau} \lambda_s ds$ is a martingale
- CIR intensity is the standard specification, yielding closed-form affine survival probabilities
- The Feller condition $2\kappa\theta \ge \sigma^2$ ensures non-negativity of intensity
- Pricing defaultable claims reduces to computing expectations of the form $\mathbb{E}[e^{-\int(r+\lambda)ds}]$

---

## Further Reading

- Lando, D. (1998). On Cox processes and credit risky securities. *Review of Derivatives Research*, 2(2--3), 99--120.
- Duffie, D., & Singleton, K. J. (1999). Modeling term structures of defaultable bonds. *Review of Financial Studies*, 12(4), 687--720.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 8.
- Brigo, D., & Mercurio, F. (2006). *Interest Rate Models: Theory and Practice*. Springer, Chapter 21.

---

## Exercises

**Exercise 1.** In the Cox process construction, $\tau = \inf\{t : \Lambda_t \ge E\}$ where $E \sim \text{Exp}(1)$ is independent of $\mathcal{F}_\infty$ and $\Lambda_t = \int_0^t \lambda_s\,ds$. For constant intensity $\lambda$, show that $\tau \sim \text{Exp}(\lambda)$. Compute $\mathbb{P}(\tau > 5)$ for $\lambda = 2\%$.

---

**Exercise 2.** Verify the conditional survival formula: $\mathbb{P}(\tau > T \mid \mathcal{F}_T) = e^{-\int_0^T \lambda_s\,ds}$ under the Cox construction. Start from $\mathbb{P}(\tau > T \mid \mathcal{F}_T) = \mathbb{P}(E > \Lambda_T \mid \mathcal{F}_T)$ and use the independence of $E$ from $\mathcal{F}_\infty$.

---

**Exercise 3.** Explain why the independence of $E$ from $\mathcal{F}_\infty$ in the Cox construction is essential for the immersion (H-hypothesis) property. What would happen to the pricing framework if $E$ were correlated with market factors?

---

**Exercise 4.** For a CIR intensity process with $\kappa = 0.3$, $\theta = 1.5\%$, $\sigma = 6\%$, and $\lambda_0 = 2\%$, simulate (or describe the simulation algorithm for) the Cox process default time. Outline the steps: (a) simulate the intensity path, (b) compute $\Lambda_t$, (c) draw $E$, and (d) find $\tau$.

---

**Exercise 5.** Under the Cox construction, the default time $\tau$ is a totally inaccessible stopping time. Explain what this means intuitively: even though the intensity $\lambda_t$ is known at each time, default cannot be predicted in advance. Contrast this with the predictable default time in a structural model.

---

**Exercise 6.** Consider a two-name credit portfolio where each default time $\tau_i$ is constructed via independent Cox processes sharing a common stochastic intensity factor: $\lambda_t^{(i)} = a_i + b_i \cdot Z_t$ where $Z_t$ is a common CIR process. Explain how this construction induces default correlation. If $Z_t$ spikes, what happens to both default probabilities simultaneously?
