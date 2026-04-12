# Compensators and Martingales

The martingale structure of default processes is formalized using **compensators**. This perspective is essential for rigorous pricing in reduced-form credit models, providing the mathematical foundation for arbitrage-free valuation and hedging of defaultable claims.

---

## The Default Indicator Process

### Definition

The **default indicator** (or default process) is:

$$
H_t := \mathbf{1}_{\{\tau \le t\}}
$$

where $\tau$ is the default time.

### Properties

- **Right-continuous:** $H_t$ has right-continuous sample paths
- **Increasing:** $H_t$ is non-decreasing (once default occurs, it stays defaulted)
- **Jump process:** $H_t$ jumps from 0 to 1 at the single time $\tau$
- **Adapted:** $H_t$ is $\mathcal{G}_t$-adapted when $\tau$ is a stopping time

### Submartingale Property

Since $H_t$ is increasing, it is automatically a **submartingale**:

$$
\mathbb{E}[H_T \mid \mathcal{G}_t] \ge H_t \quad \text{for } T \ge t
$$

The Doob-Meyer decomposition guarantees the existence of a predictable compensator.

---

## The Compensator

### Definition

The **compensator** of the default indicator $H_t$ is the unique predictable increasing process $A_t$ such that:

$$
M_t := H_t - A_t
$$

is a $(\mathcal{G}_t, \mathbb{Q})$-martingale.

### Interpretation

The compensator $A_t$ represents the **cumulative expected default** up to time $t$. It "compensates" for the jump in $H_t$ to create a martingale.

Intuitively:
- $H_t$ is what actually happens (default or not)
- $A_t$ is what was expected to happen
- $M_t = H_t - A_t$ is the surprise (unpredictable) component

---

## Compensator Under Intensity Models

### Explicit Form

Under the standard intensity framework, the compensator is:

$$
A_t = \int_0^{t \wedge \tau} \lambda_s \, ds
$$

where $\lambda_s$ is the default intensity and $t \wedge \tau = \min(t, \tau)$.

**Key observation:** The integral is only up to $t \wedge \tau$ (stopped at default). After default, $A_t$ remains constant.

### The Compensated Martingale

The process:

$$
M_t = H_t - \int_0^{t \wedge \tau} \lambda_s \, ds = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} \lambda_s \, ds
$$

is a $(\mathcal{G}_t, \mathbb{Q})$-martingale with $M_0 = 0$.

### Verification (Heuristic)

Pre-default ($t < \tau$): $H_t = 0$ and $A_t = \int_0^t \lambda_s ds$

At default ($t = \tau$): $H_t$ jumps by +1, while $A_t$ has been accumulating continuously

The "balance" is maintained in expectation:

$$
\mathbb{E}[dH_t \mid \mathcal{G}_{t-}] = \lambda_t \, dt = dA_t
$$

---

## Martingale Representation

### Differential Form

In differential notation:

$$
dM_t = dH_t - \lambda_t \mathbf{1}_{\{\tau > t\}} \, dt
$$

Since $dH_t = \mathbf{1}_{\{\tau \in dt\}}$ (the jump indicator), this reads:

$$
dM_t = dH_t - \lambda_t \mathbf{1}_{\{\tau \ge t\}} \, dt
$$

### Jump Martingale

The martingale $M_t$ is a **purely discontinuous** (jump) martingale:
- It is constant between jumps
- It has a single jump of size $1 - \int_0^{\tau} \lambda_s ds$ at time $\tau$
- No continuous martingale component

### Quadratic Variation

The predictable quadratic variation is:

$$
\langle M \rangle_t = A_t = \int_0^{t \wedge \tau} \lambda_s \, ds
$$

The actual quadratic variation is:

$$
[M]_t = H_t = \mathbf{1}_{\{\tau \le t\}}
$$

---

## Role in Pricing

### Arbitrage-Free Pricing Framework

The martingale property of $M_t$ is central to pricing:

1. **Risk-neutral expectation:** Prices are expectations of discounted payoffs
2. **Martingale condition:** Ensures no arbitrage
3. **Compensator structure:** Determines how default risk enters prices

### The Key Pricing Decomposition

For any $\mathcal{G}_T$-measurable payoff $X$:

