# Martingales and Submartingales

A **martingale** is the mathematical formalization of a *fair game*: given all past information, the expected future value equals the current value. The name originated with an 18th-century doubling-up betting strategy; the modern concept, due to Doob, is far more general and underlies the pricing of derivatives, the analysis of stochastic algorithms, and the characterization of stochastic noise.

---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space. An adapted process $M = (M_t)_{t \ge 0}$ is a **martingale** if:

1. **Integrability**: $\mathbb{E}|M_t| < \infty$ for all $t \ge 0$.
2. **Martingale property**: for all $0 \le s \le t$,

$$
\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s \quad \text{a.s.}
$$

Equivalently, $\mathbb{E}[M_t - M_s \mid \mathcal{F}_s] = 0$: increments are **uncorrelated with the past** (though not necessarily independent).

!!! info "Interpretation"
    Given the information $\mathcal{F}_s$ up to time $s$, the best prediction of $M_t$ is $M_s$. The process has no predictable drift.

---

## Sub- and Supermartingales

Relaxing the equality in the definition yields two generalizations:

- **Submartingale**: $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ — favorable game, upward drift.
- **Supermartingale**: $\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s$ — unfavorable game, downward drift.

The naming follows potential theory: *super*martingales dominate their futures on average (like superharmonic functions), while *sub*martingales are dominated by them.

---

## Fundamental Examples

!!! example "Brownian motion"
    Standard Brownian motion $W_t$ is a martingale under its natural filtration: using properties of conditional expectation (see [Conditional Expectation](conditional_expectation.md)), for $s \le t$,

    $$
    \mathbb{E}[W_t \mid \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s \mid \mathcal{F}_s] = W_s + 0 = W_s
    $$

    since $W_t - W_s$ is independent of $\mathcal{F}_s$ with mean zero. $\square$

!!! example "Compensated squared Brownian motion"
    $M_t = W_t^2 - t$ is a martingale. Writing $W_t = W_s + \Delta$ with $\Delta = W_t - W_s \perp \mathcal{F}_s$, the cross term vanishes and $\mathbb{E}[\Delta^2] = t-s$, giving $\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + (t-s)$. Subtracting $t$ makes this $W_s^2 - s$. $\square$

    *Insight*: $W_t^2$ grows on average at rate 1; subtracting $t$ removes this drift.

!!! example "Doob martingale"
    For any $X \in L^1(\mathcal{F})$, $M_t := \mathbb{E}[X \mid \mathcal{F}_t]$ is a martingale. By the tower property, for $s \le t$,

    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_t] \mid \mathcal{F}_s] = \mathbb{E}[X \mid \mathcal{F}_s] = M_s \quad \square
    $$

    This is the canonical construction: $X$ is revealed gradually as $t$ increases.

!!! example "Simple random walk"
    For i.i.d. $\xi_k$ with $\mathbb{P}(\xi_k = \pm 1) = 1/2$, the partial sum $S_n = \sum_{k=1}^n \xi_k$ is a martingale under $\mathcal{F}_n = \sigma(\xi_1, \ldots, \xi_n)$.

---

## Convex Functions Produce Submartingales

!!! abstract "Proposition"
    If $M$ is a martingale and $\varphi : \mathbb{R} \to \mathbb{R}$ is convex with $\mathbb{E}|\varphi(M_t)| < \infty$, then $\varphi(M)$ is a submartingale.

**Proof.** By conditional Jensen's inequality,

$$
\mathbb{E}[\varphi(M_t) \mid \mathcal{F}_s] \ge \varphi(\mathbb{E}[M_t \mid \mathcal{F}_s]) = \varphi(M_s) \quad \square
$$

Consequence: $|M_t|$, $M_t^2$, $(M_t)^+$, and $(M_t)^-$ are all submartingales when $M$ is a martingale. This fact drives Doob's maximal inequalities in the next section.

---

## $L^p$ Martingales and Uniform Integrability

