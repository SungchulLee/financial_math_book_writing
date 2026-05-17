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

Recall (see [Extensions of Black-Scholes](../extensions_black_scholes/limitations_extensions.md)): a market is complete when every contingent claim can be replicated by dynamic trading; the number of independent risk sources must equal the number of available hedging instruments.

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

- The **drift of Brownian motion** via Girsanov's theorem (see [Girsanov](../../ch04/girsanov/girsanov_intuition.md)): $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$
- The **jump intensity**: $\lambda^{\mathbb{Q}} \neq \lambda^{\mathbb{P}}$
- The **jump size distribution**: $\nu^{\mathbb{Q}} \neq \nu^{\mathbb{P}}$

The diffusion risk premium $\theta$ is pinned down by the no-arbitrage condition (ensuring the correct drift), but the jump parameters $(\lambda^{\mathbb{Q}}, \nu^{\mathbb{Q}})$ have a **one-parameter family** of solutions for each additional constraint.

### The Radon–Nikodym Derivative

The general Radon–Nikodym derivative for changing jump intensity and jump size distribution is:

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

---

## Exercises

**Exercise 1.** In the Black-Scholes model with one Brownian motion and one stock, explain why the market is complete by counting risk sources and hedging instruments. Then explain why adding a compound Poisson process $N_t$ (independent of $W_t$) breaks completeness, even though the stock price $S_t$ still trades continuously between jumps.

??? success "Solution to Exercise 1"
    In the Black-Scholes model, the only source of randomness is the Brownian motion $W_t$. The stock provides one hedging instrument (in addition to the bond). With one risk source and one hedging instrument, we can form a portfolio $\Pi_t = V_t - \Delta_t S_t$ and choose $\Delta_t = \partial V/\partial S$ to eliminate all randomness. The resulting portfolio earns the risk-free rate: $d\Pi_t = r\Pi_t\,dt$. Since every contingent claim can be perfectly replicated, the market is complete, and the risk-neutral measure $\mathbb{Q}$ is unique (by the second fundamental theorem of asset pricing).

    Adding a compound Poisson process $N_t$ (independent of $W_t$) introduces a second source of randomness. The stock still provides only one hedging instrument. Delta hedging eliminates the diffusion risk ($dW_t$ component), but at each jump time the hedge fails: the portfolio experiences a random P&L of $V(S_{t^-}Y) - V(S_{t^-}) - \Delta_t S_{t^-}(Y-1)$, which depends on the random jump size $Y$ and cannot be zeroed by any choice of $\Delta_t$. Since we have two risk sources (diffusion and jumps) but only one tradeable asset, we cannot span all contingent claims. The market is incomplete, and multiple equivalent martingale measures exist.

---


**Exercise 2.** For a delta-hedged portfolio $\Pi_t = V_t - \Delta_t S_t$ with $\Delta_t = \partial V/\partial S$, compute the hedging error at a jump time when $S$ jumps from $S_{t^-}$ to $S_{t^-}Y$. Show that for a European call with convex payoff, the hedging error $\Delta\Pi = V(S_{t^-}Y) - V(S_{t^-}) - \Delta_t S_{t^-}(Y-1)$ is strictly positive for large jumps (both up and down), and explain why this means jump risk cannot be hedged by any choice of $\Delta_t$.

??? success "Solution to Exercise 2"
    At a jump time, $S$ changes from $S_{t^-}$ to $S_{t^-}Y$, so the stock position changes by $\Delta_t(S_{t^-}Y - S_{t^-}) = \Delta_t S_{t^-}(Y-1)$, while the option changes by $V(S_{t^-}Y) - V(S_{t^-})$. The hedging error is:

    $$
    \Delta\Pi = V(S_{t^-}Y) - V(S_{t^-}) - \Delta_t S_{t^-}(Y-1)
    $$

    For a European call, $V(S)$ is convex: $V''(S) = \Gamma > 0$. By Taylor expansion around $S_{t^-}$:

    $$
    V(S_{t^-}Y) \approx V(S_{t^-}) + V'(S_{t^-}) S_{t^-}(Y-1) + \frac{1}{2}V''(S_{t^-}) S_{t^-}^2(Y-1)^2
    $$

    With $\Delta_t = V'(S_{t^-})$:

    $$
    \Delta\Pi \approx \frac{1}{2}\Gamma S_{t^-}^2(Y-1)^2 > 0
    $$

    This is strictly positive for any $Y \neq 1$, whether the jump is up ($Y > 1$) or down ($Y < 1$). The convexity of $V$ means the hedging error is always non-negative (to leading order), and it is strictly positive for any nonzero jump. No choice of $\Delta_t$ can eliminate this error because the error is a nonlinear function of the random variable $Y$: the delta hedge matches only the linear term $V'(S)(Y-1)$, leaving the convexity residual unhedged.

