# Sub- and Supermartingales

Martingales model fair games. Sub- and supermartingales model games that are favorable or unfavorable to the player — they introduce systematic drift while retaining enough structure for powerful theorems to hold.

---

## Definitions

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t), \mathbb{P})$ be a filtered probability space and $(X_t)_{t \ge 0}$ an adapted, integrable process.

**Submartingale**: $X$ is a **submartingale** if for all $0 \le s \le t$:

$$
\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s \quad \text{a.s.}
$$

**Supermartingale**: $X$ is a **supermartingale** if for all $0 \le s \le t$:

$$
\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s \quad \text{a.s.}
$$

**Martingale**: Both conditions hold simultaneously — equivalently, $X$ is both a sub- and a supermartingale.

**Equivalent formulation**: By the tower property, it suffices to check the one-step condition. For discrete time:

- Submartingale: $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \ge X_n$ for all $n$
- Supermartingale: $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \le X_n$ for all $n$

---

## Naming Convention

The terminology is initially counterintuitive. A **sub**martingale has conditional expectations that are **above** the current value, so it tends to rise. A **super**martingale tends to fall.

The names come from the potential-theoretic analogy: a *superharmonic* function $f$ satisfies the mean value inequality $f(x) \ge \frac{1}{|\partial B|}\int_{\partial B} f \, d\sigma$ (value exceeds the mean on surrounding spheres). Correspondingly, a **super**martingale's current value dominates its future conditional expectation.

| Type | Condition | Expected behavior | Analogy |
|------|-----------|------------------|---------|
| Submartingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ | Tends to rise | Subharmonic |
| Martingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s$ | No trend | Harmonic |
| Supermartingale | $\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s$ | Tends to fall | Superharmonic |

---

## Examples

### Submartingales

**Example 1: Brownian motion with positive drift**. Let $X_t = W_t + \mu t$ with $\mu > 0$.

$$
\mathbb{E}[X_t \mid \mathcal{F}_s] = W_s + \mu s + \mu(t - s) = X_s + \mu(t-s) \ge X_s
$$

The drift $\mu > 0$ creates an upward trend. $X$ is a submartingale.

**Example 2: Geometric Brownian Motion**. Let $S_t = e^{\sigma W_t + \mu t}$ with $\mu > -\sigma^2/2$.

By Itô's formula (proved in *Itô's Formula*): $\mathbb{E}[S_t \mid \mathcal{F}_s] = S_s \cdot e^{(\mu + \sigma^2/2)(t-s)}$. This exceeds $S_s$ when $\mu + \sigma^2/2 > 0$, so $S_t$ is a submartingale.

**Example 3: Convex function of a martingale**. If $M_t$ is a martingale and $\varphi$ is convex with $\mathbb{E}|\varphi(M_t)| < \infty$, then $\varphi(M_t)$ is a submartingale.

**Proof**: By conditional Jensen's inequality:

$$
\mathbb{E}[\varphi(M_t) \mid \mathcal{F}_s] \ge \varphi(\mathbb{E}[M_t \mid \mathcal{F}_s]) = \varphi(M_s) \quad \square
$$

**Corollaries**: If $M_t$ is a martingale, then $|M_t|$, $M_t^2$, $(M_t)^+ = \max(M_t, 0)$, and $e^{M_t}$ (when integrable) are all submartingales.

### Supermartingales

**Example 4: Brownian motion with negative drift**. $X_t = W_t + \mu t$ with $\mu < 0$ is a supermartingale.

**Example 5: Exponential process without compensator**. Fix $\theta > 0$. The exponential martingale $e^{\theta W_t - \theta^2 t/2}$ is a positive martingale (see *Brownian Motion Martingales*). Now consider $Y_t = e^{-\theta W_t}$ — the same exponential without the compensator term. Since $e^{-\theta W_t} = e^{-\theta^2 t/2} \cdot e^{-\theta W_t - (-\theta)^2 t/2}$ can be decomposed as a positive martingale multiplied by the decaying factor $e^{-\theta^2 t/2}$, we get $\mathbb{E}[Y_t \mid \mathcal{F}_s] = Y_s \cdot e^{-\theta^2(t-s)/2} \le Y_s$. Hence $Y_t = e^{-\theta W_t}$ is a supermartingale.

