# Early Exercise: When and Why

## Introduction

The holder of an American option must decide **at every moment** whether to exercise immediately or continue holding. Early exercise is optimal only when the **intrinsic value exceeds the continuation value**—that is, when the time value of the option has been exhausted.

Understanding the conditions under which early exercise is rational is essential for correct pricing and hedging. The analysis differs fundamentally between puts and calls, and depends critically on dividends.

!!! info "Prerequisites"

    - [American Option Definition](american_option_definition.md) (optimal stopping formulation)
    - [Put-Call Parity](../../ch06/black_scholes_formula/put_call_parity.md) (parity relations)
    - [Properties and Bounds](../../ch06/black_scholes_formula/properties_and_bounds.md) (option value bounds)

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

By the lower bound for European calls (Recall (see [§ Properties and bounds](../../ch06/black_scholes_formula/properties_and_bounds.md))):

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

---

## Exercises

**Exercise 1.** Prove that it is never optimal to exercise an American call early on a non-dividend-paying stock. Use the inequality $C \geq S - Ke^{-r(T-t)} > S - K$ (for $r > 0$, $T > t$) to show that the call is always worth more alive than dead.

??? success "Solution to Exercise 1"
    **Claim:** For a non-dividend-paying stock with $r > 0$ and $t < T$, it is never optimal to exercise an American call early.

    **Proof:** The European call satisfies the lower bound:

    $$
    C_{\text{Eu}}(S_t, t) \geq S_t - Ke^{-r(T-t)}
    $$

    This follows from the put-call parity $C - P = S - Ke^{-r(T-t)}$ and the fact that $P \geq 0$.

    Since $r > 0$ and $T - t > 0$, we have $e^{-r(T-t)} < 1$, so:

    $$
    C_{\text{Eu}}(S_t, t) \geq S_t - Ke^{-r(T-t)} > S_t - K
    $$

    The American call is worth at least as much as the European call: $C_{\text{Am}} \geq C_{\text{Eu}}$. Therefore:

    $$
    C_{\text{Am}}(S_t, t) \geq C_{\text{Eu}}(S_t, t) > S_t - K
    $$

    The option value strictly exceeds the exercise payoff for all $t < T$. Exercising yields $S_t - K$, but selling the option yields at least $C_{\text{Am}} > S_t - K$. Therefore, exercising is always suboptimal, and the call is "worth more alive than dead."

    Since early exercise is never optimal, the American and European calls have the same value: $C_{\text{Am}} = C_{\text{Eu}}$. $\square$

---


**Exercise 2.** For an American put on a non-dividend-paying stock, explain why early exercise can be optimal when the put is sufficiently deep in the money. Specifically, show that the interest earned on the strike proceeds $rK \, dt$ can exceed the time value lost from exercise.

??? success "Solution to Exercise 2"
    For a deep-in-the-money American put ($S_t \ll K$), early exercise can be optimal because the **interest earned** on the strike cash exceeds the **time value lost**.

    **Detailed argument:** Consider the holder of an American put at time $t$ with $S_t$ very small. If the holder exercises immediately, they receive $K - S_t$ in cash. Over a small interval $dt$, this cash earns interest $r(K - S_t) \, dt \approx rK \, dt$ (since $S_t \ll K$).

    If the holder continues, the put value changes by approximately:

    $$
    dP \approx P_t \, dt + P_S \, dS + \frac{1}{2}P_{SS}\sigma^2 S^2 \, dt
    $$

    When $S_t$ is very small, the put is deep in the money: $P_S \approx -1$, $P_{SS} \approx 0$, and the option behaves nearly like the intrinsic value $K - S$. The time value $P - (K - S)$ is small.

    The European put satisfies:

    $$
    P_{\text{Eu}}(S_t, t) \geq Ke^{-r(T-t)} - S_t
    $$

    For small $S_t$, the European put is approximately $Ke^{-r(T-t)} - S_t$, which is less than $K - S_t$ by the amount $K(1 - e^{-r(T-t)})$. This represents the cost of delaying receipt of the strike cash.

    The instantaneous benefit of early exercise over continuation is approximately:

    $$
    r(K - S_t) \, dt - \text{(time value decay avoided)}
    $$

    When $S_t$ is sufficiently small, the interest $rK \, dt$ dominates the time value lost, and early exercise becomes optimal. The critical stock price $S^*(t)$ is determined by the balance between these competing effects.

