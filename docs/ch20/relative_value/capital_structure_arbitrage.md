# Capital Structure Arbitrage

**Capital structure arbitrage** is the practice of exploiting mispricings between different securities issued by the same company—typically between equity and credit, or between senior and subordinated debt—based on the structural relationships that should theoretically bind their values together, profiting when these relationships normalize while the fundamental value of the underlying enterprise remains constant.

---

## The Core Insight

**The fundamental idea:**

- All securities of a company are claims on the same underlying assets
- Capital structure creates strict priority: Senior debt > Junior debt > Equity
- Merton model: Equity is a call option on firm assets, Debt is short put
- When equity and credit diverge, arbitrage opportunity exists
- Long undervalued security, short overvalued security
- Profit when relationship normalizes (not from directional view)
- Market-neutral at the firm level (both long and short same company)
- Requires sophisticated modeling of structural relationships

**The key equations:**

**Merton model framework:**

$$
E = \max(V - D, 0) = \text{Call}(V, D)
$$

$$
\text{Debt} = D - \text{Put}(V, D)
$$

Where:
- $E$ = Equity value
- $V$ = Firm asset value
- $D$ = Debt face value

**Relationship between credit spreads and equity volatility:**

$$
\text{Credit Spread} \approx f(\sigma_E, \text{Leverage}, r, T)
$$

**Hedge ratio (equity vs. credit):**

$$
\text{Hedge Ratio} = \frac{\Delta_{\text{equity}}}{\Delta_{\text{debt}}} = \frac{\partial E / \partial V}{\partial D / \partial V}
$$

**Distance to default:**

$$
DD = \frac{\ln(V/D) + (\mu - \sigma^2/2)T}{\sigma\sqrt{T}}
$$

**You're essentially asking: "If I believe equity is overvalued relative to credit spreads (or vice versa) based on structural models, how do I construct a market-neutral position that profits when this mispricing corrects, regardless of whether the company's fundamental value goes up or down?"**

---

## What is Capital Structure Arbitrage?

**Before implementing these strategies, understand the structural framework:**

### The Capital Structure Hierarchy

**Priority of claims (liquidation):**

```
Liquidation Value of Assets ($V)
        ↓
1. Senior Secured Debt (first claim)
2. Senior Unsecured Debt
3. Subordinated Debt (Junior)
4. Preferred Equity
5. Common Equity (residual claim)
```

**Example company:**

**ABC Corp capital structure:**
- Assets (market value): $1,000M
- Senior secured debt: $300M
- Senior unsecured debt: $200M
- Subordinated debt: $150M
- **Total debt: $650M**
- Equity market cap: $400M
- **Enterprise value: $1,050M**

**Scenario 1: Mild stress (Assets → $800M)**

| Security | Face Value | Recovery | Loss |
|----------|-----------|----------|------|
| Senior secured | $300M | $300M | 0% |
| Senior unsecured | $200M | $200M | 0% |
| Subordinated | $150M | $150M | 0% |
| **Total debt** | $650M | $650M | 0% |
| Equity | - | $150M | -62.5% |

**Equity bears all losses first!**

**Scenario 2: Severe stress (Assets → $500M)**

| Security | Face Value | Recovery | Loss |
|----------|-----------|----------|------|
| Senior secured | $300M | $300M | 0% |
| Senior unsecured | $200M | $200M | 0% |
| Subordinated | $150M | $0M | -100% |
| **Total debt** | $650M | $500M | -23% |
| Equity | - | $0M | -100% |

**Subordinated wiped out, equity zero.**

**Scenario 3: Default (Assets → $400M)**

| Security | Face Value | Recovery | Loss |
|----------|-----------|----------|------|
| Senior secured | $300M | $300M | 0% |
| Senior unsecured | $200M | $100M | -50% |
| Subordinated | $150M | $0M | -100% |
| **Total debt** | $650M | $400M | -38% |
| Equity | - | $0M | -100% |

**Senior recovers 60%, junior and equity zero.**

### The Merton Model Foundation

**Equity as a call option:**

The equity holders have a **call option** on the firm's assets with strike price equal to debt face value.

$$
E = V \cdot N(d_1) - D e^{-rT} \cdot N(d_2)
$$

Where:

$$
d_1 = \frac{\ln(V/D) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}
$$

$$
d_2 = d_1 - \sigma\sqrt{T}
$$

**Interpretation:**
- If $V > D$ at maturity: Equity worth $V - D$ (pay off debt, keep residual)
- If $V < D$ at maturity: Equity worth $0$ (default, equity wiped out)
- **This is exactly a call option payoff!**

**Debt as short put:**

Debt holders are effectively **long a risk-free bond and short a put option** on firm assets.

$$
\text{Risky Debt} = D e^{-rT} - \text{Put}(V, D, \sigma, T)
$$

**Interpretation:**
- In good state: Receive full $D$
- In bad state: Receive $V < D$ (exercise put, take assets)
- **Debt value decreases as firm value falls (short put)**

**Key insight:**

$$
V = E + D
$$

Firm value equals equity plus debt. Changes in $V$ affect both, but non-linearly.

**Delta relationships:**

$$
\frac{\partial E}{\partial V} = N(d_1) \approx 0.5 \text{ to } 1.0 \text{ (depends on leverage)}
$$

$$
\frac{\partial D}{\partial V} = 1 - N(d_1) \approx 0 \text{ to } 0.5
$$

**Sum to 1.0:** $\Delta_E + \Delta_D = 1$

**Example:**
- Low leverage (healthy): $\Delta_E \approx 0.8$, $\Delta_D \approx 0.2$
- High leverage (distressed): $\Delta_E \approx 0.3$, $\Delta_D \approx 0.7$

**This relationship is the foundation of capital structure arbitrage!**

### Credit Spreads and Equity Volatility

**Theoretical relationship:**

Higher equity volatility → Higher default probability → Wider credit spreads

$$
\text{Credit Spread} \approx \alpha \cdot \sigma_E^\beta \cdot \text{Leverage}^\gamma
$$

Where $\beta \approx 2$ and $\gamma \approx 1.5$ empirically.

**Example:**

**Company A (stable):**
- Equity volatility: 20%
- Leverage (Debt/Assets): 40%
- **Predicted spread: 80 bp**
- **Actual spread: 85 bp (fair)**

**Company B (volatile):**
- Equity volatility: 50%
- Leverage: 40%
- **Predicted spread: 320 bp** (volatility squared!)
- **Actual spread: 280 bp (too tight!)**

**Arbitrage opportunity:** Company B credit is mispriced (spreads too tight given equity vol).

**Trade:**
- Short Company B equity
- Buy CDS protection on Company B
- Profit when spreads widen or equity falls

---

## Economic Interpretation: Why Mispricings Occur

**Understanding the structural inefficiencies:**

### Market Segmentation

**Different investor bases:**

**Equity investors:**
- Focus on growth, earnings, momentum
- High turnover, shorter horizon
- Options market very active
- **React quickly to news**

**Credit investors:**
- Focus on downside risk, cash flow, covenants
- Lower turnover, longer horizon
- Less liquid (especially single names)
- **React slowly to news**

**Result:** Information often incorporated in equity first, credit lags.

**Example:**
- Company announces weak earnings
- Equity falls 15% immediately
- Credit spreads widen only 10 bp (should widen 30 bp)
- **Temporary mispricing: Equity cheap vs. credit**

