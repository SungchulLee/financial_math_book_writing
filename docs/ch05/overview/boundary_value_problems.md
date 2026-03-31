# Boundary Value Problems

A partial differential equation alone does not determine a unique solution. We must also specify **boundary conditions** -- constraints on the solution at the edges of the domain -- and **initial or terminal conditions**. The choice of conditions is dictated by the PDE type and the physics (or finance) of the problem. A problem is **well-posed** when these conditions guarantee existence, uniqueness, and continuous dependence on the data.

---

## The Parabolic Initial-Boundary Value Problem

The standard setting for financial PDEs is a **parabolic equation on a bounded domain**:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u = f \quad \text{in } (0, T) \times \Omega
$$

with terminal condition:

$$
u(T, x) = g(x) \quad \text{for } x \in \Omega
$$

and boundary conditions on $\partial\Omega$, where $\Omega \subset \mathbb{R}^d$ is the spatial domain and:

$$
\mathcal{L} = \sum_i \mu_i(x)\frac{\partial}{\partial x_i} + \frac{1}{2}\sum_{i,j} a_{ij}(x)\frac{\partial^2}{\partial x_i \partial x_j} - r(x)
$$

is the pricing operator (generator minus discounting).

The **parabolic boundary** consists of the terminal time and the spatial boundary:

$$
\Gamma = \{T\} \times \Omega \;\cup\; [0, T] \times \partial\Omega
$$

!!! note "Time Direction"
    In finance, the terminal condition is given at $t = T$ and the PDE is solved backward. Mathematically this is equivalent (via $\tau = T - t$) to a forward initial value problem.

---

## Types of Boundary Conditions

### Dirichlet Condition (Prescribed Value)

$$
\boxed{u(t, x) = h(t, x) \quad \text{for } (t, x) \in [0,T] \times \partial\Omega}
$$

The solution is prescribed on the boundary. This is the most common type in finance.

**Financial interpretation**: The option price is **known** at the boundary.

**Examples:**

- **European call** as $S \to 0$: $V(t, 0) = 0$ (worthless if stock is zero)
- **European call** as $S \to \infty$: $V(t, S) \approx S - Ke^{-r(T-t)}$ (deep in-the-money)
- **Knock-out barrier option** at barrier $B$: $V(t, B) = 0$ (option knocked out)
- **Killed diffusion**: Process absorbed at boundary $\implies$ $u = 0$ on $\partial\Omega$

### Neumann Condition (Prescribed Flux)

$$
\boxed{\frac{\partial u}{\partial n}(t, x) = h(t, x) \quad \text{for } (t, x) \in [0,T] \times \partial\Omega}
$$

where $\frac{\partial}{\partial n}$ is the outward normal derivative. The **rate of change** of the solution is prescribed, not the value itself.

**Financial interpretation**: The option's **delta** is specified at the boundary.

**Examples:**

- **Put option** as $S \to \infty$: $\frac{\partial V}{\partial S} \to 0$ (delta approaches zero)
- **Reflecting boundary**: Probability mass is reflected back into the domain
- **Symmetry condition**: $\frac{\partial u}{\partial x} = 0$ at a line of symmetry

### Robin Condition (Mixed)

$$
\boxed{\alpha(x)\,u(t, x) + \beta(x)\frac{\partial u}{\partial n}(t, x) = h(t, x) \quad \text{for } (t, x) \in [0,T] \times \partial\Omega}
$$

A linear combination of the solution value and its normal derivative is specified. This interpolates between Dirichlet ($\beta = 0$) and Neumann ($\alpha = 0$).

**Financial interpretation**: A partial absorption/reflection condition, or a **linear relationship between price and delta** at the boundary.

**Example**: Elastic barriers where partial rebates are paid upon hitting the boundary.

---

## Comparison of Boundary Conditions

| Type | Specifies | Probabilistic Meaning | Financial Example |
|---|---|---|---|
| **Dirichlet** | $u = h$ | Absorption (killing) at boundary | Barrier option knockout |
| **Neumann** | $\partial_n u = h$ | Reflection at boundary | No-flux condition |
| **Robin** | $\alpha u + \beta \partial_n u = h$ | Partial absorption/reflection | Elastic barrier |

