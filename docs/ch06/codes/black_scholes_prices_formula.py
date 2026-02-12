# ============================================================================
# black_scholes_OPTION_PRICES_USING_FORMULA.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

S = np.linspace(50, 150, 100)
K = 100
T = 1 / 12
r = 0.05
sigma = 0.3

# ===========================================================
# Loop-based computation of Black-Scholes call and put prices
# ===========================================================

call_prices = []
put_prices = []
for s in S:
    call_price, put_price = bs.BlackScholes(s, K, T, r, sigma).price_analytical()
    call_prices.append(call_price)
    put_prices.append(put_price)
call = np.array(call_prices)
put = np.array(put_prices)

print(f"\n{'='*80}")
print("BASIC OPTION PRICING RESULTS")
print("="*80,end="\n"*2)
print(f"Stock price range: ${S[0]:.0f} - ${S[-1]:.0f}")
print(f"Strike price: ${K}")
print(f"Number of price points calculated: {len(S)}")
print(f"")
print(f"At-the-money option prices (S = ${K}):")
idx_atm = np.argmin(np.abs(S - K))
print(f"  Call price: ${call[idx_atm]:.2f}")
print(f"  Put price:  ${put[idx_atm]:.2f}")
print(f"")
print(f"Price range summary:")
print(f"  Call prices: ${call.min():.2f} - ${call.max():.2f}")
print(f"  Put prices:  ${put.min():.2f} - ${put.max():.2f}")
print(f"")
print("Note: Loop-based calculation completed successfully!")

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))

fig.suptitle(
    "\n\n" +
    f"Black-Scholes Option Pricing\n" +
    f"Strike $K$ = {K}, Time to Maturity $T$ = {T:.2f} yr, " +
    f"Rate $r$ = {r:.2%}, Volatility $\sigma$ = {sigma:.2%}" + "\n\n",
    fontsize=12, y=1.05
)

ax0.plot(S, call, '-r', linewidth=2, label='Call Price')
ax0.plot(S, np.maximum(S - K, 0), '--b', linewidth=2, label='Call Payoff', alpha=0.6)
ax0.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike K = {K}')
ax0.set_title('Call Option')
ax0.set_xlabel('Underlying Price $S$')
ax0.set_ylabel('Price')
ax0.legend()
ax0.grid(True, alpha=0.3)

ax1.plot(S, put, '-r', linewidth=2, label='Put Price')
ax1.plot(S, np.maximum(K - S, 0), '--b', linewidth=2, label='Put Payoff', alpha=0.6)
ax1.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike K = {K}')
ax1.set_title('Put Option')
ax1.set_xlabel('Underlying Price $S$')
ax1.set_ylabel('Price')
ax1.legend()
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.subplots_adjust(top=0.8)
plt.show()

# ===========================================================
# Vectorized computation of Black-Scholes call and put prices
# ===========================================================

print("\n" + "="*80)
print("ALTERNATIVE: Using Black-Scholes utilities for vectorization")
print("="*80,end="\n"*2)

call_vectorized = bs.bs_call_price(S, K, T, r, sigma)
put_vectorized = bs.bs_put_price(S, K, T, r, sigma)

print(f"Call prices match: {np.allclose(call, call_vectorized)}")
print(f"Put prices match: {np.allclose(put, put_vectorized)}")
print(f"Max difference (call): {np.max(np.abs(call - call_vectorized)):.2e}")
print(f"Max difference (put): {np.max(np.abs(put - put_vectorized)):.2e}")

