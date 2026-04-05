# Pricing Derivatives on Tree

Once the Hull-White trinomial tree is constructed and calibrated to the initial yield curve, it becomes a versatile engine for pricing interest rate derivatives. The fundamental technique is backward induction: starting from the terminal payoff at the final time step, derivative values are rolled back through the tree by computing discounted expected values at each node. This section covers the backward induction algorithm and its application to European bond options, caps, floors, and swaptions.

## Backward Induction

The price of a derivative at node $(i, j)$ is the discounted expected continuation value:

$$
V_{ij} = e^{-r_{ij}\,\Delta t} \sum_{\ell} p_\ell(j)\,V_{i+1,\,m_\ell(j)}
$$

where $r_{ij} = \alpha_i + j\,\Delta x$ is the short rate at node $(i,j)$, $p_\ell(j)$ are the branching probabilities (up, middle, down), and $m_\ell(j)$ are the successor node indices determined by the branching pattern.

For normal branching from node $j$:

$$
V_{ij} = e^{-r_{ij}\,\Delta t}\left[p_u\,V_{i+1,\,j+1} + p_m\,V_{i+1,\,j} + p_d\,V_{i+1,\,j-1}\right]
$$

The algorithm proceeds from time $t_N$ (terminal condition) backward to time $t_0$ (present value).

**Algorithm (Backward Induction).**

1. At the final time step $t_N$, set $V_{N,j} = g(r_{N,j})$ for all nodes $j$, where $g$ is the terminal payoff function
2. For $i = N-1, N-2, \ldots, 0$:
    - For each node $j$ at time $t_i$, compute

$$
V_{ij} = e^{-r_{ij}\,\Delta t} \sum_{\ell} p_\ell(j)\,V_{i+1,\,m_\ell(j)}
$$

3. The derivative price is $V_{0,0}$

!!! tip "Computational Cost"
    Backward induction requires $O(1)$ work per node and traverses all nodes once, giving a total cost of $O(N \cdot j_{\max})$ --- the same as the forward calibration pass.

## Pricing Zero-Coupon Bonds

As a consistency check, the tree should recover the market zero-coupon bond prices. A ZCB maturing at $t_N$ has terminal payoff $V_{N,j} = 1$ for all $j$. Backward induction yields $V_{0,0} = P^{\text{tree}}(0, t_N)$, which should match $P^M(0, t_N)$ by the calibration construction.

More generally, a ZCB maturing at $t_K$ ($K < N$) has payoff $1$ at time $t_K$. The backward induction starts from $V_{K,j} = 1$ for all $j$ and rolls back to $t_0$.

## Pricing Zero-Coupon Bond Options

A European call option on a ZCB $P(T, S)$ with strike $K$ and expiry $T$ has payoff at time $T$:

$$
V_{T,j} = \max\!\left(P(T, S; r_{T,j}) - K,\; 0\right)
$$

where $P(T, S; r_{T,j})$ is the bond price at node $(T, j)$ computed from the affine formula:

$$
P(T, S; r_{T,j}) = \exp\!\bigl(A(T, S) + B(T, S)\,r_{T,j}\bigr)
$$

Alternatively, if $S$ falls on a tree time step $t_M$, the bond price can be computed by a separate backward induction from $t_M$ (with terminal values $1$) back to $t_T$.

The option is then priced by backward induction from time $T$ to time $0$.

???+ example "ZCB Call Option on Tree"
    Consider a call option expiring at $T = 2$ on a ZCB maturing at $S = 5$, with strike $K = 0.90$.

    1. At each node $(2, j)$, compute $P(2, 5; r_{2,j}) = \exp(A(2,5) + B(2,5)\,r_{2,j})$
    2. Set $V_{2,j} = \max(P(2,5; r_{2,j}) - 0.90,\; 0)$
    3. Roll back: $V_{1,j} = e^{-r_{1,j}\Delta t}[p_u V_{2,j+1} + p_m V_{2,j} + p_d V_{2,j-1}]$
    4. Roll back: $V_{0,0} = e^{-r_{0,0}\Delta t}[p_u V_{1,1} + p_m V_{1,0} + p_d V_{1,-1}]$

    The result should closely match the analytical Hull-White ZCB option formula.

