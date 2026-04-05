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

---

## Exercises

**Exercise 1.**
Verify that $G(t, x) = (2\pi t)^{-1/2}\exp(-x^2/(2t))$ satisfies $\partial_t G = \frac{1}{2}\partial_{xx}G$ by computing both sides explicitly and showing they are equal.

??? success "Solution to Exercise 1"
    We need to verify that $G(t,x) = (2\pi t)^{-1/2}\exp(-x^2/(2t))$ satisfies $\partial_t G = \frac{1}{2}\partial_{xx}G$.

    **Computing $\partial_t G$**: Using the product rule on $G = (2\pi t)^{-1/2}\exp(-x^2/(2t))$:

    $$
    \partial_t G = G \cdot \left(-\frac{1}{2t} + \frac{x^2}{2t^2}\right)
    $$

    **Computing $\partial_x G$**: Differentiating with respect to $x$:

    $$
    \partial_x G = G \cdot \left(-\frac{x}{t}\right)
    $$

    **Computing $\partial_{xx} G$**: Differentiating again:

    $$
    \partial_{xx} G = \partial_x\left[G \cdot \left(-\frac{x}{t}\right)\right] = \left(-\frac{x}{t}\right)\partial_x G + G\cdot\left(-\frac{1}{t}\right)
    $$

    Substituting $\partial_x G = -\frac{x}{t}G$:

    $$
    \partial_{xx} G = \frac{x^2}{t^2}G - \frac{1}{t}G = G\left(\frac{x^2}{t^2} - \frac{1}{t}\right)
    $$

    **Verification**: Now compute $\frac{1}{2}\partial_{xx}G$:

    $$
    \frac{1}{2}\partial_{xx}G = \frac{1}{2}G\left(\frac{x^2}{t^2} - \frac{1}{t}\right) = G\left(\frac{x^2}{2t^2} - \frac{1}{2t}\right)
    $$

    This equals $\partial_t G = G\left(-\frac{1}{2t} + \frac{x^2}{2t^2}\right)$, confirming that $\partial_t G = \frac{1}{2}\partial_{xx}G$.

---

**Exercise 2.**
Show that $\int_{-\infty}^{\infty}G(t, x)\,dx = 1$ for all $t > 0$. Interpret this result probabilistically: it says the total probability is conserved, consistent with $G$ being the transition density of Brownian motion.

??? success "Solution to Exercise 2"
    We compute the integral using the substitution $z = x/\sqrt{t}$, so $dx = \sqrt{t}\,dz$:

    $$
    \int_{-\infty}^{\infty} G(t,x)\,dx = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi t}} \exp\left(-\frac{x^2}{2t}\right)dx = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{z^2}{2}\right)dz
    $$

    The last integral is the integral of the standard normal density over $\mathbb{R}$, which equals $1$.

    **Probabilistic interpretation**: Since $G(t,x)$ is the probability density function of $B_t \sim N(0,t)$, the integral $\int G(t,x)\,dx = 1$ simply states that the total probability is $1$. The particle must be somewhere at every time $t > 0$, so the density integrates to unity.

---

**Exercise 3.**
The convolution formula $u(t, x) = \int_{-\infty}^{\infty}G(t, x-y)\,f(y)\,dy$ gives the solution to the heat equation with initial condition $u(0, x) = f(x)$. Compute $u(t, x)$ for $f(y) = 1$ (constant initial data) and verify the result makes physical sense.

??? success "Solution to Exercise 3"
    For constant initial data $f(y) = 1$:

    $$
    u(t,x) = \int_{-\infty}^{\infty} G(t, x-y) \cdot 1\,dy = \int_{-\infty}^{\infty} G(t, x-y)\,dy
    $$

    Substituting $w = x - y$ (so $dy = -dw$, and limits are preserved):

    $$
    u(t,x) = \int_{-\infty}^{\infty} G(t,w)\,dw = 1
    $$

    by the normalization property of the heat kernel (Exercise 2).

    **Physical interpretation**: If the temperature is uniformly $1$ everywhere at time $0$, it remains uniformly $1$ for all time. There are no temperature gradients to drive diffusion, so nothing changes. This is consistent with the fact that $u = 1$ trivially satisfies $\partial_t u = 0 = \frac{1}{2}\partial_{xx}u$.

---

**Exercise 4.**
Show that the heat kernel satisfies the semigroup property: $\int_{-\infty}^{\infty}G(t-s, x-z)\,G(s, z-y)\,dz = G(t, x-y)$ for $0 < s < t$. (Hint: this is the convolution of two Gaussians.) What is the probabilistic interpretation?

??? success "Solution to Exercise 4"
    We need to show that the convolution of two Gaussians yields another Gaussian:

    $$
    I = \int_{-\infty}^{\infty} G(t-s, x-z)\,G(s, z-y)\,dz
    $$

    Writing out the kernels:

    $$
    I = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi(t-s)}} \exp\!\left(-\frac{(x-z)^2}{2(t-s)}\right) \frac{1}{\sqrt{2\pi s}} \exp\!\left(-\frac{(z-y)^2}{2s}\right) dz
    $$

    The exponent is:

    $$
    -\frac{(x-z)^2}{2(t-s)} - \frac{(z-y)^2}{2s}
    $$

    Completing the square in $z$: let $\alpha = \frac{1}{t-s} + \frac{1}{s} = \frac{t}{s(t-s)}$. The combined exponent is quadratic in $z$ with leading coefficient $-\frac{\alpha}{2}$. After completing the square:

    $$
    -\frac{\alpha}{2}\left(z - \frac{sx + (t-s)y}{t}\right)^2 - \frac{(x-y)^2}{2t}
    $$

    The Gaussian integral in $z$ evaluates to $\sqrt{2\pi/\alpha} = \sqrt{2\pi s(t-s)/t}$. Combining the prefactors:

    $$
    I = \frac{1}{\sqrt{2\pi(t-s)}\cdot\sqrt{2\pi s}} \cdot \sqrt{\frac{2\pi s(t-s)}{t}} \cdot \exp\!\left(-\frac{(x-y)^2}{2t}\right) = \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{(x-y)^2}{2t}\right)
    $$

    This is exactly $G(t, x-y)$.

    **Probabilistic interpretation**: The semigroup property reflects the fact that Brownian increments are independent: $B_t - B_0 = (B_t - B_s) + (B_s - B_0)$ where $B_t - B_s \sim N(0, t-s)$ and $B_s \sim N(0,s)$ are independent. The sum of two independent normals is normal with variance $(t-s)+s = t$, giving $B_t \sim N(0,t)$.

