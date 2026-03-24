# Intuitive Introduction and Motivation


Girsanov’s theorem is one of the most important results in stochastic calculus,
yet it is often misunderstood at first encounter.

At an intuitive level, the theorem resolves a seeming paradox:

> *How can a stochastic process with drift become driftless, without changing its paths?*

The resolution lies in understanding the difference between **paths** and
**probability measures**.

---

## Paths vs Probability Measures


A stochastic process such as Brownian motion generates random paths

\[
\omega : [0,T] \to \mathbb{R}.
\]

A probability measure does not create new paths.
Instead, it assigns **weights** to these paths.

Changing the probability measure therefore:

- does **not** alter which paths are possible,
- but **does** change how likely each path is.

Drift is not a property of individual paths.
It is a property of how probabilities are distributed across paths.

---

## A Thought Experiment


Imagine observing many random paths over time.

Under one probability measure, paths that trend upward may be more likely.
Under another measure, those same paths may be downweighted.

From the perspective of averages:

- the first observer sees a **positive drift**,
- the second observer sees **no drift**.

The underlying paths are identical.
Only the probability weights have changed.

---

## Continuous-Time Perspective


Let \(W_t\) be Brownian motion under a measure \(\mathbb{P}\).
The process

\[
Y_t = W_t + \theta t
\]

has drift \(\theta\) under \(\mathbb{P}\).

Girsanov’s theorem answers the following question:

> *Is there another probability measure under which \(Y_t\) is a Brownian motion?*

The answer is yes.
The drift can be absorbed into the probability measure.

---

## Why This Matters in Finance


In financial markets:

- under the **physical measure**, asset prices contain risk premia,
- under the **pricing measure**, discounted prices must have no predictable trend.

Girsanov’s theorem provides the precise mechanism for moving between these two
viewpoints.

---

## The Central Idea


> **Drift lives in the probability measure, not in the paths.**

Everything that follows is a rigorous formulation of this idea.

---

## Exercises

**Exercise 1.**
Consider two observers watching the same set of stock price paths over one year. Observer A uses measure $\mathbb{P}$ and estimates a positive drift of 8%. Observer B uses measure $\mathbb{Q}$ and sees drift equal to the risk-free rate $r = 2\%$. Explain how both observers can be correct simultaneously, and describe what differs between their assessments.

---

**Exercise 2.**
Let $W_t$ be a standard Brownian motion under $\mathbb{P}$, and define $Y_t = W_t + 3t$. Under $\mathbb{P}$, compute $\mathbb{E}^{\mathbb{P}}[Y_t]$ and $\mathrm{Var}^{\mathbb{P}}(Y_t)$. Girsanov's theorem asserts there exists a measure $\mathbb{Q}$ under which $Y_t$ is a standard Brownian motion. Under $\mathbb{Q}$, what are $\mathbb{E}^{\mathbb{Q}}[Y_t]$ and $\mathrm{Var}^{\mathbb{Q}}(Y_t)$?

---

**Exercise 3.**
A skeptic argues: "If changing the probability measure does not change any sample paths, then it cannot possibly change the price of a derivative." Explain the flaw in this reasoning, using the concept that expected values (and hence prices computed as discounted expectations) depend on the measure.

---

**Exercise 4.**
Suppose you flip a biased coin with $\mathbb{P}(\text{Heads}) = 0.7$. Define a new measure $\mathbb{Q}$ with $\mathbb{Q}(\text{Heads}) = 0.5$. The sample space $\{\text{H}, \text{T}\}$ is the same under both measures. Compute the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ on each outcome and verify that $\mathbb{E}^{\mathbb{P}}[d\mathbb{Q}/d\mathbb{P}] = 1$. Use this discrete example to illustrate the intuition behind Girsanov's theorem.

---

**Exercise 5.**
In the thought experiment of observing many random paths, suppose the first observer sees an average drift of $+5\%$ per year and the second observer sees an average drift of $0\%$. If both observe the same 10,000 simulated paths, explain how the second observer's probability weights must differ from the first's. Which paths receive higher weight under the second observer's measure?

---

**Exercise 6.**
The statement "drift lives in the probability measure, not in the paths" is the central idea. Provide a concrete numerical example: take a discrete random walk with three possible paths and show that by reassigning probabilities (without adding or removing paths), you can change the expected drift from positive to zero.

---

**Exercise 7.**
Explain why the Girsanov measure change preserves the volatility of the process. Specifically, if $Y_t = W_t + \theta t$ has the same quadratic variation as $W_t$ under both $\mathbb{P}$ and $\mathbb{Q}$, what does this imply about the "roughness" or "fluctuation" of the paths? Why is this property important for option pricing?
