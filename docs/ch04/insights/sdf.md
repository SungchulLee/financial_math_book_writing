# What the Stochastic Discount Factor Really Means

In the [unifying framework](../martingale/unifying_principle.md) of this chapter, the stochastic discount factor provides the **economic foundation** for the measure change from $\mathbb{P}$ to $\mathbb{Q}$ — it explains *why* the risk-neutral measure exists, not just how to compute with it.

!!! info "Prerequisites"
    This section assumes familiarity with:

    - [Risk-Neutral Valuation Principle](../finance/risk_neutral_valuation_principle.md)
    - [Market Price of Risk](../risk_neutral/market_price_of_risk.md)
    - [Girsanov's Theorem](../girsanov/girsanov_theorem.md)

---

## Why We Need the SDF

So far, we have introduced two ways of pricing:

* Under the physical measure $\mathbb{P}$ using a stochastic discount factor (SDF)
* Under the risk-neutral measure $\mathbb{Q}$ using discounted expectations

These are mathematically equivalent. But this raises a deeper question:

> What is the *economic meaning* behind this equivalence?

The answer is the **stochastic discount factor**.

---

## The Core Idea

The SDF tells us:

> How much one unit of payoff in a given state of the world is worth *today*.

Not all outcomes are valued equally.

* Payoffs in **bad states** (recessions, crashes) are more valuable
* Payoffs in **good states** (booms) are less valuable

The SDF encodes this asymmetry.

---

## Pricing with the SDF

The most general pricing formula in finance is:

$$
\text{Price} = \mathbb{E}^{\mathbb{P}}[M_T \cdot X_T]
$$

where:

* $X_T$ is the payoff
* $M_T$ is the stochastic discount factor

This formula says:

* Start with real-world probabilities ($\mathbb{P}$)
* Reweight outcomes by their economic value ($M_T$)

---

## Connection to Economics

In economic theory, the SDF is derived from **marginal utility**:

$$
M_T = e^{-rT} \frac{u'(C_T)}{u'(C_0)}
$$

where:

* $u'(C_T)$ is marginal utility of consumption at time $T$

This gives a powerful interpretation:

* When consumption is low (bad times), $u'(C_T)$ is high → $M_T$ is high
* When consumption is high (good times), $u'(C_T)$ is low → $M_T$ is low

So:

> The SDF weights outcomes by how much investors *care* about them.

---

## From Risk-Neutral Pricing to the SDF

If pricing works both as $\mathbb{E}^{\mathbb{P}}[M_T X_T]$ and $\mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T]$, there must be an object connecting them. Start from the risk-neutral pricing formula and rewrite it under $\mathbb{P}$:

$$
\text{Price} = \mathbb{E}^{\mathbb{Q}}[e^{-rT} X_T]
= \int e^{-rT} X_T \, d\mathbb{Q}
= \int e^{-rT} X_T \frac{d\mathbb{Q}}{d\mathbb{P}} \, d\mathbb{P}
$$

The integrand reveals the connecting object. Define:

$$
M_T := e^{-rT} \frac{d\mathbb{Q}}{d\mathbb{P}}
$$

Then:

$$
\text{Price} = \int M_T X_T \, d\mathbb{P} = \mathbb{E}^{\mathbb{P}}[M_T X_T]
$$

> **SDF = discounting $\times$ change of measure.**

The SDF factors into deterministic time-value discounting ($e^{-rT}$) and stochastic probability reweighting ($d\mathbb{Q}/d\mathbb{P}$). Crucially, $M_T$ does not depend on the payoff $X_T$ — it is a **universal** pricing kernel.

Conversely, given an SDF $M_T > 0$, the risk-neutral measure is recovered by normalizing:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \frac{M_T}{\mathbb{E}^{\mathbb{P}}[M_T]}
$$

Pricing a risk-free bond ($X_T = 1$, price $= e^{-rT}$) confirms $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT}$, consistent with the definition.

---

## Intuition: Reweighting the World

The transformation from $\mathbb{P}$ to $\mathbb{Q}$ does one thing:

* It **upweights bad states**
* It **downweights good states**

This is exactly what risk-averse investors do.

So we can interpret:

> $\mathbb{Q}$ is not a belief — it is a *preference-adjusted probability*.

---

## Risk Premium Through the SDF

The SDF explains why risky assets earn excess returns.

For an asset with price $P_0$ today and payoff $P_T$ at time $T$, the **gross return** is $R_T = P_T / P_0$. It tells you how many dollars you end up with per dollar invested. From the pricing formula $P_0 = \mathbb{E}^{\mathbb{P}}[M_T P_T]$, dividing both sides by $P_0$ gives the fundamental relation:

$$
\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1
$$

Expanding via $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] + \text{Cov}(X,Y)$ and using $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT} = 1/R_f$ where $R_f = e^{rT}$ is the gross risk-free return:

$$
\mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \text{Cov}^{\mathbb{P}}(M_T, R_T)
$$

This says:

* Negative covariance with $M_T$ (pays well in good states, poorly in bad) → positive risk premium
* Positive covariance with $M_T$ (pays well in bad states) → negative risk premium (insurance)
* Zero covariance with $M_T$ → earns exactly the risk-free rate

This is the economic origin of the **risk premium**.

---

## The Big Picture

We now have two equivalent views of pricing:

### Economic View

$$
\text{Price} = \mathbb{E}^{\mathbb{P}}[M_T X_T]
$$

* Uses real-world probabilities
* Explicitly models preferences

### Mathematical View

$$
\text{Price} = \mathbb{E}^{\mathbb{Q}}[e^{-rT} X_T]
$$

* Uses adjusted probabilities
* Hides preferences inside $\mathbb{Q}$

