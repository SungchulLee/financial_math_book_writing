# Chapter 10: Greeks and Asymptotics

This chapter develops the theory of option price sensitivities (Greeks) from three complementary perspectives--direct differentiation of the Black-Scholes formula, PDE-based sensitivity analysis, and probabilistic expectation representations--then examines how prices and Greeks behave in asymptotic regimes of short maturity, small volatility, extreme strikes, and large time. The interplay between these viewpoints provides both closed-form computation tools and deep structural insight into how option values respond to changes in market variables and model parameters, forming the analytical backbone of risk measurement and hedging.

## Key Concepts

### **Greeks: Definitions, Closed-Form Expressions, and the Pricing Operator**
The pricing map $\mathcal{P}\Phi(t,S) = \mathbb{E}^{t,S}[e^{-r(T-t)}\Phi(S_T)]$ sends payoffs to price surfaces, and Greeks are partial derivatives of this operator with respect to state variables ($S$, $t$) and model parameters ($\sigma$, $r$). This separation matters because state derivatives reflect the geometry of $V$ as a function of $S$, while parameter derivatives reflect sensitivity of the law of $S_T$ to parameter changes. PDE, probabilistic, and measure-theoretic approaches yield complementary Greek formulas. The five fundamental Greeks--Delta $\Delta = \partial V/\partial S$, Gamma $\Gamma = \partial^2 V/\partial S^2$, Vega $\nu = \partial V/\partial \sigma$, Theta $\Theta = \partial V/\partial t$, and Rho $\rho = \partial V/\partial r$--quantify first- and second-order sensitivities, and a second-order Taylor expansion gives the risk decomposition $V(t,S+\delta S;\sigma+\delta\sigma,r+\delta r) \approx V + \Delta\,\delta S + \nu\,\delta\sigma + \rho\,\delta r + \frac{1}{2}\Gamma(\delta S)^2$. In the Black-Scholes model with $d_1 = \frac{\ln(S/K)+(r+\frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$ and $d_2 = d_1 - \sigma\sqrt{\tau}$, these reduce to explicit closed forms derived using the key identity $SN'(d_1) = Ke^{-r\tau}N'(d_2)$:

$$\Delta_{\text{call}} = N(d_1),\quad \Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}},\quad \nu = S\sqrt{\tau}\,N'(d_1),\quad \Theta_{\text{call}} = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2),\quad \rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)$$

Higher-order cross-Greeks--Charm $\partial\Delta/\partial\tau$, Vanna $\partial\Delta/\partial\sigma = \partial\nu/\partial S = -N'(d_1)d_2/\sigma$, and Volga $\partial^2 V/\partial\sigma^2 = \nu \cdot d_1 d_2/\sigma$--capture second-order interactions essential for smile dynamics and volatility surface risk management.

### **Greeks, Martingale Representation, and the Infinitesimal Generator**
In complete diffusion models, the discounted option price $\widetilde{V}_t = e^{-rt}V(t,S_t)$ is a $\mathbb{Q}$-martingale, and by the martingale representation theorem every square-integrable martingale admits

$$\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s\,\mathrm{d}W_s$$

Ito's formula and the PDE cancellation of drift identify the integrand as $Z_t = e^{-rt}\sigma S_t\,\Delta(t,S_t)$, providing the rigorous foundation for "delta is the hedge ratio" in complete markets. In Markov models, the infinitesimal generator $(\mathcal{L}f)(S) = rSf'(S) + \frac{1}{2}\sigma^2 S^2 f''(S)$ determines the pricing PDE $\partial_t V + \mathcal{L}V - rV = 0$, and parameter Greeks can be viewed as sensitivities of $\mathcal{L}$ itself: for instance, differentiating the generator with respect to $\sigma$ yields the source term $-\sigma S^2 V_{SS}$ in the vega PDE. This generator framework generalizes naturally to multi-factor models.

### **PDE Perspective on Greeks**
Differentiating the Black-Scholes PDE $\partial_t V + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$ with respect to state variables and parameters yields sensitivity PDEs that the Greeks themselves satisfy. Delta satisfies a modified PDE with an extra drift term:

$$\frac{\partial\Delta}{\partial t} + \frac{1}{2}\sigma^2 S^2 \Delta_{SS} + (r+\sigma^2)S\,\Delta_S + \sigma^2\Delta - r\Delta = 0$$

