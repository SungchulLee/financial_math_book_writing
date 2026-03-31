# Introduction to the Black-Scholes Model


The **Black-Scholes model**, developed independently by Fischer Black and Myron Scholes (1973) and Robert Merton (1973), constitutes a cornerstone of modern financial mathematics. It provides a robust framework for pricing European options under the assumption that the underlying asset follows **geometric Brownian motion**—a continuous-time stochastic process.

This section introduces the Black-Scholes model, its historical significance, and its relationship to the discrete-time binomial framework studied in Section 2.1.

---

## Historical Context and Significance


### 1. **The Problem Before Black-Scholes**


Prior to 1973, option pricing was largely heuristic:

- Traders used rules of thumb and intuition
- Academic models existed but lacked practical applicability
- No consensus on how to value the "optionality" component

The key challenge: How to price the **volatility risk** embedded in options?

### 2. **The Breakthrough**


Black, Scholes, and Merton showed that:

1. **Perfect hedging is possible** (in theory) through continuous rebalancing
2. **No expected return assumption needed**: Pricing depends only on volatility, not on whether investors are risk-averse or risk-seeking
3. **Closed-form formulas exist** for European options

**Impact**:

- 1997 Nobel Prize in Economics (Scholes and Merton; Black had passed away in 1995)
- Foundation for the modern derivatives industry (trillions in notional value)
- Sparked development of quantitative finance as a discipline

### 3. **Why It Matters**


The Black-Scholes model elegantly captures the interplay between:

- **Stochastic dynamics**: Random asset price movements
- **Deterministic constraints**: No-arbitrage conditions

It demonstrates that derivative pricing can be **model-based and systematic** rather than purely speculative.

---

## From Discrete to Continuous Time


### 1. **The Binomial Model as Foundation**


Recall from Section 2.1 that the **binomial model** provides a discrete-time framework:

- Time divided into finite steps $\Delta t$
- Asset price moves up by factor $u$ or down by factor $d$
- Options priced via backward induction

**Key insights from binomial model**:

1. Replication via dynamic hedging
2. Risk-neutral valuation
3. No-arbitrage principle

### 2. **The Continuous-Time Limit**


The Black-Scholes model emerges as the **continuous-time limit** of the binomial framework:

$$
\lim_{n \to \infty, \Delta t \to 0} \text{Binomial Model} = \text{Black-Scholes Model}
$$

where $n$ is the number of time steps and $\Delta t = T/n$.

**Mathematical convergence**:

- Discrete jumps → Continuous diffusion
- Binomial lattice → Geometric Brownian motion
- Discrete hedging → Continuous delta hedging
- Recursive valuation → Partial differential equation

This connection shows that Black-Scholes is the **natural extension** of simpler discrete models, not a separate theory.

### 3. **Why Go to Continuous Time?**


**Advantages**:

1. **Analytical tractability**: Closed-form solutions via PDE theory
2. **Mathematical elegance**: Rigorous framework using stochastic calculus
3. **Hedging precision**: Theoretically perfect replication (in limit)
4. **Generalization**: Easier to extend to complex derivatives

**Trade-offs**:

1. Requires more sophisticated mathematics (Itô calculus)
2. Continuous hedging is impossible in practice (discrete approximation needed)
3. Model assumptions become more stringent

---

## The Black-Scholes Framework


### 1. **Core Components**


The Black-Scholes model consists of three interrelated elements:

**1. Asset Price Dynamics**

The stock price $S_t$ follows **geometric Brownian motion**:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

where:

- $\mu$ = drift (expected return)
- $\sigma$ = volatility (standard deviation of returns)
- $W_t$ = standard Brownian motion

**2. Derivative Valuation**

The option value $V(S,t)$ satisfies the **Black-Scholes PDE**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

with terminal condition (for European call):

$$
V(S,T) = \max(S-K, 0)
$$

**3. Hedging Strategy**

The replicating portfolio:

$$
\Pi = V - \Delta S
$$

