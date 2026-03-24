# OIS-LIBOR Spread Modeling

The overnight indexed swap (OIS) rate and LIBOR historically tracked closely but diverged significantly during financial crises, revealing credit risk and market structure effects. The multi-curve framework models these spreads to capture basis risk, funding costs, and counterparty credit risk in interest rate derivatives.

## Key Concepts

**OIS vs. LIBOR Rates**
- **OIS**: Daily overnight rate compounded, zero credit risk (central bank collateral)
- **LIBOR**: 3M/6M/12M unsecured borrowing rate, contains credit and term premium

OIS-LIBOR spread (basis) represents:

$$\text{LIBOR}(T) - \text{OIS}(T) = \text{Credit Premium} + \text{Liquidity Premium} + \text{Term Premium}$$

**Multi-Curve Framework**
Traditional approach: single curve for discounting and projection
Modern approach: separate curves for:
1. **Discount curve** (OIS): risk-free rate, used for all PV calculations
2. **Projection curves** (LIBOR): one curve per tenor (3M, 6M, 12M)
3. **Basis curves**: spread between LIBOR and OIS for each tenor

Forward LIBOR in multi-curve:

$$L_{t}(T, T+\Delta) = \text{OIS}_t(T, T+\Delta) + \text{Basis}_t(\Delta)$$

**Spread Modeling Dynamics**
Spread $X_t = L_t - \text{OIS}_t$ dynamics can follow:
1. **Mean-reverting**: $dX_t = \kappa(\bar{X} - X_t) dt + \sigma_X dB_t$
2. **Deterministic spreads** (earlier models): constant basis
3. **Stochastic spreads**: correlate with credit/liquidity conditions

**Funding Cost Modeling**
Banks have different funding rates depending on creditworthiness:

$$r_t^{\text{funding}}(T) = r_t^{\text{OIS}}(T) + \text{CDS}_t + \text{Liquidity Adjustment}$$

Swap pricing reflection:

$$\text{Par Swap Rate} = \text{OIS Forward} + \text{Funding Spread}$$

**CVA and Counterparty Risk**
Multi-curve framework enables:
- Credit valuation adjustment (CVA) using OIS as risk-free rate
- Proper valuation of collateralized transactions (discounted at OIS)
- Uncollateralized liabilities (discounted at own credit curve)

**Basis Risk in Hedging**
Hedging LIBOR exposure with OIS introduces basis risk:

$$P\&L_{\text{basis}} = N \times (\text{LIBOR} - \text{OIS}) \times dBasis \times \Delta t$$

Risk management requires:
- Separate basis risk limits
- Monitoring spread term structure
- Dynamic rehedging of basis exposure

!!! warning "Implementation Challenges"
    Multi-curve framework introduces complexity:
    - Computational cost of managing multiple curves
    - Calibration instability when spreads are tight
    - Backward compatibility with legacy systems
    - Correlation assumptions between rate and spread
    - Crisis scenarios where basis explodes (e.g., LIBOR freeze 2008)

---

## Exercises

**Exercise 1.** The OIS-LIBOR spread for 3-month USD LIBOR widened from approximately 10 bps to over 350 bps during the 2008 financial crisis. Explain the economic forces that drove this widening and why the spread did not fully revert to pre-crisis levels even after markets stabilized.

---

**Exercise 2.** In a multi-curve framework, a 5-year interest rate swap has quarterly floating payments at 3-month LIBOR and annual fixed payments. The OIS discount factors are given, and the 3-month LIBOR forward rates are projected from the LIBOR curve. Write down the present value of the floating leg

$$
V_{\text{float}} = \sum_{i=1}^{20} \delta_i\,L_i^{3M}(0)\,P^{\text{OIS}}(0, T_{i})
$$

and explain why $L_i^{3M}(0)$ must come from the LIBOR curve while $P^{\text{OIS}}(0, T_i)$ comes from the OIS curve.

---

**Exercise 3.** The OIS-LIBOR spread $X_t$ follows a mean-reverting process $dX_t = \kappa(\bar{X} - X_t)\,dt + \sigma_X\,dB_t$ with $\bar{X} = 15$ bps, $\kappa = 0.5$, $\sigma_X = 8$ bps, and current value $X_0 = 20$ bps. Compute the expected spread $\mathbb{E}[X_1]$ in 1 year and the standard deviation of $X_1$. What is the probability that the spread exceeds 40 bps?

---

**Exercise 4.** A bank has a portfolio of collateralized and uncollateralized swaps. The collateralized swaps are discounted at OIS, while the uncollateralized swaps must account for funding costs. Explain why a bank with a higher credit spread assigns a different value to the same uncollateralized swap compared to a bank with a lower credit spread. Is this a market inconsistency or a legitimate economic effect?

---

**Exercise 5.** Consider a tenor basis swap that exchanges 3-month LIBOR for 6-month LIBOR. In a single-curve world, the basis spread should be zero. Explain why a non-zero basis spread exists in practice and describe how a multi-curve model captures this. If the 3M/6M basis is currently 5 bps, estimate the annual cash flow on a \$1 billion notional basis swap.

---

**Exercise 6.** In the transition from LIBOR to SOFR (Secured Overnight Financing Rate), the credit component of LIBOR disappears. Discuss how this transition affects the multi-curve framework. Will a multi-curve approach still be necessary in a post-LIBOR world, and if so, what curves will replace the LIBOR projection curves?
