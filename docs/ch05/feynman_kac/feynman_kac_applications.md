# Feynman Kac


This page has two goals:

1. practice solving PDEs using the probabilistic representation
2. make explicit where the **forward equation** sits inside Feynman–Kac

---

## Application Heat


Solve

\[
V_t + \frac12\sigma^2 V_{xx}=0,\qquad V(T,x)=x^2.
\]



Take the process \(dX_s=\sigma\,dW_s\). By Feynman–Kac (no discount, no running payoff),

\[
V(t,x)=\mathbb E_{t,x}[X_T^2].
\]


Since \(X_T=x+\sigma(W_T-W_t)\),

\[
V(t,x)=x^2+\sigma^2(T-t).
\]



**Exercise:** verify directly that this satisfies the PDE and terminal condition.

---

## Application heat


Solve

\[
V_t + \mu V_x + \frac12\sigma^2 V_{xx}=0,\qquad V(T,x)=x^2.
\]



Take \(dX_s=\mu\,ds+\sigma\,dW_s\). Then \(X_T=x+\mu(T-t)+\sigma(W_T-W_t)\), so

\[
V(t,x)=\mathbb E[X_T^2]=\big(x+\mu(T-t)\big)^2+\sigma^2(T-t).
\]



---

## Where forward


Let \(p(x,t;y,T)\) be the transition density of \(X\). Then (in the simplest case)

\[
u(x,t)=\mathbb E[f(X_T)\mid X_t=x]=\int f(y)\,p(x,t;y,T)\,dy.
\]



- For fixed \((x,t)\), as a function of \((y,T)\), the density \(p\) satisfies the **Kolmogorov forward** equation.
- For fixed \((y,T)\), as a function of \((x,t)\), the same \(p\) satisfies the **Kolmogorov backward** equation.

So even when you “solve the backward PDE for \(u\),” the representation

\[
u(x,t)=\int f(y)\,p(x,t;y,T)\,dy
\]


quietly contains the forward evolution through \(p\).

---

## Summary


- Backward PDE: differential law for \(u\)
- Forward PDE: differential law for \(p\)
- Feynman–Kac: the bridge \(u = \int f\,p\)

---

## Exercises

**Exercise 1.**
Solve the PDE $V_t + \frac{1}{2}\sigma^2 V_{xx} = 0$ with terminal condition $V(T, x) = x^3$ using the Feynman-Kac representation. (Hint: if $X_T = x + \sigma(W_T - W_t)$, compute $\mathbb{E}[X_T^3]$ using the moments of the normal distribution.)

---

**Exercise 2.**
Solve $V_t + \mu V_x + \frac{1}{2}\sigma^2 V_{xx} - rV = 0$ with $V(T, x) = x$ using the discounted Feynman-Kac formula. Verify your answer satisfies the PDE by direct substitution.

---

**Exercise 3.**
Consider the PDE $V_t + \frac{1}{2}\sigma^2 V_{xx} = 0$ with $V(T, x) = e^{ax}$ for constant $a$. Use Feynman-Kac to compute $V(t, x) = \mathbb{E}[e^{aX_T} | X_t = x]$ where $dX_s = \sigma\,dW_s$. Verify that your answer satisfies the PDE.

---

**Exercise 4.**
Explain the relationship between the backward and forward Kolmogorov equations in the context of the Feynman-Kac formula. If $u(x,t) = \int f(y)\,p(x,t;y,T)\,dy$, identify which equation governs $u$ as a function of $(x,t)$ and which governs $p$ as a function of $(y,T)$.

---

**Exercise 5.**
Solve $V_t + \mu V_x + \frac{1}{2}\sigma^2 V_{xx} = 0$ with $V(T, x) = \max(x, 0)$ using Feynman-Kac. Write $V(t, x) = \mathbb{E}[\max(X_T, 0) | X_t = x]$ and express the answer in terms of the standard normal CDF $\Phi$.

---

**Exercise 6.**
Consider $V_t + \frac{1}{2}\sigma^2 V_{xx} + f(x) = 0$ with $V(T, x) = 0$ where $f(x) = 1$. Use the Feynman-Kac formula with running payoff to show that $V(t, x) = T - t$. Verify by substitution into the PDE.

---

**Exercise 7.**
Explain why the Feynman-Kac formula provides two equivalent computational methods: solving the PDE (finite differences) and computing the expectation (Monte Carlo). For a one-dimensional problem on a fine grid, which method is typically more efficient? For a five-dimensional problem, which method is preferred and why?

---

## Solutions

