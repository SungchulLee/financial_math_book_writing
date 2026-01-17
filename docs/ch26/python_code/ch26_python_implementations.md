# Chapter 26: Python Implementations

This appendix provides Python implementations for the key concepts and strategies discussed in Chapter 26: Digital Assets. All code examples use standard libraries (NumPy, Pandas, Matplotlib) with optional exchange API integrations.

---

## 26.P.1 Funding Rate Monitoring and Alerts

### Real-Time Funding Rate Tracker

```python
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time
from typing import Dict, List, Optional

class FundingRateMonitor:
    """
    Monitor funding rates across multiple assets and exchanges.
    Generates alerts when rates exceed configurable thresholds.
    """
    
    def __init__(self, 
                 alert_threshold_high: float = 0.0008,  # 0.08% per 8h = 87.6% annual
                 alert_threshold_low: float = 0.00015,  # 0.015% per 8h = 16.4% annual
                 alert_threshold_negative: float = -0.0005):  # -0.05% per 8h
        """
        Initialize the funding rate monitor.
        
        Parameters
        ----------
        alert_threshold_high : float
            Funding rate above which to generate "elevated" alert
        alert_threshold_low : float
            Funding rate below which basis trades become unattractive
        alert_threshold_negative : float
            Negative funding rate threshold for reversal alert
        """
        self.threshold_high = alert_threshold_high
        self.threshold_low = alert_threshold_low
        self.threshold_negative = alert_threshold_negative
        self.history: Dict[str, pd.DataFrame] = {}
        
    def annualize_funding_rate(self, rate_8h: float) -> float:
        """
        Convert 8-hour funding rate to annualized percentage.
        
        Formula: Annual = Rate_8h × 3 × 365 = Rate_8h × 1095
        
        Parameters
        ----------
        rate_8h : float
            Funding rate per 8-hour period (as decimal, e.g., 0.0003 for 0.03%)
            
        Returns
        -------
        float
            Annualized rate as percentage (e.g., 32.85 for 32.85%)
        """
        return rate_8h * 1095 * 100
    
    def calculate_funding_payment(self, 
                                   position_size_usd: float,
                                   funding_rate: float,
                                   position_side: str = 'short') -> float:
        """
        Calculate expected funding payment for a position.
        
        Parameters
        ----------
        position_size_usd : float
            Notional position size in USD
        funding_rate : float
            Current 8-hour funding rate (decimal)
        position_side : str
            'long' or 'short'
            
        Returns
        -------
        float
            Expected payment (positive = receive, negative = pay)
        """
        payment = position_size_usd * funding_rate
        # Positive funding: longs pay shorts
        if position_side == 'short':
            return payment if funding_rate > 0 else -abs(payment)
        else:
            return -payment if funding_rate > 0 else abs(payment)
    
    def generate_alert(self, 
                       asset: str, 
                       exchange: str,
                       rate: float) -> Optional[Dict]:
        """
        Generate alert based on current funding rate.
        
        Parameters
        ----------
        asset : str
            Asset symbol (e.g., 'BTC', 'ETH')
        exchange : str
            Exchange name
        rate : float
            Current 8-hour funding rate
            
        Returns
        -------
        dict or None
            Alert dictionary if threshold crossed, None otherwise
        """
        annual_rate = self.annualize_funding_rate(rate)
        
        if rate >= self.threshold_high:
            return {
                'timestamp': datetime.utcnow(),
                'asset': asset,
                'exchange': exchange,
                'alert_type': 'HIGH_FUNDING',
                'rate_8h': rate,
                'rate_annual': annual_rate,
                'message': f"⚠️ {asset} funding elevated: {rate*100:.4f}% per 8h ({annual_rate:.1f}% annual)"
            }
        elif rate <= self.threshold_negative:
            return {
                'timestamp': datetime.utcnow(),
                'asset': asset,
                'exchange': exchange,
                'alert_type': 'NEGATIVE_FUNDING',
                'rate_8h': rate,
                'rate_annual': annual_rate,
                'message': f"🔻 {asset} funding negative: {rate*100:.4f}% per 8h ({annual_rate:.1f}% annual)"
            }
        elif 0 < rate <= self.threshold_low:
            return {
                'timestamp': datetime.utcnow(),
                'asset': asset,
                'exchange': exchange,
                'alert_type': 'LOW_FUNDING',
                'rate_8h': rate,
                'rate_annual': annual_rate,
                'message': f"📉 {asset} funding low: {rate*100:.4f}% per 8h ({annual_rate:.1f}% annual) - Consider exit"
            }
        return None
    
    def analyze_funding_history(self, 
                                 rates: List[float],
                                 window_days: int = 7) -> Dict:
        """
        Analyze funding rate history for trend and statistics.
        
        Parameters
        ----------
        rates : list
            Historical 8-hour funding rates (most recent last)
        window_days : int
            Analysis window in days
            
        Returns
        -------
        dict
            Analysis results including mean, std, trend
        """
        # Convert to array (3 funding periods per day)
        periods_needed = window_days * 3
        recent_rates = np.array(rates[-periods_needed:]) if len(rates) >= periods_needed else np.array(rates)
        
        if len(recent_rates) < 3:
            return {'error': 'Insufficient data'}
        
        mean_rate = np.mean(recent_rates)
        std_rate = np.std(recent_rates)
        
        # Simple linear regression for trend
        x = np.arange(len(recent_rates))
        slope = np.polyfit(x, recent_rates, 1)[0]
        
        # Trend interpretation
        if slope > 0.00001:
            trend = 'RISING'
        elif slope < -0.00001:
            trend = 'FALLING'
        else:
            trend = 'STABLE'
        
        return {
            'mean_8h': mean_rate,
            'mean_annual': self.annualize_funding_rate(mean_rate),
            'std_8h': std_rate,
            'min_8h': np.min(recent_rates),
            'max_8h': np.max(recent_rates),
            'current': recent_rates[-1],
            'trend': trend,
            'slope_per_period': slope,
            'periods_analyzed': len(recent_rates),
            'days_analyzed': len(recent_rates) / 3
        }


# Example usage with simulated data
def demo_funding_monitor():
    """Demonstrate funding rate monitor functionality."""
    
    monitor = FundingRateMonitor()
    
    # Simulated funding rates (8-hour periods over 7 days)
    np.random.seed(42)
    btc_rates = 0.0002 + np.random.randn(21) * 0.0001  # Mean 0.02%, std 0.01%
    eth_rates = 0.0004 + np.random.randn(21) * 0.00015  # Higher mean for ETH
    
    # Add some extreme values
    btc_rates[15] = 0.0012  # Spike to 0.12%
    eth_rates[18] = -0.0003  # Dip to -0.03%
    
    print("=" * 60)
    print("FUNDING RATE MONITOR DEMO")
    print("=" * 60)
    
    # Analyze BTC
    btc_analysis = monitor.analyze_funding_history(btc_rates.tolist())
    print(f"\nBTC Funding Analysis ({btc_analysis['days_analyzed']:.0f} days):")
    print(f"  Mean: {btc_analysis['mean_8h']*100:.4f}% per 8h ({btc_analysis['mean_annual']:.1f}% annual)")
    print(f"  Range: [{btc_analysis['min_8h']*100:.4f}%, {btc_analysis['max_8h']*100:.4f}%]")
    print(f"  Trend: {btc_analysis['trend']}")
    
    # Check current alert
    current_btc_rate = btc_rates[-1]
    alert = monitor.generate_alert('BTC', 'Binance', current_btc_rate)
    if alert:
        print(f"\n  Alert: {alert['message']}")
    
    # Calculate funding payment for basis trade
    position_size = 430000  # $430K (10 BTC at $43K)
    payment_per_8h = monitor.calculate_funding_payment(position_size, current_btc_rate, 'short')
    print(f"\n  Position: ${position_size:,.0f} short perpetual")
    print(f"  Funding per 8h: ${payment_per_8h:,.2f}")
    print(f"  Funding per day: ${payment_per_8h * 3:,.2f}")
    print(f"  Funding per month: ${payment_per_8h * 3 * 30:,.2f}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    demo_funding_monitor()
```

---

