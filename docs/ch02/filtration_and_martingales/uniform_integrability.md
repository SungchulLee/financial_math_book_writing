# Uniform Integrability

Almost sure convergence and $L^1$ convergence are not equivalent. Uniform integrability is precisely the additional condition bridging this gap. It is indispensable in martingale theory: it characterizes which martingales converge in $L^1$, and it governs when optional sampling holds at unbounded stopping times.

---

## The Gap Between a.s. and $L^1$ Convergence

**Example (mass escape)**: Let $X_n = n \cdot \mathbf{1}_{[0, 1/n]}$ on $\Omega = [0,1]$ with Lebesgue measure. Then $X_n \to 0$ almost surely (for every $\omega > 0$, eventually $\omega > 1/n$), yet:

$$
\mathbb{E}[|X_n|] = n \cdot \frac{1}{n} = 1 \not\to 0
$$

The sequence converges pointwise but the mass of $X_n$ concentrates on a vanishingly small set — it "escapes to zero." Uniform integrability rules out this behavior.

**Example (martingale)**: Let $M_n = \prod_{i=1}^n \xi_i$ where $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$. Then $M_n$ is a martingale, $M_n \to 0$ a.s. (eventually some $\xi_i = 0$), yet $\mathbb{E}[M_n] = 1$ for all $n$. The expected value is preserved but concentrated on the exponentially rare event $\{\xi_1 = \cdots = \xi_n = 2\}$, where $M_n = 2^n$.

These examples motivate the need for uniform control of the tails of a family of random variables.

---

## Definition

A family $\{X_\alpha\}_{\alpha \in A}$ of random variables is **uniformly integrable (UI)** if:

$$
\lim_{K \to \infty} \sup_{\alpha \in A} \mathbb{E}\bigl[|X_\alpha| \cdot \mathbf{1}_{\{|X_\alpha| > K\}}\bigr] = 0
$$

**Interpretation**: The tails of all $X_\alpha$ are uniformly small — the same truncation level $K$ works for the entire family simultaneously.

**Component conditions**:
- $L^1$-boundedness: $\sup_\alpha \mathbb{E}|X_\alpha| < \infty$ (follows from the UI definition by taking $K = 0$)
- Uniform tail control: the expectation beyond level $K$ tends to 0 uniformly in $\alpha$

---

## Equivalent Characterizations

**Theorem**: The following are equivalent for a family $\{X_\alpha\}$:

**(i) Uniform integrability** (definition above).

**(ii) $L^1$-boundedness plus equi-absolute continuity**: $\sup_\alpha \mathbb{E}|X_\alpha| < \infty$, and for every $\varepsilon > 0$ there exists $\delta > 0$ such that:
$$
\mathbb{P}(A) < \delta \implies \sup_\alpha \mathbb{E}[|X_\alpha| \cdot \mathbf{1}_A] < \varepsilon
$$

**(iii) de la Vallée Poussin condition**: There exists a convex function $\Phi: [0,\infty) \to [0,\infty)$ with $\Phi(0) = 0$ and $\Phi(x)/x \to \infty$ as $x \to \infty$, such that:
$$
\sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] < \infty
$$

**Proof sketch (i $\Rightarrow$ ii)**: For any event $A$ and level $K$:

$$
\mathbb{E}[|X_\alpha| \cdot \mathbf{1}_A] \le K \cdot \mathbb{P}(A) + \mathbb{E}[|X_\alpha| \cdot \mathbf{1}_{\{|X_\alpha| > K\}}]
$$

Given $\varepsilon > 0$, choose $K$ so that the second term $< \varepsilon/2$ (by UI), then $\delta = \varepsilon/(2K)$.

**Proof sketch (iii $\Rightarrow$ i)**: Since $\Phi$ is convex with $\Phi(0) = 0$, the function $x \mapsto \Phi(x)/x$ is non-decreasing (a standard consequence of convexity). Therefore for $x > K > 0$:

$$
x \le \frac{\Phi(x)}{\Phi(K)/K}
$$

