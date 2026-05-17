# Path-Dependent Derivative Pricing

Many interest rate derivatives encountered in practice have payoffs that depend on the entire history of the short rate, not just its terminal value. Callable bonds can be redeemed early by the issuer, range accruals pay coupons only when rates stay within a corridor, and collateralized mortgage obligations (CMOs) have cash flows driven by prepayment behavior linked to the rate path. The Hull-White model's Gaussian structure and exact simulation scheme make Monte Carlo methods the natural tool for pricing these instruments.

## General Monte Carlo Pricing Framework

Recall (see [§ Risk-Neutral Pricing](../../ch04/risk_neutral/martingale_and_no_arbitrage.md)) the price of a derivative with path-dependent cash flows $\{c_{t_1}, c_{t_2}, \ldots, c_{t_n}\}$ is

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[\sum_{i=1}^{n} \frac{c_{t_i}}{M(t_i)}\right]
$$

with $M(t) = \exp\!\left(\int_0^t r_s\,ds\right)$. The Monte Carlo estimator on $N_{\text{paths}}$ simulated paths is

$$
\hat{V}_0 = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \sum_{i=1}^{n} \frac{c_{t_i}^{(k)}}{M^{(k)}(t_i)}
$$

where $c_{t_i}^{(k)}$ is the cash flow at time $t_i$ on path $k$, computed from the simulated short rate trajectory $\{r_{t_0}^{(k)}, r_{t_1}^{(k)}, \ldots\}$.

!!! tip "Exact Simulation Advantage"
    Because Hull-White admits exact Gaussian transitions, the simulated path $\{r_{t_i}\}$ is free of discretization bias. The only source of error is the finite number of paths (statistical error), which decreases as $O(1/\sqrt{N_{\text{paths}}})$.

## Callable Bond Pricing

A callable bond pays coupons $c_i$ at dates $T_1, \ldots, T_n$ and principal $1$ at maturity $T_n$, but the issuer may redeem it at par (or at a call price $K_{\text{call}}$) on any call date $T_{j_1}, T_{j_2}, \ldots \subseteq \{T_1, \ldots, T_n\}$. The issuer exercises when the continuation value exceeds the call price from the issuer's perspective, equivalently when the bond value exceeds $K_{\text{call}}$.

The callable bond price is

$$
V_{\text{callable}} = V_{\text{straight}} - V_{\text{call option}}
$$

where $V_{\text{straight}}$ is the price of the non-callable bond and $V_{\text{call option}}$ is the value of the issuer's embedded call option.

Since the call decision depends on the path (specifically on the short rate at each call date), backward induction within Monte Carlo requires regression-based methods. The **Longstaff-Schwartz** algorithm proceeds as follows:

1. Simulate $N_{\text{paths}}$ short rate paths $\{r_{t_i}^{(k)}\}$
2. At the final call date, compute the exercise value $E^{(k)} = K_{\text{call}}$ and continuation value $C^{(k)}$ (present value of remaining cash flows)
3. At each earlier call date $T_j$, regress discounted continuation values on basis functions of $r_{T_j}$:

$$
\hat{C}(r_{T_j}) = \sum_{m=0}^{M} \beta_m\,\phi_m(r_{T_j})
$$

where $\phi_m$ are polynomial or other basis functions. The issuer calls if $\hat{C}(r_{T_j}) > K_{\text{call}}$ (bond value exceeds call price).

## Range Accrual Notes

A range accrual note pays a coupon proportional to the fraction of days the reference rate stays within a specified corridor $[L, U]$. For a coupon period $[T_{i-1}, T_i]$ with daily monitoring dates $\{s_1, \ldots, s_D\}$, the coupon is

$$
c_i = N \cdot R_{\text{fixed}} \cdot \delta_i \cdot \frac{1}{D} \sum_{d=1}^{D} \mathbf{1}_{\{L \leq \ell(s_d) \leq U\}}
$$

where $N$ is the notional, $R_{\text{fixed}}$ is the stated coupon rate, $\delta_i = T_i - T_{i-1}$, and $\ell(s_d)$ is the reference rate (e.g., the LIBOR fixing or an overnight rate) at monitoring date $s_d$.

Under Hull-White, the short rate $r_{s_d}$ is simulated at each monitoring date, and the reference rate is computed from the simulated bond prices:

$$
\ell(s_d) = \frac{1}{\delta}\left(\frac{1}{P(s_d, s_d + \delta)} - 1\right)
$$

where $\delta$ is the reference rate tenor. The Monte Carlo price is

