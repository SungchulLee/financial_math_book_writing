# Scaling and Invariance

Photograph diffusing ink at time $t$, then again at time $4t$. The second snapshot is the first stretched horizontally by $2$ and compressed vertically by $1/2$ -- same shape, rescaled. This self-similarity, with space scaling like $\sqrt{\text{time}}$, is the defining symmetry of the heat equation and the geometric fingerprint of diffusion. From it we recover the heat kernel, the $\sqrt{t}$ spread of Brownian motion, and the $\sigma\sqrt{T-t}$ inside every Black-Scholes formula.

---

## Parabolic Scaling

**Theorem**: If $u(t,x)$ solves the heat equation $u_t = \frac{1}{2}u_{xx}$, then for any $\lambda > 0$:

$$
\boxed{
u_\lambda(t,x) := u(\lambda^2 t, \lambda x)
}
$$

also solves the heat equation.

**Proof**: Let $v(t,x) = u(\lambda^2 t, \lambda x)$. Then:

$$
\frac{\partial v}{\partial t} = \lambda^2 \frac{\partial u}{\partial t}(\lambda^2 t, \lambda x)
$$

$$
\frac{\partial^2 v}{\partial x^2} = \lambda^2 \frac{\partial^2 u}{\partial x^2}(\lambda^2 t, \lambda x)
$$

Therefore:

$$
\frac{\partial v}{\partial t} - \frac{1}{2}\frac{\partial^2 v}{\partial x^2} = \lambda^2 \left(\frac{\partial u}{\partial t} - \frac{1}{2}\frac{\partial^2 u}{\partial x^2}\right) = 0 \quad \checkmark
$$

---

## The Scaling Relation: x ~ √t

Parabolic scaling reveals the fundamental relationship:

$$
\boxed{
\text{space} \sim \sqrt{\text{time}}
}
$$

This means:

- To double the spatial scale, quadruple the time
- Diffusion is **slower than linear transport**
- The "diffusion length" grows as $\sqrt{t}$

---

## Connection to Brownian Motion

Recall (see [§ Scaling and Time Change](../../ch02/brownian_motion/scaling_and_time_change.md)): Brownian motion satisfies $(B_t) \overset{d}{=} (\lambda^{-1} B_{\lambda^2 t})$, the probabilistic mirror of parabolic scaling.

---

## Self-Similar Solutions

The scaling invariance leads to **self-similar solutions** — solutions that maintain their shape under rescaling.

**Ansatz**: Look for solutions of the form:

$$
u(t,x) = t^{-\alpha} F\left(\frac{x}{\sqrt{t}}\right) = t^{-\alpha} F(\eta), \quad \eta = \frac{x}{\sqrt{t}}
$$

**Substituting into the heat equation**:

$$
u_t = -\alpha t^{-\alpha-1} F - \frac{1}{2}t^{-\alpha-1}\eta F'
$$

$$
u_{xx} = t^{-\alpha-1} F''
$$

The heat equation becomes:

$$
-\alpha F - \frac{1}{2}\eta F' = \frac{1}{2}F''
$$

For $\alpha = \frac{1}{2}$:

$$
F'' + \eta F' + F = 0
$$

**Solution**: $F(\eta) = C e^{-\eta^2/2}$

This recovers the **heat kernel**:

$$
u(t,x) = \frac{C}{\sqrt{t}} e^{-x^2/2t}
$$

---

## Diffusion vs Transport

The scaling relation distinguishes diffusion from transport:

| Process | Equation | Scaling | Characteristic |
|---------|----------|---------|----------------|
| Transport | $u_t + cu_x = 0$ | $x \sim t$ | Waves, signals |
| Diffusion | $u_t = \frac{1}{2}u_{xx}$ | $x \sim \sqrt{t}$ | Heat, particles |

**Physical implication**:

- Transport: Information travels at constant speed $c$
- Diffusion: Spread grows as $\sqrt{t}$, slower over long times

---

## Dimensional Analysis

**Diffusion coefficient**: If the equation is $u_t = D u_{xx}$, then $[D] = \frac{\text{length}^2}{\text{time}}$.

The characteristic length scale is:

$$
\ell(t) = \sqrt{Dt}
$$

**Applications**:

- Heat conduction: How far does heat spread in time $t$?
- Finance: How much can a stock price move in time $t$?
- Biology: How far do molecules diffuse?

---

## Invariance Under Other Transformations

The heat equation is also invariant under:

### 1. Translation

If $u(t,x)$ is a solution, so is $u(t, x-a)$ for any constant $a$.

### 2. Time Translation

If $u(t,x)$ is a solution, so is $u(t-t_0, x)$ for $t > t_0$.

### 3. Reflection

If $u(t,x)$ is a solution, so is $u(t,-x)$.

### 4. Galilean Transformation

