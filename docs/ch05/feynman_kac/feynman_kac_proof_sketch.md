# Proof Sketch of the Feynman-Kac Formula

The Feynman-Kac formula connects PDE solutions to stochastic expectations. This page presents a **detailed proof sketch** of both directions: starting from the PDE and arriving at the expectation formula, and starting from the expectation and deriving the PDE. The core technique is Ito's lemma applied to a carefully constructed process that becomes a martingale.

!!! tip "Related Content"
    - [Feynman-Kac Formula](feynman_kac_formula.md) -- statement and applications
    - [Discounted Feynman-Kac](discounted_feynman_kac.md) -- extension with discounting
    - [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md) -- the special case $r = 0$

---

## Setup

### The SDE

$$
dX_s = \mu(s, X_s)\,ds + \sigma(s, X_s)\,dW_s, \quad X_t = x
$$

on $[t, T]$, where $(t, x)$ is the initial condition.

### The PDE

$$
\frac{\partial u}{\partial t} + \mu(t,x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2 u}{\partial x^2} - r(t,x)\,u = 0
$$

with terminal condition $u(T, x) = g(x)$.

In compact notation:

$$
\partial_t u + \mathcal{L}u - r\,u = 0, \quad u(T, \cdot) = g
$$

where $\mathcal{L} = \mu\,\partial_x + \frac{1}{2}\sigma^2\,\partial_{xx}$ is the infinitesimal generator.

### The Claimed Representation

$$
u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(s, X_s)\,ds}\,g(X_T) \,\Big|\, X_t = x\right]
$$

---

## Direction 1: PDE Solution Implies Expectation Formula

**Given**: $u$ is a smooth ($C^{1,2}$) solution of the PDE.

**Goal**: Show $u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(s, X_s)\,ds}\,g(X_T) \mid X_t = x\right]$.

### Step 1: Define the Discount Factor

Let:

$$
D(t, s) = e^{-\int_t^s r(\tau, X_\tau)\,d\tau}
$$

This is the **stochastic discount factor** from time $t$ to time $s$. Note that:

$$
dD(t, s) = -r(s, X_s)\,D(t, s)\,ds
$$

!!! note "Why Stochastic Discounting?"
    The discount factor $D(t,s)$ depends on the path of $X$ through the rate function $r(s, X_s)$. When $r$ is constant, $D(t,s) = e^{-r(s-t)}$ and the discounting is deterministic.

### Step 2: Apply Ito's Lemma to the Discounted Solution

Define the process:

$$
Y_s = D(t, s)\,u(s, X_s), \quad s \in [t, T]
$$

By the **product rule for Ito processes**:

$$
dY_s = D(t,s)\,du(s, X_s) + u(s, X_s)\,dD(t,s)
$$

(The cross-variation $d[D, u]$ is zero because $D$ has no Brownian component -- it is adapted but driven only by $ds$.)

**Expanding $du$** via Ito's lemma:

$$
du(s, X_s) = \left(\frac{\partial u}{\partial s} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right)ds + \sigma\frac{\partial u}{\partial x}\,dW_s
$$

**Expanding $dD$:**

$$
dD(t, s) = -r(s, X_s)\,D(t,s)\,ds
$$

### Step 3: Substitute and Simplify

$$
dY_s = D(t,s)\!\left[\frac{\partial u}{\partial s} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right]ds + D(t,s)\,\sigma\frac{\partial u}{\partial x}\,dW_s - r\,D(t,s)\,u\,ds
$$

Combine the $ds$ terms:

$$
dY_s = D(t,s)\!\left[\frac{\partial u}{\partial s} + \mathcal{L}u - r\,u\right]ds + D(t,s)\,\sigma\frac{\partial u}{\partial x}\,dW_s
$$

### Step 4: Apply the PDE

Since $u$ solves $\partial_t u + \mathcal{L}u - ru = 0$, the $ds$ coefficient **vanishes**:

$$
\boxed{
dY_s = D(t,s)\,\sigma(s, X_s)\frac{\partial u}{\partial x}(s, X_s)\,dW_s
}
$$

**The discounted solution process $Y_s$ is a local martingale** (it has no drift term -- only a stochastic integral against $dW$).

!!! note "This Is the Key Step"
    The PDE is precisely the condition that eliminates the drift from $Y_s$. This is not a coincidence: the Feynman-Kac PDE is *designed* so that the discounted solution is a martingale. This is the analytical expression of the fundamental theorem of asset pricing.

### Step 5: From Local Martingale to Martingale

Under suitable integrability conditions (e.g., $u$ and its derivatives have polynomial growth, and $\sigma$ satisfies linear growth), the stochastic integral $\int_t^s D\,\sigma\,u_x\,dW$ is a true martingale, not merely a local martingale.

!!! warning "Where Regularity Matters"
    This step is where the regularity assumptions are essential. If $\sigma u_x$ grows too fast, the stochastic integral may only be a local martingale, and the expectation argument below fails. Sufficient conditions include:

    - $u$ has at most polynomial growth in $x$
    - $\sigma$ satisfies a linear growth condition
    - $r$ is bounded below

