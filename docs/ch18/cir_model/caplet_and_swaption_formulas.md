# Caplet and Swaption Formulas Under CIR

Interest rate caps and swaptions are the two most actively traded interest rate options, and any short-rate model used in practice must be able to price them. The CIR model achieves this through two key observations: first, a caplet is equivalent to a put option on a zero-coupon bond; second, Jamshidian's decomposition reduces a swaption to a portfolio of bond options. Since the CIR model provides closed-form bond option formulas via the non-central chi-squared distribution, both caps and swaptions can be priced analytically. This section develops these connections in detail.

---

## Caps and caplets

### Cap structure

An interest rate **cap** protects the holder against rising rates. It consists of a series of **caplets**, each covering one reset period. A cap with notional $N$, strike rate $K$, and reset dates $T_0 < T_1 < \cdots < T_n$ pays at each date $T_{i+1}$:

$$
N\,\delta_i\,(L(T_i, T_{i+1}) - K)^+
$$

where $\delta_i = T_{i+1} - T_i$ is the day count fraction and $L(T_i, T_{i+1})$ is the simply compounded spot rate over $[T_i, T_{i+1}]$.

The cap price is the sum of individual caplet prices:

$$
\text{Cap}(t) = \sum_{i=0}^{n-1} \text{Caplet}_i(t)
$$

### Caplet as a bond put

The simply compounded rate $L(T_i, T_{i+1})$ is related to bond prices by

$$
L(T_i, T_{i+1}) = \frac{1}{\delta_i}\left(\frac{1}{P(T_i, T_{i+1})} - 1\right)
$$

Substituting into the caplet payoff at $T_{i+1}$:

$$
N\,\delta_i\,(L(T_i, T_{i+1}) - K)^+ = N\left(1 - (1 + K\delta_i)P(T_i, T_{i+1})\right)^+
$$

$$
= N(1 + K\delta_i)\left(\frac{1}{1 + K\delta_i} - P(T_i, T_{i+1})\right)^+
$$

This is $(1 + K\delta_i)$ units of a **put option** on a zero-coupon bond maturing at $T_{i+1}$, with exercise date $T_i$ and strike $\tilde{K}_i = \frac{1}{1 + K\delta_i}$.

!!! tip "Caplet-put equivalence"
    The caplet paid at $T_{i+1}$ with rate strike $K$ is equivalent to $N(1 + K\delta_i)$ put options on the $T_{i+1}$-bond with exercise at $T_i$ and bond strike $\tilde{K}_i = 1/(1 + K\delta_i)$. This equivalence holds model-independently --- it is a payoff identity, not an approximation.

### Caplet pricing under CIR

Discounting the caplet payoff to time $t$:

$$
\text{Caplet}_i(t) = N(1 + K\delta_i)\,\text{Put}_{\text{ZCB}}(t;\,T_i,\,T_{i+1},\,\tilde{K}_i)
$$

where $\text{Put}_{\text{ZCB}}$ is the CIR zero-coupon bond put formula from the bond options section:

$$
\text{Put}_{\text{ZCB}}(t;\,T_i,\,T_{i+1},\,\tilde{K}_i) = \tilde{K}_i\,P(t,T_i)\left[1 - \chi^2(x_2;\,d,\,\lambda_2)\right] - P(t,T_{i+1})\left[1 - \chi^2(x_1;\,d,\,\lambda_1)\right]
$$

with parameters computed using option expiry $T_i$, bond maturity $T_{i+1}$, and strike $\tilde{K}_i$.

---

## Floors and floorlets

An interest rate **floor** protects against falling rates. A floorlet pays $N\delta_i(K - L(T_i, T_{i+1}))^+$ at $T_{i+1}$. By the same argument as above, this is equivalent to $N(1 + K\delta_i)$ call options on the $T_{i+1}$-bond:

$$
\text{Floorlet}_i(t) = N(1 + K\delta_i)\,\text{Call}_{\text{ZCB}}(t;\,T_i,\,T_{i+1},\,\tilde{K}_i)
$$

**Cap-floor parity** follows from call-put parity for bond options:

$$
\text{Cap}(t) - \text{Floor}(t) = \text{Swap}(t)
$$

where $\text{Swap}(t)$ is the value of the corresponding payer interest rate swap.

---

## Swaptions

### Swaption structure

