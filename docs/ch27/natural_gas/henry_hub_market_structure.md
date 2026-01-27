# Henry Hub and Natural Gas Market Structure

## Learning Objectives

By the end of this section, you will be able to:

- Understand the physical and financial structure of natural gas markets
- Navigate the NYMEX natural gas futures contract specifications
- Interpret Henry Hub as a benchmark pricing point
- Analyze the relationship between physical and paper markets

---

## 1. Henry Hub: The Benchmark

### 1.1 What is Henry Hub?

**Henry Hub** is a natural gas pipeline interconnection located in Erath, Louisiana. It serves as the official delivery point for NYMEX natural gas futures contracts and the benchmark for natural gas pricing in North America.

**Why Henry Hub?**

1. **Geographic centrality**: Located near major production basins and consumption centers
2. **Pipeline connectivity**: Interconnects 13 major interstate and intrastate pipelines
3. **Liquidity**: Highest volume trading point in North America
4. **Historical precedent**: Established as benchmark since 1990

### 1.2 Pipeline Network

```
                    ┌─────────────────────────────────────┐
                    │         HENRY HUB                   │
                    │      Erath, Louisiana               │
                    └─────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
   Gulf Coast               Northeast                      Midwest
   Production               Consumption                   Markets
   (Permian,                (Boston,                     (Chicago,
    Haynesville)            New York)                    Detroit)
```

### 1.3 Hub Pricing Differentials

Other locations price as a differential (basis) to Henry Hub:

$$
P_{\text{location}} = P_{\text{Henry Hub}} + \text{Basis}_{\text{location}}
$$

| Location | Typical Basis | Basis Volatility |
|----------|--------------|------------------|
| Algonquin (Boston) | +$0.50 to +$5.00 | Very High (winter) |
| Chicago Citygate | -$0.10 to +$0.30 | Moderate |
| SoCal Citygate | -$0.20 to +$1.00 | High |
| Waha (Permian) | -$1.00 to +$0.20 | Moderate |

---

## 2. NYMEX Natural Gas Futures

### 2.1 Contract Specifications

| Specification | Detail |
|---------------|--------|
| **Exchange** | NYMEX (CME Group) |
| **Symbol** | NG |
| **Contract Size** | 10,000 MMBtu |
| **Price Quote** | USD per MMBtu |
| **Tick Size** | $0.001 = $10 per contract |
| **Trading Hours** | Nearly 24/6 (Sunday-Friday) |
| **Delivery** | Physical at Henry Hub |
| **Expiration** | 3 business days before 1st of delivery month |

### 2.2 Understanding MMBtu

**MMBtu** = Million British Thermal Units

$$
1 \text{ MMBtu} \approx 293 \text{ kWh} \approx 1,000 \text{ cubic feet of NG}
$$

**Energy Content Comparison:**

| Fuel | Energy per Unit | MMBtu Equivalent |
|------|-----------------|------------------|
| Natural Gas | 1,030 Btu/cf | 1 MMBtu ≈ 1 Mcf |
| Crude Oil | 5.8 MMBtu/bbl | 1 bbl ≈ 5.8 MMBtu |
| Coal | 20 MMBtu/ton | 1 ton ≈ 20 MMBtu |

### 2.3 Contract Months and Term Structure

Natural gas futures trade up to 12 years forward, but liquidity concentrates in:

- **Prompt month**: Most liquid, closest to delivery
- **Balance of season**: Current heating/cooling season
- **Cal strips**: Full calendar year contracts
- **Seasonal**: Winter (Nov-Mar) or Summer (Apr-Oct)

---

## 3. Price Discovery and Market Mechanics

### 3.1 Daily Price References

| Price Point | Timing | Use |
|-------------|--------|-----|
| NYMEX Settlement | 2:30 PM ET | Futures mark-to-market |
| ICE Daily Index | 11:30 AM ET | Physical trading reference |
| Platts Day-Ahead | 2:00 PM ET | Bilateral contracts |
| Platts Bidweek | Monthly | Monthly physical pricing |

### 3.2 The Price Display

When you see: **NG 5.28 USD/MMBtu (26.02.)**

This means:

- Commodity: Natural Gas (Henry Hub)
- Price: $5.28 per million BTU
- Contract: February 2026 delivery
- Settlement: Price for delivery at Henry Hub in February

### 3.3 Contract Value Calculation

For a January 2026 contract at $5.28/MMBtu:

$$
\text{Contract Value} = 5.28 \times 10,000 = \$52,800
$$

**Margin Requirements** (approximate):

| Position | Initial Margin | Maintenance Margin |
|----------|---------------|-------------------|
| Outright | $4,500 | $3,500 |
| Calendar Spread | $350-$800 | $280-$650 |

---

## 4. Why Natural Gas is Uniquely Weather-Sensitive

Natural gas exhibits the highest weather sensitivity among major commodities. The January 2026 "Polar Express" event demonstrated this dramatically: **prices surged 70% in just one week** (from $3.10 to $5.28/MMBtu). Understanding the structural reasons behind this extreme sensitivity is essential for weather-based trading.

### 4.1 The Four Structural Factors

| Factor | Characteristic | Impact on Price Volatility |
|--------|----------------|---------------------------|
| **Storage Constraints** | Unlike oil, large-scale above-ground storage is not economically viable | Supply cannot be easily stockpiled; shortages hit immediately |
| **Demand Inelasticity** | Heating demand is non-discretionary; people must heat their homes | Demand doesn't decrease much even when prices spike |
| **Supply Rigidity** | Production cannot be rapidly increased | Short-term supply is essentially fixed |
| **Strong Seasonality** | Clear winter heating / summer cooling patterns | Predictable demand cycles amplify weather deviations |

### 4.2 Storage Constraints: The Critical Difference

**Oil vs. Natural Gas Storage:**

```
┌─────────────────────────────────────────────────────────────────┐
│                        CRUDE OIL                                │
├─────────────────────────────────────────────────────────────────┤
│  • Liquid at room temperature                                   │
│  • Easy to store in tanks (above ground)                        │
│  • Strategic Petroleum Reserve: 700+ million barrels            │
│  • Can store months of consumption                              │
│  • Price spikes can be buffered by releasing reserves           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      NATURAL GAS                                │
├─────────────────────────────────────────────────────────────────┤
│  • Gas at room temperature (must compress or liquefy)           │
│  • Requires underground storage (depleted fields, caverns)      │
│  • Total US storage: ~4,000 Bcf (limited capacity)              │
│  • Stores only ~45 days of peak winter consumption              │
│  • Once storage depletes, no buffer remains                     │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 Demand Inelasticity: Non-Discretionary Consumption

When temperatures drop to -20°F, consumers **must** heat their homes regardless of price:

$$
\text{Price Elasticity of Heating Demand} \approx -0.1 \text{ to } -0.3
$$

This means a **10% price increase reduces demand by only 1-3%**.

**Comparison of Demand Elasticity:**

| Commodity | Short-Run Elasticity | Implication |
|-----------|---------------------|-------------|
| Natural Gas (heating) | -0.1 to -0.3 | Nearly inelastic |
| Gasoline | -0.2 to -0.4 | Low elasticity |
| Electricity | -0.3 to -0.5 | Moderate |
| Airline tickets | -1.0 to -2.0 | Elastic |

### 4.4 Supply Rigidity: Fixed in the Short Term

Natural gas production cannot respond quickly to price signals:

```python
def supply_response_timeline():
    """
    Timeline for supply to respond to price increase
    """
    responses = {
        'Immediate (hours)': {
            'action': 'None possible',
            'impact': '0%',
            'reason': 'Wells produce at capacity'
        },
        'Short-term (days)': {
            'action': 'Minor flow adjustments',
            'impact': '1-2%',
            'reason': 'Limited operational flexibility'
        },
        'Medium-term (weeks)': {
            'action': 'Restart shut-in wells',
            'impact': '3-5%',
            'reason': 'Requires maintenance, crew'
        },
        'Long-term (months)': {
            'action': 'Drill new wells',
            'impact': '10%+',
            'reason': 'Capital investment, permits'
        }
    }
    return responses
