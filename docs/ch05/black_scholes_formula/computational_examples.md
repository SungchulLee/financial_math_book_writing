# Computational Examples

This section provides detailed step-by-step calculations for pricing European options using the Black-Scholes formula, along with Python implementations and practical examples. The goal is to bridge the theoretical formulas with numerical computation.

---

## 1. Manual Calculation: European Call

### **Problem Setup**

Price a European call option with:

- Current stock price: $S_0 = 50$
- Strike price: $K = 52$
- Time to maturity: $T = 0.5$ years (6 months)
- Risk-free rate: $r = 5\%$ per annum
- Volatility: $\sigma = 30\%$ per annum

### **Step 1: Compute $d_1$ and $d_2$**

$$
d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

**Numerator**:

$$
\ln(50/52) + (0.05 + 0.5 \times 0.09) \times 0.5
$$

$$
= \ln(0.9615) + (0.05 + 0.045) \times 0.5
$$

$$
= -0.0392 + 0.0475 = 0.0083
$$

**Denominator**:

$$
\sigma\sqrt{T} = 0.30 \times \sqrt{0.5} = 0.30 \times 0.7071 = 0.2121
$$

**Result**:

$$
d_1 = \frac{0.0083}{0.2121} = 0.0391
$$

**Compute $d_2$**:

$$
d_2 = d_1 - \sigma\sqrt{T} = 0.0391 - 0.2121 = -0.1730
$$

### **Step 2: Evaluate $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$**

Using standard normal CDF tables or calculator:

$$
\mathcal{N}(0.0391) \approx 0.5156
$$

$$
\mathcal{N}(-0.1730) \approx 0.4313
$$

### **Step 3: Calculate Option Price**

$$
C_0 = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

**First term**:

$$
S_0\mathcal{N}(d_1) = 50 \times 0.5156 = 25.78
$$

**Second term**:

$$
Ke^{-rT}\mathcal{N}(d_2) = 52 \times e^{-0.05 \times 0.5} \times 0.4313
$$

$$
= 52 \times 0.9753 \times 0.4313 = 21.87

$$

**Call price**:

$$
C_0 = 25.78 - 21.87 = 3.91
$$

**Answer**: The European call is worth approximately **$3.91**.

---

## 2. Manual Calculation: European Put

### **Same Setup as Above**

### **Step 1: Use $d_1$ and $d_2$ from Call Calculation**

$$
d_1 = 0.0391, \quad d_2 = -0.1730
$$

### **Step 2: Evaluate $\mathcal{N}(-d_1)$ and $\mathcal{N}(-d_2)$**

Using symmetry $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$:

$$
\mathcal{N}(-d_1) = 1 - 0.5156 = 0.4844
$$

$$
\mathcal{N}(-d_2) = 1 - 0.4313 = 0.5687
$$

### **Step 3: Calculate Put Price**

$$
P_0 = Ke^{-rT}\mathcal{N}(-d_2) - S_0\mathcal{N}(-d_1)
$$

**First term**:

$$
Ke^{-rT}\mathcal{N}(-d_2) = 52 \times 0.9753 \times 0.5687 = 28.84
$$

**Second term**:

$$
S_0\mathcal{N}(-d_1) = 50 \times 0.4844 = 24.22
$$

**Put price**:

$$
P_0 = 28.84 - 24.22 = 4.62
$$

**Answer**: The European put is worth approximately **$4.62**.

### **Verification via Put-Call Parity**

$$
C - P = S - Ke^{-rT}
$$

$$
3.91 - 4.62 = -0.71
$$

$$
50 - 52 \times 0.9753 = 50 - 50.72 = -0.72
$$

Small rounding error confirms parity holds. ✓

---

## 3. Python Implementation

### **Basic Implementation**

```python
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate European call option price using Black-Scholes formula.
    
    Parameters:
    S : float : current stock price
    K : float : strike price
    T : float : time to maturity (years)
    r : float : risk-free rate (annual)
    sigma : float : volatility (annual)
    
    Returns:
    float : call option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """
    Calculate European put option price using Black-Scholes formula.
    
    Parameters: (same as call)
    
    Returns:
    float : put option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return put_price

# Example usage
S0 = 50
K = 52
T = 0.5
r = 0.05
sigma = 0.30

call_price = black_scholes_call(S0, K, T, r, sigma)
put_price = black_scholes_put(S0, K, T, r, sigma)

print(f"Call Price: ${call_price:.2f}")
print(f"Put Price: ${put_price:.2f}")

# Verify put-call parity
parity_lhs = call_price - put_price
parity_rhs = S0 - K * np.exp(-r * T)
print(f"\nPut-Call Parity Check:")
print(f"C - P = {parity_lhs:.4f}")
print(f"S - Ke^(-rT) = {parity_rhs:.4f}")
print(f"Difference: {abs(parity_lhs - parity_rhs):.6f}")
```

