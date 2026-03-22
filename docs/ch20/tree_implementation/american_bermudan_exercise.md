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
