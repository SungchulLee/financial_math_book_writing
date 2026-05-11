# The Greeks from the PDE

The **Greeks** are sensitivities of option prices to various parameters. They are essential for hedging, risk management, and understanding option behavior. The pricing PDE provides a unified framework for computing and relating the Greeks.

Since the option price is the Feynman-Kac expectation $V = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$, every Greek is ultimately a **derivative of this expectation** with respect to the corresponding variable or parameter, holding all others fixed. The PDE makes these relationships explicit and connects them algebraically.

---

## Definition of the Greeks

For an option price $V(t, S)$:

| Greek | Symbol | Definition | Measures sensitivity to |
|-------|--------|------------|------------------------|
| Delta | $\Delta$ | $\frac{\partial V}{\partial S}$ | Underlying price |
| Gamma | $\Gamma$ | $\frac{\partial^2 V}{\partial S^2}$ | Delta (convexity) |
| Theta | $\Theta$ | $\frac{\partial V}{\partial t}$ | Time |
| Vega | $\mathcal{V}$ | $\frac{\partial V}{\partial \sigma}$ | Volatility |
| Rho | $\rho$ | $\frac{\partial V}{\partial r}$ | Interest rate |

---

## The Theta-Gamma Relationship

The Black-Scholes PDE connects the Greeks:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
$$

Rewriting in terms of Greeks:

$$
\boxed{
\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV
}
$$

**Interpretation**: Time decay ($\Theta$) is compensated by delta ($\Delta$) and gamma ($\Gamma$) effects.

---

## At-the-Money Analysis

For ATM options ($S \approx K$), the relationship simplifies.

### ATM Call (approximately)

- $\Delta \approx 0.5$
- $\Gamma$ is maximized
- $\Theta < 0$ (time decay)

From the PDE:

$$
\Theta \approx rV - rS(0.5) - \frac{1}{2}\sigma^2 S^2\Gamma
$$

For small $r$: $\Theta \approx -\frac{1}{2}\sigma^2 S^2\Gamma$

**Key insight**: High gamma implies rapid time decay.

---

## Delta: The Hedge Ratio

Differentiating the Feynman-Kac representation $V = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$ with respect to $S$ gives:

$$
\Delta = \frac{\partial V}{\partial S}
$$

### Interpretation

- Number of shares needed to hedge one option
- Probability (under $\mathbb{Q}$) of finishing in-the-money (approximately)
- Sensitivity to small price changes

### Black-Scholes Formulas

**Call**: $\Delta_C = \mathcal{N}(d_1)$

**Put**: $\Delta_P = \mathcal{N}(d_1) - 1 = -\mathcal{N}(-d_1)$

where $d_1 = \frac{\log(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}$

### Properties

- Call: $0 \leq \Delta_C \leq 1$
- Put: $-1 \leq \Delta_P \leq 0$
- Put-call parity: $\Delta_C - \Delta_P = 1$

---

## Gamma: Convexity

Differentiating the expectation twice with respect to $S$ — equivalently, differentiating delta — gives:

$$
\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\partial \Delta}{\partial S}
$$

### Interpretation

- Rate of change of delta
- Curvature of the price function
- Hedging error for discrete rebalancing

### Black-Scholes Formula

$$
\Gamma = \frac{\phi(d_1)}{S\sigma\sqrt{T-t}}
$$

where $\phi$ is the standard normal PDF.

### Properties

- Always positive for vanilla options (convexity)
- Maximum at-the-money
- Increases as expiration approaches (for ATM)

### Gamma and Hedging

Gamma measures the **instability of the hedge**:

- High gamma: Frequent rebalancing needed
- Low gamma: Stable hedge

---

## Theta: Time Decay

Differentiating the pricing function with respect to time — the remaining independent variable in the PDE — gives:

### Definition

$$
\Theta = \frac{\partial V}{\partial t}
$$

**Sign convention**: We define $\Theta = \partial V / \partial t$, so that the PDE reads $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ without extra signs. Some practitioners define theta as $-\partial V / \partial t$ (the rate of value *lost* per day), which reverses the sign. In this text, theta for a long call is negative.

**Convention**: Often reported as daily decay ($\Theta/365$).

### Black-Scholes Formulas

**Call**:

$$
\Theta_C = -\frac{S\phi(d_1)\sigma}{2\sqrt{T-t}} - rKe^{-r(T-t)}\mathcal{N}(d_2)
$$

**Put**:

$$
\Theta_P = -\frac{S\phi(d_1)\sigma}{2\sqrt{T-t}} + rKe^{-r(T-t)}\mathcal{N}(-d_2)
$$

### Properties

- Usually negative for long options (time decay)
- Can be positive for deep ITM puts
- Accelerates near expiration

### Theta-Gamma Tradeoff

$$
\Theta \approx -\frac{1}{2}\sigma^2 S^2\Gamma
$$

Long gamma positions have negative theta (pay for convexity with time decay).

---

## Vega: Volatility Sensitivity

### Definition

$$
\mathcal{V} = \frac{\partial V}{\partial \sigma}
$$

**Note**: Vega is not a Greek letter!

Unlike $\Delta$, $\Gamma$, and $\Theta$, vega cannot be read directly from the PDE because $\sigma$ is a **parameter** of the PDE, not one of its independent variables. Differentiating the entire Black-Scholes PDE with respect to $\sigma$ yields a PDE for $\mathcal{V}$:

$$
\frac{\partial \mathcal{V}}{\partial t} + rS\frac{\partial \mathcal{V}}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 \mathcal{V}}{\partial S^2} - r\mathcal{V} = -\sigma S^2 \Gamma
$$

This is the same Black-Scholes operator applied to $\mathcal{V}$, with a source term $-\sigma S^2\Gamma$ driven by gamma — confirming that vega and gamma are deeply linked.

### Black-Scholes Formula

$$
\mathcal{V} = S\sqrt{T-t}\phi(d_1)
$$

Same for calls and puts (put-call parity).

### Properties

- Always positive for vanilla options
- Maximum at-the-money
- Proportional to $\sqrt{T-t}$

### Vega and Implied Volatility

Vega is essential for:

- Converting between price and implied volatility
- Volatility trading strategies
- Model risk assessment

---

## Rho: Interest Rate Sensitivity

### Definition

$$
\rho = \frac{\partial V}{\partial r}
$$

Like vega, rho measures sensitivity to a PDE parameter rather than an independent variable. Differentiating the PDE with respect to $r$ yields a PDE for $\rho$ with source terms involving $S\Delta$ and $V$ — reflecting that interest rate changes affect both the drift and the discounting.

### Black-Scholes Formulas

**Call**: $\rho_C = K(T-t)e^{-r(T-t)}\mathcal{N}(d_2)$

**Put**: $\rho_P = -K(T-t)e^{-r(T-t)}\mathcal{N}(-d_2)$

### Properties

- Calls have positive rho (benefit from higher rates)
- Puts have negative rho
- Larger for longer maturities

---

## Computing Greeks from the PDE

### Finite Difference Approximations

Given numerical solution $V^n_j$ on a grid:

$$
\Delta \approx \frac{V_{j+1} - V_{j-1}}{2\Delta S}
$$

$$
\Gamma \approx \frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2}
$$

$$
\Theta \approx \frac{V^{n+1}_j - V^n_j}{\Delta t}
$$

### Pathwise Derivatives (Monte Carlo)

For simulation:

