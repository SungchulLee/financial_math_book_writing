# Chapter 7: Extensions, American, and Exotic Options

This chapter extends the Black-Scholes framework beyond European vanilla options in three directions: relaxing idealized assumptions (dividends, discrete hedging, transaction costs), incorporating early exercise (American options as free boundary problems), introducing path-dependent and exotic payoffs, and modeling discontinuous price dynamics via jump-diffusion. Each extension preserves the no-arbitrage principle while requiring new mathematical tools—optimal stopping, reflected processes, partial integro-differential equations—and numerical methods that go beyond closed-form solutions.

## Key Concepts

**Black-Scholes Extensions**
The classical model's assumptions—constant volatility, frictionless markets, no dividends, continuous trading—are systematically relaxed. A continuous dividend yield $q$ modifies the risk-neutral drift to $(r - q)S$, producing the Garman-Kohlhagen adjustment $C = Se^{-qT}N(d_1) - Ke^{-rT}N(d_2)$ with $d_{1,2} = (\ln(S/K) + (r - q \pm \frac{1}{2}\sigma^2)T)/(\sigma\sqrt{T})$. Discrete dividends require careful treatment of the ex-dividend price jump $S_{t_d^+} = S_{t_d^-} - D$, typically handled by subtracting the present value of future dividends from the spot price. Time-dependent volatility $\sigma(t)$ replaces $\sigma^2 T$ with $\int_0^T \sigma^2(s)\,ds$ in the Black-Scholes formula, motivating the concept of integrated variance. Transaction costs introduce the Leland correction $\tilde{\sigma}^2 = \sigma^2(1 + \sqrt{2/\pi}\,k/(\sigma\sqrt{\Delta t}))$, where $k$ is the round-trip cost, modifying the hedging bandwidth and leading to the Hoggard-Whalley-Wilmott nonlinear PDE. These extensions motivate the local volatility, stochastic volatility, and incomplete market frameworks developed in later chapters.

**American Options and Optimal Stopping**
American options permit early exercise at any time $\tau \in [0, T]$, transforming the pricing problem into an optimal stopping problem:

$$V_0 = \sup_{\tau \in \mathcal{T}_{[0,T]}} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r\tau}\Phi(S_\tau)\right]$$

where $\mathcal{T}_{[0,T]}$ is the set of stopping times. The **free boundary problem** decomposes the $(S, t)$-plane into a continuation region $\mathcal{C} = \{(S,t) : V(S,t) > \Phi(S)\}$, where the Black-Scholes PDE holds, and an exercise region $\mathcal{E}$, where $V = \Phi$. The optimal exercise boundary $S^*(t)$ separates these regions and must be determined as part of the solution—making this a Stefan-type free boundary problem. The **smooth pasting condition** $\partial V/\partial S = \partial \Phi/\partial S$ at the boundary ensures $C^1$ regularity. For American puts without dividends, the **early exercise premium** representation decomposes the price as $P_{\text{Am}} = P_{\text{Eu}} + \int_0^T e^{-rt} r K \,\mathbb{Q}(S_t \leq S^*(t))\,dt$. Key results: American calls on non-dividend-paying stocks are never exercised early; American puts always have positive early exercise premium; dividend-paying calls may be optimally exercised just before ex-dividend dates. Numerical approaches include finite difference methods with the **linear complementarity** formulation $\min(\mathcal{L}V, V - \Phi) = 0$, the **projected SOR** (PSOR) algorithm, the **penalty method** adding $\rho\max(\Phi - V, 0)$ to the PDE, and the **Longstaff-Schwartz** least-squares Monte Carlo method using regression to estimate continuation values.

**Exotic Options**
Exotic options have non-standard payoffs requiring specialized pricing techniques:

- **Barrier options** activate (knock-in) or deactivate (knock-out) when the underlying crosses a barrier $H$. For down-and-out calls under GBM, the **reflection principle** and the joint law of $(W_T, \min_{t \leq T} W_t)$ yield closed-form prices. **Girsanov's theorem** provides an alternative derivation by removing the drift and using the image method. Key identities: $\text{In} + \text{Out} = \text{Vanilla}$; the **put-call symmetry** under GBM relates up-barriers to down-barriers
- **Asian options** depend on the path average $A_T = \frac{1}{T}\int_0^T S_t\,dt$ (continuous) or $\bar{S} = \frac{1}{n}\sum_{i=1}^n S_{t_i}$ (discrete). The arithmetic average has no closed-form distribution under GBM, requiring Monte Carlo simulation or moment-matching approximations. Geometric Asian options have log-normal averages and closed-form solutions, serving as control variates
- **Lookback options** depend on the path extremum $M_T = \max_{t \leq T} S_t$ or $m_T = \min_{t \leq T} S_t$. Floating-strike lookback calls with payoff $(S_T - m_T)^+$ have closed-form solutions using the joint density of $(W_T, \min W_t)$
- **Multi-asset options**—basket, rainbow, spread, quanto—require modeling correlations between underlyings and generally demand Monte Carlo methods or copula-based approaches

**Merton Jump-Diffusion Model**
Real asset returns exhibit occasional large moves not captured by continuous diffusions. The Merton (1976) model adds compound Poisson jumps to GBM:

$$\frac{dS_t}{S_{t^-}} = (\mu - \lambda \bar{k})\,dt + \sigma\,dW_t + (J - 1)\,dN_t$$

where $N_t$ is a Poisson process with intensity $\lambda$, $J$ is the random jump multiplier with $\ln J \sim N(\mu_J, \sigma_J^2)$, and $\bar{k} = \mathbb{E}[J - 1] = e^{\mu_J + \sigma_J^2/2} - 1$ is the compensator ensuring the drift correction. The **Ito formula for jump processes** adds a finite-variation jump term $\sum_{s \leq t}[f(X_s) - f(X_{s^-})]$ to the standard Ito formula. The **characteristic function** has the Levy-Khintchine form $\phi(u) = \exp(iu\mu't - \frac{1}{2}\sigma^2 u^2 t + \lambda t(e^{iu\mu_J - \sigma_J^2 u^2/2} - 1))$, enabling Fourier pricing. The **Merton series formula** decomposes the option price as a Poisson-weighted sum of Black-Scholes prices:

$$C = \sum_{n=0}^{\infty} \frac{e^{-\lambda' T}(\lambda' T)^n}{n!} C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)$$

with $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$ and $r_n = r - \lambda\bar{k} + n\ln(1+\bar{k})/T$. The model is **incomplete**—jump risk cannot be hedged with the stock alone—requiring either risk-neutral calibration to market prices or equilibrium arguments to pin down the pricing measure. The jump-diffusion PDE becomes a **partial integro-differential equation** (PIDE), and Greeks acquire additional jump-sensitivity terms. Calibration to the implied volatility smile exploits the model's ability to generate short-maturity skew through jump parameters.

!!! note "Role in the Book"
    This chapter bridges the idealized Black-Scholes world (Chapter 6) and the more sophisticated modeling frameworks that follow. American option pricing connects to free boundary PDEs (Chapter 5) and numerical methods (Chapter 8). Exotic option pricing via the reflection principle builds on Brownian motion theory (Chapter 2). The Merton jump-diffusion model motivates stochastic volatility (Chapter 14), Fourier pricing (Chapter 9), and the Bates extension of the Heston model (Chapter 16).

---
