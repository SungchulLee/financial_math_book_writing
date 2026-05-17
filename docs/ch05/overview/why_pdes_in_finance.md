# Why PDEs in Finance

Partial differential equations arise naturally in quantitative finance whenever we ask: **what is the fair price of a derivative today, given uncertainty about the future?** The answer turns out to satisfy a deterministic PDE, even though the underlying asset follows a random process. This remarkable fact is the foundation of modern derivatives pricing.

---

## The Core Insight

Consider a derivative with payoff $g(S_T)$ at maturity $T$. Under the risk-neutral measure, its time-$t$ price is:

$$
V(t, S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]
$$

Recall (see [§ The SDE–PDE Bridge](sde_pde_bridge.md)): such a discounted expectation of a Markovian diffusion satisfies a parabolic PDE — the Feynman–Kac equation $\partial_t u + \mathcal{L}u - ru = 0$. The remarkable financial consequence: **a deterministic PDE captures the present value of a random future payoff**.

!!! quote "The Central Principle"
    Every pricing problem for a Markovian underlying reduces to solving a PDE. The drift and volatility of the underlying determine the PDE coefficients; the payoff sets the terminal condition; discounting enters as a zeroth-order term.

---

## The Three-Term Anatomy of a Pricing PDE

Recall (see [§ The SDE–PDE Bridge](sde_pde_bridge.md)): the generator $\mathcal{L}$ packages the drift and diffusion of the underlying into a single first-and-second-order spatial operator. Interpreted financially, the pricing PDE $\partial_t V + \mathcal{L}V - rV = 0$ decomposes into three meaningful terms:

- **Drift** contributes a first-order (transport) term — directional motion of the underlying
- **Volatility** contributes a second-order (diffusion) term — random fluctuation
- **Discounting** contributes a zeroth-order (decay) term — time value of money

This three-term structure — transport, diffusion, decay — is the universal anatomy of every financial pricing PDE.

---

## Three Approaches to Derivative Pricing

Given the price $V(t,S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]$, there are three computational strategies.

### Approach 1: PDE (Finite Differences)

Solve the PDE on a discretized grid in $(t, S)$ space, marching backward from the terminal condition.

**Procedure:**

1. Discretize the domain: grid points $(t_n, S_j)$
2. Apply a finite difference scheme (explicit, implicit, or Crank-Nicolson)
3. March backward from $V(T, S_j) = g(S_j)$ to $V(0, S_0)$

**Example**: For a European call under Black-Scholes, the PDE is:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

A Crank-Nicolson scheme with 200 time steps and 400 spatial nodes typically gives accuracy to several decimal places.

### Approach 2: Monte Carlo Simulation

Simulate paths of $S_t$ and average the discounted payoff.

**Procedure:**

1. Simulate $N$ independent paths of $S_t$ from $t$ to $T$
2. Compute the discounted payoff for each path: $e^{-r(T-t)} g(S_T^{(i)})$
3. Estimate: $\hat{V} = \frac{1}{N}\sum_{i=1}^N e^{-r(T-t)} g(S_T^{(i)})$

The standard error is $O(1/\sqrt{N})$, independent of dimension.

### Approach 3: Tree Methods

Discretize the stochastic process into a recombining lattice and compute expectations by backward induction.

**Procedure:**

1. Build a binomial or trinomial tree for $S_t$
2. Assign terminal payoffs at the final nodes
3. Discount backward through the tree: $V_j^n = e^{-r\Delta t}[\hat{p}\,V_{j+1}^{n+1} + (1-\hat{p})\,V_j^{n+1}]$

Trees are a discrete approximation to the PDE and converge to the continuous solution as the mesh refines.

---

## Comparison of Methods

