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

---

## Exercises

**Exercise 1.** In the Hull-White model, the bond price at time $T_m$ for maturity $T_k$ is $P(T_m, T_k) = e^{A(T_k - T_m) + B(T_k - T_m)\,r(T_m)}$ with $B(\tau) = -(1 - e^{-\lambda\tau})/\lambda$. Prove that $B(\tau) < 0$ for all $\tau > 0$ and that $P(T_m, T_k)$ is strictly decreasing in $r(T_m)$.

??? success "Solution to Exercise 1"
    We have $B(\tau) = -(1 - e^{-\lambda\tau})/\lambda$. For $\tau > 0$ and $\lambda > 0$:

    - $\lambda\tau > 0$ implies $e^{-\lambda\tau} < 1$, so $1 - e^{-\lambda\tau} > 0$
    - Therefore $(1 - e^{-\lambda\tau})/\lambda > 0$, and $B(\tau) = -(1 - e^{-\lambda\tau})/\lambda < 0$

    For the monotonicity of the bond price, compute the derivative with respect to $r(T_m)$:

    $$
    \frac{\partial P(T_m, T_k)}{\partial r(T_m)} = B(T_k - T_m) \cdot P(T_m, T_k)
    $$

    Since $P(T_m, T_k) > 0$ (bond prices are positive) and $B(T_k - T_m) < 0$ (proven above for $T_k > T_m$), the derivative is strictly negative. Therefore $P(T_m, T_k)$ is strictly decreasing in $r(T_m)$.

---

**Exercise 2.** Let $g(r) = \sum_{k=m+1}^{n} c_k\,e^{A(T_k - T_m) + B(T_k - T_m)\,r}$ with positive cash flows $c_k > 0$. Show that $\lim_{r \to -\infty} g(r) = +\infty$ and $\lim_{r \to +\infty} g(r) = 0$, and conclude that the equation $g(r) = K$ has a unique solution for any $K > 0$.

??? success "Solution to Exercise 2"
    Each term in $g(r) = \sum_{k=m+1}^n c_k e^{A(T_k - T_m) + B(T_k - T_m)r}$ has $c_k > 0$ and is an exponential function of $r$ with coefficient $B(T_k - T_m) < 0$ in the exponent.

    **Limit as $r \to -\infty$:** Since $B(T_k - T_m) < 0$, as $r \to -\infty$ we get $B(T_k - T_m) \cdot r \to +\infty$. Therefore each exponential $e^{A(T_k - T_m) + B(T_k - T_m)r} \to +\infty$, and since $c_k > 0$, we have $g(r) \to +\infty$.

    **Limit as $r \to +\infty$:** Since $B(T_k - T_m) < 0$, as $r \to +\infty$ we get $B(T_k - T_m) \cdot r \to -\infty$. Therefore each exponential $e^{A(T_k - T_m) + B(T_k - T_m)r} \to 0$, and $g(r) \to 0$.

    **Strict monotonicity:** The derivative is

    $$
    g'(r) = \sum_{k=m+1}^n c_k B(T_k - T_m) e^{A(T_k - T_m) + B(T_k - T_m)r}
    $$

    Every term has $c_k > 0$, $B(T_k - T_m) < 0$, and $e^{(\cdots)} > 0$, so $g'(r) < 0$ for all $r$. Hence $g$ is strictly decreasing.

    Since $g$ is continuous, strictly decreasing, maps to $(0, +\infty)$, and takes values from $+\infty$ down to $0$, by the intermediate value theorem, for any $K > 0$ there exists a unique $r^*$ such that $g(r^*) = K$.

---

**Exercise 3.** Consider a European put on a coupon bond with cash flows $c_k$ and strike $K$. Write the payoff at $T_m$, apply the Jamshidian decomposition, and verify that the put decomposes as $V^{\text{CB-Put}}(t_0) = \sum_k c_k \cdot V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k)$, where the option is exercised when $r(T_m) > r^*$.

