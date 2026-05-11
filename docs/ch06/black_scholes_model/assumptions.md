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

### 4. **Practical Implementation: What is r in Practice?**


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

---

## Exercises

**Exercise 1.** Consider a stock with $S_0 = 100$, $\mu = 0.10$, and $\sigma = 0.25$ under GBM. Compute the probability that the stock price is below \$80 after one year, i.e., $\mathbb{P}(S_1 < 80)$. How does this compare to the probability under Bachelier's arithmetic Brownian motion (with the same $S_0$ and $\sigma$)?

??? success "Solution to Exercise 1"
    Under GBM, the stock price at $t = 1$ satisfies

    $$
    \ln S_1 \sim \mathcal{N}\!\left(\ln S_0 + \left(\mu - \frac{1}{2}\sigma^2\right), \sigma^2\right)
    $$

    With $S_0 = 100$, $\mu = 0.10$, $\sigma = 0.25$:

    $$
    \ln S_1 \sim \mathcal{N}\!\left(\ln 100 + 0.10 - \frac{0.0625}{2}, 0.0625\right) = \mathcal{N}(4.6677, 0.0625)
    $$

    We need $\mathbb{P}(S_1 < 80) = \mathbb{P}(\ln S_1 < \ln 80)$:

    $$
    z = \frac{\ln 80 - 4.6677}{\sqrt{0.0625}} = \frac{4.3820 - 4.6677}{0.25} = \frac{-0.2857}{0.25} = -1.1429
    $$

    Therefore $\mathbb{P}(S_1 < 80) = \Phi(-1.1429) \approx 0.1265$, or about 12.65%.

    Under Bachelier's arithmetic Brownian motion with $S_t = S_0 + \sigma_{\text{ABM}} W_t$ (using the same absolute volatility $\sigma_{\text{ABM}} = \sigma \cdot S_0 = 25$), we have $S_1 \sim \mathcal{N}(100, 625)$, so:

    $$
    \mathbb{P}(S_1 < 80) = \Phi\!\left(\frac{80 - 100}{25}\right) = \Phi(-0.80) \approx 0.2119
    $$

    The ABM probability (~21.2%) is considerably higher because (i) it has no drift term pushing the price upward, and (ii) the normal distribution is symmetric about the mean, whereas the log-normal distribution under GBM is right-skewed, placing less mass in the left tail relative to the mean.

---
**Exercise 2.** Assumption 2 states that markets are frictionless. Suppose instead that each trade incurs a proportional transaction cost of $\kappa > 0$ (i.e., buying or selling \$1 of stock costs an additional $\kappa$ dollars). If a delta-hedging strategy requires rebalancing $N$ times over the life of the option, provide a rough estimate of the total transaction cost as a function of $\kappa$, $N$, the average gamma $\bar{\Gamma}$, and the stock price $S$. Explain why continuous hedging ($N \to \infty$) is infeasible in this setting.

??? success "Solution to Exercise 2"
    When delta-hedging with transaction costs, each rebalancing requires trading a quantity of stock approximately proportional to the change in delta. Over a small time interval $\Delta t$, the change in delta is dominated by the gamma term:

    $$
    |\Delta(\text{shares})| \approx \bar{\Gamma} \cdot |\Delta S|
    $$

    where $|\Delta S| \approx \sigma S \sqrt{\Delta t}$ for a typical move. Each such trade costs $\kappa$ per dollar transacted, so the cost of one rebalancing is approximately:

    $$
    \text{Cost per rebalance} \approx \kappa \cdot \bar{\Gamma} \cdot S \cdot |\Delta S| \approx \kappa \bar{\Gamma} \sigma S^2 \sqrt{\Delta t}
    $$

    With $N$ rebalancing steps and $\Delta t = T/N$, the total transaction cost is approximately:

    $$
    \text{Total cost} \approx N \cdot \kappa \bar{\Gamma} \sigma S^2 \sqrt{\frac{T}{N}} = \kappa \bar{\Gamma} \sigma S^2 \sqrt{NT}
    $$

    As $N \to \infty$, this total cost grows as $\sqrt{N} \to \infty$. Therefore, continuous hedging is infeasible: the accumulated transaction costs diverge to infinity, making perfect replication impossible in the presence of any positive transaction cost $\kappa > 0$.

