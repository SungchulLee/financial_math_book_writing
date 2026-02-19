# Chapter 20: The Hull-White Model in Detail

This chapter provides a comprehensive treatment of the Hull-White extended Vasicek model for interest rate derivatives, from its mathematical foundations through analytical bond and derivative pricing, tree-based and Monte Carlo implementations, and calibration to market data. Starting from the HJM framework and the connection to Vasicek, we derive the model's affine structure, solve for the short rate and bond prices in closed form, develop the named function apparatus, price bond options, caps, floors, and swaptions analytically, and extend to the two-factor model for richer yield curve dynamics.

## Key Concepts

**Model Definition and HJM Derivation**
The Hull-White model (1990) specifies the risk-neutral short rate dynamics:

$$dr_t = [\theta(t) - a\,r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}$$

where $a > 0$ is the mean-reversion speed, $\sigma > 0$ is the short-rate volatility, and $\theta(t)$ is a time-dependent drift chosen to exactly fit the initial term structure. The model arises from the **Heath-Jarrow-Morton** framework (Chapter 19) by choosing a deterministic volatility function $\sigma_f(t,T) = \sigma e^{-a(T-t)}$ for the instantaneous forward rate. The HJM drift condition then determines the risk-neutral drift endogenously: $\theta(t) = \partial_t f(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$, where $f(0,t)$ is the initial forward curve. This is the **extended Vasicek** model: the constant $\theta$ of the Vasicek model becomes $\theta(t)$ to absorb the initial term structure, ensuring $P^{\text{model}}(0,T) = P^{\text{market}}(0,T)$ for all $T$—a critical requirement for interest rate derivative pricing.

**Short Rate Solution and Distribution**
The Ornstein-Uhlenbeck SDE has the explicit solution:

$$r_t = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du + \sigma\int_s^t e^{-a(t-u)}\,dW_u$$

The short rate is **Gaussian** with conditional distribution $r_t \mid r_s \sim N(\mu(s,t), \Sigma^2(s,t))$ where $\mu(s,t) = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du$ and $\Sigma^2(s,t) = \frac{\sigma^2}{2a}(1-e^{-2a(t-s)})$. The **short rate decomposition** $r_t = \alpha(t) + x_t$ separates the deterministic mean-reverting component $\alpha(t)$ (absorbing $\theta(t)$ and the initial curve) from the zero-mean Gaussian process $x_t$ satisfying $dx_t = -ax_t\,dt + \sigma\,dW_t$, simplifying many calculations. A known limitation: the Gaussian distribution allows negative rates, which is acceptable for some currencies but problematic for others—the Black-Karasinski model $d\ln r_t = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$ addresses this at the cost of losing analytical tractability.

**Bond Pricing and the Affine Structure**
The model's affine structure yields the exponential-affine bond price:

$$P(t,T) = \exp\!\left(A(t,T) - B(t,T)\,r_t\right)$$

where $B(t,T) = \frac{1-e^{-a(T-t)}}{a}$ and $A(t,T)$ is determined by fitting to the initial curve: $A(t,T) = \ln\frac{P(0,T)}{P(0,t)} - B(t,T)f(0,t) - \frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$. This can be derived either via the **expectation method** $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds} \mid r_t]$, exploiting the Gaussian distribution of $\int_t^T r_s\,ds$, or via the **PDE method** with the bond pricing equation $\partial_t P + (\theta - ar)\partial_r P + \frac{1}{2}\sigma^2\partial_{rr}P - rP = 0$. Consistency with the initial yield curve is verified: $P(0,T) = \exp(A(0,T) - B(0,T)r_0) = P^{\text{market}}(0,T)$ by construction. **Yield curve dynamics** under Hull-White preserve the parallel-shift-plus-decay structure: yields at all maturities are affine functions of $r_t$, with loadings $B(t,T)/(T-t)$ that decay exponentially.

**Named Functions and Measure Change**
The **named functions** $B(\tau) = (1-e^{-a\tau})/a$, $M(t,T) = \mathbb{E}^{\mathbb{Q}}[\int_t^T r_s\,ds \mid r_t]$, and $V(t,T) = \text{Var}[\int_t^T r_s\,ds \mid r_t] = \frac{\sigma^2}{a^2}[\tau - 2B(\tau) + \frac{1}{2a}(1-e^{-2a\tau})]$ compactly express all pricing formulas. The **$T$-forward measure** $\mathbb{Q}^T$, defined by the numéraire $P(t,T)$, transforms the short rate drift: under $\mathbb{Q}^T$, $dr_t = [\theta(t) - ar_t - \sigma^2 B(t,T)]\,dt + \sigma\,dW_t^T$—the drift is reduced by $\sigma^2 B(t,T)$, reflecting the convexity adjustment. Forward bond prices $P(t,S)/P(t,T)$ are martingales under $\mathbb{Q}^T$, simplifying the pricing of options on bonds.

**Bond Options, Caps, and Swaptions**
The **zero-coupon bond option** price has the Black-like formula:

$$\text{Call}(t; T, S, K) = P(t,S)\,N(d_+) - K\,P(t,T)\,N(d_-)$$

