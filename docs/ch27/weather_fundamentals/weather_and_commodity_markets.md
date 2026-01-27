# Weather and Commodity Markets

## Learning Objectives

By the end of this section, you will be able to:

- Understand the fundamental linkage between weather events and commodity prices
- Identify which commodities are most sensitive to weather conditions
- Analyze information asymmetry in weather-based trading
- Apply weather forecasting insights to trading decisions

---

## 1. Introduction: Weather as a Market Driver

Weather represents one of the most significant exogenous factors affecting commodity markets. Unlike macroeconomic indicators or corporate earnings, weather events are:

- **Physically measurable** with increasing precision
- **Temporally predictable** (to varying degrees)
- **Geographically localized** yet globally impactful
- **Non-manipulable** by market participants

This creates unique trading opportunities for participants who can process meteorological information faster and more accurately than the market consensus.

---

## 2. The Weather-Commodity Transmission Mechanism

### 2.1 Supply-Side Effects

Weather affects commodity supply through multiple channels:

$$
S(t) = S_0 \cdot f(\text{Temperature}, \text{Precipitation}, \text{Extreme Events})
$$

| Weather Factor | Affected Commodities | Mechanism |
|----------------|---------------------|-----------|
| Temperature | Natural Gas, Power | Heating/Cooling demand |
| Precipitation | Grains, Soft Commodities | Crop yields |
| Hurricanes | Crude Oil, Natural Gas | Production disruption |
| Drought | Grains, Livestock | Supply reduction |
| Frost/Freeze | Coffee, Citrus | Crop damage |

### 2.2 Demand-Side Effects

Weather-driven demand changes are often more predictable but equally impactful:

$$
D(t) = D_{\text{base}} + \beta_{\text{HDD}} \cdot \text{HDD}(t) + \beta_{\text{CDD}} \cdot \text{CDD}(t)
$$

where:

- $\text{HDD}$ = Heating Degree Days = $\max(65°F - T, 0)$
- $\text{CDD}$ = Cooling Degree Days = $\max(T - 65°F, 0)$

---

## 3. Information Flow and Market Efficiency

### 3.1 Weather Forecast Timeline

Weather information flows through the market with predictable time lags:

```
Day -14 to -7:  Long-range ensemble forecasts (low confidence)
Day -7 to -3:   Medium-range forecasts (moderate confidence)
Day -3 to -1:   Short-range forecasts (high confidence)
Day 0:          Actual weather realization
Day +1 to +7:   Impact assessment and inventory reports
```

### 3.2 Trading Windows

The key insight for weather-based trading is identifying when forecast uncertainty resolves:

!!! tip "Optimal Entry Timing"
    The highest risk-adjusted returns typically occur when weather models **converge** from disagreement to consensus. This usually happens 3-5 days before an extreme event, before the information is fully reflected in prices.

#### Market Participant Reaction Timeline

Different market participants react to weather information at different speeds, creating exploitable time lags:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INFORMATION FLOW TIMELINE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Weather Model Release (GFS/ECMWF)                                          │
│         │                                                                   │
│         ▼                                                                   │
│  ┌──────────────────┐                                                       │
│  │ Professional     │  Response Time: Minutes to Hours                      │
│  │ Weather Traders  │  - Direct model data feeds                            │
│  │ & Hedge Funds    │  - Algorithmic interpretation                         │
│  └────────┬─────────┘  - Pre-positioned for scenarios                       │
│           │                                                                 │
│           ▼  (4-12 hours)                                                   │
│  ┌──────────────────┐                                                       │
│  │ Energy Trading   │  Response Time: Hours to 1 Day                        │
│  │ Desks & Utilities│  - Bloomberg/Reuters alerts                           │
│  └────────┬─────────┘  - Internal meteorologist analysis                    │
│           │                                                                 │
│           ▼  (1-2 days)                                                     │
│  ┌──────────────────┐                                                       │
│  │ Media Coverage & │  Response Time: 1-2 Days                              │
│  │ General Market   │  - News articles published                            │
│  └────────┬─────────┘  - Retail investor awareness                          │
│           │                                                                 │
│           ▼  (3-5 days)                                                     │
│  ┌──────────────────┐                                                       │
│  │ Physical Market  │  Response Time: 3-5 Days                              │
│  │ Supply/Demand    │  - Actual consumption changes                         │
│  └──────────────────┘  - Storage withdrawals realized                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Exploiting Information Asymmetry

