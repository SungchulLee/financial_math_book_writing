# Discounting and the Killing Term

In financial mathematics, future cash flows must be **discounted** to reflect the time value of money. This discounting enters pricing PDEs through a characteristic **killing term** $-rV$ that has deep probabilistic and analytical interpretations.

---

## The Time Value of Money

A dollar today is worth more than a dollar tomorrow because:
- It can be invested at the risk-free rate $r$
- Inflation erodes purchasing power
- There is uncertainty about future payments

**Continuous discounting**: A cash flow $X$ at time $T$ has present value:

$$
PV = e^{-r(T-t)}X
$$

at time $t < T$.

---

## The Pricing PDE with Discounting

For a diffusion $X_t$ with generator $\mathcal{L}$, the pricing PDE is:

$$
\boxed{
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0
}
$$

The term $-rV$ is called the **killing term** or **discount term**.

---

## Probabilistic Interpretation

### Feynman-Kac Representation

The solution is:

$$
V(t,x) = \mathbb{E}\left[e^{-r(T-t)}\Phi(X_T) \mid X_t = x\right]
$$

The exponential discount factor appears naturally from the killing term.

### Martingale Formulation

Consider the **discounted value process**:

$$
M_s = e^{-r(s-t)}V(s, X_s)
$$

**Claim**: If $V$ solves the pricing PDE, then $M_s$ is a martingale.

**Proof**: Apply Itô's lemma:

$$
dM_s = e^{-r(s-t)}\left[\left(\frac{\partial V}{\partial s} + \mathcal{L}V - rV\right)ds + \sigma\frac{\partial V}{\partial x}dW_s\right]
$$

Since $V$ solves the PDE, the $ds$ term vanishes:

$$
dM_s = e^{-r(s-t)}\sigma\frac{\partial V}{\partial x}dW_s
$$

This is a local martingale. $\square$

---

## The Killed Process Interpretation

The killing term has an alternative interpretation via **killed processes**.

**Definition**: A process is **killed at rate $r$** if it is terminated at a random time $\zeta$ with:

$$
\mathbb{P}(\zeta > t \mid \mathcal{F}_t) = e^{-rt}
$$

**Theorem**: The solution to the pricing PDE equals:

$$
V(t,x) = \mathbb{E}[\Phi(X_T)\mathbf{1}_{\zeta > T} \mid X_t = x]
$$

where $\zeta$ is independent of $X$ with exponential distribution of rate $r$.

**Interpretation**: Discounting is equivalent to a random termination of the contract.

---

## Why "Killing"?

The terminology comes from probability theory:

| Financial Term | Probabilistic Term |
|----------------|-------------------|
| Discount rate $r$ | Killing rate |
| Discounted value | Survival probability weighted value |
| Time value of money | Expected survival time |

In physics, $r$ might represent:
- Decay rate of radioactive particles
- Absorption rate in diffusion
- Death rate in population models

---

## State-Dependent Discounting

More generally, the discount rate can depend on the state:

$$
V(t,x) = \mathbb{E}\left[\exp\left(-\int_t^T r(X_s)\,ds\right)\Phi(X_T) \mid X_t = x\right]
$$

The PDE becomes:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - r(x)V = 0
$$

**Applications**:
- Credit risk: Higher rates for riskier states
- Stochastic interest rates: $r = r(X_t)$
- Intensity-based default models

---

## The Discount Factor Process

Define the **discount factor**:

$$
D(t,T) = \exp\left(-\int_t^T r(s)\,ds\right)
$$

or for state-dependent rates:

$$
D_t^T = \exp\left(-\int_t^T r(X_s)\,ds\right)
$$

**Properties**:
- $D(t,t) = 1$
- $D(t,T) \cdot D(T,S) = D(t,S)$ (multiplicative)
- $dD_t^s/D_t^s = -r(X_t)\,dt$

---

## Zero-Coupon Bond Pricing

A zero-coupon bond paying $1$ at maturity $T$ satisfies:

$$
\frac{\partial P}{\partial t} + \mathcal{L}P - rP = 0, \quad P(T,x) = 1
$$

**Solution**:

$$
P(t,x) = \mathbb{E}\left[e^{-\int_t^T r(X_s)\,ds} \mid X_t = x\right]
$$

For constant $r$: $P(t) = e^{-r(T-t)}$.

---

## Credit Risk and Default

In credit risk models, the killing rate represents **default intensity**:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - (r + \lambda)V = 0
$$

where $\lambda$ is the default intensity.

**Interpretation**:
- Total discount rate = risk-free rate + credit spread
- $\lambda$ represents probability of default per unit time

**Probabilistic representation**:

$$
V(t,x) = \mathbb{E}\left[e^{-\int_t^T (r+\lambda)\,ds}\Phi(X_T) \mid X_t = x\right]
$$

---

## Comparison of Terms

| Term in PDE | Financial Meaning | Mathematical Role |
|-------------|-------------------|-------------------|
| $\frac{\partial V}{\partial t}$ | Time decay | Evolution in time |
| $\mathcal{L}V$ | Market dynamics | Generator of diffusion |
| $-rV$ | Discounting | Killing term |
| $+g$ | Running payoff | Source term |

---

## Effect on Solutions

The killing term $-rV$ causes solutions to **decay** over time:

1. **Without killing** ($r = 0$): $V(t,x) = \mathbb{E}[\Phi(X_T) \mid X_t = x]$

2. **With killing** ($r > 0$): $V(t,x) = e^{-r(T-t)}\mathbb{E}^*[\Phi(X_T) \mid X_t = x]$

where $\mathbb{E}^*$ involves the "survived" paths.

**Maximum principle**: If $\Phi \geq 0$, then $V \geq 0$ (killing preserves positivity).

---

## Numerical Implications

For finite difference methods, the killing term adds a diagonal contribution to the discretization matrix:

$$
\frac{V_j^{n+1} - V_j^n}{\Delta t} = (\mathcal{L}_h V)_j^n - rV_j^n
$$

This typically **improves stability** (makes the system more diagonally dominant).

---

## Summary

$$
\boxed{
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0 \quad \Longleftrightarrow \quad V = \mathbb{E}[e^{-r(T-t)}\Phi(X_T)]
}
$$

| Aspect | Interpretation |
|--------|----------------|
| $-rV$ term | Discounting / killing |
| $e^{-r(T-t)}$ | Discount factor / survival probability |
| $r$ | Risk-free rate / killing rate |
| $r(x)$ | State-dependent discounting |

**The killing term transforms the backward Kolmogorov equation into a pricing equation, encoding the time value of money in the PDE structure.**

---

## Exercises

**Exercise 1.** Consider the Black-Scholes PDE without the killing term: $\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} = 0$. Show that $u(t,S) = \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$ (the undiscounted expectation). Explain why the killing term $-rV$ is necessary to produce the discounted price $V = e^{-r(T-t)} u$.

??? success "Solution to Exercise 1"
    Consider the PDE without the killing term:

    $$
    \frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} = 0
    $$

    with terminal condition $u(T,S) = \Phi(S)$. By the Feynman-Kac theorem, this PDE (which has the form $u_t + \mathcal{L}u = 0$ with no killing term) has the solution:

    $$
    u(t,S) = \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
    $$

    where $S_T$ follows geometric Brownian motion under $\mathbb{Q}$ with drift $r$. This is the **undiscounted** expectation because the PDE has no $-ru$ term.

    Now define $V(t,S) = e^{-r(T-t)} u(t,S)$. Computing the partial derivatives:

    $$
    \frac{\partial V}{\partial t} = e^{-r(T-t)} \frac{\partial u}{\partial t} + r e^{-r(T-t)} u = e^{-r(T-t)} \frac{\partial u}{\partial t} + rV
    $$

    $$
    \frac{\partial V}{\partial S} = e^{-r(T-t)} \frac{\partial u}{\partial S}, \quad \frac{\partial^2 V}{\partial S^2} = e^{-r(T-t)} \frac{\partial^2 u}{\partial S^2}
    $$

    Substituting into the expression $\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV$:

    $$
    = e^{-r(T-t)}\left(\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2}\right) + rV - rV = 0
    $$

    since $u$ solves the original PDE. Therefore $V = e^{-r(T-t)}u$ solves the Black-Scholes PDE with the killing term $-rV$. The killing term is necessary because the no-arbitrage price is the **discounted** expectation $V = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)]$, not the raw expectation.

