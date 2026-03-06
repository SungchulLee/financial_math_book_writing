"""
Sma Trading Strategy

Educational script demonstrating sma trading strategy concepts.
"""

# ---
# title: "Simple Moving Average (SMA) Trading Strategy"
# description: >
#   Implements and backtests a dual-SMA crossover strategy:
#     - Go LONG  when SMA_short > SMA_long  (uptrend signal).
#     - Go SHORT when SMA_short < SMA_long  (downtrend signal).
#   Includes vectorised backtesting, cumulative performance plots,
#   and a grid search over SMA window pairs to find the
#   combination that maximises out-of-sample strategy return.
#
#   Also briefly demonstrates the random-walk hypothesis via
#   lagged auto-regression of S&P 500 levels.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import product


# ======================================================================
# ── Synthetic price series for stand-alone use ────────────────────
def generate_gbm_prices(S0=100, mu=0.08, sigma=0.20,
                        T=8.0, dt=1/252, seed=42):
    """Generate a realistic daily equity price series via GBM.

    Returns a DataFrame with DatetimeIndex and column 'Price'.
    """
    np.random.seed(seed)
    n_steps = int(T / dt)
    dates = pd.bdate_range(start='2010-01-04', periods=n_steps)
    z = np.random.standard_normal(n_steps)
    log_returns = (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z
    prices = S0 * np.exp(np.cumsum(log_returns))
    return pd.DataFrame({'Price': prices}, index=dates)


# ── SMA strategy backtest ─────────────────────────────────────────
def sma_backtest(data, price_col, sma_short=42, sma_long=252):
    """Vectorised SMA crossover backtest.

    Parameters
    ----------
    data : DataFrame
        Must contain *price_col*.
    price_col : str
        Column name for the price series.
    sma_short, sma_long : int
        Window sizes for the short and long moving averages.

    Returns
    -------
    result : DataFrame
        Original data augmented with SMA1, SMA2, Position,
        Returns, Strategy columns.
    """
    df = data[[price_col]].copy()
    df['SMA1'] = df[price_col].rolling(sma_short).mean()
    df['SMA2'] = df[price_col].rolling(sma_long).mean()
    df.dropna(inplace=True)

    # Signal: +1 long, -1 short
    df['Position'] = np.where(df['SMA1'] > df['SMA2'], 1, -1)

    # Log-returns
    df['Returns'] = np.log(df[price_col] / df[price_col].shift(1))

    # Strategy return = position entered yesterday × today's return
    df['Strategy'] = df['Position'].shift(1) * df['Returns']
    df.dropna(inplace=True)

    return df


# ── Grid search over SMA window pairs ────────────────────────────
def sma_grid_search(data, price_col,
                    sma1_range=range(20, 61, 4),
                    sma2_range=range(180, 281, 10)):
    """Brute-force search for the best (SMA1, SMA2) pair.

    Returns
    -------
    results : DataFrame
        Columns: SMA1, SMA2, MARKET, STRATEGY, OUT.
    """
    rows = []
    for sma1, sma2 in product(sma1_range, sma2_range):
        df = sma_backtest(data, price_col, sma1, sma2)
        if len(df) == 0:
            continue
        perf = np.exp(df[['Returns', 'Strategy']].sum())
        rows.append({
            'SMA1': sma1, 'SMA2': sma2,
            'MARKET': perf['Returns'],
            'STRATEGY': perf['Strategy'],
            'OUT': perf['Strategy'] - perf['Returns'],
        })
    return pd.DataFrame(rows)


# ── Random-walk test via lagged auto-regression ───────────────────
def random_walk_test(data, price_col, lags=5):
    """Regress price on its own lags via OLS (normal equations).

    Under the random-walk hypothesis, only the first lag coefficient
    should be close to 1 and the rest near zero.

    Returns
    -------
    coefficients : ndarray
        OLS regression coefficients for lag_1 … lag_n.
    """
    df = data[[price_col]].copy()
    cols = []
    for lag in range(1, lags + 1):
        col = f'lag_{lag}'
        df[col] = df[price_col].shift(lag)
        cols.append(col)
    df.dropna(inplace=True)
    coeffs = np.linalg.lstsq(df[cols].values,
                              df[price_col].values, rcond=-1)[0]
    return cols, coeffs


# ── Main ──────────────────────────────────────────────────────────
if __name__ == '__main__':

    # Generate synthetic equity data
    data = generate_gbm_prices()
    price_col = 'Price'

    # ────────────────────────────────────────────────────────────
    # 1. Single SMA backtest
    # ────────────────────────────────────────────────────────────
    SMA1, SMA2 = 42, 252
    bt = sma_backtest(data, price_col, SMA1, SMA2)

    cumret = np.exp(bt[['Returns', 'Strategy']].cumsum())
    print("Cumulative return (buy-and-hold):",
          round(cumret['Returns'].iloc[-1], 4))
    print("Cumulative return (SMA strategy):",
          round(cumret['Strategy'].iloc[-1], 4))
    print("Annualised vol  (buy-and-hold):",
          round(bt['Returns'].std() * 252 ** 0.5, 4))
    print("Annualised vol  (SMA strategy):",
          round(bt['Strategy'].std() * 252 ** 0.5, 4))

    # Plot price with SMAs
    fig, ax = plt.subplots(figsize=(10, 6))
    bt[[price_col, 'SMA1', 'SMA2']].plot(ax=ax)
    ax.set_ylabel('Price')
    ax.set_title(f'SMA Crossover ({SMA1} / {SMA2})')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Cumulative performance
    fig, ax = plt.subplots(figsize=(10, 6))
    cumret.plot(ax=ax)
    bt['Position'].plot(ax=ax, secondary_y='Position', style='--',
                        alpha=0.5)
    ax.set_ylabel('Cumulative return (×)')
    ax.set_title('Strategy vs Buy-and-Hold')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ────────────────────────────────────────────────────────────
    # 2. Grid search
    # ────────────────────────────────────────────────────────────
    results = sma_grid_search(data, price_col)
    best = results.sort_values('OUT', ascending=False).head(7)
    print("\nTop SMA combinations:")
    print(best.to_string(index=False))

    # ────────────────────────────────────────────────────────────
    # 3. Random-walk regression
    # ────────────────────────────────────────────────────────────
    cols, coeffs = random_walk_test(data, price_col, lags=5)
    print("\nRandom-walk regression coefficients:")
    for c, v in zip(cols, coeffs):
        print(f"  {c}: {v:.4f}")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(cols, coeffs)
    ax.set_ylabel('Coefficient')
    ax.set_title('Lagged Auto-Regression Coefficients')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
