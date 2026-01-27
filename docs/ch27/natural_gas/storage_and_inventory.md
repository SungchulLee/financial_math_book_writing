# Natural Gas Storage and Inventory

## Learning Objectives

By the end of this section, you will be able to:

- Understand the physical and economic role of natural gas storage
- Interpret EIA storage reports and their market impact
- Analyze storage levels in the context of weather forecasts
- Build storage-based trading signals

---

## 1. The Role of Storage

### 1.1 Why Storage Matters

Natural gas storage serves as the market's **shock absorber**:

$$
\text{Balance Equation: } \text{Production} + \text{Imports} + \Delta \text{Storage} = \text{Demand} + \text{Exports}
$$

Unlike oil, natural gas cannot be economically stockpiled above ground in large quantities. Underground storage is essential for:

1. **Seasonal balancing**: Production is relatively flat; demand is highly seasonal
2. **Price stability**: Buffer against demand spikes
3. **Supply security**: Insurance against production disruptions
4. **Operational flexibility**: Daily load balancing for utilities

### 1.2 Storage Types

| Type | Capacity Share | Cycling Speed | Location |
|------|---------------|---------------|----------|
| **Depleted Fields** | 80% | Slow (seasonal) | Everywhere |
| **Aquifers** | 10% | Medium | Midwest |
| **Salt Caverns** | 10% | Fast (daily) | Gulf Coast |

Salt caverns are critical for peak-shaving during extreme weather events.

---

## 2. The Storage Cycle

### 2.1 Seasonal Pattern

```
Storage Level (Bcf)
     
4,000 ─┬────────────────────────────────────────────┬─ Maximum capacity
       │                    ╱╲                      │
3,500 ─┤               ╱╲  ╱  ╲                    ├─ Comfortable surplus
       │            ╱╲╱  ╲╱    ╲                   │
3,000 ─┤         ╱╲╱            ╲                  ├─ Normal range
       │      ╱╲╱                ╲╱╲               │
2,500 ─┤   ╱╲╱                      ╲             ├─ Normal range
       │ ╱╲                          ╲╱╲          │
2,000 ─┤╱                               ╲         ├─ Below normal
       │                                 ╲╱╲      │
1,500 ─┤                                    ╲     ├─ Critically low
       │                                     ╲    │
1,000 ─┴────────────────────────────────────────────┴─ Minimum operating
       Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
       
       ←── Withdrawal Season ──→←── Injection Season ──→
```

### 2.2 Key Dates

| Event | Typical Date | Market Significance |
|-------|--------------|---------------------|
| Injection Start | April 1 | Shift from withdrawal mode |
| Peak Storage | November 1 | Maximum pre-winter |
| Withdrawal Start | November 1 | Heating season begins |
| Minimum Storage | March 31 | End of heating season |

### 2.3 Storage Metrics

**Year-over-Year (YoY) Comparison:**

$$
\text{YoY Surplus/Deficit} = \text{Current Storage} - \text{Storage}_{t-1 \text{ year}}
$$

**vs. 5-Year Average:**

$$
\text{5-Year Deviation} = \frac{\text{Current Storage} - \text{5-Year Avg}}{\text{5-Year Avg}} \times 100\%
$$

---

## 3. EIA Weekly Storage Report

### 3.1 Report Details

| Specification | Detail |
|---------------|--------|
| **Publisher** | Energy Information Administration (EIA) |
| **Release** | Thursday 10:30 AM ET |
| **Coverage** | Lower 48 states |
| **Lag** | Data through previous Friday |
| **Regions** | East, Midwest, Mountain, Pacific, South Central |

### 3.2 Interpreting the Numbers

The report shows **net change** from the previous week:

- **Injection**: Storage increase (positive number in summer)
- **Withdrawal**: Storage decrease (negative number in winter)

**Example from January 2026:**

| Week | Storage (Bcf) | Change | vs. 5-Year Avg |
|------|--------------|--------|----------------|
| Jan 10 | 3,065 | -120 | -2.5% |
| Jan 17 | 2,945 | -150 | -4.2% |
| Jan 24 | 2,795 | -180 | -7.1% |

