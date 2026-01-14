# Overlay Strategies


**Overlay strategies** are centralized portfolio management techniques that apply systematic risk management, tactical adjustments, or alpha generation across multiple underlying portfolios without disturbing the base managers, effectively adding a layer of risk control, hedging, or return enhancement on top of existing allocations.

---

## The Core Insight


**The fundamental idea:**

- Institutional portfolios are often managed by multiple specialists
- Each manager focuses on their mandate (equities, bonds, etc.)
- But overall portfolio may have unintended risks or inefficiencies
- Overlay allows central control without disrupting base managers
- Can hedge, rebalance, or enhance returns at aggregate level
- Separates risk management from asset selection

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/overlay_structure.png?raw=true" alt="overlay_structure" width="700">
</p>
**Figure 1:** Overlay structure showing base managers handling security selection while the overlay manager implements centralized currency hedging, equity exposure adjustments, and duration management across the entire portfolio using derivatives.

**You're essentially creating: "One central risk manager for many decentralized asset managers."**

---

## What Are Overlays?


### 1. Currency Overlay


**Centralized FX management:**

**Definition:** A specialist manager handles all foreign exchange hedging for the entire portfolio, regardless of which investment manager holds the underlying foreign assets.

**When you use currency overlay:**

- Multiple global equity/bond managers
- Each invests in foreign securities
- Currency exposure is portfolio-wide risk
- Overlay manager hedges at aggregate level
- Base managers focus on security selection only

**Example:**
- Total portfolio: $1B
- Global equity manager A: Holds €200M stocks
- Global equity manager B: Holds €150M stocks  
- International bond manager: Holds €100M bonds
- **Total EUR exposure: €450M**
- Currency overlay manager hedges this at portfolio level
- Base managers never touch FX hedging

**Economic benefit:**
- Centralized expertise in FX hedging
- Netting of exposures across managers
- Economies of scale in execution
- Consistent hedge policy across portfolio
- Base managers not distracted by currency decisions

### 2. Tactical Asset Allocation


**Active rebalancing overlay:**

**Definition:** Overlay manager makes tactical shifts in asset allocation using derivatives, overweighting/underweighting asset classes based on market views, without touching underlying holdings.

**When you use TAA overlay:**

- Strategic allocation is 60% equity / 40% bonds
- Overlay manager has near-term market views
- Can shift to 65% equity / 35% bonds tactically
- Uses futures to implement (no cash movements)
- Base managers continue executing within their mandates

**How it works:**

Strategic allocation:
- 60% equity ($600M) managed by equity manager
- 40% bonds ($400M) managed by bond manager

Tactical adjustment (overlay view: bullish on equities):
- Overlay buys $50M equity index futures
- Overlay sells $50M bond futures
- **Effective allocation: 65% equity / 35% bonds**
- No cash moved, no disruption to base managers
- Base managers still managing their original $600M/$400M

**Economic benefit:**
- Centralized market timing decisions
- Lower transaction costs (futures vs. cash)
- No disruption to base managers' strategies
- Can implement faster than reallocating cash
- Separates strategic (long-term) from tactical (short-term)

### 3. Equity Exposure Overlay


**Beta management:**

**Definition:** Overlay manager adjusts the portfolio's overall equity exposure using index futures or swaps, overweighting or underweighting equities versus the strategic policy without changing individual stock holdings.

**When you use equity overlay:**

- Want to tactically reduce equity risk
- Without forcing managers to sell stocks
- Maintain active manager alpha capture
- Implement quickly using derivatives

**Example - Risk Reduction:**

- Portfolio: $1B, 60% equity ($600M)
- Market concern: Recession risk rising
- Goal: Temporarily reduce equity to 50% ($500M)

**Without overlay (traditional):**
- Call equity managers, ask them to raise cash
- They must sell $100M of stocks (disrupts positions)
- Transaction costs: ~0.5% = $500K
- Destroys active positions, damages alpha
- Takes days/weeks to execute

**With overlay:**
- Overlay manager sells $100M S&P 500 futures
- Effective equity exposure now $500M (50%)
- Equity managers' holdings unchanged
- Transaction cost: ~0.01% = $10K
- **Savings: $490K + preserved alpha generation**
- Executes in hours

### 4. Duration Overlay


**Interest rate risk management:**

**Definition:** Overlay manager adjusts the portfolio's interest rate sensitivity (duration) using bond futures or interest rate swaps, without changing actual bond holdings.

**When you use duration overlay:**

- Multiple fixed income managers
- Want centralized interest rate risk control
- Portfolio duration drifts from target
- Need to adjust quickly for rate views

**Example:**

Portfolio has three bond managers:
- Manager A: $200M, duration 5 years
- Manager B: $150M, duration 7 years  
- Manager C: $250M, duration 6 years
- **Aggregate duration: 6 years**
- **Policy target: 5 years**

**Without overlay:**
- Ask each manager to sell longer bonds, buy shorter
- Disrupts their credit/sector strategies
- High transaction costs (bond trading expensive)
- May conflict with managers' views

