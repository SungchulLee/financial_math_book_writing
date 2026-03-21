# Picard Iteration for SDEs

**Picard iteration** (successive approximations) is the constructive proof of
existence and uniqueness for SDEs under Lipschitz and linear growth conditions.
It is the stochastic analogue of the classical Picard–Lindelöf theorem for ODEs.
The conditions that make it work are stated in
[Lipschitz Conditions and Linear Growth](lipschitz_conditions.md).

---

## The Iteration Scheme

Given the SDE in integral form:

$$
X_t = x_0 + \int_0^t b(s, X_s)\,ds + \int_0^t \sigma(s, X_s)\,dW_s
$$

define the sequence $\{X_t^{(n)}\}_{n \geq 0}$ by:

$$
X_t^{(0)} = x_0
$$

$$
\boxed{X_t^{(n+1)} = x_0 + \int_0^t b\!\left(s, X_s^{(n)}\right)ds
+ \int_0^t \sigma\!\left(s, X_s^{(n)}\right)dW_s}
$$

Under Lipschitz and linear growth conditions, $X^{(n)} \to X$ where $X$ is the
unique strong solution.

---

## Convergence Analysis

### Error sequence

Define:

$$
e_n(t) := \mathbb{E}\!\left[\sup_{0 \leq s \leq t}\left|X_s^{(n+1)} - X_s^{(n)}\right|^2\right]
$$

### Step 1 — Bounding the first increment

We need $e_0(T) < \infty$. Starting from $X_t^{(0)} = x_0$:

$$
X_t^{(1)} - X_t^{(0)} = \int_0^t b(s, x_0)\,ds + \int_0^t \sigma(s, x_0)\,dW_s
$$

Since $x_0$ is deterministic, no expectation is needed before applying linear
growth. For the drift term, Cauchy–Schwarz gives:

$$
\sup_{s \leq t}\left|\int_0^s b(u,x_0)\,du\right|^2
\leq t \int_0^t |b(s,x_0)|^2\,ds \leq K^2(1+|x_0|^2)\,t^2
$$

For the stochastic integral term, Doob's maximal inequality followed by the
Itô isometry gives:

$$
\mathbb{E}\!\left[\sup_{s \leq t}\left|\int_0^s \sigma(u,x_0)\,dW_u\right|^2\right]
\leq 4\,\mathbb{E}\!\left|\int_0^t \sigma(s,x_0)\,dW_s\right|^2
= 4\int_0^t |\sigma(s,x_0)|^2\,ds \leq 4K^2(1+|x_0|^2)\,t
$$

where the linear growth condition $|\sigma(s,x_0)|^2 \leq K^2(1+|x_0|^2)$ is
used in both. Combining (and taking the expectation of the deterministic drift
bound):

$$
e_0(t) \leq C(K)(1 + |x_0|^2)\,t
$$

where $C(K)$ is a finite constant depending only on $K$.

### Step 2 — Recursive estimate

For $n \geq 1$, write:

$$
X_t^{(n+1)} - X_t^{(n)}
= \int_0^t \!\left[b\!\left(s,X_s^{(n)}\right) - b\!\left(s,X_s^{(n-1)}\right)\right]ds
+ \int_0^t \!\left[\sigma\!\left(s,X_s^{(n)}\right) - \sigma\!\left(s,X_s^{(n-1)}\right)\right]dW_s
$$

The same three tools as Step 1, now applied to the *differences*, give:

| Tool | Applied to | Outcome |
|---|---|---|
| Cauchy–Schwarz | drift difference integral | $\leq t\int_0^t K^2\mathbb{E}|X_s^{(n)}-X_s^{(n-1)}|^2\,ds$ |
| Doob's maximal inequality | stochastic integral sup | $\leq 4\,\mathbb{E}|M_t|^2$ where $M_t = \int_0^t(\sigma^{(n)}-\sigma^{(n-1)})\,dW$ |
| Itô isometry | $\mathbb{E}|M_t|^2$ | $= \int_0^t\mathbb{E}|\sigma^{(n)}-\sigma^{(n-1)}|^2\,ds \leq 4K^2\int_0^t\mathbb{E}|X_s^{(n)}-X_s^{(n-1)}|^2\,ds$ |

Applying the Lipschitz bound $|b(t,x)-b(t,y)| + |\sigma(t,x)-\sigma(t,y)| \leq K|x-y|$
and combining:

$$
e_n(t) \leq C \int_0^t e_{n-1}(s)\,ds
$$

where $C = C(K, T)$ is a finite constant.

### Step 3 — Factorial decay by induction

**Claim:**

$$
e_n(t) \leq \frac{(Ct)^n}{n!}\,e_0(T)
$$

**Proof.** Base case $n = 0$: this is Step 1. Inductive step: assume the bound
holds at $n-1$. Then by Step 2:

$$
e_n(t) \leq C\int_0^t e_{n-1}(s)\,ds
\leq C\int_0^t \frac{(Cs)^{n-1}}{(n-1)!}\,e_0(T)\,ds
= \frac{C^n\,e_0(T)}{(n-1)!} \cdot \frac{t^n}{n}
= \frac{(Ct)^n}{n!}\,e_0(T). \quad \square
$$

### Step 4 — Convergence in $L^2$

Since $n! \sim (n/e)^n\sqrt{2\pi n}$ grows faster than any exponential,

$$
\sum_{n=0}^\infty \sqrt{e_n(T)}
\leq \sqrt{e_0(T)}\sum_{n=0}^\infty \frac{(CT)^{n/2}}{\sqrt{n!}} < \infty.
$$

