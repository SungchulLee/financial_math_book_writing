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
