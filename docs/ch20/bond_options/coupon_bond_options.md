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

Each ZCB put $V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k)$ is computed using the Hull-White closed-form formula (Recall, see [§ ZCB Options](zero_coupon_bond_options.md)), with the standard $\sigma_P=\frac{\sigma}{\lambda}(1-e^{-\lambda(T_k-T_m)})\sqrt{(1-e^{-2\lambda(T_m-t_0)})/(2\lambda)}$.

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

---

## Exercises

**Exercise 1.** A 3-year European call option has strike $K = 1.02$ on a 7-year annual coupon bond with coupon rate $K_{\text{cpn}} = 0.05$ and unit notional. The option maturity is $T_m = 3$ and the bond pays coupons at years 4, 5, 6, and 7. Write out the cash flows $c_k$ for $k = 1, 2, 3, 4$ and express the coupon bond call price $V^{\text{CB-Call}}(0)$ as an explicit sum of ZCB call option prices.

??? success "Solution to Exercise 1"
    The bond pays coupons at years 4, 5, 6, 7 with coupon rate $K_{\text{cpn}} = 0.05$ and unit notional. With annual payments ($\tau_k = 1$ for all $k$):

    - $c_1 = K_{\text{cpn}} \cdot \tau_1 = 0.05 \times 1 = 0.05$ at $T_1 = 4$
    - $c_2 = K_{\text{cpn}} \cdot \tau_2 = 0.05 \times 1 = 0.05$ at $T_2 = 5$
    - $c_3 = K_{\text{cpn}} \cdot \tau_3 = 0.05 \times 1 = 0.05$ at $T_3 = 6$
    - $c_4 = K_{\text{cpn}} \cdot \tau_4 + 1 = 0.05 + 1 = 1.05$ at $T_4 = 7$ (final coupon plus principal)

    By Jamshidian's decomposition, the coupon bond call price is:

    $$
    V^{\text{CB-Call}}(0) = \sum_{k=1}^{4} c_k \cdot V_c^{\text{ZCB}}(0, T_m, T_k; K_k)
    $$

    $$
    = 0.05\,V_c^{\text{ZCB}}(0, 3, 4; K_1) + 0.05\,V_c^{\text{ZCB}}(0, 3, 5; K_2) + 0.05\,V_c^{\text{ZCB}}(0, 3, 6; K_3) + 1.05\,V_c^{\text{ZCB}}(0, 3, 7; K_4)
    $$

    where $K_k = e^{A(T_k - 3) + B(T_k - 3)r^*}$ and $r^*$ is the unique solution of $0.05\,P(3, 4; r^*) + 0.05\,P(3, 5; r^*) + 0.05\,P(3, 6; r^*) + 1.05\,P(3, 7; r^*) = 1.02$.

---

**Exercise 2.** Show that for a European payer swaption with strike $K$, option maturity $T_m$, and swap payment dates $T_{m+1}, \ldots, T_n$, the critical short rate $r^*$ satisfies

$$
\sum_{k=m+1}^{n} c_k\,A(T_m, T_k)\,e^{-B(T_m, T_k)\,r^*} = 1
$$

where $c_k = K\tau_k$ for $k < n$ and $c_n = K\tau_n + 1$. Explain why this equation has a unique solution.

??? success "Solution to Exercise 2"
    The payer swaption with strike $K$, option maturity $T_m$, and swap payment dates $T_{m+1}, \ldots, T_n$ is equivalent to a put on a coupon bond with cash flows $c_k = K\tau_k$ for $k < n$ and $c_n = K\tau_n + 1$, with bond strike $K_{\text{CB}} = 1$.

    By Jamshidian's decomposition, the critical short rate $r^*$ solves:

    $$
    \sum_{k=m+1}^n c_k P(T_m, T_k; r^*) = K_{\text{CB}} = 1
    $$

    Now $P(T_m, T_k; r^*) = e^{A(T_k - T_m) + B(T_k - T_m)r^*}$. In the Hull-White model, we can also write the bond price using the named functions: $P(T_m, T_k) = A(T_m, T_k) e^{-B(T_m, T_k)r(T_m)}$ (using the alternative convention where $A(T_m, T_k)$ absorbs the exponential of the drift term). In this convention, the equation becomes:

    $$
    \sum_{k=m+1}^n c_k\, A(T_m, T_k)\, e^{-B(T_m, T_k)\,r^*} = 1
    $$

    **Uniqueness:** Define $g(r) = \sum_k c_k A(T_m, T_k) e^{-B(T_m, T_k)r}$. Since $B(T_m, T_k) > 0$ (using the convention where $B$ is positive), the exponent $-B(T_m, T_k)r$ is decreasing in $r$. With $c_k > 0$ and $A(T_m, T_k) > 0$, the function $g(r)$ is continuous, strictly decreasing in $r$, with $g(r) \to +\infty$ as $r \to -\infty$ and $g(r) \to 0$ as $r \to +\infty$. By the intermediate value theorem, there exists a unique $r^*$ satisfying $g(r^*) = 1$.

---

**Exercise 3.** Derive the payer-receiver swaption parity relation

