# The Fundamental Solution (Heat Kernel)

The heat equation admits an explicit **fundamental solution**, also called the **heat kernel** or **Gaussian kernel**. This function is central to both the analytical theory and its probabilistic interpretation.

---

## Definition

The fundamental solution of the heat equation is:

$$
\boxed{
G(t,x) = \frac{1}{\sqrt{2\pi t}} \exp\left(-\frac{x^2}{2t}\right), \quad t > 0
}
$$

This function satisfies:

1. **The heat equation**: $\partial_t G = \frac{1}{2}\partial_{xx} G$ for $t > 0$

2. **Initial condition**: $\lim_{t \downarrow 0} G(t,\cdot) = \delta_0$ (Dirac delta at origin)

---

## Verification

**Step 1**: Compute derivatives.

$$
\partial_t G = G \cdot \left(-\frac{1}{2t} + \frac{x^2}{2t^2}\right)
$$

$$
\partial_x G = G \cdot \left(-\frac{x}{t}\right)
$$

$$
\partial_{xx} G = G \cdot \left(-\frac{1}{t} + \frac{x^2}{t^2}\right)
$$

**Step 2**: Verify the equation.

$$
\partial_t G - \frac{1}{2}\partial_{xx} G = G \cdot \left(-\frac{1}{2t} + \frac{x^2}{2t^2} + \frac{1}{2t} - \frac{x^2}{2t^2}\right) = 0 \quad \checkmark
$$

---

## Derivation via Fourier Transform

The Fourier transform provides a systematic method to derive the fundamental solution.

**Step 1**: Take Fourier transform in $x$.

Let $\hat{u}(t,\xi) = \int_{\mathbb{R}} u(t,x) e^{-i\xi x}\,dx$.

The heat equation $u_t = \frac{1}{2}u_{xx}$ transforms to:

$$
\frac{\partial \hat{u}}{\partial t} = -\frac{\xi^2}{2}\hat{u}
$$

**Step 2**: Solve the ODE.

$$
\hat{u}(t,\xi) = \hat{f}(\xi) \cdot e^{-\xi^2 t/2}
$$

where $\hat{f}$ is the Fourier transform of the initial data.

**Step 3**: For $f = \delta_0$, we have $\hat{f}(\xi) = 1$.

$$
\hat{G}(t,\xi) = e^{-\xi^2 t/2}
$$

**Step 4**: Inverse Fourier transform.

$$
G(t,x) = \frac{1}{2\pi}\int_{\mathbb{R}} e^{i\xi x} e^{-\xi^2 t/2}\,d\xi
$$

This is a Gaussian integral. Completing the square:

$$
G(t,x) = \frac{1}{2\pi} \cdot \sqrt{\frac{2\pi}{t}} \cdot e^{-x^2/2t} = \frac{1}{\sqrt{2\pi t}} e^{-x^2/2t}
$$

---

## Solution by Convolution

For general initial data $u(0,x) = f(x)$, the solution is given by **convolution**:

$$
\boxed{
u(t,x) = (G(t,\cdot) * f)(x) = \int_{\mathbb{R}} G(t, x-y) f(y)\,dy
}
$$

Explicitly:

$$
u(t,x) = \frac{1}{\sqrt{2\pi t}} \int_{\mathbb{R}} \exp\left(-\frac{(x-y)^2}{2t}\right) f(y)\,dy
$$

**Interpretation**: The solution at $(t,x)$ is a weighted average of initial values, with Gaussian weights centered at $x$.

---

## Properties of the Heat Kernel

### 1. Normalization

$$
\int_{\mathbb{R}} G(t,x)\,dx = 1 \quad \text{for all } t > 0
$$

The heat kernel is a probability density.

### 2. Semigroup Property

$$
G(t+s, x) = \int_{\mathbb{R}} G(t, x-y) G(s, y)\,dy = (G(t,\cdot) * G(s,\cdot))(x)
$$

**Probabilistic meaning**: $B_{t+s} = B_t + (B_{t+s} - B_t)$, where increments are independent.

### 3. Symmetry

$$
G(t,x) = G(t,-x)
$$

### 4. Scaling

$$
G(t,x) = \frac{1}{\sqrt{t}} G\left(1, \frac{x}{\sqrt{t}}\right)
$$

### 5. Moments

$$
\int_{\mathbb{R}} x^{2n} G(t,x)\,dx = (2n-1)!! \cdot t^n = \frac{(2n)!}{2^n n!} t^n
$$

In particular: mean $= 0$, variance $= t$.

---

## Probabilistic Interpretation

The heat kernel is the **transition density of Brownian motion**:

$$
G(t,x) = \frac{d}{dx}\mathbb{P}(B_t \leq x) = p_{B_t}(x)
$$

More generally, for Brownian motion starting at $y$:

$$
\mathbb{P}(B_t \in dx \mid B_0 = y) = G(t, x-y)\,dx
$$

The convolution formula becomes:

$$
u(t,x) = \mathbb{E}[f(x + B_t)] = \mathbb{E}[f(B_t) \mid B_0 = x]
$$

---

## Regularity

**Theorem**: If $f$ is bounded and measurable, then for all $t > 0$:

1. $u(t,\cdot) \in C^\infty(\mathbb{R})$ — infinitely differentiable
2. $u(t,x) > 0$ if $f \geq 0$ and $f \not\equiv 0$
3. $\|u(t,\cdot)\|_\infty \leq \|f\|_\infty$

**Proof sketch**: Differentiation under the integral sign is justified because $G$ and all its derivatives decay rapidly.

---

## The Heat Kernel in Higher Dimensions

In $\mathbb{R}^d$:

$$
G(t,x) = \frac{1}{(2\pi t)^{d/2}} \exp\left(-\frac{|x|^2}{2t}\right)
$$

where $|x|^2 = x_1^2 + \cdots + x_d^2$.

This is the density of $d$-dimensional Brownian motion.

---

## Connection to Other Kernels

| Kernel | Equation | Formula |
|--------|----------|---------|
| Heat kernel | $u_t = \frac{1}{2}\Delta u$ | $\frac{1}{(2\pi t)^{d/2}}e^{-|x|^2/2t}$ |
| Poisson kernel | $\Delta u = 0$ (half-space) | $\frac{y}{\pi(x^2+y^2)}$ |
| Wave kernel | $u_{tt} = \Delta u$ | $\frac{1}{2}[\delta(x-t) + \delta(x+t)]$ (1D) |

---

## Numerical Aspects

For numerical computation, the heat kernel provides:

1. **Explicit solution**: No discretization needed for simple domains
2. **Green's function method**: Extend to bounded domains via images
3. **Monte Carlo**: Sample Brownian paths instead of solving PDE

---

## Summary

$$
\boxed{
G(t,x) = \frac{1}{\sqrt{2\pi t}}e^{-x^2/2t} = \text{density of } B_t \sim N(0,t)
}
$$

The fundamental solution:
- Solves the heat equation with delta initial data
- Gives general solutions via convolution
- Equals the transition density of Brownian motion
- Exhibits instantaneous smoothing
- Satisfies the semigroup property

**The heat kernel is the bridge between the heat equation and Brownian motion.**