where $\Delta = \frac{\partial V}{\partial S}$ is the **delta** (hedge ratio).

By constructing this portfolio to be **locally risk-free**, we eliminate uncertainty and derive the PDE.

---

## Key Insights from the Model


### 1. **No Expected Return in Pricing**


**Remarkable fact**: The option price depends on $\sigma$ but **not on $\mu$**.

**Intuition**: 

- Higher expected return $\mu$ increases both the stock price and the strike payment
- These effects cancel out in the hedging portfolio
- Only volatility $\sigma$ (unpredictable variation) matters for option value

**Implication**: Investors with different return expectations still agree on option prices.

### 2. **Risk-Neutral Valuation**


Under the **risk-neutral measure** $\mathbb{Q}$:

$$
V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\text{Payoff}]
$$

The asset grows at the risk-free rate $r$ (not the actual expected return $\mu$):

$$
dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

**Why this works**:

- The hedging portfolio earns the risk-free rate
- Pricing as if risk-neutral simplifies calculations
- The replication argument justifies this "artificial" probability measure

### 3. **Dynamic Hedging**


Unlike buy-and-hold strategies, option replication requires **continuous rebalancing**:

- Delta changes as $S$ and $t$ change
- Portfolio must be adjusted continuously (in theory)
- This generates the "path-independent" option value

**Connection to binomial**: Discrete rebalancing at each node → continuous adjustment in the limit.

---

## The Black-Scholes PDE


### 1. **Derivation Idea** (Details in Section 5.4)


**Step 1**: Construct a hedged portfolio

$$
\Pi = V - \Delta S
$$

**Step 2**: Choose $\Delta$ to eliminate randomness

$$
\Delta = \frac{\partial V}{\partial S}
$$

**Step 3**: Apply Itô's lemma to $V(S,t)$

$$
dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}dt
$$

**Step 4**: Show portfolio is risk-free

$$
d\Pi = \left[\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right]dt
$$

**Step 5**: No-arbitrage requires risk-free return

$$
d\Pi = r\Pi dt
$$

**Result**: The Black-Scholes PDE.

### 2. **Trivial Solutions**


Before solving for option prices, observe that simple portfolios satisfy the PDE:

**1. The stock itself**: $V = S$

Verify:

$$
\frac{\partial S}{\partial t} = 0, \quad \frac{\partial S}{\partial S} = 1, \quad \frac{\partial^2 S}{\partial S^2} = 0
$$

$$
0 + \frac{1}{2}\sigma^2 S^2 \cdot 0 + rS \cdot 1 - rS = 0 \quad \checkmark
$$

**2. The risk-free bond**: $V = e^{rt}$

Verify:

$$
\frac{\partial e^{rt}}{\partial t} = re^{rt}, \quad \frac{\partial e^{rt}}{\partial S} = 0, \quad \frac{\partial^2 e^{rt}}{\partial S^2} = 0
$$

$$
re^{rt} + 0 + 0 - re^{rt} = 0 \quad \checkmark
$$

**Interpretation**: The PDE correctly describes basic traded assets. Any **linear combination** of stock and bond also satisfies the PDE, forming the basis of replication.

**Non-trivial solutions**: Options with payoffs $(S-K)^+$ or $(K-S)^+$ require solving the full PDE.

---

## Scope and Applications


### 1. **What the Model Prices**


**Primary applications**:

- European call and put options
- Forward contracts
- Barrier options (with modifications)
- Compound options
- Exchange options

**Extensions**:

- Dividends (continuous or discrete)
- Time-varying parameters
- Multiple underlying assets

### 2. **What It Doesn't Cover**


**Requires other methods**:

- **American options**: Early exercise creates free boundary problem (no closed form)
- **Path-dependent options**: Asian, lookback options need numerical methods or Monte Carlo
- **Jump processes**: Merton jump-diffusion extends the framework
- **Stochastic volatility**: Heston, SABR models relax constant $\sigma$

**Practical limitations**:

- Market frictions (transaction costs, liquidity)
- Discrete hedging (not continuous)
- Model risk (wrong assumptions)

---

## Beyond Black-Scholes


### 1. **The Model's Legacy**


The Black-Scholes framework spawned:

**1. Practical tools**:

- Greeks (delta, gamma, vega, theta, rho) for risk management
- Implied volatility as a market indicator
- Structured products and exotic derivatives

**2. Theoretical developments**:

- Risk-neutral pricing theory
- Stochastic volatility models (Heston)
- Local volatility (Dupire)
- Jump-diffusion (Merton)
- Rough volatility models

**3. Industry infrastructure**:

- Options exchanges (CBOE launched in 1973)
- Trading systems and risk platforms
- Regulatory frameworks (VaR, stress testing)

### 2. **When to Use Black-Scholes**


**Appropriate for**:

- Liquid European options with short maturities
- Quick approximations and benchmarking
- Understanding market-implied volatility
- Teaching fundamental concepts

**Limitations require caution**:

- Volatility smiles/skews (violated constant $\sigma$ assumption)
- Extreme events (fat tails, jumps)
- Illiquid markets
- American or exotic options

---

## Roadmap for Remaining Sections


The subsequent sections build on this foundation:

**Section 2.4: Black-Scholes Formula**

- Closed-form solutions for calls and puts
- Interpretation of formula components
- Probabilistic meaning
- Properties and bounds

**Section 2.5: BS PDE Derivation**

- Rigorous derivation via delta hedging
- Risk-neutral measure construction
- Alternative derivation methods (change of numeraire, equilibrium)

**Section 2.6: Analytical Solutions**

- PDE solution techniques (heat equation, Fourier transform, Feynman-Kac)
- Mathematical tools for solving BS PDE

**Section 2.7: Numerical Solutions**

- Finite difference methods
- Handling American options and free boundaries

**Section 2.8: Extensions**

- Local volatility, stochastic volatility
- Jump-diffusion models
- Incomplete markets

---

## Summary


The Black-Scholes model represents the transition from discrete to continuous time in derivative pricing:

**Key concepts**:

1. **Continuous-time limit**: Natural extension of binomial model as $\Delta t \to 0$
2. **Geometric Brownian motion**: Asset price follows log-normal diffusion
3. **No-arbitrage principle**: Dynamic hedging eliminates risk, leading to PDE
4. **Risk-neutral valuation**: Pricing via expectation under artificial measure
5. **Model-based pricing**: Systematic framework replacing intuition

**Significance**:

- Revolutionized derivatives markets
- Established quantitative finance as rigorous discipline
- Foundation for modern risk management
- Spawned generations of extensions and refinements

**Limitations**:

- Stylized assumptions (constant volatility, continuous trading, no jumps)
- Real markets deviate (volatility smiles, transaction costs, crises)
- Extensions needed for practical applications

Understanding the Black-Scholes model---its derivation, assumptions, and limitations---is essential for anyone working in quantitative finance, as it provides both powerful tools and cautionary lessons about the gap between theory and practice.

---

## Exercises

**Exercise 1.** Verify that $V(S,t) = S$ and $V(S,t) = e^{r(t-T)}$ both satisfy the Black-Scholes PDE. Then show that the linear combination $V(S,t) = aS + be^{r(t-T)}$ also satisfies the PDE for any constants $a$ and $b$. What financial instrument does this represent?

---

**Exercise 2.** In the binomial model, the risk-neutral probability is $p = \frac{e^{r\Delta t} - d}{u - d}$. Using the CRR parameterization $u = e^{\sigma\sqrt{\Delta t}}$ and $d = e^{-\sigma\sqrt{\Delta t}}$, show that as $\Delta t \to 0$, the binomial model converges to the Black-Scholes model by verifying that the binomial stock price distribution converges to a log-normal distribution.

---

