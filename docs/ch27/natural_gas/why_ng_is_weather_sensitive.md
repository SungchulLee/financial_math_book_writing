# Why Natural Gas is Weather-Sensitive

Natural gas exhibits the strongest weather sensitivity of any major commodity, with price swings of 10-30% occurring within days based on temperature forecasts. This unique characteristic creates both risks and opportunities for traders, making weather analysis an essential component of natural gas market participation.

!!! abstract "Chapter Overview"
    **Prerequisites:** Basic supply/demand economics, futures market mechanics
    
    **Learning Objectives:**
    
    - Understand the physical drivers of natural gas weather sensitivity
    - Quantify the relationship between temperature and demand
    - Analyze seasonal patterns and storage dynamics
    - Apply weather data to trading strategies

---

## 1. The Fundamental Driver: Heating and Cooling Demand

### 1.1 Natural Gas End-Use Breakdown

Natural gas consumption in the United States divides into four major sectors:

| Sector | Share of Demand | Weather Sensitivity |
|--------|-----------------|---------------------|
| Residential | ~15% | **Very High** (heating) |
| Commercial | ~10% | **High** (heating/cooling) |
| Industrial | ~30% | Low-Moderate |
| Electric Power | ~35% | **High** (cooling, peaking) |

The critical insight: approximately **60% of natural gas demand is directly weather-sensitive**, primarily through heating in winter and electricity generation for air conditioning in summer.

### 1.2 Heating Degree Days (HDD)

Heating demand is measured using Heating Degree Days:

$$\text{HDD} = \max(65°F - T_{\text{avg}}, 0)$$

where $T_{\text{avg}}$ is the average daily temperature and 65°F is the baseline temperature below which heating is typically required.

**Example:**

- Average temperature: 35°F
- HDD = 65 - 35 = 30 HDDs
- Interpretation: Significant heating demand

**Weekly and Seasonal Aggregation:**

$$\text{Weekly HDD} = \sum_{i=1}^{7} \text{HDD}_i$$

$$\text{Seasonal HDD} = \sum_{\text{Nov}}^{\text{Mar}} \text{Daily HDD}$$

**Normal vs. Actual:**

| Winter Type | Seasonal HDD | Demand Impact |
|-------------|--------------|---------------|
| Mild | < 3,800 | Below normal demand |
| Normal | 3,800-4,200 | Average demand |
| Cold | 4,200-4,600 | Above normal demand |
| Severe | > 4,600 | Extreme demand, price spikes |

### 1.3 Cooling Degree Days (CDD)

Summer demand uses Cooling Degree Days:

$$\text{CDD} = \max(T_{\text{avg}} - 65°F, 0)$$

**Example:**

- Average temperature: 85°F
- CDD = 85 - 65 = 20 CDDs
- Interpretation: Strong air conditioning demand → electricity demand → gas-fired power generation

!!! info "Why 65°F Baseline?"
    The 65°F (18°C) threshold is a historical convention representing the temperature at which buildings typically require neither heating nor cooling. Some analysts use population-weighted adjustments or regional baselines for more precise modeling.

### 1.4 The Demand Function

Natural gas demand can be modeled as:

$$D_t = \alpha + \beta_1 \cdot \text{HDD}_t + \beta_2 \cdot \text{CDD}_t + \gamma \cdot \text{Industrial}_t + \epsilon_t$$

Empirical estimates for U.S. markets suggest:

- $\beta_1 \approx 3.0-4.0$ Bcf per HDD (winter sensitivity)
- $\beta_2 \approx 1.5-2.5$ Bcf per CDD (summer sensitivity)

**Interpretation:** Each additional HDD increases daily demand by approximately 3-4 billion cubic feet (Bcf). A cold snap producing 10 extra HDDs can increase daily demand by 30-40 Bcf—a 30-40% swing on a typical winter day.

---

## 2. Why Not Other Commodities?

### 2.1 Comparison: Natural Gas vs. Other Energy Commodities

