# Risk Management for Commodity Weather Trading

## Learning Objectives

By the end of this section, you will be able to:

- Identify and quantify risks specific to weather-based commodity trading
- Implement position sizing frameworks that account for forecast uncertainty
- Build scenario-based stress testing for extreme weather events
- Design portfolio-level risk controls for weather strategies

---

## 1. Risk Taxonomy

### 1.1 Weather-Specific Risks

| Risk Category | Description | Mitigation |
|---------------|-------------|------------|
| **Forecast Risk** | Weather doesn't materialize as predicted | Scale position to confidence |
| **Timing Risk** | Event occurs earlier/later than forecast | Use spreads, staggered entries |
| **Magnitude Risk** | Severity differs from forecast | Scenario analysis, stress testing |
| **Model Risk** | Weather models systematically biased | Multi-model validation |
| **Data Risk** | Delayed or incorrect data feeds | Redundant data sources |

### 1.2 Market-Specific Risks

| Risk Category | Description | Mitigation |
|---------------|-------------|------------|
| **Liquidity Risk** | Wide spreads during volatility | Pre-position, use limits |
| **Gap Risk** | Price gaps on weather news | Smaller overnight positions |
| **Correlation Risk** | Unexpected cross-asset moves | Diversification |
| **Crowding Risk** | Too many similar positions | Monitor COT data |

### 1.3 The Three Critical Pitfalls of Weather Trading

Weather-based trading has unique traps that catch many traders. Understanding these is essential:

#### Pitfall 1: Forecast Uncertainty Beyond 7 Days

Weather forecast accuracy degrades rapidly with time:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FORECAST ACCURACY DECAY                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  100% ─┬─────●                                                              │
│        │      ╲                                                             │
│   90% ─┤       ●                                                            │
│        │        ╲                                                           │
│   80% ─┤         ●                                                          │
│        │          ╲                                                         │
│   70% ─┤           ●                                                        │
│        │            ╲                                                       │
│   60% ─┤             ●─────── Usable for trading                            │
│        │              ╲                                                     │
│   50% ─┤               ●─────────── Marginal                                │
│        │                ╲                                                   │
│   40% ─┤                 ●──────────────── Trend only                       │
│        │                  ╲                                                 │
│   30% ─┤                   ●───────────────────── Noise                     │
│        │                                                                    │
│        └────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────              │
│           Day1  2    3    4    5    6    7    8    9   10   14              │
│                                                                             │
│  ═══════════════════════════════════════════════════════════                │
│  Rule: Position size should decay with forecast lead time                   │
│        Day 1-3: 100% size | Day 4-6: 50% | Day 7+: 25% or less             │
│  ═══════════════════════════════════════════════════════════                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Statistics:**

| Lead Time | Temperature RMSE | Probability of Major Miss | Position Scale |
|-----------|-----------------|---------------------------|----------------|
| Day 1-3 | 2-3°F | <5% | 100% |
| Day 4-5 | 4-5°F | 10-15% | 75% |
| Day 6-7 | 5-7°F | 20-30% | 50% |
| Day 8-10 | 7-10°F | 40-50% | 25% |
| Day 11-14 | 10-15°F | 60%+ | 10% or none |

!!! danger "The 7-Day Cliff"
    Forecast accuracy drops **sharply** after day 7. Trading based on 10+ day forecasts is essentially gambling. Many traders lose money by entering positions too early based on extended forecasts that subsequently change.

#### Pitfall 2: "Buy the Rumor, Sell the Fact"

Weather events often follow a predictable pattern where prices move **before** the event, not during:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  "BUY THE RUMOR, SELL THE FACT"                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Price                           ┌───────┐                                  │
│    │                            ╱│ PEAK  │                                  │
│    │                         ╱╱  │(Event │                                  │
│    │                      ╱╱     │Arrives)                                  │
│    │                   ╱╱        └───┬───┘                                  │
│    │               ╱╱╱               │                                      │
│    │           ╱╱╱                   │╲                                     │
│    │       ╱╱╱   ← "Buy the Rumor"  │ ╲  ← "Sell the Fact"                 │
│    │    ╱╱╱                          │  ╲                                   │
│    │ ╱╱╱                             │   ╲                                  │
│    │╱                                │    ╲───────                          │
│    └─────────────────────────────────┴────────────────────                  │
│         Forecast     Media    Cold    Cold                                  │
│         Released   Coverage  Arrives  Peaks                                 │
│                                                                             │
│    Day:   -7        -3 to -1    0      +2                                   │
│                                                                             │
│  ═══════════════════════════════════════════════════════════                │
│  When the cold snap actually arrives, the trade is OVER.                    │
│  Smart money entered days earlier on the forecast.                          │
│  If you're buying when it's cold outside, you're too late.                  │
│  ═══════════════════════════════════════════════════════════                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Typical Price Discovery Timeline:**

