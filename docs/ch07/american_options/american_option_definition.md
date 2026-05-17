# American Options: Definition and Classification

## Introduction

An **American option** is a derivative contract that grants the holder the right, but not the obligation, to exercise the option **at any time up to and including maturity** $T$. This contrasts with the European option, which permits exercise only at $T$, and the Bermudan option, which allows exercise on a discrete set of dates.

The early-exercise feature has profound consequences for pricing: the holder faces an **optimal stopping problem** at every point in time, and the additional flexibility guarantees that an American option is worth **at least as much** as its European counterpart.

!!! info "Prerequisites"

    - [Binomial Model](../../ch01/binomial_model/binomial_model.md) (discrete-time pricing)
    - [Black–Scholes Model](../../ch06/black_scholes_model/introduction.md) (continuous-time framework)
    - [Free Boundary Problems](../../ch08/american_options/free_boundary_problems_american_options.md) (variational inequality formulation)

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

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S$ is the Black–Scholes generator (Recall (see [§ BS PDE structure](../../ch06/bs_pde_structure/discounting_and_killing_term.md))). Free-boundary numerics are deferred to Recall (see [§ Free Boundary Problems](../../ch08/american_options/free_boundary_problems_american_options.md)).

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

---

## Exercises

**Exercise 1.** An American call option on a non-dividend-paying stock has $S_0 = 100$, $K = 95$, $r = 5\%$, $\sigma = 25\%$, and $T = 1$. Compute the European call price using the Black-Scholes formula and explain why the American call has the same value (i.e., early exercise is never optimal). What property of the call payoff is essential for this result?

??? success "Solution to Exercise 1"
    Using the Black-Scholes formula for a European call with $S_0 = 100$, $K = 95$, $r = 0.05$, $\sigma = 0.25$, $T = 1$:

    $$
    d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} = \frac{\ln(100/95) + (0.05 + 0.03125)(1)}{0.25} = \frac{0.05129 + 0.08125}{0.25} = 0.5302
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.5302 - 0.25 = 0.2802
    $$

    $$
    C = S_0 \mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) = 100 \cdot \Phi(0.5302) - 95e^{-0.05}\Phi(0.2802)
    $$

    Computing: $\Phi(0.5302) \approx 0.7020$, $\Phi(0.2802) \approx 0.6103$, and $95e^{-0.05} \approx 90.367$:

    $$
    C \approx 100(0.7020) - 90.367(0.6103) \approx 70.20 - 55.15 \approx 15.05
    $$

    The American call has the **same value** because early exercise of a call on a non-dividend-paying stock is never optimal. The key argument is that for any $t < T$:

    $$
    C_{\text{Eu}}(S_t, t) \geq S_t - Ke^{-r(T-t)} > S_t - K
    $$

    The strict inequality holds because $r > 0$ and $T - t > 0$, so $e^{-r(T-t)} < 1$. Since the option value strictly exceeds the exercise payoff at every $t < T$, the holder never benefits from exercising early. The essential property is that the call payoff $(S - K)^+$ is **convex** in $S$, and the present value of the strike $Ke^{-r(T-t)}$ is strictly less than $K$ for positive rates.

---


**Exercise 2.** State the optimal stopping formulation for an American put: $V(t,S) = \sup_{\tau \in [t,T]} \mathbb{E}^{\mathbb{Q}}[e^{-r(\tau-t)}(K - S_\tau)^+ \mid S_t = S]$. Explain the economic meaning of the supremum over stopping times $\tau$ and why this makes the pricing problem harder than for European options.

??? success "Solution to Exercise 2"
    The optimal stopping formulation is:

    $$
    V(t, S) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau - t)}(K - S_\tau)^+ \mid S_t = S\right]
    $$

    **Economic meaning of the supremum:** The holder of the American put must choose the best possible exercise time $\tau$ from all stopping times in $[t, T]$. A stopping time is a random variable adapted to the filtration, meaning the exercise decision at time $\tau$ can depend on the stock price history up to that point but not on future information. The supremum selects the exercise strategy that maximizes the expected discounted payoff.

    **Why this is harder than European pricing:** For a European option, there is no optimization: the exercise time is fixed at $T$, so the price is simply $\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}(K - S_T)^+]$. This is a single expectation that can be computed via the Feynman-Kac theorem or closed-form formulas.

    For the American put, the $\sup$ over $\tau$ introduces an **optimization layer** on top of the expectation. The optimal $\tau^*$ depends on the solution itself (exercise when the option value equals the intrinsic value), creating a **fixed-point problem**. This transforms a linear PDE into a free-boundary problem (variational inequality), which generally has no closed-form solution.

---


**Exercise 3.** Prove that the American option price is always at least as large as the European option price with the same parameters: $V_{\text{Am}} \geq V_{\text{Eu}}$. Define the early exercise premium $\epsilon = V_{\text{Am}} - V_{\text{Eu}}$ and explain why $\epsilon = 0$ for calls on non-dividend-paying stocks.

