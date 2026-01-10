# ============================================================================
# black_scholes_SENSITIVITY_ANALYSIS.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Model parameters
    S0 = 100      # Current stock price
    K = 105       # Strike price
    T = 0.25      # 3 months to expiration
    r = 0.05      # 5% risk-free rate
    sigma = 0.2   # 20% volatility
    q = 0.02      # 2% dividend yield
    mu = 0.1
    
    # =============================================================================
    # SENSITIVITY ANALYSIS
    # =============================================================================
    print("Analyzing option price sensitivity to parameters...")
    
    # Volatility sensitivity
    vol_range = np.linspace(0.1, 0.4, 10)
    call_prices_vol = []
    
    for vol in vol_range:
        bs_temp = bs.BlackScholes(S0, K, T, r, vol, q)
        call_temp, _ = bs_temp.price_analytical()
        call_prices_vol.append(call_temp)
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(vol_range*100, call_prices_vol, 'b-', linewidth=2, marker='o')
    plt.axvline(sigma*100, color='red', linestyle='--', alpha=0.7, 
                label=f'Current σ = {sigma*100:.1f}%')
    plt.xlabel('Volatility (%)')
    plt.ylabel('Call Price ($)')
    plt.title('Call Price vs Volatility')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Stock price sensitivity
    S_range = np.linspace(80, 120, 20)
    call_prices_S = []
    
    for S in S_range:
        bs_temp = bs.BlackScholes(S, K, T, r, sigma, q)
        call_temp, _ = bs_temp.price_analytical()
        call_prices_S.append(call_temp)
    
    plt.subplot(1, 2, 2)
    plt.plot(S_range, call_prices_S, 'g-', linewidth=2, marker='o')
    plt.axvline(S0, color='red', linestyle='--', alpha=0.7, 
                label=f'Current S₀ = ${S0}')
    plt.axhline(K, color='orange', linestyle=':', alpha=0.7, 
                label=f'Strike K = ${K}')
    plt.xlabel('Stock Price ($)')
    plt.ylabel('Call Price ($)')
    plt.title('Call Price vs Stock Price')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()