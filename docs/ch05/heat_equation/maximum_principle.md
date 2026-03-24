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
