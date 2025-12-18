# Girsanov’s Theorem: Intuition and Motivation

Girsanov’s theorem explains how **changing probability measures changes drift** while preserving the Brownian motion structure.  
Before stating the full theorem and proof, we develop intuition in the simplest setting and explain *why* this result is essential in stochastic modeling and mathematical finance.

---

## 1. Why Change Measure?

In many stochastic models, especially in finance, we distinguish between:

- **The physical (real-world) measure** \( \mathbb{P} \):  
  Describes how randomness actually unfolds in reality.

- **The risk-neutral (pricing) measure** \( \mathbb{Q} \):  
  A mathematical construct under which discounted asset prices are martingales.

The challenge is that **Brownian motion under one measure may not be Brownian under another**.  
Girsanov’s theorem tells us *exactly* how to change measures so that Brownian motion remains Brownian — but with a modified drift.

---

## 2. A First Look: Brownian Motion with Drift

Let \( W_t \) be a standard Brownian motion under \( \mathbb{P} \).

Define a new process:

\[
Y_t := W_t + \theta t
\]



Under \( \mathbb{P} \), this is **not** a Brownian motion — it has deterministic drift \( \theta \).

**Question:**  
Can we find a new probability measure \( \mathbb{Q} \) under which \( Y_t \) *is* a Brownian motion?

**Answer:**  
Yes — by changing the measure appropriately.  
This is the essence of Girsanov’s theorem.

---

## 3. The Key Idea: Reweighting Paths

Probability measures assign **weights to paths** of Brownian motion.

To remove the drift \( \theta \), we must:
- Decrease the likelihood of paths that grow too fast
- Increase the likelihood of paths that grow too slowly

This is achieved by the **exponential martingale**

\[
Z_t = \exp\left(
-\theta W_t - \frac{1}{2}\theta^2 t
\right)
\]



We define a new measure \( \mathbb{Q} \) by:

\[
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_t} = Z_t
\]



This formula tells us how much more (or less) weight each path receives under \( \mathbb{Q} \).

---

## 4. What Changes — and What Does Not?

After the measure change:

- ✔ The **drift changes**
- ✔ Brownian motion structure is preserved
- ✔ Volatility is unchanged
- ✔ The filtration stays the same

Specifically:

\[
\tilde{W}_t := W_t + \theta t
\]


is a **Brownian motion under \( \mathbb{Q} \)**.

This is remarkable: a deterministic drift can be absorbed entirely into a change of measure.

---

## 5. Financial Motivation: Risk-Neutral Pricing

Consider a stock price:

\[
S_t = S_0 e^{\mu t + \sigma W_t}
\]



Under the physical measure \( \mathbb{P} \):
- Expected return = \( \mu \)

In pricing theory, we want a measure \( \mathbb{Q} \) under which:

\[
e^{-rt} S_t \quad \text{is a martingale}
\]



This requires replacing \( \mu \) by the risk-free rate \( r \).

Set:

\[
\theta = \frac{\mu - r}{\sigma}
\]



Then under the new measure \( \mathbb{Q} \):

\[
\tilde{W}_t = W_t + \theta t
\]


is Brownian, and:

\[
S_t = S_0 \exp\left(
\left(r - \frac{1}{2}\sigma^2\right)t + \sigma \tilde{W}_t
\right)
\]



The drift has changed from \( \mu \) to \( r \).

---

## 6. Intuition Behind the Exponential Weight

The density

\[
Z_t = \exp\left(
-\theta W_t - \frac{1}{2}\theta^2 t
\right)
\]


has two roles:

1. The term \( -\theta W_t \) tilts paths upward or downward
2. The correction term \( -\frac{1}{2}\theta^2 t \) ensures:

\[
\mathbb{E}^{\mathbb{P}}[Z_t] = 1
\]



Without this correction, probabilities would no longer sum to one.

---

## 7. What Girsanov’s Theorem Really Says

> **Drift is not intrinsic — it depends on the probability measure.**

By changing the measure:
- Random fluctuations remain random
- Only the *average tendency* (drift) changes

This insight lies at the heart of:
- Risk-neutral pricing
- Stochastic control
- Filtering theory
- Mathematical finance
