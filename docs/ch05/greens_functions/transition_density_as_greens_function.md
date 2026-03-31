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

---

## Exercises

**Exercise 1.**
For the SDE $dX_t = \mu\,dt + \sigma\,dW_t$ (Brownian motion with drift), write the transition density $p(t, x | s, y)$ explicitly. Verify it satisfies the forward (Fokker-Planck) equation $\partial_t p = -\mu\partial_x p + \frac{1}{2}\sigma^2\partial_{xx}p$ by direct differentiation.

---

**Exercise 2.**
Explain the identification $p(t, x | s, y) = G(t, x; s, y)$ in words: the probability density of the diffusion at $(t, x)$ starting from $(s, y)$ equals the PDE response at $(t, x)$ to a unit impulse at $(s, y)$. Why does the delta-function initial condition of the Green's function correspond to a point-mass initial distribution for the diffusion?

---

**Exercise 3.**
The transition density satisfies the backward equation $\partial_s p + \mu(y)\partial_y p + \frac{1}{2}\sigma^2(y)\partial_{yy}p = 0$ as a function of $(s, y)$. Explain the financial significance: the backward equation tells how the option price depends on the current state, while the forward equation describes the evolution of the probability distribution.

---

**Exercise 4.**
For geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, the transition density of $S_T | S_t = S$ is lognormal. Write this density explicitly and verify that $\mathbb{E}[e^{-r(T-t)}g(S_T) | S_t = S] = \int e^{-r(T-t)}g(y)p(T, y | t, S)\,dy$ recovers the risk-neutral pricing formula.

---

**Exercise 5.**
The Chapman-Kolmogorov equation $p(t, x | s, y) = \int p(t, x | r, z)\,p(r, z | s, y)\,dz$ expresses the semigroup property of transition densities. Verify this for the Gaussian transition density of standard Brownian motion by computing the convolution of two Gaussians.

---

**Exercise 6.**
For a killed diffusion (absorbing boundary at $B$), the transition density becomes $p_B(t, x | s, y) < p(t, x | s, y)$ because paths that hit $B$ are removed. Explain why $\int p_B(t, x | s, y)\,dx < 1$ and relate the "missing mass" to the first-passage probability $\mathbb{P}(\tau_B \leq t | X_s = y)$.

---

**Exercise 7.**
Show that the option pricing formula $V(t, S) = e^{-r(T-t)}\int g(y)\,p(T, y | t, S)\,dy$ is a special case of the Feynman-Kac formula with $r$ constant and $f = 0$. Identify the Green's function in this representation and explain why it encodes all the information needed for European option pricing.

---

## Solutions

??? success "Solution to Exercise 1"
    For $dX_t = \mu\,dt + \sigma\,dW_t$ with constant $\mu$ and $\sigma$, the process is Gaussian with $X_t \mid X_s = y \sim N(y + \mu(t-s),\, \sigma^2(t-s))$. The transition density is

    $$
    p(t, x \mid s, y) = \frac{1}{\sigma\sqrt{2\pi(t-s)}} \exp\!\left(-\frac{(x - y - \mu(t-s))^2}{2\sigma^2(t-s)}\right)
    $$

    The Fokker-Planck equation is $\partial_t p = -\mu\,\partial_x p + \frac{1}{2}\sigma^2\,\partial_{xx}p$. Let $\tau = t - s$ and $w = x - y - \mu\tau$ for convenience, so $p = (\sigma\sqrt{2\pi\tau})^{-1}\exp(-w^2/(2\sigma^2\tau))$.

    **Computing $\partial_t p$**:

    $$
    \partial_t p = p\!\left(-\frac{1}{2\tau} + \frac{w^2}{2\sigma^2\tau^2} + \frac{\mu w}{\sigma^2\tau}\right)
    $$

    **Computing $-\mu\,\partial_x p$**: Since $\partial_x p = p \cdot (-w/(\sigma^2\tau))$, we get $-\mu\,\partial_x p = \mu w\,p/(\sigma^2\tau)$.

    **Computing $\frac{1}{2}\sigma^2\,\partial_{xx}p$**: $\partial_{xx}p = p\,(w^2/(\sigma^4\tau^2) - 1/(\sigma^2\tau))$, so $\frac{1}{2}\sigma^2\,\partial_{xx}p = p\,(w^2/(2\sigma^2\tau^2) - 1/(2\tau))$.

    Adding: $-\mu\,\partial_x p + \frac{1}{2}\sigma^2\,\partial_{xx}p = p\,(\mu w/(\sigma^2\tau) + w^2/(2\sigma^2\tau^2) - 1/(2\tau)) = \partial_t p$. $\checkmark$

