# Coupon Bond Options

Most traded interest rate options -- swaptions, callable bonds, and options on government bonds -- involve coupon-bearing instruments rather than zero-coupon bonds. In the Hull-White model, Jamshidian's trick reduces the pricing of European coupon bond options to a sum of zero-coupon bond options, each of which has a closed-form solution. This section assembles the complete pricing formula and establishes the fundamental equivalence between European swaptions and coupon bond options.

## Coupon Bond Option Payoff

A European call option with strike $K$ and maturity $T_m$ on a coupon bond that pays cash flows $c_k$ at times $T_{m+1}, T_{m+2}, \ldots, T_n$ has payoff

$$
\text{Payoff}^{\text{Call}} = \max\!\left(\sum_{k=m+1}^{n} c_k\,P(T_m, T_k) - K,\; 0\right)
$$

For a standard fixed-rate bond with coupon rate $K_{\text{cpn}}$, payment dates $T_{m+1}, \ldots, T_n$, day count fractions $\tau_k = T_k - T_{k-1}$, and unit notional:

$$\begin{array}{lllll}
c_k &=& K_{\text{cpn}}\,\tau_k & \quad\text{for } k = m+1, \ldots, n-1
\\[4pt]
c_n &=& K_{\text{cpn}}\,\tau_n + 1 & \quad\text{(final coupon plus principal)}
\end{array}$$

## Pricing via Jamshidian Decomposition

Applying Jamshidian's trick (detailed in the preceding section), the coupon bond call option price is

!!! info "Theorem: Hull-White Coupon Bond Call Option"
    $$
    V^{\text{CB-Call}}(t_0) = \sum_{k=m+1}^{n} c_k \cdot V_c^{\text{ZCB}}(t_0,\, T_m,\, T_k;\, K_k)
    $$

    where each $V_c^{\text{ZCB}}$ is the Hull-White closed-form zero-coupon bond call option with

    $$
    K_k = A(T_m, T_k)\,e^{-B(T_m, T_k)\,r^*}
    $$

    and $r^*$ is the unique solution of $\sum_{k=m+1}^n c_k\,e^{A(T_k - T_m) + B(T_k - T_m)\,r^*} = K$.

Similarly, the coupon bond put option is

$$
V^{\text{CB-Put}}(t_0) = \sum_{k=m+1}^{n} c_k \cdot V_p^{\text{ZCB}}(t_0,\, T_m,\, T_k;\, K_k)
$$

Each ZCB option $V^{\text{ZCB}}$ is evaluated using the Hull-White ZCB option formula with option maturity $T_m$, bond maturity $T_k$, strike $K_k$, and the conditional distribution of $r(T_m)$ under the appropriate forward measure.

## Swaption as a Coupon Bond Option

The most important application of coupon bond option pricing is the equivalence between European swaptions and coupon bond options. This connection makes the Hull-White model directly applicable to the swaption market.

!!! info "Theorem: Swaption-Coupon Bond Option Equivalence"
    A European payer swaption with strike $K$, option maturity $T_m$, and swap payment dates $T_{m+1}, \ldots, T_n$ is equivalent to a European put on a coupon bond with strike 1:

    $$
    V^{\text{Payer Swaption}}(t_0) = N \cdot V^{\text{CB-Put}}(t_0;\, K_{\text{CB}} = 1,\, c_k)
    $$

    where the cash flows are $c_k = K\tau_k$ for $k < n$ and $c_n = K\tau_n + 1$.

    A European receiver swaption is equivalent to a European call on the same coupon bond:

    $$
    V^{\text{Receiver Swaption}}(t_0) = N \cdot V^{\text{CB-Call}}(t_0;\, K_{\text{CB}} = 1,\, c_k)
    $$

???+ note "Proof"

    The payer swaption payoff at $T_m$ is

    $$\begin{array}{lllll}
    \displaystyle
    N\max\!\left(\sum_{k=m+1}^{n} \tau_k P(T_m, T_k)(l_k(T_m) - K),\; 0\right)
    \end{array}$$

    Using the identity (derived in the swaption formula section)

    $$
    \sum_{k=m+1}^{n} \tau_k P(T_m, T_k)(l_k(T_m) - K) = 1 - \sum_{k=m+1}^{n} c_k\,P(T_m, T_k)
    $$

    the payoff becomes

    $$
    N\max\!\left(1 - \sum_{k=m+1}^{n} c_k\,P(T_m, T_k),\; 0\right)
    $$

    This is the payoff of a put on a coupon bond with strike $K_{\text{CB}} = 1$. $\square$

## Complete Pricing Formula for Swaptions

Combining the swaption-coupon bond equivalence with Jamshidian's decomposition:

$$
V^{\text{Payer Swaption}}(t_0) = N\sum_{k=m+1}^{n} c_k \cdot V_p^{\text{ZCB}}(t_0,\, T_m,\, T_k;\, K_k)
$$

where

