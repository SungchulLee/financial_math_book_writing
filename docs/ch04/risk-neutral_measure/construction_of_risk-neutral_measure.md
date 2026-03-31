# Construction of the Risk-Neutral Measure


The risk-neutral measure is a probability measure under which discounted asset prices
are martingales. Its existence is the mathematical expression of the absence of arbitrage.

This section explains how the risk-neutral measure is constructed using Girsanov’s theorem.

---

## Market Model


Consider a financial market consisting of:
- a risk-free asset \(B_t\),
- a risky asset \(S_t\).

Under the physical measure \(\mathbb{P}\), assume
\[
dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{P}},
\qquad
dB_t = r_t B_t\,dt,
\]
where \(\mu_t\), \(\sigma_t\), and \(r_t\) are adapted processes.

---

## Discounted Asset Price


Define the discounted price process
\[
\tilde S_t := \frac{S_t}{B_t}.
\]

Applying Itô’s formula,
\[
d\tilde S_t
= (\mu_t - r_t)\tilde S_t\,dt
+ \sigma_t \tilde S_t\,dW_t^{\mathbb{P}}.
\]

The presence of the drift term \((\mu_t - r_t)\) prevents \(\tilde S_t\) from being
a martingale under \(\mathbb{P}\).

---

## Measure Change


Define the process
\[
\theta_t := \frac{\mu_t - r_t}{\sigma_t},
\]
and the stochastic exponential
\[
Z_t = \exp\!\left(
- \int_0^t \theta_s\,dW_s^{\mathbb{P}}
- \frac12 \int_0^t \theta_s^2\,ds
\right).
\]

Under suitable integrability conditions, \(Z_t\) is a martingale and defines a new
probability measure \(\mathbb{Q}\) by
\[
\frac{d\mathbb{Q}}{d\mathbb{P}} \Big|_{\mathcal{F}_t} = Z_t.
\]

---

## Risk-Neutral Dynamics


By Girsanov’s theorem, the process
\[
W_t^{\mathbb{Q}} := W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds
\]
is a Brownian motion under \(\mathbb{Q}\).

The discounted asset price then satisfies
\[
d\tilde S_t = \sigma_t \tilde S_t\,dW_t^{\mathbb{Q}},
\]
and is therefore a martingale.

---

## Definition


A **risk-neutral measure** is a probability measure \(\mathbb{Q}\) equivalent to
\(\mathbb{P}\) under which all discounted traded asset prices are martingales.

Its existence ensures arbitrage-free pricing.

---

## Exercises

**Exercise 1.**
A stock has physical dynamics $dS_t = 0.10\,S_t\,dt + 0.25\,S_t\,dW_t^{\mathbb{P}}$ with risk-free rate $r = 0.04$. Compute the market price of risk $\theta$, write the Radon-Nikodym derivative $Z_T$, and derive the discounted price dynamics under $\mathbb{Q}$. Verify that the discounted price is a $\mathbb{Q}$-martingale.

---

**Exercise 2.**
Starting from the discounted price $\tilde{S}_t = S_t / B_t$ and its dynamics $d\tilde{S}_t = (\mu_t - r_t)\tilde{S}_t\,dt + \sigma_t\tilde{S}_t\,dW_t^{\mathbb{P}}$, show that choosing $\theta_t = (\mu_t - r_t)/\sigma_t$ and defining $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$ eliminates the drift term in the $\tilde{S}_t$ dynamics. Why is this drift removal equivalent to the martingale property?

---

**Exercise 3.**
Explain why the risk-neutral measure $\mathbb{Q}$ must be equivalent to $\mathbb{P}$ (i.e., both measures agree on which events have probability zero). What would go wrong financially if $\mathbb{Q}$ assigned positive probability to an event that is impossible under $\mathbb{P}$?

---

**Exercise 4.**
For time-varying coefficients $\mu_t$, $\sigma_t$, and $r_t$, the market price of risk $\theta_t = (\mu_t - r_t)/\sigma_t$ is a stochastic process. State the Novikov condition that ensures $Z_t$ is a true martingale and $\mathbb{Q}$ is well-defined. Give an example where the condition fails.

---

**Exercise 5.**
Consider a market with two risky assets and one Brownian motion. Write the system of equations that $\theta$ must satisfy for both discounted prices to be $\mathbb{Q}$-martingales. Under what condition on $\mu_1, \mu_2, \sigma_1, \sigma_2, r$ is the system consistent (i.e., no arbitrage)?

---