---
**Exercise 3.** Under the no-dividend assumption (Assumption 6), prove that it is never optimal to exercise an American call option early on a non-dividend-paying stock. Your proof should use only the lower bound $C \geq S - Ke^{-rT}$ and the fact that early exercise yields payoff $S - K$.

??? success "Solution to Exercise 3"
    We prove that early exercise of an American call on a non-dividend-paying stock is never optimal.

    At any time $t < T$, the holder of the American call can either (i) exercise early, receiving payoff $S_t - K$, or (ii) continue to hold the option.

    The value of the European call satisfies the lower bound:

    $$
    C(S_t, t) \geq S_t - Ke^{-r(T-t)}
    $$

    This follows from no-arbitrage: a portfolio of one call plus $Ke^{-r(T-t)}$ in the bond dominates a portfolio of one share (at maturity the call pays at least $S_T - K$ when $S_T > K$, and the bond grows to $K$, giving total $\geq S_T$; when $S_T \leq K$, the total is $\geq K \geq 0$).

    Since $r > 0$ and $T - t > 0$, we have $e^{-r(T-t)} < 1$, which gives:

    $$
    C(S_t, t) \geq S_t - Ke^{-r(T-t)} > S_t - K
    $$

    The American call is worth at least as much as the European call (it has all the same rights plus the early exercise option), so:

    $$
    C_{\text{Am}}(S_t, t) \geq C(S_t, t) > S_t - K
    $$

    Since the value of holding the option strictly exceeds the early exercise payoff $S_t - K$ at every $t < T$, it is never optimal to exercise early. $\square$

---
**Exercise 4.** The Black-Scholes model assumes a constant risk-free rate $r$. Suppose the risk-free rate follows a deterministic function $r(t)$. Show that the Black-Scholes PDE generalizes to

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r(t) S \frac{\partial V}{\partial S} - r(t) V = 0
$$

and explain how the discounting factor $e^{-rT}$ in the Black-Scholes formula should be modified.

??? success "Solution to Exercise 4"
    We derive the generalized Black-Scholes PDE with a time-dependent risk-free rate.

    Consider a portfolio $\Pi = V - \Delta S$ where $V = V(S, t)$ is the option price. By Ito's lemma:

    $$
    dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}dt
    $$

    Choosing $\Delta = \frac{\partial V}{\partial S}$ eliminates the stochastic term:

    $$
    d\Pi = dV - \frac{\partial V}{\partial S}dS = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt
    $$

    The no-arbitrage condition requires the risk-free portfolio to earn the instantaneous risk-free rate $r(t)$:

    $$
    d\Pi = r(t)\Pi \, dt = r(t)\left(V - S\frac{\partial V}{\partial S}\right)dt
    $$

    Equating the two expressions:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = r(t)V - r(t)S\frac{\partial V}{\partial S}
    $$

    Rearranging gives the generalized PDE:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r(t)S\frac{\partial V}{\partial S} - r(t)V = 0
    $$

    The discounting factor $e^{-rT}$ in the constant-rate Black-Scholes formula must be replaced by:

    $$
    e^{-rT} \longrightarrow \exp\!\left(-\int_0^T r(s)\,ds\right)
    $$

    That is, the constant discount factor is replaced by the integral of the instantaneous short rate over the option's lifetime. The risk-neutral pricing formula becomes $V_0 = \exp\!\left(-\int_0^T r(s)\,ds\right)\mathbb{E}^{\mathbb{Q}}[H]$.

