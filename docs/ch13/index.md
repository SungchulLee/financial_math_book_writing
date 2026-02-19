# Chapter 13: Local Volatility

This chapter develops the local volatility framework, in which the diffusion coefficient $\sigma(t, S)$ is a deterministic function of time and spot price chosen to exactly reproduce all observed European option prices. Starting from Dupire's formula and the forward Kolmogorov (Fokker-Planck) equation, we derive the local volatility surface from market data, study its relationship to implied volatility via asymptotic expansions, analyze the model's structural limitations—particularly its failure to capture realistic smile dynamics—and develop the numerical methods needed for calibration and pricing.

## Key Concepts

**The Local Volatility Model**
The local volatility model, introduced by Dupire (1994) and Derman-Kani (1994), specifies the risk-neutral asset dynamics as

$$dS_t = (r - q)S_t\,dt + \sigma(t, S_t)S_t\,dW_t^{\mathbb{Q}}$$

where $\sigma(t, S)$ is the **local volatility function**—a deterministic surface that makes the model Markovian in $(t, S)$ alone. Unlike the Black-Scholes model ($\sigma$ constant) or stochastic volatility models ($\sigma$ driven by a separate factor), local volatility produces a one-factor diffusion that is both complete (every European claim can be replicated) and consistent with any arbitrage-free implied volatility surface. The implied volatility $\sigma_{\text{imp}}(K,T)$ and the risk-neutral density $f(S_T \mid S_0)$ are connected via the **Breeden-Litzenberger formula** $f(K) = e^{rT}\partial^2 C/\partial K^2$, and the local volatility is the unique diffusion coefficient that generates this density.

**Dupire's Formula**
The local volatility surface is determined by observed European call prices $C(K,T)$ through Dupire's formula:

$$\sigma_{\text{loc}}^2(K,T) = \frac{\partial_T C + (r-q)K\partial_K C + qC}{\frac{1}{2}K^2\,\partial_{KK}C}$$

This is derived from the **forward (Fokker-Planck) PDE** satisfied by call prices as a function of strike and maturity. The numerator involves the calendar spread $\partial_T C$ (related to theta) and the denominator involves the butterfly spread $\partial_{KK}C$ (proportional to the risk-neutral density), so the local variance is the ratio of time decay to convexity. An equivalent formulation in terms of implied volatility is

$$\sigma_{\text{loc}}^2 = \frac{\sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}}T\partial_T\sigma_{\text{imp}} + 2(r-q)K\sigma_{\text{imp}}T\partial_K\sigma_{\text{imp}}}{(1 + Kd_1\sqrt{T}\partial_K\sigma_{\text{imp}})^2 + K^2\sigma_{\text{imp}}T(\partial_{KK}\sigma_{\text{imp}} - d_1(\partial_K\sigma_{\text{imp}})^2\sqrt{T})}$$

The derivation proceeds through **Tanaka's formula** and the occupation time formula, connecting the option price to the local time of the diffusion at the strike level.

**Relationship to Implied Volatility**
**Gyongy's theorem** (1986) provides the foundational link: the marginal distributions of any Ito process $(S_t)$ (including stochastic volatility models) can be matched by a Markovian diffusion with local volatility $\sigma_{\text{loc}}^2(t,K) = \mathbb{E}[\sigma_t^2 \mid S_t = K]$—the conditional expectation of instantaneous variance given the spot level. This **Markovian projection** means local volatility is the "average" of stochastic volatility paths passing through each $(t, K)$ point. At the ATM level for short maturities, $\sigma_{\text{imp}}(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}(t, S_0)\,dt$ plus higher-order corrections involving the curvature of $\sigma_{\text{loc}}$. The Berestycki-Busca-Florent formula provides the leading-order connection: $\sigma_{\text{imp}}(K,T) \approx \sigma_{\text{loc}}(\frac{1}{2}(S_0+K), \frac{1}{2}T)$ for small $T$—the implied volatility at strike $K$ approximates the local volatility evaluated at the midpoint in spot and time.

**Smile Dynamics and the Forward Smile Problem**
While local volatility perfectly reproduces today's implied volatility surface (static calibration), its predictions for **future** smiles are systematically wrong. Under local volatility, the smile moves in the **sticky-strike** regime: when spot rises, the ATM implied volatility drops (because $\sigma_{\text{loc}}$ is typically a decreasing function of $S$ for equities). Empirically, however, smiles exhibit partial **sticky-delta** behavior—the smile shifts with the spot rather than being anchored to fixed strikes. This discrepancy means local volatility:

- Underestimates the vol-of-vol (future smile variability)
- Produces forward smiles that are too flat compared to market-implied forward smiles
- Generates hedging ratios (deltas) that differ systematically from those of stochastic volatility models

The **forward smile problem** is the most important practical limitation: exotic options whose values depend on the future smile (cliquets, forward-starting options) are systematically mispriced.

**Calibration and Numerical Methods**
Constructing the local volatility surface from market data requires:

- **Interpolation and smoothing** of the implied volatility surface to obtain a smooth $C(K,T)$ from discrete market quotes. Cubic spline interpolation in strike and linear/quadratic interpolation in maturity, with SVI or SSVI parametrizations providing arbitrage-free functional forms. Over-smoothing loses smile detail; under-smoothing creates spurious oscillations in $\sigma_{\text{loc}}$
- **Numerical differentiation** of $C(K,T)$ to compute $\partial_T C$, $\partial_K C$, and $\partial_{KK}C$, amplifying noise in market data
- **FDM pricing**: the local volatility PDE $\partial_t V + \frac{1}{2}\sigma_{\text{loc}}^2(t,S)S^2\partial_{SS}V + (r-q)S\partial_S V - rV = 0$ is solved by finite differences with the calibrated $\sigma_{\text{loc}}(t,S)$ surface. Non-uniform grids in $S$ (clustering near the strike) improve accuracy
- **Monte Carlo**: simulating $dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(t,S_t)S_t\,dW_t$ requires interpolating $\sigma_{\text{loc}}$ at each time step and handling the boundary behavior carefully

**Calibration instability**—small perturbations in market quotes producing large oscillations in $\sigma_{\text{loc}}$—is an inherent ill-posedness of Dupire's formula (division by a small second derivative). Tikhonov regularization or parameterized functional forms mitigate this but introduce model bias.

!!! note "Role in the Book"
    Local volatility is the bridge between Black-Scholes (Chapter 6) and stochastic volatility (Chapter 14). Dupire's formula connects implied volatility (Chapter 12) to the forward PDE (Chapter 5). The model's inability to capture smile dynamics motivates the stochastic volatility framework, while Gyongy's theorem shows how local volatility arises as a Markovian projection of any diffusion model. The SABR model (Chapter 14) and Heston model (Chapter 16) address the forward smile limitations that local volatility cannot resolve.

---
