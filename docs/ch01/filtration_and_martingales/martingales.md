# Martingales and Submartingales

## The Fair Game Principle

The martingale concept originated in gambling theory, where it described a betting strategy in which the gambler doubled their stake after each loss. The modern mathematical usage, however, captures a far more general idea: a **fair game** in which, on average, one neither gains nor loses given current information.

This seemingly simple principle—that the best prediction of the future is the present—has profound consequences. Martingale theory provides the mathematical language for understanding:

- Why you cannot beat a fair casino in the long run
- How to price financial derivatives
- When iterative algorithms converge
- What makes certain stochastic processes "noise" rather than "signal"

---

## Conditional Expectation: The Foundation

Before defining martingales, we must understand conditional expectation, the fundamental tool for "averaging out the future."

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space, $\mathcal{G} \subseteq \mathcal{F}$ a sub-$\sigma$-algebra, and $X \in L^1(\Omega)$ an integrable random variable. The **conditional expectation** $\mathbb{E}[X \mid \mathcal{G}]$ is the unique (a.s.) $\mathcal{G}$-measurable random variable satisfying

$$
\int_G \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \int_G X \, d\mathbb{P} \quad \text{for all } G \in \mathcal{G}
$$

**Key properties**:

1. **Tower property**: If $\mathcal{H} \subseteq \mathcal{G} \subseteq \mathcal{F}$, then $\mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}] = \mathbb{E}[X \mid \mathcal{H}]$.

2. **Linearity**: $\mathbb{E}[aX + bY \mid \mathcal{G}] = a\mathbb{E}[X \mid \mathcal{G}] + b\mathbb{E}[Y \mid \mathcal{G}]$.

3. **Taking out what is known**: If $Y$ is $\mathcal{G}$-measurable and $XY \in L^1$, then $\mathbb{E}[XY \mid \mathcal{G}] = Y \cdot \mathbb{E}[X \mid \mathcal{G}]$.

4. **Independence**: If $X$ is independent of $\mathcal{G}$, then $\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]$.

5. **Jensen's inequality**: If $\varphi$ is convex and $\varphi(X) \in L^1$, then $\varphi(\mathbb{E}[X \mid \mathcal{G}]) \le \mathbb{E}[\varphi(X) \mid \mathcal{G}]$.

**Geometric interpretation**: $\mathbb{E}[X \mid \mathcal{G}]$ is the orthogonal projection of $X$ onto $L^2(\mathcal{G})$ (when $X \in L^2$). It is the best $\mathcal{G}$-measurable approximation to $X$ in the least-squares sense.

---

## Definition of Martingales

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space. An adapted process $M = \{M_t\}_{t \ge 0}$ is a **martingale** if:

1. **Integrability**: $\mathbb{E}|M_t| < \infty$ for all $t \ge 0$.

2. **Martingale property**: For all $0 \le s \le t$,

$$
\boxed{\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s \quad \text{a.s.}}
$$

**Interpretation**: Given all information up to time $s$, the best prediction of the future value $M_t$ is the current value $M_s$. The process has "no drift" on average.

**Equivalent formulation**: The martingale property is equivalent to

$$
\mathbb{E}[M_t - M_s \mid \mathcal{F}_s] = 0 \quad \text{for all } 0 \le s \le t
$$

The increments are **uncorrelated** with the past (though not necessarily independent).

---

## Sub- and Supermartingales

A process $X$ is a **submartingale** if

$$
\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s \quad \text{for all } 0 \le s \le t
$$

A process $X$ is a **supermartingale** if

$$
\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s \quad \text{for all } 0 \le s \le t
$$

**Mnemonic**: "Sub" suggests the process is below its expected value (tends to rise), "super" suggests it exceeds its expected value (tends to fall). This naming convention is counterintuitive but standard.

**Financial interpretation**:

- A **submartingale** represents an investment that drifts upward on average—like a savings account with positive interest.
- A **supermartingale** represents an investment that drifts downward—like a portfolio facing transaction costs.
- A **martingale** represents a fair gamble or a properly discounted asset price.

---

## Fundamental Examples

### Example 1: Brownian Motion

