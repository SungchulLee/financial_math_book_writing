# Convertible Bond Arbitrage — Overview

**Convertible bond arbitrage** is a strategy where you profit from mispriced embedded optionality by buying convertible bonds and hedging away the directional risk through short stock positions.

> **Prerequisites:** This section requires understanding of option pricing (Chapter 5: Black-Scholes), delta hedging and gamma mechanics (Chapter 6), and credit risk fundamentals. For the Merton model connection between equity volatility and credit spreads, see the equity-credit basis discussion in Section 23.4.2.

---

## Document Structure

This topic has been split into three documents for easier navigation:

| Document | Content | Lines |
|----------|---------|-------|
| **[Part 1: Mechanics](convertible_bond_mechanics.md)** | Instrument structure, valuation decomposition, embedded option analysis, economic interpretation, key Greeks | ~1,100 |
| **[Part 2: Implementation](convertible_bond_arbitrage_implementation.md)** | P&L formula, profit sources, hedging mechanics, position management, evolution pre/post-2008 | ~1,800 |
| **[Part 3: Risk & Performance](convertible_bond_arbitrage_risk.md)** | Best/worst case scenarios, practical guidance, common mistakes, real-world examples, Q&A on option extraction | ~2,500 |

---

## Quick Reference

### The Core Equation

$$
\text{Convertible Bond} = \text{Straight Bond} + \text{Embedded Call Option}
$$

### P&L Formula

$$
\delta \Pi \approx \underbrace{\text{Coupon Income}}_{\text{steady cash flow}} + \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{gamma scalping}} + \underbrace{\text{Credit P\&L}}_{\text{spread tightening}} + \underbrace{\text{Vega} \cdot \delta\sigma}_{\text{vol changes}} - \underbrace{\text{Costs}}_{\text{borrow, IR}}
$$

### Five Profit Sources

1. **Gamma scalping** — Delta hedge rebalancing captures realized volatility
2. **Coupon carry** — Bond coupons exceed financing costs (ideally)
3. **Credit spread tightening** — Bond floor appreciates with improving credit
4. **Vega expansion** — Long embedded volatility benefits from vol increases
5. **Forced conversion premium** — Issuer calls trigger favorable exit

### Key Risk Factors

| Risk | Description | Mitigation |
|------|-------------|------------|
| Credit deterioration | Bond floor collapse | Credit analysis, diversification |
| Borrow cost spike | Short squeeze dynamics | Borrow monitoring, position limits |
| Liquidity crisis | Wide bid-ask, forced liquidation | Size limits, cash buffer |
| Leverage amplification | 2008-style meltdown | Conservative leverage (3-4×) |

---

## Figures

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_delta.png?raw=true" alt="Convertible Bond Delta" width="700">
</p>

**Figure 1:** Convertible Bond Arbitrage Delta visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_payoff.png?raw=true" alt="Convertible Bond Payoff" width="700">
</p>

**Figure 2:** Convertible Bond Arbitrage Payoff visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_pnl.png?raw=true" alt="Convertible Bond P&L" width="700">
</p>

**Figure 3:** Convertible Bond Arbitrage P&L visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_structure.png?raw=true" alt="Convertible Bond Structure" width="700">
</p>

**Figure 4:** Convertible Bond Arbitrage Structure visualization.

---

*Continue to [Part 1: Mechanics](convertible_bond_mechanics.md) →*