A **payer swaption** with expiry $T_0$ gives the holder the right to enter a payer swap (paying fixed, receiving floating) with fixed rate $K$ on dates $T_1, \ldots, T_n$. The payoff at $T_0$ is

$$
\left(\sum_{i=1}^{n} \delta_{i-1}\,(L(T_{i-1}, T_i) - K)\,P(T_0, T_i)\right)^+
$$

which simplifies to

$$
\left(1 - P(T_0, T_n) - K\sum_{i=1}^{n}\delta_{i-1}\,P(T_0, T_i)\right)^+
$$

Writing $c_i = K\delta_{i-1}$ for $i = 1, \ldots, n-1$ and $c_n = 1 + K\delta_{n-1}$, this is

$$
\left(1 - \sum_{i=1}^{n} c_i\,P(T_0, T_i)\right)^+
$$

The swaption is exercised when the swap has positive value, which occurs when the coupon bond $\sum c_i P(T_0, T_i)$ is worth less than par.

---

## Jamshidian's decomposition

Jamshidian (1989) observed that in any one-factor model where bond prices are monotone decreasing functions of the short rate, a European option on a coupon bond can be decomposed into a portfolio of options on zero-coupon bonds.

### The key insight

Since each $P(T_0, T_i) = A_i\,e^{-B_i\,r_{T_0}}$ is a decreasing function of $r_{T_0}$ (where $A_i = A(T_i - T_0)$ and $B_i = B(T_i - T_0)$), the coupon bond value

$$
V(r) = \sum_{i=1}^{n} c_i\,A_i\,e^{-B_i\,r}
$$

is also a decreasing function of $r$. Therefore, there exists a unique critical rate $r^*$ satisfying

$$
\sum_{i=1}^{n} c_i\,P(T_0, T_i)\big|_{r_{T_0} = r^*} = 1
$$

equivalently $V(r^*) = 1$.

### Decomposition of the swaption

At the critical rate $r^*$, define the individual bond strikes:

$$
K_i = P(T_0, T_i)\big|_{r_{T_0} = r^*} = A_i\,e^{-B_i\,r^*}
$$

By construction, $\sum_{i=1}^n c_i K_i = 1$. Since each $P(T_0, T_i)$ is monotone decreasing in $r_{T_0}$:

- When $r_{T_0} < r^*$: all $P(T_0, T_i) > K_i$ and the swaption is in the money
- When $r_{T_0} > r^*$: all $P(T_0, T_i) < K_i$ and the swaption is out of the money

The swaption payoff therefore decomposes as

$$
\left(1 - \sum_{i=1}^{n} c_i\,P(T_0, T_i)\right)^+ = \sum_{i=1}^{n} c_i\left(K_i - P(T_0, T_i)\right)^+
$$

This is a portfolio of $n$ put options on zero-coupon bonds.

???+ note "Proof of the decomposition"

    For any $r_{T_0}$, define $g(r) = 1 - \sum c_i P_i(r)$ and $h(r) = \sum c_i (K_i - P_i(r))^+$. When $r < r^*$: $g(r) < 0$ (so $g(r)^+ = 0$) and each $K_i - P_i(r) < 0$ (so $h(r) = 0$). When $r > r^*$: $g(r) > 0$ and each $K_i - P_i(r) > 0$, so

    $$
    h(r) = \sum c_i(K_i - P_i(r)) = \sum c_i K_i - \sum c_i P_i(r) = 1 - V(r) = g(r)
    $$

    Therefore $g(r)^+ = h(r)$ for all $r$. $\square$

### Finding the critical rate

The critical rate $r^*$ is the solution of

$$
\sum_{i=1}^{n} c_i\,A_i\,e^{-B_i\,r^*} = 1
$$

This is a one-dimensional root-finding problem that can be solved efficiently by Newton's method or bisection. The function on the left is strictly decreasing and continuous, guaranteeing existence and uniqueness of $r^*$.

---

## Swaption pricing under CIR

Combining Jamshidian's decomposition with the CIR bond put formula:

$$
\text{Payer Swaption}(t) = \sum_{i=1}^{n} c_i\,\text{Put}_{\text{ZCB}}(t;\,T_0,\,T_i,\,K_i)
$$

Each put $\text{Put}_{\text{ZCB}}(t;\,T_0,\,T_i,\,K_i)$ is evaluated using the CIR closed-form formula with:

