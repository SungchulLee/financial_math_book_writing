# Stopping Times

A stopping time is a random time whose occurrence can be decided from past and present information alone. Before we can evaluate a martingale at a random time (the subject of [Optional Sampling](optional_sampling_theorem.md)) we must know which random times are even admissible. This file answers that question.

---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space (see [Filtrations](filtration.md)).

A random variable $\tau: \Omega \to [0, \infty]$ is a **stopping time** if

$$
\{\tau \le t\} \in \mathcal{F}_t \quad \text{for all } t \ge 0.
$$

By time $t$ you can decide whether $\tau$ has already occurred — no peeking into the future. The value $\tau = \infty$ is allowed (the event may never occur).

!!! note "Test your intuition"
    "First time the stock price exceeds \$100" is a stopping time.
    "Last time the stock price exceeds \$100 before it crashes" is not — it requires the future.

---

## Examples and One Non-Example

**Deterministic times.** Any constant $\tau \equiv t_0$ is a stopping time.

**First hitting time of a closed set** (canonical example). For an adapted continuous process $X$ and a closed set $A$,

$$
\tau_A := \inf\{t \ge 0 : X_t \in A\}
$$

is a stopping time. *Idea of proof*: if $A$ is open, then $\{\tau_A \le t\} = \bigcup_{s \in \mathbb{Q} \cap [0,t]} \{X_s \in A\}$ by path continuity, and this countable union lies in $\mathcal{F}_t$. Closed sets are handled by approximating from outside by open neighborhoods $A_n = \{x : d(x,A) < 1/n\}$ and taking the limit of $\tau_{A_n}$.

**Last exit time (non-example).**

$$
\sigma_A := \sup\{t \ge 0 : X_t \in A\}
$$

is generally *not* a stopping time: determining the last visit to $A$ requires the entire future path.

---

## Properties

If $\sigma, \tau$ are stopping times, so are $\sigma \wedge \tau$, $\sigma \vee \tau$, $\sigma + \tau$, and $\tau + c$ for $c \ge 0$. For (1): $\{\sigma \wedge \tau \le t\} = \{\sigma \le t\} \cup \{\tau \le t\} \in \mathcal{F}_t$. $\square$

For sequences: $\inf_n \tau_n$ is always a stopping time; $\sup_n \tau_n$ is a stopping time when the filtration is right-continuous.

---

## The σ-Algebra F_τ

The information available at the random time $\tau$ is

$$
\mathcal{F}_\tau := \{A \in \mathcal{F} : A \cap \{\tau \le t\} \in \mathcal{F}_t \text{ for all } t \ge 0\}.
$$

Key facts:

- $\mathcal{F}_\tau$ is a $\sigma$-algebra and $\tau$ is $\mathcal{F}_\tau$-measurable.
- If $X$ is progressively measurable, then $X_\tau$ is $\mathcal{F}_\tau$-measurable on $\{\tau < \infty\}$.
- $\sigma \le \tau \Rightarrow \mathcal{F}_\sigma \subseteq \mathcal{F}_\tau$.

---

## Stopped Processes

Given a process $X$ and a stopping time $\tau$, the **stopped process** is

$$
X_t^\tau := X_{t \wedge \tau}.
$$

!!! tip "Stability theorem"
    If $X$ is a [martingale](martingales.md) (sub/supermartingale), then so is $X^\tau$. Freezing a fair game at a non-anticipating time cannot introduce bias. This fact is the engine driving the [Optional Sampling Theorem](optional_sampling_theorem.md).

---

## Discrete Time

For $(\mathcal{F}_n)_{n \ge 0}$, the condition $\{\tau \le n\} \in \mathcal{F}_n$ is equivalent to $\{\tau = n\} \in \mathcal{F}_n$. Interpretation: a stopping time is a rule for when to stop that uses only what you have already seen. "Stop when I'm \$100 ahead" qualifies; "stop just before I would lose" does not.

---

## Exercises

**Exercise 1.** Which of the following are stopping times with respect to the Brownian filtration?

(a) $\tau = \inf\{t \ge 0 : W_t = 1\}$
(b) $\tau = \sup\{t \le 1 : W_t = 0\}$
(c) $\tau = \inf\{t \ge 0 : \int_0^t W_s\,ds \ge 1\}$
(d) $\tau = \inf\{t \ge 1 : W_t = W_{t-1}\}$