## 26.P.2 Liquidation Price Calculator

### Multi-Exchange Liquidation Calculator

```python
import numpy as np
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class MarginMode(Enum):
    ISOLATED = "isolated"
    CROSS = "cross"

class PositionSide(Enum):
    LONG = "long"
    SHORT = "short"

@dataclass
class ExchangeParams:
    """Exchange-specific margin parameters."""
    name: str
    maintenance_margin_rate: float  # As decimal (e.g., 0.005 for 0.5%)
    taker_fee: float  # As decimal (e.g., 0.0004 for 0.04%)
    maker_fee: float
    max_leverage: int

# Common exchange parameters (as of 2024)
EXCHANGE_PARAMS = {
    'binance': ExchangeParams('Binance', 0.004, 0.0004, 0.0002, 125),
    'bybit': ExchangeParams('Bybit', 0.005, 0.0006, 0.0001, 100),
    'okx': ExchangeParams('OKX', 0.004, 0.0005, 0.0002, 100),
    'dydx': ExchangeParams('dYdX', 0.03, 0.0005, 0.0001, 20),  # Higher MM for DeFi
}


class LiquidationCalculator:
    """
    Calculate liquidation prices for perpetual futures positions.
    
    Supports both isolated and cross margin modes across multiple exchanges.
    """
    
    def __init__(self, exchange: str = 'binance'):
        """
        Initialize calculator with exchange parameters.
        
        Parameters
        ----------
        exchange : str
            Exchange name (binance, bybit, okx, dydx)
        """
        self.params = EXCHANGE_PARAMS.get(exchange.lower(), EXCHANGE_PARAMS['binance'])
    
    def calculate_liquidation_price(self,
                                     entry_price: float,
                                     leverage: float,
                                     side: PositionSide,
                                     margin_mode: MarginMode = MarginMode.ISOLATED,
                                     wallet_balance: Optional[float] = None,
                                     position_size: Optional[float] = None) -> dict:
        """
        Calculate liquidation price for a position.
        
        For isolated margin (simplified formula):
        
        Long: P_liq = P_entry × (1 - 1/Leverage + MM_rate + Fee_rate)
        Short: P_liq = P_entry × (1 + 1/Leverage - MM_rate - Fee_rate)
        
        Parameters
        ----------
        entry_price : float
            Position entry price
        leverage : float
            Leverage used (e.g., 10 for 10×)
        side : PositionSide
            LONG or SHORT
        margin_mode : MarginMode
            ISOLATED or CROSS
        wallet_balance : float, optional
            Total wallet balance (required for cross margin)
        position_size : float, optional
            Position size in base currency (required for cross margin)
            
        Returns
        -------
        dict
            Liquidation details including price, distance, and risk metrics
        """
        mm_rate = self.params.maintenance_margin_rate
        fee_rate = self.params.taker_fee
        
        if margin_mode == MarginMode.ISOLATED:
            if side == PositionSide.LONG:
                liq_price = entry_price * (1 - 1/leverage + mm_rate + fee_rate)
            else:  # SHORT
                liq_price = entry_price * (1 + 1/leverage - mm_rate - fee_rate)
        else:
            # Cross margin - more complex, uses account equity
            if wallet_balance is None or position_size is None:
                raise ValueError("Cross margin requires wallet_balance and position_size")
            
            # Simplified cross margin calculation
            notional = entry_price * position_size
            initial_margin = notional / leverage
            maintenance_margin = notional * mm_rate
            
            # Distance to liquidation in price terms
            if side == PositionSide.LONG:
                max_loss = wallet_balance - maintenance_margin
                price_distance = max_loss / position_size
                liq_price = entry_price - price_distance
            else:
                max_loss = wallet_balance - maintenance_margin
                price_distance = max_loss / position_size
                liq_price = entry_price + price_distance
        
        # Calculate distance percentage
        distance_pct = abs(liq_price - entry_price) / entry_price * 100
        
        # Calculate what move % causes liquidation
        move_to_liq = (liq_price - entry_price) / entry_price * 100
        
        # Risk assessment
        if distance_pct >= 30:
            risk_level = 'LOW'
        elif distance_pct >= 15:
            risk_level = 'MODERATE'
        elif distance_pct >= 10:
            risk_level = 'ELEVATED'
        else:
            risk_level = 'HIGH'
        
        return {
            'entry_price': entry_price,
            'liquidation_price': round(liq_price, 2),
            'leverage': leverage,
            'side': side.value,
            'margin_mode': margin_mode.value,
            'distance_pct': round(distance_pct, 2),
            'move_to_liquidation': round(move_to_liq, 2),
            'maintenance_margin_rate': mm_rate,
            'exchange': self.params.name,
            'risk_level': risk_level
        }
    
    def calculate_safe_leverage(self,
                                 target_distance_pct: float = 30.0,
                                 side: PositionSide = PositionSide.LONG) -> float:
        """
        Calculate maximum leverage for a target liquidation distance.
        
        Formula (rearranged from liquidation formula):
        Leverage = 1 / (distance_pct/100 + MM_rate + Fee_rate)
        
        Parameters
        ----------
        target_distance_pct : float
            Desired distance to liquidation (as percentage)
        side : PositionSide
            LONG or SHORT
            
        Returns
        -------
        float
            Maximum recommended leverage
        """
        mm_rate = self.params.maintenance_margin_rate
        fee_rate = self.params.taker_fee
        
        distance = target_distance_pct / 100
        
        # Solve: distance = 1/L - MM - Fee
        # L = 1 / (distance + MM + Fee)
        leverage = 1 / (distance + mm_rate + fee_rate)
        
        # Cap at exchange max
        leverage = min(leverage, self.params.max_leverage)
        
        return round(leverage, 2)
    
    def position_size_for_risk(self,
                                capital: float,
                                entry_price: float,
                                stop_loss_pct: float,
                                max_loss_pct: float = 2.0) -> dict:
        """
        Calculate position size based on risk tolerance.
        
        Parameters
        ----------
        capital : float
            Total trading capital
        entry_price : float
            Planned entry price
        stop_loss_pct : float
            Stop loss distance as percentage
        max_loss_pct : float
            Maximum loss per trade as percentage of capital
            
        Returns
        -------
        dict
            Position sizing recommendation
        """
        max_loss_usd = capital * (max_loss_pct / 100)
        
        # Position size = Max Loss / (Stop Loss Distance)
        position_size_usd = max_loss_usd / (stop_loss_pct / 100)
        position_size_base = position_size_usd / entry_price
        
        # Calculate implied leverage
        implied_leverage = position_size_usd / capital
        
        return {
            'capital': capital,
            'max_loss_pct': max_loss_pct,
            'max_loss_usd': max_loss_usd,
            'stop_loss_pct': stop_loss_pct,
            'position_size_usd': round(position_size_usd, 2),
            'position_size_base': round(position_size_base, 6),
            'implied_leverage': round(implied_leverage, 2),
            'entry_price': entry_price
        }


def demo_liquidation_calculator():
    """Demonstrate liquidation calculator functionality."""
    
    print("=" * 60)
    print("LIQUIDATION PRICE CALCULATOR DEMO")
    print("=" * 60)
    
    calc = LiquidationCalculator('binance')
    
    # Example 1: Long position with 10× leverage
    print("\n--- Example 1: BTC Long, 10× Leverage ---")
    result = calc.calculate_liquidation_price(
        entry_price=43000,
        leverage=10,
        side=PositionSide.LONG
    )
    print(f"Entry: ${result['entry_price']:,.0f}")
    print(f"Liquidation: ${result['liquidation_price']:,.0f}")
    print(f"Distance: {result['distance_pct']:.2f}%")
    print(f"Risk Level: {result['risk_level']}")
    
    # Example 2: Short position with 20× leverage
    print("\n--- Example 2: ETH Short, 20× Leverage ---")
    calc_bybit = LiquidationCalculator('bybit')
    result = calc_bybit.calculate_liquidation_price(
        entry_price=2200,
        leverage=20,
        side=PositionSide.SHORT
    )
    print(f"Entry: ${result['entry_price']:,.0f}")
    print(f"Liquidation: ${result['liquidation_price']:,.0f}")
    print(f"Distance: {result['distance_pct']:.2f}%")
    print(f"Risk Level: {result['risk_level']}")
    
    # Example 3: Calculate safe leverage
    print("\n--- Example 3: Safe Leverage Calculation ---")
    safe_lev = calc.calculate_safe_leverage(target_distance_pct=30)
    print(f"For 30% distance to liquidation:")
    print(f"Maximum recommended leverage: {safe_lev}×")
    
    # Example 4: Position sizing
    print("\n--- Example 4: Position Sizing for 2% Risk ---")
    sizing = calc.position_size_for_risk(
        capital=100000,
        entry_price=43000,
        stop_loss_pct=5,
        max_loss_pct=2
    )
    print(f"Capital: ${sizing['capital']:,.0f}")
    print(f"Max Loss (2%): ${sizing['max_loss_usd']:,.0f}")
    print(f"Stop Loss: {sizing['stop_loss_pct']}%")
    print(f"Position Size: ${sizing['position_size_usd']:,.0f} ({sizing['position_size_base']:.4f} BTC)")
    print(f"Implied Leverage: {sizing['implied_leverage']}×")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo_liquidation_calculator()
```

