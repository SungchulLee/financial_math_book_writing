# American and Bermudan Exercise on Tree

The most compelling application of the Hull-White trinomial tree is pricing derivatives with early exercise features. European options have closed-form solutions via the bond option formula or Jamshidian's trick, but American and Bermudan options require comparing the continuation value against the exercise value at each eligible node. The tree handles this naturally by modifying the backward induction to include an exercise test at each step. The primary application in interest rate markets is the Bermudan swaption, which is one of the most actively traded exotic derivatives.

## Optimal Stopping on a Tree

The price of an American-style derivative is the solution to the optimal stopping problem

$$
V_0 = \sup_{\tau \in \mathcal{T}} \mathbb{E}^{\mathbb{Q}}\!\left[\frac{g(\tau, r_\tau)}{M(\tau)}\right]
$$

where $\mathcal{T}$ is the set of stopping times adapted to the filtration, and $g(\tau, r_\tau)$ is the exercise payoff at time $\tau$.

On the tree, this becomes a discrete dynamic programming problem. At each node $(i, j)$, the holder compares the exercise value $E_{ij}$ with the continuation value $C_{ij}$ and chooses the maximum:

$$
V_{ij} = \max\!\left(C_{ij},\; E_{ij}\right)
$$

where the continuation value is the discounted expected value from the previous section:

$$
C_{ij} = e^{-r_{ij}\,\Delta t} \sum_{\ell} p_\ell(j)\,V_{i+1,\,m_\ell(j)}
$$

and $E_{ij} = g(t_i, r_{ij})$ is the payoff from immediate exercise.

## Bermudan Exercise

A Bermudan option can be exercised only at a discrete set of dates $\mathcal{E} = \{T_{e_1}, T_{e_2}, \ldots, T_{e_K}\}$. The backward induction is modified as follows:

$$
V_{ij} = \begin{cases}
\max(C_{ij},\; E_{ij}) & \text{if } t_i \in \mathcal{E} \\
C_{ij} & \text{if } t_i \notin \mathcal{E}
\end{cases}
$$

The exercise test is performed only at the allowed exercise dates. At all other time steps, the value equals the continuation value.

**Algorithm (Bermudan Backward Induction).**

1. At the final time step $t_N$, set $V_{N,j} = g(t_N, r_{N,j})$ if $t_N \in \mathcal{E}$, otherwise $V_{N,j} = 0$
2. For $i = N-1, N-2, \ldots, 0$:
    - Compute continuation value: $C_{ij} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell V_{i+1, m_\ell}$
    - If $t_i \in \mathcal{E}$: set $V_{ij} = \max(C_{ij}, E_{ij})$
    - Otherwise: set $V_{ij} = C_{ij}$
3. The Bermudan option price is $V_{0,0}$

## Bermudan Swaption

The most important application is the Bermudan payer swaption. The holder has the right to enter a payer swap at any of the exercise dates $T_{e_1}, T_{e_2}, \ldots, T_{e_K}$, where typically $T_{e_k} = T_{k-1}$ (one period before each swap payment date).

At exercise date $T_{e_k}$, the exercise value is the value of entering a payer swap starting at $T_{e_k}$ with remaining payments at $T_{k}, T_{k+1}, \ldots, T_n$:

$$
E_{e_k, j} = N\!\left[P(T_{e_k}, T_{e_k}; r_j) - P(T_{e_k}, T_n; r_j) - K_{\text{swap}} \sum_{i=k}^{n} \delta_i\,P(T_{e_k}, T_i; r_j)\right]
$$

where all bond prices are computed from the affine formula at node $j$. As the exercise date moves later, fewer swap payments remain, so the exercise value generally decreases.

!!! tip "Exercise Boundary"
    The exercise boundary $r^*(t_i)$ separates the exercise region from the continuation region at each exercise date. For a Bermudan payer swaption, the holder exercises when $r_{T_i}$ is low enough (making the swap valuable). The critical rate $r^*(t_i)$ is implicitly determined by $C(r^*) = E(r^*)$ and can be extracted from the tree after backward induction.

