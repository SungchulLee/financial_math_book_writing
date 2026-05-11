# Classification of Second-Order PDEs

The behavior of a second-order PDE is determined by its **type**: elliptic, parabolic, or hyperbolic. This classification governs which boundary conditions are appropriate, whether solutions are smooth or can develop shocks, and which numerical methods converge. In finance, virtually every pricing PDE is **parabolic** -- a direct consequence of the diffusion nature of asset price models.

---

## The General Second-Order Linear PDE

In two independent variables $(x, y)$, the most general second-order linear PDE takes the form:

$$
A\frac{\partial^2 u}{\partial x^2} + 2B\frac{\partial^2 u}{\partial x\,\partial y} + C\frac{\partial^2 u}{\partial y^2} + \text{lower-order terms} = 0
$$

where $A$, $B$, $C$ may depend on $(x, y)$.

The classification depends on the **discriminant**:

$$
\boxed{
\Delta = B^2 - AC
}
$$

| Discriminant | Type | Prototype | Physical Behavior |
|---|---|---|---|
| $\Delta < 0$ | **Elliptic** | Laplace equation | Steady-state, equilibrium |
| $\Delta = 0$ | **Parabolic** | Heat equation | Diffusion, smoothing |
| $\Delta > 0$ | **Hyperbolic** | Wave equation | Propagation, oscillation |

!!! note "Analogy with Conic Sections"
    The names come from the classification of the conic $Ax^2 + 2Bxy + Cy^2 = 1$. The same discriminant $B^2 - AC$ determines whether the conic is an ellipse ($< 0$), parabola ($= 0$), or hyperbola ($> 0$). This is not a coincidence: the characteristic curves of the PDE are governed by the same quadratic form.

---

## The Three Types in Detail

### Elliptic Equations

**Prototype**: Laplace's equation

$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0
$$

Here $A = C = 1$, $B = 0$, so $\Delta = -1 < 0$.

**Key properties:**

- Solutions are **infinitely smooth** (analytic, in fact)
- **Maximum principle**: the maximum of $u$ occurs on the boundary
- Boundary data on the entire boundary determines the solution (Dirichlet problem)
- No preferred direction of propagation -- information spreads in all directions simultaneously

**Financial example**: The **steady-state bond pricing equation** when coefficients are time-independent:

$$
\mathcal{L}u - ru = 0
$$

where $\mathcal{L}$ is the generator of the short-rate process. This is an elliptic ODE in one spatial dimension.

### Parabolic Equations

**Prototype**: The heat equation

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}
$$

Rewriting as $-\frac{\partial u}{\partial t} + \frac{1}{2}\frac{\partial^2 u}{\partial x^2} = 0$ and setting $(x,y) = (x,t)$: we have $A = \frac{1}{2}$, $B = 0$, $C = 0$, giving $\Delta = 0$.

**Key properties:**

- **Smoothing**: Solutions become instantly $C^\infty$ for $t > 0$, even for rough initial data
- **Maximum principle**: Solutions cannot exceed their initial/boundary maxima
- **Causality**: Information propagates forward in time -- the solution at time $t$ depends only on data at earlier times
- Initial condition at $t = 0$ plus boundary conditions determine the solution

**Financial example**: The **Black-Scholes PDE** is parabolic.

### Hyperbolic Equations

**Prototype**: The wave equation

$$
\frac{\partial^2 u}{\partial t^2} = c^2\frac{\partial^2 u}{\partial x^2}
$$

Here $A = c^2$, $B = 0$, $C = -1$, so $\Delta = c^2 > 0$.

**Key properties:**

- **Finite propagation speed**: Disturbances travel at speed $c$
- **No smoothing**: Discontinuities in initial data persist
- Solutions can develop shocks and discontinuities
- Two initial conditions needed: $u(0,x)$ and $u_t(0,x)$

**Financial relevance**: Hyperbolic PDEs are essentially absent from standard financial models. Asset prices are modeled as diffusions (parabolic), not waves. However, certain mean-field game formulations in systemic risk can produce hyperbolic-like behavior.

---

## Why Financial PDEs Are Parabolic

