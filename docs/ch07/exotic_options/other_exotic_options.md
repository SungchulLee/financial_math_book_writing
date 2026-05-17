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

Recall (see [Digital Option Pricing](../../ch06/black_scholes_formula/digital_option_pricing.md)): a cash-or-nothing call pays $Q\cdot\mathbf{1}_{\{S_T>K\}}$ with BS price $Q e^{-rT} N(d_2)$; an asset-or-nothing call pays $S_T\cdot\mathbf{1}_{\{S_T>K\}}$ with BS price $S_0 N(d_1)$; the vanilla decomposition $C = S_0 N(d_1) - K e^{-rT} N(d_2)$ follows, and the discontinuous payoff at $S_T = K$ produces blow-up of delta near expiry, motivating tight call-spread replication.

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

??? success "Solution to Exercise 1"
    **Chooser decomposition.** At the choice date $t_c$, the holder picks the maximum of the call and put values. Using put–call parity for a continuous-dividend asset (with $q = 0$ here):

    $$
    P(t_c) = C(t_c) - S_{t_c} + K e^{-r(T - t_c)}
    $$

    So:

    $$
    V_{\text{chooser}}(t_c) = \max(C, P) = \max\!\bigl(C,\; C - S_{t_c} + K e^{-r(T-t_c)}\bigr)
    $$

    $$
    = C(t_c, S_{t_c}; K, T) + \max\!\bigl(0,\; K e^{-r(T-t_c)} - S_{t_c}\bigr)
    $$

    The second term is the payoff of a put with strike $K' = K e^{-r(T-t_c)}$ and maturity $t_c$. Hence, at time $0$:

    $$
    V_{\text{chooser}}(0) = C_{\text{BS}}(S_0, K, T) + P_{\text{BS}}(S_0, K', t_c)
    $$

    **Numerical pricing.** Parameters: $S_0 = 100$, $K = 100$, $T = 1$, $t_c = 0.5$, $r = 0.05$, $\sigma = 0.20$, $q = 0$.

    **Component 1 — Call with strike $K = 100$, maturity $T = 1$:**

    $$
    d_1 = \frac{\ln(100/100) + (0.05 + 0.02)\cdot 1}{0.20 \cdot 1} = \frac{0.07}{0.20} = 0.35
    $$

    $$
    d_2 = 0.35 - 0.20 = 0.15
    $$

    $$
    C = 100 \cdot N(0.35) - 100 e^{-0.05} \cdot N(0.15) \approx 100(0.6368) - 95.123(0.5596) \approx 10.45
    $$

    **Component 2 — Put with strike $K' = 100 e^{-0.05 \cdot 0.5} = 97.53$, maturity $t_c = 0.5$:**

    $$
    d_1' = \frac{\ln(100/97.53) + (0.05 + 0.02)\cdot 0.5}{0.20\sqrt{0.5}} = \frac{0.0250 + 0.035}{0.1414} \approx 0.4243
    $$

    $$
    d_2' = 0.4243 - 0.1414 = 0.2829
    $$

    $$
    P = 97.53 e^{-0.05 \cdot 0.5} N(-0.2829) - 100\, N(-0.4243)
    $$

    $$
    \approx 95.123(0.3886) - 100(0.3357) \approx 36.96 - 33.57 \approx 3.39
    $$

    **Total chooser price:** $V_{\text{chooser}} \approx 10.45 + 3.39 \approx 13.84$

---


**Exercise 2.** For a best-of call on two assets with payoff $(\max(S_T^{(1)}, S_T^{(2)}) - K)^+$, explain why the price depends critically on the correlation $\rho$ between the two assets. What happens to the best-of call price as $\rho \to +1$? As $\rho \to -1$? Sketch the price as a function of $\rho$.

??? success "Solution to Exercise 2"
    **Dependence on correlation.** The best-of call pays $(\max(S_T^{(1)}, S_T^{(2)}) - K)^+$. The distribution of $\max(S_T^{(1)}, S_T^{(2)})$ depends critically on how the two assets move together.

    **As $\rho \to +1$:** The two assets move in lockstep, so $S_T^{(1)} \approx S_T^{(2)}$ (assuming equal volatility). Then $\max(S_T^{(1)}, S_T^{(2)}) \approx S_T^{(1)}$, and the best-of call reduces to a single-asset call. This is the **lowest** price for the best-of option.

    **As $\rho \to -1$:** The assets move in opposite directions. When one is high, the other is low, so $\max(S_T^{(1)}, S_T^{(2)})$ tends to be large regardless of the direction of the market. The maximum is almost always well above its mean, which greatly increases the expected payoff. This gives the **highest** price.

    **Sketch:** The best-of call price is a **decreasing** function of $\rho$, roughly convex, starting at its highest value near $\rho = -1$ and declining to the single-asset call price as $\rho \to +1$.

    Intuitively, lower correlation provides greater diversification, making the maximum of the two assets more likely to be large.

---


**Exercise 3.** A cliquet option with annual resets and 3-year maturity has local floor $f = 0\%$ and local cap $c = 10\%$ per period. If the annual returns of the underlying are $+15\%$, $-8\%$, $+22\%$, compute the total cliquet payoff. Compare this with the payoff of holding the underlying asset directly over the same period.

??? success "Solution to Exercise 3"
    **Cliquet payoff computation.** The cliquet has local floor $f = 0\%$ and local cap $c = 10\%$. The three annual returns are $R_1 = +15\%$, $R_2 = -8\%$, $R_3 = +22\%$.

    Each period contribution is $\max(\min(R_i, c),\, f)$:

    - Period 1: $\max(\min(0.15, 0.10),\, 0) = \max(0.10,\, 0) = 0.10$
    - Period 2: $\max(\min(-0.08, 0.10),\, 0) = \max(-0.08,\, 0) = 0$
    - Period 3: $\max(\min(0.22, 0.10),\, 0) = \max(0.10,\, 0) = 0.10$

    **Total cliquet payoff:** $0.10 + 0 + 0.10 = 0.20$ (i.e., 20% of notional).

    **Direct equity holding comparison.** With a \$1 notional, the final value of the underlying is:

    $$
    1 \times (1 + 0.15)(1 - 0.08)(1 + 0.22) = 1.15 \times 0.92 \times 1.22 \approx 1.2905
    $$

    The total return is approximately $29.05\%$.

    **Comparison:** The direct equity holding returned $29.05\%$, while the cliquet returned $20\%$. The cliquet sacrificed upside (the $+15\%$ and $+22\%$ returns were capped at $10\%$) in exchange for downside protection (the $-8\%$ return was floored at $0\%$). In a scenario with larger losses, the cliquet's protection would be more valuable.

---


**Exercise 4.** A call on a call (compound option) with strikes $K_1 = 3$ (compound strike) and $K_2 = 100$ (underlying call strike), compound expiry $t_1 = 0.5$, and underlying call expiry $T_2 = 1$, gives the right to buy a call option for $\$3$. At time $t_1$, the underlying call is worth $C(t_1, S_{t_1}; 100, 1)$. (a) For what value of $S_{t_1}$ is the compound option exactly at the money? (b) Explain why compound options arise naturally in real options analysis for staged investment decisions.

??? success "Solution to Exercise 4"
    **(a) At-the-money condition.** The compound option (call on call) is at the money when its payoff is exactly zero:

    $$
    C(t_1, S_{t_1}; K_2, T_2) - K_1 = 0
    $$

    $$
    C(t_1, S_{t_1}; 100, 1) = 3
    $$

    We need to find the stock price $S^*$ at time $t_1 = 0.5$ such that a Black–Scholes call with strike $100$ and remaining time $T_2 - t_1 = 0.5$ is worth exactly $\$3$. This requires numerically inverting the Black–Scholes formula.

    With typical parameters ($r = 5\%$, $\sigma = 20\%$, remaining time $0.5$), using Black–Scholes:

    $$
    C = S^* N(d_1) - 100 e^{-0.05 \times 0.5} N(d_2) = 3
    $$

    By numerical root-finding, $S^* \approx 95.5$ (the exact value depends on $r$ and $\sigma$). For $S_{t_1} > S^*$, the compound call is in the money; for $S_{t_1} < S^*$, it expires worthless.

    **(b) Real options interpretation.** Compound options model **staged investment decisions** naturally:

    - **Stage 1 (R&D phase):** The company pays $K_1$ (the R&D cost) to acquire information about the project. This is analogous to exercising the compound option.
    - **Stage 2 (Full investment):** If the project looks promising (the "underlying call" is in the money), the company pays $K_2$ (full-scale investment cost) to capture the project value.

    The compound option captures the sequential nature of the decision: the company need not commit to the full investment upfront. It pays a small amount ($K_1$) to preserve the option to invest later. If conditions deteriorate between $t_1$ and $T_2$, the company can walk away, losing only $K_1$.

---


**Exercise 5.** A cash-or-nothing digital call pays $Q = \$1$ if $S_T > K$ and zero otherwise. Its Black-Scholes price is $e^{-rT} N(d_2)$. (a) Compute the delta of the digital call and show that it becomes infinite as $T \to 0$ when $S_0 = K$. (b) Explain why this makes digital options extremely difficult to hedge near expiry. (c) Describe how a digital call can be approximately replicated using a tight call spread $(C(K) - C(K + \epsilon))/\epsilon$.

??? success "Solution to Exercise 5"
    **(a) Delta of the digital call.** The digital call price is $V = e^{-rT} N(d_2)$ where

    $$
    d_2 = \frac{\ln(S/K) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}
    $$

    The delta is:

    $$
    \Delta = \frac{\partial V}{\partial S} = e^{-rT} N'(d_2) \frac{\partial d_2}{\partial S} = e^{-rT} \frac{N'(d_2)}{S \sigma \sqrt{T}}
    $$

    where $N'(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard normal density.

    As $T \to 0$ with $S_0 = K$: we have $d_2 \to 0$, so $N'(d_2) \to N'(0) = 1/\sqrt{2\pi}$, and the denominator $S\sigma\sqrt{T} \to 0$. Therefore:

    $$
    \Delta \to \frac{e^{0} \cdot (1/\sqrt{2\pi})}{K \cdot \sigma \cdot 0^+} = +\infty
    $$

    The delta diverges to infinity as $T \to 0$ when $S = K$.

    **(b) Hedging difficulty.** Near expiry and near the strike, an infinitesimal change in $S$ flips the payoff from $0$ to $Q$ (or vice versa). The delta-hedging portfolio requires buying or selling enormous amounts of the underlying in response to tiny price moves, incurring massive transaction costs. In the limit, perfect replication is impossible in practice because of finite liquidity and discrete rebalancing.

    **(c) Call spread replication.** Consider the portfolio $\frac{1}{\epsilon}[C(K) - C(K + \epsilon)]$ where $C(K)$ is a vanilla call with strike $K$. At expiry:

    - If $S_T < K$: both calls expire worthless, payoff $= 0$
    - If $S_T > K + \epsilon$: payoff $= \frac{1}{\epsilon}[(S_T - K) - (S_T - K - \epsilon)] = \frac{\epsilon}{\epsilon} = 1$
    - If $K < S_T < K + \epsilon$: payoff $= \frac{1}{\epsilon}(S_T - K)$, which is between $0$ and $1$

    As $\epsilon \to 0$, this converges to $\mathbf{1}_{\{S_T > K\}}$, the digital call payoff. In practice, $\epsilon$ is chosen small but finite to keep the spread manageable while providing a good approximation.

