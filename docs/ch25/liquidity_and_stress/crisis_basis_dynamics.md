# Crisis Basis Dynamics


**Crisis basis dynamics** describe the breakdown of normal price relationships between cash and derivative instruments during stress, as funding constraints, forced liquidations, and balance sheet pressures create massive dislocations and arbitrage opportunities that are impossible to exploit.

---

## The Core Insight


**The fundamental idea:**

- Normal times: Cash ≈ Futures ≈ Swaps (basis small)
- Crisis: Basis explodes (100s of bps)
- Causes: Funding stress, forced selling, dealer constraints
- "Arbitrage" appears but can't be exploited (no capital)
- Basis widens before normalizing
- Massive P&L swings for existing positions

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/crisis_basis.png?raw=true" alt="crisis_basis" width="700">
</p>
**Figure 1:** Time series of cash-futures basis and credit-CDS basis during 2008 and 2020 showing dramatic widening to 200-500 bps as normal relationships broke down, creating "arbitrage" opportunities that were unexploitable due to funding and balance sheet constraints.

**You're essentially asking: "Why do price relationships break during crises, and what are the trading implications?"**

---

## What Is Crisis Basis?


### 1. Normal Basis Relationships


**Pre-crisis equilibrium:**

**Treasury basis:**

$$
\text{Futures} \approx \text{Cash} \times \text{CF} + \text{Carry}
$$

- Net basis: 5-15 ticks
- Stable, predictable
- Converges to delivery

**Credit basis (CDS-bond):**

$$
\text{CDS Spread} \approx \text{Bond Spread} - \text{Swap Spread}
$$

- Basis: ±10-30 bps
- Mean-reverting
- Small arbitrage opportunities

**Swap spread:**

$$
\text{Swap Rate} \approx \text{Treasury Yield} + \text{Spread}
$$

- Spread: 20-50 bps (positive)
- Stable relationship
- Reflects credit and liquidity

### 2. Crisis Breakdown


**Stress dynamics:**

**Phase 1: Warning**
- Basis widens 2-3×
- Example: 15 ticks → 45 ticks
- Funding pressures emerge

**Phase 2: Dislocation**
- Basis widens 5-10×
- Example: 15 ticks → 100 ticks
- Arbitrageurs stress-tested

**Phase 3: Explosion**
- Basis widens 20-50×
- Example: 15 ticks → 300 ticks
- Arbitrageurs liquidating (forced)

**Phase 4: Seizure**
- Basis unmeasurable (no trades)
- Markets frozen
- Only distressed transactions

### 3. Why Basis Explodes


**Funding liquidity crisis:**

- Repo market seizes
- Can't finance long legs
- Haircuts increase dramatically
- Forced deleveraging

**Balance sheet constraints:**

- Dealer SLR binding
- Can't intermediate
- Withdraw from market-making
- Spreads blow out

**Forced liquidations:**

- Margin calls cascade
- Sell liquid instruments (futures)
- Hold illiquid (cash bonds)
- Basis widens

**Flight to quality:**

- Everyone wants cash, Treasuries
- Sell everything else
- Differential selling pressure
- Basis dislocates

### 4. Treasury Basis in Crisis


**2008 Financial Crisis:**

**Normal (2007):**
- Net basis: 5-10 ticks
- CTD repo: GC rate

**Crisis (Oct 2008):**
- Net basis: 200-300 ticks (20-30× wider!)
- CTD repo: 400 bps below GC (super special)
- Basis traders crushed

**Cause:**
- Lehman bankruptcy
- Funding dried up
- Balance sheets full
- Forced liquidations

**2020 COVID Crisis:**

**Normal (Feb 2020):**
- Net basis: 10-15 ticks
- CTD repo: 50 bps below GC

**Crisis (March 2020):**
- Net basis: 100-150 ticks (10× wider!)
- CTD repo: 300 bps below GC
- Even Treasuries illiquid

**Cause:**
- Dash for cash
- Dealer constraints (SLR)
- Treasury selling
- Funding stress

### 5. Credit Basis in Crisis


**CDS-bond basis:**

$$
\text{Basis} = \text{CDS Spread} - \text{Bond Spread}
$$

**Normal (2007):**
- Basis: ±20 bps
- CDS ≈ Bond spread

