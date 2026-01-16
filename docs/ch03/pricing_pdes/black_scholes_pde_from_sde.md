# The Black-Scholes PDE from SDE

The **Black-Scholes PDE** is the cornerstone of modern derivatives pricing. This section derives the PDE from the underlying stochastic dynamics, establishes its connection to risk-neutral pricing, and explores its solutions.

---

## Stock Price Dynamics

Assume the stock price follows **geometric Brownian motion** under the physical measure $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where:
- $\mu$: expected return (drift)
- $\sigma$: volatility
- $W_t$: standard Brownian motion

---

## Risk-Neutral Dynamics

Under the **risk-neutral measure** $\mathbb{Q}$, the stock price satisfies:

$$
\boxed{
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
}
$$

where:
- $r$: risk-free interest rate
- $W_t^{\mathbb{Q}}$: Brownian motion under $\mathbb{Q}$

**Key insight**: The drift changes from $\mu$ to $r$, but volatility $\sigma$ remains the same.

---

## The Infinitesimal Generator

For the risk-neutral dynamics $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, the generator is:

$$
\boxed{
\mathcal{L}f(S) = rS\frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 f}{\partial S^2}
}
$$

This captures the **local drift and diffusion structure** of the stock price.

---

## Derivation of the Black-Scholes PDE

### Method 1: Feynman-Kac

The price of a European option with payoff $\Phi(S_T)$ at maturity $T$ is:

$$
V(t,S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]
$$

By the **Feynman-Kac theorem**, $V$ satisfies:

$$
\boxed{
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
}
$$

with terminal condition $V(T,S) = \Phi(S)$.

### Method 2: Delta Hedging (Replication)

Consider a portfolio:
- Long one option with value $V(t,S)$
- Short $\Delta$ shares of stock

Portfolio value: $\Pi = V - \Delta S$

**Itô's lemma** on $V(t,S_t)$:

$$
dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS)^2
$$

$$
= \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right)dt + \frac{\partial V}{\partial S}dS
$$

**Portfolio dynamics**:

$$
d\Pi = dV - \Delta\,dS = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right)dt + \left(\frac{\partial V}{\partial S} - \Delta\right)dS
$$

**Choose** $\Delta = \frac{\partial V}{\partial S}$ (delta hedge):

$$
d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right)dt
$$

The portfolio is now **riskless** (no $dS$ term).

**No-arbitrage**: A riskless portfolio must earn the risk-free rate:

$$
d\Pi = r\Pi\,dt = r(V - \Delta S)\,dt
$$

Equating:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = r\left(V - S\frac{\partial V}{\partial S}\right)
$$

Rearranging gives the **Black-Scholes PDE**.

---

## The Black-Scholes Equation

$$
\boxed{
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
}
$$

**Compact form using the generator**:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0
$$

---

## Terminal and Boundary Conditions

### Terminal Condition

At maturity $t = T$:

$$
V(T,S) = \Phi(S)
$$

**Examples**:
- Call option: $\Phi(S) = (S - K)^+$
- Put option: $\Phi(S) = (K - S)^+$
- Digital call: $\Phi(S) = \mathbf{1}_{S > K}$

### Boundary Conditions

**As $S \to 0$**:
- Call: $V(t,0) = 0$
- Put: $V(t,0) = Ke^{-r(T-t)}$

**As $S \to \infty$**:
- Call: $V(t,S) \sim S - Ke^{-r(T-t)}$
- Put: $V(t,S) \to 0$

---

## Explicit Solution: European Call

The Black-Scholes formula for a European call option:

$$
\boxed{
C(t,S) = S\Phi(d_1) - Ke^{-r(T-t)}\Phi(d_2)
}
$$

where $\Phi$ is the standard normal CDF and:

$$
d_1 = \frac{\log(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}
$$

$$
d_2 = d_1 - \sigma\sqrt{T-t} = \frac{\log(S/K) + (r - \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}
$$

**Put-call parity**: $P = C - S + Ke^{-r(T-t)}$

---

## The Greeks from the PDE

The **Greeks** measure sensitivities of the option price:

| Greek | Definition | PDE Role |
|-------|------------|----------|
| **Delta** ($\Delta$) | $\frac{\partial V}{\partial S}$ | Hedge ratio |
| **Gamma** ($\Gamma$) | $\frac{\partial^2 V}{\partial S^2}$ | Convexity, appears in diffusion term |
| **Theta** ($\Theta$) | $\frac{\partial V}{\partial t}$ | Time decay |
| **Vega** ($\mathcal{V}$) | $\frac{\partial V}{\partial \sigma}$ | Volatility sensitivity |
| **Rho** ($\rho$) | $\frac{\partial V}{\partial r}$ | Interest rate sensitivity |

**From the PDE**:

$$
\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV
$$

This is the **theta-gamma relationship**: time decay is related to convexity.

---

## Transformation to Heat Equation

The Black-Scholes PDE can be transformed to the heat equation.

**Change of variables**:
- $x = \log(S/K)$
- $\tau = \frac{1}{2}\sigma^2(T-t)$
- $V(t,S) = Ke^{-\alpha x - \beta\tau}u(x,\tau)$

with appropriate $\alpha, \beta$, the equation becomes:

$$
\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}
$$

This transformation is useful for:
- Analytical solutions
- Numerical methods
- Asymptotic analysis

---

## Probabilistic Interpretation

Each term in the Black-Scholes PDE has a meaning:

| Term | Interpretation |
|------|----------------|
| $\frac{\partial V}{\partial t}$ | Time decay of option value |
| $rS\frac{\partial V}{\partial S}$ | Growth of underlying at risk-free rate |
| $\frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}$ | Effect of volatility (convexity) |
| $rV$ | Discounting of option value |

---

## Extensions

### 1. Dividend-Paying Stock

With continuous dividend yield $q$:

$$
\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
$$

### 2. Time-Dependent Parameters

With $r(t), \sigma(t)$:

$$
\frac{\partial V}{\partial t} + r(t)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2(t) S^2\frac{\partial^2 V}{\partial S^2} = r(t)V
$$

### 3. Multiple Underlyings

For $n$ assets with correlation:

$$
\frac{\partial V}{\partial t} + \sum_i r S_i\frac{\partial V}{\partial S_i} + \frac{1}{2}\sum_{i,j}\rho_{ij}\sigma_i\sigma_j S_i S_j\frac{\partial^2 V}{\partial S_i\partial S_j} = rV
$$

---

## Summary

$$
\boxed{
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
}
$$

| Derivation | Key Idea |
|------------|----------|
| Feynman-Kac | Discounted expectation under $\mathbb{Q}$ |
| Delta hedging | Replication + no arbitrage |

**The Black-Scholes PDE is the fundamental equation of derivatives pricing, connecting stochastic dynamics to deterministic valuation.**
