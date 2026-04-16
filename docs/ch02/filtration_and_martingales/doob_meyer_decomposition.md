# Doob-Meyer Decomposition

By now we know what martingales look like ([Martingales](martingales.md)), when they converge ([Martingale Convergence](martingale_convergence.md)), and why [Uniform Integrability](uniform_integrability.md) is the sharp condition for the $L^1$ theory. The Doob-Meyer decomposition completes this structural picture: every "reasonable" adapted process splits into a **pure-noise martingale** and a **predictable drift**. Itô processes are a special case; the theorem says the structure is universal.

---

## Discrete Time: The Elementary Case

The discrete decomposition requires no heavy machinery.

!!! success "Discrete Doob decomposition"
    Let $(X_n, \mathcal{F}_n)_{n\ge 0}$ be an adapted integrable process. There exist unique processes $M$ (martingale, $M_0 = 0$) and $A$ (predictable, $A_0 = 0$) with

    $$
    X_n = X_0 + M_n + A_n.
    $$

    If $X$ is a submartingale, $A$ is non-decreasing.

**Construction**. Set $A_n - A_{n-1} = \mathbb{E}[X_n - X_{n-1} \mid \mathcal{F}_{n-1}]$; this is $\mathcal{F}_{n-1}$-measurable, so $A$ is predictable. Define $M_n = X_n - X_0 - A_n$; by design $\mathbb{E}[M_n - M_{n-1} \mid \mathcal{F}_{n-1}] = 0$.

**Uniqueness**. Any difference $D_n$ of two such decompositions is both a predictable process and a martingale with $D_0 = 0$. Predictability means $D_n$ is $\mathcal{F}_{n-1}$-measurable, so $\mathbb{E}[D_n - D_{n-1} \mid \mathcal{F}_{n-1}] = D_n - D_{n-1}$. The martingale property also makes this $0$, so $D_n \equiv 0$. $\square$

!!! info "Reading the pieces"
    $A_n$ is the **conditional drift** accumulated through time $n$. $M_n$ is what remains after this drift is removed — the "unanticipated" part of $X_n$.

---

## Continuous Time: Class (D) Submartingales

In continuous time, two refinements are needed: paths should be càdlàg, and the stopped family $\{X_\tau : \tau \text{ bounded stopping time}\}$ should be uniformly integrable. The latter is **class (D)**; it rules out explosions under random sampling. A UI martingale is class (D); $W_t^2$ is not, but $W_{t\wedge T}^2$ is.

!!! success "Doob-Meyer decomposition"
    Every càdlàg submartingale $(X_t)$ of class (D) admits a unique decomposition

    $$
    X_t = X_0 + M_t + A_t
    $$

    with $M$ a càdlàg martingale and $A$ a predictable, non-decreasing, càdlàg process with $A_0 = 0$.

The process $A$ is the **compensator** (or **dual predictable projection**) of $X$: the best predictable drift one can strip away. Without predictability, uniqueness fails — predictability is the essential regularity.

**Idea of proof**. Discretize time along a fine partition, apply the discrete Doob decomposition, and pass to the limit; class (D) provides the uniform integrability needed for the compensators to converge, and properties of the predictable $\sigma$-algebra identify the limit. Uniqueness reduces to: *a predictable local martingale of finite variation starting at $0$ is identically zero*. (In the continuous case this is immediate — such a process has zero quadratic variation.) Details are carried out in Dellacherie-Meyer or Revuz-Yor.

---

## Key Examples

!!! example "Squared Brownian motion"
    By Itô's formula, $W_t^2 = 2\int_0^t W_s\,dW_s + t$. The decomposition reads

    $$
    W_t^2 = M_t + t, \qquad M_t = 2\int_0^t W_s\,dW_s.
    $$

    The compensator $A_t = t$ equals the quadratic variation $[W]_t$.