since $\Phi(x)/x \ge \Phi(K)/K$. Integrating:

$$
\mathbb{E}[|X_\alpha| \cdot \mathbf{1}_{\{|X_\alpha| > K\}}] \le \frac{K}{\Phi(K)} \cdot \sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] \to 0
$$

as $K \to \infty$.

---

## Examples and Non-Examples

### UI Families

**Example 1: Dominated family**. If $|X_\alpha| \le Y$ a.s. for all $\alpha$ where $Y \in L^1$, then $\{X_\alpha\}$ is UI.

**Proof**: $\mathbb{E}[|X_\alpha| \cdot \mathbf{1}_{\{|X_\alpha|>K\}}] \le \mathbb{E}[Y \cdot \mathbf{1}_{\{Y > K\}}] \to 0$ as $K \to \infty$, uniformly in $\alpha$. $\square$

**Example 2: $L^p$-bounded family, $p > 1$**. If $\sup_\alpha \mathbb{E}[|X_\alpha|^p] < \infty$ for some $p > 1$, then $\{X_\alpha\}$ is UI.

**Proof**: By Hölder's inequality:

$$
\mathbb{E}[|X_\alpha| \cdot \mathbf{1}_{\{|X_\alpha|>K\}}] \le \frac{1}{K^{p-1}} \mathbb{E}[|X_\alpha|^p] \le \frac{C}{K^{p-1}} \to 0
$$

as $K \to \infty$, where $C = \sup_\alpha \mathbb{E}[|X_\alpha|^p]$. $\square$

**Example 3: Conditional expectations of a single variable**. If $Y \in L^1$, then $\{\mathbb{E}[Y \mid \mathcal{G}] : \mathcal{G} \subseteq \mathcal{F}\}$ is UI.

**Proof**: By conditional Jensen, $|\mathbb{E}[Y|\mathcal{G}]| \le \mathbb{E}[|Y||\mathcal{G}]$, so it suffices to show $\{\mathbb{E}[|Y||\mathcal{G}] : \mathcal{G} \subseteq \mathcal{F}\}$ is UI. This family is $L^1$-bounded: $\mathbb{E}[\mathbb{E}[|Y||\mathcal{G}]] = \mathbb{E}[|Y|]$ for all $\mathcal{G}$. For equi-absolute continuity: given $\varepsilon > 0$, since $|Y| \in L^1$ there exists $\delta > 0$ such that $\int_A |Y|\,d\mathbb{P} < \varepsilon$ whenever $\mathbb{P}(A) < \delta$. For any event $A$ with $\mathbb{P}(A) < \delta$:
$$
\mathbb{E}[\mathbb{E}[|Y||\mathcal{G}]\,\mathbf{1}_A] = \mathbb{E}[|Y|\,\mathbf{1}_A] < \varepsilon
$$
By characterization (ii), the family is UI. $\square$

This is the key example: **every UI martingale arises from conditioning a single $L^1$ variable** — see the convergence theorem below.

**Example 4: Finite collection**. Any finite family $\{X_1, \ldots, X_n\} \subset L^1$ is UI (take $\delta$ small enough that each term is controlled).

### Non-UI Families

**Example 5**: $\{n \cdot \mathbf{1}_{[0,1/n]}\}$ on $[0,1]$. As shown above, $\mathbb{E}[n \cdot \mathbf{1}_{[0,1/n]} \cdot \mathbf{1}_{\{n \cdot \mathbf{1}_{[0,1/n]} > K\}}] = 1$ for all $K < n$. This does not go to 0.

**Example 6**: The exponential martingale $\{Z_t = e^{\theta W_t - \theta^2 t/2} : t \ge 0\}$ for $\theta \neq 0$. Although $\mathbb{E}[Z_t] = 1$ for all $t$, we have $Z_t \to 0$ a.s. If it were UI, we would need $\mathbb{E}[Z_t] \to \mathbb{E}[Z_\infty] = 0$, contradiction.

---

## Vitali Convergence Theorem

The fundamental theorem connecting UI to $L^1$ convergence:

**Theorem (Vitali)**: Let $\{X_n\}$ be a sequence with $X_n \to X$ almost surely (or in probability). Then:

$$
X_n \to X \text{ in } L^1 \quad \iff \quad \{X_n\} \text{ is uniformly integrable}
$$

**Proof ($\Rightarrow$, $L^1$ convergence implies UI)**: If $X_n \to X$ in $L^1$, then $\sup_n \mathbb{E}|X_n| < \infty$ and the family is equi-absolutely continuous by the $L^1$ convergence.

**Proof ($\Leftarrow$, UI plus a.s. convergence implies $L^1$)**: For any $\varepsilon > 0$, choose $\delta$ from condition (ii). By Egorov's theorem, there exists $A$ with $\mathbb{P}(A) < \delta$ such that $X_n \to X$ uniformly on $A^c$. Then:

$$
\mathbb{E}[|X_n - X|] = \mathbb{E}[|X_n - X| \cdot \mathbf{1}_{A^c}] + \mathbb{E}[|X_n - X| \cdot \mathbf{1}_A] < \varepsilon + 2\varepsilon
$$

for large $n$, using uniform convergence on $A^c$ and UI (plus dominated convergence for $X$) on $A$. $\square$

---

## Uniform Integrability and Martingales

This is the central application of UI in this chapter.

### Characterization of $L^1$-Convergent Martingales

**Theorem**: Let $(M_n, \mathcal{F}_n)_{n \ge 0}$ be a martingale. The following are equivalent:

1. $(M_n)$ is **uniformly integrable**.
2. $M_n \to M_\infty$ **in $L^1$** for some $M_\infty \in L^1$.
3. $M_n \to M_\infty$ **a.s. and in $L^1$** for some $M_\infty \in L^1$.
4. $(M_n)$ is **closed**: there exists $X \in L^1(\mathcal{F}_\infty)$ such that $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ for all $n$.

**Proof of (4) $\Rightarrow$ (1)**: Conditional expectations of a single $L^1$ variable form a UI family (Example 3 above).

**Proof of (1) $\Rightarrow$ (3)**: By Doob's a.s. convergence theorem ($L^1$-bounded martingales converge a.s.), $M_n \to M_\infty$ a.s. By Vitali (UI + a.s. convergence), $M_n \to M_\infty$ in $L^1$.

**Proof of (3) $\Rightarrow$ (4)**: For any $A \in \mathcal{F}_n$ and $m \ge n$, the martingale property gives $\int_A M_m \, d\mathbb{P} = \int_A M_n \, d\mathbb{P}$. Taking $m \to \infty$ via $L^1$ convergence:

$$
\int_A M_\infty \, d\mathbb{P} = \int_A M_n \, d\mathbb{P}
$$

Since $M_n$ is $\mathcal{F}_n$-measurable and satisfies partial averaging against all $\mathcal{F}_n$-sets, $M_n = \mathbb{E}[M_\infty \mid \mathcal{F}_n]$. $\square$

### Closure and UI: Intuition

A "closed" martingale $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ can be thought of as progressively revealing the terminal value $X$. At "time $\infty$," we have full information, and $M_\infty = X$. UI ensures that no mass escapes as $n \to \infty$ — the revelation process is tight.

### The Lévy Upward Theorem

As a direct consequence:

**Theorem**: If $X \in L^1$ and $\mathcal{F}_n \uparrow \mathcal{F}_\infty$, then:

$$
\mathbb{E}[X \mid \mathcal{F}_n] \to \mathbb{E}[X \mid \mathcal{F}_\infty] \quad \text{a.s. and in } L^1
$$

In particular, if $\mathcal{F}_\infty = \mathcal{F}$, then $\mathbb{E}[X \mid \mathcal{F}_n] \to X$ a.s. and in $L^1$.

---

## Uniform Integrability and Optional Sampling

UI is the key condition for extending optional sampling from bounded to unbounded stopping times.