- Option expiry: $T_0$
- Bond maturity: $T_i$
- Bond strike: $K_i = A(T_i - T_0)\,e^{-B(T_i - T_0)\,r^*}$

The **receiver swaption** (right to enter a receiver swap) decomposes into a portfolio of call options:

$$
\text{Receiver Swaption}(t) = \sum_{i=1}^{n} c_i\,\text{Call}_{\text{ZCB}}(t;\,T_0,\,T_i,\,K_i)
$$

**Swaption parity**:

$$
\text{Payer}(t) - \text{Receiver}(t) = \text{Swap}(t)
$$

!!! warning "Jamshidian works only for one-factor models"
    The decomposition relies on the monotonicity of all bond prices in a single state variable $r_{T_0}$. In multi-factor models, different bonds can move in different directions for the same state change, and the decomposition fails. Multi-factor swaption pricing requires different techniques (e.g., Monte Carlo or Bermudan swaption methods).

---

## Summary of pricing chain

The following diagram summarizes how CIR prices caps and swaptions.

| Derivative | Decomposition | Building Block |
|:---:|:---:|:---:|
| Caplet | $\longrightarrow$ ZCB put | CIR bond option formula ($\chi^2$) |
| Cap | $= \sum$ caplets | CIR bond option formula ($\chi^2$) |
| Floorlet | $\longrightarrow$ ZCB call | CIR bond option formula ($\chi^2$) |
| Floor | $= \sum$ floorlets | CIR bond option formula ($\chi^2$) |
| Payer swaption | Jamshidian $\longrightarrow \sum$ ZCB puts | CIR bond option formula ($\chi^2$) |
| Receiver swaption | Jamshidian $\longrightarrow \sum$ ZCB calls | CIR bond option formula ($\chi^2$) |

Every derivative in this table ultimately reduces to the CIR zero-coupon bond option formula involving the non-central chi-squared distribution.

---

## Summary

Caplets are equivalent to put options on zero-coupon bonds through a model-independent payoff identity, with bond strike $\tilde{K} = 1/(1+K\delta)$. Swaptions decompose into portfolios of zero-coupon bond options via Jamshidian's trick, which exploits the monotonicity of bond prices in the short rate. Under the CIR model, all building-block bond options have closed-form prices in terms of the non-central chi-squared distribution, making caps and swaptions analytically tractable. This analytical pricing chain --- from swaption to bond option portfolio to chi-squared CDF evaluation --- is a major advantage of the CIR model over non-affine alternatives that require numerical methods at every stage.

---

## Exercises

**Exercise 1.** A caplet has strike $K = 4\%$, reset date $T_i = 2$ years, payment date $T_{i+1} = 2.5$ years, and notional $N = \$1{,}000{,}000$. Compute the day count fraction $\delta_i$ and the equivalent bond put strike $\tilde{K}_i = 1/(1 + K\delta_i)$. How many units of the bond put does the caplet correspond to?

??? success "Solution to Exercise 1"

    The day count fraction is:

    $$
    \delta_i = T_{i+1} - T_i = 2.5 - 2 = 0.5 \text{ years}
    $$

    The equivalent bond put strike is:

    $$
    \tilde{K}_i = \frac{1}{1 + K\delta_i} = \frac{1}{1 + 0.04 \times 0.5} = \frac{1}{1.02} \approx 0.98039
    $$

    The number of units of the bond put is:

    $$
    N(1 + K\delta_i) = 1{,}000{,}000 \times 1.02 = 1{,}020{,}000
    $$

    So the caplet is equivalent to 1,020,000 put options on the zero-coupon bond maturing at $T_{i+1} = 2.5$ years, with exercise date $T_i = 2$ years and bond strike $\tilde{K}_i \approx 0.98039$.

---

**Exercise 2.** Derive the caplet-put equivalence step by step. Starting from the caplet payoff $N\delta_i(L(T_i, T_{i+1}) - K)^+$, substitute $L(T_i, T_{i+1}) = \frac{1}{\delta_i}(1/P(T_i, T_{i+1}) - 1)$ and algebraically manipulate to arrive at $N(1 + K\delta_i)(\tilde{K}_i - P(T_i, T_{i+1}))^+$. Identify which step uses the fact that $(ax - b)^+ = a(x - b/a)^+$ for $a > 0$.

