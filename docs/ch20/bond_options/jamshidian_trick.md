# Jamshidian's Trick

A European option on a coupon-bearing bond has a payoff that depends on the prices of multiple zero-coupon bonds simultaneously. Pricing such an option directly requires the joint distribution of all the bond prices, which is intractable even in a Gaussian model. Jamshidian (1989) observed that in any one-factor model where bond prices are monotone functions of the short rate, the option on a portfolio of bonds can be decomposed into a portfolio of options on individual bonds. This section presents the trick, proves it rigorously, and demonstrates its application in the Hull-White model.

## The Problem: Options on Coupon Bonds

Consider a European call option with strike $K$ and maturity $T_m$ on a coupon bond that pays cash flows $c_k$ at times $T_k$ for $k = m+1, \ldots, n$. The payoff at $T_m$ is

$$
\max\!\left(\sum_{k=m+1}^{n} c_k\,P(T_m, T_k) - K,\; 0\right)
$$

where $P(T_m, T_k)$ is the price at $T_m$ of a zero-coupon bond maturing at $T_k$. Direct evaluation of $\mathbb{E}^{T_m}[\cdot]$ requires the joint distribution of $(P(T_m, T_{m+1}), \ldots, P(T_m, T_n))$, which is not straightforward even though each $P(T_m, T_k)$ is individually lognormal.

## Key Observation: Monotonicity

In the Hull-White model, the bond price at $T_m$ for maturity $T_k$ is

$$
P(T_m, T_k) = \exp\!\left(A(T_k - T_m) + B(T_k - T_m)\,r(T_m)\right)
$$

Since $B(\tau) = -\frac{1}{\lambda}(1 - e^{-\lambda\tau}) < 0$ for all $\tau > 0$, each bond price $P(T_m, T_k)$ is a **strictly decreasing** function of $r(T_m)$.

!!! tip "Why Monotonicity Matters"
    When all bond prices move in the same direction as a function of a single state variable $r(T_m)$, the exercise decision at $T_m$ reduces to comparing $r(T_m)$ to a single threshold $r^*$. This is the essential insight that makes the decomposition possible.

## The Optimal Exercise Rate

!!! info "Definition: Critical Short Rate"
    The critical short rate $r^*$ is the unique solution of

    $$
    \sum_{k=m+1}^{n} c_k\,P(T_m, T_k;\, r^*) = K
    $$

    where $P(T_m, T_k;\, r^*) = e^{A(T_k - T_m) + B(T_k - T_m)\,r^*}$. The option is exercised if and only if $r(T_m) < r^*$ (for a call) since lower rates imply higher bond prices.

Existence and uniqueness of $r^*$ follow from the strict monotonicity of $\sum_k c_k P(T_m, T_k; r)$ in $r$: this sum is continuous, strictly decreasing, tends to $+\infty$ as $r \to -\infty$, and tends to $0$ as $r \to +\infty$.

## Decomposition of Strikes

Once $r^*$ is found, define the individual strikes

$$
K_k = P(T_m, T_k;\, r^*) = e^{A(T_k - T_m) + B(T_k - T_m)\,r^*}
$$

By construction, $\sum_{k=m+1}^n c_k\,K_k = K$.

## Jamshidian's Theorem

!!! info "Theorem: Jamshidian's Decomposition"
    The European call option on a coupon bond with payoff $\max(\sum_k c_k P(T_m, T_k) - K, 0)$ can be decomposed as

    $$
    V^{\text{CB-Call}}(t_0) = \sum_{k=m+1}^{n} c_k \cdot V_c^{\text{ZCB}}(t_0,\, T_m,\, T_k;\, K_k)
    $$

    where $V_c^{\text{ZCB}}(t_0, T_m, T_k; K_k)$ is the price of a European call on a zero-coupon bond with option maturity $T_m$, bond maturity $T_k$, and strike $K_k$.

    Similarly, a European put on the coupon bond decomposes as

    $$
    V^{\text{CB-Put}}(t_0) = \sum_{k=m+1}^{n} c_k \cdot V_p^{\text{ZCB}}(t_0,\, T_m,\, T_k;\, K_k)
    $$