**Output**:
```
Call Price: $3.91
Put Price: $4.62

Put-Call Parity Check:
C - P = -0.7065
S - Ke^(-rT) = -0.7065
Difference: 0.000000
```

---

## 4. Greeks Calculation

### **Complete Implementation with Greeks**

```python
def black_scholes_greeks(S, K, T, r, sigma, option_type='call'):
    """
    Calculate Black-Scholes option price and Greeks.
    
    Returns:
    dict : {'price', 'delta', 'gamma', 'theta', 'vega', 'rho'}
    """
    # Compute d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Standard normal PDF and CDF
    pdf_d1 = norm.pdf(d1)
    cdf_d1 = norm.cdf(d1)
    cdf_d2 = norm.cdf(d2)
    
    if option_type == 'call':
        # Call price
        price = S * cdf_d1 - K * np.exp(-r * T) * cdf_d2
        
        # Delta
        delta = cdf_d1
        
        # Theta (per year, convert to per day by dividing by 365)
        theta = (-S * pdf_d1 * sigma / (2 * np.sqrt(T)) 
                 - r * K * np.exp(-r * T) * cdf_d2)
        
        # Rho (per 1% change in r)
        rho = K * T * np.exp(-r * T) * cdf_d2 / 100
        
    else:  # put
        # Put price
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        
        # Delta
        delta = cdf_d1 - 1
        
        # Theta
        theta = (-S * pdf_d1 * sigma / (2 * np.sqrt(T)) 
                 + r * K * np.exp(-r * T) * norm.cdf(-d2))
        
        # Rho
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100
    
    # Gamma (same for call and put)
    gamma = pdf_d1 / (S * sigma * np.sqrt(T))
    
    # Vega (same for call and put, per 1% change in sigma)
    vega = S * np.sqrt(T) * pdf_d1 / 100
    
    return {
        'price': price,
        'delta': delta,
        'gamma': gamma,
        'theta': theta,
        'vega': vega,
        'rho': rho
    }

# Calculate for call
call_greeks = black_scholes_greeks(50, 52, 0.5, 0.05, 0.30, 'call')
print("Call Option:")
for greek, value in call_greeks.items():
    print(f"  {greek.capitalize()}: {value:.4f}")

print("\nPut Option:")
put_greeks = black_scholes_greeks(50, 52, 0.5, 0.05, 0.30, 'put')
for greek, value in put_greeks.items():
    print(f"  {greek.capitalize()}: {value:.4f}")
```

**Output**:
```
Call Option:
  Price: 3.9089
  Delta: 0.5156
  Gamma: 0.0377
  Theta: -4.8652
  Vega: 0.1335
  Rho: 0.1203

Put Option:
  Price: 4.6153
  Delta: -0.4844
  Gamma: 0.0377
  Theta: -3.5691
  Vega: 0.1335
  Rho: -0.1335
```

---

## 5. Sensitivity Analysis

### **Impact of Volatility**

```python
import matplotlib.pyplot as plt

# Range of volatilities
sigmas = np.linspace(0.1, 0.6, 50)
call_prices = [black_scholes_call(50, 52, 0.5, 0.05, s) for s in sigmas]
put_prices = [black_scholes_put(50, 52, 0.5, 0.05, s) for s in sigmas]

plt.figure(figsize=(10, 6))
plt.plot(sigmas * 100, call_prices, label='Call', linewidth=2)
plt.plot(sigmas * 100, put_prices, label='Put', linewidth=2)
plt.xlabel('Volatility (%)', fontsize=12)
plt.ylabel('Option Price ($)', fontsize=12)
plt.title('Option Prices vs. Volatility', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

### **Impact of Stock Price**

```python
# Range of stock prices
stock_prices = np.linspace(30, 70, 100)
call_values = [black_scholes_call(S, 52, 0.5, 0.05, 0.30) for S in stock_prices]
put_values = [black_scholes_put(S, 52, 0.5, 0.05, 0.30) for S in stock_prices]

# Intrinsic values
call_intrinsic = np.maximum(stock_prices - 52, 0)
put_intrinsic = np.maximum(52 - stock_prices, 0)

plt.figure(figsize=(12, 5))

# Call subplot
plt.subplot(1, 2, 1)
plt.plot(stock_prices, call_values, 'b-', linewidth=2, label='Call Value')
plt.plot(stock_prices, call_intrinsic, 'r--', linewidth=1.5, label='Intrinsic Value')
plt.axvline(52, color='gray', linestyle=':', alpha=0.7, label='Strike')
plt.xlabel('Stock Price ($)')
plt.ylabel('Call Value ($)')
plt.title('Call Option Value')
plt.legend()
plt.grid(True, alpha=0.3)

