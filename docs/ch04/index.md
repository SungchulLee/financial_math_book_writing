# Chapter 4: Measure Change and Girsanov's Theorem

This chapter develops the theory of probability measure changes in continuous time and its central application to derivative pricing. Starting from local martingales and stochastic exponentials, we establish the martingale foundations needed for measure change, then state and prove Girsanov's theorem with full intuition and rigorous detail. The chapter constructs the risk-neutral measure via drift removal, introduces the market price of risk, and extends the framework to numeraire changes and forward measures with worked examples spanning the Black-Scholes, multi-asset, stochastic volatility, foreign exchange, and interest rate settings. The chapter concludes with the financial interpretation of measure change---the distinction between pricing and hedging, between the physical and risk-neutral worlds, the decomposition of risk premia, and the pathologies that arise when measure change fails.

## Key Concepts

### **Local Martingales and the Martingale Hierarchy**
A **local martingale** is a process that becomes a true martingale when stopped at an increasing sequence of stopping times $\tau_n \to \infty$; the stopped process $M_{t \wedge \tau_n}$ is a martingale for each $n$. The distinction matters because many natural price processes---particularly Ito integrals with unbounded integrands---are local martingales but not true martingales. The strict inclusion hierarchy is $\text{UI Martingales} \subsetneq \text{Martingales} \subsetneq \text{Local Martingales}$. A non-negative local martingale is always a supermartingale (by Fatou's lemma), and a **strict local martingale** satisfies $\mathbb{E}[M_t] < \mathbb{E}[M_0]$. Sufficient conditions for upgrading a local martingale to a true martingale include boundedness, domination by an integrable random variable, $L^p$ boundedness for $p > 1$, and finite expected quadratic variation $\mathbb{E}[\langle M \rangle_T] < \infty$. In finance, strict local martingales correspond to **asset price bubbles**: when the discounted price process is a strict local martingale under $\mathbb{Q}$, the current price exceeds the discounted expected future payoff, $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0$, and put-call parity fails.

### **The Stochastic Exponential**
The **stochastic exponential** (Doleans-Dade exponential) of a continuous semimartingale $X_t$ is the unique solution to $d\mathcal{E}(X)_t = \mathcal{E}(X)_t\, dX_t$ with $\mathcal{E}(X)_0 = 1$, given explicitly by

$$\mathcal{E}(X)_t = \exp\!\left(X_t - X_0 - \tfrac{1}{2}\langle X \rangle_t\right)$$

The correction term $-\frac{1}{2}\langle X \rangle_t$ is the Ito correction that removes the drift arising from Ito's lemma, ensuring that $\mathcal{E}(X)$ is a local martingale when $X$ is. Key properties include strict positivity ($\mathcal{E}(X)_t > 0$ always), the multiplication rule $\mathcal{E}(X) \cdot \mathcal{E}(Y) = \mathcal{E}(X + Y + \langle X, Y \rangle)$, and unit expectation when the stochastic exponential is a true martingale. Whether $\mathcal{E}(X)$ is a true martingale (not merely a local martingale) is validated by Novikov or Kazamaki conditions. The stochastic exponential provides the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = Z_T$ for measure changes and is the fundamental building block of Girsanov's theorem.

### **Martingales and No-Arbitrage**
The deep connection between no-arbitrage and martingale pricing is the foundation of modern asset pricing theory. A discounted price process $\tilde{S}_t = S_t / B_t$ under the physical measure $\mathbb{P}$ has drift $(\mu_t - r_t)\tilde{S}_t$, violating the martingale property. The **Fundamental Theorem of Asset Pricing (FTAP)** states that no-arbitrage (NFLVR) holds if and only if there exists an **Equivalent Local Martingale Measure (ELMM)** $\mathbb{Q} \sim \mathbb{P}$ under which discounted prices are local martingales:

$$\text{No Arbitrage (NFLVR)} \iff \exists\, \mathbb{Q} \sim \mathbb{P} : \tilde{S}_t \text{ is a } \mathbb{Q}\text{-local martingale}$$

The proof that an ELMM rules out arbitrage uses the **supermartingale argument**: for any admissible strategy with gains $G_t(\phi) = \int_0^t \phi_s\, d\tilde{S}_s$ bounded below, $G_t$ is a local martingale bounded below, hence a supermartingale, giving $\mathbb{E}^{\mathbb{Q}}[G_T] \leq 0$---combined with $G_T \geq 0$ this forces $G_T = 0$ a.s. The **Second Fundamental Theorem** states that an arbitrage-free market is **complete** if and only if $\mathbb{Q}$ is unique. In incomplete markets (e.g., stochastic volatility), multiple ELMMs exist and derivative prices lie in an interval.

### **The Risk-Neutral Valuation Principle**
The central pricing formula of mathematical finance states that, in an arbitrage-free market, the time-$t$ price of a contingent claim with payoff $\Phi(X_T)$ at maturity $T$ is

$$V_t = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\, ds}\, \Phi(X_T) \;\middle|\; \mathcal{F}_t\right]$$

