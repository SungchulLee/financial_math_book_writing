# Exercises: Itô Isometry and Stochastic Integrals

Throughout these exercises, let \( \{W_t\}_{t \ge 0} \) be a standard Brownian motion on a filtered probability space satisfying the usual conditions.

---

## 1. Basic Computation via Itô Isometry

Let

\[
X_t := \int_0^t W_s \, dW_s.
\]



1. Compute \( \mathbb{E}[X_t] \).
2. Use the Itô isometry to compute \( \mathbb{E}[X_t^2] \).
3. Deduce \( \operatorname{Var}(X_t) \).

*Hint:* You may later verify the result using Itô’s formula applied to \( W_t^2 \).

---

## 2. Polynomial Integrands

Let

\[
I_t := \int_0^t s^n \, dW_s,
\quad n \in \mathbb{Z}_{\ge 0}.
\]



1. Show that \( \mathbb{E}[I_t] = 0 \).
2. Compute \( \mathbb{E}[I_t^2] \) explicitly.
3. Describe how the variance depends on \( n \) and \( t \).

---

## 3. Proof of the Itô Isometry (Simple Processes)

Let

\[
f(s) = \sum_{k=0}^{m-1} f_k \mathbf{1}_{[t_k, t_{k+1})}(s),
\]


where each \( f_k \) is \( \mathcal{F}_{t_k} \)-measurable and square-integrable.

Prove that

\[
\mathbb{E}\left[\left( \int_0^T f(s)\, dW_s \right)^2\right]
=
\mathbb{E}\left[ \int_0^T f(s)^2\, ds \right].
\]



*Hint:* Expand the square and use conditional expectation to eliminate cross terms.

---

## 4. Martingale Test

Define

\[
M_t := \int_0^t e^{-s} \, dW_s.
\]



1. Show that \( (M_t)_{t \ge 0} \) is a martingale.
2. Compute \( \mathbb{E}[M_t^2] \).
3. Does \( M_t \) converge in \( L^2 \) as \( t \to \infty \)?

---

## 5. Integration by Parts with Itô Integrals

Let

\[
X_t := \int_0^t W_s \, dW_s,
\qquad
Y_t := W_t^2.
\]



1. Use Itô’s product rule to compute \( d(X_t Y_t) \).
2. Identify the drift and martingale terms explicitly.
3. Determine whether \( X_t Y_t \) is a martingale.

---

## 6. Random Integrands

Let

\[
X_t := \int_0^t W_s^2 \, dW_s.
\]



1. Show that \( X_t \) is a martingale.
2. Compute \( \mathbb{E}[X_t] \).
3. Use the Itô isometry to compute \( \mathbb{E}[X_t^2] \).
4. Comment on the difficulty of controlling higher moments.

---

## 7. Itô Integral as a Limit of Riemann Sums

Let \( 0 = t_0 < t_1 < \dots < t_n = t \) be a partition of \( [0,t] \), and define

\[
S_n := \sum_{i=0}^{n-1} W_{t_i} (W_{t_{i+1}} - W_{t_i}).
\]



1. Show that \( \mathbb{E}[S_n] = 0 \).
2. Compute \( \mathbb{E}[S_n^2] \).
3. Show that \( S_n \to \int_0^t W_s\, dW_s \) in \( L^2 \) as the mesh of the partition tends to zero.

---

## 8. Time-Dependent Integrands

Let

\[
X_t := \int_0^t \sqrt{s} \, dW_s.
\]



1. Compute \( \mathbb{E}[X_t] \).
2. Use the Itô isometry to compute \( \mathbb{E}[X_t^2] \).
3. Interpret the result in terms of time-dependent volatility.

---

## 9. Quadratic Variation of an Itô Integral

Let

\[
X_t := \int_0^t \sin(W_s) \, dW_s.
\]



1. Compute the quadratic variation \( \langle X \rangle_t \).
2. Is \( X_t \) a martingale?
3. State general conditions under which

\[
\left\langle \int_0^t f(W_s)\, dW_s \right\rangle_t
= \int_0^t f(W_s)^2\, ds
\]


holds.

---

## 10. Comparing Stochastic and Deterministic Integrals

Compute

\[
\mathbb{E}\left[\left(\int_0^T W_s \, dW_s\right)^2\right]
\quad \text{and} \quad
\mathbb{E}\left[ \int_0^T W_s^2 \, ds \right].
\]



1. Evaluate both quantities explicitly.
2. Compare their dependence on \( T \).
3. Explain what this reveals about the variance and geometry of Itô integrals.

---

## 11. Challenge Problems (Optional)

1. Show that

\[
\int_0^t W_s\, dW_s = \frac12 \bigl(W_t^2 - t\bigr).
\]


2. Let \( X_t = \int_0^t f(s)\, dW_s \). Prove that \( X_t \) has continuous sample paths.
3. Investigate how the results of Problems 1–10 change when the Stratonovich integral is used instead.
