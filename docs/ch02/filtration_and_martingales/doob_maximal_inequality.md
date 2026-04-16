# Doob's Maximal Inequality

[Martingales](martingales.md) come with a remarkable global control: the running maximum $\sup_{s \le t} |M_s|$ is bounded, in $L^p$, by the terminal value $|M_t|$ — with an explicit and sharp constant. This is the canonical tool for turning pointwise bounds into uniform-in-time bounds.

---

## Statement

**Theorem (Doob's $L^p$ maximal inequality).** Let $M$ be a right-continuous martingale (or a nonnegative submartingale) and let $p > 1$. Then

$$
\Bigl\| \sup_{0 \le t \le T} |M_t| \Bigr\|_{L^p} \le \frac{p}{p-1} \|M_T\|_{L^p}.
$$

The constant $p/(p-1)$ is sharp and blows up as $p \to 1^+$, reflecting that the $L^1$ case requires a different form.

**Weak $L^1$ form.** For a nonnegative submartingale $X$ and $\lambda > 0$,

$$
\lambda \cdot \mathbb{P}\Bigl(\sup_{0 \le t \le T} X_t \ge \lambda\Bigr) \le \mathbb{E}\bigl[X_T \mathbf{1}_{\{X_T^* \ge \lambda\}}\bigr] \le \mathbb{E}[X_T].
$$

---

## Intuition

The maximum of an arbitrary process can be vastly larger than any single value. For martingales this fails: on the event $\{X_T^* \ge \lambda\}$, the [optional sampling](optional_sampling_theorem.md) identity forces the terminal value to "pay" for the excursion to $\lambda$. Integrating this trade-off over all $\lambda$ via the layer-cake formula upgrades the weak bound to the strong $L^p$ bound.

---

## Proof Outline

*Weak $L^1$ step.* Let $\tau = \inf\{t : X_t \ge \lambda\} \wedge T$. On $\{X_T^* \ge \lambda\}$, $X_\tau \ge \lambda$. Optional sampling for submartingales gives $\mathbb{E}[X_T \mid \mathcal{F}_\tau] \ge X_\tau$, and integrating over $\{X_T^* \ge \lambda\}$ (which is $\mathcal{F}_\tau$-measurable) yields the weak bound.

*Layer cake + Hölder.* Integrate the weak bound against $p \lambda^{p-2}\,d\lambda$:

$$
\mathbb{E}[(X_T^*)^p] \le \frac{p}{p-1} \mathbb{E}[X_T (X_T^*)^{p-1}].
$$

Apply Hölder with exponents $p$ and $p/(p-1)$ and divide through by $\|X_T^*\|_{L^p}^{p-1}$. $\square$

---

## Brownian Example

!!! example "Brownian motion, $p = 2$"
    $W_t$ is a martingale, $|W_t|$ a submartingale. Doob's $L^2$ inequality gives
    
    $$
    \mathbb{E}\Bigl[\sup_{0 \le t \le T} W_t^2\Bigr] \le 4 \mathbb{E}[W_T^2] = 4T,
    $$
    
    equivalently $\|\sup_{t \le T} |W_t|\|_{L^2} \le 2\sqrt{T}$. The weak bound gives the tail estimate
    
    $$
    \mathbb{P}\Bigl(\sup_{t \le T} |W_t| \ge a\Bigr) \le \frac{\mathbb{E}[W_T^2]}{a^2} = \frac{T}{a^2}.
    $$
    
    The reflection principle gives the exact value $2\Phi(-a/\sqrt{T})$ — Doob's bound is a universal upper bound applicable far beyond Brownian motion.

---

## Why This Matters

Doob's inequality is the standard route from pointwise to uniform control. It underpins:

- convergence of $L^p$-bounded martingales (see [Martingale Convergence](martingale_convergence.md)),
- existence of solutions to SDEs (controlling Picard iterates uniformly in $t$),
- $L^2$ theory of stochastic integrals (via the Burkholder–Davis–Gundy extension, which bounds $(M^*)^p$ by the quadratic variation $[M]^{p/2}$).

---

## Exercises

**Exercise 1.** Brownian motion.

(a) Use Doob's $L^2$ inequality to show $\mathbb{E}[\sup_{t \le T} W_t^2] \le 4T$.
(b) Bound $\mathbb{P}(\sup_{t \le 1} |W_t| \ge 3)$.
(c) Compare (b) with the exact value from the reflection principle.

??? success "Solution to Exercise 1"
    **(a)** Doob with $p = 2$: $\mathbb{E}[\sup_{t \le T} W_t^2] \le 4 \mathbb{E}[W_T^2] = 4T$.

    **(b)** The weak $L^2$ bound (Chebyshev applied to $W_t^2$, then Doob): $\mathbb{P}(\sup_{t \le 1} |W_t| \ge 3) \le \mathbb{E}[\sup_{t \le 1} W_t^2]/9 \le 4/9$. A tighter alternative uses Doob's weak $L^1$ on the submartingale $W_t^2$: $\mathbb{P}(\sup_{t \le 1} W_t^2 \ge 9) \le \mathbb{E}[W_1^2]/9 = 1/9$.

    **(c)** Reflection principle: $\mathbb{P}(\sup_{t \le 1} W_t \ge 3) = 2\Phi(-3) \approx 0.0027$, so $\mathbb{P}(\sup_{t \le 1} |W_t| \ge 3) \approx 0.0054$. Doob's bound $1/9 \approx 0.111$ is loose but universally applicable.

---

**Exercise 2.** $L^p$ bounds.

(a) For a martingale $M$ with $\mathbb{E}[|M_T|^4] = C$, bound $\mathbb{E}[\sup_{t \le T} |M_t|^4]$.
(b) What happens to the Doob constant as $p \to 1^+$?

??? success "Solution to Exercise 2"
    **(a)** With $p = 4$: $\mathbb{E}[\sup_{t \le T} |M_t|^4] \le (4/3)^4 C = 256 C / 81 \approx 3.16 C$.

    **(b)** $(p/(p-1))^p \to \infty$ as $p \to 1^+$. The strong $L^p$ bound degenerates; one must use either the weak form or an $L \log L$ refinement.

---

**Exercise 3.** Let $M_n$ be a discrete martingale with $\sup_n \mathbb{E}[M_n^2] < \infty$.

(a) Show $\sup_n |M_n| < \infty$ a.s.
(b) Deduce a.s. convergence of $M_n$.

??? success "Solution to Exercise 3"
    **(a)** Doob's $L^2$ inequality applied on $[0, N]$ and letting $N \to \infty$: $\mathbb{E}[\sup_n M_n^2] \le 4 \sup_n \mathbb{E}[M_n^2] < \infty$. A finite-expectation random variable is finite a.s.

    **(b)** $L^2$-bounded implies $L^1$-bounded (Jensen). By the martingale convergence theorem, $M_n \to M_\infty$ a.s. (and in fact in $L^2$, since $L^2$-boundedness gives uniform integrability).

---

**Exercise 4 (Prove the strong bound).** Starting from the weak $L^1$ inequality for nonnegative submartingales, derive the Doob $L^p$ inequality for $p > 1$ in full.

??? success "Solution to Exercise 4"
    Let $X_T^* = \sup_{t \le T} X_t$. By the layer-cake formula and the weak bound,
    
    $$
    \mathbb{E}[(X_T^*)^p] = p \int_0^\infty \lambda^{p-1} \mathbb{P}(X_T^* \ge \lambda)\,d\lambda \le p \int_0^\infty \lambda^{p-2} \mathbb{E}[X_T \mathbf{1}_{\{X_T^* \ge \lambda\}}]\,d\lambda.
    $$
    
    By Fubini,
    
    $$
    p \int_0^\infty \lambda^{p-2} \mathbb{E}[X_T \mathbf{1}_{\{X_T^* \ge \lambda\}}]\,d\lambda = p\, \mathbb{E}\Bigl[X_T \int_0^{X_T^*} \lambda^{p-2}\,d\lambda\Bigr] = \frac{p}{p-1} \mathbb{E}[X_T (X_T^*)^{p-1}].
    $$
    
    Hölder with conjugates $p, p/(p-1)$:
    
    $$
    \mathbb{E}[X_T (X_T^*)^{p-1}] \le \|X_T\|_{L^p} \|X_T^*\|_{L^p}^{p-1}.
    $$
    
    Combine and divide by $\|X_T^*\|_{L^p}^{p-1}$ (assumed finite and positive; otherwise truncate first):
    
    $$
    \|X_T^*\|_{L^p} \le \frac{p}{p-1} \|X_T\|_{L^p}. \quad \square
    $$

---

**Exercise 5 (Non-UI example).** Let $M_n = \prod_{i=1}^n \xi_i$ where $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$ and $M_0 = 1$.

(a) Verify $M_n$ is a martingale with $\sup_n \mathbb{E}[|M_n|] < \infty$.
(b) Show $M_n \to 0$ a.s. but $\mathbb{E}[M_n] = 1$ for all $n$.
(c) Why doesn't this contradict Doob's $L^p$ inequality?

??? success "Solution to Exercise 5"
    **(a)** $\mathbb{E}[\xi_i] = 1$, so $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = M_n \cdot \mathbb{E}[\xi_{n+1}] = M_n$ and $\mathbb{E}[|M_n|] = 1$.

    **(b)** Some $\xi_i = 0$ a.s., so $M_n = 0$ eventually, hence $M_\infty = 0$ a.s. But $\mathbb{E}[M_n] = 1$ for all $n$.

    **(c)** Doob's $L^p$ inequality needs $p > 1$. Here the mass of $M_n$ is concentrated on $\{\xi_1 = \cdots = \xi_n = 2\}$ of probability $2^{-n}$, where $M_n = 2^n$. So $\mathbb{E}[M_n^p] = 2^{n(p-1)} \to \infty$ for $p > 1$: $M$ is not $L^p$-bounded, and Doob does not apply. The family is $L^1$-bounded but not uniformly integrable, which is also why $\mathbb{E}[M_n] \not\to \mathbb{E}[M_\infty]$.
