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

Recall (see [§ HW Bond Pricing](../bond_pricing/bond_price_formula.md)): the Hull-White ZCB price $P(t,T_k)=e^{A(t,T_k)+B(t,T_k)r(t)}$ is affine and by construction matches the market ZCB curve, so the Hull-White swap price agrees with the market swap price.

---

## Exercises

**Exercise 1.** A payer swap has notional $N = \$10{,}000$, fixed rate $K = 0.05$, and annual payments from year 1 to year 10. Write out the formula for the swap value at $t = 0$ in terms of ZCB prices $P(0, T_k)$.

??? success "Solution to Exercise 1"
    The payer swap value at $t = 0$ with notional $N = \$10{,}000$, fixed rate $K = 0.05$, and annual payments from year 1 to year 10 ($T_m = 0$, $T_n = 10$, $\tau_k = 1$ for all $k$) is:

    $$
    \text{IRS}^{\text{Payer}}(0) = N\!\left(P(0, T_m) - P(0, T_n)\right) - NK\sum_{k=m+1}^{n}\tau_k P(0, T_k)
    $$

    With $T_m = 0$ (so $P(0,0) = 1$):

    $$
    \text{IRS}^{\text{Payer}}(0) = 10{,}000\!\left(1 - P(0, 10)\right) - 10{,}000 \times 0.05 \sum_{k=1}^{10} P(0, k)
    $$

    $$
    = 10{,}000\!\left(1 - P(0,10) - 0.05\sum_{k=1}^{10} P(0,k)\right)
    $$

    The floating leg value is $N(P(0,0) - P(0,10)) = N(1 - P(0,10))$, and the fixed leg value is $NK\sum_{k=1}^{10} P(0,k)$. The payer swap pays fixed and receives floating, so its value is the floating leg minus the fixed leg.

---

**Exercise 2.** Show that the par swap rate $K^*$ (the rate that makes the swap value zero at inception) is given by $K^* = \frac{P(0, T_m) - P(0, T_n)}{\sum_{k=m+1}^n \tau_k P(0, T_k)}$. Compute $K^*$ for a 5-year annual swap when $P(0, k) = e^{-0.04k}$ for $k = 1, \ldots, 5$.

??? success "Solution to Exercise 2"
    The par swap rate $K^*$ is the fixed rate that makes the swap value zero:

    $$
    \text{IRS}^{\text{Payer}}(0) = N(P(0,T_m) - P(0,T_n)) - NK^*\sum_{k=m+1}^n \tau_k P(0,T_k) = 0
    $$

    Solving for $K^*$:

    $$
    K^* = \frac{P(0,T_m) - P(0,T_n)}{\sum_{k=m+1}^n \tau_k P(0,T_k)}
    $$

    For a 5-year annual swap with $P(0,k) = e^{-0.04k}$, $T_m = 0$, $T_n = 5$, $\tau_k = 1$:

    $$
    P(0,0) = 1, \quad P(0,5) = e^{-0.20} \approx 0.81873
    $$

    $$
    \sum_{k=1}^5 P(0,k) = e^{-0.04} + e^{-0.08} + e^{-0.12} + e^{-0.16} + e^{-0.20}
    $$

    $$
    \approx 0.96079 + 0.92312 + 0.88692 + 0.85214 + 0.81873 = 4.44170
    $$

    Therefore:

    $$
    K^* = \frac{1 - 0.81873}{4.44170} = \frac{0.18127}{4.44170} \approx 0.04081
    $$

    The par swap rate is approximately 4.08%, which is close to (but slightly above) the continuous rate of 4% because of the difference between continuous and simple compounding.

---

**Exercise 3.** Explain why the Hull-White model recovers the same swap price as direct computation from the market ZCB curve. What property of the Hull-White calibration guarantees this?

??? success "Solution to Exercise 3"
    The Hull-White model recovers the same swap price as the market ZCB curve because of the **exact calibration property**. Specifically, the Hull-White model calibrates the time-dependent function $\theta(t)$ (or equivalently the drift function) so that the model-implied zero-coupon bond prices match the market curve exactly:

    $$
    P^{\text{HW}}(0, T) = P^{\text{market}}(0, T) \quad \text{for all } T
    $$

    Since the swap value at $t = 0$ depends only on ZCB prices $P(0, T_k)$ at the payment dates:

    $$
    \text{IRS}^{\text{Payer}}(0) = N(P(0,T_m) - P(0,T_n)) - NK\sum_{k=m+1}^n \tau_k P(0,T_k)
    $$

    and the Hull-White model reproduces these ZCB prices exactly, the model-implied swap price matches the market swap price. This is guaranteed by the calibration of $\theta(t)$ to fit the initial yield curve, which is the defining feature of the Hull-White (extended Vasicek) framework.

