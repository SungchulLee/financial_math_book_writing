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

---

## Solutions

??? success "Solution to Exercise 1"
    Let $\tau_a = \inf\{t \ge 0 : W_t = a\}$ with $a > 0$. Define $B_t := W_{\tau_a + t} - W_\tau = W_{\tau_a + t} - a$.

    By the **strong Markov property** of Brownian motion: conditionally on $\mathcal{F}_{\tau_a}$, the process $(W_{\tau_a + t})_{t \ge 0}$ is independent of $\mathcal{F}_{\tau_a}$ and has the same law as a Brownian motion started from $W_{\tau_a} = a$. Therefore $B_t = W_{\tau_a + t} - a$ is a standard Brownian motion (started from $0$) independent of $\mathcal{F}_{\tau_a}$.

    To verify the defining properties: (1) $B_0 = 0$; (2) for $0 \le s < t$, the increment $B_t - B_s = W_{\tau_a + t} - W_{\tau_a + s}$ is independent of $\mathcal{F}_{\tau_a + s}$ (and hence of $\mathcal{F}_{\tau_a}$) and is $\mathcal{N}(0, t-s)$; (3) $B$ has continuous paths since $W$ does.

    **Why the ordinary Markov property is insufficient:** The ordinary Markov property holds at **fixed** (deterministic) times $s$. But $\tau_a$ is a **random** time that depends on the entire trajectory of $W$ up to the moment it hits $a$. The event $\{\tau_a = t\}$ belongs to $\mathcal{F}_t$ and depends on the path history, so we cannot simply apply the Markov property at a fixed time. We need the extension to stopping times — the strong Markov property — which requires right-continuity of the filtration.

??? success "Solution to Exercise 2"
    **Computing $\mathbb{E}^x[W_{\tau_D}]$:** The function $f(x) = x$ is harmonic for Brownian motion ($\mathcal{L}f = \frac{1}{2}f'' = 0$), so $M_t = W_{t \wedge \tau_D}$ is a martingale (by the optional sampling theorem / strong Markov property). Since $W$ exits $D = (-1,1)$ at either $-1$ or $+1$:

    $$
    \mathbb{E}^x[W_{\tau_D}] = \mathbb{E}^x[M_0] = x
    $$

    by the optional sampling theorem (with $\tau_D$ bounded in $L^1$ for BM on a bounded interval).

    **Computing $\mathbb{E}^x[\tau_D]$:** Consider $g(x, t) = x^2 - t$. For BM, $\mathcal{L}g = \frac{1}{2} \cdot 2 - 1 = 0$ (where the $-1$ comes from $\partial_t g$), so $g(W_t, t) = W_t^2 - t$ is a martingale. By optional sampling at $\tau_D$:

    $$
    \mathbb{E}^x[W_{\tau_D}^2 - \tau_D] = x^2 - 0
    $$

    Since $W_{\tau_D} \in \{-1, +1\}$, we have $W_{\tau_D}^2 = 1$ a.s., so

    $$
    1 - \mathbb{E}^x[\tau_D] = x^2
    $$

    Therefore

    $$
    \mathbb{E}^x[\tau_D] = 1 - x^2
    $$

??? success "Solution to Exercise 3"
    **$\tau_n$ is a stopping time:** For any $t \ge 0$, the event $\{\tau_n \le t\} = \{\lceil 2^n \tau \rceil / 2^n \le t\} = \{\tau \le \lfloor 2^n t \rfloor / 2^n\}$. Since $\lfloor 2^n t \rfloor / 2^n$ is a deterministic value and $\tau$ is a stopping time, $\{\tau \le \lfloor 2^n t \rfloor / 2^n\} \in \mathcal{F}_{\lfloor 2^n t \rfloor / 2^n} \subseteq \mathcal{F}_t$. So $\tau_n$ is a stopping time.

    **$\tau_n \ge \tau$:** By definition, $\lceil 2^n \tau \rceil \ge 2^n \tau$, so $\tau_n = \lceil 2^n \tau \rceil / 2^n \ge \tau$.

    **$\tau_n \downarrow \tau$:** We have $\tau_n - \tau \le 1/2^n$ since $\lceil k \rceil - k < 1$ for any real $k$. Therefore $\tau_n \to \tau$ as $n \to \infty$.

    **Why right-continuity is needed:** We have $\mathcal{F}_{\tau_n} \supseteq \mathcal{F}_\tau$ for all $n$ (since $\tau_n \ge \tau$), so $\bigcap_n \mathcal{F}_{\tau_n} \supseteq \mathcal{F}_\tau$. For the reverse inclusion, we need $\bigcap_n \mathcal{F}_{\tau_n} \subseteq \mathcal{F}_\tau$. Since $\tau_n \downarrow \tau$, the stopped $\sigma$-algebras satisfy $\bigcap_n \mathcal{F}_{\tau_n} = \mathcal{F}_{\tau+}$ (the right-limit $\sigma$-algebra). Right-continuity of the filtration means $\mathcal{F}_{\tau+} = \mathcal{F}_\tau$, which gives $\bigcap_n \mathcal{F}_{\tau_n} = \mathcal{F}_\tau$. Without right-continuity, $\mathcal{F}_{\tau+}$ could be strictly larger than $\mathcal{F}_\tau$, and the backward martingale convergence argument in Step 3 would not yield the strong Markov property at $\tau$.