---

## 26.P.3 Volatility Regime Classifier

### Real-Time Regime Detection System

```python
import numpy as np
import pandas as pd
from enum import Enum
from typing import List, Tuple, Optional
from dataclasses import dataclass

class VolRegime(Enum):
    LOW = "low"           # 20-40% annualized
    MEDIUM = "medium"     # 40-80% annualized
    HIGH = "high"         # 80-150% annualized
    EXTREME = "extreme"   # 150%+ annualized

@dataclass
class RegimeThresholds:
    """Volatility regime boundaries (annualized)."""
    low_max: float = 0.40      # 40%
    medium_max: float = 0.80   # 80%
    high_max: float = 1.50     # 150%
    # Above high_max is EXTREME


class VolatilityRegimeClassifier:
    """
    Classify cryptocurrency volatility into discrete regimes.
    
    Implements the four-regime framework:
    - LOW (20-40%): Range-bound, suitable for high leverage
    - MEDIUM (40-80%): Trending, optimal for moderate leverage
    - HIGH (80-150%): Volatile, reduce exposure
    - EXTREME (150%+): Crisis, survival mode
    """
    
    def __init__(self, 
                 thresholds: Optional[RegimeThresholds] = None,
                 lookback_days: int = 30,
                 trading_days_year: int = 365):  # Crypto trades 24/7
        """
        Initialize the classifier.
        
        Parameters
        ----------
        thresholds : RegimeThresholds, optional
            Custom regime boundaries
        lookback_days : int
            Days for volatility calculation
        trading_days_year : int
            Trading days per year (365 for crypto)
        """
        self.thresholds = thresholds or RegimeThresholds()
        self.lookback = lookback_days
        self.trading_days = trading_days_year
        self.history: List[Tuple[str, float, VolRegime]] = []
    
    def calculate_realized_volatility(self, 
                                       prices: np.ndarray,
                                       method: str = 'close_to_close') -> float:
        """
        Calculate realized volatility from price series.
        
        Methods:
        - 'close_to_close': Standard close-to-close log returns
        - 'parkinson': High-low range estimator (more efficient)
        - 'garman_klass': OHLC estimator (most efficient)
        
        Parameters
        ----------
        prices : np.ndarray
            Price data (shape depends on method)
        method : str
            Volatility estimation method
            
        Returns
        -------
        float
            Annualized volatility as decimal (e.g., 0.65 for 65%)
        """
        if method == 'close_to_close':
            # Standard: σ = sqrt(252/N × Σ(log returns)²)
            log_returns = np.log(prices[1:] / prices[:-1])
            daily_var = np.mean(log_returns ** 2)
            annualized_vol = np.sqrt(self.trading_days * daily_var)
            
        elif method == 'parkinson':
            # Parkinson (1980): Uses high-low range
            # More efficient than close-to-close
            # Assumes prices is 2D: [N, 2] with [high, low]
            high = prices[:, 0]
            low = prices[:, 1]
            log_hl = np.log(high / low)
            parkinson_var = np.mean(log_hl ** 2) / (4 * np.log(2))
            annualized_vol = np.sqrt(self.trading_days * parkinson_var)
            
        elif method == 'garman_klass':
            # Garman-Klass (1980): Uses OHLC
            # Most efficient estimator
            # Assumes prices is 2D: [N, 4] with [open, high, low, close]
            o, h, l, c = prices[:, 0], prices[:, 1], prices[:, 2], prices[:, 3]
            log_hl = np.log(h / l)
            log_co = np.log(c / o)
            gk_var = np.mean(0.5 * log_hl**2 - (2*np.log(2) - 1) * log_co**2)
            annualized_vol = np.sqrt(self.trading_days * gk_var)
        else:
            raise ValueError(f"Unknown method: {method}")
        
        return annualized_vol
    
    def classify_regime(self, volatility: float) -> VolRegime:
        """
        Classify volatility into regime.
        
        Parameters
        ----------
        volatility : float
            Annualized volatility as decimal
            
        Returns
        -------
        VolRegime
            Current regime classification
        """
        if volatility <= self.thresholds.low_max:
            return VolRegime.LOW
        elif volatility <= self.thresholds.medium_max:
            return VolRegime.MEDIUM
        elif volatility <= self.thresholds.high_max:
            return VolRegime.HIGH
        else:
            return VolRegime.EXTREME
    
    def get_regime_parameters(self, regime: VolRegime) -> dict:
        """
        Get recommended trading parameters for regime.
        
        Parameters
        ----------
        regime : VolRegime
            Current regime
            
        Returns
        -------
        dict
            Recommended parameters for the regime
        """
        params = {
            VolRegime.LOW: {
                'max_leverage': 10,
                'position_size_pct': 50,  # % of capital per trade
                'stop_loss_pct': 3,
                'take_profit_pct': 6,
                'strategy': 'Range trading, mean reversion',
                'cash_allocation': 20
            },
            VolRegime.MEDIUM: {
                'max_leverage': 5,
                'position_size_pct': 30,
                'stop_loss_pct': 7,
                'take_profit_pct': 15,
                'strategy': 'Trend following, momentum',
                'cash_allocation': 30
            },
            VolRegime.HIGH: {
                'max_leverage': 2,
                'position_size_pct': 15,
                'stop_loss_pct': 12,
                'take_profit_pct': 25,
                'strategy': 'Reduced exposure, defensive',
                'cash_allocation': 50
            },
            VolRegime.EXTREME: {
                'max_leverage': 1,  # Spot only
                'position_size_pct': 5,
                'stop_loss_pct': 15,
                'take_profit_pct': 30,
                'strategy': 'Survival mode, minimal exposure',
                'cash_allocation': 80
            }
        }
        return params[regime]
    
    def calculate_adaptive_leverage(self, 
                                     volatility: float,
                                     target_risk: float = 0.40) -> float:
        """
        Calculate position leverage based on volatility targeting.
        
        Formula: Leverage = Target Risk / Realized Volatility
        
        Parameters
        ----------
        volatility : float
            Current realized volatility (annualized)
        target_risk : float
            Target portfolio volatility (e.g., 0.40 for 40%)
            
        Returns
        -------
        float
            Recommended leverage (capped at 10×)
        """
        if volatility <= 0:
            return 1.0
        
        leverage = target_risk / volatility
        
        # Cap leverage based on regime
        regime = self.classify_regime(volatility)
        max_lev = self.get_regime_parameters(regime)['max_leverage']
        
        return min(leverage, max_lev)
    
    def detect_regime_transition(self, 
                                  current_vol: float,
                                  historical_vols: List[float],
                                  window: int = 5) -> Optional[str]:
        """
        Detect regime transition events.
        
        Parameters
        ----------
        current_vol : float
            Current volatility
        historical_vols : list
            Historical volatility readings
        window : int
            Lookback window for comparison
            
        Returns
        -------
        str or None
            Transition description if detected
        """
        if len(historical_vols) < window:
            return None
        
        recent = historical_vols[-window:]
        current_regime = self.classify_regime(current_vol)
        recent_regimes = [self.classify_regime(v) for v in recent]
        
        # Check if all recent readings were in different regime
        if all(r != current_regime for r in recent_regimes):
            prev_regime = recent_regimes[-1]
            return f"TRANSITION: {prev_regime.value.upper()} → {current_regime.value.upper()}"
        
        return None
    
    def generate_report(self, 
                        prices: np.ndarray,
                        asset: str = 'BTC') -> dict:
        """
        Generate comprehensive volatility regime report.
        
        Parameters
        ----------
        prices : np.ndarray
            Historical close prices
        asset : str
            Asset name
            
        Returns
        -------
        dict
            Complete regime analysis
        """
        # Calculate volatility
        vol = self.calculate_realized_volatility(prices)
        regime = self.classify_regime(vol)
        params = self.get_regime_parameters(regime)
        leverage = self.calculate_adaptive_leverage(vol)
        
        # Historical percentile (assuming long-term BTC vol distribution)
        # Historical BTC vol: mean ~65%, std ~25%
        historical_mean = 0.65
        historical_std = 0.25
        percentile = 100 * (1 - np.exp(-(vol - historical_mean + 2*historical_std) / historical_std))
        percentile = max(0, min(100, percentile))
        
        return {
            'asset': asset,
            'realized_vol_30d': round(vol * 100, 1),
            'regime': regime.value,
            'historical_percentile': round(percentile, 0),
            'recommended_leverage': round(leverage, 1),
            'max_position_pct': params['position_size_pct'],
            'stop_loss_pct': params['stop_loss_pct'],
            'cash_allocation_pct': params['cash_allocation'],
            'strategy': params['strategy']
        }


def demo_regime_classifier():
    """Demonstrate volatility regime classifier."""
    
    print("=" * 60)
    print("VOLATILITY REGIME CLASSIFIER DEMO")
    print("=" * 60)
    
    classifier = VolatilityRegimeClassifier()
    
    # Simulate 60 days of price data with different regimes
    np.random.seed(42)
    
    # Low vol period (first 20 days): ~2% daily vol
    low_vol_returns = np.random.randn(20) * 0.02
    
    # Medium vol period (next 20 days): ~4% daily vol
    medium_vol_returns = np.random.randn(20) * 0.04
    
    # High vol period (last 20 days): ~8% daily vol
    high_vol_returns = np.random.randn(20) * 0.08
    
    # Construct price series
    all_returns = np.concatenate([low_vol_returns, medium_vol_returns, high_vol_returns])
    prices = 43000 * np.cumprod(1 + all_returns)
    prices = np.insert(prices, 0, 43000)  # Add initial price
    
    # Calculate rolling volatility
    window = 20
    rolling_vols = []
    for i in range(window, len(prices)):
        vol = classifier.calculate_realized_volatility(prices[i-window:i+1])
        rolling_vols.append(vol)
    
    print("\n--- Rolling Volatility Analysis ---")
    for i, vol in enumerate(rolling_vols[::10]):  # Sample every 10 periods
        regime = classifier.classify_regime(vol)
        day = (i * 10) + window
        print(f"Day {day}: Vol = {vol*100:.1f}%, Regime = {regime.value.upper()}")
    
    # Full report for current state
    print("\n--- Current Regime Report ---")
    report = classifier.generate_report(prices[-31:], 'BTC')
    for key, value in report.items():
        print(f"  {key}: {value}")
    
    # Demonstrate adaptive leverage
    print("\n--- Adaptive Leverage by Volatility ---")
    test_vols = [0.30, 0.50, 0.80, 1.20, 2.00]
    for vol in test_vols:
        lev = classifier.calculate_adaptive_leverage(vol)
        regime = classifier.classify_regime(vol)
        print(f"  Vol {vol*100:.0f}% ({regime.value}): Leverage = {lev:.1f}×")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo_regime_classifier()
```