### Step 6: Take Expectations

Since $Y_s$ is a martingale on $[t, T]$:

$$
Y_t = \mathbb{E}[Y_T \mid \mathcal{F}_t]
$$

**At $s = t$**: $Y_t = D(t, t)\,u(t, X_t) = 1 \cdot u(t, x) = u(t, x)$

**At $s = T$**: $Y_T = D(t, T)\,u(T, X_T) = e^{-\int_t^T r\,d\tau}\,g(X_T)$

Therefore:

$$
\boxed{
u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(s, X_s)\,ds}\,g(X_T) \,\Big|\, X_t = x\right]
}
$$

$\square$

---

## Direction 2: Expectation Defines a PDE Solution

**Given**: Define $u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(s, X_s)\,ds}\,g(X_T) \mid X_t = x\right]$.

**Goal**: Show $u$ satisfies the PDE $\partial_t u + \mathcal{L}u - ru = 0$.

### Step 1: Markov Property

By the Markov property of $X_t$:

$$
u(s, X_s) = \mathbb{E}\!\left[e^{-\int_s^T r(\tau, X_\tau)\,d\tau}\,g(X_T) \,\Big|\, \mathcal{F}_s\right]
$$

Therefore the process:

$$
M_s = D(t, s)\,u(s, X_s) = e^{-\int_t^s r\,d\tau}\,\mathbb{E}\!\left[e^{-\int_s^T r\,d\tau}\,g(X_T) \,\Big|\, \mathcal{F}_s\right]
$$

equals $\mathbb{E}\!\left[e^{-\int_t^T r\,d\tau}\,g(X_T) \mid \mathcal{F}_s\right]$, which is a martingale by the tower property.

### Step 2: Apply Ito's Lemma

Assuming $u$ is $C^{1,2}$ (which requires regularity theory -- this is the hard part), apply Ito's lemma to $M_s = D(t,s)\,u(s, X_s)$:

$$
dM_s = D(t,s)\!\left[\partial_s u + \mathcal{L}u - r\,u\right]ds + D(t,s)\,\sigma\,u_x\,dW_s
$$

### Step 3: Martingale Condition

Since $M_s$ is a martingale, the $ds$ coefficient must be zero:

$$
\partial_s u + \mathcal{L}u - r\,u = 0
$$

at every point $(s, x)$ where $u$ is smooth. $\square$

!!! info "Classical vs Viscosity Solutions"
    Direction 2 requires $u$ to be $C^{1,2}$, which may fail if:

    - The terminal condition $g$ is non-smooth (e.g., $(x-K)^+$)
    - The coefficients degenerate ($\sigma(x) = 0$ at some points)

    In such cases, $u$ is a **viscosity solution** of the PDE -- a weaker notion that does not require differentiability but still ensures uniqueness.

---

## Summary of the Proof Logic

```
Direction 1 (PDE → Expectation):

u solves PDE  ──Itô's lemma──▶  D(t,s)·u(s,Xₛ) is a martingale
                                        │
                                 E[Y_T | ℱ_t] = Y_t
                                        │
                                        ▼
                           u(t,x) = E[D(t,T)·g(X_T)]


Direction 2 (Expectation → PDE):

u(t,x) = E[D·g]  ──Markov──▶  D(t,s)·u(s,Xₛ) is a martingale
                                        │
                                 Itô: drift must vanish
                                        │
                                        ▼
                           ∂ₜu + ℒu - ru = 0
```

---

## Where Each Assumption Is Used

| Assumption | Used In | Purpose |
|---|---|---|
| $\mu, \sigma$ Lipschitz | SDE existence | Ensures $X_t$ exists and is unique |
| $u \in C^{1,2}$ | Ito's lemma | Justifies the chain rule for $u(s, X_s)$ |
| $\sigma u_x$ integrability | Step 5 (Dir. 1) | Promotes local martingale to true martingale |
| $g$ continuous, polynomial growth | Terminal condition | Ensures $u$ is well-defined |
| $r$ bounded below | Discounting | Prevents $D(t,T)$ from exploding |
| Markov property | Step 1 (Dir. 2) | Allows $u$ to depend only on $(s, X_s)$ |

---

## The Special Case $r = 0$ (Kolmogorov Backward)

When $r \equiv 0$, the Feynman-Kac formula reduces to:

$$
u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]
$$

and the PDE becomes the **Kolmogorov backward equation**:

$$
\partial_t u + \mathcal{L}u = 0, \quad u(T, x) = g(x)
$$

The proof simplifies: $Y_s = u(s, X_s)$ is directly a martingale (no discounting needed), and Ito's lemma gives:

$$
du(s, X_s) = (\partial_s u + \mathcal{L}u)\,ds + \sigma u_x\,dW_s
$$

The PDE forces the drift to vanish, so $u(s, X_s)$ is a martingale. Taking expectations: $u(t, x) = \mathbb{E}[u(T, X_T)] = \mathbb{E}[g(X_T)]$.

---

## The Martingale Interpretation

The proof reveals a deep structural insight:

$$
\boxed{
u \text{ solves the Feynman-Kac PDE} \quad \Longleftrightarrow \quad D(t,s)\,u(s, X_s) \text{ is a martingale}
}
$$

This equivalence is the mathematical core of **risk-neutral pricing**:

- **PDE perspective**: The option price satisfies a deterministic equation
- **Martingale perspective**: The discounted option price is a martingale under the risk-neutral measure
- **Feynman-Kac**: These are the same statement

In finance, the risk-free rate $r$ serves as both the discounting rate in the expectation and the coefficient in the PDE. The no-arbitrage condition (that discounted prices are martingales) is exactly the Feynman-Kac PDE.

---

## Extension: Running Payoff

When there is a source term $f(s, X_s)$ (running payoff), the PDE becomes:

$$
\partial_t u + \mathcal{L}u - ru + f = 0
$$

and the representation is:

$$
u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r\,ds}\,g(X_T) + \int_t^T e^{-\int_t^s r\,d\tau}\,f(s, X_s)\,ds \,\Big|\, X_t = x\right]
$$

The proof proceeds identically, except the process:

$$
Y_s = D(t,s)\,u(s, X_s) + \int_t^s D(t, \tau)\,f(\tau, X_\tau)\,d\tau
$$

is the martingale. The $-f$ from the PDE cancels the $+f$ from the integral term. See [Feynman-Kac Formula](feynman_kac_formula.md) for details.

---

## Summary

| Step | Direction 1 (PDE $\to$ Expectation) | Direction 2 (Expectation $\to$ PDE) |
|---|---|---|
| **Start** | $u$ solves PDE | $u(t,x) = \mathbb{E}[D \cdot g]$ |
| **Key tool** | Ito's lemma on $D \cdot u$ | Markov property + Ito's lemma |
| **Core argument** | PDE $\Rightarrow$ drift vanishes $\Rightarrow$ martingale | Martingale $\Rightarrow$ drift vanishes $\Rightarrow$ PDE |
| **Conclusion** | $u(t,x) = \mathbb{E}[D \cdot g]$ | $\partial_t u + \mathcal{L}u - ru = 0$ |
| **Regularity** | Needs integrability for true martingale | Needs $C^{1,2}$ for Ito |

**The Feynman-Kac proof is fundamentally a martingale argument: the PDE is the condition that makes the discounted solution process driftless, and driftless processes are martingales, whose values at different times are related by conditional expectations.**

---

## See Also

- [Feynman-Kac Formula](feynman_kac_formula.md) -- full statement with applications
- [Discounted Feynman-Kac](discounted_feynman_kac.md) -- the discounting/killing extension
- [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md) -- the $r = 0$ special case
- [Applications to Option Pricing](feynman_kac_option_pricing.md) -- financial applications

---

## Exercises

**Exercise 1.**
In Direction 1 (PDE to Expectation), the key step is showing that $Y_s = D(t,s)\,u(s, X_s)$ is a martingale when $u$ solves the PDE. Apply Ito's lemma to $D(t,s)\,u(s, X_s)$ for constant $r$ and verify that the drift vanishes when $\partial_t u + \mathcal{L}u - ru = 0$.

---

**Exercise 2.**
In Direction 2 (Expectation to PDE), the starting point is $u(t,x) = \mathbb{E}[D(t,T)g(X_T) | X_t = x]$. Using the Markov property, show that $u(t, X_t)$ can be expressed as a conditional expectation and hence $D(t,s)u(s, X_s)$ is a martingale. Conclude that the drift of this process must be zero.

---

**Exercise 3.**
In the proof, the integrability condition ensures that the local martingale $Y_s$ is a true martingale. Give an example where the stochastic integral $\int_t^s D\,\sigma\,u_x\,dW$ might fail to be a true martingale, and explain the consequence for the Feynman-Kac representation.

---

**Exercise 4.**
For the case $r = 0$ and $f = 0$, the Feynman-Kac proof simplifies to showing that $u(s, X_s)$ is a martingale. Carry out this simplified proof for $dX_s = \sigma\,dW_s$ and $g(x) = x^2$, verifying each step explicitly.

---

**Exercise 5.**
The running payoff extension involves the process $Y_s = D(t,s)u(s,X_s) + \int_t^s D(t,\tau)f(\tau, X_\tau)\,d\tau$. Show that the $+f$ from the integral and the $-f$ from the PDE cancel in the drift of $Y_s$, leaving $Y_s$ as a martingale.

---

**Exercise 6.**
Explain why the Feynman-Kac proof requires $u \in C^{1,2}$ (once differentiable in $t$, twice in $x$). What goes wrong with the Ito lemma application if $u$ is only continuous? In this case, what weaker concept of solution (viscosity solution) can be used?

---

**Exercise 7.**
Summarize the Feynman-Kac proof in one sentence for each of the five steps: (1) define the process, (2) apply Ito's lemma, (3) use the PDE, (4) conclude martingale property, (5) evaluate at boundary times. Then explain why step (3) is the crucial one that connects the PDE to probability.