**Exercise 3.** Explain why the Black-Scholes option price does not depend on the expected return $\mu$ of the stock. Construct a simple argument using two investors who agree on $\sigma$ but disagree on $\mu$ to show that they must nonetheless agree on the option price, provided no arbitrage exists.

---

**Exercise 4.** The Black-Scholes PDE is $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$. Identify the type of this PDE (elliptic, parabolic, or hyperbolic) by examining its principal part. What is the financial significance of this classification?

---

**Exercise 5.** Consider two options on the same underlying stock ($S_0 = 100$, $\sigma = 30\%$, $r = 5\%$): a European call with $K = 100$ and $T = 0.5$, and a European call with $K = 100$ and $T = 2$. Without computing exact prices, use the properties described in this section to determine which option has a higher price and explain why.

---

**Exercise 6.** List three derivative instruments that the standard Black-Scholes model cannot price directly and explain what feature of each instrument violates the Black-Scholes framework. For each, name a specific model extension or numerical method that can handle it.

---

## Solutions

??? success "Solution to Exercise 1"
    **Verification that $V(S,t) = S$ satisfies the BS PDE**:

    $$
    \frac{\partial S}{\partial t} = 0, \quad \frac{\partial S}{\partial S} = 1, \quad \frac{\partial^2 S}{\partial S^2} = 0
    $$

    Substituting: $0 + \frac{1}{2}\sigma^2 S^2 \cdot 0 + rS \cdot 1 - rS = 0$. $\checkmark$

    **Verification that $V(S,t) = e^{r(t-T)}$ satisfies the BS PDE**:

    $$
    \frac{\partial}{\partial t}e^{r(t-T)} = re^{r(t-T)}, \quad \frac{\partial}{\partial S}e^{r(t-T)} = 0, \quad \frac{\partial^2}{\partial S^2}e^{r(t-T)} = 0
    $$

    Substituting: $re^{r(t-T)} + 0 + 0 - re^{r(t-T)} = 0$. $\checkmark$

    **Linear combination**: Let $V(S,t) = aS + be^{r(t-T)}$. Then:

    $$
    \frac{\partial V}{\partial t} = bre^{r(t-T)}, \quad \frac{\partial V}{\partial S} = a, \quad \frac{\partial^2 V}{\partial S^2} = 0
    $$

    Substituting into the PDE:

    $$
    bre^{r(t-T)} + \frac{1}{2}\sigma^2 S^2 \cdot 0 + rS \cdot a - r(aS + be^{r(t-T)})
    $$

    $$
    = bre^{r(t-T)} + raS - raS - rbe^{r(t-T)} = 0 \quad \checkmark
    $$

    **Financial interpretation**: The portfolio $V = aS + be^{r(t-T)}$ represents $a$ shares of the stock plus $b$ units of a zero-coupon bond with face value 1 maturing at time $T$ (since $e^{r(t-T)}$ is the value at time $t$ of receiving \$1 at time $T$). This is a static portfolio of the two fundamental traded assets in the Black-Scholes market. At maturity, the payoff is $aS_T + b$, which is a linear function of the stock price --- a forward-like payoff.

