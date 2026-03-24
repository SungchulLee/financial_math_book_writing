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

---

**Exercise 2.** For a European call option on a ZCB, the payoff at expiry node $(T,j)$ uses $P(T,S;r_{T,j}) = \exp(A(T,S) + B(T,S)r_{T,j})$. Explain the advantage of using the analytic bond price formula at expiry nodes rather than computing bond prices by a separate backward induction from $S$ to $T$.

---

**Exercise 3.** The convergence rate for European options on the tree is typically $O(\Delta t)$. Explain why this rate can degrade when the strike $K$ does not align with any node value $P(T,S;r_{T,j})$. How would you modify the tree to improve convergence in this case?

---

**Exercise 4.** For a coupon bond with cash flows $c_i$ at dates $T_1, \ldots, T_n$, the backward induction adds $c_i$ at each coupon date. Describe how to price the coupon bond on the tree, then compute the price of a European put option on this coupon bond with strike $K$ and expiry $T < T_1$.

---

**Exercise 5.** A cap with annual resets at $T_0, T_1, \ldots, T_4$ and payment dates $T_1, \ldots, T_5$ is priced on the tree by pricing each caplet independently. Explain why the caplet payoff is computed at the reset date $T_{k-1}$ rather than the payment date $T_k$, and describe how the one-period discounting is applied.

---

**Exercise 6.** For a European payer swaption with expiry $T_0$ on the tree, the swap value at each expiry node is computed using the affine bond price formula. Compare this tree-based approach with the analytic Jamshidian decomposition. Under what circumstances would the two methods give different results, and which is more reliable?

---

**Exercise 7.** The backward induction formula $V_{ij} = e^{-r_{ij}\Delta t}\sum_\ell p_\ell V_{i+1,m_\ell}$ uses the discount factor $e^{-r_{ij}\Delta t}$. For a tree with very large $\Delta t$ (e.g., annual steps), this approximation becomes inaccurate. Describe how to improve the discounting approximation and discuss the trade-off between tree step size and accuracy.
