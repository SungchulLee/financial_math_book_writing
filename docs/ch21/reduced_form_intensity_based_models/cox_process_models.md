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

Recall (see [§ Compensators and Martingales](compensators_and_martingales.md)) for the Doob-Meyer decomposition $H_t = M_t + A_t$ with compensator $A_t = \int_0^{t\wedge\tau}\lambda_s\,ds$, the compensated $(\mathcal{G}_t, \mathbb{Q})$-martingale $M_t = H_t - A_t$, and its pre-/post-default behavior.

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

Recall (see [§ Affine Intensity Models](affine_intensity_models.md)) for the closed-form affine survival $S(t,T) = A(\tau_h)\exp(-B(\tau_h)\lambda_t)$ under CIR intensity, the explicit $A$, $B$ with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$, and the underlying Riccati derivation.

---

## Other Intensity Specifications

Recall (see [§ Affine Intensity Models](affine_intensity_models.md)) for Vasicek OU intensity (Gaussian, can be negative) and affine jump-diffusion extensions ($+ J\,dN_t$, extended affine when $J \sim \text{Exp}(\mu_J)$). A log-normal alternative $d\ln\lambda_t = \kappa(\theta - \ln\lambda_t)\,dt + \sigma\,dW_t$ is strictly positive with heavier tails but lacks a closed-form survival probability.

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

??? success "Solution to Exercise 1"
    For constant intensity $\lambda$, the cumulative intensity is:

    $$
    \Lambda_t = \int_0^t \lambda\,ds = \lambda t
    $$

    The default time under the Cox construction is:

    $$
    \tau = \inf\{t \ge 0 : \Lambda_t \ge E\} = \inf\{t \ge 0 : \lambda t \ge E\} = \frac{E}{\lambda}
    $$

    Since $E \sim \text{Exp}(1)$, we need to show that $\tau = E/\lambda \sim \text{Exp}(\lambda)$.

    **Proof:** For any $t > 0$:

    $$
    \mathbb{P}(\tau > t) = \mathbb{P}\left(\frac{E}{\lambda} > t\right) = \mathbb{P}(E > \lambda t) = e^{-\lambda t}
    $$

    where the last equality uses the survival function of $\text{Exp}(1)$: $\mathbb{P}(E > x) = e^{-x}$ for $x \ge 0$.

    The survival function $\mathbb{P}(\tau > t) = e^{-\lambda t}$ is exactly that of an $\text{Exp}(\lambda)$ distribution. Therefore $\tau \sim \text{Exp}(\lambda)$. $\square$

    **Computation of $\mathbb{P}(\tau > 5)$ for $\lambda = 2\% = 0.02$:**

    $$
    \mathbb{P}(\tau > 5) = e^{-0.02 \times 5} = e^{-0.1} \approx 0.9048
    $$

    The 5-year survival probability is approximately $90.48\%$.

---

**Exercise 2.** Verify the conditional survival formula: $\mathbb{P}(\tau > T \mid \mathcal{F}_T) = e^{-\int_0^T \lambda_s\,ds}$ under the Cox construction. Start from $\mathbb{P}(\tau > T \mid \mathcal{F}_T) = \mathbb{P}(E > \Lambda_T \mid \mathcal{F}_T)$ and use the independence of $E$ from $\mathcal{F}_\infty$.

??? success "Solution to Exercise 2"
    We verify $\mathbb{Q}(\tau > T \mid \mathcal{F}_T) = e^{-\int_0^T \lambda_s\,ds}$.

    Starting from the definition, since $\tau = \inf\{t : \Lambda_t \ge E\}$, we have $\{\tau > T\} = \{E > \Lambda_T\}$. Therefore:

    $$
    \mathbb{Q}(\tau > T \mid \mathcal{F}_T) = \mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_T)
    $$

    Now we use the key property: $E \sim \text{Exp}(1)$ is **independent** of $\mathcal{F}_\infty$, and in particular independent of $\mathcal{F}_T$. Since $\Lambda_T = \int_0^T \lambda_s\,ds$ is $\mathcal{F}_T$-measurable (it is determined by the intensity path up to $T$, which is part of market information), we can treat $\Lambda_T$ as a constant when computing the conditional probability:

    $$
    \mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_T) = \mathbb{Q}(E > x)\big|_{x = \Lambda_T}
    $$

    Since $E \sim \text{Exp}(1)$:

    $$
    \mathbb{Q}(E > x) = e^{-x}
    $$

    Substituting $x = \Lambda_T$:

    $$
    \mathbb{Q}(\tau > T \mid \mathcal{F}_T) = e^{-\Lambda_T} = \exp\left(-\int_0^T \lambda_s\,ds\right)
    $$

    $\square$

    The independence of $E$ from $\mathcal{F}_\infty$ is the crucial ingredient: it allows us to "freeze" the $\mathcal{F}_T$-measurable quantity $\Lambda_T$ and evaluate the exponential survival function at that point. Without independence, the conditional probability would depend on the joint distribution of $E$ and $\Lambda_T$, destroying the clean exponential formula.

