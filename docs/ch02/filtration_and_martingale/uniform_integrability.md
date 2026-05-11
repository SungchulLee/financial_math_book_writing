# Uniform Integrability

[Martingale Convergence](martingale_convergence.md) showed that $L^1$-boundedness forces almost sure convergence but not $L^1$ convergence — mass can escape along increasingly rare, increasingly large values. Uniform integrability is the precise fix. It is the condition that characterizes $L^1$-convergent martingales, and it is what extends optional sampling to unbounded stopping times.

---

## Definition

!!! abstract "Uniform integrability"
    A family $\{X_\alpha\}_{\alpha \in A}$ is **uniformly integrable (UI)** if

    $$
    \lim_{K \to \infty}\, \sup_{\alpha \in A}\, \mathbb{E}\bigl[|X_\alpha|\,\mathbf{1}_{\{|X_\alpha|>K\}}\bigr] = 0.
    $$

The truncation level $K$ controls the tails of every $X_\alpha$ at once. Taking $K = 0$ gives $L^1$-boundedness: $\sup_\alpha \mathbb{E}|X_\alpha| < \infty$. UI is strictly stronger — it also forbids the concentration of mass on shrinking high-value sets.

!!! warning "The canonical failure"
    On $\Omega = [0,1]$ with Lebesgue measure, let $X_n = n\,\mathbf{1}_{[0,1/n]}$. Then $X_n \to 0$ a.s. yet $\mathbb{E}[X_n] = 1$. For any $K$, once $n > K$, $\mathbb{E}[X_n \mathbf{1}_{\{X_n>K\}}] = 1$ — the family is not UI, and that is exactly why the expectation does not match the a.s. limit.

---

## Two Equivalent Characterizations

!!! success "Characterization theorem"
    A family $\{X_\alpha\}$ is UI if and only if it is $L^1$-bounded and **equi-absolutely continuous**: for every $\varepsilon > 0$ there exists $\delta > 0$ such that

    $$
    \mathbb{P}(A) < \delta \implies \sup_\alpha \mathbb{E}[|X_\alpha|\,\mathbf{1}_A] < \varepsilon.
    $$

**Proof**. ($\Rightarrow$) Given $\varepsilon > 0$, pick $K$ so the UI tail bound is $< \varepsilon/2$. Then for any event $A$,

$$
\mathbb{E}[|X_\alpha|\mathbf{1}_A] \le K\mathbb{P}(A) + \mathbb{E}[|X_\alpha|\mathbf{1}_{\{|X_\alpha|>K\}}] \le K\mathbb{P}(A) + \varepsilon/2.
$$

Take $\delta = \varepsilon/(2K)$. ($\Leftarrow$) Let $C = \sup_\alpha \mathbb{E}|X_\alpha|$. Markov gives $\mathbb{P}(|X_\alpha|>K) \le C/K$, so choosing $K = C/\delta$ makes the tail event small enough for equi-absolute continuity to yield the UI bound. $\square$

A second useful test is **de la Vallée Poussin**: if there is a convex $\Phi$ with $\Phi(x)/x \to \infty$ and $\sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)] < \infty$, then $\{X_\alpha\}$ is UI. The idea is that $|x| \le \Phi(x) / (\Phi(K)/K)$ for $x > K$, so tails of $|X_\alpha|$ are controlled by tails of $\Phi(|X_\alpha|)$, which are bounded uniformly.

---

## UI Examples

!!! example "UI families"

    - **Dominated**: if $|X_\alpha| \le Y$ for some $Y \in L^1$, then $\mathbb{E}[|X_\alpha|\mathbf{1}_{\{|X_\alpha|>K\}}] \le \mathbb{E}[Y\mathbf{1}_{\{Y>K\}}] \to 0$.
    - **$L^p$-bounded with $p > 1$**: $\mathbb{E}[|X_\alpha|\mathbf{1}_{\{|X_\alpha|>K\}}] \le K^{-(p-1)}\mathbb{E}|X_\alpha|^p \to 0$.
    - **Conditional expectations of a single $L^1$ variable**: $\{\mathbb{E}[Y\mid \mathcal{G}]: \mathcal{G} \subseteq \mathcal{F}\}$ is UI. Indeed $\mathbb{E}|\mathbb{E}[Y\mid\mathcal{G}]| \le \mathbb{E}|Y|$, and for $A \in \mathcal{F}$ with $\mathbb{P}(A)<\delta$, $\mathbb{E}[\mathbb{E}[|Y|\mid\mathcal{G}]\mathbf{1}_A] = \mathbb{E}[|Y|\mathbf{1}_A] < \varepsilon$ (as in equi-absolute continuity for $|Y|$). This is the decisive example: every UI martingale arises this way.
    - **Finite collection** in $L^1$.