$$
V^{\text{Payer}}(t_0) - V^{\text{Receiver}}(t_0) = N\!\left(P(t_0, T_m) - \sum_{k=m+1}^{n} c_k\,P(t_0, T_k)\right)
$$

starting from the Jamshidian decomposition of each swaption and the put-call parity for each individual ZCB option.

??? success "Solution to Exercise 3"
    By the swaption-coupon bond option equivalence:

    - Payer swaption: $V^{\text{Payer}} = N \cdot V^{\text{CB-Put}}(t_0; K_{\text{CB}} = 1, c_k)$
    - Receiver swaption: $V^{\text{Receiver}} = N \cdot V^{\text{CB-Call}}(t_0; K_{\text{CB}} = 1, c_k)$

    Applying Jamshidian's decomposition to each:

    $$
    V^{\text{Payer}} = N \sum_k c_k V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k)
    $$

    $$
    V^{\text{Receiver}} = N \sum_k c_k V_c^{\text{ZCB}}(t_0, T_m, T_k; K_k)
    $$

    Therefore:

    $$
    V^{\text{Payer}} - V^{\text{Receiver}} = N \sum_k c_k \left[V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k) - V_c^{\text{ZCB}}(t_0, T_m, T_k; K_k)\right]
    $$

    By put-call parity for each ZCB option:

    $$
    V_p^{\text{ZCB}} - V_c^{\text{ZCB}} = K_k P(t_0, T_m) - P(t_0, T_k)
    $$

    Substituting:

    $$
    V^{\text{Payer}} - V^{\text{Receiver}} = N \sum_k c_k \left[K_k P(t_0, T_m) - P(t_0, T_k)\right]
    $$

    $$
    = N\!\left[P(t_0, T_m)\sum_k c_k K_k - \sum_k c_k P(t_0, T_k)\right]
    $$

    Since $\sum_k c_k K_k = 1$ (the bond strike):

    $$
    V^{\text{Payer}} - V^{\text{Receiver}} = N\!\left[P(t_0, T_m) - \sum_k c_k P(t_0, T_k)\right]
    $$

---

**Exercise 4.** Consider a 2-year into 3-year payer swaption with annual payments, strike $K = 0.05$, notional $N = \$1{,}000{,}000$, and Hull-White parameters $\lambda = 0.03$, $\sigma = 0.015$. Suppose the market discount factors are $P^M(0,3) = 0.8700$, $P^M(0,4) = 0.8350$, and $P^M(0,5) = 0.8010$. Compute the cash flows $c_1, c_2, c_3$ and the individual ZCB put strikes $K_k$ assuming Newton's method yields $r^* = 0.0452$.

??? success "Solution to Exercise 4"
    The swap has tenor 3 years with annual payments at $T_1 = 3$, $T_2 = 4$, $T_3 = 5$, all with $\tau_k = 1$. The cash flows are:

    - $c_1 = K\tau_1 = 0.05 \times 1 = 0.05$
    - $c_2 = K\tau_2 = 0.05 \times 1 = 0.05$
    - $c_3 = K\tau_3 + 1 = 0.05 + 1 = 1.05$

    Given $r^* = 0.0452$ and $\lambda = 0.03$, the individual ZCB put strikes are:

    $$
    K_k = e^{A(T_k - T_m) + B(T_k - T_m)\,r^*}
    $$

    The $B$ values are:

    $$
    B(1) = \frac{e^{-0.03 \times 1} - 1}{0.03} = \frac{0.9704 - 1}{0.03} = -0.9851
    $$

    $$
    B(2) = \frac{e^{-0.03 \times 2} - 1}{0.03} = \frac{0.9418 - 1}{0.03} = -1.9411
    $$

    $$
    B(3) = \frac{e^{-0.03 \times 3} - 1}{0.03} = \frac{0.9139 - 1}{0.03} = -2.8694
    $$

    To compute $A(\tau)$, we need the market forward rates. From the discount factors $P^M(0,3) = 0.8700$, $P^M(0,4) = 0.8350$, $P^M(0,5) = 0.8010$, together with $P^M(0,2)$ (which we need but can estimate), the $A$ function involves $\ln(P^M(0,T_k)/P^M(0,T_m))$ plus convexity corrections. The strikes are then computed as $K_k = e^{A(T_k - 2) + B(T_k - 2) \times 0.0452}$ for each $k$.

    **Verification:** We check that $\sum_k c_k K_k = 1$ (the coupon bond strike for a payer swaption). This holds by construction since $r^* = 0.0452$ was obtained from solving $g(r^*) = 1$.

---

**Exercise 5.** Explain why the Jamshidian decomposition used in this section breaks down for a Bermudan swaption. What pricing method must be used instead, and what is the fundamental difference in the exercise decision structure?

