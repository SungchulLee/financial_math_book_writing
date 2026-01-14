# Black-Scholes Model Assumptions


The Black-Scholes model, while revolutionary in its implications, relies on a set of **simplifying assumptions** that make the mathematics tractable and enable closed-form solutions. Understanding these assumptions is essential for both appreciating the model's elegance and recognizing its practical limitations.

This section systematically examines each assumption, explains its role, and discusses its realism.

---

## The Six Core Assumptions


The Black-Scholes framework rests on six fundamental assumptions about asset price dynamics and market structure.

---

## Assumption 1: Geometric Brownian Motion with Constant Parameters


### 1. **Statement**


The underlying asset price $S_t$ follows **geometric Brownian motion** with constant drift $\mu$ and constant volatility $\sigma$:

$$
\boxed{dS_t = \mu S_t dt + \sigma S_t dW_t}
$$

where:
- $S_t$ = asset price at time $t$
- $\mu$ = constant drift (expected return, annualized)
- $\sigma$ = constant volatility (standard deviation of returns, annualized)
- $W_t$ = standard Brownian motion (Wiener process)

### 2. **Equivalent Representation**


By Itô's lemma, this implies:
$$
S_t = S_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)
$$

Taking logarithms:
$$
\ln(S_t) = \ln(S_0) + \left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t
$$

### 3. **Implications**


**1. Log-normal distribution**: Stock prices are log-normally distributed
$$
\ln(S_t) \sim \mathcal{N}\left(\ln(S_0) + \left(\mu - \frac{1}{2}\sigma^2\right)t, \sigma^2 t\right)
$$

**2. Normal returns**: Continuously compounded returns are normally distributed
$$
\ln\left(\frac{S_t}{S_0}\right) \sim \mathcal{N}\left(\left(\mu - \frac{1}{2}\sigma^2\right)t, \sigma^2 t\right)
$$

**3. Continuity**: Price paths are continuous (no jumps)
$$
\mathbb{P}(\text{jump at any instant}) = 0
$$

**4. Constant parameters**: $\mu$ and $\sigma$ do not change over time or with price level

### 4. **Why This Assumption?**


**Mathematical convenience**:
- Allows analytical solutions via PDE methods
- Log-normality ensures positive prices: $S_t > 0$ always
- Gaussian increments enable straightforward statistical analysis

**Empirical justification** (partial):
- Short-term returns are approximately normal
- Historical volatility can be estimated from data
- Captures essential features of price randomness

**Reality check**:
- Returns have **fatter tails** than normal distribution (kurtosis)
- Volatility is **not constant** (volatility clustering, GARCH effects)
- **Jumps occur** in reality (earnings announcements, news shocks)
- **Leverage effect**: Volatility tends to increase when prices fall

---

## Assumption 2: Frictionless Markets


### 1. **Statement**


The market operates without **transaction costs, bid-ask spreads, or market impact**:
- Buying and selling assets is **costless**
- The same price applies to both purchases and sales (no spread)
- Trading any quantity does not affect prices (perfect liquidity)

### 2. **Implications**


**1. Perfect replication**: Derivative payoffs can be exactly replicated via continuous trading

**2. Arbitrage elimination**: Any mispricing is immediately exploited and corrected

**3. No penalty for frequent trading**: Continuous hedging is feasible without cost accumulation

### 3. **Why This Assumption?**


**Mathematical necessity**:
- Dynamic hedging requires continuous rebalancing
- Transaction costs would accumulate infinitely over infinite adjustments
- Frictionless markets ensure the replicating portfolio equals the option value exactly

**Economic idealization**:
- Competitive markets with many traders approach this limit
- Large institutional traders face minimal transaction costs
- Facilitates no-arbitrage arguments

**Reality check**:
- **Bid-ask spreads exist**: Costs of 0.01%-0.1% for liquid stocks
- **Commission fees**: Though reduced with modern brokers
- **Market impact**: Large trades move prices, especially for illiquid assets
- **Slippage**: Executing at worse prices than expected