A martingale $M$ is **$L^p$-bounded** if $\sup_t \mathbb{E}|M_t|^p < \infty$. A family $\{X_\alpha\}$ is **uniformly integrable** (UI) if

$$
\lim_{K \to \infty} \sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_{\{|X_\alpha| > K\}}] = 0
$$

**Key facts** (used later):

1. Every $L^p$-bounded martingale with $p > 1$ is UI.
2. $L^1$-boundedness alone does **not** imply UI.
3. UI is the hypothesis for $L^1$ martingale convergence and for optional sampling at unbounded stopping times.

These will be used in the sections on Doob convergence and optional sampling.

---

## Summary

| Concept | Definition |
|---|---|
| Martingale | $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ |
| Submartingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ |
| Supermartingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s$ |
| Doob martingale | $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$ |
| Convex transform | $\varphi(M)$ submartingale for $M$ martingale, $\varphi$ convex |

The martingale property — absence of predictable drift — is one of the most powerful structural assumptions in stochastic analysis. Subsequent sections develop the consequences: stopping times, optional sampling, Doob's maximal inequalities, martingale convergence, uniform integrability, and the Doob–Meyer decomposition.

---

## Exercises

**Exercise 1.** For standard Brownian motion $W$, classify each process as martingale, sub-, super-, or none.

(a) $W_t^2 - t$

(b) $e^{W_t}$

(c) $W_t^3 - 3tW_t$

(d) $W_t^4 - 6tW_t^2 + 3t^2$

??? success "Solution to Exercise 1"
    Let $\Delta = W_t - W_s \sim N(0, t-s)$, independent of $\mathcal{F}_s$, with moments $0, t-s, 0, 3(t-s)^2$.

    **(a) Martingale.** Shown in the main text: $\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 - s$.

    **(b) Strict submartingale.** $\mathbb{E}[e^{W_t} \mid \mathcal{F}_s] = e^{W_s}\mathbb{E}[e^{\Delta}] = e^{W_s + (t-s)/2} > e^{W_s}$.

    **(c) Martingale.** Expand $W_t^3 = W_s^3 + 3W_s^2\Delta + 3W_s\Delta^2 + \Delta^3$ and take conditional expectation: $\mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3(t-s)W_s$. Hence $\mathbb{E}[W_t^3 - 3tW_t \mid \mathcal{F}_s] = W_s^3 + 3(t-s)W_s - 3tW_s = W_s^3 - 3sW_s$.

    **(d) Martingale** (fourth Hermite polynomial). Expand $(W_s + \Delta)^4$ and use the moments of $\Delta$: $\mathbb{E}[W_t^4 \mid \mathcal{F}_s] = W_s^4 + 6W_s^2(t-s) + 3(t-s)^2$. Then $\mathbb{E}[W_t^4 - 6tW_t^2 + 3t^2 \mid \mathcal{F}_s] = W_s^4 + 6W_s^2(t-s) + 3(t-s)^2 - 6t(W_s^2 + (t-s)) + 3t^2 = W_s^4 - 6sW_s^2 + 3s^2$.

---

**Exercise 2.** Let $X \in L^1(\mathcal{F})$ and $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$.

(a) Prove $M$ is a martingale.

(b) Show that if $X = W_T$, then $M_t = W_{t \wedge T}$.

(c) For $X = W_T^2$ and $t \le T$, find $M_t$.

??? success "Solution to Exercise 2"
    **(a)** Tower property: $\mathbb{E}[M_t \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_t] \mid \mathcal{F}_s] = \mathbb{E}[X \mid \mathcal{F}_s] = M_s$ for $s \le t$. $\square$

    **(b)** For $t \le T$: $M_t = \mathbb{E}[W_T \mid \mathcal{F}_t] = W_t$ (Brownian martingale property). For $t \ge T$: $W_T$ is $\mathcal{F}_T \subseteq \mathcal{F}_t$-measurable, so $M_t = W_T$. Hence $M_t = W_{t \wedge T}$.

    **(c)** For $t \le T$: $\mathbb{E}[W_T^2 \mid \mathcal{F}_t] = W_t^2 + (T - t)$.