If $u(t,x)$ solves $u_t = \frac{1}{2}u_{xx}$, then:

$$
v(t,x) = e^{cx - c^2t/2} u(t, x - ct)
$$

solves the same equation. This corresponds to Brownian motion with drift.

---

## Applications of Scaling

### 1. Finding Solutions

Scaling reduces the PDE to an ODE, as shown for self-similar solutions.

### 2. A Priori Estimates

Scaling arguments give bounds on solutions without solving explicitly:

$$
\|u(t,\cdot)\|_\infty \leq \frac{C}{\sqrt{t}}\|f\|_{L^1}
$$

### 3. Asymptotic Behavior

For large $t$, solutions approach the self-similar profile:

$$
u(t,x) \approx \frac{M}{\sqrt{2\pi t}}e^{-x^2/2t}
$$

where $M = \int f(x)\,dx$ is the total mass.

---

## The Similarity Variable

The variable $\eta = x/\sqrt{t}$ is called the **similarity variable**.

In terms of $\eta$:

- The heat kernel is $G(t,x) = \frac{1}{\sqrt{2\pi t}}e^{-\eta^2/2}$
- Self-similar solutions depend only on $\eta$
- Long-time asymptotics are controlled by behavior near $\eta = 0$

---

## Summary

$$
\boxed{
u(t,x) \text{ solves heat eq} \implies u(\lambda^2 t, \lambda x) \text{ solves heat eq}
}
$$

| Property | Expression |
|----------|------------|
| Parabolic scaling | $x \mapsto \lambda x$, $t \mapsto \lambda^2 t$ |
| Brownian scaling | $B_{\lambda^2 t} \overset{d}{=} \lambda B_t$ |
| Diffusion length | $\ell \sim \sqrt{t}$ |
| Similarity variable | $\eta = x/\sqrt{t}$ |

**Scaling invariance is the fingerprint of diffusion, distinguishing it from wave propagation and revealing the deep connection between the heat equation and Brownian motion.**

---

## Exercises

**Exercise 1.**
Verify the parabolic scaling: if $u(x, t)$ solves $\partial_t u = \frac{1}{2}\partial_{xx}u$, show that $v(x, t) = u(\lambda x, \lambda^2 t)$ also solves the same equation for any $\lambda > 0$.

??? success "Solution to Exercise 1"
    Let $u(x,t)$ solve $\partial_t u = \frac{1}{2}\partial_{xx}u$ and define $v(x,t) = u(\lambda x, \lambda^2 t)$.

    Set $X = \lambda x$ and $T = \lambda^2 t$, so $v(x,t) = u(X, T)$.

    **Time derivative**:

    $$
    \frac{\partial v}{\partial t} = \frac{\partial u}{\partial T}\cdot\frac{\partial T}{\partial t} = \lambda^2\frac{\partial u}{\partial T}(X, T)
    $$

    **Spatial derivatives**:

    $$
    \frac{\partial v}{\partial x} = \frac{\partial u}{\partial X}\cdot\frac{\partial X}{\partial x} = \lambda\frac{\partial u}{\partial X}(X, T)
    $$

    $$
    \frac{\partial^2 v}{\partial x^2} = \lambda^2\frac{\partial^2 u}{\partial X^2}(X, T)
    $$

    **Verification**:

    $$
    \frac{\partial v}{\partial t} - \frac{1}{2}\frac{\partial^2 v}{\partial x^2} = \lambda^2\frac{\partial u}{\partial T} - \frac{\lambda^2}{2}\frac{\partial^2 u}{\partial X^2} = \lambda^2\left(\frac{\partial u}{\partial T} - \frac{1}{2}\frac{\partial^2 u}{\partial X^2}\right) = 0
    $$

    since $u$ solves the heat equation. Therefore $v$ also solves $\partial_t v = \frac{1}{2}\partial_{xx}v$.

---

**Exercise 2.**
The similarity variable $\eta = x/\sqrt{t}$ reduces the heat equation to an ODE. Seek solutions of the form $u(x, t) = f(\eta)$ with $\eta = x/\sqrt{t}$. Show that $f$ satisfies $f'' + \eta f' = 0$ and identify the solution in terms of the error function.

