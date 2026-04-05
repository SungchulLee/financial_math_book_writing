# Optional Sampling Theorem

## The Central Question

The martingale property states that $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for deterministic times $s \le t$. But what happens when we evaluate a martingale at **random times**?

If $\sigma \le \tau$ are stopping times, does the martingale property extend to:

$$
\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma \quad ?
$$

The answer is: **yes, but with conditions**. The Optional Sampling Theorem (also called the Optional Stopping Theorem) provides the precise circumstances under which this holds.

---

## The Bounded Case

**Theorem (Optional Sampling — Bounded Version)**: Let $\{M_t\}_{t \ge 0}$ be a right-continuous martingale with respect to $(\mathcal{F}_t)$. Let $\sigma$ and $\tau$ be stopping times with:

$$
0 \le \sigma \le \tau \le T \quad \text{almost surely}
$$

for some constant $T < \infty$. Then:

$$
\boxed{\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma \quad \text{a.s.}}
$$

In particular:

$$
\boxed{\mathbb{E}[M_\tau] = \mathbb{E}[M_\sigma] = \mathbb{E}[M_0]}
$$

**Interpretation**: For bounded stopping times, the "fair game" property persists. On average, stopping at a random time gives the same expected value as the starting value.

---

## Proof of the Bounded Case

**Step 1**: Show that the stopped process $M_t^\tau = M_{t \wedge \tau}$ is a martingale.

For $s \le t$, we need $\mathbb{E}[M_{t \wedge \tau} \mid \mathcal{F}_s] = M_{s \wedge \tau}$.

The key idea is to approximate $\tau$ by discrete stopping times. For each $n$, define:
$$
\tau^{(n)} = \frac{\lceil 2^n \tau \rceil}{2^n}
$$
(the smallest multiple of $2^{-n}$ that is $\ge \tau$). Each $\tau^{(n)}$ takes values in $\{k/2^n : k = 0, 1, 2, \ldots\} \cup \{\infty\}$ and is a stopping time. The stopped process $M_{t \wedge \tau^{(n)}}$ satisfies the martingale property by a direct verification on each atom $\{\tau^{(n)} = k/2^n\}$.

As $n \to \infty$, $\tau^{(n)} \downarrow \tau$, and by right-continuity of paths $M_{t \wedge \tau^{(n)}} \to M_{t \wedge \tau}$ a.s. Dominated convergence (using the bound $|M_{t \wedge \tau^{(n)}}| \le \sup_{u \le T} |M_u| \in L^1$ for bounded $\tau \le T$) justifies passing to the limit in the martingale property.

**Step 2**: Apply to bounded stopping times.

Since $\tau \le T$, evaluate the stopped martingale at time $T$:

$$
\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = \mathbb{E}[M_{T \wedge \tau} \mid \mathcal{F}_\sigma] = M_{\sigma \wedge \tau} = M_\sigma
$$

where the second equality uses that $M^{\tau}$ is a martingale (Step 1), and the last uses $\sigma \le \tau$. $\square$

---

## Why Boundedness Matters: Counterexamples

Without boundedness or other integrability conditions, optional sampling can fail spectacularly.

**Example 1 (Symmetric Random Walk)**: Let $S_n = \sum_{i=1}^n \xi_i$ where $\mathbb{P}(\xi_i = \pm 1) = 1/2$. Define:

$$
\tau = \inf\{n : S_n = 1\}
$$

Then $S_n$ is a martingale with $S_0 = 0$, and $\mathbb{P}(\tau < \infty) = 1$. But:

$$
\mathbb{E}[S_\tau] = \mathbb{E}[1] = 1 \neq 0 = \mathbb{E}[S_0]
$$

The problem: $\mathbb{E}[\tau] = \infty$, so the stopping time is unbounded.