with terminal condition $\Delta(T,S) = \Phi'(S)$. Gamma satisfies its own PDE with $\Gamma(T,S) = \Phi''(S) = \delta(S-K)$ for vanilla calls. Vega and rho solve inhomogeneous parabolic PDEs with zero terminal data--for rho, $\partial_t\rho + \frac{1}{2}\sigma^2 S^2\rho_{SS} + rS\rho_S - r\rho = V - SV_S$. The theta identity $\Theta = -\frac{1}{2}\sigma^2 S^2\Gamma - rS\Delta + rV$ expresses theta algebraically from the other Greeks. These PDEs underpin boundary behavior analysis, maximum principle arguments, regularity theory, and stable finite-difference numerical schemes.

### **Smoothness, Regularity, and Boundary Behavior**
Parabolic regularity theory guarantees $V \in C^\infty((0,T)\times(0,\infty))$ even when the payoff has kinks, via Schauder estimates $\|V\|_{C^{2+\alpha,1+\alpha/2}(K)} \leq C_K\|\Phi\|_{L^\infty}$ and the smoothing property of the Gaussian heat kernel. For vanilla calls, the payoff kink $\Phi''(S) = \delta(S-K)$ regularizes into a gamma bump of height $\mathcal{O}(\tau^{-1/2})$, width $\mathcal{O}(\sqrt{\tau})$, and unit area. The Black-Scholes operator degenerates at $S=0$, requiring log-coordinates $x = \ln S$ where it becomes uniformly elliptic: $\widetilde{\mathcal{L}} = \frac{1}{2}\sigma^2\partial_{xx} + (r-\frac{1}{2}\sigma^2)\partial_x$. Far-field behavior guides numerical boundary conditions: as $S\to\infty$, $\Delta\to 1$ and $\Gamma\to 0$ with faster-than-polynomial decay; as $S\to 0$, all Greeks vanish. For OTM calls near expiry, delta decays exponentially as $\exp(-(\ln(K/S))^2/(2\sigma^2\tau))$. American options introduce free boundaries where delta remains continuous (smooth pasting) but gamma may have jump discontinuities related to the local time of $S$ at the exercise boundary.

### **Probabilistic Computation of Greeks: Pathwise, Feynman-Kac, and Likelihood Ratio Methods**
Three probabilistic approaches provide expectation representations for Greeks, each with distinct advantages. Pathwise differentiation exploits the stochastic flow $\partial S_T/\partial S = S_T/S$ (from the log-linearity of geometric Brownian motion) to write

$$\Delta = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right], \qquad \nu = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)S_T(\sqrt{\tau}\,Z - \sigma\tau)\right]$$

with analogous formulas for rho; this requires at least Lipschitz payoff regularity and provides low-variance Monte Carlo estimators. The interchange of differentiation and expectation is justified by dominated convergence. For general diffusions $dS_t = \mu(t,S_t)dt + \sigma(t,S_t)dW_t$, the Jacobian $Y_t = \partial S_t/\partial S_0$ satisfies the variational equation $dY_t = \mu'Y_t dt + \sigma'Y_t dW_t$.

The Feynman-Kac theorem connects the pricing expectation $V(t,S) = \mathbb{E}^{t,S}[e^{-r\tau}\Phi(S_T)]$ to the Black-Scholes PDE, and pathwise differentiation through this representation yields the same Greek formulas. For gamma, however, the pathwise approach breaks down when $\Phi''$ is distributional (e.g., $\delta(S-K)$ for vanilla calls), requiring alternative approaches: smoothing, finite differences, or likelihood ratio methods.

The likelihood ratio (score function) method moves derivatives from the payoff to the density via $V'(\theta) = \mathbb{E}[\Phi(X)\,\partial_\theta\log p_\theta(X)]$, yielding explicit formulas that handle non-smooth payoffs:

$$\Delta = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T)\cdot\frac{Z}{S\sigma\sqrt{\tau}}\right], \qquad \Gamma = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T)\cdot\frac{Z^2 - Z\sigma\sqrt{\tau} - 1}{S^2\sigma^2\tau}\right]$$

The cost is potentially higher variance, especially for short maturities where weights involve $Z/\sqrt{\tau}$. Malliavin calculus provides the systematic theoretical foundation, with weights expressed through Hermite polynomials (e.g., $H_2(z)=z^2-1$ in the gamma weight) and the Skorokhod integral as adjoint of the Malliavin derivative. Practical implementations combine pathwise methods away from kinks with LR methods near kinks, and use control variates, antithetic sampling, and truncation for variance reduction.

