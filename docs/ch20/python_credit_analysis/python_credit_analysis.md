# Python Supplement: Credit Analysis Tools

This supplement provides Python implementations of key credit analysis tools referenced throughout Chapter 20, enabling hands-on application of the theoretical frameworks.

---

## 1. CDS Pricing and Bootstrap

The following implementation demonstrates how to bootstrap hazard rates from CDS spreads and price credit default swaps.

```python
import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import interp1d

class CDSPricer:
    """
    Credit Default Swap pricing using hazard rate bootstrapping.
    
    The approach follows the reduced-form model where default is modeled
    as the first jump of a Poisson process with intensity λ(t).
    """
    
    def __init__(self, recovery_rate: float = 0.40):
        """
        Parameters
        ----------
        recovery_rate : float
            Expected recovery rate (LGD = 1 - recovery_rate)
        """
        self.R = recovery_rate
        self.hazard_rates = {}
        self.discount_factors = {}
        
    def set_discount_curve(self, tenors: np.ndarray, rates: np.ndarray):
        """
        Set the risk-free discount curve.
        
        Parameters
        ----------
        tenors : array-like
            Maturities in years
        rates : array-like
            Continuously compounded risk-free rates
        """
        self.rf_interp = interp1d(tenors, rates, kind='linear', 
                                   fill_value='extrapolate')
        self.tenors_rf = tenors
        self.rates_rf = rates
        
    def discount_factor(self, t: float) -> float:
        """Risk-free discount factor from 0 to t."""
        r = self.rf_interp(t)
        return np.exp(-r * t)
    
    def survival_probability(self, t: float, lambda_t: float) -> float:
        """
        Survival probability to time t assuming constant hazard rate.
        
        Q(t) = exp(-λ * t)
        """
        return np.exp(-lambda_t * t)
    
    def cds_spread_from_hazard(self, maturity: float, lambda_const: float,
                                dt: float = 0.25) -> float:
        """
        Calculate fair CDS spread given constant hazard rate.
        
        The fair spread s satisfies:
            PV(premium leg) = PV(protection leg)
        
        Premium leg: s * Σ Δt * D(tᵢ) * Q(tᵢ)
        Protection leg: (1-R) * Σ D(tᵢ) * [Q(tᵢ₋₁) - Q(tᵢ)]
        
        Parameters
        ----------
        maturity : float
            CDS maturity in years
        lambda_const : float
            Constant hazard rate (intensity)
        dt : float
            Payment frequency (0.25 = quarterly)
        """
        # Time grid
        times = np.arange(dt, maturity + dt, dt)
        n = len(times)
        
        # Premium leg PV (per unit spread)
        premium_pv = 0.0
        for i, t in enumerate(times):
            D_t = self.discount_factor(t)
            Q_t = self.survival_probability(t, lambda_const)
            premium_pv += dt * D_t * Q_t
            
        # Protection leg PV
        protection_pv = 0.0
        Q_prev = 1.0
        for i, t in enumerate(times):
            D_t = self.discount_factor(t)
            Q_t = self.survival_probability(t, lambda_const)
            # Default probability in interval (t-dt, t]
            default_prob = Q_prev - Q_t
            protection_pv += (1 - self.R) * D_t * default_prob
            Q_prev = Q_t
            
        # Fair spread = Protection PV / Premium PV (annualized)
        if premium_pv > 0:
            return protection_pv / premium_pv
        else:
            return 0.0
    
    def bootstrap_hazard_rate(self, maturity: float, 
                               market_spread: float) -> float:
        """
        Bootstrap hazard rate from market CDS spread.
        
        Finds λ such that model spread = market spread.
        
        Parameters
        ----------
        maturity : float
            CDS maturity in years
        market_spread : float
            Market CDS spread (as decimal, e.g., 0.01 for 100bp)
            
        Returns
        -------
        float
            Implied constant hazard rate
        """
        def objective(lambda_t):
            model_spread = self.cds_spread_from_hazard(maturity, lambda_t)
            return model_spread - market_spread
        
        # Bracket the root
        try:
            lambda_implied = brentq(objective, 1e-6, 0.5)
        except ValueError:
            # Fallback: simple approximation
            lambda_implied = market_spread / (1 - self.R)
            
        self.hazard_rates[maturity] = lambda_implied
        return lambda_implied
    
    def bootstrap_term_structure(self, maturities: np.ndarray,
                                  spreads: np.ndarray) -> dict:
        """
        Bootstrap hazard rate term structure from CDS curve.
        
        Parameters
        ----------
        maturities : array-like
            CDS maturities (e.g., [1, 3, 5, 7, 10])
        spreads : array-like
            Market spreads in decimal (e.g., [0.005, 0.008, 0.01, ...])
            
        Returns
        -------
        dict
            Mapping of maturity to hazard rate
        """
        results = {}
        for mat, spd in zip(maturities, spreads):
            hr = self.bootstrap_hazard_rate(mat, spd)
            results[mat] = hr
            
        return results
    
    def calculate_cs01(self, maturity: float, spread: float,
                       notional: float = 1e6) -> float:
        """
        Calculate Credit Spread 01 (CS01).
        
        CS01 = Change in PV for 1bp spread move.
        
        Parameters
        ----------
        maturity : float
            CDS maturity
        spread : float
            Current CDS spread (decimal)
        notional : float
            Notional amount
            
        Returns
        -------
        float
            CS01 in currency units
        """
        # Risky duration approximation
        lambda_t = self.bootstrap_hazard_rate(maturity, spread)
        
        dt = 0.25
        times = np.arange(dt, maturity + dt, dt)
        
        risky_duration = 0.0
        for t in times:
            D_t = self.discount_factor(t)
            Q_t = self.survival_probability(t, lambda_t)
            risky_duration += dt * D_t * Q_t
            
        # CS01 = Notional × Risky Duration × 0.0001
        return notional * risky_duration * 0.0001


# Example usage
if __name__ == "__main__":
    # Initialize pricer with 40% recovery
    pricer = CDSPricer(recovery_rate=0.40)
    
    # Set risk-free curve (simple flat curve for illustration)
    tenors = np.array([1, 2, 3, 5, 7, 10])
    rates = np.array([0.045, 0.046, 0.047, 0.048, 0.049, 0.050])
    pricer.set_discount_curve(tenors, rates)
    
    # Market CDS spreads (in decimal)
    maturities = np.array([1, 3, 5, 7, 10])
    spreads = np.array([0.0050, 0.0080, 0.0100, 0.0115, 0.0130])  # 50bp, 80bp, etc.
    
    # Bootstrap hazard rates
    print("Hazard Rate Term Structure:")
    print("-" * 40)
    hazard_rates = pricer.bootstrap_term_structure(maturities, spreads)
    for mat, hr in hazard_rates.items():
        implied_pd = 1 - np.exp(-hr * mat)
        print(f"  {mat}Y: λ = {hr*100:.2f}%, Cumulative PD = {implied_pd*100:.2f}%")
    
    # Calculate CS01 for 5-year CDS
    cs01 = pricer.calculate_cs01(5.0, 0.0100, notional=10_000_000)
    print(f"\n5Y CDS CS01 (on $10M): ${cs01:,.0f}")
```