---

**Exercise 3.** Explain why the independence of $E$ from $\mathcal{F}_\infty$ in the Cox construction is essential for the immersion (H-hypothesis) property. What would happen to the pricing framework if $E$ were correlated with market factors?

??? success "Solution to Exercise 3"
    **Role of independence of $E$ from $\mathcal{F}_\infty$ in ensuring immersion:**

    The **immersion property** (or H-hypothesis) states that every $(\mathcal{F}_t, \mathbb{Q})$-martingale remains a $(\mathcal{G}_t, \mathbb{Q})$-martingale, where $\mathcal{G}_t = \mathcal{F}_t \vee \sigma(\tau \wedge t)$ is the enlarged filtration that includes default information.

    The independence of $E$ from $\mathcal{F}_\infty$ is essential because it ensures that **learning whether or not default has occurred provides no additional information about market variables**. Specifically:

    1. The conditional distribution of any $\mathcal{F}_\infty$-measurable random variable $Y$ given $\mathcal{G}_t$ (which includes default information) equals its conditional distribution given $\mathcal{F}_t$ alone, on the pre-default event $\{\tau > t\}$. This is because $E$ (and hence $\tau$) carries no information about $\mathcal{F}$-measurable quantities.

    2. For an $\mathcal{F}_t$-martingale $X_t$, the martingale property $\mathbb{E}[X_T \mid \mathcal{F}_t] = X_t$ automatically extends to $\mathbb{E}[X_T \mid \mathcal{G}_t] = X_t$ because the additional information in $\mathcal{G}_t$ (namely $\sigma(\tau \wedge t)$) is generated by $E$, which is independent of $X$.

    **What would happen if $E$ were correlated with market factors?**

    If $E$ were correlated with $\mathcal{F}_\infty$, several problems would arise:

    - **Immersion fails:** Observing that $\tau > t$ (i.e., $E > \Lambda_t$) would convey information about $E$, and through the correlation, information about market variables. This would change the conditional distributions of market quantities and $\mathcal{F}$-martingales would need additional drift compensation to remain $\mathcal{G}$-martingales.

    - **The survival formula breaks:** The key formula $S(t,T) = \mathbb{E}[e^{-\int_t^T \lambda_s\,ds} \mid \mathcal{F}_t]$ relies on the separation $\mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_T) = e^{-\Lambda_T}$, which requires independence. With correlation, one would need the joint distribution of $(E, \Lambda_T)$.

    - **Pricing becomes intractable:** The clean separation of market risk and credit risk is lost. Every pricing formula would need to account for the feedback between default events and market dynamics, requiring additional compensation terms in the Doob-Meyer decomposition of $\mathcal{F}$-martingales under $\mathcal{G}$.

    - **Market dynamics change upon default observation:** If the occurrence or non-occurrence of default reveals information about $E$, which is correlated with market factors, then observing survival or default would shift the conditional distribution of future asset prices, interest rates, etc. This "information leakage" fundamentally complicates the pricing framework.

---

**Exercise 4.** For a CIR intensity process with $\kappa = 0.3$, $\theta = 1.5\%$, $\sigma = 6\%$, and $\lambda_0 = 2\%$, simulate (or describe the simulation algorithm for) the Cox process default time. Outline the steps: (a) simulate the intensity path, (b) compute $\Lambda_t$, (c) draw $E$, and (d) find $\tau$.

