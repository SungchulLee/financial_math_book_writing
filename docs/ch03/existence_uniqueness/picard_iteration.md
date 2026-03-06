# Picard Iteration for SDEs

The **Picard iteration** (or **successive approximations**) method is the constructive proof technique for existence and uniqueness of solutions to stochastic differential equations. It is the stochastic analogue of the classical Picard-Lindelöf theorem for ODEs.

---

## The Idea

Given the SDE:

$$
X_t = x_0 + \int_0^t b(s, X_s)\,ds + \int_0^t \sigma(s, X_s)\,dW_s
$$

we construct a sequence of approximations $\{X^{(n)}_t\}$ that converges to the true solution.

---

## The Iteration Scheme

**Step 0**: Start with a constant process:

$$
X_t^{(0)} = x_0
$$

**Step n+1**: Given $X^{(n)}$, define:

$$
\boxed{
X_t^{(n+1)} = x_0 + \int_0^t b(s, X_s^{(n)})\,ds + \int_0^t \sigma(s, X_s^{(n)})\,dW_s
}
$$

**Claim**: Under Lipschitz and linear growth conditions, $X^{(n)} \to X$ as $n \to \infty$, where $X$ is the unique solution.

---

## Convergence Analysis

### Error Definition

Define the error at step $n$:

$$
e_n(t) := \mathbb{E}\left[\sup_{0 \leq s \leq t} |X_s^{(n+1)} - X_s^{(n)}|^2\right]
$$

### Key Estimate

Using Lipschitz continuity, the Itô isometry, and Doob's maximal inequality:

$$
e_n(t) \leq C \int_0^t e_{n-1}(s)\,ds
$$

where $C$ depends on the Lipschitz constant $K$ and dimension.

### Induction

By induction, we obtain:

$$
e_n(t) \leq \frac{(Ct)^n}{n!} e_0(T)
$$

### Convergence

Since $\sum_{n=0}^\infty \frac{(CT)^n}{n!} = e^{CT} < \infty$, we have:

$$
\sum_{n=0}^\infty \sqrt{e_n(T)} < \infty
$$

By completeness of $L^2$, the sequence $X^{(n)}$ converges to a limit $X$ in $L^2(\Omega; C([0,T]))$.

---

## Detailed Proof Sketch

### Step 1: Bound the First Iteration

$$
\mathbb{E}\left[\sup_{s \leq t}|X_s^{(1)} - X_s^{(0)}|^2\right] = \mathbb{E}\left[\sup_{s \leq t}\left|\int_0^s b(u, x_0)\,du + \int_0^s \sigma(u, x_0)\,dW_u\right|^2\right]
$$

Using linear growth: $|b(t,x)|^2 + |\sigma(t,x)|^2 \leq K^2(1 + |x|^2)$

$$
e_0(t) \leq C(1 + |x_0|^2)t
$$

### Step 2: Recursive Bound

For $n \geq 1$:

$$
X_t^{(n+1)} - X_t^{(n)} = \int_0^t [b(s, X_s^{(n)}) - b(s, X_s^{(n-1)})]\,ds + \int_0^t [\sigma(s, X_s^{(n)}) - \sigma(s, X_s^{(n-1)})]\,dW_s
$$

Taking supremum and expectation, using Lipschitz condition:

$$
\mathbb{E}\left[\sup_{s \leq t}|X_s^{(n+1)} - X_s^{(n)}|^2\right] \leq 2T \int_0^t K^2 \mathbb{E}|X_s^{(n)} - X_s^{(n-1)}|^2\,ds + 8K^2 \int_0^t \mathbb{E}|X_s^{(n)} - X_s^{(n-1)}|^2\,ds
$$

The factor 8 comes from Doob's inequality for the martingale part.

### Step 3: Gronwall-Type Iteration

This gives:

$$
e_n(t) \leq C \int_0^t e_{n-1}(s)\,ds
$$

Iterating:

$$
e_n(t) \leq C^n \int_0^t \int_0^{s_1} \cdots \int_0^{s_{n-1}} e_0(s_n)\,ds_n \cdots ds_1 \leq \frac{(Ct)^n}{n!} e_0(T)
$$

---

## Uniqueness

**Suppose** $X$ and $Y$ are two solutions with $X_0 = Y_0 = x_0$.

Define $Z_t = X_t - Y_t$. Then:

$$
Z_t = \int_0^t [b(s, X_s) - b(s, Y_s)]\,ds + \int_0^t [\sigma(s, X_s) - \sigma(s, Y_s)]\,dW_s
$$

By the same estimates as above:

$$
\mathbb{E}\left[\sup_{s \leq t}|Z_s|^2\right] \leq C \int_0^t \mathbb{E}|Z_s|^2\,ds
$$

By Gronwall's inequality, since $Z_0 = 0$:

$$
\mathbb{E}\left[\sup_{s \leq t}|Z_s|^2\right] = 0 \quad \text{for all } t
$$

Therefore $X_t = Y_t$ almost surely.

---

## Example: Geometric Brownian Motion

Consider $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ with $S_0 = s_0$.

**Iteration**:

- $S^{(0)}_t = s_0$
- $S^{(1)}_t = s_0 + \int_0^t \mu s_0\,ds + \int_0^t \sigma s_0\,dW_s = s_0(1 + \mu t + \sigma W_t)$
- $S^{(2)}_t = s_0 + \int_0^t \mu S^{(1)}_s\,ds + \int_0^t \sigma S^{(1)}_s\,dW_s$

As $n \to \infty$, this converges to:

$$
S_t = s_0 \exp\left[(\mu - \tfrac{1}{2}\sigma^2)t + \sigma W_t\right]
$$

---

## Comparison with ODE Picard Iteration

| Aspect | ODE | SDE |
|--------|-----|-----|
| Iteration | $x^{(n+1)} = x_0 + \int_0^t f(s, x^{(n)})\,ds$ | $X^{(n+1)} = x_0 + \int b\,ds + \int \sigma\,dW$ |
| Convergence metric | Supremum norm | $L^2$ supremum norm |
| Key tool | Gronwall inequality | Gronwall + Doob + Itô isometry |
| Rate | $(Kt)^n/n!$ | $(Ct)^n/n!$ |

---

## Practical Considerations

### Numerical Picard Iteration

For numerical purposes, one might truncate after $N$ iterations. The error is bounded by:

$$
\mathbb{E}\left[\sup_{t \leq T}|X_t - X_t^{(N)}|^2\right] \leq \sum_{n=N}^\infty e_n(T) \approx \frac{(CT)^N}{N!}
$$

### When to Use

- **Theoretical proofs**: Standard method for existence/uniqueness
- **Numerical methods**: Rarely used directly (Euler-Maruyama is preferred)
- **Perturbation analysis**: Useful for small-noise expansions

---

## Summary

$$
\boxed{
X_t^{(n+1)} = x_0 + \int_0^t b(s, X_s^{(n)})\,ds + \int_0^t \sigma(s, X_s^{(n)})\,dW_s \xrightarrow{n \to \infty} X_t
}
$$

**Convergence rate**: $\|X - X^{(n)}\|_{L^2} = O\left(\frac{(CT)^{n/2}}{\sqrt{n!}}\right)$

**The Picard iteration is the constructive backbone of SDE existence theory, directly paralleling the classical ODE theory.**