---

**Exercise 4.** In the Monte Carlo approach, why are multiple paths simulated even though the swap at $t = 0$ is model-independent? Discuss how Monte Carlo becomes essential for pricing path-dependent swap variants.

??? success "Solution to Exercise 4"
    At $t = 0$, the plain vanilla swap price is determined entirely by the current ZCB curve through the formula $\text{IRS}(0) = N(P(0,T_m) - P(0,T_n)) - NK\sum \tau_k P(0,T_k)$. This is model-independent -- no simulation is needed.

    The Monte Carlo approach in the code simulates multiple Hull-White paths primarily for **validation**: it confirms that the Hull-White model reproduces the analytic swap price, verifying the implementation.

    Monte Carlo becomes essential for pricing **path-dependent swap variants** where the payoff depends on the evolution of rates, not just their terminal values:

    - **Callable swaps / Bermudan swaptions**: The exercise decision at each date depends on the rate path, requiring dynamic programming or regression-based methods.
    - **Range accrual swaps**: The floating coupon accrues only on days when the rate falls within a specified range, making the payoff path-dependent.
    - **CMS swaps**: The coupon depends on swap rates at future dates, which are nonlinear functions of the yield curve.
    - **Amortizing swaps**: The notional changes based on prepayment behavior, which may depend on the rate path.

    In all these cases, the payoff cannot be expressed solely in terms of $P(0, T_k)$, and simulation of the short rate dynamics is required.

---

**Exercise 5.** Derive the receiver swap value from the payer swap value using the identity $\text{IRS}^{\text{Receiver}} = -\text{IRS}^{\text{Payer}}$. For what value of $K$ are the payer and receiver swap values equal?

??? success "Solution to Exercise 5"
    The receiver swap pays fixed and receives floating, which is the opposite of the payer swap. Therefore:

    $$
    \text{IRS}^{\text{Receiver}}(t_0) = NK\sum_{k=m+1}^n \tau_k P(t_0,T_k) - N(P(t_0,T_m) - P(t_0,T_n)) = -\text{IRS}^{\text{Payer}}(t_0)
    $$

    The payer and receiver swap values are equal when both are zero:

    $$
    \text{IRS}^{\text{Payer}}(t_0) = \text{IRS}^{\text{Receiver}}(t_0) \iff \text{IRS}^{\text{Payer}}(t_0) = 0
    $$

    This occurs when the fixed rate $K$ equals the par swap rate:

    $$
    K = K^* = \frac{P(t_0,T_m) - P(t_0,T_n)}{\sum_{k=m+1}^n \tau_k P(t_0,T_k)}
    $$

    At this rate, both the payer and receiver swaps have zero value, and the swap is said to be "at par."

---

**Exercise 6.** A forward-starting swap begins at $T_m = 5$ with payments at years 6 through 10. Express its value at $t = 0$ in terms of ZCB prices and explain how the Hull-White model prices this instrument.

??? success "Solution to Exercise 6"
    A forward-starting swap beginning at $T_m = 5$ with annual payments at years 6, 7, 8, 9, 10 has the payer value at $t = 0$:

    $$
    \text{IRS}^{\text{Payer}}(0) = N\!\left(P(0, 5) - P(0, 10)\right) - NK\sum_{k=6}^{10} \tau_k P(0, T_k)
    $$

    With annual payments ($\tau_k = 1$):

    $$
    \text{IRS}^{\text{Payer}}(0) = N\!\left(P(0,5) - P(0,10) - K\sum_{k=6}^{10} P(0,k)\right)
    $$

    Note that the floating leg starts at $T_m = 5$, so $P(0,T_m) = P(0,5)$, not $P(0,0) = 1$. The first floating payment is at $T_6 = 6$ based on the rate observed at $T_5 = 5$.

    **Hull-White pricing:** The Hull-White model prices this using the same formula, since the model-implied ZCB prices $P^{\text{HW}}(0,T_k)$ match the market curve by calibration. The value depends on $P(0,5), P(0,6), \ldots, P(0,10)$, all of which are reproduced exactly. The forward-starting feature introduces no additional complexity for the Hull-White model at $t = 0$ -- the analytic formula applies directly. However, if one needs the swap value at a future date $t > 0$ (e.g., for swaption pricing), the Hull-White dynamics of $r(t)$ determine the future ZCB prices $P(t, T_k)$ and hence the swap value conditional on $r(t)$.
