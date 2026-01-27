# Weather Forecasting for Traders

## Learning Objectives

By the end of this section, you will be able to:

- Access and interpret professional weather forecast data
- Understand the strengths and limitations of different weather models
- Build a systematic weather monitoring workflow
- Translate forecast uncertainty into position sizing

---

## 1. Weather Model Landscape

### 1.1 Global Numerical Weather Prediction (NWP) Models

| Model | Agency | Resolution | Runs/Day | Forecast Length | Strengths |
|-------|--------|-----------|----------|-----------------|-----------|
| **GFS** | NOAA (US) | 13 km | 4 | 16 days | Fast, frequent, free |
| **ECMWF** | EU | 9 km | 2 | 15 days | Most accurate globally |
| **CMC** | Canada | 15 km | 2 | 10 days | Good for North America |
| **UKMO** | UK Met | 10 km | 2 | 7 days | Best for Europe |
| **JMA** | Japan | 20 km | 2 | 11 days | Best for Asia-Pacific |
| **KMA** | Korea | 12 km | 4 | 10 days | Good for East Asia |

### 1.2 Model Hierarchy

```
Global Models (GFS, ECMWF)
    ↓
Regional Models (NAM, HRRR, WRF)
    ↓
Local Models (High-resolution, urban)
    ↓
Statistical Post-Processing (MOS, NBM)
    ↓
Final Forecast Product
```

### 1.3 Weather Model Divergence Trading

A key trading strategy exploits the **convergence and divergence** between major weather models. When models disagree, uncertainty is high. When models converge on the same forecast, confidence increases significantly.

#### The Convergence Signal

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MODEL CONVERGENCE TIMELINE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Day -10: Models Diverge                                                    │
│  ┌─────┐     GFS: +5°F above normal                                         │
│  │ LOW │     ECMWF: -3°F below normal                                       │
│  │CONF.│     Spread: 8°F → HIGH UNCERTAINTY                                 │
│  └─────┘     Action: NO POSITION                                            │
│                                                                             │
│  Day -7: Models Begin Converging                                            │
│  ┌─────┐     GFS: -2°F below normal                                         │
│  │ MED │     ECMWF: -5°F below normal                                       │
│  │CONF.│     Spread: 3°F → MODERATE UNCERTAINTY                             │
│  └─────┘     Action: SMALL POSITION                                         │
│                                                                             │
│  Day -4: Models Converge                                                    │
│  ┌─────┐     GFS: -8°F below normal                                         │
│  │HIGH │     ECMWF: -10°F below normal                                      │
│  │CONF.│     Spread: 2°F → LOW UNCERTAINTY                                  │
│  └─────┘     Action: FULL POSITION (optimal entry)                          │
│                                                                             │
│  Day -1: Consensus Established                                              │
│  ┌─────┐     All models agree: Extreme cold incoming                        │
│  │VERY │     Media coverage begins                                          │
│  │HIGH │     Action: HOLD or PARTIAL PROFIT                                 │
│  └─────┘     (Price already reflects most of the move)                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Multi-Model Comparison Strategy

```python
def model_divergence_trading_signal(
    gfs_forecast: float,
    ecmwf_forecast: float,
    jma_forecast: float,
    kma_forecast: float,
    climatology_normal: float
) -> dict:
    """
    Generate trading signal based on weather model divergence/convergence
    
    Parameters:
    -----------
    gfs_forecast : float
        GFS temperature forecast (°F)
    ecmwf_forecast : float
        ECMWF temperature forecast (°F)
    jma_forecast : float
        JMA temperature forecast (°F)
    kma_forecast : float
        KMA temperature forecast (°F)
    climatology_normal : float
        Normal temperature for this time of year (°F)
    
    Returns:
    --------
    signal : dict
        Trading signal with confidence and recommended action
    """
    models = {
        'GFS': gfs_forecast,
        'ECMWF': ecmwf_forecast,
        'JMA': jma_forecast,
        'KMA': kma_forecast
    }
    
    forecasts = list(models.values())
    
    # Calculate model spread (divergence)
    model_spread = max(forecasts) - min(forecasts)
    
    # Calculate consensus forecast
    consensus = np.mean(forecasts)
    
    # Calculate deviation from normal
    anomaly = consensus - climatology_normal
    
    # Determine confidence based on model agreement
    if model_spread < 3:  # Models agree within 3°F
        confidence = 'HIGH'
        confidence_score = 0.9
        position_scale = 1.0
    elif model_spread < 6:  # Models agree within 6°F
        confidence = 'MEDIUM'
        confidence_score = 0.6
        position_scale = 0.5
    elif model_spread < 10:  # Models disagree by up to 10°F
        confidence = 'LOW'
        confidence_score = 0.3
        position_scale = 0.25
    else:  # Models strongly disagree
        confidence = 'VERY LOW'
        confidence_score = 0.1
        position_scale = 0.0  # No position
    
    # Determine direction based on anomaly
    if anomaly < -5:  # Cold anomaly
        direction = 'LONG'  # Bullish natural gas
        strength = min(abs(anomaly) / 15, 1.0)
    elif anomaly > 5:  # Warm anomaly
        direction = 'SHORT'  # Bearish natural gas
        strength = min(abs(anomaly) / 15, 1.0)
    else:
        direction = 'NEUTRAL'
        strength = 0.0
    
    return {
        'direction': direction,
        'confidence': confidence,
        'confidence_score': confidence_score,
        'position_scale': position_scale,
        'model_spread': model_spread,
        'consensus_forecast': consensus,
        'anomaly': anomaly,
        'strength': strength,
        'models': models,
        'recommendation': f"{direction} with {confidence} confidence" if direction != 'NEUTRAL' 
                          else "No trade - neutral forecast"
    }

# Example: Models converging on cold forecast
# signal = model_divergence_trading_signal(
#     gfs_forecast=25,    # Cold
#     ecmwf_forecast=23,  # Colder
#     jma_forecast=24,    # Cold
#     kma_forecast=26,    # Cold
#     climatology_normal=35
# )
# Result: LONG with HIGH confidence (spread=3°F, anomaly=-10°F)
```

