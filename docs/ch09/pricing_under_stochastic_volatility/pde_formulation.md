# PDE Formulation

Stochastic volatility models also admit a **partial differential equation (PDE)** formulation for option pricing. The PDE perspective is useful for theoretical analysis, boundary conditions, American options, and products not well-suited to Fourier methods.

---

## Risk-Neutral Pricing PDE

### Derivation from No-Arbitrage

Let $V(t, S, v)$ be the price at time $t$ of a European option when the spot price is $S$ and instantaneous variance is $v$.

By delta-vega hedging arguments (in the presence of a volatility-traded asset) or by the Feynman–Kac theorem, $V$ satisfies:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0
$$

with terminal condition:

$$
V(T, S, v) = \Phi(S)
$$

where $\Phi(S)$ is the payoff (e.g., $(S-K)^+$ for a call).

### The Infinitesimal Generator

For a general two-factor stochastic volatility model:

$$
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^S \\
dv_t &= a(v_t)\,dt + b(v_t)\,dW_t^v \\
d\langle W^S, W^v \rangle_t &= \rho\,dt
\end{aligned}
$$

the generator is:

$$
\mathcal{L}V = (r-q)S\frac{\partial V}{\partial S} + a(v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho b(v)S\sqrt{v}\frac{\partial^2 V}{\partial S \partial v} + \frac{1}{2}b(v)^2\frac{\partial^2 V}{\partial v^2}
$$

---

## Heston PDE

### Specific Form

For the Heston model with $a(v) = \kappa(\theta - v)$ and $b(v) = \xi\sqrt{v}$:

$$
\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi vS\frac{\partial^2 V}{\partial S \partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} - rV = 0
$$

### Log-Price Transformation

Setting $x = \log S$:

$$
\frac{\partial V}{\partial t} + \left(r-q-\frac{v}{2}\right)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} - rV = 0
$$

This form has constant coefficients in the second-order $x$ terms, simplifying numerical treatment.

---

## Boundary Conditions

### In Asset Price ($S$)

**As $S \to 0$:**
- Call: $V \to 0$
- Put: $V \to Ke^{-r(T-t)}$

**As $S \to \infty$:**
- Call: $V \sim Se^{-q(T-t)} - Ke^{-r(T-t)}$
- Put: $V \to 0$

### In Variance ($v$)

**As $v \to 0$:**

The PDE degenerates (diffusion coefficient vanishes). Treatment depends on the Feller condition:

- **Feller satisfied ($2\kappa\theta \geq \xi^2$):** Boundary is unattainable; no explicit condition needed
- **Feller violated:** Boundary is attainable; specify behavior (typically: smooth continuation)

A common approach: use the **limiting PDE** as $v \to 0$:

$$
\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

**As $v \to \infty$:**

Option value becomes approximately linear in $\sqrt{v}$. Common choices:
- Neumann: $\frac{\partial V}{\partial v} = 0$
- Linear extrapolation
- Far boundary placed sufficiently far

### Terminal Condition

$$
V(T, S, v) = \Phi(S)
$$

For a European call: $\Phi(S) = (S - K)^+$

---

## Numerical Methods

### Finite Difference Discretization

Discretize the $(x, v)$ domain on a grid:

$$
x_i = x_{\min} + i\Delta x, \quad v_j = j\Delta v, \quad t_n = n\Delta t
$$

Denote $V_{i,j}^n \approx V(t_n, x_i, v_j)$.

### Standard Finite Differences

**First derivatives:**
$$
\frac{\partial V}{\partial x} \approx \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta x} \quad \text{(central)}
$$

**Second derivatives:**
$$
\frac{\partial^2 V}{\partial x^2} \approx \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{(\Delta x)^2}
$$

**Mixed derivative:**
$$
\frac{\partial^2 V}{\partial x \partial v} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x \Delta v}
$$

### Time Stepping

**Explicit scheme:** Unstable for fine grids; CFL condition required

**Implicit scheme:** Unconditionally stable but requires solving linear systems

**Crank–Nicolson:** Second-order in time, but can produce oscillations

**ADI (Alternating Direction Implicit):** Preferred for 2D problems

---

## ADI Schemes

### Douglas–Rachford ADI

Split the operator: $\mathcal{L} = \mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv}$

**Step 1 (implicit in $x$):**
$$
\frac{V^* - V^n}{\Delta t} + \mathcal{L}_x V^* + \mathcal{L}_v V^n + \mathcal{L}_{xv} V^n = rV^n
$$

**Step 2 (implicit in $v$):**
$$
\frac{V^{n+1} - V^*}{\Delta t} + \mathcal{L}_v(V^{n+1} - V^n) = 0
$$