**Practical implications**:
- Hedging costs reduce option profits in practice
- Wide spreads for illiquid options create arbitrage bounds
- Transaction cost models extend Black-Scholes (e.g., Leland model)

---

## Assumption 3: Continuous Trading


### 1. **Statement**


Traders can adjust their positions **at any instant in continuous time**:
- Portfolio rebalancing can occur at infinitesimally small time intervals
- There are no restrictions on trading frequency
- Markets are open 24/7 (conceptually)

### 2. **Implications**


**1. Perfect hedging**: Delta can be maintained exactly by continuous adjustment

**2. No discrete-time error**: The discrete hedging error vanishes as $\Delta t \to 0$

**3. Theoretical replication**: Options can be replicated exactly (in theory)

### 3. **Why This Assumption?**


**Mathematical framework**:
- Continuous-time stochastic calculus (Itô calculus) requires continuous trading
- The Black-Scholes PDE derives from instantaneous hedging arguments
- Limits of binomial model as $\Delta t \to 0$ necessitate continuous adjustment

**Economic argument**:
- Modern markets allow very frequent trading (high-frequency trading)
- Approximates reality better than daily or weekly rebalancing assumptions

**Reality check**:
- **Actual trading is discrete**: Even HFT operates on millisecond scales, not continuous
- **Markets close**: Overnight and weekend risk cannot be hedged
- **Asynchronous trading**: Different assets trade at different times
- **Liquidity varies**: Not all assets can be traded at any moment

**Practical implications**:
- **Hedging errors** arise from discrete rebalancing
- **Gamma risk**: Between hedges, delta changes create exposure
- **Gap risk**: Market jumps overnight create unhedgeable losses

---

## Assumption 4: Constant Risk-Free Rate


### 1. **Statement**


The risk-free interest rate $r$ is **constant and known** over the option's life:
- $r$ does not vary with time: $r(t) = r$ for all $t$
- $r$ is non-stochastic (deterministic)
- Borrowing and lending both occur at rate $r$ (no spread)

### 2. **Implications**


**1. Deterministic discounting**: Future cash flows are discounted by $e^{-rT}$

**2. Risk-neutral drift**: Under risk-neutral measure, stock grows at rate $r$:
$$
dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

**3. Simplified PDE**: The $-rV$ term in the Black-Scholes PDE is constant

### 3. **Why This Assumption?**


**Mathematical simplification**:
- Constant $r$ allows separation of discounting from stochastic dynamics
- Time-dependent $r(t)$ would complicate the PDE
- Stochastic interest rates require joint modeling with asset prices

**Practical approximation**:
- For short-dated options (weeks to months), $r$ changes little
- Market-implied risk-free rate can be observed from bonds

**Reality check**:
- **Interest rates change**: Central banks adjust policy rates
- **Term structure matters**: Different maturities have different rates
- **Credit risk**: Actual borrowing rates exceed risk-free rate
- **Negative rates possible**: Post-2008 some central banks went negative

**Extensions**:
- **Time-dependent $r(t)$**: Can be incorporated using $r(t)$ from yield curve
- **Stochastic rates**: Hull-White, CIR models for interest rate derivatives
- **Foreign exchange options**: Two interest rates (domestic and foreign)

### 4. **Practical Implementation: What is $r$ in Practice?**


While the Black-Scholes model assumes a constant risk-free rate, practitioners must choose an appropriate rate from observable market data. The choice depends on the option's maturity, underlying asset, and market conventions.

### 5. **Historical Choice: LIBOR (Deprecated)**


**What it was**:
- **LIBOR** (London Interbank Offered Rate): Rate at which banks borrowed from each other
- Most common benchmark from 1980s-2020s
- Observable, actively traded, reflected short-term borrowing costs