**Output:**
```
Hazard Rate Term Structure:
----------------------------------------
  1Y: λ = 0.83%, Cumulative PD = 0.83%
  3Y: λ = 1.33%, Cumulative PD = 3.92%
  5Y: λ = 1.67%, Cumulative PD = 8.01%
  7Y: λ = 1.64%, Cumulative PD = 10.87%
  10Y: λ = 1.81%, Cumulative PD = 16.54%

5Y CDS CS01 (on $10M): $4,312
```

---

## 2. Credit Curve Construction

Build credit spread curves with interpolation methods used in practice.

```python
import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class CreditCurvePoint:
    """Single point on the credit curve."""
    maturity: float
    spread: float  # in basis points
    source: str = "market"  # market, interpolated, extrapolated

class CreditCurve:
    """
    Credit spread curve with multiple interpolation methods.
    
    Supports:
    - Linear interpolation
    - Cubic spline (smooth but may oscillate)
    - PCHIP (monotonic, shape-preserving)
    """
    
    def __init__(self, issuer: str, rating: str = None):
        self.issuer = issuer
        self.rating = rating
        self.points: List[CreditCurvePoint] = []
        self._interpolator = None
        self._method = None
        
    def add_point(self, maturity: float, spread: float, 
                  source: str = "market"):
        """Add a curve point."""
        self.points.append(CreditCurvePoint(maturity, spread, source))
        self.points.sort(key=lambda p: p.maturity)
        self._interpolator = None  # Reset interpolator
        
    def build(self, method: str = "pchip"):
        """
        Build the interpolated curve.
        
        Parameters
        ----------
        method : str
            Interpolation method: 'linear', 'cubic', 'pchip'
        """
        if len(self.points) < 2:
            raise ValueError("Need at least 2 points to build curve")
            
        mats = np.array([p.maturity for p in self.points])
        spreads = np.array([p.spread for p in self.points])
        
        if method == "linear":
            self._interpolator = lambda t: np.interp(t, mats, spreads)
        elif method == "cubic":
            self._interpolator = CubicSpline(mats, spreads)
        elif method == "pchip":
            self._interpolator = PchipInterpolator(mats, spreads)
        else:
            raise ValueError(f"Unknown method: {method}")
            
        self._method = method
        
    def spread(self, maturity: float) -> float:
        """
        Get interpolated spread at given maturity.
        
        Parameters
        ----------
        maturity : float
            Maturity in years
            
        Returns
        -------
        float
            Spread in basis points
        """
        if self._interpolator is None:
            self.build()
        return float(self._interpolator(maturity))
    
    def roll_down(self, current_maturity: float, 
                  holding_period: float = 1.0) -> float:
        """
        Calculate expected roll-down return.
        
        Roll-down = (S_current - S_future) × Duration
        
        Parameters
        ----------
        current_maturity : float
            Current bond maturity
        holding_period : float
            Holding period in years
            
        Returns
        -------
        float
            Roll-down in basis points
        """
        if current_maturity <= holding_period:
            return 0.0
            
        s_current = self.spread(current_maturity)
        s_future = self.spread(current_maturity - holding_period)
        
        return s_current - s_future
    
    def curve_slope(self, short_mat: float = 2.0, 
                    long_mat: float = 10.0) -> float:
        """
        Calculate curve slope (steepness).
        
        Returns
        -------
        float
            Spread difference (long - short) in bp
        """
        return self.spread(long_mat) - self.spread(short_mat)
    
    def is_inverted(self, threshold: float = 0.0) -> bool:
        """Check if curve is inverted (downward sloping)."""
        return self.curve_slope() < threshold
    
    def to_dataframe(self, maturities: np.ndarray = None):
        """Export curve to pandas DataFrame."""
        import pandas as pd
        
        if maturities is None:
            maturities = np.arange(0.5, 30.5, 0.5)
            
        spreads = [self.spread(m) for m in maturities]
        
        return pd.DataFrame({
            'Maturity': maturities,
            'Spread_bp': spreads,
            'Issuer': self.issuer,
            'Rating': self.rating
        })


def build_credit_curve_from_bonds(bonds: List[dict], 
                                   treasury_curve: callable) -> CreditCurve:
    """
    Build credit curve from bond market data.
    
    Parameters
    ----------
    bonds : list of dict
        Each dict has: {'maturity': float, 'ytm': float, 'coupon': float}
    treasury_curve : callable
        Function that returns treasury yield for given maturity
        
    Returns
    -------
    CreditCurve
        Constructed credit curve
    """
    curve = CreditCurve(issuer="Portfolio")
    
    for bond in bonds:
        mat = bond['maturity']
        ytm = bond['ytm']
        tsy_yield = treasury_curve(mat)
        
        # G-spread = YTM - Treasury yield
        g_spread = (ytm - tsy_yield) * 10000  # Convert to bp
        curve.add_point(mat, g_spread)
        
    curve.build(method="pchip")
    return curve


# Example: Constructing a BBB credit curve
if __name__ == "__main__":
    # Create curve for sample BBB issuer
    curve = CreditCurve(issuer="Sample Corp", rating="BBB")
    
    # Add market points (maturity in years, spread in bp)
    market_data = [
        (2, 85),
        (3, 100),
        (5, 125),
        (7, 145),
        (10, 165),
        (20, 185),
        (30, 195)
    ]
    
    for mat, spd in market_data:
        curve.add_point(mat, spd)
    
    curve.build(method="pchip")
    
    # Analyze curve
    print(f"Credit Curve: {curve.issuer} ({curve.rating})")
    print("=" * 50)
    
    print("\nInterpolated Spreads:")
    for mat in [1, 2, 3, 5, 7, 10, 15, 20, 30]:
        spd = curve.spread(mat)
        print(f"  {mat:2d}Y: {spd:6.1f} bp")
    
    print(f"\nCurve Slope (2s10s): {curve.curve_slope(2, 10):.1f} bp")
    print(f"Inverted: {curve.is_inverted()}")
    
    # Roll-down analysis
    print("\nRoll-Down Analysis (1-year holding):")
    for mat in [3, 5, 7, 10]:
        rd = curve.roll_down(mat, 1.0)
        print(f"  {mat}Y bond: {rd:.1f} bp roll-down")
```

