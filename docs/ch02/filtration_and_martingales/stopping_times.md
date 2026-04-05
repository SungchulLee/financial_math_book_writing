# Stopping Times

## The Concept of Observable Random Times

In stochastic analysis, we frequently need to consider random times—moments when something happens. But not all random times are created equal. The concept of a **stopping time** captures precisely those random times that can be determined using only information available up to that moment.

Consider two scenarios:

1. "The first time the stock price exceeds \$100" — You can observe when this happens in real-time.
2. "The last time the stock price exceeds \$100 before it crashes" — You cannot know this until after the crash.

The first is a stopping time; the second is not. This distinction is fundamental to what strategies are implementable and what theorems apply.

---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space.

A random variable $\tau: \Omega \to [0, \infty]$ is a **stopping time** (or **optional time**) with respect to $(\mathcal{F}_t)$ if:

$$
\boxed{\{\tau \le t\} \in \mathcal{F}_t \quad \text{for all } t \ge 0}
$$

**Interpretation**: By time $t$, you can determine whether $\tau$ has already occurred. You don't need to peek into the future.

**Equivalent formulations** (under the usual conditions):

- $\{\tau < t\} \in \mathcal{F}_t$ for all $t \ge 0$
- $\{\tau \le t\} \in \mathcal{F}_t$ for all $t \ge 0$ (the standard definition)
- $\{\tau = t\} \in \mathcal{F}_t$ for all $t \ge 0$ (for discrete filtrations)

**Remark**: We allow $\tau = \infty$, meaning the event may never occur.

---

## Examples of Stopping Times

### 1. Deterministic Times

For any fixed $t_0 \ge 0$, the constant $\tau(\omega) = t_0$ is a stopping time, since $\{\tau \le t\} = \Omega$ for $t \ge t_0$ and $\emptyset$ for $t < t_0$.

### 2. First Hitting Times

For an adapted process $X$ with continuous paths and a Borel set $A \subset \mathbb{R}$:

$$
\tau_A := \inf\{t \ge 0 : X_t \in A\}
$$

is a stopping time. (Convention: $\inf \emptyset = \infty$.)

**Proof sketch**: We consider two cases depending on the structure of $A$.

*Case 1: $A$ is open*. By path continuity and openness of $A$: if $X_s(\omega) \in A$ for some $s \le t$, then $X_r(\omega) \in A$ for some rational $r$ near $s$ with $r \le t$. Therefore:

$$
\{\tau_A \le t\} = \bigcup_{\substack{s \le t \\ s \in \mathbb{Q}}} \{X_s \in A\}
$$

Each $\{X_s \in A\} \in \mathcal{F}_s \subseteq \mathcal{F}_t$, so the countable union is in $\mathcal{F}_t$.

*Case 2: $A$ is closed*. Write $A_n = \{x : d(x, A) < 1/n\}$ (open $1/n$-neighborhoods). By Case 1 each $\tau_{A_n}$ is a stopping time, and $\tau_{A_n} \downarrow \tau_A$ since $A_n \downarrow A$ (for continuous paths). The infimum of stopping times is a stopping time, so $\tau_A$ is a stopping time.

*General Borel $A$*: The result holds but requires more care (the optional section theorem or the fact that $\tau_A = \tau_{\bar{A}}$ for continuous paths). $\square$

**Important special cases**:

- **First passage time**: $\tau_a = \inf\{t \ge 0 : W_t = a\}$ for Brownian motion
- **First exit time**: $\tau_D = \inf\{t \ge 0 : X_t \notin D\}$ from a domain $D$
- **First entry time**: $\tau_K = \inf\{t \ge 0 : X_t \in K\}$ into a set $K$

### 3. Last Exit Times (Non-Example)

The **last exit time** from a set:

$$
\sigma_A := \sup\{t \ge 0 : X_t \in A\}
$$

is generally **not** a stopping time. To know when you last visited $A$, you need to know the entire future path.

**Exception**: If $X$ never returns to $A$ after some deterministic time $T$, and this is known, then $\sigma_A \wedge T$ might be a stopping time.

