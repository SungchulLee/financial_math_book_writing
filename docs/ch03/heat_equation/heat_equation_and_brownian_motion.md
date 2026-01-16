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