??? success "Solution to Exercise 4"
    Consider the following process on $\mathbb{R}$. Let $\xi$ be a uniform random variable on $[0,1]$, and define

    $$
    X_t = \mathbf{1}_{[0,\infty)}(t - \xi)
    $$

    That is, $X_t = 0$ for $t < \xi$ and $X_t = 1$ for $t \ge \xi$. This process has the Markov property at fixed times: given $X_s$, the conditional law of $X_t$ for $t > s$ depends only on $X_s$ (if $X_s = 1$, then $X_t = 1$; if $X_s = 0$, then $X_t = 1$ with probability $(t-s)/(1-s)$ conditional on $\xi > s$).

    Now consider the stopping time $\tau = \inf\{t : X_t = 1\} = \xi$. The strong Markov property would require that, conditionally on $\mathcal{F}_\tau$, the post-$\tau$ process $(X_{\tau+t})_{t \ge 0}$ depends only on $X_\tau = 1$. The future is indeed deterministic ($X_{\tau+t} = 1$ for all $t$), so this particular stopping time does not reveal a failure.

    A cleaner example: let $(Y_t)_{t \ge 0}$ be defined as follows. Let $U \sim \text{Uniform}(0,1)$ and set $Y_t = 0$ for $t \le U$, and for $t > U$ define $Y_t$ to follow one of two deterministic trajectories depending on the **fractional part** of $U$ in a fine way that is invisible at fixed times but revealed at the jump time $\tau = U$.

    More concretely, a classical counterexample uses a **non-Feller** Markov chain in continuous time. Let the state space be $\{0,1,2\}$ with transition rates that depend on time in a discontinuous manner: from state $0$, the process jumps to state $1$ at rate $q(t) = \mathbf{1}_{\mathbb{Q}}(t)$ and to state $2$ at rate $1 - q(t)$. At any fixed time $t$, the transition probabilities are well-defined and the Markov property holds. But at the stopping time $\tau = \inf\{t : X_t \ne 0\}$, the jump destination reveals whether $\tau$ is rational or irrational — information not determined by $X_\tau$ alone — so the strong Markov property fails.

??? success "Solution to Exercise 5"
    For $a > 0$ and $b < a$, define $\tau_a = \inf\{s : W_s = a\}$. By the strong Markov property, $(W_{\tau_a + s} - a)_{s \ge 0}$ is a standard BM independent of $\mathcal{F}_{\tau_a}$.

    We compute $\mathbb{P}(\max_{0 \le s \le t} W_s \ge a,\, W_t \le b)$. On the event $\{\tau_a \le t\}$ (equivalently $\{\max_{s \le t} W_s \ge a\}$), we have

    $$
    W_t = a + (W_t - W_{\tau_a}) = a + B_{t - \tau_a}
    $$

    where $B_s = W_{\tau_a + s} - a$ is a standard BM independent of $\tau_a$. So

    $$
    \mathbb{P}(\tau_a \le t,\, W_t \le b) = \mathbb{P}(\tau_a \le t,\, a + B_{t-\tau_a} \le b)
    $$

    By the reflection principle: on $\{\tau_a \le t\}$, $W_t$ and $2a - W_t$ have the same conditional distribution (since $B_{t-\tau_a}$ and $-B_{t-\tau_a}$ have the same law). Therefore

    $$
    \mathbb{P}(\tau_a \le t,\, W_t \le b) = \mathbb{P}(\tau_a \le t,\, 2a - W_t \le b) = \mathbb{P}(\tau_a \le t,\, W_t \ge 2a - b)
    $$

    Since $b < a$ implies $2a - b > a$, the event $\{W_t \ge 2a - b\}$ implies $\{\tau_a \le t\}$, so

    $$
    \mathbb{P}(\tau_a \le t,\, W_t \ge 2a - b) = \mathbb{P}(W_t \ge 2a - b)
    $$

    Therefore

    $$
    \mathbb{P}\!\left(\max_{0 \le s \le t} W_s \ge a,\; W_t \le b\right) = \mathbb{P}(W_t \ge 2a - b) = 1 - \Phi\!\left(\frac{2a - b}{\sqrt{t}}\right)
    $$

    where $\Phi$ is the standard normal CDF.