### 4. Discrete-Time Examples

For a discrete filtration $(\mathcal{F}_n)_{n \ge 0}$:

- $\tau = \inf\{n : S_n \ge 100\}$ where $S_n$ is a random walk — stopping time
- $\tau = $ "the time of the maximum of $S_0, \ldots, S_N$" — **not** a stopping time (requires knowing all values)

---

## Properties of Stopping Times

**Proposition**: If $\sigma$ and $\tau$ are stopping times, then so are:

1. $\sigma \wedge \tau = \min(\sigma, \tau)$
2. $\sigma \vee \tau = \max(\sigma, \tau)$  
3. $\sigma + \tau$ (when both are finite a.s.)
4. $\tau + c$ for any constant $c \ge 0$

**Proof of (1)**: $\{\sigma \wedge \tau \le t\} = \{\sigma \le t\} \cup \{\tau \le t\} \in \mathcal{F}_t$. $\square$

**Proposition**: If $(\tau_n)$ is a sequence of stopping times, then:

- $\inf_n \tau_n$ is a stopping time (since $\{\inf_n \tau_n \le t\} = \bigcup_n \{\tau_n \le t\}$)
- $\sup_n \tau_n$ is a stopping time provided the filtration is right-continuous (since $\{\sup_n \tau_n \le t\} = \bigcap_n \{\tau_n \le t\} \in \mathcal{F}_t$; without right-continuity, $\sup_n \tau_n$ is only guaranteed to satisfy $\{\sup_n \tau_n < t\} \in \mathcal{F}_t$)
- $\liminf_n \tau_n$ and $\limsup_n \tau_n$ are stopping times under the usual conditions

---

## The σ-Algebra F_τ

For a stopping time $\tau$, the **$\sigma$-algebra at time $\tau$** captures information available at the random time $\tau$:

$$
\mathcal{F}_\tau := \{A \in \mathcal{F} : A \cap \{\tau \le t\} \in \mathcal{F}_t \text{ for all } t \ge 0\}
$$

**Interpretation**: $A \in \mathcal{F}_\tau$ if knowing whether $\tau$ has occurred by time $t$ allows you to determine whether $A$ has occurred.

**Key properties**:

1. $\mathcal{F}_\tau$ is a $\sigma$-algebra.
2. $\tau$ is $\mathcal{F}_\tau$-measurable.
3. If $X$ is progressively measurable (in particular if $X$ is adapted with càdlàg paths), then $X_\tau$ is $\mathcal{F}_\tau$-measurable (on $\{\tau < \infty\}$).
4. If $\sigma \le \tau$ are stopping times, then $\mathcal{F}_\sigma \subseteq \mathcal{F}_\tau$.

**Example**: For the first hitting time $\tau_a = \inf\{t : W_t = a\}$:

$$
\mathcal{F}_{\tau_a} = \sigma\left(W_{t \wedge \tau_a} : t \ge 0\right)
$$

This contains information about the path up to hitting $a$, but nothing beyond.

---

## Stopped Processes

Given a process $X = \{X_t\}$ and a stopping time $\tau$, the **stopped process** is:

$$
X_t^\tau := X_{t \wedge \tau} = X_{\min(t, \tau)}
$$

The process is "frozen" at time $\tau$.

**Key theorem**: If $X$ is a martingale (resp. submartingale, supermartingale) and $\tau$ is a stopping time, then $X^\tau$ is also a martingale (resp. submartingale, supermartingale). The proof uses dyadic approximation of $\tau$ and is carried out in full in *Optional Sampling Theorem*. The core idea: stopping a martingale before a random time cannot create systematic bias, since each "frozen" path is still a fair game up to the time of freezing.

---

## The Strong Markov Property

Stopping times interact beautifully with Markov processes. The **strong Markov property** states that the process "restarts" at a stopping time.

**Theorem (Strong Markov Property for Brownian Motion)**: Let $W$ be a Brownian motion and $\tau$ a stopping time with $\tau < \infty$ a.s. Then:

$$
\boxed{\widetilde{W}_t := W_{\tau + t} - W_\tau}
$$