| Stage | Timing | % of Move Complete | Action |
|-------|--------|-------------------|--------|
| Forecast release | Day -7 to -5 | 0-20% | **ENTER** |
| Model convergence | Day -5 to -3 | 20-50% | **ADD** |
| Media coverage | Day -3 to -1 | 50-80% | **HOLD / PARTIAL EXIT** |
| Event arrives | Day 0 | 80-95% | **EXIT** |
| Event peaks | Day +1 to +3 | 95-100% | **TOO LATE** |

!!! warning "The Late Entry Trap"
    If you hear about a "polar vortex" on the evening news, you are **at least 3 days late**. Professional traders positioned based on weather models days earlier. Entering at this point often means buying the top.

#### Pitfall 3: Black Swan Events (The 2021 Texas Freeze)

Some weather events exceed all forecasts and models. The February 2021 Texas Freeze is the canonical example:

**What Models Predicted vs. Reality:**

| Metric | Forecast (Day -7) | Forecast (Day -3) | Actual |
|--------|-------------------|-------------------|--------|
| Min Temperature (Dallas) | 15°F | 5°F | **-2°F** |
| Duration of <20°F | 2 days | 4 days | **7 days** |
| Grid Impact | Minor | Moderate | **Catastrophic** |
| Natural Gas Spot Price | $3 → $6 | $6 → $10 | **$3 → $400+** |

```python
def black_swan_risk_assessment(
    forecast_severity: float,
    infrastructure_vulnerability: float,
    historical_analog_severity: float
) -> dict:
    """
    Assess black swan risk for extreme weather events
    
    Parameters:
    -----------
    forecast_severity : float
        Forecasted severity on 1-10 scale
    infrastructure_vulnerability : float
        Regional infrastructure vulnerability (0-1)
        ERCOT (Texas) = 0.9, PJM = 0.3, etc.
    historical_analog_severity : float
        Severity of similar historical events
    
    Returns:
    --------
    assessment : dict
        Black swan risk assessment
    """
    # Black swan multiplier: actual can be 2-10x forecast
    potential_multiplier = 1 + infrastructure_vulnerability * 3
    
    # Worst case estimate
    worst_case_severity = forecast_severity * potential_multiplier
    
    # Compare to historical analogs
    if worst_case_severity > historical_analog_severity * 1.5:
        black_swan_risk = 'HIGH'
        position_cap = 0.25  # Max 25% of normal position
    elif worst_case_severity > historical_analog_severity:
        black_swan_risk = 'MODERATE'
        position_cap = 0.50
    else:
        black_swan_risk = 'LOW'
        position_cap = 1.00
    
    return {
        'black_swan_risk': black_swan_risk,
        'potential_multiplier': potential_multiplier,
        'worst_case_severity': worst_case_severity,
        'position_cap': position_cap,
        'warning': "Consider tail hedges" if black_swan_risk == 'HIGH' else None
    }

# Example: Texas-like event assessment
# result = black_swan_risk_assessment(
#     forecast_severity=7,
#     infrastructure_vulnerability=0.9,  # ERCOT
#     historical_analog_severity=5
# )
# Output: HIGH black swan risk, cap position at 25%
```

**Lessons from 2021 Texas:**

1. **Infrastructure matters**: Weatherization failures amplified the crisis 10x
2. **Spot vs. Futures divergence**: Spot hit $400/MMBtu while futures peaked at $15
3. **Liquidity vanished**: Bid-ask spreads exploded, execution became impossible
4. **Models failed**: All weather models underestimated duration and severity

!!! danger "Black Swan Protection Rules"
    1. **Never bet the farm**: Max position size = 2% of capital, even on "sure things"
    2. **Use options for tail hedges**: Buy OTM calls if short, puts if long
    3. **Monitor infrastructure**: Know ERCOT, PJM, MISO grid status
    4. **Have exit liquidity**: Don't trade sizes you can't exit in a crisis

