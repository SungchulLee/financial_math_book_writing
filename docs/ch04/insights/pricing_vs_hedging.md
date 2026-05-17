# Pricing vs Hedging

Every derivatives textbook uses the same model to price and hedge, which creates the
illusion that pricing and hedging solve the same problem. They do not. Pricing is an
expectation computed under a probability measure; hedging is a pathwise replication
argument that holds regardless of which measure is in force. Girsanov's theorem makes
this distinction precise.

!!! abstract "Core distinction"
    **Pricing** assigns a value to a contingent claim via an expectation under
    $\mathbb{Q}$. **Hedging** constructs a self-financing portfolio that replicates
    the claim path by path. Measure change affects pricing but leaves hedging
    invariant.

---

## Pricing Is a Valuation Problem

Pricing asks: what is the fair value of a future payoff $X_T$ observed today?
Recall (see [§ Risk-Neutral Valuation Principle](../risk_neutral/risk_neutral_valuation_principle.md)):
under no-arbitrage the answer is $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-\int_0^T r_s\,ds}X_T]$,
depending on the payoff $X_T$, the discount factor, and the $\mathbb{Q}$-dynamics
of the underlying.

The disappearance of the physical drift $\mu$ from the pricing formula follows from the [§ Risk Premium Decomposition](risk_premium_decomposition.md). Two traders who disagree about expected return still agree on the Black--Scholes price.

---

## Hedging Is a Replication Problem

Hedging asks a different question: how can the payoff be reproduced through dynamic
trading? A self-financing portfolio $(\phi_t, \psi_t)$---holding $\phi_t$ shares of
stock and $\psi_t$ units of the bond---satisfies

$$
dV_t = \phi_t\,dS_t + \psi_t\,dB_t
$$

This equation is a statement about paths, not probabilities. The self-financing
condition depends on the asset price trajectories $S_t(\omega)$ and $B_t(\omega)$
and on the stochastic integral, which is defined via the quadratic variation
$\langle S \rangle_t = \sigma^2 S_t^2\,dt$---a path-by-path quantity that does not
change under an equivalent measure change.

A portfolio that replicates a payoff under $\mathbb{P}$ also replicates it under
$\mathbb{Q}$, and vice versa. Hedging is **measure-invariant**.

---

## Why Pricing Uses Q but Hedging Does Not

Pricing is measure-dependent because it is an expectation: different measures assign
different weights to the same paths, producing different expected values. The
risk-neutral measure $\mathbb{Q}$ is the unique choice (in a complete market) under
which discounted asset prices are martingales, ensuring consistency with no-arbitrage.

Hedging is measure-invariant because the self-financing condition and the replication
argument depend only on the paths themselves and their quadratic variation. Neither
quantity changes when probabilities are reweighted.

In practice, hedge ratios such as the Black-Scholes delta $\Delta = \partial V / \partial S$
are derived from the $\mathbb{Q}$-price function but executed in the $\mathbb{P}$-world.
The distinction matters: hedging performance depends on the real-world paths the market
takes, not on the risk-neutral probabilities used to derive the hedge ratios.

!!! warning "Critical implication"
    A hedging strategy derived under $\mathbb{Q}$ can produce non-zero P&L under
    $\mathbb{P}$. Hedging removes model-consistent risk, not realized risk.

---

## Complete vs Incomplete Markets

The relationship between pricing and hedging depends on market completeness.

In **complete markets**, every contingent claim can be replicated. The price equals
the cost of the unique replicating portfolio, and there is no gap between the pricing
and hedging problems. The risk-neutral measure is unique.

In **incomplete markets**, perfect replication is impossible. The risk-neutral measure
is not unique, so prices are not uniquely determined---they lie in an interval
$[\underline{V}, \overline{V}]$ consistent with no-arbitrage. Hedging strategies
minimize but do not eliminate risk, and residual hedging errors accumulate through the
gamma P&L: the mismatch between realized and implied volatility generates a running
profit or loss proportional to the position's gamma (see
[Practitioner Perspective](practitioner_perspective.md) for the full decomposition).

---

## Summary

| Aspect | Pricing | Hedging |
|--------|---------|---------|
| Question | What is the fair value? | How to replicate the payoff? |
| Depends on measure? | Yes ($\mathbb{Q}$) | No (measure-invariant) |
| Key input | Risk-neutral dynamics | Quadratic variation (volatility) |
| Complete market | Unique price | Perfect replication |
| Incomplete market | Price interval | Imperfect replication |

Confusing the two leads to conceptual errors. Pricing is about expectations; hedging
is about paths. Understanding this distinction is essential for interpreting
risk-neutral valuation correctly.