**Why it's gone**:
- Manipulation scandals (2012 LIBOR-rigging scandal)
- Declining transaction volumes (based on estimates, not actual trades)
- Regulatory pressure to phase out
- **Officially discontinued**: December 31, 2021 (most tenors)

### 6. **Modern Benchmark: Overnight Rates**


**Secured Overnight Financing Rate (SOFR)** - United States:
- Based on **actual overnight transactions** in US Treasury repo market
- Secured by US Treasury securities
- Replaced LIBOR as US dollar benchmark
- More transparent and robust than LIBOR
- Published daily by New York Federal Reserve

**Other regional alternatives**:
- **SONIA** (Sterling Overnight Index Average): United Kingdom
- **€STR** (Euro Short-Term Rate): Eurozone
- **SARON** (Swiss Average Rate Overnight): Switzerland
- **TONAR** (Tokyo Overnight Average Rate): Japan

**Advantages**:
- Transaction-based (not survey-based)
- High volume of underlying transactions
- Transparent methodology
- Lower manipulation risk

### 7. **Treasury Yields**


**When used**:
- Long-term options (years to maturity)
- Options on broad market indices (S&P 500, etc.)
- Conservative baseline (truly "risk-free")

**Common choices**:
- **T-bills**: Maturities ≤ 1 year (e.g., 3-month, 6-month)
- **T-notes**: Maturities 2-10 years
- **T-bonds**: Maturities > 10 years

**Advantages**:
- Backed by full faith and credit of US government
- Highly liquid market
- Clear term structure available

**Considerations**:
- Slightly lower than interbank rates (credit spread)
- May not reflect actual funding costs for banks/hedge funds

### 8. **Forward Rate Agreements (FRA) and Swap Rates**


**When used**:
- Medium-term options (months)
- When matching option maturity to specific forward period
- Interest rate derivatives

**FRA (Forward Rate Agreement)**:
- Locks in interest rate for future period
- Reflects market expectations of future rates
- Example: 3x6 FRA = rate for 3-month period starting 3 months from now

**Interest Rate Swaps**:
- Exchange fixed for floating payments
- Swap rate = fixed rate that makes swap value zero
- Reflects average expected future short rates

**Construction**:
- Build **term structure** of forward rates
- Match option maturity to corresponding forward rate
- Accounts for rate expectations over option's life

### 9. **Repo Rates**


**When used**:
- Very short-term options (intraday to weekly)
- High-frequency trading strategies
- When immediate funding costs matter

**What it is**:
- Rate for overnight secured lending using securities as collateral
- Closely tied to Fed policy rate and money market conditions
- Reflects real-time liquidity

**Types**:
- **General Collateral (GC) Repo**: Average rate across all Treasury collateral
- **Special Repo**: Rate for specific security (can deviate from GC)

### 10. **Practical Selection Guide**


| Option Maturity | Recommended Rate | Rationale |
|-----------------|------------------|-----------|
| **Intraday - 1 week** | Repo rate, SOFR | Reflects immediate funding costs |
| **1 week - 3 months** | SOFR, 3-month T-bill | Short-term market rates |
| **3 months - 1 year** | SOFR curve, FRA, T-bill yield | Forward-looking expectations |
| **1 year - 5 years** | Swap rates, T-note yields | Medium-term structure |
| **> 5 years** | Long-dated swap rates, T-bond yields | Long-term rates |

**Equity options**: SOFR or swap curve matching option maturity  
**FX options**: Differential between domestic and foreign rates (e.g., SOFR vs. €STR)  
**Index options**: T-bill/T-note yields matching expiration  

### 11. **Term Structure Matching**


For accuracy, match the risk-free rate to the option's time to maturity:

**Example**: Pricing a 6-month option on December 18, 2025
- **Don't use**: Current overnight SOFR rate (too short)
- **Do use**: 6-month SOFR forward rate or 6-month T-bill yield
- **Rationale**: Reflects borrowing cost over the actual option period