Let $W_t$ be standard Brownian motion with natural filtration $\mathcal{F}_t = \sigma(W_s : s \le t)$.

**Claim**: $W_t$ is a martingale.

**Proof**: For $0 \le s < t$,

$$
\mathbb{E}[W_t \mid \mathcal{F}_s] = \mathbb{E}[W_s + (W_t - W_s) \mid \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s] = W_s + 0 = W_s
$$

using that $W_s$ is $\mathcal{F}_s$-measurable and $W_t - W_s$ is independent of $\mathcal{F}_s$ with mean zero. $\square$

### Example 2: Compensated Squared Brownian Motion

**Claim**: $M_t = W_t^2 - t$ is a martingale.

**Proof**: We compute $\mathbb{E}[W_t^2 \mid \mathcal{F}_s]$. Writing $W_t = W_s + (W_t - W_s)$:

$$
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = \mathbb{E}[(W_s + (W_t - W_s))^2 \mid \mathcal{F}_s] = W_s^2 + 2W_s \cdot 0 + (t-s) = W_s^2 + (t-s)
$$

Therefore, $\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 + (t-s) - t = W_s^2 - s$. $\square$

**Insight**: $W_t^2$ grows on average at rate 1 (since $\mathbb{E}[W_t^2] = t$). Subtracting this deterministic drift $t$ yields a martingale.

### Example 3: Doob Martingale

For any $X \in L^1(\mathcal{F})$, the process

$$
M_t := \mathbb{E}[X \mid \mathcal{F}_t]
$$

is a martingale. This is the canonical construction: we reveal information about $X$ over time.

**Proof**: For $s \le t$, by the tower property:

$$
\mathbb{E}[M_t \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_t] \mid \mathcal{F}_s] = \mathbb{E}[X \mid \mathcal{F}_s] = M_s \quad \square
$$

### Example 4: Simple Random Walk

Let $\xi_1, \xi_2, \ldots$ be i.i.d. with $\mathbb{P}(\xi_i = +1) = \mathbb{P}(\xi_i = -1) = 1/2$. Define

$$
S_n = \sum_{k=1}^n \xi_k, \quad \mathcal{F}_n = \sigma(\xi_1, \ldots, \xi_n)
$$

Then $S_n$ is a martingale, modeling a fair coin-tossing game.

---

## Transforms and Creating Submartingales

Convex functions applied to martingales yield submartingales:

**Proposition (Jensen for Martingales)**: If $M_t$ is a martingale and $\varphi: \mathbb{R} \to \mathbb{R}$ is convex with $\mathbb{E}|\varphi(M_t)| < \infty$ for all $t$, then $\varphi(M_t)$ is a submartingale.

**Proof**: By Jensen's inequality,

$$
\mathbb{E}[\varphi(M_t) \mid \mathcal{F}_s] \ge \varphi(\mathbb{E}[M_t \mid \mathcal{F}_s]) = \varphi(M_s) \quad \square
$$

**Corollary**: If $M_t$ is a martingale, then:

- $|M_t|$ is a submartingale (using $\varphi(x) = |x|$).
- $M_t^2$ is a submartingale (using $\varphi(x) = x^2$).
- $(M_t)^+$ and $(M_t)^-$ are submartingales (using $\varphi(x) = \max(x, 0)$ and $\varphi(x) = \max(-x, 0)$).

---

## $L^p$ Martingales and Uniform Integrability

A martingale $M$ is called an **$L^p$-martingale** if $\sup_t \mathbb{E}|M_t|^p < \infty$.

A family of random variables $\{X_\alpha\}$ is **uniformly integrable** if

$$
\lim_{K \to \infty} \sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_{\{|X_\alpha| > K\}}] = 0
$$

**Key facts**:

1. Every $L^p$-bounded martingale with $p > 1$ is uniformly integrable.
2. An $L^1$-bounded martingale need not be uniformly integrable.
3. Uniform integrability is the key condition for martingale convergence in $L^1$ and for optional sampling.

---

## The Martingale Property and Itô Integrals

A deep connection links martingales to stochastic integration. If $H_t$ is a predictable process with $\mathbb{E}\int_0^T H_s^2 \, ds < \infty$, then the Itô integral