**Example 2 (Doubling Strategy)**: Consider a gambler who doubles their bet after each loss until winning. The expected gain is positive, seemingly contradicting the fair game property. The resolution: this strategy requires unbounded capital and unbounded time—it's the unboundedness that breaks optional sampling.

**Example 3 (Brownian Motion)**: Let $\tau_a = \inf\{t : W_t = a\}$ for $a > 0$. Then $W_\tau = a$ almost surely, but:

$$
\mathbb{E}[W_{\tau_a}] = a \neq 0 = \mathbb{E}[W_0]
$$

Again, $\mathbb{E}[\tau_a] = \infty$ (the inverse Gaussian distribution has infinite mean).

---

## General Sufficient Conditions

Several conditions ensure optional sampling holds for unbounded stopping times:

### Condition 1: Uniform Integrability

**Theorem**: Let $M$ be a UI martingale. Then for any stopping times $\sigma \le \tau$ (possibly unbounded):

$$
\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma
$$

**Proof**: UI implies $M_t \to M_\infty$ in $L^1$. Apply bounded optional sampling to $\tau \wedge T$ and let $T \to \infty$. $\square$

### Condition 2: Dominated by Integrable Variable

**Theorem**: If $|M_{t \wedge \tau}| \le Y$ for all $t$ where $\mathbb{E}[Y] < \infty$, then $\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$.

### Condition 3: $L^p$ Bound with Finite Stopping Time Moment

**Theorem**: If $\sup_t \mathbb{E}|M_t|^p < \infty$ for some $p > 1$ and $\mathbb{E}[\tau] < \infty$, then optional sampling holds. (A stronger moment condition on $\tau$ yields optional sampling even in the non-$L^p$-bounded case; see Revuz–Yor, Chapter II.)

### Condition 4: Bounded Increments + Finite Mean

**Theorem (Wald's Identity Variant)**: If $M$ is a martingale with $|M_{n+1} - M_n| \le c$ a.s. and $\mathbb{E}[\tau] < \infty$, then $\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$.

---

## The Application Template

Optional sampling is a workhorse technique. Here is the standard recipe:

**Step 1**: Identify or construct a martingale $M_t$ relevant to the problem.

Common choices:

- $W_t$ (Brownian motion itself)
- $W_t^2 - t$ (compensated square)
- $\exp(\theta W_t - \frac{\theta^2 t}{2})$ (exponential martingale)
- Solutions to certain PDEs evaluated along paths

**Step 2**: Choose a stopping time $\tau$ encoding the quantity of interest.

Common choices:

- First hitting time $\tau_a = \inf\{t : W_t = a\}$
- Exit time from interval $\tau_{a,b} = \inf\{t : W_t \notin (a, b)\}$
- First passage time with specific conditions

**Step 3**: Apply optional sampling with truncation:

$$
\mathbb{E}[M_{\tau \wedge T}] = \mathbb{E}[M_0]
$$

**Step 4**: Justify passage to the limit $T \to \infty$.

Use dominated convergence, monotone convergence, or Fatou's lemma as appropriate.

**Step 5**: Extract the desired quantity.

The martingale identity often encodes the answer.

---

## Classic Applications

### Application 1: Hitting Probabilities

**Problem**: For Brownian motion starting at $x \in (a, b)$, find $\mathbb{P}(W_{\tau} = b)$ where $\tau = \inf\{t : W_t \notin (a, b)\}$.

**Solution**: $W_t$ is a bounded martingale on $[0, \tau]$ (since $W_t \in [a, b]$ for $t < \tau$). By optional sampling:

$$
\mathbb{E}[W_\tau] = x
$$

Let $p = \mathbb{P}(W_\tau = b)$. Then:

$$
b \cdot p + a \cdot (1-p) = x \implies p = \frac{x - a}{b - a}
$$

$$
\boxed{\mathbb{P}(\text{hit } b \text{ before } a \mid W_0 = x) = \frac{x - a}{b - a}}
$$

### Application 2: Expected Exit Time

**Problem**: Find $\mathbb{E}[\tau]$ where $\tau = \inf\{t : W_t \notin (-a, a)\}$.

**Solution**: Use the martingale $M_t = W_t^2 - t$.

Since $|W_t| \le a$ for $t < \tau$, we have $|M_t| \le a^2 + t$. With care:

$$
\mathbb{E}[M_{\tau \wedge T}] = \mathbb{E}[M_0] = 0
$$

As $T \to \infty$:

$$
\mathbb{E}[W_\tau^2] - \mathbb{E}[\tau] = 0
$$

Since $|W_\tau| = a$ (the process exits at the boundary):

$$
\mathbb{E}[\tau] = \mathbb{E}[W_\tau^2] = a^2
$$

$$
\boxed{\mathbb{E}[\tau_{(-a,a)}] = a^2}
$$

### Application 3: Laplace Transform of Hitting Time

**Problem**: Find $\mathbb{E}[e^{-\lambda \tau_a}]$ for $\tau_a = \inf\{t : W_t = a\}$, $a > 0$.

**Solution**: Use the exponential martingale with $\theta = \sqrt{2\lambda}$:

$$
Z_t = \exp\left(\sqrt{2\lambda} W_t - \lambda t\right)
$$

Apply optional sampling to $\tau_a \wedge T$. At $\tau_a$, $W_{\tau_a} = a$, so:

$$
Z_{\tau_a} = \exp\left(\sqrt{2\lambda} \cdot a - \lambda \tau_a\right)
$$

With justification for $T \to \infty$:

$$
\mathbb{E}[Z_{\tau_a}] = \mathbb{E}[Z_0] = 1
$$

$$
\mathbb{E}\left[\exp(-\lambda \tau_a)\right] = \exp\left(-a\sqrt{2\lambda}\right)
$$

$$
\boxed{\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}}
$$

