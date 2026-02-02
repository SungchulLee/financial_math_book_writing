# Risk-Neutral Valuation Principle

The **risk-neutral valuation principle** is the central pricing formula of mathematical finance. It states that the price of any derivative equals the discounted expected payoff under the risk-neutral measure, not the physical measure.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Martingales](../../ch01/filtration_and_martingales/martingales.md)
    - [Girsanov's Theorem](../girsanov/girsanov_theorem.md)
    - [Fundamental Theorem of Asset Pricing](../../ch05/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)

---

## The Fundamental Pricing Formula

In an arbitrage-free market, the time-$t$ price of a contingent claim with payoff $\Phi(X_T)$ at maturity $T$ is:

$$
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
}
$$

where:

- $\mathbb{Q}$ is the **risk-neutral** (equivalent martingale) measure
- $r_s$ is the instantaneous risk-free rate
- $\mathcal{F}_t$ is the information available at time $t$

For constant interest rate $r$:

$$
V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(X_T) \mid \mathcal{F}_t]
$$

---

## Foundation: The Fundamental Theorem of Asset Pricing

The risk-neutral valuation principle rests on the **Fundamental Theorem of Asset Pricing (FTAP)**:

!!! theorem "First Fundamental Theorem"
    A market is **arbitrage-free** if and only if there exists an **equivalent martingale measure** $\mathbb{Q}$ under which discounted prices of traded assets are martingales.

!!! theorem "Second Fundamental Theorem"
    An arbitrage-free market is **complete** (every contingent claim can be replicated) if and only if the equivalent martingale measure $\mathbb{Q}$ is **unique**.

**Key implications**:

1. The existence of $\mathbb{Q}$ is equivalent to no-arbitrage—it's not an assumption but a consequence
2. In complete markets, there is exactly one no-arbitrage price for every derivative
3. In incomplete markets, multiple equivalent martingale measures exist, leading to price bounds rather than unique prices

See [Fundamental Theorem of Asset Pricing](../../ch05/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) for proofs and details.

---

## Why Risk-Neutral, Not Physical?

Under the **physical measure** $\mathbb{P}$:

- Expected returns reflect risk preferences
- Different investors may assign different values
- No unique price emerges from expectations alone

Under the **risk-neutral measure** $\mathbb{Q}$:

- All assets earn the risk-free rate in expectation
- Prices are determined by no-arbitrage alone
- Unique prices emerge (in complete markets)

**Key insight**: Risk-neutral pricing is not about beliefs—it's about the price required to prevent arbitrage. The measure $\mathbb{Q}$ encodes the prices of traded options, not anyone's subjective probabilities.

---

## Derivation from No-Arbitrage

### Step 1: FTAP Gives the Martingale Property

By the First Fundamental Theorem, no-arbitrage implies existence of $\mathbb{Q}$ such that discounted prices of **traded assets** are $\mathbb{Q}$-martingales.

For the money market account $B_t = e^{\int_0^t r_s\,ds}$ as numeraire, the discounted stock price:

$$
\tilde{S}_t = \frac{S_t}{B_t} = e^{-\int_0^t r_s\,ds}S_t
$$

is a $\mathbb{Q}$-martingale.

### Step 2: Derivative Prices Must Also Be Martingales

Let $V_t$ be the price of a derivative with payoff $\Phi(X_T)$ at time $T$. If the derivative can be replicated by trading in the underlying assets, its discounted price must also be a $\mathbb{Q}$-martingale (otherwise an arbitrage exists between the derivative and its replicating portfolio).

Therefore:

$$
\tilde{V}_t = e^{-\int_0^t r_s\,ds}V_t
$$

is a $\mathbb{Q}$-martingale.

### Step 3: Apply the Martingale Property

By the martingale property:

$$
\tilde{V}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T \mid \mathcal{F}_t]
$$

### Step 4: Use the Terminal Condition

At maturity, $V_T = \Phi(X_T)$, so:

$$
e^{-\int_0^t r_s\,ds}V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
$$

### Step 5: Rearrange

Multiplying both sides by $e^{\int_0^t r_s\,ds}$:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
$$

---

## The Meaning of Risk Neutrality