---

## 2. Position Sizing Framework

### 2.1 Volatility-Adjusted Sizing

```python
import numpy as np

def volatility_adjusted_position(
    account_value: float,
    risk_per_trade: float,
    current_volatility: float,
    normal_volatility: float,
    contract_value: float
) -> int:
    """
    Calculate position size adjusted for current volatility
    
    Parameters:
    -----------
    account_value : float
        Total account value
    risk_per_trade : float
        Target risk as fraction of account (e.g., 0.02)
    current_volatility : float
        Current annualized volatility
    normal_volatility : float
        Long-term average volatility
    contract_value : float
        Notional value per contract
    
    Returns:
    --------
    contracts : int
        Number of contracts to trade
    """
    # Risk budget
    risk_budget = account_value * risk_per_trade
    
    # Volatility adjustment factor
    vol_ratio = normal_volatility / current_volatility
    adjusted_risk = risk_budget * vol_ratio
    
    # Daily VaR per contract (assuming ~250 trading days)
    daily_vol = current_volatility / np.sqrt(252)
    contract_var = contract_value * daily_vol * 2  # ~95% VaR
    
    # Position size
    contracts = int(adjusted_risk / contract_var)
    
    return max(1, contracts)

# Example: Natural gas during normal vs. extreme volatility
# Normal vol: 60%, Current vol: 120% (during polar vortex)
# Position would be halved due to elevated volatility
```

### 2.2 Confidence-Weighted Sizing

```python
def confidence_weighted_position(
    base_position: int,
    model_agreement: float,
    forecast_lead_time: int,
    storage_buffer: float
) -> int:
    """
    Adjust position based on forecast confidence factors
    
    Parameters:
    -----------
    base_position : int
        Maximum position size
    model_agreement : float
        Weather model agreement score [0, 1]
    forecast_lead_time : int
        Days until weather event
    storage_buffer : float
        Storage vs. 5-year average (%)
    
    Returns:
    --------
    adjusted_position : int
        Confidence-adjusted position size
    """
    # Lead time decay (exponential)
    lead_time_factor = np.exp(-forecast_lead_time / 7)
    
    # Storage factor (low storage = higher conviction for cold trades)
    if storage_buffer < -10:  # Below average
        storage_factor = 1.2
    elif storage_buffer > 10:  # Above average
        storage_factor = 0.8
    else:
        storage_factor = 1.0
    
    # Combined factor
    combined_factor = model_agreement * lead_time_factor * storage_factor
    
    adjusted_position = int(base_position * combined_factor)
    
    return max(1, min(adjusted_position, base_position))
```

---

## 3. Stop Loss Strategies

### 3.1 Weather-Aware Stop Losses

```python
class WeatherAwareStopLoss:
    """Dynamic stop loss that adjusts based on weather forecast changes"""
    
    def __init__(self, config: dict):
        self.base_stop_pct = config.get('base_stop_pct', 0.05)
        self.max_stop_pct = config.get('max_stop_pct', 0.10)
        self.min_stop_pct = config.get('min_stop_pct', 0.03)
        
    def calculate_stop(
        self,
        entry_price: float,
        position_direction: str,
        forecast_confidence: float,
        current_atr: float
    ) -> float:
        """
        Calculate dynamic stop loss level
        
        Parameters:
        -----------
        entry_price : float
            Trade entry price
        position_direction : str
            'LONG' or 'SHORT'
        forecast_confidence : float
            Current forecast confidence [0, 1]
        current_atr : float
            Current Average True Range
        
        Returns:
        --------
        stop_price : float
            Stop loss price level
        """
        # Adjust stop based on confidence
        # Higher confidence = tighter stop (more conviction)
        # Lower confidence = wider stop (more uncertainty)
        confidence_factor = 2 - forecast_confidence  # 1.0 to 2.0
        
        stop_distance = current_atr * 2 * confidence_factor
        
        # Clamp to min/max
        stop_pct = np.clip(
            stop_distance / entry_price,
            self.min_stop_pct,
            self.max_stop_pct
        )
        
        if position_direction == 'LONG':
            stop_price = entry_price * (1 - stop_pct)
        else:
            stop_price = entry_price * (1 + stop_pct)
        
        return stop_price
    
    def update_stop_on_forecast_change(
        self,
        current_stop: float,
        entry_price: float,
        position_direction: str,
        new_forecast_confidence: float,
        old_forecast_confidence: float
    ) -> float:
        """
        Update stop loss when forecast confidence changes
        """
        # If confidence drops significantly, tighten stop to lock in profits
        confidence_drop = old_forecast_confidence - new_forecast_confidence
        
        if confidence_drop > 0.2:  # Significant confidence drop
            # Move stop closer by 50% of drop
            adjustment = confidence_drop * 0.5
            
            if position_direction == 'LONG':
                # Can only tighten (raise) stop for longs
                new_stop = current_stop * (1 + adjustment)
                return max(new_stop, current_stop)
            else:
                # Can only tighten (lower) stop for shorts
                new_stop = current_stop * (1 - adjustment)
                return min(new_stop, current_stop)
        
        return current_stop
```

