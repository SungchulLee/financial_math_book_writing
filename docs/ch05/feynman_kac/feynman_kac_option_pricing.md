# Applications to Option Pricing

The Feynman-Kac formula transforms every option pricing problem into a PDE, and every PDE back into an expectation. This page applies the framework to concrete financial derivatives: **European options** (the Black-Scholes formula as a direct Feynman-Kac computation), **barrier options** (Feynman-Kac on restricted domains), and the **connection to American options** (free boundary problems and variational inequalities).

!!! tip "Related Content"

    - [Feynman-Kac Formula](feynman_kac_formula.md) -- the general theorem
    - [Discounted Feynman-Kac](discounted_feynman_kac.md) -- the discounting mechanism
    - [Proof Sketch](feynman_kac_proof_sketch.md) -- the martingale argument

---

## European Options: Black-Scholes via Feynman-Kac

### Setup

Under the risk-neutral measure $\mathbb{Q}$, the stock price follows:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

A European derivative with payoff $g(S_T)$ at maturity $T$ has price:

$$
V(t, S) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(T-t)}\,g(S_T) \,\Big|\, S_t = S\right]
$$

By the Feynman-Kac formula, $V$ satisfies:

$$
\boxed{
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0, \quad V(T, S) = g(S)
}
$$

### Deriving the Black-Scholes Formula

Recall (see [§ Geometric Brownian Motion](../kolmogorov_equations/transition_densities_standard_sdes.md#geometric-brownian-motion)): under $\mathbb{Q}$, $S_T \mid S_t = S$ is lognormal with $\log(S_T/S) \sim N((r-\sigma^2/2)(T-t),\,\sigma^2(T-t))$. Integrating the call payoff against this density (Exercise 6 of that page carries out the calculation) yields

$$
V(t, S) = S\,\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2),
$$

$$
d_1 = \frac{\log(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}, \qquad d_2 = d_1 - \sigma\sqrt{T-t}.
$$

The PDE and hedging derivations of the same formula live in [§ Why PDEs in Finance](../overview/why_pdes_in_finance.md); this page treats only the **option-pricing perspective** — payoff structure, boundary conditions, and extensions to barriers and American options.

### European Put

By the same method (or by put-call parity):

$$
P(t, S) = Ke^{-r(T-t)}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)
$$

**Put-call parity** (a model-independent no-arbitrage relation):

$$
C(t, S) - P(t, S) = S - Ke^{-r(T-t)}
$$

### Digital (Binary) Option

Payoff $g(S) = \mathbf{1}_{\{S > K\}}$ (pays $\$1$ if in the money):

$$
V_{\text{digital}}(t, S) = e^{-r(T-t)}\,\mathbb{Q}(S_T > K \mid S_t = S) = e^{-r(T-t)}\,\mathcal{N}(d_2)
$$

---

## Barrier Options via Feynman-Kac

Barrier options modify the domain of the PDE by introducing **absorbing boundaries**. The Feynman-Kac formula applies to the killed diffusion -- the process conditioned on not hitting the barrier.

### Down-and-Out Call

**Payoff**: $(S_T - K)^+$ if $\min_{t \leq s \leq T} S_s > B$ (barrier $B < K$).

**Feynman-Kac formulation**: The price satisfies the Black-Scholes PDE on the restricted domain $S > B$:

$$
\begin{cases}
\partial_t V + rS\,\partial_S V + \frac{1}{2}\sigma^2 S^2\,\partial_{SS}V - rV = 0 & \text{for } S > B \\
V(T, S) = (S - K)^+ & \text{terminal condition} \\
V(t, B) = 0 & \text{knockout at barrier}
\end{cases}
$$

**Probabilistic representation**:

$$
V_{\text{DO}}(t, S) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(T-t)}(S_T - K)^+\,\mathbf{1}_{\{\tau_B > T\}} \,\Big|\, S_t = S\right]
$$

where $\tau_B = \inf\{s > t : S_s \leq B\}$ is the first hitting time of the barrier.

### Closed-Form Solution

The reflection principle for Brownian motion (after the log-transformation $X = \log S$) gives:

$$
V_{\text{DO}}(t, S) = V_{\text{BS}}(t, S) - \left(\frac{B}{S}\right)^{2r/\sigma^2 - 1} V_{\text{BS}}\!\left(t, \frac{B^2}{S}\right)
$$

where $V_{\text{BS}}$ is the standard Black-Scholes price. The second term is the correction for paths that cross the barrier.

!!! info "In-Out Parity"
    For any barrier option:

    $$
    V_{\text{knock-in}} + V_{\text{knock-out}} = V_{\text{vanilla}}
    $$

    This is an immediate consequence of the partition of paths into those that hit the barrier and those that do not.