---


**Exercise 6.** Show that a vanilla European call can be decomposed as the difference of an asset-or-nothing call and $K$ cash-or-nothing calls: $C = S_0 N(d_1) - Ke^{-rT} N(d_2)$. Interpret $N(d_1)$ as the probability that $S_T > K$ under a specific measure and $N(d_2)$ as the probability under a different measure. Which measures are these?

??? success "Solution to Exercise 6"
    **Decomposition.** The vanilla European call payoff is:

    $$
    (S_T - K)^+ = S_T \cdot \mathbf{1}_{\{S_T > K\}} - K \cdot \mathbf{1}_{\{S_T > K\}}
    $$

    The first term is the payoff of an asset-or-nothing call, and the second is $K$ times the payoff of a cash-or-nothing call (with $Q = 1$). By linearity of discounted risk-neutral expectation:

    $$
    C = e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] - K e^{-rT}\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{\{S_T > K\}}]
    $$

    The second term gives $K e^{-rT} N(d_2)$, since $N(d_2) = \mathbb{Q}(S_T > K)$ is the risk-neutral probability that the option expires in the money.

    For the first term, we compute $e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] = S_0 N(d_1)$.

    Hence: $C = S_0 N(d_1) - K e^{-rT} N(d_2)$.

    **Probabilistic interpretation:**

    - $N(d_2) = \mathbb{Q}(S_T > K)$ is the probability that the option expires in the money under the **risk-neutral measure** $\mathbb{Q}$. This is the measure under which the discounted stock price $e^{-rt}S_t$ is a martingale.

    - $N(d_1) = \tilde{\mathbb{Q}}(S_T > K)$ is the probability that the option expires in the money under the **stock-numéraire measure** (also called the **share measure** or **$S$-forward measure**) $\tilde{\mathbb{Q}}$. Under this measure, the numéraire is the stock itself, and $\frac{d\tilde{\mathbb{Q}}}{d\mathbb{Q}} = \frac{S_T}{S_0 e^{rT}}$. The drift of $\ln S_t$ under $\tilde{\mathbb{Q}}$ is $r + \sigma^2/2$ rather than $r - \sigma^2/2$, which shifts $d_2$ to $d_1 = d_2 + \sigma\sqrt{T}$.