??? success "Solution to Exercise 2"

    Starting from the caplet payoff at $T_{i+1}$:

    $$
    N\delta_i(L(T_i, T_{i+1}) - K)^+
    $$

    **Step 1:** Substitute $L(T_i, T_{i+1}) = \frac{1}{\delta_i}\left(\frac{1}{P(T_i, T_{i+1})} - 1\right)$:

    $$
    N\delta_i\left(\frac{1}{\delta_i}\left(\frac{1}{P(T_i, T_{i+1})} - 1\right) - K\right)^+
    $$

    $$
    = N\left(\frac{1}{P(T_i, T_{i+1})} - 1 - K\delta_i\right)^+
    $$

    **Step 2:** Combine the constant terms:

    $$
    = N\left(\frac{1}{P(T_i, T_{i+1})} - (1 + K\delta_i)\right)^+
    $$

    **Step 3:** Factor out $\frac{1}{P(T_i, T_{i+1})}$ from inside the positive part. Write:

    $$
    = N\left(\frac{1 - (1+K\delta_i)P(T_i, T_{i+1})}{P(T_i, T_{i+1})}\right)^+
    $$

    Since $P(T_i, T_{i+1}) > 0$, this equals:

    $$
    = \frac{N}{P(T_i, T_{i+1})}\left(1 - (1 + K\delta_i)P(T_i, T_{i+1})\right)^+
    $$

    **Step 4:** This is the payoff at $T_{i+1}$. To express as a bond put payoff at $T_i$, note that the payoff $\frac{N}{P(T_i, T_{i+1})}(\cdots)^+$ paid at $T_{i+1}$ has the same present value at $T_i$ as $N(\cdots)^+$ paid at $T_i$ (by discounting). Alternatively, work directly:

    $$
    N\left(1 - (1 + K\delta_i)P(T_i, T_{i+1})\right)^+
    $$

    **Step 5:** This is where we use the identity $(ax - b)^+ = a(x - b/a)^+$ for $a > 0$. Set $a = (1+K\delta_i)$:

    $$
    = N(1 + K\delta_i)\left(\frac{1}{1 + K\delta_i} - P(T_i, T_{i+1})\right)^+
    $$

    $$
    = N(1 + K\delta_i)\left(\tilde{K}_i - P(T_i, T_{i+1})\right)^+
    $$

    This is $N(1+K\delta_i)$ units of a put option on the $T_{i+1}$-bond with strike $\tilde{K}_i$, payable at $T_{i+1}$.

---

**Exercise 3.** Explain why cap-floor parity $\text{Cap}(t) - \text{Floor}(t) = \text{Swap}(t)$ holds model-independently. Start from the identity $(x - K)^+ - (K - x)^+ = x - K$ applied to $x = L(T_i, T_{i+1})$ for each caplet-floorlet pair, and show that the resulting sum equals the swap value.

??? success "Solution to Exercise 3"

    For each caplet-floorlet pair on the interval $[T_i, T_{i+1}]$, the caplet pays $N\delta_i(L_i - K)^+$ and the floorlet pays $N\delta_i(K - L_i)^+$, where $L_i = L(T_i, T_{i+1})$.

    Using the identity $(x - K)^+ - (K - x)^+ = x - K$ for any $x, K$:

    $$
    N\delta_i(L_i - K)^+ - N\delta_i(K - L_i)^+ = N\delta_i(L_i - K)
    $$

    This holds for every realization of $L_i$, so it is a model-independent payoff identity.

    Summing over all periods and discounting to time $t$:

    $$
    \text{Cap}(t) - \text{Floor}(t) = \sum_{i=0}^{n-1} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{T_{i+1}} r_s\,ds}\,N\delta_i(L_i - K)\,\bigg|\,\mathcal{F}_t\right]
    $$

    The right-hand side is exactly the value of a payer swap (receiving floating $L_i$, paying fixed $K$), since each floating-minus-fixed cash flow $N\delta_i(L_i - K)$ is paid at $T_{i+1}$:

    $$
    \text{Cap}(t) - \text{Floor}(t) = \text{Swap}(t)
    $$

    This identity is model-independent because it relies only on the payoff decomposition $(x - K)^+ - (K - x)^+ = x - K$, not on any distributional assumption about $L_i$.

---

