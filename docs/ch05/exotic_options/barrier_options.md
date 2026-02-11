# Barrier Options

## Introduction

**Barrier options** are path-dependent derivatives that become active (**knock-in**) or expire worthless (**knock-out**) when the underlying asset price crosses a predetermined **barrier level** $H$ during the life of the option. This conditional activation or deactivation makes barrier options cheaper than their vanilla counterparts, since the holder accepts restricted optionality in exchange for a lower premium.

Barrier options are among the most widely traded exotic derivatives in OTC markets, particularly in foreign exchange and structured equity products.

!!! info "Prerequisites"
    - [Black–Scholes Formula](../black_scholes_formula/bs_formula_statement.md) (vanilla option pricing)
    - [Exotic Options Overview](exotic_options_overview.md) (classification and motivation)
    - [Reflection Principle](../../ch01/brownian_motion/reflection_principle.md) (hitting probabilities for Brownian motion)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Classify all eight standard barrier option types
    2. Write the payoff formula for each barrier type
    3. State the in–out parity relationship
    4. Identify analytical pricing formulas under GBM assumptions
    5. Understand discretization bias in barrier option pricing

---

## Barrier Types and Classification

A barrier option is characterized by three features: the **option type** (call or put), the **barrier direction** (up or down), and the **barrier effect** (knock-in or knock-out). This produces eight standard types:

| Barrier Type | Direction | Effect | Condition for Activation/Deactivation |
|---|---|---|---|
| Up-and-in call | Up | Knock-in | Option activates if $\max_{0 \leq t \leq T} S_t \geq H$ |
| Up-and-out call | Up | Knock-out | Option dies if $\max_{0 \leq t \leq T} S_t \geq H$ |
| Down-and-in call | Down | Knock-in | Option activates if $\min_{0 \leq t \leq T} S_t \leq H$ |
| Down-and-out call | Down | Knock-out | Option dies if $\min_{0 \leq t \leq T} S_t \leq H$ |
| Up-and-in put | Up | Knock-in | Option activates if $\max_{0 \leq t \leq T} S_t \geq H$ |
| Up-and-out put | Up | Knock-out | Option dies if $\max_{0 \leq t \leq T} S_t \geq H$ |
| Down-and-in put | Down | Knock-in | Option activates if $\min_{0 \leq t \leq T} S_t \leq H$ |
| Down-and-out put | Down | Knock-out | Option dies if $\min_{0 \leq t \leq T} S_t \leq H$ |

---

## Payoff Formulas

### Knock-Out Options

A **knock-out** option pays like a vanilla option provided the barrier is never breached:

$$
\boxed{
\text{Payoff}_{\text{KO}} = (S_T - K)^+ \cdot \mathbf{1}_{\{\text{barrier not breached}\}}
}
$$

For a **down-and-out call** with barrier $H < S_0$:

$$
\text{Payoff} = (S_T - K)^+ \cdot \mathbf{1}_{\left\{\min_{0 \leq t \leq T} S_t > H\right\}}
$$

For an **up-and-out call** with barrier $H > S_0$:

$$
\text{Payoff} = (S_T - K)^+ \cdot \mathbf{1}_{\left\{\max_{0 \leq t \leq T} S_t < H\right\}}
$$

### Knock-In Options

A **knock-in** option pays only if the barrier has been breached:

$$
\boxed{
\text{Payoff}_{\text{KI}} = (S_T - K)^+ \cdot \mathbf{1}_{\{\text{barrier breached}\}}
}
$$

For a **down-and-in call** with barrier $H < S_0$:

$$
\text{Payoff} = (S_T - K)^+ \cdot \mathbf{1}_{\left\{\min_{0 \leq t \leq T} S_t \leq H\right\}}
$$

---

## In–Out Parity

A fundamental relationship connects knock-in and knock-out options of the same type:

$$
\boxed{
V_{\text{knock-in}} + V_{\text{knock-out}} = V_{\text{vanilla}}
}
$$

**Proof sketch.** The barrier is either breached or not breached during $[0, T]$. If breached, the knock-in option pays the vanilla payoff and the knock-out option pays zero. If not breached, the knock-out option pays the vanilla payoff and the knock-in option pays zero. In either case, the combined payoff equals the vanilla payoff exactly.

