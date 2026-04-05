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

Martingales are defined in terms of conditional expectation. The full treatment — Radon–Nikodym definition, geometric interpretation as $L^2$ projection, and all key properties — appears in the companion document *Conditional Expectation*. We recall only the essentials here.

For a sub-$\sigma$-algebra $\mathcal{G} \subseteq \mathcal{F}$ and $X \in L^1$, the **conditional expectation** $\mathbb{E}[X \mid \mathcal{G}]$ is the unique $\mathcal{G}$-measurable random variable satisfying $\int_G \mathbb{E}[X|\mathcal{G}]\,d\mathbb{P} = \int_G X\,d\mathbb{P}$ for all $G \in \mathcal{G}$. The properties used most in this chapter are:

1. **Tower property**: $\mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}] = \mathbb{E}[X \mid \mathcal{H}]$ when $\mathcal{H} \subseteq \mathcal{G}$.
2. **Linearity**: $\mathbb{E}[aX + bY \mid \mathcal{G}] = a\mathbb{E}[X \mid \mathcal{G}] + b\mathbb{E}[Y \mid \mathcal{G}]$.
3. **Taking out what is known**: $\mathbb{E}[XY \mid \mathcal{G}] = Y\,\mathbb{E}[X \mid \mathcal{G}]$ when $Y$ is $\mathcal{G}$-measurable.
4. **Independence**: $\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]$ when $X \perp \mathcal{G}$.
5. **Jensen's inequality**: $\varphi(\mathbb{E}[X|\mathcal{G}]) \le \mathbb{E}[\varphi(X)|\mathcal{G}]$ for convex $\varphi$.

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

Martingales model fair games. Relaxing the equality to an inequality yields two important generalizations, treated in full in the companion document *Sub- and Supermartingales*:

A process $X$ is a **submartingale** if $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ and a **supermartingale** if $\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s$ for all $0 \le s \le t$.

**Key examples**: Brownian motion with positive drift is a submartingale; a portfolio with transaction costs is a supermartingale; a convex function of a martingale is a submartingale (by conditional Jensen's inequality).

The naming follows the potential-theoretic convention: *super*martingales have current values that dominate their futures (like superharmonic functions), while *sub*martingales have expected futures that exceed the present.

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
\begin{aligned}
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] &= \mathbb{E}[(W_s + (W_t - W_s))^2 \mid \mathcal{F}_s] \\
&= \mathbb{E}[W_s^2 + 2W_s(W_t - W_s) + (W_t - W_s)^2 \mid \mathcal{F}_s] \\
&= W_s^2 + 2W_s \cdot \mathbb{E}[W_t - W_s \mid \mathcal{F}_s] + \mathbb{E}[(W_t - W_s)^2 \mid \mathcal{F}_s]
\end{aligned}
$$

Now, $W_t - W_s$ is independent of $\mathcal{F}_s$, so:

- $\mathbb{E}[W_t - W_s \mid \mathcal{F}_s] = \mathbb{E}[W_t - W_s] = 0$
- $\mathbb{E}[(W_t - W_s)^2 \mid \mathcal{F}_s] = \mathbb{E}[(W_t - W_s)^2] = \text{Var}(W_t - W_s) = t - s$

Therefore:

$$
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + 0 + (t-s) = W_s^2 + (t-s)
$$

Hence $\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 + (t-s) - t = W_s^2 - s$. $\square$

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

## L^p Martingales and Uniform Integrability

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

## The Itô Integral and Martingales

A deep connection links martingales to stochastic integration, developed fully in the chapters on Itô calculus: if $H_t$ is a suitable predictable process, the Itô integral $\int_0^t H_s \, dW_s$ is a martingale. Conversely, the **martingale representation theorem** states that every square-integrable Brownian martingale can be written as an Itô integral. These connections are explored in *Brownian Motion Martingales*, *Itô Integration*, and the Martingale Representation Theorem.

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

Determine whether each process is a martingale, submartingale, supermartingale, or none of these. Prove your answers.

(a) $M_t = W_t^2 - t$

(b) $M_t = e^{W_t}$

(c) $M_t = W_t^3 - 3tW_t$