The Black-Scholes PDE (see [Why PDEs in Finance](why_pdes_in_finance.md) for its full derivation and financial meaning) serves as the prototypical parabolic example:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

Identifying $A = \frac{1}{2}\sigma^2 S^2$, $B = 0$, and $C = 0$ (there is no $\partial^2 V / \partial t^2$ term):

$$
\Delta = 0^2 - \frac{1}{2}\sigma^2 S^2 \cdot 0 = 0
$$

The equation is **parabolic** (provided $\sigma > 0$ and $S > 0$).

!!! info "The Deep Reason"
    Financial PDEs are parabolic because they arise from diffusion processes via the Feynman-Kac theorem. Any Ito diffusion

    $$
    dX_t = \mu\,dt + \sigma\,dW_t
    $$

    has a generator $\mathcal{L} = \mu\partial_x + \frac{1}{2}\sigma^2\partial_{xx}$ that is a **second-order operator with no mixed time-space second derivatives**. The resulting PDE $\partial_t u + \mathcal{L}u = 0$ is always parabolic. Parabolicity is the PDE signature of Brownian diffusion.

---

## Classification for Variable Coefficients

When coefficients depend on position, the type can vary from point to point. For a general operator:

$$
\sum_{i,j=1}^{n} a_{ij}(x)\frac{\partial^2 u}{\partial x_i\,\partial x_j} + \text{lower-order terms} = 0
$$

the classification depends on the **eigenvalues of the coefficient matrix** $A = (a_{ij})$:

| Condition on Eigenvalues | Type |
|---|---|
| All nonzero, same sign | Elliptic |
| One zero eigenvalue, rest same sign | Parabolic |
| Nonzero eigenvalues of mixed sign | Hyperbolic |

### Degenerate Parabolicity

When $\sigma(x) = 0$ at some point, the PDE **degenerates** -- it loses its second-order character there. This matters in finance:

- **At $S = 0$** in Black-Scholes: $\frac{1}{2}\sigma^2 S^2 \to 0$, so the equation degenerates. The boundary $S = 0$ is an absorbing state where no boundary condition is needed
- **At the Feller boundary** in the CIR model: $\frac{1}{2}\xi^2 v \to 0$ as $v \to 0$, leading to subtle boundary behavior

!!! warning "Degeneracy and Regularity"
    At points of degeneracy, the PDE may not have classical (smooth) solutions. The theory of **viscosity solutions** provides the correct framework for well-posedness in degenerate cases.

---

## The Multidimensional Case

For a system with $d$ spatial dimensions and one time dimension, the pricing PDE has the form:

$$
\frac{\partial u}{\partial t} + \sum_{i=1}^{d}\mu_i\frac{\partial u}{\partial x_i} + \frac{1}{2}\sum_{i,j=1}^{d}(\Sigma\Sigma^\top)_{ij}\frac{\partial^2 u}{\partial x_i\,\partial x_j} - ru = 0
$$

where $\Sigma$ is the volatility matrix from the SDE $dX_t = \mu\,dt + \Sigma\,dW_t$.

**Classification**: The equation is parabolic if the diffusion matrix $a = \Sigma\Sigma^\top$ is **positive semi-definite**. It is **uniformly parabolic** (non-degenerate) if $a$ is **positive definite**, i.e., $\Sigma$ has full rank.

**Example**: In the Heston model with state $(S, v)$, the diffusion matrix is:

$$
a = \begin{pmatrix} vS^2 & \rho\xi v S \\ \rho\xi v S & \xi^2 v \end{pmatrix}
$$

The determinant is $\xi^2 v^2 S^2(1-\rho^2) > 0$ when $v > 0$, $S > 0$, and $|\rho| < 1$, so the system is non-degenerate parabolic in the interior.

---

## Characteristic Curves and Information Flow

Each PDE type has a distinct pattern of **characteristic curves** along which information propagates:

- **Elliptic**: No real characteristics -- information spreads in all directions instantly
- **Parabolic**: One family of characteristics (the time slices $t = \text{const}$) -- information flows forward in time
- **Hyperbolic**: Two families of characteristics -- information propagates at finite speed along specific directions