The derivation follows from the FTAP: discounted derivative prices must be $\mathbb{Q}$-martingales, so the martingale property gives $\tilde{V}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T \mid \mathcal{F}_t]$, and the terminal condition $V_T = \Phi(X_T)$ yields the formula. Under $\mathbb{Q}$, the drift of $S_t$ changes from $\mu$ to $r$ while volatility $\sigma$ is invariant---this is why derivative prices do not depend on $\mu$. The risk-neutral valuation is equivalent to solving the pricing PDE via the **Feynman-Kac theorem**, connecting the expectation approach to the Black-Scholes PDE.

### **The Martingale Representation Theorem**
Under the augmented Brownian filtration, every square-integrable martingale $M_t$ admits the unique representation

$$M_t = M_0 + \int_0^t \phi_s\, dW_s$$

for a predictable process $\phi$ with $\mathbb{E}[\int_0^T \phi_s^2\, ds] < \infty$. This is the **predictable representation property**: Brownian motion is the sole source of randomness in its filtration, so every martingale is built entirely from Brownian increments. In finance, this is the mathematical foundation for **perfect hedging in complete markets**: the replicating portfolio strategy is given by the integrand $\Delta_t = \psi_t / (\sigma S_t) \cdot e^{rt}$, which equals $\partial V / \partial S$ in the Black-Scholes model. Extensions include the **Clark-Ocone formula** from Malliavin calculus (providing explicit expressions for $\phi_t$) and the **Kunita-Watanabe decomposition** for incomplete markets, which splits any martingale into a hedgeable part and an orthogonal residual representing unhedgeable risk.

### **Novikov and Kazamaki Conditions**
For the stochastic exponential $Z_t = \mathcal{E}(\int_0^\cdot \theta_s\, dW_s)_t$ to serve as a valid Radon-Nikodym derivative, it must be a true martingale with $\mathbb{E}[Z_T] = 1$. The **Novikov condition**

$$\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\tfrac{1}{2}\int_0^T \theta_s^2\, ds\right)\right] < \infty$$

is sufficient to guarantee this. The weaker **Kazamaki condition** requires $\sup_{t \leq T} \mathbb{E}[\exp(\frac{1}{2}M_t)] < \infty$, where $M_t = \int_0^t \theta_s\, dW_s$. Novikov implies Kazamaki, but not conversely. For deterministic or bounded $\theta$, Novikov reduces to $\theta \in L^2[0,T]$; for the Black-Scholes model with constant $\theta = (\mu - r)/\sigma$, verification is immediate. For stochastic volatility models (e.g., Heston), Novikov verification connects to the **Feller condition** $2\kappa\bar{V} \geq \xi^2$ ensuring the variance process stays positive. When both conditions fail, the stochastic exponential may be a strict local martingale with $\mathbb{E}[Z_T] < 1$, and the measure change is invalid---this connects to the theory of asset price bubbles.

### **Girsanov's Theorem: Intuition and Statement**
Girsanov's theorem resolves the apparent paradox of how a process with drift can become driftless without changing its paths. The key insight is that **drift lives in the probability measure, not in the paths**: changing from $\mathbb{P}$ to $\mathbb{Q}$ reweights the probability of each path, so that upward-trending paths are downweighted and the ensemble average loses its drift. Formally, given an adapted process $\theta_t$ satisfying Novikov's condition, define the exponential martingale

$$Z_t = \exp\!\left(-\int_0^t \theta_s\, dW_s - \frac{1}{2}\int_0^t \theta_s^2\, ds\right)$$

