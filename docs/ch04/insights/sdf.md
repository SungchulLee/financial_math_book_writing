# The Stochastic Discount Factor

Risk-neutral pricing tells us *how* to compute prices: take discounted expectations under $\mathbb{Q}$. But it does not explain *why* such a measure exists or what economic forces create it. The stochastic discount factor (SDF) answers this deeper question by connecting investor preferences to the mathematical measure change.

!!! info "Prerequisites"
    This section assumes familiarity with:

    - [Risk-Neutral Valuation Principle](../risk_neutral/risk_neutral_valuation_principle.md)
    - [Market Price of Risk](../risk_neutral/market_price_of_risk.md)
    - [Girsanov's Theorem](../girsanov/girsanov_theorem.md)

!!! note "Scope"
    The SDF is not required for computing derivative prices---the risk-neutral
    formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T]$ is self-contained for
    that purpose. This section provides the economic foundations behind
    risk-neutral pricing for readers seeking deeper understanding.

---

## The Core Idea

Not all future dollars are valued equally. A dollar received during a recession is worth more than a dollar received during a boom, because investors have higher marginal utility when wealth is scarce. The SDF $M_T$ encodes this asymmetry by assigning an economic weight to each state of the world.

The most general pricing formula in finance is:

$$
\text{Price} = \mathbb{E}^{\mathbb{P}}[M_T \cdot X_T]
$$

where $X_T$ is the payoff and $M_T$ is the stochastic discount factor. This says: start with real-world probabilities ($\mathbb{P}$), then reweight each outcome by its economic value ($M_T$).

In economic theory, the SDF arises from marginal utility:

$$
M_T = e^{-rT} \frac{u'(C_T)}{u'(C_0)}
$$

When consumption $C_T$ is low (bad times), marginal utility $u'(C_T)$ is high, so $M_T$ is high. When consumption is high (good times), $M_T$ is low. The SDF weights outcomes by how much investors *care* about them.

---

## Equivalence with Risk-Neutral Pricing

If pricing works both as $\mathbb{E}^{\mathbb{P}}[M_T X_T]$ and as $\mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T]$, there must be an object connecting them. Rewrite the risk-neutral formula under $\mathbb{P}$:

$$
\text{Price} = \mathbb{E}^{\mathbb{Q}}[e^{-rT} X_T]
= \int e^{-rT} X_T \, d\mathbb{Q}
= \int e^{-rT} X_T \frac{d\mathbb{Q}}{d\mathbb{P}} \, d\mathbb{P}
$$

Define:

$$
M_T := e^{-rT} \frac{d\mathbb{Q}}{d\mathbb{P}}
$$

Then:

$$
\text{Price} = \int M_T X_T \, d\mathbb{P} = \mathbb{E}^{\mathbb{P}}[M_T X_T]
$$

The SDF factors into deterministic time-value discounting ($e^{-rT}$) and stochastic probability reweighting ($d\mathbb{Q}/d\mathbb{P}$). Crucially, $M_T$ does not depend on the payoff $X_T$---it is a universal pricing kernel.

Conversely, given an SDF $M_T > 0$, the risk-neutral measure is recovered by normalizing:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \frac{M_T}{\mathbb{E}^{\mathbb{P}}[M_T]}
$$

Pricing a risk-free bond ($X_T = 1$, price $= e^{-rT}$) confirms $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT}$, consistent with the definition. The transformation from $\mathbb{P}$ to $\mathbb{Q}$ upweights bad states and downweights good states---exactly what risk-averse investors do. The risk-neutral measure $\mathbb{Q}$ is not a belief; it is a preference-adjusted probability.

---

## Risk Premium Through the SDF

The SDF explains why risky assets earn excess returns. For an asset with price $P_0$ today and payoff $P_T$ at time $T$, the gross return is $R_T = P_T / P_0$. From $P_0 = \mathbb{E}^{\mathbb{P}}[M_T P_T]$, dividing by $P_0$ gives:

$$
\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1
$$

Expanding via $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] + \operatorname{Cov}(X,Y)$ and using $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT} = 1/R_f$ where $R_f = e^{rT}$:

$$
\mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \operatorname{Cov}^{\mathbb{P}}(M_T, R_T)
$$

This says:

- Negative covariance with $M_T$ (pays well in good states, poorly in bad) implies a positive risk premium.
- Positive covariance with $M_T$ (pays well in bad states) implies a negative risk premium---the asset is insurance.
- Zero covariance with $M_T$ implies the asset earns exactly the risk-free rate.

This is the economic origin of risk premia.

---

## Summary

The two views of pricing are equivalent:

| View | Formula | Interpretation |
|---|---|---|
| Economic | $\text{Price} = \mathbb{E}^{\mathbb{P}}[M_T X_T]$ | Real-world probabilities, explicit preferences |
| Mathematical | $\text{Price} = \mathbb{E}^{\mathbb{Q}}[e^{-rT} X_T]$ | Adjusted probabilities, preferences hidden in $\mathbb{Q}$ |

The SDF explains *why* pricing works; the risk-neutral measure explains *how* to compute it. Markets do not price outcomes by how likely they are---they price them by how much they matter.

---

## Exercises

**Exercise 1.**
Let $M_T = e^{-rT} \frac{u'(C_T)}{u'(C_0)}$ with $u(C) = \ln C$. Compute $M_T$ explicitly when $C_T = C_0 e^{(\mu_C - \sigma_C^2/2)T + \sigma_C W_T}$ under $\mathbb{P}$. Show that $M_T$ is a decreasing function of $C_T$.

