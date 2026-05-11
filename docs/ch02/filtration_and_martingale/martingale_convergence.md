# Martingale Convergence

Martingales "want to converge." The conditional expectation property forces limiting behavior under mild conditions, distinguishing martingales from arbitrary sequences of integrable random variables. This section establishes when — and in what sense — a martingale admits a limit, and isolates a gap that will be filled in [Uniform Integrability](uniform_integrability.md).

---

## Almost Sure Convergence

The path to a.s. convergence runs through **upcrossings**. For $a < b$, an upcrossing of $[a,b]$ by $X_0, X_1, \ldots$ is a pair $s < t$ with $X_s \le a$ and $X_t \ge b$. If a sequence oscillates infinitely, it upcrosses some rational interval infinitely often. Bounding the expected number of upcrossings therefore forces convergence.

!!! abstract "Doob's upcrossing inequality"
    If $(X_n)_{n=0}^N$ is a submartingale and $U_N^{[a,b]}$ is the number of upcrossings of $[a,b]$, then

    $$
    (b - a)\,\mathbb{E}[U_N^{[a,b]}] \le \mathbb{E}[(X_N - a)^+]
    $$

**Idea of proof**. Define a predictable "betting strategy" $H_n = 1$ when the process is inside an unfinished upcrossing, $0$ otherwise. Each completed upcrossing contributes at least $b-a$ to the gain $G_N = \sum H_n (X_n - X_{n-1})$, and $\mathbb{E}[G_N] \ge 0$ for submartingales. The inequality follows.

---

!!! success "Martingale convergence theorem (Doob)"
    Let $(M_n)$ be a submartingale with $\sup_n \mathbb{E}|M_n| < \infty$. Then there exists $M_\infty \in L^1$ such that

    $$
    M_n \to M_\infty \quad \text{almost surely.}
    $$

**Proof**. For each rational $a < b$, the upcrossing inequality gives $\mathbb{E}[U_\infty^{[a,b]}] \le \sup_n \mathbb{E}[(M_n - a)^+]/(b-a) < \infty$, so $U_\infty^{[a,b]} < \infty$ a.s. The event "$(M_n)$ oscillates" is the countable union over rational $a < b$ of $\{U_\infty^{[a,b]} = \infty\}$, hence null. So $\liminf M_n = \limsup M_n =: M_\infty$ a.s. Finiteness follows from Markov's inequality applied to $\sup_n |M_n|$. $\square$

---

## The L¹ Gap

A.s. convergence does **not** imply $L^1$ convergence. Mass can escape to rare high values:

!!! warning "Canonical counterexample"
    Let $\xi_i$ be i.i.d. with $\mathbb{P}(\xi_i = 2) = \mathbb{P}(\xi_i = 0) = 1/2$ and $M_n = \prod_{i=1}^n \xi_i$. Then $(M_n)$ is a martingale, $M_n \to 0$ a.s. (some $\xi_i$ eventually vanishes), yet $\mathbb{E}[M_n] = 1$ for all $n$. The mass is carried by the event $\{\xi_1 = \cdots = \xi_n = 2\}$ of probability $2^{-n}$, on which $M_n = 2^n$.

The missing condition is **uniform integrability**: the entire family has uniformly controlled tails. See [Uniform Integrability](uniform_integrability.md) for the full theory; we recall only what is needed here.

A family $\{X_\alpha\}$ is UI if

$$
\lim_{K\to\infty} \sup_\alpha \mathbb{E}[|X_\alpha|\,\mathbf{1}_{\{|X_\alpha|>K\}}] = 0.
$$

Key UI examples:

- any $L^p$-bounded family with $p > 1$;
- $\{\mathbb{E}[Y \mid \mathcal{G}_\alpha]\}$ for $Y \in L^1$ and sub-$\sigma$-algebras $\mathcal{G}_\alpha$;
- any family dominated by an integrable random variable.

---

## UI Martingales and Closure