**With overlay:**
- Overlay sells $600M equivalent of 10-year Treasury futures
- Effective duration reduced by ~1 year
- **Portfolio duration now at target: 5 years**
- Bond managers' holdings unchanged
- Lower transaction costs, faster execution

### 5. Transition Overlay


**Manager changes:**

**Definition:** When replacing investment managers, overlay handles the transition from old to new manager using derivatives to maintain market exposure during the physical transition period.

**When you use transition overlay:**

- Firing Manager A, hiring Manager B
- Physical transition takes 30-60 days
- Don't want to be out of market during transition
- Risk of missing rallies or being exposed to declines

**How it works:**

**Day 1:**
- Decide to replace equity manager
- Current holding: $500M in Manager A's portfolio
- Overlay immediately buys $500M S&P 500 futures
- **Portfolio fully exposed despite upcoming transition**

**Days 1-30:**
- Manager A gradually liquidates portfolio to cash
- Cash transferred to custody
- Manager B gradually invests into new portfolio
- Throughout: Market exposure maintained via overlay futures

**Day 30:**
- Manager B fully invested ($500M in new stocks)
- Overlay closes $500M futures position
- **Transition complete, zero market timing risk**

**Economic benefit:**
- No "out of market" risk during transition
- Reduces opportunity cost
- Coordinates complex multi-manager changes
- Can take time to optimize transition (no rush)

### 6. Portable Alpha


**Alpha transport:**

**Definition:** Overlay separates alpha generation from beta exposure, allowing investors to access alternative alpha sources while maintaining desired market exposure through derivatives.

**When you use portable alpha:**

- Want market beta exposure (e.g., S&P 500)
- Want uncorrelated alpha from hedge fund
- Use overlay to combine both

**Structure:**

**Traditional approach:**
- Invest $100M in S&P 500 index
- Get beta return (~8-10% long-term)
- No alpha

**Portable alpha approach:**
- Invest $100M in market-neutral hedge fund (target: 5% alpha)
- Overlay buys $100M S&P 500 futures (cost: margin only, ~10%)
- Free up $90M to invest in additional alpha sources
- **Expected return: 8-10% beta + 5% alpha = 13-15%**

**Economic structure:**

$$
\text{Total Return} = \underbrace{\text{Beta}}_{\text{Futures}} + \underbrace{\text{Alpha}}_{\text{Active Manager}} - \underbrace{\text{Financing Cost}}_{\text{Margin/Carry}}
$$

**Real example:**

Capital: $100M
- Invest $10M as margin for $100M S&P futures (beta)
- Invest $90M in long-short equity fund (alpha source)
- **Beta exposure: $100M**
- **Alpha exposure: $90M**
- Combined leverage and diversification

### 7. Passive/Active Overlay


**Alpha completion:**

**Definition:** Use passive indexing for core beta exposure, add overlay of active managers for alpha generation, controlling aggregate exposures at overlay level.

**When you use this:**

- Believe in efficient markets (hard to beat)
- But want to try active management in select areas
- Use overlay to control total risk

**Structure:**

- Core: $800M in passive index funds (80%)
- Satellite: $200M split among 5 active managers (20%)
- Overlay monitors: Are active managers adding value or just adding risk?
- Adjusts aggregate beta exposure to maintain risk budget

**Overlay manager actions:**

If active managers increase equity exposure beyond policy:
- Overlay sells index futures to offset
- Maintains policy-level beta exposure
- Allows active managers to take style bets
- But prevents portfolio from drifting off policy

---

## Key Terminology


**Notional Exposure:**
- Dollar amount of market exposure created by derivatives
- 1 S&P 500 future = $250 × index level exposure
- Key metric for overlay programs
- Can exceed actual capital (leverage)

**Margin:**
- Collateral posted for derivative positions
- Typically 5-15% of notional
- Frees up capital for other uses
- Daily mark-to-market and variation margin

**Tracking Error:**
- Difference between overlay program and benchmark
- Measures active risk taken
- Target: 0-2% for passive overlays, 2-5% for active
- Key performance metric

**Implementation Shortfall:**
- Cost of implementing overlay decisions
- Includes bid-ask spreads, slippage, market impact
- Lower for derivatives vs. cash securities
- Important cost to monitor

**Cash Equitization:**
- Process of gaining equity exposure on cash balances
- Uses equity futures or swaps
- Maintains cash for liquidity while staying invested
- Common in transition management

**Rebalancing Drift:**
- When portfolio weights deviate from targets over time
- Due to relative performance of assets
- Overlay can correct without cash transactions
- More efficient than traditional rebalancing

---

## Overlay Design


### 1. Program Objectives


**Define clear goals:**

**Risk management objectives:**
- Maintain strategic asset allocation targets
- Control currency exposure
- Manage interest rate duration
- Limit downside risk
- Reduce tracking error vs. policy

**Return enhancement objectives:**
- Generate tactical alpha from market timing
- Capture rebalancing alpha
- Optimize transition management
- Portable alpha implementation
- Tax-loss harvesting at portfolio level