!!! warning "Non-examples"

    - $\{n\mathbf{1}_{[0,1/n]}\}$ (mass escape).
    - The exponential martingale $\{e^{\theta W_t - \theta^2 t/2}\}$ for $\theta \ne 0$: $\mathbb{E}[Z_t] = 1$ but $Z_t \to 0$ a.s., contradicting UI via Vitali.

---

## Vitali: UI Is Exactly the L¹ Bridge

!!! success "Vitali convergence theorem"
    Suppose $X_n \to X$ in probability. Then $X_n \to X$ in $L^1$ if and only if $\{X_n\}$ is uniformly integrable.

**Proof idea**. ($\Rightarrow$) $L^1$-convergent sequences are automatically $L^1$-bounded and equi-absolutely continuous.

($\Leftarrow$) Fix $\varepsilon > 0$ and choose $\delta$ from equi-absolute continuity. By Egorov (after passing to an a.s.-convergent subsequence), there is $A$ with $\mathbb{P}(A) < \delta$ such that $X_n \to X$ uniformly on $A^c$. Then

$$
\mathbb{E}|X_n - X| \le \underbrace{\mathbb{E}[|X_n - X|\mathbf{1}_{A^c}]}_{\to 0 \text{ by uniform conv.}} + \underbrace{\mathbb{E}[|X_n|\mathbf{1}_A] + \mathbb{E}[|X|\mathbf{1}_A]}_{<\,2\varepsilon \text{ by equi-abs. cont.}}.
$$

$\square$

---

## The UI Martingale Theorem

This is the crux of the chapter. Combined with [Martingale Convergence](martingale_convergence.md), it identifies closed martingales with UI martingales.

!!! success "UI martingale characterization"
    For a martingale $(M_n)$, the following are equivalent:

    1. $(M_n)$ is UI.
    2. $M_n \to M_\infty$ in $L^1$.
    3. $M_n \to M_\infty$ a.s. and in $L^1$.
    4. $(M_n)$ is **closed**: $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ for some $X \in L^1$.

**Proof**. $(4) \Rightarrow (1)$: the conditional-expectation example above. $(1) \Rightarrow (3)$: UI $\Rightarrow L^1$-bounded $\Rightarrow$ a.s. convergence (Doob), then Vitali gives $L^1$. $(3) \Rightarrow (4)$: for $A \in \mathcal{F}_n$, $\int_A M_m\,d\mathbb{P} = \int_A M_n\,d\mathbb{P}$ for $m \ge n$; let $m \to \infty$ using $L^1$ convergence to get $\int_A M_\infty = \int_A M_n$, hence $M_n = \mathbb{E}[M_\infty \mid \mathcal{F}_n]$. $\square$

!!! tip "Lévy's upward theorem"
    If $X \in L^1$ and $\mathcal{F}_n \uparrow \mathcal{F}_\infty$, then $\mathbb{E}[X \mid \mathcal{F}_n] \to \mathbb{E}[X \mid \mathcal{F}_\infty]$ a.s. and in $L^1$. This is the previous theorem applied to the closed martingale $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$.

---

## UI and Optional Sampling

UI is also the condition that extends optional sampling to unbounded stopping times.

!!! success "UI optional sampling"
    If $(M_t)$ is a UI martingale and $\sigma \le \tau$ are stopping times (possibly unbounded), then

    $$
    \mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma \quad \text{a.s.}
    $$

**Why UI**. Apply bounded optional sampling to $\tau\wedge T$ and $\sigma\wedge T$ and let $T\to\infty$. UI supplies the $L^1$ convergence needed to pass to the limit.

Without UI the conclusion fails: the doubling strategy produces an $L^1$-bounded, non-UI martingale $S_n$ with $\mathbb{E}[S_0] = 0$ but $\mathbb{E}[S_\tau] = 1$ at $\tau = \inf\{n : S_n = 1\}$.

---

## Practical Summary

| Sufficient for UI | Reason |
|---|---|
| $|X_\alpha| \le Y \in L^1$ | Dominated |
| $\sup_\alpha \mathbb{E}|X_\alpha|^p < \infty$, $p > 1$ | $L^p$ truncation |
| $\sup_\alpha \mathbb{E}[\Phi(|X_\alpha|)]<\infty$, $\Phi(x)/x \to \infty$, $\Phi$ convex | de la Vallée Poussin |
| $X_\alpha = \mathbb{E}[Y \mid \mathcal{G}_\alpha]$, $Y \in L^1$ | Closure |
| Finite $\{X_1,\ldots,X_n\}\subset L^1$ | Trivial |