!!! success "UI convergence theorem"
    For a martingale $(M_n)$, the following are equivalent:

    1. $(M_n)$ is uniformly integrable.
    2. $M_n \to M_\infty$ in $L^1$ for some $M_\infty \in L^1$.
    3. $M_n \to M_\infty$ a.s. and in $L^1$.
    4. $(M_n)$ is **closed**: $M_n = \mathbb{E}[X \mid \mathcal{F}_n]$ for some $X \in L^1$.

**Key implications**. $(4) \Rightarrow (1)$ because conditional expectations of a single $L^1$ variable are UI. $(1) \Rightarrow (3)$ combines Doob's a.s. theorem with Vitali's theorem (UI + a.s. $\Rightarrow L^1$). $(3) \Rightarrow (4)$ follows because for $A \in \mathcal{F}_n$, $\mathbb{E}[M_\infty \mathbf{1}_A] = \lim_m \mathbb{E}[M_m \mathbf{1}_A] = \mathbb{E}[M_n \mathbf{1}_A]$.

!!! tip "L^p case, p > 1"
    If $\sup_n \mathbb{E}|M_n|^p < \infty$ for some $p > 1$, then $M_n \to M_\infty$ a.s. and in $L^p$. Reason: $L^p$-boundedness with $p>1$ implies UI (hence a.s. and $L^1$ convergence), and Doob's maximal inequality gives the $L^p$ domination $\mathbb{E}[\sup_n |M_n|^p] \le (p/(p-1))^p \sup_n \mathbb{E}|M_n|^p$, so $L^p$ convergence follows by dominated convergence.

---

## Backward Martingales

A **backward martingale** $(M_n, \mathcal{F}_n)_{n\ge 1}$ satisfies $\mathcal{F}_n \supseteq \mathcal{F}_{n+1}$ and $\mathbb{E}[M_n \mid \mathcal{F}_{n+1}] = M_{n+1}$: as $n$ grows, information *shrinks*.

!!! success "Backward convergence"
    Every $L^1$-bounded backward martingale converges a.s. and in $L^1$ to $M_\infty = \mathbb{E}[M_1 \mid \mathcal{F}_\infty]$, where $\mathcal{F}_\infty = \bigcap_n \mathcal{F}_n$.

UI is automatic here: the sequence consists of conditional expectations of the single variable $M_1$.

!!! example "Strong law of large numbers"
    Let $X_i$ be i.i.d. with $\mathbb{E}|X_1| < \infty$ and mean $\mu$. Set $S_n = X_1 + \cdots + X_n$, $\bar X_n = S_n/n$, and $\mathcal{F}_n = \sigma(S_n, S_{n+1}, \ldots)$ (decreasing). By exchangeability, $\mathbb{E}[X_k \mid \mathcal{F}_{n+1}]$ is the same for all $k \le n+1$, so

    $$
    \mathbb{E}[\bar X_n \mid \mathcal{F}_{n+1}] = \bar X_{n+1},
    $$

    making $(\bar X_n)$ a backward martingale. Convergence gives $\bar X_n \to \mathbb{E}[X_1 \mid \mathcal{F}_\infty]$, and Kolmogorov's 0–1 law makes $\mathcal{F}_\infty$ trivial, yielding $\bar X_n \to \mu$ a.s. and in $L^1$.

---

## Continuous Time

For right-continuous martingales $(M_t)_{t \ge 0}$ with $\sup_t \mathbb{E}|M_t| < \infty$, the same conclusions hold: $M_\infty := \lim_{t\to\infty} M_t$ exists a.s. and is finite. If $(M_t)$ is UI, convergence is also in $L^1$ and $M_t = \mathbb{E}[M_\infty \mid \mathcal{F}_t]$. Doob's regularization theorem provides a càdlàg modification whenever the filtration satisfies the usual conditions.

