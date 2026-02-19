# Chapter 7: Extensions, American, and Exotic Options

This chapter extends the Black-Scholes framework beyond European vanilla options in four directions: relaxing idealized assumptions (constant volatility, frictionless markets, no dividends), incorporating early exercise (American options as free boundary and optimal stopping problems), introducing path-dependent and exotic payoffs (barrier, Asian, lookback, chooser, rainbow, cliquet, compound, and digital options), and modeling discontinuous price dynamics via the Merton jump-diffusion model. Each extension preserves the no-arbitrage principle while requiring new mathematical tools---optimal stopping, reflected processes, partial integro-differential equations, stochastic volatility, incomplete market theory---and numerical methods that go beyond closed-form solutions.

## Key Concepts

**Black-Scholes Extensions and Limitations**
The classical model's assumptions---constant volatility, frictionless markets, no dividends, continuous trading, Gaussian returns---are systematically confronted with empirical evidence and then relaxed. Market data reveals volatility smiles and skews (implied volatility varies with strike and maturity), fat tails (excess kurtosis of 6--8 for S&P 500 daily returns), volatility clustering, the leverage effect (negative correlation between returns and volatility), and price jumps from earnings announcements or crashes. A continuous dividend yield $q$ modifies the risk-neutral drift to $(r - q)S$, producing the Garman-Kohlhagen adjustment 

$$C = Se^{-qT}N(d_1) - Ke^{-rT}N(d_2)$$ 

with 

$$d_{1,2} = \frac{\ln(S/K) + (r - q \pm \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$ 

Discrete dividends require subtracting the present value of future dividends from the spot price. Transaction costs introduce the Leland correction 

$$\tilde{\sigma}^2 = \sigma^2\left(1 + \sqrt{2/\pi}\,\frac{k}{\sigma\sqrt{\Delta t}}\right)$$ 

and the Hoggard-Whalley-Wilmott optimal hedging bandwidth. Stochastic interest rates (Vasicek, CIR) and incomplete market pricing bounds further extend the framework. A practical model selection hierarchy ranges from Black-Scholes with strike-dependent implied volatility (Level 1) through local and jump-diffusion models (Level 2) to stochastic volatility (Level 3, Heston/SABR) and rough volatility (Level 4).

**Local Volatility Models**
Local volatility replaces constant $\sigma$ with a state-dependent function $\sigma_{\text{loc}}(t, S)$, so that 

$$dS_t = rS_t\,dt + \sigma_{\text{loc}}(t,S_t)S_t\,dW_t^{\mathbb{Q}}$$ 

Dupire's inversion formula recovers local volatility from observed call prices:

$$\sigma_{\text{loc}}^2(T, K) = \frac{\partial_T C + rK\,\partial_K C}{\frac{1}{2}K^2\,\partial_{KK}C}$$

Local volatility provides exact calibration to the vanilla implied volatility surface and maintains a complete market (one source of randomness, perfect hedging in theory). However, it predicts that the forward smile flattens over time---contrary to market behavior---leading to poor hedging performance and unrealistic smile dynamics. The CEV model $\sigma_{\text{loc}}(S) = \sigma_0 S^{\beta - 1}$ is a parametric special case. Regularization techniques (Tikhonov, spline smoothing, SVI parameterization) address the ill-posedness of numerical differentiation in Dupire's formula.

**Stochastic Volatility Models**
Stochastic volatility introduces a second random factor to capture volatility clustering, mean reversion, and the leverage effect. The general two-factor framework under $\mathbb{Q}$ is $dS_t = rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)}$ and $dv_t = \alpha(t,v_t)\,dt + \beta(t,v_t)\,dW_t^{(2)}$ with $d\langle W^{(1)},W^{(2)}\rangle_t = \rho\,dt$. The **Heston model** (1993) specifies CIR dynamics for variance:

$$dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$$

with Feller condition $2\kappa\theta \geq \xi^2$ ensuring positivity. Its affine structure yields a semi-analytical characteristic function enabling Fourier pricing: $C(K) = S_0 - \frac{Ke^{-rT}}{\pi}\int_0^\infty \text{Re}[e^{-iu\log K}\phi(u-i)/(iu)]\,du$. The option price satisfies a 2D PDE with a mixed derivative $\partial_{Sv}$ term from correlation. Other models include SABR (popular for rates/FX with the Hagan asymptotic formula), Hull-White (log-normal variance), and the 3/2 model. Stochastic volatility produces more realistic smile dynamics than local volatility but introduces market incompleteness---two sources of randomness but only one traded asset---requiring specification of a volatility risk premium $\lambda(t,v_t)$ to pin down the pricing measure.

**Incomplete Markets and Pricing Bounds**
In incomplete markets (stochastic volatility, jumps, transaction costs), multiple equivalent martingale measures exist and arbitrage-free prices form an interval $[\underline{\pi}(H), \overline{\pi}(H)]$ rather than a single value:

$$\underline{\pi}(H) = \inf_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H] \leq \pi(H) \leq \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H] = \overline{\pi}(H)$$