UI is the "no mass escape" condition. It plays the role for random variables that tightness plays for probability measures, and it is exactly what closes the gap between a.s. and $L^1$ convergence.

---

## Exercises

**Exercise 1.** Show that $\{W_t : 0 \le t \le T\}$ is UI for every $T < \infty$, while $\{e^{W_t - t/2} : t \ge 0\}$ is not.

??? success "Solution to Exercise 1"
    For the first family, $\sup_{t\le T}\mathbb{E}[W_t^2] = T < \infty$, so the family is $L^2$-bounded, hence UI by the $L^p$ criterion with $p = 2$.

    For the second, $Z_t = e^{W_t-t/2}$ is a martingale with $\mathbb{E}[Z_t] = 1$, yet $Z_t \to 0$ a.s. (the law of the iterated logarithm gives $\log Z_t = W_t - t/2 \to -\infty$). If the family were UI, Vitali would force $\mathbb{E}[Z_t] \to 0$, contradicting $\mathbb{E}[Z_t] = 1$. $\square$

---

**Exercise 2.** If $X_n \to X$ in probability and $\sup_n \mathbb{E}[X_n^2] < \infty$, show $X_n \to X$ in $L^1$.

??? success "Solution to Exercise 2"
    The $L^2$ bound implies UI (take $p = 2$ in the $L^p$ criterion). Vitali's theorem (which applies to convergence in probability) then gives $X_n \to X$ in $L^1$. $\square$

---

**Exercise 3.** Construct a martingale that is $L^1$-bounded but not UI, and verify directly that it fails to converge in $L^1$.

??? success "Solution to Exercise 3"
    Let $\xi_i$ be i.i.d. with $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$ and $M_n = \prod_{i=1}^n \xi_i$ (with $M_0 = 1$). Then $(M_n)$ is a martingale, $\mathbb{E}|M_n| = 1$ for all $n$, and $M_n \to 0$ a.s. (some $\xi_i$ eventually equals $0$).

    Because $M_n \mathbf{1}_{\{M_n \le K\}} \to 0$ a.s. and is bounded by $K$, dominated convergence gives $\mathbb{E}[M_n\mathbf{1}_{\{M_n\le K\}}] \to 0$, so $\mathbb{E}[M_n\mathbf{1}_{\{M_n>K\}}] \to 1$ for every $K$. Thus $(M_n)$ is not UI, and $\mathbb{E}[M_n] = 1 \ne 0 = \mathbb{E}[\lim M_n]$, so $M_n$ does not converge in $L^1$. $\square$

---

**Exercise 4.** Prove that if $\sup_\alpha \mathbb{E}[|X_\alpha|\log(1+|X_\alpha|)] < \infty$, then $\{X_\alpha\}$ is UI.

??? success "Solution to Exercise 4"
    Take $\Phi(x) = x\log(1+x)$. Then $\Phi$ is convex on $[0,\infty)$ (direct check: $\Phi''(x) = (1+x)^{-1} + (1+x)^{-2} > 0$), $\Phi(0) = 0$, and $\Phi(x)/x = \log(1+x) \to \infty$ as $x \to \infty$. The de la Vallée Poussin criterion applies. $\square$

---

**Exercise 5.** Let $(M_t)$ be a UI martingale with limit $M_\infty$ and $\tau$ any stopping time (possibly infinite). Prove $M_\tau = \mathbb{E}[M_\infty \mid \mathcal{F}_\tau]$ a.s.

??? success "Solution to Exercise 5"
    Since $(M_t)$ is UI, $M_t = \mathbb{E}[M_\infty \mid \mathcal{F}_t]$. For bounded $\tau_k = \tau \wedge k$, bounded optional sampling gives $M_{\tau_k} = \mathbb{E}[M_\infty \mid \mathcal{F}_{\tau_k}]$, so for $A \in \mathcal{F}_\tau \subseteq \mathcal{F}_{\tau_k}$,

    $$
    \mathbb{E}[M_{\tau_k}\mathbf{1}_A] = \mathbb{E}[M_\infty \mathbf{1}_A].
    $$

    UI and a.s. convergence of $M_t$ imply $M_{\tau_k} \to M_\tau$ a.s. and in $L^1$, so $\mathbb{E}[M_\tau \mathbf{1}_A] = \mathbb{E}[M_\infty \mathbf{1}_A]$ for all $A \in \mathcal{F}_\tau$, giving the result. $\square$