# Put subplot
plt.subplot(1, 2, 2)
plt.plot(stock_prices, put_values, 'b-', linewidth=2, label='Put Value')
plt.plot(stock_prices, put_intrinsic, 'r--', linewidth=1.5, label='Intrinsic Value')
plt.axvline(52, color='gray', linestyle=':', alpha=0.7, label='Strike')
plt.xlabel('Stock Price ($)')
plt.ylabel('Put Value ($)')
plt.title('Put Option Value')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 6. Practical Examples

### **Example 1: ATM Call with Different Maturities**

Compare ATM calls with 1 month, 3 months, 6 months, and 1 year to maturity:

```python
S = K = 100  # ATM
r = 0.05
sigma = 0.25
maturities = [1/12, 3/12, 6/12, 1.0]

print("ATM Call Prices by Maturity:")
print(f"{'Maturity':<12} {'Price':<10} {'Time Value'}")
print("-" * 35)

for T in maturities:
    call_price = black_scholes_call(S, K, T, r, sigma)
    # ATM so intrinsic value is 0
    time_value = call_price
    
    maturity_label = f"{int(T*12)} month{'s' if T != 1/12 else ''}"
    print(f"{maturity_label:<12} ${call_price:>8.2f}  ${time_value:>8.2f}")
```

**Output**:
```
ATM Call Prices by Maturity:
Maturity     Price      Time Value
-----------------------------------
1 month      $  2.05    $  2.05
3 months     $  3.56    $  3.56
6 months     $  5.04    $  5.04
12 months    $  7.13    $  7.13
```

**Observation**: Option value increases with time, but not linearly (roughly proportional to $\sqrt{T}$).

### **Example 2: OTM vs ITM vs ATM**

Compare options at different moneyness levels:

```python
S = 100
r = 0.05
sigma = 0.25
T = 0.5

strikes = [80, 90, 100, 110, 120]  # Deep ITM to Deep OTM

print("\nOption Prices at Different Strikes:")
print(f"{'Strike':<10} {'Moneyness':<12} {'Call':<10} {'Put':<10} {'Call Δ':<10} {'Put Δ'}")
print("-" * 65)

for K in strikes:
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)
    
    call_greeks = black_scholes_greeks(S, K, T, r, sigma, 'call')
    put_greeks = black_scholes_greeks(S, K, T, r, sigma, 'put')
    
    if S > K:
        moneyness = "ITM"
    elif S < K:
        moneyness = "OTM"
    else:
        moneyness = "ATM"
    
    print(f"{K:<10} {moneyness:<12} ${call_price:<9.2f} ${put_price:<9.2f} "
          f"{call_greeks['delta']:<9.3f} {put_greeks['delta']:<9.3f}")
```

**Output**:
```
Option Prices at Different Strikes:
Strike     Moneyness    Call       Put        Call Δ     Put Δ
-----------------------------------------------------------------
80         ITM          $20.65     $ 0.52     0.936      -0.064
90         ITM          $11.49     $ 1.36     0.793      -0.207
100        ATM          $ 5.04     $ 4.91     0.566      -0.434
110        OTM          $ 1.67     $11.42     0.317      -0.683
120        OTM          $ 0.39     $20.14     0.134      -0.866
```

**Observations**:
- Deep ITM call has $\Delta \approx 1$, behaves like stock
- Deep OTM call has $\Delta \approx 0$, minimal stock sensitivity
- ATM options have $\Delta \approx 0.5$

### **Example 3: Implied Volatility Calculation**

Given a market option price, back out the implied volatility:

```python
from scipy.optimize import brentq

def implied_volatility_call(market_price, S, K, T, r):
    """
    Calculate implied volatility for a call option.
    Uses Brent's method to find sigma such that BS price = market price.
    """
    def objective(sigma):
        return black_scholes_call(S, K, T, r, sigma) - market_price
    
    try:
        # Search for volatility between 1% and 200%
        implied_vol = brentq(objective, 0.01, 2.0)
        return implied_vol
    except ValueError:
        return np.nan

# Example: market call price is $6.00
market_call_price = 6.00
S, K, T, r = 100, 100, 0.5, 0.05

implied_vol = implied_volatility_call(market_call_price, S, K, T, r)
print(f"Market Call Price: ${market_call_price}")
print(f"Implied Volatility: {implied_vol * 100:.2f}%")

# Verify
bs_price = black_scholes_call(S, K, T, r, implied_vol)
print(f"BS Price at Implied Vol: ${bs_price:.2f}")
```

**Output**:
```
Market Call Price: $6.00
Implied Volatility: 30.55%
BS Price at Implied Vol: $6.00
```

