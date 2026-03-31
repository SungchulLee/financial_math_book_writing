# Doob's Maximal Inequality

## Why Maximum Control Matters

In probability theory, we often need to control not just the value of a stochastic process at a single time, but its **extremal behavior** over an entire interval. Questions like:

- How large can a martingale get before time $T$?
- What is the probability that a random walk ever exceeds level $a$?
- How do we bound the fluctuations of a stochastic integral?

All require understanding the **running maximum** $M_t^* = \sup_{0 \le s \le t} |M_s|$.

The challenge is clear: while $\mathbb{E}[M_t]$ might be controlled, the maximum could be much larger. Doob's inequalities provide the remarkable result that for martingales, the maximum is controlled by the terminal value—with explicit constants.

---

## The Maximal Process

For a stochastic process $X = \{X_t\}_{t \ge 0}$, define:

$$
X_t^* := \sup_{0 \le s \le t} X_s \quad \text{(running maximum)}
$$

$$
|X|_t^* := \sup_{0 \le s \le t} |X_s| \quad \text{(running absolute maximum)}
$$

These are increasing processes. The key question: how do we relate $\mathbb{E}[(X_t^*)^p]$ to $\mathbb{E}[|X_t|^p]$?

For general processes, there is no control: the maximum could be arbitrarily larger than any single value. But martingales are special.

---

## Doob's L^p Maximal Inequality