**Interpolation**: If exact maturity not available, interpolate between observed rates
- Linear interpolation for short maturities (< 1 year)
- Spline or polynomial for longer maturities

### 12. **Dividend-Adjusted Rates**


For equity options on dividend-paying stocks, use:
$$
r_{\text{effective}} = r - q
$$

where:
- $r$ = risk-free rate (from above)
- $q$ = continuous dividend yield

The model uses $r_{\text{effective}}$ as the drift rate.

### 13. **Why It Matters**


**Impact on option prices**:
- Call options: Higher $r$ → Higher value (larger forward price)
- Put options: Higher $r$ → Lower value (lower PV of strike)
- **Magnitude**: 1% change in $r$ can affect long-dated option prices by several percent

**Example sensitivity**:
- Option: ATM call, $S = 100$, $K = 100$, $\tau = 1$ year, $\sigma = 20\%$
- At $r = 2\%$: $C \approx 8.92$
- At $r = 5\%$: $C \approx 10.45$
- **Difference**: 17% price change from 3% rate change

**Practical concerns**:
- **Misestimation risk**: Wrong $r$ → systematic pricing errors
- **Hedging implications**: Delta and other Greeks depend on $r$
- **Credit spreads**: Corporate borrowers face $r + \text{spread}$
- **Collateral effects**: Posted collateral may earn different rate

### 14. **Market Conventions**


**Equity options**:
- Use swap curve or interpolated SOFR
- Adjust for dividends if applicable

**FX options**:
- Use interest rate differential: $r_{\text{domestic}} - r_{\text{foreign}}$
- Both rates from respective country benchmarks

**Commodity options**:
- Use SOFR or T-bill rates
- May need storage cost adjustments (convenience yield)

**Interest rate options** (caps, floors, swaptions):
- Use forward rates derived from swap curve
- Internally consistent with underlying rate

### 15. **Dynamic Adjustment**


In practice, $r$ changes over time:
- **Re-mark daily**: Update $r$ based on current market rates
- **Greeks sensitivity**: Rho ($\frac{\partial V}{\partial r}$) measures exposure
- **Hedging**: Interest rate risk can be hedged with bonds or swaps

**Post-2008 consideration**: Banks may face different borrowing rates than SOFR due to credit risk. Some use **OIS (Overnight Index Swap) discounting** for CSA (Credit Support Annex) agreements.

---

## Assumption 5: No Arbitrage


### 1. **Statement**


The market is **arbitrage-free**:
- There exist no riskless profit opportunities
- Any mispricing is immediately exploited by arbitrageurs
- Law of one price holds: identical payoffs have identical prices

### 2. **Implications**


**1. Unique pricing**: Replicable payoffs have a unique price (the replication cost)

**2. Martingale measure exists**: There exists a probability measure $\mathbb{Q}$ under which discounted prices are martingales

**3. PDE derivation**: The hedged portfolio must earn the risk-free rate (no excess return)

### 3. **Why This Assumption?**


**Fundamental principle**:
- No-arbitrage is the **foundation** of quantitative finance
- If arbitrage existed, infinite profit is possible (unrealistic)
- Competitive markets eliminate arbitrage quickly

**Theoretical necessity**:
- Black-Scholes derivation relies on replication and no-arbitrage
- Unique option price follows from uniqueness of replication cost

**Reality check**:
- **Usually holds**: In liquid markets, arbitrage is quickly eliminated
- **Violations occur**: During crises, market dislocations, or illiquidity
- **Limits to arbitrage**: Capital constraints, short-sale restrictions, counterparty risk
- **Model arbitrage**: Mis-specified models can create apparent arbitrage

**Examples of violations**:
- **2008 financial crisis**: Basis trade breakdowns (cash vs. futures)
- **Flash crashes**: Temporary mispricings
- **Emerging markets**: Capital controls prevent arbitrage
- **Convertible bonds**: Persistent mispricings due to illiquidity

