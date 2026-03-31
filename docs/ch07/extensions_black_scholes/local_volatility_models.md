# Local Volatility Models

Local volatility models replace the constant volatility $\sigma$ of Black-Scholes with a **state-dependent** function $\sigma_{\text{loc}}(t, S)$. This allows exact calibration to the observed implied volatility surface while maintaining a complete market framework.

---

## Motivation

### The Smile Problem

Black-Scholes with constant $\sigma$ produces a **flat** implied volatility surface. Market data shows:
- **Volatility smile**: IV varies with strike
- **Term structure**: IV varies with maturity
- **Skew**: Asymmetric smile (especially in equity markets)

### Local Volatility Solution

Allow $\sigma$ to depend on $(t, S)$:

$$
\boxed{
dS_t = rS_t\,dt + \sigma_{\text{loc}}(t, S_t)S_t\,dW_t^{\mathbb{Q}}
}
$$

With the right choice of $\sigma_{\text{loc}}$, any arbitrage-free implied volatility surface can be matched exactly.

---

## The Pricing PDE

Under local volatility, the option price $V(t, S)$ satisfies:

$$
\boxed{
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(t,S)S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
}
$$

with terminal condition $V(T, S) = \Phi(S)$.

**Key difference from Black-Scholes**: The diffusion coefficient $\frac{1}{2}\sigma_{\text{loc}}^2(t,S)S^2$ varies across the grid.

---

## Dupire's Formula

### The Forward PDE (Dupire Equation)

The price of a European call $C(T, K)$ as a function of maturity $T$ and strike $K$ satisfies:

$$
\boxed{
\frac{\partial C}{\partial T} = \frac{1}{2}\sigma_{\text{loc}}^2(T, K)K^2\frac{\partial^2 C}{\partial K^2} - rK\frac{\partial C}{\partial K}
}
$$

### Dupire's Inversion Formula

Given observed call prices $C(T, K)$, the local volatility is:

$$
\boxed{
\sigma_{\text{loc}}^2(T, K) = \frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}}
}
$$

Or equivalently, in terms of implied volatility $\sigma_{\text{imp}}(T, K)$:

$$
\sigma_{\text{loc}}^2(T, K) = \frac{\sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}}T\left(\frac{\partial\sigma_{\text{imp}}}{\partial T} + rK\frac{\partial\sigma_{\text{imp}}}{\partial K}\right)}{\left(1 + Kd_1\sqrt{T}\frac{\partial\sigma_{\text{imp}}}{\partial K}\right)^2 + K^2T\sigma_{\text{imp}}\left(\frac{\partial^2\sigma_{\text{imp}}}{\partial K^2} - d_1\sqrt{T}\left(\frac{\partial\sigma_{\text{imp}}}{\partial K}\right)^2\right)}
$$

### Derivation Sketch

1. Apply Itô's lemma to the indicator $\mathbf{1}_{S_T > K}$
2. Take expectations under $\mathbb{Q}$
3. Differentiate the call price w.r.t. $T$ and $K$
4. Solve for $\sigma_{\text{loc}}$

---

## Calibration Procedure

### Step 1: Interpolate Market Data

From observed $(T_i, K_j, \sigma_{\text{imp},ij})$, construct a smooth surface $\sigma_{\text{imp}}(T, K)$.

**Methods**:
- Spline interpolation
- SVI (Stochastic Volatility Inspired) parameterization
- SABR-based interpolation

### Step 2: Apply Dupire Formula

Compute $\sigma_{\text{loc}}(T, K)$ via numerical differentiation.

**Challenge**: Numerical differentiation amplifies noise.

### Step 3: Price Exotics

Use the calibrated local volatility surface to price path-dependent options via PDE or Monte Carlo.

---

## Properties of Local Volatility

### Advantages

1. **Complete market**: One source of randomness, hedging is perfect (in theory)
2. **Exact fit**: Matches all vanilla option prices by construction
3. **Tractable**: Standard PDE/MC methods apply

### Disadvantages

1. **Unrealistic smile dynamics**: The forward smile flattens too quickly
2. **Unstable calibration**: Small data changes cause large $\sigma_{\text{loc}}$ changes
3. **Hedging performance**: Poor in practice due to smile dynamics

---

## Smile Dynamics Problem

### The Issue

Local volatility predicts that the implied volatility smile **flattens** as time passes. Empirically, the smile **persists** or even steepens.