$$
\hat{V}_{\text{RA}} = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \sum_{i=1}^{n} \frac{c_i^{(k)}}{M^{(k)}(T_i)}
$$

## Target Redemption Notes (TARNs)

A TARN is a structured note where the cumulative coupon is capped at a target level $H$. Once the accumulated coupons reach $H$, the note redeems at par. The coupon at period $i$ is

$$
c_i = \min\!\left(N \cdot \max(\ell(T_{i-1}) - K, 0) \cdot \delta_i,\; H - \sum_{j=1}^{i-1} c_j\right)
$$

The path dependence arises from the cumulative sum: the coupon at period $i$ depends on all previous coupons, which in turn depend on the entire rate path up to $T_{i-1}$. The note terminates when $\sum_{j=1}^{i} c_j = H$.

## Auto-Callable Notes

An auto-callable note redeems early if the short rate (or a reference rate) falls below a trigger level $r^*$ at any observation date. The pricing requires monitoring $r_{T_j}$ at each observation date:

$$
V_{\text{auto}} = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \frac{c_{\tau^{(k)}}^{(k)}}{M^{(k)}(\tau^{(k)})}
$$

where $\tau^{(k)} = \min\{T_j : r_{T_j}^{(k)} \leq r^*\}$ is the first trigger date on path $k$, and $c_{\tau}$ includes accrued interest plus the redemption amount.

## Collateralized Mortgage Obligations

CMO tranches receive cash flows from a pool of mortgages, where prepayment rates depend on the interest rate environment. A common prepayment model specifies the conditional prepayment rate (CPR) as a function of the short rate:

$$
\text{CPR}(t) = \text{CPR}_{\min} + (\text{CPR}_{\max} - \text{CPR}_{\min}) \cdot \Phi\!\left(\frac{r^* - r_t}{\sigma_{\text{CPR}}}\right)
$$

where $\Phi$ is the standard normal CDF, $r^*$ is a refinancing threshold, and $\sigma_{\text{CPR}}$ controls the sharpness of the prepayment response. When rates fall below $r^*$, homeowners refinance, increasing prepayments.

The single monthly mortality (SMM) and scheduled principal determine the cash flow to each tranche along each simulated path, making Monte Carlo the only feasible pricing approach.

## Implementation Considerations

!!! warning "Time Grid Resolution"
    Path-dependent derivatives with daily monitoring (e.g., range accruals) require a fine time grid. With exact simulation, this adds computational cost for evaluating $A(t_i, T)$ and $B(t_i, T)$ at many time steps, but introduces no discretization bias. Precomputing these functions for the full grid is essential for efficiency.

The key implementation steps for pricing any path-dependent derivative under Hull-White are:

1. **Define the time grid**: include all coupon dates, monitoring dates, call dates, and observation dates
2. **Simulate short rate paths**: use exact Gaussian transitions at each grid point
3. **Compute path-wise quantities**: bond prices $P(t_i, T_j)$, reference rates, money market account values
4. **Evaluate path-wise cash flows**: apply the instrument-specific payoff rules
5. **Discount and average**: compute the Monte Carlo estimator as the sample mean of discounted cash flows