| Criterion | PDE (Finite Diff.) | Monte Carlo | Trees |
|---|---|---|---|
| **Dimension** | 1--3 variables | Any dimension | 1--2 variables |
| **Convergence** | $O(\Delta x^2 + \Delta t^2)$ | $O(1/\sqrt{N})$ | $O(\Delta t)$ |
| **Greeks** | Direct from grid | Requires bump-and-reprice | Finite differences on tree |
| **Early exercise** | Free boundary methods | Least-squares MC (Longstaff-Schwartz) | Natural via backward induction |
| **Path dependence** | Difficult (add state variables) | Natural | Difficult |
| **All strikes at once** | Yes (full grid) | No (one payoff per run) | Yes (full tree) |

!!! tip "When to Use PDEs"
    PDEs excel when:

    - The problem is low-dimensional (1--3 state variables)
    - You need Greeks (sensitivities) — they come directly from the PDE solution
    - You need prices for many strikes/maturities simultaneously
    - Early exercise or free boundaries are present (American options)
    - High accuracy is required with modest computational cost

!!! tip "When to Use Monte Carlo"
    Monte Carlo excels when:

    - The problem is high-dimensional (basket options, CDOs)
    - The payoff is path-dependent (Asian, lookback, barrier)
    - The model is complex (stochastic volatility + jumps)
    - Moderate accuracy suffices

---

## The Black-Scholes PDE as a Canonical Example

The most important financial PDE is the **Black-Scholes equation**. Under geometric Brownian motion:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

the price $V(t, S)$ of any European derivative with payoff $g(S_T)$ satisfies:

$$
\boxed{
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
}
$$

**Key features:**

1. **Parabolic**: The equation is second-order in $S$ and first-order in $t$, with the classification determined by the positive coefficient $\frac{1}{2}\sigma^2 S^2 > 0$ for $S > 0$
2. **Terminal condition**: $V(T, S) = g(S)$ specifies the payoff at maturity
3. **Boundary conditions**: Depend on the specific derivative (e.g., $V(t, 0) = 0$ for a call)
4. **Universal**: The same PDE holds for calls, puts, digitals, and any European payoff — only the terminal condition changes

### Derivation via Hedging

Recall (see [§ Delta Hedging](../../ch06/bs_pde_derivation/delta_hedging.md)): the BS PDE also follows from a replicating-portfolio / no-arbitrage argument, giving the same equation as the Feynman–Kac route — see also [§ Replication](../../ch06/bs_pde_derivation/replication.md) and [§ One Equation, Five Perspectives](../../ch06/bs_pde_derivation/one_equation_five_perspectives.md) for the full taxonomy of derivations.

---

## Beyond Black-Scholes

The PDE framework extends naturally to richer models:

### Stochastic Volatility (Heston Model)

$$
dS_t = rS_t\,dt + \sqrt{v_t}\,S_t\,dW_t^S
$$

$$
dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^v
$$

The option price satisfies a **two-dimensional PDE** in $(t, S, v)$:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi v S\frac{\partial^2 V}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} - rV = 0
$$

### Jump-Diffusion (Merton Model)

With jumps of random size $J$, the PDE becomes a **partial integro-differential equation** (PIDE):

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV + \lambda\int_{\mathbb{R}}\left[V(t, Se^z) - V(t, S)\right]\nu(dz) = 0
$$

where $\lambda$ is the jump intensity and $\nu$ is the jump size distribution.

### Stochastic Interest Rates

When the short rate $r_t$ follows its own diffusion, bond prices satisfy PDEs of the form:

$$
\frac{\partial P}{\partial t} + \mathcal{L}_r P - r P = 0
$$

where $\mathcal{L}_r$ is the generator of the short-rate process.

---

## The PDE Perspective on Greeks

Recall (see [§ Greeks from PDE](../../ch06/bs_pde_structure/greeks_from_pde.md)): because $V(t,S)$ is solved on a full grid, the spatial Greeks ($\Delta = \partial_S V$, $\Gamma = \partial_{SS} V$) come for free, and the PDE itself yields the algebraic identity $\Theta = rV - rS\Delta - \tfrac12\sigma^2 S^2 \Gamma$.