---


**Exercise 3.** Consider an American call on a stock that pays a discrete dividend $D$ at time $t_d < T$. Explain why it may be optimal to exercise just before the ex-dividend date. Derive the condition on $D$ that makes early exercise worthwhile.

??? success "Solution to Exercise 3"
    **When early exercise of a call may be optimal:** Just before the ex-dividend date $t_d$, the stock price is $S_{t_d^-}$. On the ex-date, the price drops to approximately $S_{t_d^-} - D$.

    If the call holder exercises just before $t_d$:

    - Pay $K$, receive the stock at $S_{t_d^-}$
    - Collect the dividend $D$
    - Net position: stock worth $S_{t_d^-} - D$ (ex-div) plus cash dividend $D$

    If the call holder does not exercise:

    - The option value drops because $S$ drops by $D$: $C(S_{t_d^-} - D, t_d) < C(S_{t_d^-}, t_d^-)$
    - The holder misses the dividend entirely

    **Condition for exercise:** Exercise is worthwhile if the dividend captured exceeds the time value sacrificed. The time value just before the ex-date is:

    $$
    \text{Time value} = C(S_{t_d^-}, t_d^-) - (S_{t_d^-} - K)
    $$

    Just after the ex-date, if the holder had exercised, they would have $S_{t_d^-} - K + D$ invested at rate $r$ for the remaining time $T - t_d$. The interest saved by paying $K$ later rather than now is $K(1 - e^{-r(T - t_d)})$.

    **Derivation of the exercise condition:** Exercise is optimal if the dividend exceeds the interest cost of early payment:

    $$
    D > K\left(1 - e^{-r(T - t_d)}\right)
    $$

    Intuitively, early exercise requires the holder to pay $K$ now rather than at maturity, forgoing interest $K(1 - e^{-r(T-t_d)})$. This cost is worthwhile only if the captured dividend $D$ exceeds it. For small $T - t_d$, the interest cost is approximately $rK(T - t_d)$, so the condition becomes $D > rK(T - t_d)$.

---


**Exercise 4.** The exercise boundary $S^*(t)$ for an American put satisfies $S^*(T) = K$ and $S^*(t) < K$ for $t < T$. At the exercise boundary, two conditions hold: $V(S^*, t) = K - S^*$ (value matching) and $\frac{\partial V}{\partial S}(S^*, t) = -1$ (smooth pasting). Explain the economic intuition behind each condition.

??? success "Solution to Exercise 4"
    **Value-matching condition** $V(S^*, t) = K - S^*$: At the exercise boundary, the option value equals the intrinsic value. This ensures **continuity** of the option price across the boundary.

    **Economic intuition:** If $V(S^*, t) > K - S^*$, the holder in the exercise region is leaving money on the table by exercising, since the option is worth more alive. If $V(S^*, t) < K - S^*$ at the boundary, an arbitrageur could buy the option for $V$ and immediately exercise for a profit of $K - S^* - V > 0$. Either case contradicts optimal behavior.

    **Smooth-pasting condition** $\frac{\partial V}{\partial S}(S^*, t) = -1$: The derivative (delta) of the option price with respect to $S$ must match the derivative of the payoff function at the boundary.

    **Economic intuition:** Consider an investor at the boundary $S = S^*$. For an infinitesimal increase $dS > 0$, the stock moves into the continuation region. The change in the option value is $V_S \, dS$, and the change in the intrinsic value is $-dS$. If $V_S \neq -1$ at $S^*$, the investor could exploit the discontinuity in the delta:

    - If $V_S > -1$ at $S^*$: Moving slightly above $S^*$ into the continuation region, the option loses less value than the intrinsic value. The holder could profit by a strategy that exploits this kink.
    - If $V_S < -1$ at $S^*$: The opposite arbitrage applies.

    Smooth pasting is a necessary condition for the **optimality** of $S^*(t)$ and can be derived from the variational characterization of the free boundary. It provides the additional equation needed (beyond value-matching) to uniquely determine the unknown boundary.

