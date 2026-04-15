# Pricing vs Hedging


Although pricing and hedging are closely related, they represent **distinct
economic problems**. Measure change clarifies the difference between them.

!!! abstract "Key distinction"
    Pricing is an expectation over probability distributions.
    Hedging is a statement about pathwise replication.
    Measure change affects pricing but not hedging.

!!! note "Common confusion"
    Pricing and hedging use the same model inputs, which creates the illusion
    that they solve the same problem. They do not: pricing assigns value,
    hedging controls pathwise risk.

---

## Pricing: A Valuation Problem


Pricing asks the question:

> *What is the fair value of a contingent claim today?*

Under no-arbitrage, the price of a payoff $X_T$ at time $T$ is given by

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[ e^{-\int_0^T r_s ds} X_T \right]
$$

where $\mathbb{Q}$ is a risk-neutral measure.

Pricing depends only on:

- the payoff structure,
- the risk-free rate,
- the risk-neutral dynamics.

---

## Hedging: A Replication Problem


Hedging asks a different question:

> *How can the payoff be replicated or risk-managed through trading?*

Hedging strategies are constructed in the **physical market**, using observable
asset prices and trading rules. They depend on:

- market completeness,
- available instruments,
- trading constraints.

---

## Why Pricing Uses ℚ


Pricing is measure-dependent because it is a valuation exercise.
The risk-neutral measure incorporates risk preferences implicitly through the
change of measure.

Hedging, however, is **measure-invariant**:

- A self-financing strategy remains self-financing under any equivalent measure.
- Replication arguments do not depend on $\mathbb{P}$ or $\mathbb{Q}$.

In practice, hedge ratios are computed from $\mathbb{Q}$-calibrated models but
evaluated under $\mathbb{P}$-realized dynamics. This means hedging performance
depends on the real-world paths the market takes, not on the risk-neutral
probabilities used to derive the hedge ratios.

!!! warning "Critical implication"
    A hedging strategy derived under $\mathbb{Q}$ can produce non-zero P&L
    under $\mathbb{P}$. Hedging removes model-consistent risk, not realized
    risk.

---

## Complete vs Incomplete Markets


- In **complete markets**, pricing and hedging coincide:
  the price is the cost of the unique replicating strategy.
- In **incomplete markets**, pricing is not unique, and hedging is imperfect.
  Hedging errors accumulate through the gamma P&L: the mismatch between
  realized and implied volatility generates a running profit or loss
  proportional to the position's gamma (see
  [Practitioner Perspective](practitioner_perspective.md) for the full
  decomposition).

This distinction will reappear in later chapters on model risk and robust pricing.

---

## Summary


- Pricing is a valuation problem → use $\mathbb{Q}$.
- Hedging is a trading problem → measure-independent.
- Confusing the two leads to conceptual errors.

Understanding this distinction is essential for interpreting risk-neutral pricing
correctly.

---

## Exercises

**Exercise 1.**
Consider a European call option with payoff $X_T = (S_T - K)^+$ in a complete market. Write the risk-neutral pricing formula for $V_0$ and explain why the formula does not involve the physical drift $\mu$ of the underlying asset.

??? success "Solution to Exercise 1"
    The risk-neutral pricing formula for the European call is

    $$
    V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}(S_T - K)^+\right]
    $$

    Under $\mathbb{Q}$, the stock dynamics are $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. The distribution of $S_T$ under $\mathbb{Q}$ is lognormal with parameters determined by $r$ and $\sigma$:

    $$
    S_T = S_0 \exp\!\left[\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma W_T^{\mathbb{Q}}\right]
    $$

    The physical drift $\mu$ does not appear because Girsanov's theorem absorbs it into the measure change. Specifically, the Brownian motion $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ with $\theta = (\mu - r)/\sigma$ shifts the drift from $\mu$ to $r$. Since the pricing formula is an expectation under $\mathbb{Q}$, only the risk-neutral drift $r$ and the volatility $\sigma$ (which is invariant under measure change) enter the calculation. The physical drift $\mu$ determines how likely different paths are under $\mathbb{P}$, but pricing uses the reweighted probabilities under $\mathbb{Q}$, where the drift is always $r$ regardless of $\mu$.

