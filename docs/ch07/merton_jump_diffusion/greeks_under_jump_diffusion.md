# Greeks Under Jump-Diffusion

Risk management of option positions requires computing sensitivities (Greeks) with respect to the underlying parameters. Under the Merton jump-diffusion model, the Greeks inherit the series structure of the pricing formula: each Greek is a Poisson-weighted sum of the corresponding Black-Scholes Greek evaluated at adjusted parameters. However, jumps introduce qualitative differences from the Black-Scholes Greeks, including reduced delta near at-the-money, higher gamma, and a multi-dimensional vega that decomposes into sensitivities with respect to diffusion and jump parameters.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive delta, gamma, and vega under the Merton series formula
    2. Explain why delta is reduced near ATM compared to Black-Scholes
    3. Decompose total vega into diffusion vega and jump parameter sensitivities
    4. Analyze the hedging error at jump times and its implications for risk management

---

## Motivation

### Greeks in Incomplete Markets

In the complete Black-Scholes market, delta hedging perfectly replicates the option payoff. The Greeks are deterministic functions of $(S, t, \sigma, r)$ and have clear hedging interpretations. Under jump-diffusion, the market is incomplete, and delta hedging leaves residual jump risk. Nevertheless, the Greeks remain essential for:

- **Local risk management**: Delta and gamma control the P&L from small and moderate continuous moves
- **Parameter sensitivity**: Vega measures exposure to changes in implied volatility levels
- **Scenario analysis**: Understanding how option values respond to parameter shifts

---

## Delta

### Series Formula for Delta

The Merton call delta is obtained by differentiating the series formula term by term:

!!! info "Proposition: Merton Delta"
    The delta of a European call under the Merton model is

    $$
    \Delta_{\text{Merton}} = \frac{\partial C}{\partial S_0} = \sum_{n=0}^{\infty} w_n \, \Delta_{\text{BS}}^{(n)}
    $$

    where $w_n = \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}$ and $\Delta_{\text{BS}}^{(n)} = e^{(r_n - r)T}N(d_1^{(n)})$ is the Black-Scholes delta with adjusted parameters $(\sigma_n, r_n)$.

**Proof.** Since the series converges uniformly in $S_0$ on compact sets (each term is bounded and the Poisson weights sum to one), differentiation and summation can be exchanged. Differentiating each Black-Scholes component with respect to $S_0$ gives the standard Black-Scholes delta with the corresponding adjusted parameters. $\square$

### Delta Reduction Near ATM

A key qualitative difference from Black-Scholes is that the Merton delta is typically **smaller** for ATM calls:

$$
\Delta_{\text{Merton}}^{\text{ATM}} < \Delta_{\text{BS}}^{\text{ATM}}
$$

The intuition is that the higher effective volatility from jumps spreads the probability mass of $S_T$ over a wider range, reducing the sensitivity to small changes in $S_0$. In Black-Scholes terms, the ATM delta is approximately $N(d_1) \approx N(\sigma\sqrt{T}/2)$, which decreases as volatility increases.

### Delta Discontinuity at Jump Times

Between jumps, delta evolves continuously as a function of the (continuously changing) stock price. At a jump time $T_i$, the stock price changes from $S_{T_i^-}$ to $S_{T_i^-} \cdot Y_i$, and the delta jumps from $\Delta(S_{T_i^-})$ to $\Delta(S_{T_i^-} \cdot Y_i)$. For a large jump, this can represent a substantial change in the hedge ratio.

!!! example "Delta Jump Illustration"
    Consider an ATM call with $S_0 = \$100$, $\Delta \approx 0.52$. If a downward jump moves the stock to $S = \$85$, the call is now OTM and $\Delta$ might drop to $0.30$. The hedge portfolio, which held 0.52 shares, now holds too many shares relative to the new delta, resulting in a loss from the excess position.

    The hedging loss at the jump is approximately:

    $$
    \text{Loss} \approx [V(85) - V(100)] - 0.52 \times (85 - 100) = [V(85) - V(100)] + 7.80
    $$

    Since $V(85) - V(100) < -7.80$ for a convex payoff, the net loss is positive.

---

## Gamma

### Series Formula for Gamma

!!! info "Proposition: Merton Gamma"
    The gamma of a European call under the Merton model is

    $$
    \Gamma_{\text{Merton}} = \frac{\partial^2 C}{\partial S_0^2} = \sum_{n=0}^{\infty} w_n \, \Gamma_{\text{BS}}^{(n)}
    $$

    where $\Gamma_{\text{BS}}^{(n)} = \frac{e^{(r_n - r)T}\,\phi(d_1^{(n)})}{S_0 \sigma_n \sqrt{T}}$ and $\phi$ is the standard normal density.

### Gamma and Jump Risk

Gamma measures the curvature of the option value, which is directly related to the hedging error at jumps. The second-order Taylor expansion of the hedging error at a jump of size $Y - 1$ relative to $S$ is:

$$
\text{Hedge error} \approx \frac{1}{2}\Gamma_{\text{Merton}} \cdot S^2(Y - 1)^2
$$

Higher gamma means larger losses from jumps. This creates a tension in risk management: a trader who is long gamma benefits from continuous volatility but suffers from large jumps (the gamma profit from continuous moves is offset by discrete jump losses).

---

## Vega

### Multi-Dimensional Vega

Unlike Black-Scholes, which has a single vega $\partial C/\partial \sigma$, the Merton model has **four distinct sensitivities** corresponding to its four volatility-related parameters:

$$
\mathcal{V}_{\text{total}} = \mathcal{V}_{\sigma} + \mathcal{V}_{\lambda} + \mathcal{V}_{\mu_J} + \mathcal{V}_{\sigma_J}
$$