---

## Guiding Insight

> The stochastic discount factor is the economic object.
> The risk-neutral measure is a mathematical convenience.

Understanding this distinction is essential:

* The SDF explains *why* pricing works
* The risk-neutral measure explains *how* to compute it

---

!!! abstract "Key takeaway"
    The SDF encodes risk preferences, values payoffs differently across states, and transforms real-world probabilities into pricing probabilities. Markets do not price outcomes by how likely they are — they price them by how much they matter.

---

## Exercises

**Exercise 1.**
Let $M_T = e^{-rT} \frac{u'(C_T)}{u'(C_0)}$ with $u(C) = \ln C$. Compute $M_T$ explicitly when $C_T = C_0 e^{(\mu_C - \sigma_C^2/2)T + \sigma_C W_T}$ under $\mathbb{P}$. Show that $M_T$ is a decreasing function of $C_T$.

??? success "Solution to Exercise 1"
    With $u(C) = \ln C$, we have $u'(C) = 1/C$, so:

    $$
    M_T = e^{-rT} \frac{C_0}{C_T} = e^{-rT} \exp\!\left(-(\mu_C - \sigma_C^2/2)T - \sigma_C W_T\right)
    $$

    Since $C_T = C_0 e^{(\mu_C - \sigma_C^2/2)T + \sigma_C W_T}$ is strictly increasing in $W_T$, and $M_T = e^{-rT} C_0 / C_T$ is strictly decreasing in $C_T$, we see that $M_T$ is indeed a decreasing function of consumption. High consumption (good states) → low $M_T$; low consumption (bad states) → high $M_T$.

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
The fundamental pricing relation states $\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1$ for any gross return $R_T$. Show that $\mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \text{Cov}^{\mathbb{P}}(M_T, R_T)$, where $R_f = e^{rT}$ is the gross risk-free return. Interpret this as a risk premium formula.

??? success "Solution to Exercise 3"
    From $\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1$, expand using the covariance identity:

    $$
    \mathbb{E}^{\mathbb{P}}[M_T]\,\mathbb{E}^{\mathbb{P}}[R_T] + \text{Cov}^{\mathbb{P}}(M_T, R_T) = 1
    $$

    Since $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT} = 1/R_f$:

    $$
    \frac{\mathbb{E}^{\mathbb{P}}[R_T]}{R_f} + \text{Cov}^{\mathbb{P}}(M_T, R_T) = 1
    $$

    Rearranging:

    $$
    \mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \text{Cov}^{\mathbb{P}}(M_T, R_T)
    $$

    **Interpretation:** The risk premium (excess expected return) is proportional to the negative covariance with the SDF. Assets that pay well in bad states (positive covariance with $M_T$) have negative risk premia — they are insurance and command a premium price. Assets that pay poorly in bad states (negative covariance with $M_T$) must offer positive risk premia to attract investors.

---

**Exercise 4.**
Consider a stock with $\text{Cov}^{\mathbb{P}}(M_T, S_T) < 0$ and a bond with $\text{Cov}^{\mathbb{P}}(M_T, B_T) = 0$. Explain which asset has the higher expected return and why. Then describe an asset with $\text{Cov}^{\mathbb{P}}(M_T, X_T) > 0$ and explain why its expected return is below the risk-free rate.

??? success "Solution to Exercise 4"
    From the risk premium formula $\mathbb{E}^{\mathbb{P}}[R] - R_f = -R_f \cdot \text{Cov}(M_T, R)$:

    - **Stock** ($\text{Cov}(M_T, S_T) < 0$): The stock pays well in good states (low $M_T$) and poorly in bad states (high $M_T$). The negative covariance gives a **positive** risk premium: $\mathbb{E}^{\mathbb{P}}[R_{\text{stock}}] > R_f$. Investors demand compensation for holding an asset that amplifies their losses in bad times.

    - **Bond** ($\text{Cov}(M_T, B_T) = 0$): Zero covariance with the SDF means zero risk premium: $\mathbb{E}^{\mathbb{P}}[R_{\text{bond}}] = R_f$. The bond payoff is independent of the state of the economy.

    - **Insurance-like asset** ($\text{Cov}(M_T, X_T) > 0$): This asset pays well in bad states (high $M_T$). The positive covariance gives a **negative** risk premium: $\mathbb{E}^{\mathbb{P}}[R_X] < R_f$. Investors accept below-market returns because the asset provides valuable hedging in downturns. Examples include put options, gold (sometimes), and Treasury bonds during flight-to-quality episodes.

---

**Exercise 5.**
An asset pays only in market crashes. Empirically, its expected return is below the risk-free rate. Without using CAPM, beta, or any formula, explain why investors willingly accept below-market returns on this asset using only the SDF framework.

??? success "Solution to Exercise 5"
    In bad states (crashes), marginal utility is high, so the SDF $M_T$ is high. An asset that pays only in these states has positive covariance with $M_T$ — its payoffs are concentrated in states where investors value wealth most. Investors willingly pay a premium (accept lower returns) because the asset delivers wealth exactly when it is most needed.

    The SDF weights these crash-state payoffs heavily, making the asset's price high relative to its expected payoff. A high price today means a low expected return. This is the SDF explanation of why insurance-like assets earn below the risk-free rate: they are not "bad investments" — they are expensive because they hedge the states investors fear most.

---

**Exercise 6.**
In one sentence, what does the stochastic discount factor do?

??? success "Solution to Exercise 6"
    The SDF converts a payoff in any future state into its present value by encoding both the time value of money and the investor's relative preference for wealth in that state versus today — equivalently, it gives the price per unit of probability in each state of the world. Every pricing formula, risk premium, and measure change in this chapter is a consequence of this single object.
