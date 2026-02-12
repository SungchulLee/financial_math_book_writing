# The Greeks from the PDE

The **Greeks** are sensitivities of option prices to various parameters. They are essential for hedging, risk management, and understanding option behavior. The pricing PDE provides a unified framework for computing and relating the Greeks.

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

### Definition

$$
\Delta = \frac{\partial V}{\partial S}
$$

### Interpretation

- Number of shares needed to hedge one option
- Probability (under $\mathbb{Q}$) of finishing in-the-money (approximately)
- Sensitivity to small price changes

### Black-Scholes Formulas

**Call**: $\Delta_C = \Phi(d_1)$

**Put**: $\Delta_P = \Phi(d_1) - 1 = -\Phi(-d_1)$

where $d_1 = \frac{\log(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}$

### Properties

- Call: $0 \leq \Delta_C \leq 1$
- Put: $-1 \leq \Delta_P \leq 0$
- Put-call parity: $\Delta_C - \Delta_P = 1$

---

## Gamma: Convexity

### Definition

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

### Definition

$$
\Theta = \frac{\partial V}{\partial t}
$$

**Convention**: Often reported as daily decay ($\Theta/365$).

### Black-Scholes Formulas

**Call**:
$$
\Theta_C = -\frac{S\phi(d_1)\sigma}{2\sqrt{T-t}} - rKe^{-r(T-t)}\Phi(d_2)
$$

**Put**:
$$
\Theta_P = -\frac{S\phi(d_1)\sigma}{2\sqrt{T-t}} + rKe^{-r(T-t)}\Phi(-d_2)
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

### Black-Scholes Formulas

**Call**: $\rho_C = K(T-t)e^{-r(T-t)}\Phi(d_2)$

**Put**: $\rho_P = -K(T-t)e^{-r(T-t)}\Phi(-d_2)$

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
