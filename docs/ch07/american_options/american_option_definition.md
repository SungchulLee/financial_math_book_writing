# American Options: Definition and Classification

## Introduction

An **American option** is a derivative contract that grants the holder the right, but not the obligation, to exercise the option **at any time up to and including maturity** $T$. This contrasts with the European option, which permits exercise only at $T$, and the Bermudan option, which allows exercise on a discrete set of dates.

The early-exercise feature has profound consequences for pricing: the holder faces an **optimal stopping problem** at every point in time, and the additional flexibility guarantees that an American option is worth **at least as much** as its European counterpart.

!!! info "Prerequisites"
    - [Binomial Model](../binomial_model/binomial_model.md) (discrete-time pricing)
    - [Black–Scholes Model](../black_scholes_model/introduction.md) (continuous-time framework)
    - [Free Boundary Problems](../bs_pde_numerical_solution/free_boundary_problems_american_options.md) (variational inequality formulation)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Distinguish American, European, and Bermudan options precisely
    2. State the no-arbitrage ordering between option types
    3. Formulate the American pricing problem as an optimal stopping problem
    4. Identify why early-exercise flexibility has value

---

## Option Classification by Exercise Rights

### European Options

A **European option** can be exercised **only at maturity** $T$. The payoff is:

$$
H = \Phi(S_T)
$$

where $\Phi$ is the payoff function. For a call and put respectively:

$$
\Phi_{\text{call}}(S) = (S - K)^+, \quad \Phi_{\text{put}}(S) = (K - S)^+
$$

The price admits a closed-form solution under Black–Scholes assumptions.

### American Options

An **American option** can be exercised at **any time** $t \in [0, T]$. At each moment, the holder chooses between:

- **Exercising now**: receiving the intrinsic value $\Phi(S_t)$
- **Continuing to hold**: preserving the option for potential future exercise

The price is the solution to:

$$
\boxed{
V(t, S) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau - t)} \Phi(S_\tau) \mid S_t = S\right]
}
$$

where $\mathcal{T}_{t,T}$ denotes the set of stopping times valued in $[t, T]$.

### Bermudan Options

A **Bermudan option** can be exercised on a finite set of dates $\{t_1, t_2, \ldots, t_m\} \subset [0, T]$. The price is:

$$
V(t, S) = \sup_{\tau \in \{t_1, \ldots, t_m\}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau - t)} \Phi(S_\tau) \mid S_t = S\right]
$$

Bermudan options interpolate between European ($m = 1$) and American ($m \to \infty$) exercise styles.

!!! note "Naming Convention"
    The terminology reflects geography: European options are named for continental exchanges where they originated, American options for US exchanges that permitted early exercise, and Bermudan options—being "between" Europe and America—for Bermuda.

---

## No-Arbitrage Ordering

The additional exercise flexibility implies a fundamental ordering. For options with identical parameters $(S_0, K, T, r, \sigma)$:

$$
\boxed{
V_{\text{European}} \leq V_{\text{Bermudan}} \leq V_{\text{American}}
}
$$

The difference $V_{\text{American}} - V_{\text{European}}$ is the **early exercise premium (EEP)**, representing the value of the right to exercise before maturity.

!!! example "Numerical Illustration"
    Consider a put option with $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$:
    
    | Option Type | Price |
    |---|---|
    | European Put (Black–Scholes) | $\approx 5.57$ |
    | American Put (Binomial, $N = 500$) | $\approx 6.08$ |
    | Early Exercise Premium | $\approx 0.51$ |

---

## The Optimal Stopping Problem

### Mathematical Formulation

Under the risk-neutral measure $\mathbb{Q}$, the American option price satisfies:

$$
V(t, S_t) = \operatorname*{ess\,sup}_{\tau \geq t} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau - t)} \Phi(S_\tau) \mid \mathcal{F}_t\right]
$$

The **optimal stopping time** $\tau^*$ is:

$$
\tau^* = \inf\{t \leq s \leq T : V(s, S_s) = \Phi(S_s)\}
$$

That is, the holder exercises the first time the option price equals the intrinsic value—equivalently, when the continuation value drops to the exercise value.

### Connection to the Variational Inequality

The optimal stopping problem is equivalent to the **variational inequality** (obstacle problem):

$$
\boxed{
\min\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV, \; V - \Phi\right) = 0
}
$$

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S$ is the Black–Scholes generator. This formulation is studied in detail in [Free Boundary Problems](../bs_pde_numerical_solution/free_boundary_problems_american_options.md).

---

## Comparison of Exercise Styles

| Feature | European | Bermudan | American |
|---|---|---|---|
| Exercise timing | At $T$ only | On dates $\{t_1, \ldots, t_m\}$ | Any $t \in [0, T]$ |
| Pricing method | Closed-form (BS) | Backward induction on dates | Optimal stopping / free boundary |
| Analytical solution | Yes (vanilla) | No | No (except perpetual) |
| Numerical complexity | Low | Moderate | High |
| Market prevalence | OTC, indices | Interest rate options | Equity, ETF options |

---

## Summary

$$
\boxed{
V_{\text{American}}(t, S) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau - t)} \Phi(S_\tau) \mid S_t = S\right]
}
$$

| Aspect | Description |
|---|---|
| Key feature | Exercise at any time $t \leq T$ |
| Value ordering | $V_{\text{European}} \leq V_{\text{American}}$ |
| Pricing problem | Optimal stopping / variational inequality |
| Early exercise premium | $V_{\text{American}} - V_{\text{European}} \geq 0$ |

**The early-exercise right transforms the pricing problem from a straightforward expectation into an optimization over stopping times, requiring fundamentally different mathematical and numerical tools.**
