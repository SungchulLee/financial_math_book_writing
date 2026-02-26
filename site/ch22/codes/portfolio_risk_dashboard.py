"""
portfolio_risk_dashboard.py
Portfolio Risk Dashboard with Correlated Multi-Asset Simulation

This module implements a portfolio risk dashboard that demonstrates:
- Multi-asset Geometric Brownian Motion (GBM) simulation with Cholesky decomposition
- Correlated underlyings (e.g., equities, indices)
- European option pricing via Monte Carlo simulation
- Position-level present value (PV), delta, and vega computation
- Portfolio-level risk aggregation and visualization

The approach follows the DX Library's derivatives_portfolio methodology:
1. Define multiple correlated underlyings using GBM
2. Use Cholesky decomposition to generate correlated Brownian increments
3. Price European call/put options via Monte Carlo across all simulated paths
4. Compute Greeks using numerical bump-and-reprice methods
5. Aggregate position-level Greeks to portfolio level

Key Educational Concepts:
- Correlation matrix and Cholesky decomposition
- Multi-dimensional Monte Carlo sampling
- Numerical differentiation for Greeks estimation
- Portfolio risk aggregation

Author: Financial Math Book Series
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import norm
import warnings

warnings.filterwarnings('ignore')


class MultiAssetGBM:
    """
    Multi-asset Geometric Brownian Motion simulator with correlation structure.
    
    Simulates multiple correlated assets following GBM:
        dS_i / S_i = r dt + sigma_i dW_i
    
    Uses Cholesky decomposition to generate correlated Brownian increments.
    """
    
    def __init__(self, initial_prices, volatilities, correlation_matrix, 
                 risk_free_rate, time_horizon, num_steps=100, num_paths=10000):
        """
        Parameters:
        -----------
        initial_prices : array, shape (n_assets,)
            Initial spot prices for each asset
        volatilities : array, shape (n_assets,)
            Volatility (sigma) for each asset
        correlation_matrix : array, shape (n_assets, n_assets)
            Correlation matrix (must be positive semi-definite)
        risk_free_rate : float
            Risk-free interest rate
        time_horizon : float
            Total simulation time (years)
        num_steps : int, default 100
            Number of time steps in the simulation
        num_paths : int, default 10000
            Number of Monte Carlo paths
        """
        self.initial_prices = np.array(initial_prices, dtype=float)
        self.volatilities = np.array(volatilities, dtype=float)
        self.correlation_matrix = np.array(correlation_matrix, dtype=float)
        self.risk_free_rate = risk_free_rate
        self.time_horizon = time_horizon
        self.num_steps = num_steps
        self.num_paths = num_paths
        self.n_assets = len(initial_prices)
        
        # Compute Cholesky decomposition of correlation matrix
        try:
            self.cholesky_matrix = np.linalg.cholesky(self.correlation_matrix)
        except np.linalg.LinAlgError:
            raise ValueError("Correlation matrix is not positive semi-definite")
        
        self.dt = time_horizon / num_steps
        self.sqrt_dt = np.sqrt(self.dt)
        
    def generate_paths(self):
        """
        Generate Monte Carlo simulation paths for all assets.
        
        Returns:
        --------
        paths : array, shape (num_paths, num_steps + 1, n_assets)
            Simulated asset price paths
                paths[path_idx, time_step, asset_idx] = S_{i,t}(w)
        """
        paths = np.zeros((self.num_paths, self.num_steps + 1, self.n_assets))
        paths[:, 0, :] = self.initial_prices  # Initial prices
        
        for step in range(1, self.num_steps + 1):
            # Generate independent standard normal increments
            # Shape: (num_paths, n_assets)
            independent_normals = np.random.standard_normal((self.num_paths, self.n_assets))
            
            # Apply Cholesky decomposition to create correlated increments
            # independent_normals @ cholesky_matrix.T gives correlated normals
            correlated_normals = independent_normals @ self.cholesky_matrix.T
            
            # GBM update: S(t + dt) = S(t) * exp((r - sigma^2/2) * dt + sigma * sqrt(dt) * dW)
            drift = (self.risk_free_rate - 0.5 * self.volatilities ** 2) * self.dt
            diffusion = self.volatilities * self.sqrt_dt * correlated_normals
            
            paths[:, step, :] = paths[:, step - 1, :] * np.exp(drift + diffusion)
        
        return paths


class EuropeanOption:
    """
    European call and put option pricer using Monte Carlo simulation.
    """
    
    def __init__(self, option_type, strike, maturity, underlying_name):
        """
        Parameters:
        -----------
        option_type : {'call', 'put'}
            Type of option
        strike : float
            Strike price
        maturity : float
            Time to maturity (years)
        underlying_name : str
            Name of underlying asset (for identification)
        """
        self.option_type = option_type.lower()
        self.strike = strike
        self.maturity = maturity
        self.underlying_name = underlying_name
        
        if self.option_type not in ['call', 'put']:
            raise ValueError("option_type must be 'call' or 'put'")
    
    def payoff(self, spot_at_maturity):
        """
        Compute option payoff at maturity.
        
        Parameters:
        -----------
        spot_at_maturity : float or array
            Asset price at maturity
        
        Returns:
        --------
        payoff : float or array
            Option payoff
        """
        if self.option_type == 'call':
            return np.maximum(spot_at_maturity - self.strike, 0)
        else:  # put
            return np.maximum(self.strike - spot_at_maturity, 0)
    
    def price(self, spot, volatility, risk_free_rate, underlying_idx, paths):
        """
        Price option using Monte Carlo simulation.
        
        Parameters:
        -----------
        spot : float
            Current spot price
        volatility : float
            Volatility
        risk_free_rate : float
            Risk-free rate
        underlying_idx : int
            Index of underlying asset in the paths array
        paths : array, shape (num_paths, num_steps + 1, n_assets)
            Simulated asset price paths
        
        Returns:
        --------
        price : float
            Option price (discounted expected payoff)
        """
        # Terminal prices for the specified underlying
        terminal_prices = paths[:, -1, underlying_idx]
        
        # Compute payoffs at maturity for all paths
        payoffs = self.payoff(terminal_prices)
        
        # Discount to present value
        discount_factor = np.exp(-risk_free_rate * self.maturity)
        price = discount_factor * np.mean(payoffs)
        
        return price


class Portfolio:
    """
    Portfolio of multiple options on correlated underlyings.
    
    Manages position information, pricing, and Greeks computation.
    """
    
    def __init__(self, positions, multi_asset_gbm):
        """
        Parameters:
        -----------
        positions : list of dict
            Each dict contains:
            - 'option': EuropeanOption instance
            - 'underlying_idx': index of underlying asset in GBM
            - 'quantity': number of contracts
            - 'position_name': descriptive name
        multi_asset_gbm : MultiAssetGBM
            Multi-asset GBM simulator
        """
        self.positions = positions
        self.gbm = multi_asset_gbm
        self.prices = {}
        self.deltas = {}
        self.vegas = {}
        self.position_pvs = {}
    
    def price_all_positions(self, paths=None):
        """
        Price all positions in the portfolio.
        
        Parameters:
        -----------
        paths : array, optional
            Pre-computed paths. If None, generates new paths.
        
        Returns:
        --------
        portfolio_value : float
            Total portfolio value
        """
        if paths is None:
            paths = self.gbm.generate_paths()
        
        portfolio_value = 0.0
        
        for pos in self.positions:
            option = pos['option']
            underlying_idx = pos['underlying_idx']
            quantity = pos['quantity']
            pos_name = pos['position_name']
            
            # Price the option
            option_price = option.price(
                self.gbm.initial_prices[underlying_idx],
                self.gbm.volatilities[underlying_idx],
                self.gbm.risk_free_rate,
                underlying_idx,
                paths
            )
            
            # Store position results
            self.prices[pos_name] = option_price
            position_pv = option_price * quantity
            self.position_pvs[pos_name] = position_pv
            portfolio_value += position_pv
        
        return portfolio_value
    
    def compute_delta(self, position_name, bump_size=0.01, paths=None):
        """
        Compute delta for a position via numerical bump-and-reprice.
        
        Delta = dPrice / dSpot
        
        Parameters:
        -----------
        position_name : str
            Name of position
        bump_size : float
            Spot price bump size (in price units, not percentage)
        paths : array, optional
            Pre-computed paths for base scenario
        
        Returns:
        --------
        delta : float
            Position delta (per unit, before multiplying by quantity)
        """
        if paths is None:
            paths = self.gbm.generate_paths()
        
        # Find position
        pos = None
        for p in self.positions:
            if p['position_name'] == position_name:
                pos = p
                break
        
        if pos is None:
            raise ValueError(f"Position '{position_name}' not found")
        
        option = pos['option']
        underlying_idx = pos['underlying_idx']
        
        # Base price
        price_base = option.price(
            self.gbm.initial_prices[underlying_idx],
            self.gbm.volatilities[underlying_idx],
            self.gbm.risk_free_rate,
            underlying_idx,
            paths
        )
        
        # Bumped price (increase spot)
        gbm_bumped = MultiAssetGBM(
            self.gbm.initial_prices.copy(),
            self.gbm.volatilities,
            self.gbm.correlation_matrix,
            self.gbm.risk_free_rate,
            self.gbm.time_horizon,
            self.gbm.num_steps,
            self.gbm.num_paths
        )
        gbm_bumped.initial_prices[underlying_idx] += bump_size
        paths_bumped = gbm_bumped.generate_paths()
        
        price_bumped = option.price(
            gbm_bumped.initial_prices[underlying_idx],
            self.gbm.volatilities[underlying_idx],
            self.gbm.risk_free_rate,
            underlying_idx,
            paths_bumped
        )
        
        # Numerical delta
        delta = (price_bumped - price_base) / bump_size
        self.deltas[position_name] = delta
        
        return delta
    
    def compute_vega(self, position_name, bump_size=0.001, paths=None):
        """
        Compute vega for a position via numerical bump-and-reprice.
        
        Vega = dPrice / dVolatility
        
        Parameters:
        -----------
        position_name : str
            Name of position
        bump_size : float
            Volatility bump size (in absolute terms, e.g., 0.001 for 0.1%)
        paths : array, optional
            Pre-computed paths for base scenario
        
        Returns:
        --------
        vega : float
            Position vega per 1% change in volatility (scaled), per unit before quantity
        """
        if paths is None:
            paths = self.gbm.generate_paths()
        
        # Find position
        pos = None
        for p in self.positions:
            if p['position_name'] == position_name:
                pos = p
                break
        
        if pos is None:
            raise ValueError(f"Position '{position_name}' not found")
        
        option = pos['option']
        underlying_idx = pos['underlying_idx']
        
        # Base price
        price_base = option.price(
            self.gbm.initial_prices[underlying_idx],
            self.gbm.volatilities[underlying_idx],
            self.gbm.risk_free_rate,
            underlying_idx,
            paths
        )
        
        # Bumped price (increase volatility)
        gbm_bumped = MultiAssetGBM(
            self.gbm.initial_prices.copy(),
            self.gbm.volatilities.copy(),
            self.gbm.correlation_matrix,
            self.gbm.risk_free_rate,
            self.gbm.time_horizon,
            self.gbm.num_steps,
            self.gbm.num_paths
        )
        gbm_bumped.volatilities[underlying_idx] += bump_size
        paths_bumped = gbm_bumped.generate_paths()
        
        price_bumped = option.price(
            self.gbm.initial_prices[underlying_idx],
            gbm_bumped.volatilities[underlying_idx],
            self.gbm.risk_free_rate,
            underlying_idx,
            paths_bumped
        )
        
        # Numerical vega (typically quoted per 1% change in volatility)
        vega = (price_bumped - price_base) / bump_size / 100.0
        self.vegas[position_name] = vega
        
        return vega
    
    def summary(self):
        """
        Print portfolio risk summary table.
        """
        print("\n" + "=" * 100)
        print("PORTFOLIO RISK SUMMARY")
        print("=" * 100)
        print(f"{'Position Name':<25} {'Type':<6} {'Quantity':>10} {'Price':>12} {'PV':>12} {'Delta':>10} {'Vega':>10}")
        print("-" * 100)
        
        total_pv = 0.0
        total_delta = 0.0
        total_vega = 0.0
        
        for pos in self.positions:
            pos_name = pos['position_name']
            option_type = pos['option'].option_type[:4].upper()  # 'CALL' or 'PUT '
            quantity = pos['quantity']
            
            price = self.prices.get(pos_name, np.nan)
            pv = self.position_pvs.get(pos_name, np.nan)
            delta = self.deltas.get(pos_name, np.nan)
            vega = self.vegas.get(pos_name, np.nan)
            
            print(f"{pos_name:<25} {option_type:<6} {quantity:>10.0f} {price:>12.4f} {pv:>12.2f} {delta:>10.4f} {vega:>10.4f}")
            
            total_pv += pv
            total_delta += delta * quantity
            total_vega += vega * quantity
        
        print("-" * 100)
        print(f"{'PORTFOLIO TOTAL':<25} {'':<6} {'':<10} {'':<12} {total_pv:>12.2f} {total_delta:>10.4f} {total_vega:>10.4f}")
        print("=" * 100)


def visualize_results(gbm, portfolio, paths):
    """
    Generate visualization plots for portfolio risk dashboard.
    
    Plots:
    1. Correlation heatmap
    2. Portfolio value distribution (histogram of path-wise PVs)
    3. Greeks bar chart
    
    Parameters:
    -----------
    gbm : MultiAssetGBM
        Multi-asset GBM simulator
    portfolio : Portfolio
        Portfolio instance
    paths : array
        Simulated asset price paths
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Portfolio Risk Dashboard', fontsize=16, fontweight='bold')
    
    # Plot 1: Correlation matrix heatmap
    ax = axes[0, 0]
    im = ax.imshow(gbm.correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    ax.set_xticks(range(gbm.n_assets))
    ax.set_yticks(range(gbm.n_assets))
    ax.set_xticklabels([f'Asset {i}' for i in range(gbm.n_assets)])
    ax.set_yticklabels([f'Asset {i}' for i in range(gbm.n_assets)])
    ax.set_title('Correlation Matrix')
    
    # Add correlation values to heatmap
    for i in range(gbm.n_assets):
        for j in range(gbm.n_assets):
            text = ax.text(j, i, f'{gbm.correlation_matrix[i, j]:.2f}',
                          ha="center", va="center", color="black", fontsize=10)
    
    plt.colorbar(im, ax=ax)
    
    # Plot 2: Simulated spot prices over time
    ax = axes[0, 1]
    for asset_idx in range(gbm.n_assets):
        time_grid = np.linspace(0, gbm.time_horizon, gbm.num_steps + 1)
        for path_idx in range(min(100, gbm.num_paths)):  # Plot first 100 paths for clarity
            ax.plot(time_grid, paths[path_idx, :, asset_idx], alpha=0.1, linewidth=0.5)
        
        # Plot mean path
        mean_path = np.mean(paths[:, :, asset_idx], axis=0)
        ax.plot(time_grid, mean_path, linewidth=2, label=f'Asset {asset_idx} (mean)')
    
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Spot Price')
    ax.set_title('Simulated Asset Price Paths')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Greeks bar chart
    ax = axes[1, 0]
    position_names = list(portfolio.deltas.keys())
    deltas = list(portfolio.deltas.values())
    
    x_pos = np.arange(len(position_names))
    bars = ax.bar(x_pos - 0.2, deltas, 0.4, label='Delta', alpha=0.8)
    
    # Normalize vega for visualization (scale by 10 for visibility)
    vegas_scaled = [v * 10 for v in portfolio.vegas.values()]
    bars = ax.bar(x_pos + 0.2, vegas_scaled, 0.4, label='Vega (x10)', alpha=0.8)
    
    ax.set_xlabel('Position')
    ax.set_ylabel('Greek Value')
    ax.set_title('Position Greeks')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(position_names, rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Position values bar chart
    ax = axes[1, 1]
    position_names = list(portfolio.position_pvs.keys())
    pvs = list(portfolio.position_pvs.values())
    
    colors = ['green' if pv > 0 else 'red' for pv in pvs]
    bars = ax.bar(position_names, pvs, color=colors, alpha=0.7)
    
    # Add value labels on bars
    for bar, pv in zip(bars, pvs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'${pv:.2f}',
               ha='center', va='bottom' if pv > 0 else 'top', fontsize=9)
    
    ax.set_xlabel('Position')
    ax.set_ylabel('Present Value ($)')
    ax.set_title('Position Values')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3, axis='y')
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    return fig


def main():
    """
    Main function demonstrating portfolio risk dashboard.
    """
    print("\n" + "=" * 100)
    print("PORTFOLIO RISK DASHBOARD - Multi-Asset Correlated Simulation")
    print("=" * 100)
    
    # =========================================================================
    # SETUP: Define three correlated underlyings
    # =========================================================================
    print("\n[1] Setting up multi-asset environment...")
    
    # Three underlyings: Equity A (S=100, sigma=0.20), 
    #                    Equity B (S=95, sigma=0.25),
    #                    Index (S=3000, sigma=0.15)
    initial_prices = np.array([100.0, 95.0, 3000.0])
    volatilities = np.array([0.20, 0.25, 0.15])
    
    # Correlation matrix: Equity A and B are correlated (0.6),
    #                     both correlated with Index (0.5 and 0.4)
    correlation_matrix = np.array([
        [1.0,  0.6,  0.5],   # Equity A
        [0.6,  1.0,  0.4],   # Equity B
        [0.5,  0.4,  1.0]    # Index
    ])
    
    risk_free_rate = 0.05
    time_horizon = 1.0  # 1 year
    num_paths = 10000
    num_steps = 252  # Daily steps (roughly 252 trading days per year)
    
    # Create GBM simulator
    gbm = MultiAssetGBM(
        initial_prices=initial_prices,
        volatilities=volatilities,
        correlation_matrix=correlation_matrix,
        risk_free_rate=risk_free_rate,
        time_horizon=time_horizon,
        num_steps=num_steps,
        num_paths=num_paths
    )
    
    print(f"  - Number of assets: {gbm.n_assets}")
    print(f"  - Initial prices: {initial_prices}")
    print(f"  - Volatilities: {volatilities}")
    print(f"  - Risk-free rate: {risk_free_rate:.2%}")
    print(f"  - Time horizon: {time_horizon} year(s)")
    print(f"  - Monte Carlo paths: {num_paths}")
    
    print("\n  Correlation Matrix:")
    print("  " + str(correlation_matrix).replace('\n', '\n  '))
    
    # =========================================================================
    # GENERATE PATHS
    # =========================================================================
    print("\n[2] Generating Monte Carlo paths...")
    paths = gbm.generate_paths()
    print(f"  - Paths shape: {paths.shape}")
    print(f"  - Terminal prices (sample): Asset 0: {paths[0, -1, 0]:.2f}, "
          f"Asset 1: {paths[0, -1, 1]:.2f}, Asset 2: {paths[0, -1, 2]:.2f}")
    
    # =========================================================================
    # DEFINE PORTFOLIO POSITIONS
    # =========================================================================
    print("\n[3] Building portfolio...")
    
    # Create options
    opt1 = EuropeanOption(option_type='call', strike=105.0, 
                         maturity=time_horizon, underlying_name='Asset 0')
    opt2 = EuropeanOption(option_type='call', strike=100.0, 
                         maturity=time_horizon, underlying_name='Asset 1')
    opt3 = EuropeanOption(option_type='put', strike=3000.0, 
                         maturity=time_horizon, underlying_name='Asset 2')
    opt4 = EuropeanOption(option_type='call', strike=3100.0, 
                         maturity=time_horizon, underlying_name='Asset 2')
    
    positions = [
        {
            'option': opt1,
            'underlying_idx': 0,
            'quantity': 100,
            'position_name': 'Long Call A'
        },
        {
            'option': opt2,
            'underlying_idx': 1,
            'quantity': 150,
            'position_name': 'Long Call B'
        },
        {
            'option': opt3,
            'underlying_idx': 2,
            'quantity': 50,
            'position_name': 'Long Put Index'
        },
        {
            'option': opt4,
            'underlying_idx': 2,
            'quantity': -30,
            'position_name': 'Short Call Index'
        }
    ]
    
    portfolio = Portfolio(positions, gbm)
    print(f"  - Number of positions: {len(positions)}")
    for pos in positions:
        print(f"    • {pos['position_name']}: {pos['quantity']:+.0f}x {pos['option'].option_type.upper()} "
              f"strike={pos['option'].strike:.0f}")
    
    # =========================================================================
    # PRICE PORTFOLIO
    # =========================================================================
    print("\n[4] Pricing portfolio positions...")
    portfolio_value = portfolio.price_all_positions(paths)
    print(f"  - Total portfolio value: ${portfolio_value:,.2f}")
    
    for pos in positions:
        pos_name = pos['position_name']
        price = portfolio.prices[pos_name]
        pv = portfolio.position_pvs[pos_name]
        print(f"    • {pos_name:20s}: ${price:>7.2f} x {pos['quantity']:>3.0f} = ${pv:>10.2f}")
    
    # =========================================================================
    # COMPUTE GREEKS
    # =========================================================================
    print("\n[5] Computing position Greeks...")
    
    for pos in positions:
        pos_name = pos['position_name']
        print(f"  - {pos_name:20s}... ", end='', flush=True)
        
        delta = portfolio.compute_delta(pos_name, bump_size=0.50, paths=paths)
        vega = portfolio.compute_vega(pos_name, bump_size=0.001, paths=paths)
        
        print(f"delta={delta:>7.4f}, vega={vega:>7.4f}")
    
    # Compute portfolio-level aggregates
    total_delta = sum(portfolio.deltas[pos['position_name']] * pos['quantity'] 
                     for pos in positions)
    total_vega = sum(portfolio.vegas[pos['position_name']] * pos['quantity'] 
                    for pos in positions)
    
    print(f"\n  Portfolio-level Greeks:")
    print(f"    • Total Delta: {total_delta:>7.4f}")
    print(f"    • Total Vega:  {total_vega:>7.4f}")
    
    # =========================================================================
    # PRINT SUMMARY TABLE
    # =========================================================================
    portfolio.summary()
    
    # =========================================================================
    # VISUALIZE RESULTS
    # =========================================================================
    print("\n[6] Generating visualizations...")
    fig = visualize_results(gbm, portfolio, paths)
    
    # Save figure
    figure_path = '/sessions/serene-kind-hopper/mnt/financial_math_book_writing/docs/ch22/codes/portfolio_dashboard.png'
    plt.savefig(figure_path, dpi=150, bbox_inches='tight')
    print(f"  - Figure saved to: {figure_path}")
    
    # =========================================================================
    # INTERPRETATION AND INSIGHTS
    # =========================================================================
    print("\n" + "=" * 100)
    print("KEY INSIGHTS")
    print("=" * 100)
    
    print("""
The portfolio risk dashboard demonstrates several key concepts in derivatives pricing:

1. CORRELATION & CHOLESKY DECOMPOSITION
   - Three correlated underlyings are simulated using the Cholesky decomposition
   - This ensures generated paths respect the specified correlation structure
   - Correlation: Asset A-B: 0.60, Asset A-Index: 0.50, Asset B-Index: 0.40

2. MONTE CARLO PRICING
   - Each option is priced via the discounted expected payoff under risk-neutral dynamics
   - 10,000 paths × 252 steps provides robust statistical estimates
   - Option values = E[discount * payoff]

3. POSITION-LEVEL GREEKS
   - Delta: Sensitivity to changes in underlying spot price ($0.50 bump)
   - Vega: Sensitivity to changes in underlying volatility (0.1% bump)
   - Computed via numerical bump-and-reprice (standard in industry practice)

4. PORTFOLIO AGGREGATION
   - Individual position Greeks are scaled by quantity and summed
   - Total Delta = {:.4f} (net directional exposure)
   - Total Vega = {:.4f} (net volatility exposure)

5. RISK DASHBOARD
   - Correlation matrix shows which assets move together
   - Simulated paths validate the GBM model and correlations
   - Greek bars reveal which positions drive portfolio sensitivity
   - Position values break down portfolio composition

This approach is foundational for:
- Risk management and hedging decisions
- Value-at-Risk (VaR) and Expected Shortfall (ES) calculations
- Portfolio rebalancing and Greeks monitoring
- Regulatory capital requirements (e.g., FRTB, SIMM)
    """.format(total_delta, total_vega))
    
    print("=" * 100)
    print("[COMPLETE] Portfolio Risk Dashboard Analysis\n")
    
    return portfolio, gbm, paths


if __name__ == '__main__':
    portfolio, gbm, paths = main()
