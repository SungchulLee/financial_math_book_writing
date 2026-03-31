# Maximum Principle and Uniqueness

The **maximum principle** is a fundamental property of parabolic equations that provides qualitative information about solutions without explicitly solving the equation. It is the key tool for establishing uniqueness and comparison results.

---

## The Weak Maximum Principle

**Theorem (Weak Maximum Principle)**: Let $u$ be a continuous function on $\overline{Q}_T = [0,T] \times [a,b]$ that satisfies:

$$
\frac{\partial u}{\partial t} - \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \leq 0 \quad \text{in } Q_T = (0,T] \times (a,b)
$$

Then:

$$
\boxed{
\max_{\overline{Q}_T} u = \max_{\Gamma_T} u
}
$$

where $\Gamma_T$ is the **parabolic boundary**:

$$
\Gamma_T = \{0\} \times [a,b] \cup [0,T] \times \{a,b\}
$$

**Interpretation**: A subsolution cannot attain its maximum in the interior—the maximum must occur on the parabolic boundary (initial time or spatial boundary).

---

## The Parabolic Boundary

For the heat equation, information flows **forward in time**. The parabolic boundary excludes the final time:

```
        t = T  ─────────────────  (NOT boundary)
               │                 │
               │     Q_T         │
               │                 │
        t = 0  ═══════════════════  (initial condition)
               x = a            x = b
               
═══ Parabolic boundary Γ_T
─── Not part of boundary
```

---

## Proof of the Weak Maximum Principle

**Proof** (by contradiction):

Suppose $u$ attains its maximum at an interior point $(t_0, x_0) \in Q_T$.

At a maximum:
- $\frac{\partial u}{\partial t}(t_0, x_0) \geq 0$ (if $t_0 < T$) or unrestricted (if $t_0 = T$)
- $\frac{\partial u}{\partial x}(t_0, x_0) = 0$
- $\frac{\partial^2 u}{\partial x^2}(t_0, x_0) \leq 0$

Therefore:

$$
\frac{\partial u}{\partial t} - \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \geq 0 - \frac{1}{2} \cdot 0 = 0
$$

with strict inequality if $u_{xx} < 0$.

This contradicts the assumption $u_t - \frac{1}{2}u_{xx} \leq 0$ (with equality only if $u$ is constant). $\square$

---

## The Strong Maximum Principle

**Theorem (Strong Maximum Principle)**: If $u$ satisfies the heat equation:

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \quad \text{in } Q_T
$$

and attains its maximum at an interior point, then $u$ is **constant**.

**Interpretation**: For true solutions (not just subsolutions), the maximum cannot be attained in the interior unless the function is constant everywhere.

---

## Comparison Principle

**Corollary**: If $u$ and $v$ both solve the heat equation and:

$$
u \leq v \quad \text{on } \Gamma_T
$$

then:

$$
u \leq v \quad \text{in } \overline{Q}_T
$$

**Proof**: Apply the maximum principle to $w = u - v$, which satisfies $w_t = \frac{1}{2}w_{xx}$ and $w \leq 0$ on $\Gamma_T$. $\square$

---

## Uniqueness of Solutions

**Theorem**: The initial-boundary value problem:

$$
\begin{cases}
u_t = \frac{1}{2}u_{xx} & \text{in } Q_T \\
u(0,x) = f(x) & \text{initial condition} \\
u(t,a) = g_a(t), \quad u(t,b) = g_b(t) & \text{boundary conditions}
\end{cases}
$$

has **at most one** solution.

**Proof**: If $u$ and $v$ are two solutions, then $w = u - v$ solves the heat equation with $w = 0$ on $\Gamma_T$. By the maximum principle:

$$
\max w \leq 0 \quad \text{and} \quad \max(-w) \leq 0
$$

Therefore $w \equiv 0$, so $u = v$. $\square$

---

## Stability and Continuous Dependence

**Corollary**: Solutions depend continuously on initial and boundary data.

If $u_1$ and $u_2$ are solutions with data $(f_1, g_1)$ and $(f_2, g_2)$, then:

$$
\|u_1 - u_2\|_\infty \leq \max\left(\|f_1 - f_2\|_\infty, \|g_1 - g_2\|_\infty\right)
$$

**Physical meaning**: Small perturbations in initial/boundary data lead to small perturbations in the solution.

---

## Maximum Principle on Unbounded Domains

For the heat equation on $\mathbb{R}$, we need growth conditions.

**Theorem**: If $u$ solves $u_t = \frac{1}{2}u_{xx}$ on $(0,T) \times \mathbb{R}$ with:

1. $u(0,x) \leq M$ for all $x$
2. $|u(t,x)| \leq Ce^{c|x|^2}$ for some constants $C, c$

Then $u(t,x) \leq M$ for all $(t,x) \in (0,T) \times \mathbb{R}$.

The growth condition prevents pathological solutions (there exist non-unique solutions without it).

---

## Probabilistic Interpretation

The maximum principle has a natural probabilistic meaning:

**For Brownian motion**: If $f \leq M$, then:

$$
u(t,x) = \mathbb{E}[f(x + B_t)] \leq M
$$

The expected value of a bounded function is bounded by the same constant.

**For killed Brownian motion**: With discounting $r > 0$:

$$
u(t,x) = \mathbb{E}[e^{-rT}f(B_T)] \leq e^{-rT}M \leq M
$$

---

## Minimum Principle

By applying the maximum principle to $-u$:

**Theorem**: If $u_t = \frac{1}{2}u_{xx}$ in $Q_T$, then:

$$
\min_{\overline{Q}_T} u = \min_{\Gamma_T} u
$$

---

## Extensions

### 1. Variable Coefficients

For $u_t = \frac{1}{2}\sigma^2(x)u_{xx} + \mu(x)u_x$, the maximum principle holds if $\sigma^2 > 0$ (uniform ellipticity).

### 2. Lower-Order Terms

For $u_t = \frac{1}{2}u_{xx} - c(x)u$ with $c \geq 0$, the maximum principle holds (killing only decreases the solution).

### 3. Systems

Maximum principles for systems of equations are more delicate and may fail without additional structure.

---

## Applications

1. **Uniqueness**: Only one solution to well-posed problems
2. **Bounds**: A priori estimates on solutions
3. **Positivity**: Non-negative initial data yields non-negative solutions
4. **Comparison**: Ordering of solutions from ordering of data
5. **Asymptotic behavior**: Long-time limits

---

## Summary

$$
\boxed{
u_t \leq \frac{1}{2}u_{xx} \implies \max u \text{ occurs on parabolic boundary}
}
$$

| Result | Statement |
|--------|-----------|
| Weak maximum principle | $\max_{\overline{Q}_T} u = \max_{\Gamma_T} u$ |
| Strong maximum principle | Interior max $\Rightarrow$ constant |
| Comparison | $u \leq v$ on $\Gamma_T \Rightarrow u \leq v$ in $Q_T$ |
| Uniqueness | At most one solution |

**The maximum principle is the analytical counterpart of the fact that Brownian motion "explores" the domain, making it impossible for expected values to exceed their boundary values.**

---

## Exercises

**Exercise 1.**
State the weak maximum principle for the heat equation on $\overline{Q}_T = [a, b] \times [0, T]$: if $\partial_t u \leq \frac{1}{2}\partial_{xx}u$ in $Q_T$, then $\max_{\overline{Q}_T}u = \max_{\Gamma_T}u$ where $\Gamma_T$ is the parabolic boundary. Identify $\Gamma_T$ explicitly.

---

**Exercise 2.**
Use the maximum principle to prove uniqueness: if $u$ and $v$ both solve the heat equation with the same initial and boundary conditions, show that $w = u - v$ satisfies $\max|w| = 0$, hence $u = v$.

---

**Exercise 3.**
Give a probabilistic interpretation of the maximum principle using Brownian motion. If $u(t, x) = \mathbb{E}_x[f(W_{\tau \wedge (T-t)})]$ where $\tau$ is the exit time from $(a, b)$, explain why $u$ cannot exceed $\max f$ on the parabolic boundary.

---

**Exercise 4.**
The strong maximum principle states: if $u$ achieves its maximum at an interior point of $Q_T$, then $u$ is constant throughout. Explain the intuition using the heat equation: if the temperature has an interior hot spot, heat would flow away from it, reducing the temperature there.

---

**Exercise 5.**
Apply the comparison principle to option pricing: if two European options have payoffs $g_1(S_T) \leq g_2(S_T)$ for all $S_T$, show that $V_1(t, S) \leq V_2(t, S)$ for all $t < T$ and $S > 0$. Which form of the maximum principle is used?

---

**Exercise 6.**
Consider the heat equation $\partial_t u = \frac{1}{2}\partial_{xx}u$ on $[0, 1] \times [0, T]$ with $u(0, t) = 0$, $u(1, t) = 1$, and $u(x, 0) = x$. Without solving the PDE, use the maximum principle to determine the range of $u$ on the entire domain.