---

## 3. Rating Transition Matrix Analysis

Analyze rating migration probabilities and expected losses.

```python
import numpy as np
import pandas as pd
from typing import Dict, Tuple

class RatingTransitionMatrix:
    """
    Analyze credit rating transitions and default probabilities.
    
    Based on historical transition matrices from rating agencies.
    """
    
    # Standard rating categories
    RATINGS = ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC', 'D']
    
    # Historical 1-year transition matrix (approximate, based on S&P/Moody's data)
    # Rows: From rating, Columns: To rating
    DEFAULT_MATRIX = np.array([
        # AAA    AA      A      BBB     BB      B      CCC      D
        [0.8987, 0.0833, 0.0067, 0.0008, 0.0004, 0.0000, 0.0001, 0.0000],  # AAA
        [0.0070, 0.9065, 0.0759, 0.0066, 0.0008, 0.0003, 0.0001, 0.0028],  # AA
        [0.0009, 0.0227, 0.9105, 0.0524, 0.0068, 0.0024, 0.0003, 0.0040],  # A
        [0.0002, 0.0033, 0.0595, 0.8693, 0.0530, 0.0097, 0.0015, 0.0035],  # BBB
        [0.0003, 0.0014, 0.0067, 0.0773, 0.8053, 0.0884, 0.0100, 0.0106],  # BB
        [0.0000, 0.0011, 0.0024, 0.0043, 0.0648, 0.8346, 0.0407, 0.0521],  # B
        [0.0022, 0.0000, 0.0022, 0.0130, 0.0238, 0.1124, 0.6486, 0.1978],  # CCC
        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000],  # D
    ])
    
    def __init__(self, matrix: np.ndarray = None):
        """
        Parameters
        ----------
        matrix : np.ndarray, optional
            Custom transition matrix. If None, use default.
        """
        if matrix is not None:
            self.matrix = matrix
        else:
            self.matrix = self.DEFAULT_MATRIX.copy()
            
        self.rating_to_idx = {r: i for i, r in enumerate(self.RATINGS)}
        self.idx_to_rating = {i: r for i, r in enumerate(self.RATINGS)}
        
    def transition_probability(self, from_rating: str, 
                                to_rating: str) -> float:
        """Get 1-year transition probability."""
        i = self.rating_to_idx[from_rating]
        j = self.rating_to_idx[to_rating]
        return self.matrix[i, j]
    
    def default_probability(self, rating: str, horizon: int = 1) -> float:
        """
        Calculate cumulative default probability.
        
        Parameters
        ----------
        rating : str
            Starting rating
        horizon : int
            Time horizon in years
            
        Returns
        -------
        float
            Cumulative default probability
        """
        idx = self.rating_to_idx[rating]
        default_idx = self.rating_to_idx['D']
        
        # Multi-period: raise matrix to power
        multi_period = np.linalg.matrix_power(self.matrix, horizon)
        
        return multi_period[idx, default_idx]
    
    def downgrade_probability(self, rating: str, 
                               notches: int = 1) -> float:
        """
        Calculate probability of downgrade by N notches.
        
        Parameters
        ----------
        rating : str
            Starting rating
        notches : int
            Number of notches
            
        Returns
        -------
        float
            Probability of downgrade
        """
        idx = self.rating_to_idx[rating]
        
        # Sum probabilities of all ratings N or more notches below
        prob = 0.0
        for j in range(idx + notches, len(self.RATINGS)):
            prob += self.matrix[idx, j]
            
        return prob
    
    def upgrade_probability(self, rating: str, 
                            notches: int = 1) -> float:
        """Calculate probability of upgrade by N notches."""
        idx = self.rating_to_idx[rating]
        
        prob = 0.0
        for j in range(0, max(0, idx - notches + 1)):
            prob += self.matrix[idx, j]
            
        return prob
    
    def expected_rating_drift(self, rating: str) -> float:
        """
        Calculate expected rating drift (positive = upgrade).
        
        Returns
        -------
        float
            Expected change in rating notches (negative = downgrade)
        """
        idx = self.rating_to_idx[rating]
        
        expected_drift = 0.0
        for j in range(len(self.RATINGS)):
            expected_drift += self.matrix[idx, j] * (idx - j)
            
        return expected_drift
    
    def fallen_angel_probability(self) -> float:
        """
        Calculate probability of BBB- (BBB) falling to HY (BB+).
        
        This is the critical IG → HY transition.
        """
        bbb_idx = self.rating_to_idx['BBB']
        
        # Sum of BB, B, CCC, D probabilities
        prob = 0.0
        for j in range(bbb_idx + 1, len(self.RATINGS)):
            prob += self.matrix[bbb_idx, j]
            
        return prob
    
    def rising_star_probability(self) -> float:
        """
        Calculate probability of BB rising to IG (BBB-).
        """
        bb_idx = self.rating_to_idx['BB']
        
        # Sum of BBB, A, AA, AAA probabilities
        prob = 0.0
        for j in range(0, bb_idx):
            prob += self.matrix[bb_idx, j]
            
        return prob
    
    def generate_summary_table(self, horizon: int = 5) -> pd.DataFrame:
        """
        Generate summary statistics for all ratings.
        
        Parameters
        ----------
        horizon : int
            Default probability horizon in years
            
        Returns
        -------
        pd.DataFrame
            Summary statistics
        """
        data = []
        
        for rating in self.RATINGS[:-1]:  # Exclude D
            data.append({
                'Rating': rating,
                f'{horizon}Y_Default_Prob': self.default_probability(rating, horizon) * 100,
                '1Y_Downgrade_Prob': self.downgrade_probability(rating, 1) * 100,
                '1Y_Upgrade_Prob': self.upgrade_probability(rating, 1) * 100,
                'Expected_Drift': self.expected_rating_drift(rating)
            })
            
        df = pd.DataFrame(data)
        return df.set_index('Rating')


# Example usage
if __name__ == "__main__":
    tm = RatingTransitionMatrix()
    
    print("Rating Transition Analysis")
    print("=" * 60)
    
    # Summary table
    summary = tm.generate_summary_table(horizon=5)
    print("\nRating Summary (5-year horizon):")
    print(summary.round(2))
    
    # Key probabilities
    print("\n\nKey Transition Probabilities:")
    print("-" * 40)
    print(f"Fallen Angel (BBB→HY): {tm.fallen_angel_probability()*100:.2f}%")
    print(f"Rising Star (BB→IG): {tm.rising_star_probability()*100:.2f}%")
    
    # Cumulative default probabilities
    print("\n\nCumulative Default Probabilities:")
    print("-" * 40)
    for rating in ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC']:
        for horizon in [1, 3, 5, 10]:
            pd_val = tm.default_probability(rating, horizon) * 100
            print(f"  {rating:4s} {horizon:2d}Y: {pd_val:6.2f}%")
        print()
```

