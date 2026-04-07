# Terminal and Boundary Conditions

A PDE alone does not determine a unique solution. **Terminal conditions** and **boundary conditions** encode the specific features of financial contracts, transforming abstract mathematics into concrete pricing tools.

---

## Why Conditions Matter

The Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
$$

has infinitely many solutions. The conditions select the **unique solution** corresponding to a specific contract.

Because the Black-Scholes PDE is **parabolic** and solved backward in time (from known payoff at $T$ toward the present), it requires a **terminal** condition rather than an initial condition. This is the reverse of the heat equation in physics, where the initial temperature is known and the solution evolves forward. In finance, the payoff at maturity is the known quantity, and the price is computed by working backward.

---

## Terminal Conditions

### Definition

At maturity $t = T$, the option value equals its **payoff**:

$$
\boxed{
V(T, S) = \Phi(S)
}
$$

The function $\Phi$ is determined by the contract.

### Common Payoffs

| Option Type | Payoff $\Phi(S)$ | Description |
|-------------|------------------|-------------|
| Call | $(S - K)^+$ | Right to buy at $K$ |
| Put | $(K - S)^+$ | Right to sell at $K$ |
| Digital call | $\mathbf{1}_{S > K}$ | Pays 1 if $S > K$ |
| Digital put | $\mathbf{1}_{S < K}$ | Pays 1 if $S < K$ |
| Straddle | $|S - K|$ | Long call + long put |
| Strangle | $(S-K_2)^+ + (K_1-S)^+$ | OTM call + OTM put |

### Regularity

The terminal condition may be:
- **Continuous**: Most standard options
- **Discontinuous**: Digital options (jumps at strike)
- **Non-smooth**: Calls and puts (kink at strike)

The PDE solution **smooths** these irregularities for $t < T$.

---

## Boundary Conditions in Space

### Types of Boundary Conditions

**1. Dirichlet Conditions** (value specified):

$$
V(t, S^*) = g(t)
$$

The option value is specified at boundary $S = S^*$.

**2. Neumann Conditions** (derivative specified):

$$
\frac{\partial V}{\partial S}(t, S^*) = h(t)
$$

The delta is specified at the boundary.

**3. Robin (Mixed) Conditions**:

$$
\alpha V + \beta\frac{\partial V}{\partial S} = g(t)
$$

A linear combination is specified.

---

## Boundary Conditions for Standard Options

### As S → 0

**Call option**: The call is worthless if the stock goes to zero:

$$
V(t, 0) = 0
$$

**Put option**: The put has maximum value:

$$
V(t, 0) = Ke^{-r(T-t)}
$$

(Present value of receiving $K$ at maturity)

### As S → ∞

**Call option**: As $S \to \infty$, $d_1, d_2 \to +\infty$ so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$, giving:

$$
V(t, S) \sim S \cdot 1 - Ke^{-r(T-t)} \cdot 1 = S - Ke^{-r(T-t)} \quad \text{as } S \to \infty
$$

The deep ITM call behaves like a forward contract, with $\Delta \to 1$.

**Put option**: Worthless for large $S$:

$$
V(t, S) \to 0 \quad \text{as } S \to \infty
$$

---

## Barrier Options

Barrier options have **explicit boundaries** where the contract terminates.

### Down-and-Out Call

Knocked out if $S$ hits barrier $B < S_0$:

$$
\begin{cases}
V(T, S) = (S - K)^+ & S > B \\
V(t, B) = 0 & \text{(knocked out)}
\end{cases}
$$

### Up-and-Out Put

Knocked out if $S$ hits barrier $B > S_0$:

$$
\begin{cases}
V(T, S) = (K - S)^+ & S < B \\
V(t, B) = 0 & \text{(knocked out)}
\end{cases}
$$

### Knock-In Options

The complementary "knock-in" satisfies:

$$
V_{\text{knock-in}} + V_{\text{knock-out}} = V_{\text{vanilla}}
$$

---

## Probabilistic Interpretation

Boundary conditions correspond to **stopping rules** for the underlying process.

### Dirichlet at S = B

$$
V(t, S) = \mathbb{E}\left[e^{-r(\tau \wedge T - t)}\Phi(S_{\tau \wedge T}) \mid S_t = S\right]
$$

where $\tau = \inf\{s \geq t : S_s = B\}$ is the hitting time.

### Absorbing Boundary

When the process hits the boundary, it is **killed**:

$$
\mathbb{P}(\text{survive to } T \mid S_t = S) = \mathbb{P}(\tau > T \mid S_t = S)
$$

### Reflecting Boundary

The process is **pushed back** at the boundary:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t + dL_t
$$

where $L_t$ is the local time at the boundary.

---

## American Options and Free Boundaries

American options introduce a **free boundary** (exercise boundary).