### Comparison with Stochastic Volatility

| Model | Forward Smile | Hedging |
|-------|---------------|---------|
| Local Vol | Flattens | Poor |
| Stoch Vol | Persists | Better |

### "Sticky Strike" vs "Sticky Delta"

- **Local volatility**: Tends toward sticky strike behavior
- **Market**: Closer to sticky delta behavior

---

## Numerical Implementation

### PDE Method

Solve the backward PDE with $\sigma_{\text{loc}}(t, S)$:

```
1. Calibrate σ_loc(t, S) from market data
2. Set up grid in (t, S)
3. Time-step backward from T to 0
4. At each step, use local σ_loc(t_n, S_j)
```

### Monte Carlo Method

Simulate paths with local volatility:

$$
S_{t+\Delta t} = S_t \exp\left[\left(r - \frac{\sigma_{\text{loc}}^2(t, S_t)}{2}\right)\Delta t + \sigma_{\text{loc}}(t, S_t)\sqrt{\Delta t}Z\right]
$$

**Note**: Use $\sigma_{\text{loc}}(t, S_t)$ evaluated at the current state.

---

## Regularization

### The Ill-Posedness Problem

Dupire's formula involves second derivatives of prices with respect to strike. Small errors in $C(T, K)$ get amplified.

### Regularization Techniques

1. **Smoothing**: Apply spline smoothing to $C(T, K)$ before differentiation
2. **Tikhonov regularization**: Add penalty for rough $\sigma_{\text{loc}}$
3. **Parameterization**: Fit a parametric form (e.g., SVI) first

### Typical Regularized Problem

$$
\min_{\sigma_{\text{loc}}} \sum_{i,j}(C^{\text{model}}_{ij} - C^{\text{market}}_{ij})^2 + \lambda \int |\nabla\sigma_{\text{loc}}|^2\,dT\,dK
$$

---

## Extensions

### CEV (Constant Elasticity of Variance)

A parametric local volatility model:

$$
\sigma_{\text{loc}}(S) = \sigma_0 S^{\beta - 1}
$$

- $\beta = 1$: Black-Scholes
- $\beta < 1$: Volatility increases as $S$ decreases (leverage effect)
- $\beta = 0$: Normal model

### Time-Dependent Parameters

$$
\sigma_{\text{loc}}(t, S) = \sigma(t) f(S)
$$

Separable form simplifies calibration.

---

## Summary

$$
\boxed{
dS_t = rS_t\,dt + \sigma_{\text{loc}}(t, S_t)S_t\,dW_t
}
$$

| Aspect | Description |
|--------|-------------|
| **Definition** | State-dependent volatility $\sigma_{\text{loc}}(t, S)$ |
| **Calibration** | Dupire formula inverts option prices |
| **Advantage** | Exact fit to vanilla surface |
| **Disadvantage** | Poor smile dynamics, unstable calibration |

$$
\boxed{
\sigma_{\text{loc}}^2(T, K) = \frac{\partial_T C + rK\partial_K C}{\frac{1}{2}K^2\partial_{KK}C}
}
$$

**Local volatility provides a complete market model that fits the smile exactly, but its unrealistic dynamics limit its use for hedging and exotic pricing.**

---

## Exercises

**Exercise 1.** Starting from the Black-Scholes PDE with $\sigma$ replaced by $\sigma_{\text{loc}}(t, S)$, derive the Dupire forward equation $\frac{\partial C}{\partial T} = \frac{1}{2}\sigma_{\text{loc}}^2(T,K)K^2 \frac{\partial^2 C}{\partial K^2} - rK\frac{\partial C}{\partial K}$. Explain why this is called a "forward" equation and how it differs from the standard "backward" Black-Scholes PDE.

---

**Exercise 2.** Dupire's inversion formula is $\sigma_{\text{loc}}^2(T,K) = \frac{\partial_T C + rK \partial_K C}{\frac{1}{2}K^2 \partial_{KK} C}$. (a) Verify that the denominator $\frac{1}{2}K^2 \partial_{KK} C$ is always positive for arbitrage-free call prices (relate $\partial_{KK} C$ to the risk-neutral density). (b) Under what conditions on the call price surface could the numerator be negative, and what would this imply?

---