| Commodity | Storage | Substitutes | Demand Elasticity | Weather Impact |
|-----------|---------|-------------|-------------------|----------------|
| **Natural Gas** | Limited (depletes in weeks) | Few short-term | **Very Low** | **Extreme** |
| Crude Oil | Large strategic reserves | Multiple fuels | Low | Moderate |
| Coal | Months of inventory | Gas, renewables | Moderate | Low |
| Electricity | Cannot be stored | Demand response | Very Low | High (but localized) |

### 2.2 The Perfect Storm of Sensitivity

Natural gas uniquely combines several factors that amplify weather sensitivity:

**1. Inelastic Short-Term Demand**

When temperatures drop, households and businesses cannot easily reduce heating:

$$\epsilon_D = \frac{\% \Delta Q}{\% \Delta P} \approx -0.1 \text{ to } -0.2$$

Demand elasticity near zero means price must adjust dramatically to balance supply and demand.

**2. Limited Storage Relative to Demand**

U.S. working gas storage capacity is approximately 4,000 Bcf, representing only about 40-50 days of winter demand:

$$\text{Days of Supply} = \frac{\text{Storage (Bcf)}}{\text{Daily Demand (Bcf)}} \approx \frac{3,500}{85} \approx 41 \text{ days}$$

Compare to crude oil's 60+ days of strategic reserve plus commercial inventory.

**3. Pipeline Constraints**

Natural gas travels by pipeline at fixed capacity. During extreme cold:

- Demand spikes in consuming regions
- Pipeline capacity becomes binding
- Regional prices can diverge dramatically (\$3 at Henry Hub vs. \$50+ at Algonquin)

**4. Production Response Lag**

Unlike oil, natural gas production cannot ramp quickly:

- Wells take months to drill
- Associated gas depends on oil production decisions
- LNG imports face shipping and regasification constraints

---

## 3. Seasonal Patterns and the Storage Cycle

### 3.1 The Annual Storage Cycle

Natural gas follows a predictable annual pattern:

```
         Storage Level (Bcf)
    4000 |         ****
         |       **    **
    3500 |      *        *
         |     *          *
    3000 |    *            *
         |   *              *
    2500 |  *                *
         | *                  *
    2000 |*                    *
         +--+--+--+--+--+--+--+--+--+--+--+--+
           J  F  M  A  M  J  J  A  S  O  N  D
           
         |--- Withdrawal ---|--- Injection ---|
              (Nov-Mar)          (Apr-Oct)
```

**Injection Season (April-October):**

- Demand falls below production
- Excess gas injected into storage
- Target: Reach ~3,800 Bcf by November 1

**Withdrawal Season (November-March):**

- Demand exceeds production
- Storage supplements supply
- Risk: Storage depletion if winter is severe

### 3.2 Storage as a Buffer

Storage moderates price volatility by providing a buffer:

$$\text{Price Sensitivity} \propto \frac{1}{\text{Storage Level}}$$

When storage is:

- **High (> 3,500 Bcf):** Weather impacts muted; supply comfortable
- **Normal (2,500-3,500 Bcf):** Standard weather sensitivity
- **Low (< 2,000 Bcf):** Extreme sensitivity; cold snaps cause price spikes

!!! warning "Storage Threshold Effects"
    Markets exhibit non-linear responses to storage levels. Below approximately 1,500 Bcf, panic buying can occur, and prices become disconnected from fundamental models. The 2014 Polar Vortex drove prices to \$6+ with storage approaching critical levels.

### 3.3 Weeks of Supply Indicator

A more informative metric than absolute storage:

$$\text{Weeks of Supply} = \frac{\text{Current Storage}}{\text{Average Weekly Withdrawal}}$$

| Weeks of Supply | Market Interpretation |
|-----------------|----------------------|
| > 12 weeks | Comfortable, bearish pressure |
| 8-12 weeks | Normal |
| 5-8 weeks | Tight, bullish bias |
| < 5 weeks | Critical, spike risk |

---

## 4. Quantifying Weather-Price Relationships

### 4.1 Temperature-Price Regression

A basic model relates price changes to weather surprises:

$$\Delta P_t = \alpha + \beta \cdot (\text{HDD}_t^{\text{actual}} - \text{HDD}_t^{\text{forecast}}) + \epsilon_t$$

where the coefficient $\beta$ represents price sensitivity to forecast errors.

**Empirical Findings:**

- Winter months: $\beta \approx \$0.02-0.05$ per MMBtu per unexpected HDD
- Effect amplified when storage is low
- Effect diminished when storage is high

### 4.2 Non-Linear Effects

The relationship is not linear—it exhibits convexity at extremes:

$$\Delta P = \beta_1 \cdot \Delta \text{HDD} + \beta_2 \cdot (\Delta \text{HDD})^2 \cdot \mathbf{1}_{\text{HDD} > \text{threshold}}$$

**Interpretation:** Marginal HDDs have increasing price impact during extreme cold because:

1. Storage depletes faster
2. Pipeline constraints bind
3. Demand becomes perfectly inelastic (people must heat)

### 4.3 The Weather Premium in Options

Natural gas options exhibit significant weather-related volatility premium:

$$\sigma_{\text{winter}} \approx 1.5-2.0 \times \sigma_{\text{summer}}$$

January options typically trade at 50-80% implied volatility versus 30-40% for summer months.

**Volatility Term Structure:**

| Contract Month | Typical IV | Rationale |
|----------------|------------|-----------|
| January | 60-80% | Peak heating season |
| February | 55-70% | Late winter risk |
| March | 45-60% | Transition month |
| April | 35-45% | Injection season begins |
| July-August | 35-50% | Cooling demand |
| October | 40-55% | Pre-winter uncertainty |

---

## 5. Regional Price Dynamics

### 5.1 Basis and Weather

Natural gas prices vary by location (basis), and weather affects regional spreads:

$$\text{Basis}_{\text{location}} = P_{\text{location}} - P_{\text{Henry Hub}}$$

**Key Pricing Points:**

| Location | Region | Winter Basis Behavior |
|----------|--------|----------------------|
| Henry Hub | Louisiana (benchmark) | Reference point (\$0) |
| Chicago Citygate | Midwest | +\$0.10-0.50 in cold |
| Algonquin Citygate | New England | **+\$1-20 in extreme cold** |
| SoCal Citygate | California | +\$0.50-2.00 (pipeline constraints) |
| AECO | Alberta, Canada | -\$0.50-1.50 (stranded supply) |

### 5.2 The New England Problem

New England demonstrates extreme weather sensitivity:

**Structural Issues:**

1. Limited pipeline capacity into region
2. High heating demand (cold climate)
3. Competition with LNG exports
4. No storage facilities in region

**Result:** Algonquin basis can spike from \$0.50 to \$20+ during cold snaps.

**Example: January 2018 Cold Snap**

- Henry Hub: \$3.00/MMBtu
- Algonquin: \$35.00/MMBtu
- Basis blow-out: +\$32.00

This creates massive hedging challenges for New England utilities.

### 5.3 Weather-Weighted Demand Centers

Population-weighted HDDs account for where people live:

$$\text{PWHDD} = \sum_{i} w_i \cdot \text{HDD}_i$$

where $w_i$ is the population weight for region $i$.

Major demand centers:

| Region | Population Weight | HDD Sensitivity |
|--------|-------------------|-----------------|
| Northeast | ~25% | High (cold winters) |
| Midwest | ~20% | Very High (extreme cold) |
| South | ~30% | Moderate (mild winters, but large population) |
| West | ~25% | Low (mild climate) |

---

## 6. Forecasting and Trading Applications

### 6.1 Weather Data Sources

**Primary Forecast Models:**

| Model | Provider | Strengths |
|-------|----------|-----------|
| GFS | NOAA (U.S.) | Free, frequent updates |
| ECMWF | European Centre | Most accurate 7-15 day |
| CFS | NOAA | Seasonal outlooks |
| Private (WSI, DTN) | Commercial | Proprietary blends |

**Forecast Horizons:**