??? success "Solution to Exercise 2"
    Seeking solutions $u(x,t) = f(\eta)$ with $\eta = x/\sqrt{t}$:

    $$
    \partial_t u = f'(\eta)\cdot\frac{\partial \eta}{\partial t} = f'(\eta)\cdot\left(-\frac{x}{2t^{3/2}}\right) = -\frac{\eta}{2t}f'(\eta)
    $$

    $$
    \partial_{xx}u = \frac{1}{t}f''(\eta)
    $$

    Substituting into $\partial_t u = \frac{1}{2}\partial_{xx}u$:

    $$
    -\frac{\eta}{2t}f'(\eta) = \frac{1}{2t}f''(\eta)
    $$

    Multiplying by $2t$:

    $$
    f''(\eta) + \eta f'(\eta) = 0
    $$

    This is a first-order ODE for $g = f'$: $g' + \eta g = 0$, which gives $g(\eta) = Ce^{-\eta^2/2}$.

    Integrating:

    $$
    f(\eta) = C\int_0^{\eta} e^{-s^2/2}\,ds + D = C\sqrt{\frac{\pi}{2}}\,\text{erf}\!\left(\frac{\eta}{\sqrt{2}}\right) + D
    $$

    where $\text{erf}(z) = \frac{2}{\sqrt{\pi}}\int_0^z e^{-s^2}\,ds$ is the error function. In terms of the original variables:

    $$
    u(x,t) = A\,\text{erf}\!\left(\frac{x}{\sqrt{2t}\cdot\sqrt{2}}\right) + D = A\,\text{erf}\!\left(\frac{x}{2\sqrt{t/2}}\right) + D
    $$

    This solution describes the diffusion of a step function initial condition and is related to the cumulative distribution function of the normal distribution.

---

**Exercise 3.**
Brownian scaling states $B_{\lambda^2 t} \overset{d}{=} \lambda B_t$. Use this to show that the standard deviation of $B_t$ grows as $\sqrt{t}$, not linearly in $t$. Explain why this $\sqrt{t}$ scaling is characteristic of diffusion processes and distinguishes them from ballistic motion.

??? success "Solution to Exercise 3"
    From Brownian scaling, $B_{\lambda^2 t} \overset{d}{=} \lambda B_t$. Taking $\lambda^2 t = T$ (so $\lambda = \sqrt{T/t}$):

    $$
    B_T \overset{d}{=} \sqrt{\frac{T}{t}}\,B_t
    $$

    In particular, with $t = 1$: $B_T \overset{d}{=} \sqrt{T}\,B_1$. Since $B_1 \sim N(0,1)$:

    $$
    \text{Std}(B_T) = \sqrt{T}\,\text{Std}(B_1) = \sqrt{T}
    $$

    The standard deviation grows as $\sqrt{T}$, not linearly.

    **Why $\sqrt{t}$ characterizes diffusion**: In ballistic (deterministic) motion with velocity $v$, displacement grows linearly: $x = vt$. In diffusion, each step is random and independent. After $n$ independent steps of typical size $\delta$, the net displacement has standard deviation $\delta\sqrt{n}$ by the central limit theorem (the random walk). Since $n \propto t$, displacement grows as $\sqrt{t}$. This sub-linear growth is the hallmark of diffusion: doubling the time does not double the spread, it only increases it by a factor of $\sqrt{2}$.

---

**Exercise 4.**
The diffusion length $\ell \sim \sigma\sqrt{t}$ determines how far a Brownian particle wanders in time $t$. For a stock with $\sigma = 0.25$, compute the diffusion length after 1 day ($t = 1/252$), 1 month ($t = 1/12$), and 1 year ($t = 1$). How does this relate to option pricing?

??? success "Solution to Exercise 4"
    The diffusion length is $\ell = \sigma\sqrt{t}$ with $\sigma = 0.25$.

    **After 1 day** ($t = 1/252$):

    $$
    \ell = 0.25\sqrt{1/252} = 0.25 \times 0.06299 \approx 0.01575
    $$

    About $1.6\%$ of the current price.

    **After 1 month** ($t = 1/12$):

    $$
    \ell = 0.25\sqrt{1/12} = 0.25 \times 0.28868 \approx 0.07217
    $$

    About $7.2\%$ of the current price.

    **After 1 year** ($t = 1$):

    $$
    \ell = 0.25\sqrt{1} = 0.25
    $$

    About $25\%$ of the current price.

    **Relation to option pricing**: The diffusion length $\sigma\sqrt{t}$ directly determines the width of the distribution of log-returns. In the Black-Scholes model, the quantity $d_1$ and $d_2$ in the pricing formula involve $\sigma\sqrt{T-t}$, which measures how far the stock can wander by expiry. Options with longer maturity have larger diffusion lengths, making them more valuable (all else equal), and the time value of an option scales approximately as $\sqrt{T-t}$, not linearly in $T-t$.

---

**Exercise 5.**
Show that the fundamental solution $G(t, x) = (2\pi t)^{-1/2}\exp(-x^2/(2t))$ is a self-similar function: $G(t, x) = t^{-1/2}\Phi(x/\sqrt{t})$ for some function $\Phi$. Identify $\Phi$ explicitly.