$$
I_t = \int_0^t H_s \, dW_s
$$

is a martingale. This is fundamental: Itô integrals are "pure noise" with no drift.

Conversely, the **martingale representation theorem** states that (under the Brownian filtration) every square-integrable martingale can be written as an Itô integral. This links the algebraic structure of martingales to the analytic structure of stochastic integration.

---

## Discrete vs. Continuous Time

While this chapter focuses on continuous-time processes, discrete-time martingales provide cleaner intuition:

| Property | Discrete Time | Continuous Time |
|----------|---------------|-----------------|
| Definition | $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = M_n$ | $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for all $s \le t$ |
| Path regularity | Automatic | Requires càdlàg version |
| Doob decomposition | Always exists | Requires class (D) for Doob–Meyer |
| Optional sampling | Bounded $\tau$ suffices | More delicate conditions |

Many results are first proved in discrete time and then extended to continuous time via approximation arguments or the general theory of processes.

---

## Why Martingales Matter

The martingale framework is central to modern probability and its applications:

1. **Financial mathematics**: The Fundamental Theorem of Asset Pricing states that a market is arbitrage-free if and only if discounted asset prices are martingales under some equivalent measure.

2. **Statistical inference**: Likelihood ratios form martingales, enabling sequential analysis and optimal stopping.

3. **Algorithm analysis**: Many iterative algorithms (stochastic gradient descent, Monte Carlo methods) involve martingale structures.

4. **Potential theory**: Harmonic functions are characterized by the mean-value property, which is precisely the martingale property for Brownian motion evaluated at exit times.

5. **Concentration inequalities**: Martingale techniques (Azuma–Hoeffding, Freedman) provide sharp tail bounds.

---

## Summary

| Concept | Definition | Intuition |
|---------|------------|-----------|
| Martingale | $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ | Fair game; no drift |
| Submartingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ | Favorable game; upward drift |
| Supermartingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s$ | Unfavorable game; downward drift |
| Doob martingale | $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$ | Gradual revelation of $X$ |
| Jensen's inequality | Convex of martingale is submartingale | Nonlinear transformations introduce drift |

The martingale property—the absence of predictable drift—is one of the most powerful structural assumptions in stochastic analysis. In the following sections, we explore the rich consequences: maximal inequalities, convergence theorems, stopping time analysis, and the Doob–Meyer decomposition.

---

## Exercises

### Exercise 1: Verifying Martingales

Determine whether each process is a martingale, submartingale, or supermartingale. Prove your answers.

(a) $M_t = W_t^2 - t$

(b) $M_t = e^{W_t}$

(c) $M_t = W_t^3 - 3tW_t$

(d) $M_t = \sin(W_t)$

(e) $M_t = W_t^4 - 6tW_t^2 + 3t^2$

### Exercise 2: The Doob Martingale

Let $X \in L^1(\mathcal{F})$ and define $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$.

(a) Prove that $(M_t)$ is a martingale using the tower property.

(b) Show that if $X = W_T$ for some $T > 0$, then $M_t = W_{t \wedge T}$.

(c) Find $M_t$ when $X = W_T^2$ for $t \le T$.

### Exercise 3: Transforms of Martingales

(a) Prove that if $M_t$ is a martingale and $\varphi$ is a convex function with $\mathbb{E}|\varphi(M_t)| < \infty$, then $\varphi(M_t)$ is a submartingale.

(b) Deduce that $|W_t|$, $W_t^2$, and $(W_t)^+$ are all submartingales.

(c) Is $\log(1 + W_t^2)$ a submartingale? Prove or disprove.

### Exercise 4: Discrete Martingales

Let $\xi_1, \xi_2, \ldots$ be i.i.d. with $\mathbb{P}(\xi_i = 1) = p$ and $\mathbb{P}(\xi_i = -1) = 1-p$.

(a) For what value of $p$ is $S_n = \sum_{k=1}^n \xi_k$ a martingale?

(b) For general $p$, find a function $f$ such that $f(S_n, n)$ is a martingale.

(c) Show that $M_n = \left(\frac{1-p}{p}\right)^{S_n}$ is a martingale when $p \neq 1/2$.