??? success "Solution to Exercise 1"
    With $dX_s = \sigma\,dW_s$ and $X_t = x$, the terminal value is $X_T = x + \sigma(W_T - W_t)$. Let $Z = W_T - W_t \sim N(0, T - t)$.

    Using the Feynman-Kac representation with $r = 0$, $f = 0$:

    $$
    V(t, x) = \mathbb{E}[X_T^3 \mid X_t = x] = \mathbb{E}[(x + \sigma Z)^3]
    $$

    Expanding the cube:

    $$
    (x + \sigma Z)^3 = x^3 + 3x^2(\sigma Z) + 3x(\sigma Z)^2 + (\sigma Z)^3
    $$

    Taking expectations and using $\mathbb{E}[Z] = 0$, $\mathbb{E}[Z^2] = T - t$, $\mathbb{E}[Z^3] = 0$ (odd moments of a Gaussian vanish):

    $$
    V(t, x) = x^3 + 3x\sigma^2(T - t)
    $$

    **Verification**: We check that $V_t + \frac{1}{2}\sigma^2 V_{xx} = 0$. We have $V_t = -3x\sigma^2$, $V_x = 3x^2 + 3\sigma^2(T-t)$, and $V_{xx} = 6x$. Therefore:

    $$
    V_t + \frac{1}{2}\sigma^2 V_{xx} = -3x\sigma^2 + \frac{1}{2}\sigma^2(6x) = -3x\sigma^2 + 3x\sigma^2 = 0 \;\checkmark
    $$

    Terminal condition: $V(T, x) = x^3 + 0 = x^3$. $\checkmark$

??? success "Solution to Exercise 2"
    The PDE is $V_t + \mu V_x + \frac{1}{2}\sigma^2 V_{xx} - rV = 0$ with $V(T, x) = x$.

    By the discounted Feynman-Kac formula with $dX_s = \mu\,ds + \sigma\,dW_s$:

    $$
    V(t, x) = e^{-r(T-t)}\mathbb{E}[X_T \mid X_t = x]
    $$

    Since $X_T = x + \mu(T - t) + \sigma(W_T - W_t)$, we have $\mathbb{E}[X_T \mid X_t = x] = x + \mu(T - t)$, so:

    $$
    V(t, x) = e^{-r(T-t)}(x + \mu(T - t))
    $$

    **Verification by substitution**: Let $\tau = T - t$. Then $V = e^{-r\tau}(x + \mu\tau)$.

    $$
    V_t = re^{-r\tau}(x + \mu\tau) - e^{-r\tau}\mu = rV - \mu e^{-r\tau}
    $$

    $$
    V_x = e^{-r\tau}, \quad V_{xx} = 0
    $$

    Substituting:

    $$
    V_t + \mu V_x + \frac{1}{2}\sigma^2 V_{xx} - rV = rV - \mu e^{-r\tau} + \mu e^{-r\tau} + 0 - rV = 0 \;\checkmark
    $$

    Terminal condition: $V(T, x) = e^0(x + 0) = x$. $\checkmark$

??? success "Solution to Exercise 3"
    With $dX_s = \sigma\,dW_s$ and $g(x) = e^{ax}$, the Feynman-Kac formula gives:

    $$
    V(t, x) = \mathbb{E}[e^{aX_T} \mid X_t = x]
    $$

    Since $X_T = x + \sigma(W_T - W_t)$ and $W_T - W_t \sim N(0, T - t)$:

    $$
    V(t, x) = \mathbb{E}\!\left[e^{a(x + \sigma Z)}\right] = e^{ax}\,\mathbb{E}\!\left[e^{a\sigma Z}\right]
    $$

    where $Z \sim N(0, T - t)$. Using the moment generating function $\mathbb{E}[e^{\lambda Z}] = e^{\lambda^2(T-t)/2}$ with $\lambda = a\sigma$:

    $$
    V(t, x) = e^{ax}\,e^{a^2\sigma^2(T-t)/2} = \exp\!\left(ax + \frac{1}{2}a^2\sigma^2(T - t)\right)
    $$

    **Verification**: $V_t = -\frac{1}{2}a^2\sigma^2 V$, $V_x = aV$, $V_{xx} = a^2 V$. Therefore:

    $$
    V_t + \frac{1}{2}\sigma^2 V_{xx} = -\frac{1}{2}a^2\sigma^2 V + \frac{1}{2}\sigma^2 a^2 V = 0 \;\checkmark
    $$

    Terminal condition: $V(T, x) = e^{ax + 0} = e^{ax}$. $\checkmark$

