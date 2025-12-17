# ============================================================================
# stock_analysis_OPTION_DATA_SPY.py
# ============================================================================
import yfinance as yf
import matplotlib.pyplot as plt

# Parameters
ticker = "SPY"
spy = yf.Ticker(ticker)
option_maturities = spy.options
filtering_volume_level = 200

# Get current SPY price
current_price = spy.info["regularMarketPrice"]

for option_maturity in option_maturities[:7]:
    option_chain = spy.option_chain(option_maturity)
    calls = option_chain.calls
    puts = option_chain.puts

    # Filter liquid options
    calls = calls[calls['volume'] >= filtering_volume_level].dropna()
    puts = puts[puts['volume'] >= filtering_volume_level].dropna()

    # Create figure with 3 subplots
    fig = plt.figure(figsize=(14, 9))
    gs = fig.add_gridspec(2, 2, height_ratios=[2.5, 1])
    ax_call = fig.add_subplot(gs[0, 0])
    ax_put = fig.add_subplot(gs[0, 1])
    ax_iv_compare = fig.add_subplot(gs[1, :])
    fig.suptitle(f'{ticker} Options Expiring {option_maturity}', fontsize=16)

    # --- CALL AXES ---
    strikes_call = calls['strike']
    last_price_call = calls['lastPrice']
    bid_call = calls['bid']
    ask_call = calls['ask']
    iv_call = calls['impliedVolatility']
    volume_call = calls['volume']

    ax_call.plot(strikes_call, last_price_call, color='tab:blue', label='Last Price')
    ax_call.fill_between(strikes_call, bid_call, ask_call, color='tab:blue', alpha=0.2, label='Bid-Ask Range')
    ax_call.set_xlabel('Strike Price')
    ax_call.set_ylabel('Price ($)', color='tab:blue')
    ax_call.tick_params(axis='y', labelcolor='tab:blue')
    ax_call.set_title(f'Call Options (Volume ≥ {filtering_volume_level})')
    ax_call.grid(True)

    iv_axis_call = ax_call.twinx()
    iv_axis_call.plot(strikes_call, iv_call, color='tab:red', label='Implied Volatility')
    iv_axis_call.set_ylabel('Implied Volatility', color='tab:red')
    iv_axis_call.tick_params(axis='y', labelcolor='tab:red')

    vol_axis_call = ax_call.twinx()
    vol_axis_call.spines["right"].set_position(("axes", 1.12))
    vol_axis_call.bar(strikes_call, volume_call, width=1.5, color='gray', alpha=0.3, label='Volume')
    vol_axis_call.set_ylabel('Volume', color='gray', labelpad=15)
    vol_axis_call.tick_params(axis='y', colors='gray')

    # --- PUT AXES ---
    strikes_put = puts['strike']
    last_price_put = puts['lastPrice']
    bid_put = puts['bid']
    ask_put = puts['ask']
    iv_put = puts['impliedVolatility']
    volume_put = puts['volume']

    ax_put.plot(strikes_put, last_price_put, color='tab:blue', label='Last Price')
    ax_put.fill_between(strikes_put, bid_put, ask_put, color='tab:blue', alpha=0.2, label='Bid-Ask Range')
    ax_put.set_xlabel('Strike Price')
    ax_put.set_ylabel('Price ($)', color='tab:blue')
    ax_put.tick_params(axis='y', labelcolor='tab:blue')
    ax_put.set_title(f'Put Options (Volume ≥ {filtering_volume_level})')
    ax_put.grid(True)

    iv_axis_put = ax_put.twinx()
    iv_axis_put.plot(strikes_put, iv_put, color='tab:red', label='Implied Volatility')
    iv_axis_put.set_ylabel('Implied Volatility', color='tab:red')
    iv_axis_put.tick_params(axis='y', labelcolor='tab:red')

    vol_axis_put = ax_put.twinx()
    vol_axis_put.spines["right"].set_position(("axes", 1.12))
    vol_axis_put.bar(strikes_put, volume_put, width=1.5, color='gray', alpha=0.3, label='Volume')
    vol_axis_put.set_ylabel('Volume', color='gray', labelpad=15)
    vol_axis_put.tick_params(axis='y', colors='gray')

    # --- Synchronize all y-axes ---
    price_min = min(ax_call.get_ylim()[0], ax_put.get_ylim()[0])
    price_max = max(ax_call.get_ylim()[1], ax_put.get_ylim()[1])
    ax_call.set_ylim(price_min, price_max)
    ax_put.set_ylim(price_min, price_max)

    iv_min = min(iv_axis_call.get_ylim()[0], iv_axis_put.get_ylim()[0])
    iv_max = max(iv_axis_call.get_ylim()[1], iv_axis_put.get_ylim()[1])
    iv_axis_call.set_ylim(iv_min, iv_max)
    iv_axis_put.set_ylim(iv_min, iv_max)

    vol_min = min(vol_axis_call.get_ylim()[0], vol_axis_put.get_ylim()[0])
    vol_max = max(vol_axis_call.get_ylim()[1], vol_axis_put.get_ylim()[1])
    vol_axis_call.set_ylim(vol_min, vol_max)
    vol_axis_put.set_ylim(vol_min, vol_max)

    # --- IV Comparison subplot ---
    common_strikes = sorted(set(strikes_call).intersection(set(strikes_put)))
    iv_call_common = calls.set_index('strike').loc[common_strikes]['impliedVolatility']
    iv_put_common = puts.set_index('strike').loc[common_strikes]['impliedVolatility']

    ax_iv_compare.plot(common_strikes, iv_call_common, label='Call IV', color='tab:green', marker='o')
    ax_iv_compare.plot(common_strikes, iv_put_common, label='Put IV', color='tab:orange', marker='x')
    ax_iv_compare.set_xlabel('Strike Price')
    ax_iv_compare.set_ylabel('Implied Volatility')
    ax_iv_compare.set_title('Call vs Put Implied Volatility (Same Strikes)')
    ax_iv_compare.grid(True)
    ax_iv_compare.legend()

    # --- Mark Current SPY Price ---
    for ax in [ax_call, ax_put, ax_iv_compare]:
        ax.axvline(current_price, color='black', linestyle='--', linewidth=1.2)
        ax.text(current_price, ax.get_ylim()[1] * 0.95, f'Current SPY\n{current_price:.2f}',
                color='black', rotation=90, ha='right', va='top', fontsize=8)

    plt.tight_layout()
    plt.show()