**Exercise 3.** In the CEV model $\sigma_{\text{loc}}(S) = \sigma_0 S^{\beta - 1}$, the parameter $\beta$ controls the leverage effect. (a) Show that for $\beta < 1$, volatility increases as the stock price decreases. (b) For $\beta = 0.5$, $\sigma_0 = 2$, and $S = 100$, compute $\sigma_{\text{loc}}$. (c) Explain why $\beta = 1$ recovers the Black-Scholes model.

---

**Exercise 4.** The local volatility surface is computed from market data via numerical differentiation. Explain why this procedure is ill-posed (sensitive to small data perturbations). Describe the Tikhonov regularization approach $\min \sum_{ij} (C^{\text{model}}_{ij} - C^{\text{market}}_{ij})^2 + \lambda \int |\nabla \sigma_{\text{loc}}|^2 \, dT \, dK$ and the role of the penalty parameter $\lambda$.

---

**Exercise 5.** Local volatility models predict that the implied volatility smile "flattens" as time progresses (sticky strike behavior), while market data shows the smile persists (closer to sticky delta behavior). Explain this difference. Why does this make local volatility unreliable for pricing forward-starting options and cliquets?

---

**Exercise 6.** Describe the full calibration procedure for a local volatility model: (a) interpolation of the implied volatility surface from market quotes, (b) application of Dupire's formula, and (c) pricing of an exotic option. At each step, identify the main numerical challenges and potential sources of error.

---

## Solutions

??? success "Solution to Exercise 1"
    The **backward** Black-Scholes PDE describes how the option price $V(t, S)$ evolves backward in time from the terminal condition $V(T, S) = \Phi(S)$:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(t, S)S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    The variables $(t, S)$ are the current time and current stock price, and the equation is solved backward from $T$ to $0$.

    The **forward** (Dupire) equation describes how the call price $C(T, K)$, viewed as a function of maturity $T$ and strike $K$, evolves forward in maturity. Starting from the Kolmogorov forward equation for the risk-neutral transition density $p(T, S_T | t, S_t)$:

    $$
    \frac{\partial p}{\partial T} = \frac{1}{2}\frac{\partial^2}{\partial S_T^2}[\sigma_{\text{loc}}^2(T, S_T)S_T^2 p] - \frac{\partial}{\partial S_T}[rS_T p]
    $$

    Since $C(T, K) = e^{-rT}\int_K^\infty (S_T - K)p(T, S_T)\,dS_T$, differentiating $C$ with respect to $T$ and $K$ and substituting the forward equation yields:

    $$
    \frac{\partial C}{\partial T} = \frac{1}{2}\sigma_{\text{loc}}^2(T, K)K^2\frac{\partial^2 C}{\partial K^2} - rK\frac{\partial C}{\partial K}
    $$

    This is called a "forward" equation because it propagates information forward in maturity $T$, starting from $T = 0$ where $C(0, K) = (S_0 - K)^+$. The key difference is:

    - **Backward PDE**: One equation per option (fixed $K, T$), solved on the $(t, S)$ grid.
    - **Forward PDE**: One equation produces call prices for all $(T, K)$ simultaneously, solved forward in $T$ on the $K$ grid.

    The forward equation is computationally advantageous when pricing many vanillas (different strikes and maturities) under the same model, as it computes the entire surface in one pass.

??? success "Solution to Exercise 2"
    **(a)** The second derivative of the call price with respect to strike is related to the risk-neutral density:

    $$
    \frac{\partial^2 C}{\partial K^2} = e^{-rT} p^{\mathbb{Q}}(S_T = K)
    $$

    where $p^{\mathbb{Q}}$ is the risk-neutral probability density function of $S_T$. Since a probability density is non-negative, $\partial_{KK}C \geq 0$, with equality only at points where the density is zero (e.g., $K = 0$ or $K \to \infty$). For interior values of $K$ where trading occurs, $\partial_{KK}C > 0$. Therefore $\frac{1}{2}K^2\partial_{KK}C > 0$.

    This positivity is also a necessary condition for the absence of butterfly arbitrage: if $\partial_{KK}C < 0$ at some strike, one could construct a butterfly spread (buy calls at $K \pm \Delta K$, sell two calls at $K$) that yields a non-negative payoff at negative cost, an arbitrage.

    **(b)** The numerator is $\partial_T C + rK\partial_K C$. For arbitrage-free call prices, this must be non-negative. Economically, $\partial_T C > 0$ for European calls (longer maturity is worth more, holding strike fixed) and $\partial_K C < 0$ (higher strike means lower call value), but $rK\partial_K C$ is negative. If $r$ is large enough or $\partial_K C$ is sufficiently negative, the numerator could in principle become negative at some $(T, K)$. A negative numerator would imply $\sigma_{\text{loc}}^2 < 0$, which is impossible. This would indicate a violation of **calendar spread arbitrage** in the input prices: a longer-dated call should be worth at least as much as a shorter-dated call after accounting for the financing cost. If the input data violates this, the local volatility surface is not well-defined, signaling that the interpolated call price surface must be corrected before applying Dupire's formula.