| Phase | Timing | Market State | Trading Strategy |
|-------|--------|--------------|------------------|
| **Phase 1: Model Release** | T+0 to T+6h | Only quants aware | Establish initial position |
| **Phase 2: Professional Response** | T+6h to T+24h | Institutions trading | Add to position on confirmation |
| **Phase 3: Media Coverage** | T+1d to T+2d | Broad awareness | Consider partial profit-taking |
| **Phase 4: Physical Realization** | T+3d to T+5d | Full price discovery | Exit remaining position |

```python
def estimate_price_discovery_stage(
    hours_since_forecast: float,
    media_coverage: bool,
    storage_report_released: bool
) -> dict:
    """
    Estimate current stage of price discovery for weather event
    
    Parameters:
    -----------
    hours_since_forecast : float
        Hours since significant forecast change
    media_coverage : bool
        Whether mainstream media has covered the event
    storage_report_released : bool
        Whether EIA storage report reflecting event has been released
    
    Returns:
    --------
    stage : dict
        Current price discovery stage and recommended action
    """
    if storage_report_released:
        return {
            'stage': 4,
            'name': 'Physical Realization',
            'price_discovery': '90-100%',
            'action': 'EXIT or FADE',
            'edge_remaining': 'Low'
        }
    elif media_coverage:
        return {
            'stage': 3,
            'name': 'Media Coverage',
            'price_discovery': '60-80%',
            'action': 'PARTIAL PROFIT',
            'edge_remaining': 'Medium-Low'
        }
    elif hours_since_forecast > 12:
        return {
            'stage': 2,
            'name': 'Professional Response',
            'price_discovery': '30-50%',
            'action': 'ADD ON CONFIRMATION',
            'edge_remaining': 'Medium'
        }
    else:
        return {
            'stage': 1,
            'name': 'Model Release',
            'price_discovery': '10-20%',
            'action': 'ESTABLISH POSITION',
            'edge_remaining': 'High'
        }
```

!!! warning "First-Mover Advantage"
    The trader who can interpret weather model data within hours of release has a significant edge. By the time weather events make mainstream news, 60-80% of the price move may have already occurred.

### 3.3 Information Sources

| Source | Update Frequency | Lead Time | Primary Use |
|--------|------------------|-----------|-------------|
| GFS (US) | 4x daily | 16 days | Baseline forecast |
| ECMWF (EU) | 2x daily | 15 days | Higher accuracy |
| Ensemble Models | Daily | 16 days | Probability ranges |
| Private Services | Real-time | Variable | Trading edge |

---

## 4. The Polar Vortex Case Study

### 4.1 Meteorological Background

The **polar vortex** is a large area of low pressure and cold air surrounding the Earth's poles. When the jet stream weakens, this cold air can spill southward into mid-latitudes.

Key indicators of polar vortex disruption:

1. **Arctic Oscillation (AO) Index** turning negative
2. **Jet stream meandering** pattern
3. **Sudden Stratospheric Warming (SSW)** events

### 4.2 Historical Events

| Event | Date | Natural Gas Price Impact | Duration |
|-------|------|-------------------------|----------|
| Great Appalachian Storm | 1950 | N/A (pre-modern markets) | 3 days |
| Superstorm | 1996 | +40% in 2 weeks | 5 days |
| Texas Freeze | Feb 2021 | +400% (spot) | 7 days |
| Polar Express | Jan 2026 | +70% in 1 week | Ongoing |

### 4.3 The January 2026 Event

