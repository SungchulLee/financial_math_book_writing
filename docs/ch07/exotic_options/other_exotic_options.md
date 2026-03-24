# Other Exotic Options

## Introduction

Beyond barrier, Asian, and lookback options, a rich variety of exotic structures exists to serve specialized financial needs. This section surveys **chooser options**, **rainbow options**, **cliquet options**, **compound options**, and **digital (binary) options**. Each introduces a distinctive payoff mechanism that addresses specific hedging, speculation, or product design requirements.

!!! info "Prerequisites"
    - [Black–Scholes Formula](../../ch06/black_scholes_formula/bs_formula_statement.md) (vanilla pricing)
    - [Put–Call Parity](../../ch06/black_scholes_formula/put_call_parity.md) (relationship between calls and puts)
    - [Exotic Options Overview](exotic_options_overview.md) (classification)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Define and write payoffs for chooser, rainbow, cliquet, compound, and digital options
    2. Price a simple chooser option using put–call parity
    3. Explain how rainbow options depend on correlation between assets
    4. Identify applications of each exotic type

---

## Chooser Options

A **chooser option** (also called an "as-you-like-it" option) gives the holder the right to decide at a future date $t_c < T$ whether the option is a **call** or a **put** with strike $K$ and maturity $T$.

### Payoff

At the choice date $t_c$, the holder selects whichever is more valuable:

$$
\boxed{
V_{\text{chooser}}(t_c) = \max\left(C(t_c, S_{t_c}; K, T),\; P(t_c, S_{t_c}; K, T)\right)
}
$$

where $C$ and $P$ are Black–Scholes call and put values at time $t_c$.

### Pricing via Put–Call Parity

Using put–call parity $P = C - S_{t_c} e^{-q(T-t_c)} + K e^{-r(T-t_c)}$, the chooser payoff becomes:

$$
V_{\text{chooser}}(t_c) = C(t_c, S_{t_c}; K, T) + \max\left(0,\; K e^{-r(T-t_c)} - S_{t_c} e^{-q(T-t_c)}\right)
$$

This decomposes the chooser into a **call with strike $K$ and maturity $T$** plus a **put with strike $K e^{-r(T-t_c)}$ and maturity $t_c$**. Both components can be priced with Black–Scholes.

!!! note "Chooser vs. Straddle"
    A chooser option is cheaper than a straddle (call + put) because the holder chooses only one leg. A straddle at expiry pays $|S_T - K|$, while a chooser's payoff is $(S_T - K)^+$ or $(K - S_T)^+$ depending on the choice made at $t_c$.

---

## Rainbow Options

**Rainbow options** have payoffs that depend on **multiple underlying assets** $S^{(1)}, S^{(2)}, \ldots, S^{(n)}$. The name derives from the idea of each asset being a different "color."

### Common Types

**Best-of option (call on max)**:

$$
\text{Payoff} = \left(\max(S_T^{(1)}, S_T^{(2)}, \ldots, S_T^{(n)}) - K\right)^+
$$

**Worst-of option (call on min)**:

$$
\text{Payoff} = \left(\min(S_T^{(1)}, S_T^{(2)}, \ldots, S_T^{(n)}) - K\right)^+
$$

**Spread option** (two assets):

$$
\text{Payoff} = \left(S_T^{(1)} - S_T^{(2)} - K\right)^+
$$

### Role of Correlation

The correlation $\rho$ between underlying assets is a critical pricing parameter:

| $\rho$ | Best-of Price | Worst-of Price |
|---|---|---|
| $\rho \to +1$ | Assets move together → approaches single-asset call | Assets move together → approaches single-asset call |
| $\rho \to -1$ | Maximum of two diverging assets → very valuable | Minimum of two diverging assets → near zero |

!!! warning "Correlation Risk"
    Rainbow option prices are highly sensitive to the correlation assumption. Since correlations are notoriously unstable and difficult to estimate, rainbow options carry significant **model risk**.

---

## Cliquet (Ratchet) Options

A **cliquet option** resets its strike at predetermined dates and accumulates payoffs over multiple periods. This "ratcheting" mechanism locks in gains periodically.

### Structure

For reset dates $t_0 < t_1 < \cdots < t_n = T$, the cliquet payoff is:

$$
\boxed{
\text{Payoff} = \sum_{i=1}^{n} \max\left(\frac{S_{t_i} - S_{t_{i-1}}}{S_{t_{i-1}}} - K_{\text{local}},\; 0\right)
}
$$

Each period's return is capped and floored independently, and the total payoff is the sum of individual period payoffs.

### Features

- **Local caps and floors**: Each period's contribution may be bounded: $\max(\min(R_i, c), f)$ where $R_i$ is the period return, $c$ is the cap, and $f$ is the floor
- **Global cap/floor**: The total accumulated payoff may also be bounded
- **Volatility sensitivity**: Cliquet prices are highly sensitive to the volatility smile and the forward volatility structure

Cliquets are common in structured products sold to retail investors, offering "equity-linked" returns with downside protection.

---

## Compound Options

A **compound option** is an option on an option—the underlying asset is itself an option.

### Four Types

| Compound Type | Description | Payoff at $t_1$ |
|---|---|---|
| Call on call | Right to buy a call | $\max(C(t_1, S_{t_1}; K_2, T_2) - K_1, 0)$ |
| Call on put | Right to buy a put | $\max(P(t_1, S_{t_1}; K_2, T_2) - K_1, 0)$ |
| Put on call | Right to sell a call | $\max(K_1 - C(t_1, S_{t_1}; K_2, T_2), 0)$ |
| Put on put | Right to sell a put | $\max(K_1 - P(t_1, S_{t_1}; K_2, T_2), 0)$ |