$$
\mathbb{E}^{\mathbb{Q}}[X \mid \mathcal{G}_t] = \mathbb{E}^{\mathbb{Q}}[X \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{G}_t] + \mathbb{E}^{\mathbb{Q}}[X \cdot \mathbf{1}_{\{\tau \le T\}} \mid \mathcal{G}_t]
$$

The compensator structure allows explicit computation of each term.

### Pre-Default Pricing Formula

On $\{\tau > t\}$, for a payoff $Y(\tau)$ at default:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} Y(\tau) \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u r_s ds} Y(u) \lambda_u S(t,u) \, du \mid \mathcal{F}_t\right]
$$

where $S(t,u) = e^{-\int_t^u \lambda_s ds}$ is the survival probability.

This formula **converts a random stopping time expectation to a deterministic integral**, which is computationally tractable.

---

## The Fundamental Credit Pricing Formula

### General Defaultable Claim

Consider a claim paying:
- $C(T)$ at maturity $T$ if no default
- $R(\tau)$ at default time $\tau$ if $\tau \le T$

The price at time $t$ (on $\{\tau > t\}$) is:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} C(T) \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} R(\tau) \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right]
$$

Using the compensator representation:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} C(T) \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s) ds} R(u) \lambda_u \, du \mid \mathcal{F}_t\right]
$$

### Interpretation

1. **First term:** Survival-weighted terminal payoff, discounted at rate $r + \lambda$
2. **Second term:** Expected recovery payment, integrated over all possible default times

The intensity $\lambda_t$ acts like an **additional discount rate** representing credit risk.

---

## Connection to Enlargement of Filtration

### Progressive Enlargement and Compensators

Under progressive enlargement $\mathcal{G}_t = \mathcal{F}_t \vee \sigma(\tau \wedge t)$:

The compensator formula:

$$
A_t = \int_0^{t \wedge \tau} \lambda_s \, ds
$$

arises naturally from the **intensity hypothesis**: the conditional default probability is governed by $\lambda_t$.

### Immersion Preserved

When immersion holds:
- $\mathcal{F}$-martingales remain $\mathcal{G}$-martingales
- No additional compensator terms for market processes
- Clean separation of default and market risks

### Without Immersion

If immersion fails, $\mathcal{F}$-martingales $X_t$ need compensation:

$$
X_t - \int_0^{t \wedge \tau} \frac{d\langle X, G \rangle_s}{G_{s-}}
$$

is a $\mathcal{G}$-martingale, where $G_t = \mathbb{Q}(\tau > t \mid \mathcal{F}_t)$.

---

## Analogy with Diffusion Models

### Parallels

| Diffusion World | Credit World |
|-----------------|--------------|
| Brownian motion $W_t$ | Default indicator $H_t$ |
| Zero drift under $\mathbb{Q}$ | Compensated $M_t = H_t - A_t$ |
| Girsanov: drift removal | Intensity adjustment |
| Martingale representation | Jump martingale representation |

### Drift Removal Analogy

In diffusion models, Girsanov's theorem removes drift to create martingales:

$$
dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} - \theta_t \, dt
$$

In credit models, the compensator plays an analogous role:

$$
dM_t = dH_t - \lambda_t \, dt
$$

---

## Stochastic Integration with M_t

### Integrating Against the Compensated Martingale

For a predictable process $\phi_t$:

$$
\int_0^t \phi_s \, dM_s = \int_0^t \phi_s \, dH_s - \int_0^t \phi_s \lambda_s \mathbf{1}_{\{\tau > s\}} \, ds
$$

The first integral is $\phi_\tau \mathbf{1}_{\{\tau \le t\}}$ (value at default, if it occurs).

### Martingale Property

If $\phi_t$ is suitably bounded, then $\int_0^t \phi_s dM_s$ is a martingale. This enables:
- Construction of hedging strategies
- Derivation of pricing PDEs
- Characterization of replicating portfolios

---

## Hedging Implications

### Hedgeable vs. Unhedgeable Risk

The martingale $M_t$ represents **default surprise risk**—the unpredictable component of default.

- **Pre-default risk:** The accumulating compensator $A_t$ can potentially be hedged with intensity-sensitive instruments
- **Jump risk:** The jump $\Delta M_\tau$ at default is inherently unhedgeable with continuous instruments

### Incomplete Markets

Credit markets are typically **incomplete**:
- Default jump cannot be perfectly replicated
- Multiple equivalent martingale measures exist
- Prices depend on risk preferences

