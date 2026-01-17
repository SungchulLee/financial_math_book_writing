# Compensators and Martingales

The martingale structure of default processes is formalized using **compensators**. This perspective is essential for rigorous pricing in reduced-form credit models, providing the mathematical foundation for arbitrage-free valuation and hedging of defaultable claims.

---

## The Default Indicator Process

### Definition

The **default indicator** (or default process) is:

$$
H_t := \mathbf{1}_{\{\tau \le t\}},
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
\mathbb{E}[H_T \mid \mathcal{G}_t] \ge H_t \quad \text{for } T \ge t.
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
A_t = \int_0^{t \wedge \tau} \lambda_s \, ds,
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
\mathbb{E}[dH_t \mid \mathcal{G}_{t-}] = \lambda_t \, dt = dA_t.
$$

---

## Martingale Representation

### Differential Form

In differential notation:

$$
dM_t = dH_t - \lambda_t \mathbf{1}_{\{\tau > t\}} \, dt.
$$

Since $dH_t = \mathbf{1}_{\{\tau \in dt\}}$ (the jump indicator), this reads:

$$
dM_t = dH_t - \lambda_t \mathbf{1}_{\{\tau \ge t\}} \, dt.
$$

### Jump Martingale

The martingale $M_t$ is a **purely discontinuous** (jump) martingale:
- It is constant between jumps
- It has a single jump of size $1 - \int_0^{\tau} \lambda_s ds$ at time $\tau$
- No continuous martingale component

### Quadratic Variation

The predictable quadratic variation is:

$$
\langle M \rangle_t = A_t = \int_0^{t \wedge \tau} \lambda_s \, ds.
$$

The actual quadratic variation is:

$$
[M]_t = H_t = \mathbf{1}_{\{\tau \le t\}}.
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
\mathbb{E}^{\mathbb{Q}}[X \mid \mathcal{G}_t] = \mathbb{E}^{\mathbb{Q}}[X \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{G}_t] + \mathbb{E}^{\mathbb{Q}}[X \cdot \mathbf{1}_{\{\tau \le T\}} \mid \mathcal{G}_t].
$$

The compensator structure allows explicit computation of each term.

### Pre-Default Pricing Formula

On $\{\tau > t\}$, for a payoff $Y(\tau)$ at default:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} Y(\tau) \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u r_s ds} Y(u) \lambda_u S(t,u) \, du \mid \mathcal{F}_t\right],
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
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} C(T) \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} R(\tau) \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right].
$$

Using the compensator representation:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} C(T) \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s) ds} R(u) \lambda_u \, du \mid \mathcal{F}_t\right].
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
dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} - \theta_t \, dt.
$$

In credit models, the compensator plays an analogous role:

$$
dM_t = dH_t - \lambda_t \, dt.
$$

---

## Stochastic Integration with $M_t$

### Integrating Against the Compensated Martingale

For a predictable process $\phi_t$:

$$
\int_0^t \phi_s \, dM_s = \int_0^t \phi_s \, dH_s - \int_0^t \phi_s \lambda_s \mathbf{1}_{\{\tau > s\}} \, ds.
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
P^d(t,T) = e^{-\int_t^T (r(s) + \lambda(s)) ds} = P(t,T) \cdot S(t,T).
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
