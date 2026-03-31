# Physical vs Risk-Neutral World


The distinction between the physical and risk-neutral probability measures is
one of the most common sources of confusion in quantitative finance.

This section clarifies their respective roles.

---

## The Physical Measure \(\mathbb{P}\)


The physical (or real-world) measure describes how asset prices actually evolve.
It reflects:

- economic growth,
- investor risk preferences,
- empirical return distributions.

Under \(\mathbb{P}\), expected returns include risk premia.

---

## The Risk-Neutral Measure \(\mathbb{Q}\)


The risk-neutral measure is a **pricing tool**, not a description of reality.
Under \(\mathbb{Q}\):

- discounted asset prices are martingales,
- expected excess returns vanish,
- probabilities are adjusted for risk.

It is constructed mathematically via Girsanov’s theorem or numéraire techniques.

---

## Same Paths, Different Weights


A crucial point is that \(\mathbb{P}\) and \(\mathbb{Q}\) are **equivalent measures**:

- they assign positive probability to the same events,
- but with different likelihoods.

Thus, measure change does not alter which scenarios are possible,
only how they are weighted.

---

## Why \(\mathbb{Q}\) Is Not “Believed”


The risk-neutral measure should not be interpreted as:

- a forecast of future prices,
- an investor’s belief,
- a statistical model of returns.

Its sole purpose is to ensure arbitrage-free pricing.

Forecasting and risk management must be performed under \(\mathbb{P}\).

---

## Practical Implications


- Use \(\mathbb{Q}\) for pricing derivatives.
- Use \(\mathbb{P}\) for risk, forecasting, and portfolio optimization.
- Mixing the two leads to systematic errors.

---

## Takeaway


> The physical measure explains the world.
> The risk-neutral measure prices claims in it.

Keeping this distinction clear is essential for both theoretical understanding
and practical modeling.

---

## Exercises

**Exercise 1.**
Let a stock follow geometric Brownian motion under the physical measure $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

with $\mu = 0.10$, $\sigma = 0.25$, and risk-free rate $r = 0.03$. Compute the market price of risk $\theta$ and write down the dynamics of $S_t$ under the risk-neutral measure $\mathbb{Q}$.

---

**Exercise 2.**
Explain why $\mathbb{P}$ and $\mathbb{Q}$ must be equivalent measures (i.e., they agree on which events have probability zero). What would go wrong economically if $\mathbb{Q}$ assigned zero probability to an event that $\mathbb{P}$ considers possible?

---

**Exercise 3.**
A risk manager estimates that a portfolio has a 5% probability of losing more than \$1 million over the next month under $\mathbb{P}$. A pricing quant computes the risk-neutral probability of the same loss to be 12%. Explain why these numbers differ and which measure is appropriate for each task.

---

**Exercise 4.**
Under $\mathbb{Q}$, the expected return on every traded asset equals the risk-free rate $r$. Does this mean that investors are indifferent to risk under $\mathbb{Q}$? Carefully explain the sense in which $\mathbb{Q}$ encodes risk preferences despite all assets earning $r$.

---

**Exercise 5.**
Consider a European call option with strike $K$ and maturity $T$. The Black-Scholes price is

$$
C_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}(S_T - K)^+\right]
$$

Explain why this formula does not involve the physical drift $\mu$. If $\mu$ were doubled while $\sigma$ and $r$ remained the same, would the option price change? Why or why not?

---

**Exercise 6.**
Suppose you observe that a stock has an expected annual return of 15% under $\mathbb{P}$ and the risk-free rate is 4%. A colleague claims: "Under $\mathbb{Q}$, the stock is expected to return only 4%, so the stock is overpriced." Identify the error in this reasoning.

---

**Exercise 7.**
In a two-period binomial model, the stock can go up by factor $u = 1.2$ or down by factor $d = 0.9$ each period. The risk-free rate per period is $R = 0.05$. Compute the physical probabilities $p^{\mathbb{P}}$ and risk-neutral probabilities $p^{\mathbb{Q}}$ if the expected return under $\mathbb{P}$ is 8% per period. Verify that both measures assign positive probability to the same events.

---

## Solutions