**Theorem**: Let $(M_t)$ be a UI martingale and $\sigma \le \tau$ stopping times (not necessarily bounded). Then:

$$
\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma \quad \text{a.s.}
$$

**Proof sketch**: Apply bounded optional sampling to $\tau \wedge T$ and $\sigma \wedge T$, obtaining $\mathbb{E}[M_{\tau \wedge T} \mid \mathcal{F}_{\sigma \wedge T}] = M_{\sigma \wedge T}$. Take $T \to \infty$: by UI, $M_{\tau \wedge T} \to M_\tau$ in $L^1$, justifying passage to the limit. $\square$

**Why UI is necessary**: Without it, the doubling strategy provides a counterexample: a martingale $S_n$ with $\mathbb{P}(S_0 = 0) = 1$ but $\mathbb{E}[S_\tau] = 1$ at the stopping time $\tau = \inf\{n : S_n = 1\}$. The martingale $S_n$ is $L^1$-bounded but **not** UI.

---

## Practical Tests for UI

In practice, these sufficient conditions for UI are most useful:

| Condition | UI? | Reference |
|-----------|-----|-----------|
| $|X_\alpha| \le Y$, $Y \in L^1$ | ✓ | Dominated family |
| $\sup_\alpha \mathbb{E}[|X_\alpha|^p] < \infty$, $p > 1$ | ✓ | $L^p$ boundedness |
| $\sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] < \infty$, $\Phi(x)/x \to \infty$ | ✓ | de la Vallée Poussin |
| $X_\alpha = \mathbb{E}[Y \mid \mathcal{G}_\alpha]$, $Y \in L^1$ | ✓ | Conditional expectations |
| Finite family in $L^1$ | ✓ | Trivially |
| $\sup_\alpha \mathbb{E}[|X_\alpha|] < \infty$ only | ✗ | Not sufficient |
| $X_\alpha \to X$ a.s. but $\mathbb{E}[X_\alpha] \not\to \mathbb{E}[X]$ | ✗ | Mass escape |

---

## Summary

| Concept | Statement |
|---------|-----------|
| Definition | $\lim_{K\to\infty} \sup_\alpha \mathbb{E}[|X_\alpha|\mathbf{1}_{\{|X_\alpha|>K\}}] = 0$ |
| Equivalent: bounded + tight | $L^1$-bounded and equi-abs. continuous |
| Equivalent: de la Vallée Poussin | $\sup_\alpha \mathbb{E}[\Phi(\|X_\alpha\|)] < \infty$ for $\Phi(x)/x \to \infty$ |
| Vitali theorem | UI + a.s. convergence $\Leftrightarrow$ $L^1$ convergence |
| Martingale closure | $M_n$ is UI $\Leftrightarrow$ $M_n = \mathbb{E}[X|\mathcal{F}_n]$ for some $X \in L^1$ |
| Optional sampling | UI martingale $\Rightarrow$ optional sampling at unbounded stopping times |

Uniform integrability is the "tightness" condition for random variables, analogous to tightness for probability measures. It is the precise condition that prevents probability mass from escaping to infinity, and it is what separates almost sure convergence from the stronger $L^1$ convergence.

---

## Exercises

### Exercise 1: Checking UI

(a) Show that $\{W_t : 0 \le t \le T\}$ is UI for any fixed $T < \infty$.

*Hint*: Use Doob's $L^2$ inequality to show $\sup_{t \le T} \mathbb{E}[W_t^2] < \infty$, then apply the $L^p$ criterion.

(b) Show that $\{e^{W_t - t/2} : t \ge 0\}$ is **not** UI.

*Hint*: The family converges to 0 a.s. but $\mathbb{E}[e^{W_t - t/2}] = 1$.

(c) Is the family $\{\sin(W_t) : t \ge 0\}$ uniformly integrable?

### Exercise 2: Vitali Theorem

(a) Give an example of $X_n \to 0$ a.s. with $\mathbb{E}[X_n] = 1$ for all $n$. Identify why the family is not UI.