## Pricing Coupon Bond Options

A coupon bond with cash flows $c_i$ at dates $T_1, \ldots, T_n$ is priced by backward induction, adding the coupon $c_i$ to the continuation value at each coupon date:

$$
V_{i,j} = e^{-r_{ij}\Delta t} \sum_{\ell} p_\ell\,V_{i+1, m_\ell} + c_i \cdot \mathbf{1}_{\{t_i \text{ is a coupon date}\}}
$$

An option on this coupon bond with strike $K$ and expiry $T$ is priced by:

1. First pricing the coupon bond on the tree (backward induction with coupon additions)
2. At the expiry nodes, computing the option payoff $\max(V_{\text{bond},T,j} - K, 0)$
3. Rolling back the option values from $T$ to $0$

This is the tree analogue of Jamshidian's trick, though the tree approach does not require decomposing the coupon bond into ZCB options.

## Pricing Caps and Floors

A caplet with reset date $T_{k-1}$ and payment date $T_k$ has payoff at $T_k$:

$$
\text{Caplet}_{T_k, j} = N\,\delta_k\,\max\!\left(\ell_k(r_{T_{k-1},j}) - K,\; 0\right)
$$

where $\ell_k(r) = \frac{1}{\delta_k}\left(\frac{1}{P(T_{k-1}, T_k; r)} - 1\right)$ is the forward rate determined at $T_{k-1}$, and $\delta_k = T_k - T_{k-1}$.

On the tree, the caplet payoff is computed at the reset date $T_{k-1}$, discounted by one period:

$$
\text{Caplet}_{T_{k-1}, j} = e^{-r_{T_{k-1},j}\,\delta_k} \cdot N\,\delta_k\,\max\!\left(\ell_k(r_{T_{k-1},j}) - K,\; 0\right)
$$

This is then rolled back from $T_{k-1}$ to time $0$.

A cap is the sum of caplets, and each caplet is priced independently on the tree and summed. Floors are handled analogously with $\max(K - \ell_k, 0)$.

## Pricing Swaps on the Tree

A payer swap with notional $N$, fixed rate $K$, and payment dates $T_1, \ldots, T_n$ has the value at time $t$:

$$
V_{\text{swap}}(t, r_t) = N\!\left[P(t, T_0) - P(t, T_n) - K \sum_{i=1}^{n} \delta_i\,P(t, T_i)\right]
$$

On the tree, this can be computed directly at any node using the affine bond price formula, or by backward induction treating each fixed leg payment as a negative coupon and the floating leg as the difference of two ZCBs.

## Pricing European Swaptions

A European payer swaption with expiry $T_0$ gives the right to enter a payer swap. At expiry, the payoff is

$$
V_{T_0, j} = \max\!\left(V_{\text{swap}}(T_0, r_{T_0,j}),\; 0\right)
$$

The swap value at each expiry node is computed from the affine bond price formula, and the swaption is rolled back from $T_0$ to $0$ using standard backward induction.

## Convergence

The tree price converges to the continuous-time analytical price as $\Delta t \to 0$ (equivalently, as $N \to \infty$). The convergence rate is typically $O(\Delta t)$ for European options, with possible oscillations due to the discrete grid not aligning perfectly with the exercise boundary.

!!! warning "Grid Alignment"
    For options with a specific strike or exercise boundary, convergence improves if the tree time steps align with the option's critical dates (expiry, coupon dates, reset dates). Misalignment can cause slower convergence and oscillatory behavior in the price as $N$ varies.

## Summary

Backward induction on the calibrated Hull-White trinomial tree prices derivatives by computing $V_{ij} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell V_{i+1,m_\ell}$ from the terminal payoff back to time $0$. European bond options use the affine formula at expiry nodes. Coupon bonds add cash flows at coupon dates. Caps and floors decompose into caplets priced independently. Swaptions use the swap value at expiry nodes. The tree approach is particularly valuable when analytical formulas are unavailable, and it naturally extends to American and Bermudan exercise, which is covered in the next section.

---

## Exercises

