# Chapter 13: Local Volatility

This chapter develops the local volatility framework, in which the diffusion coefficient $\sigma(t, S)$ is a deterministic function of time and spot price chosen to exactly reproduce all observed European option prices. Starting from the Breeden-Litzenberger connection between implied volatility and risk-neutral density, we derive Dupire's formula via both the forward Kolmogorov (Fokker-Planck) equation and Tanaka's formula, develop the explicit conversion from implied to local volatility surfaces, study the model's structural properties through Gyongy's theorem and asymptotic expansions, analyze its fundamental limitations---particularly its failure to capture realistic smile dynamics and the forward smile problem---and present the numerical methods needed for surface construction, calibration, and pricing.

## Key Concepts

### **Implied Volatility and Risk-Neutral Density**
The implied volatility surface $\sigma_{\text{imp}}(K,T)$ serves as a normalized coordinate system for the risk-neutral distribution. The Breeden-Litzenberger formula $f(K) = e^{rT}\partial^2 C/\partial K^2$ recovers the risk-neutral density from call prices, and the shape of the implied volatility surface directly encodes the distribution's moments: ATM implied volatility relates to variance, the slope $\partial\sigma_{\text{imp}}/\partial K$ at ATM relates to skewness via $\text{Skew}^{\mathbb{Q}} \approx -6F\mathcal{S}\sqrt{T}/\sigma_{\text{ATM}}$, and the curvature $\partial^2\sigma_{\text{imp}}/\partial K^2$ relates to excess kurtosis via $\text{Kurt}^{\mathbb{Q}} - 3 \approx 12F^2\mathcal{C}T$. The variance swap payoff connects to the model-free implied variance through $\text{Var}^{\mathbb{Q}}(S_T) = 2e^{rT}\left(\int_0^F P(K)/K^2\,dK + \int_F^{\infty} C(K)/K^2\,dK\right)$. Smile patterns encode distributional shapes: a flat smile implies lognormal density, downward skew implies negative skewness (equity indices), a U-shaped smile implies excess kurtosis (FX markets), and Lee's moment formula constrains the wings.

### **The Local Volatility Model and Dupire's Formula**
The local volatility model, introduced by Dupire (1994) and Derman-Kani (1994), specifies the risk-neutral asset dynamics as

$$dS_t = (r - q)S_t\,dt + \sigma(t, S_t)S_t\,dW_t^{\mathbb{Q}}$$

where $\sigma(t, S)$ is the **local volatility function**---a deterministic surface that makes the model Markovian in $(t, S)$ alone. Unlike the Black-Scholes model ($\sigma$ constant) or stochastic volatility models ($\sigma$ driven by a separate factor), local volatility produces a one-factor diffusion that is both complete (every European claim can be replicated) and consistent with any arbitrage-free implied volatility surface. The local volatility surface is determined by observed European call prices $C(K,T)$ through Dupire's formula:

$$\sigma_{\text{loc}}^2(K,T) = \frac{\partial_T C + (r-q)K\partial_K C + qC}{\frac{1}{2}K^2\,\partial_{KK}C}$$

The numerator involves the calendar spread $\partial_T C$ (related to theta) and the denominator involves the butterfly spread $\partial_{KK}C$ (proportional to the risk-neutral density), so the local variance is the ratio of time decay to convexity. In forward coordinates, this simplifies to $\sigma_{\text{loc}}^2 = 2(\partial_T C)/(K^2 \partial_{KK}C)$.