**Operational objectives:**
- Improve efficiency of portfolio adjustments
- Reduce transaction costs vs. cash rebalancing
- Maintain base manager independence
- Centralize derivative expertise
- Enhance reporting and risk monitoring

### 2. Governance Structure


**Who does what:**

**Investment Committee:**
- Sets strategic policy (asset allocation, risk limits)
- Approves overlay mandate and guidelines
- Reviews performance quarterly
- Approves material changes to program

**Overlay Manager:**
- Implements policy directives
- Makes tactical decisions within mandated ranges
- Executes derivative transactions
- Daily risk monitoring and reporting
- Margin management and collateral optimization

**Base Managers:**
- Continue security selection within mandates
- Ignore aggregate portfolio considerations
- Focus on generating alpha in their specialization
- Report positions/exposures to overlay manager

**Risk/Compliance:**
- Monitors overlay program compliance
- Checks counterparty credit risk
- Validates pricing and valuations
- Ensures regulatory compliance (ERISA, RIC, etc.)

### 3. Authority & Limits


**Overlay manager discretion:**

**Tactical ranges (example):**

```
Strategic Policy: 60% Equity / 40% Bonds

Tactical ranges allowed:
- Equity: 55-65% (±5% from policy)
- Bonds: 35-45% (±5% from policy)
- Duration: Policy ±1 year
- Currency hedge: 0-100% of foreign exposure
```

**Leverage limits:**
- Gross notional derivatives < 50% of NAV
- Net notional < 20% of NAV
- Margin < 10% of NAV
- Single currency hedge < 5% of NAV

**Counterparty limits:**
- Investment grade only (A or higher)
- Max 25% of derivative exposure per counterparty
- Minimum 4 counterparties
- Daily collateral management

**Reporting requirements:**
- Daily: Positions, margin, NAV impact
- Weekly: Risk metrics, attribution
- Monthly: Full performance report
- Quarterly: Review with Investment Committee

### 4. Instrument Selection


**Choose appropriate derivatives:**

**For equity exposure:**
- **Futures:** Liquid, low cost, exchange-traded
- **Swaps:** Customizable, OTC, for non-standard indices
- **ETFs:** Small positions, highly liquid
- Avoid: Individual stock derivatives (tracking error)

**For fixed income duration:**
- **Treasury futures:** Most liquid, standardized
- **Interest rate swaps:** Precise duration matching
- **TIPS futures:** Inflation protection
- Avoid: Credit derivatives (introduces credit risk)

**For currency hedging:**
- **FX forwards:** Most common, low cost
- **FX options:** When asymmetric risk/reward desired
- **Currency swaps:** Long-term hedges
- Avoid: Exotic structures (NDFs, barriers)

**For transitions:**
- **Futures:** Fast implementation
- **ETFs:** Smaller positions, fractional exposure
- **Total return swaps:** Custom baskets
- Cash equitization: Maintain liquidity during transition

### 5. Benchmark & Evaluation


**How to measure success:**

**For passive overlays (hedging, rebalancing):**
- **Primary metric:** Policy compliance
- Target: Within ±0.5% of strategic allocation
- Tracking error: < 1% annually
- Cost: Implementation costs < 0.05% annually

**For active overlays (TAA, alpha transport):**
- **Primary metric:** Risk-adjusted alpha
- Sharpe ratio: > 0.5 (minimum acceptable)
- Information ratio: > 0.5
- Win rate: > 55% of tactical bets
- Max drawdown: < 5%

**Cost analysis:**

$$
\text{Overlay Cost} = \text{Management Fee} + \text{Transaction Costs} + \text{Opportunity Costs}
$$

**Typical costs:**
- Passive overlay fee: 0.05-0.15% annually
- Active overlay fee: 0.25-0.75% annually
- Transaction costs: 0.01-0.10% per adjustment
- Benchmark: Must add value net of all costs

---

## Implementation Strategies


### 1. Currency Overlay Program


**Centralized FX hedging:**

**Step 1: Aggregate exposures**

Each manager reports foreign currency holdings:
- Manager A: €200M, £100M, ¥5B
- Manager B: €150M, £80M, ¥3B
- Manager C: €100M, £50M, ¥2B
- **Net: €450M, £230M, ¥10B**

**Step 2: Set hedge policy**

Example policy:
- EUR: Hedge 75% (large exposure)
- GBP: Hedge 50% (moderate exposure)
- JPY: Hedge 25% (diversification benefit)

**Step 3: Execute hedges**

Overlay manager trades:
- Sell €337.5M forward (75% of €450M)
- Sell £115M forward (50% of £230M)
- Sell ¥2.5B forward (25% of ¥10B)

**Step 4: Monitor and rebalance**

Monthly:
- Get updated foreign holdings from managers
- Compare to current hedges
- Add/remove hedges to maintain target ratios
- Report hedging P&L vs. unhedged scenario

**Performance measurement:**

$$
\text{Hedge Effectiveness} = 1 - \frac{\text{Var}(\text{Hedged Return})}{\text{Var}(\text{Unhedged Return})}
$$

Target: > 70% variance reduction

### 2. Tactical Asset Allocation