!!! tip "The Convergence Edge"
    The optimal trading window opens when models **converge from disagreement to consensus** on an extreme forecast. This typically occurs 3-5 days before the weather event, providing the best risk-adjusted entry point.

---

## 2. Key Weather Data Products

### 2.1 Temperature Products

**Heating Degree Days (HDD):**

$$
\text{HDD} = \max(65°F - T_{\text{avg}}, 0)
$$

**Cooling Degree Days (CDD):**

$$
\text{CDD} = \max(T_{\text{avg}} - 65°F, 0)
$$

**Population-Weighted Degree Days:**

$$
\text{PW-HDD} = \sum_{i=1}^{n} w_i \cdot \text{HDD}_i
$$

where $w_i$ is the population weight for region $i$.

!!! note "Why 65°F?"
    The 65°F base temperature is a historical convention representing the point at which heating/cooling demand begins. Some traders use adjusted bases (60°F, 70°F) for specific analyses.

### 2.2 Ensemble Forecasts

Rather than a single deterministic forecast, ensemble systems run multiple simulations with slightly perturbed initial conditions:

| Ensemble System | Members | Purpose |
|-----------------|---------|---------|
| GEFS (GFS Ensemble) | 31 | Probability estimation |
| ECMWF EPS | 51 | Risk assessment |
| NAEFS | 42 | North American focus |
| CMCE | 21 | Canadian ensemble |

**Interpreting Ensemble Spread:**

```python
def ensemble_confidence(ensemble_forecasts):
    """
    Calculate confidence from ensemble spread
    
    Parameters:
    -----------
    ensemble_forecasts : array
        Temperature forecasts from all ensemble members
    
    Returns:
    --------
    confidence : float
        Confidence level [0, 1]
    spread : float
        Inter-quartile range of forecasts
    """
    q25 = np.percentile(ensemble_forecasts, 25)
    q75 = np.percentile(ensemble_forecasts, 75)
    spread = q75 - q25
    
    # Typical winter temperature spread: 5-15°F
    # Narrow spread (<5°F) = high confidence
    # Wide spread (>15°F) = low confidence
    confidence = max(0, 1 - (spread - 5) / 15)
    
    return confidence, spread
```

---

## 3. Data Sources and Access

### 3.1 Free Public Sources

| Source | URL | Data Type | Update Frequency |
|--------|-----|-----------|------------------|
| NOAA NOMADS | nomads.ncep.noaa.gov | GFS, NAM, HRRR | Every 6 hours |
| NCEI | ncei.noaa.gov | Historical data | Daily |
| EIA | eia.gov | Storage reports | Weekly (Thursday) |
| AccuWeather | accuweather.com | Consumer forecasts | Real-time |

### 3.2 Professional Data Services

| Provider | Cost Range | Key Products |
|----------|-----------|--------------|
| DTN | $$$ | Proprietary forecasts, HDD/CDD |
| Maxar | $$$ | Power demand forecasts |
| Commodity Weather Group | $$$$ | Natural gas specific |
| Speedwell Weather | $$ | Degree day derivatives |

### 3.3 Python Data Access