### Up-and-Out Put

**Domain**: $S < B$ with $V(t, B) = 0$.

The PDE is the same Black-Scholes equation, but now solved on $(0, B)$ instead of $(0, \infty)$.

### Double Barrier Options

With barriers $B_l < S < B_u$, the PDE domain is the finite interval $(B_l, B_u)$:

$$
V(t, B_l) = V(t, B_u) = 0
$$

The Green's function on this bounded domain can be expressed via the **spectral decomposition** (eigenfunction expansion) or the **method of images** (infinite series of reflected Gaussians).

---

## Connection to American Options

American options can be exercised at any time $t \leq T$, which fundamentally changes the mathematical structure. The Feynman-Kac formula does not directly apply because the exercise time is a **stopping time** chosen by the holder.

### The Optimal Stopping Formulation

The American option price is:

$$
V^{\text{Am}}(t, S) = \sup_{\tau \in [t, T]}\mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(\tau - t)}\,g(S_\tau) \,\Big|\, S_t = S\right]
$$

where the supremum is over all stopping times $\tau$.

### The Variational Inequality

Instead of a PDE with equality, the American option satisfies a **variational inequality**:

$$
\boxed{
\max\!\left(\partial_t V + \mathcal{L}V - rV,\; g(S) - V\right) = 0
}
$$

This encodes two complementary conditions:

- **In the continuation region** ($V > g$): $\partial_t V + \mathcal{L}V - rV = 0$ (the standard Feynman-Kac PDE holds)
- **In the exercise region** ($V = g$): The option is exercised immediately

### The Free Boundary

The **optimal exercise boundary** $S^*(t)$ separates the two regions:

- For an American put: exercise when $S \leq S^*(t)$ (put is deep in the money)
- For an American call on a dividend-paying stock: exercise when $S \geq S^*(t)$

At the free boundary, two matching conditions hold:

$$
V(t, S^*(t)) = g(S^*(t)) \quad \text{(value matching)}
$$

$$
\frac{\partial V}{\partial S}(t, S^*(t)) = g'(S^*(t)) \quad \text{(smooth pasting)}
$$

!!! note "Early Exercise Premium"
    The American option price decomposes as:

    $$
    V^{\text{Am}} = V^{\text{Eu}} + \text{early exercise premium}
    $$

    The early exercise premium is the additional value from the right to exercise before maturity. For a non-dividend-paying call, this premium is zero (it is never optimal to exercise early), so $V^{\text{Am}} = V^{\text{Eu}}$.

---

## Exotic Options and Extensions

### Asian Options

The payoff depends on the average price: $g = \left(\frac{1}{T}\int_0^T S_s\,ds - K\right)^+$.

The average $A_t = \frac{1}{t}\int_0^t S_s\,ds$ is not Markovian in $S_t$ alone. To apply Feynman-Kac, introduce $A_t$ as an additional state variable:

$$
\partial_t V + rS\,\partial_S V + S\,\partial_A V + \frac{1}{2}\sigma^2 S^2\,\partial_{SS}V - rV = 0
$$

This is a 2D PDE in $(S, A)$ -- no closed-form solution exists in general.

### Lookback Options

The payoff depends on the running maximum: $g = S_T - \min_{0 \leq s \leq T} S_s$.

Again, the state space must be augmented with the running minimum $M_t = \min_{s \leq t} S_s$:

$$
\partial_t V + rS\,\partial_S V + \frac{1}{2}\sigma^2 S^2\,\partial_{SS}V - rV = 0 \quad \text{for } S > M
$$

with the boundary condition $\partial_M V(t, S, M)\big|_{M=S} = 0$.

### Options on Multiple Assets (Rainbow Options)

For a basket of $d$ assets with correlated dynamics:

$$
dS_t^i = rS_t^i\,dt + \sigma_i S_t^i\,dW_t^i, \quad d\langle W^i, W^j\rangle_t = \rho_{ij}\,dt
$$

the pricing PDE is $d$-dimensional:

$$
\partial_t V + \sum_i rS_i\,\partial_{S_i}V + \frac{1}{2}\sum_{i,j}\rho_{ij}\sigma_i\sigma_j S_i S_j\,\partial_{S_i S_j}V - rV = 0
$$

For $d > 3$, finite difference methods become impractical (curse of dimensionality), and Monte Carlo -- justified by the Feynman-Kac expectation representation -- becomes the method of choice.

---

## The PDE-Monte Carlo Duality

The Feynman-Kac formula establishes a **computational duality**: every option pricing problem can be attacked from either the PDE side or the expectation (Monte Carlo) side.