The compensator framework clarifies exactly what can and cannot be hedged.

---

## Worked Example: Defaultable Zero-Coupon Bond

**Setup:** Zero-coupon bond paying 1 at $T$ with zero recovery.

**Price under intensity model:**

On $\{\tau > t\}$:

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right]
$$

Using the fundamental formula:

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right]
$$

**Special case (deterministic $r$ and $\lambda$):**

$$
P^d(t,T) = e^{-\int_t^T (r(s) + \lambda(s)) ds} = P(t,T) \cdot S(t,T)
$$

The martingale/compensator framework justifies this formula rigorously.

---

## Key Takeaways

- The default indicator $H_t$ has compensator $A_t = \int_0^{t \wedge \tau} \lambda_s ds$
- The compensated process $M_t = H_t - A_t$ is a martingale
- This structure enables arbitrage-free pricing of defaultable claims
- The compensator transforms random default time expectations into tractable integrals
- Intensity acts as an additional "credit discount rate"
- The framework parallels drift removal in diffusion models
- Incomplete markets imply default jump risk cannot be perfectly hedged

---

## Further Reading

- Jeanblanc, M., & Le Cam, Y. (2009). Compensators in credit risk. *Stochastic Processes and Applications*.
- Brémaud, P. (1981). *Point Processes and Queues: Martingale Dynamics*. Springer.
- Elliott, R. J., Aggoun, L., & Moore, J. B. (1995). *Hidden Markov Models*. Springer.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 8.

---

## Exercises

**Exercise 1.** Let $H_t = \mathbf{1}_{\{\tau \le t\}}$ be the default indicator process with constant intensity $\lambda$. Show that $M_t = H_t - \lambda(t \wedge \tau)$ is a $\mathcal{G}_t$-martingale by computing $\mathbb{E}[M_t - M_s \mid \mathcal{G}_s]$ for $s < t$, separately on $\{\tau \le s\}$ and $\{\tau > s\}$.

??? success "Solution to Exercise 1"
    We show that $M_t = H_t - \lambda(t \wedge \tau)$ is a $\mathcal{G}_t$-martingale for constant intensity $\lambda$ by computing $\mathbb{E}[M_t - M_s \mid \mathcal{G}_s]$ for $s < t$.

    We split on the two events $\{\tau \le s\}$ and $\{\tau > s\}$.

    **Case 1: On the event $\{\tau \le s\}$ (default has already occurred by time $s$).**

    For $t > s$, since $\tau \le s < t$:

    - $H_t = 1$ and $H_s = 1$
    - $t \wedge \tau = \tau$ and $s \wedge \tau = \tau$

    Therefore:

    $$
    M_t - M_s = (H_t - \lambda(t \wedge \tau)) - (H_s - \lambda(s \wedge \tau)) = (1 - \lambda\tau) - (1 - \lambda\tau) = 0
    $$

    So $\mathbb{E}[M_t - M_s \mid \mathcal{G}_s] = 0$ on $\{\tau \le s\}$. $\checkmark$

    **Case 2: On the event $\{\tau > s\}$ (no default by time $s$).**

    Here $H_s = 0$ and $s \wedge \tau = s$, so $M_s = 0 - \lambda s = -\lambda s$.

    For $M_t$, we consider two sub-cases:

    - If $\tau > t$: $H_t = 0$, $t \wedge \tau = t$, so $M_t = -\lambda t$
    - If $s < \tau \le t$: $H_t = 1$, $t \wedge \tau = \tau$, so $M_t = 1 - \lambda\tau$

    Therefore:

    $$
    M_t - M_s = \begin{cases} -\lambda t + \lambda s = -\lambda(t-s) & \text{if } \tau > t \\ 1 - \lambda\tau + \lambda s & \text{if } s < \tau \le t \end{cases}
    $$

    Now compute the conditional expectation. Given $\tau > s$, we know that the remaining time to default $\tau - s$ is $\text{Exp}(\lambda)$ (by the memoryless property). Let $\xi = \tau - s \sim \text{Exp}(\lambda)$ on $\{\tau > s\}$.

    $$
    \mathbb{E}[M_t - M_s \mid \mathcal{G}_s, \tau > s] = \mathbb{P}(\tau > t \mid \tau > s)(-\lambda(t-s)) + \int_s^t (1 - \lambda u + \lambda s) \lambda e^{-\lambda(u-s)}\,du
    $$

    The first term: $\mathbb{P}(\tau > t \mid \tau > s) = e^{-\lambda(t-s)}$, contributing $-\lambda(t-s)e^{-\lambda(t-s)}$.

    For the second term, substitute $v = u - s$:

    $$
    \int_0^{t-s} (1 - \lambda v) \lambda e^{-\lambda v}\,dv = \lambda\int_0^{t-s} e^{-\lambda v}\,dv - \lambda^2\int_0^{t-s} v e^{-\lambda v}\,dv
    $$

    Computing each integral (let $\Delta = t - s$):

    $$
    \lambda\int_0^{\Delta} e^{-\lambda v}\,dv = 1 - e^{-\lambda\Delta}
    $$

    $$
    \lambda^2\int_0^{\Delta} v e^{-\lambda v}\,dv = \lambda^2\left[-\frac{v}{\lambda}e^{-\lambda v}\Big|_0^{\Delta} + \frac{1}{\lambda}\int_0^{\Delta} e^{-\lambda v}\,dv\right] = -\lambda\Delta e^{-\lambda\Delta} + (1 - e^{-\lambda\Delta})
    $$

    Combining:

    $$
    (1 - e^{-\lambda\Delta}) - (-\lambda\Delta e^{-\lambda\Delta} + 1 - e^{-\lambda\Delta}) = \lambda\Delta e^{-\lambda\Delta}
    $$

    Adding both terms:

    $$
    \mathbb{E}[M_t - M_s \mid \mathcal{G}_s, \tau > s] = -\lambda\Delta e^{-\lambda\Delta} + \lambda\Delta e^{-\lambda\Delta} = 0
    $$

    Since $\mathbb{E}[M_t - M_s \mid \mathcal{G}_s] = 0$ on both $\{\tau \le s\}$ and $\{\tau > s\}$, we conclude that $M_t$ is a $\mathcal{G}_t$-martingale. $\square$