!!! example "Three behaviors to remember"

    - **Lévy martingale** $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$: UI, so $M_t \to X$ a.s. and in $L^1$.
    - **Exponential martingale** $Z_t = \exp(\theta W_t - \theta^2 t/2)$, $\theta \ne 0$: $\mathbb{E}[Z_t] = 1$ but $Z_t \to 0$ a.s. Not UI.
    - **Simple random walk** $S_n$: $\mathbb{E}[S_n^2] = n \to \infty$, not $L^1$-bounded, does not converge a.s.

---

## Optional Sampling at Infinity

UI bridges optional sampling and convergence: for a UI martingale $(M_n)$ and any stopping time $\tau$ (possibly infinite),

$$
M_\tau = \mathbb{E}[M_\infty \mid \mathcal{F}_\tau] \quad \text{and} \quad \mathbb{E}[M_\tau] = \mathbb{E}[M_0].
$$

This extends the bounded optional sampling theorem — already established for bounded stopping times — to the unbounded case, using $L^1$ convergence to pass to the limit $\tau \wedge k \to \tau$.

---

## The Convergence Hierarchy

| Hypothesis | a.s. | $L^1$ | $L^p$, $p>1$ |
|---|---|---|---|
| $L^1$-bounded | yes | no (need UI) | — |
| UI | yes | yes | — |
| $L^p$-bounded, $p>1$ | yes | yes | yes |
| Closed: $M_n = \mathbb{E}[X\mid\mathcal{F}_n]$ | yes | yes | iff $X \in L^p$ |

A.s. convergence comes from $L^1$-boundedness alone (upcrossings). $L^1$ convergence requires UI, which is equivalent to closure. $L^p$-boundedness with $p>1$ is strictly stronger and yields $L^p$ convergence. Backward martingales always close automatically.

---

## Exercises

**Exercise 1.** Let $(M_n)$ be a submartingale with $\sup_n \mathbb{E}[M_n^+] < \infty$. Prove $M_n$ converges a.s.

??? success "Solution to Exercise 1"
    For each rational $a < b$, Doob's upcrossing inequality gives

    $$
    \mathbb{E}[U_\infty^{[a,b]}] \le \frac{\sup_n \mathbb{E}[(M_n - a)^+]}{b-a} \le \frac{\sup_n \mathbb{E}[M_n^+] + |a|}{b-a} < \infty,
    $$

    so $U_\infty^{[a,b]} < \infty$ a.s. The union over rational pairs is still a null set, so $\liminf M_n = \limsup M_n$ a.s. For finiteness, note $\mathbb{E}[M_n^-] = \mathbb{E}[M_n^+] - \mathbb{E}[M_n] \le \mathbb{E}[M_n^+] - \mathbb{E}[M_0]$ (submartingale means $\mathbb{E}[M_n] \ge \mathbb{E}[M_0]$), so $\sup_n \mathbb{E}|M_n| < \infty$ and Markov's inequality forces the limit to be finite. $\square$

---

**Exercise 2.** Show directly that $Z_t = e^{W_t - t/2}$ is not uniformly integrable.

??? success "Solution to Exercise 2"
    $Z_t$ is a martingale, so $\mathbb{E}[Z_t] = 1$. By the law of the iterated logarithm, $W_t/t \to 0$ a.s., so $\log Z_t = W_t - t/2 \to -\infty$ a.s., giving $Z_t \to 0$ a.s. If $(Z_t)$ were UI, Vitali would force $\mathbb{E}[Z_t] \to \mathbb{E}[0] = 0$, contradicting $\mathbb{E}[Z_t] = 1$. $\square$

---

**Exercise 3.** Let $X_i$ be i.i.d. with mean $\mu$ and $\mathbb{E}|X_1| < \infty$, $\bar X_n = n^{-1}\sum_{k=1}^n X_k$, and $\mathcal{F}_n = \sigma(S_n, S_{n+1}, \ldots)$. Show $(\bar X_n, \mathcal{F}_n)$ is a backward martingale and deduce the SLLN.