??? success "Solution to Exercise 5"
    The Jamshidian decomposition relies on two properties: (1) European exercise at a single date, and (2) the existence of a single threshold $r^*$ that determines the exercise decision for all cash flows simultaneously.

    A **Bermudan swaption** can be exercised at multiple dates $T_{m_1}, T_{m_2}, \ldots$. At each potential exercise date, the holder compares the immediate exercise value with the continuation value. The optimal exercise boundary is no longer a single number $r^*$ but a function $r^*(t)$ that depends on the exercise date, and the exercise decision at each date depends on the entire future evolution of rates (through the continuation value).

    Specifically:

    - At the last exercise date $T_{m_K}$, exercise occurs if the swap value exceeds zero, giving a threshold $r^*_{m_K}$.
    - At earlier dates $T_{m_j}$, exercise occurs if the swap value exceeds the continuation value, which itself is a complex function of $r(T_{m_j})$.

    The continuation value is path-dependent in the sense that it depends on the conditional distribution of future rates, not just a single comparison. This means the Bermudan swaption cannot be decomposed into a sum of individual options.

    The required pricing methods are **backward induction** on a tree or grid (finite-difference methods) or **regression-based Monte Carlo** (Longstaff-Schwartz algorithm), both of which solve the dynamic programming problem at each exercise date.

---

**Exercise 6.** In the complete pricing formula for swaptions, the volatility parameter entering each ZCB put is

$$
\sigma_P = \frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T_k - T_m)}\right)\sqrt{\frac{1 - e^{-2\lambda(T_m - t_0)}}{2\lambda}}
$$

Analyze the behavior of $\sigma_P$ as a function of the payment date $T_k$ for fixed $T_m$ and $t_0$. Does $\sigma_P$ increase or decrease with $T_k$? What is the economic interpretation?

??? success "Solution to Exercise 6"
    For fixed option maturity $T_m$ and valuation date $t_0$, the factor $\sqrt{(1 - e^{-2\lambda(T_m - t_0)})/(2\lambda)}$ is a constant independent of $T_k$. The dependence of $\sigma_P$ on the payment date $T_k$ comes entirely from:

    $$
    \frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T_k - T_m)}\right)
    $$

    Let $s = T_k - T_m > 0$. Define $h(s) = 1 - e^{-\lambda s}$. Then:

    $$
    h'(s) = \lambda e^{-\lambda s} > 0
    $$

    So $h(s)$ is strictly increasing in $s$. Since $\sigma/\lambda > 0$, $\sigma_P$ is **increasing** in $T_k$.

    The economic interpretation: longer-maturity bonds are more sensitive to interest rate changes. The factor $B(T_k - T_m) = -(1 - e^{-\lambda(T_k - T_m)})/\lambda$ increases in magnitude as $T_k$ grows, meaning the bond price volatility at option expiry is larger for bonds maturing further in the future. Therefore, the ZCB put options on longer-maturity bonds have higher volatility inputs, and their prices are larger (all else being equal).

    As $T_k - T_m \to \infty$, $\sigma_P$ saturates at $(\sigma/\lambda)\sqrt{(1 - e^{-2\lambda(T_m - t_0)})/(2\lambda)}$, reflecting the fact that the duration of a zero-coupon bond saturates at $1/\lambda$ in the Hull-White model.

---

**Exercise 7.** Suppose you price a 5-year into 5-year receiver swaption using the coupon bond option equivalence. The market par swap rate at the option maturity equals the swaption strike $K$. Show that in this at-the-money case, the critical short rate $r^*$ satisfies $\sum_{k} c_k\,P(T_m, T_k; r^*) = 1$ and that each individual ZCB option is also approximately at the money, i.e., $K_k \approx P(0, T_k)/P(0, T_m)$.

??? success "Solution to Exercise 7"
    A receiver swaption is equivalent to a call on a coupon bond with strike $K_{\text{CB}} = 1$. The critical rate $r^*$ satisfies:

    $$
    \sum_k c_k P(T_m, T_k; r^*) = 1
    $$

    This is exactly the stated condition. Now, if the swaption is at-the-money, the forward swap rate at time $0$ equals the strike $K$. The par swap rate condition at time $0$ is:

    $$
    \sum_k c_k P(0, T_k) = P(0, T_m)
    $$

    This means $\sum_k c_k [P(0, T_k)/P(0, T_m)] = 1$. Comparing with the defining equation for $r^*$: $\sum_k c_k P(T_m, T_k; r^*) = 1$.

    The individual ZCB option strikes are $K_k = P(T_m, T_k; r^*)$. At the money, the forward bond prices (at time 0 for delivery at $T_m$) are $F_k = P(0, T_k)/P(0, T_m)$. Both sets of quantities satisfy the same sum constraint:

    $$
    \sum_k c_k K_k = 1, \quad \sum_k c_k F_k = 1
    $$

    Moreover, in the ATM case, the $r^*$ that solves $\sum_k c_k P(T_m, T_k; r^*) = 1$ should be close to the forward short rate implied by the market curve at time $T_m$. When $r^* \approx$ forward rate, we have $P(T_m, T_k; r^*) \approx P(0, T_k)/P(0, T_m)$, so:

    $$
    K_k = P(T_m, T_k; r^*) \approx \frac{P(0, T_k)}{P(0, T_m)} = F_k
    $$

    Therefore each individual ZCB option is approximately at the money, with $K_k \approx F_k$.
