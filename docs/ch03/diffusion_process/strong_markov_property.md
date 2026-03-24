# Strong Markov Property

## Concept Definition

Throughout, $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ is a filtered probability space satisfying the usual conditions. A **stopping time** is a random variable $\tau : \Omega \to [0, \infty]$ such that $\{\tau \le t\} \in \mathcal{F}_t$ for all $t \ge 0$. The **stopped $\sigma$-algebra** is

$$
\mathcal{F}_\tau := \{ A \in \mathcal{F} : A \cap \{\tau \le t\} \in \mathcal{F}_t \text{ for all } t \ge 0 \}.
$$

!!! info "Definition: Markov Property vs Strong Markov Property"
    A time-homogeneous Markov process $(X_t)_{t \ge 0}$ satisfies the **Markov property** if for all bounded measurable $\varphi$ and all $0 \le s \le t$,

    $$
    \mathbb{E}[\varphi(X_t) \mid \mathcal{F}_s] = \mathbb{E}^{X_s}[\varphi(X_{t-s})].
    $$

    It satisfies the **strong Markov property** if the same identity holds when the deterministic time $s$ is replaced by any **stopping time** $\tau < \infty$ $\mathbb{P}$-a.s.: for all $t \ge 0$,

    $$
    \mathbb{E}[\varphi(X_{\tau + t}) \mid \mathcal{F}_\tau] = \mathbb{E}^{X_\tau}[\varphi(X_t)].
    $$

The key difference: the Markov property is memoryless at **fixed times**; the strong Markov property is memoryless at **random times** (first passage times, exit times, etc.).

---

## Explanation

### Why Stopping Times Require a Separate Condition

For a fixed time $s$, the Markov property follows from the independence of Brownian increments and measurability. At a stopping time $\tau$, the event $\{\tau = t\}$ depends on the entire history up to $t$, so the argument requires additional structure — specifically, right-continuity of the filtration $(\mathcal{F}_t)$ and regularity of the transition semigroup.

### Strong Markov Property for Brownian Motion

!!! theorem "Theorem"
    Let $(W_t)_{t \ge 0}$ be a standard Brownian motion and $\tau$ a stopping time with $\mathbb{P}(\tau < \infty) = 1$. Define

    $$
    B_t := W_{\tau + t} - W_\tau, \qquad t \ge 0.
    $$

    Then $(B_t)_{t \ge 0}$ is a standard Brownian motion and is **independent of $\mathcal{F}_\tau$**.

This is the prototype. The proof uses right-continuity of $(\mathcal{F}_t)$ to approximate $\tau$ by discrete stopping times $\tau_n = \lceil 2^n \tau \rceil / 2^n$, apply the ordinary Markov property at each level, and pass to the limit.

### Strong Markov Property for Diffusions

!!! theorem "Theorem"
    Let $X_t$ solve the SDE

    $$
    \mathrm{d}X_t^{i} = b^{i}(X_t)\,\mathrm{d}t + \sigma^{i\alpha}(X_t)\,\mathrm{d}W_t^{\alpha}
    $$

    with $b, \sigma$ locally Lipschitz with linear growth, so that a unique strong solution exists. Then $X$ is a **Feller process**, and every Feller process with continuous paths is strong Markov.

!!! warning "Precision note"
    The Lipschitz/growth conditions guarantee existence and uniqueness of the strong solution. The strong Markov property then follows from the **Feller property** of the semigroup $P_t f(x) = \mathbb{E}^x[f(X_t)]$: namely, $P_t$ maps $C_0(\mathbb{R}^d)$ (continuous functions vanishing at infinity) into itself, and $\|P_t f - f\|_\infty \to 0$ as $t \to 0$. Combined with right-continuity of $(\mathcal{F}_t)$, this yields strong Markov. The Lipschitz condition alone does not directly imply strong Markov; it is the route to the Feller property that does.

### Distinction from the Optional Sampling Theorem

The **strong Markov property** concerns the **conditional law** of the future path given $\mathcal{F}_\tau$. The **Optional Sampling Theorem** concerns the **expected value** of a martingale at $\tau$. These are logically independent results, though both involve stopping times.

---

## Diagram / Example

### Exit Times and the Restart Argument

Let $D \subset \mathbb{R}^d$ be open and define the **exit time**

$$
\tau_D := \inf\{t \ge 0 : X_t \notin D\}.
$$

$\tau_D$ is a stopping time. The strong Markov property asserts: conditionally on $\mathcal{F}_{\tau_D}$, the post-exit process $(X_{\tau_D + t})_{t \ge 0}$ behaves like a fresh copy of $X$ started from $X_{\tau_D} \in \partial D$.

This **restart argument** is used repeatedly in:

- Dirichlet boundary value problems (harmonic functions and BM hitting distributions),
- computing the distribution of $\max_{0 \le s \le t} W_s$ via the reflection principle,
- establishing the **strong Markov property at iterated stopping times** (the process restarts freshly each time it hits a boundary).

### Reflection Principle (Consequence)

For standard Brownian motion $W$ and $a > 0$:

$$
\mathbb{P}\!\left(\max_{0 \le s \le t} W_s \ge a\right) = 2\,\mathbb{P}(W_t \ge a).
$$