??? success "Solution to Exercise 3"
    The filtration is decreasing since functions of $(S_{n+1}, S_{n+2}, \ldots)$ are functions of $(S_n, S_{n+1}, \ldots)$. Given $\mathcal{F}_{n+1}$, the summands $X_1, \ldots, X_{n+1}$ are exchangeable by the i.i.d. assumption, so $\mathbb{E}[X_k \mid \mathcal{F}_{n+1}]$ does not depend on $k$. Summing yields $(n+1)\mathbb{E}[X_k \mid \mathcal{F}_{n+1}] = S_{n+1}$, so each equals $\bar X_{n+1}$. Then

    $$
    \mathbb{E}[\bar X_n \mid \mathcal{F}_{n+1}] = \tfrac{1}{n}\mathbb{E}[S_{n+1} - X_{n+1} \mid \mathcal{F}_{n+1}] = \tfrac{1}{n}\bigl(S_{n+1} - \bar X_{n+1}\bigr) = \bar X_{n+1}.
    $$

    Backward convergence gives $\bar X_n \to \mathbb{E}[X_1 \mid \mathcal{F}_\infty]$ a.s. and in $L^1$. Since $\mathcal{F}_\infty \subseteq \bigcap_n \sigma(X_n, X_{n+1}, \ldots)$, Kolmogorov's 0–1 law makes $\mathcal{F}_\infty$ trivial and the limit equals $\mu$. $\square$

---

**Exercise 4.** Show that $L^p$-boundedness with $p > 1$ implies UI. Deduce that an $L^p$-bounded martingale converges in $L^p$.

??? success "Solution to Exercise 4"
    For $p > 1$ and $C = \sup_\alpha \mathbb{E}|X_\alpha|^p$,

    $$
    \mathbb{E}[|X_\alpha|\,\mathbf{1}_{\{|X_\alpha|>K\}}] \le \frac{1}{K^{p-1}}\mathbb{E}[|X_\alpha|^p] \le \frac{C}{K^{p-1}} \to 0
    $$

    as $K \to \infty$, uniformly in $\alpha$; so the family is UI. For a martingale $(M_n)$, Doob's maximal inequality gives $\mathbb{E}[\sup_n |M_n|^p] \le (p/(p-1))^p \,C < \infty$. Combined with a.s. convergence $M_n \to M_\infty$ (from $L^1$-boundedness), dominated convergence yields $\mathbb{E}|M_n - M_\infty|^p \to 0$. $\square$

---

**Exercise 5.** Let $(M_t)$ be a UI martingale with limit $M_\infty$ and $\tau$ any stopping time. Prove $M_\tau = \mathbb{E}[M_\infty \mid \mathcal{F}_\tau]$ a.s.

??? success "Solution to Exercise 5"
    Let $\tau_k = \tau \wedge k$, a bounded stopping time. Bounded optional sampling applied to the closed martingale $M_n = \mathbb{E}[M_\infty \mid \mathcal{F}_n]$ gives $M_{\tau_k} = \mathbb{E}[M_\infty \mid \mathcal{F}_{\tau_k}]$. For $A \in \mathcal{F}_\tau \subseteq \mathcal{F}_{\tau_k}$,

    $$
    \mathbb{E}[M_{\tau_k}\mathbf{1}_A] = \mathbb{E}[M_\infty \mathbf{1}_A].
    $$

    Since $\tau_k \to \tau$ a.s. and $M$ converges a.s., $M_{\tau_k} \to M_\tau$ a.s. UI of $(M_n)$ carries over to $(M_{\tau_k})$ (it is bounded by the Doob maximal $L^1$ process), so $M_{\tau_k} \to M_\tau$ in $L^1$. Passing to the limit: $\mathbb{E}[M_\tau \mathbf{1}_A] = \mathbb{E}[M_\infty \mathbf{1}_A]$ for all $A \in \mathcal{F}_\tau$, giving the claim. $\square$
