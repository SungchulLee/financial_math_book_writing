# Hull-White Swap Pricing

## Hull-White Recovers Swap Pricing

The Hull-White model can price interest rate swaps by computing ZCB prices at each payment date:

```python
def main():
    # Swap setting
    CP = OptionTypeSwap.PAYER  # payer swap pays fixed rate
    notional = 10000.0
    Ks = np.linspace(0.0, 0.08, 30)

    hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)

    # Method 1: Analytic using ZCB curve
    swap_analytic = []
    for K in Ks:
        swap = compute_SwapPrice(P_market, t=0, notional=notional,
                                 K=K, Ti=1.0, Tm=10.0, n=10, CP=CP)
        swap_analytic.append(swap)

    # Method 2: Monte Carlo using Hull-White
    num_paths = 50_000
    t, R, M = hw.generate_sample_paths(num_paths, num_steps=100, T=10)

    swap_mc = []
    for K in Ks:
        # Compute swap payoff on each path
        payoffs = []
        for path in range(num_paths):
            swap_val = hw.compute_SwapPrice(
                t=0, r_t=R[path, 0], notional=notional,
                K=K, Ti=1.0, Tm=10.0, n=10, CP=CP
            )
            payoffs.append(swap_val)
        swap_mc.append(np.mean(payoffs))

    # Compare
    plt.figure(figsize=(10, 5))
    plt.plot(Ks, swap_analytic, 'b-', label='Analytic (ZCB Curve)')
    plt.plot(Ks, swap_mc, 'r--', label='Hull-White MC')
    plt.xlabel('Fixed Rate K')
    plt.ylabel('Swap Value')
    plt.title('Hull-White Recovers Swap Pricing')
    plt.legend()
    plt.grid(True)
    plt.show()
```

The payer swap value is:

$$\begin{array}{lllllllll}
\displaystyle
{\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K)
&=&
N\left(P(t,T_m)-P(t,T_n)\right)-NK\sum_{k=m+1}^n \tau_k P(t,T_k)
\end{array}$$

The Hull-White model computes each $P(t,T_k)=e^{A(t,T_k)+B(t,T_k)r(t)}$ using the calibrated functions $A$ and $B$, which by construction match the market ZCB curve. Therefore, the Hull-White swap price agrees with the market swap price.