**Example 6: Portfolio with transaction costs**. A self-financing portfolio facing proportional transaction costs is typically modeled as a supermartingale under the risk-neutral measure, reflecting the drag of trading costs.

**Example 7: Non-negative supermartingale**. Let $M_t$ be a martingale and $A_t$ an increasing predictable process ($A_0 = 0$). Then $X_t = M_t - A_t$ is a supermartingale:

$$
\mathbb{E}[X_t \mid \mathcal{F}_s] = M_s - \mathbb{E}[A_t \mid \mathcal{F}_s] \le M_s - A_s = X_s
$$

since $A_t \ge A_s$ and $A_t$ is predictable. This is the Doob–Meyer structure in reverse.

---

## Properties

### Closure Under Operations

**Proposition**: 
- If $X$ and $Y$ are submartingales and $a, b \ge 0$, then $aX + bY$ is a submartingale.
- If $X$ is a submartingale and $Y$ is a martingale, then $X + Y$ is a submartingale.
- $\max(X_t, Y_t)$ and $\min(X_t, Y_t)$ of two submartingales need not be a submartingale.

**Important case**: $\max(X_t, c)$ for a constant $c$ is a submartingale when $X_t$ is a submartingale (use $\varphi(x) = \max(x,c)$, which is convex and non-decreasing).

### Expected Value Monotonicity

For a submartingale $(X_t)$: $t \mapsto \mathbb{E}[X_t]$ is non-decreasing.

**Proof**: For $s \le t$:

$$
\mathbb{E}[X_t] = \mathbb{E}[\mathbb{E}[X_t \mid \mathcal{F}_s]] \ge \mathbb{E}[X_s] \quad \square
$$

For a supermartingale, $t \mapsto \mathbb{E}[X_t]$ is non-increasing.

### Stopped Processes

**Proposition**: If $X_t$ is a submartingale (resp. supermartingale) and $\tau$ is a stopping time, then the stopped process $X_{t \wedge \tau}$ is also a submartingale (resp. supermartingale).

---

## The Positive Part Decomposition

Every submartingale can be decomposed using its positive and negative parts. The key fact is:

**Proposition**: $X_t$ is a submartingale if and only if $X_t^+ = \max(X_t, 0)$ is a submartingale and the family $\{(X_\tau)^- : \tau \text{ bounded stopping time}\}$ is uniformly integrable.

More practically, since $x \mapsto x^+$ is convex and non-decreasing, for any submartingale $X$:

$$
X_t^+ \text{ is a submartingale}
$$