---

## Historical Context

The PDE approach to finance has a rich history:

- **1900**: Bachelier models stock prices as Brownian motion and derives option prices via the heat equation — decades before Black-Scholes
- **1973**: Black, Scholes, and Merton derive the Black-Scholes PDE via hedging and connect it to risk-neutral expectations
- **1977**: Brennan and Schwartz solve American option pricing as a free boundary PDE problem
- **1993**: Heston's stochastic volatility model leads to a 2D pricing PDE with a semi-analytical solution
- **2000s**: PIDE methods for jump models; ADI schemes for multi-factor models

---

## Summary

$$
\boxed{
\text{Derivative price} = \text{Conditional expectation} = \text{PDE solution}
}
$$

The PDE approach to finance rests on three pillars:

| Pillar | Statement |
|---|---|
| **Feynman-Kac** | Expected values of diffusions satisfy parabolic PDEs |
| **Risk-neutral pricing** | Derivative prices are discounted expectations under $\mathbb{Q}$ |
| **Generator** | The drift and volatility of the underlying determine the PDE coefficients |

**PDEs provide the analytical backbone of quantitative finance: they yield closed-form solutions when available, efficient numerical schemes when not, and Greeks as a natural byproduct.**

---

## See Also

- [§ The SDE–PDE Bridge](sde_pde_bridge.md) — the mathematical connection between diffusions and PDEs
- [§ Classification of Second-Order PDEs](classification_of_second_order_pdes.md) — elliptic, parabolic, hyperbolic
- [§ Boundary Value Problems](boundary_value_problems.md) — Dirichlet, Neumann, Robin conditions
- [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — the rigorous statement and proof
- [Black–Scholes PDE](../../ch06/bs_pde_structure/discounting_and_killing_term.md) — detailed PDE structure

---

## Exercises

**Exercise 1.** A stock follows geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ with $r = 0.05$ and $\sigma = 0.25$. Write down the infinitesimal generator $\mathcal{L}$ in terms of $S$, and verify that the Black-Scholes PDE $\partial_t V + \mathcal{L}V = rV$ matches the standard form $\partial_t V + rS\,\partial_S V + \frac{1}{2}\sigma^2 S^2\,\partial_{SS}V = rV$.

??? success "Solution to Exercise 1"
    For geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, the drift is $\mu(S) = rS$ and the diffusion coefficient is $\sigma(S) = \sigma S$.

    The infinitesimal generator is:

    $$
    \mathcal{L} = \mu(S)\frac{\partial}{\partial S} + \frac{1}{2}\sigma^2(S)\frac{\partial^2}{\partial S^2} = rS\frac{\partial}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2}{\partial S^2}
    $$

    The Feynman-Kac equation with constant discounting rate $r$ is $\partial_t V + \mathcal{L}V - rV = 0$, which gives:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    Rearranging:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
    $$

    With $r = 0.05$ and $\sigma = 0.25$, this becomes:

    $$
    \frac{\partial V}{\partial t} + 0.05\,S\frac{\partial V}{\partial S} + \frac{1}{2}(0.0625)\,S^2\frac{\partial^2 V}{\partial S^2} = 0.05\,V
    $$

    This matches the standard Black-Scholes PDE form.

---

**Exercise 2.** Using the Black-Scholes PDE relationship $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma$, compute Theta for a European call option with $S = 100$, $K = 100$, $T - t = 0.5$, $r = 0.05$, $\sigma = 0.20$, given that $\Delta = 0.5987$, $\Gamma = 0.0261$, and $V = 7.97$. Compare your result with the interpretation that Theta represents time decay.