Sensitivities can also be expressed as conditional expectations, clarifying the hedging interpretation: delta as the predictable coefficient multiplying the tradable Brownian risk factor. In incomplete markets (stochastic volatility), the martingale representation decomposes into hedgeable and unhedgeable components $Z^{(1)}$ and $Z^{(2)}$, with only the tradable-asset component corresponding to a realizable delta hedge while vega exposure requires trading other options.

### **Short-Maturity Asymptotics**
As $\tau = T - t \to 0$, diffusive increments scale as $\mathcal{O}(\sqrt{\tau})$ and prices concentrate near the current state. The ATM call price satisfies

$$C_{\text{ATM}} = \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}} + \mathcal{O}(\tau)$$

while OTM prices decay exponentially as $C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|x|}\exp(-x^2/(2\sigma^2\tau))$ with $x = \ln(K/S)$, where the rate function $I(S,K) = (\ln(K/S))^2/(2\sigma^2)$ is the squared geodesic distance in the log-moneyness metric, connecting to heat kernel small-time expansions. ITM calls converge to their intrinsic value plus carry with exponentially small time value. Near-ATM expansion gives $C \approx S\sigma\sqrt{\tau/(2\pi)} + xS/2 + \mathcal{O}(\tau)$ for $|x| = \mathcal{O}(\sqrt{\tau})$, depending only on $\sigma$ and $\tau$ at leading order. Short-maturity implied volatility converges to local volatility: $\Sigma(K,\tau) \to \sigma_{\text{local}}(S)$ as $\tau\to 0$.

### **Small-Volatility Asymptotics**
As $\sigma\to 0$, randomness vanishes and $S_T \to Se^{r\tau}$. OTM option prices shrink exponentially in $1/\sigma^2$ with rate function $c = (\ln(K/S) - r\tau)^2/\tau$, representing the squared geodesic distance from the deterministic trajectory. This connects to Varadhan's lemma in large deviations theory: $-\sigma^2\log\mathbb{P}(S_T \in A) \to \inf_{s\in A} I(s)$ where $I(s) = \frac{1}{2\tau}(\ln(s/S)-r\tau)^2$. ATM forward prices are linear in $\sigma$ at leading order, $C_{\text{ATM}} \approx S\sigma\sqrt{\tau}/\sqrt{2\pi}$. Delta becomes a step function around $Ke^{-r\tau}$, while gamma diverges as $1/(S\sigma\sqrt{2\pi\tau})$ for ATM options. The Laplace principle and heat kernel expansion $p(x,y;t) \sim (2\pi t)^{-1/2}\exp(-(y-x)^2/(2t))\sum_{n=0}^\infty a_n t^n$ provide the mathematical framework.

### **Large-Strike and Small-Strike Asymptotics**
Extreme strikes probe the tail behavior of the risk-neutral distribution. For large $K$ (OTM calls), Black-Scholes prices have Gaussian tail decay:

$$C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(K/S)|}\exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right)$$

with an analogous formula for small-$K$ (OTM puts). Roger Lee's moment formula relates the implied volatility wing slopes $\beta_R = \limsup_{k\to+\infty}\Sigma(k)^2\tau/k$ and $\beta_L$ to the existence of moments of $S_T$: if $\mathbb{E}[S_T^{1+\alpha}]<\infty$, then $\beta_R \leq 2 - 4(\sqrt{\alpha^2+\alpha}-\alpha)$. For Black-Scholes (all moments finite), $\beta_R = \beta_L = 0$. All Greeks--delta, gamma, vega--vanish exponentially for far OTM options. Market option prices often imply fatter tails than log-normal, pointing to jump and stochastic volatility models.

### **Large-Time Behavior and Ergodicity**
Black-Scholes is non-ergodic in $S$: as $T\to\infty$, $\log S_T$ has variance $\sigma^2 T\to\infty$, the call price $C\to S_0$, $\Delta\to 1$, $\Gamma\to 0$, and the option degenerates toward the underlying. In multi-factor models, mean-reverting factors such as CIR-type variance $dv_t = \kappa(\bar{v}-v_t)dt + \xi\sqrt{v_t}dW_t$ are ergodic when the Feller condition $2\kappa\bar{v}>\xi^2$ holds, with invariant Gamma distribution. The time-averaged variance converges to $\bar{v}$, so long-dated options are approximately priced by Black-Scholes with $\sigma = \sqrt{\bar{v}}$, and implied volatility satisfies $\sigma_{\text{implied}}(T) \to \sqrt{\bar{v}} + \mathcal{O}(T^{-1})$, with convergence rate governed by the mean-reversion speed $\kappa$.

