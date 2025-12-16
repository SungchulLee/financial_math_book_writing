

# 1. Motivation: What Is Brownian Motion?

Brownian motion is the **canonical continuous-time random motion** that satisfies:

* Randomness at every scale
* Continuity of paths
* Infinite variation
* Gaussian, independent increments

It is the **only** process that is simultaneously:

1. Continuous
2. Markov
3. Has stationary independent increments
4. Has Gaussian increments

---

# 2. Definition (Wiener Process)

A **standard Brownian motion** \(\{W_t\}_{t \ge 0}\) on a probability space
\((\Omega,\mathcal{F},\mathbb{P})\) is a stochastic process satisfying:

### (i) Initial condition

\[
W_0 = 0 \quad \text{almost surely}
\]

### (ii) Independent increments

For
\(
0 \le t_0 < t_1 < \cdots < t_n,
\)
the increments
\(
W_{t_1}-W_{t_0},\ldots,W_{t_n}-W_{t_{n-1}}
\)
are independent.

### (iii) Stationary increments

\[
W_t - W_s \sim \mathcal{N}(0,t-s), \quad 0 \le s < t
\]

### (iv) Continuity of paths

\[
t \mapsto W_t(\omega) \quad \text{is continuous for almost every } \omega
\]

---

# 3. Finite-Dimensional Distributions

For any \(0 \le t_1 < \cdots < t_n\),

\[
(W_{t_1},\ldots,W_{t_n})
\sim
\mathcal{N}(0,\Sigma)
\]

where

\[
\Sigma_{ij} = \min(t_i,t_j)
\]

In particular,

\[
\mathbb{E}[W_t] = 0, \quad \mathbb{E}[W_t^2] = t
\]

---

# 4. Characteristic Function

For \(0 \le s < t\),

\[
\boxed{
\mathbb{E}\left[e^{i\lambda(W_t-W_s)}\right]
=
\exp\left(-\frac{1}{2}\lambda^2(t-s)\right)
}
\]

This uniquely characterizes the Gaussian increment structure.

---

# 5. Covariance Structure

For all \(s,t \ge 0\),

\[
\boxed{
\mathbb{E}[W_s W_t] = \min(s,t)
}
\]

This identity implies:

* Non-differentiability
* Long-range correlation structure
* Self-similarity

---

# 6. Construction via Kolmogorov Extension Theorem

Define finite-dimensional distributions by:

\[
(W_{t_1},\ldots,W_{t_n})
\sim
\mathcal{N}(0,\Sigma),
\quad
\Sigma_{ij} = \min(t_i,t_j)
\]

These distributions are:

* Consistent
* Positive definite

By the **Kolmogorov extension theorem**, there exists a stochastic process with these distributions.

Continuity is then guaranteed by **Kolmogorov’s continuity theorem**.

---

# 7. Scaling Property (Self-Similarity)

For any \(c > 0,\ t \ge 0\),

\[
\boxed{
W_{ct} \overset{d}{=} 
\sqrt{c}\ W_t
}
\]

This implies Brownian motion has **no intrinsic time scale**.

---

# 8. Nowhere Differentiability

Almost surely,

\[
\boxed{
\limsup_{h \to 0}
\frac{|W_{t+h}-W_t|}{|h|}
=
\infty
}
\]

More precisely, Brownian paths are:

* Continuous
* Nowhere differentiable
* Of infinite total variation

Yet:

\[
\mathbb{E}\left[(W_{t+h}-W_t)^2\right] = h
\]

---

# 9. Quadratic Variation

For any partition

\[
\Pi_n = {0 = t_0 < t_1 < \cdots < t_n = t}
\]

with mesh \(|\Pi_n| \to 0\),

\[
\boxed{
\sum_{k=1}^n (W_{t_k}-W_{t_{k-1}})^2
\ \xrightarrow{\mathbb{P}}\ 
t
}
\]

This property **distinguishes Brownian motion** from smooth functions.

---

# 10. Martingale Property

Brownian motion is a martingale:

\[
\boxed{
\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s,
\quad s \le t
}
\]

and

\[
W_t^2 - t
\]

is also a martingale.

---

# 11. Strong Markov Property

For any stopping time \(\tau\) 뭉 $t \ge 0$,

\[
\boxed{
W_{\tau+t} - W_\tau
\text{ is independent of }\mathcal{F}_\tau
}
\]

and has the same law as Brownian motion.

---

# 12. Connection to the Heat Equation

Define

\[
u(x,t) = \mathbb{E}[f(x+W_t)]
\]

Then \(u\) satisfies:

\[
\boxed{
\frac{\partial u}{\partial t}
=
\frac{1}{2}
\frac{\partial^2 u}{\partial x^2}
}
\]

This is the **analytic shadow** of Brownian motion.

---

# 13. First Passage Times

Define the hitting time:

\[
\tau_a = \inf{t \ge 0 : W_t = a}
\]

Then:

\[
\mathbb{P}(\tau_a < \infty) = 1
\quad \text{for all } a \in \mathbb{R}
\]

But:

\[
\mathbb{E}[\tau_a] = \infty
\]