??? success "Solution to Exercise 4"
    **Simulation algorithm for Cox process default time with CIR intensity:**

    Given parameters: $\kappa = 0.3$, $\theta = 1.5\% = 0.015$, $\sigma = 6\% = 0.06$, $\lambda_0 = 2\% = 0.02$.

    First, check the Feller condition: $2\kappa\theta = 2(0.3)(0.015) = 0.009$ and $\sigma^2 = 0.0036$. Since $0.009 > 0.0036$, the Feller condition is satisfied, so $\lambda_t > 0$ a.s.

    **(a) Simulate the intensity path:**

    Choose a time grid $0 = t_0 < t_1 < \cdots < t_n = T$ with step size $\Delta t = t_{k+1} - t_k$ (e.g., $\Delta t = 1/252$ for daily steps over $T = 10$ years).

    Use the Euler-Maruyama scheme with reflection:

    $$
    \lambda_{t_{k+1}} = \left|\lambda_{t_k} + \kappa(\theta - \lambda_{t_k})\Delta t + \sigma\sqrt{\lambda_{t_k}^+}\sqrt{\Delta t}\,Z_k\right|
    $$

    where $Z_k \sim \mathcal{N}(0,1)$ are i.i.d. and $\lambda^+ = \max(\lambda, 0)$. Alternatively, use the exact simulation via the non-central chi-squared distribution for higher accuracy.

    **(b) Compute the cumulative intensity $\Lambda_t$:**

    Using the trapezoidal rule:

    $$
    \Lambda_{t_k} = \sum_{j=0}^{k-1} \frac{\lambda_{t_j} + \lambda_{t_{j+1}}}{2} \Delta t
    $$

    or more simply with the rectangle rule: $\Lambda_{t_k} = \sum_{j=0}^{k-1} \lambda_{t_j} \Delta t$.

    **(c) Draw the exponential trigger:**

    Draw $E \sim \text{Exp}(1)$, independently of all the Brownian increments used in step (a). This can be done via $E = -\ln U$ where $U \sim \text{Uniform}(0,1)$.

    **(d) Find the default time $\tau$:**

    Scan through the cumulative intensity values to find the first index $k^*$ such that $\Lambda_{t_{k^*}} \ge E$:

    $$
    k^* = \min\{k : \Lambda_{t_k} \ge E\}
    $$

    If no such $k^*$ exists (i.e., $\Lambda_{t_n} < E$), then $\tau > T$ (no default in $[0, T]$).

    If $k^*$ exists, refine the default time by linear interpolation:

    $$
    \hat{\tau} = t_{k^*-1} + \frac{E - \Lambda_{t_{k^*-1}}}{\lambda_{t_{k^*-1}}} \approx t_{k^*-1} + \frac{E - \Lambda_{t_{k^*-1}}}{(\Lambda_{t_{k^*}} - \Lambda_{t_{k^*-1}})/\Delta t}
    $$

    This approximates the time within the interval $[t_{k^*-1}, t_{k^*}]$ at which the cumulative intensity crosses $E$.

    **Remarks:** By repeating steps (a)-(d) many times (say $N = 100{,}000$ paths), one obtains an empirical distribution of $\tau$. The fraction of paths with $\tau > T$ estimates $S(0,T)$, and the empirical CDF of $\tau$ estimates the default time distribution.

---

**Exercise 5.** Under the Cox construction, the default time $\tau$ is a totally inaccessible stopping time. Explain what this means intuitively: even though the intensity $\lambda_t$ is known at each time, default cannot be predicted in advance. Contrast this with the predictable default time in a structural model.

??? success "Solution to Exercise 5"
    **Totally inaccessible stopping time -- intuitive explanation:**

    A stopping time $\tau$ is **totally inaccessible** if there is no sequence of $\mathcal{G}_t$-stopping times $(\tau_n)_{n \ge 1}$ such that $\tau_n < \tau$ for all $n$ and $\tau_n \uparrow \tau$ almost surely. In other words, $\tau$ cannot be "announced" or "approached from below" by any sequence of predictable times.

    **Intuition for Cox process default:** Even though the intensity process $\lambda_t$ is known (adapted to $\mathcal{F}_t$) at each time $t$, this does not help predict the exact moment of default. The reason is the exponential trigger $E$, which is independent of all market information. Knowing $\lambda_t$ tells us the instantaneous rate of default, but the randomness of $E$ means we cannot determine when the cumulative intensity $\Lambda_t$ will cross $E$.

    Consider an analogy: knowing the speed of a ticking clock ($\lambda_t$) at every moment does not tell you when an independently set random alarm ($E$) will go off. You can compute the probability that the alarm goes off in the next instant, but you cannot predict the exact alarm time.

    More precisely: the conditional probability of default in the next instant is $\lambda_t\,dt$, which is infinitesimally small. There is no time $t$ at which default becomes "certain" or "nearly certain" in the next instant. The hazard rate $\lambda_t$ may be large, but it remains finite, so $\mathbb{Q}(\tau \in (t, t+dt] \mid \tau > t) = \lambda_t\,dt \to 0$ as $dt \to 0$.

    **Contrast with structural models:** In a structural model (e.g., Black-Cox), the default time is:

    $$
    \tau = \inf\{t : V_t \le D\}
    $$

    where $V_t$ is a continuous diffusion process. As $V_t$ approaches the barrier $D$ from above, the conditional probability of default in the next instant approaches 1. The continuity of $V_t$ means default is "seen coming" -- the hitting time of a continuous process to a fixed barrier is a **predictable** stopping time. One can construct an announcing sequence $\tau_n = \inf\{t : V_t \le D + 1/n\}$ with $\tau_n < \tau$ and $\tau_n \uparrow \tau$.

    In summary: structural models produce predictable defaults (visible approach to barrier), while Cox process models produce totally inaccessible defaults (sudden surprise), even with full knowledge of the intensity process.

