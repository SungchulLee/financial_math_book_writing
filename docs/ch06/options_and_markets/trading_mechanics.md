# Trading Mechanics

Before developing the mathematical theory of option pricing, it is important to understand the institutional framework in which options are traded. The structure of the market --- whether trades occur on a centralized exchange or bilaterally between counterparties --- determines the degree of contract standardization, the liquidity available to participants, and the procedures governing exercise and settlement. These practical details motivate several modeling assumptions that appear later in the Black-Scholes framework.

---

## Exchange-Traded vs OTC Options

Options are traded in two distinct venues:

**Exchange-traded options** are bought and sold on organized exchanges such as the Chicago Board Options Exchange (CBOE), Eurex, or the International Securities Exchange. The exchange acts as an intermediary: it defines contract specifications, maintains an order book, and interposes a central clearinghouse between buyer and seller. Because the clearinghouse becomes the counterparty to every trade, individual credit risk is effectively eliminated.

**Over-the-counter (OTC) options** are negotiated privately between two parties, typically a bank and a corporate client or institutional investor. OTC contracts can be tailored to any underlying, strike, maturity, or payoff structure, making them suitable for hedging exposures that do not align with standardized contracts. The trade-off is **counterparty risk**: if the option writer defaults, the holder may not receive the payoff owed. OTC markets also lack the price transparency of exchanges, since quotes are not publicly displayed.

| Feature | Exchange-traded | OTC |
|---|---|---|
| Standardization | Fixed contract terms | Fully customizable |
| Counterparty risk | Eliminated by clearinghouse | Borne by each party |
| Liquidity | High for popular contracts | Varies widely |
| Price transparency | Public order book | Private quotes |

---

## Contract Standardization

Exchange-traded equity options follow strict standardization rules. In the US equity options market, the key conventions are:

- **Contract size**: Each contract covers 100 shares of the underlying stock. If the quoted price of a call option is \$3.40, the total premium for one contract is

$$
100 \times 3.40 = \$340
$$

- **Strike prices**: Strikes are set at regular intervals (typically \$1, \$2.50, or \$5, depending on the stock price) and new strikes are introduced as the stock price moves
- **Expiration dates**: Standard monthly options expire on the third Friday of the expiration month. Weekly expirations and longer-dated LEAPS (Long-term Equity AnticiPation Securities) are also available for liquid underlyings
- **Exercise style**: US-listed equity options are generally **American-style** (exercisable at any time up to expiration), while index options are often **European-style** (exercisable only at expiration)

Standardization is what makes exchange trading possible: because every contract with the same underlying, strike, and expiration is interchangeable, buyers and sellers need not find each other directly. A trader who bought a call can close the position simply by selling an identical call on the exchange.

---

## Contract Specifications: Real Market Examples

In practice, the **contract multiplier** determines the monetary scale of premiums and payoffs. Two prominent examples illustrate the convention:

### S&P 500 Index Options (SPX)

- **Underlying**: S&P 500 Index
- **Multiplier**: \$100 per index point
- **Settlement**: Cash-settled, European-style
- **Expiration**: Standard monthly options expire on the **third Friday** of the expiration month; weekly options (SPXW) expire Monday, Wednesday, or Friday
- **Final settlement**: Monthly options use **AM settlement** based on the Special Opening Quotation (SOQ) — a value computed from the opening prices of all 500 index constituents. Weekly options use **PM settlement** based on the closing index level

If the quoted premium of an SPX call is 20, the actual cost is:

$$
20 \times 100 = \$2{,}000
$$

At maturity, if the index is at 5,250 with strike $K = 5{,}200$, the cash payoff is:

$$
(5{,}250 - 5{,}200)^+ \times 100 = 50 \times 100 = \$5{,}000
$$

### KOSPI 200 Options

- **Underlying**: KOSPI 200 Index
- **Multiplier**: 250,000 KRW per index point
- **Settlement**: Cash-settled, European-style
- **Expiration**: Monthly options expire on the **second Thursday** of the expiration month
- **Tick size**: 0.01 index points = 2,500 KRW per contract

