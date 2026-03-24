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