| Approach | Method | Best For |
|---|---|---|
| **PDE** | Finite differences on the PDE | Low-dimensional, full grid of prices, Greeks |
| **Monte Carlo** | Simulate paths, average payoff | High-dimensional, path-dependent, complex payoffs |
| **Analytical** | Solve PDE or evaluate expectation in closed form | When possible (GBM, affine models) |

!!! tip "The Feynman-Kac Principle in Practice"
    When designing a pricing method:

    1. Write the PDE (identify the generator, discounting, boundary conditions)
    2. Write the expectation (identify the SDE, discount factor, payoff)
    3. Choose the more efficient approach based on dimensionality and complexity

---

## Summary

| Derivative | PDE Domain | Boundary Conditions | Feynman-Kac Representation |
|---|---|---|---|
| **European** | $(0, \infty)$ | Far-field asymptotics | $e^{-r\tau}\,\mathbb{E}[g(S_T)]$ |
| **Down-out barrier** | $(B, \infty)$ | $V(t, B) = 0$ | $e^{-r\tau}\,\mathbb{E}[g(S_T)\,\mathbf{1}_{\tau_B > T}]$ |
| **Double barrier** | $(B_l, B_u)$ | $V = 0$ at both | Killed diffusion on bounded domain |
| **American** | $(0, \infty)$ with free boundary | Smooth pasting | $\sup_\tau \mathbb{E}[e^{-r\tau}g(S_\tau)]$ |
| **Asian** | $(S, A)$ augmented | --- | Path-dependent average |

$$
\boxed{
\text{Option pricing} = \text{Feynman-Kac} = \text{PDE with appropriate boundary conditions}
}
$$

**The Feynman-Kac formula unifies all of derivatives pricing under a single mathematical framework. European options give the simplest application, barrier options demonstrate the power of domain restrictions, and American options show the limits of the standard formula -- requiring the extension to optimal stopping and variational inequalities.**

---

## See Also

- [Feynman-Kac Formula](feynman_kac_formula.md) -- the foundational theorem
- [Discounted Feynman-Kac](discounted_feynman_kac.md) -- the discounting mechanism
- [Proof Sketch](feynman_kac_proof_sketch.md) -- the martingale derivation
- [Boundary Value Problems](../overview/boundary_value_problems.md) -- types of boundary conditions
- [Free vs Bounded Domains](../greens_functions/free_vs_bounded_domains.md) -- Green's functions with barriers

---

## Exercises

**Exercise 1.**
For a European put option with payoff $g(S) = (K - S)^+$, write the Feynman-Kac probabilistic representation and the corresponding Black-Scholes PDE with terminal and boundary conditions. What are the boundary conditions as $S \to 0$ and $S \to \infty$?

??? success "Solution to Exercise 1"
    **Feynman-Kac probabilistic representation**: For a European put with payoff $g(S) = (K - S)^+$:

    $$
    P(t, S) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(T-t)}(K - S_T)^+ \,\Big|\, S_t = S\right]
    $$

    **Black-Scholes PDE**:

    $$
    \frac{\partial P}{\partial t} + rS\frac{\partial P}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 P}{\partial S^2} - rP = 0
    $$

    **Terminal condition**: $P(T, S) = (K - S)^+$

    **Boundary conditions**:

    - As $S \to 0$: The put is deep in the money with certainty, so $P(t, 0) = Ke^{-r(T-t)}$ (the discounted strike).
    - As $S \to \infty$: The put is far out of the money with certainty, so $P(t, S) \to 0$.

---

**Exercise 2.**
A down-and-out call with barrier $B < S_0$ and strike $K > B$ has price $V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+\mathbf{1}_{\{\tau_B > T\}} | S_t = S]$. Write the PDE domain and boundary conditions. Explain why the PDE is solved on $(B, \infty)$ rather than $(0, \infty)$ and how the killing at the barrier is implemented.

??? success "Solution to Exercise 2"
    **PDE domain**: The down-and-out call is priced on $S \in (B, \infty)$ with $t \in [0, T]$.

    **Boundary conditions**:

    - **Terminal**: $V(T, S) = (S - K)^+$ for $S > B$
    - **Knockout**: $V(t, B) = 0$ for all $t \in [0, T]$
    - **Far-field**: $V(t, S) \to S - Ke^{-r(T-t)}$ as $S \to \infty$ (the option behaves like a forward)

    **Why the domain is $(B, \infty)$**: Once the stock price hits the barrier $B$, the option is immediately worthless (knocked out). The process is effectively "killed" at $\tau_B = \inf\{s > t : S_s \leq B\}$. In the Feynman-Kac framework, the indicator $\mathbf{1}_{\{\tau_B > T\}}$ restricts the expectation to paths that survive above $B$ for the entire interval $[t, T]$.

    **Implementation of killing at the barrier**: The Dirichlet boundary condition $V(t, B) = 0$ enforces the knockout. When solving the PDE numerically via finite differences, the grid starts at $S = B$ (not $S = 0$), and the boundary value $V = 0$ is imposed there at every time step. This is equivalent to absorbing the probability mass at $B$: any path reaching the barrier is removed from the expectation.

