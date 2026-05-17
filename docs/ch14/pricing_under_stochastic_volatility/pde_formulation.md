# PDE Formulation

Stochastic volatility models also admit a **partial differential equation (PDE)** formulation for option pricing. The PDE perspective is useful for theoretical analysis, boundary conditions, American options, and products not well-suited to Fourier methods.

---

## Risk-Neutral Pricing PDE

### Derivation from No-Arbitrage

Let $V(t, S, v)$ be the price at time $t$ of a European option when the spot price is $S$ and instantaneous variance is $v$.

Recall (see [§ BS PDE Derivation — Replication](../../ch06/bs_pde_derivation/replication.md), [§ Delta Hedging](../../ch06/bs_pde_derivation/delta_hedging.md)): by delta-vega hedging arguments (now with a volatility-traded asset to span both shocks) or by the Feynman–Kac theorem, $V$ satisfies

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

This form has constant coefficients in the second-order $x$ terms, simplifying numerical treatment (the same affine-in-$v$ structure underlying [§ Affine Structure](../the_heston_model/affine_structure.md)).

---

## Boundary Conditions

### In Asset Price (S)

**As $S \to 0$:**

- Call: $V \to 0$
- Put: $V \to Ke^{-r(T-t)}$

**As $S \to \infty$:**

- Call: $V \sim Se^{-q(T-t)} - Ke^{-r(T-t)}$
- Put: $V \to 0$

### In Variance (v)

**As $v \to 0$:**

The PDE degenerates (diffusion coefficient vanishes). Recall (see [§ Feller Condition and Boundary Behavior](../the_heston_model/feller_condition_and_boundary_behavior.md)): if $2\kappa\theta \geq \xi^2$ the boundary is unattainable and no explicit condition is needed; otherwise it is attainable and behavior (e.g. smooth continuation) must be specified.

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

Recall (see [§ Finite Difference Methods](../../ch08/fdm/finite_difference_methods.md)): central differences give $\partial_x V$, $\partial_{xx} V$, and the four-point diagonal stencil gives the cross term

$$
\frac{\partial^2 V}{\partial x \partial v} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x \Delta v}.
$$

### Time Stepping

Recall (see [§ Explicit / Implicit / Crank–Nicolson Schemes](../../ch08/fdm/explicit_implicit_crank_nicolson_schemes.md)): explicit is CFL-limited, implicit is unconditionally stable, Crank–Nicolson is second-order but can oscillate. For 2D SV PDEs, ADI splitting is the standard choice.

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

---

## Exercises

**Exercise 1.** Starting from the Heston SDE system under $\mathbb{Q}$, apply the Feynman-Kac theorem to derive the pricing PDE for a European option $V(t, S, v)$. Identify each term in the PDE and explain its financial interpretation (e.g., which terms correspond to the asset drift, variance mean reversion, the hedging cost, etc.).

??? success "Solution to Exercise 1"
    Under $\mathbb{Q}$, the Heston SDE system is

    $$
    dS_t = (r-q)S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^S
    $$

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^v
    $$

    with $d\langle W^S, W^v\rangle_t = \rho\,dt$. By the Feynman-Kac theorem, the price $V(t,S,v) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S, v_t = v]$ satisfies

    $$
    \frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0, \qquad V(T, S, v) = \Phi(S)
    $$

    where $\mathcal{L}$ is the infinitesimal generator of $(S_t, v_t)$. Applying Ito's lemma to $V(t, S_t, v_t)$ and collecting terms:

    $$
    \frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi vS\frac{\partial^2 V}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} - rV = 0
    $$

    **Financial interpretation of each term:**

    - $(r-q)S\frac{\partial V}{\partial S}$: Risk-neutral drift of the asset (growth at $r-q$ after dividend yield)
    - $\kappa(\theta - v)\frac{\partial V}{\partial v}$: Mean reversion of variance toward $\theta$ at speed $\kappa$
    - $\frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2}$: Gamma effect from asset diffusion (convexity in $S$)
    - $\rho\xi vS\frac{\partial^2 V}{\partial S\partial v}$: Cross-gamma from correlation between asset and variance shocks
    - $\frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2}$: Vol-of-vol effect (convexity in $v$)
    - $-rV$: Discounting at the risk-free rate

---

