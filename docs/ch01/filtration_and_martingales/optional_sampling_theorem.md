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

Decompose based on whether $\tau \le s$:

$$
M_{t \wedge \tau} = M_\tau \mathbf{1}_{\{\tau \le s\}} + M_{t \wedge \tau} \mathbf{1}_{\{\tau > s\}}
$$

On $\{\tau \le s\}$: $M_{t \wedge \tau} = M_\tau = M_{s \wedge \tau}$, so conditioning gives $M_{s \wedge \tau}$.

On $\{\tau > s\}$: $s \wedge \tau = s$, and we use the martingale property carefully. The technical details involve approximating by discrete stopping times.

**Step 2**: Apply to bounded stopping times.

Since $\tau \le T$, evaluate the stopped martingale at time $T$:

$$
\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = \mathbb{E}[M_{T \wedge \tau} \mid \mathcal{F}_\sigma] = M_{\sigma \wedge \tau} = M_\sigma
$$

where the last equality uses $\sigma \le \tau$. $\square$

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

### Condition 3: $L^p$ Bound with Stopping Time Moment

**Theorem**: If $\sup_t \mathbb{E}|M_t|^p < \infty$ for some $p > 1$ and $\mathbb{E}[\tau^{p/(2(p-1))}] < \infty$, then optional sampling holds.

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

### Exercise 2: Gambler's Ruin

A gambler starts with $\$k$ and bets $\$1$ on each fair coin flip. They stop when they reach $\$0$ or $\$N$.

(a) Model this as a martingale problem and find the probability of reaching $\$N$.

(b) Find the expected number of bets.

(c) Generalize to an unfair coin with $\mathbb{P}(\text{heads}) = p \neq 1/2$.

### Exercise 3: Wald's Identities

Let $S_n = \sum_{k=1}^n X_k$ where $X_k$ are i.i.d. with $\mathbb{E}[X_1] = 0$ and $\text{Var}(X_1) = \sigma^2$. Let $\tau$ be a stopping time with $\mathbb{E}[\tau] < \infty$.

(a) Prove Wald's first identity: $\mathbb{E}[S_\tau] = 0$.

(b) Prove Wald's second identity: $\mathbb{E}[S_\tau^2] = \sigma^2 \mathbb{E}[\tau]$.

(c) Apply these to the symmetric random walk stopped at $\pm a$.

### Exercise 4: Laplace Transform of Hitting Times

Let $\tau_a = \inf\{t : W_t = a\}$ for $a > 0$.

(a) Apply optional sampling to $\exp(\theta W_t - \frac{\theta^2 t}{2})$ with $\theta = \sqrt{2\lambda}$ to derive $\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}$.

(b) Invert the Laplace transform to find the density of $\tau_a$.

(c) Show that $\mathbb{E}[\tau_a] = \infty$ despite $\mathbb{P}(\tau_a < \infty) = 1$.

### Exercise 5: First Passage with Drift

Let $X_t = W_t + \mu t$ (Brownian motion with drift $\mu > 0$). Let $\tau_a = \inf\{t : X_t = a\}$ for $a > 0$.

(a) Find a martingale involving $X_t$ by exponential tilting.

(b) Use optional sampling to find $\mathbb{E}[e^{-\lambda \tau_a}]$.

(c) Find $\mathbb{P}(\tau_a < \infty)$ for $\mu < 0$.

### Exercise 6: Two-Sided Exit

Let $\tau = \inf\{t : W_t \notin (-a, b)\}$ where $a, b > 0$.

(a) Find $\mathbb{P}(W_\tau = b)$.

(b) Find $\mathbb{E}[\tau]$.

(c) Find $\mathbb{E}[e^{-\lambda \tau}]$.