Each step involves only tridiagonal systems (fast to solve).

### Hundsdorfer–Verwer ADI

More sophisticated splitting with better stability:

$$
Y_0 = V^n + \Delta t \mathcal{L}V^n
$$
$$
Y_1 = Y_0 + \theta\Delta t(\mathcal{L}_1 Y_1 - \mathcal{L}_1 V^n)
$$
$$
Y_2 = Y_1 + \theta\Delta t(\mathcal{L}_2 Y_2 - \mathcal{L}_2 V^n)
$$
$$
\tilde{Y}_0 = Y_0 + \frac{1}{2}\Delta t(\mathcal{L}Y_2 - \mathcal{L}V^n)
$$
$$
\tilde{Y}_1 = \tilde{Y}_0 + \theta\Delta t(\mathcal{L}_1\tilde{Y}_1 - \mathcal{L}_1 Y_2)
$$
$$
V^{n+1} = \tilde{Y}_1 + \theta\Delta t(\mathcal{L}_2 V^{n+1} - \mathcal{L}_2 Y_2)
$$

with $\theta = 1/2$ for second-order accuracy.

### Mixed Derivative Treatment

The cross-derivative $\frac{\partial^2 V}{\partial x \partial v}$ complicates ADI:

**Option 1:** Include in explicit part (may limit stability)

**Option 2:** Craig–Sneyd scheme (modified ADI for mixed terms)

**Option 3:** Coordinate transformation to remove mixed term

---

## Coordinate Transformations

### Removing the Mixed Derivative

The transformation:

$$
y = x - \rho v, \quad w = v
$$

can simplify the PDE by reducing the mixed derivative coefficient.

### Non-Uniform Grids

Concentrate grid points where $V$ varies most:
- Near the strike ($S \approx K$)
- Near $v = 0$ (boundary layer)
- Near $v = v_0$ (current variance)

Common transformations:
$$
\tilde{v} = \sinh^{-1}(\alpha v)
$$

---

## American Options

### Free Boundary Problem

American options require:

$$
V(t, S, v) \geq \Phi(S) \quad \text{for all } (t, S, v)
$$

The **early exercise boundary** $S^*(t, v)$ separates continuation and exercise regions.

### Complementarity Formulation

$$
\min\left(\frac{\partial V}{\partial t} + \mathcal{L}V - rV, \; V - \Phi\right) = 0
$$

### Numerical Approaches

**Projected SOR:** After each time step, enforce $V \geq \Phi$

**Penalty method:** Replace constraint with penalty term

**Policy iteration:** Iterate between solving PDE and updating exercise boundary

---

## When PDE Methods Are Preferred

### Advantages

1. **American options:** Natural handling of early exercise
2. **Barriers:** Boundary conditions straightforward
3. **No moment restrictions:** Unlike Fourier methods
4. **Greeks:** Finite differences give Greeks directly
5. **Path-dependent (some):** Certain structures fit PDE framework

### Disadvantages

1. **Computational cost:** $O(N_x \cdot N_v \cdot N_t)$ per price
2. **Curse of dimensionality:** Multi-asset/multi-factor is expensive
3. **Boundary treatment:** Requires care at $v = 0$ and $v = \infty$
4. **Implementation complexity:** ADI schemes are intricate

### Comparison with Fourier Methods

| Aspect | PDE | Fourier |
|--------|-----|---------|
| European vanilla | Slower | Faster |
| American | Natural | Difficult |
| Barriers | Natural | Difficult |
| Greeks | Direct (FD) | Differentiation of CF |
| Calibration | Slow | Fast |
| Implementation | Complex | Moderate |

---

## Key Takeaways

- Stochastic volatility pricing can be expressed as a two-dimensional PDE
- The Heston PDE involves mixed derivatives requiring careful numerical treatment
- Boundary conditions at $v = 0$ depend on the Feller condition
- ADI schemes (Douglas–Rachford, Hundsdorfer–Verwer) are standard for efficiency
- PDE methods excel for American options and barriers
- For European calibration, Fourier methods are usually preferred

---

## Further Reading

- Wilmott, P. (2006). *Paul Wilmott on Quantitative Finance*, 2nd ed. Wiley.
- in 't Hout, K. & Foulon, S. (2010). *ADI finite difference schemes for option pricing in the Heston model with correlation*. International Journal of Numerical Analysis and Modeling.
- Ikonen, S. & Toivanen, J. (2008). *Efficient numerical methods for pricing American options under stochastic volatility*. Numerical Methods for Partial Differential Equations.
- Haentjens, T. & in 't Hout, K. (2012). *Alternating direction implicit finite difference schemes for the Heston–Hull–White PDE*. Journal of Computational Finance.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