## American Bond Options

An American put option on a zero-coupon bond with strike $K$ and maturity $T_{\text{opt}}$ allows exercise at any time $t \leq T_{\text{opt}}$:

$$
E_{ij} = \max\!\left(K - P(t_i, S; r_{ij}),\; 0\right)
$$

where $S > T_{\text{opt}}$ is the bond maturity. The backward induction applies the exercise test at every time step:

$$
V_{ij} = \max\!\left(e^{-r_{ij}\Delta t}\sum_\ell p_\ell V_{i+1,m_\ell},\;\; K - P(t_i, S; r_{ij})\right)
$$

for $i = 0, 1, \ldots, N_{\text{opt}}$ where $N_{\text{opt}}$ corresponds to $T_{\text{opt}}$.

## Callable Bonds on the Tree

A callable bond is a coupon bond where the issuer has the right to redeem at the call price $K_{\text{call}}$ on specified call dates. From the bondholder's perspective, the callable bond value is

$$
V_{\text{callable}} = V_{\text{straight}} - V_{\text{issuer call}}
$$

On the tree, the callable bond is priced by backward induction with the following modification at call dates: the issuer calls if the bond value exceeds $K_{\text{call}}$, so

$$
V_{ij} = \min\!\left(C_{ij} + c_i,\;\; K_{\text{call}}\right)
$$

where $c_i$ is the coupon at time $t_i$ (zero if not a coupon date). The $\min$ reflects the issuer's optimal strategy: cap the bondholder's value at $K_{\text{call}}$.