is a Brownian motion independent of $\mathcal{F}_\tau$.

**Interpretation**: After the random time $\tau$, Brownian motion "starts fresh"—the future evolution is independent of everything that happened before $\tau$, including how long it took to reach $\tau$.

**Contrast with ordinary Markov property**: The ordinary Markov property says this for deterministic times. The strong Markov property extends it to stopping times—a much stronger statement.

**Application (Reflection Principle)**: Let $\tau_a = \inf\{t : W_t = a\}$ for $a > 0$. By the strong Markov property:

$$
\mathbb{P}\left(\max_{0 \le s \le t} W_s \ge a\right) = 2\mathbb{P}(W_t \ge a)
$$

The idea: paths that hit $a$ and end below $a$ are in bijection (via reflection) with paths that hit $a$ and end above $a$.

---

## First Passage Time Distributions

The strong Markov property enables computation of hitting time distributions.

**Theorem**: For $a > 0$, the first passage time $\tau_a = \inf\{t : W_t = a\}$ has density:

$$
\boxed{f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right), \quad t > 0}
$$

This is the **inverse Gaussian** (or Wald) distribution.

**Key properties**:

- $\mathbb{E}[\tau_a] = \infty$ (the hitting time has infinite mean!)
- $\mathbb{P}(\tau_a < \infty) = 1$ (Brownian motion hits every level eventually)
- Mode at $t = a^2/3$

**Derivation using exponential martingale**: Apply optional sampling to $Z_t^\theta = \exp(\theta W_t - \frac{\theta^2 t}{2})$ at $\tau_a \wedge T$, then let $T \to \infty$ with careful justification:

$$
\mathbb{E}[\exp(-\lambda \tau_a)] = \exp(-a\sqrt{2\lambda}), \quad \lambda > 0
$$

Inverting this Laplace transform yields the density.

---

## Localization and Local Martingales

Stopping times enable **localization**—a technique for extending theorems from well-behaved processes to more general ones.

**Definition**: A process $M$ is a **local martingale** if there exist stopping times $\tau_n \uparrow \infty$ a.s. such that each stopped process $M^{\tau_n}$ is a martingale.

**Key insight**: Local martingales satisfy the martingale property "locally" (before large fluctuations), even if they fail it globally.

**Example**: For a predictable process $H$ satisfying $\int_0^t H_s^2\,ds < \infty$ a.s., the stochastic integral $\int_0^t H_s \, dW_s$ is always a local martingale. It is a true martingale when the stronger condition $\mathbb{E}\int_0^T H_s^2 \, ds < \infty$ holds.

---

## Predictable Stopping Times

A stopping time $\tau$ is **predictable** if there exist stopping times $\tau_n < \tau$ with $\tau_n \uparrow \tau$ a.s.

**Interpretation**: A predictable stopping time can be "announced" in advance—there's a sequence of earlier times that converge to it.

**Examples**:

- Deterministic times are predictable.
- First hitting times of open sets by continuous processes are **not** predictable (they happen "by surprise").
- First hitting times of closed sets may or may not be predictable.

**Relevance**: The distinction matters for jump processes and the general theory of stochastic integration.

---

## Stopping Times in Discrete Time

For discrete-time filtrations $(\mathcal{F}_n)_{n \ge 0}$, a stopping time satisfies:

$$
\{\tau = n\} \in \mathcal{F}_n \quad \text{for all } n \ge 0
$$

This is equivalent to $\{\tau \le n\} \in \mathcal{F}_n$.

**The gambling interpretation**: A stopping time is a rule for when to stop playing that depends only on what you've seen so far. "Stop when I'm \$100 ahead" is a stopping time; "stop just before I would have lost" is not.

---

## Summary

