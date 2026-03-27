# Chapter 17: Calibration

This chapter treats model calibration as an inverse problem: given observed market prices, recover model parameters that reproduce them. Starting from the forward pricing map and its inversion, we develop the mathematical framework for ill-posedness and regularization, then apply it to local and stochastic volatility calibration. The chapter addresses dynamic consistency of recalibration over time, filtering for time-varying parameters, and quantification of the model risk that calibration uncertainty introduces into pricing and hedging.

## Key Concepts

### Calibration as an Inverse Problem

Every pricing model contains parameters that must be inferred from market data. This inference---calibration---is fundamentally an inverse problem, and its mathematical structure determines whether calibrated parameters are reliable or dangerously unstable.

A parametric model with parameter vector $\theta \in \Theta \subset \mathbb{R}^d$ defines a **forward pricing map** $F:\Theta \to \mathbb{R}^m$ that sends parameters to model prices across $m$ traded instruments: $F(\theta) = (P_1(\theta), \ldots, P_m(\theta))$. Calibration seeks the inverse: $\hat{\theta} \in \arg\min_\theta \mathcal{L}(F(\theta), y)$ where $y$ is market data and $\mathcal{L}$ is a loss function.

The Jacobian $J(\theta) = \nabla_\theta F(\theta) \in \mathbb{R}^{m \times d}$ governs local sensitivity via $F(\theta_0 + \Delta\theta) \approx F(\theta_0) + J(\theta_0)\Delta\theta$. Small singular values of $J$ amplify data noise into large parameter errors, making the inverse unstable. **Identifiability**---whether the data uniquely determine parameters---is analyzed via the SVD $J = U\Sigma V^\top$: the model is **structurally identifiable** if $F(\theta_1) = F(\theta_2) \Rightarrow \theta_1 = \theta_2$, and **practically identifiable** when parameters are distinguishable within the noise level. The condition number $\kappa = \sigma_1/\sigma_d$ measures sensitivity, with very small $\sigma_d$ indicating a nearly unidentifiable direction.

Calibration is typically **ill-posed** in the sense of Hadamard: existence, uniqueness, and stability can all fail. The three failure mechanisms are: (1) **incomplete information**---finite instruments versus functional degrees of freedom; (2) **noisy data**---bid--ask spreads, stale quotes, and microstructure noise amplified through the unstable inverse; and (3) **model misspecification**---$y \notin \text{Range}(F)$. Non-uniqueness arises from flat directions in the loss landscape, over-parameterization, and multiple local minima.

### Optimization Algorithms for Calibration

Minimizing the calibration objective is a nonlinear optimization problem, often non-convex, sometimes noisy (when pricing involves Monte Carlo), and always subject to constraints. The choice of optimizer determines both the quality and computational cost of calibration.

**Local methods** form the core toolkit. Gradient descent $\theta^{(k+1)} = \theta^{(k)} - \alpha_k \nabla\mathcal{L}(\theta^{(k)})$ is simple but slow. The Gauss--Newton method $(J^\top WJ)\Delta\theta = -J^\top Wr$ is effective for mildly nonlinear problems. The **Levenberg--Marquardt** algorithm $(J^\top WJ + \lambda I)\Delta\theta = -J^\top Wr$---the standard workhorse---interpolates between Gauss--Newton (small $\lambda$) and gradient descent (large $\lambda$), with adaptive damping based on step acceptance. **Trust-region methods** constrain $\|\Delta\theta\| \le \Delta_k$ with radius adjusted by the actual-to-predicted reduction ratio $\rho_k$.

**Global methods** address multiple local minima: **differential evolution** creates mutants $v_i = \theta_{r_1} + F(\theta_{r_2} - \theta_{r_3})$ with mutation and crossover; **particle swarm optimization** balances cognitive and social components; **simulated annealing** accepts worse solutions with probability $\exp(-\Delta\mathcal{L}/T)$ under a cooling schedule; and **basin hopping** combines local optimization with random perturbations.

**Derivative-free methods**---Nelder--Mead simplex, Powell's conjugate directions, and **Bayesian optimization** (Gaussian process surrogate with expected improvement acquisition)---are essential when pricing involves Monte Carlo noise. Constraint handling uses projection, barrier/interior-point methods, sigmoid transformations, or augmented Lagrangian. Computational cost depends critically on the pricing method: $\mathcal{O}(1)$ for Black--Scholes, $\mathcal{O}(N_{\text{FFT}})$ for Heston via FFT, $\mathcal{O}(N_{\text{paths}} \times N_{\text{steps}})$ for Monte Carlo.

### Static Calibration to Vanilla Options

The simplest calibration task---fitting a model to a cross-section of vanilla option prices at a single point in time---already raises fundamental questions about objective function design, weighting, and market data quality.

Calibration targets either option prices or **implied volatilities** $\sigma_{\text{impl}}(K,T)$. Price-space objectives $\mathcal{L} = \frac{1}{2}\sum_j w_j(P_j(\theta) - P_j^{\text{mkt}})^2$ align with replication cost but suffer from heterogeneous magnitudes (deep ITM options dominate). Implied-vol objectives $\mathcal{L} = \frac{1}{2}\sum_j w_j(\sigma_j^{\text{impl}}(\theta) - \sigma_j^{\text{impl,mkt}})^2$ provide uniform scaling and match market conventions but implicitly re-weight errors through vega.

