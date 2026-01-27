# Seasonal Spread Trading Strategies

## Learning Objectives

By the end of this section, you will be able to:

- Design and implement calendar spread strategies based on weather forecasts
- Understand the mechanics of contango and backwardation in natural gas
- Calculate optimal spread positions based on storage projections
- Manage risk in spread trading through scenario analysis

---

## 1. Calendar Spread Fundamentals

### 1.1 What is a Calendar Spread?

A calendar spread involves simultaneously buying and selling futures contracts of the same commodity with different delivery months:

$$
\text{Spread} = F_{T_1} - F_{T_2}
$$

where $T_1 < T_2$ (near month minus far month).

**Position Types:**

| Position | Long | Short | Profit When |
|----------|------|-------|-------------|
| Bull Spread | Near month | Far month | Spread widens (backwardation) |
| Bear Spread | Far month | Near month | Spread narrows (contango) |

### 1.2 Natural Gas Term Structure Regimes

Natural gas exhibits distinct term structure patterns:

**Contango (Normal):**
- Far months > Near months
- Typical during adequate storage
- Reflects storage costs

$$
F_{T_2} > F_{T_1} + \text{Storage Cost}
$$

**Backwardation (Inverted):**
- Near months > Far months
- Occurs during supply stress or extreme demand
- Reflects convenience yield

$$
F_{T_1} > F_{T_2} + \text{Convenience Yield}
$$

### 1.3 The Winter-Summer Spread

The most fundamental NG spread:

$$
\text{Winter-Summer} = F_{\text{Jan}} - F_{\text{Jul}}
$$

**Historical Patterns:**

| Storage Condition | Typical Spread | Trading Bias |
|-------------------|----------------|--------------|
| High storage | -$0.30 to $0.00 | Sell spread |
| Normal storage | $0.00 to +$0.50 | Neutral |
| Low storage | +$0.50 to +$2.00 | Buy spread |
| Critical storage | +$2.00+ | Strong buy |

---

## 2. Weather-Driven Spread Strategies

### 2.1 The Prompt Month Spread

**Strategy: Buy Prompt vs. Sell Deferred during Cold Snaps**

When a significant cold event is forecast:

1. Near-term demand spikes immediately
2. Storage withdrawal accelerates
3. Prompt month rallies relative to deferred months

```python
class PromptSpreadStrategy:
    """
    Trade prompt month spread based on weather forecast
    """
    
    def __init__(self, config):
        self.hdd_threshold = config.get('hdd_threshold', 2.0)
        self.spread_threshold = config.get('spread_threshold', 0.05)
        self.max_position = config.get('max_position', 10)
        
    def generate_signal(
        self,
        hdd_forecast: float,
        hdd_normal: float,
        hdd_std: float,
        current_spread: float,
        model_agreement: float
    ) -> dict:
        """
        Generate spread trading signal
        """
        # Calculate weather surprise
        hdd_z = (hdd_forecast - hdd_normal) / hdd_std
        
        # Generate signal
        if hdd_z > self.hdd_threshold:
            direction = 'BUY_SPREAD'
            strength = min((hdd_z - self.hdd_threshold) / 2, 1.0)
        elif hdd_z < -self.hdd_threshold:
            direction = 'SELL_SPREAD'
            strength = min((-hdd_z - self.hdd_threshold) / 2, 1.0)
        else:
            direction = 'NEUTRAL'
            strength = 0.0
        
        position = int(self.max_position * strength * model_agreement)
        
        return {
            'direction': direction,
            'strength': strength,
            'position': position,
            'hdd_z_score': hdd_z,
            'model_confidence': model_agreement
        }
```

### 2.2 The Balance of Winter Spread

**Strategy: Trade the Remaining Heating Season**

$$
\text{BOW Spread} = \frac{1}{n}\sum_{i=1}^{n} F_{\text{winter}_i} - F_{\text{Apr}}
$$

**Entry Criteria:**

1. Storage trajectory indicates end-of-season tightness
2. Extended cold forecast with high model confidence
3. Spread not yet reflecting full weather impact

### 2.3 The Summer Fill Spread

**Strategy: Trade Injection Season Expectations**

$$
\text{Fill Spread} = F_{\text{Oct}} - F_{\text{Apr}}
$$

