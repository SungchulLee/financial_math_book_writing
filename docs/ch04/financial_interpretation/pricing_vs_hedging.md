# Pricing vs Hedging


Although pricing and hedging are closely related, they represent **distinct
economic problems**. Measure change clarifies the difference between them.

---

## Pricing: A Valuation Problem


Pricing asks the question:

> *What is the fair value of a contingent claim today?*

Under no-arbitrage, the price of a payoff \(X_T\) at time \(T\) is given by

\[
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[ e^{-\int_0^T r_s ds} X_T \right]
\]

where \(\mathbb{Q}\) is a risk-neutral measure.

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

## Why Pricing Uses \(\mathbb{Q}\)


Pricing is measure-dependent because it is a valuation exercise.
The risk-neutral measure incorporates risk preferences implicitly through the
change of measure.

Hedging, however, is **measure-invariant**:

- A self-financing strategy remains self-financing under any equivalent measure.
- Replication arguments do not depend on \(\mathbb{P}\) or \(\mathbb{Q}\).

---

## Complete vs Incomplete Markets


- In **complete markets**, pricing and hedging coincide:
  the price is the cost of the unique replicating strategy.
- In **incomplete markets**, pricing is not unique, and hedging is imperfect.

This distinction will reappear in later chapters on model risk and robust pricing.

---

## Summary


- Pricing is a valuation problem → use \(\mathbb{Q}\).
- Hedging is a trading problem → measure-independent.
- Confusing the two leads to conceptual errors.

Understanding this distinction is essential for interpreting risk-neutral pricing
correctly.

---

## Exercises

**Exercise 1.**
Consider a European call option with payoff $X_T = (S_T - K)^+$ in a complete market. Write the risk-neutral pricing formula for $V_0$ and explain why the formula does not involve the physical drift $\mu$ of the underlying asset.

---

**Exercise 2.**
A trader constructs a self-financing replicating portfolio $(\phi_t, \psi_t)$ consisting of $\phi_t$ shares of stock and $\psi_t$ units of the risk-free bond. Show that the self-financing condition

$$
dV_t = \phi_t\,dS_t + \psi_t\,dB_t
$$

holds under both $\mathbb{P}$ and $\mathbb{Q}$. Explain why this demonstrates that hedging is measure-invariant.

---

**Exercise 3.**
In an incomplete market with two Brownian motions but only one traded asset, the risk-neutral measure is not unique. Explain why the price of a non-traded contingent claim depends on the choice of $\mathbb{Q}$, while the hedging strategy using only the traded asset does not fully replicate the claim. What is the financial interpretation of the residual risk?

---

**Exercise 4.**
Consider a market where a stock follows geometric Brownian motion under $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

A derivative has payoff $\Phi(S_T)$. A practitioner argues: "Since hedging does not depend on the measure, I can compute my hedge ratios under $\mathbb{P}$ instead of $\mathbb{Q}$." Is this correct? Carefully distinguish between computing the hedge ratio and determining the derivative price.

---

**Exercise 5.**
In a complete market, the price of a contingent claim equals the cost of its unique replicating portfolio. Prove that if two different risk-neutral measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ both existed in a complete market, they would assign the same price to every contingent claim, and conclude that $\mathbb{Q}_1 = \mathbb{Q}_2$.

---

**Exercise 6.**
A market has two assets: a risk-free bond with rate $r$ and a stock $S_t$. A new non-traded asset $Y_t$ is introduced, correlated with $S_t$ but not directly hedgeable. Explain the difference between the pricing interval $[\underline{V}, \overline{V}]$ for a claim on $Y_T$ and the unique price that would exist if $Y_t$ were traded. How does the width of the pricing interval relate to the correlation between $Y_t$ and $S_t$?

---

**Exercise 7.**
A practitioner computes the Black-Scholes delta $\Delta = \partial V / \partial S$ for hedging but uses historical (physical measure) volatility $\sigma_{\mathbb{P}}$ instead of implied volatility $\sigma_{\mathrm{imp}}$. Explain the conceptual error and describe the financial consequences in terms of the gamma P&L decomposition.