and the new measure $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = Z_T$. Then $\widetilde{W}_t = W_t + \int_0^t \theta_s\, ds$ is a standard Brownian motion under $\mathbb{Q}$. The proof proceeds by verifying (via Ito's lemma) that $dZ_t = -Z_t \theta_t\, dW_t$ has no drift term, so $Z_t$ is a martingale; then showing that $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale with quadratic variation $\langle \widetilde{W} \rangle_t = t$; and applying **Levy's characterization theorem** to conclude $\widetilde{W}_t$ is $\mathbb{Q}$-Brownian motion.

### **Drift Adjustment and Financial Meaning**
The financial application of Girsanov's theorem removes the risk premium from asset dynamics. Under $\mathbb{P}$, $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t^{\mathbb{P}}$. The **market price of risk** $\theta = (\mu - r)/\sigma$ measures excess return per unit of volatility. Defining $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ and performing the measure change yields the **risk-neutral dynamics**

$$dS_t = r S_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$$

The discounted price $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale. Crucially, volatility is unchanged and sample paths are identical---only probability weights are adjusted. Worked examples include the Black-Scholes model (constant parameters), geometric Brownian motion with explicit Radon-Nikodym derivatives, and the Vasicek model where the market price of interest rate risk shifts the long-run mean from $\bar{r}$ to $\bar{r} - \sigma\theta/\kappa$.

### **Construction of the Risk-Neutral Measure**
Construction of $\mathbb{Q}$ proceeds by identifying $\theta_t = (\mu_t - r_t)/\sigma_t$ and applying Girsanov's theorem to make $\tilde{S}_t = S_t / B_t$ a $\mathbb{Q}$-martingale. Detailed examples cover: the **Black-Scholes model** (single stock, unique $\theta$, complete market), **stocks with dividends** (risk-neutral dynamics $dS_t = (r-q)S_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$), **two correlated stocks** (market price of risk vector $\boldsymbol{\theta}$ satisfying $\boldsymbol{\mu} - r\mathbf{1} = \Sigma \boldsymbol{\theta}$, unique when the volatility matrix has full rank), the **Heston stochastic volatility model** (incomplete market with undetermined volatility risk premium $\theta_2$), **foreign exchange** ($\theta = 0$ when the drift equals the interest rate differential), and the **Vasicek interest rate model** (exogenous market price of risk shifting the risk-neutral long-run mean). In complete markets ($n$ assets, $n$ Brownian motions), $\theta$ is unique; in incomplete markets, infinitely many valid risk-neutral measures exist.

### **Market Price of Risk**
The market price of risk $\theta_t = (\mu_t - r_t)/\sigma_t$ quantifies the excess return investors demand per unit of volatility risk. It determines the Radon-Nikodym derivative for the measure change, tilting probabilities from $\mathbb{P}$ to $\mathbb{Q}$. In the multi-asset case, it generalizes to a vector $\boldsymbol{\theta}_t \in \mathbb{R}^d$ satisfying $\boldsymbol{\mu}_t - r_t \mathbf{1} = \Sigma_t \boldsymbol{\theta}_t$. The market price of risk encodes risk premia, links economic intuition with probabilistic structure, and is the bridge connecting observed returns to risk-neutral pricing.

### **Numeraire and Change of Measure**
Each strictly positive traded asset $N_t$ defines a **numeraire measure** $\mathbb{Q}^N$ under which prices normalized by $N_t$ are martingales. The general pricing formula becomes $V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}[\Phi_T / N_T \mid \mathcal{F}_t]$. The **change-of-numeraire formula** relates any two numeraire measures:

$$\frac{d\mathbb{Q}^N}{d\mathbb{Q}^M}\bigg|_{\mathcal{F}_T} = \frac{N_T / N_0}{M_T / M_0}$$

Common numeraires include the money market account $B_t$ (giving $\mathbb{Q}$), the zero-coupon bond $P(t,T)$ (giving the $T$-forward measure $\mathbb{Q}^T$), and asset prices themselves (giving the stock measure). The **annuity numeraire** $A(t) = \sum_i \tau_i P(t, T_i)$ yields the swap measure under which the swap rate is a martingale, leading to Black's model for swaptions. Numeraire choice dramatically simplifies pricing: **Black's formula** $C_t = P(t,T)[F_t\Phi(d_1) - K\Phi(d_2)]$ for calls on forwards, and **Margrabe's formula** $V_t = S_t^1\Phi(d_1) - S_t^2\Phi(d_2)$ for exchange options, both emerge from judicious numeraire selection.

