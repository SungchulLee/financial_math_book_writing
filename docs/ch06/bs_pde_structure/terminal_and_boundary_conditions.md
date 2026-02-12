# Terminal and Boundary Conditions

A PDE alone does not determine a unique solution. **Terminal conditions** and **boundary conditions** encode the specific features of financial contracts, transforming abstract mathematics into concrete pricing tools.

---

## Why Conditions Matter

The Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
$$

has infinitely many solutions. The conditions select the **unique solution** corresponding to a specific contract.

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

### As $S \to 0$

**Call option**: The call is worthless if the stock goes to zero:

$$
V(t, 0) = 0
$$

**Put option**: The put has maximum value:

$$
V(t, 0) = Ke^{-r(T-t)}
$$

(Present value of receiving $K$ at maturity)

### As $S \to \infty$

**Call option**: Behaves like the forward:

$$
V(t, S) \sim S - Ke^{-r(T-t)} \quad \text{as } S \to \infty
$$

Equivalently: $V_S \to 1$ (delta approaches 1).

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

### Dirichlet at $S = B$

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

The American option price satisfies:

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