For financial PDEs, the parabolic structure means:

1. **Terminal conditions** at $t = T$ propagate backward to earlier times
2. The solution at $(t, S)$ depends on the terminal condition **everywhere** (infinite propagation speed in space)
3. Solutions are smooth for $t < T$ even if the terminal payoff is non-smooth

!!! example "Smoothing in Action"
    The call payoff $g(S) = (S - K)^+$ has a kink at $S = K$. Yet for any $t < T$, the Black-Scholes price $V(t, S)$ is a smooth ($C^\infty$) function of $S$. This is the **parabolic smoothing** property -- the diffusion in the PDE instantly regularizes discontinuities.

---

## Summary of the Classification

$$
\boxed{
B^2 - AC \begin{cases} < 0 & \text{Elliptic (equilibrium)} \\ = 0 & \text{Parabolic (diffusion)} \\ > 0 & \text{Hyperbolic (waves)} \end{cases}
}
$$

| Aspect | Elliptic | Parabolic | Hyperbolic |
|---|---|---|---|
| **Prototype** | $\Delta u = 0$ | $u_t = \frac{1}{2}u_{xx}$ | $u_{tt} = c^2 u_{xx}$ |
| **Smoothing** | Yes | Yes | No |
| **Max principle** | Yes | Yes | No |
| **Propagation** | All directions | Forward in time | Along characteristics |
| **Conditions** | Boundary only | Initial + boundary | Two initial conditions |
| **Finance** | Steady-state problems | Pricing PDEs | Not standard |

**In finance, parabolic PDEs are the rule because asset prices are modeled as diffusion processes. The classification tells us that pricing problems are well-posed with a terminal condition and appropriate boundary conditions, and that solutions enjoy the smoothing and maximum principle properties inherited from diffusion.**

---

## See Also

- [Why PDEs in Finance](why_pdes_in_finance.md) -- motivation for the PDE approach
- [Boundary Value Problems](boundary_value_problems.md) -- appropriate conditions for each PDE type
- [The SDE-PDE Bridge](sde_pde_bridge.md) -- how diffusion generators produce parabolic PDEs
- [Maximum Principle](../heat_equation/maximum_principle.md) -- the key property of parabolic equations

---

## Exercises

**Exercise 1.**
Classify each of the following PDEs as elliptic, parabolic, or hyperbolic by computing the discriminant $\Delta = B^2 - AC$:

(a) $u_{xx} + 2u_{xy} + u_{yy} = 0$

(b) $u_{xx} - 4u_{yy} = 0$

(c) $3u_{xx} + 2u_{xy} + u_{yy} = 0$

??? success "Solution to Exercise 1"
    **(a)** $u_{xx} + 2u_{xy} + u_{yy} = 0$: Here $A = 1$, $B = 1$ (the coefficient of $u_{xy}$ is $2B$, so $B = 1$), $C = 1$.

    $$
    \Delta = B^2 - AC = 1 - 1 = 0
    $$

    The equation is **parabolic**.

    **(b)** $u_{xx} - 4u_{yy} = 0$: Here $A = 1$, $B = 0$, $C = -4$.

    $$
    \Delta = B^2 - AC = 0 - (1)(-4) = 4 > 0
    $$

    The equation is **hyperbolic**. (This is a wave equation with speed $c = 2$.)

    **(c)** $3u_{xx} + 2u_{xy} + u_{yy} = 0$: Here $A = 3$, $B = 1$ (since the coefficient of $u_{xy}$ is $2B = 2$), $C = 1$.

    $$
    \Delta = B^2 - AC = 1 - 3 = -2 < 0
    $$

    The equation is **elliptic**.

---

**Exercise 2.**
The Black-Scholes PDE is $\partial_t V + rS\partial_S V + \frac{1}{2}\sigma^2 S^2 \partial_{SS} V - rV = 0$. Identify the highest-order coefficients $A$, $B$, $C$ (treating $(t, S)$ as the two independent variables) and verify that the discriminant gives $\Delta = 0$, confirming that the equation is parabolic.