---

**Exercise 7.**
The maximum principle fails for the backward heat equation $\partial_t u = -\frac{1}{2}\partial_{xx}u$. Explain why this equation is ill-posed (solutions can blow up from arbitrarily small perturbations in the initial data), and connect this to the financial fact that we solve the pricing PDE backward in time from the terminal condition.

---

## Solutions

??? success "Solution to Exercise 1"
    The weak maximum principle states: if $u$ is continuous on $\overline{Q}_T = [a,b] \times [0,T]$ and satisfies $\partial_t u \leq \frac{1}{2}\partial_{xx}u$ in the interior $Q_T = (a,b) \times (0,T]$, then:

    $$
    \max_{\overline{Q}_T} u = \max_{\Gamma_T} u
    $$

    where $\Gamma_T$ is the **parabolic boundary**.

    The parabolic boundary consists of those parts of $\partial Q_T$ from which information flows into the domain. Explicitly:

    $$
    \Gamma_T = \bigl(\{0\} \times [a,b]\bigr) \cup \bigl([0,T] \times \{a\}\bigr) \cup \bigl([0,T] \times \{b\}\bigr)
    $$

    This is the bottom edge (initial time $t = 0$ for all $x \in [a,b]$) plus the two lateral edges (spatial boundaries $x = a$ and $x = b$ for all times $t \in [0,T]$). The top edge $\{T\} \times [a,b]$ is **not** part of the parabolic boundary, because the heat equation propagates information forward in time.

??? success "Solution to Exercise 2"
    Let $u$ and $v$ both solve the heat equation $\partial_t w = \frac{1}{2}\partial_{xx}w$ on $Q_T$ with the same initial condition $u(0,x) = v(0,x) = f(x)$ and the same boundary conditions $u(t,a) = v(t,a)$ and $u(t,b) = v(t,b)$.

    Define $w = u - v$. By linearity, $w$ solves the heat equation:

    $$
    \partial_t w = \frac{1}{2}\partial_{xx}w
    $$

    with $w = 0$ on the entire parabolic boundary $\Gamma_T$ (both initial and boundary data are the same).

    Apply the maximum principle to $w$: $\max_{\overline{Q}_T} w = \max_{\Gamma_T} w = 0$.

    Apply the maximum principle to $-w$ (which also solves the heat equation): $\max_{\overline{Q}_T}(-w) = \max_{\Gamma_T}(-w) = 0$.

    Combining: $w \leq 0$ and $-w \leq 0$, so $w = 0$ everywhere. Therefore $\max_{\overline{Q}_T}|w| = 0$, giving $u = v$.

??? success "Solution to Exercise 3"
    In the probabilistic formulation, $u(t,x) = \mathbb{E}_x[f(W_{\tau \wedge (T-t)})]$ where $W$ is Brownian motion starting at $x$ and $\tau$ is the exit time from $(a,b)$.

    The process $W_{\tau \wedge s}$ is a stopped Brownian motion. At the stopping time $\tau \wedge (T-t)$, the Brownian motion is either:

    - At one of the boundary points $\{a, b\}$ (if $\tau \leq T - t$), or
    - At some interior point at the terminal time (if $\tau > T - t$)

    In both cases, $W_{\tau \wedge (T-t)}$ takes values on the parabolic boundary. Since $u(t,x)$ is an expected value of $f$ evaluated at points on the parabolic boundary:

    $$
    u(t,x) = \mathbb{E}_x[f(W_{\tau \wedge (T-t)})] \leq \max_{\Gamma_T} f
    $$

    An expected value (weighted average) of a collection of numbers cannot exceed the maximum of those numbers. This is precisely the maximum principle: the solution $u$ at any interior point is a probability-weighted average of its boundary/initial values, so it cannot exceed the maximum boundary value.

??? success "Solution to Exercise 4"
    Suppose $u$ has an interior maximum at $(t_0, x_0)$ with $0 < t_0 \leq T$ and $a < x_0 < b$.

    At this point, the temperature is higher than at all neighboring points. The heat equation describes diffusion: heat flows from hot regions to cold regions. Since $(t_0, x_0)$ is hotter than its spatial neighbors:

    - $\partial_{xx}u(t_0, x_0) \leq 0$ (the function curves downward at a maximum)

    By the heat equation, $\partial_t u = \frac{1}{2}\partial_{xx}u \leq 0$, meaning the temperature at this point is decreasing (or staying constant) over time. Heat is flowing away from the hot spot to cooler surrounding areas.

    This means the hot spot cannot persist: if it existed at time $t_0$, then at a slightly earlier time $t_0 - \epsilon$, the value must have been at least as large (since the temperature is decreasing). Tracing backward, the maximum must originate from the initial or boundary data. The only way the temperature can be constant (not decreasing) at the hot spot is if $\partial_{xx}u = 0$, which propagates the argument to neighbors, forcing $u$ to be constant everywhere.