??? success "Solution to Exercise 2"
    Given $S = 100$, $K = 100$, $T - t = 0.5$, $r = 0.05$, $\sigma = 0.20$, $\Delta = 0.5987$, $\Gamma = 0.0261$, and $V = 7.97$.

    Using the Black-Scholes PDE relationship:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    Substituting:

    $$
    \Theta = (0.05)(7.97) - (0.05)(100)(0.5987) - \frac{1}{2}(0.04)(10000)(0.0261)
    $$

    $$
    = 0.3985 - 2.9935 - 5.22
    $$

    $$
    = -7.815
    $$

    So $\Theta \approx -7.82$ per year. Converting to daily theta (dividing by 365): $\Theta_{\text{daily}} \approx -0.0214$ per day.

    **Interpretation**: The option loses approximately $\$0.02$ per day due to time decay. This is consistent with the fact that an at-the-money option with six months to expiry experiences significant time decay. The three components of theta reveal the balance: the positive $rV$ term represents the return earned on the option's value, while the $-rS\Delta$ and $-\frac{1}{2}\sigma^2 S^2\Gamma$ terms represent the cost of carrying the hedging position. The net effect is negative, confirming that a long call option position decays in value as time passes.

---

**Exercise 3.** A Crank-Nicolson scheme has convergence $O(\Delta x^2 + \Delta t^2)$, while a Monte Carlo estimator with $N$ paths has error $O(1/\sqrt{N})$. Suppose each finite-difference step costs $O(J)$ operations (where $J$ is the number of spatial grid points), and each Monte Carlo path costs $O(M)$ operations (where $M$ is the number of time steps). For a one-dimensional pricing problem requiring four decimal places of accuracy, estimate which method is more efficient and explain your reasoning.

??? success "Solution to Exercise 3"
    **Finite difference (Crank-Nicolson)**: With $J$ spatial points and $N_t$ time steps, the total cost is $O(J \cdot N_t)$ (tridiagonal solves at each time step cost $O(J)$). For convergence $O(\Delta x^2 + \Delta t^2)$, to achieve accuracy $\epsilon = 10^{-4}$:

    - Need $\Delta x \sim \epsilon^{1/2} = 10^{-2}$, so $J \sim 1/\Delta x = 100$ spatial points
    - Need $\Delta t \sim \epsilon^{1/2} = 10^{-2}$, so $N_t \sim 1/\Delta t = 100$ time steps
    - Total cost: $O(J \cdot N_t) = O(10^4)$ operations

    **Monte Carlo**: With $N$ paths and $M$ time steps per path, the total cost is $O(N \cdot M)$. The statistical error is $O(\sigma_g / \sqrt{N})$ where $\sigma_g$ is the standard deviation of the discounted payoff. To achieve accuracy $\epsilon = 10^{-4}$:

    - Need $N \sim \sigma_g^2 / \epsilon^2$. For typical option pricing, $\sigma_g \sim O(1)$, so $N \sim 10^8$ paths
    - Each path needs $M \sim 100$ time steps for discretization accuracy
    - Total cost: $O(N \cdot M) = O(10^{10})$ operations

    **Comparison**: For this one-dimensional problem, the PDE method is vastly more efficient: $O(10^4)$ vs. $O(10^{10})$ operations. The PDE method wins by roughly six orders of magnitude.

    However, this advantage is specific to low dimensions. For a $d$-dimensional PDE, the grid cost becomes $O(J^d \cdot N_t) = O(100^d \cdot 100)$, which grows exponentially in $d$. Monte Carlo cost remains $O(10^{10})$ regardless of $d$ (the $O(1/\sqrt{N})$ rate is dimension-independent). The crossover occurs around $d \approx 3$--$4$, beyond which Monte Carlo becomes more practical.

---

**Exercise 4.** Derive the Black-Scholes PDE via the hedging argument. Starting from a portfolio $\Pi = V - \Delta S$ with $\Delta = \partial V/\partial S$, apply Ito's lemma to $dV$, substitute, and impose $d\Pi = r\Pi\,dt$ to obtain the PDE. Identify where the no-arbitrage condition enters and explain why the physical drift $\mu$ drops out.