---

**Exercise 2.**
A trader constructs a self-financing replicating portfolio $(\phi_t, \psi_t)$ consisting of $\phi_t$ shares of stock and $\psi_t$ units of the risk-free bond. Show that the self-financing condition

$$
dV_t = \phi_t\,dS_t + \psi_t\,dB_t
$$

holds under both $\mathbb{P}$ and $\mathbb{Q}$. Explain why this demonstrates that hedging is measure-invariant.

??? success "Solution to Exercise 2"
    The self-financing condition states that changes in portfolio value come solely from changes in asset prices, with no external cash flows:

    $$
    dV_t = \phi_t\,dS_t + \psi_t\,dB_t
    $$

    This condition is a **pathwise** statement about the portfolio dynamics. It depends on the asset price paths $S_t(\omega)$ and $B_t(\omega)$, the holdings $\phi_t(\omega)$ and $\psi_t(\omega)$, and the stochastic integration theory---but it does not depend on the probability measure used to weight paths.

    Formally, the Ito integral $\int_0^t \phi_s\,dS_s$ is defined pathwise via the quadratic variation of $S$. The quadratic variation $\langle S \rangle_t = \int_0^t \sigma^2 S_s^2\,ds$ is a path-by-path quantity that does not change under an equivalent measure change. Since the stochastic integral depends only on the integrand $\phi_t$ and the paths of $S_t$ (including their quadratic variation), the self-financing condition holds identically under both $\mathbb{P}$ and $\mathbb{Q}$.

    This demonstrates that hedging is measure-invariant: a portfolio that replicates a payoff under $\mathbb{P}$ also replicates it under $\mathbb{Q}$, and vice versa. The measure affects expectations and probabilities, but not the pathwise trading mechanics. Pricing requires choosing a measure (to compute the expectation), but hedging does not.

---

**Exercise 3.**
In an incomplete market with two Brownian motions but only one traded asset, the risk-neutral measure is not unique. Explain why the price of a non-traded contingent claim depends on the choice of $\mathbb{Q}$, while the hedging strategy using only the traded asset does not fully replicate the claim. What is the financial interpretation of the residual risk?

??? success "Solution to Exercise 3"
    In an incomplete market with two Brownian motions $W^1, W^2$ but only one traded asset $S$, the risk premium equation $\mu - r = \sigma_1\theta_1 + \sigma_2\theta_2$ has one equation and two unknowns. This defines a one-parameter family of valid market price of risk vectors $(\theta_1, \theta_2)$, and hence a family of risk-neutral measures $\{\mathbb{Q}^{\theta}\}$.

    For a contingent claim $\Phi(W_T^2)$ that depends on the non-traded Brownian motion, different choices of $\theta_2$ produce different risk-neutral dynamics for $W^2$ and hence different prices:

    $$
    V_0^{\theta} = \mathbb{E}^{\mathbb{Q}^{\theta}}\!\left[e^{-rT}\Phi(W_T^2)\right]
    $$

    The hedging strategy using only the traded asset $S$ involves choosing $\phi_t$ to minimize risk, typically by projecting the claim's dynamics onto the traded asset. The optimal hedge ratio depends on the correlation structure and does not eliminate all risk.

    The **residual risk** is the unhedgeable component---the part of the claim's payoff that is orthogonal to the traded asset's returns. Financially, this represents the risk from the non-traded factor $W^2$ that cannot be diversified or hedged away using available instruments. The width of the pricing interval $[\underline{V}, \overline{V}]$ reflects the magnitude of this residual risk: in a complete market the interval collapses to a single point, while in an incomplete market the residual risk creates genuine pricing ambiguity.

---

**Exercise 4.**
Consider a market where a stock follows geometric Brownian motion under $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