---

**Exercise 2.** For a stochastic intensity $\lambda_t$, the compensator of $H_t$ is $\Lambda_{t \wedge \tau} = \int_0^{t \wedge \tau} \lambda_s\,ds$. Explain why the compensator stops accumulating after default (i.e., the integral is capped at $\tau$). What would go wrong economically if the compensator continued to grow after default?

??? success "Solution to Exercise 2"
    **Why the compensator stops accumulating after default:**

    The compensator is $A_t = \int_0^{t \wedge \tau} \lambda_s\,ds$, which stops at $\tau$ rather than continuing to accumulate.

    **Mathematical reason:** The compensator is the unique predictable increasing process in the Doob-Meyer decomposition $H_t = M_t + A_t$ where $M_t$ is a martingale. After default ($t > \tau$), the default indicator $H_t = 1$ is constant. For $M_t = H_t - A_t$ to remain a martingale, we need $M_t$ to also be constant for $t > \tau$. If $A_t$ continued to grow after $\tau$, then $M_t = 1 - A_t$ would be strictly decreasing for $t > \tau$, contradicting the martingale property (a decreasing process with nonzero drift cannot be a martingale).

    **Economic reason:** The compensator $A_t$ represents the cumulative "expected default" or "credit risk accrual" up to time $t$. Once default has actually occurred, there is no further credit risk to accrue. The entity has already defaulted -- the event is irreversible and complete. Continuing to accumulate hazard after default would be economically nonsensical: it would mean the model keeps "expecting" additional defaults from an entity that has already defaulted.

    **What would go wrong if the compensator continued growing:** If we defined $\tilde{A}_t = \int_0^t \lambda_s\,ds$ (without the stopping at $\tau$), then:

    $$
    \tilde{M}_t = H_t - \int_0^t \lambda_s\,ds
    $$

    For $t > \tau$: $\tilde{M}_t = 1 - \int_0^t \lambda_s\,ds$, which is strictly decreasing (since $\lambda_s > 0$). This means $\mathbb{E}[\tilde{M}_t \mid \mathcal{G}_s] < \tilde{M}_s$ for $t > s > \tau$, so $\tilde{M}_t$ would be a supermartingale, not a martingale. The Doob-Meyer decomposition would be violated.

    Economically, if hedging strategies were based on such a flawed compensator, post-default hedging positions would generate systematic losses (since the "expected default" keeps accruing but no further default event occurs), leading to arbitrage opportunities.