??? success "Solution to Exercise 4"
    **Step 1**: Assume the stock follows $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ under the physical measure, and $V(t, S)$ is a twice-differentiable function. By Ito's lemma:

    $$
    dV = \frac{\partial V}{\partial t}\,dt + \frac{\partial V}{\partial S}\,dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}\,(dS)^2
    $$

    Since $(dS)^2 = \sigma^2 S^2\,dt$:

    $$
    dV = \left(\frac{\partial V}{\partial t} + \mu S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S\frac{\partial V}{\partial S}\,dW_t
    $$

    **Step 2**: Form the hedged portfolio $\Pi = V - \Delta S$ with $\Delta = \frac{\partial V}{\partial S}$:

    $$
    d\Pi = dV - \Delta\,dS = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right)dt
    $$

    The $dW_t$ terms cancel exactly because $\Delta = \partial V/\partial S$. The portfolio is **locally riskless**.

    **Step 3**: No-arbitrage requires that a riskless portfolio earns the risk-free rate:

    $$
    d\Pi = r\Pi\,dt = r(V - \Delta S)\,dt
    $$

    **Step 4**: Equating the two expressions for $d\Pi$:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = r\left(V - \frac{\partial V}{\partial S}S\right)
    $$

    Rearranging:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    **Where no-arbitrage enters**: The condition $d\Pi = r\Pi\,dt$ is the no-arbitrage requirement. If $d\Pi > r\Pi\,dt$, one could borrow at rate $r$ and invest in $\Pi$ for a riskless profit; if $d\Pi < r\Pi\,dt$, reverse the trade.

    **Why $\mu$ drops out**: The physical drift $\mu$ appears in $dS$ but cancels when forming $d\Pi = dV - \Delta\,dS$ because the hedge ratio $\Delta = \partial V/\partial S$ eliminates all exposure to the stock's random movements. Since the portfolio is riskless, its return cannot depend on $\mu$ -- it must equal $r$ regardless of the stock's expected return. This is the essence of risk-neutral pricing.

---

**Exercise 5.** The Heston model produces a two-dimensional PDE in $(t, S, v)$ for the option price $V$. Explain why PDE methods become impractical for basket options on $d \geq 4$ assets, even though they provide excellent accuracy in low dimensions. Relate your answer to the "curse of dimensionality" and contrast with the dimension-independence of Monte Carlo convergence rates.

??? success "Solution to Exercise 5"
    For a basket option on $d$ assets, the pricing PDE lives in $d + 1$ dimensions (one time variable plus $d$ asset prices):

    $$
    \frac{\partial V}{\partial t} + \sum_{i=1}^d rS_i\frac{\partial V}{\partial S_i} + \frac{1}{2}\sum_{i,j=1}^d \rho_{ij}\sigma_i\sigma_j S_i S_j\frac{\partial^2 V}{\partial S_i \partial S_j} - rV = 0
    $$

    **The curse of dimensionality**: A finite-difference grid with $J$ points per spatial dimension requires $J^d$ total grid points. With $J = 100$ and $d = 4$: $100^4 = 10^8$ grid points per time step. For $d = 10$: $100^{10} = 10^{20}$ grid points -- far beyond any computer's memory or processing capacity.

    The computational cost scales as $O(J^d \cdot N_t)$, growing exponentially in $d$. For $d \geq 4$, the memory required to store the grid alone becomes prohibitive, and iterative solvers for the resulting linear systems become impractical.

    **Monte Carlo dimension-independence**: The Monte Carlo estimator $\hat{V} = \frac{1}{N}\sum_{i=1}^N e^{-rT}g(S_T^{(i)})$ has standard error $\sigma_g / \sqrt{N}$, where $\sigma_g$ is the payoff standard deviation. Crucially, this convergence rate $O(1/\sqrt{N})$ does **not depend on $d$**. Simulating a path of $d$ correlated assets costs $O(d)$ per step (via Cholesky decomposition of the correlation matrix), so total cost is $O(N \cdot M \cdot d)$ -- polynomial in $d$, not exponential.

    **Summary**: PDE methods excel in 1--3 dimensions due to their superior convergence rate ($O(h^2)$ vs. $O(1/\sqrt{N})$) and direct access to Greeks. For $d \geq 4$, the exponential growth of the grid makes PDEs impractical, while Monte Carlo remains viable due to its dimension-independent convergence.