???+ note "Proof"

    The call payoff at $T_m$ can be written as

    $$\begin{array}{lllll}
    \displaystyle
    \max\!\left(\sum_{k=m+1}^{n} c_k\,P(T_m, T_k) - K,\; 0\right)
    &=&\displaystyle
    \max\!\left(\sum_{k=m+1}^{n} c_k\,P(T_m, T_k) - \sum_{k=m+1}^{n} c_k\,K_k,\; 0\right)
    \end{array}$$

    since $\sum_k c_k K_k = K$ by construction. Now consider the sign of each term $P(T_m, T_k) - K_k$:

    - If $r(T_m) < r^*$: Since each $P(T_m, T_k)$ is decreasing in $r$, we have $P(T_m, T_k) > P(T_m, T_k; r^*) = K_k$ for all $k$. Every term is positive.
    - If $r(T_m) > r^*$: $P(T_m, T_k) < K_k$ for all $k$. Every term is negative.
    - If $r(T_m) = r^*$: Every term equals zero.

    Because all terms switch sign at the **same** threshold $r^*$, the maximum of the sum equals the sum of the maxima:

    $$\begin{array}{lllll}
    \displaystyle
    \max\!\left(\sum_{k} c_k(P(T_m, T_k) - K_k),\; 0\right)
    &=&\displaystyle
    \sum_{k} c_k\,\max\!\left(P(T_m, T_k) - K_k,\; 0\right)
    \end{array}$$

    Taking the $\mathbb{Q}^{T_m}$-expectation and multiplying by $P(t_0, T_m)$:

    $$\begin{array}{lllll}
    \displaystyle
    V^{\text{CB-Call}}(t_0)
    &=&\displaystyle
    P(t_0, T_m)\sum_{k=m+1}^{n} c_k\,\mathbb{E}^{T_m}\!\left[\max(P(T_m, T_k) - K_k, 0)\,\Big|\,\mathcal{F}(t_0)\right]
    \\[6pt]
    &=&\displaystyle
    \sum_{k=m+1}^{n} c_k \cdot V_c^{\text{ZCB}}(t_0, T_m, T_k; K_k)
    \end{array}$$

    $\square$

## Finding r* Numerically

The critical rate $r^*$ is found by solving $g(r) = K$ where $g(r) = \sum_k c_k e^{A(T_k - T_m) + B(T_k - T_m)r}$. Since $g$ is smooth, strictly monotone, and maps $\mathbb{R}$ onto $(0, \infty)$, Newton's method converges rapidly:

$$
r_{n+1} = r_n - \frac{g(r_n) - K}{g'(r_n)}
$$

where $g'(r) = \sum_k c_k B(T_k - T_m)\,e^{A(T_k - T_m) + B(T_k - T_m)r}$.

```python
def find_r_star(hw, T_m, T_payments, c_payments, K, tol=1e-12):
    """Find critical rate r* using Newton's method."""
    r = 0.03  # initial guess
    for _ in range(100):
        g = sum(c * hw.compute_ZCB(T_m, T_k, r)
                for c, T_k in zip(c_payments, T_payments))
        if abs(g - K) < tol:
            break
        B_vals = [hw.B(T_k - T_m) for T_k in T_payments]
        g_prime = sum(c * B * hw.compute_ZCB(T_m, T_k, r)
                      for c, B, T_k in zip(c_payments, B_vals, T_payments))
        r = r - (g - K) / g_prime
    return r
```

## Applicability and Limitations

Jamshidian's trick applies whenever the following conditions hold:

1. **Single-factor model**: All bond prices depend on a single state variable.
2. **Monotonicity**: All bond prices are monotone functions of that state variable in the same direction.
3. **European exercise**: The option is exercised at a single date.

!!! warning "When the Trick Fails"
    - **Multi-factor models** (e.g., two-factor Hull-White): Bond prices at different maturities may not be monotone in the same variable. The trick does not apply.
    - **American/Bermudan options**: Multiple exercise dates require dynamic programming, not a single threshold decomposition.
    - **Path-dependent payoffs**: The trick requires the payoff to depend only on $r(T_m)$, not on the path of $r$.

## Numerical Example

Consider a 2-year European call with strike $K = 1.0$ on a 5-year annual coupon bond paying $c = 0.05$ annually with principal at maturity. The cash flows are $c_1 = c_2 = c_3 = 0.05$ at years 3, 4, 5 and $c_3 = 1.05$ at year 5 (combined). With Hull-White parameters $\lambda = 0.05$, $\sigma = 0.01$:

1. Solve $0.05\,P(2,3;r^*) + 0.05\,P(2,4;r^*) + 1.05\,P(2,5;r^*) = 1.0$ for $r^*$.
2. Compute $K_k = P(2, T_k; r^*)$ for $k = 1, 2, 3$.
3. Price each ZCB call: $V_c^{\text{ZCB}}(0, 2, T_k; K_k)$ using the Hull-White closed-form formula.
4. Sum: $V^{\text{CB-Call}} = 0.05\,V_c^{\text{ZCB}}(0,2,3;K_1) + 0.05\,V_c^{\text{ZCB}}(0,2,4;K_2) + 1.05\,V_c^{\text{ZCB}}(0,2,5;K_3)$.

---

## Summary

Jamshidian's trick exploits the monotonicity of bond prices in the short rate to decompose a European coupon bond option into a sum of European zero-coupon bond options. The critical step is finding the unique short rate $r^*$ at which the option is exactly at the money. Each individual ZCB option can then be priced using the Hull-White closed-form formula, yielding an analytic price for the coupon bond option without any numerical integration over the joint distribution of bond prices.