$$\begin{array}{lllll}
\displaystyle
c_k &=& \begin{cases} K\tau_k & k \neq n \\ K\tau_n + 1 & k = n \end{cases}
\\[12pt]
\displaystyle
K_k &=& A(T_m, T_k)\,e^{-B(T_m, T_k)\,r^*}
\end{array}$$

and $r^*$ solves $\sum_k c_k\,P(T_m, T_k; r^*) = 1$.

Each ZCB put $V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k)$ is computed using the Hull-White closed-form formula:

$$\begin{array}{lllll}
\displaystyle
V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k)
&=&\displaystyle
K_k\,P(t_0, T_m)\,N(-d_2) - P(t_0, T_k)\,N(-d_1)
\end{array}$$

with $d_1$, $d_2$ defined as in the ZCB option section using the volatility parameter

$$
\sigma_P = \frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T_k - T_m)}\right)\sqrt{\frac{1 - e^{-2\lambda(T_m - t_0)}}{2\lambda}}
$$

## Put-Call Parity for Coupon Bond Options

The put-call parity for coupon bond options follows from the general European option parity:

$$
V^{\text{CB-Call}}(t_0) - V^{\text{CB-Put}}(t_0) = \sum_{k=m+1}^{n} c_k\,P(t_0, T_k) - K\,P(t_0, T_m)
$$

In terms of swaptions, this translates to the payer-receiver parity:

$$
V^{\text{Payer}}(t_0) - V^{\text{Receiver}}(t_0) = N\!\left(P(t_0, T_m) - \sum_{k=m+1}^{n} c_k\,P(t_0, T_k)\right) = N \cdot \text{IRS}^{\text{Payer}}(t_0)
$$

where $\text{IRS}^{\text{Payer}}(t_0)$ is the value of the underlying payer swap at time $t_0$.

## Implementation Algorithm

The complete algorithm for pricing a European payer swaption in the Hull-White model is:

1. **Inputs**: $\lambda$, $\sigma$, market curve $P^M(0,\cdot)$, notional $N$, strike $K$, dates $T_m, T_{m+1}, \ldots, T_n$.
2. **Compute cash flows**: $c_k = K\tau_k$ for $k < n$, $c_n = K\tau_n + 1$.
3. **Find $r^*$**: Solve $\sum_k c_k\,e^{A(T_k - T_m) + B(T_k - T_m)r} = 1$ via Newton's method.
4. **Compute strikes**: $K_k = e^{A(T_k - T_m) + B(T_k - T_m)r^*}$ for each $k$.
5. **Price ZCB puts**: $V_p^{\text{ZCB}}(0, T_m, T_k; K_k)$ using the Hull-White closed-form formula.
6. **Sum**: $V^{\text{Swaption}} = N\sum_k c_k\,V_p^{\text{ZCB}}(0, T_m, T_k; K_k)$.

```python
def price_swaption_jamshidian(hw, N, K, T_m, T_payments, tau):
    """Price a European payer swaption via Jamshidian decomposition."""
    n = len(T_payments)
    c = [K * tau[k] for k in range(n)]
    c[-1] += 1.0  # add principal at final payment

    # Step 1: Find r*
    r_star = find_r_star(hw, T_m, T_payments, c, K=1.0)

    # Step 2: Compute individual strikes
    K_strikes = [hw.compute_ZCB(T_m, T_k, r_star)
                 for T_k in T_payments]

    # Step 3: Price each ZCB put
    total = 0.0
    for k in range(n):
        zbp = hw.compute_ZCB_Option_Price(
            K_strikes[k], T_m, T_payments[k], CP=OptionType.PUT
        )
        total += c[k] * zbp

    return N * total
```

## Numerical Example

Consider a 5-year into 5-year payer swaption (option maturity $T_m = 5$, swap maturity $T_n = 10$) with annual payments, strike $K = 0.04$, notional $N = \$1{,}000{,}000$, and Hull-White parameters $\lambda = 0.05$, $\sigma = 0.01$.

The cash flows are $c_1 = c_2 = c_3 = c_4 = 0.04$ and $c_5 = 1.04$. Newton's method finds $r^* \approx 0.0387$. The individual ZCB put strikes are:

| $k$ | $T_k$ | $K_k = P(5, T_k; r^*)$ | $c_k$ |
|:---:|:---:|:---:|:---:|
| 1 | 6 | 0.9623 | 0.04 |
| 2 | 7 | 0.9253 | 0.04 |
| 3 | 8 | 0.8891 | 0.04 |
| 4 | 9 | 0.8537 | 0.04 |
| 5 | 10 | 0.8190 | 1.04 |

Summing the weighted ZCB put prices gives the swaption value.

---

## Summary

European coupon bond options are priced in the Hull-White model by applying Jamshidian's decomposition to reduce the problem to a sum of zero-coupon bond options. The key practical application is that European payer swaptions are equivalent to puts on coupon bonds with strike 1, and receiver swaptions are equivalent to calls. This equivalence, combined with the Hull-White ZCB option formula, yields a fully analytic pricing framework for the European swaption market.