**Crisis (2008):**
- Basis: -200 to -500 bps (negative!)
- CDS much cheaper than bonds

**Why negative?**
- Bonds can't be sold (no bids)
- CDS market still functioning
- Short protection via CDS much cheaper
- Reflects selling pressure on cash bonds

**Example:**
- Bond spread: 800 bps
- CDS spread: 400 bps
- **Basis: -400 bps**
- "Arbitrage": Buy bond (800 bps yield), buy CDS protection (400 bps cost), net = 400 bps
- **But**: Can't finance bond (repo unavailable), can't exploit

### 6. Swap Spread in Crisis


**Interest rate swap spread:**

$$
\text{Swap Spread} = \text{Swap Rate} - \text{Treasury Yield}
$$

**Normal:**
- Swap spread: +20 to +50 bps
- Swaps trade above Treasuries (credit risk)

**Crisis (2008, 2020):**
- Swap spread: -50 to -100 bps (negative!)
- Swaps trade BELOW Treasuries

**Why negative?**
- Treasury selling (dash for cash)
- Dealers can't intermediate Treasuries (balance sheet)
- But can intermediate swaps (off-balance-sheet)
- Treasury yields spike relative to swaps

### 7. FX Basis in Crisis


**Cross-currency basis:**

$$
\text{Basis} = \text{FX Swap Rate} - \text{Covered Interest Parity}
$$

**Normal:**
- Basis: ±5-10 bps
- CIP holds approximately

**Crisis:**
- Basis: -100 to -300 bps (massive deviation!)
- Reflects USD funding shortage

**Example (EUR/USD):**
- EUR borrowing: 2.0%
- USD borrowing: 1.5%
- FX swap: +200 bps premium for USD
- **Basis: -200 bps (expensive to get USD)**

**Why?**
- Global dollar shortage
- Everyone needs USD funding
- Limited supply (Fed, US banks)
- FX swap market dislocated

---

## Trading Crisis Basis


### 1. Long Basis Trade (Normal)


**Pre-crisis setup:**

- Long futures
- Short cash
- Capture basis convergence

**Example:**
- Futures: 120-00
- Cash: 118-00
- CF: 0.98
- Net basis: +0.30 (rich)
- Short basis trade

**Crisis impact:**
- Net basis widens: 0.30 → 2.00 (6× wider!)
- Futures sold more (liquid)
- Cash held (illiquid)
- **Mark-to-market loss: -1.70**

**Forced to exit:**
- Margin call
- Sell futures (buy back), sell cash
- Realize loss
- **Classic crisis casualty**

### 2. Short Basis Trade (Crisis)


**Crisis entry:**

- Basis exploded to 2.00 (very rich)
- Short futures, long cash
- Bet on normalization

**Challenge:**
- Need repo funding for cash
- Repo unavailable or expensive
- Can't hold position
- **Thesis correct but can't implement**

### 3. Credit Basis Trade


**Negative basis opportunity:**

**Setup (2008):**
- Bond: 800 bps spread
- CDS: 400 bps spread
- Basis: -400 bps

**Trade:**
- Buy bond (earn 800 bps)
- Buy CDS protection (pay 400 bps)
- Net: 400 bps carry

**Problem:**
- Can't finance bond (repo frozen)
- Need 100% cash upfront
- Huge capital requirement
- **Unexploitable for most**

**Only possible for:**
- Large asset managers (own cash)
- Sovereign wealth funds
- Patient capital

### 4. Swap Spread Trade


**Negative swap spread:**

**Setup (2020):**
- 10Y Treasury: 0.70%
- 10Y Swap: 0.50%
- Swap spread: -20 bps (negative!)

**"Arbitrage":**
- Receive fixed in swap (0.50%)
- Buy Treasury (yield 0.70%)
- Net: +20 bps

**Problem:**
- Need to finance Treasury (repo)
- Repo expensive or unavailable
- Carry eats profit
- **Not risk-free**

### 5. FX Basis Trade


**USD funding shortage:**

**Setup (2008):**
- Borrow EUR at 3%
- Lend USD at 2%
- FX basis: -200 bps (USD premium)

**Trade:**
- Borrow EUR
- Swap to USD via FX swap
- Lend USD
- Unwind at maturity

**P&L:**
- Earn: 2% (USD lending)
- Pay: 3% (EUR borrowing)
- FX swap cost: -200 bps
- **Net: -300 bps (loss!)**