??? success "Solution to Exercise 3"
    The put payoff at $T_m$ is:

    $$
    \max\!\left(K - \sum_{k=m+1}^n c_k P(T_m, T_k),\; 0\right)
    $$

    Using $\sum_k c_k K_k = K$:

    $$
    = \max\!\left(\sum_{k=m+1}^n c_k K_k - \sum_{k=m+1}^n c_k P(T_m, T_k),\; 0\right) = \max\!\left(\sum_{k=m+1}^n c_k(K_k - P(T_m, T_k)),\; 0\right)
    $$

    Now analyze the sign of each term $K_k - P(T_m, T_k)$:

    - If $r(T_m) > r^*$: Since $P(T_m, T_k)$ is decreasing in $r$, we have $P(T_m, T_k) < P(T_m, T_k; r^*) = K_k$, so $K_k - P(T_m, T_k) > 0$ for all $k$. The put is exercised.
    - If $r(T_m) < r^*$: $P(T_m, T_k) > K_k$ for all $k$, so $K_k - P(T_m, T_k) < 0$ for all $k$. The put expires worthless.

    Since all terms have the same sign, the max of the sum equals the sum of maxes:

    $$
    \max\!\left(\sum_k c_k(K_k - P(T_m, T_k)),\; 0\right) = \sum_k c_k \max(K_k - P(T_m, T_k),\; 0)
    $$

    Taking expectations under $\mathbb{Q}^{T_m}$:

    $$
    V^{\text{CB-Put}}(t_0) = P(t_0, T_m) \sum_{k=m+1}^n c_k\,\mathbb{E}^{T_m}\!\left[\max(K_k - P(T_m, T_k), 0)\,\Big|\,\mathcal{F}(t_0)\right] = \sum_k c_k \cdot V_p^{\text{ZCB}}(t_0, T_m, T_k; K_k)
    $$

    The put option is exercised when $r(T_m) > r^*$ (higher rates mean lower bond prices, making the put in-the-money), which is opposite to the call exercise condition $r(T_m) < r^*$.

---

**Exercise 4.** Suppose a coupon bond pays $c_1 = 0.03$ at $T_1 = 3$, $c_2 = 0.03$ at $T_2 = 4$, and $c_3 = 1.03$ at $T_3 = 5$. A European call on this bond has strike $K = 0.98$ and option maturity $T_m = 2$. With Hull-White parameters $\lambda = 0.05$ and $\sigma = 0.01$, outline the Newton's method iteration to find $r^*$. Write the derivative $g'(r)$ explicitly and describe how convergence is guaranteed.