### 3.2 Time-Based Exit Rules

```python
def time_based_exit(
    entry_date: datetime,
    event_date: datetime,
    current_date: datetime,
    pnl_pct: float
) -> dict:
    """
    Determine time-based exit rules
    
    Returns:
    --------
    exit_rule : dict
        Exit recommendation based on time
    """
    days_since_entry = (current_date - entry_date).days
    days_to_event = (event_date - current_date).days
    
    # Rule 1: Exit before event if profitable
    if days_to_event <= 1 and pnl_pct > 0.03:
        return {
            'action': 'EXIT',
            'reason': 'Pre-event profit taking',
            'exit_pct': 0.75
        }
    
    # Rule 2: Exit after event passes
    if days_to_event < 0:
        return {
            'action': 'EXIT',
            'reason': 'Event has passed',
            'exit_pct': 1.0
        }
    
    # Rule 3: Maximum holding period
    if days_since_entry > 14:
        return {
            'action': 'EXIT',
            'reason': 'Max holding period',
            'exit_pct': 1.0
        }
    
    return {
        'action': 'HOLD',
        'reason': 'Within normal parameters',
        'exit_pct': 0.0
    }
```

---

## 4. Scenario Analysis and Stress Testing

### 4.1 Weather Scenario Generator

```python
class WeatherScenarioGenerator:
    """Generate scenarios for stress testing"""
    
    def __init__(self, historical_data: pd.DataFrame):
        self.historical = historical_data
        
    def generate_scenarios(self, n_scenarios: int = 1000) -> list:
        """
        Generate Monte Carlo scenarios based on historical patterns
        
        Returns:
        --------
        scenarios : list
            List of scenario dictionaries
        """
        scenarios = []
        
        # Historical distribution parameters
        hdd_mean = self.historical['hdd'].mean()
        hdd_std = self.historical['hdd'].std()
        
        for i in range(n_scenarios):
            # Sample from historical distribution with fat tails
            hdd_shock = np.random.standard_t(df=5) * hdd_std
            
            scenario = {
                'scenario_id': i,
                'hdd_deviation': hdd_shock,
                'hdd_level': hdd_mean + hdd_shock,
                'severity': abs(hdd_shock) / hdd_std,
                'type': 'COLD' if hdd_shock > 0 else 'WARM'
            }
            
            scenarios.append(scenario)
        
        return scenarios
    
    def add_historical_extremes(self, scenarios: list) -> list:
        """Add actual historical extreme events to scenarios"""
        
        extreme_events = [
            {'name': 'Feb 2021 Texas Freeze', 'hdd_deviation': 4.5, 'price_impact': 4.0},
            {'name': 'Jan 2014 Polar Vortex', 'hdd_deviation': 3.8, 'price_impact': 0.8},
            {'name': 'Jan 2018 Bomb Cyclone', 'hdd_deviation': 2.5, 'price_impact': 0.3},
            {'name': 'Jan 2026 Polar Express', 'hdd_deviation': 4.0, 'price_impact': 0.7}
        ]
        
        for event in extreme_events:
            scenarios.append({
                'scenario_id': f"HIST_{event['name']}",
                'hdd_deviation': event['hdd_deviation'] * self.historical['hdd'].std(),
                'historical_price_impact': event['price_impact'],
                'type': 'HISTORICAL_EXTREME'
            })
        
        return scenarios
```

### 4.2 Portfolio Stress Test