**Exercise 4.** For a payer swaption with expiry $T_0 = 1$ year into a 3-year annual swap with fixed rate $K = 5\%$, write out the coupon bond that appears in the swaption payoff. Identify the cash flows $c_1$, $c_2$, $c_3$ and the corresponding maturities $T_1$, $T_2$, $T_3$. Explain why the swaption is exercised when this coupon bond is worth less than par.

??? success "Solution to Exercise 4"

    The payer swaption expiry is $T_0 = 1$ year. The swap is 3-year annual, so payment dates are $T_1 = 2$, $T_2 = 3$, $T_3 = 4$ years.

    The cash flows of the fixed leg are:

    - $c_1 = K\delta_0 = 0.05 \times 1 = 0.05$ at $T_1 = 2$
    - $c_2 = K\delta_1 = 0.05 \times 1 = 0.05$ at $T_2 = 3$
    - $c_3 = 1 + K\delta_2 = 1 + 0.05 \times 1 = 1.05$ at $T_3 = 4$

    The coupon bond appearing in the swaption payoff is:

    $$
    V(r_{T_0}) = c_1 P(T_0, T_1) + c_2 P(T_0, T_2) + c_3 P(T_0, T_3) = 0.05\,P(1,2) + 0.05\,P(1,3) + 1.05\,P(1,4)
    $$

    The swaption payoff at $T_0$ is $(1 - V(r_{T_0}))^+$.

    The swaption is exercised when $V(r_{T_0}) < 1$, meaning the coupon bond is worth less than par. This occurs when the swap has positive value to the payer: paying fixed at $K = 5\%$ is advantageous when market rates are high enough that the present value of the fixed payments is less than par. Higher rates at $T_0$ reduce bond prices $P(T_0, T_i)$, reducing $V$, making exercise more likely.

---

**Exercise 5.** In Jamshidian's decomposition, the critical rate $r^*$ solves $\sum_{i=1}^n c_i A_i e^{-B_i r^*} = 1$. For a 2-year annual swap with $K = 5\%$ (so $c_1 = 0.05$ and $c_2 = 1.05$), and CIR functions $A_1 = 0.99$, $B_1 = 0.95$, $A_2 = 0.97$, $B_2 = 1.85$, set up the equation for $r^*$ and describe how Newton's method would be applied. What is the derivative of the left-hand side with respect to $r^*$?

