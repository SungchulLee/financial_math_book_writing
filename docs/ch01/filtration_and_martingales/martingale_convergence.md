# Martingale Convergence

## The Convergence Question

One of the most striking features of martingale theory is that martingales "want to converge." Unlike general sequences of random variables, martingales possess an intrinsic structure—the conditional expectation property—that forces limiting behavior under mild conditions.

The fundamental question: given a martingale $\{M_t\}$ or $\{M_n\}$, does $\lim M_t$ (or $\lim M_n$) exist, and in what sense?

This section develops the convergence theory, progressing from almost sure convergence to $L^p$ convergence, with the crucial role of uniform integrability as the bridge between these modes.

---

## Almost Sure Convergence: The Upcrossing Lemma

The key to martingale convergence is Doob's **upcrossing inequality**, which bounds how often a martingale can oscillate between two levels.

### Upcrossings Defined

For a process $\{X_n\}$ and real numbers $a < b$, an **upcrossing** of the interval $[a, b]$ is a pair of times $s < t$ such that $X_s \le a$ and $X_t \ge b$ (the process crosses from below $a$ to above $b$).

Let $U_N^{[a,b]}$ denote the number of upcrossings of $[a, b]$ by $(X_0, X_1, \ldots, X_N)$.

### Doob's Upcrossing Inequality

**Theorem**: If $\{X_n\}_{n=0}^N$ is a submartingale, then:

$$
\boxed{(b - a) \mathbb{E}[U_N^{[a,b]}] \le \mathbb{E}[(X_N - a)^+]}
$$

where $(x)^+ = \max(x, 0)$.

**Proof sketch**: Define a betting strategy: "bet 1 when below $a$, bet 0 when above $b$." The gains from this predictable strategy are bounded below by $(b-a) \cdot U_N^{[a,b]} - (X_N - a)^-$. Since gains from a predictable strategy on a submartingale have nonnegative expectation, the inequality follows. $\square$

**Interpretation**: If the expected final value is bounded, the process cannot oscillate too much. Each upcrossing "costs" at least $b - a$ on average.

---

## The Martingale Convergence Theorem

**Theorem (Doob's Martingale Convergence Theorem)**: Let $\{M_n\}_{n \ge 0}$ be a martingale (or submartingale) satisfying:

$$
\sup_n \mathbb{E}[|M_n|] < \infty \quad \text{(}L^1\text{-bounded)}
$$

Then there exists a random variable $M_\infty$ with $\mathbb{E}|M_\infty| < \infty$ such that:

$$
\boxed{M_n \to M_\infty \quad \text{almost surely as } n \to \infty}
$$

**Proof**:

*Step 1*: For any rational $a < b$, the upcrossing inequality gives:

$$
\mathbb{E}[U_\infty^{[a,b]}] = \lim_N \mathbb{E}[U_N^{[a,b]}] \le \frac{\sup_n \mathbb{E}[(M_n - a)^+]}{b - a} < \infty
$$

Therefore $U_\infty^{[a,b]} < \infty$ almost surely.

*Step 2*: The event "$(M_n)$ oscillates infinitely often" equals:

$$
\bigcup_{a < b, \, a,b \in \mathbb{Q}} \{U_\infty^{[a,b]} = \infty\}
$$

This is a countable union of null sets, hence null.

*Step 3*: Therefore, $\liminf_n M_n = \limsup_n M_n$ almost surely, so the limit exists (possibly $\pm \infty$).

*Step 4*: To show $M_\infty$ is finite a.s., note that $(|M_n|)$ is a submartingale and:

$$
\mathbb{P}(|M_\infty| = \infty) \le \lim_K \mathbb{P}\left(\sup_n |M_n| \ge K\right) \le \lim_K \frac{\sup_n \mathbb{E}|M_n|}{K} = 0 \quad \square
$$

---

## $L^1$ Convergence and Uniform Integrability

Almost sure convergence does **not** imply $L^1$ convergence. The canonical counterexample:

**Example**: Let $\xi_1, \xi_2, \ldots$ be i.i.d. with $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$. Define:

$$
M_n = \prod_{i=1}^n \xi_i
$$

Then $M_n$ is a martingale with $\mathbb{E}[M_n] = 1$ for all $n$. However, $M_n \to 0$ almost surely (since $\mathbb{P}(\text{at least one } \xi_i = 0) = 1$), but $\mathbb{E}[M_n] = 1 \not\to 0 = \mathbb{E}[M_\infty]$.

The gap is filled by **uniform integrability**.

### Uniform Integrability

A family of random variables $\{X_\alpha\}_{\alpha \in A}$ is **uniformly integrable (UI)** if:

$$
\lim_{K \to \infty} \sup_{\alpha \in A} \mathbb{E}[|X_\alpha| \mathbf{1}_{\{|X_\alpha| > K\}}] = 0
$$

**Equivalent conditions**:

1. $\sup_\alpha \mathbb{E}|X_\alpha| < \infty$ and for every $\epsilon > 0$ there exists $\delta > 0$ such that $\mathbb{P}(A) < \delta \Rightarrow \sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_A] < \epsilon$.