!!! note "The 120 Bcf Draw"
    From [Mer's Blog (메르의 블로그)](https://blog.naver.com/ranto28/224159783476): "2026년 1월 16일 기준 천연가스 총 재고량은 3,065 Bcf(10억 입방피트)인데, 최근 일주일간 120Bcf가 인출되어 재고가 줄어들었다" — a 120 Bcf weekly draw indicates significant heating demand during the "Polar Express" cold event.

### 3.3 Data Sources and Access

#### Official EIA Data (Free)

| Source | URL | Description |
|--------|-----|-------------|
| **Weekly Storage Report** | [ir.eia.gov/ngs/ngs.html](https://ir.eia.gov/ngs/ngs.html) | Official report, released Thursday 10:30 AM ET |
| **Storage Dashboard** | [eia.gov/naturalgas/storage](https://www.eia.gov/naturalgas/storage/) | Interactive visualization with historical data |
| **Historical Data (CSV)** | [eia.gov/dnav/ng/ng_stor_wkly_s1_w.htm](https://www.eia.gov/dnav/ng/ng_stor_wkly_s1_w.htm) | Downloadable time series |
| **Natural Gas Weekly Update** | [eia.gov/naturalgas/weekly](https://www.eia.gov/naturalgas/weekly/) | Market analysis and commentary |
| **Release Schedule** | [ir.eia.gov/ngs/schedule.html](https://ir.eia.gov/ngs/schedule.html) | Holiday-adjusted release dates |
| **EIA API** | [eia.gov/opendata](https://www.eia.gov/opendata/) | Programmatic access (free API key required) |

#### Python Data Access

```python
import pandas as pd
import requests

# =============================================================
# Method 1: EIA API (Recommended for automation)
# Get free API key at: https://www.eia.gov/opendata/register.php
# =============================================================

def get_ng_storage_eia_api(api_key: str, num_weeks: int = 100) -> pd.DataFrame:
    """
    Fetch natural gas storage data via EIA API v2
    
    Parameters:
    -----------
    api_key : str
        EIA API key (free registration required)
    num_weeks : int
        Number of weeks of historical data
    
    Returns:
    --------
    df : DataFrame
        Weekly storage data with columns: date, storage_bcf, change_bcf
    """
    url = "https://api.eia.gov/v2/natural-gas/stor/wkly/data/"
    
    params = {
        "api_key": api_key,
        "frequency": "weekly",
        "data[0]": "value",
        "facets[process][]": "SAY",  # Total working gas, Lower 48
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "length": num_weeks
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    df = pd.DataFrame(data['response']['data'])
    
    # Clean up
    df['date'] = pd.to_datetime(df['period'])
    df['storage_bcf'] = pd.to_numeric(df['value'])
    df = df.sort_values('date').reset_index(drop=True)
    
    # Calculate weekly change
    df['change_bcf'] = df['storage_bcf'].diff()
    
    return df[['date', 'storage_bcf', 'change_bcf']]


# =============================================================
# Method 2: Direct CSV Download (No API key needed)
# =============================================================

def get_ng_storage_csv() -> pd.DataFrame:
    """
    Download storage data directly from EIA website
    
    Returns:
    --------
    df : DataFrame
        Historical weekly storage data
    """
    # Direct link to weekly storage CSV
    url = "https://www.eia.gov/dnav/ng/hist/nw2_epg0_swo_r48_bcfw.csv"
    
    try:
        df = pd.read_csv(url, skiprows=4)
        df.columns = ['date', 'storage_bcf']
        df['date'] = pd.to_datetime(df['date'])
        df['storage_bcf'] = pd.to_numeric(df['storage_bcf'], errors='coerce')
        df = df.dropna().sort_values('date').reset_index(drop=True)
        df['change_bcf'] = df['storage_bcf'].diff()
        return df
    except Exception as e:
        print(f"Error fetching CSV: {e}")
        return pd.DataFrame()


# =============================================================
# Method 3: Regional Storage Data
# =============================================================

def get_regional_storage(api_key: str) -> pd.DataFrame:
    """
    Fetch storage data by EIA region
    
    Regions: East, Midwest, Mountain, Pacific, South Central
    """
    url = "https://api.eia.gov/v2/natural-gas/stor/wkly/data/"
    
    regions = {
        'SAE': 'East',
        'SAM': 'Midwest', 
        'SAR': 'Mountain',
        'SAP': 'Pacific',
        'SAC': 'South Central'
    }
    
    all_data = []
    
    for code, name in regions.items():
        params = {
            "api_key": api_key,
            "frequency": "weekly",
            "data[0]": "value",
            "facets[process][]": code,
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "length": 52  # One year
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        for row in data['response']['data']:
            all_data.append({
                'date': row['period'],
                'region': name,
                'storage_bcf': float(row['value'])
            })
    
    return pd.DataFrame(all_data)


# =============================================================
# Example Usage
# =============================================================

if __name__ == "__main__":
    # Replace with your API key
    API_KEY = "your_api_key_here"
    
    # Get national storage data
    storage_df = get_ng_storage_eia_api(API_KEY, num_weeks=52)
    print(f"Latest storage: {storage_df['storage_bcf'].iloc[-1]:.0f} Bcf")
    print(f"Latest change: {storage_df['change_bcf'].iloc[-1]:.0f} Bcf")
    
    # Calculate 5-year average comparison
    current_week = storage_df['date'].iloc[-1].isocalendar()[1]
    five_year_avg = storage_df[
        storage_df['date'].dt.isocalendar().week == current_week
    ]['storage_bcf'].tail(5).mean()
    
    deviation = (storage_df['storage_bcf'].iloc[-1] - five_year_avg) / five_year_avg * 100
    print(f"vs 5-Year Avg: {deviation:+.1f}%")
```

#### Alternative Data Sources

| Source | Features | Cost |
|--------|----------|------|
| **Investing.com** | Real-time updates, economic calendar | Free |
| **Bloomberg Terminal** | Professional, real-time, analytics | $$$ |
| **Refinitiv/LSEG** | Institutional data feed | $$ |
| **Quandl (Nasdaq Data Link)** | API-friendly, historical | Free/Paid |
| **OPIS** | Physical market pricing | $$ |

#### Release Schedule Notes

- **Standard Release**: Thursday 10:30 AM ET (한국 시간: 금요일 00:30 KST)
- **Holiday Weeks**: Schedule shifts - check [ir.eia.gov/ngs/schedule.html](https://ir.eia.gov/ngs/schedule.html)
- **Data Coverage**: Through previous Friday (5-day lag)

!!! tip "Real-Time Monitoring"
    Set up alerts for EIA releases using services like [Investing.com Economic Calendar](https://www.investing.com/economic-calendar/natural-gas-storage-386) or Bloomberg's notification system.

### 3.4 Consensus Estimates

Before each report, analysts provide estimates:

```python
def calculate_storage_surprise(actual, consensus, std_dev):
    """
    Calculate storage report surprise
    
    Parameters:
    -----------
    actual : float
        Actual storage change (Bcf)
    consensus : float
        Analyst consensus estimate (Bcf)
    std_dev : float
        Historical standard deviation of surprises
    
    Returns:
    --------
    surprise : float
        Standardized surprise (z-score)
    """
    surprise = (actual - consensus) / std_dev
    return surprise

# Example: Actual -150, Consensus -130, Historical StdDev 15
# surprise = (-150 - (-130)) / 15 = -1.33 (bearish for NG)
# Note: More withdrawal than expected = bullish, but here we're
# calculating the surprise, not the direction
```

---

## 4. Storage Economics

### 4.1 The Storage Arbitrage

Storage owners profit from seasonal spreads:

$$
\text{Storage Value} = P_{\text{winter}} - P_{\text{summer}} - \text{Injection Cost} - \text{Carry Cost}
$$

**Injection Cost**: ~$0.05-0.15/MMBtu
**Withdrawal Cost**: ~$0.05-0.15/MMBtu
**Carry Cost**: Interest + fixed costs

### 4.2 Full Carry vs. Convenience Yield

**Full Carry Market:**

$$
F_{t,T} = S_t \cdot e^{(r + u - y)(T-t)}
$$

where:
- $r$ = interest rate
- $u$ = storage cost
- $y$ = convenience yield

**Backwardated Market** (convenience yield > carry cost):

When storage is low, the convenience of having gas NOW exceeds storage costs, causing backwardation.

### 4.3 Storage Level and Price Volatility

| Storage Level | Price Behavior | Volatility |
|---------------|----------------|-----------|
| >10% above avg | Contango, low vol | 40-50% |
| ±10% of avg | Normal spread | 50-60% |
| 10-20% below | Slight backwardation | 60-80% |
| >20% below | Strong backwardation | 80-120% |

---

## 5. Weather-Storage-Price Dynamics

### 5.1 The Feedback Loop

```
Cold Weather Forecast
        │
        ▼
Increased Demand Expectation
        │
        ▼
Storage Withdrawal Acceleration
        │
        ▼
Storage Level Concern
        │
        ▼
Price Increase
        │
        ▼
Demand Destruction (at extreme prices)
        │
        ▼
New Equilibrium
```

### 5.2 Storage Trajectory Modeling

```python
import numpy as np
from dataclasses import dataclass

@dataclass
class StorageScenario:
    """Model storage trajectory based on weather forecasts"""
    
    current_storage: float  # Bcf
    hdd_forecast: np.ndarray  # Daily HDD forecast
    base_demand: float = 80  # Bcf/day baseline
    hdd_sensitivity: float = 3.5  # Bcf per HDD
    production: float = 105  # Bcf/day
    lng_exports: float = 14  # Bcf/day
    
    def project_storage(self, days: int = 30) -> np.ndarray:
        """
        Project storage levels based on weather forecast
        
        Returns:
        --------
        storage_path : array
            Projected daily storage levels
        """
        storage = np.zeros(days)
        storage[0] = self.current_storage
        
        for d in range(1, days):
            # Daily demand
            demand = self.base_demand + self.hdd_sensitivity * self.hdd_forecast[d]
            
            # Net balance
            net_flow = self.production - demand - self.lng_exports
            
            # Update storage
            storage[d] = storage[d-1] + net_flow
            
        return storage
    
    def end_of_season_projection(self) -> float:
        """
        Project March 31 storage level
        """
        days_remaining = 65  # Approximate days to end of March
        storage_path = self.project_storage(days_remaining)
        return storage_path[-1]

# Example usage:
# scenario = StorageScenario(
#     current_storage=2800,
#     hdd_forecast=np.full(65, 25)  # 25 HDD/day average
# )
# end_storage = scenario.end_of_season_projection()
```

### 5.3 Critical Storage Thresholds

| Threshold | Level (Bcf) | Market Impact |
|-----------|-------------|---------------|
| Critically Low | <1,000 | Supply emergency, price spike |
| Below Normal | 1,000-1,500 | Elevated prices, high vol |
| Normal Low | 1,500-2,000 | Slightly bullish bias |
| Normal Range | 2,000-3,000 | Balanced market |
| Above Normal | 3,000-3,500 | Bearish pressure |
| Near Capacity | >3,500 | Production curtailment risk |

### 5.4 Storage Report + Weather Combo Strategy

The most powerful trading setup combines **EIA storage surprises** with **weather forecast confirmation**. This combo creates high-conviction signals.

#### The Combo Matrix

| Storage Surprise | Weather Forecast | Signal | Strength |
|------------------|------------------|--------|----------|
| Larger draw than expected | Cold continuing | **STRONG BUY** | ⭐⭐⭐⭐⭐ |
| Larger draw than expected | Warming trend | Moderate buy | ⭐⭐⭐ |
| Smaller draw than expected | Cold continuing | Neutral/Mild buy | ⭐⭐ |
| Smaller draw than expected | Warming trend | **STRONG SELL** | ⭐⭐⭐⭐⭐ |
| In-line with consensus | Cold continuing | Mild buy | ⭐⭐ |
| In-line with consensus | Warming trend | Mild sell | ⭐⭐ |

#### January 2026 Example: The Perfect Combo

From [Mer's Blog](https://blog.naver.com/ranto28/224159783476):

```
EIA Report (Jan 16, 2026):
├── Actual withdrawal: -120 Bcf
├── Consensus estimate: -100 Bcf (assumed)
├── Surprise: -20 Bcf (larger than expected)
└── Storage level: 3,065 Bcf

Weather Forecast:
├── Polar Express incoming
├── Continental cold coverage
├── 20-40°F below normal
└── Duration: 5+ days

COMBO SIGNAL: STRONG BUY ⭐⭐⭐⭐⭐
Result: +70% in 5 days ($3.10 → $5.28)
```

#### Implementation Code

```python
def storage_weather_combo_signal(
    actual_withdrawal: float,
    consensus_withdrawal: float,
    current_storage: float,
    five_year_avg_storage: float,
    hdd_forecast_7d: float,
    hdd_normal_7d: float,
    model_agreement: float
) -> dict:
    """
    Generate trading signal from Storage Report + Weather combination
    
    This is the most powerful signal when both factors align.
    
    Parameters:
    -----------
    actual_withdrawal : float
        Actual storage change from EIA report (negative = withdrawal)
    consensus_withdrawal : float
        Market consensus estimate
    current_storage : float
        Current storage level (Bcf)
    five_year_avg_storage : float
        5-year average storage for this week (Bcf)
    hdd_forecast_7d : float
        7-day HDD forecast
    hdd_normal_7d : float
        Normal 7-day HDD for this period
    model_agreement : float
        Weather model agreement score [0, 1]
    
    Returns:
    --------
    signal : dict
        Combo trading signal
    """
    # Storage surprise (negative = bullish, more withdrawal than expected)
    storage_surprise = actual_withdrawal - consensus_withdrawal
    storage_surprise_bullish = storage_surprise < -5  # More than 5 Bcf surprise
    
    # Storage level vs average
    storage_vs_avg = (current_storage - five_year_avg_storage) / five_year_avg_storage * 100
    storage_tight = storage_vs_avg < -5  # More than 5% below average
    
    # Weather forecast (positive anomaly = colder than normal = bullish)
    hdd_anomaly = hdd_forecast_7d - hdd_normal_7d
    cold_forecast = hdd_anomaly > 10  # Significantly colder than normal
    
    # COMBO LOGIC
    # Best case: Larger draw + Cold continuing + Tight storage
    
    if storage_surprise < -10 and cold_forecast and storage_tight:
        signal_strength = 'VERY_STRONG_BUY'
        confidence = 0.95 * model_agreement
        stars = 5
    elif storage_surprise < -5 and cold_forecast:
        signal_strength = 'STRONG_BUY'
        confidence = 0.85 * model_agreement
        stars = 4
    elif storage_surprise < 0 and cold_forecast:
        signal_strength = 'MODERATE_BUY'
        confidence = 0.70 * model_agreement
        stars = 3
    elif storage_surprise > 10 and not cold_forecast:
        signal_strength = 'STRONG_SELL'
        confidence = 0.85 * model_agreement
        stars = 4
    elif storage_surprise > 5 and not cold_forecast:
        signal_strength = 'MODERATE_SELL'
        confidence = 0.70 * model_agreement
        stars = 3
    else:
        signal_strength = 'NEUTRAL'
        confidence = 0.50
        stars = 1
    
    return {
        'signal': signal_strength,
        'confidence': confidence,
        'stars': stars,
        'storage_surprise_bcf': storage_surprise,
        'storage_vs_avg_pct': storage_vs_avg,
        'hdd_anomaly': hdd_anomaly,
        'cold_forecast': cold_forecast,
        'combo_aligned': (storage_surprise < 0 and cold_forecast) or 
                         (storage_surprise > 0 and not cold_forecast),
        'rationale': f"Storage surprise: {storage_surprise:.0f} Bcf, "
                     f"HDD anomaly: {hdd_anomaly:+.0f}, "
                     f"Storage vs avg: {storage_vs_avg:+.1f}%"
    }
```

!!! warning "Thursday Trading Protocol"
    Every Thursday at 10:30 AM ET, be prepared:
    
    1. **Pre-report**: Know consensus estimate and your model's estimate
    2. **T+0 seconds**: Compare actual vs consensus
    3. **T+30 seconds**: Cross-reference with current weather forecast
    4. **T+1 minute**: Execute if combo signal aligns
    5. **T+5 minutes**: Assess price action quality

---

## 6. Trading the Storage Report

### 6.1 Pre-Report Positioning

The storage report is the most important weekly event for natural gas:

```python
def pre_storage_report_analysis(
    current_storage: float,
    weather_hdds: float,
    consensus_estimate: float,
    model_estimate: float
) -> dict:
    """
    Analyze pre-report positioning opportunity
    
    Parameters:
    -----------
    current_storage : float
        Most recent storage level (Bcf)
    weather_hdds : float
        Actual HDDs during reporting period
    consensus_estimate : float
        Market consensus for storage change
    model_estimate : float
        Our model's estimate for storage change
    
    Returns:
    --------
    analysis : dict
        Trading analysis and recommendation
    """
    # Calculate our divergence from consensus
    divergence = model_estimate - consensus_estimate
    
    # Calculate implied price move
    # Typical: $0.02-0.05 per 10 Bcf surprise
    expected_move = divergence * 0.003  # $/MMBtu per Bcf
    
    # Assess confidence based on weather clarity
    # (In practice, correlate HDD accuracy with storage accuracy)
    
    analysis = {
        'consensus': consensus_estimate,
        'our_estimate': model_estimate,
        'divergence_bcf': divergence,
        'expected_price_impact': expected_move,
        'direction': 'LONG' if divergence < 0 else 'SHORT',
        'confidence': min(abs(divergence) / 20, 1.0)
    }
    
    return analysis
```

### 6.2 Post-Report Trading

Price response to storage reports follows a predictable pattern:

```
Release Time: 10:30 AM ET
│
├── 10:30-10:31: Initial spike/drop on headline
│
├── 10:31-10:35: Algorithmic response intensifies
│
├── 10:35-10:45: Secondary assessment (regional breakdown)
│
├── 10:45-11:00: Comparison to weather forecasts
│
└── 11:00+: Fade or continuation based on technical levels
```

### 6.3 Storage-Weather Combined Signal

```python
def combined_storage_weather_signal(
    storage_vs_avg: float,
    weather_z_score: float,
    model_agreement: float
) -> dict:
    """
    Combine storage level and weather forecast into trading signal
    
    Parameters:
    -----------
    storage_vs_avg : float
        Storage deviation from 5-year average (%)
    weather_z_score : float
        Temperature forecast deviation (z-score)
    model_agreement : float
        Weather model agreement [0, 1]
    
    Returns:
    --------
    signal : dict
        Trading signal with direction and strength
    """
    # Storage component: negative = bullish
    storage_signal = -storage_vs_avg / 20  # Scale to [-1, 1]
    
    # Weather component: negative temp = cold = bullish
    weather_signal = -weather_z_score / 3  # Scale to [-1, 1]
    
    # Interaction term: low storage + cold = very bullish
    interaction = storage_signal * weather_signal * 0.5
    
    # Combined signal
    raw_signal = storage_signal + weather_signal + interaction
    
    # Apply confidence adjustment
    adjusted_signal = raw_signal * model_agreement
    
    # Clip to [-2, 2]
    final_signal = np.clip(adjusted_signal, -2, 2)
    
    return {
        'direction': 'LONG' if final_signal > 0 else 'SHORT',
        'strength': abs(final_signal),
        'storage_component': storage_signal,
        'weather_component': weather_signal,
        'interaction': interaction,
        'confidence': model_agreement
    }
```

---

## 7. Regional Storage Analysis

### 7.1 Regional Breakdown

EIA reports storage by region:

| Region | Capacity | Key Characteristics |
|--------|----------|---------------------|
| **East** | 900 Bcf | Demand center, limited production |
| **Midwest** | 1,100 Bcf | Aquifer storage, moderate demand |
| **South Central** | 1,400 Bcf | Near production, salt caverns |
| **Mountain** | 200 Bcf | Small market |
| **Pacific** | 400 Bcf | Isolated, LNG import capable |

### 7.2 Regional Price Implications

Regional storage levels drive basis differentials:

$$
\text{Basis}_{\text{region}} = f(\text{Storage}_{\text{region}}, \text{Pipeline Flow}, \text{Local Weather})
$$

---

## 8. End-of-Season Analysis

### 8.1 March 31 Storage Projections

End-of-season storage is a key focal point:

```python
def end_of_season_risk_assessment(
    current_storage: float,
    current_date: str,
    remaining_hdd_forecast: float,
    historical_hdd_avg: float
) -> dict:
    """
    Assess end-of-heating-season storage risk
    
    Parameters:
    -----------
    current_storage : float
        Current storage level (Bcf)
    current_date : str
        Current date (YYYY-MM-DD)
    remaining_hdd_forecast : float
        Total remaining HDD forecast
    historical_hdd_avg : float
        Historical average remaining HDD
    
    Returns:
    --------
    assessment : dict
        Risk assessment for end-of-season storage
    """
    from datetime import datetime, date
    
    current = datetime.strptime(current_date, '%Y-%m-%d')
    end_season = datetime(current.year, 3, 31)
    if current.month > 6:
        end_season = datetime(current.year + 1, 3, 31)
    
    days_remaining = (end_season - current).days
    
    # Estimate remaining withdrawal
    hdd_deviation = remaining_hdd_forecast - historical_hdd_avg
    withdrawal_per_hdd = 3.5  # Bcf
    
    expected_withdrawal = historical_hdd_avg * withdrawal_per_hdd
    weather_adjustment = hdd_deviation * withdrawal_per_hdd
    
    projected_end_storage = current_storage - expected_withdrawal - weather_adjustment
    
    # Risk categorization
    if projected_end_storage < 1000:
        risk_level = 'CRITICAL'
    elif projected_end_storage < 1500:
        risk_level = 'ELEVATED'
    elif projected_end_storage < 2000:
        risk_level = 'MODERATE'
    else:
        risk_level = 'NORMAL'
    
    return {
        'current_storage': current_storage,
        'projected_end_storage': projected_end_storage,
        'days_remaining': days_remaining,
        'risk_level': risk_level,
        'weather_impact': weather_adjustment
    }
```

### 8.2 Market Pricing of Storage Risk

When end-of-season storage looks low:

1. **Prompt month premium**: Immediate demand for gas
2. **Winter strip premium**: Entire heating season bids up
3. **Calendar spread inversion**: Near months > far months
4. **Increased volatility**: Uncertainty premium rises

---

## 9. Summary

Natural gas storage is the critical variable connecting weather forecasts to prices:

1. **Seasonal cycle** creates predictable injection/withdrawal patterns
2. **EIA weekly report** is the most important market-moving data
3. **Storage levels** determine price sensitivity to weather shocks
4. **Regional analysis** reveals basis trading opportunities
5. **End-of-season projections** drive seasonal positioning

The trader's edge comes from better forecasting the storage trajectory through superior weather analysis.

---

## References

1. EIA. "Weekly Natural Gas Storage Report Methodology." [eia.gov/naturalgas/storage](https://www.eia.gov/naturalgas/storage/)
2. EIA. "Natural Gas Data." [eia.gov/naturalgas/data.php](https://www.eia.gov/naturalgas/data.php)
3. EIA API Documentation. [eia.gov/opendata](https://www.eia.gov/opendata/)
4. Mer's Blog (메르의 블로그). "천연가스 가격이 일주일간 70%가 올랐다." [blog.naver.com/ranto28/224159783476](https://blog.naver.com/ranto28/224159783476)
5. Serletis, A., & Shahmoradi, A. (2006). "Measuring and Testing Natural Gas and Electricity Markets Volatility." *Energy Economics*
6. Brown, S.P., & Yücel, M.K. (2008). "What Drives Natural Gas Prices?" *Energy Journal*
7. Mu, X. (2007). "Weather, storage, and natural gas price dynamics." *Journal of Futures Markets*

---

!!! info "Next Section"
    Continue to [Weather-Based Trading Strategies](../trading_strategies/seasonal_spread_strategies.md) to learn specific trading approaches.