Under $\mathbb{Q}$, investors behave **as if** they are indifferent to risk:

| Aspect | Physical World ($\mathbb{P}$) | Risk-Neutral World ($\mathbb{Q}$) |
|--------|------------------------------|-----------------------------------|
| Stock drift | $\mu$ (includes risk premium) | $r$ (risk-free rate) |
| Risk premium | $\mu - r > 0$ (typically) | $0$ |
| Interpretation | Reflects beliefs and preferences | Reflects no-arbitrage prices |

**Important**: Risk-neutral pricing does not assume investors are actually risk-neutral. It's a mathematical transformation that simplifies pricing by absorbing risk preferences into the measure change.

---

## Connection to PDE Pricing

Risk-neutral valuation is equivalent to solving the pricing PDE via the **Feynman–Kac theorem**.

### The Pricing PDE

If $V(t,x)$ is the price as a function of time $t$ and underlying value $x$, it satisfies:

$$
\frac{\partial V}{\partial t} + \mathcal{L}^{\mathbb{Q}}V - rV = 0, \quad V(T,x) = \Phi(x)
$$

where $\mathcal{L}^{\mathbb{Q}}$ is the **infinitesimal generator under $\mathbb{Q}$**.

### Generator for Geometric Brownian Motion

For a stock following $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ under $\mathbb{Q}$:

$$
\mathcal{L}^{\mathbb{Q}} = rx\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2}{\partial x^2}
$$

Note that the drift is $r$, not $\mu$—this is the risk-neutral drift.

### The Black–Scholes PDE

Substituting into the pricing PDE:

$$
\frac{\partial V}{\partial t} + rx\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2 V}{\partial x^2} - rV = 0
$$

This is the **Black–Scholes PDE**.

### Feynman–Kac Connection

The Feynman–Kac theorem states that the solution to the PDE equals the risk-neutral expectation:

$$
V(t,x) = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi(X_T) \mid X_t = x]
$$

**Two equivalent computational approaches**:

1. **Solve the PDE** (analytical methods, finite differences)
2. **Compute the expectation** (Monte Carlo simulation)

See [Feynman–Kac Formula](../../ch03/feynman_kac/feynman_kac_formula.md) for the rigorous statement and proof.

---

## Examples

### Example 1: European Call Option

Under $\mathbb{Q}$, the stock follows:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The call price is:

$$
C_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t]
$$

**Evaluating the expectation**: Under $\mathbb{Q}$, the terminal stock price is:

$$
S_T = S_t \exp\left(\left(r - \frac{\sigma^2}{2}\right)(T-t) + \sigma\sqrt{T-t}\,Z\right)
$$

where $Z \sim N(0,1)$ under $\mathbb{Q}$. The expectation of $(S_T - K)^+$ for lognormal $S_T$ can be evaluated explicitly (see [Black–Scholes Formula](../../ch05/black_scholes_formula/bs_formula_statement.md)), yielding:

$$
C_t = S_t\Phi(d_1) - Ke^{-r(T-t)}\Phi(d_2)
$$

where:

$$
d_1 = \frac{\ln(S_t/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}
$$

### Example 2: Zero-Coupon Bond

A bond paying $1$ at time $T$ has price:

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds} \;\middle|\; \mathcal{F}_t\right]
$$

For constant $r$: $P(t,T) = e^{-r(T-t)}$.

For stochastic $r_t$, the expectation depends on the short-rate model (Vasicek, CIR, etc.).

### Example 3: Digital (Binary) Option

A digital call paying $1$ if $S_T > K$ has price:

$$
V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{S_T > K} \mid \mathcal{F}_t] = e^{-r(T-t)}\mathbb{Q}(S_T > K \mid S_t)
$$

Under the Black–Scholes model:

$$
V_t = e^{-r(T-t)}\Phi(d_2)
$$

where $d_2$ is as defined above, and $\Phi$ is the standard normal CDF.

---

## What Changes Under $\mathbb{Q}$?

