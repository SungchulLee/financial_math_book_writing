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

---

## Exercises

**Exercise 1.** A payer swap has notional $N = \$10{,}000$, fixed rate $K = 0.05$, and annual payments from year 1 to year 10. Write out the formula for the swap value at $t = 0$ in terms of ZCB prices $P(0, T_k)$.

---

**Exercise 2.** Show that the par swap rate $K^*$ (the rate that makes the swap value zero at inception) is given by $K^* = \frac{P(0, T_m) - P(0, T_n)}{\sum_{k=m+1}^n \tau_k P(0, T_k)}$. Compute $K^*$ for a 5-year annual swap when $P(0, k) = e^{-0.04k}$ for $k = 1, \ldots, 5$.

---

**Exercise 3.** Explain why the Hull-White model recovers the same swap price as direct computation from the market ZCB curve. What property of the Hull-White calibration guarantees this?

---

**Exercise 4.** In the Monte Carlo approach, why are multiple paths simulated even though the swap at $t = 0$ is model-independent? Discuss how Monte Carlo becomes essential for pricing path-dependent swap variants.

---

**Exercise 5.** Derive the receiver swap value from the payer swap value using the identity $\text{IRS}^{\text{Receiver}} = -\text{IRS}^{\text{Payer}}$. For what value of $K$ are the payer and receiver swap values equal?

---

**Exercise 6.** A forward-starting swap begins at $T_m = 5$ with payments at years 6 through 10. Express its value at $t = 0$ in terms of ZCB prices and explain how the Hull-White model prices this instrument.