**Exercise 2.** Perform the log-price transformation $x = \log S$ on the Heston PDE. Show explicitly how the terms $S\frac{\partial V}{\partial S}$ and $S^2\frac{\partial^2 V}{\partial S^2}$ transform. Verify that the resulting PDE has coefficients that are at most linear in $v$ (confirming the affine structure).

??? success "Solution to Exercise 2"
    Set $x = \log S$, so $S = e^x$. Let $U(t, x, v) = V(t, e^x, v)$. By the chain rule:

    $$
    \frac{\partial V}{\partial S} = \frac{\partial U}{\partial x}\cdot\frac{1}{S}, \qquad S\frac{\partial V}{\partial S} = \frac{\partial U}{\partial x}
    $$

    For the second derivative:

    $$
    \frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\!\left(\frac{1}{S}\frac{\partial U}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial U}{\partial x} + \frac{1}{S^2}\frac{\partial^2 U}{\partial x^2}
    $$

    so

    $$
    S^2\frac{\partial^2 V}{\partial S^2} = \frac{\partial^2 U}{\partial x^2} - \frac{\partial U}{\partial x}
    $$

    Substituting into the Heston PDE:

    $$
    \frac{\partial U}{\partial t} + (r-q)\frac{\partial U}{\partial x} + \kappa(\theta - v)\frac{\partial U}{\partial v} + \frac{v}{2}\!\left(\frac{\partial^2 U}{\partial x^2} - \frac{\partial U}{\partial x}\right) + \rho\xi v\frac{\partial^2 U}{\partial x\partial v} + \frac{\xi^2 v}{2}\frac{\partial^2 U}{\partial v^2} - rU = 0
    $$

    Combining the first-order $x$ terms:

    $$
    \frac{\partial U}{\partial t} + \left(r - q - \frac{v}{2}\right)\frac{\partial U}{\partial x} + \kappa(\theta - v)\frac{\partial U}{\partial v} + \frac{v}{2}\frac{\partial^2 U}{\partial x^2} + \rho\xi v\frac{\partial^2 U}{\partial x\partial v} + \frac{\xi^2 v}{2}\frac{\partial^2 U}{\partial v^2} - rU = 0
    $$

    All coefficients are either constant or linear in $v$: the $\frac{\partial U}{\partial x}$ coefficient is $(r-q-v/2)$, the $\frac{\partial^2 U}{\partial x^2}$ coefficient is $v/2$, the cross-derivative coefficient is $\rho\xi v$, and the $\frac{\partial^2 U}{\partial v^2}$ coefficient is $\xi^2 v/2$. This confirms the affine structure in $v$.

---

**Exercise 3.** At the boundary $v = 0$, the Heston PDE degenerates because the diffusion coefficients involving $v$ vanish. Write the limiting PDE as $v \to 0$ and show it reduces to

$$
\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

Explain why this is a first-order PDE in $v$ (no second-order $v$ derivatives) and what this means for the numerical treatment of the $v = 0$ boundary.

??? success "Solution to Exercise 3"
    In the Heston PDE (in original $S$ coordinates), the terms involving $v$ as a multiplicative factor are:

    $$
    \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi vS\frac{\partial^2 V}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2}
    $$

    As $v \to 0$, all three terms vanish. The drift term $\kappa(\theta - v)\frac{\partial V}{\partial v} \to \kappa\theta\frac{\partial V}{\partial v}$, which remains nonzero (since $\theta > 0$). The surviving terms give the limiting PDE:

    $$
    \frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
    $$

    This is a **first-order PDE in $v$** because there are no second-order derivatives in $v$ (or mixed derivatives). The $\kappa\theta\frac{\partial V}{\partial v}$ term acts as a transport term pushing variance away from zero (since $\kappa\theta > 0$, it advects in the positive $v$ direction).

    **Numerical implications:** Because the PDE degenerates at $v = 0$, standard second-order finite difference stencils cannot be applied at that boundary. Instead, we use the first-order limiting PDE as a boundary condition. If the Feller condition $2\kappa\theta \geq \xi^2$ holds, the variance process never reaches zero, so the boundary is unattainable and the limiting PDE is only needed formally. If the Feller condition is violated, variance can reach zero, and the first-order boundary PDE must be imposed explicitly, requiring a one-sided (upwind) discretization in the $v$-direction at $v = 0$.