???+ example "Bermudan Swaption Pricing"
    Consider a Bermudan payer swaption on a 5-year swap with annual payments and fixed rate $K = 3\%$. Exercise is allowed annually at $T = 1, 2, 3, 4$ years.

    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)

        # Build and calibrate tree
        N = 100
        T_max = 5.0
        tree = build_hw_tree(hw, N, T_max)

        # Exercise dates and swap structure
        exercise_dates = [1.0, 2.0, 3.0, 4.0]
        payment_dates = [1.0, 2.0, 3.0, 4.0, 5.0]
        K_swap = 0.03

        # Backward induction with Bermudan exercise
        V = backward_induction_bermudan(
            tree, exercise_dates, payment_dates, K_swap
        )
        print(f"Bermudan swaption price: {V[0][0]:.6f}")
    ```

## Early Exercise Premium

The early exercise premium is the difference between the Bermudan and European option prices:

$$
\text{EEP} = V_{\text{Bermudan}} - V_{\text{European}}
$$

The European swaption is priced on the same tree but without the exercise test (only the first exercise date is allowed). The EEP is always non-negative and represents the value of the optionality to exercise early.

For Bermudan swaptions, the EEP is typically 5--15\% of the European value, depending on the mean-reversion parameter $\lambda$ and the slope of the yield curve. Higher mean-reversion reduces the EEP because it limits the range of future rate movements, making early exercise less attractive.

## Convergence and Accuracy

The tree price for American/Bermudan options converges to the continuous-time price as $\Delta t \to 0$. However, the convergence can be non-monotone due to the discrete exercise boundary not aligning with the continuous optimal boundary.

!!! warning "Exercise Date Alignment"
    For Bermudan options, the tree time steps should be chosen so that the exercise dates $\mathcal{E}$ fall exactly on tree time steps. If an exercise date falls between two tree steps, interpolation introduces error. A practical approach is to set $\Delta t$ as a divisor of all exercise date spacings.

Richardson extrapolation can accelerate convergence: compute the price on trees with $N$ and $2N$ steps, then form $V_{\text{ext}} = 2V_{2N} - V_N$, which eliminates the leading-order error term.

## Summary

American and Bermudan exercise on the Hull-White trinomial tree extends backward induction by comparing continuation and exercise values: $V_{ij} = \max(C_{ij}, E_{ij})$ at eligible exercise dates. The primary application is the Bermudan swaption, where the holder may enter a swap at any of several dates. Callable bonds use $\min(C_{ij}, K_{\text{call}})$ reflecting the issuer's optimal call strategy. The early exercise premium, the excess over the European value, is typically 5--15\% for Bermudan swaptions. Convergence improves when tree time steps align with exercise dates, and Richardson extrapolation accelerates the convergence rate.

---

## Exercises

**Exercise 1.** For a Bermudan payer swaption with exercise dates at years 1, 2, and 3 on a 4-year swap, describe the exercise value $E_{ij}$ at each exercise date. How does the number of remaining swap payments affect $E_{ij}$, and why does the exercise value generally decrease at later exercise dates (for a given short rate)?

??? success "Solution to Exercise 1"
    At each exercise date $T_{e_k}$ ($k = 1, 2, 3$ corresponding to years 1, 2, 3), the holder can enter a payer swap with the remaining payment schedule.

    **At $T_{e_1} = 1$:** The swap has payments at years 1, 2, 3, 4 (four remaining payments):

    $$
    E_{e_1, j} = N\!\left[1 - P(1, 4; r_j) - K_{\text{swap}} \sum_{i=1}^{4} \delta_i\,P(1, T_i; r_j)\right]
    $$

    **At $T_{e_2} = 2$:** The swap has payments at years 2, 3, 4 (three remaining payments):

    $$
    E_{e_2, j} = N\!\left[1 - P(2, 4; r_j) - K_{\text{swap}} \sum_{i=2}^{4} \delta_i\,P(2, T_i; r_j)\right]
    $$

    **At $T_{e_3} = 3$:** The swap has payments at years 3, 4 (two remaining payments):

    $$
    E_{e_3, j} = N\!\left[1 - P(3, 4; r_j) - K_{\text{swap}} \sum_{i=3}^{4} \delta_i\,P(3, T_i; r_j)\right]
    $$

    The exercise value generally decreases at later exercise dates (for a given short rate) because fewer swap payments remain. The swap's fixed leg annuity factor $\sum_i \delta_i P(T_{e_k}, T_i; r_j)$ and the floating leg $1 - P(T_{e_k}, T_n; r_j)$ both shrink as the number of remaining payments decreases, but the net swap value (which depends on the difference between floating and fixed legs) typically decreases, making the option less valuable at later dates.

---

**Exercise 2.** Explain why the Bermudan backward induction uses $V_{ij} = C_{ij}$ at non-exercise dates but $V_{ij} = \max(C_{ij}, E_{ij})$ at exercise dates. What would go wrong if the exercise test were applied at every time step for a Bermudan option?

??? success "Solution to Exercise 2"
    A Bermudan option has contractually specified exercise dates $\mathcal{E}$. The holder is not permitted to exercise at dates outside $\mathcal{E}$. Therefore:

    - At $t_i \in \mathcal{E}$: the holder has the choice to exercise (receiving $E_{ij}$) or continue (receiving $C_{ij}$), so $V_{ij} = \max(C_{ij}, E_{ij})$.
    - At $t_i \notin \mathcal{E}$: the holder cannot exercise and must continue, so $V_{ij} = C_{ij}$.

    **What would go wrong:** If the exercise test were applied at every time step, the Bermudan option would become an American option, which has a higher value because the holder has more exercise opportunities. The price would be overestimated, violating the contract terms. For example, a Bermudan swaption exercisable annually at years 1, 2, 3, 4 would be mispriced as an American swaption exercisable at any time, which is a strictly more valuable instrument.

---

**Exercise 3.** For a callable bond, the backward induction uses $\min(C_{ij} + c_i, K_{\text{call}})$ at call dates. Explain why the issuer's optimal strategy corresponds to a $\min$ rather than a $\max$. How does the callable bond value relate to the straight bond value and the issuer's call option value?

??? success "Solution to Exercise 3"
    For a callable bond, the issuer (not the holder) has the option to call. The issuer will exercise the call when it is beneficial to the issuer, which is when the bond's continuation value exceeds the call price $K_{\text{call}}$ --- because the issuer can retire expensive debt cheaply.

    Using $\min$ rather than $\max$: from the bondholder's perspective, the bond value is capped at $K_{\text{call}}$ on call dates because the issuer will redeem the bond if its value exceeds $K_{\text{call}}$. Therefore:

    $$
    V_{ij} = \min(C_{ij} + c_i, K_{\text{call}})
    $$

    The $\min$ reflects that the bondholder receives the lesser of the continuation value and the call price.

    The relationship to the straight bond and call option:

    $$
    V_{\text{callable}} = V_{\text{straight}} - V_{\text{issuer call}}
    $$

    The issuer's call option value is $V_{\text{issuer call}} = V_{\text{straight}} - V_{\text{callable}} \geq 0$. The bondholder has effectively sold a call option to the issuer, so the callable bond is worth less than the straight bond.

---

**Exercise 4.** The exercise boundary $r^*(t_i)$ for a Bermudan payer swaption is the rate at which $C(r^*) = E(r^*)$. On the tree, describe how to extract $r^*(t_i)$ from the backward induction values at exercise date $t_i$. Would you use interpolation between nodes, and if so, what method?

??? success "Solution to Exercise 4"
    At each exercise date $t_i \in \mathcal{E}$, after backward induction, we have $C_{ij}$ (continuation value) and $E_{ij}$ (exercise value) at every node $j$.

    The exercise boundary $r^*(t_i)$ is the critical short rate where $C(r^*) = E(r^*)$, i.e., the holder is indifferent between exercising and continuing.

    **Extraction procedure:**

    1. For each exercise date $t_i$, scan the nodes from $j = -j_{\max}$ to $j = j_{\max}$.
    2. Find the pair of adjacent nodes $j^*$ and $j^* + 1$ where the exercise decision changes: $V_{i,j^*} = E_{i,j^*}$ (exercise) and $V_{i,j^*+1} = C_{i,j^*+1}$ (continue), or vice versa.
    3. The exercise boundary lies between the short rates $r_{i,j^*} = \alpha_i + j^*\Delta x$ and $r_{i,j^*+1} = \alpha_i + (j^*+1)\Delta x$.

    **Interpolation:** Linear interpolation between the two bracketing nodes gives a more accurate estimate:

    $$
    r^*(t_i) \approx r_{i,j^*} + \frac{C_{i,j^*} - E_{i,j^*}}{(C_{i,j^*} - E_{i,j^*}) - (C_{i,j^*+1} - E_{i,j^*+1})} \cdot \Delta x
    $$

    This finds the rate where $C - E$ changes sign by linear interpolation. For higher accuracy, cubic interpolation on the difference $C_{ij} - E_{ij}$ could be used.

---

**Exercise 5.** Richardson extrapolation combines tree prices with $N$ and $2N$ steps via $V_{\text{ext}} = 2V_{2N} - V_N$. Derive this formula assuming the tree price has an error of the form $V_N = V_{\text{true}} + c\Delta t + O(\Delta t^2)$. What order of convergence does the extrapolated price achieve?

??? success "Solution to Exercise 5"
    Assume the tree price has an asymptotic expansion in $\Delta t$:

    $$
    V_N = V_{\text{true}} + c\,\Delta t + O(\Delta t^2)
    $$

    With $N$ steps, $\Delta t = T/N$. With $2N$ steps, $\Delta t' = T/(2N) = \Delta t/2$. Therefore:

    $$
    V_N = V_{\text{true}} + c\,\Delta t + O(\Delta t^2)
    $$

    $$
    V_{2N} = V_{\text{true}} + c\,\frac{\Delta t}{2} + O(\Delta t^2)
    $$

    Subtracting: $V_N - V_{2N} = c\,\frac{\Delta t}{2} + O(\Delta t^2)$.

    Forming the Richardson extrapolant:

    $$
    V_{\text{ext}} = 2V_{2N} - V_N = 2\!\left(V_{\text{true}} + \frac{c\Delta t}{2}\right) - \left(V_{\text{true}} + c\Delta t\right) + O(\Delta t^2) = V_{\text{true}} + O(\Delta t^2)
    $$

    The leading-order $O(\Delta t)$ error term cancels, and the extrapolated price achieves $O(\Delta t^2)$ convergence --- a second-order method constructed from two first-order computations.

---

**Exercise 6.** The early exercise premium (EEP) for a Bermudan swaption is typically 5--15% of the European value. Explain qualitatively why the EEP increases with volatility $\sigma$ and decreases with mean-reversion speed $\lambda$. For a flat yield curve at $r_0 = K_{\text{swap}}$, would the EEP be larger or smaller than for a steep upward-sloping curve?

??? success "Solution to Exercise 6"
    **EEP increases with volatility $\sigma$:** Higher volatility means the short rate can reach more extreme values in the future, increasing the potential payoff from waiting. However, it also means that the swap can become very valuable (when rates move favorably), making early exercise tempting. The net effect is that higher volatility increases the value of optionality, and since the EEP represents the value of the additional exercise opportunities, it increases with $\sigma$.

    **EEP decreases with mean-reversion $\lambda$:** Stronger mean reversion pulls rates back toward the long-run mean, reducing the range of future rate movements. With less rate variability, the difference between exercising now and waiting is smaller, so the additional exercise dates are less valuable. The EEP thus decreases as $\lambda$ increases.

    **Flat curve at $r_0 = K_{\text{swap}}$:** With a flat yield curve at the swap rate, the swap is at-the-money at inception, and the swaption has significant time value. The EEP tends to be moderate because there is no intrinsic value advantage to exercising early.

    **Steep upward-sloping curve:** With a steep curve, forward rates exceed the current short rate. If $K_{\text{swap}}$ equals the current short rate, the swap becomes more in-the-money as we look further out (since forward rates are above $K_{\text{swap}}$). Early exercise sacrifices this increasing intrinsic value, but the steep curve also means rates are expected to rise, potentially making the swap less attractive later. The EEP would generally be **smaller** for a steep upward-sloping curve because the term structure implies that rates will rise, reducing the benefit of the payer swap and making early exercise less attractive compared to the flat curve case.

---

**Exercise 7.** An American put option on a ZCB with maturity $S = 5$, strike $K = 0.95$, and option expiry $T_{\text{opt}} = 3$ allows exercise at any time $t \leq 3$. Describe the backward induction on the tree, including the exercise value formula $E_{ij} = \max(K - P(t_i, S; r_{ij}), 0)$ at each node. When would early exercise be optimal for this option?

??? success "Solution to Exercise 7"
    **Backward induction for the American put on a ZCB:**

    1. **Terminal condition:** At the option expiry $T_{\text{opt}} = 3$ (corresponding to tree time step $N_{\text{opt}}$), set

        $$
        V_{N_{\text{opt}}, j} = \max(K - P(3, 5; r_{N_{\text{opt}},j}),\; 0) = \max(0.95 - e^{A(3,5) + B(3,5)\,r_{3,j}},\; 0)
        $$

    2. **Backward induction with exercise test:** For $i = N_{\text{opt}} - 1, \ldots, 0$:

        - Compute continuation value: $C_{ij} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell\,V_{i+1, m_\ell}$
        - Compute exercise value: $E_{ij} = \max(0.95 - P(t_i, 5; r_{ij}),\; 0)$
        - Set $V_{ij} = \max(C_{ij}, E_{ij})$

    3. **Price:** $V_{0,0}$

    **When is early exercise optimal?** The American put is exercised when the exercise value exceeds the continuation value, i.e., $E_{ij} > C_{ij}$. This occurs when:

    - The short rate $r_{ij}$ is high enough that the bond price $P(t_i, 5; r_{ij})$ is well below the strike $K = 0.95$ (the put is deep in the money).
    - The remaining time to option expiry $T_{\text{opt}} - t_i$ is small enough that the time value of waiting is low.
    - Mean reversion is expected to pull rates back down, which would increase the bond price and reduce the put's intrinsic value.

    Intuitively, early exercise is optimal when rates are high (putting the put deep in the money) and the interest earned on the \$0.95 received upon exercise exceeds the expected future gain from continuing to hold the option.
