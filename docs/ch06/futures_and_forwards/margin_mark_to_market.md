# Margin and Marking to Market

## One Day at the Margin Window

Before any definitions, watch what happens at the close of one trading day. A trader is long one S&P 500 E-mini futures contract (multiplier \$50) entered at $F_0 = 5{,}000$. The exchange has the trader deposit \$12,000 as an initial performance bond. By the end of the day, the settlement price prints at $F_1 = 5{,}030$. Three things happen automatically, in order:

1. The clearinghouse computes the day's price change: $\Delta_1 = 5{,}030 - 5{,}000 = 30$ index points.
2. It credits the trader's margin account with $\$50 \times 30 = \$1{,}500$ in cash.
3. The short side of the same contract is debited \$1,500 — a zero-sum transfer.

The trader's deposit is now \$13,500. The next morning the contract is treated as if it had been entered at $F_1 = 5{,}030$: the slate is wiped clean and the cycle repeats.

Three consequences follow immediately, and the rest of this page just unpacks them:

- A forward's *single* terminal payment $F_T - F_0$ has been replaced by *daily* payments $\sum_t \Delta_t$. The two sums are equal (telescope), but the timing is radically different.
- Because cash is exchanged every evening, no large unrealized obligation accumulates — counterparty credit risk is *capped* at one day's adverse move.
- The trader must keep enough cash on hand to absorb adverse $\Delta_t$ before they trigger a forced liquidation — *credit* risk has been swapped for *liquidity* risk.

The formal definitions below give names to the pieces of this one-day cycle.

---

## What Marking to Market Is

Exchange-traded futures contracts are settled daily through a process called **marking to market**. At the close of each trading day the exchange recalculates the contract's value using the day's settlement price, and the resulting gain or loss is immediately credited to or debited from the trader's margin account. This daily cash flow mechanism is the defining operational difference between futures and forwards.

---

## Initial Margin and Maintenance Margin

When a trader opens a futures position, the exchange requires a deposit called the **initial margin**. This is not a down payment on the asset; it is a performance bond ensuring the trader can absorb potential losses. The initial margin is typically a small fraction of the contract's notional value.

The exchange also sets a **maintenance margin**, a lower threshold for the account balance. As long as the margin account stays at or above the maintenance level, no action is required. If daily losses push the balance below the maintenance margin, the trader receives a **margin call** and must deposit enough funds to restore the account to the initial margin level. Failure to meet the margin call allows the broker to liquidate the position.

---

## Daily Settlement Mechanics

Let $F_t$ denote the futures settlement price at the end of day $t$. A trader who is long one contract experiences a daily cash flow of

$$
\Delta_t = F_t - F_{t-1}
$$

where $F_{t-1}$ is the previous day's settlement price (or the entry price on day 0). If $\Delta_t > 0$ the long side gains; if $\Delta_t < 0$ the long side loses. The margin account balance $M_t$ at the end of day $t$ is

$$
M_t = M_{t-1} + \Delta_t + D_t
$$

where $D_t \geq 0$ is any deposit made in response to a margin call. A margin call is triggered whenever $M_{t-1} + \Delta_t$ falls below the maintenance margin.

!!! info "Settlement Price vs Market Price"
    The settlement price $F_t$ is not simply the last traded price of the day. It is an **official closing value** determined by the exchange using a specific calculation window near market close. The settlement price serves as the authoritative reference for daily mark-to-market, margin calculations, and end-of-day P&L reporting. It can differ — sometimes significantly — from the price at which the contract last traded during the session.

---

## Worked Example: Three-Day Margin Account

A trader goes long one gold futures contract at a price of \$2{,}000 per ounce. Each contract covers 100 ounces, so the notional value is \$200{,}000. The initial margin is \$10{,}000 and the maintenance margin is \$7{,}500.

| Day | Settlement price | Price change | Daily P&L (100 oz) | Margin before deposit | Margin call? | Deposit | Margin after deposit |
|---|---|---|---|---|---|---|---|
| 0 | \$2{,}000 | — | — | \$10{,}000 | No | \$0 | \$10{,}000 |
| 1 | \$1{,}997 | $-\$3$ | $-\$300$ | \$9{,}700 | No | \$0 | \$9{,}700 |
| 2 | \$1{,}993 | $-\$4$ | $-\$400$ | \$9{,}300 | No | \$0 | \$9{,}300 |
| 3 | \$1{,}978 | $-\$15$ | $-\$1{,}500$ | \$7{,}800 | No | \$0 | \$7{,}800 |