**Exercise 6.**
A student claims: "The risk-neutral measure is the probability measure that investors actually use to form expectations." Explain why this is incorrect and describe the correct interpretation of $\mathbb{Q}$.

---

**Exercise 7.**
Suppose the risk-free rate is stochastic: $dr_t = \alpha(r_t)\,dt + \beta(r_t)\,dW_t^{\mathbb{P}}$, and the same Brownian motion drives the stock. Write the discounted stock price dynamics and determine $\theta_t$. Explain why this market is complete (one Brownian motion, one traded asset besides the bond).

---

## Solutions

??? success "Solution to Exercise 1"
    Given $\mu = 0.10$, $\sigma = 0.25$, and $r = 0.04$, the market price of risk is

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.10 - 0.04}{0.25} = 0.24
    $$

    The Radon-Nikodym derivative at time $T$ is

    $$
    Z_T = \exp\!\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right) = \exp\!\left(-0.24\,W_T^{\mathbb{P}} - \frac{1}{2}(0.24)^2 T\right)
    $$

    Under $\mathbb{Q}$, the process $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t = W_t^{\mathbb{P}} + 0.24\,t$ is a Brownian motion. Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - 0.24\,dt$ into the stock dynamics:

    $$
    dS_t = 0.10\,S_t\,dt + 0.25\,S_t\,(dW_t^{\mathbb{Q}} - 0.24\,dt) = 0.04\,S_t\,dt + 0.25\,S_t\,dW_t^{\mathbb{Q}}
    $$

    The discounted price $\tilde{S}_t = e^{-0.04\,t}S_t$ satisfies

    $$
    d\tilde{S}_t = 0.25\,\tilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    Since the drift vanishes, $\tilde{S}_t$ is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 2"
    Starting from the discounted price dynamics

    $$
    d\tilde{S}_t = (\mu_t - r_t)\tilde{S}_t\,dt + \sigma_t\tilde{S}_t\,dW_t^{\mathbb{P}}
    $$

    we define $\theta_t = (\mu_t - r_t)/\sigma_t$ and $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$. Then $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta_t\,dt$, and substituting:

    $$
    d\tilde{S}_t = (\mu_t - r_t)\tilde{S}_t\,dt + \sigma_t\tilde{S}_t\,(dW_t^{\mathbb{Q}} - \theta_t\,dt)
    $$

    $$
    = (\mu_t - r_t)\tilde{S}_t\,dt - \sigma_t\theta_t\tilde{S}_t\,dt + \sigma_t\tilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    Since $\sigma_t\theta_t = \mu_t - r_t$, the drift terms cancel exactly:

    $$
    d\tilde{S}_t = \sigma_t\tilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    The drift removal is equivalent to the martingale property because a continuous local martingale of the form $dX_t = \sigma_t X_t\,dW_t$ has zero drift, meaning $\mathbb{E}^{\mathbb{Q}}[\tilde{S}_t \mid \mathcal{F}_s] = \tilde{S}_s$ for $s \le t$ (assuming appropriate integrability). A process is a martingale if and only if it has zero drift in its semimartingale decomposition, so eliminating the drift is precisely what makes $\tilde{S}_t$ a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 3"
    The risk-neutral measure $\mathbb{Q}$ must be equivalent to $\mathbb{P}$, meaning they agree on which events have probability zero. This equivalence is essential for two reasons:

    **If $\mathbb{Q}(A) > 0$ for some event $A$ with $\mathbb{P}(A) = 0$**: Then $\mathbb{Q}$ assigns positive probability to a physically impossible event. This means derivative prices under $\mathbb{Q}$ could depend on payoffs in scenarios that can never occur, leading to economically nonsensical prices. One could construct "arbitrage" by selling claims that pay in impossible states, collecting premium for risk that can never materialize.

    **If $\mathbb{Q}(A) = 0$ for some event $A$ with $\mathbb{P}(A) > 0$**: Then there exists a physically possible event whose payoff is completely ignored in pricing. An agent could buy a claim that pays in state $A$ for zero cost (since $\mathbb{Q}$ gives it zero weight) but receives a positive payoff with positive physical probability, creating an arbitrage opportunity.

    Equivalence ensures a one-to-one correspondence between possible and priced events, which is exactly the no-arbitrage condition.

