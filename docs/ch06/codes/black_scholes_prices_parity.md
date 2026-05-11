# Option Prices (Using Put-Call Parity)

## Background

Black Scholes Prices Parity

Educational script demonstrating black scholes prices parity concepts.

---

## Code

```python
"""
Black Scholes Prices Parity

Educational script demonstrating black scholes prices parity concepts.
"""

# ============================================================================
# black_scholes_OPTION_PRICES_USING_PUT_CALL_PARITY.py
# ============================================================================
import black_scholes as bs
import numpy as np
import matplotlib.pyplot as plt

# Parameters


if __name__ == "__main__":
    S = np.arange(50, 155, 5)
    K = 100
    T = 1
    r = 0.03
    sigma = 0.2

    # Print basic information
    print(f"\n{'='*60}")
    print("PUT-CALL PARITY DEMONSTRATION")
    print("="*60)
    print(f"Stock price range: ${S[0]} - ${S[-1]} (step: ${S[1]-S[0]})")
    print(f"Strike price: ${K}")
    print(f"Time to maturity: {T} year")
    print(f"Risk-free rate: {r:.1%}")
    print(f"Volatility: {sigma:.1%}")
    print(f"Number of price points: {len(S)}")

    # Compute Black-Scholes call and put prices using the wrapper
    # We need to vectorize for array of S values
    call_prices = []
    put_prices = []

    for s in S:
        bs_model = bs.BlackScholes(s, K, T, r, sigma)
        call_price, put_price = bs_model.price_analytical()
        call_prices.append(call_price)
        put_prices.append(put_price)

    call = np.array(call_prices)
    put = np.array(put_prices)

    # Alternative: Use vectorized utility functions (more efficient)
    call_vectorized = bs.bs_call_price(S, K, T, r, sigma)
    put_vectorized = bs.bs_put_price(S, K, T, r, sigma)

    # Verify both methods give same results
    print(f"\nCalculation verification:")
    print(f"  Call prices match: {np.allclose(call, call_vectorized)}")
    print(f"  Put prices match: {np.allclose(put, put_vectorized)}")
    print(f"  Max difference: {np.max(np.abs(call - call_vectorized)):.2e}")

    # Use the more efficient vectorized results
    call = call_vectorized
    put = put_vectorized

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot Black-Scholes put price
    ax.plot(S, put, '-r', linewidth=2, label='Put using Black-Scholes Formula')

    # Compute put price using put-call parity: P = C - S + K*exp(-rT)
    put_parity = call - S + K * np.exp(-r * T)
    ax.plot(S, put_parity, '*g', markersize=8, label='Put using Put-Call Parity')

    # Plot intrinsic value (payoff at maturity)
    S1 = np.sort(np.concatenate((S, [K])))
    payoff = np.maximum(K - S1, 0)
    ax.plot(S1, payoff, '--b', linewidth=2, alpha=0.7, label='Put Payoff (Intrinsic Value)')

    # Add strike price reference line
    ax.axvline(x=K, color='gray', linestyle=':', alpha=0.7, label=f'Strike = ${K}')

    # Axis labels and legend
    ax.set_xlabel('Stock Price ($)', fontsize=12)
    ax.set_ylabel('Put Option Value ($)', fontsize=12)
    ax.set_title('Put-Call Parity Verification\n' + 
                f'K=${K}, T={T}yr, r={r:.1%}, σ={sigma:.1%}', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Clean up plot appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

    # Verify put-call parity numerically
    print(f"\nPut-Call Parity Verification:")
    print(f"  Formula: P = C - S + K*e^(-rT)")
    print(f"  Expected: Put prices should match parity calculation")

    # Calculate differences
    parity_differences = np.abs(put - put_parity)
    max_diff = np.max(parity_differences)
    mean_diff = np.mean(parity_differences)

    print(f"\nNumerical Results:")
    print(f"  Maximum difference: ${max_diff:.2e}")
    print(f"  Mean difference: ${mean_diff:.2e}")
    print(f"  All differences < 1e-10: {np.all(parity_differences < 1e-10)}")

    if max_diff < 1e-10:
        print(f"  ✓ Excellent! Put-call parity holds within numerical precision")
    else:
        print(f"  ⚠ Differences detected - check calculation")

    # Show some specific examples
    print(f"\nSpecific Examples:")
    print(f"{'Stock Price':<12}{'BS Put':<10}{'Parity Put':<12}{'Difference':<12}")
    print("-" * 48)

    # Show results for a few key points
    key_indices = [0, len(S)//4, len(S)//2, 3*len(S)//4, -1]
    for i in key_indices:
        s_val = S[i]
        put_bs = put[i]
        put_par = put_parity[i]
        diff = abs(put_bs - put_par)
        print(f"${s_val:<11.0f}${put_bs:<9.4f}${put_par:<11.4f}${diff:<11.2e}")

    print(f"\nAt-the-Money Analysis (S = K = ${K}):")
    idx_atm = np.argmin(np.abs(S - K))
    s_atm = S[idx_atm]
    call_atm = call[idx_atm]
    put_atm = put[idx_atm]
    intrinsic_call = max(s_atm - K, 0)
    intrinsic_put = max(K - s_atm, 0)
    time_value_call = call_atm - intrinsic_call
    time_value_put = put_atm - intrinsic_put

    print(f"  Stock Price: ${s_atm:.0f}")
    print(f"  Call Price: ${call_atm:.4f} (Intrinsic: ${intrinsic_call:.4f}, Time: ${time_value_call:.4f})")
    print(f"  Put Price:  ${put_atm:.4f} (Intrinsic: ${intrinsic_put:.4f}, Time: ${time_value_put:.4f})")

    # Demonstrate using wrapper for single calculation
    print(f"\nWrapper Usage Example:")
    atm_model = bs.BlackScholes(S0=K, K=K, T=T, r=r, sigma=sigma)
    call_wrapper, put_wrapper = atm_model.price_analytical()
    greeks = atm_model.calculate_greeks()

    print(f"  Using BlackScholes wrapper at S=${K}:")
    print(f"    Call: ${call_wrapper:.4f}")
    print(f"    Put:  ${put_wrapper:.4f}")
    print(f"    Delta (Call/Put): {greeks['delta_call']:.4f} / {greeks['delta_put']:.4f}")
    print(f"    Gamma: {greeks['gamma']:.6f}")
    print(f"    Vega:  {greeks['vega']:.4f}")

    print("="*60)
```