(d) $M_t = \sin(W_t)$ *(Hint: Apply Itô's formula and examine the drift.)*

(e) $M_t = W_t^4 - 6tW_t^2 + 3t^2$

??? success "Solution to Exercise 1"
    **(a)** $M_t = W_t^2 - t$ is a **martingale**. This was proved in the text: $\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + (t - s)$, so $\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 - s$.

    **(b)** $M_t = e^{W_t}$ is a **submartingale** (and not a martingale or supermartingale). Since $\varphi(x) = e^x$ is convex and $W_t$ is a martingale, Jensen's inequality gives:

    $$
    \mathbb{E}[e^{W_t} \mid \mathcal{F}_s] \ge e^{\mathbb{E}[W_t \mid \mathcal{F}_s]} = e^{W_s}
    $$

    Direct computation confirms: $\mathbb{E}[e^{W_t} \mid \mathcal{F}_s] = e^{W_s} \cdot \mathbb{E}[e^{W_t - W_s}] = e^{W_s} \cdot e^{(t-s)/2} = e^{W_s + (t-s)/2} > e^{W_s}$ for $t > s$. Since the inequality is strict, $e^{W_t}$ is a strict submartingale (not a martingale).

    **(c)** $M_t = W_t^3 - 3tW_t$ is a **martingale**. Expanding $(W_s + \Delta)^3$ where $\Delta = W_t - W_s$:

    $$
    \mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3W_s(t-s)
    $$

    Also $\mathbb{E}[3tW_t \mid \mathcal{F}_s] = 3tW_s$. Therefore:

    $$
    \mathbb{E}[W_t^3 - 3tW_t \mid \mathcal{F}_s] = W_s^3 + 3W_s(t-s) - 3tW_s = W_s^3 - 3sW_s
    $$

    **(d)** $M_t = \sin(W_t)$ is a **supermartingale**. By Ito's formula:

    $$
    d\sin(W_t) = \cos(W_t)\,dW_t - \frac{1}{2}\sin(W_t)\,dt
    $$

    The drift is $-\frac{1}{2}\sin(W_t)$. Since the drift is not identically zero (and has no definite sign), $\sin(W_t)$ is neither a martingale nor purely a sub/supermartingale in general.

    More precisely: $\mathbb{E}[\sin(W_t)] = e^{-t/2}\sin(0) = 0$ (using the formula $\mathbb{E}[\sin(\theta W_t)] = e^{-\theta^2 t/2}\sin(0)$... actually $\mathbb{E}[\sin(W_t)] = \text{Im}(\mathbb{E}[e^{iW_t}]) = \text{Im}(e^{-t/2}) = 0$).

    Since $\mathbb{E}[\sin(W_t) \mid \mathcal{F}_s] = e^{-(t-s)/2}\sin(W_s)$ (which can be verified by writing $\sin(W_t) = \text{Im}(e^{iW_t})$ and computing the conditional expectation of the exponential), and $e^{-(t-s)/2} \le 1$ with $|\sin(W_s)| \le 1$, the conditional expectation has the same sign as $\sin(W_s)$ but smaller magnitude. Thus $\sin(W_t)$ is **neither** a submartingale nor a supermartingale (since $e^{-(t-s)/2}\sin(W_s) \le \sin(W_s)$ when $\sin(W_s) \ge 0$ and $e^{-(t-s)/2}\sin(W_s) \ge \sin(W_s)$ when $\sin(W_s) \le 0$). It is **none of the above**.

    **(e)** $M_t = W_t^4 - 6tW_t^2 + 3t^2$ is a **martingale**. This is the fourth Hermite polynomial martingale $H_4(W_t, t)$. One can verify directly by expanding $(W_s + \Delta)^4$ and computing the conditional expectation, using $\mathbb{E}[\Delta] = 0$, $\mathbb{E}[\Delta^2] = t-s$, $\mathbb{E}[\Delta^3] = 0$, $\mathbb{E}[\Delta^4] = 3(t-s)^2$.

---

### Exercise 2: The Doob Martingale

Let $X \in L^1(\mathcal{F})$ and define $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$.

(a) Prove that $(M_t)$ is a martingale using the tower property.

(b) Show that if $X = W_T$ for some $T > 0$, then $M_t = W_{t \wedge T}$.

(c) Find $M_t$ when $X = W_T^2$ for $t \le T$.

??? success "Solution to Exercise 2"
    **(a)** For $s \le t$, by the tower property:

    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_t] \mid \mathcal{F}_s] = \mathbb{E}[X \mid \mathcal{F}_s] = M_s
    $$

    The second equality uses the tower property (since $\mathcal{F}_s \subseteq \mathcal{F}_t$). $\square$

    **(b)** For $t \le T$: $M_t = \mathbb{E}[W_T \mid \mathcal{F}_t] = W_t$ (by the martingale property of Brownian motion). For $t > T$: $M_t = \mathbb{E}[W_T \mid \mathcal{F}_t] = W_T$ (since $W_T$ is $\mathcal{F}_T \subseteq \mathcal{F}_t$-measurable).

    Therefore $M_t = W_{t \wedge T}$ for all $t \ge 0$.

    **(c)** For $t \le T$:

    $$
    M_t = \mathbb{E}[W_T^2 \mid \mathcal{F}_t]
    $$

    Write $W_T = W_t + (W_T - W_t)$, so $W_T^2 = W_t^2 + 2W_t(W_T - W_t) + (W_T - W_t)^2$.

    $$
    \mathbb{E}[W_T^2 \mid \mathcal{F}_t] = W_t^2 + 2W_t \cdot 0 + (T - t) = W_t^2 + (T - t)
    $$

    Therefore $M_t = W_t^2 + T - t$ for $t \le T$.

---

### Exercise 3: Transforms of Martingales

(a) Prove that if $M_t$ is a martingale and $\varphi$ is a convex function with $\mathbb{E}|\varphi(M_t)| < \infty$, then $\varphi(M_t)$ is a submartingale.

