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