2. The family is $L^1$-bounded and tight in the de la Vallée Poussin sense: there exists a convex increasing function $\Phi$ with $\Phi(x)/x \to \infty$ as $x \to \infty$ such that $\sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] < \infty$.

**Key examples of UI families**:

- Any $L^p$-bounded family with $p > 1$ (since $\mathbb{E}[|X| \mathbf{1}_{\{|X| > K\}}] \le K^{1-p} \mathbb{E}|X|^p$).
- The family $\{\mathbb{E}[Y \mid \mathcal{G}_\alpha]\}$ for any $Y \in L^1$ and any sub-$\sigma$-algebras $\mathcal{G}_\alpha$.
- Any family dominated by an integrable random variable.

---

## The UI Convergence Theorem

**Theorem**: Let $\{M_n\}$ be a martingale. The following are equivalent:

1. $(M_n)$ is uniformly integrable.

2. $M_n \to M_\infty$ in $L^1$ for some $M_\infty \in L^1$.

3. $M_n \to M_\infty$ a.s. and in $L^1$ for some $M_\infty \in L^1$.

4. There exists $M_\infty \in L^1$ such that $M_n = \mathbb{E}[M_\infty \mid \mathcal{F}_n]$ for all $n$.

5. $(M_n)$ is **closed**: there exists $X \in L^1$ such that $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$.

**Proof sketch** (main implications):

$(4) \Rightarrow (1)$: Conditional expectations of an integrable random variable form a UI family.

$(1) \Rightarrow (3)$: By the basic convergence theorem, $M_n \to M_\infty$ a.s. UI plus a.s. convergence implies $L^1$ convergence (Vitali).

$(3) \Rightarrow (4)$: For any $A \in \mathcal{F}_n$, by dominated convergence:

$$
\mathbb{E}[M_\infty \mathbf{1}_A] = \lim_m \mathbb{E}[M_m \mathbf{1}_A] = \mathbb{E}[M_n \mathbf{1}_A]
$$

showing $M_n = \mathbb{E}[M_\infty \mid \mathcal{F}_n]$. $\square$

---

## $L^p$ Convergence

**Theorem**: Let $p > 1$ and let $(M_n)$ be a martingale with $\sup_n \mathbb{E}|M_n|^p < \infty$. Then:

$$
\boxed{M_n \to M_\infty \quad \text{in } L^p \text{ and a.s.}}
$$

**Proof**: $L^p$-boundedness with $p > 1$ implies UI, so $L^1$ (hence a.s.) convergence follows. For $L^p$ convergence, Doob's maximal inequality gives:

$$
\mathbb{E}\left[\sup_n |M_n|^p\right] \le \left(\frac{p}{p-1}\right)^p \sup_n \mathbb{E}|M_n|^p < \infty
$$

Since $|M_n - M_\infty|^p \le 2^p \sup_n |M_n|^p$ which is integrable, dominated convergence yields $L^p$ convergence. $\square$

**Remark**: The case $p = 1$ fails: $L^1$-boundedness gives a.s. convergence but not $L^1$ convergence without UI.

---

## Backward Martingales

A **backward martingale** (or reverse martingale) is a sequence $(M_n, \mathcal{F}_n)_{n \le 0}$ with $\mathcal{F}_n \supseteq \mathcal{F}_{n-1}$ (decreasing filtration) and:

$$
\mathbb{E}[M_n \mid \mathcal{F}_{n-1}] = M_{n-1} \quad \text{for } n \le 0
$$

**Theorem (Backward Martingale Convergence)**: If $(M_n)_{n \le 0}$ is a backward martingale with $\sup_n \mathbb{E}|M_n| < \infty$, then:

$$
M_n \to M_{-\infty} \quad \text{a.s. and in } L^1
$$

where $M_{-\infty} = \mathbb{E}[M_0 \mid \mathcal{F}_{-\infty}]$ and $\mathcal{F}_{-\infty} = \bigcap_n \mathcal{F}_n$.

**Key difference**: Backward martingales **always** converge in $L^1$—uniform integrability is automatic since $(M_n)$ is a sequence of conditional expectations of $M_0$.

**Application (Strong Law of Large Numbers)**: Let $X_1, X_2, \ldots$ be i.i.d. with $\mathbb{E}|X_1| < \infty$. Define $\mathcal{F}_n = \sigma(S_n, S_{n+1}, \ldots)$ and $M_n = \frac{S_n}{n}$. Then $(M_n)$ is a backward martingale, and:

$$
\frac{S_n}{n} \to \mathbb{E}[X_1] \quad \text{a.s. and in } L^1
$$

---

## Continuous-Time Convergence

The convergence theorems extend to continuous time with appropriate modifications.

**Theorem**: Let $(M_t)_{t \ge 0}$ be a right-continuous martingale with:

$$
\sup_t \mathbb{E}|M_t| < \infty
$$