| Concept | Definition | Key Property |
|---------|------------|--------------|
| Stopping time $\tau$ | $\{\tau \le t\} \in \mathcal{F}_t$ | Observable without seeing the future |
| First hitting time | $\inf\{t : X_t \in A\}$ | Stopping time for adapted continuous $X$ |
| $\mathcal{F}_\tau$ | Information at random time $\tau$ | $X_\tau$ is $\mathcal{F}_\tau$-measurable |
| Stopped process $X^\tau$ | $X_{t \wedge \tau}$ | Preserves martingale property |
| Strong Markov | Fresh start at $\tau$ | $W_{\tau + t} - W_\tau$ is independent BM |

**The power of stopping times**: They allow us to analyze processes at random times while maintaining the mathematical structure (martingales stay martingales, Markov processes restart). This is essential for:

- Optional sampling (evaluating expectations at random times)
- Boundary value problems (exit times from domains)  
- Sequential analysis (optimal stopping)
- Financial mathematics (exercise times of options)

---

## Exercises

### Exercise 1: Stopping Time Verification

Determine which of the following are stopping times. Justify your answers.

(a) $\tau = \inf\{t \ge 0 : W_t = 1\}$

(b) $\tau = \sup\{t \le 1 : W_t = 0\}$

(c) $\tau = \inf\{t \ge 0 : W_t > W_s \text{ for all } s < t\}$

(d) $\tau = \inf\{t \ge 0 : \int_0^t W_s \, ds \ge 1\}$

(e) $\tau = \inf\{t \ge 1 : W_t = W_{t-1}\}$

??? success "Solution to Exercise 1"
    **(a)** $\tau = \inf\{t \ge 0 : W_t = 1\}$ is a **stopping time**. This is the first hitting time of the closed set $\{1\}$ by the continuous adapted process $W_t$. By the general result for first hitting times of closed sets by continuous processes, $\tau$ is a stopping time.

    **(b)** $\tau = \sup\{t \le 1 : W_t = 0\}$ is **not** a stopping time. To determine whether the last zero before time 1 has occurred by time $t < 1$, one would need to know the future path after $t$ — specifically, whether Brownian motion returns to 0 between $t$ and 1. This requires information beyond $\mathcal{F}_t$.

    **(c)** $\tau = \inf\{t \ge 0 : W_t > W_s \text{ for all } s < t\}$. This asks for the first time the process exceeds all previous values. Since $W_0 = 0$ and $W_t$ is continuous with $\limsup_{t \to 0^+} W_t/\sqrt{t} = +\infty$ a.s. (by the law of the iterated logarithm), there exist arbitrarily small times $t$ with $W_t > 0 = W_0$. In fact, $\tau = 0$ a.s. because for any $\varepsilon > 0$, there exists $t \in (0, \varepsilon)$ with $W_t > 0 > \inf_{s \in [0, t)} W_s$ is not guaranteed to mean $W_t > W_s$ for ALL $s < t$. Actually, $\tau = 0$ because Brownian motion starts fresh and immediately exceeds its starting value. Since $\tau = 0$ is a constant, it is trivially a **stopping time**.

    **(d)** $\tau = \inf\{t \ge 0 : \int_0^t W_s\,ds \ge 1\}$ is a **stopping time**. The process $Y_t = \int_0^t W_s\,ds$ is adapted and continuous (as the integral of a continuous adapted process). Therefore $\tau$ is the first hitting time of the closed set $[1, \infty)$ by the continuous adapted process $Y_t$, hence a stopping time.

    **(e)** $\tau = \inf\{t \ge 1 : W_t = W_{t-1}\}$ is a **stopping time**. Define $Y_t = W_t - W_{t-1}$ for $t \ge 1$. Then $Y_t$ is adapted to $(\mathcal{F}_t)$ (since both $W_t$ and $W_{t-1}$ are $\mathcal{F}_t$-measurable for $t \ge 1$) and has continuous paths. The time $\tau = \inf\{t \ge 1 : Y_t = 0\}$ is the first hitting time of 0 by the continuous adapted process $Y_t$ starting at time 1, hence a stopping time.

---

### Exercise 2: Operations on Stopping Times

Let $\sigma$ and $\tau$ be stopping times.

(a) Prove that $\sigma \wedge \tau$ is a stopping time.

(b) Prove that $\sigma + \tau$ is a stopping time (assuming both are finite a.s.).