| Horizon | Accuracy | Trading Use |
|---------|----------|-------------|
| 1-3 days | High (90%+) | Spot/prompt trading |
| 4-7 days | Moderate (70-80%) | Weekly positioning |
| 8-14 days | Low-Moderate (50-70%) | Calendar spreads |
| 15-30 days | Low (skill drops rapidly) | Option strategies |
| Seasonal | Climatology-based | Strategic hedging |

### 6.2 Trading the Weather

**Strategy 1: HDD Surprise Trading**

Trade based on forecast changes rather than actual weather:

$$\text{Signal} = \text{HDD}_{\text{new forecast}} - \text{HDD}_{\text{old forecast}}$$

If the 7-day HDD forecast increases by 20 HDDs → bullish signal.

**Strategy 2: Storage Trajectory**

Project end-of-season storage based on weather forecasts:

$$S_{\text{end}} = S_{\text{current}} - \sum_{t=\text{now}}^{\text{March}} W_t(\text{HDD}_t)$$

where $W_t$ is the weekly withdrawal as a function of HDDs.

If projected storage falls below 1,500 Bcf → strong bullish signal.

**Strategy 3: Volatility Trading**

Sell elevated winter volatility and hedge with weather derivatives:

- Sell January straddles
- Buy HDD call options (CME weather derivatives) as catastrophe hedge

### 6.3 Weather Derivatives

CME offers HDD/CDD futures and options:

$$\text{HDD Index Payout} = \$20 \times \text{Cumulative Monthly HDD}$$

**Example:**

- January HDD futures settle at 950 HDDs
- Contract value: 950 × \$20 = \$19,000

These allow pure weather exposure without commodity basis risk.

---

## 7. Python Implementation

### 7.1 HDD/CDD Calculator

```python
import numpy as np
import pandas as pd

def calculate_hdd(temp_avg: pd.Series, base: float = 65.0) -> pd.Series:
    """
    Calculate Heating Degree Days.
    
    Parameters
    ----------
    temp_avg : pd.Series
        Average daily temperature (Fahrenheit)
    base : float
        Base temperature (default 65°F)
        
    Returns
    -------
    pd.Series
        Heating Degree Days
    """
    return np.maximum(base - temp_avg, 0)


def calculate_cdd(temp_avg: pd.Series, base: float = 65.0) -> pd.Series:
    """
    Calculate Cooling Degree Days.
    
    Parameters
    ----------
    temp_avg : pd.Series
        Average daily temperature (Fahrenheit)
    base : float
        Base temperature (default 65°F)
        
    Returns
    -------
    pd.Series
        Cooling Degree Days
    """
    return np.maximum(temp_avg - base, 0)


def population_weighted_hdd(regional_temps: pd.DataFrame, 
                            weights: dict) -> pd.Series:
    """
    Calculate population-weighted HDD.
    
    Parameters
    ----------
    regional_temps : pd.DataFrame
        Columns are regions, values are average temps
    weights : dict
        Population weights by region (should sum to 1)
        
    Returns
    -------
    pd.Series
        Population-weighted HDD
    """
    pwhdd = pd.Series(0.0, index=regional_temps.index)
    
    for region, weight in weights.items():
        if region in regional_temps.columns:
            regional_hdd = calculate_hdd(regional_temps[region])
            pwhdd += weight * regional_hdd
    
    return pwhdd
```

### 7.2 Demand Model

