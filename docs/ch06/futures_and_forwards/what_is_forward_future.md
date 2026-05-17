# What is a Forward and a Future?

## A Farmer and a Baker

Before any formal definition, watch the mechanism work between two people. In March, a wheat farmer expects to harvest 5,000 bushels in September. At the same time, an industrial baker knows the same volume will be needed for autumn production. Today's spot price is \$6 per bushel, but neither side wants to gamble on September: the farmer fears a price collapse, the baker fears a price spike. They agree, in writing, to exchange 5,000 bushels at \$6.50 per bushel on September 15. No money changes hands today. Whatever the September spot price turns out to be — \$4.50, \$6.50, or \$9.00 — both parties are bound to the agreed terms.

That single agreement is a **forward contract**. Strip the wheat and the names away and you are left with three pieces:

- A future date (September 15).
- A predetermined price (\$6.50 per bushel — the *delivery price* $K$).
- An obligation, symmetric on both sides, to transact at that price on that date.

A **futures contract** is the same agreement made anonymous and tradable. Instead of the farmer and baker locating one another, an exchange writes a standardized version of the contract — fixed contract size, fixed expiry dates, a clearinghouse as guaranteed counterparty — and lets thousands of unrelated participants take either side. The economic structure is identical; what changes is *who is on the other side* and *how* the obligation is enforced.

The rest of this page formalizes these two ideas (forward = bilateral, futures = exchange-traded), surveys real contracts in modern markets, and shows how the same mechanism extends from physical commodities to volatility itself.

---

## Forwards and Futures in Two Sentences

Forwards and futures are the simplest derivative contracts: two parties agree today on a price for a transaction that will occur in the future. Unlike options, both parties are **obligated** to perform — there is no optionality and no premium changes hands at inception, which is why forwards and futures are the natural starting point for understanding derivative pricing.

---

## Forward Contracts

A **forward contract** is a binding agreement between two parties to buy or sell a specified asset at a predetermined price on a specified future date. Formally, a forward contract specifies:

- **Underlying asset**: the commodity, stock, index, or financial instrument to be exchanged
- **Delivery price** $K$: the price agreed upon at inception for the future transaction
- **Maturity** $T$: the date at which the transaction takes place
- **Notional amount**: the quantity of the underlying asset covered by the contract

At time $t = 0$ the contract is initiated, and at time $t = T$ the buyer pays $K$ and receives the asset. The key feature is that **no money changes hands at inception** — the delivery price $K$ is chosen so that the contract has zero initial value.

Forwards are **over-the-counter (OTC)** instruments: they are privately negotiated between two counterparties, and their terms (maturity, notional, delivery method) can be fully customized.

---

## Futures Contracts

A **futures contract** is a standardized forward contract traded on an organized exchange. The exchange specifies the contract terms — underlying asset, contract size, delivery months, and settlement procedure — so that contracts are fungible and can be traded anonymously.

The critical difference from forwards is the mechanism of **daily settlement** (mark-to-market). Rather than waiting until maturity to settle the full amount, gains and losses are realized every day through a margin account. This virtually eliminates counterparty credit risk, which is the main vulnerability of OTC forwards.

---

## Real-World Examples

| Contract | Exchange | Contract size | 1-point P&L |
|---|---|---|---|
| S&P 500 E-mini (ES) | CME | \$50 $\times$ index | \$50 |
| S&P 500 Micro E-mini (MES) | CME | \$5 $\times$ index | \$5 |
| KOSPI 200 | KRX | 250,000 KRW $\times$ index | 250,000 KRW |
| KOSPI 200 Mini | KRX | 50,000 KRW $\times$ index | 50,000 KRW |
| WTI Crude Oil | NYMEX | 1,000 barrels (\$1 move = \$1,000) | \$1,000 |
| Gold | COMEX | 100 troy ounces (\$1 move = \$100) | \$100 |

!!! note "S&P 500 futures naming"
    A full-size S&P 500 futures contract (ticker SP, multiplier \$250) once existed but is largely obsolete. When practitioners say "S&P 500 futures" they almost always mean the **E-mini (ES)**. The **Micro E-mini (MES)** at \$5 per point is one-tenth the size of ES, making it accessible to smaller accounts.