Now suppose instead that on Day 3 the price drops to \$1{,}970 (a change of $-\$23$ from Day 2):

| Day | Settlement price | Price change | Daily P&L (100 oz) | Margin before deposit | Margin call? | Deposit | Margin after deposit |
|---|---|---|---|---|---|---|---|
| 3 | \$1{,}970 | $-\$23$ | $-\$2{,}300$ | \$7{,}000 | **Yes** | \$3{,}000 | \$10{,}000 |

The margin balance of \$7{,}000 falls below the maintenance level of \$7{,}500, triggering a margin call. The trader must deposit \$3{,}000 to restore the account to the initial margin of \$10{,}000.

---

## Counterparty Risk and the Role of the Clearinghouse

Because gains and losses are settled in cash every day, no large unrealized obligation accumulates over the life of the contract. If a trader cannot meet a margin call, the position is closed immediately and the loss is limited to one day's adverse move. The clearinghouse, acting as the counterparty to every trade, therefore faces only overnight exposure rather than the full maturity exposure that arises in a forward contract. This is why marking to market is said to **virtually eliminate counterparty risk** in futures markets.

??? example "April 2020: When the Margin System Was Tested"
    On April 20, 2020, the front-month WTI crude oil contract (CLK20, May 2020) settled at $-\$37.63$ per barrel — the first time a major commodity futures contract traded at a negative price. The collapse was driven by COVID-19 demand destruction, nearly full storage at the Cushing delivery point, and expiration pressure on traders who could not take physical delivery.

    The margin system operated as designed: as prices plunged, margin calls were triggered on long positions throughout the day, and brokers liquidated accounts that could not meet the calls. The clearinghouse's exposure remained limited to intraday price movement rather than the full cumulative loss over the contract's life. However, the event revealed that standard margin models had assumed a non-negative price floor — an assumption that negative prices spectacularly violated, prompting exchanges to revise their risk models.

---

## Comparison with Forward Contracts

Recall (see [§ Futures vs Forwards](futures_vs_forwards.md)): a forward has no intermediate cash flows — the full payoff $S_T - K$ is exchanged once at maturity, exposing the winning party to default risk for the contract's entire life. Daily settlement of futures replaces that single large payment with a sequence of small daily payments, converting **credit risk** into **liquidity risk** (the need to fund margin calls promptly).

---

## Exercises

**Exercise 1.** A trader goes long one crude oil futures contract (1{,}000 barrels) at \$75 per barrel. The initial margin is \$5{,}000 and the maintenance margin is \$3{,}750. Over three days the settlement prices are \$74.50, \$73.80, and \$74.60. Compute the margin account balance at the end of each day and determine whether any margin calls occur.

??? success "Solution to Exercise 1"
    Day 1: P&L $= (74.50 - 75.00) \times 1{,}000 = -\$500$. Balance $= 5{,}000 - 500 = \$4{,}500$. No margin call ($4{,}500 > 3{,}750$).

    Day 2: P&L $= (73.80 - 74.50) \times 1{,}000 = -\$700$. Balance $= 4{,}500 - 700 = \$3{,}800$. No margin call ($3{,}800 > 3{,}750$).

    Day 3: P&L $= (74.60 - 73.80) \times 1{,}000 = +\$800$. Balance $= 3{,}800 + 800 = \$4{,}600$. No margin call.

    The margin balance remains above the maintenance level throughout, so no margin call is triggered.

---

**Exercise 2.** Using the same setup as Exercise 1, suppose the Day 2 settlement price is \$72.00 instead of \$73.80. Determine whether a margin call occurs on Day 2, and if so, compute the required deposit and the margin balance after the deposit.

??? success "Solution to Exercise 2"
    Day 1: P&L $= (74.50 - 75.00) \times 1{,}000 = -\$500$. Balance $= 5{,}000 - 500 = \$4{,}500$.

    Day 2: P&L $= (72.00 - 74.50) \times 1{,}000 = -\$2{,}500$. Balance before deposit $= 4{,}500 - 2{,}500 = \$2{,}000$.

    Since $\$2{,}000 < \$3{,}750$, a margin call is triggered. The trader must deposit $5{,}000 - 2{,}000 = \$3{,}000$ to restore the account to the initial margin. Balance after deposit $= \$5{,}000$.