This plays a key role in convergence theory (Doob's upcrossing lemma uses $\mathbb{E}[(X_N - a)^+]$).

---

## Continuous-Time Regularity

In continuous time, we impose path regularity to avoid pathological behavior.

**Definition**: A submartingale (or supermartingale) is **regular** if it has a càdlàg modification — a version with right-continuous sample paths that have left limits everywhere.

**Theorem (Doob's Regularity)**: Every $L^1$-bounded submartingale (resp. supermartingale) has a càdlàg modification if the filtration satisfies the usual conditions.

This justifies working with càdlàg paths throughout, which ensures that stopped processes and hitting times behave as expected.

---

## Relationship to the Doob–Meyer Decomposition

The Doob–Meyer decomposition (treated fully in *Doob–Meyer Decomposition*) characterizes submartingales structurally:

**Theorem**: A càdlàg adapted process $X_t$ is a submartingale if and only if it can be written as:

$$
X_t = M_t + A_t
$$

where $M_t$ is a local martingale and $A_t$ is a predictable, non-decreasing process with $A_0 = 0$.

**The compensator $A_t$ is the cumulative drift** — it measures how much the process has risen on average up to time $t$.

**Examples**:

| Submartingale | Martingale part | Compensator |
|---------------|-----------------|-------------|
| $W_t + \mu t$, $\mu > 0$ | $W_t$ | $\mu t$ |
| $W_t^2$ | $W_t^2 - t$ | $t$ |
| $e^{\sigma W_t + \mu t}$, $\mu > -\sigma^2/2$ | (stochastic exponential) | (increasing) |
| $|W_t|$ | $\int_0^t \text{sgn}(W_s)\,dW_s$ | $L_t^0$ (local time) |

---

## Class (D)

A special subclass of supermartingales plays a central role in optional sampling and the Doob–Meyer theorem.

**Definition**: A càdlàg adapted process $X$ is of **class (D)** if:

$$
\{X_\tau : \tau \text{ bounded stopping time}\} \quad \text{is uniformly integrable}
$$

**Why class (D)?** The letter D stands for "Dirichlet" — class (D) processes arise naturally in potential theory as Dirichlet solutions. For supermartingales, class (D) is exactly the condition needed to apply optional sampling at unbounded stopping times.

**Examples**:
- Any uniformly integrable martingale is class (D).
- Bounded supermartingales are class (D).
- $W_t$ on $[0, T]$ is class (D) (by Doob's $L^2$ inequality: $\mathbb{E}[\sup_{t \le T} W_t^2] \le 4T$).
- $W_t^2$ on $[0, \infty)$ is **not** class (D) (the expectation grows without bound).

---

## Optional Sampling for Sub/Supermartingales

The optional sampling theorem extends naturally to sub- and supermartingales.

**Theorem**: Let $X$ be a supermartingale and $0 \le \sigma \le \tau \le T$ bounded stopping times. Then:

$$
\mathbb{E}[X_\tau \mid \mathcal{F}_\sigma] \le X_\sigma \quad \text{a.s.}
$$

For submartingales, the inequality reverses.

**Consequence for supermartingales**: $\mathbb{E}[X_\tau] \le \mathbb{E}[X_0]$. The expected value can only decrease at random stopping times — stopping early is weakly beneficial for a supermartingale player.

**Financial interpretation**: If a discounted portfolio process is a supermartingale (modeling transaction costs or fees), then no admissible stopping strategy can produce a positive expected gain over the initial value.

---

## Convergence of Non-Negative Supermartingales

Non-negative supermartingales converge almost surely without any additional conditions — a powerful result.

**Theorem**: Let $(X_t)_{t \ge 0}$ be a non-negative supermartingale (with càdlàg paths). Then:

$$
X_\infty := \lim_{t \to \infty} X_t \quad \text{exists a.s. and } \mathbb{E}[X_\infty] \le \mathbb{E}[X_0]
$$

**Proof**: Since $X_t \ge 0$, we have $\mathbb{E}[X_t] \le \mathbb{E}[X_0]$ (from the supermartingale property), so $\sup_t \mathbb{E}[X_t] \le \mathbb{E}[X_0] < \infty$. Since $-X_t$ is a submartingale and $L^1$-bounded (as $\mathbb{E}[-X_t] \ge -\mathbb{E}[X_0]$), Doob's a.s. convergence theorem applied to $-X_t$ yields that $-X_t$, hence $X_t$, converges a.s. $\square$

**Important**: The inequality $\mathbb{E}[X_\infty] \le \mathbb{E}[X_0]$ may be strict (the limit has smaller expectation than the start). This happens when probability mass "escapes to infinity."

**Example**: The exponential martingale $Z_t = e^{\theta W_t - \theta^2 t/2}$ is a non-negative martingale. It satisfies $Z_t \to 0$ a.s. even though $\mathbb{E}[Z_t] = 1$ for all $t$. As a positive supermartingale, the theorem says $Z_\infty$ exists a.s. (and equals 0), confirming $\mathbb{E}[Z_\infty] = 0 < 1 = \mathbb{E}[Z_0]$.

---

## Summary

| Concept | Condition | Key implication |
|---------|-----------|----------------|
| Submartingale | $\mathbb{E}[X_t\|\mathcal{F}_s] \ge X_s$ | $\mathbb{E}[X_t]$ is non-decreasing |
| Supermartingale | $\mathbb{E}[X_t\|\mathcal{F}_s] \le X_s$ | $\mathbb{E}[X_t]$ is non-increasing |
| Convex of martingale | $\varphi(M_t)$, $\varphi$ convex | Submartingale (Jensen) |
| Doob–Meyer | $X_t = M_t + A_t$ | Submartingale iff $A_t$ increasing |
| Class (D) | UI over bounded stopping times | Optional sampling, Doob–Meyer apply |
| Non-negative supermartingale | $X_t \ge 0$ | Always converges a.s. |

---

## Exercises

### Exercise 1: Verifying Sub/Supermartingales

(a) Let $X_t = e^{W_t}$. Show that $X_t$ is a submartingale. Is it a supermartingale?

*Hint*: Compute $\mathbb{E}[e^{W_t} \mid \mathcal{F}_s]$ using the independence of the increment $W_t - W_s$.

(b) Let $X_n = \left(\frac{q}{p}\right)^{S_n}$ where $S_n$ is a random walk with $\mathbb{P}(\xi = +1) = p > 1/2$ and $\mathbb{P}(\xi = -1) = q = 1-p$. Is $X_n$ a martingale, submartingale, or supermartingale?

(c) Let $M_t$ be a martingale. For which values of $\alpha > 0$ is $|M_t|^\alpha$ a submartingale?

### Exercise 2: Jensen Applications

(a) Prove: if $M_t$ is a martingale with $\mathbb{E}[M_t^2] < \infty$ for all $t$, then $M_t^2$ is a submartingale.

(b) Show that $(M_t - c)^+ = \max(M_t - c, 0)$ is a submartingale for any constant $c$. What is the financial interpretation?

(c) Give an example of a martingale $M_t$ and a function $f$ such that $f(M_t)$ is a submartingale but not of the form $\varphi(M_t)$ for convex $\varphi$.

### Exercise 3: Expected Value Monotonicity

(a) Prove that if $X_t$ is a submartingale, then $t \mapsto \mathbb{E}[X_t]$ is non-decreasing.

(b) Suppose $\mathbb{E}[X_t] = \mathbb{E}[X_0]$ for all $t$ in a submartingale. What can you conclude?

(c) A process $(X_t)$ has $\mathbb{E}[X_t] \to L$ as $t \to \infty$. Must it converge a.s.? Provide an example or counterexample.

### Exercise 4: Stopping

(a) Prove that if $X_t$ is a supermartingale and $\tau$ is a bounded stopping time, then $\mathbb{E}[X_\tau] \le \mathbb{E}[X_0]$.

(b) Suppose a gambler plays a supermartingale game (expected value decreases at each step). Prove that no bounded stopping time can make the game favorable in expectation.

(c) Does the conclusion of (b) hold for unbounded stopping times? Construct a counterexample or prove it holds.

### Exercise 5: Non-Negative Supermartingales

(a) Let $Z_t = e^{\theta W_t - \theta^2 t/2}$ for $\theta \neq 0$. Verify $Z_t$ is a non-negative martingale with $Z_t \to 0$ a.s. Show this is consistent with the non-negative supermartingale convergence theorem.

(b) Let $(X_t)$ be a non-negative supermartingale. Show that for any $\lambda > 0$:

$$
\lambda \cdot \mathbb{P}\left(\sup_{t \ge 0} X_t \ge \lambda\right) \le \mathbb{E}[X_0]
$$

*Hint*: Apply optional sampling to $\tau = \inf\{t : X_t \ge \lambda\}$.

(c) Use (b) to bound $\mathbb{P}(\sup_{t \ge 0} e^{\theta W_t - \theta^2 t/2} \ge K)$ for $K > 1$.

---

## Solutions

??? success "Solution to Exercise 1"
    **(a)** Compute $\mathbb{E}[e^{W_t} \mid \mathcal{F}_s]$ for $s \le t$. Write $e^{W_t} = e^{W_s} \cdot e^{W_t - W_s}$.

    $$
    \mathbb{E}[e^{W_t} \mid \mathcal{F}_s] = e^{W_s} \cdot \mathbb{E}[e^{W_t - W_s}] = e^{W_s} \cdot e^{(t-s)/2}
    $$

    Since $e^{(t-s)/2} > 1$ for $t > s$, we have $\mathbb{E}[e^{W_t} \mid \mathcal{F}_s] > e^{W_s}$, so $e^{W_t}$ is a **submartingale**.

    It is not a supermartingale (the inequality goes the wrong way), so it is not a martingale either.

    **(b)** Let $r = q/p$ where $q = 1 - p$. We compute:

    $$
    \mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = \mathbb{E}[r^{S_{n+1}} \mid \mathcal{F}_n] = r^{S_n} \cdot \mathbb{E}[r^{\xi_{n+1}}]
    $$

    $$
    \mathbb{E}[r^{\xi_{n+1}}] = p \cdot r + q \cdot r^{-1} = p \cdot \frac{q}{p} + q \cdot \frac{p}{q} = q + p = 1
    $$

    Therefore $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$, and $X_n$ is a **martingale** for all $p \in (0, 1)$.

    **(c)** $|M_t|^\alpha$ is a submartingale when $\alpha \ge 1$. The function $\varphi(x) = |x|^\alpha$ is convex for $\alpha \ge 1$ (its second derivative is $\alpha(\alpha - 1)|x|^{\alpha - 2} \ge 0$). By conditional Jensen:

    $$
    \mathbb{E}[|M_t|^\alpha \mid \mathcal{F}_s] \ge |\mathbb{E}[M_t \mid \mathcal{F}_s]|^\alpha = |M_s|^\alpha
    $$

    For $0 < \alpha < 1$, $\varphi(x) = |x|^\alpha$ is concave, and Jensen gives the reverse inequality:

    $$
    \mathbb{E}[|M_t|^\alpha \mid \mathcal{F}_s] \le |M_s|^\alpha
    $$

    So $|M_t|^\alpha$ is a supermartingale for $0 < \alpha < 1$.

??? success "Solution to Exercise 2"
    **(a)** Since $M_t$ is a martingale with $\mathbb{E}[M_t^2] < \infty$, the function $\varphi(x) = x^2$ is convex. By conditional Jensen:

    $$
    \mathbb{E}[M_t^2 \mid \mathcal{F}_s] \ge (\mathbb{E}[M_t \mid \mathcal{F}_s])^2 = M_s^2
    $$

    So $M_t^2$ is a submartingale. $\square$

    **(b)** The function $\varphi(x) = (x - c)^+ = \max(x - c, 0)$ is convex (it is the maximum of the linear function $x - c$ and the constant 0). By conditional Jensen:

    $$
    \mathbb{E}[(M_t - c)^+ \mid \mathcal{F}_s] \ge (\mathbb{E}[M_t \mid \mathcal{F}_s] - c)^+ = (M_s - c)^+
    $$

    **Financial interpretation**: If $M_t$ represents the price of an underlying asset (a martingale under the risk-neutral measure) and $c$ is the strike price, then $(M_t - c)^+$ is the intrinsic value of a European call option. The submartingale property says the expected intrinsic value increases over time — reflecting the growing "optionality" as time progresses.

    **(c)** Consider the two-dimensional Brownian motion case. Let $W_t^{(1)}, W_t^{(2)}$ be independent Brownian motions and $M_t = W_t^{(1)}$. Define $f(x) = \mathbb{E}[g(x, W_1^{(2)})]$ for some carefully chosen $g$. This is somewhat contrived.

    A simpler observation: let $M_t = W_t$ and define $f(M_t, t) = W_t^2 - t$. This is a martingale. But $f(x) = x^2 - t$ depends on $t$ as well as $x$, so it's not of the form $\varphi(M_t)$ for a fixed function $\varphi$. However, the exercise asks for $f(M_t)$ that is a submartingale but not $\varphi(M_t)$ for convex $\varphi$, which requires a time-dependent $f$ or a more elaborate construction.

    As a concrete example: the constant function $f \equiv 0$ gives a trivial martingale (hence submartingale), but this is $\varphi(M_t)$ with $\varphi \equiv 0$ (convex). The key point is that time-dependent submartingale transforms like $M_t^2 - t + t = M_t^2$ can be expressed as convex functions of $M_t$, so distinguishing these cases requires external randomness or time dependence in $f$.

??? success "Solution to Exercise 3"
    **(a)** For a submartingale $X_t$ and $s \le t$:

    $$
    \mathbb{E}[X_t] = \mathbb{E}[\mathbb{E}[X_t \mid \mathcal{F}_s]] \ge \mathbb{E}[X_s]
    $$

    The inequality uses the submartingale property $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ and monotonicity of expectation. $\square$

    **(b)** If $\mathbb{E}[X_t] = \mathbb{E}[X_0]$ for all $t$ and $X_t$ is a submartingale, then $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ with $\mathbb{E}[\mathbb{E}[X_t \mid \mathcal{F}_s]] = \mathbb{E}[X_t] = \mathbb{E}[X_s]$.

    If $\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s$ a.s. and $\mathbb{E}[\mathbb{E}[X_t \mid \mathcal{F}_s] - X_s] = 0$, then $\mathbb{E}[X_t \mid \mathcal{F}_s] - X_s \ge 0$ a.s. with expectation 0, which forces $\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s$ a.s. Therefore $X_t$ is actually a **martingale**.

    **(c)** No, convergence of $\mathbb{E}[X_t]$ does not imply a.s. convergence. **Counterexample**: Let $X_n = (-1)^n$. Then $\mathbb{E}[X_n] = (-1)^n$ does not converge. Instead, let $X_n = \mathbf{1}_{A_n}$ where $A_n$ cycles through events of measure $1/2$: $A_n = [0, 1/2)$ for $n$ even and $A_n = [1/2, 1)$ for $n$ odd. Then $\mathbb{E}[X_n] = 1/2$ for all $n$ (converges to $1/2$), but $X_n(\omega)$ oscillates between 0 and 1 for every $\omega$, so there is no a.s. convergence.

??? success "Solution to Exercise 4"
    **(a)** Let $\tau$ be a bounded stopping time with $\tau \le T$. Since $X_t$ is a supermartingale, the stopped process $X_{t \wedge \tau}$ is also a supermartingale. Therefore:

    $$
    \mathbb{E}[X_\tau] = \mathbb{E}[X_{T \wedge \tau}] \le \mathbb{E}[X_0]
    $$

    The last inequality uses the supermartingale property at times $0$ and $T$: $\mathbb{E}[X_{T \wedge \tau} \mid \mathcal{F}_0] \le X_0$, and taking expectations gives $\mathbb{E}[X_{T \wedge \tau}] \le \mathbb{E}[X_0]$. $\square$

    **(b)** For any bounded stopping time $\tau \le T$, part (a) gives $\mathbb{E}[X_\tau] \le \mathbb{E}[X_0]$. Since the expected value at any bounded stopping time is at most the starting value, no bounded stopping rule can make the game favorable (i.e., achieve $\mathbb{E}[X_\tau] > \mathbb{E}[X_0]$). $\square$

    **(c)** For unbounded stopping times, the conclusion can fail without additional conditions. **Counterexample**: Let $S_n$ be a symmetric random walk ($p = 1/2$), so $-S_n$ is also a martingale (hence a supermartingale). Define $\tau = \inf\{n : S_n = -1\}$. Then $\mathbb{P}(\tau < \infty) = 1$ and $S_\tau = -1$, so $\mathbb{E}[-S_\tau] = 1 > 0 = \mathbb{E}[-S_0]$. The supermartingale $-S_n$ has $\mathbb{E}[(-S)_\tau] > \mathbb{E}[(-S)_0]$, contradicting the inequality. This works because $\tau$ is unbounded ($\mathbb{E}[\tau] = \infty$).

??? success "Solution to Exercise 5"
    **(a)** $Z_t = e^{\theta W_t - \theta^2 t/2}$ is a positive martingale with $\mathbb{E}[Z_t] = 1$ (proved in the text on Brownian motion martingales).

    To show $Z_t \to 0$ a.s.: take logarithms: $\log Z_t = \theta W_t - \frac{\theta^2}{2}t$. By the law of the iterated logarithm, $W_t / t \to 0$ a.s., so $\theta W_t = o(t)$. Therefore $\log Z_t \sim -\frac{\theta^2}{2}t \to -\infty$ a.s., giving $Z_t \to 0$ a.s.

    This is consistent with the non-negative supermartingale convergence theorem: $Z_t$ is a non-negative martingale (hence supermartingale), so $Z_\infty = \lim_{t \to \infty} Z_t$ exists a.s. We have shown $Z_\infty = 0$ a.s. The theorem also states $\mathbb{E}[Z_\infty] \le \mathbb{E}[Z_0] = 1$, which is satisfied since $\mathbb{E}[Z_\infty] = 0 < 1$.

    **(b)** Let $\tau = \inf\{t : X_t \ge \lambda\}$. If $\sup_{t \ge 0} X_t \ge \lambda$, then $\tau < \infty$ and $X_\tau \ge \lambda$ (by right-continuity).

    By optional sampling for the supermartingale $X$ at the bounded stopping time $\tau \wedge T$:

    $$
    \mathbb{E}[X_{\tau \wedge T}] \le \mathbb{E}[X_0]
    $$

    On the event $\{\tau \le T\}$, $X_{\tau \wedge T} = X_\tau \ge \lambda$. Therefore:

    $$
    \mathbb{E}[X_0] \ge \mathbb{E}[X_{\tau \wedge T}] \ge \mathbb{E}[X_\tau \mathbf{1}_{\{\tau \le T\}}] \ge \lambda \cdot \mathbb{P}(\tau \le T)
    $$

    Letting $T \to \infty$: $\lambda \cdot \mathbb{P}(\tau < \infty) \le \mathbb{E}[X_0]$. Since $\{\sup_{t \ge 0} X_t \ge \lambda\} = \{\tau < \infty\}$:

    $$
    \lambda \cdot \mathbb{P}\left(\sup_{t \ge 0} X_t \ge \lambda\right) \le \mathbb{E}[X_0] \quad \square
    $$

    **(c)** Apply (b) with $X_t = Z_t = e^{\theta W_t - \theta^2 t/2}$ (a non-negative martingale, hence supermartingale) and $\lambda = K$:

    $$
    K \cdot \mathbb{P}\left(\sup_{t \ge 0} e^{\theta W_t - \theta^2 t/2} \ge K\right) \le \mathbb{E}[Z_0] = 1
    $$

    Therefore:

    $$
    \mathbb{P}\left(\sup_{t \ge 0} e^{\theta W_t - \theta^2 t/2} \ge K\right) \le \frac{1}{K}
    $$
