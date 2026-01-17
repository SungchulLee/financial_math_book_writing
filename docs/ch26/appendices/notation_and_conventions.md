# Chapter 26: Notation and Conventions


This document establishes the standard notation used throughout Chapter 26: Digital Assets. All formulas across the eight main documents adhere to these conventions.

---

## Price and Position Variables


| Symbol | Meaning | Units | Example |
|--------|---------|-------|---------|
| $P$ | Price | USD | $P = 43{,}000$ |
| $P_{\text{spot}}$ | Spot price | USD | Spot BTC price |
| $P_{\text{perp}}$ | Perpetual price | USD | Perpetual mark price |
| $P_{\text{entry}}$ | Entry price | USD | Trade entry |
| $P_{\text{liq}}$ | Liquidation price | USD | Forced closure price |
| $P_{\text{mark}}$ | Mark price | USD | Fair value (anti-manipulation) |
| $Q$ | Quantity/Position size | Base currency (BTC, ETH) | $Q = 10$ BTC |
| $V$ | Volume | Base currency or USD | Daily volume |
| $N$ | Notional value | USD | $N = Q \times P$ |

---

## Funding Rate Notation


**Standard convention:**

| Symbol | Meaning | Typical Range |
|--------|---------|---------------|
| $r_{8h}$ | 8-hour funding rate | 0.01% - 0.10% |
| $r_{\text{daily}}$ | Daily funding rate | $r_{8h} \times 3$ |
| $r_{\text{annual}}$ | Annualized funding | $r_{8h} \times 1095$ |

**Annualization formula (standard form):**

$$
r_{\text{annual}} = r_{8h} \times 3 \times 365 = r_{8h} \times 1095
$$

**Note:** Both expressions ($3 \times 365$ and $1095$) are equivalent and may appear interchangeably.

**Funding payment:**

$$
\text{Payment} = N \times r_{8h}
$$

Where $N$ = notional position size in USD.

---

## Leverage and Margin


| Symbol | Meaning | Formula |
|--------|---------|---------|
| $L$ | Leverage multiple | e.g., $L = 10$ for 10× |
| $M_{\text{init}}$ | Initial margin | $M_{\text{init}} = N / L$ |
| $M_{\text{maint}}$ | Maintenance margin rate | Typically 0.4% - 1% |
| $\text{MM}$ | Maintenance margin rate | Alternative notation |

**Liquidation price (long position):**

$$
P_{\text{liq}} = P_{\text{entry}} \times \left(1 - \frac{1}{L} + \frac{M_{\text{maint}} + f}{L}\right)
$$

Where $f$ = fee rate (typically 0.05% - 0.10%).

**Liquidation price (short position):**

$$
P_{\text{liq}} = P_{\text{entry}} \times \left(1 + \frac{1}{L} - \frac{M_{\text{maint}} + f}{L}\right)
$$

---

## Volatility Notation


| Symbol | Meaning | Annualization |
|--------|---------|---------------|
| $\sigma$ | Volatility (generic) | Context-dependent |
| $\sigma_{\text{daily}}$ | Daily volatility | Direct measure |
| $\sigma_{\text{annual}}$ | Annualized volatility | $\sigma_{\text{daily}} \times \sqrt{365}$ |
| $\sigma_{\text{realized}}$ | Realized (historical) volatility | From past returns |
| $\sigma_{\text{implied}}$ | Implied volatility | From options prices |

**Realized volatility calculation:**

$$
\sigma_{\text{realized}} = \sqrt{\frac{365}{N} \sum_{i=1}^{N} r_i^2}
$$

Where $r_i = \ln(P_i / P_{i-1})$ are log returns.

**Note:** Crypto uses 365 trading days (24/7 markets), not 252 as in traditional finance.

---

## Market Impact Notation


| Symbol | Meaning | Typical Value |
|--------|---------|---------------|
| $\sigma$ | Daily volatility | 3% (BTC typical) |
| $Q$ | Order quantity | Base currency |
| $V$ | Daily volume | Base currency |

**Square root law:**

$$
\text{Impact} = \sigma \times \sqrt{\frac{Q}{V}}
$$