(c) Give a counterexample showing that $\sigma - \tau$ need not be a stopping time.

??? success "Solution to Exercise 2"
    **(a)** For any $t \ge 0$:

    $$
    \{\sigma \wedge \tau \le t\} = \{\min(\sigma, \tau) \le t\} = \{\sigma \le t\} \cup \{\tau \le t\}
    $$

    Since $\sigma$ and $\tau$ are stopping times, $\{\sigma \le t\} \in \mathcal{F}_t$ and $\{\tau \le t\} \in \mathcal{F}_t$. As $\mathcal{F}_t$ is a $\sigma$-algebra, $\{\sigma \le t\} \cup \{\tau \le t\} \in \mathcal{F}_t$. $\square$

    **(b)** Assume $\sigma, \tau < \infty$ a.s. We need $\{\sigma + \tau \le t\} \in \mathcal{F}_t$. Write:

    $$
    \{\sigma + \tau \le t\} = \bigcup_{q \in \mathbb{Q} \cap [0, t]} (\{\sigma \le q\} \cap \{\tau \le t - q\})
    $$

    For each rational $q \in [0, t]$: $\{\sigma \le q\} \in \mathcal{F}_q \subseteq \mathcal{F}_t$ and $\{\tau \le t - q\} \in \mathcal{F}_{t-q} \subseteq \mathcal{F}_t$. So each intersection is in $\mathcal{F}_t$, and the countable union is in $\mathcal{F}_t$. $\square$

    **(c)** Let $\sigma = \tau = \inf\{t : W_t = 1\}$. Then $\sigma - \tau = 0$ is trivially a stopping time. For a non-trivial example: let $\sigma = 2$ (deterministic) and $\tau = \inf\{t : W_t = 1\}$. Then $\sigma - \tau = 2 - \tau$. The event $\{2 - \tau \le t\} = \{\tau \ge 2 - t\}$ for $t \le 2$, which is $\{\tau < 2 - t\}^c$. For small $t$, $\{\tau \ge 2 - t\}$ depends on whether Brownian motion has hit 1 by time $2 - t$, which requires looking at the path up to time $2 - t > t$ (for $t < 1$). This is not necessarily in $\mathcal{F}_t$. Hence $\sigma - \tau$ need not be a stopping time.

---

### Exercise 3: The σ-Algebra F_τ

Let $\tau = \inf\{t : W_t = 1\}$.

(a) Show that $W_\tau$ is $\mathcal{F}_\tau$-measurable.

(b) Is $W_{\tau + 1}$ $\mathcal{F}_\tau$-measurable?

(c) Describe $\mathcal{F}_\tau$ in words.

??? success "Solution to Exercise 3"
    **(a)** Let $\tau = \inf\{t : W_t = 1\}$. The random variable $W_\tau = 1$ (by continuity of Brownian paths, the process equals 1 at the hitting time). A constant is measurable with respect to any $\sigma$-algebra, so $W_\tau$ is $\mathcal{F}_\tau$-measurable.

    More generally, for any progressively measurable process $X$, $X_\tau$ is $\mathcal{F}_\tau$-measurable on $\{\tau < \infty\}$.

    **(b)** $W_{\tau + 1}$ is **not** $\mathcal{F}_\tau$-measurable. By the strong Markov property, $\widetilde{W}_s = W_{\tau + s} - W_\tau$ is a Brownian motion independent of $\mathcal{F}_\tau$. Therefore $W_{\tau + 1} = W_\tau + \widetilde{W}_1 = 1 + \widetilde{W}_1$, and $\widetilde{W}_1 \sim N(0, 1)$ is independent of $\mathcal{F}_\tau$. Since $W_{\tau + 1}$ depends on the independent increment $\widetilde{W}_1$, it is not $\mathcal{F}_\tau$-measurable.

    **(c)** $\mathcal{F}_\tau$ consists of all events whose occurrence can be determined by knowing the path of Brownian motion up to and including the first time it hits 1. Formally, $\mathcal{F}_\tau = \sigma(W_{t \wedge \tau} : t \ge 0)$ — it contains all information about the Brownian path up to the hitting time, but no information about the path after hitting 1. It encodes the shape of the path on $[0, \tau]$, the value of $\tau$ itself, and all events determined by these.