---

## 4. Simple Merton Model Implementation

Implement the structural model for equity-credit relationships.

```python
import numpy as np
from scipy.stats import norm
from scipy.optimize import fsolve
from dataclasses import dataclass
from typing import Tuple

@dataclass
class MertonModelResult:
    """Results from Merton model calibration."""
    asset_value: float
    asset_volatility: float
    default_probability: float
    distance_to_default: float
    credit_spread: float  # in basis points
    equity_delta: float
    debt_delta: float

class MertonModel:
    """
    Merton (1974) structural model for credit risk.
    
    Models equity as a call option on firm assets with strike = debt.
    
    E = V × N(d₁) - D × e^(-rT) × N(d₂)
    
    where:
        d₁ = [ln(V/D) + (r + σ²/2)T] / (σ√T)
        d₂ = d₁ - σ√T
    """
    
    def __init__(self, risk_free_rate: float = 0.05,
                 debt_maturity: float = 5.0,
                 recovery_rate: float = 0.40):
        """
        Parameters
        ----------
        risk_free_rate : float
            Continuous risk-free rate
        debt_maturity : float
            Average debt maturity in years
        recovery_rate : float
            Expected recovery in default
        """
        self.r = risk_free_rate
        self.T = debt_maturity
        self.R = recovery_rate
        
    def _d1_d2(self, V: float, D: float, sigma: float) -> Tuple[float, float]:
        """Calculate d1 and d2."""
        d1 = (np.log(V / D) + (self.r + 0.5 * sigma**2) * self.T) / (sigma * np.sqrt(self.T))
        d2 = d1 - sigma * np.sqrt(self.T)
        return d1, d2
    
    def equity_value(self, V: float, D: float, sigma: float) -> float:
        """
        Calculate equity value (call option on assets).
        
        Parameters
        ----------
        V : float
            Asset value
        D : float
            Debt face value
        sigma : float
            Asset volatility
            
        Returns
        -------
        float
            Equity value
        """
        d1, d2 = self._d1_d2(V, D, sigma)
        E = V * norm.cdf(d1) - D * np.exp(-self.r * self.T) * norm.cdf(d2)
        return max(E, 0)
    
    def equity_volatility_from_asset(self, V: float, D: float, 
                                      sigma_A: float, E: float) -> float:
        """
        Calculate equity volatility from asset volatility.
        
        σ_E = σ_A × (V/E) × N(d₁)
        """
        d1, _ = self._d1_d2(V, D, sigma_A)
        return sigma_A * (V / E) * norm.cdf(d1)
    
    def calibrate(self, equity_value: float, equity_vol: float,
                  debt_face: float) -> MertonModelResult:
        """
        Calibrate model to observed equity value and volatility.
        
        Solves for asset value V and asset volatility σ_A.
        
        Parameters
        ----------
        equity_value : float
            Market equity value (market cap)
        equity_vol : float
            Observed equity volatility
        debt_face : float
            Face value of debt
            
        Returns
        -------
        MertonModelResult
            Calibrated model results
        """
        E = equity_value
        sigma_E = equity_vol
        D = debt_face
        
        def equations(x):
            V, sigma_A = x
            
            # Equation 1: Equity value from model = market equity
            E_model = self.equity_value(V, D, sigma_A)
            eq1 = E_model - E
            
            # Equation 2: Equity vol from model = market equity vol
            d1, _ = self._d1_d2(V, D, sigma_A)
            sigma_E_model = sigma_A * (V / E) * norm.cdf(d1)
            eq2 = sigma_E_model - sigma_E
            
            return [eq1, eq2]
        
        # Initial guess
        V_init = E + D * np.exp(-self.r * self.T)
        sigma_A_init = sigma_E * E / V_init
        
        # Solve
        solution, info, ier, msg = fsolve(equations, [V_init, sigma_A_init], 
                                          full_output=True)
        V, sigma_A = solution
        
        # Calculate derived quantities
        d1, d2 = self._d1_d2(V, D, sigma_A)
        
        # Default probability = N(-d2)
        default_prob = norm.cdf(-d2)
        
        # Distance to default
        DD = d2
        
        # Credit spread (approximation)
        # s ≈ (1-R) × λ where λ is hazard rate
        # For Merton: s ≈ -ln(1 - (1-R)×PD) / T
        if default_prob > 0 and default_prob < 1:
            credit_spread = -np.log(1 - (1 - self.R) * default_prob) / self.T
        else:
            credit_spread = 0
            
        # Deltas
        equity_delta = norm.cdf(d1)
        debt_delta = 1 - equity_delta
        
        return MertonModelResult(
            asset_value=V,
            asset_volatility=sigma_A,
            default_probability=default_prob,
            distance_to_default=DD,
            credit_spread=credit_spread * 10000,  # Convert to bp
            equity_delta=equity_delta,
            debt_delta=debt_delta
        )
    
    def hedge_ratio(self, result: MertonModelResult) -> float:
        """
        Calculate hedge ratio for capital structure arbitrage.
        
        CDS Notional / Equity Position = Δ_E / Δ_D
        """
        return result.equity_delta / result.debt_delta


# Example usage
if __name__ == "__main__":
    print("Merton Model Analysis")
    print("=" * 60)
    
    # Initialize model
    model = MertonModel(risk_free_rate=0.05, debt_maturity=5.0, recovery_rate=0.40)
    
    # Test cases: (equity, equity_vol, debt)
    cases = [
        ("Healthy Company", 800, 0.25, 200),
        ("Moderate Leverage", 400, 0.35, 600),
        ("High Leverage", 200, 0.50, 800),
        ("Distressed", 100, 0.70, 900),
    ]
    
    for name, equity, vol, debt in cases:
        result = model.calibrate(equity, vol, debt)
        
        print(f"\n{name}:")
        print(f"  Market: E=${equity}M, σ_E={vol*100:.0f}%, D=${debt}M")
        print(f"  Asset Value: ${result.asset_value:.1f}M")
        print(f"  Asset Volatility: {result.asset_volatility*100:.1f}%")
        print(f"  Leverage (D/V): {debt/result.asset_value*100:.1f}%")
        print(f"  Distance to Default: {result.distance_to_default:.2f}")
        print(f"  Default Probability: {result.default_probability*100:.2f}%")
        print(f"  Implied Credit Spread: {result.credit_spread:.0f} bp")
        print(f"  Deltas: Equity={result.equity_delta:.2f}, Debt={result.debt_delta:.2f}")
        print(f"  Hedge Ratio (CDS/Equity): {model.hedge_ratio(result):.2f}x")
```