A "1-point move" always refers to one unit of the quoted price. The **contract size** determines how many such units you control, and therefore how price changes translate into profit and loss.

A single S&P 500 E-mini futures contract with the index at 5,000 controls a notional value of

$$
\$50 \times 5{,}000 = \$250{,}000
$$

If the index moves from 5,000 to 5,010, the holder gains $10 \times \$50 = \$500$.

Similarly, one KOSPI 200 futures contract with the index at 350 controls

$$
250{,}000 \text{ KRW} \times 350 = 87{,}500{,}000 \text{ KRW}
$$

The KOSPI 200 Mini contract at the same level controls one-fifth of this: $50{,}000 \times 350 = 17{,}500{,}000$ KRW, making it accessible to smaller participants.

While contract specifications differ across markets, the economic structure is identical: a quoted price multiplied by a contract size determines the monetary exposure. These large notional amounts relative to the margin required illustrate the **leverage** embedded in futures contracts.

### Contract Month Codes and the Front Month

Exchange-traded futures are identified by a ticker symbol that encodes the underlying asset and the delivery month. The standard month codes used across most exchanges are:

| Code | Month | Code | Month |
|---|---|---|---|
| F | January | N | July |
| G | February | Q | August |
| H | March | U | September |
| J | April | V | October |
| K | May | X | November |
| M | June | Z | December |

For example, CLK26 denotes the WTI crude oil contract for May 2026 delivery, and CLM26 denotes June 2026. The **front-month contract** is the nearest active contract — the one with the closest delivery date that has not yet expired.

Because many futures expire *before* the delivery month begins, the calendar can be unintuitive. WTI crude oil futures stop trading roughly three business days before the 25th of the month prior to delivery. The April 2026 contract (CLJ26) therefore expired in late March; by early April the front month had already rolled to May (CLK26).

Most traders do not hold contracts to delivery. Instead they **roll** their positions — selling the expiring front-month contract and buying the next — typically one to two weeks before expiration as liquidity shifts to the next contract.

---

## Volatility Futures and ETFs (VIX, UVIX)

Not all futures are written on physical assets or equity indices. A particularly important modern class is **volatility derivatives**, whose underlying is the market's *expectation* of future volatility rather than a tradable asset.

### VIX Futures

The **VIX index** measures the market's expectation of 30-day volatility of the S&P 500. Because the VIX itself is not directly tradable, exchanges list **VIX futures** that allow investors to trade forward expectations of volatility. A VIX futures contract specifies a maturity $T$ and a price representing expected volatility at $T$. At maturity, VIX futures are **cash-settled** against a special settlement value of the VIX index.

- Rising VIX futures → market expects higher volatility (often stress or downturns).
- Falling VIX futures → market expects calmer conditions.

### Term Structure and Rolling

Unlike equity index futures, VIX futures often exhibit a pronounced **term structure** (recall, see [§ Cost of Carry](cost_of_carry.md): contango when later maturities are priced higher, backwardation in crises). Traders typically hold the **front-month contract** and must **roll** before expiration; depending on the slope of the curve, rolling introduces systematic gains or losses.

### Volatility ETFs (UVIX)

Exchange-traded products such as **UVIX** (a 2× leveraged long short-term VIX futures ETF) provide leveraged exposure to a basket of front-month VIX futures, targeting approximately twice the *daily* return of that basket. Because of **daily rebalancing**, returns are path-dependent, and these products typically **decay** over time due to contango in the futures curve, rolling costs, and leverage compounding. They are short-term trading instruments, not long-term investments — UVIX can lose value even when realized volatility is flat.

### Conceptual Extension

VIX futures illustrate that the "underlying" of a futures contract need not be a physical asset — it can be an **expectation of a future quantity**. This reinforces the general principle (developed in [§ No-Arbitrage Pricing of Forwards](no_arbitrage_pricing.md)) that a futures price reflects the market's consensus expectation under risk-neutral dynamics, with the underlying itself potentially derived from other assets (e.g., option-implied variance).