The superhedging price equals the minimum initial capital for a strategy dominating the payoff. Criteria for selecting a specific price include the minimal martingale measure (preserves orthogonal risk), variance-optimal measure, utility indifference pricing ($\pi^U(H)$ makes the investor indifferent between buying the claim or not, often using exponential utility $U(x) = -e^{-\gamma x}$), and entropy minimization. The FTAP for incomplete markets states: the market is arbitrage-free if and only if $\mathcal{Q} \neq \emptyset$, and complete if and only if $|\mathcal{Q}| = 1$.

**American Options and Optimal Stopping**
American options permit early exercise at any time $\tau \in [0, T]$, transforming the pricing problem into an optimal stopping problem:

$$V_0 = \sup_{\tau \in \mathcal{T}_{[0,T]}} \mathbb{E}^{\mathbb{Q}}\!\left[e^{-r\tau}\Phi(S_\tau)\right]$$

where $\mathcal{T}_{[0,T]}$ is the set of stopping times. The **free boundary problem** decomposes the $(S, t)$-plane into a continuation region $\mathcal{C} = \{(S,t) : V(S,t) > \Phi(S)\}$, where the Black-Scholes PDE holds, and an exercise region $\mathcal{E}$, where $V = \Phi$. The optimal exercise boundary $S^*(t)$ separates these regions and must be determined as part of the solution---a Stefan-type free boundary problem. The **smooth pasting condition** $\partial V/\partial S = \partial \Phi/\partial S$ at the boundary ensures $C^1$ regularity. The **complementarity formulation** compactly states: $\min(-\partial_t V - \mathcal{L}V + rV,\; V - \Phi) = 0$. Key results: American calls on non-dividend-paying stocks are never exercised early (since $C_{\text{Eu}} \geq S_t - Ke^{-r(T-t)} > S_t - K$); American puts always have positive early exercise premium $P_{\text{Am}} = P_{\text{Eu}} + \text{EEP}$; dividend-paying calls may be optimally exercised just before ex-dividend dates when $D > K(1 - e^{-r\Delta t})$. The **perpetual American put** is the only analytically tractable case: $V(S) = (S^*/S)^{\lambda}(K - S^*)$ with $S^* = \lambda K/(\lambda+1)$ and $\lambda = 2r/\sigma^2$. The **binomial tree** method prices American options via backward induction with $V_{n,j} = \max(\Phi(S_{n,j}),\; e^{-r\Delta t}[q\,V_{n+1,j+1} + (1-q)V_{n+1,j}])$, converging as $O(1/\sqrt{N})$ with oscillation; Richardson extrapolation $V_{\text{ext}} = 2V(2N) - V(N)$ accelerates convergence. The **Longstaff-Schwartz** least-squares Monte Carlo method uses regression $\hat{C}(t_k, S_{t_k}) = \sum_p \hat{\beta}_p\psi_p(S_{t_k})$ to estimate continuation values, producing a low-biased estimator $\hat{V}_{\text{LSM}} \leq V_{\text{Am}}$ that scales to high-dimensional problems. **Penalty methods** add $\lambda\max(\Phi - V, 0)$ to the PDE with error $O(1/\lambda)$, while **PSOR** directly solves the linear complementarity problem with exact constraint satisfaction.

**Exotic Options**
Exotic options have non-standard payoffs requiring specialized pricing techniques:

- **Barrier options** activate (knock-in) or deactivate (knock-out) when the underlying crosses a barrier $H$, producing eight standard types (up/down $\times$ in/out $\times$ call/put). The fundamental **in-out parity** $V_{\text{KI}} + V_{\text{KO}} = V_{\text{vanilla}}$ holds. Under GBM with continuous monitoring, closed-form prices use the **reflection principle** and the **joint law** of $(W_T, \sup_{t \leq T} W_t)$: $C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - (S_0/H)^{2\lambda-2}C_{\text{BS}}(H^2/S_0, K, T)$ where $\lambda = r/\sigma^2 + 1/2$. **Girsanov's theorem** removes the drift via measure change, with the factor $(S_0/H)^{2\lambda-2}$ encoding the Radon-Nikodym derivative. The **Broadie-Glasserman-Kou correction** $H_{\text{eff}} = H\cdot e^{\pm\beta\sigma\sqrt{T/m}}$ with $\beta \approx 0.5826$ adjusts for discrete monitoring bias, improving convergence from $O(1/\sqrt{m})$ to $O(1/m)$.
- **Asian options** depend on the path average $\bar{S} = \frac{1}{n}\sum_{i=1}^n S_{t_i}$ (discrete arithmetic) or $\bar{S}_{\text{geom}} = (\prod S_{t_i})^{1/n}$ (geometric). The arithmetic average has no closed-form distribution under GBM (sum of correlated lognormals), requiring Monte Carlo or moment-matching approximations. Geometric Asian options have lognormal averages with closed-form solutions using adjusted parameters $\hat{\sigma} = \sigma/\sqrt{3}$, serving as control variates. The variance reduction from averaging implies $C_{\text{Asian}} \leq C_{\text{vanilla}}$.
- **Lookback options** depend on the path extremum $M_T = \max_{t \leq T} S_t$ or $m_T = \min_{t \leq T} S_t$. Floating-strike lookback calls with payoff $S_T - m_T \geq 0$ are always in the money; the Goldman-Sosin-Gatto formula provides closed-form pricing under GBM. The ordering $V_{\text{vanilla}} \leq V_{\text{fixed lookback}} \leq V_{\text{floating lookback}}$ holds, with lookback premiums typically 2--3$\times$ vanilla prices.
- **Other exotics**: **Chooser options** decompose via put-call parity into a call plus a put with adjusted strike. **Rainbow options** (best-of, worst-of, spread) depend critically on correlation $\rho$ between assets. **Cliquet options** reset strikes periodically, accumulating $\sum_i \max(R_i - K_{\text{local}}, 0)$, with high sensitivity to the forward volatility structure. **Compound options** (options on options) use the bivariate normal distribution (Geske's formula). **Digital options** pay $Q\cdot\mathbf{1}_{\{S_T > K\}}$ with price $Qe^{-rT}N(d_2)$, and a vanilla call decomposes as asset-or-nothing minus $K$ units of cash-or-nothing.
- **Pricing methods**: Monte Carlo simulation with GBM path discretization $S_{t_{k+1}} = S_{t_k}\exp[(r - \frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}Z_k]$ converges at the dimension-independent rate $O(1/\sqrt{N})$. Antithetic variates pair each path with its negated draws; control variates using the European call or geometric Asian provide variance reduction factors of 2--100$\times$. Multi-asset Monte Carlo uses Cholesky decomposition for correlated simulation. Binomial trees extend to exotics by tracking additional state variables but face exponential state-space growth for Asian options and oscillatory convergence for barrier options.

**Merton Jump-Diffusion Model**
Real asset returns exhibit occasional large moves not captured by continuous diffusions. The Merton (1976) model adds compound Poisson jumps to GBM:

$$\frac{dS_t}{S_{t^-}} = (r - \lambda \bar{k})\,dt + \sigma\,dW_t + (J - 1)\,dN_t$$

where $N_t$ is a Poisson process with intensity $\lambda$, $J$ is the random jump multiplier with $\ln J \sim N(\mu_J, \sigma_J^2)$, and $\bar{k} = \mathbb{E}[J - 1] = e^{\mu_J + \sigma_J^2/2} - 1$ is the compensator ensuring the drift correction. The **Ito formula for jump processes** adds a finite-variation jump term $\sum_{s \leq t}[f(X_s) - f(X_{s^-})]$ to the standard Ito formula. The **characteristic function** has the Levy-Khintchine form $\phi(u) = \exp(iu\mu't - \frac{1}{2}\sigma^2 u^2 t + \lambda t(e^{iu\mu_J - \sigma_J^2 u^2/2} - 1))$, enabling Fourier pricing. The **Merton series formula** decomposes the option price as a Poisson-weighted sum of Black-Scholes prices:

$$C = \sum_{n=0}^{\infty} \frac{e^{-\lambda' T}(\lambda' T)^n}{n!} C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)$$

with $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$ and $r_n = r - \lambda\bar{k} + n\ln(1+\bar{k})/T$. The jump-diffusion PDE becomes a **partial integro-differential equation** (PIDE) $\partial_t V + \frac{1}{2}\sigma^2 S^2 V_{SS} + (r-\lambda\bar{k})SV_S - rV + \lambda\int[V(Sy) - V]\nu(dy) = 0$, solved numerically using implicit schemes for the differential part and explicit treatment of the integral term. The model is **incomplete**---jump risk cannot be hedged with the stock alone---requiring calibration to market prices to implicitly select a pricing measure. Greeks acquire additional jump-sensitivity terms: delta is reduced near ATM, and total vega decomposes into $\mathcal{V}_\sigma + \mathcal{V}_\lambda + \mathcal{V}_{\mu_J} + \mathcal{V}_{\sigma_J}$. Calibration to the implied volatility smile exploits the model's ability to generate short-maturity skew through jump parameters ($\mu_J$ controls skew, $\sigma_J$ controls convexity, $\lambda$ controls overall smile level). The **Kou double-exponential model** offers asymmetric jumps with memoryless property for better tractability. The **Bates model** combines Heston stochastic volatility with Merton jumps (SVJ), providing both short-maturity skew from jumps and long-maturity smile persistence from stochastic volatility. Monte Carlo simulation of jump-diffusion generates Poisson jump counts and log-normal jump sizes at each time step alongside the diffusion component.

!!! note "Role in the Book"
    This chapter bridges the idealized Black-Scholes world (Chapter 6) and the more sophisticated modeling frameworks that follow. American option pricing connects to free boundary PDEs (Chapter 5) and numerical methods (Chapter 8). Exotic option pricing via the reflection principle builds on Brownian motion theory (Chapter 2). The Merton jump-diffusion model motivates stochastic volatility (Chapter 14), Fourier pricing (Chapter 9), and the Bates extension of the Heston model (Chapter 16). Local volatility and incomplete market theory lay the groundwork for the calibration and advanced modeling techniques in later chapters.

---