### **The Forward Measure**
The **$T$-forward measure** $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numeraire, with Radon-Nikodym derivative $d\mathbb{Q}^T/d\mathbb{Q}|_{\mathcal{F}_t} = P(t,T)/(P(0,T) B_t)$. Under $\mathbb{Q}^T$, the forward price $F(t,T) = S_t / P(t,T)$ is a martingale, so the pricing formula becomes

$$V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[\Phi_T \mid \mathcal{F}_t]$$

eliminating the need for stochastic discounting. The forward LIBOR rate $L(t; T, T+\delta)$ defined by $1 + \delta L = P(t,T)/P(t,T+\delta)$ is a $\mathbb{Q}^{T+\delta}$-martingale, yielding **Black's formula for caplets**: $V_t = P(t,T+\delta) \cdot \delta \cdot [L_t \Phi(d_1) - K\Phi(d_2)]$. Multiple maturities create a tower of forward measures $\mathbb{Q}^{T_1} \leftrightarrow \mathbb{Q}^{T_2} \leftrightarrow \cdots$, all connected by Radon-Nikodym derivatives. Forward measures are the natural tool for interest rate derivatives (caps, floors, swaptions) and bond options.

### **Pricing vs Hedging**
Pricing and hedging are distinct economic problems unified by measure change. **Pricing** asks "what is the fair value?" and is answered by the $\mathbb{Q}$-expectation $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-\int_0^T r_s\, ds} X_T]$; it depends on the risk-neutral dynamics and payoff structure. **Hedging** asks "how can the payoff be replicated?" and is a trading problem answered by the martingale representation integrand $\phi_t$; it is **measure-invariant** because self-financing strategies remain self-financing under any equivalent measure. In complete markets, pricing and hedging coincide (the price equals the cost of the unique replicating strategy), while in incomplete markets, pricing is not unique and hedging is imperfect.

### **Physical vs Risk-Neutral World**
The physical measure $\mathbb{P}$ describes how asset prices actually evolve---with risk premia, empirical return distributions, and investor preferences. The risk-neutral measure $\mathbb{Q}$ is a mathematical pricing tool under which expected excess returns vanish and discounted prices are martingales. The two measures are **equivalent** ($\mathbb{P}(A) = 0 \iff \mathbb{Q}(A) = 0$), so they assign positive probability to the same events but with different weights. The $\mathbb{Q}$ measure should not be interpreted as a forecast or investor belief---its sole purpose is to ensure arbitrage-free pricing. In practice, use $\mathbb{Q}$ for pricing derivatives and $\mathbb{P}$ for risk management, forecasting, and portfolio optimization.

### **Risk Premium Decomposition**
The risk premium $\mu - r = \sigma\theta$ decomposes the physical drift into the risk-free rate $r$ and compensation for bearing volatility risk $\sigma\theta$. This decomposition connects the market price of risk to the observed excess return, quantifying how much of the physical drift compensates investors for exposure to randomness. Large $\theta$ indicates high compensation required for bearing risk; small $\theta$ implies low risk premia.

### **When Measure Change Fails**
Measure change can fail in several important settings: when markets are **incomplete** (the risk-neutral measure is non-unique, leaving derivative prices undetermined), when **Novikov and Kazamaki conditions** are violated (the stochastic exponential is only a local martingale with $\mathbb{E}[Z_T] < 1$, so the measure change does not define a valid probability measure), and when **bubbles** cause the discounted price to be a strict local martingale under $\mathbb{Q}$. These pathologies connect to the CEV model with exponent $\beta > 1$ (explosion to infinity), the reciprocal of the 3D Bessel process (mass leakage), and practical scenarios involving unchecked model assumptions.

### **Practitioner Perspective**
From a practitioner standpoint, measure change connects theoretical pricing to market practice. The risk-neutral measure $\mathbb{Q}$ is typically inferred from market prices of liquid instruments (calibration) rather than derived from the physical measure $\mathbb{P}$. Model calibration, the choice of numeraire, and the treatment of incomplete markets all require careful interpretation of the mathematical framework in the context of real trading and risk management.

!!! note "Role in the Book"
    Girsanov's theorem and the risk-neutral measure are the theoretical engine behind the Black-Scholes PDE derivation (Chapter 6), the Feynman-Kac connection between expectations and PDEs (Chapter 5), and interest rate modeling via forward measures (Chapter 19). The martingale representation theorem provides the mathematical basis for hedging arguments used throughout the remainder of the book. The Fundamental Theorem of Asset Pricing, whose continuous-time formulation relies on the tools developed here, connects to the discrete-time foundations in Chapter 1.

---