**Fundamental Theorem of Asset Pricing (FTAP)**:
- No arbitrage ⟺ Equivalent martingale measure exists
- Completeness + No arbitrage ⟺ Unique martingale measure
- See Section 2.2 for rigorous treatment

---

## Assumption 6: No Dividends


### 1. **Statement**


The underlying asset pays **no dividends or cash distributions** during the option's life:
- No dividend payments before maturity $T$
- No stock splits, special dividends, or return of capital
- All return comes from price appreciation

### 2. **Implications**


**1. Simplified PDE**: No dividend term in the Black-Scholes equation

**2. Early exercise**: American calls are never exercised early (for non-dividend stocks)

**3. Put-call parity**: Simpler form without dividend adjustments

### 3. **Why This Assumption?**


**Mathematical simplicity**:
- Dividends create discontinuities in price dynamics
- Removes complications from the basic derivation

**Applicability**:
- Some stocks (growth stocks, tech firms) pay no dividends
- Short-dated options may avoid dividend dates

**Reality check**:
- **Many stocks pay dividends**: S&P 500 stocks average ~2% yield
- **Ex-dividend price drops**: Stock falls by dividend amount on ex-date
- **Strategic exercise**: American calls may be exercised just before dividends

### 4. **Theoretical Discussion: The Dividend-Adjusted Model**


In many realistic financial markets, the assumption of zero dividends is overly restrictive. Stocks, particularly those of established companies, often pay dividends at regular intervals. Incorporating a continuous dividend yield into the Black-Scholes framework makes the model more applicable to real-world financial instruments.

### 5. **Why Non-Zero Dividends Make Sense**


The rationale for introducing a non-zero dividend yield $q$ stems from the fact that **dividends reduce the value of the underlying asset over time**. When a stock pays dividends, the expected return to investors comes not only from capital appreciation but also from dividend payments. This introduces an opportunity cost for holding the underlying asset rather than selling it to capture the dividend.

**Key motivations for including dividend yield**:

**1. Stock price adjustment**:
- When a stock pays dividends, its price typically drops by the dividend amount on the ex-dividend date
- This directly affects the payoff of options written on the stock
- Ignoring dividends leads to systematic mispricing

**2. Hedging adjustment**:
- The value of a hedge must account for lost dividends on the underlying stock
- Alters the construction of a risk-free portfolio
- The replicating portfolio must be adjusted for dividend flows

**3. Market practice**:
- Options on dividend-paying stocks are typically priced using dividend-adjusted models
- Market makers incorporate expected dividends into pricing
- Failing to adjust creates arbitrage opportunities

**Modified price dynamics**:

When dividends are incorporated as a continuous yield $q$, the underlying price process becomes:

$$
\boxed{dS_t = (\mu - q) S_t dt + \sigma S_t dW_t}
$$

**Interpretation**:
- The dividend yield acts as a **negative drift term**
- Stockholders receive a portion of total return through dividends rather than price appreciation
- The asset's capital gains rate is $\mu - q$ instead of $\mu$

**Modified Black-Scholes PDE**:

From the hedging perspective, an option holder is exposed to the dividend-adjusted growth rate $(\mu - q)$ rather than $\mu$. Under the risk-neutral measure, the Black-Scholes PDE becomes:

$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r - q) S \frac{\partial V}{\partial S} - rV = 0}
$$

**Key change**: The drift term $rS\frac{\partial V}{\partial S}$ becomes $(r-q)S\frac{\partial V}{\partial S}$.

### 6. **Why Continuous Dividends May Not Hold**


Although including dividends enhances model realism, it introduces complications and limitations:

**1. Discrete vs. continuous payments**:
- Most companies pay dividends at discrete intervals (quarterly, annually)
- Continuous yield is a mathematical convenience, not market reality
- Creates discontinuities on ex-dividend dates that the model doesn't capture