??? success "Solution to Exercise 2"
    The identification $p(t, x \mid s, y) = G(t, x; s, y)$ says that two seemingly different objects are the same function:

    - **Probabilistic side**: $p(t, x \mid s, y)$ is the probability density of finding the diffusion $X_t$ at position $x$, given that it started at position $y$ at time $s$. This is defined through the SDE and the Markov property.

    - **Analytical side**: $G(t, x; s, y)$ is the solution of the PDE $\partial_t G = \mathcal{L}_x G$ with initial condition $G(s, x; s, y) = \delta(x - y)$. This is the PDE response to a point source.

    The delta-function initial condition $G(s, x; s, y) = \delta(x - y)$ corresponds to a point-mass initial distribution because both encode the same information: the system starts with certainty at position $y$. For the diffusion, "starting at $y$" means $X_s = y$ with probability $1$, which is a point mass $\delta_y$ in distribution space. For the PDE, a delta-function source $\delta(x - y)$ means all the "mass" (heat, probability) is concentrated at the single point $y$ at time $s$. As time evolves, both the probability distribution and the PDE solution spread out from this initial point in the same way, because the Kolmogorov equations (derived from the SDE) are exactly the PDEs that the Green's function satisfies.

??? success "Solution to Exercise 3"
    The backward equation $\partial_s p + \mu(y)\,\partial_y p + \frac{1}{2}\sigma^2(y)\,\partial_{yy}p = 0$ describes how the transition density varies as a function of the starting state $(s, y)$, with the destination $(t, x)$ held fixed.

    **Financial significance**: Consider the option price $V(s, y) = e^{-r(t-s)}\int g(x)\,p(t, x \mid s, y)\,dx$. Since $g$ and the observation point $(t, x)$ are integrated out, $V$ is a function of the current state $(s, y)$. The backward equation for $p$ translates directly into the Black-Scholes PDE for $V$:

    $$
    \partial_s V + \mu(y)\,\partial_y V + \frac{1}{2}\sigma^2(y)\,\partial_{yy}V - rV = 0
    $$

    This tells the trader how the option price changes with the current stock price $y$ and current time $s$ -- exactly the information needed for hedging and risk management.

    The **forward equation** $\partial_t p = \mathcal{L}^*_x p$ describes how the probability density evolves in time. It tells us how the distribution of future asset prices spreads out and shifts. This is useful for:

    - Understanding the shape of the implied distribution at different maturities
    - Calibrating models to market-observed distributions (implied densities from option prices)
    - Computing quantities like value-at-risk that depend on the full distribution

    In summary: the backward equation is the "pricing equation" (how value depends on current state), while the forward equation is the "distribution equation" (how probabilities evolve over time).

??? success "Solution to Exercise 4"
    Under $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, the log-price $X_t = \ln S_t$ satisfies $dX_t = (r - \sigma^2/2)\,dt + \sigma\,dW_t$ by Ito's formula. Given $S_t = S$, we have $X_t = \ln S$ and

    $$
    X_T \mid X_t = \ln S \sim N\!\left(\ln S + (r - \sigma^2/2)(T-t),\; \sigma^2(T-t)\right)
    $$

    The transition density of $S_T$ is obtained by the change of variables $S_T = e^{X_T}$:

    $$
    p(T, S_T \mid t, S) = \frac{1}{S_T\,\sigma\sqrt{2\pi(T-t)}} \exp\!\left(-\frac{(\ln(S_T/S) - (r-\sigma^2/2)(T-t))^2}{2\sigma^2(T-t)}\right)
    $$

    Now verify the pricing formula. The risk-neutral price of a derivative with payoff $g(S_T)$ is

    $$
    V(t, S) = e^{-r(T-t)}\int_0^{\infty} g(y)\,p(T, y \mid t, S)\,dy
    $$

    For a European call $g(y) = (y - K)^+$:

    $$
    V(t, S) = e^{-r(T-t)}\int_K^{\infty} (y - K)\,p(T, y \mid t, S)\,dy
    $$

    Substituting $z = (\ln(y/S) - (r - \sigma^2/2)(T-t))/(\sigma\sqrt{T-t})$, the integral splits into two terms. The first gives $S\,\Phi(d_1)$ (using the moment generating function of the normal) and the second gives $-Ke^{-r(T-t)}\Phi(d_2)$, where

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}
    $$

    This recovers the Black-Scholes formula $V = S\,\Phi(d_1) - Ke^{-r(T-t)}\Phi(d_2)$, confirming that the risk-neutral pricing integral with the lognormal transition density yields the correct result.