**Active overlay implementation:**

**Decision process:**

1. **Gather inputs:**
   - Economic indicators (GDP, inflation, unemployment)
   - Market technicals (trends, momentum, sentiment)
   - Valuation metrics (P/E, yield curves)
   - Risk indicators (VIX, credit spreads)

2. **Form view:**
   - Bullish: Overweight equities, underweight bonds
   - Bearish: Underweight equities, overweight bonds
   - Neutral: Match policy weights

3. **Size position:**
   - Conviction-weighted
   - High conviction: Max tilt (±5%)
   - Medium conviction: Modest tilt (±2-3%)
   - Low conviction: Small tilt (±1%)

4. **Execute:**
   - Use liquid index futures (S&P 500, Russell 2000, 10Y Treasury)
   - Implement over 1-2 days (avoid market impact)
   - Document rationale and expected holding period

**Example tactical trade:**

**Setup (January):**
- Fed signaling rate cuts later in year
- Credit spreads tight (low recession risk)
- Equity momentum strong
- **View: Bullish equities for next 3 months**

**Action:**
- Current: 60% equity / 40% bonds
- Target: 65% equity / 35% bonds
- Buy $50M S&P 500 futures
- Sell $50M 10-year Treasury futures
- **Hold period: 90 days**

**Outcome (April):**
- S&P 500: +8% (futures gain: $4M)
- 10Y Treasury: +2% (futures loss: $1M)
- **Net overlay gain: $3M**
- Close positions, return to policy weights

**Risk management:**
- Stop loss: If view wrong, exit at -1% loss
- Time stop: Review after 90 days regardless
- Position limit: Never exceed ±5% tilt

### 3. Completion Overlay


**Filling gaps in base manager coverage:**

**Problem:**

Portfolio has:
- Large-cap equity manager (Russell 1000)
- International equity manager (MSCI EAFE)
- Bond manager (US Aggregate)

**Missing exposures:**
- Small-cap US equities (not covered)
- Emerging markets (not covered)
- TIPS (inflation protection missing)

**Overlay solution:**

Add completion positions using ETFs/futures:
- Russell 2000 futures: $50M (5% allocation to small-cap)
- MSCI EM futures: $30M (3% allocation to EM)
- TIPS futures: $40M (4% allocation to inflation protection)

**Total portfolio now:**
- Large-cap: 52% (via base manager)
- Small-cap: 5% (via overlay)
- International: 25% (via base manager)
- EM: 3% (via overlay)
- Bonds: 11% (via base manager)
- TIPS: 4% (via overlay)
- **Total: 100% policy compliance**

**Benefits:**
- Don't need to hire another manager
- Low cost (futures cheaper than active managers)
- Flexible (can adjust allocations easily)
- Maintains base managers' focus

### 4. Dynamic Rebalancing


**Automated rebalancing overlay:**

**Problem:**
- Portfolio drifts from policy due to performance
- Traditional rebalancing: quarterly, costly
- Miss opportunities to rebalance at extremes

**Overlay solution:**

**Rule-based triggers:**

```python
IF equity allocation > (policy + 3%):
    Sell enough equity futures to return to (policy + 1%)
ELIF equity allocation < (policy - 3%):
    Buy enough equity futures to return to (policy - 1%)
ELSE:
    No action
```

**Example:**

Policy: 60% equity / 40% bonds

**Month 1:**
- Equities rally +5%, bonds flat
- New allocation: 63% / 37% (drift of +3%)
- **Trigger: Sell equity futures to rebalance to 61% / 39%**
- Overlay sells $20M equity futures

**Month 2:**
- Equities continue up +3%, bonds flat
- New allocation: 63% / 37% again
- **Trigger: Sell more equity futures to maintain 61% / 39%**

**Month 3:**
- Equities fall -7%, bonds flat
- New allocation: 57% / 43% (drift of -3%)
- **Trigger: Buy equity futures to rebalance to 59% / 41%**
- Overlay buys $40M equity futures

**Performance:**
- Captures rebalancing alpha (sell high, buy low)
- Maintains policy compliance continuously
- Lower cost than cash rebalancing
- Automatic and disciplined

**Rebalancing alpha:**

$$
\text{Rebalancing Alpha} \approx \frac{1}{2} \sigma^2 (\text{Difference in volatilities})
$$

Typical: 0.25-0.50% annually for diversified portfolio

### 5. Portable Alpha


**Alpha transport implementation:**

**Structure:**

**Capital: $100M**

**Step 1: Obtain beta exposure**
- Buy $100M S&P 500 futures
- Margin required: $10M
- Remaining capital: $90M free

**Step 2: Invest in alpha source**
- Allocate $90M to market-neutral hedge fund
- Target: 5-7% absolute return (uncorrelated to beta)
- Fund uses long-short equity, market-neutral

**Step 3: Monitor combined position**
- Beta return: S&P 500 performance (~8-10% long-term)
- Alpha return: Hedge fund performance (5-7% target)
- Financing cost: Margin interest (~2-3%)

**Expected return:**