---


**Exercise 3.** The no-arbitrage constraint for an EMM $\mathbb{Q}$ is $r = \mu^{\mathbb{P}} - \sigma\theta + \lambda^{\mathbb{Q}}\bar{k}^{\mathbb{Q}} - \lambda^{\mathbb{P}}\bar{k}^{\mathbb{P}}$. Verify that this is a single equation in the unknowns $(\theta, \lambda^{\mathbb{Q}}, \mu_J^{\mathbb{Q}}, \sigma_J^{\mathbb{Q}})$, and explain why infinitely many solutions exist. For the special case where $\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}}$ and $\sigma_J^{\mathbb{Q}} = \sigma_J^{\mathbb{P}}$, solve for $\mu_J^{\mathbb{Q}}$ in terms of the other parameters.

??? success "Solution to Exercise 3"
    The no-arbitrage constraint is:

    $$
    r = \mu^{\mathbb{P}} - \sigma\theta + \lambda^{\mathbb{Q}}\bar{k}^{\mathbb{Q}} - \lambda^{\mathbb{P}}\bar{k}^{\mathbb{P}}
    $$

    where $\bar{k}^{\mathbb{Q}} = e^{\mu_J^{\mathbb{Q}} + (\sigma_J^{\mathbb{Q}})^2/2} - 1$. The unknowns are $\theta$ (market price of diffusion risk), $\lambda^{\mathbb{Q}}$ (risk-neutral jump intensity), $\mu_J^{\mathbb{Q}}$ (risk-neutral mean log-jump), and $\sigma_J^{\mathbb{Q}}$ (risk-neutral jump dispersion). This is one equation in four unknowns, so there are three free degrees of freedom, yielding infinitely many solutions.

    For the special case $\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}} \equiv \lambda$ and $\sigma_J^{\mathbb{Q}} = \sigma_J^{\mathbb{P}} \equiv \sigma_J$, the constraint becomes:

    $$
    r = \mu^{\mathbb{P}} - \sigma\theta + \lambda(e^{\mu_J^{\mathbb{Q}} + \sigma_J^2/2} - 1) - \lambda(e^{\mu_J^{\mathbb{P}} + \sigma_J^2/2} - 1)
    $$

    $$
    r = \mu^{\mathbb{P}} - \sigma\theta + \lambda e^{\sigma_J^2/2}(e^{\mu_J^{\mathbb{Q}}} - e^{\mu_J^{\mathbb{P}}})
    $$

    Solving for $\mu_J^{\mathbb{Q}}$:

    $$
    e^{\mu_J^{\mathbb{Q}}} = e^{\mu_J^{\mathbb{P}}} + \frac{r - \mu^{\mathbb{P}} + \sigma\theta}{\lambda e^{\sigma_J^2/2}}
    $$

    $$
    \mu_J^{\mathbb{Q}} = \ln\!\left(e^{\mu_J^{\mathbb{P}}} + \frac{r - \mu^{\mathbb{P}} + \sigma\theta}{\lambda e^{\sigma_J^2/2}}\right)
    $$

    Note that $\theta$ (the market price of diffusion risk) is still free, so even in this restricted case, there is a one-parameter family of solutions.

---