This is the Laplace transform of the inverse Gaussian distribution.

---

## Optional Sampling for Sub/Supermartingales

**Theorem**: If $X$ is a supermartingale and $\sigma \le \tau \le T$ are bounded stopping times:

$$
\mathbb{E}[X_\tau \mid \mathcal{F}_\sigma] \le X_\sigma
$$

For submartingales, the inequality reverses.

**Application**: If $|M_t|$ is a submartingale (true for any martingale $M_t$):

$$
\mathbb{E}[|M_\tau|] \ge \mathbb{E}[|M_\sigma|]
$$

The expected absolute value can only increase at stopping times.

---

## Connection to PDEs

Optional sampling connects stochastic processes to partial differential equations.

**Theorem (Dynkin's Formula)**: If $u$ is $C^2$ and $X_t$ is a diffusion with generator $\mathcal{L}$, then:

$$
u(X_t) - u(X_0) - \int_0^t \mathcal{L}u(X_s) \, ds
$$

is a local martingale. If $\mathcal{L}u = 0$ (i.e., $u$ is harmonic), then $u(X_t)$ is a local martingale.

**Consequence**: For Brownian motion ($\mathcal{L} = \frac{1}{2}\Delta$), if $u$ is harmonic on domain $D$:

$$
u(x) = \mathbb{E}^x[u(W_\tau)]
$$

where $\tau$ is the exit time from $D$. This is the **probabilistic solution to the Dirichlet problem**.

---

## Summary

The Optional Sampling Theorem:

$$
\boxed{\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma}
$$

holds when:

| Condition | Applicability |
|-----------|---------------|
| $\tau \le T$ bounded | Always works |
| $(M_t)$ uniformly integrable | Unbounded $\tau$ OK |
| $|M_t|$ dominated by integrable r.v. | Unbounded $\tau$ OK |
| Bounded increments + $\mathbb{E}[\tau] < \infty$ | Discrete time |

**Failure modes**: Unbounded stopping times without integrability control lead to counterexamples (doubling strategy, first passage times with infinite mean).

**Power**: Optional sampling transforms martingale identities into computational tools for hitting probabilities, expected hitting times, Laplace transforms, and boundary value problems.

---

## Exercises

### Exercise 1: Bounded Stopping Times

Let $\tau = \inf\{t : W_t \notin (-1, 1)\}$.

(a) Apply the optional sampling theorem to $W_t$ to find $\mathbb{E}[W_\tau]$.

(b) Apply optional sampling to $W_t^2 - t$ to find $\mathbb{E}[\tau]$.

(c) Find $\mathbb{P}(W_\tau = 1)$.

??? success "Solution to Exercise 1"
    Let $\tau = \inf\{t : W_t \notin (-1, 1)\}$.

    **(a)** The stopped process $W_{t \wedge \tau}$ is bounded: $|W_{t \wedge \tau}| \le 1$. By optional sampling for bounded stopping times (since $W_\tau$ exists and $|W_\tau| = 1$ a.s.):

    $$
    \mathbb{E}[W_\tau] = \mathbb{E}[W_0] = 0
    $$

    **(b)** The process $M_t = W_t^2 - t$ is a martingale. Apply optional sampling to $M_{\tau \wedge T}$:

    $$
    \mathbb{E}[W_{\tau \wedge T}^2 - (\tau \wedge T)] = \mathbb{E}[M_0] = 0
    $$

    Since $|W_{\tau \wedge T}| \le 1$, we have $W_{\tau \wedge T}^2 \le 1$. As $T \to \infty$, $\tau \wedge T \to \tau$ a.s. (since $\tau < \infty$ a.s. for exit from a bounded interval), $W_{\tau \wedge T}^2 \to W_\tau^2 = 1$ a.s., and $\tau \wedge T \uparrow \tau$. By monotone convergence for $\tau \wedge T$ and bounded convergence for $W_{\tau \wedge T}^2$:

    $$
    \mathbb{E}[W_\tau^2] - \mathbb{E}[\tau] = 0 \implies \mathbb{E}[\tau] = \mathbb{E}[W_\tau^2] = 1
    $$

    **(c)** Let $p = \mathbb{P}(W_\tau = 1)$. By symmetry of Brownian motion (reflecting $W \to -W$), $\mathbb{P}(W_\tau = 1) = \mathbb{P}(W_\tau = -1)$. Since $W_\tau \in \{-1, 1\}$:

    $$
    p + (1 - p) = 1 \quad \text{and} \quad p = 1 - p \implies p = \frac{1}{2}
    $$

    Alternatively, from (a): $\mathbb{E}[W_\tau] = 1 \cdot p + (-1)(1 - p) = 2p - 1 = 0$, giving $p = 1/2$.

---

### Exercise 2: Gambler's Ruin

A gambler starts with $\$k$ and bets $\$1$ on each fair coin flip. They stop when they reach $\$0$ or $\$N$.

(a) Model this as a martingale problem and find the probability of reaching $\$N$.

(b) Find the expected number of bets.

(c) Generalize to an unfair coin with $\mathbb{P}(\text{heads}) = p \neq 1/2$.

??? success "Solution to Exercise 2"
    **(a)** Let $S_n$ be the gambler's wealth, starting at $S_0 = k$, with absorbing barriers at 0 and $N$. For a fair coin ($p = 1/2$), $S_n$ is a martingale.

    Let $\tau = \inf\{n : S_n = 0 \text{ or } S_n = N\}$. The stopped martingale $S_{n \wedge \tau}$ is bounded ($0 \le S_{n \wedge \tau} \le N$). By optional sampling:

    $$
    \mathbb{E}[S_\tau] = \mathbb{E}[S_0] = k
    $$

    Let $p_k = \mathbb{P}(S_\tau = N)$. Then $N \cdot p_k + 0 \cdot (1 - p_k) = k$, so:

    $$
    p_k = \frac{k}{N}
    $$

    **(b)** Apply optional sampling to the martingale $M_n = S_n^2 - n$ (here $S_n - k$ is a martingale with zero mean increments of variance 1, so $(S_n - k)^2 - n$ is a martingale, equivalently $S_n^2 - 2kS_n + k^2 - n$ is a martingale). Actually, more directly: since the increments $\xi_i$ have mean 0 and variance 1, $S_n^2 - n$ is a submartingale. For the compensated process: $S_n^2 - n = (S_0 + \sum \xi_i)^2 - n$. The martingale is $M_n = S_n^2 - n$.

    $$
    \mathbb{E}[S_\tau^2 - \tau] = \mathbb{E}[S_0^2 - 0] = k^2
    $$

    $$
    \mathbb{E}[S_\tau^2] = N^2 \cdot \frac{k}{N} + 0 \cdot \frac{N - k}{N} = kN
    $$

    Therefore $\mathbb{E}[\tau] = \mathbb{E}[S_\tau^2] - k^2 = kN - k^2 = k(N - k)$.

    **(c)** For $p \neq 1/2$, $S_n$ is not a martingale. Use the martingale $M_n = (q/p)^{S_n}$ where $q = 1 - p$.

    $$
    \mathbb{E}[M_\tau] = M_0 = (q/p)^k
    $$

    $$
    (q/p)^N \cdot p_k + (q/p)^0 \cdot (1 - p_k) = (q/p)^k
    $$

    $$
    p_k = \frac{(q/p)^k - 1}{(q/p)^N - 1}
    $$

---

### Exercise 3: Wald's Identities

Let $S_n = \sum_{k=1}^n X_k$ where $X_k$ are i.i.d. with $\mathbb{E}[X_1] = 0$ and $\text{Var}(X_1) = \sigma^2$. Let $\tau$ be a stopping time with $\mathbb{E}[\tau] < \infty$.

(a) Prove Wald's first identity: $\mathbb{E}[S_\tau] = 0$.

(b) Prove Wald's second identity: $\mathbb{E}[S_\tau^2] = \sigma^2 \mathbb{E}[\tau]$.

(c) Apply these to the symmetric random walk stopped at $\pm a$.

??? success "Solution to Exercise 3"
    **(a)** Since $\mathbb{E}[X_k] = 0$, $S_n$ is a martingale. The increments $|X_k|$ are i.i.d. with $\mathbb{E}[\tau] < \infty$. By Wald's first identity (optional sampling for martingales with bounded increments and $\mathbb{E}[\tau] < \infty$, which can be justified since $|S_{n+1} - S_n| = |X_{n+1}|$ is integrable):

    $$
    \mathbb{E}[S_\tau] = \mathbb{E}[S_0] = 0 \quad \square
    $$

    More precisely: $\mathbb{E}[S_{\tau \wedge n}] = 0$ for all $n$. Since $|S_{\tau \wedge n}| \le |S_\tau| + \max_{k \le \tau} |X_k|$ and $\mathbb{E}[\tau] < \infty$ ensures the dominated convergence argument works (via Wald's equation), $\mathbb{E}[S_\tau] = \lim_n \mathbb{E}[S_{\tau \wedge n}] = 0$.

    **(b)** The process $M_n = S_n^2 - n\sigma^2$ is a martingale (verify: $\mathbb{E}[S_{n+1}^2 - (n+1)\sigma^2 \mid \mathcal{F}_n] = S_n^2 + \sigma^2 - (n+1)\sigma^2 = S_n^2 - n\sigma^2$). By optional sampling:

    $$
    \mathbb{E}[S_\tau^2 - \tau\sigma^2] = \mathbb{E}[M_0] = 0
    $$

    Therefore $\mathbb{E}[S_\tau^2] = \sigma^2 \mathbb{E}[\tau]$. $\square$

    **(c)** For the symmetric random walk ($\sigma^2 = 1$) stopped at $\pm a$:

    - By Wald's first identity: $\mathbb{E}[S_\tau] = 0$ (consistent with symmetry: $\mathbb{P}(S_\tau = a) = \mathbb{P}(S_\tau = -a) = 1/2$).

    - By Wald's second identity: $\mathbb{E}[S_\tau^2] = \mathbb{E}[\tau]$. Since $|S_\tau| = a$ (the walk exits at $\pm a$), $\mathbb{E}[S_\tau^2] = a^2$, so $\mathbb{E}[\tau] = a^2$.

---

### Exercise 4: Laplace Transform of Hitting Times

Let $\tau_a = \inf\{t : W_t = a\}$ for $a > 0$.

(a) Apply optional sampling to $\exp(\theta W_t - \frac{\theta^2 t}{2})$ with $\theta = \sqrt{2\lambda}$ to derive $\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}$.

(b) Invert the Laplace transform to find the density of $\tau_a$.

(c) Show that $\mathbb{E}[\tau_a] = \infty$ despite $\mathbb{P}(\tau_a < \infty) = 1$.

??? success "Solution to Exercise 4"
    **(a)** Apply optional sampling to $Z_t = \exp(\sqrt{2\lambda}\,W_t - \lambda t)$ at $\tau_a \wedge T$:

    $$
    \mathbb{E}[Z_{\tau_a \wedge T}] = \mathbb{E}[Z_0] = 1
    $$

    On $\{\tau_a \le T\}$: $Z_{\tau_a} = \exp(\sqrt{2\lambda} \cdot a - \lambda \tau_a)$.

    On $\{\tau_a > T\}$: $Z_T = \exp(\sqrt{2\lambda}\,W_T - \lambda T)$. As $T \to \infty$, $\exp(\sqrt{2\lambda}\,W_T - \lambda T) \to 0$ a.s. (since $W_T = o(T)$). Since $Z_{\tau_a \wedge T} \le e^{\sqrt{2\lambda} \cdot a}$ on $\{\tau_a \le T\}$ and $Z_T \ge 0$, by dominated convergence on $\{\tau_a \le T\}$ and the fact that $\mathbb{P}(\tau_a < \infty) = 1$:

    $$
    \mathbb{E}[\exp(\sqrt{2\lambda} \cdot a - \lambda \tau_a)] = 1
    $$

    Therefore:

    $$
    \mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}
    $$

    **(b)** The Laplace transform $\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}$ uniquely determines the distribution. By standard Laplace inversion (or lookup), this is the Laplace transform of the inverse Gaussian distribution with density:

    $$
    f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right), \quad t > 0
    $$

    **(c)** $\mathbb{E}[\tau_a] = -\frac{d}{d\lambda}\mathbb{E}[e^{-\lambda\tau_a}]\big|_{\lambda = 0^+} = -\frac{d}{d\lambda}e^{-a\sqrt{2\lambda}}\big|_{\lambda = 0^+} = a\sqrt{2} \cdot \frac{1}{2\sqrt{\lambda}} \cdot e^{-a\sqrt{2\lambda}}\big|_{\lambda = 0^+}$

    As $\lambda \to 0^+$, $\frac{1}{2\sqrt{\lambda}} \to \infty$, so $\mathbb{E}[\tau_a] = \infty$.

    Alternatively, from the density: $\mathbb{E}[\tau_a] = \int_0^\infty t \cdot \frac{a}{\sqrt{2\pi t^3}} e^{-a^2/(2t)}\,dt = \int_0^\infty \frac{a}{\sqrt{2\pi t}} e^{-a^2/(2t)}\,dt$. The substitution $u = a^2/(2t)$ gives $dt = -a^2/(2u^2)\,du$, and the integral diverges at $t \to \infty$ (equivalently $u \to 0$). $\square$