### **Scaling Laws for Greeks**
Near-the-money ATM options exhibit universal scaling in $\tau$: $\Gamma \sim \tau^{-1/2}$, $\Theta \sim -\tau^{-1/2}$, $\nu \sim \tau^{1/2}$, $\rho \sim \tau$, while delta remains $\mathcal{O}(1)$. Dimensional analysis from $V_{\text{ATM}} \sim S\sigma\sqrt{\tau}$ confirms all scalings. The fundamental theta-gamma identity

$$\Theta + \frac{1}{2}\sigma^2 S^2\Gamma = rV - rS\Delta$$

shows that convexity benefit (positive gamma) is paid for through time decay (negative theta)--two sides of the same coin. For moderate maturities ($\tau \sim 1$ year), vega dominates portfolio risk; for long maturities, $\Delta\to 1$ and $\Gamma\to 0$ as $\tau^{-1/2}$. OTM Greeks decay exponentially with rate $\exp(-x^2/(2\sigma^2\tau))$, where the characteristic scale separating ATM from OTM is $|x| \sim \sigma\sqrt{\tau}$.

### **Gamma Blow-Up and Delta Step-Function Behavior Near Expiry**
As $\tau\to 0$, gamma concentrates near the strike with $\Gamma_{\text{ATM}} = 1/(S\sigma\sqrt{2\pi\tau}) \sim \tau^{-1/2}$, while the peak localizes in a band of width $\mathcal{O}(\sigma\sqrt{\tau})$ in log-moneyness with unit area--a Gaussian approximation to the Dirac delta $\delta(S-K)$. Theta exhibits matching blow-up: $\Theta_{\text{ATM}} = -S\sigma/(2\sqrt{2\pi\tau}) \sim -\tau^{-1/2}$. Simultaneously, delta approaches a step function $\mathbf{1}_{S>K}$, with the transition layer width $\Delta S \approx 2K\sigma\sqrt{\tau}$. The inner-layer scaling $z = \ln(S/K)/(\sigma\sqrt{\tau})$ provides the universal asymptotic description: $\Delta \approx N(z) + \mathcal{O}(\sqrt{\tau})$. These effects create pin risk, delta instability, and expensive rebalancing--the expected squared hedging error scales as $\Gamma^2 S^4\sigma^2\Delta t \sim S^2\sigma\Delta t/\tau$, growing as $\tau\to 0$.

### **Vega Asymptotics and Smile Sensitivity**
ATM vega scales as $\nu_{\text{ATM}} \approx S\sqrt{\tau}/\sqrt{2\pi} \sim \sqrt{\tau}$ and vanishes at expiry, while OTM vega decays exponentially as $S\sqrt{\tau}\exp(-x^2/(2\sigma^2\tau))$. In Black-Scholes, the identity $\nu = \sigma S^2\tau\,\Gamma$ links vega and gamma risk, meaning hedging one automatically hedges the other--a proportionality that breaks in stochastic volatility models. The second-order sensitivity Volga $= \nu\cdot d_1 d_2/\sigma$ governs P&L convexity under large volatility moves. In smile models, the scalar vega generalizes to multi-dimensional surface sensitivity: bucket vegas $\nu_{ij} = \partial V/\partial\Sigma_{ij}$ partition the implied volatility surface, term structure vegas aggregate across maturities, and model vegas (sensitivities to Heston parameters $v_0$, $\bar{v}$, $\xi$, etc.) capture distinct aspects of volatility risk.

!!! note "Role in the Book"
    The Greeks computed here using closed-form Black-Scholes expressions (Chapter 6) and Feynman-Kac representations (Chapter 5) serve as benchmarks for later chapters. Implied volatility (Chapter 7) reinterprets vega as surface sensitivity and connects short-maturity asymptotics to local volatility via Dupire's formula. Stochastic volatility models (Chapter 9) break the vega-gamma proportionality and introduce unhedgeable risk components. The PDE structure, boundary behavior, and regularity results developed here underpin numerical methods (Chapter 8) for finite-difference Greeks computation. Roger Lee's moment formula and tail asymptotics connect to the distributional assumptions explored in jump and Levy models, while the large-time ergodicity results inform long-dated product pricing under mean-reverting variance dynamics.

---