$$
\Delta = \mathbb{E}\left[e^{-rT}\Phi'(S_T)\frac{\partial S_T}{\partial S_0}\right]
$$

Using GBM: $\frac{\partial S_T}{\partial S_0} = \frac{S_T}{S_0}$

---

## Greeks for Portfolios

For a portfolio $\Pi = \sum_i w_i V_i$:

$$
\Delta_\Pi = \sum_i w_i \Delta_i, \quad \Gamma_\Pi = \sum_i w_i \Gamma_i, \quad \text{etc.}
$$

### Delta-Gamma Hedging

To hedge both delta and gamma:

1. Add a second option to zero gamma
2. Adjust stock position to zero delta

---

## Higher-Order Greeks

| Greek | Definition | Measures |
|-------|------------|----------|
| Vanna | $\frac{\partial^2 V}{\partial S \partial \sigma}$ | Delta-vol interaction |
| Volga | $\frac{\partial^2 V}{\partial \sigma^2}$ | Vega convexity |
| Charm | $\frac{\partial \Delta}{\partial t}$ | Delta decay |
| Speed | $\frac{\partial \Gamma}{\partial S}$ | Gamma sensitivity |

---

## Summary

$$
\boxed{
\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV
}
$$

| Greek | Role in Hedging | Sign (Long Call) |
|-------|-----------------|------------------|
| Delta | Stock hedge ratio | Positive |
| Gamma | Hedge stability | Positive |
| Theta | Time decay | Negative |
| Vega | Volatility exposure | Positive |
| Rho | Interest rate exposure | Positive |

**The Greeks provide a complete picture of option risk, all unified through the Black-Scholes PDE.**

---

## Exercises

**Exercise 1.** Starting from the Black-Scholes PDE $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$, show that for a long call position, theta must be negative when gamma is positive. Provide the financial intuition for why positive convexity (gamma) comes at the cost of time decay (theta).

??? success "Solution to Exercise 1"
    From the Black-Scholes PDE in Greek notation:

    $$
    \Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV
    $$

    Rearranging for $\Theta$:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    For a long call position: $V > 0$, $0 < \Delta < 1$, and $\Gamma > 0$.

    The term $rV - rS\Delta = r(V - S\Delta)$. For a call option, $V < S$ (the option is worth less than the stock), and $\Delta < 1$, so $V - S\Delta$ can be positive or negative depending on moneyness. However, the dominant term for typical parameters is $-\frac{1}{2}\sigma^2 S^2 \Gamma$, which is strictly negative when $\Gamma > 0$.

    More precisely, for an at-the-money call where $r$ is small relative to $\sigma^2$, the approximation $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$ shows clearly that positive gamma forces negative theta.

    **Financial intuition**: A long gamma position benefits from large moves in either direction (convexity profit). This is a valuable feature and cannot be obtained for free. The cost of maintaining this convexity is time decay: each day that passes without a sufficiently large move, the option loses value. This is the **theta-gamma tradeoff** — the holder pays a daily "insurance premium" (theta) in exchange for profiting from large price swings (gamma).

---
**Exercise 2.** Compute the delta, gamma, theta, vega, and rho for a European call with $S = 100$, $K = 100$, $T = 0.5$, $r = 5\%$, $\sigma = 20\%$. Verify that the PDE relationship $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$ holds numerically.

??? success "Solution to Exercise 2"
    Given: $S = 100$, $K = 100$, $T - t = 0.5$, $r = 0.05$, $\sigma = 0.20$.

    First, compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}} = \frac{0 + (0.05 + 0.02)(0.5)}{0.20\sqrt{0.5}} = \frac{0.035}{0.1414} \approx 0.2475
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T-t} = 0.2475 - 0.1414 \approx 0.1061
    $$

    Using standard normal tables: $\mathcal{N}(d_1) \approx 0.5977$, $\mathcal{N}(d_2) \approx 0.5423$, $\phi(d_1) \approx 0.3873$.

    **Call price**:

    $$
    C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) = 100(0.5977) - 100e^{-0.025}(0.5423) \approx 59.77 - 52.89 = 6.88
    $$

    **Delta**: $\Delta = \mathcal{N}(d_1) \approx 0.5977$

    **Gamma**:

    $$
    \Gamma = \frac{\phi(d_1)}{S\sigma\sqrt{T-t}} = \frac{0.3873}{100 \times 0.20 \times 0.7071} \approx 0.02739
    $$

    **Theta**:

    $$
    \Theta = -\frac{S\phi(d_1)\sigma}{2\sqrt{T-t}} - rKe^{-r(T-t)}\mathcal{N}(d_2) = -\frac{100 \times 0.3873 \times 0.20}{2 \times 0.7071} - 0.05 \times 100 \times 0.9753 \times 0.5423
    $$

    $$
    \approx -5.480 - 2.645 = -8.125
    $$

    **Vega**: $\mathcal{V} = S\sqrt{T-t}\,\phi(d_1) = 100 \times 0.7071 \times 0.3873 \approx 27.39$

    **Rho**: $\rho = K(T-t)e^{-r(T-t)}\mathcal{N}(d_2) = 100 \times 0.5 \times 0.9753 \times 0.5423 \approx 26.44$

    **Verification** of the PDE relationship:

    $$
    \Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = -8.125 + 0.05 \times 100 \times 0.5977 + \frac{1}{2}(0.04)(10000)(0.02739)
    $$

    $$
    \approx -8.125 + 2.989 + 5.478 = 0.342
    $$

    And $rV = 0.05 \times 6.88 \approx 0.344$. The two sides agree (up to rounding), confirming the PDE relationship.