??? success "Solution to Exercise 2"
    The Black-Scholes PDE is:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    With independent variables $(x, y) = (S, t)$, the highest-order terms are:

    - Coefficient of $\partial^2 V / \partial S^2$: this gives $A = \frac{1}{2}\sigma^2 S^2$
    - Coefficient of $\partial^2 V / \partial S\,\partial t$: there is no mixed second-order term, so $2B = 0$, hence $B = 0$
    - Coefficient of $\partial^2 V / \partial t^2$: there is no such term, so $C = 0$

    The discriminant is:

    $$
    \Delta = B^2 - AC = 0 - \frac{1}{2}\sigma^2 S^2 \cdot 0 = 0
    $$

    Since $\Delta = 0$, the equation is **parabolic**, as expected for a pricing PDE arising from a diffusion process. Note that this classification holds for all $S > 0$ and $\sigma > 0$; at $S = 0$ the equation degenerates (the leading coefficient $A$ vanishes).

---

**Exercise 3.**
The heat equation has the smoothing property: solutions become $C^\infty$ for $t > 0$ even if the initial data is discontinuous. The wave equation does not have this property. Explain this difference in terms of the PDE classification and the nature of characteristic curves for parabolic versus hyperbolic equations.

??? success "Solution to Exercise 3"
    **Parabolic equations (heat equation)**: The discriminant $\Delta = 0$ means there is exactly **one family of real characteristics** -- the time slices $t = \text{const}$. Information from the initial data propagates instantaneously in all spatial directions. In Fourier space, an initial mode $e^{ikx}$ evolves as $e^{ikx - \frac{1}{2}k^2 t}$, where the factor $e^{-\frac{1}{2}k^2 t}$ damps high-frequency components exponentially fast. This damping is stronger for larger $|k|$, which explains why the heat equation smooths rough initial data instantly: all discontinuities and kinks are immediately suppressed.

    **Hyperbolic equations (wave equation)**: The discriminant $\Delta > 0$ means there are **two families of real characteristics** $x \pm ct = \text{const}$. Information propagates at finite speed $c$ along these characteristics. The general solution $u(t,x) = f(x - ct) + g(x + ct)$ shows that the initial profile is simply translated without distortion. In Fourier space, modes evolve as $e^{i(kx \pm kct)}$ -- pure oscillation with no damping. Discontinuities in the initial data travel along the characteristics indefinitely without being smoothed.

    **Summary**: The parabolic structure implies infinite propagation speed with exponential frequency damping (smoothing), while the hyperbolic structure implies finite propagation speed with no damping (preservation of singularities). This is why the heat equation instantaneously regularizes any initial data, whereas the wave equation preserves discontinuities forever.

---

**Exercise 4.**
For the Heston model, the diffusion matrix is

$$
a = \begin{pmatrix} vS^2 & \rho\xi v S \\ \rho\xi v S & \xi^2 v \end{pmatrix}
$$

Compute the determinant and eigenvalues of $a$. Under what conditions on $v$, $S$, $\rho$, and $\xi$ is the pricing PDE non-degenerate parabolic? What happens at $v = 0$ or $S = 0$?