```python
def estimate_ng_demand(hdd: pd.Series, 
                       cdd: pd.Series,
                       base_demand: float = 60.0,
                       hdd_sensitivity: float = 3.5,
                       cdd_sensitivity: float = 2.0) -> pd.Series:
    """
    Estimate daily natural gas demand.
    
    Parameters
    ----------
    hdd : pd.Series
        Heating Degree Days
    cdd : pd.Series
        Cooling Degree Days
    base_demand : float
        Base industrial/commercial demand (Bcf/day)
    hdd_sensitivity : float
        Bcf per HDD
    cdd_sensitivity : float
        Bcf per CDD
        
    Returns
    -------
    pd.Series
        Estimated demand (Bcf/day)
    """
    return base_demand + hdd_sensitivity * hdd + cdd_sensitivity * cdd


def project_storage(current_storage: float,
                    production: float,
                    demand: pd.Series,
                    start_date: str = None) -> pd.DataFrame:
    """
    Project storage trajectory based on demand forecast.
    
    Parameters
    ----------
    current_storage : float
        Current storage level (Bcf)
    production : float
        Daily production (Bcf/day), assumed constant
    demand : pd.Series
        Daily demand forecast (Bcf/day)
        
    Returns
    -------
    pd.DataFrame
        Projected storage levels
    """
    storage = [current_storage]
    
    for d in demand:
        net_change = production - d
        new_storage = max(storage[-1] + net_change, 0)
        storage.append(new_storage)
    
    dates = demand.index.tolist() if hasattr(demand, 'index') else range(len(demand))
    
    return pd.DataFrame({
        'date': list(dates) + [None],
        'storage': storage,
        'demand': list(demand) + [None],
        'net_change': [None] + [production - d for d in demand]
    })
```

### 7.3 Weather-Price Regression

```python
from scipy import stats

def weather_price_regression(price_changes: pd.Series,
                             hdd_surprises: pd.Series,
                             storage_level: pd.Series = None) -> dict:
    """
    Regress price changes on weather surprises.
    
    Parameters
    ----------
    price_changes : pd.Series
        Daily price changes
    hdd_surprises : pd.Series
        Actual HDD - Forecast HDD
    storage_level : pd.Series, optional
        Storage levels for interaction term
        
    Returns
    -------
    dict
        Regression results
    """
    # Align series
    df = pd.DataFrame({
        'price_change': price_changes,
        'hdd_surprise': hdd_surprises
    }).dropna()
    
    # Basic regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df['hdd_surprise'], df['price_change']
    )
    
    results = {
        'beta': slope,
        'alpha': intercept,
        'r_squared': r_value ** 2,
        'p_value': p_value,
        'std_err': std_err,
        'interpretation': f"${slope:.4f}/MMBtu per unexpected HDD"
    }
    
    # Storage interaction if provided
    if storage_level is not None:
        df['storage'] = storage_level
        df['low_storage'] = (df['storage'] < df['storage'].median()).astype(int)
        df['interaction'] = df['hdd_surprise'] * df['low_storage']
        
        # Simple interaction estimate
        low_storage_mask = df['low_storage'] == 1
        high_storage_mask = df['low_storage'] == 0
        
        if low_storage_mask.sum() > 10 and high_storage_mask.sum() > 10:
            beta_low = stats.linregress(
                df.loc[low_storage_mask, 'hdd_surprise'],
                df.loc[low_storage_mask, 'price_change']
            )[0]
            beta_high = stats.linregress(
                df.loc[high_storage_mask, 'hdd_surprise'],
                df.loc[high_storage_mask, 'price_change']
            )[0]
            
            results['beta_low_storage'] = beta_low
            results['beta_high_storage'] = beta_high
            results['storage_amplification'] = beta_low / beta_high if beta_high != 0 else None
    
    return results
```

### 7.4 Seasonal Volatility Analysis

```python
def seasonal_volatility(prices: pd.Series, 
                        window: int = 21) -> pd.DataFrame:
    """
    Calculate seasonal volatility patterns.
    
    Parameters
    ----------
    prices : pd.Series
        Price series with datetime index
    window : int
        Rolling window for volatility calculation
        
    Returns
    -------
    pd.DataFrame
        Monthly volatility statistics
    """
    returns = prices.pct_change().dropna()
    rolling_vol = returns.rolling(window).std() * np.sqrt(252)
    
    # Extract month
    monthly_vol = pd.DataFrame({
        'volatility': rolling_vol,
        'month': rolling_vol.index.month
    })
    
    # Aggregate by month
    seasonal = monthly_vol.groupby('month')['volatility'].agg([
        'mean', 'std', 'min', 'max'
    ])
    
    seasonal.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Add winter premium calculation
    winter_vol = seasonal.loc[['Jan', 'Feb', 'Dec'], 'mean'].mean()
    summer_vol = seasonal.loc[['Jun', 'Jul', 'Aug'], 'mean'].mean()
    
    return {
        'seasonal_stats': seasonal,
        'winter_avg_vol': winter_vol,
        'summer_avg_vol': summer_vol,
        'winter_premium': winter_vol / summer_vol
    }
```

