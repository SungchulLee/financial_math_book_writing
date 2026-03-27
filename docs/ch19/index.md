# Chapter 19: Interest Rate Derivatives and HJM

This chapter develops the modern framework for pricing and hedging interest rate derivatives. Starting from the Heath--Jarrow--Morton approach to forward rate dynamics, we build the theory of forward measures and numeraire techniques, then construct the LIBOR Market Model for direct modeling of observable rates. The chapter covers bond options, caps, floors, swaptions, convexity adjustments, calibration pipelines, and the model risk challenges of multi-curve environments and negative rates.

## Key Concepts

### The Heath--Jarrow--Morton Framework

Short-rate models specify a single stochastic process and derive the entire yield curve as output. The HJM framework reverses this logic: it takes the forward rate curve as the fundamental state variable and shows that no-arbitrage imposes a powerful constraint linking drift to volatility.

The HJM framework models the entire instantaneous forward rate curve $f(t,T)$ directly via $df(t,T) = \alpha(t,T)\,dt + \sum_{i=1}^{n} \sigma_i(t,T)\,dW_t^i$ where $f(t,T) = -\partial_T \ln P(t,T)$ and $P(t,T) = \exp(-\int_t^T f(t,u)\,du)$. The central result is the **no-arbitrage drift condition**: requiring discounted bond prices to be $\mathbb{Q}$-martingales uniquely determines the drift from the volatility structure,

$$
\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du = \sigma(t,T)\,\Sigma(t,T)
$$

where $\Sigma(t,T) = \int_t^T \sigma(t,u)\,du$ is the bond price volatility. The proof proceeds by writing bond dynamics $dP(t,T)/P(t,T) = [\cdots]\,dt - \Sigma(t,T)\,dW_t$ and imposing the $\mathbb{Q}$-martingale condition on $P(t,T)/B_t$. Under $\mathbb{Q}$, bond prices satisfy $dP(t,T)/P(t,T) = r_t\,dt - \Sigma(t,T)\,dW_t$.

Short-rate models are special cases of HJM with specific volatility structures: the Vasicek model corresponds to exponentially decaying $\sigma_f(t,T)$, Ho--Lee to constant $\sigma_f$, and CIR to $\sigma_f(t,T) \propto \sqrt{r_t}\,e^{-\kappa(T-t)}$. The framework is intrinsically **infinite-dimensional**---the state at time $t$ is the entire curve $T \mapsto f(t,T)$---but practical implementations use finite-factor approximations, separable volatility structures $\sigma(t,T) = \phi(t)\psi(T-t)$, and maturity discretization.

### Forward Measures and Numeraire Techniques

The key to tractable interest rate derivative pricing is choosing the right numeraire. Each choice of numeraire defines a probability measure under which the relevant forward rate becomes driftless, dramatically simplifying expectation calculations.

A **numeraire** is any strictly positive tradable asset $N_t$; the generalized pricing formula $V_t = N_t\,\mathbb{E}^{\mathbb{Q}^N}[V_T/N_T \mid \mathcal{F}_t]$ holds under the associated measure $\mathbb{Q}^N$ where $S_t/N_t$ is a martingale. The **risk-neutral measure** $\mathbb{Q}$ uses the money-market account $B_t = \exp(\int_0^t r_s\,ds)$, giving $V_t = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}V_T \mid \mathcal{F}_t]$.

The **$T$-forward measure** $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numeraire, so $V_t = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}[V_T \mid \mathcal{F}_t]$---eliminating the stochastic discount factor and making the forward price a martingale. The Girsanov transformation $dW^T(t) = dW^{\mathbb{Q}}(t) + \Sigma(t,T)\,dt$ connects the measures. Under the $T$-forward measure, the forward LIBOR rate $L(t;T,T+\delta)$ is a martingale under $\mathbb{Q}^{T+\delta}$, and the forward bond price $P(t,S)/P(t,T)$ is a martingale under $\mathbb{Q}^T$ for $S > T$.

The **swap measure** $\mathbb{Q}^A$ uses the annuity factor $A(t) = \sum_{i}\delta_i P(t,T_i)$ as numeraire, under which the forward swap rate $S(t) = (P(t,T_0) - P(t,T_n))/A(t)$ is a martingale. Choosing the natural numeraire for each derivative simplifies pricing: bond options use the $T$-forward measure, caplets use the $T_{i+1}$-forward measure, and swaptions use the annuity measure.

