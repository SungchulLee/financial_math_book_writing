# Exercises


Throughout these exercises, let \( (\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P}) \) be a filtered probability space satisfying the usual conditions.

---

## Filtrations


1. Give an intuitive explanation of what a filtration represents.
2. Show that if \( s \le t \), then \( \mathcal{F}_s \subseteq \mathcal{F}_t \).
3. Provide an example of a stochastic process that is **not** adapted to a given filtration.

---

## Natural Filtration


Let \( (W_t)_{t \ge 0} \) be a Brownian motion.

1. Define the natural filtration \( \mathcal{F}_t^W \).
2. Explain why \( W_t \) is adapted to \( \mathcal{F}_t^W \).
3. Why is it necessary to take the usual augmentation of this filtration?

---

## Adapted Predictable


1. Define what it means for a process to be adapted.
2. Define a predictable process.
3. Give an example of an adapted process that is not predictable.
4. Explain why predictability is required for defining the Itô integral.

---

## Definition


Let \( (X_t)_{t \ge 0} \) be an integrable adapted process.

1. State the definition of a martingale.
2. Define submartingales and supermartingales.
3. Give an example of each.

---

## Simple Martingale


Determine whether the following processes are martingales with respect to their natural filtrations:

1. \( W_t \)
2. \( W_t^2 \)
3. \( W_t^2 - t \)
4. \( e^{\lambda W_t} \), \( \lambda \in \mathbb{R} \)

Justify each answer.

---

## Conditional


Let \( X \in L^1(\Omega) \) and define

\[
M_t := \mathbb{E}[X \mid \mathcal{F}_t].
\]



1. Show that \( (M_t)_{t \ge 0} \) is a martingale.
2. Explain why conditional expectation represents *best prediction given current information*.
3. Give an example where \( M_t \) is constant in time.

---

## Stopping Times


1. Define a stopping time with respect to a filtration.
2. Show that the hitting time

\[
\tau_a := \inf\{ t \ge 0 : W_t = a \}
\]


is a stopping time.
3. Give an example of a random time that is **not** a stopping time.

---

## Optional Stopping


Let \( (M_t)_{t \ge 0} \) be a martingale and \( \tau \) a stopping time.

1. State the Optional Stopping Theorem informally.
2. Why are integrability and boundedness conditions required?
3. Give an example where optional stopping fails.

---

## Doob Decomposition


Let \( (X_t)_{t \ge 0} \) be a submartingale.

1. State the Doob–Meyer decomposition theorem (informally).
2. Explain the roles of the martingale and predictable increasing process.
3. Why is this decomposition fundamental in stochastic calculus?

---

## Uniform


1. Define uniform integrability.
2. Explain why uniform integrability is important for martingale convergence.
3. Give an example of a martingale that is not uniformly integrable.

---

## Martingale


1. State the martingale convergence theorem.
2. What role does uniform integrability play?
3. Give an example of a martingale that converges almost surely but not in \( L^1 \).

---

## Doob s Inequalities


Let \( (M_t)_{t \ge 0} \) be a martingale.

1. State Doob’s maximal inequality.
2. Explain how it controls the size of martingale fluctuations.
3. Apply it to bound

\[
\mathbb{P}\left( \sup_{0 \le s \le t} |W_s| \ge a \right).
\]



---

## Discrete Time


Let \( (X_n, \mathcal{F}_n)_{n \ge 0} \) be a discrete-time process.

1. State the definition of a discrete-time martingale.
2. Give an example arising from a fair coin-tossing game.
3. Explain how discrete-time martingales motivate the continuous-time theory.

---

## Martingales Fair


1. Explain the interpretation of martingales as “fair games.”
2. Why does increasing expected wealth contradict the martingale property?
3. How does this relate to the absence of arbitrage in financial markets?

---

## Challenge Problems


1. Show that every bounded martingale is uniformly integrable.
2. Prove that if \( (M_t) \) is a martingale, then \( \mathbb{E}[M_t] \) is constant in time.
3. Investigate whether \( \exp(W_t^2 - t) \) is a martingale.