```python
import requests
from datetime import datetime, timedelta
import xarray as xr

class WeatherDataFetcher:
    """Fetch weather forecast data from public APIs"""
    
    def __init__(self):
        self.gfs_base = "https://nomads.ncep.noaa.gov/dods/gfs_0p25"
        
    def get_gfs_forecast(self, date=None, variable='tmp2m'):
        """
        Fetch GFS forecast data
        
        Parameters:
        -----------
        date : datetime
            Forecast initialization date
        variable : str
            Weather variable (tmp2m, ugrd10m, etc.)
        
        Returns:
        --------
        forecast : xarray.Dataset
            Forecast data
        """
        if date is None:
            date = datetime.utcnow()
            
        # Format: gfs_0p25/gfs20260127/gfs_0p25_00z
        date_str = date.strftime('%Y%m%d')
        url = f"{self.gfs_base}/gfs{date_str}/gfs_0p25_00z"
        
        try:
            ds = xr.open_dataset(url)
            forecast = ds[variable]
            return forecast
        except Exception as e:
            print(f"Error fetching GFS data: {e}")
            return None
    
    def calculate_regional_hdd(self, temp_data, region='us_total'):
        """
        Calculate population-weighted HDD for a region
        
        Parameters:
        -----------
        temp_data : xarray.DataArray
            Temperature forecast grid
        region : str
            Region identifier
        
        Returns:
        --------
        hdd : float
            Population-weighted HDD
        """
        # Population weights by region (simplified)
        weights = {
            'us_total': self._us_pop_weights(),
            'us_east': self._us_east_weights(),
            'us_west': self._us_west_weights()
        }
        
        # Convert Kelvin to Fahrenheit if needed
        temp_f = (temp_data - 273.15) * 9/5 + 32
        
        # Calculate HDD
        hdd_grid = np.maximum(65 - temp_f, 0)
        
        # Apply population weights
        weighted_hdd = np.average(hdd_grid, weights=weights[region])
        
        return weighted_hdd
```

---

## 4. Forecast Skill and Accuracy

### 4.1 Skill Degradation with Time

Forecast skill decays approximately exponentially with lead time:

$$
\text{Skill}(t) = \text{Skill}_0 \cdot e^{-t/\tau}
$$

where $\tau \approx 5$ days for temperature forecasts.

| Lead Time | Temperature RMSE | HDD Accuracy | Trading Utility |
|-----------|-----------------|--------------|-----------------|
| Day 1-3 | 2-3°F | ±5% | High confidence |
| Day 4-7 | 4-6°F | ±15% | Moderate confidence |
| Day 8-10 | 6-8°F | ±25% | Low confidence |
| Day 11-14 | 8-12°F | ±40% | Trend guidance only |

### 4.2 Systematic Biases

Weather models exhibit known biases that traders can exploit:

**GFS:**
- Tends to underforecast extreme cold
- Often too progressive with storm systems
- Better for western US

**ECMWF:**
- Generally most accurate
- Slight cold bias in winter
- Better for pattern changes

**Ensemble Mean:**
- Always less extreme than reality
- Underestimates tail events
- Good for expected value, bad for extremes

---

## 5. Model Comparison and Blending

### 5.1 The "Model Wars" Framework

Rather than relying on a single model, professional forecasters blend multiple models:

$$
T_{\text{blend}} = \sum_{i=1}^{n} w_i \cdot T_i
$$

where weights $w_i$ are determined by recent forecast skill.

### 5.2 Identifying High-Confidence Forecasts

```python
def model_agreement_score(forecasts_dict):
    """
    Calculate agreement between major weather models
    
    Parameters:
    -----------
    forecasts_dict : dict
        {'gfs': temp_gfs, 'ecmwf': temp_ecmwf, 'cmc': temp_cmc, ...}
    
    Returns:
    --------
    agreement : float
        Agreement score [0, 1]
    consensus_forecast : float
        Weighted average forecast
    """
    temps = list(forecasts_dict.values())
    
    # Calculate spread
    spread = max(temps) - min(temps)
    
    # Typical spread thresholds
    if spread < 3:  # Models agree within 3°F
        agreement = 1.0
    elif spread < 6:
        agreement = 0.7
    elif spread < 10:
        agreement = 0.4
    else:
        agreement = 0.2
    
    # Weighted consensus (ECMWF weighted higher)
    weights = {'gfs': 0.25, 'ecmwf': 0.40, 'cmc': 0.15, 'ukmo': 0.20}
    consensus_forecast = sum(
        forecasts_dict[m] * weights.get(m, 0.2) 
        for m in forecasts_dict
    )
    
    return agreement, consensus_forecast
```

---

## 6. Building a Weather Trading Workflow

### 6.1 Daily Routine

```
06:00 UTC: Review overnight ECMWF run
12:00 UTC: Compare with GFS 06z run
13:00 UTC: Check ensemble spread and trends
14:00 UTC: Review CWG/DTN proprietary forecasts
15:00 UTC: Update trading signals
18:00 UTC: Review GFS 12z run
20:00 UTC: Final position adjustments

Weekly:
- Thursday 10:30 ET: EIA storage report
- Review actual vs forecast HDD
- Update model bias estimates
```