### Leverage Dynamics

**As firm value changes, leverage changes:**

**Scenario: Firm value increases**

$$
\text{Leverage} = \frac{D}{V} \text{ decreases (denominator rises)}
$$

- Lower leverage → Lower default risk → Credit spreads tighten
- Equity benefits twice: (1) from value increase, (2) from lower financial distress
- **Equity should outperform credit**

**Scenario: Firm value decreases**

$$
\text{Leverage} = \frac{D}{V} \text{ increases (denominator falls)}
$$

- Higher leverage → Higher default risk → Credit spreads widen
- Equity suffers twice: (1) from value decrease, (2) from higher financial distress
- **Credit should outperform equity (lose less)**

**Arbitrage when this relationship breaks down:**

If equity rallies but credit doesn't tighten proportionally → Short equity, long credit.

### Volatility Smile and Capital Structure

**Equity options implied volatility:**

Equity options price in default risk through volatility smile.

**At-the-money (ATM) options:**
- Price in normal volatility
- Less sensitive to default

**Out-of-the-money (OTM) puts:**
- Price in tail risk (default)
- Very sensitive to default probability
- **Implied vol spikes for deep OTM puts**

**Relationship to credit:**

$$
\text{CDS Spread} \approx f(\text{Implied Vol}_{\text{OTM puts}})
$$

**When OTM put vol spikes but CDS doesn't widen → Arbitrage.**

**Trade:**
- Sell OTM puts (collect high premium from default fear)
- Buy CDS protection (cheaper than put vol implies)
- Profit from mispricing

### Recovery Rate Assumptions

**Credit markets assume recovery rates:**

- Senior secured: 70%
- Senior unsecured: 40%
- Subordinated: 20%

**But equity market prices zero recovery for equity (always).**

**Mispricing opportunity:**

If credit market is too optimistic about recovery (e.g., pricing 50% when reality is 30%):
- Credit spreads too tight
- **Buy CDS protection (bet on wider spreads when recovery repriced)**

---

## Key Terminology

**Capital Structure:**

- Hierarchy of claims on company assets
- Priority: Senior debt > Junior debt > Preferred > Common equity
- Determines payoff in default/distress

**Merton Model:**

- Structural model of default
- Equity = Call option on assets
- Debt = Risk-free bond - Put option on assets
- Foundation for capital structure arbitrage

**Delta (Equity vs. Credit):**

$$
\Delta_E = \frac{\partial E}{\partial V}, \quad \Delta_D = \frac{\partial D}{\partial V}
$$

- Equity delta: 0.5-1.0 (higher for low leverage)
- Debt delta: 0-0.5 (higher for high leverage)
- Sum: $\Delta_E + \Delta_D = 1$

**Hedge Ratio:**

$$
\text{HR} = \frac{\text{Equity Shares}}{\text{Credit Notional}} = \frac{\Delta_E}{\Delta_D}
$$

Number of shares to short per dollar of credit exposure to be delta-neutral.

**Distance to Default (DD):**

$$
DD = \frac{\ln(V/D) + (\mu - \sigma^2/2)T}{\sigma\sqrt{T}}
$$

- Measures how far firm value is from default threshold
- Higher DD = Lower default probability
- Typical: DD > 3 = Safe, DD < 1 = Distressed

**CDS-Equity Basis:**

$$
\text{Basis} = \text{Implied Default Prob}_{\text{CDS}} - \text{Implied Default Prob}_{\text{Equity}}
$$

- Positive basis: CDS pricing more risk than equity
- Negative basis: Equity pricing more risk than CDS

**Leverage:**

$$
\text{Leverage} = \frac{D}{V} = \frac{\text{Debt}}{\text{Equity} + \text{Debt}}
$$

- Higher leverage → Higher default risk
- Key driver of credit spreads

**Senior vs. Subordinated Spread:**

$$
\text{Sub Premium} = \text{Spread}_{\text{sub}} - \text{Spread}_{\text{senior}}
$$

- Compensates for lower recovery
- Typically 100-300 bp for same issuer
- Widens in distress

**Z-Score (Altman):**

$$
Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5
$$

Where $X_i$ are financial ratios (working capital, retained earnings, EBIT, equity, sales).

- Z > 2.99: Safe zone
- 1.81 < Z < 2.99: Gray zone
- Z < 1.81: Distress zone

**Notional Conversion:**

$$
\text{CDS Notional} = \frac{\text{Equity Market Cap} \times \Delta_E}{\Delta_D}
$$

How much CDS to match equity position delta.

---

## Basic Capital Structure Arbitrage Strategies

### Strategy 1: Long Credit, Short Equity (Classic)

**Setup:**

**Company XYZ:**
- Equity market cap: $800M
- Stock price: $40
- Equity volatility: 45% (very high)
- Total debt: $600M
- 5-year CDS: 180 bp
- Credit rating: BBB

**Analysis:**

**Equity pricing:**
- High volatility suggests significant default risk
- Implied default probability from equity: 8% (5-year)

**Credit pricing:**
- 180 bp spread implies: 3% default probability (assuming 40% recovery)
- **Credit is not pricing the same risk as equity!**

**Merton model:**

Inputs:
- $V = E + D = \$1,400M$ (implied)
- $\sigma_E = 45\%$
- Leverage = $600 / 1,400 = 43\%$

**Model prediction:**
- Fair CDS spread: 350 bp
- **Actual: 180 bp**
- **Credit is mispriced (too tight by 170 bp)**

**Trade:**

**Long credit risk (sell equity, buy CDS protection):**

1. Short 10,000 shares at $40 = $400,000
2. Buy $1M notional CDS protection at 180 bp

**Hedge ratio calculation:**

$$
\Delta_E = N(d_1) \approx 0.65 \text{ (from Merton model)}
$$

$$
\Delta_D = 1 - 0.65 = 0.35
$$

$$
\text{CDS Notional} = \frac{\$400k \times 0.65}{0.35} = \$743k
$$

**Use $750k CDS for simplicity.**

**Costs:**
- CDS premium: $750k × 1.80% = $13,500 annually
- Short equity cost (borrow): ~1% = $4,000 annually
- **Total cost: $17,500/year**

**Scenario 1: Company deteriorates (view correct)**

**6 months later:**
- Stock: $40 → $28 (-30%)
- CDS: 180 bp → 450 bp (+270 bp)

**P/L:**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | -30% | +$120,000 |
| CDS (long protection) | +270 bp × $30k DV01 | +$81,000 |
| Costs (6 months) | | -$8,750 |
| **Net** | | **+$192,250** |

**Return on capital (~$50k margin): 384% in 6 months!**

**Scenario 2: Company stabilizes (spreads converge)**

**1 year later:**
- Stock: $40 → $38 (-5%)
- CDS: 180 bp → 280 bp (+100 bp)
- **Credit widened to fair value, equity stable**

**P/L:**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | -5% | +$20,000 |
| CDS | +100 bp × $30k DV01 | +$30,000 |
| Costs (1 year) | | -$17,500 |
| **Net** | | **+$32,500** |

**Return: 65% on $50k capital**

**Scenario 3: Company improves (wrong view)**

**Stock rallies on good news:**
- Stock: $40 → $52 (+30%)
- CDS: 180 bp → 120 bp (-60 bp)