!!! example "Convex transform of a martingale"
    If $M$ is a continuous martingale and $f \in C^2$ is convex, Itô's formula gives

    $$
    f(M_t) = f(M_0) + \underbrace{\int_0^t f'(M_s)\,dM_s}_{\text{martingale part}} + \underbrace{\tfrac{1}{2}\int_0^t f''(M_s)\,d[M]_s}_{\text{compensator } A_t}.
    $$

    Convexity ($f'' \ge 0$) makes $A_t$ non-decreasing, confirming that $f(M_t)$ is a submartingale.

!!! example "Absolute value and local time"
    $|W_t|$ is a submartingale. Tanaka's formula gives its decomposition

    $$
    |W_t| = \int_0^t \operatorname{sgn}(W_s)\,dW_s + L_t^0,
    $$

    where $L_t^0$ is the local time of $W$ at $0$ — a continuous, non-decreasing process that grows only when $W_t = 0$.

---

## Compensators and Quadratic Variation

For a continuous local martingale $M$, the quadratic variation $[M]_t$ is the unique continuous increasing process such that $M_t^2 - [M]_t$ is a local martingale. Comparing with Doob-Meyer:

$$
\text{quadratic variation of } M \;=\; \text{compensator of } M^2.
$$

For Brownian motion, $[W]_t = t$, recovering $W_t^2 - t$ is a martingale.

---

## Semimartingales

Allowing $A$ to be any adapted càdlàg finite-variation process (not necessarily predictable or increasing) and $M$ to be a local martingale defines the class of **semimartingales**:

$$
X_t = X_0 + M_t + A_t.
$$

Every class (D) submartingale is a semimartingale by Doob-Meyer, and Itô processes are the prime examples. Semimartingales are the natural integrators for stochastic integration, and the class is preserved under $C^2$ transformations via Itô's formula.

---

## Why It Matters

A process is a martingale exactly when its Doob-Meyer compensator vanishes, so the decomposition is the standard tool for testing and for change of measure: Girsanov shifts the compensator, and the risk-neutral measure is the one under which the compensator of discounted prices is zero. This is why the decomposition sits at the foundation of pricing theory.

---

## Exercises

**Exercise 1.** Let $X_n = \sum_{k=1}^n Y_k$ with $Y_k \ge 0$ and $\mathbb{E}[Y_k \mid \mathcal{F}_{k-1}] = c > 0$. Find the Doob decomposition and identify it as a sub- or supermartingale.

??? success "Solution to Exercise 1"
    $A_n - A_{n-1} = \mathbb{E}[X_n - X_{n-1} \mid \mathcal{F}_{n-1}] = \mathbb{E}[Y_n \mid \mathcal{F}_{n-1}] = c$, so $A_n = cn$ (predictable and strictly increasing). The martingale part is $M_n = X_n - cn = \sum_{k=1}^n (Y_k - c)$. Since $A_n$ is increasing, $X_n$ is a submartingale. $\square$

---

**Exercise 2.** Use Itô's formula to find the Doob-Meyer decomposition of $f(W_t)$ for $f \in C^2$ convex. Verify on $f(x) = x^2$ and $f(x) = e^{\theta x}$.

??? success "Solution to Exercise 2"
    Itô's formula gives

    $$
    f(W_t) = f(0) + \int_0^t f'(W_s)\,dW_s + \tfrac{1}{2}\int_0^t f''(W_s)\,ds,
    $$

    so $M_t = \int_0^t f'(W_s)\,dW_s$ (local martingale) and $A_t = \tfrac{1}{2}\int_0^t f''(W_s)\,ds$ (non-decreasing by convexity).

    For $f(x) = x^2$: $M_t = 2\int_0^t W_s\,dW_s$, $A_t = t$. For $f(x) = e^{\theta x}$: $M_t = \theta\int_0^t e^{\theta W_s}\,dW_s$, $A_t = \tfrac{\theta^2}{2}\int_0^t e^{\theta W_s}\,ds$. $\square$

---

**Exercise 3.** State Tanaka's formula for $|W_t|$ and identify the martingale and compensator parts.

??? success "Solution to Exercise 3"
    Tanaka's formula:

    $$
    |W_t| = \int_0^t \operatorname{sgn}(W_s)\,dW_s + L_t^0,
    $$

    where $L_t^0$ is local time at $0$. The martingale part is $M_t = \int_0^t \operatorname{sgn}(W_s)\,dW_s$ (a true martingale, since $|\operatorname{sgn}| \le 1$ gives $L^2$ bound). The compensator is $A_t = L_t^0$: continuous, non-decreasing, grows only on $\{W_t = 0\}$. Classical Itô fails here because $|x|$ is not $C^2$ at $0$; the local time is precisely what records the "kink." $\square$

---

**Exercise 4.** Show uniqueness of the discrete Doob decomposition: a predictable martingale starting at $0$ is identically zero.

??? success "Solution to Exercise 4"
    Let $D$ be predictable and a martingale with $D_0 = 0$. Predictability makes $D_n$ $\mathcal{F}_{n-1}$-measurable, so

    $$
    \mathbb{E}[D_n - D_{n-1} \mid \mathcal{F}_{n-1}] = D_n - D_{n-1}.
    $$

    The martingale property makes the left side $0$. Hence $D_n = D_{n-1}$ a.s., and induction from $D_0 = 0$ gives $D_n = 0$ a.s. for all $n$. $\square$

---

**Exercise 5.** Why is the compensator of a continuous martingale $M$ applied to $M^2$ equal to $[M]$? Illustrate on $M = W$.

??? success "Solution to Exercise 5"
    Itô's formula for $f(x) = x^2$ on the continuous local martingale $M$ gives

    $$
    M_t^2 = M_0^2 + 2\int_0^t M_s\,dM_s + [M]_t,
    $$

    so $M_t^2 - [M]_t$ is a local martingale — the Doob-Meyer martingale part — and $[M]_t$ is the compensator. For $M = W$, $[W]_t = t$, recovering $W_t^2 - t$ as a martingale. $\square$