---

**Exercise 3.**
For a double barrier option with lower barrier $B_l$ and upper barrier $B_u$, the domain is $(B_l, B_u)$. If the payoff is $g(S) = (S - K)^+$ and both barriers are knock-out, write the boundary conditions at $S = B_l$ and $S = B_u$. How does the solution domain affect the Feynman-Kac expectation?

??? success "Solution to Exercise 3"
    **Boundary conditions for the double barrier knockout call**:

    - **Lower barrier**: $V(t, B_l) = 0$ for all $t \in [0, T]$ (knockout when the stock falls to $B_l$)
    - **Upper barrier**: $V(t, B_u) = 0$ for all $t \in [0, T]$ (knockout when the stock rises to $B_u$)
    - **Terminal**: $V(T, S) = (S - K)^+$ for $B_l < S < B_u$

    **Effect on the Feynman-Kac expectation**: The solution domain is the bounded interval $(B_l, B_u)$, and the Feynman-Kac representation becomes:

    $$
    V(t, S) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(T-t)}(S_T - K)^+\,\mathbf{1}_{\{\tau_{B_l} \wedge \tau_{B_u} > T\}} \,\Big|\, S_t = S\right]
    $$

    where $\tau_{B_l}$ and $\tau_{B_u}$ are the first hitting times of the lower and upper barriers. Only paths that remain entirely within $(B_l, B_u)$ during $[t, T]$ contribute to the expectation. The bounded domain means the Green's function decays faster than on $(0, \infty)$, and the option price is strictly less than the corresponding single-barrier or vanilla option.

---

**Exercise 4.**
Explain the difference between the Feynman-Kac representation for European options ($e^{-r\tau}\mathbb{E}[g(S_T)]$) and the optimal stopping formulation for American options ($\sup_\tau \mathbb{E}[e^{-r\tau}g(S_\tau)]$). Why does the American option require a free boundary problem rather than a standard PDE?

??? success "Solution to Exercise 4"
    **European option**: The price is a fixed expectation over all paths at the terminal time:

    $$
    V^{\text{Eu}}(t, S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]
    $$

    The exercise time is fixed at $T$, and $V$ satisfies the standard Feynman-Kac PDE $\partial_t V + \mathcal{L}V - rV = 0$ with equality throughout the domain.

    **American option**: The holder chooses an optimal stopping time $\tau \in [t, T]$:

    $$
    V^{\text{Am}}(t, S) = \sup_{\tau \in [t, T]}\mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(\tau - t)}g(S_\tau) \mid S_t = S\right]
    $$

    **Why a free boundary is needed**: At each time $t$, the holder compares the exercise value $g(S)$ with the continuation value $\mathbb{E}^{\mathbb{Q}}[e^{-r\Delta t}V^{\text{Am}}(t + \Delta t, S_{t+\Delta t})]$. There exists a critical stock price $S^*(t)$ separating:

    - **Continuation region** ($V^{\text{Am}} > g$): The Feynman-Kac PDE holds with equality.
    - **Exercise region** ($V^{\text{Am}} = g$): It is optimal to exercise immediately; $V^{\text{Am}} = g(S)$.

    The boundary $S^*(t)$ between these regions is not known a priori -- it must be determined as part of the solution. This is why the problem is a **free boundary problem** rather than a standard PDE with fixed boundary conditions. The standard Feynman-Kac formula does not apply directly because the terminal time is replaced by an optimally chosen random time.

---

**Exercise 5.**
For a European call in the Black-Scholes model, verify that the solution $V(t,S) = S\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)$ satisfies the terminal condition $V(T, S) = (S - K)^+$ by computing $\lim_{t \to T^-} V(t, S)$ for the cases $S > K$ and $S < K$.

