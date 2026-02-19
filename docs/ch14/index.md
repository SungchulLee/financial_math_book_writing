# Chapter 14: Stochastic Volatility

This chapter develops the theory of stochastic volatility models, in which the diffusion coefficient is itself a random process driven by its own source of uncertainty. Starting from the empirical failures of constant and local volatility—volatility clustering, mean reversion, the leverage effect—we build the general two-factor diffusion framework, study the Heston and SABR models in detail, analyze the fundamental consequences of market incompleteness for pricing and hedging, and develop calibration methods that jointly fit the implied volatility surface across strikes and maturities.

## Key Concepts

**Empirical Motivation**
Constant-volatility models fail to explain three robust empirical facts: (1) **volatility clustering**—periods of high and low volatility persist, with autocorrelation in $|\Delta \ln S|$ decaying slowly; (2) **mean reversion**—volatility fluctuates around a long-run level, returning from extremes over months; (3) the **leverage effect**—negative correlation between returns and volatility changes, with equity vol rising after price drops. The implied volatility smile and skew (Chapter 12) are market manifestations of these dynamics. Local volatility (Chapter 13) reproduces today's smile but generates incorrect forward smile dynamics because it lacks a separate volatility factor. Stochastic volatility introduces this missing degree of freedom.

**General Two-Factor Framework**
The generic stochastic volatility model specifies

$$dS_t = (r-q)S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}, \qquad dv_t = \alpha(t, v_t)\,dt + \eta(t, v_t)\,dZ_t$$

with $d\langle W^{(1)}, Z \rangle_t = \rho\,dt$ and $|\rho| \leq 1$. The correlation $\rho$ generates the skew: $\rho < 0$ produces the negative equity skew (vol rises when spot falls). The **risk-neutral drift** of $v_t$ includes a market price of volatility risk $\lambda(t, v_t)$ that cannot be determined by no-arbitrage alone—only by calibration to option prices or equilibrium arguments. The pricing PDE becomes two-dimensional:

$$\partial_t V + \frac{1}{2}vS^2\partial_{SS}V + \rho\eta v S\,\partial_{Sv}V + \frac{1}{2}\eta^2\partial_{vv}V + (r-q)S\partial_S V + \alpha^{\mathbb{Q}}\partial_v V - rV = 0$$

where $\alpha^{\mathbb{Q}} = \alpha - \lambda\eta$ is the risk-neutral drift of variance. The extra dimension $v$ reflects market incompleteness: volatility risk cannot be hedged with the underlying alone.

**The Heston Model**
The Heston (1993) model specifies a CIR process for variance:

$$dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$$

with parameters: mean-reversion speed $\kappa$, long-run variance $\theta$, vol-of-vol $\xi$, and correlation $\rho$. The **Feller condition** $2\kappa\theta \geq \xi^2$ ensures $v_t > 0$ almost surely. The model's **affine structure** yields a closed-form characteristic function $\phi(u) = \exp(C(u,\tau) + D(u,\tau)v_0 + iu\ln S_0)$ where $C$ and $D$ satisfy Riccati ODEs, enabling fast pricing via Fourier methods (Chapter 9). The Heston model produces realistic smiles with $\rho$ controlling skew, $\xi$ controlling smile curvature (wings), $\kappa$ and $\theta$ controlling term structure, and $v_0$ setting the ATM level. It is the workhorse stochastic volatility model in practice. (Detailed treatment in Chapter 16.)

**The SABR Model**
The SABR model (Hagan et al., 2002) specifies

$$dF_t = \alpha_t F_t^{\beta}\,dW_t^{(1)}, \qquad d\alpha_t = \nu\alpha_t\,dW_t^{(2)}$$

with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt$, where $F_t$ is the forward price, $\beta \in [0,1]$ controls the **CEV backbone** (the local volatility shape), $\alpha_t$ is the stochastic volatility, and $\nu$ is the vol-of-vol. The model is widely used for interest rate smiles because it naturally operates in forward space and the Hagan approximation provides a closed-form implied volatility formula:

$$\sigma_{\text{imp}}(K) \approx \frac{\alpha}{(FK)^{(1-\beta)/2}}\cdot\frac{z}{x(z)}\cdot\left[1 + \left(\frac{(1-\beta)^2\alpha^2}{24(FK)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK)^{(1-\beta)/2}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]$$

where $z = (\nu/\alpha)(FK)^{(1-\beta)/2}\ln(F/K)$ and $x(z) = \ln((\sqrt{1-2\rho z+z^2}+z-\rho)/(1-\rho))$. Boundary behavior depends on $\beta$: for $\beta < 1$, the forward can reach zero (absorption vs. reflection), requiring careful treatment. **Arbitrage-free SABR** extensions (Hagan et al., 2014) address the density leakage and arbitrage violations in the wings of the Hagan approximation.

**Incompleteness, Pricing, and the Volatility Risk Premium**
Stochastic volatility markets are **incomplete**: the volatility factor $v_t$ introduces risk that cannot be hedged by trading the underlying alone. Consequently, the risk-neutral measure $\mathbb{Q}$ is not unique—it depends on the **market price of volatility risk** $\lambda(t,v_t)$, which must be estimated from option market data. Under the physical measure $\mathbb{P}$, the variance drift is $\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - v_t)$; under $\mathbb{Q}$, it becomes $\kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - v_t)$ with $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda$ and $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$. The **volatility risk premium** $\lambda$ is typically negative for equity markets (investors pay a premium for protection against vol spikes), explaining why implied volatility systematically exceeds realized volatility and why selling variance swaps is profitable on average.

**Hedging Under Stochastic Volatility**
Delta hedging with the Black-Scholes delta leaves residual **vega risk** proportional to the vol-of-vol and the option's vega. The minimum-variance hedge modifies the delta to $\Delta_{\text{MV}} = \Delta_{\text{BS}} + \rho\xi\sqrt{v_t}\,\partial_v V / (S\sqrt{v_t})$, incorporating the correlation-mediated exposure to volatility moves. Full hedging of vega risk requires trading a second option or a variance swap, solving the two-instrument system for delta-vega neutrality. In the SABR model, the smile-adjusted delta $\Delta_{\text{SABR}} = \Delta_{\text{BS}} + \nu_{\text{BS}}\,\partial\sigma_{\text{imp}}/\partial F$ automatically incorporates the sticky-delta smile dynamics.

**Calibration**
Stochastic volatility models are calibrated by minimizing the distance between model and market implied volatilities across the $(K,T)$ surface:

$$\min_{\Theta} \sum_{i,j} w_{ij}\left(\sigma_{\text{imp}}^{\text{model}}(K_i, T_j; \Theta) - \sigma_{\text{imp}}^{\text{market}}(K_i, T_j)\right)^2$$

**Identifiability** challenges arise because different parameter combinations can produce similar surfaces—$\kappa$ and $\theta$ are partially degenerate for short maturities, and $\rho$ and $\xi$ interact in the skew-curvature decomposition. Joint calibration across multiple maturities breaks some degeneracies. **Parameter stability**—smooth day-to-day evolution—is often more important in practice than achieving the tightest fit, as unstable parameters produce erratic hedging behavior.

!!! note "Role in the Book"
    Stochastic volatility models address the key limitations of local volatility (Chapter 13) and constant volatility (Chapter 6) by introducing a separate variance factor. The Heston model's affine structure connects to Chapter 15 (affine processes) and is developed in full detail in Chapter 16. The SABR model provides the standard framework for interest rate smile modeling (Chapters 18-19). Calibration methods connect to Chapter 17, and the incompleteness framework motivates the hedging strategies of Chapter 11.

---
