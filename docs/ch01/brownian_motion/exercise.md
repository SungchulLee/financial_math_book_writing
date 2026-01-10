# Exercises: Brownian Motion

Throughout these exercises, let \( \{W_t\}_{t \ge 0} \) be a standard Brownian motion defined on a filtered probability space satisfying the usual conditions.

---

## 1. Basic Properties of Brownian Motion

1. Show that \( \mathbb{E}[W_t] = 0 \) and \( \operatorname{Var}(W_t) = t \).
2. Compute \( \mathbb{E}[W_s W_t] \) for \( 0 \le s \le t \).
3. Deduce that \( (W_t)_{t \ge 0} \) has stationary increments.

---

## 2. Gaussian Increments

Let \( 0 \le s < t \).

1. Show that \( W_t - W_s \sim \mathcal{N}(0, t - s) \).
2. Prove that \( W_t - W_s \) is independent of \( \mathcal{F}_s \).
3. Compute the characteristic function of \( W_t - W_s \).

---

## 3. Continuity and Path Properties

1. Show that \( \mathbb{E}[(W_t - W_s)^2] = |t - s| \).
2. Use Kolmogorov’s continuity theorem to justify the existence of a continuous modification.
3. Why does Brownian motion fail to be differentiable almost surely?

---

## 4. Scaling Property

Let \( a > 0 \) and define

\[
X_t := \frac{1}{\sqrt{a}} W_{a t}.
\]



1. Show that \( (X_t)_{t \ge 0} \) is a standard Brownian motion.
2. Explain why this property is called *self-similarity*.
3. How does this scaling affect variance and time units?

---

## 5. Reflection Principle

Let

\[
M_t := \sup_{0 \le s \le t} W_s.
\]



1. Use the reflection principle to compute

\[
\mathbb{P}(M_t \ge a)
\quad \text{for } a > 0.
\]


2. Deduce the distribution of \( M_t \).
3. Compute \( \mathbb{P}(|W_t| \ge a) \) using symmetry.

---

## 6. Hitting Times

Define the stopping time

\[
\tau_a := \inf\{ t \ge 0 : W_t = a \},
\quad a > 0.
\]



1. Show that \( \mathbb{P}(\tau_a < \infty) = 1 \).
2. Compute \( \mathbb{E}[\tau_a] \), or explain why it is infinite.
3. Discuss how recurrence of Brownian motion is reflected in this result.

---

## 7. Martingales Associated with Brownian Motion

1. Show that \( (W_t)_{t \ge 0} \) is a martingale.
2. Show that \( (W_t^2 - t)_{t \ge 0} \) is a martingale.
3. Is \( (W_t^3)_{t \ge 0} \) a martingale? Justify your answer.

---

## 8. Quadratic Variation

Let \( \Pi_n \) be a partition of \( [0,t] \) with mesh going to zero. Consider

\[
Q_n := \sum_{i} (W_{t_{i+1}} - W_{t_i})^2.
\]



1. Show that \( \mathbb{E}[Q_n] = t \).
2. Show that \( Q_n \to t \) in probability.
3. Explain why this distinguishes Brownian motion from smooth functions.

---

## 9. Covariation of Brownian Motion

Let \( W_t \) and \( \widetilde{W}_t \) be independent Brownian motions.

1. Compute the quadratic covariation \( \langle W, \widetilde{W} \rangle_t \).
2. What changes if \( \widetilde{W}_t = \rho W_t + \sqrt{1-\rho^2} B_t \), where \( B_t \) is independent of \( W_t \)?
3. Interpret the result in terms of correlation.

---

## 10. Exponential Martingales

Define

\[
M_t := \exp\left( \lambda W_t - \frac12 \lambda^2 t \right),
\quad \lambda \in \mathbb{R}.
\]



1. Show that \( (M_t)_{t \ge 0} \) is a martingale.
2. Compute \( \mathbb{E}[M_t] \).
3. Explain why this martingale is fundamental in stochastic calculus and finance.

---

## 11. Law of the Iterated Logarithm (Qualitative)

The law of the iterated logarithm states that

\[
\limsup_{t \to 0^+}
\frac{W_t}{\sqrt{2 t \log \log (1/t)}} = 1
\quad \text{a.s.}
\]



1. Interpret this result intuitively.
2. What does it say about the “roughness” of Brownian paths?
3. Why is this result incompatible with differentiability?

---

## 12. Challenge Problems (Optional)

1. Show that Brownian motion has infinite total variation on any interval.
2. Prove that Brownian motion is Hölder continuous of any order \( \alpha < \tfrac12 \), but of no higher order.
3. Investigate how Brownian motion changes under time reversal.
