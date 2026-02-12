# LMM Drift in Terminal Measure

The LIBOR Market Model (LMM) is the standard framework for pricing interest rate derivatives across multiple tenors simultaneously. A crucial technical aspect is the drift correction required when changing the numeraire to a specific maturity, enabling efficient calibration and pricing under different term structures.

## Key Concepts

**LIBOR Dynamics in Spot Measure**
Define forward LIBOR $L_k(t)$ for tenor $[T_k, T_{k+1}]$ with accrual $\delta_k$:
$$dL_k(t) = \mu_k^{\text{spot}}(t) dt + \sigma_k(t) dB_k(t)$$

The spot measure uses the rolling bank account as numeraire:
$$N_t^{\text{spot}} = \prod_{j: T_j \leq t} (1 + \delta_j L_j(T_j))$$

**Terminal Measure Change**
The terminal measure uses the zero-coupon bond maturing at time $T_N$ as numeraire:
$$N_t^{N} = P(t, T_N)$$

Under terminal measure:
$$dL_k(t) = \mu_k^N(t) dt + \sigma_k(t) dB_k^N(t)$$

The Brownian motion has changed to $B_k^N$ reflecting the new measure.

**Drift Correction Formula**
The drift correction relates spot and terminal measure drifts:
$$\mu_k^N(t) = \mu_k^{\text{spot}}(t) + \sigma_k(t) \sum_{j=k+1}^{N} \frac{\delta_j \sigma_j(t) \rho_{k,j}}{1 + \delta_j L_j(t)}$$

Key features:
- Correction term is positive (martingale property enforced)
- Depends on instantaneous correlation $\rho_{k,j}$ between rate curves
- Involves future rates for indices $j > k$ in terminal measure

**Intuition**
The drift correction arises because:
1. Zero-coupon bond price depends on all future rates
2. When changing numeraire to $P(t, T_N)$, relative pricing changes
3. Girsanov theorem ensures the SDE coefficient structure remains proportional to $\sigma_k$
4. Only drift changes, volatility structure preserved

**Practical Implementation**
LMM calibration proceeds in terminal measure:
1. Specify volatility structure $\sigma_k(t)$ (typically piecewise constant or deterministic)
2. Specify correlation matrix $\rho_{i,j}$ for all rate pairs
3. Drift is automatically computed from formula
4. Simulate forward rates under terminal measure
5. Compute prices by averaging discounted payoffs

**Efficient Calibration**
Terminal measure enables efficient calibration:
- Caplets/floorlets prices depend on individual rate volatilities $\sigma_k$
- Swaptions prices depend on rate correlation structure
- Two-stage calibration: fit volatilities to caps, correlations to swaptions
- Avoids explicit specification of spot measure drifts

**Connection to Swap Measure**
Alternative: swap measure uses annuity as numeraire
$$N_t^{\text{swap}} = A_t = \sum_{j=k}^{N} \delta_j P(t, T_j)$$

Swap measure drift is different from terminal measure, optimized for swaption pricing.

!!! note "Practical Insights"
    Terminal measure provides:
    - Computational efficiency through direct calibration
    - Intuitive interpretation: numeraire is final cash received
    - Stability in long-dated simulations
    - Effective handling of multiple correlated rates simultaneously