---

**Exercise 4.** For a finite difference grid with $N_x = 200$ points in the log-price direction and $N_v = 100$ points in the variance direction, compute the total number of unknowns per time step. If $N_t = 500$ time steps are used, estimate the total number of floating-point operations for: (a) an explicit scheme ($O(N_x \cdot N_v)$ per step); (b) an implicit scheme requiring solution of a banded linear system. Compare with the cost of a Fourier method using $N_u = 256$ integration points.

??? success "Solution to Exercise 4"
    The grid has $N_x = 200$ points in log-price and $N_v = 100$ points in variance, giving $N_x \cdot N_v = 20{,}000$ unknowns per time step.

    **(a) Explicit scheme:** Each time step requires $O(N_x \cdot N_v)$ operations (one stencil evaluation per grid point). Over $N_t = 500$ steps:

    $$
    \text{Total} = O(N_x \cdot N_v \cdot N_t) = O(200 \times 100 \times 500) = O(10^7)
    $$

    **(b) Implicit scheme:** A fully implicit scheme requires solving a linear system of size $20{,}000 \times 20{,}000$ per time step. Using ADI splitting, each sub-step involves tridiagonal solves: $N_v$ tridiagonal systems of size $N_x$ (cost $O(N_x)$ each) plus $N_x$ tridiagonal systems of size $N_v$. Per time step: $O(N_v \cdot N_x + N_x \cdot N_v) = O(2 N_x N_v)$. Over $N_t$ steps:

    $$
    \text{Total (ADI)} = O(2 N_x N_v N_t) = O(2 \times 10^7)
    $$

    Without ADI (direct sparse solve), the cost is higher: $O(N_t \cdot (N_x N_v)^{3/2})$ for a banded system, which is $O(500 \cdot 20000^{1.5}) \approx O(1.4 \times 10^9)$.

    **(c) Fourier method:** With $N_u = 256$ integration points, each requiring one CF evaluation, the cost is $O(256)$ for a single strike. For $N$ strikes via FFT: $O(N_u \log N_u) = O(256 \times 8) \approx O(2000)$.

    The Fourier method is roughly 4--5 orders of magnitude faster than PDE methods for European option pricing.

---

**Exercise 5.** The mixed derivative $\frac{\partial^2 V}{\partial x \partial v}$ is approximated by the four-point stencil

$$
\frac{\partial^2 V}{\partial x \partial v} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x \Delta v}
$$

Show that this stencil has truncation error $O((\Delta x)^2 + (\Delta v)^2)$. When $\rho$ is close to $\pm 1$, explain why the coefficient of the mixed derivative becomes large and can cause stability issues. How does the coordinate transformation $y = x - \rho v$ help?

??? success "Solution to Exercise 5"
    **Truncation error:** Taylor-expand $V_{i\pm 1, j\pm 1}$ around $(x_i, v_j)$:

    $$
    V_{i+1,j+1} = V + \Delta x\,V_x + \Delta v\,V_v + \frac{(\Delta x)^2}{2}V_{xx} + \Delta x\Delta v\,V_{xv} + \frac{(\Delta v)^2}{2}V_{vv} + \cdots
    $$

    Computing the stencil combination:

    $$
    V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1} = 4\Delta x\Delta v\,V_{xv} + O((\Delta x)^3\Delta v + \Delta x(\Delta v)^3)
    $$

    Dividing by $4\Delta x\Delta v$ gives

    $$
    \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x\Delta v} = V_{xv} + O((\Delta x)^2 + (\Delta v)^2)
    $$

    confirming second-order accuracy.

    **Stability when $|\rho| \approx 1$:** The coefficient of the mixed derivative in the PDE is $\rho\xi v$. When $|\rho|$ is close to 1, this coefficient becomes large relative to the pure second derivatives. The four-point stencil connects diagonal grid neighbors, and the resulting finite difference matrix can lose diagonal dominance, producing negative coefficients in the stencil. This can cause non-physical oscillations or instability, particularly in explicit schemes.

    **Coordinate transformation:** The substitution $y = x - \rho v$, $w = v$ transforms the cross-derivative term. Since $\frac{\partial}{\partial x} = \frac{\partial}{\partial y}$ and $\frac{\partial}{\partial v} = -\rho\frac{\partial}{\partial y} + \frac{\partial}{\partial w}$, the mixed derivative $\rho\xi v\frac{\partial^2 V}{\partial x\partial v}$ is absorbed into pure second-order terms in $y$ and $w$, eliminating or reducing the mixed derivative coefficient. This restores diagonal dominance and standard ADI applicability.