Here $K_1$ is the strike for the compound option (expiring at $t_1$), and $K_2$ is the strike of the underlying option (expiring at $T_2 > t_1$).

### Applications

Compound options arise naturally in **real options** analysis: a company's decision to invest in a project can be modeled as a call on a call—the initial R&D investment ($K_1$) gives the right to proceed with full-scale investment ($K_2$).

### Geske's Formula

Under GBM assumptions, Geske (1979) derived a closed-form formula for compound options using the **bivariate normal distribution** $N_2(\cdot, \cdot; \rho)$.

---

## Digital (Binary) Options

**Digital options** pay a fixed amount if a condition is met at expiry, regardless of the magnitude by which the condition is satisfied.

### Cash-or-Nothing

$$
\boxed{
\text{Payoff}_{\text{digital call}} = Q \cdot \mathbf{1}_{\{S_T > K\}}
}
$$

where $Q$ is the fixed cash payment. Under Black–Scholes:

$$
V_{\text{digital call}} = Q\, e^{-rT}\, N(d_2)
$$

### Asset-or-Nothing

$$
\text{Payoff}_{\text{asset-or-nothing call}} = S_T \cdot \mathbf{1}_{\{S_T > K\}}
$$

Under Black–Scholes:

$$
V_{\text{asset-or-nothing call}} = S_0\, N(d_1)
$$

### Relationship to Vanilla Options

A vanilla call is the difference between an asset-or-nothing call and $K$ units of a cash-or-nothing call:

$$
C_{\text{vanilla}} = S_0\, N(d_1) - K\, e^{-rT}\, N(d_2)
$$

This decomposition clarifies the probabilistic structure of the Black–Scholes formula.

!!! warning "Hedging Difficulty"
    Digital options have a **discontinuous payoff** at $S_T = K$. The delta approaches infinity near the strike as $T \to 0$, making hedging extremely difficult. In practice, digital options are often replicated approximately using tight call spreads.

---

## Summary

| Exotic Type | Key Feature | Pricing Approach | Main Application |
|---|---|---|---|
| Chooser | Choose call or put at $t_c$ | Put–call parity decomposition | Volatility speculation |
| Rainbow | Multiple underlying assets | Monte Carlo (correlation critical) | Multi-asset structured products |
| Cliquet | Periodic reset and accumulation | Monte Carlo, forward vol sensitive | Retail structured products |
| Compound | Option on an option | Bivariate normal (Geske) | Real options, staged investment |
| Digital | Fixed payout if condition met | $e^{-rT} N(d_2)$ | Binary outcomes, structured notes |

**Beyond the core barrier, Asian, and lookback structures, the exotic options universe includes chooser, rainbow, cliquet, compound, and digital options—each designed to serve specific financial needs through tailored payoff mechanisms.**

---

## Exercises

**Exercise 1.** Using put-call parity, show that a simple chooser option with choice date $t_c$, strike $K$, and maturity $T$ can be decomposed into a call with strike $K$ and maturity $T$ plus a put with strike $Ke^{-r(T-t_c)}$ and maturity $t_c$. Price both components using Black-Scholes for $S_0 = 100$, $K = 100$, $T = 1$, $t_c = 0.5$, $r = 5\%$, $\sigma = 20\%$.

---

**Exercise 2.** For a best-of call on two assets with payoff $(\max(S_T^{(1)}, S_T^{(2)}) - K)^+$, explain why the price depends critically on the correlation $\rho$ between the two assets. What happens to the best-of call price as $\rho \to +1$? As $\rho \to -1$? Sketch the price as a function of $\rho$.

---

**Exercise 3.** A cliquet option with annual resets and 3-year maturity has local floor $f = 0\%$ and local cap $c = 10\%$ per period. If the annual returns of the underlying are $+15\%$, $-8\%$, $+22\%$, compute the total cliquet payoff. Compare this with the payoff of holding the underlying asset directly over the same period.

---

**Exercise 4.** A call on a call (compound option) with strikes $K_1 = 3$ (compound strike) and $K_2 = 100$ (underlying call strike), compound expiry $t_1 = 0.5$, and underlying call expiry $T_2 = 1$, gives the right to buy a call option for $\$3$. At time $t_1$, the underlying call is worth $C(t_1, S_{t_1}; 100, 1)$. (a) For what value of $S_{t_1}$ is the compound option exactly at the money? (b) Explain why compound options arise naturally in real options analysis for staged investment decisions.

---

**Exercise 5.** A cash-or-nothing digital call pays $Q = \$1$ if $S_T > K$ and zero otherwise. Its Black-Scholes price is $e^{-rT} N(d_2)$. (a) Compute the delta of the digital call and show that it becomes infinite as $T \to 0$ when $S_0 = K$. (b) Explain why this makes digital options extremely difficult to hedge near expiry. (c) Describe how a digital call can be approximately replicated using a tight call spread $(C(K) - C(K + \epsilon))/\epsilon$.

---

**Exercise 6.** Show that a vanilla European call can be decomposed as the difference of an asset-or-nothing call and $K$ cash-or-nothing calls: $C = S_0 N(d_1) - Ke^{-rT} N(d_2)$. Interpret $N(d_1)$ as the probability that $S_T > K$ under a specific measure and $N(d_2)$ as the probability under a different measure. Which measures are these?