??? success "Solution to Exercise 3"
    **(a)** For $\beta < 1$, the local volatility is $\sigma_{\text{loc}}(S) = \sigma_0 S^{\beta - 1}$. Since $\beta - 1 < 0$, we have

    $$
    \frac{\partial \sigma_{\text{loc}}}{\partial S} = \sigma_0(\beta - 1)S^{\beta - 2} < 0
    $$

    because $\beta - 1 < 0$, $\sigma_0 > 0$, and $S^{\beta - 2} > 0$. Therefore, as $S$ decreases, $S^{\beta - 1}$ increases (negative exponent), and volatility increases. This captures the leverage effect: falling stock prices correspond to rising volatility.

    **(b)** For $\beta = 0.5$, $\sigma_0 = 2$, and $S = 100$:

    $$
    \sigma_{\text{loc}} = 2 \times 100^{0.5 - 1} = 2 \times 100^{-0.5} = \frac{2}{\sqrt{100}} = \frac{2}{10} = 0.20
    $$

    So the local volatility is 20%.

    **(c)** For $\beta = 1$: $\sigma_{\text{loc}}(S) = \sigma_0 S^{1-1} = \sigma_0 S^0 = \sigma_0$, a constant independent of $S$. This is exactly the Black-Scholes assumption of constant volatility. The SDE becomes $dS_t = rS_t\,dt + \sigma_0 S_t\,dW_t$, which is the geometric Brownian motion of Black-Scholes.

??? success "Solution to Exercise 4"
    Dupire's formula $\sigma_{\text{loc}}^2(T, K) = \frac{\partial_T C + rK\partial_K C}{\frac{1}{2}K^2\partial_{KK}C}$ requires computing partial derivatives of the call price surface $C(T, K)$. In practice, $C$ is observed only at discrete strikes and maturities with bid-ask noise. The procedure is **ill-posed** because:

    1. **Numerical differentiation amplifies noise**: Computing $\partial_{KK}C$ from noisy data via finite differences magnifies small errors. If the call price has noise of order $\epsilon$, the second derivative has noise of order $\epsilon/(\Delta K)^2$, which can be enormous for small strike spacing.
    2. **Sparse data**: Market quotes may be available only at a few strikes and maturities, requiring interpolation. Different interpolation schemes yield different derivatives.
    3. **Sensitivity to interpolation**: The choice of smoothing method (splines, SVI, etc.) strongly affects the resulting $\sigma_{\text{loc}}$, and small changes in the input data can produce large changes in the local volatility surface.

    **Tikhonov regularization** addresses this by reformulating the calibration as an optimization:

    $$
    \min_{\sigma_{\text{loc}}} \sum_{i,j}(C^{\text{model}}_{ij} - C^{\text{market}}_{ij})^2 + \lambda\int|\nabla\sigma_{\text{loc}}|^2\,dT\,dK
    $$

    The first term ensures the model fits market prices. The second term (penalty) penalizes rough or oscillatory local volatility surfaces by penalizing the gradient magnitude. The parameter $\lambda > 0$ controls the trade-off:

    - **Small $\lambda$**: Fits the data closely but may produce a noisy, oscillatory $\sigma_{\text{loc}}$.
    - **Large $\lambda$**: Produces a smooth $\sigma_{\text{loc}}$ but may not fit the data well.
    - **Optimal $\lambda$**: Balances fit quality against smoothness, typically chosen via cross-validation or the L-curve method.

