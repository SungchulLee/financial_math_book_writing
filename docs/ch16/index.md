# Chapter 16: The Heston Model in Detail


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

This chapter provides a comprehensive, self-contained treatment of the Heston stochastic volatility model---from its mathematical foundations through pricing, hedging, calibration, and numerical implementation. Starting from the bivariate SDE system and its affine structure, we derive the closed-form characteristic function, develop multiple pricing engines (Fourier inversion, COS, FFT, Monte Carlo, finite differences), compute Greeks analytically and numerically, calibrate to the implied volatility surface, price exotic derivatives, and study the model's extensions including jumps (Bates), multiple factors (double Heston), and rough volatility. Throughout, we address the measure-theoretic foundations---risk-neutral pricing, the stock-price numeraire, the volatility risk premium, and the minimal entropy martingale measure---that underpin all Heston model applications.

## Key Concepts

### **Model Definition and Affine Structure**
The Heston (1993) model specifies the risk-neutral dynamics:

$$dS_t = (r-q)S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}, \qquad dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$$

with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt$. The five parameters are: initial variance $v_0$, mean-reversion speed $\kappa > 0$, long-run variance $\theta > 0$, vol-of-vol $\xi > 0$, and correlation $\rho \in [-1,1]$. The model belongs to the **affine class**: the log-price characteristic function $\phi(u,\tau) = \mathbb{E}[e^{iu\ln S_T} \mid S_t, v_t]$ has the exponential-affine form $\phi(u,\tau) = \exp(C(\tau,u) + D(\tau,u)v_t + iu\ln S_t)$, where $C$ and $D$ satisfy **Riccati ODEs** $D' = \frac{1}{2}\xi^2 D^2 + (\rho\xi iu - \kappa)D + \frac{1}{2}(iu - u^2)$ and $C' = \kappa\theta D$. This affine structure connects the Heston model to the general stochastic volatility framework and enables semi-analytical pricing. **Moment explosions** occur when $\mathbb{E}[S_T^p] = \infty$ for $p > p^*$, where $p^*$ depends on $\kappa, \theta, \xi, \rho$ and determines the domain of the characteristic function---critical for the integrability conditions of Fourier pricing.

### **Variance Dynamics and CIR Process**
The variance process $v_t$ follows a **CIR (Cox-Ingersoll-Ross) process** with explicit solution via the non-central chi-squared transition density $v_T \sim \frac{\xi^2(1-e^{-\kappa\tau})}{4\kappa}\chi^2_d(\lambda)$ where $d = 4\kappa\theta/\xi^2$ degrees of freedom and non-centrality parameter $\lambda = 4\kappa e^{-\kappa\tau}v_t/(\xi^2(1-e^{-\kappa\tau}))$. The **Feller condition** $2\kappa\theta \geq \xi^2$ ensures strict positivity of $v_t$; when violated, $v_t$ can touch zero but is immediately reflected. Conditional moments are: $\mathbb{E}[v_T \mid v_t] = \theta + (v_t - \theta)e^{-\kappa\tau}$ and $\text{Var}[v_T \mid v_t] = v_t\xi^2 e^{-\kappa\tau}(1-e^{-\kappa\tau})/\kappa + \theta\xi^2(1-e^{-\kappa\tau})^2/(2\kappa)$. The **mean-reversion** mechanism pulls $v_t$ toward $\theta$ with half-life $\ln 2/\kappa$, while the **long-run variance** $\theta$ determines the stationary level. The correlation $\rho$ generates the **leverage effect**: $\rho < 0$ makes large downward moves in $S$ coincide with variance increases, producing the negative equity skew observed in markets.

### **Characteristic Function and Numerical Stability**
The closed-form solutions for the Riccati system involve $\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}$ and the **Albrecher formulation** (preferred for numerical stability):

$$D(\tau,u) = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2}\cdot\frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}}, \qquad g = \frac{\kappa - i\rho\xi u - \gamma}{\kappa - i\rho\xi u + \gamma}$$