---

**Exercise 6.** In the Merton jump-diffusion model, the pricing equation is a partial integro-differential equation (PIDE) with an integral term $\lambda\int_{\mathbb{R}}[V(t, Se^z) - V(t, S)]\,\nu(dz)$. Explain physically what this integral term represents, why it is nonlocal, and why a standard finite difference scheme for the Black-Scholes PDE cannot be applied directly without modification.

??? success "Solution to Exercise 6"
    The integral term in the Merton PIDE is:

    $$
    \lambda\int_{\mathbb{R}}\left[V(t, Se^z) - V(t, S)\right]\nu(dz)
    $$

    **Physical meaning**: This term represents the **expected change in option value due to jumps**. At rate $\lambda$ (the jump intensity), the stock price jumps from $S$ to $Se^z$, where $z$ is the log-jump size drawn from the distribution $\nu$. The integral averages $V(t, Se^z) - V(t, S)$ over all possible jump sizes, weighted by $\nu(dz)$.

    - $V(t, Se^z)$: option value after a jump of size $z$
    - $V(t, S)$: option value before the jump
    - The difference captures the instantaneous P\&L from a jump event

    **Why it is nonlocal**: The integral term evaluates $V$ at the point $Se^z$ for all possible $z$. When $z$ is large, $Se^z$ can be far from $S$. This means the PIDE at the point $(t, S)$ depends on the values of $V$ at **distant points** in the spatial domain. This is fundamentally different from a standard PDE, where the equation at $(t, S)$ depends only on $V$ and its derivatives at $(t, S)$ -- purely local information.

    **Why standard finite differences fail**: A standard finite difference scheme for the Black-Scholes PDE approximates $\partial_S V$ and $\partial_{SS} V$ using values of $V$ at neighboring grid points (e.g., $V_{j-1}$, $V_j$, $V_{j+1}$). This works because the PDE is local. The integral term, however, requires evaluating $V(t, Se^z)$ at points that may span the entire grid. To handle this:

    - The integral must be **discretized separately**, typically by numerical quadrature over the jump-size distribution
    - If $\nu$ has fat tails (e.g., Gaussian jumps), the integral couples distant grid points, producing a **dense matrix** rather than the tridiagonal structure of the diffusion part
    - Implicit time-stepping for the integral part leads to a full linear system (not tridiagonal), dramatically increasing computational cost
    - Common approaches split the operator: treat the diffusion part implicitly (tridiagonal) and the integral part explicitly, or use FFT-based methods to evaluate the convolution efficiently

---

**Exercise 7.** The text states that tree methods are "a discrete approximation to the PDE and converge to the continuous solution as the mesh refines." For a one-step binomial tree with up factor $u = e^{\sigma\sqrt{\Delta t}}$, down factor $d = 1/u$, and risk-neutral probability $\hat{p} = (e^{r\Delta t} - d)/(u - d)$, show that the backward pricing equation $V = e^{-r\Delta t}[\hat{p}V_u + (1-\hat{p})V_d]$ is consistent with the Black-Scholes PDE in the limit $\Delta t \to 0$ by performing a Taylor expansion to second order in $\sqrt{\Delta t}$.