```

**Key insight**: During a 5-day cold snap, supply is essentially **fixed**. All price adjustment must come from demand destruction or storage withdrawal.

### 4.5 Seasonality: Amplifying Weather Deviations

Natural gas demand follows a clear seasonal pattern:

| Season | Avg Daily Demand | Primary Driver | Weather Sensitivity |
|--------|-----------------|----------------|---------------------|
| Winter (Dec-Feb) | 100-120 Bcf/d | Heating | **Extreme** |
| Shoulder (Mar-Apr, Oct-Nov) | 70-80 Bcf/d | Mixed | Moderate |
| Summer (Jun-Aug) | 80-90 Bcf/d | Cooling (power) | High |
| Spring (May) | 65-75 Bcf/d | Baseline | Low |

**The Amplification Effect:**

When a cold snap occurs during peak winter:
- Baseline demand is already high (100 Bcf/d)
- Weather adds incremental demand (+20-30 Bcf/d)
- Storage withdrawal accelerates
- Supply cannot respond
- **Price must rise to destroy marginal demand**

### 4.6 The Perfect Storm: January 2026 "Polar Express"

The 70% price surge in January 2026 resulted from all four factors combining:

| Factor | January 2026 Condition | Contribution |
|--------|----------------------|--------------|
| Storage | 3,065 Bcf (slightly below average) | Moderate concern |
| Demand | +40% above normal (extreme cold) | **Primary driver** |
| Supply | Fixed (no response possible) | Amplified shortage |
| Seasonality | Peak winter demand period | Maximum vulnerability |

$$
\text{Price Impact} = f(\text{Storage Tightness}) \times f(\text{Demand Shock}) \times f(\text{Supply Rigidity})
$$

When storage is below average AND demand spikes AND supply cannot respond, price moves become **non-linear** and extreme.

!!! warning "The 70% Rule"
    From [Mer's Blog analysis](https://blog.naver.com/ranto28/224159783476): Natural gas prices can move 70%+ in a week during extreme weather precisely because of these structural factors. No other major commodity exhibits this combination of storage constraints, demand inelasticity, supply rigidity, and seasonality.

---

## 5. Supply and Demand Fundamentals

### 5.1 Supply Sources

**US Production (~105 Bcf/day in 2025-2026):**

| Basin | Production | Characteristics |
|-------|------------|-----------------|
| Appalachian (Marcellus/Utica) | 35 Bcf/d | Dry gas, constrained takeaway |
| Permian | 20 Bcf/d | Associated gas, oil-driven |
| Haynesville | 15 Bcf/d | Flexible, close to Gulf |
| Other | 35 Bcf/d | Diverse regions |

**Key Supply Metrics:**

$$
\text{Supply Adequacy} = \frac{\text{Storage} + \text{Production} \times \text{Days}}{\text{Expected Demand} \times \text{Days}}
$$

### 5.2 Demand Segments

**US Natural Gas Demand (~90-100 Bcf/day):**

| Segment | Share | Weather Sensitivity |
|---------|-------|---------------------|
| Electric Power | 35% | High (seasonal) |
| Residential/Commercial | 25% | Very High (HDD-driven) |
| Industrial | 25% | Low (relatively stable) |
| LNG Exports | 15% | Low (contracted) |

### 5.3 The Storage Cycle

Natural gas storage follows a predictable seasonal pattern:

```
           Bcf
         3,500 │                         ┌───┐
               │                    ┌────┘   │
         3,000 │               ┌────┘        │
               │          ┌────┘             │
         2,500 │     ┌────┘                  └───┐
               │┌────┘                           │
         2,000 ││                                └───┐
               ││                                    └───┐
         1,500 │┘                                        └──
               └────────────────────────────────────────────
               Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
               
               ← Withdrawal Season →    ← Injection Season →
