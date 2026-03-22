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
