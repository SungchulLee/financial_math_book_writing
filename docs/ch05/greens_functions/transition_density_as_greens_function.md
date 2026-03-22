# Transition Density as Green's Function

The **transition density** of a diffusion process and the **Green's function** of the corresponding parabolic PDE are the same mathematical object viewed from two perspectives. This identification is one of the most powerful results connecting probability and analysis: it means every statement about diffusion probabilities has an equivalent PDE formulation, and vice versa.

---

## The Two Perspectives

### Probabilistic: Transition Density

Given the SDE:

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

the **transition density** $p(t, x \mid s, y)$ is defined by:

$$
\mathbb{P}(X_t \in A \mid X_s = y) = \int_A p(t, x \mid s, y)\,dx
$$

It answers: *starting from $y$ at time $s$, what is the probability density of being at $x$ at time $t$?*

### Analytical: Green's Function

The **Green's function** $G(t, x; s, y)$ of the operator $\partial_t - \mathcal{L}$ satisfies:

$$
\frac{\partial G}{\partial t} = \mathcal{L}_x G, \quad \lim_{t \downarrow s} G(t, x; s, y) = \delta(x - y)
$$

It answers: *what is the PDE response at $(t, x)$ to a unit impulse at $(s, y)$?*

### The Identification

$$
\boxed{
p(t, x \mid s, y) = G(t, x; s, y)
}
$$

**The transition density of the diffusion is the Green's function of its generator.**

---

## Why Are They Equal?

The identification follows from the Kolmogorov backward equation. Define:

$$
u(s, y) = \mathbb{E}[g(X_t) \mid X_s = y] = \int g(x)\,p(t, x \mid s, y)\,dx
$$

The Kolmogorov backward equation states that $u$ satisfies:

$$
-\frac{\partial u}{\partial s} = \mathcal{L}_y u, \quad u(t, y) = g(y)
$$

But the Green's function representation gives:

$$
u(s, y) = \int g(x)\,G(t, x; s, y)\,dx
$$

Since this holds for all test functions $g$, we must have $p(t, x \mid s, y) = G(t, x; s, y)$.

**In other words**: the backward equation, which governs expected values, forces the transition density to coincide with the Green's function.

---

## Both Equations Simultaneously

The transition density/Green's function satisfies two PDEs in different variables:

### Forward Equation (Fokker-Planck)

Fix the initial state $(s, y)$ and let $(t, x)$ vary:

$$
\boxed{
\frac{\partial p}{\partial t}(t, x \mid s, y) = \mathcal{L}_x^* p(t, x \mid s, y)
}
$$

where $\mathcal{L}^*$ is the adjoint generator:

$$
\mathcal{L}^* p = -\frac{\partial}{\partial x}[\mu(x)\,p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)\,p]
$$

**Initial condition**: $p(s, x \mid s, y) = \delta(x - y)$

**Interpretation**: Tracks how probability density spreads from the source point $y$.

### Backward Equation (Kolmogorov)

Fix the observation state $(t, x)$ and let $(s, y)$ vary:

$$
\boxed{
-\frac{\partial p}{\partial s}(t, x \mid s, y) = \mathcal{L}_y p(t, x \mid s, y)
}
$$

**Terminal condition**: $p(t, x \mid t, y) = \delta(x - y)$

**Interpretation**: As you vary the starting point $y$ or starting time $s$, the transition density to a fixed destination $(t, x)$ satisfies the backward equation.

| Equation | Varies | Fixed | Operator |
|---|---|---|---|
| Forward | $(t, x)$ destination | $(s, y)$ origin | $\mathcal{L}^*$ (adjoint) |
| Backward | $(s, y)$ origin | $(t, x)$ destination | $\mathcal{L}$ (generator) |

---

## Verification for Brownian Motion

For $dX_t = dW_t$ (standard Brownian motion), the generator is $\mathcal{L} = \frac{1}{2}\partial_{xx}$.

The transition density is:

$$
p(t, x \mid s, y) = \frac{1}{\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x-y)^2}{2(t-s)}\right)
$$

**Forward equation check**: $\mathcal{L}^* = \mathcal{L} = \frac{1}{2}\partial_{xx}$ (self-adjoint).

$$
\frac{\partial p}{\partial t} = p\left(\frac{(x-y)^2}{2(t-s)^2} - \frac{1}{2(t-s)}\right)
$$

$$
\frac{1}{2}\frac{\partial^2 p}{\partial x^2} = \frac{1}{2}p\left(\frac{(x-y)^2}{(t-s)^2} - \frac{1}{t-s}\right) = p\left(\frac{(x-y)^2}{2(t-s)^2} - \frac{1}{2(t-s)}\right)
$$

These are equal. $\checkmark$

**Backward equation check**: By symmetry in $(x,y)$, the backward equation in $y$ gives the same result. $\checkmark$

---

## The Chapman-Kolmogorov Equation

The semigroup property of the Green's function corresponds to the **Chapman-Kolmogorov equation** for transition densities.

For $s < r < t$:

$$
p(t, x \mid s, y) = \int_{-\infty}^{\infty} p(t, x \mid r, z)\,p(r, z \mid s, y)\,dz
$$

**Probabilistic proof**: By the Markov property and the law of total probability:

$$
\mathbb{P}(X_t \in dx \mid X_s = y) = \int \mathbb{P}(X_t \in dx \mid X_r = z)\,\mathbb{P}(X_r \in dz \mid X_s = y)
$$

Writing in terms of densities gives the Chapman-Kolmogorov equation. $\square$

**PDE proof**: The semigroup property follows from the uniqueness of solutions to the initial value problem (superposition).

---

## Financial Applications

### State-Price Density

Under the risk-neutral measure $\mathbb{Q}$, the transition density of the asset price process is the **state-price density** (or **Arrow-Debreu price**):

$$
V(t, S) = e^{-r(T-t)}\int_0^{\infty} g(S_T)\,p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T
$$

Here $p^{\mathbb{Q}}$ is the transition density of $S_t$ under $\mathbb{Q}$. For each terminal state $S_T$, the integrand $e^{-r(T-t)}p^{\mathbb{Q}}(T, S_T \mid t, S)$ is the price today of a security that pays $\$1$ if $S_T = S_T$ and zero otherwise.

### Implied Transition Density from Options

The **Breeden-Litzenberger result** extracts the transition density from option prices:

$$
p^{\mathbb{Q}}(T, K \mid t, S) = e^{r(T-t)}\frac{\partial^2 C}{\partial K^2}(t, S; T, K)
$$

where $C(t, S; T, K)$ is the price of a European call with strike $K$ and maturity $T$.

!!! info "From Options to Densities"
    This remarkable formula says that the second derivative of the call price with respect to strike recovers the risk-neutral transition density. It is the basis of implied density estimation and model calibration from market data.

### Example: Black-Scholes Transition Density

Under geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, the log-return $\log(S_T/S_t)$ is normal:

$$
p^{\mathbb{Q}}(T, S_T \mid t, S) = \frac{1}{S_T\sigma\sqrt{2\pi(T-t)}} \exp\left(-\frac{(\log(S_T/S) - (r - \sigma^2/2)(T-t))^2}{2\sigma^2(T-t)}\right)
$$

This is the Green's function of the Black-Scholes operator, expressed in the original $(S_T)$ variable. Substituting into the pricing integral and evaluating gives the Black-Scholes formula.

---

## Transition Density as a Propagator

In physics terminology, the Green's function is a **propagator** -- it propagates the state of the system from one time to another.

$$
u(t, x) = \int p(t, x \mid s, y)\,u(s, y)\,dy
$$

This is a **semigroup action**: the map $T_{s,t}: u(s, \cdot) \mapsto u(t, \cdot)$ defined by integration against the transition density forms a semigroup:

$$
T_{s,t} = T_{r,t} \circ T_{s,r} \quad \text{for } s < r < t
$$

| Terminology | Probability | PDE | Finance |
|---|---|---|---|
| $p(t,x \mid s,y)$ | Transition density | Green's function | State-price density |
| $\int p \cdot f\,dy$ | Expected value | Solution of IVP | Option price |
| Chapman-Kolmogorov | Markov property | Semigroup property | Law of iterated expectations |
| $\delta(x-y)$ initial data | Start at $y$ | Point source | Unit Arrow-Debreu security |

---

## Example: Ornstein-Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, the transition density is:

$$
p(t, x \mid s, y) = \frac{1}{\sqrt{2\pi v(\tau)}} \exp\left(-\frac{(x - ye^{-\kappa\tau})^2}{2v(\tau)}\right)
$$

where $\tau = t - s$ and $v(\tau) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$.

**As Green's function**: This satisfies the forward equation:

$$
\frac{\partial p}{\partial t} = \kappa\frac{\partial}{\partial x}(xp) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
$$

and the backward equation:

$$
-\frac{\partial p}{\partial s} = -\kappa y\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Long-time limit**: As $\tau \to \infty$, the transition density converges to the stationary density $p_\infty(x) = N(0, \sigma^2/2\kappa)$, independent of $y$. This is the Green's function "forgetting" its initial condition.

---

## Summary

$$
\boxed{
p(t, x \mid s, y) = G(t, x; s, y) \quad \Longleftrightarrow \quad \text{transition density} = \text{Green's function}
}
$$

| Property | Probabilistic View | PDE View |
|---|---|---|
| Definition | $\mathbb{P}(X_t \in dx \mid X_s = y)/dx$ | Solution to $\partial_t G = \mathcal{L}_x G$ with $\delta$ data |
| Forward equation | Density evolution (Fokker-Planck) | Adjoint operator on observation variables |
| Backward equation | Expected values via generator | Original operator on source variables |
| Semigroup | Chapman-Kolmogorov / Markov property | Uniqueness / superposition |
| Normalization | Total probability = 1 | Conservation law |

**The identification of the transition density with the Green's function is the heart of the SDE-PDE connection. It allows probabilistic questions to be answered by PDE techniques and analytical questions to be answered by stochastic methods.**

---

## See Also

- [Green's Function for Parabolic PDEs](greens_function_parabolic.md) -- definition and construction
- [Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md) -- the forward PDE for the density
- [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md) -- the backward PDE for expectations
- [Transition Densities for Standard SDEs](../kolmogorov_equations/transition_densities_standard_sdes.md) -- explicit formulas
- [Feynman-Kac Formula](../feynman_kac/feynman_kac_formula.md) -- the extension with discounting