$$
\text{Total Return} = \underbrace{9\%}_{\text{Beta}} + \underbrace{6\%}_{\text{Alpha}} - \underbrace{2.5\%}_{\text{Financing}} = 12.5\%
$$

**vs. traditional:**
- 100% S&P 500: 9% return
- **Portable alpha advantage: +3.5%**

**Risk considerations:**
- Hedge fund could underperform (alpha = 0%)
- Leverage amplifies losses if both beta and alpha negative
- Financing cost varies (rises with interest rates)
- Operational complexity (margin calls, collateral)

**Example outcome (good scenario):**

Year 1:
- S&P 500: +10% (futures gain: $10M)
- Hedge fund: +7% ($90M × 7% = $6.3M)
- Financing: -2.5% ($90M × 2.5% = $2.25M)
- **Total: $14.05M (14% return on $100M)**

**Example outcome (bad scenario):**

Year 1:
- S&P 500: -15% (futures loss: $15M)
- Hedge fund: +5% ($90M × 5% = $4.5M)
- Financing: -2.5% ($90M × 2.5% = $2.25M)
- **Total: -$12.75M (-12.75% loss)**
- Note: Worse than owning S&P 500 alone (-15% + no leverage)

---

## Common Mistakes


### 1. Over-Complication


**Too many overlays:**

- **Mistake:** Layer multiple overlays on top of each other
- **Why it fails:** Conflicts arise, attribution becomes impossible, costs multiply
- **Fix:** One overlay manager coordinates all derivative activity
- **Real cost:** Duplicate positions, confused performance reporting

**Example:**
- Currency overlay manager hedges EUR exposure
- Tactical overlay manager also short EUR (bearish Europe)
- **Result: Over-hedged EUR, double costs, conflicting goals**

### 2. Ignoring Base Managers


**Communication breakdown:**

- **Mistake:** Overlay manager doesn't coordinate with base managers
- **Why it fails:** Base managers may adjust exposures, breaking overlay assumptions
- **Fix:** Daily exposure reports, regular communication
- **Real cost:** Mis-hedged portfolio, tracking error spikes

**Example:**
- Overlay calculates 60% equity exposure based on yesterday's data
- Overnight, equity manager sells $50M (down to 55%)
- Overlay still hedging as if 60%
- **Result: Over-hedged by 5%, unintended bond overweight**

### 3. Chasing Performance


**Tactical whipsaw:**

- **Mistake:** Overlay makes frequent directional bets, chasing recent trends
- **Why it fails:** Trend following doesn't work short-term, high costs
- **Fix:** Disciplined process, minimum hold periods (30-90 days)
- **Real cost:** Transaction costs eat all alpha, negative after fees

**Example:**

Month 1: Bullish equities, buy futures (market falls -3%)
Month 2: Bearish equities, sell futures (market rallies +4%)
Month 3: Bullish again, buy futures (market falls -2%)

**Result:**
- Lost -3%, -4%, -2% = -9% from tactical calls
- Transaction costs: -0.3% (10 bps per trade × 3 trades)
- **Total: -9.3% vs. staying at policy: -1% (simple average)**

### 4. Leverage Creep


**Unintentional leverage:**

- **Mistake:** Derivatives allow easy leverage, position sizes grow unchecked
- **Why it fails:** Losses amplified, margin calls force liquidation
- **Fix:** Hard limits on gross/net notional, frequent monitoring
- **Real cost:** Catastrophic losses in tail events

**Example:**

**Intended overlay:** ±5% tactical tilts
- Buy $50M equity futures (5% overweight on $1B portfolio)

**Leverage creep:**
- Also short $30M bonds (duration adjustment)
- Also long $20M commodities (diversification)
- Also short $40M currencies (hedge)
- **Total notional: $140M (14% of portfolio)**

**Crisis event:** 
- All risk assets fall together (correlation → 1)
- Equity futures: -$10M
- Commodity futures: -$4M  
- Currency moves against: -$2M
- **Total loss: -$16M (1.6% of portfolio)**
- Original ±5% limit was supposed to cap loss at 0.5%

**Lesson:** Gross notional matters, not just net. All positions can lose simultaneously.

### 5. Ignoring Costs


**Death by a thousand cuts:**

- **Mistake:** Frequent small adjustments, each with bid-ask spread and slippage
- **Why it fails:** Costs add up, eat any alpha generated
- **Fix:** Batch trades, wider rebalancing bands, limit turnover
- **Real cost:** 0.5-1% annually in unnecessary costs

**Cost breakdown:**

Daily rebalancing (bad):
- 250 trading days/year
- Average adjustment: $10M
- Bid-ask spread: 1 bp
- **Annual cost: $25,000 × 250 = $6.25M (0.625% of $1B portfolio)**

Monthly rebalancing (better):
- 12 trading days/year
- Average adjustment: $30M (larger but less frequent)
- Bid-ask spread: 1 bp  
- **Annual cost: $30,000 × 12 = $360K (0.036% of $1B portfolio)**

**Savings: $5.89M annually by trading less frequently**

### 6. No Stop-Loss Discipline


**Letting losses run:**

