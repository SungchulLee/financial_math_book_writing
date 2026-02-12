# ============================================================================
# stock_analysis/visualization/candlestick.py
# ============================================================================
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Optional, Tuple, List, Dict
try:
    import mplfinance as mpf
    HAS_MPLFINANCE = True
except ImportError:
    HAS_MPLFINANCE = False


def plot_ohlc_with_ma(df: pd.DataFrame, ticker: str, 
                      ma_windows: List[int] = [5, 10, 20, 60],
                      company_name: Optional[str] = None,
                      figsize: Tuple[int, int] = (14, 8)) -> None:
    """
    Plot OHLC candlestick chart with moving averages using mplfinance.
    
    Args:
        df: DataFrame with OHLC data (Open, High, Low, Close, Volume)
        ticker: Stock ticker symbol
        ma_windows: List of moving average window sizes
        company_name: Optional company name for title
        figsize: Figure size tuple (width, height)
    """
    if not HAS_MPLFINANCE:
        raise ImportError("mplfinance is required for candlestick plots. Install with: pip install mplfinance")
    
    required_cols = ['Open', 'High', 'Low', 'Close']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain OHLC columns: {missing_cols}")
    
    # Prepare data for mplfinance
    df_plot = df[['Open', 'High', 'Low', 'Close']].copy()
    if 'Volume' in df.columns:
        df_plot['Volume'] = df['Volume']
    
    # Ensure index is named 'Date' for mplfinance
    df_plot.index.name = 'Date'
    
    # Create title
    title = f'{ticker if company_name is None else company_name} OHLC with Moving Averages'
    
    # Custom style
    mc = mpf.make_marketcolors(
        up='#26A69A',      # Green for up candles
        down='#EF5350',    # Red for down candles
        edge='inherit',
        wick={'up': '#26A69A', 'down': '#EF5350'},
        volume='in'
    )
    
    style = mpf.make_mpf_style(
        marketcolors=mc,
        gridstyle='-',
        gridcolor='#E0E0E0',
        facecolor='white',
        figcolor='white'
    )
    
    # Plot with moving averages and volume
    mpf.plot(df_plot,
             type='candle',
             style=style,
             mav=ma_windows,
             volume=True if 'Volume' in df_plot.columns else False,
             title=title,
             ylabel='Price ($)',
             ylabel_lower='Volume' if 'Volume' in df_plot.columns else None,
             figratio=figsize,
             figscale=1.0)