**Exercise 1.** Show that pricing a ZCB maturing at $t_N$ on the calibrated tree (with $V_{N,j} = 1$ for all $j$) recovers $V_{0,0} = P^M(0,t_N)$. Explain why this result is guaranteed by the calibration construction and what it would mean if the result failed.

??? success "Solution to Exercise 1"
    For a ZCB maturing at $t_N$, the terminal condition is $V_{N,j} = 1$ for all nodes $j$. Backward induction gives

    $$
    V_{N-1,j} = e^{-r_{N-1,j}\Delta t}\sum_\ell p_\ell \cdot 1 = e^{-r_{N-1,j}\Delta t}
    $$

    since $\sum_\ell p_\ell = 1$. Continuing backward, the value at $t_0$ is

    $$
    V_{0,0} = \sum_{\text{all paths}} \left(\prod_{i=0}^{N-1} e^{-r_{i,j_i}\Delta t}\right) \cdot \left(\prod_{i=0}^{N-1} p_{\ell_i}\right) = \sum_{j} Q_{N,j}
    $$

    This equals $P^{\text{tree}}(0, t_N)$ by definition of Arrow-Debreu prices.

    The result $V_{0,0} = P^M(0, t_N)$ is guaranteed by the calibration construction, which sets $\alpha_i$ at each time step to ensure $\sum_j Q_{i+1,j} = P^M(0, t_{i+1})$. Since $P^{\text{tree}}(0, t_N) = \sum_j Q_{N,j}$, the calibration directly ensures the ZCB price matches the market.

    If the result failed, it would indicate a bug in either the calibration step (incorrect $\alpha_i$ computation) or the backward induction (incorrect branching probabilities, discount factors, or node indexing). This test is a fundamental sanity check for any tree implementation.

---

**Exercise 2.** For a European call option on a ZCB, the payoff at expiry node $(T,j)$ uses $P(T,S;r_{T,j}) = \exp(A(T,S) + B(T,S)r_{T,j})$. Explain the advantage of using the analytic bond price formula at expiry nodes rather than computing bond prices by a separate backward induction from $S$ to $T$.

??? success "Solution to Exercise 2"
    Using the analytic bond price formula $P(T, S; r_{T,j}) = \exp(A(T,S) + B(T,S)\,r_{T,j})$ at expiry nodes has two key advantages:

    **Efficiency:** Computing the analytic formula requires only evaluating the deterministic functions $A(T,S)$ and $B(T,S)$ once, then plugging in the short rate $r_{T,j}$ at each node. This is $O(j_{\max})$ work. A separate backward induction from $S$ to $T$ would require building and rolling back through all time steps between $T$ and $S$, costing $O((S-T)/\Delta t \cdot j_{\max})$ per expiry node evaluation --- or $O((S-T)/\Delta t \cdot j_{\max})$ total if done once to get the bond price at all expiry nodes simultaneously.

    **Accuracy:** The analytic formula gives the exact Hull-White bond price at each node, with no discretization error. A backward induction from $S$ to $T$ introduces discretization error from the finite time step $\Delta t$. Since the bond option payoff depends on the bond price through a $\max$ function, errors in the bond price translate directly into errors in the option value.

    The only scenario where backward induction might be preferred is if the bond maturity $S$ does not correspond to a point where the analytic formula is easily evaluated, or if the model is not affine and no closed-form bond price exists.

---

**Exercise 3.** The convergence rate for European options on the tree is typically $O(\Delta t)$. Explain why this rate can degrade when the strike $K$ does not align with any node value $P(T,S;r_{T,j})$. How would you modify the tree to improve convergence in this case?