### Optimal Stopping Problem

$$
V(t, S) = \sup_{\tau \in [t,T]} \mathbb{E}\left[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S\right]
$$

### Complementarity Formulation

The exercise decision divides the $(t,S)$-plane into two regions: a **continuation region** where the PDE holds as an equality, and an **exercise region** where $V = \Phi$. At any point, exactly one of these conditions is active. This structure is compactly expressed as a complementarity problem — the American option price satisfies:

$$
\begin{cases}
\frac{\partial V}{\partial t} + \mathcal{L}V - rV \leq 0 \\
V \geq \Phi \\
\left(\frac{\partial V}{\partial t} + \mathcal{L}V - rV\right)(V - \Phi) = 0
\end{cases}
$$

This is a **free boundary problem**: the exercise boundary $S^*(t)$ is part of the solution.

### Exercise Boundary

For an American put:
- $V(t, S) = K - S$ for $S < S^*(t)$ (immediate exercise)
- $V(t, S) > K - S$ for $S > S^*(t)$ (hold)

The boundary $S^*(t)$ must be determined as part of solving the problem.

---

## Well-Posedness

A problem is **well-posed** if:

1. **Existence**: A solution exists
2. **Uniqueness**: Only one solution exists
3. **Stability**: Solution depends continuously on data

### For Pricing PDEs

With appropriate terminal and boundary conditions:
- **Existence**: Feynman-Kac provides probabilistic solution
- **Uniqueness**: Maximum principle ensures uniqueness
- **Stability**: Comparison principle gives continuous dependence

---

## Numerical Considerations

### Grid Truncation

Numerical methods require finite domains. Far-field boundaries are placed at $S_{\min}$ and $S_{\max}$ where:

$$
S_{\min} \ll K \ll S_{\max}
$$

### Boundary Condition Errors

Incorrect boundary conditions cause errors that propagate inward. Use:
- Asymptotic analysis for far-field behavior
- Sufficiently large domain
- Absorbing boundary conditions

---

## Summary

| Condition Type | Mathematical Form | Financial Meaning |
|----------------|-------------------|-------------------|
| Terminal | $V(T,S) = \Phi(S)$ | Payoff at maturity |
| Dirichlet | $V(t,B) = g(t)$ | Barrier, knockout |
| Neumann | $V_S(t,B) = h(t)$ | Delta constraint |
| Free boundary | $V = \Phi$ on $S^*(t)$ | Optimal exercise |

$$
\boxed{
\text{PDE} + \text{Terminal Condition} + \text{Boundary Conditions} = \text{Unique Price}
}
$$

**Terminal and boundary conditions transform abstract PDEs into specific pricing problems, encoding the contractual features of financial derivatives.**

---

## Exercises

**Exercise 1.** Write down the terminal condition and boundary conditions (as $S \to 0$ and $S \to \infty$) for a European put option with strike $K$ and maturity $T$. Verify that the boundary conditions are consistent with the put-call parity relation.

??? success "Solution to Exercise 1"
    **Terminal condition**: At maturity $t = T$:

    $$
    V(T, S) = (K - S)^+
    $$

    **Boundary condition as $S \to 0$**: When the stock price goes to zero, the put is deep in the money and will certainly be exercised. The present value of the payoff $K$ received at time $T$ is:

    $$
    V(t, 0) = Ke^{-r(T-t)}
    $$

    **Boundary condition as $S \to \infty$**: For very large $S$, the put is deep out of the money and worthless:

    $$
    V(t, S) \to 0 \quad \text{as } S \to \infty
    $$

    **Consistency with put-call parity**: Put-call parity states $C - P = S - Ke^{-r(T-t)}$, so $P = C - S + Ke^{-r(T-t)}$.

    As $S \to 0$: $C \to 0$ (call is worthless), so $P \to -0 + Ke^{-r(T-t)} = Ke^{-r(T-t)}$. This matches our boundary condition.

    As $S \to \infty$: $C \sim S - Ke^{-r(T-t)}$, so $P \sim (S - Ke^{-r(T-t)}) - S + Ke^{-r(T-t)} = 0$. This matches.

    At $t = T$: $C(T,S) - P(T,S) = (S-K)^+ - (K-S)^+ = S - K$, and $S - Ke^{0} = S - K$. Consistent.

---
**Exercise 2.** For a down-and-out call with barrier $B < K$, the option is worthless if $S$ ever touches $B$. Write down the complete set of conditions: terminal condition at $t = T$, Dirichlet boundary condition at $S = B$, and behavior as $S \to \infty$. Explain why the far-field condition $V \sim S - Ke^{-r(T-t)}$ as $S \to \infty$ is appropriate.