---

**Exercise 3.** The compensated default process $M_t^H = H_t - \int_0^{t \wedge \tau} \lambda_s\,ds$ is a martingale. Show that $\mathbb{E}[M_t^H] = 0$ for all $t$ and compute $\text{Var}(M_t^H)$ for constant intensity $\lambda$.

??? success "Solution to Exercise 3"
    **Part 1: Show that $\mathbb{E}[M_t^H] = 0$ for all $t$.**

    Since $M_t^H$ is a martingale with $M_0^H = H_0 - \int_0^{0 \wedge \tau} \lambda_s\,ds = 0 - 0 = 0$, the martingale property gives:

    $$
    \mathbb{E}[M_t^H] = \mathbb{E}[\mathbb{E}[M_t^H \mid \mathcal{G}_0]] = M_0^H = 0
    $$

    $\square$

    Alternatively, we can verify directly. Write $M_t^H = H_t - \int_0^{t \wedge \tau} \lambda\,ds$ (for constant $\lambda$):

    $$
    \mathbb{E}[M_t^H] = \mathbb{E}[H_t] - \lambda\,\mathbb{E}[t \wedge \tau]
    $$

    We have $\mathbb{E}[H_t] = \mathbb{Q}(\tau \le t) = 1 - e^{-\lambda t}$ and:

    $$
    \mathbb{E}[t \wedge \tau] = \int_0^t \mathbb{Q}(\tau > s)\,ds = \int_0^t e^{-\lambda s}\,ds = \frac{1 - e^{-\lambda t}}{\lambda}
    $$

    Therefore:

    $$
    \mathbb{E}[M_t^H] = (1 - e^{-\lambda t}) - \lambda \cdot \frac{1 - e^{-\lambda t}}{\lambda} = (1 - e^{-\lambda t}) - (1 - e^{-\lambda t}) = 0 \quad \checkmark
    $$

    **Part 2: Compute $\text{Var}(M_t^H)$ for constant intensity $\lambda$.**

    Since $\mathbb{E}[M_t^H] = 0$, we have $\text{Var}(M_t^H) = \mathbb{E}[(M_t^H)^2]$.

    We compute this by conditioning on whether default has occurred:

    $$
    \mathbb{E}[(M_t^H)^2] = \mathbb{E}[(M_t^H)^2 \mathbf{1}_{\{\tau > t\}}] + \mathbb{E}[(M_t^H)^2 \mathbf{1}_{\{\tau \le t\}}]
    $$

    **On $\{\tau > t\}$:** $H_t = 0$, $t \wedge \tau = t$, so $M_t^H = -\lambda t$.

    $$
    \mathbb{E}[(M_t^H)^2 \mathbf{1}_{\{\tau > t\}}] = \lambda^2 t^2 \cdot e^{-\lambda t}
    $$

    **On $\{\tau \le t\}$:** $H_t = 1$, $t \wedge \tau = \tau$, so $M_t^H = 1 - \lambda\tau$.

    $$
    \mathbb{E}[(M_t^H)^2 \mathbf{1}_{\{\tau \le t\}}] = \int_0^t (1 - \lambda u)^2 \lambda e^{-\lambda u}\,du
    $$

    Expanding $(1 - \lambda u)^2 = 1 - 2\lambda u + \lambda^2 u^2$ and integrating term by term:

    $$
    \int_0^t \lambda e^{-\lambda u}\,du = 1 - e^{-\lambda t}
    $$

    $$
    \int_0^t 2\lambda^2 u\,e^{-\lambda u}\,du = 2\left[1 - e^{-\lambda t}(1 + \lambda t)\right]
    $$

    $$
    \int_0^t \lambda^3 u^2 e^{-\lambda u}\,du = 2 - e^{-\lambda t}(2 + 2\lambda t + \lambda^2 t^2)
    $$

    Combining:

    $$
    (1 - e^{-\lambda t}) - 2(1 - e^{-\lambda t} - \lambda t e^{-\lambda t}) + 2 - e^{-\lambda t}(2 + 2\lambda t + \lambda^2 t^2)
    $$

    $$
    = 1 - e^{-\lambda t} - 2 + 2e^{-\lambda t} + 2\lambda t e^{-\lambda t} + 2 - 2e^{-\lambda t} - 2\lambda t e^{-\lambda t} - \lambda^2 t^2 e^{-\lambda t}
    $$

    $$
    = 1 - e^{-\lambda t} - \lambda^2 t^2 e^{-\lambda t}
    $$

    Adding both contributions:

    $$
    \text{Var}(M_t^H) = \lambda^2 t^2 e^{-\lambda t} + 1 - e^{-\lambda t} - \lambda^2 t^2 e^{-\lambda t} = 1 - e^{-\lambda t}
    $$

    Therefore:

    $$
    \boxed{\text{Var}(M_t^H) = 1 - e^{-\lambda t} = \mathbb{Q}(\tau \le t)}
    $$

    This elegant result shows that the variance of the compensated martingale equals the default probability. As $t \to \infty$, $\text{Var}(M_t^H) \to 1$, reflecting the certainty that default will eventually occur. Note also that $\text{Var}(M_t^H) = \mathbb{E}[H_t] = \mathbb{E}[\langle M^H \rangle_t] = \mathbb{E}[A_t]$, consistent with the general identity for compensated point processes.