??? success "Solution to Exercise 2"
    In the CRR binomial model, $u = e^{\sigma\sqrt{\Delta t}}$, $d = e^{-\sigma\sqrt{\Delta t}} = 1/u$, and $\Delta t = T/n$.

    After $n$ steps, if the stock moves up $k$ times and down $n-k$ times:

    $$
    S_T = S_0 u^k d^{n-k} = S_0 \exp\!\left[(2k - n)\sigma\sqrt{\Delta t}\right]
    $$

    Under the risk-neutral measure, $k \sim \text{Binomial}(n, p)$ where $p = \frac{e^{r\Delta t} - d}{u - d}$.

    Define $Y_n = 2k - n = \sum_{i=1}^n X_i$ where $X_i = +1$ (up) with probability $p$ or $-1$ (down) with probability $1-p$. Then:

    $$
    \ln(S_T/S_0) = Y_n \cdot \sigma\sqrt{\Delta t}
    $$

    Each $X_i$ has mean $\mathbb{E}[X_i] = 2p - 1$ and variance $\text{Var}(X_i) = 1 - (2p-1)^2 = 4p(1-p)$.

    For small $\Delta t$, expanding $p$:

    $$
    p = \frac{e^{r\Delta t} - e^{-\sigma\sqrt{\Delta t}}}{e^{\sigma\sqrt{\Delta t}} - e^{-\sigma\sqrt{\Delta t}}} \approx \frac{1}{2} + \frac{r - \frac{1}{2}\sigma^2}{2\sigma}\sqrt{\Delta t} + O(\Delta t)
    $$

    Therefore $2p - 1 \approx \frac{(r - \frac{1}{2}\sigma^2)\sqrt{\Delta t}}{\sigma}$ and $4p(1-p) \approx 1$.

    The log-return $\ln(S_T/S_0) = \sigma\sqrt{\Delta t}\sum_{i=1}^n X_i$ has:

    $$
    \text{Mean} = n\sigma\sqrt{\Delta t}(2p - 1) \approx n\sigma\sqrt{\Delta t}\frac{(r - \frac{1}{2}\sigma^2)\sqrt{\Delta t}}{\sigma} = (r - \tfrac{1}{2}\sigma^2)T
    $$

    $$
    \text{Variance} = n\sigma^2\Delta t \cdot 4p(1-p) \approx n\sigma^2\Delta t = \sigma^2 T
    $$

    By the central limit theorem, as $n \to \infty$:

    $$
    \ln(S_T/S_0) \xrightarrow{d} \mathcal{N}\!\left((r - \tfrac{1}{2}\sigma^2)T, \sigma^2 T\right)
    $$

    which is exactly the distribution of $\ln(S_T/S_0)$ under the risk-neutral measure in the Black-Scholes model. $\square$

??? success "Solution to Exercise 3"
    Suppose two investors, Alice and Bob, agree on $\sigma$ but disagree on $\mu$: Alice believes $\mu = \mu_A$ and Bob believes $\mu = \mu_B$ with $\mu_A \neq \mu_B$.

    Both observe the same market: the stock at price $S_0$, the bond earning rate $r$, and the option. Both agree on the hedging strategy because delta depends only on $(S, t, K, T, r, \sigma)$, not on $\mu$.

    Suppose the option is trading at some price $C^*$. Both investors can construct the replicating portfolio: hold $\Delta = \frac{\partial V}{\partial S}$ shares and invest the remainder in bonds, rebalancing continuously. The cost of this replicating strategy is $C_{\text{BS}}$, which depends on $(S_0, K, T, r, \sigma)$ only.

    If $C^* > C_{\text{BS}}$, both investors can sell the option at $C^*$, buy the replicating portfolio for $C_{\text{BS}}$, and pocket $C^* - C_{\text{BS}} > 0$ as a riskless profit (since the replicating portfolio exactly offsets the option at maturity). If $C^* < C_{\text{BS}}$, both reverse the trade.

    Since both investors agree that the replication cost is $C_{\text{BS}}$ (which is independent of $\mu$), and both reject arbitrage, they must agree that the fair option price is $C^* = C_{\text{BS}}$. The parameter $\mu$ enters neither the hedging strategy nor the replication cost, so disagreement about $\mu$ is irrelevant to the option price.