??? success "Solution to Exercise 5"
    We need to show $\lim_{t \to T^-} V(t, S) = (S - K)^+$.

    As $t \to T^-$, we have $\tau = T - t \to 0^+$, so $d_1 = \frac{\log(S/K) + (r + \sigma^2/2)\tau}{\sigma\sqrt{\tau}}$ and $d_2 = d_1 - \sigma\sqrt{\tau}$.

    **Case $S > K$**: $\log(S/K) > 0$, so as $\tau \to 0^+$, $d_1 \to +\infty$ and $d_2 \to +\infty$. Therefore $\mathcal{N}(d_1) \to 1$ and $\mathcal{N}(d_2) \to 1$:

    $$
    V(t, S) \to S \cdot 1 - K \cdot e^0 \cdot 1 = S - K = (S - K)^+ \;\checkmark
    $$

    **Case $S < K$**: $\log(S/K) < 0$, so as $\tau \to 0^+$, $d_1 \to -\infty$ and $d_2 \to -\infty$. Therefore $\mathcal{N}(d_1) \to 0$ and $\mathcal{N}(d_2) \to 0$:

    $$
    V(t, S) \to S \cdot 0 - K \cdot e^0 \cdot 0 = 0 = (S - K)^+ \;\checkmark
    $$

    **Case $S = K$**: $\log(S/K) = 0$, so $d_1 = (r + \sigma^2/2)\sqrt{\tau}/\sigma \to 0^+$ and $d_2 \to 0^-$. Therefore $\mathcal{N}(d_1) \to 1/2$ and $\mathcal{N}(d_2) \to 1/2$:

    $$
    V(t, S) \to K \cdot \frac{1}{2} - K \cdot 1 \cdot \frac{1}{2} = 0 = (K - K)^+ \;\checkmark
    $$

---

**Exercise 6.**
An Asian option has payoff $g = (\frac{1}{T}\int_0^T S_s\,ds - K)^+$. Explain why the standard one-dimensional Feynman-Kac approach is insufficient and an augmented state variable $A_t = \int_0^t S_s\,ds$ is needed. Write the two-dimensional PDE that the option price satisfies.

??? success "Solution to Exercise 6"
    The payoff $g = \left(\frac{1}{T}\int_0^T S_s\,ds - K\right)^+$ depends on the entire path of $S$ through its time-average. The price $V$ at time $t$ depends not only on the current stock price $S_t$ but also on how much of the average has already been accumulated.

    **Why one dimension is insufficient**: The Feynman-Kac formula requires the state to be Markovian. The stock price $S_t$ alone does not determine the value of the Asian option because the accumulated average $\frac{1}{T}\int_0^t S_s\,ds$ is needed. Two scenarios with the same $S_t$ but different past averages have different option values.

    **Augmented state variable**: Define $A_t = \int_0^t S_s\,ds$, so $dA_t = S_t\,dt$. The pair $(S_t, A_t)$ is Markovian, and $V = V(t, S, A)$.

    **Two-dimensional PDE**: Applying the Feynman-Kac formula to the augmented state $(S_t, A_t)$:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + S\frac{\partial V}{\partial A} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    with terminal condition $V(T, S, A) = \left(\frac{A}{T} - K\right)^+$. The $S\,\partial_A V$ term arises from the drift $dA_t = S_t\,dt$ of the auxiliary variable. There is no second-order derivative in $A$ because $A_t$ has no diffusion component.

---

**Exercise 7.**
A digital (binary) barrier option pays $\$1$ if $S_T > K$ and the stock never crosses the barrier $B < K$ during $[0, T]$. Write the Feynman-Kac representation, identify the PDE domain, and describe the terminal and boundary conditions.

??? success "Solution to Exercise 7"
    **Feynman-Kac representation**: The digital barrier option pays $\$1$ if $S_T > K$ and the barrier $B$ is never breached:

    $$
    V(t, S) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(T-t)}\,\mathbf{1}_{\{S_T > K\}}\,\mathbf{1}_{\{\tau_B > T\}} \,\Big|\, S_t = S\right]
    $$

    where $\tau_B = \inf\{s > t : S_s \leq B\}$.

    **PDE domain**: $S \in (B, \infty)$, $t \in [0, T]$. The PDE is the standard Black-Scholes equation on this restricted domain:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0 \quad \text{for } S > B
    $$

    **Terminal condition**: $V(T, S) = \mathbf{1}_{\{S > K\}}$ for $S > B$. This is a step function: $V(T, S) = 1$ if $S > K$, and $V(T, S) = 0$ if $B < S \leq K$.

    **Boundary conditions**:

    - **Knockout at barrier**: $V(t, B) = 0$ for all $t$ (the option is worthless once the barrier is hit)
    - **Far-field**: $V(t, S) \to e^{-r(T-t)}$ as $S \to \infty$ (deep in-the-money digital converges to the discounted $\$1$ payment, and the barrier is irrelevant)