def create_enhanced_option_plot(S_range, K, T, r, sigma, save_path=None):
    S = np.linspace(S_range[0], S_range[1], 200)
    
    call_prices = bs.bs_call_price(S, K, T, r, sigma)
    put_prices = bs.bs_put_price(S, K, T, r, sigma)
    
    call_intrinsic = np.maximum(S - K, 0)
    put_intrinsic = np.maximum(K - S, 0)
    
    call_time_value = call_prices - call_intrinsic
    put_time_value = put_prices - put_intrinsic
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    fig.suptitle(
        f"Comprehensive Black-Scholes Option Analysis\n" +
        f"K = ${K}, T = {T:.3f} yr, r = {r:.1%}, σ = {sigma:.1%}",
        fontsize=14, y=0.98
    )
    
    ax1.plot(S, call_prices, '-r', linewidth=2, label='Call Price')
    ax1.plot(S, call_intrinsic, '--k', linewidth=2, label='Intrinsic Value', alpha=0.7)
    ax1.fill_between(S, call_intrinsic, call_prices, alpha=0.3, color='green', label='Time Value')
    ax1.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax1.set_title('Call Option Components')
    ax1.set_xlabel('Stock Price ($)')
    ax1.set_ylabel('Option Value ($)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(S, put_prices, '-b', linewidth=2, label='Put Price')
    ax2.plot(S, put_intrinsic, '--k', linewidth=2, label='Intrinsic Value', alpha=0.7)
    ax2.fill_between(S, put_intrinsic, put_prices, alpha=0.3, color='orange', label='Time Value')
    ax2.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax2.set_title('Put Option Components')
    ax2.set_xlabel('Stock Price ($)')
    ax2.set_ylabel('Option Value ($)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    ax3.plot(S, call_time_value, '-g', linewidth=2, label='Call Time Value')
    ax3.plot(S, put_time_value, color='orange', linestyle='-', linewidth=2, label='Put Time Value')
    ax3.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax3.set_title('Time Value Comparison')
    ax3.set_xlabel('Stock Price ($)')
    ax3.set_ylabel('Time Value ($)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    current_call_price = bs.bs_call_price(K, K, T, r, sigma)
    current_put_price = bs.bs_put_price(K, K, T, r, sigma)
    
    call_pnl = call_intrinsic - current_call_price
    put_pnl = put_intrinsic - current_put_price
    
    ax4.plot(S, call_pnl, color='red', linestyle='-', linewidth=2, label=f'Call P&L (paid ${current_call_price:.2f})')
    ax4.plot(S, put_pnl, color='blue', linestyle='-', linewidth=2, label=f'Put P&L (paid ${current_put_price:.2f})')
    ax4.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax4.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')
    ax4.set_title('Profit & Loss at Expiration')
    ax4.set_xlabel('Stock Price at Expiration ($)')
    ax4.set_ylabel('Profit/Loss ($)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    for ax in [ax1, ax2, ax3, ax4]:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_position(('data', K))
        
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")
    
    plt.show()
    
    print(f"\nKey Statistics at Current Stock Price (S = ${K}):")
    print(f"  Call Option Price:    ${current_call_price:.2f}")
    print(f"  Put Option Price:     ${current_put_price:.2f}")
    print(f"  Call Time Value:      ${current_call_price:.2f}")
    print(f"  Put Time Value:       ${current_put_price:.2f}")
    print(f"  Put-Call Parity:      C - P = S - K*e^(-rT)")
    
    parity_left = current_call_price - current_put_price
    parity_right = K - K * np.exp(-r * T)
    print(f"    Left side:          ${parity_left:.2f}")
    print(f"    Right side:         ${parity_right:.2f}")
    print(f"    Difference:         ${abs(parity_left - parity_right):.2f}")

print(f"\n{'='*80}")
print("ENHANCED OPTION ANALYSIS")
print("="*80)

create_enhanced_option_plot(
    S_range=(50, 150),
    K=100,
    T=1/12,
    r=0.05,
    sigma=0.3
)

print(f"\n{'='*80}")
print("WRAPPER USAGE EXAMPLES")
print("="*80,end="\n"*2)

print("Example 1: At-the-money options (S = $100)")
atm_model = bs.BlackScholes(S0=100, K=100, T=1/12, r=0.05, sigma=0.3)
call_atm, put_atm = atm_model.price_analytical()
greeks_atm = atm_model.calculate_greeks()

print(f"  Call price: ${call_atm:.2f}")
print(f"  Put price:  ${put_atm:.2f}")
print(f"  Call delta: {greeks_atm['delta_call']:.4f}")
print(f"  Put delta:  {greeks_atm['delta_put']:.4f}")
print(f"  Gamma:      {greeks_atm['gamma']:.4f}")
print(f"  Vega:       {greeks_atm['vega']:.4f}")

print(f"\nExample 2: In-the-money call (S = $120)")
itm_call_model = bs.BlackScholes(S0=120, K=100, T=1/12, r=0.05, sigma=0.3)
call_itm, put_itm = itm_call_model.price_analytical()
greeks_itm = itm_call_model.calculate_greeks()

print(f"  Call price: ${call_itm:.2f}")
print(f"  Put price:  ${put_itm:.2f}")
print(f"  Call delta: {greeks_itm['delta_call']:.4f}")
print(f"  Intrinsic:  ${max(120-100, 0):.2f}")
print(f"  Time value: ${call_itm - max(120-100, 0):.2f}")

print(f"\nExample 3: Out-of-the-money put (S = $120)")
print(f"  Put price:  ${put_itm:.2f}")
print(f"  Put delta:  {greeks_itm['delta_put']:.4f}")
print(f"  Intrinsic:  ${max(100-120, 0):.2f}")
print(f"  Time value: ${put_itm - max(100-120, 0):.2f}")
print()