??? success "Solution to Exercise 4"
    The diffusion matrix of the Heston model is:

    $$
    a = \begin{pmatrix} vS^2 & \rho\xi v S \\ \rho\xi v S & \xi^2 v \end{pmatrix}
    $$

    **Determinant**:

    $$
    \det(a) = vS^2 \cdot \xi^2 v - (\rho\xi v S)^2 = \xi^2 v^2 S^2 - \rho^2\xi^2 v^2 S^2 = \xi^2 v^2 S^2(1 - \rho^2)
    $$

    **Eigenvalues**: The trace is $\text{tr}(a) = vS^2 + \xi^2 v = v(S^2 + \xi^2)$, and $\det(a) = \xi^2 v^2 S^2(1-\rho^2)$. The eigenvalues $\lambda_{1,2}$ satisfy:

    $$
    \lambda_{1,2} = \frac{\text{tr}(a) \pm \sqrt{\text{tr}(a)^2 - 4\det(a)}}{2}
    $$

    $$
    = \frac{v(S^2 + \xi^2) \pm \sqrt{v^2(S^2 + \xi^2)^2 - 4\xi^2 v^2 S^2(1-\rho^2)}}{2}
    $$

    The discriminant under the square root simplifies to:

    $$
    v^2\left[(S^2 - \xi^2)^2 + 4\rho^2\xi^2 S^2\right] \geq 0
    $$

    so both eigenvalues are real and non-negative.

    **Non-degenerate parabolic condition**: The PDE is non-degenerate parabolic when both eigenvalues are strictly positive, which requires $\det(a) > 0$. This holds when:

    - $v > 0$ (variance is positive)
    - $S > 0$ (stock price is positive)
    - $|\rho| < 1$ (correlation is not $\pm 1$)
    - $\xi > 0$ (vol-of-vol is positive)

    **At $v = 0$**: Both entries involving $v$ vanish, so $a = 0$ (the zero matrix). The PDE completely degenerates -- there is no diffusion. This corresponds to the variance process hitting zero, where the Feller boundary condition determines the behavior.

    **At $S = 0$**: The matrix becomes $a = \begin{pmatrix} 0 & 0 \\ 0 & \xi^2 v \end{pmatrix}$, which has rank 1 (if $v > 0$). The PDE degenerates in the $S$-direction but remains diffusive in the $v$-direction. As with Black-Scholes, $S = 0$ is an absorbing boundary for geometric Brownian motion.

---

**Exercise 5.**
Explain why the Black-Scholes PDE degenerates at $S = 0$ (the coefficient of $\partial_{SS}$ vanishes). What does this degeneracy imply about the nature of the boundary at $S = 0$ for geometric Brownian motion? Why is no boundary condition required there, unlike at a finite barrier?

??? success "Solution to Exercise 5"
    The Black-Scholes PDE has the second-order term $\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}$. At $S = 0$, the coefficient $\frac{1}{2}\sigma^2 S^2$ vanishes, so the PDE loses its second-order (diffusive) character. Similarly, the drift term $rS\frac{\partial V}{\partial S}$ also vanishes. The equation reduces to:

    $$
    \frac{\partial V}{\partial t} - rV = 0
    $$

    which is a first-order ODE in $t$ that determines $V(t, 0)$ uniquely from the terminal condition $V(T, 0) = g(0)$.

    **Why no boundary condition is needed**: For a non-degenerate parabolic PDE on a domain with boundary, a boundary condition is required because the diffusion term allows the process to reach the boundary, and we must specify what happens there. At $S = 0$, the diffusion coefficient vanishes, so the PDE cannot "transport" information through the boundary $S = 0$. The equation is self-contained at that point.

    **Probabilistic connection**: Geometric Brownian motion has the explicit solution:

    $$
    S_t = S_0 \exp\!\left(\left(r - \tfrac{1}{2}\sigma^2\right)t + \sigma W_t\right)
    $$

    The exponential function is strictly positive for all real arguments, so $S_t > 0$ for all $t \geq 0$ whenever $S_0 > 0$. Therefore $\mathbb{P}(S_t = 0 \text{ for some } t > 0) = 0$. Since the diffusion never reaches $S = 0$, there are no sample paths that require a boundary rule at $S = 0$. The conditional expectation $V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]$ is fully determined without specifying boundary behavior.

    In contrast, at a finite barrier $B > 0$, the coefficient $\frac{1}{2}\sigma^2 B^2 > 0$ and the process reaches $B$ with positive probability, so a boundary condition is necessary to specify the option's behavior upon barrier contact.

---

**Exercise 6.**
For an Ito diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$, the generator $\mathcal{L} = \mu\partial_x + \frac{1}{2}\sigma^2\partial_{xx}$ is a second-order operator with no mixed $\partial_{tx}$ term. Explain why this structure always produces a parabolic PDE $\partial_t u + \mathcal{L}u = 0$, regardless of the choice of $\mu$ and $\sigma$ (provided $\sigma \neq 0$).