??? success "Solution to Exercise 1"
    **(a)** Stopping time: first hitting time of the closed set $\{1\}$ by a continuous adapted process.

    **(b)** Not a stopping time: knowing whether the last zero before time $1$ has occurred by time $t < 1$ requires the future path on $(t, 1]$.

    **(c)** Stopping time: $Y_t = \int_0^t W_s\,ds$ is adapted and continuous, and $\tau$ is the first hitting time of $[1, \infty)$ by $Y$.

    **(d)** Stopping time: $Y_t = W_t - W_{t-1}$ for $t \ge 1$ is adapted and continuous, and $\tau$ is its first zero on $[1, \infty)$.

---

**Exercise 2.** Let $\sigma, \tau$ be stopping times.

(a) Show that $\sigma \wedge \tau$ is a stopping time.
(b) Show that $\sigma + \tau$ is a stopping time.
(c) Give an example showing $\sigma - \tau$ need not be.

??? success "Solution to Exercise 2"
    **(a)** $\{\sigma \wedge \tau \le t\} = \{\sigma \le t\} \cup \{\tau \le t\} \in \mathcal{F}_t$.

    **(b)** For rational $q \in [0, t]$:

    $$
    \{\sigma + \tau \le t\} = \bigcup_{q \in \mathbb{Q} \cap [0,t]} \bigl(\{\sigma \le q\} \cap \{\tau \le t - q\}\bigr).
    $$

    Each intersection lies in $\mathcal{F}_t$, and the union is countable.

    **(c)** Let $\sigma = 2$ and $\tau = \inf\{t : W_t = 1\}$. Then $\{2 - \tau \le t\} = \{\tau \ge 2 - t\}$, and deciding this event for small $t$ requires knowing the Brownian path up to time $2 - t > t$.

---

**Exercise 3.** Let $\tau = \inf\{t : W_t = 1\}$.

(a) Is $W_\tau$ $\mathcal{F}_\tau$-measurable?
(b) Is $W_{\tau + 1}$ $\mathcal{F}_\tau$-measurable?
(c) Describe $\mathcal{F}_\tau$ in plain words.

??? success "Solution to Exercise 3"
    **(a)** Yes — in fact $W_\tau = 1$ a.s. by path continuity, so it is constant and measurable with respect to any $\sigma$-algebra.

    **(b)** No. The increment $W_{\tau + 1} - W_\tau$ is $N(0,1)$ and independent of $\mathcal{F}_\tau$ (this is the strong Markov property, developed in the Brownian motion chapter). So $W_{\tau + 1}$ depends on information beyond $\mathcal{F}_\tau$.

    **(c)** $\mathcal{F}_\tau$ records everything observable about the path $\{W_s : 0 \le s \le \tau\}$ — the shape of the path up to the first hit of level $1$, and nothing thereafter.

---

**Exercise 4.** Let $X$ be adapted with continuous paths and let $A \subset \mathbb{R}$ be open. Prove that $\tau_A = \inf\{t : X_t \in A\}$ is a stopping time.

??? success "Solution to Exercise 4"
    For any $t \ge 0$, path continuity and openness of $A$ give

    $$
    \{\tau_A < t\} = \bigcup_{s \in \mathbb{Q} \cap [0, t)} \{X_s \in A\}.
    $$

    ($\supseteq$ is clear; for $\subseteq$, if $X_{s_0} \in A$ for some $s_0 < t$, continuity places $X_s \in A$ on an open interval around $s_0$, which contains a rational.) Each $\{X_s \in A\} \in \mathcal{F}_s \subseteq \mathcal{F}_t$, so $\{\tau_A < t\} \in \mathcal{F}_t$. Since $\{\tau_A \le t\} = \bigcap_{n} \{\tau_A < t + 1/n\}$, this lies in $\mathcal{F}_{t^+}$ and under right-continuity in $\mathcal{F}_t$. $\square$

---

**Exercise 5.** Let $\tau$ be a stopping time and $M$ a martingale. Show directly from the definition that $\mathbb{E}[M_t \mathbf{1}_{\{\tau \le s\}}] = \mathbb{E}[M_s \mathbf{1}_{\{\tau \le s\}}]$ for $s \le t$.

??? success "Solution to Exercise 5"
    The event $\{\tau \le s\} \in \mathcal{F}_s$. Because $M$ is a martingale, $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$, and so

    $$
    \mathbb{E}[M_t \mathbf{1}_{\{\tau \le s\}}] = \mathbb{E}\bigl[\mathbb{E}[M_t \mid \mathcal{F}_s] \mathbf{1}_{\{\tau \le s\}}\bigr] = \mathbb{E}[M_s \mathbf{1}_{\{\tau \le s\}}].
    $$

    This identity is the seed of the Optional Sampling Theorem.
