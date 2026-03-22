# Path-Dependent Derivative Pricing

Many interest rate derivatives encountered in practice have payoffs that depend on the entire history of the short rate, not just its terminal value. Callable bonds can be redeemed early by the issuer, range accruals pay coupons only when rates stay within a corridor, and collateralized mortgage obligations (CMOs) have cash flows driven by prepayment behavior linked to the rate path. The Hull-White model's Gaussian structure and exact simulation scheme make Monte Carlo methods the natural tool for pricing these instruments.

## General Monte Carlo Pricing Framework

Under the risk-neutral measure $\mathbb{Q}$, the price at time $0$ of a derivative with path-dependent cash flows $\{c_{t_1}, c_{t_2}, \ldots, c_{t_n}\}$ is

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[\sum_{i=1}^{n} \frac{c_{t_i}}{M(t_i)}\right]
$$

where $M(t) = \exp\!\left(\int_0^t r_s\,ds\right)$ is the money market account. The Monte Carlo estimator on $N_{\text{paths}}$ simulated paths is

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
