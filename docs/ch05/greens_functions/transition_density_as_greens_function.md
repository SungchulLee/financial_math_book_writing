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

Recall (see [§ Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md) and [§ Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md)): $p(t,x\mid s,y)$ satisfies $\partial_t p = \mathcal{L}_x^* p$ in the destination $(t,x)$ and $-\partial_s p = \mathcal{L}_y p$ in the origin $(s,y)$, each with the delta initial/terminal condition. The forward operator $\mathcal{L}^* p = -\partial_x[\mu p] + \tfrac12\partial_{xx}[\sigma^2 p]$ is the formal adjoint of the generator; this adjoint structure is what enforces conservation of probability.

| Equation | Varies | Fixed | Operator | Role |
|---|---|---|---|---|
| Forward (Fokker-Planck) | $(t, x)$ destination | $(s, y)$ origin | $\mathcal{L}_x^*$ | Density evolution |
| Backward (Kolmogorov) | $(s, y)$ origin | $(t, x)$ destination | $\mathcal{L}_y$ | Expectation / pricing |

Here the Green's-function lens adds one observation: the **same** kernel $G = p$ solves both PDEs simultaneously -- forward in $(t,x)$, backward in $(s,y)$ -- because the delta-source condition is symmetric in the two variable pairs. The two Kolmogorov equations are thus two views of one object, not two unrelated facts.

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

Recall (see [§ Fundamental Solution](../heat_equation/fundamental_solution.md) and [§ Transition Densities for Standard SDEs](../kolmogorov_equations/transition_densities_standard_sdes.md)): for $dX_t = \mu\,dt + \sigma\,dW_t$ with $X_t - X_s \sim N(\mu(t-s), \sigma^2(t-s))$,

$$
p(t, x \mid s, y) = \frac{1}{\sigma\sqrt{2\pi(t-s)}}\exp\!\left(-\frac{(x - y - \mu(t-s))^2}{2\sigma^2(t-s)}\right)
$$

is the heat kernel translated by the drift -- and identifying it as $G$ makes the Black-Scholes operator's fundamental solution an Arrow-Debreu kernel.

---

## Ornstein-Uhlenbeck

Recall (see [§ Transition Densities for Standard SDEs](../kolmogorov_equations/transition_densities_standard_sdes.md)): for $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, $p(t,x\mid s,y)$ is Gaussian with mean $ye^{-\kappa\tau}$ and variance $v(\tau) = \sigma^2(1-e^{-2\kappa\tau})/(2\kappa)$, $\tau = t-s$.

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

Recall (see [§ Geometric Brownian Motion](../kolmogorov_equations/transition_densities_standard_sdes.md#geometric-brownian-motion) and [§ Black-Scholes via Heat Equation](../../ch06/bs_pde_analytic_solution/heat_equation.md)): the risk-neutral GBM transition density is the lognormal $p^{\mathbb{Q}}(T,S_T\mid t,S)$, and integrating any payoff against $e^{-r(T-t)}p^{\mathbb{Q}}$ reproduces the Black-Scholes price. The Green's-function lens identifies this kernel as the Arrow-Debreu state-price density for the Black-Scholes operator.

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
The direct verification of the forward equation $\partial_t p = -\mu\partial_x p + \tfrac12\sigma^2\partial_{xx}p$ for the Gaussian density of $dX_t = \mu\,dt + \sigma\,dW_t$ is carried out in [§ Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md). Explain why this same Gaussian must **also** solve the backward equation $-\partial_s p = \mu\partial_y p + \tfrac12\sigma^2\partial_{yy}p$, without redoing the differentiation.

??? success "Solution to Exercise 1"
    The Gaussian depends on $(t,x,s,y)$ only through $\tau = t-s$ and $w = x - y - \mu\tau$. Under the symmetry $(t,x) \leftrightarrow (s,y)$, $\tau \to -\tau$ and $w \to -w$, but the density depends only on $\tau$ and $w^2$, so the forward operator in $(t,x)$ and the backward operator in $(s,y)$ produce identical actions on $p$. This is the Green's-function identity at work: one kernel, two PDEs.

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
The full derivation of $V = S\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)$ from the lognormal transition density of geometric Brownian motion is carried out in [§ Black-Scholes PDE: Analytic Solutions](../../ch06/bs_pde_analytic_solution/heat_equation.md). In the Green's-function language of this page, state which object $G$ is being integrated against and identify the financial role of the prefactor $e^{-r(T-t)}$.

??? success "Solution to Exercise 4"
    $G$ is the **risk-neutral lognormal transition density** $p^{\mathbb{Q}}(T,S_T \mid t,S)$ for GBM under $\mathbb{Q}$; the pricing integral $V(t,S) = e^{-r(T-t)}\int (S_T - K)^+ G\,dS_T$ integrates the payoff against $G$ over the in-the-money region.

    The prefactor $e^{-r(T-t)}$ converts the kernel into the **Arrow-Debreu state-price density**: $e^{-r(T-t)}G(T,S_T;t,S)\,dS_T$ is the price today of \$1 delivered if $S_T \in [S_T, S_T+dS_T]$. The Black-Scholes formula is then the integral of the call payoff against this state-price density.

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