**Theorem (Doob's $L^p$ Maximal Inequality)**: Let $\{M_t\}_{0 \le t \le T}$ be a right-continuous martingale (or nonnegative submartingale). Then for $p > 1$:

$$
\boxed{\left\| M_T^* \right\|_{L^p} \le \frac{p}{p-1} \|M_T\|_{L^p}}
$$

Equivalently:

$$
\mathbb{E}\left[\sup_{0 \le t \le T} |M_t|^p\right] \le \left(\frac{p}{p-1}\right)^p \mathbb{E}[|M_T|^p]
$$

**The constant**: The factor $\frac{p}{p-1}$ is sharp—it cannot be improved in general. As $p \to 1^+$, the constant blows up, reflecting that the $L^1$ case requires different treatment.

| $p$ | $\frac{p}{p-1}$ | $\left(\frac{p}{p-1}\right)^p$ |
|-----|-----------------|-------------------------------|
| 2 | 2 | 4 |
| 3 | 1.5 | 3.375 |
| 4 | 1.33 | 3.16 |
| $\infty$ | 1 | 1 |

---

## Proof Strategy

The proof proceeds in two steps:

### Step 1: Doob's L¹ Maximal Inequality (Weak Form)

**Lemma**: For a nonnegative submartingale $\{X_t\}$ and any $\lambda > 0$:

$$
\boxed{\lambda \cdot \mathbb{P}(X_T^* \ge \lambda) \le \mathbb{E}[X_T \mathbf{1}_{\{X_T^* \ge \lambda\}}]}
$$

**Proof**: Define the stopping time $\tau = \inf\{t \ge 0 : X_t \ge \lambda\} \wedge T$. On the event $\{X_T^* \ge \lambda\}$, we have $X_\tau \ge \lambda$.

By the optional sampling theorem for submartingales (with bounded stopping times):

$$
\mathbb{E}[X_T \mid \mathcal{F}_\tau] \ge X_\tau
$$

Taking expectations and using $X_\tau \ge \lambda$ on $\{X_T^* \ge \lambda\}$:

$$
\mathbb{E}[X_T \mathbf{1}_{\{X_T^* \ge \lambda\}}] \ge \mathbb{E}[X_\tau \mathbf{1}_{\{X_T^* \ge \lambda\}}] \ge \lambda \cdot \mathbb{P}(X_T^* \ge \lambda) \quad \square
$$

### Step 2: From Weak L¹ to Strong L^p

Using the layer cake formula and the weak inequality:

$$
\mathbb{E}[(X_T^*)^p] = p \int_0^\infty \lambda^{p-1} \mathbb{P}(X_T^* \ge \lambda) \, d\lambda \le p \int_0^\infty \lambda^{p-2} \mathbb{E}[X_T \mathbf{1}_{\{X_T^* \ge \lambda\}}] \, d\lambda
$$

Applying Fubini's theorem and integrating:

$$
= p \mathbb{E}\left[X_T \int_0^{X_T^*} \lambda^{p-2} \, d\lambda\right] = \frac{p}{p-1} \mathbb{E}[X_T (X_T^*)^{p-1}]
$$

By Hölder's inequality with exponents $p$ and $\frac{p}{p-1}$:

$$
\mathbb{E}[X_T (X_T^*)^{p-1}] \le \|X_T\|_{L^p} \cdot \|(X_T^*)^{p-1}\|_{L^{p/(p-1)}} = \|X_T\|_{L^p} \cdot \|X_T^*\|_{L^p}^{p-1}
$$

Combining:

$$
\|X_T^*\|_{L^p}^p \le \frac{p}{p-1} \|X_T\|_{L^p} \cdot \|X_T^*\|_{L^p}^{p-1}
$$

Dividing by $\|X_T^*\|_{L^p}^{p-1}$ (assuming it's positive):

$$
\|X_T^*\|_{L^p} \le \frac{p}{p-1} \|X_T\|_{L^p} \quad \square
$$

---

## Doob's $L^1$ Results

The case $p = 1$ requires separate treatment since $\frac{p}{p-1} \to \infty$ as $p \to 1$.

### Weak $L^1$ Inequality (already proved above)

The first result is the weak $L^1$ bound already established in the proof:

$$
\boxed{\lambda \cdot \mathbb{P}(X_T^* \ge \lambda) \le \mathbb{E}[X_T \cdot \mathbf{1}_{\{X_T^* \ge \lambda\}}] \le \mathbb{E}[X_T]}
$$

This yields the tail bound $\mathbb{P}(M_T^* \ge \lambda) \le \frac{\mathbb{E}[|M_T|]}{\lambda}$ for martingales (by applying to $|M_t|$, which is a submartingale). Note: this follows from Doob's weak inequality, not directly from Markov's inequality.

### Strong $L^1$ Inequality (Orlicz space bound)

For a *strong* bound on $\mathbb{E}[M_T^*]$ itself, one needs more than $L^1$ integrability of $M_T$. The sharp result involves the $L \log L$ Orlicz space:

**Theorem**: For a martingale $\{M_t\}$ with $M_T \in L \log L$ (i.e., $\mathbb{E}[|M_T| \log^+ |M_T|] < \infty$):

$$
\mathbb{E}[M_T^*] \le \frac{e}{e-1}\left(\mathbb{E}[|M_T| \log^+ |M_T|] + 1\right)
$$

where $\log^+ x = \max(\log x, 0)$. This bound is sharp. The constant $e/(e-1)$ arises naturally when optimizing the layer-cake integral using the inequality $\log^+ x \le x/e$ at the critical point $x = e$. If $M_T \in L^1 \setminus L\log L$, then $M_T^*$ need not be integrable.

---

## Application: Brownian Motion

**Example**: For Brownian motion $W_t$ on $[0, T]$:

$$
\mathbb{E}\left[\sup_{0 \le t \le T} |W_t|^2\right] \le 4 \mathbb{E}[W_T^2] = 4T
$$

More precisely, using $p = 2$ in Doob's inequality:

$$
\left\|\sup_{0 \le t \le T} |W_t|\right\|_{L^2} \le 2 \|W_T\|_{L^2} = 2\sqrt{T}
$$

**Tail bound**: For any $a > 0$:

$$
\mathbb{P}\left(\sup_{0 \le t \le T} W_t \ge a\right) \le \frac{\mathbb{E}[W_T^+ \mathbf{1}_{\{W_T^* \ge a\}}]}{a}
$$

Using the reflection principle (which gives the exact distribution), one can show:

$$
\mathbb{P}\left(\sup_{0 \le t \le T} W_t \ge a\right) = 2\mathbb{P}(W_T \ge a) = 2\Phi\left(-\frac{a}{\sqrt{T}}\right)
$$

where $\Phi$ is the standard normal CDF. Doob's inequality provides a general upper bound; the reflection principle gives the exact answer for Brownian motion.

---

## The Burkholder-Davis-Gundy Inequality

Doob's inequality bounds the maximum in terms of the terminal value. The **Burkholder-Davis-Gundy (BDG) inequality** bounds it in terms of the **quadratic variation**.

**Theorem (BDG)**: For any continuous local martingale $M$ with $M_0 = 0$ and $p > 0$, there exist universal constants $c_p, C_p$ such that:

$$
\boxed{c_p \mathbb{E}[[M]_T^{p/2}] \le \mathbb{E}[(M_T^*)^p] \le C_p \mathbb{E}[[M]_T^{p/2}]}
$$

where $[M]_T$ is the quadratic variation.

For $p = 2$, the constants are $c_2 = 1$ and $C_2 = 4$:

$$
\mathbb{E}[[M]_T] \le \mathbb{E}[(M_T^*)^2] \le 4\mathbb{E}[[M]_T]
$$

**Application to Itô integrals**: If $I_t = \int_0^t H_s \, dW_s$, then $[I]_t = \int_0^t H_s^2 \, ds$, giving:

$$
\mathbb{E}\left[\sup_{0 \le t \le T} \left|\int_0^t H_s \, dW_s\right|^2\right] \le 4\mathbb{E}\left[\int_0^T H_s^2 \, ds\right]
$$

---

## Applications in Stochastic Analysis

### 1. Existence and Uniqueness of SDEs

In proving existence of solutions to stochastic differential equations, one uses Doob's inequality to control the maximum of Picard iterations:

$$
\mathbb{E}\left[\sup_{0 \le t \le T} |X_t^{(n+1)} - X_t^{(n)}|^2\right] \le C \cdot \mathbb{E}\left[\int_0^T |X_s^{(n)} - X_s^{(n-1)}|^2 \, ds\right]
$$

This leads to Gronwall-type arguments establishing convergence.

### 2. Convergence of Martingales

Doob's inequality implies that $L^p$-bounded martingales with $p > 1$ converge almost surely. If $\sup_n \mathbb{E}[|M_n|^p] < \infty$, then:

$$
\mathbb{E}\left[\sup_n |M_n|^p\right] \le \left(\frac{p}{p-1}\right)^p \sup_n \mathbb{E}[|M_n|^p] < \infty
$$

By the monotone convergence theorem for the supremum, $M_n$ converges a.s.

### 3. Concentration Inequalities

Doob's inequality underpins many concentration results. Combined with the exponential martingale:

$$
Z_t = \exp\left(\theta M_t - \frac{\theta^2}{2}[M]_t\right)
$$

one obtains exponential tail bounds for martingales.

---

## Discrete-Time Version

For discrete-time martingales $(M_n)_{n=0}^N$, Doob's inequality takes the form:

$$
\mathbb{E}\left[\max_{0 \le n \le N} |M_n|^p\right] \le \left(\frac{p}{p-1}\right)^p \mathbb{E}[|M_N|^p]
$$

The proof is essentially identical, using the optional sampling theorem for bounded stopping times.

---

## Comparison with Other Inequalities

| Inequality | Statement | Application |
|------------|-----------|-------------|
| Markov | $\mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ | Basic tail bound |
| Chebyshev | $\mathbb{P}(\|X - \mu\| \ge a) \le \frac{\text{Var}(X)}{a^2}$ | Variance-based bound |
| Doob's $L^p$ | $\|M^*\|_p \le \frac{p}{p-1}\|M_T\|_p$ | Maximum control for martingales |
| BDG | $\|M^*\|_p \asymp \|[M]^{1/2}\|_p$ | Two-sided control via quadratic variation |
| Azuma-Hoeffding | Exponential tail for bounded differences | Concentration for bounded martingales |

---

## Summary

Doob's maximal inequality is one of the most powerful tools in martingale theory:

$$
\boxed{\left\|\sup_{0 \le t \le T} |M_t|\right\|_{L^p} \le \frac{p}{p-1} \|M_T\|_{L^p}, \quad p > 1}
$$

**Key insights**:

1. The maximum of a martingale is controlled by its terminal value—with explicit constants.
2. The constant $\frac{p}{p-1}$ is optimal and blows up as $p \to 1$.
3. The inequality extends to submartingales (for the positive part).
4. Combined with BDG, it provides comprehensive control of martingale fluctuations.

**Applications span**:

- SDE theory (existence and uniqueness)
- Martingale convergence
- Concentration inequalities
- Numerical analysis of stochastic algorithms

---

## Exercises

### Exercise 1: Maximal Inequality Applications

(a) Use Doob's $L^2$ inequality to show $\mathbb{E}[\sup_{t \le T} W_t^2] \le 4T$.

(b) Find an upper bound for $\mathbb{P}(\sup_{t \le 1} |W_t| \ge 3)$.

(c) Compare your bound in (b) with the exact value from the reflection principle.

### Exercise 2: L^p Bounds

Let $M_t$ be a martingale with $\mathbb{E}[|M_T|^4] = C$.

(a) Use Doob's inequality to bound $\mathbb{E}[\sup_{t \le T} |M_t|^4]$.

(b) What happens to the constant as $p \to 1$?

(c) State and prove Doob's $L^1$ weak inequality.

### Exercise 3: Convergence Application

Let $M_n$ be a discrete martingale with $\sup_n \mathbb{E}[M_n^2] < \infty$.

(a) Use Doob's inequality to show $\sup_n |M_n| < \infty$ a.s.

(b) Deduce that $M_n$ converges a.s.

(c) Give an example where $\sup_n \mathbb{E}[|M_n|] < \infty$ but $M_n$ does not converge in $L^1$.

### Exercise 4: Maximum of Brownian Motion

Let $M_t = \sup_{s \le t} W_s$.

(a) Prove that $M_t - W_t \ge 0$ and is increasing in $t$.

(b) Show that $M_t$ and $M_t - W_t$ each have the same distribution as $|W_t|$.

*Hint*: Use the reflection principle. The process $W'_t = W_t - 2(W_t - M_t)^+ = 2M_t - W_t$ (reflecting $W$ at its running maximum) is also a Brownian motion. Show $M_t = \sup_{s\le t}W'_s$ and use symmetry.

(c) Use this to find $\mathbb{P}(M_t \ge a, W_t \le b)$ for $a > b$.

---

## Solutions

??? success "Solution to Exercise 1"
    **(a)** Brownian motion $W_t$ is a martingale, so $|W_t|$ is a non-negative submartingale. By Doob's $L^2$ inequality (with $p = 2$):

    $$
    \mathbb{E}\left[\sup_{0 \le t \le T} |W_t|^2\right] \le \left(\frac{2}{2-1}\right)^2 \mathbb{E}[|W_T|^2] = 4\mathbb{E}[W_T^2] = 4T
    $$

    **(b)** By Doob's weak $L^1$ inequality (applied to the submartingale $|W_t|$) with $\lambda = 3$:

    $$
    \mathbb{P}\left(\sup_{t \le 1} |W_t| \ge 3\right) \le \frac{\mathbb{E}[|W_1|^2]}{3^2} = \frac{1}{9} \approx 0.111
    $$

    Alternatively, using the $L^2$ bound: by Markov's inequality applied to the $L^2$ result:

    $$
    \mathbb{P}\left(\sup_{t \le 1} |W_t| \ge 3\right) \le \frac{\mathbb{E}[\sup_{t \le 1} W_t^2]}{9} \le \frac{4 \cdot 1}{9} = \frac{4}{9} \approx 0.444
    $$

    The Chebyshev-type bound is tighter: $1/9$.

    **(c)** The exact value from the reflection principle: $\mathbb{P}(\sup_{t \le 1} W_t \ge 3) = 2\mathbb{P}(W_1 \ge 3) = 2\Phi(-3) \approx 2 \times 0.00135 = 0.0027$. By symmetry, $\mathbb{P}(\sup_{t \le 1} |W_t| \ge 3) \le 2 \times 0.0027 = 0.0054$ (this is not exact for the absolute value, but gives the right order). The exact value is approximately $0.0054$, far smaller than the bounds of $1/9 \approx 0.111$ or $4/9 \approx 0.444$. The Doob bounds are correct but conservative.

??? success "Solution to Exercise 2"
    **(a)** By Doob's $L^p$ inequality with $p = 4$:

    $$
    \mathbb{E}\left[\sup_{t \le T} |M_t|^4\right] \le \left(\frac{4}{4-1}\right)^4 \mathbb{E}[|M_T|^4] = \left(\frac{4}{3}\right)^4 C = \frac{256}{81}C \approx 3.16C
    $$

    **(b)** As $p \to 1^+$, the constant $\left(\frac{p}{p-1}\right)^p \to \infty$. Specifically, $\frac{p}{p-1} \to \infty$ as $p \to 1^+$, so the bound becomes vacuous. This reflects the fact that for $p = 1$, the maximal inequality in the strong $L^p$ form does not hold — one needs the weaker $L^1$ form or the $L\log L$ condition.

    **(c)** **Doob's $L^1$ weak inequality**: For a non-negative submartingale $\{X_t\}$ and $\lambda > 0$:

    $$
    \lambda \cdot \mathbb{P}(X_T^* \ge \lambda) \le \mathbb{E}[X_T \cdot \mathbf{1}_{\{X_T^* \ge \lambda\}}] \le \mathbb{E}[X_T]
    $$

    **Proof**: Define $\tau = \inf\{t : X_t \ge \lambda\} \wedge T$. On $\{X_T^* \ge \lambda\}$, $X_\tau \ge \lambda$. By optional sampling for submartingales:

    $$
    \mathbb{E}[X_T \mid \mathcal{F}_\tau] \ge X_\tau
    $$

    Multiplying by $\mathbf{1}_{\{X_T^* \ge \lambda\}}$ (which is $\mathcal{F}_\tau$-measurable) and taking expectations:

    $$
    \mathbb{E}[X_T \cdot \mathbf{1}_{\{X_T^* \ge \lambda\}}] \ge \mathbb{E}[X_\tau \cdot \mathbf{1}_{\{X_T^* \ge \lambda\}}] \ge \lambda \cdot \mathbb{P}(X_T^* \ge \lambda) \quad \square
    $$

??? success "Solution to Exercise 3"
    **(a)** By Doob's $L^2$ inequality:

    $$
    \mathbb{E}\left[\sup_n |M_n|^2\right] \le 4 \sup_n \mathbb{E}[M_n^2] < \infty
    $$

    Since $\mathbb{E}[\sup_n |M_n|^2] < \infty$, we have $\sup_n |M_n|^2 < \infty$ a.s., hence $\sup_n |M_n| < \infty$ a.s. $\square$

    **(b)** Since $\sup_n \mathbb{E}[M_n^2] < \infty$ implies $\sup_n \mathbb{E}[|M_n|] \le \sup_n (\mathbb{E}[M_n^2])^{1/2} < \infty$ (by Jensen), the martingale is $L^1$-bounded. By Doob's martingale convergence theorem, $M_n$ converges a.s. to a finite limit $M_\infty$.

    Moreover, $L^2$-boundedness implies uniform integrability (since $p = 2 > 1$), so $M_n \to M_\infty$ also in $L^1$ (and in fact in $L^2$). $\square$

    **(c)** Let $M_n = \prod_{i=1}^n \xi_i$ where $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$, with $M_0 = 1$. Then $\mathbb{E}[M_n] = 1$ and $\sup_n \mathbb{E}[|M_n|] = 1 < \infty$.

    By the convergence theorem, $M_n \to M_\infty$ a.s. Since eventually some $\xi_i = 0$, $M_\infty = 0$ a.s.

    But $\mathbb{E}[M_n] = 1 \not\to 0 = \mathbb{E}[M_\infty]$, so $M_n$ does not converge in $L^1$. The family $\{M_n\}$ is not uniformly integrable: the expectation is carried by the event $\{\xi_1 = \cdots = \xi_n = 2\}$ of probability $(1/2)^n$, where $M_n = 2^n$.

??? success "Solution to Exercise 4"
    **(a)** Let $M_t = \sup_{s \le t} W_s$. Since $W_t \le M_t$ always and $M_t$ is the running maximum, $M_t - W_t \ge 0$.

    To show $M_t - W_t$ is increasing in $t$: for $s < t$, $M_t \ge M_s$ (the maximum can only increase). But $M_t - W_t$ is not necessarily monotone increasing. Actually, $M_t - W_t$ is **not** monotone increasing in general (it can decrease when $W$ moves up toward a new maximum). The correct statement is that $M_t$ is increasing in $t$ (non-decreasing). The process $M_t - W_t$ is non-negative but oscillates.

    What is true: $M_t - W_t \ge 0$ for all $t$, and $M_t - W_t = 0$ precisely when $W_t$ is at its running maximum (i.e., $W_t = M_t$).

    **(b)** By the reflection principle and Lévy's identity:

    $$
    (M_t, M_t - W_t) \stackrel{d}{=} (|W_t|, |W_t| \cdot \text{sign terms...})
    $$

    More precisely, **Lévy's identity** states:

    $$
    M_t - W_t \stackrel{d}{=} |W_t|
    $$

    and $M_t \stackrel{d}{=} |W_t|$.

    To see $M_t \stackrel{d}{=} |W_t|$: from the reflection principle, $\mathbb{P}(M_t \ge a) = 2\mathbb{P}(W_t \ge a) = \mathbb{P}(|W_t| \ge a)$ for $a > 0$ (using $\mathbb{P}(W_t \ge a) = \mathbb{P}(W_t \le -a)$ by symmetry). So $M_t$ and $|W_t|$ have the same distribution.

    The identity $M_t - W_t \stackrel{d}{=} |W_t|$ follows from Lévy's theorem, which states that $(M_t - W_t, M_t) \stackrel{d}{=} (|W_t|, L_t)$ where $L_t$ is the local time at 0, or more directly that $M_t - W_t$ is a reflected Brownian motion.

    **(c)** For $a > b$ (so $a > 0$ and $b < a$):

    $$
    \mathbb{P}(M_t \ge a, W_t \le b) = \mathbb{P}(M_t \ge a) - \mathbb{P}(M_t \ge a, W_t > b)
    $$

    By the reflection principle: on $\{M_t \ge a\}$, reflect the path at time $\tau_a$. The reflected path $\hat{W}_t = 2a - W_t$ has $\hat{W}_t \ge 2a - b > a$ when $W_t \le b$. Therefore:

    $$
    \mathbb{P}(M_t \ge a, W_t \le b) = \mathbb{P}(W_t \ge 2a - b)
    $$

    since the reflection creates a bijection between paths hitting $a$ and ending at or below $b$, and paths ending at or above $2a - b$.

    $$
    \mathbb{P}(M_t \ge a, W_t \le b) = \Phi\left(\frac{-(2a - b)}{\sqrt{t}}\right) = \Phi\left(\frac{b - 2a}{\sqrt{t}}\right)
    $$

    where $\Phi$ is the standard normal CDF.