where $d_{\pm} = \frac{\ln(P(t,S)/(K\,P(t,T)))}{\sigma_P} \pm \frac{\sigma_P}{2}$ and $\sigma_P = \frac{\sigma}{a}(1-e^{-a(S-T)})\sqrt{\frac{1-e^{-2a(T-t)}}{2a}}$ is the bond price volatility. **Jamshidian's trick** decomposes a coupon bond option into a portfolio of zero-coupon bond options: since all bond prices are monotone functions of $r_T$, the coupon bond option exercises optimally at a unique threshold $r^*$, and the payoff splits as $\sum_i c_i(P(T,T_i) - K_i)^+$ where $K_i = P_{r^*}(T,T_i)$. **Caplets** are put options on zero-coupon bonds: $\text{Caplet}(t; T_{i-1}, T_i) = (1+\delta K_{\text{cap}})\,\text{Put}(t; T_{i-1}, T_i, 1/(1+\delta K_{\text{cap}}))$ where $\delta = T_i - T_{i-1}$. **Caps** are portfolios of caplets. **Swaptions** price is obtained either via Jamshidian's trick on the swap as a coupon bond, or by direct integration under the annuity measure, yielding a Black-like formula with the swap rate volatility.

**Calibration**
Hull-White calibration proceeds in two stages: (1) the initial curve $P(0,T)$ determines $\theta(t)$ analytically—this is exact by construction; (2) the volatility parameters $(a, \sigma)$ are calibrated to **cap volatilities** or **swaption volatilities** by minimizing $\sum_i w_i(\sigma_{\text{model}}^i - \sigma_{\text{market}}^i)^2$. **Joint calibration** to both caps and swaptions is overconstrained for a two-parameter model, requiring trade-offs. The mean-reversion $a$ primarily controls the decorrelation between short and long rates (and hence the swaption skew), while $\sigma$ scales the overall volatility level. **Parameter stability** is important: small changes in $a$ can significantly affect long-dated swaption prices while barely changing cap prices, creating instability in joint calibration. **Identifiability**: $a$ and $\sigma$ are well-identified from at-the-money volatilities across multiple tenors, but the two-parameter model cannot fit the full volatility surface, motivating extensions.

**Tree Implementation**
The **trinomial tree** (Hull-White, 1994) discretizes the short rate process for pricing path-dependent and early-exercise derivatives. Construction: (1) build a tree for the zero-mean process $x_t$ on a recombining grid with spacing $\Delta x = \sigma\sqrt{3\Delta t}$; (2) choose branching probabilities to match the first two moments of $x_t$; (3) shift each time slice by $\alpha(t_i)$ to fit the initial yield curve. **Arrow-Debreu prices** propagated through the tree enable efficient calibration: $\alpha(t_i)$ is chosen so that $\sum_j Q_{ij}e^{-(r_j + \alpha_i)\Delta t}P(0,t_i) = P(0, t_{i+1})$. **American and Bermudan swaptions** are priced by backward induction with early exercise comparison at each node. The tree naturally handles time-dependent $\theta(t)$ and provides a lattice visualization of the yield curve dynamics.

**Two-Factor Extension**
The two-factor Hull-White model adds a second mean-reverting factor:

$$dr_t = [\theta(t) + u_t - a\,r_t]\,dt + \sigma_1\,dW_t^{(1)}, \qquad du_t = -b\,u_t\,dt + \sigma_2\,dW_t^{(2)}$$

with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt$. The additional factor $u_t$ allows richer yield curve dynamics: twist and butterfly movements beyond the parallel shifts of the one-factor model. Bond prices remain exponential-affine in $(r_t, u_t)$, preserving analytical tractability. The correlation between factors controls the shape of the yield curve volatility surface. Calibration with four parameters $(a, b, \sigma_1, \sigma_2)$ plus $\rho$ fits the swaption volatility matrix more accurately than the one-factor model, particularly for off-diagonal (non-co-terminal) swaptions.

**Monte Carlo Simulation**
**Exact simulation** exploits the Gaussian transition density: $r_{t+\Delta t} = \mu(t, t+\Delta t) + \Sigma(t, t+\Delta t)\,Z$ with $Z \sim N(0,1)$, requiring no discretization error. Bond prices along each path are computed via $P(t_i, T) = \exp(A(t_i, T) - B(t_i, T)r_{t_i})$. **Path-dependent derivatives** (e.g., callable bonds, range accruals, TARNs) are priced by simulating the short rate path and applying exercise/knock-out conditions. **Variance reduction**: antithetic variates, control variates (using the analytical bond price), and stratified sampling on the initial short rate all improve efficiency.

!!! note "Role in the Book"
    The Hull-White model is the workhorse short-rate model for interest rate derivatives, complementing the HJM and LIBOR market model frameworks (Chapter 19). Its affine structure connects to the general theory of Chapter 15, the calibration techniques parallel Chapter 17, and the tree and Monte Carlo implementations extend the numerical methods of Chapter 8 to the interest rate domain. The model's Gaussian limitation motivates the CIR-based and log-normal alternatives discussed in Chapter 18.

---
