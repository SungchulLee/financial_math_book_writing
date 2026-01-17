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