---

## 26.P.4 TWAP/VWAP Execution Simulator

### Algorithmic Execution Framework

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import time

class ExecutionAlgo(Enum):
    MARKET = "market"
    TWAP = "twap"
    VWAP = "vwap"
    ICEBERG = "iceberg"

@dataclass
class Fill:
    """Represents a single order fill."""
    timestamp: float
    price: float
    quantity: float
    side: str
    chunk_id: int

@dataclass
class ExecutionResult:
    """Complete execution results."""
    algo: str
    total_quantity: float
    avg_fill_price: float
    benchmark_price: float  # VWAP or arrival price
    slippage_bps: float
    total_cost_usd: float
    execution_time_hours: float
    fills: List[Fill]


class OrderBookSimulator:
    """
    Simulates order book dynamics for execution modeling.
    
    Models:
    - Bid-ask spread
    - Depth at each level
    - Temporary and permanent impact
    - Liquidity replenishment
    """
    
    def __init__(self,
                 mid_price: float,
                 spread_bps: float = 5,  # 0.05% spread
                 depth_per_level: float = 10,  # BTC per $100 level
                 volatility: float = 0.03,  # Daily vol
                 permanent_impact: float = 0.1,
                 temporary_impact: float = 0.5):
        """
        Initialize order book simulator.
        
        Parameters
        ----------
        mid_price : float
            Initial mid-market price
        spread_bps : float
            Bid-ask spread in basis points
        depth_per_level : float
            Liquidity available per price level
        volatility : float
            Daily volatility for price evolution
        permanent_impact : float
            Fraction of impact that persists
        temporary_impact : float
            Fraction of impact that reverts
        """
        self.mid_price = mid_price
        self.spread = spread_bps / 10000
        self.depth = depth_per_level
        self.volatility = volatility
        self.permanent_impact = permanent_impact
        self.temporary_impact = temporary_impact
        self.cumulative_impact = 0.0
    
    def get_execution_price(self, 
                            quantity: float,
                            side: str,
                            daily_volume: float = 50000) -> Tuple[float, float]:
        """
        Calculate execution price for an order using square-root impact model.
        
        Square Root Law: Impact = σ × √(Q/V)
        
        Parameters
        ----------
        quantity : float
            Order quantity in base currency
        side : str
            'buy' or 'sell'
        daily_volume : float
            Average daily volume in base currency
            
        Returns
        -------
        tuple
            (execution_price, impact_bps)
        """
        # Square root impact model
        participation_rate = quantity / daily_volume
        impact = self.volatility * np.sqrt(participation_rate)
        
        # Add spread cost
        half_spread = self.spread / 2
        
        if side == 'buy':
            exec_price = self.mid_price * (1 + half_spread + impact)
        else:
            exec_price = self.mid_price * (1 - half_spread - impact)
        
        # Update mid for permanent impact
        self.cumulative_impact += impact * self.permanent_impact
        if side == 'buy':
            self.mid_price *= (1 + impact * self.permanent_impact)
        else:
            self.mid_price *= (1 - impact * self.permanent_impact)
        
        impact_bps = impact * 10000
        
        return exec_price, impact_bps
    
    def evolve_price(self, hours: float) -> None:
        """
        Evolve mid price with random walk.
        
        Parameters
        ----------
        hours : float
            Time elapsed in hours
        """
        # Convert daily vol to hourly
        hourly_vol = self.volatility / np.sqrt(24)
        price_change = np.random.randn() * hourly_vol * np.sqrt(hours)
        self.mid_price *= (1 + price_change)