---

## Exercises

**Exercise 1.**
Consider a European call with payoff $X_T = (S_T - K)^+$ in a complete
Black-Scholes market. Write the risk-neutral pricing formula for $V_0$ and explain
why the physical drift $\mu$ does not appear.

??? success "Solution to Exercise 1"
    The risk-neutral pricing formula is

    $$
    V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}(S_T - K)^+\right]
    $$

    Under $\mathbb{Q}$, the stock satisfies $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, so

    $$
    S_T = S_0 \exp\!\left[\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma W_T^{\mathbb{Q}}\right]
    $$

    The physical drift $\mu$ does not appear because Girsanov's theorem absorbs it into the measure change. The Brownian motion transforms as $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ with $\theta = (\mu - r)/\sigma$, shifting the drift from $\mu$ to $r$. Since the pricing formula is an expectation under $\mathbb{Q}$, only $r$ and $\sigma$ enter. The volatility $\sigma$ is unchanged because quadratic variation is invariant under equivalent measure changes. The drift $\mu$ determines how likely different paths are under $\mathbb{P}$, but pricing uses the reweighted probabilities under $\mathbb{Q}$, where the drift is $r$ regardless of $\mu$.

---

**Exercise 2.**
A trader constructs a self-financing portfolio $(\phi_t, \psi_t)$ consisting of
$\phi_t$ shares of stock and $\psi_t$ units of the risk-free bond. Show that the
self-financing condition $dV_t = \phi_t\,dS_t + \psi_t\,dB_t$ holds under both
$\mathbb{P}$ and $\mathbb{Q}$, and explain why this demonstrates that hedging is
measure-invariant.

??? success "Solution to Exercise 2"
    The self-financing condition

    $$
    dV_t = \phi_t\,dS_t + \psi_t\,dB_t
    $$

    is a pathwise statement: changes in portfolio value come solely from changes in asset prices, with no external cash flows. It depends on the asset price paths $S_t(\omega)$ and $B_t(\omega)$ and on the stochastic integral---but not on the probability measure.

    The Ito integral $\int_0^t \phi_s\,dS_s$ is constructed via the quadratic variation $\langle S \rangle_t = \int_0^t \sigma^2 S_s^2\,ds$, which is a path-by-path quantity unchanged under equivalent measure changes. Since the integral depends only on the integrand $\phi_t$ and the paths of $S_t$ (including their quadratic variation), the self-financing condition holds identically under both $\mathbb{P}$ and $\mathbb{Q}$.

    This demonstrates that hedging is measure-invariant: a portfolio that replicates a payoff under $\mathbb{P}$ also replicates it under $\mathbb{Q}$. The measure affects expectations and probabilities but not pathwise trading mechanics. Pricing requires choosing a measure; hedging does not.

---

**Exercise 3.**
In an incomplete market with two Brownian motions but only one traded asset, the
risk-neutral measure is not unique. Explain why the price of a non-traded claim
depends on the choice of $\mathbb{Q}$, while the hedging strategy does not fully
replicate the claim. What is the financial interpretation of the residual risk?

??? success "Solution to Exercise 3"
    With two Brownian motions $W^1, W^2$ and one traded asset $S$, the risk premium equation $\mu - r = \sigma_1\theta_1 + \sigma_2\theta_2$ has one equation and two unknowns. This defines a one-parameter family of valid market prices of risk $(\theta_1, \theta_2)$, hence a family of risk-neutral measures $\{\mathbb{Q}^{\theta}\}$.

    For a claim $\Phi(W_T^2)$ depending on the non-traded factor, different choices of $\theta_2$ produce different risk-neutral dynamics for $W^2$ and hence different prices:

    $$
    V_0^{\theta} = \mathbb{E}^{\mathbb{Q}^{\theta}}\!\left[e^{-rT}\Phi(W_T^2)\right]
    $$

    The hedging strategy using only $S$ involves projecting the claim's dynamics onto the traded asset. This cannot eliminate all risk because the claim depends on the non-traded factor.

    The **residual risk** is the unhedgeable component---the part of the payoff orthogonal to traded asset returns. It represents risk from $W^2$ that cannot be hedged with available instruments. The width of the pricing interval $[\underline{V}, \overline{V}]$ reflects the magnitude of this residual risk: in a complete market it collapses to a point; in an incomplete market it creates genuine pricing ambiguity.

---

**Exercise 4.**
A practitioner argues: "Since hedging does not depend on the measure, I can compute
my hedge ratios under $\mathbb{P}$ instead of $\mathbb{Q}$." Is this correct?
Carefully distinguish between computing the hedge ratio and determining the price.

