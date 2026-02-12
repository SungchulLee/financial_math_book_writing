# Early Exercise: When and Why

## Introduction

The holder of an American option must decide **at every moment** whether to exercise immediately or continue holding. Early exercise is optimal only when the **intrinsic value exceeds the continuation value**—that is, when the time value of the option has been exhausted.

Understanding the conditions under which early exercise is rational is essential for correct pricing and hedging. The analysis differs fundamentally between puts and calls, and depends critically on dividends.

!!! info "Prerequisites"
    - [American Option Definition](american_option_definition.md) (optimal stopping formulation)
    - [Put-Call Parity](../black_scholes_formula/put_call_parity.md) (parity relations)
    - [Properties and Bounds](../black_scholes_formula/properties_and_bounds.md) (option value bounds)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Prove that American calls on non-dividend-paying stocks are never exercised early
    2. Explain why American puts may be exercised early
    3. Identify the role of dividends in call early exercise
    4. Decompose the early exercise premium

---

## American Calls on Non-Dividend-Paying Stocks

### The No-Early-Exercise Theorem

!!! tip "Key Result"
    For a **non-dividend-paying stock**, it is **never optimal** to exercise an American call option before maturity. Therefore:
    
    $$
    C_{\text{American}}(S, t) = C_{\text{European}}(S, t)
    $$

### Proof

Consider an American call with strike $K$ and maturity $T$. At any time $t < T$, the holder can either:

**Option A — Exercise now:** Receive $S_t - K$.

**Option B — Sell the option:** Receive at least $C_{\text{European}}(S_t, t)$.

By the lower bound for European calls:

$$
C_{\text{European}}(S_t, t) \geq S_t - K e^{-r(T-t)}
$$

Since $r > 0$ and $T - t > 0$:

$$
C_{\text{European}}(S_t, t) \geq S_t - K e^{-r(T-t)} > S_t - K
$$

Therefore selling the option always dominates exercising. The option is worth more alive than dead.

!!! note "Intuition: Three Sources of Value Lost by Early Exercise"
    Exercising an American call early sacrifices:
    
    1. **Time value**: The possibility that $S_T$ may rise further
    2. **Interest on the strike**: Paying $K$ now rather than $K e^{-r(T-t)}$ later
    3. **Insurance value**: Protection against $S_T$ falling below $K$

---

## American Puts: Early Exercise Can Be Optimal

### Why Puts Differ

The analogous argument **fails** for puts. The lower bound for a European put is:

$$
P_{\text{European}}(S_t, t) \geq K e^{-r(T-t)} - S_t
$$

When the put is deep in-the-money ($S_t \ll K$), the **immediate exercise value** is:

$$
K - S_t > K e^{-r(T-t)} - S_t = K\left(1 - e^{-r(T-t)}\right) + (K e^{-r(T-t)} - S_t)
$$

The European put value can be **less than** the intrinsic value $K - S_t$ because discounting the strike reduces the continuation value. The holder can earn interest on the cash received from exercise.

!!! example "When Early Exercise Is Optimal"
    Consider $K = 100$, $S_t = 20$, $r = 0.10$, $T - t = 1$:
    
    - **Exercising**: receive $K - S_t = 80$ immediately, invest at $r$ to get $80 e^{0.10} \approx 88.4$
    - **Holding**: the put is deep ITM and $S_t$ has little room to fall further; the additional optionality is negligible
    
    The interest earned on $80$ exceeds any remaining time value.

### The Early Exercise Premium for Puts

The American put price decomposes as:

$$
\boxed{
P_{\text{American}}(S, t) = P_{\text{European}}(S, t) + \text{EEP}(S, t)
}
$$

The early exercise premium $\text{EEP}$ is always non-negative and increases as:

- The option goes deeper in-the-money
- Interest rates increase (greater benefit of receiving cash early)
- Time to maturity increases (more opportunities to exercise optimally)
- Volatility decreases (less optionality value remaining)

---

## American Calls on Dividend-Paying Stocks

### When Early Exercise Becomes Optimal

For dividend-paying stocks, early exercise of American calls **may be optimal** just before **ex-dividend dates**. The logic is:

1. On the ex-dividend date, the stock price drops by approximately the dividend amount $D$.
2. The call holder does not receive the dividend.
3. By exercising just before the ex-dividend date, the holder:
    - Pays $K$ to receive the stock
    - Captures the dividend $D$
    - The net benefit of exercise is $D$ minus the time value sacrificed

!!! tip "Early Exercise Rule for Calls"
    Exercise is potentially optimal just before the ex-dividend date if:
    
    $$
    \boxed{D > K\left(1 - e^{-r \Delta t}\right)}
    $$
    
    where $\Delta t$ is the time remaining to maturity after the dividend date. The dividend must exceed the interest savings from deferring the strike payment.

### Multiple Dividend Dates

With multiple dividends at dates $t_1 < t_2 < \cdots < t_m$ before $T$, the exercise decision must be evaluated **at each dividend date**, working backward from maturity. At each date $t_k$:

- Compare the value of exercising (receiving $S_{t_k} - K + D_k$) against continuing
- The decision depends on all future dividends and the remaining time value

---

## The Exercise Boundary

### Definition

The **optimal exercise boundary** $S^*(t)$ is the critical asset price at which early exercise becomes optimal:

- **American put**: exercise when $S_t \leq S^*(t)$
- **American call (with dividends)**: exercise when $S_t \geq S^*(t)$

### Properties of the Put Exercise Boundary

The exercise boundary for an American put satisfies:

| Property | Description |
|---|---|
| Terminal value | $S^*(T) = K$ (at maturity, exercise when ITM) |
| Monotonicity | $S^*(t)$ is non-decreasing as $t \to T$ |
| Lower bound | $S^*(t) \geq K \cdot \min\left(1, \frac{r}{\sigma^2/2}\right)$ for large $T - t$ |
| Dependence on $r$ | $S^*(t)$ decreases as $r$ increases |
| Dependence on $\sigma$ | $S^*(t)$ decreases as $\sigma$ increases |

!!! warning "No Closed-Form Boundary"
    The exercise boundary $S^*(t)$ cannot be expressed in closed form except for **perpetual options** (where $T = \infty$ and the boundary is a constant). For finite maturity, $S^*(t)$ must be computed numerically.

---

## Decomposition Summary

| Option Type | Stock Type | Early Exercise? | Reason |
|---|---|---|---|
| American call | No dividends | **Never** | Time value + interest savings always positive |
| American call | With dividends | **Possibly**, before ex-div | Dividend capture may exceed time value |
| American put | Any | **Possibly**, when deep ITM | Interest on received cash exceeds time value |

---

## Summary

$$
\boxed{
\text{Exercise early} \iff \Phi(S_t) > \mathbb{E}^{\mathbb{Q}}\left[e^{-r\Delta t} V(t + \Delta t, S_{t+\Delta t}) \mid S_t\right]
}
$$

| Aspect | Description |
|---|---|
| Call (no dividends) | Never exercise early: $C_{\text{Am}} = C_{\text{Eu}}$ |
| Call (with dividends) | May exercise just before ex-dividend dates |
| Put | May exercise when deep ITM (interest > time value) |
| Exercise boundary | $S^*(t)$ separates exercise and continuation regions |
| Key trade-off | Immediate payoff vs. future optionality + time value |

**Early exercise analysis reveals a fundamental asymmetry between calls and puts: while call exercise sacrifices time value and interest, put exercise can generate interest that dominates the remaining optionality.**
