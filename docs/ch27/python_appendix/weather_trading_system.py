"""
Weather-Based Commodity Trading System
======================================

This module provides a complete implementation for weather-based
natural gas trading strategies.

Author: Quant Finance with Python
Date: January 2026
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Tuple
from enum import Enum
import warnings

# ============================================================
# SECTION 1: DATA STRUCTURES
# ============================================================

class TradeDirection(Enum):
    LONG = 1
    SHORT = -1
    FLAT = 0

@dataclass
class WeatherForecast:
    """Weather forecast data structure"""
    forecast_date: datetime
    valid_date: datetime
    hdd_forecast: float
    hdd_normal: float
    hdd_std: float
    model_source: str
    confidence: float = 0.5
    
    @property
    def z_score(self) -> float:
        """Calculate HDD z-score"""
        if self.hdd_std == 0:
            return 0
        return (self.hdd_forecast - self.hdd_normal) / self.hdd_std
    
    @property
    def is_extreme(self) -> bool:
        """Check if forecast is extreme (>2 sigma)"""
        return abs(self.z_score) > 2.0

@dataclass
class WeatherEvent:
    """Detected weather event"""
    event_type: str
    detection_date: datetime
    expected_start: datetime
    expected_duration: int
    severity: float  # 0-1
    confidence: float  # 0-1
    affected_regions: List[str] = field(default_factory=list)
    
    @property
    def days_until_start(self) -> int:
        return (self.expected_start - datetime.now()).days

@dataclass
class Position:
    """Trading position"""
    commodity: str
    direction: TradeDirection
    quantity: int
    entry_price: float
    entry_date: datetime
    stop_loss: float
    take_profit: float
    confidence: float
    event_reference: Optional[str] = None
    
    @property
    def notional_value(self) -> float:
        """Calculate notional value (assuming NG contract = 10000 MMBtu)"""
        return self.quantity * self.entry_price * 10000
    
    def calculate_pnl(self, current_price: float) -> float:
        """Calculate current P&L"""
        price_change = current_price - self.entry_price
        return price_change * self.quantity * self.direction.value * 10000

@dataclass
class TradeSignal:
    """Trading signal from strategy"""
    timestamp: datetime
    direction: TradeDirection
    commodity: str
    strength: float  # 0-1
    confidence: float  # 0-1
    reason: str
    target_position: int
    stop_loss_pct: float
    take_profit_pct: float

# ============================================================
# SECTION 2: WEATHER DATA PROCESSING
# ============================================================

class WeatherDataProcessor:
    """Process and analyze weather data for trading"""
    
    def __init__(self, hdd_sensitivity: float = 3.5):
        """
        Parameters:
        -----------
        hdd_sensitivity : float
            Bcf of natural gas demand per HDD
        """
        self.hdd_sensitivity = hdd_sensitivity
        
    def calculate_population_weighted_hdd(
        self,
        regional_temps: Dict[str, float],
        regional_weights: Dict[str, float],
        base_temp: float = 65.0
    ) -> float:
        """
        Calculate population-weighted heating degree days
        
        Parameters:
        -----------
        regional_temps : dict
            Average temperatures by region
        regional_weights : dict
            Population weights by region (should sum to 1)
        base_temp : float
            Base temperature for HDD calculation (default 65°F)
        
        Returns:
        --------
        pw_hdd : float
            Population-weighted HDD
        """
        pw_hdd = 0.0
        for region, temp in regional_temps.items():
            weight = regional_weights.get(region, 0)
            hdd = max(base_temp - temp, 0)
            pw_hdd += weight * hdd
        return pw_hdd
    
    def estimate_demand_impact(
        self,
        hdd_forecast: float,
        hdd_normal: float
    ) -> Dict[str, float]:
        """
        Estimate natural gas demand impact from HDD deviation
        
        Returns:
        --------
        impact : dict
            Demand impact estimates
        """
        hdd_deviation = hdd_forecast - hdd_normal
        demand_change_bcf = hdd_deviation * self.hdd_sensitivity
        
        # Estimate price impact (simplified)
        # Typically $0.02-0.05 per 10 Bcf demand change
        price_impact_pct = demand_change_bcf * 0.003
        
        return {
            'hdd_deviation': hdd_deviation,
            'demand_change_bcf': demand_change_bcf,
            'estimated_price_impact_pct': price_impact_pct
        }
    
    def calculate_model_agreement(
        self,
        forecasts: List[WeatherForecast]
    ) -> float:
        """
        Calculate agreement between multiple weather models
        
        Parameters:
        -----------
        forecasts : list
            List of forecasts from different models
        
        Returns:
        --------
        agreement : float
            Agreement score [0, 1]
        """
        if len(forecasts) < 2:
            return 0.5
        
        hdds = [f.hdd_forecast for f in forecasts]
        spread = max(hdds) - min(hdds)
        mean_hdd = np.mean(hdds)
        
        # Normalize spread by mean (coefficient of variation)
        if mean_hdd == 0:
            return 0.5
        
        cv = spread / mean_hdd
        
        # Convert to agreement score (lower spread = higher agreement)
        agreement = max(0, 1 - cv * 2)
        
        return agreement

# ============================================================
# SECTION 3: EVENT DETECTION
# ============================================================

class WeatherEventDetector:
    """Detect tradeable weather events"""
    
    def __init__(self, config: Optional[Dict] = None):
        config = config or {}
        self.cold_threshold = config.get('cold_threshold', -2.0)
        self.heat_threshold = config.get('heat_threshold', 2.0)
        self.min_duration = config.get('min_duration', 3)
        self.min_confidence = config.get('min_confidence', 0.5)
    
    def detect_cold_event(
        self,
        forecasts: List[WeatherForecast]
    ) -> Optional[WeatherEvent]:
        """
        Detect significant cold weather event from forecast series
        
        Parameters:
        -----------
        forecasts : list
            Chronological list of daily forecasts
        
        Returns:
        --------
        event : WeatherEvent or None
        """
        # Check for consecutive extreme cold days
        cold_streak = 0
        max_severity = 0
        start_idx = None
        
        for i, forecast in enumerate(forecasts):
            if forecast.z_score < self.cold_threshold:
                if cold_streak == 0:
                    start_idx = i
                cold_streak += 1
                max_severity = max(max_severity, abs(forecast.z_score))
            else:
                if cold_streak >= self.min_duration:
                    break
                cold_streak = 0
                start_idx = None
        
        if cold_streak >= self.min_duration and start_idx is not None:
            # Calculate average confidence
            avg_confidence = np.mean([f.confidence for f in forecasts[start_idx:start_idx+cold_streak]])
            
            if avg_confidence >= self.min_confidence:
                return WeatherEvent(
                    event_type='COLD_OUTBREAK',
                    detection_date=datetime.now(),
                    expected_start=forecasts[start_idx].valid_date,
                    expected_duration=cold_streak,
                    severity=min(max_severity / 4, 1.0),  # Normalize to 0-1
                    confidence=avg_confidence,
                    affected_regions=['US_TOTAL']  # Simplified
                )
        
        return None
    
    def detect_events(
        self,
        forecasts: List[WeatherForecast]
    ) -> List[WeatherEvent]:
        """Detect all types of weather events"""
        events = []
        
        cold_event = self.detect_cold_event(forecasts)
        if cold_event:
            events.append(cold_event)
        
        # Add heat event detection, hurricane detection, etc.
        
        return events

# ============================================================
# SECTION 4: TRADING STRATEGIES
# ============================================================

class BaseWeatherStrategy:
    """Base class for weather trading strategies"""
    
    def __init__(self, config: Optional[Dict] = None):
        config = config or {}
        self.max_position = config.get('max_position', 10)
        self.base_stop_pct = config.get('base_stop_pct', 0.05)
        self.base_target_pct = config.get('base_target_pct', 0.10)
    
    def generate_signal(self, *args, **kwargs) -> TradeSignal:
        raise NotImplementedError


class PromptSpreadStrategy(BaseWeatherStrategy):
    """
    Trade prompt month spread based on weather forecasts
    
    Long spread (buy near, sell far) when cold weather expected
    Short spread (sell near, buy far) when warm weather expected
    """
    
    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)
        config = config or {}
        self.hdd_threshold = config.get('hdd_threshold', 1.5)
    
    def generate_signal(
        self,
        forecast: WeatherForecast,
        model_agreement: float,
        current_spread: float
    ) -> TradeSignal:
        """
        Generate spread trading signal
        
        Parameters:
        -----------
        forecast : WeatherForecast
            Current weather forecast
        model_agreement : float
            Model agreement score [0, 1]
        current_spread : float
            Current prompt-deferred spread price
        
        Returns:
        --------
        signal : TradeSignal
        """
        z_score = forecast.z_score
        
        # Determine direction
        if z_score > self.hdd_threshold:
            direction = TradeDirection.LONG
            reason = f"Cold forecast (z={z_score:.2f}), buy spread"
        elif z_score < -self.hdd_threshold:
            direction = TradeDirection.SHORT
            reason = f"Warm forecast (z={z_score:.2f}), sell spread"
        else:
            direction = TradeDirection.FLAT
            reason = f"Neutral forecast (z={z_score:.2f})"
        
        # Calculate strength and position size
        strength = min(abs(z_score) / 3, 1.0) if direction != TradeDirection.FLAT else 0
        confidence = model_agreement * forecast.confidence
        target_position = int(self.max_position * strength * confidence)
        
        return TradeSignal(
            timestamp=datetime.now(),
            direction=direction,
            commodity='NG_SPREAD',
            strength=strength,
            confidence=confidence,
            reason=reason,
            target_position=target_position,
            stop_loss_pct=self.base_stop_pct / confidence if confidence > 0 else self.base_stop_pct,
            take_profit_pct=self.base_target_pct * (1 + strength)
        )


class EventDrivenStrategy(BaseWeatherStrategy):
    """
    Trade outright natural gas based on detected weather events
    """
    
    def generate_signal(
        self,
        event: WeatherEvent,
        current_price: float,
        storage_vs_avg: float
    ) -> TradeSignal:
        """
        Generate trading signal from weather event
        
        Parameters:
        -----------
        event : WeatherEvent
            Detected weather event
        current_price : float
            Current NG price
        storage_vs_avg : float
            Storage level vs 5-year average (%)
        
        Returns:
        --------
        signal : TradeSignal
        """
        # Direction based on event type
        if event.event_type == 'COLD_OUTBREAK':
            direction = TradeDirection.LONG
            reason = f"Cold outbreak detected, severity={event.severity:.2f}"
        elif event.event_type == 'HEAT_WAVE':
            direction = TradeDirection.LONG  # Cooling demand
            reason = f"Heat wave detected, severity={event.severity:.2f}"
        else:
            direction = TradeDirection.FLAT
            reason = "Unknown event type"
        
        # Adjust for storage levels
        storage_factor = 1.0
        if storage_vs_avg < -10:  # Below average storage
            storage_factor = 1.3  # More bullish
        elif storage_vs_avg > 10:  # Above average storage
            storage_factor = 0.7  # Less bullish
        
        # Calculate position
        strength = event.severity * storage_factor
        confidence = event.confidence
        target_position = int(self.max_position * strength * confidence)
        
        # Timing adjustment - reduce size for distant events
        if event.days_until_start > 7:
            target_position = int(target_position * 0.5)
            reason += " (early entry, half size)"
        
        return TradeSignal(
            timestamp=datetime.now(),
            direction=direction,
            commodity='NG',
            strength=strength,
            confidence=confidence,
            reason=reason,
            target_position=target_position,
            stop_loss_pct=self.base_stop_pct,
            take_profit_pct=self.base_target_pct * (1 + event.severity)
        )

# ============================================================
# SECTION 5: RISK MANAGEMENT
# ============================================================

class RiskManager:
    """Portfolio risk management for weather trading"""
    
    def __init__(self, config: Optional[Dict] = None):
        config = config or {}
        self.max_portfolio_risk = config.get('max_portfolio_risk', 0.05)
        self.max_position_risk = config.get('max_position_risk', 0.02)
        self.max_concentration = config.get('max_concentration', 0.30)
        self.vol_adjustment = config.get('vol_adjustment', True)
    
    def calculate_position_size(
        self,
        account_value: float,
        signal: TradeSignal,
        current_vol: float,
        normal_vol: float = 0.60
    ) -> int:
        """
        Calculate risk-adjusted position size
        
        Parameters:
        -----------
        account_value : float
            Total account value
        signal : TradeSignal
            Trading signal
        current_vol : float
            Current annualized volatility
        normal_vol : float
            Normal volatility level
        
        Returns:
        --------
        position_size : int
            Number of contracts
        """
        # Risk budget
        risk_budget = account_value * self.max_position_risk
        
        # Volatility adjustment
        if self.vol_adjustment:
            vol_factor = normal_vol / max(current_vol, 0.3)
            vol_factor = np.clip(vol_factor, 0.5, 1.5)
        else:
            vol_factor = 1.0
        
        # Confidence adjustment
        confidence_factor = signal.confidence
        
        # Calculate position
        adjusted_risk = risk_budget * vol_factor * confidence_factor
        
        # Assume 2-sigma daily move for position sizing
        contract_value = 10000 * 5.0  # Approximate NG contract value
        daily_risk = contract_value * current_vol / np.sqrt(252) * 2
        
        position_size = int(adjusted_risk / daily_risk)
        
        # Cap at signal's target
        position_size = min(position_size, signal.target_position)
        
        return max(1, position_size)
    
    def check_portfolio_limits(
        self,
        positions: List[Position],
        new_signal: TradeSignal,
        account_value: float
    ) -> Tuple[bool, str]:
        """
        Check if new trade would violate portfolio limits
        
        Returns:
        --------
        (approved, reason) : tuple
        """
        # Calculate current exposure
        total_exposure = sum(p.notional_value for p in positions)
        
        # Check concentration
        commodity_exposure = sum(
            p.notional_value for p in positions 
            if p.commodity == new_signal.commodity
        )
        
        if commodity_exposure / account_value > self.max_concentration:
            return False, f"Concentration limit exceeded for {new_signal.commodity}"
        
        # Check total risk
        if total_exposure / account_value > self.max_portfolio_risk * 10:  # Rough notional limit
            return False, "Portfolio exposure limit exceeded"
        
        return True, "Approved"

# ============================================================
# SECTION 6: BACKTESTING
# ============================================================

class WeatherStrategyBacktester:
    """Backtest weather trading strategies"""
    
    def __init__(
        self,
        strategy: BaseWeatherStrategy,
        risk_manager: RiskManager,
        initial_capital: float = 1_000_000
    ):
        self.strategy = strategy
        self.risk_manager = risk_manager
        self.initial_capital = initial_capital
        
    def run_backtest(
        self,
        weather_data: pd.DataFrame,
        price_data: pd.DataFrame,
        start_date: str,
        end_date: str
    ) -> Dict:
        """
        Run backtest over historical period
        
        Parameters:
        -----------
        weather_data : DataFrame
            Historical weather data with HDD columns
        price_data : DataFrame
            Historical price data
        start_date, end_date : str
            Backtest period
        
        Returns:
        --------
        results : dict
            Backtest results and metrics
        """
        # Initialize tracking
        capital = self.initial_capital
        positions = []
        trades = []
        equity_curve = []
        
        # Filter date range
        mask = (price_data.index >= start_date) & (price_data.index <= end_date)
        prices = price_data.loc[mask]
        
        for date in prices.index:
            # Get weather forecast for this date (simulated as actual - lookahead bias noted)
            if date in weather_data.index:
                hdd = weather_data.loc[date, 'hdd']
                hdd_normal = weather_data.loc[date, 'hdd_normal']
                hdd_std = weather_data.loc[date, 'hdd_std']
            else:
                continue
            
            forecast = WeatherForecast(
                forecast_date=date,
                valid_date=date,
                hdd_forecast=hdd,
                hdd_normal=hdd_normal,
                hdd_std=hdd_std,
                model_source='HISTORICAL',
                confidence=0.8  # Assumed
            )
            
            # Generate signal (simplified - would need spread prices for spread strategy)
            if isinstance(self.strategy, EventDrivenStrategy):
                # Detect events
                detector = WeatherEventDetector()
                # Simplified - in practice would use multi-day forecasts
                if forecast.z_score < -2:
                    event = WeatherEvent(
                        event_type='COLD_OUTBREAK',
                        detection_date=date,
                        expected_start=date,
                        expected_duration=3,
                        severity=min(abs(forecast.z_score) / 4, 1.0),
                        confidence=0.7
                    )
                    signal = self.strategy.generate_signal(
                        event, 
                        prices.loc[date, 'close'],
                        weather_data.loc[date, 'storage_vs_avg'] if 'storage_vs_avg' in weather_data.columns else 0
                    )
                else:
                    signal = None
            else:
                signal = self.strategy.generate_signal(
                    forecast,
                    0.7,  # Assumed model agreement
                    0  # Current spread
                )
            
            # Process signal and update positions
            # (Simplified - full implementation would handle entries, exits, stops)
            
            # Track equity
            equity_curve.append({
                'date': date,
                'equity': capital
            })
        
        # Calculate metrics
        equity_df = pd.DataFrame(equity_curve).set_index('date')
        returns = equity_df['equity'].pct_change().dropna()
        
        results = {
            'total_return': (capital - self.initial_capital) / self.initial_capital,
            'sharpe_ratio': returns.mean() / returns.std() * np.sqrt(252) if len(returns) > 0 else 0,
            'max_drawdown': self._calculate_max_drawdown(equity_df['equity']),
            'total_trades': len(trades),
            'equity_curve': equity_df
        }
        
        return results
    
    def _calculate_max_drawdown(self, equity: pd.Series) -> float:
        """Calculate maximum drawdown"""
        peak = equity.expanding().max()
        drawdown = (equity - peak) / peak
        return drawdown.min()

# ============================================================
# SECTION 7: EXAMPLE USAGE
# ============================================================

def example_usage():
    """Demonstrate system usage"""
    
    # 1. Create weather forecast
    forecast = WeatherForecast(
        forecast_date=datetime.now(),
        valid_date=datetime.now() + timedelta(days=5),
        hdd_forecast=45,  # Heavy heating demand
        hdd_normal=30,
        hdd_std=8,
        model_source='GFS',
        confidence=0.75
    )
    
    print(f"Weather Forecast Z-Score: {forecast.z_score:.2f}")
    print(f"Is Extreme: {forecast.is_extreme}")
    
    # 2. Check for events
    forecasts = [forecast] * 5  # Simplified: 5 days of same forecast
    detector = WeatherEventDetector()
    events = detector.detect_events(forecasts)
    
    if events:
        print(f"\nDetected Event: {events[0].event_type}")
        print(f"Severity: {events[0].severity:.2f}")
    
    # 3. Generate trading signal
    strategy = PromptSpreadStrategy({'max_position': 10})
    signal = strategy.generate_signal(forecast, model_agreement=0.8, current_spread=-0.10)
    
    print(f"\nTrading Signal:")
    print(f"Direction: {signal.direction.name}")
    print(f"Target Position: {signal.target_position}")
    print(f"Confidence: {signal.confidence:.2f}")
    print(f"Reason: {signal.reason}")
    
    # 4. Risk-adjusted position sizing
    risk_mgr = RiskManager()
    position_size = risk_mgr.calculate_position_size(
        account_value=500_000,
        signal=signal,
        current_vol=0.80  # Elevated volatility
    )
    
    print(f"\nRisk-Adjusted Position: {position_size} contracts")

if __name__ == "__main__":
    example_usage()