- **Mistake:** Tactical position moves against, but "conviction" prevents exit
- **Why it fails:** One big loss wipes out years of gains
- **Fix:** Hard stop-loss at -1% per position, -3% max total overlay loss
- **Real cost:** Career risk, potential fiduciary breach

**Example:**

**Tactical call:** Bearish on bonds (expect yields to rise)
- Overlay shorts $100M 10-year Treasury futures
- **Target:** 2-3% gain if yields rise as expected

**Outcome:** Yields fall instead (bond rally)
- Month 1: -1% loss ($1M) → No action, "still think we're right"
- Month 2: -2% additional ($2M cumulative) → "Can't be wrong, double down"
- Month 3: -3% additional ($5M cumulative) → "Fed will change policy soon"
- Month 4: -2% additional ($7M cumulative) → Finally exit

**Result:**
- **Total loss: $7M (0.7% of portfolio)**
- A -1% stop loss would have capped this at $1M
- **Unnecessary loss: $6M** (0.6% drag on annual return)

---

## Best vs. Worst Case


### 1. Best Case: Success


**Efficient currency overlay:**

**Setup:**
- $2B global portfolio
- 40% foreign equities (€300M, £200M, ¥20B)
- No FX hedging historically (risk: 8% volatility from FX)

**Overlay implementation:**
- Systematic 75% hedge program
- Layer hedges quarterly
- Use forwards only (simple, low cost)

**Year 1 results:**

**Scenario: Home currency (USD) strengthens 10% vs. basket**

Without overlay:
- Foreign equity returns: +12% in local currency
- Currency impact: -10%
- **Net return: +2%** (severely dragged down by FX)
- Return volatility: 18% (equity + FX volatility)

With overlay:
- Foreign equity returns: +12% in local currency
- 75% of FX hedged: -10% × 25% = -2.5% currency drag
- Hedge cost: -0.5% (forward points)
- **Net return: +9%** (protected from most FX loss)
- Return volatility: 13% (mostly equity volatility)

**Quantified benefit:**
- Return improvement: 9% - 2% = **+7%** ($140M on $2B)
- Volatility reduction: 18% → 13% = **-5% vol**
- Sharpe ratio: Improved from 0.11 to 0.69
- **Successful risk management without sacrificing equity alpha**

### 2. Worst Case: Failure


**Over-leveraged tactical overlay:**

**Setup:**
- $1B pension fund
- Hired "aggressive" tactical overlay manager
- Mandate: Generate +2-3% alpha through market timing

**Year 1: Disaster**

**Q1:** Bullish equities, bought $200M equity futures (20% overlay)
- Market fell -8%
- **Loss: $16M**

**Q2:** Bearish equities (panic), sold all futures + short $100M
- Market rallied +12%
- Long positions would have made +$24M
- Short position lost +$12M
- **Loss: $36M total**

**Q3:** Bullish again (FOMO), bought $300M futures (30% overlay!)
- Market volatile, ended flat
- Whipsawed by intra-quarter moves
- **Loss: $5M from trading costs**

**Q4:** "Hedging" with short positions after year of losses
- Modest rally +4%
- **Loss: $8M**

**Total Year:**
- Overlay losses: **-$65M** (-6.5% of portfolio)
- vs. policy return: +6%
- **Total underperformance: -12.5%**
- Manager fired, program terminated
- Board sued for breach of fiduciary duty

**Post-mortem:**
- No risk limits enforced (started with ±5%, crept to 30%)
- No stop-losses (held losing positions hoping for reversal)
- Excessive turnover (30 trades, $6M in transaction costs)
- Emotional decision-making (panic, FOMO, revenge trading)
- **Destroyed $65M in 12 months**

---

## Risk Management Rules


### 1. Position Limits


**Hard limits on exposure:**

$$
\begin{align*}
\text{Gross Notional} & \leq 50\% \text{ of NAV} \\
\text{Net Notional} & \leq 20\% \text{ of NAV} \\
\text{Single Position} & \leq 10\% \text{ of NAV} \\
\text{Margin Used} & \leq 10\% \text{ of NAV}
\end{align*}
$$

**Example ($1B portfolio):**
- Max gross notional: $500M total derivative exposure
- Max net notional: $200M directional bet
- Max single position: $100M in one contract type
- Max margin: $100M committed to collateral

### 2. Stop-Loss Rules


**Cut losses quickly:**

**Per position:**
- Stop-loss: -1% of NAV
- If position loses -1%, close immediately
- No exceptions, no "waiting for reversal"

**Aggregate overlay:**
- Monthly loss limit: -0.5% of NAV
- Quarterly loss limit: -1.5% of NAV
- Annual loss limit: -3% of NAV
- **Breach = Program pause, review by Investment Committee**

### 3. Tracking Error Budget


**Control active risk:**

**For passive overlays (rebalancing, hedging):**
- Target tracking error: < 0.5% annually
- Maximum: 1.0% annually
- Measured daily, reported monthly

**For active overlays (TAA):**
- Target tracking error: 1-2% annually
- Maximum: 3.0% annually
- Information ratio must be > 0.5
- **If IR < 0.5 for 12 months, terminate active overlay**