Then $M_\infty := \lim_{t \to \infty} M_t$ exists almost surely and is finite a.s.

If additionally $(M_t)$ is UI, then $M_t \to M_\infty$ in $L^1$ and $M_t = \mathbb{E}[M_\infty \mid \mathcal{F}_t]$.

**Regularity**: In continuous time, one typically assumes càdlàg paths. The Doob regularization theorem guarantees that any $L^1$-bounded martingale has a càdlàg modification.

---

## Convergence of Specific Martingales

### Example 1: Doob Martingale

If $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$ for some $X \in L^1$, then $M_t \to X$ a.s. and in $L^1$ as $t \to \infty$ (assuming $\mathcal{F}_t \uparrow \mathcal{F}$).

This is the Lévy martingale convergence theorem: as information increases, our best estimate of $X$ converges to $X$ itself.

### Example 2: Exponential Martingale

Consider $Z_t = \exp(\theta W_t - \frac{\theta^2 t}{2})$. For $\theta \neq 0$:

- $\mathbb{E}[Z_t] = 1$ for all $t$.
- $Z_t \to 0$ almost surely as $t \to \infty$ (since $W_t/t \to 0$ a.s. but the quadratic term dominates).

This is **not** UI: $\mathbb{E}[Z_t] = 1 \not\to 0 = \mathbb{E}[Z_\infty]$.

### Example 3: Random Walk Martingale

The simple random walk $S_n = \sum_{i=1}^n \xi_i$ (fair coin) satisfies $S_n \to ?$. Since $\mathbb{E}[S_n^2] = n \to \infty$, the walk is not $L^2$-bounded, and indeed $S_n$ does not converge.

However, $S_n/\sqrt{n} \Rightarrow N(0,1)$ in distribution (CLT), though this is **not** a.s. convergence.

---

## The Optional Stopping Connection

Martingale convergence and optional sampling are deeply connected:

**Theorem**: Let $(M_n)$ be a UI martingale with limit $M_\infty$. For any stopping time $\tau$ (possibly infinite):

$$
\mathbb{E}[M_\tau] = \mathbb{E}[M_0] \quad \text{and} \quad M_\tau = \mathbb{E}[M_\infty \mid \mathcal{F}_\tau]
$$

This extends the optional sampling theorem to unbounded stopping times, using convergence to handle the limit.

---

## Summary: The Convergence Hierarchy

| Condition | Almost Sure | $L^1$ | $L^p$ ($p > 1$) |
|-----------|-------------|-------|-----------------|
| $L^1$-bounded | ✓ | ✗ (need UI) | — |
| Uniformly integrable | ✓ | ✓ | — |
| $L^p$-bounded ($p > 1$) | ✓ | ✓ | ✓ |
| Closed (= $\mathbb{E}[X \mid \mathcal{F}_n]$) | ✓ | ✓ | Depends on $X$ |

**Key takeaways**:

1. **$L^1$-boundedness alone gives a.s. convergence** via the upcrossing lemma.

2. **Uniform integrability bridges a.s. and $L^1$ convergence** and is equivalent to closure.

3. **$L^p$-boundedness with $p > 1$ is stronger than UI** and gives $L^p$ convergence.

4. **Backward martingales always converge in $L^1$**—no additional conditions needed.

The convergence theory completes the structural picture of martingales: they are processes that, under boundedness conditions, settle down to limiting values, preserving the martingale property even at "time infinity."

---

## Exercises

### Exercise 1: Upcrossings

Let $M_n$ be a submartingale and let $U_N^{[a,b]}$ denote the number of upcrossings of $[a,b]$ by $M_0, \ldots, M_N$.

(a) State Doob's upcrossing inequality.

(b) Use the upcrossing inequality to prove: if $\sup_n \mathbb{E}[M_n^+] < \infty$, then $M_n$ converges a.s.

(c) Explain why the condition involves $M_n^+$ rather than $|M_n|$.

### Exercise 2: Uniform Integrability

(a) Prove that a family $\{X_\alpha\}$ is uniformly integrable if and only if it is $L^1$-bounded and satisfies: for all $\epsilon > 0$, there exists $\delta > 0$ such that $\mathbb{P}(A) < \delta$ implies $\sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_A] < \epsilon$.

(b) Show that $\{W_t : t \le T\}$ is uniformly integrable for any $T < \infty$.

(c) Show that $\{e^{W_t - t/2} : t \ge 0\}$ is **not** uniformly integrable.

### Exercise 3: Backward Martingales

Let $X_1, X_2, \ldots$ be i.i.d. with $\mathbb{E}[X_1] = \mu$ and let $\bar{X}_n = \frac{1}{n}\sum_{k=1}^n X_k$.

(a) Define $\mathcal{F}_{-n} = \sigma(\bar{X}_n, \bar{X}_{n+1}, \ldots)$. Show this is a decreasing sequence of $\sigma$-algebras.

(b) Prove that $(\bar{X}_n, \mathcal{F}_{-n})$ is a backward martingale.

(c) Use backward martingale convergence to prove the strong law of large numbers.