??? success "Solution to Exercise 1"
    The market price of risk is defined as

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.10 - 0.03}{0.25} = 0.28
    $$

    Under $\mathbb{Q}$, Girsanov's theorem gives $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, so $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$. Substituting into the $\mathbb{P}$-dynamics:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}} = \mu S_t\,dt + \sigma S_t(dW_t^{\mathbb{Q}} - \theta\,dt)
    $$

    $$
    = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}} = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    Therefore the risk-neutral dynamics are

    $$
    dS_t = 0.03\,S_t\,dt + 0.25\,S_t\,dW_t^{\mathbb{Q}}
    $$

    The drift has changed from $\mu = 0.10$ to $r = 0.03$, while the volatility $\sigma = 0.25$ is unchanged.

??? success "Solution to Exercise 2"
    The measures $\mathbb{P}$ and $\mathbb{Q}$ must be equivalent (mutually absolutely continuous) so that they agree on which events have probability zero. This means: $\mathbb{P}(A) = 0$ if and only if $\mathbb{Q}(A) = 0$ for every measurable event $A$.

    If $\mathbb{Q}$ assigned zero probability to an event $A$ that $\mathbb{P}$ considers possible ($\mathbb{P}(A) > 0$), then the risk-neutral pricing framework would ignore a scenario that can actually occur. Concretely, a contingent claim that pays off only in event $A$ would be priced at zero under $\mathbb{Q}$, yet the holder could receive a positive payoff with positive probability under $\mathbb{P}$. This would constitute a free lunch: a costless position with a non-negative payoff that is strictly positive with positive probability. Such an arbitrage opportunity is ruled out by the fundamental theorem of asset pricing, which requires equivalence of $\mathbb{P}$ and $\mathbb{Q}$.

    Conversely, if $\mathbb{P}(A) = 0$ but $\mathbb{Q}(A) > 0$, the pricing measure would assign positive weight to impossible events, distorting prices.

??? success "Solution to Exercise 3"
    The two probabilities differ because they are computed under different measures serving different purposes.

    The $\mathbb{P}$-probability of 5% is the **physical** (real-world) probability of the loss event, reflecting actual market dynamics, risk premia, and empirical return distributions. This is the appropriate measure for **risk management** tasks such as computing Value-at-Risk (VaR) and expected shortfall.

    The $\mathbb{Q}$-probability of 12% is the **risk-neutral** probability, which reweights scenarios to remove risk premia and ensure that discounted prices are martingales. Under $\mathbb{Q}$, adverse outcomes (losses) are upweighted because $\mathbb{Q}$ penalizes the risk premium embedded in the physical drift. This is the appropriate measure for **pricing** derivatives and contingent claims on the portfolio.

    The risk-neutral probability is higher because the change of measure from $\mathbb{P}$ to $\mathbb{Q}$ tilts the distribution toward unfavorable outcomes (it removes the positive risk premium from asset drifts, effectively lowering expected returns). For risk management, one must use $\mathbb{P}$; for pricing, one must use $\mathbb{Q}$. Using risk-neutral probabilities for risk management would overstate the likelihood of losses, while using physical probabilities for pricing would violate no-arbitrage consistency.

??? success "Solution to Exercise 4"
    The statement that all assets earn $r$ under $\mathbb{Q}$ does **not** mean investors are indifferent to risk. The risk-neutral measure $\mathbb{Q}$ is not a description of investor beliefs or preferences---it is a mathematical construction used for pricing.

    Under $\mathbb{Q}$, risk preferences are not absent; they are **encoded in the change of measure itself**. The Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ reweights paths: scenarios with high asset returns are downweighted, and scenarios with low returns are upweighted. The magnitude of this reweighting is determined by the market price of risk $\theta = (\mu - r)/\sigma$, which directly reflects the compensation investors demand for bearing risk.

    In a world where investors were truly risk-neutral, the physical measure $\mathbb{P}$ itself would satisfy the martingale property for discounted prices, and $\mathbb{Q} = \mathbb{P}$. The fact that $\mathbb{Q} \neq \mathbb{P}$ (i.e., $\theta \neq 0$) is precisely the signature of risk aversion. The risk-neutral measure absorbs risk preferences into the probability weights, so that the simple formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(S_T)]$ can be used without explicitly modeling utility functions.