### 4. Liquidity Requirements


**Ensure positions can be unwound:**

**Minimum liquidity standards:**
- Average daily volume > 10× position size
- Bid-ask spread < 0.1% of mid-price
- Can exit entire position in < 3 days
- Multiple counterparties available

**Example:**
- Want to hold $100M S&P 500 futures
- Minimum required: S&P futures trade $1B+ daily ✓
- Bid-ask spread: 0.01% ✓
- Can exit 5000 contracts in 1 day easily ✓
- 10+ dealers make markets ✓
- **Acceptable liquidity**

### 5. Counterparty Risk


**Diversify credit exposure:**

$$
\text{Max Exposure per Counterparty} = \frac{\text{Total Derivatives Exposure}}{N_{\text{counterparties}}} \leq 25\%
$$

**Requirements:**
- Minimum credit rating: A-
- Minimum 4 counterparties
- ISDA and CSA agreements required
- Daily mark-to-market and collateral calls
- Monthly credit review

---

## Real-World Examples


### 1. CalPERS Currency Overlay


**World's largest public pension fund:**

**Program details:**
- $300B+ portfolio
- 50%+ non-US assets
- Systematic currency hedging overlay
- Target: 50% hedge ratio for developed markets

**Implementation:**
- Centralized overlay manager
- Base managers ignore FX completely
- Monthly rebalancing to maintain 50% hedge
- Use forwards only (simple, low cost)

**Results (2015-2020):**
- Reduced FX volatility by 40%
- Hedge cost: ~0.03% annually (very efficient)
- Improved Sharpe ratio of international portfolio
- **Estimated value added: $500M-$1B over 5 years**

### 2. Bridgewater Risk Parity


**Pioneering overlay approach:**

**Structure:**
- Equal risk contribution from each asset class
- Use leverage overlay to amplify low-risk assets (bonds)
- Target: 10-12% volatility across all asset classes

**Overlay mechanism:**
- Bond allocation: 40% of capital, but 100% of risk (using leverage)
- Equity allocation: 30% of capital, 100% of risk (no leverage)
- Commodities: 20%, leverage to 100% risk
- Other: 10%, adjust to 100% risk

**Risk parity formula:**

$$
\text{Leverage}_i = \frac{\text{Target Volatility}}{\text{Asset } i \text{ Volatility}}
$$

**Example:**
- Target portfolio vol: 12%
- Bonds: 5% vol → Leverage 2.4× ($40M becomes $96M exposure via futures)
- Equities: 16% vol → Leverage 0.75× ($30M becomes $22.5M via selling some)
- Result: Each contributes 12% to portfolio risk

**Performance:**
- All-weather performance (diversification works)
- Lower drawdowns than stock-heavy portfolios
- Requires sophisticated overlay management
- **15-20 years: ~10% annual return with lower vol than 60/40**

### 3. Norwegian Oil Fund Equity Overlay


**$1.3 trillion sovereign wealth fund:**

**Challenge:**
- Mandate: 70% equity / 30% bonds
- Cash inflows: $5-10B monthly from oil revenues
- Can't let cash drag returns while deciding allocations

**Overlay solution:**
- Immediately equitize all cash inflows using futures
- Overlay buys equity index futures on day cash arrives
- Over next 30-60 days, gradually invest cash into actual stocks
- Overlay closes futures as cash invested

**Benefits:**
- Zero cash drag (always fully invested)
- Time to optimize stock purchases (no rush)
- Lower market impact (gradual implementation)
- **Estimated benefit: 0.2-0.3% annually** ($2.6-$3.9B per year!)

### 4. University Endowment TAA Overlay


**$15B endowment:**

**Problem:**
- Strategic allocation: 40% equity, 30% bonds, 30% alternatives
- Investment Committee meetings: Quarterly only
- Market moves happen daily, can't adjust quickly

**Overlay implementation:**
- Hired tactical overlay manager
- Authority: ±5% from strategic weights
- Review cycle: Monthly (faster than Investment Committee)
- Instruments: Equity/bond futures only (liquid)

**Example tactical call:**
- December 2018: Market crash (-20% in Q4)
- Overlay manager: Opportunistic, buy into panic
- Increased equity from 40% to 45% using futures
- January-March 2019: Market +20% rebound
- **Overlay gain: 5% × 20% = +1%** ($150M on $15B portfolio)
- Closed overlay position at end of Q1

**5-year results:**
- Win rate: 60% of tactical bets profitable
- Average gain: +0.5% per year after costs
- Sharpe ratio: 1.2 (solid risk-adjusted returns)
- **Total value added: +2.5%** ($375M)

---

## Practical Steps


### 1. Program Design


**Initial setup (3-6 months):**

1. **Needs assessment:**
   - Audit current portfolio structure
   - Identify inefficiencies: unhedged FX, allocation drift, transition costs
   - Quantify opportunity: What could overlay solve?
   - Cost-benefit analysis: Is it worth the complexity?