??? success "Solution to Exercise 6"
    The Ornstein–Uhlenbeck process $\mathrm{d}X_t = -\theta X_t\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ with $\theta > 0$ has coefficients $b(x) = -\theta x$ and $\sigma(x) = \sigma$ that are globally Lipschitz with linear growth. By the standard existence and uniqueness theorem, the SDE has a unique strong solution.

    The OU semigroup $P_t f(x) = \mathbb{E}^x[f(X_t)]$ satisfies the **Feller property**: $P_t$ maps $C_0(\mathbb{R})$ into $C_0(\mathbb{R})$, and $\|P_t f - f\|_\infty \to 0$ as $t \to 0$. This follows because $X_t = xe^{-\theta t} + \sigma\int_0^t e^{-\theta(t-s)}\,\mathrm{d}W_s$ is Gaussian with mean $xe^{-\theta t}$ and variance $\frac{\sigma^2}{2\theta}(1 - e^{-2\theta t})$, so $P_t f(x) = \int f(xe^{-\theta t} + y)\,\nu_t(\mathrm{d}y)$ for a Gaussian measure $\nu_t$, which preserves continuity and vanishing at infinity.

    By the **general theorem** (Feller process with right-continuous filtration implies strong Markov), the OU process is strong Markov. Therefore, at the stopping time $\tau = \inf\{t : X_t = c\}$, the strong Markov property guarantees:

    $$
    \mathbb{E}[\varphi(X_{\tau+t}) \mid \mathcal{F}_\tau] = \mathbb{E}^{X_\tau}[\varphi(X_t)] = \mathbb{E}^c[\varphi(X_t)]
    $$

    The post-$\tau$ process $(X_{\tau+t})_{t \ge 0}$, conditioned on $\mathcal{F}_\tau$, behaves as an OU process started from $c$, independent of the pre-$\tau$ history. The key property is **Feller continuity** of the semigroup — the continuity $x \mapsto P_t f(x)$ ensures the restart argument works at the random location $X_\tau = c$.

??? success "Solution to Exercise 7"
    **The strong Markov property** concerns the **conditional law** of the future process given $\mathcal{F}_\tau$: it states $\mathbb{E}[\varphi(X_{\tau+t}) \mid \mathcal{F}_\tau] = \mathbb{E}^{X_\tau}[\varphi(X_t)]$. It is a property of **Markov processes** and applies to the full path after $\tau$.

    **The optional sampling theorem (OST)** concerns the **expected value** of a (sub/super)martingale at a stopping time: for a martingale $M$ and bounded stopping times $\sigma \le \tau$, it states $\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma$. It applies to **any** martingale, regardless of whether it is Markov.

    **OST applies, strong Markov not relevant:** Let $Y_t = e^{W_t - t/2}$ (the exponential martingale). Let $\tau = \min(1, \inf\{t : Y_t = 2\})$. The OST gives $\mathbb{E}[Y_\tau] = Y_0 = 1$. Here $Y_t$ is not a Markov process on its own (its conditional expectation depends on $t$, not just $Y_t$), so the strong Markov property for $Y$ is not meaningful.

    **Strong Markov applies, OST not relevant:** Let $X_t$ be an OU process and $\tau = \inf\{t : X_t = c\}$. The strong Markov property tells us the full distributional behavior of $(X_{\tau+t})_{t \ge 0}$. Now consider the submartingale $Y_t = |X_t|$. The OST for submartingales gives the inequality $\mathbb{E}[Y_\tau] \ge Y_0$ (under appropriate integrability), but this says nothing about the post-$\tau$ law. The strong Markov property provides the richer conclusion that the process restarts as an OU process from $c$.