A derivative has payoff $\Phi(S_T)$. A practitioner argues: "Since hedging does not depend on the measure, I can compute my hedge ratios under $\mathbb{P}$ instead of $\mathbb{Q}$." Is this correct? Carefully distinguish between computing the hedge ratio and determining the derivative price.

??? success "Solution to Exercise 4"
    The practitioner's statement is partially correct but requires careful qualification.

    **Hedge ratio computation:** The Black-Scholes delta is $\Delta = \partial V / \partial S$, which is a derivative of the option price with respect to the stock price. To compute $\Delta$, one needs the option price function $V(S, t)$, which is derived under $\mathbb{Q}$. The delta itself depends on $r$, $\sigma$, $S$, $K$, and $T$---not on $\mu$. So the delta is the same regardless of whether one "thinks in $\mathbb{P}$" or "$\mathbb{Q}$," because it is a derivative of the $\mathbb{Q}$-price.

    **The subtle point:** While the hedge ratio $\Delta$ does not depend on $\mu$, it does depend on the volatility $\sigma$. If the practitioner uses $\sigma$ estimated from historical data under $\mathbb{P}$ (statistical volatility) instead of the implied volatility from the $\mathbb{Q}$-calibrated model, the delta will differ. This is important because implied and historical volatilities are generally different.

    **Price determination:** The derivative price $V$ must be computed under $\mathbb{Q}$, not $\mathbb{P}$. Using $\mathbb{P}$-dynamics to compute the price (e.g., via $\mathbb{E}^{\mathbb{P}}[e^{-rT}\Phi(S_T)]$) would give the wrong answer because this expectation does not account for risk preferences correctly.

    In summary: the replication argument is measure-invariant, but the price function from which $\Delta$ is derived must come from $\mathbb{Q}$-pricing. The practitioner can hedge under $\mathbb{P}$ (execute trades in the physical market) but must use the $\mathbb{Q}$-derived hedge ratio.

---

**Exercise 5.**
In a complete market, the price of a contingent claim equals the cost of its unique replicating portfolio. Prove that if two different risk-neutral measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ both existed in a complete market, they would assign the same price to every contingent claim, and conclude that $\mathbb{Q}_1 = \mathbb{Q}_2$.

??? success "Solution to Exercise 5"
    In a complete market, every contingent claim $\Phi(S_T)$ can be replicated by a self-financing trading strategy. Let $V_0$ denote the initial cost of the unique replicating portfolio. By the law of one price (no arbitrage), the price of the claim must equal $V_0$.

    Now suppose two equivalent martingale measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ exist. Under each, the price of $\Phi(S_T)$ is given by

    $$
    V_0^{(j)} = \mathbb{E}^{\mathbb{Q}_j}\!\left[e^{-rT}\Phi(S_T)\right], \quad j = 1, 2
    $$

    Since the market is complete, the claim is replicated by a unique self-financing portfolio with initial cost $V_0$. By the martingale property under $\mathbb{Q}_j$, the initial value of this portfolio equals the $\mathbb{Q}_j$-expected discounted payoff. Therefore $V_0^{(1)} = V_0 = V_0^{(2)}$ for every contingent claim.

    Since $\mathbb{Q}_1$ and $\mathbb{Q}_2$ assign the same expected value to $e^{-rT}\Phi(S_T)$ for every bounded measurable function $\Phi$, they must agree on the distribution of $S_T$ for every $T$. More generally, since this holds for all $\mathcal{F}_T$-measurable random variables (by completeness), we conclude $\mathbb{Q}_1 = \mathbb{Q}_2$ on every $\mathcal{F}_T$, hence $\mathbb{Q}_1 = \mathbb{Q}_2$.

    This is the content of the Second Fundamental Theorem of Asset Pricing: completeness is equivalent to uniqueness of the equivalent martingale measure.

---

