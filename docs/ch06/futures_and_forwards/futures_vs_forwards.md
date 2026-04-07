# Futures vs Forwards

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

---

## Why Mark-to-Market Matters

The most important operational difference is **daily settlement**. At the end of each trading day, the clearinghouse revalues every open futures position. Gains are credited and losses are debited from the trader's margin account.

Suppose a trader enters a long futures contract at price $F_0$. If the settlement price on day $k$ is $F_k$, then the cash flow on that day is

$$
F_k - F_{k-1}
$$

with $F_0$ being the initial futures price. Over the life of the contract, the cumulative cash flow is

$$
\sum_{k=1}^{n}(F_k - F_{k-1}) = F_n - F_0
$$

which equals the same total gain or loss as a forward, but the timing of cash flows is different. This daily realization of gains and losses dramatically reduces credit exposure: no large obligation accumulates over the contract's life.

---

## When Forward and Futures Prices Are Equal

A natural question is whether the forward price and the futures price on the same underlying with the same maturity must agree.

**Theorem.** If interest rates are deterministic (constant or a known function of time), then the forward price equals the futures price.

The intuition is straightforward. When rates are deterministic, the reinvestment of daily settlement cash flows is perfectly predictable. One can replicate a forward payoff using futures, and vice versa, at zero cost. Since both contracts deliver the same terminal exposure with no additional cost, no-arbitrage forces their prices to coincide.

Formally, if $r$ is constant and the maturity is $T$, then both the forward price and the futures price equal

$$
F_0 = S_0 \, e^{rT}
$$

for a non-dividend-paying asset, or more generally $S_0 \, e^{(r-q)T}$ with continuous dividend yield $q$.

---

## When They Differ: The Convexity Adjustment

When interest rates are **stochastic**, the forward price and the futures price generally diverge. The reason is that daily settlement interacts with random interest rates.

Consider a long futures position. When the futures price rises, gains are received and can be reinvested. If interest rates tend to be high when the underlying price rises (positive correlation between $S$ and $r$), then gains are reinvested at favorable rates and losses are financed at low rates. This makes the long futures position more attractive than a long forward, pushing the futures price above the forward price.

The relationship can be expressed as

$$
G_0 = F_0 + \text{convexity adjustment}
$$

where $G_0$ is the futures price and $F_0$ is the forward price. When the asset price $S$ and the interest rate $r$ are **positively correlated**, the adjustment is positive and $G_0 > F_0$. When they are **negatively correlated**, $G_0 < F_0$.

This is sometimes called the **futures convexity bias** and is particularly relevant in fixed-income markets, where the underlying (a bond or interest rate) is mechanically linked to interest rates themselves.

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
