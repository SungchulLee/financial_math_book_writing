# Synthetic Positions

**Synthetic positions** use combinations of options (calls and puts) to **replicate the payoff of other assets or strategies**, most commonly **stock-like exposure**, without directly trading the underlying. They rely on **put–call parity** and are fundamental to understanding how options encode forward prices, leverage, and financing.

---

## The Core Insight

**The fundamental idea:**
- Calls and puts are not independent
- Their prices are linked by **put–call parity**
- By combining options, you can **recreate stock, short stock, or forward contracts**
- These positions often behave almost identically to the underlying
- Differences come from financing, dividends, and early-exercise features

**The key equation (put–call parity):**
\[
C - P = S - K e^{-rT}
\]

Rearranged:
\[
S = C - P + K e^{-rT}
\]

This identity is the mathematical foundation of all synthetic positions.

---

## What Is a Synthetic Position?

A **synthetic** is a position constructed from options that **replicates the payoff** of another position at expiration (and often approximately before expiration).

**Key idea:**
> If two portfolios have the same payoff in all states, they must have the same price (no-arbitrage).

---

## Why Synthetics Exist

### 1. Capital Efficiency
You may want stock exposure without:
- paying full share price
- tying up capital
- triggering taxes or restrictions

Synthetics can replicate exposure with **less upfront cash**.

### 2. Structural Constraints
- Shorting stock may be impossible or expensive
- Certain accounts may restrict stock transactions
- Options may be more liquid than shares

### 3. Hedging and Risk Transfer
Institutions frequently use synthetics to:
- hedge large positions
- convert exposure without trading the underlying
- neutralize dividends or financing effects

---

## Core Synthetic Positions

### 1) Synthetic Long Stock

**Replicates:** owning the stock

#### Structure
- **Buy 1 call**
- **Sell 1 put**
- Same strike \(K\), same expiration \(T\)

\[
\text{Synthetic Long Stock} = +C(K,T) - P(K,T)
\]

#### Payoff at Expiration
\[
\max(S-K,0) - \max(K-S,0) = S - K
\]

Linear, stock-like payoff.

#### Interpretation
- Delta ≈ +1
- Unlimited upside
- Downside similar to owning stock (below strike)

---

### 2) Synthetic Short Stock

**Replicates:** shorting the stock

#### Structure
- **Sell 1 call**
- **Buy 1 put**
- Same strike and expiration

\[
\text{Synthetic Short Stock} = -C(K,T) + P(K,T)
\]

#### Payoff at Expiration
\[
-(S-K) = K - S
\]

#### Interpretation
- Delta ≈ −1
- Unlimited downside risk (like short stock)
- Profits if stock falls

---

### 3) Synthetic Forward Contract

From parity:
\[
C - P = S - K e^{-rT}
\]

So:
- Long call + short put ≈ **long forward**
- Strike-adjusted cash position completes equivalence

This is heavily used in institutional pricing.

---

## The Portfolio View

### Synthetic Long Stock
\[
\Pi = C(K,T) - P(K,T)
\]

**Greeks (approximate):**
- Delta: ≈ +1
- Gamma: near 0 (away from ATM)
- Theta: small (call theta − put theta)
- Vega: small (call vega − put vega)

### Synthetic Short Stock
\[
\Pi = -C(K,T) + P(K,T)
\]

Greeks mirror synthetic long stock with opposite signs.

---

## Concrete Example 1: Synthetic Long Stock

**Setup:**
- Stock at \(S = 100\)
- 3-month options
- Strike \(K = 100\)

**Trade:**
- Buy $100 call for $5
- Sell $100 put for $5

**Net cost:** ~$0 (ignoring interest/dividends)

### Outcomes at Expiration

| Stock Price | Call | Put | Net Payoff |
|------------|------|-----|------------|
| 80 | 0 | -20 | -20 |
| 100 | 0 | 0 | 0 |
| 120 | 20 | 0 | +20 |

**Identical to owning stock from $100.**

---

## Concrete Example 2: Synthetic Short Stock

**Setup:**
- Stock at \(S = 100\)
- Same options

**Trade:**
- Sell $100 call for $5
- Buy $100 put for $5

### Outcomes

| Stock Price | Call | Put | Net Payoff |
|------------|------|-----|------------|
| 80 | 0 | +20 | +20 |
| 100 | 0 | 0 | 0 |
| 120 | -20 | 0 | -20 |

Identical to shorting stock from $100.

---

## Strike Selection

### ATM Synthetics (Most Common)
- Best replication of stock
- Delta ≈ ±1
- Most liquid options
- Most accurate parity behavior

### ITM / OTM Synthetics
- Still work mathematically
- Different capital requirements
- Delta deviates slightly from ±1
- Used for fine-tuning exposure

---

## Time Selection

### Short-Dated
- Tracks stock closely
- Higher gamma near expiration
- More sensitive to price moves

### Longer-Dated
- Smoother behavior
- Less gamma
- Often preferred for long-term exposure

---

## Synthetics vs. Stock

| Aspect | Synthetic | Stock |
|------|-----------|-------|
| Capital | Lower upfront | Full share price |
| Dividends | Indirect (priced in) | Received directly |
| Voting rights | None | Yes |
| Margin | Often required | None (cash account) |
| Flexibility | High | Lower |

**Key insight:** synthetics replicate **price exposure**, not ownership benefits.

---

## Practical Applications

### 1) Replacing Stock Exposure
- Want delta ≈ 1
- Less capital tied up
- Easy to adjust or close

### 2) Avoiding Short-Sale Constraints
- Hard-to-borrow stock
- Use synthetic short instead

### 3) Transition Trades
- Convert stock → options exposure (or vice versa)
- Maintain risk while restructuring portfolio

---

## Risks and Caveats

### 1) Assignment Risk
- Short option leg can be assigned
- Leads to temporary stock position
- Must be managed proactively

### 2) Dividend Effects
- Dividends affect put–call parity
- Early assignment risk increases near ex-dividend dates

### 3) Financing Differences
- Interest rates embedded in option prices
- Synthetic may not be exactly free

### 4) Margin Requirements
- Brokers may require margin similar to stock exposure
- Not “free leverage” in practice

---

## Common Mistakes

### 1) Forgetting Dividends
Parity assumes known dividends.
Ignoring them causes mispricing expectations.

### 2) Treating Synthetics as Limited Risk
Synthetic long stock has **full downside risk**.
Synthetic short stock has **unlimited risk**.

### 3) Ignoring Early Exercise
American options break exact parity before expiration.

---

## When to Use Synthetics

### Best Use Cases
- You want stock-like exposure without stock
- You need flexibility and fast adjustments
- You understand assignment and margin mechanics

### Avoid When
- You want dividends or voting rights
- You cannot manage assignment risk
- Liquidity is poor

---

## Summary

Synthetic positions reveal the **true structure of options markets**:
- Calls, puts, and stock are tightly linked
- Options are not “side bets” — they encode forwards and financing
- Understanding synthetics is essential for:
  - advanced spreads
  - arbitrage intuition
  - professional options trading

Master synthetics, and the rest of options theory becomes much clearer.