## Exercises

**Exercise 1.**
State put-call parity for European options. Derive it using a no-arbitrage argument involving two portfolios.

??? success "Solution to Exercise 1"
    Put-call parity: $C - P = S_0 - Ke^{-rT}$.

    **Portfolio A**: Long call + $Ke^{-rT}$ in bonds. At $T$: if $S_T > K$, exercise call for $S_T - K + K = S_T$; if $S_T \le K$, call expires, get $K$.

    **Portfolio B**: Long put + long stock. At $T$: if $S_T > K$, put expires, have $S_T$; if $S_T \le K$, exercise put for $K - S_T + S_T = K$.

    Both portfolios pay $\max(S_T, K)$ at $T$. By no-arbitrage, they must have equal present values: $C + Ke^{-rT} = P + S_0$, giving $C - P = S_0 - Ke^{-rT}$.

---

**Exercise 2.**
Using put-call parity, if $C = 8.50$, $S_0 = 100$, $K = 95$, $T = 0.5$, $r = 0.04$, compute $P$.

??? success "Solution to Exercise 2"
    $$
    P = C - S_0 + Ke^{-rT} = 8.50 - 100 + 95e^{-0.02} = 8.50 - 100 + 93.12 = \$1.62
    $$

---

**Exercise 3.**
Explain how put-call parity can be used to verify the correctness of option pricing implementations. What discrepancy would indicate a bug?

??? success "Solution to Exercise 3"
    After computing $C$ and $P$ independently (whether by formula, MC, or PDE), check that $C - P = S_0 e^{-qT} - Ke^{-rT}$ (with dividends). Any discrepancy beyond numerical tolerance indicates a bug.

    Common bugs detected:

    - Incorrect discount factor (using $e^{-rT}$ instead of $e^{-(r-q)T}$ for dividends).
    - Wrong sign in $d_1$ or $d_2$ formula.
    - Boundary condition errors in PDE solvers.
    - Payoff function errors ($\max(S-K,0)$ vs $\max(K-S,0)$).

---

**Exercise 4.**
Does put-call parity hold for American options? If not, what inequality replaces it?

??? success "Solution to Exercise 4"
    Put-call parity does **not** hold for American options because the early exercise feature breaks the equivalence between the two portfolios.

    For American options on a non-dividend-paying stock: $S_0 - K \le C_A - P_A \le S_0 - Ke^{-rT}$.

    The upper bound comes from the European parity (since $C_A = C_E$ for non-dividend stocks). The lower bound accounts for the possibility that the American put may be exercised early. With dividends, the bounds become: $S_0 e^{-qT} - K \le C_A - P_A \le S_0 - Ke^{-rT}$.