**2. Dividend uncertainty**:
- Future dividends are not always known with certainty
- Companies can change dividend policy (cut, increase, suspend)
- Economic shocks alter dividend expectations
- Fixed dividend yield $q$ assumption is questionable for long maturities

**3. Exotic options**:
- For barrier options, discrete dividend drops can trigger knock-in/knock-out events
- For Asian options, dividend timing affects average price calculations
- Path-dependent payoffs interact complexly with dividend structure

**4. Tax effects**:
- Dividends and capital gains may be taxed differently
- After-tax returns differ from pre-tax models
- Investors in different tax brackets value dividends differently

### 7. **Impact on Option Pricing**


The dividend yield has opposite effects on calls and puts:

**Call options**:
- Dividends **reduce** the underlying stock's expected growth rate
- Lower call option price compared to no-dividend case
- Stockholder receives part of return through dividends, not capital gains
- **Mathematical effect**: $e^{-qT}$ factor in front of $S$ in formula

**Put options**:
- Dividends **increase** the likelihood of expiring in-the-money
- Dividends reduce underlying stock price over time
- Put options on dividend-paying stocks are more expensive
- **Mathematical effect**: Same $e^{-qT}$ adjustment, but increases put value

**Numerical example**:
- Stock: $S_0 = 100$, $K = 100$, $T = 1$ year, $r = 5\%$, $\sigma = 20\%$
- **No dividends** ($q = 0\%$): $C \approx 10.45$, $P \approx 5.57$
- **With dividends** ($q = 3\%$): $C \approx 8.92$, $P \approx 6.97$
- Call decreases by ~15%, put increases by ~25%

### 8. **Practical Relevance**


The dividend effect depends critically on option maturity:

**Short-term options** (weeks to months):
- Dividends may have little impact
- Dividend payment unlikely within option lifespan
- Can sometimes ignore dividend adjustment

**Long-term options** (LEAPS - 1+ years):
- Cumulative effect of dividend payments becomes significant
- Multiple dividend payments expected
- Failing to account for dividends causes serious mispricing
- **Rule of thumb**: For $T > 6$ months, dividend adjustment essential

**Market practice**:
- Traders compute **implied continuous dividend yield** from market prices
- Back out $q$ from observed option prices and stock dynamics
- Use forward prices: $F = Se^{(r-q)T}$ to infer $q$
- Adjust $q$ based on announced dividend schedules

**American options**:
- Early exercise decisions depend on dividend timing
- American calls may be optimally exercised just before ex-dividend date
- Discrete dividends create complex free boundary problems

### 9. **Summary**


The introduction of a continuous dividend yield into the Black-Scholes model:

**Advantages**:
- Enhances realism for dividend-paying stocks
- Improves pricing accuracy
- Prevents systematic mispricing
- Analytically tractable (closed-form solutions still exist)

**Limitations**:
- Continuous yield is an idealization (actual dividends are discrete)
- Assumes known, constant dividend rate
- Simplifies mathematics at expense of empirical accuracy

**Practical verdict**:
Despite its limitations, the dividend-adjusted Black-Scholes model remains widely used due to:
- Analytical tractability
- Ease of implementation
- Reasonable approximation for stocks with regular dividend policies
- Standard market convention

For precise pricing around ex-dividend dates or for options highly sensitive to dividend timing, discrete dividend models may be necessary.

---

### 10. **Extensions to Include Dividends**


**1. Continuous dividend yield $q$**:

Replace $r$ with $r - q$ in the drift:
$$
dS_t = (r - q)S_t dt + \sigma S_t dW_t
$$

Black-Scholes formula becomes:
$$
C = Se^{-qT}\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