---
**Exercise 2.** Verify the Feynman-Kac correspondence: the killing term $-rV$ in the PDE corresponds to the discount factor $e^{-r(T-t)}$ in the pricing formula. Show this by defining $F = Ve^{r(T-t)}$ and deriving the PDE satisfied by $F$ (the forward price), confirming that the $-rV$ term vanishes.

??? success "Solution to Exercise 2"
    Define $F(t,S) = V(t,S) e^{r(T-t)}$, so that $V = e^{-r(T-t)}F$. The function $F$ represents the **forward price** of the derivative.

    Computing the derivatives of $V$ in terms of $F$:

    $$
    V = e^{-r(T-t)}F
    $$

    $$
    \frac{\partial V}{\partial t} = e^{-r(T-t)}\frac{\partial F}{\partial t} + re^{-r(T-t)}F = e^{-r(T-t)}\left(\frac{\partial F}{\partial t} + rF\right)
    $$

    $$
    \frac{\partial V}{\partial S} = e^{-r(T-t)}\frac{\partial F}{\partial S}, \quad \frac{\partial^2 V}{\partial S^2} = e^{-r(T-t)}\frac{\partial^2 F}{\partial S^2}
    $$

    Substituting into the Black-Scholes PDE $\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0$:

    $$
    e^{-r(T-t)}\left(\frac{\partial F}{\partial t} + rF + rS\frac{\partial F}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 F}{\partial S^2} - rF\right) = 0
    $$

    The $+rF$ and $-rF$ terms cancel, giving:

    $$
    \frac{\partial F}{\partial t} + rS\frac{\partial F}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 F}{\partial S^2} = 0
    $$

    This is precisely the backward Kolmogorov equation without any killing term. The killing term $-rV$ in the original PDE corresponds exactly to the discount factor $e^{-r(T-t)}$ that connects $V$ and $F$: when we factor out discounting by working with the forward price, the killing term disappears.

---
**Exercise 3.** For a state-dependent killing rate $r(S)$, the PDE becomes $\frac{\partial V}{\partial t} + \mu(S)\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2(S) S^2 \frac{\partial^2 V}{\partial S^2} - r(S) V = 0$. Give a financial interpretation of state-dependent discounting. What type of derivative might naturally feature a killing rate that depends on the underlying price?

??? success "Solution to Exercise 3"
    **State-dependent discounting** means the rate at which future cash flows are discounted varies with the current level of the underlying asset $S$. The PDE:

    $$
    \frac{\partial V}{\partial t} + \mu(S)\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2(S) S^2 \frac{\partial^2 V}{\partial S^2} - r(S) V = 0
    $$

    has solution:

    $$
    V(t,S) = \mathbb{E}\left[\exp\left(-\int_t^T r(S_u)\,du\right)\Phi(S_T) \;\middle|\; S_t = S\right]
    $$

    **Financial interpretation**: The discount rate depends on the state of the economy as proxied by $S$. When $S$ is low (distressed conditions), credit risk is higher, so the effective discount rate increases. When $S$ is high (benign conditions), credit risk is lower.

    **Derivatives with state-dependent killing**: A natural example is a **credit-risky derivative** where the default intensity depends on the firm's asset value or stock price. For instance, consider a corporate bond or a derivative issued by a counterparty whose default hazard rate $\lambda(S)$ is a decreasing function of the stock price:

    $$
    r(S) = r_f + \lambda(S)
    $$

    where $r_f$ is the risk-free rate and $\lambda(S)$ might take the form $\lambda(S) = a \cdot (S_0 / S)^b$ for constants $a, b > 0$, so that default becomes more likely as the stock price declines. **Convertible bonds** also naturally feature state-dependent effective discount rates since the conversion feature creates a payoff whose discounting interacts with the stock price level.

---
**Exercise 4.** Show that the killing term $-rV$ makes the discretized PDE system more diagonally dominant compared to the backward Kolmogorov equation without discounting. Explain why this improves numerical stability for finite difference methods.