??? success "Solution to Exercise 2"
    For a down-and-out call with barrier $B < K$:

    **Terminal condition** at $t = T$ (for $S > B$):

    $$
    V(T, S) = (S - K)^+
    $$

    **Dirichlet boundary condition** at $S = B$:

    $$
    V(t, B) = 0 \quad \text{for all } t \in [0, T]
    $$

    This encodes the knock-out feature: the option becomes worthless the moment $S$ touches $B$.

    **Far-field condition** as $S \to \infty$:

    $$
    V(t, S) \sim S - Ke^{-r(T-t)} \quad \text{as } S \to \infty
    $$

    **Why this far-field condition is appropriate**: When $S \gg B$, the probability that the stock price will ever reach the barrier $B$ before maturity becomes negligible. Therefore the knock-out feature has virtually no value, and the down-and-out call behaves like a vanilla call. For a deep-in-the-money vanilla call, $V \sim S - Ke^{-r(T-t)}$ (the forward value, since $\Phi(d_1) \to 1$ and $\Phi(d_2) \to 1$ as $S \to \infty$). Formally, $\mathbb{P}(\min_{t \leq s \leq T} S_s < B \mid S_t = S) \to 0$ exponentially as $S/B \to \infty$.

---
**Exercise 3.** The American put has a free boundary $S^*(t)$ separating the exercise and continuation regions. State the smooth-pasting conditions at $S = S^*(t)$ and explain their financial interpretation. Why are two conditions (value matching and smooth pasting) needed at the free boundary?

??? success "Solution to Exercise 3"
    At the free boundary $S = S^*(t)$, the American put satisfies two **smooth-pasting conditions**:

    **Value matching** (continuity of $V$):

    $$
    V(t, S^*(t)) = K - S^*(t)
    $$

    The option value equals the exercise payoff at the boundary.

    **Smooth pasting** (continuity of $V_S$):

    $$
    \frac{\partial V}{\partial S}(t, S^*(t)) = -1
    $$

    The delta of the option equals the delta of the payoff at the boundary.

    **Financial interpretation of value matching**: At the exercise boundary, the holder is indifferent between exercising (receiving $K - S$) and continuing to hold. If $V > K - S$, it is better to hold; if $V = K - S$, exercising is optimal.

    **Financial interpretation of smooth pasting**: The option's sensitivity to the stock price transitions smoothly into the payoff's sensitivity. If the delta were discontinuous at $S^*(t)$, a small perturbation of the stock price would create a discrete jump in value, which would generate an arbitrage opportunity.

    **Why two conditions are needed**: The PDE in the continuation region $S > S^*(t)$ is a second-order equation that requires boundary data to determine its solution. But the boundary location $S^*(t)$ is itself unknown. We have two unknowns at the boundary: the solution value and the boundary position. Value matching provides one equation; smooth pasting provides the second. Together, they uniquely determine both $V$ and $S^*(t)$. This is the hallmark of a **free boundary problem**: the extra unknown (boundary location) requires an extra condition (smooth pasting) beyond what a fixed-boundary problem needs.

---
**Exercise 4.** For a finite-difference implementation on a truncated domain $[0, S_{\max}]$, discuss the effect of choosing $S_{\max}$ too small. What type of error does this introduce, and how does the error propagate inward from the boundary? Provide a rule of thumb for choosing $S_{\max}$ in terms of $K$ and $\sigma\sqrt{T}$.

??? success "Solution to Exercise 4"
    Choosing $S_{\max}$ too small introduces **boundary truncation error**. The artificial boundary condition imposed at $S_{\max}$ (typically $V(t, S_{\max}) = S_{\max} - Ke^{-r(T-t)}$ for a call) is only an approximation to the true asymptotic behavior.

    **Type of error**: The error is a **systematic bias** that contaminates the numerical solution in the interior of the domain. For a call option, if $S_{\max}$ is too small, the imposed boundary condition overestimates or underestimates the true option value at $S_{\max}$, since the asymptotic formula $V \sim S - Ke^{-r(T-t)}$ is only accurate for $S \gg K$.

    **Error propagation**: The error propagates **inward from the boundary** through the diffusion mechanism of the PDE. Over each time step, the influence of the boundary error spreads by approximately $\sigma S \sqrt{\Delta t}$ in the $S$-direction. Over the full time horizon $T$, the contaminated region extends roughly $\sigma S_{\max} \sqrt{T}$ inward from the boundary. For a parabolic PDE, the maximum principle ensures that boundary errors do not amplify, but they can still significantly affect the solution near the boundary if the domain is too small.

    **Rule of thumb**: A common choice is:

    $$
    S_{\max} \approx K \cdot \exp\left(c \cdot \sigma\sqrt{T}\right)
    $$

    where $c \in [3, 5]$. This ensures the boundary is several standard deviations away from the strike, making the probability of the stock reaching $S_{\max}$ negligible. For example, with $c = 4$:

    $$
    S_{\max} \approx K \cdot e^{4\sigma\sqrt{T}}
    $$

    For typical parameters ($\sigma = 0.3$, $T = 1$), this gives $S_{\max} \approx 3.3K$. A simpler rule often used in practice is $S_{\max} = 3K$ to $5K$, depending on the desired accuracy and the volatility level.

