# Limitations and Extensions of the Black-Scholes Model


While the Black-Scholes model provides an elegant framework for option pricing, its simplifying assumptions often **do not fully hold in practice**. Real markets exhibit volatility clustering, jumps, transaction costs, and other phenomena not captured by the standard model.

This section examines the gap between Black-Scholes assumptions and market reality, and surveys extensions that address these limitations.

---

## Reality vs. Assumptions: Where the Model Fails


The following table summarizes the main discrepancies between Black-Scholes assumptions and empirical evidence:

| Assumption | Model Says | Reality Shows | Observable Evidence |
|------------|------------|---------------|---------------------|
| Constant $\sigma$ | Volatility is constant | Volatility varies over time and with price | Volatility smiles, GARCH effects |
| Continuous paths | No jumps in prices | Large price discontinuities occur | Flash crashes, earnings announcements |
| Frictionless | No transaction costs | Spreads and fees exist | Bid-ask spreads of 0.01%-0.5% |
| Continuous trading | Trade at any instant | Markets close; discrete rebalancing | Overnight gaps, weekend risk |
| Constant $r$ | Risk-free rate fixed | Interest rates fluctuate | Central bank policy changes |
| No dividends | No cash payments | Most stocks pay dividends | Quarterly dividend distributions |
| Gaussian returns | Normal distribution | Fat tails (excess kurtosis) | Black Monday (1987), 2008 crisis |

We now examine each discrepancy in detail and present modeling solutions.

---

## Limitation 1: Constant Volatility


### 1. **What Black-Scholes Assumes**


✅ Volatility $\sigma$ is constant over the option's life and across all strike prices.

### 2. **What Reality Shows**


❌ **Empirical violations**:

**1. Volatility smile/smirk**: Implied volatility varies with strike $K$

- Low strikes (OTM puts): Higher implied volatility
- High strikes (OTM calls): Lower implied volatility
- ATM options: Typically lowest implied volatility

**2. Term structure**: Implied volatility varies with maturity $T$

- Short-term: Often more volatile
- Long-term: Mean-reverting to long-run average

**3. Volatility clustering**: Historical volatility is autocorrelated

- High volatility periods persist (GARCH effects)
- Calm periods also cluster
- "Volatility is stochastic, not constant"

**4. Leverage effect**: Volatility increases when stock prices fall

- Negative correlation between returns and volatility changes
- Asymmetric response to up/down moves

### 3. **Market Evidence**


**Volatility smile example** (S&P 500 options):
```
Strike/Spot   Implied Vol
0.90          28%
0.95          24%
1.00 (ATM)    20%
1.05          22%
1.10          24%
```

The "smile" shape contradicts constant $\sigma$.

### 4. **Modeling Extensions**


🔧 **Extension 1: Stochastic Volatility Models**

Allow volatility itself to be random:

**Heston model** (1993):

$$
\begin{aligned}
dS_t &= rS_t dt + \sqrt{v_t} S_t dW_t^S \\
dv_t &= \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW_t^v
\end{aligned}
$$

where:

- $v_t$ = instantaneous variance (stochastic)
- $\kappa$ = mean-reversion speed
- $\theta$ = long-run variance
- $\xi$ = volatility of volatility
- $\text{Corr}(dW_t^S, dW_t^v) = \rho$ (leverage effect)

**Features**:

- Captures volatility smiles
- Allows mean-reversion
- Incorporates leverage effect via correlation $\rho < 0$
- Requires numerical solutions (no closed form for vanilla options, though semi-closed form exists)

**Other stochastic vol models**:

- **SABR model**: Popular for interest rate derivatives
- **3/2 model**: $dv_t = \kappa(\theta - v_t)dt + \xi v_t^{3/2} dW_t^v$
- **Rough volatility models**: Recent development using fractional Brownian motion

🔧 **Extension 2: Local Volatility Models**

Make volatility a **deterministic function** of price and time:

**Dupire model** (1994):

$$
\sigma = \sigma(S, t)
$$

**Key equation (Dupire's formula)**:

$$
\sigma^2(K, T) = \frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}}
$$

where $C(K,T)$ is the market price of call option with strike $K$ and maturity $T$.