---
**Exercise 3.** Show that gamma is the same for calls and puts with the same strike and maturity by differentiating the put-call parity relation $C - P = S - Ke^{-rT}$ twice with respect to $S$. Similarly, show that vega is the same for calls and puts.

??? success "Solution to Exercise 3"
    **Gamma**: Put-call parity states:

    $$
    C - P = S - Ke^{-r(T-t)}
    $$

    Differentiating once with respect to $S$:

    $$
    \frac{\partial C}{\partial S} - \frac{\partial P}{\partial S} = 1
    $$

    which gives $\Delta_C - \Delta_P = 1$. Differentiating again:

    $$
    \frac{\partial^2 C}{\partial S^2} - \frac{\partial^2 P}{\partial S^2} = 0
    $$

    Therefore $\Gamma_C = \Gamma_P$. Gamma is the same for calls and puts with the same strike and maturity.

    **Vega**: Differentiating put-call parity with respect to $\sigma$:

    $$
    \frac{\partial C}{\partial \sigma} - \frac{\partial P}{\partial \sigma} = \frac{\partial}{\partial \sigma}\left(S - Ke^{-r(T-t)}\right) = 0
    $$

    since the right-hand side $S - Ke^{-r(T-t)}$ does not depend on $\sigma$. Therefore $\mathcal{V}_C = \mathcal{V}_P$.

    **Intuition**: Put-call parity shows that calls and puts differ only by a forward contract $S - Ke^{-r(T-t)}$, which is linear in $S$ and independent of $\sigma$. All second-order effects in $S$ (gamma) and all volatility sensitivity (vega) come from the nonlinear "optionality" component, which is identical for calls and puts.

---
**Exercise 4.** For a portfolio consisting of $n_1$ calls at strike $K_1$ and $n_2$ calls at strike $K_2$, derive the conditions on $n_1$ and $n_2$ such that the portfolio is both delta-neutral and gamma-neutral. Explain why such a portfolio still has nonzero theta.

??? success "Solution to Exercise 4"
    Let the portfolio be $\Pi = n_1 C_1 + n_2 C_2$ where $C_i$ is a call at strike $K_i$ with Greeks $\Delta_i$ and $\Gamma_i$.

    **Delta-neutral condition**: $n_1 \Delta_1 + n_2 \Delta_2 = 0$

    **Gamma-neutral condition**: $n_1 \Gamma_1 + n_2 \Gamma_2 = 0$

    From the gamma condition: $n_1 / n_2 = -\Gamma_2 / \Gamma_1$. Substituting into the delta condition:

    $$
    -\frac{\Gamma_2}{\Gamma_1} \Delta_1 + \Delta_2 = 0 \quad \Longrightarrow \quad \Delta_2 \Gamma_1 = \Delta_1 \Gamma_2
    $$

    In general, $\Delta_i / \Gamma_i$ differs across strikes (this ratio depends on $d_1$), so the system has a nontrivial solution. One can choose $n_2 = 1$ and solve:

    $$
    n_1 = -\frac{\Gamma_2}{\Gamma_1}, \quad \text{with the delta condition automatically satisfied when } \frac{\Delta_1}{\Gamma_1} = \frac{\Delta_2}{\Gamma_2}
    $$

    If the delta and gamma conditions are not simultaneously satisfiable with just the two options, one adds a stock position $n_S$ shares. Then: solve $n_1 \Gamma_1 + n_2 \Gamma_2 = 0$ for the ratio $n_1/n_2$, and set $n_S = -(n_1 \Delta_1 + n_2 \Delta_2)$ to zero the total delta.

    **Why theta is nonzero**: From the PDE relationship applied to the portfolio:

    $$
    \Theta_\Pi + rS\Delta_\Pi + \frac{1}{2}\sigma^2 S^2 \Gamma_\Pi = r V_\Pi
    $$

    With $\Delta_\Pi = 0$ and $\Gamma_\Pi = 0$, this reduces to $\Theta_\Pi = r V_\Pi$. As long as the portfolio has nonzero value ($V_\Pi \neq 0$), theta must be nonzero. The portfolio earns (or pays) the risk-free rate on its value, which manifests as theta.