??? note "Advanced: Risk-Neutral Pricing of VIX Futures"
    Naively one might expect

    $$
    F_t(T) = \mathbb{E}^{\mathbb{Q}}[\mathrm{VIX}_T \mid \mathcal{F}_t]
    $$

    to behave like the standard forward formula. The subtlety is that the VIX is itself a conditional expectation: schematically,

    $$
    \mathrm{VIX}_t^2 \approx \mathbb{E}^{\mathbb{Q}}[\text{realized variance over } [t, t + 30d] \mid \mathcal{F}_t]
    $$

    So a VIX future is

    $$
    F_t(T) = \mathbb{E}^{\mathbb{Q}}\!\left[ \sqrt{\mathbb{E}^{\mathbb{Q}}[\text{future variance} \mid \mathcal{F}_T]} \;\middle|\; \mathcal{F}_t \right]
    $$

    Because the square root is concave, Jensen's inequality gives

    $$
    F_t(T) \le \sqrt{\mathbb{E}^{\mathbb{Q}}[\text{future variance} \mid \mathcal{F}_t]}
    $$

    Consequences:

    - VIX futures are **not** equal to forward variance or to the current VIX.
    - The gap depends on volatility-of-volatility and on the correlation between variance and returns.
    - Pricing is model-dependent (e.g., Heston), illustrating that the general principle $F_t(T) = \mathbb{E}^{\mathbb{Q}}[\text{payoff}_T \mid \mathcal{F}_t]$ becomes subtle when the payoff is a **nonlinear functional of expectations** — a theme that returns when we price options.

---

## Physical Delivery vs Cash Settlement

At maturity, a futures contract is settled in one of two ways:

- **Physical delivery**: The seller delivers the actual underlying asset and the buyer pays the delivery price. This is standard for commodity futures (crude oil, wheat, gold).
- **Cash settlement**: No physical asset changes hands. Instead, the difference between the futures price and the spot price at expiration is paid in cash. This is typical for index futures, where delivering a basket of 200 or 500 stocks would be impractical.

In mathematical pricing, the settlement method does not affect the no-arbitrage price of the contract — what matters is the value of the underlying at maturity. In practice, however, the delivery mechanism has important operational consequences.

### Physical Delivery: WTI Crude Oil

WTI crude oil futures (CL) are physically delivered at Cushing, Oklahoma. Unlike contracts with a single settlement date, CL uses a **delivery window** spanning the entire delivery month — there is no single delivery date. After the contract expires, the process works as follows:

1. The **short position** (seller) submits a formal "Notice of Intention to Deliver," choosing when during the delivery month to deliver.
2. **CME Clearing** assigns the delivery notice to a long position holder, who must accept delivery.
3. The physical transfer of 1,000 barrels per contract (approximately 159,000 liters) is coordinated through pipeline and storage infrastructure at Cushing.

A trader who cannot take or make physical delivery must exit the position before expiration. Recall (see [§ Margin and Marking to Market](margin_mark_to_market.md)): on April 20, 2020, the front-month WTI contract settled at $-\$37.63$ because Cushing storage was full and trapped longs could not accept delivery.

### Cash Settlement: KOSPI 200

KOSPI 200 futures on the Korea Exchange (KRX) are cash-settled. Each contract expires on the **second Thursday** of the contract month, and the final settlement value is determined by a Special Opening Quotation (SOQ) of the KOSPI 200 index. No shares change hands — only the cash difference between the futures price and the settlement index level is exchanged. This clean mechanism avoids the logistical complexities of physical delivery entirely.

---

## Long, Short, and the Contrast with Options

Recall (see [§ Payoff of Forwards and Futures](payoff.md)): the long pays $K$ and receives the asset (benefits when $S_T > K$); the short does the reverse. Recall (see [§ From Forwards to Options](bridge_to_options.md)): both parties are symmetrically **obligated**, so no upfront premium is paid — this is the structural difference from options, where the holder pays for the right (not obligation) to transact.

---

## Exercises

**Exercise 1.** A farmer enters a forward contract to sell 5,000 bushels of wheat at a delivery price of \$6.50 per bushel, with maturity in 6 months. Describe the farmer's obligation and explain under what market conditions the farmer benefits or loses from this contract.

