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
