# Scaling and Invariance

The heat equation possesses a characteristic **scaling symmetry** that reflects the fundamental nature of diffusion. This symmetry connects analytical properties of the PDE to probabilistic properties of Brownian motion.

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

## The Scaling Relation: $x \sim \sqrt{t}$

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

Brownian motion satisfies the identical scaling property:

$$
\boxed{
(B_t)_{t \geq 0} \overset{d}{=} \left(\frac{1}{\lambda}B_{\lambda^2 t}\right)_{t \geq 0}
}
$$

**Proof**: Both sides are Gaussian processes with:
- Mean zero
- Covariance $\mathbb{E}[B_s B_t] = \min(s,t)$

The scaling of Brownian motion explains why the heat equation governs the evolution of Brownian distributions.

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