---

## Well-Posedness in the Sense of Hadamard

A problem is **well-posed** if it satisfies three conditions:

1. **Existence**: A solution exists
2. **Uniqueness**: The solution is unique (in an appropriate function space)
3. **Continuous dependence**: Small changes in the data lead to small changes in the solution

$$
\boxed{
\|u_1 - u_2\| \leq C\left(\|g_1 - g_2\| + \|h_1 - h_2\| + \|f_1 - f_2\|\right)
}
$$

where $g$ is the terminal data, $h$ is the boundary data, and $f$ is the source term.

!!! warning "Ill-Posedness"
    Not all combinations of PDE type and boundary conditions are well-posed:

    - **Backward heat equation** ($u_t + \frac{1}{2}u_{xx} = 0$ with *initial* data at $t = 0$, solving forward): ill-posed. Arbitrarily small perturbations in data can produce arbitrarily large changes in the solution. This reflects the irreversibility of diffusion.
    - **Laplace equation with Cauchy data** (prescribing both $u$ and $\partial_n u$ on part of the boundary): ill-posed (Hadamard's counterexample).

### Correct Pairings

| PDE Type | Well-Posed Problem | Condition Type |
|---|---|---|
| **Elliptic** | Dirichlet/Neumann/Robin on entire $\partial\Omega$ | Boundary only |
| **Parabolic** | Terminal data + boundary conditions on $\partial\Omega$ | Initial/terminal + boundary |
| **Hyperbolic** | Initial data $u(0,x)$, $u_t(0,x)$ + boundary | Two initial + boundary |

---

## The Maximum Principle and Uniqueness

For parabolic equations, the **maximum principle** provides both uniqueness and continuous dependence.

**Theorem (Parabolic Maximum Principle)**: If $u$ satisfies $\partial_t u + \mathcal{L}u \leq 0$ in $(0,T) \times \Omega$ (with $r \geq 0$ in $\mathcal{L}$), then:

$$
\max_{\overline{Q}_T} u = \max_{\Gamma} u
$$

where $\Gamma$ is the parabolic boundary.

**Corollary (Uniqueness)**: If $u_1$ and $u_2$ both solve the same parabolic IBVP, then $w = u_1 - u_2$ satisfies the homogeneous problem with zero data on $\Gamma$. By the maximum principle, $w \leq 0$ and $-w \leq 0$, so $w = 0$. $\square$

**Corollary (Stability)**: The continuous dependence estimate:

$$
\|u_1 - u_2\|_{L^\infty(Q_T)} \leq \max\left(\|g_1 - g_2\|_\infty,\, \|h_1 - h_2\|_\infty\right)
$$

follows directly from the maximum principle.

---

## Boundary Conditions in the Black-Scholes Framework

For a European derivative with payoff $g(S)$ under Black-Scholes dynamics, the PDE domain is typically $(t, S) \in [0, T] \times [0, \infty)$.

### Terminal Condition

$$
V(T, S) = g(S)
$$

This is universal -- it encodes the derivative's payoff structure.

### Boundary at $S = 0$

At $S = 0$, the Black-Scholes operator degenerates: $\frac{1}{2}\sigma^2 S^2 \partial_{SS} \to 0$. The PDE reduces to:

$$
\frac{\partial V}{\partial t} = rV \quad \Longrightarrow \quad V(t, 0) = e^{-r(T-t)} g(0)
$$

For a call ($g(0) = 0$): $V(t, 0) = 0$. For a put ($g(0) = K$): $V(t, 0) = Ke^{-r(T-t)}$.

!!! info "Why No Boundary Condition Is Needed at $S = 0$"
    The degeneracy of the PDE at $S = 0$ means $S = 0$ is an **absorbing boundary** for geometric Brownian motion: once $S_t = 0$, it remains there forever. Probabilistically, $\mathbb{P}(S_t = 0 \text{ for some } t) = 0$, so the boundary is never reached. The PDE determines its own boundary behavior there.

### Boundary as $S \to \infty$

An artificial truncation at $S = S_\text{max}$ requires a far-field boundary condition. Common choices:

| Derivative | Far-Field Condition | Justification |
|---|---|---|
| European call | $V \approx S - Ke^{-r(T-t)}$ | Deep ITM asymptotics |
| European put | $V \approx 0$ | Worthless for large $S$ |
| General | $\frac{\partial^2 V}{\partial S^2} \approx 0$ | Gamma vanishes far from strike |

---

## Barrier Options and Domain Truncation

**Barrier options** provide the cleanest financial example of Dirichlet boundary conditions.

### Down-and-Out Call

Domain: $(t, S) \in [0, T] \times (B, \infty)$ where $B < K$ is the barrier.

$$
\begin{cases}
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0 & \text{for } S > B \\
V(T, S) = (S - K)^+ & \text{terminal condition} \\
V(t, B) = 0 & \text{Dirichlet at barrier}
\end{cases}
$$

The Dirichlet condition $V(t, B) = 0$ encodes the knockout feature: the option becomes worthless upon hitting the barrier.

### Up-and-Out Put

Domain: $(t, S) \in [0, T] \times (0, B)$ where $B > K$ is the upper barrier.

$$
V(t, B) = 0 \quad \text{(knockout at upper barrier)}
$$

### Rebate Barrier Option

If a rebate $R$ is paid upon knockout:

$$
V(t, B) = R \quad \text{(nonzero Dirichlet)}
$$

---

## Free Boundary Problems and American Options

**American options** introduce a fundamentally new type of boundary condition: the **free boundary** (also called the **optimal exercise boundary**).

The holder can exercise at any time $t \leq T$, so the price satisfies the **linear complementarity problem**:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V \leq 0, \quad V \geq g(S), \quad \left(\frac{\partial V}{\partial t} + \mathcal{L}V\right)(V - g) = 0
$$

This decomposes the domain into:

- **Continuation region**: $V > g$ and $\frac{\partial V}{\partial t} + \mathcal{L}V = 0$ (standard PDE)
- **Exercise region**: $V = g$ (option exercised immediately)
- **Free boundary** $S^*(t)$: The curve separating the two regions

At the free boundary, two conditions hold simultaneously:

$$
V(t, S^*(t)) = g(S^*(t)) \quad \text{(value matching)}
$$

$$
\frac{\partial V}{\partial S}(t, S^*(t)) = g'(S^*(t)) \quad \text{(smooth pasting)}
$$

!!! tip "Smooth Pasting"
    The smooth-pasting condition states that not only the price but also the delta is continuous across the free boundary. This is a necessary condition for the optimal exercise policy and emerges naturally from the variational inequality formulation.

---

## Existence and Regularity Theory

For the parabolic IBVP with Dirichlet conditions:

$$
\begin{cases}
\partial_t u + \mathcal{L}u = f & \text{in } Q_T = (0,T) \times \Omega \\
u(T, \cdot) = g & \text{on } \Omega \\
u = h & \text{on } [0,T] \times \partial\Omega
\end{cases}
$$

**Theorem (Classical Existence)**: If $\Omega$ has smooth boundary, coefficients are smooth, $a_{ij}$ is uniformly elliptic, and data $(f, g, h)$ are compatible and smooth, then there exists a unique classical solution $u \in C^{2,1}(\overline{Q}_T)$.

**Theorem (Weak/Viscosity Solutions)**: Under weaker conditions (bounded measurable coefficients, continuous data), the problem admits a unique viscosity solution. This is the appropriate framework for degenerate equations and non-smooth payoffs encountered in finance.

---

## Summary

| Aspect | Description |
|---|---|
| **Dirichlet** | Prescribes $u$ on boundary; absorbing/knockout |
| **Neumann** | Prescribes $\partial_n u$; reflecting/no-flux |
| **Robin** | Linear combination; partial absorption |
| **Well-posedness** | Existence + uniqueness + stability |
| **Maximum principle** | Ensures uniqueness and stability for parabolic PDEs |
| **Free boundary** | American options; exercise boundary determined as part of solution |

$$
\boxed{
\text{PDE} + \text{terminal condition} + \text{boundary conditions} \;\Longrightarrow\; \text{unique, stable solution}
}
$$

**The choice of boundary conditions reflects the financial structure of the derivative: knockout barriers impose Dirichlet conditions, no-arbitrage constraints determine far-field behavior, and early exercise creates free boundaries.**

---

## See Also

- [Why PDEs in Finance](why_pdes_in_finance.md) -- motivation for the PDE approach
- [Classification of Second-Order PDEs](classification_of_second_order_pdes.md) -- which boundary conditions are appropriate for which PDE type
- [Maximum Principle](../heat_equation/maximum_principle.md) -- the tool for uniqueness and stability
- [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md) -- boundary conditions for diffusion expectations

---

## Exercises

**Exercise 1.**
For a European put option under Black-Scholes dynamics, state the terminal condition $V(T, S)$ and the boundary conditions at $S = 0$ and as $S \to \infty$. Verify that the boundary condition at $S = 0$ is consistent with the degenerate PDE $\partial_t V = rV$ at that point.

---

**Exercise 2.**
Consider a down-and-out call option with barrier $B < K$ and strike $K$. Write the complete initial-boundary value problem: the Black-Scholes PDE on the domain $S \in (B, \infty)$, the terminal condition, and the Dirichlet boundary condition at $S = B$. What is the probabilistic interpretation of the Dirichlet condition?

---

**Exercise 3.**
The Hadamard well-posedness conditions require existence, uniqueness, and continuous dependence on data. Using the maximum principle, prove the continuous dependence estimate

$$
\|u_1 - u_2\|_\infty \leq \max(\|g_1 - g_2\|_\infty, \|h_1 - h_2\|_\infty)
$$

for two solutions $u_1$, $u_2$ of the parabolic IBVP with different terminal data $g_1$, $g_2$ and boundary data $h_1$, $h_2$.

---

**Exercise 4.**
Explain why the backward heat equation $\partial_t u + \frac{1}{2}\partial_{xx} u = 0$ with initial data $u(0, x) = f(x)$ solved forward in time is ill-posed. Construct a sequence of initial data $f_n(x) = \frac{1}{n}\sin(nx)$ such that $\|f_n\|_\infty \to 0$ but the solution at any $t > 0$ blows up. What does this say about the irreversibility of diffusion?

---

**Exercise 5.**
For an American put option, the free boundary $S^*(t)$ separates the continuation region from the exercise region. State the smooth-pasting condition at $S^*(t)$ and explain why both value matching and smooth pasting must hold simultaneously. What would happen to the hedging strategy if the delta were discontinuous across the exercise boundary?

---

**Exercise 6.**
At $S = 0$, the Black-Scholes PDE degenerates because $\frac{1}{2}\sigma^2 S^2 \to 0$. Explain why this means no boundary condition needs to be imposed at $S = 0$. Connect this to the probabilistic fact that geometric Brownian motion can never reach zero: $\mathbb{P}(S_t = 0 \text{ for some } t > 0) = 0$.

---

**Exercise 7.**
Compare Dirichlet, Neumann, and Robin boundary conditions in terms of their probabilistic meaning for a diffusion process. For a particle undergoing Brownian motion in the interval $(a, b)$, describe the behavior at the boundary under each condition: absorption (killing), reflection, and partial absorption with probability $\alpha$.

---

## Solutions

??? success "Solution to Exercise 1"
    The European put has payoff $g(S) = (K - S)^+$, so the **terminal condition** is:

    $$
    V(T, S) = (K - S)^+ = \max(K - S,\, 0)
    $$

    **Boundary at $S = 0$**: At $S = 0$, the Black-Scholes PDE degenerates since $\frac{1}{2}\sigma^2 S^2 \to 0$, leaving $\frac{\partial V}{\partial t} = rV$. The payoff at $S = 0$ is $g(0) = K$, so the solution of $\partial_t V = rV$ with terminal value $K$ is:

    $$
    V(t, 0) = K e^{-r(T-t)}
    $$

    This is the present value of receiving $K$ at maturity, which is consistent: if the stock is at zero, it stays at zero (absorbing state for GBM), and the put pays $K$ with certainty.

    **Boundary as $S \to \infty$**: For large $S$, the put is deep out-of-the-money and becomes worthless:

    $$
    V(t, S) \to 0 \quad \text{as } S \to \infty
    $$

    **Verification**: At $S = 0$ the PDE reduces to $\partial_t V = rV$. Substituting $V(t, 0) = Ke^{-r(T-t)}$:

    $$
    \frac{\partial}{\partial t}\left[Ke^{-r(T-t)}\right] = rKe^{-r(T-t)} = rV(t,0)
    $$

    confirming consistency with the degenerate PDE.

??? success "Solution to Exercise 2"
    The complete initial-boundary value problem for the down-and-out call with barrier $B < K$ and strike $K$ is:

    **PDE** on the domain $S \in (B, \infty)$, $t \in [0, T]$:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0 \quad \text{for } S > B,\; t < T
    $$

    **Terminal condition** at $t = T$:

    $$
    V(T, S) = (S - K)^+ \quad \text{for } S > B
    $$

    **Dirichlet boundary condition** at $S = B$:

    $$
    V(t, B) = 0 \quad \text{for all } t \in [0, T]
    $$

    **Far-field condition** as $S \to \infty$:

    $$
    V(t, S) \approx S - Ke^{-r(T-t)} \quad \text{as } S \to \infty
    $$

    **Probabilistic interpretation of the Dirichlet condition**: The condition $V(t, B) = 0$ corresponds to the option being **killed** (knocked out) when the stock price hits the barrier $B$. In probabilistic terms, if $\tau_B = \inf\{s \geq t : S_s = B\}$ is the first hitting time of the barrier, then the option pays zero if $\tau_B \leq T$. The Dirichlet condition encodes this absorbing boundary: the diffusion is killed upon reaching $B$, and the discounted payoff from that point onward is zero.

??? success "Solution to Exercise 3"
    Let $u_1$ and $u_2$ solve the parabolic IBVP with the same operator but different data:

    $$
    \partial_t u_i + \mathcal{L}u_i = 0 \quad \text{in } (0,T) \times \Omega
    $$

    with terminal data $u_i(T, x) = g_i(x)$ and boundary data $u_i(t, x) = h_i(t, x)$ on $\partial\Omega$.

    Define $w = u_1 - u_2$. Then $w$ satisfies:

    $$
    \partial_t w + \mathcal{L}w = 0 \quad \text{in } (0,T) \times \Omega
    $$

    with terminal data $w(T, x) = g_1(x) - g_2(x)$ and boundary data $w = h_1 - h_2$ on $\partial\Omega$.

    By the **parabolic maximum principle**, the maximum of $w$ over $\overline{Q}_T = [0,T] \times \overline{\Omega}$ is attained on the parabolic boundary $\Gamma = \{T\} \times \Omega \cup [0,T] \times \partial\Omega$:

    $$
    \max_{\overline{Q}_T} w = \max_\Gamma w \leq \max\left(\|g_1 - g_2\|_\infty,\, \|h_1 - h_2\|_\infty\right)
    $$

    Applying the same argument to $-w$ (which also satisfies the homogeneous PDE):

    $$
    \max_{\overline{Q}_T} (-w) \leq \max\left(\|g_1 - g_2\|_\infty,\, \|h_1 - h_2\|_\infty\right)
    $$

    Combining these two inequalities:

    $$
    \|u_1 - u_2\|_\infty = \|w\|_{L^\infty(Q_T)} \leq \max\left(\|g_1 - g_2\|_\infty,\, \|h_1 - h_2\|_\infty\right)
    $$

    This is the continuous dependence estimate, confirming well-posedness in the sense of Hadamard. $\square$

??? success "Solution to Exercise 4"
    Consider the backward heat equation $\partial_t u + \frac{1}{2}\partial_{xx} u = 0$ with initial data $u(0, x) = f(x)$, solved forward in time (i.e., for $t > 0$).

    **Why it is ill-posed**: Under the change $\tau = -t$, this becomes the standard heat equation solved backward in time. Equivalently, by separation of variables or Fourier analysis, an initial mode $e^{ikx}$ evolves as $e^{ikx + \frac{1}{2}k^2 t}$, which **grows exponentially** in $t$. High-frequency components are amplified rather than damped.

    **Explicit construction**: Take $f_n(x) = \frac{1}{n}\sin(nx)$. Then $\|f_n\|_\infty = \frac{1}{n} \to 0$ as $n \to \infty$.

    The solution of $\partial_t u + \frac{1}{2}\partial_{xx}u = 0$ with $u(0,x) = \frac{1}{n}\sin(nx)$ is:

    $$
    u_n(t, x) = \frac{1}{n}\sin(nx)\,e^{\frac{1}{2}n^2 t}
    $$

    One can verify: $\partial_t u_n = \frac{n}{2}\sin(nx)\,e^{\frac{1}{2}n^2 t}$ and $\frac{1}{2}\partial_{xx}u_n = -\frac{n}{2}\sin(nx)\,e^{\frac{1}{2}n^2 t}$, so $\partial_t u_n + \frac{1}{2}\partial_{xx}u_n = 0$.

    At any fixed $t > 0$:

    $$
    \|u_n(t, \cdot)\|_\infty = \frac{1}{n}\,e^{\frac{1}{2}n^2 t} \to \infty \quad \text{as } n \to \infty
    $$

    So the initial data converges to zero uniformly, but the solution blows up for any $t > 0$. This violates continuous dependence on data.

    **Connection to irreversibility of diffusion**: The heat equation (forward in time) smooths and loses information -- high-frequency details are exponentially damped. Reversing this process requires reconstructing those lost details, which amplifies any noise exponentially. This reflects the fundamental **thermodynamic irreversibility** of diffusion: you cannot "unmix" a diffused substance.

??? success "Solution to Exercise 5"
    For an American put with payoff $g(S) = (K - S)^+$, the free boundary $S^*(t)$ is the critical stock price below which immediate exercise is optimal.

    **Value matching** at the free boundary:

    $$
    V(t, S^*(t)) = (K - S^*(t))^+ = K - S^*(t)
    $$

    This states that the option price equals the exercise value at the boundary -- continuity of the price across the exercise boundary.

    **Smooth pasting** at the free boundary:

    $$
    \frac{\partial V}{\partial S}(t, S^*(t)) = g'(S^*(t)) = -1
    $$

    This states that the delta of the option equals the delta of the exercise payoff at the boundary -- the first derivative is also continuous.

    **Why both must hold simultaneously**: Value matching alone is insufficient because it only ensures price continuity. The smooth-pasting condition is a **necessary optimality condition** that arises from the variational inequality formulation. If only value matching held but $\partial_S V \neq g'$ at $S^*(t)$, then the exercise boundary could be shifted slightly to improve the option value, contradicting optimality.

    **Consequences of discontinuous delta**: If the delta were discontinuous across the exercise boundary, the hedging portfolio $\Pi = V - \Delta S$ would require a **discrete, instantaneous rebalancing** at the moment the stock crosses $S^*(t)$. This would create:

    - A jump in the hedge ratio, leading to a non-self-financing portfolio
    - Infinite transaction costs in the presence of market frictions
    - An inability to perfectly replicate the option payoff

    The smooth-pasting condition ensures that the hedge ratio transitions continuously, making delta hedging implementable in practice.

??? success "Solution to Exercise 6"
    The Black-Scholes PDE for $V(t, S)$ is:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    At $S = 0$, the coefficient of the second-order term vanishes: $\frac{1}{2}\sigma^2 S^2 \big|_{S=0} = 0$. Likewise, the first-order drift term vanishes: $rS\big|_{S=0} = 0$. The PDE degenerates to the ODE $\frac{\partial V}{\partial t} = rV$, which has the unique solution $V(t, 0) = e^{-r(T-t)}g(0)$ given the terminal condition $V(T, 0) = g(0)$.

    **Why no boundary condition is needed**: Since the PDE itself determines $V(t, 0)$ uniquely from the terminal condition, imposing an additional boundary condition at $S = 0$ would **overdetermine** the problem. The degeneracy of the second-order term means the PDE transitions from a parabolic equation (requiring boundary data) to an ODE (self-contained) at $S = 0$.

    **Probabilistic connection**: Geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t$ has the explicit solution $S_t = S_0 \exp\left((r - \frac{1}{2}\sigma^2)t + \sigma W_t\right)$. Since the exponential function is strictly positive for all finite values of its argument, $S_t > 0$ for all $t \geq 0$ whenever $S_0 > 0$. Therefore:

    $$
    \mathbb{P}(S_t = 0 \text{ for some } t > 0 \mid S_0 > 0) = 0
    $$

    The boundary $S = 0$ is **never reached** by the diffusion. In the Feller classification, $S = 0$ is an **entrance boundary** (or natural boundary, depending on parameters): the process cannot reach it from the interior. Since no sample paths touch this boundary, no boundary condition is needed to determine the conditional expectation $\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}g(S_T) \mid S_t = S]$.

    In contrast, a finite barrier $B > 0$ is reachable by the diffusion with positive probability, so a Dirichlet condition at $S = B$ carries genuine information about what happens upon arrival.