**Exercise 6.**
A market has two assets: a risk-free bond with rate $r$ and a stock $S_t$. A new non-traded asset $Y_t$ is introduced, correlated with $S_t$ but not directly hedgeable. Explain the difference between the pricing interval $[\underline{V}, \overline{V}]$ for a claim on $Y_T$ and the unique price that would exist if $Y_t$ were traded. How does the width of the pricing interval relate to the correlation between $Y_t$ and $S_t$?

??? success "Solution to Exercise 6"
    When $Y_t$ is non-traded but correlated with the traded asset $S_t$, the market is incomplete. The risk premium on the non-traded Brownian motion driving $Y_t$ (independently of $S_t$) is a free parameter, leading to a family of risk-neutral measures.

    The **pricing interval** $[\underline{V}, \overline{V}]$ for a claim on $Y_T$ is the range of prices consistent with no-arbitrage:

    $$
    \underline{V} = \inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\Phi(Y_T)\right], \qquad \overline{V} = \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\Phi(Y_T)\right]
    $$

    where the optimization is over all valid risk-neutral measures. If $Y_t$ were traded, the additional no-arbitrage constraint would pin down the free parameter, collapsing the interval to a single **unique price**.

    The width of the pricing interval is related to the **correlation** $\rho$ between $Y_t$ and $S_t$:

    - If $|\rho| = 1$: $Y_t$ is perfectly correlated with $S_t$ and can be perfectly hedged using $S_t$. The pricing interval collapses to a point.
    - If $|\rho| = 0$: $Y_t$ is independent of $S_t$ and completely unhedgeable. The pricing interval is widest because the risk-neutral distribution of $Y_T$ is entirely unconstrained by the traded asset.
    - For intermediate $|\rho|$: The interval width decreases as $|\rho|$ increases, because higher correlation means more of $Y_t$'s risk can be hedged with $S_t$, leaving less residual ambiguity.

---

**Exercise 7.**
A practitioner computes the Black-Scholes delta $\Delta = \partial V / \partial S$ for hedging but uses historical (physical measure) volatility $\sigma_{\mathbb{P}}$ instead of implied volatility $\sigma_{\mathrm{imp}}$. Explain the conceptual error and describe the financial consequences in terms of the gamma P&L decomposition.

??? success "Solution to Exercise 7"
    The conceptual error is that the practitioner is mixing measures. The Black-Scholes delta $\Delta = \partial V / \partial S$ is computed from the option price $V$, which is a function of implied volatility $\sigma_{\mathrm{imp}}$ (a $\mathbb{Q}$-measure quantity). Using historical volatility $\sigma_{\mathbb{P}}$ instead means computing the delta from a different price function, leading to an incorrect hedge ratio.

    The financial consequences can be understood through the gamma P&L decomposition. Over a hedging interval, the P&L of a delta-hedged position is approximately

    $$
    \text{P&L} \approx \frac{1}{2}\Gamma\,S^2\left(\sigma_{\mathrm{realized}}^2 - \sigma_{\mathrm{model}}^2\right)\Delta t
    $$

    When the practitioner uses $\sigma_{\mathbb{P}}$ for hedging, there are two distinct sources of error:

    1. **Delta mismatch:** The delta computed with $\sigma_{\mathbb{P}}$ differs from the delta computed with $\sigma_{\mathrm{imp}}$. This creates a systematic hedging error proportional to $(\Delta_{\sigma_{\mathbb{P}}} - \Delta_{\sigma_{\mathrm{imp}}}) \cdot dS$.

    2. **Gamma P&L bias:** The gamma and the option value are computed inconsistently. The hedge is based on a model (with $\sigma_{\mathbb{P}}$) that does not match the price at which the option was bought or sold (which reflects $\sigma_{\mathrm{imp}}$). The residual P&L will not average to zero even if realized volatility equals implied volatility, because the hedge ratios are wrong.

    In practice, the correct approach is to compute delta using $\sigma_{\mathrm{imp}}$ (matching the pricing measure) and then assess whether realized volatility will differ from implied volatility to form a view on the expected gamma P&L.