---

**Exercise 4.** Prove that the default indicator $H_t$ is a submartingale. Use the Doob-Meyer decomposition to identify its predictable compensator. How does this relate to the hazard rate?

??? success "Solution to Exercise 4"
    **Proving $H_t$ is a submartingale:**

    The default indicator $H_t = \mathbf{1}_{\{\tau \le t\}}$ is a non-decreasing process: $H_s \le H_t$ for $s \le t$ almost surely. This is because once $\tau \le s$ (i.e., $H_s = 1$), we also have $\tau \le t$ (i.e., $H_t = 1$), and if $\tau > s$ (i.e., $H_s = 0$), then $H_t \ge 0 = H_s$.

    To verify the submartingale property, for $s \le t$:

    $$
    \mathbb{E}[H_t \mid \mathcal{G}_s] = \mathbb{E}[\mathbf{1}_{\{\tau \le t\}} \mid \mathcal{G}_s] = \mathbb{Q}(\tau \le t \mid \mathcal{G}_s)
    $$

    Since $\{\tau \le s\} \subset \{\tau \le t\}$, on $\{\tau \le s\}$ we have $\mathbb{Q}(\tau \le t \mid \mathcal{G}_s) = 1 \ge 1 = H_s$.

    On $\{\tau > s\}$, $H_s = 0$ and $\mathbb{Q}(\tau \le t \mid \mathcal{G}_s) \ge 0 = H_s$.

    In both cases, $\mathbb{E}[H_t \mid \mathcal{G}_s] \ge H_s$, confirming $H_t$ is a submartingale. $\square$

    **Doob-Meyer decomposition and the compensator:**

    By the Doob-Meyer decomposition theorem, any right-continuous submartingale $H_t$ of class (D) can be uniquely decomposed as:

    $$
    H_t = M_t + A_t
    $$

    where $M_t$ is a martingale and $A_t$ is a predictable, increasing process with $A_0 = 0$.

    Under the intensity framework, the predictable compensator is:

    $$
    A_t = \int_0^{t \wedge \tau} \lambda_s\,ds
    $$

    **Relation to the hazard rate:** The compensator is precisely the integral of the hazard rate (intensity) stopped at default. The hazard rate $\lambda_t$ is the "rate of accumulation" of the compensator:

    $$
    dA_t = \lambda_t \mathbf{1}_{\{\tau > t\}}\,dt
    $$

    The intensity $\lambda_t$ determines how fast the "expected default" accumulates. Before default, the compensator grows at rate $\lambda_t$; at default, it stops. The connection is that $\lambda_t$ is the unique predictable process such that $H_t - \int_0^{t \wedge \tau} \lambda_s\,ds$ is a martingale. Thus, the hazard rate is operationally defined as the "Radon–Nikodym derivative" of the compensator with respect to Lebesgue measure on $[0, \tau]$.

---

**Exercise 5.** Using the martingale property of $M_t^H$, derive the pricing formula for a defaultable claim that pays 1 at default time $\tau$ if $\tau \le T$:

$$
\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{\tau} r_s\,ds}\,\mathbf{1}_{\{\tau \le T\}}\right] = \mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T e^{-\int_0^u r_s\,ds}\,\lambda_u\,S(0,u)\,du\right]
$$

