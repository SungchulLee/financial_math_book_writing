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

**Proof sketch**: The set $\{\tau_A \le t\} = \{\omega : X_s(\omega) \in A \text{ for some } s \le t\}$ can be written as:

$$
\{\tau_A \le t\} = \bigcup_{s \le t, s \in \mathbb{Q}} \{X_s \in A\}
$$

using path continuity. Each $\{X_s \in A\} \in \mathcal{F}_s \subseteq \mathcal{F}_t$, so the union is in $\mathcal{F}_t$. $\square$

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

- $\inf_n \tau_n$ is a stopping time
- $\sup_n \tau_n$ is a stopping time
- $\liminf_n \tau_n$ and $\limsup_n \tau_n$ are stopping times

---

## The $\sigma$-Algebra $\mathcal{F}_\tau$

For a stopping time $\tau$, the **$\sigma$-algebra at time $\tau$** captures information available at the random time $\tau$:

$$
\mathcal{F}_\tau := \{A \in \mathcal{F} : A \cap \{\tau \le t\} \in \mathcal{F}_t \text{ for all } t \ge 0\}
$$

**Interpretation**: $A \in \mathcal{F}_\tau$ if knowing whether $\tau$ has occurred by time $t$ allows you to determine whether $A$ has occurred.

**Key properties**:

1. $\mathcal{F}_\tau$ is a $\sigma$-algebra.
2. $\tau$ is $\mathcal{F}_\tau$-measurable.
3. If $X$ is adapted and right-continuous, then $X_\tau$ is $\mathcal{F}_\tau$-measurable (on $\{\tau < \infty\}$).
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

**Key theorem**: If $X$ is a martingale (resp. submartingale, supermartingale) and $\tau$ is a stopping time, then $X^\tau$ is also a martingale (resp. submartingale, supermartingale).

**Proof**: For $s \le t$:

$$
\mathbb{E}[X_{t \wedge \tau} \mid \mathcal{F}_s] = \mathbb{E}[X_{t \wedge \tau} \mid \mathcal{F}_{s \wedge \tau}] = X_{s \wedge \tau}
$$

where the second equality uses the martingale property applied carefully to the stopped times. $\square$

**Implication**: Stopping a martingale preserves the martingale property. This is the foundation of the optional sampling theorem.

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

**Example**: The stochastic integral $\int_0^t H_s \, dW_s$ is always a local martingale. It is a true martingale if $\mathbb{E}\int_0^T H_s^2 \, ds < \infty$.

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

### Exercise 2: Operations on Stopping Times

Let $\sigma$ and $\tau$ be stopping times.

(a) Prove that $\sigma \wedge \tau$ is a stopping time.

(b) Prove that $\sigma + \tau$ is a stopping time (assuming both are finite a.s.).

(c) Give a counterexample showing that $\sigma - \tau$ need not be a stopping time.

### Exercise 3: The $\sigma$-Algebra $\mathcal{F}_\tau$

Let $\tau = \inf\{t : W_t = 1\}$.

(a) Show that $W_\tau$ is $\mathcal{F}_\tau$-measurable.

(b) Is $W_{\tau + 1}$ $\mathcal{F}_\tau$-measurable?

(c) Describe $\mathcal{F}_\tau$ in words.

### Exercise 4: Strong Markov Property

(a) State the strong Markov property for Brownian motion.

(b) Let $\tau_a = \inf\{t : W_t = a\}$. Use the strong Markov property to show that $\tau_a + \tau_b \circ \theta_{\tau_a}$ has the same distribution as $\tau_{a+b}$, where $\theta$ is the shift operator.

(c) Derive the reflection principle: $\mathbb{P}(\sup_{s \le t} W_s \ge a) = 2\mathbb{P}(W_t \ge a)$ for $a > 0$.