??? success "Solution to Exercise 4"
    The Black-Scholes PDE is:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    This is a second-order linear PDE in the variables $(S, t)$. To classify it, examine the principal part (the highest-order terms). Under the change of variable $x = \ln S$, the PDE transforms to one with constant coefficients, and the principal part becomes $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial x^2}$.

    For a second-order PDE $a V_{tt} + 2b V_{tx} + c V_{xx} + \text{lower order} = 0$, the classification depends on the discriminant $b^2 - ac$. In our case (with $t$ as one variable and $x = \ln S$ as the other), the PDE has no $V_{tt}$ term, so $a = 0$, $b = 0$, $c = \frac{1}{2}\sigma^2$.

    The discriminant is $b^2 - ac = 0 - 0 = 0$, which classifies the PDE as **parabolic**.

    **Financial significance**: Parabolic PDEs describe diffusion processes --- the same class as the heat equation $u_t = \kappa u_{xx}$. In fact, the Black-Scholes PDE can be transformed into the heat equation by a suitable change of variables. Parabolic equations propagate information in one direction (backward in time from the terminal condition), which is exactly what derivative pricing requires: given the known payoff at maturity $T$, we solve backward to find the current price. The parabolic character also ensures well-posedness: given appropriate boundary and terminal conditions, the solution exists and is unique, which guarantees a unique arbitrage-free price.

??? success "Solution to Exercise 5"
    Both options are European calls on the same underlying with the same strike $K = 100$. The key parameters are $S_0 = 100$, $\sigma = 30\%$, $r = 5\%$.

    The option with $T = 2$ has a **higher price** than the option with $T = 0.5$. There are several reasons:

    1. **Time value of money**: A longer-dated option has a lower present value of the strike payment $Ke^{-rT}$. For $T = 0.5$: $Ke^{-0.025} = 97.53$. For $T = 2$: $Ke^{-0.10} = 90.48$. The reduced effective cost of exercise increases the call value.

    2. **More uncertainty**: With longer time to maturity, the stock price has more time to diffuse, creating a wider distribution of possible outcomes. Since a call option benefits from upside movements (which are unlimited) but has limited downside (the payoff is floored at zero), greater dispersion increases the call value.

    3. **Formal bound**: For European calls on non-dividend-paying stocks, $C \geq S_0 - Ke^{-rT}$. This lower bound is $100 - 97.53 = 2.47$ for the short-dated option and $100 - 90.48 = 9.52$ for the long-dated option.

    4. **Monotonicity in $T$**: For a European call on a non-dividend-paying stock, the Black-Scholes price is strictly increasing in $T$ (theta of a European call is negative, meaning value decreases as time passes, equivalently value is higher when more time remains). This follows because both $d_1$ and the discounting effect work in favor of longer maturities.

??? success "Solution to Exercise 6"
    **1. American put option**:

    The standard Black-Scholes model provides closed-form pricing only for European options. An American put can be exercised at any time $t \leq T$, creating a **free boundary problem**: the exercise boundary $S^*(t)$ (below which early exercise is optimal) must be determined as part of the solution. The Black-Scholes PDE holds only in the continuation region $S > S^*(t)$, with the constraint $V \geq (K - S)^+$ everywhere.

    **Method**: Finite difference methods (Crank-Nicolson scheme) applied to the Black-Scholes PDE with the early exercise constraint, or the binomial tree method with backward induction checking for optimal exercise at each node.

    **2. Asian option** (arithmetic average):

    An Asian option with payoff $(\frac{1}{T}\int_0^T S_t\,dt - K)^+$ depends on the entire price path through the running average. The Black-Scholes framework assumes the option price depends only on $(S_t, t)$, but the Asian payoff introduces an additional state variable (the running average), and the arithmetic average of log-normal variables is not log-normal, so no closed-form solution exists.

    **Method**: Monte Carlo simulation under the risk-neutral measure, or PDE methods with an augmented state space including the running average as a second spatial variable.

    **3. Options on assets with stochastic volatility**:

    If the true volatility is random (e.g., following its own diffusion process as in the Heston model), the market has two sources of randomness (stock price and volatility) but only one traded risky asset. The market is **incomplete**: not every payoff can be replicated, and the risk-neutral measure is no longer unique. The constant-$\sigma$ Black-Scholes formula cannot account for the volatility risk premium.

    **Method**: The Heston stochastic volatility model $dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW_t^{(2)}$ admits a semi-analytical pricing formula via characteristic functions and Fourier inversion, allowing efficient computation of European option prices that account for stochastic volatility.