??? success "Solution to Exercise 5"
    We derive the pricing formula for a claim that pays 1 at default time $\tau$ if $\tau \le T$.

    **Goal:** Show that

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^{\tau} r_s\,ds}\,\mathbf{1}_{\{\tau \le T\}}\right] = \mathbb{E}^{\mathbb{Q}}\left[\int_0^T e^{-\int_0^u r_s\,ds}\,\lambda_u\,S(0,u)\,du\right]
    $$

    **Derivation:** We use the compensator representation. The key identity is that for any predictable process $\phi_t$:

    $$
    \mathbb{E}\left[\phi_\tau \mathbf{1}_{\{\tau \le T\}}\right] = \mathbb{E}\left[\int_0^T \phi_u \lambda_u \mathbf{1}_{\{\tau > u\}}\,du\right]
    $$

    This follows from the fact that $dH_u = dM_u + \lambda_u \mathbf{1}_{\{\tau > u\}}\,du$, so:

    $$
    \mathbb{E}\left[\int_0^T \phi_u\,dH_u\right] = \mathbb{E}\left[\int_0^T \phi_u\,dM_u\right] + \mathbb{E}\left[\int_0^T \phi_u \lambda_u \mathbf{1}_{\{\tau > u\}}\,du\right]
    $$

    The integral $\int_0^T \phi_u\,dM_u$ is a martingale (for suitable $\phi$), so its expectation is zero. Also, $\int_0^T \phi_u\,dH_u = \phi_\tau \mathbf{1}_{\{\tau \le T\}}$ since $H$ jumps only once at $\tau$.

    Therefore:

    $$
    \mathbb{E}\left[\phi_\tau \mathbf{1}_{\{\tau \le T\}}\right] = \mathbb{E}\left[\int_0^T \phi_u \lambda_u \mathbf{1}_{\{\tau > u\}}\,du\right]
    $$

    Setting $\phi_u = e^{-\int_0^u r_s\,ds}$ (which is predictable):

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^{\tau} r_s\,ds}\,\mathbf{1}_{\{\tau \le T\}}\right] = \mathbb{E}^{\mathbb{Q}}\left[\int_0^T e^{-\int_0^u r_s\,ds}\,\lambda_u\,\mathbf{1}_{\{\tau > u\}}\,du\right]
    $$

    Now we use the tower property and the fact that under the Cox construction:

    $$
    \mathbb{E}[\mathbf{1}_{\{\tau > u\}} \mid \mathcal{F}_\infty] = \mathbb{Q}(\tau > u \mid \mathcal{F}_\infty) = e^{-\int_0^u \lambda_s\,ds} = S(0,u)
    $$

    (where $S(0,u)$ denotes the $\mathcal{F}$-conditional survival probability, which equals $e^{-\Lambda_u}$). Taking the expectation over both $\mathcal{F}$ and default:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\int_0^T e^{-\int_0^u r_s\,ds}\,\lambda_u\,\mathbf{1}_{\{\tau > u\}}\,du\right] = \mathbb{E}^{\mathbb{Q}}\left[\int_0^T e^{-\int_0^u r_s\,ds}\,\lambda_u\,e^{-\int_0^u \lambda_s\,ds}\,du\right]
    $$

    $$
    = \mathbb{E}^{\mathbb{Q}}\left[\int_0^T e^{-\int_0^u r_s\,ds}\,\lambda_u\,S(0,u)\,du\right]
    $$

    This completes the derivation. $\square$

    **Interpretation:** The left side is the expected discounted payment at the random default time. The right side converts this into a deterministic integral over all possible default times $u \in [0,T]$, weighted by the intensity $\lambda_u$ (instantaneous default probability) and survival probability $S(0,u)$ (probability of reaching time $u$ without earlier default). This transformation from a random stopping time to a deterministic integral is the key computational advantage of the compensator framework.

---

**Exercise 6.** In a model with two default times $\tau_1$ and $\tau_2$ (e.g., two firms), the joint default indicator is $H_t^{(1,2)} = \mathbf{1}_{\{\tau_1 \le t, \tau_2 \le t\}}$. If defaults are conditionally independent given a common factor $Z$, describe the compensator of $H_t^{(1,2)}$. How does the correlation between default events enter through the common factor?