??? success "Solution to Exercise 4"
    The statement is partially correct but requires careful qualification.

    **Hedge ratio computation.** The Black-Scholes delta $\Delta = \partial V / \partial S$ is a derivative of the option price with respect to the stock price. To compute $\Delta$, one needs the price function $V(S,t)$, which is derived under $\mathbb{Q}$. The delta depends on $r$, $\sigma$, $S$, $K$, and $T$---not on $\mu$. So the delta is the same regardless of whether one "thinks in $\mathbb{P}$" or "$\mathbb{Q}$," because it is a derivative of the $\mathbb{Q}$-price.

    **The subtle point.** While $\Delta$ does not depend on $\mu$, it does depend on $\sigma$. If the practitioner uses historical volatility (estimated under $\mathbb{P}$) instead of implied volatility (from the $\mathbb{Q}$-calibrated model), the delta will differ. Implied and historical volatilities are generally not equal.

    **Price determination.** The price $V$ must be computed under $\mathbb{Q}$. Using $\mathbb{E}^{\mathbb{P}}[e^{-rT}\Phi(S_T)]$ gives the wrong answer because it does not account for risk preferences.

    In summary: the replication argument is measure-invariant, but the price function from which $\Delta$ is derived must come from $\mathbb{Q}$-pricing. The practitioner executes trades in the physical market but must use $\mathbb{Q}$-derived hedge ratios.

---

**Exercise 5.**
Prove that if two risk-neutral measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ both
existed in a complete market, they would assign the same price to every contingent
claim, and conclude $\mathbb{Q}_1 = \mathbb{Q}_2$.

??? success "Solution to Exercise 5"
    In a complete market, every contingent claim $\Phi(S_T)$ can be replicated by a self-financing strategy with unique initial cost $V_0$. By no-arbitrage, the price of the claim must equal $V_0$.

    Suppose two equivalent martingale measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ exist. Under each, the price is

    $$
    V_0^{(j)} = \mathbb{E}^{\mathbb{Q}_j}\!\left[e^{-rT}\Phi(S_T)\right], \quad j = 1, 2
    $$

    By the martingale property under $\mathbb{Q}_j$, the initial portfolio value equals the $\mathbb{Q}_j$-expected discounted payoff. Since the replicating portfolio is unique, $V_0^{(1)} = V_0 = V_0^{(2)}$ for every claim.

    Since $\mathbb{Q}_1$ and $\mathbb{Q}_2$ assign the same expected value to $e^{-rT}\Phi(S_T)$ for every bounded measurable $\Phi$, they agree on the distribution of $S_T$ for every $T$. More generally, completeness ensures this holds for all $\mathcal{F}_T$-measurable random variables, so $\mathbb{Q}_1 = \mathbb{Q}_2$ on every $\mathcal{F}_T$.

    This is the Second Fundamental Theorem of Asset Pricing: completeness is equivalent to uniqueness of the equivalent martingale measure. $\square$

---

**Exercise 6.**
A market has a risk-free bond with rate $r$, a traded stock $S_t$, and a non-traded
asset $Y_t$ correlated with $S_t$. Explain the difference between the pricing
interval $[\underline{V}, \overline{V}]$ for a claim on $Y_T$ and the unique price
that would exist if $Y_t$ were traded. How does the interval width depend on the
correlation $\rho$ between $Y_t$ and $S_t$?

??? success "Solution to Exercise 6"
    When $Y_t$ is non-traded, the market is incomplete. The risk premium on the non-traded Brownian motion driving $Y_t$ is a free parameter, leading to a family of risk-neutral measures. The pricing interval is

    $$
    \underline{V} = \inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\Phi(Y_T)\right], \qquad \overline{V} = \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\Phi(Y_T)\right]
    $$

    If $Y_t$ were traded, the additional no-arbitrage constraint would pin down the free parameter, collapsing the interval to a unique price.

    The interval width depends on the correlation $\rho$:

    - **$|\rho| = 1$:** $Y_t$ is perfectly correlated with $S_t$ and can be perfectly hedged. The interval collapses to a point.
    - **$|\rho| = 0$:** $Y_t$ is independent of $S_t$ and completely unhedgeable. The interval is widest because the risk-neutral distribution of $Y_T$ is unconstrained by the traded asset.
    - **Intermediate $|\rho|$:** The width decreases as $|\rho|$ increases, because higher correlation means more of $Y_t$'s risk can be hedged with $S_t$, leaving less residual ambiguity.