Hence $\{X^{(n)}\}$ is Cauchy in $L^2(\Omega; C([0,T]))$ — the Banach space of
square-integrable, a.s.-continuous $\mathbb{R}^d$-valued processes with norm
$\|X\| = \mathbb{E}[\sup_{t \leq T}|X_t|^2]^{1/2}$. By completeness it converges
to a limit $X$. Passing to the limit in the integral equation — using dominated
convergence for the drift (the dominating function $\sup_n |b(s, X_s^{(n)})|$ is
integrable by linear growth and the uniform $L^2$ moment bound from Step 1) and
$L^2$ continuity of the Itô integral for the diffusion — shows $X$ satisfies
the SDE.

---

## Uniqueness

**Theorem.** Under global Lipschitz and linear growth conditions, the solution is unique.

**Proof.** Let $X_t$ and $Y_t$ be two solutions with $X_0 = Y_0 = x_0$. Set
$Z_t = X_t - Y_t$. Then:

$$
Z_t = \int_0^t \bigl[b(s,X_s)-b(s,Y_s)\bigr]\,ds
      + \int_0^t \bigl[\sigma(s,X_s)-\sigma(s,Y_s)\bigr]\,dW_s
$$

By the same estimates as Step 2 (Cauchy–Schwarz + Doob + Itô isometry + Lipschitz):

$$
\mathbb{E}\!\left[\sup_{s \leq t}|Z_s|^2\right] \leq C\int_0^t \mathbb{E}|Z_s|^2\,ds
$$

Since $Z_0 = 0$, Gronwall's inequality gives $\mathbb{E}[\sup_{s \leq t}|Z_s|^2] = 0$
for all $t$, hence $X_t = Y_t$ a.s. $\square$

---

## Example: Linear SDE (Full Iteration)

Consider $dX_t = \alpha X_t\,dt + \beta X_t\,dW_t$ with $X_0 = x_0$. This is
globally Lipschitz with $K = |\alpha| + |\beta|$.

**Iterates:**

$$
X_t^{(0)} = x_0
$$

$$
X_t^{(1)} = x_0 + \int_0^t \alpha x_0\,ds + \int_0^t \beta x_0\,dW_s
= x_0\bigl(1 + \alpha t + \beta W_t\bigr)
$$

Substituting $X_s^{(1)} = x_0(1 + \alpha s + \beta W_s)$ into the iteration:

$$
X_t^{(2)} = x_0\!\left[
  1 + \alpha t + \beta W_t
  + \alpha^2 \frac{t^2}{2}
  + \alpha\beta \int_0^t s\,dW_s
  + \beta^2 \int_0^t W_s\,dW_s
\right]
$$

Both remaining integrals evaluate explicitly. By Itô's formula applied to $sW_s$:

$$
\int_0^t s\,dW_s = tW_t - \int_0^t W_s\,ds
$$

By Itô's formula applied to $f(x) = x^2/2$:

$$
\int_0^t W_s\,dW_s = \tfrac{1}{2}W_t^2 - \tfrac{1}{2}t
$$

Substituting both:

$$
X_t^{(2)} = x_0\!\left[
  1 + \alpha t + \beta W_t
  + \alpha^2 \frac{t^2}{2}
  + \alpha\beta\!\left(tW_t - \int_0^t W_s\,ds\right)
  + \beta^2\!\left(\tfrac{1}{2}W_t^2 - \tfrac{1}{2}t\right)
\right]
$$

This is fully explicit in $t$, $W_t$, and $\int_0^t W_s\,ds$. As $n \to \infty$,
the iterated stochastic integrals form the stochastic exponential series, and the
sequence converges to:

$$
X_t = x_0\exp\!\left[\!\left(\alpha - \tfrac{1}{2}\beta^2\right)t + \beta W_t\right]
$$

This is the unique strong solution (geometric Brownian motion when $\alpha = \mu$,
$\beta = \sigma$), verifiable directly by Itô's formula.

---

## Comparison with ODE Picard Iteration

| Aspect | ODE | SDE |
|---|---|---|
| Iteration | $x^{(n+1)} = x_0 + \int_0^t f(s,x^{(n)})\,ds$ | $X^{(n+1)} = x_0 + \int_0^t b(s,X^{(n)})\,ds + \int_0^t \sigma(s,X^{(n)})\,dW_s$ |
| Convergence metric | $\sup$ norm | $L^2$-$\sup$ norm: $\mathbb{E}[\sup_t|\cdot|^2]^{1/2}$ |
| Extra tools vs ODE | — | Doob's maximal inequality + Itô isometry |
| Decay rate | $(Kt)^n/n!$ | $(Ct)^n/n!$ |
| Uniqueness | Gronwall on $\sup|Z_t|$ | Gronwall on $\mathbb{E}[\sup|Z_t|^2]$ |

---

## Summary

$$
\boxed{X_t^{(n+1)} = x_0 + \int_0^t b\!\left(s, X_s^{(n)}\right)ds
+ \int_0^t \sigma\!\left(s, X_s^{(n)}\right)dW_s \;\xrightarrow{n\to\infty}\; X_t}
$$

The argument has four logical layers:

1. **Linear growth** + Cauchy–Schwarz + Doob + Itô isometry bound the first increment: $e_0(T) < \infty$.
2. **Lipschitz** + the same three tools give the recursive bound $e_n(t) \leq C\int_0^t e_{n-1}(s)\,ds$.
3. **Induction** produces the factorial decay $e_n(t) \leq (Ct)^n e_0(T)/n!$.
4. **Gronwall** with zero initial data closes the uniqueness argument.