??? success "Solution to Exercise 5"
    For standard Brownian motion, the transition density is $p(t, x \mid s, y) = (2\pi(t-s))^{-1/2}\exp(-(x-y)^2/(2(t-s)))$. The Chapman-Kolmogorov equation requires

    $$
    p(t, x \mid s, y) = \int_{-\infty}^{\infty} p(t, x \mid r, z)\,p(r, z \mid s, y)\,dz
    $$

    for $s < r < t$. Let $\tau_1 = r - s$ and $\tau_2 = t - r$. The right side is

    $$
    \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\tau_2}}\exp\!\left(-\frac{(x-z)^2}{2\tau_2}\right) \frac{1}{\sqrt{2\pi\tau_1}}\exp\!\left(-\frac{(z-y)^2}{2\tau_1}\right)dz
    $$

    Combine the exponents: $-\frac{(x-z)^2}{2\tau_2} - \frac{(z-y)^2}{2\tau_1} = -\frac{\tau_1(x-z)^2 + \tau_2(z-y)^2}{2\tau_1\tau_2}$.

    Complete the square in $z$. The numerator is $(\tau_1 + \tau_2)z^2 - 2(\tau_1 x + \tau_2 y)z + (\tau_1 x^2 + \tau_2 y^2)$, which equals

    $$
    (\tau_1 + \tau_2)\!\left(z - \frac{\tau_1 x + \tau_2 y}{\tau_1 + \tau_2}\right)^2 + \frac{\tau_1\tau_2(x-y)^2}{\tau_1 + \tau_2}
    $$

    The Gaussian integral over $z$ evaluates to $\sqrt{2\pi\tau_1\tau_2/(\tau_1 + \tau_2)}$. Combining all factors:

    $$
    \frac{1}{2\pi\sqrt{\tau_1\tau_2}} \cdot \sqrt{\frac{2\pi\tau_1\tau_2}{\tau_1+\tau_2}} \cdot \exp\!\left(-\frac{(x-y)^2}{2(\tau_1+\tau_2)}\right) = \frac{1}{\sqrt{2\pi(\tau_1+\tau_2)}}\exp\!\left(-\frac{(x-y)^2}{2(\tau_1+\tau_2)}\right)
    $$

    Since $\tau_1 + \tau_2 = t - s$, this equals $p(t, x \mid s, y)$. $\checkmark$

    This result reflects the fact that the sum of independent Gaussian increments is Gaussian with variance equal to the sum of the variances.

??? success "Solution to Exercise 6"
    For a killed diffusion with absorbing boundary at $B$, a path is removed (killed) the first time it hits $B$. The transition density $p_B(t, x \mid s, y)$ accounts only for surviving paths:

    $$
    p_B(t, x \mid s, y)\,dx = \mathbb{P}(X_t \in dx,\; \tau_B > t \mid X_s = y)
    $$

    where $\tau_B = \inf\{u \geq s : X_u = B\}$ is the first passage time to $B$.

    Since $p_B$ excludes killed paths while the unrestricted density $p$ includes all paths, we have $p_B(t, x \mid s, y) \leq p(t, x \mid s, y)$ pointwise. Integrating:

    $$
    \int p_B(t, x \mid s, y)\,dx = \mathbb{P}(\tau_B > t \mid X_s = y) < 1
    $$

    The "missing mass" is

    $$
    1 - \int p_B(t, x \mid s, y)\,dx = \mathbb{P}(\tau_B \leq t \mid X_s = y)
    $$

    This is exactly the first-passage probability -- the probability that the diffusion has hit $B$ by time $t$. Probability mass leaks out through the absorbing boundary at a rate determined by the probability flux at $B$:

    $$
    -\frac{d}{dt}\int p_B\,dx = \frac{\sigma^2(B)}{2}\,\partial_x p_B(t, B \mid s, y)
    $$

    In the barrier option context, $1 - \int p_B\,dx$ is the knock-out probability -- the probability that the option has been deactivated by time $t$. The option price involves only the surviving density, which is why barrier options are always worth less than their vanilla counterparts.

??? success "Solution to Exercise 7"
    The **Feynman-Kac formula** states that the solution to

    $$
    \partial_t u + \mathcal{L}u - r(x)\,u + f(t, x) = 0, \quad u(T, x) = g(x)
    $$

    is given by

    $$
    u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(X_s)\,ds}\,g(X_T) + \int_t^T e^{-\int_t^s r(X_u)\,du}\,f(s, X_s)\,ds \;\Big|\; X_t = x\right]
    $$

    Setting $r(x) = r$ (constant) and $f = 0$ (no running payoff), this reduces to

    $$
    u(t, x) = e^{-r(T-t)}\,\mathbb{E}[g(X_T) \mid X_t = x] = e^{-r(T-t)}\int g(y)\,p(T, y \mid t, x)\,dy
    $$

    which is exactly the option pricing formula $V(t, S) = e^{-r(T-t)}\int g(y)\,p(T, y \mid t, S)\,dy$.

    The **Green's function** in this representation is $p(T, y \mid t, S) = G(T, y; t, S)$, the transition density of the (risk-neutral) asset price process.

    This Green's function encodes all information needed for European option pricing because:

    - **Completeness**: Any European payoff $g(S_T)$ is priced by integrating $g$ against $e^{-r(T-t)}G$. Different payoffs are different functions $g$, but the kernel $G$ is universal for the given model.
    - **Model specification**: $G$ fully encodes the dynamics of the underlying -- drift, volatility, and their state dependence -- through the PDE it satisfies.
    - **Discount factor**: The constant $e^{-r(T-t)}$ factors out because $r$ is constant. For stochastic $r$, the discounting would be absorbed into a modified Green's function.
    - **Linearity**: The pricing map $g \mapsto V$ is linear, and $G$ is its integral kernel. Knowing $G$ is equivalent to knowing this entire linear operator, hence all European prices simultaneously.