---

**Exercise 3.** Explain why a futures contract has lower counterparty risk than a forward contract with the same maturity and underlying asset. In your answer, identify the role of daily settlement and the clearinghouse.

??? success "Solution to Exercise 3"
    In a forward contract, the entire gain or loss accumulates over the life of the contract and is settled in a single payment at maturity. The winning party bears the risk that the counterparty will be unable or unwilling to pay.

    In a futures contract, marking to market settles gains and losses daily. If a trader's margin account falls below the maintenance level and the trader fails to meet the margin call, the clearinghouse closes the position immediately. The maximum exposure is therefore limited to roughly one day's price movement rather than the cumulative movement over the entire contract life.

    The clearinghouse further reduces risk by acting as the counterparty to every trade, mutualizing residual risk across all market participants through a guarantee fund.

---

**Exercise 4.** A trader is short one S&P 500 futures contract at 5{,}200, with a contract multiplier of \$50. The initial margin is \$12{,}000 and the maintenance margin is \$10{,}000. Over two days the settlement prices are 5{,}220 and 5{,}190. Compute the margin balance at the end of each day. Does a margin call occur?

??? success "Solution to Exercise 4"
    A short position profits when the price falls. The daily P&L for the short is $(F_{t-1} - F_t) \times 50$.

    Day 1: P&L $= (5{,}200 - 5{,}220) \times 50 = -20 \times 50 = -\$1{,}000$. Balance $= 12{,}000 - 1{,}000 = \$11{,}000$. No margin call ($11{,}000 > 10{,}000$).

    Day 2: P&L $= (5{,}220 - 5{,}190) \times 50 = 30 \times 50 = +\$1{,}500$. Balance $= 11{,}000 + 1{,}500 = \$12{,}500$. No margin call.

    No margin call is triggered on either day. The Day 1 loss from the price increase is more than offset by the Day 2 gain from the price decrease.

---

**Exercise 5.** A trader goes long one micro E-mini S&P 500 futures (MES, multiplier \$5) at 5{,}000. The initial margin is \$1{,}500 and the maintenance margin is \$1{,}200. Over four days the settlement prices are 4{,}980, 4{,}930, 4{,}900, and 4{,}950. Compute the margin balance at the end of each day, identify the day a margin call is triggered, and compute the required deposit.

??? success "Solution to Exercise 5"
    Daily P&L for the long is $(F_t - F_{t-1}) \times 5$.

    Day 1: $(4{,}980 - 5{,}000) \times 5 = -\$100$. Balance $= 1{,}500 - 100 = \$1{,}400$. No call.

    Day 2: $(4{,}930 - 4{,}980) \times 5 = -\$250$. Balance $= 1{,}400 - 250 = \$1{,}150$. **Margin call** ($1{,}150 < 1{,}200$). Deposit $= 1{,}500 - 1{,}150 = \$350$. Balance after deposit $= \$1{,}500$.

    Day 3: $(4{,}900 - 4{,}930) \times 5 = -\$150$. Balance $= 1{,}500 - 150 = \$1{,}350$. No call.

    Day 4: $(4{,}950 - 4{,}900) \times 5 = +\$250$. Balance $= 1{,}350 + 250 = \$1{,}600$. No call.

---

**Exercise 6.** Daily mark-to-market converts a single large terminal payment into a stream of small daily payments. State two ways this benefits the clearinghouse, and one situation in which it can harm an otherwise solvent trader.

??? success "Solution to Exercise 6"
    Two benefits to the clearinghouse:

    1. **Bounded credit exposure.** A defaulting trader can owe at most roughly one day's adverse move, not the full contract maturity exposure.
    2. **Early detection of stress.** Inability to meet a margin call signals trouble immediately, allowing the clearinghouse to liquidate the position before losses accumulate beyond the posted margin.

    Harm to a solvent trader: **liquidity stress**. A trader with a correct long-horizon thesis may be forced to liquidate a position (or post substantial additional collateral on short notice) after a transient adverse move, even though the position would have been profitable held to maturity. The 2020 negative-WTI episode is an extreme example — long-position traders who could not fund margin calls intraday were forcibly closed out at the lows.
