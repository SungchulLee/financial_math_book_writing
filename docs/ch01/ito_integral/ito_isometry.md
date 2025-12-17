# Itô Isometry

In stochastic calculus, the **Itô integral** plays the role of a *random sum* of products of a strategy and noise. Unlike deterministic integrals—where Riemann sums converge smoothly under refinement—stochastic integrals already exhibit rich probabilistic structure at the level of the sum itself.

This section explains the **Itô isometry**, first heuristically and then conceptually, highlighting why it is the fundamental identity underlying the construction of the Itô integral.

---

## 1. Heuristic Setup: Sums of Gains from Trading

Let \( W_t \) be a standard Brownian motion and let \( \beta(t) \) be a **simple adapted process**, representing (for intuition) a trading strategy: the number of shares held at each time.

Fix a partition

\[
0 = t_0 < t_1 < \dots < t_n = T,
\]


and assume \( \beta(t) = \beta_i \) on \( [t_i, t_{i+1}) \). The Itô integral is then approximated by the stochastic sum


\[
\int_0^T \beta(t)\, dW_t \;\approx\; \sum_{i=0}^{n-1} \beta_i (W_{t_{i+1}} - W_{t_i}).
\]



Each term \( \beta_i (W_{t_{i+1}} - W_{t_i}) \) can be interpreted as the **gain from holding \( \beta_i \) units of risk** over the interval \( [t_i, t_{i+1}] \), during which the Brownian motion moves by

\[
\Delta W_i := W_{t_{i+1}} - W_{t_i}.
\]



---

## 2. Squaring the Sum: Toward Variance

To understand the *size* of the Itô integral, we examine its second moment. Squaring the sum gives


\[
\left( \sum_{i=0}^{n-1} \beta_i \Delta W_i \right)^2
= \sum_{i=0}^{n-1} \beta_i^2 (\Delta W_i)^2
+ 2 \sum_{i < j} \beta_i \beta_j \Delta W_i \Delta W_j.
\]



This expansion consists of:

- **Diagonal terms**, corresponding to variances  
- **Cross terms**, corresponding to covariances  

Taking expectations,


\[
\mathbb{E}\left[ \left( \int_0^T \beta(t)\, dW_t \right)^2 \right]
= \mathbb{E}\left[ \sum_{i=0}^{n-1} \beta_i^2 (\Delta W_i)^2 \right]
+ 2 \sum_{i<j} \mathbb{E}[\beta_i \beta_j \Delta W_i \Delta W_j].
\]



The key step is to understand **why the cross terms vanish**.

---

## 3. Why the Cross Terms Vanish

Let \( (\mathcal{F}_t)_{t \ge 0} \) denote the natural filtration of the Brownian motion. Fix indices \( i < j \). Then:

- \( \beta_i \) and \( \Delta W_i \) are \( \mathcal{F}_{t_{i+1}} \)-measurable  
- \( \beta_j \) is \( \mathcal{F}_{t_j} \)-measurable  
- \( \Delta W_j \) is **independent of \( \mathcal{F}_{t_j} \)** and satisfies

  \[
  \mathbb{E}[\Delta W_j \mid \mathcal{F}_{t_j}] = 0
  \]



Using conditional expectation,


\[
\begin{aligned}
\mathbb{E}[\beta_i \beta_j \Delta W_i \Delta W_j]
&= \mathbb{E}\left[ \beta_i \Delta W_i \cdot \beta_j \Delta W_j \right] \\
&= \mathbb{E}\left[ \beta_i \Delta W_i \cdot
\mathbb{E}[ \beta_j \Delta W_j \mid \mathcal{F}_{t_j} ] \right].
\end{aligned}
\]



Since \( \beta_j \) is \( \mathcal{F}_{t_j} \)-measurable,


\[
\mathbb{E}[ \beta_j \Delta W_j \mid \mathcal{F}_{t_j} ]
= \beta_j \, \mathbb{E}[ \Delta W_j \mid \mathcal{F}_{t_j} ] = 0.
\]



Therefore,


\[
\mathbb{E}[\beta_i \beta_j \Delta W_i \Delta W_j] = 0.
\]



### Intuition

- \( \Delta W_j \) represents **future noise**, independent of everything known at time \( t_j \).
- Conditional expectation *kills the future noise*.
- Brownian increments behave like **orthogonal vectors in \( L^2 \)**.

---

## 4. The Remaining Diagonal Terms

We are left with


\[
\mathbb{E}\left[ \sum_{i=0}^{n-1} \beta_i^2 (\Delta W_i)^2 \right]
= \sum_{i=0}^{n-1} \mathbb{E}[\beta_i^2] \, \mathbb{E}[(\Delta W_i)^2].
\]



Since

\[
\Delta W_i \sim \mathcal{N}(0, t_{i+1} - t_i),
\quad
\mathbb{E}[(\Delta W_i)^2] = t_{i+1} - t_i,
\]


we obtain


\[
\sum_{i=0}^{n-1} \mathbb{E}[\beta_i^2] \, (t_{i+1} - t_i).
\]



As the partition is refined, this Riemann sum converges to


\[
\mathbb{E}\left[ \int_0^T \beta^2(t)\, dt \right].
\]



---

## 5. The Itô Isometry

Putting everything together yields the **Itô isometry**:


\[
\boxed{
\mathbb{E}\left[ \left( \int_0^T \beta(t)\, dW_t \right)^2 \right]
= \mathbb{E}\left[ \int_0^T \beta^2(t)\, dt \right]
}
\]



This identity shows that the Itô integral preserves the \( L^2 \) norm:

- Square-integrable adapted processes on \( [0,T] \)
- Are mapped isometrically into \( L^2(\Omega) \)

---

## 6. Why This Result Is Intuitive but Nontrivial

- **Orthogonality**: Brownian increments have zero covariance on disjoint intervals.
- **Geometry**: The magnitude of a stochastic integral is measured by *variance*, not path length.
- **Conditional expectation**: The martingale property

  \[
  \mathbb{E}[\Delta W_i \mid \mathcal{F}_{t_i}] = 0
  \]


  is essential.

The Itô isometry is the stochastic analogue of **Parseval’s identity**: energy in equals energy out.

---

## 7. From Heuristics to a Rigorous Theory

To make the argument fully rigorous:

1. Define the Itô integral for **simple adapted processes**.
2. Prove the isometry directly for this class.
3. Extend the definition to general \( L^2 \)-adapted processes by density and completion.

This equips stochastic integration with a **Hilbert space structure**, forming the foundation of modern stochastic calculus.

---

## Summary

- The Itô isometry explains why stochastic integrals are well-defined in \( L^2 \).
- Cross terms vanish due to independence and conditional expectation.
- The identity reveals the geometric backbone of stochastic calculus.
- Nearly all structural results about Itô integrals trace back to this theorem.