### 7.5 Storage Model

```python
class NGStorageModel:
    """
    Natural gas storage modeling and projection.
    """
    
    def __init__(self, 
                 max_capacity: float = 4100,
                 min_operating: float = 300,
                 max_injection_rate: float = 100,
                 max_withdrawal_rate: float = 150):
        """
        Initialize storage model.
        
        Parameters
        ----------
        max_capacity : float
            Maximum storage capacity (Bcf)
        min_operating : float
            Minimum operating level (Bcf)
        max_injection_rate : float
            Maximum daily injection (Bcf/day)
        max_withdrawal_rate : float
            Maximum daily withdrawal (Bcf/day)
        """
        self.max_capacity = max_capacity
        self.min_operating = min_operating
        self.max_injection_rate = max_injection_rate
        self.max_withdrawal_rate = max_withdrawal_rate
        
    def weeks_of_supply(self, 
                        current_storage: float,
                        avg_weekly_demand: float) -> float:
        """Calculate weeks of supply remaining."""
        usable_storage = current_storage - self.min_operating
        return usable_storage / avg_weekly_demand if avg_weekly_demand > 0 else float('inf')
    
    def price_sensitivity_factor(self, current_storage: float) -> float:
        """
        Estimate price sensitivity based on storage level.
        
        Returns multiplier for weather-price relationship.
        """
        # Normalize storage level
        fill_pct = current_storage / self.max_capacity
        
        if fill_pct > 0.85:
            return 0.5  # High storage, muted response
        elif fill_pct > 0.60:
            return 1.0  # Normal response
        elif fill_pct > 0.40:
            return 1.5  # Elevated sensitivity
        elif fill_pct > 0.25:
            return 2.5  # High sensitivity
        else:
            return 4.0  # Extreme sensitivity, panic regime
    
    def end_of_season_projection(self,
                                 current_storage: float,
                                 current_date: pd.Timestamp,
                                 hdd_forecast: pd.Series,
                                 production: float = 100,
                                 hdd_sensitivity: float = 3.5,
                                 base_demand: float = 60) -> dict:
        """
        Project end-of-winter storage level.
        
        Parameters
        ----------
        current_storage : float
            Current storage (Bcf)
        current_date : pd.Timestamp
            Current date
        hdd_forecast : pd.Series
            Forecasted daily HDDs through end of March
        production : float
            Daily production (Bcf/day)
        hdd_sensitivity : float
            Bcf per HDD
        base_demand : float
            Base demand (Bcf/day)
            
        Returns
        -------
        dict
            Projection results
        """
        storage = current_storage
        trajectory = [(current_date, storage)]
        
        for date, hdd in hdd_forecast.items():
            demand = base_demand + hdd_sensitivity * hdd
            net_change = production - demand
            
            # Apply withdrawal constraint
            if net_change < -self.max_withdrawal_rate:
                net_change = -self.max_withdrawal_rate
            
            storage = max(storage + net_change, self.min_operating)
            trajectory.append((date, storage))
        
        # Find minimum storage point
        min_storage = min(s for _, s in trajectory)
        min_date = [d for d, s in trajectory if s == min_storage][0]
        
        return {
            'end_storage': storage,
            'min_storage': min_storage,
            'min_storage_date': min_date,
            'trajectory': pd.DataFrame(trajectory, columns=['date', 'storage']),
            'risk_level': 'CRITICAL' if min_storage < 1500 else 
                         'ELEVATED' if min_storage < 2000 else 'NORMAL'
        }
```

---

## 8. Case Study: The 2014 Polar Vortex

!!! example "Historical Event Analysis"
    The January 2014 Polar Vortex provides a textbook example of weather-driven price dynamics in natural gas markets.