**Exercise 4.** Under the Esscher transform with parameter $h$, the jump intensity changes to $\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}} e^{h\mu_J + h^2\sigma_J^2/2}$ and the mean log-jump shifts to $\mu_J^{\mathbb{Q}} = \mu_J + h\sigma_J^2$. Suppose $\lambda^{\mathbb{P}} = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$. For $h = 1$, compute $\lambda^{\mathbb{Q}}$ and $\mu_J^{\mathbb{Q}}$. Interpret the sign of the shift in $\mu_J$: does the Esscher transform make downward jumps more or less severe?

??? success "Solution to Exercise 4"
    With $\lambda^{\mathbb{P}} = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$, and $h = 1$:

    $$
    \lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}} e^{h\mu_J + h^2\sigma_J^2/2} = 0.5 \cdot e^{1 \cdot (-0.10) + 1 \cdot 0.09/2} = 0.5 \cdot e^{-0.10 + 0.045} = 0.5 \cdot e^{-0.055} \approx 0.5 \times 0.9465 = 0.4733
    $$

    $$
    \mu_J^{\mathbb{Q}} = \mu_J + h\sigma_J^2 = -0.10 + 1 \times 0.09 = -0.01
    $$

    **Interpretation:** The Esscher transform with $h = 1$ shifts $\mu_J$ from $-0.10$ to $-0.01$, making downward jumps **less severe** under $\mathbb{Q}$. The positive shift $h\sigma_J^2 = 0.09$ moves the mean log-jump closer to zero, reducing the expected loss per jump. Simultaneously, the jump intensity decreases slightly from 0.5 to 0.4733. For $h > 0$, the Esscher transform tilts the distribution toward higher values of $S_T$ (since $e^{hX_T}$ upweights paths with large $X_T$), which reduces the severity of downward jumps. To increase the severity of downward jumps (as observed in market calibration), one would need $h < 0$.

---


**Exercise 5.** The minimal entropy martingale measure minimizes $H(\mathbb{Q} \| \mathbb{P}) = \mathbb{E}^{\mathbb{Q}}[\ln(d\mathbb{Q}/d\mathbb{P})]$ over all EMMs. Explain intuitively why this criterion chooses the measure that is "closest" to the physical measure. In what sense is a low-entropy measure more conservative than one with high entropy? Contrast this with the minimal martingale measure, which fixes jump parameters at their physical values.

??? success "Solution to Exercise 5"
    The minimal entropy martingale measure minimizes the Kullback-Leibler divergence $H(\mathbb{Q} \| \mathbb{P}) = \mathbb{E}^{\mathbb{Q}}[\ln(d\mathbb{Q}/d\mathbb{P})]$ over all EMMs $\mathbb{Q} \in \mathcal{Q}$.

    **Intuitive interpretation:** The KL divergence measures the "information cost" of replacing the physical measure $\mathbb{P}$ with the pricing measure $\mathbb{Q}$. Minimizing it selects the $\mathbb{Q}$ that distorts the real-world probabilities as little as possible while still satisfying the martingale condition. This is conservative in the sense that it does not introduce large risk premia beyond what is minimally required by no-arbitrage.

    **Low-entropy vs. high-entropy measures:** A low-entropy $\mathbb{Q}$ stays close to $\mathbb{P}$, meaning the Radon–Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ is close to 1 across most scenarios. This implies moderate risk premia and prices that are close to actuarial (physical) expectations. A high-entropy $\mathbb{Q}$ assigns probabilities very different from $\mathbb{P}$, which can produce extreme risk premia (e.g., greatly inflating crash probabilities).

    **Contrast with the minimal martingale measure:** The minimal martingale measure fixes $\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}}$ and $\nu^{\mathbb{Q}} = \nu^{\mathbb{P}}$, adjusting only the diffusion drift. This does not distort jump probabilities at all, which is appropriate when jump risk is truly idiosyncratic. The MEMM, by contrast, may adjust both diffusion and jump parameters, but it does so in a way that minimizes overall distortion. For the Merton model with log-normal jumps, the MEMM coincides with the Esscher transform for a particular $h$, providing a principled balance between no distortion (minimal martingale) and arbitrary distortion.

---