---
**Exercise 5.** Charm is defined as $\frac{\partial \Delta}{\partial t} = \frac{\partial^2 V}{\partial S \partial t}$. By differentiating the PDE $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$ with respect to $S$, derive a relationship between charm, speed ($\frac{\partial \Gamma}{\partial S}$), and other Greeks.

??? success "Solution to Exercise 5"
    Starting from the Black-Scholes PDE in Greek form:

    $$
    \Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV
    $$

    Differentiate both sides with respect to $S$:

    $$
    \frac{\partial \Theta}{\partial S} + r\Delta + rS\frac{\partial \Delta}{\partial S} + \sigma^2 S \Gamma + \frac{1}{2}\sigma^2 S^2 \frac{\partial \Gamma}{\partial S} = r\Delta
    $$

    The $r\Delta$ terms cancel. Recognizing the higher-order Greeks:

    - Charm: $\text{Ch} = \frac{\partial \Delta}{\partial t} = \frac{\partial \Theta}{\partial S}$ (by equality of mixed partials, $V_{tS} = V_{St}$)
    - Speed: $\text{Sp} = \frac{\partial \Gamma}{\partial S} = \frac{\partial^3 V}{\partial S^3}$

    The equation becomes:

    $$
    \text{Ch} + rS\Gamma + \sigma^2 S \Gamma + \frac{1}{2}\sigma^2 S^2 \,\text{Sp} = 0
    $$

    Solving for charm:

    $$
    \boxed{\text{Ch} = -(rS + \sigma^2 S)\Gamma - \frac{1}{2}\sigma^2 S^2 \,\text{Sp}}
    $$

    This shows that charm (the rate at which delta changes over time) is determined by gamma and speed. For an ATM option where speed is small, charm is approximately $-(r + \sigma^2)S\Gamma$, meaning delta drifts over time at a rate proportional to gamma.

---
**Exercise 6.** A trader holds a delta-hedged call position. Explain how gamma risk arises between rebalancing times and estimate the P&L over a time step $\Delta t$ in terms of gamma and the realized stock move $\Delta S$. When does the trader profit from gamma, and when does the theta cost dominate?

??? success "Solution to Exercise 6"
    A trader holds a delta-hedged call: long one call $C(t,S)$ and short $\Delta$ shares. The portfolio value is $\Pi = C - \Delta S$, which is delta-neutral at time $t$.

    **How gamma risk arises**: Over a small interval $\Delta t$, the stock moves by $\Delta S$. Taylor-expanding the call price:

    $$
    \Delta C \approx \Theta\,\Delta t + \Delta \cdot \Delta S + \frac{1}{2}\Gamma(\Delta S)^2
    $$

    The hedge (short $\Delta$ shares) offsets the $\Delta \cdot \Delta S$ term. The portfolio P&L is:

    $$
    \Delta\Pi = \Delta C - \Delta \cdot \Delta S \approx \Theta\,\Delta t + \frac{1}{2}\Gamma(\Delta S)^2
    $$

    **Gamma P&L**: The term $\frac{1}{2}\Gamma(\Delta S)^2$ is always non-negative for a long call ($\Gamma > 0$). The trader profits from the gamma whenever the stock moves, regardless of direction.

    **Theta cost**: The term $\Theta\,\Delta t$ is negative for a long call ($\Theta < 0$), representing the daily time decay cost.

    **When gamma profits dominate**: The trader profits when:

    $$
    \frac{1}{2}\Gamma(\Delta S)^2 > |\Theta|\,\Delta t
    $$

    Using $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$, the breakeven condition is:

    $$
    \frac{1}{2}\Gamma(\Delta S)^2 > \frac{1}{2}\sigma^2 S^2 \Gamma\,\Delta t
    $$

    $$
    (\Delta S)^2 > \sigma^2 S^2\,\Delta t
    $$

    Since the expected squared move under GBM is $\mathbb{E}[(\Delta S)^2] \approx \sigma^2 S^2 \Delta t$, the trader profits when the **realized** move exceeds the **implied** (expected) move. In other words:

    - **Gamma profits dominate** when realized volatility exceeds implied volatility
    - **Theta cost dominates** when realized volatility is below implied volatility

    This is the fundamental principle behind volatility trading: buying options (long gamma) is a bet that realized volatility will exceed the implied volatility priced into the option.