(b) Deduce that $|W_t|$, $W_t^2$, and $(W_t)^+$ are all submartingales.

(c) Is $\log(1 + W_t^2)$ a submartingale? Prove or disprove.

??? success "Solution to Exercise 3"
    **(a)** By conditional Jensen's inequality with convex $\varphi$:

    $$
    \mathbb{E}[\varphi(M_t) \mid \mathcal{F}_s] \ge \varphi(\mathbb{E}[M_t \mid \mathcal{F}_s]) = \varphi(M_s)
    $$

    The last equality uses the martingale property $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$. Since $\varphi(M_t)$ is adapted and integrable (by hypothesis), it is a submartingale. $\square$

    **(b)** Apply part (a):

    - $|W_t|$: Use $\varphi(x) = |x|$ (convex). Then $|W_t|$ is a submartingale.
    - $W_t^2$: Use $\varphi(x) = x^2$ (convex). Then $W_t^2$ is a submartingale.
    - $(W_t)^+ = \max(W_t, 0)$: Use $\varphi(x) = \max(x, 0)$ (convex). Then $(W_t)^+$ is a submartingale.

    **(c)** The function $\varphi(x) = \log(1 + x^2)$ is **not** convex on all of $\mathbb{R}$ (its second derivative is $\varphi''(x) = \frac{2(1 + x^2) - 4x^2}{(1 + x^2)^2} = \frac{2 - 2x^2}{(1 + x^2)^2}$, which is negative for $|x| > 1$). So we cannot directly apply Jensen's inequality.

    However, $\log(1 + W_t^2)$ is still a submartingale. To see this, since $W_t^2$ is a submartingale and $x \mapsto \log(1 + x)$ is concave and increasing on $[0, \infty)$, one might think this gives a supermartingale. But a direct computation using Ito's formula yields:

    $$
    d\log(1 + W_t^2) = \frac{2W_t}{1 + W_t^2}\,dW_t + \frac{1 + W_t^2 - 2W_t^2}{(1 + W_t^2)^2}\,dt = \frac{2W_t}{1 + W_t^2}\,dW_t + \frac{1 - W_t^2}{(1 + W_t^2)^2}\,dt
    $$

    The drift $\frac{1 - W_t^2}{(1 + W_t^2)^2}$ changes sign, so $\log(1 + W_t^2)$ is **neither** a submartingale nor a supermartingale in general.

---

### Exercise 4: Discrete Martingales

Let $\xi_1, \xi_2, \ldots$ be i.i.d. with $\mathbb{P}(\xi_i = 1) = p$ and $\mathbb{P}(\xi_i = -1) = 1-p$.

(a) For what value of $p$ is $S_n = \sum_{k=1}^n \xi_k$ a martingale?

(b) For general $p \in (0,1)$, find a function $f$ such that $f(S_n, n)$ is a martingale.

(c) Show that $M_n = \left(\frac{1-p}{p}\right)^{S_n}$ is a martingale when $p \neq 1/2$. *(Note: This also holds trivially when $p = 1/2$ since the ratio equals 1.)*

??? success "Solution to Exercise 4"
    **(a)** $S_n$ is a martingale when $\mathbb{E}[\xi_i] = 0$, i.e., $p \cdot 1 + (1-p) \cdot (-1) = 2p - 1 = 0$, so $p = 1/2$.

    **(b)** We seek $f$ such that $f(S_n, n)$ is a martingale. Since $\mathbb{E}[S_{n+1} \mid \mathcal{F}_n] = S_n + (2p - 1)$, the process has drift $\mu = 2p - 1$ per step.

    Define $f(x, n) = x - n\mu = x - n(2p - 1)$. Then $f(S_n, n) = S_n - n(2p-1)$ and:

    $$
    \mathbb{E}[f(S_{n+1}, n+1) \mid \mathcal{F}_n] = \mathbb{E}[S_{n+1} \mid \mathcal{F}_n] - (n+1)(2p-1)
    $$

    $$
    = S_n + (2p-1) - (n+1)(2p-1) = S_n - n(2p-1) = f(S_n, n)
    $$

    So $S_n - n(2p - 1)$ is a martingale.

    **(c)** Let $r = \frac{1-p}{p}$ and $M_n = r^{S_n}$. We verify:

    $$
    \mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = \mathbb{E}[r^{S_n + \xi_{n+1}} \mid \mathcal{F}_n] = r^{S_n} \cdot \mathbb{E}[r^{\xi_{n+1}}]
    $$

    since $\xi_{n+1}$ is independent of $\mathcal{F}_n$. Now:

    $$
    \mathbb{E}[r^{\xi_{n+1}}] = p \cdot r^1 + (1-p) \cdot r^{-1} = p \cdot \frac{1-p}{p} + (1-p) \cdot \frac{p}{1-p} = (1-p) + p = 1
    $$

    Therefore $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = r^{S_n} = M_n$, so $M_n$ is a martingale. $\square$