**Participation rate:**

$$
\rho = \frac{Q}{V}
$$

---

## Open Interest Notation


| Symbol | Meaning | Units |
|--------|---------|-------|
| $\text{OI}$ | Open interest | Base currency or USD |
| $\text{OI}_{\text{Long}}$ | Long open interest | Aggregate long positions |
| $\text{OI}_{\text{Short}}$ | Short open interest | Aggregate short positions |

**Note:** $\text{OI}_{\text{Long}} = \text{OI}_{\text{Short}}$ by definition (every long has a short counterparty).

---

## Basis and Spread Notation


| Symbol | Meaning | Formula |
|--------|---------|---------|
| $B$ | Basis | $B = P_{\text{futures}} - P_{\text{spot}}$ |
| $b$ | Basis (percentage) | $b = B / P_{\text{spot}}$ |
| $s$ | Spread (bid-ask) | $s = P_{\text{ask}} - P_{\text{bid}}$ |

**Basis annualization (quarterly futures):**

$$
b_{\text{annual}} = b \times \frac{365}{T}
$$

Where $T$ = days to expiration.

---

## Risk Metrics


| Symbol | Meaning | Formula |
|--------|---------|---------|
| $\text{VaR}$ | Value at Risk | Quantile of loss distribution |
| $\text{ES}$ | Expected Shortfall | Mean loss beyond VaR |
| $\beta$ | Beta to market | $\beta = \text{Cov}(r_{asset}, r_{market}) / \text{Var}(r_{market})$ |
| $\rho$ | Correlation | Pearson correlation coefficient |

---

## Greek Letters Summary


| Symbol | Usage in Chapter 26 |
|--------|---------------------|
| $\sigma$ | Volatility (daily or annual, context-dependent) |
| $\rho$ | Correlation coefficient or participation rate |
| $\lambda$ | Kyle's lambda (market impact coefficient) |
| $\gamma$ | Risk aversion parameter |
| $\eta$ | Temporary impact coefficient |
| $\alpha$ | Impact exponent (typically 0.5 for square root) |

---

## Time Conventions


| Symbol | Meaning |
|--------|---------|
| $T$ | Time horizon or days to expiration |
| $t$ | Current time or time index |
| $\Delta t$ | Time interval |
| 8h | Standard funding period (8 hours) |
| 365 | Trading days per year (crypto) |
| 252 | Trading days per year (TradFi comparison) |

---

## Currency and Asset Notation


| Symbol | Meaning |
|--------|---------|
| BTC | Bitcoin |
| ETH | Ethereum |
| USDT | Tether stablecoin |
| USDC | USD Coin stablecoin |
| USD | US Dollar |

**Pair notation:** BTC-USDT, ETH-USD, etc.

---

## Example Price Disclaimer


> **Note on Example Prices:** Throughout Chapter 26, numerical examples use illustrative prices (e.g., BTC = $43,000, ETH = $2,200) that reflect market conditions at the time of writing. These prices are for demonstration purposes only and should not be interpreted as current market prices or price forecasts. The mathematical relationships and formulas remain valid regardless of the specific prices used. Readers should substitute current market prices when applying these concepts in practice.

---

## Unit Conversions


**Basis points to percentage:**

$$
1 \text{ bp} = 0.01\% = 0.0001
$$

**Percentage to decimal:**

$$
1\% = 0.01
$$

**DXA (document units, for reference):**

$$
1 \text{ inch} = 1440 \text{ DXA}
$$

---

## Subscript Conventions


| Subscript | Meaning |
|-----------|---------|
| $_{\text{entry}}$ | At trade entry |
| $_{\text{exit}}$ | At trade exit |
| $_{\text{liq}}$ | At liquidation |
| $_{\text{spot}}$ | Spot market |
| $_{\text{perp}}$ | Perpetual market |
| $_{\text{fut}}$ | Futures market |
| $_{8h}$ | Per 8-hour period |
| $_{\text{daily}}$ | Per day |
| $_{\text{annual}}$ | Annualized |

---

*This notation guide ensures consistency across all Chapter 26 documents.*
