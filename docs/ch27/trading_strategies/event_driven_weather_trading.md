# Event-Driven Weather Trading

## Learning Objectives

By the end of this section, you will be able to:

- Identify and categorize tradeable weather events
- Build systematic event detection and trading frameworks
- Execute trades around EIA storage reports
- Manage event risk through position sizing and timing

---

## 1. Weather Event Taxonomy

### 1.1 Event Categories

| Category | Lead Time | Duration | Price Impact | Examples |
|----------|-----------|----------|--------------|----------|
| **Acute Cold** | 3-7 days | 3-10 days | +20-100% | Polar vortex, Arctic blast |
| **Acute Heat** | 3-7 days | 3-14 days | +10-30% | Heat dome, heat wave |
| **Tropical** | 5-14 days | 3-7 days | +10-50% | Hurricanes, tropical storms |
| **Seasonal Shift** | 14-30 days | Seasonal | +/-10-20% | Early winter, late spring |
| **Drought** | 30+ days | Months | Varies | Agricultural impacts |

### 1.2 The January 2026 "Polar Express" as Case Study

From [Mer's Blog analysis (메르의 블로그)](https://blog.naver.com/ranto28/224159783476):

```
Timeline:
Jan 22: Jet stream weakening detected
Jan 24: Arctic air mass begins southward migration  
Jan 26: Near-continental coverage, prices +70% in 5 days

Key Characteristics:
- Geographic extent: ~90% of continental US
- Temperature anomaly: 20-40°F below normal
- Duration: 5+ days
- Comparison: 1950 + 1996 + 2021 combined severity
```

---

## 2. Event Detection Framework

### 2.1 Automated Monitoring System

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import numpy as np

@dataclass
class WeatherEvent:
    """Structured weather event for trading"""
    event_type: str
    detection_date: datetime
    expected_start: datetime
    expected_end: datetime
    severity: float  # 0-1 scale
    confidence: float  # 0-1 scale
    geographic_extent: str
    affected_regions: list
    price_impact_estimate: float

class WeatherEventDetector:
    """Detect and classify tradeable weather events"""
    
    def __init__(self, config: dict):
        self.cold_threshold = config.get('cold_threshold', -2.0)  # z-score
        self.heat_threshold = config.get('heat_threshold', 2.0)
        self.duration_threshold = config.get('duration_days', 3)
        self.coverage_threshold = config.get('coverage_pct', 0.5)
        
    def detect_cold_event(
        self,
        temp_forecast: np.ndarray,
        temp_normal: np.ndarray,
        temp_std: np.ndarray,
        geographic_weights: np.ndarray
    ) -> Optional[WeatherEvent]:
        """
        Detect significant cold weather events
        
        Parameters:
        -----------
        temp_forecast : array
            Forecasted temperatures by region and day
        temp_normal : array
            Climatological normal temperatures
        temp_std : array
            Historical standard deviation
        geographic_weights : array
            Population/demand weights by region
        
        Returns:
        --------
        event : WeatherEvent or None
        """
        # Calculate z-scores
        z_scores = (temp_forecast - temp_normal) / temp_std
        
        # Weighted average z-score
        weighted_z = np.average(z_scores, weights=geographic_weights, axis=1)
        
        # Find consecutive days below threshold
        cold_days = weighted_z < self.cold_threshold
        
        if self._count_consecutive(cold_days) >= self.duration_threshold:
            # Calculate event characteristics
            start_idx = np.argmax(cold_days)
            severity = abs(np.min(weighted_z))
            coverage = np.mean(z_scores < self.cold_threshold)
            
            return WeatherEvent(
                event_type='COLD_OUTBREAK',
                detection_date=datetime.now(),
                expected_start=datetime.now() + timedelta(days=start_idx),
                expected_end=datetime.now() + timedelta(days=start_idx + self._count_consecutive(cold_days[start_idx:])),
                severity=min(severity / 4, 1.0),
                confidence=self._calculate_confidence(z_scores),
                geographic_extent='CONTINENTAL' if coverage > 0.7 else 'REGIONAL',
                affected_regions=self._identify_regions(z_scores),
                price_impact_estimate=self._estimate_price_impact(severity, coverage)
            )
        
        return None
    
    def _count_consecutive(self, bool_array: np.ndarray) -> int:
        """Count maximum consecutive True values"""
        max_count = 0
        current_count = 0
        for val in bool_array:
            if val:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count
    
    def _calculate_confidence(self, z_scores: np.ndarray) -> float:
        """Calculate forecast confidence based on ensemble spread"""
        # Placeholder - in practice, use ensemble spread
        return 0.7
    
    def _identify_regions(self, z_scores: np.ndarray) -> list:
        """Identify affected regions"""
        # Placeholder
        return ['EAST', 'MIDWEST', 'SOUTH']
    
    def _estimate_price_impact(self, severity: float, coverage: float) -> float:
        """Estimate potential price impact"""
        base_impact = 0.10  # 10% base
        return base_impact * severity * (1 + coverage)
```

### 2.2 Multi-Source Validation

```python
def validate_event_across_sources(
    gfs_forecast: dict,
    ecmwf_forecast: dict,
    private_forecasts: list
) -> dict:
    """
    Cross-validate weather event detection across multiple sources
    
    Returns:
    --------
    validation : dict
        Validation results with confidence score
    """
    # Extract key metrics from each source
    sources = [gfs_forecast, ecmwf_forecast] + private_forecasts
    
    temp_forecasts = [s['min_temp'] for s in sources]
    duration_forecasts = [s['cold_duration'] for s in sources]
    
    # Calculate agreement metrics
    temp_spread = max(temp_forecasts) - min(temp_forecasts)
    temp_mean = np.mean(temp_forecasts)
    duration_mean = np.mean(duration_forecasts)
    
    # Confidence based on agreement
    if temp_spread < 5:  # Models agree within 5°F
        confidence = 0.9
    elif temp_spread < 10:
        confidence = 0.7
    elif temp_spread < 15:
        confidence = 0.5
    else:
        confidence = 0.3
    
    return {
        'consensus_temp': temp_mean,
        'consensus_duration': duration_mean,
        'model_spread': temp_spread,
        'confidence': confidence,
        'agreement_level': 'HIGH' if confidence > 0.7 else 'MEDIUM' if confidence > 0.5 else 'LOW'
    }
```

---

## 3. Trading the EIA Storage Report

### 3.1 Report Trading Framework

The EIA Weekly Natural Gas Storage Report is the single most important scheduled event:

```
Thursday 10:30 AM ET

Pre-Report (T-24h to T-0):
├── Gather analyst estimates
├── Calculate our model estimate
├── Identify consensus divergence
└── Set entry orders

Report Release (T+0):
├── Compare actual vs consensus
├── Execute directional trade if surprise
└── Manage position through volatility

Post-Report (T+0 to T+4h):
├── Assess price response
├── Compare to weather forecasts
└── Adjust position or take profits
```

### 3.2 Storage Surprise Trading

```python
class EIAReportTrader:
    """Trade around EIA storage report releases"""
    
    def __init__(self, config: dict):
        self.surprise_threshold = config.get('surprise_threshold', 5)  # Bcf
        self.max_position = config.get('max_position', 10)
        self.price_impact_per_bcf = config.get('impact_per_bcf', 0.003)
        
    def pre_report_analysis(
        self,
        our_estimate: float,
        consensus_estimate: float,
        weather_data: dict,
        current_price: float
    ) -> dict:
        """
        Analyze positioning opportunity before report
        
        Parameters:
        -----------
        our_estimate : float
            Our model's storage change estimate (Bcf)
        consensus_estimate : float
            Market consensus estimate (Bcf)
        weather_data : dict
            Recent and forecast weather data
        current_price : float
            Current NG price
        
        Returns:
        --------
        analysis : dict
            Pre-report analysis and recommendation
        """
        divergence = our_estimate - consensus_estimate
        
        # Estimate expected price move if we're right
        expected_move = -divergence * self.price_impact_per_bcf
        
        # Risk assessment
        risk_reward = abs(expected_move) / (self.price_impact_per_bcf * 10)
        
        # Generate recommendation
        if abs(divergence) > self.surprise_threshold and risk_reward > 1.5:
            if divergence < 0:  # We expect larger draw than consensus
                direction = 'LONG'
            else:  # We expect smaller draw than consensus
                direction = 'SHORT'
                
            position_size = min(
                int(abs(divergence) / self.surprise_threshold * 5),
                self.max_position
            )
        else:
            direction = 'FLAT'
            position_size = 0
        
        return {
            'our_estimate': our_estimate,
            'consensus': consensus_estimate,
            'divergence': divergence,
            'expected_move': expected_move,
            'direction': direction,
            'position_size': position_size,
            'risk_reward': risk_reward
        }
    
    def post_report_response(
        self,
        actual: float,
        consensus: float,
        price_reaction: float
    ) -> dict:
        """
        Analyze and respond to actual report
        
        Parameters:
        -----------
        actual : float
            Actual storage change
        consensus : float
            Pre-report consensus
        price_reaction : float
            Price change since report
        
        Returns:
        --------
        response : dict
            Trading response recommendation
        """
        surprise = actual - consensus
        expected_reaction = -surprise * self.price_impact_per_bcf
        
        # Check if market reacted as expected
        reaction_ratio = price_reaction / expected_reaction if expected_reaction != 0 else 0
        
        if abs(reaction_ratio) < 0.5:
            # Market under-reacted - potential continuation
            action = 'ADD_TO_POSITION'
        elif abs(reaction_ratio) > 2.0:
            # Market over-reacted - potential fade
            action = 'TAKE_PROFITS'
        else:
            # Normal reaction
            action = 'HOLD'
        
        return {
            'surprise_bcf': surprise,
            'expected_reaction': expected_reaction,
            'actual_reaction': price_reaction,
            'reaction_ratio': reaction_ratio,
            'recommended_action': action
        }
```

---

## 4. Hurricane and Tropical Storm Trading

### 4.1 Gulf of Mexico Impact Assessment

```python
def assess_hurricane_impact(
    storm_track: dict,
    intensity_forecast: dict,
    production_data: dict
) -> dict:
    """
    Assess natural gas supply impact from tropical system
    
    Parameters:
    -----------
    storm_track : dict
        Forecasted storm path with uncertainty cone
    intensity_forecast : dict
        Expected intensity at key points
    production_data : dict
        Current Gulf of Mexico production by platform
    
    Returns:
    --------
    impact : dict
        Production impact assessment
    """
    # Calculate platforms in path
    platforms_at_risk = []
    total_production_risk = 0
    
    for platform in production_data['platforms']:
        distance = calculate_distance(
            platform['lat'], platform['lon'],
            storm_track['center_lat'], storm_track['center_lon']
        )
        
        # Typical evacuation within 200 miles of Cat 1+
        if distance < 200 and intensity_forecast['max_wind'] > 74:
            platforms_at_risk.append(platform)
            total_production_risk += platform['daily_production']
    
    # Estimate duration of shut-ins
    if intensity_forecast['max_wind'] > 110:  # Major hurricane
        shutin_days = 10
    elif intensity_forecast['max_wind'] > 95:
        shutin_days = 7
    else:
        shutin_days = 4
    
    # Total supply impact
    supply_impact_bcf = total_production_risk * shutin_days
    
    # Price impact estimate
    price_impact = supply_impact_bcf * 0.01  # ~1% per 10 Bcf
    
    return {
        'platforms_at_risk': len(platforms_at_risk),
        'daily_production_risk': total_production_risk,
        'estimated_shutin_days': shutin_days,
        'total_supply_impact_bcf': supply_impact_bcf,
        'estimated_price_impact': price_impact
    }
```

### 4.2 Hurricane Trading Playbook

| Storm Stage | Lead Time | Trading Action |
|-------------|-----------|----------------|
| Tropical Depression | 5-7 days | Monitor only |
| Tropical Storm (GoM bound) | 3-5 days | Small long position |
| Hurricane Warning | 1-3 days | Full position if track confirmed |
| Landfall | 0 days | Hold or take profits |
| Post-Storm | +1-7 days | Assess damage, fade if overreaction |

---

## 5. Position Sizing for Events

### 5.1 Kelly-Based Event Sizing

```python
def event_position_size(
    bankroll: float,
    win_probability: float,
    expected_win_pct: float,
    expected_loss_pct: float,
    kelly_fraction: float = 0.25  # Quarter Kelly for safety
) -> float:
    """
    Calculate position size using Kelly criterion
    
    Parameters:
    -----------
    bankroll : float
        Total trading capital
    win_probability : float
        Estimated probability of profitable trade
    expected_win_pct : float
        Expected return if trade wins
    expected_loss_pct : float
        Expected loss if trade loses
    kelly_fraction : float
        Fraction of full Kelly to use
    
    Returns:
    --------
    position_value : float
        Recommended position size in dollars
    """
    # Kelly formula: f* = (bp - q) / b
    # where b = win/loss ratio, p = win prob, q = loss prob
    
    b = expected_win_pct / expected_loss_pct
    p = win_probability
    q = 1 - p
    
    kelly = (b * p - q) / b
    
    # Apply fractional Kelly
    position_fraction = max(0, kelly * kelly_fraction)
    position_value = bankroll * position_fraction
    
    return position_value
```

### 5.2 Event Confidence Scaling

| Confidence Level | Position Scale | Use Case |
|------------------|---------------|----------|
| Very High (>80%) | 100% of max | Model convergence + historical analog |
| High (60-80%) | 75% of max | Model convergence |
| Medium (40-60%) | 50% of max | Partial agreement |
| Low (20-40%) | 25% of max | Early signal, high uncertainty |
| Very Low (<20%) | 0% | No trade |

---

## 6. Event Trade Management

### 6.1 Entry Timing

```python
def optimal_entry_timing(
    event: WeatherEvent,
    current_price: float,
    price_history: pd.Series
) -> dict:
    """
    Determine optimal entry timing for weather event trade
    
    Returns:
    --------
    timing : dict
        Entry timing recommendation
    """
    days_to_event = (event.expected_start - datetime.now()).days
    
    # Historical analysis suggests:
    # - Too early (>7 days): Forecast may change
    # - Sweet spot (3-5 days): Models converging, not fully priced
    # - Late (<3 days): Mostly priced in
    
    if days_to_event > 7:
        recommendation = 'WAIT'
        entry_size = 0.0
    elif days_to_event > 5:
        recommendation = 'SCALE_IN'
        entry_size = 0.25
    elif days_to_event > 3:
        recommendation = 'FULL_ENTRY'
        entry_size = 1.0
    else:
        recommendation = 'LATE_ENTRY_PARTIAL'
        entry_size = 0.5
    
    return {
        'days_to_event': days_to_event,
        'recommendation': recommendation,
        'entry_size_fraction': entry_size,
        'confidence': event.confidence
    }
```

### 6.2 Exit Strategy

```python
def event_exit_strategy(
    entry_price: float,
    current_price: float,
    event: WeatherEvent,
    position_size: int
) -> dict:
    """
    Determine exit strategy for event trade
    
    Returns:
    --------
    strategy : dict
        Exit recommendations
    """
    pnl_pct = (current_price - entry_price) / entry_price
    days_since_entry = (datetime.now() - event.detection_date).days
    
    # Profit taking levels
    if pnl_pct > 0.15:  # >15% profit
        action = 'TAKE_75%_PROFIT'
        exit_fraction = 0.75
    elif pnl_pct > 0.10:
        action = 'TAKE_50%_PROFIT'
        exit_fraction = 0.50
    elif pnl_pct > 0.05:
        action = 'TAKE_25%_PROFIT'
        exit_fraction = 0.25
    elif pnl_pct < -0.08:  # Stop loss
        action = 'STOP_LOSS_EXIT'
        exit_fraction = 1.0
    else:
        action = 'HOLD'
        exit_fraction = 0.0
    
    # Time-based exit: close before event passes
    if datetime.now() > event.expected_end:
        action = 'EVENT_PASSED_EXIT'
        exit_fraction = 1.0
    
    return {
        'action': action,
        'exit_fraction': exit_fraction,
        'current_pnl_pct': pnl_pct,
        'contracts_to_exit': int(position_size * exit_fraction)
    }
```

---

## 7. Summary

Event-driven weather trading requires:

1. **Systematic detection** of tradeable weather events
2. **Multi-source validation** for confidence assessment
3. **Precise timing** based on forecast evolution
4. **Dynamic position sizing** scaled to confidence
5. **Disciplined exits** with profit targets and stop losses

The edge comes from processing information faster than the market while maintaining rigorous risk management.

---

## References

1. Boudoukh, J., Richardson, M., & Whitelaw, R. (1994). "Industry Returns and the Fisher Effect." *Journal of Finance*
2. Roll, R. (1984). "Orange Juice and Weather." *American Economic Review*
3. Chincarini, L. (2011). "Natural Gas Futures and Spread Trading." *Journal of Alternative Investments*
