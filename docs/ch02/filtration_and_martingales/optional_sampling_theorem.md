# Optional Sampling Theorem

[Martingales](martingales.md) are fair games at deterministic times: $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$. What happens when we replace $s, t$ by random times $\sigma \le \tau$? The Optional Sampling Theorem answers precisely this question: when does $\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma$?

---

## The Bounded Case

**Theorem (Optional Sampling, bounded version).** Let $M$ be a right-continuous martingale and let $\sigma \le \tau \le T$ be [stopping times](stopping_times.md) with $T < \infty$. Then

$$
\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma \quad \text{a.s.}
$$

In particular $\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$.

*Proof (sketch).* Approximate $\tau$ from above by discrete stopping times $\tau^{(n)} = \lceil 2^n \tau \rceil / 2^n$. On each atom $\{\tau^{(n)} = k/2^n\}$ the martingale property is a direct discrete-time calculation, so $M^{\tau^{(n)}}$ is a martingale. Right-continuity and the uniform bound $|M_{t \wedge \tau^{(n)}}| \le \sup_{u \le T} |M_u| \in L^1$ let us pass $n \to \infty$ by dominated convergence, giving the result for $\sigma \le \tau \le T$. $\square$

---

## Why Boundedness Matters

!!! warning "Counterexample: symmetric random walk"
    Let $S_n$ be a symmetric simple random walk ($S_0 = 0$) and $\tau = \inf\{n : S_n = 1\}$. Then $S_n$ is a martingale and $\mathbb{P}(\tau < \infty) = 1$, yet
    
    $$
    \mathbb{E}[S_\tau] = 1 \ne 0 = \mathbb{E}[S_0].
    $$
    
    The culprit is $\mathbb{E}[\tau] = \infty$. With no bound on $\tau$ and no integrability control, the "fair game" identity fails.

---

## Sufficient Conditions Beyond Bounded τ

The following each suffice for $\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma$ on (possibly unbounded) stopping times $\sigma \le \tau$:

| Condition | Setting |
|---|---|
| $\tau \le T$ bounded | always |
| $M$ uniformly integrable | general |
| $|M_{t \wedge \tau}| \le Y$ with $Y \in L^1$ | general |
| bounded increments and $\mathbb{E}[\tau] < \infty$ | discrete time |

Each reduces to the bounded case via a truncation $\tau \wedge T$ followed by $T \to \infty$.

---

## The Application Template

Optional sampling is a workhorse. The recipe:

1. **Pick a martingale** encoding the quantity of interest. Standard choices for Brownian motion:
   - $W_t$ itself,
   - $W_t^2 - t$,
   - the exponential martingale $\exp(\theta W_t - \theta^2 t / 2)$.
2. **Pick a stopping time** $\tau$ (typically a hitting or exit time).
3. **Apply optional sampling to** $\tau \wedge T$: $\mathbb{E}[M_{\tau \wedge T}] = \mathbb{E}[M_0]$.
4. **Pass $T \to \infty$** (dominated/monotone/Fatou), and read off the answer.

---

## Three Canonical Applications

**1. Hitting probability.** For $W_0 = x \in (a, b)$ and $\tau = \inf\{t : W_t \notin (a, b)\}$, the bounded martingale $W_{t \wedge \tau}$ gives $\mathbb{E}[W_\tau] = x$. Writing $p = \mathbb{P}(W_\tau = b)$, we get $bp + a(1-p) = x$, hence

$$
\mathbb{P}(\text{hit } b \text{ before } a \mid W_0 = x) = \frac{x - a}{b - a}.
$$

**2. Expected exit time.** For $\tau = \inf\{t : W_t \notin (-a, a)\}$, apply optional sampling to $W_t^2 - t$ at $\tau \wedge T$ and let $T \to \infty$. Since $|W_\tau| = a$,

$$
\mathbb{E}[\tau] = \mathbb{E}[W_\tau^2] = a^2.
$$

**3. Laplace transform of a hitting time.** For $\tau_a = \inf\{t : W_t = a\}$ with $a > 0$, apply optional sampling to $Z_t = \exp(\sqrt{2\lambda}\,W_t - \lambda t)$ at $\tau_a \wedge T$. On $\{\tau_a < \infty\}$, $W_{\tau_a} = a$, and as $T \to \infty$ the contribution from $\{\tau_a > T\}$ vanishes. The result is

$$
\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}.
$$

This is the Laplace transform of the inverse Gaussian distribution.

---

## Sub/Supermartingale Version

If $X$ is a supermartingale and $\sigma \le \tau \le T$ are bounded,

$$
\mathbb{E}[X_\tau \mid \mathcal{F}_\sigma] \le X_\sigma,
$$

with the inequality reversed for submartingales. In particular, $|M|$ (submartingale) satisfies $\mathbb{E}[|M_\tau|] \ge \mathbb{E}[|M_\sigma|]$.

---

## Exercises

**Exercise 1.** Let $\tau = \inf\{t : W_t \notin (-1, 1)\}$.

(a) Find $\mathbb{E}[W_\tau]$ using optional sampling.
(b) Find $\mathbb{E}[\tau]$.
(c) Find $\mathbb{P}(W_\tau = 1)$.

??? success "Solution to Exercise 1"
    **(a)** $W_{t \wedge \tau}$ is bounded by $1$, so optional sampling gives $\mathbb{E}[W_\tau] = W_0 = 0$.

    **(b)** Apply optional sampling to $M_t = W_t^2 - t$ at $\tau \wedge T$:
    
    $$
    \mathbb{E}[W_{\tau \wedge T}^2] = \mathbb{E}[\tau \wedge T].
    $$
    
    As $T \to \infty$, monotone convergence gives $\mathbb{E}[\tau]$ on the right, and bounded convergence gives $\mathbb{E}[W_\tau^2] = 1$ on the left. Hence $\mathbb{E}[\tau] = 1$.

    **(c)** By symmetry (or from (a)): $2p - 1 = 0$, so $p = 1/2$.