???+ example "Callable Bond Pricing Algorithm"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)
        t, R, M = hw.generate_sample_paths(
            num_paths=10_000, num_steps=120, T=10, seed=42
        )

        # Coupon dates every 0.5 years, callable after year 3
        coupon_dates = np.arange(0.5, 10.5, 0.5)
        call_dates = np.arange(3.0, 10.5, 0.5)
        coupon_rate = 0.05
        K_call = 1.0

        # Backward induction with Longstaff-Schwartz
        # At each call date, regress continuation on r_t
        # Exercise if bond value > K_call
    ```

## Summary

Path-dependent derivatives under the Hull-White model are priced via Monte Carlo simulation, leveraging the model's exact Gaussian transitions to eliminate discretization bias. Callable bonds require regression-based backward induction (Longstaff-Schwartz), range accruals need fine-grid monitoring of the reference rate, TARNs involve cumulative coupon tracking, and CMO tranches depend on rate-driven prepayment models. In all cases, the affine bond price formula allows efficient computation of reference rates and discount factors at each simulated time step. The primary source of error is statistical, decreasing as $O(1/\sqrt{N_{\text{paths}}})$, and can be reduced further using the variance reduction techniques discussed in the next section.

---

## Exercises

**Exercise 1.** For a range accrual note with corridor $[L, U] = [0.02, 0.05]$, daily monitoring over a 1-year period, and notional $N = \$1{,}000{,}000$, describe the Monte Carlo pricing procedure step by step. How many time steps are needed in the simulation, and what determines the time grid?

??? success "Solution to Exercise 1"
    **Step-by-step Monte Carlo pricing for the range accrual note:**

    1. **Define the time grid:** Daily monitoring over 1 year requires approximately $D = 252$ business days (or 365 calendar days). The time grid includes all monitoring dates: $s_1, s_2, \ldots, s_D$ with $\Delta t \approx 1/252$ (or $1/365$).

    2. **Simulate short rate paths:** For each of $N_{\text{paths}}$ paths, generate the short rate trajectory $\{r_{s_1}^{(k)}, r_{s_2}^{(k)}, \ldots, r_{s_D}^{(k)}\}$ using exact Gaussian transitions with step size $\Delta t$.

    3. **Compute reference rates:** At each monitoring date $s_d$, compute the reference rate from the bond price:

        $$
        \ell(s_d) = \frac{1}{\delta}\left(\frac{1}{P(s_d, s_d + \delta)} - 1\right) = \frac{1}{\delta}\left(\exp(-A(s_d, s_d+\delta) - B(s_d, s_d+\delta)\,r_{s_d}) - 1\right)
        $$

        where $\delta$ is the reference rate tenor (e.g., 3 months).

    4. **Evaluate the accrual indicator:** For each path $k$ and each monitoring date $s_d$, check if $L \leq \ell^{(k)}(s_d) \leq U$, i.e., $0.02 \leq \ell^{(k)}(s_d) \leq 0.05$.

    5. **Compute the coupon:** For the single coupon period $[0, 1]$:

        $$
        c^{(k)} = N \cdot R_{\text{fixed}} \cdot 1 \cdot \frac{1}{D}\sum_{d=1}^{D} \mathbf{1}_{\{0.02 \leq \ell^{(k)}(s_d) \leq 0.05\}}
        $$

    6. **Discount and average:**

        $$
        \hat{V}_{\text{RA}} = \frac{1}{N_{\text{paths}}}\sum_{k=1}^{N_{\text{paths}}} \frac{c^{(k)}}{M^{(k)}(1)}
        $$

    The time grid requires approximately 252--365 steps per year, determined by the daily monitoring frequency. The functions $A(s_d, s_d + \delta)$ and $B(s_d, s_d + \delta)$ should be precomputed for all monitoring dates.

---

**Exercise 2.** In the Longstaff-Schwartz algorithm for callable bonds, the regression $\hat{C}(r_{T_j}) = \sum_{m=0}^M \beta_m \phi_m(r_{T_j})$ estimates the continuation value. Explain why the issuer calls when $\hat{C}(r_{T_j}) > K_{\text{call}}$ (not $<$). What is the difference between the issuer's call decision and the holder's exercise decision for a Bermudan swaption?

??? success "Solution to Exercise 2"
    In the Longstaff-Schwartz algorithm for callable bonds, the issuer (not the bondholder) holds the embedded option. The issuer's objective is to minimize the cost of the bond, which means calling it when the bond's market value exceeds the call price $K_{\text{call}}$.

    The continuation value $\hat{C}(r_{T_j})$ estimates what the bond is worth if not called. The issuer calls when $\hat{C}(r_{T_j}) > K_{\text{call}}$, because:

    - If the bond value exceeds $K_{\text{call}}$, the issuer benefits by redeeming the bond at $K_{\text{call}}$ (a lower cost) and refinancing at the now-lower market rate.
    - If the bond value is below $K_{\text{call}}$, calling would be disadvantageous to the issuer (paying $K_{\text{call}}$ for a bond worth less).

    **Comparison with Bermudan swaption:** For a Bermudan swaption, the holder benefits from exercise when the exercise value exceeds the continuation value, so the holder exercises when $E_{ij} > C_{ij}$, i.e., $V_{ij} = \max(C_{ij}, E_{ij})$.

    For the callable bond, the issuer's call caps the bondholder's value: $V_{ij} = \min(C_{ij}, K_{\text{call}})$ at call dates. The key difference is max vs. min:

    - Bermudan swaption: holder maximizes (exercises to gain)
    - Callable bond: issuer minimizes the bondholder's value (calls to save)

---

**Exercise 3.** A TARN has a cumulative coupon cap $H$. Explain why Monte Carlo is the natural pricing method for TARNs, and why tree-based backward induction is difficult. What additional state variable would the tree need to track?

??? success "Solution to Exercise 3"
    A TARN's cumulative coupon cap $H$ introduces a path-dependent state: the cumulative sum $S_i = \sum_{j=1}^{i} c_j$. The coupon at period $i$ depends on $S_{i-1}$ (all previous coupons):

    $$
    c_i = \min\!\left(N \cdot \max(\ell(T_{i-1}) - K, 0) \cdot \delta_i,\; H - S_{i-1}\right)
    $$

    **Why Monte Carlo is natural:** Monte Carlo simulates each path forward in time, naturally tracking the cumulative coupon $S_i$ along each path. The TARN termination condition ($S_i = H$) is checked at each period on each path independently. This is straightforward to implement.

    **Why tree-based backward induction is difficult:** Backward induction computes option values at each node $(i, j)$ from future values. However, the TARN value at node $(i, j)$ depends not only on the short rate $r_{ij}$ but also on the cumulative coupon $S_i$ along the path that reached this node. Different paths arriving at the same node $(i, j)$ may have different values of $S_i$.

    **Additional state variable:** The tree would need to track $S_i$ as an additional state variable, expanding each node $(i, j)$ into multiple sub-nodes $(i, j, s)$ for each possible cumulative coupon level $s$. Since $S_i$ can take a continuum of values, it must be discretized, and the tree size becomes $O(N \cdot j_{\max} \cdot N_S)$ where $N_S$ is the number of discretized coupon levels. This dramatically increases computational cost and is impractical for fine discretizations of $S$.

---

**Exercise 4.** The CMO prepayment model uses $\text{CPR}(t) = \text{CPR}_{\min} + (\text{CPR}_{\max} - \text{CPR}_{\min})\Phi\left(\frac{r^* - r_t}{\sigma_{\text{CPR}}}\right)$. Explain the economic intuition: why does prepayment increase when $r_t < r^*$? What do the parameters $r^*$ and $\sigma_{\text{CPR}}$ control?

??? success "Solution to Exercise 4"
    The CMO prepayment model $\text{CPR}(t) = \text{CPR}_{\min} + (\text{CPR}_{\max} - \text{CPR}_{\min})\Phi\!\left(\frac{r^* - r_t}{\sigma_{\text{CPR}}}\right)$ captures the economic relationship between interest rates and mortgage prepayments.

    **Why prepayment increases when $r_t < r^*$:** When market rates $r_t$ fall below the refinancing threshold $r^*$, homeowners have an incentive to refinance their existing mortgages at lower rates. This triggers prepayment of the original mortgage. The lower the rates relative to $r^*$, the stronger the incentive, so $\Phi\!\left(\frac{r^* - r_t}{\sigma_{\text{CPR}}}\right) \to 1$ as $r_t \to -\infty$.

    **Parameter $r^*$:** This is the refinancing threshold --- the rate level below which prepayment activity accelerates significantly. It is typically set near the average coupon rate of the mortgage pool. When $r_t = r^*$, the CPR is at the midpoint $\frac{\text{CPR}_{\min} + \text{CPR}_{\max}}{2}$.

    **Parameter $\sigma_{\text{CPR}}$:** This controls the sharpness of the prepayment response:

    - Small $\sigma_{\text{CPR}}$: the $\Phi$ function transitions sharply from 0 to 1 around $r^*$, modeling a population of borrowers who all refinance at nearly the same rate threshold.
    - Large $\sigma_{\text{CPR}}$: the transition is gradual, reflecting heterogeneity among borrowers (different coupon rates, credit scores, refinancing costs).

---

**Exercise 5.** The auto-callable note redeems when $r_{T_j} \leq r^*$ at any observation date. Describe how to compute the Monte Carlo price, paying careful attention to the stopping time $\tau^{(k)}$ on each path. What happens on paths where the trigger is never hit?

??? success "Solution to Exercise 5"
    **Monte Carlo pricing procedure for auto-callable notes:**

    1. Simulate $N_{\text{paths}}$ short rate paths $\{r_{t_0}^{(k)}, r_{t_1}^{(k)}, \ldots\}$.
    2. For each path $k$, determine the stopping time:

        $$
        \tau^{(k)} = \min\{T_j : r_{T_j}^{(k)} \leq r^*\}
        $$

        scanning observation dates $T_1, T_2, \ldots$ in order until the trigger condition $r_{T_j}^{(k)} \leq r^*$ is met.

    3. If the trigger is hit at $\tau^{(k)} = T_j$, the cash flow is $c_{\tau^{(k)}}$, which includes the redemption amount (typically par = 1) plus any accrued interest or enhanced coupon.

    4. Compute the discounted payoff:

        $$
        \hat{V}^{(k)} = \frac{c_{\tau^{(k)}}}{M^{(k)}(\tau^{(k)})}
        $$

    5. **Paths where the trigger is never hit:** If $r_{T_j}^{(k)} > r^*$ for all observation dates $j = 1, \ldots, J$, the note survives to maturity and pays the final redemption cash flow $c_{\text{final}}$ at the last date $T_J$:

        $$
        \hat{V}^{(k)} = \frac{c_{\text{final}}}{M^{(k)}(T_J)}
        $$

    6. The Monte Carlo price is

        $$
        \hat{V}_{\text{auto}} = \frac{1}{N_{\text{paths}}}\sum_{k=1}^{N_{\text{paths}}} \hat{V}^{(k)}
        $$

    The key implementation detail is correctly handling the early termination on each path and ensuring that intermediate coupons (if any are paid before the trigger) are also included in the discounted cash flow sum.

---

**Exercise 6.** For path-dependent derivatives with daily monitoring, the time grid must include all monitoring dates. With exact simulation, adding more time steps does not introduce discretization bias but increases computational cost. Describe strategies to reduce this cost, such as precomputing $A(t_i, T)$ and $B(t_i, T)$ for the full grid.

??? success "Solution to Exercise 6"
    **Strategies to reduce computational cost with fine time grids:**

    1. **Precompute $A(t_i, T)$ and $B(t_i, T)$:** These functions depend only on model parameters and the initial curve. Compute them once for all $(t_i, T)$ pairs needed and store in arrays. This avoids repeated evaluation of exponentials and logarithms during path simulation. Memory cost is $O(N \times M_T)$ doubles, which is typically small (a few MB at most).

    2. **Vectorized computation:** Use NumPy array operations to compute bond prices for all paths simultaneously at each time step, avoiding Python loops over paths. The operation $P(t_i, T_j) = \exp(A_{i,j} + B_{i,j} \cdot r_{t_i})$ is a simple element-wise computation on arrays.

    3. **Coarse-fine grid strategy:** Use a coarse grid for the short rate simulation (where exact simulation eliminates bias) and a fine grid only for monitoring. Since the exact transition is known, one can simulate $r$ at monitoring dates directly without needing intermediate steps.

    4. **Brownian bridge:** For range accruals, simulate the short rate at coupon dates (coarse grid), then use Brownian bridge interpolation to estimate the fraction of time the rate spends in the corridor, rather than simulating at every monitoring date.

    5. **Analytical approximations:** For some path-dependent features, approximate the daily monitoring with continuous monitoring using an analytical correction factor, reducing the number of required time steps.

---

**Exercise 7.** Compare tree-based and Monte Carlo approaches for pricing a callable bond in the one-factor Hull-White model. What are the advantages of each method? For a two-factor Hull-White model, why does the tree approach become impractical?

??? success "Solution to Exercise 7"
    **Tree-based approach for callable bonds (one-factor Hull-White):**

    - *Advantages:* Backward induction naturally handles the issuer's optimal call decision at each node without regression. The call decision is deterministic given the node's short rate and continuation value. Exact, no Monte Carlo noise. Converges systematically as $\Delta t \to 0$.
    - *Disadvantages:* Limited to one or two factors. Path-dependent features (e.g., cumulative coupons) are difficult to handle without expanding the state space.

    **Monte Carlo approach for callable bonds:**

    - *Advantages:* Handles path-dependent features naturally (TARNs, range accruals combined with callability). Extends to multi-factor models without modification. Exact simulation eliminates discretization bias.
    - *Disadvantages:* The Longstaff-Schwartz regression introduces approximation error in the call decision. Monte Carlo estimates have statistical noise. Convergence is slower ($O(1/\sqrt{N_{\text{paths}}})$) than tree methods.

    **Why trees become impractical for two-factor models:** In the two-factor Hull-White model, the state is $(x_t, y_t) \in \mathbb{R}^2$. A tree must discretize both dimensions, creating a 2D grid. If each dimension has $O(j_{\max})$ nodes, the total nodes per time step are $O(j_{\max}^2)$. For typical values ($j_{\max} \approx 10$--$50$), this gives $100$--$2500$ nodes per step, still feasible but much more expensive.

    The real difficulty is the cross-term: the correlation between $x_t$ and $y_t$ requires careful construction of branching probabilities on the 2D grid (e.g., 9-point stencils) to match the cross-covariance. As the number of factors increases to 3 or more, the grid becomes $O(j_{\max}^d)$ where $d$ is the dimension, suffering from the curse of dimensionality. For $d = 3$ with $j_{\max} = 20$, there are $8000$ nodes per step, and the branching structure becomes complex. Monte Carlo, whose cost is independent of dimension, becomes the clearly superior method.