??? success "Solution to Exercise 3"
    The tree discretizes the short rate on a finite grid with spacing $\Delta x$. At expiry time step $T$, the bond prices at the nodes are $P(T, S; r_{T,j})$ for $j = -j_{\max}, \ldots, j_{\max}$. The call option payoff $\max(P(T,S;r_{T,j}) - K, 0)$ is zero for some nodes and positive for others. The exercise boundary lies at the node where the payoff transitions from zero to positive.

    If the strike $K$ falls exactly on a node value $P(T,S;r_{T,j^*})$ for some $j^*$, the exercise boundary is accurately captured. However, if $K$ lies between two adjacent node values, the true exercise boundary is between nodes $j^*$ and $j^*+1$, introducing discretization error in the payoff. This causes the convergence rate to degrade, potentially from $O(\Delta t)$ to $O(\sqrt{\Delta t})$.

    To improve convergence:

    - **Adjust the tree to align nodes with the strike:** Choose $\Delta x$ or shift the grid so that $P(T, S; \alpha_T + j^*\Delta x) = K$ for some integer $j^*$. This is sometimes called "strike-adjusted" tree construction.
    - **Interpolation at the exercise boundary:** Use linear or cubic interpolation between adjacent nodes to estimate the payoff more accurately near the boundary.
    - **Richardson extrapolation:** Compute the price with $N$ and $2N$ steps and extrapolate to remove the leading-order error.
    - **Smoothing the payoff:** Replace the $\max$ function with a smoothed approximation near the strike, though this introduces a small bias.

---

**Exercise 4.** For a coupon bond with cash flows $c_i$ at dates $T_1, \ldots, T_n$, the backward induction adds $c_i$ at each coupon date. Describe how to price the coupon bond on the tree, then compute the price of a European put option on this coupon bond with strike $K$ and expiry $T < T_1$.

??? success "Solution to Exercise 4"
    **Pricing the coupon bond on the tree:**

    At the final time step $t_N$ (at or after the last coupon date $T_n$), set $V_{N,j} = 1$ (the principal repayment, assuming it occurs at $T_n$).

    Roll backward through the tree. At each time step $t_i$:

    $$
    V_{ij} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell\,V_{i+1, m_\ell} + c_i \cdot \mathbf{1}_{\{t_i \text{ is a coupon date}\}}
    $$

    The coupon $c_i$ is added after discounting the continuation value. At the final coupon date $T_n$, the value includes the principal $1$ plus the final coupon $c_n$.

    **Pricing the European put option on the coupon bond:**

    First, run the backward induction above to obtain $V_{\text{bond}, T, j}$ at the option expiry nodes (the value of the coupon bond at each node at time $T$). Since $T < T_1$ (expiry is before the first coupon), the bond value at expiry equals the present value of all future coupons and principal.

    Then set the option payoff at each expiry node:

    $$
    V_{\text{put}, T, j} = \max(K - V_{\text{bond}, T, j},\; 0)
    $$

    Finally, roll the option values backward from $T$ to $t_0$ using standard backward induction (no coupons, just discounting):

    $$
    V_{\text{put}, i, j} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell\,V_{\text{put}, i+1, m_\ell}
    $$

    The put option price is $V_{\text{put}, 0, 0}$.

---

**Exercise 5.** A cap with annual resets at $T_0, T_1, \ldots, T_4$ and payment dates $T_1, \ldots, T_5$ is priced on the tree by pricing each caplet independently. Explain why the caplet payoff is computed at the reset date $T_{k-1}$ rather than the payment date $T_k$, and describe how the one-period discounting is applied.

??? success "Solution to Exercise 5"
    The caplet payoff depends on the forward rate $\ell_k(r_{T_{k-1}})$, which is determined (fixed) at the reset date $T_{k-1}$ based on the short rate at that time. The actual cash flow is paid at $T_k$, but the rate has already been locked in at $T_{k-1}$.

    The payoff is computed at the reset date $T_{k-1}$ because:

    1. The forward rate $\ell_k$ is an $\mathcal{F}_{T_{k-1}}$-measurable function of $r_{T_{k-1}}$, determined by the bond price ratio $P(T_{k-1}, T_k)$.
    2. The cash flow at $T_k$ is $N\delta_k\max(\ell_k - K, 0)$, which is known at $T_{k-1}$.
    3. To bring this cash flow back to $T_{k-1}$, we multiply by the one-period discount factor $P(T_{k-1}, T_k) = e^{-r_{T_{k-1}}\delta_k}$ (approximately, for one period).

    So at node $(T_{k-1}, j)$:

    $$
    \text{Caplet}_{T_{k-1}, j} = e^{-r_{T_{k-1},j}\,\delta_k} \cdot N\,\delta_k\,\max(\ell_k(r_{T_{k-1},j}) - K,\; 0)
    $$

    This discounted payoff is then rolled back from $T_{k-1}$ to time $0$ using standard backward induction. Computing the payoff at the reset date and discounting by one period is equivalent to computing the payoff at the payment date and discounting from $T_k$ to $T_{k-1}$, but it avoids the need to track the payoff between $T_{k-1}$ and $T_k$.