**Robust loss functions** reduce sensitivity to outliers: Huber loss $\ell_H(r) = \frac{1}{2}r^2$ for $|r| \le \delta$ and $\delta|r| - \frac{1}{2}\delta^2$ for $|r| > \delta$; $\ell_1$ loss; and multi-objective formulations. **Weighting and market liquidity** are critical: near-the-money options are most liquid and should receive higher weight; vega-weighted objectives $w_j \propto 1/\nu_j^2$ normalize for option price sensitivity; and maturity balancing prevents one tenor from dominating.

The **implied volatility surface** is typically constructed in log-moneyness coordinates $k = \log(K/F_T)$ with arbitrage filtering---calendar monotonicity in total variance $\partial_T w \ge 0$ and butterfly convexity in strike $\partial_{KK}C \ge 0$---before calibration proceeds.

### Regularization and Stability

Perfect fit to noisy data is neither achievable nor desirable. Regularization trades a small bias for a large reduction in variance, producing parameters that are more stable, more interpretable, and ultimately more useful for hedging.

**Tikhonov regularization** $\min_\theta \frac{1}{2}\|F(\theta)-y\|_W^2 + \frac{\lambda}{2}\|L(\theta-\theta_0)\|^2$ stabilizes ill-conditioned problems by damping small singular values, where $L$ is a regularization matrix (identity for standard shrinkage, a finite-difference operator for smoothness). It admits a **Bayesian interpretation** as the MAP estimator under a Gaussian prior $\theta \sim \mathcal{N}(\theta_0, (\lambda L^\top L)^{-1})$. Selection of $\lambda$ uses the **L-curve method**, the **discrepancy principle**, or **cross-validation**.

Beyond parameter shrinkage, **penalization and smoothness constraints** encode structural beliefs: finite-difference penalties $\lambda\sum_i(\theta_{i+1} - \theta_i)^2$, monotonicity and convexity constraints from no-arbitrage, and positivity requirements. **Time stability**---smooth day-to-day parameter evolution via $\lambda\|\theta - \hat{\theta}_{t-1}\|^2$---is often the decisive practical criterion.

### Calibration of Local Volatility

The local volatility model $dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(t,S_t)S_t\,dW_t$ achieves exact fit to a continuum of vanilla prices, but recovering $\sigma_{\text{loc}}$ from market data is a severely ill-posed problem because it requires differentiating noisy, discrete observations.

**Dupire's inversion** $\sigma_{\text{loc}}^2 = 2(\partial_T C + (r-q)K\partial_K C - qC)/(K^2\partial_{KK}C)$ requires second derivatives of option prices with respect to strike. For the central difference approximation, noise amplification scales as $\sigma_\varepsilon/h^2$, with optimal step size $h^* \sim (\sigma_\varepsilon/|C^{(4)}|)^{1/4}$ balancing noise amplification against truncation error.

**Spline-based differentiation**---fitting smoothing splines $\min\sum_i(S(K_i) - C_i)^2 + \lambda\int(S''(K))^2\,dK$ and differentiating analytically---avoids step-size selection and handles non-uniform strike spacing. Working in **total variance coordinates** $w(k,T) = T\sigma_{\text{impl}}^2(k,T)$ with $k = \log(K/F_T)$ simplifies the Dupire formula and makes calendar arbitrage equivalent to $\partial_T w \ge 0$.

**SVI parameterization** $w(k) = a + b(\rho(k-m) + \sqrt{(k-m)^2+\sigma^2})$ provides a parsimonious 5-parameter smile fit with analytic derivatives. Butterfly-free sufficient conditions include $b(1+|\rho|) \le 4/T$ and $a + b\sigma\sqrt{1-\rho^2} \ge 0$. **SSVI (Surface SVI)** extends to the full $(k,T)$ surface with calendar arbitrage freedom built in by construction. Instability concentrates near extreme strikes, sparse maturities, and short expiries.

### Dynamic Calibration and Time Consistency

A model calibrated today may need different parameters tomorrow. If these parameter shifts are inconsistent with the model's own dynamics, the result is unexplained P&L and unstable hedges---the recalibration problem.

Models recalibrated daily face the issue that parameter shifts $\theta_t \to \theta_{t+\Delta t}$ generate residual P&L beyond what Greeks predict. Sources include genuine regime shifts, quote noise, model misspecification, and optimizer sensitivity to initialization.

**Forward consistency** requires that model-implied parameter evolution match fresh recalibration: $\hat{\theta}_{t+\Delta t}^{\text{calib}} \approx \Phi_{t \to t+\Delta t}(\hat{\theta}_t, \omega)$. The **HJM framework** achieves this for interest rates by modeling the entire forward rate curve as the state variable, with the no-arbitrage drift condition ensuring recalibration is unnecessary for curve shape. Low-dimensional equity models (Heston, SABR) are structurally forward-inconsistent because their finite-parameter state cannot capture arbitrary surface dynamics.