??? success "Solution to Exercise 6"
    For a general Ito diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$, the infinitesimal generator is:

    $$
    \mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
    $$

    The Kolmogorov backward equation for $u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$ is:

    $$
    \frac{\partial u}{\partial t} + \mathcal{L}u = 0
    $$

    Written explicitly:

    $$
    \frac{\partial u}{\partial t} + \mu(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2} = 0
    $$

    Identifying the second-order coefficients with $(x, y) = (x, t)$:

    - $A = \frac{1}{2}\sigma^2(x)$ (coefficient of $\partial_{xx}$)
    - $B = 0$ (no mixed $\partial_{xt}$ term)
    - $C = 0$ (no $\partial_{tt}$ term)

    The discriminant is $\Delta = B^2 - AC = 0 - \frac{1}{2}\sigma^2(x) \cdot 0 = 0$.

    This gives $\Delta = 0$ **regardless** of the specific forms of $\mu$ and $\sigma$. The reason is structural: the Ito SDE is first-order in time ($dX_t = \ldots\,dt + \ldots\,dW_t$), so the generator $\mathcal{L}$ contains no time derivatives. The resulting PDE $\partial_t u + \mathcal{L}u = 0$ is therefore first-order in $t$ and (at most) second-order in $x$, with no $\partial_{tt}$ or $\partial_{tx}$ terms. This structure forces $B = C = 0$ and hence $\Delta = 0$, making the PDE parabolic.

    The condition $\sigma \neq 0$ ensures that $A = \frac{1}{2}\sigma^2 > 0$, so the equation is genuinely second-order (non-degenerate parabolic), with the associated smoothing and maximum principle properties. If $\sigma = 0$ everywhere, the equation reduces to a first-order PDE (transport equation) rather than a parabolic one.

---

**Exercise 7.**
The call payoff $g(S) = (S - K)^+$ has a kink (discontinuous first derivative) at $S = K$. Yet for any $t < T$, the Black-Scholes price $V(t, S)$ is a smooth function of $S$. This is the parabolic smoothing property. Give an intuitive explanation using the probabilistic interpretation: $V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t = S]$ is an average over many possible terminal values, which smooths out the kink.

??? success "Solution to Exercise 7"
    The Black-Scholes price of a European call is:

    $$
    V(t, S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}\!\left[(S_T - K)^+ \mid S_t = S\right]
    $$

    Under the risk-neutral measure, $S_T = S\exp\!\left((r - \frac{1}{2}\sigma^2)(T-t) + \sigma\sqrt{T-t}\,Z\right)$ where $Z \sim N(0,1)$. Thus:

    $$
    V(t, S) = e^{-r(T-t)} \int_{-\infty}^{\infty} \left(S e^{(r-\frac{1}{2}\sigma^2)(T-t) + \sigma\sqrt{T-t}\,z} - K\right)^+ \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz
    $$

    **Why smoothing occurs**: The payoff $(S_T - K)^+$ has a kink at $S_T = K$. However, the price $V(t, S)$ is an **integral** of this kinked function against the Gaussian density $\phi(z)$. This integral is a convolution-like operation that averages the payoff over all possible outcomes of $S_T$.

    For any $t < T$, the distribution of $S_T \mid S_t = S$ is a **log-normal distribution with positive variance** $\sigma^2(T-t) > 0$. The key mechanism is:

    1. When $S$ varies smoothly, the entire log-normal distribution of $S_T$ shifts smoothly
    2. The kink at $S_T = K$ is a fixed feature of the integrand, but the weight placed on values near $K$ changes smoothly as $S$ varies
    3. Integration against a smooth (Gaussian) kernel produces a smooth function

    Technically, differentiation under the integral sign is justified because the Gaussian density $\phi(z)$ is $C^\infty$ and decays rapidly. Each derivative $\frac{\partial^k V}{\partial S^k}$ passes through the integral, producing a finite result for all orders $k$.

    At $t = T$, however, the variance $\sigma^2(T - t) = 0$, so $S_T = S$ deterministically. The "averaging" collapses to a point evaluation, and the kink reappears: $V(T, S) = (S - K)^+$. The smoothing is only effective when there is genuine uncertainty ($T - t > 0$) to "smear out" the non-smoothness.