If the quoted premium is 0.80, the actual cost is:

$$
0.80 \times 250{,}000 = 200{,}000 \text{ KRW}
$$

If at maturity the index is at 320 with strike $K = 300$:

$$
(320 - 300)^+ \times 250{,}000 = 20 \times 250{,}000 = 5{,}000{,}000 \text{ KRW}
$$

### Why Multipliers Matter

The multiplier directly affects the monetary value of payoffs, the risk exposure per contract, and the margin requirements. Throughout this text, we work in **normalized units** (one unit of underlying), so the payoff of a call is simply $(S_T - K)^+$. In practice, all quantities must be scaled by the contract multiplier to obtain actual dollar (or won) amounts.

---

## Bid-Ask Spread and Liquidity

At any moment, the order book displays two prices for each option contract:

- **Bid price**: The highest price a buyer is currently willing to pay
- **Ask price**: The lowest price a seller is currently willing to accept

The **bid-ask spread** is the difference between the two. If the bid is \$2.80 and the ask is \$3.00, the spread is \$0.20. The spread represents a transaction cost: a trader who buys at the ask and immediately sells at the bid loses the spread.

Liquidity --- the ease of executing trades without significant price impact --- varies across contracts. At-the-money options with near-term expirations on actively traded stocks have tight spreads (a few cents), while deep out-of-the-money options on illiquid underlyings may have spreads that are a substantial fraction of the option's value. The **relative spread**, defined as

$$
\text{Relative spread} = \frac{\text{Ask} - \text{Bid}}{\tfrac{1}{2}(\text{Ask} + \text{Bid})}
$$

provides a normalized measure of transaction costs that is comparable across contracts with different price levels.

??? example "Bid-Ask Spreads in Practice"
    For SPX options near the money with near-term expiration, bid-ask spreads are typically a few index points wide. An ATM SPX call might show a bid of 177 and an ask of 182 — a spread of 5 points, or \$500 per contract at the \$100 multiplier. At-the-money options on actively traded indices have relative spreads of a few percent, while far out-of-the-money options on illiquid underlyings may have relative spreads exceeding 20%.

    KOSPI 200 options, which are among the most actively traded index options in the world, typically exhibit tight spreads near the money — reflecting a market with exceptionally high retail participation compared to the more institutionally dominated SPX options market.

---

## Market Makers

Why does liquidity matter for pricing theory? The Black-Scholes model assumes continuous, frictionless trading. In practice, the bid-ask spread is the primary friction, and its size determines how closely real hedging approximates the theoretical ideal.

Liquidity on options exchanges is provided in large part by **market makers** --- firms that continuously post bid and ask quotes and stand ready to trade in either direction. Market makers profit from the bid-ask spread but bear inventory risk: after filling a customer order, they hold a position that must be hedged. In practice, market makers use delta hedging and other Greek-based strategies to manage this risk, making the Black-Scholes framework not merely an academic construct but the operational backbone of options market-making.

---

## Settlement and Exercise

When an option is exercised, the terms of the contract must be fulfilled. The settlement procedure depends on the contract type:

**Physical settlement**: The underlying asset is delivered. For equity options, the call holder pays $K$ per share and receives the shares; the put holder delivers the shares and receives $K$ per share. Most US equity options use physical settlement.

**Cash settlement**: No asset changes hands. Instead, the writer pays the holder the intrinsic value of the option at expiration. For a call, the cash payment is

$$
(S_T - K)^+
$$

per unit of the underlying. Index options (e.g., S\&P 500 options) are typically cash-settled because delivering a basket of 500 stocks is impractical.

For American-style options, early exercise introduces additional considerations. A holder may exercise before expiration if it is optimal to do so --- for example, to capture a dividend on the underlying stock. The **Options Clearing Corporation (OCC)** manages the exercise and assignment process: when a holder exercises, the OCC randomly selects a writer with an open short position in the same contract to fulfill the obligation.

From the standpoint of mathematical pricing theory, the distinction between physical and cash settlement is immaterial. In both cases, the economic value to the holder at expiration is $(S_T - K)^+$ for a call and $(K - S_T)^+$ for a put, and this is the payoff function used throughout the remainder of the text.