Approaches to restore consistency include **state-extended models** (Bergomi's variance curve model), **stochastic parameter models**, the **consistent recalibration (CRC) framework**, and market models for volatility instruments. Practitioners often use exponential parameter smoothing, hierarchical calibration (freezing slowly-moving parameters while recalibrating fast-moving ones), and Tikhonov regularization toward prior values.

### Filtering for Time-Varying Parameters

Rather than recalibrating from scratch at each time step, filtering treats parameters as evolving state variables and updates them optimally as new data arrives---providing smooth parameter paths with automatic uncertainty quantification.

The **state-space formulation** has state equation $\theta_{t+1} = f(\theta_t) + \eta_t$ with $\eta_t \sim \mathcal{N}(0,Q)$ and observation equation $y_t = h(\theta_t) + \varepsilon_t$ with $\varepsilon_t \sim \mathcal{N}(0,R)$, where $h$ is the pricing function and $Q$, $R$ encode parameter uncertainty growth and market data noise respectively.

The **Kalman filter** provides exact updates for linear-Gaussian systems: predict $\hat{\theta}_{t|t-1} = A\hat{\theta}_{t-1|t-1}$, $P_{t|t-1} = AP_{t-1|t-1}A^\top + Q$; update via Kalman gain $K_t = P_{t|t-1}H^\top(HP_{t|t-1}H^\top + R)^{-1}$. The **extended Kalman filter (EKF)** linearizes $H_t = \nabla_\theta h(\hat{\theta}_{t|t-1})$ at the current estimate. The **unscented Kalman filter (UKF)** propagates sigma points through nonlinear functions, capturing second-order accuracy without explicit Jacobians. **Particle filters** (sequential Monte Carlo) represent the posterior with weighted samples for general non-Gaussian problems.

For the **Heston model**, the augmented state vector $\theta_t = (v_t, \kappa, \bar{v}, \sigma_v, \rho)^\top$ typically uses a random walk state equation with $Q$ encoding beliefs about parameter stability. Filter hyperparameters are estimated via maximum likelihood, cross-validation, or expert judgment.

### Model Risk from Calibration

Calibration uncertainty does not end at the parameter estimates---it propagates through to every price, Greek, and hedge ratio the model produces. Quantifying this propagation is essential for risk management.

Parameter error propagates via the first-order approximation $\Delta P \approx -\nabla_\theta P(\hat{\theta})^\top \Delta\theta$, with price variance $\text{Var}(P) \approx \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P$ where $\Sigma_\theta$ is the parameter covariance. Price variance decomposes by parameter: $\text{Contribution}_i = (\partial P/\partial\theta_i)^2\sigma_{\theta_i}^2$, with spot volatility $v_0$ dominating short-dated options and correlation $\rho$ critical for skew-sensitive instruments.

**Exotic options amplify calibration error**: a barrier option may exhibit $5$--$10\%$ price uncertainty from $5\%$ correlation error, far exceeding vanilla sensitivity. Greeks are equally affected: $\Delta(\hat{\theta}) \neq \Delta(\theta^\star)$ produces systematic hedging errors that accumulate over time.

**Robust calibration criteria** combine: stability under data perturbations, avoidance of extreme parameters, reasonable out-of-sample performance, temporal smoothness, and stable Greeks. **Model risk governance** under regulatory expectations (OCC SR 11-7) requires sensitivity analysis, documentation of parameter uncertainty, position limits for high-model-sensitivity products, and reserves for hedging error.

### Stochastic Volatility Calibration Pipelines

Different models excel at different tasks, and practical calibration often involves running multiple models and comparing their outputs for robustness.

Heston calibration typically uses semi-analytic FFT pricing with Levenberg--Marquardt optimization, requiring careful initialization due to non-convexity and parameter entanglement between $\kappa$ and $\bar{v}$. SABR calibration leverages Hagan's asymptotic approximation formula for rapid per-slice fits with 4 intuitive parameters, excelling near ATM but less accurate at far OTM strikes. Differential evolution and other global search methods address multi-modality.

**Cross-model comparison** reveals complementary strengths: SABR provides excellent ATM and smile fit with good parameter stability; Heston offers analytical dynamics for path-dependent exotics; local volatility achieves perfect fit by construction but suffers from poor extrapolation. A practical pipeline starts with SABR for speed and stability, validates with Heston for dynamics, uses local vol for exotic pricing, and compares Greeks across models for robustness.

!!! note "Role in the Book"
    Calibration connects the theoretical models developed in earlier chapters---local volatility (Chapter 8), stochastic volatility (Chapter 9), and the implied volatility surface (Chapter 7)---to market data. The inverse-problem framework, regularization techniques, and filtering methods developed here underpin all practical applications of option pricing models. The optimization algorithms apply directly to Heston calibration (Chapter 16), while the dynamic calibration and model risk analysis extend to interest rate model fitting (Chapter 18) and the HJM framework (Chapter 19). The SVI/SSVI parameterization provides the arbitrage-free surface construction needed for both local volatility extraction and stochastic volatility calibration.
