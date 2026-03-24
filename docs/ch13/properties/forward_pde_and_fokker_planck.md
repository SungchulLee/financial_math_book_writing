# Forward PDE and Fokker-Planck Equation

The backward Kolmogorov equation propagates option prices backward from the terminal payoff to the present. Its dual, the forward Kolmogorov equation (or Fokker-Planck equation), propagates the transition density forward in time. In the local volatility setting, the forward equation provides the theoretical foundation for Dupire's formula: inverting the Fokker-Planck equation for the local volatility function yields a direct formula in terms of observable call prices. This section develops the forward PDE, derives its key properties, and shows how it connects the local volatility surface to the evolution of the risk-neutral density.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Derive the Fokker-Planck equation for the local volatility diffusion from first principles
    - Explain the duality between forward and backward Kolmogorov equations
    - Show how the Fokker-Planck equation leads to the Dupire formula
    - State the conditions under which the forward PDE has a unique smooth solution
    - Interpret the forward equation as a conservation law for probability

## The Forward Kolmogorov Equation

### Derivation from the SDE

Under the risk-neutral measure $\mathbb{Q}$, the asset price evolves as:

$$
dS_t = (r - q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t^{\mathbb{Q}}
$$

Let $p(S, t \mid S_0, 0)$ denote the transition density: the probability density that $S_t = S$ given $S_0$ at time $0$. For any smooth test function $\varphi(S)$ with compact support, Ito's lemma gives:

$$
d\varphi(S_t) = \left[(r - q)S_t \varphi'(S_t) + \frac{1}{2}\sigma_{\text{loc}}^2(S_t, t) S_t^2 \varphi''(S_t)\right] dt + \sigma_{\text{loc}}(S_t, t) S_t \varphi'(S_t) \, dW_t^{\mathbb{Q}}
$$

Taking expectations and using $\mathbb{E}^{\mathbb{Q}}[\varphi(S_t)] = \int_0^{\infty} \varphi(S) p(S, t) \, dS$:

$$
\frac{d}{dt} \int_0^{\infty} \varphi(S) p(S, t) \, dS = \int_0^{\infty} \left[(r - q)S \varphi'(S) + \frac{1}{2}\sigma_{\text{loc}}^2(S, t) S^2 \varphi''(S)\right] p(S, t) \, dS
$$

Integrating by parts twice on the right-hand side (assuming $p$ and its derivatives vanish sufficiently fast at $S = 0$ and $S = \infty$):

$$
\int_0^{\infty} (r - q)S \varphi'(S) p(S, t) \, dS = -\int_0^{\infty} \varphi(S) \frac{\partial}{\partial S}\bigl[(r - q)S \, p(S, t)\bigr] \, dS
$$

$$
\int_0^{\infty} \frac{1}{2}\sigma_{\text{loc}}^2 S^2 \varphi''(S) p(S, t) \, dS = \int_0^{\infty} \varphi(S) \frac{1}{2}\frac{\partial^2}{\partial S^2}\bigl[\sigma_{\text{loc}}^2(S, t) S^2 p(S, t)\bigr] \, dS
$$

Since this holds for all test functions $\varphi$, the density $p(S, t)$ satisfies:

**Theorem 13.3.1** (Fokker-Planck Equation for Local Volatility).

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}\bigl[(r - q)S \, p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial S^2}\bigl[\sigma_{\text{loc}}^2(S, t) S^2 \, p\bigr]
$$

with initial condition $p(S, 0) = \delta(S - S_0)$. $\square$

### General Form

For a general Ito diffusion $dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t$, the Fokker-Planck equation takes the form:

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\bigl[\mu(x, t) p(x, t)\bigr] + \frac{1}{2}\frac{\partial^2}{\partial x^2}\bigl[\sigma^2(x, t) p(x, t)\bigr]
$$

For the local volatility model with $\mu(S, t) = (r-q)S$ and $\sigma(S, t) = \sigma_{\text{loc}}(S, t) S$, the diffusion coefficient in the Fokker-Planck equation is $a(S, t) = \sigma_{\text{loc}}^2(S, t) S^2$.

## Duality: Forward vs Backward

### The Backward Kolmogorov Equation

The backward Kolmogorov equation governs the evolution of conditional expectations. For $u(S, t) = \mathbb{E}^{\mathbb{Q}}[\varphi(S_T) \mid S_t = S]$:

$$
\frac{\partial u}{\partial t} + (r - q)S \frac{\partial u}{\partial S} + \frac{1}{2}\sigma_{\text{loc}}^2(S, t) S^2 \frac{\partial^2 u}{\partial S^2} = 0
$$

with terminal condition $u(S, T) = \varphi(S)$. The backward equation runs backward in time from $T$ to $t$ and uses derivatives with respect to the **initial** spot $S$.

### Adjoint Relationship

The forward and backward operators are formal adjoints. Define:

$$
\mathcal{L} u = (r - q)S \frac{\partial u}{\partial S} + \frac{1}{2}\sigma_{\text{loc}}^2 S^2 \frac{\partial^2 u}{\partial S^2}
$$

$$
\mathcal{L}^* p = -\frac{\partial}{\partial S}\bigl[(r - q)S \, p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial S^2}\bigl[\sigma_{\text{loc}}^2 S^2 \, p\bigr]
$$

Then for suitable functions $u, p$ vanishing at the boundary:

$$
\int_0^{\infty} u \, \mathcal{L}^* p \, dS = \int_0^{\infty} p \, \mathcal{L} u \, dS
$$

This adjoint relationship is the mathematical expression of the duality between:

- **Backward equation**: Given a fixed terminal payoff, how does the expected value depend on the initial state?
- **Forward equation**: Given a fixed initial state, how does the probability distribution evolve forward?

**Proposition 13.3.1** (Duality Identity).
For the transition density $p(S, T \mid S_0, 0)$ and any smooth function $\varphi$ with compact support:

$$
\int_0^{\infty} \varphi(S) p(S, T \mid S_0, 0) \, dS = u(S_0, 0)
$$

where $u$ solves the backward equation with terminal condition $u(S, T) = \varphi(S)$. $\square$

This identity confirms that both equations encode the same information: one in terms of densities (forward), the other in terms of expected values (backward).

## From Fokker-Planck to Dupire's Formula

### Derivation via Density Integration

The European call price is:

$$
C(K, T) = e^{-rT} \int_K^{\infty} (S - K) p(S, T) \, dS
$$

Differentiating with respect to maturity $T$:

$$
\frac{\partial C}{\partial T} = -rC + e^{-rT} \int_K^{\infty} (S - K) \frac{\partial p}{\partial T}(S, T) \, dS
$$

Substituting the Fokker-Planck equation and integrating by parts (as detailed in the Dupire Formula Derivation section):

$$
\frac{\partial C}{\partial T} = -rC + (r - q)e^{-rT}\int_K^{\infty} S \, p(S, T) \, dS + \frac{1}{2}\sigma_{\text{loc}}^2(K, T) K^2 e^{-rT} p(K, T)
$$

Using the identities:

$$
e^{-rT}\int_K^{\infty} S \, p \, dS = C - KC_K, \quad e^{-rT} p(K, T) = C_{KK}
$$

we obtain:

$$
\frac{\partial C}{\partial T} = -qC - (r - q)KC_K + \frac{1}{2}\sigma_{\text{loc}}^2(K, T) K^2 C_{KK}
$$

Solving for $\sigma_{\text{loc}}^2$:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\partial_T C + (r - q)K \partial_K C + qC}{\frac{1}{2}K^2 \partial_{KK} C}
$$

This is Dupire's formula. The Fokker-Planck equation is the theoretical engine behind it: the forward evolution of the density determines how call prices change with maturity, and inverting this relationship yields the local volatility.

### Forward Equation in Call Price Space

An equivalent and often more useful formulation writes the forward PDE directly in terms of call prices. Defining $U(K, T) = e^{rT} C(K, T)$ (the undiscounted call price), Dupire's forward PDE becomes:

$$
\frac{\partial U}{\partial T} = \frac{1}{2}\sigma_{\text{loc}}^2(K, T) K^2 \frac{\partial^2 U}{\partial K^2} - (r - q)K \frac{\partial U}{\partial K} - qU
$$

with initial condition $U(K, 0) = (S_0 - K)^+$.

This PDE is **forward** in the maturity variable $T$ and has the strike $K$ as its spatial variable. Its advantage over the backward PDE is computational: a single solve sweeps forward through all maturities simultaneously, producing the entire call price surface from a fixed initial spot $S_0$.

!!! tip "Computational Advantage"
    The backward PDE must be solved separately for each option payoff (each strike $K$). The forward PDE solves for **all strikes simultaneously** with a single forward sweep, making it the natural tool for calibrating the entire local volatility surface.

## Probability Conservation and Flux Interpretation

### Conservation Law

The Fokker-Planck equation can be written in conservation form:

$$
\frac{\partial p}{\partial t} + \frac{\partial J}{\partial S} = 0
$$

where the **probability flux** is:

$$
J(S, t) = (r - q)S \, p(S, t) - \frac{1}{2}\frac{\partial}{\partial S}\bigl[\sigma_{\text{loc}}^2(S, t) S^2 \, p(S, t)\bigr]
$$

The conservation form expresses the fact that probability is neither created nor destroyed: the total probability $\int_0^{\infty} p(S, t) \, dS = 1$ is preserved for all $t$.

**Proposition 13.3.2** (Conservation of Probability).
If $p(S, t)$ solves the Fokker-Planck equation with $p(S, 0) = \delta(S - S_0)$ and $J(S, t) \to 0$ as $S \to 0^+$ and $S \to \infty$, then:

$$
\int_0^{\infty} p(S, t) \, dS = 1 \quad \text{for all } t \geq 0
$$

*Proof.* Integrate the conservation law over $(0, \infty)$:

$$
\frac{d}{dt}\int_0^{\infty} p(S, t) \, dS = -\bigl[J(S, t)\bigr]_0^{\infty} = 0
$$

by the boundary conditions. Since $\int_0^{\infty} p(S, 0) \, dS = 1$, the result follows. $\square$

### Physical Interpretation of the Flux

The probability flux $J$ has two components:

- **Drift flux** $(r - q)S \, p$: Probability is transported in the direction of the risk-neutral drift. For $r > q$, probability flows toward higher values of $S$.
- **Diffusion flux** $-\frac{1}{2}\partial_S[\sigma_{\text{loc}}^2 S^2 p]$: Probability spreads out due to volatility. The diffusion flux moves probability from regions of high concentration to regions of low concentration, but the rate depends on the local volatility.

Where $\sigma_{\text{loc}}(S, t)$ is large, the diffusion flux is strong and the density spreads rapidly. Where $\sigma_{\text{loc}}$ is small, the density remains concentrated. The local volatility surface therefore controls the shape of the density at each instant.

## Well-Posedness and Regularity

### Existence and Uniqueness

**Theorem 13.3.2** (Well-Posedness of the Forward PDE).
Suppose $\sigma_{\text{loc}}(S, t)$ satisfies:

1. **Uniform ellipticity**: There exist constants $0 < \lambda \leq \Lambda < \infty$ such that $\lambda \leq \sigma_{\text{loc}}(S, t) \leq \Lambda$ for all $(S, t)$
2. **Holder continuity**: $\sigma_{\text{loc}}$ is Holder continuous in both variables

Then the Fokker-Planck equation with initial condition $p(S, 0) = \delta(S - S_0)$ admits a unique classical solution $p \in C^{2,1}((0, \infty) \times (0, T^*])$ satisfying $p(S, t) > 0$ for all $S > 0$, $t > 0$.

The proof relies on the theory of parabolic PDEs (Friedman, 1964) and the parametrix method for constructing the fundamental solution. The strict positivity of $p$ follows from the strong maximum principle for parabolic equations.

### Smoothness of the Density

Under the conditions of Theorem 13.3.2, the transition density $p(S, t)$ has several important properties:

1. **Smoothness**: $p$ is infinitely differentiable in $S$ for $t > 0$, even though the initial condition is a Dirac delta
2. **Gaussian bounds**: There exist constants $c, C > 0$ such that

    $$
    \frac{c}{S\sqrt{t}} \exp\left(-\frac{C(\log S/S_0)^2}{t}\right) \leq p(S, t) \leq \frac{C}{S\sqrt{t}} \exp\left(-\frac{c(\log S/S_0)^2}{t}\right)
    $$

3. **Short-time behavior**: As $t \to 0^+$, the density concentrates around $S_0$ and converges to $\delta(S - S_0)$ in the distributional sense

These bounds ensure that the Dupire formula is well-defined: the denominator $C_{KK} = e^{-rT} p(K, T) > 0$ for all $K > 0$ and $T > 0$.

## Forward Equation in Log Coordinates

### Change of Variable

The transformation $x = \log S$ simplifies the Fokker-Planck equation. Under the SDE for $x_t = \log S_t$:

$$
dx_t = \left(r - q - \frac{1}{2}\sigma_{\text{loc}}^2(e^{x_t}, t)\right) dt + \sigma_{\text{loc}}(e^{x_t}, t) \, dW_t^{\mathbb{Q}}
$$

the transition density $\tilde{p}(x, t) = p(e^x, t) e^x$ satisfies:

$$
\frac{\partial \tilde{p}}{\partial t} = -\frac{\partial}{\partial x}\left[\left(r - q - \frac{1}{2}\tilde{\sigma}^2(x, t)\right)\tilde{p}\right] + \frac{1}{2}\frac{\partial^2}{\partial x^2}\bigl[\tilde{\sigma}^2(x, t) \tilde{p}\bigr]
$$

where $\tilde{\sigma}(x, t) = \sigma_{\text{loc}}(e^x, t)$. In log coordinates, the diffusion coefficient no longer depends on the price level through $S^2$, which improves the numerical conditioning of the PDE.

### Constant Volatility Case

When $\sigma_{\text{loc}}(S, t) = \sigma$ is constant, the density in log coordinates is Gaussian:

$$
\tilde{p}(x, t) = \frac{1}{\sigma\sqrt{2\pi t}} \exp\left(-\frac{\bigl(x - x_0 - (r - q - \frac{1}{2}\sigma^2)t\bigr)^2}{2\sigma^2 t}\right)
$$

where $x_0 = \log S_0$. This recovers the Black-Scholes lognormal distribution. The forward PDE reduces to the heat equation with drift, confirming the Gaussian transition density.

## Worked Example

??? example "Density Evolution with Piecewise Constant Local Volatility"

    **Setup.** Consider a simple local volatility function that depends only on the price level:

    $$
    \sigma_{\text{loc}}(S, t) = \begin{cases} 0.30 & \text{if } S \leq 100 \\ 0.15 & \text{if } S > 100 \end{cases}
    $$

    with $r = 0.03$, $q = 0$, $S_0 = 100$.

    The Fokker-Planck equation has a higher diffusion coefficient below $S = 100$ and a lower coefficient above. This means:

    - Probability mass below $S_0 = 100$ spreads out faster (higher vol region)
    - Probability mass above $S_0 = 100$ remains more concentrated (lower vol region)

    The resulting density $p(S, T)$ is **negatively skewed**: the left tail is fatter than the right tail. This produces an implied volatility surface with a downward-sloping skew, consistent with the empirical equity skew.

    The Dupire formula applied to call prices generated by this model recovers the piecewise constant $\sigma_{\text{loc}}$:

    - For $K < 100$: $\sigma_{\text{loc}}^2(K, T) = 0.09$, yielding $\sigma_{\text{loc}} = 0.30$
    - For $K > 100$: $\sigma_{\text{loc}}^2(K, T) = 0.0225$, yielding $\sigma_{\text{loc}} = 0.15$

    This confirms the consistency of the forward PDE and Dupire inversion.

## Connection to Other Results

### Gyongy's Theorem

The Fokker-Planck equation plays a central role in Gyongy's theorem. For any stochastic volatility model, the marginal density $p(S, t)$ satisfies a Fokker-Planck equation with effective diffusion coefficient $\mathbb{E}[\sigma_t^2 S_t^2 \mid S_t = S]$. The Markovian projection produces a local volatility model whose Fokker-Planck equation has the same solution -- hence the same marginal densities.

### Dupire Formula as Inversion

The Dupire formula is the **algebraic inversion** of the Fokker-Planck equation: given the density $p(S, T) = e^{rT} C_{KK}(S, T)$ and its time evolution $\partial_T p$ (encoded in $C_T$), one solves for the diffusion coefficient $\sigma_{\text{loc}}^2 S^2$. The forward PDE determines $p$; inverting for $\sigma_{\text{loc}}^2$ recovers the Dupire formula.

### Transition to Numerical Methods

In practice, the forward PDE is solved numerically using finite difference methods. The PDE is discretized on a $(S, T)$ grid, and the density (or equivalently, call prices) is propagated forward in time using Crank-Nicolson or implicit Euler schemes. The forward formulation is especially efficient for calibration, since a single forward sweep produces call prices at all strikes simultaneously.

## Summary

The Fokker-Planck equation is the forward counterpart of the backward pricing PDE:

1. **Forward evolution**: The Fokker-Planck equation $\partial_t p = -\partial_S[\mu p] + \frac{1}{2}\partial_{SS}[a \, p]$ propagates the transition density forward from the initial Dirac delta.
2. **Adjoint duality**: The forward operator $\mathcal{L}^*$ is the formal adjoint of the backward operator $\mathcal{L}$, encoding the same information in dual form.
3. **Foundation for Dupire**: Integrating the Fokker-Planck equation against the call payoff and inverting yields the Dupire formula for local volatility.
4. **Conservation law**: The forward PDE preserves total probability and admits a flux interpretation with drift and diffusion components.
5. **Computational efficiency**: The forward PDE solves for all strikes simultaneously, making it the natural tool for calibrating the local volatility surface.
6. **Well-posedness**: Under uniform ellipticity and regularity conditions on $\sigma_{\text{loc}}$, the forward PDE has a unique, strictly positive, smooth solution.

---

## Exercises

**Exercise 1.** Starting from the SDE $dS_t = (r - q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t$, carry out the integration-by-parts steps to derive the Fokker-Planck equation. Specifically, show that:

$$
\int_0^{\infty} \frac{1}{2}\sigma_{\text{loc}}^2 S^2 \varphi''(S) p(S, t) \, dS = \int_0^{\infty} \varphi(S) \frac{1}{2}\frac{\partial^2}{\partial S^2}[\sigma_{\text{loc}}^2 S^2 p] \, dS
$$

State the boundary conditions on $p$ required for the boundary terms to vanish.

---

**Exercise 2.** Write the Fokker-Planck equation for the log-coordinate $x = \log S$, with density $\tilde{p}(x, t) = p(e^x, t)e^x$. Verify that when $\sigma_{\text{loc}}$ is constant, the solution is a Gaussian density with mean $x_0 + (r - q - \sigma^2/2)t$ and variance $\sigma^2 t$.

---

**Exercise 3.** The probability flux is $J(S, t) = (r - q)S p - \frac{1}{2}\partial_S[\sigma_{\text{loc}}^2 S^2 p]$. Consider a piecewise constant local volatility: $\sigma_{\text{loc}} = 0.30$ for $S < 100$ and $\sigma_{\text{loc}} = 0.15$ for $S > 100$. Qualitatively describe the shape of the density $p(S, T)$ for $T = 1$ year. Which region has a fatter tail, and why?

---

**Exercise 4.** Prove the conservation of probability: starting from $\partial_t p + \partial_S J = 0$, show that $\int_0^{\infty} p(S, t) \, dS = 1$ for all $t \geq 0$. What physical assumptions are needed at the boundaries $S = 0$ and $S = \infty$?

---

**Exercise 5.** Explain the duality between the forward and backward Kolmogorov equations. If $u(S, t)$ solves the backward equation with terminal condition $u(S, T) = \varphi(S)$ and $p(S, T \mid S_0, 0)$ solves the forward equation with initial condition $p(S, 0) = \delta(S - S_0)$, show that:

$$
\int_0^{\infty} \varphi(S) p(S, T \mid S_0, 0) \, dS = u(S_0, 0)
$$

---

**Exercise 6.** The forward PDE in call price space is:

$$
\frac{\partial U}{\partial T} = \frac{1}{2}\sigma_{\text{loc}}^2(K, T) K^2 \frac{\partial^2 U}{\partial K^2} - (r - q)K \frac{\partial U}{\partial K} - qU
$$

with $U(K, 0) = (S_0 - K)^+$. Explain why this formulation computes call prices at all strikes simultaneously in a single forward sweep. Compare the computational cost with the backward PDE approach for pricing vanilla options at $N$ different strikes.

---

**Exercise 7.** Under the Gaussian bounds for the transition density (Theorem 13.3.2), show that $C_{KK} = e^{-rT} p(K, T) > 0$ for all $K > 0$ and $T > 0$. Explain why this strict positivity is essential for the well-definedness of Dupire's formula.