??? success "Solution to Exercise 6"
    **Setup:** Two firms with default times $\tau_1$ and $\tau_2$, conditionally independent given a common factor $Z$. Each has intensity $\lambda_t^{(i)}$ with $i = 1, 2$.

    The joint default indicator is:

    $$
    H_t^{(1,2)} = \mathbf{1}_{\{\tau_1 \le t, \tau_2 \le t\}} = H_t^{(1)} \cdot H_t^{(2)}
    $$

    **Deriving the compensator of $H_t^{(1,2)}$:**

    Using the product rule for semimartingales:

    $$
    dH_t^{(1,2)} = H_{t-}^{(1)} dH_t^{(2)} + H_{t-}^{(2)} dH_t^{(1)} + d[H^{(1)}, H^{(2)}]_t
    $$

    Since $H^{(1)}$ and $H^{(2)}$ are pure jump processes that each jump at most once, and under conditional independence given $Z$ they almost surely do not jump simultaneously (i.e., $\mathbb{Q}(\tau_1 = \tau_2) = 0$), the covariation term $d[H^{(1)}, H^{(2)}]_t = 0$ a.s.

    Therefore:

    $$
    dH_t^{(1,2)} = H_{t-}^{(1)} dH_t^{(2)} + H_{t-}^{(2)} dH_t^{(1)}
    $$

    Using the Doob-Meyer decomposition $dH_t^{(i)} = dM_t^{(i)} + \lambda_t^{(i)} \mathbf{1}_{\{\tau_i > t\}}\,dt$, the compensator (predictable part) of $H_t^{(1,2)}$ is:

    $$
    A_t^{(1,2)} = \int_0^t H_{s-}^{(1)} \lambda_s^{(2)} \mathbf{1}_{\{\tau_2 > s\}}\,ds + \int_0^t H_{s-}^{(2)} \lambda_s^{(1)} \mathbf{1}_{\{\tau_1 > s\}}\,ds
    $$

    Simplifying using $H_{s-}^{(i)} \mathbf{1}_{\{\tau_j > s\}} = \mathbf{1}_{\{\tau_i \le s\}} \mathbf{1}_{\{\tau_j > s\}}$:

    $$
    A_t^{(1,2)} = \int_0^t \mathbf{1}_{\{\tau_1 \le s < \tau_2\}} \lambda_s^{(2)}\,ds + \int_0^t \mathbf{1}_{\{\tau_2 \le s < \tau_1\}} \lambda_s^{(1)}\,ds
    $$

    **Interpretation:**

    - The first integral accumulates at rate $\lambda_s^{(2)}$ during the period when firm 1 has defaulted but firm 2 has not yet defaulted
    - The second integral accumulates at rate $\lambda_s^{(1)}$ during the period when firm 2 has defaulted but firm 1 has not yet defaulted
    - Before either default, $A_t^{(1,2)} = 0$ (the joint default indicator has not started accumulating)
    - After both defaults, both integrals stop (both indicators are capped)

    **How correlation enters through the common factor:**

    The correlation between $\tau_1$ and $\tau_2$ enters through the common factor $Z$ in the intensities. Although defaults are conditionally independent given $Z$, the shared dependence on $Z$ creates unconditional dependence:

    - When the common factor $Z$ takes high values, both $\lambda_t^{(1)}$ and $\lambda_t^{(2)}$ are elevated, increasing the probability that both defaults occur early
    - When $Z$ takes low values, both intensities are low, and both defaults are delayed
    - This co-movement creates positive default correlation: $\text{Corr}(\mathbf{1}_{\{\tau_1 \le T\}}, \mathbf{1}_{\{\tau_2 \le T\}}) > 0$

    The unconditional joint default probability is:

    $$
    \mathbb{Q}(\tau_1 \le T, \tau_2 \le T) = \mathbb{E}_Z\left[\mathbb{Q}(\tau_1 \le T \mid Z) \cdot \mathbb{Q}(\tau_2 \le T \mid Z)\right]
    $$

    By Jensen's inequality (since $f(x) = x^2$ is convex and taking the symmetric case for illustration):

    $$
    \mathbb{E}[p(Z)^2] \ge (\mathbb{E}[p(Z)])^2
    $$

    This shows the joint default probability exceeds what it would be under independence, confirming positive default correlation induced by the common factor.