??? success "Solution to Exercise 5"
    The Black-Scholes price is computed as a discounted expectation under $\mathbb{Q}$:

    $$
    C_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}(S_T - K)^+\right]
    $$

    Under $\mathbb{Q}$, the stock dynamics are $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. The distribution of $S_T$ under $\mathbb{Q}$ depends only on $r$, $\sigma$, $S_0$, and $T$---the physical drift $\mu$ does not appear. This is because Girsanov's theorem replaces $\mu$ with $r$ when constructing $\mathbb{Q}$, and the entire pricing formula is computed under $\mathbb{Q}$.

    If $\mu$ were doubled (with $\sigma$ and $r$ unchanged), the physical dynamics would change, but the risk-neutral dynamics would remain $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. The market price of risk $\theta = (\mu - r)/\sigma$ would increase (the Radon-Nikodym derivative would change), but the distribution of $S_T$ under $\mathbb{Q}$ would be identical. Therefore, the option price $C_0$ would **not** change.

    This is the fundamental insight of Black-Scholes: option prices depend on volatility and the risk-free rate, not on the expected return of the underlying. The expected return affects only the measure change, not the risk-neutral distribution.

??? success "Solution to Exercise 6"
    The colleague's reasoning contains a fundamental conceptual error: confusing the risk-neutral expected return with a statement about valuation or mispricing.

    Under $\mathbb{Q}$, **every** traded asset has an expected return equal to the risk-free rate $r = 4\%$. This is not a statement about the stock being overpriced or underpriced; it is a mathematical property of the risk-neutral measure by construction. The measure $\mathbb{Q}$ is designed so that discounted asset prices are martingales, which automatically implies that expected returns under $\mathbb{Q}$ equal $r$.

    The fact that the stock earns 15% under $\mathbb{P}$ and only 4% under $\mathbb{Q}$ simply reflects the risk premium $\mu - r = 11\%$ that investors demand for holding the stock. This premium is removed by the measure change, not because the stock is overpriced, but because $\mathbb{Q}$ reweights probabilities to make discounted prices into martingales.

    If the colleague's logic were correct, **every** stock in the market would be "overpriced" since every stock earns only $r$ under $\mathbb{Q}$, which is clearly absurd. The risk-neutral measure is a pricing tool, not a forecast of returns.

??? success "Solution to Exercise 7"
    **Risk-neutral probabilities:** Under $\mathbb{Q}$, the expected return per period must equal the risk-free rate $R = 0.05$. Writing $1 + R = p^{\mathbb{Q}} u + (1 - p^{\mathbb{Q}})d$:

    $$
    1.05 = p^{\mathbb{Q}} \cdot 1.2 + (1 - p^{\mathbb{Q}}) \cdot 0.9
    $$

    $$
    1.05 = 0.9 + 0.3\,p^{\mathbb{Q}} \implies p^{\mathbb{Q}} = \frac{1.05 - 0.9}{1.2 - 0.9} = \frac{0.15}{0.30} = 0.5
    $$

    **Physical probabilities:** Under $\mathbb{P}$, the expected return per period is 8%, so $1 + 0.08 = p^{\mathbb{P}} u + (1 - p^{\mathbb{P}})d$:

    $$
    1.08 = p^{\mathbb{P}} \cdot 1.2 + (1 - p^{\mathbb{P}}) \cdot 0.9
    $$

    $$
    1.08 = 0.9 + 0.3\,p^{\mathbb{P}} \implies p^{\mathbb{P}} = \frac{1.08 - 0.9}{0.3} = \frac{0.18}{0.30} = 0.6
    $$

    **Verification of equivalence:** Both $p^{\mathbb{P}} = 0.6$ and $p^{\mathbb{Q}} = 0.5$ lie strictly in $(0, 1)$, so both measures assign strictly positive probability to both up and down moves. In the two-period model, the possible terminal states are $\{uu, ud, du, dd\}$, and both $\mathbb{P}$ and $\mathbb{Q}$ assign strictly positive probability to each of these four events. The measures are therefore equivalent: they agree on which events are possible, but differ in the weights assigned to each path. The physical measure assigns higher probability to upward moves ($p^{\mathbb{P}} = 0.6 > 0.5 = p^{\mathbb{Q}}$), reflecting the positive risk premium of 3% per period ($8\% - 5\%$).