---
**Exercise 5.** The dividend-adjusted Black-Scholes formula is $C = Se^{-qT}\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ with $d_1 = \frac{\ln(S/K) + (r - q + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$. Compute the call and put prices for $S = 100$, $K = 100$, $r = 5\%$, $q = 3\%$, $\sigma = 20\%$, and $T = 1$ year. Verify that the dividend-adjusted put-call parity $C - P = Se^{-qT} - Ke^{-rT}$ holds.

??? success "Solution to Exercise 5"
    With $S = 100$, $K = 100$, $r = 0.05$, $q = 0.03$, $\sigma = 0.20$, $T = 1$.

    First compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(100/100) + (0.05 - 0.03 + 0.5 \times 0.04) \times 1}{0.20 \times 1} = \frac{0 + 0.04}{0.20} = 0.20
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.20 - 0.20 = 0.00
    $$

    From normal distribution tables: $\mathcal{N}(0.20) \approx 0.5793$ and $\mathcal{N}(0.00) = 0.5000$.

    **Call price**:

    $$
    C = 100 \cdot e^{-0.03} \cdot 0.5793 - 100 \cdot e^{-0.05} \cdot 0.5000
    $$

    $$
    C = 100 \times 0.97045 \times 0.5793 - 100 \times 0.95123 \times 0.5000
    $$

    $$
    C \approx 56.22 - 47.56 = 8.66
    $$

    **Put price** via put-call parity: $P = C - Se^{-qT} + Ke^{-rT}$:

    $$
    P = 8.66 - 100 \times 0.97045 + 100 \times 0.95123
    $$

    $$
    P = 8.66 - 97.045 + 95.123 \approx 6.74
    $$

    **Verification of dividend-adjusted put-call parity**:

    $$
    C - P = 8.66 - 6.74 = 1.92
    $$

    $$
    Se^{-qT} - Ke^{-rT} = 97.045 - 95.123 = 1.92 \quad \checkmark
    $$

    The dividend-adjusted put-call parity $C - P = Se^{-qT} - Ke^{-rT}$ holds exactly (up to rounding).

---
**Exercise 6.** Discuss which of the six Black-Scholes assumptions is most severely violated for each of the following instruments: (a) a 1-week option on a liquid large-cap stock, (b) a 2-year LEAPS option on a high-dividend utility stock, (c) an option on a cryptocurrency. For each case, identify the assumption that is most problematic and suggest an appropriate model extension.

??? success "Solution to Exercise 6"
    **(a) 1-week option on a liquid large-cap stock**:

    The most severely violated assumption is **Assumption 3 (Continuous Trading)**. Even though the stock is liquid and one week is short enough that dividends, interest rate changes, and volatility shifts are minor, markets close overnight and on weekends. For a 1-week option, overnight gaps represent a significant fraction of the total time to maturity, creating unhedgeable exposure. Additionally, while rare, flash crashes or sudden news events can cause discrete jumps (violating Assumption 1), and these are relatively more impactful for short-dated options where gamma is high. **Model extension**: Discrete hedging models or jump-diffusion (Merton, 1976) to account for overnight gaps and sudden moves.

    **(b) 2-year LEAPS option on a high-dividend utility stock**:

    The most severely violated assumption is **Assumption 6 (No Dividends)**. Utility stocks typically have dividend yields of 3--5%, and over a 2-year horizon, multiple quarterly dividend payments will occur, each causing a discrete drop in the stock price on the ex-dividend date. Ignoring dividends leads to significant overpricing of calls and underpricing of puts. The constant risk-free rate assumption (Assumption 4) is also problematic over 2 years, as interest rates can change materially. **Model extension**: The dividend-adjusted Black-Scholes model with continuous yield $q$ as a first approximation, or a discrete-dividend model for greater accuracy. For interest rate uncertainty, one could use Black's model with the forward price.

    **(c) Option on a cryptocurrency**:

    The most severely violated assumption is **Assumption 1 (GBM with constant parameters)**. Cryptocurrency prices exhibit extreme volatility clustering, very fat tails (daily moves of 10--20% are not unusual), and frequent jumps driven by regulatory announcements, exchange failures, or shifts in market sentiment. The constant volatility assumption is grossly inadequate. Additionally, Assumption 2 (frictionless markets) is violated due to significant bid-ask spreads on many exchanges, varying liquidity across platforms, and potential for exchange outages. **Model extension**: Stochastic volatility with jumps (e.g., Bates model combining Heston stochastic volatility with Merton jumps), or regime-switching models to capture the distinct volatility regimes observed in cryptocurrency markets.