### The LIBOR Market Model

The HJM framework models instantaneous forward rates, which are not directly observable. The LIBOR Market Model (BGM model) instead specifies dynamics for the discrete forward rates that are actually quoted and traded in interest rate markets.

The Brace--Gatarek--Musiela (BGM) model specifies dynamics for observable forward LIBOR rates $L_i(t) = \frac{1}{\delta_i}(P(t,T_i)/P(t,T_{i+1}) - 1)$ on a tenor structure $0 = T_0 < T_1 < \cdots < T_n$. Under the $T_{i+1}$-forward measure, each rate is a driftless diffusion: $dL_i(t)/L_i(t) = \sigma_i(t)\,dW_i^{T_{i+1}}(t)$ with correlations $dW_i \cdot dW_j = \rho_{ij}\,dt$.

Under the **terminal measure** $\mathbb{Q}^{T_n}$, a drift correction appears:

$$
\frac{dL_i(t)}{L_i(t)} = -\sum_{j=i+1}^{n-1}\frac{\delta_j\rho_{ij}\sigma_i(t)\sigma_j(t)L_j(t)}{1+\delta_j L_j(t)}\,dt + \sigma_i(t)\,dW_i^{T_n}(t)
$$

obtained by telescoping the measure changes from $\mathbb{Q}^{T_{i+1}}$ through to $\mathbb{Q}^{T_n}$. Under the **spot measure** with rolling bank account numeraire, the drift reverses sign.

**Correlation parameterizations**---exponential decay $\rho_{ij} = e^{-\beta|T_i - T_j|}$, two-factor, or angle-based---and **volatility specifications** (time-homogeneous, separable, piecewise constant) determine the model's flexibility.

The log-normal assumption yields **Black's caplet formula** $\text{Caplet}_i = \delta_i P(0,T_{i+1})[L_i(0)N(d_1) - KN(d_2)]$ with $d_{1,2} = (\ln(L_i(0)/K) \pm \frac{1}{2}v_i^2)/v_i$ and integrated variance $v_i^2 = \int_0^{T_i}\sigma_i(t)^2\,dt$. **Swaption pricing** uses the frozen-drift approximation: the swap rate volatility $\sigma_S^2 T_0 \approx \sum_{i,j}w_i w_j L_i L_j \rho_{ij}\int_0^{T_0}\sigma_i\sigma_j\,dt / S_0^2$ (Rebonato's formula), feeding into Black's formula with the annuity as numeraire.

**Monte Carlo simulation** uses log-Euler discretization $\ln L_i(t+\Delta t) = \ln L_i(t) + (\mu_i - \frac{1}{2}\sigma_i^2)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i$ with Cholesky-decomposed correlated normals $Z = Lz$ where $LL^\top = \rho$ and $z \sim N(0,I)$. Extensions include stochastic volatility LMM (SABR-LMM), displaced diffusion, and RFR-based models for the post-LIBOR era.

### Pricing Interest Rate Derivatives

With the theoretical machinery of HJM, forward measures, and the LMM in hand, we can now price the major classes of interest rate derivatives. The common thread is selecting the natural numeraire for each instrument and exploiting the resulting martingale property.

Bond prices satisfy either the **Feynman--Kac** representation $P(t,T) = \mathbb{E}^{\mathbb{Q}}_t[\exp(-\int_t^T r_s\,ds)]$ or the **bond pricing PDE** $\partial_t P + \mu^{\mathbb{Q}}\partial_r P + \frac{1}{2}\sigma^2\partial_{rr}P = rP$ with terminal condition $P(T,T) = 1$. **Yield curve dynamics** describe yields as affine functions of the short rate in affine models, with the Nelson--Siegel form providing a parsimonious parameterization.

**Bond options** in Vasicek/Hull--White models have closed-form prices: $C(0) = P(0,T_B)N(d_1) - KP(0,T)N(d_2)$. The **Jamshidian decomposition** reduces coupon bond options to portfolios of zero-coupon bond options by finding the critical rate $r^*$ solving $\sum c_i P(T,T_i,r^*) = K$.

**Caps and floors** are portfolios of caplets/floorlets, with cap--floor parity $\text{Cap} - \text{Floor} = \text{Payer Swap}$. Black's caplet formula applies under log-normal forward dynamics, and the Bachelier formula $\text{Caplet} = N\delta_i P(0,T_{i+1})[(F-K)N(d) + \sigma^{(n)}\sqrt{T_i}\,\phi(d)]$ handles negative rate environments. **Swaptions** price as $A_0[S_0 N(d_1) - KN(d_2)]$ under the annuity measure.

