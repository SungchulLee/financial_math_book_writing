# Master Strategy Comparison Table

**A comprehensive reference guide comparing all volatility trading strategies side-by-side.**

---

## How to Use This Guide

This document helps you:

1. **Compare strategies** across all dimensions
2. **Choose the right strategy** for your situation
3. **Understand relationships** between strategies
4. **Quick reference** for key characteristics

**Navigate to:**

- [Greek Profiles](#greek-profiles) - Theta, Vega, Gamma, Delta
- [Complexity & Accessibility](#complexity-and-accessibility) - Who can trade each
- [Market Conditions](#best-market-conditions) - When to use each
- [Risk/Reward](#risk-reward-profiles) - Profit potential vs. risk
- [Capital & Time](#capital-and-time-requirements) - Resources needed
- [Decision Framework](#decision-framework) - Which strategy to choose
- [Quick Reference Matrix](#quick-reference-matrix) - At-a-glance comparison

---

## Greek Profiles

**How each strategy positions you across the four main Greeks:**

| Strategy | Theta | Vega | Gamma | Delta | Hedging |
|----------|-------|------|-------|-------|---------|
| **Delta Hedging** | - | + | + | 0 | Constant |
| **Straddles (Long)** | - - | + + | + + | 0 | None |
| **Gamma Scalping** | - | + + | + + | 0 | Continuous |
| **Vega Trading** | - | + + | + | 0 | Periodic |
| **Smile/Skew** | - | ± | ± | 0 | Periodic |
| **Calendar Spreads** | **+** | + | ± | 0 | Rare |
| **Dispersion (Long)** | - | + | + | 0 | Continuous (all) |
| **Convertible Arb** | ± | + | + | 0 | Constant |
| **Variance Swaps** | **0** | **0** | **0** | 0 | **None** |
| **Theta/Carry (Short Vol)** | **+ +** | - - | - - | 0 | None/Rare |
| **Static Hedging** | - | + | + | 0 | **None (by design)** |

**Legend:**

- `++` = Very positive exposure
- `+` = Positive exposure
- `0` = Neutral / Hedged away
- `±` = Mixed / Depends on structure
- `-` = Negative exposure (pay)
- `--` = Very negative exposure

**Key Insights:**

- **Calendar Spreads unique:** Only major strategy with positive theta AND positive vega
- **Variance Swaps pure:** All Greeks hedged away (pure variance exposure)
- **Theta/Carry opposite:** Positive theta but negative gamma (fundamental trade-off)
- **Static Hedging philosophy:** Accept Greek drift, avoid rebalancing costs

---

## Complexity and Accessibility

**Who can trade each strategy and what skills are needed:**

| Strategy | Complexity | Retail Access | Institutional | Key Skills Required |
|----------|-----------|---------------|---------------|---------------------|
| **Delta Hedging** | Medium | Yes* | Yes | Hedging discipline, Greeks understanding |
| **Straddles** | **Low** | **Yes** | Yes | Basic options, event timing |
| **Gamma Scalping** | High | Difficult | Yes | Continuous hedging, cost management |
| **Vega Trading** | Medium-High | Yes* | Yes | IV analysis, hedging, timing |
| **Smile/Skew** | High | Difficult | Yes | Multi-leg options, Greeks across strikes |
| **Calendar Spreads** | Medium | **Yes** | Yes | Term structure, time management |
| **Dispersion** | Very High | No | Yes | Multiple assets, complex hedging |
| **Convertible Arb** | Very High | No | Yes | Credit analysis, multi-factor risk |
| **Variance Swaps** | Low (trading) | **No** | **Yes** | Access to dealers, institutional size |
| **Theta/Carry** | Medium-High | Yes* | Yes | Risk management, discipline, stops |
| **Static Hedging** | Medium | Yes | Yes | Upfront structuring, model knowledge |

**\*Yes but:** Retail can access but requires discipline and sophistication

**Accessibility Ranking (Easiest to Hardest):**

1. **Straddles** - Buy call + put, hold (retail-friendly)
2. **Calendar Spreads** - Two options, rare rebalancing
3. **Delta Hedging** - Foundational skill for all others
4. **Static Hedging** - Set once, forget (if know how to structure)
5. **Vega Trading** - Single option + hedge
6. **Theta/Carry** - Requires extreme discipline
7. **Gamma Scalping** - Continuous rebalancing burden
8. **Smile/Skew** - Multi-leg complexity
9. **Convertible Arb** - Need bond access, credit skills
10. **Dispersion** - Many positions simultaneously
11. **Variance Swaps** - Institutional OTC only

---

## Best Market Conditions

**When each strategy works best:**

| Strategy | VIX Level | Market State | Time Horizon | Event Timing |
|----------|-----------|--------------|--------------|--------------|
| **Delta Hedging** | Any | Any | Any | Any (foundational) |
| **Straddles (Long)** | Low (< 15) | Pre-event | Short (< 1 month) | **Before binary event** |
| **Gamma Scalping** | Any | Volatile/Moving | Medium (1-3 months) | Avoid events |
| **Vega Trading** | Any | IV expected to change | Short-Medium | Capture IV moves |
| **Smile/Skew** | Extreme skew | Mean reversion | Short-Medium | Post-panic or pre-event |
| **Calendar Spreads** | Normal (15-25) | **Range-bound** | Medium (2-3 months) | Between events |
| **Dispersion (Long)** | High corr (> 70%) | Post-crisis | Medium | Correlation spike reverting |
| **Convertible Arb** | High spreads | Dislocated | Long (6+ months) | Market stress |
| **Variance Swaps** | Any | Any (if available) | Medium | Pure vol view |
| **Theta/Carry (Short Vol)** | **High (> 25)** | **Post-event** | Short (< 45 days) | **After vol spike** |
| **Static Hedging** | Low vol | Stable | **Long (6+ months)** | Long-dated hedges |

**Best Opportunities by Market State:**

**High VIX (> 30) - Crisis/Panic:**

- Theta/Carry (short vol from elevated levels) ✓✓
- Dispersion (long - wait for correlation reversion)
- Straddles (long - but IV expensive, wait for entry)

**Normal VIX (15-25) - Steady State:**

- Calendar Spreads ✓✓✓ (collect theta differential)
- Gamma Scalping (steady vol trading)
- Vega Trading (tactical IV plays)
- Smile/Skew (relative value)

**Low VIX (< 15) - Complacent:**

- Straddles (long - options cheap) ✓✓✓
- Variance Swaps (long - cheap entry)
- Avoid short vol! (risk >> reward)

**Range-Bound Markets:**

- Calendar Spreads ✓✓✓
- Theta/Carry (Iron Condors)
- Static Hedging (low rebalancing need)

**Volatile/Trending Markets:**

- Gamma Scalping ✓✓✓
- Avoid Theta/Carry (steamroller coming)

---

## Risk/Reward Profiles

**Profit potential, loss potential, and win rates:**

| Strategy | Max Loss | Max Profit | Win Rate | Best/Worst | Risk/Reward |
|----------|----------|------------|----------|------------|-------------|
| **Delta Hedging** | Tracking error | N/A (hedged) | N/A | N/A | Risk mgmt tool |
| **Straddles (Long)** | **Premium paid** | **Unlimited** | Low (30-40%) | Large moves / No move | Asymmetric (good) |
| **Gamma Scalping** | Theta paid | Rebalancing profits | Medium (50-60%) | Volatile / Calm | Balanced |
| **Vega Trading** | Theta + adverse IV | IV change profits | Medium (50-60%) | IV spike / IV stable | Balanced |
| **Smile/Skew** | Net debit | Limited | Medium (50-60%) | Skew normalizes / Skew diverges | Moderate |
| **Calendar Spreads** | **Net debit** | **Limited** | High (60-70%) | Stable / Large move | Moderate |
| **Dispersion (Long)** | Net premium | Correlation profits | Medium (50%) | Low corr / High corr | Balanced |
| **Convertible Arb** | Credit loss | Multiple sources | Medium (55-65%) | All factors work / Credit crisis | Moderate |
| **Variance Swaps** | Unlimited (if short) | Unlimited (if long) | Depends | Realized ≠ implied / Correct forecast | Symmetric |
| **Theta/Carry (Short)** | **UNLIMITED** | **Premium received** | High (70-80%) | Calm / Large move | Asymmetric (bad) |
| **Static Hedging** | Tracking error | Cost savings | N/A | Long horizon / Short horizon | Depends |

**Risk Profile Categories:**

**Limited Risk, Limited Reward:**

- Calendar Spreads
- Smile/Skew (spreads)
- Iron Condors (theta/carry variant)

**Limited Risk, Unlimited Reward:**

- Straddles (long)
- Variance Swaps (long)
- Gamma Scalping

**Unlimited Risk, Limited Reward:**

- Short Straddles ⚠️
- Naked options ⚠️
- Most theta/carry trades ⚠️

**Unlimited Risk, Unlimited Reward:**

- Variance Swaps (short)
- Unhedged exotics

---

## Capital and Time Requirements

**Resources needed to execute each strategy:**

| Strategy | Capital Need | Margin Need | Time Commitment | Monitoring |
|----------|--------------|-------------|-----------------|------------|
| **Delta Hedging** | Medium | Medium | Continuous | High (constant) |
| **Straddles** | **Low** (premium) | Low | **Minimal** | Low (buy & hold) |
| **Gamma Scalping** | High (hedge + option) | Medium-High | Continuous | Very High |
| **Vega Trading** | Medium | Medium | Periodic | Medium |
| **Smile/Skew** | Medium | Medium-High | Periodic | Medium |
| **Calendar Spreads** | Low-Medium | Low | Periodic | Low-Medium |
| **Dispersion** | **Very High** | **Very High** | Continuous | Very High |
| **Convertible Arb** | **Very High** | **Very High** | Daily | High |
| **Variance Swaps** | **Very High** ($1M+ min) | Medium | **None** | Minimal |
| **Theta/Carry** | Medium | **High** (if naked) | Daily | High |
| **Static Hedging** | Low-Medium | Low-Medium | **Minimal** | Minimal |

**Capital Efficiency (Best to Worst):**

1. **Variance Swaps** - Pure exposure, no rebalancing
2. **Straddles** - Just premium, no hedging
3. **Calendar Spreads** - Small net debit
4. **Static Hedging** - One-time deployment
5. Vega Trading - Option + occasional hedge
6. Gamma Scalping - Need hedge capital
7. Dispersion - Many positions simultaneously
8. Convertible Arb - Bonds + hedges + complexity

**Time Commitment (Least to Most):**

1. **Straddles** (set and forget)
2. **Variance Swaps** (wait for settlement)
3. **Static Hedging** (by design)
4. **Calendar Spreads** (monthly review)
5. Vega Trading (watch IV)
6. Theta/Carry (daily monitoring)
7. **Gamma Scalping** (continuous rebalancing)
8. **Dispersion** (multiple assets to manage)

---

## Primary Profit Sources

**Where the P&L comes from:**

| Strategy | Profit Source 1 | Profit Source 2 | Profit Source 3 | Profit Source 4 |
|----------|----------------|-----------------|-----------------|-----------------|
| **Delta Hedging** | None (hedged) | - | - | - |
| **Straddles** | Large price move | Early IV spike | - | - |
| **Gamma Scalping** | **Rebalancing** (½Γ(δS)²) | Realized > Implied | - | - |
| **Vega Trading** | **IV changes** (Vega·δσ) | Some gamma | - | - |
| **Smile/Skew** | **Skew changes** (rel. IV) | Time decay | Gamma | - |
| **Calendar Spreads** | **Theta differential** | Vega (back month) | Term structure | - |
| **Dispersion** | **Correlation changes** | Some gamma | Some vega | - |
| **Convertible Arb** | **Gamma scalping** | **Credit tightening** | **Coupon income** | Cheapness capture |
| **Variance Swaps** | **Pure variance** (realized vs. strike) | - | - | - |
| **Theta/Carry** | **Theta collection** | Vol staying low | IV crush | - |
| **Static Hedging** | **Cost savings** (no rebalancing) | - | - | - |

**Unique Profit Sources:**

- **Calendar Spreads:** ONLY strategy with positive theta AND positive vega
- **Convertible Arb:** FOUR profit sources (most diversified)
- **Variance Swaps:** Cleanest (pure variance, no noise)
- **Theta/Carry:** Pure time decay (opposite of most)
- **Static Hedging:** Saves costs rather than generates profits

---

## Strategy Relationships

**How strategies relate to each other:**

### Evolutionary Relationships

```
Basic → Refined → Pure

Straddles (raw vol bet)
    ↓ (add delta hedging)
Gamma Scalping (hedged vol bet)
    ↓ (remove friction)
Variance Swaps (pure variance)
```

```
Vega Trading (single maturity)
    ↓ (add time dimension)
Calendar Spreads (multiple maturities)
```

```
Vega Trading (single strike)
    ↓ (add strike dimension)
Smile/Skew (multiple strikes)
```

### Complementary Pairs

**Can combine for enhanced strategies:**

- **Calendar + Skew:** Calendar spread across different skew points
- **Gamma Scalping + Vega:** Both profit from volatility different ways
- **Dispersion + Skew:** Trade correlation AND shape
- **Convertible + Credit:** Bond arbitrage with gamma scalping

### Substitutes

**Different ways to express similar views:**

**Want long volatility:**

- Straddles (simple, unhedged)
- Gamma Scalping (complex, hedged)
- Variance Swaps (pure, institutional)

**Want positive carry:**

- Calendar Spreads (safe, defined risk)
- Iron Condors (safe, defined risk)
- Short Straddles (risky, unlimited loss)

**Want to trade term structure:**

- Calendar Spreads (options-based)
- VIX futures curve (futures-based)

---

## Decision Framework

**How to choose the right strategy:**

### Step 1: What Do You Want to Trade?

```
START HERE
    |
    ├─ Market Direction? 
    │   └─> Use underlying or directional options (not these strategies)
    |
    ├─ Volatility LEVEL (high vs. low)?
    │   ├─> Realized vol → Gamma Scalping or Variance Swaps
    │   └─> Implied vol → Vega Trading
    |
    ├─ Volatility SHAPE (across strikes)?
    │   └─> Smile/Skew Trading
    |
    ├─ Volatility TIME (term structure)?
    │   └─> Calendar Spreads
    |
    ├─ Correlation (multi-asset)?
    │   └─> Dispersion Trading
    |
    ├─ Want POSITIVE CARRY (collect theta)?
    │   ├─> Safe: Calendar Spreads, Iron Condors
    │   └─> Risky: Short Straddles, Naked Options
    |
    ├─ Simple bet on BIG MOVE?
    │   └─> Straddles/Strangles
    |
    └─ Multiple factors (credit + vol)?
        └─> Convertible Arbitrage
```

### Step 2: Check Your Constraints

**Do you have:**

- [ ] Retail account? → Straddles, Calendars, some Vega
- [ ] Institutional access? → All strategies available
- [ ] High capital ($1M+)? → Variance Swaps, Dispersion, Convertibles
- [ ] Low capital (< $10K)? → Straddles, Calendars only
- [ ] Can monitor continuously? → Gamma Scalping, Dispersion
- [ ] Want passive? → Straddles, Variance Swaps, Static Hedging
- [ ] Discipline for stops? → Theta/Carry trades
- [ ] No discipline? → Avoid Theta/Carry!

### Step 3: Match to Market Conditions

**Current market:**

**VIX < 15 (Low Vol):**

→ Long Straddles, Long Variance Swaps
→ AVOID short vol!

**VIX 15-25 (Normal):**

→ Calendar Spreads, Gamma Scalping, Vega Trading
→ Most strategies work

**VIX > 25 (Elevated):**

→ Short vol (theta/carry), wait for correlation reversion
→ Be cautious with long vol (expensive)

**Range-bound:**

→ Calendars, Iron Condors, Theta collection

**Trending:**

→ Gamma Scalping
→ Avoid theta collection

### Step 4: Risk Tolerance Check

**Your risk appetite:**

**Conservative (limited loss):**

✓ Calendar Spreads
✓ Iron Condors
✓ Protective Puts (static hedging)
✗ Short Straddles
✗ Naked options

**Moderate:**

✓ Gamma Scalping (hedged)
✓ Vega Trading (hedged)
✓ Smile/Skew (spreads)
✓ Long Straddles (limited loss)

**Aggressive:**

✓ Dispersion (complex)
✓ Convertibles (multi-factor)
✓ Variance Swaps (pure exposure)
⚠️ Short vol (ONLY with discipline!)

---

## Quick Reference Matrix

**At-a-glance comparison:**

### By Primary Characteristic

**Best for Beginners:**

1. Straddles (simplest)
2. Calendar Spreads (straightforward)
3. Delta Hedging (foundational)

**Best for Professionals:**

1. Dispersion (complex, institutional)
2. Convertible Arb (multi-factor)
3. Gamma Scalping (continuous work)

**Best Risk/Reward:**

1. Straddles (limited loss, unlimited profit)
2. Variance Swaps (pure exposure if right)
3. Calendar Spreads (positive theta + vega)

**Most Dangerous:**

1. Short Straddles (unlimited loss) ⚠️⚠️⚠️
2. Naked short options ⚠️⚠️⚠️
3. Theta/carry without stops ⚠️⚠️

**Most Cost-Efficient:**

1. Variance Swaps (no rebalancing)
2. Static Hedging (one-time cost)
3. Straddles (no hedging needed)

**Requires Most Capital:**

1. Dispersion (many positions)
2. Convertible Arb (bonds + hedges)
3. Variance Swaps (high notional)

### By Greek Exposure

**Want Positive Theta:**

- Calendar Spreads ✓✓
- Theta/Carry strategies ✓✓
- (Everything else pays theta)

**Want Long Vega:**

- Gamma Scalping ✓✓
- Vega Trading ✓✓
- Straddles ✓✓
- Most strategies (except short vol)

**Want Long Gamma:**

- Gamma Scalping ✓✓✓ (core focus)
- Straddles ✓✓
- Most long vol strategies ✓

**Want Delta-Neutral:**

- All strategies after hedging
- (Core principle across board)

### By Time Horizon

**Short-term (< 1 month):**

- Straddles (events)
- Theta/Carry (rapid decay)
- Vega (IV changes)

**Medium-term (1-6 months):**

- Gamma Scalping
- Calendar Spreads
- Smile/Skew
- Dispersion

**Long-term (6+ months):**

- Static Hedging
- Convertible Arb
- Long-dated protective puts

---

## Common Strategy Combinations

**Strategies that work well together:**

### Portfolio Approaches

**Conservative Vol Portfolio:**

- 40% Calendar Spreads (positive carry)
- 40% Iron Condors (safe carry)
- 20% Long Straddles on cheap opportunities

**Aggressive Vol Portfolio:**

- 30% Gamma Scalping (active)
- 30% Dispersion (correlation)
- 20% Vega Trading (tactical)
- 20% Convertibles (multi-factor)

**Balanced Approach:**

- 30% Calendar Spreads (steady income)
- 30% Gamma Scalping (vol trading)
- 20% Smile/Skew (relative value)
- 20% Cash (opportunity fund)

### Complementary Strategies

**Event Trading:**

- Before: Long Straddles (capture move)
- After: Short vol (IV crush)

**Correlation Trading:**

- Crisis: Wait (correlation → 1)
- Recovery: Long Dispersion (correlation ↓)

**Term Structure:**

- Front month: Vega trading (IV changes)
- Back month: Static hedge (low rebalancing)

---

## Common Mistakes by Strategy

**What NOT to do:**

| Strategy | Common Mistake | Why It Fails | Fix |
|----------|---------------|--------------|-----|
| **Straddles** | Hold to zero | Theta bleeds daily | Exit at 50% profit or IV spike |
| **Gamma Scalping** | Over-rebalancing | Transaction costs overwhelm | Optimize frequency |
| **Vega Trading** | Ignore theta | Time decay eats profits | Short-dated options |
| **Calendar Spreads** | Chase last dollar | Stock moves kill P&L | Exit at 50% of max |
| **Theta/Carry** | Over-size | One loss wipes out months | Position size strictly |
| **Short Straddles** | No stop loss | Unlimited loss risk | ALWAYS have stops |
| **Dispersion** | Ignore single-stock risk | Earnings blow up position | Diversify, manage events |
| **Static Hedging** | Wrong model | Hedge doesn't work | Validate assumptions |

---

## Strategy Selection Checklist

**Before entering any strategy, verify:**

### General Checklist

- [ ] Do I understand the strategy completely?
- [ ] Have I read the full chapter?
- [ ] Do I know the max loss?
- [ ] Do I know the profit source?
- [ ] What's my exit plan?
- [ ] What's my stop loss?
- [ ] Can I afford the time commitment?
- [ ] Do I have the required capital?
- [ ] Is this the right market environment?

### Strategy-Specific

**For Theta/Carry (Short Vol):**

- [ ] Position size < 2% of portfolio?
- [ ] Stop loss defined and honored?
- [ ] No events in next 30 days?
- [ ] Using defined risk structure?
- [ ] VIX elevated (> 20)?

**For Gamma Scalping:**

- [ ] Can rebalance frequently?
- [ ] Transaction costs acceptable?
- [ ] Time horizon 1-3 months?
- [ ] Volatility expected?

**For Straddles:**

- [ ] Event identified?
- [ ] IV low (< 20th percentile)?
- [ ] Time to event < 1 month?
- [ ] Max loss acceptable (premium)?
- [ ] Exit plan for IV spike?

---

## Glossary of Comparison Terms

**Key terms used in this comparison:**

**Greeks:**

- **Theta:** Time decay ($ per day)
- **Vega:** IV sensitivity ($ per 1% IV change)
- **Gamma:** Delta change rate (curvature)
- **Delta:** Directional exposure ($ per $1 move)

**Hedging:**

- **Dynamic:** Continuous rebalancing
- **Static:** No rebalancing
- **Semi-static:** Rare rebalancing

**Complexity:**

- **Low:** 1-2 instruments, simple logic
- **Medium:** Multiple instruments or frequent adjustments
- **High:** Many instruments, constant management
- **Very High:** Institutional-only, extreme complexity

**Capital Need:**

- **Low:** < $10K
- **Medium:** $10K - $100K
- **High:** $100K - $1M
- **Very High:** > $1M

**Time Commitment:**

- **Minimal:** Check weekly
- **Low:** Check daily
- **Medium:** Adjust weekly
- **High:** Monitor/adjust daily
- **Continuous:** Real-time monitoring

---

## Further Reading

**For each strategy, see the full chapter:**

1. [Delta Hedging](delta_hedging.md) - Foundation for all strategies
2. [Straddles and Strangles](straddles_strangles.md) - Simple volatility bets
3. [Gamma Scalping](gamma_scalping.md) - Active volatility trading
4. [Vega Trading](vega_trading.md) - Implied volatility speculation
5. [Volatility Smile and Skew](vol_smile_skew_trading.md) - Cross-strike patterns
6. [Calendar Spreads](calendar_spreads.md) - Term structure trading
7. [Dispersion Trading](dispersion_trading.md) - Correlation strategies
8. [Convertible Arbitrage](convertible_bond_arbitrage.md) - Multi-factor approaches
9. [Variance Swaps](variance_swaps.md) - Pure variance exposure
10. [Theta and Carry](theta_and_carry.md) - Time decay strategies
11. [Static Hedging](static_hedging.md) - Alternative hedging approaches

---

## The Big Picture

**What this comparison reveals:**

### Universal Principles

**1. The Theta-Gamma Trade-off**

- Can't have positive theta AND positive gamma
- Must choose: collect carry OR benefit from movement
- Exception: Calendar Spreads (different maturities allow both!)

**2. The Cost-Accuracy Trade-off**

- Dynamic hedging: high cost, low tracking error
- Static hedging: low cost, high tracking error
- Choose based on which cost dominates

**3. The Complexity Spectrum**

- Simple (Straddles) → Complex (Dispersion)
- More complex ≠ better returns
- Choose based on skill and resources

**4. The Volatility Risk Premium**

- IV > Realized Vol (historically)
- Short vol earns premium (but with tail risk)
- Long vol pays premium (but limited loss)

### Strategy Families

**The Hedging Family:**

- Delta Hedging (foundation)
- Gamma Scalping (refined)
- Static Hedging (alternative)
- All about removing directional risk

**The Carry Family:**

- Calendar Spreads (safe carry)
- Iron Condors (defined risk)
- Short Straddles (risky carry)
- All about collecting theta

**The Pure Exposure Family:**

- Straddles (raw vol bet)
- Variance Swaps (pure variance)
- Gamma Scalping (refined vol bet)
- All about volatility level

**The Relative Value Family:**

- Smile/Skew (across strikes)
- Calendar Spreads (across time)
- Dispersion (across assets)
- All about relationships

### Career Paths

**Path 1: Volatility Buyer (Theta Payer)**

- Start: Straddles
- Advance: Gamma Scalping
- Master: Variance Swaps (long)
- Profile: Pay theta, profit from movement

**Path 2: Volatility Seller (Theta Collector)**

- Start: Calendar Spreads
- Advance: Iron Condors
- Expert: Systematic short vol programs
- Profile: Collect theta, manage gamma risk

**Path 3: Relative Value Trader**

- Start: Calendar Spreads
- Advance: Smile/Skew
- Master: Dispersion
- Profile: Trade relationships, not levels

**Path 4: Multi-Strategy Professional**

- Foundation: Delta Hedging + Gamma Scalping
- Add: Vega + Calendars + Skew
- Master: Dispersion + Convertibles
- Profile: Use right tool for each opportunity

---

## Final Wisdom

**Choosing the right strategy:**

> "There is no 'best' strategy - only the right strategy for your situation, skills, capital, and market conditions. Master the fundamentals (Delta Hedging, Straddles, Gamma Scalping) before attempting advanced strategies (Dispersion, Convertibles). Understand the trade-offs (theta vs. gamma, cost vs. accuracy). And above all: manage risk obsessively. The best strategy executed with poor risk management will destroy you. A simple strategy executed with excellent risk management will succeed."

**The progression:**

1. Learn the basics (Straddles, Delta Hedging)
2. Master one strategy deeply (Gamma Scalping or Calendars)
3. Add complementary strategies (Vega, Skew)
4. Build systematic approach (combinations)
5. Never stop learning (markets evolve)

**The essential truth:**

- **All strategies are variations on delta hedging + options**
- **All face the theta-gamma trade-off**
- **All require discipline and risk management**
- **All work in some markets, fail in others**
- **Choose wisely, execute flawlessly, manage risk obsessively**

---

## Quick Decision Tool

**"I want to..."**

- **Make a simple vol bet** → Straddles
- **Trade volatility actively** → Gamma Scalping
- **Get clean variance exposure** → Variance Swaps
- **Collect steady income** → Calendar Spreads or Iron Condors
- **Trade the skew** → Smile/Skew strategies
- **Trade correlation** → Dispersion
- **Get institutional access** → Variance Swaps or Convertibles
- **Start with basics** → Straddles then Delta Hedging
- **Avoid rebalancing** → Static Hedging or Variance Swaps
- **Trade term structure** → Calendar Spreads

**"The market is..."**

- **Pre-event** → Long Straddles
- **Post-event** → Short vol (theta/carry)
- **Range-bound** → Calendar Spreads
- **Volatile** → Gamma Scalping
- **Low VIX** → Long Straddles, Long Variance
- **High VIX** → Short vol, Calendars
- **Correlation spike** → Wait, then Long Dispersion
- **Steep skew** → Skew flattening trades

**"I am..."**

- **A beginner** → Straddles, Calendars
- **Intermediate** → Gamma Scalping, Vega Trading
- **Advanced** → Dispersion, Convertibles
- **Retail trader** → Straddles, Calendars, some Gamma
- **Institution** → All strategies available
- **Risk-averse** → Calendars, Iron Condors
- **Risk-seeking** → Dispersion, Convertibles (with skill!)

---

## Conclusion

**You now have a complete toolkit:**

✓ **11 strategies** covering all dimensions of volatility trading

✓ **Complete comparison** across all relevant factors

✓ **Decision framework** for choosing the right strategy

✓ **Risk awareness** for each approach

**Use this guide as:**

- Reference when considering trades
- Learning roadmap (start simple → advance)
- Strategy selection tool
- Risk checklist

**Remember:**

- No strategy works all the time
- Risk management is paramount
- Start simple, master fundamentals
- Build complexity only with skill

**Good luck, and trade wisely!** 🎯📊