The original **Heston (1993) formulation** suffers from branch-cut discontinuities in the complex square root $\gamma$ and the logarithm in $C(\tau,u) = \kappa\theta[\tau(\kappa - i\rho\xi u - \gamma)/\xi^2 - 2\ln((1-ge^{-\gamma\tau})/(1-g))/\xi^2]$. The Albrecher formulation resolves this by choosing the branch such that $|g| < 1$, ensuring the logarithm's argument never crosses the branch cut. The **rotation count method** provides an additional safeguard for continuity across the complex plane. Log-stock price **moments** $\mathbb{E}[(\ln S_T)^n]$ are obtained by differentiating $\phi$ at $u=0$: $\mathbb{E}[\ln S_T] = -i\phi'(0)$, $\text{Var}[\ln S_T] = -\phi''(0) + (\phi'(0))^2$, providing skewness and kurtosis diagnostics for the model.

### **Measure Change and Risk-Neutral Pricing**
The Heston model operates under the **risk-neutral measure** $\mathbb{Q}$, obtained from the physical measure $\mathbb{P}$ via Girsanov's theorem with a two-dimensional market price of risk. The **stock-price numeraire** measure $\mathbb{Q}^S$ (with numeraire $S_t$) transforms the characteristic function and simplifies the computation of $P_1$ in the Gil-Pelaez decomposition. The **volatility risk premium**---the difference between physical and risk-neutral variance dynamics---manifests as a shift in the mean-reversion level: $\kappa^{\mathbb{Q}} = \kappa + \lambda_v$ and $\theta^{\mathbb{Q}} = \kappa\theta/(\kappa + \lambda_v)$ where $\lambda_v$ is the variance risk premium. The **minimal entropy martingale measure** selects the equivalent martingale measure closest (in relative entropy) to the physical measure, providing a principled pricing rule in the incomplete Heston market where variance risk cannot be perfectly hedged.

### **European Pricing: Fourier Methods**
Three complementary Fourier approaches price European options:

- **Gil-Pelaez inversion**: $C = S_0 P_1 - Ke^{-rT}P_2$ where $P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}[e^{-iu\ln K}\phi_j(u)/({iu})]\,du$ with $\phi_1$ and $\phi_2$ the characteristic functions under the stock-numeraire and money-market-numeraire measures respectively. This **semi-closed-form** representation reduces option pricing to a single numerical integration.
- **COS method**: The Fourier cosine expansion $V \approx e^{-r\tau}\frac{b-a}{2}\sum_{k=0}^{N-1}{}' A_k H_k$ achieves **exponential convergence** with $N \sim 64$--$128$ terms, using density coefficients $A_k = \frac{2}{b-a}\text{Re}[\varphi(\frac{k\pi}{b-a})e^{-ik\pi a/(b-a)}]$ and closed-form payoff coefficients $H_k$ involving the chi and psi auxiliary functions. The COS method also prices **digital and cash-or-nothing options** via modified payoff coefficients, and serves as a platform for **convergence and accuracy benchmarks** against Monte Carlo and FDM.
- **Carr-Madan FFT**: produces option prices across a grid of $N$ strikes in $\mathcal{O}(N\log N)$ operations via density recovery $f(x) = \frac{1}{\pi}\text{Re}(\int_0^{\infty}e^{-iux}\varphi(u)\,du)$ with grid constraint $\Delta_u \cdot \Delta_x = 2\pi/N$, optimal for calibration sweeps across the entire implied volatility surface.

### **Greeks**
Greeks are computed via three methods: (1) **finite differences on the characteristic function**---bumping parameters in $\phi$ and re-inverting; (2) **analytic differentiation** of $\phi$ with respect to $S_0$ (delta), $v_0$ (variance sensitivity), $\sigma$ (vega); (3) **COS method Greeks** obtained by differentiating the cosine series term-by-term, producing delta, gamma, vega, and higher-order sensitivities with the same exponential convergence as the price. The **vega surface** $\partial V/\partial v_0$ and vol-of-vol sensitivity $\partial V/\partial\xi$ are particularly important: unlike Black-Scholes where $\nu = \sigma S^2\tau\Gamma$, in Heston vega and gamma are decoupled, with vega depending on the variance mean-reversion timescale. **P&L explanation** under Heston decomposes into delta P&L, gamma P&L, theta, and a new **vega P&L** from variance moves: $dV \approx \Delta\,dS + \frac{1}{2}\Gamma(dS)^2 + \Theta\,dt + \mathcal{V}\,dv$, providing a richer attribution than Black-Scholes.

### **Monte Carlo Simulation**
Simulating the Heston SDE requires special schemes due to the square-root variance process:

- **Euler discretization** with full truncation $v_{t+\Delta t} = |v_t + \kappa(\theta - v_t)\Delta t + \xi\sqrt{v_t^+}\sqrt{\Delta t}\,Z|$ is simple but biased, with $\mathcal{O}(\sqrt{\Delta t})$ weak convergence. Pitfalls include negative variance, which requires truncation or reflection schemes.
- **Milstein scheme**: adds the correction term $\frac{1}{4}\xi^2(\Delta t)(Z^2 - 1)$ to the variance discretization, improving weak convergence to $\mathcal{O}(\Delta t)$ but still requiring care with the square-root diffusion.
- **Exact simulation** (Broadie-Kaya, 2006) samples the integrated variance $\int_t^{t+\Delta t}v_s\,ds$ exactly using its non-central chi-squared distribution, eliminating discretization bias but requiring expensive inverse CDF computation.
- **Quadratic-exponential scheme** (Andersen, 2008) matches the first two moments of $v_{t+\Delta t}$ exactly using a mixture of a point mass and an exponential, achieving near-exact accuracy with minimal computational overhead---the standard choice in practice.
- **Variance reduction**: antithetic variates (exploiting the symmetry of $Z$), control variates (using the geometric average or Black-Scholes price), and importance sampling improve efficiency by factors of 10--100x depending on the payoff structure.