### Diffusion Vega

$$
\mathcal{V}_{\sigma} = \frac{\partial C}{\partial \sigma} = \sum_{n=0}^{\infty} w_n \frac{\partial C_{\text{BS}}^{(n)}}{\partial \sigma}
$$

Since $\sigma$ enters each term through $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$:

$$
\frac{\partial \sigma_n}{\partial \sigma} = \frac{\sigma}{\sigma_n}
$$

The diffusion vega is the dominant sensitivity for long-maturity options, where the diffusion component dominates the jump component.

### Jump Intensity Vega

$$
\mathcal{V}_{\lambda} = \frac{\partial C}{\partial \lambda}
$$

This sensitivity measures the option price change when the expected number of jumps changes. Increasing $\lambda$ generally increases option prices (more jumps means more uncertainty), particularly for OTM options.

### Jump Mean Vega

$$
\mathcal{V}_{\mu_J} = \frac{\partial C}{\partial \mu_J}
$$

This controls the **skew**: making $\mu_J$ more negative tilts the distribution leftward, increasing OTM put prices and decreasing OTM call prices.

### Jump Volatility Vega

$$
\mathcal{V}_{\sigma_J} = \frac{\partial C}{\partial \sigma_J}
$$

This controls the **smile convexity**: increasing $\sigma_J$ raises both OTM put and OTM call prices, making the implied volatility smile more curved.

!!! tip "Parameter Impact on Implied Volatility"
    | Parameter | Effect on IV smile |
    |-----------|-------------------|
    | $\sigma$ | Parallel shift up |
    | $\lambda$ | Parallel shift up (more for short maturities) |
    | $\mu_J$ | Controls skew (tilt) |
    | $\sigma_J$ | Controls convexity (curvature) |

---

## Theta

### Time Decay with Jumps

The theta of a Merton option is:

$$
\Theta_{\text{Merton}} = \frac{\partial C}{\partial T} = \sum_{n=0}^{\infty} \frac{\partial}{\partial T}\left[w_n C_{\text{BS}}^{(n)}\right]
$$

The time derivative acts on both the Poisson weights (which depend on $\lambda'T$) and the Black-Scholes prices (which depend on $T$ through $d_1^{(n)}$, $d_2^{(n)}$, and the discount factor). The theta is generally more negative (larger time decay) than Black-Scholes theta because the jump component adds volatility that decays with time.

---

## Worked Example

!!! example "Comparing Black-Scholes and Merton Greeks"
    **Parameters:** $S_0 = \$100$, $K = \$100$, $T = 0.25$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.08$, $\sigma_J = 0.25$.

    **Black-Scholes Greeks** (no jumps):

    | Greek | Value |
    |-------|-------|
    | Delta | 0.554 |
    | Gamma | 0.0282 |
    | Vega ($\mathcal{V}_\sigma$) | 19.82 |

    **Merton Greeks** (with jumps):

    | Greek | Value |
    |-------|-------|
    | Delta | 0.518 |
    | Gamma | 0.0241 |
    | Vega ($\mathcal{V}_\sigma$) | 14.67 |
    | Vega ($\mathcal{V}_\lambda$) | 1.23 |
    | Vega ($\mathcal{V}_{\mu_J}$) | $-2.85$ |
    | Vega ($\mathcal{V}_{\sigma_J}$) | 3.41 |

    **Key observations:**

    - Delta is reduced from 0.554 to 0.518 (6.5% decrease) due to the higher effective volatility
    - Gamma is lower because the option value curve is smoother when volatility is higher
    - The diffusion vega $\mathcal{V}_\sigma$ decreases because part of the total variance comes from jumps, reducing the sensitivity to the diffusion component alone
    - The jump mean vega $\mathcal{V}_{\mu_J}$ is negative for a call: making $\mu_J$ more negative shifts the distribution leftward, reducing call values
    - The jump volatility vega $\mathcal{V}_{\sigma_J}$ is positive: larger jump dispersion increases the option value through convexity

---

## Hedging Strategies

### Delta Hedging Only

The simplest approach hedges only the diffusion risk using $\Delta_{\text{Merton}}$. The residual P&L over a period $[t, t + dt]$ without jumps is approximately zero, but at each jump the portfolio suffers a loss of order $\Gamma S^2(Y-1)^2/2$.

### Delta-Gamma Hedging with Options

Adding a second option allows hedging both delta and gamma, reducing the sensitivity to moderate jumps. However, this still does not eliminate the higher-order jump risk.

### Hedging with Jump-Sensitive Instruments

The most complete approach uses instruments that are directly sensitive to jump risk:

- **OTM puts** hedge downward jump risk
- **Variance swaps** hedge total variance (diffusion plus jump)
- **VIX options** hedge changes in implied volatility driven by jump parameter shifts

In practice, most desks use a combination of delta hedging and scenario analysis (stress testing against specific jump sizes) rather than attempting to perfectly hedge jump risk.

---

## Summary

The Greeks under the Merton jump-diffusion model inherit the series structure of the pricing formula, with each Greek being a Poisson-weighted sum of the corresponding Black-Scholes Greek at adjusted parameters. Jumps reduce the ATM delta, create a multi-dimensional vega decomposition ($\mathcal{V}_\sigma$, $\mathcal{V}_\lambda$, $\mathcal{V}_{\mu_J}$, $\mathcal{V}_{\sigma_J}$), and generate hedging errors at jump times that are proportional to gamma. The market incompleteness means that no dynamic hedging strategy in the stock alone can eliminate jump risk, making scenario analysis and jump-sensitive instruments essential complements to traditional delta hedging.