??? success "Solution to Exercise 4"
    The cash flows are $c_1 = 0.03$, $c_2 = 0.03$, $c_3 = 1.03$. The function to solve is:

    $$
    g(r) = 0.03\,e^{A(1) + B(1)r} + 0.03\,e^{A(2) + B(2)r} + 1.03\,e^{A(3) + B(3)r} = 0.98
    $$

    where $A(k)$ and $B(k)$ denote $A(T_k - T_m)$ and $B(T_k - T_m)$, with $T_m = 2$ and $T_k = 3, 4, 5$.

    The $B$ values with $\lambda = 0.05$ are:

    $$
    B(1) = \frac{e^{-0.05} - 1}{0.05} \approx -0.9754, \quad B(2) = \frac{e^{-0.10} - 1}{0.05} \approx -1.9032, \quad B(3) = \frac{e^{-0.15} - 1}{0.05} \approx -2.7860
    $$

    The derivative for Newton's method is:

    $$
    g'(r) = 0.03\,B(1)\,e^{A(1) + B(1)r} + 0.03\,B(2)\,e^{A(2) + B(2)r} + 1.03\,B(3)\,e^{A(3) + B(3)r}
    $$

    Since $B(k) < 0$ for all $k$ and $c_k > 0$, we have $g'(r) < 0$ for all $r$. The Newton iteration is:

    $$
    r_{n+1} = r_n - \frac{g(r_n) - 0.98}{g'(r_n)}
    $$

    Convergence is guaranteed because $g$ is smooth (infinitely differentiable), strictly monotone, and convex (since $g''(r) = \sum_k c_k B(k)^2 e^{A(k) + B(k)r} > 0$). The convexity ensures that Newton's method converges quadratically from any initial guess once the iterates enter a neighborhood of $r^*$.

---

**Exercise 5.** In a two-factor Hull-White model, bond prices depend on two state variables $(r_1(t), r_2(t))$. Explain why the monotonicity argument fails: construct a scenario where increasing $r_1$ increases $P(T_m, T_1)$ but decreases $P(T_m, T_2)$, so that the terms $c_k(P(T_m, T_k) - K_k)$ do not all switch sign at the same threshold.

??? success "Solution to Exercise 5"
    In a two-factor model, the bond price at $T_m$ for maturity $T_k$ is:

    $$
    P(T_m, T_k) = \exp\!\left(A^{(2)}(T_m, T_k) + B_x(T_m, T_k)\,x(T_m) + B_y(T_m, T_k)\,y(T_m)\right)
    $$

    where $B_x(T_m, T_k) = (e^{-\lambda_1(T_k - T_m)} - 1)/\lambda_1$ and $B_y(T_m, T_k) = (e^{-\lambda_2(T_k - T_m)} - 1)/\lambda_2$. Both factor loadings are negative, so the bond price is decreasing in both $x$ and $y$ individually.

    However, the monotonicity argument requires that for a **single** variable, all bond prices move together. In the two-factor model, the exercise decision depends on two variables $(x(T_m), y(T_m))$, and there is no single threshold that determines exercise.

    **Counterexample:** Suppose $\lambda_1 = 0.01$, $\lambda_2 = 0.5$, $T_m = 2$, $T_1 = 3$, $T_2 = 30$.

    - $B_x(2, 3) = (e^{-0.01} - 1)/0.01 \approx -0.995$, $B_y(2, 3) = (e^{-0.5} - 1)/0.5 \approx -0.787$
    - $B_x(2, 30) = (e^{-0.28} - 1)/0.01 \approx -24.4$, $B_y(2, 30) = (e^{-14} - 1)/0.5 \approx -2.0$

    Consider a scenario where $x$ increases by $\Delta x = 0.001$ and simultaneously $y$ decreases by $\Delta y = -0.003$. The log-price changes are:

    - $\Delta\!\log P(T_m, T_1) \approx B_x \cdot 0.001 + B_y \cdot (-0.003) = -0.000995 + 0.002361 = +0.00137$ (bond price increases)
    - $\Delta\!\log P(T_m, T_2) \approx -24.4 \cdot 0.001 + (-2.0) \cdot (-0.003) = -0.0244 + 0.006 = -0.0184$ (bond price decreases)

    The short-maturity bond increased while the long-maturity bond decreased. The terms $c_k(P(T_m, T_k) - K_k)$ can therefore have opposite signs, so $\max(\sum_k a_k, 0) \neq \sum_k \max(a_k, 0)$. The Jamshidian decomposition fails.

---

**Exercise 6.** Verify numerically that $\sum_{k=m+1}^{n} c_k K_k = K$ holds by construction. Starting from $K_k = P(T_m, T_k; r^*)$ and the definition $g(r^*) = K$, show this identity algebraically without relying on any specific parameter values.

??? success "Solution to Exercise 6"
    By definition, $K_k = P(T_m, T_k; r^*) = e^{A(T_k - T_m) + B(T_k - T_m)r^*}$. Therefore:

    $$
    \sum_{k=m+1}^n c_k K_k = \sum_{k=m+1}^n c_k\, e^{A(T_k - T_m) + B(T_k - T_m)r^*}
    $$

    But $r^*$ is defined as the solution of:

    $$
    g(r^*) = \sum_{k=m+1}^n c_k\, e^{A(T_k - T_m) + B(T_k - T_m)r^*} = K
    $$

    Comparing the two expressions, they are identical. Therefore:

    $$
    \sum_{k=m+1}^n c_k K_k = g(r^*) = K
    $$

    This identity holds by construction for any parameter values, any set of cash flows $c_k > 0$, and any maturity dates $T_k$. It is purely algebraic and does not depend on the specific Hull-White parameters.

---

**Exercise 7.** The Jamshidian decomposition relies on the identity $\max(\sum_k a_k, 0) = \sum_k \max(a_k, 0)$ when all $a_k$ have the same sign. Construct a simple two-term counterexample where $a_1 > 0$ and $a_2 < 0$ to show that this identity fails when the terms can have different signs. Relate this to why the trick requires a one-factor model.

??? success "Solution to Exercise 7"
    **Counterexample:** Let $a_1 = 3$ and $a_2 = -1$. Then:

    - Left side: $\max(a_1 + a_2, 0) = \max(3 + (-1), 0) = \max(2, 0) = 2$
    - Right side: $\max(a_1, 0) + \max(a_2, 0) = \max(3, 0) + \max(-1, 0) = 3 + 0 = 3$

    Since $2 \neq 3$, the identity $\max(\sum_k a_k, 0) = \sum_k \max(a_k, 0)$ fails.

    In general, when some terms are positive and others are negative:

    $$
    \max\!\left(\sum_k a_k, 0\right) \leq \sum_k \max(a_k, 0)
    $$

    with strict inequality whenever the sum is positive but some individual terms are negative (the positive terms partially compensate for the negative ones in the sum, but not in the individual maxima).

    This relates to the one-factor requirement as follows: in a one-factor model, all $a_k = c_k(P(T_m, T_k) - K_k)$ have the same sign because all bond prices are monotone in the same single variable $r(T_m)$. Either all terms are positive ($r < r^*$), all negative ($r > r^*$), or all zero ($r = r^*$). In a multi-factor model, different bond prices can move in different directions for the same realization of the state variables, causing some $a_k$ to be positive and others negative simultaneously. The identity breaks down, and Jamshidian's trick cannot be applied.