??? success "Solution to Exercise 1"
    With $u(C) = \ln C$, we have $u'(C) = 1/C$, so:

    $$
    M_T = e^{-rT} \frac{C_0}{C_T} = e^{-rT} \exp\!\left(-(\mu_C - \sigma_C^2/2)T - \sigma_C W_T\right)
    $$

    Since $C_T = C_0 e^{(\mu_C - \sigma_C^2/2)T + \sigma_C W_T}$ is strictly increasing in $W_T$, and $M_T = e^{-rT} C_0 / C_T$ is strictly decreasing in $C_T$, we see that $M_T$ is indeed a decreasing function of consumption. High consumption (good states) gives low $M_T$; low consumption (bad states) gives high $M_T$.

---

**Exercise 2.**
Starting from the SDF pricing formula $\text{Price} = \mathbb{E}^{\mathbb{P}}[M_T X_T]$ and the definition $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = M_T / \mathbb{E}^{\mathbb{P}}[M_T]$, derive the risk-neutral pricing formula $\text{Price} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[X_T]$. State what assumption on $M_T$ is needed.

??? success "Solution to Exercise 2"
    By definition of $\mathbb{Q}$:

    $$
    \mathbb{E}^{\mathbb{P}}[M_T X_T] = \mathbb{E}^{\mathbb{P}}\!\left[\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} \cdot \mathbb{E}^{\mathbb{P}}[M_T] \cdot X_T\right] = \mathbb{E}^{\mathbb{P}}[M_T] \cdot \mathbb{E}^{\mathbb{Q}}[X_T]
    $$

    For a risk-free bond paying 1 at time $T$, the price is $e^{-rT}$, so $\mathbb{E}^{\mathbb{P}}[M_T \cdot 1] = e^{-rT}$, giving $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT}$. Substituting:

    $$
    \mathbb{E}^{\mathbb{P}}[M_T X_T] = e^{-rT} \mathbb{E}^{\mathbb{Q}}[X_T]
    $$

    The key assumption is that $M_T > 0$ a.s. and $\mathbb{E}^{\mathbb{P}}[M_T] < \infty$, so that $\mathbb{Q}$ is a well-defined equivalent probability measure.

---

**Exercise 3.**
Starting from $\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1$, derive $\mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \operatorname{Cov}^{\mathbb{P}}(M_T, R_T)$. Then consider a stock with $\operatorname{Cov}^{\mathbb{P}}(M_T, R_{\text{stock}}) < 0$ and an insurance contract with $\operatorname{Cov}^{\mathbb{P}}(M_T, R_{\text{ins}}) > 0$. Which has the higher expected return, and why?

??? success "Solution to Exercise 3"
    From $\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1$, expand using the covariance identity:

    $$
    \mathbb{E}^{\mathbb{P}}[M_T]\,\mathbb{E}^{\mathbb{P}}[R_T] + \operatorname{Cov}^{\mathbb{P}}(M_T, R_T) = 1
    $$

    Since $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT} = 1/R_f$:

    $$
    \frac{\mathbb{E}^{\mathbb{P}}[R_T]}{R_f} + \operatorname{Cov}^{\mathbb{P}}(M_T, R_T) = 1
    $$

    Rearranging:

    $$
    \mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \operatorname{Cov}^{\mathbb{P}}(M_T, R_T)
    $$

    The **stock** has negative covariance with $M_T$---it pays well in good states (low $M_T$) and poorly in bad states (high $M_T$). The formula gives a positive risk premium: $\mathbb{E}[R_{\text{stock}}] > R_f$. Investors demand compensation for holding an asset that fails when wealth is most needed.

    The **insurance contract** has positive covariance with $M_T$---it pays well in bad states. The formula gives a negative risk premium: $\mathbb{E}[R_{\text{ins}}] < R_f$. Investors accept below-market returns because the payoff arrives when marginal utility is high. The stock has the higher expected return.

---

**Exercise 4.**
An asset pays only in market crashes. Empirically, its expected return is below the risk-free rate. Without using CAPM, beta, or any specific model, explain why investors willingly accept below-market returns using only the SDF framework.

??? success "Solution to Exercise 4"
    In bad states (crashes), marginal utility is high, so the SDF $M_T$ is high. An asset that pays only in these states has positive covariance with $M_T$---its payoffs are concentrated in states where investors value wealth most. Investors willingly pay a premium (accept lower returns) because the asset delivers wealth exactly when it is most needed.

    The SDF weights these crash-state payoffs heavily, making the asset's price high relative to its expected payoff. A high price today means a low expected return. This is why insurance-like assets earn below the risk-free rate: they are not bad investments---they are expensive because they hedge the states investors fear most.

---

**Exercise 5.**
In one sentence, explain what the stochastic discount factor does. Then state the two components it factors into and interpret each.

??? success "Solution to Exercise 5"
    The SDF converts a payoff in any future state into its present value by encoding both the time value of money and the investor's relative preference for wealth in that state.

    It factors as $M_T = e^{-rT} \cdot (d\mathbb{Q}/d\mathbb{P})$:

    - $e^{-rT}$: deterministic discounting for the time value of money.
    - $d\mathbb{Q}/d\mathbb{P}$: stochastic reweighting that inflates the probability of bad states and deflates the probability of good states, reflecting risk aversion.

    Together, they transform the real-world expectation of a payoff into its market price.