```

---

## 6. Weather-Price Relationship

### 6.1 The Demand Equation

Natural gas demand is strongly correlated with temperature:

$$
D = \alpha + \beta_1 \cdot \text{HDD} + \beta_2 \cdot \text{CDD} + \gamma \cdot \text{Industrial} + \epsilon
$$

Typical winter coefficients:

$$
\frac{\partial D}{\partial \text{HDD}} \approx 3-5 \text{ Bcf per HDD}
$$

### 6.2 Price Sensitivity

The relationship between HDD surprise and price:

$$
\Delta P \approx \kappa \cdot \frac{\text{HDD}_{\text{forecast}} - \text{HDD}_{\text{normal}}}{\text{HDD}_{\text{normal}}}
$$

where $\kappa$ varies with storage levels:

| Storage vs. 5-Year Avg | $\kappa$ (price elasticity) |
|------------------------|-----------------------------|
| >10% above | Low (0.3-0.5) |
| ±10% | Moderate (0.5-0.8) |
| >10% below | High (0.8-1.5) |
| >20% below | Very High (1.5-3.0) |

### 6.3 The January 2026 Example

From the Mer's Blog article:

| Metric | Value | Implication |
|--------|-------|-------------|
| Price 5 days ago | $3.10/MMBtu | Starting point |
| Price current | $5.28/MMBtu | 70% increase |
| Storage draw | 120 Bcf/week | Above normal |
| Temperature anomaly | -20 to -40°F | Extreme cold |

Price move calculation:

$$
\frac{\$5.28 - \$3.10}{\$3.10} = +70.3\%
$$

---

## 7. Market Structure and Participants

### 7.1 Participant Categories

| Category | Role | Position Bias |
|----------|------|--------------|
| **Producers** | Hedge production | Net short |
| **Utilities** | Secure supply | Net long |
| **Marketers** | Physical trading | Neutral |
| **Hedge Funds** | Speculation | Variable |
| **Index Funds** | Passive long | Net long |
| **Prop Traders** | Short-term trading | Neutral |

### 7.2 Commitment of Traders (COT) Data

CFTC releases weekly positioning data:

```python
def analyze_cot_positioning(cot_data):
    """
    Analyze CFTC Commitment of Traders data
    
    Parameters:
    -----------
    cot_data : DataFrame
        Weekly COT report data
    
    Returns:
    --------
    signal : dict
        Positioning analysis
    """
    # Net speculative position
    spec_net = cot_data['MM_Long'] - cot_data['MM_Short']
    
    # Historical percentile
    percentile = (spec_net - cot_data['MM_Net'].min()) / \
                 (cot_data['MM_Net'].max() - cot_data['MM_Net'].min())
    
    # Producer hedging
    prod_net = cot_data['Prod_Long'] - cot_data['Prod_Short']
    
    signal = {
        'spec_net': spec_net,
        'spec_percentile': percentile,
        'producer_hedge': prod_net,
        'crowding_risk': percentile > 0.8 or percentile < 0.2
    }
    
    return signal
```

---

## 8. Related Instruments

### 8.1 Natural Gas ETFs

| Ticker | Name | Strategy | Expense Ratio |
|--------|------|----------|---------------|
| **UNG** | US Natural Gas Fund | Prompt month | 1.11% |
| **BOIL** | 2x Natural Gas Bull | 2x leveraged | 1.01% |
| **KOLD** | 2x Natural Gas Bear | -2x leveraged | 1.01% |
| **GAZ** | iPath Series B | Diversified | 0.75% |

!!! warning "Contango Decay"
    Natural gas ETFs suffer from severe contango decay. UNG lost ~95% of its value from 2012-2020 despite spot prices being relatively stable. These are short-term trading instruments, not investments.

### 8.2 Natural Gas Equities

| Company | Ticker | Exposure Type |
|---------|--------|---------------|
| EQT Corporation | EQT | Pure-play producer |
| Chesapeake Energy | CHK | Large producer |
| Antero Resources | AR | Appalachian producer |
| Kinder Morgan | KMI | Pipeline/midstream |
| Cheniere Energy | LNG | LNG export |

### 8.3 Spread Products

| Spread | Components | Rationale |
|--------|------------|-----------|
| **Calendar** | NG nearby vs deferred | Seasonal/storage |
| **Spark** | NG vs Power | Generation economics |
| **Crack** | NG vs Oil (NGL) | Petrochemical value |
| **Basis** | Henry Hub vs regional | Transportation |

---

## 9. Trading Mechanics

### 9.1 Order Types

```python
# Example: Natural gas trading orders

