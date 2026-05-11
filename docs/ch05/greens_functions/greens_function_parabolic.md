# Green's Function for Parabolic PDEs

A **Green's function** is the response of a linear PDE to a unit impulse -- a delta source at a single point in space and time. For parabolic equations, the Green's function is the complete solution operator: once you know how the system responds to a point source, arbitrary solutions follow by superposition. This page treats the Green's function through the **operator / PDE lens**. The probabilistic counterpart -- the transition density of a diffusion -- is developed in [Transition Density as Green's Function](transition_density_as_greens_function.md).

---

## Intuition

Inject a unit of heat at point $y$ at time $s$. The Green's function $G(t, x; s, y)$ describes how this heat spreads to point $x$ at time $t > s$: it starts as a delta at $y$, diffuses outward, and (on unbounded domains) dissipates as $t \to \infty$. Arbitrary initial data are reconstructed by superposing point sources -- the entire content of the **superposition principle**.

---

## Definition

Consider the parabolic operator $\mathcal{P}u = \partial_t u - \mathcal{L}u$, where $\mathcal{L}$ is the second-order elliptic operator

$$
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \tfrac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
$$

The **Green's function** $G(t, x; s, y)$ is the fundamental solution:

$$
\boxed{\;\partial_t G = \mathcal{L}_x G \quad (t > s), \qquad \lim_{t \downarrow s} G(t, x; s, y) = \delta(x - y)\;}
$$

Here $\mathcal{L}_x$ acts on the observation variable $x$. $G(t, x; s, y)$ is the PDE response at $(t, x)$ to a unit impulse at $(s, y)$.

---

## Superposition Principle

This page **owns** the integral representation: once $G$ is known, every linear problem reduces to an integral against $G$.

**Initial value problem.** For $\partial_t u = \mathcal{L}_x u$ with $u(0, x) = f(x)$:

$$
\boxed{\;u(t, x) = \int G(t, x; 0, y)\,f(y)\,dy\;}
$$

**Source problem (Duhamel).** For $\partial_t u - \mathcal{L}_x u = h(t, x)$ with $u(0, x) = 0$:

$$
u(t, x) = \int_0^t\!\int G(t, x; s, y)\,h(s, y)\,dy\,ds
$$

**Combined.** Linearity gives

$$
u(t, x) = \int G(t, x; 0, y)\,f(y)\,dy + \int_0^t\!\int G(t, x; s, y)\,h(s, y)\,dy\,ds
$$

The response to distributed data is the integral of responses to point sources.

---

## Properties

1. **Positivity.** $G(t, x; s, y) > 0$ for $t > s$ -- heat flows everywhere from a positive source.
2. **Normalization.** $\int G(t, x; s, y)\,dx = 1$ -- total heat (or probability) is conserved.
3. **Semigroup (Chapman-Kolmogorov).** For $s < r < t$,

    $$
    G(t, x; s, y) = \int G(t, x; r, z)\,G(r, z; s, y)\,dz
    $$

    Evolving from $s$ to $t$ is the same as evolving from $s$ to $r$ and then from $r$ to $t$. The full derivation and its probabilistic meaning live in [Transition Density as Green's Function](transition_density_as_greens_function.md).

4. **Symmetry.** When $\mathcal{L}$ is self-adjoint (e.g. pure diffusion), $G(t, x; s, y) = G(t, y; s, x)$. With drift this fails, but $G$ is related to the Green's function of the adjoint operator -- see the forward/backward discussion in [Transition Density as Green's Function](transition_density_as_greens_function.md).
5. **Smoothing.** $f \mapsto \int G(t, x; s, y)\,f(y)\,dy$ sends $L^\infty$ into $C^\infty$ for any $t > s$: parabolic equations regularize instantly.

