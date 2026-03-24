# Theoretical Impossibility Results


Beyond practical challenges, there are **theoretical limits** to what learning algorithms can achieve in financial markets.

---

## No-free-lunch principles


No-free-lunch theorems state that:
- averaged over all data-generating processes,
- no learning algorithm outperforms others.

Assumptions drive performance, not algorithms alone.

---

## Market efficiency arguments


Under strong forms of market efficiency:
- predictable excess returns cannot persist,
- learning algorithms cannot systematically outperform.

Any discovered pattern may vanish once exploited.

---

## Adversarial and adaptive markets


In adaptive markets:
- strategies change the environment,
- learning induces feedback effects,
- convergence guarantees may fail.

This limits long-term learnability.

---

## Implications for practice


Impossibility results imply:
- performance guarantees are fragile,
- humility is required in model claims,
- robustness matters more than optimality.

Learning must be combined with judgment.

---

## Key takeaways


- There are fundamental limits to learning.
- Efficiency and adaptivity constrain predictability.
- Robust risk management dominates pure optimization.

---

## Further reading


- Wolpert & Macready, no-free-lunch theorems.
- Farmer, markets as adaptive systems.

---

## Exercises

**Exercise 1.** State the No-Free-Lunch theorem for optimization: averaged over all possible objective functions, no optimization algorithm outperforms random search. Explain why this theorem does not make optimization useless in practice---what role do problem-specific assumptions (structure, smoothness, convexity) play in making certain algorithms effective for financial applications?

---

**Exercise 2.** Under the strong form of the Efficient Market Hypothesis, all information (public and private) is reflected in prices. If true, show that the best predictor of tomorrow's return is zero (a martingale). What does this imply for any learning algorithm attempting to forecast returns? Under what weaker form of efficiency can learning algorithms still add value?

---

**Exercise 3.** In an adaptive market (Lo, 2004), strategies that exploit inefficiencies attract capital, which erodes the inefficiency. Model this as a simple game: strategy $i$ earns return $\alpha_i(1 - c_i/C)$ where $c_i$ is capital allocated and $C$ is a capacity parameter. Show that in equilibrium, all strategies earn zero excess return. How does this limit the long-run profitability of any learned strategy?

---

**Exercise 4.** The bias-variance decomposition states that expected prediction error = bias$^2$ + variance + irreducible noise. In a financial time series with signal-to-noise ratio $\text{SNR} = 0.01$ (typical for daily returns), compute the minimum number of observations needed to detect the signal at the 5% significance level using $n \geq (z_{0.025}/\text{SNR})^2$. What does this imply about the feasibility of learning from short samples?

---

**Exercise 5.** A fundamental impossibility in adversarial settings is that if an agent's strategy is predictable, a counterparty can exploit it. Formalize this: if a trading algorithm $\mathcal{A}$ produces trades $\{a_t\}$ that are $\mathcal{F}_{t-1}$-measurable, an adversary with knowledge of $\mathcal{A}$ can construct prices $\{S_t\}$ such that $\mathcal{A}$ loses money. How does this relate to the game-theoretic foundations of market microstructure?

---

**Exercise 6.** Compare the implications of impossibility results for two contexts: (a) high-frequency trading where the data-generating process is approximately stationary over short horizons, and (b) macro factor investing where regimes span years. In which context are impossibility results more binding, and why? Propose a practical framework for deciding when learning is likely to succeed.