class ExecutionSimulator:
    """
    Simulate different execution algorithms.
    
    Implements:
    - Market order (immediate, high impact)
    - TWAP (time-weighted average price)
    - VWAP (volume-weighted average price)
    - Iceberg (hidden size)
    """
    
    def __init__(self,
                 initial_price: float,
                 daily_volume: float = 50000,  # BTC daily volume
                 spread_bps: float = 5,
                 volatility: float = 0.03):
        """
        Initialize execution simulator.
        
        Parameters
        ----------
        initial_price : float
            Starting mid-market price
        daily_volume : float
            Average daily volume in base currency
        spread_bps : float
            Bid-ask spread in basis points
        volatility : float
            Daily volatility
        """
        self.initial_price = initial_price
        self.daily_volume = daily_volume
        self.spread_bps = spread_bps
        self.volatility = volatility
    
    def execute_market_order(self,
                              quantity: float,
                              side: str = 'buy') -> ExecutionResult:
        """
        Execute full quantity immediately as market order.
        
        Parameters
        ----------
        quantity : float
            Total quantity to execute
        side : str
            'buy' or 'sell'
            
        Returns
        -------
        ExecutionResult
            Execution details
        """
        book = OrderBookSimulator(
            self.initial_price,
            self.spread_bps,
            volatility=self.volatility
        )
        
        exec_price, impact_bps = book.get_execution_price(
            quantity, side, self.daily_volume
        )
        
        fill = Fill(
            timestamp=0,
            price=exec_price,
            quantity=quantity,
            side=side,
            chunk_id=0
        )
        
        slippage_bps = (exec_price - self.initial_price) / self.initial_price * 10000
        if side == 'sell':
            slippage_bps = -slippage_bps
        
        return ExecutionResult(
            algo='MARKET',
            total_quantity=quantity,
            avg_fill_price=exec_price,
            benchmark_price=self.initial_price,
            slippage_bps=slippage_bps,
            total_cost_usd=abs(slippage_bps) / 10000 * quantity * exec_price,
            execution_time_hours=0,
            fills=[fill]
        )
    
    def execute_twap(self,
                     quantity: float,
                     duration_hours: float,
                     num_chunks: int,
                     side: str = 'buy') -> ExecutionResult:
        """
        Execute using Time-Weighted Average Price algorithm.
        
        Splits order evenly over time.
        
        Parameters
        ----------
        quantity : float
            Total quantity to execute
        duration_hours : float
            Execution window in hours
        num_chunks : int
            Number of child orders
        side : str
            'buy' or 'sell'
            
        Returns
        -------
        ExecutionResult
            Execution details
        """
        book = OrderBookSimulator(
            self.initial_price,
            self.spread_bps,
            volatility=self.volatility
        )
        
        chunk_size = quantity / num_chunks
        interval_hours = duration_hours / num_chunks
        
        fills = []
        total_cost = 0
        
        for i in range(num_chunks):
            # Execute chunk
            exec_price, _ = book.get_execution_price(
                chunk_size, side, self.daily_volume
            )
            
            fill = Fill(
                timestamp=i * interval_hours,
                price=exec_price,
                quantity=chunk_size,
                side=side,
                chunk_id=i
            )
            fills.append(fill)
            total_cost += chunk_size * exec_price
            
            # Evolve price between chunks
            book.evolve_price(interval_hours)
        
        avg_price = total_cost / quantity
        slippage_bps = (avg_price - self.initial_price) / self.initial_price * 10000
        if side == 'sell':
            slippage_bps = -slippage_bps
        
        return ExecutionResult(
            algo='TWAP',
            total_quantity=quantity,
            avg_fill_price=avg_price,
            benchmark_price=self.initial_price,
            slippage_bps=slippage_bps,
            total_cost_usd=abs(slippage_bps) / 10000 * quantity * avg_price,
            execution_time_hours=duration_hours,
            fills=fills
        )
    
    def execute_vwap(self,
                     quantity: float,
                     duration_hours: float,
                     volume_profile: Optional[List[float]] = None,
                     side: str = 'buy') -> ExecutionResult:
        """
        Execute using Volume-Weighted Average Price algorithm.
        
        Weights execution by expected volume distribution.
        
        Parameters
        ----------
        quantity : float
            Total quantity to execute
        duration_hours : float
            Execution window in hours
        volume_profile : list, optional
            Hourly volume weights (defaults to typical crypto profile)
        side : str
            'buy' or 'sell'
            
        Returns
        -------
        ExecutionResult
            Execution details
        """
        # Default crypto volume profile (24h, relatively flat with some patterns)
        if volume_profile is None:
            # Higher volume during US/EU overlap hours
            volume_profile = np.array([
                0.8, 0.7, 0.6, 0.5, 0.5, 0.6,  # 00:00-06:00 UTC
                0.8, 1.0, 1.2, 1.3, 1.4, 1.5,  # 06:00-12:00 UTC (EU morning)
                1.6, 1.7, 1.8, 1.7, 1.5, 1.3,  # 12:00-18:00 UTC (US morning)
                1.2, 1.1, 1.0, 0.9, 0.85, 0.82  # 18:00-24:00 UTC
            ])
        
        # Normalize to execution window
        hours_in_window = min(int(duration_hours), 24)
        profile = volume_profile[:hours_in_window]
        profile = profile / profile.sum()
        
        book = OrderBookSimulator(
            self.initial_price,
            self.spread_bps,
            volatility=self.volatility
        )
        
        fills = []
        total_cost = 0
        
        for i, weight in enumerate(profile):
            chunk_size = quantity * weight
            
            exec_price, _ = book.get_execution_price(
                chunk_size, side, self.daily_volume
            )
            
            fill = Fill(
                timestamp=i,
                price=exec_price,
                quantity=chunk_size,
                side=side,
                chunk_id=i
            )
            fills.append(fill)
            total_cost += chunk_size * exec_price
            
            book.evolve_price(1)  # 1 hour between chunks
        
        avg_price = total_cost / quantity
        slippage_bps = (avg_price - self.initial_price) / self.initial_price * 10000
        if side == 'sell':
            slippage_bps = -slippage_bps
        
        return ExecutionResult(
            algo='VWAP',
            total_quantity=quantity,
            avg_fill_price=avg_price,
            benchmark_price=self.initial_price,
            slippage_bps=slippage_bps,
            total_cost_usd=abs(slippage_bps) / 10000 * quantity * avg_price,
            execution_time_hours=duration_hours,
            fills=fills
        )
    
    def compare_algorithms(self,
                           quantity: float,
                           duration_hours: float = 6,
                           side: str = 'buy') -> pd.DataFrame:
        """
        Compare execution algorithms for same order.
        
        Parameters
        ----------
        quantity : float
            Total quantity to execute
        duration_hours : float
            Execution window for algos
        side : str
            'buy' or 'sell'
            
        Returns
        -------
        pd.DataFrame
            Comparison of algorithm performance
        """
        results = []
        
        # Market order
        market_result = self.execute_market_order(quantity, side)
        results.append({
            'Algorithm': 'MARKET',
            'Avg Price': market_result.avg_fill_price,
            'Slippage (bps)': market_result.slippage_bps,
            'Cost ($)': market_result.total_cost_usd,
            'Time (hours)': 0,
            'Num Fills': len(market_result.fills)
        })
        
        # TWAP
        twap_result = self.execute_twap(quantity, duration_hours, 
                                         int(duration_hours), side)
        results.append({
            'Algorithm': 'TWAP',
            'Avg Price': twap_result.avg_fill_price,
            'Slippage (bps)': twap_result.slippage_bps,
            'Cost ($)': twap_result.total_cost_usd,
            'Time (hours)': duration_hours,
            'Num Fills': len(twap_result.fills)
        })
        
        # VWAP
        vwap_result = self.execute_vwap(quantity, duration_hours, side=side)
        results.append({
            'Algorithm': 'VWAP',
            'Avg Price': vwap_result.avg_fill_price,
            'Slippage (bps)': vwap_result.slippage_bps,
            'Cost ($)': vwap_result.total_cost_usd,
            'Time (hours)': duration_hours,
            'Num Fills': len(vwap_result.fills)
        })
        
        return pd.DataFrame(results)