---

**Exercise 3.** Let $\xi_k$ be i.i.d. with $\mathbb{P}(\xi_k = 1) = p$, $\mathbb{P}(\xi_k = -1) = 1 - p$, and $S_n = \sum_{k=1}^n \xi_k$.

(a) For what $p$ is $S_n$ a martingale?

(b) For general $p$, find $f$ such that $S_n - n f(p)$ is a martingale.

(c) Show $M_n = \left(\frac{1-p}{p}\right)^{S_n}$ is a martingale for any $p \in (0,1)$.

??? success "Solution to Exercise 3"
    **(a)** $\mathbb{E}[\xi_k] = 2p - 1 = 0 \Leftrightarrow p = 1/2$.

    **(b)** With $\mu = 2p - 1$, $\mathbb{E}[S_{n+1} - S_n \mid \mathcal{F}_n] = \mu$, so $S_n - n\mu$ has zero drift. Hence $f(p) = 2p - 1$.

    **(c)** Let $r = (1-p)/p$. Independence of $\xi_{n+1}$ from $\mathcal{F}_n$ and "taking out what is known" give

    $$
    \mathbb{E}[r^{S_{n+1}} \mid \mathcal{F}_n] = r^{S_n} \mathbb{E}[r^{\xi_{n+1}}] = r^{S_n} \bigl(p \cdot r + (1-p) \cdot r^{-1}\bigr) = r^{S_n} \bigl((1-p) + p\bigr) = r^{S_n}
    $$

    So $M_n$ is a martingale. $\square$

---

**Exercise 4.** Prove: if $M$ is a martingale and $\varphi$ is convex with $\mathbb{E}|\varphi(M_t)| < \infty$, then $\varphi(M)$ is a submartingale. Deduce that $|W_t|$, $W_t^2$, and $(W_t)^+$ are submartingales.

??? success "Solution to Exercise 4"
    By conditional Jensen's inequality: $\mathbb{E}[\varphi(M_t) \mid \mathcal{F}_s] \ge \varphi(\mathbb{E}[M_t \mid \mathcal{F}_s]) = \varphi(M_s)$. Adaptedness and integrability hold by hypothesis. $\square$

    Apply with $\varphi(x) = |x|$, $x^2$, $x^+ = \max(x,0)$ respectively (all convex).

---

**Exercise 5.** Let $M$ be a martingale on $[0, T]$ with $\mathbb{E}[M_T^2] < \infty$. Show that $\mathbb{E}[(M_t - M_s)^2] = \mathbb{E}[M_t^2] - \mathbb{E}[M_s^2]$ for $s \le t$, and that $t \mapsto \mathbb{E}[M_t^2]$ is nondecreasing.

??? success "Solution to Exercise 5"
    Expand $(M_t - M_s)^2 = M_t^2 - 2M_s M_t + M_s^2$. Take expectations, and condition the middle term on $\mathcal{F}_s$: $\mathbb{E}[M_s M_t] = \mathbb{E}[M_s \mathbb{E}[M_t \mid \mathcal{F}_s]] = \mathbb{E}[M_s^2]$ by the martingale property. Hence

    $$
    \mathbb{E}[(M_t - M_s)^2] = \mathbb{E}[M_t^2] - 2\mathbb{E}[M_s^2] + \mathbb{E}[M_s^2] = \mathbb{E}[M_t^2] - \mathbb{E}[M_s^2]
    $$

    The LHS is $\ge 0$, so $\mathbb{E}[M_s^2] \le \mathbb{E}[M_t^2]$. $\square$

    *Remark*: this says martingale increments are orthogonal in $L^2$, and $t \mapsto \mathbb{E}[M_t^2]$ plays the role of "accumulated variance" — foreshadowing the quadratic variation $\langle M \rangle_t$ of the Doob–Meyer decomposition.