??? success "Solution to Exercise 4"
    The Feynman-Kac formula involves two functions of the transition density $p(x, t; y, T)$:

    - **As a function of $(x, t)$** (initial condition), $p$ satisfies the **Kolmogorov backward equation**: $\partial_t p + \mathcal{L}_x p = 0$, where $\mathcal{L}_x$ acts on the $x$ variable.
    - **As a function of $(y, T)$** (terminal state and time), $p$ satisfies the **Kolmogorov forward (Fokker-Planck) equation**: $\partial_T p = \mathcal{L}_y^* p$, where $\mathcal{L}_y^*$ is the adjoint of $\mathcal{L}$ acting on $y$.

    The function $u(x, t) = \int f(y)\,p(x, t; y, T)\,dy$ is governed by the **backward equation** as a function of $(x, t)$: since $\mathcal{L}_x$ acts on $p$ and $f(y)$ does not depend on $x$ or $t$, the integral inherits the backward PDE $\partial_t u + \mathcal{L}_x u = 0$.

    The density $p(x, t; y, T)$ appearing inside the integral satisfies the **forward equation** as a function of $(y, T)$. So even though we "solve the backward PDE for $u$," the probabilistic representation $u = \int f\,p\,dy$ implicitly encodes the forward evolution of probability densities through $p$.

??? success "Solution to Exercise 5"
    With $dX_s = \mu\,ds + \sigma\,dW_s$, $X_t = x$, and $g(x) = \max(x, 0)$:

    $$
    V(t, x) = \mathbb{E}[\max(X_T, 0) \mid X_t = x]
    $$

    We have $X_T = x + \mu(T - t) + \sigma\sqrt{T - t}\,Z$ where $Z \sim N(0,1)$. Let $m = x + \mu(T - t)$ and $s = \sigma\sqrt{T - t}$. Then $X_T = m + sZ$ and:

    $$
    V = \mathbb{E}[\max(m + sZ, 0)] = \int_{-m/s}^{\infty}(m + sz)\frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz
    $$

    Splitting the integral:

    $$
    V = m\,\Phi\!\left(\frac{m}{s}\right) + s\,\phi\!\left(\frac{m}{s}\right)
    $$

    where $\Phi$ is the standard normal CDF and $\phi$ is the standard normal PDF. Substituting back:

    $$
    V(t, x) = \bigl(x + \mu(T - t)\bigr)\,\Phi\!\left(\frac{x + \mu(T - t)}{\sigma\sqrt{T - t}}\right) + \sigma\sqrt{T - t}\;\phi\!\left(\frac{x + \mu(T - t)}{\sigma\sqrt{T - t}}\right)
    $$

??? success "Solution to Exercise 6"
    The PDE is $V_t + \frac{1}{2}\sigma^2 V_{xx} + 1 = 0$ with $V(T, x) = 0$. This has $r = 0$, $g(x) = 0$ (terminal), and running payoff $f(x) = 1$.

    By the Feynman-Kac formula with running payoff:

    $$
    V(t, x) = \mathbb{E}\!\left[\int_t^T 1\,ds \,\Big|\, X_t = x\right] = T - t
    $$

    The expectation is simply the length of the interval $[t, T]$, since $f = 1$ is constant and there is no discounting.

    **Verification**: $V(t, x) = T - t$, so $V_t = -1$, $V_{xx} = 0$. Then:

    $$
    V_t + \frac{1}{2}\sigma^2 V_{xx} + 1 = -1 + 0 + 1 = 0 \;\checkmark
    $$

    Terminal condition: $V(T, x) = T - T = 0$. $\checkmark$

??? success "Solution to Exercise 7"
    The Feynman-Kac formula establishes the equivalence $u(t,x) = \mathbb{E}[e^{-\int r\,ds}g(X_T) \mid X_t = x]$, which is simultaneously a PDE solution and an expected value. This gives two computational methods:

    - **PDE approach (finite differences)**: Discretize the spatial domain and march backward from the terminal condition. Cost scales as $O(N^d)$ where $N$ is the number of grid points per dimension and $d$ is the number of spatial dimensions.
    - **Monte Carlo approach**: Simulate paths of $X_t$ and average the discounted payoff. Cost scales as $O(M \cdot n)$ where $M$ is the number of paths and $n$ is the number of time steps, with convergence rate $O(1/\sqrt{M})$ independent of dimension.

    **One-dimensional problem**: Finite differences are typically more efficient. With $N$ grid points, the PDE solver has cost $O(N)$ per time step (tridiagonal system), giving all option values across the entire grid simultaneously. Monte Carlo requires many paths to achieve comparable accuracy.

    **Five-dimensional problem**: Monte Carlo is strongly preferred. The PDE finite difference grid requires $O(N^5)$ points, which becomes computationally intractable even for moderate $N$ (e.g., $N = 100$ gives $10^{10}$ points). Monte Carlo, by contrast, has convergence rate $O(1/\sqrt{M})$ regardless of dimension, making it the only feasible approach. This exponential growth of PDE grid complexity with dimension is known as the **curse of dimensionality**.