??? success "Solution to Exercise 7"
    The one-step binomial pricing equation is:

    $$
    V(t, S) = e^{-r\Delta t}\left[\hat{p}\,V(t+\Delta t, Su) + (1-\hat{p})\,V(t+\Delta t, Sd)\right]
    $$

    with $u = e^{\sigma\sqrt{\Delta t}}$, $d = e^{-\sigma\sqrt{\Delta t}}$, and $\hat{p} = \frac{e^{r\Delta t} - d}{u - d}$.

    **Taylor expansions** (letting $h = \sqrt{\Delta t}$):

    $$
    u = e^{\sigma h} = 1 + \sigma h + \frac{1}{2}\sigma^2 h^2 + O(h^3)
    $$

    $$
    d = e^{-\sigma h} = 1 - \sigma h + \frac{1}{2}\sigma^2 h^2 + O(h^3)
    $$

    $$
    e^{r\Delta t} = e^{rh^2} = 1 + rh^2 + O(h^4)
    $$

    The risk-neutral probability:

    $$
    \hat{p} = \frac{(1 + rh^2) - (1 - \sigma h + \frac{1}{2}\sigma^2 h^2)}{(1 + \sigma h + \frac{1}{2}\sigma^2 h^2) - (1 - \sigma h + \frac{1}{2}\sigma^2 h^2)} = \frac{rh^2 + \sigma h - \frac{1}{2}\sigma^2 h^2}{2\sigma h}
    $$

    $$
    = \frac{1}{2} + \frac{(r - \frac{1}{2}\sigma^2)h}{2\sigma} + O(h^2)
    $$

    Now expand $V$ at the up and down nodes. Let $V_S = \partial V/\partial S$, $V_{SS} = \partial^2 V/\partial S^2$, and $V_t = \partial V/\partial t$:

    $$
    V(t+\Delta t, Su) = V + V_t h^2 + V_S S(\sigma h + \tfrac{1}{2}\sigma^2 h^2) + \tfrac{1}{2}V_{SS} S^2 \sigma^2 h^2 + O(h^3)
    $$

    $$
    V(t+\Delta t, Sd) = V + V_t h^2 + V_S S(-\sigma h + \tfrac{1}{2}\sigma^2 h^2) + \tfrac{1}{2}V_{SS} S^2 \sigma^2 h^2 + O(h^3)
    $$

    Computing the weighted average:

    $$
    \hat{p}\,V_u + (1-\hat{p})\,V_d = V + V_t h^2 + V_S S\sigma h(2\hat{p} - 1) + V_S S\tfrac{1}{2}\sigma^2 h^2 + \tfrac{1}{2}V_{SS}S^2\sigma^2 h^2 + O(h^3)
    $$

    Substituting $2\hat{p} - 1 = \frac{(r - \frac{1}{2}\sigma^2)h}{\sigma} + O(h^2)$:

    $$
    = V + V_t h^2 + V_S S(r - \tfrac{1}{2}\sigma^2)h^2 + V_S S\tfrac{1}{2}\sigma^2 h^2 + \tfrac{1}{2}V_{SS}S^2\sigma^2 h^2 + O(h^3)
    $$

    $$
    = V + \left(V_t + rSV_S + \tfrac{1}{2}\sigma^2 S^2 V_{SS}\right)h^2 + O(h^3)
    $$

    Multiplying by $e^{-r\Delta t} = 1 - rh^2 + O(h^4)$:

    $$
    e^{-r\Delta t}[\hat{p}\,V_u + (1-\hat{p})\,V_d] = V + \left(V_t + rSV_S + \tfrac{1}{2}\sigma^2 S^2 V_{SS} - rV\right)h^2 + O(h^3)
    $$

    For the binomial equation $V = e^{-r\Delta t}[\hat{p}\,V_u + (1-\hat{p})\,V_d]$ to hold to order $h^2$, we need:

    $$
    V_t + rSV_S + \tfrac{1}{2}\sigma^2 S^2 V_{SS} - rV = 0
    $$

    This is exactly the **Black-Scholes PDE**, confirming that the binomial tree is consistent with it in the limit $\Delta t \to 0$.