**But:**
- If you HAVE EUR cash (no borrow cost)
- Swap to USD via FX swap (-200 bps)
- Lend USD (2%)
- **Net: +200 bps (profit from providing USD liquidity)**

### 6. Basis Unwind


**Existing position caught:**

**Pre-crisis:**
- Short Treasury basis (profitable trade)
- Small MTM swings (±0.05)

**Crisis:**
- Basis widens dramatically (explodes 10×)
- MTM loss large
- Margin calls
- **Forced to unwind at worst time**

**Outcome:**
- Realize loss (convergence thesis correct but too early)
- Can't hold through crisis (liquidity constraints)
- **"Arbitrageurs" become forced sellers**

### 7. Post-Crisis Entry


**After seizure passes:**

**Opportunity:**
- Basis still wide (50-100× normal)
- Funding returning (slowly)
- Dealers re-entering market

**Trade:**
- Enter mean-reversion trades
- But: Need long time horizon (months to years)
- Requires patience and capital

**Example (2009):**
- Credit basis still -200 bps (June 2009)
- Enter: Buy bond, buy CDS
- Hold 2 years
- Basis normalizes to -20 bps
- **Profit: 180 bps over 2 years**

---

## Mathematical Framework


### 1. Basis Explosion Dynamics


**Time-series model:**

$$
\text{Basis}_t = \mu + \beta \times \text{Funding Stress}_t + \gamma \times \text{Volatility}_t + \epsilon_t
$$

**Normal regime:**
- $\mu = 10$ bps (mean)
- $\beta = 5$ (low sensitivity)
- Basis: 5-20 bps

**Crisis regime:**
- $\mu = 100$ bps (elevated)
- $\beta = 50$ (high sensitivity)
- Basis: 50-500 bps

### 2. Funding Liquidity Spiral


**Feedback loop:**

$$
\Delta \text{Basis}_t = \alpha \times \text{Basis}_{t-1} + \beta \times \text{Margin Call}_t
$$

**Positive feedback (crisis):**
- Basis widens → MTM losses → Margin calls → Forced liquidations → Basis widens more

**Eventually stabilizes when:**
- Forced sellers exhausted
- Central bank intervenes
- Patient capital enters

### 3. Optimal Exit Strategy


**Minimize loss during crisis:**

$$
\min \mathbb{E}[\text{Loss}] = \text{Current MTM Loss} + \mathbb{E}[\text{Future Widening}] \times \text{Position}
$$

**Decision:**
- If $\mathbb{E}[\text{Widening}] > \text{Holding Cost}$, exit now
- Else hold and wait for normalization

**Challenge:**
- Hard to estimate $\mathbb{E}[\text{Widening}]$ during crisis
- Uncertainty huge
- Usually best to exit early

### 4. Arbitrage Bounds


**Normal arbitrage bounds:**

$$
|\text{Basis}| < \text{Transaction Costs} + \text{Financing Costs}
$$

**Crisis arbitrage bounds:**

$$
|\text{Basis}| < \text{Transaction Costs} + \text{Financing Costs} + \text{Balance Sheet Costs} + \text{Capital Charges}
$$

**Result:**
- Bounds widen dramatically (10-50×)
- "Arbitrages" appear but unexploitable

### 5. Liquidation Threshold


**Forced exit when:**

$$
\text{MTM Loss} > \text{Available Capital} - \text{Minimum Buffer}
$$

**Example:**
- Available capital: $\$10M$
- Minimum buffer: $\$2M$ (operational needs)
- Maximum tolerable loss: $\$8M$

**If basis widening causes $\$8M$ loss:**
- **Must exit immediately** (hit threshold)

### 6. Recovery Time


**Mean reversion speed:**

$$
\text{Basis}_t = \text{Basis}_{\text{crisis}} \times e^{-\lambda t} + \text{Basis}_{\text{normal}}
$$

**Typical half-life:**
- $\lambda \approx 0.1$ to $0.5$ (daily)
- Half-life: 1-7 days (fast)
- Full recovery: 2-4 weeks

**But:**
- Assumes funding returns
- If funding stays tight, recovery slower (months)

### 7. Cross-Market Contagion


**Correlation in stress:**

$$
\rho_{\text{crisis}} \approx 0.8 \text{ to } 0.9
$$