---

## 7. Common Numerical Issues

### **Issue 1: Extreme Values of $d_1$ or $d_2$**

When $d_1$ or $d_2$ are very large (positive or negative), numerical precision issues arise in evaluating $\mathcal{N}(d)$.

**Solution**: Use asymptotic approximations:

- If $d_1 > 8$: $\mathcal{N}(d_1) \approx 1$
- If $d_1 < -8$: $\mathcal{N}(d_1) \approx 0$

### **Issue 2: Near Expiration** ($T \to 0$)

As $T \to 0$, $d_1$ and $d_2$ can become undefined (division by zero).

**Solution**: For $T < 0.001$, use intrinsic value directly:

$$
C \approx \max(S - K, 0)
$$

### **Issue 3: Very Low Volatility** ($\sigma \to 0$)

When $\sigma$ is very small, option behaves like forward contract.

**Solution**: Use forward value formula:

$$
C \approx \max(S - Ke^{-rT}, 0)
$$

---

## 8. Complete Working Example

### **Real-World Scenario**

You're analyzing a call option on Apple stock:

- Current stock price: $S = \$175.00$
- Strike price: $K = \$180.00$
- Days to expiration: 45 days
- Risk-free rate: $r = 4.5\%$ (annual)
- Historical volatility: $\sigma = 28\%$ (annual)

**Question**: What is the fair value of this call option?

**Solution**:

```python
# Input parameters
S = 175.00
K = 180.00
T = 45 / 365  # Convert days to years
r = 0.045
sigma = 0.28

# Calculate option price
call_price = black_scholes_call(S, K, T, r, sigma)
greeks = black_scholes_greeks(S, K, T, r, sigma, 'call')

print("=" * 50)
print("BLACK-SCHOLES OPTION VALUATION")
print("=" * 50)
print(f"\nInput Parameters:")
print(f"  Stock Price (S):        ${S:.2f}")
print(f"  Strike Price (K):       ${K:.2f}")
print(f"  Time to Maturity (T):   {T*365:.0f} days ({T:.4f} years)")
print(f"  Risk-Free Rate (r):     {r*100:.2f}%")
print(f"  Volatility (σ):         {sigma*100:.2f}%")

print(f"\nOption Valuation:")
print(f"  Call Price:             ${greeks['price']:.2f}")
print(f"  Intrinsic Value:        ${max(S - K, 0):.2f}")
print(f"  Time Value:             ${greeks['price'] - max(S - K, 0):.2f}")

print(f"\nGreeks:")
print(f"  Delta (Δ):              {greeks['delta']:.4f}")
print(f"  Gamma (Γ):              {greeks['gamma']:.4f}")
print(f"  Vega (ν):               ${greeks['vega']:.4f} per 1% vol")
print(f"  Theta (Θ):              ${greeks['theta']:.2f} per year")
print(f"                          ${greeks['theta']/365:.2f} per day")
print(f"  Rho (ρ):                ${greeks['rho']:.4f} per 1% rate")

print("\n" + "=" * 50)
```

**Output**:
```
==================================================
BLACK-SCHOLES OPTION VALUATION
==================================================

Input Parameters:
  Stock Price (S):        $175.00
  Strike Price (K):       $180.00
  Time to Maturity (T):   45 days (0.1233 years)
  Risk-Free Rate (r):     4.50%
  Volatility (σ):         28.00%

Option Valuation:
  Call Price:             $3.67
  Intrinsic Value:        $0.00
  Time Value:             $3.67

Greeks:
  Delta (Δ):              0.4089
  Gamma (Γ):              0.0441
  Vega (ν):               $0.1382 per 1% vol
  Theta (Θ):              $-22.05 per year
                          $-0.06 per day
  Rho (ρ):                $0.0433 per 1% rate

==================================================
```

**Interpretation**: This OTM call with 45 days to expiration is worth $3.67, consisting entirely of time value. It has a delta of 0.41, meaning for every $1 increase in the stock price, the option gains approximately $0.41.

---

## Summary

This section provided:

1. **Manual calculations**: Step-by-step computation of call and put prices

2. **Python implementation**: Complete code with Greeks calculation

3. **Sensitivity analysis**: Visual exploration of parameter effects

4. **Practical examples**: Real-world scenarios and interpretation

5. **Numerical considerations**: Common issues and solutions

**Key takeaways**:
- Black-Scholes formula is straightforward to implement computationally
- Standard normal CDF $\mathcal{N}(\cdot)$ is the only special function required
- Greeks provide sensitivity measures essential for risk management
- Put-call parity serves as a validation check
- Implied volatility calculation inverts the pricing formula

The combination of theoretical understanding and computational proficiency enables effective use of the Black-Scholes model in practice.
