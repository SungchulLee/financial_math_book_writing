# Futures vs Forwards

**Key idea**: Daily settlement transforms credit risk into liquidity risk — the counterparty may not default, but must fund daily margin calls.

## A Five-Day Tale of Two Contracts

Before any taxonomy, watch the same economic exposure run through two settlement machines. Two long positions on the S&P 500 are entered at $F_0 = 5{,}000$; both will close out at $F_5 = 5{,}080$ five days later. The cumulative gain is identical: $80$ index points, or \$4,000 at the \$50 E-mini multiplier.

| Day | Settlement | Forward cash flow | Futures cash flow |
|---|---|---|---|
| 0 | 5,000 | — | — |
| 1 | 4,960 | $0$ | $-\$2{,}000$ |
| 2 | 5,020 | $0$ | $+\$3{,}000$ |
| 3 | 4,990 | $0$ | $-\$1{,}500$ |
| 4 | 5,040 | $0$ | $+\$2{,}500$ |
| 5 | 5,080 | $+\$4{,}000$ | $+\$2{,}000$ |
| **Total** | | $\$4{,}000$ | $\$4{,}000$ |

The two columns sum to the same number, but the *paths* differ:

- The **forward** holder receives a single \$4,000 payment on day 5, after carrying the full unrealized P&L for five days against a counterparty who might default before maturity.
- The **futures** holder receives daily flows $F_t - F_{t-1}$ — small, signed, sometimes negative. After day 1 the trader had to *post* \$2,000 to the exchange in cash, or face liquidation, even though the position would ultimately profit by \$4,000.

Three observations follow immediately:

- Cumulative cash is identical, so under deterministic rates the *prices* of the two contracts must also be identical — that is the theorem below.
- The forward exposes one party to credit risk over the whole horizon; the futures caps that exposure at one day's adverse move.
- A futures trader who is right about the terminal price can still be forced out at day 1 if cash to fund margin runs short — **credit risk has been transformed into liquidity risk**.

The rest of this page formalizes these observations: the structural comparison, the deterministic-rate theorem, and the convexity adjustment that breaks the equivalence when rates are stochastic.

---

## A Structural Comparison

Both futures and forwards are agreements to buy or sell an asset at a predetermined price on a future date. Despite this shared purpose, they differ fundamentally in how they are traded, settled, and regulated. Understanding these differences is essential for pricing, risk management, and choosing the right instrument in practice.

---

## Comparison of Key Features

The table below summarizes the structural differences between forwards and futures.

| Feature | Forward | Future |
|---|---|---|
| Trading venue | Over-the-counter (OTC) | Organized exchange |
| Contract terms | Customized (any size, maturity, asset) | Standardized (fixed sizes, expiry dates) |
| Counterparty risk | Direct exposure to the other party | Clearinghouse acts as counterparty |
| Settlement | Single payment at maturity | Daily mark-to-market (daily settlement) |
| Liquidity | Generally lower; harder to exit | Higher; can close position by offsetting |
| Regulation | Minimal | Regulated by exchange rules and authorities |
| Margin requirement | Negotiable (often none at inception) | Initial and maintenance margin required |

In short, forwards offer flexibility while futures offer liquidity and credit safety.

A practical consequence of standardization is that futures contracts have fixed expiry months rather than custom maturity dates. A hedger needing protection through mid-July must choose between the June and August contracts rather than matching the exact date. To maintain continuous exposure, futures traders periodically **roll** their positions — closing the expiring contract and opening the next — incurring transaction costs and potential slippage at each roll. Forward users, by contrast, can match the maturity precisely to their need and hold a single position without rolling.

---

## Why Mark-to-Market Matters

Recall (see [§ Margin and Marking to Market](margin_mark_to_market.md)): daily settlement replaces a single terminal payment with daily flows $F_k - F_{k-1}$ that telescope to $F_n - F_0$, converting credit risk into liquidity risk.

---

## When Forward and Futures Prices Are Equal

A natural question is whether the forward price and the futures price on the same underlying with the same maturity must agree.

**Theorem.** If interest rates are deterministic (constant or a known function of time), then the forward price equals the futures price.

The intuition is straightforward. When rates are deterministic, the reinvestment of daily settlement cash flows is perfectly predictable. One can replicate a forward payoff using futures, and vice versa, at zero cost. Since both contracts deliver the same terminal exposure with no additional cost, no-arbitrage forces their prices to coincide.