The "Polar Express" event of January 2026 combined multiple risk factors:

$$
\text{Impact Severity} = f(\text{Geographic Extent}, \text{Temperature Anomaly}, \text{Duration})
$$

- **Geographic extent**: Near-universal US coverage
- **Temperature anomaly**: 20-40°F below normal
- **Duration**: 5+ days of extreme cold

The result was a natural gas price surge from $3.1/MMBtu to $5.28/MMBtu in just 5 trading days—a 70% increase.

---

## 5. Commodity-Specific Weather Sensitivities

### 5.1 Natural Gas

Natural gas exhibits the highest weather sensitivity due to:

- Limited storage capacity relative to demand
- Inelastic short-term supply
- Direct heating/cooling demand linkage
- Pipeline and production vulnerabilities

**Price elasticity to temperature:**

$$
\frac{\partial P}{\partial T} \approx -\$0.05 \text{ to } -\$0.15 \text{ per } ^\circ F \text{ (winter)}
$$

### 5.2 Agricultural Commodities

Agricultural markets respond to weather with longer time horizons:

| Stage | Weather Sensitivity | Price Response |
|-------|---------------------|----------------|
| Planting | Precipitation, temperature | Moderate |
| Growing | Drought, heat stress | High |
| Harvest | Rain, early frost | Very High |
| Storage | Humidity, flooding | Low |

### 5.3 Energy Complex

The broader energy complex shows correlated weather responses:

$$
\rho(\text{NG}, \text{Power}) \approx 0.85 \text{ during extreme cold}
$$

---

## 6. Practical Implications for Traders

### 6.1 Data Requirements

Essential data feeds for weather-based trading:

1. **Weather Models**: GFS, ECMWF, NAM
2. **Degree Day Forecasts**: HDD/CDD projections
3. **Inventory Data**: EIA weekly reports
4. **Grid Status**: ERCOT, PJM real-time data

### 6.2 Analytical Framework

```python
def weather_trading_signal(forecast_data, historical_data):
    """
    Generate trading signal based on weather forecast divergence
    
    Parameters:
    -----------
    forecast_data : dict
        Current weather model outputs
    historical_data : DataFrame
        Historical weather-price relationships
    
    Returns:
    --------
    signal : float
        Trading signal strength [-1, 1]
    """
    # Calculate forecast surprise
    forecast_hdd = forecast_data['hdd_forecast']
    normal_hdd = historical_data['hdd_30yr_avg']
    surprise = (forecast_hdd - normal_hdd) / historical_data['hdd_std']
    
    # Model convergence factor
    gfs_ecmwf_diff = abs(forecast_data['gfs_temp'] - forecast_data['ecmwf_temp'])
    convergence = 1 - min(gfs_ecmwf_diff / 10, 1)
    
    # Combine factors
    signal = np.tanh(surprise * convergence)
    
    return signal
```

---

## 7. Summary

Weather-based commodity trading offers unique opportunities due to:

1. **Measurable physical drivers** with known transmission mechanisms
2. **Predictable information flow** with exploitable time lags
3. **Model convergence signals** indicating high-confidence forecasts
4. **Structural market features** (storage, demand inelasticity) amplifying price moves

The key challenge is developing systematic approaches that can process meteorological data faster than competing market participants while managing the inherent forecast uncertainty.

---

## References

1. Roll, R. (1984). "Orange Juice and Weather." *American Economic Review*
2. Considine, T. (2000). "The impacts of weather variations on energy demand and carbon emissions." *Resource and Energy Economics*
3. Mu, X. (2007). "Weather, storage, and natural gas price dynamics." *Journal of Futures Markets*
4. Ederington, L., Fernando, C., Holland, K., & Linn, S. (2019). "The response of natural gas futures to weather events." *Energy Economics*

---

!!! info "Next Section"
    Continue to [Henry Hub and Natural Gas Markets](../natural_gas/henry_hub_market_structure.md) to understand the specific market mechanics of natural gas trading.