**P/L:**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | +30% | -$120,000 |
| CDS | -60 bp × $30k DV01 | -$18,000 |
| Costs (1 year) | | -$17,500 |
| **Net** | | **-$155,500** |

**Loss: -311% (wipeout!)**

**Risk management:** Set stop loss at -50% (-$25k).

### Strategy 2: Senior vs. Subordinated (Credit Curve Trade)

**Setup:**

**Company ABC:**
- Senior unsecured CDS: 200 bp
- Subordinated CDS: 450 bp
- **Spread differential: 250 bp**
- Historical average differential: 180 bp

**Analysis:**

**Subordinated too wide relative to senior:**
- 250 bp vs. 180 bp historical
- **Subordinated looks cheap (or senior rich)**

**Expected recovery:**
- Senior: 40%
- Subordinated: 15%
- Recovery differential: 25%

**Implied default probability:**

Senior: $\text{PD} = \frac{200}{100 - 40} = 3.33\%$

Subordinated: $\text{PD} = \frac{450}{100 - 15} = 5.29\%$

**Same company, same default probability!**

**Mispricing:** Subordinated pricing 59% higher default probability than senior.

**Trade:**

**Buy subordinated protection (it's overpriced, will tighten):**
**Sell senior protection (it's underpriced, will widen):**

1. Buy $10M subordinated CDS at 450 bp
2. Sell $10M senior CDS at 200 bp

**Net position:**
- Receive: 200 bp on senior
- Pay: 450 bp on subordinated
- **Net cost: 250 bp = $25,000/year**

**Scenario 1: Spreads normalize (view correct)**

**6 months later:**
- Senior: 200 bp → 230 bp (+30 bp)
- Subordinated: 450 bp → 410 bp (-40 bp)
- **Differential: 180 bp** (normalized!)

**P/L:**

| Position | Change | DV01 | P/L |
|----------|--------|------|-----|
| Short senior (sold protection) | +30 bp widen | $40k | -$12,000 |
| Long subordinated (bought protection) | -40 bp tighten | $35k | +$14,000 |
| Net premium (6M) | | | -$12,500 |
| **Net** | | | **-$10,500** |

**Wait, lost money even though view was correct?**

**Problem:** Senior widened more than subordinated tightened (absolute bp).

**Better trade design: DV01-neutral**

Adjust notional:
- Sell $14M senior CDS (higher DV01 to match subordinated)
- Buy $10M subordinated CDS

**Revised P/L:**

| Position | Change | P/L |
|----------|--------|-----|
| Short $14M senior | +30 bp | -$16,800 |
| Long $10M sub | -40 bp | +$14,000 |
| Net premium | | -$17,500 |
| **Net** | | **-$20,300** |

**Still lost! Why?**

**Issue: Differential narrowed but absolute levels moved against us.**

**Correct trade: Focus on differential, not absolute:**

Use **spread options or custom structures** that directly bet on differential.

Or **wait for senior to cheapen before entering.**

### Strategy 3: Distressed Long Equity / Short Senior Debt

**Setup:**

**Company DEF (distressed):**
- Stock price: $5 (down from $30)
- Market cap: $100M
- Total debt: $800M
- Senior unsecured bonds: Trading at $40 (60% discount)
- CDS: 2,500 bp (extreme distress)

**Analysis:**

**Equity seems cheap:**
- Restructuring announced
- New management
- Asset sales underway
- **If survives, equity could triple**

**Credit seems expensive:**
- Bonds at $40 assume 40% recovery
- But if company survives, bonds go to par ($100)
- **Upside: 150%**

**But: If company defaults:**
- Equity → $0 (100% loss)
- Bonds → $25 recovery (37.5% loss from $40)

**Asymmetry:**

**Equity upside/downside:** +200% / -100%
**Credit upside/downside:** +150% / -37.5%

**Trade (contrarian):**

**Long equity (bet on survival):**
- Buy $100k equity at $5

**Short senior debt (hedge):**
- Short $400k senior bonds at $40
- Or buy $400k CDS protection at 2,500 bp

**Scenario 1: Company survives and restructures**

**1 year later:**
- Stock: $5 → $15 (+200%)
- Bonds: $40 → $85 (+112.5%)
- CDS: 2,500 bp → 800 bp

**P/L:**

| Position | Change | P/L |
|----------|--------|-----|
| Long equity $100k | +200% | +$200,000 |
| Short bonds $400k | +112.5% | -$450,000 |
| **Net** | | **-$250,000** |

**Disaster! The hedge lost more than equity gained.**

**Problem:** Bonds rallied more in absolute dollar terms.

**Scenario 2: Company defaults**

**Bonds → $25 recovery**
**Equity → $0**

**P/L:**

| Position | P/L |
|----------|-----|
| Long equity | -$100,000 |
| Short bonds ($40 → $25) | +$150,000 |
| **Net** | **+$50,000** |

**Profitable on default!**

**This trade is backwards:**
- Profitable if company fails
- Unprofitable if company survives
- **Opposite of intent!**

**Correct trade: Long equity, NO hedge**

If bullish on distressed company, just buy equity. Don't short credit (it will rally more if you're right).

### Strategy 4: Volatility Arbitrage (Equity Options vs. CDS)

**Setup:**

**Company GHI:**
- Stock: $50
- 1-year ATM put implied vol: 35%
- 1-year ATM call implied vol: 28%
- **Volatility skew: 7%** (put vol > call vol)

**CDS:**
- 1-year CDS: 120 bp
- Implied default probability: 2% (assuming 40% recovery)

**Analysis:**

**Equity put vol (35%) implies:**
- Extreme downside risk priced in
- Probability of stock <$25: 15%
- **If stock <$25, default very likely**

**CDS (120 bp) implies:**
- Default probability: 2%
- **Inconsistent with 15% severe distress probability**

**Arbitrage:**

Put vol overpricing default risk OR CDS underpricing it.

**Trade:**

**Sell 1-year $40 puts (collect high premium):**
- Premium: $6 per share
- Sell 100 contracts = 10,000 shares = $60,000 premium

**Buy CDS protection:**
- Notional: $500,000
- Premium: 120 bp = $6,000

**Net premium collected: $54,000**

**Scenario 1: Stock stable (no default)**

- Puts expire worthless
- CDS expires worthless
- **Profit: $54,000 (90% annualized return on $60k capital)**

**Scenario 2: Stock crashes but no default**

- Stock: $50 → $35
- Puts: Lose $5 × 10,000 = -$50,000
- CDS: Worthless (no default)
- Net premium: +$54,000
- **Net: +$4,000** (still profitable!)

**Scenario 3: Default occurs**

- Stock → $0
- Puts: Lose $40 × 10,000 = -$400,000
- CDS: Gain (100 - 40) × $500k = +$300,000
- Net premium: +$54,000
- **Net: -$46,000** (loss, but hedged 75% of put loss)

**Without CDS hedge, would have lost $346k!**

---

## Greeks in Capital Structure Arbitrage

**Understanding cross-asset sensitivities:**

### Equity Delta vs. Credit Delta

**From Merton model:**

$$
\Delta_E = N(d_1), \quad \Delta_D = 1 - N(d_1)
$$

**Relationship:**

$$
\Delta_E + \Delta_D = 1
$$

**Example calculations:**

**Healthy company (low leverage 30%):**
- $d_1 = 1.5$ (far from default)
- $\Delta_E = N(1.5) = 0.93$
- $\Delta_D = 0.07$
- **Equity very sensitive, credit barely moves**

**Moderate leverage (50%):**
- $d_1 = 0.5$
- $\Delta_E = N(0.5) = 0.69$
- $\Delta_D = 0.31$
- **Equity still more sensitive, credit significant**

**Distressed (leverage 80%):**
- $d_1 = -0.5$
- $\Delta_E = N(-0.5) = 0.31$
- $\Delta_D = 0.69$
- **Credit now MORE sensitive than equity!**

**Implication for hedging:**

As company deteriorates, need more credit protection per dollar of equity shorted.

### Vega: Volatility Sensitivity

**Equity vega:**

$$
\text{Vega}_E = V \cdot N'(d_1) \cdot \sqrt{T}
$$

**Positive:** Equity value increases with volatility (call option property).

**Credit vega:**

$$
\text{Vega}_D = -V \cdot N'(d_1) \cdot \sqrt{T}
$$

**Negative:** Credit value decreases with volatility (short put).

**Implication:**

When implied volatility spikes (e.g., VIX jump):
- Equity gains from higher vol
- Credit spreads widen (bonds lose value)
- **Long equity / short credit position wins on vol spike**
- **Short equity / long credit position loses on vol spike**

**Risk management:**

If short equity / long credit (betting on deterioration):
- **Vulnerable to vol crush** (sudden decline in implied vol)
- VIX falls → Equity outperforms credit
- Can hedge with long VIX or short vol

### Gamma: Convexity

**Equity gamma:**

$$
\Gamma_E = \frac{N'(d_1)}{V \sigma \sqrt{T}}
$$

**Credit gamma:**

$$
\Gamma_D = -\Gamma_E
$$

**Interpretation:**

**For out-of-the-money equity (high leverage):**
- Equity has high gamma (convex)
- Small firm value increase → Big equity percentage gain
- **Equity can rally more than credit tightens**

**This explains why distressed equity can rally 100%+ while bonds only rally 20-30%.**

**Capital structure arbitrage challenge:**

Shorting equity and longing credit in distressed situations faces **negative gamma**:
- If firm improves: Equity rallies more than credit tightens (lose)
- If firm deteriorates: Equity falls but may be near zero already (limited gain)

**Asymmetric risk!**

---

## Capital Structure Arbitrage Payoff Analysis

### Long Credit / Short Equity Expected Returns

**Setup:**
- Short $1M equity
- Long $2M CDS protection (delta-matched)
- Holding period: 1 year

**Scenario analysis:**

| Firm Value Change | Equity Return | Credit Spread Change | CDS MTM | Net P/L | Probability |
|-------------------|---------------|----------------------|---------|---------|-------------|
| +20% | -20% | -50 bp | -$40k | +$160k | 15% |
| +10% | -10% | -20 bp | -$16k | +$84k | 20% |
| 0% | 0% | 0 bp | $0 | $0 | 30% |
| -10% | +10% | +50 bp | +$40k | -$60k | 20% |
| -20% | +20% | +120 bp | +$96k | -$104k | 10% |
| -30% (default) | +30% | Default | +$1.2M | +$1.5M | 5% |

**Expected value:**

$$
E[P/L] = 0.15(160k) + 0.20(84k) + 0.30(0) + 0.20(-60k) + 0.10(-104k) + 0.05(1,500k)
$$

$$
= 24k + 16.8k + 0 - 12k - 10.4k + 75k = \$93.4k
$$

**Expected return: 9.3% on $1M capital**

**But look at the distribution:**
- Win big if default (5% chance): +$1.5M
- Win small if mild deterioration (20%): +$84k average
- Breakeven if stable (30%): $0
- Lose moderate if improves (35%): -$82k average

**Skewed distribution:** Small probability of huge win, large probability of moderate loss.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/capital_structure_arb_payoff.png?raw=true" alt="capital_structure_arb_payoff" width="700">
</p>
**Figure 1:** P/L distribution for long credit / short equity capital structure arbitrage showing positive skew with small probability of large gain (default scenario) and higher probability of moderate losses (firm improvement).

### Senior vs. Subordinated Spread Trade

**Setup:**
- Long $10M subordinated CDS at 450 bp (overpaying protection)
- Short $10M senior CDS at 200 bp (receiving premium)
- Net cost: 250 bp = $25k/year

**Expected spread differential movement:**

| Scenario | Senior Spread | Sub Spread | Differential | P/L | Probability |
|----------|---------------|------------|--------------|-----|-------------|
| Strong improvement | 120 bp | 280 bp | 160 bp | +$36k | 10% |
| Mild improvement | 180 bp | 400 bp | 220 bp | +$12k | 25% |
| Stable | 200 bp | 450 bp | 250 bp | -$25k | 30% |
| Mild deterioration | 250 bp | 520 bp | 270 bp | -$33k | 25% |
| Severe deterioration | 400 bp | 750 bp | 350 bp | -$65k | 10% |

**Expected value:**

$$
E[P/L] = 0.10(36k) + 0.25(12k) + 0.30(-25k) + 0.25(-33k) + 0.10(-65k)
$$

$$
= 3.6k + 3k - 7.5k - 8.25k - 6.5k = -\$15.65k
$$

**Negative expected return!**

**Why?**
- Differential widens more in stress (tail risk)
- Subordinated gap relative to senior explodes in default scenarios
- **Position loses in tail events**

**Better formulation:**

Express as **ratio trade:**

$$
\text{Spread Ratio} = \frac{\text{Sub Spread}}{\text{Senior Spread}}
$$

Current: 450 / 200 = 2.25x
Historical: 1.8x average

**Trade on ratio mean reversion** instead of absolute differential.

---

## Real-World Capital Structure Arbitrage Examples

### Example 1: Tesla 2019 - Short Equity / Long Credit (Winner)

**Setup:**

- **Date:** February 2019
- **Hedge Fund:** Credit arbitrage specialist
- **View:** Tesla equity overvalued relative to credit risk

**Market conditions:**

**Tesla:**
- Stock price: $310
- Market cap: $53B
- Total debt: $11B
- 5-year CDS: 420 bp (distressed territory)
- Credit rating: B- (deep junk)

**Equity market:**
- Pricing in strong growth
- Model 3 ramp success assumed
- Musk premium (loyal investors)

**Credit market:**
- 420 bp CDS implies 20% cumulative default probability
- Bonds trading at $80-85 (15-20% discount)
- **Credit pricing significant distress**

**Merton model analysis:**

Inputs:
- Equity value: $53B
- Debt: $11B
- Equity volatility: 65% (very high)
- Leverage: 17% (debt/enterprise value)

**Model output:**
- Fair CDS spread: 380-450 bp
- Actual: 420 bp (fair to slightly wide)
- **Credit pricing is reasonable**

**But equity:**
- At 65% vol and current price, implies very low default risk
- **Inconsistent with 420 bp CDS!**

**Trade:**

**Short equity, buy CDS protection:**

1. Short 50,000 shares at $310 = $15.5M
2. Buy $30M CDS protection at 420 bp
3. Hedge ratio: $30M / $15.5M ≈ 1.9x (delta-adjusted)

**Costs:**
- CDS premium: $30M × 4.2% = $1.26M annually
- Short stock borrow: ~5% (Tesla hard to borrow) = $775k
- **Total annual cost: $2.035M**

**Evolution (9 months):**

**March-May 2019:**
- Weak Q1 delivery numbers
- Cash burn concerns
- Stock: $310 → $245 (-21%)
- CDS: 420 bp → 580 bp (+160 bp)

**Interim P/L (3 months):**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | -21% | +$3.255M |
| CDS | +160 bp × $120k DV01 | +$1.920M |
| Costs (3 months) | | -$509k |
| **Net** | | **+$4.666M** |

**Return on capital (~$5M margin): 93% in 3 months!**

**June-August 2019:**
- Strong Q2 deliveries surprise
- Elon raises capital ($2.7B equity + debt)
- Sentiment improves
- Stock: $245 → $230 (sideways)
- CDS: 580 bp → 520 bp (-60 bp)

**Additional P/L:**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | -6% | +$930k |
| CDS | -60 bp × $115k DV01 | -$690k |
| Costs (3 months) | | -$509k |
| **Net** | | -$269k |

**September-October 2019:**
- Q3 profit surprise!
- Stock rallies hard
- Decision: Close position

**Final prices (October):**
- Stock: $230 → $300 (-3% from entry)
- CDS: 520 → 380 bp (-40 bp from entry)

**Final P/L (9 months total):**

| Component | P/L |
|-----------|-----|
| Short equity ($310 → $300) | +$500k |
| CDS (420 → 380 bp) | +$480k |
| Costs (9 months) | -$1.526M |
| **Net** | **-$546k** |

**Wait, lost money overall?**

**But interim gain was $4.666M!**

**What happened:**
- Should have closed in May at peak
- Held too long
- Stock recovered, spreads tightened
- **Gave back profits**

**Correct exit:** Closed in May

**May P/L (revised):**
- Net: +$4.666M
- **Return: 93% in 3 months**

**Lessons:**

1. **Capital structure arbitrage had correct signal** (equity overvalued vs. credit in Feb)
2. **Trade worked beautifully for 3 months** (+$4.666M)
3. **Should have taken profits** when spreads widened to 580 bp (fair value)
4. **Holding too long reversed gains** (stock can rally even with credit stress)
5. **Tesla borrow costs hurt** (5% annual drag is massive)

**Moral:** Capital structure arbitrage requires discipline to take profits. Don't get greedy.

### Example 2: GM 2008-2009 - Long Senior / Short Subordinated (Loser)

**Setup:**

- **Date:** September 2008 (Lehman bankruptcy)
- **Fund:** Multi-strategy credit hedge fund
- **Strategy:** Senior vs. subordinated arbitrage on GM

**Market conditions:**

**GM (before crisis):**
- Senior unsecured CDS: 450 bp
- Subordinated CDS: 850 bp
- **Differential: 400 bp**

**Historical differential: 250-300 bp**

**View:**
- Differential too wide (400 bp vs. 300 bp normal)
- Expect mean reversion
- Subordinated will outperform (tighten more)

**Trade:**

**Buy subordinated CDS protection (bet on tightening):**
- Notional: $20M
- Spread: 850 bp

**Sell senior CDS protection (bet on widening):**
- Notional: $20M
- Spread: 450 bp

**Net position:**
- Pay: 850 bp on subordinated
- Receive: 450 bp on senior
- **Net cost: 400 bp = $800k/year**

**Evolution - The Disaster:**

**October 2008:**
- Financial crisis intensifies
- Auto sales collapse
- GM survival questioned

**Spreads:**
- Senior: 450 → 1,200 bp (+750 bp)
- Subordinated: 850 → 3,500 bp (+2,650 bp)
- **New differential: 2,300 bp**

**The differential EXPLODED (not tightened!)**

**P/L:**

| Position | Change | DV01 | P/L |
|----------|--------|------|-----|
| Long sub protection (bought) | +2,650 bp | $80k | +$2.12M |
| Short senior (sold) | +750 bp | $60k | -$450k |
| Net premium (1 month) | | | -$67k |
| **Net** | | | **+$1.603M** |

**Huge gain! But...**

**November-December 2008:**
- Government bailout announced (TARP auto funds)
- GM will be rescued
- **Both spreads compress, but differential remains wide**

**Spreads:**
- Senior: 1,200 → 800 bp (-400 bp from peak)
- Subordinated: 3,500 → 2,000 bp (-1,500 bp from peak)
- Differential still: 1,200 bp (3x historical)

**P/L from peak:**

| Position | Change | P/L |
|----------|--------|-----|
| Long sub | -1,500 bp | -$1.2M |
| Short senior | -400 bp | +$240k |
| Net premium (2 months) | | -$133k |
| **Net** | | **-$1.093M** |

**Gave back most of gains!**

**January-March 2009:**
- GM files bankruptcy (June 2009 eventually)
- But trades intensify BEFORE filing
- Differential stays extremely wide

**Fund decision (March 2009):**
- Close position to limit losses
- **Realized loss from entry: -$1.8M**

**What went wrong:**

1. **Historical differential was wrong reference:**
   - 250-300 bp was "normal times"
   - Crisis fundamentally changed relationship
   - **New normal: 1,000-2,000 bp differential**

2. **Subordinated exploded more in crisis:**
   - Senior: 450 → 1,200 bp (2.7x)
   - Subordinated: 850 → 3,500 bp (4.1x)
   - **Subordinated more sensitive in tail events**

3. **Recovery differential widened:**
   - Pre-crisis assumption: Senior 40%, Sub 15% (25% gap)
   - Crisis reality: Senior 30%, Sub 0% (30% gap)
   - **This widened differential further**

4. **Regime change:**
   - Strategy assumed mean reversion to historical
   - But crisis created new regime
   - **Historical relationships broke down**

5. **Should have closed in October:**
   - Had +$1.6M gain
   - Got greedy, held for "normalization"
   - **Normalization never came before bankruptcy**

**Lessons:**

- **Historical spread differentials break in crisis**
- **Subordinated explodes relative to senior in distress**
- **Regime changes invalidate historical relationships**
- **Take profits in tail events** (don't wait for full normalization)

### Example 3: Hertz 2020 - Equity vs. Credit Dislocation (Winner and Loser)

**Setup:**

- **Date:** May 2020 (COVID crisis)
- **Company:** Hertz (car rental)

**Situation:**

**Hertz files bankruptcy (May 22, 2020)**

**Expectation:**
- Equity should be worth $0 (bankruptcy = equity wipeout)
- Bonds/credit should trade at recovery value (30-40 cents)

**What actually happened:**

**Equity:**
- Should be: $0
- Actual (day after bankruptcy): $0.80
- 1 week later: $2.50
- 2 weeks later: **$5.50** (!!)

**WTF?!** Bankrupt company equity rallying!

**Why:**
- Retail investors (Robinhood traders) piling in
- "It's cheap, might recover"
- Misunderstanding of bankruptcy = equity wipeout
- **Pure irrational speculation**

**Credit:**
- Bonds trading at $35-40 (40% recovery assumed)
- CDS: 5,000 bp (default certain, pricing recovery)

**The arbitrage trade:**

**Sophisticated funds:**

**Short equity at $5.50 (clearly overvalued):**
- Equity worth $0 in bankruptcy
- Short 1M shares at $5.50 = $5.5M

**Expected profit:** $5.5M (100% gain when equity → $0)

**Evolution:**

**June 2020:**
- Equity continues rallying (!)
- $5.50 → $6.00 → $4.50 → $5.00
- Volatility extreme

**Funds shorting:**
- Borrowed shares at $5.50
- Stock stayed elevated around $4-6
- **Borrow cost: 50-100% annually** (extreme)
- Hard to maintain short

**July-August 2020:**
- Bankruptcy court approves equity offering (!)
- New shares to be issued to pay creditors
- Old equity will be diluted/wiped out
- **But retail doesn't understand dilution**

**Equity:**
- Continues trading $3-5
- Funds holding short bleeding from borrow costs

**September 2020:**
- Restructuring plan finalized
- Old equity officially canceled
- Trading halted

**Final P/L for shorts:**

**Entered short: $5.50**
**Exited (when halted): $3.50** (some exited early)

| Component | Amount |
|-----------|--------|
| Short gain | $5.50 - $3.50 = $2.00/share |
| Borrow cost (4 months) | ~25% = -$1.375/share |
| **Net** | **$0.625/share** |

**On $5.5M position:** +$625k / $5.5M = **11% gain**

**Expected:** 100% gain (to zero)
**Actual:** 11% gain (borrow costs destroyed returns)

**Lesson:**

**Capital structure arbitrage failed because:**
1. **Irrational retail buying** kept equity elevated
2. **Extreme borrow costs** (50-100% annually)
3. **Time to bankruptcy resolution** (4 months) allowed bleed
4. **Eventually correct** (equity canceled) but path mattered

**Many funds gave up and covered at loss!**

**The winners:**

**Hedge funds that bought credit instead:**
- Bought bonds at $35
- Hertz emerged from bankruptcy (2021)
- Bonds recovered to $65
- **Gain: 86% in 1 year**

**Capital structure arbitrage lesson:**

**When equity is clearly overvalued (bankrupt company), consider:**
- Just long the undervalued asset (credit) instead of complex hedge
- Shorting equity has massive borrow costs + timing risk
- **Simpler = better in extreme dislocations**

---

## Best Case Scenario

### The Perfect Capital Structure Arbitrage - Lehman Brothers (2008)

**Setup:**

- **Date:** March 2008 (Bear Stearns collapsed, before Lehman)
- **Fund:** Sophisticated capital structure arbitrage specialist
- **Capital:** $100M

**Market environment:**

**Financial sector stress:**
- Bear Stearns rescued (March)
- Investment banks under pressure
- **Lehman Brothers next most vulnerable**

**Lehman Brothers (March 2008):**
- Stock price: $45
- Market cap: $25B
- Leverage: 30x (!)
- Assets: $600B, Equity: $20B
- 5-year CDS: 350 bp (investment grade!)

**Analysis:**

**The dislocation:**

**Equity market:**
- Pricing in survival + recovery
- Institutional investors long (pensions, indexes)
- Stock down from $65 but "finding support at $45"

**Credit market:**
- 350 bp CDS implies only 6% default probability
- Investment grade rating (A-)
- **Credit not pricing existential risk**

**Merton model analysis:**

Inputs:
- Leverage: 30x (insane for investment bank)
- Equity volatility: 55%
- Asset volatility: ~15% (implied)

**Model output:**
- At 30x leverage and 55% equity vol:
- Fair CDS spread: **1,500-2,000 bp** (distressed!)
- Actual: 350 bp
- **Credit massively mispriced (too tight by 1,200+ bp)**

**The perfect trade:**

**Short equity, buy CDS protection:**

1. Short 1M shares at $45 = $45M
2. Buy $150M CDS protection at 350 bp
3. Hedge ratio: 3.3x (delta-adjusted for high leverage)

**Position:**
- Short equity: $45M
- Long CDS: $150M notional
- Collateral: $15M (margin)
- CDS premium: $150M × 3.5% = $5.25M annually

**Evolution - The Perfect Storm:**

**April-May 2008:**
- Lehman reports losses
- Stock: $45 → $35 (-22%)
- CDS: 350 → 550 bp (+200 bp)

**P/L (2 months):**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | -22% | +$9.9M |
| CDS | +200 bp × $600k DV01 | +$12.0M |
| Premium (2 months) | | -$875k |
| **Net** | | **+$21.025M** |

**Return on $15M capital: 140% in 2 months!**

**June-August 2008:**
- Crisis intensifying
- Lehman scrambling for capital
- Stock: $35 → $18 (-49%)
- CDS: 550 → 1,200 bp (+650 bp)

**Cumulative P/L (5 months):**

| Component | Total P/L |
|-----------|-----------|
| Short equity | $45 → $18 = +$27M |
| CDS | 350 → 1,200 = +$51M |
| Premium (5 months) | -$2.2M |
| **Net** | **+$75.8M** |

**Return on $15M: 505% in 5 months!**

**September 2008: The Endgame:**

**September 15, 2008: Lehman files bankruptcy**

**Final prices:**
- Stock: $18 → $0 (halted, delisted)
- CDS: Triggered credit event

**CDS settlement:**
- Auction recovery: **8.6%**
- CDS payout: (100 - 8.6) × $150M = **$137.1M**

**Final P/L:**

| Component | P/L |
|-----------|-----|
| Short equity | $45 → $0 = +$45M |
| CDS payout | +$137.1M |
| CDS premium (6 months) | -$2.625M |
| Borrow costs | -$1.125M |
| **Total** | **+$178.25M** |

**On $15M capital: 1,188% return in 6 months!**

**Fund decision: Close position at bankruptcy**

- Covered short at $0 (bought back shares for pennies)
- CDS settled at auction
- **Locked in $178.25M profit**

**Full attribution:**

| Source | Amount | % of Total |
|--------|--------|------------|
| Equity short | $45M | 25% |
| CDS gain | $137.1M | 77% |
| Costs | -$3.75M | -2% |
| **Total** | **$178.25M** | **100%** |

**Why this was best case:**

1. **Perfect entry timing:**
   - Entered March 2008 (6 months before bankruptcy)
   - Just after Bear Stearns (warning sign)
   - Before credit spreads widened materially

2. **Massive mispricing:**
   - CDS at 350 bp (IG-rated)
   - Should have been 1,500-2,000 bp
   - **1,200+ bp mispricing = huge opportunity**

3. **Equity also overvalued:**
   - Stock at $45 (down from $65 but still high)
   - Should have been <$10 given leverage/stress
   - **Both legs profitable**

4. **Hedge ratio optimal:**
   - 3.3x notional (CDS/equity)
   - Matched deltas perfectly
   - Neither over- nor under-hedged

5. **Event occurred quickly:**
   - Only 6 months from entry to bankruptcy
   - Minimized carry costs
   - Maximized compound returns

6. **Recovery very low (8.6%):**
   - Amplified CDS payout
   - Expected 30-40%, actual 8.6%
   - **Extra $30M+ gain from low recovery**

7. **No early exit temptation:**
   - Fund had conviction
   - Held through $21M gain (month 2)
   - Held through $75M gain (month 5)
   - **Captured full $178M at bankruptcy**

**Comparison to other trades:**

| Alternative | Return | Notes |
|-------------|--------|-------|
| **Actual trade** | **+1,188%** | **Short equity + long CDS** |
| Just short equity | +300% | $45 → $0, but huge borrow costs |
| Just buy CDS | +3,614% | On $15M CDS premium, but no equity hedge |
| Buy puts | +400% | OTM puts, but premium expensive |

**Capital structure arbitrage was optimal structure:**
- Hedged (long credit, short equity)
- Leveraged via CDS
- Low capital requirement
- Massive asymmetry

**This trade exemplifies the theoretical foundation of capital structure arbitrage:**

$$
\text{Equity overvalued} + \text{Credit underpricing risk} = \text{Perfect arbitrage}
$$

When both hold simultaneously, returns can be extraordinary.

---

## Worst Case Scenario

### The Crushing Loss - AMC 2021 Meme Stock Reversal

**Setup:**

- **Date:** January 2021
- **Fund:** Quantitative hedge fund
- **Strategy:** Short meme stocks, hedge with credit
- **Capital:** $200M

**Market environment:**

**Meme stock mania:**
- GameStop squeezing
- Reddit/WallStreetBets pumping stocks
- AMC Entertainment caught up in frenzy

**AMC Entertainment (January 2021):**
- Stock price: $5
- Market cap: $500M
- Fundamentals: Terrible (COVID, theaters closed)
- Debt: $5B
- CDS: 3,500 bp (distressed, near-default)
- **Bankruptcy expected by many**

**Analysis (Fundamental):**

**Equity should be worth near-zero:**
- $5B debt vs. $500M equity
- Massive losses (COVID closed theaters)
- Cash burn: $100M/month
- **Bankruptcy within 6 months likely**

**Credit correctly pricing distress:**
- 3,500 bp = 40%+ default probability
- Bonds at $30-40 (60-70% loss expected)

**Merton model:**
- Extreme leverage (10x debt/equity)
- Equity should be $1-2, not $5

**The "obvious" trade:**

**Short equity (overvalued), buy CDS (insurance):**

1. Short 10M shares at $5 = $50M
2. Buy $150M CDS protection at 3,500 bp
3. **Expected:** Equity → $0, profit $50M + CDS gain

**Costs:**
- CDS premium: $150M × 35% = $52.5M annually (!!)
- Short borrow: 10% = $5M annually
- **Total carry: $57.5M annually**

**This should print money, right?**

**Evolution - The Nightmare:**

**February 2021:**
- Retail buying pressure
- Stock: $5 → $8 (+60%)
- CDS: 3,500 → 3,200 bp (stable)

**P/L (1 month):**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | +60% | -$30M |
| CDS | -300 bp | +$4.5M |
| Costs (1 month) | | -$4.8M |
| **Net** | | **-$30.3M** |

**Down 15% in 1 month! But "fundamentals haven't changed, hold on..."**

**March 2021:**
- More retail buying
- Stock: $8 → $14 (+75%)
- CDS: 3,200 → 2,800 bp (-400 bp)

**Additional loss:**

| Position | Change | P/L |
|----------|--------|-----|
| Short equity | +75% | -$60M |
| CDS | -400 bp | +$6M |
| Costs | | -$4.8M |
| **Net** | | **-$58.8M** |

**Cumulative: -$89M (-44.5% of capital)**

**Risk manager:** "Close this position, it's killing us!"

**Portfolio manager:** "But fundamentals say it should go to zero! Let me add to the short!"

**Fatal mistake: Averaged down**

**Added $50M more short at $14:**
- Total short: $100M notional
- Average price: $9.50
- CDS: Increased to $200M notional

**May-June 2021: The Meme Squeeze**

**June 2021:**
- AMC announces equity raise (dilution)
- Stock rallies on the news (!!)
- Stock: $14 → **$72** (+414%!)

**The wipeout:**

| Position | P/L |
|----------|-----|
| Short $50M at $5 | $5 → $72 = -$67M (-1,340%) |
| Short $50M at $14 | $14 → $72 = -$58M (-414%) |
| **Total short loss** | **-$125M** |
| CDS | Improved to 1,800 bp = +$34M |
| Costs (5 months) | -$24M |
| **Net** | **-$115M** |

**Lost 57.5% of fund capital on ONE trade!**

**Forced liquidation:**

**June 2021:**
- Prime broker margin call
- Forced to cover shorts at $72
- **Realized losses: -$115M**

**The aftermath:**

**2 months later (August 2021):**
- AMC stock: $72 → $38 (-47%)
- "Fundamentals" reasserting
- **If held, would have recovered $34M of losses**

**But couldn't hold - blown out by margin calls.**

**1 year later (June 2022):**
- AMC: $38 → $12 (-68% from peak)
- **If held, would have recovered $60M**

**2 years later (2023):**
- AMC: $12 → $5 (back to entry!)
- **Fundamentals were right, timing was disaster**

**What went catastrophically wrong:**

1. **Ignored market dynamics:**
   - Focused on fundamentals only
   - Ignored technical (short squeeze risk)
   - **Meme stocks don't follow fundamentals**

2. **Underestimated retail power:**
   - Assumed retail would capitulate
   - Instead, they doubled down
   - **WallStreetBets coordination**

3. **Averaged down (fatal error):**
   - Turned bad trade into catastrophic
   - $50M → $100M exposure
   - **Doubled down on losing trade**

4. **Ignored borrow costs:**
   - 10% annual borrow = 0.83% monthly
   - On $100M = $833k/month bleed
   - **Carry costs unbearable**

5. **CDS hedge ineffective:**
   - CDS responds to default risk
   - Stock squeeze ≠ default risk
   - **Credit didn't move with equity**
   - Paid 35% premium for hedge that didn't work

6. **Leverage (implicit):**
   - $200M fund
   - $100M short + $200M CDS notional
   - **Concentration way too high (50% in one trade)**

7. **No stop loss:**
   - Should have exited at -20% (-$40M)
   - Instead held to -57.5% (-$115M)
   - **Pride and "fundamental conviction" destroyed capital**

8. **Wrong instrument for thesis:**
   - If bearish on AMC, should:
     - Buy puts (defined risk)
     - Or just buy CDS alone (no equity short)
   - **Short + CDS was over-hedged and over-exposed**

**Theoretical vs. Practical:**

**Merton model said:**
- AMC equity worth $1-2
- Credit spreads correct at 3,500 bp
- **Short equity = free money**

**Market reality:**
- Equity went to $72 (14x "fair value")
- Stayed elevated for months
- **Fundamentals don't matter in manias**

**The lesson:**

$$
\text{Capital Structure Arbitrage} \neq \text{Short Squeeze Protection}
$$

**Capital structure arbitrage works when:**
- Markets are rational
- Information flows normally
- No technical squeezes

**Capital structure arbitrage FAILS when:**
- Retail manias
- Short squeezes
- Memes override fundamentals
- Borrow costs prohibitive

**AMC 2021 proved:** You can be right on fundamentals and still get destroyed on timing and market dynamics.

---

## What to Remember

### Core Concept

**Capital structure arbitrage exploits mispricings between securities of the same company:**

$$
\text{Firm Value} = \text{Equity} + \text{Debt}
$$

- All securities are claims on same assets
- Should move together based on structural relationships
- When relationships break → Arbitrage opportunity
- Long undervalued security, short overvalued
- Market-neutral to firm value

### Merton Model Framework

**Equity as call option:**

$$
E = \max(V - D, 0)
$$

**Debt as short put:**

$$
D_{\text{risky}} = D_{\text{risk-free}} - \text{Put}(V, D)
$$

**Key deltas:**

$$
\Delta_E + \Delta_D = 1
$$

- Healthy firm: $\Delta_E \approx 0.8$, $\Delta_D \approx 0.2$
- Distressed: $\Delta_E \approx 0.3$, $\Delta_D \approx 0.7$

### Hedge Ratio Calculation

$$
\text{CDS Notional} = \frac{\text{Equity Position} \times \Delta_E}{\Delta_D}
$$

**Example:**
- Short $10M equity
- $\Delta_E = 0.65$, $\Delta_D = 0.35$
- CDS notional: $10M × (0.65/0.35) = **$18.6M**

### Entry Checklist

**For long credit / short equity:**

1. **Valuation gap:**
   - [ ] Equity pricing low default probability
   - [ ] Credit pricing high default probability
   - [ ] Merton model confirms mispricing

2. **Catalyst:**
   - [ ] Identified event or trend
   - [ ] Not just valuation gap
   - [ ] Timeframe reasonable (<12 months)

3. **Technical:**
   - [ ] Borrow available for short
   - [ ] Borrow cost <5% annually
   - [ ] CDS liquid (bid-ask <10 bp)

4. **Risk management:**
   - [ ] Position size <10% of fund
   - [ ] Stop loss defined (-25%)
   - [ ] Hedge ratio calculated

### Common Strategies

**1. Long credit / Short equity:**
- When equity overvalued vs. credit
- Most common
- Works in deterioration scenarios

**2. Short credit / Long equity:**
- When credit overpriced vs. equity
- Rare (credit usually lags equity)
- Works in recovery scenarios

**3. Senior vs. Subordinated:**
- Spread differential mean reversion
- Less directional
- Lower returns but more stable

**4. Equity puts vs. CDS:**
- Volatility arbitrage
- Exploit put vol vs. CDS mispricing
- Advanced

### Exit Rules

**Close position when:**

1. **Profit target hit:**
   - Long credit/short equity: +25-50%
   - Senior/sub: +15-30%
   - **Lock in gains, don't get greedy**

2. **Thesis invalidated:**
   - Fundamental view changed
   - Capital raised (strengthens balance sheet)
   - Business improvement

3. **Stop loss triggered:**
   - Position down 25%
   - **Never let winners turn into losers**

4. **Time stop:**
   - Held 12 months with no movement
   - Carry costs mounting
   - Opportunity cost

5. **Technical squeeze:**
   - Short squeeze developing (equity)
   - Borrow costs >10%
   - **Exit before forced liquidation**

### Position Sizing

**Conservative:**

$$
\text{Position Size} = \min\left(10\% \text{ of fund}, \frac{5\%}{\text{Equity Beta}}\right)
$$

**Example:**
- Fund: $100M
- Equity beta: 1.5
- Max: min($10M, $3.33M) = **$3.33M**

**Leverage limits:**
- Total notional (equity + CDS): <2x fund
- Any single position: <10% of fund

### Common Mistakes

1. **Ignoring borrow costs**
   - 5-10% annual drag kills returns
   - Calculate breakeven including costs

2. **Wrong hedge ratio**
   - Using 1:1 instead of delta-adjusted
   - Results in directional exposure

3. **Averaging down**
   - Turning bad trade into disaster
   - Never add to losing capital structure trade

4. **No catalyst**
   - Just "valuation gap" insufficient
   - Need event or trend

5. **Ignoring technical factors**
   - Short squeezes
   - Meme stock dynamics
   - Retail coordination

6. **Overleveraging**
   - Using too much of fund on one trade
   - One bad trade can blow up fund

7. **Holding too long**
   - Not taking profits
   - Waiting for "perfect" convergence
   - Carry costs mount

8. **Wrong maturity**
   - Shorting equity with 1-year CDS
   - Maturity mismatch creates basis risk

### Performance Expectations

**Long credit / Short equity:**

| Outcome | Probability | Return | Notes |
|---------|-------------|--------|-------|
| Big win | 10% | +100% | Default or major deterioration |
| Good | 25% | +25-50% | Spreads widen, equity falls |
| Breakeven | 35% | 0-10% | Small moves, carry drag |
| Small loss | 25% | -10-25% | Wrong timing, carry costs |
| Big loss | 5% | -50% | Squeeze, averaged down |

**Expected return: 5-15% annually**
**Sharpe ratio: 0.8-1.2**

### Risk Metrics

**Key risks to monitor:**

1. **Short squeeze risk:**
   - Short interest as % of float
   - Borrow cost trend
   - Social media mentions

2. **Carry bleed:**
   - Daily cost: CDS premium + borrow
   - Breakeven: How much spread widening needed

3. **Correlation:**
   - Equity-credit correlation
   - Should be high (0.6-0.8)
   - If breaks down, hedge fails

4. **Leverage drift:**
   - As firm value changes, $\Delta_E$ and $\Delta_D$ change
   - Need to rebalance hedge ratio

### Your Learning Path

**Phase 1 (Months 1-3): Theory**
- Study Merton model
- Calculate deltas manually
- Understand credit-equity relationships
- Paper trade scenarios

**Phase 2 (Months 4-6): Analysis**
- Build screening tools
- Identify mispricings
- Calculate hedge ratios
- Backtest signals

**Phase 3 (Months 7-12): Small positions**
- Trade 1-2% of fund
- Focus on execution
- Learn from mistakes
- Build track record

**Phase 4 (Year 2+): Full implementation**
- 5-10% per position
- Multiple positions
- Systematic process
- Advanced structures

### Final Wisdom

> "Capital structure arbitrage is intellectually beautiful—the Merton model elegantly describes how equity and debt should move together. But the market is messier than theory. Equity can decouple from credit for months or years. Meme stocks can rally 10x despite bankruptcy risk. Borrow costs can reach 50-100% annually. The successful practitioner knows when theory applies (rational markets, information-driven) and when it doesn't (manias, squeezes, retail coordination). The Lehman trade (2008) was perfect because both equity and credit were mispriced, catalysts were clear, and fundamentals dominated. The AMC trade (2021) was catastrophic because technicals trumped fundamentals, retail coordinated against shorts, and timing was everything. Know the difference."

**Keys to success:**

1. **Use Merton model as framework** (not gospel)
2. **Calculate proper hedge ratios** (delta-adjusted)
3. **Monitor borrow costs daily** (can destroy returns)
4. **Take profits aggressively** (don't wait for perfection)
5. **Set hard stop losses** (-25% maximum)
6. **Avoid meme stocks entirely** (fundamentals don't matter)
7. **Size conservatively** (<10% per position)
8. **Have clear catalyst** (not just valuation gap)

**Most critical rule:**

$$
\text{Fundamental mispricing} + \text{Technical setup} + \text{Catalyst} = \text{Trade}
$$

Missing any of the three = Pass.

Capital structure arbitrage works when markets are rational and information-driven. It fails spectacularly when technicals, squeezes, or manias dominate. The AMC disaster proves that being right on fundamentals is insufficient. You must also be right on timing, market dynamics, and technical factors. The great capital structure trades (Lehman 2008) combined fundamental mispricing with clear catalysts and normal market conditions. Pick your spots carefully. 🎯📊
