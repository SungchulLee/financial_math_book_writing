# Incomplete Market and Measure Choice

In the Black-Scholes model, there is exactly one source of randomness (Brownian motion) and one traded asset (the stock), yielding a **complete market** with a unique risk-neutral measure. The Merton jump-diffusion model introduces a second source of randomness---the compound Poisson jump process---that cannot be replicated by continuous trading in the stock and bond alone. This makes the market **incomplete**: multiple equivalent martingale measures exist, and the arbitrage-free price of a derivative is no longer unique but lies within an interval. Selecting a specific pricing measure requires additional economic or mathematical criteria.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Explain why jump risk makes the Merton model incomplete
    2. Characterize the set of equivalent martingale measures for jump-diffusion
    3. Describe the Esscher transform and minimal entropy measure as selection criteria
    4. Understand Merton's original diversification argument and its limitations

---

## Why the Market Is Incomplete

### Source Counting

A market is complete when every contingent claim can be replicated by dynamic trading. The number of independent risk sources must equal the number of available hedging instruments.

| Model | Risk sources | Traded assets | Complete? |
|-------|-------------|---------------|-----------|
| Black-Scholes | 1 ($W_t$) | 1 (stock) | Yes |
| Merton jump-diffusion | 2 ($W_t$, $N_t$) | 1 (stock) | No |
| Heston stochastic volatility | 2 ($W_t^{(1)}$, $W_t^{(2)}$) | 1 (stock) | No |
| Bates (Heston + jumps) | 3 ($W_t^{(1)}$, $W_t^{(2)}$, $N_t$) | 1 (stock) | No |

With one stock and a risk-free bond, we can hedge the diffusion risk through delta hedging, but the jump risk remains unhedgeable.

### The Hedging Gap

Consider a delta-hedged portfolio $\Pi_t = V_t - \Delta_t S_t$ where $V_t$ is an option value and $\Delta_t = \partial V/\partial S$ is the Black-Scholes delta. Between jumps, $d\Pi_t \approx r\Pi_t\,dt$ (the hedge works). At a jump time, however:

$$
\Delta\Pi = V(S_{t^-}Y) - V(S_{t^-}) - \Delta_t S_{t^-}(Y - 1)
$$

This **hedging error** is nonzero whenever $V$ is not linear in $S$ (which is the case for any convex payoff like a call or put). The error depends on the random jump size $Y$, and no choice of $\Delta_t$ can eliminate it for all possible realizations of $Y$.

!!! warning "Jump Risk Cannot Be Diversified Away"
    Merton's original argument (1976) was that jump risk is idiosyncratic and can be diversified in a large portfolio. This justifies using the physical jump intensity $\lambda^{\mathbb{P}}$ as the risk-neutral intensity $\lambda^{\mathbb{Q}}$. However, market crashes and systemic events produce correlated jumps across assets, undermining the diversification argument. Modern practice treats jump parameters under $\mathbb{Q}$ as free parameters to be calibrated to option prices.

---

## The Set of Equivalent Martingale Measures

### Characterization

An equivalent martingale measure (EMM) $\mathbb{Q}$ for the Merton model must satisfy:

1. $\mathbb{Q} \sim \mathbb{P}$ (equivalent: same null sets)
2. The discounted price $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale

The change of measure from $\mathbb{P}$ to $\mathbb{Q}$ can modify:

- The **drift of Brownian motion** via Girsanov's theorem: $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ for some market price of diffusion risk $\theta$
- The **jump intensity**: $\lambda^{\mathbb{Q}} \neq \lambda^{\mathbb{P}}$
- The **jump size distribution**: $\nu^{\mathbb{Q}} \neq \nu^{\mathbb{P}}$

The diffusion risk premium $\theta$ is pinned down by the no-arbitrage condition (ensuring the correct drift), but the jump parameters $(\lambda^{\mathbb{Q}}, \nu^{\mathbb{Q}})$ have a **one-parameter family** of solutions for each additional constraint.

### The Radon-Nikodym Derivative

The general Radon-Nikodym derivative for changing jump intensity and jump size distribution is:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\!\left[-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T + (\lambda^{\mathbb{P}} - \lambda^{\mathbb{Q}})T + \sum_{i=1}^{N_T}\ln\frac{\lambda^{\mathbb{Q}}f^{\mathbb{Q}}(Y_i)}{\lambda^{\mathbb{P}}f^{\mathbb{P}}(Y_i)}\right]
$$

where $f^{\mathbb{P}}$ and $f^{\mathbb{Q}}$ are the jump size densities under the respective measures.

!!! info "Proposition: No-Arbitrage Constraint"
    Any EMM $\mathbb{Q}$ must satisfy

    $$
    r = \mu^{\mathbb{P}} - \sigma\theta + \lambda^{\mathbb{Q}}\bar{k}^{\mathbb{Q}} - \lambda^{\mathbb{P}}\bar{k}^{\mathbb{P}}
    $$

    where $\bar{k}^{\mathbb{Q}} = \mathbb{E}^{\mathbb{Q}}[Y - 1]$. This single equation constrains the parameters $(\theta, \lambda^{\mathbb{Q}}, \nu^{\mathbb{Q}})$, but since there are more unknowns than equations, infinitely many solutions exist.

---

## Measure Selection Criteria

### Merton's Original Approach

Merton assumed that jump risk is diversifiable, implying:

$$
\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}}, \qquad f^{\mathbb{Q}} = f^{\mathbb{P}}
$$