---
**Exercise 5.** A Neumann boundary condition $\frac{\partial V}{\partial S}\big|_{S=B} = h(t)$ constrains the delta at the boundary. Give a financial example where such a condition arises naturally, and explain how it differs from a Dirichlet condition in terms of the information it encodes about the derivative contract.

??? success "Solution to Exercise 5"
    **Financial example**: A Neumann condition arises naturally in **capped options** or **options with a delta constraint**. Consider a derivative that, at a boundary $S = B$, is contractually required to have a fixed delta. For instance, a **cliquet option** or a structured product might specify that the participation rate (delta) at certain levels is fixed.

    A more concrete example is a **power option** or **leveraged note** where the payoff structure imposes $V_S(t, B) = h$ at a barrier. Another natural occurrence is at a **reflecting boundary**: if the underlying is modeled with a reflecting barrier at $S = B$ (e.g., an exchange rate under a central bank floor), the reflecting condition translates mathematically to a Neumann condition $V_S(t, B) = 0$.

    **Difference from Dirichlet**: A Dirichlet condition $V(t,B) = g(t)$ specifies the **price** of the derivative at the boundary. This encodes information about **what the contract is worth** when the underlying reaches $B$ (e.g., a knockout event where the value drops to zero). A Neumann condition $V_S(t,B) = h(t)$ specifies the **hedge ratio** at the boundary, encoding information about **how the contract responds to price changes** at that level, without directly constraining its value.

    In terms of information content: Dirichlet constrains the zeroth-order behavior (level), while Neumann constrains the first-order behavior (slope). Dirichlet is typical for barrier options (the value is known at knockout). Neumann is typical for regularity or symmetry conditions and for reflecting boundaries, where the physical setup determines the gradient rather than the value.

---
**Exercise 6.** Show that the terminal condition $V(T,S) = (S - K)^+$ is not differentiable at $S = K$. Discuss the implications for the PDE solution at $t = T$: is $V(t,S)$ smooth for $t < T$ even though the terminal data is not? Relate this to the smoothing property of the heat equation.

??? success "Solution to Exercise 6"
    The terminal condition $\Phi(S) = (S-K)^+$ can be written as:

    $$
    \Phi(S) = \begin{cases} 0 & \text{if } S < K \\ S - K & \text{if } S \geq K \end{cases}
    $$

    **Non-differentiability at $S = K$**: The left derivative and right derivative at $S = K$ are:

    $$
    \Phi'(K^-) = \lim_{S \to K^-} \frac{\Phi(S) - \Phi(K)}{S - K} = \lim_{S \to K^-} \frac{0 - 0}{S - K} = 0
    $$

    $$
    \Phi'(K^+) = \lim_{S \to K^+} \frac{(S - K) - 0}{S - K} = 1
    $$

    Since $\Phi'(K^-) = 0 \neq 1 = \Phi'(K^+)$, the function is not differentiable at $S = K$. There is a "kink" where the payoff transitions from flat to linear.

    **Smoothness for $t < T$**: Despite the non-smooth terminal data, the PDE solution $V(t,S)$ is **infinitely differentiable** ($C^\infty$) for all $t < T$. This is the **smoothing property** of parabolic equations.

    To see why, perform the standard change of variables $x = \ln(S/K)$, $\tau = T - t$, which transforms the Black-Scholes PDE into the heat equation:

    $$
    \frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \text{(lower-order terms)}
    $$

    The heat equation has the fundamental solution (heat kernel):

    $$
    G(x, \tau) = \frac{1}{\sqrt{2\pi\sigma^2\tau}} \exp\left(-\frac{x^2}{2\sigma^2\tau}\right)
    $$

    The solution is the convolution $u(\tau, x) = \int G(x - y, \tau)\, \Phi(e^y K)\, dy$. Since $G$ is a Gaussian (smooth in $x$ for any $\tau > 0$), convolution with $G$ produces a smooth function regardless of how rough the initial data $\Phi$ is. The Gaussian kernel "smears out" any kinks or discontinuities instantaneously.

    Financially, for $t < T$ there is always some time remaining, so the probability distribution of $S_T$ given $S_t$ is a smooth lognormal density. This smooths the expected payoff. Only at $t = T$ (zero time remaining) does the distribution collapse to a point mass, and the kink in the payoff reappears. In terms of the Greeks, $\Delta = \Phi(d_1)$ is smooth for $t < T$ but converges to a step function as $t \to T$.