??? success "Solution to Exercise 3"
    **Proof that $V_{\text{Am}} \geq V_{\text{Eu}}$:**

    The European option is a special case of the American option where the holder is restricted to exercise only at maturity. Let $\mathcal{T}_{t,T}$ denote the set of all stopping times in $[t, T]$. Since $\tau = T$ is a valid stopping time in $\mathcal{T}_{t,T}$:

    $$
    V_{\text{Am}}(t, S) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S\right] \geq \mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)}\Phi(S_T) \mid S_t = S\right] = V_{\text{Eu}}(t, S)
    $$

    The inequality holds because the supremum over all stopping times is at least as large as the value at any particular stopping time, including $\tau = T$. $\square$

    **Early exercise premium:** The EEP is defined as:

    $$
    \epsilon(t, S) = V_{\text{Am}}(t, S) - V_{\text{Eu}}(t, S) \geq 0
    $$

    **Why $\epsilon = 0$ for calls on non-dividend-paying stocks:** For a non-dividend-paying stock, we have shown (Exercise 1) that the call value always strictly exceeds the intrinsic value for $t < T$. This means the optimal stopping time for the American call is $\tau^* = T$, which is exactly the European exercise time. Since both options are optimally exercised at $T$, their values coincide and $\epsilon = 0$. Formally:

    $$
    C_{\text{Eu}}(S, t) \geq S - Ke^{-r(T-t)} > S - K = \Phi_{\text{call}}(S) \quad \text{for all } t < T
    $$

    so the continuation value always dominates the exercise value, and the $\sup$ in the American price is attained at $\tau = T$.

---


**Exercise 4.** A Bermudan put can be exercised at times $t_1 = 0.25$, $t_2 = 0.5$, $t_3 = 0.75$, and $T = 1$, with $K = 100$, $r = 5\%$, $\sigma = 30\%$. Explain qualitatively how the Bermudan put price relates to the European and American put prices. As the number of exercise dates increases, what does the Bermudan price converge to?

??? success "Solution to Exercise 4"
    **Ordering of prices:** By the no-arbitrage ordering:

    $$
    V_{\text{European}} \leq V_{\text{Bermudan}} \leq V_{\text{American}}
    $$

    The European put can be exercised only at $T = 1$. The Bermudan put can be exercised at $\{0.25, 0.5, 0.75, 1\}$, giving four exercise opportunities. The American put can be exercised at any time in $[0, 1]$.

    **Qualitative reasoning:** The Bermudan price lies between the European and American prices because:

    - It has strictly more exercise flexibility than the European option (4 dates vs. 1), so its price is at least as high.
    - It has strictly less flexibility than the American option (4 dates vs. a continuum), so its price is at most as high.

    With $\sigma = 30\%$ and $K = 100$, the put can go significantly in the money, making early exercise valuable. The Bermudan holder captures most (but not all) of this early-exercise value through quarterly exercise opportunities.

    **Convergence as exercise dates increase:** As the number of exercise dates $m \to \infty$ (with dates becoming dense in $[0, T]$), the Bermudan price converges to the American price:

    $$
    \lim_{m \to \infty} V_{\text{Bermudan}}^{(m)} = V_{\text{American}}
    $$

    This convergence is monotone from below, since adding more exercise dates can only increase the option value. In practice, with weekly or daily exercise dates, the Bermudan price is virtually indistinguishable from the American price.

---


**Exercise 5.** The variational inequality for an American put is $\min(-\mathcal{L}V, \, V - (K-S)^+) = 0$ where $\mathcal{L}$ is the Black-Scholes operator. Interpret each of the two conditions: (a) $-\mathcal{L}V = 0$ and (b) $V = (K-S)^+$. In which region of the $(S,t)$ plane does each condition hold?

??? success "Solution to Exercise 5"
    The variational inequality $\min\left(-\mathcal{L}V, \, V - (K-S)^+\right) = 0$ encodes two conditions, exactly one of which holds as an equality at each point $(S, t)$:

    **(a) Condition $-\mathcal{L}V = 0$:** This means

    $$
    -\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 V_{SS} - rSV_S + rV = 0
    $$

    This is the standard Black-Scholes PDE. It holds in the **continuation region** $\mathcal{C} = \{(S, t) : V(S, t) > (K - S)^+\}$, where the option value strictly exceeds the intrinsic value. In this region, the holder should not exercise because the option is worth more alive than dead. The PDE describes the evolution of the option value when the holder optimally continues to hold.

    For the American put, the continuation region is $\{(S, t) : S > S^*(t)\}$, where $S^*(t)$ is the free boundary (the critical stock price below which exercise is optimal).

    **(b) Condition $V = (K - S)^+$:** This means the option value equals the intrinsic value of immediate exercise. It holds in the **exercise (stopping) region** $\mathcal{E} = \{(S, t) : V(S, t) = (K - S)^+\}$. In this region, the holder should exercise immediately because the time value is zero and waiting offers no benefit.

    For the American put, the exercise region is $\{(S, t) : S \leq S^*(t)\}$, corresponding to stock prices sufficiently low that the interest earned on the strike cash $K$ exceeds the remaining optionality value.

    The $\min$ operator ensures complementarity: at every point, at least one factor is zero, and both are non-negative. The boundary between the two regions is the free boundary $S^*(t)$, which is unknown and must be determined as part of the solution.
