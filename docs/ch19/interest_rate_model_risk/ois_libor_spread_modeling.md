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