with modified $d_1$:
$$
d_1 = \frac{\ln(S/K) + (r - q + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

**2. Discrete dividends $D_i$ at times $t_i$**:

Replace $S$ with $S - \text{PV(dividends)}$:
$$
S' = S - \sum_{i: t_i < T} D_i e^{-r(t_i - t)}
$$

Use $S'$ in the Black-Scholes formula.

**3. Proportional dividends**: If dividend is $\delta \cdot S$ at $t_d$, model the percentage drop directly.

---

## Why These Assumptions Matter


### 1. **Analytical Tractability**


The six assumptions enable **closed-form solutions**:
- Constant parameters → time-homogeneous PDE
- Frictionless markets → exact replication
- Continuous trading → Itô calculus applies
- Constant $r$ → simple discounting
- No arbitrage → unique pricing
- No dividends → simplified dynamics

**Result**: The elegant Black-Scholes formula for European options.

### 2. **Practical Limitations**


Real-world deviations create:

**1. Model risk**: Predictions differ from reality
- Volatility smiles indicate non-constant $\sigma$
- Fat tails suggest non-Gaussian returns
- Discrete hedging creates hedging errors

**2. Implementation challenges**:
- Transaction costs reduce hedging profitability
- Discrete rebalancing requires optimization
- Parameter estimation (especially $\sigma$) is noisy

**3. Extensions needed**:
- Stochastic volatility models (Heston)
- Jump-diffusion (Merton)
- Local volatility (Dupire)
- Transaction cost models (Leland)

### 3. **The Role of Idealization**


Like any scientific model, Black-Scholes **simplifies reality to capture essence**:
- Physics uses frictionless planes and point masses
- Economics assumes rational agents and perfect competition
- Black-Scholes assumes perfect hedging and constant volatility

**Value despite limitations**:
- Provides **baseline benchmark** for pricing
- **Implied volatility** reveals market expectations
- **Greeks** guide risk management
- **Framework** extends to more complex models

The assumptions are best viewed as **starting points** for more realistic models, not as descriptions of reality.

---

## Summary Table


| Assumption | Statement | Implication | Main Violation |
|------------|-----------|-------------|----------------|
| **1. GBM with constant $\mu, \sigma$** | $dS = \mu S dt + \sigma S dW$ | Log-normal prices, continuous paths | Volatility clustering, jumps, fat tails |
| **2. Frictionless markets** | No transaction costs or spreads | Perfect replication possible | Bid-ask spreads, market impact |
| **3. Continuous trading** | Adjust positions at any instant | Exact delta hedging | Discrete rebalancing, market closures |
| **4. Constant risk-free rate** | $r$ fixed over time | Simple discounting | Interest rates vary, term structure |
| **5. No arbitrage** | No riskless profit opportunities | Unique pricing via replication | Crisis dislocations, limits to arbitrage |
| **6. No dividends** | Asset pays no cash distributions | Simplified dynamics | Most stocks pay dividends |

---

## Summary


The Black-Scholes model rests on six core assumptions:

**1. Geometric Brownian motion** with constant drift $\mu$ and volatility $\sigma$  
**2. Frictionless markets** with no transaction costs  
**3. Continuous trading** at any instant  
**4. Constant risk-free rate** $r$  
**5. No arbitrage** opportunities  
**6. No dividends** during option life  

**Purpose**: These assumptions enable:
- Analytical solutions (closed-form formulas)
- Unique pricing via replication
- Mathematical rigor and tractability

**Reality**: Each assumption is violated to some degree in practice:
- Volatility is not constant (smiles, clustering)
- Transaction costs are non-zero (though small for liquid assets)
- Trading is discrete (not continuous)
- Interest rates vary over time
- Arbitrage opportunities occasionally appear (but vanish quickly)
- Most stocks pay dividends

**Importance**: Understanding these assumptions is critical for:
- Recognizing model limitations
- Knowing when Black-Scholes is appropriate
- Motivating extensions and more sophisticated models
- Interpreting implied volatility and model calibration

The next section examines how real markets deviate from these assumptions and what extensions address these violations.