def demo_execution_simulator():
    """Demonstrate execution algorithms."""
    
    print("=" * 70)
    print("EXECUTION ALGORITHM COMPARISON")
    print("=" * 70)
    
    simulator = ExecutionSimulator(
        initial_price=43000,
        daily_volume=50000,  # 50K BTC daily volume
        spread_bps=5,
        volatility=0.03
    )
    
    # Large order: 100 BTC (~$4.3M)
    quantity = 100
    
    print(f"\nOrder: Buy {quantity} BTC at ${simulator.initial_price:,.0f}")
    print(f"Notional: ${quantity * simulator.initial_price:,.0f}")
    print(f"Daily Volume: {simulator.daily_volume:,} BTC")
    print(f"Participation: {quantity/simulator.daily_volume*100:.2f}%")
    
    # Compare algorithms
    comparison = simulator.compare_algorithms(quantity, duration_hours=6, side='buy')
    
    print("\n" + "-" * 70)
    print("ALGORITHM COMPARISON")
    print("-" * 70)
    
    for _, row in comparison.iterrows():
        print(f"\n{row['Algorithm']}:")
        print(f"  Avg Fill Price: ${row['Avg Price']:,.2f}")
        print(f"  Slippage: {row['Slippage (bps)']:.1f} bps")
        print(f"  Total Cost: ${row['Cost ($)']:,.0f}")
        print(f"  Execution Time: {row['Time (hours)']:.0f} hours")
    
    # Calculate savings
    market_cost = comparison[comparison['Algorithm'] == 'MARKET']['Cost ($)'].values[0]
    twap_cost = comparison[comparison['Algorithm'] == 'TWAP']['Cost ($)'].values[0]
    vwap_cost = comparison[comparison['Algorithm'] == 'VWAP']['Cost ($)'].values[0]
    
    print("\n" + "-" * 70)
    print("COST SAVINGS vs MARKET ORDER")
    print("-" * 70)
    print(f"TWAP: ${market_cost - twap_cost:,.0f} saved ({(1-twap_cost/market_cost)*100:.1f}%)")
    print(f"VWAP: ${market_cost - vwap_cost:,.0f} saved ({(1-vwap_cost/market_cost)*100:.1f}%)")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demo_execution_simulator()
```

---

## 26.P.5 Basis Trade P&L Tracker

### Cash-and-Carry Arbitrage Monitor

```python
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class BasisPosition:
    """Represents a basis trade position."""
    entry_date: datetime
    asset: str
    spot_exchange: str
    perp_exchange: str
    spot_size: float  # In base currency
    perp_size: float  # Should equal spot_size for delta-neutral
    spot_entry_price: float
    perp_entry_price: float
    
    # Tracking fields
    funding_collected: float = 0.0
    funding_history: List[Dict] = field(default_factory=list)
    fees_paid: float = 0.0
    is_open: bool = True


class BasisTradeTracker:
    """
    Track P&L for cash-and-carry (basis) trades.
    
    Position structure:
    - Long spot (physical BTC/ETH)
    - Short perpetual (synthetic short)
    - Delta-neutral: P&L comes from funding rate collection
    """
    
    def __init__(self):
        """Initialize the tracker."""
        self.positions: Dict[str, BasisPosition] = {}
        self.closed_positions: List[BasisPosition] = []
    
    def open_position(self,
                      position_id: str,
                      asset: str,
                      spot_exchange: str,
                      perp_exchange: str,
                      size: float,
                      spot_price: float,
                      perp_price: float,
                      entry_fee_rate: float = 0.001) -> BasisPosition:
        """
        Open a new basis trade position.
        
        Parameters
        ----------
        position_id : str
            Unique identifier for position
        asset : str
            Asset being traded (e.g., 'BTC')
        spot_exchange : str
            Exchange for spot leg
        perp_exchange : str
            Exchange for perpetual leg
        size : float
            Position size in base currency
        spot_price : float
            Spot entry price
        perp_price : float
            Perpetual entry price
        entry_fee_rate : float
            Combined entry fee rate
            
        Returns
        -------
        BasisPosition
            The opened position
        """
        notional = size * spot_price
        entry_fees = notional * entry_fee_rate * 2  # Both legs
        
        position = BasisPosition(
            entry_date=datetime.utcnow(),
            asset=asset,
            spot_exchange=spot_exchange,
            perp_exchange=perp_exchange,
            spot_size=size,
            perp_size=size,
            spot_entry_price=spot_price,
            perp_entry_price=perp_price,
            fees_paid=entry_fees
        )
        
        self.positions[position_id] = position
        return position
    
    def record_funding(self,
                        position_id: str,
                        funding_rate: float,
                        price: float,
                        timestamp: Optional[datetime] = None) -> float:
        """
        Record a funding payment collection.
        
        Parameters
        ----------
        position_id : str
            Position identifier
        funding_rate : float
            8-hour funding rate (as decimal, e.g., 0.0003 for 0.03%)
        price : float
            Current price for notional calculation
        timestamp : datetime, optional
            Funding timestamp
            
        Returns
        -------
        float
            Funding amount collected (positive = received)
        """
        if position_id not in self.positions:
            raise ValueError(f"Position {position_id} not found")
        
        position = self.positions[position_id]
        
        # Funding payment = Position Size × Price × Rate
        # Short perp receives when funding positive
        notional = position.perp_size * price
        funding_payment = notional * funding_rate
        
        position.funding_collected += funding_payment
        position.funding_history.append({
            'timestamp': timestamp or datetime.utcnow(),
            'rate': funding_rate,
            'price': price,
            'payment': funding_payment
        })
        
        return funding_payment
    
    def get_position_pnl(self,
                          position_id: str,
                          current_spot: float,
                          current_perp: float) -> Dict:
        """
        Calculate current P&L for a position.
        
        Parameters
        ----------
        position_id : str
            Position identifier
        current_spot : float
            Current spot price
        current_perp : float
            Current perpetual price
            
        Returns
        -------
        dict
            Detailed P&L breakdown
        """
        if position_id not in self.positions:
            raise ValueError(f"Position {position_id} not found")
        
        position = self.positions[position_id]
        
        # Spot P&L (long)
        spot_pnl = position.spot_size * (current_spot - position.spot_entry_price)
        
        # Perp P&L (short)
        perp_pnl = position.perp_size * (position.perp_entry_price - current_perp)
        
        # Total market P&L (should be ~0 for delta-neutral)
        market_pnl = spot_pnl + perp_pnl
        
        # Funding P&L
        funding_pnl = position.funding_collected
        
        # Fees
        fees = position.fees_paid
        
        # Net P&L
        net_pnl = market_pnl + funding_pnl - fees
        
        # Calculate notional and returns
        entry_notional = position.spot_size * position.spot_entry_price
        current_notional = position.spot_size * current_spot
        
        # Time in position
        days_held = (datetime.utcnow() - position.entry_date).days or 1
        
        return {
            'position_id': position_id,
            'asset': position.asset,
            'size': position.spot_size,
            'entry_date': position.entry_date,
            'days_held': days_held,
            'entry_notional': entry_notional,
            'current_notional': current_notional,
            'spot_pnl': spot_pnl,
            'perp_pnl': perp_pnl,
            'market_pnl': market_pnl,
            'funding_collected': funding_pnl,
            'fees_paid': fees,
            'net_pnl': net_pnl,
            'return_pct': (net_pnl / entry_notional) * 100,
            'annualized_return': (net_pnl / entry_notional) * (365 / days_held) * 100,
            'funding_payments': len(position.funding_history)
        }
    
    def close_position(self,
                        position_id: str,
                        exit_spot: float,
                        exit_perp: float,
                        exit_fee_rate: float = 0.001) -> Dict:
        """
        Close a position and calculate final P&L.
        
        Parameters
        ----------
        position_id : str
            Position identifier
        exit_spot : float
            Spot exit price
        exit_perp : float
            Perpetual exit price
        exit_fee_rate : float
            Combined exit fee rate
            
        Returns
        -------
        dict
            Final P&L summary
        """
        # Get current P&L
        pnl = self.get_position_pnl(position_id, exit_spot, exit_perp)
        
        # Add exit fees
        position = self.positions[position_id]
        exit_notional = position.spot_size * exit_spot
        exit_fees = exit_notional * exit_fee_rate * 2
        
        position.fees_paid += exit_fees
        position.is_open = False
        
        # Recalculate with exit fees
        pnl['exit_fees'] = exit_fees
        pnl['fees_paid'] += exit_fees
        pnl['net_pnl'] -= exit_fees
        pnl['return_pct'] = (pnl['net_pnl'] / pnl['entry_notional']) * 100
        pnl['annualized_return'] = (pnl['net_pnl'] / pnl['entry_notional']) * (365 / pnl['days_held']) * 100
        
        # Move to closed
        self.closed_positions.append(position)
        del self.positions[position_id]
        
        return pnl
    
    def simulate_basis_trade(self,
                              entry_price: float,
                              size: float,
                              duration_days: int,
                              avg_funding_rate: float,
                              funding_volatility: float = 0.0001,
                              price_drift: float = 0.0,
                              entry_fee: float = 0.001,
                              exit_fee: float = 0.001) -> Dict:
        """
        Simulate a complete basis trade with random funding.
        
        Parameters
        ----------
        entry_price : float
            Entry price for spot and perp
        size : float
            Position size in base currency
        duration_days : int
            Trade duration in days
        avg_funding_rate : float
            Average 8-hour funding rate
        funding_volatility : float
            Standard deviation of funding rate
        price_drift : float
            Average daily price change (for stress testing)
        entry_fee : float
            Entry fee rate
        exit_fee : float
            Exit fee rate
            
        Returns
        -------
        dict
            Simulation results
        """
        # Open position
        position_id = f"sim_{datetime.utcnow().timestamp()}"
        self.open_position(
            position_id=position_id,
            asset='BTC',
            spot_exchange='Coinbase',
            perp_exchange='Binance',
            size=size,
            spot_price=entry_price,
            perp_price=entry_price,
            entry_fee_rate=entry_fee
        )
        
        # Simulate funding over duration (3 payments per day)
        num_payments = duration_days * 3
        funding_rates = avg_funding_rate + np.random.randn(num_payments) * funding_volatility
        
        # Simulate price evolution
        prices = [entry_price]
        for i in range(num_payments):
            daily_return = price_drift / 3 + np.random.randn() * 0.02 / np.sqrt(3)
            prices.append(prices[-1] * (1 + daily_return))
        
        # Record each funding payment
        for i, rate in enumerate(funding_rates):
            self.record_funding(
                position_id=position_id,
                funding_rate=max(rate, -0.005),  # Floor at -0.5%
                price=prices[i],
                timestamp=datetime.utcnow() + timedelta(hours=i*8)
            )
        
        # Close position
        exit_price = prices[-1]
        result = self.close_position(
            position_id=position_id,
            exit_spot=exit_price,
            exit_perp=exit_price,
            exit_fee_rate=exit_fee
        )
        
        result['funding_rates_simulated'] = funding_rates.tolist()
        result['price_path'] = prices
        
        return result