---

**Exercise 6.** For a European payer swaption with expiry $T_0$ on the tree, the swap value at each expiry node is computed using the affine bond price formula. Compare this tree-based approach with the analytic Jamshidian decomposition. Under what circumstances would the two methods give different results, and which is more reliable?

??? success "Solution to Exercise 6"
    **Tree-based approach:** Compute the swap value at each expiry node using $V_{\text{swap}}(T_0, r_{T_0,j}) = N[P(T_0,T_0) - P(T_0,T_n) - K_{\text{swap}}\sum_i \delta_i P(T_0,T_i)]$, where bond prices are from the affine formula. The swaption payoff $\max(V_{\text{swap}}, 0)$ is then rolled back. This is a single backward induction on the tree.

    **Jamshidian decomposition:** Decomposes the swaption into a portfolio of zero-coupon bond options, each with its own strike determined by the critical rate $r^*$ that makes the swap worthless. Each bond option is priced analytically using the Hull-White bond option formula, and the total swaption price is the sum.

    **When the methods differ:**

    - For European swaptions in the exact Hull-White model, both methods should give the same result (up to tree discretization error). The tree converges to the Jamshidian result as $\Delta t \to 0$.
    - For Bermudan swaptions, Jamshidian's decomposition does not apply (it is strictly a European result), so the tree approach is necessary.
    - For models where the bond price is not monotone in the short rate, Jamshidian's trick fails entirely, while the tree approach remains valid.

    The Jamshidian method is more reliable for European swaptions because it uses exact formulas, whereas the tree introduces discretization error. However, the tree is more general and extends naturally to Bermudan and American exercise.

---

**Exercise 7.** The backward induction formula $V_{ij} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell V_{i+1,m_\ell}$ uses the discount factor $e^{-r_{ij}\Delta t}$. For a tree with very large $\Delta t$ (e.g., annual steps), this approximation becomes inaccurate. Describe how to improve the discounting approximation and discuss the trade-off between tree step size and accuracy.

??? success "Solution to Exercise 7"
    The discount factor $e^{-r_{ij}\Delta t}$ approximates the exact one-period discount $\exp(-\int_{t_i}^{t_{i+1}} r_s\,ds)$ by assuming the short rate is constant at $r_{ij}$ over $[t_i, t_{i+1}]$. For large $\Delta t$, the short rate varies significantly within the interval, making this approximation poor.

    **Improvements:**

    1. **Trapezoidal discounting:** Use $\exp\!\left(-\frac{r_{ij} + r_{i+1,m}}{2}\Delta t\right)$ for the discount factor from node $(i,j)$ to node $(i+1,m)$, averaging the short rates at both ends. This is second-order accurate.

    2. **Using the affine bond price:** In the Hull-White model, the exact one-period discount factor from node $(i,j)$ to the next time step is available via $P(t_i, t_{i+1}; r_{ij}) = \exp(A(t_i, t_{i+1}) + B(t_i, t_{i+1})\,r_{ij})$. This is exact and should be used whenever possible.

    3. **Smaller time steps:** Reduce $\Delta t$ so that the piecewise-constant approximation is more accurate, at the cost of more nodes and computation.

    **Trade-off:** Using smaller $\Delta t$ improves discounting accuracy but increases computational cost as $O(1/\Delta t)$. The affine discount factor approach gives exactness without requiring smaller steps, but requires the analytic bond price formula, which is model-specific. For the Hull-White model where the affine formula is available, using $P(t_i, t_{i+1}; r_{ij})$ as the one-period discount factor is the recommended approach and eliminates the discounting error entirely regardless of step size.