Recall (see [§ No-Arbitrage Pricing of Forwards](no_arbitrage_pricing.md) and [§ Cost of Carry](cost_of_carry.md)): under deterministic rates this common value is $F_0 = S_0 e^{rT}$ for a non-dividend-paying asset, generalizing to $S_0 e^{(r-q)T}$ with continuous dividend yield $q$.

---

## When They Differ: The Convexity Adjustment

For most practical purposes, forward and futures prices are nearly identical. The difference becomes meaningful only when interest rates are **stochastic** and correlated with the underlying — a subtlety that primarily affects interest rate derivatives. The following discussion explains the mechanism; readers focused on equity applications may safely note the conclusion and move on.

When interest rates are stochastic, the forward price and the futures price generally diverge. The reason is that daily settlement interacts with random interest rates.

Consider a long futures position. When the futures price rises, gains are received and can be reinvested. If interest rates tend to be high when the underlying price rises (positive correlation between $S$ and $r$), then gains are reinvested at favorable rates and losses are financed at low rates. This makes the long futures position more attractive than a long forward, pushing the futures price above the forward price.

The relationship can be expressed as

$$
G_0 = F_0 + \text{convexity adjustment}
$$

where $G_0$ is the futures price and $F_0$ is the forward price. When the asset price $S$ and the interest rate $r$ are **positively correlated**, the adjustment is positive and $G_0 > F_0$. When they are **negatively correlated**, $G_0 < F_0$.

This is sometimes called the **futures convexity bias**. Why does this matter? In fixed-income markets, where the underlying (a bond or interest rate) is mechanically linked to interest rates themselves, the adjustment can be material and must be accounted for in pricing.

---

## Practical Significance

For most equity and equity-index products, the correlation between the asset price and interest rates is weak, and the time to maturity is moderate. In these cases, the convexity adjustment is negligible, and practitioners treat forward and futures prices as interchangeable.

The distinction becomes material in two settings:

1. **Interest rate derivatives**: Eurodollar futures (now replaced by SOFR futures) versus forward rate agreements, where the underlying itself is an interest rate.
2. **Long-dated contracts**: Over horizons of several years, even small correlations compound into meaningful price differences.

For a short-dated equity futures contract, the difference between the forward and futures price is typically on the order of a few basis points, well within bid-ask spreads.

---

## Exercises

**Exercise 1.** A non-dividend-paying stock trades at $S_0 = 100$. The continuously compounded risk-free rate is $r = 5\%$ and the contract maturity is $T = 0.5$ years. Assuming deterministic interest rates, compute the common forward/futures price.

??? success "Solution"
    Under deterministic rates, the forward price equals the futures price:

    $$
    F_0 = S_0 \, e^{rT} = 100 \times e^{0.05 \times 0.5}
    $$

    $$
    = 100 \times e^{0.025} = 100 \times 1.02532 = 102.53
    $$

    The forward and futures price are both $\$102.53$.

---

**Exercise 2.** Explain why daily mark-to-market reduces counterparty credit risk compared to a forward contract that settles only at maturity. In your answer, contrast the maximum credit exposure under each arrangement for a contract with notional value \$1,000,000 and six months to maturity.

??? success "Solution"
    In a forward contract, no cash changes hands until maturity. Over six months, the value of the contract to one party can grow substantially. If the counterparty defaults at that point, the entire accumulated gain is at risk. The maximum credit exposure equals the full change in the contract's mark-to-market value over the entire six-month period, which for a \$1,000,000 notional could be tens of thousands of dollars or more.

    With daily mark-to-market, gains and losses are settled every day. If a counterparty defaults, the maximum loss is roughly one day's price movement. For a \$1,000,000 notional, a typical daily move might be on the order of \$1,000 to \$5,000, which is far smaller than the exposure that could accumulate over six months.

    Additionally, the margin system requires each party to post collateral (initial margin) that covers several days of adverse moves, providing a further buffer. The clearinghouse can liquidate positions before losses exceed the posted margin.

---

**Exercise 3.** Suppose the asset price $S$ and the short rate $r$ are positively correlated. Explain intuitively why the futures price exceeds the forward price. Would the relationship reverse if the correlation were negative?