---

### Exercise 5: First Passage with Drift

Let $X_t = W_t + \mu t$ (Brownian motion with drift $\mu > 0$). Let $\tau_a = \inf\{t : X_t = a\}$ for $a > 0$.

(a) Find a martingale involving $X_t$ by exponential tilting.

(b) Use optional sampling to find $\mathbb{E}[e^{-\lambda \tau_a}]$.

(c) Find $\mathbb{P}(\tau_a < \infty)$ for $\mu < 0$.

??? success "Solution to Exercise 5"
    **(a)** Let $X_t = W_t + \mu t$ with $\mu > 0$. The exponential martingale for Brownian motion with drift is obtained by exponential tilting. Define:

    $$
    Z_t = \exp\left(\theta X_t - \left(\mu\theta + \frac{\theta^2}{2}\right)t\right) = \exp\left(\theta W_t + \theta\mu t - \mu\theta t - \frac{\theta^2}{2}t\right) = \exp\left(\theta W_t - \frac{\theta^2}{2}t\right)
    $$

    This is the standard exponential martingale for $W_t$. Alternatively, using the parameter $\alpha$ such that the exponent involves $X_t$: define $Z_t = \exp(\alpha X_t - \psi(\alpha)t)$ where $\psi(\alpha) = \mu\alpha + \alpha^2/2$. Then $Z_t = \exp(\alpha(W_t + \mu t) - (\mu\alpha + \alpha^2/2)t) = \exp(\alpha W_t - \alpha^2 t/2)$, which is indeed a martingale.

    **(b)** Set $\alpha = -\mu + \sqrt{\mu^2 + 2\lambda}$ (choosing the root so that $\psi(\alpha) = \lambda$, i.e., $\mu\alpha + \alpha^2/2 = \lambda$). Apply optional sampling to $Z_t = \exp(\alpha X_t - \lambda t)$ at $\tau_a$:

    $$
    \mathbb{E}[Z_{\tau_a}] = 1 \implies \mathbb{E}[\exp(\alpha a - \lambda\tau_a)] = 1
    $$

    $$
    \mathbb{E}[e^{-\lambda\tau_a}] = e^{-\alpha a} = \exp\left(-a(-\mu + \sqrt{\mu^2 + 2\lambda})\right) = \exp\left(a\mu - a\sqrt{\mu^2 + 2\lambda}\right)
    $$

    **(c)** For $\mu < 0$ and $a > 0$: $\mathbb{P}(\tau_a < \infty) = \lim_{\lambda \to 0^+} \mathbb{E}[e^{-\lambda\tau_a}]$ (by monotone convergence).

    $$
    \lim_{\lambda \to 0^+} \exp\left(a\mu - a\sqrt{\mu^2 + 2\lambda}\right) = \exp(a\mu - a|\mu|) = \exp(a\mu + a\mu) = e^{2a\mu}
    $$

    (using $|\mu| = -\mu$ since $\mu < 0$). Therefore:

    $$
    \mathbb{P}(\tau_a < \infty) = e^{2a\mu} < 1
    $$

    With negative drift, Brownian motion drifts to $-\infty$, and the probability of ever reaching level $a > 0$ is strictly less than 1.