**All bases explode together:**
- Treasury basis
- Credit basis
- Swap spread
- FX basis

**No diversification benefit**

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. "Picking Up Nickels"


**Mistake:** Enter basis trade thinking "can't go wider"

**Why it fails:** Can ALWAYS go wider

**Example:**
- Basis at 50 (5× normal)
- Think: "Can't get worse, short basis"
- Basis → 200 (20× normal)
- **Wiped out**

**Fix:** Don't assume bounds in crisis

### 2. Underestimating Funding Risk


**Mistake:** Assume repo always available

**Why it fails:** Repo seizes in crisis

**Example:**
- Long Treasury cash (basis trade)
- Fund via overnight repo
- Crisis: Repo unavailable
- **Forced to sell at distressed prices**

**Fix:** Use term repo, maintain large cash buffer

### 3. Insufficient Capital


**Mistake:** Fully levered position

**Why it fails:** No buffer for widening

**Example:**
- $\$10M$ capital
- $\$100M$ basis position (10× levered)
- Basis widens 0.50
- MTM loss: $\$100M × 0.005 = $\$500K$
- After 20× widening: $\$10M$ loss
- **Account wiped out**

**Fix:** Max 2-3× leverage for basis trades

### 4. Ignoring Correlation


**Mistake:** Diversify across "different" bases

**Why it fails:** All bases correlate in crisis

**Example:**
- Treasury basis: +0.50
- Credit basis: +0.50  
- FX basis: +0.50
- Think: "Diversified"

**Crisis:**
- All explode together
- **No diversification benefit**

**Fix:** Treat all basis trades as correlated

### 5. Averaging Down


**Mistake:** Add to losing position

**Why it fails:** Basis can widen much more

**Example:**
- Initial: Short basis at 0.50
- Widens to 1.00, add more (short more)
- Widens to 2.00, add more
- Widens to 5.00
- **Position now huge, losses catastrophic**

**Fix:** Cut losers, don't average down in crisis

### 6. Ignoring Delivery Squeeze


**Mistake:** Short basis into delivery month

**Why it fails:** Forced delivery or squeeze

**Example:**
- Short futures, long cash (basis trade)
- Enter delivery month
- Can't deliver (CTD bond scarce)
- **Squeezed, forced to cover at terrible prices**

**Fix:** Exit 10 days before delivery in stress

### 7. Overleveraging "Arbitrage"


**Mistake:** Massive position in "risk-free arbitrage"

**Why it fails:** It's not risk-free

**Example:**
- Credit basis: -200 bps (huge!)
- Think: "Free money"
- Lever 20×
- Basis widens to -400 bps
- **Margin call, forced liquidation**

**Fix:** Even "arbitrage" needs conservative sizing

### 8. Misunderstanding Fed Put


**Mistake:** Assume Fed will save quickly

**Why it fails:** Fed acts with lag

**Example:**
- March 2020: Basis exploded
- Think: "Fed will fix tomorrow"
- Hold losing position
- Fed announced programs 1-2 weeks later
- Basis stayed wide for days
- **Interim losses large**

**Fix:** Don't count on immediate rescue

---

## Risk Management Rules


### 1. Position Sizing


**Maximum basis notional:**

$$
\text{Max Notional} = \frac{\text{Capital}}{\text{Max Basis Widening} \times \text{DV01}}
$$

**Example:**
- Capital: $\$10M$
- Max widening: 2.00 (200 bps)
- DV01: $\$100$ per bp

**Max notional:**

$$
\frac{\$10M}{2.00 \times \$100} = \$50M
$$

**Rule of thumb:** Max 3-5× leverage

### 2. Stop-Loss Rules


**Mandatory exits:**

- **Basis widens > 2× entry level** → Exit immediately
- **Funding costs > Expected carry** → Exit
- **Capital buffer < 25%** → Reduce by 50%

**Example:**
- Enter at basis 0.30
- Exit trigger: 0.60 (2× entry)
- No exceptions

### 3. Funding Contingency


**Multiple funding sources:**

- Minimum 5 repo dealers
- Mix term and overnight (70% term in stress)
- Credit lines (backup)
- Cash buffer ≥ 30 days funding needs

### 4. Stress Testing


**Weekly basis stress test:**