2. **Mandate definition:**
   - Objective: Risk management, return enhancement, or both?
   - Scope: Currency only? TAA? Transitions?
   - Authority: Limits on positions, leverage, tracking error
   - Governance: Who approves, who monitors, who reports?

3. **Manager selection:**
   - In-house vs. outsource decision
   - If outsource: RFP process, due diligence
   - Check references, review track record
   - Negotiate fees (should be < 0.25% for passive, < 0.75% for active)

4. **Infrastructure setup:**
   - Derivative accounts and ISDA agreements
   - Margin facilities and collateral management
   - Risk and position reporting systems
   - Integration with base managers' reporting

### 2. Launch Phase


**First 90 days:**

**Week 1-2: Data gathering**
- Collect position data from all base managers
- Calculate current exposures: equity, bonds, currency, duration
- Compare to policy targets: Where are the gaps?
- Build baseline: This is what overlay must manage

**Week 3-4: Initial positioning**
- Start conservatively: Close only the biggest gaps
- Example: If 65% equity vs. 60% target, sell $50M futures
- Don't try to fix everything immediately (avoid market impact)
- Document all trades and rationale

**Month 2-3: Ramp up**
- Gradually increase coverage of policy gaps
- Add currency hedges if applicable
- Begin regular rebalancing cycle
- Establish reporting rhythm with stakeholders

**End of Q1: Review**
- How well did overlay achieve policy targets?
- What were the costs?
- Any operational issues?
- Refine processes based on lessons learned

### 3. Ongoing Management


**Daily operations:**

- **Morning:**
  - Review overnight derivative positions and P&L
  - Check margin accounts and collateral levels
  - Assess any corporate actions affecting exposures
  - Monitor market conditions (volatility, liquidity)

- **Afternoon:**
  - Execute any required trades (rebalancing, new hedges)
  - Update risk reports for internal stakeholders
  - Coordinate with base managers on exposure changes
  - Prepare end-of-day reporting

**Weekly operations:**
- Full risk report: positions, exposures, tracking error, costs
- Performance attribution: overlay P&L vs. benchmark
- Base manager exposure updates (get updated holdings)
- Adjust hedges if significant exposure changes

**Monthly operations:**
- Comprehensive performance report for Investment Committee
- Rebalancing analysis: What needs adjustment?
- Execute tactical changes (if active overlay)
- Cost analysis: Transaction costs, management fees, opportunity costs

**Quarterly operations:**
- Full program review with Investment Committee
- Hedge effectiveness testing (for accounting)
- Update policy benchmarks if needed
- Manager evaluation: Should we continue/modify/terminate?

### 4. Performance Evaluation


**Key metrics to track:**

**Policy replication accuracy:**

$$
\text{Tracking Error} = \sqrt{\frac{1}{N}\sum_{i=1}^{N} (R_{\text{portfolio}, i} - R_{\text{policy}, i})^2}
$$

**Target: < 0.5% for passive overlay**

**Cost efficiency:**

$$
\text{Total Overlay Cost} = \text{Mgmt Fee} + \text{Transaction Costs} + \text{Opportunity Costs}
$$

**Benchmark: < 0.15% annually**

**Alpha generation (if active):**

$$
\text{Alpha} = R_{\text{portfolio}} - R_{\text{benchmark}} - \beta (R_{\text{market}} - R_{\text{benchmark}})
$$

$$
\text{Information Ratio} = \frac{\text{Alpha}}{\text{Tracking Error}}
$$

**Target: IR > 0.5**

**Risk-adjusted return:**

$$
\text{Sharpe Ratio} = \frac{R_{\text{portfolio}} - R_f}{\sigma_{\text{portfolio}}}
$$

**Target: > Sharpe of policy benchmark**

### 5. Termination Decision


**When to end the overlay:**

**Terminate if:**
- Costs exceed benefits for 12+ months
- Operational complexity too high (errors, missed trades)
- Base managers can handle exposures themselves
- Leverage/risk controls repeatedly breached
- Better alternatives available (new technologies, ETFs)

**Example termination:**
- Active TAA overlay hired to generate +2% alpha
- After 3 years: Generated +0.5% alpha gross, -0.3% net of fees
- Information ratio: 0.3 (below 0.5 target)
- Transaction costs higher than expected
- **Decision: Terminate, not adding value net of costs**

---

## Final Wisdom


> "Overlay strategies are like the conductor of an orchestra: they don't replace the musicians (base managers), but coordinate them to create harmony. The best overlay programs are nearly invisible—base managers hardly know they exist, but the portfolio stays perfectly in tune with policy. When overlays become the main show, demanding attention and resources, something has gone wrong. Keep overlays simple, focused, and humble. Their job is to make everyone else's job easier, not to be a hero."

**Key to success:**

- Clear objectives (what problem are you solving?)
- Simple implementation (liquid derivatives, vanilla structures)
- Rigorous limits (position size, leverage, tracking error)
- Excellent communication (with base managers and oversight)
- Humble expectations (0.5-1% value add is success, not 5%)
- Regular evaluation (measure costs vs. benefits annually)
- Know when to stop (if not adding value, terminate)