---

### Exercise 6: Two-Sided Exit

Let $\tau = \inf\{t : W_t \notin (-a, b)\}$ where $a, b > 0$.

(a) Find $\mathbb{P}(W_\tau = b)$.

(b) Find $\mathbb{E}[\tau]$.

(c) Find $\mathbb{E}[e^{-\lambda \tau}]$.

??? success "Solution to Exercise 6"
    Let $\tau = \inf\{t : W_t \notin (-a, b)\}$ where $a, b > 0$ and $W_0 = 0$.

    **(a)** Apply optional sampling to $W_t$ (martingale, bounded on $[-a, b]$ before $\tau$):

    $$
    \mathbb{E}[W_\tau] = \mathbb{E}[W_0] = 0
    $$

    Let $p = \mathbb{P}(W_\tau = b)$. Then $b \cdot p + (-a)(1 - p) = 0$, giving:

    $$
    p = \frac{a}{a + b}
    $$

    **(b)** Apply optional sampling to $M_t = W_t^2 - t$:

    $$
    \mathbb{E}[W_\tau^2 - \tau] = 0 \implies \mathbb{E}[\tau] = \mathbb{E}[W_\tau^2]
    $$

    $$
    \mathbb{E}[W_\tau^2] = b^2 \cdot \frac{a}{a+b} + a^2 \cdot \frac{b}{a+b} = \frac{ab(b + a)}{a + b} = ab
    $$

    Therefore $\mathbb{E}[\tau] = ab$.

    **(c)** Apply optional sampling to $Z_t = \exp(\theta W_t - \theta^2 t/2)$ at $\tau \wedge T$, then let $T \to \infty$:

    $$
    \mathbb{E}[Z_\tau] = 1
    $$

    With $\theta = i\alpha$ (purely imaginary, taking the analytic continuation) or directly using $\theta = \sqrt{2\lambda}$:

    Setting $\theta^2/2 = \lambda$ (so $\theta = \sqrt{2\lambda}$):

    $$
    \mathbb{E}\left[e^{\sqrt{2\lambda} W_\tau - \lambda\tau}\right] = 1
    $$

    $$
    e^{\sqrt{2\lambda} \cdot b} \cdot \frac{a}{a+b} \cdot \mathbb{E}[e^{-\lambda\tau} \mid W_\tau = b] \cdot \text{(not quite...)}
    $$

    A cleaner approach: use both $\theta$ and $-\theta$. From $\mathbb{E}[e^{\theta W_\tau - \lambda\tau}] = 1$:

    $$
    e^{\theta b} \cdot p \cdot \mathbb{E}[e^{-\lambda\tau} \mid W_\tau = b] + e^{-\theta a} \cdot (1-p) \cdot \mathbb{E}[e^{-\lambda\tau} \mid W_\tau = -a] = 1
    $$

    Using both $\theta = \sqrt{2\lambda}$ and $\theta = -\sqrt{2\lambda}$ gives two equations. Let $\alpha = \sqrt{2\lambda}$, $L_+ = \mathbb{E}[e^{-\lambda\tau} \mid W_\tau = b]$, $L_- = \mathbb{E}[e^{-\lambda\tau} \mid W_\tau = -a]$:

    $$
    e^{\alpha b}\,p\,L_+ + e^{-\alpha a}(1-p)L_- = 1
    $$

    $$
    e^{-\alpha b}\,p\,L_+ + e^{\alpha a}(1-p)L_- = 1
    $$

    Solving and using $p = a/(a+b)$, $(1-p) = b/(a+b)$, one obtains:

    $$
    \mathbb{E}[e^{-\lambda\tau}] = \frac{\cosh(\alpha(b - a)/2)}{\cosh(\alpha(a + b)/2)} \cdot \frac{1}{?}
    $$

    The explicit result is:

    $$
    \mathbb{E}[e^{-\lambda\tau}] = \frac{1}{\cosh(\alpha a) + \frac{\sinh(\alpha a)}{\tanh(\alpha(a+b))} \cdot \ldots}
    $$

    More directly, the Laplace transform of the exit time from $(-a, b)$ starting at 0 is:

    $$
    \mathbb{E}[e^{-\lambda\tau}] = \frac{\cosh\left(\sqrt{2\lambda}\frac{b-a}{2}\right)}{\cosh\left(\sqrt{2\lambda}\frac{a+b}{2}\right)}
    $$

    This can be verified by noting it equals 1 when $\lambda = 0$ and satisfies the ODE $\frac{1}{2}u'' = \lambda u$ on $(-a, b)$ with boundary conditions $u(-a) = u(b) = 1$.