---

### Exercise 4: Strong Markov Property

(a) State the strong Markov property for Brownian motion.

(b) Let $\tau_a = \inf\{t : W_t = a\}$. Use the strong Markov property to show that $\tau_a + \tau_b \circ \theta_{\tau_a}$ has the same distribution as $\tau_{a+b}$, where $\theta$ is the shift operator.

(c) Derive the reflection principle: $\mathbb{P}(\sup_{s \le t} W_s \ge a) = 2\mathbb{P}(W_t \ge a)$ for $a > 0$.

??? success "Solution to Exercise 4"
    **(a)** The **strong Markov property for Brownian motion**: Let $W$ be a standard Brownian motion and $\tau$ a stopping time with $\tau < \infty$ a.s. Then the process $\widetilde{W}_t := W_{\tau + t} - W_\tau$, $t \ge 0$, is a standard Brownian motion independent of $\mathcal{F}_\tau$.

    **(b)** By the strong Markov property, $\widetilde{W}_t = W_{\tau_a + t} - W_{\tau_a}$ is a Brownian motion independent of $\mathcal{F}_{\tau_a}$, starting from 0. The first hitting time of level $b$ by $\widetilde{W}$ is $\tilde{\tau}_b = \inf\{t : \widetilde{W}_t = b\}$. This has the same distribution as $\tau_b$ (by the definition of Brownian motion).

    Now, $\tau_a + \tilde{\tau}_b$ is the first time $W$ reaches level $a$ (at time $\tau_a$) and then the additional time for the process to travel from $a$ to $a + b$ (an additional distance of $b$). Since $W_{\tau_a} = a$, the first time $W$ reaches level $a + b$ is $\tau_{a+b} = \tau_a + \tilde{\tau}_b$, and $\tilde{\tau}_b \stackrel{d}{=} \tau_b$ is independent of $\tau_a$. Therefore $\tau_{a+b} \stackrel{d}{=} \tau_a + \tau_b$ with $\tau_a$ and $\tau_b$ independent.

    **(c)** For $a > 0$, define $\tau_a = \inf\{t : W_t = a\}$. Decompose the event $\{W_t \ge a\}$:

    $$
    \{W_t \ge a\} \subseteq \left\{\sup_{s \le t} W_s \ge a\right\}
    $$

    Conversely, on the event $\{\sup_{s \le t} W_s \ge a\}$, we have $\tau_a \le t$. By the strong Markov property, $\widetilde{W}_s = W_{\tau_a + s} - a$ is a Brownian motion independent of $\mathcal{F}_{\tau_a}$. Thus:

    $$
    \mathbb{P}\left(\sup_{s \le t} W_s \ge a\right) = \mathbb{P}(\tau_a \le t)
    $$

    Given $\tau_a \le t$, by symmetry of $\widetilde{W}$:

    $$
    \mathbb{P}(W_t \ge a \mid \tau_a \le t) = \mathbb{P}(W_t - a \ge 0 \mid \tau_a \le t) = \mathbb{P}(\widetilde{W}_{t - \tau_a} \ge 0 \mid \tau_a \le t) = \frac{1}{2}
    $$

    (The last equality uses symmetry of Brownian motion: $\mathbb{P}(\widetilde{W}_s \ge 0) = 1/2$ for any $s > 0$, and independence.)

    Therefore:

    $$
    \mathbb{P}(W_t \ge a) = \mathbb{P}(W_t \ge a, \tau_a \le t) = \mathbb{P}(\tau_a \le t) \cdot \frac{1}{2} = \frac{1}{2}\mathbb{P}\left(\sup_{s \le t} W_s \ge a\right)
    $$

    Rearranging:

    $$
    \mathbb{P}\left(\sup_{s \le t} W_s \ge a\right) = 2\mathbb{P}(W_t \ge a) \quad \square
    $$