def demo_basis_tracker():
    """Demonstrate basis trade tracking."""
    
    print("=" * 60)
    print("BASIS TRADE P&L TRACKER DEMO")
    print("=" * 60)
    
    tracker = BasisTradeTracker()
    
    # Simulate a 90-day basis trade
    print("\n--- Simulating 90-Day Basis Trade ---")
    
    result = tracker.simulate_basis_trade(
        entry_price=43000,
        size=10,  # 10 BTC
        duration_days=90,
        avg_funding_rate=0.0003,  # 0.03% per 8h = ~33% annual
        funding_volatility=0.0001,
        price_drift=0.001,  # Slight bullish drift
        entry_fee=0.001,
        exit_fee=0.001
    )
    
    print(f"\nTrade Summary:")
    print(f"  Asset: {result['asset']}")
    print(f"  Size: {result['size']:.2f} BTC")
    print(f"  Entry Notional: ${result['entry_notional']:,.0f}")
    print(f"  Duration: {result['days_held']} days")
    print(f"  Funding Payments: {result['funding_payments']}")
    
    print(f"\nP&L Breakdown:")
    print(f"  Spot P&L: ${result['spot_pnl']:,.2f}")
    print(f"  Perp P&L: ${result['perp_pnl']:,.2f}")
    print(f"  Market P&L (should be ~0): ${result['market_pnl']:,.2f}")
    print(f"  Funding Collected: ${result['funding_collected']:,.2f}")
    print(f"  Fees Paid: ${result['fees_paid']:,.2f}")
    print(f"  ─────────────────────")
    print(f"  Net P&L: ${result['net_pnl']:,.2f}")
    print(f"  Return: {result['return_pct']:.2f}%")
    print(f"  Annualized: {result['annualized_return']:.2f}%")
    
    # Statistics on funding rates
    rates = np.array(result['funding_rates_simulated'])
    print(f"\nFunding Rate Statistics:")
    print(f"  Mean: {rates.mean()*100:.4f}% per 8h ({rates.mean()*1095*100:.1f}% annual)")
    print(f"  Min: {rates.min()*100:.4f}%")
    print(f"  Max: {rates.max()*100:.4f}%")
    print(f"  Negative periods: {(rates < 0).sum()} / {len(rates)}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo_basis_tracker()
```

---

## 26.P.6 Open Interest Analysis

### OI Monitoring and Liquidation Heatmap

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class LiquidationCluster:
    """Represents a liquidation price cluster."""
    price_level: float
    estimated_size_usd: float
    distance_pct: float
    leverage_avg: float
    risk_level: str


class OpenInterestAnalyzer:
    """
    Analyze open interest data for positioning insights.
    
    Tracks:
    - OI changes and trends
    - Long/short ratio estimation
    - Liquidation cluster identification
    - OI + Price divergence signals
    """
    
    def __init__(self):
        """Initialize the analyzer."""
        self.oi_history: List[Dict] = []
        self.liquidation_clusters: List[LiquidationCluster] = []
    
    def analyze_oi_price_relationship(self,
                                       oi_series: np.ndarray,
                                       price_series: np.ndarray) -> Dict:
        """
        Analyze OI and price relationship for trend confirmation.
        
        Interpretations:
        - Rising OI + Rising Price = Bullish (new longs entering)
        - Rising OI + Falling Price = Bearish (new shorts entering)
        - Falling OI + Rising Price = Weak rally (short covering)
        - Falling OI + Falling Price = Capitulation (long liquidation)
        
        Parameters
        ----------
        oi_series : np.ndarray
            Open interest time series
        price_series : np.ndarray
            Price time series (same length)
            
        Returns
        -------
        dict
            Analysis results
        """
        if len(oi_series) != len(price_series):
            raise ValueError("Series must be same length")
        
        # Calculate changes
        oi_change = (oi_series[-1] - oi_series[0]) / oi_series[0]
        price_change = (price_series[-1] - price_series[0]) / price_series[0]
        
        # Determine regime
        oi_rising = oi_change > 0.02  # >2% threshold
        oi_falling = oi_change < -0.02
        price_rising = price_change > 0.01
        price_falling = price_change < -0.01
        
        if oi_rising and price_rising:
            interpretation = "BULLISH"
            signal = "Strong trend: New longs entering with conviction"
            strength = min(abs(oi_change) + abs(price_change), 1.0)
        elif oi_rising and price_falling:
            interpretation = "BEARISH"
            signal = "New shorts entering, potential squeeze if reverses"
            strength = min(abs(oi_change) + abs(price_change), 1.0)
        elif oi_falling and price_rising:
            interpretation = "WEAK_RALLY"
            signal = "Short covering, not new buying - fade strength"
            strength = 0.5
        elif oi_falling and price_falling:
            interpretation = "CAPITULATION"
            signal = "Long liquidation cascade, potential bottom near"
            strength = min(abs(oi_change) + abs(price_change), 1.0)
        else:
            interpretation = "NEUTRAL"
            signal = "No clear signal, market consolidating"
            strength = 0.2
        
        # Calculate correlation
        correlation = np.corrcoef(oi_series, price_series)[0, 1]
        
        return {
            'oi_change_pct': oi_change * 100,
            'price_change_pct': price_change * 100,
            'interpretation': interpretation,
            'signal': signal,
            'strength': strength,
            'correlation': correlation,
            'periods': len(oi_series)
        }
    
    def estimate_liquidation_clusters(self,
                                       current_price: float,
                                       total_oi_usd: float,
                                       leverage_distribution: Optional[Dict] = None) -> List[LiquidationCluster]:
        """
        Estimate liquidation price clusters.
        
        Uses typical leverage distribution if not provided.
        
        Parameters
        ----------
        current_price : float
            Current market price
        total_oi_usd : float
            Total open interest in USD
        leverage_distribution : dict, optional
            {leverage: percentage} distribution
            
        Returns
        -------
        list
            List of LiquidationCluster objects
        """
        # Default leverage distribution (based on typical crypto market data)
        if leverage_distribution is None:
            leverage_distribution = {
                100: 0.02,  # 2% at 100×
                50: 0.05,   # 5% at 50×
                25: 0.10,   # 10% at 25×
                20: 0.15,   # 15% at 20×
                10: 0.25,   # 25% at 10×
                5: 0.25,    # 25% at 5×
                3: 0.13,    # 13% at 3×
                2: 0.05     # 5% at 2×
            }
        
        clusters = []
        
        # Assume 60/40 long/short split for longs (liquidate below)
        long_oi = total_oi_usd * 0.6
        
        for leverage, pct in leverage_distribution.items():
            # Liquidation distance ≈ 1/leverage - maintenance margin
            liq_distance = (1 / leverage) - 0.005  # 0.5% maintenance
            liq_price = current_price * (1 - liq_distance)
            size_at_level = long_oi * pct
            distance_pct = liq_distance * 100
            
            # Risk assessment
            if distance_pct < 5:
                risk = 'CRITICAL'
            elif distance_pct < 10:
                risk = 'HIGH'
            elif distance_pct < 20:
                risk = 'MEDIUM'
            else:
                risk = 'LOW'
            
            cluster = LiquidationCluster(
                price_level=round(liq_price, 2),
                estimated_size_usd=size_at_level,
                distance_pct=round(distance_pct, 2),
                leverage_avg=leverage,
                risk_level=risk
            )
            clusters.append(cluster)
        
        # Sort by distance (closest first)
        clusters.sort(key=lambda x: x.distance_pct)
        
        return clusters
    
    def generate_heatmap_data(self,
                              current_price: float,
                              clusters: List[LiquidationCluster],
                              price_range_pct: float = 30) -> pd.DataFrame:
        """
        Generate data for liquidation heatmap visualization.
        
        Parameters
        ----------
        current_price : float
            Current market price
        clusters : list
            Liquidation clusters
        price_range_pct : float
            Price range to display (as percentage)
            
        Returns
        -------
        pd.DataFrame
            Heatmap data with price levels and sizes
        """
        # Create price levels
        price_min = current_price * (1 - price_range_pct/100)
        price_max = current_price * (1 + price_range_pct/100)
        
        # Bin clusters into price levels
        num_levels = 50
        price_levels = np.linspace(price_min, price_max, num_levels)
        
        heatmap_data = []
        for level in price_levels:
            size_at_level = 0
            for cluster in clusters:
                # Gaussian smoothing around cluster
                distance = abs(level - cluster.price_level)
                if distance < current_price * 0.02:  # 2% bandwidth
                    weight = np.exp(-0.5 * (distance / (current_price * 0.01))**2)
                    size_at_level += cluster.estimated_size_usd * weight
            
            distance_from_current = (level - current_price) / current_price * 100
            
            heatmap_data.append({
                'price': level,
                'liquidation_size_usd': size_at_level,
                'distance_pct': distance_from_current,
                'side': 'LONG' if level < current_price else 'SHORT'
            })
        
        return pd.DataFrame(heatmap_data)
    
    def cascade_risk_assessment(self,
                                 current_price: float,
                                 clusters: List[LiquidationCluster],
                                 daily_volume_usd: float) -> Dict:
        """
        Assess risk of liquidation cascade.
        
        Parameters
        ----------
        current_price : float
            Current price
        clusters : list
            Liquidation clusters
        daily_volume_usd : float
            Average daily trading volume
            
        Returns
        -------
        dict
            Cascade risk assessment
        """
        # Sum liquidations within 10% of current price
        near_liqs = sum(
            c.estimated_size_usd for c in clusters
            if c.distance_pct < 10
        )
        
        # Cascade risk = near liquidations / daily volume
        cascade_ratio = near_liqs / daily_volume_usd
        
        if cascade_ratio > 0.5:
            risk_level = 'EXTREME'
            recommendation = 'Consider closing leveraged positions immediately'
        elif cascade_ratio > 0.25:
            risk_level = 'HIGH'
            recommendation = 'Reduce leverage to 3× maximum'
        elif cascade_ratio > 0.10:
            risk_level = 'ELEVATED'
            recommendation = 'Monitor closely, set tight stops'
        else:
            risk_level = 'NORMAL'
            recommendation = 'Normal market conditions'
        
        return {
            'near_liquidations_usd': near_liqs,
            'daily_volume_usd': daily_volume_usd,
            'cascade_ratio': cascade_ratio,
            'risk_level': risk_level,
            'recommendation': recommendation
        }


def demo_oi_analyzer():
    """Demonstrate OI analysis functionality."""
    
    print("=" * 60)
    print("OPEN INTEREST ANALYZER DEMO")
    print("=" * 60)
    
    analyzer = OpenInterestAnalyzer()
    
    # Simulate OI and price data (30 days)
    np.random.seed(42)
    days = 30
    
    # Scenario: Rising OI + Rising Price (bullish)
    price_start = 43000
    prices = price_start * np.cumprod(1 + 0.002 + np.random.randn(days) * 0.02)
    oi_start = 500000  # 500K BTC
    oi = oi_start * np.cumprod(1 + 0.003 + np.random.randn(days) * 0.01)
    
    print("\n--- OI + Price Relationship Analysis ---")
    analysis = analyzer.analyze_oi_price_relationship(oi, prices)
    print(f"OI Change: {analysis['oi_change_pct']:.1f}%")
    print(f"Price Change: {analysis['price_change_pct']:.1f}%")
    print(f"Interpretation: {analysis['interpretation']}")
    print(f"Signal: {analysis['signal']}")
    print(f"Strength: {analysis['strength']:.2f}")
    print(f"Correlation: {analysis['correlation']:.2f}")
    
    # Estimate liquidation clusters
    print("\n--- Liquidation Cluster Estimation ---")
    current_price = prices[-1]
    total_oi_usd = oi[-1] * current_price
    
    clusters = analyzer.estimate_liquidation_clusters(current_price, total_oi_usd)
    
    print(f"\nCurrent Price: ${current_price:,.0f}")
    print(f"Total OI: ${total_oi_usd/1e9:.1f}B")
    print("\nLiquidation Clusters (LONGS):")
    print("-" * 50)
    
    for cluster in clusters[:6]:  # Top 6 closest
        print(f"  ${cluster.price_level:,.0f} ({cluster.distance_pct:.1f}% away): "
              f"${cluster.estimated_size_usd/1e6:.0f}M at {cluster.leverage_avg}× - "
              f"Risk: {cluster.risk_level}")
    
    # Cascade risk assessment
    print("\n--- Cascade Risk Assessment ---")
    daily_volume = 40e9  # $40B daily volume
    risk = analyzer.cascade_risk_assessment(current_price, clusters, daily_volume)
    
    print(f"Liquidations within 10%: ${risk['near_liquidations_usd']/1e9:.2f}B")
    print(f"Daily Volume: ${risk['daily_volume_usd']/1e9:.0f}B")
    print(f"Cascade Ratio: {risk['cascade_ratio']:.2%}")
    print(f"Risk Level: {risk['risk_level']}")
    print(f"Recommendation: {risk['recommendation']}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo_oi_analyzer()
```

---

## Notes on Usage

### Dependencies

```bash
pip install numpy pandas matplotlib
```

### API Integration

The code examples use simulated data for demonstration. For production use, integrate with exchange APIs:

**Binance:**
```python
from binance.client import Client
client = Client(api_key, api_secret)
funding = client.futures_funding_rate(symbol='BTCUSDT')
```

**Bybit:**
```python
from pybit.unified_trading import HTTP
session = HTTP(api_key=api_key, api_secret=api_secret)
funding = session.get_funding_rate_history(category="linear", symbol="BTCUSDT")
```

### Real-Time Monitoring

For production systems:
1. Use websocket connections for real-time data
2. Implement database storage for historical analysis
3. Set up alerting via email/SMS/Telegram
4. Consider cloud deployment (AWS Lambda, GCP Cloud Functions)

---

*Code implementations for Chapter 26: Digital Assets*
*Part of the Quantitative Finance with Python textbook series*