### **Finite Difference Methods**
The two-dimensional Heston PDE is formulated on a $(S, v)$ grid and solved using **ADI (alternating direction implicit)** schemes---Douglas, Craig-Sneyd, or Hundsdorfer-Verwer---that split the 2D implicit problem into sequences of tridiagonal 1D solves. **Boundary conditions** require care: at $v = 0$ the PDE degenerates (the $v$-diffusion vanishes), requiring the Feller boundary condition or extrapolation; at $v = v_{\max}$ asymptotic conditions are applied; at $S = 0$ and $S = S_{\max}$ standard Dirichlet or Neumann conditions are used. Non-uniform grids concentrate points near $(S, v) = (K, v_0)$ for accuracy. **American options** are handled via **PSOR (projected successive over-relaxation)** within the ADI framework, combining the early exercise constraint projection with each directional sweep.

### **Calibration**
The calibration problem minimizes $\sum_{i,j}w_{ij}(\sigma_{\text{imp}}^{\text{Heston}}(K_i,T_j;\Theta) - \sigma_{\text{imp}}^{\text{mkt}}(K_i,T_j))^2$ over $\Theta = (v_0, \kappa, \theta, \xi, \rho)$. The **objective function design** balances price-space versus implied-vol-space formulations, with the latter providing more uniform scaling across strikes and maturities. The objective is non-convex with multiple local minima, requiring global optimization: **differential evolution** or particle swarm for initial exploration, followed by Levenberg-Marquardt or BFGS for local refinement. The Jacobian of implied volatilities with respect to parameters is computed via the chain rule through the Fourier inversion. **Joint calibration across maturities** is essential: short maturities pin down $v_0$ and $\rho$, while long maturities identify $\kappa\theta$ and the mean-reversion timescale $1/\kappa$. **Calibration to the implied volatility surface** proceeds on a grid of $(K_i, T_j)$ points after arbitrage filtering and surface construction. **Parameter stability**---requiring smooth day-to-day evolution through regularization penalties $\lambda\|\Theta_t - \Theta_{t-1}\|^2$---is critical for hedging consistency. **Identifiability**: $\kappa$ and $\theta$ are partially degenerate (only $\kappa\theta$ is well-identified from short-maturity data), and $\xi$ and $\rho$ interact in the skew-curvature decomposition.

### **Exotic Pricing Under Heston**
The affine structure enables semi-analytical pricing for several exotic derivatives:

- **Variance swaps**: $\mathbb{E}^{\mathbb{Q}}[\frac{1}{T}\int_0^T v_t\,dt] = \theta + (v_0 - \theta)(1 - e^{-\kappa T})/(\kappa T)$ in closed form
- **Forward-start options**: the characteristic function of $\ln(S_T/S_{T_1})$ for $T_1 < T$ retains affine form, enabling COS pricing---a key advantage over local volatility
- **Barrier options**: semi-analytical via Fourier-space methods (Green's function of the killed process) or Monte Carlo with continuity corrections
- **VIX options**: since VIX$^2 \approx \mathbb{E}^{\mathbb{Q}}[\frac{1}{\tau}\int_t^{t+\tau}v_s\,ds \mid \mathcal{F}_t]$ is affine in $v_t$, VIX$^2$ options can be priced via the affine transform
- **Asian options**: priced via Monte Carlo simulation with the QE scheme, using control variates based on the geometric average for variance reduction

### **Extensions**

- **Bates model** (1996): adds Merton-type jumps $J\,dN_t$ to the stock price, producing short-maturity smile steepening that pure Heston cannot generate; the characteristic function adds a Poisson-lognormal jump contribution to the Riccati system
- **Double Heston**: two independent CIR variance factors $v_t^{(1)}, v_t^{(2)}$ with different correlations and mean-reversion speeds, providing richer term structure of skew and better calibration to both short- and long-dated options simultaneously
- **Time-dependent parameters**: $\kappa(t), \theta(t)$ enable exact calibration to the term structure of ATM volatility, at the cost of losing time-homogeneous analytical simplicity
- **Rough Heston**: replaces the CIR variance process with a fractional kernel $v_t = v_0 + \int_0^t K_H(t-s)\kappa(\theta - v_s)\,ds + \int_0^t K_H(t-s)\xi\sqrt{v_s}\,dW_s$ with $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$ and $H \approx 0.1$, capturing the rough volatility signature observed in high-frequency data; the characteristic function satisfies a fractional Riccati equation

!!! note "Role in the Book"
    The Heston model is the central stochastic volatility model of the book, integrating the affine process theory (Chapter 15), Fourier pricing methods (Chapter 9), and calibration framework (Chapter 17). Its characteristic function is the prototype for all affine model pricing. The Monte Carlo and FDM implementations extend the numerical methods of Chapter 8 to two dimensions. The measure-change analysis connects to the general incomplete-market theory and the volatility risk premium literature. The model's limitations---inability to fit very short-maturity smiles and the ATM term structure simultaneously---motivate the extensions (Bates, rough Heston) and the local-stochastic volatility hybrids discussed in later chapters.

---