!!! note "Forward and backward PDEs"
    $G$ solves one PDE in $(t, x)$ and an adjoint PDE in $(s, y)$. The full forward/backward table, with financial interpretation, is presented in [Transition Density as Green's Function](transition_density_as_greens_function.md).

---

## Construction for Variable Coefficients

**Parametrix method (Levi).** For general $\mathcal{L} = \mu(x)\partial_x + \tfrac{1}{2}\sigma^2(x)\partial_{xx}$, freeze coefficients at the source $y$ to get an explicit Gaussian approximation $G_0$:

$$
G_0(t, x; s, y) = \frac{1}{\sigma(y)\sqrt{2\pi(t-s)}}\exp\!\left(-\frac{(x - y - \mu(y)(t-s))^2}{2\sigma^2(y)(t-s)}\right)
$$

and iterate $G = G_0 + G_1 + G_2 + \cdots$, where each $G_n$ corrects the frozen-coefficient error. Under Hölder continuity, the series converges to a smooth $G$, with short-time asymptotics

$$
G(t, x; s, y) = G_0(t, x; s, y)\bigl(1 + O((t-s)^{1/2})\bigr)
$$

---

## Canonical Examples (Results Only)

The full derivations and probabilistic interpretations are in [Transition Density as Green's Function](transition_density_as_greens_function.md); the spectral/eigenfunction structure is in [Spectral Decomposition](spectral_decomposition.md).

**Brownian motion with drift.** For $dX_t = \mu\,dt + \sigma\,dW_t$,

$$
G(t, x; s, y) = \frac{1}{\sigma\sqrt{2\pi(t-s)}}\exp\!\left(-\frac{(x - y - \mu(t-s))^2}{2\sigma^2(t-s)}\right)
$$

**Ornstein-Uhlenbeck.** For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$,

$$
G(t, x; s, y) = \frac{1}{\sqrt{2\pi\,v(\tau)}}\exp\!\left(-\frac{(x - y e^{-\kappa\tau})^2}{2\,v(\tau)}\right), \qquad v(\tau) = \frac{\sigma^2}{2\kappa}\bigl(1 - e^{-2\kappa\tau}\bigr)
$$

with $\tau = t - s$. Mean reverts at rate $\kappa$; variance saturates at $\sigma^2/(2\kappa)$.

---

## Summary

$$
\boxed{\;u(t, x) = \int G(t, x; s, y)\,f(y)\,dy \quad \text{(superposition principle)}\;}
$$

| Property | Statement |
|---|---|
| Definition | $\partial_t G = \mathcal{L}_x G$, $G(s^+, x; s, y) = \delta(x-y)$ |
| Positivity | $G > 0$ for $t > s$ |
| Normalization | $\int G\,dx = 1$ |
| Semigroup | $G(t,x;s,y) = \int G(t,x;r,z)\,G(r,z;s,y)\,dz$ |
| Smoothing | $L^\infty \to C^\infty$ |

The Green's function is the fundamental building block for parabolic PDEs: it solves the point-source problem, and arbitrary solutions follow by superposition. In probability it is the transition density; in finance it is the state-price density -- both discussed in [Transition Density as Green's Function](transition_density_as_greens_function.md).

---

## See Also

- [Transition Density as Green's Function](transition_density_as_greens_function.md) -- probabilistic lens, equivalence proof, forward/backward table
- [Spectral Decomposition](spectral_decomposition.md) -- eigenfunction expansion of $G$
- [Free vs Bounded Domains](free_vs_bounded_domains.md) -- how boundaries modify $G$
- [Fundamental Solution](../heat_equation/fundamental_solution.md) -- heat kernel as the simplest $G$

---

## Exercises

**Exercise 1.**
For the heat equation on $\mathbb{R}$, verify that $G(t,x;0,y) = (2\pi t)^{-1/2}\exp(-(x-y)^2/(2t))$ satisfies the delta-function initial condition: $\lim_{t \to 0^+}\int G(t,x;0,y)\,f(y)\,dy = f(x)$ for continuous bounded $f$.

??? success "Solution to Exercise 1"
    Substitute $z = (y-x)/\sqrt{t}$, so $y = x + z\sqrt{t}$ and $dy = \sqrt{t}\,dz$:

    $$
    \int G(t,x;0,y)\,f(y)\,dy = \int \frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,f(x + z\sqrt{t})\,dz
    $$

    As $t \to 0^+$, $f(x + z\sqrt{t}) \to f(x)$ pointwise. By dominated convergence (with bound $\|f\|_\infty$ times the standard Gaussian),

    $$
    \lim_{t \to 0^+}\int \frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,f(x + z\sqrt{t})\,dz = f(x)\int\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz = f(x)
    $$

    $G$ acts as an approximate identity as $t \to 0^+$.

---

**Exercise 2.**
Using the superposition principle, compute $u(t, x) = \int G(t,x;0,y)\,e^{-y^2}\,dy$ for the free-space heat kernel.

??? success "Solution to Exercise 2"
    Combine exponents:

    $$
    -\frac{(x-y)^2}{2t} - y^2 = -\frac{(1+2t)y^2 - 2xy + x^2}{2t}
    $$

    Complete the square: $(1+2t)y^2 - 2xy = (1+2t)(y - x/(1+2t))^2 - x^2/(1+2t)$, leaving an $x^2$ residual of $-x^2/(1+2t)$. The Gaussian integral in $y$ contributes $\sqrt{2\pi t/(1+2t)}$. Hence

    $$
    u(t, x) = \frac{1}{\sqrt{1+2t}}\exp\!\left(-\frac{x^2}{1+2t}\right)
    $$

    A Gaussian broadening in time, consistent with convolution adding variances.

---

**Exercise 3.**
State the superposition formula for the inhomogeneous problem $\partial_t u - \tfrac{1}{2}u_{xx} = h(t,x)$, $u(0,x) = 0$, and explain in one paragraph why it is called **Duhamel's principle**.

??? success "Solution to Exercise 3"
    The solution is

    $$
    u(t, x) = \int_0^t\!\int G(t, x; s, y)\,h(s, y)\,dy\,ds
    $$

    Duhamel's principle: treat the source as a time-indexed family of initial conditions. The piece $h(s, y)\,ds$ injected at time $s$ evolves according to $G(t, x; s, y)$ for the remaining time $t - s$. Integrating over all injection times gives the total response. This is the direct translation of the superposition principle from spatial point sources to space-time point sources.

---

**Exercise 4.**
The parametrix method approximates $G$ by freezing coefficients at the source. Write down the frozen-coefficient Green's function $G_0$ for $\mathcal{L} = \mu(x)\partial_x + \tfrac{1}{2}\sigma^2(x)\partial_{xx}$ and explain why the approximation is good for small $t - s$.

??? success "Solution to Exercise 4"
    Freezing $\mu, \sigma$ at the source $y$:

    $$
    G_0(t, x; s, y) = \frac{1}{\sigma(y)\sqrt{2\pi(t-s)}}\exp\!\left(-\frac{(x - y - \mu(y)(t-s))^2}{2\sigma^2(y)(t-s)}\right)
    $$

    Over a short interval $t - s$, a diffusion started at $y$ stays close to $y$ (typical excursion $\sim \sigma(y)\sqrt{t-s}$), so $\mu, \sigma$ vary little over the path. Hölder continuity of the coefficients bounds the variation by a power of $t - s$, which makes the parametrix series converge with short-time error $O((t-s)^{1/2})$ relative to $G_0$.

---

**Exercise 5.**
Use the superposition formula to express the price of a European derivative with payoff $g(S_T)$ under a diffusion model as an integral against $G$. Identify the factor that makes $G$ the **state-price density** (Arrow-Debreu price).

??? success "Solution to Exercise 5"
    Under the risk-neutral measure, $V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]$. Writing the expectation as an integral,

    $$
    V(t, S) = \int g(S_T)\,\bigl[e^{-r(T-t)}G(T, S_T; t, S)\bigr]\,dS_T
    $$

    The bracketed quantity $e^{-r(T-t)}G(T, S_T; t, S)\,dS_T$ is the **Arrow-Debreu price**: what you pay today for \$1 delivered if $S_T \in [S_T, S_T + dS_T]$. Knowing $G$ is equivalent to knowing all European prices; see [Transition Density as Green's Function](transition_density_as_greens_function.md) for the full financial development.

---

**Exercise 6.**
For the constant-coefficient operator $\mathcal{L} = \tfrac{1}{2}\partial_{xx} - \tfrac{1}{2}\partial_x$ (drift $-1/2$), derive $G(t, x; 0, y)$ from the heat kernel by the change of variable $u = e^{\alpha x + \beta t}\,v$ that eliminates the first-order term.

??? success "Solution to Exercise 6"
    Substituting $u = e^{\alpha x + \beta t}\,v$ into $u_t = \tfrac{1}{2}u_{xx} - \tfrac{1}{2}u_x$ and collecting: the $v_x$ coefficient is $\alpha - 1/2$, vanishing at $\alpha = 1/2$. The remaining coefficient of $v$ then forces $\beta = \alpha/2 - \alpha^2/2 = 1/8$. So $v$ solves the standard heat equation $v_t = \tfrac{1}{2}v_{xx}$.

    Reverting with the heat kernel $\Gamma(t, x-y) = (2\pi t)^{-1/2}e^{-(x-y)^2/(2t)}$ and combining exponents:

    $$
    -\frac{(x-y)^2}{2t} - \tfrac{1}{2}(x-y) - \tfrac{t}{8} = -\frac{(x - y + t/2)^2}{2t}
    $$

    Therefore

    $$
    G(t, x; 0, y) = \frac{1}{\sqrt{2\pi t}}\exp\!\left(-\frac{(x - y + t/2)^2}{2t}\right)
    $$

    The drift $\mu = -1/2$ simply translates the Gaussian's center by $\mu t$.