!!! example "Numerical Example"
    For $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$, $H = 90$ (down barrier):
    
    | Component | Price |
    |---|---|
    | Vanilla call (Black–Scholes) | $\approx 10.45$ |
    | Down-and-out call | $\approx 7.93$ |
    | Down-and-in call | $\approx 2.52$ |
    | Sum (KI + KO) | $\approx 10.45$ ✓ |

---

## Analytical Pricing Under GBM

Under geometric Brownian motion with continuous barrier monitoring, closed-form solutions exist. The key mathematical tool is the **reflection principle** for Brownian motion, which provides the joint distribution of $(S_T, \min_{t} S_t)$ or $(S_T, \max_{t} S_t)$.

### Down-and-Out Call ($H < K$, $H < S_0$)

The Rubinstein–Reiner (1991) formula gives:

$$
C_{\text{do}} = S_0\, N(x_1) - K e^{-rT} N(x_1 - \sigma\sqrt{T}) - S_0 \left(\frac{H}{S_0}\right)^{2\lambda} N(y_1) + K e^{-rT} \left(\frac{H}{S_0}\right)^{2\lambda - 2} N(y_1 - \sigma\sqrt{T})
$$

where:

$$
\lambda = \frac{r + \frac{1}{2}\sigma^2}{\sigma^2}, \quad x_1 = \frac{\ln(S_0/K)}{\sigma\sqrt{T}} + \lambda \sigma\sqrt{T}, \quad y_1 = \frac{\ln(H^2/(S_0 K))}{\sigma\sqrt{T}} + \lambda \sigma\sqrt{T}
$$

The terms involving $(H/S_0)^{2\lambda}$ arise from the reflection principle and encode the probability of the barrier being hit.

---

## Discrete vs. Continuous Monitoring

In practice, barriers are typically monitored at **discrete intervals** (daily closes, for example) rather than continuously. This distinction matters significantly for pricing:

### Broadie–Glasserman–Kou Correction

For a discrete barrier monitored at $m$ equally-spaced times, the effective continuous barrier is approximately:

$$
\boxed{
H_{\text{eff}} = H \cdot e^{\pm \beta \sigma \sqrt{T/m}}
}
$$

where $\beta = -\zeta(1/2)/\sqrt{2\pi} \approx 0.5826$, $\zeta$ is the Riemann zeta function, and the sign depends on whether the barrier is above ($+$) or below ($-$) the current price.

This correction shifts the barrier **outward**, reflecting the fact that discrete monitoring makes it harder for the barrier to be breached between observation times.

### Pricing Implications

| Monitoring | Down-and-Out Price | Explanation |
|---|---|---|
| Continuous | Lower | Barrier more easily breached → higher knockout probability |
| Discrete (daily) | Higher | May "skip over" barrier between observation times |
| Difference | Can be 5–15% | Significant for near-barrier situations |

---

## Rebate Features

Many barrier options include a **rebate** $R$ paid when the barrier is hit (for knock-out options) or at maturity if the barrier is never hit (for knock-in options):

$$
\text{Payoff}_{\text{KO with rebate}} = (S_T - K)^+ \cdot \mathbf{1}_{\{\text{not breached}\}} + R \cdot e^{-r(\tau_H - t)} \cdot \mathbf{1}_{\{\text{breached at } \tau_H\}}
$$

where $\tau_H$ is the first hitting time of the barrier. The rebate compensates the holder for the loss of optionality when the barrier is triggered.

---

## Summary

$$
\boxed{
V_{\text{knock-in}} + V_{\text{knock-out}} = V_{\text{vanilla}}
}
$$

| Aspect | Description |
|---|---|
| Definition | Options that activate/deactivate at a barrier level $H$ |
| Eight types | Up/down × in/out × call/put |
| Key relationship | In–out parity: $V_{\text{KI}} + V_{\text{KO}} = V_{\text{vanilla}}$ |
| Analytical pricing | Available under GBM with continuous monitoring (reflection principle) |
| Discrete monitoring | Broadie–Glasserman–Kou correction adjusts for discrete observation |
| Cost advantage | Barrier options are cheaper than vanilla (restricted optionality) |

**Barrier options introduce path dependency through threshold conditions, creating a family of derivatives that trade optionality for reduced premiums and are priced using the reflection principle of Brownian motion.**