??? success "Solution to Exercise 5"

    The equation for $r^*$ is:

    $$
    c_1 A_1 e^{-B_1 r^*} + c_2 A_2 e^{-B_2 r^*} = 1
    $$

    $$
    0.05 \times 0.99 \times e^{-0.95\,r^*} + 1.05 \times 0.97 \times e^{-1.85\,r^*} = 1
    $$

    $$
    0.0495\,e^{-0.95\,r^*} + 1.0185\,e^{-1.85\,r^*} = 1
    $$

    Define $g(r) = 0.0495\,e^{-0.95 r} + 1.0185\,e^{-1.85 r}$.

    **Newton's method:** Starting from an initial guess $r^{(0)}$, iterate:

    $$
    r^{(n+1)} = r^{(n)} - \frac{g(r^{(n)}) - 1}{g'(r^{(n)})}
    $$

    **Derivative of the left-hand side:**

    $$
    g'(r^*) = -c_1 B_1 A_1 e^{-B_1 r^*} - c_2 B_2 A_2 e^{-B_2 r^*}
    $$

    $$
    = -0.05 \times 0.95 \times 0.99 \times e^{-0.95\,r^*} - 1.05 \times 1.85 \times 0.97 \times e^{-1.85\,r^*}
    $$

    $$
    = -0.047025\,e^{-0.95\,r^*} - 1.88423\,e^{-1.85\,r^*}
    $$

    The derivative is strictly negative (the function is strictly decreasing in $r^*$), which guarantees existence and uniqueness of the root and ensures Newton's method converges rapidly.

---

**Exercise 6.** After finding $r^*$ in Jamshidian's decomposition, the individual bond strikes are $K_i = A_i e^{-B_i r^*}$. Verify that $\sum c_i K_i = 1$ by construction. Then prove the key identity: when $r_{T_0} > r^*$, we have $P(T_0, T_i) < K_i$ for all $i$ simultaneously, and when $r_{T_0} < r^*$, we have $P(T_0, T_i) > K_i$ for all $i$. Why does this simultaneous crossing property depend on the model being one-factor?

??? success "Solution to Exercise 6"

    **Verification that $\sum c_i K_i = 1$:** By construction, $K_i = A_i e^{-B_i r^*}$, and $r^*$ is defined as the solution to $\sum c_i A_i e^{-B_i r^*} = 1$. Therefore $\sum c_i K_i = \sum c_i A_i e^{-B_i r^*} = 1$.

    **Simultaneous crossing property:** Each bond price $P(T_0, T_i) = A_i e^{-B_i r_{T_0}}$ and its strike $K_i = A_i e^{-B_i r^*}$.

    When $r_{T_0} > r^*$: Since $B_i > 0$ for all $i$, $-B_i r_{T_0} < -B_i r^*$, so $e^{-B_i r_{T_0}} < e^{-B_i r^*}$, which gives $P(T_0, T_i) = A_i e^{-B_i r_{T_0}} < A_i e^{-B_i r^*} = K_i$ for **all** $i$ simultaneously.

    When $r_{T_0} < r^*$: By the same logic, $e^{-B_i r_{T_0}} > e^{-B_i r^*}$, so $P(T_0, T_i) > K_i$ for **all** $i$ simultaneously.

    **Why this depends on the model being one-factor:** The simultaneous crossing property requires that all bond prices are monotone functions of the **same** state variable $r_{T_0}$. In a one-factor model, each $P(T_0, T_i)$ is determined by the single short rate $r_{T_0}$, and since all $B_i > 0$, they all decrease in $r_{T_0}$ simultaneously.

    In a multi-factor model, bond prices depend on multiple state variables (e.g., $r_{T_0}$ and a slope factor $x_{T_0}$). Different bonds have different sensitivities to each factor, so it is possible for $P(T_0, T_1)$ to increase while $P(T_0, T_2)$ decreases (if the factors move in offsetting directions). This breaks the simultaneous crossing property, and Jamshidian's decomposition fails.

---

**Exercise 7.** Consider pricing a 1Y-into-5Y payer swaption under CIR with semi-annual payment dates. How many zero-coupon bond put options appear in the Jamshidian decomposition? If each CIR bond put evaluation requires two non-central chi-squared CDF evaluations, how many $\chi^2$ CDF calls are needed in total? Compare this computational cost to a non-affine model (e.g., Black-Karasinski) where each bond option requires a full tree backward induction.

??? success "Solution to Exercise 7"

    A 1Y-into-5Y payer swaption with semi-annual payments has:

    - Expiry: $T_0 = 1$ year
    - Swap payment dates: $T_1 = 1.5$, $T_2 = 2.0$, $T_3 = 2.5$, $T_4 = 3.0$, $T_5 = 3.5$, $T_6 = 4.0$, $T_7 = 4.5$, $T_8 = 5.0$, $T_9 = 5.5$, $T_{10} = 6.0$

    So there are $n = 10$ payment dates, yielding **10 zero-coupon bond put options** in the Jamshidian decomposition.

    Each CIR bond put uses the put formula, which involves two non-central chi-squared CDF evaluations (one for each of the $\chi^2(x_1; d, \lambda_1)$ and $\chi^2(x_2; d, \lambda_2)$ terms). Therefore:

    $$
    \text{Total } \chi^2 \text{ CDF calls} = 10 \times 2 = 20
    $$

    Plus one root-finding step to determine $r^*$ (typically 5--10 function evaluations, each requiring 10 exponential evaluations).

    **Comparison with non-affine models:** In a Black-Karasinski model (log-normal short rate), there is no closed-form bond option formula. Each of the 10 bond put options would require a full backward induction on a trinomial tree. If the tree has $N$ time steps and $O(N)$ nodes at each step, each bond option pricing requires $O(N^2)$ operations. For $N = 500$ (typical for accurate pricing), each option costs $O(250{,}000)$ operations, and the total is $10 \times 250{,}000 = 2{,}500{,}000$ operations.

    By contrast, the CIR approach requires only 20 chi-squared CDF evaluations (each costing $O(100)$ operations for the series evaluation), totaling $O(2{,}000)$ operations. The CIR model is thus roughly **three orders of magnitude faster** for swaption pricing, which is a major practical advantage when calibrating to a large panel of swaption quotes.
