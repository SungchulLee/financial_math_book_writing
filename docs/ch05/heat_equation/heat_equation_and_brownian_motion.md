# Heat Equation and Brownian Motion

The heat equation provides the **analytical description** of Brownian motion. This connection is one of the most beautiful correspondences in mathematics, linking probability theory to partial differential equations.

---

## The Fundamental Connection

Let $(B_t)_{t \geq 0}$ be a standard Brownian motion starting at $0$.

**Theorem**: The density of $B_t$ is the heat kernel:

$$
\boxed{
p_{B_t}(x) = \frac{1}{\sqrt{2\pi t}} \exp\left(-\frac{x^2}{2t}\right) = G(t,x)
}
$$

This density **solves the heat equation** with initial condition $\delta_0$.

---

## Expectation Representation

For any bounded measurable function $f$, define:

$$
u(t,x) = \mathbb{E}[f(x + B_t)] = \mathbb{E}[f(B_t) \mid B_0 = x]
$$

**Theorem**: The function $u$ solves the **initial value problem**:

$$
\boxed{
\begin{cases}
\displaystyle\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2} & t > 0 \\[1em]
u(0,x) = f(x)
\end{cases}
}
$$

**Proof**: 

Using the convolution formula:

$$
u(t,x) = \int_{\mathbb{R}} f(y) G(t, y-x)\,dy = \int_{\mathbb{R}} f(x+z) G(t,z)\,dz
$$

Since $G$ solves the heat equation and differentiation commutes with integration:

$$
\frac{\partial u}{\partial t} = \int f(x+z) \frac{\partial G}{\partial t}(t,z)\,dz = \frac{1}{2}\int f(x+z) \frac{\partial^2 G}{\partial z^2}(t,z)\,dz = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}
$$

The initial condition follows from $G(t,\cdot) \to \delta_0$ as $t \to 0$. $\square$

---

## The Generator Connection

The **infinitesimal generator** of Brownian motion is:

$$
\mathcal{L}f(x) = \lim_{t \to 0} \frac{\mathbb{E}_x[f(B_t)] - f(x)}{t} = \frac{1}{2}f''(x)
$$

**The heat equation is**: $u_t = \mathcal{L}u$

This generalizes: for any diffusion with generator $\mathcal{L}$, expected values satisfy $u_t = \mathcal{L}u$.

---

## Probabilistic Interpretation of PDE Concepts

| PDE Concept | Probabilistic Meaning |
|-------------|----------------------|
| $u(t,x)$ | $\mathbb{E}[f(B_t) \mid B_0 = x]$ |
| $G(t,x)$ | Density of $B_t$ |
| $u_t = \frac{1}{2}u_{xx}$ | Generator equation |
| Smoothing | Averaging over paths |
| Maximum principle | $B_t$ visits all points |
| Conservation | Total probability = 1 |

---

## The Martingale Connection

**Theorem**: If $u$ solves $u_t = \frac{1}{2}u_{xx}$, then:

$$
M_t := u(T-t, B_t)
$$

is a **martingale** for $0 \leq t \leq T$.

**Proof**: Apply Itô's lemma to $u(T-t, B_t)$:

$$
dM_t = \left(-\frac{\partial u}{\partial t} + \frac{1}{2}\frac{\partial^2 u}{\partial x^2}\right)dt + \frac{\partial u}{\partial x}dB_t
$$

Since $u$ solves the heat equation (with time running backward), the $dt$ term vanishes:

$$
dM_t = \frac{\partial u}{\partial x}(T-t, B_t)\,dB_t
$$

This is a local martingale (and a true martingale under growth conditions). $\square$

**Consequence**: $u(T,x) = \mathbb{E}[M_T \mid M_0] = \mathbb{E}[u(0, B_T) \mid B_0 = x] = \mathbb{E}[f(B_T) \mid B_0 = x]$

---

## Solving the Heat Equation via Simulation

The probabilistic representation enables **Monte Carlo methods**:

**Algorithm**:
1. Generate $N$ independent samples $B_t^{(1)}, \ldots, B_t^{(N)}$ of Brownian motion at time $t$
2. Estimate: $u(t,x) \approx \frac{1}{N}\sum_{i=1}^N f(x + B_t^{(i)})$

**Advantages**:
- Works in high dimensions (no curse of dimensionality for well-behaved $f$)
- Easy to implement
- Naturally parallelizable

**Disadvantages**:
- Slow convergence: error $\sim 1/\sqrt{N}$
- Variance reduction may be needed

---

## Exit Problems and Boundary Conditions

For Brownian motion in a domain $D$, define the **exit time**:

$$
\tau = \inf\{t > 0 : B_t \notin D\}
$$

**Theorem (Kakutani)**: The function:

$$
u(x) = \mathbb{E}_x[f(B_\tau)]
$$

solves the **Dirichlet problem**:

$$
\begin{cases}
\frac{1}{2}\Delta u = 0 & \text{in } D \\
u = f & \text{on } \partial D
\end{cases}
$$

This connects harmonic functions (solutions to Laplace's equation) to Brownian motion.

---

## The Reflection Principle

For Brownian motion hitting a boundary, the **reflection principle** provides:

$$
\mathbb{P}\left(\max_{0 \leq s \leq t} B_s \geq a\right) = 2\mathbb{P}(B_t \geq a) = 2\Phi\left(-\frac{a}{\sqrt{t}}\right)
$$

for $a > 0$.

**PDE interpretation**: This relates to boundary conditions for the heat equation on a half-line.

---

## Heat Equation with Drift

For Brownian motion with drift $dX_t = \mu\,dt + dB_t$:

$$
u(t,x) = \mathbb{E}[f(X_t) \mid X_0 = x]
$$

solves the **advection-diffusion equation**:

$$
\frac{\partial u}{\partial t} = -\mu\frac{\partial u}{\partial x} + \frac{1}{2}\frac{\partial^2 u}{\partial x^2}
$$

The generator becomes $\mathcal{L} = \mu\partial_x + \frac{1}{2}\partial_{xx}$.

---

## From Heat Equation to Feynman-Kac

The connection extends naturally:

| Equation | Probabilistic Representation |
|----------|------------------------------|
| $u_t = \frac{1}{2}u_{xx}$ | $\mathbb{E}[f(B_T) \mid B_0 = x]$ |
| $u_t = \mathcal{L}u$ | $\mathbb{E}[f(X_T) \mid X_0 = x]$ (general diffusion) |
| $u_t = \mathcal{L}u - ru$ | $\mathbb{E}[e^{-rT}f(X_T) \mid X_0 = x]$ (discounted) |
| $u_t = \mathcal{L}u - ru + g$ | $\mathbb{E}[\int_0^T e^{-rs}g(X_s)ds + e^{-rT}f(X_T)]$ |

This hierarchy leads to the **Feynman-Kac theorem**.

---

## Historical Development

1. **Einstein (1905)**: Physical theory of Brownian motion, diffusion equation
2. **Smoluchowski (1906)**: Independent derivation
3. **Wiener (1923)**: Rigorous construction of Brownian motion
4. **Kolmogorov (1931)**: General theory of diffusions and PDEs
5. **Kakutani (1944)**: Brownian motion solves Dirichlet problem
6. **Kac (1949)**: Probabilistic representation of PDE solutions

---

## Summary

$$
\boxed{
\mathbb{E}[f(B_t) \mid B_0 = x] = \int_{\mathbb{R}} f(y) G(t, y-x)\,dy \quad \text{solves} \quad u_t = \frac{1}{2}u_{xx}
}
$$

The heat equation-Brownian motion connection establishes:

| Probability | Analysis |
|-------------|----------|
| Brownian paths | Solutions to heat equation |
| Expected values | Convolution with heat kernel |
| Generator | Differential operator |
| Martingales | Harmonic functions |
| Exit times | Boundary value problems |

**This connection is the prototype for Feynman-Kac, risk-neutral pricing, and all probabilistic methods in PDE theory.**

---

## Exercises

**Exercise 1.**
Let $W_t$ be a standard Brownian motion. Show that $u(t, x) = \mathbb{E}[f(x + W_{T-t})]$ solves $\partial_t u + \frac{1}{2}\partial_{xx}u = 0$ for $t < T$ with terminal condition $u(T, x) = f(x)$. What is the connection to the heat kernel convolution?

??? success "Solution to Exercise 1"
    Define $u(t,x) = \mathbb{E}[f(x + W_{T-t})]$. Using the convolution representation:

    $$
    u(t,x) = \int_{-\infty}^{\infty} f(y)\,G(T-t, y-x)\,dy
    $$

    where $G(s,z) = (2\pi s)^{-1/2}\exp(-z^2/(2s))$.

    **Computing $\partial_t u$**: Since the time variable enters through $T - t$:

    $$
    \partial_t u = \int f(y)\,\frac{\partial}{\partial t}G(T-t, y-x)\,dy = -\int f(y)\,\frac{\partial G}{\partial s}(T-t, y-x)\,dy
    $$

    **Computing $\partial_{xx} u$**: Differentiating twice in $x$:

    $$
    \partial_{xx} u = \int f(y)\,\frac{\partial^2 G}{\partial x^2}(T-t, y-x)\,dy = \int f(y)\,\frac{\partial^2 G}{\partial z^2}(T-t, y-x)\,dy
    $$

    Since $G$ satisfies the heat equation $\frac{\partial G}{\partial s} = \frac{1}{2}\frac{\partial^2 G}{\partial z^2}$, we have:

    $$
    \partial_t u + \frac{1}{2}\partial_{xx}u = -\int f(y)\frac{\partial G}{\partial s}\,dy + \frac{1}{2}\int f(y)\frac{\partial^2 G}{\partial z^2}\,dy = 0
    $$

    For the terminal condition, as $t \to T$, $T - t \to 0$ and $G(T-t, \cdot) \to \delta_0$, so $u(T,x) = f(x)$.

    **Connection to heat kernel convolution**: This is the backward-in-time heat equation. Setting $s = T - t$, the function $v(s,x) = u(T-s,x) = \mathbb{E}[f(x + W_s)]$ solves the forward heat equation $\partial_s v = \frac{1}{2}\partial_{xx}v$ with initial condition $v(0,x) = f(x)$.

---

**Exercise 2.**
A function $h(x)$ is harmonic for Brownian motion on $(a, b)$ if $\frac{1}{2}h''(x) = 0$. Show that $h(x) = \alpha + \beta x$ for constants $\alpha, \beta$. Verify that $h(W_{t \wedge \tau})$ is a martingale, where $\tau$ is the exit time from $(a, b)$.

??? success "Solution to Exercise 2"
    If $h$ is harmonic for Brownian motion on $(a,b)$, then $\frac{1}{2}h''(x) = 0$, which gives $h''(x) = 0$. Integrating twice:

    $$
    h'(x) = \beta, \quad h(x) = \alpha + \beta x
    $$

    for constants $\alpha, \beta$. So $h$ is an affine function.

    **Martingale verification**: By Ito's lemma applied to $h(W_t) = \alpha + \beta W_t$:

    $$
    dh(W_t) = h'(W_t)\,dW_t + \frac{1}{2}h''(W_t)\,dt = \beta\,dW_t + 0
    $$

    So $h(W_t) = \alpha + \beta W_t$ is a martingale (being a stochastic integral against Brownian motion). Stopping at $\tau \wedge t$ preserves the martingale property by the optional stopping theorem (since $h(W_{t\wedge\tau})$ is bounded on the compact interval $[a,b]$).

---

**Exercise 3.**
The expected exit time of Brownian motion from $(-a, a)$ starting at $x = 0$ satisfies $\frac{1}{2}u''(x) = -1$ with $u(-a) = u(a) = 0$. Solve this boundary value problem and compute $u(0)$.

??? success "Solution to Exercise 3"
    The expected exit time $u(x) = \mathbb{E}_x[\tau]$ satisfies the ODE:

    $$
    \frac{1}{2}u''(x) = -1 \quad \text{on } (-a, a), \quad u(-a) = u(a) = 0
    $$

    Integrating $u''(x) = -2$ twice:

    $$
    u'(x) = -2x + C_1, \quad u(x) = -x^2 + C_1 x + C_2
    $$

    Applying boundary conditions:

    - $u(a) = 0$: $-a^2 + C_1 a + C_2 = 0$
    - $u(-a) = 0$: $-a^2 - C_1 a + C_2 = 0$

    Subtracting: $2C_1 a = 0$, so $C_1 = 0$. Then $C_2 = a^2$.

    $$
    u(x) = a^2 - x^2
    $$

    At $x = 0$:

    $$
    u(0) = a^2
    $$

    The expected exit time of Brownian motion from $(-a,a)$ starting at the center is $a^2$.

---

**Exercise 4.**
The generator of Brownian motion is $\mathcal{L} = \frac{1}{2}\partial_{xx}$. For Brownian motion with drift $\mu$, the generator becomes $\mathcal{L} = \mu\partial_x + \frac{1}{2}\partial_{xx}$. Show that the function $u(t, x) = \mathbb{E}[f(x + \mu(T-t) + W_{T-t})]$ satisfies $\partial_t u + \mu\partial_x u + \frac{1}{2}\partial_{xx}u = 0$.

??? success "Solution to Exercise 4"
    Define $u(t,x) = \mathbb{E}[f(x + \mu(T-t) + W_{T-t})]$. Writing $s = T - t$ and using the convolution:

    $$
    u(t,x) = \int_{-\infty}^{\infty} f(y)\,G(s, y - x - \mu s)\,dy
    $$

    **Computing $\partial_t u$**: Since $s = T - t$, $\partial_t = -\partial_s$:

    $$
    \partial_t u = -\frac{\partial}{\partial s}\int f(y)\,G(s, y - x - \mu s)\,dy
    $$

    By the chain rule, $G$ depends on $s$ both explicitly and through the argument $y - x - \mu s$:

    $$
    \partial_t u = -\int f(y)\left[\frac{\partial G}{\partial s} - \mu\frac{\partial G}{\partial z}\right]dy
    $$

    where $z = y - x - \mu s$.

    **Computing spatial derivatives**:

    $$
    \partial_x u = -\int f(y)\frac{\partial G}{\partial z}\,dy, \quad \partial_{xx}u = \int f(y)\frac{\partial^2 G}{\partial z^2}\,dy
    $$

    Now $\partial_t u + \mu\partial_x u + \frac{1}{2}\partial_{xx}u$ becomes:

    $$
    -\int f\left[\frac{\partial G}{\partial s} - \mu\frac{\partial G}{\partial z}\right]dy - \mu\int f\frac{\partial G}{\partial z}\,dy + \frac{1}{2}\int f\frac{\partial^2 G}{\partial z^2}\,dy
    $$

    $$
    = -\int f\frac{\partial G}{\partial s}\,dy + \frac{1}{2}\int f\frac{\partial^2 G}{\partial z^2}\,dy = -\int f\left(\frac{\partial G}{\partial s} - \frac{1}{2}\frac{\partial^2 G}{\partial z^2}\right)dy = 0
    $$

    since $G$ satisfies the heat equation $\partial_s G = \frac{1}{2}\partial_{zz}G$.

---

**Exercise 5.**
Explain the correspondence: Brownian paths correspond to solutions of the heat equation, expected values correspond to convolution with the heat kernel. For $f(x) = x^2$, compute $\mathbb{E}[(W_t + x)^2]$ and verify it equals the heat equation solution with initial data $f$.

??? success "Solution to Exercise 5"
    For $f(x) = x^2$, the probabilistic representation gives:

    $$
    \mathbb{E}[(W_t + x)^2] = \mathbb{E}[W_t^2 + 2xW_t + x^2] = \mathbb{E}[W_t^2] + 2x\mathbb{E}[W_t] + x^2
    $$

    Since $W_t \sim N(0,t)$: $\mathbb{E}[W_t] = 0$ and $\mathbb{E}[W_t^2] = t$. Therefore:

    $$
    u(t,x) = t + x^2
    $$

    **Verification via the heat equation**: Check that $u(t,x) = t + x^2$ satisfies $\partial_t u = \frac{1}{2}\partial_{xx}u$:

    - $\partial_t u = 1$
    - $\partial_{xx} u = 2$
    - $\frac{1}{2}\partial_{xx}u = 1 = \partial_t u$ $\checkmark$

    Initial condition: $u(0,x) = x^2 = f(x)$ $\checkmark$

    This illustrates the correspondence: Brownian motion computes $\mathbb{E}[f(W_t + x)]$, and the result is the same as the convolution $\int f(y)G(t, y-x)\,dy$, both of which solve the heat equation with initial data $f$.

---

**Exercise 6.**
In the heat equation, an initial hot spot diffuses and spreads over time. In the Brownian motion picture, a particle starting at a point wanders randomly. Explain how the maximum principle ($u$ cannot have an interior maximum) follows from the martingale property of $u(t, W_t)$.

??? success "Solution to Exercise 6"
    If $u(t,x)$ solves the heat equation and $u(t, W_t)$ is a (local) martingale (by Ito's lemma, the $dt$ coefficient vanishes because $u$ solves the heat equation), then by the martingale property:

    $$
    u(t_0, x_0) = \mathbb{E}[u(t, W_t) \mid W_{t_0} = x_0] \quad \text{for } t > t_0
    $$

    An expected value of a random variable cannot exceed its maximum:

    $$
    u(t_0, x_0) = \mathbb{E}[u(t, W_t) \mid W_{t_0} = x_0] \leq \max_{y} u(t, y)
    $$

    More precisely, for the domain problem, $W_t$ can reach the boundary with positive probability. The value $u(t_0, x_0)$ is an average of boundary and terminal values weighted by the distribution of where Brownian motion exits the domain. Since an average cannot exceed the maximum of the values being averaged, $u$ cannot have an interior maximum that exceeds the boundary values.

    If $u$ had a strict interior maximum, Brownian paths starting there would immediately move to points with lower values (since $W_t$ is nondegenerate), making the expected value strictly less than the starting value -- contradicting the assumed maximum.

---

**Exercise 7.**
The exit time $\tau = \inf\{t : W_t \notin (a, b)\}$ connects Brownian motion to the Dirichlet boundary value problem. State the relationship $\mathbb{E}_x[f(W_\tau)] = u(x)$ where $u$ solves $\frac{1}{2}u'' = 0$ on $(a,b)$ with $u(a) = f(a)$ and $u(b) = f(b)$. Solve for $u(x)$ and verify with a specific example.

??? success "Solution to Exercise 7"
    **Statement**: Let $\tau = \inf\{t : W_t \notin (a,b)\}$ and let $u(x) = \mathbb{E}_x[f(W_\tau)]$. Then $u$ solves:

    $$
    \frac{1}{2}u''(x) = 0 \quad \text{on } (a,b), \quad u(a) = f(a), \quad u(b) = f(b)
    $$

    **Solution**: From $u''(x) = 0$, we get $u(x) = \alpha + \beta x$. Applying boundary conditions:

    - $u(a) = f(a)$: $\alpha + \beta a = f(a)$
    - $u(b) = f(b)$: $\alpha + \beta b = f(b)$

    Solving: $\beta = \frac{f(b) - f(a)}{b - a}$ and $\alpha = f(a) - a\beta$. Therefore:

    $$
    u(x) = f(a)\frac{b - x}{b - a} + f(b)\frac{x - a}{b - a}
    $$

    **Example**: Take $(a,b) = (0,1)$ and $f(x) = x^2$, so $f(0) = 0$ and $f(1) = 1$. Then:

    $$
    u(x) = 0 \cdot \frac{1 - x}{1} + 1 \cdot \frac{x - 0}{1} = x
    $$

    This means $\mathbb{E}_x[W_\tau^2] = x$ where $\tau$ is the exit time from $(0,1)$. We can verify: $u(x) = x$ is linear, so $u'' = 0$, and $u(0) = 0 = f(0)$, $u(1) = 1 = f(1)$.