---

**Exercise 5.**
Compute $\lim_{t \to 0^+}G(t, x)$ for $x \neq 0$ and $x = 0$ separately. Explain why $G(t, x) \to \delta(x)$ in the distributional sense as $t \to 0^+$, even though $G(t, 0) \to \infty$.

??? success "Solution to Exercise 5"
    **For $x \neq 0$**: The exponential dominates:

    $$
    G(t,x) = \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{x^2}{2t}\right)
    $$

    As $t \to 0^+$, the exponent $-x^2/(2t) \to -\infty$, so $\exp(-x^2/(2t)) \to 0$ faster than any power of $t$. Therefore $\lim_{t\to 0^+} G(t,x) = 0$ for all $x \neq 0$.

    **For $x = 0$**:

    $$
    G(t,0) = \frac{1}{\sqrt{2\pi t}} \to +\infty \quad \text{as } t \to 0^+
    $$

    **Distributional convergence to $\delta(x)$**: For any smooth test function $\varphi$ with compact support:

    $$
    \int_{-\infty}^{\infty} G(t,x)\,\varphi(x)\,dx \to \varphi(0) \quad \text{as } t \to 0^+
    $$

    This holds because $G(t,\cdot)$ is a probability density with total mass $1$ that concentrates all its mass near the origin as $t \to 0^+$. Specifically, for any $\epsilon > 0$:

    $$
    \int_{|x|>\epsilon} G(t,x)\,dx = \mathbb{P}(|B_t| > \epsilon) = 2\Phi\!\left(-\frac{\epsilon}{\sqrt{t}}\right) \to 0
    $$

    So the mass outside any neighborhood of $0$ vanishes, while the total mass remains $1$. This is precisely the defining property of convergence to the Dirac delta in the distributional sense.

---

**Exercise 6.**
The heat kernel exhibits instantaneous smoothing: for any initial condition $f \in L^1(\mathbb{R})$, the solution $u(t, x) = \int G(t, x-y)f(y)\,dy$ is $C^{\infty}$ for $t > 0$. Explain intuitively why convolution with a Gaussian produces a smooth function, regardless of how rough $f$ is.

??? success "Solution to Exercise 6"
    Convolution with a Gaussian produces a smooth function because the Gaussian kernel $G(t,\cdot)$ is itself infinitely differentiable ($C^\infty$), and derivatives can be passed under the integral:

    $$
    \frac{\partial^n}{\partial x^n} u(t,x) = \int_{-\infty}^{\infty} \frac{\partial^n G}{\partial x^n}(t, x-y)\,f(y)\,dy
    $$

    This is valid because all derivatives of $G$ with respect to $x$ decay rapidly (faster than any polynomial) as $|x| \to \infty$, so the integral converges absolutely for any $f \in L^1$.

    **Intuitive explanation**: Convolution is a weighted average. The Gaussian kernel assigns smooth, bell-shaped weights centered at $x$. Even if $f$ has jumps, kinks, or other irregularities, the weighted average "averages them out." The output inherits the smoothness of the kernel, not of $f$.

    In physical terms, diffusion instantaneously mixes the initial data over all nearby points. After any positive time, each point's value depends on the initial data over an entire neighborhood, smoothing out any local irregularities.

---

**Exercise 7.**
For the diffusion equation with coefficient $D$, the fundamental solution is $G_D(t, x) = (4\pi D t)^{-1/2}\exp(-x^2/(4Dt))$. Identify the relationship between $D$ and the notation used in this text (where $D = \sigma^2/2$). For a stock with $\sigma = 0.30$, compute $D$ and the standard deviation $\sqrt{2Dt}$ of the kernel after one year.

??? success "Solution to Exercise 7"
    The general diffusion equation $\partial_t u = D\,\partial_{xx}u$ has fundamental solution $G_D(t,x) = (4\pi D t)^{-1/2}\exp(-x^2/(4Dt))$.

    In our text, the heat equation is written as $\partial_t u = \frac{1}{2}\partial_{xx}u$, corresponding to diffusion coefficient $D = 1/2$. More generally, for a process with volatility $\sigma$, the diffusion coefficient is:

    $$
    D = \frac{\sigma^2}{2}
    $$

    **For $\sigma = 0.30$**:

    $$
    D = \frac{(0.30)^2}{2} = \frac{0.09}{2} = 0.045
    $$

    The standard deviation of the kernel at time $t$ is:

    $$
    \text{std} = \sqrt{2Dt} = \sqrt{\sigma^2 t} = \sigma\sqrt{t}
    $$

    After one year ($t = 1$):

    $$
    \text{std} = 0.30 \times \sqrt{1} = 0.30
    $$

    This means that after one year, the kernel has spread to a standard deviation of $30\%$, which in the context of a stock's log-return corresponds to a $30\%$ annualized volatility -- exactly matching the input $\sigma$.