**Features**:

- Calibrates exactly to observed volatility surface
- Deterministic (easier to implement than stochastic vol)
- Still uses PDE framework
- Forward volatility may not match market expectations

🔧 **Extension 3: Implied Volatility Surface**

**Practitioner approach**:

- Interpolate/extrapolate implied volatilities across strikes and maturities
- Use Black-Scholes formula with strike/maturity-dependent $\sigma_{imp}(K,T)$
- No internal consistency (arbitrage-free not guaranteed)
- Simple and widely used for vanilla options

---

## Limitation 2: Continuous Paths (No Jumps)


### 1. **What Black-Scholes Assumes**


✅ Asset prices evolve continuously with no discontinuous jumps.

### 2. **What Reality Shows**


❌ **Empirical violations**:

**1. Price jumps**: Large, sudden price changes occur

- Earnings announcements (can move stock ±10% instantly)
- News events (geopolitical shocks, Fed announcements)
- Market crashes (Black Monday 1987: -22% in one day)

**2. Fat tails**: Return distribution has excess kurtosis

- Extreme events more frequent than normal distribution predicts
- "Five-sigma" events occur more often than expected

**3. Asymmetric jumps**: Crashes more severe than rallies

- Downward jumps larger and more common
- Tail risk asymmetry

### 3. **Market Evidence**


**Kurtosis of S&P 500 daily returns**: ~6-8 (normal distribution has kurtosis = 3)

**Frequency of large moves**: 

- Theory (normal): Prob(|return| > 4%) ≈ 0.003%
- Reality: Occurs ~0.1-0.3% of days (100x more frequent)

### 4. **Modeling Extensions**


🔧 **Extension: Jump-Diffusion Models**

Add a jump component to the price process:

**Merton model** (1976):

$$
dS_t = \mu S_t dt + \sigma S_t dW_t + S_t dJ_t
$$

where:

- $J_t$ = compound Poisson process (jump process)
- $\lambda$ = jump intensity (average number of jumps per year)
- Jump size $Y \sim \mathcal{N}(\mu_J, \sigma_J^2)$ (log-normal)

**Full dynamics**:

$$
S_t = S_0 \exp\left((\mu - \frac{1}{2}\sigma^2)t + \sigma W_t + \sum_{i=1}^{N_t} Y_i\right)
$$

where $N_t \sim \text{Poisson}(\lambda t)$.

**Option pricing**:

$$
C = \sum_{n=0}^\infty \frac{e^{-\lambda' T}(\lambda' T)^n}{n!} C_{BS}(S, K, T, r, \sigma_n)
$$

where:

- $\lambda' = \lambda(1 + \mu_J e^{\sigma_J^2/2})$ (risk-neutral jump intensity)
- $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$ (conditional volatility given $n$ jumps)

**Features**:

- Captures fat tails and skewness
- Semi-closed form solution (sum of Black-Scholes terms)
- Can model crash risk via negative $\mu_J$

**Other jump models**:

- **Kou model**: Double exponential jump distribution (different upward/downward intensities)
- **Variance gamma**: Pure jump process (infinite activity)
- **CGMY model**: Lévy process with flexible tail behavior

---

## Limitation 3: Frictionless Markets and Continuous Trading


### 1. **What Black-Scholes Assumes**


✅ **Frictionless**: No transaction costs, bid-ask spreads, or market impact  
✅ **Continuous**: Can trade at any instant

### 2. **What Reality Shows**


❌ **Empirical violations**:

**Transaction costs**:

- Bid-ask spreads: 0.01%-0.1% for liquid stocks, 0.5%-2% for illiquid
- Commission fees: \$0-10 per trade (varies by broker)
- Market impact: Large trades move prices

**Discrete trading**:

- Markets closed overnight, weekends, holidays
- Hedging occurs at discrete intervals (minutes, hours, days)
- Overnight gap risk cannot be hedged

**Liquidity constraints**:

- Short-sale restrictions or costs
- Position limits for large traders
- Margin requirements

### 3. **Modeling Extensions**


🔧 **Extension 1: Transaction Cost Models**

**Leland model** (1985):