---

## 3. Spread Mechanics and Execution

### 3.1 Spread Order Types

```python
# CME spread order example
spread_order = {
    'order_type': 'SPREAD',
    'leg1': {'symbol': 'NGG26', 'side': 'BUY', 'ratio': 1},
    'leg2': {'symbol': 'NGH26', 'side': 'SELL', 'ratio': 1},
    'spread_price': -0.15,
    'quantity': 5
}
```

### 3.2 Margin Efficiency

| Position Type | Initial Margin | Margin Reduction |
|---------------|----------------|------------------|
| Outright | $4,500 | - |
| Adjacent Month Spread | $350 | 92% |
| 2-Month Spread | $500 | 89% |
| Winter-Summer Spread | $800 | 82% |

### 3.3 Spread P&L Calculation

```python
def calculate_spread_pnl(
    entry_spread: float,
    exit_spread: float,
    position: int,
    contract_size: int = 10000
) -> float:
    """Calculate P&L for a spread trade"""
    spread_change = exit_spread - entry_spread
    pnl = spread_change * contract_size * position
    return pnl
```

---

## 4. Risk Management

### 4.1 Spread-Specific Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Forecast Risk** | Weather doesn't materialize | Position sizing by confidence |
| **Liquidity Risk** | Wide bid-ask in back months | Use liquid spreads |
| **Roll Risk** | Spread changes during roll | Monitor roll dates |
| **Correlation Breakdown** | Legs move independently | Set stop-loss on spread |

### 4.2 Scenario Analysis

```python
def spread_scenario_analysis(
    current_spread: float,
    position_size: int,
    scenarios: list
) -> pd.DataFrame:
    """Analyze spread P&L under different weather scenarios"""
    results = []
    
    for scenario in scenarios:
        pnl = scenario['spread_change'] * 10000 * position_size
        expected_pnl = pnl * scenario['probability']
        
        results.append({
            'scenario': scenario['name'],
            'probability': scenario['probability'],
            'spread_change': scenario['spread_change'],
            'pnl': pnl,
            'expected_pnl': expected_pnl
        })
    
    return pd.DataFrame(results)
```

### 4.3 Stop Loss Implementation

```python
def spread_stop_loss(
    entry_spread: float,
    current_spread: float,
    position: int,
    max_loss_per_spread: float = 0.15
) -> dict:
    """Check and execute spread stop loss"""
    
    if position > 0:  # Long spread
        stop_level = entry_spread - max_loss_per_spread
        triggered = current_spread < stop_level
    else:  # Short spread
        stop_level = entry_spread + max_loss_per_spread
        triggered = current_spread > stop_level
    
    return {
        'stop_level': stop_level,
        'current_spread': current_spread,
        'triggered': triggered,
        'action': 'CLOSE_POSITION' if triggered else 'HOLD'
    }
```

---

## 5. Backtesting Framework

### 5.1 Historical Analysis

```python
class SpreadBacktester:
    """Backtest spread strategies on historical data"""
    
    def __init__(self, price_data: pd.DataFrame, weather_data: pd.DataFrame):
        self.prices = price_data
        self.weather = weather_data
        self.trades = []
        
    def run_backtest(self, strategy, start_date: str, end_date: str) -> dict:
        """Run backtest over specified period"""
        
        results = {
            'total_trades': 0,
            'winning_trades': 0,
            'total_pnl': 0,
            'max_drawdown': 0,
            'sharpe_ratio': 0
        }
        
        # Implementation details...
        return results
```

---

## 6. Summary

Seasonal spread strategies offer compelling risk-adjusted returns:

1. **Lower margin** requirements than outright positions
2. **Weather edge** translates directly to spread moves
3. **Defined risk** through spread stop losses
4. **Portfolio benefits** from low correlation to other assets

The key is matching spread tenor to forecast confidence and managing position size dynamically.

---

## References

1. Geman, H. (2005). *Commodities and Commodity Derivatives*. Wiley.
2. Eydeland, A., & Wolyniec, K. (2003). *Energy and Power Risk Management*. Wiley.
3. Pilipovic, D. (2007). *Energy Risk: Valuing and Managing Energy Derivatives*. McGraw-Hill.