??? success "Solution to Exercise 5"
    **Sticky strike vs. sticky delta**:

    - **Sticky strike** (local volatility prediction): When the spot price moves, the implied volatility at a fixed absolute strike $K$ remains unchanged. The smile "stays in place" on the $(K, \sigma_{\text{imp}})$ plot. This means if $S$ moves from 100 to 105, the implied vol at $K = 100$ is the same as before.
    - **Sticky delta** (closer to market behavior): When the spot price moves, the implied volatility at a fixed moneyness (e.g., 25-delta put) remains approximately unchanged. The smile "moves with the spot." If $S$ moves from 100 to 105, the ATM implied vol shifts to $K = 105$.

    Local volatility models tend toward sticky strike behavior because $\sigma_{\text{loc}}(t, S)$ is a fixed function of the spot price. As $S$ evolves, the model "reads off" the local vol from this fixed surface, which causes the smile to flatten over time as the distribution of future prices "diffuses" through the local vol surface.

    In reality, the smile **persists** because volatility is itself stochastic: the future smile shape is random, not deterministic. Stochastic volatility models capture this by allowing $v_t$ to fluctuate, which maintains the smile's shape and level over time.

    **Implications for forward-starting options and cliquets**: These products depend critically on the **forward smile** -- the shape of the implied volatility smile at future dates. A forward-starting option, for example, has a strike set at a future date relative to the then-prevailing spot. Its price depends on what the smile looks like at that future date. Local volatility predicts the forward smile will be much flatter than today's smile, leading to systematic underpricing of these products. Cliquets (sequences of forward-starting options) amplify this error across multiple reset dates, making local volatility unreliable for their pricing. Stochastic volatility models, which produce persistent forward smiles, give more accurate prices for these products.

??? success "Solution to Exercise 6"
    **(a) Interpolation of the implied volatility surface**:

    Start with market quotes $\{(T_i, K_j, \sigma_{\text{imp},ij})\}$ for a finite grid of maturities and strikes. Construct a smooth, arbitrage-free surface $\sigma_{\text{imp}}(T, K)$ by interpolation and extrapolation.

    **Methods**: Cubic spline interpolation in strike for each maturity, linear or spline interpolation across maturities, or parametric approaches such as SVI (Stochastic Volatility Inspired) which fits $\sigma_{\text{imp}}^2(K)$ as a function of log-moneyness.

    **Challenges**: (1) Ensuring no butterfly arbitrage ($\partial_{KK}C \geq 0$) and no calendar arbitrage ($\partial_T C \geq 0$ after accounting for discounting). (2) Extrapolation to extreme strikes and long maturities where data is sparse. (3) Handling bid-ask noise: should one fit the mid or use a weighted scheme?

    **(b) Application of Dupire's formula**:

    Convert the implied volatility surface to a call price surface $C(T, K)$ using the Black-Scholes formula. Then compute:

    $$
    \sigma_{\text{loc}}^2(T, K) = \frac{\partial_T C + rK\partial_K C}{\frac{1}{2}K^2\partial_{KK}C}
    $$

    using numerical differentiation (finite differences or analytical derivatives if using a parametric form).

    **Challenges**: (1) Numerical differentiation amplifies noise, especially $\partial_{KK}C$. (2) The denominator may become very small near extreme strikes, causing $\sigma_{\text{loc}}$ to blow up. (3) Consistency: small violations of arbitrage conditions in the interpolated surface lead to negative or imaginary local volatilities. Regularization (Tikhonov or smoothing) is typically required.

    **(c) Pricing an exotic option**:

    Use the calibrated $\sigma_{\text{loc}}(t, S)$ surface in a PDE solver or Monte Carlo simulation:

    - **PDE**: Solve $\partial_t V + \frac{1}{2}\sigma_{\text{loc}}^2(t,S)S^2\partial_{SS}V + rS\partial_S V - rV = 0$ on a $(t, S)$ grid with appropriate boundary conditions.
    - **Monte Carlo**: Simulate $S_{t+\Delta t} = S_t\exp[(r - \frac{1}{2}\sigma_{\text{loc}}^2(t, S_t))\Delta t + \sigma_{\text{loc}}(t, S_t)\sqrt{\Delta t}Z]$ and average discounted payoffs.

    **Challenges**: (1) Interpolation of $\sigma_{\text{loc}}$ between grid points during simulation must be smooth. (2) The local volatility model's poor smile dynamics mean that exotic prices (especially for forward-starting or path-dependent products) may be unreliable. (3) Computational cost: PDE requires a fine 2D grid; Monte Carlo requires many paths, especially for barrier options. (4) Model risk: the exotic price is only as reliable as the local volatility dynamics, which are known to be unrealistic for forward smile behavior.