### **Dupire Formula Derivation and Tanaka's Formula**
The Dupire formula can be derived via two complementary approaches. The **forward Kolmogorov (Fokker-Planck)** approach starts from the forward PDE satisfied by the transition density $\partial_t p = -\partial_S[(r-q)Sp] + \frac{1}{2}\partial_{SS}[\sigma_{\text{loc}}^2 S^2 p]$, differentiates the call price with respect to maturity, and solves for $\sigma_{\text{loc}}^2$. An alternative derivation uses **integration by parts** on the Feynman-Kac representation $C = e^{-rT}\int_K^{\infty}(s-K)p\,ds$, yielding the key partial derivatives $C_K = -e^{-rT}\int_K^{\infty}p\,ds$ and $C_{KK} = e^{-rT}p(K,T)$. The **Tanaka formula** approach extends Ito's lemma to the non-smooth call payoff $(S_T - K)^+$ using distributional derivatives: the first derivative is the Heaviside function $\mathbf{1}(S_T > K)$ and the second derivative is the Dirac delta $\delta(S_T - K)$. Applying Tanaka's formula gives $d(S_T - K)^+ = \mathbf{1}(S_T > K)\,dS_T + \frac{1}{2}\delta(S_T - K)\sigma^2(S_T,T)S_T^2\,dt$, and taking expectations recovers the Dupire PDE $C_T + rKC_K - \frac{1}{2}\sigma^2(K,T)K^2 C_{KK} = 0$.

### **From Implied to Local Volatility**
An equivalent formulation of Dupire's formula directly in terms of implied volatility is

$$\sigma_{\text{loc}}^2 = \frac{\sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}}T\partial_T\sigma_{\text{imp}} + 2(r-q)K\sigma_{\text{imp}}T\partial_K\sigma_{\text{imp}}}{(1 + Kd_1\sqrt{T}\partial_K\sigma_{\text{imp}})^2 + K^2\sigma_{\text{imp}}T(\partial_{KK}\sigma_{\text{imp}} - d_1(\partial_K\sigma_{\text{imp}})^2\sqrt{T})}$$

The transformation from $(K,T)$ coordinates to log-moneyness and variance coordinates $(y,w)$ with $y = \log(K/S_0 e^{rT})$ and $w = \sigma_{\text{imp}}^2 T$ simplifies the relationship to $\sigma^2 = \sigma_{\text{imp}}^2 C_w / [\frac{1}{2}(C_{yy} - C_y)]$, revealing the elegant structure of the implied-to-local volatility mapping. At the money, a useful approximation is $\sigma_{\text{loc}}^2(F,T) \approx \sigma_{\text{imp}}^2(F,T) + 2T\sigma_{\text{imp}}(F,T)\partial_T\sigma_{\text{imp}}|_{K=F}$.

### **Gyongy's Theorem and Markovian Projection**
**Gyongy's theorem** (1986) provides the foundational link: the marginal distributions of any Ito process $(S_t)$ (including stochastic volatility models) can be matched by a Markovian diffusion with local volatility $\sigma_{\text{loc}}^2(t,K) = \mathbb{E}[\sigma_t^2 \mid S_t = K]$---the conditional expectation of instantaneous variance given the spot level. This **Markovian projection** means local volatility is the "average" of stochastic volatility paths passing through each $(t, K)$ point.

### **Relationship to Implied Volatility and Forward PDE**
The forward Kolmogorov (Fokker-Planck) PDE governs the evolution of the transition density forward in time, providing the theoretical foundation for Dupire's formula as an inversion of this PDE. The Berestycki-Busca-Florent formula provides the leading-order connection: $\sigma_{\text{imp}}(K,T) \approx \sigma_{\text{loc}}(\frac{1}{2}(S_0+K), \frac{1}{2}T)$ for small $T$---the implied volatility at strike $K$ approximates the local volatility evaluated at the midpoint in spot and time. At the ATM level for short maturities, $\sigma_{\text{imp}}(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}(t, S_0)\,dt$ plus higher-order corrections.