??? success "Solution"
    When $S$ and $r$ are positively correlated, a long futures position benefits from favorable reinvestment dynamics. When the futures price rises (generating a margin credit), interest rates also tend to be high, so the daily gains can be reinvested at above-average rates. Conversely, when the futures price falls (generating a margin debit), interest rates tend to be low, so losses are financed at below-average rates.

    This asymmetry makes the long futures position more valuable than a long forward (which has no intermediate cash flows to reinvest). To restore no-arbitrage equilibrium, the futures price must be set higher than the forward price: $G_0 > F_0$.

    Yes, the relationship reverses if the correlation is negative. With negative correlation, gains arrive when rates are low (poor reinvestment) and losses arrive when rates are high (expensive financing). This makes the long futures position less attractive, so the futures price must be lower than the forward price: $G_0 < F_0$.

---

**Exercise 4.** Under constant interest rates, show that the cumulative cash flow from a long futures position entered at price $F_0$ and held to maturity at price $F_n$ equals $F_n - F_0$, the same as the payoff of a long forward. Explain why the present values of these two cash flow streams are nevertheless identical when $r$ is constant.

??? success "Solution"
    The daily cash flows from the futures position are $F_1 - F_0, \, F_2 - F_1, \, \ldots, \, F_n - F_{n-1}$. The cumulative (undiscounted) total is the telescoping sum:

    $$
    \sum_{k=1}^{n}(F_k - F_{k-1}) = F_n - F_0
    $$

    This equals the forward payoff $F_n - F_0$ received at maturity.

    However, the futures cash flows are received at different times: the cash flow $F_k - F_{k-1}$ is received at day $k$, not at maturity. The present value of the futures cash flow stream is:

    $$
    \text{PV}_{\text{futures}} = \sum_{k=1}^{n}(F_k - F_{k-1}) \, e^{-r \, t_k}
    $$

    while the forward payoff has present value $(F_n - F_0) \, e^{-rT}$.

    When $r$ is constant (and known), a hedging argument shows these are equal. Each daily cash flow $F_k - F_{k-1}$ received at time $t_k$ can be invested (or borrowed) at the known rate $r$ to time $T$, yielding $(F_k - F_{k-1}) \, e^{r(T - t_k)}$ at maturity. The sum of these rolled-up cash flows, discounted back to time $0$, equals $(F_n - F_0) \, e^{-rT}$ because the compounding factors are deterministic. This is precisely why forward and futures prices coincide under deterministic rates: the reinvestment strategy perfectly transforms one cash flow pattern into the other.

---

**Exercise 5.** Suppose the futures price $G_0$ and forward price $F_0$ on the same underlying satisfy $G_0 = F_0 + 0.30$ for a 5-year contract. Explain qualitatively whether the underlying $S$ is more likely positively or negatively correlated with short-term interest rates $r$, and identify a real-world asset class where this sign matters in practice.

??? success "Solution to Exercise 5"
    Since $G_0 > F_0$, the convexity adjustment is positive. Recall: a positive adjustment corresponds to **positive** correlation between $S$ and $r$ — gains on the long futures arrive when rates are high (favorable reinvestment) and losses arrive when rates are low (cheap financing), making the long futures preferable to the long forward and pushing $G_0$ above $F_0$.

    This sign matters most for **interest rate derivatives** (e.g., SOFR futures vs. forward rate agreements), where the underlying is mechanically tied to interest rates and the correlation is strong. For short-dated equity index futures the correlation is weak and the adjustment is negligible.

---

**Exercise 6.** A producer wants to hedge revenue from selling 50,000 barrels of crude oil exactly 75 days from today. The exchange lists WTI futures with monthly expirations only. Explain the trade-offs between using a customized OTC forward versus stacking exchange-traded futures, in terms of basis risk, credit risk, and liquidity.

??? success "Solution to Exercise 6"
    With a customized OTC **forward**, the producer can match the exact 75-day maturity and the exact 50,000-barrel notional. There is **no basis risk** at maturity (the contract settles against the producer's actual delivery), but the producer is exposed to **counterparty credit risk** for the full 75 days, and the contract is illiquid — exiting early is difficult and usually expensive.

    With exchange-traded **futures**, the producer would use the nearest monthly contracts (e.g., the contract expiring just after day 75) and roll if needed. The clearinghouse eliminates credit risk and daily mark-to-market reduces accumulated exposure, but the maturity mismatch introduces **basis risk**: the futures price at day 75 may differ from the producer's local cash price. Liquidity is high — positions can be closed at any time at tight spreads — at the cost of having to fund daily margin calls.

    The choice trades off precision (forward) against credit safety and liquidity (futures); large producers commonly combine both.