---


**Exercise 5.** Compare the early exercise behavior of American calls and puts by filling in a table with the following columns: option type (call/put), dividend status (yes/no), early exercise possible (yes/no), and economic reason. Cover all four combinations.

??? success "Solution to Exercise 5"
    | Option Type | Dividend Status | Early Exercise Possible? | Economic Reason |
    |---|---|---|---|
    | American call | No dividends | **No** | $C \geq S - Ke^{-r(T-t)} > S - K$; time value + interest savings are always positive |
    | American call | With dividends | **Yes** | Exercising before ex-div date captures dividend $D$; optimal if $D > K(1 - e^{-r\Delta t})$ |
    | American put | No dividends | **Yes** | Deep ITM puts benefit from early exercise: interest on $K - S$ cash exceeds remaining time value |
    | American put | With dividends | **Yes** | Same as no-dividend case, but dividends reduce the stock price over time, making exercise less urgent (dividends work against put early exercise since they push $S$ lower, increasing the option's future payoff potential) |

    **Key asymmetry between calls and puts:** For calls without dividends, the holder benefits from paying $K$ later (earning interest on $K$) and retaining insurance against $S$ dropping below $K$. Both effects favor continuation. For puts, the holder receives $K$ upon exercise and can earn interest on it; when the option is deep in the money, this interest exceeds the remaining time value and insurance value.

    Dividends break the no-early-exercise result for calls because the holder misses dividend payments while holding the option instead of the stock. For puts, dividends actually reduce the incentive to exercise early because future stock price declines (from dividends) increase the put's future payoff.

---


**Exercise 6.** An American call on a stock paying continuous dividends at rate $q > 0$ may be exercised early. Show that the critical dividend yield $q^*$ above which early exercise becomes possible depends on $r$, $\sigma$, and $T$. For $r = 5\%$, $\sigma = 20\%$, $T = 1$, estimate $q^*$ numerically using a binomial tree.

??? success "Solution to Exercise 6"
    For a stock paying continuous dividends at rate $q$, the lower bound for the European call becomes:

    $$
    C_{\text{Eu}} \geq S e^{-q(T-t)} - Ke^{-r(T-t)}
    $$

    The exercise payoff is $S - K$. Early exercise is never optimal if:

    $$
    Se^{-q(T-t)} - Ke^{-r(T-t)} \geq S - K
    $$

    Rearranging:

    $$
    K(1 - e^{-r(T-t)}) \geq S(1 - e^{-q(T-t)})
    $$

    For an at-the-money option ($S = K$), this simplifies to $1 - e^{-r(T-t)} \geq 1 - e^{-q(T-t)}$, i.e., $q \leq r$. So when $q > r$, early exercise may become optimal.

    However, the precise critical yield $q^*$ depends on $\sigma$ and $T$ because the option's time value also includes a volatility component. Higher $\sigma$ increases the value of continuation (more optionality), raising $q^*$. Longer $T$ increases both the dividend loss and the time value, with the net effect depending on the parameter regime.

    **Numerical estimation:** For $r = 0.05$, $\sigma = 0.20$, $T = 1$, one builds a binomial tree with the dividend-adjusted risk-neutral probability $q_{\text{RN}} = (e^{(r-q)\Delta t} - d)/(u-d)$ and checks whether the American call price exceeds the European call price.

    - For $q = 0$: $C_{\text{Am}} = C_{\text{Eu}}$ (no early exercise)
    - For $q = 0.02$: $C_{\text{Am}} \approx C_{\text{Eu}}$ (early exercise premium negligible)
    - For $q = 0.04$: $C_{\text{Am}}$ begins to exceed $C_{\text{Eu}}$ slightly
    - For $q = 0.05$: $C_{\text{Am}} > C_{\text{Eu}}$ clearly (early exercise is optimal for sufficiently high $S$)

    The critical yield is approximately $q^* \approx 0.03$--$0.04$ for these parameters. This is slightly below $r = 0.05$ because the option's time value provides some buffer. The exact threshold can be found by searching for the smallest $q$ at which any node in the binomial tree triggers early exercise.