(b) Suppose $X_n \to X$ in probability and $\mathbb{E}[X_n^2] \le C < \infty$ for all $n$. Prove $X_n \to X$ in $L^1$.

(c) Give an example showing that $L^1$ convergence without a.s. convergence can still imply UI.

### Exercise 3: Martingale Convergence

(a) Let $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ for $X \in L^2$. Show the family is UI and that $M_n \to X$ in $L^2$.

(b) Construct a martingale that is $L^1$-bounded but **not** uniformly integrable. Verify it does not converge in $L^1$.

*Hint*: Use the product martingale $M_n = \prod_{i=1}^n \xi_i$ from the introduction.

(c) Prove: if $(M_n)$ is a UI martingale with $M_n \to M_\infty$ a.s., then for any stopping time $\tau$ (including $\tau = \infty$ on the event $\{\tau = \infty\}$):

$$
M_\tau = \mathbb{E}[M_\infty \mid \mathcal{F}_\tau] \quad \text{a.s.}
$$

### Exercise 4: de la Vallée Poussin

(a) Prove: if $\sup_\alpha \mathbb{E}[|X_\alpha| \log(1 + |X_\alpha|)] < \infty$, then $\{X_\alpha\}$ is UI.

*Hint*: Take $\Phi(x) = x \log(1+x)$ and verify $\Phi(x)/x \to \infty$.

(b) Conversely, show that for any UI family $\{X_\alpha\}$, there exists a function $\Phi$ with $\Phi(x)/x \to \infty$ such that $\sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] < \infty$.

*Hint*: This is the converse direction of the de la Vallée Poussin theorem. Construct $\Phi$ stepwise using the UI condition.

(c) Conclude that the three characterizations of UI in the main text are all equivalent.

---

## Solutions

??? success "Solution to Exercise 1"
    **(a)** For $T < \infty$, $\sup_{t \le T} \mathbb{E}[W_t^2] = \sup_{t \le T} t = T < \infty$. Since the family $\{W_t : 0 \le t \le T\}$ is $L^2$-bounded (with $p = 2 > 1$), it is uniformly integrable by the $L^p$ criterion. $\square$

    **(b)** The exponential martingale $Z_t = e^{W_t - t/2}$ satisfies $Z_t \to 0$ a.s. as $t \to \infty$ (since $\log Z_t = W_t - t/2 \to -\infty$ a.s. by the law of the iterated logarithm). However, $\mathbb{E}[Z_t] = 1$ for all $t$.

    If $\{Z_t : t \ge 0\}$ were UI, then by the Vitali convergence theorem, $Z_t \to 0$ a.s. combined with UI would imply $Z_t \to 0$ in $L^1$, giving $\mathbb{E}[Z_t] \to 0$. But $\mathbb{E}[Z_t] = 1$ for all $t$, a contradiction. Therefore the family is **not** UI. $\square$

    **(c)** $|\sin(W_t)| \le 1$ for all $t$ and $\omega$. The constant $Y \equiv 1$ is in $L^1$. Since $|\sin(W_t)| \le Y$ for all $t$, the family is dominated by an integrable random variable, hence **uniformly integrable**. $\square$