---

**Exercise 2 (Gambler's ruin).** A gambler starts with \$$k$ and bets \$$1$ per fair coin flip, stopping at $0$ or $N$.

(a) Find the probability of reaching $N$.
(b) Find the expected number of bets.

??? success "Solution to Exercise 2"
    Let $S_n$ be wealth and $\tau$ the exit time from $\{0, \ldots, N\}$.

    **(a)** $S_n$ is a bounded martingale on $[0, \tau]$. Optional sampling: $\mathbb{E}[S_\tau] = k$. With $p_k = \mathbb{P}(S_\tau = N)$,
    
    $$
    N p_k = k \implies p_k = k/N.
    $$

    **(b)** $S_n^2 - n$ is a martingale. Optional sampling: $\mathbb{E}[S_\tau^2] = k^2 + \mathbb{E}[\tau]$. Also $\mathbb{E}[S_\tau^2] = N^2 \cdot (k/N) = kN$. Therefore $\mathbb{E}[\tau] = k(N - k)$.

---

**Exercise 3 (Wald's identities).** Let $S_n = \sum_{i=1}^n X_i$ with $X_i$ i.i.d., $\mathbb{E}[X_1] = 0$, $\mathrm{Var}(X_1) = \sigma^2$, and let $\tau$ be a stopping time with $\mathbb{E}[\tau] < \infty$.

(a) Prove $\mathbb{E}[S_\tau] = 0$.
(b) Prove $\mathbb{E}[S_\tau^2] = \sigma^2 \mathbb{E}[\tau]$.

??? success "Solution to Exercise 3"
    **(a)** $S_n$ is a martingale with integrable increments; $\mathbb{E}[\tau] < \infty$ gives the discrete bounded-increments optional sampling criterion, so $\mathbb{E}[S_\tau] = \mathbb{E}[S_0] = 0$.

    **(b)** $M_n = S_n^2 - n\sigma^2$ is a martingale:
    
    $$
    \mathbb{E}[S_{n+1}^2 \mid \mathcal{F}_n] = S_n^2 + \sigma^2.
    $$
    
    Optional sampling gives $\mathbb{E}[S_\tau^2] = \sigma^2 \mathbb{E}[\tau]$.

---

**Exercise 4 (Hitting time Laplace transform).** Let $\tau_a = \inf\{t : W_t = a\}$, $a > 0$.

(a) Use optional sampling on $Z_t = \exp(\sqrt{2\lambda}\,W_t - \lambda t)$ to show $\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}$.
(b) Deduce $\mathbb{E}[\tau_a] = \infty$ even though $\mathbb{P}(\tau_a < \infty) = 1$.

??? success "Solution to Exercise 4"
    **(a)** On $\tau_a \wedge T$, $Z$ is bounded by $e^{a\sqrt{2\lambda}}$, so $\mathbb{E}[Z_{\tau_a \wedge T}] = 1$. On $\{\tau_a > T\}$, $Z_T \to 0$ a.s. as $T \to \infty$ (since $W_T = o(T)$), and $\mathbb{P}(\tau_a < \infty) = 1$. Passing to the limit,
    
    $$
    \mathbb{E}[e^{\sqrt{2\lambda} \cdot a - \lambda \tau_a}] = 1 \implies \mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}.
    $$

    **(b)** $\mathbb{E}[\tau_a] = -\partial_\lambda \mathbb{E}[e^{-\lambda \tau_a}]\big|_{\lambda \to 0^+} = a/\sqrt{2\lambda}\big|_{\lambda \to 0^+} = \infty$.

---

**Exercise 5 (Two-sided exit).** Let $\tau = \inf\{t : W_t \notin (-a, b)\}$ with $a, b > 0$ and $W_0 = 0$.

(a) Find $\mathbb{P}(W_\tau = b)$.
(b) Find $\mathbb{E}[\tau]$.

??? success "Solution to Exercise 5"
    **(a)** By optional sampling on $W$: $b p - a(1-p) = 0$, so $p = a/(a + b)$.

    **(b)** By optional sampling on $W_t^2 - t$: $\mathbb{E}[\tau] = \mathbb{E}[W_\tau^2] = b^2 \cdot \frac{a}{a+b} + a^2 \cdot \frac{b}{a+b} = ab$.

---

**Exercise 6 (Why the counterexample fails).** Let $S_n$ be a symmetric simple random walk and $\tau = \inf\{n : S_n = 1\}$. Explain *which* hypothesis of optional sampling fails for this $\tau$, and why optional sampling *does* hold for $\tau_N = \tau \wedge N$ for every finite $N$.

??? success "Solution to Exercise 6"
    For the unbounded $\tau$: $\mathbb{P}(\tau < \infty) = 1$ but $\mathbb{E}[\tau] = \infty$ (and $S$ is not UI on $[0, \tau]$). None of the sufficient conditions apply, so $\mathbb{E}[S_\tau] \ne \mathbb{E}[S_0]$ is possible — and indeed $\mathbb{E}[S_\tau] = 1$.

    For the truncation $\tau_N = \tau \wedge N$: this is bounded by $N$, so the bounded-case theorem applies and $\mathbb{E}[S_{\tau_N}] = 0$ for every finite $N$. The limit $N \to \infty$ is where things break: $S_{\tau_N} \to S_\tau = 1$ a.s., but $\{S_{\tau_N}\}_N$ is not uniformly integrable, so expectations do not pass to the limit.