**Exercise 6.** Consider the no-arbitrage pricing interval $[\underline{\pi}(H),\, \overline{\pi}(H)]$ for a deep out-of-the-money put option with strike $K = 0.7 S_0$. The text states that this interval widens with increasing jump sensitivity. Explain why OTM puts are more sensitive to jump risk than ATM calls, and why the interval width increases with $\lambda$ (jump intensity) and $\sigma_J$ (jump size dispersion).

??? success "Solution to Exercise 6"
    OTM puts with strike $K = 0.7 S_0$ pay off only when the stock drops by at least 30%. Under Black-Scholes (continuous paths), such a move over a short horizon is extremely unlikely. Under the Merton model, a single large downward jump ($Y = 0.7$ or less) can trigger the payoff immediately. The OTM put payoff is therefore highly sensitive to the jump component:

    - The probability $\mathbb{P}(S_T \leq 0.7 S_0)$ depends strongly on $\lambda$ and the left tail of the jump size distribution ($\mu_J$ and $\sigma_J$)
    - Different EMMs assign very different probabilities to this tail event, creating a wide spread in prices

    For ATM calls, the payoff region ($S_T > K$) is reached even without jumps (by diffusion alone), so the option value is less sensitive to the specific choice of jump parameters.

    The interval width increases with $\lambda$ because higher jump intensity means more jump events, amplifying the impact of different measures' treatment of jump risk. With more jumps, the cumulative effect of different $\mathbb{Q}$-specifications of $(\mu_J^{\mathbb{Q}}, \sigma_J^{\mathbb{Q}})$ becomes larger.

    The width increases with $\sigma_J$ because larger jump dispersion makes the tail probabilities more sensitive to distributional assumptions. When $\sigma_J$ is large, even small changes in $\mu_J^{\mathbb{Q}}$ produce large changes in the probability of extreme events, widening the range of no-arbitrage prices.

---


**Exercise 7.** A practitioner calibrates the Merton model to S&P 500 option prices and finds $\lambda^{\mathbb{Q}} = 1.5$ while the historical estimate is $\lambda^{\mathbb{P}} = 0.5$. The calibrated mean log-jump is $\mu_J^{\mathbb{Q}} = -0.15$ versus the historical $\mu_J^{\mathbb{P}} = -0.08$. Interpret these differences as a **jump risk premium**: the market prices crashes as both more frequent and more severe than historical data suggests. Compute the ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ and discuss what this implies about investors' attitude toward tail risk.

??? success "Solution to Exercise 7"
    The ratio of risk-neutral to physical jump intensity is:

    $$
    \frac{\lambda^{\mathbb{Q}}}{\lambda^{\mathbb{P}}} = \frac{1.5}{0.5} = 3.0
    $$

    The market prices jump risk as if crashes occur three times more frequently than historical data suggests. The mean log-jump shift is $\mu_J^{\mathbb{Q}} - \mu_J^{\mathbb{P}} = -0.15 - (-0.08) = -0.07$, meaning the market also prices each crash as 7 percentage points more severe than history.

    **Interpretation as jump risk premium:** Investors are averse to crash risk (sudden large losses) and demand compensation for bearing it. This compensation manifests as inflated risk-neutral crash parameters: under $\mathbb{Q}$, crashes appear both more frequent ($\lambda^{\mathbb{Q}} > \lambda^{\mathbb{P}}$) and more damaging ($\mu_J^{\mathbb{Q}} < \mu_J^{\mathbb{P}}$). The ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}} = 3$ is consistent with the well-documented "crash risk premium" in equity option markets, where implied volatilities (especially for OTM puts) far exceed realized volatility.

    This implies investors have strong aversion to tail risk (large negative returns), which goes beyond standard mean-variance preferences. The jump risk premium is analogous to the equity risk premium but concentrated in the tail: investors are willing to pay a significant premium (via expensive put options) to insure against rare but severe market crashes. The magnitude of the premium ($3\times$ frequency, nearly $2\times$ severity) suggests that jump risk is not diversifiable in aggregate (it is systematic), contrary to Merton's original assumption.