---

**Exercise 6.** Consider a two-name credit portfolio where each default time $\tau_i$ is constructed via independent Cox processes sharing a common stochastic intensity factor: $\lambda_t^{(i)} = a_i + b_i \cdot Z_t$ where $Z_t$ is a common CIR process. Explain how this construction induces default correlation. If $Z_t$ spikes, what happens to both default probabilities simultaneously?

??? success "Solution to Exercise 6"
    **How the common factor induces default correlation:**

    Each default time $\tau_i$ ($i = 1, 2$) is constructed via an independent Cox process:

    $$
    \tau_i = \inf\{t : \Lambda_t^{(i)} \ge E_i\}, \quad \Lambda_t^{(i)} = \int_0^t \lambda_s^{(i)}\,ds
    $$

    where $E_1, E_2 \sim \text{Exp}(1)$ are independent of each other and of $\mathcal{F}_\infty$, and:

    $$
    \lambda_t^{(i)} = a_i + b_i Z_t
    $$

    with $Z_t$ following a common CIR process.

    **Conditional independence vs. unconditional dependence:**

    *Conditionally* on the entire path of $Z$, the two default times are independent because $E_1$ and $E_2$ are independent. Specifically:

    $$
    \mathbb{Q}(\tau_1 > t_1, \tau_2 > t_2 \mid \mathcal{F}_\infty) = \mathbb{Q}(\tau_1 > t_1 \mid \mathcal{F}_\infty) \cdot \mathbb{Q}(\tau_2 > t_2 \mid \mathcal{F}_\infty)
    $$

    However, *unconditionally*, the default times are dependent because they share the common factor $Z_t$:

    $$
    \mathbb{Q}(\tau_1 > t_1, \tau_2 > t_2) = \mathbb{E}\left[e^{-\int_0^{t_1} \lambda_s^{(1)}\,ds} \cdot e^{-\int_0^{t_2} \lambda_s^{(2)}\,ds}\right]
    $$

    This expectation does **not** factor into a product $\mathbb{E}[e^{-\int \lambda^{(1)}ds}] \cdot \mathbb{E}[e^{-\int \lambda^{(2)}ds}]$ because $\lambda^{(1)}$ and $\lambda^{(2)}$ are both functions of the same process $Z_t$.

    **Mechanism of correlation:** The common factor $Z_t$ drives both intensities simultaneously. When $Z_t$ is high, both $\lambda_t^{(1)} = a_1 + b_1 Z_t$ and $\lambda_t^{(2)} = a_2 + b_2 Z_t$ are high (assuming $b_1, b_2 > 0$), making both defaults more likely. When $Z_t$ is low, both intensities are low, making both defaults less likely. This co-movement in default probabilities creates positive default correlation.

    **If $Z_t$ spikes:**

    A sudden increase in $Z_t$ causes:

    - $\lambda_t^{(1)}$ increases by $b_1 \Delta Z_t$ and $\lambda_t^{(2)}$ increases by $b_2 \Delta Z_t$
    - Both cumulative intensities $\Lambda_t^{(1)}$ and $\Lambda_t^{(2)}$ accelerate
    - The probabilities $\mathbb{Q}(\tau_i \in (t, t+dt] \mid \tau_i > t) = \lambda_t^{(i)}\,dt$ both increase simultaneously
    - If the spike is large enough, both $\Lambda_t^{(i)}$ may cross their respective thresholds $E_i$ in a short window, producing **clustered defaults**

    This is the mechanism by which common factor models generate default clustering during crises (e.g., multiple financial institutions defaulting during 2008). The magnitudes $b_1$ and $b_2$ control each name's sensitivity to the systematic factor, while $a_1$ and $a_2$ represent idiosyncratic baseline default risk. The default correlation increases with $b_1 \cdot b_2$ relative to the overall intensity levels.