**Duration** $D_{\text{mod}} = -\frac{1}{P}\frac{dP}{dy}$ and **convexity** $C = \frac{1}{P}\frac{d^2P}{dy^2}$ provide first- and second-order sensitivity measures: $\Delta P/P \approx -D_{\text{mod}}\,\Delta y + \frac{1}{2}C\,(\Delta y)^2$, with DV01 as the standard risk metric. **Key rate duration** $\text{KRD}_k = -\frac{1}{P}\frac{\partial P}{\partial y_k}$ decomposes sensitivity across specific tenor points.

### Convexity Adjustments

When a rate is observed under one probability measure but paid under another, the expectation of the rate differs between the two measures. This mismatch---a convexity adjustment---arises systematically from the Girsanov measure-change machinery.

Key applications include: *LIBOR-in-arrears*, where payment at $T_i$ rather than $T_{i+1}$ requires a forward-rate-dependent correction $\mathbb{E}^{T_i}[L(T_i)] = L(0) + \frac{L(0)^2 \sigma^2 T_i \delta}{1 + \delta L(0)}$ under log-normal dynamics; *timing adjustments* for payment date mismatches; *CMS convexity adjustments* for constant-maturity swap rates, where the swap rate is a martingale under the annuity measure but must be evaluated under a different forward measure; and *quanto adjustments* for cross-currency payoffs incorporating the correlation between the rate and the exchange rate.

### Calibration of Interest Rate Models

Calibration proceeds in two stages, reflecting the separation between the initial curve (a static snapshot) and the volatility structure (which governs option prices and dynamic behavior).

First, **fitting the initial yield curve**: time-dependent drift functions $\theta(t)$ (Hull--White) or the HJM construction ensure $P^{\text{model}}(0,T) = P^{\text{market}}(0,T)$ for all $T$. Methods include bootstrapping from swaps and bonds, spline interpolation, and the Nelson--Siegel--Svensson parameterization.

Second, **volatility structure calibration** targets cap/floor and swaption implied volatilities. The joint calibration objective $\min_\theta \sum w_c(C^{\text{model}} - C^{\text{mkt}})^2 + \sum w_s(S^{\text{model}} - S^{\text{mkt}})^2$ balances fit across instruments. **LMM calibration** uses a cascade: caplet volatilities pin down $\sigma_i$ sequentially, then correlation parameters $\rho_{ij}$ fit swaption prices through Rebonato's formula. Stability and identifiability remain persistent challenges, with Jacobian analysis, condition number diagnostics, and regularization penalties $\lambda\|\theta - \theta_{\text{prior}}\|^2$ guiding robust calibration.

### Interest Rate Model Risk

The post-2008 financial landscape introduced fundamental complications: multiple discount curves, negative rates, and the transition away from LIBOR. These challenges expose implicit assumptions in classical models and require careful extensions.

The **multi-curve framework** separates OIS discounting from tenor-specific LIBOR projection, with the OIS--LIBOR spread decomposing into credit, liquidity, and term premia. This increases dimensionality and introduces basis risk.

**Negative rates** expose implicit positivity assumptions in log-normal models. Responses include normal (Bachelier) models $dL = \sigma^{(n)}\,dW$, shifted log-normal models $d(L+s) = \sigma(L+s)\,dW$ with shift $s > 0$, and Gaussian short-rate models that naturally accommodate negative rates.

The **SOFR transition** replaces forward-looking LIBOR with backward-looking compounded overnight rates $R_{\text{SOFR}}(T_i, T_{i+1}) = \prod_{k}(1 + r_k \delta_k)/\delta - 1$, requiring RFR-adapted models with backward-looking rate dynamics. Model risk management requires validation across scenarios, stress testing, and conservative reserves.

!!! note "Role in the Book"
    This chapter extends the short-rate models of Chapter 18 to the full forward curve (HJM) and market-observable rates (LMM). The measure-change and Girsanov machinery from Chapter 4, Feynman--Kac theory from Chapter 5, and calibration framework from Chapter 17 are applied throughout. The convexity adjustments and multi-curve issues connect to the broader themes of model risk and practical implementation that run through the later chapters. The Hull--White model, a special case of HJM treated in full detail in Chapter 20, provides the bridge between short-rate and forward-curve approaches.