### 8.1 The Setup

**Pre-Event Conditions (December 2013):**

- Storage: 2,823 Bcf (near 5-year average)
- Henry Hub: ~\$4.20/MMBtu
- Weather outlook: Normal winter expected

### 8.2 The Event

**January 6-8, 2014:**

- Arctic air mass descended across U.S.
- Temperature departures: 20-30°F below normal
- HDDs: 40-50% above normal for the week

**Market Response:**

| Date | Henry Hub | Change | Storage Draw |
|------|-----------|--------|--------------|
| Jan 3 | \$4.23 | — | — |
| Jan 7 | \$4.52 | +7% | — |
| Jan 10 | \$5.17 | +22% | 287 Bcf (record) |
| Jan 21 | \$5.45 | +29% | — |
| Feb 19 | \$6.15 | +45% | Another polar vortex |

### 8.3 Lessons Learned

1. **Storage velocity matters:** The record 287 Bcf weekly draw raised fears of depletion
2. **Non-linear response:** Price rose faster than linear HDD models predicted
3. **Regional blowouts:** Algonquin basis hit \$70+/MMBtu
4. **Persistence:** Cold weather extended into February, compounding effects

### 8.4 Quantitative Analysis

**HDD Analysis:**

```
Week of Jan 6-12:
  Normal HDD: 210
  Actual HDD: 320
  Surprise: +110 HDDs (52% above normal)
  
Price Response:
  Expected (linear model): +$0.33 (at $0.003/HDD)
  Actual: +$0.94
  Amplification factor: 2.8x
```

**Storage Analysis:**

```
Pre-event trajectory: End-Mar storage ~1,800 Bcf
Post-event trajectory: End-Mar storage ~800 Bcf (critical!)
Revision magnitude: -1,000 Bcf
```

---

## 9. Summary

Natural gas is uniquely weather-sensitive due to the combination of inelastic heating demand, limited storage relative to consumption, pipeline constraints, and slow supply response. This creates a market where temperature forecasts drive price movements more directly than in any other major commodity.

!!! success "Key Takeaways"
    **Why Natural Gas is Weather-Sensitive:**
    
    1. ~60% of demand is heating/cooling related
    2. Demand elasticity near zero in short-term
    3. Storage provides only 40-50 days of winter supply
    4. Pipeline constraints create regional bottlenecks
    5. Production cannot respond quickly to demand spikes
    
    **Trading Implications:**
    
    - Monitor HDD/CDD forecasts for 1-14 day horizon
    - Track storage levels and weeks-of-supply metrics
    - Expect non-linear price responses during extreme weather
    - Winter volatility premium is structural, not anomalous
    - Regional basis can blow out during cold snaps

**The Fundamental Equation:**

$$\text{NG Price Sensitivity} = f\left(\frac{\text{Weather Severity}}{\text{Storage Buffer}}\right)$$

When storage is low and weather turns extreme, natural gas becomes the most volatile major commodity in the world—creating both significant risks for consumers and opportunities for informed traders.

---

## References

1. U.S. Energy Information Administration. (2024). *Natural Gas Weekly Update*. [https://www.eia.gov/naturalgas/weekly/](https://www.eia.gov/naturalgas/weekly/)

2. Considine, T. J. (2000). The Impacts of Weather Variations on Energy Demand and Carbon Emissions. *Resource and Energy Economics*, 22(4), 295-314.

3. Nick, S., & Thoenes, S. (2014). What Drives Natural Gas Prices? A Structural VAR Approach. *Energy Economics*, 45, 517-527.

4. CME Group. (2024). *Henry Hub Natural Gas Futures Contract Specifications*. [https://www.cmegroup.com/](https://www.cmegroup.com/)

5. Mu, X. (2007). Weather, Storage, and Natural Gas Price Dynamics: Fundamentals and Volatility. *Energy Economics*, 29(1), 46-63.

6. Brown, S. P., & Yücel, M. K. (2008). What Drives Natural Gas Prices? *The Energy Journal*, 29(2), 45-60.