??? success "Solution to Exercise 4"
    Consider the semi-discrete scheme for the pricing PDE on a spatial grid $\{S_j\}$:

    $$
    \frac{V_j^{n+1} - V_j^n}{\Delta t} = (\mathcal{L}_h V)_j^n - r V_j^n
    $$

    The discrete generator $\mathcal{L}_h$ applied to $V_j$ using central differences gives:

    $$
    (\mathcal{L}_h V)_j = \frac{1}{2}\sigma^2 S_j^2 \frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2} + r S_j \frac{V_{j+1} - V_{j-1}}{2\Delta S}
    $$

    Collecting terms, the coefficient of $V_j$ from the diffusion term is $-\sigma^2 S_j^2 / (\Delta S)^2$. Adding the killing term $-rV_j$ makes the diagonal coefficient:

    $$
    -\frac{\sigma^2 S_j^2}{(\Delta S)^2} - r
    $$

    Without the killing term, the diagonal coefficient is just $-\sigma^2 S_j^2 / (\Delta S)^2$. The additional $-r$ contribution from the killing term **increases the magnitude of the diagonal entry** by $r$.

    In the implicit scheme, the system matrix $A$ has diagonal entries of the form $1/\Delta t + \sigma^2 S_j^2/(\Delta S)^2 + r$ versus $1/\Delta t + \sigma^2 S_j^2/(\Delta S)^2$ without the killing term. The ratio of diagonal to off-diagonal entries increases, making the matrix **more diagonally dominant**.

    Diagonal dominance guarantees:

    - The matrix is invertible (existence of unique solution at each time step)
    - Iterative solvers (Jacobi, Gauss-Seidel, SOR) converge faster
    - The discrete maximum principle holds, preventing spurious oscillations
    - Stability of both explicit and implicit schemes is improved

    For the explicit scheme, the CFL-type stability condition becomes less restrictive since the additional diagonal damping from $-rV$ suppresses growth of numerical errors.

---
**Exercise 5.** The survival interpretation views $e^{-rT}$ as the probability of "surviving" to time $T$ in a Poisson killing process with rate $r$. Under this interpretation, what is the financial analogue of "being killed"? Connect this to the pricing of defaultable derivatives where the issuer may default with hazard rate $\lambda$.

??? success "Solution to Exercise 5"
    In the Poisson killing interpretation, the process $X_t$ is "killed" at a random exponential time $\zeta \sim \text{Exp}(r)$ independent of $X$. The probability of surviving to time $T$ is:

    $$
    \mathbb{P}(\zeta > T) = e^{-rT}
    $$

    **Financial analogue of "being killed"**: Being killed corresponds to the contract **becoming worthless** before maturity. In the pure discounting context, this is an abstract device: the killing reweights paths by $e^{-rT}$, which is equivalent to discounting. There is no literal "death" of the contract.

    However, in **credit risk**, the analogy becomes concrete. Consider a derivative issued by a counterparty who may **default** with hazard rate $\lambda$. The default time $\tau_d \sim \text{Exp}(\lambda)$ plays the role of the killing time. The pricing PDE becomes:

    $$
    \frac{\partial V}{\partial t} + \mathcal{L}V - (r + \lambda)V = 0
    $$

    The total killing rate $r + \lambda$ consists of two components:

    - $r$: time-value-of-money discounting (abstract killing)
    - $\lambda$: actual default risk (literal killing of the contract)

    The Feynman-Kac representation is:

    $$
    V(t,S) = \mathbb{E}\left[e^{-(r+\lambda)(T-t)}\Phi(S_T) \mid S_t = S\right]
    $$

    Here $e^{-\lambda(T-t)}$ is the survival probability (probability the issuer does not default before $T$), and $e^{-r(T-t)}$ is the discount factor. Being "killed" financially means the **issuer defaults**, rendering the derivative worthless (assuming zero recovery). For nonzero recovery rate $R$, the payoff upon killing is $R \cdot V$ rather than zero, and the PDE includes an additional source term $\lambda R V$, modifying the effective killing rate to $r + \lambda(1-R)$.
