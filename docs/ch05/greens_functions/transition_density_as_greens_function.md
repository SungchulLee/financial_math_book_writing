# Transition Density as Green's Function

The **transition density** of a diffusion and the **Green's function** of its generator are the same mathematical object viewed through two lenses. This page is the probability lens: it establishes the equivalence, derives the forward/backward equations, and develops the financial interpretation (state-price density, Arrow-Debreu price, Breeden-Litzenberger). The PDE lens -- operator definition, superposition principle, and smoothing -- is in [Green's Function for Parabolic PDEs](greens_function_parabolic.md).

---

## The Two Perspectives

Given the SDE $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ with generator $\mathcal{L}$, define:

- **Probabilistic.** The transition density $p(t, x \mid s, y)$ by $\mathbb{P}(X_t \in A \mid X_s = y) = \int_A p(t, x \mid s, y)\,dx$.
- **Analytical.** The Green's function $G(t, x; s, y)$ as the fundamental solution of $\partial_t - \mathcal{L}$ (see [Green's Function for Parabolic PDEs](greens_function_parabolic.md)).

The central claim:

$$
\boxed{\;p(t, x \mid s, y) = G(t, x; s, y)\;}
$$

The transition density of a diffusion is the Green's function of its generator.

---

## Proof of the Equivalence

Let $g$ be a bounded continuous test function and set

$$
u(s, y) = \mathbb{E}[g(X_t) \mid X_s = y] = \int g(x)\,p(t, x \mid s, y)\,dx
$$

The Kolmogorov backward equation (derived from Itô's formula applied to $u(s, X_s)$) gives

$$
-\partial_s u = \mathcal{L}_y u, \qquad u(t, y) = g(y)
$$

The Green's function representation of the same backward problem gives

$$
u(s, y) = \int g(x)\,G(t, x; s, y)\,dx
$$

Both representations hold for **every** bounded continuous $g$. By the density of such $g$ in the space of test functions, the kernels must agree:

$$
p(t, x \mid s, y) = G(t, x; s, y) \qquad \square
$$

The delta-function initial condition of $G$ reflects the point-mass initial law $X_s = y$ a.s.: both encode "the system starts with certainty at $y$".

---

## Forward and Backward Equations

The transition density satisfies **two** PDEs -- one in each pair of variables.

| Equation | Varies | Fixed | Operator | Role |
|---|---|---|---|---|
| **Forward** (Fokker-Planck) | $(t, x)$ destination | $(s, y)$ origin | $\mathcal{L}_x^*$ (adjoint) | Density evolution |
| **Backward** (Kolmogorov) | $(s, y)$ origin | $(t, x)$ destination | $\mathcal{L}_y$ (generator) | Expectation / pricing |

### Forward (Fokker-Planck)

$$
\boxed{\;\partial_t\,p(t, x \mid s, y) = \mathcal{L}_x^*\,p(t, x \mid s, y)\;}
$$

with initial condition $p(s, x \mid s, y) = \delta(x - y)$, where

$$
\mathcal{L}^* p = -\partial_x[\mu(x)\,p] + \tfrac{1}{2}\partial_{xx}[\sigma^2(x)\,p]
$$

The structure $\partial_t p + \partial_x J = 0$ (advective flux $\mu p$, diffusive flux $-\tfrac{1}{2}\partial_x(\sigma^2 p)$) is a conservation law: $\tfrac{d}{dt}\int p\,dx = 0$.

### Backward (Kolmogorov)

$$
\boxed{\;-\partial_s\,p(t, x \mid s, y) = \mathcal{L}_y\,p(t, x \mid s, y)\;}
$$

with terminal condition $p(t, x \mid t, y) = \delta(x - y)$.

!!! info "Why adjoint on the forward side"
    Integration by parts against a test function $g$:
    $\int g(\mathcal{L}p)\,dx = \int (\mathcal{L}^* g)\,p\,dx$ moves derivatives off $p$ and onto $g$, producing $-\partial_x[\mu\,p] + \tfrac{1}{2}\partial_{xx}[\sigma^2 p]$ -- exactly the forward operator. The adjoint structure is what enforces conservation of probability.

---

## Chapman-Kolmogorov Equation

For $s < r < t$:

$$
\boxed{\;p(t, x \mid s, y) = \int p(t, x \mid r, z)\,p(r, z \mid s, y)\,dz\;}
$$

**Probabilistic derivation.** By the Markov property and total probability,

$$
\mathbb{P}(X_t \in dx \mid X_s = y) = \int \mathbb{P}(X_t \in dx \mid X_r = z)\,\mathbb{P}(X_r \in dz \mid X_s = y)
$$

Dividing by $dx$ gives the displayed equation.

**PDE interpretation.** Solve the point-source problem in two stages: first evolve from $s$ to $r$, obtaining $p(r, z \mid s, y)$; then use this as initial data for the segment $r \to t$. By uniqueness, the two-stage result equals the direct transition $p(t, x \mid s, y)$. This is the semigroup property of $G$ from [Green's Function for Parabolic PDEs](greens_function_parabolic.md).

The pricing analogue is the **law of iterated expectations**: $\mathbb{E}[\,\cdot \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{E}[\,\cdot \mid \mathcal{F}_r] \mid \mathcal{F}_s]$.

---

## Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constants), the increment $X_t - X_s \sim N(\mu(t-s), \sigma^2(t-s))$, so

$$
p(t, x \mid s, y) = \frac{1}{\sigma\sqrt{2\pi(t-s)}}\exp\!\left(-\frac{(x - y - \mu(t-s))^2}{2\sigma^2(t-s)}\right)
$$

**Forward-equation check.** Set $\tau = t - s$, $w = x - y - \mu\tau$, so $p = (\sigma\sqrt{2\pi\tau})^{-1}\exp(-w^2/(2\sigma^2\tau))$. Direct differentiation:

$$
\partial_t p = p\!\left(-\frac{1}{2\tau} + \frac{w^2}{2\sigma^2\tau^2} + \frac{\mu w}{\sigma^2\tau}\right)
$$

$$
-\mu\partial_x p + \tfrac{1}{2}\sigma^2\partial_{xx}p = p\!\left(\frac{\mu w}{\sigma^2\tau} + \frac{w^2}{2\sigma^2\tau^2} - \frac{1}{2\tau}\right)
$$

The two sides match. This is the **Gaussian heat kernel (fundamental solution)** shifted by the drift.

---

## Ornstein-Uhlenbeck

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, the solution $X_t = y e^{-\kappa(t-s)} + \sigma\int_s^t e^{-\kappa(t-u)}\,dW_u$ is Gaussian with

$$
\mathbb{E}[X_t \mid X_s = y] = y e^{-\kappa\tau}, \qquad \mathrm{Var}(X_t \mid X_s = y) = v(\tau) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})
$$