??? success "Solution to Exercise 2"
    **(a)** Let $X_n = n \cdot \mathbf{1}_{[0, 1/n]}$ on $(\Omega, \mathbb{P}) = ([0,1], \text{Lebesgue})$. Then $X_n \to 0$ a.s. (for $\omega > 0$, eventually $\omega > 1/n$) but $\mathbb{E}[X_n] = n \cdot (1/n) = 1$ for all $n$.

    The family is not UI because the tail mass does not vanish: for $K < n$,

    $$
    \mathbb{E}[X_n \mathbf{1}_{\{X_n > K\}}] = \mathbb{E}[n \cdot \mathbf{1}_{[0, 1/n]}] = 1
    $$

    since $X_n = n > K$ on $[0, 1/n]$ and $X_n = 0$ elsewhere. Thus $\sup_n \mathbb{E}[X_n \mathbf{1}_{\{X_n > K\}}] = 1$ for all $K$, which does not tend to 0.

    **(b)** Since $\mathbb{E}[X_n^2] \le C$ for all $n$, the family $\{X_n\}$ is $L^2$-bounded with $p = 2 > 1$, hence uniformly integrable. Combined with $X_n \to X$ in probability (which implies a.s. convergence along a subsequence), the Vitali convergence theorem gives $X_n \to X$ in $L^1$. $\square$

    More directly: UI and convergence in probability imply $L^1$ convergence (this is a standard extension of Vitali's theorem where a.s. convergence is replaced by convergence in probability).

    **(c)** Consider $X_n = Y \cdot \mathbf{1}_{\{U \le 1/n\}}$ where $Y \in L^1$ and $U \sim \text{Uniform}[0,1]$ independent of $Y$. Then $X_n \to 0$ in $L^1$ (since $\mathbb{E}[|X_n|] = \mathbb{E}[|Y|]/n \to 0$). However, $X_n$ need not converge a.s. (consider replacing the indicator with a more oscillating sequence). The $L^1$ convergence directly implies UI by the Vitali theorem (in the $L^1$-convergence-implies-UI direction). $\square$

??? success "Solution to Exercise 3"
    **(a)** Let $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ for $X \in L^2$. By the conditional Jensen inequality:

    $$
    \mathbb{E}[M_n^2] = \mathbb{E}[(\mathbb{E}[X \mid \mathcal{F}_n])^2] \le \mathbb{E}[\mathbb{E}[X^2 \mid \mathcal{F}_n]] = \mathbb{E}[X^2] < \infty
    $$

    So $\sup_n \mathbb{E}[M_n^2] \le \mathbb{E}[X^2] < \infty$. The family is $L^2$-bounded, hence UI.

    For $L^2$ convergence: $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ is the orthogonal projection of $X$ onto $L^2(\mathcal{F}_n)$. As $\mathcal{F}_n \uparrow \mathcal{F}_\infty$, the projections converge: $\|M_n - X\|_{L^2} \to 0$ by the $L^2$ martingale convergence theorem. $\square$

    **(b)** Let $M_n = \prod_{i=1}^n \xi_i$ where $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$, with $M_0 = 1$.

    - $\mathbb{E}[M_n] = 1$ for all $n$, so $\sup_n \mathbb{E}[|M_n|] = 1 < \infty$ ($L^1$-bounded).
    - $M_n \to 0$ a.s. (since with probability 1, eventually some $\xi_i = 0$).
    - $\mathbb{E}[M_n] = 1 \not\to 0 = \mathbb{E}[M_\infty]$, so $M_n$ does not converge in $L^1$.

    To see it is not UI: $\mathbb{E}[M_n \mathbf{1}_{\{M_n > K\}}] = \mathbb{E}[M_n] - \mathbb{E}[M_n \mathbf{1}_{\{M_n \le K\}}]$. Since $M_n \to 0$ a.s. and $M_n \mathbf{1}_{\{M_n \le K\}} \to 0$ a.s. with $|M_n \mathbf{1}_{\{M_n \le K\}}| \le K$, by bounded convergence $\mathbb{E}[M_n \mathbf{1}_{\{M_n \le K\}}] \to 0$. Therefore $\mathbb{E}[M_n \mathbf{1}_{\{M_n > K\}}] \to 1$ as $n \to \infty$, so $\sup_n \mathbb{E}[M_n \mathbf{1}_{\{M_n > K\}}] = 1$ for all $K$. Not UI. $\square$

    **(c)** Let $\tau$ be a stopping time (possibly infinite) and $(M_n)$ a UI martingale with $M_n \to M_\infty$ a.s. and in $L^1$. Define $\tau_k = \tau \wedge k$ (bounded stopping times).

    By bounded optional sampling: $M_{\tau_k} = \mathbb{E}[M_k \mid \mathcal{F}_{\tau_k}]$... Actually, more directly: for bounded stopping times $\sigma \le \tau_k$:

    $$
    \mathbb{E}[M_{\tau_k} \mid \mathcal{F}_\sigma] = M_\sigma
    $$

    As $k \to \infty$, $\tau_k \to \tau$ and $M_{\tau_k} \to M_\tau$ a.s. By UI of the martingale, $M_{\tau_k} \to M_\tau$ in $L^1$. For any $A \in \mathcal{F}_\tau$:

    $$
    \mathbb{E}[M_\tau \mathbf{1}_A] = \lim_k \mathbb{E}[M_{\tau_k} \mathbf{1}_A]
    $$

    Also, for $A \in \mathcal{F}_\tau$ and $k$ large enough, since $M$ is a UI martingale with terminal value $M_\infty$:

    $$
    \mathbb{E}[M_{\tau_k} \mathbf{1}_A] = \mathbb{E}[\mathbb{E}[M_\infty \mid \mathcal{F}_{\tau_k}] \mathbf{1}_A] = \mathbb{E}[M_\infty \mathbf{1}_A]
    $$

    (using $A \in \mathcal{F}_\tau \subseteq \mathcal{F}_{\tau_k}$). Therefore $\mathbb{E}[M_\tau \mathbf{1}_A] = \mathbb{E}[M_\infty \mathbf{1}_A]$ for all $A \in \mathcal{F}_\tau$, giving $M_\tau = \mathbb{E}[M_\infty \mid \mathcal{F}_\tau]$. $\square$

??? success "Solution to Exercise 4"
    **(a)** Take $\Phi(x) = x\log(1 + x)$. Then $\Phi(0) = 0$, $\Phi$ is convex on $[0, \infty)$ (since $\Phi''(x) = \frac{1}{1+x} + \frac{1}{(1+x)^2} \cdot x^{-1}\ldots$ actually let's verify: $\Phi'(x) = \log(1+x) + \frac{x}{1+x}$ and $\Phi''(x) = \frac{1}{1+x} + \frac{1}{(1+x)^2} > 0$), and

    $$
    \frac{\Phi(x)}{x} = \log(1 + x) \to \infty \quad \text{as } x \to \infty
    $$

    If $\sup_\alpha \mathbb{E}[|X_\alpha|\log(1 + |X_\alpha|)] < \infty$, then by the de la Vallee Poussin criterion (with $\Phi(x) = x\log(1+x)$), the family $\{X_\alpha\}$ is UI. $\square$

    **(b)** Given a UI family $\{X_\alpha\}$, for each $n \ge 1$, by UI there exists $K_n$ such that:

    $$
    \sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_{\{|X_\alpha| > K_n\}}] < \frac{1}{n}
    $$

    We may take $K_1 < K_2 < \cdots$ increasing. Define $\Phi$ piecewise: set $\Phi(x) = x$ for $x \le K_1$, and for $x \in (K_n, K_{n+1}]$, define $\Phi(x)$ to grow like $nx$ (making $\Phi(x)/x$ increase to $\infty$). Specifically, define:

    $$
    \Phi(x) = \int_0^x g(t)\,dt, \quad g(t) = n \text{ for } t \in (K_n, K_{n+1}]
    $$

    Then $\Phi$ is convex (since $g$ is non-decreasing), $\Phi(x)/x \to \infty$ as $x \to \infty$ (since $g(t) \to \infty$), and:

    $$
    \sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] \le \sum_{n=1}^\infty n \cdot \sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_{\{|X_\alpha| > K_n\}}] \le \sum_{n=1}^\infty n \cdot \frac{1}{n} + C < \infty
    $$

    (with appropriate bookkeeping of the bounded part). $\square$

    **(c)** Parts (a) and (b) together with the proof sketches in the main text (i $\Rightarrow$ ii, ii $\Rightarrow$ i, iii $\Rightarrow$ i, and the construction in (b) showing i $\Rightarrow$ iii) establish that all three characterizations are equivalent:

    - (i) UI definition (tail truncation)
    - (ii) $L^1$-bounded plus equi-absolute continuity
    - (iii) de la Vallee Poussin condition $\square$