??? success "Solution to Exercise 5"
    The fundamental solution is:

    $$
    G(t,x) = \frac{1}{\sqrt{2\pi t}}\exp\!\left(-\frac{x^2}{2t}\right)
    $$

    Factor out $t^{-1/2}$:

    $$
    G(t,x) = t^{-1/2} \cdot \frac{1}{\sqrt{2\pi}} \exp\!\left(-\frac{1}{2}\left(\frac{x}{\sqrt{t}}\right)^2\right) = t^{-1/2}\,\Phi\!\left(\frac{x}{\sqrt{t}}\right)
    $$

    where:

    $$
    \Phi(\eta) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{\eta^2}{2}\right)
    $$

    This is the standard normal density. The self-similar structure $G(t,x) = t^{-1/2}\Phi(x/\sqrt{t})$ confirms that the heat kernel at any time $t$ is just a rescaled version of the standard normal density, stretched horizontally by $\sqrt{t}$ and compressed vertically by $1/\sqrt{t}$ to preserve unit total mass.

---

**Exercise 6.**
The wave equation $\partial_{tt}u = c^2\partial_{xx}u$ has scaling $x \mapsto \lambda x$, $t \mapsto \lambda t$ (linear scaling). Compare this with the parabolic scaling $x \mapsto \lambda x$, $t \mapsto \lambda^2 t$ of the heat equation. Explain the physical difference: waves propagate at constant speed $c$, while diffusion spreads as $\sqrt{t}$.

??? success "Solution to Exercise 6"
    **Wave equation scaling**: If $u(x,t)$ solves $u_{tt} = c^2 u_{xx}$, then $v(x,t) = u(\lambda x, \lambda t)$ also solves it, because:

    $$
    v_{tt} = \lambda^2 u_{tt}, \quad v_{xx} = \lambda^2 u_{xx}
    $$

    The ratio $v_{tt}/(c^2 v_{xx}) = u_{tt}/(c^2 u_{xx}) = 1$. The scaling is $x \mapsto \lambda x$, $t \mapsto \lambda t$ (both scale the same way).

    **Heat equation scaling**: As shown in Exercise 1, the scaling is $x \mapsto \lambda x$, $t \mapsto \lambda^2 t$.

    **Physical difference**:

    - Waves: The characteristic speed is $x/t = c$ (constant). A disturbance at the origin reaches position $x$ at time $t = x/c$. Doubling the distance doubles the travel time. Waves propagate at constant speed.
    - Diffusion: The characteristic length is $x/\sqrt{t} = \text{const}$ (the similarity variable). A disturbance at the origin reaches position $x$ at time $t \propto x^2$. Doubling the distance quadruples the time. Diffusion slows down at large distances because particles must perform many random steps to drift far from the origin.

    This fundamental difference explains why sound travels across a room in milliseconds (wave propagation), while the scent of perfume takes minutes to diffuse across the same distance (diffusion).

---

**Exercise 7.**
In option pricing, the Black-Scholes formula depends on $\sigma\sqrt{T-t}$ rather than $\sigma(T-t)$ or $\sigma(T-t)^2$. Explain how this $\sqrt{T-t}$ dependence is a direct consequence of parabolic scaling and why it determines the shape of the implied volatility surface as a function of maturity.

??? success "Solution to Exercise 7"
    In the Black-Scholes model, after transforming to log-price coordinates $x = \log(S/K)$ and time-to-maturity $\tau = T - t$, the option pricing PDE reduces to the heat equation with diffusion coefficient $\sigma^2/2$. The solution involves the heat kernel evaluated at the similarity variable:

    $$
    \frac{x}{\sigma\sqrt{\tau}} = \frac{\log(S/K)}{\sigma\sqrt{T-t}}
    $$

    This is precisely the quantity $d_2$ (up to the drift correction). The appearance of $\sigma\sqrt{T-t}$ rather than $\sigma(T-t)$ is a direct consequence of parabolic scaling: the natural dimensionless combination of space and time for the heat equation is $x/\sqrt{t}$, not $x/t$.

    **Impact on the implied volatility surface**: For at-the-money options ($S \approx K$, so $x \approx 0$), the option price scales approximately as $\sigma\sqrt{T-t}$ (from the linear approximation of the normal CDF near zero). This means:

    - The at-the-money option price is approximately proportional to $\sqrt{T-t}$
    - The implied volatility for ATM options is roughly constant across maturities in the Black-Scholes model
    - For out-of-the-money options, the moneyness $\log(S/K)$ enters through the ratio $\log(S/K)/(\sigma\sqrt{T-t})$, so a fixed strike becomes "less out-of-the-money" at longer maturities (since $\sigma\sqrt{T-t}$ grows)

    In real markets, deviations from the Black-Scholes model create the volatility smile/skew, but the $\sqrt{T-t}$ scaling still governs the overall maturity structure. The implied volatility surface is often parameterized in terms of the "total variance" $\sigma^2(T-t)$, directly reflecting this parabolic scaling.