```python
def portfolio_stress_test(
    positions: list,
    scenarios: list,
    price_models: dict
) -> pd.DataFrame:
    """
    Stress test portfolio across weather scenarios
    
    Parameters:
    -----------
    positions : list
        Current positions with details
    scenarios : list
        Weather scenarios to test
    price_models : dict
        Price response models by commodity
    
    Returns:
    --------
    results : DataFrame
        Stress test results
    """
    results = []
    
    for scenario in scenarios:
        scenario_pnl = 0
        position_details = []
        
        for position in positions:
            commodity = position['commodity']
            quantity = position['quantity']
            direction = position['direction']
            
            # Get price impact from model
            price_model = price_models.get(commodity)
            if price_model:
                price_change = price_model.predict_impact(scenario)
                
                # Calculate P&L
                if direction == 'LONG':
                    pnl = quantity * price_change * position['contract_value']
                else:
                    pnl = -quantity * price_change * position['contract_value']
                
                scenario_pnl += pnl
                position_details.append({
                    'commodity': commodity,
                    'pnl': pnl
                })
        
        results.append({
            'scenario_id': scenario['scenario_id'],
            'scenario_type': scenario.get('type', 'MONTE_CARLO'),
            'hdd_deviation': scenario['hdd_deviation'],
            'total_pnl': scenario_pnl,
            'position_details': position_details
        })
    
    return pd.DataFrame(results)
```

---

## 5. Portfolio-Level Risk Controls

### 5.1 Correlation Management

```python
def calculate_weather_portfolio_risk(
    positions: dict,
    correlation_matrix: pd.DataFrame,
    volatilities: dict
) -> dict:
    """
    Calculate portfolio risk accounting for weather correlations
    
    Parameters:
    -----------
    positions : dict
        Positions by commodity {'NG': 5, 'HO': 3, ...}
    correlation_matrix : DataFrame
        Correlation matrix between commodities
    volatilities : dict
        Annualized volatilities by commodity
    
    Returns:
    --------
    risk_metrics : dict
        Portfolio risk metrics
    """
    commodities = list(positions.keys())
    n = len(commodities)
    
    # Position vector
    pos_vector = np.array([positions[c] for c in commodities])
    
    # Volatility vector
    vol_vector = np.array([volatilities[c] for c in commodities])
    
    # Covariance matrix
    corr_matrix = correlation_matrix.loc[commodities, commodities].values
    cov_matrix = np.outer(vol_vector, vol_vector) * corr_matrix
    
    # Portfolio variance
    portfolio_var = pos_vector @ cov_matrix @ pos_vector
    portfolio_vol = np.sqrt(portfolio_var)
    
    # Marginal risk contributions
    marginal_risk = cov_matrix @ pos_vector / portfolio_vol
    risk_contributions = pos_vector * marginal_risk
    
    return {
        'portfolio_volatility': portfolio_vol,
        'portfolio_var_95': portfolio_vol * 1.65,
        'risk_contributions': dict(zip(commodities, risk_contributions)),
        'concentration_ratio': max(risk_contributions) / sum(risk_contributions)
    }
```

### 5.2 Dynamic Risk Limits

```python
class DynamicRiskLimits:
    """Adjust risk limits based on market conditions"""
    
    def __init__(self, base_limits: dict):
        self.base_limits = base_limits
        
    def get_current_limits(
        self,
        current_vix: float,
        normal_vix: float,
        weather_uncertainty: float
    ) -> dict:
        """
        Calculate current risk limits based on conditions
        
        Parameters:
        -----------
        current_vix : float
            Current VIX level
        normal_vix : float
            Normal VIX level (~18)
        weather_uncertainty : float
            Forecast uncertainty score [0, 1]
        
        Returns:
        --------
        limits : dict
            Adjusted risk limits
        """
        # VIX adjustment (reduce limits when VIX elevated)
        vix_ratio = normal_vix / max(current_vix, 10)
        vix_factor = np.clip(vix_ratio, 0.5, 1.5)
        
        # Weather uncertainty adjustment
        weather_factor = 1 - weather_uncertainty * 0.3
        
        # Combined adjustment
        adjustment = vix_factor * weather_factor
        
        adjusted_limits = {}
        for key, base_value in self.base_limits.items():
            adjusted_limits[key] = base_value * adjustment
        
        return adjusted_limits
```