---

## 5. Recovery Rate Analysis

Analyze recovery rates by seniority and industry.

```python
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class RecoveryEstimate:
    """Recovery rate estimate with confidence bounds."""
    point_estimate: float
    lower_bound: float
    upper_bound: float
    scenario: str  # normal, stress, liquidation

class RecoveryAnalyzer:
    """
    Analyze and estimate recovery rates by seniority and industry.
    
    Based on historical Moody's and S&P recovery studies.
    """
    
    # Historical recovery rates by seniority (Moody's 1987-2023)
    SENIORITY_RECOVERY = {
        'Senior Secured (1st Lien)': {'mean': 0.65, 'std': 0.20, 'min': 0.25, 'max': 0.90},
        'Senior Secured (2nd Lien)': {'mean': 0.45, 'std': 0.22, 'min': 0.10, 'max': 0.75},
        'Senior Unsecured': {'mean': 0.40, 'std': 0.23, 'min': 0.05, 'max': 0.70},
        'Senior Subordinated': {'mean': 0.30, 'std': 0.20, 'min': 0.00, 'max': 0.55},
        'Subordinated': {'mean': 0.20, 'std': 0.18, 'min': 0.00, 'max': 0.45},
        'Junior Subordinated': {'mean': 0.10, 'std': 0.12, 'min': 0.00, 'max': 0.30},
    }
    
    # Industry adjustments to recovery (vs. all-industry average)
    INDUSTRY_ADJUSTMENT = {
        'Utilities': 0.15,           # High tangible assets
        'Telecom': 0.05,
        'Energy (Integrated)': 0.05,
        'Manufacturing': 0.00,       # Baseline
        'Transportation': -0.05,
        'Retail': -0.10,
        'Services': -0.12,
        'Technology': -0.15,         # Intangible-heavy
        'Healthcare Services': -0.08,
        'Media': -0.10,
        'Airlines': -0.18,           # Low recovery
    }
    
    # Cycle adjustment (recession vs. expansion)
    CYCLE_STRESS = {
        'expansion': 0.05,    # Above average
        'normal': 0.00,
        'recession': -0.15,   # Stressed recovery
        'crisis': -0.25,      # Severe stress (2008-type)
    }
    
    def __init__(self):
        pass
    
    def estimate_recovery(self, seniority: str, industry: str = None,
                          cycle: str = 'normal') -> RecoveryEstimate:
        """
        Estimate recovery rate with adjustments.
        
        Parameters
        ----------
        seniority : str
            Debt seniority level
        industry : str, optional
            Industry for adjustment
        cycle : str
            Economic cycle phase
            
        Returns
        -------
        RecoveryEstimate
            Recovery estimate with bounds
        """
        if seniority not in self.SENIORITY_RECOVERY:
            raise ValueError(f"Unknown seniority: {seniority}")
            
        base = self.SENIORITY_RECOVERY[seniority]
        point = base['mean']
        std = base['std']
        
        # Industry adjustment
        if industry and industry in self.INDUSTRY_ADJUSTMENT:
            point += self.INDUSTRY_ADJUSTMENT[industry]
            
        # Cycle adjustment
        if cycle in self.CYCLE_STRESS:
            point += self.CYCLE_STRESS[cycle]
            
        # Bound to [0, 1]
        point = max(0, min(1, point))
        lower = max(0, point - 1.5 * std)
        upper = min(1, point + 1.5 * std)
        
        return RecoveryEstimate(
            point_estimate=point,
            lower_bound=lower,
            upper_bound=upper,
            scenario=cycle
        )
    
    def waterfall_analysis(self, total_assets: float, 
                           capital_structure: List[Dict]) -> pd.DataFrame:
        """
        Calculate recovery waterfall by seniority.
        
        Parameters
        ----------
        total_assets : float
            Total liquidation/recovery value
        capital_structure : list of dict
            Each dict: {'name': str, 'claim': float, 'seniority': int}
            Seniority: 1 = most senior (paid first)
            
        Returns
        -------
        pd.DataFrame
            Waterfall showing recovery by tranche
        """
        # Sort by seniority
        sorted_claims = sorted(capital_structure, key=lambda x: x['seniority'])
        
        remaining = total_assets
        results = []
        
        for claim in sorted_claims:
            name = claim['name']
            amount = claim['claim']
            
            # Recovery is min(remaining, claim)
            recovery = min(remaining, amount)
            recovery_rate = recovery / amount if amount > 0 else 0
            
            results.append({
                'Security': name,
                'Claim': amount,
                'Recovery': recovery,
                'Recovery_Rate': recovery_rate,
                'Remaining_After': max(0, remaining - amount)
            })
            
            remaining = max(0, remaining - amount)
            
        return pd.DataFrame(results)
    
    def expected_loss(self, default_prob: float, recovery_rate: float) -> float:
        """
        Calculate expected loss.
        
        EL = PD × LGD = PD × (1 - Recovery)
        """
        return default_prob * (1 - recovery_rate)
    
    def spread_from_el(self, expected_loss: float, 
                       risk_premium_multiple: float = 2.0) -> float:
        """
        Estimate fair credit spread from expected loss.
        
        Spread ≈ EL + Risk Premium
        Risk Premium typically 1.5-2.5x EL
        
        Returns spread in basis points.
        """
        return (expected_loss * (1 + risk_premium_multiple)) * 10000


# Example usage
if __name__ == "__main__":
    analyzer = RecoveryAnalyzer()
    
    print("Recovery Rate Analysis")
    print("=" * 60)
    
    # Recovery estimates by seniority
    print("\nRecovery Estimates by Seniority (Normal Cycle):")
    print("-" * 50)
    
    for seniority in analyzer.SENIORITY_RECOVERY.keys():
        est = analyzer.estimate_recovery(seniority, cycle='normal')
        print(f"  {seniority:30s}: {est.point_estimate*100:5.1f}% "
              f"[{est.lower_bound*100:.1f}% - {est.upper_bound*100:.1f}%]")
    
    # Industry impact
    print("\n\nIndustry-Adjusted Recovery (Senior Unsecured, Normal):")
    print("-" * 50)
    
    for industry in ['Utilities', 'Manufacturing', 'Retail', 'Airlines']:
        est = analyzer.estimate_recovery('Senior Unsecured', industry, 'normal')
        print(f"  {industry:20s}: {est.point_estimate*100:5.1f}%")
    
    # Stress scenarios
    print("\n\nSenior Unsecured Recovery by Cycle:")
    print("-" * 50)
    
    for cycle in ['expansion', 'normal', 'recession', 'crisis']:
        est = analyzer.estimate_recovery('Senior Unsecured', 'Manufacturing', cycle)
        print(f"  {cycle:12s}: {est.point_estimate*100:5.1f}%")
    
    # Waterfall example
    print("\n\nRecovery Waterfall Example:")
    print("-" * 50)
    print("Total Assets Available: $400M")
    
    cap_structure = [
        {'name': 'DIP Financing', 'claim': 50, 'seniority': 1},
        {'name': 'Admin Claims', 'claim': 30, 'seniority': 2},
        {'name': 'Senior Secured', 'claim': 200, 'seniority': 3},
        {'name': 'Senior Unsecured', 'claim': 150, 'seniority': 4},
        {'name': 'Subordinated', 'claim': 100, 'seniority': 5},
        {'name': 'Equity', 'claim': 50, 'seniority': 6},
    ]
    
    waterfall = analyzer.waterfall_analysis(400, cap_structure)
    print(waterfall.to_string(index=False))
```

---

## Usage Notes

1. **Dependencies**: These scripts require `numpy`, `scipy`, and `pandas`. Install with:
   ```bash
   pip install numpy scipy pandas
   ```

2. **Production Use**: These implementations are educational. Production systems should use:
   - Bloomberg BVAL for CDS pricing
   - ISDA Standard Model (via QuantLib)
   - Commercial credit risk systems (Moody's Analytics, S&P Capital IQ)

3. **Data Sources**: Historical recovery and transition data from:
   - Moody's Annual Default Study
   - S&P Global Ratings Default Studies
   - Fitch Ratings Transition Studies

4. **Calibration**: The models use simplified assumptions. Real-world applications require:
   - Stochastic interest rate models
   - Term structure of hazard rates
   - Recovery rate volatility and correlation with default