??? success "Solution to Exercise 4"
    The Novikov condition states that $Z_t$ is a true martingale (and hence $\mathbb{Q}$ is well-defined) if

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
    $$

    This is a sufficient condition ensuring that the stochastic exponential $Z_t = \exp\!\left(-\int_0^t \theta_s\,dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)$ is a uniformly integrable martingale, not merely a local martingale.

    **Example where Novikov fails:** Consider $\sigma_t = \sigma$ constant and $\mu_t - r_t = \sigma / \sqrt{T - t}$ for $t < T$. Then $\theta_t = 1/\sqrt{T-t}$ and

    $$
    \int_0^T \theta_s^2\,ds = \int_0^T \frac{1}{T-s}\,ds = +\infty
    $$

    The integral diverges, so the Novikov condition fails. In this case, $Z_t$ may fail to be a true martingale, and a well-defined equivalent measure $\mathbb{Q}$ may not exist.

??? success "Solution to Exercise 5"
    With two risky assets $S^1, S^2$ and one Brownian motion $W_t$, the dynamics are

    $$
    dS_t^i = \mu_i S_t^i\,dt + \sigma_i S_t^i\,dW_t^{\mathbb{P}}, \quad i = 1, 2
    $$

    For both discounted prices to be $\mathbb{Q}$-martingales, we need a single $\theta$ satisfying

    $$
    \mu_1 - r = \sigma_1 \theta, \qquad \mu_2 - r = \sigma_2 \theta
    $$

    From the first equation, $\theta = (\mu_1 - r)/\sigma_1$. Substituting into the second:

    $$
    \mu_2 - r = \sigma_2 \cdot \frac{\mu_1 - r}{\sigma_1}
    $$

    This simplifies to the **no-arbitrage consistency condition**:

    $$
    \frac{\mu_1 - r}{\sigma_1} = \frac{\mu_2 - r}{\sigma_2}
    $$

    Both assets must have the same Sharpe ratio. If this condition is violated, say $(\mu_1 - r)/\sigma_1 > (\mu_2 - r)/\sigma_2$, then no risk-neutral measure exists, and an arbitrage strategy can be constructed: go long asset 1 and short asset 2 in proportions that eliminate the Brownian motion exposure while retaining a positive drift.

??? success "Solution to Exercise 6"
    The risk-neutral measure $\mathbb{Q}$ is **not** the probability measure investors use to form expectations. Under the physical measure $\mathbb{P}$, investors form beliefs about actual probabilities of future events and demand compensation (risk premia) for bearing risk.

    The correct interpretation: $\mathbb{Q}$ is an artificial probability measure constructed so that discounted asset prices are martingales. Under $\mathbb{Q}$, all assets earn the risk-free rate in expectation — risk premia have been absorbed into the probability weighting. The measure $\mathbb{Q}$ encodes both the physical probabilities **and** the market prices of risk into a single object.

    Pricing under $\mathbb{Q}$ is a mathematical convenience, not a statement about investor beliefs. The formula $V_t = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}\Phi_T \mid \mathcal{F}_t]$ gives the no-arbitrage price, which reflects both the probability of outcomes (from $\mathbb{P}$) and the risk adjustment (from $\theta$), combined into the tilted measure $\mathbb{Q}$. In markets with risk-averse investors, $\mathbb{Q}$ typically overweights adverse outcomes relative to $\mathbb{P}$.

??? success "Solution to Exercise 7"
    With $dr_t = \alpha(r_t)\,dt + \beta(r_t)\,dW_t^{\mathbb{P}}$ and $dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{P}}$ driven by the same Brownian motion, the discounted price $\tilde{S}_t = S_t / B_t$ where $B_t = \exp(\int_0^t r_s\,ds)$ satisfies (by Itô's formula):

    $$
    d\tilde{S}_t = (\mu_t - r_t)\tilde{S}_t\,dt + \sigma_t\tilde{S}_t\,dW_t^{\mathbb{P}}
    $$

    The market price of risk is

    $$
    \theta_t = \frac{\mu_t - r_t}{\sigma_t}
    $$

    Note that $\theta_t$ is now stochastic since both $\mu_t$ and $r_t$ may depend on the state. Under the measure change with $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$, the risk-neutral dynamics become $d\tilde{S}_t = \sigma_t\tilde{S}_t\,dW_t^{\mathbb{Q}}$ and

    $$
    dS_t = r_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{Q}}
    $$

    $$
    dr_t = [\alpha(r_t) - \beta(r_t)\theta_t]\,dt + \beta(r_t)\,dW_t^{\mathbb{Q}}
    $$

    The market is **complete** because there is exactly one source of randomness (one Brownian motion) and one traded risky asset (the stock). The single equation $\mu_t - r_t = \sigma_t\theta_t$ uniquely determines $\theta_t$, leaving no free parameters. This means there is a unique risk-neutral measure, and every contingent claim can be replicated by a dynamic portfolio of the stock and the bond.