---

## 6. Operational Risk Controls

### 6.1 Pre-Trade Checks

```python
def pre_trade_risk_check(
    proposed_trade: dict,
    current_portfolio: dict,
    risk_limits: dict,
    market_conditions: dict
) -> dict:
    """
    Comprehensive pre-trade risk check
    
    Returns:
    --------
    approval : dict
        Trade approval status and any concerns
    """
    concerns = []
    
    # Check 1: Position limits
    new_position = current_portfolio.get(proposed_trade['commodity'], 0) + \
                   proposed_trade['quantity'] * (1 if proposed_trade['direction'] == 'LONG' else -1)
    
    if abs(new_position) > risk_limits['max_position']:
        concerns.append(f"Position limit exceeded: {new_position} > {risk_limits['max_position']}")
    
    # Check 2: Portfolio concentration
    total_exposure = sum(abs(v) for v in current_portfolio.values()) + abs(proposed_trade['quantity'])
    commodity_pct = abs(new_position) / total_exposure
    
    if commodity_pct > risk_limits['max_concentration']:
        concerns.append(f"Concentration limit: {commodity_pct:.1%} > {risk_limits['max_concentration']:.1%}")
    
    # Check 3: Liquidity check
    if market_conditions['bid_ask_spread'] > risk_limits['max_spread']:
        concerns.append(f"Wide spread: {market_conditions['bid_ask_spread']}")
    
    # Check 4: Volatility check
    if market_conditions['current_vol'] > risk_limits['max_vol_for_new_trades']:
        concerns.append(f"High volatility: {market_conditions['current_vol']:.1%}")
    
    return {
        'approved': len(concerns) == 0,
        'concerns': concerns,
        'proposed_trade': proposed_trade
    }
```

### 6.2 Daily Risk Report

```python
def generate_daily_risk_report(
    portfolio: dict,
    market_data: dict,
    weather_data: dict,
    limits: dict
) -> dict:
    """
    Generate comprehensive daily risk report
    
    Returns:
    --------
    report : dict
        Daily risk report
    """
    report = {
        'report_date': datetime.now().strftime('%Y-%m-%d'),
        'portfolio_summary': {},
        'risk_metrics': {},
        'limit_utilization': {},
        'weather_outlook': {},
        'alerts': []
    }
    
    # Portfolio summary
    report['portfolio_summary'] = {
        'total_positions': len(portfolio),
        'gross_exposure': sum(abs(v) for v in portfolio.values()),
        'net_exposure': sum(portfolio.values())
    }
    
    # Risk metrics (simplified)
    report['risk_metrics'] = {
        'portfolio_var_1d_95': calculate_var(portfolio, market_data),
        'max_drawdown_30d': calculate_max_dd(portfolio),
        'sharpe_ratio_30d': calculate_sharpe(portfolio)
    }
    
    # Limit utilization
    for limit_name, limit_value in limits.items():
        current_usage = get_limit_usage(limit_name, portfolio, market_data)
        utilization = current_usage / limit_value
        report['limit_utilization'][limit_name] = {
            'current': current_usage,
            'limit': limit_value,
            'utilization': utilization
        }
        
        if utilization > 0.8:
            report['alerts'].append(f"Limit warning: {limit_name} at {utilization:.1%}")
    
    # Weather outlook
    report['weather_outlook'] = {
        'next_7d_hdd_forecast': weather_data['hdd_forecast_7d'],
        'hdd_vs_normal': weather_data['hdd_anomaly'],
        'model_agreement': weather_data['model_agreement'],
        'key_events': weather_data.get('upcoming_events', [])
    }
    
    return report
```

---

## 7. Summary

Effective risk management for weather-based commodity trading requires:

1. **Multi-factor position sizing** that accounts for volatility, confidence, and storage
2. **Dynamic stop losses** that adjust to forecast confidence changes
3. **Comprehensive scenario analysis** including historical extremes
4. **Portfolio-level controls** for correlation and concentration
5. **Operational safeguards** with pre-trade checks and daily monitoring

The goal is to capture weather-driven opportunities while protecting against the inherent uncertainty in forecasting.

---

## References

1. Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk*. McGraw-Hill.
2. Taleb, N.N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House.
3. Geman, H. (2005). *Commodities and Commodity Derivatives*. Wiley.