# Market order - immediate execution
market_buy = {
    'symbol': 'NGG26',  # February 2026
    'side': 'BUY',
    'quantity': 5,
    'order_type': 'MARKET'
}

# Limit order - price specified
limit_buy = {
    'symbol': 'NGG26',
    'side': 'BUY', 
    'quantity': 5,
    'order_type': 'LIMIT',
    'price': 5.15
}

# Stop order - trigger at price
stop_loss = {
    'symbol': 'NGG26',
    'side': 'SELL',
    'quantity': 5,
    'order_type': 'STOP',
    'stop_price': 4.80
}

# Calendar spread order
calendar_spread = {
    'leg1': {'symbol': 'NGG26', 'side': 'BUY', 'ratio': 1},
    'leg2': {'symbol': 'NGH26', 'side': 'SELL', 'ratio': 1},
    'spread_price': -0.15  # Feb at discount to March
}
```

### 9.2 Settlement Process

**Physical Settlement (rare for speculators):**

1. Last trading day: 3 business days before first of delivery month
2. Delivery period: Throughout delivery month
3. Location: Henry Hub delivery point
4. Alternative delivery points available with basis adjustment

**Cash Settlement (typical):**

1. Close position before expiration
2. Mark-to-market settlement daily
3. No physical delivery obligation

---

## 10. Risk Management

### 10.1 Position Limits

CFTC imposes speculative position limits:

| Month | Spot Month | Single Month | All Months |
|-------|-----------|--------------|-----------|
| Limit | 2,000 | 6,000 | 12,000 |

### 10.2 Volatility Considerations

Natural gas is one of the most volatile commodities:

| Metric | Natural Gas | Crude Oil | S&P 500 |
|--------|------------|-----------|---------|
| Avg Daily Move | 3.5% | 1.8% | 0.9% |
| Max Daily Move | 40%+ | 15%+ | 12%+ |
| Annual Vol | 60-80% | 30-40% | 15-20% |

### 10.3 Risk Sizing

```python
def calculate_ng_position_size(
    account_value: float,
    risk_per_trade: float,
    stop_distance: float,
    contract_size: int = 10000
) -> int:
    """
    Calculate appropriate position size for natural gas
    
    Parameters:
    -----------
    account_value : float
        Total account value in USD
    risk_per_trade : float
        Maximum risk as fraction of account (e.g., 0.02 for 2%)
    stop_distance : float
        Stop loss distance in $/MMBtu
    contract_size : int
        Contract size (10,000 MMBtu for NG)
    
    Returns:
    --------
    contracts : int
        Number of contracts to trade
    """
    risk_amount = account_value * risk_per_trade
    risk_per_contract = stop_distance * contract_size
    contracts = int(risk_amount / risk_per_contract)
    
    return max(1, contracts)

# Example: $100,000 account, 2% risk, $0.30 stop
# position = calculate_ng_position_size(100000, 0.02, 0.30)
# = int(2000 / 3000) = 0 → 1 contract minimum
```

---

## 11. Summary

Understanding Henry Hub and natural gas market structure is essential for weather-based trading:

1. **Henry Hub** is the benchmark pricing point with deep liquidity
2. **Contract specifications** determine trading mechanics and risk
3. **Storage cycle** creates predictable seasonal patterns
4. **Weather sensitivity** is highest during injection/withdrawal periods
5. **Position sizing** must account for extreme volatility

The combination of high weather sensitivity, structural storage constraints, and inelastic demand creates significant trading opportunities during extreme weather events.

---

## References

1. Considine, T.J., & Larson, D.F. (2001). "Risk Premiums on Inventory Assets: The Case of Crude Oil and Natural Gas." *Journal of Futures Markets*
2. Suenaga, H., Smith, A., & Williams, J. (2008). "Volatility Dynamics of NYMEX Natural Gas Futures Prices." *Journal of Derivatives*
3. Linn, S.C., & Zhu, Z. (2004). "Natural Gas Prices and the Gas Storage Report." *Journal of Futures Markets*
4. CME Group. "Henry Hub Natural Gas Futures Contract Specifications."

---

!!! info "Next Section"
    Continue to [Natural Gas Storage and Inventory](../natural_gas/storage_and_inventory.md) to understand the critical role of storage data in price formation.