- Scenario 1: Basis 5× wider
- Scenario 2: Basis 10× wider  
- Scenario 3: Basis 20× wider + funding lost

**Action triggers:**
- Scenario 1 loss > 20% capital → Reduce position
- Scenario 2 loss > 50% capital → Exit entirely

### 5. Exposure Limits


**By crisis type:**

- **Treasury basis:** Max 20% of capital
- **Credit basis:** Max 15% of capital
- **Swap spread:** Max 10% of capital
- **FX basis:** Max 10% of capital

**Total across all bases:** Max 30% of capital

### 6. Term Structure Management


**Avoid front-month exposure:**

- No exposure < 30 days to delivery
- Prefer 60-90 day contracts
- Roll early (60 days before expiry)

### 7. Monitoring Dashboard


**Real-time tracking:**

- Current basis (all markets)
- MTM P&L
- Repo availability and rates
- VIX level
- Dealer capacity (calls)

**Alert triggers:**
- Any basis > 2× normal
- VIX > 30
- Repo spread > 100 bps over SOFR
- Dealer reduces capacity

---

## Real-World Examples


### 1. LTCM Collapse (1998)


**Setup:**
- Massive basis trades (levered 30×)
- Russian default triggered crisis

**Basis explosion:**
- Treasury basis: 5 ticks → 50 ticks (10× wider)
- Credit basis: -20 bps → -300 bps
- Swap spread: +40 bps → +150 bps

**LTCM positions:**
- $\$125B$ notional
- $\$4B$ capital
- Losses: $\$4B$ (wiped out)
- Fed-orchestrated rescue

**Lesson:** Leverage kills in crisis

### 2. Lehman Bankruptcy (2008)


**Setup:**
- Basis traders ubiquitous
- Repo market healthy

**Crisis (Sept 15, 2008):**
- Lehman files Chapter 11
- Repo market seizes
- Treasury basis: 10 ticks → 200 ticks (20× wider!)
- Credit basis: -30 bps → -500 bps

**Impact:**
- Hedge funds liquidating
- Dealers exit market-making
- Even "arbitrages" fail

**Survivors:**
- Those with term funding
- Conservative leverage (2-3×)
- Large cash buffers

**Lesson:** Funding liquidity essential

### 3. COVID Dash for Cash (March 2020)


**Setup:**
- Basis trades common (low rates)
- Balance sheet constraints (SLR)

**Crisis (March 2020):**
- Everyone selling everything
- Even Treasury selling!
- Treasury basis: 10 ticks → 100 ticks
- Swap spread: +20 bps → -50 bps (negative!)

**Why?**
- Dealers couldn't intermediate (SLR binding)
- Massive Treasury selling
- Basis exploded

**Fed response:**
- $\$750B$ Treasury purchases
- Temporary SLR relief
- Basis normalized over 2-3 weeks

**Lesson:** Regulatory constraints impair crisis response

### 4. Basis Whipsaw (2020)


**Trade:**
- Short Treasury basis at 0.40 (Jan 2020)
- Expect convergence to 0.10

**March crisis:**
- Basis → 1.50 (exploded!)
- MTM loss: Massive
- Margin calls
- Forced to exit at 1.50

**April normalization:**
- Basis → 0.20 (would have been profitable!)
- But: Already exited at 1.50
- **Lost despite being right long-term**

**Lesson:** Need capital to survive interim widening

### 5. FX Basis Blowout (2008)


**Setup:**
- EUR/USD FX basis: -10 bps (normal)
- European banks need USD funding

**Crisis:**
- FX basis: -10 bps → -300 bps (30× wider!)
- USD extremely expensive to obtain via FX swap

**Impact:**
- European banks struggled
- Fed opened swap lines (provided USD)
- Basis slowly normalized (6 months)

**Opportunity:**
- US money funds lent USD via FX swaps
- Earned 300 bps premium
- Safe and profitable (Fed backstop)

**Lesson:** Crisis creates opportunities for patient capital

---

## Practical Steps


### 1. Monitoring Basis Stress


**Daily basis tracking:**