Under this assumption, the jump parameters are the same under $\mathbb{P}$ and $\mathbb{Q}$, and only the diffusion drift changes. This gives the unique pricing measure of the Merton series formula. While economically motivated, the assumption fails for systematic (market-wide) jump risk.

### The Esscher Transform

The Esscher transform tilts the probability distribution exponentially:

!!! info "Definition: Esscher Transform"
    For a parameter $h \in \mathbb{R}$, the Esscher measure $\mathbb{Q}^h$ is defined by

    $$
    \frac{d\mathbb{Q}^h}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \frac{e^{hX_T}}{\mathbb{E}^{\mathbb{P}}[e^{hX_T}]}
    $$

    where $X_T = \ln(S_T/S_0)$.

Under the Esscher transform:

- The jump intensity changes to $\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}} \cdot \mathbb{E}^{\mathbb{P}}[e^{h\ln Y}] = \lambda^{\mathbb{P}} e^{h\mu_J + h^2\sigma_J^2/2}$
- The jump size density shifts: $\mu_J^{\mathbb{Q}} = \mu_J + h\sigma_J^2$

The parameter $h$ is chosen so that $e^{-rt}S_t$ is a $\mathbb{Q}^h$-martingale, which gives a single equation for $h$.

**Advantages:** The Esscher transform preserves the distributional family (log-normal jumps remain log-normal under $\mathbb{Q}^h$) and has deep connections to exponential utility maximization.

### Minimal Entropy Measure

The minimal entropy martingale measure (MEMM) $\mathbb{Q}^*$ minimizes the relative entropy (Kullback-Leibler divergence) from $\mathbb{P}$:

$$
\mathbb{Q}^* = \arg\min_{\mathbb{Q} \in \mathcal{Q}} H(\mathbb{Q} \| \mathbb{P}) = \arg\min_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}\!\left[\ln\frac{d\mathbb{Q}}{d\mathbb{P}}\right]
$$

where $\mathcal{Q}$ is the set of all EMMs.

**Interpretation:** Among all risk-neutral measures, the MEMM is "closest" to the physical measure in an information-theoretic sense. It perturbs the real-world probabilities as little as possible while still being an EMM.

For the Merton model with log-normal jumps, the MEMM coincides with the Esscher transform for a specific value of $h$.

### Minimal Martingale Measure

The minimal martingale measure $\mathbb{Q}^{\text{min}}$ adjusts only the drift of the continuous part, leaving the jump characteristics unchanged under the change of measure:

$$
\lambda^{\mathbb{Q}^{\text{min}}} = \lambda^{\mathbb{P}}, \qquad \nu^{\mathbb{Q}^{\text{min}}} = \nu^{\mathbb{P}}
$$

This is equivalent to Merton's original assumption. It preserves the orthogonal (jump) risk and is particularly natural when the jump component is modeled as purely idiosyncratic.

---

## Pricing Bounds

### The No-Arbitrage Interval

Since multiple EMMs exist, the arbitrage-free price of a derivative $H$ lies in the interval:

$$
\underline{\pi}(H) = \inf_{\mathbb{Q} \in \mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[e^{-rT}H] \leq \pi(H) \leq \sup_{\mathbb{Q} \in \mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[e^{-rT}H] = \overline{\pi}(H)
$$

!!! info "Proposition: Width of the Pricing Interval"
    The width $\overline{\pi}(H) - \underline{\pi}(H)$ is:

    - Zero for claims that depend only on the diffusion component (linear payoffs in $S_T$)
    - Increasing in the jump sensitivity of $H$ (convex payoffs have wider bounds)
    - Increasing in $\lambda$ (more frequent jumps widen the bounds)

For vanilla European options, the practical width of the pricing interval is typically small because calibration to liquid option prices effectively selects a measure. The interval becomes wider for exotic options with strong jump sensitivity (e.g., deep OTM puts, barrier options near the barrier).

---

## Calibration as Implicit Measure Selection

### The Practitioner's Approach

In practice, the measure choice problem is resolved by **calibrating** the jump-diffusion parameters to observed option prices:

1. Take the Merton series formula with parameters $(\sigma, \lambda, \mu_J, \sigma_J)$ under $\mathbb{Q}$
2. Minimize the distance between model prices and market prices across strikes and maturities
3. The calibrated parameters implicitly define a specific EMM

This approach treats the $\mathbb{Q}$-parameters as free and makes no assumption about the physical measure $\mathbb{P}$. The calibrated $\lambda^{\mathbb{Q}}$ and $(\mu_J^{\mathbb{Q}}, \sigma_J^{\mathbb{Q}})$ generally differ from their physical counterparts, reflecting the **market price of jump risk**.

!!! example "Implied Jump Risk Premium"
    If the physical jump intensity is $\lambda^{\mathbb{P}} = 0.5$ (one jump every two years on average) but calibration to S&P 500 options yields $\lambda^{\mathbb{Q}} = 1.5$, the market prices jump risk as if jumps are three times more frequent than they actually are. This reflects investors' aversion to crash risk.

---

## Summary

The Merton jump-diffusion model is incomplete because the compound Poisson jump process introduces unhedgeable risk. Multiple equivalent martingale measures exist, each corresponding to different assumptions about the market price of jump risk. Selection criteria include the Esscher transform (exponential tilting with connections to utility theory), the minimal entropy measure (closest to $\mathbb{P}$ in Kullback-Leibler divergence), and the minimal martingale measure (Merton's original diversification argument). In practice, calibration to observed option prices implicitly selects a pricing measure, with the calibrated jump parameters under $\mathbb{Q}$ reflecting investors' compensation for bearing jump risk.