| Quantity | Under $\mathbb{P}$ | Under $\mathbb{Q}$ |
|----------|-------------------|-------------------|
| Drift of $S$ | $\mu$ | $r$ |
| Volatility of $S$ | $\sigma$ | $\sigma$ (unchanged) |
| Brownian motion | $W^{\mathbb{P}}$ | $W^{\mathbb{Q}} = W^{\mathbb{P}} + \int_0^\cdot \theta_s\,ds$ |
| Probabilities | Reflect beliefs | Reflect market prices |

### Volatility Invariance

The **instantaneous (diffusion) volatility** $\sigma(t, S_t)$ is invariant under equivalent measure changes—only drift changes. This follows from Girsanov's theorem: the measure change affects the drift of the Brownian motion but not its quadratic variation.

**Clarification**: This refers to the model volatility parameter. Implied volatility (extracted from option prices) and realized volatility (computed from historical data) are market/statistical quantities that don't "change under measure"—they are what they are.

---

## Generalization: Change of Numéraire

The risk-neutral measure uses the money market account $B_t = e^{\int_0^t r_s\,ds}$ as numéraire. More generally, for any positive tradeable asset $N_t$ as numéraire:

$$
V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\left[\frac{\Phi(X_T)}{N_T} \;\middle|\; \mathcal{F}_t\right]
$$

where $\mathbb{Q}^N$ is the measure under which prices divided by $N_t$ are martingales.

**Common choices**:

- $N_t = B_t$ (money market): gives the standard risk-neutral measure $\mathbb{Q}$
- $N_t = P(t,T)$ (zero-coupon bond): gives the **$T$-forward measure** $\mathbb{Q}^T$
- $N_t = S_t$ (stock): gives the **stock measure**

See [Numéraire and Measure Change](../risk-neutral_measure/numeraire_and_measure_change.md) for details.

---

## Limitations and Extensions

### Incomplete Markets

When markets are incomplete (unhedgeable risks exist):

- **Multiple** equivalent martingale measures exist
- Risk-neutral pricing gives a **range** of arbitrage-free prices, not a unique price
- Additional criteria are needed to select a price:
    - **Utility-based pricing**: maximize expected utility
    - **Variance-optimal measure**: minimize hedging error variance
    - **Minimal entropy measure**: closest to $\mathbb{P}$ in relative entropy
    - **Superhedging**: worst-case bound

See [Incomplete Markets and Pricing Bounds](../../ch05/extensions_black_scholes/incomplete_markets_and_pricing_bounds.md).

### Model Dependence

Risk-neutral pricing requires:

- A **model** for the underlying dynamics (GBM, stochastic vol, jumps, etc.)
- **Calibration** to market prices of liquid instruments
- The derivative price is only as good as the model

Model risk is the risk that the model is misspecified.

### Path-Dependent Options

For options whose payoff depends on the entire path $\{X_s\}_{t \leq s \leq T}$:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(\{X_s\}_{t \leq s \leq T}) \;\middle|\; \mathcal{F}_t\right]
$$

Examples include:

- **Asian options**: payoff depends on average price
- **Barrier options**: payoff depends on whether price crosses a level
- **Lookback options**: payoff depends on maximum or minimum price

These expectations typically require Monte Carlo simulation or specialized PDE methods.

---

## Summary

$$
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)}\Phi(X_T) \mid \mathcal{F}_t\right]
}
$$

| Aspect | Description |
|--------|-------------|
| **What it says** | Price = discounted expected payoff under $\mathbb{Q}$ |
| **Foundation** | Fundamental Theorem of Asset Pricing (no-arbitrage ⟺ $\mathbb{Q}$ exists) |
| **Why $\mathbb{Q}$** | Ensures no-arbitrage; unique prices in complete markets |
| **What changes** | Drift becomes $r$; volatility unchanged |
| **PDE equivalence** | Same as solving Black–Scholes PDE (Feynman–Kac) |
| **Limitations** | Incomplete markets → non-unique prices; model dependence |

!!! summary "Key Takeaway"
    The risk-neutral valuation principle transforms the economic problem of pricing into a mathematical problem of computing expectations. The measure $\mathbb{Q}$ is not about beliefs—it encodes the no-arbitrage constraints from traded asset prices. In complete markets, this gives unique derivative prices; in incomplete markets, it gives bounds.