```python
# Track all bases
bases = {
    'treasury_10y': compute_net_basis(futures, cash, cf, carry),
    'credit_ig': compute_cds_bond_basis(cds_spread, bond_spread),
    'swap_spread_10y': swap_rate - treasury_yield,
    'eur_usd_fx_basis': fx_basis_calculator(eur_rate, usd_rate, fx_swap)
}

# Compare to normal levels
for basis_name, current_value in bases.items():
    normal = historical_mean[basis_name]
    ratio = current_value / normal
    
    if ratio > 2:
        alert(f"{basis_name} at {ratio}× normal - WARNING")
    if ratio > 5:
        alert(f"{basis_name} at {ratio}× normal - CRISIS")
```

### 2. Stress Scenario Analysis


**Monthly stress test:**

1. **Mild stress (2× widening):**
   - All bases double
   - Compute MTM loss
   - Check vs. 20% capital threshold

2. **Severe stress (10× widening):**
   - All bases 10× wider
   - Compute MTM loss
   - Check vs. 50% capital threshold

3. **Extreme stress (20× + funding loss):**
   - Bases 20× wider
   - Can't roll repo
   - Forced liquidation costs

4. **Action plan:**
   - If Scenario 2 loss > 50% → Reduce positions now
   - If Scenario 3 loss > 80% → Exit all basis trades

### 3. Funding Contingency Planning


**Prepare for stress:**

1. **Normal times:**
   - 5+ repo dealers
   - 50% overnight, 50% term repo
   - Cash buffer = 10 days funding

2. **Warning signs (VIX > 25):**
   - Shift to 30% overnight, 70% term
   - Increase cash buffer to 30 days
   - Negotiate additional dealer lines

3. **Crisis (VIX > 40):**
   - Term repo only
   - Cash buffer to 60 days
   - Prepare to exit positions

### 4. Position Scaling


**Dynamic adjustment:**

```python
def calculate_position_size(current_basis, normal_basis, capital):
    # Scale down as basis widens
    basis_ratio = current_basis / normal_basis
    
    if basis_ratio < 1.5:
        scale = 1.0  # Full position
    elif basis_ratio < 2:
        scale = 0.75  # Reduce 25%
    elif basis_ratio < 3:
        scale = 0.5  # Reduce 50%
    else:
        scale = 0.0  # Exit entirely
    
    max_notional = capital * 3  # 3× max leverage
    return max_notional * scale
```

### 5. Exit Strategy


**Predetermined rules:**

1. **Stop-loss (any basis):**
   - MTM loss > 20% of capital → Exit 50% of position
   - MTM loss > 30% of capital → Exit 100% of position

2. **Time-based:**
   - Basis trade > 6 months old → Review (decay?)
   - Approaching delivery < 30 days → Exit

3. **Market-based:**
   - VIX > 40 → Reduce all basis trades by 50%
   - Repo unavailable → Exit immediately

---

## Final Wisdom


> "Crisis basis dynamics reveal the harsh truth that arbitrage isn't arbitrage when you can't fund it, can't hold it, or can't survive the interim volatility. The 2008 crisis showed that Treasury basis could widen 20× normal levels, credit basis could reach -500 bps, and swap spreads could go negative - relationships that 'couldn't happen' based on decades of data. The fundamental lesson: basis trades are leveraged relative value bets that profit in normal times but can destroy capital in crises when funding evaporates, balance sheets constrain, and forced liquidations cascade. Survivors have three attributes: (1) conservative leverage (2-3× max), (2) term funding secured before stress, and (3) enough capital to survive 10-20× basis widening. The worst mistake is treating basis trades as 'low-risk arbitrage' - they're actually highly levered macro bets that blow up exactly when you need liquidity most."

**Key to success:**

- **Assume basis can widen 10-20× during crisis** (Treasury: 5 ticks → 100 ticks, Credit: -20 bps → -400 bps)
- **Max 2-3× leverage** for any basis trade (LTCM was 30× and died, survivors were <5×)
- **Secure term funding before stress** (overnight repo dries up first, need 70%+ term in crisis)
- **Stop-loss at 2× entry basis level** (if entered at 0.30 and widens to 0.60, exit immediately no exceptions)
- **Diversification illusion** (all bases correlate 0.8-0.9 in crises, can't diversify away crisis risk)
- **Don't average down in crisis** (basis can always widen more, adding to losers fatal)
- **Exit before delivery month** (last 30 days create squeeze risk, exit 60+ days before)
- **Remember:** "Arbitrage" opportunities in crisis are unexploitable (no funding, no balance sheet, no capital)
