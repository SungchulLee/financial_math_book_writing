# What is a Forward and a Future?

Forwards and futures are the simplest derivative contracts: two parties agree today on a price for a transaction that will occur in the future. Unlike options, both parties are **obligated** to perform — there is no optionality and no premium changes hands at inception. This simplicity makes forwards and futures the natural starting point for understanding derivative pricing.

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

| Contract | Exchange | Contract size | Settlement |
|---|---|---|---|
| WTI Crude Oil | NYMEX (CME) | 1,000 barrels | Physical delivery |
| S&P 500 E-mini | CME | \$50 $\times$ index level | Cash settlement |
| KOSPI 200 | KRX | 250,000 KRW $\times$ index level | Cash settlement |

A single S&P 500 E-mini futures contract with the index at 5,000 controls a notional value of

$$
\$50 \times 5{,}000 = \$250{,}000
$$

Similarly, one KOSPI 200 futures contract with the index at 350 controls

$$
250{,}000 \text{ KRW} \times 350 = 87{,}500{,}000 \text{ KRW}
$$

These large notional amounts relative to the margin required illustrate the **leverage** embedded in futures contracts.

---

## Physical Delivery vs Cash Settlement

At maturity, a futures contract is settled in one of two ways:

- **Physical delivery**: The seller delivers the actual underlying asset and the buyer pays the delivery price. This is standard for commodity futures (crude oil, wheat, gold).
- **Cash settlement**: No physical asset changes hands. Instead, the difference between the futures price and the spot price at expiration is paid in cash. This is typical for index futures, where delivering a basket of 200 or 500 stocks would be impractical.

In mathematical pricing, the settlement method does not affect the no-arbitrage price of the contract — what matters is the value of the underlying at maturity.

---

## Long and Short Positions

Every forward or futures contract has exactly two sides:

**Long position (buyer)**: Agrees to **buy** the asset at price $K$ at maturity $T$. The long benefits when the asset price rises above $K$.

**Short position (seller)**: Agrees to **sell** the asset at price $K$ at maturity $T$. The short benefits when the asset price falls below $K$.

Both parties are **obligated** to perform at maturity. This is the fundamental distinction from options, where the holder has the right but not the obligation. Because of this symmetry, neither party pays an upfront premium — the contract is structured so that at inception, the expected benefit to each side is equal.

---

## Key Difference from Options

It is worth emphasizing the contrast with options. An option buyer pays a premium for the **right** to transact; if the market moves unfavorably, the buyer simply walks away, losing only the premium. A forward or futures participant has no such escape: the contract **must** be honored regardless of market conditions. This obligation means that both the long and the short face potentially unlimited losses — a feature that makes margin and daily settlement essential for futures markets.

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