### **Smile Dynamics and the Static vs. Dynamic Smile**
While local volatility perfectly reproduces today's implied volatility surface (static calibration), its predictions for **future** smiles are systematically wrong. Under local volatility, the smile moves in the **sticky-strike** regime: when spot rises, the ATM implied volatility drops (because $\sigma_{\text{loc}}$ is typically a decreasing function of $S$ for equities). Empirically, however, smiles exhibit partial **sticky-delta** behavior---the smile shifts with the spot rather than being anchored to fixed strikes. This discrepancy between static consistency and dynamic behavior means local volatility underestimates the vol-of-vol (future smile variability) and generates hedging ratios (deltas) that differ systematically from those of stochastic volatility models.

### **The Forward Smile Problem and Bridge to Stochastic Volatility**
The **forward smile problem** is the most important practical limitation: local volatility produces forward smiles that are too flat compared to market-implied forward smiles. Exotic options whose values depend on the future smile (cliquets, forward-starting options) are systematically mispriced. This failure motivates the transition to stochastic volatility models, which introduce a separate variance factor to capture realistic smile dynamics. Local volatility serves as a bridge: Gyongy's theorem shows how local volatility arises as a Markovian projection of any diffusion model, while its dynamic limitations demonstrate why additional degrees of freedom are needed.

### **Calibration Instability**
**Calibration instability**---small perturbations in market quotes producing large oscillations in $\sigma_{\text{loc}}$---is an inherent ill-posedness of Dupire's formula (division by a small second derivative). Sources include non-uniqueness of parameter sets, sensitivity to bid-ask noise in option prices, sparse data at extreme strikes/maturities requiring extrapolation, and ill-posed inverse problems where high-frequency oscillations in $\sigma_{\text{loc}}(S,t)$ can match prices equally well. Practical mitigation strategies include Tikhonov regularization, parameterized functional forms, multi-stage calibration (fitting liquid instruments first), parameter anchoring to realistic ranges, and daily recalibration with incremental adjustment using previous parameters as initialization.

### **Numerical Methods: Surface Construction, Interpolation, FDM, and Monte Carlo**
Constructing the local volatility surface from market data requires careful numerical treatment across several stages:

- **Interpolation and smoothing** of the implied volatility surface to obtain a smooth $C(K,T)$ from discrete market quotes. Cubic spline interpolation in strike and linear/quadratic interpolation in maturity, with SVI or SSVI parametrizations providing arbitrage-free functional forms. Monotonicity ($C_K \leq 0$), convexity ($C_{KK} \geq 0$), and calendar monotonicity ($C_T \geq 0$) constraints must be enforced.
- **Local volatility surface construction** via numerical differentiation of $C(K,T)$ to compute $\partial_T C$, $\partial_K C$, and $\partial_{KK}C$, using centered finite differences while managing noise amplification and division by small second derivatives in the wings.
- **FDM pricing**: the local volatility PDE $\partial_t V + \frac{1}{2}\sigma_{\text{loc}}^2(t,S)S^2\partial_{SS}V + (r-q)S\partial_S V - rV = 0$ is solved by finite differences with the calibrated $\sigma_{\text{loc}}(t,S)$ surface. Non-uniform grids in $S$ (clustering near the strike) improve accuracy.
- **Monte Carlo simulation**: simulating $dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(t,S_t)S_t\,dW_t$ requires interpolating $\sigma_{\text{loc}}$ at each time step and handling the boundary behavior carefully, particularly near regions where the local volatility surface becomes extreme.

!!! note "Role in the Book"
    Local volatility is the bridge between Black-Scholes (Chapter 6) and stochastic volatility (Chapter 14). Dupire's formula connects implied volatility (Chapter 12) to the forward PDE (Chapter 5). The Breeden-Litzenberger formula and Tanaka's formula provide rigorous distributional foundations for extracting both the risk-neutral density and the local volatility surface from market data. The model's inability to capture smile dynamics motivates the stochastic volatility framework, while Gyongy's theorem shows how local volatility arises as a Markovian projection of any diffusion model. The SABR model (Chapter 14) and Heston model (Chapter 16) address the forward smile limitations that local volatility cannot resolve.

---