??? success "Solution to Exercise 5"
    Since $g_1(S_T) \leq g_2(S_T)$ for all $S_T > 0$, the option prices satisfy $V_i(T, S) = g_i(S)$ at maturity. Both $V_1$ and $V_2$ solve the Black-Scholes PDE:

    $$
    \partial_t V + \frac{1}{2}\sigma^2 S^2 \partial_{SS}V + rS\partial_S V - rV = 0
    $$

    Define $w = V_1 - V_2$. Then $w$ solves the same PDE (by linearity) with terminal condition $w(T, S) = g_1(S_T) - g_2(S_T) \leq 0$.

    After transforming the Black-Scholes PDE into the heat equation (via $x = \log S$, $\tau = T - t$), the terminal condition becomes an initial condition, and the comparison principle (a consequence of the maximum principle) applies:

    $$
    w \leq 0 \quad \text{on } \Gamma_T \implies w \leq 0 \quad \text{everywhere}
    $$

    Therefore $V_1(t, S) \leq V_2(t, S)$ for all $t < T$ and $S > 0$.

    This uses the **comparison principle**, which is a direct corollary of the weak maximum principle applied to $w = V_1 - V_2$.

??? success "Solution to Exercise 6"
    The boundary and initial data are: $u(0, t) = 0$, $u(1, t) = 1$, and $u(x, 0) = x$.

    On the parabolic boundary $\Gamma_T$:

    - At $x = 0$: $u = 0$
    - At $x = 1$: $u = 1$
    - At $t = 0$: $u(x, 0) = x \in [0, 1]$ for $x \in [0, 1]$

    So $\min_{\Gamma_T} u = 0$ and $\max_{\Gamma_T} u = 1$.

    By the maximum principle: $\max_{\overline{Q}_T} u = \max_{\Gamma_T} u = 1$.

    By the minimum principle: $\min_{\overline{Q}_T} u = \min_{\Gamma_T} u = 0$.

    Therefore $0 \leq u(x,t) \leq 1$ for all $(x,t) \in [0,1] \times [0,T]$.

    In fact, the steady-state solution $u_\infty(x) = x$ satisfies the heat equation ($\partial_t u_\infty = 0$, $\partial_{xx} u_\infty = 0$) and matches all the boundary and initial data. By uniqueness, $u(x,t) = x$ for all $t$.

??? success "Solution to Exercise 7"
    The backward heat equation $\partial_t u = -\frac{1}{2}\partial_{xx}u$ is ill-posed because high-frequency perturbations grow exponentially in time rather than decaying.

    Consider the Fourier mode $u(x,t) = e^{\alpha^2 t/2}\sin(\alpha x)$. This solves the backward heat equation:

    $$
    \partial_t u = \frac{\alpha^2}{2}e^{\alpha^2 t/2}\sin(\alpha x), \quad -\frac{1}{2}\partial_{xx}u = \frac{\alpha^2}{2}e^{\alpha^2 t/2}\sin(\alpha x)
    $$

    For large $\alpha$, the growth rate $\alpha^2/2$ is enormous. An initial perturbation of amplitude $\epsilon$ at frequency $\alpha$ grows to $\epsilon e^{\alpha^2 t/2}$, which is unbounded as $\alpha \to \infty$. No matter how small $\epsilon$ is, arbitrarily high frequencies cause the solution to blow up instantly.

    The maximum principle fails because the backward equation has the wrong sign: at an interior maximum, $\partial_{xx}u \leq 0$ gives $\partial_t u = -\frac{1}{2}\partial_{xx}u \geq 0$, meaning the maximum grows rather than shrinks.

    **Financial connection**: In option pricing, the Black-Scholes PDE is naturally posed backward in time (from terminal payoff at $T$ to present value at $t < T$). However, this is well-posed because setting $\tau = T - t$ transforms it into the forward heat equation $\partial_\tau u = \frac{1}{2}\partial_{xx}u$, which is stable. The financial practice of "solving backward from terminal condition" corresponds mathematically to solving the well-posed forward heat equation in the reversed time variable $\tau$.