### 6.2 Alert System

```python
class WeatherAlertSystem:
    """Generate trading alerts from weather data"""
    
    def __init__(self):
        self.hdd_threshold = 2.0  # Standard deviations from normal
        self.confidence_threshold = 0.6
        
    def check_temperature_anomaly(self, forecast_hdd, normal_hdd, std_hdd):
        """
        Check for significant temperature anomalies
        """
        z_score = (forecast_hdd - normal_hdd) / std_hdd
        
        if z_score > self.hdd_threshold:
            return {
                'type': 'COLD_ALERT',
                'severity': min(z_score / 3, 1.0),
                'hdd_deviation': forecast_hdd - normal_hdd
            }
        elif z_score < -self.hdd_threshold:
            return {
                'type': 'WARM_ALERT', 
                'severity': min(-z_score / 3, 1.0),
                'hdd_deviation': forecast_hdd - normal_hdd
            }
        return None
    
    def check_model_convergence(self, model_forecasts, prev_forecasts):
        """
        Alert when models converge on extreme outcome
        """
        current_spread = max(model_forecasts) - min(model_forecasts)
        prev_spread = max(prev_forecasts) - min(prev_forecasts)
        
        # Convergence = spread narrowing while maintaining extreme
        if current_spread < prev_spread * 0.7:  # 30% reduction
            consensus = np.mean(model_forecasts)
            return {
                'type': 'CONVERGENCE_ALERT',
                'spread_reduction': 1 - current_spread/prev_spread,
                'consensus_value': consensus
            }
        return None
```

---

## 7. Position Sizing Based on Forecast Confidence

### 7.1 Kelly-Inspired Framework

Adjust position size based on forecast confidence:

$$
\text{Position Size} = \text{Base Size} \times \text{Confidence} \times \text{Signal Strength}
$$

### 7.2 Practical Implementation

```python
def calculate_weather_position_size(
    base_position: float,
    model_agreement: float,
    forecast_lead_time: int,
    signal_z_score: float
) -> float:
    """
    Calculate position size based on weather forecast confidence
    
    Parameters:
    -----------
    base_position : float
        Maximum position size in contracts/shares
    model_agreement : float
        Agreement score between models [0, 1]
    forecast_lead_time : int
        Days until weather event
    signal_z_score : float
        Temperature deviation z-score
    
    Returns:
    --------
    position : float
        Recommended position size
    """
    # Lead time decay
    lead_time_factor = np.exp(-forecast_lead_time / 7)
    
    # Signal strength (capped at 3 sigma)
    signal_factor = min(abs(signal_z_score) / 3, 1.0)
    
    # Combine factors
    position = base_position * model_agreement * lead_time_factor * signal_factor
    
    return position
```

---

## 8. Common Pitfalls

### 8.1 Recency Bias

Don't overweight the latest model run:

!!! warning "The 00z Trap"
    The most recent model run is not always the best. Look for consistency across multiple runs before trading on a forecast change.

### 8.2 Confirmation Bias

Actively seek disconfirming evidence:

- If you're bullish on NG, focus on models showing warmer outcomes
- If models disagree, err on the side of caution

### 8.3 False Precision

Remember the limits of predictability:

- Day 10 forecasts are guidelines, not predictions
- Ensemble spread > signal strength → reduce conviction
- A 50% chance of extreme cold ≠ average outcome

---

## 9. Summary

Effective weather forecasting for trading requires:

1. **Multiple data sources**: GFS, ECMWF, ensembles, private services
2. **Systematic workflow**: Daily monitoring routine
3. **Confidence calibration**: Match position size to forecast certainty
4. **Model awareness**: Know biases and limitations
5. **Alert systems**: Automated monitoring for anomalies

The goal is not perfect forecasts—it's extracting the maximum signal from imperfect information while managing uncertainty appropriately.

---

## References

1. Kalnay, E. (2003). *Atmospheric Modeling, Data Assimilation and Predictability*. Cambridge University Press.
2. Wilks, D.S. (2011). *Statistical Methods in the Atmospheric Sciences*. Academic Press.
3. Richardson, D.S. (2000). "Skill and relative economic value of the ECMWF ensemble prediction system." *Quarterly Journal of the Royal Meteorological Society*
4. Bauer, P., Thorpe, A., & Brunet, G. (2015). "The quiet revolution of numerical weather prediction." *Nature*

---

!!! info "Next Section"
    Continue to [Henry Hub and Natural Gas Markets](../natural_gas/henry_hub_market_structure.md) to understand the market structure and trading mechanics.