---

## Exercises

**Exercise 1.** A trader buys 5 contracts of a European call option quoted at \$4.20 per share. Each contract covers 100 shares. What is the total premium paid? If at expiration $S_T = 72$ and $K = 65$, what is the total payoff and the total profit?

??? success "Solution to Exercise 1"
    The total premium paid is

    $$
    5 \times 100 \times 4.20 = \$2{,}100
    $$

    At expiration, each share yields a payoff of $(S_T - K)^+ = (72 - 65)^+ = 7$. The total payoff across all 5 contracts is

    $$
    5 \times 100 \times 7 = \$3{,}500
    $$

    The total profit is payoff minus premium: $3{,}500 - 2{,}100 = \$1{,}400$.

---

**Exercise 2.** An option has a bid price of \$1.50 and an ask price of \$1.80. Compute the bid-ask spread and the relative spread. If a trader buys 10 contracts (100 shares each) at the ask and immediately sells at the bid, what is the total transaction cost?

??? success "Solution to Exercise 2"
    The bid-ask spread is $1.80 - 1.50 = \$0.30$.

    The relative spread is

    $$
    \frac{1.80 - 1.50}{\tfrac{1}{2}(1.80 + 1.50)} = \frac{0.30}{1.65} \approx 0.1818 = 18.18\%
    $$

    The total transaction cost from the round-trip trade is the spread times the number of shares:

    $$
    10 \times 100 \times 0.30 = \$300
    $$

---

**Exercise 3.** Explain why exchange-traded options eliminate counterparty risk while OTC options do not. In your answer, describe the role of the clearinghouse and discuss one advantage that OTC options retain despite this disadvantage.

??? success "Solution to Exercise 3"
    On an exchange, every trade is novated through a central **clearinghouse**: once a trade is executed, the clearinghouse becomes the buyer to every seller and the seller to every buyer. The clearinghouse manages risk by requiring margin deposits from all participants and marking positions to market daily. Even if one counterparty defaults, the clearinghouse guarantees performance of the contract using its own capital and the defaulting party's margin. This structure effectively eliminates counterparty risk for exchange participants.

    In the OTC market, no such intermediary exists. The buyer and seller deal directly with each other, and each bears the risk that the other party may fail to honor the contract. This risk is mitigated through bilateral collateral agreements (Credit Support Annexes under ISDA documentation), but it is not eliminated.

    Despite the counterparty risk disadvantage, OTC options offer **full customization**. An airline hedging fuel costs over an irregular schedule, or a corporation hedging a foreign currency exposure with a non-standard notional amount and maturity, can negotiate an OTC contract tailored precisely to its needs. Exchange-traded contracts, bound by standardized strikes, maturities, and underlyings, may not provide an adequate hedge for such exposures.

---

**Exercise 4.** A European call option on a stock index is cash-settled with $K = 2{,}000$. At expiration, the index level is $S_T = 2{,}073.50$. The contract multiplier is \$100 per index point. Compute the cash payment from the writer to the holder. Compare this to what would happen under physical settlement and explain why cash settlement is the standard convention for index options.

??? success "Solution to Exercise 4"
    Under cash settlement, the writer pays the holder

    $$
    (S_T - K)^+ \times 100 = (2{,}073.50 - 2{,}000)^+ \times 100 = 73.50 \times 100 = \$7{,}350
    $$

    Under physical settlement, the holder would pay $K \times 100 = 2{,}000 \times 100 = \$200{,}000$ and receive a portfolio replicating the index (i.e., all constituent stocks in their index-weighted proportions). The holder could then sell this portfolio at the market value of $2{,}073.50 \times 100 = \$207{,}350$, realizing the same net gain of \$7,350.

    Cash settlement is the standard for index options because physical delivery would require assembling or disassembling a portfolio of hundreds of stocks in their precise index weights --- a logistically burdensome and costly operation. Cash settlement achieves the same economic outcome without the need to trade the underlying stocks, reducing transaction costs and operational complexity.