Adjust volatility to account for discrete hedging with proportional transaction cost $k$:

$$
\sigma_{adj} = \sigma\sqrt{1 + \sqrt{\frac{2}{\pi}} \frac{k}{\sigma\sqrt{\Delta t}}}
$$

where $\Delta t$ = rehedging interval.

**Effect**: Higher effective volatility → higher option value (seller compensation for hedging costs)

**Hoggard-Whalley-Wilmott model**:

- Optimal hedging strategy balances transaction costs vs. hedging error
- Creates a "no-transaction band" around delta-neutral position
- Option value includes expected hedging costs

🔧 **Extension 2: Utility-Based Pricing**

In incomplete markets (with frictions), derive prices from investor preferences:

$$
V = \arg\min_{V} \mathbb{E}[U(\text{Wealth})]
$$

where $U$ is utility function.

**Features**:

- No unique price (depends on risk aversion)
- Bid-ask bounds emerge naturally
- Captures indifference pricing

---

## Limitation 4: Constant Risk-Free Rate


### 1. **What Black-Scholes Assumes**


✅ Risk-free rate $r$ is constant over time.

### 2. **What Reality Shows**


❌ **Empirical violations**:

**Interest rate changes**:

- Central banks adjust policy rates (Fed funds rate varied 0%-5.5% in 2022-2023)
- Yield curve shifts and rotates
- Term structure of rates: different maturities have different rates

**Uncertainty**:

- Future rates are stochastic, not deterministic
- Interest rate derivatives exist precisely because $r$ is random

### 3. **Market Evidence**


**US Treasury yield curve** (example from 2023):
```
Maturity    Yield
3-month     5.2%
2-year      4.8%
10-year     4.3%
30-year     4.5%
```

Clearly not a single constant $r$.

### 4. **Modeling Extensions**


🔧 **Extension 1: Deterministic $r(t)$**

Use time-dependent but deterministic risk-free rate:

$$
r = r(t)
$$

**Implementation**: Replace $e^{-rT}$ with $\exp\left(-\int_0^T r(s)ds\right)$ in formulas.

**Data source**: Bootstrapped from market yield curve.

🔧 **Extension 2: Stochastic Interest Rate Models**

Model interest rates as random:

**Vasicek model** (1977):

$$
dr_t = \kappa(\theta - r_t)dt + \sigma_r dW_t^r
$$

**Cox-Ingersoll-Ross (CIR) model** (1985):

$$
dr_t = \kappa(\theta - r_t)dt + \sigma_r\sqrt{r_t} dW_t^r
$$

**Features**:

- Mean-reverting (rates pulled toward $\theta$)
- CIR ensures $r_t \geq 0$ (unlike Vasicek)
- Used for interest rate derivatives

**Joint equity-interest rate models**:
Combine stock price dynamics with stochastic rates for long-dated equity options.

---

## Limitation 5: No Dividends


### 1. **What Black-Scholes Assumes**


✅ No dividends paid during option life.

### 2. **What Reality Shows**


❌ **Empirical violations**:

**Most stocks pay dividends**:

- S&P 500 average yield: ~2%
- Mature companies: 3%-5% yields
- Quarterly payments

**Price discontinuity**:

- Stock price drops by dividend amount on ex-dividend date
- Creates jump in price path

### 3. **Modeling Extensions**


🔧 **Extension 1: Continuous Dividend Yield**

Replace drift $r$ with $r - q$ where $q$ = dividend yield:

$$
dS_t = (r - q)S_t dt + \sigma S_t dW_t
$$

**Black-Scholes formula adjustment**:

$$
C = Se^{-qT}\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

with:

$$
d_1 = \frac{\ln(S/K) + (r - q + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

**Application**: Foreign exchange (treat foreign interest rate as dividend yield).

🔧 **Extension 2: Discrete Dividends**

**Known dividends** $D_1, D_2, \ldots$ at times $t_1, t_2, \ldots$:

**Method 1**: Subtract PV of dividends from stock price:

$$
S' = S - \sum_{i:t_i < T} D_i e^{-r(t_i - t)}
$$

Use $S'$ in Black-Scholes formula.

**Method 2**: Escrowed dividend model (binomial tree with dividend nodes).

**Method 3**: Roll-Geske-Whaley formula (closed form for one dividend).

---

## Limitation 6: No Arbitrage


### 1. **What Black-Scholes Assumes**


✅ No arbitrage opportunities exist.

### 2. **What Reality Shows**


❌ **Empirical violations**:

**Arbitrage does appear temporarily**:

- **2008 crisis**: Basis trades (cash-futures) dislocated
- **Flash crashes**: Temporary mispricings
- **Convertible bonds**: Persistent arbitrage due to illiquidity

**Limits to arbitrage**:

- **Capital constraints**: Arbitrageurs can't deploy infinite capital
- **Margin requirements**: Regulators limit leverage
- **Short-sale restrictions**: Borrowing stocks can be costly or impossible
- **Execution risk**: Trades may not execute at expected prices

### 3. **Modeling Extensions**


🔧 **Extension: Incomplete Markets**

When perfect replication is impossible:

**Pricing bounds**:

$$
C_{lower} \leq C \leq C_{upper}
$$

Instead of unique price, derive **bid-ask bounds**.

**Super-replication**:

- Upper bound: cheapest super-hedging portfolio (always covers payoff)
- Lower bound: most expensive sub-hedging portfolio (always below payoff)

**Utility indifference pricing**:

- Price depends on investor's risk preferences
- Different agents quote different prices

---

## Summary of Extensions


| Limitation | Extension Model | Key Feature | Complexity |
|------------|----------------|-------------|------------|
| Constant $\sigma$ | **Heston** | Stochastic volatility with mean-reversion | Semi-analytical |
| Constant $\sigma$ | **Dupire** | Local volatility $\sigma(S,t)$ | Calibration to surface |
| Continuous paths | **Merton jump** | Adds Poisson jumps | Semi-analytical |
| Continuous paths | **Kou / Variance Gamma** | More flexible jump distributions | Numerical |
| Frictionless | **Leland** | Transaction cost adjustment | Analytical adjustment |
| Constant $r$ | **Vasicek / CIR** | Stochastic interest rates | Analytical (bonds) |
| No dividends | **Continuous yield** | Replace $r$ with $r - q$ | Closed form |
| No dividends | **Discrete dividends** | Subtract PV from stock price | Adjustment |
| No arbitrage | **Incomplete markets** | Super-replication bounds | Optimization |

---

## Practical Implications


### 1. **When Black-Scholes is Sufficient**


The standard model works reasonably well for:

- **Liquid European options** on major indices/stocks
- **Short maturities** (< 3 months)
- **Near ATM strikes** where smile is less pronounced
- **Quick approximations** and benchmarking
- **Implied volatility** extraction

### 2. **When Extensions are Needed**


Use more sophisticated models for:

- **Long-dated options** (volatility and rates vary significantly)
- **Deep OTM options** (smile/skew effects dominate)
- **Exotic options** (path-dependent, barriers, etc.)
- **Earnings events** (jump risk)
- **Structured products** (multiple risk factors)
- **Risk management** (capturing all Greeks accurately)

### 3. **Model Selection Hierarchy**


**Level 1** (Simple): Black-Scholes with strike-dependent implied vol  
**Level 2** (Intermediate): Local volatility or jump-diffusion  
**Level 3** (Advanced): Stochastic volatility (Heston, SABR)  
**Level 4** (Research): Rough volatility, multi-factor models  

**Trade-off**: Complexity vs. calibration stability vs. computational cost.

---

## The Role of Black-Scholes Today


### 1. **Still Relevant Despite Limitations**


**1. Benchmark and baseline**: Universal language for option pricing

**2. Implied volatility**: Market standard for quoting options

- "Trade vol, not price"
- Volatility surface is the primary market observable

**3. Greeks framework**: Risk management foundation

- Delta, gamma, vega, theta, rho
- Sensitivities guide hedging strategies

**4. Teaching tool**: Introduction to derivative pricing

- Builds intuition for no-arbitrage
- Foundation for more complex models

### 2. **Modern Usage Pattern**


**Vanilla options**:

- Price using Black-Scholes with **strike-dependent implied volatility**
- Calibrate $\sigma(K, T)$ surface from market data
- Interpolate for unmaintained strikes/maturities

**Exotic options**:

- Use **stochastic volatility** or **local volatility** models
- Calibrate to vanilla surface
- Price exotics consistently

**Risk management**:

- Compute Greeks using appropriate model
- Stress test across volatility scenarios
- Account for model risk

---

## Summary


Black-Scholes assumptions face numerous real-world violations:

**Main limitations**:

1. **Volatility not constant** → Smiles, clustering, stochastic vol
2. **Jumps exist** → Fat tails, crash risk, earnings shocks
3. **Markets have frictions** → Transaction costs, discrete hedging
4. **Rates vary** → Yield curve, stochastic rates
5. **Dividends paid** → Price discontinuities
6. **Arbitrage constraints** → Incomplete markets, limits to arbitrage

**Extensions address each limitation**:

- **Stochastic vol**: Heston, SABR, rough vol
- **Jumps**: Merton, Kou, variance gamma
- **Frictions**: Leland, optimal hedging
- **Rates**: Vasicek, CIR, HJM
- **Dividends**: Yield adjustments, discrete dividends
- **Incompleteness**: Super-replication, utility pricing

**Practical wisdom**:

- Black-Scholes remains the **industry standard baseline**
- Extensions add complexity but improve realism
- Model choice depends on application and data availability
- **No model is perfect**: All models are wrong, some are useful

The evolution from Black-Scholes to modern models illustrates the progression of quantitative finance—building on elegant foundations while addressing empirical challenges. Understanding both the original model and its extensions is essential for effective derivative pricing and risk management.

---

## Exercises

**Exercise 1.** The S&P 500 implied volatility surface shows a pronounced skew: OTM puts trade at higher implied volatility than OTM calls. Explain why the Black-Scholes assumption of constant volatility is inconsistent with this observation. Which model extension (local volatility, stochastic volatility, or jump-diffusion) would you choose to capture this feature, and why?

??? success "Solution to Exercise 1"
    The Black-Scholes assumption of constant volatility implies that all European options on the same underlying with the same maturity should have the same implied volatility, regardless of strike price. The pronounced skew in S&P 500 options directly contradicts this: OTM puts at lower strikes have implied volatilities of 25-30%, while OTM calls at higher strikes have implied volatilities of 18-20%. If $\sigma$ were constant, the implied volatility surface would be perfectly flat.

    Among the three extensions, **stochastic volatility** (e.g., Heston) is the best choice for capturing the skew. The key reasons are:

    - **Local volatility** can fit the observed skew exactly by construction (via Dupire's formula), but it predicts that the smile will flatten over time (poor dynamics). The forward smile does not match market behavior.
    - **Stochastic volatility** captures the skew through the negative correlation $\rho < 0$ between the stock and volatility processes (leverage effect). When the stock drops, volatility rises, making OTM puts more expensive. Crucially, stochastic volatility produces a smile that **persists** over time, matching empirical observations.
    - **Jump-diffusion** models generate skew through asymmetric downward jumps and are effective for short-maturity smiles, but they do not capture volatility clustering or the term structure of the smile as well as stochastic volatility.

    For a model that captures both the static skew shape and its realistic dynamic behavior, stochastic volatility is preferred.

---


**Exercise 2.** The kurtosis of S&P 500 daily returns is approximately 6-8, compared to 3 for a normal distribution. (a) Explain what excess kurtosis implies about the frequency of extreme events. (b) Show that the Merton jump-diffusion model can produce excess kurtosis by considering the unconditional return distribution as a mixture. (c) Estimate the probability of a 4-standard-deviation move under a normal distribution versus a Merton model with $\lambda = 1$, $\mu_J = -0.05$, $\sigma_J = 0.10$.

??? success "Solution to Exercise 2"
    **(a)** Excess kurtosis (kurtosis greater than 3) means the return distribution has heavier tails than the normal distribution. With kurtosis of 6-8, extreme events (large positive or negative returns) occur far more frequently than a Gaussian model predicts. The distribution has more probability mass in the tails and at the center, with less in the intermediate region. This implies that "five-sigma" or "six-sigma" events, which should be extraordinarily rare under normality, are observed relatively often in financial markets.

    **(b)** In the Merton model, the return over period $[0, T]$ is a mixture:

    $$
    \log(S_T/S_0) = (r - \tfrac{1}{2}\sigma^2 - \lambda\kappa)T + \sigma W_T + \sum_{i=1}^{N_T} \log Y_i
    $$

    Conditioning on $N_T = n$ jumps, the log-return is normal with variance $\sigma^2 T + n\sigma_J^2$. The unconditional distribution is a Poisson mixture of normals:

    $$
    f(x) = \sum_{n=0}^{\infty} \frac{e^{-\lambda T}(\lambda T)^n}{n!} \phi\left(x; \mu_n, \sigma^2 T + n\sigma_J^2\right)
    $$

    A mixture of normals with different variances produces excess kurtosis because the mixture has heavier tails than any single component. The kurtosis of the mixture exceeds 3 because the Poisson-weighted averaging of different variance levels fattens the tails.

    **(c)** Under a normal distribution with $\sigma_{\text{daily}} \approx 0.01$ (1% daily vol), a 4-standard-deviation move ($|r| > 0.04$) has probability $\Pr(|Z| > 4) \approx 6.3 \times 10^{-5}$, or about 0.006% of days (roughly once every 63 years).

    Under the Merton model with $\lambda = 1$ (one jump per year on average), $\mu_J = -0.05$, $\sigma_J = 0.10$, and daily time step $\Delta t = 1/252$: The probability of at least one jump in a day is $\lambda \Delta t \approx 0.004$. When a jump occurs, the additional log-return is $N(-0.05, 0.01)$, contributing roughly $\pm 10\%$ moves. The probability of a 4% move is substantially higher because even a single jump can contribute 5-15% in magnitude. Numerically, the probability of $|r| > 4\%$ under the Merton model is approximately 0.1-0.3%, which is 15-50 times more frequent than the Gaussian prediction.

---


**Exercise 3.** The Leland model adjusts volatility for transaction costs as $\sigma_{\text{adj}} = \sigma\sqrt{1 + \sqrt{2/\pi} \cdot k/(\sigma\sqrt{\Delta t})}$. (a) For $\sigma = 0.20$, $k = 0.005$ (0.5% round-trip cost), and daily rehedging ($\Delta t = 1/252$), compute $\sigma_{\text{adj}}$. (b) Explain why the adjusted volatility is always higher than the true volatility. (c) What happens to $\sigma_{\text{adj}}$ as $\Delta t \to 0$, and what does this imply about continuous hedging with transaction costs?

??? success "Solution to Exercise 3"
    **(a)** With $\sigma = 0.20$, $k = 0.005$, and $\Delta t = 1/252$:

    $$
    \frac{k}{\sigma\sqrt{\Delta t}} = \frac{0.005}{0.20 \times \sqrt{1/252}} = \frac{0.005}{0.20 \times 0.06299} = \frac{0.005}{0.01260} \approx 0.3968
    $$

    $$
    \sqrt{\frac{2}{\pi}} \approx 0.7979
    $$

    $$
    \sigma_{\text{adj}} = 0.20\sqrt{1 + 0.7979 \times 0.3968} = 0.20\sqrt{1 + 0.3166} = 0.20\sqrt{1.3166} = 0.20 \times 1.1475 \approx 0.2295
    $$

    The adjusted volatility is approximately 22.95%, compared to the true volatility of 20%.

    **(b)** The adjusted volatility is always higher because $\sigma_{\text{adj}} = \sigma\sqrt{1 + \text{positive term}}$. The term $\sqrt{2/\pi} \cdot k/(\sigma\sqrt{\Delta t})$ is strictly positive for any $k > 0$ and finite $\Delta t$, so $\sigma_{\text{adj}} > \sigma$ always. Financially, the option seller must charge more to compensate for the transaction costs incurred during delta hedging. Each rebalance costs $k$ times the notional traded, and this accumulated cost is reflected as a higher effective volatility.

    **(c)** As $\Delta t \to 0$ (continuous hedging):

    $$
    \frac{k}{\sigma\sqrt{\Delta t}} \to \infty
    $$

    so $\sigma_{\text{adj}} \to \infty$. This means the total transaction costs explode when hedging continuously with proportional costs. Continuous rebalancing requires infinitely many trades, each incurring a cost, and the total cost diverges. This is a fundamental result: the Black-Scholes perfect hedging strategy, which requires continuous trading, is not feasible in the presence of transaction costs. In practice, one must hedge at discrete intervals, accepting some hedging error to keep transaction costs finite.

---


**Exercise 4.** Explain why the Black-Scholes model remains the industry standard despite its well-documented limitations. Discuss at least three specific roles the model plays in modern practice (e.g., quoting conventions, benchmarking, risk management) that do not require the model to be "correct."

??? success "Solution to Exercise 4"
    Despite its well-documented limitations, Black-Scholes remains the industry standard for several reasons:

    **1. Quoting convention (implied volatility)**: Options are quoted in terms of Black-Scholes implied volatility rather than price. Traders say "the 100-strike call trades at 22 vol" rather than quoting a dollar price. This convention is universal across exchanges, brokers, and asset classes. The implied volatility is a normalized, unit-free measure that allows comparison across strikes, maturities, and underlyings. The model does not need to be "correct" for this usage -- it merely serves as a bijective mapping between prices and volatilities.

    **2. Benchmarking and relative value**: Black-Scholes provides a common baseline against which all models and market prices are compared. Traders assess whether an option is "cheap" or "expensive" relative to Black-Scholes. The difference between model prices and market prices reveals information about market expectations (skew, term structure, jump risk). More complex models are evaluated by how much they improve upon the Black-Scholes baseline.

    **3. Risk management (Greeks)**: The Black-Scholes Greeks ($\Delta$, $\Gamma$, $\Theta$, $\mathcal{V}$, $\rho$) provide the foundational language for risk management. Even when traders use more sophisticated models, they often translate risk sensitivities into Black-Scholes equivalent Greeks. The simple, intuitive relationships (e.g., delta hedging, gamma scalping, theta decay) provide actionable hedging guidance. The Greeks framework extends naturally to more complex models but originated with Black-Scholes.

    **Additional roles**: Black-Scholes also serves as a teaching tool that builds intuition for no-arbitrage pricing, risk-neutral valuation, and dynamic replication. Its closed-form solution allows rapid computation for real-time trading and is used for back-of-the-envelope calculations. Regulatory frameworks often reference Black-Scholes or its Greeks for margin requirements and capital calculations.

---


**Exercise 5.** For a European call with $S_0 = 100$, $K = 90$ (deep ITM), $T = 0.25$ (3 months), the market implied volatility is 25%, while for $K = 110$ (deep OTM) it is 22%. (a) Compute the Black-Scholes prices using each implied volatility. (b) Explain the "model selection hierarchy" from Level 1 (BS with strike-dependent implied vol) to Level 3 (stochastic volatility). (c) For which applications does Level 1 suffice, and when must one move to Level 3?

??? success "Solution to Exercise 5"
    **(a)** Using $r = 0.05$, $T = 0.25$, and $S_0 = 100$:

    For $K = 90$ with $\sigma = 0.25$:

    $$
    d_1 = \frac{\ln(100/90) + (0.05 + 0.5 \times 0.0625) \times 0.25}{0.25\sqrt{0.25}} = \frac{0.10536 + 0.02031}{0.125} = \frac{0.12567}{0.125} \approx 1.0054
    $$

    $$
    d_2 = 1.0054 - 0.125 = 0.8804
    $$

    $$
    C_{90} = 100 \times \mathcal{N}(1.0054) - 90 \times e^{-0.0125} \times \mathcal{N}(0.8804)
    $$

    $$
    C_{90} \approx 100 \times 0.8426 - 88.882 \times 0.8107 \approx 84.26 - 72.06 \approx 12.20
    $$

    For $K = 110$ with $\sigma = 0.22$:

    $$
    d_1 = \frac{\ln(100/110) + (0.05 + 0.5 \times 0.0484) \times 0.25}{0.22\sqrt{0.25}} = \frac{-0.09531 + 0.01855}{0.11} = \frac{-0.07676}{0.11} \approx -0.6978
    $$

    $$
    d_2 = -0.6978 - 0.11 = -0.8078
    $$

    $$
    C_{110} = 100 \times \mathcal{N}(-0.6978) - 110 \times e^{-0.0125} \times \mathcal{N}(-0.8078)
    $$

    $$
    C_{110} \approx 100 \times 0.2427 - 108.633 \times 0.2096 \approx 24.27 - 22.77 \approx 1.50
    $$

    **(b)** The model selection hierarchy:

    - **Level 1 (BS with strike-dependent implied vol)**: Use a different $\sigma_{\text{imp}}(K, T)$ for each option. The model is internally inconsistent (no single process generates these prices), but it matches market quotes exactly. Simple, fast, and widely used for vanilla pricing and quoting.
    - **Level 2 (Local volatility or jump-diffusion)**: Use a single consistent model with $\sigma_{\text{loc}}(t, S)$ or jumps. Calibrate to the vanilla surface. Provides a coherent framework for pricing exotics, but local vol has poor dynamics and jump-diffusion may miss long-term features.
    - **Level 3 (Stochastic volatility)**: Use Heston, SABR, or similar models. Captures realistic smile dynamics (persistence, leverage effect), produces better hedging strategies, and gives more reliable exotic prices.

    **(c)** Level 1 suffices for quoting and trading vanilla options, real-time risk monitoring, and quick pricing. One must move to Level 3 for pricing path-dependent exotics (barriers, cliquets, forward-starting options), computing accurate hedging ratios that account for smile dynamics, and any application where forward volatility or smile evolution matters.

---


**Exercise 6.** In the Heston stochastic volatility model, the correlation $\rho$ between the stock and variance Brownian motions is typically negative for equities ($\rho \approx -0.7$). Explain the economic mechanism (leverage effect) behind this negative correlation, and describe how it produces a volatility skew in implied volatility. What would the implied volatility surface look like if $\rho = 0$?

??? success "Solution to Exercise 6"
    The **leverage effect** refers to the economic mechanism linking stock price declines to volatility increases. Two main explanations exist:

    **Financial leverage**: When a firm's stock price drops, its debt-to-equity ratio increases (debt is relatively fixed), making the firm more leveraged. Higher leverage means the equity is riskier, so its volatility increases. Conversely, stock price increases reduce leverage and lower volatility.

    **Behavioral/feedback**: When markets fall, fear and uncertainty rise, prompting increased hedging activity (buying puts, selling stocks), which further increases realized and implied volatility. This feedback loop reinforces the negative correlation.

    In the Heston model, $\rho < 0$ encodes this relationship. When $dW^{(1)} < 0$ (stock falls), the correlated increment $dW^{(2)}$ tends to be negative as well, but since $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$ has $\xi > 0$, a correlated negative $dW^{(2)}$ pushes $v_t$ upward (recalling that $W^{(2)}$ enters with a positive coefficient). Actually, let us be precise: with $\rho < 0$, when $dW^{(1)} < 0$, we have $dW^{(2)}$ tending to have the same sign as $\rho \cdot dW^{(1)}$, i.e., positive when $\rho < 0$ and $dW^{(1)} < 0$. This means $v_t$ increases when $S_t$ decreases.

    **How this produces skew**: For OTM puts (low $K$), reaching the strike requires the stock to fall. But when the stock falls, volatility rises (due to $\rho < 0$), making the fall even more likely. This positive feedback inflates the value of OTM puts, raising their implied volatility. For OTM calls (high $K$), reaching the strike requires the stock to rise, which decreases volatility (due to $\rho < 0$), making large upward moves less likely. This depresses OTM call values and their implied volatilities. The result is a downward-sloping implied volatility curve: higher implied vol at low strikes, lower at high strikes -- the classic equity skew.

    **If $\rho = 0$**: Stock and volatility movements would be independent. Volatility would still be stochastic (creating a smile), but increases and decreases in the stock would be equally likely to coincide with high or low volatility. The implied volatility surface would show a **symmetric smile** (convex in strike, centered at ATM) rather than a skew. There would be no preferential increase in implied vol for low strikes versus high strikes.