---

**Exercise 6.** For an American put option under Heston dynamics, the free boundary problem requires

$$
V(t, S, v) \geq (K - S)^+ \quad \text{for all } (t, S, v)
$$

Explain why the early exercise boundary $S^*(t, v)$ is now a surface (function of both $t$ and $v$) rather than a curve as in Black-Scholes. How does increasing $v$ affect $S^*(t, v)$? (Hint: consider the option holder's incentive to exercise when volatility is high vs. low.)

??? success "Solution to Exercise 6"
    In Black-Scholes, the early exercise boundary $S^*(t)$ is a function of time only because the volatility is deterministic. Under Heston dynamics, the instantaneous variance $v$ is stochastic and affects the option value, so the exercise decision depends on $v$ as well. The boundary becomes a surface $S^*(t, v)$ in the $(t, v)$ plane.

    **Effect of increasing $v$ on $S^*(t,v)$:** Consider an American put holder at time $t$ with stock price $S$ and current variance $v$. The value of holding (continuing) the option increases with $v$, because higher variance means a greater chance of the stock falling further, increasing the expected payoff. The exercise value $(K - S)^+$ is independent of $v$. Therefore, for higher $v$, the holder demands a lower stock price before exercising (continuation is more valuable). This means $S^*(t, v)$ is decreasing in $v$: as variance increases, the critical stock price below which exercise occurs drops.

    Intuitively, when volatility is high, there is more "optionality" to benefit from further price moves, making early exercise less attractive. When volatility is very low, the option behaves nearly like an intrinsic-value instrument, and early exercise becomes optimal at stock prices closer to the strike.

---

**Exercise 7.** Compare PDE and Fourier methods for the following pricing problems, and recommend the better approach for each:

(a) Pricing ATM European calls at 50 different strikes for calibration.

(b) Pricing an American put with $T = 1$ year under Heston dynamics.

(c) Computing delta and gamma of a European call.

(d) Pricing a down-and-out barrier call with barrier at $B = 0.8 S_0$.

Justify each recommendation based on computational cost, accuracy, and ease of implementation.

??? success "Solution to Exercise 7"
    **(a) Pricing ATM European calls at 50 different strikes for calibration:** **Fourier methods (COS or Carr-Madan FFT)** are strongly preferred. The FFT computes prices at all strikes simultaneously in $O(N\log N)$, and COS achieves $O(N \cdot N_K)$ where $N_K = 50$ is the number of strikes. A PDE solve gives one price surface but costs $O(N_x \cdot N_v \cdot N_t) \sim O(10^7)$, and calibration requires many such solves (iterating over parameters). Fourier methods are orders of magnitude faster for this task.

    **(b) Pricing an American put with $T = 1$ year under Heston dynamics:** **PDE methods** are preferred. The early exercise constraint $V \geq (K-S)^+$ is naturally handled via projected SOR or penalty methods within the PDE framework. Fourier methods are designed for European payoffs and do not directly accommodate the free boundary. While extensions exist (e.g., COS for Bermudan options), PDE methods remain the standard, robust approach.

    **(c) Computing delta and gamma of a European call:** **PDE methods** have a slight edge, since finite differences on the $(S, v)$ grid provide Greeks directly as by-products (e.g., $\Delta \approx \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta S}$, $\Gamma \approx \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{(\Delta S)^2}$). However, **Fourier methods** can also deliver Greeks by differentiating the pricing integral or using finite difference bumps on the input parameters. For a single option, either method works; for calibration with Greeks, Fourier is faster.

    **(d) Pricing a down-and-out barrier call with barrier at $B = 0.8\,S_0$:** **PDE methods** are preferred. The barrier condition $V(t, B, v) = 0$ is implemented as a Dirichlet boundary condition on the PDE grid, which is straightforward. Fourier methods require either image-charge techniques or conditional CFs that are model-specific and less general. PDE methods handle barriers naturally and accurately (especially with grid points placed at the barrier).