??? success "Solution to Exercise 1"
    The farmer holds a **short forward** position. At maturity, the farmer is obligated to deliver 5,000 bushels of wheat and receive $K = \$6.50$ per bushel, for a total of $5{,}000 \times 6.50 = \$32{,}500$.

    If the spot price at maturity is $S_T = \$5.80$, the farmer benefits: the wheat is worth only $5{,}000 \times 5.80 = \$29{,}000$ on the open market, but the farmer receives \$32,500 through the forward. The gain is $5{,}000 \times (6.50 - 5.80) = \$3{,}500$.

    If $S_T = \$7.20$, the farmer loses: the wheat could have been sold for $5{,}000 \times 7.20 = \$36{,}000$, but the forward obliges the farmer to sell for only \$32,500. The loss is $5{,}000 \times (7.20 - 6.50) = \$3{,}500$.

---

**Exercise 2.** An investor holds one long S&P 500 E-mini futures contract (multiplier \$50) entered at a futures price of 4,800. At the end of the day, the settlement price is 4,835. What is the daily mark-to-market cash flow? What if the settlement price is 4,770 instead?

??? success "Solution to Exercise 2"
    The daily cash flow is the change in futures price times the multiplier.

    If the settlement price rises to 4,835:

    $$
    \$50 \times (4{,}835 - 4{,}800) = \$50 \times 35 = \$1{,}750
    $$

    The long position receives \$1,750 credited to its margin account.

    If the settlement price falls to 4,770:

    $$
    \$50 \times (4{,}770 - 4{,}800) = \$50 \times (-30) = -\$1{,}500
    $$

    The long position has \$1,500 debited from its margin account.

---

**Exercise 3.** Explain why a forward contract requires no upfront payment while an option requires a premium. Relate your answer to the obligations of each party.

??? success "Solution to Exercise 3"
    In a forward contract, both parties are **symmetrically obligated**: the buyer must purchase and the seller must deliver. The delivery price $K$ is set so that the contract has zero value at inception — neither side has an advantage, so no payment is needed.

    In an option contract, the holder has the **right but not the obligation** to transact. This asymmetry favors the holder: in the worst case, the holder walks away and loses nothing beyond the premium. The writer, by contrast, bears all the downside risk. To compensate the writer for accepting this one-sided obligation, the holder must pay a premium at inception. The premium is the price of optionality.

---

**Exercise 4.** A KOSPI 200 futures contract has a multiplier of 250,000 KRW. An investor goes long at a futures price of 340 and closes the position three days later at a futures price of 348. Compute the total profit in KRW. If the exchange rate is 1,300 KRW per USD, what is the profit in USD?

??? success "Solution to Exercise 4"
    The total change in the futures price over the holding period is $348 - 340 = 8$ index points.

    The profit in KRW is:

    $$
    250{,}000 \text{ KRW} \times 8 = 2{,}000{,}000 \text{ KRW}
    $$

    Converting to USD at 1,300 KRW per USD:

    $$
    \frac{2{,}000{,}000}{1{,}300} \approx \$1{,}538.46
    $$

---

**Exercise 5.** UVIX targets approximately twice the daily return of a basket of front-month VIX futures. Suppose over two consecutive days the basket returns are $+10\%$ and $-10\%$. Compute the two-day return for an unleveraged holder of the basket and for a holder of UVIX (ignoring fees). What does this illustrate about leveraged ETFs as long-term holdings?

??? success "Solution to Exercise 5"
    The basket goes $1 \to 1.10 \to 0.99$, a two-day return of $-1\%$.

    UVIX targets twice the daily return, so it goes $1 \to 1.20 \to 0.96$, a two-day return of $-4\%$.

    Even though the basket loses only $1\%$, the leveraged product loses $4\%$. This is **volatility decay** from daily rebalancing: $2 \times$ the daily return is not the same as the cumulative return times $2$. Over many days with oscillation, even a flat basket can produce significant losses in the leveraged ETF — the reason UVIX is a short-term trading instrument, not a long-term hedge.

---

**Exercise 6.** WTI crude oil futures (CL) use the standard month codes. The current date is March 10, 2026, and the April 2026 contract (CLJ26) expired in late March (roughly three business days before the 25th of the prior month). Identify the front-month contract on March 10. What is the ticker for the June 2026 contract?

??? success "Solution to Exercise 6"
    The April 2026 contract (CLJ26) expired before March 25; on March 10, it is no longer the front month. The next active contract is **May 2026**, which uses month code **K**: ticker **CLK26**. This is the front month on March 10, 2026.

    The June 2026 contract uses month code **M**, giving ticker **CLM26**.