??? success "Solution to Exercise 7"
    Consider a particle undergoing standard Brownian motion $X_t$ in the interval $(a, b)$. The three boundary conditions correspond to distinct physical behaviors at the endpoints:

    **Dirichlet condition** $u(t, a) = 0$, $u(t, b) = 0$: This corresponds to **absorption** (killing). When the Brownian particle reaches the boundary $a$ or $b$, it is immediately removed from the system. In the PDE context, $u(t, x) = \mathbb{E}_x[g(X_T)\,\mathbf{1}_{\{\tau > T\}}]$ where $\tau = \inf\{t : X_t \notin (a,b)\}$ is the first exit time. The solution accounts only for particles that survive to time $T$ without hitting the boundary.

    - Probabilistic meaning: The particle is **killed** upon reaching the boundary
    - Financial analogy: Knock-out barrier options, where the contract terminates at the barrier

    **Neumann condition** $\frac{\partial u}{\partial n}(t, a) = 0$, $\frac{\partial u}{\partial n}(t, b) = 0$: This corresponds to **reflection**. When the particle reaches the boundary, it is instantaneously pushed back into the interior. The resulting process is **reflected Brownian motion**, which satisfies $X_t \in [a, b]$ for all $t$ and accumulates local time at the boundary. The zero-flux condition $\partial_n u = 0$ ensures no probability mass leaks out of the domain.

    - Probabilistic meaning: The particle is **reflected** at the boundary
    - Financial analogy: Models where the state variable is constrained to a range (e.g., interest rates with a floor)

    **Robin condition** $\alpha u(t, a) + \beta \frac{\partial u}{\partial n}(t, a) = 0$: This corresponds to **partial absorption** (elastic boundary). When the particle reaches the boundary, it is killed with probability proportional to $\alpha / (\alpha + \beta)$ and reflected with the complementary probability. This interpolates between pure absorption ($\beta = 0$, Dirichlet) and pure reflection ($\alpha = 0$, Neumann).

    - Probabilistic meaning: The particle is **killed with probability $p$** and **reflected with probability $1 - p$** at each boundary encounter, where $p$ depends on the ratio $\alpha/\beta$
    - Financial analogy: Elastic barrier options where a partial rebate is paid upon hitting the boundary, and the option has a probability of surviving the barrier hit

    In summary:

    | Condition | Boundary Behavior | Probability Mass |
    |---|---|---|
    | Dirichlet ($u = 0$) | Absorption/killing | Mass destroyed at boundary |
    | Neumann ($\partial_n u = 0$) | Reflection | Mass conserved, pushed back |
    | Robin ($\alpha u + \beta \partial_n u = 0$) | Partial absorption | Fraction destroyed, rest reflected |