*Proof sketch.* Let $\tau_a = \inf\{s : W_s = a\}$. By the strong Markov property, $B_s := W_{\tau_a + s} - a$ is a fresh standard BM independent of $\mathcal{F}_{\tau_a}$. On $\{\tau_a \le t\}$, the event $\{W_t \ge a\}$ equals $\{B_{t-\tau_a} \ge 0\}$ and by symmetry of BM has probability $1/2$ conditionally on $\mathcal{F}_{\tau_a}$. Therefore $\mathbb{P}(W_t \ge a,\, \tau_a \le t) = \frac{1}{2}\mathbb{P}(\tau_a \le t)$. Since $\mathbb{P}(\max_{s \le t} W_s \ge a) = \mathbb{P}(\tau_a \le t)$ and $\mathbb{P}(W_t \ge a) = \mathbb{P}(W_t \ge a,\, \tau_a \le t)$ (as $a > 0$), the result follows. $\square$

---

## Proof / Derivation

We sketch the proof for Brownian motion via discrete approximation.

**Step 1.** Define $\tau_n := \frac{\lceil 2^n \tau \rceil}{2^n}$, a sequence of stopping times taking values in $\{k/2^n : k \ge 0\}$ with $\tau_n \ge \tau$ and $\tau_n \downarrow \tau$ (i.e. $\tau_{n+1} \le \tau_n$ for all $n$, decreasing to $\tau$ from above).

**Step 2.** For each fixed $n$, on the event $\{\tau_n = k/2^n\}$, we have $\mathcal{F}_{\tau_n} = \mathcal{F}_{k/2^n}$ (by definition of the stopped $\sigma$-algebra restricted to this event), so:

$$
\mathbb{E}[\varphi(W_{\tau_n + t}) \mid \mathcal{F}_{\tau_n}]
= \mathbb{E}^{W_{k/2^n}}[\varphi(W_t)]
$$

by the ordinary Markov property at the deterministic time $k/2^n$.

**Step 3.** Since $\varphi$ is bounded and $W$ has continuous paths, $\varphi(W_{\tau_n + t}) \to \varphi(W_{\tau + t})$ a.s. as $n \to \infty$. Since $\tau_n \downarrow \tau$ (each $\tau_n \ge \tau$), stopping later gives more information: $\mathcal{F}_{\tau_n} \supseteq \mathcal{F}_\tau$ (finer $\sigma$-algebras for larger stopping times), and $\bigcap_n \mathcal{F}_{\tau_n} = \mathcal{F}_\tau$ by right-continuity. Dominated convergence and backward martingale convergence complete the passage to the limit. $\square$

---

## What to Remember

- The **Markov property** holds at fixed times; the **strong Markov property** holds at stopping times.
- For Brownian motion: $(W_{\tau+t} - W_\tau)_{t \ge 0}$ is a fresh BM independent of $\mathcal{F}_\tau$.
- For diffusions: strong Markov follows from the Feller property (not directly from Lipschitz conditions).
- The canonical application is the **restart argument** at first exit times, connecting SDEs to boundary value PDEs.

---

## Exercises

**Exercise 1.** Let $(W_t)_{t \ge 0}$ be a standard Brownian motion and define $\tau_a = \inf\{t \ge 0 : W_t = a\}$ for $a > 0$. Using the strong Markov property, show that $B_t := W_{\tau_a + t} - a$ is a standard Brownian motion independent of $\mathcal{F}_{\tau_a}$. Explain why the ordinary Markov property at a fixed time is insufficient for this conclusion.

---

**Exercise 2.** Let $D = (-1, 1) \subset \mathbb{R}$ and let $W_t$ be a standard Brownian motion started at $x \in D$. Define the exit time $\tau_D = \inf\{t \ge 0 : W_t \notin D\}$. Using the strong Markov property and the fact that $f(x) = x$ is harmonic, compute $\mathbb{E}^x[W_{\tau_D}]$. Then use $g(x) = x^2 - t$ (which satisfies $\mathcal{L}g = 0$ for BM) to find $\mathbb{E}^x[\tau_D]$.

---

**Exercise 3.** Let $\tau$ be a stopping time with $\mathbb{P}(\tau < \infty) = 1$. Define the discrete approximation $\tau_n = \lceil 2^n \tau \rceil / 2^n$. Show that $\tau_n$ is a stopping time, $\tau_n \ge \tau$, and $\tau_n \downarrow \tau$ as $n \to \infty$. Explain why right-continuity of the filtration $(\mathcal{F}_t)$ is needed in Step 3 of the proof to conclude $\bigcap_n \mathcal{F}_{\tau_n} = \mathcal{F}_\tau$.

---

**Exercise 4.** Give an example of a Markov process that satisfies the ordinary Markov property at all fixed times but fails the strong Markov property at some stopping time. (Hint: consider a process whose transition mechanism depends on the time parameter in a discontinuous way.)

---

**Exercise 5.** Using the reflection principle (which follows from the strong Markov property), compute

$$
\mathbb{P}\!\left(\max_{0 \le s \le t} W_s \ge a,\; W_t \le b\right)
$$

for $a > 0$ and $b < a$, where $W$ is a standard Brownian motion. Express your answer in terms of the standard normal CDF $\Phi$.

---

**Exercise 6.** Let $X_t$ solve $\mathrm{d}X_t = -\theta X_t\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ with $\theta > 0$ (Ornstein–Uhlenbeck process). Let $\tau = \inf\{t \ge 0 : X_t = c\}$ for some level $c$. Explain why the strong Markov property guarantees that the post-$\tau$ process $(X_{\tau + t})_{t \ge 0}$, conditioned on $\mathcal{F}_\tau$, behaves like an OU process started from $c$. What property of the OU semigroup (related to Feller continuity) is needed?

---

**Exercise 7.** Explain the distinction between the strong Markov property and the optional sampling theorem. Construct a scenario involving a submartingale $Y_t$ and a stopping time $\tau$ where the optional sampling theorem applies but the strong Markov property is not relevant, and vice versa.