Hence

$$
p(t, x \mid s, y) = \frac{1}{\sqrt{2\pi\,v(\tau)}}\exp\!\left(-\frac{(x - y e^{-\kappa\tau})^2}{2v(\tau)}\right)
$$

As $\tau \to \infty$, $p \to N(0, \sigma^2/(2\kappa))$ independent of $y$: the process **forgets** its initial condition and relaxes to the stationary density. The same phenomenon appears in [Spectral Decomposition](spectral_decomposition.md) as the decay of all non-zero eigenmodes -- and in [Free vs Bounded Domains](free_vs_bounded_domains.md) as the contrast between free-space dissipation and bounded-domain equilibration.

---

## Financial Interpretation

### State-Price Density

Under the risk-neutral measure $\mathbb{Q}$, the transition density of the asset price is the **state-price density** (Arrow-Debreu kernel):

$$
V(t, S) = e^{-r(T-t)}\int g(S_T)\,p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T
$$

For each terminal state $S_T$, the quantity $e^{-r(T-t)}p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T$ is the price today of an Arrow-Debreu security paying \$1 in that state and nothing otherwise. Knowing $p^{\mathbb{Q}}$ is equivalent to knowing all European option prices simultaneously. The integral-against-$G$ formulation is developed in [Green's Function for Parabolic PDEs](greens_function_parabolic.md).

### Breeden-Litzenberger

The second derivative of call prices with respect to strike recovers the risk-neutral density:

$$
\boxed{\;p^{\mathbb{Q}}(T, K \mid t, S) = e^{r(T-t)}\,\frac{\partial^2 C}{\partial K^2}(t, S; T, K)\;}
$$

This is the basis of implied-density estimation and non-parametric calibration from option quotes.

### Black-Scholes

For $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, Itô on $X_t = \ln S_t$ gives $dX_t = (r - \sigma^2/2)\,dt + \sigma\,dW_t^{\mathbb{Q}}$. The Gaussian density in $X_T$ transforms to the lognormal

$$
p^{\mathbb{Q}}(T, S_T \mid t, S) = \frac{1}{S_T\,\sigma\sqrt{2\pi(T-t)}}\exp\!\left(-\frac{(\ln(S_T/S) - (r - \sigma^2/2)(T-t))^2}{2\sigma^2(T-t)}\right)
$$

with the Jacobian $1/S_T$ from the exponential change of variables.

---

## Dictionary

| Object | Probability | PDE | Finance |
|---|---|---|---|
| $p(t, x \mid s, y) = G$ | Transition density | Green's function | State-price density |
| Action $\int G\cdot f$ | Expected value | Solution of IVP | Option price |
| Semigroup / CK | Markov property | Uniqueness / superposition | Iterated expectations |
| $\delta(x - y)$ initial | $X_s = y$ a.s. | Point source | Unit Arrow-Debreu |

---

## Summary

$$
\boxed{\;p(t, x \mid s, y) = G(t, x; s, y) \quad \Longleftrightarrow \quad \text{transition density} = \text{Green's function}\;}
$$

The identification collapses two parallel theories into one. Probabilistic questions become PDE problems; PDE problems become stochastic computations. The forward equation tracks density evolution; the backward equation prices claims. The Chapman-Kolmogorov / semigroup property expresses the Markov property in analytic form. And in finance, the Green's function **is** the Arrow-Debreu pricing kernel.

---

## See Also

- [Green's Function for Parabolic PDEs](greens_function_parabolic.md) -- operator definition, superposition, parametrix
- [Spectral Decomposition](spectral_decomposition.md) -- eigenfunction expansion of $p$, modal convergence to stationarity
- [Free vs Bounded Domains](free_vs_bounded_domains.md) -- boundary effects and killed transition densities
- [Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md)
- [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md)
- [Feynman-Kac Formula](../feynman_kac/feynman_kac_formula.md)

---

## Exercises

**Exercise 1.**
For $dX_t = \mu\,dt + \sigma\,dW_t$, verify the forward equation $\partial_t p = -\mu\partial_x p + \tfrac{1}{2}\sigma^2\partial_{xx}p$ from the explicit Gaussian density.

??? success "Solution to Exercise 1"
    With $\tau = t - s$ and $w = x - y - \mu\tau$, $p = (\sigma\sqrt{2\pi\tau})^{-1}\exp(-w^2/(2\sigma^2\tau))$.

    $$
    \partial_t p = p\!\left(-\frac{1}{2\tau} + \frac{w^2}{2\sigma^2\tau^2} + \frac{\mu w}{\sigma^2\tau}\right)
    $$

    $\partial_x p = -p\,w/(\sigma^2\tau)$ gives $-\mu\partial_x p = p\,\mu w/(\sigma^2\tau)$. And $\partial_{xx}p = p(w^2/(\sigma^4\tau^2) - 1/(\sigma^2\tau))$ gives $\tfrac{1}{2}\sigma^2\partial_{xx}p = p(w^2/(2\sigma^2\tau^2) - 1/(2\tau))$. Sum equals $\partial_t p$.

---

**Exercise 2.**
Verify the Chapman-Kolmogorov equation for standard Brownian motion by explicit Gaussian convolution.

??? success "Solution to Exercise 2"
    With $\tau_1 = r - s$, $\tau_2 = t - r$, combine exponents:

    $$
    -\frac{(x - z)^2}{2\tau_2} - \frac{(z - y)^2}{2\tau_1} = -\frac{(\tau_1 + \tau_2)(z - z^*)^2 + \tau_1\tau_2(x - y)^2/(\tau_1+\tau_2)}{2\tau_1\tau_2}
    $$

    with $z^* = (\tau_1 x + \tau_2 y)/(\tau_1 + \tau_2)$. The $z$-integral gives $\sqrt{2\pi\tau_1\tau_2/(\tau_1+\tau_2)}$. Combining prefactors:

    $$
    \frac{1}{\sqrt{2\pi(\tau_1 + \tau_2)}}\exp\!\left(-\frac{(x - y)^2}{2(\tau_1 + \tau_2)}\right) = p(t, x \mid s, y) \quad\checkmark
    $$

    The result says: adding independent Gaussian increments adds variances -- the defining property of Brownian motion.

---

**Exercise 3.**
State the forward and backward equations for the Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ in the two pairs of variables, and identify which PDE governs the option price $V(s, y) = \mathbb{E}[g(X_t) \mid X_s = y]$.

??? success "Solution to Exercise 3"
    With $\mathcal{L} = -\kappa x\,\partial_x + \tfrac{1}{2}\sigma^2\partial_{xx}$, the adjoint is $\mathcal{L}^* p = \kappa\,\partial_x(x p) + \tfrac{1}{2}\sigma^2\partial_{xx}p$.

    **Forward** (in $(t, x)$): $\partial_t p = \kappa\,\partial_x(x p) + \tfrac{1}{2}\sigma^2\partial_{xx}p$.

    **Backward** (in $(s, y)$): $-\partial_s p = -\kappa y\,\partial_y p + \tfrac{1}{2}\sigma^2\partial_{yy}p$.

    The option price $V(s, y) = \mathbb{E}[g(X_t) \mid X_s = y]$ depends on $(s, y)$ and satisfies the **backward** equation $-\partial_s V = \mathcal{L}_y V$ with $V(t, y) = g(y)$. The backward equation is the pricing equation; the forward equation governs implied-distribution and risk analysis.

---

**Exercise 4.**
For geometric Brownian motion, use the lognormal transition density to derive the risk-neutral pricing integral for a European call and show that it yields $V = S\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)$.

??? success "Solution to Exercise 4"
    With $p^{\mathbb{Q}}(T, S_T \mid t, S) = (S_T\sigma\sqrt{2\pi(T-t)})^{-1}\exp(-(\ln(S_T/S) - (r-\sigma^2/2)(T-t))^2/(2\sigma^2(T-t)))$,

    $$
    V(t, S) = e^{-r(T-t)}\int_K^\infty (S_T - K)\,p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T
    $$

    Change to $z = (\ln(S_T/S) - (r - \sigma^2/2)(T-t))/(\sigma\sqrt{T-t}) \sim N(0,1)$. The integration domain becomes $z > -d_2$ with $d_2 = (\ln(S/K) + (r - \sigma^2/2)(T-t))/(\sigma\sqrt{T-t})$.

    The $K$-piece gives $-Ke^{-r(T-t)}\mathcal{N}(d_2)$. The $S_T$-piece uses $S_T = S\exp(\sigma\sqrt{T-t}\,z + (r - \sigma^2/2)(T-t))$, completing the square in the integrand (shift $z \to z + \sigma\sqrt{T-t}$) to produce $S\mathcal{N}(d_1)$ with $d_1 = d_2 + \sigma\sqrt{T-t}$. Combining:

    $$
    V = S\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)
    $$

---

**Exercise 5.**
Explain **Breeden-Litzenberger**: derive $p^{\mathbb{Q}}(T, K \mid t, S) = e^{r(T-t)}\partial_K^2 C(t, S; T, K)$ by differentiating the pricing integral twice.

??? success "Solution to Exercise 5"
    $C(t, S; T, K) = e^{-r(T-t)}\int_K^\infty (S_T - K)\,p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T$.

    Differentiate once in $K$: the boundary term $(S_T - K)p^{\mathbb{Q}}$ at $S_T = K$ vanishes, leaving

    $$
    \partial_K C = -e^{-r(T-t)}\int_K^\infty p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T
    $$

    Differentiate again, applying Leibniz to the moving lower limit:

    $$
    \partial_K^2 C = e^{-r(T-t)}\,p^{\mathbb{Q}}(T, K \mid t, S)
    $$

    Rearranging gives the Breeden-Litzenberger formula. Model-free content: given a dense set of call quotes in $K$, the risk-neutral marginal density at maturity $T$ is recovered by numerical second differencing.

---

**Exercise 6.**
For a diffusion killed at an absorbing barrier $B$, the killed density $p_B(t, x \mid s, y) \le p(t, x \mid s, y)$ integrates to **less than** $1$. Relate the deficit to the first-passage probability $\mathbb{P}(\tau_B \le t \mid X_s = y)$ and derive the flux formula for the rate at which mass leaks out.

??? success "Solution to Exercise 6"
    The killed density is

    $$
    p_B(t, x \mid s, y)\,dx = \mathbb{P}(X_t \in dx,\ \tau_B > t \mid X_s = y)
    $$

    Integrating over $x$:

    $$
    \int p_B(t, x \mid s, y)\,dx = \mathbb{P}(\tau_B > t \mid X_s = y)
    $$

    so the deficit is $1 - \int p_B\,dx = \mathbb{P}(\tau_B \le t \mid X_s = y)$.

    The leakage rate follows from the Fokker-Planck equation with absorbing condition $p_B = 0$ at $x = B$:

    $$
    -\frac{d}{dt}\int p_B\,dx = \pm\tfrac{1}{2}\sigma^2(B)\,\partial_x p_B(t, B \mid s, y)
    $$

    (sign determined by whether $B$ is upper or lower barrier). In barrier-option pricing, this deficit is the knock-out probability; see [Free vs Bounded Domains](free_vs_bounded_domains.md) for the full boundary-value-problem treatment.