def plot_candlestick_matplotlib(df: pd.DataFrame, ticker: str,
                               figsize: Tuple[int, int] = (12, 6),
                               max_candles: int = 100) -> None:
    """
    Plot candlestick chart using matplotlib (fallback when mplfinance not available).
    
    Args:
        df: DataFrame with OHLC data
        ticker: Stock ticker symbol
        figsize: Figure size tuple (width, height)
        max_candles: Maximum number of candles to display for readability
    """
    required_cols = ['Open', 'High', 'Low', 'Close']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain OHLC columns: {missing_cols}")
    
    # Limit data for readability
    if len(df) > max_candles:
        df = df.tail(max_candles)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create x-axis positions
    x_pos = np.arange(len(df))
    
    # Determine up and down days
    up_days = df['Close'] >= df['Open']
    down_days = df['Close'] < df['Open']
    
    # Colors
    up_color = '#26A69A'
    down_color = '#EF5350'
    
    # Plot wicks (high-low lines)
    ax.vlines(x_pos, df['Low'], df['High'], colors='black', linewidth=0.8)
    
    # Plot candle bodies
    candle_width = 0.6
    
    # Up candles (green)
    if up_days.any():
        ax.bar(x_pos[up_days], 
               df.loc[up_days, 'Close'] - df.loc[up_days, 'Open'],
               bottom=df.loc[up_days, 'Open'],
               width=candle_width,
               color=up_color,
               alpha=0.8)
    
    # Down candles (red)
    if down_days.any():
        ax.bar(x_pos[down_days], 
               df.loc[down_days, 'Open'] - df.loc[down_days, 'Close'],
               bottom=df.loc[down_days, 'Close'],
               width=candle_width,
               color=down_color,
               alpha=0.8)
    
    # Formatting
    ax.set_title(f'{ticker} Candlestick Chart', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Price ($)', fontsize=12)
    ax.set_xlabel('Date', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # Set x-axis labels (sample every nth label to avoid crowding)
    step = max(1, len(df) // 10)
    x_labels = [df.index[i].strftime('%Y-%m-%d') for i in range(0, len(df), step)]
    x_positions = list(range(0, len(df), step))
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels, rotation=45, ha='right')
    
    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.show()


def plot_candlestick_with_indicators(df: pd.DataFrame, ticker: str,
                                   rsi_window: int = 14,
                                   macd_fast: int = 12,
                                   macd_slow: int = 26,
                                   macd_signal: int = 9,
                                   figsize: Tuple[int, int] = (14, 10)) -> None:
    """
    Plot candlestick chart with technical indicators (RSI, MACD).
    
    Args:
        df: DataFrame with OHLC data
        ticker: Stock ticker symbol
        rsi_window: RSI calculation window
        macd_fast: MACD fast EMA period
        macd_slow: MACD slow EMA period
        macd_signal: MACD signal line EMA period
        figsize: Figure size tuple (width, height)
    """
    if not HAS_MPLFINANCE:
        # Fallback to basic candlestick
        print("mplfinance not available. Displaying basic candlestick chart.")
        plot_candlestick_matplotlib(df, ticker, figsize)
        return
    
    required_cols = ['Open', 'High', 'Low', 'Close']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain OHLC columns: {missing_cols}")
    
    # Calculate technical indicators
    df_with_indicators = df.copy()
    
    # RSI calculation
    delta = df_with_indicators['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_window).mean()
    rs = gain / loss
    df_with_indicators['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD calculation
    ema_fast = df_with_indicators['Close'].ewm(span=macd_fast).mean()
    ema_slow = df_with_indicators['Close'].ewm(span=macd_slow).mean()
    df_with_indicators['MACD'] = ema_fast - ema_slow
    df_with_indicators['MACD_Signal'] = df_with_indicators['MACD'].ewm(span=macd_signal).mean()
    df_with_indicators['MACD_Histogram'] = df_with_indicators['MACD'] - df_with_indicators['MACD_Signal']
    
    # Prepare for mplfinance
    df_plot = df_with_indicators[['Open', 'High', 'Low', 'Close']].copy()
    if 'Volume' in df_with_indicators.columns:
        df_plot['Volume'] = df_with_indicators['Volume']
    
    # Create additional plots for indicators
    apds = [
        mpf.make_addplot(df_with_indicators['RSI'], panel=1, color='purple', ylabel='RSI'),
        mpf.make_addplot(df_with_indicators['MACD'], panel=2, color='blue', ylabel='MACD'),
        mpf.make_addplot(df_with_indicators['MACD_Signal'], panel=2, color='red'),
        mpf.make_addplot(df_with_indicators['MACD_Histogram'], panel=2, type='bar', color='gray', alpha=0.3)
    ]
    
    # Custom style
    mc = mpf.make_marketcolors(
        up='#26A69A',
        down='#EF5350',
        edge='inherit',
        wick={'up': '#26A69A', 'down': '#EF5350'},
        volume='in'
    )
    
    style = mpf.make_mpf_style(
        marketcolors=mc,
        gridstyle='-',
        gridcolor='#E0E0E0',
        facecolor='white',
        figcolor='white'
    )
    
    # Plot with indicators
    mpf.plot(df_plot,
             type='candle',
             style=style,
             addplot=apds,
             volume=True if 'Volume' in df_plot.columns else False,
             title=f'{ticker} with Technical Indicators',
             figratio=figsize,
             figscale=1.0,
             panel_ratios=(3, 1, 1))


def plot_volume_profile(df: pd.DataFrame, ticker: str,
                       bins: int = 50,
                       figsize: Tuple[int, int] = (12, 8)) -> None:
    """
    Plot price with volume profile (volume at price levels).
    
    Args:
        df: DataFrame with Close and Volume columns
        ticker: Stock ticker symbol
        bins: Number of price bins for volume profile
        figsize: Figure size tuple (width, height)
    """
    required_cols = ['Close', 'Volume']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain columns: {missing_cols}")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize, 
                                   gridspec_kw={'width_ratios': [3, 1]},
                                   sharey=True)
    
    # Price chart
    ax1.plot(df.index, df['Close'], linewidth=1.5, color='#2E86AB')
    ax1.set_title(f'{ticker} Price with Volume Profile', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Volume profile
    price_min, price_max = df['Close'].min(), df['Close'].max()
    price_bins = np.linspace(price_min, price_max, bins)
    
    # Calculate volume at each price level
    volume_profile = []
    for i in range(len(price_bins) - 1):
        mask = (df['Close'] >= price_bins[i]) & (df['Close'] < price_bins[i + 1])
        volume_at_level = df.loc[mask, 'Volume'].sum()
        volume_profile.append(volume_at_level)
    
    # Plot volume profile as horizontal bars
    bin_centers = (price_bins[:-1] + price_bins[1:]) / 2
    ax2.barh(bin_centers, volume_profile, height=(price_max - price_min) / bins * 0.8,
             alpha=0.7, color='#A23B72')
    ax2.set_xlabel('Volume', fontsize=12)
    ax2.set_title('Volume Profile', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.show()


def plot_heikin_ashi(df: pd.DataFrame, ticker: str,
                     figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot Heikin-Ashi candlestick chart.
    
    Args:
        df: DataFrame with OHLC data
        ticker: Stock ticker symbol
        figsize: Figure size tuple (width, height)
    """
    required_cols = ['Open', 'High', 'Low', 'Close']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain OHLC columns: {missing_cols}")
    
    # Calculate Heikin-Ashi values
    ha_df = df.copy()
    
    # HA Close = (O + H + L + C) / 4
    ha_df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    
    # HA Open = (previous HA Open + previous HA Close) / 2
    ha_df['HA_Open'] = 0.0
    ha_df.iloc[0, ha_df.columns.get_loc('HA_Open')] = (df['Open'].iloc[0] + df['Close'].iloc[0]) / 2
    
    for i in range(1, len(ha_df)):
        ha_df.iloc[i, ha_df.columns.get_loc('HA_Open')] = (
            ha_df.iloc[i-1, ha_df.columns.get_loc('HA_Open')] + 
            ha_df.iloc[i-1, ha_df.columns.get_loc('HA_Close')]
        ) / 2
    
    # HA High = max(H, HA Open, HA Close)
    ha_df['HA_High'] = ha_df[['High', 'HA_Open', 'HA_Close']].max(axis=1)
    
    # HA Low = min(L, HA Open, HA Close)
    ha_df['HA_Low'] = ha_df[['Low', 'HA_Open', 'HA_Close']].min(axis=1)
    
    if HAS_MPLFINANCE:
        # Use mplfinance for better visualization
        ha_plot_df = ha_df[['HA_Open', 'HA_High', 'HA_Low', 'HA_Close']].copy()
        ha_plot_df.columns = ['Open', 'High', 'Low', 'Close']
        
        mc = mpf.make_marketcolors(up='#26A69A', down='#EF5350', edge='inherit')
        style = mpf.make_mpf_style(marketcolors=mc, gridstyle='-', gridcolor='#E0E0E0')
        
        mpf.plot(ha_plot_df,
                 type='candle',
                 style=style,
                 title=f'{ticker} Heikin-Ashi Chart',
                 figratio=figsize)
    else:
        # Fallback to matplotlib
        fig, ax = plt.subplots(figsize=figsize)
        
        # Use the matplotlib candlestick function with HA data
        ha_plot_df = ha_df[['HA_Open', 'HA_High', 'HA_Low', 'HA_Close']].copy()
        ha_plot_df.columns = ['Open', 'High', 'Low', 'Close']
        
        # Limit data for readability
        if len(ha_plot_df) > 100:
            ha_plot_df = ha_plot_df.tail(100)
        
        x_pos = np.arange(len(ha_plot_df))
        up_days = ha_plot_df['Close'] >= ha_plot_df['Open']
        down_days = ha_plot_df['Close'] < ha_plot_df['Open']
        
        # Plot wicks and bodies
        ax.vlines(x_pos, ha_plot_df['Low'], ha_plot_df['High'], colors='black', linewidth=0.8)
        
        if up_days.any():
            ax.bar(x_pos[up_days], 
                   ha_plot_df.loc[up_days, 'Close'] - ha_plot_df.loc[up_days, 'Open'],
                   bottom=ha_plot_df.loc[up_days, 'Open'],
                   width=0.6, color='#26A69A', alpha=0.8)
        
        if down_days.any():
            ax.bar(x_pos[down_days], 
                   ha_plot_df.loc[down_days, 'Open'] - ha_plot_df.loc[down_days, 'Close'],
                   bottom=ha_plot_df.loc[down_days, 'Close'],
                   width=0.6, color='#EF5350', alpha=0.8)
        
        ax.set_title(f'{ticker} Heikin-Ashi Chart', fontsize=16, fontweight='bold')
        ax.set_ylabel('Price ($)', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()